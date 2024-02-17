from threading import Thread
import uuid

from client import Client

from packets.clientbountpackets import LoginSuccessPacket, SetCompressionPacket
from packets.serverboundpackets import HandshakePacket, StatusRequestPacket, LoginStartPacket, LoginAcknowledged, PingRequestPacket, LoginAcknowledged, ClientInformationConfigurationPacket
#from packets.configuration.serverbound.clientinformationconfiguration import ClientInformationConfigurationPacket
from packets.packet import UnknowPacket
from utils import logger

host = 'localhost'
port = 25565

client = Client(host, port)

client.connect()

client_information_configuration_packet = ClientInformationConfigurationPacket(
    locale = 'it_IT',
    view_distance = bytes.fromhex(hex(int('11111110', 2))[2:]),
    chat_mode = 0,
    chat_color = True,
    displayer_skin_parts = b'\x01',
    main_hand = 1,
    enable_text_filtering = False,
    allow_server_listing = True,
)

@client.listener()
def _l(packet):
    if(isinstance(packet, UnknowPacket)):
        return
    
    if(isinstance(packet, SetCompressionPacket)):
        logger.info(packet.threshold)

    if(isinstance(packet, LoginSuccessPacket)):
        logger.info(packet.response)
        client.sendPacket(LoginAcknowledged())
        client.sendPacket(client_information_configuration_packet)
        return

# Handshake
next_state = 2

handshake_packet = HandshakePacket(
    host,
    port,
    next_state
)
client.sendPacket(handshake_packet)

# Login Start
login_start_packet = LoginStartPacket(
    'Paxxo',
    uuid.UUID('d9f0fa31-b299-49a7-989e-d7a1e34a87f7')
)
client.sendPacket(login_start_packet)
