#!/usr/bin/env python
# -*- coding: utf-8 -*-
import calendar
from datetime import date
from datetime import time
from datetime import timedelta


def month_to_quarter(month):
    if month in (1, 2, 3):
        return 1
    elif month in (4, 5, 6):
        return 2
    elif month in (7, 8, 9):
        return 3
    else:
        return 4


def quarter_to_month(quarter):
    if quarter == 1:
        return (1, 3)
    elif quarter == 2:
        return (4, 6)
    elif quarter == 3:
        return (7, 9)
    else:
        return (10, 12)


class DateRange(object):

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
        start = (self.start_date - timedelta(days=self.start_date.weekday()))
        for n in xrange(self.weeks() + 1):
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
            for n in xrange(self.months()):
                days = calendar.monthrange(start.year, start.month)[1]
                end = date(start.year, start.month, days)
                yield (start, end)
                start = end + timedelta(days=1)

    def get_quarterdelta(self):
        """
        Calcualte date difference in quraters.
        """
        start_quarter = month_to_quarter(self.start_date.month)
        end_quarter = month_to_quarter(self.end_date.month)
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
        quarter = month_to_quarter(self.start_date.month)
        start_month, end_month = quarter_to_month(quarter)
        start = date(self.start_date.year, start_month, 1)
        if self.quarters() == 0:
            days = calendar.monthrange(start.year, start.month + 2)[1]
            end = date(start.year, start.month + 2, days)
            yield (start, end)
        else:
            for n in xrange(self.quarters()):
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
        for n in xrange(self.start_date.year, self.end_date.year + 1):
            start = date(n, 1, 1)
            end = date(n, 12, 31)
            yield (start, end)

    def get_range(self):
        """
        Return a tuple that contains self.start_date and self.end_date
        """
        return (self.start_date, self.end_date)


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
        start =  base_date - timedelta(days=base_date.weekday())
        end = start + timedelta(days=6)
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
        base_start, _ = self.base_week().get_range()
        start, end = self.get_week_range(base_start - timedelta(days=7*weeks))
        return DateRange(start, end)

    def next_week(self, weeks=1):
        """
        Get the DateRange that n weeks after self.base_date.

        Argus:
            weeks - next n weeks
        """
        base_start, _ = self.base_week().get_range()
        start, end = self.get_week_range(base_start + timedelta(days=7*weeks))
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
        base_start, _ = self.base_month().get_range()
        for n in xrange(months):
            end = base_start - timedelta(days=1)
            start = date(end.year, end.month, 1)
            base_start = start
        end = end + timedelta(days=1)
        return DateRange(start, end)

    def next_month(self, months=1):
        """
        Get the DateRange that n months after self.base_date.

        Argus:
            months - next n months
        """
        _, base_end = self.base_month().get_range()
        for n in xrange(months):
            next_month = base_end + timedelta(days=1)
            start, end = self.get_month_range(next_month.year, next_month.month)
            base_end = end
        return DateRange(start, end)

    def get_quarter_range(self, year, quarter):
        """
        Get time range with specific year and quarter.
        """
        if quarter not in (1, 2, 3, 4):
            return (None, None)

        start_month, end_month = quarter_to_month(quarter)
        days = calendar.monthrange(year, end_month)[1]
        start = date(year, start_month, 1)
        end = date(year, end_month, days) + timedelta(days=1)
        return start, end

    def base_quarter(self):
        """
        Get the DateRange of the quarter that contains self.base_date.
        """
        quarter = month_to_quarter(self.base_date.month)
        start, end = self.get_quarter_range(self.base_date.year, quarter)
        return DateRange(start, end)

    def prev_quarter(self, quarters=1):
        """
        Get the DateRange that n quarters before self.base_date.

        Argus:
            quarters - n quarters ago
        """
        base_year = self.base_date.year
        base_quarter = month_to_quarter(self.base_date.month)
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
        base_quarter = month_to_quarter(self.base_date.month)
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
        return DateRange(from_date, self.base_date + timedelta(days=1))

    def to_date(self, to_date):
        """
        Return the DateRange from self.base_date to `to_date`

        Argus:
            to_date - Example: date(2015, 1, 1)
        """
        return DateRange(self.base_date, to_date + timedelta(days=1))
