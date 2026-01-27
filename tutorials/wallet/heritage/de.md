---
name: Heritage
description: Ein Bitcoin-Portfolio mit integriertem Vererbungsmechanismus über Taproot-Skripte
---

![cover](assets/cover.webp)



Die Weitergabe von Bitcoins im Todesfall oder bei Geschäftsunfähigkeit stellt für jeden Inhaber eines Krypto-Vermögens eine große Herausforderung dar. Ohne einen geeigneten Nachlassplan sind diese Vermögenswerte für Ihre Angehörigen uneinbringlich.



Heritage bietet eine elegante Antwort, indem es einen Totmann-Schalter-Mechanismus direkt auf der Bitcoin-Blockchain implementiert. Mit diesem quelloffenen wallet können on-chain-Nachfolgebedingungen konfiguriert werden: Wenn der Eigentümer über einen bestimmten Zeitraum keine weiteren Transaktionen vornimmt, können zuvor festgelegte alternative Schlüssel die Mittel freigeben.



## Was ist Kulturerbe?



Heritage ist ein Bitcoin-Portfolio, das von Haus aus einen Vererbungsmechanismus über Taproot-Skripte integriert. Diese Open-Source-Software wurde von Jérémie Rodon unter MIT-Lizenz entwickelt und garantiert Transparenz und Beständigkeit.



Heritage verwendet Taproot-Skripte, die in Bitcoin-Adressen kodiert sind. Jede UTXO umfasst zwei Arten von Ausgabenbedingungen:





- Primärpfad** : Der Besitzer kann seine Bitcoins jederzeit mit seinem Primärschlüssel ausgeben
- Alternative Wege**: Für jeden vorgesehenen Erben kombiniert ein Skript seinen öffentlichen Schlüssel mit einer Zeitsperre



Jede Eigentümertransaktion verschiebt automatisch das Aktivierungsdatum der Erbschaftsklauseln. Im Falle längerer Inaktivität (Tod, Unfähigkeit) werden die Bedingungen automatisch ausgelöst.



## Erbschaftsdienst (fakultativ)



Heritage bietet zwei Nutzungsmöglichkeiten:



**Do it yourself (kostenlos)**: Die Open-Source-Anwendung allein. Sie verwalten alles selbstständig mit Ihrem eigenen Knoten. Diese Option bietet integrierten Backup-Zugang, integrierte Vererbung und exklusive Kontrolle über Ihre Bitcoins. Allerdings müssen Sie Ihre eigenen Benachrichtigungen (Kalender, Erinnerungen) erstellen, damit Sie nicht vergessen, Ihre Timelocks zu erneuern, und es gibt keine automatischen Benachrichtigungen für Ihre Erben.



**Nutzen Sie den Service (0,05% pro Jahr)** : Der btc-heritage.com-Dienst bietet zusätzliche Funktionen, um die Verwaltung zu vereinfachen:




- Automatische Erinnerungen vor Ablauf Ihrer Fristen
- Automatische Benachrichtigung der Erben, um sie durch den Einziehungsprozess zu führen
- Vorrangige Unterstützung
- Vereinfachte Verwaltung von Deskriptoren



Gebühr: 0,05% des verwalteten Betrags pro Jahr, mindestens 0,5 mBTC/Jahr. Das erste Jahr ist kostenlos.



Der Dienst ist nicht verwahrungspflichtig: Ihre privaten Schlüssel verlassen niemals Ihr Gerät. Heritage hat keinen Zugriff auf Ihr Geld.



## Erbe CLI



Für fortgeschrittene Benutzer, die das Terminal bevorzugen, bietet Heritage ein Befehlszeilentool (CLI) für die granulare Steuerung und den Betrieb von Maschinen mit Luftabdeckung.



![Page Heritage CLI](assets/fr/03.webp)



Die vollständige CLI-Dokumentation ist unter [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli) verfügbar. Hier finden Sie Anleitungen zum Herunterladen, Verbinden mit dem Dienst, Erstellen von Wallets (mit Ledger oder lokalen Schlüsseln), Verwalten von Erben und Transaktionen.



Dieses Tutorial konzentriert sich auf die Desktop-Anwendung, die für die meisten Benutzer leichter zugänglich ist.



## Erbe Desktop



Heritage Desktop ist eine grafische Anwendung mit einer intuitiven Benutzeroberfläche, die den Benutzer durch jeden Schritt des Konfigurationsprozesses führt.



### Herunterladen



Gehen Sie zu [btc-heritage.com](https://btc-heritage.com) und klicken Sie auf "Anwendung herunterladen".



![Page d'accueil Heritage](assets/fr/01.webp)



Wählen Sie die Version, die Ihrem Betriebssystem entspricht (Linux 64bits oder Windows 64bits). Die Binärdateien sind nicht digital signiert, was zu Sicherheitswarnungen führen kann.



![Page de téléchargement](assets/fr/02.webp)



### Installation unter Linux



Unter Linux wird die Anwendung im AppImage-Format verteilt. Bevor Sie sie ausführen können, müssen Sie die Abhängigkeit `libfuse2` installieren:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Machen Sie die Datei dann ausführbar und führen Sie sie aus:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### Erster Start



Beim ersten Start bietet Ihnen der Onboarding-Assistent drei Auswahlmöglichkeiten:



![Onboarding initial](assets/fr/05.webp)





- Einrichten eines Heritage Wallet**: Erstellen Sie einen neuen wallet mit Erbschaftsplan
- Bitcoins erben**: Bitcoins als Erbe zurückgewinnen
- Selbständig erkunden**: Funktionen ohne Hilfe erforschen



Wählen Sie "Setup an Heritage Wallet", um Ihr erstes wallet zu erstellen.



### Bitcoin-Netzwerkverbindung



Wählen Sie aus, wie die Verbindung zum Bitcoin-Netz hergestellt werden soll:



![Choix connexion](assets/fr/06.webp)





- Nutzung des Nachlassdienstes**: Verwaltete Infrastruktur, einfacher für Erben
- Eigenen Knoten verwenden**: Verbindung zu Ihrem eigenen Bitcoin-Kern oder Electrum-Knoten



Für dieses Tutorial verwenden wir unseren eigenen Knoten.



### Verwaltung privater Schlüssel



Wählen Sie aus, wie Sie Ihre privaten Schlüssel verwalten möchten:



![Gestion des clés](assets/fr/07.webp)





- Mit einer Ledger-Beschlagsvorrichtung** : Maximale Sicherheit mit wallet-Hardware (empfohlen)
- Lokale Speicherung mit Passwort**: Örtlich gespeicherte Schlüssel mit Passwortschutz
- Wiederherstellen eines vorhandenen wallet** : Wiederherstellen von einem vorhandenen seed



### Konfiguration des Knotens



Wenn Sie Ihren eigenen Knoten verwenden, führt Sie die Anwendung durch die Konfiguration. Stellen Sie sicher, dass Ihr Bitcoin- oder Electrum-Knoten auf :




- Installiert und in Betrieb
- Synchronisiert mit dem Bitcoin-Netzwerk
- Konfiguriert, um RPC-Verbindungen zu akzeptieren (für Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



Klicken Sie auf "Mein Bitcoin-Knoten ist einsatzbereit", wenn Ihr Knoten bereit ist.



### Status-Panel



Klicken Sie auf "Status" in der oberen rechten Ecke und dann auf "Konfiguration öffnen", um die Verbindungsparameter aufzurufen.



![Panneau Status](assets/fr/09.webp)



Geben Sie die URL Ihres Electrum-Servers ein (z. B. `umbrel.local:50001`, wenn Sie Umbrel verwenden).



![Configuration Electrum](assets/fr/10.webp)



### Erstellung von wallet



Sobald die Verbindung hergestellt ist, klicken Sie auf der Registerkarte WALLETS auf "Wallet erstellen".



![Créer wallet](assets/fr/11.webp)



Ein Popup erklärt die geteilte Architektur von Heritage :



![Architecture split](assets/fr/12.webp)



1. **Schlüsselanbieter (Offline)**: Verwaltet Ihre privaten Schlüssel und signiert Transaktionen. Kann eine Ledger oder eine wallet Software sein.


2. **Online Wallet**: Übernimmt die Synchronisierung mit dem Bitcoin-Netz, die Erstellung von Adressen und die Übertragung von Transaktionen.



Füllen Sie das Erstellungsformular aus:



![Formulaire création wallet](assets/fr/13.webp)





- Wallet Name**: Ein eindeutiger Name zur Identifizierung Ihres wallet
- Schlüsselanbieter**: Wählen Sie für dieses Tutorial die lokale Schlüsselspeicherung
- Neu/Wiederherstellen**: Wählen Sie "Neu", um generate ein neues seed zu erstellen
- Wortzahl**: 24 Wörter empfohlen für maximale Sicherheit



Geben Sie ein sicheres Passwort ein und wählen Sie Optionen für Online Wallet :



![Options Online Wallet](assets/fr/14.webp)





- Lokaler Knoten**: Verwendet Ihren eigenen Electrum- oder Bitcoin-Kernknoten
- Heritage-Dienst**: Verwendet den Heritage-Dienst (empfohlen für Benachrichtigungsfunktionen)



Klicken Sie auf "Wallet erstellen", um die Erstellung abzuschließen.



### Interface von wallet



Ihr wallet ist nun erstellt. Die Schnittstelle zeigt an:



![Interface wallet](assets/fr/15.webp)





- Bilanz
- Tasten SEND und RECEIVE
- Verlauf der Transaktionen
- Erbe Konfiguration Geschichte
- wallet-Adressen



### Erben schaffen



Gehen Sie auf die Registerkarte "ERBEN", um Ihre Erben anzulegen.



![Page Heirs](assets/fr/16.webp)



Das Informations-Popup erklärt:




- Erben sind öffentliche Bitcoin-Schlüssel, die mit Personen verbunden sind
- Jeder Erbe hat seine eigene Eselsbrücke
- Der erste Erbe sollte ein "Backup" für Sie selbst sein (für den Fall, dass Sie Ihren Haupt-wallet verlieren)



#### Erstellung von Backup-Erben



Klicken Sie auf "Erbe erstellen" und nennen Sie es "Backup".



![Création héritier Backup](assets/fr/17.webp)



Das Popup erklärt, warum ein 12-Wörter-Satz ohne passphrase für Erben sicher ist:


1. **Kein sofortiger Zugriff**: Erbenschlüssel können erst nach Ablauf der Zeitsperre auf die Mittel zugreifen


2. **Kompromiss-Erkennung**: Wenn jemand auf die Phrase zugreift, können Sie die Heritage-Konfiguration aktualisieren


3. **Langfristige Zugänglichkeit**: Ein passphrase könnte nach vielen Jahren vergessen werden



Konfigurieren Sie den Erben:



![Configuration héritier](assets/fr/18.webp)





- Schlüsselanbieter** : Lokaler Schlüsselspeicher
- Neu**: Erzeugen eines neuen seed
- Wortzahl**: 12 Wörter



Schließen Sie die Erstellung ab:



![Finalisation héritier](assets/fr/19.webp)





- Erbtyp**: Erweiterter öffentlicher Schlüssel
- Zum Dienst exportieren**: Optional, ermöglicht automatische Benachrichtigung der Erben



Der Backup-Erbe ist nun erstellt:



![Héritier créé](assets/fr/20.webp)



#### Die Eselsbrücke des Erben speichern



Klicken Sie auf den Erben Backup und dann auf "Mnemonic anzeigen":



![Afficher mnemonic](assets/fr/21.webp)



**WICHTIG: Notieren Sie sich diese 12 Wörter und bewahren Sie sie an einem sicheren Ort auf. Dies ist der Schlüssel zur Wiedererlangung des Geldes.



![Phrase mnémotechnique](assets/fr/22.webp)



#### Entfernen von seed aus der Anwendung



Wenn Sie die Phrase aufgeschrieben haben, rufen Sie die Erbe-Parameter auf (Zahnrad-Symbol):



![Paramètres héritier](assets/fr/23.webp)



Verwenden Sie "Strip Heir Seed", um den privaten Schlüssel aus der Anwendung zu entfernen. Bestätigen Sie, dass Sie die Phrase gespeichert haben.



![Strip Heir Seed](assets/fr/24.webp)



Dies ist eine Sicherheitsmaßnahme: Nur der öffentliche Schlüssel verbleibt in der Anwendung und reicht aus, um die Vererbung zu konfigurieren.



#### Schaffung eines zweiten Erben



Wiederholen Sie den Vorgang, um einen zweiten Erben anzulegen (z. B. "Satoshi"). Sie haben nun zwei Erben:



![Deux héritiers](assets/fr/25.webp)





- Sicherung**: Ihr persönlicher Notfallschlüssel
- Satoshi**: Ein designierter Erbe



### Konfiguration des Erbes



Kehren Sie zu Ihrem wallet zurück und klicken Sie auf das Symbol Einstellungen:



![Paramètres wallet](assets/fr/26.webp)



Klicken Sie im Abschnitt "Konfiguration des Erbes" auf "Erstellen":



![Heritage Configuration](assets/fr/27.webp)



Setzen Sie für jedes Erbe Zeitlimits fest:



![Configuration délais](assets/fr/28.webp)





- Sicherung**: 180 Tage (6 Monate) - Fälligkeitsdatum: 2026-06-18
- Satoshi**: 455 Tage (15 Monate) - Fälligkeitsdatum: 2027-03-20



**Wichtig**: Jeder Erbe muss eine längere Frist haben als der vorhergehende Erbe. Der erste Erbe (Backup) hat zuerst Zugriff auf die Mittel.



Auch konfigurieren:



![Configuration finale](assets/fr/29.webp)





- Bezugsdatum**: Anfangsdatum für die Berechnung der Vorlaufzeiten
- Mindestfrist für die Fälligkeit**: Mindestlaufzeit nach einer Transaktion (10 Tage empfohlen)



Klicken Sie auf "Erstellen", um die Konfiguration zu bestätigen.



Die Heritage-Konfiguration ist nun aktiv:



![Configuration active](assets/fr/30.webp)



Sie zeigt beide Erben mit ihren jeweiligen Fristen und Verfallsdaten an.



### Speichern von Deskriptoren



**Wichtig**: Speichern Sie Ihre wallet Deskriptoren. Ohne diese Deskriptoren ist eine Wiederherstellung der Mittel unmöglich, selbst wenn Sie die Eselsbrücke verwenden.



Klicken Sie auf "Sicherungsdeskriptoren" :



![Bouton Backup](assets/fr/31.webp)



Speichern Sie die JSON-Datei mit Ihren Bitcoin-Deskriptoren:



![Backup descripteurs](assets/fr/32.webp)



Diese Datei sollte zusammen mit den entsprechenden Merksätzen an Ihre Erben weitergegeben werden.



### Bitcoins erhalten



Klicken Sie auf "RECEIVE", um generate eine Empfangsadresse zu geben:



![Recevoir bitcoins](assets/fr/33.webp)



Herzlichen Glückwunsch! Ihr Heritage Wallet ist bereit, Bitcoins zu empfangen. Jede generierte Adresse enthält automatisch Ihre Heritage-Konditionen.



Nach Erhalt einer Transaktion wird Ihr Saldo aktualisiert:



![Solde mis à jour](assets/fr/34.webp)



Die Historie zeigt die Transaktion und die zugehörige Heritage-Konfiguration an.



---

## Einziehung durch einen Erben



Nach Ablauf der festgesetzten Frist kann der Erbe das Geld zurückfordern.



### Voraussetzungen



Der Erbe braucht :


1. Sein 12-Wörter-Memoniksatz


2. Die ursprüngliche wallet-Deskriptor-Sicherungsdatei (JSON)



### Erstellen eines Erben Wallet



Auf der Registerkarte "ERBEN" werden Sie in einem Popup-Fenster auf diese Voraussetzungen hingewiesen:



![Page Heir Wallets](assets/fr/35.webp)



**Bitte beachten**: Ohne die Sicherungsdatei für den Deskriptor ist der Zugang zu den Fonds selbst mit der richtigen mnemotechnischen Phrase UNMÖGLICH.



Klicken Sie auf "Erbe Wallet erstellen" :



![Créer Heir Wallet](assets/fr/36.webp)



Bitte füllen Sie das Formular aus:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Erbe Wallet Name**: Ein Name zur Identifizierung dieses Erben wallet
- Schlüsselanbieter** : Lokaler Schlüsselspeicher
- Wiederherstellen**: Wählen Sie diese Option, um eine vorhandene Phrase einzugeben



Geben Sie die 12 Wörter der Mnemonik des Erben ein und konfigurieren Sie den Heritage Provider:



![Entrée mnemonic](assets/fr/38.webp)





- Heritage Provider**: "Lokal", um Ihren eigenen Knoten mit der Sicherungsdatei zu verwenden



Laden Sie die JSON-Sicherungsdatei und klicken Sie auf "Erben Wallet erstellen":



![Chargement backup](assets/fr/39.webp)



### Interface Erbe Wallet



Der Erbe Wallet wird erstellt. Wenn die Zeitsperre noch nicht abgelaufen ist, ist zunächst keine Vererbung möglich:



![Pas d'héritage disponible](assets/fr/40.webp)



Sobald die Frist verstrichen ist und die Mittel mit dem Bitcoin-Netzwerk synchronisiert wurden, erscheinen sie in der Liste der Erbschaften:



![Héritage disponible](assets/fr/41.webp)



Die Schnittstelle zeigt an:




- Schlüsseltyp und Fingerabdruck
- Gesamtes vererbbares Vermögen
- Aktueller ausgabefähiger Betrag (0 sat, wenn die Zeitsperre noch nicht abgelaufen ist)
- Fälligkeits- und Verfallsdaten



Wenn das Fälligkeitsdatum erreicht ist, werden die Bitcoins über die Schaltfläche "Ausgeben" auf eine persönliche wallet übertragen.



---

## Bewährte Praktiken



### Speichern von Deskriptoren



wallet-Deskriptoren sind für die Rekonstruktion Ihrer Erbschaftsadressen unerlässlich. **Ohne die Deskriptoren werden Sie auch mit Ihrer Eselsbrücke nicht in der Lage sein, Ihre Fonds zu finden.



### Sicherheit der Schlüssel





- Verwenden Sie nach Möglichkeit einen Ledger für den Hauptschlüssel
- Bewahren Sie die Urteile der Erben niemals am selben Ort auf wie Ihre eigenen
- Verbreitung von Informationen über mehrere Medien und Standorte



### Dokumentation für Ihre Angehörigen



Schreiben Sie klare Anweisungen, die jeden Schritt des Wiederherstellungsprozesses erklären. Ihre Erben sind im entscheidenden Moment vielleicht nicht mit Bitcoin vertraut.



## Alternativen



Es gibt noch andere Lösungen, um die Übertragung Ihrer Bitcoins zu verwalten, darunter Liana und Bitcoin Keeper. Sie finden unsere Anleitungen unten:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Schlussfolgerung



Heritage ermöglicht es Ihnen, Ihre Bitcoin-Nachfolge souverän über die Desktop-Anwendung zu planen. Bei der Umsetzung gilt es, den richtigen Zeitrahmen und die Sicherung von Geheimnissen zu bedenken. Vergessen Sie nicht, an Ihre Erben weiterzugeben:




- Ihr 12-Wörter-Memoniksatz
- Die Deskriptor-Sicherungsdatei
- Anweisungen zur Wiederherstellung



## Ressourcen





- [Offizielle Website des Kulturerbes](https://btc-heritage.com)
- [Dokumentation CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)