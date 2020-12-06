Advent of Code Day 6: ``custom_customs``
=======================================

Running tests: ``python -m doctest -v tests.rst``

``count_any``:
--------------

For each group, count the unique answers. Return the total for all groups.

Import function:

    >>> from custom_customs import count_any

Now to use it:

    >>> count_any([])
    0
    >>> count_any(['w\ns\nq\ns'])
    3
    >>> count_any(['klfrwivqhc\nw\nwgyze\nanw'])
    16
    >>> count_any(['w\ns\nq\ns', 'klfrwivqhc\nw\nwgyze\nanw'])
    19

Using ``count_all``:
--------------------

For each group, count what everyone answered. Return the total for all groups.

Import function:

    >>> from custom_customs import count_all

Now to use it:

    >>> count_all([])
    0
    >>> count_all(['w\ns\nq\ns'])
    0
    >>> count_all(['ur\nrq\nr'])
    1
    >>> count_all(['mraiyzpxngdl\nynzdmgkxwpaiolr'])
    12
    >>> count_all(['ur\nrq\nr', 'mraiyzpxngdl\nynzdmgkxwpaiolr'])
    13
