---
name: Blockstream Green - 2FA
description: Kuweka 2/2 Multisig kwenye Green Wallet
---
![cover](assets/cover.webp)

___

***Kumbuka:** Kuanzia Mei 2025, haitakuwa tena inawezekana kuanzisha akaunti mpya zilizo na ulinzi wa two-factor authentication (2FA). Kipengele hiki kinapatikana tu kwa watumiaji waliokuwa tayari wamewasha aina hii ya akaunti awali.*

___

Software Wallet ni programu iliyosakinishwa kwenye kompyuta, simu mahiri au kifaa kingine kilichounganishwa kwenye mtandao, kukuwezesha kudhibiti na kulinda funguo zako za Bitcoin Wallet. Tofauti na hardware wallets, ambazo hutenga funguo za kibinafsi, Hot wallet  kwa hivyo hufanya kazi katika mazingira ambayo yanaweza kukabiliwa na mashambulizi ya mtandao, na hivyo kuongeza hatari ya uharamia na wizi.

Software wallets zinapaswa kutumiwa kudhibiti viwango vya kuridhisha vya bitcoin, haswa kwa miamala ya kila siku. Wanaweza pia kuwa chaguo la kuvutia kwa watu walio na mali chache za Bitcoin, ambao uwekezaji wao katika Hardware Wallet unaweza kuonekana usio na uwiano. Hata hivyo, utumiaji wao wa mara kwa mara kwenye mtandao huwafanya wasiwe na usalama mdogo wa kuhifadhi akiba yako ya muda mrefu au pesa nyingi. Kwa hili la mwisho, ni bora kuchagua suluhu zilizo salama zaidi, kama vile hardware wallets.

Katika somo hili, nitakuonyesha jinsi ya kuboresha usalama wa Hot Wallet kwa kutumia chaguo la "*2FA*" kwenye Blockstream Green.


![GREEN 2FA MULTISIG](assets/fr/01.webp)


## Tunawaletea Blockstream Green


Blockstream Green ni Software Wallet inayopatikana kwenye simu na eneo-kazi. Hapo awali ilijulikana kama *Green Address*, Wallet hii ikawa mradi wa Blockstream kufuatia kupatikana kwake mwaka wa 2016.


Green ni programu ambayo ni rahisi kutumia, ambayo inafanya kuvutia kwa wanaoanza. Inatoa vipengele vyote muhimu vya Bitcoin Wallet nzuri, ikijumuisha RBF (*Replace-by-fee*), chaguo la muunganisho wa Tor, uwezo wa kuunganisha node yako mwenyewe, SPV (*Simplified Payment Verification*), kuweka alama kwenye sarafu na kudhibiti.


Blockstream Green pia inasaidia Liquid Network, Bitcoin Sidechain iliyotengenezwa na Blockstream kwa haraka, Confidential Transactions nje ya Blockchain kuu. Katika somo hili, tunaangazia Bitcoin pekee, lakini pia nimefanya mafunzo mengine ya kujifunza jinsi ya kutumia Liquid kwenye Green :


https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## Chaguo 2/2 Multisig (2FA)


Kwenye Green, unaweza kuunda "*singlesig*" ya kawaida ya Hot Wallet. Lakini pia una chaguo la "*2FA Multisig*", ambayo huongeza usalama wa Hot Wallet yako bila kutatiza usimamizi wake wa kila siku.


Kwa hivyo utaweka 2/2 Multisig Wallet, ambayo ina maana kwamba kila miamala itahitaji saini ya funguo mbili. Ufunguo wa kwanza, unaotokana na maneno yako ya Mnemonic yenye 12- au 24, umelindwa ndani kwa kutumia msimbo wa PIN kwenye simu yako. Una udhibiti kamili juu ya ufunguo huu. Ufunguo wa pili unashikiliwa na server za Blockstream na utumiaji wake kutia sahihi unahitaji uthibitishaji, ambao unaweza kupatikana kupitia nambari ya kuthibitisha iliyopokelewa kwa barua pepe, SMS, simu, au, kama tutakavyoona katika mafunzo haya, kupitia programu ya uthibitishaji (Authy, Google Authenticator, n.k.).


Ili kuhakikisha uhuru wako katika tukio la Blockstream kushindwa (kwa mfano, katika tukio la kufilisika kwa kampuni au uharibifu wa server zilizoshikilia ufunguo wa pili), utaratibu wa kufunga saa unatumiwa kwenye Multisig yako. Utaratibu huu hubadilisha 2/2 Multisig kuwa 1/2 Multisig baada ya mwaka mmoja (au kwa usahihi Blocks 51,840, lakini thamani hii inaweza kubadilishwa), baada ya hapo Wallet yako itahitaji tu ufunguo wako wa ndani ili kutumia bitcoin. Kwa hivyo, ikiwa utapoteza ufikiaji wa server za Blockstream au uthibitishaji wa 2FA, itabidi usubiri tu kwa muda usiozidi mwaka mmoja ili kuweza kutumia bitcoin zako kwa uhuru na programu yako, bila kutegemea Blockstream.


![GREEN 2FA MULTISIG](assets/fr/02.webp)


Njia hii huongeza kwa kiasi kikubwa usalama wa Hot Wallet yako, huku ikiendelea kukuacha na udhibiti wa bitcoin zako na kuwezesha matumizi ya kila siku. Hata hivyo, inahitaji kusasishwa upya kwa saa ili kudumisha usalama wa 2FA. Muda uliosalia wa siku 360, ambao pesa zako zinalindwa na 2FA, huanza mara tu unapopokea bitcoin. Ikiwa, baada ya siku 360 tangu kupokea, hutafanya muamala wowote ukitumia pesa hizi, bitcoin zako zitalindwa tu na ufunguo wako wa ndani, bila 2FA.


Kizuizi hiki hufanya chaguo la 2FA kufaa zaidi kwa matumizi ya Wallet, ambapo miamala ya kawaida husasisha kiotomatiki kufuli za saa. Kwa uokoaji wa muda mrefu wa Wallet, hii inaweza kuwa shida, kwani utahitaji kufikiria juu ya kufanya miamala ya kufagia kila mwaka kabla ya muda kuisha.


Ubaya mwingine wa njia hii ya usalama ni kwamba utalazimika kutumia violezo vya hati vinavyotumiwa na watu wachache. Hii ina maana kwamba, kwa mtazamo wa faragha, mambo yanakuwa magumu zaidi: ni watu wachache sana wanaotumia aina sawa ya hati kama wewe, hivyo kumrahisishia mwangalizi wa nje kutambua alama ya kidole ya wallet yako. Zaidi ya hayo, hati hizi zitahitaji ada za muamala za juu kutokana na ukubwa wake mkubwa.


Iwapo unapendelea kutotumia chaguo la 2FA na ungependa tu kusanidi "*singlesig*" Wallet kwenye Green, ninakualika kushauriana na mafunzo haya mengine :


https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

## Inasakinisha na kusanidi programu ya Blockstream Green


Hatua ya kwanza ni kupakua programu ya Green. Nenda kwenye duka lako la maombi:



- [Kwa Android](https://play.google.com/store/apps/details?id=com.greenaddress.greenbits_android_wallet);
- [Kwa Apple](https://apps.apple.com/us/app/Green-Bitcoin-Wallet/id1402243590).

![GREEN 2FA MULTISIG](assets/fr/03.webp)


Kwa watumiaji wa Android, unaweza pia kusakinisha programu kupitia faili ya `.apk` [inapatikana kwenye GitHub ya Blockstream](https://github.com/Blockstream/green_android/releases).


![GREEN 2FA MULTISIG](assets/fr/04.webp)


Fungua programu, kisha uteue kisanduku cha "Ninakubali masharti...".


![GREEN 2FA MULTISIG](assets/fr/05.webp)


Unapofungua Green kwa mara ya kwanza, skrini ya nyumbani inaonekana bila Wallet iliyosanidiwa. Baadaye, ikiwa utaunda au kuagiza pochi, zitaonekana kwenye Interface hii. Kabla ya kuendelea kuunda Wallet, nakushauri urekebishe mipangilio ya programu kulingana na mahitaji yako. Bonyeza "Mipangilio ya Maombi".


![GREEN 2FA MULTISIG](assets/fr/06.webp)


Chaguo la "*Faragha Iliyoimarishwa*", inayopatikana kwenye Android pekee, huboresha faragha kwa kuzima picha za skrini na kuficha uhakiki wa programu. Pia hufunga ufikiaji wa programu kiotomatiki mara tu simu yako inapofungwa, na kufanya data yako kuwa ngumu zaidi kufichua.


![GREEN 2FA MULTISIG](assets/fr/07.webp)


Kwa wale wanaotaka kuboresha ufaragha wao, programu hutoa chaguo la kusimamisha trafiki yako kupitia Tor, mtandao ambao husimba miunganisho yako yote na kufanya miamala yako kuwa ngumu kufuatilia. Ingawa chaguo hili linaweza kupunguza kasi ya utendakazi wa programu, inapendekezwa sana kulinda faragha yako, haswa ikiwa hutumii full node yako.


![GREEN 2FA MULTISIG](assets/fr/08.webp)


Kwa watumiaji ambao wana full node, Green Wallet inatoa uwezekano wa kuunganishwa nayo kupitia server ya Electrum, kuhakikisha udhibiti kamili wa habari za mtandao wa Bitcoin na usambazaji wa muamala.


![GREEN 2FA MULTISIG](assets/fr/09.webp)


Kipengele kingine mbadala ni chaguo la "*Uthibitishaji wa SPV*", ambayo hukuruhusu kuthibitisha data fulani ya Blockchain moja kwa moja na hivyo kupunguza hitaji la kuamini node chaguo-msingi ya Blockstream, ingawa njia hii haitoi dhamana zote za Full node.


![GREEN 2FA MULTISIG](assets/fr/10.webp)


Mara tu ukirekebisha mipangilio hii kwa mahitaji yako, bofya kitufe cha "*Hifadhi*" na uanze upya programu.


![GREEN 2FA MULTISIG](assets/fr/11.webp)


## Unda Bitcoin Wallet kwenye Blockstream Green


Sasa uko tayari kuunda Bitcoin Wallet. Bonyeza kitufe cha "*Anza*".


![GREEN 2FA MULTISIG](assets/fr/12.webp)


Unaweza kuchagua kati ya kuunda Software Wallet ya ndani au kudhibiti Cold Wallet kupitia Hardware Wallet. Kwa mafunzo haya, tutazingatia kuunda Hot Wallet, kwa hivyo utahitaji kuchagua chaguo la "*Kwenye Kifaa Hiki*".


![GREEN 2FA MULTISIG](assets/fr/13.webp)


Kisha unaweza kuchagua kurejesha Wallet ya Bitcoin iliyopo au kuunda mpya. Kwa madhumuni ya somo hili, tutaunda Wallet mpya. Hata hivyo, ikiwa unahitaji kuunda upya Wallet ya Bitcoin iliyopo kutoka kwenye maneno yake ya mnemonic, kwa mfano baada ya kupoteza simu yako ya zamani, utahitaji kuchagua chaguo la pili.


![GREEN 2FA MULTISIG](assets/fr/14.webp)


Kisha unaweza kuchagua kati ya maneno 12 au maneno 24 ya Mnemonic. Kifungu hiki cha maneno kitakuwezesha kurejesha ufikiaji wa Wallet yako kutoka kwa programu yoyote inayooana ikiwa kuna tatizo kwenye simu yako. Kwa sasa, kuchagua kifungu cha maneno 24 hakutoi usalama zaidi ya kifungu cha maneno 12. Kwa hivyo ninapendekeza kwamba uchague maneno 12 ya Mnemonic.


Green itakupa kishazi chako cha Mnemonic. Kabla ya kuendelea, hakikisha hutazamwa. Bofya kwenye "*Onyesha kifungu cha maneno cha uokoaji*" ili kukionyesha kwenye skrini.


![GREEN 2FA MULTISIG](assets/fr/15.webp)


**Mnemonic hii inakupa ufikiaji kamili, usio na kikomo kwa bitcoin zako zote**. Mtu yeyote aliye na kifungu hiki cha maneno anaweza kuiba pesa zako, hata bila ufikiaji wa kimwili wa simu yako (kulingana na muda ulioisha au 2FA ikiwa ni 2/2 Wallet kwenye Green).


Inakuruhusu kurejesha ufikiaji wa funguo zako za ndani ikiwa simu yako itapotea, kuibiwa au kuharibika. Kwa hivyo ni muhimu sana kuihifadhi kwa uangalifu **kwenye nyenzo halisi (si ya dijitali)** na kuihifadhi mahali salama. Unaweza kuiandika kwenye kipande cha karatasi, au kwa usalama ulioongezwa, ikiwa ni Wallet kubwa, ninapendekeza kuandika kwenye usaidizi wa chuma cha pua ili kuilinda kutokana na hatari ya moto, mafuriko au kuanguka (kwa Hot Wallet iliyopangwa ili kupata kiasi kidogo cha bitcoin, nakala rahisi ya karatasi ni pengine ya kutosha).


*Ni wazi, hupaswi kamwe kushiriki maneno haya kwenye Mtandao, kama ninavyofanya katika mafunzo haya. Sampuli hii ya Wallet itatumika kwenye Testnet pekee na itafutwa mwishoni mwa mafunzo.*


![GREEN 2FA MULTISIG](assets/fr/16.webp)


Mara baada ya kurekodi maneno yako ya mnemonic kwa usahihi kwenye nyenzo halisi, bofya '*Endelea*'. Green Wallet itakuomba uthibitishe baadhi ya maneno katika seti yako ya mnemonic ili kuhakikisha kuwa umeandika kwa usahihi. Jaza nafasi zilizoachwa wazi kwa maneno yanayokosekana.


![GREEN 2FA MULTISIG](assets/fr/17.webp)


Chagua PIN ya kifaa chako, ambayo itatumika kufungua Green Wallet yako. Huu ni ulinzi wako dhidi ya ufikiaji wa kimwili ambao haujaidhinishwa. Msimbo huu wa PIN hauhusiki katika upataji wa funguo za cryptography za Wallet yako. Kwa hivyo, hata bila ufikiaji wa msimbo huu wa PIN, kumiliki vifungu vyako vya maneno 12 au 24 vya Mnemonic kutakuwezesha kupata tena ufikiaji wa funguo za eneo lako.


Tunapendekeza uchague PIN ya tarakimu 6 ambayo ni nasibu iwezekanavyo. Hakikisha umehifadhi msimbo huu ili usiusahau; vinginevyo utalazimika kurejesha wallet yako kutoka kwa mnemonic. Baadaye unaweza kuongeza chaguo la kufungua kwa njia ya kibayometriki ili kuepuka kuingiza PIN kila wakati unapoitumia. Hata hivyo, bayometriki si salama zaidi kuliko PIN yenyewe, hivyo kwa chaguo-msingi nakushauri kutowasha kipengele hiki.


![GREEN 2FA MULTISIG](assets/fr/18.webp)


Weka PIN yako mara ya pili ili kuithibitisha.


![GREEN 2FA MULTISIG](assets/fr/19.webp)


Subiri Wallet yako iundwe, kisha ubofye kitufe cha "*Fungua akaunti*".


![GREEN 2FA MULTISIG](assets/fr/20.webp)


Kisha unaweza kuchagua kati ya Wallet ya kawaida ya sahihi moja au Wallet inayolindwa na Two-Factor Authentication (2FA). Katika somo hili, tutachagua chaguo la pili.


![GREEN 2FA MULTISIG](assets/fr/21.webp)


Bitcoin Multisig Wallet yako sasa imeundwa kwa kutumia programu ya Green!


![GREEN 2FA MULTISIG](assets/fr/22.webp)


## Kuanzisha 2FA


Bofya kwenye akaunti yako.


![GREEN 2FA MULTISIG](assets/fr/23.webp)


Bofya kwenye kitufe cha Green "*Ongeza usalama wa akaunti yako kwa kuongeza 2FA*".


![GREEN 2FA MULTISIG](assets/fr/24.webp)


Kisha utaweza kuchagua mbinu ya uthibitishaji ili kufikia ufunguo wa pili wa multisig yako ya 2/2. Kwa mafunzo haya, tutatumia programu ya uthibitishaji. Ikiwa hujui kuhusu aina hii ya programu, ninapendekeza uangalie mafunzo yetu kuhusu Authy:


https://planb.academy/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Chagua "*Authenticator app*".


![GREEN 2FA MULTISIG](assets/fr/25.webp)


Green itaonyesha msimbo wa QR pamoja na ufunguo wa kurejesha akaunti. Ufunguo huu hukuruhusu kurejesha ufikiaji wa 2FA yako endapo programu yako ya Authy itapotea. Inashauriwa kuhifadhi nakala salama ya ufunguo huu, ingawa bado unaweza kurejesha ufikiaji wa bitcoin zako baada ya muda wa kufunga kuisha, kama ilivyoelezwa hapo juu.


Katika programu yako ya uthibitishaji, ongeza msimbo mpya, kisha uchanganue msimbo wa QR uliotolewa na Green.


![GREEN 2FA MULTISIG](assets/fr/26.webp)


*Ni wazi, hupaswi kamwe kushiriki ufunguo huu na msimbo wa QR kwenye Mtandao, kama ninavyofanya katika mafunzo haya. Sampuli hii ya Wallet itatumika kwenye Testnet pekee na itafutwa mwishoni mwa mafunzo.*


Bonyeza kitufe cha "*Endelea*".


![GREEN 2FA MULTISIG](assets/fr/27.webp)


Weka nambari ya kuthibitisha yenye tarakimu 6 iliyopo kwenye programu yako ya uthibitishaji.


![GREEN 2FA MULTISIG](assets/fr/28.webp)


Uthibitishaji wa 2-factor sasa umewashwa.


![GREEN 2FA MULTISIG](assets/fr/29.webp)


Kwa kuvinjari menyu hii, unaweza pia kuweka muda wa kufunga saa. Muda uliosalia huanza mara tu bitcoin zinapopokelewa, na baada ya muda wa kufunga kuisha, pesa zako zinaweza kutumika tu na ufunguo wako wa ndani, bila kuhitaji 2FA. Muda chaguo-msingi umewekwa kuwa miezi 12, lakini kwa wallet ya akiba, inaweza kuwa na maana kuchagua miezi 15 ili kupunguza marudio ya kusasisha muda. Kinyume chake, kwa matumizi ya wallet, muda wa miezi 6 unaweza kuwa bora zaidi, kwani utasasishwa mara kwa mara na miamala yako ya kila siku, na muda mfupi hupunguza kusubiri katika tukio la tatizo na 2FA. Ni juu yako kuamua muda wa kufunga saa unaokufaa zaidi.


![GREEN 2FA MULTISIG](assets/fr/30.webp)


Sasa unaweza kuondoka kwenye menyu hii. Multisig Wallet yako iko tayari!


![GREEN 2FA MULTISIG](assets/fr/31.webp)


## Kuweka Wallet yako kwenye Blockstream Green


Ikiwa ungependa kubinafsisha wallet yako, bofya kwenye vitone vitatu vidogo vilivyo kwenye kona ya juu kulia.


![GREEN 2FA MULTISIG](assets/fr/32.webp)


Chaguo la "*Badilisha jina*" hukuwezesha kubinafsisha jina la Wallet yako, ambayo ni muhimu sana ikiwa unadhibiti pochi kadhaa kwenye programu tumizi sawa.


![GREEN 2FA MULTISIG](assets/fr/33.webp)


Menyu ya "*Kitengo*" hukuruhusu kubadilisha kitengo cha msingi cha Wallet yako. Kwa mfano, unaweza kuchagua kuionyesha katika satoshis badala ya bitcoin.


![GREEN 2FA MULTISIG](assets/fr/34.webp)


Menyu ya "*Mipangilio*" hutoa ufikiaji wa chaguo mbalimbali za Bitcoin Wallet yako.


![GREEN 2FA MULTISIG](assets/fr/35.webp)


Hapa, kwa mfano, utapata ufunguo wako uliopanuliwa wa umma na *kielezi* chake, muhimu ikiwa unapanga kusanidi Wallet katika hali ya saa pekee kutoka kwenye Wallet hii.


![GREEN 2FA MULTISIG](assets/fr/36.webp)


Unaweza pia kubadilisha PIN yako ya Wallet na kuamilisha muunganisho wa kibayometriki.


![GREEN 2FA MULTISIG](assets/fr/37.webp)


## Kwa kutumia Blockstream Green


Sasa kwa kuwa Bitcoin Wallet yako imesanidiwa, uko tayari kupokea Sats yako ya kwanza! Bonyeza tu kwenye kitufe cha "* Pokea*".


![GREEN 2FA MULTISIG](assets/fr/38.webp)


Kisha Green itaonyesha nafasi ya kwanza inayopokea Address katika Wallet yako. Unaweza kuchanganua msimbo husika wa QR, au kunakili Address moja kwa moja ili kutuma bitcoin. Aina hii ya Address haielezei kiasi cha kutumwa na mlipaji. Unaweza, hata hivyo, generate Address inayoomba kiasi mahususi, kwa kubofya nukta tatu ndogo kwenye kona ya juu kulia, kisha kwenye "*Omba kiasi*", na kuingiza kiasi unachotaka.


![GREEN 2FA MULTISIG](assets/fr/39.webp)


Wakati muamala unatangazwa kwenye mtandao, utaonekana kwenye Wallet yako.


![GREEN 2FA MULTISIG](assets/fr/40.webp)


Subiri hadi upate uthibitisho wa kutosha ili kuzingatia muamala kuwa suluhu.


![GREEN 2FA MULTISIG](assets/fr/41.webp)


Ukiwa na bitcoin kwenye Wallet yako, sasa unaweza pia kutuma bitcoin. Bonyeza "*Tuma*".


![GREEN 2FA MULTISIG](assets/fr/42.webp)


Kwenye ukurasa unaofuata, ingiza Address ya mpokeaji. Unaweza kuiingiza wewe mwenyewe au kuchanganua msimbo wa QR.


![GREEN 2FA MULTISIG](assets/fr/43.webp)


Chagua kiasi cha malipo.


![GREEN 2FA MULTISIG](assets/fr/44.webp)


Katika sehemu ya chini ya skrini, unaweza kuchagua kiwango cha ada ya muamala huu. Una chaguo la kufuata mapendekezo ya programu au kubinafsisha ada zako. Kadiri ada inavyoongezeka ikilinganishwa na miamala mingine inayosubiri, ndivyo muamala wako utakavyochakatwa kwa haraka zaidi. Kwa maelezo zaidi kuhusu soko la ada, tafadhali tembelea [Mempool.space](https://Mempool.space/) katika sehemu ya "*Ada za Muamala*".


![GREEN 2FA MULTISIG](assets/fr/45.webp)


Bofya kwenye "*Inayofuata*" ili kufikia skrini ya muhtasari wa muamala. Hakikisha kuwa Address, kiasi na gharama ni sahihi.


![GREEN 2FA MULTISIG](assets/fr/46.webp)


Ikiwa kila kitu kitaenda vizuri, telezesha kitufe cha Green chini ya skrini kulia ili kusaini na kutangaza miamala kwenye mtandao wa Bitcoin.


![GREEN 2FA MULTISIG](assets/fr/47.webp)


Huu ndio wakati unahitaji kuweka msimbo wako wa uthibitishaji ili kufungua ufunguo wa pili wa Multisig unaoshikiliwa na Blockstream. Weka msimbo wa tarakimu 6 unaoonyeshwa kwenye programu yako ya uthibitishaji.


![GREEN 2FA MULTISIG](assets/fr/48.webp)


Muamala wako sasa utaonekana kwenye dashibodi yako ya Bitcoin Wallet, ukingoja uthibitisho.


![GREEN 2FA MULTISIG](assets/fr/49.webp)


Kwa hivyo sasa unajua jinsi ya kusanidi kwa urahisi 2/2 Multisig Wallet kwa kutumia chaguo la Blockstream Green la 2FA!


Ikiwa umepata mafunzo haya kuwa ya manufaa, ningeshukuru ikiwa utaacha kidole gumba cha Green hapa chini. Jisikie huru kushiriki nakala hii kwenye mitandao yako ya kijamii. Asante sana!


Pia ninapendekeza uangalie mafunzo haya mengine ya kina juu ya programu ya simu ya Blockstream Green ili kusanidi Liquid Wallet :


https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a
