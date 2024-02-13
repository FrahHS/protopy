import time

from datatypes.datatypes import DataTypes
from packets.packet import Packet, PacketDirection, PacketMode
from packets.packetreader import PacketReader

class PingResponsePacket(Packet):
    PACKET_ID = b'\x01'
    DIRECTION = PacketDirection.CLIENT
    MODE = PacketMode.STATUS
    NEXT_MODE = PacketMode.STATUS

    def __init__(self, raw_data: bytes) -> None:
        self.raw_data = raw_data

        fmt = [
            DataTypes.LONG
        ]

        packet_reader = PacketReader()
        self.response = packet_reader.read(fmt, raw_data, self.MODE)

    @property
    def ping(self):
        return round(time.time() * 1000) - self.response[0]
