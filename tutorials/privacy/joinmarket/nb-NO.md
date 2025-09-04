---
name: JoinMarket

description: Veiledning og opplæring i hvordan du bruker JoinMarket til å gjøre CoinJoin over Bitcoin via kommandolinjen
---

![cover](assets/cover.webp)



---

Hvis du fant denne siden ved å søke på nettet etter "JoinTmarket", har du min oppriktige takknemlighet. Du har imidlertid snublet over en guide som omhandler et helt annet, men ekstremt interessant tema! 🚬🍁



Målet med denne veiledningen er å illustrere den teoretiske og praktiske bruken av JoinMarket via kommandolinjen. 🐢 💚



## JoinMarket Teoretisk definisjon



Vi kan definere JoinMarket som et verktøy, eller en Wallet, som muliggjør CoinJoin med andre brukere på en helt Trustless-måte og uten noen sentral koordinator.



Siden hele den teoretiske delen av dette verktøyet er ekstremt omfattende, bestemte jeg meg for å Address det i en egen episode av podcasten min. For de som forstår italiensk, anbefaler jeg på det sterkeste å fortsette å lese etter å ha lyttet til episoden, slik at du bedre kan assimilere de grunnleggende konseptene for å bruke dette programmet riktig.



Du kan se episoden via disse direktelinkene:




- [Spotify] (https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast] (https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor] (https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (her kan du lytte til den direkte fra nettleseren).
- [Antenna pod](https://antennapod.org/) er en gratis og åpen kildekode podcast manager som ikke krever registrering. For å finne episoden, last ned appen, legg til podcasten min manuelt ved å lime inn [denne lenken](https://Anchor.fm/s/bd5d5b20/podcast/rss) i _feed rss_-delen, og søk deretter etter episoden som er dedikert til JoinMarket.



## Installasjon



Operativsystemer:





- Raspiblitz
- Paraply
- MinNode
- Raspibolt



## Konfigurasjonsfiler



JoinMarket er en programvare som kan tilpasses med et uendelig antall innstillinger; disse innstillingene er spesifisert i en konfigurasjonsfil som ligger i hovedprogramkatalogen og heter `Joinmarket.cfg`.



I denne delen skal vi gå gjennom noen felt som kan være interessante å utforske og/eller endre, avhengig av dine behov. Jeg vil understreke at alle endringene som er oppført nedenfor, er nyttige å kjenne til for å tilpasse driften av programvaren til personlige behov, men at de ikke er obligatoriske.



La oss først gå til mappen `joinmarket/scripts` og kjøre kommandoen:



```bash
python wallet-tool.py generate
```


På dette tidspunktet skal vi få en feilmelding, men hvis vi gjør det, vil programvaren generate en forhåndsinnstilt innstillingsfil for oss. Vi kan redigere innstillingsfilen fra terminalen med :



```bash
nano joinmarket.cfg
```



eller:



```bash
vim joinmarket.cfg
```



når den er åpnet, vil vi legge merke til mange linjer med forskjellige innstillinger og deres forklaring på engelsk. Nedenfor vil vi analysere de mest interessante variablene:





- `merge_algorithm` i tilfelle vi gjør det som en produsent, justerer dette feltet hvor aggressivt programvaren vil konsolidere ubrukte utganger. Hvis vi har mange UTXO-er som skal konsolideres, kan det være fornuftig å bytte fra _gradual_ til _greedy_
- `tx_fees` justerer som en taker gebyrene som skal betale transaksjonen, det er veldig nyttig å endre denne innstillingen i tilfelle du bruker tumbleren ofte (vi vil snakke om dette senere) fordi hvis det er en topp i gebyrene under utførelsen av sistnevnte, hvis vi ikke setter dette feltet riktig, risikerer vi å bruke mye Sats for CoinJoin. Ved å angi verdier i tusen (for eksempel 2000) vil dette tilsvare 2 Sats/vBytes, 3500 tilsvarer 3,5 Sats/vBytes, og så videre. Jeg vil anbefale et tall fra 1500 til 6000, avhengig av dine behov.
- `max_cj_fee_abs` brukes til å spesifisere hvor mye vi er villige til å betale i absolutte termer for produsentene vi velger i løpet av CoinJoin. Som standard er dette feltet for makere 200 Sats, et godt alternativ kan være et tall fra 200 til 1000 Sats per motpart (dette er basert på hvor mye du ønsker å bruke og hvor mye anon-set du ønsker for dine CoinJoins)
- `max_cj_fee_rel` har samme funksjon som feltet ovenfor, men angir de relative gebyrene (prosentandelene) vi er villige til å betale til hver motpart. Siden dette er en "prosentverdi", må du være forsiktig med å sette høye verdier for å unngå høye kostnader i CoinJoins med store beløp. Standardverdien for makers er _0,00002_, og jeg anbefaler en tilsvarende eller litt høyere verdi.
- `minimum_makers` er feltet som spesifiserer hvor mange andre motparter vi gjør CoinJoin med, som standard velger joinMarket alltid mellom 4 og 9 motparter, men hvis vi vil ha mer privatliv, kan vi øke denne verdien til 5 eller 6 (det vil imidlertid gjøre transaksjonene dyrere).
- `cjfee_a` spesifiserer, i tilfelle vi opptrer som produsent, hvor mange Sats i absolutte termer vi ønsker å samle inn for å leie ut likviditeten vår. Dette feltet er helt subjektivt, standardverdien er allerede veldig bra (vi vil dermed ha bedre personvern som produsent), men vi kan vurdere å sette den til 0 hvis vi ønsker å tjene mer CoinJoin på kortere tid.
- `cjfee_r` samme som feltet ovenfor, men i prosent og ikke absolutt. Igjen anbefaler jeg å beholde standardverdien eller senke den for å tiltrekke seg flere kjøpere.
- `ordertype` med dette feltet velger vi fra produsenten om vi skal kreve absolutt (absoffer) eller prosent (reloffer). Vanligvis foretrekker takere absolutte bud for økonomiske spørsmål.
- `minsize` hvis vi som produsent ikke ønsker å ha UTXO for liten, kan vi angi minimum CoinJoin for å delta. Dette feltet uttrykkes i Satoshi og er helt subjektivt. Vi kan la dette feltet stå på 0 eller øke til 500000 (Sats), 1000000 (Sats), og så videre.



Vær veldig forsiktig så du ikke redigerer feil felter, noen av variablene i joinmarket.cfg-filen kan kompromittere funksjonaliteten til programvaren eller fullstendig ødelegge personvernet ditt, så hold øynene åpne og vær forsiktig!



## Oppsett av arbeidsmiljø



Noen noder angir automatisk de riktige verdiene for disse feltene i joinmarket.cfg-filen, men jeg anbefaler at du sjekker dem manuelt:





- rpc_user = dittbrukernavn-som-i-Bitcoin.conf
- rpc_password = ditt passord-som-i-Bitcoin.conf
- `rpc_host = localhost #standard vanligvis riktig`
- rpc_port = 8332 # standard for Mainnet



Nå kan vi gå videre med opprettelsen av Wallet i JoinMarket:



```bash
python wallet-tool.py generate
```



Denne kommandoen vil få oss til å skrive inn et passord som vi vil kryptere Wallet med og navnet vi vil gi det, når det spør deg om du vil støtte troskapsobligasjoner eller ikke, anbefaler jeg å bruke alternativet _yes_, utdataene som returneres vil se slik ut:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


hvis det vises en feil, er det mest sannsynlig at vi har angitt feil i de 4 RPC-feltene som er angitt ovenfor. I tilfelle det kan hjelpe å følge [denne veiledningen] (https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) som du finner i den opprinnelige JoinMarket-dokumentasjonen.



Vi har nå fullført oppsettet av arbeidsmiljøet vårt og kan begynne å utforske de kommandoene som vil være mest nyttige for oss. Alle skriptene vi skal snakke om, kan startes i konsollen etterfulgt av `--help` for en grundig forklaring.



Vi kan nå prøve å starte:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



denne kommandoen vil vise deg alle de forskjellige Wallet-miksdybdene med de forskjellige adressene kategorisert som:




- Ny (Address aldri brukt)
- Change-out (rest av en tidligere transaksjon)
- Cj-out (utgang fra en CoinJoin)



her er et praktisk eksempel på resultatet:



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


Nå kan vi fortsette å sette inn våre første Satoshis på en eller flere adresser, og huske at uansett hvem som lager eller tar dem, vil programvaren aldri gå og konsolidere UTXO i forskjellige mixdybder direkte, på denne måten kan vi holde Satss med forskjellige nivåer av personvern atskilt innenfor Wallet.



## Sende Bitcoin med CoinJoin Single



Nå kan vi flytte Satoshiene våre. En av hovedkommandoene i denne programvaren er skriptet:



```bash
pyhton sendpayment.py
```


som gjør det mulig for oss å sende transaksjoner til andre adresser med eller uten CoinJoin. La oss gå gjennom hvordan det fungerer og noen praktiske eksempler. Som standard er formateringen av kommandoen (husk å erstatte teksten som er omsluttet av symbolene < og >):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



et grunnleggende eksempel på bruk kan være:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


i dette tilfellet skal vi sende til Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc, dvs. 5000000 Satoshi fra vår mixdepth 0 (standard) ved å velge mellom 4 til 9 motparter for CoinJoin (standardalternativ).



For å få mer kontroll over hvordan og hvilke UTXO-er som skal brukes, kan vi gå gjennom tilleggsalternativene til denne kommandoen:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


i dette eksemplet har vi lagt til to spesifikasjoner: -N angir hvor mange motparter vi skal mikse med, -m m miksdybden som vi skal ta ut midler fra. Vi har faktisk sendt 100 000 000 Sats (1 btc) til Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c med midlene i mixdybde 1 og miksing med 5 motparter.



Hvis vi angir 0 som send-verdi ved å spesifisere en mixdybde, vil joinMarket utføre en såkalt `sweep`, det vil si at den vil sende alle fondene i denne mixdybden ved å slå dem sammen med hverandre:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



her sendte vi alle midlene fra mixdepth 0 (vi kunne ikke ha spesifisert det fordi det er standard) og blandet med 7 motparter.



Kommandoen sendpayment brukes til å flytte penger fra joinMarket til eksterne Wallet eller til å sende Satoshi til en person ved å legge til en Layer av personvern mellom oss og vedkommende. For å oppnå et tilstrekkelig nivå av personvern på UTXO-ene våre er det mer hensiktsmessig å bruke tumbler.py-kommandoen, som vi vil forklare senere i denne veiledningen.



## Å være en skaper



Skriptet vi skal gå gjennom i denne delen, er



```bash
yg-privacyenhanced.py
```



Dette programmet brukes til å fungere som en maker i joinMarket. Programvaren vil koble seg til Bitcoin-noden vår og til den interne markedsplassen på plattformen der beslutningstakerne presenterer seg som likviditetsbudgivere og takere ser etter motparter. Hvis du ønsker å bruke en troskapsobligasjon, kan du opprette en med denne formateringen:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



for eksempel:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



utskriften som vil bli returnert til oss vil være en Bitcoin Address (dvs. den du må sette inn midlene du ønsker å allokere til troskap).



**Forsiktighetsregler**: Det er to ting du må være nøye med hvis du skal opprette en Fidelity Bond (også kjent som FB);





- når midlene er satt inn, kan de ikke flyttes igjen før den utløper. Vær oppmerksom på hvor mange Satss du sender til Address, og hvordan du formaterer datoen. Feil er ikke tillatt!
- Troskapsobligasjonen er lett gjenkjennelig på kjeden, så det anbefales å sette inn penger gjennom en CoinJoin og med en opprinnelse som ikke er relatert til identiteten din. Det samme er også tilrådelig å gjøre når du ønsker å flytte den utløpte troskapsobligasjonen ut av JoinMarket.



Det er viktig å huske at det er mulig å laste opp troskapsobligasjonen med bare én transaksjon, i tilfelle UTXO flere ganger vil bare den største anses som gyldig for FB.



La oss nå ta for oss skriptet som ble nevnt i begynnelsen av dette avsnittet, når vi har opprettet troskapsobligasjonen (som vi husker er valgfri), er vi klare til å kjøre den kjørbare filen for å fungere som en maker på joinMarket. Når satssene er deponert på de forskjellige adressene og mixdepth, kan vi kjøre kommandoen:



```bash
python yg-privacyenhanced.py <wallet name>
```



Fra dette tidspunktet (etter noen minutter med tilkobling til nettverket) og frem til vi stopper skriptet, vil JoinMarket-klienten vår vises på listen over aktive beslutningstakere på protokollen og tilby likviditeten vår til ulike motparter for å gjøre CoinJoin. Ikke forvent dusinvis av CoinJoins per dag (med mindre du har stor fidlity og stor likviditet deponert på Wallet), husk også at faktorer som gebyrer som kreves og Satoshis deponert påvirker hvor ofte du vil være en maker.



Ved å kjøre kommandoen nedenfor vil du kunne se historikken til alle transaksjonene som er gjort på Wallet og eventuelle gevinster (hvis du er en maker) eller gebyrutgifter (hvis du er en taker) du har hatt i løpet av Wallets levetid.



```bash
python wallet-tool.py <wallet name> history
```



Når Satoshiene dine lager CoinJoins, vil de bevege seg fra mixdybde til mixdybde til de når den siste. Når de har passert den fjerde, vil de gå tilbake til mixdybde 0. Det er opp til deg hvor mye privatliv du vil ha før du flytter dem til en Cold Wallet, og det anbefales å fullføre en full Wallet syklus.



## Tumbler



Her er vi endelig på den saftigste delen av JoinMarket, tumbler! Hvis du har lyttet til podcasten vet du allerede hva dette handler om. En anbefaling før vi kommer i gang: **Husk å sette grensene i joinmarket.cfg-filen (som forklart i begynnelsen), og vurder å kjøre programmet bare når onchain-gebyrene er relativt lave (under 10 Sats/vB).



For å starte tumbleren er det nødvendig å ha stoppet skriptet fra maker (hvis det var aktivt), etter det kan vi kjøre kommandoen:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Det er viktig å angi **mindst** 3 utgangsadresser for tumbleren: dette er for å sikre godt personvern og for ikke å skape åpenbare koblinger mellom UTXOer i løpet av prosessen. Som vanlig kan du legge til `--help` i kommandoen for å se alle tilleggsdetaljene. La oss gå til et mer komplekst eksempel med avanserte regler:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



I dette tilfellet har vi lansert et tumbling-skript som ikke vil bruke standard antall motparter (parameteren -N indikerer at vi trenger 7 motparter med en maksimal varians på 2, så et tilfeldig antall produsenter fra 5 til 9) og med et større antall CoinJoin per blandingsdybde (som standard lager dette skriptet et tilfeldig antall CoinJoin per seksjon av Wallet som strekker seg fra 1 til 3, ved å bruke kommandoen -c 3 1 i stedet blir det fra 2 til 4). På denne måten vil vi bruke mer Sats i avgifter, men ha et større anonymitetssett.



Du kan også legge til så mange utgangsadresser du vil (minimum 3, det finnes ikke noe maksimum annet enn sunn fornuft). Av personvernhensyn er det imidlertid ikke mulig å bestemme hvordan Satoshi skal fordeles mellom adressene som er angitt som utdata.



Tumbler er en bevisst lang prosess, og av og til kan det skje at noe slutter å fungere, i de fleste tilfeller vil dette løse seg selv i løpet av noen timer. I tilfelle en total krasj kan vi forsøke å starte den på nytt med kommandoen:



```bash
python tumbler.py --restart
```



Eller bare start en ny trommelkommando på nytt. Dette vil ikke starte planleggingen av den forrige tumbleren, men vil starte en ny blandingssyklus. Hvis SSH-terminalen til noden din også stopper skriptet, kan du dra nytte av programmet `TMUX` som kan installeres med kommandoen:



```bash
sudo apt install tmux
```



Hvis du starter den fra skallet ved å skrive `tmux`, åpnes en terminal for deg som forblir aktiv i bakgrunnen selv om du lukker fjerntilkoblingen. Når du kobler deg til noden på nytt med kommandoen `tmux attach`, åpnes skallet som var aktivt i bakgrunnen på nytt.



## Konklusjon



JoinMarket er grenseløs og tilpassbar programvare. I denne guiden har vi oppdaget de viktigste funksjonene slik at det er mulig for alle (eller i det minste jeg har prøvd, jeg innser at ved hjelp av denne programvaren er ikke en tur i parken) for å bruke den. Et av de største problemene med JoinMarket er nettopp det: antall personer som bruker det og å være en maker. Hvis få brukere dra nytte av denne programvaren, den generelle personvern (anon-set) er senket. Derfor håper jeg at denne guiden vil stimulere til bruk og overbevise deg om å laste ned og installere favorittprogramvaren min for å lage CoinJoin. I tilfelle du vil gå enda dypere inn i noen aspekter, anbefaler jeg deg å lese de forskjellige dybdedokumentene på github, de er veldig godt utført, og du finner dem her.



God miksing av skilpadder! 🐢 💚



[Her](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) kan du støtte Turtlecute