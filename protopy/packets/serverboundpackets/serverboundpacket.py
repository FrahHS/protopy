from abc import ABC, abstractmethod

from protopy.packets import Packet
from protopy.datatypes.buffer import Buffer

class ServerBoundPacket(Packet, ABC):
    def __init__(self, is_compressed) -> None:
        super().__init__(is_compressed)

    @abstractmethod
    def _write(self):
        pass

    def pack(self, packet_id: bytes, raw_data: bytes, compression: bool = False,) -> None:
        packet = Buffer()
        if(compression):
            #TODO: Handle zlib compression
            packet.write(b'\x00')
            packet.write(packet_id)
            packet.write(raw_data)
        else:
            packet.write(packet_id)
            packet.write(raw_data)

        return Packet.data_pack(packet.data)

    def packet(self, compression: bool = False) -> bytes:
        packet = self._write()
        return self.pack(self.PACKET_ID, packet, compression)
