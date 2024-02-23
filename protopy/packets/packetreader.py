import struct, uuid, zlib, io, gzip
from nbt.nbt import NBTFile, MalformedFileError

from protopy.datatypes.varint import Varint
from protopy.packets.packet import Packet, PacketDirection, PacketMode, UnknowPacket
from protopy.utils import logger

class PacketReader:
    """
    A class for reading and parsing different types of data packets.

    Attributes:
        compression (bool): A boolean indicating whether the data is compressed.
    """

    all_packets = {}

    def __init__(self, compression: bool = False) ->  None:
        """
        Initializes a PacketReader object.

        Args:
            compression (bool, optional): A boolean indicating whether the data is compressed.
        """
        self.compression = compression

    def get_packet_id_and_data(self, raw_data: bytes) -> tuple[Varint, bytes]:
        """
        Gets the packet ID and body data from the raw data.

        This method unpacks the raw data to extract the packet ID and the remaining body data.

        Args:
            raw_data (bytes): The raw data of the packet.

        Returns:
            Varint: The packet ID.
        """
        if self.compression:
            body = Varint.unpack(raw_data)[1]
            data_length, body = Varint.unpack(body)
            body = zlib.decompress(body) if data_length != 0 else body
            packet_id, body = Varint.unpack(body)
        else:
            body = Varint.unpack(raw_data)[1]
            packet_id, body = Varint.unpack(body)

        return Varint(packet_id), body

    def build_packet_from_raw_data(self, raw_data: bytes, mode: PacketMode, is_compressed: bool = False) -> Packet:
        """
        Builds a packet from raw data.

        This method constructs a packet child object using the provided raw data.

        Args:
            raw_data (bytes): The raw data of the packet.
            mode (PacketMode): The mode of the packet (e.g., PLAY, STATUS, LOGIN).
            is_compressed (bool, optional): A boolean indicating whether the data is compressed.

        Returns:
            Packet: The constructed packet object.
        """
        packet_id = self.get_packet_id_and_data(raw_data)[0]
        new_packet = (packet_id.bytes, PacketDirection.CLIENT, mode,)

        if not Packet.all_packets.keys().__contains__(new_packet):
            return UnknowPacket(packet_id.bytes, mode, PacketDirection.CLIENT, raw_data, is_compressed)

        return Packet.all_packets[new_packet](raw_data, is_compressed)

    def read_boolean(self, data: bool) ->  tuple[bool, bytes]:
        """
        Reads a boolean value from the data.

        This method reads a boolean value from the provided data.

        Args:
            data (bool): The data containing the boolean value.

        Returns:
            tuple: A tuple containing the boolean value and the remaining data.
        """
        res = struct.unpack("?", data[:1])[0]
        return (res, data[1:])

    # TODO: Implement these methods
    def read_byte(self, data: bytes) ->  tuple[bytes, bytes]:
        pass

    def read_unsigned_byte(self, data: bytes) ->  tuple:
        pass

    def read_unsigned_short(self, data: int) ->  tuple:
        pass

    def read_unsigned_int(self, data: int) ->  tuple:
        pass

    def read_int(self, data: int) ->  tuple:
        pass

    def read_long(self, data: int) -> tuple[int, bytes]:
        """
        Reads a long integer value from the data.

        This method reads a long integer value from the provided data.

        Args:
            data (int): The data containing the long integer value.

        Returns:
            tuple: A tuple containing the long integer value and the remaining data.
        """
        res = struct.unpack(">Q", data[:8])[0]
        return(res, data[8:])

    def read_float(self, data: float) ->  tuple:
        pass

    def read_double(self, data: float) ->  tuple:
        pass

    def read_string(self, data: str) -> tuple[str, bytes]:
        """
        Reads a string from the data.

        This method reads a string from the provided data.

        Args:
            data (str): The data containing the string.

        Returns:
            tuple: A tuple containing the string and the remaining data.
        """
        lenght, string = Varint.unpack(data)
        return (string[:lenght].decode(), data[lenght+1:])

    def read_chat(self, data: bytes) -> tuple[NBTFile, bytes]:
        """
        Reads chat data from the data.

        This method reads chat data from the provided data.

        Args:
            data (bytes): The data containing the chat data.

        Returns:
            tuple: A tuple containing the chat data and the remaining data.
        """
        try:
            data = b'\n\x00\x07content' + data
            file = io.BytesIO(gzip.compress(data))
            nbtfile = NBTFile(fileobj=file)

            buffer = io.BytesIO()
            nbtfile.write_file(fileobj=buffer)
            data = data[len(gzip.decompress(buffer.getvalue())):]
            return (nbtfile, data)
        except MalformedFileError as e:
            logger.warning(f'NBTFile parsing error {e}\nraw data:\n{data}')
            return (data, data)

    # TODO: Implement these methods
    def read_json_chat(self, data: str) ->  tuple:
        pass

    def read_identifier(self, data: str) ->  tuple:
        pass

    def read_varint(self, data: Varint) -> tuple[Varint, bytes]:
        """
        Reads a varint value from the data.

        This method reads a varint value from the provided data.

        Args:
            data (Varint): The data containing the varint value.

        Returns:
            tuple: A tuple containing the varint value and the remaining data.
        """
        res, bytes_body = Varint.unpack(data)
        return (res, bytes_body)

    # TODO: Implement these methods
    def read_varlong(self, data: int) ->  tuple:
        pass

    def read_entity_metadata(self, data: str) ->  tuple:
        pass

    def read_slot(self, data: str) ->  tuple:
        pass

    def read_nbt_tag(self, data: str) ->  tuple:
        pass

    def read_position(self, data: int) ->  tuple:
        pass

    def read_angle(self, data: int) ->  tuple:
        pass

    def read_uuid(self, data: uuid.UUID) -> tuple[uuid.UUID, bytes]:
        """
        Reads a UUID from the data.

        This method reads a UUID from the provided data.

        Args:
            data (uuid.UUID): The data containing the UUID.

        Returns:
            tuple: A tuple containing the UUID and the remaining data.
        """
        res = uuid.UUID(bytes=data[:16])
        return(res, data[16:])

    # TODO: Implement these methods
    def read_optional_x(self, data: int) ->  tuple:
        pass

    def read_array_of_x(self, data: int) ->  tuple:
        pass

    def read_x_enum(self, data: int) ->  tuple:
        pass

    def read_byte_array(self, data: bytearray, lenght: int) -> tuple[bytes, bytes]:
        """
        Reads a byte array from the data.

        This method reads a byte array from the provided data.

        Args:
            data (bytearray): The data containing the byte array.
            lenght (int): The length of the byte array.

        Returns:
            tuple: A tuple containing the byte array and the remaining data.
        """
        return(data[:lenght], data[lenght:])
