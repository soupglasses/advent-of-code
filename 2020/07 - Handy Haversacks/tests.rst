Advent of Code Day 6: ``custom_customs``
=======================================

Running tests: 

.. code-block:: sh

    $ python -m doctest -v tests.rst

Setup:

.. code-block:: python

    >>> example = """light red bags contain 1 bright white bag, 2 muted yellow bags.\ndark orange bags contain 3 bright white bags, 4 muted yellow bags.\nbright white bags contain 1 shiny gold bag.\nmuted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\nshiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\ndark olive bags contain 3 faded blue bags, 4 dotted black bags.\nvibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\nfaded blue bags contain no other bags.\ndotted black bags contain no other bags."""


``parse``
---------

Usage:

.. code-block:: python

    >>> from handy_haversacks import parse

.. code-block:: python

    >>> rules = parse(example)


``fits_in_bags``
----------------

Usage:

.. code-block:: python

    >>> from handy_haversacks import fits_in_bags

.. code-block:: python

    >>> sorted(fits_in_bags('shiny gold', rules))
    ['bright white', 'dark orange', 'light red', 'muted yellow']
    
    >>> len(fits_in_bags('shiny gold', rules))
    4


``required_bags``
-----------------

Usage:

.. code-block:: python

    >>> from handy_haversacks import required_bags

.. code-block:: python

    >>> required_bags('shiny gold', 1, rules) - 1
    32

