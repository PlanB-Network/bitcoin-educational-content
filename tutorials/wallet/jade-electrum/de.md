---
name: Jade - Electrum
description: So verwenden Sie Ihren Jade oder Jade Plus mit Electrum (Desktop)
---

![cover](assets/cover.webp)



dieser Leitfaden stammt aus einer [Bitcoin Workshop-Lektion](https://officinebitcoin.it/lezioni/jadeele/index.html)_



Das Tutorial wurde mit Jade Classic erstellt, aber die Operationen sind auch für diejenigen gültig, die Jade Plus haben.



Nach der Initialisierung von Jade können Sie es verwenden und dazu ein wallet-Display auswählen.



Jade ist ein Gerät, das mit mehreren wallet oder Companion Apps verwendet werden kann, wie sie von Blockstream auf seiner Website beschrieben werden.



In dieser Anleitung sehen Sie die Schritte für die Verwendung des Electrum Wallet über eine USB-Kabelverbindung.



## Übertragung des öffentlichen Schlüssels



Nehmen Sie Ihre initialisierte Jade und schalten Sie sie ein. Sobald du sie einschaltest, sieht sie so aus:




![img](assets/en/32.webp)



Wenn Sie _Jade entsperren_ wählen, wird das Menü angezeigt, in dem Sie auswählen müssen, wie Sie Ihr Gerät mit der Begleit-App verbinden.



Beim Electrum können Sie Jade nur über USB anschließen, also wählen Sie diese Methode.



Starten Sie Electrum, das als Standardoption vorschlägt, das zuletzt verwendete wallet zu öffnen.



Wenn dies das erste Mal ist, dass Sie Jade mit dem Electrum verbinden, wählen Sie _Neue Brieftasche erstellen_ und dann _Fertigstellen_.



![img](assets/en/34.webp)



Name wallet.



![img](assets/en/35.webp)



Wählen Sie Standard Wallet.



![img](assets/en/36.webp)



Bei der Auswahl des Schlüsselspeichers muss unbedingt _Hardwaregerät verwenden_ ausgewählt werden.



![img](assets/en/37.webp)



Electrum beginnt mit der Suche nach dem Hardware-Gerät.



![img](assets/en/38.webp)



Wenn Sie die USB-Verbindung zum Computer herstellen (die USB-C-Seite ist bereits an Jade angeschlossen), erscheint die wallet-Hardware im Sperrmodus. Jade entsperrt sich durch Eingabe der sechsstelligen PIN, die bei der Einrichtung festgelegt wurde.




![img](assets/en/39.webp)



Ungesperrtes Hardware-Gerät, Electrum erkennt Jade. Fahren Sie fort, indem Sie auf _Weiter_ klicken.



![img](assets/en/40.webp)



An dieser Stelle fordert Electrum Sie auf, das Richtlinienskript festzulegen: Wählen Sie _Native Segwit_.



![img](assets/en/41.webp)



Die Phase der Übertragung des öffentlichen Schlüssels von wallet von Jade zum Display Electrum beginnt.



Wenn der Export des öffentlichen Schlüssels abgeschlossen ist, ist der Vorgang beendet.



Der Watch-Only ist bereit und Electrum meldet die Fertigstellung mit folgendem Bildschirm.



![img](assets/en/42.webp)



wallet wird tatsächlich erstellt, und Sie können mit der Erkundung beginnen: Sie sehen die _Adressen_, die _Wallet-Informationen_ und - was am wichtigsten ist - Sie sehen in der unteren rechten Ecke den Hinweis, dass es sich um ein Gerät von Blockstream handelt. Der grüne Punkt neben dem Blockstream-Logo zeigt an, dass das Gerät eingeschaltet und korrekt mit dem lokalen Netzwerk verbunden ist.



![img](assets/en/43.webp)



## Empfangen und Ausgeben von Transaktionen



Geben Sie im Menü _Empfangen_ von Electrum, generate einen `scriptPubKey` (Adresse) ein, um Gelder zu empfangen. Beginnen Sie immer mit einem kleinen Betrag und machen Sie einen Empfangs- und Ausgabetest.



![img](assets/en/44.webp)



Wenn Sie Satss empfangen haben, können Sie deren Ankunft im Menü _History_ überprüfen.



![img](assets/en/45.webp)



![img](assets/en/46.webp)



Sobald die Transaktion bestätigt ist, können Sie diese UTXO ausgeben und den Test beenden.



Die Kosten entstehen durch die Verwendung von Jade zum Unterschreiben.



Gehen Sie zum Menü _Senden_ von Electrum, fügen Sie einen scriptPubKey ein, und prüfen Sie ihn gut.



![img](assets/en/47.webp)



Wenn Sie fertig sind, drücken Sie _Bezahlen_.



Es öffnet sich das Transaktionsfenster, in dem es wichtig ist, die richtigen Transaktionsgebühren einzustellen. Wenn Sie alle Einstellungen vorgenommen haben, klicken Sie auf _Vorschau_ in der unteren rechten Ecke.



![img](assets/en/48.webp)



Das Transaktionsfenster zeigt einige wichtige Details, vor allem den Status: "Unsigniert".



In diesem Stadium sehen Sie auch den Befehl _Sign_, den Sie anklicken müssen, um die Unterschrift mit Jade anzubringen.



![img](assets/en/49.webp)



Nun beginnt eine Kommunikationsphase zwischen dem Display wallet und dem Hardware-Gerät, in der Electrum Sie darauf hinweist, den Anweisungen auf dem eingeschalteten und unterschriftsbereiten Hardware-Gerät zu folgen.



![img](assets/en/50.webp)



**Zunächst sollten Sie jedoch überprüfen, was Sie unterschreiben: Alle Parameter der Transaktion, die Sie gerade eingerichtet haben, erscheinen auch auf Jade** und Sie können sie alle überprüfen.



![img](assets/en/51.webp)



Um fortzufahren, stellen Sie sicher, dass Sie den Cursor immer auf den "→"-Pfeil stellen, der zu den nächsten Schritten führt, und niemals auf das "X", es sei denn, Sie wollen den Vorgang beenden, ohne ihn zu vollenden.



Der Prüfungsteil endet mit der Gebührenanzeige. Zu diesem Zeitpunkt ist die Bestätigung gleichbedeutend mit Ihrer Unterschrift.



![img](assets/en/52.webp)



Jade bearbeitet den Vorgang für einen kurzen Moment, danach kehrt es zum Startmenü zurück.



![img](assets/en/53.webp)



Auf Electrum sehen Sie den Status der Transaktion, der sich von "unsigniert" zu "signiert" geändert hat, und Sie können die Transaktion nun durch Klicken auf "Übertragen" weiterleiten.



![img](assets/en/54.webp)



Das so geprüfte wallet kann zur Aufnahme des für die sichere Lagerung bestimmten UTXO verwendet werden.



![img](assets/en/55.webp)



Diese Anleitung ist ein Beispiel für die Verwendung Ihres über USB angeschlossenen Jade mit einer wallet-Uhr. Electrum ist ein klassisches Beispiel, aber Sie können andere wallet Software bevorzugen. Jade exportiert den öffentlichen Schlüssel zu vielen anderen Geldbörsen: finden Sie die ähnlichen Funktionen, die Sie über in diesem Tutorial lesen, um Sie zu führen und finden, wie es Ihre Lieblings companio App zu verwenden.