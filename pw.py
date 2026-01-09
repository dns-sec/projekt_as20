#!/usr/bin/env python3
import argparse
import secrets
import string
from pathlib import Path
import hashlib
import urllib.request
import urllib.error

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

HIBP_API_PREFIX = "https://api.pwnedpasswords.com/range/"

def sha1_hex_upper(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest().upper()

def hibp_pwned_count(password: str, timeout: float = 5.0) -> int:
    """
    Returns the number of times a password appears in HIBP Pwned Passwords.
    Uses k-anonymity: only the first 5 chars of SHA1 are sent.
    Returns:
      - 0 if not found
      - >0 if found (pwned count)
    Raises urllib.error.URLError on network errors.
    """
    sha1 = sha1_hex_upper(password)
    prefix, suffix = sha1[:5], sha1[5:]

    req = urllib.request.Request(
        HIBP_API_PREFIX + prefix,
        headers={
            "User-Agent": "projekt_as20-password-tool",
            "Add-Padding": "true",  # optional privacy enhancement
        },
    )

    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read().decode("utf-8", errors="replace")

    for line in body.splitlines():
        # format: SUFFIX:COUNT
        try:
            sfx, cnt = line.split(":")
        except ValueError:
            continue
        if sfx.strip().upper() == suffix:
            try:
                return int(cnt.strip())
            except ValueError:
                return 1
    return 0

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

    parser.add_argument(
    "--hibp",
    action="store_true",
    help="Check generated passwords against Have I Been Pwned (k-anonymity).",
    )

    parser.add_argument(
    "--hibp-timeout",
    type=float,
    default=5.0,
    help="Timeout for HIBP requests in seconds (default: 5).",
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

        tags = []

        # Local wordlist tag
        if wordlist_path is not None:
            if in_wordlist(pw, wordlist_path):
                tags.append(f"{COLOR_RED}[HIT local]{COLOR_RESET}")
            else:
                tags.append(f"{COLOR_GREEN}[OK local]{COLOR_RESET}")

        # HIBP tag
        if args.hibp:
            try:
                count = hibp_pwned_count(pw, timeout=args.hibp_timeout)
                if count > 0:
                    tags.append(f"{COLOR_RED}[HIBP HIT: {count}]{COLOR_RESET}")
                else:
                    tags.append(f"{COLOR_GREEN}[HIBP OK]{COLOR_RESET}")
            except urllib.error.URLError:
                tags.append(f"{COLOR_RED}[HIBP ERROR]{COLOR_RESET}")

        if tags:
            print(pw, " ".join(tags))
        else:
            print(pw)


    return 0

if __name__ == "__main__":
    raise SystemExit(main())
