from sense_hat import SenseHat
from time import sleep
import requests
import sys

sense = SenseHat()
sense.clear()

# Constants
WRITE_API_KEY = "RVZQOKHCZL4IM94H"
BASE_URL = "https://api.thingspeak.com/update"
POST_DELAY_MINUTES = 10 # 5 minutes


payload = {"api_key": WRITE_API_KEY,
           "field1": "",
           "field2": "",
           "field3": ""}

try:
    while True:
            
        temperature = round(sense.temperature, 2) # Celcius
        humidity = round(sense.humidity, 2) # Percentage of relative humidity
        pressure = round(sense.pressure, 2) # Millibars
    
        payload.update({"field1": str(temperature),
                    "field2": str(humidity),
                    "field3": str(pressure)})
    
        request = requests.post(BASE_URL, params=payload)
        
        print("Updated")
        sleep(POST_DELAY_MINUTES)

except:
    sys.exit()
    