---
term: HTLC
---

Steht für "*Hashed Timelock Contract*". Dies ist ein Smart contract-Mechanismus, der hauptsächlich bei Lightning verwendet wird. Er findet sich manchmal auch in Atomtauschgeschäften. Im Grunde macht HTLC eine Geldüberweisung von der Offenlegung eines Geheimnisses abhängig und enthält außerdem eine Zeitbedingung, um das Geld des Absenders im Falle einer fehlgeschlagenen Transaktion zu schützen.


Bei Lightning ermöglicht HTLC das Senden von Bitcoins an einen Knoten, mit dem man keinen direkten Kanal hat, indem man mehrere Kanäle durchläuft, ohne dass auf dem Weg dorthin Vertrauen erforderlich ist. Die Zahlung zwischen den einzelnen Knoten hängt von der Bereitstellung eines Vorabbildes ab (das Geheimnis, das, wenn es gehasht wird, einem vereinbarten Wert entspricht). Wenn der Endempfänger dieses Vorabbild zur Verfügung stellt, kann er die Gelder einfordern, was zwangsläufig jeden Zwischenknoten in die Lage versetzt, die Gelder kaskadenartig einzufordern.


Wenn Alice zum Beispiel 1 BTC an David senden möchte, aber keinen direkten Kanal mit ihm hat, muss sie über Bob und Carol gehen, die untereinander Zahlungskanäle haben. So funktioniert die Transaktion:




- David überreicht Alice einen Invoice-Blitz. Dieser enthält den Hash $h$ eines geheimen $s$ (das Vor-Bild), das nur David kennt. Wir haben also: $h = \text{Hash}(s)$ ;
- Alice erstellt eine HTLC mit Bob, der ihr anbietet, ihr 1 BTC unter der Bedingung zu schicken, dass Bob ihr ein geheimes $s$ (das Vorabbild) liefert, das der Hash $h$ entspricht;
- Bob erstellt ein HTLC mit Carol, die ihm anbietet, ihm 1 BTC zu schicken, wenn sie das gleiche Geheimnis $s$ preisgibt;
- Carol erstellt ein HTLC mit David, der weitere 1 BTC bietet, wenn er das $s$-Präbild preisgibt;
- David verrät Carol $s$ (das nur er kennt), um 1 BTC zu erhalten. Carol kann nun $s$ benutzen, um die BTC von Bob zu erhalten. Und Bob, der nun $s$ kennt, macht dasselbe mit Alice.


Schließlich schickte Alice über Bob und Carol 1 BTC an David (eine neutrale Aktion für letztere), ohne dass jemand dem anderen vertrauen muss, da alles in der Kaskade durch die Bedingungen der HTLCs gesichert ist.


HTLCs ermöglichen somit den so genannten "atomaren" Austausch: entweder ist die Überweisung vollständig erfolgreich oder sie scheitert, und die Mittel werden zurückgegeben. Dies garantiert die Sicherheit von Transaktionen, auch zwischen mehreren Teilnehmern, die kein Vertrauen benötigen.