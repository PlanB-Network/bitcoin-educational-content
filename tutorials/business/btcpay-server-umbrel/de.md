---
name: BTCPay Server - Umbrel
description: Installation und Verwendung von BTCPay Server auf Umbrel, um Bitcoin und Lightning zu akzeptieren
---

![cover](assets/cover.webp)



Im Bitcoin-Ökosystem stellt die Annahme von Zahlungen eine große Herausforderung für Händler und Unternehmen gleichermaßen dar. Herkömmliche Lösungen, ob Banken (Kreditkarten, Stripe, PayPal) oder sogar Bitcoin (BitPay, Coinbase Commerce), erzwingen Zwischenhändler, die erhebliche Gebühren erheben, Ihre sensiblen Geschäftsdaten sammeln und Ihre Transaktionen nach Lust und Laune blockieren oder zensieren können. Diese Abhängigkeit steht im Widerspruch zu den Grundprinzipien von Bitcoin: Dezentralisierung, Vertraulichkeit und finanzielle Souveränität.



BTCPay Server entwickelt sich zur Open-Source-Antwort auf dieses Problem. Dieser selbst gehostete Zahlungsprozessor verwandelt Ihren eigenen Bitcoin-Knoten in eine professionelle Infrastruktur, ohne Zwischenhändler, ohne zusätzliche Bearbeitungsgebühren und ohne Kompromisse beim Datenschutz. BTCPay Server wird seit 2017 von einer globalen Gemeinschaft von Mitwirkenden entwickelt und ermöglicht es Ihnen, Bitcoin- und Lightning-Zahlungen direkt in Ihren Wallets zu empfangen, wobei Sie jederzeit die volle Kontrolle über Ihre Gelder behalten.



Traditionell erfordert die Installation von BTCPay Server fortgeschrittene technische Kenntnisse: Linux-Server-Konfiguration, Beherrschung von Docker, Verwaltung von SSL-Zertifikaten und Netzwerksicherheit. Umbrel revolutioniert diesen Ansatz mit einer Ein-Klick-Installation, die direkt in Ihren Bitcoin und Lightning Node integriert ist. Diese Vereinfachung macht das, was bisher erfahrenen Technikern vorbehalten war, für jedermann zugänglich.



**Wichtig zu verstehen**: Der BTCPay Server auf Umbrel funktioniert standardmäßig nur in Ihrem lokalen Netzwerk. Sie können Rechnungen erstellen, Lightning- und Bitcoin-Zahlungen akzeptieren und Ihre Buchhaltung von jedem Gerät aus verwalten, das mit Ihrem Heimnetzwerk verbunden ist (Computer, Smartphone, Tablet). Diese Konfiguration ist ideal für die Abrechnung von persönlichen Dienstleistungen, die Verwaltung von persönlichen Zahlungen oder die Verwendung von BTCPay Server über Ihr lokales Netzwerk. Für die Integration von BTCPay Server in einen Online-Shop, der im Internet öffentlich zugänglich ist, ist hingegen eine zusätzliche Konfiguration mit öffentlichem Zugang erforderlich (wir werden dieses Thema am Ende des Tutorials behandeln).



Dieses Tutorial führt Sie durch die komplette Installation von BTCPay Server auf Umbrel, die Konfiguration Ihres Bitcoin wallet und Lightning Knotens, die Erstellung und Bezahlung von Rechnungen und die Verwaltung von Buchhaltungsberichten. Sie erfahren, wie Sie den BTCPay Server effizient in Ihrem lokalen Netzwerk nutzen können, und dann sehen wir uns Lösungen für die öffentliche Anzeige an, wenn Sie ihn in eine E-Commerce-Website integrieren möchten.



## Voraussetzungen



Um diesem Tutorial folgen zu können, müssen Sie Umbrel korrekt installiert und konfiguriert haben. Falls Sie dies noch nicht getan haben, lesen Sie bitte unser Tutorial zur Installation von Umbrel.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Ihr Bitcoin Core-Knoten muss vollständig mit der Blockchain synchronisiert werden (100% in der Bitcoin-Anwendung von Umbrel). Diese erste Synchronisation dauert in der Regel zwischen 3 Tagen und 2 Wochen, abhängig von Ihrer Hardware und Internetverbindung.



Um Lightning-Zahlungen zu akzeptieren, müssen Sie auch LND (Lightning Network Daemon) auf Umbrel installieren. Siehe unser Tutorial zur Installation und Konfiguration von LND auf Umbrel, wenn Sie diese Funktion aktivieren möchten.



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Sie sollten mindestens 50 GB freien Speicherplatz für den BTCPay-Server, seine Datenbanken und Lightning-Daten zur Verfügung stellen. Eine stabile Internetverbindung über ein Ethernet-Kabel wird dringend empfohlen, um Verbindungsunterbrechungen zu vermeiden.



## Installation des BTCPay-Servers auf Umbrel



Rufen Sie über die Umbrel-Schnittstelle (`umbrel.local`) den App Store auf und suchen Sie nach "BTCPay Server" in der Kategorie Bitcoin.



![Interface Umbrel App Store avec BTCPay Server](assets/fr/01.webp)



Klicken Sie auf Installieren. Umbrel prüft automatisch, ob Bitcoin Core und LND installiert sind und beginnt dann mit der Installation (2-5 Minuten).



![Dépendances requises pour BTCPay Server](assets/fr/02.webp)



Nach der Installation öffnen Sie die Anwendung. Sie müssen ein Administratorkonto mit sicheren Anmeldedaten erstellen.



![Création du compte administrateur BTCPay Server](assets/fr/03.webp)



Sobald Ihr Konto erstellt wurde, werden Sie von BTCPay Server sofort aufgefordert, Ihr erstes Geschäft einzurichten. Wählen Sie einen Geschäftsnamen und eine Referenzwährung (EUR, USD oder BTC).



![Création du premier magasin BTCPay Server](assets/fr/04.webp)



## Zugang zum BTCPay Server in Ihrem lokalen Netzwerk



BTCPay Server ist von jedem Gerät in Ihrem lokalen Netzwerk (WiFi oder Ethernet) zugänglich. Zugriff über Ihren Browser auf :



```url
http://umbrel.local
```



Oder direkt an :



```url
http://umbrel.local:3003
```



**Fernzugriff mit Tailscale**: Um von überall auf der Welt auf den BTCPay Server zuzugreifen, verwenden Sie Tailscale. Mit diesem sicheren VPN können Sie sich mit Ihrem Umbrel verbinden, als ob Sie sich in Ihrem lokalen Netzwerk befinden würden. Siehe unser Tutorial zu Tailscale auf Umbrel.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

## Konfigurieren Sie Ihr Bitcoin-Portfolio



Um Zahlungen zu akzeptieren, müssen Sie einen Bitcoin wallet konfigurieren. BTCPay Server zeigt die Konfigurationsoptionen im Dashboard an.



![Tableau de bord avec options de configuration de portefeuille](assets/fr/05.webp)



Um wallet Bitcoin zu konfigurieren, gehen Sie zu "Geldbörsen" > "Bitcoin".



Sie haben zwei Möglichkeiten: Sie können ein neues Portfolio direkt in BTCPay erstellen oder ein bestehendes Portfolio importieren. Für den Import stehen mehrere Methoden zur Verfügung:




- Schließen Sie die Hardware wallet** an (empfohlen): Importieren Sie Ihre öffentlichen Schlüssel über die Vault-Anwendung
- wallet-Datei importieren** (empfohlen): Laden Sie eine exportierte Datei aus Ihrem Portfolio hoch
- Erweiterten öffentlichen Schlüssel eingeben**: Geben Sie Ihren XPub/YPub/ZPub manuell ein
- wallet QR-Code scannen** : Scannen eines QR-Codes von BlueWallet, Cobo Vault, Passport oder Specter DIY
- Geben Sie wallet seed** (nicht empfohlen) ein: Geben Sie Ihre 12- oder 24-Wort-Wiederherstellungsphrase ein



![Options de création de portefeuille](assets/fr/06.webp)



Für dieses Tutorial werden wir ein neues Hot wallet erstellen: der private Schlüssel wird also auf unserem Umbrel-Server gespeichert. In diesem Fall raten wir Ihnen dringend, die Gelder regelmäßig auf einen kalten wallet zu verschieben, um zu vermeiden, dass große Beträge auf dem Server gespeichert werden.



![Choix entre Hot wallet et Watch-only wallet](assets/fr/07.webp)



Nach der Konfiguration bestätigt der BTCPay-Server, dass Ihr wallet bereit ist, on-chain-Zahlungen zu akzeptieren.



![Portefeuille Bitcoin configuré avec succès](assets/fr/08.webp)



## Aktivieren Sie Lightning Network



Um sofortige Lightning-Zahlungen zu akzeptieren, gehen Sie zu Wallets > Lightning. Da Ihr LND-Knoten bereits auf Umbrel eingerichtet ist, klicken Sie einfach auf die Schaltfläche "Speichern", um die Verbindung zwischen Ihrem BTCPay-Server und Ihrem Lightning-Knoten zu bestätigen.



![Configuration du nœud Lightning](assets/fr/09.webp)



## Rechnungen erstellen und bezahlen



Navigieren Sie in der BTCPay Server-Oberfläche zu Rechnungen > Invoice erstellen. Geben Sie den Betrag ein, fügen Sie eine optionale Beschreibung hinzu, und klicken Sie auf Erstellen.



![Création d'une nouvelle facture](assets/fr/10.webp)



Sie können dann auf die Schaltfläche "Zur Kasse gehen" klicken, um die Rechnung anzuzeigen. BTCPay erstellt dann eine Rechnung mit einem einheitlichen QR-Code (BIP21), der die Bitcoin-Adresse und die Lightning-Rechnung enthält.



![Détails de la facture générée](assets/fr/11.webp)



Ihr Kunde kann den QR-Code mit jedem kompatiblen wallet scannen.



![Page de paiement avec QR code](assets/fr/12.webp)



Sobald die Rechnung bezahlt ist, wird sie für Lightning in Sekundenschnelle "beglichen".



![Confirmation de paiement réussi](assets/fr/13.webp)



## Zahlungsmanagement und -verfolgung



In der Rubrik "Berichte", Registerkarte "Rechnungen", finden Sie eine vollständige Übersicht über Ihre Rechnungen mit Datum, Betrag, Status und Zahlungsmethode. Sie können sie bei Bedarf exportieren.



![Section reporting avec l'historique des factures](assets/fr/14.webp)



## Konfiguration speichern



BTCPay Server ermöglicht es Ihnen, mehrere Shops mit unterschiedlichen Parametern zu verwalten. Jeder Shop stellt eine separate Geschäftseinheit dar: E-Commerce-Shop, physische Verkaufsstelle oder Dienstleistungsabrechnung.



In den Shop-Einstellungen finden Sie mehrere wichtige Bereiche:



![Paramètres du magasin](assets/fr/15.webp)





- Allgemeine Einstellungen**: Shop-Name, Referenzwährung (BTC, EUR, USD), Ablaufzeit der Rechnung (Standard 15 Minuten), Anzahl der erforderlichen Blockchain-Bestätigungen
- Kurse**: Konfiguration von Wechselkursquellen und Fiat/Bitcoin-Umrechnungen
- Erscheinungsbild der Kasse**: Passen Sie das Aussehen Ihrer Kassenseiten an (Logo, Farben, personalisierte Nachrichten)
- E-Mail-Einstellungen**: Konfiguration von E-Mail-Benachrichtigungen für Zahlungseingänge
- Zugangs-Token**: Verwaltung von API-Tokens für E-Commerce-Integrationen (WooCommerce, Shopify, etc.)
- Benutzer**: Verwalten Sie den Benutzerzugriff auf den Shop mit verschiedenen Berechtigungsstufen (Eigentümer, Gast)
- Webhaken**: Webhook-Konfiguration für die Echtzeit-Synchronisation mit Ihrem Buchhaltungs- oder ERP-System



BTCPay Server bietet auch einen Plugin-Bereich, um die Funktionalität mit E-Commerce-Integrationen, Point-of-Sale-Systemen und zusätzlichen Tools zu erweitern.



![Gestion des plugins](assets/fr/16.webp)



## Vorteile und Grenzen der lokalen Nutzung



**Vorteile von BTCPay Server gegenüber Umbrel** :




- Völlige Souveränität: Ausschließliche Kontrolle über private Schlüssel und Gelder, keine dritte Partei kann Ihre Zahlungen einfrieren oder zensieren
- Erhebliche Einsparungen: nur Bitcoin Netzwerkkosten (ein paar Cent bei Lightning) im Vergleich zu 2-3% bei herkömmlichen Prozessoren
- Maximale Vertraulichkeit: keine Registrierung, Identitätsüberprüfung oder Datenweitergabe an Drittunternehmen
- Die Open-Source-Architektur garantiert Transparenz, Überprüfbarkeit und Nachhaltigkeit durch eine große Gemeinschaft von Entwicklern
- Einfache Installation über Umbrel, keine technischen Vorkenntnisse erforderlich



**Wichtige Einschränkungen** :




- Nur lokales Netzwerk**: Der BTCPay Server auf Umbrel ist nur von Ihrem Heimnetzwerk aus zugänglich. Perfekt für die Abrechnung von Angesicht zu Angesicht, freiberufliche Dienstleistungen oder kleine physische Geschäfte, aber ungeeignet für öffentlich zugängliche Online-Shops.
- Volle technische Verantwortung: Wartung der Knoten, regelmäßige Backups, Überwachung der Konnektivität
- Blitzliquiditätsmanagement: Eröffnung und Verwaltung von Kanälen mit ausreichender Eingangskapazität
- Der Support beschränkt sich auf Community-Dokumentation und Foren und erfordert mehr Autonomie als eine kommerzielle Kundendienstabteilung



Diese Einschränkung des lokalen Netzwerks ist das Haupthindernis für die Integration von BTCPay Server in ein E-Commerce-Geschäft, bei dem die Kunden in der Lage sein müssen, von überall im Internet auf die Zahlungsseiten zuzugreifen.



## Bewährte Praktiken und Sicherheit



Aktivieren Sie automatische Umbrel-Backups und speichern Sie eine Kopie auf einem externen Medium (USB-Stick, Festplatte, verschlüsselte Cloud). Bewahren Sie Ihre Bitcoin Seeds (Wiederherstellungsphrasen) an einem sicheren, physisch getrennten Ort auf. Sichern Sie die channel.backup-Datei von LND für die Wiederherstellung von Lightning.



Überwachen Sie regelmäßig die Bitcoin Core-Synchronisation, die Lightning-Kanäle und die Reaktion des BTCPay-Servers. Ein einfacher wöchentlicher Test: generate und eine Rechnung über ein paar Satoshis bezahlen. Halten Sie Umbrel auf dem neuesten Stand (Sicherheitspatches, Erweiterungen). Machen Sie ein Backup vor größeren Updates. Für den professionellen Einsatz sollten Sie eine externe Überwachung (UptimeRobot) mit E-Mail/SMS-Warnungen in Betracht ziehen.



## BTCPay Server öffentlich zugänglich machen für einen Online-Shop



Um BTCPay Server in einen webbasierten E-Commerce-Shop (WooCommerce, Shopify usw.) zu integrieren, müssen Ihre Kunden von überall aus auf die Zahlungsseiten zugreifen können, nicht nur von Ihrem lokalen Netzwerk aus.



**Lösung: Nginx Proxy Manager**



Sie können den BTCPay Server öffentlich zugänglich machen, indem Sie den Nginx Proxy Manager verwenden (erhältlich im Umbrel App Store). Diese Lösung erfordert :




- Ein Domänenname (klassisch oder kostenlos über DuckDNS, No-IP, Afraid.org)
- Konfigurieren der Portweiterleitung (Ports 80 und 443) auf Ihrem Router
- Installation von Nginx Proxy Manager, der automatisch SSL-Zertifikate verwaltet



Diese Konfiguration setzt Ihren Server dem Internet aus und erfordert zusätzliche Wachsamkeit (starke Passwörter, 2FA, regelmäßige Updates). Wir werden ein spezielles Tutorial vorbereiten, in dem dieses Verfahren ausführlich beschrieben wird.



## Schlussfolgerung



BTCPay Server on Umbrel kombiniert die Leistungsfähigkeit des Bitcoin Knotens mit der Einfachheit von Umbrel, um eine selbstgehostete, professionelle Zahlungsinfrastruktur zu schaffen, die für alle zugänglich ist. Diese finanzielle Souveränität geht mit einer Wartungsverantwortung einher, aber Umbrel vereinfacht die betriebliche Belastung im Vergleich zu den Vorteilen erheblich: Beseitigung von Bearbeitungsgebühren, Schutz Ihrer Privatsphäre, Widerstand gegen Zensur und totale Kontrolle über Ihre Gelder.



Die Nutzung des lokalen Netzwerks deckt bereits eine breite Palette von Anwendungen ab: Abrechnung von freiberuflichen Dienstleistungen, persönliche Zahlungen, kleine physische Geschäfte oder einfach nur das Lernen und Experimentieren mit Bitcoin und Lightning in einer kontrollierten Umgebung. Für E-Commerce-Bedürfnisse, die ein öffentliches Engagement erfordern, gibt es die Nginx Proxy Manager-Lösung, die jedoch zusätzliche technische Konfigurationen erfordert, die wir in einem speziellen Tutorial näher erläutern werden.



Egal, ob Sie ein Unternehmen betreiben, ein junges Projekt oder einfach nur experimentieren, BTCPay Server on Umbrel bietet Ihnen völlige finanzielle Autonomie. Der Weg beginnt mit Ihrem ersten Shop, Ihrer ersten Rechnung, Ihrer ersten Zahlung, die direkt in Ihrer souveränen Infrastruktur eingeht.



## Ressourcen



### Offizielle Dokumentation




- [Offizielle BTCPay Server Webseite](https://btcpayserver.org)
- [Vollständige BTCPay Server Dokumentation](https://docs.btcpayserver.org)
- [GitHub BTCPay Server](https://github.com/btcpayserver/btcpayserver)
- [Tailscale-Dokumentation](https://tailscale.com/kb)


### Gemeinschaft und Unterstützung




- [Forum BTCPay Server](https://chat.btcpayserver.org)
- [Forum Umbrella] (https://community.getumbrel.com)
- [Reddit r/BTCPayServer](https://reddit.com/r/BTCPayServer)