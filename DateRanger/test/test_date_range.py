#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from datetime import date

from DateRanger import DateRange


class TestDateRange(unittest.TestCase):

    """
    Test cases for DateRange
    """

    def set_dates(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.obj = DateRange(start_date, end_date)

    def test_days(self):
        self.set_dates(date(2009, 5, 20), date(2009, 5, 22))
        expect = (self.end_date - self.start_date).days
        self.assertEqual(self.obj.days(), expect)

    def test_each_day(self):
        self.set_dates(date(2009, 12, 19), date(2010, 1, 21))
        result = [item for item in self.obj.each_day()]
        expect = (self.end_date - self.start_date).days
        self.assertEqual(len(result), expect)

    def test_months1(self):
        self.set_dates(date(2009, 5, 20), date(2009, 5, 22))
        self.assertEqual(self.obj.months(), 0)

    def test_months2(self):
        self.set_dates(date(2009, 5, 20), date(2009, 6, 22))
        self.assertEqual(self.obj.months(), 1)

    def test_months3(self):
        self.set_dates(date(2009, 5, 20), date(2011, 6, 22))
        self.assertEqual(self.obj.months(), 26)
