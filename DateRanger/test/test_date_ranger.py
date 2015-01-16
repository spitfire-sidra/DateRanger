#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from datetime import date
from datetime import timedelta

from DateRanger import DateRanger


class TestDateRanger(unittest.TestCase):

    """
    Test cases for DateRanger
    """

    def set_date(self, base_date):
        self.obj = DateRanger(base_date)

    def test_set_base_date(self):
        test_date = date(2009, 12, 1)
        obj = DateRanger()
        obj.set_base_date(test_date)
        self.assertEqual(obj.base_date, test_date)

    def test_base_day(self):
        test_date = date(2009, 12, 1)
        self.set_date(test_date)
        expect = (test_date, test_date + timedelta(days=1))
        self.assertEqual(self.obj.base_day().get_range(), expect)

    def test_prev_day(self):
        test_date = date(2010, 1, 2)
        self.set_date(test_date)
        expect = (date(2009, 12, 31), date(2010, 1, 1))
        self.assertEqual(self.obj.prev_day(2).get_range(), expect)

    def text_next_day(self):
        test_date = date(2010, 12, 30)
        self.set_date(test_date)
        expect = (date(2011, 1, 1), date(2011, 1, 2))
        self.assertEqual(self.obj.next_day(2).get_range(), expect)

    def test_base_week(self):
        test_date = date(2015, 1, 1)
        self.set_date(test_date)
        expect = (date(2014, 12, 29), date(2015, 1, 4))
        self.assertEqual(self.obj.base_week().get_range(), expect)

    def test_prev_week(self):
        test_date = date(2015, 1, 1)
        self.set_date(test_date)
        expect = (date(2014, 12, 15), date(2014, 12, 21))
        self.assertEqual(self.obj.prev_week(2).get_range(), expect)

    def test_next_week(self):
        test_date = date(2014, 12, 15)
        self.set_date(test_date)
        expect = (date(2014, 12, 29), date(2015, 1, 4))
        self.assertEqual(self.obj.next_week(2).get_range(), expect)

    def test_base_month(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2015, 1, 1), date(2015, 2, 1))
        self.assertEqual(self.obj.base_month().get_range(), expect)

    def test_prev_month(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2014, 11, 1), date(2014, 12, 1))
        self.assertEqual(self.obj.prev_month(2).get_range(), expect)

    def test_next_month(self):
        test_date = date(2014, 11, 16)
        self.set_date(test_date)
        expect = (date(2015, 1, 1), date(2015, 2, 1))
        self.assertEqual(self.obj.next_month(2).get_range(), expect)

    def test_base_quarter(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2015, 1, 1), date(2015, 4, 1))
        self.assertEqual(self.obj.base_quarter().get_range(), expect)

    def test_prev_quarter1(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2014, 10, 1), date(2015, 1, 1))
        self.assertEqual(self.obj.prev_quarter().get_range(), expect)

    def test_prev_quarter2(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2014, 7, 1), date(2014, 10, 1))
        self.assertEqual(self.obj.prev_quarter(2).get_range(), expect)

    def test_prev_quarter3(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2013, 7, 1), date(2013, 10, 1))
        self.assertEqual(self.obj.prev_quarter(6).get_range(), expect)

    def test_next_quarter1(self):
        test_date = date(2013, 7, 16)
        self.set_date(test_date)
        expect = (date(2015, 1, 1), date(2015, 4, 1))
        self.assertEqual(self.obj.next_quarter(6).get_range(), expect)

    def test_base_year(self):
        test_date = date(2013, 7, 16)
        self.set_date(test_date)
        expect = (date(2013, 1, 1), date(2014, 1, 1))
        self.assertEqual(self.obj.base_year().get_range(), expect)

    def test_prev_year(self):
        test_date = date(2015, 7, 16)
        self.set_date(test_date)
        expect = (date(2013, 1, 1), date(2014, 1, 1))
        self.assertEqual(self.obj.prev_year(2).get_range(), expect)

    def test_next_year(self):
        test_date = date(2015, 7, 16)
        self.set_date(test_date)
        expect = (date(2017, 1, 1), date(2018, 1, 1))
        self.assertEqual(self.obj.next_year(2).get_range(), expect)
