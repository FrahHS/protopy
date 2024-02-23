from protopy.datatypes.datatypes import DataTypes
from protopy.packets.clientbountpackets import ClientBoundPacket
from protopy.packets.packet import PacketDirection, PacketMode
from protopy.packets.packetreader import PacketReader

class ClientBoundFinishConfigurationPacket(ClientBoundPacket):
    PACKET_ID = b'\x02'
    DIRECTION = PacketDirection.CLIENT
    MODE = PacketMode.CONFIGURATION
    NEXT_MODE = PacketMode.CONFIGURATION

    def __init__(self, raw_data: bytes, is_compressed: bool = False) -> None:
        super().__init__(raw_data, is_compressed)

    def _read(self, body):
        pass
