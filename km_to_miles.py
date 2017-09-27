#!/usr/bin/python3

import sys

def km_to_miles(km):
    return km * 0.621371

if __name__ == "__main__":
    km = float(sys.argv[1])
    print("{0} km".format(km))
    print("{0} km".format(km_to_miles(km)))

