---
name: Mwavuli LND
description: Mafunzo ya kina juu ya kusakinisha na kusanidi Lightning Network Daemon (LND) kwenye Umbrel
---
![cover](assets/cover.webp)




## Utangulizi



Mafunzo haya ya kina hukuchukua hatua kwa hatua kupitia usakinishaji, usanidi na matumizi ya programu ya Njia ya Umeme (LND) kwenye nodi yako ya Mwavuli. Utajifunza jinsi ya kufungua chaneli, kudhibiti ukwasi wako na kusawazisha nodi yako na programu ya simu ya mkononi.



## 1. Sharti: kazi ya Bitcoin Umbrel node



Kabla ya kupeleka Umeme, unahitaji kuwa na nodi ya Bitcoin inayofanya kazi kikamilifu kwenye Umbrel. Hii inahusisha kusakinisha Umbrel (kwenye Raspberry Pi, NAS au mashine nyingine) na kusawazisha kikamilifu Blockchain Bitcoin.



Ili kusakinisha Umbrel na kusanidi nodi yako ya Bitcoin, tunapendekeza ufuate mafunzo yetu yaliyojitolea:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Hakikisha nodi yako ya Bitcoin imesasishwa na inafanya kazi ipasavyo, kwani Lightning Network inaitegemea kwa shughuli zote za off-chain.



## 2. Utangulizi wa Lightning Network



Lightning Network ni itifaki ya pili ya Layer iliyoundwa ili kuharakisha na kupunguza gharama ya miamala ya Bitcoin kwa kuifanya nje ya Blockchain kuu.



Kwa maneno madhubuti, Umeme hutumia mtandao wa njia za malipo kati ya nodi: watumiaji wawili hufungua chaneli kwa kuzuia On-Chain BTC (muamala wa awali), kisha wanaweza kufanya malipo ya Exchange papo hapo ndani ya kituo hiki. Shughuli hizi za off-chain hazijarekodiwa kwenye Blockchain, kwa hivyo kasi yao na gharama karibu sifuri.



Malipo yanaweza kupitishwa kupitia chaneli nyingi (shukrani kwa nodi za kati) ili kufikia mpokeaji yeyote kwenye mtandao, na hivyo kuwezesha kiasi kisicho na kikomo cha miamala ya papo hapo. Umeme hivyo hutoa shughuli za haraka sana, za gharama nafuu, bora kwa malipo ya kila siku au shughuli ndogo ndogo, huku ukipunguza mzigo kwenye Blockchain Bitcoin.



Ili kufanya kazi, nodi ya Umeme lazima iunganishwe kabisa kwenye mtandao na kuingiliana na nodi zingine za Umeme. Utekelezaji wa programu mbalimbali upo (LND, Core Lightning, Eclair, n.k.), ambayo yote yanaoana. Mwavuli hutumia LND (Lightning Network Daemon) kama sehemu ya programu rasmi ya Njia ya Umeme. Mafunzo haya yanalenga LND.



Kwa utangulizi kamili wa kinadharia kwa Lightning Network, tunapendekeza usome kozi yetu maalum :



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Kozi hii itakupa msingi kamili wa dhana za kimsingi za Lightning Network, kabla ya kuendelea na mazoezi na nodi yako ya LND.



## 3. Kwa nini mwenyeji wa kibinafsi LND?



Kuendesha nodi yako mwenyewe ya Umeme (LND) kwenye Umbrel hukupa mamlaka kamili juu ya fedha na chaneli zako, ikilinganishwa na suluhu za uhifadhi au nusu-utunzi.



### Ulinganisho wa suluhisho la umeme:



**Uhifadhi wa suluhisho (mfano: Wallet ya Satoshi)** :




- Bitcoins zako za umeme zinasimamiwa na mtu wa tatu anayeaminika
- Rahisi kutumia, hakuna utata wa kiufundi
- Opereta anashikilia pesa zako na anaweza kufuatilia miamala yako
- Unajitolea udhibiti na usiri



**Mali ya watumiaji yasiyo ya bidhaa (k.m. Phoenix, Breez)** :




- Watumiaji huhifadhi funguo zao za kibinafsi na kwa hivyo Ownership ya BTC yao
- Hakuna usimamizi kamili wa nodi - programu hudhibiti chaneli chinichini
- Maelewano kati ya unyenyekevu na uhuru
- Utegemezi wa miundombinu ya wasambazaji kwa ukwasi
- Vizuizi vya kiufundi (simu mahiri moja haiwezi kuelekeza malipo kwa wengine)



**Njia inayojiendesha ya LND (Mwavuli)** :




- Kiwango cha juu zaidi cha uhuru: On-Chain na off-chain BTC zako ziko chini ya udhibiti wako kabisa.
- Hakuna washirika wengine wanaohusika katika kufungua vituo au kudhibiti malipo yako
- Kuongezeka kwa usiri (njia na miamala yako inajulikana na wewe tu na wenzako wa moja kwa moja)
- Uhuru wa kutumia: unganisha kwa huduma zako na pochi
- Uwezekano wa kuelekeza shughuli kwa wengine (malipo ya ada ndogo)
- Kuongezeka kwa majukumu ya kiufundi (matengenezo, usimamizi wa ukwasi, chelezo)



Kwa kifupi, ukaribishaji-mwenyeji wa LND hukupa udhibiti wa juu zaidi, lakini unahitaji ujuzi zaidi wa kiufundi. Ni biashara kati ya urahisi na uhuru.



## 4. Mafunzo ya hatua kwa hatua



### 4.1 Kusakinisha na kusanidi programu ya Njia ya Umeme kwenye Umbrel



Mara baada ya nodi yako ya Umbrel (Bitcoin) kusawazishwa, fuata hatua hizi:



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Sakinisha programu ya Njia ya Umeme kutoka sehemu ya "Duka la Programu" ya Mwavuli wa Interface.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



LND (Lightning Network Daemon) itatumwa kwenye Umbrel yako kama programu. Ukiifungua kwa mara ya kwanza, utaona ujumbe wa onyo ukikujulisha kuwa Umeme ni teknolojia ya majaribio.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Unaweza kuchagua kati ya kuunda nodi mpya au kurejesha moja kutoka kwa chelezo/seed. Kwa usakinishaji wa mara ya kwanza, chagua kuunda nodi mpya. Programu ya Njia ya Umeme ita generate kishazi cha Mnemonic chenye maneno 24 (Umeme wako wa seed): iandike kwa uangalifu sana (ikiwa ni bora nje ya mtandao, kwenye karatasi), kwani itatumika kurejesha pesa zako za Umeme ikihitajika.



**Kumbuka: Kwenye matoleo ya hivi majuzi ya Umbrel, usakinishaji wa programu ya Umeme hutoa seed ya maneno 24 (nodi ya Mwavuli ya Bitcoin yenyewe haifanyi hivyo).



![Interface principale de Lightning Node](assets/fr/04.webp)



Baada ya kuanzishwa, utafikia Interface kuu ya Njia ya Umeme.



![Paramètres de l'application](assets/fr/05.webp)



Katika mipangilio ya programu, utapata idadi ya chaguo muhimu:




   - Tazama Kitambulisho chako cha Nodi (kitambulisho cha kipekee cha nodi yako)
   - Inaunganisha Wallet ya nje (Unganisha Wallet)
   - Tazama maneno ya siri
   - Fikia Mipangilio ya Kina
   - Rejesha vituo
   - Pakua faili ya chelezo ya kituo
   - Washa chelezo otomatiki
   - Sanidi nakala rudufu kupitia Tor (Hifadhi nakala juu ya Tor)



Chaguo hizi ni muhimu kwa usalama na usimamizi wa nodi yako ya Umeme. Hakikisha umewasha hifadhi rudufu za kiotomatiki na uweke maneno yako ya siri salama.



**Nyenzo muhimu:**




- [Jumuiya ya Mwavuli](https://community.umbrel.com) - Jukwaa la majadiliano kwa watumiaji kushiriki matatizo na masuluhisho kuhusu Umbrel na mfumo wake wa ikolojia


> - [Duka la Programu ya Mwavuli - Njia ya Umeme (LND)](https://apps.umbrel.com/app/lightning) - Maelezo ya vipengele vya programu ya Njia ya Umeme kwenye Mwavuli
> - [Hati za LND - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Hati Rasmi za LND

### 4.2 Kufungua njia ya Umeme



Mara tu LND inapoanza kufanya kazi, unaweza kufungua chaneli yako ya kwanza ya Umeme. Ili kupata nodi za ubora za kuunganisha kwa:



![Page d'accueil Amboss.space](assets/fr/06.webp)



[Amboss.space](https://amboss.space/) ni mgunduzi wa kutafuta nodi zinazotegemeka za kufungua vituo.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Kwa mfano, [ACINQ nodi](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) ni nodi inayotambulika na yenye utulivu wa hali ya juu.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



Kwa mafunzo haya, tutafungua kituo tukitumia [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). Taarifa inayohitajika kwa ajili ya kuunganisha (pubkey@ip:port) imetolewa kwenye ukurasa wao wa Amboss.



Ili kufungua kituo:



![Bouton d'ouverture de canal](assets/fr/09.webp)



Kwenye ukurasa wa nyumbani wa Njia ya Umeme, bofya kitufe cha "+ FUNGUA CHANNEL".



![Configuration du canal](assets/fr/10.webp)



Katika ukurasa wa usanidi wa kituo :




   - Bandika kitambulisho cha nodi kilichonakiliwa kutoka kwa Amboss (umbizo: pubkey@ip:port)
   - Bainisha kiasi cha uwezo wa kituo (baadhi ya nodi kama ACINQ zina viwango vya chini zaidi, k.m. 400k Sats)
   - Rekebisha ada za shughuli za kufungua ikiwa ni lazima



![Canal en cours d'ouverture](assets/fr/11.webp)



Mara tu muamala utakapotumwa, kituo kitaonekana kama "kinafunguliwa" kwenye ukurasa wa nyumbani. Subiri uthibitisho wa muamala wa On-Chain.



![Détails du canal](assets/fr/12.webp)



Bofya kwenye kituo kutazama maelezo yake:




   - Hali ya sasa
   - Jumla ya uwezo
   - Mchanganuo wa ukwasi (zinazoingia/zinazotoka)
   - Kitufe cha umma cha nodi ya mbali
   - Na habari zingine za kiufundi



### Kutumia Lightning Network+ kupata ukwasi unaoingia



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



Lightning Network+ inapatikana katika Umbrel App Store ili kurahisisha kupata pesa zinazoingia.



![Interface principale de LN+](assets/fr/14.webp)



Interface kuu inatoa chaguzi tatu muhimu:




- "Ubadilishanaji wa Liquidity: chunguza matoleo yanayopatikana ya kubadilishana
- "Fungua Kwa Ajili Yangu": chuja ubadilishaji ambao unastahiki
- "Kwa Hati": ufikiaji wa hati



![Message d'erreur LN+](assets/fr/15.webp)



Kumbuka: Ikiwa bado huna chaneli iliyofunguliwa, utaona ujumbe huu wa hitilafu unapobofya "Nifungulie".



![Liste des swaps disponibles](assets/fr/16.webp)



Ukurasa wa "Liquidity Swips" unaonyesha matoleo yote ya kubadilishana yanayopatikana kwenye mtandao.



![Swaps éligibles](assets/fr/17.webp)



"Fungua Kwa Ajili Yangu" huchuja tu zile ubadilishaji ambazo nodi yako inakidhi masharti yanayohitajika.



![Détails d'un swap](assets/fr/18.webp)



Mfano wa maelezo ya kubadilishana:




- Usanidi wa Pentagon (washiriki 5)
- Uwezo wa 300k Sats kwa kila chaneli
- Sharti: angalau chaneli 10 zilizofunguliwa na jumla ya uwezo wa 1M Sats
- Maeneo yanayopatikana: 4/5



### 4.3 Usawazishaji na programu ya simu (Zeus)



Ili kudhibiti eneo lako la Umeme ukiwa mbali (simu mahiri), unaweza kutumia Zeus (programu huria inayopatikana kwenye iOS/Android).



**Usanidi wa Zeus na Umbrel:**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Hakikisha nodi yako ya Umbrel inapatikana (kwa chaguo-msingi kupitia Tor).


Katika Mwavuli wa Interface, fungua programu ya Njia ya Umeme, kisha ubofye kitufe cha "Unganisha Wallet" kama inavyoonyeshwa na mshale.



![Page de connexion avec QR code](assets/fr/20.webp)



Msimbo wa QR unaonekana, ulio na data yako ya ufikiaji ya LND katika umbizo la lndconnect. Msimbo huu wa QR ni mnene sana wenye maelezo, kwa hivyo usisite kuukuza ili usomaji rahisi zaidi.



![Configuration initiale de Zeus](assets/fr/21.webp)



Kwenye simu yako:




   - Fungua Zeus
   - Kwenye ukurasa wa nyumbani, bofya "Usanidi wa hali ya juu" ili kuunganisha nodi yako ya Umeme
   - Katika vigezo, chagua "Unda au unganisha Wallet"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



Katika Zeus:




   - Chagua "LND (REST)" kama aina ya muunganisho
   - Unaweza kuchanganua msimbo wa QR (njia inayopendekezwa) au uweke maelezo wewe mwenyewe. (Usisite kuvuta msimbo wa Umbrel QR, kwani ni mnene sana)
   - Muhimu: washa chaguo la "Tumia Tor" ikiwa Mwavuli wako unapatikana tu kupitia Tor (chaguo-msingi)
   - Hifadhi usanidi



Zeus yako sasa imeunganishwa kwenye nodi yako ya Mwavuli na hukuruhusu kufanya malipo ya Radi, kutazama chaneli zako, salio, n.k., huku ukiendelea kujidhibiti kikamilifu.



**Chaguo za uunganisho wa hali ya juu:**



Kwa chaguo-msingi, muunganisho wa mwavuli wa Zeus ↔ ni kupitia Tor. Kwa muunganisho wa haraka, kuna njia mbili mbadala:



**Unganisha Njia ya Umeme (LNC)** :




   - Utaratibu wa muunganisho uliosimbwa kwa njia fiche wa Maabara ya Umeme
   - Sakinisha programu ya Kituo cha Umeme kwenye Umbrel (pamoja na ufikiaji wa LNC)
   - generate msimbo wa QR wa unganisho kwenye Kituo cha Umeme (Unganisha → Unganisha Zeus kupitia LNC)
   - Ichanganue kuwa Zeus (chagua "LNC" kama aina ya unganisho)



**Kiwango cha mkia cha VPN**:




   - Ni rahisi kusanidi VPN ya matundu
   - Sakinisha Tailcale kwenye Umbrel (Duka la Programu) na kwenye simu yako ya rununu
   - Unganisha Zeus kupitia IP ya faragha ya Tailscale badala ya Tor Address



Chaguzi hizi sio lazima, na suluhisho la Tor + Zeus hufanya kazi vizuri katika hali nyingi.



> **Nyenzo muhimu:**
> - [Hati za Zeus - Muunganisho wa Mwavuli](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Mwongozo rasmi wa kuunganisha Zeus kwenye Mwavuli
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Mradi wa chanzo huria wa Zeus
> - [Jumuiya ya Mwavuli - Kuunganisha Zeus kupitia Tailscale](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Mwongozo wa kuunganisha Zeus kwa Mwavuli kwa kutumia Tailscale

## 5. Usalama na mbinu bora



Kusimamia nodi ya Umeme inayojiendesha yenyewe inahitaji umakini maalum kwa usalama.



### Hifadhi rudufu na usalama kwa nodi yako



**Aina muhimu za chelezo**



Nodi yako ya Mwavuli ya Umeme inahitaji aina mbili za chelezo:



**Sentensi ya seed (maneno 24)**




- Hurejesha fedha za On-Chain
- Inahitajika kuunda upya Umeme wako wa Wallet
- Kwa hifadhi salama kabisa (nje ya mtandao, kwenye karatasi)



**Faili ya Hifadhi Nakala ya Idhaa Tuli (SCB)**




- Ina maelezo ya kituo cha Umeme
- Huwasha kufungwa kwa kituo kwa lazima katika tukio la kuacha kufanya kazi
- Muhimu:** Kamwe usihifadhi faili ya `channel.db` mwenyewe (hatari ya adhabu)



** Utaratibu wa kuhifadhi nakala kwa mikono



Ili kuhifadhi chaneli zako mwenyewe :


1. Fikia menyu ya Njia ya Umeme (vidokezo vitatu "⋮" karibu na "+ Fungua Kituo")


2. Pakua faili ya chelezo ya kituo


3. Hamisha SCB mpya baada ya kila urekebishaji wa kituo


4. Hifadhi SCB kwa usalama (midia iliyosimbwa kwa njia fiche, nakala ya nje ya tovuti)



**Mwavuli** mfumo wa kuhifadhi nakala kiotomatiki



Umbrel ina mfumo wa kisasa wa kuhifadhi nakala otomatiki unaohakikisha :



*Ulinzi wa data:*




- Usimbaji fiche wa upande wa mteja kabla ya kutuma
- Inatuma kupitia mtandao wa Tor
- Data inayoongezewa na kujaza bila mpangilio
- Ufunguo wa usimbaji fiche wa kipekee kwa kifaa chako



*Usalama ulioimarishwa:*




- Hifadhi nakala za papo hapo kwenye mabadiliko ya hali
- Decoy" chelezo kwa vipindi nasibu
- Ficha mabadiliko ya ukubwa wa chelezo
- Ulinzi dhidi ya uchambuzi wa wakati



*Mchakato wa kurejesha:*




- Kitambulisho na ufunguo unaotokana na Mwavuli wako wa seed
- Urejeshaji kamili unawezekana kwa maneno ya Mnemonic pekee
- Urejeshaji otomatiki wa chelezo za hivi punde
- Rejesha mipangilio ya kituo na data



### Marejesho ya ajali



Ikiwa nodi yako imepotea (kushindwa kwa vifaa, kadi ya SD iliyoharibika):




- Sakinisha tena Umbrel
- Weka seed yako ya maneno 24 katika programu ya Umeme
- Ingiza faili ya SCB wakati wa kurejesha



LND itawasiliana na kila mshirika wa vituo vyako vya zamani ili kuvifunga na kurejesha sehemu yako ya fedha za On-Chain. Vituo vitafungwa kabisa (vifunguliwe tena ikihitajika).



### Upatikanaji na ulinzi wa ulaghai



Kimsingi, acha fundo lako mtandaoni mara nyingi iwezekanavyo. Katika kesi ya kutokuwepo kwa muda mrefu:




- Rafiki mwenye nia mbaya anaweza kujaribu kutangaza hali ya zamani ya kituo
- Umeme hutoa "kipindi cha maandamano" (takriban wiki 2 kwenye LND)
- Ikiwa utaenda mbali kwa muda mrefu, weka Watchtower



**Usanidi wa Watchtower:**




- Katika mipangilio ya kina ya LND, ongeza URL ya seva inayoaminika ya Watchtower
- Unaweza kutumia huduma ya umma au kusakinisha Watchtower yako mwenyewe




Ili kujua zaidi kuhusu kusanidi na kutumia minara, tunapendekeza uangalie mafunzo yetu yaliyojitolea:



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Mazoea mengine bora





- Masasisho ya programu:** Sasisha Umbrel na LND (marekebisho ya usalama)
- Ulinzi wa maunzi:** Tumia mfumo thabiti (Raspberry Pi na SSD, mini-PC) na UPS
- Usalama wa mtandao:** Weka usanidi chaguo-msingi wa Tor, badilisha nenosiri la msimamizi wa Umbrel (chaguo-msingi: "moneyprintergobrrr")
- Usimbaji fiche:** Washa usimbaji fiche wa diski ikiwezekana



## 6. Zana za ziada



Programu ya Umbrel's Lightning Node hutoa mambo muhimu ya kudhibiti chaneli zako, lakini zana za wahusika wengine hutoa utendakazi wa hali ya juu.



### ThunderHub



Mfumo wa kisasa wa usimamizi wa nodi za Umeme unaotegemea wavuti unaowekwa kwenye wavuti unaoweza kusakinishwa kupitia Duka la Programu la Umbrel.



**Sifa:**




- Taswira ya wakati halisi ya chaneli (uwezo, mizani)
- Vyombo vya kusawazisha vilivyojumuishwa
- Usaidizi wa utozaji wa njia nyingi (MPP)
- Uzalishaji wa msimbo wa QR LNURL
- Usimamizi wa shughuli On-Chain



ThunderHub ni bora kwa ufuatiliaji wa nodi inayotumika ya uelekezaji na kutekeleza kusawazisha upya kwa urahisi.



### Panda Umeme (RTL)



Wavuti ya Interface inaoana na utekelezaji kadhaa wa Umeme (LND, Umeme wa Msingi, Eclair).



**Mambo muhimu:**




- Usimamizi wa nodi nyingi
- Dashibodi zinazozingatia muktadha
- Usaidizi wa ubadilishaji wa manowari (Kitanzi cha Umeme)
- Uthibitishaji wa sababu-2
- Hamisha/ingiza nakala rudufu za kituo



RTL ni "kisu cha jeshi la Uswizi" kamili cha kusimamia eneo la Umeme kwa mbinu iliyoelekezwa zaidi kwa utaalam.



### Zana nyingine muhimu





- Shell ya Umeme** : Mstari wa amri (lncli) kupitia kivinjari
- BTC RPC Explorer & Mempool** : Ufuatiliaji Blockchain
- LNmetrics & Torq**: Uchanganuzi wa utendaji wa njia
- Amboss & 1ML**: Usimamizi wa "Kijamii" wa nodi yako (lakabu, anwani, uchanganuzi wa mtandao)



Zana hizi zinaweza kusakinishwa kwa kubofya mara chache tu kupitia Hifadhi ya Programu ya Umbrel, bila usanidi wowote changamano.



**Nyenzo za zana za ziada:**




- [ThunderHub.io - Vipengele](https://thunderhub.io) - Muhtasari wa vipengele vya ThunderHub
- [Maelezo ya Ride The Lightning (RTL)](https://www.ridethelightning.info/) - Hati za RTL
- [David Kaspar - Usawazishaji kupitia ThunderHub](https://blog.davidkaspar.com) - Mwongozo wa vitendo wa kusawazisha upya
- [Mwongozo "Kudhibiti Nodi za Umeme"](https://github.com/openoms/lightning-node-management) - Hati za hali ya juu kwa watumiaji wa nishati



## Hitimisho



Kuendesha nodi yako ya LND kwenye Umbrel ni hatua muhimu kuelekea uhuru wa kifedha. Ingawa inahitaji ushirikishwaji wa kiufundi zaidi kuliko suluhisho la uhifadhi, faida katika suala la udhibiti, usiri na ushiriki hai katika Lightning Network ni kubwa.



Kwa kufuata mwongozo huu, sasa unapaswa kuwa na uwezo wa kusakinisha LND, kufungua njia, kudhibiti ukwasi wako na kufikia nodi yako ukiwa mbali. Jisikie huru kuchunguza vipengele vya kina na zana za ziada hatua kwa hatua kadri unavyofahamu zaidi mfumo ikolojia.



Kumbuka kwamba usalama wa fedha zako unategemea ulinzi na mazoea yako. Chukua muda kuelewa kila kipengele kabla ya kufanya kiasi kikubwa.
