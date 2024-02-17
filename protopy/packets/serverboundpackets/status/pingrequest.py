import time

from protopy.datatypes.buffer import Buffer
from protopy.packets.serverboundpackets import ServerBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode

class PingRequestPacket(ServerBoundPacket):
    PACKET_ID = b'\x01'
    DIRECTION = PacketDirection.SERVER
    MODE = PacketMode.STATUS
    NEXT_MODE = PacketMode.STATUS

    def _write(self):
        buffer = Buffer()
        buffer.write_long(round(time.time() * 1000))

        return buffer
