from uuid import UUID

from protopy.packets.buffer import Buffer
from protopy.packets.serverboundpackets import ServerBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode

class LoginStartPacket(ServerBoundPacket):
    packet_id = b'\x00'
    mode = PacketMode.LOGIN

    def __init__(self, name: str, player_uuid: UUID, is_compressed: bool = False) -> None:
        super().__init__(
            is_compressed = is_compressed,
        )

        self.name = name
        self.player_uuid = player_uuid

    def _write(self):
        buffer = Buffer()
        buffer.write_string(self.name)
        buffer.write_uuid(self.player_uuid)

        return buffer
