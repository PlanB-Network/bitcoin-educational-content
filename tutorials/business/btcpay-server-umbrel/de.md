---
name: BTCPAY SERVER - Regenschirm
description: Installation und Verwendung von BTCPAY SERVER auf Umbrel zur Aufnahme von Bitcoin und Lightning
---

![cover](assets/cover.webp)



Im Bitcoin-Ökosystem stellt die Annahme von Zahlungen eine große Herausforderung für Händler und Unternehmen gleichermaßen dar. Herkömmliche Lösungen, ob Banken (Kreditkarten, Stripe, PayPal) oder sogar Bitcoin (BitPay, Coinbase Commerce), erzwingen Zwischenhändler, die erhebliche Gebühren erheben, Ihre sensiblen Geschäftsdaten sammeln und Ihre Transaktionen nach Lust und Laune BLOCK oder zensieren können. Diese Abhängigkeit steht im Widerspruch zu Bitcoins Grundprinzipien der Dezentralisierung, Vertraulichkeit und finanziellen Souveränität.



BTCPAY SERVER entwickelt sich zur Open-Source-Antwort auf dieses Problem. Dieser selbst gehostete Zahlungsprozessor verwandelt Ihren eigenen Bitcoin-Knoten in eine professionelle Infrastruktur, ohne Zwischenhändler, ohne zusätzliche Bearbeitungsgebühren und ohne Kompromisse beim Datenschutz. BTCPAY SERVER wird seit 2017 von einer globalen Gemeinschaft von Mitwirkenden entwickelt und ermöglicht es Ihnen, Bitcoin- und Lightning-Zahlungen direkt in Ihren Wallets zu empfangen und dabei jederzeit die volle Kontrolle über Ihre Gelder zu behalten.



Traditionell erfordert die Installation von BTCPAY SERVER fortgeschrittene technische Kenntnisse: Linux-Server-Konfiguration, Beherrschung von Docker, Verwaltung von SSL-Zertifikaten und Netzwerksicherheit. Umbrel revolutioniert diesen Ansatz mit einer Ein-Klick-Installation, die direkt mit Ihrem Bitcoin und LIGHTNING NODE integriert ist. Diese Vereinfachung macht das, was bisher erfahrenen Technikern vorbehalten war, für jedermann zugänglich.



**Wichtig zu verstehen**: BTCPAY SERVER on Umbrel funktioniert standardmäßig nur in Ihrem lokalen Netzwerk. Sie können Rechnungen erstellen, Lightning- und Bitcoin-Zahlungen akzeptieren und Ihre Buchhaltung von jedem Gerät aus verwalten, das mit Ihrem Heimnetzwerk verbunden ist (Computer, Smartphone, Tablet). Diese Konfiguration ist ideal für die Abrechnung persönlicher Dienstleistungen, die Verwaltung persönlicher Zahlungen oder die Verwendung von BTCPAY SERVER über Ihr lokales Netzwerk. Für die Integration von BTCPAY SERVER in einen Online-Shop, der im Internet öffentlich zugänglich ist, ist hingegen eine zusätzliche Konfiguration mit öffentlichem Zugang erforderlich (wir werden dieses Thema am Ende des Tutorials behandeln).



Dieses Tutorial führt Sie durch die komplette Installation von BTCPAY SERVER auf Umbrel, die Konfiguration Ihrer Bitcoin, Wallet und LIGHTNING NODE, die Erstellung und Bezahlung von Rechnungen und die Verwaltung von Buchhaltungsberichten. Sie werden herausfinden, wie Sie BTCPAY SERVER effektiv in Ihrem lokalen Netzwerk nutzen können, und dann werden wir über Lösungen für die öffentliche Anzeige sprechen, wenn Sie es in eine E-Commerce-Website integrieren möchten.



## Voraussetzungen



Um diesem Tutorial folgen zu können, müssen Sie Umbrel korrekt installiert und konfiguriert haben. Falls Sie dies noch nicht getan haben, lesen Sie bitte unser Tutorial zur Installation von Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Ihr Bitcoin core-Knoten muss vollständig mit Blockchain synchronisiert werden (100% in der Bitcoin-Anwendung von Umbrel). Diese anfängliche Synchronisierung dauert in der Regel zwischen 3 Tagen und 2 Wochen, abhängig von Ihrer Hardware und Internetverbindung.



Um Lightning-Zahlungen zu akzeptieren, müssen Sie auch LND (Lightning Network Daemon) auf Umbrel installieren. Siehe unsere Anleitung zur Installation und Konfiguration von LND auf Umbrel, wenn Sie diese Funktion aktivieren möchten.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Mindestens 50 GB freier Festplattenspeicher für BTCPAY SERVER, seine Datenbanken und Lightning-Daten. Eine stabile Internetverbindung über ein Ethernet-Kabel wird dringend empfohlen, um Verbindungsunterbrechungen zu vermeiden.



## Installation von BTCPAY SERVER auf Umbrella



Gehen Sie von Umbrel Interface (`umbrel.local`) zum App Store und suchen Sie nach "BTCPAY SERVER" in der Kategorie Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Klicken Sie auf Installieren. Umbrel prüft automatisch, ob Bitcoin core und LND installiert sind, und beginnt dann mit der Installation (2-5 Minuten).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Nach der Installation öffnen Sie die Anwendung. Sie müssen ein Administratorkonto mit sicheren Anmeldedaten erstellen.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Sobald Ihr Konto erstellt wurde, fordert BTCPAY SERVER Sie sofort auf, Ihren ersten Shop einzurichten. Wählen Sie einen professionellen Namen und wählen Sie eine Referenzwährung (EUR, USD oder BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Zugang zum BTCPAY SERVER in Ihrem lokalen Netzwerk



Der BTCPAY SERVER ist von jedem Gerät in Ihrem lokalen Netzwerk (WiFi oder Ethernet) zugänglich. Zugriff über Ihren Browser auf :



```url
http://umbrel.local
```



Oder direkt an :



```url
http://umbrel.local:3003
```



**Fernzugriff mit Tailscale**: Um von überall auf der Welt auf BTCPAY SERVER zuzugreifen, verwenden Sie Tailscale. Mit diesem sicheren VPN können Sie sich mit Ihrem Umbrel verbinden, als ob Sie sich in Ihrem lokalen Netzwerk befänden. Siehe unser Tutorial zu Tailscale auf Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Konfigurieren des Bitcoin-Portfolios



Um Zahlungen zu akzeptieren, müssen Sie ein Bitcoin Wallet konfigurieren. BTCPAY SERVER zeigt die Konfigurationsoptionen auf dem Dashboard an.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Um Wallet Bitcoin zu konfigurieren, gehen Sie zu "Geldbörsen" > "Bitcoin".



Sie haben zwei Möglichkeiten: Sie können ein neues Portfolio direkt in BTCPay erstellen oder ein bestehendes Portfolio importieren. Für den Import stehen mehrere Methoden zur Verfügung:




- Verbinden Sie Hardware Wallet** (empfohlen): Importieren Sie Ihre öffentlichen Schlüssel über die Vault-Anwendung
- Wallet-Datei importieren** (empfohlen): Laden Sie eine exportierte Datei aus Ihrem Portfolio hoch
- Erweiterten öffentlichen Schlüssel eingeben**: Geben Sie Ihren XPub/YPub/ZPub manuell ein
- Wallet QR-Code scannen** : Scannen eines QR-Codes von BlueWallet, Cobo Vault, Passport oder Specter DIY
- Geben Sie Wallet seed** (nicht empfohlen) ein: Geben Sie Ihre 12- oder 24-Wort-Wiederherstellungsphrase ein



![Options de création de portefeuille](assets/fr/06.webp)



Für dieses Tutorial werden wir einen neuen Hot Wallet erstellen: der private Schlüssel wird also auf unserem Umbrel-Server gespeichert. In diesem Fall raten wir Ihnen dringend, die Gelder regelmäßig auf einen Cold Wallet zu übertragen, um zu vermeiden, dass große Beträge auf dem Server gespeichert werden.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Nach der Konfiguration bestätigt BTCPAY SERVER, dass Ihr Wallet bereit ist, On-Chain-Zahlungen zu akzeptieren.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Lightning Network aktivieren



Um sofortige Lightning-Zahlungen zu akzeptieren, gehen Sie zu Wallets > Lightning. Da Ihr LND-Knoten bereits auf Umbrel installiert ist, klicken Sie einfach auf die Schaltfläche "Speichern", um die Verbindung zwischen Ihrem BTCPAY SERVER und Ihrem LIGHTNING NODE zu bestätigen.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Rechnungen erstellen und bezahlen



Navigieren Sie in Interface BTCPAY SERVER zu Rechnungen > Erstellen Invoice. Geben Sie den Betrag ein, fügen Sie eine optionale Beschreibung hinzu, und klicken Sie auf Erstellen.



![Création d'une nouvelle facture](assets/fr/10.webp)



Sie können dann auf die Schaltfläche "Checkout" klicken, um den Invoice anzuzeigen. BTCPay generiert dann einen Invoice mit einem einheitlichen QR-Code (BIP21), der den Bitcoin Address und den Lightning Invoice enthält.



![Détails de la facture générée](assets/fr/11.webp)



Ihr Kunde kann den QR-Code mit jedem kompatiblen Wallet scannen.



![Page de paiement avec QR code](assets/fr/12.webp)



Sobald die Zahlung erfolgt ist, wird der Invoice in Sekundenschnelle für Lightning "abgerechnet".



![Confirmation de paiement réussi](assets/fr/13.webp)



## Zahlungsmanagement und -verfolgung



In der Rubrik "Berichte", Registerkarte "Rechnungen", finden Sie eine vollständige Übersicht über Ihre Rechnungen mit Datum, Betrag, Status und Zahlungsmethode. Sie können sie bei Bedarf exportieren.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Konfiguration speichern



Mit BTCPAY SERVER können Sie mehrere Geschäfte mit unterschiedlichen Parametern verwalten. Jeder Shop stellt eine separate Geschäftseinheit dar: E-Commerce-Shop, physische Verkaufsstelle oder Dienstleistungsabrechnung.



In den Shop-Einstellungen finden Sie mehrere wichtige Bereiche:



![Paramètres du magasin](assets/fr/15.webp)





- Allgemeine Einstellungen**: Shopname, Referenzwährung (BTC, EUR, USD), Invoice Ablaufzeit (Standard 15 Minuten), Anzahl der erforderlichen Blockchain Bestätigungen
- Kurse**: Konfiguration von Exchange Kursquellen und fiat/Bitcoin Umrechnungen
- Erscheinungsbild der Kasse**: Passen Sie das Aussehen Ihrer Kassenseiten an (Logo, Farben, personalisierte Nachrichten)
- E-Mail-Einstellungen**: Konfiguration von E-Mail-Benachrichtigungen für Zahlungseingänge
- Zugangs-Token**: API token-Verwaltung für E-Commerce-Integrationen (WooCommerce, Shopify, etc.)
- Benutzer**: Verwalten Sie den Benutzerzugriff auf den Shop mit verschiedenen Berechtigungsstufen (Eigentümer, Gast)
- Webhaken**: Webhook-Konfiguration für die Echtzeit-Synchronisation mit Ihrem Buchhaltungs- oder ERP-System



BTCPAY SERVER bietet auch einen Plugin-Bereich zur Erweiterung der Funktionalität durch E-Commerce-Integrationen, Kassensysteme und zusätzliche Tools.



![Gestion des plugins](assets/fr/16.webp)



## Vorteile und Grenzen der lokalen Nutzung



**Vorteile von BTCPAY SERVER auf Umbrel** :




- Völlige Souveränität: Ausschließliche Kontrolle über private Schlüssel und Gelder, keine dritte Partei kann Ihre Zahlungen einfrieren oder zensieren
- Erhebliche Einsparungen: nur Bitcoin Netzwerkkosten (ein paar Cent bei Lightning) im Vergleich zu 2-3% bei herkömmlichen Prozessoren
- Maximale Vertraulichkeit: keine Registrierung, Identitätsüberprüfung oder Datenweitergabe an Drittunternehmen
- Die Open-Source-Architektur garantiert Transparenz, Überprüfbarkeit und Nachhaltigkeit durch eine große Gemeinschaft von Entwicklern
- Einfache Installation über Umbrel, keine technischen Vorkenntnisse erforderlich



**Wichtige Einschränkungen** :




- Nur lokales Netzwerk**: BTCPAY SERVER auf Umbrel ist nur von Ihrem Heimnetzwerk aus zugänglich. Perfekt für persönliche Abrechnungen, freiberufliche Dienstleistungen oder kleine physische Geschäfte, aber nicht geeignet für Online-Shops, die öffentlich im Internet zugänglich sind.
- Volle technische Verantwortung: Wartung der Knoten, regelmäßige Backups, Überwachung der Konnektivität
- Blitzliquiditätsmanagement: Eröffnung und Verwaltung von Kanälen mit ausreichender Eingangskapazität
- Der Support beschränkt sich auf Community-Dokumentation und Foren und erfordert mehr Autonomie als eine kommerzielle Kundendienstabteilung



Diese LAN-Beschränkung ist das Haupthindernis für die Integration von BTCPAY SERVER in ein E-Commerce-Geschäft, bei dem die Kunden in der Lage sein müssen, von überall im Internet auf die Zahlungsseiten zuzugreifen.



## Bewährte Praktiken und Sicherheit



Aktivieren Sie automatische Umbrel-Backups und speichern Sie eine Kopie auf einem externen Medium (USB-Stick, Hard-Diskette, verschlüsselte Cloud). Bewahren Sie Ihre Bitcoin Seeds (Wiederherstellungsphrasen) an einem sicheren, physisch getrennten Ort auf. Speichern Sie die LND channel.backup Datei für die Lightning-Wiederherstellung.



Überprüfen Sie regelmäßig die Bitcoin core-Synchronisation, die Blitzkanäle und die Reaktion des BTCPAY SERVER. Ein einfacher wöchentlicher Test: generate und bezahlen Sie eine Rechnung über ein paar Satoshis. Halten Sie Umbrel auf dem neuesten Stand (Sicherheitspatches, Verbesserungen). Machen Sie ein Backup vor größeren Aktualisierungen. Für den professionellen Einsatz sollten Sie eine externe Überwachung (UptimeRobot) mit E-Mail/SMS-Warnungen in Betracht ziehen.



## BTCPAY SERVER öffentlich für einen Online-Shop anzeigen



Um BTCPAY SERVER in einen webbasierten E-Commerce-Shop (WooCommerce, Shopify usw.) zu integrieren, müssen Ihre Kunden in der Lage sein, von überall auf die Zahlungsseiten zuzugreifen, nicht nur von Ihrem lokalen Netzwerk aus.



**Lösung: Nginx Proxy Manager**



Sie können den BTCPAY SERVER öffentlich zugänglich machen, indem Sie den Nginx Proxy Manager verwenden (erhältlich im Umbrel App Store). Diese Lösung erfordert :




- Ein Domänenname (klassisch oder kostenlos über DuckDNS, No-IP, Afraid.org)
- Konfigurieren der Portweiterleitung (Ports 80 und 443) auf Ihrem Router
- Installation von Nginx Proxy Manager, der automatisch SSL-Zertifikate verwaltet



Diese Konfiguration setzt Ihren Server dem Internet aus und erfordert zusätzliche Wachsamkeit (starke Passwörter, 2FA, regelmäßige Updates). Wir werden ein spezielles Tutorial vorbereiten, in dem dieses Verfahren ausführlich beschrieben wird.



## Schlussfolgerung



BTCPAY SERVER on Umbrel kombiniert die Leistung des Bitcoin Knotens mit der Einfachheit von Umbrel, um eine selbstgehostete professionelle Zahlungsinfrastruktur zu schaffen, die für alle zugänglich ist. Diese finanzielle Souveränität geht mit einer Wartungsverantwortung einher, aber Umbrel vereinfacht die betriebliche Belastung im Vergleich zu den Vorteilen: Beseitigung von Bearbeitungsgebühren, Schutz Ihrer Privatsphäre, Widerstand gegen Zensur und totale Kontrolle über Ihre Gelder.



Die Nutzung des lokalen Netzwerks deckt bereits eine breite Palette von Anwendungen ab: Abrechnung von freiberuflichen Dienstleistungen, persönliche Zahlungen, kleine physische Geschäfte oder einfach nur das Lernen und Experimentieren mit Bitcoin und Lightning in einer kontrollierten Umgebung. Für E-Commerce-Bedürfnisse, die ein öffentliches Engagement erfordern, gibt es die Nginx Proxy Manager-Lösung, die jedoch zusätzliche technische Konfigurationen erfordert, die wir in einem eigenen Tutorial näher erläutern werden.



Ob Sie nun ein Unternehmen betreiben, ein junges Projekt oder einfach nur experimentieren, BTCPAY SERVER on Umbrel bietet Ihnen völlige finanzielle Autonomie. Der Weg beginnt mit einem ersten Geschäft, einem ersten Invoice, einer ersten Zahlung, die direkt in Ihre souveräne Infrastruktur fließt.



## Ressourcen



### Offizielle Dokumentation




- [BTCPAY SERVER offizielle Website](https://btcpayserver.org)
- [Vollständige BTCPAY SERVER-Dokumentation](https://docs.btcpayserver.org)
- [GitHub BTCPAY SERVER](https://github.com/btcpayserver/btcpayserver)
- [Tailscale-Dokumentation](https://tailscale.com/kb)


### Gemeinschaft und Unterstützung




- [Forum BTCPAY SERVER] (https://chat.btcpayserver.org)
- [Forum Umbrella] (https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)