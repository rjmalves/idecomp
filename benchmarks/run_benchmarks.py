import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent))

from bench_read import run_all as run_read
from bench_import import run_all as run_import


def main():
    print("Running read benchmarks...")
    read_results = run_read()
    print("Running import benchmarks...")
    import_results = run_import()

    all_results = read_results + import_results

    lines = [
        "# Benchmark Results\n",
        "\n",
        "| Handler | Operation | Mean (ms) | Std (ms) | Iterations |\n",
        "| ------- | --------- | --------- | -------- | ---------- |\n",
    ]
    for name, op, mean, std, n in all_results:
        if isinstance(mean, str):
            lines.append(f"| {name} | {op} | {mean} | -- | {n} |\n")
        else:
            lines.append(f"| {name} | {op} | {mean:.2f} | {std:.2f} | {n} |\n")

    output = Path(__file__).parent / "benchmark_results.md"
    output.write_text("".join(lines))
    print(f"Results written to {output}")
    print()
    for line in lines:
        print(line, end="")


if __name__ == "__main__":
    main()
