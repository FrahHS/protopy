from protopy.packets.buffer import Buffer
from protopy.packets.serverboundpackets import ServerBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode

class ServerBoundFinishConfigurationPacket(ServerBoundPacket):
    packet_id = b'\x02'
    mode = PacketMode.CONFIGURATION
    next_mode= PacketMode.PLAY

    def __init__(self, is_compressed: bool = False) -> None:
        super().__init__(
            is_compressed = is_compressed,
        )

    def _write(self):
        buffer = Buffer()
        buffer.write(b'')

        return buffer
