---
term: VOUT

---
Et spesifikt element i en Bitcoin-transaksjon som bestemmer destinasjonen for de sendte midlene. En transaksjon kan inneholde flere utganger, og hver av dem er unikt identifisert av en kombinasjon av transaksjonsidentifikatoren (`txid`) og en indeks kalt `vout`. Denne indeksen, som starter på `0`, markerer utgangens posisjon i sekvensen av transaksjonsutganger. Den første utdataen vil dermed bli betegnet med `"vout": 0`, den andre med `"vout": 1`, og så videre.

Hver `vout` inneholder først og fremst to typer informasjon:


- verdien, uttrykt i bitcoins, som representerer beløpet som er sendt;
- et låseskript (`scriptPubKey`) som fastsetter betingelsene som kreves for at midlene skal kunne brukes igjen i en fremtidig transaksjon.

Kombinasjonen av `txid` og `vout` for en bestemt brikke danner for eksempel det som kalles en UTXO:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```