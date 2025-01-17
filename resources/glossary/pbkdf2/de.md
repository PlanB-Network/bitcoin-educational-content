---
term: PBKDF2

---
pBKDF2" steht für *Password-Based Key Derivation Function 2*. Es handelt sich um eine Methode zur Erzeugung kryptografischer Schlüssel aus einem Passwort unter Verwendung einer Ableitungsfunktion. Sie nimmt als Eingabe ein Passwort und ein kryptografisches Salz und wendet iterativ eine vorbestimmte Funktion (oft eine Hash-Funktion wie `SHA256` oder `HMAC`) auf diese Daten an. Dieser Vorgang wird viele Male wiederholt, um einen kryptografischen Schlüssel zu erzeugen.

Im Zusammenhang mit Bitcoin wird `PBKDF2` in Verbindung mit der Funktion `HMAC-SHA512` verwendet, um den Seed einer deterministischen und hierarchischen Wallet (Seed) aus einer Recovery-Phrase von 12 oder 24 Wörtern zu erstellen. Das in diesem Fall verwendete kryptografische Salz ist die BIP39-Passphrase, und die Anzahl der Iterationen beträgt "2048".