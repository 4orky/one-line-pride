# One Line of Earned Pride — make.fun bounty
# u-mang-one-line-of-earned-pride-a0138557
#
# The program writes one line of text (1-240 characters) to /output/entry.txt.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. a quiet, earned moment of pride for someone in a scene — a small
#      person doing something hard, or a long effort finally landing
#   2. a concrete scene with a real person in it, seen happening, not summarised
#   3. the pride is earned inside the line, by effort the reader can feel —
#      never asserted, congratulated or explained
#   4. it lands in one read: the pride arrives by the last word
#   5. fresh: no stock trophy, podium or graduation
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: subject 9, scene 9, earned 10, landing 10, fresh 10 = 48
    ("He'd spent a decade rebuilding the boat in his garage; this morning "
     "he pushed it into the harbour, and it floated.",
     48),
    # score: subject 9, scene 10, earned 10, landing 9, fresh 9 = 47
    ("She failed her driving test eleven times; on the twelfth, she parked "
     "the car, switched the engine off, and sat a moment with both hands "
     "still on the wheel.",
     47),
    # score: subject 9, scene 9, earned 9, landing 9, fresh 9 = 45
    ("She'd spent six years learning English in the laundry room after her "
     "shift; tonight she answered the phone, took the order, and didn't ask "
     "anyone to repeat it.",
     45),
    # score: subject 10, scene 9, earned 9, landing 8, fresh 8 = 44
    ("At sixty-one, after three years of evening classes, she read the "
     "bedtime story to her granddaughter all the way to the end without "
     "stumbling on a single word.",
     44),
    # score: subject 9, scene 9, earned 9, landing 8, fresh 8 = 43
    ("He'd practised the same Chopin nocturne every evening for forty "
     "years; tonight, in the empty kitchen, he played it through without "
     "stopping once.",
     43),
    # score: subject 8, scene 9, earned 9, landing 8, fresh 9 = 43
    ("For thirty years he mopped the school hall before dawn; on his last "
     "morning, he left his keys on the desk and walked out across a floor "
     "that shone like a lake.",
     43),
    # score: subject 9, scene 9, earned 9, landing 7, fresh 8 = 42
    ("After four winters of dawn practice on the frozen pond, the girl "
     "landed her first axel, and the only sound was her skate carving "
     "the ice.",
     42),
    # score: subject 9, scene 8, earned 9, landing 8, fresh 8 = 42
    ("He'd carried the same toolbox up the same hill for thirty years; on "
     "his last day the apprentice carried it for him, and he let him.",
     42),
]

# The gate requires 1-240 characters of non-whitespace UTF-8 text.
BANNED_CLICHES = ("trophy", "podium", "graduation", "champion", "winner")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 240, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_CLICHES), \
            f"candidate uses a stock image: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what landed on disk: byte-identical to the chosen line, one
    # line only, inside the 1-240 character gate. A mismatch here means the
    # program failed loudly instead of submitting a wrong entry.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert "\n" not in written, "entry must be a single line"
    assert 1 <= len(written) <= 240, f"entry over gate: {len(written)} chars"
    print(f"{line} ({len(written)} chars)")


if __name__ == "__main__":
    main()
