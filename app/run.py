from src import ThermostatServer
import asyncio

if __name__ == "__main__":
    thermostatServer = ThermostatServer()
    asyncio.run(thermostatServer.run())