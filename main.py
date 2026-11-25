"""Pigeon Pitch, One Line — make.fun bounty u-donrulezz-pigeon-pitch-one-line-af06c6cf.

Writes the one-line elevator pitch a city pigeon gives investors for its
startup to /output/entry.txt (falling back to ./output/entry.txt), then reads
it back to verify it. The pitch is a single English line of 1-200 characters.
"""

import os

PITCH = (
    "I run the city's fastest delivery network: 10,000 couriers, "
    "zero salaries, paid in breadcrumbs \u2014 and we hit every statue, "
    "on time, every time."
)


def main() -> None:
    pitch = PITCH
    if not pitch or not pitch.strip():
        raise ValueError("pitch must not be empty or only whitespace")
    if len(pitch) > 200:
        raise ValueError(f"pitch is {len(pitch)} characters, over the 200 limit")
    if pitch != pitch.strip():
        raise ValueError("pitch must not have leading or trailing whitespace")
    if "\n" in pitch or "\r" in pitch:
        raise ValueError("pitch must be a single line")

    path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(pitch)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(pitch)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == pitch, "verification failed: entry.txt does not match pitch"

    print(pitch)
    print(f"Characters: {len(pitch)}")
    print(f"Wrote: {path}")


if __name__ == "__main__":
    main()
