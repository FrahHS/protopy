from datatypes.buffer import Buffer
from packets.serverboundpackets import ServerBoundPacket
from packets.packet import PacketDirection, PacketMode

class LoginAcknowledged(ServerBoundPacket):
    PACKET_ID = b'\x03'
    DIRECTION = PacketDirection.SERVER
    MODE = PacketMode.LOGIN
    NEXT_MODE = PacketMode.CONFIGURATION

    def __init__(self) -> None:
        #super().__init__(self.PACKET_ID)
        pass

    def write(self):
        buffer = Buffer()
        buffer.write(b'')

        return buffer

    def packet(self, compression: bool = False) -> bytes:
        packet = self.write()
        return self.pack(self.PACKET_ID, packet, compression)
