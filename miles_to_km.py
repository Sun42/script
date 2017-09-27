#!/usr/bin/python3

import sys

def miles_to_km(miles):
    return miles * 1.60934

if __name__ == "__main__":
    miles = int(sys.argv[1])
    print("{0} miles".format(miles))
    print("{0} km".format(miles_to_km(miles)))

