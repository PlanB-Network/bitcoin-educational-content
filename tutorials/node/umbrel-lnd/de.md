---
name: Regenschirm LND
description: Erweiterte Anleitung zur Installation und Konfiguration von Lightning Network Daemon (LND) auf Umbrel
---
![cover](assets/cover.webp)




## Einführung



Dieses Tutorial für Fortgeschrittene führt Sie Schritt für Schritt durch die Installation, Konfiguration und Nutzung der Lightning Node (LND) Anwendung auf Ihrem Umbrel Node. Sie werden lernen, wie Sie Kanäle öffnen, Ihre Liquidität verwalten und Ihren Knoten mit einer mobilen Anwendung synchronisieren.



## 1. Voraussetzung: funktionsfähiger Bitcoin Umbrel-Knoten



Bevor Sie Lightning einsetzen können, müssen Sie einen voll funktionsfähigen Bitcoin Knoten auf Umbrel haben. Dies beinhaltet die Installation von Umbrel (auf einem Raspberry Pi, NAS oder einer anderen Maschine) und die vollständige Synchronisierung des Blockchain Bitcoin.



Um Umbrel zu installieren und Ihren Bitcoin Knoten zu konfigurieren, empfehlen wir Ihnen, unserem Tutorial zu folgen:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Stellen Sie sicher, dass Ihr Bitcoin-Knoten auf dem neuesten Stand ist und ordnungsgemäß funktioniert, da Lightning Network für alle off-chain-Transaktionen auf ihn angewiesen ist.



## 2. Einführung in Lightning Network



Lightning Network ist ein zweites Layer-Protokoll, das dazu dient, Bitcoin-Transaktionen zu beschleunigen und ihre Kosten zu senken, indem sie außerhalb des Haupt-Blockchain durchgeführt werden.



Konkret nutzt Lightning ein Netzwerk von Zahlungskanälen zwischen Knoten: Zwei Nutzer öffnen einen Kanal, indem sie On-Chain BTC blockieren (Anfangstransaktion), und können dann sofort Exchange-Zahlungen innerhalb dieses Kanals tätigen. Diese off-chain-Transaktionen werden nicht auf dem Blockchain aufgezeichnet, daher ihre Schnelligkeit und praktisch null Kosten.



Zahlungen können über mehrere Kanäle geleitet werden (dank zwischengeschalteter Knoten), um jeden Empfänger im Netzwerk zu erreichen, was eine nahezu unbegrenzte Anzahl von Soforttransaktionen ermöglicht. Lightning bietet somit sehr schnelle, kostengünstige Transaktionen, die sich ideal für alltägliche Zahlungen oder Mikrotransaktionen eignen und gleichzeitig den Blockchain Bitcoin entlasten.



Um zu funktionieren, muss ein Lightning-Knoten ständig mit dem Netz verbunden sein und mit anderen Lightning-Knoten interagieren. Es gibt verschiedene Software-Implementierungen (LND, Core Lightning, Eclair, etc.), die alle miteinander kompatibel sind. Umbrel verwendet LND (Lightning Network Daemon) als Teil seiner offiziellen Lightning Node Anwendung. Dieses Tutorial konzentriert sich auf LND.



Für eine vollständige theoretische Einführung in Lightning Network empfehlen wir Ihnen, unseren speziellen Kurs zu besuchen:



https://planb.network/courses/introduction-theorique-au-lightning-network-34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

In diesem Kurs erhalten Sie eine gründliche Einführung in die grundlegenden Konzepte des Lightning Network, bevor Sie mit Ihrem LND-Knoten üben können.



## 3. Warum LND selbst hosten?



Der Betrieb eines eigenen Lightning-Knotens (LND) auf Umbrel gibt Ihnen die totale Souveränität über Ihre Gelder und Kanäle, verglichen mit verwahrten oder halbverwahrten Lösungen.



### Vergleich von Blitzlösungen :



**Solutions custodiales (ex: Wallet von Satoshi)** :




- Ihre Lightning-Bitcoins werden von einer vertrauenswürdigen dritten Partei verwaltet
- Einfach zu bedienen, keine technische Komplexität
- Der Betreiber verfügt über Ihr Geld und kann Ihre Transaktionen verfolgen
- Sie verzichten auf Kontrolle und Vertraulichkeit



**Nicht-Rohstoff-Verbraucherportfolios (z. B. Phoenix, Breez)** :




- Die Nutzer behalten ihre privaten Schlüssel und damit Ownership ihrer BTC
- Keine vollständige Knotenverwaltung - Anwendung verwaltet Kanäle im Hintergrund
- Kompromiss zwischen Einfachheit und Souveränität
- Abhängigkeit von der Infrastruktur der Lieferanten für Liquidität
- Technische Einschränkungen (ein Smartphone kann keine Zahlungen für andere weiterleiten)



**Selbstgehosteter LND-Knoten (Umbrel)** :




- Maximale Souveränität: Ihre On-Chain und off-chain BTCs sind vollständig unter Ihrer Kontrolle
- Es sind keine Dritten an der Eröffnung von Kanälen oder der Verwaltung Ihrer Zahlungen beteiligt
- Erhöhte Vertraulichkeit (Ihre Kanäle und Transaktionen sind nur Ihnen und Ihren direkten Kollegen bekannt)
- Nutzungsfreiheit: Verbinden Sie sich mit Ihren eigenen Diensten und Geldbörsen
- Möglichkeit der Weiterleitung von Transaktionen für andere (Mikrovergütung)
- Erhöhte technische Verantwortung (Wartung, Liquiditätsmanagement, Backups)



Kurz gesagt, die selbst gehostete LND bietet Ihnen maximale Kontrolle, erfordert aber mehr technisches Know-how. Es ist ein Kompromiss zwischen Bequemlichkeit und Souveränität.



## 4. Schritt-für-Schritt-Anleitung



### 4.1 Installation und Konfiguration der Lightning Node Anwendung auf Umbrel



Sobald Ihr Umbrel-Knoten (Bitcoin) synchronisiert wurde, folgen Sie diesen Schritten:



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Installieren Sie die Lightning Node-Anwendung aus dem Abschnitt "App Store" des Interface Umbrel.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) wird als Anwendung auf Ihrem Umbrel installiert. Wenn Sie es zum ersten Mal öffnen, werden Sie eine Warnmeldung sehen, die Sie darüber informiert, dass Lightning eine experimentelle Technologie ist.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Sie haben die Wahl zwischen der Erstellung eines neuen Knotens oder der Wiederherstellung eines Knotens aus einer Sicherung/seed. Bei einer Erstinstallation wählen Sie die Option, einen neuen Knoten zu erstellen. Die Lightning Node App wird generate eine 24-Wörter-Mnemonic-Phrase (Ihr seed Lightning) eingeben: Schreiben Sie diese Phrase sorgfältig auf (idealerweise offline, auf Papier), da sie zur Wiederherstellung Ihrer Lightning-Fonds verwendet wird, falls erforderlich.



**Hinweis: Bei neueren Versionen von Umbrel liefert die Installation der Lightning-App dieses 24-Wörter-seed (der Bitcoin Umbrel-Knoten selbst tut dies nicht).



![Interface principale de Lightning Node](assets/fr/04.webp)



Nach der Initialisierung haben Sie Zugriff auf das Haupt-Interface von Lightning Node.



![Paramètres de l'application](assets/fr/05.webp)



In den Anwendungseinstellungen finden Sie eine Reihe von wichtigen Optionen:




   - Konsultieren Sie Ihre Knoten-ID (den eindeutigen Bezeichner Ihres Knotens)
   - Anschließen eines externen Wallet (Wallet anschließen)
   - Geheime Wörter anzeigen
   - Zugriff auf erweiterte Einstellungen
   - Kanäle wiederherstellen
   - Kanal-Sicherungsdatei herunterladen
   - Automatische Backups aktivieren
   - Backup über Tor konfigurieren (Backup over Tor)



Diese Optionen sind für die Sicherheit und Verwaltung Ihres Lightning-Knotens unerlässlich. Stellen Sie sicher, dass Sie automatische Backups aktivieren und Ihre geheimen Wörter sicher aufbewahren.



**Nützliche Ressourcen:**




- [Umbrel Community](https://community.umbrel.com) - Diskussionsforum für Nutzer zum Austausch von Problemen und Lösungen zu Umbrel und seinem Ökosystem


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Beschreibung der Funktionen der Lightning Node App auf Umbrel
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Offizielle LND Dokumentation

### 4.2 Öffnen eines Lightning-Kanals



Sobald LND betriebsbereit ist, können Sie Ihren ersten Lightning-Kanal eröffnen. So finden Sie Qualitätsknoten, mit denen Sie sich verbinden können:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/) ist ein Explorer zum Auffinden zuverlässiger Knotenpunkte, um Kanäle zu öffnen.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Der [ACINQ-Knoten] (https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) ist beispielsweise ein anerkannter Knotenpunkt mit hervorragenden Verfügbarkeits- und Liquiditätsstatistiken.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



Für dieses Tutorial werden wir einen Kanal mit [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca) öffnen. Die für die Verbindung erforderlichen Informationen (pubkey@ip:port) finden Sie auf der Amboss-Seite.



Um den Kanal zu öffnen:



![Bouton d'ouverture de canal](assets/fr/09.webp)



Klicken Sie auf der Startseite des Lightning Node auf die Schaltfläche "+ KANAL ÖFFNEN"



![Configuration du canal](assets/fr/10.webp)



Auf der Kanalkonfigurationsseite :




   - Fügen Sie die von Amboss kopierte Knoten-ID ein (Format: pubkey@ip:port)
   - Legen Sie die Kanalkapazität fest (einige Knoten wie ACINQ haben Mindestanforderungen, z. B. 400k Sats)
   - Gegebenenfalls Anpassung der Eröffnungsgebühren für Transaktionen



![Canal en cours d'ouverture](assets/fr/11.webp)



Sobald die Transaktion gesendet wurde, wird der Kanal auf der Startseite als "offen" angezeigt. Warten Sie auf die Bestätigung der On-Chain-Transaktion.



![Détails du canal](assets/fr/12.webp)



Klicken Sie auf den Kanal, um seine Details anzuzeigen:




   - Aktueller Stand
   - Gesamtkapazität
   - Aufschlüsselung der Liquidität (eingehend/ausgehend)
   - Öffentlicher Schlüssel des entfernten Knotens
   - Und andere technische Informationen



### Verwendung von Lightning Network+ zur Erlangung eingehender Liquidität



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ ist im Umbrel App Store erhältlich, um die Beschaffung von Bargeld zu erleichtern.



![Interface principale de LN+](assets/fr/14.webp)



Das Hauptmenü Interface bietet drei wichtige Optionen:




- "Liquiditätsswaps: Erkundung der verfügbaren Swap-Angebote
- "Für mich öffnen": Filtern Sie die Swaps, für die Sie in Frage kommen
- "To Docs": Zugang zur Dokumentation



![Message d'erreur LN+](assets/fr/15.webp)



Hinweis: Wenn Sie noch keinen Kanal geöffnet haben, wird diese Fehlermeldung angezeigt, wenn Sie auf "Für mich öffnen" klicken.



![Liste des swaps disponibles](assets/fr/16.webp)



Auf der Seite "Liquiditätsswaps" werden alle im Netz verfügbaren Swap-Angebote angezeigt.



![Swaps éligibles](assets/fr/17.webp)



mit "Für mich öffnen" werden nur die Swaps gefiltert, für die Ihr Knoten die erforderlichen Bedingungen erfüllt.



![Détails d'un swap](assets/fr/18.webp)



Beispiel für Swap-Details :




- Pentagon-Konfiguration (5 Teilnehmer)
- Kapazität von 300k Sats pro Kanal
- Voraussetzung: mindestens 10 offene Kanäle mit 1M Sats Gesamtkapazität
- Verfügbare Plätze: 4/5



### 4.3 Synchronisierung mit einer mobilen Anwendung (Zeus)



Um Ihren Lightning-Knoten aus der Ferne (per Smartphone) zu steuern, können Sie Zeus verwenden (Open-Source-Anwendung für iOS/Android).



**Zeus-Konfiguration mit Umbrel :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Stellen Sie sicher, dass Ihr Umbrel-Knoten erreichbar ist (standardmäßig über Tor).


Öffnen Sie in der Interface Umbrella die Lightning Node App und klicken Sie dann auf die Schaltfläche "Wallet verbinden", wie durch den Pfeil angezeigt.



![Page de connexion avec QR code](assets/fr/20.webp)



Es erscheint ein QR-Code, der Ihre LND Zugangsdaten im lndconnect-Format enthält. Dieser QR-Code ist besonders informationsreich. Zögern Sie daher nicht, ihn zum besseren Lesen zu vergrößern.



![Configuration initiale de Zeus](assets/fr/21.webp)



Auf Ihrem Telefon:




   - Zeus öffnen
   - Klicken Sie auf der Startseite auf "Erweiterte Einstellungen", um Ihren eigenen Lightning-Knoten zu verbinden
   - Wählen Sie in den Parametern "Wallet erstellen oder verbinden"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



In Zeus:




   - Wählen Sie "LND (REST)" als Verbindungstyp
   - Sie können entweder den QR-Code scannen (empfohlene Methode) oder die Informationen manuell eingeben. (Zögern Sie nicht, den QR-Code von Umbrel zu vergrößern, da er sehr dicht ist)
   - Wichtig: aktiviere die Option "Tor verwenden", wenn dein Umbrel nur über Tor zugänglich ist (Standardeinstellung)
   - Konfiguration speichern



Ihr Zeus ist nun mit Ihrem Umbrel-Knotenpunkt verbunden und ermöglicht es Ihnen, Blitzzahlungen zu tätigen, Ihre Kanäle, Guthaben usw. einzusehen und dabei vollständig selbst verwaltet zu bleiben.



**Erweiterte Verbindungsoptionen:**



Standardmäßig erfolgt die Zeus ↔ Umbrel-Verbindung über Tor. Für eine schnellere Verbindung gibt es zwei Alternativen:



**Lightning Node Connect (LNC)** :




   - Lightning Labs' verschlüsselter Verbindungsmechanismus
   - Installieren Sie die Lightning Terminal App auf Umbrel (mit LNC-Zugang)
   - generate einen Verbindungs-QR-Code in Lightning Terminal (Verbinden → Zeus über LNC verbinden)
   - Scannen Sie es in Zeus ein (wählen Sie "LNC" als Verbindungstyp)



**VPN Tailscale**:




   - Einfach zu konfigurierendes Mesh-VPN
   - Installieren Sie Tailscale auf Umbrel (App Store) und auf Ihrem Mobiltelefon
   - Verbinde Zeus über die private IP von Tailscale anstelle von Tor Address



Diese Optionen sind nicht zwingend erforderlich, und die Lösung Tor + Zeus funktioniert in den meisten Fällen gut.



> **Nützliche Ressourcen:**
> - [Zeus-Dokumentation - Umbrel-Anbindung](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Offizielle Anleitung zur Anbindung von Zeus an Umbrel
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Zeus Open-Source-Projekt
> - [Umbrel Community - Anschluss von Zeus über Tailscale](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Anleitung zum Anschluss von Zeus an Umbrel über Tailscale

## 5. Sicherheit und bewährte Praktiken



Die Verwaltung eines selbst gehosteten Lightning-Knotens erfordert besondere Aufmerksamkeit für die Sicherheit.



### Backup und Sicherheit für Ihren Knotenpunkt



**Wesentliche Arten von Backups**



Ihr Lightning Umbrel-Knoten benötigt zwei Arten von Backups:



**Der seed-Satz (24 Wörter)**




- Rückgewinnung von On-Chain-Mitteln
- Erforderlich für den Nachbau des Wallet Lightning
- Für hochsichere Speicherung (offline, auf Papier)



**Static Channel Backup (SCB)** Datei




- Enthält Lightning-Kanal-Informationen
- Ermöglicht das erzwungene Schließen des Kanals im Falle eines Absturzes
- Wichtig:** Speichern Sie die Datei `channel.db` niemals manuell (Risiko von Strafen)



**Manuelles Sicherungsverfahren



So speichern Sie Ihre Kanäle manuell:


1. Rufen Sie das Menü Lightning Node auf (drei Punkte "⋮" neben "+ Open Channel")


2. Laden Sie die Sicherungsdatei des Kanals herunter


3. Exportieren einer neuen SCB nach jeder Kanaländerung


4. SCB sicher aufbewahren (verschlüsselte Medien, Kopie außerhalb des Standorts)



**Umbrel** automatisches Sicherungssystem



Umbrel verfügt über ein ausgeklügeltes automatisches Sicherungssystem, das die :



*Datenschutz:*




- Client-seitige Verschlüsselung vor der Übertragung
- Versenden über das Tor-Netzwerk
- Daten ergänzt durch zufällige Füllung
- Einzigartiger Verschlüsselungsschlüssel für Ihr Gerät



*Verbesserte Sicherheit:*




- Sofortige Backups bei Statusänderungen
- Decoy"-Backups in zufälligen Abständen
- Änderungen der Sicherungsgröße ausblenden
- Schutz vor Zeitanalyse



*Wiederherstellungsprozess:*




- Kennung und Schlüssel von Ihrem seed Umbrella
- Vollständige Wiederherstellung nur mit Mnemonic-Satz möglich
- Automatische Wiederherstellung der letzten Backups
- Kanaleinstellungen und Daten wiederherstellen



### Restaurierung von Unfällen



Wenn Ihr Knoten verloren geht (Hardwarefehler, beschädigte SD-Karte) :




- Regenschirm wieder einbauen
- Geben Sie Ihren seed mit 24 Wörtern in der Lightning-App ein
- Importieren der SCB-Datei während der Wiederherstellung



LND wird sich mit jedem Partner Ihrer alten Kanäle in Verbindung setzen, um sie zu schließen und Ihren Anteil an den On-Chain-Geldern zurückzuerhalten. Die Kanäle werden dauerhaft geschlossen (und können bei Bedarf wieder geöffnet werden).



### Verfügbarkeit und Schutz vor Betrug



Idealerweise sollten Sie Ihren Knoten so oft wie möglich online lassen. Im Falle längerer Abwesenheit:




- Ein böswilliger Peer könnte versuchen, einen alten Kanalstatus zu übertragen
- Lightning sieht eine "Protestfrist" vor (etwa 2 Wochen bei LND)
- Wenn Sie für längere Zeit abwesend sind, richten Sie einen Watchtower ein



**Watchtower Konfiguration:**




- Fügen Sie in den erweiterten LND-Einstellungen die URL eines vertrauenswürdigen Watchtower-Servers hinzu
- Sie können einen öffentlichen Dienst nutzen oder Ihren eigenen Watchtower installieren




Um mehr über die Konfiguration und Verwendung von Wachtürmen zu erfahren, empfehlen wir Ihnen einen Blick in unser spezielles Tutorial:



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Andere bewährte Praktiken





- Software-Updates:** Halten Sie Umbrel und LND auf dem neuesten Stand (Sicherheitskorrekturen)
- Hardware-Schutz:** Verwenden Sie ein stabiles System (Raspberry Pi mit SSD, Mini-PC) und eine USV
- Netzwerksicherheit:** Behalte die Standard-Tor-Konfiguration bei, ändere das Umbrel-Administrator-Passwort (Standard: "moneyprintergobrrr")
- Verschlüsselung:** Aktivieren Sie die Festplattenverschlüsselung, wenn möglich



## 6. Zusätzliche Tools



Die Lightning Node App von Umbrel bietet die grundlegenden Funktionen für die Verwaltung Ihrer Kanäle, aber Tools von Drittanbietern bieten erweiterte Funktionen.



### ThunderHub



Interface modernes webbasiertes Lightning-Node-Management-System, das über den Umbrel App Store installiert werden kann.



**Merkmale:**




- Echtzeit-Visualisierung der Kanäle (Kapazitäten, Salden)
- Integrierte Werkzeuge für die Neugewichtung
- Unterstützung für Mehrwegabrechnung (MPP)
- QR-Code-Erzeugung LNURL
- Transaktionsmanagement On-Chain



ThunderHub eignet sich ideal für die Überwachung eines aktiven Routingknotens und die Durchführung eines einfachen Rebalancing.



### Ride The Lightning (RTL)



Interface webkompatibel mit verschiedenen Lightning-Implementierungen (LND, Core Lightning, Eclair).



**Highlights:**




- Verwaltung mehrerer Knotenpunkte
- Kontextabhängige Dashboards
- Unterstützung für U-Boot-Swaps (Lightning Loop)
- 2-Faktor-Authentifizierung
- Exportieren/Importieren von Kanalsicherungen



RTL ist ein komplettes "Schweizer Taschenmesser" für die Verwaltung eines Lightning-Knotens mit einem eher expertenorientierten Ansatz.



### Andere nützliche Tools





- Lightning Shell** : Befehlszeile (lncli) über Browser
- BTC RPC Explorer & Mempool** : Überwachung Blockchain
- LNmetrics und Torq**: Analyse der Routingleistung
- Amboss & 1ML**: "Soziale" Verwaltung Ihres Knotens (Pseudonyme, Kontakte, Netzwerkanalyse)



Diese Tools können mit nur wenigen Klicks über den Umbrel App Store installiert werden, ohne dass eine komplexe Konfiguration erforderlich ist.



**Zusätzliche Ressourcen für Werkzeuge:**




- [ThunderHub.io - Funktionen](https://thunderhub.io) - Überblick über die Funktionen von ThunderHub
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - RTL-Dokumentation
- [David Kaspar - Rebalance via ThunderHub](https://blog.davidkaspar.com) - Ein praktischer Leitfaden zum Rebalancing
- [Leitfaden "Lightning Nodes verwalten"](https://github.com/openoms/lightning-node-management) - Erweiterte Dokumentation für Power-User



## Schlussfolgerung



Der Betrieb eines eigenen LND Knotens auf Umbrel ist ein wichtiger Schritt in Richtung Finanzsouveränität. Obwohl es mehr technischen Einsatz erfordert als eine Depotlösung, sind die Vorteile in Bezug auf Kontrolle, Vertraulichkeit und aktive Teilnahme am Lightning Network beträchtlich.



Wenn Sie diesen Leitfaden befolgen, sollten Sie jetzt in der Lage sein, LND zu installieren, Kanäle zu öffnen, Ihre Liquidität zu verwalten und aus der Ferne auf Ihren Knoten zuzugreifen. Fühlen Sie sich frei, nach und nach erweiterte Funktionen und zusätzliche Tools zu erkunden, wenn Sie mit dem Ökosystem vertrauter werden.



Denken Sie daran, dass die Sicherheit Ihrer Gelder von Ihren Sicherheitsvorkehrungen und -praktiken abhängt. Nehmen Sie sich die Zeit, alle Aspekte zu verstehen, bevor Sie große Summen einsetzen.