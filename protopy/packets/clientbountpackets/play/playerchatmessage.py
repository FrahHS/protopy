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

    def _read(self, body):
        # Header
        res, body = self.packet_reader.read_uuid(body)
        self.response['sender'] = res

        res, body = self.packet_reader.read_varint(body)
        self.response['index'] = res

        res, body = self.packet_reader.read_boolean(body)
        self.response['message_signature_present'] = res

        # TODO: handle
        if(self.response['message_signature_present']):
            res, body = self.packet_reader.read_boolean(body)
            self.response['message_signature_bytes'] = res

        # Body
        res, body = self.packet_reader.read_string(body)
        self.response['message'] = res

        res, body = self.packet_reader.read_long(body)
        self.response['timestamp'] = res

        res, body = self.packet_reader.read_long(body)
        self.response['salt'] = res

        # Previous Messages
        res, body = self.packet_reader.read_varint(body)
        self.response['total_previous_messages'] = res

        res, body = self.packet_reader.read_varint(body)
        self.response['message_id'] = res

        # TODO: handle
        if(self.response['message_signature_present']):
            res, body = self.packet_reader.read_boolean(body)
            self.response['signature'] = res

        # Other
        res, body = self.packet_reader.read_boolean(body)
        self.response['unsigned_content_present'] = res

        # TODO: handle
        if(self.response['unsigned_content_present']):
            res, body = self.packet_reader.read_boolean(body)
            self.response['unsigned_content'] = res

        res, body = self.packet_reader.read_varint(body)
        self.response['filter_type'] = res

        # TODO: handle
        if(self.response['filter_type'] == 2):
            res, body = self.packet_reader.read_boolean(body)
            self.response['filter_type_bits'] = res

        # Chat Formatting
        res, body = self.packet_reader.read_varint(body)
        self.response['chat_type'] = res

        res, body = self.packet_reader.read_chat(body)
        self.response['sender_name'] = res

        res, body = self.packet_reader.read_boolean(body)
        self.response['has_target_name'] = res

        if(self.response['has_target_name']):
            res, body = self.packet_reader.read_chat(body)
            self.response['target_name'] = res

    @property
    def sender(self) -> UUID:
        return self.response['sender']

    @property
    def index(self) -> Varint:
        return self.response['index']

    @property
    def message(self) -> str:
        return self.response['message']

    @property
    def timestamp(self) -> int:
        return self.response['timestamp']
