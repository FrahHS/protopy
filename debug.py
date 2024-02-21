import uuid

from protopy import ProtoPY
from protopy.utils import logger

host = 'localhost'
port = 25565

client = ProtoPY(host, port)
client.login('Steve', uuid.uuid4())

@client.listener()
def _l(packet):
    id = packet.PACKET_ID
    logger.info(f'[PACKET RECEIVED] packet_id: {(id.hex())}')
