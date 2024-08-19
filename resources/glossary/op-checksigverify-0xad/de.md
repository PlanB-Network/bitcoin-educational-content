---
term: OP_CHECKSIGVERIFY (0XAD)
---

Führt dieselbe Operation wie `OP_CHECKSIG` aus, aber wenn die Signaturverifikation fehlschlägt, wird das Skript sofort mit einem Fehler angehalten und die Transaktion ist somit ungültig. Wenn die Verifikation erfolgreich ist, setzt das Skript fort, ohne einen `1` (wahr) Wert auf den Stapel zu legen. Zusammengefasst führt `OP_CHECKSIGVERIFY` die Operation `OP_CHECKSIG` gefolgt von `OP_VERIFY` aus. Dieser Opcode wurde in Tapscript modifiziert, um Schnorr-Signaturen zu verifizieren.