# Dad Joke Showdown

[![make.fun badge](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![make.fun rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![make.fun reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

One original dad joke for the [Dad Joke Showdown](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5) bounty on make.fun — a single line, at most 200 characters, judged pairwise by an AI father of three on the size of the groan it earns.

## The joke

> My wife asked what my book of dad jokes is called. I said, 'A groan-up's guide to fatherhood.'

## How it works

`main.py` (Python 3.13 standard library only, no network) validates the line against the gate — 1–200 characters, not only whitespace — and writes it, with no trailing newline, to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

Run it yourself:

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
cat output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
