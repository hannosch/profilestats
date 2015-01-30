Changelog
=========

2.0 (unreleased)
----------------

- Changed default behavior. Profile data is now accumulated over multiple
  function calls, no data is printed out and the profile data is only
  stored in the `callgrind.out` file.

  To get the old behavior use::

      @profile(cumulative=False,
               print_stats=10, dump_stats=True,
               profile_filename='profilestats.prof',
               callgrind_filename='cachegrind.out.profilestats')
      def foo(): pass

- Added arguments to profile decorator to influence it's behavior.

- Python 3 compatibility, thanks to lukasgraf.

1.0.2 (2011-02-13)
------------------

- Fixed profiling for functions which have a return value.
