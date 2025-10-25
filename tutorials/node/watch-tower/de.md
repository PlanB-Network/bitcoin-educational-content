---
name: Lightning Watchtower
description: Verstehen und Verwenden eines Watchtower auf Ihrem Lightning-Knoten
---
![cover](assets/cover.webp)



## Wie funktionieren die Wachtürme?



Als wesentlicher Bestandteil des Lightning Network-Ökosystems bieten _Wachtürme_ einen zusätzlichen Schutz für die Lightning-Kanäle der Nutzer. Ihre Hauptaufgabe ist es, den Kanalstatus zu überwachen und einzugreifen, wenn eine Seite des Kanals versucht, die andere zu betrügen.



Wie kann eine Watchtower feststellen, ob ein Kanal kompromittiert wurde? Sie erhält vom Kunden (einer der Parteien des Kanals) die Informationen, die erforderlich sind, um eine Verletzung korrekt zu erkennen und zu behandeln. Diese Informationen umfassen Details der letzten Transaktion, den aktuellen Status des Kanals und die Elements, die für die Erstellung von Strafgeschäften erforderlich sind. Vor der Übermittlung dieser Daten an Watchtower kann der Kunde sie verschlüsseln, um die Vertraulichkeit zu wahren. Selbst wenn Watchtower die Daten erhält, kann es sie erst entschlüsseln, wenn tatsächlich ein Verstoß vorliegt. Dieser Verschlüsselungsmechanismus schützt die Privatsphäre des Kunden und verhindert, dass Watchtower unbefugten Zugriff auf sensible Informationen erhält.



In diesem Tutorial werden wir uns 3 Möglichkeiten ansehen, einen **Watchtower** zu verwenden:




- zunächst die klassische Rohmethode über LND,
- dann ein weiterer Ansatz mit dem Auge von Satoshi,
- und schließlich die vereinfachte Konfiguration eines Watchtower auf Ihrem mit Umbrel gehosteten Lightning-Knoten.



## 1 - Konfigurieren eines Watchtower oder eines Clients über LND



*Diese Anleitung stammt aus [der offiziellen LND-Dokumentation] (https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). An der Originalversion wurden möglicherweise einige Änderungen vorgenommen



Seit Version 0.7.0 unterstützt LND die Ausführung eines privaten altruistischen Watchtower als vollständig integriertes Subsystem von LND. Wachtürme bieten eine zweite Verteidigungslinie gegen böswillige oder versehentliche Einbruchszenarien, wenn der Kundenknoten zum Zeitpunkt des Einbruchs offline oder nicht in der Lage ist, zu reagieren, und bieten so ein höheres Maß an Sicherheit für Kanalfonds.



Im Gegensatz zu einem _Belohnungswachturm_, der als Gegenleistung für seine Dienste einen Anteil am Geld des Senders verlangt, gibt ein _Altruistenwachturm_ das gesamte Geld des Opfers zurück (abzüglich der On-Chain-Gebühren), ohne eine Provision zu verlangen. Belohnungswachtürme werden in einer späteren Version aktiviert werden; sie befinden sich noch in der Test- und Verbesserungsphase.



Darüber hinaus kann der LND jetzt so konfiguriert werden, dass er als _Wachturm-Client_ fungiert und verschlüsselte Transaktionen zur Behebung von Sicherheitsverletzungen (sogenannte "Gerechtigkeitstransaktionen") von anderen altruistischen Wachtürmen speichert. Der Watchtower speichert verschlüsselte Blobs fester Größe und kann die Gerechtigkeitstransaktion erst entschlüsseln und veröffentlichen, nachdem die angreifende Partei einen widerrufenen Commitment-Status gesendet hat. Die Kommunikation Kunde ↔ Watchtower wird mit ephemeren Schlüsselpaaren verschlüsselt und authentifiziert, was die Fähigkeit des Watchtower einschränkt, seine Kunden über langfristige Anmeldeinformationen zu verfolgen.



Beachten Sie, dass wir uns entschieden haben, in dieser Version eine begrenzte Anzahl von Funktionen bereitzustellen, die den Nutzern von LND bereits erhebliche Sicherheit bieten. Viele andere Watchtower-bezogene Funktionen stehen entweder kurz vor der Fertigstellung oder sind bereits weit fortgeschritten; wir werden sie weiterhin bereitstellen, sobald wir sie testen und sobald sie als sicher eingestuft werden.



hinweis: Derzeit speichern die Wachtürme nur die Ausgaben "to_local" und "to_remote" von widerrufenen Zusagen; die Speicherung der HTLC-Ausgaben wird in einer zukünftigen Version eingeführt, da das Protokoll erweitert werden kann, um zusätzliche Signaturdaten in verschlüsselten Blobs zu enthalten



### Konfigurieren eines Watchtower



Um einen Watchtower einzurichten, müssen Kommandozeilenbenutzer den optionalen `watchtowerrpc`-Subserver kompilieren, der die Interaktion mit dem Watchtower über gRPC oder `lncli` ermöglicht. Die veröffentlichten Binärdateien enthalten standardmäßig den `watchtowerrpc`-Subserver.



Die Mindestkonfiguration für die Aktivierung von Watchtower ist `Watchtower.active=1`.



Sie können Ihre Watchtower-Konfigurationsinformationen mit `lncli tower info` abrufen:



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



Der vollständige Satz von Watchtower-Konfigurationsoptionen ist über `LND -h` verfügbar:



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### Abhörschnittstellen



Standardmäßig lauscht das Watchtower auf `:9911`, was dem Port `9911` auf allen verfügbaren Schnittstellen entspricht. Benutzer können ihre eigenen Abhörschnittstellen über die Option `--Watchtower.listen=` definieren. Sie können Ihre Konfiguration im Feld `"listeners"` von `lncli tower info` überprüfen. Wenn Sie Probleme haben, sich mit Ihrem Watchtower zu verbinden, stellen Sie sicher, dass der `<Port>` offen ist oder dass Ihr Proxy korrekt auf einen aktiven Interface konfiguriert ist.



#### Externe IP-Adressen



Die Benutzer können auch die externe IP Address(es) des Watchtower mit `Watchtower.externalip=` angeben, wodurch die vollständige URI des Watchtower (pubkey@host:port) über RPC oder `lncli tower info` sichtbar wird:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Watchtower-URIs können den Kunden mit folgendem Befehl zur Verbindung und Nutzung mitgeteilt werden:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Wenn Watchtower-Kunden aus der Ferne darauf zugreifen müssen, stellen Sie sicher, dass Sie :




- Öffnen Sie Port 9911 (oder einen über `Watchtower.listen` definierten Port).
- Verwenden Sie einen Proxy, um den Datenverkehr von einem offenen Port zum Watchtower des Address umzuleiten.



#### Versteckte Tor-Dienste



Watchtower unterstützen die versteckten Tor-Dienste und können mit den folgenden Optionen automatisch generate beim Start einrichten:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



Die .onion Address erscheint dann im Feld "uris" bei einer "lncli tower info"-Abfrage:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



hinweis: Der öffentliche Schlüssel des Watchtower unterscheidet sich vom öffentlichen Schlüssel des "LND"-Knotens. Vorläufig dient er als "Soft-Whitelist", da die Kunden den öffentlichen Schlüssel des Watchtower kennen müssen, um ihn als Backup zu verwenden, bis fortgeschrittenere Whitelist-Mechanismen zur Verfügung stehen. Wir empfehlen, diesen öffentlichen Schlüssel NICHT offenzulegen, es sei denn, Sie sind bereit, Ihren Watchtower dem gesamten Internet auszusetzen



#### Watchtower Datenbankverzeichnis



Die Watchtower-Datenbank kann mit der Option `Watchtower.towerdir=` verschoben werden. Beachten Sie, dass ein Suffix `/Bitcoin/Mainnet/Watchtower.db` an den gewählten Pfad angehängt wird, um die Datenbanken nach Zeichenketten zu isolieren. Wenn Sie also `Watchtower.towerdir=/path/to/towerdir` setzen, wird eine Datenbank unter `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db` erzeugt.



Unter Linux zum Beispiel befindet sich die Standarddatenbank des Watchtower unter :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Konfigurieren eines Watchtower-Clients



Um einen Watchtower-Client zu konfigurieren, benötigen Sie zwei Dinge:





- Aktivieren Sie den Watchtower-Client mit der Option `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- Der URI eines aktiven Watchtower.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Sie können mehrere Wachtürme auf diese Weise konfigurieren.



#### Gebührensätze für Rechtsgeschäfte



Benutzer können optional den Gebührensatz für Rechtstransaktionen über die Option `wtclient.sweep-fee-rate` festlegen, die Werte in Sat/Byte akzeptiert. Der Standardwert ist 10 sat/Byte, aber es ist möglich, höhere Raten anzustreben, um eine höhere Priorität bei Spitzenbelastungen zu erreichen. Die Änderung von `sweep-fee-rate` gilt für alle neuen Aktualisierungen nach dem Neustart von daemon.



#### Beaufsichtigung



Mit dem Befehl "lncli wtclient" können Benutzer jetzt direkt mit dem Watchtower-Client interagieren, um Informationen über alle registrierten Wachtürme zu erhalten oder zu ändern.



Mit `lncli wtclient tower` können Sie zum Beispiel die Anzahl der Sitzungen herausfinden, die derzeit mit dem oben hinzugefügten Watchtower ausgehandelt werden, und dank des Feldes `active_session_candidate` feststellen, ob er für Backups verwendet wird.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Um Informationen über Watchtower-Sitzungen zu erhalten, verwenden Sie die Option `--include_sessions`.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



Alle Watchtower-Client-Konfigurationsoptionen sind über "lncli wtclient -h" verfügbar:



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - Installieren Sie Ihr eigenes Auge von Satoshi



*Diese Anleitung ist teilweise einem Artikel aus dem [Summer of Bitcoin Blog] (https://blog.summerofbitcoin.org/) entnommen. An der ursprünglichen Version wurden Änderungen vorgenommen*



Das Auge von Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) ist ein nicht deponierter Watchtower-Blitz, der mit [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org) übereinstimmt. Er besteht aus zwei Hauptkomponenten:





- teos**: enthält einen Befehlszeilen-Interface (CLI) und die wesentlichen Serverfunktionen von Watchtower. Zwei Binärdateien - **teosd** und **teos-CLI** - werden erzeugt, wenn dieser _Krate_ kompiliert wird.





- teos-common**: enthält gemeinsame server- und clientseitige Funktionen (nützlich für die Erstellung eines Clients).



Um Watchtower korrekt auszuführen, müssen Sie **bitcoind** ausführen, bevor Sie Watchtower mit dem Befehl **teosd** starten. Bevor Sie diese beiden Befehle ausführen, müssen Sie Ihre **Bitcoin.conf**-Datei konfigurieren. Hier ist die Vorgehensweise:





- Installieren Sie Bitcoin core aus dem Quellcode oder laden Sie es herunter. Nach dem Herunterladen legen Sie die Datei **Bitcoin.conf** im Bitcoin core-Benutzerverzeichnis ab. Unter diesem Link finden Sie weitere Informationen darüber, wo Sie die Datei ablegen müssen, da dies vom verwendeten Betriebssystem abhängt.





- Sobald der Standort festgelegt ist, fügen Sie die folgenden Optionen hinzu:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- server**: für RPC-Anfragen





- rpcuser** und **rpcpassword**: Authentifizierung von RPC-Clients gegenüber dem Server





- regtest**: nicht erforderlich, aber nützlich, wenn Sie eine Entwicklung planen.



Die Werte für **rpcuser** und **rpcpassword** sind von Ihnen zu wählen. Sie müssen ohne Anführungszeichen geschrieben werden. Zum Beispiel:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Wenn Sie nun **bitcoind** ausführen, sollte der Knoten starten.





- Für den Watchtower-Teil müssen Sie zunächst **teos** aus dem Quellcode installieren. Folgen Sie den Anweisungen in diesem Link.





- Wenn Sie **teos** erfolgreich auf Ihrem System installiert und die Tests durchgeführt haben, können Sie zum letzten Schritt übergehen: dem Einrichten der Datei **teos.toml** im Benutzerverzeichnis von teos. Die Datei sollte in einem Ordner mit dem Namen **.teos** (beachten Sie den Punkt) unter Ihrem Home-Verzeichnis abgelegt werden. Zum Beispiel **/home//.teos** unter Linux. Sobald Sie den Speicherort gefunden haben, erstellen Sie eine **teos.toml**-Datei und stellen Sie diese Optionen entsprechend den Änderungen auf **bitcoind** ein:



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Beachten Sie, dass hier der Benutzername und das Passwort **in Anführungszeichen** geschrieben werden müssen. Nach dem vorherigen Beispiel:



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Sobald dies geschehen ist, sollten Sie bereit sein, den Watchtower zu starten. Da wir auf **regtest** laufen, ist es wahrscheinlich, dass keine Blöcke auf unserem Bitcoin Testnetzwerk abgebaut wurden, als sich der Watchtower zum ersten Mal verbunden hat (falls doch, ist etwas falsch). Watchtower baut einen internen Cache mit den letzten 100 Blöcken von **bitcoind** auf; daher kann beim ersten Start der folgende Fehler auftreten:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Da wir **regtest** verwenden, können wir Miner-Blöcke mit einem RPC-Befehl erzeugen, ohne die durchschnittliche 10-minütige Verzögerung abzuwarten, die in anderen Netzen (wie Mainnet oder Testnet) auftritt. In der **bitcoin-cli**-Hilfe finden Sie Einzelheiten über Miner-Blöcke.



![Image](assets/fr/01.webp)



Das ist alles: Sie haben den Watchtower erfolgreich durchgeführt. Herzlichen Glückwunsch! 🎉




## 3 - Konfigurieren eines Watchtower auf Umbrel



Bei Umbrel ist die Verbindung mit einem Watchtower zum Schutz Ihres Lightning-Knotens extrem einfach, da alles über das grafische Interface erfolgt. Nachdem Sie eine Fernverbindung zu Ihrem Knoten hergestellt haben, öffnen Sie die Anwendung "**Lightning Node**".



![Image](assets/fr/02.webp)



Klicken Sie auf die drei kleinen Punkte oben rechts auf dem Interface und wählen Sie dann "**Erweiterte Einstellungen**".



![Image](assets/fr/03.webp)



Im Menü "**Watchtower**" sind zwei Optionen verfügbar:





- Watchtower Service**: Mit dieser Option können Sie einen Watchtower betreiben, d. h. einen Dienst, der die Kanäle anderer Knotenpunkte überwacht, um Betrugsversuche zu erkennen. Im Falle eines Verstoßes veröffentlicht Ihr Watchtower eine Transaktion auf dem Blockchain, so dass die Nutzer ihre gesperrten Gelder zurückerhalten können. Nach der Aktivierung erscheint der URI Ihres Watchtower und kann anderen Knoten mitgeteilt werden, damit diese ihn zu ihrem Watchtower-Client hinzufügen können;





- Watchtower Client**: Mit dieser Option können Sie sich mit externen Wachtürmen verbinden, um Ihre eigenen Kanäle zu schützen. Sobald sie aktiviert ist, können Sie Watchtower-Dienste hinzufügen, an die Ihr Knoten die notwendigen Informationen über seine Kanäle übermittelt. Diese Wachtürme überwachen dann deren Status und greifen im Falle eines Betrugsversuchs ein.



Vorrangig sollten Sie natürlich den *Watchtower Client* aktivieren, um Ihren Knoten zu schützen, aber ich empfehle Ihnen auch, den *Watchtower Service* zu aktivieren, um im Gegenzug zur Sicherheit anderer Benutzer beizutragen.



![Image](assets/fr/04.webp)



Klicken Sie dann auf die Green-Schaltfläche "**Knoten speichern und neu starten**". Ihr LND wird neu gestartet.



Im gleichen Menü finden Sie auch die URI Ihres Watchtower-Dienstes, wenn Sie ihn aktiviert haben. Sie können auch die URI eines externen Watchtower hinzufügen, um Ihre Kanäle zu schützen. Klicken Sie zur Bestätigung auf "**ADD**".



![Image](assets/fr/05.webp)



Es gibt mehrere online verfügbare Wachtürme. Zum Beispiel bieten [LN+ und Voltage einen altruistischen Watchtower] (https://lightningnetwork.plus/Watchtower) an, mit dem Sie sich verbinden können:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Eine andere Möglichkeit ist, Exchange Ihre Watchtower URI mit Ihren Mit-Bitcoinern zu teilen, so dass jeder den Knoten des anderen schützt.



Ich empfehle Ihnen auch, mehrere Wachtürme einzurichten, um das Risiko zu verringern, dass einer von ihnen nicht mehr verfügbar ist.



Schließlich können Sie den Parameter "**Watchtower Client Sweep Fee Rate**" anpassen. Damit legen Sie den maximalen Gebührensatz fest, den Sie bereit sind, für eine Watchtower-Rundfunk-Straftransaktion zu zahlen, die in einen Block aufgenommen werden soll. Stellen Sie sicher, dass Sie einen ausreichend hohen Wert einstellen, der an die in Ihren Kanälen gesperrten Beträge angepasst ist.