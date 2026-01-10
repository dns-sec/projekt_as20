<h1 align="center">🛡️ Secure Password Generator 🛡️</h1>

<div align="center">

A Python3-based tool to generate secure passwords and check them against local and/or remote wordlists to discover potential weak outputs.  

The thought behind this is to create simple, yet secure, passwords so as to make them easy to memorize.  

This way you can combine them into much longer sequences, and add special characters where convenient, while still being able to memorize them.
  
</div>

## ⭐ Functions

- Generates random passwords with `secrets`

- Supports checking against custom wordlists

- Automatically checks against 3 (three) included standardized wordlists

- Uses SHA-1 for k-anonymity when checking with HIBP (the passwords never leave your terminal)

- NO storing or logging of passwords except in YOUR terminal history
   - To remove terminal history on Linux: `history -c && history -w && clear`
   - To remove terminal history on Windows: `Remove-Item (Get-PSReadLineOption).HistorySavePath`

## ⚙️ How-To-Use

1. Install Python 3 if you haven't already, get it at https://www.python.org/downloads/

2. Open the `projekt_as20` folder in your terminal of choice

3. Run `python3 pw.py`
   - Run `python3 pw.py -h` to see all options

## 📄 Documentation

Below you can see a side-by-side of the script running on both Windows and Debian

<p align="center">
  <img src="screenshots/demo.png" alt="Demo screenshot">
</p>

Documentation can also be found in `docs/`:

- `docs/overview.md` – Project overview.
- `docs/usage.md` – Usage.
- `docs/design.md` – Design and thinking.

Enjoy
