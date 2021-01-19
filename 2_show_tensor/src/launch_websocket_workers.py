import subprocess
import sys
import time

python = "python" + sys.version[0:3]

call_server = [python, "server_worker.py", "--host", "localhost", "--port", "8768", "--id", "fed", "-v"]
call_client = [python, "client_worker.py", "--host", "localhost", "--port", "8768", "--id", "fed", "-v"]

print("Starting worker for Server")
subprocess.Popen(call_server)

time.sleep(0.5)

print("Starting worker for Client")
subprocess.Popen(call_client)




