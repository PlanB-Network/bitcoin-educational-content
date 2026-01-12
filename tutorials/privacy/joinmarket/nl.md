---
name: JoinMarket

description: Handleiding en tutorial over hoe JoinMarket te gebruiken om CoinJoin over Bitcoin te doen via de opdrachtregel
---

![cover](assets/cover.webp)



---

Als je deze pagina hebt gevonden door online te zoeken naar "JoinTmarket", dan heb je mijn oprechte waardering. Je bent echter op een gids gestuit die over een heel ander, maar uiterst interessant onderwerp gaat! 🚬🍁



Het doel van deze tutorial is om de theoretische en praktische werking van JoinMarket te illustreren via de opdrachtregel. 🐢 💚



## JoinMarket Theoretische definitie



We kunnen JoinMarket definiëren als een hulpmiddel, of een Wallet, dat CoinJoin met andere gebruikers mogelijk maakt op een volledig Trustless manier en zonder centrale coördinator.



Omdat het hele theoretische gedeelte van deze tool erg breed is, heb ik besloten om Address in een specifieke aflevering van mijn podcast te behandelen. Voor degenen die Italiaans kunnen verstaan, raad ik aan om na het beluisteren van de aflevering verder te lezen, zodat ze de basisconcepten voor het juiste gebruik van dit programma beter kunnen assimileren.



Je kunt de aflevering bekijken via deze directe links:




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (hier kun je het direct vanuit de browser beluisteren).
- [Antenna pod](https://antennapod.org/) is een gratis en open source podcastmanager waarvoor geen registratie nodig is. Download de app om de aflevering te vinden, voeg mijn podcast handmatig toe door [deze link](https://Anchor.fm/s/bd5d5b20/podcast/rss) in de _feed rss_ sectie te plakken en zoek vervolgens naar de aflevering die aan JoinMarket is gewijd.



## Installatie



Besturingssystemen:





- Raspiblitz
- Paraplu
- MijnNode
- Raspibolt



## Configuratiebestanden



JoinMarket is een aanpasbare software met een oneindig aantal instellingen; deze instellingen worden gespecificeerd in een configuratiebestand in de hoofdmap van het programma genaamd `Joinmarket.cfg`.



In dit gedeelte gaan we een aantal velden bespreken die je misschien interessant vindt om te onderzoeken en/of aan te passen, afhankelijk van je behoeften. Ik wil benadrukken dat alle wijzigingen die hieronder worden genoemd nuttig zijn om te weten om de werking van de software aan te passen aan persoonlijke behoeften, maar dat ze niet verplicht zijn.



Laten we eerst naar de map `joinmarket/scripts` gaan en het commando uitvoeren:



```bash
python wallet-tool.py generate
```


Op dit punt zouden we een foutmelding moeten krijgen, maar door dit te doen zal de software generate een vooraf ingesteld instellingenbestand voor ons maken. We kunnen het instellingenbestand vanaf de terminal bewerken met:



```bash
nano joinmarket.cfg
```



of:



```bash
vim joinmarket.cfg
```



eenmaal geopend zien we talloze regels met verschillende instellingen en hun uitleg in het Engels. Hieronder analyseren we de meest interessante variabelen:





- `merge_algorithm` in het geval we dat doen als een maker dit veld past aan hoe agressief de software zal consolideren ongebruikte Outputs. Als we veel UTXO's hebben om te consolideren, kan het zinvol zijn om van _gradual_ naar _greedy_ te schakelen
- `tx_fees` past als nemer de vergoedingen aan waarmee de transactie wordt betaald, het is erg handig om deze instelling te veranderen als je de tumbler vaak gebruikt (we zullen het hier later over hebben), want als er een piek is in de vergoedingen tijdens de uitvoering van de laatste, als we dit veld niet goed instellen, lopen we het risico dat we veel Sats voor CoinJoin uitgeven. Door waarden in duizendtallen in te stellen (zoals 2000) komt dit neer op 2 Sats/vBytes, 3500 op 3,5 Sats/vBytes, enzovoort. Ik zou een getal tussen 1500 en 6000 aanraden, afhankelijk van je behoeften.
- `max_cj_fee_abs` wordt gebruikt om aan te geven hoeveel we bereid zijn te betalen in absolute termen voor de makers die we kiezen tijdens CoinJoin. Standaard is dit veld voor makers 200 Sats, een goede optie zou kunnen zijn een getal variërend van 200 tot 1000 Sats per tegenhanger. Standaard is dit veld voor makers 200 Sats, een goede optie zou een getal tussen 200 en 1000 Sats per tegenhanger kunnen zijn (dit is gebaseerd op hoeveel je wilt uitgeven en hoeveel anon-set je zoekt voor je CoinJoins)
- `max_cj_fee_rel` heeft dezelfde functie als het veld hierboven, maar specificeert de relatieve vergoedingen (percentages) die we bereid zijn aan elke tegenpartij te betalen. Aangezien dit een `percentage` waarde is, moet je oppassen dat je geen hoge waarden instelt om hoge kosten in CoinJoins met grote bedragen te voorkomen. De standaardwaarde voor makers is _0.00002_, ik raad een vergelijkbare of iets hogere waarde aan.
- `minimum_makers` is het veld dat aangeeft met hoeveel andere tegenpartijen we CoinJoin doen, standaard kiest joinMarket altijd tussen 4 en 9 tegenpartijen, als we willen, voor meer privacy, kunnen we deze waarde verhogen naar 5 of 6 (dit maakt de transacties wel duurder).
- `cjfee_a` specificeert, als we optreden als maker, hoeveel Sats we in absolute termen willen innen voor het verhuren van onze liquiditeit. Dit veld is volledig subjectief, de standaardwaarde is al erg goed (we hebben dus meer privacy als maker), we kunnen overwegen om het op 0 te zetten als we meer CoinJoin in minder tijd willen verdienen.
- `cjfee_r` hetzelfde als bovenstaand veld, maar dan in percentages en niet absoluut. Ook hier raad ik aan om de standaardwaarde te laten staan of deze te verlagen om meer aanvragers aan te trekken.
- `ordertype` met dit veld kiezen we van de maker of we absoluut (absbod) of procentueel (relbod) willen bieden. Meestal geven kopers de voorkeur aan absolute biedingen voor economische kwesties.
- `minsize` als we als maker UTXO niet te klein willen hebben, kunnen we het minimum CoinJoin opgeven om mee te doen. Dit veld wordt uitgedrukt in Satoshi en is geheel subjectief. We kunnen dit veld op 0 laten staan of verhogen naar 500000 (Sats), 1000000 (Sats), enzovoort.



Wees heel voorzichtig dat je niet de verkeerde velden bewerkt, sommige variabelen in het joinmarket.cfg bestand kunnen, als ze verkeerd zijn ingesteld, de functionaliteit van de software in gevaar brengen of je privacy volledig vernietigen, ogen open en uiterste voorzichtigheid geboden!



## Werkomgeving instellen



Sommige nodes stellen automatisch de juiste waarden in voor deze velden in het joinmarket.cfg bestand, maar ik raad aan om dit handmatig te controleren:





- `rpc_user = uwgebruikersnaam-zoals-in-Bitcoin.conf`
- `rpc_wachtwoord = jouwwachtwoord-zoals-in-Bitcoin.conf`
- `rpc_host = localhost #standaard meestal correct`
- `rpc_port = 8332 # standaard voor Mainnet`



Op dit punt kunnen we verder gaan met het aanmaken van onze Wallet binnen JoinMarket:



```bash
python wallet-tool.py generate
```



Dit commando laat ons een wachtwoord invoeren waarmee we de Wallet willen versleutelen en de naam die we eraan willen geven, wanneer het vraagt of je al dan niet fidelity bonds wilt ondersteunen raad ik aan de _yes_ optie te gebruiken, de uitvoer die je terugkrijgt ziet er als volgt uit:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


als er een foutmelding verschijnt, is het waarschijnlijk dat we de 4 RPC velden die hierboven zijn gespecificeerd, onjuist hebben ingesteld. In dat geval kan het helpen om [deze gids](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) te volgen die je kunt vinden in de originele JoinMarket documentatie.



We zijn klaar met het opzetten van onze werkomgeving en kunnen beginnen met het verkennen van de commando's die ons het meest van pas zullen komen. Alle scripts die we zullen bespreken kunnen worden gestart in de console gevolgd door `--help` voor een diepgaande uitleg.



We kunnen nu proberen te lanceren:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



dit commando toont je alle verschillende Wallet mixdepths met de verschillende adressen gecategoriseerd als:




- Nieuw (Address nooit gebruikt)
- Change-out (restant van een vorige transactie)
- Cj-out (uitgang van een CoinJoin)



hier is een praktisch voorbeeld van het resultaat:



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


Nu kunnen we overgaan tot het storten van onze eerste Satoshi's binnen één of meerdere adressen, waarbij we onthouden dat ongeacht de maker of nemer, de software nooit direct UTXO zal gaan consolideren in verschillende mixdieptes, op deze manier kunnen we Satss met verschillende niveaus van privacy gescheiden houden binnen Wallet.



## Bitcoin met CoinJoin enkel verzenden



We kunnen nu onze Satoshi's verplaatsen. Een van de belangrijkste commando's in deze software is het script:



```bash
pyhton sendpayment.py
```


waarmee we transacties naar andere adressen kunnen sturen, met of zonder CoinJoin. Laten we eens kijken hoe het werkt en wat praktische voorbeelden geven. Standaard is de opmaak van het commando (vergeet niet om de tekst ingesloten door de symbolen < en > te vervangen):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



een eenvoudig gebruiksvoorbeeld zou kunnen zijn:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


in dit geval gaan we naar Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0,05 Btc sturen, d.w.z. 5000000 Satoshi van onze mixdepth 0 (de standaard) door te kiezen tussen 4 en 9 tegenhangers voor CoinJoin (standaard optie).



Om meer controle te hebben over hoe en welke UTXO's worden uitgegeven, kunnen we de extra opties van dit commando bekijken:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


in dit voorbeeld hebben we twee specificaties toegevoegd: -N geeft aan met hoeveel tegenpartijen we gaan mixen, -m de mixdiepte waaraan we geld gaan onttrekken. In feite hebben we 100.000.000 Sats (1 btc) naar Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c gestuurd met de fondsen in mixdepth 1 en mix met 5 tegenpartijen.



Als we 0 als verzendwaarde zetten door een mixdiepte op te geven, zal joinMarket een zogenaamde `sweep` uitvoeren, dat wil zeggen, het zal alle fondsen in die mixdiepte verzenden door ze met elkaar te consolideren:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



hier hebben we alle fondsen van mixdepth 0 (we hadden het niet kunnen specificeren omdat dat de standaard is) gemengd met 7 tegenhangers.



Het sendpayment commando wordt gebruikt om geld te verplaatsen van joinMarket naar externe Wallet of om Satoshi naar een persoon te sturen door een Layer van privacy toe te voegen tussen ons en hem. Om voldoende privacy op onze UTXO's te krijgen is het beter om het tumbler.py commando te gebruiken, dat we later in deze gids zullen uitleggen.



## Een maker zijn



Het script dat we in dit gedeelte gaan behandelen is:



```bash
yg-privacyenhanced.py
```



Dit programma wordt gebruikt om op te treden als maker in de joinMarket. De software maakt verbinding met onze Bitcoin node en met de interne marktplaats van het platform waar de makers zich presenteren als liquiditeitsbieders en takers tegenpartijen zoeken. Als je een fidelity bond wilt gebruiken, kun je er een maken met deze opmaak:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



bijvoorbeeld:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



de uitvoer die naar ons teruggestuurd zal worden, zal een Bitcoin Address zijn (d.w.z. de uitvoer waarop u de fondsen moet storten die u aan fidelity wilt toewijzen).



**Let op**: Er zijn twee dingen waar je goed op moet letten als je een Fidelity Bond (ook bekend als FB) gaat maken;





- als het geld eenmaal is gestort, kan het niet meer worden verplaatst totdat het verloopt. Let goed op hoeveel Satss je naar de Address stuurt en hoe je de datum opmaakt. Fouten zijn niet toegestaan!
- De fidelity bond is gemakkelijk herkenbaar op de keten, dus het is raadzaam om geld te storten via een CoinJoin en met een oorsprong die niet gerelateerd is aan je identiteit. Hetzelfde is ook aan te raden wanneer je de verlopen loyaliteitsgarantie uit JoinMarket wilt verwijderen.



Het is belangrijk om te onthouden dat het mogelijk is om de getrouwheidsobligatie te herladen met slechts één transactie, in het geval van UTXO veelvouden zal alleen de grootste als geldig voor FB worden beschouwd.



Laten we nu het script behandelen dat aan het begin van deze paragraaf is genoemd, zodra we de fidelity bond hebben aangemaakt (waarvan we ons herinneren dat het optioneel is) zijn we klaar om de executable uit te voeren om op te treden als maker op joinMarket. Zodra de Satss zijn gedeponeerd op de verschillende adressen en mixdepth kunnen we het commando uitvoeren:



```bash
python yg-privacyenhanced.py <wallet name>
```



Vanaf dit punt (na een paar minuten verbinding te hebben gemaakt met het netwerk) en totdat we het script stoppen, zal onze JoinMarket client verschijnen op de lijst van actieve makers op het protocol en onze liquiditeit aanbieden aan verschillende tegenpartijen om CoinJoin te maken. Verwacht geen tientallen CoinJoins per dag (tenzij je een enorme fidliteit hebt en veel liquiditeit op Wallet hebt gestort), vergeet ook niet dat factoren zoals vereiste vergoedingen en gestorte Satoshis van invloed zijn op hoe vaak je een maker zult zijn.



Door het onderstaande commando uit te voeren, kun je de geschiedenis van alle transacties op Wallet zien en alle winsten (als je een maker bent) of kosten (als je een nemer bent) die je hebt gehad tijdens de levensduur van Wallet.



```bash
python wallet-tool.py <wallet name> history
```



Zodra je Satoshi's CoinJoins maken, gaan ze van mixdiepte naar mixdiepte tot ze de laatste bereiken. Eenmaal voorbij de vierde zullen ze terugkeren naar mixdiepte 0, het is aan jou hoeveel privacy je wilt voordat je ze verplaatst naar een Cold Wallet, het is aan te raden om een volledige Wallet cyclus af te maken.



## Tuimelaar



Hier zijn we dan eindelijk bij het sappigste onderdeel van JoinMarket, de tumbler! Als je naar de podcast hebt geluisterd, weet je al waar dit over gaat. Eén aanbeveling voordat we beginnen: **Vergeet niet de limieten in te stellen in het joinmarket.cfg bestand (zoals uitgelegd aan het begin) en overweeg het programma alleen te draaien wanneer de onchain fees relatief laag zijn (onder de 10 Sats/vB).**



Om de tumbler te starten is het nodig om het script van maker te stoppen (als het actief was), daarna kunnen we het commando uitvoeren:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Het is essentieel om **minstens** 3 uitvoeradressen voor de tuimelaar in te voeren: dit is om een goede privacy te garanderen en om geen duidelijke links tussen UTXO's te maken tijdens het proces. Zoals gebruikelijk kun je door `--help` aan het commando toe te voegen alle aanvullende details bekijken. Laten we een complexer voorbeeld gaan bekijken met geavanceerde regels:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



In dit geval hebben we een tuimelscript gestart dat niet het standaard aantal tegenhangers zal gebruiken (de -N parameter geeft aan dat we 7 tegenhangers nodig hebben met een maximale variantie van 2, dus een willekeurig aantal makers van 5 tot 9) en met een groter aantal CoinJoin per mixdiepte (standaard maakt dit script een willekeurig aantal CoinJoin per sectie van Wallet variërend van 1 tot 3, met het -c 3 1 commando in plaats daarvan zal het van 2 tot 4 zijn). Op deze manier geven we meer Sats uit aan vergoedingen, maar hebben we een grotere anonimiteitsset.



Je kunt ook zoveel uitvoeradressen toevoegen als je wilt (minimaal 3, er is geen maximum behalve gezond verstand). Om privacyredenen is het echter niet mogelijk om te bepalen hoe Satoshi wordt verdeeld over de adressen die als uitvoer zijn opgegeven.



Tumbler is een bewust lang proces, af en toe kan het gebeuren dat iets stopt met werken, in de meeste gevallen lost dit zichzelf binnen een paar uur op. In het geval van een totale crash kunnen we proberen het opnieuw op te starten met het commando:



```bash
python tumbler.py --restart
```



Of start gewoon een nieuw trommelcommando. Dit zal niet het schema van de vorige tumbler starten, maar zal een nieuwe mengcyclus starten. Als het afsluiten van de SSH-terminal naar je node ook het script stopt, kun je gebruikmaken van het programma `TMUX` dat met het commando kan worden geïnstalleerd:



```bash
sudo apt install tmux
```



Als je het vanuit de shell start door `tmux` in te typen, wordt er een terminal voor je geopend die op de achtergrond actief blijft, zelfs als je de externe verbinding sluit. Wanneer je opnieuw verbinding maakt met je knooppunt met het commando: `tmux attach` open je opnieuw de shell die op de achtergrond actief bleef.



## Conclusie



JoinMarket is grenzeloze en aanpasbare software. In deze gids hebben we de belangrijkste functies ontdekt zodat het voor iedereen mogelijk is (althans ik heb het geprobeerd, ik realiseer me dat het gebruik van deze software geen walk in the park is) om het te gebruiken. Een van de grootste problemen met JoinMarket is juist dat: het aantal mensen dat het gebruikt en een maker is. Als weinig gebruikers gebruik maken van deze software, wordt de algemene privacy (anon-set) verlaagd. Daarom hoop ik dat deze gids het gebruik zal stimuleren en je zal overtuigen om mijn favoriete software te downloaden en te installeren om CoinJoin te maken. Als je nog dieper op sommige aspecten wilt ingaan, raad ik je aan om de verschillende diepgaande docs op github te lezen, ze zijn vermanete goed gedaan en je kunt ze hier vinden.



Happy mixing schildpadden!



[Hier](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) kunt u Turtlecute steunen