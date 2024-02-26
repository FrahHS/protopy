from protopy.packets.clientbountpackets import ClientBoundPacket
from protopy.packets.packet import PacketMode


class LoginSuccessPacket(ClientBoundPacket):
    packet_id = b"\x02"
    mode = PacketMode.LOGIN

    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(
            raw_data=raw_data,
            is_compressed=is_compressed,
        )

    def _read(self, body):
        res, body = self.packet_reader.read_uuid(body)
        self.response["uuid"] = res

        res, body = self.packet_reader.read_string(body)
        self.response["username"] = res

        res, body = self.packet_reader.read_string(body)
        self.response["number_of_proprieties"] = res

    @property
    def uuid(self):
        return self.response["uuid"]

    @property
    def username(self):
        return self.response["username"]

    @property
    def number_of_proprieties(self):
        return self.response["number_of_proprieties"]
