# Benchmark Results

| Handler | Operation | Mean (ms) | Std (ms) | Iterations |
| ------- | --------- | --------- | -------- | ---------- |
| Dadger | read | 0.16 | 0.32 | 10 |
| Hidr | read | 39.42 | 0.28 | 10 |
| Vazoes | read | 3.05 | 0.22 | 10 |
| DecOperUsih | read | 0.03 | 0.03 | 10 |
| idecomp.decomp | import | 0.10 | 0.02 | 50 |
| idecomp.decomp + Dadger | import | 3.12 | 4.17 | 50 |
