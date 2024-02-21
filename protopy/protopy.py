from uuid import UUID
import zlib

from protopy.client.tcpclient import TcpClient
from protopy.datatypes.varint import Varint
from protopy.packets import clientbountpackets
from protopy.packets import serverboundpackets
from protopy.packets.clientbountpackets.login.loginsuccess import LoginSuccessPacket
from protopy.packets.serverboundpackets.handshaking.handshake import HandshakePacket
from protopy.packets.serverboundpackets.login.loginacknowledged import LoginAcknowledged
from protopy.packets.serverboundpackets.login.loginstart import LoginStartPacket
from protopy.utils import logger

from protopy.packets.clientbountpackets import SetCompressionPacket, ClientboundKeepAlivePacket
from protopy.packets.serverboundpackets import ServerboundKeepAlivePacket

class ProtoPY(TcpClient):
    def __init__(self, host: str, port: int, buffer_size: int = 2097151) -> None:
        super().__init__(host, port, buffer_size)
        self.connect()

    def packets_handler(self, packet):
        # Check for compression
        if(isinstance(packet, SetCompressionPacket)):
            self.compression = True
            self.threshold = packet.threshold

        # Handle keep Alive
        if(isinstance(packet, ClientboundKeepAlivePacket)):
            logger.info("keep alive received")

            packet_length, body = Varint.unpack(packet.raw_data)
            data_length, body = Varint.unpack(body)
            body = zlib.decompress(body) if data_length != 0 else body
            packet_id, body = Varint.unpack(body)

            self.sendPacket(ServerboundKeepAlivePacket(body, True))


        super().packets_handler(packet)

    def login(self, username: str, uuid: UUID):
        # Handshake
        next_state = 2

        handshake_packet = HandshakePacket(
            self.host,
            self.port,
            next_state
        )
        self.sendPacket(handshake_packet)

        # Login Start
        login_start_packet = LoginStartPacket(
            username,
            uuid
        )
        self.sendPacket(login_start_packet)

        # Handle login and configuration
        def _l(packet):
            if(isinstance(packet, LoginSuccessPacket)):
                self.sendPacket(LoginAcknowledged())

            if(isinstance(packet, clientbountpackets.FinishConfigurationPacket)):
                self.sendPacket(serverboundpackets.FinishConfigurationPacket())
                self.dispose_listener(_l)

        self.add_listener(_l)
