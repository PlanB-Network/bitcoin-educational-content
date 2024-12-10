---
name: BIP39 Passphrase
description: Verständnis darüber, wie eine Passphrase funktioniert
---
![cover](assets/cover.webp)

## Was ist eine BIP39 Passphrase?

HD Wallets werden typischerweise aus einer mnemonischen Phrase generiert, die aus 12 oder 24 Wörtern besteht. Diese Phrase ist sehr wichtig, da sie die Wiederherstellung aller Schlüssel eines Wallets ermöglicht, falls dessen physisches Medium (wie zum Beispiel ein Hardware-Wallet) verloren geht. Allerdings stellt sie einen einzigen Ausfallpunkt dar, denn wenn sie kompromittiert wird, könnte ein Angreifer alle Bitcoins stehlen.

![PASSPHRASE BIP39](assets/notext/01.webp)

Hier kommt die Passphrase ins Spiel. Es handelt sich um ein optionales Passwort, das Sie frei wählen können, welches zum mnemonischen Phrase im Schlüsselableitungsprozess hinzugefügt wird, um die Sicherheit des Wallets zu erhöhen.

![PASSPHRASE BIP39](assets/notext/02.webp)

Achten Sie darauf, die Passphrase nicht mit dem PIN-Code Ihres Hardware-Wallets oder dem Passwort zu verwechseln, das verwendet wird, um den Zugang zu Ihrem Wallet auf Ihrem Computer freizuschalten. Im Gegensatz zu all diesen Elementen spielt die Passphrase eine Rolle in der Ableitung der Schlüssel Ihres Wallets. **Das bedeutet, dass Sie ohne sie niemals in der Lage sein werden, Ihre Bitcoins wiederherzustellen.**

Die Passphrase arbeitet zusammen mit der mnemonischen Phrase und verändert den Seed, aus dem die Schlüssel generiert werden. So kann selbst, wenn jemand Ihre 12- oder 24-Wort-Phrase erhält, ohne die Passphrase nicht auf Ihre Mittel zugreifen. **Die Verwendung einer Passphrase erstellt im Wesentlichen ein neues Wallet mit unterschiedlichen Schlüsseln. Eine Modifikation (selbst eine geringfügige) der Passphrase wird ein anderes Wallet generieren.**

## Warum sollten Sie eine Passphrase verwenden?

Die Passphrase ist willkürlich und kann jede vom Benutzer gewählte Kombination von Zeichen sein. Die Verwendung einer Passphrase bietet daher mehrere Vorteile. Zunächst reduziert sie alle Risiken, die mit dem Kompromittieren der mnemonischen Phrase verbunden sind, indem sie einen zweiten Faktor zur Zugangskontrolle der Mittel erfordert (Einbruch, Zugang zu Ihrem Zuhause usw.).

Weiterhin kann sie strategisch verwendet werden, um ein Köder-Wallet zu erstellen, um mit physischen Zwängen umzugehen, die darauf abzielen, Ihre Mittel zu stehlen, wie der berüchtigte "*$5 Schraubenschlüssel-Angriff*". In diesem Szenario besteht die Idee darin, ein Wallet ohne Passphrase zu haben, das nur eine kleine Menge an Bitcoins enthält, genug, um einen potenziellen Aggressor zufriedenzustellen, während man ein verstecktes Wallet hat. Dieses letztere verwendet dieselbe mnemonische Phrase, ist aber mit einer zusätzlichen Passphrase gesichert.

Schließlich ist die Verwendung einer Passphrase interessant, wenn man die Zufälligkeit der Seed-Generierung des HD Wallets kontrollieren möchte.

## Wie wählt man eine gute Passphrase aus?
Damit die Passphrase wirksam ist, muss sie ausreichend lang und zufällig sein. Genau wie bei einem starken Passwort empfehle ich, eine Passphrase zu wählen, die so lang und zufällig wie möglich ist, mit einer Vielzahl von Buchstaben, Zahlen und Symbolen, um jeden Brute-Force-Angriff unmöglich zu machen.

Es ist auch wichtig, diese Passphrase richtig zu speichern, genauso wie die mnemonische Phrase. **Ihr Verlust bedeutet den Verlust des Zugangs zu Ihren Bitcoins**. Ich rate dringend davon ab, sie ausschließlich im Kopf zu behalten, da dies das Risiko eines Verlusts unangemessen erhöht. Das Ideal ist, sie auf einem physischen Medium (Papier oder Metall) getrennt von der mnemonischen Phrase niederzuschreiben. Dieses Backup muss offensichtlich an einem anderen Ort aufbewahrt werden, als Ihre mnemonische Phrase, um zu verhindern, dass beide gleichzeitig kompromittiert werden.

## Tutorials

Um eine Passphrase auf einem Ledger-Gerät (Stax, Flex oder Nano) einzurichten, können Sie dieses Tutorial konsultieren:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49