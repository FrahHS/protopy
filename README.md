
<p align="center">
  <a href="https://protopy.gitbook.io/protopy/"><img src="https://i.imgur.com/0RFOsZA.png" alt="ProtoPY"></a>
</p>
<p align="center">
    <em>ProtoPY, Minecraft protocol in python</em>
</p>

---

**Documentation**: <a href="https://protopy.gitbook.io/protopy/" target="_blank">https://protopy.gitbook.io/protopy/</a>

**Source Code**: <a href="https://github.com/FrahHS/protopy" target="_blank">https://github.com/FrahHS/protopy</a>

---

ProtoPY is a Python library that allows interacting with the Minecraft protocol in a simple and efficient manner.


* **Fast to code**: Really quick to develop features, especially if you're already familiar with Bukkit plugin development, packet handling is very similar to event handling.

## Installation

<div class="termy">

```console
$ pip install protopy
```

</div>

## Example

* Create a file `main.py` with:

```Python
import time

from protopy import ProtoPY
from protopy.packets.clientbountpackets import ClientBoundFinishConfigurationPacket


host = 'localhost'
port = 25565

client = ProtoPY(host=host, port=port, protocol_version=765)

client.login('XSteve')

@client.listener(ClientBoundFinishConfigurationPacket)
def on_login(packet: ClientBoundFinishConfigurationPacket):
    print("Connected!")
```

## License

This project is licensed under the terms of the GPL-3.0 license.
