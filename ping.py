#!/usr/bin/python3

import subprocess
import sys

hostname = "google.com"
command_line = "ping -c 1 {0}".format(hostname)
try:
    response = subprocess.check_output(command_line, shell=True, stderr=subprocess.STDOUT, timeout=5)
except subprocess.CalledProcessError as pe:
    print("PING: error")
    sys.exit(1)
except subprocess.TimeoutExpired as te:
    print("PING: timeout")
    sys.exit(1)
for line in response.decode('utf-8').split('\n'):
    for i in line.split(' '):
        if i.startswith('time='):
            print("PING: {0} ms".format(i[5:]))
            sys.exit(0)
print("PING: ?")
