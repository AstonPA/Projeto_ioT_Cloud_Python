import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(f'Temperatura: {temperature}°C, Umidade: {humidity}%')
    else:
        print('Falha ao ler o sensor. Tente novamente!')

    time.sleep(2)  
