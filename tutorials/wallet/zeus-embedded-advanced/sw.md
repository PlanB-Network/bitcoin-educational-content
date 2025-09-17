---
name: Zeus Embedded - Ya Juu
description: Wallet ya Lightning yenye nodi nyingi ya kujihifadhi
---

![Zeus](assets/cover.webp)


## Utangulizi wa ZEUS Wallet


ZEUS ni programu ya simu ya Bitcoin Wallet na usimamizi wa nodi yenye utendaji kamili wa Bitcoin umeme Wallet ambayo hurahisisha malipo ya Bitcoin, inawapa watumiaji udhibiti kamili wa fedha zao, na inaruhusu watumiaji wa hali ya juu zaidi kudhibiti nodi zao za Umeme kutoka kwenye kiganja cha mkono wao.


### ZEUS ni ya nani?

Kwa sasa ZEUS ni kwa watu wanaoendesha nodi zao za nyumbani / biashara kwa [Lightning Network Daemon (LND)](https://lightning.engineering/) au [Core Lightning (CLN)](https://blockstream.com/lightning/) na kuzisimamia kwa mbali kupitia Zeus.


Wafanyabiashara wanaotumia [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) au [Alby](https://getalby.com/) (au akaunti nyingine yoyote ya LNDhub) pia wanaweza kuunganisha, kutumia na kudhibiti nodi / akaunti zao kutoka ZEUS.


[Kuanzia v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/), ZEUS utaanza kuhudumia watumiaji wa kawaida wanaotaka njia rahisi ya kufanya malipo ya bitcoin ya haraka na ya bei nafuu kutoka kwenye kifaa chao cha mkononi, kwa kuwa na [node ya Lightning ya simu iliyojengewa ndani](https://docs.zeusln.app/category/embedded-node) yenye [Mtoa Huduma wa Lightning (LSP)](https://docs.zeusln.app/lsp/intro) aliyeunganishwa.


### Rasilimali muhimu za Zeus:


- Ukurasa rasmi wa wavuti wa Zeus - [https://zeusln.app/](https://zeusln.app/)
- Hati za Zeus - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Hifadhi ya Zeus kwenye Github](https://github.com/ZeusLN/zeus)
- [Kikundi cha msaada cha Zeus kwenye Telegram](https://t.me/ZeusLN)
- [Zeus kwenye NOSTR](https://iris.to/zeus@zeusln.app)
- [Matangazo ya Blogu ya Zeus](https://blog.zeusln.com)


### Vipengele vya Zeus

#### Vipengele vya jumla:


- Kujitunza, Bitcoin na Umeme tu Wallet
- Hakuna ada za usindikaji, Hakuna KYC
- Chanzo huria kabisa (APGLv3)
- Nodi nyingi / akaunti zinazotumika (unaweza kudhibiti nodi zako za nyumbani), endesha nodi iliyopachikwa ya LND, unganisha kwa akaunti nyingi za LNDhub)
- Rahisi kutumia menyu ya shughuli
- Usimbaji PIN au passphrase, Hali ya Faragha - ficha data yako nyeti
- Kitabu cha mawasiliano, mada nyingi, lugha nyingi


#### Vipengele vya kiufundi


- Unganisha kupitia Tor
- Usaidizi kamili wa LNURL (Lipa, toa, uthibitishaji, kituo), Tuma kwa anwani za Umeme
- Udhibiti wa kina wa kituo cha Mwangaza, usaidizi wa MPP/AMP, Keysend, usimamizi wa ada za uelekezaji
- Usaidizi wa Replace-by-fee (RBF) na Mtoto-kulipa-kwa-mzazi (CPFP)
- Malipo na maombi ya NFC, Saini na uthibitishe ujumbe
- SegWit na Taproot msaada
- Njia rahisi za Taproot
- Anwani za umeme za kujilinda (@zeuspay.com)
- Sehemu ya Uuzaji kwa Mraba (PoS itafunguliwa hivi karibuni)


### Miongozo na Mafunzo ya Video

Ili kuweza kutumia Zeus na kudhibiti chaneli za Umeme, ukwasi, ada n.k, ni bora kusoma kwanza miongozo muhimu kuhusu Lightning Network.


#### Waelekezi:


- [LND - Nyaraka za Lightning Network Daemon](https://docs.lightning.engineering/)
- [CLN - Nyaraka za Core Lightning](https://lightning.readthedocs.io/index.html)
- [Mwongozo wa Lightning kwa wanaoanza](https://bitcoiner.guide/lightning/) – na Bitcoin Q&A
- [Usimamizi wa Node ya Lightning](https://www.lightningnode.info/) – na openoms
- [Mtandao wa Lightning na mfano wa uwanja wa ndege](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Usimamizi wa ukwasi wa Node ya Lightning](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Matengenezo ya Node ya Lightning](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Mafunzo ya video na Vikao vya BTC


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Mwongozo wa kutembea jinsi ya kuanza kutumia nodi iliyopachikwa ya Zeus LN kwenye kifaa chako cha mkononi


![Image](assets/en/01.webp)


Ninatoa mwongozo huu kwa watumiaji wote wapya wa Lightning Network (LN) ambao wanataka kuanza safari mpya ya uhuru kwa kutumia nodi ya kujilinda ya Wallet kwenye vifaa vyao vya rununu.


Hebu tuzingatie kwamba tayari unapitia wingi huo wote wa pochi za LN za ulinzi, lakini hauko tayari kuanza kuendesha nodi ya UMMA ya LN ya kuelekeza, unataka tu kuweka Sats zaidi juu ya LN kwa njia ya kujidhibiti zaidi na kufanya malipo yako ya kawaida zaidi ya LN.


Hapa anakuja Zeus, kuanzia [toleo v0.8.0 lililotangazwa kwenye blogu yao](https://blog.zeusln.com/new-release-zeus-v0-8-0/), sasa inatoa node ya LND iliyojengewa ndani ya programu. Hadi sasa Zeus ilikuwa programu ya kusimamia node za mbali + akaunti za LNDhub. Lakini sasa… node ipo kwenye simu!


![Image](assets/en/02.webp)


### Muhtasari wa haraka wa huduma kuu za Node ya Zeus:



- Nodi ya kibinafsi ya **LND** - Hiyo ina maana kwamba nodi hii HAITAFANYA uelekezaji wa malipo ya watu wengine kwa umma kupitia nodi yako. Node na njia hazijatangazwa (za kibinafsi, hazionekani kwenye grafu ya umma ya LN). Kupokea na kufanya malipo kutafanywa kwa ukamilifu na washirika wako waliounganishwa wa LSP. **KUMBUKA**: Njia Iliyopachikwa ya Zeus HAITAFANYA uelekezaji wa umma!
- **Huduma endelevu ya LND** - mtumiaji anaweza kuwezesha kipengele hiki na kuweka huduma ya LND amilifu mfululizo kama nodi yoyote ya kawaida ya LN. Programu haifai kuwa wazi, huduma inayoendelea itaweka mawasiliano yote mtandaoni.
-   **Vichujio vya bloku vya Neutrino** - usawazishaji wa bloku unafanywa kwa kutumia [vichujio vya bloku na itifaki ya Neutrino](https://bitcoinops.org/en/topics/compact-block-filters/) (bila kutoa taarifa kuhusu fedha za on-chain za watumiaji wetu). Kumbuka: kwa muunganisho wa intaneti wenye ucheleweshaji mkubwa / polepole, usawazishaji huu wa bloku unaotegemea Neutrino wakati mwingine unaweza kushindwa. Kujaribu kubadilisha kwa seva ya Neutrino iliyo karibu kunaweza kusaidia kurejesha usawazishaji. Bila usawazishaji huu, nodi yako ya LND haiwezi kuanza!
- **Vituo Rahisi vya Taproot** - Wakati wa kufunga vituo hivi, watumiaji hutozwa ada kidogo na hupewa faragha zaidi kwa vile wanaonekana kupenda matumizi mengine yoyote ya Taproot wanapokagua alama zao za On-Chain.
- LSP iliyojumuishwa - Olympus ndio nodi mpya ya LSP ya Zeus. Watumiaji wanaweza kupokea Sats juu ya LN mara moja, bila kuwa na mipangilio ya awali ya vituo vya LN. Itabidi tu kuunda LN Invoice na kulipa kutoka LN Wallet nyingine yoyote, kwa huduma ya chaneli ya Zeus 0-conf. Soma zaidi kuhusu Zeus LSP hapa. LSP pia hutoa ufaragha ulioongezwa kwa watumiaji wetu kwa kuwapa ankara zilizofungwa ambazo huficha funguo zao za umma kutoka kwa walipaji.
- **Kitabu cha Anwani** - unaweza kuhifadhi mwenyewe anwani au kuagiza kutoka NOSTR, kwa ajili ya kutuma malipo kwa urahisi kwenye unakoenda mara kwa mara.
- Usaidizi kamili wa LNURL, LN Address tuma na upokee - sana unaweza kusanidi LN Address yako binafsi ukitumia @zeuspay.com. Kikumbusho: Unaweza pia kutumia Zeus kwa LN-auth kwenye tovuti ambazo unaweza kuingia kwa uthibitishaji wa LN. Inafaa sana.
- **Sehemu ya Uuzaji** - Sasa watumiaji wa wauzaji wanaweza kusanidi bidhaa zao na kuuza moja kwa moja kutoka kwa Zeus, kwa kutumia PoS iliyojumuishwa. Kwa sasa vyenye mahitaji ya msingi lakini katika siku zijazo itakuwa na vipengele virefu.
- **Kumbukumbu za LND** - mtumiaji anaweza kusoma kwa wakati halisi kumbukumbu za huduma za LND na kuzitumia kutatua masuala yanayowezekana (haswa kwa miunganisho mibaya)
- **Hifadhi Nakala Kiotomatiki** - chaneli za nodi za LN zinahifadhiwa nakala kiotomatiki kwenye seva ya Olympus. Nakala hii ya kiotomatiki imesimbwa kwa njia fiche na nodi yako ya Wallet seed (bila seed haina maana kabisa). Mtumiaji pia anaweza kusafirisha mwenyewe SCB (chelezo cha njia tuli) kwa uokoaji wa maafa.


### Jinsi ya kuingia kwenye Nodi ya Zeus LN (LND iliyopachikwa)


Katika mwongozo huu nitazungumza tu kuhusu nodi ya LND iliyojengewa ndani, na siyo njia nyingine za kutumia programu hii ya kipekee (usimamizi wa nodi za mbali na akaunti za LNDhub). Kwa aina nyingine za miunganisho, tafadhali rejelea [ukurasa wa Nyaraka za Zeus](https://docs.zeusln.app/category/getting-started), ambao umeelezwa vizuri sana na hauna haja ya mwongozo maalum.


#### HATUA YA 1 - KUWEKA MIPANGILIO YA AWALI


Kwa sababu ya ukweli kwamba Zeus ni nodi kamili ya LND nitakuwa na mapendekezo ya awali:



- Usitumie kifaa cha zamani, ambacho kinaweza kuathiri matumizi ya programu hii yenye nguvu. Hasa katika kipindi cha kusawazisha programu inaweza kutumia CPU na RAM kwa umakini. Ukosefu wa hizi unaweza hata kufanya haiwezekani kutumia programu ya Zeus.
- Tumia angalau Android 11 kama OS ya rununu na usasishe kadri uwezavyo. Kwa iOS sawa, jaribu kutumia toleo la juu zaidi la OS.
- Utahitaji angalau nafasi ya diski 1GB kwa hifadhi ya data. Baada ya muda inaweza kukua zaidi, lakini kuna utendaji wa kuunganisha hifadhidata kwa kiwango cha MB.
- HAKUNA haja ya kutumia Zeus na huduma ya Tor au Orbot. Tafadhali usifanye mambo kuwa magumu zaidi kuliko inavyohitajika. Tor katika kesi hii haitakupa faragha zaidi lakini itazidisha mambo kwa usawazishaji wa kwanza. Pia kuwa mwangalifu na ni VPN gani unaitumia na angalia muda wa muunganisho kuelekea seva za neutrino. Kumbuka, kichujio cha kuzuia Neutrino hakivuji au kufuatilia utambulisho wa kifaa chako, ni vizuizi tu. Trafiki ya LN pia iko nyuma ya LSP iliyo na chaneli za kibinafsi kwa hivyo habari chache sana zimetolewa, hakuna sababu ya kuogopa kuhusu faragha.
-   Kuwa na subira kwa usawazishaji wa awali, unaweza kuchukua dakika kadhaa. Jaribu kuunganishwa na muunganisho wa intaneti wa broadband wenye latency nzuri. Ikiwa unaendesha nodi yako ya Bitcoin, [unaweza kuwezesha huduma ya neutrino](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core) na kuunganisha Zeus wako kwenye nodi yako mwenyewe, hata kwa kutumia LAN ya ndani, ili upate kasi ya juu zaidi.


Mara baada ya kusanidi aina ya muunganisho "Njia iliyopachikwa" programu itaanza kusawazisha kwa muda. Subiri kwa subira ili kumaliza sehemu hiyo, kisha uingie kwenye ukurasa mkuu wa Mipangilio.


![Image](assets/en/03.webp)


Kwa kifupi, hebu tuzame katika kila sehemu ya Mipangilio na tuelewe baadhi ya vipengele vikuu, kabla ya kuanza kutumia Zeus:


**A - MIPANGILIO**


Hii ni sehemu iliyo na mipangilio ya jumla ya programu nzima


**1 - Lightning Service Provider (LSP)**


Hapa kuna huduma mbili za LSP:



- _Kwa wakati tu chaneli_ - wakati huna chaneli yoyote iliyofunguliwa au inayoingia inayopatikana, huduma ikiwashwa itakufungulia chaneli popote ulipo. Chaguo hili linaweza kuzimwa ikiwa hutaki kufungua vituo zaidi vya aina hii.
- _Omba vituo mapema_ - unaweza kununua chaneli zinazoingia kutoka kwa Olympus LSP moja kwa moja kwenye programu ukitumia chaguo na viwango vingi (kwa zinazoingia na kutoka).


LSP husaidia kuunganisha watumiaji kwenye mtandao wa Lightning kwa kufungua njia za malipo kwenye nodi zao. [Soma zaidi kuhusu LSP hapa](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS ina LSP mpya iliyoingizwa inayoitwa [OLYMPUS by ZEUS](https://mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), inayopatikana kwa watumiaji wote wanaotumia nodi mpya iliyojengewa ndani.


Katika sehemu hii, kwa chaguo-msingi ni Olympus LSP ( https://0conf.lnolymp.us ), lakini hivi karibuni unaweza pia kuweka 0conf LSP nyingine inayotumia itifaki hii.


_Kumbuka:_

_unapofungua chaneli na Olympus LSP kwa kutumia ankara zilizofungwa za LN pia unapata ukwasi unaoingia wa 100k! Hili ni chaguo zuri ikiwa utahitaji kupokea mara moja zaidi Sats._

_Mfano: unaweka 400k Sats ili kufungua chaneli ya LSP, kisha LSP inafungua chaneli yenye uwezo wa 500k Sats kuelekea nodi yako ya Zeus na kusukuma 400k Sats unayoweka upande wako._

_"Kiwango cha fedha kinachoingia" = "nafasi" zaidi katika kituo chako ili kupokea._


Katika siku zijazo tunatumai tunaweza kuwa na LSP nyingine nyingi ambazo zinaweza kuunganishwa katika Zeus na kutumia njia mbadala kila moja. Ni suala la muda tu hadi LSP mpya zipitishe kiwango wazi kwa aina hizi za chaneli za 0conf.


Ikiwa hutaki kufungua vituo vipya "kwa kuruka", unaweza kuzima chaguo hili.


Katika sehemu hii hii, pia una chaguo la kuchagua "omba Njia Rahisi za Taproot" wakati LSP itafungua kituo kuelekea nodi yako ya Zeus. Vituo hivi Rahisi vya Taproot vinatoa faragha bora zaidi ya On-Chain na ada za chini wakati wa kufunga chaneli. Kuna sababu mbili tu ambazo hutaki kuzitumia:



- Ni mpya, na bado kunaweza kuwa na mende katika LND wakati wa kuzitumia.
- Mwenzako hauungi mkono. Hata nodi za LND zinapaswa kujijumuisha kwa uwazi, kwa sasa.


**2 - Mipangilio ya malipo**


Kipengele hiki kitakupa njia ya kuweka ada unazopendelea za malipo, zaidi ya LN au onchain. Pia toa chaguo la kuongeza au kupunguza muda wa kuisha kwa ankara zako.


Ikiwa baadhi ya malipo yako ya LN yatashindwa, unaweza kuongeza ada ili kupata njia bora zaidi. Pia ikiwa unafanya onchain txs, unaweza kusanidi ada mahususi ili tx yako isiishie kukwama kwenye Mempool kwa muda mrefu, ikiwa ni muda wa ada ya juu.


**3 - Mipangilio ya ankara**


Katika sehemu hii kuna chaguzi kadhaa za ankara za generate:



- Weka memo ya kawaida ya kuonyeshwa katika Invoice wewe generate
- Muda wa mwisho wa matumizi katika sekunde, ikiwa ungependa muda maalum, mrefu au mfupi zaidi kwa Invoice yako kulipwa
- Jumuisha vidokezo vya njia - toa maelezo ili kupata vituo visivyotangazwa au vya faragha. Hii inaruhusu uelekezaji wa malipo kwa nodi ambazo hazionekani hadharani kwenye mtandao. Kidokezo cha uelekezaji hutoa njia ya sehemu kati ya nodi ya kibinafsi ya mpokeaji na nodi ya umma. Kidokezo hiki cha uelekezaji basi kinajumuishwa kwenye Invoice inayotolewa na mpokeaji na kutolewa kwa mlipaji. Ninapendekeza iwashwe kwa chaguomsingi, vinginevyo malipo yanayoingia yanaweza kushindwa (hakuna njia iliyopatikana).
- AMP Invoice - Malipo ya Njia Nyingi za Atomiki ni aina mpya ya malipo ya Umeme inayotekelezwa na LND ambayo inaruhusu kupokea Sats bila Invoice mahususi, kwa kutumia [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/tuma-messages-with-key). Ni msimbo wa malipo tuli. [Soma zaidi hapa](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Onyesha sehemu ya taswira maalum - tumia chaguo hili tu katika hali mahususi wakati unataka kutumia sehemu maalum katika taswira. [Soma zaidi hapa](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Chaguo jingine katika sehemu hii ni jinsi ya kuweka aina ya onchain Address unayotaka kutumia: SegWit nested, SegWit, Taproot.


![Image](assets/en/04.webp)


Bofya kwenye kitufe cha gurudumu la juu na skrini ibukizi itaonekana ili kuchagua aina inayotakiwa ya Address. Mara tu ukiweka hiyo, wakati mwingine unapogonga kitufe cha kupokea kwa onchain, itakuwa generate aina ya Address iliyochaguliwa. Unaweza kuibadilisha wakati wowote.


**4 - Mipangilio ya vituo**


Katika sehemu hii unaweka mapema baadhi ya vipengele vya kufungua vituo kama vile:



- idadi ya uthibitisho
- Tangaza kituo (kwa chaguomsingi kimezimwa), hiyo inamaanisha kuwa kitakuwa chaneli ambazo hazijatangazwa
- Njia rahisi za Taproot
- Onyesha kitufe cha ununuzi wa kituo


**5 - Mipangilio ya faragha**


Hapa utapata mipangilio ya msingi ya kuongeza faragha zaidi kwa kutumia programu ya Zeus:



- Block explorer ili kufungua maelezo ya tx (Mempool.space, blockstream.info au ya kibinafsi maalum)
- Soma ubao wa kunakili - washa/uzima kugeuza ikiwa unataka Zeus kusoma ubao wa kunakili wa kifaa chako
- Hali ya Lurker - kuwasha/kuzima geuza ikiwa unataka kuficha maelezo mahususi nyeti kutoka kwa programu yako ya Zeus. Ni chaguo zuri unapotengeneza onyesho au picha za skrini.
- Pendekezo la ada ya Mempool - wezesha chaguo hili ikiwa ungependa kutumia viwango vya ada vinavyopendekezwa kutoka [Mempool.space](https://Mempool.space/)


**6 - Usalama**


Sehemu hii ina chaguo mbili pekee za kulinda programu wakati wa kufungua: weka nenosiri au PIN.


Mara tu unapoweka PIN ili kufungua programu, unaweza pia kuweka "PIN ya kulazimisha". PIN hii ya ziada ya siri itatumika TU katika hali ya kulazimishwa, ikiwa unatishiwa. Ukiweka PIN hii, usanidi utakuwa wote FUTA. Kwa hivyo ni bora uendelee kusasisha nakala zako. Hifadhi rudufu otomatiki IMEWASHWA kwa chaguomsingi, lakini ni vizuri kuwa na nakala zako pia, nje ya kifaa.


**7 - Sarafu**


Washa au uzime chaguo la kuonyesha ubadilishaji wa sarafu ya fiat katika matumizi ya programu ya Zeus. Hivi sasa inasaidia zaidi ya sarafu 30 za fiat duniani kote.


**8 - Lugha**


Unaweza kubadilisha kati ya lugha nyingi za tafsiri, zilizokaguliwa na jumuiya ya Zeus yenye wazungumzaji asilia.


**9 - Onyesho**


Katika sehemu hii unaweza kubinafsisha onyesho lako la Zeus, ukichagua mandhari mbalimbali za rangi, skrini chaguo-msingi (kibodi au salio), onyesha lakabu yako ya nodi, washa vitufe vikubwa vya vitufe, onyesha sehemu zaidi za desimali.


**10 - Pointi ya Uuzaji**


Hiki ni kipengele maalum cha kuwezesha / kuzima mfumo jumuishi wa PoS kwenye Zeus. Unaweza kuendesha PoS iliyojitegemea au iliyounganishwa na mfumo wa Square PoS. Kwa sasa inasaidia utendakazi wa kimsingi kama PoS, lakini inatosha kwa mwanzo mzuri na inaweza kuwasaidia wafanyabiashara hao wadogo (baa/mikahawa, mboga) kuanza kukubali BTC kwa njia asili.


Ndani ya mipangilio hii, utapata chaguzi mbalimbali za kusanidi PoS yako:



- Aina ya malipo ya uthibitishaji: LN pekee, 0-conf, 1-conf
- Washa / zima vidokezo kwa mfanyakazi anayetumia PoS
- Onyesha / ficha vitufe
- Asilimia ya kodi ya kutuma maombi kwenye tikiti
- Unda bidhaa na kategoria za bidhaa
- Orodha rahisi ya mauzo yote


Hapa kuna video ya demo ya moja kwa moja jinsi ya kutumia Zeus PoS:


**B - Hifadhi nakala ya Wallet**


Nodi iliyopachikwa katika ZEUS inategemea LND na hutumia [umbizo la aezeed seed](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Hii ni tofauti na [umbizo la BIP39] la kawaida (https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) unaona katika pochi nyingi za Bitcoin, ingawa inaweza kuonekana kuwa sawa. Aezeed inajumuisha data ya ziada ikiwa ni pamoja na tarehe ya kuzaliwa ya Wallet ambayo itasaidia kuchanganua upya wakati wa urejeshaji kutokea kwa ufanisi zaidi.


Umbizo la ufunguo wa aezeed unapaswa kuendana na pochi zifuatazo za rununu: Blixt, BlueWallet na Breez. Kumbuka kuwa seed pekee haitatosha kurejesha salio zako zote ikiwa una njia zilizofunguliwa au zinazosubiri kufungwa !


Pata maelezo zaidi kuhusu mchakato wa kuhifadhi nakala na kurejesha kwenye [ukurasa wa Hati za Zeus](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


USHAURI WA NGUVU: Unapohifadhi seed yako, tafadhali hifadhi pia pubkey ya nodi! Wakati mwingine ni vizuri kuwa nayo, pamoja na seed yako na SCB (Nakala ya Njia Tuli) ikiwa utahitaji kuthibitisha urejeshaji.


SCB inahitajika tu ikiwa una chaneli za LN zimefunguliwa. Ikiwa una pesa za onchain tu, sio lazima.


Ikiwa unaona kwamba baada ya muda mrefu bado hauonyeshi txs za historia ya zamani, nenda kwa nodi Iliyopachikwa - Wenzake na uzima chaguo la kutumia orodha ya wenzao waliochaguliwa (kwa chaguo-msingi ni btcd.lnolymp.us). Hiyo itaanzisha kuwashwa upya na itaunganishwa na nodi ya neutrino inayopatikana kwanza na jibu bora la wakati. Au tumia mvuto uliotajwa wenzao wengine wanaojulikana wa neutrino.


Iwapo ungependa kuona chaguo zaidi za urejeshaji za nodi ya LND, [tafadhali soma mwongozo wangu wa awali](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), ambapo unaweza kupata hatua za jinsi ya kuingiza seed iliyoazwa kwenye Sparrow Wallet au njia nyinginezo.


**C - Njia Iliyopachikwa**


Katika sehemu hii tutapata zana za kimsingi za kudhibiti nodi iliyojumuishwa:



- _Urejeshaji Maafa_ - Hifadhi rudufu za kiotomatiki na za mwongozo za chaneli za LN. Tafadhali soma zaidi jinsi ya kutumia kipengele hiki kwenye ukurasa wa Hati za Zeus.
- _Express Graph Sync_ - Programu ya Zeus itapakua grafu ya data ya LN kutoka kwa seva maalum, kwa ulandanishi wa haraka na bora zaidi, kutoa njia bora zaidi za malipo. Unaweza pia kuchagua kufuta data ya awali ya grafu wakati wa kuanza.
- _Peers_ - sehemu ya kudhibiti wenzao wa neutrino na wenzao wa 0-conf. Ikiwa una matatizo na usawazishaji wa kwanza, vituo havitumii mtandaoni, ni kwa sababu kifaa chako kina muda wa kusubiri wa hali ya juu na programu rika ya neutrino iliyosanidiwa. Jaribu kubadilisha orodha ya programu zingine unazopendelea au ongeza programu nyingine mahususi ambayo unajua ina muda bora wa kusawazisha. Seva za neutrino zinazojulikana ni:



 - btcd1.lnolymp.us | btcd2.lnolymp.us - kwa eneo la Marekani
 - sg.lnolymp.us - kwa eneo la Asia
 - btcd-Mainnet.lightning.computer - kwa eneo la Marekani
 - uswest.blixtwallet.com (Seattle) - kwa eneo la Marekani
 - europe.blixtwallet.com (Ujerumani) - kwa kanda ya EU
 - asia.blixtwallet.com - kwa mkoa wa Asia
 - node.eldamar.icu - kwa eneo la Marekani
 - noad.sathoarder.com - kwa mkoa wa Amerika
 - bb1.breez.teknolojia | bb2.breez.technology - kwa eneo la Marekani
 - neutrino.shock.network - eneo la Marekani



- _Kumbukumbu za LND_ - zana muhimu sana ya kutatua masuala ya nodi zako za LN na kudhibiti kwa kina kile kinachoendelea kwa kiwango cha kiufundi zaidi.
- _Mipangilio ya hali ya juu_ - zana zaidi za kudhibiti matumizi ya nodi yako ya LND:



 - _Modi ya kutafuta njia_ - njia mbili au za awali, njia za kupata njia bora ya malipo yako ya LN na pia kuweka upya maelezo ya awali ya uelekezaji. Tafadhali soma miongozo hii mizuri sana kuhusu kutafuta njia: [Pathfinding](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - by Docs Lightning Engineering na [LN Payment Utafutaji njia](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - by Voltage
 - _LND_Inayoendelea - washa hali hii ikiwa ungependa huduma ya LND iendeshe chinichini na uweke kifundo chako mtandaoni 24/7. Hii ni muhimu sana ikiwa unatumia Zeus kama PoS kwenye duka ndogo au unapokea vidokezo vingi vya LN juu ya LN Address.
 - _Changanua tena pochi_ - chaguo hili litaanzisha wakati wa kuanzisha upya uchanganuzi kamili wa txs zote za onchain za Wallet yako. Iwashe ikiwa tu unakosa baadhi ya txs kwenye Wallet yako. Kazi ya kuchambua upya itachukua muda, dakika kadhaa kwa hivyo kuwa na subira na uangalie kumbukumbu kila wakati ili kuona maelezo zaidi kuhusu maendeleo.
 - _Compact Database_ - chaguo hili ni muhimu sana ikiwa programu yako ya Zeus inachukua nafasi nyingi za kifaa (angalia maelezo ya programu katika mipangilio ya kifaa chako). Ikiwa una shughuli nyingi kwa kutumia Zeus, ningependekeza kufanya compaction hii mara nyingi zaidi. Mara tu unapoona kuwa una data zaidi ya 1-1.5GB ya programu ya Zeus, fanya ujumuishaji. Itaanza upya na kuchukua muda, kwa hivyo kuwa na subira.
 - _Futa faili za Neutrino_ - chaguo hili la kufuta faili za neutrino (kwa kuwasha upya) litapunguza sana matumizi ya hifadhi ya data. Kupunguza matumizi ya data pia kuna athari kubwa katika matumizi ya betri, kupunguza matumizi ya betri, haswa ikiwa unatumia Zeus katika hali inayoendelea.


**D - Maelezo ya Nodi**


Katika sehemu hii, utapata maelezo zaidi kuhusu hali ya nodi yako ya Zeus kama:



- Lakabu - kitambulisho cha nodi fupi
- Ufunguo wa Umma - ufunguo kamili wa umma wa nodi yako inayohitajika kwa nodi zingine kupata njia hiyo kuelekea nodi yako. Kumbuka kwamba pubkey hii HAIONEKANI kwenye Vivinjari vya kawaida vya LN (Mempool, Amboss, 1ML n.k). Kitufe hiki cha pubkey kinaweza kufikiwa TU kupitia programu zingine na chaneli zako zilizounganishwa za LN.
- Toleo la utekelezaji wa LN
- Toleo la programu ya Zeus
- Imesawazishwa kwa mnyororo na Imesawazishwa kwa hali ya grafu - muhimu sana, inayoonyesha hali sahihi ya nodi yako. Ikiwa hizi mbili hazionyeshi "kweli" inamaanisha kuwa nodi yako bado inasawazisha au ina matatizo fulani ya kusawazisha. Kwa hivyo inashauriwa kuangalia kumbukumbu zako za LND au subiri muda mrefu zaidi.
- Urefu wa kuzuia na Hash - inaonyesha kizuizi cha mwisho na Hash ambayo nodi yako iliona na kusawazisha.


**E - Taarifa za Mtandao**


Sehemu hii inaonyesha maelezo zaidi kuhusu hali ya jumla ya Lightning Network, iliyotolewa kutoka kwa data yako ya kusawazisha grafu: idadi ya vituo vya umma vinavyopatikana, idadi ya nodi, idadi ya chaneli za zombie (nje ya mtandao au iliyokufa), kipenyo cha grafu, wastani na kiwango cha juu zaidi cha nje cha grafu.


Data hii ya maelezo inaweza kuwa muhimu kutatua au kutumika tu kwa takwimu.


**F - Umeme Address**


Katika sehemu hii mtumiaji anaweza kusanidi ulinzi wake binafsi LN Address @zeuspay.com.


ZEUS PAY hutumia heshi za awali zinazozalishwa na mtumiaji, ankara za HODL, na mpango wa uthibitishaji wa Zaplocker Nostr ili kuruhusu watumiaji ambao huenda hawako mtandaoni 24/7 kupokea malipo kwa umeme tuli wa Address. Watumiaji wanahitaji tu kuingia kwenye pochi zao za ZEUS ndani ya saa 24 ili kudai malipo, vinginevyo watarejeshwa kwa mtumaji.


Ukiwasha "hali inayoendelea" malipo yote kwa LN Address yako yatapokelewa papo hapo.


Pata maelezo kuhusu jinsi malipo ya [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) yanavyofanya kazi na zaidi kuhusu [Ada za ZeusPay hapa](https://docs.zeusln.app/lightning-Address/fees).


**G - Anwani za Onchain**


Katika sehemu hii unaweza kushauriana na anwani zako ulizozalisha za onchain kwa udhibiti bora wa sarafu


**H - Anwani**


Kitabu kipya cha mawasiliano kilianzishwa katika Zeus v 0.8.0 ambacho unaweza kutumia kutuma malipo kwa haraka kwa marafiki na familia yako, pia kikiwa na uwezo wa kuleta anwani zako kutoka Nostr.


Ingiza kwa urahisi Nostr npub yako au NIP-05 Address inayoweza kusomeka na binadamu, na ZEUS itaulizia Nostr kwa anwani zako zote. Ukiwa hapo unaweza kutuma malipo ya haraka kwa mtu unayewasiliana naye, au kuleta zote au kuchagua anwani kwenye kitabu chako cha mawasiliano cha karibu nawe./<


Hapa kuna video fupi jinsi ya kusanidi na kutumia anwani zako za Zeus:


**Mimi - Zana**


Hapa tuna sehemu ndogo tofauti zilizo na zana zaidi:



- _Akaunti_ - hapa unaweza kuingiza akaunti / pochi za nje, pochi za Cold, pochi za Hot, ili kudhibiti au kutumia kama chanzo cha ufadhili wa nje kwa chaneli zako za nodi ya Zeus. Kipengele hiki bado ni cha majaribio.
- _Ongeza kasi ya muamala_ - Kipengele hiki kinaweza kukusaidia unapokuwa na tx iliyokwama kwenye Mempool na ungependa kufidia ada. Utahitaji kutoa matokeo ya tx kutoka kwa maelezo ya tx na uchague ada mpya unayotaka kutumia. Lazima iwe ya juu kuliko ya awali na ikuhitaji uwe na pesa zaidi zinazopatikana kwenye onchain yako Wallet.


![Image](assets/en/05.webp)


Inabidi uende kwa tx yako inayosubiri na unakili sehemu ya nje ya txid. Kisha njoo kwenye sehemu hii na ubandike, kisha uchague ada mpya unayotaka kutumia ili kuibandika. Itaonyesha skrini mpya yenye ada zinazopendekezwa katika wakati huo, au unaweza kuweka maalum. Kumbuka LAZIMA iwe juu zaidi ya ile iliyopita.


Daima ni bora kuweka UTXO yenye upeo wa 100k Sats kwenye Zeus onchain Wallet yako, ili uweze kuitumia kulipia ada inapobidi.



- _Saini au uthibitishe_ - ​​Kwa kipengele hiki unaweza kutia sahihi ujumbe mahususi kwa funguo zako za Wallet. Pia inaweza kutumika kuthibitisha ujumbe ili kuthibitisha kuwa unatoka kwa funguo maalum za Wallet.
- _Kigeuzi cha sarafu_ - zana rahisi ya kukokotoa ubadilishaji wa kiwango kati ya BTC na sarafu zingine za fiat.


**J - Bidhaa na Usaidizi**


Hapa utapata maelezo zaidi na viungo kuhusu Zeus, duka la mtandaoni, wafadhili, mitandao ya kijamii.


**K - Msaada**


Katika sehemu hii ya mwisho utapata viungo vya ukurasa wa nyaraka wa Zeus, masuala ya Github (ikiwa unataka kuchapisha hitilafu au ombi moja kwa moja kwa wasanidi programu), usaidizi wa barua pepe.



### HATUA YA 2 - ANZA KUTUMIA ZEUS NODE



Kumbuka, Zeus itatumika zaidi kama LN Wallet, kwa malipo rahisi na ya haraka zaidi ya LN. Hakika, pia ina onchain Wallet, lakini hiyo inapaswa kutumika kwa ajili ya kufungua / kufunga chaneli za LN pekee na si kwa malipo ya kawaida ya kahawa.


Tafadhali soma mwongozo wangu mwingine kuhusu [jinsi ya kuwa benki yako mwenyewe kwa kutumia viwango 3 vya Stash](https://darth-coin.github.io/beginner/be-your-own-bank-sw.html).


Kwa wakati huu mtumiaji ana njia 2 za kuanza kutumia Zeus:



- Moja kwa moja juu ya LN, kwa kutumia chaneli ya 0-conf kutoka Olympus LSP
- Weka kwanza kwenye onchain Wallet na kisha ufungue chaneli ya kawaida ya LN na programu rika unayotaka.


#### Njia A - Kutumia Olympus LSP


Hii ni njia rahisi sana na iliyonyooka ya kuabiri mtumiaji mpya wa LN na Zeus. Inaweza kuwa mtumiaji mpya kabisa wa Bitcoin ambaye hana Sats hata kidogo, amepanda na rafiki, au mfanyabiashara mpya anayeanza na malipo yake ya 1 ya LN.


Kwa chaguo-msingi, Zeus itatumia LSP yake, Olympus. Lakini baadaye unaweza kubadilisha pia kwa LSP zingine zinazotumia itifaki hii ya 0-conf kufungua vituo.


Kwa kuunda Invoice kwenye Zeus yako (weka kiasi na ubofye kitufe cha "ombi"), utaweza kupokea hizo Sats mara moja.


Invoice you generate [itafungwa](https://docs.zeusln.app/lsp/wrapped-invoices) na utawasilishwa ada zinazohusiana na huduma ikiwa zitalipwa. Invoice hii iliyofunikwa ina vidokezo vya njia kuelekea nodi yako ya Zeus, ili LSP ipate nodi yako mpya na kufungua chaneli kwa kutumia pesa mpya unazoweka.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Ili kupata chaneli ya LN kutoka LSP kwa fedha unazotaka kupokea mara ya kwanza, Invoice hii lazima ilipwe kutoka kwa LN Wallet nyingine na usubiri muda mfupi hadi LSP ifungue chaneli kuelekea eneo lako la Zeus, ondoa ada na usukuma kiasi kilichobaki cha malipo upande wako wa kituo.


Unachotakiwa kufanya ni kulipa Invoice iliyotengenezewa kwa ajili yako katika ZEUS ukitumia umeme mwingine wa Wallet, na kituo chako kitafunguka papo hapo. [Tafadhali rejea ada za Zeus LSP](https://docs.zeusln.app/lsp/fees).


Faida nyingine ya kulipia kituo ni uelekezaji wa ada sifuri. Hiyo inamaanisha wakati wa kuelekeza malipo, marudio ya kwanza kupitia OLYMPUS na ZEUS hailipi ada za uelekezaji. Kumbuka, kwamba kurukaruka zaidi ya OLYMPUS kwa ZEUS bado kutakutoza.


Mara tu kituo kikiwa tayari, bofya kwenye kitufe cha kulia chini ya skrini, kinachoonyesha chaneli za Zeus.


![Image](assets/en/08.webp)


Na utaona chaneli kama hii, inayoonyesha upande wako wa salio la kituo:


![Image](assets/en/09.webp)


Kwa zaidi utakayotumia kutoka kwa chaneli hii, utapata ukwasi zaidi unaoingia. Kwa Sats zaidi utapokea kwenye chaneli hii, utakuwa na nafasi ndogo ya ukwasi unaoingia.


Hapa kuna onyesho zuri la kuona (na Rene Pickhardt) kuhusu jinsi chaneli za LN zinavyofanya kazi:


Kwa wakati huu, ukizingatia skrini ya onyesho ya chaneli, bofya kwenye jina la kituo na utaona maelezo zaidi kuihusu.


Una chaneli moja na Olympus, ya jumla ya uwezo wa 490 000 Sats, na salio la 378k Sats upande wako na 88k Sats upande wa Olympus. Hiyo inamaanisha kuwa unaweza kupokea kiwango cha juu zaidi cha 88k Sats katika kituo kimoja.


Ikiwa unahitaji kupokea zaidi ya 88k Sats (kiasi kinachopatikana cha ndani katika kesi hii), hebu tuseme 500k Sats nyingine, kwa kuunda tu LN Invoice mpya na kiasi hicho, itasababisha ombi jipya la kituo kwa Olympus LSP. Kwa hivyo utapata chaneli ya 2.


Ndiyo sababu, ili kuepuka kulipa ada zaidi kwa kufungua njia nyingi, inashauriwa kufungua mara ya kwanza kituo kikubwa, tuseme 1-2M Sats. Mara tu ikiwa imefunguliwa, unaweza kubadilishana na sehemu ya onchain ya hizo Sats, tuseme 50%, kwa kutumia huduma yoyote ya ubadilishanaji wa nje iliyoelezewa katika mwongozo huu.


Mara tu unapobadilishana kutoka kwa chaneli hiyo, tuseme 50% na urejeshe Sats kuwa Zeus onchain Wallet yako mwenyewe, uko tayari kwenda kwa njia inayofuata ya kufungua chaneli mpya - kutoka kwa salio la onchain.


#### Njia B - Kutumia salio lako la onchain


Kwa njia hii unaweza kufungua njia kuelekea nodi nyingine yoyote ya LN, ikiwa ni pamoja na Olympus LSP sawa. Lakini ikiwa tayari unayo chaneli na Olympus inashauriwa kuwa nayo na nodi nyingine, kwa kuegemea zaidi na pia inaweza kutumia MPP (malipo ya sehemu nyingi).


![Image](assets/en/10.webp)


Hapo juu ni mfano wa kulipa LN Invoice kwa kutumia MPP. Kama unavyoona chini ya skrini una "mipangilio" na inafungua ukurasa wa kushuka wenye maelezo zaidi ya malipo unayokaribia kufanya. Katika skrini hiyo, ikiwa una angalau chaneli 2 zilizofunguliwa, kipengele cha MPP KITAWASHWA kwa chaguomsingi. Pia unaweza kuwezesha AMP (njia nyingi za atomiki) na kuweka sehemu maalum unazotaka. Hiki ni kipengele chenye nguvu!


Kwa nodi ya kibinafsi kama Zeus, ningependekeza kuwa na chaneli 2-3 nzuri (max. 4-5), zenye LSP nzuri na ukwasi mzuri ili kukidhi mahitaji yako yote ya kulipa au kupokea Sats zaidi ya LN. [Angalia ushauri zaidi wa ukwasi wa nodi za LN katika mwongozo huu](/nodes/managing-lightning-node-liquidity-en.html). Pia huu hapa [mwongozo wa jumla kuhusu ukwasi wa LN](https://Bitcoin.design/guide/how-it-works/liquidity/) kutoka kwa timu ya Usanifu ya Bitcoin.


Kuchagua marafiki sahihi, najua, si kazi rahisi, hata kwa watumiaji wenye uzoefu. [Kwa hivyo nitakupa chaguo kadhaa ili uanze](https://github.com/ZeusLN/zeus/discussions/2265), hizi ni nodi rika ambazo nilijijaribu kwa kutumia Zeus (nilijaribu kuunganisha kwenye nodi za LND pekee ili kuepusha masuala ya kutotangamana)


Hapa pia kuna orodha ya wenzao wa nodi waliothibitishwa kwa Zeus. Ikiwa unawajua wazuri, unakaribishwa kuwaongeza kwenye orodha hiyo.


Unaweza kufungua chaneli katika Zeus kwa kwenda kwenye mwonekano wa Vituo kwa kubofya ikoni ya kituo kwenye kona ya chini kulia ya mwonekano mkuu, na kisha kugonga ikoni ya + kwenye kona ya juu kulia.


![Image](assets/en/11.webp)


Iwapo ungependa kufungua kituo chenye nodi mahususi, bofya kwenye (A) kona ya juu ili kuchanganua nodi ya QR (kwenye Mempool, Amboss, 1ML unaweza kupata QR hiyo) na maelezo yote ya programu zingine yatawekwa watu.


KUMBUSHO:


- Nodi iliyopachikwa ya Zeus usitumie huduma ya Tor ! Kwa hivyo tafadhali usijaribu kufungua chaneli zilizo na nodi zilizo chini ya Tor! Unajidhuru zaidi kuliko kuongeza faragha zaidi. Tor kwa LN haitoi faragha zaidi lakini inaongeza shida zaidi.
- chagua kwa busara wenzako, bora uwe LSP wazuri, nodi nzuri za kuelekeza, si nodi za nasibu ambazo zinaweza kufunga chaneli zako na zisingeweza kutoa ukwasi mzuri. [Hapa niliandika mwongozo maalum](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) kuhusu ukwasi na mfano wa nodi.


Ukibofya moja kwa moja kitufe cha "Fungua Mkondo kwa Olympus" utajaza sehemu zinazohitajika ili kufungua kituo kwa [OLYMPUS na ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


Tofauti na vituo vya kulipia vya LSP, kituo chako kitahitaji uthibitisho wa On-Chain, kwa kutumia pesa zako za onchain (unaweza kuchagua kutoka kwa UTXO zako katika mwonekano wa wazi wa kituo); haitafunguka mara moja. Tafadhali tazama kwanza ada halisi za Mempool na uzirekebishe ipasavyo, kulingana na kasi unayotaka kufungua kituo hicho.


Kabla ya kubofya kitufe ili kufungua kituo, telezesha chini chaguo za kina:


![Image](assets/en/12.webp)


Utahitaji pia kuhakikisha kuwa chaneli haijatangazwa (faragha). Kwa chaguo-msingi chaguo limezimwa kwa vituo vilivyotangazwa. Chaguo hili halipendekezwi kuamilishwa kwa nodi iliyopachikwa ya Zeus, ni muhimu tu unapotumia Zeus na nodi yako ya mbali, kama nodi ya uelekezaji wa umma.


Tofauti na vituo vya kulipia vya LSP, hutanufaika na uelekezaji wa ada sifuri kwa kufungua vituo ukitumia njia hii.


Na kufanyika, bonyeza tu kwenye kifungo "Fungua Channel", kusubiri tx kuthibitishwa na wachimbaji. Baada ya kituo kufunguliwa unaweza kufanya shughuli upendavyo ukitumia Sats kutoka kwa vituo vyako.


Kumbuka kuwa chaneli hizi zitakuwa na salio lote upande WAKO, kwa hivyo hutakuwa na ukwasi unaoingia. Kama nilivyosema awali, badilishana au utumie baadhi ya Sats kununua vitu zaidi ya LN ili "kutengeneza nafasi zaidi" ili kupokea.


Fikiria chaneli zako za LN kama glasi ya maji. Unamwaga maji (Sats) kwenye glasi tupu (chaneli yako) hadi uijaze. Huwezi kumwaga maji zaidi hadi unywe (kutumia / kubadilishana). Wakati glasi iko karibu tupu, mimina maji zaidi (Sats) ndani yake kwa kutumia ubadilishaji. [Soma zaidi kuhusu huduma za kubadilishana nje hapa](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


Pia kuna huduma zingine za LSP kama kukuuzia chaneli zinazoingia: LNBig au Bitrefill. Nadhani ni huduma zaidi kama hizi lakini siwezi kuzikumbuka kwa sasa.


Kwa hivyo ikiwa unahitaji kivitendo chaneli tupu ya LN (salio ni 100% kwa upande wa programu zingine tangu mwanzo), kwa ajili ya kupokea malipo zaidi ya unavyoweza kushughulikia kwenye chaneli zako zilizojazwa zilizopo, hili linaweza kuwa chaguo zuri sana. Utalipa ada mahususi kwa kufungua chaneli hizi na utapata nafasi nyingi za kuingia.



## VIDOKEZO NA HILA


### Vikomo vya hifadhi inayoingia


Hivi sasa, kutokana na baadhi ya mapungufu ya msimbo wa LN haiwezekani kupokea ni kiasi gani hasa kinachoonyeshwa katika "Inbound". Kumbuka kila wakati kwamba unapaswa kufanya ankara zako kwa kiasi kidogo, mtawalia kiasi cha "Hifadhi ya Ndani ya Kituo".


![Image](assets/en/13.webp)


Kama unaweza kuona kwenye picha hapo juu, "inbound" inaonyesha kwamba bado ninaweza kupokea 5101 Sats, lakini kwa kweli katika wakati huu haiwezekani kupokea zaidi. Na unaweza kuona kwamba ni kiasi sawa na "Hifadhi ya Ndani".


Kwa hivyo kumbuka, unapofanya ankara za kupokea, angalia pia ukwasi wa vituo vyako na utoe hifadhi ya ndani kutoka kwa kiasi hicho, ikiwa ungependa kusukuma hadi kikomo kiasi kinachoweza kupokelewa.


### Ushauri wa haraka kwa watumiaji wapya kuanzia na nodi ya Zeus:



- Chukua kwa usahihi vituo vyako vipya.


Kwa mfano, kama unajua kwamba utapokea baada ya wiki moja tuseme 1M Sats, fungua chaneli ya 2M Sats na ubadilishe kuwa onchain Wallet au kwenye akaunti nyingine (ya muda) ya LN ya 50-60% ya ukwasi wako wa nje. Daima uwe tayari na ukwasi zaidi. Mara tu unapohitaji ukwasi zaidi katika chaneli zako za Zeus, unaweza kuirejesha kutoka kwa akaunti za uhifadhi.


Ikiwa unajua kwamba utatuma tuseme 500k Sats/wiki, kisha ufungue chaneli ya 1M Sats. Kwa njia hii bado utakuwa na akiba hadi uijaze tena.



- Ikiwa wewe ni mfanyabiashara na utapokea kila mara zaidi ya unavyotumia mara kwa mara, nunua chaneli maalum ya ndani. Njia ya bei nafuu zaidi. Unalipa ada kidogo na utapata chaneli "tupu".



- Usifungue njia ndogo zisizo na maana za 50-100-300-500k Sats. Utazijaza baada ya siku chache, hata kama utazitumia kwa zaps pekee. Fungua kubwa zaidi na tofauti, SIO chaneli moja tu.


Mara tu unapofungua chaneli kubwa zaidi, unaweza kutumia ubadilishaji wa nyambizi za nje kila wakati kusogeza Sats kwenye pochi zako za onchain (ikiwa ni pamoja na kurudi kwenye Zeus onchain). Kuweka usawa kati ya ukwasi wa ndani na nje ni vizuri na pia unaweza "kutumia tena" hizo Sats kufungua chaneli zaidi ukipenda.


### Imefungwa Invoice


Ikiwa ungependa kuongeza faragha zaidi unapopokea, unaweza kutumia mbinu ya "Invoice iliyofungwa". Kikumbusho: ili uweze kufanya hivyo, unahitaji chaneli iliyo na Olympus LSP. Ankara zilizofungwa "zitaficha" mahali pa mwisho (nodi yako ya Zeus) na kuonyesha nodi yako ya LSP kama marudio ya mlipaji.


Ili kupata Invoice iliyofunikwa, nenda kwenye skrini kuu ya vitufe, weka kiasi na ugonge ombi. Itaonyesha msimbo wa kawaida wa QR kwa Invoice yako. Sasa, bofya kitufe cha "X" cha juu kulia na utaelekezwa kwenye chaguo zaidi za Invoice.


![Image](assets/en/14.webp)


Sasa itabidi uwashe chaguo hilo juu "Wezesha LSP" na ubofye kitufe cha "Unda Invoice". Chaguo hilo litaunda Invoice iliyofungwa na kumbuka, itatoza ada ndogo.


### Ankara zilizo na vidokezo vya njia


Hiki ni kipengele muhimu sana ikiwa unataka kudhibiti ukwasi wa njia nyingi zinazoingia. Kwa kweli unaweza kuonyesha ni chaneli gani inayoingia unataka kupokea Sats kutoka kwa Invoice.


Kipengele hiki kinaweza kutumika pia kwa kusawazisha upya kwa mduara, unapotaka kuhamisha ukwasi kutoka kwa chaneli moja iliyojazwa hadi nyingine iliyoisha.


Jinsi ya kuunda Invoice na vidokezo vya njia?



- Kwenye skrini kuu, telezesha kulia droo ya LN na ubofye "Pokea"
- Katika usanidi wa Invoice ilifika sehemu ya chini na kuamsha kitufe cha "Ingiza vidokezo vya njia", kisha uchague kichupo cha "Custom". Itafungua skrini iliyo na chaneli zako zote zinazopatikana. Chagua moja unayotaka kupokea.
- Jaza maelezo mengine yote ya Invoice, kiasi, memo n.k na ubofye "unda Invoice".
- Kulipa hiyo Invoice kutaleta Sats kwenye chaneli iliyoonyeshwa.


Iwapo ungependa kujilipia hiyo Invoice (kusawazisha upya kwa mduara), unapoilipa kutoka kwa nodi yako hiyo hiyo ya Zeus, kwenye skrini ya malipo, chagua chaneli inayotoka (iliyo na ukwasi zaidi) unayotaka itumike kama malipo.


### Lipa kwa kutumia Keysend


Keysend ni kipengele cha chini sana cha LN na watumiaji wanapaswa kukitumia mara nyingi zaidi.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) huruhusu watumiaji katika Lightning Network kutuma malipo kwa wengine , moja kwa moja kwa ufunguo wao wa umma, mradi tu nodi zao zina chaneli za umma na utumaji wa vitufe umewashwa. Keysend haihitaji mpokeaji kutoa Invoice.


Kwa hivyo unawezaje kufanya hivyo na Zeus?


Changanua kwa urahisi au nakili kitambulisho lengwa (au tumia anwani za Zeus ili kuhifadhi nodi zako za kawaida za lengwa kama waasiliani) na kisha kutoka kwenye skrini kuu ya Zeus, bofya kitufe cha "Tuma". Katika skrini hiyo basi ubandike nodiID au uchague kutoka kwa anwani zako.


Weka kiasi cha Sats, ujumbe ikiwa ni lazima (ndio, unaweza kuutumia pia kama gumzo la siri kwenye LN) na ubofye kitufe cha "Tuma". Imekamilika!


![Image](assets/en/15.webp)


Ikiwa una kituo cha moja kwa moja na mwenzi lengwa, HAKUNA ada zinazohusika.


Iwapo huna chaneli ya moja kwa moja na mwenzi mwingine lengwa, basi malipo ya ufunguo yatalipa ada kama malipo ya kawaida ya LN Invoice, yanayoelekezwa kwenye njia ya udhibiti kama malipo mengine yoyote. Hiyo tu, kumbuka, haitabaki kuwa athari yoyote kama LN Invoice.


## Hitimisho


Ninapendekeza usome mwongozo wa ufuatiliaji [Matumizi ya hali ya juu ya Zeus](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) ukiwa na maagizo zaidi na kesi za utumiaji.


Na ... ndivyo hivyo! Kuanzia sasa unatumia Zeus Node kama BTC/LN Wallet ya kawaida kwenye simu yako. Kiolesura ni cha moja kwa moja na ni rahisi kutumia, ni angavu kwa aina yoyote ya mtumiaji, sidhani kama ni lazima niandike maelezo zaidi kuhusu jinsi ya kufanya na kupokea malipo.


Kwa kumalizia, hapa kuna chati ya kulinganisha ya faragha:


![Image](assets/en/16.webp)