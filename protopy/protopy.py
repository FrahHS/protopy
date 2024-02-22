from uuid import UUID
import zlib

from protopy.client.tcpclient import TcpClient
from protopy.datatypes.varint import Varint

from protopy.utils import logger

from protopy.packets import clientbountpackets
from protopy.packets import serverboundpackets
from protopy.packets.clientbountpackets import LoginSuccessPacket, SetCompressionPacket, ClientboundKeepAlivePacket
from protopy.packets.serverboundpackets import HandshakePacket, LoginAcknowledged, LoginStartPacket,ServerboundKeepAlivePacket

class ProtoPY(TcpClient):
    def __init__(self, host: str, port: int, protocol_version: int, buffer_size: int = 2097151) -> None:
        super().__init__(host, port, buffer_size)
        self.protocol_version = protocol_version
        self.connect()

    def _packets_handler(self, packet):
        # Check for compression
        if(isinstance(packet, SetCompressionPacket)):
            self.compression = True
            self.threshold = packet.threshold

        # Handle keep Alive
        if(isinstance(packet, ClientboundKeepAlivePacket)):
            logger.debug("keep alive")
            self.sendPacket(ServerboundKeepAlivePacket(packet.keep_alive_id, packet.is_compressed))

        super()._packets_handler(packet)

    def login(self, username: str, uuid: UUID):
        # Handshake
        next_state = 2

        handshake_packet = HandshakePacket(
            self.protocol_version,
            self.host,
            self.port,
            next_state
        )
        self.sendPacket(handshake_packet)
        logger.debug("handshake")

        # Login Start
        login_start_packet = LoginStartPacket(
            username,
            uuid
        )
        self.sendPacket(login_start_packet)
        logger.debug("login start...")

        # Handle login and configuration
        def _l(packet):
            if(isinstance(packet, LoginSuccessPacket)):
                self.sendPacket(LoginAcknowledged())

            if(isinstance(packet, clientbountpackets.FinishConfigurationPacket)):
                self.sendPacket(serverboundpackets.FinishConfigurationPacket())
                self.dispose_listener(_l)
                logger.info('Logged in')

        self.add_listener(_l)
