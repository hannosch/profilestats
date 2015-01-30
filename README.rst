============
profilestats
============

This module contains a simple helper decorator, which allows you to profile
a function and write the profiling data to the file system in both the pstats
and the k/qcachegrind format.

The decorator can be used as::

    from profilestats import profile

    @profile(print_stats=10, dump_stats=True)
    def my_function(args, etc):
        pass

You can pass the following arguments to the decorator:

* `cumulative` (default: True) - Accumulate profile data over multiple
  function calls (True) or use a new profile for each function call (False).
  Only the data from the last profile is saved to disk.

* `print_stats` (default: 0) - How many lines of profile output to
  show on stdout after each function call. If set to 0, do not print
  out anything.

* `sort_stats` (default: 'cumulative') - How to sort the print output.
  Other options include 'time' and 'ncalls'.

* `dump_stats` (default: False) - Save the profile data in the Python
  profile format to a file.

* `profile_filename` (default: 'profilestats.out') - The filename for
  the profile data in Python's own format.

* `callgrind_filename` (default: 'callgrind.out') - The filename for
  the profile data in k/qcachegrind's format.
