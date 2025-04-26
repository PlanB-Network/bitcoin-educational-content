---
term: ENKEL BETALING

---
Transaksjonsmønster (eller modell) som brukes i kjedeanalyse, kjennetegnet ved forbruk av en eller flere UTXO-er i input og produksjon av 2 UTXO-er i output. Denne modellen vil derfor se slik ut:

![](../../dictionnaire/assets/5.webp)

Denne enkle betalingsmodellen indikerer at vi sannsynligvis er i nærvær av en sende- eller betalingstransaksjon. Brukeren har brukt sin egen UTXO i inndata for å tilfredsstille en UTXO for betaling og en UTXO for veksling (veksling som returneres til samme bruker) i utdata. Vi vet derfor at den observerte brukeren sannsynligvis ikke lenger er i besittelse av én av de to UTXO-ene i utdata (betalings UTXO-en), men at han eller hun fortsatt er i besittelse av den andre UTXO-en (endrings UTXO-en).