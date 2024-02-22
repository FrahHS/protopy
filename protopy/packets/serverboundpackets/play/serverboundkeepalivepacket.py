from protopy.packets.buffer import Buffer
from protopy.packets.serverboundpackets import ServerBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode

class ServerboundKeepAlivePacket(ServerBoundPacket):
    PACKET_ID = b'\x15'
    DIRECTION = PacketDirection.SERVER
    MODE = PacketMode.PLAY
    NEXT_MODE = PacketMode.PLAY

    def __init__(self, keep_alive_id: bytes, is_compressed: bool = False) -> None:
        super().__init__(is_compressed)
        self.keep_alive_id = keep_alive_id

    def _write(self):
        buffer = Buffer()
        buffer.write_long(self.keep_alive_id)

        return buffer

