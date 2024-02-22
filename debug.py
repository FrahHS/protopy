import uuid

from protopy import ProtoPY

from protopy.packets.clientbountpackets import PlayerChatMessagePacket

host = 'localhost'
port = 25565

client = ProtoPY(host, port)
client.login('XSteve', uuid.UUID('6accdd58-b3fb-4c15-a87b-335b717627b3'))

@client.listener()
def _l(packet):
    if(isinstance(packet, PlayerChatMessagePacket)):
        print(packet.message)
