# tiny-chess-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/a25822457/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/a25822457/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4 KB Python chess engine for make.fun's tiny-chess-01 bounty: alpha-beta
search with quiescence, a transposition table, null-move pruning,
piece-square tables and pawn-structure evaluation, on a fixed node budget
(deterministic, no clock, no randomness). `main.py` unpacks the engine
from `engine.b85` + `engine2.b85` (lzma + base85, split into lines — two
files because one blob no longer fits the 4,096-byte file cap) at startup;
the unpacked source is a single-file 0x88-board engine written for this bounty.

## v7 — evaluation upgrade over the submitted v6

v6 (trial-0 Elo 1279, 3W-0D-3L) plus two cheap evaluation terms, search untouched:

- **King shelter**: while queens are on the board, each missing pawn on the
  three squares directly in front of the king costs 15 cp. Castled kings
  keep their shield; exposed kings are now punished instead of being
  treated like any other king.
- **Rook activity**: a rook on an open file (+12), on a semi-open file
  (+6), or on the 7th rank (+15). Rooks finally get paid for what they do
  instead of standing on closed files for free.

Local results (official practice scorer, trial-0, same opponents and seed
as v6): **Elo 1545, 4W-1D-1L** — beat depth-2, depth-3, depth-4 and
nodes-100k, drew nodes-500k, lost only nodes-250k. Max think 7.6 s
(mean 2.9 s), inside the 10 s limit. A tempo bonus (+10 for the side to
move) was tried on top of this and scored lower in trial-0 (Elo 1364),
so it was left out.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
