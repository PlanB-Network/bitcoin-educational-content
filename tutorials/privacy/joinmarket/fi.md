---
name: JoinMarket

description: Opas ja opetusohjelma siitä, miten JoinMarketia käytetään CoinJoin:n tekemiseen Bitcoin:n yli komentorivin kautta
---

![cover](assets/cover.webp)



---

Jos löysit tämän sivun etsimällä verkossa "JoinTmarket" sinulla on vilpitön arvostukseni. Olet kuitenkin törmännyt oppaaseen, joka käsittelee täysin erilaista, mutta erittäin mielenkiintoista aihetta! 🚬🍁



Tämän opetusohjelman tavoitteena on havainnollistaa JoinMarketin teoreettista ja käytännön toimintaa komentorivin kautta. 🐢 💚



## JoinMarket Teoreettinen määritelmä



Voimme määritellä JoinMarketin työkaluksi tai Wallet:ksi, joka mahdollistaa CoinJoin:n käytön muiden käyttäjien kanssa täysin Trustless:lla tavalla ja ilman keskitettyä koordinaattoria.



Koska koko tämän työkalun teoreettinen osa on erittäin laaja, päätin käsitellä sitä podcastini erityisessä jaksossa. Niille, jotka ymmärtävät italiaa, suosittelen lämpimästi jatkamaan lukemista jakson kuuntelemisen jälkeen, jotta voit omaksua paremmin peruskäsitteet tämän ohjelman käyttämiseksi oikein.



Voit katsoa jakson näistä suorista linkeistä:




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (tästä voit kuunnella sen suoraan selaimesta).
- [Antenna pod](https://antennapod.org/) on ilmainen ja avoimen lähdekoodin podcast-hallintaohjelma, joka ei vaadi rekisteröitymistä. Löytääksesi jakson lataa sovellus, lisää podcastini manuaalisesti liittämällä [tämä linkki](https://Anchor.fm/s/bd5d5b20/podcast/rss) _feed rss_ -osioon ja etsi sitten JoinMarketille omistettu jakso.



## Asennus



Käyttöjärjestelmät:





- Raspiblitz
- Sateenvarjo
- MyNode
- Raspibolt



## Määritystiedostot



JoinMarket on muokattavissa oleva ohjelmisto, jossa on ääretön määrä asetuksia; nämä asetukset määritetään ohjelman päähakemistossa sijaitsevassa konfigurointitiedostossa nimeltä `Joinmarket.cfg`.



Tässä osiossa käymme läpi joitakin kenttiä, joiden tutkiminen ja/tai muokkaaminen voi olla mielenkiintoista tarpeidesi mukaan. Haluan korostaa, että kaikki alla luetellut muutokset on hyödyllistä tietää, jotta ohjelmiston toiminta voidaan mukauttaa henkilökohtaisiin tarpeisiin, mutta ne eivät ole pakollisia.



Siirry ensin `joinmarket/scripts`-kansioon ja suorita komento:



```bash
python wallet-tool.py generate
```


Tässä vaiheessa pitäisi tulla virheilmoitus, mutta se aiheuttaa sen, että ohjelmisto käyttää generate:aa, joka on esiasetettu asetustiedosto. Voimme mennä muokkaamaan asetustiedostoa päätelaitteesta seuraavasti:



```bash
nano joinmarket.cfg
```



tai:



```bash
vim joinmarket.cfg
```



kun se on avattu, huomaamme lukuisia rivejä, joissa on erilaisia asetuksia ja niiden selitykset englanniksi. Seuraavassa analysoidaan erityisesti mielenkiintoisimpia muuttujia:





- `merge_algorithm` jos teemme niin kuin valmistaja tämä kenttä säätää, kuinka aggressiivisesti ohjelmisto yhdistää käyttämättömät tuotokset. Jos yhdistettäviä UTXO:ita on paljon, voi olla järkevää vaihtaa _gradual_:sta _greedy_:hen
- `tx_fees` säätää ottajana maksut, joilla maksetaan tapahtuma, on erittäin hyödyllistä muuttaa tätä asetusta, jos käytät peukaloa usein (puhumme tästä myöhemmin), koska jos maksujen piikki on jälkimmäisen suorittamisen aikana, jos emme aseta tätä kenttää oikein, vaarana on, että käytämme paljon Sats CoinJoin: lle. Asettamalla arvot tuhansina (esimerkiksi 2000) tämä vastaa 2 Sats/vBytes, 3500 vastaa 3,5 Sats/vBytes ja niin edelleen. Suosittelisin lukua, joka vaihtelee 1500:sta 6000:een tarpeidesi mukaan.
- `max_cj_fee_abs`:n avulla määritetään, kuinka paljon olemme valmiita maksamaan absoluuttisesti valmistajista, jotka valitsemme CoinJoin:n aikana. Oletusarvoisesti tämä kenttä tekijöille on 200 Sats, hyvä vaihtoehto voisi olla luku, joka vaihtelee 200:sta 1000 Sats:een vastapuolta kohden (tämä perustuu siihen, kuinka paljon haluat käyttää ja kuinka paljon anon-settiä haet CoinJoineistasi)
- `max_cj_fee_rel` toimii samalla tavalla kuin edellä mainittu kenttä, mutta sillä määritetään suhteelliset palkkiot (prosentit), jotka olemme valmiita maksamaan kullekin vastapuolelle. Koska kyseessä on `prosenttiarvo`, varo asettamasta korkeita arvoja, jotta vältyt suurilta kustannuksilta CoinJoineissa, joissa on suuria summia. Oletusarvo päättäjille on _0.00002_, suosittelen samanlaista tai hieman korkeampaa arvoa.
- `minimum_makers` on kenttä, joka määrittää, kuinka monen muun vastapuolen kanssa teemme CoinJoin:n. Oletusarvoisesti joinMarket valitsee aina 4-9 vastapuolta, mutta halutessamme voimme nostaa tämän arvon 5:een tai 6:een, jos haluamme lisää yksityisyyttä (se tekee transaktioista kuitenkin kalliimpia).
- `cjfee_a` määrittää, jos toimimme päättäjänä, kuinka monta Sats:tä absoluuttisesti ilmaistuna haluamme periä likviditeettimme vuokraamisesta. Tämä kenttä on täysin subjektiivinen, oletusarvo on jo erittäin hyvä (meillä on siten parempi yksityisyys makerina), mutta voimme harkita sen ottamista 0:aan, jos haluamme ansaita enemmän CoinJoin lyhyemmässä ajassa.
- `cjfee_r` sama kuin edellä oleva kenttä, mutta prosentteina eikä absoluuttisesti. Suosittelen jälleen kerran jättämään oletusarvon tai alentamaan sitä, jotta saadaan enemmän ottajia.
- `Tilaustyyppi` Tällä kentällä valitsemme valmistajalta, veloitetaanko ehdottomasti (absoffer) vai prosentuaalisesti (reloffer). Yleensä tarjouksenottajat suosivat absoluuttisia tarjouksia taloudellisissa kysymyksissä.
- `minsize`, jos valmistajana emme halua UTXO:n olevan liian pieni, voimme määritellä vähimmäismäärän CoinJoin, jotta voimme osallistua. Tämä kenttä ilmaistaan Satoshi:nä, ja se on täysin subjektiivinen. Voimme jättää tämän kentän arvoksi 0 tai nostaa sen arvoon 500000 (Sats), 1000000 (Sats) ja niin edelleen.



Ole hyvin varovainen, ettet muokkaa vääriä kenttiä, jotkut joinmarket.cfg-tiedoston muuttujat, jos ne on asetettu väärin, voivat vaarantaa ohjelmiston toiminnallisuuden tai tuhota yksityisyytesi kokonaan, silmät auki ja varovaisuus maksimiin!



## Työympäristön asetukset



Jotkin solmut asettavat automaattisesti oikeat arvot näille kentille joinmarket.cfg-tiedostossa, joten suosittelen tarkistamaan ne uudelleen manuaalisesti:





- `rpc_user = käyttäjätunnuksesi kuten-Bitcoin.conf`
- `rpc_password = yourpassword-as-in-Bitcoin.conf` (rpc_salasana = salasanasi-as-in-Bitcoin.conf)
- `rpc_host = localhost #default yleensä oikein`
- `rpc_port = 8332 # oletusarvo Mainnet:lle`



Tässä vaiheessa voimme jatkaa Wallet:n luomista JoinMarketissa:



```bash
python wallet-tool.py generate
```



Tämä komento antaa meille salasanan, jolla Wallet salataan, ja nimen, jonka haluamme antaa sille, kun se kysyy, haluatko tukea uskollisuusbondeja, suosittelen käyttämään _yes_-vaihtoehtoa, palautettu tuloste näyttää tältä:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


jos virhe tulee näkyviin, on todennäköistä, että olemme asettaneet edellä määritetyt 4 RPC-kenttää väärin. Jos tästä on apua, kannattaa seurata [tätä opasta](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure), joka löytyy alkuperäisestä JoinMarketin dokumentaatiosta.



Olemme saaneet työympäristömme asetukset valmiiksi ja voimme alkaa tutkia meille hyödyllisimpiä komentoja. Kaikki käsikirjoitukset, joista keskustelemme, voidaan käynnistää konsolissa, ja syvällisen selityksen saa valitsemalla `--help`.



Voimme nyt yrittää käynnistää:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



tämä komento näyttää sinulle kaikki eri wallet-sekoitussyvyydet eri osoitteilla, jotka on luokiteltu seuraavasti:




- Uusi (Address ei koskaan käytetty)
- Muutos (edellisen liiketoimen jäännös)
- Cj-out (CoinJoin:n lähtö)



tässä on käytännön esimerkki tuloksesta:



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


Nyt voimme tallettaa ensimmäiset Satoshimme yhteen tai useampaan osoitteeseen muistaen, että riippumatta tekijästä tai vastaanottajasta, ohjelmisto ei koskaan mene konsolidoimaan UTXO:tä suoraan eri sekoitussyvyyksiin, ja näin voimme pitää eri yksityisyystasoilla olevat Satssit erillään Wallet:ssä.



## Bitcoin:n lähettäminen yhdessä CoinJoin:n kanssa Single



Voimme nyt siirtää Satoshit. Yksi tämän ohjelmiston tärkeimmistä komennoista on käsikirjoitus:



```bash
pyhton sendpayment.py
```


jonka avulla voimme lähettää tapahtumia muihin osoitteisiin CoinJoin:n kanssa tai ilman. Käydään läpi, miten se toimii ja joitakin käytännön esimerkkejä. Oletusarvoisesti komennon muotoilu on (muista korvata symboleilla < ja > ympäröity teksti):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



peruskäyttöesimerkki voisi olla:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


tässä tapauksessa aiomme lähettää osoitteeseen 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc eli 5000000 Satoshi meidän mixdepth 0 (oletusarvoisesti) menemällä valita 4-9 vastinetta CoinJoin (oletusarvoisesti).



Jos haluat hallita paremmin sitä, miten ja mitä UTXO:ta käytetään, voimme tarkastella tämän komennon lisäasetuksia:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


tässä esimerkissä olemme lisänneet kaksi määrittelyä: --m mixdepth, josta aiomme nostaa varoja. Itse asiassa olemme lähettäneet 100 000 000 Sats (1 btc) osoitteeseen 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c, jossa varat ovat sekoitussyvyydessä 1 ja sekoitamme ne 5 vastapuolen kanssa.



Jos asetamme lähetysarvoksi 0 määrittelemällä sekoitussyvyyden, joinMarket suorittaa niin sanotun "pyyhkäisyn", eli se lähettää kaikki kyseiseen sekoitussyvyyteen kuuluvat varat yhdistämällä ne toisiinsa:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



tässä tapauksessa lähetimme kaikki varat sekoitussyvyydestä 0 (emme olisi voineet määrittää sitä, koska se on oletusarvo) sekoittaen ne 7 vastapuolen kanssa.



Komennolla sendpayment siirretään varoja joinMarketista ulkoiseen Wallet:aan tai lähetetään Satoshi henkilölle lisäämällä Layer yksityisyyden suoja meidän ja hänen välillemme. Saadaksemme riittävän yksityisyyden tason UTXO:llemme on tarkoituksenmukaisempaa käyttää tumbler.py-komentoa, josta kerromme myöhemmin tässä oppaassa.



## Tekijänä oleminen



Käsikirjoitus, jota käsittelemme tässä jaksossa, on:



```bash
yg-privacyenhanced.py
```



Tätä ohjelmaa käytetään toimimaan päättäjänä joinMarketissa. Ohjelmisto muodostaa yhteyden Bitcoin-solmuun ja alustan sisäiseen markkinapaikkaan, jossa päättäjät esittäytyvät likviditeettitarjoajina ja ottajat etsivät vastapuolia. Jos haluat käyttää uskollisuusvelkakirjaa, voit luoda sellaisen tällä muotoilulla:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



esimerkiksi:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



tuloste, joka palautetaan meille, on Bitcoin-osoite (eli osoite, johon sinun on talletettava varat, jotka haluat osoittaa Fidelitylle).



**Varoitus**: Jos aiot luoda Fidelity Bondin (eli FB:n), sinun on kiinnitettävä huomiota kahteen asiaan;





- kun varat on talletettu, niitä ei voi siirtää uudelleen ennen sen voimassaolon päättymistä. Kiinnitä huomiota siihen, kuinka monta Satss lähetät osoitteeseen ja miten muotoilet päivämäärän. Virheitä ei sallita!
- Luottovelkakirjalaina on helposti tunnistettavissa ketjussa, joten on suositeltavaa tallettaa varoja CoinJoin:n kautta ja henkilöllisyydestäsi riippumattomalla alkuperällä. Sama kannattaa tehdä myös silloin, kun haluat siirtää vanhentuneen fidelity bondin pois JoinMarketista.



On tärkeää muistaa, että uskollisuusobligaatio on mahdollista ladata uudelleen vain yhdellä tapahtumalla, jos UTXO:n kertoja on useampia, vain suurin niistä katsotaan FB:lle kelvolliseksi.



Käsittelemme nyt tämän kappaleen alussa mainittua skriptiä, kun olemme luoneet uskollisuusjoukkolainan (jonka muistamme olevan valinnainen), olemme valmiita suorittamaan suoritettavan ohjelman toimimaan päättäjänä joinMarketissa. Kun Satss on talletettu eri osoitteisiin ja mixdepth voimme ajaa komennon:



```bash
python yg-privacyenhanced.py <wallet name>
```



Tästä lähtien (muutaman minuutin kuluttua verkkoyhteyden muodostamisesta) ja kunnes lopetamme skriptin, JoinMarket-asiakas näkyy protokollan aktiivisten päättäjien luettelossa ja tarjoaa likviditeettiä eri vastapuolille CoinJoin:n tekemistä varten. Älä odota kymmeniä CoinJoins päivässä (ellei sinulla ole valtava fidlity ja suuri likviditeetti talletettu Wallet), myös muistaa, että tekijät, kuten vaaditut palkkiot ja Satoshis talletettu vaikuttaa siihen, kuinka usein olet maker.



Suorittamalla alla olevan komennon näet kaikkien Wallet:lla tehtyjen transaktioiden historian ja kaikki voitot (jos olet tekijä) tai kulut (jos olet ottaja), joita sinulla on ollut wallet:n elinkaaren aikana.



```bash
python wallet-tool.py <wallet name> history
```



Kun Satoshisi tekevät CoinJoineja, ne siirtyvät sekoitussyvyydestä toiseen, kunnes ne saavuttavat viimeisen sekoitussyvyyden. Kun ne ovat ohittaneet neljännen, ne palaavat mixdepth 0:aan, on sinusta kiinni, kuinka paljon yksityisyyttä haluat saada ennen kuin siirrät ne Cold Wallet:aan, on suositeltavaa lopettaa koko Wallet-sykli.



## Tumbler



Olemme vihdoin JoinMarketin mehukkaimmassa osassa, tumblerissa! Jos olet kuunnellut podcastia, tiedät jo mistä tässä on kyse. Yksi suositus ennen kuin aloitamme: **Muista asettaa rajat joinmarket.cfg-tiedostossa (kuten alussa selitettiin) ja harkitse ohjelman käyttämistä vain silloin, kun onchain-maksut ovat suhteellisen alhaiset (alle 10 Sats/vB).



Käynnistää peukalo on tarpeen pysäyttää skripti maker (jos se oli aktiivinen), jonka jälkeen voimme suorittaa komennon:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



On tärkeää syöttää **vähintään** kolme lähtöosoitetta tumbleria varten: näin varmistetaan hyvä yksityisyys ja estetään UTXO:iden välisten ilmeisten yhteyksien luominen prosessin aikana. Kuten tavallista, lisäämällä komentoon `--help` voit nähdä kaikki lisätiedot. Mennään katsomaan monimutkaisempaa esimerkkiä, jossa on kehittyneitä sääntöjä:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



Tässä tapauksessa olemme käynnistäneet tumbling-skriptin, joka ei käytä oletusarvoista vastineiden lukumäärää (-N-parametri osoittaa, että tarvitsemme 7 vastinetta, joiden maksimihajonta on 2, joten satunnainen määrä tekijöitä 5-9) ja suurempi määrä CoinJoin:tä sekoitussyvyyttä kohti (oletusarvoisesti tämä skripti tekee satunnaisen määrän CoinJoin:tä Wallet:n jaksoa kohti, joka vaihtelee välillä 1-3, kun sen sijaan käytetään komentoa -c 3 1, se on 2:sta 4:ään). Tällä tavoin käytämme enemmän Sats-maksuja, mutta saamme suuremman anonymiteettisarjan.



Voit myös lisätä niin monta lähtöosoitetta kuin haluat (vähintään 3, maksimi on vain maalaisjärki). Yksityisyyden suojaan liittyvistä syistä ei kuitenkaan ole mahdollista päättää, miten Satoshi jaetaan lähtöosoitteiksi määritettyjen osoitteiden kesken.



Tumbler on tarkoituksellisen pitkä prosessi, ja joskus voi käydä niin, että jokin asia lakkaa toimimasta, mutta useimmissa tapauksissa tämä korjaantuu muutamassa tunnissa. Täydellisen kaatumisen sattuessa voimme yrittää käynnistää sen uudelleen komennolla:



```bash
python tumbler.py --restart
```



Tai yksinkertaisesti käynnistä uusi tumbling-komento. Tämä ei käynnistä edellisen tumblerin aikataulutusta, vaan aloittaa uuden sekoitussyklin. Jos myös solmun SSH-päätteen sulkeminen pysäyttää skriptin, voit hyödyntää komennolla asennettavaa `TMUX`-ohjelmaa:



```bash
sudo apt install tmux
```



Käynnistämällä sen komentotulkista kirjoittamalla `tmux` avautuu sinulle terminaali, joka pysyy aktiivisena taustalla, vaikka suljet etäyhteyden. Kun otat uudelleen yhteyden solmuun komennolla: `tmux attach`, avaat uudelleen komentotulkin, joka pysyi aktiivisena taustalla.



## Päätelmä



JoinMarket on rajaton ja muokattavissa oleva ohjelmisto. Tässä oppaassa olemme löytäneet tärkeimmät toiminnot, jotta kuka tahansa (tai ainakin minä olen yrittänyt, ymmärrän, että tämän ohjelmiston käyttäminen ei ole mikään kävelymatka) voi käyttää sitä. Yksi JoinMarketin suurimmista ongelmista on juuri se: sitä käyttävien ihmisten määrä ja tekijänä oleminen. Jos harvat käyttäjät käyttävät tätä ohjelmistoa hyväkseen, yleinen yksityisyys (anon-set) laskee. Siksi toivon, että tämä opas kannustaa käyttöön ja vakuuttaa sinut lataamaan ja asentamaan suosikkiohjelmistoni CoinJoin:n tekemiseen. Jos haluat mennä vielä syvemmälle joihinkin näkökohtiin, suosittelen sinua lukemaan githubissa olevat erilaiset syvälliset dokumentit, ne ovat hyvin tehtyjä ja löydät ne täältä.



Iloista kilpikonnien sekoittamista!🐢 💚 💚



[Täällä](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) voit tukea Turtlecutea!