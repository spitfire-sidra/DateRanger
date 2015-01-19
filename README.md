What is DateRanger?
=========================

A package for getting common date ranges.

Installation
===================

::

    pip install git+https://github.com/spitfire-sidra/DateRanger

Usage
=============


.. code-block:: python

    dr = DateRanger()

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


DateRange

.. code-block:: python

    r = DateRange(start_date, end_date)

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
    (start_date, end_date)


Contribute
==============

test:

::

    python -m unittest discover

This command executes all test cases under the folder `DateRanger/test/`
