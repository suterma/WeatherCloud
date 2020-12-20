# WeatherCloud (This project is in Alpha-Stage!)

A simple, Raspberry Pi based weather station, that posts to an [Azure IoT Hub](https://azure.microsoft.com/en-us/services/iot-hub/). See my [//TODO blog post](https://qrys.ch) for details and how to install it. This project is based a former work on https://github.com/suterma/WeatherCloud

 - `Si7021.py` is a PiGPIO-based sensor reader
 - `WeatherCloud.py` is the implementation for this project.
 - `RunWeatherCloud.sh` is a script that prepares and runs a single measurement.
 
 # Credits
 - PIBITS: Raspberry Pi and Si7021 sensor example
 - Joan at abyz.me.uk: Si7021 reader and PiGPIO daemon
