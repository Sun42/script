#!/usr/bin/python3

import subprocess
import sys

response = subprocess.check_output("free -b",
                                   shell=True,
                                   stderr=subprocess.STDOUT,
                                   timeout=5)
responses = response.decode('utf-8').split('\n')
keys = responses[0].split()
values = responses[1].split()[1:]
mydict = dict(zip(keys, map(int, values)))
activity = (mydict['total'] - mydict['available']) / mydict['total'] * 100
print("RAM: {0:.1f}%".format(activity))
