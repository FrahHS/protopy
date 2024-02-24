from protopy.client.tcpclient import TcpClient
from protopy.utils import logger
from protopy.utils.getuuid import get_uuid

from protopy.packets.clientbountpackets import LoginSuccessPacket, SetCompressionPacket, ClientboundKeepAlivePacket, DisconnectPlayPacket, ClientBoundFinishConfigurationPacket
from protopy.packets.serverboundpackets import HandshakePacket, LoginAcknowledged, LoginStartPacket,ServerboundKeepAlivePacket, ServerBoundFinishConfigurationPacket

class ProtoPY(TcpClient):
    def __init__(self, host: str, port: int, protocol_version: int, buffer_size: int = 1024) -> None:
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
            self.sendPacket(ServerboundKeepAlivePacket(keep_alive_id=packet.keep_alive_id, is_compressed=packet.is_compressed))

        super()._packets_handler(packet)

    def login(self, username: str):
        # Handle login and configuration
        def _listener(packet):
            if(isinstance(packet, LoginSuccessPacket)):
                self.sendPacket(LoginAcknowledged())

            if(isinstance(packet, ClientBoundFinishConfigurationPacket)):
                self.sendPacket(ServerBoundFinishConfigurationPacket())
                logger.info('Logged in')

            if(isinstance(packet, DisconnectPlayPacket)):
                logger.info(f'Disconnected: {packet.reason}')

        #self.packets_listeners.insert(0, _listener)
        self.add_listener(None, _listener)

        # Handshake
        next_state = 2

        handshake_packet = HandshakePacket(
            protocol_version=self.protocol_version,
            server_address=self.host,
            server_port=self.port,
            next_state=next_state,
        )

        # Login Start
        login_start_packet = LoginStartPacket(
            name=username,
            player_uuid=get_uuid(username),
        )

        self.sendPacket(handshake_packet)
        logger.debug("handshake")
        self.sendPacket(login_start_packet)
        logger.debug("login start...")

