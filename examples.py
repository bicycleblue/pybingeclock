#!/usr/bin/env python3

from bingeclock import bingeclock_series, bingeclock_marathon


def main():
    # both functions return a tuple: (days, hours, minutes)
    clock = bingeclock_series("avatar-the-last-airbender")
    print("Aang: {} days, {} hours, and {} minutes".format(clock[0], clock[1], clock[2]))

    # request time excluding credits and commercial runtime
    clock = bingeclock_series("avatar-the-last-airbender", commercials=False)
    print("Aang, no commercials/credits: {} days, {} hours, and {} minutes".format(clock[0], clock[1], clock[2]))

    # request time given 8 hours a day of binging
    clock = bingeclock_series("avatar-the-last-airbender", hours=8)
    print("Aang, 8 hours/day: {} days, {} hours, and {} minutes".format(clock[0], clock[1], clock[2]))

    (days, hours, minutes) = bingeclock_series("tiger-king")
    print("Joe Exotic: {} days, {} hours, and {} minutes".format(days, hours, minutes))

    # on error, you get back an empty tuple
    clock = bingeclock_series("the-chilling-adventures-of-dolph-lundgren")
    if clock:
        print("Dolph found: {} days, {} hours, and {} minutes".format(clock[0], clock[1], clock[2]))
    else:
        print("Dolph not found")

    # you can also ask for one of thier movie binge lists, aka marathons
    clock = bingeclock_marathon("marvel-cinematic-universe-2")
    print("MCU movies: {} days, {} hours, and {} minutes".format(*clock))


if __name__ == "__main__":
    main()

