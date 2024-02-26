from protopy.packets.buffer import Buffer
from protopy.packets.serverboundpackets import ServerBoundPacket
from protopy.packets.packet import PacketMode


class StatusRequestPacket(ServerBoundPacket):
    packet_id = b"\x00"
    mode = PacketMode.STATUS

    def __init__(self, is_compressed: bool = False) -> None:
        super().__init__(
            is_compressed=is_compressed,
        )

    def _write(self) -> bytes:
        buffer = Buffer()
        buffer.write(b"\x00")

        return buffer

    def packet(self, compression: bool = False) -> bytes:
        packet = self._write()
        return self.pack(self.packet_id, packet, compression)
