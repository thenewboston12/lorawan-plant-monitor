# LoRaWAN plant monitoring system

Using temperature and ambient light sensors to capture data

Sending data to The Things Network(TTN) cloud

### Project organization 
**/lib** folder contains the libraries used by sensors 

**decoder.js** is a script for decoding LoRaWAN messages in TTN(The Things Network) server

**lorawan.py** contains helper methods for connecting to LoRaWAN of TTN

**sensors.py** is a helper python script that takes measurements and returns them

