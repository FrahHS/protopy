from protopy.packets.packet import Packet
from protopy.packets.packet import PacketDirection
from protopy.packets.packet import PacketMode

from protopy.packets.serverboundpackets import *
from protopy.packets.clientbountpackets import *

all_packets = {}
for cls in ClientBoundPacket.__subclasses__():
        all_packets[(cls.packet_id, cls.direction, cls.mode)] = cls
for cls in ServerBoundPacket.__subclasses__():
        all_packets[(cls.packet_id, cls.direction, cls.mode)] = cls
Packet.all_packets = all_packets


