from uuid import UUID

from datatypes.buffer import Buffer
from packets.packet import Packet, PacketDirection, PacketMode

class LoginStartPacket(Packet):
    PACKET_ID = b'\x00'
    DIRECTION = PacketDirection.SERVER
    MODE = PacketMode.LOGIN
    NEXT_MODE = PacketMode.LOGIN

    def __init__(self, name: str, player_uuid: UUID) -> None:
        self.name = name
        self.player_uuid = player_uuid

    def write(self):
        buffer = Buffer()
        buffer.write_string(self.name)
        buffer.write_uuid(self.player_uuid)

        return buffer

    def packet(self, compression: bool = False) -> bytes:
        packet = self.write()
        return self.pack(self.PACKET_ID, packet, compression)
