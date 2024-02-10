---
name: Watch Tower
description: Verständnis und Nutzung eines Wachturms
---

## Wie funktionieren Wachtürme?

Als wesentlicher Bestandteil des Lightning-Netzwerks bieten Wachtürme einen zusätzlichen Schutz für die Lightning-Kanäle der Benutzer. Ihre Hauptaufgabe besteht darin, die Gesundheit der Kanäle im Auge zu behalten und einzugreifen, wenn eine Partei versucht, die andere zu betrügen.

Wie kann ein Wachturm feststellen, ob ein Kanal kompromittiert wurde? Der Wachturm erhält die benötigten Informationen vom Client, einer der Kanalparteien, um Verstöße ordnungsgemäß zu identifizieren und darauf zu reagieren. Die aktuellsten Transaktionsdetails, der aktuelle Zustand des Kanals und die Informationen, die zur Erstellung von Straftransaktionen erforderlich sind, werden häufig in diesen Informationen enthalten sein. Bevor die Daten an den Wachturm übertragen werden, kann der Client sie möglicherweise verschlüsseln, um die Privatsphäre und Geheimhaltung zu schützen. Dadurch wird verhindert, dass der Wachturm die verschlüsselten Daten entschlüsseln kann, es sei denn, es hat tatsächlich einen Verstoß gegeben, selbst wenn er die Daten erhält. Dieses Verschlüsselungssystem schützt die Privatsphäre des Clients und verhindert auch, dass der Wachturm ohne Autorisierung auf private Daten zugreifen kann.

## So richten Sie Ihr eigenes Auge von Satoshi ein und beginnen mit der Beitragserstellung

Das Auge von Satoshi ([RUST-TEOS](https://github.com/talaia-labs/rust-teos?ref=blog.summerofbitcoin.org)) ist ein nicht verwahrender Lightning-Wachturm, der mit [BOLT 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org) kompatibel ist. Es besteht aus zwei Hauptkomponenten:

1. teos: einschließlich einer Befehlszeilenschnittstelle (CLI) und der serverseitigen Kernfunktionalität des Wachturms. Beim Erstellen dieser Kiste werden zwei Binärdateien - teosd und teos-cli - erzeugt.

2. teos-common: Enthält gemeinsame serverseitige und clientseitige Funktionalitäten (hilfreich für die Erstellung eines Clients).

Um den Wachturm erfolgreich auszuführen, müssen Sie bitcoind ausführen, bevor Sie den Wachturm mit dem Befehl teosd starten. Bevor Sie diese Befehle ausführen, müssen Sie Ihre bitcoin.conf-Datei einrichten. Hier sind die Schritte, wie Sie dies tun können:

1. Installieren Sie Bitcoin Core aus dem Quellcode oder laden Sie es herunter. Nach dem Download platzieren Sie die bitcoin.conf-Datei im Benutzerverzeichnis von Bitcoin Core. Überprüfen Sie diesen Link für weitere Informationen darüber, wo die Datei platziert werden soll, da dies vom Betriebssystem abhängt, das Sie verwenden.

2. Nachdem Sie den Speicherort identifiziert haben, an dem die Datei erstellt werden muss, fügen Sie diese Optionen hinzu:

```
#RPC
server=1
rpcuser=<Ihr-Benutzername>
rpcpassword=<Ihr-Passwort>

#chain
regtest=1
```

- server: Für RPC-Anfragen
- rpcuser und rpcpassword: RPC-Clients können sich beim Server authentifizieren
- regtest: Nicht erforderlich, aber nützlich, wenn Sie für die Entwicklung planen.

rpcuser und rpcpassword müssen von Ihnen ausgewählt werden. Sie müssen ohne Anführungszeichen geschrieben werden. Beispiel:

```
rpcuser=aniketh
rpcpassword=strongpassword
```

Wenn Sie jetzt bitcoind ausführen, sollte der Knoten gestartet werden.

1. Für den Wachturmteil müssen Sie zuerst teos aus dem Quellcode installieren. Befolgen Sie die Anweisungen in diesem Link.
2. Nach erfolgreicher Installation von teos auf Ihrem System und dem Ausführen der Tests können Sie mit dem letzten Schritt fortfahren, nämlich der Einrichtung der teos.toml-Datei im Benutzerverzeichnis von teos. Die Datei muss in einem Ordner namens .teos (Achtung auf den Punkt) unter Ihrem Home-Verzeichnis abgelegt werden. Das heißt zum Beispiel /home/<Ihr-Benutzername>/.teos für Linux. Sobald Sie den richtigen Ort gefunden haben, erstellen Sie eine teos.toml-Datei und setzen Sie diese Optionen entsprechend den Änderungen, die wir an bitcoind vorgenommen haben.

```
#bitcoind
btc_network = "regtest"
btc_rpc_user = <Ihr-Benutzer>
btc_rpc_password = <Ihr-Passwort>
```

Beachten Sie, dass hier der Benutzername und das Passwort in Anführungszeichen geschrieben werden müssen, also zum Beispiel:

```
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```

Sobald Sie das erledigt haben, sollten Sie bereit sein, den Tower auszuführen. Da wir auf regtest laufen, besteht die Möglichkeit, dass beim ersten Verbinden des Towers keine Blöcke in unserem Bitcoin-Testnetzwerk abgebaut werden (wenn doch, stimmt etwas nicht). Der Tower erstellt einen internen Cache der neuesten 100 Blöcke von bitcoind, daher erhalten wir beim ersten Ausführen möglicherweise folgenden Fehler:

> ERROR [teosd] Nicht genügend Blöcke, um den Tower zu starten (erforderlich: 100). Bauen Sie mindestens 100 weitere Blöcke ab.

Da wir auf regtest laufen, können wir einen Block abbauen, indem wir einen RPC-Befehl ausführen, ohne auf die 10-minütige Medianzeit warten zu müssen, die wir normalerweise in anderen Netzwerken (wie Mainnet oder Testnet) sehen. Überprüfen Sie die Hilfe von bitcoin-cli und suchen Sie nach Informationen zum Blockabbau. Wenn Sie Hilfe benötigen, können Sie diesen Artikel durchgehen.

![image](assets/2.png)

Das war's, Sie haben den Tower erfolgreich ausgeführt. Herzlichen Glückwunsch. 🎉
