import json, random, os, sys

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
STATE_PATH = f"{script_directory}/state.json"

class TemperatureData:
    def __init__(self):
        self.temperature = 0
        self.target = 84
        self.on = False
        self.load_state()

    def save_state(self):
        with open(STATE_PATH,'w') as file:
            jsonData = self.to_json_object()
            file.writelines(json.dumps(jsonData))

    def load_state(self):
        with open(STATE_PATH,'r') as file:
            data = json.loads(file.read())
            self.from_json(data)

    def from_json(self, data):
        self.temperature = data["temperature"]
        self.target = data["target"]
        self.on = data["on"]

    def to_json_object(self):
        return {
            "temperature": self.temperature,
            "target": self.target,
            "on": self.on
        }
    
    def to_json_string(self):
        return json.dumps(self.to_json_object())