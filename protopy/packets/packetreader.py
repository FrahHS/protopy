import struct, uuid, zlib

from datatypes.varint import Varint
from datatypes.datatypes import DataTypes
from packets.packet import Packet, PacketDirection, PacketMode, UnknowPacket
from utils import logger

class PacketReader:
    all_packets = {}

    def __init__(self, compression: bool = False) -> None:
        self.compression = compression

    def get_packet_id_and_data(self, raw_data: bytes, mode: PacketMode) -> Varint:
        if(self.compression):
            packet_length, body = Varint.unpack(raw_data)
            data_length, body = Varint.unpack(body)

            #TODO: Handle zlib compresion
            body = zlib.decompress(body) if data_length != 0 else body

            packet_id, body = Varint.unpack(body)
        else:
            packet_length, body = Varint.unpack(raw_data)
            packet_id, body = Varint.unpack(body)


        return Varint(packet_id), body

    def build_packet_from_raw_data(self, raw_data: bytes, mode: PacketMode):
        packet_id, body = self.get_packet_id_and_data(raw_data, mode)
        new_packet = (packet_id.bytes, PacketDirection.CLIENT, mode,)

        if(not Packet.all_packets.keys().__contains__(new_packet)):
            logger.warning(f'Packet not found!')
            logger.info(f'packet_id: {hex(packet_id.int)}')
            logger.info(f'packet_direction: {PacketDirection.CLIENT}')
            logger.info(f'packet_mode: {mode}')
            #logger.info(f'packet_raw_data: {raw_data}\n')
            return UnknowPacket(packet_id, raw_data)

        return Packet.all_packets[new_packet](raw_data)

    def read(self, _fmt, raw_data, mode: PacketMode) -> list:
        response = list()
        packet_id, body = self.get_packet_id_and_data(raw_data, mode)

        for field in _fmt:
            match field:
                case DataTypes.BOOLEAN:
                    # TODO: code for handling BOOLEAN type
                    pass
                case DataTypes.BYTE:
                    # TODO: code for handling BYTE type
                    pass
                case DataTypes.UNSIGNED_BYTE:
                    # TODO: code for handling UNSIGNED_BYTE type
                    pass
                case DataTypes.SHORT:
                    # TODO: code for handling SHORT type
                    pass
                case DataTypes.UNSIGNED_SHORT:
                    # TODO: code for handling UNSIGNED_SHORT type
                    pass
                case DataTypes.INT:
                    # TODO: code for handling INT type
                    pass
                case DataTypes.LONG:
                    res = struct.unpack("Q", body)[0]

                    body = body[len(bytes(res)):]
                    response.append(res)
                case DataTypes.FLOAT:
                    # TODO: code for handling FLOAT type
                    pass
                case DataTypes.DOUBLE:
                    # TODO: code for handling DOUBLE type
                    pass
                case DataTypes.STRING:
                    len, string = Varint.unpack(body)

                    body = body[len+1:]
                    response.append(string[:len].decode())
                case DataTypes.CHAT:
                    # TODO: code for handling CHAT type
                    pass
                case DataTypes.JSON_CHAT:
                    # TODO: code for handling JSON_CHAT type
                    pass
                case DataTypes.IDENTIFIER:
                    # TODO: code for handling IDENTIFIER type
                    pass
                case DataTypes.VARINT:
                    res, bytes = Varint.unpack(body)
                    body = bytes

                    response.append(res)
                case DataTypes.VARLONG:
                    # TODO: code for handling VARLONG type
                    pass
                case DataTypes.ENTITY_METADATA:
                    # TODO: code for handling ENTITY_METADATA type
                    pass
                case DataTypes.SLOT:
                    # TODO: code for handling SLOT type
                    pass
                case DataTypes.NBT_TAG:
                    # TODO: code for handling NBT_TAG type
                    pass
                case DataTypes.POSITION:
                    # TODO: code for handling POSITION type
                    pass
                case DataTypes.ANGLE:
                    # TODO: code for handling ANGLE type
                    pass
                case DataTypes.UUID:
                    res = uuid.UUID(bytes=body[:16])
                    response.append(res)
                    body = body[16:]
                case DataTypes.OPTIONAL_X:
                    # TODO: code for handling OPTIONAL_X type
                    pass
                case DataTypes.ARRAY_OF_X:
                    # TODO: code for handling ARRAY_OF_X type
                    pass
                case DataTypes.X_ENUM:
                    # TODO: code for handling X_ENUM type
                    pass
                case DataTypes.BYTE_ARRAY:
                    # TODO: code for handling BYTE_ARRAY type
                    pass
                case _:
                    # TODO: Default case if the field doesn't match any of the defined types
                    pass
        if(body != b''):
            print(f'parte del pacchetto ignorata: {body}')
        return response
