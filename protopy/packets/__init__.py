from protopy.packets.packet import Packet

from protopy.packets.serverboundpackets import *
from protopy.packets.clientbountpackets import *

for cls in ClientBoundPacket.__subclasses__():
    Packet.all_packets[(cls.packet_id, cls.direction, cls.mode)] = cls
for cls in ServerBoundPacket.__subclasses__():
    Packet.all_packets[(cls.packet_id, cls.direction, cls.mode)] = cls
