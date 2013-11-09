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
            f = open('cachegrind.out.profilestats', "w")
            conv.output(f)
            f.close()
            stats.strip_dirs().sort_stats('cumulative').print_stats(10)
        return result
    return decorator
