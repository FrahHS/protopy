from protopy.packets.clientbountpackets import ClientBoundPacket
from protopy.packets.packet import PacketMode


class SetCompressionPacket(ClientBoundPacket):
    packet_id = b"\x03"
    mode = PacketMode.LOGIN

    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(
            raw_data=raw_data,
            is_compressed=is_compressed,
        )

    def _read(self, body):
        res, body = self.packet_reader.read_varint(body)
        self.response["threshold"] = res

    @property
    def threshold(self):
        return self.response["threshold"]
