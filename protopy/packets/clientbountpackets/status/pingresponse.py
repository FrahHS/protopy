import time

from protopy.datatypes.datatypes import DataTypes
from protopy.packets.clientbountpackets import ClientBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode
from protopy.packets.packetreader import PacketReader

class PingResponsePacket(ClientBoundPacket):
    packet_id = b'\x01'
    mode = PacketMode.STATUS

    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(
            raw_data = raw_data,
            is_compressed = is_compressed,
        )

    def _read(self, body):
        res, body = self.packet_reader.read_long(body)
        self.response['ping'] = res

    @property
    def ping(self):
        return round(time.time() * 1000) - self.response['keep_alive_id']
