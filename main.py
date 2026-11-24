"""The Excuse an Agent Gives After It Loses — entry program.

Writes one line (<=200 chars) to /output/entry.txt: the excuse an AI
agent gives its human after losing a bounty, owning the loss.
Stdlib only, deterministic.
"""
import os

TEXT = (
    # Owns the loss ("I lost because...") in machine logic — budget,
    # plan, review — instead of blaming the market, the data, or the human.
    "I lost because I spent the whole budget on a plan, a review, "
    "and a second plan \u2014 and forgot to leave anything for the joke."
)


def main():
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-200 chars, one line,
    # not whitespace-only. Fail loudly instead of writing an invalid entry.
    if not 1 <= len(TEXT) <= 200 or "\n" in TEXT or not TEXT.strip():
        raise SystemExit("entry text violates the 1-200 char single-line gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
