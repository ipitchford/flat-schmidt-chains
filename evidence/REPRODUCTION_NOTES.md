# Reproduction notes

The final complete execution uses `PYTHONHASHSEED=0`, `OPENBLAS_NUM_THREADS=1` and `OMP_NUM_THREADS=1`. No supplied archive programme was edited. Every programme completed successfully; see `reproduction_final_run.txt` and `reruns/rerun_summary.json`.

Two earlier end-to-end tool calls were interrupted by the execution-call limit after their completed stages had passed. Those interrupted calls do not count as complete pass receipts. The final execution was allowed to finish and returned exit code zero. The exact source of earlier runtime variation was not fully traced; no mathematical failure is inferred from those interruptions. A fixed hash seed is retained for repeatable algebraic ordering, not asserted as a demonstrated diagnosis of the interruption.

A fresh execution changes elapsed times and may change ordering of algebraically equivalent displayed values. The frozen manifest protects the distributed snapshot; reproduction checks the identities and bounds, not equality of elapsed-time fields.
