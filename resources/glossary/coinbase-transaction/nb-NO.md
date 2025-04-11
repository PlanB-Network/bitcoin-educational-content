---
term: COINBASE (TRANSAKSJON)

---
Coinbase-transaksjonen er en spesiell og unik transaksjon som er inkludert i hver blokk i Bitcoin-blokkjeden. Den representerer den første transaksjonen i en blokk og opprettes av utvinneren som har funnet en header som validerer arbeidsbeviset (*Proof-of-Work*), det vil si mindre enn eller lik målet.

Coinbase-transaksjonen tjener primært to formål: å tildele blokkbelønningen til utvinneren og å tilføre nye enheter bitcoins til den sirkulerende pengemengden. Blokkbelønningen, som er det økonomiske insentivet for utvinnere til å engasjere seg i proof of work, inkluderer de akkumulerte gebyrene for transaksjonene som inngår i blokken, og en bestemt mengde nyopprettede bitcoins ex-nihilo (blokksubsidie). Dette beløpet, som opprinnelig ble satt til 50 bitcoins per blokk i 2009, halveres hver 210 000. blokk (omtrent hvert fjerde år) under en hendelse som kalles "halvering"

Coinbase-transaksjonen skiller seg fra vanlige transaksjoner på flere måter. For det første har den ingen input, noe som betyr at den ikke bruker eksisterende transaksjonsoutput (UTXO). Deretter inneholder signaturskriptet (`scriptSig`) for coinbase-transaksjonen vanligvis et vilkårlig felt som gjør det mulig å innlemme tilleggsdata, for eksempel egendefinerte meldinger eller informasjon om versjon av utvinningsprogramvare. Til slutt er bitcoins generert av coinbase-transaksjonen underlagt en forfallsperiode på 100 blokker (101 bekreftelser) før de kan brukes, for å forhindre potensiell bruk av ikke-eksisterende bitcoins i tilfelle en omorganisering av kjeden.

> det finnes ingen oversettelse for "Coinbase" på fransk. Derfor er det akseptert å bruke dette begrepet direkte*