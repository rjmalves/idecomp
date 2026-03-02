import time
import statistics
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent))

from tests.mocks.mock_open import mock_open


def bench_text_read(handler_cls, mock_data, n_iter=10):
    times = []
    for _ in range(n_iter):
        m = mock_open(read_data=mock_data)
        with patch("builtins.open", m):
            start = time.perf_counter()
            handler_cls.read("bench_file")
            elapsed = time.perf_counter() - start
        times.append(elapsed * 1000)
    mean = statistics.mean(times)
    std = statistics.stdev(times) if len(times) > 1 else 0.0
    return mean, std


def bench_binary_read(handler_cls, file_path, n_iter=10):
    times = []
    for _ in range(n_iter):
        start = time.perf_counter()
        handler_cls.read(str(file_path))
        elapsed = time.perf_counter() - start
        times.append(elapsed * 1000)
    mean = statistics.mean(times)
    std = statistics.stdev(times) if len(times) > 1 else 0.0
    return mean, std


def bench_dadger():
    from idecomp.decomp.dadger import Dadger
    from tests.mocks.arquivos.dadger import MockDadger

    data = "".join(MockDadger)
    return bench_text_read(Dadger, data)


def bench_hidr():
    from idecomp.decomp.hidr import Hidr

    path = (
        Path(__file__).parent.parent
        / "tests"
        / "mocks"
        / "arquivos"
        / "hidr.dat"
    )
    return bench_binary_read(Hidr, path)


def bench_vazoes():
    from idecomp.decomp.vazoes import Vazoes

    path = (
        Path(__file__).parent.parent
        / "tests"
        / "mocks"
        / "arquivos"
        / "vazoes.rv0"
    )
    return bench_binary_read(Vazoes, path)


def bench_dec_oper_usih():
    from idecomp.decomp.dec_oper_usih import DecOperUsih
    from tests.mocks.arquivos.dec_oper_usih import MockDecOperUsih

    data = "".join(MockDecOperUsih)
    return bench_text_read(DecOperUsih, data)


def run_all():
    results = []
    benchmarks = [
        ("Dadger", bench_dadger),
        ("Hidr", bench_hidr),
        ("Vazoes", bench_vazoes),
        ("DecOperUsih", bench_dec_oper_usih),
    ]
    for name, fn in benchmarks:
        try:
            mean, std = fn()
            results.append((name, "read", mean, std, 10))
        except Exception as e:
            results.append((name, "read", f"ERROR: {e}", 0.0, 0))
    return results
