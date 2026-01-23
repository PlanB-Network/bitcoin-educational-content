---
term: Anonsets (anonymity sets)

definition: Indikatorer som måler graden av personvern for en UTXO ved å telle antall uadskillelige UTXO-er i et sett, typisk etter en coinjoin.
---
Anonsets fungerer som indikatorer for å vurdere graden av personvern for en bestemt UTXO. Mer spesifikt måler de antallet UTXO-er som er uatskillelige innenfor mengden som inkluderer den aktuelle mynten. Siden det kreves en gruppe identiske UTXO-er, beregnes anonsets vanligvis innenfor en coinjoin-syklus. De gjør det mulig, der det er relevant, å vurdere kvaliteten på coinjoins. Et stort anonset innebærer et høyere nivå av anonymitet, ettersom det blir vanskelig å skille ut en spesifikk UTXO innenfor mengden.

Det finnes to typer anonsets: forward anonset (forward-looking metrics); og backward anonset (backward-looking metrics). Begrepet "*score*" brukes også noen ganger for å betegne anonsets.

Den første angir størrelsen på gruppen der den analyserte utgående UTXO-en skjuler seg, gitt den inngående UTXO-en. Denne indikatoren gjør det mulig å måle hvor robust myntens personvern er mot en analyse fra fortid til nåtid (fra inngang til utgang). Den andre angir antallet mulige kilder for en gitt mynt, gitt den utgående UTXO-en. Denne indikatoren gjør det mulig å måle hvor robust myntens personvern er mot en analyse fra nåtid til fortid (fra utgang til inngang).










