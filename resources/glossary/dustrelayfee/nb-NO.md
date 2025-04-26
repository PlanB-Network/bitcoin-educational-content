---
term: DUSTRELAYFEE

---
En standardiseringsregel som brukes av nettverksnoder for å bestemme hva de anser som "støvgrensen" Denne parameteren angir en avgiftssats i sats per virtuell kilobyte (sats/kvB) som fungerer som en referanse for å beregne om verdien av en UTXO er mindre enn de nødvendige avgiftene for å inkludere den i en transaksjon. En UTXO anses som "støv" på Bitcoin hvis den krever mer i gebyrer for å bli overført enn verdien den selv representerer. Beregningen av denne grensen er som følger:

```text
limit = (input size + output size) * fee rate
```

Ettersom avgiftssatsen som kreves for at en transaksjon skal inkluderes i en Bitcoin-blokk, varierer hele tiden, lar parameteren `DustRelayFee` hver node definere avgiftssatsen som brukes i denne beregningen. Som standard er denne verdien satt til 3 000 sats/kvB i Bitcoin Core. For eksempel, for å beregne støvgrensen for en P2PKH-inngang og -utgang, som måler henholdsvis 148 og 34 byte, vil beregningen være:

```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Dette betyr at den aktuelle noden ikke vil videresende transaksjoner som inkluderer en P2PKH-sikret UTXO med en verdi som er mindre enn 546 sats.