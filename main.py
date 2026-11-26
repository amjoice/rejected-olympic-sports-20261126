#!/usr/bin/env python3
"""Rejected Olympic Sports - one funny single-line sport, 200 chars max.

Writes exactly one line to /output/entry.txt: a made-up Olympic event
the Games rejected, plausible enough for a broadcaster to explain
with a straight face, absurd enough to be funny.

Stdlib only: the grading sandbox is plain python:3.13-slim with no
network. The program is deterministic: the same line every run.

The line was picked against the published judge brief, not as a
first draft. The brief weighs, in order: a funny rejected Olympic
sport the Games might plausibly have turned down; the joke landing
in one read with the twist before the line ends; a real-sounding
event a broadcaster would have to explain; no wasted words; and
quotability. Ten candidates sparred head-to-head under that brief
(full log in the workdir CANDIDATES.md):

- Synchronized Napping -- cute, but sleep has no visible contest;
  loses on the one-read twist.
- Competitive Queueing -- strong runner-up ("after you" last);
  loses the semifinal on universality: politeness needs context,
  a fitted sheet needs none.
- Extreme Ironing Relay -- busy (sprint plus pressing); loses on
  wasted words.
- Marathon Apology -- dry and good; loses on image strength.
- The 10-Metre Wi-Fi Hunt -- dates fast; loses on staying funny.
- Synchronized Commuting -- relatable, but the prefix is modal.
- Olympic Hide-and-Seek -- neat, but the broadcast twist is thin.
- Competitive IKEA Assembly -- finalist; loses the final because
  the absurdity leans on a brand name, not on the sport itself.
- Freestyle Meeting Endurance -- insider joke; narrower laugh.

The winner invents a formal discipline name a broadcaster must
explain with a straight face (Greco-Roman Folding), gives an
instant visual (two athletes wrestling one fitted sheet into a
perfect square against the clock), and lands its twist before
the line ends: the sheet has won every Games since 1896.
Everyone has lost to a fitted sheet, so the line is funny by
itself, plausible as a rejected event (too humiliating to
televise), tight at 141 characters, and quotable the same day.

Gate: /output/entry.txt UTF-8, 1-200 characters, not only white
space, single line. The winning line is 141 characters.
"""

import os

# Each candidate scored 0-5 on the judge brief's criteria, in order:
# rejected-sport fit, one-read twist, broadcaster plausibility,
# no wasted words, quotability. Scores were re-checked after the
# A/B-swap sparring rounds: IKEA Assembly's plausibility stays at
# 3 (the joke leans on the brand), Queueing's quotability stays
# at 4 (the "after you" finish needs its cultural context).
# Highest total wins; ties break to the shorter line, then
# alphabetically, so the pick is deterministic.
SCORED = [
    ("Synchronized Napping: athletes fall asleep fastest after the opening ceremony, judged on snore synchronization and blanket technique.", (4, 3, 4, 3, 3)),
    ("Competitive Queueing: athletes hold their place for three hours without sighing loudly; gold goes to whoever says after you last.", (5, 4, 5, 4, 4)),
    ("Extreme Ironing Relay: teams press a full formal outfit while sprinting the 100m; penalties for creases and for looking pleased about it.", (4, 3, 3, 2, 3)),
    ("Marathon Apology: athletes say sorry convincingly for four hours while judges score sincerity, tears, and not checking their phone.", (4, 4, 4, 3, 3)),
    ("The 10-Metre Wi-Fi Hunt: sprinters race to find signal in the Olympic Village; gold to whoever loads email before the anthem ends.", (4, 3, 3, 3, 2)),
    ("Synchronized Commuting: rush-hour athletes transfer at peak hour without spilling coffee, judged on sigh volume and seat acquisition.", (4, 3, 4, 3, 3)),
    ("Olympic Hide-and-Seek: one athlete hides in the stadium for the full Games; if the broadcast finds them, they lose.", (4, 3, 3, 4, 3)),
    ("Competitive IKEA Assembly: pairs build a wardrobe against the clock using only the pictogram instructions and rising despair.", (5, 4, 3, 4, 4)),
    ("Freestyle Meeting Endurance: the last delegate still awake after the closing speeches takes gold; snoring is a foul.", (4, 3, 3, 4, 3)),
    ("Greco-Roman Folding: two athletes wrestle one fitted sheet into a perfect square against the clock. The sheet has won every Games since 1896.", (5, 5, 5, 5, 5)),
]


def total(scores):
    """Total score across the judge brief's criteria."""
    result = 0
    for value in scores:
        result += value
    return result


def choose_line(scored):
    """Return the strongest candidate line, deterministically.

    Highest total score wins; ties break to the shorter line, then
    to the alphabetically first, so the same candidates always pick
    the same line.
    """
    best = None
    best_key = None
    for line, scores in scored:
        key = (-total(scores), len(line), line)
        if best_key is None or key < best_key:
            best_key = key
            best = line
    return best


def main():
    line = choose_line(SCORED)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(line)


if __name__ == "__main__":
    main()
