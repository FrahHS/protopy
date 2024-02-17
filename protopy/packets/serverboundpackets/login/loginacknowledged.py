from protopy.datatypes.buffer import Buffer
from protopy.packets.serverboundpackets import ServerBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode

class LoginAcknowledged(ServerBoundPacket):
    PACKET_ID = b'\x03'
    DIRECTION = PacketDirection.SERVER
    MODE = PacketMode.LOGIN
    NEXT_MODE = PacketMode.CONFIGURATION

    def __init__(self, is_compressed: bool = False) -> None:
        super().__init__(is_compressed)

    def _write(self):
        buffer = Buffer()
        buffer.write(b'')

        return buffer
