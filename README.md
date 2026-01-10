<h1 align="center">🛡️ Secure Password Generator 🛡️</h1>

<div align="center">

A Python-based tool to generate secure passwords and check them against local and/or remote word lists to discover potential weak outputs.  

The thought behind this is to create simple, yet secure, passwords so as to make them easy to memorize.  

This way you can combine them into much longer sequences, and add special characters where convenient, while still keeping them locked tight in your head.
  
</div>

## ⭐ Functions

- Generates random passwords with `secrets`

- Support for custom number and length

- Support for optional check against word lists

- 🛡️ Uses SHA-1 for k-anonymity when checking with HIBP (the passwords never leave your terminal)

- 🛡️ NO storing or logging of passwords except in YOUR terminal history
   - To clear Bash: `history -c && history -w && clear`
   - To clear Pwsh: `Remove-Item (Get-PSReadLineOption).HistorySavePath`

## ⚙️ Usage

Generate 5 passwords with 10 characters (default):
`./pw.py`

Adjust (-n)umber and (-l)ength:
`./pw.py -n <Number of PWs> -l <Length of PWs>`

Check against default word list:
`./pw.py --wl`

Check against custom word list:
`./pw.py --wordlist /path/to/wordlist.txt`

Check against Have I Been Pwned (HIBP) (Requires internet connection):
`./pw.py --hibp`

Example usage:
`./pw.py -n 10 -l 10 --wl --hibp`

## 📄 Documentation

Further documentation can be found in `docs/`:

- `docs/overview.md` – Project overview.
- `docs/usage.md` – Usage.
- `docs/design.md` – Design and safety.

## ⚠️ Requirements

- Python 3.8+
- Word list(s), e.g. `wamerican` with `sudo apt update && sudo apt install wamerican` (this one is required to run --wl)
