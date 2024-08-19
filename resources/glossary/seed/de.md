---
term: SEED
---

Im spezifischen Kontext einer hierarchisch deterministischen Bitcoin-Wallet ist ein Seed ein 512-Bit-Stück Information, das aus Zufälligkeit abgeleitet wird. Es wird verwendet, um deterministisch und hierarchisch einen Satz von privaten Schlüsseln und deren entsprechenden öffentlichen Schlüsseln für eine Bitcoin-Wallet zu generieren. Der Seed wird oft mit der Wiederherstellungsphrase selbst verwechselt. Es handelt sich jedoch um unterschiedliche Informationen. Der Seed wird durch Anwendung der `PBKDF2`-Funktion auf die mnemonische Phrase und eine mögliche Passphrase erhalten.

Der Seed wurde mit der Einführung von BIP32 erfunden, das die Grundlagen der hierarchisch deterministischen Wallet definiert. In diesem Standard war der Seed 128 Bit groß. Dies ermöglicht die Ableitung aller Schlüssel in einer Wallet von einem einzigen Informationsstück, im Gegensatz zu JBOK (*Just a Bunch Of Keys*) Wallets, die für jeden generierten Schlüssel neue Backups benötigen. BIP39 führte später eine Kodierung dieses Seeds ein, um seine Lesbarkeit durch Menschen zu vereinfachen. Diese Kodierung erfolgt in Form einer Phrase, die üblicherweise als mnemonische Phrase oder Wiederherstellungsphrase bezeichnet wird. Dieser Standard hilft, Fehler bei der Sicherung des Seeds zu vermeiden, insbesondere durch die Verwendung einer Prüfsumme.

Allgemeiner gesagt, in der Kryptographie, ist ein Seed ein Stück zufälliger Daten, das als Ausgangspunkt zur Generierung kryptographischer Schlüssel, Verschlüsselungen oder pseudo-zufälliger Sequenzen verwendet wird. Die Qualität und Sicherheit vieler kryptographischer Prozesse hängen von der Zufälligkeit und Vertraulichkeit des Seeds ab.

> ► *Die englische Übersetzung von "graine" ist "seed". Im Französischen verwenden viele direkt das englische Wort, um sich auf den Seed zu beziehen.*