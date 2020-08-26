#!/usr/bin/env python3

import requests
import string
import re


def create_series_url(name, commercials, hours):
    url = "https://www.bingeclock.com/s/{}/".format(name)

    if not commercials:
        url += "al/"

    if hours > 0:
        url += "daily/{}".format(hours)

    return(url)


def create_marathon_url(name):
    url = "https://www.bingeclock.com/film/marathon/{}/".format(name)

    return(url)


def parse_body(body):
    # look for error message
    if body.find("Updated: Dec 31st 1969 at 7:00 pm") > -1: return(())

    # look for 1-3 of "<span class="date_type">word</span>"
    regex = r'<span class="date_type">([a-z]+)</span>'
    match_type = re.findall(regex, body)

    # look for 1-3 of "<span class="date_num">NUMBER</span>"
    regex = r'<span class="date_num">(\d+)</span>'
    match_num = re.findall(regex, body)

    # terminate on any mismatches
    if len(match_type) != len(match_num): return(())
    if not 1 <= len(match_type) <= 3: return(())
    if not 1 <= len(match_num) <= 3: return(())

    ans = [0, 0, 0]

    while len(match_type) > 0:
        typ = match_type.pop(0)
        num = match_num.pop(0)
        if typ == "day" or typ == "days":
            ans[0] = int(num)
        if typ == "hour" or typ == "hours":
            ans[1] = int(num)
        if typ == "minutes":
            ans[2] = int(num)
        
    return(tuple(ans))


def bingeclock_series(name, commercials=True, hours=False):
    # don't allow both options
    if not commercials and hours:
        return(())

    if not hours:
        hours = 0
    elif hours < 1:  # bingeclock accepts any positive int
        hours = 1

    url = create_series_url(name, commercials, hours)

    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            return(())
    except:
        return(())

    tup = parse_body(resp.text)

    return(tup)


def bingeclock_marathon(name):
    url = create_marathon_url(name)

    try:
        resp = requests.get(url)
        if resp.status_code != 200:
            return(())
    except:
        return(())

    tup = parse_body(resp.text)

    return(tup)

