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
        return((tup[2],))

    return(tup)

