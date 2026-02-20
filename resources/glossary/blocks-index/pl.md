---
term: Indeks bloków
definition: Struktura LevelDB w Bitcoin Core katalogująca metadane i lokalizacje bloków.
---

Struktura danych LevelDB w Bitcoin Core, która kataloguje metadane o wszystkich blokach. Każdy wpis w tym indeksie zawiera szczegóły, takie jak identyfikator bloku, jego wysokość w Blockchain, wskaźnik do bloku w bazie danych i inne metadane. To indeksowanie pozwala na szybkie wyszukanie bloku przechowywanego w pamięci.