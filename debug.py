import uuid

from protopy import ProtoPY

from protopy.packets.clientbountpackets import PlayerChatMessagePacket
from protopy.packets.clientbountpackets.play.disconnectplay import DisconnectPlayPacket
from protopy.utils import logger

host = 'localhost'
port = 25565

client = ProtoPY(host=host, port=port, protocol_version=765)
client.login('XSteve', uuid.UUID('6accdd58-b3fb-4c15-a87b-335b717627b3'))

@client.listener()
def _l(packet):
    if(isinstance(packet, PlayerChatMessagePacket)):
        print(f'{packet.sender_name["text"]}: {packet.message}')
    if(isinstance(packet, DisconnectPlayPacket)):
        print(packet.reason)
