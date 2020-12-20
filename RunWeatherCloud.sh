#!/bin/bash
# Prepares the pigpiod daemon and runs the WeatherCloud python script

# start the daemon, if not running
if ! ps -u root | grep -q pigpiod; then
    echo "starting pigpiod..."
    sudo pigpiod
fi
echo "pigpiod is running."


# start the WeatherCloud.py script
python3 WeatherCloud.py

# optionally, terminate the pigpiod daemon
# sudo killall pigpiod
