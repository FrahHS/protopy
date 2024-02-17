from threading import Thread
import uuid

from client import Client

from packets.clientbountpackets import LoginSuccessPacket, PingResponsePacket, SetCompressionPacket
from packets.serverboundpackets import HandshakePacket, StatusRequestPacket, LoginStartPacket, LoginAcknowledged, PingRequestPacket, LoginAcknowledged, ClientInformationConfigurationPacket
#from packets.configuration.serverbound.clientinformationconfiguration import ClientInformationConfigurationPacket
from packets.packet import UnknowPacket
from utils import logger

host = 'localhost'
port = 25565

client = Client(host, port)

client.connect()

@client.listener()
def _l(packet):

    if(isinstance(packet, SetCompressionPacket)):
        logger.info(packet)
        print(packet.threshold)
    if(isinstance(packet, UnknowPacket)):
        return

    if(isinstance(packet, PingResponsePacket)):
        logger.debug(packet.ping)
        return

# Handshake
next_state = 1

handshake_packet = HandshakePacket(
    host,
    port,
    next_state
)
client.sendPacket(handshake_packet)

# Status Request
#statusRequestPacket = StatusRequestPacket()
#client.sendPacket(statusRequestPacket)

# Ping Request
pingRequestPacket = PingRequestPacket()
client.sendPacket(pingRequestPacket)
