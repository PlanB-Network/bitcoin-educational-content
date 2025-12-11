---
name: Joinstr
description: CoinJoins yegerejwe biciye ku rubuga rwa Nostr ku bw'ibanga ry'ubutegetsi bwa Bitcoin
---

![cover](assets/cover.webp)



Uguseruka kw’uruzitiro rwa Bitcoin gutuma bishoboka gukurikirana amateka y’ibikorwa. CoinJoins zica ayo mahuza mu kuvanga amafaranga menshi akoreshwa icarimwe, zigasubizaho urugero rw’ibanga rugereranywa n’amahera.



Ariko rero, inyishu z’imigenzo zishingiye ku muhuzabikorwa mukuru nk’aho ari ikintu kimwe co kunanirwa. Wasabi na Samourai zahagaritse ibikorwa mu 2024 kubera igitutu c’abajejwe amategeko.



**Joinstr** ikuraho iyo ntege nke mu gukoresha urubuga rwa Nostr rwigenga kugira ngo habeho uguhuza. Iyi porogaramu y’inkomoko yuguruye ishobora gutuma CoinJoins zigira ubusegaba vy’ukuri, aho ata butegetsi bukuru bushobora gucengera, gukurikirana canke guhagarika igikorwa.



## Joinstr ni iki?



Joinstr ni igikoresho c’inkomoko yuguruye gihindura uburyo bwa CoinJoins mu gukoresha umurongo wa Nostr nk’ibikorwa remezo vy’uguhuza. Udakunze inyishu zihuriweko zisaba umukozi yihariye, Joinstr yizigira uruja n’uruza rw’ibikoresho vya Nostr kugira ngo abaje mu nama bashobore guhuza ata guca ku ruhande hagati y’urunganwe.



**Ubwubatsi bwegerejwe** : Urubuga rwa Nostr rusubirira umuhuzabikorwa wa mbere. Abaje mu nama barahingura canke bakifatanya n'"ibidengeri" mu gushiramwo amatangazo apfutse biciye ku nzira za Nostr. Aya makuru (amafaranga, abaje mu nama, amaderesi) aguma atamenyekana ku bamenyeshamakuru, kugira ngo ata kigo nyamukuru gishobora gukurikirana, gucengera canke gucungera CoinJoins.



**SIGHASH_ALL|Uburyo bwa ANYONECANPAY**: Joinstr ikoresha iri bendera ry'umukono wa Bitcoin, iremesha uwuriko arakora wese gusinya gusa ivyo yinjije mu gihe yemeza ivyo yinjije vyose. Buri muntu wese akoresha PSBT yiwe mu karere, hanyuma akayitanga biciye kuri Nostr. Uwukoresha wese akora PSBT yiwe mu karere, akayishirako umukono, hanyuma akayitanga biciye kuri Nostr. Bitcoins zawe ziguma munsi y’ububasha bwawe gusa gushika umukono wa nyuma.



**Filozofiya**: Joinstr ikurikira inyifato ya Bitcoin cypherpunk, igamije intumbero zitatu: **kurwanya ugucengera** (nta butegetsi bushobora guhagarika igikorwa), **ukudacungera vyose** (uzigama imfunguruzo zawe z’ibanga), na **gufatwa kimwe** (nta discrimin UTXO ishobora gufatwa).



### Ibirango nyamukuru



**Ibidengeri bishobora guhinduka**: Bitandukanye n’amashengero adahinduka, uwukoresha wese arashobora gukora ikidengeri gifise umubare nyawo yipfuza n’umubare w’abazoja muri iyo nama, bikaba bituma UTXO ikoreshwa neza ata gucapura kw’abantu.



**Amahera agaragara**: Nta mahera y’uguhuza ibikorwa. Amafaranga y’ugucuruza Bitcoin gusa ni yo asangira kimwe hagati y’abaje mu nama (ibihumbi bikeyi vy’amasatoshi ku muntu).



**Ubuzima**: Nta makuru y'abakoresha abikwa. Amakuru aca mu butumwa bwa Nostr bw’igihe gito bushizwemwo amakuru, bugaca bwibagirwa inyuma y’ugucuruza.



### Imbuga ziboneka



Iyi nyigisho yibanze ku **Iporogarama ya Android**, umuti umwe rudende ushikamye kandi ushimikwako ubu. Igikoresho ca Electrum kirahari ariko gifise ingorane zo guhuza bituma kidashikama. Urubuga ruriko rurategurwa.



## Bitcoin imiterere nyamukuru



Joinstr Android isaba guhuzwa n'uruzitiro rwa Bitcoin biciye ku nzira ya RPC. Utegerezwa kubanza gutegura Bitcoin Core kuri mudasobwa yawe kugira ngo wemere ama connexions ava kuri telefone yawe.



**Iciyumviro**: Kugira ngo umenye vyinshi ku bijanye n'imiterere yose ya Bitcoin Core, raba inyigisho zacu zihariye :



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Ibisabwa ku rubuga



#### Tora aderesi IP yawe yo mu karere



Telefone yawe ya Android itegerezwa kuba ishobora gushika ku nzira yawe ya Bitcoin iri ku rubuga rwo mu karere. Rondera aderesi IP ya mudasobwa yawe:



**Kuri macOS** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Ubundi buryo bworoshe:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**Kuri Linux** :



```bash
hostname -I | awk '{print $1}'
```



**Ku madirisha** :



```cmd
ipconfig
```



Rondera aderesi ya IPv4 (imiterere `192.168.x.x` canke `10.0.x.x`)



### RPC imiterere



#### Guhindura bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Rondera dosiye yawe `bitcoin.conf`:




- Linux**: `~/.ibiceri/bitcoin.conf
- macOS**: `~/Isoko ry'ibitabo/Ibikorwa/Bitcoin/bitcoin.conf
- Idirisha**: `%IBIMENYETSO%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Ugurure dosiye n'umuhinduzi w'inyandiko ukunda maze wongereko iyi ntunganyo kugira ngo ukoreshe umukozi wa RPC.



**Ivyiza vyo gutunganya kugira ngo utangure (ikimenyetso)** :



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



**mainnet** imiterere (ku gukoresha mu guhingura) :



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



**Bihambaye** :




- Signet iraremeshwa cane** ku bigeragezo vyawe vya mbere: porogaramu iracari mu gutegurwa (beta), kandi ibikoko bishobora kuba bikiriho. Signet iragufasha kugerageza ku buntu, ataco ushize mu kaga k’amahera nyayo
- Subiriza `192.168.1.0/24` n'urubuga rwawe (nk'akarorero nimba IP yawe ari `192.168.68.57`, koresha `192.168.68.0/24`)



**Umutekano**: Gutanga ijambobanga rikomeye :



```bash
openssl rand -base64 32
```



### Gutangura



#### Gusubira gutangura no kugenzura



1. Funga Bitcoin Core burundu


2. Subiramwo kugira ngo ukoreshe ivyategekanijwe




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Igihe Bitcoin Core izotangura ku ncuro ya mbere, izokuraho no gukorana n’ibindi bikoresho vy’ibara ry’agahama. Ivyo bikorwa vyihuta cane kuruta ivyo kuri mainnet (iminota mikeyi gusa). Urasabwa kurindira gushika uguhuza birangiye imbere y'uko ukomeza.



![CRÉATION DE WALLET](assets/fr/04.webp)



Igihe umaze gukorana, rema igitabo gishasha ukanda kuri "Rema wallet nshasha". Uyihe izina ritomoye nka `tuto_joinstr_signet`.



![WALLET CRÉÉ](assets/fr/05.webp)



wallet yawe ubu yararemwe kandi yiteguriye kwakira ama bitcoins yashizweko ikimenyetso kugira ngo ageragezwe.



#### Kuronka ama bitcoins yashizweko ikimenyetso (ikigeragezo)



Kugira ngo ugerageze Joinstr ku kimenyetso, ukeneye kugerageza bitcoins ku buntu :



![SIGNET FAUCET](assets/fr/06.webp)



Koresha ikimenyetso ca bose nka :




- [ikinyamakuru.com](https://ikinyamakuru.com)
- [iyindi.ikimenyetso.com](https://iyindi.ikimenyetso.com)
- [ikimenyetso c'igitabu257.igisagara cacu](ikimenyetso257.ikinyamakuru.org)



Muri Bitcoin Core, generate aderesi nshasha yo kwakira ("Kwakira" tab), uyikope maze uyishire mu rupapuro rw'amazi. Gutorera umuti captcha nimba bikenewe. Uzoronka ama bitcoins y’ubuntu mu masegonda makeyi.



## Porogaramu ya Android



### Gushiramwo



![APPLICATION ANDROID](assets/fr/07.webp)



Genda kuri [gitlab.com/ubuzima bwite-budashobora gutsindwa/joinstr-kmp/-/ibisohotse](https://gitlab.com/ubuzima bwite-budashobora gutsindwa/joinstr-kmp/-/ibisohotse) kugira ngo ubone verisiyo ya APK nshasha. Ku mucukumbuzi wawe wa Android, nushireko iyo dosiye, hanyuma uyifungure kugira ngo utangure kuyishiramwo. Uzokenera kwemera gushiramwo ibintu bivuye mu bibanza bitazwi mu mategeko y’umutekano wa telefone yawe nimba bikenewe.



### Gutunganya ibikorwa



![PERMISSIONS VPN](assets/fr/08.webp)



Ku gutangura kwa mbere, porogarama ya Joinstr izosaba uruhusha rwo kugenzura VPN yubatswemwo. Emera ivyo bisabwa vyose vy’uruhusha: OpenVPN ubugenzuzi n’uguhuza VPN. Ivyo vyemezo birakenewe kugira ngo VPN ikoreshe, ivyo bikaba bikingira ubuzima bwite bw’urubuga rwawe.



![INTERFACE APPLICATION](assets/fr/09.webp)



Porogaramu ya Joinstr itunganijwe mu bice bitatu nyamukuru:




- Inzu**: Igishushanyo c'inzu
- Ibidengeri**: Guhingura no gucunga ibidengeri vya CoinJoin
- Amagenamiterere**: Gutunganya porogaramu



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Gutunganya amagenamiterere mu "Magenamiterere" tab:



**1. Nostr Relay**: Aderesi ya Nostr yo guhuza ibidengeri




- Akarorero: `wss://ugutangaza.damus.io`
- Ibindi bimenyetso vyiza: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Igihambaye**: Abazoja muri iyo nama bose bategerezwa gukoresha **relay ya Nostr imwe** kugira ngo babone kandi baje mu bidengeri bimwe. Niwakoresha uburyo butandukanye, ntuzobona ibidengeri vyakozwe ku bindi bikoresho



**2. URL y'uruzitiro**: Aderesi IP y'uruzitiro rwawe rwa Bitcoin (ata port)




- Uburyo: `http://AMATORA_IP_IGIHUGU`
- Akarorero: `Ikinyamakuru 192.168.68.57`



**3. RPC Izina ry'ukoresha** : Izina ry'ukoresha ryatunganijwe muri `rpcuser=` kuri bitcoin.conf yawe




- Akarorero: `satoshi



**4. Ijambobanga rya RPC** : Ijambobanga ryashizwe muri `rpcijambobanga=` kuri bitcoin.conf yawe



**5. Icuma ca RPC** : Icuma ca RPC bivanye n'urubuga




- Mainnet** : '8332'
- Ikimenyetso**: `38332`



**6. Wallet**: Hitamwo igitabo ca Bitcoin Core kirimwo ama UTXO azovangwa




- Akarorero: `tuto_gufatanya_ikidodo`



**7. Umuryango wa VPN**: Hitamwo umukozi wa VPN




- Akarorero: `(Parisi) vpn07-guhaguruka.urubuga`
- Ibindi biraboneka: Amsterdam, Seattle, n’ibindi.
- ⚠️ **Igihambaye**: Abazoja muri pool imwe bose bategerezwa gukoresha **VPN Gateway imwe** kugira ngo baje muri CoinJoin. Mu gihe c’urugendo rwo guvanga, abaje mu nama bose bategerezwa kugaragara bafise aderesi IP imwe yo gusohoka kugira ngo ntihagire isesengura ry’urubuga rihuza abaje mu nama .



Igikoresho ca Joinstr **kifatanya mu buryo bw’akavukire** Riseup VPN, kigatuma habaho uguhuza ibikorwa hagati y’abaje mu nama.



**Bihambaye** :




- Raba neza ko telefone yawe na mudasobwa yawe biri ku rubuga rumwe rwa WiFi
- Ihuriro rya VPN rizokwikora ubwaryo iyo uriko uragira uruhara mu kidengeri
- Fyonda kuri **"Bika"** umaze gushinga amaparametere yose



## Ikoreshwa ry'ingirakamaro



### Rema canke wifatanye n'ikidengeri



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Ufise uburyo bubiri bwo kuja muri CoinJoin:



**Ihitamwo rya mbere: Rema ikidengeri gishasha**



Fyonda kuri "Rema Pool nshasha" mu gice ca "Pools". Sobanura idini riri muri BTC (nk’akarorero 0.002 BTC) n’umubare wipfuza w’abazoja muri iyo nama (nibura 2, 3-5 kugira ngo umuntu ntamenyekane). Iryo koraniro rero ritegerezwa kurindira ko abandi bakoresha bifatanya n’ikidengeri cawe. Igihe umubare usabwa ugeze, igikorwa co kwandika gisohoka kiratangura ubwaco, kandi uzokenera guhitamwo UTXO yawe kugira ngo uyivange maze ukande kuri "Iyandikisha".



**⏱️ Ivy’agaciro**: Amapool arahera inyuma y’iminota **10** y’ukudakora. Iyo umubare w’abazoja muri iyo nama usabwa utashitse, iyo pool ica ifunga ubwayo.



**Ihitamwo rya 2: Kwifatanya n'ikidengeri kiriho**



Mu gice ca "Reba ibindi bidengeri", genda mu bidengeri biriho vyaremwe n'abandi bakoresha. Hitamwo ikidengeri gihuye n’amahera yawe maze ugishiremwo. Raba neza ko watunganije Nostr relay na VPN Gateway nk’abandi bari muri iyo nama (raba igice c’Itunganywa).



**Itegeko ryo guhitamwo UTXO**: UTXO yawe itegerezwa kuba hejuru gatoyi y’igiciro c’ikidengeri (hagati ya +500 na +5000 sats y’amasaranganya).



**Akarorero**: Ku kidengeri c'ama BTC 0,002 (200.000 sats), koresha UTXO iri hagati ya 200.500 na 205.000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Ivyo rero **bica vyikora**: iyo inyishu yawe imaze kwandikwa, iyo porogarama irindira ko abayigize bose bandika inyishu zabo. Ivyo vyose bimaze kwandikwa, PSBT iraremwa, igaca ishirwako umukono n’imfunguruzo zawe, hanyuma igafatanywa n’imikono y’abandi bari muri iyo nama. Ubwa nyuma, iyo nzira yose iratangazwa ku rubuga rwa Bitcoin. Uronka TXID (ikimenyetso c’ibikorwa) iyo ikiganiro kirangiye. Nta gukoresha amaboko kwa PSBT bisabwa kuri Android.



### on-chain kugenzura



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Iyo amafaranga amaze gutangazwa, uzoronka TXID (ikimenyetso c’amafaranga). Raba kuri [mempool.ikibanza](https://mempool.ikibanza) canke ku mucukumbuzi ukunda. Kugira ngo ugerageze ku kimenyetso c'igitabu, koresha [mempool.umwanya/ikidodo](https://mempool.umwanya/ikimenyetso).



Ushobora kwihweza :





- N entries**: Umwe ku muntu wese yitabira (mu karorero kacu, 2)
- N ibisohoka bisa**: umubare nyawo w’ibara (aha, ibisohoka 2 vya 0.00199800 BTC kuri kimwe cose)
- Igishushanyo c'urugendo**: mempool.space kigaragaza mu buryo bw'amaso uruvange rw'ibishirwamwo n'ibisohoka
- Ibirango** : Ivyo bishobora kumenyekana ko ari SegWit, Taproot, RBF, n’ibindi.



Nk'uko ibisohoka vyose bifise umubare umwe, **ntibishoboka ko umuntu amenya uwuhe ari uwa nde**. Iryo ni ryo hame ry’ishimikiro rya CoinJoin: ukudatandukanya ibisohoka.



**Akarorero k'ikidodo c'ubucuruzi** : 160bf63fca8c3b29be125e7360dbec44c] .ikibanza/ikidodo/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Iciyumviro**: Iyo UTXO zawe zari nini kuruta igiciro c’amahera y’ikidengeri, uzoba ufise amafaranga y’amahanga asohoka (amafaranga y’amahanga). Izo UTXO z’uguhanahana ziguma zishobora gukurikirana kandi zitegerezwa gucungirwa zitandukanye n’ibisohoka vyawe bitamenyekanye. Ntukigere ubifatanya n’ivyo usohora bivanze.



## CoinJoin uburyo n'amapaki y'ukutamenyekana



Ubushobozi bwa CoinJoin bupimwa n’**anonset** yayo: umubare w’ibisohoka vy’agaciro kamwe biva ku gucuruza. Uko uwo mubare urushiriza kuba munini, ni ko bigorana kumenya ivyo winjiza bihuye n’ivyo usohora.



Joinstr ubu itanga ama pools y'abantu **2 gushika kuri 5** ku rugero rwa mwayeni. Ivyo biharuro biri hasi y’abahuzabikorwa ba kera bo hagati nka Wasabi (abaje mu nama 50-100) canke Whirlpool (abaje mu nama 5-10), ariko ico ni co giciro co kwegereza ubutegetsi hagati.



💡 **Kugira ngo utahure amaseti y'ukutamenyekana n'uguharura kwayo mu buryo burambuye**, raba inyigisho yacu yuzuye: [Ukutamenyekana n’amashure y’isumbuye.



### Joinstr n'ibindi bihuza



| Aspect | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Participants par pool** | 50-100 | 5-10 | Variable (P2P) | **2-5** |
| **Coordinateur** | Centralisé (fermé 2024) | Centralisé (actif) | P2P maker/taker | **Aucun (Nostr)** |
| **Résistance à la censure** | Faible | Moyenne | Très élevée | **Très élevée** |
| **Frais de coordination** | Pourcentage | Frais d'entrée | Payés aux makers | **Aucun** |
| **Discrimination UTXO** | Oui (blacklists) | Non | Non | **Non** |

💡 **Ibindi bisubizo vya CoinJoin bikora** :




- Ashigaru**: Gushirwa mu ngiro kw’inkomoko yuguruye kw’amasezerano ya Whirlpool n’umuhuzabikorwa ari hagati ariko ashobora gukoreshwa mu buryo bushizwe ahantu hamwe. Ikomeza gukora inyuma y’aho Samourai Wallet ifashwe mu 2024.
- JoinMarket**: Umuti wa P2P wegerejwe ata muhuzabikorwa mukuru, ushingiye ku bucuruzi bw'umuhinguzi/uwufata aho "abahinguzi" batanga amafaranga kandi bagahembwa n'"abafata".



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Ivyiyumviro vy’ishimikiro**: Joinstr na JoinMarket ni vyo vyonyene bishobora gutorera umuti ata muhuzabikorwa wa mbere. JoinMarket ikoresha uburyo bw’ubudandaji bwa P2P bufise inkurikizi z’amahera, mu gihe Joinstr ikoresha Nostr mu guhuza ibikorwa ataco bimaze. Joinstr itanga ibimazi vy’ukutamenyekana kw’urugero runini kugira ngo bibe vyoroshe (nta burongozi bw’umuhinguzi/uwufata) no kutagira amahera yo guhuza ibikorwa.



**Impanuro ngirakamaro**: Kugira ngo ushobore gusubiza inyuma ibidengeri bitobito, nukore ibice vyinshi bikurikirana vya CoinJoin n’abantu batandukanye. Gutanga umwanya mu bice vyawe no guhindura Nostr relays hagati y’ibice vyose kugira ngo ukoreshe ibanga ryawe ryinshi.



Ushobora kuraba inyigisho yacu yose ku vyerekeye ubuzima bwite bwa bitcoin kugira uronke ibindi bisobanuro kuri iyi nkuru:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Inyungu n'aho bigarukira



### Ibintu bihambaye



**Ubuzima bwite bwongerewe**: Ihuriro ry’ububiko bw’itumanaho bwa Nostr, VPN isangiwe hagati y’abaje mu nama, n’ikoreshwa ryiza rya Tor rituma habaho uburinzi bw’ibice vyinshi bigoye kurenga.



**Ibiciro bigaragara, bike**: Nta giciro co guhuza ibikorwa, igiciro ca mining gusa ni co gisangira mu buryo bubereye hagati y’abaje mu nama. Nta ijana ry’ijanisha ry’umukoresha uwo ari we wese.



### Intambamyi zo kwihweza





- Ivyiyumviro bihinduka**: Ivyumba bitobito, bishobora kurindira ko abaje mu nama baza hamwe
- Umugambi uriko urakorwa**: Gukoresha muri beta, ibikoko birashoboka. Ugerageze mbere n'amahera makeyi ku kimenyetso
- Sybil attacks**: Bishoboka ko umunsi umwe ashobora kugenzura abaje mu pool benshi



## Ibikorwa vyiza



**Ukwitandukanya kwa UTXO**: Ntukigere ufatanya UTXO ivanze n’itavanze. Koresha igitabo gitandukanye ku bisohoka vyawe bitamenyekanye.



**Ivyiyumviro vyinshi birakenewe**: Kora nibura ivyifuzo 3 bikurikirana n’abantu batandukanye. Hindura ingero n’ibihe kugira ngo wirinde ivyitegererezo. Ikirere kizunguruka amasaha menshi kitandukanye.



**Ukurinda urubuga**: Koresha mu buryo bubereye Tor uretse VPN yubatswemwo. Gutanga imfunguruzo za Nostr z'igihe gito ku kiganiro cose gihambaye.



**Ugutera imbere mu kwiyubara**: Tangira gushiramwo ibitabu n’amahera makeyi.



## Iciyumviro



Joinstr iserukira umuti w’ubuzima bwite bwa Bitcoin vy’ukuri. Mu gukoresha Nostr mu guhuza ibikorwa, birakuraho ukuvyifatamwo neza mu guhuza ibikorwa hagati mu gihe bizigama ubusegaba bw’abakoresha.



**Ku bakoresha baha agaciro ukurwanya ugucengera kandi biteguriye gukora ibice vyinshi vya CoinJoin kugira ngo basubize inyuma ibidengeri bitobito.



Mu gihe ivy’ugusuzuma ivy’amahera biriko birarushiriza, ibikoresho vy’inzego zitandukanye vyo kurinda ubuzima bwite biriko biraba ivy’agaciro.



## Ubutunzi



### Inyandiko zemewe




- [Urubuga rwemewe rwa Joinstr](https://joinstr.xyz)
- [Inyandiko z'ukoresha](https://inyandiko.gufatanya.xyz/abakoresha/gukoresha-gufatanya)
- [Inyandiko z'ubuhinga](https://inyandiko.joinstr.xyz/insiguro/ingene-bikora)
- [Kode y'inkomoko ya GitLab](gitlab.com/ubuzima bwite-budashobora gutsindwa/ugufatanya)
- [Iporogaramu ya Android](ibanga ry'ubuzima bwite/joinstr-kmp/-/ibisohoka)



### Inyigisho




- [Inyigisho y'ivyo gukoresha Electrum](https://ubuhinga butagiramwo ubuhinga.



### Umuryango n'infashanyo




- [Itsinda ry'abafatanyabikorwa b'itelegaramu](https://t.me/joinstr) - Infashanyo y'abanyagihugu n'imfuruka z'ibimenyetso
- [Ikiganiro c'ubuhinga ku bijanye n'amahera] (https:



### Ibindi bikoresho




- [Ikimenyetso Faucet] (ikimenyetso c'ikimenyetso.com) - Igerageza ry'ubuntu ry'ama Bitcoins
- [Ikimenyetso c'iyindi Faucet](iyindi nkuru.com) - Faucet ubundi buryo
- [Mempool.ikibanza](kibanza) - Block explorer n'isesengura ry'ubuzima bwite
