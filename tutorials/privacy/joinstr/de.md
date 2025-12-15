---
name: Joinstr
description: Dezentralisierte CoinJoins über das Nostr-Netzwerk für souveräne Bitcoin-Vertraulichkeit
---

![cover](assets/cover.webp)



Die Transparenz der Bitcoin-Blockchain macht es möglich, den Transaktionsverlauf nachzuvollziehen. CoinJoins unterbrechen diese Verbindungen, indem sie mehrere gleichzeitige Transaktionen mischen und so ein mit Bargeld vergleichbares Maß an Vertraulichkeit wiederherstellen.



Herkömmliche Lösungen stützen sich jedoch auf einen zentralen Koordinator, der eine einzige Schwachstelle darstellt. Wasabi und Samourai stellten 2024 auf Druck der Regulierungsbehörden ihren Betrieb ein.



**Joinstr** beseitigt diese Schwäche, indem es das dezentralisierte Nostr-Netzwerk für die Koordination nutzt. Diese Open-Source-Anwendung ermöglicht wirklich souveräne CoinJoins, bei denen keine zentrale Behörde den Dienst zensieren, überwachen oder unterbrechen kann.



## Was ist Joinstr?



Joinstr ist ein Open-Source-Tool, das den CoinJoins-Ansatz revolutioniert, indem es das Nostr-Protokoll als Koordinationsinfrastruktur nutzt. Im Gegensatz zu zentralisierten Lösungen, die einen dedizierten Server benötigen, stützt sich Joinstr auf ein verteiltes Netzwerk von Nostr-Relais, die es den Teilnehmern ermöglichen, sich direkt zwischen Peers zu koordinieren.



**Dezentrale Architektur** : Das Nostr-Netz ersetzt den zentralen Koordinator. Die Teilnehmer erstellen "Pools" oder treten ihnen bei, indem sie verschlüsselte Ankündigungen über die Nostr-Relais veröffentlichen. Diese Informationen (Beträge, Teilnehmer, Adressen) bleiben für die Relays unverständlich, wodurch sichergestellt wird, dass keine zentrale Instanz CoinJoins überwachen, zensieren oder filtern kann.



**SIGHASH_ALL|ANYONECANPAY-Mechanismus**: Joinstr nutzt dieses Bitcoin-Signaturkennzeichen aus und ermöglicht es jedem Teilnehmer, nur seine Eingaben zu signieren, während er alle Ausgaben validiert. Jeder Benutzer generiert seine PSBT lokal und verteilt sie dann über Nostr. Jeder Benutzer generiert sein PSBT lokal, signiert es und verteilt es dann über Nostr. Ihre Bitcoins bleiben bis zur endgültigen Unterschrift unter Ihrer alleinigen Kontrolle.



**Philosophie**: Joinstr folgt dem Bitcoin Cypherpunk-Ethos und strebt drei Ziele an: **Widerstand gegen Zensur** (keine Behörde kann den Dienst stoppen), **totale Nicht-Zensur** (Sie behalten Ihre privaten Schlüssel) und **Gleichbehandlung** (kein UTXO darf diskriminiert werden).



### Hauptmerkmale



**Flexible Pools**: Im Gegensatz zu festen Stückelungen kann jeder Nutzer einen Pool mit genau dem gewünschten Betrag und der angestrebten Teilnehmerzahl erstellen und so den Einsatz von UTXO ohne künstliche Aufteilung optimieren.



**Transparente Gebühren**: Keine Koordinierungsgebühren. Lediglich die Bitcoin-Transaktionsgebühren werden gleichmäßig auf die Teilnehmer verteilt (einige tausend Satoshis pro Person).



**Ephemerität**: Keine Benutzerdaten werden gespeichert. Die Informationen werden über verschlüsselte ephemere Nostr-Nachrichten übertragen, die nach der Transaktion sofort vergessen werden.



### Verfügbare Plattformen



Dieser Leitfaden konzentriert sich auf die **Android-Anwendung**, die einzige derzeit stabile und empfohlene Lösung. Es gibt ein Electrum-Plugin, das jedoch aufgrund von Kompatibilitätsproblemen instabil ist. Eine Webschnittstelle ist in Entwicklung.



## Bitcoin Kernkonfiguration



Joinstr Android erfordert eine Verbindung zu einem Bitcoin-Knoten über RPC. Sie müssen zunächst Bitcoin Core auf Ihrem Computer so konfigurieren, dass er Verbindungen von Ihrem Telefon akzeptiert.



**Hinweis**: Weitere Einzelheiten zur vollständigen Konfiguration von Bitcoin Core finden Sie in unseren speziellen Tutorials:



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Anforderungen an das Netz



#### Suchen Sie Ihre lokale IP-Adresse



Ihr Android-Telefon muss in der Lage sein, Ihren Bitcoin-Knoten im lokalen Netzwerk zu erreichen. Suchen Sie die IP-Adresse Ihres Computers:



**unter macOS** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Einfache Alternative:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**unter Linux** :



```bash
hostname -I | awk '{print $1}'
```



**unter Windows** :



```cmd
ipconfig
```



Ermittlung der IPv4-Adresse (Format "192.168.x.x" oder "10.0.x.x")



### RPC-Konfiguration



#### bitcoin.conf bearbeiten



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Suchen Sie Ihre Datei `bitcoin.conf`:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/Library/Application Support/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Öffnen Sie die Datei mit Ihrem bevorzugten Texteditor und fügen Sie diese Konfiguration hinzu, um den RPC-Server zu aktivieren.



**Empfohlene Konfiguration für die ersten Schritte (Lesezeichen)** :



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



*konfiguration *mainnet** (für den Produktionseinsatz) :



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**Wichtig** :




- Signet wird für Ihre ersten Tests dringend empfohlen**: Die Anwendung befindet sich noch in der Entwicklung (Beta), und es können noch Fehler auftreten. Mit Signet können Sie kostenlos testen, ohne echtes Geld zu riskieren
- Ersetzen Sie "192.168.1.0/24" durch Ihr Netzwerk-Subnetz (z. B. wenn Ihre IP "192.168.68.57" lautet, verwenden Sie "192.168.68.0/24")



**Sicherheit**: Erzeugen Sie ein sicheres Passwort:



```bash
openssl rand -base64 32
```



### Initialisierung



#### Neustart und Überprüfung



1. Bitcoin Core vollständig abschalten


2. Starten Sie ihn neu, um die Konfiguration zu übernehmen




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Wenn Bitcoin Core zum ersten Mal gestartet wird, lädt er die Lesezeichen-Blockchain herunter und synchronisiert sie. Dieser Vorgang ist viel schneller als bei mainnet (nur ein paar Minuten). Bitte warten Sie, bis die Synchronisierung abgeschlossen ist, bevor Sie fortfahren.



![CRÉATION DE WALLET](assets/fr/04.webp)



Nach der Synchronisierung erstellen Sie ein neues Portfolio, indem Sie auf "Create a new wallet" klicken. Geben Sie ihm einen eindeutigen Namen wie "tuto_joinstr_signet".



![WALLET CRÉÉ](assets/fr/05.webp)



Ihr wallet ist nun erstellt und bereit, mit Lesezeichen versehene Bitcoins zum Testen zu empfangen.



#### Bitcoins mit Lesezeichen erhalten (Test)



Um Joinstr auf Lesezeichen zu testen, benötigen Sie kostenlose Test-Bitcoins:



![SIGNET FAUCET](assets/fr/06.webp)



Verwenden Sie ein öffentliches Lesezeichen wie :




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



Legen Sie in Bitcoin Core, generate eine neue Empfangsadresse an (Registerkarte "Empfangen"), kopieren Sie sie und fügen Sie sie in das Formular für den Wasserhahn ein. Lösen Sie das Captcha, falls erforderlich. Sie erhalten innerhalb von Sekunden kostenlose Bitcoins mit Lesezeichen.



## Android-Anwendung



### Einrichtung



![APPLICATION ANDROID](assets/fr/07.webp)



Gehen Sie zu [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases), um die neueste APK-Version herunterzuladen. Laden Sie die Datei in Ihrem Android-Browser herunter, und öffnen Sie sie, um die Installation zu starten. Falls nötig, müssen Sie in den Sicherheitseinstellungen Ihres Telefons die Installation aus unbekannten Quellen zulassen.



### Konfiguration der Anwendung



![PERMISSIONS VPN](assets/fr/08.webp)



Beim ersten Start bittet die Joinstr-Anwendung um die Erlaubnis, das integrierte VPN zu steuern. Akzeptieren Sie beide Berechtigungsanfragen: OpenVPN-Steuerung und VPN-Verbindung. Diese Berechtigungen sind für die VPN-Integration erforderlich, die Ihre Netzwerkdaten schützt.



![INTERFACE APPLICATION](assets/fr/09.webp)



Die Joinstr-Anwendung ist in drei Hauptregisterkarten unterteilt:




- Startseite**: Startbildschirm
- Pools**: Erstellen und Verwalten von CoinJoin-Pools
- Einstellungen**: Konfiguration der Anwendung



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Konfigurieren Sie die Einstellungen auf der Registerkarte "Einstellungen":



**1. Nostr-Relais**: Nostr-Relay-Adresse für die Pool-Koordination




- Beispiel: `wss://relay.damus.io`
- Andere empfohlene Weiterleitungen: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Wichtig**: Alle Teilnehmer müssen das **gleiche Nostr-Relais** verwenden, um die gleichen Pools zu sehen und ihnen beizutreten. Wenn Sie ein anderes Relay verwenden, sehen Sie keine Pools, die auf anderen Relays erstellt wurden



**2. Knoten-URL**: IP-Adresse Ihres Bitcoin-Knotens (ohne Port)




- Format: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3. RPC-Benutzername** : Der in `rpcuser=` auf Ihrem bitcoin.conf konfigurierte Benutzername




- Beispiel: `satoshi



**4. RPC Passwort** : Das in `rpcpassword=` auf Ihrem bitcoin.conf festgelegte Passwort



**5. RPC-Anschluss** : RPC-Anschluss je nach Netzwerk




- Mainnet** : `8332`
- Lesezeichen**: `38332`



**6. Wallet**: Wählen Sie das Bitcoin Core-Portfolio, das die zu mischenden UTXOs enthält




- Beispiel: `tuto_joinstr_signet`



**7. VPN-Gateway**: Wählen Sie einen Riseup VPN-Server




- Beispiel: `(Paris) vpn07-par.riseup.net`
- Andere verfügbar: Amsterdam, Seattle, usw.
- ⚠️ **Wichtig**: Alle Teilnehmer desselben Pools müssen das **gleiche VPN-Gateway** verwenden, um an CoinJoin teilzunehmen. Während der Mixing-Runde müssen alle Teilnehmer mit der gleichen Exit-IP-Adresse auftreten, um zu verhindern, dass die Netzwerkanalyse die Teilnehmer korreliert



Die Joinstr-Anwendung **integriert** nativ das Riseup VPN und vereinfacht so die Koordination zwischen den Teilnehmern.



**Wichtig** :




- Vergewissern Sie sich, dass Ihr Telefon und Ihr Computer mit demselben lokalen WiFi-Netzwerk verbunden sind
- Die VPN-Verbindung wird bei der Teilnahme an einem Pool automatisch aktiviert
- Klicken Sie auf **"Speichern "**, wenn Sie alle Parameter eingestellt haben



## Praktische Anwendung



### Einen Pool erstellen oder einem Pool beitreten



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Sie haben zwei Möglichkeiten, an einer CoinJoin teilzunehmen:



**Option 1: Einen neuen Pool anlegen**



Klicken Sie in der Registerkarte "Pools" auf "Neuen Pool erstellen". Geben Sie den Nennwert in BTC (z. B. 0,002 BTC) und die gewünschte Anzahl der Teilnehmer an (mindestens 2, empfohlen 3-5 für mehr Anonymität). Die Anwendung wartet dann darauf, dass andere Benutzer Ihrem Pool beitreten. Sobald die erforderliche Anzahl erreicht ist, beginnt der Ausgabe-Registrierungsprozess automatisch, und Sie müssen Ihren UTXO zum Mischen auswählen und auf "Registrieren" klicken.



**⏱️ Wichtig**: Pools verfallen nach **10 Minuten** Inaktivität. Wenn die erforderliche Anzahl von Teilnehmern nicht erreicht wird, wird der Pool automatisch geschlossen.



**Option 2: Beitritt zu einem bestehenden Pool**



Durchsuchen Sie auf der Registerkarte "Andere Pools anzeigen" die verfügbaren Pools, die von anderen Benutzern erstellt wurden. Wählen Sie einen Pool aus, der Ihrer Menge entspricht, und treten Sie ihm bei. Vergewissern Sie sich, dass Sie dasselbe Nostr-Relay und VPN-Gateway konfiguriert haben wie die anderen Teilnehmer (siehe Abschnitt Konfiguration).



**UTXO-Auswahlregel**: Ihr UTXO muss etwas höher sein als die Pool-Stückelung (zwischen +500 und +5000 sats Überschuss).



**Beispiel**: Für einen Pool von 0,002 BTC (200.000 sats), verwenden Sie einen UTXO zwischen 200.500 und 205.000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Der Prozess läuft dann **vollautomatisch** ab: Sobald Ihre Eingabe registriert wurde, wartet die Anwendung darauf, dass alle Teilnehmer ihre Eingaben registrieren. Sobald alle Eingaben registriert sind, wird der PSBT erstellt, automatisch mit Ihren Schlüsseln signiert und dann mit den Signaturen der anderen Teilnehmer kombiniert. Schließlich wird die gesamte Transaktion im Bitcoin-Netz übertragen. Sobald die Übertragung abgeschlossen ist, erhalten Sie die TXID (Transaction Identifier). Auf Android ist keine manuelle Manipulation des PSBT erforderlich.



### on-chain-Prüfung



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Sobald die Transaktion übertragen wurde, erhalten Sie die TXID (Transaktionskennung). Diese können Sie auf [mempool.space](https://mempool.space) oder in Ihrem bevorzugten Browser einsehen. Zum Testen mit einem Lesezeichen verwenden Sie [mempool.space/signet](https://mempool.space/signet).



Sie können beobachten:





- N Einträge**: Eine pro Teilnehmer (in unserem Beispiel, 2 Einträge)
- N identische Ausgänge**: exakter Betrag der Stückelung (hier 2 Ausgänge zu je 0,00199800 BTC)
- Flussdiagramm**: mempool.space zeigt visuell die Mischung aus Eingängen und Ausgängen
- Merkmale** : Die Transaktion kann als SegWit, Taproot, RBF, etc. identifiziert werden.



Da alle Hauptausgänge den gleichen Betrag haben, ist es **unmöglich festzustellen, welcher zu wem gehört**. Dies ist das Grundprinzip von CoinJoin: die Ununterscheidbarkeit der Ausgaben.



**Exemple de transaction signet** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Bitte beachten**: Wenn Ihre UTXOs größer waren als die Pool-Stückelung, haben Sie Devisenausgänge (Überschüsse). Diese Devisen-UTXOs bleiben nachvollziehbar und müssen getrennt von Ihren anonymisierten Outputs verwaltet werden. Kombinieren Sie diese niemals mit Ihren gemischten Outputs.



## CoinJoin Qualitäts- und Anonymitätspakete



Die Effizienz eines CoinJoin wird durch seinen **Anonset** gemessen: die Anzahl der Outputs von gleichem Wert, die durch die Transaktion erzeugt werden. Je höher diese Zahl ist, desto schwieriger ist es zu bestimmen, welcher Input welchem Output entspricht.



Joinstr generiert derzeit im Durchschnitt Pools von **2 bis 5 Teilnehmern**. Diese Zahlen sind niedriger als die traditioneller zentralisierter Koordinatoren wie Wasabi (50-100 Teilnehmer) oder Whirlpool (5-10 Teilnehmer), aber das ist der Preis der Dezentralisierung.



💡 **Um die Anonymitätssätze und ihre Berechnung im Detail zu verstehen**, siehe unseren vollständigen Kurs: [Anonymitätssätze] (https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr vs. andere CoinJoins



| Aspect | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Participants par pool** | 50-100 | 5-10 | Variable (P2P) | **2-5** |
| **Coordinateur** | Centralisé (fermé 2024) | Centralisé (actif) | P2P maker/taker | **Aucun (Nostr)** |
| **Résistance à la censure** | Faible | Moyenne | Très élevée | **Très élevée** |
| **Frais de coordination** | Pourcentage | Frais d'entrée | Payés aux makers | **Aucun** |
| **Discrimination UTXO** | Oui (blacklists) | Non | Non | **Non** |

💡 **Andere aktive CoinJoin-Lösungen** :




- Ashigaru**: Open-Source-Implementierung des Whirlpool-Protokolls mit zentralem Koordinator, der jedoch dezentral eingesetzt werden kann. Wird auch nach der Beschlagnahme von Samourai Wallet im Jahr 2024 weiter betrieben.
- JoinMarket**: Dezentralisierte P2P-Lösung ohne zentralen Koordinator, basierend auf einem Maker/Taker-Geschäftsmodell, bei dem "Maker" Liquidität bereitstellen und von "Takern" entlohnt werden.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Der grundlegende Kompromiss**: Joinstr und JoinMarket sind die einzigen beiden Lösungen ohne einen zentralen Koordinator. JoinMarket verwendet ein P2P-Geschäftsmodell mit finanziellen Anreizen, während Joinstr Nostr für eine kostenfreie Koordination verwendet. Joinstr opfert die unmittelbare Anonymität in großem Maßstab zugunsten der Einfachheit (keine Verwaltung von Anbietern und Nachfragern) und des völligen Fehlens von Koordinierungsgebühren.



**Praktische Empfehlung**: Um kleinere Pools zu kompensieren, führen Sie mehrere aufeinanderfolgende CoinJoin-Runden mit verschiedenen Teilnehmern durch. Verteilen Sie die Runden und wechseln Sie die Nostr-Staffeln zwischen den einzelnen Runden, um die Vertraulichkeit zu maximieren.



Weitere Informationen zu diesem Thema finden Sie in unserem vollständigen Kurs über Bitcoin-Datenschutz:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Vorteile und Grenzen



### Höhepunkte



**Erhöhter Datenschutz**: Die Kombination aus Nostr-Kommunikationsverschlüsselung, gemeinsamem VPN zwischen den Teilnehmern und der empfohlenen Nutzung von Tor schafft einen mehrschichtigen Schutz, der nur schwer zu umgehen ist.



**Transparente, minimale Kosten**: Keine Koordinierungskosten, nur mining-Kosten werden gleichmäßig auf die Teilnehmer verteilt. Keiner der Betreiber erhebt einen Prozentsatz.



### Zu berücksichtigende Zwänge





- Variable Liquidität**: Kleinere Pools, die warten können, bis die Teilnehmer zusammenkommen
- Projekt in Arbeit**: Anwendung im Beta-Stadium, Bugs möglich. Testen Sie zunächst mit kleinen Beträgen auf Lesezeichen
- Sybil-Angriffe**: Möglichkeit, dass ein Gegner mehrere Poolteilnehmer kontrolliert



## Bewährte Praktiken



**UTXO-Isolierung**: Kombinieren Sie niemals ein gemischtes UTXO mit einem unvermischten. Verwenden Sie eine separate Mappe für Ihre anonymisierten Ausgaben.



**Mehrere Runden erforderlich**: Führen Sie mindestens 3 aufeinanderfolgende Runden mit verschiedenen Teilnehmern durch. Variieren Sie die Mengen und die Zeitpunkte, um Muster zu vermeiden. Lassen Sie die Runden mehrere Stunden auseinander liegen.



**Netzwerkschutz**: Verwende Tor systematisch zusätzlich zum eingebauten VPN. Erzeuge ephemere Nostr-Schlüssel für jede wichtige Sitzung.



**Vorsichtiger Fortschritt**: Beginnen Sie mit kleinen Beträgen, um Lesezeichen zu setzen.



## Schlussfolgerung



Joinstr ist eine wirklich dezentralisierte Bitcoin-Datenschutzlösung. Durch die Verwendung von Nostr für die Koordinierung entfällt die Abhängigkeit von zentralen Koordinatoren, während die Souveränität der Nutzer erhalten bleibt.



**Für Nutzer, die Wert auf Zensurresistenz legen und bereit sind, mehrere Runden CoinJoin durchzuführen, um kleinere Pools auszugleichen.



Vor dem Hintergrund zunehmender finanzieller Kontrolle werden dezentralisierte Instrumente zum Schutz der Privatsphäre immer wichtiger.



## Ressourcen



### Offizielle Dokumentation




- [Joinstr offizielle Website](https://joinstr.xyz)
- [Benutzerdokumentation](https://docs.joinstr.xyz/users/using-joinstr)
- [Technische Dokumentation] (https://docs.joinstr.xyz/overview/how-does-it-work)
- [GitLab-Quellcode](https://gitlab.com/invincible-privacy/joinstr)
- [Android-Anwendung] (https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Anleitungen




- [Electrum plugin tutorial](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Vollständige Anleitung von Uncensored Tech



### Gemeinschaft und Unterstützung




- [Telegram Joinstr Group](https://t.me/joinstr) - Community-Unterstützung und Lesezeichen-Ecken
- [Technische Diskussion über DelvingBitcoin](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Zusätzliche Tools




- [Lesezeichen Faucet](https://signetfaucet.com) - Bitcoins kostenlos testen
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Faucet Alternative
- [Mempool.space](https://mempool.space) - Block explorer mit Datenschutzanalyse