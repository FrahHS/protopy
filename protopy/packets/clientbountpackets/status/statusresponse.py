from packets.packet import Packet, PacketDirection, PacketMode
from datatypes.datatypes import DataTypes
from packets.packetreader import PacketReader

class StatusResponsePacket(Packet):
    PACKET_ID = b'\x00'
    DIRECTION = PacketDirection.CLIENT
    MODE = PacketMode.STATUS
    NEXT_MODE = PacketMode.STATUS

    def __init__(self, raw_data: bytes) -> None:
        self.raw_data = raw_data

        fmt = [
            DataTypes.STRING
        ]

        packet_reader = PacketReader()
        self.response = packet_reader.read(fmt, raw_data, self.MODE)
