from packets.clientbountpackets import ClientBoundPacket
from packets.packet import PacketDirection, PacketMode
from datatypes.datatypes import DataTypes
from packets.packetreader import PacketReader

class StatusResponsePacket(ClientBoundPacket):
    PACKET_ID = b'\x00'
    DIRECTION = PacketDirection.CLIENT
    MODE = PacketMode.STATUS
    NEXT_MODE = PacketMode.STATUS

    def __init__(self, raw_data: bytes) -> None:
        super().__init__(raw_data)
    
    def _fmt(self):
        fmt = [
            DataTypes.STRING
        ]

        return fmt
