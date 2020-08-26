# pybingeclock
python module to query bingeclock.com

examples of usage

two functions
return tuple of days, hours, minutes


have to know exact string from bingeclock, show example

url formats
https://www.bingeclock.com/s/series-name/
https://www.bingeclock.com/s/series-name/al  - no commercials/credits
https://www.bingeclock.com/s/series-name/daily/#  - hours per day
no way to do al and daily together?

https://www.bingeclock.com/film/marathon/marathon-name/
no options for marathons
multiple marathons may exist, check for -1, -2 at end of name

series
basic return: D:H:M
some omit day, maybe hour, those don't display

parsing: search for <span class="date_num">1</span>
to find the numbers of D:H:M

search for <span class="date_type">day</span>
to find day / hours / minutes
or in marathons, days is plural and hour is singular
to find days / hour / minutes

exception on marathons, https://www.bingeclock.com/film/marathon/star-wars-1/
returns 1 day 1 hour, no minutes displayed

errors in searches don't have an error page, they throw up a junk entry with a note:
Updated: Dec 31st 1969 at 7:00 pm


test -v

./test_bingeclock.py -v TestBingeClock.test_marathon_valid

dev notes

doesn't do search

#!/usr/bin/env python3

from bingeclock import bingeclock_series
import unittest



Examples from earlier version for docs


def main():
    clock = bingeclock_series("avatar-the-last-airbender")  # normal, 3 numbers expected
    if clock == (1, 6, 30):
        print("ATLA: success {} days, {} hours, and {} minutes".format(clock[0], clock[1], clock[2]))
    else:
        print("ATLA: fail")

    clock = bingeclock_series("days-of-our-lives", hours=4)  # hours per day, will only return answer in days
    if clock and len(clock) == 1 and clock == (2821,):
        print("Days: success {} days".format(clock[0]))
    else:
        print("Days: fail")

    clock = bingeclock_series("avatar-the-last-airbender", commercials=False)  # cut commerials+credits
    if clock and clock == (0, 22, 22):
        print("ATLA: success {} days, {} hours, and {} minutes".format(clock[0], clock[1], clock[2]))
    else:
        print("ATLA: fail")

    clock = bingeclock_series("avatar-the-last-airbender", commercials=False, hours=7)  # fail, can't use both optionals
    if clock and clock == (0, 22, 22):
        print("ATLA: fail {} days, {} hours, and {} minutes".format(clock[0], clock[1], clock[2]))
    else:
        print("ATLA: both options disallowed, success")

    clock = bingeclock_series("tiger-king")  # 5:17, no days
    if clock and clock == (0, 5, 17):
        print("Joe Exotic: success {} days, {} hours, and {} minutes".format(clock[0], clock[1], clock[2]))
    else:
        print("Joe Exotic: fail")

    clock = bingeclock_series("the-chilling-adventures-of-dolph-lundgren")  # doesn't exist
    if clock:
        print("Dolph found, fail: {} days, {} hours, and {} minutes".format(clock[0], clock[1], clock[2]))
    else:
        print("Dolph not found, success")


if __name__ == "__main__":
    unittest.main()

