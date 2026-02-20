---
term: OP_CHECKMULTISIGVERIFY (0XAF)

definition: Kombiniert OP_CHECKMULTISIG und OP_VERIFY und stoppt das Skript, wenn die Verifizierung fehlschlägt.
---
Kombiniert ein `OP_CHECKMULTISIG` und ein `OP_VERIFY`. Es nimmt mehrere Unterschriften und öffentliche Schlüssel, um zu überprüfen, ob `M` von `N` Unterschriften gültig sind, genau wie `OP_CHECKMULTISIG`. Wenn die Überprüfung fehlschlägt, bricht das Skript wie bei `OP_VERIFY` sofort mit einer Fehlermeldung ab. Wenn die Überprüfung erfolgreich ist, fährt das Skript fort, ohne einen Wert auf den Stack zu schieben. Dieser Opcode wurde in Tapscript entfernt.