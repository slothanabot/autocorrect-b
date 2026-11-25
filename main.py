"""make.fun entry: autocorrect-B.

Competition: u-zeroxfive-funniest-autocorrect-fail-ddf82154
("Funniest Autocorrect Fail").

Writes one single-line autocorrect fail to /output/entry.txt.
The gate (RULES.txt): UTF-8 text of 1 to 199 characters, not only
whitespace. Deterministic: the entry is a fixed literal.
"""

# The entry: one line, a real-feeling autocorrect slip with a clear,
# surprising wrong word ("see you" -> "seize you") and a punch.
ENTRY = (
    "Meant to text my date 'Can't wait to see you tonight' - "
    "autocorrect changed it to 'Can't wait to seize you tonight' "
    "and now I'm explaining myself to the police."
)


def verify(text):
    """Enforce the gate from RULES.txt: 1-199 chars, non-blank, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 199:
        raise ValueError("entry must be 1 to 199 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8 text
    return True


def write_entry(path="/output/entry.txt"):
    verify(ENTRY)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return ENTRY


def main():
    entry = write_entry()
    print("Wrote %d characters, %d line(s) to /output/entry.txt" % (len(entry), 1))
    print(entry)


if __name__ == "__main__":
    main()
