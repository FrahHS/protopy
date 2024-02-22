from protopy.packets.buffer import Buffer
from protopy.packets.serverboundpackets import ServerBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode

class FinishConfigurationPacket(ServerBoundPacket):
    PACKET_ID = b'\x02'
    DIRECTION = PacketDirection.SERVER
    MODE = PacketMode.CONFIGURATION
    NEXT_MODE = PacketMode.PLAY

    def __init__(self, is_compressed: bool = False) -> None:
        super().__init__(is_compressed)

    def _write(self):
        buffer = Buffer()
        buffer.write(b'')

        return buffer
