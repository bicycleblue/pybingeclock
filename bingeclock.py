#!/usr/bin/env python3

import requests
import re


def create_url(name):
    url = "https://www.bingeclock.com/s/{}/".format(name)

    return(url)

def parse_body(body):
    regex = r'date_counter_cont.*span class="date_num">(\d+)</span>.*date_counter_cont.*span class="date_num">(\d+)</span>.*date_counter_cont.*span class="date_num">(\d+)</span>'

    m = re.search(regex, body)
    if m:
        print(m.groups())
        return(int(m.group(1)), int(m.group(2)), int(m.group(3)))   # int maybe with some error checking?
    else:
        print("m bad {}".format(repr(m)))
        return(())

def bingeclock_series(name):
    url = create_url(name)
    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            print("error from website")
            return("")
        print("good fetch")
    except:
        print("error fetching series")
        return("")

    (days, hours, minutes) = parse_body(resp.text)
    print("found d {} m {} h {}".format(days, hours, minutes))

    return((days, hours, minutes))


def main():
    print("running tests")

    tup = bingeclock_series("avatar-the-last-airbender")
    if tup == (1, 6, 30):
        print("correct")
    else:
        print("wrong")

    # need a short and a long series to test max things


if __name__ == "__main__":
    main()

