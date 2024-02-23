import time

from protopy.packets.buffer import Buffer
from protopy.packets.serverboundpackets import ServerBoundPacket
from protopy.packets.packet import PacketMode

class PingRequestPacket(ServerBoundPacket):
    packet_id = b'\x01'
    mode = PacketMode.STATUS

    def __init__(self, is_compressed: bool = False) -> None:
        super().__init__(
            is_compressed = is_compressed,
        )

    def _write(self):
        buffer = Buffer()
        buffer.write_long(round(time.time() * 1000))

        return buffer
