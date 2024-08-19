---
term: OP_CHECKSIG (0XAC)
---

Überprüft die Gültigkeit einer Signatur gegenüber einem gegebenen öffentlichen Schlüssel. Es nimmt die obersten zwei Elemente vom Stapel: die Signatur und den öffentlichen Schlüssel und bewertet, ob die Signatur korrekt für den Transaktionshash und den spezifizierten öffentlichen Schlüssel ist. Wenn die Überprüfung erfolgreich ist, wird der Wert `1` (wahr) auf den Stapel gelegt, andernfalls `0` (falsch). Dieser Opcode wurde in Tapscript modifiziert, um Schnorr-Signaturen zu überprüfen.