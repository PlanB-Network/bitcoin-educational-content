---
name: Utangulizi wa Kriptografia
goal: Kuelewa uundaji wa mkoba wa Bitcoin kutoka mtazamo wa kriptografia
objectives:
  - Kufafanua istilahi za kriptografia zinazohusiana na Bitcoin.
  - Kujifunza uundaji wa mkoba wa Bitcoin.
  - Kuelewa muundo wa mkoba wa Bitcoin.
  - Kuelewa anwani na njia za kuzaliana.
---

# Safari katika kriptografia

Je, una mshangao na Bitcoin? Unajiuliza jinsi mkoba wa Bitcoin unavyofanya kazi? Jiandae kwa safari ya kusisimua katika kriptografia! Loïc, mtaalam wetu, atakuongoza kupitia ugumu wa kuunda mkoba wa Bitcoin, akifichua siri nyuma ya istilahi za kiufundi zenye kutisha kama vile hashing, kuzaliana kwa funguo, na mizunguko ya elliptic.

Mafunzo haya hayatakupa tu maarifa ya kuelewa muundo wa mkoba wa Bitcoin, lakini pia kukutayarisha kuchunguza zaidi ulimwengu wa kusisimua wa kriptografia. Basi, je, uko tayari kuanza safari hii? Jiunge nasi na geuza udadisi wako kuwa ujuzi!

+++

# Utangulizi

## Utangulizi wa Kriptografia

### Je, mafunzo haya ni kwa ajili yako? NDIYO!

![utangulizi na Rogzy](https://youtu.be/ul8zU5QWIXg)

Tunafurahi kukukaribisha kwenye kozi mpya ya mafunzo inayoitwa "Crypto 301: Utangulizi wa Kriptografia na HD Wallet", iliyoandaliwa na mtaalam mwenyewe, Loïc Morel. Kozi hii itakuzamisha katika ulimwengu wa kusisimua wa kriptografia, nidhamu msingi ya hisabati ambayo inahakikisha kusimbwa na usalama wa data yako.

Katika maisha yetu ya kila siku, na hasa katika uwanja wa Bitcoin, kriptografia inacheza jukumu muhimu. Dhana zinazohusiana na kriptografia kama vile funguo za faragha, funguo za umma, anwani, njia za kuzaliana, mbegu, na entropy zipo moyoni mwa matumizi na uundaji wa mkoba wa Bitcoin. Katika kozi hii, Loïc ataelezea kwa undani jinsi funguo za faragha zinavyozalishwa na jinsi zinavyohusishwa na anwani. Loïc pia atatumia saa moja kuelezea maelezo ya hisabati ya mizunguko ya elliptic, mzunguko huu mgumu wa hisabati. Aidha, utaelewa kwa nini matumizi ya HMAC SHA512 ni muhimu kwa kusimba mkoba wako na tofauti kati ya mbegu na kauli ya mnemoniki.

Lengo kuu la mafunzo haya ni kukusaidia kuelewa michakato ya kiufundi ya kuunda mkoba wa HD na njia za kriptografia zinazotumiwa. Kwa miaka, mikoba ya Bitcoin imeendelea kuwa rahisi kutumia, salama zaidi, na imekuwa kiwango kutokana na BIPs maalum. Loïc atakusaidia kuelewa BIPs hizi ili kuelewa chaguzi zilizofanywa na watengenezaji wa Bitcoin na wataalamu wa kriptografia. Kama mafunzo yote yanayotolewa na chuo chetu, hii ni bure kabisa na chanzo wazi. Hii inamaanisha kuwa unaweza kuchukua na kutumia mafunzo haya kama unavyotaka. Tunatarajia kupokea maoni yako mwishoni mwa kozi hii ya kusisimua.

### Sasa ni zamu yako, profesa!

![utangulizi na loïc](https://youtu.be/mwuxXLk4Kws)

Habari zenu wote, mimi ni Loïc Morel, mwongozaji wako katika uchunguzi huu wa kiufundi wa kriptografia inayotumiwa katika mikoba ya Bitcoin.

Safari yetu inaanza na kuchunguza kwa kina kazi za ndani za kazi za hash za kriptografia. Pamoja, tutachambua jinsi SHA256 muhimu na kuchunguza algorithm mbalimbali zilizotengwa kwa ajili ya kuzaliana.

Tutaendelea na uchunguzi wa ulimwengu wa siri wa saini za kidijitali. Utagundua jinsi uchawi wa mizunguko ya elliptic unavyotumika kwenye saini hizi, na tutatoa ufafanuzi juu ya jinsi ya kuhesabu funguo za umma kutoka kwa funguo za faragha. Na bila shaka, tutajadili hatua ya kusaini kwa kutumia funguo za faragha.
Kisha, tutarudi nyuma katika wakati ili kuona mabadiliko ya mifuko ya Bitcoin, na tutajadili dhana za entropy na nambari za nasibu. Tutapitia kwa kina sentensi maarufu ya mnemoniki, huku tukijadili pia suala la maneno ya siri. Hata utapata fursa ya kujaribu kitu kipekee kwa kuunda mbegu kutoka kwa kurusha kete 128!

Kwa msingi imara kama huo, tutakuwa tayari kwa sehemu muhimu: kuunda mfuko wa Bitcoin. Kutoka kwa kuzaliwa kwa mbegu na ufunguo mkuu, hadi kujifunza kuhusu ufunguo uliopanuliwa, na kuzalisha jozi za ufunguo wa watoto, kila hatua itachunguzwa kwa undani. Tutajadili pia muundo wa mfuko na njia za kuzalisha.

Kumalizia yote haya, tutahitimisha safari yetu kwa kuchunguza anwani za Bitcoin. Tutaelezea jinsi zinavyoundwa na jinsi zinavyocheza jukumu muhimu katika utendaji wa mifuko ya Bitcoin.

Jiunge nami katika safari hii ya kuvutia, na jiandae kuchunguza ulimwengu wa kriptografia kama kamwe kabla. Acha dhana zako za awali mlangoni na fungua akili yako kwa njia mpya ya kuelewa Bitcoin na muundo wake msingi.

# Kazi za Hash

## Utangulizi kwa kazi za hash za kriptografia zinazohusiana na Bitcoin

![2.1 - Kazi za Hash za Kriptografia](https://youtu.be/dvnGArYvVr8)

Karibu kwenye kikao cha leo kilichojitolea kwa kina katika ulimwengu wa kriptografia wa kazi za hash, ambazo ni msingi muhimu wa usalama wa itifaki ya Bitcoin. Fikiria kazi ya hash kama roboti ya kriptografia yenye ufanisi mkubwa ambayo inabadilisha habari za ukubwa wowote kuwa alama ya kidijitali ya kipekee na ya ukubwa uliowekwa inayoitwa "hash". Katika uchunguzi wetu, tutaelezea sifa za kazi za hash za kriptografia, tukionyesha matumizi yao katika itifaki ya Bitcoin, na kufafanua malengo maalum ambayo kazi hizi za kriptografia lazima zifikie.

![picha](assets/image/section1/0.JPG)

Kuelezea sifa za kazi za hash za kriptografia kunahitaji kuelewa sifa mbili muhimu: kutokurekebishika kwao na upinzani wao dhidi ya udanganyifu. Kila kazi ya hash ya kriptografia ni kama msanii mmoja wa kipekee, akizalisha "hash" tofauti kwa kila kipengele cha kuingizwa. Hata brashi inayotofautiana kidogo inabadilisha sana picha ya mwisho, yaani, hash. Kazi hizi hufanya kazi kama walinzi wa kidijitali, kuhakikisha uadilifu wa programu iliyopakuliwa. Tabia muhimu nyingine wanayo ni upinzani wao dhidi ya migongano. Bila shaka, katika ulimwengu wa kuhesabu hash, migongano haiwezi kuepukika, lakini kazi nzuri ya hash ya kriptografia inapunguza migongano hiyo kwa kiasi kikubwa. Ni kama kila hash ni nyumba katika mji mkubwa; licha ya idadi kubwa ya nyumba, kazi nzuri ya hash inahakikisha kila nyumba ina anwani ya kipekee.

![picha](assets/image/section1/1.JPG)

Hebu sasa tuvuke maji yenye msukosuko ya kazi za hash zilizopitwa na wakati. SHA0, SHA1, na MD5 sasa zinachukuliwa kama vitu vya zamani katika bahari ya kuhesabu hash ya kriptografia. Mara nyingi huzuiwa kwa sababu wamepoteza upinzani wao dhidi ya migongano. Kanuni ya makabati inaelezea kwa nini, licha ya jitihada zetu bora, kuepuka migongano ni jambo lisilowezekana kutokana na kikomo cha ukubwa wa matokeo. Ni muhimu pia kutambua kuwa upinzani dhidi ya pili ya picha unategemea upinzani dhidi ya migongano. Ili kuchukuliwa kuwa salama kweli, kazi ya hash lazima iweze kuzuia migongano, pili ya picha, na picha ya kwanza.

Kipengele muhimu katika itifaki ya Bitcoin, kazi ya hash ya SHA-256 ndiye nahodha wa meli. Kazi nyingine, kama vile SHA-512, hutumiwa kwa kuzalisha na HMAC na PBKDF. Aidha, RIPMD160 hutumiwa kupunguza alama ya vidole hadi bits 160. Tunapozungumzia HASH256 na HASH160, tunarejelea matumizi ya kuhesabu hash mara mbili na SHA-256 na RIPMD. Matumizi ya HASH160 ni ya faida hasa kwani inaruhusu usalama wa SHA-256 wakati inapunguza ukubwa wa alama ya kidole.
Kwa kumalizia, lengo kuu la kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya kazi ya
Hatimaye, baada ya kugawanya kuingiza imara katika sehemu tofauti za ujumbe wa biti 512, tunafanya mizunguko 64 ya hesabu katika kazi ya kusukuma. Kama katika mbio za baiskeli, kila mzunguko unaboresha nafasi yetu. Tunahesabu hali ya kati kwa hali ya awali ya kazi ya kusukuma kwa kuongeza modulo 2^32. Kuongeza katika kazi ya kusukuma ni kuongeza modulo 2^32 ili kudhibiti ukubwa wa jumla hadi biti 32.

Kwa kumalizia, tunapenda kusisitiza jukumu muhimu la hesabu zinazofanywa katika sanduku za CH, MAJ, σ0, na σ1. Uendeshaji huu, miongoni mwa wengine, ni walinzi ambao huhakikisha uimara wa kazi ya hash ya SHA256 dhidi ya mashambulizi, ikifanya kuwa chaguo la kupendelewa kwa kusimamia mifumo mingi ya dijiti, haswa ndani ya itifaki ya Bitcoin. Ni dhahiri kwamba, ingawa ni ngumu, uzuri wa SHA256 unapatikana katika uimara wake wa kupata kuingiza kutoka kwa hash, wakati kuhakiki hash kwa kuingiza lililopewa ni hatua rahisi kwa kiufundi.

## Algorithm zinazotumiwa kwa kuzaliwa

![Algorithm zinazotumiwa kwa kuzaliwa](https://youtu.be/ZF1_BMsOJXc)

Algorithm za kuzaliwa za HMAC na PBKDF2 ni sehemu muhimu katika mfumo wa usalama wa itifaki ya Bitcoin. Zinazuia aina mbalimbali za mashambulizi na kuhakikisha uadilifu wa mifuko ya Bitcoin.

HMAC na PBKDF2 ni zana za kriptografia zinazotumiwa kwa kazi tofauti katika Bitcoin. HMAC hutumiwa hasa kupinga mashambulizi ya kuongeza urefu wakati wa kuzalisha mifuko ya hierarchically deterministic (HD), wakati PBKDF2 hutumiwa kubadilisha neno la mnemoniki kuwa mbegu.

HMAC, ambayo inachukua ujumbe na ufunguo kama pembejeo, inazalisha pembejeo ya ukubwa uliowekwa. Ili kuhakikisha usawa, ufunguo unabadilishwa kulingana na ukubwa wa kizuizi kinachotumiwa katika kazi ya hash. Katika muktadha wa kuzaliwa kwa mifuko ya HD, HMAC-SHA-512 hutumiwa. Hii ya mwisho inafanya kazi na kizuizi cha biti 1024 (baiti 128) na kurekebisha ufunguo kwa mujibu huo. Inatumia vikwazo vya OPAD (0x5c) na IPAD (0x36), vilivyorejewa kama inavyohitajika kuimarisha usalama.

Mchakato wa HMAC-SHA-512 unahusisha kuunganisha matokeo ya SHA-512 yaliyotumiwa kwa ufunguo XOR OPAD na ufunguo XOR IPAD na ujumbe. Ikitumiwa na kizuizi cha biti 1024 (baiti 128), ufunguo wa pembejeo unapigwa kwa sufuri ikiwa ni lazima, kisha XORed na IPAD na OPAD. Ufunguo uliobadilishwa kisha unaunganishwa na ujumbe.

Matumizi ya chumvi, kwa kuingiza chanzo kingine cha entropy, huongeza usalama wa funguo zilizozaliwa. Bila hiyo, shambulio linaweza kuhatarisha mifuko yote na kuiba bitcoins zote.
PBKDF2 hutumiwa kubadilisha kauli ya mnemoniki kuwa mbegu. Algorithm hii inafanya raundi 2048 kwa kutumia HMAC SHA512. Kwa sababu ya algorithm hizi za kuzaliana, viingizo viwili tofauti vinaweza kutoa matokeo ya pekee na yaliyofungwa, ambayo inapunguza tatizo la mashambulizi ya kuongeza urefu kwenye kazi za familia ya SHA-2. Shambulio la kuongeza urefu linatumia sifa maalum ya kazi fulani za hash ya kriptografia. Katika shambulio kama hilo, mshambuliaji ambaye tayari ana hash ya ujumbe usiojulikana anaweza kuitumia kuhesabu hash ya ujumbe mrefu zaidi, ambao ni kuongeza ya ujumbe wa awali. Mara nyingi hii inawezekana bila kujua maudhui ya ujumbe wa awali, ambayo inaweza kusababisha udhaifu mkubwa wa usalama ikiwa aina hii ya kazi ya hash inatumika kwa kazi kama uhakiki wa ukweli.

Kwa hitimisho, algorithm za HMAC na PBKDF2 zina jukumu muhimu katika usalama wa kuzaliana kwa mkoba wa HD katika itifaki ya Bitcoin. HMAC-SHA-512 hutumiwa kulinda dhidi ya mashambulizi ya kuongeza urefu, wakati PBKDF2 inaruhusu kubadilisha kauli ya mnemoniki kuwa mbegu. Kanuni ya mnyororo inaongeza chanzo kingine cha entropy katika kuzaliana kwa funguo, ikidumisha nguvu ya mfumo.

# Saini za Dijitali

## Saini za Dijitali na Mipira ya Elipiti

![Saini za Dijitali na Mipira ya Elipiti](https://youtu.be/gOjYiPkx4z8)

Katika ulimwengu wa sarafu za dijitali, usalama wa shughuli ni muhimu sana. Katika msingi wa itifaki ya Bitcoin, saini za dijitali hutumiwa kama ushahidi wa kihisabati unaodhihirisha umiliki wa ufunguo wa kibinafsi unaohusishwa na ufunguo wa umma maalum. Teknolojia hii ya ulinzi wa data inategemea msingi wa kuvutia wa kriptografia unaoitwa kriptografia ya mipira ya elipiti (ECC).

![image](assets/image/section2/0.JPG)

Kriptografia ya mipira ya elipiti ndio msingi wa usalama wa shughuli za Bitcoin. Mipira hii ya elipiti, inayokumbusha mipira ya hisabati tuliyosoma shuleni, ina faida katika matumizi mbalimbali ya kriptografia, ikiwa ni pamoja na kubadilishana funguo, kuchanganya usimbaji, na uundaji wa saini za dijitali. Jambo la kuvutia linalotofautisha mipira ya elipiti ni usawa wake: mstari wowote usio wima unaokatiza alama mbili kwenye mpira utakatiza alama ya tatu.

Sasa hebu tuende kidogo zaidi: itifaki ya Bitcoin hutumia mpira maalum wa elipiti unaoitwa SecP256K1 kufanya shughuli zake za kriptografia. Mpira huu, uliofafanuliwa kwenye seti ya nambari chanya za mwisho wa namba ya kimsingi ya 256, unaweza kuonekana kama wingu la alama badala ya mstari wa jadi. Ni muundo huu wa kipekee ambao unaruhusu Bitcoin kuhakikisha usalama wake kwa ufanisi.

![image](assets/image/section2/1.JPG)

Kuhusu uchaguzi wa mpira wa secp256k1 kwa Bitcoin, ni muhimu kufahamu kuwa ulipendelewa kuliko mpira wa secp256r1. Mpira huu unafafanuliwa na vigezo a=0 na b=7, na equation yake ni y² = x³ + 7 modulo n, ambapo n inawakilisha namba ya kimsingi inayotambua utaratibu wa mpira.

Tunapozungumzia vipengele vinavyotumiwa katika mfumo wa Bitcoin, kwa ujumla tunarejelea vigezo maalum vya Algorithm ya Saini ya Dijitali ya Mipira ya Elipiti (ECDSA) na mfumo wa mipira ya elipiti inayotumiwa na Bitcoin, ambayo ni mpira wa secp256k1. Hapa kuna vigezo hivyo:
- uga wa kwanza (p): Bitcoin hutumia mzunguko juu ya uga wa kwanza, kwa hivyo p ni nambari ya kwanza inayotumika kufafanua uga huu. Kwa mzunguko wa secp256k1, p ni sawa na `p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F` kwa mfumo wa hexadecimal au p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 -1 kwa mfumo wa decimal.
- utaratibu wa mzunguko (n): Hii ni idadi ya pointi kwenye mzunguko, ikiwa ni pamoja na pointi ya upeo. Kwa secp256k1, n ni sawa na `n = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141` kwa mfumo wa hexadecimal au n = 2^256 - 432420386565659656852420866394968145599 kwa mfumo wa decimal.
- pointi ya jenereta (G): Pointi ya msingi, au jenereta, ni pointi kwenye mzunguko ambayo pointi zingine zote za umma huzalishwa kutoka kwake. Ina vipengele maalum vya x na y, kawaida vikiwakilishwa kwa mfumo wa hexadecimal. Kwa secp256k1, vipengele vya G ni, kwa mfumo wa hexadecimal:
  - `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
  - `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

![image](assets/image/section2/2.JPG)

Tafadhali kumbuka kuwa thamani zote za hexadecimal kwa ujumla zinaonyeshwa kwa mfumo wa msingi 16, wakati thamani za decimal zinaonyeshwa kwa mfumo wa msingi 10. Aidha, shughuli zote kwenye vipengele hivi hufanywa modulo p kwa vipengele vya pointi kwenye mzunguko na modulo n kwa shughuli za ufunguo na saini.

Basi, wapi hasa bitcoins hizi maarufu zimehifadhiwa? Sio kwenye mkoba wa Bitcoin, kama mtu anavyoweza kufikiria. Kwa kweli, mkoba wa Bitcoin huhifadhi funguo za kibinafsi zinazohitajika kuthibitisha umiliki wa bitcoins. Bitcoins wenyewe hurekodiwa kwenye blockchain, hifadhidata isiyosimamiwa ambayo inahifadhi shughuli zote.

Katika mfumo wa Bitcoin, kitengo cha akaunti ni bitcoin (tazama herufi ndogo "b"). Inaweza kugawanywa hadi nafasi nane za kumi, na kitengo kidogo zaidi kikiwa satoshi. UTXOs, au "Unspent Transaction Outputs," inawakilisha pato la shughuli ambalo halijatumika la mtumiaji. Ili kutumia bitcoins hizi, mtu lazima athibitishe umiliki wa funguo za kibinafsi zinazolingana na funguo za umma zinazohusiana na kila UTXO.

Ili kuhakikisha usalama wa shughuli, Bitcoin hutegemea itifaki mbili za saini za dijiti: ECDSA (Elliptic Curve Digital Signature Algorithm) na Schnorr. ECDSA ni itifaki ya saini iliyounganishwa ndani ya Bitcoin tangu kuzinduliwa kwake mnamo 2009, wakati saini za Schnorr ziliongezwa hivi karibuni mnamo Novemba 2021. Ingawa itifaki zote zinategemea cryptography ya mzunguko wa elliptic na kutumia taratibu za kihisabati zinazofanana, tofauti kuu ni muundo wa saini.

Kabla ya kuchunguza kwa undani taratibu hizi za saini, ni muhimu kuelewa ni nini mzunguko wa elliptic. Mzunguko wa elliptic unafafanuliwa na equation y² = x³ + ax + b. Kila pointi kwenye mzunguko huu ina usawa maalum ambao ni muhimu kwa umuhimu wake katika cryptography.
Hatimaye, mizunguko mbalimbali ya duara imekubaliwa kuwa salama kwa matumizi ya kriptografia. Labda inayojulikana zaidi ni mzunguko wa secp256r1. Walakini, kwa Bitcoin, Satoshi Nakamoto aliamua kutumia mzunguko tofauti: secp256k1.

Katika sehemu inayofuata ya kozi hii, tutachunguza kwa karibu ufunguo wa umma na ufunguo wa kibinafsi ili kuelewa kikamilifu kriptografia kwenye mizunguko ya duara na algorithm ya saini ya dijiti. Hii ndio wakati wa kuimarisha maarifa yako na kuelewa jinsi habari hii yote inakuja pamoja kuhakikisha usalama wa itifaki ya Bitcoin.

## Kuhesabu ufunguo wa umma kutoka kwa ufunguo wa kibinafsi

![Kuhesabu ufunguo wa umma kutoka kwa ufunguo wa kibinafsi](https://youtu.be/NJENwFU889Y)

Katika sehemu inayofuata ya kozi hii, tutachunguza kwa undani mifumo ya ufunguo wa umma na ufunguo wa kibinafsi, vipengele viwili muhimu sana vya itifaki ya Bitcoin. Ufunguo hizi zinaunganishwa kwa asili na Algorithm ya Saini ya Dijiti ya Mizunguko ya Duara (ECDSA). Kuzielewa kutatupa ufahamu wa kina juu ya jinsi Bitcoin inahakikisha shughuli kwenye jukwaa lake.

![image](assets/image/section2/3.JPG)
![image](assets/image/section2/4.JPG)

Kuanza, hebu tuingie ulimwengu wa algorithm ya ECDSA. Bitcoin hutumia algorithm hii ya saini ya dijiti kuunganisha ufunguo wa kibinafsi na ufunguo wa umma. Katika mfumo huu, ufunguo wa kibinafsi ni nambari ya 256-bit ya nasibu au pseudo-nasibu. Jumla ya idadi ya uwezekano kwa ufunguo wa kibinafsi ni nadharia 2^256, lakini kwa kweli, ni kidogo kuliko hiyo. Kwa usahihi, baadhi ya ufunguo wa kibinafsi wa 256-bit sio halali kwa Bitcoin.

![image](assets/image/section2/5.JPG)

Ili kuwa sawa na Bitcoin, ufunguo wa kibinafsi lazima uwe kati ya 1 na n-1, ambapo n inawakilisha utaratibu wa mzunguko wa duara. Hii inamaanisha kuwa jumla ya idadi ya uwezekano kwa ufunguo wa kibinafsi wa Bitcoin ni karibu sawa na 1.158 x 10^77. Ili kuweka hii katika mtazamo, ni takriban idadi sawa ya atomi zilizopo katika ulimwengu unaoweza kuonekana. Ufunguo wa kibinafsi wa kipekee kisha hutumiwa kutoa ufunguo wa umma wa 512-bit.

![image](assets/image/section2/6.JPG)

Ufunguo wa umma, unaoonyeshwa kama K, ni hatua kwenye mzunguko wa duara ambayo inatokana na ufunguo wa kibinafsi kwa kutumia shughuli za hatua kwenye mzunguko. Ni muhimu kutambua kuwa kazi ya ECDSA haiwezi kubadilishwa, maana haiwezekani kupata ufunguo wa kibinafsi kutoka kwa ufunguo wa umma. Urejeshaji huu usiobadilishwa ni msingi wa usalama wa pochi ya Bitcoin.

Ufunguo wa umma unajumuisha hatua mbili za 256-bit, jumla ya biti 512. Walakini, inaweza kusukumwa kuwa nambari ya 264-bit. Hatua G ni hatua ya kuanzia ya kuhesabu ufunguo wa umma wa watumiaji wote katika mfumo.

![image](assets/image/section2/7.JPG)

Sifa moja ya kushangaza ya mizunguko ya duara ni kwamba mstari unaoingiliana na mzunguko kwenye hatua mbili pia utaingiliana na hatua ya tatu, inayoitwa hatua O. Sifa hii hutumiwa kubaini hatua U, ambayo ni kinyume cha hatua O. Kuongeza hatua kwa yenyewe hufanywa kwa kuchora mstari mstari kwenye mzunguko kwenye hatua hiyo, ikisababisha hatua mpya ya pekee inayoitwa j. Kuzidisha kwa kiasi cha hatua na n ni sawa na kuongeza hatua hiyo kwa yenyewe mara n.

![image](assets/image/section2/8.JPG)
Hizi operesheni kwenye alama za mzunguko wa duara ni msingi wa kuhesabu funguo za umma. Kwa kujua funguo za siri, ni rahisi kuhesabu funguo za umma. Hata hivyo, kujua funguo za umma hakuruhusu kuhesabu funguo za siri, hivyo kuhakikisha usalama wa mfumo wa Bitcoin. Kwa kweli, usalama wa funguo za umma na siri unategemea tatizo la logaridi ya kugawanyika, swali la hisabati ngumu.

Katika somo letu lijalo, tutachunguza jinsi saini ya kidijitali inapatikana kwa kutumia algorithm ya ECDSA na funguo ya siri ili kufungua bitcoins. Endelea kuwa makini kwa uchunguzi huu wa kusisimua wa ulimwengu wa sarafu za kidijitali na kriptografia.

## Kusaini kwa kutumia funguo ya siri

![Kusaini kwa kutumia funguo ya siri](https://youtu.be/h2hIyGgPqkM)

Mchakato wa saini ya kidijitali ni njia muhimu ya kuthibitisha kuwa wewe ni mmiliki wa funguo ya siri bila kuiruhusu kujulikana. Hii inafanikiwa kwa kutumia algorithm ya ECDSA, ambayo inahusisha kujua nambari ya pekee, kuhesabu nambari maalum V, na kuunda saini ya kidijitali iliyojengwa na sehemu mbili, S1 na S2. Ni muhimu kutumia nambari ya pekee daima ili kuepuka mashambulizi ya usalama. Mfano maarufu wa kile kinachoweza kutokea wakati sheria hii haifuatwi ni kesi ya kuvunjika kwa PlayStation 3, ambayo ilidhoofishwa kutokana na matumizi ya nambari ya pekee mara kwa mara.

Kwa kawaida, hatua zifuatazo zinahusika katika kuthibitisha saini ya kidijitali kwa kutumia algorithm ya ECDSA (Elliptic Curve Digital Signature Algorithm):

1. Thibitisha kuwa thamani za saini, S1 na S2, ziko kwenye kikomo cha [1, n-1]. Ikiwa sivyo, saini ni batili.
2. Hesabu kinyume cha S2 mod n. Tutaita hii u. Mara nyingi hupatikana kama ifuatavyo: u = (S2)^-1 mod n.
3. Hesabu H, ambayo ni thamani ya hash ya ujumbe uliosainiwa.
4. Hesabu u1 = H _ u mod n na u2 = S1 _ u mod n.
5. Hesabu alama P kwenye mzunguko wa duara kwa kutumia u1, u2, na funguo ya umma K: P = u1*G + u2*K, ambapo G ni alama ya jenereta ya mzunguko wa duara.
6. Ikiwa P ni alama ya kutoweka, saini ni batili.
7. Hesabu I = kigawanyo cha x ya P mod n.
8. Saini ni halali ikiwa I ni sawa na S1.

Ni muhimu kutambua kuwa kila programu inaweza kutumia alama tofauti na hatua fulani zinaweza kuunganishwa au kubadilishwa, lakini mantiki ya msingi inabaki ile ile. Pia kumbuka kuwa shughuli zote za hesabu zinafanywa kwenye uga ulioainishwa na mzunguko wa duara (mod n, ambapo n ni utaratibu wa mzunguko wa duara). Kama kumbusho, mzunguko wa secp256k1 (unaotumiwa katika Bitcoin) una n = 2^256 - 432420386565659656852420866394968145599. Linapokuja suala la kuzalisha funguo za umma na siri, ni muhimu kujifunza kuhusu mzunguko wa duara na alama ya jenereta. Ili kupata funguo ya umma, nambari ya nasibu lazima ichaguliwe kama funguo ya siri, mara nyingi huitwa `nonce`, na kutumika katika equation ya mzunguko wa duara.
Mzingo wa elliptic ni chombo chenye nguvu cha kuzalisha funguo za umma na za kibinafsi zenye usalama. Kwa mfano, ili kupata funguo za umma 3G, unachora mstari mnyoofu kwenye alama G, kisha unahesabu kinyume cha -G ili kupata 2G, na kisha kuongeza G na 2G. Ili kufanya muamala, lazima uthibitishe kuwa unajua nambari 3 kwa kufungua bitcoins zinazohusiana na funguo ya umma 3G.
 
Ili kuunda saini ya dijiti na kuthibitisha kuwa unajua funguo ya kibinafsi inayohusiana na funguo ya umma 3G, kwanza unahesabu nambari isiyojulikana, kisha alama V inayohusiana na nambari hii isiyojulikana (kwa mfano, ni 4G). Kisha, unahesabu alama T kwa kuongeza funguo ya umma 3G na alama V, ambayo inatoa 7G.

Kuweka saini ya dijiti ni hatua muhimu katika kutumia algorithm ya ECDSA, ambayo inaruhusu kuthibitisha uhalisi wa ujumbe uliosainiwa bila kuhitaji funguo ya kibinafsi ya mtumaji. Hapa ndivyo inavyofanya kazi kwa undani:

Katika mfano wetu, tuna thamani mbili muhimu: T na V. T ni thamani ya kimaumbile (7 katika mfano huu), na V ni alama kwenye mzingo wa elliptic (inayowakilishwa na 4G hapa). Thamani hizi zinazalishwa wakati wa kuunda saini ya dijiti na kisha zinatumwa pamoja na ujumbe ili kuwezesha uthibitisho.

Mara tu mpokeaji anapopokea ujumbe, pia atapokea thamani hizi mbili, T na V.

Hapa ni hatua ambazo mpokeaji atafuata kuthibitisha saini:

1. Kwanza, watahesabu hash ya ujumbe, ambayo tutaiita H.
2. Kisha, watahesabu u1 na u2. Kufanya hivyo, wataitumia fomula zifuatazo:
   - u1 = H * (S2)^-1 mod n
   - u2 = T * (S2)^-1 mod n'

# Sentensi ya mnemoniki

## Maendeleo ya mifuko ya Bitcoin

![Maendeleo ya mifuko ya Bitcoin](https://youtu.be/6tmu1R9cXyk)

Mfuko wa Hierarchical Deterministic, au maarufu zaidi kama mfuko wa HD, unacheza jukumu muhimu katika mfumo wa sarafu ya sarafu. Neno "mfuko" linaweza kuonekana kuwa la kudanganya kwa wale wapya katika uwanja huu, kwani halimaanishi kushikilia pesa au sarafu. Badala yake, inahusu mkusanyiko wa funguo za kibinafsi za kriptografia zilizopatikana kutoka kwa funguo mkuu mmoja, kwa njia ya mchakato wa hesabu ya algorithmic. Funguo hizi za kibinafsi, ambazo ni urefu wa 256 bits, ndizo kiini halisi cha umiliki wa sarafu ya kriptografia, na mara nyingi huitwa kwa jina la "Just a Bunch Of Keys" (JBOC) kwa jina la kawaida.

![image](assets/image/section3/0.JPG)

Hata hivyo, ugumu wa kusimamia funguo hizi unatulizwa na seti ya itifaki, inayojulikana kama Bitcoin Improvement Proposals (BIPs). Mapendekezo haya ya kuboresha ni msingi wa utendaji na usalama wa mifuko ya HD. Kwa mfano, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), iliyozinduliwa mwaka 2012, ilibadilisha njia funguo hizi zinazozalishwa na kuhifadhiwa, ikileta dhana ya funguo zilizopatikana kwa njia ya kuhesabiwa kwa njia ya kihierarkia na kwa njia ya kuhesabiwa kwa njia ya kihierarkia. Hii inasaidia sana mchakato wa kuokoa funguo hizi, wakati inaendelea kudumisha kiwango chao cha usalama.

![image](assets/image/section3/1.JPG)
Kwa hiyo, [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) ilileta ubunifu muhimu: sentensi ya maneno 24 yenye mnemoniki. Mfumo huu ulifanya iwezekane kubadilisha mfuatano mgumu wa tarakimu ambao ni vigumu kukumbuka kuwa safu ya maneno ya kawaida, ambayo ni rahisi zaidi kukumbuka na kuhifadhi. Aidha, [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) ilipendekeza kuongeza neno la siri la ziada ili kuimarisha usalama wa funguo binafsi. Maboresho haya yaliyofuata yalisababisha BIP43 na BIP44, ambazo zilistandarisha muundo na muundo wa mifuko ya HD, kufanya iwe rahisi zaidi na rahisi kutumia kwa umma.

Katika sehemu zifuatazo, tutachunguza kwa undani jinsi mifuko ya HD inavyofanya kazi. Tutajadili kanuni za kuzaliana kwa funguo, na kuchunguza dhana msingi za entropy na kuzalisha nambari za nasibu, ambazo ni muhimu kuhakikisha usalama wa mifuko yako ya HD.

Mfuko wa Hierarchical Deterministic, au maarufu zaidi kama mfuko wa HD, unacheza jukumu kuu katika mfumo wa sarafu ya sarafu. Neno "mfuko" linaweza kuonekana kuwa la kudanganya kwa wale wapya katika uwanja huu, kwani halimaanishi kushikilia pesa au sarafu. Badala yake, inahusu mkusanyiko wa funguo za siri za kryptographiska zilizopatikana kutoka kwa funguo mkuu mmoja, shukrani kwa mchakato wa hesabu ya algorithmic. Funguo hizi za siri, ambazo ni urefu wa 256 bits, ndizo kiini cha umiliki wa sarafu ya sarafu, na mara nyingine huitwa kwa jina la "Just a Bunch Of Keys" (JBOC) kwa jina la kawaida kidogo.

![picha](assets/image/section3/0.JPG)

Hata hivyo, ugumu wa kusimamia funguo hizi unafidiwa na seti ya itifaki, inayojulikana kama Maboresho ya Bitcoin (BIPs). Mapendekezo haya ya kuboresha yako katika kiini cha utendaji na usalama wa mifuko ya HD. Kwa mfano, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), iliyozinduliwa mwaka 2012, ilibadilisha njia funguo hizi zinazozalishwa na kuhifadhiwa, ikileta dhana ya funguo zilizopatikana kwa njia ya kuzaliana kwa utaratibu na kwa njia ya hiyerarkia. Hii inasaidia sana mchakato wa kuhifadhi funguo hizi, wakati inadumisha kiwango chao cha usalama.![picha](assets/image/section3/1.JPG)

Kwa muhtasari, ni muhimu kuzingatia jukumu kuu la BIP32 na BIP39 katika kubuni na usalama wa mifuko ya HD. Itifaki hizi zinaruhusu kuzalisha funguo nyingi kutoka kwa mbegu moja, ambayo inapaswa kuwa nambari ya nasibu au nambari ya pseudo-nasibu. Leo, viwango hivi vimekubaliwa na idadi kubwa ya mifuko ya sarafu ya sarafu, iwe inalenga sarafu moja au inasaidia aina mbalimbali za sarafu.

Natumai utangulizi huu umekusaidia kuelewa vizuri misingi ya mifuko ya HD na sifa zake mbalimbali. Lengo letu ni kukusaidia kumudu dhana muhimu hizi na kupata njia bora zaidi katika ulimwengu tata wa sarafu ya sarafu. Kwa hiyo, endelea kuwa nasi tunapoendelea kuchunguza undani na nyuzi za ulimwengu huu wa kuvutia katika masomo yanayofuata.

## Entropy na Nambari za Nasibu

![Entropy na Nambari za Nasibu](https://youtu.be/k18yH18w2TE)
Umuhimu wa usalama wa funguo binafsi katika mfumo wa Bitcoin ni dhahiri. Kwa kweli, funguo hizo ni msingi ambao hutoa usalama wa shughuli za Bitcoin. Ili kuepuka udhaifu wowote unaohusiana na uwezekano, funguo hizi lazima zizalishwe kwa njia ya kweli ya nasibu, ambayo inaweza kuwa zoezi gumu kwa mtumiaji. Suluhisho moja kwa tatizo hili ni Mkoba wa Hierarchical Deterministic, au HD wallet. Njia hii inaruhusu uzalishaji wa nasibu na wa hiari wa jozi za funguo za watoto kutoka kwa kipande kimoja cha habari kwenye msingi wa mkoba. Hapa ndipo nasibu inakuwa muhimu kuhakikisha usalama wa funguo zilizopatikana.
![image](assets/image/section3/2.JPG)

Uzalishaji wa nambari za nasibu ni kweli sehemu muhimu katika kriptografia, ili kuhakikisha uadilifu wa funguo binafsi. Ili kuepuka udhaifu wowote unaohusiana na uwezekano, funguo binafsi lazima zizalishwe kwa nasibu. Matumizi ya jozi mpya ya funguo kwa kila shughuli huongeza usalama, ingawa inafanya kuwa ngumu kuzihifadhi na kuhifadhi siri kwa sehemu. Kwa muhtasari, usalama wa funguo binafsi ni kipaumbele cha juu, kinachohitaji uzalishaji wa kina na wa nasibu. HD wallets hutoa suluhisho la kuwezesha uzalishaji na usimamizi wa funguo wakati wa kudumisha kiwango cha juu cha usalama.

Walakini, kuzalisha nambari za nasibu kwenye kompyuta kunaweka changamoto kubwa, kwani matokeo yanayopatikana sio ya kweli kabisa. Ndiyo sababu ni muhimu kutumia Kizalishaji cha Nambari za Nasibu (RNG). Aina za RNG hutofautiana, kuanzia Kizalishaji cha Nambari za Nasibu za Pseudo (PRNG) hadi Kizalishaji cha Nambari za Nasibu za Kweli (TRNG), pamoja na PRNG ambazo zinaingiza chanzo cha entropy.

![image](assets/image/section3/3.JPG)

Katika kesi ya Bitcoin, funguo binafsi huzalishwa kutoka kwa kipande kimoja cha habari kwenye msingi wa mkoba. Habari hii inaruhusu uzalishaji wa nasibu na wa hiari wa jozi za funguo za watoto. Entropy ndio msingi wa mkoba wowote wa HD, ingawa hakuna kiwango cha kawaida cha kuzalisha nambari hii ya nasibu. Kwa hivyo, kuzalisha nambari za nasibu ni wasiwasi mkubwa kwa kuhakikisha usalama wa shughuli za Bitcoin.

Hatua ya ukaguzi ya uzalishaji wa funguo ni muhimu kuhakikisha usalama na uhalali wa uzalishaji wa nambari za nasibu, hatua muhimu katika kuzuia udhaifu wowote unaohusiana na uwezekano. Inapendekezwa sana kutumia mikoba ya chanzo wazi ili kuwezesha ukaguzi huu.

Walakini, ni muhimu kuzingatia kuwa baadhi ya mikoba ya vifaa inaweza kuwa "chanzo kilichofungwa," ikifanya iwe haiwezekani kuthibitisha uzalishaji wa nambari ya nasibu. Njia mbadala inaweza kuwa kuzalisha msemo wa kipekee kwa kutumia dadu, ingawa njia hii inaweza kuwa na hatari fulani.

![image](assets/image/section3/4.JPG)

Kutumia msemo wa kipekee uliozalishwa kwa nasibu kunaweza kusaidia kupunguza hatari hizi.

Mfano wa kutumia njia hii ni chaguo la "dice roll" linalotolewa na CoinKit kuzalisha msemo wa kipekee. Njia nyingine inaweza kuwa kutumia kipande kikubwa sana cha habari ya awali na kupunguza habari hii hadi bits 256 na kazi ya hash ya SHA-256, ambayo inaweza kuzalisha nambari nzuri ya nasibu. Ni muhimu kutaja kuwa kazi ya hash ya SHA-256 inapinga migongano, uongo, na mashambulizi ya pre-image na pre-image ya pili.

Mwishowe, nasibu inacheza jukumu muhimu katika kriptografia na sayansi ya kompyuta, na uwezo wa kuzalisha nasibu kwa usalama ni muhimu kuhakikisha usalama wa funguo binafsi na shughuli za Bitcoin. Entropy, ambayo iko katika moyo wa mkoba wa HD wa Bitcoin, ni muhimu kwa usalama wake. Katika somo letu lijalo, tutazidi kuchunguza mada hii, tukijadili jinsi entropy inachangia katika usalama wa mikoba ya HD.

## Msemo wa kipekee

![Msemo wa kipekee](https://youtu.be/uJERqH9Xp7I)

Usalama wa mkoba wa Bitcoin ni wasiwasi mkubwa kwa watumiaji wake wote. Njia muhimu ya kuhakikisha uhifadhi wa mkoba ni kuzalisha msemo wa kipekee kulingana na entropy na checksum.
Entropy ni msingi wa usalama wa mkoba wa HD. Kuna njia kadhaa za kuzalisha entropy hii, ikiwa ni pamoja na kupitia pseudo-random number generators (PRNGs), true random number generators (TRNGs), au kwa njia ya kawaida. Ni muhimu kwamba entropy hii iwe random au pseudo-random ili kuhakikisha usalama wa mkoba.

Kwa upande mwingine, checksum inahakikisha uthibitisho wa usahihi wa neno la kupona. Bila checksum hii, kosa katika neno hilo linaweza kusababisha uumbaji wa mkoba tofauti na hivyo kupoteza fedha. Checksum inapatikana kwa kupitisha entropy kupitia kazi ya SHA256 na kupata biti za kwanza 8 za hash.

Viwango tofauti vipo kwa neno la mnemoniki kulingana na ukubwa wa entropy. Kiwango kinachotumiwa zaidi kwa neno la kupona lenye maneno 24 ni entropy ya biti 256. Ukubwa wa checksum unategemea kugawanya ukubwa wa entropy na 32.

Kwa mfano, entropy ya biti 256 inazalisha checksum ya biti 8. Uunganishaji wa entropy na checksum kisha unaongoza kwa ukubwa wa mtawanyiko wa biti 128, biti 160, nk. Kulingana na ukubwa wa entropy, neno la kupona litajumuisha maneno 12 kwa biti 128, maneno 15 kwa biti 160, na maneno 24 kwa biti 256.

Kwa kubadilisha biti kuwa maneno, kila sehemu inahusishwa na neno kutoka kwenye orodha ya maneno 2048. Ni muhimu kutambua kwamba hakuna neno linaloagana na utaratibu wa herufi nne za kwanza.

Ni muhimu kuhifadhi neno la kupona lenye maneno 24 ili kuhifadhi uadilifu wa mkoba wa Bitcoin. Viwango viwili vinavyotumiwa zaidi vina msingi wa entropy ya biti 128 au 256 na unganisho la maneno 12 au 24. Kuongeza neno la siri ni chaguo la ziada kuimarisha usalama wa mkoba.

Kwa hitimisho, kuzalisha neno la mnemoniki ili kuhifadhi mkoba wa Bitcoin ni mchakato muhimu. Ni muhimu kuzingatia viwango vya neno la mnemoniki kulingana na ukubwa wa entropy. Kuhifadhi neno la kupona lenye maneno 24 ni muhimu ili kuzuia upotezaji wowote wa fedha. Asante kwa umakini wako na tunatarajia kozi yetu ya sarafu ya baadaye.

## Neno la siri

Neno la siri ni nenosiri la ziada ambalo linaweza kuunganishwa kwenye mkoba wa Bitcoin ili kuongeza usalama wake. Matumizi yake ni ya hiari na yako kwa uamuzi wa mtumiaji. Kwa kuongeza habari isiyo na maana ambayo, pamoja na neno la mnemoniki, inaruhusu kuhesabu mbegu ya mkoba, neno la siri linaimarisha usalama wake.

Kwa kuzalisha funguo za mkoba wa HD, neno la mnemoniki na neno la siri vyote ni muhimu. Neno la siri ni bure na linaweza kuwa na ukubwa karibu usio na kikomo. Halijumuishwi katika neno la mnemoniki, ambalo ni la kawaida na lazima lifuate vikwazo fulani vya ukubwa, checksum, na uandishi. Mshambuliaji hawezi kupata bitcoins za mtumiaji bila kujua neno la siri. Neno la siri linacheza jukumu katika ujenzi na kuhesabu funguo zote za mkoba.

Kazi ya pbkdf2 hutumiwa kuzalisha mbegu kutoka kwa neno la siri. Mbegu hii inaruhusu kuzalisha jozi zote za funguo za mtoto za mkoba. Ikiwa neno la siri linabadilishwa, mkoba wa Bitcoin unakuwa tofauti kabisa.
Neno la siri ni zana muhimu ya kuimarisha usalama wa mifuko ya Bitcoin. Inaweza kuwezesha matumizi ya mikakati mbalimbali ya usalama. Kwa mfano, inaweza kutumika kuunda nakala na kurahisisha kuhifadhiwa kwa neno la kumbukumbu. Pia inaweza kuimarisha usalama wa mifuko kwa kupunguza hatari zinazohusiana na uundaji wa nasibu wa neno la kumbukumbu.

Neno la siri linalofaa linapaswa kuwa refu (kutoka herufi 20 hadi 40) na lenye tofauti (kwa kutumia herufi kubwa, herufi ndogo, nambari, na alama). Halipaswi kuwa moja kwa moja kuhusiana na mtumiaji au mazingira yake. Ni salama zaidi kutumia mfuatano wa nasibu wa herufi badala ya neno rahisi kama neno la siri.

![image](assets/image/section3/9.JPG)

Neno la siri ni salama zaidi kuliko nenosiri rahisi. Neno la siri linalofaa ni refu, lenye tofauti, na nasibu. Inaweza kuimarisha usalama wa mifuko ya kuhifadhi au programu ya moto. Pia inaweza kutumika kuunda nakala rudufu na salama.

Ni muhimu kuchukua tahadhari katika kuhifadhi nakala za neno la siri ili kuepuka kupoteza ufikiaji wa mifuko ya kuhifadhi. Neno la siri ni chaguo kwa mifuko ya HD. Inaweza kuundwa nasibu kwa kutumia kete au kizazi kingine cha nambari nasibu. Haipendekezi kuhifadhi neno la siri au neno la kumbukumbu kwa kumbukumbu.

Katika somo letu lijalo, tutachunguza kwa undani jinsi mbegu na jozi ya kwanza ya funguo zinazozalishwa kutoka kwake zinafanya kazi. Jisikie huru kuendelea na somo hili ili kuendelea kujifunza. Tunatarajia kukutana nawe hivi karibuni.

# Uundaji wa Mifuko ya Bitcoin

## Uundaji wa mbegu na funguo kuu

![Uundaji wa mbegu na funguo kuu](https://youtu.be/56yAt_JDWhY)

Katika sehemu hii ya somo, tutachunguza hatua za kuzalisha Mfuko wa Hierarchical Deterministic (HD Wallet), ambao unaruhusu uundaji na usimamizi wa funguo za kibinafsi na za umma kwa njia ya hiyerariki.

![image](assets/image/section4/0.JPG)

Msingi wa HD Wallet unategemea vipengele viwili muhimu: neno la kumbukumbu na neno la siri (nenosiri la ziada lisilo la lazima). Pamoja, wanachangia mbegu, mfuatano wa herufi na nambari wa biti 512 ambao unatumika kama msingi wa kuzalisha funguo za mifuko ya Bitcoin. Kutoka kwenye mbegu hii, inawezekana kuzalisha jozi zote za funguo za mtoto za mifuko ya Bitcoin. Mbegu ndiyo ufunguo unaoruhusu ufikiaji wa bitcoins zote zinazohusiana na mfuko, iwe unatumia neno la siri au la.

Ili kupata mbegu, hutumiwa kazi ya pbkdf2 (Kazi ya Derivation ya Funguo kwa Msingi wa Nenosiri 2) na neno la kumbukumbu na neno la siri. Matokeo ya pbkdf2 ni mbegu ya biti 512. Funguo kuu cha kibinafsi na kificho cha mfuatano kuu hupatikana kwa kutumia algorithm ya HMAC SHA-512 (Nambari ya Uthibitishaji wa Ujumbe kwa Msingi wa Hash Salama 512). Algorithm hii inahitaji ujumbe na ufunguo ili kuzalisha matokeo. Funguo kuu cha kibinafsi kinahesabiwa kutoka kwenye mbegu na neno "Bitcoin SEED". Neno hili ni sawa kwa mifuko yote ya HD, ikidumisha umoja kati ya mifuko.

![image](assets/image/section4/1.JPG)

Awali, kazi ya SHA-512 haikuwa imeanzishwa katika itifaki ya Bitcoin, ndio maana HMAC SHA-512 hutumiwa. Matumizi ya HMAC SHA-512 na neno "Bitcoin SEED" yanamzuia mtumiaji kuunda mfuko maalum kwa Bitcoin. Matokeo ya HMAC SHA-512 ni nambari ya biti 512, iliyogawanywa katika sehemu mbili: biti 256 za kushoto zinaonyesha funguo kuu cha kibinafsi, wakati biti 256 za kulia zinaonyesha kificho cha mfuatano kuu.
Mfunguo wa siri wa msingi ni mfunguo wa mzazi wa funguo zote za baadaye kwenye mkoba, wakati nambari ya mnyororo wa msingi inahusika katika kuzalisha funguo za watoto. Ni muhimu kuelewa kwamba haiwezekani kuzalisha jozi ya funguo ya mtoto bila kujua nambari ya mnyororo inayohusiana na jozi ya mzazi. Nambari ya mnyororo inaongeza chanzo cha entropy kwenye mchakato wa kuzalisha funguo.

Jozi ya funguo kwenye mkoba inajumuisha funguo ya siri, funguo ya umma, na nambari ya mnyororo. Nambari ya mnyororo inaruhusu uingizaji wa upya katika kuzalisha funguo za watoto na kuisolate kila jozi ya funguo ili kuzuia uvujaji wa habari yoyote.

![image](assets/image/section4/2.JPG)

Ni muhimu kusisitiza kwamba funguo ya siri ya msingi ni funguo ya kwanza ya siri inayozalishwa kutoka kwa mbegu na haina uhusiano wowote na funguo zilizopanuliwa za mkoba. Kwa hivyo, mbegu ndio kipengele msingi cha kuzalisha funguo zote za mkoba. Inatofautiana na sentensi ya mnemoniki na nywila, ambazo hutumiwa kwa uumbaji wa mbegu.

Katika somo lifuatalo, tutachunguza kwa undani funguo zilizopanuliwa, kama vile xPub, xPRV, zPub, na kuelewa kwa nini hutumiwa na jinsi zinavyoundwa.

## Funguo Zilizopanuliwa

![Funguo Zilizopanuliwa](https://youtu.be/TRz760E_zUY)

Katika sehemu hii ya somo, tutajifunza kuhusu funguo zilizopanuliwa (xPub, zPub, yPub) na vikundi vyao, ambavyo vina jukumu muhimu katika kuzalisha funguo za watoto kwenye mkoba wa HD (Hierarchical Deterministic Wallet).

![image](assets/image/section4/3.JPG)

Funguo zilizopanuliwa zinatofautiana na funguo za msingi. Mkoba wa HD unazalisha sentensi ya mnemoniki na mbegu ili kupata funguo ya msingi na nambari ya mnyororo ya msingi. Funguo zilizopanuliwa hutumiwa kuzalisha funguo za watoto na zinahitaji funguo ya mzazi na nambari ya mnyororo inayohusiana. Funguo zilizopanuliwa huchanganya habari hizi mbili kuwezesha mchakato wa kuzalisha funguo.

Funguo zilizopanuliwa zinaonyeshwa na vikundi maalum (XPRV, XPUB, YPUB, ZPUB) ambavyo vinabainisha ikiwa ni funguo ya siri au ya umma iliyopanuliwa, pamoja na kusudi lake maalum. Metadata inayohusiana na funguo iliyopanuliwa inajumuisha toleo (kikundi), kina, alama ya kidole cha funguo ya umma, indeksi, na mzigo (nambari ya mnyororo na funguo ya mzazi).

![image](assets/image/section4/4.JPG)

Mzigo unajumuisha nambari ya mnyororo (baiti 32) na funguo ya mzazi (baiti 33). Vipengele hivi ni muhimu kwa kuzalisha funguo za watoto. Funguo ya siri inazalishwa kutoka nambari ya nasibu au nambari ya nasibu ya uwongo, wakati funguo ya umma inazalishwa kwa kutumia algorithm ya ECDSA (Elliptic Curve Digital Signature Algorithm).

Kila jozi ya funguo iliyopanuliwa inahusishwa na nambari ya mnyororo ya kipekee, ambayo inaruhusu derivations maalum. Kwa kuunganisha funguo ya mzazi na nambari ya mnyororo, funguo ya siri au ya umma iliyopanuliwa inapatikana.

![image](assets/image/section4/5.JPG)

Funguo za umma zilizopanuliwa zinaweza kuzalishwa tu kutoka kwa funguo za umma za watoto za kawaida, wakati funguo za siri zilizopanuliwa zinaweza kuzalishwa kutoka kwa funguo za umma na siri za watoto, iwe kupitia derivations za kawaida au zilizofungwa. Kutumia funguo zilizopanuliwa na kikundi cha XPUB kunaruhusu kuzalisha anwani mpya bila kurudi kwa funguo za siri zinazohusiana, hivyo kutoa usalama bora. Metadata inayohusiana na funguo zilizopanuliwa hutoa habari muhimu juu ya jukumu na nafasi yao katika muundo wa funguo.

Funguo za umma zilizopunguzwa zina ukubwa wa baiti 33, wakati funguo za umma zisizopunguzwa ni bits 512. Funguo zilizopanuliwa zina ukubwa wa baiti 82 na kikundi chake kinawakilishwa katika msingi 58 kupitia uongofu wa hexadecimal. Kukokotoa kisanduku kunafanywa kwa kutumia kazi ya HASH256 hash. 

![image](assets/image/section4/6.JPG)
Derivations imara huanza kutoka kwenye viashiria ambavyo ni nguvu za 2 (2^31). Ufunguo mpanuzi wa umma unaruhusu kudurusiwa kwa funguo za umma za watoto wa kawaida, wakati ufunguo mpanuzi wa binafsi unaruhusu kudurusiwa kwa funguo za watoto wowote. Ni muhimu kutambua kuwa vifungu vinavyotumiwa sana ni xpub na zpub, ambavyo vinahusiana na viwango vya zamani na segwit v1 na segwit v0 mtawaliwa.

Katika somo letu lijalo, tutachunguza kudurusiwa kwa jozi za funguo za watoto kwa kutumia maarifa yaliyopatikana kuhusu funguo mpanuzi na ufunguo mkuu wa mkoba.

Kwa hitimisho, funguo mpanuzi hucheza jukumu muhimu katika kriptografia na uendeshaji wa mikoba ya HD. Kuelewa matumizi yao na hesabu ni muhimu kuhakikisha usalama wa shughuli na ulinzi wa mali za dijiti. Vifungu na metadata vinavyohusiana na funguo mpanuzi huruhusu matumizi yenye ufanisi na kudurusiwa sahihi ya funguo za watoto muhimu.

## Kudurusiwa kwa Jozi za Funguo za Watoto

![Kudurusiwa kwa Jozi za Funguo za Watoto](https://youtu.be/FXhI-GmE9Aw)

Kwa kuongezea, tutajadili hesabu ya mbegu na ufunguo mkuu, ambao ni vipengele muhimu vya kwanza kwa shirika na kudurusiwa kwa mkoba wa HD (Hierarchical Deterministic Wallet). Mbegu, yenye urefu wa biti 128 hadi 256, inazalishwa kwa nasibu au kutoka kwa sentensi ya siri. Inacheza jukumu la kudurusiwa kwa funguo zingine zote. Ufunguo mkuu ni ufunguo wa kwanza uliodurusiwa kutoka kwa mbegu, na huruhusu kudurusiwa kwa jozi zingine za funguo za watoto.

Msimbo wa mnyororo mkuu unacheza jukumu muhimu katika kurejesha mkusanyiko kutoka kwa mbegu. Inapaswa kuzingatiwa kuwa funguo zote zilizodurusiwa kutoka kwa mbegu ile ile zitakuwa na msimbo wa mnyororo mkuu sawa.

![picha](assets/image/section4/7.JPG)

Mkoba wa ierarkia na wa kudurusiwa (HD wallet) hutoa usimamizi bora wa funguo na miundo ya mkoba. Funguo mpanuzi huruhusu kudurusiwa kwa jozi ya funguo za watoto kutoka kwa jozi ya funguo ya mzazi kwa kutumia hesabu za hisabati na algorithm maalum.

Kuna aina tofauti za jozi za funguo za watoto, ikiwa ni pamoja na funguo imara na funguo za kawaida. Ufunguo mpanuzi wa umma unaruhusu kudurusiwa kwa funguo za umma za watoto wa kawaida, wakati ufunguo mpanuzi wa binafsi unaruhusu kudurusiwa kwa funguo za watoto wote, za umma na za binafsi, iwe katika hali ya kawaida au imara. Kila jozi ya funguo ina kiashiria kinachowatofautisha.

![picha](assets/image/section4/8.JPG)

Kudurusiwa kwa funguo za watoto kunatumia kazi ya HMAC-SHA512 kwa kutumia ufunguo wa mzazi ulioongezwa na kiashiria na msimbo wa mnyororo unaoambatana na jozi ya funguo. Funguo za watoto wa kawaida zina kiashiria kinachotoka kati ya 0 hadi 2 kwa nguvu ya 31 minus 1, wakati funguo za watoto imara zina kiashiria kinachotoka kati ya 2 kwa nguvu ya 31 hadi 2 kwa nguvu ya 32 minus 1.

![picha](assets/image/section4/9.JPG)
![picha](assets/image/section4/10.JPG)

Kuna aina mbili za jozi za funguo za watoto: jozi imara na jozi za kawaida. Mchakato wa kudurusiwa kwa funguo za watoto hutumia funguo za umma kuzalisha hali za matumizi, wakati funguo za binafsi hutumika kwa ajili ya kusaini. Ufunguo mpanuzi wa umma unaruhusu kudurusiwa kwa funguo za umma za watoto wa kawaida, wakati ufunguo mpanuzi wa binafsi unaruhusu kudurusiwa kwa funguo za watoto wote, za umma na za binafsi, katika hali ya kawaida au imara.

![picha](assets/image/section4/11.JPG)
![picha](assets/image/section4/12.JPG)

Kudurusiwa kwa imara kunatumia ufunguo wa binafsi wa mzazi, wakati kudurusiwa kwa kawaida kunatumia ufunguo wa umma wa mzazi. Kazi ya HMAC-SHA512 hutumiwa kwa kudurusiwa kwa imara, wakati kudurusiwa kwa kawaida hutumia hash ya biti 512. Funguo wa umma wa watoto unapatikana kwa kuzidisha funguo wa binafsi wa watoto na jenereta ya mzunguko wa elliptic.

![picha](assets/image/section4/13.JPG)
Muundo wa Mfuko na Njia za Kupatikana

Katika sura hii, tutajifunza muundo wa mti wa kupatikana katika Mfuko wa Hierarchical Deterministic (HD Wallet). Tumeshajifunza kuhusu hesabu ya mbegu, ufunguo wa msingi, na upatikanaji wa jozi za ufunguo wa watoto. Sasa, tutazingatia utaratibu wa ufunguo ndani ya mfuko.

HD Wallet hutumia safu za kina kuweka ufunguo. Kila upatikanaji kutoka kwa jozi ya wazazi hadi jozi ya watoto unalingana na safu ya kina. Safu ya kina 0 inalingana na ufunguo wa msingi na nambari ya msingi ya mnyororo.

- Safu ya kina 1 hutumiwa kupata ufunguo wa watoto kwa kusudi maalum, ambalo linadhibitishwa na nambari ya utambulisho. Madhumuni haya yanalingana na viwango vya BIP 84 na Segwit v0/v1.

- Safu ya kina 2 inaruhusu tofauti ya akaunti kwa sarafu au mitandao tofauti. Hii inaruhusu kuweka mfuko kulingana na vyanzo tofauti vya fedha.

- Safu ya kina 3 hutumiwa kuweka mfuko katika akaunti tofauti, ikitoa muundo wazi na ulioandaliwa zaidi.

- Safu ya kina 4 inalingana na minyororo ya nje na ndani, ambayo hutumiwa kwa anwani zinazokusudiwa kutangazwa hadharani. Nambari 0 inahusishwa na mnyororo wa nje, wakati nambari 1 inahusishwa na mnyororo wa ndani. Kila akaunti ina minyororo miwili: mnyororo wa nje (0) na mnyororo wa ndani (1). Safu ya kina 4 pia hutumiwa kusimamia aina za skripti katika kesi ya mifuko ya saini nyingi.

- Safu ya kina 5 hutumiwa kwa anwani za kupokea katika mfuko wa kawaida. Katika sehemu inayofuata, tutachunguza upatikanaji wa jozi za ufunguo wa watoto kwa undani zaidi.

Kwa kila safu ya kina, tunatumia nambari za utambulisho kutofautisha jozi za ufunguo wa watoto. Nambari za utambulisho zilizohakikishwa hutumiwa na alama ya nukta kwa upatikanaji fulani. Ufunguo wa umma kwa mwaka hutumiwa kama kuingiza kwa kazi ya HMAC. Nambari ya utambulisho katika njia ya upatikanaji inaonyesha thamani inayotumiwa katika kazi ya HMAC.
Nambari bila alama ya nukta inalingana na nambari halisi iliyotumiwa, wakati nambari yenye alama ya nukta inalingana na nambari halisi + 2^31. Upatikanaji ulioimarishwa hutumia nambari kutoka 2^31 hadi 2^32-1. Kwa mfano, nambari 44' inalingana na nambari halisi 2^31 + 44.
Ili kuzalisha anwani ya kupokea maalum, tunapata jozi ya ufunguo wa watoto kutoka kwa ufunguo wa msingi na nambari ya msingi ya mnyororo. Kisha, tunatumia nambari ya utambulisho kutofautisha jozi tofauti za ufunguo wa watoto kwenye kina sawa.

Ufunguo uliopanuliwa, kama XPUB, inaruhusu kushiriki mfuko wako na watu wengine. Njia ya upatikanaji hutumiwa kutofautisha kati ya mnyororo wa nje (anwani zinazokusudiwa kutangazwa) na mnyororo wa ndani (anwani za kubadilisha).

Ni muhimu kutambua kuwa kina tofauti hutumiwa katika HD Wallet kulingana na viwango tofauti. Kupata ufunguo wa wazazi hadi ufunguo wa watoto kunaruhusu mpito kutoka kina kimoja hadi kingine. Matumizi ya matawi tofauti katika HD Wallet inaonyesha viwango tofauti vinavyofuatwa.

Katika sura inayofuata, tutajifunza anwani za kupokea, faida zao za matumizi, na hatua zinazohusika katika ujenzi wao.

# Ni anwani gani ya Bitcoin?

## Anwani za Bitcoin
Katika sura hii, tutachunguza anwani za kupokea, ambazo zina jukumu muhimu katika mfumo wa Bitcoin. Zinaruhusu kupokea fedha kwenye sarafu na hutengenezwa kutoka kwa jozi za funguo za kibinafsi na za umma. Ingawa kuna aina ya skripti inayoitwa Pay2PublicKey inayoruhusu kufunga bitcoins kwa funguo za umma, watumiaji kwa ujumla wanapendelea kutumia anwani za kupokea badala ya skripti hii.
![picha](assets/image/section5/0.JPG)

Wakati mpokeaji anataka kupokea bitcoins, hutoa anwani ya kupokea kwa mtumaji badala ya funguo zao za umma. Anwani ni hash ya funguo za umma, na ina muundo maalum. Funguo za umma zinapatikana kutoka kwa funguo za kibinafsi za watoto kwa kutumia operesheni za kihisabati kama vile kuongeza na kuzidisha kwenye mizunguko ya elliptic.

![picha](assets/image/section5/1.JPG)

Ni muhimu kutambua kwamba haiwezekani kubadilisha anwani kuwa funguo za umma, wala kutoka kwa funguo za umma kuwa funguo za kibinafsi. Kutumia anwani husaidia kupunguza ukubwa wa habari ya funguo za umma, ambayo kwa kawaida ni bits 512 mwanzoni. Inawezekana kubana funguo za umma kwa kubaki na thamani ya x na kuongeza kipengee cha awali, lakini mbinu hii haikuwa inajulikana wakati wa uumbaji wa Bitcoin. Kwa hivyo, kutumia anwani haipunguzi nafasi kwenye vitalu.

## Jinsi ya kuunda anwani ya Bitcoin?

![Jinsi ya kuunda anwani ya Bitcoin?](https://youtu.be/ewMGTN8dKjI)

Katika sura hii, tutajadili ujenzi wa anwani ya kupokea kwa shughuli za Bitcoin. Anwani ya kupokea ni uwakilishi wa alfanumeriki wa funguo za umma zilizopunguzwa. Ubadilishaji wa funguo za umma kuwa anwani ya kupokea hufuata hatua kadhaa.

![picha](assets/image/section5/3.JPG)

Moja ya sifa nzuri ya anwani za kupokea ni uwepo wa checksum, ambayo inaruhusu kugundua makosa. Kwa hili, tunatumia teknolojia ya checksum ya BCH (Bose-Chaudhuri-Hocquenghem), ambayo inahakikisha ugunduzi sahihi wa makosa. Teknolojia hii pia inachangia kupunguza idadi ya herufi zinazohitajika kuwakilisha anwani, ikifanya iwe rahisi kutumia.

Ili kuanza kujenga anwani, tunahitaji kupunguza ukubwa wa funguo za umma zinazolingana. Funguo za umma zisizosindika zinachukua bits 520, lakini kwa sababu ya usawa wa mzunguko wa elliptic unaotumiwa, mzunguko wa elliptic unaweza kuwa na kisanduku cha x kinachohusishwa na thamani mbili inayowezekana ya y: chanya au hasi. Kwenye mtandao wa Bitcoin, tunafanya kazi na seti ya kikomo cha nambari chanya badala ya seti ya nambari halisi. Ili kuwakilisha funguo za umma kutoka kwa x, tunaweka kipengee cha awali kinachoonyesha thamani ya y (hata au isiyo ya kawaida). Kupunguza ukubwa wa funguo za umma kunapunguza ukubwa wake kutoka bits 520 hadi 264. Upariti wa y katika seti ya kikomo cha nambari chanya unalingana na upariti wa y katika seti ya nambari halisi.

![picha](assets/image/section5/4.JPG)
![picha](assets/image/section5/5.JPG)

Tuchukue mfano wa funguo za umma zinazomilikiwa na Satoshi Nakamoto, na kipengee cha awali 0,3 kinachoonyesha thamani isiyo ya kawaida ya y. Kisha tunaweza kuendelea na hatua ya pili ya ujenzi wa anwani kutoka kwa funguo za umma zilizopunguzwa. Inawezekana kuhesabu anwani mbili kwa kila funguo za umma. Kufanya hivyo, tunatumia kazi ya SHA256 kupata hash ya funguo za umma. Kisha, tunatumia kazi ya ripemd160 kwa matokeo ya SHA256 kupata mfululizo wa herufi. Mfululizo huu kisha unakodishwa kwa muundo wa binary kwa vikundi vya bits 5, ambapo metadata inaongezwa kwa ajili ya kuhesabu checksum kwa kutumia programu ya BCH.
Katika kesi ya anwani za zamani, tunatumia kuhesabu mara mbili ya SHA256 ili kuzalisha kisanduku cha anwani. Walakini, kwa anwani za Segwit V0 na V1, tunategemea teknolojia ya BCH checksum ili kuhakikisha ugunduzi wa makosa. Programu ya BCH inaweza kupendekeza na kusahihisha makosa kwa uwezekano wa makosa ya chini sana. Kwa sasa, programu ya BCH inatumika kugundua na kupendekeza marekebisho, lakini haifanyi moja kwa moja kwa niaba ya mtumiaji. Hesabu ya kisanduku na nambari ya BCH inategemea hisabati ya polinomial ya Chien-Chauffage.

![image](assets/image/section5/7.JPG)

Programu ya BCH inahitaji habari kadhaa za kuingiza, ikiwa ni pamoja na HRP (Sehemu Inayoweza Kusomwa na Binadamu) ambayo inahitaji kupanuliwa. Upanuzi wa HRP unahusisha kuweka kila herufi kwa msingi wa 2, kuchukua bits tatu za kwanza za kila herufi kwa kuingiza kipengee cha 0, na kisha kuunganisha bits tano za mwisho za kila herufi. Herufi za bluu zilizobadilishwa kuwa msingi wa 10 zinaendana na 3 na 3 kwa mfumo wa decimal, wakati herufi tano za machungwa zinaendana na 2 na 3 kwa msingi wa 10. Upanuzi wa HRP katika msingi wa 10 unaruhusu kufunga bits tano za mwisho za kila herufi, hivyo kuimarisha kisanduku cha anwani.

![image](assets/image/section5/8.JPG)

Toleo la Segwit V0 linawakilishwa na nambari 00 na "payload" iko katika rangi nyeusi, katika msingi wa 10. Hii inafuatwa na herufi sita zilizohifadhiwa kwa ajili ya kisanduku cha anwani. Kuingiza metadata kunaambatishwa kwa programu ya BCH ili kupata kisanduku cha anwani katika msingi wa 10. Kuunganisha toleo, payload, na kisanduku cha anwani kunaruhusu kujenga anwani. Herufi za msingi wa 10 kisha zinabadilishwa kuwa herufi za bech32 kwa kutumia jedwali la ramani. Alfabeti ya bech32 inajumuisha herufi zote za alfanumeriki, isipokuwa 1, b, i, na o, ili kuepuka mkanganyiko.

![image](assets/image/section5/9.JPG)
![image](assets/image/section5/10.JPG)

Ili kujenga anwani inayoanza na bc1q, tunahitaji kutumia kazi ya hash (H160) kwa ufunguo wa umma uliopunguzwa, kisha kuongeza kisanduku cha anwani, toleo (q), HRP (bc), na kipengee cha kugawanya (1). Anwani za Taproot, kwa upande mwingine, zinaanza na bc1p kwa sababu toleo lao (Segwit V1) linalingana na 0+1=1, hivyo matumizi ya herufi p. Vitu vyote hivi basi vinabadilishwa kuwa BCH32, toleo la Bitcoin la msingi 32.

Hivyo, tumepitia hatua za kujenga anwani ya kupokea, matumizi ya teknolojia ya BCH checksum, pamoja na ujenzi wa anwani inayoanza na bc1q au bc1p kwa kutumia toleo la BCH32 la msingi 32 maalum kwa Bitcoin.

## Muhtasari wa Kriptografia kwa Mifuko ya Bitcoin

![muhtasari wa mafunzo](https://youtu.be/NkAYoVUMvOs)

Katika mafunzo haya, tumesoma kwa kina mkoba wa Hierarchical Deterministic (HD) na BIP32. Entropia inacheza jukumu muhimu katika aina hii ya mkoba, kwani inatumika kuzalisha sentensi ya mnemoniki kutoka nambari ya nasibu. Kwa orodha ya maneno 2048 zinazotolewa katika BIP39, sentensi ya mnemoniki inaweza kuwekwa katika mfululizo wa maneno rahisi kukumbuka. Sentensi ya mnemoniki, pamoja na neno la siri hiari, ni muhimu kuzalisha mbegu ya mkoba. Neno la siri linafanya kazi kama chumvi ya kriptografia ambayo inaongeza safu ya ziada ya ulinzi kwa mkoba.

![image](assets/image/section5/11.JPG)
Kazi kuu ya mkalimani mtaalamu mwenye ujuzi ni kutafsiri kwa usahihi maudhui ya kiufundi kutoka kwenye lugha ya asili, English, kwenda kwenye lugha ya Swahili. Ni muhimu kufuata mwongozo ufuatao ili kuhakikisha tafsiri yenye ubora wa hali ya juu:

Lugha ya Asili: Maudhui yameandikwa kwa lugha ya asili ya English.
Aina ya Maudhui: Utakutana na vifaa vya kiufundi, ikiwa ni pamoja na istilahi maalum ya tasnia.
Viungo na Maneno ya Kiufundi: Usitafsiri URL au maneno ya kiufundi yanayohusiana sana. Ikiwa haujiamini, weka neno la asili.
Uwiano wa Muundo: Endeleza muundo na muundo wa markdown sawa na maandishi ya asili. Uwiano wa muundo ni muhimu.
Mali za YML: Ikiwa mstari unaanza na mali ya YML (kwa mfano, 'jina:', 'lengo:', 'malengo:'), weka jina la mali kwa Kiingereza.
Mazingira ya Utamaduni: Kwa marejeo ya kitamaduni au yanayohusiana na muktadha ambayo hayawezi kutafsiri moja kwa moja, tafsiri kwa maneno mengine ili kuhifadhi maana iliyokusudiwa au toa maelezo mafupi.
Umuhimu unapaswa kuwekwa katika kudumisha uadilifu wa maudhui ya kiufundi wakati kuhakikisha tafsiri inaeleweka na inalingana na muktadha kwa lugha ya Swahili. Hii ni maandishi ya kutafsiri:

Kazi kuu ya kazi ya pbkdf2 ni kuzalisha mbegu kutoka kwa msemo wa mnemoniki na nywila, kwa kutumia hmacha512 na mizunguko 2048. Muhuri mkuu na msimbo wa mnyororo wa mkuu kisha hupatikana kutoka kwa mbegu hii kwa kutumia tena kazi ya hmacha512 na msemo "mbegu ya bitcoin". Muhuri wa kibinafsi wa mkuu na msimbo wa mnyororo wa mkuu ndio vipengele vya juu kabisa katika muundo wa mkoba wa HD.
![image](assets/image/section5/12.JPG)

Kuongezeka kwa ufunguo wa mtoto kunategemea mambo kadhaa, ikiwa ni pamoja na ufunguo wa mzazi na msimbo wa mnyororo unaofanana. Ufunguo uliopanuliwa unapatikana kwa kuunganisha ufunguo wa mzazi na msimbo wake wa mnyororo, wakati ufunguo wa mkuu ni ufunguo tofauti. Ili kupata anwani, ufunguo wa umma uliopunguzwa kwanza hufanyiwa hash kwa kutumia SHA256 na RIPMD160, na kisha checksum hupimwa. Kuhesabu checksum kunatumia hash ya Double SHA256 katika kesi ya kiwango cha zamani, wakati programu ya BCH (Bose-Chaudhuri-Hocquenghem) inatumika kuhesabu checksum katika kesi ya kiwango cha segwit. Kisha, uwakilishi wa muundo wa msingi 58 hutumiwa kwa kiwango cha zamani, wakati muundo wa bech32 hutumiwa kwa kiwango cha segwit, ili kupata anwani ya mkoba wa HD.

![image](assets/image/section5/13.JPG)

Kwa muhtasari, tumegundua kwa undani kazi za hash na sifa zao, pamoja na saini za dijiti na mizunguko ya elliptic. Kisha tukaingia katika ulimwengu wa mkoba wa Hierarchical Deterministic (HD) na BIP32, tukitumia entropy na msemo wa siri kuzalisha mbegu ya mkoba. Pia tumejifunza jinsi ya kupata ufunguo wa mtoto na kupata anwani ya mkoba wa HD. Natumai habari hii imekuwa na manufaa kwako, na sasa nakuhimiza uendelee na tathmini ili kupima maarifa yako uliyopata wakati wa kozi ya Crypto 301. Asante kwa umakini wako.

# Endelea zaidi

## Kuunda mbegu kutoka kwa kurusha 128 za kete!

![Kuunda mbegu kutoka kwa kurusha 128 za kete!](https://youtu.be/lUw-1kk75Ok)

Uundaji wa msemo wa mnemoniki ni hatua muhimu katika kuhakikisha usalama wa mkusanyiko wako wa sarafu za sarafu. Kuna njia kadhaa za kuzalisha msemo wa mnemoniki, hata hivyo, tutazingatia njia ya uundaji wa mwongozo kwa kutumia kete. Ni muhimu kuzingatia kuwa njia hii haifai kwa mkoba wenye thamani kubwa. Inapendekezwa kutumia programu ya chanzo wazi au mkoba wa vifaa ili kuzalisha msemo wa mnemoniki. Ili kuunda msemo wa mnemoniki, tutatumia kete kuunda habari ya binary. Lengo ni kuelewa mchakato wa kuunda msemo wa mnemoniki.

**Hatua ya 1 - Maandalizi:**
Hakikisha una usambazaji wa Linux wa amnesic, kama vile Tails OS, uliofungwa kwenye kifaa cha USB kwa usalama zaidi. Tafadhali kumbuka kuwa mafunzo haya hayapaswi kutumika kuunda mkoba wa msingi.

**Hatua ya 2 - Kuzalisha nambari ya binary ya nasibu:**
Tutatumia kete kuunda habari ya binary. Ruka kete 128 na andika matokeo ya kila kurusha (1 kwa nambari isiyo na mpangilio, 0 kwa nambari ya mpangilio).

**Hatua ya 3 - Kupanga nambari za binary:**
Panga nambari za binary zilizopatikana katika safu za nambari 11 ili kurahisisha hesabu zaidi. Safu ya kumi na mbili inapaswa kuwa na nambari 7 tu.

**Hatua ya 4 - Kuhesabu checksum:**
Wakati wa safu ya kumi na mbili, tarakimu nne za mwisho zinahusiana na checksum. Ili kuhesabu checksum hii, tunahitaji kutumia terminal kutoka kwenye usambazaji wa Linux. Inapendekezwa kutumia [TailOs](https://tails.boum.org/index.fr.html), ambayo ni usambazaji usio na kumbukumbu unaozinduka kutoka kwenye kifaa cha USB. Mara baada ya kuwa kwenye terminal yako, ingiza amri `echo <binary number> | shasum -a 254 -0`. Badilisha `<binary number>` na orodha yako ya sifuri na moja mia ishirini na nane. Matokeo ni hash ya hexadecimali. Chukua tahadhari ya herufi ya kwanza ya hash hii na ibadilishe kuwa binary. Unaweza kutumia [meza hii](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) kwa msaada. Ongeza checksum ya binary (tarakimu nne) kwenye safu ya kumi na mbili ya karatasi yako.
**Hatua ya 5 - Kubadilisha kuwa decimali:**
Ili kupata maneno yanayohusiana na kila safu yako, kwanza unahitaji kubadilisha kila mfululizo wa bits 11 kuwa decimali. Hapa huwezi kutumia kigeuzi cha mtandaoni kwa sababu hizi bits zinawakilisha sentensi yako ya mnemoniki. Kwa hivyo utahitaji kubadilisha kwa kutumia kikokotoo na mbinu ifuatayo: kila bit inahusishwa na nguvu ya 2, kwa hivyo kutoka kushoto kwenda kulia tuna safu 11 zinazolingana na 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. Ili kubadilisha mfululizo wako wa bits 11 kuwa decimali, unahitaji tu kuongeza safu ambazo zina 1. Kwa mfano, kwa mfululizo 00110111011, hii inalingana na jumla ifuatayo: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Sasa unaweza kubadilisha kila safu kuwa decimali. Na kabla ya kuendelea na uandikishaji kwa maneno, unahitaji kuongeza +1 kwa safu zote kwa sababu indeksi ya orodha ya maneno ya BIP39 inaanza kutoka 1 na sio 0.

**Hatua ya 8 - Uzalishaji wa sentensi ya mnemoniki:**
Anza kwa kuchapisha [orodha ya maneno 2048](https://seedxor.com/files/wordlist.pdf) ili kubadilisha kati ya nambari zako za decimali na maneno ya BIP39. Kipekee ya orodha hii ni kwamba hakuna neno linaloshiriki herufi nne za kwanza sawa na maneno mengine yote katika kamusi hii. Kisha, kwa kila safu yako, tafuta neno linalohusiana na nambari ya decimali.

**Hatua ya 9 - Jaribio la sentensi ya mnemoniki:**
Jaribu mara moja sentensi yako ya mnemoniki kwenye Sparrow Wallet kwa kuiunda mkoba kutoka kwake. Ikiwa unapata kosa la checksum batili, ni uwezekano mkubwa kuwa umefanya kosa la kuhesabu. Sawa kosa hili kwa kurudi kwenye hatua ya 4 na jaribu tena kwenye Sparrow Wallet. Hiyo ndiyo! Umeunda mkoba mpya wa Bitcoin kutoka kwa kurusha kete 128.

Kuzalisha sentensi ya mnemoniki ni mchakato muhimu kwa kusimamia mkoba wako wa sarafu ya sarafu. Inapendekezwa kutumia njia salama zaidi, kama matumizi ya programu ya chanzo wazi au mkoba wa vifaa, kuzalisha sentensi ya mnemoniki. Walakini, kukamilisha warsha hii husaidia kuelewa vizuri jinsi tunaweza kuunda mkoba wa Bitcoin kutoka kwa nambari ya nasibu.

## Hitimisho na mwisho

### Shukrani na endelea kuchimba shimo la sungura

Tungependa kukushukuru kwa kuhudhuria mafunzo ya Crypto 301. Tunatumai kuwa uzoefu huu umekuwa wa kuelimisha na wa kujenga kwako. Tumeshughulikia mada nyingi za kusisimua, kuanzia hisabati hadi kriptografia hadi jinsi itifaki ya Bitcoin inavyofanya kazi.
Ikiwa unataka kuchunguza zaidi juu ya somo hili, tunayo rasilimali ya ziada ya kukupa. Tumefanya mahojiano maalum na Théo Pantamis na Loïc Morel, wataalamu mashuhuri katika uga wa kriptografia. Mahojiano haya yanachunguza kwa kina sehemu mbalimbali za somo na yanatoa mitazamo ya kuvutia.

Jisikie huru kuangalia mahojiano haya ili kuendelea kuchunguza uga wa kusisimua wa kriptografia. Tunatumaini kuwa itakuwa na manufaa na yenye kuvutia katika safari yako. Tena, asante kwa ushiriki wako na jitihada zako katika mafunzo haya.

### Tufadhili

Kozi hii, pamoja na yaliyomo yote yanayopatikana kwenye chuo kikuu hiki, imetolewa kwako bure na jamii yetu. Ili kutusaidia, unaweza kushiriki na wengine, kuwa mwanachama wa chuo kikuu, na hata kuchangia katika maendeleo yake kupitia GitHub. Kwa niaba ya timu nzima, asante sana!

### Pima Mafunzo

Mfumo wa upimaji wa mafunzo utaunganishwa hivi karibuni katika jukwaa hili jipya la kujifunza mtandaoni! Kwa sasa, asante sana kwa kuchukua kozi, na ikiwa ulifurahia, tafadhali fikiria kushiriki na wengine.
