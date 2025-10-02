---
name: Dojo
description: Ein quelloffener Bitcoin-Knoten für Privatsphäre und Autonomie
---

![cover](assets/cover.webp)



*Dieses Tutorial basiert auf [der offiziellen Ashigaru-Dokumentation] (https://ashigaru.rs/docs/), die ich übernommen und erweitert habe. Ich habe alle Abschnitte umgeschrieben, um die Übersichtlichkeit zu verbessern, und weitere detaillierte Erklärungen sowie Illustrationen für Anfänger hinzugefügt, um die Installation und Verwendung leichter verständlich zu machen.*



---

Dojo ist ein Open-Source-Programm, das als Backend-Server für bestimmte datenschutzorientierte Bitcoin-Geldbörsen dient, die auf einem Bitcoin core-Knoten basieren. Ursprünglich wurde es entwickelt, um mit Samourai Wallet zu arbeiten, einem mobilen Wallet, das erweiterte Datenschutzfunktionen wie Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym... bot. Samourai Wallet wurde nach der Verhaftung seiner Entwickler eingestellt, aber sein Nachfolger in der Community, **Ashigaru Wallet**, hat die Arbeit übernommen und setzt weiterhin auf Dojo, um Nutzern, die bei der Verwendung von Bitcoin die Kontrolle über ihre Daten behalten wollen, eine umfassende Erfahrung zu bieten.



![Image](assets/fr/01.webp)



In der Praxis fungiert Dojo als Gateway zwischen Ihrem Wallet und dem Bitcoin-Netz. Ohne Dojo müsste ein leichtgewichtiger mobiler Wallet Server von Drittanbietern abfragen, um den Status Ihrer UTXOs und Ihre Historie zu erhalten oder um Ihre Transaktionen zu übermitteln. Dies bedeutet Abhängigkeit und Weitergabe sensibler Daten an einen Drittanbieter-Server (verwendete Adressen, Beträge, Zahlungsfrequenz usw.). Mit Dojo hosten Sie diesen Server selbst, direkt verbunden mit Ihrem eigenen Bitcoin-Knoten. Auf diese Weise laufen alle Ihre Portfolioanfragen über eine Infrastruktur, die Sie kontrollieren, ohne Zwischenhändler, was Ihre Vertraulichkeit und Souveränität stärkt.



## Voraussetzungen für die Einrichtung eines Dojos



Um einen Dojo-Server einzurichten, braucht man keinen extrem leistungsstarken Rechner. Jeder mit einem Einsteiger-Computer, einer stabilen Internetverbindung und der Fähigkeit, ihn ständig (24/7) eingeschaltet zu lassen, kann ein funktionierendes Dojo einrichten.



### Wählen Sie Ihren Maschinentyp



Sie können verwenden:




- einen Laptop;
- einen Desktop-Computer;
- einen Mini-PC (z. B. Intel NUC, Lenovo Thincentre Tiny...).



Jede Option hat ihre Vor- und Nachteile:




- Preis: Ein generalüberholter Mini-PC oder Desktop ist oft billiger als ein neuer Laptop.
- Platzbedarf: Ein Mini-PC nimmt weniger Platz ein.
- Strom Supply: Ein Laptop hat den Vorteil, dass er im Gegensatz zu einem Mini-PC bei einem Stromausfall nicht heruntergefahren wird.
- Aufrüstbarkeit: Barbones ermöglichen im Allgemeinen das Hinzufügen von Speicher oder den einfachen Austausch einer Hard-Platte.



Für weitere Informationen zur Auswahl Ihrer Ausrüstung empfehle ich Ihnen diesen Kurs:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Empfohlene Ausrüstung



Es ist nicht nötig, einen neuen Computer zu kaufen. Ein generalüberholter Computer mit den unten aufgeführten Spezifikationen bietet eine viel bessere Leistung als Einplatinen-Elektronik (wie der Raspberry Pi).



**Mindestanforderungen:**




- X86-64-Architektur (64-Bit-Prozessor).
- 2 GHz Dual-Core-Prozessor oder schneller.
- mindestens 8 GB RAM.
- 2 TB oder mehr NVMe-SSD (zum Speichern von Blockchain oder Bitcoin und der erforderlichen Indizes).



**Empfohlenes Betriebssystem: **




- Eine Debian-basierte Distribution, wie Ubuntu 24.04 LTS.



**Empfohlene Ausrüstung:**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- usw.



Es ist durchaus möglich, einen Dojo-Server auf anderen Hardware-Konfigurationen zu betreiben. Um jedoch die beste Leistung zu erzielen und Probleme zu vermeiden, raten wir Ihnen, die oben genannten Empfehlungen zu befolgen.



In diesem Tutorial verwende ich einen alten ThinkCentre Tiny mit einem Intel Pentium Dual-Core G4400T Prozessor, 8 GB RAM und einer 2 TB SSD.



## 1 - Installation von Ubuntu



*Wenn Sie Dojo auf einem Gerät installieren möchten, das bereits konfiguriert ist, können Sie diesen Schritt überspringen und direkt mit Schritt 2.* fortfahren



Nachdem Sie die gewählte Hardware vorbereitet haben, ist es an der Zeit, ein Betriebssystem zu installieren. Sie können praktisch jede Debian-Distribution verwenden, aber ich empfehle Ihnen, sich für eine LTS-Version von Ubuntu zu entscheiden, da sie für unsere Zwecke perfekt geeignet ist. Hier sind die zu befolgenden Schritte:



### 1.1. einen bootfähigen USB-Stick erstellen



Laden Sie von einem bereits funktionierenden Computer (Ihrem üblichen Rechner) das Ubuntu LTS-ISO-Image [von der offiziellen Website] (https://ubuntu.com/download/desktop) herunter (zum Zeitpunkt der Erstellung dieses Dokuments `24.04`, aber nehmen Sie das neueste, falls ein anderes verfügbar ist).



![Image](assets/fr/02.webp)



Stecken Sie einen USB-Stick von mindestens 8 GB in diesen Computer und erstellen Sie dann einen bootfähigen Stick mit einer Software wie [Balena Etcher] (https://etcher.balena.io/). Wählen Sie das soeben heruntergeladene Ubuntu-ISO-Image aus, wählen Sie den USB-Stick als Zielgerät und starten Sie dann den Erstellungsprozess (haben Sie etwas Geduld, es kann einige Minuten dauern).



![Image](assets/fr/03.webp)



Stecken Sie den bootfähigen USB-Stick in den ausgeschalteten Computer (den, auf dem Sie Dojo ausführen möchten). Starten Sie den Computer und drücken Sie sofort **F12** oder **F10** auf Ihrer Tastatur (je nach Modell), um das Bootmenü aufzurufen. Wählen Sie dann Ihren USB-Stick als vorrangiges Gerät in der Startreihenfolge des Computers.



![Image](assets/fr/04.webp)



### 1.2. Installieren Sie das Betriebssystem



Der Startbildschirm von Ubuntu wird angezeigt. Wählen Sie "Ubuntu* ausprobieren oder installieren".



![Image](assets/fr/05.webp)



Folgen Sie dann dem klassischen Ubuntu-Installationsprozess:




- Sprache auswählen.
- Wählen Sie den Tastaturtyp.
- Wenn Sie über ein RJ45-Kabel verbunden sind, müssen Sie kein Wi-Fi konfigurieren.
- Klicken Sie auf "*Ubuntu installieren*" und aktivieren Sie die Option zur Installation von Software von Drittanbietern (Wi-Fi-Treiber, Multimedia-Codecs usw.).
- Wenn der Assistent nach der Art der Installation fragt, wählen Sie "*Datenträger löschen und Ubuntu installieren*". **Warnung**: Dieser Vorgang löscht den Inhalt des Datenträgers vollständig. Überprüfen Sie sorgfältig, dass die von Ihnen gewählte Festplatte der für Dojo vorgesehenen NVMe-SSD entspricht.
- Erstellen Sie einen einfachen Benutzernamen (z. B. "*loic*").
- Weisen Sie dem Rechner einen Namen zu (z. B. "*dojo-node*").
- Legen Sie ein sicheres Passwort fest und bewahren Sie es sicher auf.
- Aktivieren Sie die Option "*Mein Passwort anfordern, um sich anzumelden*", um die Sicherheit zu erhöhen.
- Geben Sie Ihre Zeitzone an und klicken Sie dann auf "*Installieren*".
- Warten Sie, bis die Installation abgeschlossen ist. Sobald die Installation abgeschlossen ist, wird das System automatisch neu gestartet.
- Entfernen Sie den USB-Installationsschlüssel, wenn Sie den Computer neu starten.



Weitere Details zum Ubuntu-Installationsprozess finden Sie in unserem speziellen Tutorial:



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. System-Update



Öffnen Sie nach dem ersten Start ein Terminal mit der Tastenkombination ***Strg + Alt + T*** und führen Sie die folgenden Befehle aus, um das System zu aktualisieren:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Installation von Nebengebäuden



Damit Dojo richtig funktioniert, müssen bestimmte Software-Bausteine auf Ihrem System vorhanden sein. Diese werden für die Verwaltung von Software-Repositories, die Kommunikation, die Dekomprimierung von Archiven und die Ausführung von Dojo in Docker-Containern verwendet. Alle diese Vorgänge werden im Terminal ausgeführt.



### 2.1. Vorbereitung



Mit dem folgenden Befehl kehren Sie zu Ihrem persönlichen Ordner zurück. Dies ist eine gute Übung, bevor Sie eine Reihe von Installationen durchführen.



```bash
cd ~/
```



Vergewissern Sie sich vor der Installation von Software, dass die Datenbank der auf Ihrem Computer verfügbaren Software auf dem neuesten Stand ist. So vermeiden Sie die Installation veralteter Versionen.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. Dienstprogramme installieren



Das System muss um mehrere Instrumente erweitert werden:




- `apt-transport-https`: ermöglicht das sichere Herunterladen von Paketen über HTTPS
- `ca-certificates`: verwaltet die für verschlüsselte Verbindungen erforderlichen Zertifikate
- `curl`: zum Abrufen von Dateien aus dem Internet
- gnupg-agent": für die GPG-Schlüsselverwaltung
- software-properties-common`: bietet Dienstprogramme für die Bearbeitung von APT-Repositories
- `unzip`: entpackt Dateien im ZIP-Format



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Während der Installation kann das System Sie um eine Bestätigung bitten. Drücken Sie die Taste "*y*" und dann "*Eingabe*".



![Image](assets/fr/08.webp)



### 2.3. Torsocks installieren



Mit Torsocks können bestimmte Befehle über das Tor-Netzwerk ausgeführt werden, wodurch die Vertraulichkeit der Kommunikation verbessert wird.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. Docker und Docker Compose installieren



Dojo wird innerhalb von Docker-Containern ausgeführt. Dies bedeutet, dass jeder Dienst in einer unabhängigen Umgebung isoliert ist, was die Wartung und Sicherheit vereinfacht. Dazu müssen Sie Docker und das Tool Docker Compose installieren, mit dem Sie mehrere Container gleichzeitig verwalten können.



#### Docker-Signierschlüssel hinzufügen



Docker bietet seinen eigenen digitalen Signaturschlüssel. Durch Hinzufügen dieses Schlüssels wird die Authentizität der heruntergeladenen Pakete überprüft.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Offizielles Docker-Repository hinzugefügt



Als nächstes müssen Sie dem System mitteilen, wo die offiziellen Docker-Pakete zu finden sind. Dieser Befehl fügt ein neues Repository zu Ihrer Paketmanager-Konfiguration hinzu.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Installation von Docker und Docker Compose



Die wichtigsten Docker-Komponenten können nun installiert werden.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Benutzerberechtigung



Standardmäßig können nur Befehle, die mit Administratorrechten ausgeführt werden, Docker starten. Für mehr Komfort empfehle ich, Ihren aktuellen Benutzer zur Gruppe "*docker*" hinzuzufügen. Dadurch können Sie Docker verwenden, ohne jedes Mal "sudo" eingeben zu müssen.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Erstellung eines einzelnen Benutzers (optional)



Wenn Sie die Sicherheit Ihres Systems verbessern wollen, empfehle ich Ihnen, einen separaten Benutzer ausschließlich für die Ausführung von Dojo zu erstellen. Diese Trennung begrenzt die Risiken: Wenn ein Sicherheitsproblem in Dojo auftritt, wird es nicht direkt Ihr Hauptkonto gefährden.



### 3.1. Erstellung eines Benutzerkontos



Der folgende Befehl erstellt einen neuen Benutzer namens "*dojo*". Dieser Benutzer hat ein Home-Verzeichnis `/home/dojo` und Zugriff auf das Bash-Terminal. Er wird auch der sudo-Gruppe hinzugefügt, um die Ausführung von Admin-Befehlen zu ermöglichen.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Festlegen eines Passworts



Es ist wichtig, für dieses Konto ein sicheres Passwort zu vergeben. Idealerweise sollten Sie einen Passwort-Manager wie Bitwarden verwenden, um generate eine lange, Hard zu erratende Kombination zu geben.



```bash
sudo passwd dojo
```



Das System fordert Sie dann auf, das von Ihnen gewählte Passwort einzugeben und ein zweites Mal zu bestätigen.



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Benutzer für die Verwendung von Docker autorisieren



Damit der Benutzer "*dojo*" die zur Ausführung von Dojo benötigten Container starten kann, muss er der Docker-Gruppe hinzugefügt werden. Dadurch wird vermieden, dass jedem Befehl ein "sudo" vorangestellt werden muss.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Neustart des Systems



Damit die Gruppenänderungen wirksam werden, muss der Rechner neu gestartet werden.



```bash
sudo reboot
```



### 3.5. Anmeldung mit neuem Benutzer



Wenn das System neu gestartet wird, melden Sie sich mit dem Login ***dojo*** und dem zuvor festgelegten Passwort an. Alle nachfolgenden Schritte müssen von diesem speziellen Konto aus durchgeführt werden.



## 4. Dojo herunterladen und überprüfen



Bevor Sie Dojo installieren, müssen Sie sicherstellen, dass die Dateien vom offiziellen Entwickler stammen und nicht verändert wurden. Dieser Schritt beruht auf der Verwendung von PGP und Hashes, um die Authentizität und Integrität der Dateien zu überprüfen.



### 4.1. Importieren Sie den PGP-Schlüssel des Entwicklers



Laden Sie den öffentlichen Schlüssel des Entwicklers über Tor herunter und importieren Sie ihn in Ihren lokalen Schlüsselbund. Dieser Schlüssel wird verwendet, um die mit Dojo-Dateien verbundenen Signaturen zu überprüfen.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. laden Sie die neueste Version von Dojo herunter



Rufen Sie das komprimierte Archiv ab, das den Dojo-Quellcode enthält. In diesem Beispiel ist die neueste Version `1.27.0`: Ändern Sie den Befehl entsprechend [die neueste Version hier im offiziellen GitHub Repository](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Fingerabdrücke und Unterschrift herunterladen



Die Entwickler veröffentlichen eine Datei, in der die digitalen Fingerabdrücke der Archive aufgelistet sind, sowie eine mit ihrem PGP-Schlüssel signierte Datei. Laden Sie sie herunter, um Ihre Dateien lokal zu vergleichen.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. PGP-Signatur prüfen



Überprüfen Sie, ob die Fingerabdruckdatei mit dem importierten Schlüssel signiert wurde.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Ein korrektes Ergebnis zeigt eine gültige Signatur mit dem Schlüssel `E53AD419B242822F19E23C6D3033D463D6E544F6` und dem zugehörigen Address `dojocoder@pm.me` an. Es kann eine Warnung erscheinen, die besagt, dass der Schlüssel nicht zertifiziert ist: Sie können sie ignorieren.



Ist die Signatur hingegen ungültig, brechen Sie den Installationsvorgang sofort ab und beginnen Sie von vorne.



![Image](assets/fr/17.webp)



### 4.5. Integrität des Archivs prüfen



Berechnen Sie den SHA256-Fingerabdruck der heruntergeladenen Datei und öffnen Sie dann die Fingerabdruckdatei, um die beiden Werte zu vergleichen.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Wenn die beiden Fingerabdrücke identisch sind, können Sie sicher sein, dass das Archiv nicht verändert wurde. Wenn die Fingerabdrücke unterschiedlich sind, löschen Sie die Dateien.



![Image](assets/fr/18.webp)



### 4.6. Dateien extrahieren und organisieren



Sobald die Überprüfung erfolgreich abgeschlossen ist, können Sie das Archiv entpacken und einen Ordner für die Dojo-Installation vorbereiten.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Unnötige Dateien bereinigen



Löschen Sie temporäre Dateien und nicht mehr benötigte Archive, um Ihre Umgebung sauber zu halten.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Dojo-Konfiguration



Dojo ist ein Backend-Server, der mehrere Dienste zusammenführt, um mit Ihrem Portfolio zu interagieren und Ihren Bitcoin-Knoten zu verwalten. Seine Konfiguration kann komplex sein, aber das Projekt bietet eine vereinfachte Methode, die automatisch die folgenden Komponenten installiert und konfiguriert:




- Dojo (Haupt-API)
- Bitcoin core (vollständiger Knoten Bitcoin)
- BTC-RPC Entdecker (Web Block explorer)
- Fulcrum Indexer (schnelle Indizierung von Blöcken und Transaktionen)
- Fulcrum Electrum Server im Tor-Netzwerk verfügbar
- Fulcrum Electrum Server im lokalen Netzwerk verfügbar
- Beglaubigung der Verwaltung



### 5.1. Beglaubigung der Verwaltung



Um den Zugang zu den verschiedenen Diensten zu sichern, müssen Sie mehrere eindeutige Identifikatoren generate verwenden:




- bITCOIND_RPC_USER
- bITCOIND_RPC_PASSWORD
- mYSQL_ROOT_PASSWORD`
- mYSQL_USER
- mYSQL_PASSWORD
- nODE_API_KEY`
- kNOTEN_ADMIN_SCHLÜSSEL"
- nODE_JWT_SECRET



Diese Kennungen **müssen eindeutig sein** (dies ist sehr wichtig: Sie dürfen nicht dasselbe Passwort für mehrere Dienste verwenden), ausschließlich aus Zahlen, Groß- und Kleinbuchstaben bestehen (alphanumerisch) und etwa 40 Zeichen lang sein, um ein hohes Maß an Sicherheit zu gewährleisten. Auch hier empfehle ich dringend die Verwendung eines Passwortmanagers.



### 5.2. Zugriff auf Konfigurationsdateien



Dojo-Konfigurationsdateien befinden sich im Ordner `conf/`. Wechseln Sie in dieses Verzeichnis:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Bitcoin core-Konfiguration



Öffnen Sie die Bitcoin core-Konfigurationsdatei mit dem Texteditor nano:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



In dieser Datei geben Sie die generierten Bezeichner ein:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ ***Ersetzen Sie "your-ID-here" und "your-password-here" durch Ihre eigenen Logins (mit einem sicheren Passwort)



Sie können auch die Größe des von Bitcoin core verwendeten Cache-Speichers anpassen, um die Leistung zu verbessern (Sie können sogar mehr verwenden, wenn Sie viel RAM zur Verfügung haben):



```
BITCOIND_DB_CACHE=2048
```



Um Ihre Änderungen zu speichern und den Editor zu schließen:




- drücken Sie `Strg + X
- typ `y`
- und drücken Sie dann "*Eingabe*"



### 5.4. MySQL-Konfiguration



Öffnen Sie dann die Konfiguration der MySQL-Datenbank:



```bash
nano docker-mysql.conf.tpl
```



Bitte geben Sie Ihre Anmeldedaten ein:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ ***Ersetzen Sie `Ihre-ID-hier` und `Ihr-Passwort-hier` durch Ihre eigenen Logins (mit starken, eindeutigen Passwörtern).***



Speichern Sie auf die gleiche Weise (Strg + X, y, *Eingabe*).



![Image](assets/fr/23.webp)



### 5.5. Konfiguration des Fulcrum-Indexers



Öffnen Sie die folgende Datei:



```bash
nano docker-indexer.conf.tpl
```



Fügen Sie die Parameter hinzu, um Fulcrum zu aktivieren und es korrekt in Dojo zu integrieren:



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



Als nächstes gibt es 2 Möglichkeiten, abhängig von Ihrer Konfiguration. Wenn Dojo auf einem Rechner installiert ist, der von Ihrem normalen Computer getrennt ist (auf einem dedizierten Rechner, einem Server...), geben Sie dessen IP Address in Ihrem lokalen Netzwerk ein, zum Beispiel :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Um die lokale IP Address Ihres Rechners herauszufinden, öffnen Sie ein anderes Terminal und geben Sie den folgenden Befehl ein:



```bash
hostname -I
```



Zweite Möglichkeit: Wenn Dojo direkt auf dem PC ausgeführt wird, behalten Sie den Standardwert bei, der bereits in der Konfigurationsdatei vorhanden ist:



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Speichern Sie und beenden Sie den Editor (`Strg + X`, `y`, "*Eingabe*").



### 5.6. Konfiguration des Knotendienstes



Öffnen Sie schließlich die Konfiguration des Hauptdienstes von Dojo:



```bash
nano docker-node.conf.tpl
```



Bitte geben Sie Ihre Anmeldedaten ein:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ ***Ersetzen Sie `Ihr-Passwort-hier` durch Ihre eigenen Anmeldedaten (mit starken, eindeutigen Passwörtern).***



![Image](assets/fr/26.webp)



Aktivieren Sie dann den lokalen Indexer:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Speichern Sie und beenden Sie den Editor (`Strg + X`, `y`, "*Eingabe*").



### 5.7. Login-Verwaltung



Wenn die Konfiguration abgeschlossen ist, müssen nicht alle erzeugten Kennungen gespeichert werden. Die einzige Kennung, die unbedingt gespeichert werden muss, ist :



```
NODE_ADMIN_KEY
```



Mit diesem Login können Sie sich später in das Dojo-Wartungstool einloggen. Alle anderen Logins können aus Ihrem Passwort-Manager oder Ihren handschriftlichen Notizen entfernt werden. Sie bleiben über die Dojo-Konfigurationsdateien zugänglich, falls Sie sie in Zukunft abrufen müssen.



## 6. Dojo-Installation



In diesem Stadium wird Dojo auf Ihrem Rechner installiert und gestartet. Bei diesem Vorgang werden mehrere Dienste gestartet (Bitcoin core, der Fulcrum-Indexer, das Dojo-Backend usw.) und eine vollständige Synchronisierung der Blockchain Bitcoin eingeleitet. Dies kann je nach Ihrer Hardware und Internetverbindung mehrere Tage dauern.



### 6.1. Prüfen Sie, ob Docker ordnungsgemäß funktioniert



Vergewissern Sie sich vor Beginn der Installation, dass Docker betriebsbereit ist. Führen Sie den folgenden Befehl aus:



```bash
docker run hello-world
```



Mit diesem Befehl wird ein kleiner Testcontainer heruntergeladen und gestartet. Wenn alles korrekt funktioniert, sollten Sie eine Meldung ähnlich der folgenden sehen:



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Wenn diese Meldung nicht angezeigt wird, starten Sie Ihren Rechner mit neu:



```bash
sudo reboot
```



Melden Sie sich dann wieder bei Ihrem **dojo**-Konto an und führen Sie den Testbefehl erneut aus. Wenn der Fehler weiterhin auftritt, wurde Docker nicht korrekt installiert. Gehen Sie in diesem Fall zurück zu Schritt `2.4.` über die Installation von Docker und überprüfen Sie jeden Befehl sorgfältig.



### 6.2. Gehen Sie zum Dojo-Installationsverzeichnis



Die für die Installation erforderlichen Skripte befinden sich im Ordner `my-dojo`. Wechseln Sie in dieses Verzeichnis:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Verwenden Sie den Befehl `ls`, um zu überprüfen, ob die Datei `dojo.sh` vorhanden ist. Dies ist das Hauptskript, das die Installation von Dojo und den Start aller seiner Dienste automatisiert.



![Image](assets/fr/29.webp)



### 6.3. Installation starten



Starten Sie die Installation durch Ausführen der Datei :



```bash
./dojo.sh install
```



Bestätigen Sie die Installation durch Drücken von "y" und dann "*Enter*".



![Image](assets/fr/30.webp)



Dieses Skript wird :




- die erforderlichen Docker-Container herunterladen und starten,
- initialisierung von Bitcoin core und Beginn der Synchronisierung von Blockchain,
- den Fulcrum-Indexer starten, um Transaktionen und Adressen zu verfolgen,
- aktivieren Sie das Dojo-Backend und seine APIs.



Sie werden einen stetigen Strom von Protokollen sehen, die mit bunten Verweisen wie `bitcoind`, `soroban`, `nodejs` oder `fulcrum` vorbeiziehen. Dieses Scrollen zeigt an, dass Dojo läuft und beginnt, die verschiedenen Dienste auszuführen.



![Image](assets/fr/31.webp)



### 6.4. Beenden der Protokollanzeige



Die Protokolle erscheinen in Echtzeit in Ihrem Terminal. Um zur Eingabeaufforderung zurückzukehren, während Dojo im Hintergrund ausgeführt wird, geben Sie ein:



```
Ctrl + C
```



Keine Sorge: Wenn Sie die Protokollanzeige stoppen, werden die Dienste nicht gestoppt. Docker führt Dojo im Hintergrund weiter aus (Sie müssen den Computer natürlich nicht anhalten, wenn Sie möchten, dass IBD weiterläuft).



### 6.5. Verstehen des *Initial Block Download* (IBD)



Beim Start muss Bitcoin core den gesamten Blockchain seit 2009 herunterladen und verifizieren. Dieser Schritt wird ***Initial Block Download* (IBD)** genannt. Er ist unerlässlich, da er es Ihrem Dojo-Knoten ermöglicht, jeden Bitcoin-Block und jede Transaktion unabhängig zu überprüfen.



Die Dauer dieser Synchronisation hängt von mehreren Faktoren ab:




- die Leistung Ihres Prozessors und die Größe des verfügbaren RAM-Speichers,
- die Geschwindigkeit Ihrer Festplatte,
- die Anzahl und Qualität der Peers, mit denen sich Ihr Knoten verbindet,
- die Geschwindigkeit Ihrer Internetverbindung.



In der Praxis dauert dieser Vorgang im Allgemeinen zwischen **2 und 7 Tagen**. Während dieses Zeitraums können Sie Ihren Rechner ununterbrochen laufen lassen. Je länger der Rechner eingeschaltet ist, desto schneller wird die Synchronisierung abgeschlossen sein. Ich empfehle Ihnen, den Synchronisierungsstatus regelmäßig zu überprüfen, indem Sie die Bitcoin core-Protokolle einsehen oder das Dojo-Wartungstool nach der Installation verwenden (siehe nächster Abschnitt).



Um Ihr Wissen über IBD und ganz allgemein über die Funktionsweise und die Rolle Ihres Bitcoin-Knotens zu vertiefen, empfehle ich Ihnen, diesen Kurs zu besuchen:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Überwachung der Synchronisation



Wenn Sie Dojo zum ersten Mal installieren, müssen Sie warten, bis zwei wichtige Vorgänge vollständig abgeschlossen sind: der vollständige Download des Blockchain Bitcoin (*IBD*) und die Indizierung dieses Blockchain durch Fulcrum. Je nach Ihrer Verbindung und der Leistung Ihres Computers kann dies mehrere Tage dauern. Während dieser Zeit können Sie den Fortschritt des Prozesses überwachen, um sicherzustellen, dass alles reibungslos abläuft.



Es gibt zwei Möglichkeiten, den Status der Synchronisierung zu überwachen:




- verwendung des Dojo-Wartungstools (oder DMT), das einfach ist, aber nur wenige Details während der IBD liefert;
- direkte Konsultation der Dojo-Protokolle auf Ihrem Rechner, technisch anspruchsvoller, aber viel präziser.



### 7.1. Überprüfung über das Dojo Maintenance Tool (DMT)



Das Dojo Maintenance Tool ist ein sicheres, webbasiertes Interface, mit dem Sie den Status Ihrer Anlage überwachen und bestimmte Vorgänge durchführen können. Es ist der einfachste und zugänglichste Weg, um den Fortschritt der IBD zu überwachen. Während der anfänglichen Synchronisierungsphase können die angezeigten Informationen begrenzt sein. So zeigt der DMT beispielsweise nicht den detaillierten Fortschritt der Fulcrum-Indexierung an. Sobald die Synchronisierung abgeschlossen ist, zeigt das DMT jedoch deutlich an:




- alle Lichter am Green;
- der letzte validierte Block für jeden Dienst (Node, Indexer, Dojo DB).



Um darauf zuzugreifen, musst du die URL deines DMT kennen und dich mit ihm [über den Tor-Browser] verbinden (https://www.torproject.org/download/). Dazu öffnest du ein Terminal und gehst in das Verzeichnis `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Führen Sie dann den folgenden Befehl aus:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Du hast dann Zugang zu allen Informationen, die sich auf die Verbindungen zu deinem Dojo über Tor beziehen. Die URL, die uns hier interessiert, ist die folgende:



```
Dojo API and Maintenance Tool =
```



Um auf den DMT von einem beliebigen Rechner in einem beliebigen Netzwerk zuzugreifen (auch aus der Ferne), öffne den Tor-Browser und gib diese URL gefolgt von `/admin` ein. Wenn deine URL zum Beispiel `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion` ist, musst du sie in die [Tor Browser](https://www.torproject.org/download/) Leiste eingeben:



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Bitte behandeln Sie diesen Address streng vertraulich



Sie werden dann auf eine Authentifizierungsseite weitergeleitet. Das DMT wird mit dem zuvor erstellten Passwort "NODE_ADMIN_KEY" angemeldet.



![Image](assets/fr/33.webp)



Sobald Sie eingeloggt sind, können Sie auf das *Dojo Maintenance Tool* zugreifen! Während IBD können Sie im Menü "*Full node*" die Information "*Latest Block*" sehen, die Sie über den aktuellen Status Ihres Bitcoin-Knotens informiert.



![Image](assets/fr/34.webp)



Vergiss nicht, ein Lesezeichen für diesen Address im Tor Browser zu setzen, damit du ihn später leicht wiederfinden kannst.



Sobald Ihr Dojo vollständig synchronisiert ist, sollten Sie Green check ✅ auf allen Indikatoren auf der DMT-Startseite sehen.



### 7.2. Verifizierung über Dojo-Protokolle



Die zweite Möglichkeit, den Fortschritt Ihrer IBD zu verfolgen, besteht darin, Ihre Maschinenprotokolle direkt einzusehen. Dieser Ansatz bietet eine viel präzisere Überwachung in Echtzeit. Sie können sehen, wie Bitcoin core beim Herunterladen von Blöcken vorankommt und wie Fulcrum sie indiziert.



Verbinden Sie sich mit dem Rechner, auf dem Ihr Dojo läuft, und öffnen Sie ein Terminal. Alle Befehle sollten aus dem Verzeichnis `my-dojo` ausgeführt werden. Positionieren Sie sich in diesem Ordner:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Bitcoin core-Protokolle



Zeigen Sie Bitcoin core-Protokolle an, um den IBD-Fortschritt zu verfolgen:



```bash
./dojo.sh logs bitcoind
```



Zu Beginn sehen Sie eine Vorsynchronisationsphase der Blockköpfe:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



Wenn diese Zahl 100 % erreicht, beginnt Bitcoin core mit dem vollständigen Download von Blockchain. Sie werden den IBD-Fortschritt sehen. Um die aktuelle Blockhöhe zu ermitteln, schauen Sie sich den Wert an, der durch `height=` angezeigt wird. Sie können auch den Schlüssel `progress=` verfolgen, der den prozentualen IBD-Fortschritt anzeigt.



![Image](assets/fr/36.webp)



Um die Protokolle zu schließen und zur Eingabeaufforderung zurückzukehren, drücken Sie wie immer die Tastenkombination "Strg + C".



#### Fulcrum-Protokolle



Sobald Bitcoin core die Vorsynchronisierung des Headers abgeschlossen hat, beginnt Fulcrum mit der Indizierung von Blockchain, während es weiterläuft. Betrachten Sie seine Protokolle mit :



```bash
./dojo.sh logs fulcrum
```



Sie sehen dann die Höhe des zuletzt indizierten Blocks, die nach `Höhe:` angezeigt wird, sowie den Prozentsatz des Indizierungsfortschritts.



![Image](assets/fr/37.webp)



### 7.3. Beschädigung der Fulcrum-Datenbank



Fulcrum ist ein besonders leistungsfähiger Indexer, aber seine Installation kann kompliziert sein, nicht zuletzt wegen seiner empfindlichen Datenbankverwaltung. Im Falle eines Stromausfalls oder eines plötzlichen Herunterfahrens der Maschine während der ersten Synchronisierung kann die Datenbank des Indexers beschädigt werden. Sie können dies zum Beispiel an den folgenden Protokollen sehen:



```bash
fulcrum | The database has been corrupted etc...
```



**Hinweis:** Diese Art von Fehler sollte mit der kommenden Version von Fulcrum 2.0 behoben werden.



Sollte dies bei Ihnen der Fall sein, hat dies keine Auswirkungen auf bitcoind (Ihren Bitcoin-Knoten): Sein IBD wird unabhängig von Fulcrum weiterlaufen. Sie können Fulcrum jedoch erst dann wieder benutzen, wenn Sie die beschädigten Daten gelöscht und die Synchronisierung von Anfang an neu gestartet haben. So funktioniert es:



Dojo anhalten:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Löschen Sie nur den Fulcrum-Container und das Volumen:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Normalerweise lautet der Name `my-dojo_data-fulcrum`, wenn dies bei Ihnen nicht der Fall ist, passen Sie den vom vorherigen Befehl zurückgegebenen Namen an.



Dann starten Sie Dojo neu und bauen Fulcrum von Grund auf neu auf:



```bash
./dojo.sh upgrade
```



Sie können dann anhand der Protokolle überprüfen, ob Fulcrum ordnungsgemäß funktioniert:



```bash
docker logs -f fulcrum
```




## 8. Verwendung des Dojo-Wartungswerkzeugs



Sobald Ihr Bitcoin-Knoten mit dem Proof of Work auf den Kettkopf synchronisiert ist und der Blockchain von Fulcrum zu 100% indexiert wurde, können Sie Ihr Dojo benutzen.



Ihr Dojo bietet eine breite Palette von Funktionen, die mit jeder neuen Version regelmäßig verbessert werden. Meiner Meinung nach sind die 2 wichtigsten davon :




- die Möglichkeit, Ihren Ashigaru Wallet anzuschließen, um Ihren eigenen Knotenpunkt zu nutzen, um Blockchain-Daten abzufragen und Ihre Transaktionen zu übertragen,
- und den Block explorer, der Ihnen Zugang zu Informationen über den Blockchain Bitcoin verschafft, ohne Ihre Daten einer externen Instanz zugänglich zu machen, die Sie nicht kontrollieren.



Wir wollen herausfinden, wie man sie benutzt.


### 8.1. Verbinde Ashigaru mit deinem Dojo



Das Verbinden Ihres Ashigaru Wallet mit Ihrem Dojo ist sehr einfach: Öffnen Sie auf Ihrem DMT das Menü "*Paarung*". Es erscheint ein QR-Code, den Sie direkt mit der Ashigaru-Anwendung scannen können.



![Image](assets/fr/38.webp)



Wenn Sie die Ashigaru-Anwendung nach dem Erstellen oder Wiederherstellen Ihrer Wallet zum ersten Mal starten, werden Sie auf die Seite "*Konfigurieren Sie Ihren Dojo-Server*" weitergeleitet. Drücken Sie auf "*Scan QR*" und scannen Sie dann den auf Ihrem DMT angezeigten QR-Code.



![Image](assets/fr/39.webp)



Klicken Sie dann auf die Schaltfläche "*Fortfahren*".



![Image](assets/fr/40.webp)



Sie sind jetzt mit Ihrem Dojo verbunden.



![Image](assets/fr/41.webp)



### 8.2. Verwendung des Block explorer



Dojo installiert automatisch einen Block explorer, [BTC-RPC Explorer] (https://github.com/janoside/btc-RPC-explorer), der direkt auf die Daten Ihres eigenen Bitcoin Knotens zugreift. Ein Explorer ermöglicht Ihnen den Zugriff auf Rohdaten von Blockchain und Ihrem Mempool über ein leicht verständliches Interface-Web. So können Sie z. B. den Status einer ausstehenden Transaktion überprüfen, den Saldo eines Address einsehen oder die Zusammensetzung eines Blocks mit Leichtigkeit untersuchen.



Um darauf zuzugreifen, rufe einfach den Tor Address von deinem Browser ab. Führe dazu denselben Befehl aus, mit dem du den Address deines DMTs abgerufen hast:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Über Tor hast du Zugriff auf alle deine Dojo-Verbindungsinformationen. Die URL, die uns hier interessiert, ist die folgende:



```
Block Explorer =
```



Wenn Sie bereits mit Ihrem DMT verbunden sind, können Sie diesen Address auch im Menü "*Pairing*" innerhalb des Verbindungs-JSON finden:



![Image](assets/fr/43.webp)



Um von einem beliebigen Rechner in einem beliebigen Netzwerk (auch aus der Ferne) auf deinen Browser zuzugreifen, öffne [Tor Browser] (https://www.torproject.org/download/) und gib die URL ein, die du gerade abgerufen hast.



⚠️ **Bitte behandeln Sie diese Address streng vertraulich



Sie haben dann Zugang zu Ihrem eigenen Block explorer.



![Image](assets/fr/44.webp)



*Bildnachweis: https://ashigaru.rs/.*



Um eine Transaktion zu verfolgen, geben Sie einfach ihre txid in die Suchleiste oben rechts ein.



![Image](assets/fr/45.webp)



*Bildnachweis: https://ashigaru.rs/.*



Um die mit einem Address verbundenen Bewegungen zu überprüfen, geben Sie den Address in die Suchleiste ein.



![Image](assets/fr/46.webp)



*Bildnachweis: https://ashigaru.rs/.*



Sie können auch die Hash oder die Höhe eines Blocks in die Suchleiste eingeben, um Details anzuzeigen.



![Image](assets/fr/47.webp)



*Bildnachweis: https://ashigaru.rs/.*



## 9. Dojo-Wartung



### 9.1 Stoppen Sie Ihr Dojo



Unterbrechen Sie niemals abrupt die Stromzufuhr zu Dojo, da dies bestimmte Datenbanken beschädigen kann, insbesondere den Fulcrum-Indexer. Wenn Sie ihn ausschalten müssen, führen Sie immer ein sauberes Herunterfahren von Dojo durch und schalten Sie dann, sobald alle Verfahren abgeschlossen sind, auch den Rechner aus:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Aktualisieren Sie Ihr Dojo



Dojo wird regelmäßig weiterentwickelt und neue Versionen werden veröffentlicht, um Fehler zu beheben, die Stabilität zu verbessern und neue Funktionen hinzuzufügen. Es ist daher wichtig [regelmäßig nach Updates zu suchen](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) und Ihr Dojo zu aktualisieren. Der Prozess ähnelt der Erstinstallation, erfordert aber, dass Sie bestimmte Dateien durch die neueste verfügbare Version ersetzen, während Sie Ihre Konfiguration beibehalten. Hier sind die detaillierten Schritte, die Sie für ein sauberes und sicheres Update befolgen müssen:



Um die aktuelle Version Ihres Dojos herauszufinden, führen Sie den Befehl :



```bash
./dojo.sh version
```



Obwohl dieser Schritt optional ist, empfehle ich, dass Sie zunächst Ihr Betriebssystem aktualisieren. Dies verringert das Risiko von Inkompatibilitäten und stellt sicher, dass die von Dojo verwendeten Abhängigkeiten auf dem neuesten Stand sind:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Wechseln Sie in das Dojo-Verzeichnis und beenden Sie die aktuellen Dienste:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Starten Sie dann Ihr System neu, um einen Neuanfang zu machen:



```bash
sudo reboot
```



Dojo wird mit digital signierten Dateien geliefert. Diese PGP-Signaturen stellen sicher, dass die Dateien vom Entwickler stammen und in keiner Weise verändert worden sind. Es ist wichtig, dass du sie jedes Mal überprüfst, wenn du Dojo aktualisierst, genauso wie du es bei der ersten Installation getan hast. Beginne damit, den öffentlichen Schlüssel des Entwicklers über Tor herunterzuladen, dann importiere ihn:



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Kehren Sie zu Ihrem persönlichen Verzeichnis zurück:



```bash
cd ~/
```



Lade die neueste Version von Dojo von GitHub über Tor herunter. In diesem Beispiel ist es die Version `1.28.0` (die zum Zeitpunkt des Schreibens noch nicht existiert: dies ist nur ein Beispiel). Vergiss nicht, die Datei und den Link [durch die Version, die du installieren möchtest] zu ersetzen (https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Laden Sie auch die Datei mit den PGP-Fingerabdrücken und der Signatur herunter (denken Sie auch hier daran, die Version im Befehl anzupassen):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Überprüfen Sie, ob die heruntergeladene Fingerabdruckdatei mit dem Schlüssel des Entwicklers signiert wurde:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Ein korrektes Ergebnis sollte angezeigt werden:



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



Es kann eine Warnung erscheinen, dass der Schlüssel nicht zertifiziert ist, aber das ist nicht wichtig. Ist die Signatur hingegen ungültig oder entspricht sie einem anderen Schlüssel, gehen Sie nicht weiter und beginnen Sie erneut mit der Überprüfung der Links.



Berechnen Sie dann den SHA256-Fingerabdruck des Archivs und vergleichen Sie ihn mit der offiziellen Fingerabdruckdatei:



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Wenn die beiden Fingerabdrücke perfekt übereinstimmen, ist das Archiv echt und intakt. Wenn sie sich unterscheiden, löschen Sie die Dateien sofort und fahren Sie nicht fort.



Dekomprimieren Sie das Archiv in Ihrem Heimatverzeichnis:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Kopieren Sie dann den Inhalt in das Dojo-Verzeichnis und überschreiben Sie dabei die alte :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Bei diesem Vorgang bleiben die Konfigurationsdateien in `~/dojo-app/docker/my-dojo/conf` erhalten, aber alle anderen Dateien werden durch die aktualisierten Versionen ersetzt.



Um Ihre Umgebung sauber zu halten, löschen Sie unnötige Dateien:



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Kehren Sie in das Dojo-Skriptverzeichnis zurück und führen Sie den Aktualisierungsbefehl aus:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



Dieser Befehl weist Docker an, die Images mit den neuen Dateien neu zu erstellen und dann automatisch alle Dienste neu zu starten. Überprüfen Sie am Ende des Prozesses die Protokolle, um sicherzustellen, dass Bitcoin core, Fulcrum und Dojo alle korrekt funktionieren:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Wenn die Dienste ohne Fehler starten und die Protokolle zeigen, dass Blöcke verarbeitet werden, ist Ihr Dojo jetzt auf dem neuesten Stand und betriebsbereit.