##allow script to sleep between readings
import time

##talk and interact with DHT22 sensor
import adafruit_dht
import board

dht_device = adafruit_dht.DHT22(board.D4)

#Get readings from sensor constantly
while True: 
    try: 
        temperature_c = dht_device.temperature
        temperature_f = temperature_c * (9/5) + 32
        humidity = dht_device.humidity

        print("Temp:{:.1f} C / {:.1f} F  Humidity: {}%.format(temperature_c, humidity)")
    except RuntimeError as error: 
        print(err.args[0])
        time.sleep(2.0)
        continue
    except Exception as error: 
        dht_device.exit()
        raise error
    
    time.sleep(3.0)

        