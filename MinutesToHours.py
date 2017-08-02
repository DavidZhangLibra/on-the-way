#!/usr/bin/env python3
import sys
def Hours(minutes):
    minute = minutes % 60
    hour = int(minutes / 60)
    return hour, minute


if __name__ == '__main__':
    try:
        if int(sys.argv[1]) < 0:
            raise ValueError()
        hour, minute = Hours(int(sys.argv[1]))    
        print("{} H, {} M".format(hour, minute))
    except ValueError:
       print("ValueError: Input number cannot be negative")
