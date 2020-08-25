#!/usr/bin/env python3

from bingeclock import bingeclock_series
import unittest


class TestBingeClock(unittest.TestCase):

    def test_series_basic(self):
        clock = bingeclock_series("avatar-the-last-airbender")  # normal, 3 numbers expected
        self.assertEqual(clock, (1, 6, 30))

    def test_series_hours(self):
        clock = bingeclock_series("days-of-our-lives", hours=4)  # hours per day, will only return answer in days
        self.assertEqual(clock, (2821,))

    def test_series_commercials(self):
        clock = bingeclock_series("avatar-the-last-airbender", commercials=False)  # cut commerials+credits
        self.assertEqual(clock, (0, 22, 22))

    def test_series_rejectoptions(self):
        clock = bingeclock_series("avatar-the-last-airbender", commercials=False, hours=7)  # fail, can't use both optionals
        self.assertEqual(clock, ())

    def test_series_shortanswer(self):
        clock = bingeclock_series("tiger-king")  # 5:17, no days
        self.assertEqual(clock, (0, 5, 17))

    def test_series_notaseries(self):
        clock = bingeclock_series("the-chilling-adventures-of-dolph-lundgren")  # doesn't exist
        self.assertEqual(clock, ())


if __name__ == "__main__":
    unittest.main()

