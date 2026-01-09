#!/usr/bin/env python3
import argparse
import secrets
import string
from pathlib import Path

PASSWORD_COUNT = 5
PASSWORD_LENGTH = 10

CHARSET = string.ascii_lowercase + string.ascii_uppercase + string.digits

DEFAULT_WORDLIST = Path("/usr/share/dict/words")

COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"

def generate_password(length: int) -> str:
    return "".join(secrets.choice(CHARSET) for _ in range(length))


def in_wordlist(password: str, wordlist_path: Path) -> bool:
    """
    Stream the wordlist line-by-line to avoid high RAM usage.
    Exact match against lines in the file.
    """
    with wordlist_path.open("r", errors="ignore") as f:
        for line in f:
            if line.rstrip("\r\n") == password:
                return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Password generator with optional local wordlist check"
    )
    parser.add_argument(
        "-n", "--count",
        type=int,
        default=PASSWORD_COUNT,
        help=f"How many passwords to generate (default: {PASSWORD_COUNT})",
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=PASSWORD_LENGTH,
        help=f"Password length (default: {PASSWORD_LENGTH})",
    )
    parser.add_argument(
        "--wordlist",
        type=str,
        default=None,
        help="Path to local wordlist for checking (optional). "
             "If omitted, tries /usr/share/dict/words.",
    )

    parser.add_argument(
    "--wl",
    action="store_true",
    help="Enable wordlist check using default wordlist (/usr/share/dict/words)",
    )


    args = parser.parse_args()

    wordlist_path = None
    if args.wordlist:
        wordlist_path = Path(args.wordlist)
    elif args.wl:
        wordlist_path = DEFAULT_WORDLIST


    if args.count <= 0:
        print("ERROR: --count must be >= 1")
        return 2
    if args.length <= 0:
        print("ERROR: --length must be >= 1")
        return 2

    if wordlist_path is not None and not wordlist_path.exists():
        print(f"ERROR: Wordlist not found: {wordlist_path}")
        print("Install a default wordlist with:")
        print("  sudo apt update && sudo apt install wamerican")
        return 2

    for _ in range(args.count):
        pw = generate_password(args.length)

        if wordlist_path is not None:
            if in_wordlist(pw, wordlist_path):
                print(f"{pw}  {COLOR_RED}[HIT in wordlist]{COLOR_RESET}")
            else:
                print(f"{pw}  {COLOR_GREEN}[OK not in wordlist]{COLOR_RESET}")
        else:
            print(pw)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

