What is DateRanger?
==========================

.. image:: https://travis-ci.org/spitfire-sidra/DateRanger.svg
   :target: https://travis-ci.org/spitfire-sidra/DateRanger

.. image:: https://coveralls.io/repos/spitfire-sidra/DateRanger/badge.svg
  :target: https://coveralls.io/r/spitfire-sidra/DateRanger

.. image:: https://pypip.in/v/DateRanger/badge.png
   :target: https://pypi.python.org/pypi/DateRanger

.. image:: https://pypip.in/d/DateRanger/badge.png
   :target: https://pypi.python.org/pypi/DateRanger



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

DateFrame
---------

DateFrame helps you to calculate number of days, weeks, quarters or years in date ranges.

It also can yeild each day, week, month, quarters in date ranges.



-----------------
Example code:
-----------------

To calculate number of days, weeks, months, quarters or years in date ranges.

.. code:: python

    >>> from datetime import date
    >>> from DateRanger.objects import DateFrame
    >>>
    >>> df = DateFrame(date(2014, 11, 1), date(2014, 12, 20))
    >>> df.days() # There are 49 days between date(2014, 11, 1) and date(2014, 12, 20)
    49
    >>> df.weeks() # There are 7 weeks between date(2014, 11, 1) and date(2014, 12, 20)
    7
    >>> df.months() 
    1
    >>> df.quarters()
    0
    >>> df.years()
    0



To yield each day, week, month, quarter or years in date ranges.

.. code:: python

    >>> from datetime import date
    >>> from DateRanger.objects import DateFrame
    >>>
    >>> df = DateFrame(date(2014, 11, 30), date(2014, 12, 2))
    >>> days = [day for day in df.each_day()]
    >>> days
    [datetime.date(2014, 11, 30), datetime.date(2014, 12, 1), datetime.date(2014, 12, 2)]
    >>>
    >>> weeks = [week for week in df.each_week()] # 2 weeks
    >>> weeks # 2 tuples in a list
    [(datetime.date(2014, 11, 23), datetime.date(2014, 11, 29)), (datetime.date(2014, 11, 30), datetime.date(2014, 12, 6))]
 


-------------------------
Other useful methods
-------------------------

.. code:: python

    >>> df.days()
    >>> df.weeks()
    >>> df.months()
    >>> df.quarters()
    >>> df.years()
    >>>
    >>> df.each_day()
    >>> df.each_week()
    >>> df.each_month()
    >>> df.each_quarter()
    >>> df.each_years()
    >>> df.get_range()



DateRanger
----------------

To use this module, first we need to set the base_date. Base_date can be any date in the past, present and future. Default base_date is the present date which is TODAY (date.today()). Based on the date given, this module helps us to find in what week, quarter or year this date falls in.

For example:

If base_date is datetime.date(2015, 1, 19), then the relative date ranges would be:

.. code::

    base_week
    => datetime.date(2015, 1, 18) ~ datetime.date(2015, 1, 24)
    The week that contains base_date.

.. code::

    base_month
    => datetime.date(2015, 1, 1) ~ datetime.date(2015, 1, 31)
    The month that contains base_date.

.. code::

    base_quarter
    => datetime.date(2015, 1, 1) ~ datetime.date(2015, 3, 31)
    The quarter that contains base_date.

.. code::

    base_year
    => datetime.date(2015, 1, 1) ~ datetime.date(2015, 12, 31)
    The year that contains base_date.

.. code::

    prev_week
    => datetime.date(2015, 1, 11) ~ datetime.date(2015, 1, 17)
    Date range of previous week.

.. code::

    prev_month
    => datetime.date(2014, 12, 1) ~ datetime.date(2012, 12, 31)
    Date range of previous month.

.. code::

    next_week
    => datetime.date(2015, 1, 25) ~ datetime.date(2015, 1, 31)
    Date range of next week.

.. code::

    next_month
    => datetime.date(2015, 2, 1) ~ datetime.date(2015, 2, 28)
    Date range of next month.



------------------
Example code:
------------------

.. code:: python

        >>> from datetime import date
        >>> from DateRanger import DateRanger
        >>>
        >>> dr = DateRanger(base_date=date(2015, 1, 1))
        >>> date_frame = dr.prev_month(2)
        >>> date_frame
        <DateRanger.objects.DateFrame object ...>
        >>> date_frame.weeks()
        5
        >>> date_frame.get_range()
        (datetime.date(2014, 11, 1), datetime.date(2014, 11, 30))



---------------------------
Other useful methods
---------------------------

.. code:: python

    >>> dr.set_base_date(date)
    >>> dr.get_base_day()
    >>> dr.base_week()
    >>> dr.base_month()
    >>> dr.base_quarter()
    >>> dr.base_year()
    >>>
    >>> dr.prev_week(...)
    >>> dr.next_week(...)
    >>>
    >>> dr.prev_month(...)
    >>> dr.next_month(...)
    >>>
    >>> dr.prev_quarter(...)
    >>> dr.next_quarter(...)
    >>>
    >>> dr.prev_year(...)
    >>> dr.next_year(...)
    >>>
    >>> dr.from_date(...)
    >>> dr.to_date(...)



Contribute
================

test:
-----

.. code:: bash

        python -m unittest discover

This command executes all test cases under the directory ``DateRanger/test/``.
