from datatypes.buffer import Buffer
from packets.serverboundpackets import ServerBoundPacket
from packets.packet import PacketDirection, PacketMode

class StatusRequestPacket(ServerBoundPacket):
    PACKET_ID = b'\x00'
    DIRECTION = PacketDirection.SERVER
    MODE = PacketMode.STATUS
    NEXT_MODE = PacketMode.STATUS

    def _write(self) -> bytes:
        buffer = Buffer()
        buffer.write(b'\x00')

        return buffer

    def packet(self, compression: bool = False) -> bytes:
        packet = self._write()
        return self.pack(self.PACKET_ID, packet, compression)

