---
term: UNIX AEG
---

Unix Aeg ehk Unix Ajatempel tähistab sekundite arvu, mis on möödunud alates 1. jaanuarist 1970 kell 00:00 UTC (Unix Epohh). Seda süsteemi kasutatakse Unixi operatsioonisüsteemides ja nende tuletistes aja märkimiseks universaalsel ja standardiseeritud viisil. See võimaldab kellade sünkroniseerimist ja ajapõhiste sündmuste haldamist, sõltumata ajavöönditest.

Bitcoini kontekstis kasutatakse seda sõlmede kohaliku kella jaoks ja seega NAT-i (Network-Adjusted Time ehk Võrgu Kohandatud Aeg) arvutamiseks. Võrgu kohandatud aeg on sõlmede poolt kohalikult arvutatud sõlmeaegade mediaan, ja seda viidet kasutatakse seejärel ploki ajatemplite kehtivuse kontrollimiseks. Tõepoolest, et sõlm ploki aktsepteeriks, peab selle ajatempel olema MTP (Median Time Past ehk viimase 11 kaevandatud ploki mediaanaeg) ja NAT pluss 2 tundi vahel:

```text
MTP < Kehtiv Ajatempel < (NAT + 2h)
```

Unix Aega kasutatakse ka ajalukkude seadmisel, kui need põhinevad reaalsel ajal, mitte plokkide arvul.