from abc import ABC, abstractmethod
import zlib
from protopy.datatypes.varint import Varint

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
            paylaod = self.PACKET_ID + raw_data.data
            if(len(paylaod) >= 256):
                data_lenght = Varint(len(paylaod)).bytes
                compressed_payload = zlib.compress(paylaod, level=9)

                lenght_and_payload = data_lenght + compressed_payload
                header = Varint(len(lenght_and_payload)).bytes

                return header + lenght_and_payload
            else:
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
