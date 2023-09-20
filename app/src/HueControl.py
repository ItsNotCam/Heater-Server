import requests, json
from datetime import datetime

import os, sys

from src import Logger

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
CONFIG_PATH = f"{script_directory}/config.json"

class HueControl:
    def __init__(self):
        self.hue_url = ""
        self.light_name = ""
        self.light_index = -1

        self.is_on = False

        with open(CONFIG_PATH,'r') as file:
            data = json.loads(file.read())
            self.hue_url = data["hue_url"]
            self.light_name = data["light_name"]

        res = requests.get(self.hue_url)
        if res is None or res.status_code != 200:
            Logger.log("Failed to retrieve hue data")
            return
        
        data = res.json()['lights']
        for key, value in data.items():
            if value["name"] == self.light_name:
                self.light_index = int(key)
                break
        
        if self.light_index == -1:
            Logger.log(f"Failed to get light index, do you have a light named '{self.light_name}'?")
        else:
            self.is_on = data[f"{self.light_index}"]["state"]["on"]
            
    def set_state(self, on):
        current_time = datetime.now().strftime("%H:%M:%S")
        if on != self.is_on:
            if on:
                Logger.log("Turning heater on")
            else:
                Logger.log("Turning heater off")

            uri = f"{self.hue_url}/lights/{self.light_index}/state"
            resp = requests.put(uri, data=json.dumps({ "on": on }))
            self.is_on = on