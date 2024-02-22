import uuid
import zlib

from protopy import ProtoPY
from protopy.datatypes.varint import Varint

from protopy.packets.clientbountpackets import PlayerChatMessagePacket
from protopy.utils import logger

host = 'localhost'
port = 25565

client = ProtoPY(host, port)
client.login('XSteve', uuid.UUID('6accdd58-b3fb-4c15-a87b-335b717627b3'))

@client.listener()
def _l(packet):
    if(isinstance(packet, PlayerChatMessagePacket)):
        logger.info(packet.message)
