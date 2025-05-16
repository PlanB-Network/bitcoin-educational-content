---
name: Lightning Network Daemon (Linux)
description: Installieren und Ausführen von Lightning Network Daemon unter Linux
---

![cover-lightning-network-daemon](assets/cover.webp)



Der Lightning Network ist ein zweiter Layer des Bitcoin, der vor allem durch die Schnelligkeit und die niedrigen Kosten der Transaktionen, die er bietet, blitzartige Dimensionen annehmen kann.



In diesem Tutorial werden wir die Lightning Network Daemon-Implementierung auf unserem Linux-Rechner (Ubuntu 24.04-Distribution) installieren.



## Was ist Lightning Network Daemon?



Lightning Network Daemon ist eine vollständige Go-Implementierung des Lightning Network. Sie wurde von Lightning Labs entwickelt und ermöglicht es Ihnen, eine vollständige Instanz eines Lightning-Knotens auf Ihrem Rechner auszuführen.


Mit anderen Worten: Mit dieser Implementierung können Sie :





- Interaktion mit dem Lightning Network**: Mit Hilfe von Befehlszeilen können Sie Lightning-Portfolios erstellen, Zahlungskanäle und -wege verwalten und vieles mehr, direkt von Ihrem Computerterminal aus.
- Verknüpfung eines entfernten Bitcoin-Knotens oder Ihrer eigenen Bitcoin-Core-Instanz**: Mit LND können Sie eine Bitcoin-Instanz verknüpfen und sie als Backend verwenden. Um diese Implementierung zu verwenden, müssen Sie keine Bitcoin-Core-Instanz auf Ihrem Computer ausführen.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Warum ein eigener Lightning-Knoten?


Lightning ist ein Bitcoin-Overlay, das den Übertragungsprozess optimiert und die Transaktionskosten senkt.



Durch die Rotation Ihres Blitzknotens gewinnen Sie Souveränität und Autonomie. Sie haben die Kontrolle über Ihr Geld, also denken Sie daran:



"Nicht Ihre Schlüssel, nicht Ihre Bitcoins."



In diesem Sinne erhöht der Betrieb eines Lightning-Knotens die Sicherheit und Integrität Ihrer Daten auf folgende Weise:





- Totale Kontrolle**: Verwalten Sie Ihre eigenen Zahlungskanäle, werden Sie Ihre eigene Bank und seien Sie Herr über Ihr Vermögen.
- Vertraulichkeit**: Tätigen Sie Transaktionen, ohne sich zum Schutz Ihrer Daten auf Dritte zu verlassen.
- Lernen und Autonomie**: Dank der `lncli`-Befehle können Sie die Lightning zugrundeliegenden Prozesse besser verstehen, indem Sie sie selbst von Ihrem Terminal aus anwenden.
- Dezentralisierung**: Beteiligen Sie sich aktiv an der Stärkung und Dezentralisierung der Bitcoin / Lightning Network.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Sie haben zwei Möglichkeiten, eine Instanz der LND-Implementierung auf unserem Rechner auszuführen. Wir können entweder die Umgebung auf unserem eigenen Rechner einrichten, um sie lokal auszuführen, oder LND über einen Docker-Container installieren. Hier konzentrieren wir uns auf die erste Option und sehen in einem späteren Tutorial, wie wir mit Docker vorgehen.


## LND aus dem Quellcode installieren



### Voraussetzungen


Da LND in Go geschrieben ist, müssen Sie sicherstellen, dass Sie die GoLang-Umgebung und die erforderlichen Abhängigkeiten auf Ihrem Linux-Rechner haben.





- Hardware-Anforderungen:**


Für ein reibungsloses, nahtloses Erlebnis muss Ihr Rechner über die nötige Kapazität verfügen, um Ihren LND Lightning-Knoten auszuführen.



Sie benötigen:


1. **8 GB RAM** für optimale Flüssigkeit,


2. **Ein Multi-Core-Prozessor (Quad-Core oder mehr)** zur effizienten Verwaltung der Aktionen Ihres Knotens,


3. **Mindestens 5 GB Festplattenspeicher** für den Pruned-Node-Modus und 1 TB zur Ausführung von Bitcoin Core (optional bei Verwendung eines Remote-Nodes)





- Nützliche Abhängigkeiten installieren:**


Mit dem folgenden Befehl können Sie auf Ihrem Rechner die Werkzeuge installieren, die Sie für die Ausführung von LND benötigen. Unter anderem müssen Sie `Git`, ein Werkzeug zur Versionsverwaltung, und `make` installieren, das die LND-Implementierung aus dem Quellcode ausführen und erstellen kann.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Installieren Sie GoLang auf Ihrem Linux-Rechner**



Zum Zeitpunkt der Erstellung dieser Anleitung benötigt LND die Version 1.23.6 von Go*** zur Installation.



Wenn Sie bereits eine frühere Version installiert hatten, entfernen Sie diese für die neue Go-Installation.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Konfiguration der Go**-Umgebung


Initialisieren Sie in Ihrer Datei `~/.bashrc` die folgenden Umgebungsvariablen, um Go zu Ihrem Linux-System hinzuzufügen.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Überprüfung der Installation** (auf Französisch)


```bash
go version
```



![go-version](assets/fr/03.webp)


### Klonen Sie das LND GitHub-Repository



Verwenden Sie git, um eine Kopie des LND-Quellcodes lokal auf Ihrem Rechner zu erhalten


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Bauen und installieren



Mit dem zuvor installierten Tool `make` können Sie eine ausführbare Datei aus dem LND-Quellcode erstellen und mit der Installation fortfahren.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Installieren Sie LND auf Ihrem Rechner



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Überprüfung Ihrer Installation** (auf Französisch)



Um sicherzugehen, dass alles reibungslos funktioniert hat, sollten Sie diesen Befehl ausführen, um die aktuelle Version von LND zu erhalten.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Wartung und Upgrades



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **WICHTIG**: LND-Updates können neuere Versionen von Go erfordern. Aktualisieren Sie daher Ihr System, um Abhängigkeitsprobleme bei der Installation zu vermeiden.


### Lightning Network Daemon konfigurieren



Die Konfiguration eines Lightning LND Knotens ist ähnlich wie die von Bitcoin und erfolgt in einer Konfigurationsdatei, die alle Parameter Ihres Knotens enthält. Dazu können Sie im Stammverzeichnis Ihres Rechners einen versteckten Ordner `.LND` anlegen und in diesem Ordner Ihre Konfigurationsdatei `LND.conf` erstellen.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





In der Konfigurationsdatei können Sie Ihren LND-Knoten einrichten.



```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```



## Verstehen Sie Ihre Konfiguration



Es ist wichtig, dass Sie die Mindestkonfiguration kennen, die Sie für eine korrekte und vollständige Installation Ihres LND-Knotens benötigen.



Basierend auf dem Inhalt der Datei `~/.LND/LND.conf`, sind hier die Details der Felder:





- noseedbackup**: Hier können Sie festlegen, ob LND automatische Backups Ihrer Portfolios durchführen soll.  Wenn Sie diese Eigenschaft auf "0" setzen, können Sie die Wiederherstellungsinformationen manuell an einem persönlich gewählten sicheren Ort speichern.





- debuglevel**: Ermöglicht es Ihnen, den Detaillierungsgrad von Fehlern und Protokollen im Falle von Fehlern, die während einer Aktion auftreten, festzulegen.





- Bitcoin.aktiv**: Weist LND an, als Bitcoin-Knoten zu arbeiten und mit dem Bitcoin-Netz zu interagieren.





- Bitcoin.Mainnet**: Legt fest, dass LND eine Verbindung zum Hauptnetz von Bitcoin (Mainnet) herstellt. Sie können die Werte "bitcoind.signet" und "bitcoind.regtest" für die Netze Bitcoin Signet und Bitcoin Regtest festlegen





- Bitcoin.Knoten**: Gibt den Typ des Bitcoin-Knotens an, mit dem LND verbunden werden soll.





- Bitcoin.rpcuser** und **Bitcoin.rpcpassword** : Repräsentieren.


bzw. die Logins (Benutzer, Passwort) für die Verbindung zu Ihrem Bitcoin-Knoten





- bitcoind.zmqpubrawblock** und **bitcoind.zmqpubrawtx**: definieren jeweils ZeroMQ-Endpunkte, um Benachrichtigungen über neue Blöcke und Transaktionen im Bitcoin-Netzwerk zu erhalten.




## Überprüfen Sie Ihre Installation mit LND



Sie werden sich wahrscheinlich vergewissern wollen, dass der Prozess erfolgreich war und dass Sie mit der Lightning Network synchronisieren, um Ihre Knoteninformationen auf dem neuesten Stand zu halten.



Um die LND-Implementierung zu starten und Informationen über Ihren Knoten zu erhalten, geben Sie einfach den Befehl :


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Durchführen von Aktionen am LND



Sobald die Installation abgeschlossen und überprüft ist, können Sie die Software verwenden.


Hier sind die wichtigsten Befehle für den Anfang.



### Ein Portfolio erstellen


Ihr Blitzportfolio ist der erste Schritt bei jeder Maßnahme zur Verwaltung Ihrer Mittel.



⚠️ **WICHTIG**: Notieren Sie sich sorgfältig Ihren 24-Wörter-Satz **seed**. Sie brauchen ihn, um bei Problemen Ihr Geld zurückzubekommen.



Speichern Sie auch Ihr Wallet-Passwort, damit Sie es mit dem Befehl `lncli unlock` entsperren können, wenn Sie Ihren LND-Knoten neu starten.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Prüfen Sie Ihr Guthaben



Konsultieren Sie Ihre Konten direkt von Ihrem Terminal aus:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Informationen über Ihren Knoten



Verwenden Sie den folgenden Befehl, um herauszufinden, welche Kanäle auf Ihrem Knoten aktiv sind.



```bash
lncli listchannels
```



Sie können auch eine Liste der Knoten erhalten, mit denen Sie verbunden sind.



```bash
lncli listpeers
```



### Verwaltung der Kanäle



Ein Lightning-Kanal ermöglicht Ihnen eine **direkte, paarweise Verbindung mit einem anderen Knoten des Lightning Network**. In diesem Kanal können Sie Exchange Satoshis bis zur Kapazität des Kanals frei verwenden.



### Verbinden mit einem Knoten



Die Verbindung zu anderen Lightning-Knoten ist eine grundlegende Maßnahme, wenn Sie aktiv an Lightning teilnehmen und von dessen Leistungsfähigkeit profitieren möchten.



Um eine Verbindung zu einem Peer (Lightning-Knoten) herzustellen, benötigen Sie drei Informationen:




- Der öffentliche Schlüssel des Knotens**: Dies ist die eindeutige Kennung des Knotens im Bitcoin-Netz;
- IP** : Die IP des Rechners, auf dem der Knoten installiert ist;
- PORT** :  Der auf dem Rechner offene Port, der die Kommunikation mit diesem Knoten ermöglicht.



Sie können auf [amboss](https://amboss.space/), einer Plattform, die Informationen über Lightning-Knoten auflistet, Knoten finden, mit denen Sie sich verbinden können.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Stellen Sie sicher, dass Sie sich mit **zuverlässigen Knoten** verbinden, um die Integrität Ihres eigenen Systems zu wahren. Hier sind einige Empfehlungen für die Auswahl der richtigen Verbindungen.





- Geografische Diversifizierung**: Verbindung zu Knotenpunkten in verschiedenen Regionen.





- Reputation**: Wählen Sie Knotenpunkte mit guter Verfügbarkeit.





- Kapazität**: Wählen Sie Knoten mit guter Liquidität.





- Gebühren**: Gebühren für die Weiterleitung von Schecks.


### Einen Zahlungskanal eröffnen


Um einen Zahlungskanal zu eröffnen, vergewissern Sie sich, dass Sie mit dem Peer-Knoten **verbunden** sind, und legen Sie dann die **Kapazität** (die Menge der Satoshis) fest, die Sie in diesem Kanal blockieren möchten.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Erstellen eines Blitzes Invoice



Ein Lightning Invoice steht für eine Zeichenkette, die Ihren Wunsch ausdrückt, Satoshis in Ihrem Lightning Wallet zu erhalten.


Die Erstellung von Lightning-Rechnungen mit Ihrem eigenen Knotenpunkt ermöglicht es Ihnen, Ihre (geografischen und persönlichen) Daten zu schützen und gibt Ihnen 100 % Autonomie bei der Verwaltung Ihrer Mittel.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Bezahlen eines Blitzes Invoice



```bash
lncli payinvoice <FACTURE>
```


### Einen Kanal schließen



Es gibt zwei Möglichkeiten, einen aktiven Channel auf Ihrem aktuellen Knoten zu schließen.





- Kooperative Schließung**: Damit wird der Wunsch Ihres Knotens signalisiert, sich aus dem Zahlungskanal zurückzuziehen, um sicherzustellen, dass die laufenden Aufgaben abgeschlossen und die Daten gesichert werden, um Geldverluste zu vermeiden.


```
lncli closechannel <ID_CANAL>
```




- Erzwungene Schließung**: ⚠️ Diese Aktion sollte nach Möglichkeit vermieden werden, da sie die laufenden Prozesse in Ihrem Zahlungskanal unterbricht und das Risiko von Geldverlusten erhöht.


```
lncli closechannel --force <ID_CANAL>
```


## Bewährte Verfahren und Sicherheit für Ihren LND-Knoten.


Bei der Verwendung eines Bitcoin/Blitzknotens steht die Sicherheit an erster Stelle. Im Folgenden finden Sie einige Punkte, die die Sicherheit Ihrer Installation erhöhen:





- Bewahren Sie Ihren "seed-Satz" an einem sicheren Ort auf, der nicht mit dem Internet verbunden ist.





- Erstellen Sie regelmäßig Sicherungskopien der Datei `~/.LND/channel.backup`: Diese Datei speichert Ihre Channel-Status jedes Mal, wenn ein neuer Channel auf Ihrem Knoten geöffnet (oder ein alter Channel geschlossen) wird.


⚠️ Ermöglicht die Wiederherstellung von Kanälen und die Wiederherstellung von in Zahlungskanälen gesperrten Geldern im Falle eines Datenverlusts oder eines Knotenausfalls



Sie können Ihr Guthaben mit dem folgenden Befehl wiederherstellen, indem Sie den Sicherungspfad für diese Datei angeben:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Stellen Sie sicher, dass Sie die Wiederherstellungswörter und das Kennwort Ihres Lightning Wallet gespeichert haben.
- Halten Sie Ihr System auf dem neuesten Stand.



## Aktuelle Fehlersuche


### Häufige Probleme




- bitcoind Verbindungsfehler** : Überprüfen Sie Ihre RPC-Anmeldedaten
- Synchronisierung blockiert** : Überprüfen Sie Ihre Internetverbindung
- Berechtigungsfehler**: Überprüfen Sie die Rechte des Ordners `~/.LND`




Sie sind also am Ende dieses Tutorials angelangt. Wenn Sie mehr über Lightning erfahren möchten, bieten wir Ihnen diesen Einführungskurs an, um Ihnen ein besseres Verständnis für die Konzepte und Verfahren hinter dem Lightning Network zu vermitteln.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb