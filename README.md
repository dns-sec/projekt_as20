<h1 align="center">🔐 Projekt – Säker lösenordsgenerator</h1>

Ett Python-baserat verktyg för att generera kryptografiskt säkra lösenord och
kontrollera dem mot lokala ordlistor för att upptäcka svaga lösenord.

## Funktioner

- Genererar slumpmässiga lösenord med `secrets`
- Stöd för valfritt antal och längd
- Valfri kontroll mot lokal wordlist
- Färgkodad terminalutmatning (OK / HIT)
- Ingen lagring eller loggning av lösenord

## Användning

Generera 5 lösenord (10 tecken):
`./src/password_tool.py`

Anpassa antal och längd:
`./src/password_tool.py -n <antal_pw> -l <antal_tecken>`

Aktivera kontroll av default wordlist:
`./src/password_tool.py --wl`

Använd egen wordlist:
`./src/password_tool.py --wordlist /path/till/wordlist.txt`

## Dokumentation

Mer detaljerad dokumentation finns i `docs/`:

- `docs/overview.md` – projektöversikt
- `docs/usage.md` – användning
- `docs/design.md` – design och säkerhet

## Krav

- Python 3.8+
- Wordlist-paket, t.ex. `wamerican` med `sudo apt update && sudo apt install wamerican`
