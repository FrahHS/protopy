from protopy.packets.clientbountpackets import ClientBoundPacket
from protopy.packets.packet import PacketMode


class DisconnectPlayPacket(ClientBoundPacket):
    packet_id = b"\x1B"
    mode = PacketMode.PLAY

    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(
            raw_data=raw_data,
            is_compressed=is_compressed,
        )

    def _read(self, body):
        res = self.packet_reader.read_string(body[15:])[0]
        self.response["reason"] = res

    @property
    def reason(self):
        return self.response["reason"]
