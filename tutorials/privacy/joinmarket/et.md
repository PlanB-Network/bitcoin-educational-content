---
name: JoinMarket

description: Juhend ja õpetus selle kohta, kuidas kasutada JoinMarketit, et teha CoinJoin üle Bitcoin käsurea kaudu
---

![cover](assets/cover.webp)



---

Kui leidsite selle lehekülje otsides internetis "JoinTmarket", siis on teil minu siiras tänu. Olete aga sattunud juhendile, mis käsitleb täiesti erinevat, kuid äärmiselt huvitavat teemat! 🚬🍁



Selle õpetuse eesmärk on illustreerida JoinMarketi teoreetilist ja praktilist toimimist käsurea kaudu. 🐢 💚



## JoinMarket Teoreetiline määratlus



Me võime määratleda JoinMarketit kui vahendit ehk Wallet, mis võimaldab CoinJoin koos teiste kasutajatega täielikult Trustless viisil ja ilma keskse koordinaatorita.



Kuna kogu selle tööriista teoreetiline osa on äärmiselt lai, otsustasin Address seda oma podcasti eraldi episoodis käsitleda. Neile, kes saavad itaalia keelest aru, soovitan pärast episoodi kuulamist jätkata lugemist, et paremini omaks võtta põhimõisted selle programmi õigeks kasutamiseks.



Saate selle episoodiga tutvuda nende otselinkide kaudu:




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (siin saate seda otse brauserist kuulata).
- [Antenna pod](https://antennapod.org/) on tasuta ja avatud lähtekoodiga podcastide haldur, mis ei nõua registreerimist. Episoodi leidmiseks laadige rakendus alla, lisage käsitsi minu podcast, sisestades [see link](https://Anchor.fm/s/bd5d5b20/podcast/rss) _feed rss_ sektsiooni, seejärel otsige JoinMarketile pühendatud episoodi.



## Paigaldamine



Operatsioonisüsteemid:





- Raspiblitz
- Vihmavarju
- MyNode
- Raspibolt



## Konfiguratsioonifailid



JoinMarket on kohandatav tarkvara, millel on lõputu hulk seadistusi; need seadistused on määratud programmi põhikataloogis asuvas konfiguratsioonifailis nimega `Joinmarket.cfg`.



Selles jaotises vaatame läbi mõned väljad, mida on huvitav uurida ja/või muuta, sõltuvalt teie vajadustest. Tahaksin rõhutada, et kõiki allpool loetletud muudatusi on kasulik teada, et kohandada tarkvara toimimist isiklike vajadustega, samas ei ole need kohustuslikud.



Kõigepealt liigume kausta `joinmarket/scripts` ja käivitame käsu:



```bash
python wallet-tool.py generate
```


Siinkohal peaksime saama veateate, kuid see põhjustab tarkvara generate eelseadistuste faili meie jaoks. Me võime minna ja muuta seadistusfaili terminalist koos:



```bash
nano joinmarket.cfg
```



või:



```bash
vim joinmarket.cfg
```



avades märkame arvukaid ridu erinevate seadete ja nende selgitustega inglise keeles. Täpsemalt analüüsime allpool kõige huvitavamaid muutujaid:





- `merge_algorithm` juhul, kui me teeme nagu tegija see väli reguleerib, kuidas agressiivselt tarkvara konsolideerib kasutamata väljundid. Juhul, kui meil on palju UTXOsid, mida konsolideerida, võib olla mõistlik lülitada _gradual_lt _greedy_le_
- `tx_fees` reguleerib kui võtja tasud, millega maksta tehingu, see on väga kasulik muuta seda seadistust juhul, kui te kasutate tumbler sageli (me räägime sellest hiljem), sest kui on piik tasud täitmise ajal viimane, kui me ei ole seadistatud see väli õigesti, me riskime läheb kulutada palju Sats CoinJoin. Määrates väärtused tuhandetes (näiteks 2000), võrdub see 2 Sats/vBytes, 3500 3,5 Sats/vBytes jne. Ma soovitaksin arvu vahemikus 1500 kuni 6000, sõltuvalt teie vajadustest.
- `max_cj_fee_abs` kasutatakse selleks, et määrata, kui palju me oleme valmis maksma absoluutarvudes tootjate eest, kelle me CoinJoin ajal valime. Vaikimisi on see väli tegijate jaoks 200 Sats, hea valik võiks olla number vahemikus 200 kuni 1000 Sats ühe vastaspoole kohta (see põhineb sellel, kui palju sa tahad kulutada ja kui palju anon-set sa soovid oma CoinJoins'i eest)
- `max_cj_fee_rel` on sama funktsioon nagu eespool nimetatud väljal, kuid määrab suhtelised tasud (protsendid), mida me oleme valmis igale vastaspoolele maksma. Kuna tegemist on `protsendilise` väärtusega, siis olge ettevaatlik, et mitte määrata suuri väärtusi, et vältida suuri kulusid suurte summadega CoinJoins'is. Makerite vaikeväärtus on _0.00002_, soovitan sarnast või veidi kõrgemat väärtust.
- `minimum_makers` on väli, mis määrab, kui paljude teiste vastaspooltega me CoinJoin teeme, vaikimisi valib joinMarket alati 4 kuni 9 vastaspoolt, kui me tahame, et suurendada privaatsust, võime tõsta seda väärtust 5 või 6 (see muudab tehingud kallimaks).
- `cjfee_a` määrab, kui me tegutseme tootjana, mitu Sats absoluutarvudes me tahame koguda oma likviidsuse rentimise eest. See väli on täiesti subjektiivne, vaikimisi väärtus on juba väga hea (meil on seega parem privaatsus makerina), me võime kaaluda selle võtmist 0-le, kui tahame teenida rohkem CoinJoin vähemal ajal.
- `cjfee_r` sama nagu eespool nimetatud väli, kuid protsentides ja mitte absoluutsetes väärtustes. Jällegi soovitan jätta vaikimisi väärtus või alandada seda, et meelitada rohkem soovijaid.
- `Tellimuse tüüp` selle väljaga valime tegijalt, kas küsida absoluutselt (absoffer) või protsentuaalselt (reloffer). Tavaliselt eelistavad võtjad majanduslike küsimuste puhul absoluutseid pakkumisi.
- `minsize`, kui me ei taha, et UTXO oleks liiga väike, siis võime määrata minimaalse CoinJoin osalemiseks. See väli on väljendatud Satoshi ja on täiesti subjektiivne. Me võime jätta selle välja 0-ks või suurendada seda 500000-ni (Sats), 1000000-ni (Sats) jne.



Olge väga ettevaatlik, et mitte muuta valesid välju, mõned varibles in joinmarket.cfg faili, kui valesti seatud võib ohustada funktsionaalsust tarkvara või täielikult hävitada oma privaatsust, silmad lahti ja ettevaatust kuni maksimumini!



## Töökeskkonna seadistamine



Mõned sõlmed seavad automaatselt õiged väärtused nendele väljadele joinmarket.cfg failis, mida soovitan käsitsi uuesti kontrollida:





- `rpc_user = sinu kasutajanimi nagu-Bitcoin.conf`
- `rpc_password = yourpassword-as-in-Bitcoin.conf`
- `rpc_host = localhost #default tavaliselt õige`
- `rpc_port = 8332 # vaikimisi Mainnet jaoks`



Siinkohal võime jätkata Wallet loomist JoinMarketis:



```bash
python wallet-tool.py generate
```



See käsk laseb meil sisestada salasõna, millega Wallet krüpteerida ja nime, mille me tahame anda, kui ta küsib, kas soovite toetada fidelity bond'i või mitte, soovitan kasutada valikut _yes_, tagastatav väljund näeb välja selline:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


kui ilmneb viga, siis tõenäoliselt oleme eespool nimetatud 4 RPC välja valesti seadistanud. Juhul, kui sellest võib olla abi, siis järgige [seda juhendit](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure), mis leiate JoinMarket'i algdokumentatsioonist.



Oleme lõpetanud oma töökeskkonna seadistamise ja saame hakata uurima käske, mis on meile kõige kasulikumad. Kõik skriptid, mida me arutame, saab käivitada konsoolis, millele järgneb `--help` põhjalikuks selgituseks.



Nüüd võime proovida käivitada:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



see käsk näitab teile kõiki erinevaid portfelli segusügavusi erinevate aadressidega, mis on kategoriseeritud järgmiselt:




- Uus (Address ei ole kunagi kasutatud)
- Väljavahetus (eelmise tehingu jääk)
- Cj-out (CoinJoin väljund)



siin on praktiline näide tulemuse kohta:



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


Nüüd saame jätkata oma esimese Satoshis hoiule ühe või mitme aadressi sees, pidades meeles, et olenemata tegija või vastuvõtja, tarkvara ei lähe kunagi ja konsolideerida UTXO eri mixdepths otse, sel viisil saame hoida Satss erineva privaatsustasemega eraldi Wallet sees.



## Bitcoin saatmine koos CoinJoin Single



Nüüd saame oma Satoshit liigutada. Üks peamisi käske selles tarkvaras on skript:



```bash
pyhton sendpayment.py
```


mis võimaldab meil saata tehinguid teistele aadressidele CoinJoin-ga või ilma. Vaatame üle, kuidas see toimib ja mõned praktilised näited. Vaikimisi on käsu vorming järgmine (ärge unustage asendada sümbolitega < ja > ümbritsetud teksti):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



põhiline näide kasutamise kohta võiks olla:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


sel juhul saadame Address-le 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc ehk 5000000 Satoshi meie mixdepth 0 (vaikimisi), valides 4 kuni 9 vastast CoinJoin jaoks (vaikimisi valik).



Et rohkem kontrollida, kuidas ja milliseid UTXO-sid kulutada, võime vaadata üle selle käsu lisavõimalused:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


selles näites oleme lisanud kaks spetsifikatsiooni: -N näitab, kui paljude vastaspooltega me kavatseme segada, -m segamissügavus, millest me kavatseme raha välja võtta. Tegelikult oleme saatnud 100 000 000 Sats (1 btc) Address-le 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c koos vahenditega mixdepth 1 ja segades 5 vastaspoolega.



Kui me paneme saateväärtuseks 0, määrates mixdepth, teeb joinMarket nn `sweep`, st ta saadab kõik selles mixdepth'is olevad vahendid, konsolideerides need omavahel:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



siin me saatsime kõik vahendid mixdepth 0 (me ei oleks võinud seda määrata, sest see on vaikimisi) segamine 7 vastaspoolega.



Käsku sendpayment kasutatakse raha liigutamiseks joinMarketist välisesse Wallet või Satoshi saatmiseks isikule, lisades Layer privaatsuse meie ja tema vahele. Meie UTXOs piisava privaatsuse saavutamiseks on sobivam kasutada käsku tumbler.py, mida selgitame hiljem selles juhendis.



## Olles tegija



Skript, mida me selles osas käsitleme, on järgmine:



```bash
yg-privacyenhanced.py
```



Seda programmi kasutatakse joinMarketis tegijana. Tarkvara ühendab meie Bitcoin sõlme ja platvormi sisemise turuga, kus tegijad esitlevad end likviidsuse pakkujatena ja võtjad otsivad vastaspoolt. Juhul, kui soovite kasutada truuduslike võlakirju, saate selle vormingu abil luua sellise võlakirja:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



näiteks:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



väljund, mis meile tagastatakse, on Bitcoin Address (st see, millele te peate fidelityle eraldatavad vahendid hoiule andma).



**Ohutus**: Kui kavatsete luua Fidelity Bond'i (a.k.a. FB), tuleb pöörata tähelepanu kahele asjaolule;





- kui raha on hoiule antud, ei saa seda enne selle kehtivuse lõppemist uuesti liigutada. Pöörake tähelepanu sellele, kui palju Satss te Address-le saadate ja kuidas te kuupäeva vormistate. Vead ei ole lubatud!
- Usaldusvõlakiri on kergesti äratuntav onchain, seega on soovitatav hoiustada raha CoinJoin kaudu ja teie identiteediga mitteseotud päritoluga. Sama on soovitatav teha ka siis, kui soovite aegunud fidelity bond'i JoinMarketist välja viia.



Oluline on meeles pidada, et fidelity bond'i on võimalik uuesti laadida ainult ühe tehinguga, UTXO mitmekordsete tehingute puhul loetakse FB jaoks kehtivaks ainult suurim tehing.



Tegeleme nüüd selle lõigu alguses mainitud skriptiga, kui oleme loonud fidelity bond'i (mis mäletatavasti on vabatahtlik), oleme valmis käivitama käivitatava faili, et tegutseda makerina joinMarketil. Kui Satss on hoiustatud erinevatel aadressidel ja mixdepth saame käivitada käsu:



```bash
python yg-privacyenhanced.py <wallet name>
```



Alates sellest hetkest (pärast mõne minuti pikkust võrku ühendamist) ja kuni me lõpetame skripti, meie JoinMarket klient ilmub protokolli aktiivsete tegijate nimekirja ja pakub meie likviidsust erinevatele vastaspooltele, et teha CoinJoin. Ärge oodake kümneid CoinJoins päevas (kui teil ei ole suur fidlity ja suur likviidsus hoiustatud Wallet), samuti pidage meeles, et tegurid nagu nõutavad tasud ja hoiustatud Satoshis mõjutavad seda, kui tihti te olete tegija.



Allpool toodud käsu käivitamisega näete kõigi Wallet tehtavate tehingute ajalugu ja mis tahes kasumit (kui olete tegija) või tasu kulu (kui olete võtja), mis teil on olnud portfelli eluea jooksul.



```bash
python wallet-tool.py <wallet name> history
```



Kui teie Satoshid teevad CoinJoins'i, liiguvad nad segusügavusest segusügavusse, kuni nad jõuavad viimasesse segusügavusse. Kui nad ületavad neljanda, naasevad nad mixdepth 0, see on teie otsustada, kui palju privaatsust saada, enne kui nad liiguvad Cold Wallet, on soovitatav lõpetada täielik Wallet tsükkel.



## Tumbler



Siin me oleme lõpuks JoinMarketi kõige mahlakama osa juures, tumbleri juures! Kui olete podcasti kuulanud, siis teate juba, millest see kõik räägib. Üks soovitus enne, kui me alustame: **Vältige tasusid!** Ärge unustage joinmarket.cfg failis piiranguid (nagu alguses selgitatud) ja kaaluge programmi käivitamist ainult siis, kui onchain tasud on suhteliselt madalad (alla 10 Sats/vB).



Et käivitada tumbler on vaja peatada skripti tegija (kui see oli aktiivne), pärast seda saame käivitada käsu:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Oluline on sisestada **sellele** vähemalt 3 väljundaadressi: see on vajalik selleks, et tagada hea privaatsus ja mitte luua protsessi jooksul ilmseid seoseid UTXOde vahel. Nagu tavaliselt, lisades käsule `--help`, saate minna ja näha kõiki täiendavaid üksikasju. Lähme vaatama keerulisemat näidet täiustatud reeglitega:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



Sel juhul oleme käivitanud tumbling skripti, mis ei kasuta vaikimisi arv vasteid (-N parameeter näitab, et me nõuame 7 vasteid maksimaalse variatsiooniga 2, nii et juhuslik arv tegijaid 5 kuni 9) ja suurema arvu CoinJoin kohta mixdepth (vaikimisi see skript teeb juhusliku arvu CoinJoin kohta lõik Wallet vahemikus 1 kuni 3, kasutades -c 3 1 käsu asemel on 2 TO 4). Nii kulutame rohkem Sats tasusid, kuid meil on suurem anonüümsuse kogum.



Samuti võite lisada nii palju väljundaadresse kui soovite (minimaalselt 3, maksimum on ainult terve mõistus). Siiski ei ole privaatsuse huvides võimalik otsustada, kuidas Satoshi jaotatakse väljundiks määratud aadresside vahel.



Tumbler on tahtlikult pikk protsess, aeg-ajalt võib juhtuda, et midagi ei tööta, enamasti laheneb see mõne tunni jooksul. Täieliku krahhi korral saame proovida seda taaskäivitada käsuga:



```bash
python tumbler.py --restart
```



Või lihtsalt taaskäivitage uus tumbling käsk. See ei käivita eelmise tumbleri ajakava, vaid alustab uut segamistsüklit. Juhul, kui sulgedes oma sõlme SSH-terminali, peatate ka skripti, võite kasutada käsuga paigaldatavat programmi `TMUX`:



```bash
sudo apt install tmux
```



Selle käivitamine shell'ist, kirjutades `tmux`, avab teile terminali, mis jääb taustal aktiivseks isegi siis, kui te sulgete kaugühenduse. Kui te ühendute uuesti oma sõlme käsuga: `tmux attach`, avate uuesti shell'i, mis jäi taustal aktiivseks.



## Kokkuvõte



JoinMarket on piirideta ja kohandatav tarkvara. Selles juhendis oleme avastanud peamised funktsioonid, nii et igaühel on võimalik seda kasutada (või vähemalt mina olen proovinud, saan aru, et selle tarkvara kasutamine ei ole jalutuskäik). Üks suurimaid probleeme JoinMarketiga on just see, et seda kasutavad inimesed ja on tegija. Kui seda tarkvara kasutavad vähe kasutajaid, väheneb üldine privaatsus (anon-set). Seepärast loodan, et see juhend stimuleerib kasutamist ja veenab teid minu lemmiktarkvara CoinJoin tegemiseks alla laadima ja installima. Juhul, kui soovite minna veel sügavamalt mõnda aspekti, soovitan teil lugeda erinevaid põhjalikke dokumente githubis, need on väga hästi tehtud ja te leiate need siit.



Õnnelik kilpkonnade segamine!🐢 💚 💚



[Siin](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) saate toetada Turtlecute'i