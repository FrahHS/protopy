import socket
from threading import Thread
from protopy.datatypes.varint import Varint

from protopy.packets.packetreader import PacketReader
from protopy.packets.packet import Packet, PacketMode, UnknowPacket
from protopy.packets.clientbountpackets import SetCompressionPacket
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

        self._stream = b''
        self._mode = PacketMode.HANDSHAKING
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self) -> None:
        try:
            self._socket.connect((self.host, self.port))
            self.is_connected = True
            Thread(target=lambda: self._listen()).start()
            Thread(target=lambda: self._split_packets()).start()
        except ConnectionRefusedError:
            logger.warning("Server is not online")
            exit()

    def close(self) -> None:
        self.is_connected = False
        self._socket.close()

    def sendPacket(self, packet: Packet) -> None:
        self._mode = packet.NEXT_MODE
        packet.is_compressed = self.compression
        raw_data = packet.packet()
        self._socket.sendall(raw_data)

    def _receive(self) -> bytes:
        return self._socket.recv(self.buffer_size)

    def _packets_handler(self, packet: Packet):
        # Set connection mode
        if(not isinstance(packet, UnknowPacket)):
            self._mode = packet.NEXT_MODE

        # Call listeners
        self.call_packet_listeners(packet)

    def _split_packets(self):
        while self.is_connected:
            if self._stream != b'':
                lenght, body = Varint.unpack(self._stream)
                if len(body) >= lenght:
                    self._stream = body
                    raw_data = Varint.pack(lenght) + self._stream[:lenght]

                    # Build received packet
                    packet_reader = PacketReader(compression=self.compression)
                    packet = packet_reader.build_packet_from_raw_data(raw_data, self._mode, self.compression)

                    # Handle packet
                    self._packets_handler(packet)
                    self._stream = self._stream[lenght:]

    def _listen(self) -> None:
        while self.is_connected:
            if data := self._receive():
                self._stream += data
            else:
                if self.is_connected:
                    self.is_connected = False
                    logger.info("Connection Lost.")

    def listener(self):
        def inner(func):
            self.add_listener(func)
            return func
        return inner

    def add_listener(self, func):
        self.packets_listeners.append(func)

    def dispose_listener(self, func):
        self.packets_listeners.remove(func)

    def call_packet_listeners(self, packet):
        for func in self.packets_listeners:
            func(packet)
