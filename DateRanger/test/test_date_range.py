#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from datetime import date

from DateRanger import DateRange


class TestDateRange(unittest.TestCase):

    """
    Test cases for DateRange
    """

    def test_days(self):
        start_date, end_date = date(2009, 5, 20), date(2009, 5, 22)
        rag = DateRange(start_date, end_date)
        self.assertEqual(rag.days(), int((end_date - start_date).days))

    def test_each_day(self):
        start_date, end_date = date(2009, 12, 19), date(2010, 1, 21)
        rag = DateRange(start_date, end_date)
        result = list()
        for tp in rag.each_day():
            result.append(tp)
        self.assertEqual(len(result), int((end_date - start_date).days))

    def test_months1(self):
        start_date, end_date = date(2009, 5, 20), date(2009, 5, 22)
        rag = DateRange(start_date, end_date)
        self.assertEqual(rag.months(), 0)

    def test_months2(self):
        start_date, end_date = date(2009, 5, 20), date(2009, 6, 22)
        rag = DateRange(start_date, end_date)
        self.assertEqual(rag.months(), 1)

    def test_months3(self):
        start_date, end_date = date(2009, 5, 20), date(2011, 6, 22)
        rag = DateRange(start_date, end_date)
        self.assertEqual(rag.months(), 26)
