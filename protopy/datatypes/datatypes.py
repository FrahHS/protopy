from enum import Enum


class DataTypes(Enum):
    BOOLEAN = 1
    BYTE = 2
    UNSIGNED_BYTE = 3
    SHORT = 4
    UNSIGNED_SHORT = 5
    INT = 6
    LONG = 7
    FLOAT = 8
    DOUBLE = 9
    STRING = 10
    CHAT = 11
    JSON_CHAT = 12
    IDENTIFIER = 13
    VARINT = 14
    VARLONG = 15
    ENTITY_METADATA = 16
    SLOT = 17
    NBT_TAG = 18
    POSITION = 19
    ANGLE = 20
    UUID = 21
    OPTIONAL_X = 22
    ARRAY_OF_X = 23
    X_ENUM = 24
    BYTE_ARRAY = 25
