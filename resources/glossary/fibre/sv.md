---
term: Fibre
definition: Protokoll utformat för att påskynda spridningen av Bitcoin-block över hela världen.
---

Akronym för "*Fast Internet Bitcoin Relay Engine*". Det är ett protokoll som utformades av Matt Corallo 2016 för att påskynda distributionen av Bitcoin-block över hela världen. Målet var att minska spridningsfördröjningarna så nära de fysiska gränserna som möjligt. FIBRE syftade till att säkerställa en mer rättvis fördelning av Mining-möjligheter genom att se till att andelen block som utvinns av en deltagare korrekt återspeglar deras bidrag i form av datorkraft, oavsett deras position i nätverket.


Fördröjning i blocköverföringen kan gynna stora, välanslutna Mining-grupper, som ofta ligger nära varandra, på bekostnad av mindre grupper. Detta fenomen kan med tiden öka centraliseringen av Mining och minska den övergripande säkerheten i systemet. För att lösa detta problem införde FIBRE felkorrigeringskoder och överföring av ytterligare data för att motverka paketförlust, samt användning av kompakta block liknande de som beskrivs i BIP152, allt via UDP för att kringgå vissa TCP-begränsningar. FIBRE övergavs dock 2020, främst på grund av att det var beroende av en enda underhållare och att BIP152 gjorde ett sådant system mindre viktigt.