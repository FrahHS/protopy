import struct, uuid
from enum import Enum
from datatypes.buffer import Buffer

from datatypes.varint import Varint
from datatypes.datatypes import DataTypes

class PacketDirection(Enum):
    CLIENT = 1
    SERVER = 2

class PacketMode(Enum):
    HANDSHAKING = 1
    STATUS = 2
    LOGIN = 3
    CONFIGURATION = 4
    PLAY = 5


class Packet:
    def __init__(self, packet_id) -> None:
        #packet = self.write()
        #self.raw_data = self.pack(packet_id, packet,)
        pass

    def write(self):
        pass

    def pack(self, packet_id: bytes, raw_data: bytes, compression: bool = False,) -> None:
        packet = Buffer()
        if(compression):
            #TODO: Handle zlib compression
            packet.write(b'\x00')
            packet.write(packet_id)
            packet.write(raw_data)
        else:
            packet.write(packet_id)
            packet.write(raw_data)

        return Packet.data_pack(packet.data)

    @staticmethod
    def data_pack(data) -> bytes:
        return Varint.data_pack(data)

class UnknowPacket:
    def __init__(self, packet_id: bytes, raw_data: bytes) -> None:
        self.packet_id =packet_id
        self.raw_data = raw_data
