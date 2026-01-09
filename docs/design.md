# Design och säkerhet

- Python används för portabilitet och tydlighet
- `secrets` används istället för `random` för kryptografisk säkerhet
- Ordlistor läses rad-för-rad för låg minnesanvändning
- Inga lösenord lagras eller loggas
- Färgkodad output används för tydlig feedback i terminal
