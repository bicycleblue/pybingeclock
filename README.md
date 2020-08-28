# pybingeclock
python module to query bingeclock.com

DISCLAIMERS XXX

# setup

Grab bingeclock.py from this repo and drop it where you'd like.

# usage

See the examples.py for some examples of usage. The two functions return a tuple of (days, hours, minutes) to watch a series or movie marathon. If an error occurs they silently return an empty tuple.

Basically there are two functions:

## bingeclock_series(title)

Get the time to binge a series. Specify the title in the format of the bingeclock.com URL for that title. example: "avatar-the-last-airbender" for the search https://www.bingeclock.com/s/avatar-the-last-airbender/. Yea, you have to go and manually query bingeclock to get the string to then search for again. Search is yet to be implemented.

bingeclock_series() can take either of two optional arguments.

commercials=False removes commercials and credits time from the returned binge time.

hours=8 will limit binging to a specified number of hours per day, and just tells you how many days it will take. The site lists 1-16 hours per day, but will take any reasonable positive integer).

## bingeclock_marathon(title)

Get the time to binge a movie marathon. Similar idea as above, find one of their movie marathon lists and you can query it by name from the url.

# developer notes

## series
```
https://www.bingeclock.com/s/series-name/
https://www.bingeclock.com/s/series-name/al  - no commercials/credits
https://www.bingeclock.com/s/series-name/daily/#  - hours per day, returns just days
```
It doesn't appear possible to ask for both no commercials and hours per day

## marathons
```
https://www.bingeclock.com/film/marathon/marathon-name/
```

No options available for marathons. Multiple marathons may exist, check for -1, -2 at end of name.

## parsing the HTML

They only print non-zero values. If something adds up to an even number of hours, you won't get a minutes value. Same for days on short items.

After several attempts it looks like the best way to extract the data and get the Days, Hours, and Minutes right is to look for "date_num" to get the numbers for each d:h:m, then look for "date_type" to get which values are present in the HTML.

<span class="date_num">1</span>
<span class="date_type">day</span>

They're not consistent between series and marathons, date_type may be day or days, or hour and hours.

They don't give a consistent error message for a title not found. Seaching for the string "Updated: Dec 31st 1969 at 7:00 pm" seems to work pretty well.

## untitest

```
./test_bingeclock.py -v TestBingeClock.test_marathon_valid
```

# todo

* implement search for titles
* maybe raise an exception on error instead of just returning an empty tuple

