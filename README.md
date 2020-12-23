# WeatherCloud (This project is in Alpha-Stage!)

A simple, Raspberry Pi based weather station, that posts to an [Azure IoT Hub](https://azure.microsoft.com/en-us/services/iot-hub/). See my [//TODO blog post](https://qrys.ch) for details and how to install it. This project is based a former work on https://github.com/suterma/WeatherCloud

 - `Si7021.py` is a PiGPIO-based sensor reader
 - `WeatherCloud.py` is the implementation for this project.
 - `RunWeatherCloud.sh` is a script that prepares and runs a single measurement.
 
## Installation
This project requires an actual [Si7021 temperature and humidity sensor](https://www.digitec.ch/de/s1/product/adafruit-si7021-sensor-elektronikmodul-6310870). See my [blog post about how to set the SI7021 up with a Rasperry Pi](https://qrys.ch/a-raspberry-pi-based-weather-station-posting-to-wordpress/#setting-up-the-si7021-sensor). 

From there, within an SSH session you can now install this WeatherCloud client.

    # get git (Not included in the raspian lite version)
    sudo apt-get install git
    
    # install the Azure IoT SDK
    pip3 install azure-iot-device
     
    # clone the WeatherCloud repo
    cd /home/pi
    git clone git://github.com/suterma/WeatherCloud
    cd WeatherCloud
    sudo chmod u+x RunWeatherCloud.sh
    
Now, you need to configure the Iot Hub connection string.    


 
# Credits
 - PIBITS: Raspberry Pi and Si7021 sensor example
 - Joan at abyz.me.uk: Si7021 reader and PiGPIO daemon
