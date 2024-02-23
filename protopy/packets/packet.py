from enum import Enum
from abc import ABC, abstractmethod

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
    all_packets = {}

    def __init__(self, raw_data: bytes, is_compressed: bool) -> None:
        self.raw_data = raw_data
        self.is_compressed = is_compressed


    @staticmethod
    def data_pack(data: bytes) -> bytes:
        return Varint.data_pack(data)

    @staticmethod
    @property
    @abstractmethod
    def packet_id() -> bytes:
        pass

    @staticmethod
    @property
    @abstractmethod
    def mode() -> PacketMode:
        pass

    @staticmethod
    @property
    @abstractmethod
    def direction() -> PacketMode:
        pass

    @property
    def next_mode(self) -> PacketMode:
        return self.mode

class UnknowPacket:
    def __init__(self, packet_id: bytes, mode: PacketMode, direction: PacketDirection, raw_data: bytes, is_compressed: bool) -> None:
        self.raw_data = raw_data
        self.is_compressed = is_compressed
        self.packet_id = packet_id
        self.mode = mode
        self.direction = direction

