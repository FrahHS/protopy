# Get started

### Startup a client

* Create a file `main.py` with:

```python
from protopy import ProtoPY
from protopy.packets.clientbountpackets import ClientBoundFinishConfigurationPacket


host = 'localhost'
port = 25565
protocol_version = 765

client = ProtoPY(host=host, port=port, protocol_version=protocol_version)

client.login('XSteve')

@client.listener
def on_login(packet: ClientBoundFinishConfigurationPacket):
    print("Connected!")
```

Here is a simple example of how to create and manage a simple connection.

