---
term: Vergrendeling (.lock)
definition: Bestand dat voorkomt dat meerdere instanties van Bitcoin Core tegelijkertijd toegang krijgen tot dezelfde map.
---

Bestand gebruikt in Bitcoin core voor het vergrendelen van de datamap. Het wordt aangemaakt wanneer bitcoind of Bitcoin-qt start om te voorkomen dat meerdere instanties van de software tegelijkertijd toegang hebben tot dezelfde datamap. Het doel is om conflicten en data corruptie te voorkomen. Als de software onverwacht stopt, kan het .lock bestand achterblijven en moet het handmatig worden verwijderd, voordat Bitcoin core opnieuw wordt gestart.