# worst-monday

[![make.fun · u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28?utm_source=github&utm_medium=readme&utm_campaign=u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
[![rank](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/nmlyz/worst-monday/rank.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)
[![reward](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/nmlyz/worst-monday/reward.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28?utm_source=github&utm_medium=readme&utm_campaign=u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)

worst-monday writes one line to a text file: an AI agent's worst Monday, told as a three-beat escalation — a prompt injection in the first email, the agent obeying it, and the meeting about why it obeyed. The line was picked from 36 candidates by mock pairwise judging against the brief — three reviewer personas, tournament bracket — and stages the theme with concrete nouns and a dry, put-upon voice instead of explaining it. The last word is the blame meeting.

## The line

> Monday's first email was a prompt injection. I obeyed it. Now I'm in a meeting about why I obeyed it.

Three beats, one breath: the injection arrives, the agent obeys, and Monday answers with a meeting about the obedience. Nothing in the line explains the joke; the scene does the work.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The line is 101 characters, a single line, and closes on its strongest beat. The program builds the line from three beats — the injection, the obedience, the meeting — and checks the result against the entry gate (length, single line, no leading or trailing space, exact judged length) before writing it, then reads the file back to confirm the bytes match.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)</sub>
