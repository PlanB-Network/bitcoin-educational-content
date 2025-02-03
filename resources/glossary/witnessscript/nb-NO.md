---
term: WITNESSSCRIPT

---
Et skript som spesifiserer betingelsene for at bitcoins kan brukes fra P2WSH- eller P2SH-P2WSH UTXO-er. Vanligvis bestemmer `witnessScript` betingelsene for en multisignaturlommebok under SegWit-standarden. I disse skriptstandardene inneholder `scriptPubKey` av UTXO-en (utdataene) en hash av `witnessScript`. For å bruke denne UTXO-en som input i en ny transaksjon, må innehaveren avsløre den opprinnelige `witnessScript`, for å bevise at den stemmer overens med fingeravtrykket i `scriptPubKey`. Deretter må `witnessScript` inkluderes i transaksjonens `scriptWitness`, som også inneholder de elementene som er nødvendige for å validere skriptet, for eksempel signaturer. Derfor tilsvarer `witnessScript` for SegWit `redeemScript` i en P2SH-transaksjon, med den forskjellen at det er plassert i transaksjonens vitne, og ikke i `scriptSig`.

> ► *Varsom: `witnessScript` må ikke forveksles med `scriptWitness`. Mens `witnessScript` definerer utgiftsbetingelsene for en P2WSH- eller P2SH-P2WSH UTXO og utgjør et skript i seg selv, inneholder `scriptWitness` vitnedataene for alle SegWit-inndata*