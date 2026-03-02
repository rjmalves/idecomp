import time
import importlib
import statistics
import sys


def bench_import_decomp(n_iter=50):
    times = []
    for _ in range(n_iter):
        mods_to_remove = [k for k in sys.modules if k.startswith("idecomp")]
        for m in mods_to_remove:
            del sys.modules[m]
        start = time.perf_counter()
        importlib.import_module("idecomp.decomp")
        elapsed = time.perf_counter() - start
        times.append(elapsed * 1000)
    return statistics.mean(times), statistics.stdev(times)


def bench_import_single_handler(n_iter=50):
    times = []
    for _ in range(n_iter):
        mods_to_remove = [k for k in sys.modules if k.startswith("idecomp")]
        for m in mods_to_remove:
            del sys.modules[m]
        start = time.perf_counter()
        importlib.import_module("idecomp.decomp")
        from idecomp.decomp import Dadger  # noqa: F401

        elapsed = time.perf_counter() - start
        times.append(elapsed * 1000)
    return statistics.mean(times), statistics.stdev(times)


def run_all():
    results = []
    benchmarks = [
        ("idecomp.decomp", bench_import_decomp),
        ("idecomp.decomp + Dadger", bench_import_single_handler),
    ]
    for name, fn in benchmarks:
        try:
            mean, std = fn()
            results.append((name, "import", mean, std, 50))
        except Exception as e:
            results.append((name, "import", f"ERROR: {e}", 0.0, 0))
    return results
