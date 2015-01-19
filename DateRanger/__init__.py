#!/usr/bin/env python
# -*- coding: utf-8 -*-
import calendar
from datetime import date
from datetime import timedelta

from DateRanger.utils import get_quarter
from DateRanger.utils import get_monthrange
from DateRanger.objects import DateRange
from DateRanger.exceptions import InvalidDateRange

class DateRanger(object):

    """
    A class for getting common bussiness date ranges.
    """

    def __init__(self, base_date=None):
        """
        Argus:
            base_date - the base day. Example: date(2009, 11, 1)
        """
        self.base_date = base_date or date.today()

    def set_base_date(self, base_date):
        """
        Set base date.

        Argus:
            base_date - Example: date(2009, 11, 1)
        """
        self.base_date = base_date

    def base_day(self):
        """
        Get the DateRange of self.base_date.
        """
        return DateRange(self.base_date, self.base_date + timedelta(days=1))

    def prev_day(self, days=1):
        """
        Get the DateRange that n days before self.base_date.

        Argus:
            days - n days ago
        """
        prev_date = self.base_date - timedelta(days=days)
        return DateRange(prev_date, prev_date + timedelta(days=1))

    def next_day(self, days=1):
        """
        Get the DateRange that n days after self.base_date.

        Argus:
            days - next n days
        """
        next_date = self.base_date + timedelta(days=days)
        return DateRange(next_date, next_date + timedelta(days=1))

    def get_week_range(self, base_date):
        """
        Find the first/last day of the week for the given day.
        Weeks start on Sunday and end on Saturday.

        Argus:
            base_date - any date
        """
        start =  base_date - timedelta(days=base_date.weekday()+1)
        end = start + timedelta(days=7)
        return (start, end)

    def base_week(self):
        """
        Get DateRange of the week that contains self.base_date.
        """
        start, end = self.get_week_range(self.base_date)
        return DateRange(start, end)

    def prev_week(self, weeks=1):
        """
        Get the DateRange that n weeks before self.base_date.

        Argus:
            weeks - n week ago
        """
        _, end_date = self.base_week().get_range()
        start, end = self.get_week_range(end_date - timedelta(days=7*weeks))
        return DateRange(start, end)

    def next_week(self, weeks=1):
        """
        Get the DateRange that n weeks after self.base_date.

        Argus:
            weeks - next n weeks
        """
        _, end_date = self.base_week().get_range()
        start, end = self.get_week_range(end_date + timedelta(days=7*weeks))
        return DateRange(start, end)

    def get_month_range(self, year, month):
        """
        Get the first and last day of the given month in given year.

        Args:
            year
            month
        """
        days = calendar.monthrange(year, month)[1]
        start = date(year, month, 1)
        end = date(year, month, days) + timedelta(days=1)
        return (start, end)

    def base_month(self):
        """
        Get the DateRange of the month that contains self.base_date
        """
        year, month = self.base_date.year, self.base_date.month
        start, end = self.get_month_range(year, month)
        return DateRange(start, end)

    def prev_month(self, months=1):
        """
        Get the DateRange that n months before self.base_date.

        Argus:
            months - n months ago
        """
        start, end = self.base_month().get_range()
        for n in range(months):
            prev = start - timedelta(days=1)
            start, end = self.get_month_range(prev.year, prev.month)
        return DateRange(start, end)

    def next_month(self, months=1):
        """
        Get the DateRange that n months after self.base_date.

        Argus:
            months - next n months
        """
        start, end = self.base_month().get_range()
        for n in range(months):
            start = end
            _, end = self.get_month_range(start.year, start.month)
        return DateRange(start, end)

    def get_quarter_range(self, year, quarter):
        """
        Get time range with specific year and quarter.
        """
        if quarter not in (1, 2, 3, 4):
            return (None, None)

        start_month, end_month = get_monthrange(quarter)
        days = calendar.monthrange(year, end_month)[1]
        start = date(year, start_month, 1)
        end = date(year, end_month, days) + timedelta(days=1)
        return start, end

    def base_quarter(self):
        """
        Get the DateRange of the quarter that contains self.base_date.
        """
        quarter = get_quarter(self.base_date.month)
        start, end = self.get_quarter_range(self.base_date.year, quarter)
        return DateRange(start, end)

    def prev_quarter(self, quarters=1):
        """
        Get the DateRange that n quarters before self.base_date.

        Argus:
            quarters - n quarters ago
        """
        base_year = self.base_date.year
        base_quarter = get_quarter(self.base_date.month)
        if base_quarter - quarters < 0:
            quarters = abs(base_quarter - quarters)
            yeardelta = (quarters // 4) + 1
            quarterdelta = quarters % 4
            quarter = 4 - quarterdelta
        elif base_quarter - quarters == 0:
            yeardelta = 1
            quarter = 4
        else:
            yeardelta = 0
            quarter = base_quarter - quarters

        year = base_year - yeardelta
        start, end = self.get_quarter_range(year, quarter)
        return DateRange(start, end)

    def next_quarter(self, quarters=1):
        """
        Get the DateRange that n quarters after self.base_date.

        Argus:
            quarters - next n quarters
        """
        base_year = self.base_date.year
        base_quarter = get_quarter(self.base_date.month)
        if (base_quarter + quarters > 4):
            yeardelta = (base_quarter + quarters) // 4
            year = base_year + yeardelta
            quarter = (base_quarter + quarters) % 4
        else:
            year = base_year
            quarter = base_quarter + quarters
        start, end = self.get_quarter_range(year, quarter)
        return DateRange(start, end)

    def get_year_range(self, year):
        """
        Get time range of the year.
        """
        start = date(year, 1, 1)
        end = date(year + 1, 1, 1)
        return (start, end)

    def base_year(self):
        """
        Get the DateRange of the year that contains self.base_date.
        """
        base_year = self.base_date.year
        start, end = self.get_year_range(base_year)
        return DateRange(start, end)

    def prev_year(self, years=1):
        """
        Get the DateRange that n years before self.base_date.

        Argus:
            years - n years ago
        """
        year = self.base_date.year - years
        start, end = self.get_year_range(year)
        return DateRange(start, end)

    def next_year(self, years=1):
        """
        Get the DateRange that n years after self.base_date.

        Argus:
            year - next n years
        """
        year = self.base_date.year + years
        start, end = self.get_year_range(year)
        return DateRange(start, end)

    def from_date(self, from_date):
        """
        Return the DateRange from `from_date` to self.base_date

        Argus:
            from_date - Example: date(2015, 1, 1)
        """
        if from_date > self.base_date:
            raise InvalidDateRange()

        return DateRange(from_date, self.base_date + timedelta(days=1))

    def to_date(self, to_date):
        """
        Return the DateRange from self.base_date to `to_date`

        Argus:
            to_date - Example: date(2015, 1, 1)
        """
        if to_date < self.base_date:
            raise InvalidDateRange()

        return DateRange(self.base_date, to_date + timedelta(days=1))
