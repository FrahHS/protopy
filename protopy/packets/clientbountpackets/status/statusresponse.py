from protopy.packets.clientbountpackets import ClientBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode
from protopy.datatypes.datatypes import DataTypes
from protopy.packets.packetreader import PacketReader

class StatusResponsePacket(ClientBoundPacket):
    PACKET_ID = b'\x00'
    DIRECTION = PacketDirection.CLIENT
    MODE = PacketMode.STATUS
    NEXT_MODE = PacketMode.STATUS

    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(raw_data, is_compressed)
    
    def _fmt(self):
        fmt = [
            DataTypes.STRING
        ]

        return fmt
