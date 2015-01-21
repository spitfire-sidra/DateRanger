#! /usr/bin/env python
# -*- coding: utf-8 -*-
import calendar
from datetime import date
from datetime import timedelta

from DateRanger.utils import get_quarter
from DateRanger.utils import get_monthrange
from DateRanger.exceptions import InvalidDateRange


class DateFrame(object):

    """
    An object for operations(get difference/yield date range) of date range.
    All methods do not include end_date.
    """

    def __init__(self, start_date, end_date):
        """
        Argus:
            start_date - the start date
            end_date - the end date
        """
        if start_date > end_date:
            raise InvalidDateRange()

        self.start_date = start_date
        self.end_date = end_date

    def get_timedelta(self):
        """
        Get timedelta of `self.end_date - self.start_date`
        """
        return self.end_date - self.start_date

    def days(self):
        """
        Calcualte the difference in days.
        """
        return int(self.get_timedelta().days)

    def each_day(self):
        """
        Yield each day between start_date and end_date.
        """
        for n in range(self.days()):
            yield self.start_date + timedelta(n)

    def get_weekdelta(self):
        """
        Simplify this question by counting weeks between monday1 and monday2.

        monday1 - monday of the week of self.start_date
        monday2 - monday of the week of self.end_date
        """
        monday1 = (self.start_date - timedelta(days=self.start_date.weekday()))
        monday2 = (self.end_date - timedelta(days=self.end_date.weekday()))
        return int((monday2 - monday1).days / 7)

    def weeks(self):
        """
        Return date difference in months.
        """
        return self.get_weekdelta()

    def each_week(self):
        """
        Yield each week between self.start_date and self.end_date
        """
        start = (self.start_date - timedelta(days=self.start_date.weekday()+1))
        for n in range(self.weeks() + 1):
            end = start + timedelta(days=7)
            yield (start, end)
            start = end + timedelta(days=1)

    def get_monthdelta(self):
        """
        Get month delta.
        """
        yeardelta = self.get_yeardelta()
        if yeardelta == 0:
            return int(self.end_date.month) - int(self.start_date.month)

        monthdelta = (12 - int(self.start_date.month) + 1) + \
            ((yeardelta - 1) * 12) + int(self.end_date.month)
        return monthdelta

    def months(self):
        """
        Calcualte the difference in months.
        """
        return self.get_monthdelta()

    def each_month(self):
        """
        Yield each month between self.start_date and self.end_date
        """
        start = date(self.start_date.year, self.start_date.month, 1)
        if self.months() == 0:
            days = calendar.monthrange(start.year, start.month)[1]
            end = date(start.year, start.month, days)
            yield (start, end)
        else:
            for n in range(self.months()):
                days = calendar.monthrange(start.year, start.month)[1]
                end = date(start.year, start.month, days)
                yield (start, end)
                start = end + timedelta(days=1)

    def get_quarterdelta(self):
        """
        Calcualte date difference in quraters.
        """
        start_quarter = get_quarter(self.start_date.month)
        end_quarter = get_quarter(self.end_date.month)
        yeardelta = self.get_yeardelta()
        if yeardelta == 0:
            return end_quarter - start_quarter

        quarterdelta = (4 - start_quarter) + \
            ((yeardelta - 1) * 4) + end_quarter
        return quarterdelta

    def quarters(self):
        """
        Return date difference in quraters.
        """
        return self.get_quarterdelta()

    def each_quarter(self):
        """
        Yield each quarter.
        """
        quarter = get_quarter(self.start_date.month)
        start_month, end_month = get_monthrange(quarter)
        start = date(self.start_date.year, start_month, 1)
        if self.quarters() == 0:
            days = calendar.monthrange(start.year, start.month + 2)[1]
            end = date(start.year, start.month + 2, days)
            yield (start, end)
        else:
            for n in range(self.quarters()):
                days = calendar.monthrange(start.year, start.month + 2)[1]
                end = date(start.year, start.month + 2, days)
                yield (start, end)
                start = end + timedelta(days=1)

    def get_yeardelta(self):
        """
        Calcualte date difference in years.
        """
        return int(self.end_date.year) - int(self.start_date.year)

    def years(self):
        """
        Return date difference in years.
        """
        return self.get_yeardelta()

    def each_year(self):
        """
        Yield each year.
        """
        for n in range(self.start_date.year, self.end_date.year + 1):
            start = date(n, 1, 1)
            end = date(n, 12, 31)
            yield (start, end)

    def get_range(self):
        """
        Return a tuple that contains self.start_date and self.end_date
        """
        return (self.start_date, self.end_date)
