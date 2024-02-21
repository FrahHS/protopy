import uuid
import zlib

from protopy import ProtoPY
from protopy.datatypes.varint import Varint

from protopy.packets.clientbountpackets import PlayerChatMessagePacket
from protopy.utils import logger

host = 'localhost'
port = 25565

client = ProtoPY(host, port)
client.login('XSteve', uuid.uuid4())

@client.listener()
def _l(packet):
    if(isinstance(packet, PlayerChatMessagePacket)):
        logger.info(f'{packet.response}')
        packet_length, body = Varint.unpack(packet.raw_data)
        data_length, body = Varint.unpack(body)
        body = zlib.decompress(body) if data_length != 0 else body
        logger.info(f'{body}')
