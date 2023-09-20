# dependencies
import time, json, random
import asyncio, tornado

# heater server class
from TemperatureData import TemperatureData
import TemperatureReader as TR

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
        recv = asyncio.create_task(self.recv_temperature_data(websocket))
        send = asyncio.create_task(self.send_temperature_data(websocket))
        await recv
        await send

    # Websocket loop
    async def send_temperature_data(self, websocket):
        print("Sending data task started")
        while True:
            # Read temperature from DHT11
            self.tempData.temperature = TR.read_temperature()

            # JSONify the temperature data and send it
            dataJSON = self.tempData.to_json_string()
            await websocket.send(dataJSON)

            # Sleep
            time.sleep(1)

    async def recv_temperature_data(self, websocket):
        print("Receive data task started")
        while True:
            rawData = await websocket.recv()
            jsonData = json.loads(rawData)
            print(jsonData)
            self.tempData.target = jsonData["target"]
            self.tempData.save_state()

if __name__ == "__main__":
    thermostatServer = ThermostatServer()
    asyncio.run(thermostatServer.run())