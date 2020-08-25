#!/usr/bin/env python3

import requests
import re


def create_url(name, commercials, hours):
    url = "https://www.bingeclock.com/s/{}/".format(name)

    if not commercials:
        url += "al/"

    if hours > 0:
        url += "daily/{}".format(hours)

    return(url)


def parse_body(body):
    # look for 1-3 of "<span class="date_num">NUMBER</span>"
    regex = r'<span class="date_num">(\d+)</span>'

    m = re.findall(regex, body)

    if m:
        while len(m) < 3:    # insert 0 for missing D H values, even if hours in play
            m.insert(0, 0)

        return(tuple(map(int, m)))
    else:
        return(())


def bingeclock_series(name, commercials=True, hours=False):
    # don't allow both options
    if not commercials and hours:
        return(())

    if not hours:
        hours = 0
    elif hours < 1:  # bingeclock accepts any positive int
        hours = 1

    url = create_url(name, commercials, hours)

    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            return(())
    except:
        return(())

    tup = parse_body(resp.text)

    if hours:
        #return((tup[2],))
        return((tup[2],))

    return(tup)


def main():
    print("running tests")

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
    main()

