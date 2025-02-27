---
name: Lipa
description: Einrichtung und Nutzung der mobilen Geldbörse Lipa lightning
---
![cover](assets/cover.webp)

Eine Bitcoin-Lightning-Wallet ist eine mobile Anwendung, die sofortige, kostengünstige Transaktionen über das Lightning-Netzwerk von Bitcoin ermöglicht. Im Gegensatz zu Transaktionen auf der Haupt-Blockchain (On-Chain) sind Lightning-Zahlungen nahezu sofort möglich und erfordern nur minimale Gebühren, wodurch sie sich besonders für kleine, alltägliche Zahlungen eignen.

Blitz-Geldbörsen gelten wie alle mobilen Geldbörsen als "heiße" Geldbörsen, da sie mit dem Internet verbunden sind. Sie sind daher in erster Linie für die Verwaltung kleiner Geldbeträge für Ihre täglichen Ausgaben gedacht. Für größere Beträge ist es besser, sicherere Speicherlösungen wie Hardware-Wallets zu verwenden.

Wenn Sie mehr über das Lightning-Netzwerk erfahren möchten und verstehen wollen, wie es technisch funktioniert, empfehle ich Ihnen diesen Kurs:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
In diesem Tutorial werfen wir einen Blick auf **Lipa**, eine einfache und effektive Lightning-Wallet, die in der Schweiz entwickelt wurde.

## Lipa stellt sich vor

Lipa ist eine nicht-vertrauliche Blitzgeldbörse, die sich durch ihre Benutzerfreundlichkeit und eine übersichtliche Oberfläche auszeichnet. Sie wurde von einem Schweizer Team entwickelt und legt Wert auf Vertraulichkeit und Benutzerfreundlichkeit für Anfänger.

Die wichtigsten Merkmale sind:


- Intuitive Benutzeroberfläche
- Autonome Blitzkanalverwaltung
- Unterstützung des LNURL-Protokolls
- Möglichkeit, Bitcoins direkt in der Anwendung zu kaufen

## Installieren und Konfigurieren von Lipa

Der erste Schritt besteht darin, die Lipa-App herunterzuladen. Im Moment ist sie nur auf iOS verfügbar:


- [Für Apple] (https://apps.apple.com/app/lipa-bitcoin-lightning/id1602180066)

Die Android-Version befindet sich derzeit in der Entwicklung und wird bald verfügbar sein.

![Installation de Lipa](assets/fr/01.webp)

Sobald Sie die Anwendung gestartet haben, gelangen Sie auf den Startbildschirm, der Ihnen zwei Optionen bietet:


- Ein neues Portfolio erstellen
- Wiederherstellung eines bestehenden Portfolios aus einem Backup

Sobald Sie Ihre Option gewählt haben, fordert die Anwendung Sie auf, Benachrichtigungen zu aktivieren. Dieser Schritt ist wichtig, da die Benachrichtigungen für :


- Erhalten Sie Benachrichtigungen, wenn Zahlungen eingegangen sind, auch wenn die Anwendung geschlossen ist
- Informieren Sie sich über die Schritte, die beim Kauf von Bitcoin über ihre integrierte Lösung erforderlich sind

Die Anwendung stellt dann ihre Hauptfunktionen über eine Reihe von Einführungsbildschirmen vor:


- Nahtloser Zahlungseingang**: Nutzer können Bitcoin-Zahlungen empfangen, auch wenn die Anwendung geschlossen ist, was Zuverlässigkeit und Komfort garantiert.
- Nicht-kustodiale Lightning-Adressen**: Lipa unterstützt jetzt nicht-verwahrende Lightning-Adressen, was den Datenschutz und die Sicherheit erhöht, da die Nutzer die volle Kontrolle über ihre Bitcoins haben.
- Kontrolle über analytische Daten** : Da Transparenz und Vertraulichkeit an erster Stelle stehen, können die Nutzer die Art der erfassten Daten einsehen und ihre Präferenzen für die Weitergabe festlegen.
- Senden Sie über Ihre Telefonnummer**: Sie brauchen keine komplexen Adressen - wählen Sie einfach einen Kontakt aus, geben Sie den Betrag ein und senden Sie Bitcoins direkt an dessen Telefonnummer.

Die Anwendung profitiert außerdem von kontinuierlichen Verbesserungen in Bezug auf Stabilität, Sicherheit und Zuverlässigkeit, um eine optimale Nutzererfahrung zu gewährleisten.

## Navigation in der Anwendung

Die Benutzeroberfläche von Lipa ist in 4 Hauptregisterkarten unterteilt, die über die Navigationsleiste am unteren Rand des Bildschirms zugänglich sind:

![Navigation principale](assets/fr/02.webp)


- Startseite**: Zeigt Ihren aktuellen Kontostand und die Transaktionshistorie an
- Scanner**: Ermöglicht das Scannen von QR-Codes zur Durchführung von Zahlungen
- Karte**: Zeigt eine interaktive Karte mit Bitcoin-akzeptierenden Unternehmen in Ihrer Nähe an
- Einstellungen**: Zugriff auf Anwendungseinstellungen, Backup und Präferenzen

Ein zusätzliches Menü kann durch Herunterziehen des Startbildschirms aufgerufen werden:

![Menu supplémentaire](assets/fr/03.webp)

Diese Geste offenbart zusätzliche Funktionen wie :


- Kauf von Bitcoins
- On-chain Bitcoin-Einzahlung
- Lightning-Rechnungen erstellen, um Bitcoins zu erhalten
- Blitzschnelle Rechnungsbezahlung

## Speichern Sie Ihr Portfolio

Um Ihre Brieftasche zu sichern, gehen Sie auf die Registerkarte "Einstellungen" und wählen Sie "Wiederherstellungsphrase". Lipa verwendet eine Wiederherstellungsphrase, die Sie unbedingt sorgfältig auf einem physischen Medium (Papier, Metall) notieren müssen. Nur mit diesem Satz können Sie Ihr Guthaben wiederherstellen, wenn Ihr Telefon verloren geht oder gestohlen wird. Um Ihre Sicherung zu bestätigen, werden Sie von der Anwendung aufgefordert, 3 zufällige Wörter aus Ihrer Phrase zu bestätigen.

![Backup](assets/fr/04.webp)

Für weitere Informationen darüber, wie Sie Ihre Wiederherstellungsphrase richtig sichern und verwalten, empfehle ich Ihnen diesen anderen Lehrgang, besonders wenn Sie Anfänger sind:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
## Bitcoins erhalten

Um Bitcoins zu erhalten, haben Sie zwei Möglichkeiten. Um auf diese Optionen zuzugreifen, kehren Sie zum Startbildschirm zurück und ziehen den Bildschirm nach unten. Dann können Sie entweder :


- Wählen Sie "BTC übertragen", um Bitcoins auf der Kette zu erhalten. Scannen Sie dann einfach den QR-Code mit Ihrer anderen Geldbörse und schließen Sie die Transaktion ab.
- Wählen Sie "Anfordern", um über das Lightning-Netzwerk zu empfangen, und geben Sie den Betrag ein, den Sie empfangen möchten.

In beiden Fällen müssen Sie eine Gebühr in Höhe von 0,4 % des Betrags bzw. rund 2 500 Sats entrichten, wenn für den Antrag ein neuer Zahlungskanal eröffnet werden muss (was bei der ersten Zahlung unweigerlich der Fall sein wird).

![Recevoir des bitcoins on chain](assets/fr/05.webp)

![Recevoir des bitcoins lightning](assets/fr/06.webp)

## Bitcoins senden

Um Bitcoins zu versenden, gehen Sie auf den Startbildschirm, ziehen den Bildschirm nach unten und wählen "Bezahlen". Dann einfach entweder :


- eine blitzschnelle LNURL-Adresse eingeben
- scannen Sie einen Blitz-QR-Code, um die Zahlung vorzunehmen.

Sie können auch auf die zweite Registerkarte am unteren Rand des Bildschirms gehen, um einen QR-Code direkt zu scannen.

![Envoi de bitcoins](assets/fr/07.webp)

## Bitcoins kaufen

Lipa bietet die Möglichkeit, Bitcoins gegen eine Gebühr von 1,5 % direkt in der Anwendung zu kaufen. Um einen Kauf zu tätigen, gehen Sie auf den Startbildschirm und ziehen Sie nach unten, um das Menü anzuzeigen. Wählen Sie dann "BTC kaufen". Drei Einführungsbildschirme führen Sie durch den Kaufvorgang.

![Menu d'achat](assets/fr/08.webp)

Geben Sie dann einfach die Bankverbindung des Kontos ein, über das Sie den Kauf tätigen möchten. Wählen Sie Ihre Währung und geben Sie Ihre E-Mail-Adresse ein.

Nach dem Ladebildschirm finden Sie die Referenznummer, die Sie bei der Überweisung angeben müssen, sowie die Bankverbindung für den Umtausch.

![Sélection du montant](assets/fr/09.webp)

Alles, was Sie tun müssen, ist, Ihre Bank zu benutzen, um den gewünschten Betrag zu überweisen, die Überweisung durch Angabe der zuvor abgerufenen RIB einzurichten und die Referenz zum Zeitpunkt der Transaktion anzugeben, damit Lipa diese Bankbewegung mit Ihrer Lipa-Brieftasche verknüpfen kann.

![Confirmation d'achat](assets/fr/10.webp)

## Vorteile und Nachteile

### Vorteile


- Intuitive Schnittstelle
- Korrekte Nebenkosten
- Nicht verwahrend
- Integrierte Bitcoin-Kauflösung
- BTCmap-Integration
- NFC-Unterstützung

### Benachteiligungen


- Es ist nicht möglich, Bitcoins auf der Kette zu versenden
- Geringfügig längere Zahlungsfristen als der Durchschnitt

Lipa ist eine hervorragende Wahl für den Einstieg in das Lightning-Netzwerk und eignet sich besonders für Nutzer, die eine einfache Lösung für alltägliche Zahlungen suchen. Die einfache Bedienung und die übersichtliche Oberfläche machen es zu einer idealen Wallet für Einsteiger und bieten gleichzeitig die wesentlichen Funktionen für die tägliche Nutzung von Lightning.

## Ressourcen


- [Lipas offizielle Website](https://lipa.swiss/)
- [Lipa Unterstützung](https://getlipa.atlassian.net/servicedesk/customer/portal/1)