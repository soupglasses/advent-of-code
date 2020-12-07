Advent of Code Day 7: ``handy_haversacks``
==========================================

https://adventofcode.com/2020/day/7

**Running the tests:**

.. code-block:: sh

    $ python -m doctest -v tests.rst

**Setup:**

.. code-block:: python

    >>> example = """light red bags contain 1 bright white bag, 2 muted yellow bags.\ndark orange bags contain 3 bright white bags, 4 muted yellow bags.\nbright white bags contain 1 shiny gold bag.\nmuted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\nshiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\ndark olive bags contain 3 faded blue bags, 4 dotted black bags.\nvibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\nfaded blue bags contain no other bags.\ndotted black bags contain no other bags."""


``parse``
---------

Returns a dictionary with keys of the bag's color and a list of tuples containing the rules that the bag color needs to follow.

**Signature:**

.. code-block:: python
    
    parse(raw_rules: str) -> dict[str, list]

**Usage:**

.. code-block:: python

    >>> from handy_haversacks import parse

.. code-block:: python

    >>> rules = parse(example)

    >>> list(rules.items())[0:2]
    [('light red', [(1, 'bright white'), (2, 'muted yellow')]), ('dark orange', [(3, 'bright white'), (4, 'muted yellow')])]


``fits_in_bags``
----------------

Returns a set of all bag colors that ``color`` can fit into following ``rules``.

**Signature**:

.. code-block:: python
    
    fits_in_bags(color: str, rules: dict[str, list]) -> set

**Usage:**

.. code-block:: python

    >>> from handy_haversacks import fits_in_bags

.. code-block:: python

    >>> sorted(fits_in_bags('shiny gold', rules))
    ['bright white', 'dark orange', 'light red', 'muted yellow']
    
    >>> len(fits_in_bags('shiny gold', rules))
    4


``required_bags``
-----------------

Returns the total amount of bags required to fit into bag ``color``, following the given ``rules``.

Note: Return includes the top most bag(s), subtract the return value by ``count`` to get total bags needed inside of parent bag.

**Signature**:

.. code-block:: python
    
    required_bags(color: str, count: int, rules: dict[str, list]) -> int

**Usage:**

.. code-block:: python

    >>> from handy_haversacks import required_bags

.. code-block:: python

    >>> required_bags('shiny gold', 1, rules) - 1
    32

