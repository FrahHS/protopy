import uuid
import zlib

from protopy.client import Client
from protopy.datatypes.varint import Varint

from protopy.packets import serverboundpackets
from protopy.packets import clientbountpackets

from protopy.packets.clientbountpackets import LoginSuccessPacket, SetCompressionPacket, FinishConfigurationPacket
from protopy.packets.clientbountpackets.play.clientboundkeepalive import ClientboundKeepAlivePacket
from protopy.packets.serverboundpackets import ServerboundKeepAlivePacket, HandshakePacket, StatusRequestPacket, LoginStartPacket, LoginAcknowledged, PingRequestPacket, LoginAcknowledged, ClientInformationConfigurationPacket
from protopy.packets.packet import Packet, PacketDirection, PacketMode, UnknowPacket
from protopy.utils import logger

host = 'localhost'
port = 25565

client = Client(host, port)

client.connect()

@client.listener()
def _l(packet):
    if(isinstance(packet, UnknowPacket)):
        #logger.warning(f'Packet not found!')
        logger.debug(f'packet_id: {hex(packet.packet_id.int)}')
        #logger.debug(f'raw_data: {packet.raw_data}')
        #logger.debug(f'packet_direction: {packet.direction}')
        #logger.debug(f'packet_mode: {packet.mode}')
        #logger.debug(f'packet_raw_data: {raw_data}\n')
        pass
    else:
        logger.info(f'packet_id: {packet.PACKET_ID}')

    if(isinstance(packet, LoginSuccessPacket)):
        client.sendPacket(LoginAcknowledged())
        pass

    if(isinstance(packet, clientbountpackets.FinishConfigurationPacket)):
        client.sendPacket(serverboundpackets.FinishConfigurationPacket())
        pass

    if(isinstance(packet, ClientboundKeepAlivePacket)):
        logger.info("keep alive received")
        logger.info(packet.keep_alive_id)
        logger.info(packet.raw_data)

        packet_length, body = Varint.unpack(packet.raw_data)
        data_length, body = Varint.unpack(body)
        body = zlib.decompress(body) if data_length != 0 else body
        packet_id, body = Varint.unpack(body)

        logger.info(body)

        client.sendPacket(ServerboundKeepAlivePacket(body, True))

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
    'Steve',
    uuid.UUID('d9f0fa31-b299-49a7-989e-d7a1e34a87f7')
)
client.sendPacket(login_start_packet)
