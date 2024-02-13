from uuid import UUID

from datatypes.buffer import Buffer
from datatypes.varint import Varint
from packets.packet import Packet, PacketDirection, PacketMode

class ClientInformationConfigurationPacket(Packet):
    PACKET_ID = b'\x00'
    DIRECTION = PacketDirection.SERVER
    MODE = PacketMode.CONFIGURATION
    NEXT_MODE = PacketMode.CONFIGURATION

    def __init__(self, locale: str, view_distance: bytes, chat_mode: int, chat_color: bool, displayer_skin_parts: bytes, main_hand: int, enable_text_filtering: bool, allow_server_listing: bool) -> None:
        self.locale: str = locale
        self.view_distance: bytes = view_distance
        self.chat_mode: int = chat_mode
        self.chat_color: bool = chat_color
        self.displayer_skin_parts: bytes = displayer_skin_parts
        self.main_hand: int = main_hand
        self.enable_text_filtering: bool = enable_text_filtering
        self.allow_server_listing: bool = allow_server_listing


    def write(self):
        buffer = Buffer()
        buffer.write_string(self.locale)
        buffer.write_byte(self.view_distance)
        buffer.write_varint(self.chat_mode)
        buffer.write_boolean(self.chat_color)
        buffer.write_unsigned_byte(self.displayer_skin_parts)
        buffer.write_varint(self.main_hand)
        buffer.write_boolean(self.enable_text_filtering)
        buffer.write_boolean(self.allow_server_listing)

        return buffer

    def packet(self, compression: bool = False) -> bytes:
        packet = self.write()
        return self.pack(self.PACKET_ID, packet, compression)
