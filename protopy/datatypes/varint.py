import struct

class Varint:
    def __init__(self, int: int):
        self.int = int

    def __str__(self):
        return str(self.bytes)

    @property
    def bytes(self):
        return self.pack(self.int)

    @staticmethod
    def pack(d):
        o = b''
        while True:
            b = d & 0x7F
            d >>= 7
            o += struct.pack("B", b | (0x80 if d > 0 else 0))
            if d == 0:
                break
        return o

    @staticmethod
    def unpack(s):
        d, l = 0, 0
        length = len(s)
        if length > 5:
            length = 5
        for i in range(length):
            l += 1
            b = s[i]
            d |= (b & 0x7F) << 7 * i
            if not b & 0x80:
                break
        return (d, s[l:])

    @staticmethod
    def data_pack(data) -> bytes:
        return Varint(len(data)).bytes + data
