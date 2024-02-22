from enum import Enum
from abc import ABC, abstractmethod

from protopy.packets.buffer import Buffer
from protopy.datatypes.varint import Varint

class PacketDirection(Enum):
    CLIENT = 1
    SERVER = 2

class PacketMode(Enum):
    HANDSHAKING = 1
    STATUS = 2
    LOGIN = 3
    CONFIGURATION = 4
    PLAY = 5

class Packet(ABC):
    def __init__(self, is_compressed) -> None:
        self.is_compressed = is_compressed

    @staticmethod
    def data_pack(data: bytes) -> bytes:
        return Varint.data_pack(data)

class UnknowPacket:
    def __init__(self, packet_id: Varint, mode: PacketMode, direction: PacketDirection, raw_data: bytes) -> None:
        self.PACKET_ID = packet_id.bytes
        self.MODE = mode,
        self.DIRECTION = direction
        self.raw_data = raw_data
