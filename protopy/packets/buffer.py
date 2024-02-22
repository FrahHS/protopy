import struct
import time
from uuid import UUID

from protopy.datatypes.varint import Varint

class Buffer:
    def __init__(self) -> None:
        self.body = b''

    @property
    def data(self) -> bytes:
        return self.body

    def write(self, data) -> None:
        if(isinstance(data, Buffer)):
            self.body += data.data
        else:
            self.body += data

    def write_boolean(self, data: bool) -> None:
        self.body += b'\x01' if data else b'\x00'

    def write_byte(self, data: bytes) -> None:
        self.body += data

    def write_unsigned_byte(self, data: bytes) -> None:
        self.body += data

    def write_unsigned_short(self, data: int) -> None:
        self.body += struct.pack('>H', data)

    #TODO
    def write_unsigned_int(self, data: int) -> None:
        pass

    #TODO
    def write_int(self, data: int) -> None:
        pass

    def write_long(self, data: int) -> None:
        self.body += struct.pack(">Q", data)

    #TODO
    def write_float(self, data: float) -> None:
        pass

    #TODO
    def write_double(self, data: float) -> None:
        pass

    def write_string(self, data: str) -> None:
        self.body += Varint.data_pack(data.encode())

    #TODO
    def write_chat(self, data: str) -> None:
        pass

    #TODO
    def write_json_chat(self, data: str) -> None:
        pass

    #TODO
    def write_identifier(self, data: str) -> None:
        pass

    def write_varint(self, data: Varint) -> None:
        self.body += Varint(data).bytes

    #TODO: change when Varlong will be created
    def write_varlong(self, data: int) -> None:
        pass

    #TODO
    def write_entity_metadata(self, data: str) -> None:
        pass

    #TODO
    def write_slot(self, data: str) -> None:
        pass

    #TODO
    def write_nbt_tag(self, data: str) -> None:
        pass

    #TODO
    def write_position(self, data: int) -> None:
        pass

    #TODO
    def write_angle(self, data: int) -> None:
        pass

    #TODO
    def write_uuid(self, data: UUID) -> None:
        self.body += data.bytes

    #TODO
    def write_optional_x(self, data: int) -> None:
        pass

    #TODO
    def write_array_of_x(self, data: int) -> None:
        pass

    #TODO
    def write_x_enum(self, data: int) -> None:
        pass

    #TODO
    def write_byte_array(self, data: bytearray) -> None:
        pass
