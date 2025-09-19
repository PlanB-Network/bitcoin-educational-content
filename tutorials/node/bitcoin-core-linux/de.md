---
name: Bitcoin Core (Linux)
description: Betrieb eines eigenen Knotens mit Bitcoin core unter Linux
---

![cover](assets/cover.webp)


## Betrieb eines eigenen Knotens mit Bitcoin core


Einführung in Bitcoin und das Konzept eines Knotens, ergänzt durch eine umfassende Installationsanleitung für Linux.


Einer der spannendsten Aspekte von Bitcoin ist die Möglichkeit, das Programm selbst auszuführen und so auf einer granularen Ebene am Netzwerk und der Überprüfung der öffentlichen Transaktion Ledger teilzunehmen.


Bitcoin ist ein Open-Source-Projekt, das seit 2009 frei verfügbar ist und öffentlich verbreitet wird. Fast 17 Jahre nach seiner Gründung ist Bitcoin nun ein robustes und unaufhaltsames digitales Geldnetzwerk, das von einem starken organischen Netzwerkeffekt profitiert. Für ihre Bemühungen und Visionen gebührt Satoshi Nakamoto unsere Dankbarkeit. Übrigens, das Bitcoin-Whitepaper finden Sie hier auf Agora 256 (Anmerkung: auch auf der Universität).


### Werden Sie Ihre eigene Bank


Der Betrieb eines eigenen Knotens ist für Anhänger des Bitcoin-Ethos unerlässlich geworden. Ohne jemanden um Erlaubnis zu fragen, ist es möglich, den Blockchain von Anfang an herunterzuladen und so alle Transaktionen von A bis Z gemäß dem Bitcoin-Protokoll zu überprüfen.


Das Programm umfasst auch einen eigenen Wallet. So haben wir die Kontrolle über die Transaktionen, die wir an den Rest des Netzes senden, ohne einen Vermittler oder eine dritte Partei. Sie sind Ihre eigene Bank.


Der Rest dieses Artikels ist daher eine Anleitung zur Installation von Bitcoin core - der am weitesten verbreiteten Bitcoin-Softwareversion - speziell auf Debian-kompatiblen Linux-Distributionen wie Ubuntu und Pop!OS. Folgen Sie dieser Anleitung, um Ihrer individuellen Souveränität einen Schritt näher zu kommen.


## Bitcoin core Installationsanleitung für Debian/Ubuntu


**Voraussetzungen**


- Mindestens 6 GB Datenspeicher (pruned-Knoten) - 1 TB Datenspeicher (Full node)
- Rechnen Sie damit, dass der *Initial Block Download* (IBD) mindestens 24 Stunden dauert. Dieser Vorgang ist selbst für einen pruned-Knoten obligatorisch.
- Erlauben Sie ~600 GB Bandbreite für die IBD, selbst für einen pruned-Knoten.


**Hinweis:💡** die folgenden Befehle sind für Bitcoin core Version 24.1 vordefiniert.


### Herunterladen und Überprüfen von Dateien



- [Download](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, sowie die Dateien `SHA256SUMS` und `SHA256SUMS.asc` (Sie müssen natürlich die neueste Version der Software herunterladen).



- Öffnen Sie ein Terminal in dem Verzeichnis, in dem sich die heruntergeladenen Dateien befinden. Beispiel: `cd ~/Downloads/`.



- Überprüfen Sie, ob die Prüfsumme der Versionsdatei in der Prüfsummendatei aufgeführt ist, indem Sie den Befehl `sha256sum --ignore-missing --check SHA256SUMS` verwenden.



- Die Ausgabe dieses Befehls sollte den Namen der heruntergeladenen Versionsdatei enthalten, gefolgt von `OK`. Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Installieren Sie git mit dem Befehl `sudo apt install git`. Dann klonen Sie das Repository, das die PGP-Schlüssel der Bitcoin core-Unterzeichner enthält, mit dem Befehl `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Importieren Sie die PGP-Schlüssel aller Unterzeichner mit dem Befehl `gpg --import guix.sigs/builder-keys/*`



- Überprüfen Sie, ob die Prüfsummendatei mit den PGP-Schlüsseln der Unterzeichner signiert ist, indem Sie den Befehl `gpg --verify SHA256SUMS.asc` verwenden.



Für jede gültige Signatur wird eine Zeile angezeigt, die mit `gpg: Gute Signatur` und eine weitere Zeile, die mit: `Primärschlüssel-Fingerabdruck: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320" (Beispiel für den Fingerabdruck des PGP-Schlüssels von Pieter Wuille).


**Hinweis💡:** Es ist nicht notwendig, dass alle Unterzeichnerschlüssel ein "OK" zurückgeben. Es kann sogar sein, dass nur einer erforderlich ist. Es ist dem Benutzer überlassen, seine eigene Validierungsschwelle für die PGP-Verifizierung zu bestimmen.


Sie können die Warnungen ignorieren:



- dieser Schlüssel ist nicht mit einer vertrauenswürdigen Signatur zertifiziert!



- es gibt keinen Hinweis darauf, dass die Unterschrift dem Eigentümer gehört


### Installation des grafischen Bitcoin core Interface



- Verwenden Sie im Terminal, immer noch in dem Verzeichnis, in dem sich die Bitcoin core-Versionsdatei befindet, den Befehl `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, um die im Archiv enthaltenen Dateien zu entpacken.



- Installieren Sie die zuvor entpackten Dateien mit dem Befehl `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Installieren Sie die notwendigen Abhängigkeiten mit dem Befehl `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Starten Sie _bitcoin-qt_ (Bitcoin core grafischer Interface) mit dem Befehl `Bitcoin-qt`.



- Um einen pruned-Knoten auszuwählen, markieren Sie _Blockchain-Speicher begrenzen_ und konfigurieren Sie die zu speichernde Datengrenze:


![welcome](assets/fr/02.webp)


### Abschluss von Teil 1: Installationsanleitung


Sobald Bitcoin core installiert ist, wird empfohlen, ihn so oft wie möglich laufen zu lassen, um zum Bitcoin-Netzwerk beizutragen, indem Transaktionen verifiziert und neue Blöcke an andere Peers übertragen werden.


Es ist jedoch nach wie vor eine gute Praxis, den Knoten gelegentlich zu betreiben und zu synchronisieren, und sei es nur, um empfangene und gesendete Transaktionen zu validieren.


![Creation wallet](assets/fr/03.webp)


## Tor für einen Bitcoin core-Knoten konfigurieren


**Hinweis💡:** Diese Anleitung ist für Bitcoin core 24.0.1 auf Ubuntu/Debian-kompatiblen Linux-Distributionen konzipiert.


### Installiere und konfiguriere Tor für Bitcoin core


Zunächst müssen wir den Tor-Dienst (The Onion Router) installieren, ein Netzwerk für anonyme Kommunikation, das es uns ermöglicht, unsere Interaktionen mit dem Bitcoin-Netzwerk zu anonymisieren. Eine Einführung in Tools zum Schutz der Privatsphäre im Internet, einschließlich Tor, finden Sie in unserem Artikel zu diesem Thema.


Um Tor zu installieren, öffne ein Terminal und gib `sudo apt -y install tor` ein. Sobald die Installation abgeschlossen ist, wird der Dienst normalerweise automatisch im Hintergrund gestartet. Überprüfe, ob er korrekt läuft, indem du den Befehl `sudo systemctl status tor` eingibst. Die Antwort sollte `Active: active (exited)` zeigen. Drücken Sie `Strg+C`, um diese Funktion zu beenden.


**Tipp:** Du kannst in jedem Fall die folgenden Befehle im Terminal verwenden, um Tor zu starten, zu stoppen oder neu zu starten:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Als nächstes starten wir den grafischen Bitcoin core mit dem Befehl `Bitcoin-qt`. Aktiviere dann die automatische Funktion der Software, um unsere Verbindungen über einen Tor-Proxy zu leiten: _Einstellungen > Netzwerk_, und dort _Verbinden über SOCKS5-Proxy (Standard-Proxy)_ sowie _Einen separaten SOCKS5-Proxy verwenden, um andere Nutzer über Tor-Zwiebel-Dienste zu erreichen_.


![option](assets/fr/04.webp)


Bitcoin core erkennt automatisch, ob Tor installiert ist und stellt standardmäßig ausgehende Verbindungen zu anderen Knoten her, die ebenfalls Tor benutzen, zusätzlich zu Verbindungen zu Knoten, die IPv4/IPv6-Netzwerke (clearnet) benutzen.


**Hinweis💡:** Um die Anzeigesprache auf Französisch zu ändern, gehen Sie in den Einstellungen auf die Registerkarte Anzeige.


### Erweiterte Tor-Konfiguration (optional)


Es ist möglich, Bitcoin core so zu konfigurieren, dass er nur das Tor-Netzwerk verwendet, um sich mit anderen Nutzern zu verbinden und so die Anonymität über unseren Knoten zu optimieren. Da es im grafischen Interface keine eingebaute Funktion dafür gibt, müssen wir manuell eine Konfigurationsdatei erstellen. Gehe zu Einstellungen und dann zu Optionen.


![option 2](assets/fr/05.webp)


Hier klicken Sie auf _Open configuration file_. In der Textdatei `Bitcoin.conf` fügen Sie einfach die Zeile `onlynet=onion` ein und speichern die Datei. Sie müssen Bitcoin core neu starten, damit dieser Befehl wirksam wird.


Wir werden dann den Tor-Dienst so konfigurieren, dass Bitcoin core eingehende Verbindungen über einen Proxy empfangen kann, so dass andere Knoten im Netzwerk unseren Knoten zum Herunterladen von Blockchain-Daten nutzen können, ohne die Sicherheit unseres Rechners zu gefährden.


Gib im Terminal `sudo nano /etc/tor/torrc` ein, um die Konfigurationsdatei des Tor-Dienstes zu öffnen. Suche in dieser Datei nach der Zeile `#ControlPort 9051` und entferne das `#`, um es zu aktivieren. Füge nun zwei neue Zeilen in die Datei ein:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Um die Datei zu verlassen, während du sie speicherst, drücke `Strg+X > Y > Enter`. Zurück im Terminal, starte Tor neu, indem du den Befehl `sudo systemctl restart tor` eingibst.


Mit dieser Konfiguration kann Bitcoin core eingehende und ausgehende Verbindungen mit anderen Knoten im Netzwerk nur über das Tor-Netzwerk (Onion) herstellen. Um dies zu bestätigen, klicken Sie auf die Registerkarte _Fenster_, dann _Peers_.


![Nodes Window](assets/fr/06.webp)


### Zusätzliche Ressourcen


Wenn du nur das Tor-Netzwerk (`onlynet=onion`) verwendest, könntest du für einen Sybil Attack anfällig werden. Deshalb wird empfohlen, eine Konfiguration mit mehreren Netzwerken beizubehalten, um dieses Risiko zu minimieren. Außerdem werden alle IPv4/IPv6-Verbindungen durch den Tor-Proxy geleitet, sobald dieser konfiguriert ist, wie bereits erwähnt.


Alternativ kannst du, um nur im Tor-Netzwerk zu bleiben und das Risiko eines Sybil Attack zu verringern, den Address eines anderen vertrauenswürdigen Knotens zu deiner `Bitcoin.conf`-Datei hinzufügen, indem du die Zeile `addnode=trusted_address.onion` hinzufügst. Sie können diese Zeile mehrfach hinzufügen, wenn Sie eine Verbindung zu mehreren vertrauenswürdigen Knoten herstellen möchten.


Um die Logs deines Bitcoin-Knotens zu sehen, die sich speziell auf seine Interaktion mit Tor beziehen, füge `debug=tor` zu deiner `Bitcoin.conf`-Datei hinzu. Du wirst nun relevante Tor-Informationen in deinem Debug-Log haben, die du im _Informations_-Fenster mit dem _Debug File_-Knopf ansehen kannst. Es ist auch möglich, diese Protokolle direkt im Terminal mit dem Befehl `bitcoind -debug=tor` anzusehen.


**Tipp💡:** Hier sind einige interessante Links:


- [Wiki-Seite, die Tor und seine Beziehung zu Bitcoin erklärt] (https://en.Bitcoin.it/wiki/Tor)
- [Bitcoin core Konfigurationsdatei-Generator von Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Tor-Konfigurationsanleitung von Jon Atack] (https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Wie immer, wenn Sie Fragen haben, können Sie diese gerne mit der Agora256 Gemeinschaft teilen. Wir lernen gemeinsam, um morgen besser zu sein als heute!