from packets.packet import Packet
from packets.packet import PacketDirection
from packets.packet import PacketMode

Packet.all_packets = {(cls.PACKET_ID, cls.DIRECTION, cls.MODE): cls for cls in Packet.__subclasses__()}

from packets.serverboundpackets import ServerBoundPacket
from packets.clientbountpackets import ClientBoundPacket
