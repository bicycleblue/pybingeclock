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

