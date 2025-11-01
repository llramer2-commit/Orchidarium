##allow script to sleep between readings
import time

##talk and interact with DHT22 sensor
import adafruit_dht
import board

dht_device = adafruit_dht.DHT22(board.D3)

#Get readings from sensor constantly
while True: 
    try: 
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity

        print("Temp:{:.1f} C / {:.1f} C Humidity: {}%.format(temperature_c, humidity)")
    except RuntimeError as error: 
        print(err.args[0])
        
        time.sleep(2.0)

        