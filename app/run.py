from src import ThermostatServer
import asyncio

from src import Logger

if __name__ == "__main__":
    Logger.log("Thermostat Server Starting up")
    thermostatServer = ThermostatServer()
    asyncio.run(thermostatServer.run())
        