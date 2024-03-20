# Packets Listeners

In ProtopPY è davvero semplice ricevere e lavorare sui pacchetti ricevuti.\
\
Innanzitutto è  necesario definite un client:\


```python
client = ProtoPY(...)
```

A questo punto è davvero semplice creare un listener usando il seguente decoratore:

<pre class="language-python"><code class="lang-python"><strong>@client.listener
</strong>def on_login(packet: PlayerChatMessagePacket):
    pass
</code></pre>

Specificare il parametro della funzione ha l'effetto di filtro, in questo caso il listener `on_login` verrà chiamata ogni volta che il server invierà un pacchetto di ClientBoundFinishConfigurationPacket.

In questo modo puoi definire tutti i listener che vuoi:

```python
...

@client.listener
def on_login(packet: ClientBoundFinishConfigurationPacket):
    # Some code

@client.listener
def chat_message(packet: ChatMessagePacketr):
    # Some code

...
```

\
Nel caso nessun tipo venga specificato la funzione riceverà tutti i pacchetti inviati dal server, questo modo di agire è molto sconsigliato a meno di particolari necessità

## Lavorare con più listener allo stesso tempo

E' possibile lavorare con più listener annidati, esempio:

<pre class="language-python"><code class="lang-python">@client.listener
def listener1(packet: ...):
    @client.listener
<strong>    def listener2(packet: ...):
</strong>        # Some code
    client.dispose_listener(listener2)
</code></pre>

ricorda di disporre i listener di cui non hai più bisogno, o questi continueranno a lavorare per tutta l'esecuzione del programma.



