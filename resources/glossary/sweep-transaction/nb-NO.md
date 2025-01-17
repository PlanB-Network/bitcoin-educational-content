---
term: SWEEP-TRANSAKSJON

---
Mønster- eller transaksjonsmodell som brukes i kjedeanalyse for å bestemme transaksjonens art. Denne modellen kjennetegnes av forbruk av en enkelt UTXO som input og produksjon av en enkelt UTXO som output. Tolkningen av denne modellen er at vi er i nærvær av en selvoverføring. Brukeren har overført bitcoinsene sine til seg selv, til en annen adresse han eller hun eier. Siden det ikke er noen endring i transaksjonen, er det svært usannsynlig at vi har å gjøre med en betaling. Når en betaling foretas, er det nesten umulig for betaleren å ha en UTXO som nøyaktig samsvarer med beløpet som kreves av selgeren, i tillegg til transaksjonsgebyrene. Som regel er betaleren derfor tvunget til å produsere en endringsutgang. Vi vet da at den observerte brukeren sannsynligvis fortsatt er i besittelse av denne UTXO-en. I forbindelse med en kjedeanalyse, hvis vi vet at UTXO-en som ble brukt som input i transaksjonen tilhører Alice, kan vi anta at UTXO-en i output også tilhører henne.

![](../../dictionnaire/assets/6.webp)

> på fransk kan "sweep transaction" oversettes med "transaksjon de balayage"