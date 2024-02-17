from datatypes.buffer import Buffer
from packets.serverboundpackets import ServerBoundPacket
from packets.packet import PacketDirection, PacketMode

class LoginAcknowledged(ServerBoundPacket):
    PACKET_ID = b'\x03'
    DIRECTION = PacketDirection.SERVER
    MODE = PacketMode.LOGIN
    NEXT_MODE = PacketMode.CONFIGURATION

    def _write(self):
        buffer = Buffer()
        buffer.write(b'')

        return buffer
