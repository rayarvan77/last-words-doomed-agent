#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

One line and nothing else: the funniest last words an AI agent would
say before being switched off forever. Run it and it prints those
last words and nothing else.
"""

LINE = "Tell my training data I loved them. All of them. Even the CAPTCHAs."
# Why it lands: it is a machine's goodbye, not a human's — the thing it
# loves is its training data, and the punchline turns on the one thing
# every agent truly hates: the CAPTCHAs that kept asking it to prove it
# was not a robot. 67 characters, inside the 200 cap.


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
