from datetime import datetime

class Logger:
    def log(msg):
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"{current_time} {msg}")