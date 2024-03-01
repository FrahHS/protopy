from abc import ABC, abstractmethod

from protopy.packets.packet import Packet, PacketDirection
from protopy.packets.packetreader import PacketReader


class ClientBoundPacket(Packet, ABC):
    direction = PacketDirection.CLIENT

    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(
            raw_data=raw_data,
            is_compressed=is_compressed,
        )

        self.response = {}
        self.packet_reader = PacketReader(self.is_compressed)
        self.payload = self.packet_reader.get_packet_id_and_data(self.raw_data)[1]

        self._read(self.payload)

    @abstractmethod
    def _read(self, body):
        pass
