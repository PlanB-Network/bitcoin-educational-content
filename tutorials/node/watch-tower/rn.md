---
name: Lightning Watchtower
description: Gutahura no gukoresha Watchtower ku nzira yawe y'umuravyo
---
![cover](assets/cover.webp)



## None Iminara y’Inderetsi ikora gute?



Igice gihambaye c'ibidukikije vya Lightning Network, _Watchtowers_ itanga urugero rwongerekanye rw'uburinzi ku mirongo y'umuravyo y'abakoresha. Uruhara rwabo nyamukuru ni ugukurikirana uko umurongo uri no gufasha iyo uruhande rumwe rw’umurongo rugerageza guhenda urundi.



Ni gute Watchtower ishobora kumenya nimba umurongo wacitse intege? Ironka ku mukiriya (umwe mu bagize iyo nzira) amakuru akenewe kugira ngo imenye neza kandi ikoreshe ukurenga ku mategeko kwose. Aya makuru arimwo amakuru y’ido n’ido y’ugucuruza guherutse gukorwa, uko umurongo uri ubu, na Elements isabwa kugira ngo umuntu ashobore gucuruza ibihano. Imbere yo gutanga ayo makuru kuri Watchtower, umukiriya arashobora kuyashiramwo amakuru kugira ngo azigame ibanga. Rero, naho Watchtower yoronka ayo makuru, ntizoshobora kuyafungura gushika habayeho ukurenga ku mategeko vy’ukuri. Ubwo buryo bwo gupfuka amakuru burakingira ubuzima bwite bw’umukiriya kandi bukabuza Watchtower kuronka amakuru y’agaciro ata wemerewe.



Muri iyi nyigisho, turaza kuraba uburyo 3 bwo gukoresha **Watchtower** :




- mbere, uburyo bwa kera butagiramwo ibinure biciye kuri LND,
- hanyuma ubundi buryo bukoresheje Ijisho rya Satoshi,
- kandi mu nyuma, ugutunganya kworoshe kwa Watchtower ku nzira yawe ya Lightning yakiriwe na Umbrel.



## 1 - Gutegura Watchtower canke umukiriya biciye kuri LND



*Iyi nyigisho yakuwe muri [inyandiko zizwi za LND] Hari ivyo bishobora kuba vyahinduwe kuri verisiyo y'intango .



Kuva v0.7.0, `LND` ishigikira ugushirwa mu ngiro kwa Watchtower nk'uburyo bushitse bwa `LND`. Iminara y’abagenzuzi itanga umurongo wa kabiri wo kwikingira ibintu bibi canke ivy’uguhungabanya amategeko igihe urudodo rw’abaguzi rutari ku murongo canke rudashobora kwishura mu gihe c’uguhungabanya amategeko, bikaba bitanga urugero rwongerekanye rw’umutekano ku mahera y’umuhora.



Udakunze _umunara w’impera_, usaba umugabane w’amahera y’umurongo mu gusubiza igikorwa cawo, _umunara w’ubugwaneza_ usubiza amahera yose y’uwagirizwa (ukurako amafaranga y’i On-Chain) ata komisiyo usaba. Iminara y’ibarabara y’impera izokoreshwa mu gihe kizoza; baracari mu rwego rwo kugerageza no kunoza.



Ikindi, `LND` ubu irashobora gutunganirizwa gukora nk'umukiriya w'umunara w'abacungera_, igakiza amafaranga yo gutorera umuti ibibazo (ivyo bita "amafaranga y'ubutungane") avuye mu yindi minara y'abacungezi y'ubugwaneza. Watchtower ibika amabara apfutse afise ubunini butahinduka kandi ishobora gusa gufungura no gutangaza ivy’ubutungane inyuma y’aho uwukoze icaha amaze gutangaza igihugu ca Commitment cakuweho. Umukiriya ↔ Ivyiyumviro vya Watchtower birashirwa mu nzira kandi bikemezwa hakoreshejwe urufunguzo rw’igihe gito, ivyo bikaba bigabanya ubushobozi bwa Watchtower bwo gukurikirana abakiriya bayo biciye ku bimenyetso vy’igihe kirekire.



Zirikana ko twahisemwo gukoresha muri iki gisohoka ibintu bikeyi bimaze gutanga umutekano mwinshi ku bakoresha `LND`. Ibindi bintu vyinshi bijanye na Watchtower biri hafi kurangira canke birateye imbere cane; tuzobandanya tuzitanga uko tuzigerageza, kandi zizoba zibonwa ko zitekanye.



iciyumviro: ubu, iminara y'abagenzuzi ibika gusa `to_local` na `to_remote` umusohoka w'amasezerano yasubiwemwo; kubika HTLC igisohoka kizokoreshwa muri verisiyo izoza, nk'uko porotokole ishobora kwaguka kugira ngo ishiremwo amakuru y'inyongera y'umukono mu bice vy'ibanga._



### Gutegura Watchtower



Kugira ngo ushireho Watchtower, abakoresha umurongo w'amabwirizwa barakeneye gukoranya umukozi mutoyi `watchtowerrpc`, wemerera gukorana na Watchtower biciye kuri gRPC canke `lncli`. Ivyasohowe birimwo `watchtowerrpc` umukozi mutoyi ku buryo busanzwe.



Igishushanyo gitoyi co gukoresha Watchtower ni `Watchtower.ikora=1`.



Ushobora kugarura amakuru y'imiterere ya Watchtower yawe ukoresheje `amakuru y'umunara wa lncli` :



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



Ivyiyumviro vyose vy'imiterere ya Watchtower biraboneka biciye ku `LND -h` :



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



#### Gutega yompi ibigaragara



Ku mburabuzi, Watchtower yumviriza kuri `:9911`, ihuye n'icuma `9911` ku mirongo yose iriho. Abakoresha bashobora gusobanura imirongo yabo yo kwumviriza biciye ku `--Watchtower.listen=`. Ushobora kugenzura imiterere yawe mu `"abatega yompi"` umwanya wa `lncli tower info`. Niba ufise ingorane zo kwifatanya na Watchtower yawe, menya neza ko `<port>` yuguruye canke ko proxy yawe itunganijwe neza kuri Interface ikora.



#### Aderesi za IP zo hanze



Abakoresha bashobora kandi gusobanura IP y'inyuma ya Watchtower Address(s) n'`Watchtower.externalip=`, igaragaza URI yuzuye ya Watchtower (pubkey@host:port) biciye kuri RPC canke `amakuru y'umunara wa lncli` :



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Watchtower URIs zishobora kumenyeshwa abakiriya kugira ngo bahuze kandi bakoreshe n'itegeko rikurikira:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Niba abakiriya ba Watchtower bakeneye kuyironka kure, urabe ko :




- Gufungura icuma 9911 (canke icuma gisobanuwe biciye ku `Watchtower.umviriza`).
- Koresha proxy kugira ngo uhindure uruja n'uruza ruva ku cambu kigutse ruje kuri Address yumviriza Address.



#### Ibikorwa vya Tor vyihishijwe



Watchtowers ishigikira ibikorwa vyihishijwe vya Tor kandi ishobora kwihitiramwo generate imwe mu gutangura n’amahitamwo akurikira:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



Igitunguru Address rero kigaragara mu `"uris"` umwanya mu gihe c'ikibazo c'amakuru y'umunara wa lncli:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



iciyumviro: urufunguzo rwa bose rwa Watchtower rutandukanye n'urufunguzo rwa bose rw'uruzitiro rwa `LND`. Kugeza ubu, ikora nk'"urutonde rwera rwa Soft", kuko abakiriya bakeneye kumenya urufunguzo rwa bose rwa Watchtower kugira ngo bayikoreshe nk'ububiko, barindiriye uburyo bwo gushiramwo urutonde rwera buteye imbere. Turagusavye KUTAmenyesha urufunguzo rwa bose ku mugaragaro, kiretse witeguriye gushikiriza Watchtower yawe kuri Internet yose._



#### Ububiko bw'urutonde rwa Watchtower



Urutonde rw'amakuru rwa Watchtower rushobora kwimurirwa hakoreshejwe uburyo bwa `Watchtower.towerdir=`. Zirikana ko `/Bitcoin/Mainnet/Watchtower.db` izokwongerwa ku nzira yatowe kugira ngo utandukanye amakuru n'urudodo. Gutyo, gushinga `Watchtower.umunara=/inzira/ku/umunara` bizoteza imbere urutonde rw'amakuru kuri `/inzira/ku/umunara/Bitcoin/Mainnet/Watchtower.db`.



Munsi ya Linux, nk'akarorero, urutonde rw'amakuru rwa Watchtower ruri kuri :


`/inzu/$UMUKORESHA/.LND/amakuru/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Gutunganya umukiriya wa Watchtower



Kugira ngo utunganye umukiriya wa Watchtower, ukeneye ibintu bibiri:





- Gukoresha umukiriya wa Watchtower n'uburyo bwa `--wtclient.active`.



```shell
$  lnd --wtclient.active
```





- URI ya Watchtower ikora.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Ushobora gutunganya iminara myinshi y’ibarabara muri ubwo buryo.



#### Ibiciro vy'amafaranga y'ibikorwa vyemewe n'amategeko



Abakoresha bashobora gushinga igiciro c'amafaranga y'ubutungane biciye ku mahitamwo ya `wtclient.sweep-fee-rate`, yemera agaciro muri sat/byte. Agaciro ka mbere ni 10 sat/byte, ariko birashoboka ko umuntu ashaka ibiciro vyinshi kugira ngo ashike ku ntumbero nyinshi mu gihe c’amahera menshi. Guhindura `igiciro c'amahera yo gukubura` bikoreshwa ku bishasha vyose inyuma y'aho daemon isubiye gutangura.



#### Ubugenzuzi



Hamwe n'itegeko rya `lncli wtclient`, abakoresha ubu barashobora gukorana n'umukiriya wa Watchtower kugira ngo baronke canke bahindure amakuru ku minara yose y'ibarabara yanditswe.



Nk'akarorero, na `lncli wtclient tower`, urashobora kumenya umubare w'ibiganiro ubu biriko biraganirwako na Watchtower yongewe haruguru maze ukamenya nimba iriko irakoreshwa mu gusubiza inyuma biciye ku mwanya wa `active_session_candidate`.



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



Kugira ngo uronke amakuru ku biganiro vya Watchtower, koresha uburyo bwa `--include_sessions`.



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



Amahitamwo yose y'imiterere y'umukiriya wa Watchtower araboneka biciye kuri `lncli wtclient -h` :



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




## 2 - Gushiramwo Ijisho ryawe rya Satoshi



*Iyi nyigisho ivuye mu ngingo iri ku rubuga rwa [Ici ca Bitcoin Blog](https://blog.summerofbitcoin.org/). Hariho ivyo bahinduye kuri verisiyo y'intango*



Ijisho rya Satoshi ([Rust-TEOS]) ni umuravyo Watchtower udafise ububiko, uhuye n’[Bolt]. 13](blog.com/sr-gi/bolt13/blob/master/13-iminara y'abacungera. Gigizwe n’ibice bibiri nyamukuru:





- teos**: harimwo umurongo w'amabwirizwa Interface (CLI) n'ibiranga umukozi w'ingenzi wa Watchtower. Ivyiyumviro bibiri - **teosd** na **teos-CLI** - birasohoka iyo iyi _sandugu_ ikozwe hamwe.





- teos-common**: irimwo imikorere y'uruhande rwa server n'iy'umukiriya (ifasha mu kurema umukiriya).



Kugira ngo ukoreshe neza Watchtower, ukeneye gukoresha **bitcoind** imbere yo gutanguza Watchtower ukoresheje itegeko **teosd**. Imbere yo gukoresha aya mabwirizwa abiri, ukeneye gutunganya dosiye yawe **Bitcoin.conf**. Ehe ingene wobikora:





- Shiraho Bitcoin core uhereye ku nzira canke uyikureko. Uhejeje gukuraho, shira dosiye **Bitcoin.conf** mu bubiko bw'abakoresha bwa Bitcoin core. Raba iyi nzira kugira uronke ibindi bisobanuro ku bijanye n'aho woshira dosiye, kuko ivyo bivana n'uburyo bwo gukoresha.





- Aho hantu hamaze kumenyekana, wongereko amahitamwo akurikira:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- umukozi**: ku bisabwa vya RPC





- rpcuser** na **ijambobanga rpc**: kwemeza abaguzi ba RPC kuri server





- regtest**: ntibisabwa, ariko ni ngirakamaro nimba uriko urategura iterambere.



Ivyiza vya **rpcuser** na **ijambobanga rpc** ni wewe ubihitamwo. Bitegerezwa kwandikwa ata n’ibimenyetso vy’ugusubiramwo. Nk'akarorero:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



None, iyo ukoresheje **bitcoind**, urudodo rukwiye gutangura.





- Ku gice ca Watchtower, utegerezwa kubanza gushiramwo **teos** uhereye ku nkomoko. Kurikiza amabwirizwa atangwa muri iyi link.





- Umaze gushiramwo neza **teos** kuri sisitemu yawe maze ugakora ibigeragezo, urashobora kuja ku ntambwe ya nyuma: gushinga dosiye **teos.toml** mu bubiko bw'abakoresha ba teos. Dosiye ikwiye gushirwa muri dosiye yitwa **.teos** (menya akadomo) munsi y'ububiko bwawe bw'i muhira. Nk'akarorero, **/inzu//.teos** munsi ya Linux. Igihe ahantu habonetse, rema dosiye **teos.toml** maze ushireho aya mahitamwo ajanye n'amahinduka yakozwe kuri **bitcoind** :



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



Zirikana ko aha, izina ry'ukoresha n'ijambobanga bitegerezwa kwandikwa **mu bimenyetso vy'ugusubiramwo**. Ukoresheje akarorero ka mbere :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



Ivyo bimaze gukorwa, ukwiye kuba witeguriye gutanguza Watchtower. Kubera ko turiko turakoresha **regtest**, birashoboka ko ata mabuye yacukuwe ku rubuga rwacu rwo kugerageza Bitcoin igihe Watchtower yatangura gufatanya (niba vyariho, hari ikintu kitagenda neza). Watchtower yubaka ububiko bw’imbere bw’ibice 100 vya nyuma vya **bitcoind**; rero, ku gutangura kwa mbere, ushobora kuronka ikosa rikurikira:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Kubera ko turiko turakoresha **regtest**, turashobora guhagarika Miner mu gutanga itegeko rya RPC, tutabwirizwa kurindira igihe c'iminota 10 c'imbere kiboneka ku zindi nzira (nka Mainnet canke Testnet). Raba **bitcoin-cli** imfashanyo ku bijanye n'ingene wokora amabuye ya Miner.



![Image](assets/fr/01.webp)



Ivyo nivyo vyose: warashoboye gukoresha neza Watchtower. Urakoze cane. 🎉




## 3 - Gutegura Watchtower ku Mutaka



Ku Umbrel, gufatanya na Watchtower kugira ngo ukinge urudodo rwawe rw'umuravyo biroroshe cane, kuko vyose bikorwa biciye ku gishushanyo Interface. Amaze gufatanya n'uruzitiro rwawe, fungura porogaramu "**Uruzitiro rw'umuravyo**".



![Image](assets/fr/02.webp)



Fyonda ku tudodo dutatu turi hejuru iburyo bwa Interface, hanyuma uhitemwo "**Imiterere iteye imbere**".



![Image](assets/fr/03.webp)



Mu "**Watchtower**", hariho uburyo bubiri:





- Watchtower Service**: iyi nzira ishobora kugufasha gukoresha Watchtower, ni ukuvuga igikorwa kigenzura imirongo y’izindi nzira kugira ngo umenye ubuhendanyi bwose bugeragejwe. Iyo habaye ukurenga, Watchtower yawe iratangaza ivy’ugucuruza kuri Blockchain, bikaba bishoboza abakoresha gusubirana amahera yabo yafunzwe. Iyo imaze gukoreshwa, URI ya Watchtower yawe iraboneka kandi ishobora kumenyeshwa izindi node kugira ngo zishobore kuyishira ku mukiriya wabo wa Watchtower;





- Watchtower Client**: iyi nzira ishobora kugufasha kwifatanya n’iminara y’inyuma kugira ngo ukinge imirongo yawe bwite. Iyo imaze gukoreshwa, urashobora kwongerako ibikorwa vya Watchtower aho node yawe izorungika amakuru akenewe yerekeye imirongo yayo. Ivyo bibanza vy’abacungera umutekano bizoca bikurikirana uko bimeze, bifashe ingingo iyo habayeho ubuhendanyi.



Ico ubanza gukora ni ugukoresha *Watchtower Client* kugira ngo ukinge node yawe, ariko ndagusavye kandi gukoresha *Watchtower Service* kugira ngo ushiremwo umusanzu mu mutekano w'abandi bakoresha mu gusubiza.



![Image](assets/fr/04.webp)



Hanyuma ukande kuri buto ya Green "**Bika kandi usubire gutangura Node**". LND yawe izosubira gutangura.



Muri iyo menyu nyene, uzosanga kandi URI ya serivisi yawe ya Watchtower nimba warayikoresheje. Ushobora kandi kwongerako URI ya Watchtower yo hanze kugira ngo ukinge imirongo yawe. Fyonda kuri "**ADD**" kugira ngo wemeze.



![Image](assets/fr/05.webp)



Hariho Iminara y’Inderetsi myinshi iboneka kuri Internet. Nk’akarorero, [LN+ na Voltage bitanga Watchtower y’ubugwaneza](Watchtower) ushobora gufatanya nayo:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



Iyindi nzira ni ugukora Exchange Watchtower URI yawe n’abagenzi bawe ba bitcoiners, kugira ngo umwe wese akingire node y’uwundi.



Ndabahimiriza kandi gushinga Iminara y’Inderetsi myinshi kugira ngo mugabanye ingorane mu gihe imwe muri zo yoba itaboneka.



Ubwa nyuma, urashobora guhindura "**Igiciro c'amahera yo gukubura umukiriya wa Watchtower**". Ivyo bisigura igipimo c’amahera menshi cane wifuza kwishura ku bijanye n’ugucuruza igihano co gutangaza Watchtower kugira ngo ushire mu gice. Raba neza ko ushizeho agaciro kanini bihagije, gahuye n’amahera yugarijwe mu mirongo yawe.