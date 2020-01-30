# Sense-Hat
* I made a simple Weather Station with a Sense Hat attached to a Raspberry Pi 3 B+.

* But what is a Sense Hat?

* The [Raspberry Pi site](https://www.raspberrypi.org/products/sense-hat/) states the following ->

> The Sense HAT is an add-on board for Raspberry Pi, made especially for the Astro Pi mission – it launched to the International Space Station in December 2015 – and is now available to buy.

> The Sense HAT has an 8×8 RGB LED matrix, a five-button joystick and includes the following sensors:

> ### Gyroscope
> ### Accelerometer
> ### Magnetometer
> ### Temperature
> ### Barometric pressure
> ### Humidity

_For this project I only used the **Temperature**, **Barometric pressure** and **Humidity** sensors_

* Every 10 minutes the current **Temperature in degrees Celcius**, **Barometric pressure in Millibars** and the **percentage of relative Humidity** is uploaded to ThingSpeak
* When data is uploaded to ThingSpeak a green circle is shown
* Middle clicking on the joystick shows the last measured Temperature on the 8x8 LED's
* Moving the joystick to the left shows the last measured Humidity
* Moving the joystick to the right shows the last measured Barometric pressure
* When the program terminates a red cross is shown

[See uploaded data here at ThingSpeak](https://thingspeak.com/channels/972879)

### Raspberry Pi 3B+ with the Sense Hat attached to it
<img src="images/RaspberryPiSenseHat.jpg" width="300">


### When the temperature, barometric pressure and humidity has been uploaded to ThingSpeak
<img src="images/SentData.jpg" width="300">


### Barometric pressure is showing
<a href="https://imgflip.com/gif/3nm2ju"><img src="https://i.imgflip.com/3nm2ju.gif" title="made at imgflip.com"/></a>


### When the program is terminated
<img src="images/Exception.jpg" width="300">

