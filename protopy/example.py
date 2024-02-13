from threading import Thread
import time
import uuid

from client import Client
from packets import HandshakePacket, StatusRequestPacket, LoginStartPacket, LoginAcknowledged, LoginSuccessPacket, PingRequestPacket, LoginAcknowledged
from packets.configuration.serverbound.clientinformationconfiguration import ClientInformationConfigurationPacket
from packets.packet import UnknowPacket

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

print(((client_information_configuration_packet.packet(True))))

@client.listener()
def _l(packet):
    if(isinstance(packet, UnknowPacket)):
        return

    if(isinstance(packet, LoginSuccessPacket)):
        print(packet.response)
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

# Status Request
#statusRequestPacket = StatusRequestPacket()
#client.sendPacket(statusRequestPacket)

# Ping Request
#pingRequestPacket = PingRequestPacket()
#client.sendPacket(pingRequestPacket)
