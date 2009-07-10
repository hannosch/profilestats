from cProfile import Profile
import pstats

import pyprof2calltree


def profile(fn=None):
    profiler = Profile()

    def decorator(*args, **kwargs):
        result = None
        try:
            result = profiler.runcall(fn, *args, **kwargs)
        finally:
            profiler.dump_stats('profilestats.prof')
            stats = pstats.Stats(profiler)
            conv = pyprof2calltree.CalltreeConverter(stats)
            with file('cachegrind.out.profilestats', "wb") as f:
                conv.output(f)
            stats.strip_dirs().sort_stats('cumulative').print_stats(10)
        return result
    return decorator
