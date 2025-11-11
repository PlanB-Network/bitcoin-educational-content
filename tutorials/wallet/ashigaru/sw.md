---
name: Ashigaru
description: fork kutoka Samourai Wallet ili kulinda, kudhibiti na kuchanganya bitcoins zako
---

![cover](assets/cover.webp)



Ashigaru ni programu ya Bitcoin ya simu ya wallet ambayo inafuata kutoka kwa mradi wa Samourai Wallet, lakini kwa njia mpya. Programu hii ilizaliwa katika muktadha fulani: mnamo Aprili 2024, waanzilishi wa Samourai Wallet walikamatwa na mamlaka ya Amerika, na seva zao zilikamatwa. Ingawa programu ya Samurai yenyewe ilibaki kutumika, kwa sasa haijatunzwa tena. Ashigaru ni toleo lisilolipishwa la fork la Samurai Wallet, linalodumishwa na timu isiyojulikana ili kuhakikisha utendakazi wa Samurai uendelevu na kulinda falsafa yake asili: kutetea faragha na uhuru wa watumiaji wa Bitcoin.



Ashigaru huchukua sehemu kubwa ya DNA ya Samourai: kiolesura sawa, mbinu ya kujilinda, chanzo huria na kuzingatia faragha. Nambari ya kuthibitisha inasambazwa chini ya leseni ya GNU GPLv3, ambayo inahakikisha kwamba mtu yeyote anaweza kukagua, kurekebisha au kusambaza upya programu.



Programu ya Ashigaru inaunganisha seti ya zana mahiri za usiri na usimamizi wa UTXO zako:




- Whirlpool**, itifaki ya sanjari kulingana na Zerolink, inayokuwezesha kuvunja viungo vya kubainisha kati ya maingizo ya muamala na kuondoka, bila kupoteza mamlaka juu ya pesa zako.
- PayNym**, ambayo hutumia misimbo ya malipo inayoweza kutumika tena (BIP47), ambayo sasa inawakilishwa kupitia mfumo wa avatar wa "*Pepehash*".
- Ricochet**, kipengele kinachoongeza miruko ya kati kwa shughuli ili kuzifanya kuwa ngumu zaidi kuzifuatilia.
- Na bila shaka ***Coin Control*** ili kuchagua, kugandisha na kuweka lebo kwenye UTXO zako kwa usahihi.
- Matumizi ya Kundi***, ili kupunguza gharama kwa kupanga malipo kadhaa katika shughuli moja.
- **Njia ya Siri**, ambayo huficha programu kwenye simu yako nyuma ya kizindua dummy ili isionekane wakati wa ukaguzi wa kimwili wa simu yako.
- Zana za matumizi ya hali ya juu ili kuboresha usiri wako (payjoin, stonewall...).
- Mfumo wa urejeshaji ulioboreshwa kwa kutumia Nenosiri BIP39.
- Mfumo wa kuboresha kiotomatiki chaguo la ada za muamala.



![Image](assets/fr/01.webp)



Kwa hivyo, Ashigaru inalenga watumiaji wanaofahamu masuala yanayohusu ufuatiliaji wa miamala kwenye Bitcoin. Iwe wewe ni mtumiaji anayejali faragha, mtaalam wa bitcoin aliyejitolea kujilinda, au mtu aliye katika hatari ya kuongezeka kwa ufuatiliaji, programu hii ya wallet hukupa zana unazohitaji ili kurejesha udhibiti wa shughuli zako kwenye Bitcoin.



Ashigaru inapatikana katika toleo la simu kupitia programu yake, ambayo tutaichunguza katika somo hili. Lakini pia inaweza kutumika kwenye Kompyuta na ***Ashigaru Terminal***, ambayo tutaanzisha katika mafunzo yajayo.



![Image](assets/fr/02.webp)



Katika somo hili, ningependa kukujulisha matumizi ya kimsingi ya Ashigaru: usakinishaji, unganisho kwenye Dojo, chelezo, kupokea na kutuma bitcoins. Zana za kina zitawasilishwa katika mafunzo mengine maalum.



## 1. Mahitaji ya Ashigaru



Programu inahitaji masharti machache ili kufanya kazi vizuri. Kwanza kabisa, si programu inayopatikana kwenye maduka ya kawaida kama vile Google Play Store au App Store. Inasakinisha mwenyewe kwenye simu yako kutoka kwa faili yake ya `.apk`, inayoweza kupakuliwa kupitia mtandao wa Tor. Kwa hiyo ikiwa unatumia iPhone, njia hii haitafanya kazi: utahitaji kifaa cha Android.



Ili kupakua faili ya `.apk` kupitia Tor, utahitaji kivinjari chenye uwezo wa kufikia tovuti za `.onion`. Njia rahisi ni kusakinisha programu ya Kivinjari cha Tor kwenye simu yako, inayopatikana kutoka [Duka la Google Play](https://play.google.com/store/apps/details?id=org.torproject.torbrowser) au moja kwa moja [kupitia `.apk`](https://www.torproject.org/download/#android) yake.



![Image](assets/fr/03.webp)



Simu mahiri za hivi karibuni huzuia usakinishaji wa programu kutoka kwa vyanzo visivyojulikana kwa chaguomsingi. Utahitaji kuwezesha chaguo hili kwa Kivinjari cha Tor kwa muda katika mipangilio ya kifaa chako ili kuruhusu usakinishaji. Baada ya programu kusakinishwa, kumbuka kuzima kipengele hiki ili kuimarisha usalama wa simu yako.



Sharti lingine muhimu la kutumia Ashigaru ni nodi ya Bitcoin Dojo. Kwa sababu za usalama na uhuru, timu ya Ashigaru haitunzi seva iliyo katikati ili kuunganisha programu yako. Kwa hivyo utahitaji kuendesha mfano wako wa Dojo, au uunganishe kwa unaoaminika.



Dojo huwezesha programu yako ya Ashigaru kushauriana na maelezo ya blockchain, kuona salio la anwani yako na kutangaza miamala yako kwenye mtandao wa Bitcoin.



Ili kujua zaidi kuhusu Dojo na kujifunza jinsi ya kuisakinisha, ninakualika ufuate mafunzo haya mahususi:



https://planb.network/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Iwapo huwezi kumudu kuendesha Dojo yako mwenyewe, unaweza kupata watu walio tayari kushiriki mfano wao bila malipo kwenye [dojobay.pw](https://www.dojobay.pw/mainnet/). Hili linaweza kuwa suluhu la muda, lakini baada ya muda mrefu, ninapendekeza utumie Dojo yako ili kuhakikisha uhuru na usiri wako.



## 2. Angalia na usakinishe programu ya Ashigaru



### 2.1. Pakua programu ya Ashigaru



Kwenye simu yako, fungua Kivinjari cha Tor na uende kwenye [tovuti rasmi ya Ashigaru](https://ashigaru.rs/download/), katika sehemu ya `Pakua`. Kisha bofya kitufe cha `Pakua kwa Android` ili kupakua faili ya usakinishaji.



![Image](assets/fr/04.webp)



Kabla ya kusakinisha programu kwenye kifaa chako, tutaangalia uhalisi na uadilifu wake. Hii ni hatua muhimu sana, hasa wakati wa kusakinisha programu moja kwa moja kutoka kwa faili ya `.apk'.



### 2.2. Angalia maombi ya Ashigaru



Rudi kwenye [tovuti rasmi ya Ashigaru](https://ashigaru.rs/download/) katika sehemu ya `Pakua`, kisha unakili ujumbe unaoonyeshwa chini ya kichwa `SHA-256 Hash cha faili ya APK`. Nakili kizuizi kizima, kutoka kwa `ANZA UJUMBE ULIO SAINI WA PGP` hadi `MALIZA SAINI YA PGP`.



![Image](assets/fr/05.webp)



Bado kwenye simu yako, fungua kichupo kipya kwenye Kivinjari cha Tor na uende kwenye [zana ya uthibitishaji wa Keybase](https://keybase.io/verify). Bandika ujumbe ambao umenakili hivi punde kwenye sehemu iliyotolewa, kisha ubofye kitufe cha `Thibitisha`.



![Image](assets/fr/06.webp)



Ikiwa saini ni halisi, Keybase itaonyesha ujumbe unaothibitisha kuwa faili imetiwa saini na wasanidi wa Ashigaru. Unaweza pia kubofya wasifu wa `ashigarudev` ulioonyeshwa na Keybase na uangalie kuwa alama zao za vidole muhimu zinalingana kabisa na : `A138 06B1 FA2A 676B`.



Hata hivyo, ikiwa hitilafu inaonekana katika hatua hii, inamaanisha kuwa sahihi ni batili. Katika hali hii, **usisakinishe APK**. Anza tena tangu mwanzo, au iombe jumuiya usaidizi kabla ya kuendelea.



![Image](assets/fr/07.webp)



Keybase imekupa heshi ya programu. Sasa tutaangalia kwamba heshi ya faili ya `.apk` uliyopakua inalingana na ile iliyothibitishwa kwenye Keybase. Ili kufanya hivyo, nenda kwenye [HASH FILE ONLINE](https://hash-file.online/).



![Image](assets/fr/08.webp)



Bofya kwenye kitufe cha `BROWSE...` na uchague faili ya `.apk` iliyopakuliwa katika hatua ya 2.1.


Kisha chagua kitendakazi cha heshi `SHA-256`, na ubofye `CALCULATE HASH` ili kukokotoa heshi ya faili yako.



![Image](assets/fr/09.webp)



Tovuti itaonyesha heshi ya faili yako ya `.apk`. Linganisha na heshi uliyoithibitisha kwenye Keybase.io. Ikiwa heshi mbili zinafanana, ukaguzi wa uhalisi na uadilifu umefaulu. Sasa unaweza kuendelea kusakinisha programu.



![Image](assets/fr/10.webp)



### 2.3. sakinisha programu ya Ashigaru



Ili kusakinisha programu, fungua kidhibiti faili cha simu yako na uende kwenye folda ya vipakuliwa. Kisha ubofye faili ya `.apk` ambayo umeangalia hivi punde, na uthibitishe usakinishaji unapoombwa.



![Image](assets/fr/11.webp)



Ashigaru sasa imesakinishwa kwenye simu yako.



## 3. Anzisha programu na uunde kwingineko ya Bitcoin



Unapozindua programu kwa mara ya kwanza, chagua `MAINNET`.



![Image](assets/fr/12.webp)



Kisha bonyeza `Anza`.



![Image](assets/fr/13.webp)



Sasa tutaunda kwingineko mpya ya Bitcoin. Bonyeza kitufe cha `Unda wallet mpya`.



![Image](assets/fr/14.webp)



### 3.1. unda kwingineko ya Bitcoin



Ashigaru inahitaji passphrase BIP39. Chagua passphrase yako na uiweke katika sehemu zinazofaa. Ni lazima iwe ndefu na nasibu iwezekanavyo ili kupinga shambulio la nguvu-katili.



Weka nakala rudufu ya passphrase hii mara moja. Hii ni hatua muhimu sana: ukipoteza simu yako, **ikiwa huna tena passphrase hii, hutaweza tena kufikia bitcoins zako** zilizohifadhiwa na Ashigaru wallet yako. passphrase hii hiyo pia inatumika kusimba faili ya uokoaji ya wallet kwa njia fiche.



Ikiwa hujui passphrase ni nini, au huelewi kikamilifu jinsi inavyofanya kazi, ninapendekeza sana kwamba usome mafunzo haya ya ziada. Hii ni muhimu, kwa sababu passphrase ni kipengele muhimu cha usalama wako: kutoelewa matumizi yake kunaweza kusababisha hasara ya kudumu ya pesa zako.



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Mara tu unapoingiza passphrase yako, bofya `INAYOFUATA`.



![Image](assets/fr/15.webp)



Kisha chagua msimbo wa PIN. Msimbo huu utatumika kufungua Ashigaru wallet yako, na kuilinda dhidi ya ufikiaji wa kimwili ambao haujaidhinishwa. Haihusiki katika utoaji wa kriptografia wa funguo zako za wallet. Hii ina maana kwamba, hata bila kujua msimbo wa PIN, mtu yeyote aliye na maneno yako ya mnemonic na passphrase ataweza kurejesha upatikanaji wa bitcoins zako.



Chagua PIN ndefu na nasibu. Kumbuka kuweka nakala rudufu katika eneo tofauti na simu yako, ili kuzizuia zisiathiriwe kwa wakati mmoja.



![Image](assets/fr/16.webp)



Pindi msimbo wa PIN unapoundwa, Ashigaru ataonyesha maneno ya mnemonic ya wallet yako. Onyo: kifungu hiki, pamoja na passphrase yako, kinakupa ufikiaji kamili wa bitcoins zako. Mtu yeyote anayeishikilia anaweza kumiliki pesa zako, hata kama hana idhini ya kufikia simu yako. Mfuatano huu wa maneno 12 unaweza kutumika kurejesha wallet yako iwapo simu yako itapotea, kuibiwa au kuharibika. Kwa hiyo ni muhimu kuihifadhi kwa uangalifu mkubwa juu ya kati ya kimwili (karatasi au chuma).



Kamwe usihifadhi kifungu hiki katika mfumo wa dijitali, au una hatari ya kufichua pesa zako kwa wizi. Kulingana na mkakati wako wa usalama, unaweza kuunda nakala kadhaa halisi, lakini usiigawanye. Weka maneno katika mpangilio wake halisi, na uhakikishe kuwa yamehesabiwa.



Hatimaye, usiwahi kuhifadhi mnemonic na passphrase mahali pamoja. Ikiwa zote mbili ziliathiriwa kwa wakati mmoja, mshambuliaji anaweza kupata ufikiaji wa wallet yako.



![Image](assets/fr/17.webp)



Ili kupata maelezo zaidi kuhusu jinsi ya kupata maneno ya mafumbo, tafadhali soma mafunzo haya ya ziada :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Kisha Ashigaru anakuomba uthibitishe tena passphrase yako. Chukua fursa hii kuangalia kuwa nakala yako ya nakala halisi ni sahihi.



![Image](assets/fr/18.webp)



### 3.2. kuunganisha dojo



Inayofuata inakuja hatua ya kuunganisha kwenye Dojo yako. Kama ilivyoelezwa katika utangulizi, Ashigaru lazima aunganishwe na Dojo ili kuingiliana na mtandao wa Bitcoin.



Ingia kwenye "Zana ya Matengenezo" ya Dojo yako na ufungue menyu ya `PAIRING`.



![Image](assets/fr/19.webp)



Kwenye Ashigaru, bonyeza kitufe cha `Changanua QR`, kisha uchanganua msimbo wa QR wa muunganisho unaoonyeshwa na DMT yako. Kisha ubofye `Endelea` ili kuthibitisha.



![Image](assets/fr/20.webp)



Weka PIN yako ili kufungua wallet. Hii itakupeleka kwenye ukurasa wa maingiliano. Ni kawaida kuona hitilafu za *PayNym* katika hatua hii, kwa kuwa wallet ni mpya. Bofya tu `Endelea`.



![Image](assets/fr/21.webp)



Kisha utapelekwa kwenye ukurasa wa nyumbani wa kwingineko yako.



![Image](assets/fr/22.webp)



Kabla ya kwenda mbali zaidi, ninapendekeza ufanye urejeshaji wa majaribio wakati wallet bado haina bitcoin. Hii itakuwezesha kuangalia kuwa nakala zako za karatasi zinafanya kazi ipasavyo. Ili kujua jinsi gani, fuata mafunzo haya:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 4. Kuanzisha programu ya Ashigaru



Ili kufikia mipangilio ya programu, bofya kwenye picha ya *PayNym* yako katika kona ya juu kushoto, kisha uchague `Mipangilio`.



![Image](assets/fr/23.webp)



Hapa utapata chaguo kadhaa za kurekebisha uendeshaji wa Ashigaru kulingana na mahitaji yako. Hata hivyo, ninapendekeza sana kwamba uamilishe vigezo 2 muhimu tangu mwanzo.



Anza kwa kufungua menyu ya `Usalama > Hali ya siri`, kisha uwashe kipengele hiki ukihitaji. Inaficha programu ya Ashigaru nyuma ya jina, nembo na kiolesura cha programu ya kawaida iliyosakinishwa kwenye simu yako. Lengo ni kumzuia mtu yeyote asimtambue Ashigaru katika tukio la ukaguzi wa kimwili wa simu yako.



![Image](assets/fr/24.webp)



Kila programu ghushi inayotolewa ina njia maalum ya kufungua kiolesura halisi cha Ashigaru. Kwa mfano, ukichagua kikokotoo, programu ya Ashigaru itatoweka kwenye skrini yako ya nyumbani na kubadilishwa na kikokotoo cha uwongo. Unapoifungua, unaona kiolesura cha kikokotoo cha kawaida cha kufanya kazi, lakini ili kufikia Ashigaru, unachotakiwa kufanya ni kugonga alama ya `=` mara tano haraka.



Kigezo cha pili muhimu cha kuwezesha ni [**RBF** (*Replace-by-Fee*)](https://planb.academy/resources/glossary/rbf-replacebyfee). Chaguo hili hukuruhusu kuongeza gharama ya shughuli ikiwa itakwama kwenye kumbukumbu kwa sababu gharama ni ya chini sana. Unaweza kuiwasha kupitia menyu ya `Shughuli > Tumia kwa kutumia RBF`.



![Image](assets/fr/25.webp)



Kidokezo: Unaweza kubadilisha kitengo cha kuonyesha cha kwingineko yako kutoka `BTC` hadi `sat` kwa kubofya jumla ya salio iliyoonyeshwa kwenye ukurasa wa nyumbani.



## 5. Pokea bitcoins kwenye Ashigaru



Sasa kwa kuwa kwingineko yako inafanya kazi, unaweza kupokea satss. Ili kufanya hivyo, bonyeza kitufe cha `+` chini kulia mwa kiolesura, kisha kitufe cha kijani `Pokea`.



![Image](assets/fr/26.webp)



Kisha Ashigaru hukuonyesha anwani ya kwanza ya kupokea ambayo haijatumika katika wallet yako, ili kuzuia utumiaji wa anwani (utumiaji wa anwani ni utaratibu mbaya sana kwa faragha yako). Kisha unaweza kusambaza anwani hii kwa mtu au huduma inayohitaji kukutumia bitcoins.



![Image](assets/fr/27.webp)



Mara tu muamala utakapotangazwa kwenye mtandao, utaonekana kiotomatiki kwenye ukurasa wa nyumbani wa programu.



![Image](assets/fr/28.webp)



## 6. Tuma bitcoins na Ashigaru



Sasa kwa kuwa una bitcoins kwenye Ashigaru wallet yako, unaweza pia kuzituma. Ili kufanya hivyo, bonyeza kitufe cha `+` chini kulia, kisha uchague kitufe chekundu cha `Tuma`.



![Image](assets/fr/29.webp)



Kisha chagua akaunti ambayo ungependa kufanya matumizi. Kwa sasa, bado hatujashughulikia akaunti ya `Postmix`, iliyohifadhiwa kwa viunganishi vya sarafu, ambayo tutaangalia katika mafunzo ya baadaye. Kwa hivyo tutatuma pesa kutoka kwa akaunti kuu ya amana.



![Image](assets/fr/30.webp)



Weka maelezo yako ya muamala: kiasi kitakachotumwa na anwani ya Bitcoin ya mpokeaji.



![Image](assets/fr/31.webp)



Kwa kubofya vitone vitatu kwenye kona ya juu kulia, kisha kwenye `Onyesha matokeo ambayo hayajatumika`, unaweza pia kuchagua kwa usahihi ni UTXOs gani ungependa kutumia, ili kuboresha faragha yako.



![Image](assets/fr/32.webp)



Mara tu unapojaza maelezo yote, bofya kwenye kishale cheupe chini ya kiolesura ili kuendelea.



Kisha utapelekwa kwenye ukurasa wa muhtasari unaoonyesha maelezo yote ya muamala wako. Vipengele kadhaa muhimu vinaonyeshwa:




- Katika kizuizi cha `Njia`, angalia mara ya mwisho kwamba anwani ya mpokeaji na kiasi kilichotumwa ni sahihi;
- Katika kizuizi cha `Fees`, unaweza kuona kiwango cha ada kilichochaguliwa kiotomatiki na Ashigaru na, ikiwa ni lazima, kirekebishe kwa kubofya `MANAGE` ;
- Kizuizi cha `Muamala` kinaonyesha aina ya muamala unaokaribia kufanya. Hapa, tunazungumza kuhusu muamala rahisi, lakini Ashigaru pia inasaidia aina nyingine za miamala iliyoboreshwa kwa faragha, ambayo tutashughulikia kwa kina katika mafunzo yajayo;
- Kizuizi chekundu cha `Tahadhari ya Muamala` hukutahadharisha ikiwa muamala wako unaonyesha ruwaza zinazoweza kutambuliwa na zana za uchanganuzi wa mfululizo, na ambazo zinaweza kuhatarisha faragha yako. Kwa kubofya juu yake, unaweza kuona maelezo. Kwa mfano, katika kesi yangu, Ashigaru ananiambia kuwa kiasi kilichotumwa ni cha pande zote (`3000 sats`), ikiniruhusu kuamua ni pato lipi linalolingana na gharama na lipi ni ubadilishaji. Ili kujua zaidi kuhusu heuristics hizi za uchanganuzi wa mnyororo, ninakualika ufuate mafunzo yangu ya BTC 204 kuhusu Mpango ₿ Academy ;
- Hatimaye, unaweza kuongeza lebo kwenye muamala wako ili kuweka rekodi ya madhumuni yake.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Mara tu ukiangalia maelezo yote, tumia kishale cha kijani kutuma bitcoins. Shikilia mshale chini, kisha uuburute kulia ili kuthibitisha upakiaji.



![Image](assets/fr/33.webp)



Muamala wako umetangazwa kwenye mtandao wa Bitcoin.



![Image](assets/fr/34.webp)



## 7. Kurejesha Ashigaru wallet yako



Urejeshaji wa Ashigaru wallet hutofautiana kidogo na ule wa Bitcoin wallet ya kawaida, kwani programu hutumia mbinu sawa na Samurai Wallet. Ukipoteza ufikiaji wa wallet yako (iwe kwa sababu umesahau PIN yako, uliiondoa au umepoteza simu yako), kuna njia kadhaa za kurejesha bitcoins zako.



Ikiwa bado unaweza kufikia simu yako, au kama ulikuwa umehifadhi nakala ya faili hii, njia rahisi ni kutumia faili ya chelezo `ashigaru.txt`. Faili hii ina maelezo yote unayohitaji ili kurejesha kwingineko yako kwenye mfano mpya wa Ashigaru (au kwenye Sparrow Wallet), lakini imesimbwa kwa njia fiche kwa passphrase uliyofafanua katika hatua ya 3.1 ya mafunzo haya. Kwa hivyo ni lazima uwe na faili ya `ashigaru.txt` na passphrase yako ili kutumia mbinu hii.



Kwa vipengele hivi viwili, unaweza, kwa mfano, kurejesha kwingineko yako kwenye Sparrow Wallet.



![Image](assets/fr/35.webp)



Iwapo huna idhini ya kufikia faili ya `ashigaru.txt`, bado unaweza kurejesha ufikiaji wa pesa zako kwa kutumia maneno ya mnemonic ya passphrase, kama vile ungefanya kwa kwingineko yoyote ya Bitcoin. Ninapendekeza ufanye urejeshaji huu ama kwa mfano mpya wa Ashigaru, au moja kwa moja kwenye Sparrow Wallet, ili kurejesha njia za bypass kutoka Whirlpool kwa urahisi ikiwa ulikuwa unaitumia. Vinginevyo, unaweza kuingiza maelezo haya kwenye programu nyingine yoyote inayooana na BIP39 kwa kuingiza mwenyewe njia za utokaji.



Kwa maelezo zaidi kuhusu mchakato huu, tafadhali soma mafunzo kamili ambayo nimeandika kuhusu kurejesha Wallet Samurai wallet. Kwa kuwa Ashigaru ni fork, utaratibu ni sawa:



https://planb.academy/tutorials/wallet/backup/samourai-recover-23bb6221-ea3e-42e6-a5b7-e6dbef5073c3

Kama unaweza kuona, njia yoyote ya urejeshaji unayotumia, passphrase ni ya lazima. Kwa hivyo hakikisha unaiunga mkono kwa uangalifu. Unaweza pia kutengeneza nakala kadhaa, kulingana na mkakati wako wa usalama.



## 8. Sasisha programu



Ili kusasisha programu ya Ashigaru, kwa kuwa uliisakinisha kutoka kwenye faili ya `.apk` na si kupitia Duka la Google Play kama programu ya kawaida, utahitaji kupakua faili mpya ya `.apk` inayolingana na toleo lililosasishwa, kisha uisakinishe wewe mwenyewe.



Rudia hatua zilizoelezwa katika sehemu ya 2 ya mafunzo haya, isipokuwa unapobofya faili ya `.apk` ili kuzindua usakinishaji, **simu yako ya Android inapaswa kukupa chaguo la `Sasisha`, si `Sakinisha`**.



![Image](assets/fr/41.webp)



Hili ni jambo muhimu sana: ikiwa Android itaonyesha `Sakinisha` badala ya `Sasisha`, huenda unasakinisha toleo la ulaghai. Katika kesi hii, kata utaratibu wa ufungaji mara moja.



Kama ilivyokuwa usakinishaji wa kwanza, tafadhali angalia uhalisi na uadilifu wa faili ya `.apk` kabla ya kuendelea na sasisho.



Ili kujua wakati toleo jipya linapatikana, angalia tovuti rasmi ya Ashigaru mara kwa mara. Uwe na uhakika, Ashigaru ni programu thabiti, iliyoiva, iliyorithiwa kutoka kwa Samourai Wallet, na masasisho ni machache ikilinganishwa na programu changa zaidi.



## 9. Changia mradi wa Ashigaru



Ashigaru ni mradi wa chanzo huria. Ikiwa ungependa kufadhili uundaji wake, unaweza kutoa mchango moja kwa moja kutoka kwa programu kupitia PayNym.



Ili kufanya hivyo, bofya PayNym yako katika sehemu ya juu ya kulia ya kiolesura, kisha uchague msimbo wako wa malipo ukianza na `PM...`.



![Image](assets/fr/36.webp)



Kisha bonyeza kitufe cha `+` chini kulia mwa skrini.



![Image](assets/fr/37.webp)



Chagua `Ashigaru Open Source Project` kama mpokeaji.



![Image](assets/fr/38.webp)



Bofya kitufe cha `CONNECT` ili kuanzisha kituo cha mawasiliano cha BIP47 (zaidi kuhusu itifaki hii katika mafunzo yaliyo hapa chini).



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

![Image](assets/fr/39.webp)



Baada ya shughuli ya arifa kuthibitishwa, unaweza kutuma michango yako kwa mradi kwa kubofya kishale kidogo cheupe kwenye kona ya juu ya mkono wa kulia wa kiolesura.



![Image](assets/fr/40.webp)



Sasa unajua jinsi ya kutumia vipengele vya msingi vya programu ya Ashigaru. Katika mafunzo yajayo, tutaangalia jinsi ya kunufaika na miamala ya juu ya matumizi, pamoja na Whirlpool, utekelezaji sanjari uliorithiwa kutoka kwa Samurai Wallet.
https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add
