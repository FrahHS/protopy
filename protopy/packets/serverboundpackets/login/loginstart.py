from uuid import UUID

from protopy.datatypes.buffer import Buffer
from protopy.packets.serverboundpackets import ServerBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode

class LoginStartPacket(ServerBoundPacket):
    PACKET_ID = b'\x00'
    DIRECTION = PacketDirection.SERVER
    MODE = PacketMode.LOGIN
    NEXT_MODE = PacketMode.LOGIN

    def __init__(self, name: str, player_uuid: UUID) -> None:
        self.name = name
        self.player_uuid = player_uuid

    def _write(self):
        buffer = Buffer()
        buffer.write_string(self.name)
        buffer.write_uuid(self.player_uuid)

        return buffer
