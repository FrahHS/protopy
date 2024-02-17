from protopy.datatypes.datatypes import DataTypes
from protopy.packets.clientbountpackets import ClientBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode
from protopy.packets.packetreader import PacketReader

class LoginSuccessPacket(ClientBoundPacket):
    PACKET_ID = b'\x02'
    DIRECTION = PacketDirection.CLIENT
    MODE = PacketMode.LOGIN
    NEXT_MODE = PacketMode.LOGIN

    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(raw_data, is_compressed)
    
    def _fmt(self):
        fmt = [
            DataTypes.UUID,
            DataTypes.STRING,
            DataTypes.VARINT
        ]

        return fmt
