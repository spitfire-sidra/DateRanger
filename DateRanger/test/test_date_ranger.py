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
        self.assertEqual(obj.bdate, test_date)

    def test_base_day(self):
        test_date = date(2009, 12, 1)
        self.set_date(test_date)
        expect = (test_date, test_date)
        self.assertEqual(self.obj.base_day().get_range(), expect)

    def test_prev_0day(self):
        test_date = date(2010, 1, 2)
        self.set_date(test_date)
        expect = (date(2010, 1, 2), date(2010, 1, 2))
        self.assertEqual(self.obj.prev_day(0).get_range(), expect)

    def test_prev_2day(self):
        test_date = date(2010, 1, 2)
        self.set_date(test_date)
        expect = (date(2009, 12, 31), date(2009, 12, 31))
        self.assertEqual(self.obj.prev_day(2).get_range(), expect)

    def test_next_0day(self):
        test_date = date(2010, 1, 2)
        self.set_date(test_date)
        expect = (date(2010, 1, 2), date(2010, 1, 2))
        self.assertEqual(self.obj.next_day(0).get_range(), expect)

    def text_next_2day(self):
        test_date = date(2010, 12, 30)
        self.set_date(test_date)
        expect = (date(2011, 1, 1), date(2011, 1, 1))
        self.assertEqual(self.obj.next_day(2).get_range(), expect)

    def test_base_week(self):
        test_date = date(2015, 1, 1)
        self.set_date(test_date)
        expect = (date(2014, 12, 28), date(2015, 1, 3))
        self.assertEqual(self.obj.base_week().get_range(), expect)

    def test_prev_0week(self):
        test_date = date(2015, 1, 1)
        self.set_date(test_date)
        expect = (date(2014, 12, 28), date(2015, 1, 3))
        self.assertEqual(self.obj.prev_week(0).get_range(), expect)
        self.assertEqual(self.obj.prev_week(0).weeks(), 0)

    def test_prev_2week(self):
        test_date = date(2015, 1, 1)
        self.set_date(test_date)
        expect = (date(2014, 12, 14), date(2014, 12, 20))
        self.assertEqual(self.obj.prev_week(2).get_range(), expect)

    def test_next_0week(self):
        test_date = date(2014, 12, 15)
        self.set_date(test_date)
        expect = (date(2014, 12, 14), date(2014, 12, 20))
        self.assertEqual(self.obj.next_week(0).get_range(), expect)

    def test_next_2week(self):
        test_date = date(2014, 12, 15)
        self.set_date(test_date)
        expect = (date(2014, 12, 28), date(2015, 1, 3))
        self.assertEqual(self.obj.next_week(2).get_range(), expect)

    def test_base_month(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2015, 1, 1), date(2015, 1, 31))
        self.assertEqual(self.obj.base_month().get_range(), expect)

    def test_prev_0month(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2015, 1, 1), date(2015, 1, 31))
        self.assertEqual(self.obj.prev_month(0).get_range(), expect)

    def test_prev_1month(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2014, 12, 1), date(2014, 12, 31))
        self.assertEqual(self.obj.prev_month(1).get_range(), expect)

    def test_prev_2month(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2014, 11, 1), date(2014, 11, 30))
        self.assertEqual(self.obj.prev_month(2).get_range(), expect)

    def test_next_0month(self):
        test_date = date(2014, 11, 16)
        self.set_date(test_date)
        expect = (date(2014, 11, 1), date(2014, 11, 30))
        self.assertEqual(self.obj.next_month(0).get_range(), expect)

    def test_next_2month(self):
        test_date = date(2014, 11, 16)
        self.set_date(test_date)
        expect = (date(2015, 1, 1), date(2015, 1, 31))
        self.assertEqual(self.obj.next_month(2).get_range(), expect)

    def test_base_quarter(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2015, 1, 1), date(2015, 3, 31))
        self.assertEqual(self.obj.base_quarter().get_range(), expect)

    def test_prev_0quarter(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2015, 1, 1), date(2015, 3, 31))
        self.assertEqual(self.obj.prev_quarter(0).get_range(), expect)

    def test_prev_1quarter(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2014, 10, 1), date(2014, 12, 31))
        self.assertEqual(self.obj.prev_quarter().get_range(), expect)

    def test_prev_2quarter(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2014, 7, 1), date(2014, 9, 30))
        self.assertEqual(self.obj.prev_quarter(2).get_range(), expect)

    def test_prev_6quarter(self):
        test_date = date(2015, 1, 16)
        self.set_date(test_date)
        expect = (date(2013, 7, 1), date(2013, 9, 30))
        self.assertEqual(self.obj.prev_quarter(6).get_range(), expect)

    def test_next_0quarter(self):
        test_date = date(2013, 7, 16)
        self.set_date(test_date)
        expect = (date(2013, 7, 1), date(2013, 9, 30))
        self.assertEqual(self.obj.next_quarter(0).get_range(), expect)

    def test_next_1quarter(self):
        test_date = date(2013, 7, 16)
        self.set_date(test_date)
        expect = (date(2013, 10, 1), date(2013, 12, 31))
        self.assertEqual(self.obj.next_quarter().get_range(), expect)

    def test_next_6quarter(self):
        test_date = date(2013, 7, 16)
        self.set_date(test_date)
        expect = (date(2015, 1, 1), date(2015, 3, 31))
        self.assertEqual(self.obj.next_quarter(6).get_range(), expect)

    def test_base_year(self):
        test_date = date(2013, 7, 16)
        self.set_date(test_date)
        expect = (date(2013, 1, 1), date(2013, 12, 31))
        self.assertEqual(self.obj.base_year().get_range(), expect)

    def test_prev_0year(self):
        test_date = date(2015, 7, 16)
        self.set_date(test_date)
        expect = (date(2015, 1, 1), date(2015, 12, 31))
        self.assertEqual(self.obj.prev_year(0).get_range(), expect)

    def test_prev_2year(self):
        test_date = date(2015, 7, 16)
        self.set_date(test_date)
        expect = (date(2013, 1, 1), date(2013, 12, 31))
        self.assertEqual(self.obj.prev_year(2).get_range(), expect)

    def test_next_0year(self):
        test_date = date(2015, 7, 16)
        self.set_date(test_date)
        expect = (date(2015, 1, 1), date(2015, 12, 31))
        self.assertEqual(self.obj.next_year(0).get_range(), expect)

    def test_next_2year(self):
        test_date = date(2015, 7, 16)
        self.set_date(test_date)
        expect = (date(2017, 1, 1), date(2017, 12, 31))
        self.assertEqual(self.obj.next_year(2).get_range(), expect)


if __name__ == '__main__':
    unittest.main()
