from packets.packet import Packet

# Handshaking bound to Server
from packets.handshaking.serverbound.handshake import HandshakePacket

# Status bound to Client
from packets.status.clientbound.statusresponse import StatusResponsePacket
from packets.status.clientbound.pingresponse import PingResponsePacket

# Status bound to Server
from packets.status.serverbound.statusrequest import StatusRequestPacket
from packets.status.serverbound.pingrequest import PingRequestPacket

# Login bound to Client
from packets.login.clientbound.loginsuccess import LoginSuccessPacket
from packets.login.clientbound.setcompression import SetCompressionPacket

# Login bound to Server
from packets.login.serverbound.loginstart import LoginStartPacket
from packets.login.serverbound.loginacknowledged import LoginAcknowledged


Packet.all_packets = {(cls.PACKET_ID, cls.DIRECTION, cls.MODE): cls for cls in Packet.__subclasses__()}
