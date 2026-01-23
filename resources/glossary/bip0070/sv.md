---
term: BIP0070
definition: Interaktivt betalningsprotokoll som använder betalningsbegäranden signerade med SSL-certifikat. Blev aldrig allmänt antaget.
---

Interaktivt betalningsprotokoll för Bitcoin. Det gör det möjligt att skicka betalningsbegäran och att ta emot betalningar på ett säkert och standardiserat sätt. I det här protokollet klickar klienten på en Bitcoin URI (BIP21) som utökats med en ytterligare parameter (beskrivs i BIP72). Betalningsbegäran signeras med handlarens SSL-certifikat. Efter mottagande och validering av denna begäran fylls betalningsuppgifterna automatiskt i i klientens Wallet-transaktion Interface. Detta protokoll ger betalningsbekräftelse och förbättrar säkerheten och användarupplevelsen genom att klargöra betalningens mottagande enhet. Denna metod som föreslås i BIP70 har aldrig använts av handlare i någon större utsträckning.