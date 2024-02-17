from datatypes.datatypes import DataTypes
from packets.packet import Packet, PacketDirection, PacketMode
from packets.packetreader import PacketReader

class SetCompressionPacket(Packet):
    PACKET_ID = b'\x03'
    DIRECTION = PacketDirection.CLIENT
    MODE = PacketMode.LOGIN
    NEXT_MODE = PacketMode.LOGIN

    def __init__(self, raw_data: bytes) -> None:
        self.raw_data = raw_data

        fmt = [
            DataTypes.VARINT
        ]

        packet_reader = PacketReader()
        self.response = packet_reader.read(fmt, raw_data, self.MODE)

    @property
    def threshold(self):
        return self.response[0]
