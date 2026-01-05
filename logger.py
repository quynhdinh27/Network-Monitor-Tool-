from datetime import datetime
import os

def write_log(message, log_file="logs/monitor.log"):
    dirpath = os.path.dirname(log_file)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)

    with open(log_file, "a") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{time} | {message}\n")