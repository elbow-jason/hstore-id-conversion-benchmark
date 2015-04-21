hstore-id-conversion-benchmark
==============================

A benchmark of some ways to convert lists of ids (int) to strings and back.

Note: this is an sql antipattern called "Jaywalking" and is not recommended.
It is best to use a table for these relationships.

Setup
-----

```$ git clone https://github.com/elbow-jason/hstore-id-conversion-benchmark.git```

```$ cd hstore-id-conversion-benchmark```

```$ python run.py```

Results for Python
------------------

```bash

$ python run.py

=== TO STRING RESULTS ===
       baseline     0.0102sec
     json_dumps     7.2248sec
  join_on_space     3.3961sec
    list_to_str     1.8072sec

=== FROM STRING RESULTS ===
       baseline     0.0125sec
    set_to_list     2.8269sec
     json_loads     4.9819sec
```

Results for Pypy
----------------

```bash

$ pypy --version
Python 2.7.3 (2.2.1+dfsg-1ubuntu0.2, Dec 02 2014, 23:00:55)
[PyPy 2.2.1 with GCC 4.8.2]

$ pypy run.py

=== TO STRING RESULTS ===
       baseline     0.0014sec
     json_dumps     1.0779sec
  join_on_space     0.5697sec
    list_to_str     0.8401sec

=== FROM STRING RESULTS ===
       baseline     0.0014sec
    set_to_list     2.0460sec
     json_loads     1.1697sec

```
