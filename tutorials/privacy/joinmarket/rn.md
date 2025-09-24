---
name: JoinMarket

description: Inyigisho n'inyigisho ku buryo bwo gukoresha JoinMarket kugira ngo ukore CoinJoin kuri Bitcoin biciye ku murongo w'amabwirizwa
---

![cover](assets/cover.webp)



---

Niwaba wabonye iyi page mu kurondera kuri internet "JoinTmarket" urafise ugukenguruka kwanje kuvuye ku mutima. Ariko rero, waratsitaye ku ndongozi ivuga ku ciyumviro gitandukanye rwose, ariko gishimishije cane! 🚬🍁



Intumbero y’iyi nyigisho ni iyo kwerekana ingene JoinMarket ikora mu vyiyumviro no mu bikorwa, biciye ku murongo w’amabwirizwa. 🐢 💚



## Insobanuro y'Ivyiyumviro vy'Isoko



Turashobora gusobanura JoinMarket nk’igikoresho, canke Wallet, gishoboza CoinJoin n’abandi bakoresha mu buryo bwa Trustless bwose kandi ata muhuzabikorwa wa mbere.



Kubera ko igice cose c’ivyiyumviro c’iki gikoresho ari kinini cane, nafashe ingingo yo kugikora Address mu kiganiro kinaka ca podcast yanje. Ku bashobora gutahura igitaliyano, ndabahimiriza cane gukomeza gusoma bamaze kwumviriza ikiganiro, kugira ngo bashobore gutahura neza ivyiyumviro nyamukuru vyo gukoresha neza iyo porogarama.



Ushobora gukurikirana ikiganiro kuri aya mahuza:




- [Spotify] (gufungura.spotify.com/igice/1UaeQxpNq9capLE3KwArbo)
- [Google n'ibindi biganiro] (ibiganiro e/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAQEw)
- [Amazoni umuziki] (ibice 54 ukuboza 992-5b 03-463a-bb98-f653b72ccb63/I-Imbere-ya-Bitcoin-Isoko-ry'Igihugu-ry'Igihugu-Igihugu-Igihugu-Igikoko)
- [Anchor](aha ushobora kuyumviriza uhereye ku mucukumbuzi).
- [Antenna pod](https://antennapod.org/) ni umuyobozi w’amakuru y’ubuntu kandi yuguruye adasaba kwiyandikisha. Kugira uronke ikiganiro fungura app, wongereko n’amaboko podcast yanje mu gushiramwo [iyi nzira](https://Anchor.fm/s/bd5d5b20/podcast/rss) mu gice ca _feed rss_, hanyuma urondere ikiganiro cagenewe JoinMarket.



## Gushiramwo



Uburyo bwo gukoresha:





- Raspiblitz
- Umutaka
- Urudodo rwanje
- Igipfunsi



## Dosiye z'imiterere



JoinMarket ni porogaramu ishobora guhindurwa ifise umubare udahera w’ibintu bishobora guhindurwa; ivyo bimenyetso bigaragazwa muri dosiye y'imiterere iri mu bubiko bwa porogaramu nyamukuru yitwa `Joinmarket.cfg`.



Muri iki gice turaza guca ku bintu bimwe bimwe woshobora gusanga bishimishije gutohoza no/canke guhindura, bivanye n’ivyo ukeneye. Ndashaka gushimika ku vy’uko amahinduka yose ari aha hepfo ari ngirakamaro kumenya kugira ngo umuntu ashobore guhuza imikorere ya porogarama n’ivyo umuntu akeneye mu gihe atari ngombwa.



Mbere reka tuje kuri dosiye ya `joinmarket/scripts` maze dukoreshe itegeko:



```bash
python wallet-tool.py generate
```


Muri iki gihe dukwiye kuronka ikosa, ariko kubigira bizotuma porogarama idufasha generate dosiye y’imiterere yashizweho imbere y’igihe. Turashobora kuja guhindura dosiye y'imiterere kuva kuri terminal na:



```bash
nano joinmarket.cfg
```



canke:



```bash
vim joinmarket.cfg
```



iyo umaze gufungura tuzobona imirongo myinshi irimwo ibintu bitandukanye n’insobanuro yayo mu congereza. Mu buryo bwihariye tuzosuzuma aha hepfo ibihinduka bishimishije cane:





- `merge_algorithm` mu gihe twobikora nk'umuhinguzi iki kibanza gihindura ingene porogaramu izokoranya Ibisohoka bitakoreshejwe. Mu gihe twoba dufise ama UTXO menshi yo gushiramwo, vyoshobora kuba vyiza duhindutse tuva ku _buhoro buhoro_ tukaja ku _kunzi_
- `tx_fees` itunganya nk'uwufata amafaranga yo kwishura igikorwa, ni ngirakamaro cane guhindura iyo nzira mu gihe woba ukoresha igikombe kenshi (ivyo tuzobivuga mu nyuma) kuko iyo habaye ugutera imbere kw'amahera mu gihe c'ugushirwa mu ngiro kw'ivyo vya nyuma, iyo tutashizeho neza iki kibanza sp-W to G10. Mu gushinga agaciro mu bihumbi (nk’aka 2000) ivyo bizongana na 2 Sats/vBytes, 3500 gushika kuri 3,5 Sats/vBytes, n’ibindi. Nashaka gusaba umubare uva kuri 1500 gushika kuri 6000 bivanye n’ivyo ukeneye.
- `max_cj_fee_abs` ikoreshwa mu kugaragaza ingene twiteguye kwishura mu buryo bushitse ku bahinga duhisemwo mu gihe ca CoinJoin. Kubera ko iki kibanza c’abahinguzi ari 200 Sats, uburyo bwiza bwoshobora kuba umubare uva kuri 200 gushika kuri 1000 Sats ku muntu wese (ivyo bishingiye ku rugero ushaka gukoresha n’ingene anon-set urondera kuri CoinJoins zawe)
- `max_cj_fee_rel` ifise igikorwa kimwe n'ico mu mwanya uri hejuru ariko igaragaza amafaranga (amajana) twiteguye kwishura umugenzi wese. Kubera ko iki ari `agaciro k'ijanisha`, urabe ko udashiraho agaciro kanini kugira ngo wirinde ibiciro vyinshi muri CoinJoins n'amahera menshi. Agaciro ka mbere k'abahinguzi ni _0.00002_, ndasaba agaciro gasa canke karengeye gato.
- `minimum_makers` ni umurima ugaragaza ingene abandi bafatanyabikorwa dukorana CoinJoin, ku buryo busanzwe joinMarket yama ihitamwo kuva ku bafatanyabikorwa 4 gushika ku 9, nitwabishaka, kugira ngo tugire ubuzima bwite bwinshi, turashobora kuduza ako gaciro kugera kuri 5 canke 6 (bizotuma amafaranga azimvye naho).
- `cjfee_a` isobanura, mu gihe twokora nk'umuhinguzi, ni Sats zingahe mu majambo y'ukuri dushaka gukoranya kugira ngo dukodeshe amahera yacu. Iyi nzira ni iyo umuntu yiyumvira, agaciro ka mbere karasanzwe ari keza cane (tuzogira rero ubuzima bwite bwiza nk’umuhinguzi) turashobora kwiyumvira kuyijana kuri 0 nimba dushaka gukora CoinJoin nyinshi mu gihe gito.
- `cjfee_r` kimwe n'ivyo hejuru ariko mu majambo y'ijanisha kandi si ivy'ukuri. Na none ndabagira inama yo gusiga agaciro ka mbere canke mukagabanura kugira ngo mukwegere abafata benshi.
- `ordertype` n'iki kibanza duhitamwo ku muhinguzi nimba twosaba vyose (absoffer) canke ijana (reloffer). Kenshi abafata amasoko bakunda gutanga amasoko ataco amaze ku bibazo vy’ubutunzi.
- `minsize` nimba nk'umuhinguzi tudashaka ko UTXO iba nto cane turashobora gusobanura CoinJoin ntoyi kugira ngo tugiremwo uruhara. Ico kibanza kigaragazwa muri Satoshi kandi ni ikintu umuntu yiyumvira. Twoshobora gusiga uwo murima kuri 0 canke tukawongera ukagera kuri 500000 (Sats), 1000000 (Sats), n’ibindi.



Urabe maso cane ntuhindure ivyicaro bitari vyo, bimwe mu bihinduka biri muri dosiye joinmarket.cfg iyo bishizweho nabi bishobora gutuma porogarama idakora neza canke bikazimanganya burundu ubuzima bwite bwawe, amaso yuguruye kandi wiyubare ku rugero rwo hejuru!



## Gutegura ibidukikije vy'akazi



Hariho ama node yihita ashiraho agaciro kabereye k'ivyo bibanza muri dosiye joinmarket.cfg ndabagira inama yo gusubira gusuzuma n'amaboko:





- `rpc_ukoresha = izina ryawe-nk'uko-muri-Bitcoin.conf`
- `rpc_ijambobanga = ijambobanga ryawe-nk'uko-muri-Bitcoin.conf`
- `rpc_host = umushitsi wo mu karere # mburabuzi akenshi arakosora`
- `Icuma_c_rpc = 8332 # mburabuzi kuri Mainnet`



Muri iki gihe turashobora gukomeza n’uguhingura Wallet yacu muri JoinMarket:



```bash
python wallet-tool.py generate
```



Iri tegeko rizotuma twinjiza ijambobanga twokoresha mu gupfuka Wallet n’izina dushaka kuyiha, iyo ikubajije nimba ushaka canke utashaka gushigikira amasezerano y’ubudahemuka ndagusavye gukoresha uburyo bwa _yes_, igisubizo kizogaruka kizomera gutya:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


iyo habaye ikosa birashoboka cane ko twashizeho nabi ivyicaro 4 vya RPC vyavuzwe haruguru. Mu gihe vyoshobora gufasha gukurikira [iyi nkuru](https://github.com/JoinMarket-Org-Org/umucukumbuzi-umukozi/umucungerezi w’isoko/umucungerezi/USA.md#uclengagisi) aboneka mu nyandiko y’intango y’intango.



Twararangije gutegura aho dukorera kandi turashobora gutangura gutohoza amabwirizwa azotugirira akamaro cane. Ivyanditswe vyose tuzovugako birashobora gutangura muri console ikurikirwa na `--help` kugira ngo ubone insobanuro yimbitse.



Ubu turashobora kugerageza gutanguza:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



iri tegeko rizokwereka uburebure bwose butandukanye bwa Wallet n'amaderesi atandukanye ashizwe mu migwi nk'iyi:




- Ishasha (Address ntiyigeze ikoreshwa)
- Guhindura-inyuma (ibisigaye vy'ugucuruza kwa kera)
- Cj-isohoka (isohoka rya CoinJoin)



aka ni akarorero ngirakamaro k’ivyo vyavuyemwo:



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


Ubu turashobora gukomeza gushiramwo Satoshis zacu za mbere muri aderesi imwe canke nyinshi twibuka ko ata kuraba uwuyikora canke uwuyifata, porogarama ntizokwigera ija ngo ishiremwo UTXO mu mixdepths zitandukanye ataco ihinduye, muri ubwo buryo turashobora kuguma dufise Satss n’ingero zitandukanye z’ubuzima bwite zitandukanye muri Wallet.



## Kurungika Bitcoin na CoinJoin imwe



Ubu turashobora kwimura Satoshis zacu. Imwe mu mategeko nyamukuru muri iyi porogaramu ni inyandiko:



```bash
pyhton sendpayment.py
```


ivyo bizotuma twohereza amafaranga ku yindi mideresi dufise canke tutafise CoinJoin. Reka turabe ingene bikora be n’ingero zimwe zimwe ngirakamaro. Ku mburabuzi, imiterere y'itegeko ni (wibuke gusubirira umwandiko ukikujwe n'ibimenyetso < na >):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



akarorero k'ishimikiro k'ikoreshwa gashobora kuba:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


muri iki gihe tugiye kohereza kuri Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc ni ukuvuga 5000000 Satoshi kuva ku mixdepth yacu 0 (iyisanzwe) mu kuja guhitamwo kuva ku 9fa-4. ubugyo).



Kugira ngo tugire ububasha bwinshi ku buryo n'ivyo UTXOs twokoresha turashobora guca ku mahitamwo y'inyongera kuri iri tegeko:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


muri aka karorero twongeyeko ibintu bibiri: -N yerekana umubare w’abafatanyabikorwa tuzovanga, -m uburebure bw’uguvanga tuzokuramwo amahera. Nkako, twarungitse amafaranga 100.000.000 Sats (1 btc) ku Address 1mprGzBA9rQ82Ly41TsmpQGa8UPpZb2w8c n’amahera ari mu mixdepth 1 no kuvanga n’abafatanyabikorwa 5.



Nitwashira 0 nk'agaciro ko kohereza mu kugaragaza uburebure bw'uruvange, joinMarket izokora ico bita `sweep`, ni ukuvuga ko izorungika amahera yose ari muri ubwo burebure bw'uruvange mu kuyafatanya:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



aha twarungitse amafaranga yose avuye muri mixdepth 0 (twari gushobora kutayasobanura kuko arivyo bimenyetso) tuvanga n’ibindi 7.



Itegeko rya sendpayment rikoreshwa mu gukura amahera muri joinMarket aja muri Wallet yo hanze canke mu kohereza Satoshi ku muntu mu kwongerako Layer y’ubuzima bwite hagati yacu na we. Kugira ngo turonke urugero ruhagije rw’ubuzima bwite ku ma UTXO yacu birabereye gukoresha itegeko tumbler.py tuzosigura mu nyuma muri iyi nkuru.



## Kuba Umuhinguzi



Inyandiko tugiye kuvuga muri iki gice ni:



```bash
yg-privacyenhanced.py
```



Iyi porogaramu ikoreshwa mu gukora nk'umuhinguzi muri joinMarket. Iyi porogarama izohuza n’uruzitiro rwacu rwa Bitcoin be n’isoko ry’imbere ry’urubuga aho abayikora biyerekana nk’abatanga amasoko y’amahera n’abayifata barondera abayifata. Mu gihe woba ushaka gukoresha ubucuti bw'ubudahemuka ushobora kubukora ufise ubu buryo:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



Nk'akarorero:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



igisohoka kizodusubiza kizoba ari Bitcoin Address (i.e., iyo uzokenera gushiramwo amahera ushaka guha ubudahemuka).



**Iciyumviro**: Hari ibintu bibiri vyo kwitwararika cane nimba ugiye gukora Fidelity Bond (a.k.a. FB);





- iyo amafaranga amaze gushirwamwo, ntashobora gusubira kwimurirwa gushika igihe kirangiye. Witwararike Satss zingahe wohereje kuri Address n’ingene ukora format y’itariki. Amakosa ntabwo yemerewe!
- Iryo kete ry’ubudahemuka rimenyekana bitagoranye onchain, ni vyiza rero ko ushiramwo amahera biciye ku CoinJoin kandi ufise inkomoko idafitaniye isano n’akaranga kawe. Ivyo nyene ni vyiza gukora igihe ushaka kwimurira isezerano ry’ubudahemuka ryaheze muri JoinMarket.



Ni vyiza kwibuka ko bishoboka gusubira gushiramwo ingwati y’ubudahemuka n’ugucuruza kumwe gusa, mu gihe c’incuro za UTXO iyo nini cane ni yo yonyene izobonwa ko ifise akamaro kuri FB.



Reka noneho dufate ku script twavuze mu ntango y’iki gice, tumaze kurema fidelity bond (ico twibuka ko ari ubusabe) tuba twiteguye gukoresha executable kugira ngo ikore nk’umuhinguzi kuri joinMarket. Igihe Satss zimaze gushirwa ku ma aderesi atandukanye no ku mixdepth turashobora gukoresha itegeko:



```bash
python yg-privacyenhanced.py <wallet name>
```



Kuva ng’aho (inyuma y’iminota mikeyi yo kwifatanya n’urubuga) no gushika duhagaritse inyandiko, umukiriya wacu wa JoinMarket azoboneka ku rutonde rw’abakora ku masezerano maze atanga amahera yacu ku bandi batandukanye kugira ngo bakore CoinJoin. Ntukitege amajana ya CoinJoins ku musi (kiretse iyo ufise fidlity nini cane n’amahera menshi ubitse kuri Wallet), kandi wibuke ko ibintu nk’amahera asabwa n’ama Satoshis ashizweko bigira ico bikoze ku kuntu uzoba umuhinguzi.



Mu gukoresha itegeko riri musi uzoshobora kubona amateka y'ibikorwa vyose vyakozwe kuri Wallet n'inyungu iyo ari yo yose (niba uri umuhinguzi) canke amafaranga (niba uri umufata) waronse mu buzima bwa Wallet.



```bash
python wallet-tool.py <wallet name> history
```



Igihe aba Satoshis bawe bazoba bakoze CoinJoins, bazova ku mixdepth baje ku mixdepth gushika bashitse ku rwa nyuma. Iyo bamaze guca ku rwa kane bazosubira kuri mixdepth 0, ni wewe ubwawe ushobora kuronka ubuzima bwite bungana gute imbere yo kubajana mu Cold Wallet, ni vyiza ko urangiza urugendo rwuzuye rwa Wallet.



## Igikombe



Aha rero turi ku gice gifise umutobe mwinshi cane muri JoinMarket, igikombe! Niba warateze amatwi podcast urazi ivyo vyose arivyo. Impanuro imwe imbere y’uko dutangura: **Iyubare amafaranga!** Ibuka gushinga imipaka muri dosiye joinmarket.cfg (nk’uko vyasiguwe mu ntango) kandi wiyumvire gukoresha porogarama gusa iyo amafaranga onchain ari make cane (munsi ya 10 Sats/vB).



Kugira ngo utangure igikombe ni ngombwa ko haba ahagaritse inyandiko kuva ku muhinguzi (niba yari ikora), hanyuma turashobora gukoresha itegeko:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



Ni ngombwa kwinjiza **nibura** aderesi 3 z’isohoka ry’igikombe: ivyo ni kugira ngo habeho ubuzima bwite bwiza kandi ntihagire amahuzu agaragara hagati y’ama UTXO mu gihe cose c’urugendo. Nk'uko bisanzwe mu kwongerako`--help` kw'itegeko ushobora kuja kubona ibintu vyose vy'inyongera. Reka tugende turabe akarorero gakomeye cane gafise amategeko ateye imbere:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



Muri iki gihe twatanguje inyandiko y’ugutera imbere itazokoresha umubare w’abagenzi (parameter -N yerekana ko dusaba abagenzi 7 bafise itandukaniro ryinshi rya 2, rero umubare w’abahinguzi b’imburakimazi kuva kuri 5 gushika kuri 9) kandi n’umubare munini wa CoinJoin ku mixdepth ya seW ya se- Wallet kuva kuri 1 gushika kuri 3, ukoresheje itegeko -c 3 1 aho kuba kuva kuri 2 GUSHIKA kuri 4). Uko niko tuzokoresha Sats nyinshi mu mahera ariko tuzogira urutonde runini rw’ukutamenyekana.



Ushobora kandi kwongerako amaderesi menshi y’isohoka nk’uko ushaka (minimum 3, nta maximum iriho atari common sense). Ariko rero, ntibishoboka, ku bibazo vy’ubuzima bwite, gufata ingingo y’ingene Satoshi izokwiragizwa hagati y’amaderesi yerekanwa nk’isohoka.



Tumbler ni igikorwa kirekire n’ibigirankana, rimwe na rimwe bishobora gushika ikintu kigahagarika gukora, kenshi ivyo bizokwitorera umuti mu masaha makeyi. Mu gihe co gusenyuka kwose dushobora kugerageza gusubira kuyitangura n'itegeko:



```bash
python tumbler.py --restart
```



Canke gusa wongere utangure itegeko rishasha ry’ugutera. Ivyo ntibizotangura gutegura igikombe c’imbere ariko bizotangura urugendo rushasha rwo kuvanga. Mu gihe gufunga terminal ya SSH ku node yawe navyo bihagarika inyandiko ushobora gukoresha porogarama ya `TMUX` ishobora gushirwamwo n'itegeko:



```bash
sudo apt install tmux
```



Kuyitanguza ukoresheje shell wandika `tmux` bizokugururira terminal izoguma ikora mu nyuma naho woba wafunze ihuriro ryo kure. Iyo usubiye gufatanya n'urudodo rwawe n'itegeko: `tmux attach` uzosubira gufungura igikoko cagumye gikora inyuma.



## Iciyumviro



JoinMarket ni porogaramu itagira aho igarukira kandi ishobora guhindurwa. Muri iyi nkuru twabonye ibikorwa nyamukuru kugira ngo umuntu wese (canke n’imiburiburi naragerageje, ndabona ko gukoresha iyi porogarama atari ugutembera muri pariki) ashobore kuyikoresha. Kimwe mu bibazo bikomeye vya JoinMarket ni ivyo gusa: umubare w’abantu bayikoresha no kuba umuhinguzi. Iyo abakoresha bakeyi bakoresheje iyo porogarama, ubuzima bwite muri rusangi (anon-set) buragabanywa. Ni co gituma nizigiye ko iyi nkuru izotuma mukoresha kandi ikakwemeza ko mushobora gukura no gushiramwo porogarama nkunda cane kugira ngo mukore CoinJoin. Mu gihe woba ushaka kuja mbere n’imbere cane mu mice imwe imwe ndagusavye gutanga igisomwa ku nyandiko zitandukanye zijanye n’ivy’imbere kuri github, ni vermanete zikozwe neza kandi ushobora kuzisanga hano.



Ivyiza vyo kuvanga inzoka!🐢 💚



[Hano](https/btcpay.priorato.org/api/v1/invoices?Id y'ububiko=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&amahera=EUR) ushobora gushigikira Turtlecute