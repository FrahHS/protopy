from packets.packet import Packet, PacketDirection, PacketMode
from datatypes.buffer import Buffer

class StatusRequestPacket(Packet):
    PACKET_ID = b'\x00'
    DIRECTION = PacketDirection.SERVER
    MODE = PacketMode.STATUS
    NEXT_MODE = PacketMode.STATUS

    @property
    def packet(self) -> bytes:
        packet = Buffer()
        packet.write(b'\x00')

        return Packet.data_pack(packet.data)
