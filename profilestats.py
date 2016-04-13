from cProfile import Profile
from functools import wraps
import pstats
import os
import threading

import pyprof2calltree

profiler = Profile()


def profile(cumulative=True, print_stats=0, sort_stats='cumulative',
            dump_stats=False, profile_filename='profilestats.out',
            callgrind_filename='callgrind.out', dump_dir='',
            generate_callgrind=True, generate_profile=True,
            profile_per_thread=False):
    def closure(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            result = None
            current_thread = threading.current_thread()
            if cumulative:
                if profile_per_thread:
                    tls = threading.local()
                    if not hasattr(tls, 'profiler'):
                        tls.profiler = Profile()
                    profiler = tls.profiler
                else:
                    global profiler
            else:
                profiler = Profile()
            try:
                result = profiler.runcall(func, *args, **kwargs)
            finally:
                if dump_stats:
                    if generate_profile:
                        if profile_per_thread:
                            profile_path = os.path.join(dump_dir, '%s.%s' % (current_thread.name, profile_filename))
                        else:
                            profile_path = os.path.join(dump_dir, profile_filename)
                        profiler.dump_stats(profile_path)

                stats = pstats.Stats(profiler)
                conv = pyprof2calltree.CalltreeConverter(stats)
                if generate_callgrind:
                    if profile_per_thread:
                        callgrind_path = os.path.join(dump_dir, '%s.%s' % (current_thread.name, callgrind_filename))
                    else:
                        callgrind_path = os.path.join(dump_dir, callgrind_filename)

                    with open(callgrind_path, 'w') as fd:
                        conv.output(fd)
                if print_stats:
                    stats.strip_dirs().sort_stats(
                        sort_stats).print_stats(print_stats)
            return result
        return decorator
    return closure
