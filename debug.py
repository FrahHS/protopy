import logging
import time

from protopy import ProtoPY
from protopy.datatypes.bitset import BitSet

from protopy.packets.clientbountpackets import PlayerChatMessagePacket, ClientBoundFinishConfigurationPacket
from protopy.packets.serverboundpackets import ChatMessagePacket
from protopy.utils import logger
logger.setLevel(logging.DEBUG)

host = 'localhost'
port = 25565

client = ProtoPY(host=host, port=port, protocol_version=765)

client.login('XSteve')

@client.listener
def l(packet: PlayerChatMessagePacket):
    if(packet.sender_name != 'XSteve'):
        print(f'{packet.sender_name}: {packet.message}')

@client.listener
def l(packet: ClientBoundFinishConfigurationPacket):
    message_packet = ChatMessagePacket(
        message="I'm a bot made using Protopy",
        timestamp=round(time.time() * 1000),
        salt=0,
        has_signature=False,
        message_count=0,
        acknowledged=BitSet(20).tobytes(),
    )
    client.sendPacket(message_packet)
