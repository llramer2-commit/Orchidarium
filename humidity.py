##sleep script between readings##
import time
import adafruit_dht
##import board library to use adafruit##
import board

##pass function to pin on DHT22 sensor connected to pi
<<<<<<< HEAD
dht_device = adafruit_dht.DHT22(board.D4)
=======
dht_device = adafruit_dht.DHT22(board.D3)
>>>>>>> 5b2cb53f73269ecf987e34b4a945a455809d892c

##start and infinite loop to read humidity constantly##
while True: 
    try: 
        temperature_ = dht_device.temperature

        humidity = dht_device.humidity

        print("Temp:{:.1f} C/{:.1f} C    Humidity: {}%".format(temperature_c, humidity))
    except RuntimeError as error:
        print(err.args[0])

<<<<<<< HEAD
        time.sleep(2.0)
=======
        time.sleep(2.0)
>>>>>>> 5b2cb53f73269ecf987e34b4a945a455809d892c
