from protopy.packets.clientbountpackets import ClientBoundPacket
from protopy.packets.packet import PacketMode

class ClientboundKeepAlivePacket(ClientBoundPacket):
    packet_id = b'\x24'
    mode = PacketMode.PLAY

    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(
            raw_data = raw_data,
            is_compressed = is_compressed,
        )

    def _read(self, body):
        res, body = self.packet_reader.read_long(body)
        self.response['keep_alive_id'] = res

    @property
    def keep_alive_id(self):
        return self.response['keep_alive_id']
