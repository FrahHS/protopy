from protopy.packets.buffer import Buffer
from protopy.packets.serverboundpackets import ServerBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode

class LoginAcknowledged(ServerBoundPacket):
    packet_id = b'\x03'
    mode = PacketMode.LOGIN
    next_mode= PacketMode.CONFIGURATION

    def __init__(self, is_compressed: bool = False) -> None:
        super().__init__(
            is_compressed = is_compressed,
        )

    def _write(self):
        buffer = Buffer()
        buffer.write(b'')

        return buffer
