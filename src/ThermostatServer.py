# dependencies
import time, json, random
import asyncio
from websockets import serve

# heater server class
from TemperatureData import TemperatureData
import TemperatureReader as TR
from HueControl import HueControl
from Logger import Logger

from datetime import datetime
import requests
import threading

class ThermostatServer:
    def __init__(self):
        self.tempData = TemperatureData()
        self.hueControl = HueControl()

    # Run websocket server
    async def run(self):
        heaterControlThread = threading.Thread(target=self.heater_control_thread)
        heaterControlThread.start()

        async with serve(self.start_server, "", 3005):
            await asyncio.Future()

        heaterControlThread.join()

    def heater_control_thread(self):
        # Read temperature from DHT11 every 5 seconds
        lastReadingTime = datetime.now()

        while True:
            deltaTime = (lastReadingTime - datetime.now()).seconds
            if deltaTime >= 5:
                self.tempData.temperature = TR.read_temperature()
                lastReadingTime = datetime.now()

            self.hueControl.set_state(self.tempData.temperature < self.tempData.target)
            time.sleep(1)

    # Update the target temperature and save to disk
    def updateTargetTemperature(targetTemperature):
        self.tempData.data["target"] = targetTemperature
        self.tempData.saveState()

    async def start_server(self, websocket):
        Logger.log("Sending data task started")

        while True:
            message = json.loads(await websocket.recv())
            if message["action"] == "POST":
                self.tempData.target = message["target"]
                self.tempData.save_state()
                
                target = self.tempData.target
                Logger.log(f"Changed target to {target}")

            dataJSON = self.tempData.to_json_string()
            await websocket.send(dataJSON)

            target = self.tempData.target
            temperature = self.tempData.temperature
            Logger.log(f"Temperature: {temperature} Target: {target}")

if __name__ == "__main__":
    thermostatServer = ThermostatServer()
    asyncio.run(thermostatServer.run())