#!/usr/bin/env python3

import requests
import re


def create_url(name):
    url = "https://www.bingeclock.com/s/{}/".format(name)

    return(url)


def parse_body(body):
    # look for 1-3 of "<span class="date_num">NUMBER</span>", if all three, D H M. If less, H M or M
    regex = r'<span class="date_num">(\d+)</span>'

    m = re.findall(regex, body)

    if m:
        while len(m) < 3:    # insert 0 for missing D H values
            m.insert(0, 0)

        return((int(m[0]), int(m[1]), int(m[2])))
    else:
        return(())


def bingeclock_series(name):
    url = create_url(name)
    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            return(())
    except:
        return(())

    tup = parse_body(resp.text)

    return(tup)


def main():
    print("running tests")

    clock = bingeclock_series("avatar-the-last-airbender")  # normal, 3 numbers expected
    if clock == (1, 6, 30):
        print("ATLA: success {} days, {} hours, and {} minutes".format(clock[0], clock[1], clock[2]))
    else:
        print("ATLA: fail")

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

