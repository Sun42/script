#!/usr/bin/python3

import sys
from datetime import timedelta

speeds = {"snail": 0.0036, "mosquito" : 2, "sprinter" : 36, "walker" : 10, "bus" : 90, "normal_car": 110, "sport_car": 200, "tgv" : 350, "plane": 850, "sound": 1225, "fighter_airplane": 3500, "rocket": 8000, "orbital_station": 28800, "earth": 107320, "sun" : 965000, "light": 1079252848.8}

def human_readable_time(hours):
    return timedelta(hours=hours)

if __name__ == "__main__":
    distance_km = float(sys.argv[1])
    print("Race {0} km".format(distance_km))
    for key in sorted(speeds, key=speeds.get):
        speed = speeds[key]
        hours = distance_km / speed
        print("{0} speed:{1} km/h time: {2}".format(key, speed, human_readable_time(hours)))
