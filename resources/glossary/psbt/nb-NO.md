---
term: PSBT

---
Forkortelse for "Partially Signed Bitcoin Transaction". Det er en spesifikasjon som ble introdusert med BIP174 for å standardisere måten uferdige transaksjoner konstrueres på i programvare relatert til Bitcoin, som for eksempel lommebokprogramvare. En PSBT innkapsler en transaksjon der inndataene kanskje ikke er fullstendig signert. Den inneholder all nødvendig informasjon for at en deltaker skal kunne signere transaksjonen uten å kreve ytterligere data. En PSBT kan derfor ha tre ulike former:


- Transaksjonen er ferdig konstruert, men ennå ikke signert;
- En delvis signert transaksjon, der noen inndata er signert, mens andre ikke er det ennå;
- Eller en fullstendig signert Bitcoin-transaksjon, som kan konverteres slik at den er klar for kringkasting i nettverket.

PSBT-formatet legger til rette for interoperabilitet mellom ulike lommebokprogramvarer og signaturenheter (maskinvarelommebøker). For øyeblikket brukes versjon 0 av PSBT, som definert i BIP174, men versjon 2 er foreslått via BIP370.

> ► * Versjon 1 av PSBT finnes ikke. Siden versjon 0 var den første versjonen, ble den andre versjonen uformelt kalt versjon 2. Ava Chow, som har forfattet BIP370, bestemte seg derfor for å gi denne nye versjonen nummer 2 for å unngå forvirring