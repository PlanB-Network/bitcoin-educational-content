---
term: SEED

---
Im spezifischen Kontext einer hierarchisch-deterministischen Bitcoin-Wallet ist ein Seed eine 512-Bit-Information, die aus dem Zufallsprinzip abgeleitet ist. Er wird verwendet, um deterministisch und hierarchisch einen Satz privater Schlüssel und die entsprechenden öffentlichen Schlüssel für eine Bitcoin-Wallet zu erzeugen. Der Seed wird oft mit der Recovery Phrase selbst verwechselt. Es handelt sich jedoch um unterschiedliche Informationen. Der Seed wird durch Anwendung der Funktion `PBKDF2` auf die mnemonische Phrase und jede potentielle Passphrase erhalten.

Der Seed wurde mit der Einführung von BIP32 erfunden, das die Grundlagen der hierarchischen deterministischen Brieftasche definiert. In diesem Standard betrug der Seed 128 Bit. Dies ermöglicht die Ableitung aller Schlüssel in einer Geldbörse aus einer einzigen Information, im Gegensatz zu JBOK (*Just a Bunch of Keys*) Geldbörsen, die für jeden erzeugten Schlüssel neue Sicherungen erfordern. BIP39 führte später eine Kodierung dieses Seeds ein, um seine Lesbarkeit für Menschen zu vereinfachen. Diese Kodierung erfolgt in Form einer Phrase, die gemeinhin als mnemonische Phrase oder Wiederherstellungsphrase bezeichnet wird. Dieser Standard hilft, Fehler bei der Sicherung des Seeds zu vermeiden, insbesondere durch die Verwendung einer Prüfsumme.

Allgemeiner ausgedrückt ist ein Seed in der Kryptografie ein Stück Zufallsdaten, das als Ausgangspunkt für die Erzeugung von kryptografischen Schlüsseln, Verschlüsselungen oder Pseudozufallssequenzen dient. Die Qualität und Sicherheit vieler kryptografischer Verfahren hängt von der Zufälligkeit und Vertraulichkeit des Seeds ab.

> ► *Die englische Übersetzung von "graine" ist "Samen". Im Französischen verwenden viele direkt das englische Wort, um sich auf den Samen zu beziehen