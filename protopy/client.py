import socket
from threading import Thread

from protopy.packets.packetreader import PacketReader
from protopy.packets.packet import Packet, PacketMode
from protopy.packets.clientbountpackets import SetCompressionPacket
from protopy.utils import logger

packets_listeners = []

class Client:
    def __init__(self, host: str, port: int, buffer_size: int = 2097151) -> None:
        self.is_connected = False

        self.host = host
        self.port = port
        self.buffer_size = buffer_size

        self.compression = False
        self.threshold = 0

        self.mode = PacketMode.HANDSHAKING

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self) -> None:
        try:
            self.socket.connect((self.host, self.port))
            self.is_connected = True
            Thread(target=lambda: self.listen()).start()
        except ConnectionRefusedError:
            raise ConnectionError("Server is not online")
    
    def close(self) -> None:
        self.socket.close()
        self.is_connected = False

    def sendPacket(self, packet: Packet) -> None:
        self.mode = packet.NEXT_MODE
        raw_data = packet.packet(self.compression)
        self.socket.sendall(raw_data)

    def receive(self) -> bytes:
        return self.socket.recv(self.buffer_size)

    def listen(self) -> None:
        while self.is_connected:
            data = self.receive()
            if data:
                # Build received packet
                packet_reader = PacketReader(compression=self.compression)

                packet = packet_reader.build_packet_from_raw_data(data, self.mode, self.compression)

                # Check for compression
                if(isinstance(packet, SetCompressionPacket)):
                    self.compression = True
                    self.threshold = packet.threshold

                # Call listeners
                self.call_packet_listeners(packet)
                # TODO:
                #self.mode = packet.nextMode
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
