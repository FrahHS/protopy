from protopy.packets.buffer import Buffer
from protopy.packets.serverboundpackets import ServerBoundPacket
from protopy.packets.packet import PacketMode

from typing import Optional

class ChatMessagePacket(ServerBoundPacket):
    packet_id = b'\x05'
    mode = PacketMode.PLAY

    def __init__(self, message: str, timestamp: int, salt: int, has_signature: bool, message_count: int, acknowledged, signature: int = b'', is_compressed: bool = False) -> None:
        super().__init__(
            is_compressed = is_compressed,
        )

        self.message = message
        self.timestamp = timestamp
        self.salt = salt
        self.has_signature = has_signature
        self.signature = signature
        self.message_count = message_count
        self.acknowledged = acknowledged

    def _write(self):
        buffer = Buffer()
        buffer.write_string(self.message)
        buffer.write_long(self.timestamp)
        buffer.write_long(self.salt)
        buffer.write_boolean(self.has_signature)
        if self.has_signature:
            buffer.write_byte_array(self.signature, length=256)
        buffer.write_varint(self.message_count)
        buffer.write(self.acknowledged)

        return buffer


