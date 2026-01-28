---
term: OP_CHECKSIG (0XAC)

definition: Opcode, der die Gültigkeit einer Signatur im Vergleich zu einem öffentlichen Schlüssel prüft.
---
Überprüft die Gültigkeit einer Signatur anhand eines bestimmten öffentlichen Schlüssels. Sie nimmt die beiden obersten Elemente des Stapels: die Signatur und den öffentlichen Schlüssel, und bewertet, ob die Signatur für den Transaktionshash und den angegebenen öffentlichen Schlüssel korrekt ist. Wenn die Überprüfung erfolgreich ist, wird der Wert "1" (wahr) auf den Stapel gelegt, andernfalls "0" (falsch). Dieser Opcode wurde in Tapscript geändert, um Schnorr-Signaturen zu verifizieren.