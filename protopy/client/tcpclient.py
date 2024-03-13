import inspect
import socket
from threading import Thread
import time
from protopy.datatypes.varint import Varint

from protopy.packets.packetreader import PacketReader
from protopy.packets.packet import Packet, PacketMode, UnknowPacket
from protopy.utils import logger


class TcpClient:
    def __init__(self, host: str, port: int, buffer_size: int = 1024) -> None:
        self.host = host
        self.port = port
        self.buffer_size = buffer_size

        self.packets_listeners = []
        self.is_connected = False
        self.compression = False
        self.threshold = 0

        self._stream = b""
        self._mode = PacketMode.HANDSHAKING
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self) -> None:
        try:
            self._socket.connect((self.host, self.port))
            self.is_connected = True
            Thread(name="Packet listeners", target=lambda: self._listen()).start()
            Thread(name="Packet analyzer", target=lambda: self._split_packets()).start()
        except ConnectionRefusedError:
            logger.warning("Server is not online")
            exit()

    def close(self) -> None:
        self.is_connected = False
        self._socket.close()

    def sendPacket(self, packet: Packet) -> None:
        self._mode = packet.next_mode
        packet.is_compressed = self.compression
        raw_data = packet.packet()
        self._socket.sendall(raw_data)

    def _receive(self) -> bytes:
        return self._socket.recv(self.buffer_size)

    def _packets_handler(self, packet: Packet):
        # Set connection mode
        if not isinstance(packet, UnknowPacket):
            self._mode = packet.next_mode

        # Call listeners
        self.call_packet_listeners(packet)

    def _split_packets(self):
        while self.is_connected:
            if self._stream != b"":
                lenght, body = Varint.unpack(self._stream)
                if len(body) >= lenght:
                    self._stream = body
                    raw_data = Varint.pack(lenght) + self._stream[:lenght]

                    # Build received packet
                    packet_reader = PacketReader(compression=self.compression)
                    packet = packet_reader.build_packet_from_raw_data(
                        raw_data, self._mode, self.compression
                    )

                    # Handle packet
                    self._packets_handler(packet)
                    self._stream = self._stream[lenght:]

    def _listen(self) -> None:
        while self.is_connected:
            if data := self._receive():
                self._stream += data
            else:
                if self.is_connected:
                    logger.info("Connection Lost.")
                    time.sleep(1)
                    self.is_connected = False
                    exit()

    def listener(self):
        def inner(func):
            self.add_listener(func)
            return func

        return inner

    def add_listener(self, func):
        # Check if listener is valid
        if len(inspect.signature(func).parameters) != 1:
            listener_argc = len(inspect.signature(func).parameters)
            raise ListenerError(
                f"listeners must have 1 argument, {listener_argc} found: def {func.__name__}{inspect.signature(func)}:"
            )

        # Get listener packet arg type
        func_args_spec = list(inspect.getfullargspec(func).annotations.values())

        if len(func_args_spec) == 0:
            packet_class = None
        else:
            packet_class = func_args_spec[0]

        # Add listener
        self.packets_listeners.append({"callback": func, "class": packet_class})

    def dispose_listener(self, func):
        self.packets_listeners.remove(func)

    def call_packet_listeners(self, packet: object):
        for cur_listener in self.packets_listeners:
            if isinstance(cur_listener, dict):
                if cur_listener["class"] == packet.__class__:
                    cur_listener["callback"](packet)
                elif cur_listener["class"] is None:
                    cur_listener["callback"](packet)


class ListenerError(Exception):
    pass
