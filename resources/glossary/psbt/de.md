---
term: PSBT

---
Akronym für "Partially Signed Bitcoin Transaction". Es ist eine Spezifikation, die mit BIP174 eingeführt wurde, um die Art und Weise zu standardisieren, in der unfertige Transaktionen in Software im Zusammenhang mit Bitcoin, wie z.B. Wallet-Software, konstruiert werden. Eine PSBT kapselt eine Transaktion, bei der die Eingaben möglicherweise nicht vollständig signiert sind. Er enthält alle notwendigen Informationen, die ein Teilnehmer benötigt, um die Transaktion zu signieren, ohne dass zusätzliche Daten erforderlich sind. Somit kann ein PSBT 3 verschiedene Formen annehmen:


- Eine vollständig ausgearbeitete, aber noch nicht unterzeichnete Transaktion;
- Eine teilweise signierte Transaktion, bei der einige Eingaben signiert sind, während andere noch nicht signiert sind;
- Oder eine vollständig signierte Bitcoin-Transaktion, die so umgewandelt werden kann, dass sie für die Übertragung im Netzwerk bereit ist.

Das PSBT-Format erleichtert die Interoperabilität zwischen verschiedener Wallet-Software und Signaturgeräten (Hardware-Wallet). Derzeit wird die Version 0 des PSBT-Formats verwendet, die im BIP174 definiert ist, aber die Version 2 wird über das BIP370 vorgeschlagen.

> ► *Version 1 der PSBT gibt es nicht. Da Version 0 die erste Version war, wurde die zweite Version informell als Version 2 bezeichnet. Ava Chow, die Autorin des BIP370, hat daher beschlossen, dieser neuen Version die Nummer 2 zu geben, um Verwechslungen zu vermeiden