---
term: BIP21

---
Forslag skrevet av Nils Schneider og Matt Corallo, basert på BIP20 skrevet av Luke Dashjr, som i sin tur kom fra et annet dokument skrevet av Nils Schneider. BIP21 definerer hvordan mottaksadresser skal kodes i URI-er (*Uniform Resource Identifier*) for å lette betalinger. For eksempel vil en Bitcoin URI som følger BIP21 der jeg ber om å få tilsendt 0,1 BTC under etiketten "*Pandul*" se slik ut:

```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```

Denne standardiseringen forbedrer brukeropplevelsen av Bitcoin-transaksjoner ved å gjøre det mulig å klikke på en lenke eller skanne en QR-kode for å sette i gang parameterne. BIP21-standarden er nå tatt i bruk i programvare for Bitcoin-lommebøker.