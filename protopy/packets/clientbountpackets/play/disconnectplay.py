from protopy.datatypes.datatypes import DataTypes
from protopy.packets.clientbountpackets import ClientBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode

class DisconnectPlayPacket(ClientBoundPacket):
    PACKET_ID = b'\x1B'
    DIRECTION = PacketDirection.CLIENT
    MODE = PacketMode.PLAY
    NEXT_MODE = PacketMode.PLAY

    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(raw_data, is_compressed)

    def _read(self, body):
        res, body = self.packet_reader.read_string(body[15:])
        self.response['reason'] = res

    @property
    def reason(self):
        return self.response['reason']
