from abc import ABC, abstractmethod

from protopy.packets.packet import Packet
from protopy.packets.packetreader import PacketReader

class ClientBoundPacket(Packet, ABC):
    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(is_compressed)
        self.raw_data = raw_data
        self._read()

    @abstractmethod
    def _fmt(self):
        pass

    def _read(self):
        fmt = self._fmt()
        packet_reader = PacketReader(self.is_compressed)
        self.response = packet_reader.read(fmt, self.raw_data, self.MODE)

