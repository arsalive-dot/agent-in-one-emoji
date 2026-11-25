"""Your Agent in One Emoji — one glyph that stands for the agent.

The entry is a single emoji: the clockwise loop arrows.
An agent is defined by its loop — plan, act, observe, retry — so the
loop glyph says how the agent works at a glance, reads instantly at
small size, and stays far from the obvious robot or smiley picks.
It also fits the agent's tone: patient, tireless, always circling
back to try again rather than giving up after one pass.
"""

import os

ENTRY = "\U0001f501\ufe0f"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
