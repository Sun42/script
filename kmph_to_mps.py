#!/usr/bin/python3

import sys

def kmph_to_mps(kmph):
    return kmph / 3.6

if __name__ == "__main__":
    kmph = int(sys.argv[1])
    print("{0} km/h".format(kmph))
    print("{0} m/s".format( kmph_to_mps(kmph)))

