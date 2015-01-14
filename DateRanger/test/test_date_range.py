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
        self.assertEqual(self.obj.days(), 2)

    def test_each_day(self):
        self.set_dates(date(2009, 12, 19), date(2010, 1, 21))
        result = [item for item in self.obj.each_day()]
        expect = (self.end_date - self.start_date).days
        self.assertEqual(len(result), expect)

    def test_weeks1(self):
        self.set_dates(date(2015, 1, 9), date(2015, 1, 14))
        self.assertEqual(self.obj.weeks(), 1)

    def test_weeks2(self):
        self.set_dates(date(2015, 1, 9), date(2015, 1, 19))
        self.assertEqual(self.obj.weeks(), 2)

    def test_each_week1(self):
        self.set_dates(date(2014, 12, 2), date(2015, 1, 19))
        result = [item for item in self.obj.each_week()]
        self.assertEqual(len(result), 8)

    def test_each_week2(self):
        self.set_dates(date(2014, 12, 2), date(2014, 12, 2))
        result = [item for item in self.obj.each_week()]
        self.assertEqual(len(result), 1)

    def test_months1(self):
        self.set_dates(date(2009, 5, 20), date(2009, 5, 22))
        self.assertEqual(self.obj.months(), 0)

    def test_months2(self):
        self.set_dates(date(2009, 5, 20), date(2009, 6, 22))
        self.assertEqual(self.obj.months(), 1)

    def test_months3(self):
        self.set_dates(date(2009, 5, 20), date(2011, 6, 22))
        self.assertEqual(self.obj.months(), 26)

    def test_each_month1(self):
        self.set_dates(date(2009, 5, 20), date(2011, 6, 22))
        result = [item for item in self.obj.each_month()]
        self.assertEqual(len(result), 26)

    def test_each_month2(self):
        self.set_dates(date(2009, 5, 20), date(2009, 5, 22))
        result = [item for item in self.obj.each_month()]
        self.assertEqual(len(result), 1)

    def test_quarters1(self):
        self.set_dates(date(2011, 6, 20), date(2011, 6, 22))
        self.assertEqual(self.obj.quarters(), 0)

    def test_quarters2(self):
        self.set_dates(date(2011, 2, 20), date(2011, 4, 22))
        self.assertEqual(self.obj.quarters(), 1)

    def test_quarters3(self):
        self.set_dates(date(2011, 2, 20), date(2013, 9, 22))
        self.assertEqual(self.obj.quarters(), 10)

    def test_each_quarter1(self):
        self.set_dates(date(2011, 2, 20), date(2013, 9, 22))
        result = [item for item in self.obj.each_quarter()]
        self.assertEqual(len(result), 10)

    def test_each_quarter2(self):
        self.set_dates(date(2011, 2, 20), date(2011, 2, 22))
        result = [item for item in self.obj.each_quarter()]
        self.assertEqual(len(result), 1)

    def test_years1(self):
        self.set_dates(date(2009, 5, 20), date(2009, 6, 22))
        self.assertEqual(self.obj.years(), 0)

    def test_years2(self):
        self.set_dates(date(2009, 5, 20), date(2011, 6, 22))
        self.assertEqual(self.obj.years(), 3)

    def test_each_year(self):
        self.set_dates(date(2009, 5, 20), date(2010, 6, 22))
        result = [item for item in self.obj.each_year()]
        self.assertEqual(len(result), 2)
