---
name: Boltz
description: Wechseln Sie zwischen verschiedenen Bitcoin-Schichten und behalten Sie dabei die Kontrolle.
---


![cover](assets/cover.webp)



Seit seiner Einführung im Jahr 2009 ist das Peer-to-Peer-Electronic-Cash-System von Bitcoin exponentiell gewachsen und hat Lösungen hervorgebracht, die es uns heute ermöglichen, das System sofort in unserem Alltag zu nutzen, insbesondere durch Lightning Network.



Ein großes Problem blieb jedoch zwischen den Bitcoin-Protokollschichten bestehen: die flüssige Interoperabilität. Um das Potenzial von Bitcoin voll ausschöpfen zu können, musste unbedingt eine Lösung gefunden werden, die Transaktionen zwischen den verschiedenen Schichten des Protokolls ermöglicht. Aus dieser Notwendigkeit heraus entstand 2019 Boltz, eine Brücke, die mehrere Bitcoin-Schichten miteinander verbindet.



## Was ist Boltz?



[Boltz] (https://boltz.Exchange) ist eine nicht-verwahrende Plattform, die ideal für jeden ist, der zwischen den verschiedenen Schichten des Bitcoin-Protokolls Transaktionen durchführen möchte:




- on chain**: Die Hauptkette von Bitcoin, bei der Transaktionen im Durchschnitt alle 10 Minuten bestätigt werden, hat oft hohe Transaktionsgebühren, was nicht unbedingt den Bedürfnissen der Nutzer entspricht;
- Lightning Network**: Das Bitcoin-Overlay für Sofortzahlungen zu niedrigen Gebühren, so dass das Bitcoin für tägliche Zahlungen verwendet werden kann;
- Liquid Network**: ein von Blockstream geschaffenes Overlay für Bitcoin, das schnelle, Confidential Transactions und die Verwendung anderer Bitcoin-basierter Finanzinstrumente ermöglicht;
- RootStock**: Eine Lösung für die Entwicklung intelligenter Verträge auf der Grundlage des Bitcoin-Protokolls.



![layers](assets/fr/01.webp)



Die Interoperabilität zwischen diesen verschiedenen Schichten ist von großer Bedeutung, da sie den Nutzern die Flexibilität bietet, die sie benötigen, um alle Vorteile des Bitcoin-Ökosystems voll auszuschöpfen.



Boltz verwendet Atomic Swaps. Diese Technologie ermöglicht den Tausch von Bitcoins zwischen zwei Schichten (z. B. BTC onchain in Exchange gegen BTC auf Lightning) direkt zwischen zwei Parteien, ohne dass Vertrauen oder ein Vermittler erforderlich sind. Diese Tauschvorgänge werden "atomar" genannt, weil sie nur zwei Ergebnisse hervorbringen können:




- Entweder ist der Exchange erfolgreich und die beiden Teilnehmer haben ihre BTC tatsächlich ausgetauscht;
- Entweder scheitert der Exchange, und beide Teilnehmer gehen mit ihren ursprünglichen BTC.



Auf diese Weise behalten Sie die ständige Selbstverwahrung Ihrer Bitcoins, und der Exchange basiert nicht auf dem Vertrauen in die Gegenpartei: Entweder der Exchange ist erfolgreich oder scheitert, aber keine Partei kann die Gelder der anderen stehlen.



Ein atomarer Exchange arbeitet mit intelligenten Verträgen [HTLC](https://planb.network/resources/glossary/htlc) (*Hashed Timelock Contract*). Bei dieser Art von Contract wird der Betrag in einem Zwei-Wege-Kanal "gesperrt", und es wird eine zeitliche Beschränkung eingeführt, so dass der Saldo an den Einzahler zurückfällt, wenn die Transaktion nicht innerhalb einer bestimmten Zeit abgeschlossen wird. Dieser Mechanismus wird von der Boltz-Plattform verwendet.



## Ihr erster Austausch mit Boltz



Boltz ist eine nicht-verwahrende Web-Plattform, die keine persönlichen Daten von Ihnen verlangt. Boltz hat eine minimalistische, flüssige Interface, die es Ihnen ermöglicht, in weniger als einer Minute mit dem Handel zu beginnen.



![boltz](assets/fr/02.webp)



Sobald Sie auf der Plattform sind, können Sie den atomaren Austausch zwischen den verschiedenen Schichten des Bitcoin-Ökosystems herstellen.



![home](assets/fr/03.webp)



Sie sehen die minimale und maximale Anzahl von Satoshis (die kleinste Einheit von Bitcoin), die Sie über Boltz handeln können, einschließlich der Netzgebühren und eines von Boltz erhobenen Prozentsatzes zwischen 0,1 % und 0,5 %.



![fees](assets/fr/04.webp)



Wählen Sie dann das Layer aus, von dem Sie ein atomares Exchange machen wollen, und wählen Sie das Layer aus, auf dem Sie die Bitcoins empfangen wollen.



![couches](assets/fr/05.webp)



In diesem Lernprogramm konzentrieren wir uns auf den atomaren Exchange vom Haupt-Layer zum Lightning Network.



Sie können die Basiseinheit für Ihre Vermittlungsstellen konfigurieren, indem Sie zwischen den Optionen wählen:




- BTC ;
- Sats.



![unités](assets/fr/06.webp)



Sobald Sie Ihre Grundkonfigurationen abgeschlossen haben, fügen Sie den Betrag Ihres atomaren Exchange ein und erstellen dann einen Lightning Invoice für den entsprechenden Betrag oder fügen einfach Ihre LNURL ein.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.network/tutorials/wallet/mobile/blitz-wallet-794bdac4-1af4-49d5-9ea5-abb8228ca196

![swap](assets/fr/07.webp)



Um auf Nummer sicher zu gehen, überprüfen Sie bitte die Parameter Ihres Exchange, um die mit Ihrem Exchange verbundenen Sicherungsschlüssel zu exportieren.



Laden Sie über das Symbol **Einstellungen** den Sicherungsschlüssel herunter und speichern Sie die Datei entsprechend.



![settings](assets/fr/08.webp)



![rescue-key](assets/fr/09.webp)



Diese Datei enthält die 12 Schlüsselwörter des Portfolios, das mit Ihren Atomtauschbörsen verbunden ist.



Klicken Sie dann auf die Schaltfläche **Atomic Exchange erstellen** und fahren Sie mit der Zahlung des angegebenen Betrags fort.



![payment](assets/fr/10.webp)



https://planb.network/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

https://planb.network/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

Sobald Ihre Zahlung erfolgt ist und bestätigt wurde, erhalten Sie automatisch den entsprechenden Betrag auf Ihrem Lightning Wallet.



Suchen Sie im Menü **Rückerstattung** Ihren atomaren Exchange-Verlauf, um den Exchange zu identifizieren, für den Sie eine Rückerstattung wünschen. Sie können auch eine Historie von Umtauschvorgängen importieren, die Sie auf einem anderen Gerät durchgeführt haben, z. B. mithilfe der Sicherungsschlüsseldatei, die mit diesen Umtauschvorgängen verbunden ist.



![refund](assets/fr/11.webp)



Im Menü **Historie** können Sie eine detailliertere Historie der mit Ihrem Rettungsschlüssel verbundenen Austauschvorgänge herunterladen, indem Sie auf die Schaltfläche **Sicherung** klicken.



![backup](assets/fr/12.webp)



⚠️ Bitte geben Sie auch diese Datei nicht weiter, da sie alle Informationen zu Ihren Transaktionen und den mit diesen Transaktionen verbundenen Sicherungsschlüssel enthält.



Boltz bietet Ihnen ein hohes Maß an Vertraulichkeit dank seines Zugangs über einen `.onion`-Link im Tor-Netzwerk. Machen Sie den atomaren Austausch völlig anonym, indem Sie das Menü **Onion** auswählen, nachdem Sie das Tor-Browsing in Ihrem Browser aktiviert haben.



![onion](assets/fr/13.webp)



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Inzwischen sind Sie mit Boltz vertraut, einer einzigartigen Exchange-Plattform, die die Interoperabilität zwischen den verschiedenen Schichten des Bitcoin-Ökosystems ermöglicht.