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
