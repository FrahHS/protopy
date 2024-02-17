from protopy.packets.packet import Packet
from protopy.packets.packet import PacketDirection
from protopy.packets.packet import PacketMode

from protopy.packets.serverboundpackets import *
from protopy.packets.clientbountpackets import *

all_packets = {}
for cls in ClientBoundPacket.__subclasses__():
    if hasattr(cls, 'PACKET_ID'):
        all_packets[(cls.PACKET_ID, cls.DIRECTION, cls.MODE)] = cls
for cls in ServerBoundPacket.__subclasses__():
    if hasattr(cls, 'PACKET_ID'):
        all_packets[(cls.PACKET_ID, cls.DIRECTION, cls.MODE)] = cls
Packet.all_packets = all_packets

#Packet.all_packets = {(cls.PACKET_ID, cls.DIRECTION, cls.MODE): cls for cls in Packet.__subclasses__()}


