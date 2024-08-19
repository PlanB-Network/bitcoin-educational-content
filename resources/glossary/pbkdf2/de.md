---
term: PBKDF2
---

`PBKDF2` steht für *Password-Based Key Derivation Function 2*. Es handelt sich um eine Methode zur Erstellung kryptografischer Schlüssel aus einem Passwort mittels einer Ableitungsfunktion. Sie nimmt als Eingabe ein Passwort, ein kryptografisches Salt und wendet iterativ eine vorher festgelegte Funktion (oft eine Hash-Funktion wie `SHA256` oder ein `HMAC`) auf diese Daten an. Dieser Prozess wird viele Male wiederholt, um einen kryptografischen Schlüssel zu generieren.

Im Kontext von Bitcoin wird `PBKDF2` in Verbindung mit der Funktion `HMAC-SHA512` verwendet, um den Seed einer deterministischen und hierarchischen Wallet (Seed) aus einer Wiederherstellungsphrase von 12 oder 24 Wörtern zu erstellen. Das in diesem Fall verwendete kryptografische Salt ist die BIP39-Passphrase, und die Anzahl der Iterationen beträgt `2048`.