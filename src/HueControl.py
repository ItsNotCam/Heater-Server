import requests, json
from datetime import datetime

import os, sys
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
CONFIG_PATH = f"{script_directory}/../config.json"

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
            print("Failed to retrieve hue data")
            return
        
        data = res.json()['lights']
        for key, value in data.items():
            if value["name"] == self.light_name:
                self.light_index = int(key)
                break
        
        if self.light_index == -1:
            print(f"Failed to get light index, do you have a light named '{self.light_name}'?")
            
    def set_state(self, on):
        current_time = datetime.now().strftime("%H:%M:%S")
        if on != self.is_on:
            if on:
                print(f"{current_time} Turning heater on")
            else:
                print(f"{current_time} Turning heater off")

            uri = f"{self.hue_url}/lights/{self.light_index}/state"
            resp = requests.put(uri, data=json.dumps({ "on": on }))
            self.is_on = on