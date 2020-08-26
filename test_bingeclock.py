#!/usr/bin/env python3

from bingeclock import bingeclock_series, bingeclock_marathon
import unittest


class TestBingeClock(unittest.TestCase):

    def test_series_basic(self):
        clock = bingeclock_series("avatar-the-last-airbender")  # normal, 3 numbers expected
        self.assertEqual(clock, (1, 6, 30))

    def test_series_hours(self):
        clock = bingeclock_series("days-of-our-lives", hours=4)  # hours per day, will only return answer in days
        self.assertEqual(clock, (2821, 0, 0))

    def test_series_nomin(self):
        clock = bingeclock_series("legend-of-korra/")  # returns D:H, no minutes
        self.assertEqual(clock, (1, 2, 0))

    def test_series_nodays(self):
        clock = bingeclock_series("tiger-king")  # 5:17, no days
        self.assertEqual(clock, (0, 5, 17))

    def test_series_commercials(self):
        clock = bingeclock_series("avatar-the-last-airbender", commercials=False)  # cut commerials+credits
        self.assertEqual(clock, (0, 22, 22))

    def test_series_toomanyoptions(self):
        clock = bingeclock_series("avatar-the-last-airbender", commercials=False, hours=7)  # fail, can't use both optionals
        self.assertEqual(clock, ())

    def test_series_notaseries(self):
        clock = bingeclock_series("the-chilling-adventures-of-dolph-lundgren")  # doesn't exist
        self.assertEqual(clock, ())


    def test_marathon_valid(self):
        clock = bingeclock_marathon("marvel-cinematic-universe-2")  # valid marathon with all 3 numbers
        self.assertEqual(clock, (2, 2, 3))

    def test_marathon_nohour(self):
        clock = bingeclock_marathon("mission-impossible")  # no hours
        self.assertEqual(clock, (0, 13, 2))

    def test_marathon_nomin(self):
        clock = bingeclock_marathon("star-wars-1")  # returns D:H, no mintues
        self.assertEqual(clock, (1, 1, 0))

    def test_marathon_invalid(self):
        clock = bingeclock_marathon("mission-very-much-kim-possible")  # doesn't exist
        self.assertEqual(clock, ())


if __name__ == "__main__":
    unittest.main()

