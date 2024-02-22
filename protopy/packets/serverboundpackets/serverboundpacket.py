from abc import ABC, abstractmethod

from protopy.packets import Packet
from protopy.packets.buffer import Buffer

class ServerBoundPacket(Packet, ABC):
    def __init__(self, is_compressed) -> None:
        super().__init__(is_compressed)

    @abstractmethod
    def _write(self):
        pass

    def pack(self, raw_data: bytes) -> None:
        packet = Buffer()
        if(self.is_compressed):
            #TODO: Handle zlib compression
            packet.write(b'\x00')
            packet.write(self.PACKET_ID)
            packet.write(raw_data)
        else:
            packet.write(self.PACKET_ID)
            packet.write(raw_data)

        return Packet.data_pack(packet.data)

    def packet(self) -> bytes:
        packet = self._write()
        return self.pack(packet)
