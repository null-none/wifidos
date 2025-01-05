from .wifidos import Wifidos

network = "00:00:00:00:00:00"
victims = ["00:00:00:00:00:00", 
           "00:00:00:00:00:00"]

wifidos = Wifidos(network=network, victims=victims)
wifidos.start()