---
term: PSBT
---

Akronym für "Partially Signed Bitcoin Transaction" (Teilweise signierte Bitcoin-Transaktion). Es handelt sich um eine Spezifikation, die mit BIP174 eingeführt wurde, um die Art und Weise zu standardisieren, wie unvollständige Transaktionen in mit Bitcoin verwandter Software, wie Wallet-Software, konstruiert werden. Ein PSBT umfasst eine Transaktion, bei der die Eingaben möglicherweise nicht vollständig signiert sind. Es beinhaltet alle notwendigen Informationen, damit ein Teilnehmer die Transaktion signieren kann, ohne zusätzliche Daten zu benötigen. Somit kann ein PSBT drei verschiedene Formen annehmen:
* Eine vollständig konstruierte Transaktion, aber noch nicht signiert;
* Eine teilweise signierte Transaktion, bei der einige Eingaben signiert sind, während andere noch nicht signiert sind;
* Oder eine vollständig signierte Bitcoin-Transaktion, die zur Übertragung im Netzwerk bereit gemacht werden kann.

Das PSBT-Format erleichtert die Interoperabilität zwischen verschiedenen Wallet-Software und Signaturgeräten (Hardware-Wallets). Derzeit wird Version 0 des PSBT verwendet, wie in BIP174 definiert, aber Version 2 wird über BIP370 vorgeschlagen.

> ► *Version 1 des PSBT existiert nicht. Da Version 0 die erste Version war, wurde die zweite Version informell als Version 2 bezeichnet. Ava Chow, die Autorin von BIP370, entschied sich daher, dieser neuen Version die Nummer 2 zuzuweisen, um jegliche Verwirrung zu vermeiden.*