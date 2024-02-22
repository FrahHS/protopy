import io
import json, gzip
import struct, uuid, zlib
import nbtlib

from protopy.datatypes.varint import Varint
from protopy.datatypes.datatypes import DataTypes
from protopy.packets.packet import Packet, PacketDirection, PacketMode, UnknowPacket
from protopy.utils import logger

class PacketReader:
    all_packets = {}

    def __init__(self, compression: bool = False) -> None:
        self.compression = compression

    def get_packet_id_and_data(self, raw_data: bytes) -> Varint:
        if(self.compression):
            packet_length, body = Varint.unpack(raw_data)
            data_length, body = Varint.unpack(body)
            body = zlib.decompress(body) if data_length != 0 else body
            packet_id, body = Varint.unpack(body)
        else:
            packet_length, body = Varint.unpack(raw_data)
            packet_id, body = Varint.unpack(body)

        return Varint(packet_id), body

    def build_packet_from_raw_data(self, raw_data: bytes, mode: PacketMode, is_compressed: bool = False):
        packet_id, payload = self.get_packet_id_and_data(raw_data)
        new_packet = (packet_id.bytes, PacketDirection.CLIENT, mode,)

        if(not Packet.all_packets.keys().__contains__(new_packet)):
            return UnknowPacket(packet_id, mode, PacketDirection.CLIENT, raw_data)

        return Packet.all_packets[new_packet](raw_data, is_compressed)

    def read_boolean(self, data: bool) -> None:
        res = struct.unpack("?", data[:1])[0]
        return (res, data[1:])

    #TODO
    def read_byte(self, data: bytes) -> None:
        pass

    #TODO
    def read_unsigned_byte(self, data: bytes) -> None:
        pass

    #TODO
    def read_unsigned_short(self, data: int) -> None:
        pass

    #TODO
    def read_unsigned_int(self, data: int) -> None:
        pass

    #TODO
    def read_int(self, data: int) -> None:
        pass

    def read_long(self, data: int) -> None:
        res = struct.unpack(">Q", data[:8])[0]
        return(res, data[8:])

    #TODO
    def read_float(self, data: float) -> None:
        pass

    #TODO
    def read_double(self, data: float) -> None:
        pass

    def read_string(self, data: str) -> None:
        lenght, string = Varint.unpack(data)
        return (string[:lenght].decode(), data[lenght+1:])

    #TODO: fix, is not reading full NBT Tag
    def read_chat(self, data: bytes) -> None:
        file = io.BytesIO((data))
        nbt_file = nbtlib.File.parse(fileobj=file)

        # A very unelegant way to fint nbt tag lenght in bytes
        file_for_lenght = io.BytesIO(b'')
        nbt_file.write(fileobj=file_for_lenght)
        file_for_lenght.seek(0)
        lenght = len(file_for_lenght.read())
        data = data[lenght+1:]

        return (nbt_file, data)

    #TODO
    def read_json_chat(self, data: str) -> None:
        pass

    #TODO
    def read_identifier(self, data: str) -> None:
        pass

    def read_varint(self, data: Varint) -> None:
        res, bytes_body = Varint.unpack(data)
        return (res, bytes_body)

    #TODO: change when Varlong will be created
    def read_varlong(self, data: int) -> None:
        pass

    #TODO
    def read_entity_metadata(self, data: str) -> None:
        pass

    #TODO
    def read_slot(self, data: str) -> None:
        pass

    #TODO
    def read_nbt_tag(self, data: str) -> None:
        pass

    #TODO
    def read_position(self, data: int) -> None:
        pass

    #TODO
    def read_angle(self, data: int) -> None:
        pass

    def read_uuid(self, data: uuid.UUID) -> None:
        res = uuid.UUID(bytes=data[:16])
        return(res, data[16:])

    #TODO
    def read_optional_x(self, data: int) -> None:
        pass

    #TODO
    def read_array_of_x(self, data: int) -> None:
        pass

    #TODO
    def read_x_enum(self, data: int) -> None:
        pass

    #TODO
    def read_byte_array(self, data: bytearray) -> None:
        pass
