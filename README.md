# wifidos
Python script based on aireplay-ng to keep deauthenticating the specified stations from your WiFi network. 


```python
from .wifidos import Wifidos

network = "00:00:00:00:00:00"

victims = [
            "00:00:00:00:00:11",
            "00:00:00:00:00:22",
            "00:00:00:00:00:33",
            "00:00:00:00:00:44",
            "00:00:00:00:00:55"
        ]

wifidos = Wifidos(network=network, victims=victims)
wifidos.start()
```