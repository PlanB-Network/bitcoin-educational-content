---
name: Joinstr
description: CoinJoins Zilizogatuliwa kupitia mtandao wa Nostr kwa usiri huru wa Bitcoin
---

![cover](assets/cover.webp)



Uwazi wa blockchain ya Bitcoin hufanya iwezekane kufuatilia historia ya muamala. CoinJoins huvunja viungo hivi kwa kuchanganya miamala mingi kwa wakati mmoja, kurejesha kiwango cha usiri kinacholingana na pesa taslimu.



Walakini, suluhisho za kitamaduni hutegemea mratibu mkuu kama sehemu moja ya kutofaulu. Wasabi na Samourai zilikoma kufanya kazi mwaka wa 2024 chini ya shinikizo la udhibiti.



**Joinstr** huondoa udhaifu huu kwa kutumia mtandao wa Nostr uliogatuliwa kwa uratibu. Programu hii ya programu huria huwezesha CoinJoins huru kabisa, ambapo hakuna mamlaka kuu inayoweza kukagua, kufuatilia au kukatiza huduma.



## Joinstr ni nini?



Joinstr ni zana huria ambayo inabadilisha mbinu ya CoinJoins kwa kutumia itifaki ya Nostr kama miundombinu ya uratibu. Tofauti na suluhu za kati zinazohitaji seva iliyojitolea, Joinstr inategemea mtandao uliosambazwa wa relay za Nostr ili kuwawezesha washiriki kuratibu moja kwa moja kati ya wenzao.



**Usanifu uliogatuliwa** : Mtandao wa Nostr unachukua nafasi ya mratibu mkuu. Washiriki huunda au kujiunga na "pools" kwa kuchapisha matangazo yaliyosimbwa kwa njia fiche kupitia relay za Nostr. Taarifa hii (idadi, washiriki, anwani) bado haieleweki kwa relay, ikihakikisha kwamba hakuna huluki kuu inayoweza kufuatilia, kuhakiki au kuchuja CoinJoins.



**SIGHASH_ALL|Mchakato wa ANYONECANPAY**: Joinstr anatumia alama hii ya sahihi ya Bitcoin, kumruhusu kila mshiriki kutia sahihi ingizo lake pekee huku akithibitisha matokeo yote. Kila mtumiaji huzalisha PSBT yake ndani ya nchi, kisha husambaza kupitia Nostr. Kila mtumiaji hutengeneza PSBT yake ndani ya nchi, hutia saini, kisha huisambaza kupitia Nostr. Bitcoins zako zitasalia chini ya udhibiti wako wa kipekee hadi saini ya mwisho.



**Falsafa**: Joinstr inafuata kanuni za Bitcoin za cypherpunk, zinazolenga malengo matatu: **upinzani wa udhibiti** (hakuna mamlaka inayoweza kusimamisha huduma), **kutoweka kwa jumla** (unaweka funguo zako za faragha), na **kutendewa sawa** (hakuna UTXO inayoweza kubaguliwa).



### Sifa kuu



**Dimbwi linalonyumbulika**: Tofauti na madhehebu yasiyobadilika, mtumiaji yeyote anaweza kuunda bwawa lenye kiasi kamili anachotaka na idadi inayolengwa ya washiriki, ili kuboresha matumizi ya UTXO bila mgawanyiko bandia.



**Ada za uwazi**: Hakuna ada za uratibu. Ada za miamala za Bitcoin pekee ndizo zinazoshirikiwa kwa usawa kati ya washiriki (satoshi elfu chache kwa kila mtu).



**Ephemerality**: Hakuna data ya mtumiaji iliyohifadhiwa. Usafirishaji wa habari kupitia ujumbe uliosimbwa wa ephemeral Nostr, uliosahaulika mara baada ya shughuli.



### Majukwaa yanayopatikana



Mafunzo haya yanaangazia **Programu ya Android**, suluhisho pekee thabiti na linalopendekezwa kwa sasa. Programu-jalizi ya Electrum ipo lakini ina matatizo ya uoanifu ambayo huifanya kuwa thabiti. Kiolesura cha wavuti kinatengenezwa.



## Usanidi wa Bitcoin Core



Joinstr Android inahitaji muunganisho kwa nodi ya Bitcoin kupitia RPC. Lazima kwanza usanidi Bitcoin Core kwenye kompyuta yako ili kukubali miunganisho kutoka kwa simu yako.



**Kumbuka**: Kwa maelezo zaidi kuhusu usanidi kamili wa Bitcoin Core, angalia mafunzo yetu mahususi :



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Mahitaji ya mtandao



#### Tafuta anwani yako ya karibu ya IP



Simu yako ya Android lazima iweze kufikia nodi yako ya Bitcoin kwenye mtandao wa ndani. Pata anwani ya IP ya kompyuta yako:



**Kwenye macOS** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Mbadala rahisi:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**Kwenye Linux** :



```bash
hostname -I | awk '{print $1}'
```



**Kwenye Windows** :



```cmd
ipconfig
```



Tafuta anwani ya IPv4 (umbizo `192.168.x.x` au `10.0.x.x`)



### Usanidi wa RPC



#### Badilisha bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Tafuta faili yako ya `bitcoin.conf`:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/Library/Application Support/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Fungua faili na kihariri chako cha maandishi unachopenda na uongeze usanidi huu ili kuamilisha seva ya RPC.



**Usanidi unaopendekezwa wa kuanza (alamisho)** :



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



**usanidi wa mainnet** (kwa matumizi ya uzalishaji) :



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



**Muhimu** :




- Saini inapendekezwa sana** kwa majaribio yako ya kwanza: programu bado inaundwa (beta), na hitilafu bado zinaweza kuwepo. Saini hukuruhusu kufanya majaribio bila malipo, bila kuhatarisha pesa halisi
- Badilisha `192.168.1.0/24` na subnet ya mtandao wako (k.m. ikiwa IP yako ni `192.168.68.57`, tumia `192.168.68.0/24`)



**Usalama**: Tengeneza nenosiri thabiti :



```bash
openssl rand -base64 32
```



### Kuanzisha



#### Anzisha tena na uangalie



1. Zima Bitcoin Core kabisa


2. Anzisha upya ili kutumia usanidi




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Wakati Bitcoin Core itaanza kwa mara ya kwanza, itapakua na kusawazisha alamisho blockchain. Operesheni hii ni haraka sana kuliko kwenye mainnet (dakika chache tu). Tafadhali subiri hadi ulandanishi ukamilike kabla ya kuendelea.



![CRÉATION DE WALLET](assets/fr/04.webp)



Mara baada ya kuoanishwa, unda kwingineko mpya kwa kubofya "Unda wallet mpya". Ipe jina wazi kama `tuto_joinstr_signet`.



![WALLET CRÉÉ](assets/fr/05.webp)



wallet yako sasa imeundwa na iko tayari kupokea bitcoins zilizoalamishwa kwa majaribio.



#### Pata bitcoins zilizoalamishwa (jaribio)



Ili kujaribu Joinstr kwenye alamisho, unahitaji bitcoins za majaribio bila malipo :



![SIGNET FAUCET](assets/fr/06.webp)



Tumia alamisho ya umma kama:




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [alama257.bublina.eu.org](https://signet257.bublina.eu.org)



Katika Bitcoin Core, generate anwani mpya ya kupokea (kichupo cha "Pokea"), nakili na ubandike kwenye fomu ya bomba. Tatua captcha ikiwa ni lazima. Utapokea bitcoins zilizoalamishwa bila malipo ndani ya sekunde chache.



## Programu ya Android



### Ufungaji



![APPLICATION ANDROID](assets/fr/07.webp)



Nenda kwenye [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) ili kupakua toleo jipya zaidi la APK. Kwenye kivinjari chako cha Android, pakua faili, kisha uifungue ili kuzindua usakinishaji. Utahitaji kuruhusu usakinishaji kutoka kwa vyanzo visivyojulikana katika mipangilio ya usalama ya simu yako ikihitajika.



### Usanidi wa programu



![PERMISSIONS VPN](assets/fr/08.webp)



Wakati wa uzinduzi wa kwanza, programu ya Joinstr itaomba ruhusa ili kudhibiti VPN iliyojengewa ndani. Kubali maombi yote mawili ya ruhusa: Udhibiti wa OpenVPN na muunganisho wa VPN. Ruhusa hizi zinahitajika kwa ujumuishaji wa VPN, ambayo inalinda faragha ya mtandao wako.



![INTERFACE APPLICATION](assets/fr/09.webp)



Programu ya Joinstr imepangwa katika tabo kuu tatu:




- Nyumbani**: Skrini ya nyumbani
- Mabwawa**: Kuunda na kusimamia mabwawa ya CoinJoin
- Mipangilio**: Usanidi wa programu



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Sanidi mipangilio kwenye kichupo cha "Mipangilio":



**1. Nostr Relay**: Anwani ya relay ya Nostr kwa uratibu wa bwawa




- Mfano: `wss://relay.damus.io`
- Reli nyingine zinazopendekezwa: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Muhimu**: Washiriki wote lazima watumie **wilaya sawa ya Nostr** ili kuona na kujiunga na madimbwi sawa. Ikiwa unatumia relay tofauti, hutaona mabwawa yaliyoundwa kwenye relay nyingine



**2. URL ya nodi**: Anwani ya IP ya nodi yako ya Bitcoin (bila lango)




- Umbizo: `http://VOTRE_IP_LOCALE`
- Mfano: `http://192.168.68.57`



**3. RPC Jina la mtumiaji** : Jina la mtumiaji lililosanidiwa katika `rpcuser=` kwenye bitcoin.conf yako




- Mfano: `satoshi



**4. Nenosiri la RPC** : Nenosiri limewekwa `rpcpassword=` kwenye bitcoin.conf yako



**5. RPC Port** : RPC bandari kulingana na mtandao




- Mainnet** : `8332`
- Alamisho**: `38332`



**6. Wallet**: Chagua kwingineko ya Msingi ya Bitcoin iliyo na UTXO itakayochanganywa




- Mfano: `tuto_joinstr_signet`



**7. Lango la VPN**: Chagua seva ya Riseup VPN




- Mfano: `(Paris) vpn07-par.riseup.net`
- Nyingine zinazopatikana: Amsterdam, Seattle, nk.
- ⚠️ **Muhimu**: Washiriki wote katika bwawa moja lazima watumie **Mlango sawa wa VPN** ili kushiriki katika CoinJoin. Wakati wa mzunguko wa kuchanganya, washiriki wote lazima waonekane na anwani sawa ya kutoka ya IP ili kuzuia uchanganuzi wa mtandao kutoka kwa washiriki wanaohusiana.



Programu ya Joinstr **huunganisha kwa asili** Riseup VPN, kurahisisha uratibu kati ya washiriki.



**Muhimu** :




- Hakikisha simu na kompyuta yako ziko kwenye mtandao sawa wa WiFi wa karibu nawe
- Muunganisho wa VPN utawashwa kiotomatiki unaposhiriki kwenye bwawa
- Bonyeza **"Hifadhi "** mara tu umeweka vigezo vyote



## Matumizi ya vitendo



### Unda au ujiunge na bwawa



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Una chaguo mbili za kushiriki katika CoinJoin:



**Chaguo la 1: Unda bwawa jipya**



Bonyeza "Unda Dimbwi Jipya" kwenye kichupo cha "Madimbwi". Bainisha dhehebu katika BTC (k.m. 0.002 BTC) na idadi inayotakiwa ya washiriki (angalau 2, iliyopendekezwa 3-5 kwa kutokujulikana zaidi). Programu basi husubiri watumiaji wengine wajiunge na dimbwi lako. Mara tu nambari inayohitajika imefikiwa, mchakato wa usajili wa towe huanza kiotomatiki, na utahitaji kuchagua UTXO yako ili kuchanganya na kubofya "Jisajili".



**⏱️ Muhimu**: Muda wa kuogelea unaisha baada ya **dakika 10** ya kutokuwa na shughuli. Ikiwa idadi inayotakiwa ya washiriki haijafikiwa, bwawa litafungwa moja kwa moja.



**Chaguo la 2: Jiunge na bwawa lililopo**



Katika kichupo cha "Angalia Madimbwi Mengine", vinjari madimbwi yanayopatikana yaliyoundwa na watumiaji wengine. Chagua bwawa linalolingana na kiasi chako na ujiunge nayo. Hakikisha kuwa umesanidi relay ya Nostr na VPN Gateway sawa na washiriki wengine (angalia sehemu ya Usanidi).



**Sheria ya uteuzi ya UTXO**: UTXO yako lazima iwe juu kidogo kuliko madhehebu ya bwawa (kati ya +500 na +5000 sats ya ziada).



**Mfano**: Kwa bwawa la 0.002 BTC (200,000 sats), tumia UTXO kati ya 200,500 na 205,000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Mchakato basi huwa **kiotomatiki kabisa**: punde tu ingizo lako limesajiliwa, ombi linasubiri washiriki wote kusajili pembejeo zao. Mara tu pembejeo zote zimesajiliwa, PSBT inaundwa, imesainiwa kiotomatiki na funguo zako, kisha kuunganishwa na saini za washiriki wengine. Hatimaye, shughuli kamili inatangazwa kwenye mtandao wa Bitcoin. Unapokea TXID (kitambulisho cha muamala) mara tu matangazo yatakapokamilika. Hakuna ugeuzaji mwenyewe wa PSBT unaohitajika kwenye Android.



### Uthibitishaji wa on-chain



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Mara tu muamala utakapotangazwa, utapokea TXID (kitambulisho cha muamala). Iangalie kwenye [mempool.space](https://mempool.space) au kivinjari chako unachokipenda. Ili kujaribu alamisho, tumia [mempool.space/signet](https://mempool.space/signet).



Unaweza kutazama:





- Maingizo n**: Moja kwa kila mshiriki (katika mfano wetu, maingizo 2)
- N matokeo yanayofanana**: kiasi kamili cha dhehebu (hapa, matokeo 2 ya 0.00199800 BTC kila moja)
- Chati ya mtiririko**: mempool.space huonyesha kwa macho mchanganyiko wa pembejeo na matokeo
- Vipengele** : Muamala unaweza kutambuliwa kama SegWit, Taproot, RBF, nk.



Kwa vile matokeo yote makuu yana kiasi sawa, **haiwezekani kuamua ni mali ya nani**. Hii ndiyo kanuni ya msingi ya CoinJoin: kutotofautishwa kwa matokeo.



**Mfano wa saini ya muamala** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool) .space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Tafadhali kumbuka**: Ikiwa UTXO zako zilikuwa kubwa kuliko madhehebu ya bwawa, utakuwa na matokeo ya kubadilisha fedha za kigeni (ziada). UTXO hizi za kubadilishana zinaendelea kufuatiliwa na lazima zidhibitiwe kando na matokeo yako ambayo hayakutambulisha. Usiwahi kuzichanganya na matokeo yako mseto.



## Vifurushi vya ubora wa CoinJoin na kutokujulikana



Ufanisi wa CoinJoin hupimwa kwa **anonset** yake: idadi ya matokeo ya thamani inayofanana inayotolewa na muamala. Nambari hii ya juu, ni vigumu zaidi kuamua ni pembejeo gani inayofanana na pato gani.



Joinstr kwa sasa inazalisha vikundi vya washiriki 2 hadi 5 ** kwa wastani. Takwimu hizi ni za chini kuliko waratibu wa jadi wa serikali kuu kama Wasabi (washiriki 50-100) au Whirlpool (washiriki 5-10), lakini hiyo ndiyo bei ya ugatuaji.



💡 **Ili kuelewa seti za kutokujulikana na hesabu zao kwa undani**, angalia kozi yetu kamili: [Kutokujulikana seti](https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c/be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr dhidi ya CoinJoins nyingine



| Aspect | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Participants par pool** | 50-100 | 5-10 | Variable (P2P) | **2-5** |
| **Coordinateur** | Centralisé (fermé 2024) | Centralisé (actif) | P2P maker/taker | **Aucun (Nostr)** |
| **Résistance à la censure** | Faible | Moyenne | Très élevée | **Très élevée** |
| **Frais de coordination** | Pourcentage | Frais d'entrée | Payés aux makers | **Aucun** |
| **Discrimination UTXO** | Oui (blacklists) | Non | Non | **Non** |

💡 **Suluhisho zingine zinazotumika za CoinJoin** :




- Ashigaru**: Utekelezaji wa chanzo huria wa itifaki ya Whirlpool na mratibu wa serikali kuu lakini inaweza kupelekwa kwa njia iliyogatuliwa. Inaendelea kufanya kazi baada ya kunaswa kwa Samourai Wallet mnamo 2024.
- JoinMarket**: Suluhisho la P2P lililogatuliwa bila mratibu mkuu, kulingana na mtindo wa biashara wa mtengenezaji/mchukuaji ambapo "watengenezaji" hutoa ukwasi na hulipwa na "wachukuaji".



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Ubadilishanaji wa kimsingi**: Joinstr na JoinMarket ndio masuluhisho mawili pekee bila mratibu mkuu. JoinMarket hutumia mtindo wa biashara wa P2P na motisha za kifedha, wakati Joinstr hutumia Nostr kwa uratibu wa bure. Joinstr hujitolea kutokujulikana mara moja kwa kiwango kikubwa ili kupendelea unyenyekevu (hakuna usimamizi wa mtengenezaji/mchukua) na kutokuwepo kwa ada za uratibu.



**Mapendekezo ya vitendo**: Ili kufidia madimbwi madogo, endesha mizunguko kadhaa mfululizo ya CoinJoin na washiriki tofauti. Angaza miduara yako na ubadilishe relay za Nostr kati ya kila raundi ili kuongeza usiri wako.



Jisikie huru kushauriana na kozi yetu kamili juu ya faragha ya bitcoin kwa habari zaidi juu ya mada hii:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Faida na mapungufu



### Vivutio



**Faragha iliyoimarishwa**: Mchanganyiko wa usimbaji fiche wa mawasiliano ya Nostr, VPN iliyoshirikiwa kati ya washiriki, na matumizi yanayopendekezwa ya Tor hutengeneza ulinzi wa tabaka nyingi ambao ni vigumu kuukwepa.



**Uwazi, gharama ndogo**: Hakuna gharama za uratibu, ni gharama za mining pekee ndizo zinazoshirikiwa kwa usawa kati ya washiriki. Hakuna asilimia inayotozwa na mwendeshaji yeyote.



### Vikwazo vya kuzingatia





- Ukwasi unaobadilika**: Vidimbwi vidogo, vinaweza kusubiri washiriki wakutane
- Mradi unaendelea**: Utumaji programu katika beta, hitilafu zinawezekana. Jaribu kwanza kwa kiasi kidogo kwenye alamisho
- Mashambulizi ya Sybil**: Uwezekano wa mpinzani mmoja kudhibiti washiriki kadhaa wa kundi



## Mbinu bora



**UTXO kutengwa**: Kamwe usichanganye UTXO iliyochanganywa na isiyochanganywa. Tumia kwingineko tofauti kwa matokeo yako yasiyojulikana.



**Raundi nyingi muhimu**: Fanya angalau mizunguko 3 mfululizo na washiriki tofauti. Badili kiasi na nyakati ili kuepuka ruwaza. Nafasi huzunguka kwa saa kadhaa.



**Ulinzi wa mtandao**: Tumia Tor kwa utaratibu pamoja na VPN iliyojengewa ndani. Tengeneza funguo za ephemeral Nostr kwa kila kipindi muhimu.



**Maendeleo ya tahadhari**: Anza kuweka alamisho kwa kiasi kidogo.



## Hitimisho



Joinstr inawakilisha suluhisho la faragha la Bitcoin lililogatuliwa kweli. Kwa kutumia Nostr kwa uratibu, huondoa utegemezi kwa waratibu wa kati wakati wa kuhifadhi uhuru wa mtumiaji.



**Kwa watumiaji wanaothamini upinzani dhidi ya udhibiti na wako tayari kutekeleza mizunguko kadhaa ya CoinJoin ili kufidia madimbwi madogo.



Kutokana na hali ya kuongezeka kwa uchunguzi wa kifedha, zana zilizogatuliwa kulinda faragha zinakuwa muhimu.



## Rasilimali



### Nyaraka rasmi




- [Jiunge na tovuti rasmi](https://joinstr.xyz)
- [Hati za mtumiaji](https://docs.joinstr.xyz/users/using-joinstr)
- [Nyaraka za kiufundi](https://docs.joinstr.xyz/overview/how-does-it-work)
- [Msimbo wa chanzo wa GitLab](https://gitlab.com/invincible-privacy/joinstr)
- [Programu ya Android](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Mafunzo




- [Mafunzo ya programu-jalizi ya Electrum](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Mwongozo kamili wa Uncensored Tech



### Jumuiya na msaada




- [Telegram Joinstr Group](https://t.me/joinstr) - Usaidizi wa jumuiya na pembe za alamisho
- [Majadiliano ya kiufundi kuhusu DelvingBitcoin](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Zana za ziada




- [Alamisho Faucet](https://signetfaucet.com) - Mtihani wa Bitcoins bila malipo
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Faucet mbadala
- [Mempool.space](https://mempool.space) - Block explorer yenye uchanganuzi wa faragha