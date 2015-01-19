What is DateRanger?
==========================

.. image:: https://travis-ci.org/spitfire-sidra/DateRanger.svg?branch=0.2.7.dev
    :target: https://travis-ci.org/spitfire-sidra/DateRanger

DateRanger is a module that helps user to find date ranges.

Installation
==========================

Currently, DateRanger is still in development.

It can be installed via GitHub and pip.

Install via GitHub
-------------------

.. code:: bash

    pip install git+https://github.com/spitfire-sidra/DateRanger

Install via pip
-------------------

.. code:: bash

    pip install --pre DateRanger

Usage
==========================

DateRange
---------

DateRange helps you to calculate number of days, weeks, quarters or years in date ranges.

-----------------
Example Code:
-----------------

.. code:: python

    from datetime import date
    from DateRanger import DateRanger
    from DateRanger.objects import DateRange

    r = DateRange(date(2014, 11, 1), date(2014, 12, 1))
    print r.months()
    print r.days()

-------------------------
Other useful methods
-------------------------

.. code:: python

    r.days()
    r.weeks()
    r.months()
    r.quarters()
    r.years()

    r.each_day()
    r.each_week()
    r.each_month()
    r.each_quarter()
    r.each_years()

    r.get_range()


DateRanger
----------------

To use this module, first we need to set the base_date.
Base_date can be any date in the past, present and future.
Default base_date is the present date which is TODAY (date.today()).
Based on the date given, this module helps us to find in what week,
quarter or year this date falls in.

For example:

If base_date is datetime.date(2015, 1, 19),
then the relative date ranges would be:

base_week
=> datetime.date(2015, 1, 18) ~ datetime.date(2015, 1, 25)
The week that contains base_date.

base_month
=> datetime.date(2015, 1, 1) ~ datetime.date(2015, 2, 1)
The month that contains base_date.

base_quarter
=> datetime.date(2015, 1, 1) ~ datetime.date(2015, 4, 1)
The quarter that contains base_date.

base_year
=> datetime.date(2015, 1, 1) ~ datetime.date(2016, 1, 1)
The year that contains base_date.

prev_week
=> datetime.date(2015, 1, 11) ~ datetime.date(2015, 1, 18)
Date range of previous week.

prev_month
=> datetime.date(2014, 12, 1) ~ datetime.date(2015, 1, 1)
Date range of previous month.

next_week
=> datetime.date(2015, 1, 25) ~ datetime.date(2015, 2,1)
Date range of next week.

next_month
=> datetime.date(2015, 2, 1) ~ datetime.date(2015, 3, 1)
Date range of next month.

------------------
Example Code:
------------------

.. code:: python

        from datetime import date
        from DateRanger import DateRanger
        from DateRanger.objects import DateRange

        dr = DateRanger()
        test_range = dr.prev_month(2)
        print test_range.get_range()

---------------------------
Other useful methods
---------------------------

.. code:: python

    dr.set_base_date(date)
    dr.get_base_day()
    dr.base_week()
    dr.base_month()
    dr.base_quarter()
    dr.base_year()

    dr.prev_week(2)
    dr.next_week(2)

    dr.prev_month(2)
    dr.next_month(2)

    dr.prev_quarter(2)
    dr.next_quarter(2)

    dr.prev_year(2)
    dr.next_year(2)

    dr.from_date(date)
    dr.to_date(date)

Contribute
================

test:
-----

.. code:: bash

        python -m unittest discover

This command executes all test cases under the directory ``DateRanger/test/``.
