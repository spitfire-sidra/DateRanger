#!/usr/bin/env python
# -*- coding: utf-8 -*-
import calendar
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


class DateRange(object):

    """
    An object for operations(get difference/yield date range) of date range.
    """

    def __init__(self, start_date, end_date):
        """
        Argus:
            start_date - the start date
            end_date - the end date
        """
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

        This method does not include end_date.
        """
        return int(self.get_timedelta().days)

    def each_day(self):
        """
        Yield each day between start_date and end_date.
        """
        for n in xrange(self.days()):
            yield self.start_date + timedelta(n)

    def get_weekdelta(self):
        """
        Simplify this question by counting weeks between monday1 and monday2.

        monday1 - monday of the week of self.start_date
        monday2 - monday of the week of self.end_date
        """
        monday1 = (self.start_date - timedelta(days=self.start_date.weekday()))
        monday2 = (self.end_date - timedelta(days=self.end_date.weekday()))
        return (monday2 - monday1).days / 7

    def weeks(self):
        """
        Return date difference in months.
        """
        return self.get_weekdelta()

    def each_week(self):
        """
        Yield each week between self.start_date and self.end_date
        """
        monday = (self.start_date - timedelta(days=self.start_date.weekday()))
        for n in self.weeks():
            start = monday
            end = start + timedelta(days=7)
            yield (start, end)
            start = monday + timedelta(weeks=n)

    def get_monthdelta(self):
        """
        Get month delta.
        """
        yeardelta = int(self.end_date.year) - int(self.start_date.year)
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
        for n in self.months():
            days = monthrange(start.year, start.month)[1]
            end = date(self.start_date.year, self.start_date.month, days)
            yield (start, end)
            start = end + timedelta(days=1)


class DateRanger(object):

    """
    A class for getting common date ranges.

    >>> ranger = DateRanger()
    >>> ranger.get_base_day_range()

    >>> ranger.time_range_current_week()

    >>> ranger.time_range_prev_week(2)

    >>> ranger.time_range_current_month()

    >>> ranger.time_range_prev_month()

    >>> ranger.time_range_current_quarter()

    >>> ranger.time_range_prev_quarter()

    >>> ranger.time_range_current_year()

    >>> ranger.time_range_prev_year()
    """

    def __init__(self, base_day=None, time_min=None, time_max=None):
        self.base_day = base_day or date.today()
        self.time_min = time_min or time.min
        self.time_max = time_max or time.max

    def get_timerange(self, start, end):
        """
        Get the time range between 's' and 'e'.
        """
        s = datetime.combine(start, self.time_min)
        e = datetime.combine(end, self.time_max)
        return (s, t)

    def get_base_day_range(self):
        return self.get_timerange(self.base_day, self.base_day)

    def get_previous_day(self, days=1):
        previous_day = self.base_day - timedelta(days=1)
        return self.get_timerange(previous_day, previous_day)

    def get_week_timerange(self, date):
        """
        Find the first/last day of the week for the given day.
        Weeks start on Sunday and end on Saturday.
        """
        year, week, dow = date.isocalendar()
        if dow == 7:
            start = date
        else:
            start = date - timedelta(dow)
        end = start + timedelta(6)
        return self.get_timerange(start, end)

    def time_range_current_week(self):
        """
        Get time range of current week.
        """
        return self.get_week_timerange(self.base_day)

    def time_range_prev_week(self, weeks=1):
        """
        Get time range of previous week.
        """
        f, t = self.time_range_current_week()
        delta = timedelta(days=7*weeks)
        return (f - delta, t - delta)

    def time_range_month(self, year, month):
        days = calendar.monthrange(year, month)[1]
        first_day = date(year, month, 1)
        last_day = date(year, month, days)
        return self.get_timerange(first_day, last_day)

    def time_range_current_month(self):
        return self.time_range_month(self.base_day.year, self.base_day.month)

    def time_range_prev_month(self):
        first_day, _ = self.time_range_current_month()
        prev_month = first_day - timedelta(days=1)
        return self.time_range_month(prev_month.year, prev_month.month)

    def get_quarter_timerange(self, year, quarter):
        """
        Get time range with specific year and quarter.
        >>> get_quarter_timerange(2014, 11)
        (datetime.datetime(2014, 11, 1, 0, 0), \
            datetime.datetime(2014, 11, 30, 23, 59, 59, 999999))
        """
        if quarter not in (1, 2, 3, 4):
            return (None, None)
        start_month = ((quarter - 1) * 3) + 1
        end_month = start_month + 2
        days_of_end_month = calendar.monthrange(year, end_month)[1]
        first_day = date(year, start_month, 1)
        last_day = date(year, end_month, days_of_end_month)
        return self.get_timerange(first_day, last_day)

    def time_range_current_quarter(self):
        """
        Get current quarter timerange.
        """
        quarter = (self.base_day.month // 4) + 1
        return self.get_quarter_timerange(self.base_day.year, quarter)

    def time_range_prev_quarter(self):
        """
        Get previous quarter timerange.
        """
        year = self.base_day.year
        quarter = (self.base_day.month // 4) + 1
        if quarter - 1 == 0:
            quarter = 4
            year = year - 1
        else:
            quarter = quarter - 1
        return self.get_quarter_timerange(year, quarter)

    def get_year_timerange(self, year):
        """
        Get time range of the year.
        """
        first_day = date(year, 1, 1)
        last_day = date(year, 12, 31)
        return self.get_timerange(first_day, last_day)

    def time_range_current_year(self):
        """
        Get time range of current year.
        """
        year = self.base_day.year
        return self.get_year_timerange(year)

    def time_range_prev_year(self):
        """
        Get time range of previous year.
        """
        year = self.base_day.year - 1
        return self.get_year_timerange(year)
