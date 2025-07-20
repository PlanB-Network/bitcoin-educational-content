---
name: Regenschirm
description: Entdecken und installieren Sie Umbrel - Ihren Bitcoin-Knoten und Heimserver
---

![cover](assets/cover.webp)



## Einführung



### Was ist ein Bitcoin-Knoten?



Ein Bitcoin-Knoten ist ein Computer, der am Bitcoin-Netz teilnimmt, indem er die Software Bitcoin Core oder einen alternativen Client ausführt. Seine Rolle ist wesentlich für den Betrieb und die Sicherheit des Netzes:





- Blockchain-Speicher**: Bewahrt eine vollständige, aktuelle Kopie des Blockchain Bitcoin
- Transaktionsüberprüfung**: validiert jede Transaktion und jeden Block gemäß den Protokollregeln
- Weitergabe von Informationen**: Teilt neue Transaktionen und Blöcke mit anderen Knotenpunkten
- Konsensbildung**: Trägt zur Anwendung der Netzregeln bei



Der Betrieb eines eigenen Bitcoin-Knotens ist ein entscheidender Schritt auf dem Weg zur finanziellen Souveränität und bietet mehrere entscheidende Vorteile:





- Vertraulichkeit**: Teilen Sie Ihre Transaktionen, ohne Ihre Informationen an Dritte weiterzugeben
- Widerstand gegen Zensur**: Niemand kann Sie davon abhalten, Bitcoin zu benutzen
- Unabhängige Überprüfung**: Sie müssen sich bei der Verifizierung Ihrer Transaktionen nicht auf die Knotenpunkte anderer Personen verlassen
- Konsensbildung**: Beitrag zur Anwendung der Bitcoin-Netzregeln
- Netzwerk-Unterstützung**: Werden Sie ein aktiver Teilnehmer an der Verteilung und Dezentralisierung des Netzes



### Umbrel: Eine einfache Lösung für den Betrieb eines Bitcoin-Knotens



Umbrel ist ein Open-Source-Betriebssystem, das die Installation und Verwaltung eines Bitcoin-Knotens vereinfacht. Außerdem verwandelt es Ihren Computer in einen persönlichen und privaten Heimserver, der es einfach macht, :





- Ein vollständiger Bitcoin-Knoten
- Bitcoin wesentliche Anwendungen (Electrs, Mempool.space)
- Andere persönliche Dienste (Cloud-Speicher, Streaming, VPN, usw.)



Mit seinem eleganten und intuitiven Interface Benutzer Interface macht Umbrel selbst gehostete Dienste für alle zugänglich, während Sie die volle Kontrolle über Ihre Daten behalten.



## Optionen für die Installation des Schirms



Umbrel bietet zwei Möglichkeiten, seine Lösung zu nutzen: eine schlüsselfertige Option (Umbrel Home) und eine kostenlose Open-Source-Version (UmbrelOS).



![Comparaison Umbrel Home et UmbrelOS](assets/fr/22.webp)



### Umbrel Home: Die schlüsselfertige Lösung



Umbrel Home ist ein vorkonfigurierter Heimserver, der speziell für ein optimales Erlebnis entwickelt wurde. Diese All-in-One-Hardware-Lösung umfasst:



**Hardware-Merkmale**




- Leistungsstarker Prozessor, optimiert für Self-Hosting
- Vorinstallierter Hochgeschwindigkeits-SSD-Speicher
- Geräuscharmes Kühlsystem
- Kompaktes, elegantes Design
- Integrierte USB- und Ethernet-Anschlüsse



**Exklusive Vorteile**




- Plug-and-Play-Installation: einstecken und loslegen
- Premium-Support mit engagierter Unterstützung
- Garantierte automatische Aktualisierungen
- Integrierter Migrationsassistent
- Volle Hardware-Garantie
- Volle Unterstützung für alle Funktionalitäten



**Preis**: 399 € (Preis kann je nach Saison variieren)



### UmbrelOS: Die Open-Source-Version



UmbrelOS ist die freie, quelloffene Version des Umbrel-Betriebssystems. Mit dieser flexiblen Lösung können Sie Ihre eigene Hardware verwenden und gleichzeitig von den wesentlichen Funktionen von Umbrel profitieren.



**Vorteile**




- Völlig unentgeltlich
- Offener, überprüfbarer Quellcode
- Freiheit der Wahl
- Erweiterte Anpassungsoptionen



**Unterstützte Plattformen**




- Raspberry Pi 5: Eine beliebte und erschwingliche Lösung
- X86-Systeme: Für Standard-PCs oder Server
- Virtuelle Maschine: Zum Testen oder zur Verwendung in einer bestehenden Infrastruktur



**Einschränkungen




- Nur Gemeinschaftsunterstützung
- Einige erweiterte Funktionen sind Umbrel Home vorbehalten
- Mehr technische Erstkonfiguration
- Leistung hängt von der gewählten Hardware ab



Diese Version ist ideal für :




- Technische Benutzer
- Diejenigen, die bereits kompatible Geräte besitzen
- Menschen, die lernen und experimentieren wollen
- Entwickler, die zu dem Projekt beitragen möchten



Offizielle Installationslinks :




- [Installation auf Raspberry Pi 5](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- [Installation auf x86-Systemen (https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-x86-Systems)
- [Installation einer virtuellen Maschine](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Linux-VM)



In diesem Tutorial werden wir uns auf die Installation von UmbrelOS auf einem Raspberry Pi 5 konzentrieren, aber die Grundprinzipien sind auch für andere Plattformen ähnlich.



## Installation von Umbrel OS auf dem Raspberry Pi 5



### Erforderliche Komponenten



Für diese Installation benötigen Sie :





- Raspberry Pi 5 (4 GB oder 8 GB RAM)
- Ein offizieller Raspberry Pi Power Supply (wichtig für die Stabilität!)
- MicroSD-Karte (mindestens 32 GB)
- Ein microSD-Kartenlesegerät
- Eine externe SSD zur Datenspeicherung
- Ethernet-Kabel
- Ein USB-Kabel zum Anschließen der SSD



### Installationsschritte



**Download UmbrelOS**



![Téléchargement UmbrelOS](assets/fr/01.webp)




- Besuchen Sie die [offizielle Website](https://github.com/getumbrel/umbrel/wiki/Install-umbrelOS-on-a-Raspberry-Pi-5)
- Laden Sie die neueste Version von UmbrelOS für Raspberry Pi 5 herunter



**Balena Etcher** Installation



![Téléchargement Balena Etcher](assets/fr/02.webp)




- Laden Sie [Balena Etcher](https://www.balena.io/etcher/) herunter und installieren Sie es auf Ihrem Computer



**Vorbereiten der microSD**-Karte



![Insertion carte microSD](assets/fr/03.webp)




- Stecken Sie Ihre microSD-Karte in den Kartenleser Ihres Computers



**Bild blinkend**



![Flashage UmbrelOS](assets/fr/04.webp)




- Start Balena Etcher
- Wählen Sie das heruntergeladene UmbrelOS-Image
- Wählen Sie Ihre microSD-Karte als Ziel
- Klicken Sie auf "Flash!" und warten Sie, bis der Vorgang abgeschlossen ist
- Sicheres Auswerfen der Karte



**Einbau der microSD-Karte



![Installation microSD](assets/fr/05.webp)




- Setzen Sie die microSD-Karte in Ihren Raspberry Pi 5 ein



**Peripherieanschluss**



![Connexion périphériques](assets/fr/06.webp)




- Schließen Sie die externe SSD an einen freien USB-Anschluss an
- Verbinden Sie das Ethernet-Kabel zwischen dem Pi und Ihrem Router



**Einschalten



![Démarrage du Pi](assets/fr/07.webp)




- Schließen Sie das offizielle Raspberry Pi-Netzteil Supply an
- Warten Sie ein paar Minuten, bis das System hochgefahren ist



**Erster Zugang**



![Accès interface web](assets/fr/08.webp)




- Öffnen Sie auf einem Gerät, das mit demselben Netzwerk verbunden ist, Ihren Browser
- Zugang zur Interface-Website von Umbrel unter: `http://umbrel.local`



![Page d'accueil Umbrel](assets/fr/09.webp)



Wenn `umbrel.local` nicht funktioniert, musst du die IP Address deines Raspberry Pi in deinem lokalen Netzwerk finden. Sie können :




- Konsultieren Sie das Interface Ihres Routers
- Verwendung eines Netzwerkscanners wie nmap
- Verwenden Sie den Befehl `arp -a` im Terminal Ihres Computers



## Erster Schritt auf Umbrel



Sobald Ihr Umbrel gestartet und über Ihren Browser zugänglich ist, folgen Sie diesen Schritten, um loszulegen:



### Erstmalige Konfiguration



**Erstellen Sie Ihr Konto**



![Création compte](assets/fr/10.webp)




- Wählen Sie einen Benutzernamen
- Ein sicheres Passwort festlegen
- Für den Zugang zu Ihrem Umbrel benötigen Sie diese Anmeldedaten



**Kontobestätigung



![Confirmation compte](assets/fr/11.webp)




- Klicken Sie auf "Weiter", um Ihr Dashboard aufzurufen



**Entdeckung des Interface**



![Interface Umbrel](assets/fr/12.webp)




- Zugriff auf den Umbrel App Store
- Entdecken Sie die vielen verfügbaren Anwendungen
- Beginnen wir mit der Installation der wichtigsten Anwendungen für Bitcoin



### Installation von Bitcoin-Anwendungen



**Bitcoin-Knoten**



![Bitcoin Node](assets/fr/13.webp)




- Erste zu installierende Anwendung
- Herunterladen und Überprüfen des gesamten Blockchain Bitcoin



**Wähler*



![Installation Electrs](assets/fr/14.webp)




- Electrum-Server für die Verbindung von Bitcoin-Geldbörsen
- Synchronisierung mit Ihrem Bitcoin-Knoten



**Mempool**



![Installation Mempool](assets/fr/15.webp)




- Interface Anzeige für Blockchain
- Verfolgt Transaktionen und Blöcke in Echtzeit



## Verfolgung einer Transaktion mit Mempool.space



Mempool.space ist ein Open-Source-Blockchain-Explorer, der das Bitcoin-Netzwerk in Echtzeit visualisiert. Damit können Sie Ihre Transaktionen verfolgen und verstehen, wie sich Transaktionen im Netzwerk ausbreiten.



### Verstehen von Mempool und Bestätigungen



Der "Mempool" (Speicherpool) ist wie ein virtueller Warteraum, in dem alle unbestätigten Bitcoin-Transaktionen gespeichert werden, bevor sie in einen Block aufgenommen werden. So wird eine Transaktion verarbeitet:



1. **Broadcast**: Wenn Sie eine Transaktion senden, wird sie zunächst im Bitcoin-Netz übertragen


2. **Wartend in Mempool**: Wartet darauf, von einem Miner auf der Grundlage der Kosten ausgewählt zu werden


3. **Erste Bestätigung**: Ein Minderjähriger fügt sie in einen Block ein (1. Bestätigung)


4. **Zusätzliche Bestätigungen**: Jeder neue Block, der nach dem Block, der Ihre Transaktion enthält, geschürft wird, fügt eine Bestätigung hinzu



Die empfohlene Anzahl der Bestätigungen hängt von der Menge ab:




- Für kleine Beträge: 1-2 Bestätigungen können ausreichen
- Für große Beträge: 6 Bestätigungen gelten im Allgemeinen als sehr sicher



### Erkunden Sie Interface von Mempool.space



1. **Die Startseite** gibt Ihnen einen Überblick über das Bitcoin-Netz:




   - Kürzlich abgebaute Blöcke
   - Kostenschätzungen für verschiedene Prioritäten
   - Der aktuelle Stand von Mempool



![Page d'accueil de Mempool.space avec visualisation des blocs et estimations de frais](assets/fr/23.webp)



2. **Suchen Sie nach einer Transaktion**: Um eine bestimmte Transaktion zu verfolgen, geben Sie ihre Kennung (txid) in die Suchleiste oben auf der Seite ein.



![Recherche d'une transaction dans Mempool.space](assets/fr/24.webp)



### Analysieren Sie Transaktionsdetails



Sobald Ihre Transaktion gefunden wurde, präsentiert Mempool.space Ihnen eine vollständige Analyse:



1. **Wesentliche Informationen** :




   - Status (bestätigt oder nicht)
   - Bezahlte Kosten (in Sats/vB)
   - Geschätzte Bestätigungszeit



![Détails des frais et statut de la transaction](assets/fr/25.webp)



2. **Transaktionsstruktur** :




   - Visuelle Darstellung von Eingängen und Ausgängen
   - Detaillierte Liste der betroffenen Adressen
   - Übertragene Beträge



3. **Technische Daten** :




   - Gewicht des Vorgangs
   - Virtuelle Größe
   - Format und verwendete Version
   - Andere spezifische Metadaten



![Informations techniques et structure des entrées/sorties](assets/fr/26.webp)



### Vorteile der Verwendung von Mempool.space auf Umbrel



1. **Vertraulichkeit**: Ihre Anfragen gehen über Ihren eigenen Knotenpunkt


2. **Unabhängigkeit**: Keine Abhängigkeit von einem Drittanbieterdienst


3. **Zuverlässigkeit**: Zugriff auf Daten auch bei Ausfall der öffentlichen Browser



Mit dieser Anwendung können Sie Ihre Transaktionen effizient überwachen, verstehen, wie sich Gebühren auf die Bestätigungsgeschwindigkeit auswirken, und erhalten ein besseres Verständnis für die Funktionsweise des Bitcoin-Netzwerks.



## Anschließen eines Wallet Bitcoin an Ihren Knoten



### Elektronische Konfiguration



**Lokale Verbindung



![Connexion locale](assets/fr/18.webp)




- Zur Verwendung in Ihrem lokalen Netzwerk
- Schneller und einfacher einzurichten



**Fernverbindung über Tor**



![Connexion Tor](assets/fr/19.webp)




- So greifen Sie von überall auf Ihren Knoten zu
- Mehr Sicherheit und Privatsphäre



### Verbindung mit Sparrow Wallet



**Zugang zu Parametern



![Paramètres Sparrow](assets/fr/20.webp)




- Offener Sperling Wallet
- Gehen Sie zu Präferenzen > Server
- Klicken Sie auf "Bestehende Verbindung ändern"



**Wahl der Verbindungsart



Sparrow bietet drei Verbindungsmodi:



***Öffentlicher Server***




- Verbindung zu öffentlichen Servern (z. B. blockstream.info, Mempool.space)
- Einfach, aber weniger privat



***Bitcoin Kern***




- Direkte Verbindung zu einem Bitcoin-Knoten
- Privat, aber langsamer



***Privat Electrum***




- Verbinden Sie sich mit Ihrem Electrs-Server
- Kombiniert Vertraulichkeit und Leistung



**Electrs** Konfiguration



Wählen Sie Ihre Verbindungsart anhand der Informationen, die in der Electrs-Anwendung angezeigt werden, die wir bereits gesehen haben:



In beiden Fällen lassen Sie die Optionen "SSL verwenden" und "Proxy verwenden" unmarkiert.



**Lokale Verbindung


Rechner: umbrel.local


Anschlussnummer: 50001



**Fernverbindung (Tor)**


Host : [Ihr-Address-Zwiebel]


Anschlussnummer: 50001



Die Tor-Verbindung ist notwendig, wenn du außerhalb deines lokalen Netzwerks auf deinen Knoten zugreifen willst.



![Configuration connexion](assets/fr/21.webp)


Für weitere Informationen über die Software Sparrow Wallet haben wir eine umfassende Anleitung:


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d
## Schlussfolgerung



Ihr Umbrel ist nun einsatzbereit. Du nimmst aktiv am Bitcoin Netzwerk teil und behältst dabei die volle Kontrolle über Deine Daten. Entdecken Sie die vielen anderen Anwendungen, die im Umbrel App Store verfügbar sind, um die Möglichkeiten Ihres Heimservers zu erweitern.



## Nützliche Ressourcen



### Offizielle Dokumentation




- [Offizielle Umbrel-Website](https://umbrel.com)
- [Umbrella-Dokumentation](https://github.com/getumbrel/umbrel/wiki)
- [App Store Umbrel](https://apps.umbrel.com)



### Bitcoin-Anwendungen




- [Bitcoin Kern](https://Bitcoin.org/fr/)
- [Electrs](https://github.com/romanz/electrs)
- [Mempool](https://Mempool.space)
- [Sperling Wallet](https://sparrowwallet.com)



### Gemeinschaft




- [Forum Umbrella] (https://community.getumbrel.com)
- [GitHub Umbrel](https://github.com/getumbrel)
- [Twitter Umbrella](https://twitter.com/umbrel)