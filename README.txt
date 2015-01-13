A class for getting common date ranges.

Usage
=============

::

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


Contribute
==============

test:

    python -m unittest discover

This command executes all test cases under the folder DateRanger/test/
