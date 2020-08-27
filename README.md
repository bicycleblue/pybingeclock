# pybingeclock
python module to query bingeclock.com

# setup

Grab bingeclock.py from this repo and drop it where you'd like.

# usage

See the examples.py for some examples of usage. The two functions return a tuple of (days, hours, minutes) to watch a series or movie marathon. If an error occurs it gives you back an empty tuple.

Basically there are two functions:

## bingeclock_series(title)

Get the time to binge a series. Specify the title in the format of the bingeclock.com URL for that title. example: "avatar-the-last-airbender" for the search https://www.bingeclock.com/s/avatar-the-last-airbender/. Yea, you have to go and manually query bingeclock to get the string to then search for again. Search is yet to be implemented.

bingeclock_series() can take either of two optional arguments.

commercials=False removes commercials and credits time from the returned binge time.

hours=8 will limit binging to a specified number of hours per day, and just tells you how many days it will take. The site lists 1-16 hours per day, but will take any reasonable positive integer).

## bingeclock_marathon(title)

Get the time to binge a movie marathon. Similar idea as above, find one of their movie marathon lists and you can query it by name from the url.

# developer notes

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


# todo

* implement search for titles
* maybe raise an exception on error instead of just returning an empty tuple

