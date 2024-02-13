from datatypes.buffer import Buffer
from packets.packet import Packet, PacketDirection, PacketMode

class HandshakePacket(Packet):
    PACKET_ID = b'\x00'
    DIRECTION = PacketDirection.SERVER
    MODE = PacketMode.HANDSHAKING
    NEXT_MODE = PacketMode.HANDSHAKING

    def __init__(self, server_address: str, server_port: int, next_state: int) -> None:
        self.server_address = server_address
        self.server_port = server_port
        self.next_state = next_state

        #super().__init__(self.PACKET_ID)

    def write(self):
        buffer = Buffer()
        buffer.write_varint(765)
        buffer.write_string(self.server_address)
        buffer.write_unsigned_short(self.server_port)
        buffer.write_varint(self.next_state)

        return buffer

    def packet(self, compression: bool = False) -> bytes:
        packet = self.write()
        return self.pack(self.PACKET_ID, packet, compression)
