#!/usr/bin/env python
# -*- coding: utf-8 -*-
import calendar
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


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

    def __init__(self, base_day=date.today(), time_min=time.min, time_max=time.max):
        self.base_day = base_day
        self.time_min = time_min
        self.time_max = time_max

    def get_timerange(self, s, e):
        """
        Get the time range between 's' and 'e'.
        """
        f = datetime.combine(s, self.time_min)
        t = datetime.combine(e, self.time_max)
        return (f, t)

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
