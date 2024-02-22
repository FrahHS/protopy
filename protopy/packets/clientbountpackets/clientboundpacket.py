from abc import ABC, abstractmethod

from protopy.packets.packet import Packet
from protopy.packets.packetreader import PacketReader

class ClientBoundPacket(Packet, ABC):
    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(is_compressed)
        self.raw_data = raw_data

        self.packet_reader = PacketReader(self.is_compressed)
        id, self.payload = self.packet_reader.get_packet_id_and_data(self.raw_data)
        self.response = {}
        self._read(self.payload)

    @abstractmethod
    def _read(self, body):
        pass
