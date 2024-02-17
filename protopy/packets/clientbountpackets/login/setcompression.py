from datatypes.datatypes import DataTypes
from packets.clientbountpackets import ClientBoundPacket
from packets.packet import PacketDirection, PacketMode
from packets.packetreader import PacketReader

class SetCompressionPacket(ClientBoundPacket):
    PACKET_ID = b'\x03'
    DIRECTION = PacketDirection.CLIENT
    MODE = PacketMode.LOGIN
    NEXT_MODE = PacketMode.LOGIN

    def __init__(self, raw_data: bytes) -> None:
        super().__init__(raw_data)
    
    def _fmt(self):
        fmt = [
            DataTypes.VARINT
        ]

        return fmt

    @property
    def threshold(self):
        return self.response[0]
