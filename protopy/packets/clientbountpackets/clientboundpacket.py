from abc import ABC, abstractmethod

from packets.packet import Packet
from packets.packetreader import PacketReader

class ClientBoundPacket(Packet, ABC):
    def __init__(self, raw_data: bytes) -> None:
        self.raw_data = raw_data
        self._read()

    @abstractmethod
    def _fmt(self):
        pass

    def _read(self):
        fmt = self._fmt()
        packet_reader = PacketReader()
        self.response = packet_reader.read(fmt, self.raw_data, self.MODE)

