import uuid, time

from protopy import ProtoPY

from protopy.packets import clientbountpackets
from protopy.packets.clientbountpackets import PlayerChatMessagePacket
from protopy.packets.serverboundpackets import ChatMessagePacket

host = 'localhost'
port = 25565

client = ProtoPY(host=host, port=port, protocol_version=765)
client.login('XSteve', uuid.UUID('6accdd58-b3fb-4c15-a87b-335b717627b3'))

@client.listener()
def _l(packet):
    if(isinstance(packet, PlayerChatMessagePacket)):
        if(packet.sender_name != 'XSteve'):
            print(f'{packet.sender_name}: {packet.message}')

    if(isinstance(packet, clientbountpackets.FinishConfigurationPacket)):
        message_packet = ChatMessagePacket(
            message="I'm a bot made using Protopy",
            timestamp=round(time.time() * 1000),
            salt=0,
            has_signature=False,
            message_count=0, 
            acknowledged=b'\x00\x00\x00',
        )
        client.sendPacket(message_packet)

while True:
    msg = input()
    message_packet = ChatMessagePacket(
        message= msg,
        timestamp=round(time.time() * 1000),
        salt=0,
        has_signature=False,
        message_count=0, 
        acknowledged=b'\x00\x00\x00',
    )
    client.sendPacket(message_packet)
