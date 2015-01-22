#!/usr/bin/env python
# -*- coding: utf-8 -*-
import calendar
from datetime import date
from datetime import timedelta

from DateRanger.utils import get_quarter
from DateRanger.utils import get_monthrange
from DateRanger.objects import DateFrame
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

        Note:
            self.b____, 'b' means 'base'
        """
        self.bdate = base_date or date.today()
        self.bmonth = self.bdate.month
        self.byear = self.bdate.year
        self.bquarter = get_quarter(self.bmonth)

    def base_day(self):
        """
        Get the DateRange of self.bdate.
        """
        return DateFrame(self.bdate, self.bdate)

    def relative_day(self, days=0):
        """
        Calcuate a relative date from self.bdate.
        """
        rday = self.bdate + timedelta(days=days)
        return (rday, rday)

    def prev_day(self, days=1):
        """
        Get the DateRange that n days before self.bdate.

        Argus:
            days - n days ago
        """
        ndays = days * -1
        start, end = self.relative_day(days=ndays)
        return DateFrame(start, end)

    def next_day(self, days=1):
        """
        Get the DateRange that n days after self.bdate.

        Argus:
            days - next n days
        """
        start, end = self.relative_day(days=days)
        return DateFrame(start, end)

    def get_week_range(self, base_date):
        """
        Find the first/last day of the week for the given day.
        Weeks start on Sunday and end on Saturday.

        Argus:
            base_date - any date
        """
        start =  base_date - timedelta(days=base_date.weekday()+1)
        end = start + timedelta(days=6)
        return (start, end)

    def base_week(self):
        """
        Get DateRange of the week that contains self.bdate.
        """
        start, end = self.get_week_range(self.bdate)
        return DateFrame(start, end)

    def relative_week(self, weeks=0):
        """
        Calcuate a relative week range from self.bdate.
        """
        _, end_date = self.base_week().get_range()
        start, end = self.get_week_range(end_date + timedelta(days=7*weeks))
        return (start, end)

    def prev_week(self, weeks=1):
        """
        Get the DateRange that n weeks before self.bdate.

        Argus:
            weeks - n week ago
        """
        nweeks = weeks * -1
        start, end = self.relative_week(weeks=nweeks)
        return DateFrame(start, end)

    def next_week(self, weeks=1):
        """
        Get the DateRange that n weeks after self.bdate.

        Argus:
            weeks - next n weeks
        """
        start, end = self.relative_week(weeks=weeks)
        return DateFrame(start, end)

    def get_month_range(self, year, month):
        """
        Get the first and last day of the given month in given year.

        Args:
            year
            month
        """
        days = calendar.monthrange(year, month)[1]
        start = date(year, month, 1)
        end = date(year, month, days)
        return (start, end)

    def relative_month(self, months=0):
        """
        Calcuate a relative month range from self.bdate.
        """
        month_sum = self.bmonth + months
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
        year = self.byear + yeardelta
        start, end = self.get_month_range(year, month)
        return (start, end)

    def base_month(self):
        """
        Get the DateRange of the month that contains self.bdate
        """
        year, month = self.byear, self.bmonth
        start, end = self.get_month_range(year, month)
        return DateFrame(start, end)

    def prev_month(self, months=1):
        """
        Get the DateRange that n months before self.bdate.

        Argus:
            months - n months ago
        """
        nmonths = months * -1
        start, end = self.relative_month(months=nmonths)
        return DateFrame(start, end)

    def next_month(self, months=1):
        """
        Get the DateRange that n months after self.bdate.

        Argus:
            months - next n months
        """
        start, end = self.relative_month(months=months)
        return DateFrame(start, end)

    def get_quarter_range(self, year, quarter):
        """
        Get time range with specific year and quarter.
        """
        if quarter not in (1, 2, 3, 4):
            raise InvalidQuarter()

        start_month, end_month = get_monthrange(quarter)
        days = calendar.monthrange(year, end_month)[1]
        start = date(year, start_month, 1)
        end = date(year, end_month, days)
        return start, end

    def relative_quarter(self, quarters=0):
        """
        Calcuate a relative quarters range from self.bdate.
        """
        quarter_sum = self.bquarter + quarters
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
        year = self.byear + yeardelta
        start, end = self.get_quarter_range(year, quarter)
        return (start, end)

    def base_quarter(self):
        """
        Get the DateRange of the quarter that contains self.bdate.
        """
        quarter = get_quarter(self.bmonth)
        start, end = self.get_quarter_range(self.byear, quarter)
        return DateFrame(start, end)

    def prev_quarter(self, quarters=1):
        """
        Get the DateRange that n quarters before self.bdate.

        Argus:
            quarters - n quarters ago
        """
        nquarters = quarters * -1
        start, end = self.relative_quarter(quarters=nquarters)
        return DateFrame(start, end)

    def next_quarter(self, quarters=1):
        """
        Get the DateRange that n quarters after self.bdate.

        Argus:
            quarters - next n quarters
        """
        start, end = self.relative_quarter(quarters=quarters)
        return DateFrame(start, end)

    def get_year_range(self, year):
        """
        Get time range of the year.
        """
        start = date(year, 1, 1)
        end = date(year, 12, 31)
        return (start, end)

    def relative_year(self, years=0):
        year = self.byear + years
        start, end = self.get_year_range(year)
        return (start, end)

    def base_year(self):
        """
        Get the DateRange of the year that contains self.bdate.
        """
        start, end = self.get_year_range(self.byear)
        return DateFrame(start, end)

    def prev_year(self, years=1):
        """
        Get the DateRange that n years before self.bdate.

        Argus:
            years - n years ago
        """
        nyears = years * -1
        start, end = self.relative_year(years=nyears)
        return DateFrame(start, end)

    def next_year(self, years=1):
        """
        Get the DateRange that n years after self.bdate.

        Argus:
            year - next n years
        """
        start, end = self.relative_year(years=years)
        return DateFrame(start, end)

    def from_date(self, from_date):
        """
        Return the DateRange from `from_date` to self.bdate

        Argus:
            from_date - Example: date(2015, 1, 1)
        """
        if from_date > self.bdate:
            raise InvalidDateRange()

        return DateFrame(from_date, self.bdate + timedelta(days=1))

    def to_date(self, to_date):
        """
        Return the DateRange from self.bdate to `to_date`

        Argus:
            to_date - Example: date(2015, 1, 1)
        """
        if to_date < self.bdate:
            raise InvalidDateRange()

        return DateFrame(self.bdate, to_date + timedelta(days=1))
