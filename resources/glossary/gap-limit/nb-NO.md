---
term: GAP LIMIT

---
En parameter som brukes i Bitcoin-lommebokprogramvare for å bestemme det maksimale antallet ubrukte adresser som skal genereres før søket etter flere transaksjoner stoppes. Det er ofte nødvendig å justere denne parameteren ved gjenoppretting av en lommebok for å sikre at alle transaksjoner blir funnet. En utilstrekkelig Gap Limit kan føre til at noen transaksjoner ikke blir funnet hvis adresser ble hoppet over under avledningsfasene. Ved å øke Gap Limit kan lommeboken søke videre i adressesekvensen for å gjenopprette alle tilknyttede transaksjoner.

En enkelt `xpub` kan i teorien utlede mer enn 4 milliarder mottakeradresser (både interne og eksterne adresser). Lommebokprogramvare kan imidlertid ikke utlede og sjekke alle disse for bruk uten å pådra seg enorme driftskostnader. Derfor går de frem i indeksrekkefølge, siden det normalt er i denne rekkefølgen all lommebokprogramvare genererer adresser. Programvaren registrerer hver brukte adresse før den går videre til neste, og den stopper søket når den støter på et antall tomme adresser etter hverandre. Dette antallet kalles gap-grensen.

Hvis for eksempel Gap Limit er satt til `20`, og adressen `m/84'/0'/0'/0'/0/15/` er tom, vil lommeboken utlede adresser opp til `m/84'/0'/0'/0'/0/34/`. Hvis dette adresseområdet forblir ubrukt, stopper søket der. En transaksjon som bruker adressen `m/84'/0'/0'/0'/0/40/` vil derfor ikke bli oppdaget i dette eksempelet.