---
term: ASMAP
definition: Ett Bitcoin Core-verktyg som diversifierar anslutningar mellan noder enligt autonoma system (ASN) för att förhindra Eclipse-attacker.
---

Ett verktyg som uppfanns av Gleb Naumenko och som används av Bitcoin Core för att förbättra säkerheten och topologin i Bitcoin-nätverket genom att diversifiera anslutningar mellan noder. Det är en IP Address-mappning till Autonomous System Numbers (ASN), vilket möjliggör en bättre fördelning av utgående anslutningar baserat på ASN snarare än IP-prefix. Detta bidrar till att förhindra Eclipse-attacker (inklusive Erebus-attacken) genom att göra det svårare för en angripare att simulera flera noder.