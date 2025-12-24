---
name: JoinMarket

description: Leitfaden und Anleitung zur Verwendung von JoinMarket für die Ausführung von CoinJoin über Bitcoin über die Befehlszeile
---

![cover](assets/cover.webp)



---

Wenn Sie diese Seite über die Online-Suche nach "JoinTmarket" gefunden haben, möchte ich Ihnen meine aufrichtige Anerkennung aussprechen. Sie sind jedoch über einen Leitfaden gestolpert, der sich mit einem ganz anderen, aber äußerst interessanten Thema beschäftigt! 🚬🍁



Das Ziel dieses Tutorials ist es, die theoretische und praktische Funktionsweise von JoinMarket über die Kommandozeile zu veranschaulichen. 🐢 💚



## JoinMarket Theoretische Definition



Wir können JoinMarket als ein Werkzeug oder ein Wallet definieren, das CoinJoin mit anderen Nutzern auf eine völlig Trustless Weise und ohne einen zentralen Koordinator ermöglicht.



Da der gesamte theoretische Teil dieses Tools sehr umfangreich ist, habe ich beschlossen, es in einer speziellen Folge meines Podcasts Address zu behandeln. Denjenigen, die Italienisch verstehen, empfehle ich dringend, nach dem Anhören der Folge weiterzulesen, um die grundlegenden Konzepte für die richtige Verwendung dieses Programms besser zu verinnerlichen.



Sie können die Episode über diese direkten Links nachholen:




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google-Podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (hier können Sie es direkt im Browser anhören).
- [Antenna pod](https://antennapod.org/) ist ein kostenloser und quelloffener Podcast-Manager, für den keine Registrierung erforderlich ist. Um die Episode zu finden, laden Sie die App herunter, fügen Sie meinen Podcast manuell hinzu, indem Sie [diesen Link](https://Anchor.fm/s/bd5d5b20/podcast/rss) in den Bereich _feed rss_ einfügen, und suchen Sie dann nach der Episode, die JoinMarket gewidmet ist.



## Einrichtung



Betriebssysteme:





- Raspiblitz
- Regenschirm
- MyNode
- Raspibolt



## Konfigurationsdateien



JoinMarket ist eine anpassbare Software mit einer unendlichen Anzahl von Einstellungen; diese Einstellungen werden in einer Konfigurationsdatei im Hauptverzeichnis des Programms namens `Joinmarket.cfg` festgelegt.



In diesem Abschnitt gehen wir auf einige Felder ein, die für Sie interessant sein könnten, um sie zu erforschen und/oder zu ändern, je nach Ihren Bedürfnissen. Ich möchte betonen, dass alle unten aufgeführten Änderungen nützlich sind, um den Betrieb der Software an die persönlichen Bedürfnisse anzupassen, aber nicht zwingend erforderlich sind.



Wechseln wir zunächst in den Ordner `joinmarket/scripts` und führen den Befehl aus:



```bash
python wallet-tool.py generate
```


An diesem Punkt sollten wir eine Fehlermeldung erhalten, aber wenn wir dies tun, wird die Software eine voreingestellte Einstellungsdatei generate für uns erstellen. Wir können die Einstellungsdatei über das Terminal mit bearbeiten:



```bash
nano joinmarket.cfg
```



oder:



```bash
vim joinmarket.cfg
```



einmal geöffnet, werden wir zahlreiche Zeilen mit verschiedenen Einstellungen und deren Erklärung auf Englisch sehen. Im Folgenden werden wir die interessantesten Variablen analysieren:





- dieses Feld legt fest, wie aggressiv die Software nicht verbrauchte Outputs konsolidieren soll. Falls wir viele UTXOs zu konsolidieren haben, kann es sinnvoll sein, von _gradual_ auf _greedy_ zu wechseln
- es ist sehr nützlich, diese Einstellung zu ändern, wenn Sie den Tumbler oft verwenden (wir werden später darüber sprechen), denn wenn es eine Spitze in den Gebühren während der Ausführung des letzteren gibt, wenn wir dieses Feld nicht richtig einstellen, riskieren wir, eine Menge Sats für CoinJoin auszugeben. Die Angabe von Tausenderwerten (z. B. 2000) entspricht 2 Sats/vBytes, 3500 entspricht 3,5 Sats/vBytes und so weiter. Ich würde eine Zahl zwischen 1500 und 6000 empfehlen, je nach Ihren Bedürfnissen.
- mit `max_cj_fee_abs` wird angegeben, wie viel wir in absoluten Zahlen für die Maker zu zahlen bereit sind, die wir während CoinJoin auswählen. Standardmäßig ist dieses Feld für Maker 200 Sats, eine gute Option könnte eine Zahl zwischen 200 und 1000 Sats pro Gegenstück sein (dies basiert darauf, wie viel Sie ausgeben wollen und wie viel Anon-Set Sie für Ihre CoinJoins suchen)
- max_cj_fee_rel" hat die gleiche Funktion wie das obige Feld, gibt aber die relativen Gebühren (Prozentsätze) an, die wir bereit sind, an jede Gegenpartei zu zahlen. Da es sich hierbei um einen `Prozentwert` handelt, sollten Sie darauf achten, keine hohen Werte einzustellen, um hohe Kosten bei CoinJoins mit großen Beträgen zu vermeiden. Der Standardwert für Maker ist _0.00002_, ich empfehle einen ähnlichen oder etwas höheren Wert.
- das Feld `minimum_makers` gibt an, mit wie vielen anderen Gegenparteien wir CoinJoin machen. Standardmäßig wählt joinMarket immer zwischen 4 und 9 Gegenparteien aus, wenn wir wollen, können wir diesen Wert für mehr Privatsphäre auf 5 oder 6 erhöhen (das macht die Transaktionen allerdings teurer).
- cjfee_a" gibt für den Fall, dass wir als Maker auftreten, an, wie viele Sats wir in absoluten Zahlen für die Vermietung unserer Liquidität einnehmen wollen. Dieses Feld ist völlig subjektiv, der Standardwert ist bereits sehr gut (wir haben also eine bessere Privatsphäre als Maker), wir können in Betracht ziehen, ihn auf 0 zu setzen, wenn wir mehr CoinJoin in weniger Zeit verdienen wollen.
- cjfee_r" ist dasselbe wie das obige Feld, aber in Prozent und nicht absolut. Auch hier empfehle ich, den Standardwert beizubehalten oder ihn zu senken, um mehr Teilnehmer anzuziehen.
- ordertype` mit diesem Feld wählen wir vom Anbieter, ob wir absolut (absoffer) oder prozentual (reloffer) bieten wollen. In der Regel bevorzugen Übernehmer absolute Gebote für wirtschaftliche Fragen.
- minsize", wenn wir als Hersteller nicht wollen, dass UTXO zu klein ist, können wir das Minimum von CoinJoin für die Teilnahme angeben. Dieses Feld wird in Satoshi ausgedrückt und ist völlig subjektiv. Wir könnten dieses Feld auf 0 belassen oder auf 500000 (Sats), 1000000 (Sats) usw. erhöhen.



Seien Sie sehr vorsichtig, dass Sie nicht die falschen Felder bearbeiten, denn einige der Variablen in der Datei joinmarket.cfg können bei falscher Einstellung die Funktionalität der Software beeinträchtigen oder Ihre Privatsphäre komplett zerstören, also Augen auf und Vorsicht!



## Einrichtung der Arbeitsumgebung



Einige Knoten setzen automatisch die korrekten Werte für diese Felder in der Datei joinmarket.cfg. Ich empfehle, dies manuell zu überprüfen:





- rpc_user = IhrBenutzername-wie-in-Bitcoin.conf`
- rpc_password = IhrPasswort-wie-in-Bitcoin.conf"
- rpc_host = localhost #Standard normalerweise korrekt`
- rpc_port = 8332 # Standard für Mainnet`



Jetzt können wir mit der Erstellung unseres Wallet in JoinMarket fortfahren:



```bash
python wallet-tool.py generate
```



Bei diesem Befehl müssen wir ein Passwort eingeben, mit dem der Wallet verschlüsselt werden soll, sowie den Namen, den wir ihm geben wollen. Wenn Sie gefragt werden, ob Sie Fidelity Bonds unterstützen wollen, empfehle ich Ihnen, die Option _yes_ zu wählen; die Ausgabe sieht dann so aus:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


falls eine Fehlermeldung erscheint, ist es sehr wahrscheinlich, dass wir die 4 oben angegebenen RPC-Felder falsch gesetzt haben. In diesem Fall könnte es hilfreich sein, [diesen Leitfaden](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) aus der Originaldokumentation von JoinMarket zu befolgen.



Wir haben die Einrichtung unserer Arbeitsumgebung abgeschlossen und können nun damit beginnen, die Befehle zu erkunden, die für uns am nützlichsten sein werden. Alle Skripte, die wir besprechen werden, können in der Konsole gestartet werden, gefolgt von "-help" für eine ausführliche Erklärung.



Wir können nun versuchen zu starten:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



dieser Befehl zeigt Ihnen alle verschiedenen Portfoliotiefen mit den verschiedenen Adressen an, die wie folgt kategorisiert sind:




- Neu (Address nie benutzt)
- Change-out (Rest einer früheren Transaktion)
- Cj-out (Ausgang eines CoinJoin)



hier ist ein praktisches Beispiel für das Ergebnis:



```bash
JM wallet
mixdepth	0	xpub6CMAJ67vZWVXuzjzYXUoJgWrmuvFRiqiUG4dwoXNFmJtpTH3WgviANNxGyZYo27zxbMuqhDDym6fnBxmGaYoxr6LHgNDo1eEghkXHTX4Jnx
external addresses	m/84'/0'/0'/0	xpub6FFUn4AxdqFbnTH2fyPrkLreEkStNnMFb6R1PyAykZ4fzN3LzvkRB4VF8zWrks4WhJroMYeFbCcfeooEVM6n2YRy1EAYUvUxZe6JET6XYaW
m/84'/0'/0'/0/0     	bc1qt493axn3wl4gzjxvfg03vkacre0m6f2gzfhv5t	0.00000000	new
m/84'/0'/0'/0/1     	bc1q2av9emer8k2j567yzv6ey6muqkuew4nh4rl85q	0.00000000	new
m/84'/0'/0'/0/2     	bc1qggpg0q7cn4mpe98t29wte2rfn2rzjtn3zdmqye	0.00000000	new
m/84'/0'/0'/0/3     	bc1qnnkqz8vcdjan7ztcpr68tyec7dw2yk8gjnr9ze	0.00000000	new
m/84'/0'/0'/0/4     	bc1qud5s2ln88ktg83hkr6gv9s576zvt249qn2lepx	0.00000000	new
m/84'/0'/0'/0/5     	bc1qw0lhq7xlhj7ww2jdaknv23vcyhnz6qxg23uthy	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/0'/1
Balance:	0.00000000
Balance for mixdepth 0:	0.00000000
mixdepth	1	xpub6CMAJ67vZWVXyTJEaZndxZy9ACUufsmNuJwp9k5dHHKa22zQdsgALxXvMRFSwtvB8BRJzsd8h17pKqoAyHtkBrAoSqC9AUcXB1cPrSYATsZ
external addresses	m/84'/0'/1'/0	xpub6FNSLcHuGnoUbaiKgwXuKpfcbR63ybrjaqHCudrma13NDqMfKgBtZRiPZaHjSbCY3P3cgEEcdzZCwrLKXeT5jeuk8erdSmBuRgJJzfNnVjj
m/84'/0'/1'/0/0     	bc1qhrvm7kd9hxv3vxs8mw2arcrsl9w37a7d6ccwe4	0.00000000	new
m/84'/0'/1'/0/1     	bc1q0sccdfrsnjtgfytul5zulst46wxgahtcf44tcw	0.00000000	new
m/84'/0'/1'/0/2     	bc1qst6p8hr8yg280zcpvvkxahv42ecvdzq63t75su	0.00000000	new
m/84'/0'/1'/0/3     	bc1q0gkarwg8y3nc2mcusuaw9zsn3gvzwe8mp3ac9h	0.00000000	new
m/84'/0'/1'/0/4     	bc1qkf5wlcla2qlg5g5sym9gk6q4l4k5c98vvyj33u	0.00000000	new
m/84'/0'/1'/0/5     	bc1qz6zptlh3cqty2tqyspjk6ksqelnvrrrvmyqa5v	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/1'/1
Balance:	0.00000000
Balance for mixdepth 1:	0.00000000
mixdepth	2	xpub6CMAJ67vZWVY2cq5fmVxXw92fcgTchphGNFxweSiupYH1xYfjBiK6dj5wEEVAQeA4JcGDQGm2xcuz2UsMnDkzVmi2ESZ3xey63mQMY4x2w2
external addresses	m/84'/0'/2'/0	xpub6DqkbMG3tj2oixGYniEQTFamLCHTZx9CeAbUdBttiGuYwgfGZbrLMor8LWeJBUqTpsa81JcJqAUXuDxhXdLpKDxJAEqKMqPgJyXstj5dp3o
m/84'/0'/2'/0/0     	bc1qwtdgg928wma8jz32upkje7e4cegtef7yrv233l	0.00000000	new
m/84'/0'/2'/0/1     	bc1qhkuk2gny4gumrxcaw999uq3jm3fjrjvcwz7lz3	0.00000000	new
m/84'/0'/2'/0/2     	bc1qvu753lkltc8akfasclnq89tdv8yylu2alyg76y	0.00000000	new
m/84'/0'/2'/0/3     	bc1qal3r040k26cw2f08337huzcf00hrnws5rhfrz3	0.00000000	new
m/84'/0'/2'/0/4     	bc1qpv4nm7wwtxesgwsr0g0slxls33u0w02gqx2euk	0.00000000	new
m/84'/0'/2'/0/5     	bc1qk3ekjzlvw3uythw738z7nvwe2sg93w2rtuy6ml	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/2'/1
Balance:	0.00000000
Balance for mixdepth 2:	0.00000000
mixdepth	3	xpub6CMAJ67vZWVY3uty61M6jeGheGU5ni5mQmqMW2QLQbEa8ZQXuBw1K2umKFZsmU8EMEafJZKQkGS1trtWE5dtz4XmDbvLvUccAPn26ZC5i2o
external addresses	m/84'/0'/3'/0	xpub6EvT4QFPRdkt2sji3QdLLZjkJQmk7G2y3umT99ceomKTXGYvZ5S9TLaGos6cEugXEuxS6s9kvSUj1Xvpiu65dn5yzK7CgdZLzXawpKC9Mpe
m/84'/0'/3'/0/0     	bc1q9ph5l2gknjezcmzv84rnhu4df566jgputzef7l	0.00000000	new
m/84'/0'/3'/0/1     	bc1qrlvmmxfuryr3mfhssjv45h0fl6s43g3vzrkwca	0.00000000	new
m/84'/0'/3'/0/2     	bc1q40xkajgv9q42ve92zstwjc9v4jgauxme9su6uc	0.00000000	new
m/84'/0'/3'/0/3     	bc1q38pfk8yfnu97v4mckkuk2dhk9u8geuyzu9c0hc	0.00000000	new
m/84'/0'/3'/0/4     	bc1q2qzxyw56em9qdxc5z5s5xjz3j6s2qlzn3juvtu	0.00000000	new
m/84'/0'/3'/0/5     	bc1qd2f8f3dau5pfjqu7dpuvt6fahj36w4rgl3xevr	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/3'/1
Balance:	0.00000000
Balance for mixdepth 3:	0.00000000
mixdepth	4	xpub6CMAJ67vZWVY7gT4oJQBMc1fhbausT57yNVLCLCMwaGed5spHKaQY1EMQxvL2vTgDfhEimuAy7bzBE1qx5uY6D7cpUjQtXPHpyJzFuUtQPN
external addresses	m/84'/0'/4'/0	xpub6EQWpKsBTG3N9TFU4v6WtCcBJuLAeTZTcUwVJTxYUAsHeVPFdey4qT1dg4G7MqvnFFgHZDxqTo37S81UWUA2BqKKoTff1pcHTcSFzxyp5JG
m/84'/0'/4'/0/0     	bc1qdpjh3ewm367jm5eazqdf8wfrm09py50wn47urs	0.00000000	new
m/84'/0'/4'/0/1     	bc1q2x0fmtms5nr3wz3x3660c8wampg7t22e6m30t8	0.00000000	new
m/84'/0'/4'/0/2     	bc1q23595yg3dkj8gd3jrgup0hyzslhzf9skrg50r5	0.00000000	new
m/84'/0'/4'/0/3     	bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl	0.00000000	new
m/84'/0'/4'/0/4     	bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes	0.00000000	new
m/84'/0'/4'/0/5     	bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/4'/1
Balance:	0.00000000
Balance for mixdepth 4:	0.00000000
Total balance:	0.00000000
```


Jetzt können wir fortfahren, unsere ersten Satoshis in einer oder mehreren Adressen zu deponieren, wobei wir uns daran erinnern, dass die Software unabhängig vom Erzeuger oder Nehmer niemals UTXO direkt in verschiedene Mischtiefen konsolidieren wird. Auf diese Weise können wir Satss mit verschiedenen Vertraulichkeitsstufen in Wallet getrennt halten.



## Senden von Bitcoin mit CoinJoin einzeln



Wir können nun unsere Satoshis verschieben. Einer der wichtigsten Befehle in dieser Software ist das Skript:



```bash
pyhton sendpayment.py
```


die es uns ermöglichen wird, Transaktionen an andere Adressen mit oder ohne CoinJoin zu senden. Lassen Sie uns die Funktionsweise und einige praktische Beispiele durchgehen. Die Standardformatierung des Befehls ist (denken Sie daran, den von den Symbolen < und > eingeschlossenen Text zu ersetzen):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



ein einfaches Beispiel für die Verwendung könnte sein:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


in diesem Fall senden wir an Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0,05 Btc, d.h. 5000000 Satoshi aus unserer Mischtiefe 0 (die Standardeinstellung), indem wir 4 bis 9 Gegenstücke für CoinJoin (Standardoption) auswählen.



Um mehr Kontrolle darüber zu haben, wie und welche UTXOs ausgegeben werden sollen, können wir die zusätzlichen Optionen zu diesem Befehl durchgehen:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


in diesem Beispiel haben wir zwei Angaben hinzugefügt: -N gibt an, mit wie vielen Gegenparteien wir mischen werden, -m die Mischtiefe, von der wir Geld abheben werden. In der Tat haben wir 100.000.000 Sats (1 btc) an den Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c mit den Mitteln in der Mixdepth 1 und der Mischung mit 5 Gegenparteien gesendet.



Wenn wir als Sendewert 0 angeben, führt joinMarket einen so genannten "Sweep" durch, d. h. es sendet alle Fonds in dieser Tiefe, indem es sie miteinander konsolidiert:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



hier haben wir alle Mittel aus der Mixtiefe 0 (die wir nicht hätten angeben können, da dies die Standardeinstellung ist) mit 7 Gegenwerten gemischt.



Der Befehl sendpayment wird verwendet, um Gelder von joinMarket auf externe Wallet zu übertragen oder um Satoshi an eine Person zu senden, indem ein Layer der Privatsphäre zwischen uns und ihr hinzugefügt wird. Um ein ausreichendes Maß an Privatsphäre auf unseren UTXOs zu erreichen, ist es sinnvoller, den Befehl tumbler.py zu verwenden, den wir später in diesem Leitfaden erklären werden.



## Ein Macher sein



Das Skript, das wir in diesem Abschnitt behandeln werden, ist:



```bash
yg-privacyenhanced.py
```



Dieses Programm dient dazu, als Maker auf dem joinMarket zu agieren. Die Software stellt eine Verbindung zu unserem Bitcoin-Knoten und zum internen Marktplatz der Plattform her, auf dem sich die Maker als Liquiditätsanbieter präsentieren und die Taker nach Gegenparteien suchen. Falls Sie einen Fidelity Bond verwenden möchten, können Sie ihn mit dieser Formatierung erstellen:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



zum Beispiel:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



die Ausgabe, die an uns zurückgeschickt wird, ist eine Bitcoin Address (d. h. diejenige, auf der Sie die Gelder, die Sie Fidelity zuweisen wollen, hinterlegen müssen).



**Vorsicht**: Es gibt zwei Dinge, auf die Sie achten müssen, wenn Sie eine Treueanleihe (auch bekannt als FB) erstellen wollen;





- wenn das Geld einmal eingezahlt wurde, kann es bis zum Ablauf der Frist nicht mehr bewegt werden. Achten Sie darauf, wie viele Satss Sie an die Address senden und wie Sie das Datum formatieren. Irrtümer sind nicht erlaubt!
- Der Fidelity Bond ist auf der Kette leicht zu erkennen, daher ist es ratsam, Gelder über einen CoinJoin und mit einer Herkunft, die nichts mit Ihrer Identität zu tun hat, einzuzahlen. Dasselbe ist auch ratsam, wenn Sie den abgelaufenen Treueschein aus JoinMarket entfernen möchten.



Es ist wichtig, sich daran zu erinnern, dass es möglich ist, die Treueanleihe mit nur einer Transaktion aufzuladen, im Falle von UTXO wird nur die größte Transaktion als gültig für FB angesehen.



Nachdem wir die Treueanleihe erstellt haben (die, wie wir uns erinnern, optional ist), können wir das ausführbare Programm starten, um als Maker auf joinMarket zu agieren. Sobald die Satss an den verschiedenen Adressen und Mixdepth hinterlegt sind, können wir den Befehl ausführen:



```bash
python yg-privacyenhanced.py <wallet name>
```



Von diesem Zeitpunkt an (nach ein paar Minuten der Verbindung mit dem Netzwerk) und bis wir das Skript stoppen, wird unser JoinMarket-Client auf der Liste der aktiven Maker im Protokoll erscheinen und unsere Liquidität verschiedenen Gegenparteien anbieten, um CoinJoin zu machen. Erwarten Sie nicht Dutzende von CoinJoins pro Tag (es sei denn, Sie haben große Geiz und große Liquidität auf Wallet hinterlegt), auch daran denken, dass Faktoren wie Gebühren erforderlich und Satoshis hinterlegt beeinflussen, wie oft Sie ein Maker sein wird.



Wenn Sie den nachstehenden Befehl ausführen, können Sie die Historie aller mit Wallet getätigten Transaktionen sowie alle Gewinne (wenn Sie ein Maker sind) oder Kosten (wenn Sie ein Taker sind), die Sie während der Laufzeit des Portfolios hatten, einsehen.



```bash
python wallet-tool.py <wallet name> history
```



Sobald Ihre Satoshis CoinJoins machen, wandern sie von Mixdepth zu Mixdepth, bis sie die letzte erreichen. Sobald sie die vierte hinter sich gelassen haben, kehren sie zur Mischtiefe 0 zurück. Es liegt an Ihnen, wie viel Privatsphäre Sie haben möchten, bevor Sie sie zu einem Cold Wallet verschieben, es ist ratsam, einen vollen Wallet-Zyklus zu beenden.



## Becher



Hier sind wir nun endlich bei dem interessantesten Teil von JoinMarket, dem Becher! Wenn Sie sich den Podcast angehört haben, wissen Sie bereits, worum es geht. Bevor wir loslegen, noch eine Empfehlung: **Vorsicht vor den Gebühren!** Denken Sie daran, die Limits in der Datei joinmarket.cfg zu setzen (wie zu Beginn erklärt) und erwägen Sie, das Programm nur dann laufen zu lassen, wenn die Onchain-Gebühren relativ niedrig sind (unter 10 Sats/vB).



Um den Tumbler zu starten, muss das Skript von Maker gestoppt werden (falls es aktiv war), danach können wir den Befehl ausführen:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Es ist wichtig, **mindestens** 3 Ausgabeadressen für den Tumbler einzugeben: Dies soll eine gute Privatsphäre gewährleisten und keine offensichtlichen Verbindungen zwischen UTXOs während des gesamten Prozesses herstellen. Wie üblich kann man durch Hinzufügen von `--help` zum Befehl alle zusätzlichen Details einsehen. Sehen wir uns nun ein komplexeres Beispiel mit erweiterten Regeln an:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



In diesem Fall haben wir ein Tumbling-Skript gestartet, das nicht die Standardanzahl von Gegenstücken verwendet (der Parameter -N gibt an, dass wir 7 Gegenstücke mit einer maximalen Varianz von 2 benötigen, also eine zufällige Anzahl von Machern von 5 bis 9) und mit einer größeren Anzahl von CoinJoin pro Mixtiefe (standardmäßig macht dieses Skript eine zufällige Anzahl von CoinJoin pro Abschnitt von Wallet im Bereich von 1 bis 3, wenn wir stattdessen den Befehl -c 3 1 verwenden, wird es von 2 bis 4 sein). Auf diese Weise werden wir mehr Sats in Gebühren ausgeben, haben aber eine größere Anonymität.



Sie können auch so viele Ausgabeadressen hinzufügen, wie Sie möchten (mindestens 3, es gibt keine Höchstzahl außer dem gesunden Menschenverstand). Aus Datenschutzgründen ist es jedoch nicht möglich, zu entscheiden, wie Satoshi auf die als Ausgabe angegebenen Adressen verteilt wird.



Tumbler ist ein absichtlich langwieriger Prozess, gelegentlich kann es vorkommen, dass etwas nicht mehr funktioniert, in den meisten Fällen löst sich dies innerhalb weniger Stunden von selbst. Im Falle eines Totalabsturzes können wir versuchen, ihn mit dem Befehl neu zu starten:



```bash
python tumbler.py --restart
```



Oder starten Sie einfach einen neuen Tumblerbefehl. Dies wird nicht die Planung des vorherigen Tumbler starten, sondern einen neuen Mischzyklus beginnen. Falls das Schließen des SSH-Terminals zu Ihrem Knoten auch das Skript stoppt, können Sie das Programm `TMUX` nutzen, das mit dem Befehl installiert werden kann:



```bash
sudo apt install tmux
```



Wenn Sie es von der Shell aus starten, indem Sie `tmux` eingeben, wird ein Terminal für Sie geöffnet, das im Hintergrund aktiv bleibt, auch wenn Sie die Fernverbindung schließen. Wenn Sie die Verbindung zu Ihrem Knoten mit dem Kommando erneut herstellen: `tmux attach` öffnen Sie wieder die Shell, die im Hintergrund aktiv blieb.



## Schlussfolgerung



JoinMarket ist eine grenzenlose und anpassbare Software. In diesem Leitfaden haben wir die wichtigsten Funktionen entdeckt, so dass es für jeden möglich ist (oder zumindest habe ich versucht, ich weiß, dass die Verwendung dieser Software ist kein Spaziergang im Park), es zu benutzen. Eines der größten Probleme von JoinMarket ist genau das: die Anzahl der Nutzer und die Tatsache, dass es ein Maker ist. Wenn nur wenige Nutzer die Vorteile dieser Software nutzen, wird die allgemeine Privatsphäre (anon-set) herabgesetzt. Deshalb hoffe ich, dass dieser Leitfaden einen Anreiz zur Nutzung bietet und Sie davon überzeugt, meine Lieblingssoftware herunterzuladen und zu installieren, um CoinJoin herzustellen. Für den Fall, dass Sie noch tiefer in einige Aspekte einsteigen wollen, empfehle ich Ihnen, die verschiedenen ausführlichen Dokumente auf github zu lesen, sie sind sehr gut gemacht und Sie können sie hier finden.



Glückliche Schildkröten beim Mischen!🐢 💚



[Hier](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) können Sie Turtlecute unterstützen