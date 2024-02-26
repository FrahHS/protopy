from protopy.packets.buffer import Buffer
from protopy.packets.serverboundpackets import ServerBoundPacket
from protopy.packets.packet import PacketMode


class HandshakePacket(ServerBoundPacket):
    packet_id = b"\x00"
    mode = PacketMode.HANDSHAKING

    def __init__(
        self,
        protocol_version: int,
        server_address: str,
        server_port: int,
        next_state: int,
        is_compressed: bool = False,
    ) -> None:
        super().__init__(
            is_compressed=is_compressed,
        )

        self.protocol_version = protocol_version
        self.server_address = server_address
        self.server_port = server_port
        self.next_state = next_state

    def _write(self):
        buffer = Buffer()
        buffer.write_varint(self.protocol_version)
        buffer.write_string(self.server_address)
        buffer.write_unsigned_short(self.server_port)
        buffer.write_varint(self.next_state)

        return buffer
