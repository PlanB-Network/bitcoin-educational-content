---
term: BIP0012
definition: Förslag som introducerar opkoden OP_EVAL för kapslade skript, ersatt av BIP16 (P2SH) av säkerhetsskäl.
---

Förslag av Gavin Andresen för att förbättra flexibiliteten och integriteten i Bitcoin-transaktionsskript. Denna BIP föreslår att man implementerar en ny opcode för skript, kallad `OP_EVAL`, som gör det möjligt att utvärdera ett skript som finns i data från en `scriptSig` under transaktionsvalideringsprocessen. Den viktigaste ändringen i BIP12 är att det blir möjligt att inkludera ett skript inuti ett annat skript. Denna teknik gör det möjligt att skapa mer komplexa villkor som kan verifieras vid tidpunkten för utgifterna, utan att behöva avslöja dem för användare som skickar bitcoins till den använda Address. BIP12 ersattes senare av säkrare förslag, särskilt BIP16 (P2SH), som erbjuder en annan metod för att uppnå samma mål som `OP_EVAL`.