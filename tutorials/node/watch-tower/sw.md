---
name: Lightning Watchtower
description: Kuelewa na kutumia Watchtower kwenye nodi yako ya Umeme
---
![cover](assets/cover.webp)



## Mnara wa Mlinzi hufanyaje kazi?



Sehemu muhimu ya mfumo ikolojia wa Lightning Network, _Watchtowers_ hutoa kiwango cha ziada cha ulinzi kwa chaneli za Umeme za watumiaji. Jukumu lao kuu ni kufuatilia hali ya kituo na kuingilia kati ikiwa upande mmoja wa kituo unajaribu kulaghai mwingine.



Je, Watchtower inawezaje kubaini iwapo kituo kimeathiriwa? Inapokea kutoka kwa mteja (mmoja wa wahusika kwenye chaneli) habari inayohitajika ili kutambua kwa usahihi na kushughulikia ukiukaji wowote. Maelezo haya yanajumuisha maelezo ya shughuli ya hivi majuzi zaidi, hali ya sasa ya kituo, na Elements inayohitajika ili kuunda miamala ya adhabu. Kabla ya kusambaza data hii kwa Watchtower, mteja anaweza kuisimba kwa njia fiche ili kuhifadhi usiri. Kwa hivyo, hata kama Watchtower itapokea data, haitaweza kuiondoa hadi uvunjaji umetokea. Utaratibu huu wa usimbaji fiche hulinda faragha ya mteja na huzuia Watchtower kupata ufikiaji usioidhinishwa wa taarifa nyeti.



Katika somo hili, tutaangalia njia 3 za kutumia **Watchtower** :




- kwanza, njia mbichi ya asili kupitia LND,
- kisha mbinu nyingine na Jicho la Satoshi,
- na hatimaye, usanidi uliorahisishwa wa Watchtower kwenye nodi yako ya Umeme iliyopangishwa na Umbrel.



## 1 - Kusanidi Watchtower au mteja kupitia LND



*Mafunzo haya yamechukuliwa kutoka [hati rasmi ya LND](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md). Baadhi ya mabadiliko yanaweza kuwa yamefanywa kwa toleo asili



Tangu v0.7.0, `LND` inasaidia utekelezaji wa Watchtower ya kibinafsi kama mfumo mdogo uliounganishwa kikamilifu wa `LND`. Watchtowers hutoa safu ya pili ya ulinzi dhidi ya matukio ya ukiukaji hasidi au kwa bahati mbaya wakati nodi ya mteja iko nje ya mtandao au haiwezi kujibu wakati wa uvunjaji, ikitoa kiwango cha juu cha usalama kwa fedha za kituo.



Tofauti na _reward watchtower_, ambayo hudai mgao wa fedha za kituo ili kurejesha huduma yake, _altruist watchtower_ hurejesha pesa zote za mwathiriwa (bila ada za On-Chain) bila kutoza tume. Minara ya malipo itawashwa katika toleo la baadaye; bado wako katika hatua ya majaribio na uboreshaji.



Kwa kuongeza, `LND` sasa inaweza kusanidiwa kufanya kazi kama mteja wa _watchtower_, kuhifadhi miamala iliyosimbwa ya kurekebisha ukiukaji (kinachojulikana kama "shughuli za haki") kutoka kwa minara mingine ya uangalizi. Watchtower huhifadhi vitone vilivyosimbwa vya saizi isiyobadilika na inaweza tu kusimbua na kuchapisha shughuli ya haki baada ya mhusika kutangaza hali iliyobatilishwa ya Commitment. Mteja ↔ Mawasiliano ya Watchtower husimbwa kwa njia fiche na kuthibitishwa kwa kutumia jozi za funguo za muda mfupi, jambo ambalo linazuia uwezo wa Watchtower kufuatilia wateja wake kupitia kitambulisho cha muda mrefu.



Kumbuka kuwa tumechagua kutumia katika toleo hili seti ndogo ya vipengele ambavyo tayari vinatoa usalama mkubwa kwa watumiaji wa `LND`. Vipengele vingine vingi vinavyohusiana na Watchtower ama viko karibu kukamilika au vya hali ya juu; tutaendelea kuzitoa kadri tunavyozijaribu, na mara tu zitakapoonekana kuwa salama.



kumbuka: kwa sasa, minara ya ulinzi huhifadhi tu matokeo ya `kwa_ndani` na `kwa_mbali` ya ahadi zilizobatilishwa; kuokoa pato la HTLC kutatumiwa katika toleo la baadaye, kwa kuwa itifaki inaweza kupanuliwa ili kujumuisha data ya ziada ya sahihi katika vitone vilivyosimbwa._



### Kusanidi Watchtower



Ili kusanidi Watchtower, watumiaji wa mstari wa amri wanahitaji kujumuisha seva ndogo ya hiari ya `watchtowerrpc`, ambayo inaruhusu mwingiliano na Watchtower kupitia gRPC au `lncli`. Nambari za jozi zilizochapishwa ni pamoja na seva ndogo ya `watchtowerrpc` kwa chaguo-msingi.



Usanidi wa chini kabisa wa kuwezesha Watchtower ni `Watchtower.active=1`.



Unaweza kuepua maelezo yako ya usanidi wa Watchtower kwa `lncli tower info` :



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



Seti kamili ya chaguo za usanidi wa Watchtower inapatikana kupitia `LND -h` :



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



#### Violesura vya kusikiliza



Kwa chaguomsingi, Watchtower inasikiza kwenye `:9911`, ambayo inalingana na mlango `9911` kwenye violesura vyote vinavyopatikana. Watumiaji wanaweza kufafanua violesura vyao vya kusikiliza kupitia chaguo la `--Watchtower.listen=`. Unaweza kuangalia usanidi wako katika sehemu ya `"wasikilizaji"` ya `maelezo ya mnara wa lncli`. Ikiwa unatatizika kuunganisha kwenye Watchtower yako, hakikisha kwamba `<port>` imefunguliwa au seva mbadala yako imesanidiwa ipasavyo kuwa Interface inayotumika.



#### Anwani za IP za nje



Watumiaji wanaweza pia kubainisha IP ya nje ya Watchtower Address(es) na `Watchtower.externalip=`, ambayo inafichua URI kamili ya Watchtower (pubkey@host:port) kupitia RPC au `lncli tower info` :



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



URI za Watchtower zinaweza kuwasilishwa kwa wateja ili kuunganishwa na kutumia kwa amri ifuatayo:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Ikiwa wateja wa Watchtower wanahitaji kuipata kwa mbali, hakikisha:




- Fungua mlango wa 9911 (au mlango uliofafanuliwa kupitia `Watchtower.listen`).
- Tumia proksi kuelekeza upya trafiki kutoka mlango wazi hadi Address ya Address ya kusikiliza.



#### Tor huduma zilizofichwa



Watchtowers inasaidia huduma zilizofichwa za Tor na inaweza kiotomatiki generate moja inapoanzisha na chaguo zifuatazo:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



Kisha .onion Address inaonekana katika sehemu ya `"uris"` wakati wa hoja ya `lncli tower info`:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



kumbuka: ufunguo wa umma wa Watchtower ni tofauti na ufunguo wa umma wa nodi ya `LND`. Kwa sasa, inafanya kazi kama "orodha ya walioidhinishwa ya Soft", kwa vile wateja wanahitaji kujua ufunguo wa umma wa Watchtower ili kuutumia kama hifadhi rudufu, ikisubiri mbinu za juu zaidi za uidhinishaji. Tunapendekeza USIFUNGE ufunguo huu wa umma kwa uwazi, isipokuwa kama uko tayari kufichua Watchtower yako kwenye Mtandao mzima._



#### Watchtower orodha ya hifadhidata



Hifadhidata ya Watchtower inaweza kuhamishwa kwa kutumia chaguo la `Watchtower.towerdir=`. Kumbuka kuwa kiambishi tamati `/Bitcoin/Mainnet/Watchtower.db` kitaongezwa kwenye njia iliyochaguliwa ili kutenga hifadhidata kwa mfuatano. Kwa hivyo, kuweka `Watchtower.towerdir=/path/to/towerdir` kutazalisha hifadhidata katika `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`.



Chini ya Linux, kwa mfano, hifadhidata chaguo-msingi ya Watchtower iko katika:


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Inasanidi mteja wa Watchtower



Ili kusanidi mteja wa Watchtower, unahitaji vitu viwili:





- Washa kiteja cha Watchtower kwa chaguo `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- URI ya Watchtower inayotumika.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Unaweza kusanidi minara kadhaa kwa njia hii.



#### Viwango vya ada kwa shughuli za kisheria



Watumiaji wanaweza kuweka kwa hiari kiwango cha ada kwa miamala ya haki kupitia chaguo la `wtclient.sweep-fee-rate`, ambalo linakubali thamani katika sat/byte. Thamani chaguo-msingi ni 10 sat/byte, lakini inawezekana kulenga viwango vya juu ili kufikia kipaumbele cha juu wakati wa gharama za juu zaidi. Kubadilisha `kiwango cha ada ya kufagia` hutumika kwa masasisho yote mapya baada ya kuanza tena kwa daemon.



#### Usimamizi



Kwa amri ya `lncli wtclient`, watumiaji sasa wanaweza kuingiliana moja kwa moja na mteja wa Watchtower ili kupata au kurekebisha maelezo kuhusu minara yote ya uangalizi iliyosajiliwa.



Kwa mfano, ukitumia `lncli wtclient tower`, unaweza kujua idadi ya vipindi vinavyojadiliwa kwa sasa na Watchtower iliyoongezwa hapo juu na ubaini kama inatumika kwa hifadhi rudufu kwa uga wa `amilishi_session_candidate`.



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



Ili kupata maelezo kuhusu vipindi vya Watchtower, tumia chaguo la `--include_sessions`.



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



Chaguo zote za usanidi wa mteja wa Watchtower zinapatikana kupitia `lncli wtclient -h` :



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




## 2 - Kuweka Jicho lako mwenyewe la Satoshi



*Mafunzo haya yametolewa kwa sehemu kutoka kwa makala kuhusu [Majira ya joto ya Blogu ya Bitcoin](https://blog.summerofbitcoin.org/). Marekebisho yamefanywa kwa toleo asilia*



Jicho la Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) ni Umeme usio na hazina wa Watchtower, unaolingana na [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org). Inajumuisha sehemu kuu mbili:





- teos**: inajumuisha mstari wa amri Interface (CLI) na vipengele muhimu vya seva vya Watchtower. Pembe mbili - **teosd** na **teos-CLI** - hutolewa wakati _crate_ hii inapokusanywa.





- teos-common**: inajumuisha utendakazi wa upande wa seva na upande wa mteja (muhimu kwa kuunda mteja).



Ili kuendesha Watchtower kwa usahihi, unahitaji kukimbia **bitcoind** kabla ya kuzindua Watchtower kwa amri ya **teosd**. Kabla ya kutekeleza amri hizi mbili, unahitaji kusanidi faili yako **Bitcoin.conf**. Hapa ni jinsi ya kufanya hivyo:





- Sakinisha Bitcoin core kutoka kwa chanzo au uipakue. Baada ya kupakua, weka faili ya **Bitcoin.conf** kwenye saraka ya mtumiaji wa Bitcoin core. Tazama kiunga hiki kwa habari zaidi juu ya mahali pa kuweka faili, kwani hii inategemea mfumo wa uendeshaji unaotumiwa.





- Mara tu eneo limetambuliwa, ongeza chaguzi zifuatazo:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- seva**: kwa maombi ya RPC





- rpcuser** na **rpcpassword**: thibitisha wateja wa RPC kwa seva





- regtest**: haihitajiki, lakini ni muhimu ikiwa unapanga maendeleo.



Thamani za **rpcuser** na **rpcpassword** zitachaguliwa na wewe. Lazima ziandikwe bila alama za nukuu. Kwa mfano:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



Sasa, ukiendesha **bitcoind**, nodi inapaswa kuanza.





- Kwa sehemu ya Watchtower, lazima kwanza usakinishe **teos** kutoka kwa chanzo. Fuata maagizo yaliyotolewa kwenye kiungo hiki.





- Mara baada ya kusakinisha **teos** kwa ufanisi kwenye mfumo wako na kufanya majaribio, unaweza kuendelea hadi hatua ya mwisho: kusanidi faili ya **teos.toml** katika saraka ya mtumiaji wa teos. Faili inapaswa kuwekwa kwenye folda inayoitwa **.teos** (kumbuka nukta) chini ya saraka yako ya nyumbani. Kwa mfano, **/home//.teos** chini ya Linux. Mara tu eneo limepatikana, unda faili **teos.toml** na uweke chaguo hizi kulingana na mabadiliko yaliyofanywa kwenye **bitcoind** :



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Kumbuka kuwa hapa, jina la mtumiaji na nenosiri lazima liandikwe **ndani ya alama za nukuu**. Kwa kutumia mfano uliopita:



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Mara hii imefanywa, unapaswa kuwa tayari kuzindua Watchtower. Kwa kuwa tunatumia **regtest**, kuna uwezekano kuwa hakuna vizuizi vilivyochimbwa kwenye mtandao wetu wa majaribio wa Bitcoin wakati Watchtower ilipounganishwa kwa mara ya kwanza (ikiwa walikuwa, kuna tatizo). Watchtower huunda hifadhi ya ndani ya vitalu 100 vya mwisho vya **bitcoind**; kwa hivyo, kwenye uzinduzi wa kwanza, unaweza kupata makosa yafuatayo:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Kwa kuwa tunatumia **regtest**, tunaweza kuzuia Miner kwa kutoa amri ya RPC, bila kusubiri ucheleweshaji wa wastani wa dakika 10 unaoonekana kwenye mitandao mingine (kama vile Mainnet au Testnet). Tazama usaidizi wa **bitcoin-cli** kwa maelezo ya jinsi ya kutengeneza vitalu vya Miner.



![Image](assets/fr/01.webp)



Ni hayo tu: umefanikiwa kuendesha Watchtower. Hongera sana. 🎉




## 3 - Kusanidi Watchtower kwenye Mwavuli



Kwenye Mwavuli, kuunganisha kwenye Watchtower ili kulinda nukta yako ya Umeme ni rahisi sana, kwani kila kitu hufanywa kupitia mchoro wa Interface. Baada ya kuunganisha kwa mbali kwenye nodi yako, fungua programu ya "**Njia ya Umeme**".



![Image](assets/fr/02.webp)



Bofya kwenye vitone vitatu kwenye sehemu ya juu ya kulia ya Interface, kisha uchague "**Mipangilio ya Juu**".



![Image](assets/fr/03.webp)



Katika menyu ya "**Watchtower**", chaguzi mbili zinapatikana:





- Huduma ya Watchtower**: chaguo hili hukuwezesha kutumia Watchtower, yaani, huduma inayofuatilia njia za nodi nyingine ili kugundua ulaghai wowote uliojaribiwa. Katika tukio la ukiukaji, Watchtower yako itachapisha muamala kwenye Blockchain, ili kuwawezesha watumiaji kurejesha pesa zao walizofunga. Mara baada ya kuanzishwa, URI yako ya Watchtower inaonekana na inaweza kuwasilishwa kwa nodi nyingine ili waweze kuiongeza kwa mteja wao wa Watchtower;





- Mteja wa Watchtower**: chaguo hili hukuwezesha kuunganisha kwenye minara ya nje ili kulinda chaneli zako mwenyewe. Mara baada ya kuanzishwa, unaweza kuongeza huduma za Watchtower ambazo nodi yako itasambaza taarifa muhimu kuhusu njia zake. Walinzi hawa watafuatilia hali yao na kuingilia kati katika tukio la jaribio la ulaghai.



Kipaumbele chako bila shaka ni kuwezesha *Mteja wa Watchtower* ili kulinda nodi yako, lakini pia ninapendekeza uwashe *Huduma ya Watchtower* ili kuchangia usalama wa watumiaji wengine kwa malipo.



![Image](assets/fr/04.webp)



Kisha bonyeza kitufe cha Green "** Hifadhi na Anzisha tena Node **". LND yako itaanza upya.



Katika menyu hiyo hiyo, utapata URI ya huduma yako ya Watchtower ikiwa umeiwasha. Unaweza pia kuongeza URI ya Watchtower ya nje ili kulinda vituo vyako. Bofya "**Ongeza **" ili kuthibitisha.



![Image](assets/fr/05.webp)



Kuna Mnara wa Mlinzi kadhaa unaopatikana mtandaoni. Kwa mfano, [LN+ na Voltage zinatoa Watchtower] (https://lightningnetwork.plus/Watchtower) ambayo unaweza kuunganisha kwayo:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Chaguo jingine ni Exchange Watchtower URI yako na bitcoiners wenzako, ili kila mmoja kulinda nodi ya mwingine.



Mimi pia kupendekeza kwamba kuanzisha Watchtowers kadhaa ili kupunguza hatari katika tukio la mmoja wao kuwa haipatikani.



Hatimaye, unaweza kurekebisha kigezo cha "**Watchtower Kiwango cha Ada ya Kufagia Mteja**". Hii inabainisha kiwango cha juu cha ada ambacho uko tayari kulipa kwa ajili ya muamala wa adhabu ya utangazaji wa Watchtower ili kujumuishwa kwenye kizuizi. Hakikisha umeweka thamani ya juu ya kutosha, iliyorekebishwa kwa kiasi kilichofungwa kwenye chaneli zako.