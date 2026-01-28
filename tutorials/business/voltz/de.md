---
name: Voltz
description: Der All-in-One Lightning wallet für Ihr Unternehmen.
---

![cover](assets/cover.webp)



Die Idee für die Voltz-Plattform stammt von einer Gruppe von Bitcoinern, die ihren eigenen Bitcoin-wallet-Dienst anbieten wollten. Das Ergebnis war eine komplette Infrastruktur für die Akzeptanz von Bitcoin im Einzelhandel. In diesem Tutorial nehmen wir Sie mit auf eine Tour durch Voltz und die Möglichkeiten der Bitcoin-Integration, die die Plattform zu bieten hat.



## Erste Schritte mit Voltz



Voltz ist nicht nur ein verwahrender Lightning wallet, mit dem Sie täglich senden, empfangen und bezahlen können, sondern auch eine vollständige Plattform, die zahlreiche Erweiterungen für die Integration von Bitcoin als Verkaufsstelle oder Marktplatz in Ihrem Unternehmen bietet.



Gehen Sie zur [Voltz]-Plattform (https://www.voltz.com/en) und erstellen Sie ein Konto, indem Sie auf die Schaltfläche "Jetzt ausprobieren" klicken.



![voltz](assets/fr/01.webp)



![login](assets/fr/02.webp)



⚠️ Es ist wichtig, ein starkes alphanumerisches Passwort festzulegen, um Ihre Chancen gegen Brute-Force-Angriffe zu erhöhen, und zu überprüfen, dass Sie sich tatsächlich auf der offiziellen Voltz-Website befinden, um Ihre Anmeldedaten einzugeben, um sich vor Phishing zu schützen.



Die Voltz-Schnittstelle ist der der LnBits-Plattform sehr ähnlich.



https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz ist auf einem LnBits-Server aufgebaut. In unserem Tutorial erfahren Sie, wie Sie Ihre eigenen LnBits-Server einrichten und Ihre Lösungen darauf aufbauen können.



https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

Die Plattform ermöglicht es Ihnen, mehrere Portfolios effizient zu verwalten. Wenn Sie sich anmelden, verfügen Sie automatisch über ein Lightning-Portfolio. Sie können jedoch weitere Portfolios hinzufügen.



![wallets](assets/fr/03.webp)



### Tragbarkeit



Voltz ist nicht auf eine Weboberfläche beschränkt: Im Bereich **Mobile Access** können Sie Ihren aktiven Voltz wallet mit Anwendungen wie Zeus oder Blue Wallet verbinden.



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

Zu diesem Zweck müssen Sie die Erweiterung **LndHub** auf der Plattform installieren und aktivieren.



![lndhub](assets/fr/04.webp)



Wählen Sie Ihr aktives Voltz-Portfolio aus und scannen Sie je nach den Rechten, die Sie vergeben möchten, den entsprechenden QR-Code.




- Mit dem Rechnungs-QR-Code können Sie nur Ihre Portfoliohistorie und generate neue Rechnungen lesen.
- Über den Admin-QR-Code können Sie die Historie einsehen, generate-Rechnungen einsehen und auch Blitzrechnungen bezahlen.



![qrs](assets/fr/05.webp)



In diesem Tutorial verbinden wir unseren Voltz wallet mit der Blue Wallet Anwendung.



![connect](assets/fr/06.webp)



Sobald unser Portfolio verbunden ist, werden alle durchgeführten Aktionen zwischen Blue Wallet und Voltz synchronisiert. Wenn Sie zum Beispiel eine Rechnung in Blue Wallet erstellen, haben Sie auch eine Historie in Voltz.



![sync](assets/fr/07.webp)



Im Abschnitt **Portfoliokonfiguration** finden Sie minimale Parameter wie die Anpassung des Portfolionamens und die Währung, in der Sie Ihre Zahlungen erhalten möchten.



![config](assets/fr/08.webp)



### Erweiterungen



Eine der besonderen Eigenschaften der Voltz-Plattform ist ihre Modularität, die es Ihnen ermöglicht, die von Ihnen benötigten Erweiterungen zu aktivieren. Die Liste der Erweiterungen finden Sie im Menü **Erweiterungen**.



![extensions](assets/fr/09.webp)



Eine dieser Erweiterungen ist der TPoS, ein Point-of-Sale-Terminal, mit dem Sie ein Inventar führen und Zahlungen von Ihren Kunden einholen können.



![tpos](assets/fr/10.webp)



Vom Point-of-Sale-Terminal aus können Sie :




- Sie erhalten eine Webseite, die Sie mit Ihren Kunden und Partnern teilen können;
- Verwalten Sie den Produktbestand;
- Generieren Sie Lightning-Rechnungen;
- Barzahlungen über Bolt-Karten.



Die Erweiterung ist als kostenlose Version und als kostenpflichtige Version mit erweiterten Funktionen erhältlich. Um ein POS-Terminal zu erstellen, klicken Sie auf die Schaltfläche **Öffnen** unter dem Logo der Erweiterung und dann auf **New POS**.



![new_tpos](assets/fr/11.webp)



Legen Sie den Namen Ihrer Verkaufsstelle fest und verbinden Sie dann Ihren Voltz wallet mit Ihrem Terminal, um Zahlungen einzuziehen. Sie können Trinkgelder aktivieren, indem Sie das Kontrollkästchen **Trinkgelder aktivieren** aktivieren. Aktivieren Sie auch die Option Rechnungsdruck, wenn Sie Ihren Kunden Quittungen ausstellen möchten (diese Funktion befindet sich noch in der Entwicklung, daher kann es zu Fehlfunktionen kommen).



Das Point-of-Sale-Terminal umfasst auch eine Steuerkonfiguration, wenn Sie die Steuer Ihres Landes direkt auf Ihre Produkte anwenden möchten.



![tpos](assets/fr/12.webp)



Sobald Ihr POS-Terminal erstellt ist, können Sie vorkonfigurierte Produkte und Dienstleistungen hinzufügen, um einen reibungslosen Zahlungs- und Abrechnungsprozess für Sie und Ihre Kunden zu gewährleisten.



![product](assets/fr/13.webp)



Legen Sie Ihre Produkte an, indem Sie deren Namen definieren, ein Bild hinzufügen und einen Verkaufspreis festlegen.  Sie können Ihre Produkte zur leichteren Nachverfolgung kategorisieren. Sie können Steuern direkt auf ein bestimmtes Produkt anwenden. Wenn auf das Produkt keine Steuer erhoben wird, wird die bei der Erstellung des Kassenterminals konfigurierte Steuer automatisch erhoben.



![products](assets/fr/14.webp)



Sie können Ihre Produktliste automatisch aus einem JSON-Format importieren, indem Sie auf die Schaltfläche **Import/Export** klicken.



![exports](assets/fr/15.webp)



Rufen Sie den Kassenbereich über den Link auf, indem Sie auf das Symbol **Neue Registerkarte** klicken, oder teilen Sie Ihre POS-Plattform per QR-Code mit Ihren Kunden, indem Sie auf das Symbol **QR-Code** klicken.



![lien](assets/fr/16.webp)



![qr](assets/fr/17.webp)



Ihre Kunden können über diese Schnittstelle Ihren Katalog einsehen und ihre Zahlungen vornehmen.



![pos](assets/fr/18.webp)



![chose](assets/fr/19.webp)



![pay](assets/fr/20.webp)



![checkout](assets/fr/21.webp)



In der Gruppe der verfügbaren Erweiterungen finden Sie auch Tools wie die **Invoice**- und **Payment Link**-Erweiterungen, mit denen Sie generate-Rechnungen mit bestimmten Produkten erstellen können, um isolierte Zahlungen ohne Umweg über das POS-Terminal einzuziehen.



## Behalten Sie den Überblick über Ihre Zahlungen



Im Menü **Zahlungen** gibt Ihnen Voltz einen Überblick über die Zahlungen an Ihre verschiedenen Portfolios.


Sie können Ihre Zahlungen nachverfolgen:




- Status.
- Das Label: zum Beispiel **TPOS** für Point-of-Sale-Zahlungen und **lnhub** über die mobile Verbindung in Zeus- und Blue Wallet-Geldbörsen.
- Das Portfolio der Sammlung.
- Summe der Zahlungseingänge und -ausgänge.
- Ein klar definierter Zeitraum.



![payments](assets/fr/22.webp)



## Mehr Optionen



Voltz ist auch eine Infrastruktur, auf der Sie Ihre eigenen Lösungen aufbauen können. Im Abschnitt **Erweiterungen** finden Sie eine Anleitung zur Entwicklung eigener Erweiterungen innerhalb des Voltz- und LnBits-Ökosystems.



![build](assets/fr/23.webp)



Für den Fall, dass Sie Lösungen außerhalb des Ökosystems entwickeln, aber dennoch deren Infrastruktur nutzen möchten, finden Sie im Abschnitt **URL des Knotens** API-Schlüssel und Dokumentationsinformationen mit einem Beispiel dafür, was Sie mit diesen Daten tun können.



Sie können Lightning-Rechnungen aus Ihren Anwendungen mit Ihrem Voltz wallet erstellen, Lightning-Rechnungen bezahlen, Rechnungen entschlüsseln und prüfen.



![keys](assets/fr/24.webp)



Sie haben nun ein gutes Verständnis von Voltz. Wenn Ihnen dieses Tutorial gefallen hat, sind wir sicher, dass Sie in unserem Kurs mehr über die besten Methoden und Werkzeuge zur Integration von Bitcoin in Ihr Unternehmen erfahren werden: Bitcoin für Unternehmen.



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a