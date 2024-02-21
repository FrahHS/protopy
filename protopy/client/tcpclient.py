import socket
from threading import Thread
from protopy.datatypes.varint import Varint

from protopy.packets.packetreader import PacketReader
from protopy.packets.packet import Packet, PacketMode, UnknowPacket
from protopy.packets.clientbountpackets import SetCompressionPacket
from protopy.utils import logger

packets_listeners = []

class TcpClient:
    def __init__(self, host: str, port: int, buffer_size: int = 2097151) -> None:
        self.is_connected = False

        self.host = host
        self.port = port
        self.buffer_size = buffer_size

        self.compression = False
        self.threshold = 0

        self.stream = b''

        self.mode = PacketMode.HANDSHAKING

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self) -> None:
        try:
            self.socket.connect((self.host, self.port))
            self.is_connected = True
            Thread(target=lambda: self.listen()).start()
            Thread(target=lambda: self.split_packets()).start()
        except ConnectionRefusedError:
            raise ConnectionError("Server is not online")

    def close(self) -> None:
        self.is_connected = False
        self.socket.close()

    def sendPacket(self, packet: Packet) -> None:
        logger.debug(f'[PACKET SENT] packet_id: {packet.PACKET_ID}')
        self.mode = packet.NEXT_MODE
        packet.is_compressed = self.compression
        raw_data = packet.packet()
        self.socket.sendall(raw_data)

    def receive(self) -> bytes:
        return self.socket.recv(self.buffer_size)

    def packets_handler(self, data):
        # Build received packet
        packet_reader = PacketReader(compression=self.compression)

        packet = packet_reader.build_packet_from_raw_data(data, self.mode, self.compression)

        # Check for compression
        if(isinstance(packet, SetCompressionPacket)):
            self.compression = True
            self.threshold = packet.threshold

        if(not isinstance(packet, UnknowPacket)):
            self.mode = packet.NEXT_MODE

        # Call listeners
        self.call_packet_listeners(packet)

    def split_packets(self):
        while self.is_connected:
            if self.stream != b'':
                lenght, self.stream = Varint.unpack(self.stream)
                self.packets_handler(Varint.pack(lenght) + self.stream[:lenght])
                self.stream = self.stream[lenght:]

    def listen(self) -> None:
        while self.is_connected:
            if data := self.receive():
                self.stream += data
            else:
                if self.is_connected:
                    self.is_connected = False
                    logger.info("Connection Lost.")

    def listener(self):
        def inner(func):
            packets_listeners.append(func)
            return func
        return inner

    def call_packet_listeners(self, packet):
        for func in packets_listeners:
            func(packet)
