import subprocess
import sys
import os
import time

if os.name == "nt":
    python = "python"
else:
    python = "python" + sys.version[0:3]

call_server = [python, "server_worker.py"]
call_client = [python, "client_worker.py"]


print("Starting worker for Server")
subprocess.Popen(call_server)

time.sleep(0.5)

print("Starting worker for Client")
subprocess.Popen(call_client)




