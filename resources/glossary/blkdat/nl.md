---
term: Blk*.dat
definition: Bestanden in Bitcoin Core die ruwe data van blockchain-blokken opslaan.
---

Naam van de bestanden in Bitcoin core die de ruwe blokgegevens van de Blockchain opslaan. Elk bestand wordt geïdentificeerd door een uniek nummer in de naam. De blokken worden dus in chronologische volgorde opgeslagen, te beginnen met het bestand blk00000.dat. Wanneer dit bestand zijn maximale capaciteit bereikt, worden de volgende blokken opgenomen in blk00001.dat, dan blk00002.dat, enzovoort. Elk blk-bestand heeft een maximale capaciteit van 128 mebibytes (MiB), wat overeenkomt met iets meer dan 134 megabytes (MB). Deze bestanden zijn verplaatst naar de `/blocks` map sinds versie 0.8.0.