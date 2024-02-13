import time

from packets.packet import Packet, PacketDirection, PacketMode
from datatypes.buffer import Buffer

class PingRequestPacket(Packet):
    PACKET_ID = b'\x01'
    DIRECTION = PacketDirection.SERVER
    MODE = PacketMode.STATUS
    NEXT_MODE = PacketMode.STATUS

    @property
    def packet(self) -> bytes:
        buffer = Buffer()
        buffer.write_long(round(time.time() * 1000))

        packet = Buffer()
        packet.write(self.PACKET_ID)
        packet.write(buffer)

        return Packet.data_pack(packet.data)
