# WeatherCloud.py - A simple, Raspberry Pi based weather station, that sends data
# to an Azure IoT Hub.
# ------------------------------------------------------------------------------

import time
import Si7021
import pigpio

pi = pigpio.pi()
s = Si7021.sensor(pi)

# set the resolution
# 0 denotes the maxium available: Humidity 12 bits, Temperature 14 bits
# See the documentation for more details
s.set_resolution(0)

# get the environment data
temperature = s.temperature()
humidity = s.humidity()

print("{:.3f} °C".format(temperature) + " | {:.3f} %rH".format(humidity))

s.cancel()
pi.stop()

# Prepare the message
textHumidity = "Relative Humidity is : %.3f %%rH" %humidity
textTemperature = "Temperature in Celsius is : %.3f °C" %temperature
messageText = textHumidity + " " + textTemperature

# Post the data to an azure IoT Hub
import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient

import yaml
with open("WeatherCloud.config.yml", "r") as configFile:
    config = yaml.safe_load(configFile)


async def main():
    # Fetch the connection string from the configuration
    conn_str = config['deviceConnectionString']

    # Create instance of the device client using the connection string
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the device client.
    await device_client.connect()

    # Send a single message
    print("Sending message...")
    await device_client.send_message(messageText")
    print("Message successfully sent!")

    # finally, disconnect
    await device_client.disconnect()


if __name__ == "__main__":
    # asyncio.run(main())

    # If using Python 3.6 or below, use the following code instead of asyncio.run(main()):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
