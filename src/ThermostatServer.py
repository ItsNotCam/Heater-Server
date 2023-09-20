# dependencies
import time, json, random
import asyncio
from websockets import serve

# heater server class
from TemperatureData import TemperatureData
import TemperatureReader as TR
from datetime import datetime

class ThermostatServer:
    def __init__(self):
        self.tempData = TemperatureData()

    # Run websocket server
    async def run(self):
        async with serve(self.start_server, "", 3005):
            await asyncio.Future()

    # Update the target temperature and save to disk
    def updateTargetTemperature(targetTemperature):
        self.tempData.data["target"] = targetTemperature
        self.tempData.saveState()

    async def start_server(self, websocket):
        print("Sending data task started")
        lastReadingTime = datetime.now()

        while True:
            # Read temperature from DHT11 every 5 seconds
            deltaTime = (lastReadingTime - datetime.now()).seconds
            if deltaTime >= 5:
                self.tempData.temperature = TR.read_temperature()
                lastReadingTime = datetime.now()

            message = json.loads(await websocket.recv())
            if message["action"] == "POST":
                self.tempData.target = message["target"]
                self.tempData.save_state()

            dataJSON = self.tempData.to_json_string()
            await websocket.send(dataJSON)

if __name__ == "__main__":
    thermostatServer = ThermostatServer()
    asyncio.run(thermostatServer.run())