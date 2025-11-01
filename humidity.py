##sleep script between readings##
import time
import adafruit_dht
##import board library to use adafruit##
import board

##pass function to pin on DHT22 sensor connected to pi
dht_device = adafruit_dht.DHT22(board.D4)

##start and infinite loop to read humidity constantly##
while True: 
    try: 
        temperature_ = dht_device.temperature

        humidity = dht_device.humidity

        print("Temp:{:.1f} C/{:.1f} C    Humidity: {}%".format(temperature_c, humidity))
    except RuntimeError as error:
        print(err.args[0])

        time.sleep(2.0)