============
profilestats
============

This module contains a simple helper decorator which allows you to profile
a function and write the profiling data to the file system in both the pstats
and the kcachegrind format.

The decorator can be used as::

    from profilestats import profile

    @profile
    def my_function(args, etc):
        pass
