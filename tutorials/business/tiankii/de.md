---
name: Tiankii
description: Lightning-Suite von Tools für Einzelhändler und Verbraucher
---

![cover](assets/cover.webp)



Im Bitcoin-Ökosystem bleibt die Annahme von Zahlungen in Echtzeit eine große Herausforderung für Unternehmen und Privatpersonen. Herkömmliche Lösungen erfordern oft fortgeschrittenes technisches Wissen, eine komplexe Infrastruktur, die es zu unterhalten gilt, oder erfordern, dass Gelder von Zwischenhändlern gehalten werden. Diese Situation behindert die Massenanwendung von Bitcoin als Alltagswährung, trotz der vielversprechenden technologischen Fortschritte von Lightning Network.



Tiankii, ein salvadorianisches Unternehmen, das im Jahr 2021 gegründet wurde, reagiert auf dieses Problem, indem es eine zugängliche, modulare Bitcoin-Infrastruktur anbietet. Anstatt die Annahme eines geschlossenen Ökosystems zu erzwingen, bietet Tiankii eine Reihe miteinander verbundener Tools an, die es jedem ermöglichen, Bitcoin Lightning in sein Unternehmen zu integrieren, ohne die Kontrolle über seine Mittel zu verlieren.



## Was ist Tiankii?



### Ursprung und Philosophie



Tiankii - ein Nahuatl-Begriff, der "Markt unter freiem Himmel, der für alle zugänglich ist" bedeutet - ist El Salvadors erstes Start-up-Unternehmen, das zu 100 % aus Bitcoin besteht. Das von Darvin Otero nach der Einführung von Bitcoin als gesetzliches Zahlungsmittel des Landes gegründete Unternehmen zielt darauf ab, Bitcoin von einem Wertaufbewahrungsmittel in eine transaktionsfähige Währung für alltägliche Einkäufe zu verwandeln. Im Gegensatz zu verwahrenden Plattformen verfolgt Tiankii einen nicht-verwahrenden Ansatz, bei dem die Nutzer die Kontrolle über ihre Gelder behalten und die Infrastruktur nur als technischer Vermittler dient.



### Technische Architektur



Tiankii ist als Anbieter einer Bitcoin-as-a-Service-Infrastruktur auf der Grundlage von Lightning Network positioniert. Diese Technologie der zweiten Schicht ermöglicht nahezu augenblickliche Transaktionen mit vernachlässigbaren Kosten, wodurch Mikrozahlungen und alltägliche Einkäufe möglich werden.



Die Architektur stützt sich auf drei Säulen:



**Lightning-zuerst**: Systematische Bevorzugung des Lightning-Netzwerks wegen seiner Geschwindigkeit und niedrigeren Kosten, während on-chain-Transaktionsunterstützung für große Beträge beibehalten wird.



**Offene Standards**: Verwendung von LNURL zur Automatisierung von Zahlungsanforderungen, Lightning Address für lesbare E-Mail-IDs und Bolt Card für interoperable NFC-Zahlungen.



**wallet-agnostische Modularität**: Es besteht die Möglichkeit, verschiedene Lightning-Portfolios (LNbits, Blink, BlueWallet) oder Ihren eigenen Knotenpunkt anzuschließen, was maximale Flexibilität je nach dem erforderlichen Maß an Fachwissen und Autonomie bietet.



## Tiankii Ökosystem Werkzeuge



### Bitcoin POS - Terminal für die Bezahlung in Geschäften



Die Anwendung verwandelt Smartphone oder Tablet in ein Lightning-Terminal. Der Händler gibt den Betrag in der lokalen Währung ein, und die App generiert einen Lightning-QR-Code oder akzeptiert eine Bolt-Karte. Die Transaktionen werden sofort und provisionsfrei gutgeschrieben, mit automatischer Umrechnung in über 150 Währungen, Trinkgeldverwaltung und Umsatzhistorie.



### Merchant Dashboard - Vereinheitlichtes Vertriebsmanagement



Interface Web zentralisiert, um seine wallet Lightning zu verbinden, Transaktionen in Echtzeit zu verfolgen, Rechnungen und generate Buchhaltungsberichte auszustellen. Die Plattform fasst alle Kanäle zusammen: Zahlungen im Geschäft (POS), Online-Verkäufe (E-Commerce-Plug-ins) oder API-Integrationen. Die Zahlungen laufen auf dem gewählten wallet zusammen.



### Bitcoin Kontaktlose Karte (Bolt Karte)



Die NFC Bolt Karte ist die wichtigste Innovation von Tiankii zur Demokratisierung des Bitcoin für die Allgemeinheit. Sie funktioniert wie eine kontaktlose Bankkarte und ermöglicht es Ihnen, Bitcoin Lightning-Einkäufe einfach durch Antippen eines kompatiblen Terminals zu bezahlen.



Im Gegensatz zu herkömmlichen Verwahrungslösungen folgt diese Karte einem offenen Standard, der Interoperabilität garantiert. Die Nutzer können sie über die IBI-Anwendung mit ihrem eigenen wallet verknüpfen und so ihre privaten Schlüssel und die volle Kontrolle über die damit verbundenen Mittel behalten. Die Zahlung dauert nur eine Sekunde, ohne dass Sie Ihr Smartphone herausnehmen oder eine aktive Internetverbindung zum Zeitpunkt der Zahlung haben müssen.



Diese Lösung ist besonders integrativ für Menschen, die mit Smartphones nicht vertraut sind, und bietet einen zugänglichen Zugang zur Bitcoin-Wirtschaft.



### IBI App - Interface einzelne Bitcoin



Die IBI-Anwendung (Individual Bitcoin Interface) ist für Einzelpersonen gedacht, die Bitcoin Lightning täglich nutzen möchten. Ihr Hauptvorteil liegt in der Generierung eines personalisierten Address Lightning, einer Zahlungskennung, die im E-Mail-Format lesbar ist (Beispiel: alice@ibi.me).



Diese Kennung vereinfacht den Zahlungseingang drastisch: Sie müssen nicht für jede Transaktion eine neue Rechnung ausstellen, sondern der Absender kann einfach die Lightning-Adresse eingeben. Über die Schnittstelle können Sie auch Ihre Bolt Karte verwalten (Aktivierung, Deaktivierung, Ausgabenlimits), verschiedene Lightning-Wallets verbinden und Zahlungen durch Scannen von QR-Codes vornehmen.



### E-Commerce-Plugins



Gebrauchsfertige Integrationen für WooCommerce, Shopify und Cloudbeds. Installiert in wenigen Minuten, um Bitcoin Lightning zur Kasse zu bringen. Vorteile: Null Provision (im Vergleich zu 2-3% bei Kreditkarten), sofortige Abrechnung, weltweiter Zugang, keine Rückbuchungen. Zahlungen treffen direkt auf dem angeschlossenen wallet des Händlers ein.



### Bitcoin API und Entwicklerwerkzeuge



Das Tiankii SDK ermöglicht es, Bitcoin Lightning in bestehende Anwendungen zu integrieren, ohne einen eigenen Knotenpunkt zu unterhalten. API wickelt die Rechnungserstellung, Zahlungsüberprüfung und Massenversand über eine robuste, in der Google Cloud gehostete Infrastruktur ab. Command Center vervollständigt das Angebot für Unternehmen mit Address Lightning für benutzerdefinierte Domains, Massenzahlungen und die zentralisierte Verwaltung von NFC-Terminals und -Karten.



## Installation und erste Schritte



### Wesentliche Voraussetzungen



Die Nutzung von Tiankii erfordert keine komplexen technischen Voraussetzungen. Die Anwendungen funktionieren über einen Webbrowser auf einem Smartphone, Tablet oder Computer. Es ist keine native Anwendungsinstallation erforderlich: Sie benötigen lediglich einen Internetzugang und einen aktuellen Browser, um auf IBI oder das Merchant Dashboard zuzugreifen.



**Für private Nutzer (IBI App)**: Es ist kein vorheriger wallet Lightning erforderlich. Wenn Sie Ihr Konto erstellen, konfiguriert Tiankii automatisch ein funktionierendes Address Lightning über das [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html), eine nodeless Implementierung, die das Liquid Netzwerk im Hintergrund nutzt. Sie können sofort Zahlungen empfangen und senden, ohne dass eine technische Konfiguration erforderlich ist. Diese Lösung vereinfacht den Zugang für Einsteiger drastisch und bleibt dabei selbsterklärend.



**Für Händler (Merchant Dashboard)** : Der Anschluss eines bestehenden wallet Lightning ist zwingend erforderlich, um Point-of-Sale-Terminals zu nutzen und Zahlungen zu empfangen. Tiankii unterstützt zahlreiche Lösungen: mobile Geldbörsen (Blink, Strike), selbst gehostete Lösungen (LNbits, LND/CLN-Node) oder Web-Wallets (Alby). Detaillierte Anleitungen für die Verbindung finden Sie im Abschnitt Ressourcen dieses Tutorials.



### Für Privatkunden: IBI-App



**Kontoerstellung



Gehen Sie zu accounts.ibi.me, um Ihr Konto zu erstellen. Auf dieser Seite können Sie zwischen zwei Kontotypen wählen: "Personal Use" für die private Nutzung oder "Business Use" für die gewerbliche Nutzung. Wählen Sie "Persönliche Nutzung", um Zugang zu den Tools für den Empfang und Versand von Zahlungen in Bitcoin zu erhalten.



![Choix du type de compte](assets/fr/01.webp)



Nachdem Sie "Persönliche Nutzung" ausgewählt haben, werden Sie automatisch zu go.ibi.me weitergeleitet, um Ihre Registrierung abzuschließen. Dies kann per E-Mail, Telefonnummer oder über Ihr Google-, Microsoft- oder Twitter-Konto erfolgen. Sobald Sie sich registriert haben, können Sie sofort auf Ihre IBI-Schnittstelle zugreifen, wobei Ihr Lightning Address bereits betriebsbereit ist.



![Création du compte](assets/fr/02.webp)



**Interface main**



Die IBI-Benutzeroberfläche zeigt Ihr Guthaben in Satoshis und lokaler Währung (USD) an. Mit drei Schaltflächen können Sie interagieren: "Empfangen", um Zahlungen zu empfangen, "Scannen", um einen QR-Code zu scannen, und "Senden", um Satoshis zu senden.



![Interface IBI](assets/fr/03.webp)



**Zahlung erhalten**



Um Satoshis zu empfangen, drücken Sie auf "Empfangen". Die Anwendung generiert automatisch einen QR-Code und zeigt Ihren persönlichen Address Lightning an (nom@ibi.me Format). Teilen Sie diese Adresse oder den QR-Code dem Absender mit: Das Geld kommt sofort auf Ihrem IBI-Konto an.



![Réception avec Lightning Address](assets/fr/04.webp)



Sobald Ihr Guthaben gutgeschrieben wurde, können Sie diese Satoshis für Zahlungen verwenden.



**Senden Sie eine Zahlung**



Um Satoshis zu senden, drücken Sie "Senden". Sie können entweder einen Lightning QR-Code scannen oder direkt ein Lightning Address Ziel eingeben.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



Geben Sie den gewünschten Betrag in Satoshis ein, prüfen Sie den Gegenwert in der Landeswährung und bestätigen Sie dann die Zahlung.



![Confirmation du montant](assets/fr/07.webp)



Eine Erfolgsmeldung bestätigt den Versand mit folgenden Angaben: gesendeter Betrag, Transaktionsgebühr und Empfänger.



![Paiement réussi](assets/fr/08.webp)



**Kontoführung



Unter Einstellungen können Sie Ihre Bitcoin NFC-Karten (Bolt Cards) verwalten. Über die Schnittstelle können Sie Ihre Karten aktivieren, deaktivieren oder Ausgabenlimits für sie festlegen.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### Für Händler: Händler-Dashboard und POS



**Erstellung eines Geschäftskontos



Gehen Sie zu accounts.ibi.me, um Ihr Konto zu erstellen. Wählen Sie "Business Use", um auf die Händler-Tools zuzugreifen. Diese Art von Konto schaltet den Zugang zum Händler-Dashboard und zu Point-of-Sale-Terminals frei.



Nachdem Sie "Business Use" ausgewählt haben, werden Sie automatisch zum Merchant Dashboard (pay.tiankii.com) weitergeleitet. Dies führt Sie zur Geschäftsverwaltungsoberfläche mit Umsatzverfolgung, Transaktionen und Zahlungstools. Um mit der Annahme von Zahlungen zu beginnen, müssen Sie zunächst Ihr wallet Lightning anschließen, indem Sie auf den Link oben auf der Seite klicken (siehe Pfeil im Bild).



![Dashboard marchand](assets/fr/11.webp)



**wallet Lightning** Anschluss



Entscheidender Schritt bei der Aktivierung Ihrer Verkaufsstelle: Schließen Sie Ihren wallet Lightning an, um Zahlungen zu empfangen. Die Schnittstelle bietet mehrere Verbindungsoptionen. Bitte beachten Sie, dass einige Optionen (Bitcoin Onchain und Lightning Network) noch in der Entwicklung sind und auf der Schnittstelle ausgegraut erscheinen.



![Options de connexion wallet](assets/fr/12.webp)



In diesem Tutorial verwenden wir den Lightning Address-Anschluss, der mit Chivo, Blink Wallet und Strike kompatibel ist. Geben Sie Ihren Lightning Address (nom@domaine.com Format) ein, zum Beispiel von LN Markets, Alby oder einem anderen kompatiblen Anbieter.



![Saisie de la Lightning Address](assets/fr/13.webp)



Sobald Sie sich angemeldet haben, ist Ihr Konto einsatzbereit. Sie können nun auf die Kasse zugreifen oder zum Dashboard zurückkehren, um andere Einstellungen zu konfigurieren.



![Connexion réussie](assets/fr/14.webp)



*zahlungslinks** *Zahlungslinks



Das Menü "Zahlungstools" ermöglicht den Zugriff auf "Zahlungsanforderung", mit der Sie Zahlungslinks erstellen und verwalten können. Diese Funktion ist nützlich, um personalisierte Zahlungslinks zu erstellen, die per E-Mail oder Nachricht verschickt werden: Spenden, Einzelzahlungen, Mehrfachzahlungen oder sogar Paywalls zum Schutz von Inhalten. Sie können verschiedene Arten von Links erstellen, um Ihren geschäftlichen Anforderungen gerecht zu werden.



![Liens de paiement](assets/fr/15.webp)



**Verkaufsterminal-Konfiguration**



Um Zahlungen in Geschäften zu akzeptieren, rufen Sie das Menü "Verkaufsterminal" unter "Zahlungstools" auf. In diesem Bereich können Sie Ihre POS-Terminals erstellen und verwalten (die Anzahl der Terminals hängt von Ihrem Tarif ab, siehe Freemium vs. Business-Tarif unten). Klicken Sie auf "Öffnen", um die POS-Schnittstelle in Ihrem Browser zu öffnen.



![Gestion des terminaux](assets/fr/16.webp)




**Verkaufsanbahnung**



Das POS-Terminal zeigt ein numerisches Tastenfeld zur Eingabe des Verkaufsbetrags an. Geben Sie den Betrag in Ihrer Landeswährung ein (z. B. 500 sats entspricht 630,74 ARS), und drücken Sie dann zur Bestätigung auf "OK".



![Saisie du montant](assets/fr/17.webp)



Die Anwendung generiert sofort einen Lightning QR-Code und ein Lightning Address für die Zahlung. Kunden können den QR-Code mit ihrem wallet scannen oder ihre Bolt-Karte an einem NFC-Terminal verwenden.



![QR code de paiement](assets/fr/18.webp)



Sobald die Zahlung eingegangen ist, erscheint ein Bestätigungsbildschirm, der den erhaltenen Betrag in Landeswährung und Satoshis anzeigt. Sie können eine Quittung per E-Mail versenden, das Ticket ausdrucken oder sofort einen neuen Verkauf starten.



![Paiement encaissé](assets/fr/19.webp)



**Überwachung und Verwaltung**



Alle Transaktionen werden in Ihrem Merchant Dashboard aufgezeichnet. Sie haben eine vollständige Nachverfolgung der Einnahmen nach Zeitraum, der Gesamtzahl der Verkäufe und eine detaillierte Historie für Ihre Buchhaltung.



Die Oberfläche der Einstellungen bietet mehrere Konfigurationsregisterkarten. Auf der Registerkarte "Allgemeine Einstellungen" können Sie Ihr Händlerprofil und Ihre Benachrichtigungen verwalten. Auf der Registerkarte "Benutzer" können Sie den Zugriff auf das Händler-Dashboard für Ihr Team hinzufügen und verwalten (Mehrbenutzerverwaltung je nach Plan). Die Registerkarte "Entwicklungsarbeitsbereich" ermöglicht den Zugriff auf API-Schlüssel für fortgeschrittene Integrationen, während "Abonnement" die Verwaltung Ihres Abonnements ermöglicht.



![Paramètres du compte marchand](assets/fr/20.webp)



**Freemium vs. Business-Pläne



Tiankii bietet zwei Pakete für das Merchant Dashboard an. Der **Freemium**-Plan (kostenlos) eignet sich für Start-ups mit Einschränkungen: eine einzige Verkaufsstelle, ein einziger Benutzer, ein auf 1.000 USD begrenztes monatliches Volumen und kein Zugang zu E-Commerce-Konnektoren. Der **Business**-Tarif (0,5 % Gebühr pro Transaktion) bietet unbegrenzte Terminals, unbegrenzte Benutzer, unbegrenztes Volumen, Zugang zu WooCommerce/Shopify/Cloudbeds-Plugins und exklusive WhatsApp-Benachrichtigungen.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## Vorteile und Zwänge



### Höhepunkte



**Selbstverwahrung**: Sie behalten Ihre privaten Schlüssel und die volle Kontrolle über Ihr Geld. Kein Risiko des Einfrierens von Konten oder des Konkurses von Drittanbieter-Plattformen.



**Einfachheit**: Lightning Address als E-Mail-Adresse, NFC-Zahlungen durch einfaches Antippen, intuitive Benutzeroberfläche ohne technische Kenntnisse.



**Komplettes Ökosystem**: Tools für alle Profile (Einzelpersonen, Einzelhändler, Entwickler) mit modularen Integrationen, die Ihren Bedürfnissen entsprechen.



**Professionelle Einhaltung der Vorschriften**: Sicheres Cloud-Hosting, PCI-DSS-Konformität, Einhaltung der salvadorianischen Vorschriften.



### Beschränkungen



**Einschränkungen durch Blitzschlag**: Erfordert permanente wallet-Verbindung, Liquiditätsmanagement für große Mengen, Ausfallrisiko, wenn der Empfänger offline ist. Tiankii entschärft diese Aspekte mit integrierten LSPs.



**SaaS-Abhängigkeit**: Wenn Tiankii nicht verfügbar ist, ist die Rechnungserstellung vorübergehend nicht möglich (Ihre Gelder bleiben sicher).



**Datenschutz**: Tiankii kann die Metadaten der Transaktionen (Beträge, Daten) einsehen. Weniger privat als eine selbst gehostete Lösung wie BTCPay Server.



## Schlussfolgerung



Tiankii veranschaulicht, wie eine gut konzipierte Infrastruktur die technischen Hindernisse beseitigen kann, die die Masseneinführung von Bitcoin als Alltagswährung verhindern. Durch die Kombination der Leistung von Lightning Network mit einem nicht-rechtsstaatlichen Ansatz und zugänglichen Tools bietet das Ökosystem einen ausgewogenen Weg zwischen finanzieller Souveränität und einfacher Nutzung.



Für Händler stellt Tiankii eine Möglichkeit dar, die Transaktionskosten drastisch zu senken und gleichzeitig einen neuen Kundenstamm zu erschließen. Für die Verbraucher verwandeln Lightning Address und NFC-Karten Bitcoin in eine praktische Währung, ohne technische Komplexität.



Auch wenn die breite Einführung von Bitcoin eine Herausforderung bleibt, die Ausbildung und Zeit erfordert, zeigen Infrastrukturen wie Tiankii, dass die technischen Mittel bereits vorhanden sind. Das Ziel, Bitcoin-Zahlungen zu vereinfachen, ist nicht länger eine ferne Vision, sondern eine Realität, die für jeden zugänglich ist, der bereit ist, den Schritt zu wagen.



## Ressourcen



### Offizielle Dokumentation




- [Tiankii offizielle Website](https://tiankii.com)
- [Tiankii Help Center](https://help.tiankii.com)
- [IBI-Antrag](https://go.ibi.me)
- [Merchant Dashboard](https://pay.tiankii.com)
- [Kommandozentrale](https://cc.ibi.me)



### Wallet Verbindungsführungen




- [LNbits verbinden](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Connect BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Connect Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### Gemeinschaft




- [Lightning Network Plus](https://lightningnetwork.plus) - Bildungsressource für Blitze
- [Bitcoin Beach](https://www.bitcoinbeach.com) - Salvadorianische Initiative für Kreislaufwirtschaft Bitcoin



### Verwandte Tools




- [Blink Wallet](https://blink.sv) - Wallet Lightning kompatibel empfohlen
- [LNbits](https://lnbits.com) - Selbst gehostete wallet-Lösung
- [Standard Bolt Karte](https://github.com/boltcard) - Technische Spezifikationen für NFC-Karten