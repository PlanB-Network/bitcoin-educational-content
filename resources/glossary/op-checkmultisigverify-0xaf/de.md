---
term: OP_CHECKMULTISIGVERIFY (0XAF)
---

Kombiniert ein `OP_CHECKMULTISIG` und ein `OP_VERIFY`. Es benötigt mehrere Signaturen und öffentliche Schlüssel, um zu verifizieren, dass `M` aus `N` Signaturen gültig sind, genau wie es `OP_CHECKMULTISIG` tut. Dann, wie bei `OP_VERIFY`, stoppt das Skript sofort mit einem Fehler, wenn die Verifizierung fehlschlägt. Wenn die Verifizierung erfolgreich ist, fährt das Skript fort, ohne irgendeinen Wert auf den Stapel zu legen. Dieser Opcode wurde in Tapscript entfernt.