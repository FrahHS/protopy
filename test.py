"""import gzip
import io
from nbt.nbt import NBTFile

b'\n\x00\nhoverEvent\n\x00\x08contents\x08\x00\x04name\x00\x0eCiccioFumaerba\x0b\x00\x02id\x00\x00\x00\x04\xd6\xbe6D\xe0D3\xa4\x85\xf1P\xacI\xdb\x92\xa1\x08\x00\x04type\x00\x10minecraft:player\x00\x08\x00\x06action\x00\x0bshow_entity\x00\n\x00\nclickEvent\x08\x00\x06action\x00\x0fsuggest_command\x08\x00\x05value\x00\x15/tell CiccioFumaerba \x00\x08\x00\tinsertion\x00\x0eCiccioFumaerba\x08\x00\x04text\x00\x0eCiccioFumaerba\x00\x00'

data = b'\n\t\x00\x05extra\x08\x00\x00\x00\x01\x00\x15Kicked by an operator\x08\x00\x04text\x00\x00\x00'

#data = b'\n\x00\x07content' + data
file = io.BytesIO(gzip.compress(data))
nbtfile = NBTFile(fileobj=file)

buffer = io.BytesIO()
nbtfile.write_file(fileobj=buffer)
data = data[len(gzip.decompress(buffer.getvalue())):]

print(nbtfile, data)"""

from collections.abc import Sequence
import math

class Bitset(Sequence):
    """A very simple bitset implementation for Python.

    Note that, like with normal numbers, the leftmost
    index is the MSB, and like normal sequences, that
    is 0.

    Usage:
        >>> b = Bitset(5)
        >>> b
        Bitset(101)
        >>> b[:]
        [True, False, True]
        >>> b[0] = False
        >>> b
        Bitset(001)
        >>> b << 1
        Bitset(010)
        >>> b >> 1
        Bitset(000)
        >>> b & 1
        Bitset(001)
        >>> b | 2
        Bitset(011)
        >>> b ^ 6
        Bitset(111)
        >>> ~b
        Bitset(110)
    """

    value = 0
    length = 0

    @classmethod
    def from_sequence(cls, seq):
        """Iterates over the sequence to produce a new Bitset.

        As in integers, the 0 position represents the LSB.
        """
        n = 0
        for index, value in enumerate(reversed(seq)):
            n += 2**index * bool(int(value))
        b = Bitset(n)
        return b

    def __init__(self, value=0, length=0):
        """Creates a Bitset with the given integer value."""
        self.value = value
        try: self.length = length or math.floor(math.log(value, 2)) + 1
        except Exception: self.length = 0

    def __and__(self, other):
        b = Bitset(self.value & int(other))
        b.length = max((self.length, b.length))
        return b

    def __or__(self, other):
        b = Bitset(self.value | int(other))
        b.length = max((self.length, b.length))
        return b

    def __invert__(self):
        b = Bitset(~self.value)
        b.length = max((self.length, b.length))
        return b

    def __xor__(self, value):
        b = Bitset(self.value ^ int(value))
        b.length = max((self.length, b.length))
        return b

    def __lshift__(self, value):
        b = Bitset(self.value << int(value))
        b.length = max((self.length, b.length))
        return b

    def __rshift__(self, value):
        b = Bitset(self.value >> int(value))
        b.length = max((self.length, b.length))
        return b

    def __eq__(self, other):
        try:
            return self.value == other.value
        except Exception:
            return self.value == other

    def __int__(self):
        return self.value

    def __str__(self):
        s = ""
        for i in self[:]:
            s += "1" if i else "0"
        return s

    def __repr__(self):
        return "Bitset(%s)" % str(self)

    def __getitem__(self, s):
        """Gets the specified position.

        Like normal integers, 0 represents the MSB.
        """
        try:
            start, stop, step = s.indices(len(self))
            results = []
            for position in range(start, stop, step):
                pos = len(self) - position - 1
                results.append(bool(self.value & (1 << pos)))
            return results
        except:
            pos = len(self) - s - 1
            return bool(self.value & (1 << pos))

    def __setitem__(self, s, value):
        """Sets the specified position/s to value.

        Like normal integers, 0 represents the MSB.
        """
        try:
            start, stop, step = s.indices(len(self))
            for position in range(start, stop, step):
                pos = len(self) - position - 1
                if value: self.value |= (1 << pos)
                else: self.value &= ~(1 << pos)
            maximum_position = max((start + 1, stop, len(self)))
            self.length = maximum_position
        except:
            pos = len(self) - s - 1
            if value: self.value |= (1 << pos)
            else: self.value &= ~(1 << pos)
            if len(self) < pos: self.length = pos
        return self

    def __iter__(self):
        """Iterates over the values in the bitset."""
        for i in self[:]:
            yield i

    def __len__(self):
        """Returns the length of the bitset."""
        return self.length

