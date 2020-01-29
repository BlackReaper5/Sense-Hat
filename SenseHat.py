from sense_hat import SenseHat, ACTION_RELEASED
from time import sleep
import requests
import sys


sense = SenseHat()
sense.clear()


# Constants
WRITE_API_KEY = "RVZQOKHCZL4IM94H"
BASE_URL = "https://api.thingspeak.com/update"
POST_DELAY_MINUTES = 10 * 60 # 10 minutes interval before uploading weather data


# Data to send to ThingSpeak inclusive the write API key
payload = {"api_key": WRITE_API_KEY,
           "field1": "",
           "field2": "",
           "field3": ""}


# Red
R = [255, 0, 0]


# White
W = [255, 255, 255]


# Green
G = [0, 255, 0]


# The mark to show when the Sense Hat is terminated
X_MARK = [
R, W, W, W, W, W, W, R,
W, R, W, W, W, W, R, W,
W, W, R, W, W, R, W, W,
W, W, W, R, R, W, W, W,
W, W, W, R, R, W, W, W,
W, W, R, W, W, R, W, W,
W, R, W, W, W, W, R, W,
R, W, W, W, W, W, W, R
]


# The mark to show when the Sense Hat sends data to ThingSpeak
O_MARK = [
W, W, G, G, G, G, W, W,
W, G, W, W, W, W, G, W,
G, W, W, W, W, W, W, G,
G, W, W, W, W, W, W, G,
G, W, W, W, W, W, W, G,
G, W, W, W, W, W, W, G,
W, G, W, W, W, W, G, W,
W, W, G, G, G, G, W, W
]


# The data to send to ThingSpeak
temperature = 0
humidity = 0
pressure = 0


def format_data(data):
    """Returns sensed data rounded to 2 decimals as a String"""
    return str(round(data, 2))


def is_action_released(event):
    """Checks if action is released"""
    if event.action == ACTION_RELEASED: return True; return False


def get_temperature():
    """Returns the temperature in degrees Celcius"""
    return format_data(sense.temperature)  


def get_humidity():
    """Returns the percentage of relative humidity"""
    return format_data(sense.humidity)  
    

def get_pressure():
    """Returns the pressure in Millibars"""
    return format_data(sense.pressure) 


def show_temperature(event):
    """Shows the temperature on the 8x8 LEDs"""
    if is_action_released(event): sense.show_message(temperature)
     
     
def show_humidity(event):
    """Shows the humidity on the 8x8 LEDs"""
    if is_action_released(event): sense.show_message(humidity)
        

def show_pressure(event):
    """Shows the pressure on the 8x8 LEDs"""
    if is_action_released(event): sense.show_message(pressure)
    
    
def upload_data(payload):
    """Uploads the temperature, humidity and pressure to ThingSpeak"""
    requests.post(BASE_URL, params=payload)
    sense.set_pixels(O_MARK)
    

try:
    while True:
        # Get the new sensed data
        temperature = get_temperature()
        humidity = get_humidity()
        pressure = get_pressure()

        # Update payload with newly sensed data
        payload.update({
            "field1": temperature,
            "field2": humidity,
            "field3": pressure})
        
        # Upload newly sensed data
        upload_data(payload)
    
        # Listen for joystick actions
        sense.stick.direction_middle = show_temperature
        sense.stick.direction_left = show_humidity
        sense.stick.direction_right = show_pressure
        
        # Time-out before sending data to ThingSpeak again
        sleep(POST_DELAY_MINUTES)

except KeyboardInterrupt:
    # Show a red X mark when an exception happens, in this case when manually interrupting with the keyboard (CTRL-C)
    sense.set_pixels(X_MARK)
    
