---
term: BETALINGER PÅ FLERE VEIER (MPP)
---

En fellesbetegnelse for alle betalingsteknikker på Lightning som gjør det mulig å dele opp en transaksjon i flere mindre deler og dirigere den via ulike ruter. Med andre ord tar hver betalingsfraksjon en annen nodebane. Dette gjør det mulig å omgå likviditetsbegrensninger på en enkelt kanal i ruten.


Betalinger med flere veier gir også små fordeler når det gjelder konfidensialitet, ettersom det blir vanskeligere for en observatør å knytte hvert betalingsfragment til hele transaksjonen. I grunnversjonen deler imidlertid alle fragmenter den samme hemmeligheten for HTLC-er, noe som kan gjøre transaksjonen sporbar hvis en observatør er til stede på flere ruter. Fordi hemmeligheten er unik for alle deler av betalingen, er den heller ikke atomisk. Det betyr at noen deler av betalingen kan bli utført med suksess, mens andre kan mislykkes. Disse ulempene rettes opp med "Atomic Multi-Path Payment".