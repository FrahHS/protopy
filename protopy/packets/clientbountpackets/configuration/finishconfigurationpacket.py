from protopy.packets.clientbountpackets import ClientBoundPacket
from protopy.packets.packet import PacketMode


class ClientBoundFinishConfigurationPacket(ClientBoundPacket):
    packet_id = b"\x02"
    mode = PacketMode.CONFIGURATION

    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(
            raw_data=raw_data,
            is_compressed=is_compressed,
        )

    def _read(self, body):
        pass
