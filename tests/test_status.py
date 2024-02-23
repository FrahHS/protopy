import time

import pytest

from protopy.client.tcpclient import TcpClient
from protopy.packets.clientbountpackets import StatusResponsePacket, PingResponsePacket
from protopy.packets.serverboundpackets import HandshakePacket, StatusRequestPacket, PingRequestPacket

class TestClassDemoInstance:
    def setup_method(self):
        host = 'localhost'
        port = 25565

        self.client = TcpClient(host=host, port=port)
        self.client.connect()

        # Handshake
        next_state = 1
        handshake_packet = HandshakePacket(
            765,
            host,
            port,
            next_state
        )
        self.client.sendPacket(handshake_packet)


    def test_ping(self):
        response = False

        @self.client.listener(PingResponsePacket)
        def _l(packet: PingResponsePacket):
            nonlocal response
            assert isinstance(packet.ping, int)
            response = True

        # Ping Request
        pingRequestPacket = PingRequestPacket()
        self.client.sendPacket(pingRequestPacket)

        # Wait until response becomes True or 5 seconds have elapsed
        timeout = 5
        interval = 0.1  # 100 ms
        start_time = time.time()

        while not response:
            if time.time() - start_time > timeout:
                break
            time.sleep(interval)

        if response:
            assert response  # Ensure the response is True at the end
        else:
            raise pytest.fail("Ping response not received")


    def test_status(self):
        @self.client.listener(StatusResponsePacket)
        def _l(packet: StatusResponsePacket):
            print(packet.json_response)
            return

        # Ping Request
        statusRequestPacket = StatusRequestPacket()
        self.client.sendPacket(statusRequestPacket)
