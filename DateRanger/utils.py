#!/usr/bin/env python
# -*- coding: utf-8 -*-
from DateRanger.exceptions import InvalidMonth
from DateRanger.exceptions import InvalidQuarter


def get_quarter(month):
    """
    Determine a month belongs to which quarter.

    Argus:
        month - 1 ~ 12 (Integer)
    """
    if month not in range(1, 13):
        raise InvalidMonth()

    quarter = 4
    if month in (1, 2, 3): quarter = 1
    if month in (4, 5, 6): quarter = 2
    if month in (7, 8, 9): quarter = 3
    return quarter


def get_monthrange(quarter):
    """
    Get start and end month of a quarter.

    Argus:
        quarter - 1 ~ 4 (Integer)
    """
    if quarter not in range(1, 5):
        raise InvalidQuarter()

    monthranges = ((1, 3), (4, 6), (7, 9), (10, 12))
    return monthranges[quarter-1]
