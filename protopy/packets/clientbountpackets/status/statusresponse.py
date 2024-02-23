from protopy.packets.clientbountpackets import ClientBoundPacket
from protopy.packets.packet import PacketMode

class StatusResponsePacket(ClientBoundPacket):
    packet_id = b'\x00'
    mode = PacketMode.STATUS

    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(
            raw_data = raw_data,
            is_compressed = is_compressed,
        )

    def _read(self, body):
        res, body = self.packet_reader.read_string(body)
        self.response['json_response'] = res

    @property
    def json_response(self):
        return self.response['json_response']
