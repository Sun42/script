#!/usr/bin/python3

import sys

def meterssecond_to_kmh(meters_by_second):
    return meters_by_second * 3.6

if __name__ == "__main__":
    meters_by_second = float(sys.argv[1])
    print("{0} m/s".format(meters_by_second))
    print("{0} km/h".format( meterssecond_to_kmh(meters_by_second)))

