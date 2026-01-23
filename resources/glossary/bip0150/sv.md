---
term: BIP0150
definition: Autentiseringsmekanism mellan noder för att stärka säkerheten och begränsa åtkomsten till vissa nodtjänster.
---

Föreslår en autentiseringsmekanism mellan peers i Bitcoin-nätverket för att förbättra säkerheten och säkerställa nodernas Ownership. Den gör det möjligt för nodoperatörer att begränsa tillgången till vissa tjänster eller bevilja dataflödesprioriteringar endast till specifika peers, genom ömsesidig autentisering för att undvika MITM-attacker (Man-In-The-Middle). Denna BIP kommer att förbli i utkaststatus, men den kommer att fungera som en lektion för BIP324 (*P2P transport V2*), som nu är valfritt implementerad i Bitcoin Core.