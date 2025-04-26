---
term: OP_CHECKSIGADD (0XBA)

---
Extrahiert die obersten drei Werte aus dem Stack: einen "öffentlichen Schlüssel", eine "CScriptNum" "n" und eine "Signatur". Wenn die Signatur nicht der leere Vektor und ungültig ist, bricht das Skript mit einem Fehler ab. Wenn die Signatur gültig ist oder der leere Vektor ist (`OP_0`), werden zwei Szenarien dargestellt:


- Wenn die Signatur der leere Vektor ist: eine `CScriptNum` mit dem Wert von `n` wird auf den Stack geschoben und die Ausführung wird fortgesetzt;
- Wenn die Signatur nicht der leere Vektor ist und gültig bleibt: eine `CScriptNum` mit dem Wert von `n + 1` wird auf den Stack geschoben, und die Ausführung wird fortgesetzt.

Zur Vereinfachung führt `OP_CHECKSIGADD` eine ähnliche Operation wie `OP_CHECKSIG` durch, aber anstatt true oder false auf den Stack zu schieben, addiert es `1` zum zweiten Wert oben auf dem Stack, wenn die Signatur gültig ist, oder lässt diesen Wert unverändert, wenn die Signatur den leeren Vektor darstellt. mit `OP_CHECKSIGADD` können in Tapscript die gleichen Multisignatur-Richtlinien wie mit `OP_CHECKMULTISIG` und `OP_CHECKMULTISIGVERIFY` erstellt werden, jedoch in einer stapelverifizierbaren Art und Weise, was bedeutet, dass der Nachschlageprozess bei der Verifizierung einer traditionellen Multisignatur entfällt und somit die Verifizierung beschleunigt wird, während die CPUs der Knoten entlastet werden. Dieser Opcode wurde in Tapscript ausschließlich für die Bedürfnisse von Taproot hinzugefügt.