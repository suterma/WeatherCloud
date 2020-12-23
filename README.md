# WeatherCloud

A simple, Raspberry Pi based weather station, that posts to an [Azure IoT Hub](https://azure.microsoft.com/en-us/services/iot-hub/). See my [//TODO blog post](https://qrys.ch) for details and how to install it. This project is based a former work on https://github.com/suterma/WeatherCloud

 - `Si7021.py` is a PiGPIO-based sensor reader
 - `WeatherCloud.py` is the implementation for this project.
 - `RunWeatherCloud.sh` is a script that prepares and runs a single measurement.
 
## Installation
This project requires an actual [Si7021 temperature and humidity sensor](https://www.digitec.ch/de/s1/product/adafruit-si7021-sensor-elektronikmodul-6310870). See my [blog post about how to set the SI7021 up with a Rasperry Pi](https://qrys.ch/a-raspberry-pi-based-weather-station-posting-to-wordpress/#setting-up-the-si7021-sensor). 

From there, within an SSH session you can now install this WeatherCloud client.

    # get git and python3 (Not included in the raspian lite version)
    sudo apt-get install git python3 python3-pip
    
    # install the Azure IoT device SDK
    pip3 install azure-iot-device
     
    # clone the WeatherCloud repo
    cd /home/pi
    git clone git://github.com/suterma/WeatherCloud
    cd WeatherCloud
    sudo chmod u+x RunWeatherCloud.sh
    
Now, you need to [register this new device with Azure IoT hub](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-python-python-device-management-get-started#register-a-new-device-in-the-iot-hub) and configure the resulting "IoT Hub device connection string" in the WeatherCloud.config.yml file:

    sudo nano WeatherCloud.config.yml
    
 ## Run
 
    # Test out the weather station:
    ./RunWeatherCloud.sh
    
You can also have it post data perodically, e.g. using the crontab file:

    crontab -e
    # Add a line similar to this one at the end
    # */15 * * * * cd /home/pi/WeatherCloud && ./RunWeatherCloud.sh
    
This will send a new message every 15 minutes
