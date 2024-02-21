from uuid import UUID
from protopy.datatypes.datatypes import DataTypes
from protopy.datatypes.varint import Varint
from protopy.packets.clientbountpackets import ClientBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode
from protopy.packets.packetreader import PacketReader
from protopy.utils import logger

class PlayerChatMessagePacket(ClientBoundPacket):
    PACKET_ID = b'\x37'
    DIRECTION = PacketDirection.CLIENT
    MODE = PacketMode.PLAY
    NEXT_MODE = PacketMode.PLAY

    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(raw_data, is_compressed)

    def _fmt(self):
        fmt = [
            # Sender
            DataTypes.UUID,
            # Index
            DataTypes.VARINT,
            # Message Signature Present
            DataTypes.BOOLEAN,
        ]

        # Check for Message Signature Present
        packet_reader = PacketReader(self.is_compressed)
        res = packet_reader.read(fmt, self.raw_data, self.MODE, suppress_warning=True)

        # TODO: Handle signature
        if(res[2]):
            # Message Signature bytes
            fmt.append(DataTypes.BYTE_ARRAY)

        fmt += [
            # Message
            DataTypes.STRING,
            # Timestamp
            DataTypes.LONG,
            # Salt
            DataTypes.LONG,
            # Total Previous Messages
            DataTypes.VARINT,
            # Message ID
            DataTypes.VARINT,
        ]

        return fmt

    @property
    def sender(self) -> UUID:
        return self.response[0]
