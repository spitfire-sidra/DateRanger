#!/usr/bin/env python
# -*- coding: utf-8 -*-
import calendar
from datetime import date
from datetime import timedelta

from DateRanger.utils import get_quarter
from DateRanger.utils import get_monthrange
from DateRanger.objects import DateRange
from DateRanger.exceptions import InvalidDateRange
from DateRanger.exceptions import InvalidQuarter


class DateRanger(object):

    """
    A class for getting common bussiness date ranges.
    """

    def __init__(self, base_date=None):
        """
        Argus:
            base_date - the base day. Example: date(2009, 11, 1)
        """
        self.set_base_date(base_date)

    def set_base_date(self, base_date=None):
        """
        Set base date.

        Argus:
            base_date - Example: date(2009, 11, 1)
        """
        self.base_date = base_date or date.today()

    def base_day(self):
        """
        Get the DateRange of self.base_date.
        """
        return DateRange(self.base_date, self.base_date + timedelta(days=1))

    def relative_day(self, days=0):
        """
        Calcuate a relative date from self.base_date.
        """
        rday = self.base_date + timedelta(days=days)
        return (rday, rday + timedelta(days=1))

    def prev_day(self, days=1):
        """
        Get the DateRange that n days before self.base_date.

        Argus:
            days - n days ago
        """
        ndays = days * -1
        start, end = self.relative_day(days=ndays)
        return DateRange(start, end)

    def next_day(self, days=1):
        """
        Get the DateRange that n days after self.base_date.

        Argus:
            days - next n days
        """
        start, end = self.relative_day(days=days)
        return DateRange(start, end)

    def get_week_range(self, base_date):
        """
        Find the first/last day of the week for the given day.
        Weeks start on Sunday and end on Sunday.
        Because we don't include the last day.

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

    def relative_week(self, weeks=0):
        """
        Calcuate a relative week range from self.base_date.
        """
        _, end_date = self.base_week().get_range()
        start, end = self.get_week_range(end_date + timedelta(days=7*weeks))
        return (start, end)

    def prev_week(self, weeks=1):
        """
        Get the DateRange that n weeks before self.base_date.

        Argus:
            weeks - n week ago
        """
        nweeks = weeks * -1
        start, end = self.relative_week(weeks=nweeks)
        return DateRange(start, end)

    def next_week(self, weeks=1):
        """
        Get the DateRange that n weeks after self.base_date.

        Argus:
            weeks - next n weeks
        """
        start, end = self.relative_week(weeks=weeks)
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

    def relative_month(self, months=0):
        """
        Calcuate a relative month range from self.base_date.
        """
        base_year = self.base_date.year
        month_sum = self.base_date.month + months
        if month_sum < 0:
            back_months = abs(month_sum)
            yeardelta = ((back_months // 12) + 1) * -1
            month = 12 - (back_months % 12)
        elif month_sum == 0:
            yeardelta = -1
            month = 12
        elif month_sum <= 12:
            yeardelta = 0
            month = month_sum
        else:
            yeardelta = month_sum // 12
            month = month_sum % 12
        year = base_year + yeardelta
        start, end = self.get_month_range(year, month)
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
        nmonths = months * -1
        start, end = self.relative_month(months=nmonths)
        return DateRange(start, end)

    def next_month(self, months=1):
        """
        Get the DateRange that n months after self.base_date.

        Argus:
            months - next n months
        """
        start, end = self.relative_month(months=months)
        return DateRange(start, end)

    def get_quarter_range(self, year, quarter):
        """
        Get time range with specific year and quarter.
        """
        if quarter not in (1, 2, 3, 4):
            raise InvalidQuarter()

        start_month, end_month = get_monthrange(quarter)
        days = calendar.monthrange(year, end_month)[1]
        start = date(year, start_month, 1)
        end = date(year, end_month, days) + timedelta(days=1)
        return start, end

    def relative_quarter(self, quarters=0):
        """
        Calcuate a relative quarters range from self.base_date.
        """
        base_year = self.base_date.year
        base_quarter = get_quarter(self.base_date.month)
        quarter_sum = base_quarter + quarters
        if quarter_sum < 0:
            back_quarters = abs(quarter_sum)
            yeardelta = ((back_quarters // 4) + 1) * -1
            quarter = 4 - (back_quarters % 4)
        elif quarter_sum == 0:
            yeardelta = -1
            quarter = 4
        elif quarter_sum <= 4:
            yeardelta = 0
            quarter = quarter_sum
        else:
            yeardelta = quarter_sum // 4
            quarter = quarter_sum % 4
        year = base_year + yeardelta
        start, end = self.get_quarter_range(year, quarter)
        return (start, end)

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
        nquarters = quarters * -1
        start, end = self.relative_quarter(quarters=nquarters)
        return DateRange(start, end)

    def next_quarter(self, quarters=1):
        """
        Get the DateRange that n quarters after self.base_date.

        Argus:
            quarters - next n quarters
        """
        start, end = self.relative_quarter(quarters=quarters)
        return DateRange(start, end)

    def get_year_range(self, year):
        """
        Get time range of the year.
        """
        start = date(year, 1, 1)
        end = date(year + 1, 1, 1)
        return (start, end)

    def relative_year(self, years=0):
        year = self.base_date.year + years
        start, end = self.get_year_range(year)
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
        nyears = years * -1
        start, end = self.relative_year(years=nyears)
        return DateRange(start, end)

    def next_year(self, years=1):
        """
        Get the DateRange that n years after self.base_date.

        Argus:
            year - next n years
        """
        start, end = self.relative_year(years=years)
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
