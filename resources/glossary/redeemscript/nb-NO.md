---
term: REDEEMSCRIPT

---
Et skript som definerer de spesifikke betingelsene som må oppfylles for å låse opp midlene som er knyttet til en P2SH-utgang. I en P2SH UTXO inneholder `scriptPubKey` hashen til `redeemScript`. Når en transaksjon ønsker å bruke denne UTXO-en som input, må den oppgi en klar `redeemScript` som samsvarer med hashen i `scriptPubKey`. `redeemScript` oppgis dermed i `scriptSig` i input, sammen med andre elementer som er nødvendige for å oppfylle skriptets betingelser, for eksempel signaturer eller offentlige nøkler. Denne innkapslede strukturen sørger for at detaljene i utgiftsbetingelsene forblir skjult helt til bitcoinsene faktisk blir brukt. Den brukes særlig til Legacy P2SH-lommebøker med flere signaturer.