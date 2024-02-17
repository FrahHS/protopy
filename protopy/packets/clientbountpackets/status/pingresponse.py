import time

from datatypes.datatypes import DataTypes
from packets.clientbountpackets import ClientBoundPacket
from packets.packet import PacketDirection, PacketMode
from packets.packetreader import PacketReader

class PingResponsePacket(ClientBoundPacket):
    PACKET_ID = b'\x01'
    DIRECTION = PacketDirection.CLIENT
    MODE = PacketMode.STATUS
    NEXT_MODE = PacketMode.STATUS

    def __init__(self, raw_data: bytes) -> None:
        super().__init__(raw_data)
    
    def _fmt(self):
        fmt = [
            DataTypes.LONG
        ]

        return fmt

    @property
    def ping(self):
        return round(time.time() * 1000) - self.response[0]
