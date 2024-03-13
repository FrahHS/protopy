import struct
from uuid import UUID

from protopy.datatypes.varint import Varint


class BufferTypeException(Exception):
    pass


class Buffer:
    def __init__(self) -> None:
        self.body = b""
        self.argc = 0

    def writer(func):
        def wrapper(self, data):
            # Incremeng args counter
            self.argc += 1

            # Get writer data type required
            func_data_arg_type = func.__annotations__["data"]

            # Raise BufferTypeException if incoming data type is not matching writer data type
            if type(data) != func_data_arg_type:
                raise BufferTypeException(
                    f"Data type exception raised for args {self.argc} of the buffer, {type(data)} received when {func_data_arg_type} was required"
                )

            # Call the writer
            func(self, data)

        return wrapper

    @property
    def data(self) -> bytes:
        return self.body

    def write(self, data) -> None:
        if isinstance(data, Buffer):
            self.body += data.data
        else:
            self.body += data

    @writer
    def write_boolean(self, data: bool) -> None:
        self.body += b"\x01" if data else b"\x00"

    @writer
    def write_byte(self, data: bytes) -> None:
        self.body += data

    @writer
    def write_unsigned_byte(self, data: bytes) -> None:
        self.body += data

    @writer
    def write_unsigned_short(self, data: int) -> None:
        self.body += struct.pack(">H", data)

    # TODO
    @writer
    def write_unsigned_int(self, data: int) -> None:
        pass

    # TODO
    @writer
    def write_int(self, data: int) -> None:
        pass

    @writer
    def write_long(self, data: int) -> None:
        self.body += struct.pack(">Q", data)

    # TODO
    @writer
    def write_float(self, data: float) -> None:
        pass

    # TODO
    @writer
    def write_double(self, data: float) -> None:
        pass

    @writer
    def write_string(self, data: str) -> None:
        self.body += Varint.data_pack(data.encode())

    # TODO
    @writer
    def write_chat(self, data: str) -> None:
        pass

    # TODO
    @writer
    def write_json_chat(self, data: str) -> None:
        pass

    # TODO
    @writer
    def write_identifier(self, data: str) -> None:
        pass

    @writer
    def write_varint(self, data: int) -> None:
        self.body += Varint(data).bytes

    # TODO: change when Varlong will be created
    @writer
    def write_varlong(self, data: int) -> None:
        pass

    # TODO
    @writer
    def write_entity_metadata(self, data: str) -> None:
        pass

    # TODO
    @writer
    def write_slot(self, data: str) -> None:
        pass

    # TODO
    @writer
    def write_nbt_tag(self, data: str) -> None:
        pass

    # TODO
    @writer
    def write_position(self, data: int) -> None:
        pass

    # TODO
    @writer
    def write_angle(self, data: int) -> None:
        pass

    # TODO
    @writer
    def write_uuid(self, data: UUID) -> None:
        self.body += data.bytes

    # TODO
    @writer
    def write_optional_x(self, data: int) -> None:
        pass

    # TODO
    @writer
    def write_array_of_x(self, data: int) -> None:
        pass

    # TODO
    @writer
    def write_x_enum(self, data: int) -> None:
        pass

    # TODO
    @writer
    def write_byte_array(self, data: bytearray) -> None:
        pass
