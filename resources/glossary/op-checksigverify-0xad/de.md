---
term: OP_CHECKSIGVERIFY (0XAD)

---
Führt die gleiche Operation durch wie `OP_CHECKSIG`, aber wenn die Überprüfung der Signatur fehlschlägt, hält das Skript sofort mit einem Fehler an und die Transaktion ist somit ungültig. Wenn die Überprüfung erfolgreich war, fährt das Skript fort, ohne den Wert `1` (true) auf den Stack zu legen. Zusammenfassend lässt sich sagen, dass `OP_CHECKSIGVERIFY` die Operation `OP_CHECKSIG` gefolgt von `OP_VERIFY` durchführt. Dieser Opcode wurde in Tapscript geändert, um Schnorr-Signaturen zu verifizieren.