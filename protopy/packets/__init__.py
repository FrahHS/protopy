from packets.packet import Packet
from packets.packet import PacketDirection
from packets.packet import PacketMode

from packets.serverboundpackets import *
from packets.clientbountpackets import *

all_packets = {}
for cls in ClientBoundPacket.__subclasses__():
    if hasattr(cls, 'PACKET_ID'):
        all_packets[(cls.PACKET_ID, cls.DIRECTION, cls.MODE)] = cls
for cls in ServerBoundPacket.__subclasses__():
    if hasattr(cls, 'PACKET_ID'):
        all_packets[(cls.PACKET_ID, cls.DIRECTION, cls.MODE)] = cls
Packet.all_packets = all_packets

#Packet.all_packets = {(cls.PACKET_ID, cls.DIRECTION, cls.MODE): cls for cls in Packet.__subclasses__()}


