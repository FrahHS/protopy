from protopy.datatypes.datatypes import DataTypes
from protopy.packets.clientbountpackets import ClientBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode
from protopy.utils import logger

class SetCompressionPacket(ClientBoundPacket):
    PACKET_ID = b'\x03'
    DIRECTION = PacketDirection.CLIENT
    MODE = PacketMode.LOGIN
    NEXT_MODE = PacketMode.LOGIN

    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(raw_data, is_compressed)

    def _read(self, body):
        res, body = self.packet_reader.read_varint(body)
        self.response['threshold'] = res

    @property
    def threshold(self):
        return self.response['threshold']
