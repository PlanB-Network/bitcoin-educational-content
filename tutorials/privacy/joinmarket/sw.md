---
name: JoinMarket

description: Mwongozo na mafunzo ya jinsi ya kutumia JoinMarket kufanya CoinJoin juu ya Bitcoin kupitia mstari wa amri
---

![cover](assets/cover.webp)



---

Ikiwa umepata ukurasa huu kwa kutafuta mtandaoni kwa "JoinTmarket" una shukrani zangu za dhati. Hata hivyo, umejikwaa kwenye mwongozo unaohusu mada tofauti kabisa, lakini ya kuvutia sana! 🚬🍁



Lengo la somo hili ni kuonyesha utendakazi wa kinadharia na vitendo wa JoinMarket, kupitia mstari wa amri. 🐢 💚



## Ufafanuzi wa Kinadharia wa JoinMarket



Tunaweza kufafanua JoinMarket kama zana, au Wallet, inayowezesha CoinJoin na watumiaji wengine kwa njia ya Trustless kabisa na bila mratibu mkuu yeyote.



Kwa kuwa sehemu nzima ya kinadharia ya zana hii ni pana sana, niliamua kuiweka Address katika kipindi maalum cha podikasti yangu. Kwa wale wanaoweza kuelewa Kiitaliano, ninapendekeza sana kuendelea kusoma baada ya kusikiliza kipindi, ili kuiga vyema dhana za msingi za kutumia programu hii ipasavyo.



Unaweza kupata kipindi kwa viungo hivi vya moja kwa moja:




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/kipindi e/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon muziki](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b 03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (hapa unaweza kuisikiliza moja kwa moja kutoka kwa kivinjari).
- [Antena pod](https://antennapod.org/) ni kidhibiti cha podikasti huria na huria ambacho hakihitaji usajili. Ili kupata kipindi pakua programu, ongeza podikasti yangu mwenyewe kwa kubandika [kiungo hiki](https://Anchor.fm/s/bd5d5b20/podcast/rss) katika sehemu ya _feed rss_, kisha utafute kipindi kilichowekwa kwa JoinMarket.



## Ufungaji



Mifumo ya Uendeshaji:





- Raspiblitz
- Mwavuli
- MyNode
- Raspibolt



## Faili za Usanidi



JoinMarket ni programu inayoweza kubinafsishwa na idadi isiyo na kikomo ya mipangilio; mipangilio hii imebainishwa katika faili ya usanidi iliyo katika saraka kuu ya programu inayoitwa `Joinmarket.cfg`.



Katika sehemu hii tutapitia baadhi ya nyanja ambazo unaweza kupata kuvutia kuchunguza na/au kurekebisha, kulingana na mahitaji yako. Ningependa kusisitiza kwamba mabadiliko yote yaliyoorodheshwa hapa chini ni muhimu kujua ili kurekebisha uendeshaji wa programu kwa mahitaji ya kibinafsi wakati sio lazima.



Kwanza wacha tuhamie kwenye folda ya `joinmarket/scripts` na tuendeshe amri:



```bash
python wallet-tool.py generate
```


Katika hatua hii tunapaswa kupata hitilafu, lakini kufanya hivyo kutasababisha programu generate faili ya mipangilio iliyowekwa awali kwa ajili yetu. Tunaweza kwenda na kuhariri faili ya mipangilio kutoka kwa terminal na:



```bash
nano joinmarket.cfg
```



au:



```bash
vim joinmarket.cfg
```



ikifunguliwa tutaona mistari mingi yenye mipangilio mbalimbali na maelezo yake kwa Kiingereza. Hasa tutachambua hapa chini vigezo vya kuvutia zaidi:





- `merge_algorithm` iwapo tutafanya kama mtengenezaji sehemu hii itarekebisha jinsi programu itaunganisha kwa ukali Matokeo ambayo hayajatumika. Iwapo tutakuwa na UTXO nyingi za kujumuisha, inaweza kuwa na maana kubadili kutoka _gradual_ hadi _greedy_
- `tx_fees` hurekebisha kama mtoaji ada za kulipia muamala, ni muhimu sana kubadilisha mpangilio huu ikiwa unatumia bilauri mara kwa mara (tutazungumza juu yake baadaye) kwa sababu ikiwa kuna ongezeko la ada wakati wa kutekeleza la pili, ikiwa hatutaweka uga huu ipasavyo, tunaweza kutumia kiasi kikubwa cha CoinJoin1 kwa CoinJoin1. Kwa kuweka maadili katika maelfu (kama vile 2000) hii itakuwa sawa na 2 Sats/vBytes, 3500 hadi 3.5 Sats/vBytes, na kadhalika. Ningependekeza nambari kuanzia 1500 hadi 6000 kulingana na mahitaji yako.
- `max_cj_fee_abs` hutumika kubainisha ni kiasi gani tuko tayari kulipa kwa masharti kamili kwa waundaji tunaowachagua wakati wa CoinJoin. Kwa chaguo-msingi sehemu hii ya watengenezaji ni 200 Sats, chaguo zuri linaweza kuwa nambari kuanzia 200 hadi 1000 Sats kwa kila mwenza (hii inategemea ni kiasi gani unataka kutumia na ni kiasi gani kisichopangwa unachotafuta kwa CoinJoins zako)
- `max_cj_fee_rel` ina kazi sawa na sehemu iliyo hapo juu lakini inabainisha ada husika (asilimia) ambazo tuko tayari kulipa kwa kila kampuni. Kwa kuwa hii ni thamani ya `asilimia`, kuwa mwangalifu usiweke viwango vya juu ili kuepuka gharama kubwa katika CoinJoins kwa kiasi kikubwa. Thamani chaguo-msingi ya waundaji ni _0.00002_, ninapendekeza thamani inayofanana au ya juu zaidi.
- `minimum_makers` ni sehemu inayobainisha ni washirika wangapi tunafanya nao CoinJoin, kwa chaguo-msingi joinMarket huchagua kila mara kutoka kwa washirika 4 hadi 9, ikiwa tunataka, kwa faragha zaidi, tunaweza kuongeza thamani hii hadi 5 au 6 (itafanya miamala kuwa ghali zaidi ingawa).
- `cjfee_a` inabainisha, iwapo tutatenda kama mtengenezaji, ni Sats ngapi kwa masharti kamili tunayotaka kukusanya kwa ajili ya kukodisha ukwasi wetu. Sehemu hii ni ya kibinafsi kabisa, thamani chaguo-msingi tayari ni nzuri sana (kwa hivyo tutakuwa na faragha bora kama mtengenezaji) tunaweza kufikiria kuipeleka hadi 0 ikiwa tunataka kutengeneza CoinJoin zaidi kwa muda mfupi.
- `cjfee_r` sawa na sehemu iliyo hapo juu lakini kwa asilimia na si kamili. Tena ninapendekeza kuacha thamani chaguo-msingi au kuipunguza ili kuvutia wapokeaji zaidi.
- `ordertype` iliyo na sehemu hii tunachagua kutoka kwa mtengenezaji ikiwa tutachaji kabisa (absoffer) au asilimia (reloffer). Kawaida wapokeaji wanapendelea zabuni kamili kwa maswala ya kiuchumi.
- `minsize` ikiwa kama mtengenezaji hatutaki kuwa na UTXO ndogo sana tunaweza kubainisha kiwango cha chini cha CoinJoin cha kushiriki. Sehemu hii imeonyeshwa katika Satoshi na ni ya kibinafsi kabisa. Tunaweza kuacha uwanja huu kwa 0 au kuongeza hadi 500000 (Sats), 1000000 (Sats), na kadhalika.



Kuwa mwangalifu sana usihariri sehemu zisizo sahihi, baadhi ya vigeu katika faili ya joinmarket.cfg ikiwa imewekwa vibaya inaweza kuathiri utendaji wa programu au kuharibu kabisa faragha yako, macho wazi na tahadhari kwa upeo!



## Mpangilio wa Mazingira ya Kazi



Baadhi ya nodi huweka kiotomati thamani sahihi za sehemu hizi ndani ya faili ya joinmarket.cfg ninapendekeza uangalie upya mwenyewe:





- `rpc_user = yourusername-as-in-Bitcoin.conf`
- `rpc_password = yourpassword-as-in-Bitcoin.conf`
- `rpc_host = localhost #default kawaida ni sahihi`
- `rpc_port = 8332 # chaguomsingi kwa Mainnet`



Kwa hatua hii tunaweza kuendelea na uundaji wa Wallet yetu ndani ya JoinMarket:



```bash
python wallet-tool.py generate
```



Amri hii itatufanya tuingize nenosiri ambalo tutatumia kwa njia fiche Wallet na jina tunalotaka kuipa, inapokuuliza ikiwa unataka kuunga mkono vifungo vya uaminifu ninapendekeza kutumia chaguo la _yes_, matokeo yaliyorejeshwa yataonekana kama hii:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


ikiwa hitilafu itatokea kuna uwezekano mkubwa kwamba tumeweka kimakosa sehemu 4 za RPC zilizotajwa hapo juu. Iwapo inaweza kusaidia kufuata [mwongozo huu](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) inayopatikana katika hati asili ya JoinMarket.



Tumekamilisha usanidi wa mazingira yetu ya kazi na tunaweza kuanza kuchunguza amri ambazo zitakuwa na manufaa zaidi kwetu. Hati zote tutakazojadili zinaweza kuzinduliwa katika dashibodi ikifuatiwa na `--help` kwa maelezo ya kina.



Sasa tunaweza kujaribu kuzindua:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



amri hii itakuonyesha mchanganyiko wote wa Wallet na anwani tofauti zilizoainishwa kama:




- Mpya (Address haijawahi kutumika)
- Kubadilisha (salio la muamala uliopita)
- Cj-out (matokeo ya CoinJoin)



hapa kuna mfano wa vitendo wa matokeo:



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


Sasa tunaweza kuendelea kuweka Satoshi zetu za kwanza ndani ya anwani moja au zaidi tukikumbuka kwamba bila kujali mtengenezaji au anayeichukua, programu haitawahi kwenda na kuunganisha UTXO katika mchanganyiko tofauti moja kwa moja, kwa njia hii tunaweza kutenganisha Satss na viwango tofauti vya faragha ndani ya Wallet.



## Inatuma Bitcoin na CoinJoin Single



Sasa tunaweza kuhamisha Satoshi zetu. Moja ya amri kuu katika programu hii ni hati:



```bash
pyhton sendpayment.py
```


ambayo itaturuhusu kutuma miamala kwa anwani zingine na au bila CoinJoin. Wacha tuangalie jinsi inavyofanya kazi na mifano kadhaa ya vitendo. Kwa chaguo-msingi umbizo la amri ni (kumbuka kubadilisha maandishi yaliyoambatanishwa na alama < na >):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



mfano wa msingi wa matumizi unaweza kuwa:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


katika hali hii tutatuma kwa Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc yaani 5000000 Satoshi kutoka kwa kina chetu cha mchanganyiko 0 (chaguo-msingi) kwa kuchagua kutoka kwa 4 hadi 9 za chaguo-msingi za GW-3 (defa 9).



Ili kuwa na udhibiti zaidi juu ya jinsi na UTXO za kutumia tunaweza kwenda juu ya chaguzi za ziada kwa amri hii:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


katika mfano huu tumeongeza vipimo viwili: -N inaonyesha ni vyama vingapi tutachanganyikana, -m mchanganyiko ambao tutatoa pesa. Kwa hakika, tumetuma 100,000,000 Sats (1 btc) kwa Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c pamoja na fedha hizo kwa kina 1 na kuchanganya na wenzao 5.



Ikiwa tutaweka 0 kama thamani ya kutuma kwa kubainisha kina cha mchanganyiko, joinMarket itafanya kile kinachoitwa `kufagia`, yaani, itatuma pesa zote kwa undani huo kwa kuziunganisha zenyewe:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



hapa tulituma pesa zote kutoka kwa mixdepth 0 (hatungeweza kuainisha kwa sababu hiyo ndio chaguo-msingi) tukichanganya na wenzao 7.



Amri ya malipo ya kutuma hutumika kuhamisha fedha kutoka joinMarket hadi Wallet ya nje au kutuma Satoshi kwa mtu kwa kuongeza Layer ya faragha kati yetu na yeye. Ili kupata kiwango cha kutosha cha faragha kwenye UTXO zetu inafaa zaidi kutumia amri ya tumbler.py ambayo tutaelezea baadaye katika mwongozo huu.



## Kuwa Muumba



Hati tutakayoshughulikia katika sehemu hii ni:



```bash
yg-privacyenhanced.py
```



Mpango huu unatumika kama mtengenezaji katika joinMarket. Programu itaunganishwa kwenye nodi yetu ya Bitcoin na soko la ndani la jukwaa ambalo waundaji wanajionyesha kama wazabuni wa ukwasi na wapokeaji kutafuta wenzao. Iwapo unataka kutumia dhamana ya uaminifu unaweza kuunda moja na umbizo hili:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



kwa mfano:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



pato ambalo litarejeshwa kwetu litakuwa Bitcoin Address (yaani, moja ambayo utahitaji kuweka fedha unayotaka kutenga kwa uaminifu).



**Tahadhari**: Kuna mambo mawili ya kuzingatia kwa makini ikiwa utaunda Fidelity Bond (a.k.a. FB);





- fedha zikishawekwa, haziwezi kuhamishwa tena hadi muda wake uishe. Zingatia ni Sats ngapi unazotuma kwa Address na jinsi unavyopanga tarehe. Makosa hayaruhusiwi!
- Dhamana ya uaminifu inatambulika kwa urahisi kwenye mnyororo, kwa hivyo inashauriwa kuweka fedha kupitia CoinJoin na asili isiyohusiana na utambulisho wako. Jambo hilo hilo pia inashauriwa kufanya mara tu unapotaka kuhamisha dhamana ya uaminifu iliyoisha muda wake kutoka kwa JoinMarket.



Ni muhimu kukumbuka kuwa inawezekana kupakia upya dhamana ya uaminifu kwa muamala mmoja tu, katika kesi ya vizidishio vya UTXO, kubwa zaidi pekee ndiyo itachukuliwa kuwa halali kwa FB.



Wacha sasa tushughulikie hati iliyotajwa mwanzoni mwa aya hii, mara tu tumeunda dhamana ya uaminifu (ambayo tunakumbuka kuwa ni ya hiari) tuko tayari kutekeleza inayoweza kutekelezwa ili kufanya kazi kama mtengenezaji kwenye joinMarket. Mara tu Satss zimewekwa kwenye anwani tofauti na mchanganyiko tunaweza kutekeleza amri:



```bash
python yg-privacyenhanced.py <wallet name>
```



Kuanzia wakati huu na kuendelea (baada ya dakika chache za kuunganishwa kwenye mtandao) na hadi tutakaposimamisha hati, mteja wetu wa JoinMarket ataonekana kwenye orodha ya waundaji wanaofanya kazi kwenye itifaki na kutoa ukwasi wetu kwa washirika mbalimbali kutengeneza CoinJoin. Usitarajie dazeni za CoinJoins kwa siku (isipokuwa una uaminifu mkubwa na ukwasi mkubwa uliowekwa kwenye Wallet), pia kumbuka kuwa vipengele kama vile ada zinazohitajika na Satoshis zilizowekwa huathiri mara ngapi utakuwa mtengenezaji.



Kwa kutekeleza amri iliyo hapa chini utaweza kuona historia ya miamala yote iliyofanywa kwenye Wallet na faida yoyote (ikiwa wewe ni mtengenezaji) au gharama ya ada (ikiwa wewe ni mchukuaji) umekuwa nayo kwa muda wa maisha ya Wallet.



```bash
python wallet-tool.py <wallet name> history
```



Mara Satoshis wako wanapotengeneza CoinJoins, zitasonga kutoka kwa mchanganyiko hadi kwa kina hadi kufikia ile ya mwisho. Mara baada ya nne watarudi kwa mixdepth 0, ni juu yako ni kiasi gani cha faragha kupata kabla ya kuwahamishia kwenye Cold Wallet, inashauriwa kumaliza mzunguko kamili wa Wallet.



## Birika



Hapa hatimaye tuko kwenye sehemu yenye juisi zaidi ya JoinMarket, bilauri! Ikiwa umesikiliza podikasti tayari unajua hii inahusu nini. Pendekezo moja kabla hatujaanza: **Jihadhari na ada!** Kumbuka kuweka vikomo katika faili ya joinmarket.cfg (kama ilivyoelezwa mwanzoni) na uzingatie kuendesha programu wakati ada za onchain ziko chini kiasi (chini ya 10 Sats/vB).



Ili kuzindua bilauri ni muhimu kusimamisha hati kutoka kwa mtengenezaji (ikiwa ilikuwa hai), baada ya hapo tunaweza kuendesha amri:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Ni muhimu kuweka **angalau** anwani 3 za kutoa kwa bilauri: hii ni kuhakikisha faragha nzuri na sio kuunda viungo dhahiri kati ya UTXOs katika mchakato wote. Kama kawaida kwa kuongeza`--help` kwa amri unaweza kwenda na kuona maelezo yote ya ziada. Wacha tuone mfano ngumu zaidi na sheria za hali ya juu:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



Katika kesi hii, tumezindua hati inayoporomoka ambayo haitatumia nambari chaguo-msingi ya wenzao (kigezo cha -N kinaonyesha kuwa tunahitaji wenzao 7 walio na tofauti ya juu ya 2, kwa hivyo idadi isiyo ya kawaida ya waundaji kutoka 5 hadi 9) na kwa idadi kubwa ya CoinJoin kwa kila mchanganyiko (kwa chaguo-msingi hati hii hufanya nambari isiyo ya kawaida ya GW-51 kwa kila sehemu ya GW-51 - 6 kwa kila sehemu ya GW-51 - 6. 3 1 amri badala yake itakuwa kutoka 2 HADI 4). Kwa njia hii tutatumia Sats zaidi katika ada lakini tutakuwa na seti kubwa ya kutokujulikana.



Unaweza pia kuongeza anwani nyingi za pato unavyotaka (kiwango cha chini 3, hakuna kiwango cha juu zaidi ya akili ya kawaida). Hata hivyo, haiwezekani, kwa masuala ya faragha, kuamua jinsi Satoshi itasambazwa kati ya anwani zilizobainishwa kama pato.



Bilauri ni mchakato mrefu wa kimakusudi, mara kwa mara inaweza kutokea kwamba kitu kitaacha kufanya kazi, katika hali nyingi hii itajisuluhisha yenyewe ndani ya saa chache. Katika kesi ya ajali jumla tunaweza kujaribu kuianzisha tena kwa amri:



```bash
python tumbler.py --restart
```



Au anzisha tena amri mpya ya kuporomoka. Hii haitaanza upangaji wa bilauri iliyotangulia lakini itaanza mzunguko mpya wa kuchanganya. Katika kesi ya kufunga terminal ya SSH kwa nodi yako pia itasimamisha hati unaweza kuchukua fursa ya programu ya `TMUX` ambayo inaweza kusanikishwa kwa amri:



```bash
sudo apt install tmux
```



Kuizindua kutoka kwa ganda kwa kuandika `tmux` kutafungua terminal kwa ajili yako ambayo itasalia amilifu chinichini hata ukifunga muunganisho wa mbali. Unapounganisha tena kwa nodi yako kwa amri: `tmux ambatisha` utafungua tena ganda lililobakia amilifu nyuma.



## Hitimisho



JoinMarket ni programu isiyo na kikomo na inayoweza kubinafsishwa. Katika mwongozo huu tumegundua kazi kuu ili iwezekanavyo kwa mtu yeyote (au angalau nimejaribu, ninatambua kuwa kutumia programu hii sio kutembea kwenye hifadhi) kuitumia. Mojawapo ya shida kubwa na JoinMarket ni kwamba tu: idadi ya watu wanaoitumia na kuwa mtengenezaji. Ikiwa watumiaji wachache watachukua fursa ya programu hii, faragha ya jumla (isiyo ya kuweka) itapunguzwa. Ndio maana ninatumai mwongozo huu utakuhimiza utumiaji na kukushawishi kupakua na kusakinisha programu ninayopenda kutengeneza CoinJoin. Iwapo unataka kwenda zaidi katika vipengele vingine ninapendekeza usome kwa hati mbalimbali za kina kwenye github, zimefanywa vizuri na unaweza kuzipata hapa.



Furaha ya kuchanganya kasa!🐢 💚



[Hapa](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) unaweza kusaidia Turtlecute