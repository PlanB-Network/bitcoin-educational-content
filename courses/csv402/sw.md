---
name: Itifaki ya RGB, kutoka kwa nadharia hadi mazoezi
goal: Pata ujuzi unaohitajika kuelewa na kutumia RGB
objectives: 

  - Kuelewa dhana za kimsingi za itifaki ya RGB
  - Bidii kanuni za ahadi za Client-side Validation na Bitcoin
  - Jifunze jinsi ya kuunda, kudhibiti na kuhamisha mikataba ya RGB
  - Jinsi ya kuendesha nodi ya Umeme inayoendana na RGB

---
# Kugundua itifaki ya RGB

Ingia katika ulimwengu wa RGB, itifaki iliyoundwa kutekeleza na kutekeleza haki za kidijitali, katika mfumo wa mikataba na mali, kwa kuzingatia sheria za makubaliano na uendeshaji wa Bitcoin Blockchain. Kozi hii ya kina ya mafunzo hukuongoza kupitia misingi ya kiufundi na kiutendaji ya RGB, kuanzia dhana za "Client-side Validation" na "Mihuri ya Matumizi Moja", hadi utekelezaji wa mikataba mahiri ya hali ya juu.

Kupitia mpango ulioundwa, hatua kwa hatua, utagundua mbinu za Client-side Validation, ahadi bainifu kwenye Bitcoin na mifumo ya mwingiliano kati ya watumiaji. Jifunze jinsi ya kuunda, kudhibiti na kuhamisha tokeni za RGB kwenye Bitcoin au Lightning Network.

Iwe wewe ni msanidi programu, mpenda Bitcoin, au una hamu ya kujua zaidi kuhusu teknolojia hii, kozi hii ya mafunzo itakupa zana na maarifa unayohitaji ili kufahamu RGB na kuunda suluhu bunifu kwenye Bitcoin.

Kozi hiyo inatokana na semina ya moja kwa moja iliyoandaliwa na Fulgur'Ventures na kufundishwa na walimu watatu mashuhuri na wataalam wa RGB.

+++
# Utangulizi

<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>

## Uwasilishaji wa kozi

<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>

Hamjambo nyote, na karibu kwenye kozi hii ya mafunzo inayotolewa kwa RGB, mfumo wa Smart contract ulioidhinishwa kwa upande wa mteja unaotumia Bitcoin na Lightning Network. Muundo wa kozi hii umeundwa ili kuwezesha uchunguzi wa kina wa somo hili changamano. Hivi ndivyo kozi inavyopangwa:

**Sehemu ya 1: Nadharia

Sehemu ya kwanza imejitolea kwa dhana za kinadharia zinazohitajika ili kuelewa misingi ya Client-side Validation na RGB. Kama utakavyogundua katika kozi hii, RGB inatanguliza dhana nyingi za kiufundi ambazo hazionekani kwa kawaida katika Bitcoin. Katika sehemu hii, utapata pia faharasa inayotoa ufafanuzi wa maneno yote mahususi kwa itifaki ya RGB.

**Sehemu ya 2: Fanya mazoezi

Sehemu ya pili itazingatia matumizi ya dhana za kinadharia zinazoonekana katika sehemu ya 1. Tutajifunza jinsi ya kuunda na kuendesha kandarasi za RGB. Pia tutaona jinsi ya kupanga na zana hizi. Sehemu hizi mbili za kwanza zinawasilishwa na Maxim Orlovsky.

**Sehemu ya 3: Maombi

Sehemu ya mwisho inaongozwa na wazungumzaji wengine wanaowasilisha maombi madhubuti yenye msingi wa RGB, ili kuangazia matukio ya matumizi halisi.

---
Awali kozi hii ya mafunzo ilikua nje ya kambi ya mafunzo ya hali ya juu ya wiki mbili huko Viareggio, Toscany, iliyoandaliwa na [Fulgur'Ventures](https://fulgur.ventures/). Wiki ya kwanza, inayolenga Rust na SDK, inaweza kupatikana katika kozi hii nyingine:

https://planb.network/courses/9fbd8b57-f278-4304-8d88-a2d384eaff58
Katika kozi hii, tunazingatia wiki ya pili ya bootcamp, ambayo inalenga RGB.

**Wiki ya 1 - LNP402:**

![RGB-Bitcoin](assets/fr/001.webp)

**Wiki ya 2 - Mafunzo ya sasa CSV402:**

![RGB-Bitcoin](assets/fr/002.webp)

Shukrani nyingi kwa waandaaji wa kozi hizi za moja kwa moja na kwa walimu 3 walioshiriki:


- Maxim Orlovsky: *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, AI, robotiki, transhumanism. Waundaji wa RGB, Prime, Radiant na lnp_bp, mycitadel_io & cyphernet_io* ;
- Hunter Trujilo: *Developer, Rust, Bitcoin, Lightning, RGB* ;
- Federico Tenga: *Ninafanya bidii yangu kugeuza ulimwengu kuwa ugonjwa wa Cypherpunk. Hivi sasa inafanya kazi kwenye RGB huko Bitfinex*.

Toleo lililoandikwa la kozi hii ya mafunzo liliandaliwa kwa kutumia nyenzo kuu 2:


- Video za Maxim Orlovsky, Hunter Trujilo na semina ya Frederico Tenga katika Lightning Bootcamp;
- Hati za RGB, ambazo utayarishaji wake ulifadhiliwa na [Bitfinex](https://www.bitfinex.com/).

# RGB kwa nadharia

<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## Utangulizi wa dhana za kompyuta zilizosambazwa

<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

:::video id=f27338bc-4210-4a2e-9b27-30278ed3282c:::

RGB ni itifaki iliyoundwa ili kutumia na kutekeleza haki za kidijitali (katika mfumo wa mikataba na mali) kwa njia ya hatari na ya siri, kwa kuzingatia sheria za makubaliano na uendeshaji wa Bitcoin Blockchain. Lengo la sura hii ya kwanza ni kuwasilisha dhana za kimsingi na istilahi zinazozunguka itifaki ya RGB, ikiangazia hasa viungo vyake vya karibu na dhana za msingi za kompyuta zilizosambazwa kama vile Client-side Validation na Mihuri ya Matumizi Moja.

Katika sura hii, tunachunguza misingi ya **mifumo ya makubaliano iliyosambazwa** na kuona jinsi RGB inavyofaa katika familia hii ya teknolojia. Pia tutakuletea kanuni kuu zinazotusaidia kuelewa ni kwa nini RGB inalenga kupanuka na kutotegemea utaratibu wa maafikiano wa Bitcoin, huku tukiitegemea inapohitajika.

### Utangulizi

Kompyuta iliyosambazwa, tawi maalum la sayansi ya kompyuta, husoma itifaki zinazotumiwa kusambaza na kuchakata habari kwenye mtandao wa nodi. Kwa pamoja, nodi hizi na sheria za itifaki zinaunda kile kinachojulikana kama mfumo uliosambazwa. Miongoni mwa sifa muhimu za mfumo kama huu ni:


- **uwezo wa uthibitishaji huru na uthibitishaji** wa data fulani kwa kila nodi;
- Uwezekano wa nodes kujenga (kulingana na itifaki) mtazamo kamili au sehemu ya habari. Maoni haya ni **majimbo** ya mfumo uliosambazwa;
- **Mpangilio wa matukio** wa utendakazi, ili data iwekwe muhuri wa wakati kwa uhakika na kuwe na makubaliano juu ya mlolongo wa matukio (mfuatano wa majimbo).

Hasa, dhana ya **makubaliano** katika mfumo uliosambazwa inashughulikia vipengele viwili:


- Utambuzi wa uhalali ** wa mabadiliko ya hali (kulingana na sheria za itifaki);
- **makubaliano juu ya mpangilio** wa mabadiliko haya ya hali, ambayo hufanya kuwa haiwezekani kuandika upya au kutengua shughuli zilizothibitishwa nyuma (hii pia inajulikana katika Bitcoin kama "ulinzi wa matumizi mara mbili").

Utekelezaji wa kwanza unaofanya kazi, usio na ruhusa wa utaratibu wa makubaliano uliosambazwa ulianzishwa na Satoshi Nakamoto na Bitcoin, kutokana na matumizi ya pamoja ya muundo wa data wa Blockchain na algoriti ya Proof-of-Work (PoW). Katika mfumo huu, uaminifu wa historia ya kuzuia inategemea nguvu ya kompyuta iliyotolewa na nodes (wachimbaji). Kwa hivyo Bitcoin ni mfano mkuu na wa kihistoria wa mfumo wa makubaliano uliosambazwa wazi kwa wote (*bila ruhusa*).

Katika ulimwengu wa Blockchain na kompyuta iliyosambazwa, tunaweza kutofautisha dhana mbili za msingi: ***Blockchain*** kwa maana ya jadi, na *** njia za serikali ***, mfano bora ambao katika uzalishaji ni Lightning Network. Blockchain inafafanuliwa kama rejista ya matukio yaliyopangwa kwa mpangilio, yanayoigwa kwa maafikiano ndani ya mtandao wazi, usio na ruhusa. Njia za serikali, kwa upande mwingine, ni njia za rika-kwa-rika zinazowezesha washiriki wawili (au zaidi) kudumisha hali iliyosasishwa ya off-chain, kwa kutumia Blockchain pekee wakati wa kufungua na kufunga njia hizi.

Katika muktadha wa Bitcoin, bila shaka unafahamu kanuni za Mining, ugatuaji na ukamilifu wa miamala kwenye Blockchain, pamoja na jinsi njia za malipo zinavyofanya kazi. Kwa RGB, tunatanguliza dhana mpya iitwayo **Client-side Validation**, ambayo, tofauti na Blockchain au Umeme, inajumuisha uhifadhi wa ndani (upande wa mteja) na uthibitishaji wa mabadiliko ya hali ya Smart contract. Hii pia inatofautiana na mbinu nyingine za "DeFi" (_rollups_, _plasma_, _ARK_, nk.), kwa kuwa Client-side Validation inategemea Blockchain ili kuzuia Double-spending na kuwa na mfumo wa kuweka wakati, wakati wa kuweka rejista ya majimbo ya off-chain na mabadiliko, tu na washiriki wanaohusika.

![RGB-Bitcoin](assets/fr/003.webp)

Baadaye, pia tutaanzisha neno muhimu: dhana ya "**Stash**", ambayo inarejelea seti ya data ya upande wa mteja inayohitajika ili kuhifadhi hali ya Contract, kwa kuwa data hii haiigizwi kimataifa kote kwenye mtandao. Hatimaye, tutaangalia mantiki nyuma ya RGB, itifaki ambayo inachukua faida ya Client-side Validation, na kwa nini inakamilisha mbinu zilizopo (Blockchain na njia za serikali).

### Trilemmas katika kompyuta iliyosambazwa

Ili kuelewa jinsi matatizo ya Client-side Validation na RGB Address hayajatatuliwa na Blockchain na Umeme, hebu tugundue "trilemmas" 3 kuu katika kompyuta iliyosambazwa:


- Scalability, Ugatuaji, Faragha** ;
- CAP** Nadharia (Uthabiti, Upatikanaji, Uvumilivu wa Sehemu);
- CIA** trilemma (Usiri, Uadilifu, Upatikanaji).

#### 1. Scalability, ugatuaji na usiri


- Blockchain (Bitcoin)**

Blockchain ina ugatuzi wa hali ya juu, lakini sio hatari sana. Zaidi ya hayo, kwa kuwa kila kitu kiko katika rejista ya kimataifa, ya umma, usiri ni mdogo. Tunaweza kujaribu kuboresha usiri kwa kutumia teknolojia zisizo na maarifa (Confidential Transactions, mifumo ya mimblewimble, n.k.), lakini msururu wa umma hauwezi kuficha grafu ya muamala.


- Njia za umeme/Jimbo**

Njia za serikali (kama ilivyo kwa Lightning Network) ni hatari zaidi na ni za faragha zaidi kuliko Blockchain, kwani shughuli zinafanyika off-chain. Hata hivyo, wajibu wa kutangaza hadharani baadhi ya Elements (miamala ya ufadhili, topolojia ya mtandao) na ufuatiliaji wa trafiki ya mtandao inaweza kwa kiasi fulani kuhatarisha usiri. Ugatuaji pia unateseka: uelekezaji unatumia pesa nyingi, na nodi kuu zinaweza kuwa sehemu kuu za uwekaji. Hili ndilo jambo ambalo tunaanza kuona kwenye Umeme.


- Client-side Validation (RGB)**

Mtazamo huu mpya ni hatari zaidi na wa siri zaidi, kwa sababu sio tu kwamba tunaweza kuunganisha mbinu za uthibitisho wa maarifa bila ufichuzi, lakini hakuna grafu ya kimataifa ya miamala, kwa kuwa hakuna mtu anayeshikilia rejista nzima. Kwa upande mwingine, pia inamaanisha maelewano fulani juu ya ugatuaji wa madaraka: mtoaji wa Smart contract anaweza kuwa na jukumu kuu (kama "msambazaji wa Contract" huko Ethereum). Hata hivyo, tofauti na Blockchain, iliyo na Client-side Validation, unahifadhi na kuthibitisha kandarasi ambazo unazipenda pekee, jambo ambalo huboresha uwezo wako kwa kuepuka hitaji la kupakua na kuthibitisha majimbo yote yaliyopo.

![RGB-Bitcoin](assets/fr/004.webp)

#### 2. Nadharia ya CAP (Uthabiti, Upatikanaji, Uvumilivu wa Sehemu)

Nadharia ya CAP inasisitiza kuwa haiwezekani kwa mfumo uliosambazwa kukidhi uthabiti kwa wakati mmoja (*Uthabiti*), upatikanaji (*Upatikanaji*) na ustahimilivu wa kizigeu (*Uvumilivu wa kizigeu*).


- Blockchain**

Blockchain inapendelea uthabiti na upatikanaji, lakini haifanyi vizuri na ugawaji wa mtandao: ikiwa huwezi kuona kizuizi, huwezi kuchukua hatua na kuwa na mtazamo sawa na mtandao mzima.


- Umeme** (kwa Kifaransa)

Mfumo wa chaneli za serikali una upatikanaji na uvumilivu wa kugawa (kwa kuwa nodi mbili zinaweza kubaki zimeunganishwa kwa kila mmoja hata ikiwa mtandao umegawanyika), lakini uthabiti wa jumla unategemea ufunguzi na kufungwa kwa njia kwenye Blockchain.


- Client-side Validation (RGB)**

Mfumo kama vile RGB unatoa uthabiti (kila mshiriki anathibitisha data yake ndani ya nchi, bila utata) na ustahimilivu wa kugawa (unaweka data yako kivyake), lakini haihakikishii upatikanaji wa kimataifa (kila mtu anapaswa kuhakikisha kuwa ana sehemu zinazofaa za historia, na baadhi ya washiriki wanaweza wasichapishe chochote au kuacha kushiriki taarifa fulani).

![RGB-Bitcoin](assets/fr/005.webp)

#### 3. CIA trilemma (Usiri, Uadilifu, Upatikanaji)

Utatu huu unatukumbusha kuwa usiri, uadilifu na upatikanaji haviwezi kuboreshwa vyote kwa wakati mmoja. Blockchain, Umeme na Client-side Validation huanguka tofauti katika usawa huu. Wazo ni kwamba hakuna mfumo mmoja unaweza kutoa kila kitu; ni muhimu kuchanganya mbinu kadhaa (Blockchain's-muhuri, mbinu ya upatanishi ya Umeme, na uthibitishaji wa ndani na RGB) ili kupata kifurushi madhubuti kinachotoa dhamana nzuri katika kila mwelekeo.

![RGB-Bitcoin](assets/fr/006.webp)

### Jukumu la Blockchain na wazo la kugawanyika

Blockchain (katika kesi hii, Bitcoin) hutumika kama utaratibu wa _wakati wa kuweka muhuri_ na ulinzi dhidi ya matumizi maradufu. Badala ya kuingiza data kamili ya Smart contract au mfumo uliogatuliwa, tunajumuisha tu **ahadi za kriptografia** (_commitments_) kwa miamala (kwa maana ya Client-side Validation, ambayo tutaita "mipito ya serikali"). Hivyo:


- Tunatoa Blockchain kutoka kwa kiasi kikubwa cha data na mantiki;
- Kila mtumiaji huhifadhi tu historia inayohitajika kwa sehemu yake mwenyewe ya Contract ("*Shard** yake"), badala ya kuiga Global State.

Sharding ni dhana iliyotokana na hifadhidata zilizosambazwa (k.m. MySQL kwa mitandao ya kijamii kama vile Facebook au Twitter). Ili kutatua tatizo la kiasi cha data na ucheleweshaji wa maingiliano, hifadhidata imegawanywa katika _shards_ (Marekani, Ulaya, Asia, n.k.). Kila sehemu inalingana ndani ya nchi na imesawazishwa kwa sehemu na zingine.

Kwa mikataba mahiri ya aina ya RGB, sisi Shard kulingana na mikataba yenyewe. Kila Contract ni _shard_ inayojitegemea. Kwa mfano, ikiwa una tokeni za USDT pekee, huhitaji kuhifadhi au kuthibitisha historia nzima ya tokeni nyingine kama USDC. Kwenye Bitcoin, Blockchain haifanyi _sharding_: una seti ya kimataifa ya UTXO. Kwa Client-side Validation, kila mshiriki anahifadhi tu data ya Contract ambayo inashikilia au kutumia.

Kwa hivyo tunaweza kufikiria mfumo ikolojia kama ifuatavyo:


- Blockchain (Bitcoin)** kama msingi unaohakikisha urudufu kamili wa rejista ndogo na hutumika kama muhuri wa muda wa Layer;
- Lightning Network** kwa haraka, Confidential Transactions, bado kulingana na usalama na makazi ya mwisho ya Bitcoin Blockchain;
- RGB na Client-side Validation** ili kuongeza mantiki changamano zaidi ya Smart contract, bila kuunganisha Blockchain au kupoteza usiri.

![RGB-Bitcoin](assets/fr/007.webp)

Hizi tatu za Elements huunda nzima ya triangular, badala ya safu ya mstari wa "Layer 2", "Layer 3" na kadhalika. Umeme unaweza kuunganisha moja kwa moja kwenye Bitcoin, au kuhusishwa na miamala ya Bitcoin inayojumuisha data ya RGB. Vile vile, matumizi ya "BiFi" (fedha kwenye Bitcoin) yanaweza kujumuisha na Blockchain, pamoja na Umeme na RGB kulingana na mahitaji ya usiri, scalability au mantiki ya Contract.

![RGB-Bitcoin](assets/fr/008.webp)

### Wazo la mabadiliko ya serikali

Katika mfumo wowote uliosambazwa, lengo la utaratibu wa uthibitishaji ni kuweza **kubainisha uhalali na mpangilio wa mpangilio wa mabadiliko ya hali**. Lengo ni kuthibitisha kwamba sheria za itifaki zimeheshimiwa, na kuthibitisha kwamba mabadiliko haya ya serikali yanafuatana kwa utaratibu dhahiri, usioweza kupingwa.

Ili kuelewa jinsi uthibitisho huu unavyofanya kazi katika muktadha wa **Bitcoin** na, kwa ujumla zaidi, ili kufahamu falsafa nyuma ya Client-side Validation, hebu kwanza tuangalie nyuma kwenye taratibu za Bitcoin Blockchain, kabla ya kuona jinsi Client-side Validation inatofautiana nao na ni uboreshaji gani unaowezekana.

![RGB-Bitcoin](assets/fr/009.webp)

Kwa upande wa Bitcoin Blockchain, uthibitishaji wa shughuli unategemea kanuni rahisi:


- Node zote za mtandao hupakua kila block na shughuli;
- Wanathibitisha shughuli hizi ili kuthibitisha mabadiliko sahihi ya seti ya UTXO (matokeo yote ambayo hayajatumika);
- Wanahifadhi data hii (kwa namna ya vizuizi) ili historia iweze kurudiwa ikiwa ni lazima.

![RGB-Bitcoin](assets/fr/010.webp)

Walakini, muundo huu una shida mbili kuu:


- Scalability**: kwa kuwa kila nodi lazima ichakate, ithibitishe na kuhifadhi shughuli za kila mtu kwenye kumbukumbu, kuna kikomo dhahiri cha uwezo wa muamala, unaohusishwa haswa na ukubwa wa juu wa block (MB 1 kwa wastani zaidi ya dakika 10 kwa Bitcoin, bila kujumuisha vidakuzi);
- Faragha**: kila kitu kinatangazwa na kuhifadhiwa hadharani (kiasi, anwani lengwa, n.k.), ambayo inazuia usiri wa ubadilishanaji.

![RGB-Bitcoin](assets/fr/012.webp)

Kiutendaji, muundo huu hufanya kazi kwa Bitcoin kama msingi wa Layer (Layer 1), lakini inaweza kuwa haitoshi kwa matumizi magumu zaidi ambayo kwa wakati mmoja yanahitaji upitishaji wa juu wa muamala na kiwango fulani cha usiri.

Client-side Validation inategemea wazo kinyume: badala ya kuhitaji mtandao mzima kuhalalisha na kuhifadhi miamala yote, kila mshiriki (mteja) atathibitisha tu sehemu ya historia inayomhusu:


- Mtu anapopokea mali (au mali nyingine yoyote ya kidijitali), anahitaji tu kujua na kuthibitisha mlolongo wa shughuli (mpito za serikali) zinazoongoza kwenye mali hiyo na kuthibitisha uhalali wake;
- Msururu huu wa shughuli, kutoka kwa ***Genesis*** (toleo la awali) hadi shughuli ya hivi majuzi zaidi, huunda grafu iliyoelekezwa kwa acyclic (DAG) au Shard, yaani, sehemu ya historia ya jumla.

![RGB-Bitcoin](assets/fr/013.webp)

Wakati huo huo, ili mtandao uliobaki (au kwa usahihi zaidi, Layer ya msingi, kama vile Bitcoin) iweze kufunga katika hali ya mwisho bila kuona maelezo ya data hii, Client-side Validation inategemea dhana ya ***Commitment***.

*Commitment* ni kriptografia Commitment, kwa kawaida _hash_ (SHA-256 kwa mfano) huingizwa katika shughuli ya Bitcoin, ambayo inathibitisha kuwa data ya faragha imejumuishwa, bila kufichua data hii.

Shukrani kwa _ahadi_ hizi, tunaweza kuthibitisha:


- Uwepo wa habari (kwani imejitolea kwa Hash);
- Utangulizi wa habari hii (kwa sababu ni nanga na imepigwa wakati katika Blockchain, na tarehe na utaratibu wa kuzuia).

Maudhui kamili, hata hivyo, hayajafichuliwa, hivyo kuhifadhi usiri wake.

Kwa maneno madhubuti, hii ndio jinsi RGB State Transition inavyofanya kazi:


- Unatayarisha State Transition mpya (k.m. uhamisho wa ishara ya RGB);
- Unaweka generate kificho Commitment kwa mpito huu na kuiingiza katika shughuli ya Bitcoin (ahadi hizi zinaitwa "*nanga*" katika itifaki ya RGB);
- Mshirika (mpokeaji) hurejesha historia ya upande wa mteja inayohusishwa na kipengee hiki na kuthibitisha uthabiti wa mwisho hadi mwisho, kutoka Genesis ya Smart contract hadi mpito unayoipitishia.

![RGB-Bitcoin](assets/fr/014.webp)

Client-side Validation inatoa faida kuu mbili:


- Ubora:**

Ahadi (*ahadi*) zilizojumuishwa kwenye Blockchain ni ndogo (za mpangilio wa baiti kadhaa). Hii inahakikisha kwamba nafasi ya kuzuia haijajaa, kwani ni Hash pekee inayohitaji kuingizwa. Pia huwezesha itifaki ya off-chain kubadilika, kwani kila mtumiaji anapaswa tu kuhifadhi kipande chake cha historia (_stash_ yake).


- Faragha :**

Miamala yenyewe (yaani maudhui yake ya kina) haijachapishwa On-Chain. Alama zao za vidole pekee (*Hash*) ndizo. Kwa hivyo, kiasi, anwani na mantiki ya Contract hubakia faragha, na mpokeaji anaweza kuthibitisha, ndani ya nchi, uhalali wa Shard yake kwa kukagua mabadiliko yote ya awali. Hakuna sababu kwa mpokeaji kuweka data hii kwa umma, isipokuwa katika tukio la mzozo au ambapo uthibitisho unahitajika.

Katika mfumo kama vile RGB, mabadiliko mengi ya serikali kutoka kwa mikataba tofauti (au mali tofauti) yanaweza kujumlishwa kuwa muamala mmoja wa Bitcoin kupitia _commitment_ moja. Utaratibu huu huanzisha kiungo cha kuamua, kilichowekwa kwa wakati kati ya shughuli ya On-Chain na data ya off-chain (mipito iliyoidhinishwa ya upande wa mteja), na kuwezesha shards nyingi kurekodiwa kwa wakati mmoja katika nukta moja ya Anchor, na hivyo kupunguza zaidi gharama na alama ya On-Chain.

Katika mazoezi, wakati shughuli hii ya Bitcoin imeidhinishwa, "hufunga" kabisa hali ya mikataba ya msingi, kwani inakuwa vigumu kurekebisha Hash tayari imeandikwa katika Blockchain.

![RGB-Bitcoin](assets/fr/015.webp)

### Dhana ya Stash

**Stash** ni seti ya data ya upande wa mteja ambayo mshiriki lazima ahifadhi kabisa ili kudumisha uadilifu na historia ya RGB Smart contract. Tofauti na kituo cha Umeme, ambapo majimbo fulani yanaweza kujengwa upya ndani ya nchi kutokana na taarifa zilizoshirikiwa, Stash ya RGB Contract haijaigwa mahali pengine: ukiipoteza, hakuna mtu atakayeweza kuirejesha kwako, kwa kuwa unawajibika kwa sehemu yako ya historia. Hii ndiyo sababu unahitaji kupitisha mfumo na taratibu za kuaminika za chelezo katika RGB.

![RGB-Bitcoin](assets/fr/016.webp)

### Single-Use Seal: asili na uendeshaji

Wakati wa kukubali mali kama vile sarafu, dhamana mbili ni muhimu:


- Uhalisi wa bidhaa iliyopokelewa;
- Upekee wa bidhaa iliyopokelewa, ili kuepuka gharama mara mbili.

Kwa mali halisi, kama vile noti, uwepo wa kimwili unatosha kuthibitisha kwamba haujarudiwa. Hata hivyo, katika ulimwengu wa kidijitali, ambapo mali ni ya taarifa tu, uthibitishaji huu ni mgumu zaidi, kwani maelezo yanaweza kuongezeka kwa urahisi na kunakiliwa.

Kama tulivyoona hapo awali, ufunuo wa mtumaji wa historia ya mabadiliko ya serikali hutuwezesha kuhakikisha uhalisi wa tokeni ya RGB. Kwa kupata ufikiaji wa shughuli zote tangu muamala wa Genesis, tunaweza kuthibitisha uhalisi wa tokeni. Kanuni hii ni sawa na ile ya Bitcoin, ambapo historia ya sarafu inaweza kufuatiliwa hadi kwenye Coinbase Transaction ya awali ili kuthibitisha uhalali wao. Hata hivyo, tofauti na Bitcoin, historia hii ya mabadiliko ya serikali katika RGB ni ya faragha na kuwekwa upande wa mteja.

Ili kuzuia Double-spending ya ishara za RGB, tunatumia utaratibu unaoitwa "**Single-Use Seal**". Mfumo huu unahakikisha kwamba kila ishara, mara tu inapotumiwa, haiwezi kutumika tena kwa ulaghai mara ya pili.

Mihuri ya matumizi moja ni maandishi ya awali ya kriptografia, yaliyopendekezwa mwaka wa 2016 na Peter Todd, sawa na dhana ya mihuri halisi: mara tu Seal imewekwa kwenye chombo, inakuwa vigumu kuifungua au kuirekebisha bila kuvunja Seal bila kutenduliwa.

![RGB-Bitcoin](assets/fr/018.webp)

Njia hii, iliyopitishwa kwa ulimwengu wa kidijitali, inafanya uwezekano wa kudhibitisha kuwa mlolongo wa matukio umefanyika kweli, na kwamba hauwezi tena kubadilishwa nyuma. Mihuri ya matumizi moja kwa hivyo huenda zaidi ya mantiki rahisi ya `Hash + Timestamp`, na kuongeza dhana ya Seal ambayo inaweza kufungwa **mara moja tu**.

![RGB-Bitcoin](assets/fr/017.webp)

Ili Mihuri ya Matumizi Moja ifanye kazi, unahitaji nyenzo ya uthibitisho wa uchapishaji inayoweza kuthibitisha kuwepo au kutokuwepo kwa uchapishaji, na vigumu (ikiwa haiwezekani) kughushi mara tu taarifa inaposambazwa. **Blockchain** (kama Bitcoin) inaweza kujaza jukumu hili, kama vile gazeti la karatasi lenye mzunguko wa umma, kwa mfano. Wazo ni kama ifuatavyo:


- Tunataka kuthibitisha kuwa Commitment fulani kwenye ujumbe `h(m)` imechapishwa kwa hadhira bila kufichua maudhui ya ujumbe `m` ;
- Tunataka kuthibitisha kwamba hakuna ujumbe mwingine wa `h(m')` unaoshindana Commitment ambao umechapishwa badala ya `h(m)` ;
- Pia tunataka kuweza kuangalia kuwa ujumbe `m` upo kabla ya tarehe fulani.

Blockchain inajitolea kwa jukumu hili: punde tu shughuli inapojumuishwa kwenye kizuizi, mtandao mzima una uthibitisho sawa usio na uwongo wa kuwepo kwake na maudhui (angalau kwa sehemu, kwa kuwa _commitment_ inaweza kuficha maelezo wakati wa kuthibitisha ukweli wa ujumbe).

Kwa hivyo Single-Use Seal inaweza kuonekana kama ahadi rasmi ya kuchapisha ujumbe (bado haujulikani kwa hatua hii) mara moja na mara moja tu, kwa njia ambayo inaweza kuthibitishwa na wahusika wote wanaovutiwa.

Tofauti na _ahadi_ rahisi (Hash) au mihuri ya muda, ambayo inathibitisha tarehe ya kuwepo, Single-Use Seal inatoa hakikisho la ziada kwamba **hakuna Commitment** mbadala inayoweza kuwepo pamoja: huwezi kufunga Seal sawa mara mbili, au kujaribu kubadilisha ujumbe uliotiwa muhuri.

Ulinganisho ufuatao husaidia kuelewa kanuni hii:


- Cryptographic Commitment (Hash)**: Ukiwa na chaguo za kukokotoa za Hash, unaweza kujitolea kwa kipande cha data (nambari) kwa kuchapisha Hash yake. Data inabakia kuwa siri hadi udhihirishe picha ya awali, lakini unaweza kuthibitisha kwamba uliijua mapema;
- Timestamp (Blockchain)**: Kwa kuingiza Hash hii katika Blockchain, tunathibitisha pia kwamba tuliijua kwa wakati mahususi (ile ya kujumuishwa kwenye kizuizi);
- Single-Use Seal**: Kwa mihuri ya matumizi moja, tunaenda hatua moja zaidi kwa kuifanya Commitment kuwa ya kipekee. Ukiwa na Hash moja, unaweza kuunda ahadi kadhaa zinazopingana sambamba (tatizo la daktari ambaye anatangaza "*Ni mvulana*" kwa familia na "*Ni msichana*" katika shajara yake ya kibinafsi). Single-Use Seal inaondoa uwezekano huu kwa kuunganisha Commitment kwa njia ya uthibitisho wa uchapishaji, kama vile Bitcoin Blockchain, ili matumizi ya UTXO yaweke Commitment kwa uhakika. Mara baada ya kutumiwa, UTXO hiyo hiyo haiwezi kutumika tena kuchukua nafasi ya Commitment.

|                                                                                  | Rahisi Commitment (digest/Hash) | Muhuri wa nyakati | Mihuri ya matumizi moja |

| -------------------------------------------------------------------------- | ------------------------------- | ---------- | ---------------- |

| Kuchapisha Commitment hakufichui ujumbe | Ndiyo | Ndiyo | Ndiyo |

| Uthibitisho wa tarehe ya Commitment / kuwepo kwa ujumbe kabla ya tarehe fulani | Haiwezekani | Inawezekana | Inawezekana |

| Uthibitisho kwamba hakuna mbadala wa Commitment unaweza kuwepo | Haiwezekani | Haiwezekani | Inawezekana |

Mihuri ya matumizi moja hufanya kazi katika hatua kuu tatu:

**Seal Definition :**


- Alice anafafanua mapema sheria za uchapishaji wa Seal (wakati, wapi na jinsi ujumbe utachapishwa);
- Bob anakubali au anakubali masharti haya.

![RGB-Bitcoin](assets/fr/021.webp)

**Seal Inafungwa :**


- Wakati wa utekelezaji, Alice hufunga Seal kwa kuchapisha ujumbe halisi (kwa kawaida katika mfumo wa _commitment_, k.m. Hash);
- Pia hutoa **shahidi** (ushahidi wa siri) unaothibitisha kuwa Seal imefungwa na haiwezi kubatilishwa.

![RGB-Bitcoin](assets/fr/019.webp)

**Uthibitishaji wa Seal :**


- Mara tu Seal imefungwa, Bob hawezi tena kuifungua: anaweza kuangalia tu kwamba imefungwa;
- Bob hukusanya Seal, **shahidi** na ujumbe (au Commitment yake) ili kuhakikisha kuwa kila kitu kinalingana na kwamba hakuna mihuri inayoshindana au matoleo tofauti.

Mchakato unaweza kufupishwa kama ifuatavyo:

```txt
# Défini par Alice, validé ou accepté par Bob
seal <- Define()
# Fermeture du sceau par Alice avec le message
witness <- Close(seal, message)
# Vérification par Bob
bool <- Verify(seal, witness, message)
```

Client-side Validation, hata hivyo, huenda hatua moja zaidi: ikiwa ufafanuzi wa Seal yenyewe unabaki nje ya Blockchain, inawezekana (kwa nadharia) kwa mtu kupinga kuwepo au uhalali wa Seal katika swali. Ili kuondokana na tatizo hili, mlolongo wa kuunganisha Mihuri ya Matumizi Moja hutumiwa:


- Kila Seal iliyofungwa ina ufafanuzi wa Seal ifuatayo;
- Tunasajili kufungwa huku (pamoja na _ahadi_ zao) ndani ya Blockchain (katika muamala wa Bitcoin);
- Kwa hivyo, jaribio lolote la kurekebisha Seal iliyopita lingepingana na historia iliyoingia kwenye Bitcoin.

Hivi ndivyo mfumo wa RGB hufanya:


- Ujumbe uliochapishwa ni _ahadi_ kwa data iliyothibitishwa ya upande wa mteja;
- Seal Definition inahusishwa na Bitcoin UTXO;
- Seal hufunga wakati UTXO hii inatumiwa au wakati pato jipya linawekwa kwenye Commitment sawa;
- Msururu wa muamala unaotumia UTXO hizi unalingana na uthibitisho wa uchapishaji: kila mpito au mabadiliko ya hali kwenye RGB kwa hivyo yamewekwa kwenye Bitcoin.

Kwa muhtasari:


- Ufafanuzi wa _muhuri_ ni UTXO unayokusudia Seal Commitment ya baadaye;
- _seal closing_ hutokea unapotumia UTXO hii, kutengeneza muamala ambao una Commitment;
- _shahidi_ ni shughuli yenyewe, ambayo inathibitisha kwamba umefunga Seal na maudhui haya;
- Huwezi kuthibitisha kwamba Seal haijafungwa (huwezi kuwa na uhakika kabisa kwamba UTXO haijatumiwa tayari au haitatumika katika kizuizi ambacho haujaona bado), lakini unaweza kuthibitisha kwamba kweli imefungwa.

Upekee huu ni muhimu kwa Client-side Validation: unapoidhinisha State Transition, unaangalia kuwa inalingana na UTXO ya kipekee, ambayo haikutumiwa hapo awali katika Commitment inayoshindana. Hii ndiyo inahakikisha kutokuwepo kwa matumizi mara mbili katika mikataba ya smart ya off-chain.

### Ahadi nyingi na mizizi

RGB Smart contract inaweza kuhitaji kutumia Mihuri ya Matumizi Moja (UTXO kadhaa) kwa wakati mmoja. Zaidi ya hayo, muamala mmoja wa Bitcoin unaweza kurejelea mikataba kadhaa tofauti, kila moja ikifunga State Transition yake. Hili linahitaji utaratibu wa **Commitment** nyingi ili kuthibitisha, kwa uthabiti na kipekee, kwamba hakuna ahadi yoyote iliyopo katika nakala. Hapa ndipo dhana ya **Anchor** inapojitokeza katika RGB: muundo maalum unaounganisha muamala wa Bitcoin na ahadi moja au zaidi ya upande wa mteja (mabadiliko ya serikali), kila moja ikiwezekana kuwa ya Contract tofauti. Tutaangalia kwa undani dhana hii katika sura inayofuata.

![RGB-Bitcoin](assets/fr/023.webp)

Mbili kati ya hazina kuu za mradi za GitHub (chini ya shirika la LNPBP) huunganisha pamoja utekelezaji wa kimsingi wa dhana hizi zilizosomwa katika sura ya kwanza:


- client_side_validation** : Ina Rust ya awali kwa uthibitisho wa ndani ;
- single_use_seals**: Inatekeleza mantiki ya kufafanua na kufunga mihuri hii kwa usalama.

![RGB-Bitcoin](assets/fr/020.webp)

Kumbuka kwamba matofali haya ya programu ni Bitcoin agnostic; kwa nadharia, zinaweza kutumika kwa njia nyingine yoyote ya uthibitisho wa uchapishaji (masajili nyingine, jarida, n.k.). Kwa vitendo, RGB inategemea Bitcoin kwa uimara wake na makubaliano mapana.

![RGB-Bitcoin](assets/fr/021.webp)

### Maswali kutoka kwa umma

#### Kuelekea matumizi mapana ya Mihuri ya matumizi Moja

Peter Todd pia aliunda itifaki ya _Open Timestamps_, na dhana ya Single-Use Seal ni upanuzi wa asili wa mawazo haya. Zaidi ya RGB, kesi zingine za utumiaji zinaweza kuzingatiwa, kama vile ujenzi wa _sidechains_ bila kutumia _merge mining_ au mapendekezo yanayohusiana na drivechain kama BIP300. Mfumo wowote unaohitaji Commitment moja unaweza, kimsingi, kutumia mbinu hii ya awali ya kriptografia. Leo, RGB ni utekelezaji mkubwa wa kwanza kamili.

#### Matatizo ya upatikanaji wa data

Kwa kuwa katika Client-side Validation, kila mtumiaji huhifadhi sehemu yake ya historia, upatikanaji wa data haujahakikishwa duniani kote. Ikiwa mtoaji wa Contract atazuia au kubatilisha taarifa fulani, huenda hujui kuhusu mabadiliko halisi ya ofa. Katika baadhi ya matukio (kama vile stablecoins), mtoaji anatarajiwa kudumisha data ya umma ili kuthibitisha kiasi katika mzunguko, lakini hakuna wajibu wa kiufundi wa kufanya hivyo. Kwa hiyo inawezekana kuunda mikataba isiyo wazi kwa makusudi na ukomo wa Supply, ambayo inaleta maswali ya uaminifu.

#### Sharding na kutengwa kwa Contract

Kila Contract inawakilisha _shard_ iliyotengwa: USDT na USDC, kwa mfano, si lazima zishiriki historia zao. Mabadiliko ya atomiki bado yanawezekana, lakini hii haihusishi kuunganisha rejista zao. Kila kitu kinafanywa kwa kriptografia Commitment, bila kufichua grafu nzima ya historia kwa kila mshiriki.

### Hitimisho

Tumeona mahali ambapo dhana ya Client-side Validation inalingana na Blockchain na _state channels_, jinsi inavyojibu kwa trilemmas za kompyuta zilizosambazwa, na jinsi inavyotumia Bitcoin Blockchain kipekee ili kuepuka Double-spending na kwa *kupiga muhuri kwa muda*. Wazo hili linatokana na dhana ya **Single-Use Seal**, kuwezesha uundaji wa ahadi za kipekee ambazo huwezi kutumia tena upendavyo. Kwa njia hii, kila mshiriki anapakia tu historia ambayo ni muhimu kabisa, na kuongeza uwekaji hatari na usiri wa mikataba mahiri huku akihifadhi usalama wa Bitcoin kama mandharinyuma.

Hatua inayofuata itakuwa kueleza kwa undani zaidi jinsi utaratibu huu wa Single-Use Seal unatumika katika Bitcoin (kupitia UTXOs), jinsi nanga zinaundwa na kuthibitishwa, na kisha jinsi mikataba kamili ya smart inavyojengwa katika RGB. Hasa, tutaangalia suala la ahadi nyingi, changamoto ya kiufundi ya kuthibitisha kwamba muamala wa Bitcoin hufunga wakati huo huo mabadiliko mengi ya serikali katika mikataba tofauti, bila kuanzisha udhaifu au ahadi mbili.

Kabla ya kuzama katika maelezo ya kiufundi zaidi ya sura ya pili, jisikie huru kusoma tena ufafanuzi muhimu (Client-side Validation, Single-Use Seal, nanga, n.k.) na kukumbuka mantiki ya jumla: tunatazamia kupatanisha uthabiti wa Bitcoin Blockchain (usalama, ugatuaji, uwekaji muhuri wa wakati, usiri,8, na zile za Bitcoin) scalability), na hii ndiyo hasa RGB na Client-side Validation wanajaribu kufikia.

## Commitment Layer

<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

:::video id=73ddea2d-c243-479d-a3dc-12d7db8eef70:::

Katika sura hii, tutaangalia utekelezaji wa Client-side Validation na Mihuri ya Matumizi Moja ndani ya Bitcoin Blockchain. Tutawasilisha kanuni kuu za RGB **Commitment Layer** (Layer 1), tukizingatia hasa mpango wa **TxO2**, ambao RGB hutumia kufafanua na kufunga Seal katika shughuli ya Bitcoin. Ifuatayo, tutajadili mambo mawili muhimu ambayo bado hayajashughulikiwa kwa undani:


- Ahadi za _deterministic Bitcoin_;
- Ahadi za itifaki nyingi.

Ni mchanganyiko wa dhana hizi unaotuwezesha kutawala mifumo au mikataba kadhaa juu ya UTXO moja na kwa hiyo Blockchain moja.

Ikumbukwe kwamba shughuli za kriptografia zilizoelezewa zinaweza kutumika, kwa maneno kamili, kwa blockchains zingine au media ya uchapishaji, lakini sifa za Bitcoin (katika suala la ugatuaji, upinzani wa udhibiti na uwazi kwa wote) hufanya iwe msingi mzuri wa kukuza upangaji wa hali ya juu kama vile inavyotakiwa na **RGB**.

### Miradi ya Commitment katika Bitcoin na matumizi yao na RGB

Kama tulivyoona katika sura ya kwanza ya kozi, Mihuri ya Matumizi Moja ni dhana ya jumla: tunatoa ahadi ya kujumuisha Commitment (_ahadi_) katika eneo mahususi la muamala, na eneo hili hufanya kama Seal ambayo tunafunga kwenye ujumbe. Walakini, kwenye Bitcoin Blockchain, kuna chaguzi kadhaa za kuchagua mahali pa kuweka _commitment_ hii.

Ili kuelewa mantiki, hebu tukumbuke kanuni ya msingi: kufunga _muhuri wa matumizi moja_, tunatumia eneo lililofungwa kwa kuingiza _ahadi_ kwenye ujumbe fulani. Katika Bitcoin, hii inaweza kufanywa kwa njia kadhaa:


- Tumia ufunguo wa umma au Address**

Tunaweza kuamua kuwa ufunguo mahususi wa umma au Address ndio _muhuri wa matumizi moja_. Mara tu ufunguo huu au Address inaonekana On-Chain katika shughuli, ina maana kwamba Seal imefungwa na ujumbe fulani.


- Tumia pato la muamala la Bitcoin**

Hii ina maana kwamba _seal-matumizi moja_ inafafanuliwa kama _outpoint_ sahihi (jozi ya nambari ya pato ya txid +). Mara tu _outpoint_ hii inapotumika, Seal inafungwa.

Wakati tukifanyia kazi RGB, tulitambua angalau njia 4 tofauti za kutekeleza mihuri hii kwenye Bitcoin:


- Bainisha Seal kupitia ufunguo wa umma, na uifunge kwa _output_ ;
- Bainisha Seal kwa _outpoint_ na uifunge kwa _output_ ;
- Bainisha Seal kupitia thamani ya ufunguo wa umma, na uifunge kwa _input_ ;
- Bainisha Seal kupitia _outpoint_, na uifunge kwa _input_.

| Jina la Schema | Seal Definition | Seal Kufungwa | Mahitaji ya Ziada | Maombi Kuu | Mipango inayowezekana ya Commitment |

| ----------- | ------------------------- | ------------------------- | ---------------------------------------------------------- | --------------------------- | ------------------------------- |

| PkO | Thamani ya Ufunguo wa Umma | Pato la Muamala | P2(W)PKH | Hakuna kwa sasa | Keytweak, taptweak, opret |

| TxO2 | Pato la Muamala | Pato la Muamala | Inahitaji ahadi bainifu kwenye Bitcoin | RGBv1 (zima) | Kurekebisha, tapret, opret |

| PkI | Thamani ya Ufunguo wa Umma | Ingizo la Muamala | Taproot pekee na haioani na pochi za urithi | Vitambulisho vinavyotokana na Bitcoin | Sigtweak, witweak |

| TxO1 | Pato la Muamala | Ingizo la Muamala | Taproot pekee na haioani na pochi za urithi | Hakuna kwa sasa | Sigtweak, witweak |

Hatutaeleza kwa kina kuhusu kila mojawapo ya usanidi huu, kwani katika RGB tumechagua kutumia **an _outpoint_ kama ufafanuzi wa Seal**, na kuweka _commitment_ katika matokeo ya shughuli ya kutumia _outpoint_ hii. Kwa hivyo tunaweza kuanzisha dhana zifuatazo kwa mwendelezo:


- "Seal Definition "** : _outpoint_ iliyotolewa (iliyotambuliwa na txid + towe no.) ;
- "Seal kufunga "**: Muamala unaotumia _outpoint_ hii, ambapo _ahadi_ huongezwa kwa ujumbe.

Mpango huu umechaguliwa kwa utangamano wake na usanifu wa RGB, lakini usanidi mwingine unaweza kuwa muhimu kwa matumizi tofauti.

"O2" katika "TxO2" inatukumbusha kuwa ufafanuzi na kufungwa hutegemea matumizi (au uundaji) wa matokeo ya muamala.

### Mfano wa mchoro wa TxO2

Kama ukumbusho, kufafanua _seal-matumizi moja_ si lazima kuhitaji kuchapisha muamala wa On-Chain. Inatosha kwa Alice, kwa mfano, tayari kuwa na UTXO ambayo haijatumika. Anaweza kuamua: "Hii _outpoint_ (tayari ipo) sasa ni Seal yangu". Anabainisha hili ndani ya nchi (_client-side_), na hadi UTXO hii inatumika, Seal inachukuliwa kuwa wazi.

![RGB-Bitcoin](assets/fr/024.webp)

Siku inapotaka kufunga Seal (kuashiria tukio, au kwa Anchor ujumbe fulani), inatumia UTXO hii katika muamala mpya (muamala huu mara nyingi huitwa "_witness transaction_" (haihusiani na _segwit_, ni neno tu tunalotoa). Ujumbe huu mpya utakuwa na _muamala._

![RGB-Bitcoin](assets/fr/025.webp)

Kumbuka kuwa katika mfano huu:


- Hakuna mtu ila Bob (au watu ambao Alice anachagua kuwafunulia uthibitisho kamili) watajua kwamba ujumbe fulani umefichwa katika shughuli hii;
- Kila mtu anaweza kuona kwamba _outpoint_ imetumika, lakini ni Bob pekee ndiye anayeshikilia uthibitisho kwamba ujumbe umetiwa nanga katika shughuli hiyo.

Ili kufafanua mpango huu wa TxO2, tunaweza kutumia _seal-matumizi moja_ kama utaratibu wa kubatilisha ufunguo wa PGP. Badala ya kuchapisha cheti cha ubatilishaji kwenye seva, Alice anaweza kusema: "Hii pato la Bitcoin, ikiwa itatumika, inamaanisha kuwa ufunguo wangu wa PGP umebatilishwa".

Kwa hivyo Alice ana UTXO maalum, ambayo hali fulani au data (inayojulikana kwake tu) inahusishwa ndani ya nchi (upande wa mteja).

Alice anamwarifu Bob kwamba ikiwa UTXO hii itatumika, tukio fulani litachukuliwa kuwa limetokea. Kutoka nje, yote tunayoona ni shughuli ya Bitcoin; lakini Bob anajua kwamba matumizi haya yana maana iliyofichika.

![RGB-Bitcoin](assets/fr/026.webp)

Alice anapotumia UTXO hii, anafunga Seal kwenye ujumbe unaoonyesha ufunguo wake mpya, au kubatilisha ule wa zamani. Kwa njia hii, mtu yeyote anayefuatilia On-Chain ataona kuwa UTXO inatumika, lakini wale tu walio na uthibitisho kamili watajua kuwa ni kubatilisha ufunguo wa PGP.

![RGB-Bitcoin](assets/fr/027.webp)

Ili Bob au mtu mwingine yeyote anayehusika aangalie ujumbe uliofichwa, ni lazima Alice ampe taarifa za off-chain.

![RGB-Bitcoin](assets/fr/028.webp)

Kwa hivyo Alice lazima ampe Bob na:


- Ujumbe wenyewe (kwa mfano, kitufe kipya cha PGP);
- Uthibitisho wa siri kwamba ujumbe ulihusika katika muamala (unaojulikana kama _extra transaction proof_ au _anchor_).

![RGB-Bitcoin](assets/fr/029.webp)

Wahusika wengine hawana habari hii. Wanaona tu kwamba UTXO imetumika. Kwa hivyo usiri unahakikishwa.

Ili kufafanua muundo, hebu tufanye muhtasari wa mchakato katika shughuli mbili:


- Muamala wa 1**: Hii ina _muhuri ufafanuzi_, yaani _outpoint_ ambayo itatumika kama Seal.

![RGB-Bitcoin](assets/fr/031.webp)


- Muamala 2**: Hutumia _outpoint_ hii. Hii inafunga Seal na, katika shughuli hiyo hiyo, inaingiza _commitment_ kwenye ujumbe.

![RGB-Bitcoin](assets/fr/033.webp)

Kwa hiyo tunaita muamala wa pili "_shahidi muamala_".

Ili kuonyesha hili kutoka kwa pembe nyingine, tunaweza kuwakilisha tabaka mbili:


- Layer ya juu (Blockchain, public)**: kila mtu anaona muamala na anajua kuwa _outpoint_ imetumika;
- Layer ya chini (upande wa mteja, faragha)** : Alice pekee (au mtu husika) anajua kwamba gharama hii inalingana na ujumbe kama huo, kupitia uthibitisho wa siri na ujumbe anaohifadhi ndani.

![RGB-Bitcoin](assets/fr/034.webp)

Lakini wakati wa kufunga Seal, swali linatokea ni wapi _commitment_ inapaswa kuingizwa.

Katika sehemu iliyopita, tulitaja kwa ufupi jinsi mfano wa Client-side Validation unaweza kutumika kwa RGB na mifumo mingine. Hapa, tunashughulikia sehemu kuhusu **ahadi bainifu za Bitcoin** na jinsi ya kuzijumuisha katika muamala. Wazo ni kuelewa ni kwa nini tunajaribu kuingiza Commitment moja kwenye _shahidi muamala_, na zaidi ya yote jinsi ya kuhakikisha kwamba hakuwezi kuwa na ahadi nyinginezo ambazo hazijafichuliwa.

### Maeneo ya Commitment katika muamala

Unapompa mtu uthibitisho kwamba ujumbe fulani umepachikwa katika muamala, unahitaji kuwa na uwezo wa kuhakikisha kuwa hakuna aina nyingine ya Commitment (sekunde, ujumbe uliofichwa) katika muamala ule ule ambao haujafichuliwa kwako. Ili Client-side Validation iendelee kuwa thabiti, unahitaji utaratibu wa **ubainishaji** wa kuweka _ahadi_ moja katika muamala unaofunga _muhuri wa matumizi moja_.

Shughuli ya _shahidi_ hutumia UTXO maarufu (au _seal definition_) na matumizi haya yanalingana na kufungwa kwa Seal. Kitaalamu, tunajua kwamba kila muhtasari unaweza kutumika mara moja tu. Hili ndilo hasa linalosisitiza upinzani wa Bitcoin kwa matumizi maradufu. Lakini shughuli ya matumizi inaweza kuwa na _pembejeo_ kadhaa, _matokeo_ kadhaa, au ikatungwa kwa njia changamano (sainjoins, njia za umeme, n.k.). Kwa hivyo tunahitaji kufafanua wazi mahali pa kuingiza _commitment_ katika muundo huu, bila utata na kwa usawa.

Njia yoyote (PkO, TxO2, n.k.), _commitment_ inaweza kuingizwa :


- Katika Ingizo** kupitia:
    - Sigtweak** (hurekebisha kipengele cha `r` cha sahihi ya ECDSA, sawa na kanuni ya "Sign-to-Contract") ;
    - Witweak** (data ya _shahidi_ aliyetengwa_ imerekebishwa).
- Katika Pato** kupitia :
    - Keytweak** (ufunguo wa umma wa mpokeaji "umebadilishwa" na ujumbe);
    - Opret** (ujumbe umewekwa katika pato lisiloweza spendable `OP_RETURN`);
    - Tapret** (au _Taptweak_), ambayo inategemea Taproot kuingiza Commitment kwenye sehemu ya hati ya ufunguo wa Taproot, hivyo basi kurekebisha ufunguo wa umma kwa uthabiti.

![RGB-Bitcoin](assets/fr/035.webp)

Hapa kuna maelezo ya kila njia:

![RGB-Bitcoin](assets/fr/038.webp)

***Sig tweak (saini-kwa-Contract) :***

Mpango wa awali ulihusisha kutumia sehemu nasibu ya sahihi (ECDSA au Schnorr) ili kupachika _commitment_: hii ndiyo mbinu inayojulikana kama "**Sign-to-Contract**". Unabadilisha Nonce iliyozalishwa bila mpangilio na Hash iliyo na data. Kwa njia hii, saini inafichua Commitment yako, bila nafasi yoyote ya ziada katika ununuzi. Mbinu hii ina faida kadhaa:


- Hakuna On-Chain overload (unatumia sehemu sawa na msingi Nonce);
- Kwa nadharia, hii inaweza kuwa tofauti kabisa, kwani Nonce hapo awali ni hifadhidata ya nasibu.

Walakini, shida kuu 2 zimeibuka:


- Multisig kabla ya Taproot: unapokuwa na watia saini kadhaa, unahitaji kuamua ni saini ipi itakayobeba _ahadi_. Saini zinaweza kuagizwa kwa njia tofauti, na ikiwa mtu aliyetia saini anakataa, unapoteza udhibiti wa matokeo ya _ahadi_;
- MuSig na Nonce iliyoshirikiwa: pamoja na Schnorr Multisig (*MuSig*), kizazi cha Nonce ni algoriti ya vyama vingi, na inakuwa vigumu kabisa kurekebisha Nonce kibinafsi.

Kwa mazoezi, **sig tweak** pia haiendani sana na maunzi yaliyopo (pochi za vifaa) na umbizo (Umeme, nk.). Kwa hivyo wazo hili kubwa ni Hard kuweka katika vitendo.

*** Marekebisho muhimu (lipa-kwa-Contract) :***

**muhimu wa kurekebisha** unachukua dhana ya kihistoria ya _lipa-kwa-mkataba_. Tunachukua ufunguo wa umma `X` na kuurekebisha kwa kuongeza thamani `H(ujumbe)`. Hasa, ikiwa `X = x * G` na `h = H(ujumbe)`, basi ufunguo mpya utakuwa `X' = X + h * G`. Ufunguo huu uliobadilishwa huficha Commitment kwa `ujumbe`. Mmiliki wa ufunguo asilia wa faragha anaweza, kwa kuongeza `h` kwenye ufunguo wake wa faragha `x`, kuthibitisha kwamba ana ufunguo wa kutumia pato. Kwa nadharia, hii ni ya kifahari, kwa sababu:


- _ahadi_ imeingizwa bila kuongeza sehemu zozote za ziada;
- Huhifadhi data yoyote ya ziada ya On-Chain.

Katika mazoezi, hata hivyo, tunakabiliana na shida zifuatazo:


- Wallet haitambui tena ufunguo wa kawaida wa umma, kwa kuwa "umebadilishwa", kwa hivyo haziwezi kuhusisha kwa urahisi UTXO na ufunguo wako wa kawaida;
- Pochi za vifaa hazijaundwa kutia saini kwa ufunguo ambao haujatokana na asili yao ya kawaida;
- Unahitaji kurekebisha hati zako, maelezo, n.k.

Katika muktadha wa RGB, njia hii ilitarajiwa hadi 2021, lakini ilionekana kuwa ngumu sana kuifanya ifanye kazi na viwango vya sasa na miundombinu.

***Marekebisho ya mashahidi:***

Wazo lingine, ambalo baadhi ya itifaki kama vile _inscriptions Ordinals_ zimeweka katika vitendo, ni kuweka data moja kwa moja katika sehemu ya `shahidi` ya shughuli ya ununuzi (kwa hivyo usemi "shahidi tweak"). Walakini, njia hii:


- Hufanya uchumba uonekane mara moja (unabandika data mbichi kwenye shahidi);
- Inaweza kuwa chini ya udhibiti (wachimbaji wa madini au nodi wanaweza kukataa relay ikiwa ni kubwa sana au tabia nyingine yoyote ya kiholela);
- Hutumia nafasi kwenye vizuizi, kinyume na lengo la RGB la busara na wepesi.

Kwa kuongezea, shahidi imeundwa ili iweze kupogolewa katika miktadha fulani, ambayo inaweza kufanya kuwa na uthibitisho thabiti kuwa mgumu zaidi.

***Rudisha-wazi (opret) :***

Rahisi sana katika uendeshaji wake, `OP_RETURN` inakuwezesha kuhifadhi Hash au ujumbe katika uwanja maalum wa manunuzi. Lakini inaweza kutambulika mara moja: kila mtu anaona kuwa kuna _ahadi_ katika shughuli hiyo, na inaweza kuchunguzwa au kutupwa, na pia kuongeza pato la ziada. Kwa kuwa hii huongeza uwazi na saizi, inachukuliwa kuwa ya kuridhisha kutoka kwa mtazamo wa suluhisho la Client-side Validation.

```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|
1-byte       1-byte         32 bytes
```

### Tapret

Chaguo la mwisho ni matumizi ya **Taproot** (iliyoletwa na BIP341) na mpango wa *Tapret*. *Tapret* ni aina changamano zaidi ya Commitment ya kubainisha, ambayo huleta maboresho katika suala la alama ya Blockchain na usiri wa shughuli za Contract. Wazo kuu ni kuficha Commitment katika sehemu ya `Njia ya Hati Tumia` ya [muamala wa Taproot](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki).

![RGB-Bitcoin](assets/fr/036.webp)

Kabla ya kueleza jinsi Commitment inavyoingizwa katika shughuli ya Taproot, hebu tuangalie **fomu kamili** ya Commitment, ambayo lazima **imeshurutishwa** ilingane na mfuatano wa baiti 64. [imejengwa](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) kama ifuatavyo:

```txt
64-byte_Tapret_Commitment =
OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|
TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```


- Baiti 29 `OP_RESERVED`, ikifuatiwa na `OP_RETURN`, kisha `OP_PUSHBYTE_33`, huunda sehemu ya _kiambishi_ cha baiti 31;
- Inayofuata inakuja _commitment_ ya baiti 32 (kawaida Merkle Root kutoka **MPC**), ambayo tunaongeza baiti 1 ya **Nonce** (jumla ya baiti 33 kwa sehemu hii ya pili).

Kwa hivyo mbinu ya `Tapret` ya baiti 64 inaonekana kama `Opret` ambayo tumeweka awali baiti 29 za `OP_RESERVED` na kuongeza baiti ya ziada kama Nonce.

Ili kudumisha kubadilika katika suala la utekelezaji, usiri na kuongeza, mpango wa Tapret huzingatia hali mbalimbali za utumiaji, kulingana na mahitaji:


- Ujumuishaji wa kipekee wa Tapret Commitment katika shughuli ya Taproot bila muundo wa Njia ya Hati iliyokuwepo;
- Ujumuishaji wa Tapret Commitment kwenye muamala wa Taproot tayari ukiwa na Njia ya Hati.

Hebu tuangalie kwa karibu kila moja ya matukio haya mawili.

#### Gusa ujumuishaji bila Njia iliyopo ya Hati

Katika kesi hii ya kwanza, tunaanza kutoka kwa kitufe cha pato cha Taproot (*Taproot Output Key*) `Q` ambayo ina ufunguo wa ndani wa umma `P` *(Internal Key*), bila njia ya hati inayohusishwa (*Script Path*) :

![RGB-Bitcoin](assets/fr/047.webp)


- `P`: ufunguo wa ndani wa umma wa _Njia ya Ufunguo Tumia_.
- `G`: sehemu inayozalisha ya mkunjo wa duaradufu [secp256k1](https://en.Bitcoin.it/wiki/Secp256k1).
- t = tH_TWEAK(P)` ni kigezo cha tweak, kinachokokotolewa kupitia _tagged hash_ (k.m. `SHA-256(SHA-256(TapTweak) || P)`), kwa mujibu wa [BIP86](https://github.com/Bitcoin/bips/blob/master/bip-0086.mediawiki#Address-derivation). Hii inathibitisha kuwa hakuna hati iliyofichwa.

Ili kujumuisha **Tapret** Commitment, ongeza **Njia ya Hati Tumia ** iliyo na **hati ya kipekee**, kama ifuatavyo:

![RGB-Bitcoin](assets/fr/048.webp)


- t = tH_TWEAK(P || Script_root)` kisha inakuwa kigezo kipya cha kurekebisha, ikijumuisha **Script_root**.
- `Script_root = tH_BRANCH(64-byte_Tapret_Commitment)` inawakilisha mzizi wa **hati** hii, ambayo ni Hash ya aina ya `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`.

Uthibitisho wa kujumuishwa na wa kipekee katika mti wa Taproot hapa unatokana na ufunguo mmoja wa ndani wa umma `P`.

#### Gusa muunganisho kwenye Njia ya Hati iliyokuwepo awali

Hali ya pili inahusu matokeo changamano zaidi ya `Q` Taproot**, ambayo tayari ina hati kadhaa. Kwa mfano, tunayo mti wa maandishi 3:

![RGB-Bitcoin](assets/fr/049.webp)


- tH_LEAF(x)` hubainisha chaguo za kukokotoa za Hash zilizowekwa tagi za kawaida za hati ya jani.
- a, B, C` inawakilisha hati ambazo tayari zimejumuishwa katika muundo wa Taproot.

Ili kuongeza Tapret Commitment, tunahitaji kuingiza *hati isiyoweza kutumika* katika ngazi ya kwanza ya mti, tukihamisha hati zilizopo ngazi moja chini. Kwa kuibua, mti unakuwa:

![RGB-Bitcoin](assets/fr/050.webp)


- thHABC` inawakilisha Hash iliyotambulishwa ya kambi ya kiwango cha juu `A, B, C`.
- tHT` inawakilisha Hash ya hati inayolingana na `Tapret` ya 64-byte.

Kulingana na sheria za Taproot, kila tawi/jani lazima liunganishwe kulingana na mpangilio wa leksikografia wa Hash. Kuna kesi mbili zinazowezekana:


- `tHT` > `thHABC`: Tapret Commitment inasogea upande wa kulia wa mti. Uthibitisho wa upekee unahitaji tu `thHABC` na `P` ;
- tHT` < `thHABC`**: Tapret Commitment imewekwa upande wa kushoto. Ili kuthibitisha kuwa hakuna Tapret Commitment nyingine upande wa kulia, `tHAB` na `tHC` lazima zifichuliwe ili kuonyesha kutokuwepo kwa hati nyingine yoyote kama hiyo.

Mfano unaoonekana wa kesi ya kwanza (`thHABC <tHT`):

![RGB-Bitcoin](assets/fr/051.webp)

Mfano kwa kesi ya pili (`thHABC > tHT`):

![RGB-Bitcoin](assets/fr/052.webp)

#### Uboreshaji na Nonce

Ili kuboresha usiri, tunaweza "mgodi" (neno sahihi zaidi litakuwa "kulazimisha ukatili") thamani ya `<Nonce>` (baiti ya mwisho ya `Tapret` ya baiti 64) katika jaribio la kupata Hash `tHT` kiasi kwamba `tHABC < tHT`. Katika hali hii, Commitment imewekwa upande wa kulia, ili kuokoa mtumiaji kutokana na kufichua yaliyomo yote ya hati zilizopo ili kuthibitisha upekee wa Tapret.

Kwa muhtasari, `Tapret` inatoa njia dhahiri na bainifu ya kujumuisha Commitment katika shughuli ya Taproot, huku ikiheshimu hitaji la upekee na kutokuwa na utata muhimu kwa mantiki ya RGB ya Client-side Validation na Single-Use Seal.

#### Njia halali za kutoka

Kwa miamala ya RGB Commitment, hitaji kuu la mpango halali wa Bitcoin Commitment ni kama ifuatavyo: Muamala (*Witness Transaction*) lazima uwe na Commitment moja. Sharti hili hufanya isiwezekane kuunda historia mbadala kwa data iliyothibitishwa ya upande wa mteja ndani ya shughuli hiyo hiyo. Hii ina maana kwamba ujumbe ambao _seal-matumizi moja_ hufunga ni wa kipekee.

Ili kukidhi kanuni hii, na bila kujali idadi ya matokeo katika muamala, tunahitaji kwamba **toleo moja na moja pekee** linaweza kuwa na Commitment (*Commitment*). Kwa kila moja ya miundo inayotumika (*Opret* au *Tapret*), matokeo halali pekee ambayo yanaweza kuwa na RGB _commitment_ ni :


- Toleo la kwanza `OP_RETURN` (kama lipo) la mpango wa *Opret*;
- Pato la kwanza la Taproot (kama lipo) la mpango wa *Tapret*.

Kumbuka kuwa inawezekana kabisa kwa muamala kuwa na `Opret` Commitment moja na `Tapret` Commitment moja katika matokeo mawili tofauti. Shukrani kwa hali ya uamuzi ya Seal Definition, ahadi hizi mbili basi zinalingana na vipande viwili tofauti vya data vilivyothibitishwa kwa upande wa mteja.

### Uchambuzi na chaguzi za vitendo katika RGB

Tulipoanzisha RGB, tulikagua mbinu hizi zote ili kubaini ni wapi na jinsi ya kuweka _ahadi_ katika muamala kwa njia ya kubainisha. Tulifafanua baadhi ya vigezo:


- Utangamano na matukio tofauti (k.m. Multisig, Umeme, pochi za vifaa, nk);
- Athari kwenye nafasi ya On-Chain;
- Ugumu wa utekelezaji na matengenezo;
- Usiri na upinzani dhidi ya udhibiti.

| Mbinu | On-Chain alama & saizi | Saizi ya upande wa mteja | Ushirikiano wa Wallet | Utangamano wa Vifaa | Utangamano wa Umeme | Utangamano wa Taproot |

| ------------------------------------------------ | --------------------- | ---------------- | ------------------ | ---------------------- | ---------------------- | --------------------- |

| Keytweak (P2C inayoamua) | 🟢 | 🟡 | 🔴 | 🟠 | 🔴 Bolt, 🔴 Bifrost | 🟠 Taproot, 🟢 MuSig |

| Sigtweak (S2C inayoamua) | 🟢 | 🟢 | 🟠 | 🔴 | 🔴 Bolt, 🔴 Bifrost | 🟠 Taproot, 🔴 MuSig |

| Opret (OP_RETURN) | 🔴 | 🟢 | 🟢 | 🟠 | 🔴 Bolt, 🟠 Bifrost | - |

| Tapret Algorithm: nodi ya juu-kushoto | 🟠 | 🔴 | 🟠 | 🟢 | 🔴 Bolt, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig |

| Tapret Algorithm #4: nodi yoyote + dhibitisho | 🟢 | 🟠 | 🟠 | 🟢 | 🔴 Bolt, 🟢 Bifrost | 🟢 Taproot, 🟢 MuSig |

| Mpango wa Kuamua wa Commitment | Kawaida | Gharama ya On-Chain | Saizi ya Uthibitisho kwa Upande wa Mteja |

| --------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------... --------------------------------------------------------------------------------------------- |

| Keytweak (P2C ya Kuamua) | LNPBP-1, 2 | baiti 0 | 33 byte (ufunguo usio na tweaked) |

| Sigtweak (Deterministic S2C) | WIP (LNPBP-39) | baiti 0 | baiti 0 |

| Opret (OP_RETURN) | - | 36 (v)baiti (TxOut ya ziada) | baiti 0 |

| Tapret Algorithm: nodi ya juu-kushoto | LNPBP-6 | Baiti 32 katika shahidi (8 vbytes) kwa n-of-m Multisig yoyote na matumizi kupitia njia ya hati | Baiti 0 kwenye hati zisizo na hati Taproot ~ 270 byte katika kesi moja ya hati, ~ byte 128 ikiwa hati nyingi |

| Tapret Algorithm #4: nodi yoyote + uthibitisho wa kipekee | LNPBP-6 | Baiti 32 katika shahidi (vibaiti 8) kwa kesi za hati moja, baiti 0 katika shahidi katika kesi zingine nyingi | 0 baiti kwenye hati zisizo na hati Taproot, baiti 65 hadi Taptree iwe na hati kadhaa |

| Layer | Gharama ya On-Chain (Baiti/vbytes) | Gharama ya On-Chain (Baiti/vbytes) | Gharama ya On-Chain (Baiti/vbytes) | Gharama ya On-Chain (Baiti/vbytes) | Gharama ya On-Chain (Baiti/vbytes) | Gharama ya Upande wa Mteja (Baiti) | Gharama ya Upande wa Mteja (Baiti) | Gharama ya Upande wa Mteja (Baiti) | Gharama ya Upande wa Mteja (Baiti) | Gharama ya Upande wa Mteja (Baiti) |

| ------------------------------ | --------------------------- | --------------------------- | --------------------------- | --------------------------- | --------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |

| **Aina** | **Gonga** | **Gonga #4** | **Keytweak** | **Sigtweak** | **Opret** | **Gonga** | **Gonga #4** | **Keytweak** | **Sigtweak** | **Opret** |

| Sigi moja | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 32 | 0?                       | 0 |

| MuSig (n-of-n) | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 32 | ? > 0 | 0 |

| multi-sig 2-ya-3 | 32/8 | 32/8 au 0 | 0 | n/a | 32 | ~ 270 | 65 | 32 | n/a | 0 |

| multi-sig 3-ya-5 | 32/8 | 32/8 au 0 | 0 | n/a | 32 | ~ 340 | 65 | 32 | n/a | 0 |

| multi-sig 2-ya-3 na muda umeisha | 32/8 | 0 | 0 | n/a | 32 | 64 | 65 | 32 | n/a | 0 |

| Layer | On-Chain Gharama (vbytes) | On-Chain Gharama (vbytes) | On-Chain Gharama (vbytes) | Gharama ya Upande wa Mteja (baiti) | Gharama ya Upande wa Mteja (baiti) |

| ------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |

| **Aina** | **Msingi** | **Gonga #2** | **Gonga #4** | **Gonga #2** | **Gonga #4** |

| MuSig (n-of-n) | 16.5 | 0 | 0 | 0 | 0 |

| FROST (n-of-m) | ?                      | 0 | 0 | 0 | 0 |

| Multi_a (n-of-m) | 1+16n+8m | 8 | 8 | 33 * m | 65 |

| MuSig ya Tawi / Multi_a (n-of-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| Na muda umeisha (n-of-m) | 1+16n+8n+8xlog(n) | 8 | 0 | 64 | 65 |

| Mbinu | Faragha na Uwezo | Mwingiliano | Utangamano | Kubebeka | Utata |

| ---------------------------------------- | ---------------------- | ---------------- | ------------- | ----------- | ---------- |

| Keytweak (P2C ya Kuamua) | 🟢 | 🔴 | 🔴 | 🟡 | 🟡 |

| Sigtweak (Deterministic S2C) | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 |

| Opret (OP_RETURN) | 🔴 | 🟠 | 🔴 | 🟢 | 🟢 |

| Algo Tapret: nodi ya juu kushoto | 🟠 | 🟢 | 🟢 | 🔴 | 🟠 |

| Algo Tapret #4: Nodi yoyote + dhibitisho | 🟢 | 🟢 | 🟢 | 🟠 | 🔴 |

Katika kipindi cha utafiti, ilionekana wazi kuwa hakuna mpango wowote wa Commitment unaoendana kikamilifu na kiwango cha sasa cha Umeme (ambacho hakitumii Taproot, _muSig2_ au usaidizi wa ziada wa _commitment). Juhudi zinaendelea za kurekebisha ujenzi wa chaneli ya Lightning (*BiFrost*) ili kuruhusu uwekaji wa ahadi za RGB. Hili ni eneo lingine ambalo tunahitaji kukagua muundo wa muamala, funguo na jinsi masasisho ya vituo yanavyotiwa saini.

Uchanganuzi ulionyesha kuwa, kwa kweli, mbinu zingine (key tweak, sig tweak, shahidi tweak, n.k.) ziliwasilisha aina zingine za utata:


- Ama tuna kiasi kikubwa cha On-Chain;
- Ama kuna kutopatana kwa kiasi kikubwa na msimbo uliopo wa Wallet;
- Ama suluhisho haliwezi kutumika katika mashirika yasiyo ya ushirika Multisig.

Kwa RGB, mbinu mbili hasa zinajulikana: ***Opret*** na ***Tapret***, zote zikiwa zimeainishwa kama "Pato la Muamala", na zinazooana na hali ya TxO2 inayotumiwa na itifaki.

### Ahadi nyingi za Itifaki - MPC

Katika sehemu hii, tunaangalia jinsi **RGB** hushughulikia ujumlishaji wa mikataba mingi (au, kwa usahihi zaidi, _vifurushi vyake vya mpito_) ndani ya Commitment (*Commitment*) moja iliyorekodiwa katika shughuli ya Bitcoin kupitia mpango wa kubainisha (kulingana na `Tapret` au `Opret`). Ili kufanikisha hili, utaratibu wa Merkelization wa mikataba mbalimbali unafanyika katika muundo unaoitwa **MPC Tree** (_Multi Protocol Commitment Tree_). Katika sehemu hii, tutaangalia ujenzi wa Mti huu wa MPC, jinsi ya kupata mzizi wake, na jinsi kandarasi nyingi zinaweza kushiriki muamala sawa kwa siri na bila utata.

Multi Protocol Commitment (MPC) imeundwa kukidhi mahitaji mawili:


- Ujenzi wa `mpc::Commitment` Hash: hii itajumuishwa katika Bitcoin Blockchain kulingana na mpango wa `Opret` au `Tapret`, na lazima iakisi mabadiliko yote ya serikali ili kuthibitishwa;
- Uhifadhi wa wakati mmoja wa mikataba mingi katika _ahadi_ moja, kuwezesha masasisho tofauti kuhusu mali nyingi au mikataba ya RGB kusimamiwa katika muamala mmoja wa Bitcoin.

Kwa maneno madhubuti, kila _transition bundle_ ni mali ya Contract fulani. Maelezo haya yote yameingizwa kwenye **Mti wa MPC**, ambao mzizi wake (`mpc::Root`) huharakishwa tena ili kutoa `mpc::Commitment`. Ni Hash hii ya mwisho ambayo imewekwa katika shughuli ya Bitcoin (_witness transaction_), kulingana na mbinu ya kubainisha iliyochaguliwa.

![RGB-Bitcoin](assets/fr/042.webp)

#### Mzizi wa MPC Hash

Thamani iliyoandikwa kwa hakika On-Chain (katika `Opret` au `Tapret`) inaitwa `mpc::Commitment`. Hii inakokotolewa katika mfumo wa [BIP-341](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki), kulingana na fomula :

```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```

wapi:


- `mpc_tag` ni lebo: `urn:ubideco:mpc:Commitment#2024-01-31`, iliyochaguliwa kulingana na [kanuni za kuweka lebo za RGB](https://github.com/RGB-WG/RGB-core/blob/master/doc/Commitments);
- `kina` (baiti 1) huonyesha kina cha *Mti wa MPC* ;
- cofactor` (biti 16, katika Endian Kidogo) ni kigezo kinachotumiwa kukuza upekee wa nafasi zilizopewa kila Contract kwenye mti;
- `mpc::Root` ni mzizi wa *MPC Tree*, unaokokotolewa kulingana na mchakato ulioelezwa katika sehemu inayofuata.

![RGB-Bitcoin](assets/fr/044.webp)

#### MPC ujenzi wa miti

Ili kujenga Mti huu wa MPC, tunahitaji kuhakikisha kwamba kila Contract inalingana na nafasi ya kipekee ya jani. Tuseme tunayo:


- c` mikataba ya kujumuishwa, iliyoorodheshwa na `i` katika `i = {0,1,..,C-1}` ;
- Kwa kila Contract `c_i`, tuna kitambulisho `ContractId(i) = c_i`.

Kisha tunaunda mti wa upana `w` na kina `d` hivi kwamba `2^d = w`, kwa `w > C`, ili kila Contract iwekwe katika _jani_ tofauti. Nafasi `pos(c_i)` ya kila Contract kwenye mti imebainishwa na:

```txt
pos(c_i) = c_i mod (w - cofactor)
```

ambapo `cofactor` ni nambari kamili inayoongeza uwezekano wa kupata nafasi tofauti kwa kila Contract. Kwa mazoezi, ujenzi unafuata mchakato wa kurudia:


- Tunaanza kutoka kwa kina cha chini kabisa (`d=3` kwa makubaliano ili kuficha idadi kamili ya mikataba);
- Tunajaribu `cofactors` tofauti (hadi `w/2`, au zisizozidi 500 kwa sababu za utendaji);
- Ikiwa tutashindwa kuweka mikataba yote bila mgongano, tunaongeza `d` na kuanza tena.

Kusudi ni kuzuia miti ambayo ni mirefu sana, huku ukiweka hatari ya kugongana kwa kiwango cha chini. Kumbuka kuwa tukio la mgongano hufuata mantiki ya usambazaji nasibu, iliyounganishwa na [Anniversary Paradox](https://en.wikipedia.org/wiki/Birthday_problem).

#### Majani yanayokaliwa

Mara baada ya `C` nafasi mahususi `pos(c_i)` kupatikana kwa kandarasi `i = {0,1,..,C-1}`, kila laha hujazwa na chaguo za kukokotoa za Hash (*imewekwa lebo ya Hash*):

```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```

wapi:


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, huchaguliwa kila mara kulingana na kanuni za Merkle za RGB ;
- `0x10` inabainisha _jani la mkataba_ ;
- `c_i` ni kitambulishi cha Contract cha baiti 32 (kinachotokana na Genesis Hash);
- bundleId(c_i)` ni Hash ya baiti 32 inayoelezea seti ya `Mipito ya Jimbo` inayohusiana na `c_i` (iliyokusanywa katika *Transition Bundle*).

#### Majani yasiyo na watu

Majani yaliyosalia, ambayo hayajawekwa kwa Contract (yaani `w - C` majani), yamejazwa thamani ya "dummy" (_entropy leaf_) :

```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```

wapi:


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, huchaguliwa kila mara kulingana na kanuni za Merkle za RGB ;
- `0x11` inaashiria _jani la entropy_ ;
- `entropy` ni thamani ya nasibu ya baiti 64, iliyochaguliwa na mtu anayejenga mti;
- `j` ni nafasi (katika biti 32 Endian Ndogo) ya jani hili kwenye mti.

#### Nodi za MPC

Baada ya kutengeneza majani ya `w` (yatakayokaliwa au la), tunaendelea na utengenezaji wa merkelization. Nodi zozote za ndani zimeharakishwa kama ifuatavyo:

```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```

wapi:


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, huchaguliwa kila mara kulingana na kanuni za Merkle za RGB ;
- b` ni _kigezo cha matawi_ (biti 8). Mara nyingi, `b=0x02` kwa sababu mti ni wa jozi na umekamilika;
- d` ni kina cha nodi kwenye mti;
- `w` ni upana wa mti (katika binary ya Endian Ndogo ya 256-bit);
- tH1` na `tH2` ni heshi za nodi za mtoto (au majani), ambazo tayari zimekokotolewa kama inavyoonyeshwa hapo juu.

Inaendelea kwa njia hii, tunapata mzizi `mpc::Root`. Kisha tunaweza kukokotoa `mpc::Commitment` (kama ilivyoelezwa hapo juu) na kuiingiza On-Chain.

Ili kufafanua hili, hebu tufikirie mfano ambapo `C=3` (mikataba mitatu). Nafasi zao zinachukuliwa kuwa `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`. Majani mengine (nafasi 0, 1, 3, 5, 6) ni _majani ya entropy_. Mchoro hapa chini unaonyesha mlolongo wa heshi kwenye mzizi na:


- `BUNDLE_i` ambayo inawakilisha `BundleId(c_i)` ;
- `tH_MPC_LEAF(A)` na kadhalika, ambayo inawakilisha majani (baadhi ya kandarasi, wengine kwa entropy);
- Kila tawi `tH_MPC_BRANCH(...)` huchanganya heshi za watoto wake wawili.

Matokeo ya mwisho ni **mpc::Root**, kisha `mpc::Commitment`.

![RGB-Bitcoin](assets/fr/053.webp)

#### ukaguzi wa shimoni la MPC

Kithibitishaji kinapotaka kuhakikisha kuwa `c_i` Contract (na `BundleId` yake) imejumuishwa kwenye `mpc::Commitment` ya mwisho, anapokea tu uthibitisho wa Merkle. Uthibitisho huu unaonyesha vifundo vinavyohitajika ili kufuatilia majani (katika kesi hii, `c_i`'s _contract jani_) kurudi kwenye mzizi. Hakuna haja ya kufichua *Mti wa MPC* mzima: hii inalinda usiri wa mikataba mingine.

Katika mfano, kithibitishaji `c_2` kinahitaji tu Hash ya kati (`tH_MPC_LEAF(D)`), `tH_MPC_BRANCH(...)` mbili, `pos(c_2)` uthibitisho wa nafasi na thamani `cofactor`. Kisha inaweza kuunda upya mzizi ndani ya nchi, kisha kukokotoa upya `mpc::Commitment` na kuilinganisha na ile iliyoandikwa katika shughuli ya Bitcoin (ndani ya `Opret` au `Tapret`).

![RGB-Bitcoin](assets/fr/054.webp)

Utaratibu huu unahakikisha kuwa:


- Hali inayohusiana na `c_2` kwa hakika imejumuishwa katika uzuiaji wa taarifa wa jumla (upande wa mteja);
- Hakuna mtu anayeweza kuunda historia mbadala kwa shughuli sawa, kwa sababu On-Chain _commitment_ inaelekeza kwenye mzizi mmoja wa MPC.

#### Muhtasari wa muundo wa MPC

Multi Protocol Commitment* (MPC) ndiyo kanuni inayowezesha RGB kujumlisha mikataba mingi katika muamala mmoja wa Bitcoin, huku ikidumisha upekee wa ahadi na usiri dhidi ya washiriki wengine. Shukrani kwa ujenzi wa kuamua wa mti, kila Contract imepewa nafasi ya pekee, na uwepo wa majani ya "dummy" (*Majani ya Entropy*) hufunika kwa sehemu idadi ya mikataba inayoshiriki katika shughuli hiyo.

Merkle Tree nzima haihifadhiwi kwenye mteja. Sisi kwa urahisi generate a _Merkle path_ kwa kila Contract inayohusika, kutumwa kwa mpokeaji (ambaye anaweza kuthibitisha Commitment). Katika baadhi ya matukio, unaweza kuwa na mali kadhaa ambazo zimepitia UTXO sawa. Kisha unaweza kuunganisha _Merkle paths_ kadhaa kwenye kinachojulikana kama _multi-protocol Commitment block_, ili kuepuka kunakili data nyingi.

Kwa hivyo, kila _Merkle proof_ ni nyepesi, haswa kwa vile kina cha mti hakitazidi 32 katika RGB. Pia kuna dhana ya "Merkle block", ambayo huhifadhi maelezo zaidi (sehemu nzima, entropy, nk.), muhimu kwa kuchanganya au kutenganisha matawi kadhaa.

Ndiyo maana ilichukua muda mrefu kukamilisha RGB. Tulikuwa na maono ya jumla kutoka 2019: kuweka kila kitu kwa upande wa mteja, kusambaza tokeni za off-chain. Lakini kwa maelezo kama vile kugawanya kandarasi nyingi, muundo wa Merkle Tree, jinsi ya kushughulikia migongano na uunganisho wa uthibitisho... yote haya yalihitaji marudio.

### Nanga: mkutano wa kimataifa

Kufuatia ujenzi wa ahadi zetu (`Opret` au `Tapret`) na MPC wetu (*Multi Protocol Commitment*), tunahitaji Address dhana ya **Anchor** katika itifaki ya RGB. Anchor ni muundo ulioidhinishwa wa upande wa mteja ambao unaleta pamoja Elements inayohitajika ili kuthibitisha kuwa Bitcoin Commitment kweli ina maelezo mahususi ya kimkataba. Kwa maneno mengine, Anchor inatoa muhtasari wa data yote inayohitajika ili kuthibitisha _commitments_ ilivyoelezwa hapo juu.

Anchor ina sehemu tatu zilizoagizwa:


- `txid`
- `Ushahidi wa MPC`
- Uthibitisho wa Muamala wa ziada - ETP

Kila moja ya sehemu hizi ina sehemu katika mchakato wa uthibitishaji, iwe ni suala la kuunda upya shughuli ya msingi ya Bitcoin au kuthibitisha kuwepo kwa Commitment iliyofichwa (hasa katika kesi ya `Tapret`).

#### txid

Sehemu ya `txid` inalingana na kitambulishi cha baiti 32 cha shughuli ya Bitcoin iliyo na `Opret` au `Tapret` Commitment.

Kinadharia, itawezekana kupata `txid` hii kwa kufuatilia msururu wa mabadiliko ya serikali ambayo yenyewe yanaelekeza kwa kila Witness Transaction, kwa kufuata mantiki ya Mihuri ya Matumizi Moja. Hata hivyo, ili kuwezesha na kuharakisha uthibitishaji, `txid` hii imejumuishwa kwa urahisi kwenye Anchor, hivyo basi kuokoa kiidhinishi kutokana na kurudi nyuma kupitia historia nzima ya off-chain.

#### Ushahidi wa MPC

Sehemu ya pili, `Uthibitisho wa MPC`, inarejelea uthibitisho kwamba Contract hii mahususi (k.m. `c_i`) imejumuishwa katika _Ahadi ya Itifaki nyingi_. Ni mchanganyiko wa:


- `pos_i`, nafasi ya Contract hii katika mti wa MPC;
- cofactor`, thamani iliyobainishwa ili kutatua migongano ya nafasi;
- `Uthibitisho wa Merkle`, yaani seti ya vifundo na heshi zilizotumiwa kuunda upya mzizi wa MPC na kuthibitisha kuwa kitambulishi cha Contract na `Transition Bundle` yake zimekabidhiwa kwenye mzizi.

Utaratibu huu ulielezewa katika sehemu iliyotangulia ya kujenga *Mti wa MPC*, ambapo kila Contract inapata jani la kipekee kutokana na:

```txt
pos(c_i) = c_i mod (w - cofactor)
```

Kisha, mpango wa merkelization wa kuamua hutumiwa kukusanya majani yote (mikataba + entropy). Mwishowe, `Uthibitisho wa MPC` huruhusu mzizi kujengwa upya ndani ya nchi na ikilinganishwa na `mpc::Commitment` iliyojumuishwa On-Chain.

#### Uthibitisho wa Muamala wa Ziada - ETP

Sehemu ya tatu, **ETP**, inategemea aina ya Commitment iliyotumiwa. Ikiwa Commitment ni ya aina ya `Opret`, hakuna uthibitisho wa ziada unaohitajika. Kihalalishi hukagua matokeo ya kwanza ya `OP_RETURN` ya muamala na kupata `mpc::Commitment` moja kwa moja hapo.

**Ikiwa Commitment ni ya aina ya `Tapret`**, uthibitisho wa ziada unaoitwa *Uthibitisho wa Muamala wa Ziada - ETP* lazima utolewe. Ina:


- Ufunguo wa ndani wa umma (`P`) wa pato la Taproot ambamo *Commitment* imepachikwa;
- Nodi za washirika za `Njia ya Hati Tumia` (wakati Tapret *Commitment* inapoingizwa kwenye hati), ili kuthibitisha eneo kamili la hati hii katika mti wa Taproot:
 - Ikiwa `Tapret` *Commitment* iko kwenye tawi la mkono wa kulia, tunafichua nodi ya mkono wa kushoto (k.m. `thHABC`),
 - Ikiwa `Tapret` *Commitment* iko upande wa kushoto, unahitaji kufichua nodi 2 (k.m. `tHAB` na `tHC`) ili kuthibitisha kuwa hakuna *Commitment* nyingine iliyopo upande wa kulia.
- `Nonce` inaweza kutumika "kuchimba" usanidi bora zaidi, ikiruhusu *Commitment* kuwekwa upande wa kulia wa mti (uboreshaji wa uthibitisho).

Uthibitisho huu wa ziada ni muhimu kwa sababu, tofauti na `Opret`, `Tapret` Commitment imeunganishwa katika muundo wa hati ya Taproot, ambayo inahitaji kufichuliwa kwa sehemu ya mti wa Taproot ili kuthibitisha kwa usahihi eneo la *Commitment*.

![RGB-Bitcoin](assets/fr/045.webp)

**Nanga** kwa hivyo hujumuisha taarifa zote zinazohitajika ili kuthibitisha Bitcoin Commitment katika muktadha wa RGB. Zinaonyesha muamala husika (`txid`) na uthibitisho wa nafasi ya Contract (`Uthibitisho wa MPC`), huku zikidhibiti uthibitisho wa ziada (`ETP`) katika kesi ya `Tapret`. Kwa njia hii, Anchor inalinda uadilifu na upekee wa hali ya off-chain kwa kuhakikisha kuwa shughuli hiyo hiyo haiwezi kufasiriwa upya kwa data nyingine za mkataba.

### Hitimisho

Katika sura hii, tunashughulikia:


- Jinsi ya kutumia dhana ya Mihuri ya matumizi Moja katika Bitcoin (haswa kupitia _outpoint_);
- Mbinu mbalimbali za kubainisha _ahadi_ katika muamala (Sig tweak, Key tweak, tweak ya mashahidi, OP_RETURN, Taproot/Tapret);
- Sababu kwa nini RGB inazingatia ahadi za Tapret;
- Usimamizi wa Contract nyingi kupitia _ahadi za itifaki nyingi_, ni muhimu ikiwa hutaki kufichua jimbo zima au mikataba mingine unapotaka kuthibitisha hoja mahususi;
- Tumeona pia jukumu la _Anchors_, ambayo huleta kila kitu pamoja (muamala txid, uthibitisho wa Merkle Tree na uthibitisho wa Taproot) katika kifurushi kimoja.

Katika mazoezi, utekelezaji wa kiufundi umegawanywa kati ya Rust _crates_ kadhaa maalum (katika _client_side_validation_, _commit-verify_, _bp_core_, nk.). Mawazo ya kimsingi yapo:

![RGB-Bitcoin](assets/fr/046.webp)

Katika sura inayofuata, tutaangalia sehemu ya off-chain ya RGB, ambayo ni mantiki ya Contract. Tutaona jinsi mikataba ya RGB, iliyopangwa kama mashine za hali _finite iliyoigwa kwa sehemu_, inavyofikia uwazi zaidi kuliko hati za Bitcoin, huku zikihifadhi usiri wa data zao.

## Utangulizi wa mikataba mahiri na majimbo yao

<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

:::video id=db4ee09f-1352-4ad1-9f7a-c962df7ea9fa:::

Katika sura hii na inayofuata, tutaangalia dhana ya **Smart contract** ndani ya mazingira ya RGB na kuchunguza njia tofauti ambazo mikataba hii inaweza kufafanua na kubadilisha *hali* yao. Tutaona ni kwa nini usanifu wa RGB, kwa kutumia mfuatano ulioagizwa wa Mihuri ya Matumizi Moja, kuwezesha kutekeleza aina mbalimbali za ***Operesheni za Contract*** kwa njia inayoweza kusambazwa na bila kupitia sajili ya kati. Pia tutaangalia jukumu la msingi la ***Business Logic*** katika kutunga mageuzi ya Contract State.

### Mikataba mahiri na haki za mshikaji dijitali

Lengo la RGB ni kutoa miundombinu ya kutekeleza mikataba mahiri kwenye Bitcoin. Kwa "Smart contract" tunamaanisha makubaliano kati ya wahusika kadhaa ambayo yanatekelezwa kiotomatiki na kwa kukokotoa, bila uingiliaji wa kibinadamu ili kutekeleza vifungu. Kwa maneno mengine, sheria ya Contract inatekelezwa na programu, sio na mtu wa tatu anayeaminika.

Uendeshaji huu otomatiki huibua swali la ugatuaji: tunawezaje kujikomboa kutoka kwa sajili kuu (k.m. jukwaa kuu au hifadhidata) ili kudhibiti utendaji wa Ownership na Contract? Wazo la asili, lililochukuliwa na RGB, ni kurejea kwenye hali ya Ownership inayojulikana kama "vyombo vya kubeba". Kihistoria, dhamana fulani (bondi, hisa, n.k.) zilitolewa kwa namna ya mhusika, kuwezesha mtu yeyote ambaye ana hati hiyo kutekeleza haki zake.

![RGB-Bitcoin](assets/fr/055.webp)

RGB inatumia dhana hii kwa ulimwengu wa kidijitali: haki (na wajibu) zimejumuishwa katika data ambayo inabadilishwa off-chain, na hali ya data hii inathibitishwa na washiriki wenyewe. Hii inaruhusu, kipaumbele, kiwango kikubwa zaidi cha usiri na uhuru kuliko ile inayotolewa na mbinu nyingine kulingana na rejista za umma.

### Utangulizi wa hali ya Smart contract RGB

Smart contract katika RGB inaweza kuonekana kama mashine ya serikali, iliyofafanuliwa na:


- A **Jimbo**, yaani seti ya taarifa inayoonyesha usanidi wa sasa wa Contract;
- A **Business Logic** (seti ya sheria), ambayo inaelezea chini ya hali gani na nani serikali inaweza kurekebishwa.

![RGB-Bitcoin](assets/fr/056.webp)

Ni muhimu kuelewa kwamba mikataba hii sio mdogo kwa uhamisho rahisi wa ishara. Zinaweza kujumuisha aina mbalimbali za matumizi: kutoka kwa mali ya kitamaduni (ishara, hisa, bondi) hadi ufundi changamano zaidi (haki za matumizi, masharti ya kibiashara, n.k.). Tofauti na minyororo mingine ya kuzuia, ambapo msimbo wa Contract unapatikana na kutekelezwa na wote, mbinu ya RGB inagawanya upatikanaji na ujuzi wa Contract kwa washiriki ("***Contract washiriki***"). Kuna majukumu kadhaa:


- Mtoaji** au muundaji wa Contract, ambaye anafafanua Genesis ya Contract na vigezo vyake vya awali;
- Vyama vilivyo na haki** (*Ownership*) au uwezo mwingine wa kutekeleza ;
- Waangalizi**, wana uwezekano mdogo wa kuona taarifa fulani, lakini ambao hawawezi kuanzisha marekebisho.

Mgawanyo huu wa majukumu huchangia upinzani wa udhibiti, kwa kuhakikisha kuwa watu walioidhinishwa pekee ndio wanaoweza kuingiliana na hali ya kimkataba. Pia huipa RGB uwezo wa kuongeza mlalo: uthibitishaji mwingi hufanyika nje ya Blockchain, na ni nanga za kriptografia pekee (*ahadi*) zimeandikwa kwenye Bitcoin.

### Hali na Business Logic katika RGB

Kwa mtazamo wa vitendo, Contract ya **Business Logic** inachukua fomu ya sheria na maandishi, iliyofafanuliwa katika kile RGB inachokiita **Schema**. Nambari za Schema:


- Muundo wa serikali (ni nyanja zipi ni za umma? Ni nyanja zipi zinamilikiwa na vyama gani?
- Masharti ya uhalali (ni nini kinachopaswa kuangaliwa kabla ya kuidhinisha sasisho la hali?);
- Uidhinishaji (nani anaweza kuanzisha *State Transition*? Ni nani anayeweza kuangalia tu?).

Wakati huo huo, **Contract State** mara nyingi hugawanyika katika vipengele viwili:


- A **Global State**: sehemu ya umma, ambayo inaweza kuonekana na wote (kulingana na usanidi);
- Nchi Zinazomilikiwa**: sehemu za siri, zilizotengwa mahususi kwa wamiliki kupitia UTXO zilizorejelewa katika mantiki ya Contract.

Kama tutakavyoona katika sura zifuatazo, sasisho lolote la hali (*Contract Operation*) lazima liambatishwe kwenye Bitcoin _ahadi_ (kupitia `Opret` au `Tapret`) na litii hati za *Business Logic* ili kuchukuliwa kuwa halali.

### Uendeshaji wa Contract: uundaji na mageuzi ya Serikali

Katika ulimwengu wa RGB, ***Contract Operation*** ni tukio lolote linalobadilisha Contract kutoka **hali ya zamani** hadi **hali mpya**. Operesheni hizi hufuata mantiki ifuatayo:


- Tunazingatia hali ya sasa ya Contract;
- Tunatumia sheria au uendeshaji (**State Transition***, ***Genesis*** ikiwa ni hali ya kwanza kabisa, au ***State Extension*** ikiwa kuna *Valency* ya umma ya kuwasha tena);
- Sisi Anchor marekebisho kupitia _ahadi_ mpya kwenye Blockchain, kufunga _seal-matumizi moja_ na kuunda nyingine;
- Wamiliki wa haki wanaohusika wanathibitisha ndani ya nchi (*upande wa mteja*) kwamba mageuzi yanafuata *Schema* na kwamba muamala husika wa Bitcoin umesajiliwa On-Chain.

![RGB-Bitcoin](assets/fr/057.webp)

Matokeo yake ni Contract iliyosasishwa, sasa ikiwa na hali tofauti. Mpito huu hauhitaji mtandao mzima wa Bitcoin kuhusika na maelezo, kwa kuwa ni alama ndogo ya kriptografia tu (the _commitment_) iliyorekodiwa katika Blockchain. Mfuatano wa Mihuri ya Matumizi Moja huzuia matumizi yoyote ya Double-spending au mara mbili ya Serikali.

### Mlolongo wa uendeshaji: kutoka Genesis hadi Jimbo la Terminal

Ili kuweka hili katika mtazamo, RGB Smart contract huanza na **Genesis**, hali ya kwanza kabisa. Baada ya hapo, Operesheni mbalimbali za Contract zinafuatana, na kutengeneza DAG (*Directed Acyclic Graph*) ya uendeshaji:


- Kila mpito inategemea hali ya awali (au kadhaa, katika kesi ya mabadiliko ya kuunganishwa);
- Mpangilio wa mpangilio unahakikishwa na kuingizwa kwa kila mpito katika Bitcoin Anchor, shukrani za muda na zisizoweza kubadilika kwa makubaliano na Proof-of-Work;
- Wakati hakuna shughuli zaidi zinazoendelea, **Jimbo la Kituo** hufikiwa: hali ya hivi punde zaidi na kamili ya Contract.

![RGB-Bitcoin](assets/fr/012.webp)

Topolojia hii ya DAG (badala ya msururu rahisi wa mstari) inaonyesha uwezekano kwamba sehemu tofauti za Contract zinaweza kubadilika kwa sambamba, mradi hazipingani. RGB basi hujihadhari ili kuepuka mikanganyiko yoyote kwa uthibitishaji wa *upande wa mteja* wa kila mshiriki anayehusika.

### Muhtasari

Mikataba mahiri katika RGB inatanguliza muundo wa zana zinazobeba dijitali, zilizogatuliwa lakini zilizowekwa katika Bitcoin kwa kuweka muhuri wa wakati na kuhakikisha mpangilio wa miamala. Utekelezaji wa kiotomatiki wa mikataba hii inategemea:


- A **Contract State*, inayoonyesha usanidi wa sasa wa Contract (haki, mizani, vigezo, nk);
- A **Business Logic** (*Schema*), ikifafanua ni mabadiliko gani yanaruhusiwa na jinsi yanapaswa kuthibitishwa;
- Contract Operations**, ambayo husasisha jimbo hili hatua kwa hatua, kutokana na ahadi zilizowekwa katika miamala ya Bitcoin.

Katika sura inayofuata, tutaingia kwa undani zaidi kuhusu uwakilishi halisi wa hizi ***states*** na ***mabadiliko ya serikali*** katika kiwango cha off-chain, na jinsi zinavyohusiana na UTXO na Mihuri ya Matumizi Moja iliyopachikwa kwenye Bitcoin. Hii itakuwa fursa ya kuona jinsi mitambo ya ndani ya RGB, kulingana na Client-side Validation, inavyoweza kudumisha uthabiti wa mikataba mahiri huku ikihifadhi usiri wa data.

## Shughuli za RGB Contract

<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

:::video id=1caec34d-f214-425b-a1a4-0a40ae7d3e0e:::

Katika sura hii, tutaangalia jinsi utendakazi katika mikataba mahiri na mabadiliko ya serikali hufanya kazi, tena ndani ya itifaki ya RGB. Lengo pia litakuwa kuelewa jinsi washiriki kadhaa wanavyoshirikiana kuhamisha Ownership ya mali.

### Mabadiliko ya serikali na mechanics yao

Kanuni ya jumla bado ni ile ya Client-side Validation, ambapo data ya serikali inashikiliwa na mmiliki na kuthibitishwa na mpokeaji. Hata hivyo, umaalum hapa na RGB unatokana na ukweli kwamba Bob, kama mpokeaji, anamwomba Alice kujumuisha taarifa fulani kwenye data ya Contract ili kuwa na udhibiti wa kweli wa mali iliyopokelewa, kupitia rejeleo lililofichwa kwa mojawapo ya UTXO zake.

Ili kuonyesha mchakato wa *State Transition* (ambayo ni mojawapo ya Operesheni za msingi za ***Contract*** katika RGB), hebu tuchukue mfano wa hatua kwa hatua wa uhamisho wa mali kati ya Alice na Bob:

**Hali ya awali:**

Alice ana ***Stash RGB*** ya data iliyothibitishwa ndani ya nchi (*upande wa mteja*). Stash hii inarejelea moja ya UTXO zake kwenye Bitcoin. Hii inamaanisha kuwa _seal definition_ katika data hii inaelekeza kwa UTXO mali ya Alice. Wazo ni kumwezesha kuhamisha haki fulani za kidijitali zilizounganishwa na mali (k.m. tokeni za RGB) hadi kwa Bob.

![RGB-Bitcoin](assets/fr/058.webp)

**Bob pia ana UTXOs:**

Bob, kwa upande mwingine, ana angalau UTXO yake mwenyewe, bila kiungo cha moja kwa moja kwa Alice. Katika tukio ambalo Bob hana UTXO, bado inawezekana kufanya uhamisho kwake kwa kutumia *Witness Transaction* yenyewe: matokeo ya shughuli hii itajumuisha Commitment (_commitment_) na kuhusisha kwa uwazi Ownership ya Contract mpya na Bob.

![RGB-Bitcoin](assets/fr/059.webp)

**Ujenzi wa mali mpya (*Jimbo Jipya*):**

Bob hutuma maelezo ya Alice yaliyosimbwa kwa njia ya ***Invoice*** (tutaingia kwa undani zaidi kuhusu ujenzi wa Invoice katika sura za baadaye), akimwomba aunde hali mpya ambayo inalingana na sheria za Contract. Jimbo hili litajumuisha *Seal Definition* mpya inayoelekeza kwenye mojawapo ya UTXO za Bob. Kwa njia hii, Bob anapewa Ownership ya mali iliyoelezwa katika hali hii mpya, kwa mfano kiasi fulani cha ishara za RGB.

![RGB-Bitcoin](assets/fr/060.webp)

**Maandalizi ya sampuli ya muamala:**

Kisha Alice huunda muamala wa Bitcoin akitumia UTXO iliyorejelewa katika Seal iliyotangulia (ile iliyomhalalisha kama mmiliki). Katika matokeo ya muamala huu, *Commitment* (kupitia `Opret` au `Tapret`) imeingizwa kwenye Anchor hali mpya ya RGB. Ahadi za `Opret` au `Tapret` zimetokana na *Mti wa MPC* (kama inavyoonekana katika sura zilizopita), ambao unaweza kujumlisha mabadiliko kadhaa kutoka kwa mikataba tofauti.

**Usambazaji wa *Consignment* kwa Bob:**

Kabla ya kutangaza muamala, Alice humtumia Bob ***Consignment*** iliyo na data yote muhimu ya *upande wa mteja* (*Stash* yake) na taarifa mpya ya jimbo kwa niaba ya Bob. Katika hatua hii, Bob anatumia sheria za makubaliano ya RGB:


- Inathibitisha data yote ya RGB iliyo katika *Consignment*, ikijumuisha hali mpya inayoipatia Ownership ya mali;
- Kwa kutegemea *Nanga* zilizojumuishwa katika *Consignment*, inathibitisha mpangilio wa shughuli za mashahidi (kutoka Genesis hadi mpito wa hivi majuzi) na kuthibitisha ahadi zinazolingana katika Blockchain.

**Kukamilika kwa Mpito:**

Ikiwa Bob ameridhika, anaweza kutoa kibali chake (kwa mfano, kwa kusaini *Consignment*). Kisha Alice anaweza kutangaza shughuli ya sampuli iliyotayarishwa. Baada ya kuthibitishwa, hii inafunga Seal iliyoshikiliwa hapo awali na Alice na kurasimisha Ownership na Bob. Usalama wa Anti-Double-spending basi unategemea utaratibu sawa na katika Bitcoin: UTXO inatumika, kuthibitisha kwamba Alice hawezi tena kuitumia tena.

![RGB-Bitcoin](assets/fr/061.webp)

Jimbo hilo jipya sasa linarejelea UTXO ya Bob, ikimpa Bob Ownership iliyokuwa ikishikiliwa na Alice. Pato la Bitcoin ambapo data ya RGB imetiwa nanga inakuwa dhibitisho lisiloweza kubatilishwa la uhamisho wa Ownership.

Mfano wa DAG ndogo (*Directed Acyclic Graph*) inayojumuisha oparesheni mbili za Contract (**Genesis** kisha ***State Transition***) inaweza kuonyesha jinsi hali ya RGB (*upande wa mteja* Layer, kwa rangi nyekundu) inavyounganishwa na Commitment5-7335 GW7*735 GW, 733 GW-7, GW-7 machungwa).

![RGB-Bitcoin](assets/fr/062.webp)

Inaonyesha kuwa Genesis inafafanua Seal (*Seal Definition*), kisha *State Transition* inafunga Seal hii ili kuunda mpya katika UTXO nyingine.

Katika muktadha huu, hapa kuna vikumbusho vichache vya istilahi:


- ***Assignment*** inachanganya :
    - A ***Seal Definition*** (ambayo inaashiria UTXO);
    - Mataifa Yanayomilikiwa**, yaani, data iliyounganishwa na Ownership (kwa mfano, idadi ya tokeni zilizohamishwa).
- **Global State** huleta pamoja sifa za jumla za Contract, zinazoonekana kwa wote, na kuhakikisha uwiano wa kimataifa wa mageuzi.

Mpito wa Jimbo**, ulioelezewa katika sura iliyopita, ni aina kuu ya Contract Operation. Wanarejelea jimbo moja au zaidi zilizopita (kutoka Genesis au State Transition nyingine) na wanasasisha hadi hali mpya.

![RGB-Bitcoin](assets/fr/063.webp)

Mchoro huu unaonyesha jinsi, katika *Jimbo Transition Bundle*, mihuri kadhaa inaweza kufungwa katika shughuli ya sampuli moja, wakati huo huo kufungua mihuri mpya. Kwa hakika, kipengele cha kuvutia cha itifaki ya RGB ni uwezo wake wa kupima: mabadiliko kadhaa yanaweza kuunganishwa kuwa Transition Bundle, kila mkusanyiko ukihusishwa na jani tofauti la *mti wa MPC* (kitambulisho cha kipekee cha kifungu). Shukrani kwa utaratibu wa *Deterministic Bitcoin Commitment* (DBC), ujumbe wote unaingizwa kwenye towe la `Tapret` au `Opret`, huku ukifunga mihuri iliyotangulia na ikiwezekana kubainisha mipya. `Anchor* hutumika kama kiungo cha moja kwa moja kati ya Commitment iliyohifadhiwa katika Blockchain na muundo wa Client-side Validation (*upande wa mteja*).

Katika sura zifuatazo, tutaangalia vipengele na taratibu zote zinazohusika katika kujenga na kuhalalisha State Transition. Nyingi za hizi Elements ni sehemu ya makubaliano ya RGB, yanayotekelezwa katika **RGB Core Library**.

### Transition Bundle

Kwenye RGB, inawezekana kuunganisha Mipito tofauti ya Jimbo inayomilikiwa na Contract sawa (yaani, kushiriki **ContractId** sawa, inayotokana na Genesis **OpId**). Katika hali rahisi, kama kati ya Alice na Bob katika mfano hapo juu, **Transition Bundle** ina mpito mmoja tu. Lakini usaidizi wa shughuli za walipaji wengi (kama vile coinjoins, fursa za vituo vya umeme, n.k.) inamaanisha kuwa watumiaji kadhaa wanaweza kuchanganya Mpito wa Jimbo lao katika kifungu kimoja.

Mara baada ya kukusanywa, mabadiliko haya yameimarishwa (na utaratibu wa MPC + DBC) katika shughuli moja ya Bitcoin:


- Kila State Transition imeharakishwa na kuunganishwa katika Transition Bundle;
- Transition Bundle yenyewe imeharakishwa na kuingizwa kwenye jani la mti la MPC linalolingana na hii Contract (BundleId);
- Mti wa MPC hatimaye unahusishwa kupitia `Opret` au `Tapret` katika Witness Transaction, ambayo kwa hivyo hufunga sili zinazotumiwa na kufafanua mihuri mipya.

Kwa kusema kitaalamu, **BundleId** iliyoingizwa kwenye laha ya MPC inapatikana kutoka kwa alama ya Hash iliyotumika kwa ufuataji kamili wa sehemu ya *InputMap* ya kifungu:

```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```

Ambapo `bundle_tag = urn:lnp-bp:RGB:bundle#2024-02-03` kwa mfano.

*InputMap* ni muundo wa data unaoorodhesha, kwa kila ingizo `i` la sampuli ya muamala, marejeleo ya *OpId* ya State Transition inayolingana. Kwa mfano:

```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|
MapElement1                MapElement2                       MapElementN
```


- `N` ni jumla ya idadi ya maingizo katika muamala yanayorejelea `OpId`;
- opId(input_j)` ni kitambulisho cha operesheni ya mojawapo ya Mpito za Serikali zilizopo kwenye kifurushi.

Kwa kurejelea kila ingizo mara moja tu na kwa utaratibu, tunazuia Seal ile ile isitumike mara mbili katika Mipito miwili ya Serikali kwa wakati mmoja.

### Kizazi cha Jimbo na Jimbo Amilifu

Kwa hivyo Mpito wa Jimbo unaweza kutumika kuhamisha Ownership ya mali kutoka kwa mtu mmoja hadi kwa mwingine. Walakini, sio shughuli pekee zinazowezekana katika itifaki ya RGB. Itifaki inafafanua tatu **Uendeshaji wa Contract** :


- State Transition** ;
- Genesis** ;
- State Extension**.

Kati ya hizi, **Genesis** na **State Extension** wakati mwingine huitwa "*Shughuli za Kizazi cha Jimbo*", kwa sababu huunda majimbo mapya bila kufunga yoyote mara moja. Hili ni jambo muhimu sana: **Genesis** na **State Extension** hazihusishi kufunga Seal. Badala yake, wanafafanua Seal mpya, ambayo lazima itumike na **State Transition** inayofuata ili kuthibitishwa kweli katika historia ya Blockchain.

![RGB-Bitcoin](assets/fr/064.webp)

**Hali Inayotumika** ya Contract mara nyingi hufafanuliwa kuwa seti ya majimbo ya hivi punde kutokana na historia (DAG) ya miamala, kuanzia Genesis na kufuata nanga zote katika Bitcoin Blockchain. Majimbo yoyote ya zamani ambayo tayari yamepitwa na wakati (yaani yaliyoambatishwa kwa UTXO zilizotumika) hayachukuliwi kuwa hai, lakini yanasalia kuwa muhimu kwa kuangalia uthabiti wa historia.

### Genesis

Genesis ndio mahali pa kuanzia kwa kila RGB Contract. Imeundwa na mtoaji wa Contract na hufafanua vigezo vya awali, kwa mujibu wa **Schema**. Kwa upande wa ishara ya RGB, Genesis inaweza kutaja, kwa mfano:


- Idadi ya ishara zilizoundwa awali na wamiliki wao;
- Jumla ya suala linalowezekana dari;
- Sheria zozote za kutoa upya, na ni washiriki gani wanastahiki.

Kwa kuwa ni shughuli ya kwanza katika Contract, Genesis hairejelei hali yoyote ya awali, wala haifungi Seal yoyote. Hata hivyo, ili kuonekana kwenye historia na kuthibitishwa, Genesis lazima **itumike** (imefungwa) na State Transition ya kwanza (mara nyingi ni shughuli ya kuchanganua/kutumia kiotomatiki kwa mtoaji yenyewe, au usambazaji wa awali kwa watumiaji).

### State Extension

Viendelezi vya Jimbo** hutoa kipengele asili kwa mikataba mahiri. Wanawezesha Redeem haki fulani za kidijitali (*Valencies*) zinazotolewa katika ufafanuzi wa Contract, bila kufunga Seal mara moja. Mara nyingi, hii inahusu:


- Masuala ya ishara iliyosambazwa;
- Taratibu za kubadilisha mali;
- Matoleo mapya ya masharti (ambayo yanaweza kujumuisha uharibifu wa mali nyingine, nk).

Kitaalamu, State Extension inarejelea *Redeem* (aina fulani ya RGB) ambayo inalingana na *Valency* iliyofafanuliwa hapo awali (kwa mfano, katika Genesis au State Transition nyingine). Inafafanua Seal mpya, inayopatikana kwa mtu au hali inayonufaika nayo. Ili Seal hii ifanye kazi, ni lazima itumike na State Transition inayofuata.

![RGB-Bitcoin](assets/fr/065.webp)

Kwa mfano: Genesis inaunda haki ya kutoa (*Valency*). Hii inaweza kutekelezwa na mwigizaji aliyeidhinishwa, ambaye kisha huunda State Extension :


- Inahusu Valency (Redeem);
- Inaunda *Assignment* mpya (data mpya ya *Owned State*) inayoelekeza kwenye UTXO ;
- State Transition ya baadaye, iliyotolewa na mmiliki wa UTXO hii mpya, itahamisha au kusambaza tokeni mpya zilizotolewa.

### Sehemu ya Contract Operation

Ningependa sasa kuangalia kwa kina kila mojawapo ya sehemu za Elements za **Contract Operation** katika RGB. Contract Operation ni hatua ambayo hurekebisha hali ya Contract, na ambayo inathibitishwa kwa upande wa mteja, kwa njia ya kuamua, na mpokeaji halali. Hasa, tutaona jinsi Contract Operation inavyozingatia, kwa upande mmoja, ** hali ya zamani ** ( * Jimbo la Kale * ) la Contract, na kwa upande mwingine, ufafanuzi wa ** hali mpya ** ( * Jimbo Mpya * ).

```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
```

Tukiangalia mchoro hapo juu, tunaweza kuona kwamba Contract Operation inajumuisha Elements inayorejelea **Jimbo Jipya** na zingine zikirejelea **Jimbo la Kale** lililosasishwa.

Elements ya **Jimbo Jipya** ni:


- Kazi**, ambazo zimefafanuliwa:
 - **Seal Definition**;
 - **Owned State**.
- **Global State**, ambayo inaweza kurekebishwa au kuimarishwa;
- Valencies**, ikiwezekana kufafanuliwa katika State Transition au Genesis.

**Jimbo la Kale** linarejelewa kupitia:


- Ingizo**, zinazoelekeza kwenye *Kazi* za mabadiliko ya awali ya hali (hazipo katika Genesis);
- Hukomboa**, ambayo inarejelea Uhalali uliobainishwa awali (katika Viendelezi vya Jimbo pekee).

Kwa kuongezea, Contract Operation inajumuisha nyanja za jumla zaidi maalum kwa operesheni:


- ffv` (*Toleo la kusonga mbele kwa haraka*): nambari kamili ya baiti 2 inayoonyesha toleo la Contract;
- transitionType` au ExtensionType`: nambari kamili ya biti 16 inayobainisha aina ya Mpito au Kiendelezi, kulingana na Business Logic;
- `Id ya Mkataba`: nambari ya baiti 32 inayorejelea *OpId* ya Contract Genesis. Imejumuishwa katika Mpito na Viendelezi, lakini si katika Genesis;
- schemaId: iliyopo tu katika Genesis, hii ni Hash ya 32-byte inayowakilisha muundo (*Schema*) wa Contract;
- Testnet`: Boolean ikionyesha kama uko kwenye mtandao wa Testnet au Mainnet. Genesis pekee;
- altlayers1`: kigezo kinachobainisha Layer mbadala (Sidechain au nyingine) inayotumika kwa data ya Anchor pamoja na Bitcoin. Ipo tu katika Genesis;
- metadata": sehemu inayoweza kuhifadhi maelezo ya muda, muhimu kwa kuthibitisha changamano ya Contract, lakini ambayo haipaswi kurekodiwa katika historia ya hali ya mwisho.

Hatimaye, sehemu hizi zote zimefupishwa kwa mchakato wa kurudisha nyuma uliogeuzwa kukufaa, ili kutoa alama ya kidole ya kipekee, `OpId`. `OpId` hii basi inaunganishwa kwenye Transition Bundle, na kuiwezesha kuthibitishwa na kuthibitishwa ndani ya itifaki.

Kwa hivyo kila *Contract Operation* inatambuliwa na Hash ya 32-byte iitwayo `OpId`. Hash hii imekokotolewa na SHA256 Hash ya Elements zote zinazounda operesheni. Kwa maneno mengine, kila *Contract Operation* ina Commitment yake ya kriptografia, ambayo inajumuisha data yote inayohitajika ili kuthibitisha uhalisi na uthabiti wa operesheni.

RGB Contract basi hutambuliwa kwa `ContractId`, inayotokana na Genesis `OpId` (kwa kuwa hakuna operesheni ya kabla ya Genesis). Kwa maneno madhubuti, tunachukua Genesis `OpId`, kubadilisha mpangilio wa baiti na kutumia usimbaji wa Base58. Usimbaji huu hurahisisha `ContractId` kushughulikia na kutambua.

### Mbinu na sheria za kusasisha hali

**Contract State** inawakilisha seti ya maelezo ambayo itifaki ya RGB lazima ifuatilie kwa Contract fulani. Inaundwa na:


- Global State** moja: hii ni sehemu ya umma, ya kimataifa ya Contract, inayoonekana kwa wote;
- Nchi Moja au zaidi Zinazomilikiwa**: kila Owned State inahusishwa na Seal ya kipekee (na kwa hivyo UTXO kwenye Bitcoin). Tofauti inafanywa kati ya:
    - **Nchi zinazomilikiwa na umma**,
    - **Nchi zinazomilikiwa** za Kibinafsi.

![RGB-Bitcoin](assets/fr/066.webp)

*Global State* imejumuishwa moja kwa moja kwenye *Contract Operation* kama kizuizi kimoja. *Nchi Zinazomilikiwa* zimefafanuliwa katika kila *Assignment*, sambamba na *Seal Definition*.

Kipengele kikuu cha RGB ni njia ambayo Global State na Mataifa Yanayomilikiwa yanarekebishwa. Kwa ujumla kuna aina mbili za tabia:


- Inaweza kubadilika**: kipengele cha hali kinapofafanuliwa kuwa kinaweza kubadilika, kila operesheni mpya inachukua nafasi ya hali ya awali na hali mpya. Data ya zamani basi inachukuliwa kuwa ya kizamani;
- Kukusanya**: kipengele cha hali kinapofafanuliwa kuwa ni mkusanyiko, kila operesheni mpya huongeza taarifa mpya kwa hali ya awali, bila kuibadilisha. Matokeo yake ni aina ya historia iliyokusanywa.

Ikiwa, katika Contract, kipengele cha hali hakijafafanuliwa kuwa kinachoweza kubadilika au limbikizi, kipengele hiki kitasalia tupu kwa shughuli zinazofuata (kwa maneno mengine, hakuna matoleo mapya ya uga huu). Ni Contract Schema (yaani Business Logic) yenye msimbo ambayo huamua ikiwa jimbo (Jumla au Linalomilikiwa) linaweza kubadilika, kujumlisha au kudumu. Mara tu Genesis imefafanuliwa, mali hizi zinaweza kubadilishwa tu ikiwa Contract yenyewe inaruhusu, kwa mfano kupitia State Extension maalum.

Jedwali hapa chini linaonyesha jinsi kila aina ya Contract Operation inaweza kuendesha (au la) Global State na Owned State:

|                              | Genesis | State Extension | State Transition |

| --------------------------- | :-----: | :-------------: | :--------------: |

| **Ongezeko la Global State** |    + |        - |        + |

| **Mabadiliko ya Global State** |   n/a |        - |        + |

| **Ongezeko la Owned State** |    + |        - |        + |

| **Mabadiliko ya Owned State** |   n/a |       Hapana |        + |

| **Ongezeko la Valencies** |    + |        + |        + |

**`+`** : hatua inawezekana ikiwa Schema ya Contract inaruhusu.

**`-`**: operesheni lazima idhibitishwe na State Transition inayofuata (State Extension pekee haifungi Single-Use Seal).

Kwa kuongeza, upeo wa muda na haki za kusasisha za kila aina ya data zinaweza kutofautishwa katika jedwali lifuatalo:

|                                 | Metadata | Global State | Owned State |

| ------------------------------- | --------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------- |

| **Upeo** | Imefafanuliwa kwa Contract Operation moja | Inafafanuliwa kimataifa kwa Contract | Imefafanuliwa kwa kila Seal (*Assignment*) |

| **Nani anaweza kuisasisha?** | Isiyosasishwa (data ya muda mfupi) | Operesheni iliyotolewa na watendaji (mtoaji, n.k.) | Inategemea mmiliki halali ambaye anamiliki Seal (yule anayeweza kuitumia katika shughuli ifuatayo) |

| **Upeo wa Muda** | Kwa operesheni ya sasa pekee | Jimbo huanzishwa mwishoni mwa operesheni | Hali inafafanuliwa kabla ya operesheni (na *Seal Definition* ya operesheni ya awali) |

### Global State

Global State mara nyingi hufafanuliwa kama "hakuna anayemiliki, kila mtu anajua". Ina maelezo ya jumla kuhusu Contract, ambayo yanaonekana hadharani. Kwa mfano, katika Contract inayotoa ishara, ina uwezekano wa kuwa na:


- Tika (kifupi cha ishara ya ishara): `tika` ;
- Jina kamili la ishara: `jina` ;
- Usahihi (idadi ya sehemu za desimali): `usahihi` ;
- Toleo la awali (na/au upeo wa juu wa tokeni): `Ugavi uliotolewa` ;
- Tarehe ya toleo: `iliyoundwa` ;
- Data ya kisheria au taarifa nyingine za umma: `data`.

Global State hii inaweza kuwekwa kwenye rasilimali za umma (tovuti, IPFS, Nostr, Torrent, n.k.) na kusambazwa kwa jamii. Pia, motisha ya kiuchumi (haja ya kushikilia na kuhamisha tokeni hizi, n.k.) kwa kawaida huendesha watumiaji wa Contract kudumisha na kueneza data hii wenyewe.

### Kazi

*Assignment* ndio muundo wa msingi wa kufafanua :


- Seal (*Seal Definition*), ambayo inaashiria UTXO maalum;
- *Owned State*, yaani, mali au data inayohusiana na Seal hii.

*Assignment* inaweza kuonekana kama analogi ya pato la muamala wa Bitcoin, lakini kwa kunyumbulika zaidi. Hapa ndipo kuna mantiki ya uhawilishaji wa mali: *Assignment* inahusisha aina fulani ya mali au haki (`Aina ya Ugawaji`) na Seal. Yeyote aliye na ufunguo wa faragha wa UTXO uliounganishwa na Seal hii (au yeyote anayeweza kutumia UTXO hii) anachukuliwa kuwa mmiliki wa hii *Owned State*.

Mojawapo ya uwezo mkubwa wa RGB upo katika uwezo wa kufichua (*fichua*) au kuficha (*kuficha*) nyuga za *Seal Definition* na *Owned State* upendavyo. Hii inatoa mchanganyiko wenye nguvu wa usiri na kuchagua. Kwa mfano, unaweza kuthibitisha kuwa mpito ni halali bila kufichua data yote, kwa kutoa toleo lililofunuliwa kwa mtu ambaye anapaswa kuhalalisha, wakati wahusika wengine wanaona tu toleo lililofichwa (Hash). Kwa vitendo, `OpId` ya mpito kila mara hukokotwa kutoka kwa data *iliyofichwa*.

![RGB-Bitcoin](assets/fr/067.webp)

#### Seal Definition

*Seal Definition*, katika umbo lake lililofichuliwa, ina sehemu nne za msingi: `txptr`, `vout`, `blinding` na `mbinu` :


- txptr**: hii ni rejeleo la UTXO kwenye Bitcoin :
    - Katika kesi ya **Genesis Seal **, inaelekeza moja kwa moja kwa UTXO iliyopo (ile inayohusishwa na Genesis);
    - Kwa upande wa **Grafu Seal**, tunaweza kuwa na :
        - `txid` rahisi, ikiwa inaashiria UTXO mahususi,
        - Au `WitnessTx`, ambayo hutaja rejeleo la kibinafsi: Seal inaelekeza kwenye shughuli yenyewe. Hii ni muhimu hasa wakati hakuna UTXO ya nje inayopatikana, kwa mfano katika miamala ya kufungua kituo cha Umeme, au ikiwa mpokeaji hana UTXO.
- vout** : nambari ya matokeo ya shughuli iliyoonyeshwa na `txptr`. Wasilisha pekee kwa Grafu ya kawaida ya Seal (si kwa `WitnessTx`);
- kupofusha**: idadi nasibu ya ka 8, ili kuimarisha usiri na kuzuia majaribio ya nguvu ya kikatili kwenye utambulisho wa UTXO;
- method** : inaonyesha njia ya kutia nanga iliyotumika (`Tapret` au `Opret`).

Fomu ya *iliyofichwa* ya Seal Definition ni SHA256 Hash (iliyotambulishwa) ya muunganisho wa sehemu hizi 4, ikiwa na lebo maalum kwa RGB.

![RGB-Bitcoin](assets/fr/068.webp)

#### Nchi Zinazomilikiwa

Sehemu ya pili ya *Assignment* ni Owned State. Tofauti na Global State, inaweza kuwepo katika hali ya umma au ya kibinafsi:


- Owned State ya Umma**: kila mtu anajua data inayohusiana na Seal. Kwa mfano, picha ya umma;
- Owned State** ya kibinafsi: data imefichwa, inayojulikana na mmiliki pekee (na uwezekano wa kiidhinishaji ikiwa ni lazima). Kwa mfano, idadi ya ishara zilizofanyika.

RGB inafafanua aina nne za hali zinazowezekana (*StateTypes*) kwa Owned State:


- Tamko**: haina data ya nambari, ni haki ya kutangaza tu (k.m. haki ya kupiga kura). Fomu zilizofichwa na zilizofunuliwa zinafanana;
- Fungible**: inawakilisha wingi unaoweza kuvutwa (kama ishara). Katika umbo lililofichuliwa, tuna `kiasi` na `kupofusha`. Katika fomu iliyofichwa, tunayo *Pedersen commitment * moja ambayo inaficha kiasi na upofu;
- Muundo**: huhifadhi data iliyopangwa (hadi kB 64). Katika fomu iliyofichuliwa, ni sehemu ya data. Katika hali iliyofichwa, ni alama ya Hash ya blob hii:

```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```

Na, kwa mfano:

```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```


- Viambatisho**: huunganisha faili (sauti, picha, mfumo wa jozi, n.k.) kwa Owned State, ikihifadhi faili Hash `file_hash`, aina ya MIME `aina ya midia` na chumvi fiche `chumvi`. Faili yenyewe inapangishwa mahali pengine. Katika hali iliyofichwa, ni Hash iliyotambulishwa na vipengee vitatu vya data vilivyotangulia:

```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```

Na, kwa mfano:

```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```

Kwa muhtasari, hapa kuna aina 4 zinazowezekana za serikali kwa umma na fomu iliyofichwa:

```txt
State                      Concealed form                              Revealed form
+---------------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |
+--------------------------+             +---------------------------------------+
```

| **Kipengele** | **Tamko** | **Mwenye Kuvu** | **Muundo** | **Viambatisho** |

| ------------------- | -------------- | ----------------------------------- | ---------------------------- | ---------------------------- |

| **Data** | Hakuna | Imetiwa saini au haijatiwa saini nambari kamili ya biti 64 | Aina yoyote kali ya data | Faili yoyote |

| **Aina ya Taarifa** | Hakuna | Imetiwa saini au haijatiwa saini | Aina kali | Aina ya MIME |

| **Faragha** | Haihitajiki | Pedersen commitment | Hash yenye upofu | Kitambulisho cha faili chepesi |

| **Vikomo vya ukubwa** | N/A | baiti 256 | Hadi KB 64 | Hadi GB 500 |

### Ingizo

Ingizo za *Contract Operation* hurejelea *Kazi* ambazo zinatumika katika operesheni hii mpya. Ingizo linaonyesha:


- prevOpId` : kitambulisho (`OpId`) cha operesheni ya awali ambapo *Assignment* ilipatikana;
- assignmentType` : aina ya *Assignment* (kwa mfano, `assetOwner` kwa tokeni);
- `Index`: faharasa ya *Assignment* katika orodha inayohusishwa na `OpId` ya awali, iliyobainishwa baada ya upangaji wa kamusi ya mihuri iliyofichwa.

Ingizo hazionekani kamwe katika Genesis, kwa kuwa hakuna Kazi za awali. Wala hazionekani katika Viendelezi vya Jimbo (kwa sababu Viendelezi vya Jimbo havifungi mihuri; badala yake, vinafafanua upya mihuri mipya kulingana na Valencies).

Tunapokuwa na Nchi Zinazomilikiwa za aina ya `Fungible`, mantiki ya uthibitishaji (kupitia hati ya AluVM iliyotolewa katika Schema) hukagua uwiano wa hesabu: jumla ya tokeni zinazoingia (*Pembejeo*) lazima ziwe sawa na jumla ya tokeni zinazotoka (katika *Kazi* mpya).

### Metadata

Sehemu ya **Metadata** inaweza kuwa hadi 64 KiB na inatumika kujumuisha data ya muda muhimu kwa uthibitishaji, lakini haijaunganishwa katika hali ya kudumu ya Contract. Kwa mfano, vigeu vya hesabu vya kati vya hati ngumu vinaweza kuhifadhiwa hapa. Nafasi hii haikusudiwa kuhifadhiwa katika historia ya kimataifa, ndiyo maana iko nje ya mawanda ya Nchi Zinazomilikiwa au Global State.

### Valencies

Valencies** ni utaratibu halisi wa itifaki wa RGB. Wanaweza kupatikana katika Genesis, Mpito wa Jimbo au Viendelezi vya Jimbo. Zinawakilisha haki za nambari zinazoweza kuamilishwa na State Extension (kupitia *Redeems*), kisha kukamilishwa na Mpito unaofuata. Kila Valency inatambuliwa na `ValencyType` (biti 16). Semantiki zake (kutoa tena kulia, kubadilishana ishara, kuchoma kulia, nk) zimefafanuliwa katika Schema.

Kwa maneno madhubuti, tunaweza kufikiria Genesis ikifafanua "haki ya kutoa tena" Valency. State Extension itaitumia (*Redeem*) ikiwa hali fulani zinakabiliwa, ili kuanzisha kiasi kipya cha ishara. Kisha, State Transition inayotoka kwa mmiliki wa Seal iliyoundwa hivyo inaweza kuhamisha ishara hizi mpya.

### Hukomboa

Kukomboa ni sawa na Valency na Pembejeo za Kazi. Zinaonekana tu katika Viendelezi vya Jimbo, kwani hapa ndipo Valency iliyofafanuliwa hapo awali inawezeshwa. Redeem ina sehemu mbili:


- `PrevOpId` : `OpId` ya operesheni ambapo Valency ilibainishwa;
- `ValencyType`: aina ya Valency unayotaka kuwezesha (kila `ValencyType` inaweza kutumika mara moja tu na State Extension).

Mfano: Redeem inaweza kuendana na utekelezaji wa CoinSwap, kulingana na kile kilichowekwa katika Valency.

### Tabia za hali ya RGB

Sasa tutaangalia sifa kadhaa za kimsingi za hali katika RGB. Hasa, tutazingatia:


- **Mfumo wa Aina Mkali**, ambao unaweka shirika sahihi na lililoandikwa la data;
- Umuhimu wa kutenganisha **uthibitishaji** kutoka **Ownership** ;
- **Mfumo wa mageuzi ya makubaliano** katika RGB, unaojumuisha dhana za *kusonga mbele kwa haraka* na *sukuma nyuma*.

Kama kawaida, kumbuka kuwa kila kitu kinachohusiana na hali ya Contract kinathibitishwa kwa upande wa mteja kulingana na sheria za makubaliano zilizowekwa katika itifaki, na ambao marejeleo yake ya mwisho ya kriptografia yameainishwa katika miamala ya Bitcoin.

#### Mfumo wa Aina Mkali

RGB hutumia *Mfumo wa Aina Madhubuti* na hali ya kubainisha ya ufuataji (*Usimbaji Mkali*). Shirika hili limeundwa ili kuhakikisha uzalishwaji kamili na usahihi katika ufafanuzi, utunzaji na uthibitishaji wa data ya Contract.

Katika mazingira mengi ya programu (JSON, YAML...), muundo wa data unaweza kunyumbulika, hata kuruhusu sana. Katika RGB, kwa upande mwingine, Muundo na Aina za kila uwanja hufafanuliwa kwa vikwazo vya wazi. Kwa mfano:


- Kila kigezo kina aina mahususi (kwa mfano, nambari kamili ya 8-bit isiyotiwa saini `u8`, au nambari kamili iliyotiwa saini ya biti 16, n.k.);
- Aina zinaweza kutengenezwa (aina zilizowekwa kiota). Hii inamaanisha kuwa unaweza kufafanua aina kulingana na aina zingine (k.m. aina ya jumla iliyo na sehemu ya `u8`, sehemu ya `bool`, n.k.);
- Mikusanyiko pia inaweza kubainishwa: orodha (*orodha*), seti (*weka*) au kamusi (*ramani*), zenye mpangilio maalum wa kuendelea;
- Kila uwanja umefungwa (*upande wa chini* / *upper bound*). Pia tunaweka mipaka kwa idadi ya Elements katika makusanyo (containment);
- Data imepangiliwa kwa baiti na usakinishaji unafafanuliwa kwa uwazi na usio na utata.

Shukrani kwa itifaki hii kali ya usimbuaji:


- Utaratibu wa mashamba daima ni sawa, bila kujali utekelezaji au lugha ya programu inayotumiwa;
- Kwa hivyo heshi zinazokokotolewa kwenye seti sawa ya data zinaweza kuzaliana tena na zinafanana ( *ahadi* zinazoamua);
- Mipaka huzuia ukuaji usiodhibitiwa wa saizi ya data (k.m. sehemu nyingi sana);
- Njia hii ya usimbaji hurahisisha uthibitishaji wa kriptografia, kwani kila mshiriki anajua haswa jinsi ya kusasisha na Hash data.

Kwa mazoezi, muundo (*Schema*) na msimbo unaosababisha (*Interface* na mantiki inayohusishwa) hukusanywa. Lugha ya maelezo hutumika kufafanua Contract (aina, nyanja, sheria) na generate umbizo kali la binary. Inapokusanywa, matokeo yake ni:


- *Mpangilio wa Kumbukumbu* kwa kila sehemu;
- Vitambulishi vya kisemantiki (ambavyo vinaonyesha ikiwa kubadilisha jina la kutofautisha kuna athari kwenye mantiki, hata kama muundo wa kumbukumbu unabaki kuwa sawa).

Mfumo madhubuti wa aina pia huwezesha ufuatiliaji sahihi wa mabadiliko: marekebisho yoyote ya muundo (hata mabadiliko ya jina la uwanja) yanaweza kutambulika na yanaweza kusababisha mabadiliko katika alama ya jumla.

Hatimaye, kila mkusanyiko hutoa alama ya vidole, kitambulisho cha kriptografia ambacho kinathibitisha toleo halisi la msimbo (data, sheria, uthibitishaji). Kwa mfano, kitambulisho cha fomu:

```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```

Hii inafanya uwezekano wa kudhibiti makubaliano au masasisho ya utekelezaji, huku ikihakikisha ufuatiliaji wa kina wa matoleo yanayotumika kwenye mtandao.

Ili kuzuia hali ya RGB Contract kuwa ngumu sana kuthibitishwa kwa upande wa mteja, sheria ya makubaliano inaweka ukubwa wa juu wa baiti `2^16` (64 Kio) kwa data yoyote inayohusika katika hesabu za uthibitishaji. Hii inatumika kwa kila kigezo au muundo: si zaidi ya baiti 65536, au nambari inayolingana (32768 16-bit integers, nk.). Hii inatumika pia kwa mikusanyiko (orodha, seti, ramani), ambayo inaweza isizidi `2^16` Elements.

Kikomo hiki kinahakikisha:


- Hudhibiti ukubwa wa juu zaidi wa data wa kubadilishwa wakati wa State Transition;
- Utangamano na mashine pepe (*AluVM*) inayotumiwa kuendesha hati za uthibitishaji.

#### Uthibitishaji != Ownership dhana

Mojawapo ya uvumbuzi mkuu wa RGB ni utengano mkali kati ya dhana mbili:


- Uthibitishaji**: kuangalia kwamba State Transition inaheshimu sheria za Contract (Business Logic, historia, nk);
- **Ownership** (Ownership, au udhibiti): ukweli wa kumiliki Bitcoin UTXO ambayo inaruhusu Single-Use Seal kutumika (au kufungwa), na hivyo State Transition kufanyika.

Uthibitishaji** unafanyika katika kiwango cha programu ya RGB (maktaba, itifaki ya *ahadi*, n.k.). Jukumu lake ni kuhakikisha kwamba sheria za ndani za Contract (kiasi, ruhusa, nk) zinaheshimiwa. Waangalizi au washiriki wengine wanaweza pia kuthibitisha historia ya data.

Ownership**, kwa upande mwingine, inategemea kabisa usalama wa Bitcoin. Kumiliki ufunguo wa faragha wa UTXO kunamaanisha kudhibiti uwezo wa kuzindua mpito mpya (kufunga Single-Use Seal). Kwa hivyo, hata kama mtu anaweza kuona au kuthibitisha data, hawezi kubadilisha hali ikiwa hamiliki UTXO inayohusika.

![RGB-Bitcoin](assets/fr/069.webp)

Mbinu hii inapunguza udhaifu wa kawaida unaopatikana katika minyororo changamano zaidi (ambapo msimbo wote wa Smart contract ni wa umma na unaweza kubadilishwa na mtu yeyote, ambayo wakati mwingine imesababisha udukuzi). Kwenye RGB, mshambuliaji hawezi tu kuingiliana na hali ya On-Chain, kwani haki ya kuchukua hatua kwa serikali (*Ownership*) inalindwa na Bitcoin Layer.

Zaidi ya hayo, utengano huu unaruhusu RGB kuunganishwa kwa kawaida na Lightning Network. Njia za umeme zinaweza kutumika kuhusisha na kuhamisha vipengee vya RGB bila kushirikisha On-Chain *ahadi* kila wakati. Tutaangalia kwa karibu muunganisho huu wa RGB kwenye Umeme katika sura za baadaye za kozi.

#### Maendeleo ya Makubaliano katika RGB

Kando na toleo la msimbo wa kisemantiki, RGB inajumuisha mfumo wa kutoa au kusasisha sheria za makubaliano za Contract kwa wakati. Kuna aina mbili kuu za mageuzi:


- Songa mbele kwa kasi**
- Sukuma nyuma** (kwa Kifaransa)

Usambazaji mbele kwa haraka hutokea wakati sheria ambayo hapo awali ilikuwa batili inakuwa halali. Kwa mfano, ikiwa Contract itabadilika ili kuruhusu aina mpya ya `AssignmentType` au sehemu mpya :


- Hii haiwezi kulinganishwa na hardfork ya kawaida ya Blockchain, kwani RGB inafanya kazi katika Client-side Validation na haiathiri utangamano wa jumla wa Blockchain;
- Kwa maneno ya kiutendaji, aina hii ya mabadiliko inaonyeshwa na uga wa `Ffv` (*toleo la mbele-haraka*) katika Contract Operation;
- Wamiliki wa sasa hawana madhara: hali yao inabakia halali;
- Walengwa wapya (au watumiaji wapya), kwa upande mwingine, wanahitaji kusasisha programu zao (Wallet yao) ili kutambua sheria mpya.

Kusukuma nyuma kunamaanisha kuwa sheria halali ya hapo awali inakuwa batili. Kwa hivyo ni "ugumu" wa sheria, lakini sio kusema kabisa uma laini:


- Wamiliki waliopo wanaweza kuathiriwa (wanaweza kujikuta na vipengee ambavyo vimepitwa na wakati au si sahihi katika toleo jipya);
- Tunaweza kuzingatia kwamba kwa kweli tunaunda itifaki mpya: yeyote anayechukua sheria mpya anaondoka kutoka kwa ile ya zamani;
- Mtoaji anaweza kuamua kutoa tena mali katika itifaki hii mpya, na kulazimisha watumiaji kudumisha pochi mbili tofauti (moja kwa itifaki ya zamani, nyingine kwa mpya), ikiwa wanataka kudhibiti matoleo yote mawili.

Katika sura hii kuhusu utendakazi wa RGB Contract, tumechunguza kanuni za msingi zinazotokana na itifaki hii. Kama ulivyoona, utata wa asili wa itifaki ya RGB unahitaji matumizi ya maneno mengi ya kiufundi. Kwa hivyo, katika sura inayofuata, nitakupa faharasa ambayo itafanya muhtasari wa dhana zote zilizojumuishwa katika sehemu hii ya kwanza ya kinadharia, pamoja na ufafanuzi wa maneno yote ya kiufundi yanayohusiana na RGB. Kisha, katika sehemu inayofuata, tutaangalia kwa vitendo ufafanuzi na utekelezaji wa mikataba ya RGB.

## RGB Glossary

<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>

Iwapo unahitaji kurejea faharasa hii fupi ya maneno muhimu ya kiufundi yanayotumika katika ulimwengu wa RGB (yaliyoorodheshwa kwa mpangilio wa alfabeti), utayapata yanafaa. Sura hii si muhimu ikiwa tayari umeelewa kila kitu ambacho tumeshughulikia katika sehemu ya kwanza.

#### AluVM

Kifupi cha AluVM kinasimama kwa "_Algorithmic logic unit Virtual Machine_", mashine pepe ya msingi ya rejista iliyoundwa kwa ajili ya uthibitishaji wa Smart contract na kompyuta iliyosambazwa. Inatumika (lakini haijahifadhiwa pekee) kwa uthibitishaji wa mikataba ya RGB. Hati au shughuli zilizojumuishwa katika RGB Contract zinaweza kutekelezwa katika mazingira ya AluVM.

Kwa habari zaidi: [Tovuti rasmi ya AluVM](https://www.AluVM.org/)

#### Anchor

Anchor inawakilisha seti ya data ya upande wa mteja inayotumiwa kuthibitisha kujumuishwa kwa _commitment_ ya kipekee katika shughuli ya ununuzi. Katika itifaki ya RGB, Anchor ina Elements ifuatayo:


- Kitambulishi cha muamala cha Bitcoin (txid) cha **Witness Transaction** ;
- **Multi Protocol Commitment (MPC)** ;
- **Deterministic Bitcoin Commitment (DBC)**;
- **Uthibitisho wa Ziada wa Muamala (ETP)** ikiwa utaratibu wa **Tapret** Commitment unatumiwa (angalia sehemu iliyowekwa kwa muundo huu).

Kwa hivyo Anchor hutumika kuanzisha kiungo kinachoweza kuthibitishwa kati ya shughuli mahususi ya Bitcoin na data ya faragha iliyoidhinishwa na itifaki ya RGB. Inahakikisha kwamba data hizi kwa hakika zimejumuishwa kwenye Blockchain, bila maudhui yake halisi kufichuliwa hadharani.

#### Assignment

Katika mantiki ya RGB, Assignment ni sawa na matokeo ya muamala ambayo hurekebisha, kusasisha au kuunda sifa fulani ndani ya hali ya Contract. Assignment inajumuisha Elements mbili:


- A **Seal Definition** (rejea UTXO maalum);
- **Owned State** (data inayoelezea hali inayohusishwa na mmiliki huyu mpya).

Kwa hivyo Assignment inaonyesha kuwa sehemu ya serikali (kwa mfano, mali) sasa imetolewa kwa mmiliki fulani, aliyetambuliwa kupitia Single-Use Seal iliyounganishwa na UTXO.

#### Business Logic

Vikundi vya Business Logic pamoja na sheria zote na uendeshaji wa ndani wa Contract, iliyoelezwa na **Schema** yake (yaani muundo wa Contract yenyewe). Inaamuru jinsi hali ya Contract inaweza kubadilika, na chini ya hali gani.

#### Client-side Validation

Client-side Validation inarejelea mchakato ambao kila mhusika (mteja) anathibitisha seti ya data inayobadilishwa kwa faragha, kulingana na sheria za itifaki. Kwa upande wa RGB, data hii iliyobadilishwa huwekwa pamoja katika kile kinachojulikana kama **shehena**. Tofauti na itifaki ya Bitcoin, ambayo inahitaji shughuli zote kuchapishwa On-Chain, RGB inaruhusu tu _ahadi_ (zilizotia nanga katika Bitcoin) kuhifadhiwa hadharani, huku maelezo muhimu ya Contract (mabadiliko, uthibitisho, uthibitisho) yanasalia kuwa off-chain pekee, inayoshirikiwa na watumiaji.

#### Commitment

Commitment (katika maana ya kriptografia) ni kitu cha hisabati, kinachoashiria `C`, kinachotokana na kubainishwa kutokana na operesheni kwenye data iliyopangwa `m` (ujumbe) na thamani nasibu `r`. Tunaandika:

$$
C = \text{commit}(m, r)
$$

Utaratibu huu unajumuisha shughuli kuu mbili:


- Ahadi**: kazi ya kriptografia inatumika kwa ujumbe `m` na nambari nasibu `r` kutoa `C` ;
- Thibitisha**: tunatumia `C`, ujumbe `m` na thamani `r` ili kuangalia kama Commitment hii ni sahihi. Chaguo za kukokotoa hurejesha `Kweli` au `Sivyo`.

Commitment lazima iheshimu sifa mbili:


- Kufunga**: lazima isiwezekane kupata jumbe mbili tofauti zinazotoa `C` :

$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$

Kama vile:

$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$


- Kuficha**: maarifa ya `C` lazima yasionyeshe yaliyomo katika `m`.

Katika itifaki ya RGB, Commitment imejumuishwa katika shughuli ya Bitcoin ili kuthibitisha kuwepo kwa kipande fulani cha habari kwa wakati fulani, bila kufunua habari yenyewe.

#### Consignment

A **Consignment** hukusanya pamoja data iliyobadilishwa kati ya wahusika, kulingana na Client-side Validation katika RGB. Kuna aina mbili kuu za Consignment:


- Contract Consignment**: inayotolewa na *mtoaji* (mtoaji wa Contract), inajumuisha maelezo ya uanzishaji kama vile Schema, Genesis, Interface na Interface Implementation.
- Uhamisho wa Consignment**: hutolewa na mhusika anayelipa (*mlipaji*). Ina historia nzima ya mabadiliko ya serikali kuelekea Terminal Consignment (yaani hali ya mwisho iliyopokelewa na mlipaji).

Mizigo hii haijarekodiwa hadharani kwenye Blockchain; zinabadilishwa moja kwa moja kati ya pande zinazohusika kupitia njia ya mawasiliano wanayochagua.

#### Contract

Contract ni seti ya haki zinazotekelezwa kidijitali kati ya watendaji kadhaa kupitia itifaki ya RGB. Ina hali inayotumika na Business Logic, iliyofafanuliwa na Schema, ambayo inabainisha ni shughuli gani zimeidhinishwa (uhamisho, upanuzi, nk). Hali ya Contract, pamoja na sheria za uhalali wake, zinaonyeshwa katika Schema. Wakati wowote, Contract inabadilika kulingana na kile kinachoruhusiwa na Schema hii na kwa hati za uthibitishaji (kukimbia, kwa mfano, katika AluVM).

#### Contract Operation

Contract Operation ni sasisho la hali ya Contract linalofanywa kulingana na sheria za Schema. Operesheni zifuatazo zipo katika RGB:


- State Transition** ;
- Genesis** ;
- State Extension**.

Kila operesheni hurekebisha hali kwa kuongeza au kubadilisha data fulani (Global State, Owned State...).

#### Contract Participant

Contract Participant ni mwigizaji anayeshiriki katika shughuli zinazohusiana na Contract. Katika RGB, tofauti hufanywa kati ya:


- Mtoaji wa Contract, ambayo inaunda Genesis (asili ya Contract);
- Vyama vya Contract, yaani wamiliki wa haki za serikali ya Contract;
- Vyama vya umma, vinavyoweza kujenga Viendelezi vya Jimbo ikiwa Contract inatoa Valencies zinazoweza kufikiwa na umma.

#### Contract Rights

Contract Rights inarejelea haki mbalimbali zinazoweza kutumiwa na wale wanaohusika katika RGB Contract. Wanaanguka katika vikundi kadhaa:


- Haki za Ownership**, zinazohusishwa na Ownership ya UTXO fulani (kupitia _Seal Definition_);
- Haki za utendaji**, yaani uwezo wa kujenga mpito mmoja au zaidi (Mipito ya Jimbo) kwa mujibu wa Schema;
- Haki za umma**, Schema inapoidhinisha matumizi fulani ya umma, kwa mfano kuunda State Extension kupitia ukombozi wa Valency.

#### Contract State

Contract State inalingana na hali ya sasa ya Contract kwa wakati fulani. Inaweza kujumuisha data ya umma na ya kibinafsi, inayoakisi hali ya Contract. RGB inatofautisha kati ya:


- **Global State**, ambayo inajumuisha mali ya umma ya Contract (imewekwa katika Genesis au kuongezwa kupitia masasisho yaliyoidhinishwa);
- Nchi Zinazomilikiwa**, ambazo ni za wamiliki mahususi, zinazotambuliwa na UTXOs zao.

#### Deterministic Bitcoin Commitment - DBC

Deterministic Bitcoin Commitment (DBC) ni seti ya sheria zinazotumiwa kusajili _ahadi_ katika shughuli ya Bitcoin kwa njia ya kipekee na ya kipekee. Katika itifaki ya RGB, kuna aina mbili kuu za DBC:


- Opt**
- Gonga **

Mbinu hizi hufafanua kwa usahihi jinsi _ahadi_ inavyosimbwa katika utoaji au muundo wa muamala wa Bitcoin, ili kuhakikisha kuwa Commitment hii inaweza kufuatiliwa na kuthibitishwa.

#### Directed Acyclic Graph - DAG

DAG (au *Acyclic Guided Graph*) ni grafu isiyo na mzunguko, inayowezesha uratibu wa kitolojia. Blockchains, kama _shards_ ya mikataba ya RGB, inaweza kuwakilishwa na DAG.

Kwa maelezo zaidi: [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)

#### Kuchonga

Kuchonga ni mfuatano wa data wa hiari ambao wamiliki mfululizo wa Contract wanaweza kuingia katika historia ya Contract. Kipengele hiki kipo, kwa mfano, katika **RGB21** Interface na kuwezesha maelezo ya ukumbusho au maelezo kuongezwa kwenye historia ya Contract.

#### Uthibitisho wa Muamala wa Ziada - ETP

ETP (*Uthibitisho wa Muamala wa Ziada*) ni sehemu ya Anchor ambayo ina data ya ziada inayohitajika ili kuthibitisha **Tapret** *Commitment* (katika muktadha wa _taproot_). Inajumuisha, miongoni mwa mambo mengine, ufunguo wa ndani wa hati ya Taproot (_internal PubKey_) na maelezo mahususi kwa _Script Path Spend_.

#### Genesis

Genesis inarejelea seti ya data, inayosimamiwa na Schema, ambayo huunda hali ya awali ya Contract yoyote katika RGB. Inaweza kulinganishwa na dhana ya _Genesis Block_ ya Bitcoin, au dhana ya Coinbase Transaction, lakini hapa katika kiwango cha tokeni cha _client-side_ na RGB.

#### Global State

Global State ni seti ya mali za umma zilizomo katika Contract State. Inafafanuliwa kwenye Genesis na, kulingana na sheria za Contract, inaweza kusasishwa na mabadiliko yaliyoidhinishwa. Tofauti na Mataifa Yanayomilikiwa, Global State si mali ya huluki fulani; iko karibu na sajili ya umma ndani ya Contract.

#### Interface

Interface ni seti ya maagizo yanayotumiwa kusimbua data ya jozi iliyokusanywa katika Schema au katika shughuli za Contract na hali zao, ili kuzifanya zisomeke kwa mtumiaji au Wallet yake. Inafanya kazi kama tafsiri ya Layer.

#### Interface Implementation

Interface Implementation ni seti ya matamko yanayounganisha **Interface** na **Schema**. Inawezesha tafsiri ya kisemantiki inayofanywa na Interface yenyewe, ili data ghafi ya Contract iweze kueleweka na mtumiaji au programu inayohusika (mikoba).

#### Invoice

Invoice inachukua fomu ya URL iliyosimbwa katika [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), ambayo hupachika data muhimu kwa ajili ya ujenzi wa **State Transition** (na mlipaji). Kwa maneno mengine, ni Invoice inayowezesha mshirika mwingine (*mlipaji*) kuunda mpito unaolingana wa kuhamisha kipengee au kusasisha hali ya Contract.

#### Lightning Network

Lightning Network ni mtandao uliogatuliwa wa njia za malipo (au _state channels_) kwenye Bitcoin, inayoundwa na pochi 2/2 zenye sahihi nyingi. Huwasha miamala ya _off-chain_ ya haraka, ya gharama nafuu, huku ikitegemea Bitcoin's Layer 1 kwa usuluhishi (au kufungwa) inapobidi.

Kwa habari zaidi juu ya jinsi Umeme unavyofanya kazi, ninapendekeza uchukue kozi hii nyingine:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
#### Multi Protocol Commitment - MPC

Multi Protocol Commitment (MPC) inarejelea muundo wa Merkle Tree unaotumika katika RGB kujumuisha, ndani ya muamala mmoja wa Bitcoin, **Vifungu vingi vya Mpito** kutoka kwa mikataba tofauti. Wazo ni kuweka pamoja ahadi kadhaa (zinazoweza kuendana na mikataba tofauti au mali tofauti) katika sehemu moja ya Anchor ili kuboresha ukaliaji wa nafasi ya kuzuia.

#### Owned State

Owned State ni sehemu ya Contract State ambayo imefungwa katika Assignment na kuhusishwa na mmiliki fulani (kupitia Single-Use Seal inayoelekeza kwa UTXO). Hii inawakilisha, kwa mfano, mali ya kidijitali au haki mahususi ya kimkataba aliyopewa mtu huyo.

#### Ownership

Ownership inarejelea uwezo wa kudhibiti na kutumia UTXO inayorejelewa na Seal Definition. Wakati Owned State inaunganishwa na UTXO, mmiliki wa UTXO hii ana haki, uwezekano, kuhamisha au kubadilisha hali inayohusishwa, kulingana na sheria za Contract.

#### Partially Signed Bitcoin Transaction - PSBT

PSBT (_Partially Signed Bitcoin Transaction_) ni muamala wa Bitcoin ambao bado haujatiwa saini kikamilifu. Inaweza kushirikiwa kati ya huluki kadhaa, ambayo kila moja inaweza kuongeza au kuthibitisha Elements fulani (saini, hati...), hadi muamala uchukuliwe kuwa uko tayari kwa usambazaji wa On-Chain.

Kwa maelezo zaidi: [BIP-0174](https://github.com/Bitcoin/bips/blob/master/bip-0174.mediawiki)

#### Pedersen commitment

Pedersen commitment ni aina ya kriptografia Commitment yenye sifa ya kuwa **homomorphic** kuhusiana na operesheni ya kuongeza. Hii ina maana kwamba inawezekana kuthibitisha jumla ya ahadi mbili bila kufichua maadili ya mtu binafsi.

Rasmi, ikiwa:

$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$

basi:

$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$

Mali hii ni muhimu, kwa mfano, kwa kuficha kiasi cha ishara zilizobadilishwa, wakati bado inaweza kuthibitisha jumla.

Taarifa zaidi: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)

#### Redeem

Katika State Extension, Redeem inarejelea hatua ya kurejesha (au kutumia) **Valency** iliyotangazwa hapo awali. Kwa vile Valency ni haki ya umma, Redeem inaruhusu mshiriki aliyeidhinishwa kudai Contract State Extension mahususi.

#### Schema

Schema katika RGB ni kipande cha msimbo tangazo kinachoelezea seti ya vigezo, sheria na Business Logic (*Business Logic*) ambayo inasimamia uendeshaji wa Contract. Schema inafafanua muundo wa serikali, aina za mabadiliko zinazoruhusiwa na hali ya uthibitishaji.

#### Seal Definition

Seal Definition ni sehemu ya Assignment inayohusisha _ahadi_ na UTXO inayomilikiwa na mmiliki mpya. Kwa maneno mengine, inaonyesha mahali ambapo hali iko (ambayo UTXO), na huanzisha Ownership ya mali au haki.

#### Shard

Shard inawakilisha tawi katika DAG ya historia ya Mpito ya Jimbo ya RGB Contract. Kwa maneno mengine, ni sehemu ndogo ya jumla ya historia ya Contract, inayolingana, kwa mfano, na mlolongo wa mabadiliko yanayohitajika ili kuthibitisha uhalali wa mali fulani tangu _Mwanzo_.

#### Single-Use Seal

Single-Use Seal ni ahadi ya siri ya Commitment kwa ujumbe ambao bado haujulikani, ambao utafichuliwa mara moja tu katika siku zijazo na lazima ujulikane na washiriki wote wa hadhira mahususi. Lengo ni kuzuia kuundwa kwa ahadi nyingi zinazoshindana kwa Seal sawa.

#### Stash

Stash ni seti ya data ya upande wa mteja ambayo mtumiaji huhifadhi kwa kandarasi moja au zaidi za RGB, kwa madhumuni ya uthibitishaji (*Client-side Validation*). Hii ni pamoja na historia ya mpito, shehena, uthibitisho wa uhalali, n.k. Kila mmiliki anahifadhi tu sehemu za historia anazohitaji (*shards*).

#### State Extension

State Extension ni Contract Operation inayotumika kuanzisha upya masasisho ya hali kwa kukomboa **Valencies** zilizotangazwa awali. Ili kuwa na ufanisi, State Extension lazima ifungwe na State Transition (ambayo inasasisha hali ya mwisho ya Contract).

#### State Transition

State Transition ni operesheni inayobadilisha hali ya RGB Contract hadi hali mpya. Inaweza kurekebisha data ya Global State na/au Owned State. Katika mazoezi, kila mpito inathibitishwa na sheria za Schema na kuunganishwa katika Bitcoin Blockchain kupitia _commitment_.

#### Taproot

Inarejelea umbizo la muamala la Bitcoin la SegWit v1, lililoletwa na [BIP341](https://github.com/Bitcoin/bips/blob/master/bip-0341.mediawiki) na [BIP342](https://github.com/Bitcoin/bips/blob/master/bip-0342.mediawiki). Taproot inaboresha usiri na unyumbulifu wa hati, haswa kwa kufanya miamala iwe ngumu zaidi na ngumu kutofautisha kutoka kwa mwingine.

#### Terminal Consignment - Consignment Endpoint

Terminal Consignment (au _Consignment Endpoint_) ni *uhamisho Consignment* iliyo na hali ya mwisho ya Contract, ikijumuisha State Transition iliyoundwa kutoka kwa Invoice ya mpokeaji (*mlipaji*). Kwa hiyo ni mwisho wa uhamisho, na data muhimu ili kuthibitisha kwamba Ownership au hali imehamishwa.

#### Transition Bundle

Transition Bundle ni seti ya Mabadiliko ya Jimbo la RGB (ya Contract sawa) ambayo yote yanahusika katika ***Witness Transaction*** Bitcoin sawa. Hii inafanya uwezekano wa kuunganisha masasisho au uhamisho kadhaa kwenye On-Chain Anchor moja.

#### UTXO

Bitcoin UTXO (*Pato la Muamala Usiotumika*) hufafanuliwa na Hash ya shughuli na faharasa ya pato (*vout*). Pia wakati mwingine huitwa _outpoint_. Katika itifaki ya RGB, rejeleo la UTXO (kupitia **Seal Definition**) huwezesha eneo la **Owned State**, yaani mali iliyoshikiliwa kwenye Blockchain.

#### Valency

Valency ni haki ya umma ambayo haihitaji hifadhi ya hali kama hiyo, lakini ambayo inaweza kukombolewa kupitia **State Extension**. Kwa hiyo ni aina ya uwezekano wazi kwa wote (au wachezaji fulani), iliyotangazwa katika mantiki ya Contract, ili kutekeleza ugani fulani baadaye.

#### Witness Transaction

Witness Transaction ni shughuli ya Bitcoin inayofunga Single-Use Seal karibu na ujumbe ulio na Multi Protocol Commitment (MPC). Muamala huu hutumia UTXO au kuunda moja, ili Seal Commitment iliyounganishwa na itifaki ya RGB. Inafanya kazi kama uthibitisho wa On-Chain kwamba serikali imewekwa katika hatua maalum kwa wakati.

# Kupanga kwenye RGB

<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>

## Utekelezaji wa mikataba ya RGB

<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>

:::video id=97d81b85-5a82-40a5-b111-7d96be5afd0f:::

Katika sura hii, tutaangalia kwa undani jinsi RGB Contract inavyofafanuliwa na kutekelezwa. Tutaona vipengele vya RGB Contract ni nini, majukumu yao ni nini na jinsi yanavyoundwa.

### Sehemu za RGB Contract

Kufikia sasa, tayari tumejadili **Genesis**, ambayo inawakilisha mwanzo wa Contract, na tumeona jinsi inavyolingana na mantiki ya *Contract Operation* na hali ya itifaki. Ufafanuzi kamili wa RGB Contract, hata hivyo, sio tu kwa Genesis pekee: inahusisha vipengele vitatu vya ziada ambavyo, pamoja, huunda moyo wa utekelezaji.

Sehemu ya kwanza inaitwa **Schema**. Hili ni faili linaloelezea muundo msingi na Business Logic (*Business Logic*) ya Contract. Inabainisha aina za data zinazotumika, sheria za uthibitishaji, shughuli zinazoruhusiwa (k.m. utoaji wa tokeni wa awali, uhamisho, masharti maalum, n.k.) - kwa ufupi, mfumo wa jumla unaoelekeza jinsi Contract inavyofanya kazi.

Sehemu ya pili ni **Interface**. Inaangazia jinsi watumiaji (na kwa ugani, programu ya kwingineko) itaingiliana na Contract hii. Inaeleza semantiki, yaani uwakilishi unaosomeka wa nyanja na vitendo mbalimbali. Kwa hivyo, wakati Schema inafafanua jinsi Contract inavyofanya kazi kiufundi, Interface inafafanua jinsi ya kuwasilisha na kufichua utendaji huu: majina ya njia, maonyesho ya data, nk.

Sehemu ya tatu ni **Interface Implementation**, ambayo inakamilisha mbili zilizopita kwa kufanya kama aina ya daraja kati ya Schema na Interface. Kwa maneno mengine, inahusisha semantiki iliyoonyeshwa na Interface na sheria za msingi zilizofafanuliwa katika Schema. Ni utekelezaji huu ambao utasimamia, kwa mfano, ubadilishaji kati ya parameta iliyoingia kwenye Wallet na muundo wa binary uliowekwa na itifaki, au utungaji wa sheria za uthibitishaji katika lugha ya mashine.

Utaratibu huu ni kipengele cha kuvutia cha RGB, kwani huruhusu vikundi tofauti vya wasanidi programu kufanya kazi tofauti kwenye vipengele hivi (*Schema*, *Interface*, *Utekelezaji*), mradi tu wanafuata sheria za makubaliano ya itifaki.

Kwa muhtasari, kila Contract ina:


- Genesis**, ambayo ni hali ya awali ya Contract (na inaweza kulinganishwa na shughuli maalum inayofafanua Ownership ya kwanza ya mali, haki, au data nyingine yoyote ya parameterizable);
- Schema**, ambayo inaelezea Contract ya Business Logic (aina za data, sheria za uthibitishaji, nk);
- Interface**, ambayo hutoa Layer ya semantic kwa pochi na watumiaji wa kibinadamu, kufafanua usomaji na utekelezaji wa shughuli;
- Utekelezaji** Interface, ambayo huziba pengo kati ya Business Logic na uwasilishaji, ili kuhakikisha kuwa ufafanuzi wa Contract unalingana na matumizi ya mtumiaji.

![RGB-Bitcoin](assets/fr/070.webp)

Ni muhimu kutambua kwamba ili Wallet iweze kusimamia mali ya RGB (iwe ishara ya kuvu au haki ya aina yoyote), lazima iwe na Elements hizi zote zilizokusanywa: *Schema*, *Interface*, *Interface Implementation* na *Genesis*. Hii hupitishwa kupitia ***Contract Consignment***, yaani, kifurushi cha data kilicho na kila kitu kinachohitajika ili kuthibitisha upande wa mteja wa Contract.

Ili kusaidia kufafanua dhana hizi, hapa kuna jedwali la muhtasari linalolinganisha vijenzi vya RGB Contract na dhana ambazo tayari zinajulikana ama katika upangaji unaolenga kitu (OOP) au katika mfumo ikolojia wa Ethereum:

| Sehemu ya RGB Contract | Maana | OOP Sawa | Ethereum Sawa |

| --------------------------- | ------------------------------------ | ----------------------------------------- | -------------------------------- |

| **Genesis** | Hali ya awali ya Contract | Mjenzi wa darasa | Mjenzi wa Contract |

| **Schema** | Business Logic ya Contract | Darasa | Contract |

| **Interface** | Semantiki ya Contract | Interface (Java) / Sifa (Rust) / Itifaki (Swift) | ERC Kawaida |

| **Interface Implementation** | Kuchora semantiki na mantiki | Impl (Rust) / Zana (Java) | Maombi Binary Interface (ABI) |

Safu wima ya kushoto inaonyesha Elements maalum kwa itifaki ya RGB. Safu ya kati inaonyesha kazi halisi ya kila sehemu. Halafu, kwenye safu wima ya "OOP sawa", tunapata neno sawa katika programu inayolenga kitu:


- **Genesis** ina jukumu sawa na lile la *Mjenzi wa Hatari*: hapa ndipo hali ya Contract inapoanzishwa;
- **Schema** ni maelezo ya darasa, yaani ufafanuzi wa mali zake, mbinu na mantiki ya msingi;
- **Interface** inalingana na *interfaces* (Java), *sifa* (Rust) au *itifaki* (Swift): haya ni ufafanuzi wa umma wa kazi, matukio, nyanja... ;
- **Interface Implementation** inalingana na *Impl* katika Rust au *Emplements* katika Java, ambapo tunabainisha jinsi msimbo utakavyotekeleza kwa hakika mbinu zilizotangazwa katika Interface.

Katika muktadha wa Ethereum, Genesis iko karibu na kijenzi cha *Contract*, Schema kwa ufafanuzi wa Contract, Interface kwa kiwango kama vile ERC-20 au ERC-721, na Interface Implementation kwa muundo wa ABI (*2 GW-3) ambayo muundo wa aina mbili wa GW-3 huingiliana. na Contract.

Faida ya moduli ya RGB pia inatokana na ukweli kwamba wadau mbalimbali wanaweza kuandika, kwa mfano, Interface Implementation yao wenyewe, mradi tu wanaheshimu mantiki ya *Schema* na semantiki ya *Interface*. Kwa hivyo, mtoaji anaweza kukuza mwisho mpya, wa kirafiki zaidi wa mtumiaji (Interface), bila kurekebisha mantiki ya Contract, au kinyume chake, mtu anaweza kupanua Schema ili kuongeza utendaji, na kutoa toleo jipya la Interface Implementation iliyobadilishwa, wakati utekelezaji wa zamani ungebaki kuwa halali kwa utendaji wa kimsingi.

Tunapokusanya Contract mpya, sisi generate Genesis (hatua ya kwanza katika kutoa au kusambaza mali), pamoja na vipengele vyake (Schema, Interface, Interface Implementation). Baada ya hayo, Contract inafanya kazi kikamilifu na inaweza kuenezwa kwa pochi na watumiaji. Njia hii, ambapo Genesis imejumuishwa na vipengele hivi vitatu, inahakikisha ubinafsishaji wa hali ya juu (kila Contract inaweza kuwa na mantiki yake), ugatuaji (kila mtu anaweza kuchangia sehemu fulani), na usalama (uthibitisho unabaki kubainishwa madhubuti na itifaki, bila kutegemea nambari ya On-Chain ya kiholela kama ilivyo kawaida ya minyororo).

Ningependa sasa kuangalia kwa karibu kila moja ya vipengele hivi: **Schema**, **Interface** na **Interface Implementation**.

### Schema

Katika sehemu iliyotangulia, tuliona kwamba katika mfumo wa ikolojia wa RGB, Contract inaundwa na Elements kadhaa: Genesis, ambayo huanzisha hali ya awali, na vipengele vingine kadhaa vya ziada. Madhumuni ya Schema ni kueleza kwa uwazi Business Logic zote za Contract, yaani muundo wa data, aina zinazotumika, shughuli zinazoruhusiwa na masharti yao. Kwa hiyo ni kipengele muhimu sana katika kufanya kazi ya Contract kwa upande wa mteja, kwa kuwa kila mshiriki (Wallet, kwa mfano) lazima aangalie kwamba mabadiliko ya hali inayopokea yanapatana na mantiki iliyofafanuliwa katika Schema.

Schema inaweza kulinganishwa na "darasa" katika upangaji unaolenga kitu (OOP). Kwa ujumla, hutumika kama kielelezo kinachofafanua vipengele vya Contract, kama vile:


- Aina tofauti za Nchi Zinazomilikiwa na Kazi;
- Valencies, yaani, haki maalum ambazo zinaweza kuanzishwa (*kombolewa*) kwa shughuli fulani;
- Sehemu za Global State, ambazo zinaelezea mali ya kimataifa, ya umma na ya pamoja ya Contract;
- Muundo wa Genesis (operesheni ya kwanza kabisa ambayo inawasha Contract);
- Aina zinazoruhusiwa za Mpito za Jimbo na Viendelezi vya Jimbo, na jinsi shughuli hizi zinaweza kurekebisha;
- Metadata inayohusishwa na kila operesheni, kuhifadhi maelezo ya muda au ya ziada;
- Sheria zinazobainisha jinsi data ya ndani ya Contract inaweza kubadilika (kwa mfano, ikiwa sehemu inaweza kubadilika au kuongezwa);
- Misururu ya utendakazi inachukuliwa kuwa halali: kwa mfano, agizo la mpito la kuheshimiwa au seti ya masharti ya kimantiki ya kutimizwa.

![RGB-Bitcoin](assets/fr/071.webp)

Wakati *mtoaji* wa mali kwenye RGB anachapisha Contract, hutoa Genesis na Schema inayohusishwa nayo. Watumiaji au pochi wanaotaka kuingiliana na kipengee hiki hurejesha Schema hii ili kuelewa mantiki ya Contract, na kuweza kuthibitisha baadaye kwamba mabadiliko ambayo watashiriki ni halali.

Hatua ya kwanza, kwa mtu yeyote anayepokea taarifa kuhusu mali ya RGB (k.m. uhamisho wa tokeni), ni kuthibitisha maelezo haya dhidi ya Schema. Hii inajumuisha kutumia mkusanyiko wa Schema kwa:


- Hakikisha kuwa Nchi Zinazomilikiwa, Kazi na Elements nyingine zimefafanuliwa kwa usahihi na kwamba zinaheshimu aina zilizowekwa (kinachojulikana kama *mfumo wa aina kali*);
- Hakikisha kuwa sheria za mpito (hati za uthibitishaji) zimeridhika. Maandishi haya yanaweza kuendeshwa kupitia AluVM, ambayo iko kwa upande wa mteja na ina jukumu la kuthibitisha uthabiti wa Business Logic (kiasi cha uhamisho, hali maalum, nk).

Kwa mazoezi, Schema sio msimbo unaoweza kutekelezwa, kama inavyoonekana katika blockchains ambazo huhifadhi msimbo wa On-Chain (EVM kwenye Ethereum). Kinyume chake, RGB hutenganisha Business Logic (declarative) kutoka kwa msimbo unaoweza kutekelezwa kwenye Blockchain (ambayo ni mdogo kwa nanga za siri). Kwa hivyo, Schema huamua sheria, lakini matumizi ya sheria hizi hufanyika nje ya Blockchain, kwenye tovuti ya kila mshiriki, kulingana na kanuni ya Client-side Validation.

Schema lazima iundwe kabla ya kutumiwa na programu za RGB. Mkusanyiko huu hutoa faili ya jozi (k.m. `.RGB`) au faili ya binary iliyosimbwa kwa njia fiche (`.rgba`). Wakati Wallet inaingiza faili hii, inajua:


- Jinsi kila aina ya data (integers, miundo, arrays...) inaonekana kama shukrani kwa mfumo wa aina kali;
- Jinsi Genesis inapaswa kupangwa (kuelewa uanzishaji wa mali);
- Aina tofauti za utendakazi (Mipito ya Jimbo, Viendelezi vya Jimbo) na jinsi zinavyoweza kurekebisha hali ;
- Sheria za uandishi (zilizoletwa katika Schema) ambazo injini ya AluVM itatumika ili kuangalia uhalali wa shughuli.

Kama ilivyoelezwa katika sura zilizopita, *mfumo wa aina kali* hutupatia umbizo la usimbaji dhabiti na dhabiti: anuwai zote, ziwe Nchi Zinazomilikiwa, Mataifa ya Ulimwenguni au Dhamana, zimefafanuliwa kwa usahihi (ukubwa, mipaka ya chini na ya juu ikiwa ni lazima, aina iliyotiwa sahihi au isiyotiwa saini, n.k.). Pia inawezekana kufafanua miundo ya kiota, kwa mfano kusaidia kesi za matumizi tata.

Kwa hiari, Schema inaweza kurejelea mzizi `SchemaId`, ambayo hurahisisha utumiaji tena wa muundo msingi uliopo (kiolezo). Kwa njia hii, unaweza kubadilisha Contract au kuunda tofauti (k.m. aina mpya ya ishara) kutoka kwa kiolezo kilichothibitishwa tayari. Utaratibu huu unaepuka hitaji la kuunda upya kandarasi nzima, na kuhimiza kusawazisha mbinu bora.

Jambo lingine muhimu ni kwamba mantiki ya mageuzi ya serikali (uhamisho, sasisho, nk) imeelezwa katika Schema kwa namna ya maandiko, sheria na masharti. Kwa hiyo, ikiwa mtengenezaji wa Contract anataka kuidhinisha upya au kuweka utaratibu wa kuchoma (uharibifu wa ishara), anaweza kutaja maandiko yanayofanana ya AluVM katika sehemu ya uthibitishaji wa Schema.

#### Tofauti kutoka kwa blockchains za On-Chain zinazoweza kupangwa

Tofauti na mifumo kama Ethereum, ambapo msimbo wa Smart contract (unaoweza kutekelezwa) umeandikwa kwenye Blockchain yenyewe, RGB huhifadhi Contract (mantiki yake) off-chain, katika mfumo wa hati iliyokusanywa ya kutangaza. Hii ina maana kwamba:


- Hakuna VM ya Turing-kamili inayoendesha katika kila nodi ya mtandao wa Bitcoin. Sheria za RGB Contract hazitekelezwi kwenye Blockchain, lakini kwa kila mtumiaji ambaye anataka kuthibitisha hali;
- Data ya Contract haichafui Blockchain: ushahidi wa kriptografia pekee (*ahadi*) ndio uliopachikwa katika shughuli za Bitcoin (kupitia `Tapret` au `Opret`);
- Schema inaweza kusasishwa au kukataliwa (*haraka-mbele*, *sukuma-nyuma*, nk.), bila kuhitaji Fork kwenye Bitcoin Blockchain. Pochi zinahitaji tu kuagiza Schema mpya na kukabiliana na mabadiliko ya makubaliano.

#### Inatumiwa na mtoaji na watumiaji

Wakati *mtoaji* anatengeneza kipengee (kwa mfano, tokeni inayoweza kugundulika isiyo ya mfumuko wa bei), hutayarisha :


- Schema inayoelezea sheria za utoaji, uhamisho, nk.
- Genesis iliyorekebishwa kwa Schema hii (pamoja na jumla ya idadi ya tokeni zilizotolewa, utambulisho wa mmiliki wa kwanza, Valencies yoyote maalum ya kutolewa upya, nk).

Kisha hufanya Schema iliyokusanywa (faili ya `.RGB`) ipatikane kwa watumiaji, ili mtu yeyote anayepokea uhamisho wa tokeni hii aweze kuangalia uthabiti wa operesheni ndani ya nchi. Bila Schema hii, mtumiaji hangeweza kutafsiri data ya hali au kuangalia kwamba inatii sheria za Contract.

Kwa hivyo wakati Wallet mpya inataka kusaidia mali, inahitaji tu kujumuisha Schema husika. Utaratibu huu unawezesha kuongeza uoanifu kwa aina mpya za vipengee vya RGB, bila kubadilisha kwa uvamizi msingi wa programu ya Wallet: kinachohitajika ni kuleta binary ya Schema na kuelewa muundo wake.

Schema inafafanua Business Logic katika RGB. Inaorodhesha sheria za mageuzi za Contract, muundo wa data yake (Mataifa Yanayomilikiwa, Global State, Valencies) na hati zinazohusiana za uthibitishaji (zinazoweza kutekelezwa na AluVM). Shukrani kwa hati hii ya kutangaza, ufafanuzi wa Contract (faili iliyokusanywa) imetenganishwa wazi na utekelezaji halisi wa sheria (upande wa mteja). Utengano huu huipa RGB unyumbulifu mkubwa, kuwezesha matukio mbalimbali ya utumiaji (tokeni zinazoweza kuvurugika, NFT, mikataba ya kisasa zaidi) huku ikiepuka ugumu na dosari za kawaida za minyororo ya On-Chain inayoweza kuratibiwa.

#### Mfano wa Schema

Hebu tuangalie mfano halisi wa Schema kwa RGB Contract. Hiki ni dondoo katika Rust kutoka kwa faili `nia.rs` (awali za "*Mali Zisizoweza Kuingiliwa*"), ambayo hufafanua muundo wa tokeni zinazoweza kuvuliwa ambazo haziwezi kutolewa tena zaidi ya Supply yao ya awali (mali isiyo ya mfumuko wa bei). Aina hii ya ishara inaweza kuonekana kuwa sawa, katika ulimwengu wa RGB, wa ERC20 kwenye Ethereum, yaani, tokeni zinazoweza kuvuliwa ambazo zinaheshimu sheria fulani za msingi (k.m. kwenye uhamishaji, uanzishaji wa Supply, n.k.).

Kabla ya kupiga mbizi kwenye nambari, inafaa kukumbuka muundo wa jumla wa RGB Schema. Kuna mfululizo wa matamko ya kuunda:


- `SchemaId` inayowezekana inayoonyesha matumizi ya Schema nyingine ya msingi kama kiolezo;
- **Mataifa ya Ulimwenguni** na **Nchi Zinazomilikiwa** (pamoja na aina zao kali);
- Valencies** (kama ipo);
- **Operesheni** (Genesis, Mipito ya Jimbo, Viendelezi vya Jimbo) inayoweza kurejelea majimbo na wawakilishi hawa;
- **Mfumo wa Aina Madhubuti** unaotumika kuelezea na kuthibitisha data;
- Hati za uthibitishaji** (huendesha kupitia AluVM).

![RGB-Bitcoin](assets/fr/072.webp)

Nambari hapa chini inaonyesha ufafanuzi kamili wa Rust Schema. Tutatoa maoni kwa sehemu, tukifuata maelezo (1) hadi (9) hapa chini:

```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
// definitions of libraries and variables
// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),
// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},
// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},
// ===== PART 5: Valencies =====
valency_types: none!(),
// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},
// ===== PART 7: Extensions =====
extensions: none!(),
// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},
// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```


- (1) - Kichwa cha kazi na SubSchema**

Chaguo za kukokotoa za `nia_schema()` hurejesha `SubSchema`, ikionyesha kuwa Schema hii inaweza kurithi nusu kutoka kwa Schema ya kawaida zaidi. Katika mfumo ikolojia wa RGB, unyumbufu huu unawezesha kutumia tena kiwango fulani cha Elements cha Schema kuu, na kisha kufafanua sheria mahususi kwa Contract inayohusika. Hapa, tunachagua kutowasha urithi, kwa kuwa `sehemu ndogo_ya` itakuwa `Hakuna`.


- (2) - Sifa za jumla: ffv, subset_of, type_system**

Sifa ya `ffv` inalingana na toleo la *songa mbele kwa haraka* la Contract. Thamani ya `sifuri!()` hapa inaonyesha kuwa tuko kwenye toleo la 0 au toleo la awali la Schema hii. Ikiwa ungependa kuongeza utendakazi mpya baadaye (aina mpya ya utendakazi, n.k.), unaweza kuongeza toleo hili ili kuonyesha mabadiliko ya makubaliano.

Mali ya `ndogo_ya: Hakuna` inathibitisha kutokuwepo kwa urithi. Sehemu ya `aina_mfumo` inarejelea mfumo wa aina kali ambao tayari umefafanuliwa katika maktaba ya `aina`. Mstari huu unaonyesha kuwa data zote zinazotumiwa na Contract hutumia utekelezaji madhubuti wa usanifu unaotolewa na maktaba inayohusika.


- (3) - Mataifa ya Kimataifa

Katika kizuizi cha `global_types`, tunatangaza Elements nne. Tunatumia ufunguo, kama vile `GS_NOMINAL` au `GS_ISSUED_SUPPLY`, ili kuzirejelea baadaye:


- `GS_NOMINAL` inarejelea aina ya `DivisibleAssetSpec`, ambayo inaeleza sehemu mbalimbali za tokeni iliyoundwa (jina kamili, tiki, usahihi...);
- `GS_DATA` inawakilisha data ya jumla, kama vile kanusho, metadata, au maandishi mengine;
- `GS_TIMESTAMP` inarejelea tarehe ya toleo;
- `GS_ISSUED_SUPPLY` huweka jumla ya Supply, yaani, idadi ya juu zaidi ya tokeni zinazoweza kuundwa.

Neno kuu `mara moja(...)` linamaanisha kuwa kila moja ya sehemu hizi inaweza kuonekana mara moja pekee.


- (4) - Aina zinazomilikiwa

Katika `aina_zinazomilikiwa`, tunatangaza `OS_ASSET`, ambayo inaelezea hali ya kutambulika. Tunatumia `Mtindo wa Jimbo::Fungible(FungibleType::Unsigned64Bit)`, ikionyesha kwamba idadi ya mali (tokeni) imehifadhiwa kama nambari kamili ya biti 64 isiyotiwa saini. Kwa hivyo, shughuli yoyote itatuma kiasi fulani cha vitengo vya ishara hii, ambayo itathibitishwa kulingana na muundo huu wa nambari uliochapwa madhubuti.


- (5) - Wasifu**

Tunaonyesha `aina_za_upendavyo: hakuna!()`, ambayo ina maana kwamba hakuna Valencies katika Schema hii, kwa maneno mengine hakuna haki maalum au za ziada (kama vile kutoa upya, kuchoma kwa masharti, n.k.). Ikiwa Schema itajumuisha yoyote, itatangazwa katika sehemu hii.


- (6) - Genesis: shughuli za kwanza

Hapa tunaingia sehemu inayotangaza Operesheni za Contract. Genesis inaelezewa na:


- Kutokuwepo kwa `metadata` (uga `metadata: Ty::<SemId>::UNIT.id(None)`) ;
- Mataifa ya Ulimwenguni ambayo lazima yawepo mara moja kila moja (`Mara moja`);
- Orodha ya Kazi ambapo `OS_ASSET` lazima ionekane `OnceOrMore`. Hii ina maana kwamba Genesis inahitaji angalau `OS_ASSET` Assignment moja (kimiliki cha kwanza);
- Hakuna Valency : `valencies: hakuna!()`.

Hivi ndivyo tunavyowekea kikomo ufafanuzi wa suala la tokeni la awali: ni lazima tutangaze Supply iliyotolewa (`GS_ISSUED_SUPPLY`), pamoja na angalau mmiliki mmoja (Owned State ya aina ya `OS_ASSET`).


- (7) - Viendelezi

Sehemu ya `viendelezi: hakuna!()` inaonyesha kuwa hakuna State Extension inayotarajiwa katika Contract hii. Hii ina maana kwamba hakuna operesheni kwa Redeem haki ya dijiti (Valency) au kutekeleza State Extension kabla ya Mpito. Kila kitu kinafanywa kupitia Genesis au Mpito wa Jimbo.


- (8) - Mpito: TS_TRANSFER

Katika `mipito`, tunafafanua `TS_TRANSFER` aina ya operesheni. Tunaeleza kwamba:


- Haina metadata;
- Haibadilishi Global State (ambayo tayari imefafanuliwa katika Genesis);
- Inachukua `OS_ASSETs` moja au zaidi kama ingizo. Hii ina maana ni lazima itumie Nchi Zinazomilikiwa zilizopo;
- Huunda (`kazi`) angalau `OS_ASSET` moja mpya (kwa maneno mengine, mpokeaji au wapokeaji hupokea tokeni);
- Haizalishi Valency mpya.

Huu ni mfano wa tabia ya uhamishaji wa kimsingi, ambao hutumia tokeni kwenye UTXO, kisha huunda Nchi mpya zinazomilikiwa kwa niaba ya wapokeaji, na hivyo kuhifadhi usawa wa jumla ya kiasi kati ya pembejeo na matokeo.


- (9) - Hati ya AluVM na Pointi za Kuingia** (kwa Kifaransa)

Hatimaye, tunatangaza hati ya AluVM (`Hati::AluVM(AluScript { ... })`). Hati hii ina:


- Maktaba moja au zaidi za nje (`libs`) zitakazotumika wakati wa uthibitishaji;
- Viingilio vinavyoelekeza kwenye viamilisho vya utendakazi katika msimbo wa AluVM, unaolingana na uthibitishaji wa Genesis (`ValidateGenesis`) na kila Mpito uliotangazwa (`ValidateTransition(TS_TRANSFER)`).

Msimbo huu wa uthibitishaji unawajibika kutumia Business Logic. Kwa mfano, itaangalia:


- Kwamba `GS_ISSUED_SUPPLY` haipitiki wakati wa Genesis ;
- Kwamba jumla ya `vidokezo` (ishara zilizotumika) ni sawa na jumla ya `kazi` (tokeni zilizopokewa) za `TS_TRANSFER`.

Ikiwa sheria hizi hazitazingatiwa, mpito utazingatiwa kuwa batili.

Mfano huu wa "*Mali Inayoweza Kung'alika Isiyo na Inflatable*" Schema inatupa ufahamu bora zaidi wa muundo wa tokeni rahisi ya RGB inayoweza kuvumbuka ya Contract. Tunaweza kuona kwa uwazi utenganisho kati ya maelezo ya data (Mataifa na Mataifa Yanayomilikiwa), tamko la operesheni (Genesis, Mpito, Viendelezi) na utekelezaji wa uthibitishaji (hati za AluVM). Shukrani kwa mfano huu, ishara hufanya kama ishara ya kawaida ya kuvu, lakini inabaki kuthibitishwa kwa upande wa mteja na haitegemei miundombinu ya On-Chain kutekeleza nambari yake. Ahadi za kriptografia pekee ndizo zilizowekwa kwenye Bitcoin Blockchain.

### Interface

Interface ni Layer iliyoundwa kufanya Contract isomeke na iweze kubadilishwa, na watumiaji (kusoma kwa binadamu) na kwa portfolios (kusoma programu). Kwa hivyo Interface ina jukumu la kulinganishwa na ile ya Interface katika lugha ya programu inayolenga kitu (Java, Rust sifa, n.k.), kwa kuwa inafichua na kufafanua muundo wa utendaji wa Contract, bila kufunua maelezo ya ndani ya Business Logic.

Tofauti na Schema, ambayo ni ya kutangaza na kukusanywa kuwa faili ya binary ambayo ni ngumu kutumia kama ilivyo, Interface hutoa funguo za kusoma zinazohitajika:


- Orodhesha na ueleze Majimbo na Nchi Zinazomilikiwa zilizojumuishwa katika Contract;
- Fikia majina na thamani za kila uga, ili ziweze kuonyeshwa (k.m. kwa ishara, tafuta ticker yake, kiwango cha juu zaidi, nk);
- Tafsiri na uunde Uendeshaji wa Contract (Genesis, State Transition, au State Extension) kwa kuhusisha data na majina yanayoeleweka (k.m., fanya uhamishaji kwa kubainisha kwa uwazi "kiasi" badala ya kitambulishi jozi).

![RGB-Bitcoin](assets/fr/073.webp)

Shukrani kwa Interface, unaweza, kwa mfano, kuandika msimbo katika Wallet ambayo, badala ya kuchezea sehemu, inadhibiti moja kwa moja lebo kama vile "idadi ya ishara", "jina la mali", nk. Kwa njia hii, kusimamia Contract inakuwa angavu zaidi. Kwa njia hii, usimamizi wa Contract unakuwa rahisi zaidi.

#### Operesheni ya jumla

Mbinu hii ina faida nyingi:


- Usanifu:**

Aina sawa ya Contract inaweza kuungwa mkono na kiwango cha Interface, kilichoshirikiwa kati ya utekelezaji kadhaa wa Wallet. Hii hurahisisha utangamano na utumiaji wa msimbo tena.


- Utengano wazi kati ya Schema na Interface:**

Katika muundo wa RGB, Schema (Business Logic) na Interface (uwasilishaji na udanganyifu) ni vyombo viwili vya kujitegemea. Waendelezaji wanaoandika mantiki ya Contract wanaweza kuzingatia Schema, bila kuwa na wasiwasi kuhusu ergonomics au uwakilishi wa data, wakati timu nyingine (au timu sawa, lakini kwa muda tofauti) inaweza kuendeleza Interface.


- Mageuzi yanayobadilika:**

Interface inaweza kurekebishwa au kuongezwa baada ya mali kutolewa, bila kubadilisha Contract yenyewe. Hii ni tofauti kubwa kutoka kwa baadhi ya mifumo ya On-Chain Smart contract, ambapo Interface (mara nyingi huchanganywa na msimbo wa utekelezaji) imegandishwa katika Blockchain.


- Uwezo wa Multi-Interface

Contract hiyo hiyo inaweza kufichuliwa kupitia Violesura tofauti vilivyorekebishwa kulingana na mahitaji mahususi: Interface rahisi kwa mtumiaji wa mwisho, nyingine ya juu zaidi kwa mtoaji anayehitaji kudhibiti utendakazi changamano wa usanidi. Wallet basi inaweza kuchagua Interface ya kuagiza, kulingana na matumizi yake.

![RGB-Bitcoin](assets/fr/074.webp)

Kiutendaji, Wallet inaporejesha RGB Contract (kupitia faili ya `.RGB` au `.rgba`), pia huingiza Interface inayohusishwa, ambayo pia imeundwa. Wakati wa kukimbia, Wallet inaweza, kwa mfano:


- Vinjari orodha ya majimbo na usome majina yao, ili kuonyesha Ticker, Kiasi cha Awali, Tarehe ya Kutolewa, n.k. kwa mtumiaji Interface, badala ya kitambulishi cha nambari kisichoweza kusomeka;
- Tengeneza utendakazi (kama vile uhamisho) kwa kutumia majina ya vigezo dhahiri: badala ya kuandika `kazi { OS_ASSET => 1 }`, inaweza kumpa mtumiaji sehemu ya "Kiasi" katika fomu, na kutafsiri maelezo haya katika sehemu zilizochapwa kwa ukali zinazotarajiwa na Contract.

#### Tofauti na Ethereum na mifumo mingine

Kwenye Ethereum, Interface (iliyofafanuliwa kupitia ABI, *Application Binary Interface*) kwa ujumla inatokana na msimbo uliohifadhiwa wa On-Chain (Smart contract). Inaweza kuwa ya gharama kubwa au ngumu kurekebisha sehemu maalum ya Interface bila kugusa Contract yenyewe. Hata hivyo, RGB inategemea mantiki ya off-chain kabisa, ikiwa na data iliyounga mkono *ahadi* kwenye Bitcoin. Muundo huu unawezesha kurekebisha Interface (au utekelezaji wake) bila kuathiri usalama wa kimsingi wa Contract, kwani uthibitishaji wa sheria za biashara unasalia katika Schema na msimbo unaorejelewa wa AluVM.

#### Mkusanyiko wa Interface

Kama ilivyo kwa Schema, Interface inafafanuliwa katika msimbo wa chanzo (mara nyingi katika Rust) na kukusanywa kuwa `.RGB` au `.rgba` faili. Faili hii ya binary ina taarifa zote zinazohitajika na Wallet kwa:


- Tambua sehemu kwa majina;
- Unganisha kila shamba (na thamani yake) kwa aina kali ya mfumo iliyofafanuliwa katika Contract;
- Jua shughuli mbalimbali zinazoruhusiwa na jinsi ya kuzijenga.

Mara tu Interface imeagizwa, Wallet inaweza kuonyesha kwa usahihi Contract na kupendekeza mwingiliano kwa mtumiaji.

### Violesura vilivyosanifishwa na chama cha LNP/BP

Katika mfumo ikolojia wa RGB, Interface inatumika kutoa maana inayoweza kusomeka na inayoweza kubadilika kwa data na uendeshaji wa Contract. Kwa hivyo Interface inakamilisha Schema, ambayo inaelezea Business Logic ndani (aina kali, hati za uthibitishaji, nk). Katika sehemu hii, tutaangalia Violesura vya kawaida vilivyotengenezwa na chama cha LNP/BP kwa aina za kawaida za Contract (tokeni zinazoweza kuvurugika, NFT, n.k.).

Kama ukumbusho, wazo ni kwamba kila Interface inaeleza jinsi ya kuonyesha na kuendesha Contract kwenye upande wa Wallet, ikizitaja nyuga kwa uwazi (kama vile `spec`, `tika`, `Ugavi uliotolewa`...) na kufafanua shughuli zinazowezekana (kama vile `Transfer,``, `Burnan`). Violesura kadhaa tayari vinafanya kazi, lakini kutakuwa na zaidi na zaidi katika siku zijazo.

#### Baadhi ya violesura vilivyo tayari kutumia

**RGB20** ndiyo Interface ya mali inayoweza kuvu, ambayo inaweza kulinganishwa na kiwango cha Ethereum cha ERC20. Walakini, inakwenda hatua zaidi, ikitoa utendakazi mpana zaidi:


- Kwa mfano, uwezo wa kubadilisha jina la mali (mabadiliko ya *tika* au jina kamili) baada ya kutolewa, au kurekebisha usahihi wake (*migawanyiko ya hisa*);
- Inaweza pia kuelezea taratibu za urejeshaji upya wa pili (wa kikomo au usio na kikomo) na wa kuchoma na kisha uingizwaji, ili kuidhinisha mtoaji kuharibu na kisha kuunda upya mali chini ya hali fulani;

Kwa mfano, RGB20 Interface inaweza kuunganishwa kwa **mpango wa Mali Isiyoweza Kuingiliwa (NIA)**, ambao unaweka Supply ya awali isiyoweza kupunguka, au kwa miradi mingine ya juu zaidi inavyohitajika.

**RGB21** inahusu mikataba ya aina ya NFT, au kwa upana zaidi, maudhui yoyote ya kipekee ya kidijitali, kama vile uwakilishi wa vyombo vya habari dijitali (picha, muziki, n.k.). Mbali na kuelezea suala na uhamisho wa mali moja, inajumuisha vipengele kama vile:


- Usaidizi uliojumuishwa wa kuingizwa moja kwa moja kwa faili (hadi MB 16) katika Contract (kwa ajili ya kurejesha upande wa mteja);
- Uwezekano wa mmiliki kuingiza "*engraving*" katika historia ili kuthibitisha zamani za Ownership za NFT.

**RGB25** ni kiwango cha mseto kinachochanganya vipengele vinavyoweza kuvuliwa na visivyoweza kuvu. Imeundwa kwa ajili ya mali ambayo inaweza kuvumbuliwa kwa kiasi, kama vile tokeni ya mali isiyohamishika, ambapo unataka kugawanya mali huku ukihifadhi kiungo cha mzizi mmoja (kwa maneno mengine, una vipande vya nyumba vinavyoweza kuvuliwa, vinavyounganishwa na nyumba isiyoweza kuvu). Kitaalam, Interface hii inaweza kuunganishwa na **Mali Inayoweza Kuweza Kuonekana* (CFA)** Schema, ambayo inatilia maanani dhana ya kugawanya wakati wa kufuatilia mali asili.

#### Maingiliano chini ya maendeleo

Violesura vingine vimepangwa kwa matumizi maalum zaidi, lakini bado havijapatikana:


- RGB22**, iliyojitolea kwa vitambulisho vya kidijitali, kudhibiti vitambulisho na wasifu wa On-Chain katika mfumo ikolojia wa RGB;
- RGB23**, kwa upigaji chapa wa muda wa juu, kwa kutumia baadhi ya mawazo ya *Opentimestamps*, lakini yenye vipengele vya ufuatiliaji;
- RGB24**, ambayo inalenga sawa na mfumo wa jina la kikoa uliogatuliwa (DNS) sawa na *Huduma ya Jina la Ethereum* ;
- RGB26**, iliyoundwa ili kudhibiti DAO (*Shirika Linalojiendesha Lililogatuliwa*) katika muundo changamano zaidi (utawala, upigaji kura, n.k.);
- RGB30**, sawa na RGB20 lakini kwa umaalum wa kuzingatia utoaji wa awali uliogatuliwa na kutumia Viendelezi vya Jimbo. Hii itatumika kwa mali ambazo utoaji upya unadhibitiwa na vyombo kadhaa, au chini ya masharti bora zaidi.

Bila shaka, kulingana na tarehe ambayo unashauriana na kozi hii, miingiliano hii inaweza kuwa tayari kufanya kazi na kufikiwa.

#### Mfano wa Interface

Kijisehemu hiki cha msimbo wa Rust kinaonyesha [RGB20](https://github.com/RGB-WG/RGB-std/blob/master/src/Interface/rgb20.rs) Interface (mali inayoweza kuvu). Msimbo huu umechukuliwa kutoka kwa faili `rgb20.rs` katika maktaba ya kawaida ya RGB. Hebu tuiangalie ili kuelewa muundo wa Interface na jinsi inavyotoa daraja kati, kwa upande mmoja, Business Logic (iliyofafanuliwa katika Schema) na, kwa upande mwingine, utendaji unaoonekana kwa pochi na watumiaji.

```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());
Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```

Katika Interface hii, tunaona kufanana na muundo wa Schema: tunapata tamko la Global State, Nchi Zinazomilikiwa, Contract Operesheni (Genesis na Transitions), pamoja na kushughulikia makosa. Lakini Interface inaangazia uwasilishaji na upotoshaji wa hizi Elements kwa Wallet au programu nyingine yoyote.

Tofauti na Schema iko katika asili ya aina. Schema hutumia aina kali (kama vile `FungibleType::Unsigned64Bit`) na vitambulishi zaidi vya kiufundi. Interface hutumia majina ya sehemu, macros (`fname!()`, `tn!()`), na marejeleo ya madarasa ya hoja (`ArgSpec`, `OwnedIface::Rights`...). Lengo hapa ni kuwezesha uelewa wa kiutendaji na mpangilio wa Elements kwa Wallet.

Zaidi ya hayo, Interface inaweza kuanzisha utendakazi wa ziada kwa Schema ya msingi (k.m. usimamizi wa `burnEpoch` kulia), mradi tu hii itasalia kulingana na mantiki ya mwisho iliyothibitishwa ya upande wa mteja. Sehemu ya "hati" ya AluVM katika Schema itahakikisha uhalali wa kriptografia, huku Interface inaelezea jinsi mtumiaji (au Wallet) anavyoingiliana na hali na mabadiliko haya.

#### Global State na Kazi

Katika sehemu ya `global_state`, tunapata sehemu kama vile `spec` (maelezo ya kipengee), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Hizi ni nyanja ambazo Wallet inaweza kusoma na kuwasilisha. Kwa mfano:


- `spec` itaonyesha usanidi wa ishara;
- `Ugavi uliotolewa` au `Ugavi uliochomwa` unatupa jumla ya idadi ya tokeni zilizotolewa au kuchomwa, n.k.

Katika sehemu ya `kazi`, tunafafanua majukumu au haki mbalimbali. Kwa mfano:


- `Mmiliki wa mali` inalingana na ushikiliaji wa tokeni (inaweza kuvuliwa *Owned State*) ;
- `burnRight` inalingana na uwezo wa kuchoma tokeni;
- updateRight` inalingana na haki ya kubadilisha jina la mali.

Neno kuu la `umma` au `la faragha` (k.m. `AssignIface::public(...)`) linaonyesha kama majimbo haya yanaonekana (`umma`) au ya siri (`binafsi`). Kuhusu `Req::NoneAuMore`, `Req::Hiari`, zinaonyesha tukio linalotarajiwa.

#### Genesis na mabadiliko

Sehemu ya `Genesis` inaeleza jinsi kipengee kinavyoanzishwa:


- Sehemu za `spec`, `data`, `created`, `issuedSupply` ni za lazima (`ArgSpec::required()`) ;
- Kazi kama vile `Mmiliki wa mali` inaweza kuwepo katika nakala nyingi (`ArgSpec::nyingi()`), ikiruhusu tokeni kusambazwa kwa wamiliki wengi wa awali;
- Sehemu kama vile `InflationAllowance` au `burnEpoch` zinaweza (au haziwezi) kujumuishwa katika Genesis.

Kisha, kwa kila Mpito (`Uhamisho`, `Toleo`, `Kuchoma`...), Interface inafafanua ni sehemu gani utendakazi unatarajia kama ingizo, ni sehemu gani za utendakazi zitazalisha kama pato, na hitilafu zozote zinazoweza kutokea. Kwa mfano:

** Mpito :**


- Ingizo : `iliyotangulia` → lazima iwe `Mmiliki wa mali` ;
- Kazi : `mfaidika` → atakuwa `Mmiliki wa mali` mpya;
- Hitilafu: `NON_EQUAL_AMOUNTS` (Wallet kwa hivyo itaweza kushughulikia hali ambapo jumla ya ingizo hailingani na jumla ya matokeo).

**Mpito `Suala` :**


- Hiari (`hiari: kweli`), kwani utoaji wa ziada sio lazima uamilishwe;
- Ingizo: `imetumika` → `InflationAllowance`, yaani, ruhusa ya kuongeza tokeni zaidi ;
- Kazi: `mnufaika` (tokeni mpya zimepokelewa) na `baadaye` (iliyobaki `Allowance ya mfumuko wa bei`);
- Hitilafu zinazowezekana: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE`, n.k.

**Kuchoma mpito:**


- Ingizo : `kutumika` → a `burnRight` ;
- Globals : `burnedSupply` inahitajika;
- Kazi: `baadaye` → uwezekano wa kuendelea kwa `burnRight` ikiwa hatujachoma kila kitu;
- Hitilafu: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.

Kwa hivyo, kila operesheni inaelezewa kwa njia ambayo inaweza kusomeka kwa Wallet. Hii inafanya uwezekano wa kuonyesha mchoro wa Interface ambapo mtumiaji anaweza kuona kwa uwazi: "Una haki ya kuchoma. Je, ungependa kuchoma kiasi fulani? Msimbo unajua kujaza sehemu ya `burnedSupply` na kuangalia kwamba `burnRight` ni halali.

Kwa muhtasari, ni muhimu kuzingatia kwamba Interface, hata hivyo kamili, haifafanui yenyewe mantiki ya ndani ya Contract. Moyo wa kazi unafanywa na **Schema **, ambayo inajumuisha aina kali, muundo wa Genesis, mabadiliko na kadhalika. Interface inafichua hizi Elements kwa njia angavu zaidi na iliyopewa jina, kwa matumizi katika programu.

Shukrani kwa urekebishaji wa RGB, Interface inaweza kuboreshwa (kwa mfano, kwa kuongeza mpito wa `Rename`, kusahihisha onyesho la uga, n.k.) bila kulazimika kuandika upya Contract nzima. Watumiaji wa Interface hii wanaweza kufaidika mara moja kutokana na maboresho haya, mara tu wanaposasisha faili ya `.RGB` au `.rgba`.

Lakini mara tu unapotangaza Interface, unahitaji kuiunganisha na Schema inayolingana. Hii inafanywa kupitia ***Interface Implementation***, ambayo hubainisha jinsi ya kuweka ramani ya kila sehemu iliyotajwa (kama vile `fname!("Mmiliki wa mali")`) hadi kitambulisho kali (kama vile `OS_ASSET`) kilichofafanuliwa katika Schema. Hii inahakikisha, kwa mfano, kwamba wakati Wallet inadhibiti uwanja wa `burnRight`, hii ndiyo hali ambayo, katika Schema, inaelezea uwezo wa kuchoma tokeni.

### Interface Implementation

Katika usanifu wa RGB, tumeona kwamba kila sehemu (Schema, Interface, nk) inaweza kuendelezwa na kukusanywa kwa kujitegemea. Hata hivyo, bado kuna kipengele kimoja cha lazima ambacho huunganisha vitalu hivi tofauti vya ujenzi pamoja: ***Interface Implementation***. Hiki ndicho kinachoonyesha kwa uwazi vitambulishi au sehemu zilizobainishwa katika Schema (upande wa Business Logic) hadi kwa majina yaliyotangazwa katika Interface (upande wa uwasilishaji na mwingiliano wa watumiaji). Kwa hiyo wakati Wallet inapakia Contract, inaweza kuelewa hasa ni shamba gani linalingana na nini, na jinsi operesheni inayoitwa katika Interface inahusiana na mantiki ya Schema.

Jambo muhimu ni kwamba Interface Implementation haikusudiwi kufichua utendakazi wote wa Schema, wala sehemu zote za Interface: inaweza kuzuiwa kwa kitengo kidogo. Kwa mazoezi, hii inafanya uwezekano wa kuzuia au kuchuja vipengele fulani vya Schema. Kwa mfano, unaweza kuwa na Schema yenye aina nne za uendeshaji, lakini Utekelezaji Interface ambayo inaweka ramani mbili tu kati yao katika muktadha fulani. Kinyume chake, ikiwa Interface inapendekeza vidokezo vya ziada, tunaweza kuchagua kutovitekeleza hapa.

Huu hapa ni mfano wa kawaida wa Interface Implementation, ambapo tunahusisha *Mali Isiyoweza Kuingiliwa Kiasi* (NIA) Schema na RGB20 Interface:

```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();
IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```

Katika Utekelezaji huu Interface :


- Tunarejelea kwa uwazi Schema, kupitia `nia_schema()`, na Interface, kupitia `Rgb20::iface()`. Simu `Schema.schema_id()` na `iface.iface_id()` hutumiwa kwa Anchor Interface Implementation kwenye upande wa mkusanyiko (hii inahusisha vitambulishi vya kriptografia vya vijenzi hivi viwili);
- Uchoraji wa ramani umeanzishwa kati ya Schema Elements na Interface Elements. Kwa mfano, sehemu ya `GS_NOMINAL` katika Schema imeunganishwa kwa mfuatano `"spec"` kwenye upande wa Interface (`NamedField::with(GS_NOMINAL, fname!("spec"))`). Tunafanya vivyo hivyo kwa shughuli, kama vile `TS_TRANSFER`, ambayo tunaunganisha kwa `"Hamisha"` katika Interface... ;
- Tunaweza kuona kwamba hakuna valencies (`valencies: none!()`) au viendelezi (`viendelezi: hakuna!()`), kuonyesha ukweli kwamba NIA hii Contract haitumii vipengele hivi.

Matokeo baada ya kukusanywa ni faili tofauti ya `.RGB` au `.rgba`, itakayoletwa kwenye Wallet pamoja na Schema na Interface. Kwa hivyo, programu inajua jinsi ya kuunganisha kwa uhakika NIA Contract hii (ambayo mantiki yake inaelezewa na Schema) kwa "RGB20" Interface (ambayo hutoa majina ya kibinadamu na hali ya mwingiliano wa ishara zinazoweza kuvutwa), ikitumia Interface Implementation hii kama lango kati ya hizo mbili.

#### Kwa nini kutenganisha Interface Implementation?

Kutengana huongeza kubadilika. Schema moja inaweza kuwa na Utekelezaji kadhaa tofauti wa Interface, kila moja ikipanga seti tofauti za utendakazi. Zaidi ya hayo, Interface Implementation yenyewe inaweza kubadilika au kuandikwa upya bila kuhitaji mabadiliko katika Schema au Interface. Hii inabaki na kanuni ya urekebishaji ya RGB: kila sehemu (Schema, Interface, Interface Implementation) inaweza kubadilishwa na kusasishwa kwa kujitegemea, mradi tu sheria za utangamano zilizowekwa na itifaki zinaheshimiwa (vitambulisho sawa, uthabiti wa aina, nk).

Katika matumizi halisi, wakati Wallet inapakia Contract, lazima:


- Pakia iliyokusanywa **Schema** (ili kujua muundo wa Business Logic);
- Mzigo umekusanywa **Interface** (kuelewa majina na shughuli za upande wa mtumiaji);
- Mzigo umekusanywa **Interface Implementation** (ili kuunganisha mantiki ya Schema kwa majina ya Interface, uendeshaji kwa uendeshaji, shamba kwa shamba).

Usanifu huu wa kawaida hufanya uwezekano wa matumizi kama vile:


- Punguza utendakazi fulani kwa watumiaji fulani: toa Utekelezaji wa Interface ambao hutoa ufikiaji wa uhamishaji wa kimsingi pekee, bila kutoa vitendaji vya kuchoma au kusasisha, kwa mfano;
- Badilisha uwasilishaji: tengeneza Interface Implementation ambayo inabadilisha jina la uwanja katika Interface au ramani tofauti, bila kubadilisha msingi wa Contract;
- Kusaidia miradi mingi: Wallet inaweza kupakia Utekelezaji wa Interface nyingi kwa aina sawa ya Interface, kushughulikia mipango tofauti (mantiki tofauti ya ishara), mradi muundo wao unaendana.

Katika sura inayofuata, tutaangalia jinsi uhamisho wa Contract unavyofanya kazi, na jinsi ankara za RGB zinatolewa.

## Uhamisho wa Contract

<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>

:::video id=75eb5a8d-1910-4155-b5e3-81204c9a8901:::

Katika sura hii, tutachambua mchakato wa uhamisho wa Contract katika mfumo ikolojia wa RGB. Ili kufafanua hili, tutaangalia Alice na Bob, wahusika wetu wakuu, wanaotaka Exchange kuwa na kipengee cha RGB. Pia tutaonyesha baadhi ya manukuu ya amri kutoka kwa zana ya mstari wa amri `RGB`, ili kuona jinsi inavyofanya kazi kwa vitendo.

### Kuelewa uhamisho wa RGB Contract

Hebu tuchukue mfano wa uhamisho kati ya Alice na Bob. Katika mfano huu, tunadhania kwamba Bob anaanza kutumia RGB, wakati Alice tayari ana mali ya RGB katika Wallet yake. Tutaona jinsi Bob anavyoweka mazingira yake, kuingiza Contract husika, kisha kuomba uhamisho kutoka kwa Alice, na hatimaye jinsi Alice anavyotekeleza shughuli halisi kwenye Bitcoin Blockchain.

#### 1) Kufunga RGB Wallet

Kwanza kabisa, Bob anahitaji kusakinisha RGB Wallet, yaani programu inayoendana na itifaki. Hii haina mikataba yoyote mwanzoni. Bob pia atahitaji:


- Bitcoin Wallet ya kusimamia UTXO zako;
- Muunganisho kwa nodi ya Bitcoin (au kwa seva ya Electrum), ili uweze kutambua UTXO zako na kueneza miamala yako kwenye mtandao.

Kama ukumbusho, **Nchi Zinazomilikiwa** katika RGB rejea Bitcoin UTXOs. Kwa hivyo ni lazima tuweze kudhibiti na kutumia UTXO kila wakati katika muamala wa Bitcoin unaojumuisha ahadi za kriptografia (`Tapret` au `Opret`) inayoelekeza kwenye data ya RGB.

#### 2) Upataji wa habari wa Contract

Bob basi anahitaji kuepua data ya Contract ambayo anavutiwa nayo. Data hii inaweza kuzunguka kupitia kituo chochote: tovuti, barua pepe, programu ya kutuma ujumbe... Kwa kawaida, zimepangwa pamoja katika ***Consignment***, yaani, pakiti ndogo ya data iliyo na :


- **Genesis **, ambayo inafafanua hali ya awali ya Contract;
- **Schema**, ambayo inaelezea Business Logic (aina kali, hati za uthibitishaji, nk);
- **Interface**, ambayo inafafanua uwasilishaji Layer (majina ya uwanja, shughuli zinazoweza kupatikana);
- **Interface Implementation**, ambayo inaunganisha kikamilifu Schema na Interface.

![RGB-Bitcoin](assets/fr/075.webp)

Ukubwa wa jumla mara nyingi ni wa mpangilio wa kilobaiti chache, kwani kila kijenzi kwa ujumla kina uzani wa chini ya baiti 200. Pia inaweza kuwezekana kutangaza Consignment hii katika Base58, kupitia chaneli zinazokinza udhibiti (kama vile Nostr au kupitia Lightning Network, kwa mfano), au kama msimbo wa QR.

#### 3) Contract kuagiza na uthibitisho

Mara baada ya Bob kupokea Consignment, anaiingiza kwenye RGB Wallet yake. Hii basi:


- Angalia kwamba Genesis na Schema ni halali;
- Mzigo Interface na Interface Implementation;
- Sasisha data yako ya upande wa mteja Stash.

Bob sasa anaweza kuona mali katika Wallet yake (hata kama bado haimiliki) na kuelewa ni nyanja gani zinapatikana, ni shughuli gani zinazowezekana... Kisha anahitaji kuwasiliana na mtu ambaye anamiliki mali hiyo ili kuhamishwa. Katika mfano wetu, huyu ni Alice.

Mchakato wa kugundua ni nani anayeshikilia mali fulani ya RGB ni sawa na kutafuta mlipaji wa Bitcoin. Maelezo ya muunganisho huu hutegemea matumizi (masoko, njia za mazungumzo ya faragha, ankara, uuzaji wa bidhaa na huduma, mshahara...).

#### 4) Kutoa Invoice

Ili kuanzisha uhamisho wa mali ya RGB, Bob lazima kwanza atoe Invoice. Invoice hii inatumika:


- Mwambie Alice aina ya operesheni itakayofanywa (kwa mfano, `Uhamisho` kutoka kwa RGB20 Interface);
- Mpe Alice na *Seal Definition* ya Bob (yaani UTXO ambapo anataka kupokea mali);
- Bainisha kiasi cha kiambato amilifu kinachohitajika (k.m. 100).

Bob anatumia zana ya `RGB` kwenye mstari wa amri. Tuseme anataka vipimo 100 vya tokeni ambayo `ContractId` yake inajulikana, anataka kutegemea `Tapret`, na kubainisha UTXO yake (`456e3..dfe1:0`) :

```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```

Tutaangalia kwa karibu muundo wa ankara za RGB mwishoni mwa sura hii.

#### 5) maambukizi ya Invoice

Invoice iliyotengenezwa (k.m. kama URL: `RGB:2WBcas9.../RGB20/100+utxob:...`) ina maelezo yote anayohitaji Alice ili kuandaa uhamisho. Kama ilivyo kwa Consignment, inaweza kusimba kwa ushikamano (Base58 au umbizo lingine) na kutumwa kupitia programu ya ujumbe, barua pepe, Nostr...

![RGB-Bitcoin](assets/fr/076.webp)

#### 6) Maandalizi ya shughuli kwa upande wa Alice

Alice anapokea Invoice ya Bob. Katika RGB Wallet yake, ana Stash iliyo na mali ya kuhamishwa. Ili kutumia UTXO iliyo na mali, lazima kwanza generate a PSBT (*Partially Signed Bitcoin Transaction*), yaani, muamala ambao haujakamilika wa Bitcoin, kwa kutumia UTXO aliyonayo:

```bash
alice$ wallet construct tx.psbt
```

Muamala huu wa kimsingi (ambao haujatiwa saini kwa sasa) utatumika kwa Anchor kriptografia Commitment iliyounganishwa na uhamisho kwa Bob. Kwa hivyo, UTXO ya Alice itatumika, na katika matokeo, tutaweka `Tapret` au `Opret` Commitment kwa Bob.

#### 7) Kizazi cha uhamisho Consignment

Kisha, Alice huunda ***Terminal Consignment*** (wakati mwingine huitwa "transfer Consignment") kupitia amri :

```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```

Faili hii mpya ya `Consignment.RGB` ina :


- Historia kamili ya Mpito wa Jimbo inayohitajika ili kuhalalisha mali hadi sasa (tangu Genesis);
- State Transition mpya inayohamisha mali kutoka kwa Alice hadi kwa Bob, kulingana na Invoice Bob imetoa;
- Muamala ambao haujakamilika wa Bitcoin (*Witness Transaction*) (`tx.PSBT`), unaotumia Single-Use Seal ya Alice, iliyorekebishwa ili kujumuisha kriptografia Commitment hadi Bob.

Katika hatua hii, shughuli bado haijatangazwa kwenye mtandao wa Bitcoin. Consignment ni kubwa kuliko Consignment ya msingi, kwani inajumuisha historia nzima (*msururu wa ushahidi*) ili kuthibitisha uhalali wa mali.

#### 8) Bob huangalia na kukubali Consignment

Alice anasambaza hii **Terminal Consignment** kwa Bob. Bob basi:


- Angalia uhalali wa State Transition (hakikisha kwamba historia ni sawa, kwamba sheria za Contract zinaheshimiwa, nk);
- Iongeze kwa Stash yako ya karibu;
- Huenda generate saini (`sig:...`) kwenye Consignment, ili kuthibitisha kwamba imekaguliwa na kuidhinishwa (wakati mwingine huitwa "*payslip*").

```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```

![RGB-Bitcoin](assets/fr/077.webp)

#### 9) Chaguo: Bob anatuma uthibitisho kwa Alice (*karatasi ya malipo*)

Ikiwa Bob anataka, anaweza kutuma saini hii kwa Alice. Hii inaashiria:


- Kwamba inatambua mpito kuwa halali;
- Kwamba anakubali shughuli ya Bitcoin kutangazwa.

Hili si la lazima, lakini linaweza kumpa Alice hakikisho kwamba hakutakuwa na mizozo inayofuata kuhusu uhamisho.

#### 10) Alice anasaini na kuchapisha shughuli hiyo

Alice basi anaweza:


- Angalia saini ya Bob (`RGB angalia <sig>`) ;
- Saini *Witness Transaction* ambayo bado ni PSBT (`Wallet ishara`) ;
- Chapisha Witness Transaction kwenye mtandao wa Bitcoin (`-publish`).

```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```

![RGB-Bitcoin](assets/fr/078.webp)

Baada ya kuthibitishwa, muamala huu unaashiria hitimisho la uhamishaji. Bob anakuwa mmiliki mpya wa mali: sasa ana Owned State inayoelekeza kwa UTXO anayodhibiti, kuthibitishwa na uwepo wa Commitment katika shughuli hiyo.

Kwa muhtasari, hapa kuna mchakato kamili wa uhamishaji:

![RGB-Bitcoin](assets/fr/079.webp)

### Faida za uhamisho wa RGB


- Usiri** :

Alice na Bob pekee ndio wanaoweza kufikia data yote ya State Transition. Wao Exchange habari hii nje ya Blockchain, kupitia mizigo. Ahadi za kriptografia katika shughuli ya Bitcoin hazifichui aina ya mali au kiasi, ambacho kinahakikisha usiri mkubwa zaidi kuliko mifumo mingine ya tokeni ya On-Chain.


- Uthibitishaji wa upande wa mteja** :

Bob anaweza kuangalia uthabiti wa uhamisho kwa kulinganisha *Consignment* na *nanga* katika Bitcoin Blockchain. Yeye haitaji uthibitisho wa mtu wa tatu. Si lazima Alice achapishe historia kamili kwenye Blockchain, ambayo hupunguza mzigo kwenye itifaki ya msingi na kuboresha usiri.


- Atomiki iliyorahisishwa** :

Ubadilishanaji tata (mabadilishano ya atomiki kati ya BTC na mali ya RGB, kwa mfano) yanaweza kufanywa ndani ya shughuli moja, kuepuka hitaji la hati za HTLC au PTLC. Ikiwa makubaliano hayatatangazwa, kila mtu anaweza kutumia tena UTXO zao kwa njia zingine.

### Mchoro wa muhtasari wa uhamisho

Kabla ya kuangalia ankara kwa undani zaidi, hapa kuna mchoro wa muhtasari wa mtiririko wa jumla wa uhamishaji wa RGB:


- Bob anasakinisha RGB Wallet na kupata Contract Consignment ya awali;
- Bob anatoa Invoice akitaja UTXO mahali pa kupokea mali;
- Alice anapokea Invoice, anajenga PSBT na kuzalisha Terminal Consignment;
- Bob anaikubali, anakagua, anaongeza data kwenye Stash yake, na ishara (* payslip*) ikiwa ni lazima;
- Alice huchapisha shughuli hiyo kwenye mtandao wa Bitcoin;
- Uthibitishaji wa shughuli hufanya uhamishaji kuwa rasmi.

![RGB-Bitcoin](assets/fr/080.webp)

Uhamisho unaonyesha uwezo na unyumbulifu wote wa itifaki ya RGB: Exchange ya kibinafsi, iliyoidhinishwa kwa upande wa mteja, iliyotiwa nanga kidogo na kwa busara kwenye Bitcoin Blockchain, na kubakiza usalama bora zaidi wa itifaki (hakuna hatari ya Double-spending). Hii inafanya RGB kuwa mfumo ikolojia wa kuahidi kwa uhamishaji wa thamani ambao ni wa siri zaidi na unaoweza kuenea kuliko minyororo ya On-Chain inayoweza kuratibiwa.

### ankara za RGB

Katika sehemu hii, tutaeleza kwa kina jinsi ** ankara** zinavyofanya kazi katika mfumo ikolojia wa RGB na jinsi zinavyowezesha shughuli (haswa uhamishaji) kutekelezwa na Contract. Kwanza, tutaangalia vitambulishi vinavyotumiwa, kisha jinsi ambavyo vimesimbwa, na hatimaye katika muundo wa Invoice ulioonyeshwa kama URL (umbizo ambalo ni rahisi kutosha kutumika katika pochi).

#### Vitambulisho na usimbaji

Kitambulisho cha kipekee kimefafanuliwa kwa kila mojawapo ya Elements zifuatazo:


- RGB Contract;
- Schema yake (Business Logic) ;
- Interface yake na Interface Implementation;
- Mali yake (ishara, NFT, n.k.),

Upekee huu ni muhimu sana, kwani kila sehemu ya mfumo lazima iweze kutofautishwa. Kwa mfano, Contract X lazima isichanganywe na Contract Y nyingine, na violesura viwili tofauti (RGB20 dhidi ya RGB21, kwa mfano) lazima viwe na vitambulishi tofauti.

Ili kufanya vitambulishi hivi viwe na ufanisi (ukubwa mdogo) na kusomeka, tunatumia:


- usimbaji wa Base58, ambao huepuka matumizi ya herufi zinazochanganya (k.m. `0` na herufi `O`) na kutoa mifuatano mifupi kiasi;
- Kiambishi awali kinachoonyesha asili ya kitambulishi, kwa kawaida katika umbo la `RGB:` au URN sawa.

Kwa mfano, `ContractId` inaweza kuwakilishwa na kitu kama :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Kiambishi awali cha `RGB:` kinathibitisha kwamba hiki ni kitambulisho cha RGB, na si kiungo cha HTTP au itifaki nyingine. Shukrani kwa kiambishi awali hiki, pochi zinaweza kutafsiri kamba kwa usahihi.

#### Sehemu ya kitambulisho

Vitambulishi vya RGB mara nyingi huwa virefu sana, kwani usalama wa msingi (wa kriptografia) unaweza kuhitaji sehemu za biti 256 au zaidi. Ili kuwezesha usomaji na uthibitishaji wa binadamu, sisi *hutenganisha* mifuatano hii katika sehemu kadhaa zinazotenganishwa na kistari (`-`). Kwa hiyo, badala ya kuwa na mfuatano mrefu, usioingiliwa wa wahusika, tunaigawanya katika vizuizi vifupi. Zoezi hili ni la kawaida kwa kadi ya mkopo au nambari za simu, na pia linatumika hapa kwa urahisi wa uthibitishaji. Kwa hivyo, kwa mfano, mtumiaji au mshirika anaweza kuambiwa: "*Tafadhali angalia kuwa kizuizi cha tatu ni `9GEgnyMj7`*", badala ya kulazimika kulinganisha kitu kizima mara moja. Kizuizi cha mwisho mara nyingi hutumika kama **checksum**, ili kuwa na hitilafu au mfumo wa kutambua makosa.

Kwa mfano, `ContractId` katika base58 iliyosimbwa na kugawanywa inaweza kuwa:

```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Kila moja ya dashi huvunja kamba katika sehemu. Hii haiathiri semantiki ya msimbo, uwasilishaji wake tu.

#### Kutumia URLs kwa ankara

RGB Invoice imewasilishwa kama URL. Hii ina maana kwamba inaweza kubofya au kuchanganuliwa (kama msimbo wa QR), na Wallet inaweza kuifasiri moja kwa moja ili kutekeleza muamala. Urahisi huu wa mwingiliano hutofautiana na mifumo mingine ambapo unapaswa kunakili na kubandika vipande mbalimbali vya data katika nyanja tofauti za programu.

Invoice ya tokeni inayoweza kuvutwa (k.m. tokeni ya RGB20) inaweza kuonekana kama hii:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Hebu tuchambue URL hii:


- `RGB:`** (kiambishi awali): inaonyesha kiungo kinachotumia itifaki ya RGB (sawa na `http:` au `Bitcoin:` katika miktadha mingine);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`**: inawakilisha `Kitambulisho cha Mkataba` cha ishara unayotaka kuchezea;
- `/RGB20/100`**: inaonyesha kuwa `RGB20` Interface inatumika na kwamba vitengo 100 vya mali vimeombwa. Sintaksia ni: `/Interface/amount` ;
- `+utxob:`**: inabainisha kwamba taarifa kuhusu mpokeaji UTXO (au, kwa usahihi zaidi, ufafanuzi wa Single-Use Seal) huongezwa;
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`**: hii ni *blinded* UTXO (au Seal Definition). Kwa maneno mengine, Bob ameficha UTXO yake halisi, kwa hivyo mtumaji (Alice) hajui Address ni nini. Anajua tu kwamba kuna Seal halali inayorejelea UTXO inayodhibitiwa na Bob.

Ukweli kwamba kila kitu kinafaa katika URL moja hurahisisha maisha kwa mtumiaji: kubofya au kuchanganua rahisi katika Wallet, na operesheni iko tayari kutekelezwa.

Mtu anaweza kufikiria mifumo ambapo kiweka tiki rahisi (k.m. `USDT`) kinatumika badala ya `ContractId`. Hata hivyo, hii inaweza kuibua matatizo makubwa ya uaminifu na usalama: ticker si rejeleo la kipekee (mikataba kadhaa inaweza kudai kuitwa `USDT`). Tukiwa na RGB, tunataka kitambulishi cha kipekee kisicho na utata. Kwa hivyo kupitishwa kwa mfuatano wa 256-bit, uliosimbwa katika base58 na kugawanywa. Mtumiaji anajua kwamba anadanganya kwa usahihi Contract ambayo kitambulisho chake ni `2WBcas9-yjz...` na si nyingine yoyote.

#### Vigezo vya ziada vya URL

Unaweza pia kuongeza vigezo vya ziada kwa URL, kwa njia sawa na HTTP, kama vile:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```


- `?sig=...`: inawakilisha, kwa mfano, saini inayohusishwa na Invoice, ambayo baadhi ya pochi zinaweza kuthibitisha;
- Ikiwa Wallet haidhibiti saini hii, inapuuza tu parameter hii.

Wacha tuchukue kesi ya NFT kupitia RGB21 Interface. Kwa mfano, tunaweza kuwa na:

```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Hapa tunaona:


- `RGB:`**: kiambishi awali cha URL ;
- `7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: Contract ID (NFT) ;
- rGB21**: Interface kwa mali zisizoweza kuvu (NFT) ;
- `DbwzvSu-4BZU81jEp-...`**: rejeleo dhahiri la sehemu ya kipekee ya NFT, kwa mfano Hash ya blob ya data (media, metadata...) ;
- `+utxob:egXsFnw-...`**: the Seal Definition.

Wazo ni lile lile: sambaza kiungo cha kipekee ambacho Wallet inaweza kutafsiri, ikibainisha kwa uwazi mali ya kipekee itakayohamishwa.

#### Shughuli zingine kupitia URL

URL za RGB hazitumiwi tu kuomba uhamisho. Wanaweza pia kusimba utendakazi wa hali ya juu zaidi, kama vile kutoa tokeni mpya (*utoaji*). Kwa mfano:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Hapa tunapata:


- `RGB:` : itifaki ;
- `2WBcas9-...`: Kitambulisho cha Contract;
- `/RGB20/issue/100000`: inaonyesha kuwa unataka kutumia mpito wa "*Suala*" ili kuunda tokeni 100,000 za ziada;
- `+utxob:`: Seal Definition.

Kwa mfano, Wallet inaweza kusoma: "Nimeombwa kutekeleza oparesheni `suala` kutoka kwa `RGB20` Interface, kwenye Contract kama vile, kwa vitengo 100,000, kwa manufaa ya Single-Use Seal.

Sasa kwa kuwa tumeangalia Elements kuu ya utayarishaji wa RGB, nitakupitisha katika sura inayofuata ya jinsi ya kuchora RGB Contract.

## Kuandaa mikataba mahiri

<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>

:::video id=a3ad6dcd-90b8-4272-9dfc-76c85c859167:::

Katika sura hii, tutachukua mbinu ya hatua kwa hatua ya kuandika Contract, kwa kutumia zana ya mstari wa amri `RGB`. Lengo ni kuonyesha jinsi ya kusakinisha na kuendesha CLI, kukusanya **Schema**, kuagiza **Interface** na **Interface Implementation**, kisha kutoa (*toleo*) mali. Pia tutaangalia mantiki ya msingi, ikiwa ni pamoja na mkusanyiko na uthibitishaji wa hali. Kufikia mwisho wa sura hii, unapaswa kuwa na uwezo wa kuzalisha mchakato na kuunda mikataba yako mwenyewe ya RGB.

Kama ukumbusho, mantiki ya ndani ya RGB inategemea maktaba za Rust ambazo wewe, kama wasanidi, unaweza kuingiza katika miradi yako ili kudhibiti sehemu ya Client-side Validation. Kwa kuongeza, timu ya Chama cha LNP/BP inashughulikia masuala ya kuunganisha lugha nyingine, lakini hili bado halijakamilika. Kwa kuongezea, huluki zingine kama vile Bitfinex zinatengeneza safu zao za ujumuishaji (tutazungumza juu ya haya katika sura 2 za mwisho za kozi). Kwa wakati huu, kwa hivyo, `RGB` CLI ndiyo marejeleo rasmi, hata kama haijasafishwa kwa kiasi.

### Ufungaji na uwasilishaji wa chombo cha RGB

Amri kuu inaitwa tu `RGB`. Imeundwa ili kukumbusha `git`, ikiwa na seti ya amri ndogo za kuchezea kandarasi, kuzivutia, kutoa mali na kadhalika. Bitcoin Wallet haijaunganishwa kwa sasa, lakini itakuwa katika toleo la karibu (0.11). Toleo hili linalofuata litawawezesha watumiaji kuunda na kudhibiti pochi zao (kupitia vifafanuzi) moja kwa moja kutoka kwa `RGB`, ikijumuisha kizazi cha PSBT, uoanifu na maunzi ya nje (k.m. Hardware Wallet) ya kutia sahihi, na ushirikiano na programu kama vile Sparrow. Hii itarahisisha utoaji na uhamishaji wa kipengee kizima.

#### Ufungaji kupitia Cargo

Tunasanikisha zana katika Rust na:

```bash
cargo install rgb-contracts --all-features
```

(Kumbuka: kreti inaitwa `RGB-contracts`, na amri iliyosakinishwa itaitwa `RGB`. Ikiwa kreti inayoitwa `RGB` tayari ilikuwepo, kunaweza kuwa na mgongano, kwa hivyo jina)

Usakinishaji unajumuisha idadi kubwa ya vitegemezi (k.m. uchanganuzi wa amri, ujumuishaji wa Electrum, udhibiti wa uthibitisho usio na maarifa, n.k.).

Mara baada ya ufungaji kukamilika,:

```bash
rgb
```

Uendeshaji `RGB` (bila hoja) huonyesha orodha ya amri ndogo zinazopatikana, kama vile `interfaces`, `Schema`, `import`, `export`, `suala`, `Invoice`, `transfer`, n.k. Unaweza kubadilisha saraka ya hifadhi ya ndani (Schema), kuchagua kumbukumbu zote za mtandao, na kuchagua kumbukumbu za mtandao. (Testnet, Mainnet) au usanidi seva yako ya Electrum.

![RGB-Bitcoin](assets/fr/081.webp)

#### Muhtasari wa kwanza wa vidhibiti

Unapoendesha amri ifuatayo, utaona kwamba `RGB20` Interface tayari imeunganishwa kwa chaguo-msingi:

```bash
rgb interfaces
```

Ikiwa Interface hii haijaunganishwa, linganisha :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Tunga:

```bash
cargo run
```

Kisha ingiza Interface ya chaguo lako:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-Bitcoin](assets/fr/082.webp)

Kwa upande mwingine, tunaambiwa kwamba hakuna Schema bado imeingizwa kwenye programu. Wala hakuna Contract katika Stash. Ili kuiona, endesha amri:

```bash
rgb schemata
```

Kisha unaweza kuiga hazina ili kupata schematics fulani:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-Bitcoin](assets/fr/083.webp)

Hazina hii ina, katika saraka yake ya `src/`, faili kadhaa za Rust (kwa mfano `nia.rs`) ambazo hufafanua miundo (NIA ya "*Asset isiyoweza Kuingiliwa*", UDA ya "*Unique Digital Asset*", n.k.). Kukusanya, unaweza kisha kukimbia:

```bash
cd rgb-schemata
cargo run
```

Hii huzalisha faili kadhaa za `.RGB` na `.rgba` zinazolingana na michoro iliyokusanywa. Kwa mfano, utapata `NonInflatableAsset.RGB`.

#### Inaagiza Schema na Interface Implementation

Sasa unaweza kuleta mpangilio katika `RGB` :

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-Bitcoin](assets/fr/084.webp)

Hii inaiongeza kwa Stash ya ndani. Ikiwa tunaendesha amri ifuatayo, tunaona kwamba Schema sasa inaonekana:

```bash
rgb schemata
```

### Uundaji wa Contract (inatoa)

Kuna njia mbili za kuunda mali mpya:


- Tunaweza kutumia hati au msimbo katika Rust ambayo huunda Contract kwa kujaza sehemu za Schema (Global State, Nchi Zinazomilikiwa, n.k.) na kutoa faili ya `.RGB` au `.rgba`;
- Au tumia amri ndogo ya `suala` moja kwa moja, ukiwa na faili ya YAML (au TOML) inayoelezea sifa za tokeni.

Unaweza kupata mifano katika Rust kwenye folda ya `mifano`, inayoonyesha jinsi unavyounda `ContractBuilder`, jaza `Global State` (jina la kipengee, tiki, Supply, tarehe, n.k.), fafanua Owned State (ambayo UTXO inakusanya *19W-1 yote), Consignment* ambayo unaweza kuuza nje, kuhalalisha na kuagiza katika Stash.

Njia nyingine ni kuhariri mwenyewe faili ya YAML ili kubinafsisha `tika`, `jina`, `Supply`, na kadhalika. Tuseme faili inaitwa `RGB20-demo.yaml`. Unaweza kubainisha:


- `spec`: ticker, jina, usahihi;
- `masharti`: uwanja wa notisi za kisheria;
- `issuedSupply`: kiasi cha tokeni iliyotolewa;
- `Kazi`: inaonyesha Single-Use Seal (*Seal Definition*) na idadi iliyofunguliwa.

Hapa kuna mfano wa faili ya YAML kuunda:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-Bitcoin](assets/fr/085.webp)

Kisha endesha amri tu:

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-Bitcoin](assets/fr/086.webp)

Kwa upande wangu, kitambulishi cha kipekee cha Schema (kitakachoambatanishwa katika nukuu moja) ni `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` na sijaweka mtoaji wowote. Kwa hivyo agizo langu ni:

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Ikiwa hujui kitambulisho cha Schema, endesha amri:

```bash
rgb schemata
```

CLI inajibu kwamba Contract mpya imetolewa na kuongezwa kwa Stash. Ikiwa tutaandika amri ifuatayo, tunaona kwamba sasa kuna Contract ya ziada, inayolingana na ile iliyotolewa hivi karibuni:

```bash
rgb contracts
```

![RGB-Bitcoin](assets/fr/087.webp)

Kisha, amri inayofuata inaonyesha mataifa ya kimataifa (jina, tiki, Supply...) na orodha ya Nchi Zinazomilikiwa, yaani mgao (kwa mfano, tokeni za `PBN` milioni 1 zilizofafanuliwa katika UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-Bitcoin](assets/fr/088.webp)

### Hamisha, ingiza na uthibitishaji

Ili kushiriki Contract hii na watumiaji wengine, inaweza kusafirishwa kutoka Stash hadi :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-Bitcoin](assets/fr/089.webp)

Faili ya `myContractPBN.RGB` inaweza kupitishwa kwa mtumiaji mwingine, ambaye anaweza kuiongeza kwenye Stash yake kwa amri :

```bash
rgb import myContractPBN.rgb
```

Inapoingizwa, ikiwa ni *Contract Consignment* rahisi*, tutapata ujumbe wa "`Inaagiza Consignment RGB`". Ikiwa ni *State Transition Consignment* kubwa zaidi, amri itakuwa tofauti (`RGB kubali`).

Ili kuhakikisha uhalali, unaweza pia kutumia kitendakazi cha uthibitishaji wa ndani. Kwa mfano, unaweza kukimbia:

```bash
rgb validate myContract.rgb
```

#### Stash matumizi, uthibitishaji na maonyesho

Kama ukumbusho, Stash ni orodha ya ndani ya schemas, miingiliano, utekelezaji na mikataba (Genesis + mabadiliko). Kila wakati unapoendesha "kuagiza", unaongeza kipengee kwenye Stash. Stash hii inaweza kutazamwa kwa undani na amri:

```bash
rgb dump
```

![RGB-Bitcoin](assets/fr/090.webp)

Hii itakuwa generate folda yenye maelezo ya Stash nzima.

### Uhamisho na PSBT

Ili kutekeleza uhamisho, utahitaji kudanganya Bitcoin Wallet ya ndani ili kudhibiti ahadi za `Tapret` au `Opret`.

#### generate na Invoice

Mara nyingi, mwingiliano kati ya washiriki katika Contract (k.m. Alice na Bob) hufanyika kupitia kizazi cha Invoice. Ikiwa Alice anataka Bob atekeleze jambo fulani (uhamisho wa ishara, utoaji upya, kitendo katika DAO, n.k.), Alice anaunda Invoice inayoelezea maagizo yake kwa Bob. Kwa hivyo tunayo:


- Alice** (mtoaji wa Invoice) ;
- Bob** (ambaye anapokea na kutekeleza Invoice).

Tofauti na mifumo ikolojia mingine, RGB Invoice haizuiliwi na wazo la malipo. Inaweza kupachika ombi lolote lililounganishwa na Contract: kubatilisha ufunguo, kupiga kura, kuunda mchongo (*engraving*) kwenye NFT, nk. Operesheni inayolingana inaweza kuelezewa katika Contract Interface. Operesheni inayolingana inaweza kuelezewa katika Contract Interface.

Amri ifuatayo inazalisha RGB Invoice:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Na:


- `$Contract`: Kitambulishi cha Contract (*ContractId*) ;
- `$Interface`: Interface itatumika (k.m. `RGB20`) ;
- `$ACTION`: jina la operesheni iliyobainishwa katika Interface (kwa uhamishaji rahisi wa tokeni unaoweza kufungika, hii inaweza kuwa "Hamisha"). Ikiwa Interface tayari inatoa kitendo chaguo-msingi, huhitaji kukiingiza tena hapa;
- `$STATE`: data ya hali ya kuhamishwa (kwa mfano, kiasi cha tokeni ikiwa tokeni inayoweza kuvu itahamishwa);
- `$Seal`: mnufaika (Alice's) Single-Use Seal, yaani marejeleo dhahiri ya UTXO. Bob atatumia maelezo haya kuunda Witness Transaction, na matokeo yanayolingana yatakuwa ya Alice (katika *blinded UTXO* au fomu ambayo haijasimbwa).

Kwa mfano, na amri zifuatazo

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

CLI itakuwa generate na Invoice kama:

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Inaweza kupitishwa kwa Bob kupitia chaneli yoyote (maandishi, msimbo wa QR, nk).

#### Kufanya uhamisho

Kuhamisha kutoka Invoice :


- Bob (ambaye anashikilia ishara katika Stash yake) ana Bitcoin Wallet. Anahitaji kutayarisha shughuli ya Bitcoin (katika mfumo wa PSBT, k.m. `tx.PSBT`) ambayo hutumia UTXO ambapo tokeni zinazohitajika za RGB zinapatikana, pamoja na UTXO moja kwa sarafu (Exchange) ;
- Bob anatoa amri ifuatayo:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Hii inazalisha `Consignment.RGB` faili ambayo ina :
 - Historia ya mpito inayothibitisha kwa Alice kwamba ishara ni za kweli;
 - Mpito mpya unaohamisha ishara kwa Single-Use Seal ya Alice;
 - Witness Transaction (isiyo na saini).
- Bob anatuma faili hii ya `Consignment.RGB` kwa Alice (kwa barua pepe, seva inayoshiriki au itifaki ya RGB-RPC, Storm, n.k.);
- Alice anapokea `Consignment.RGB` na anaikubali katika Stash yake yenyewe:

```bash
alice$ rgb accept consignment.rgb
```


- CLI hukagua uhalali wa mpito na kuiongeza kwenye Stash ya Alice. Ikiwa si sahihi, amri itashindwa na ujumbe wa makosa ya kina. Vinginevyo, inafanikiwa, na inaripoti kwamba shughuli ya sampuli bado haijatangazwa kwenye mtandao wa Bitcoin (Bob anasubiri mwanga wa Green wa Alice);
- Kwa njia ya uthibitisho, amri ya `kukubali` inarejesha saini (*karatasi ya malipo*) ambayo Alice anaweza kutuma kwa Bob ili kumuonyesha kwamba ameidhinisha *Consignment* ;
- Kisha Bob anaweza kusaini na kuchapisha (`--publish`) muamala wake wa Bitcoin:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Mara tu shughuli hii inapothibitishwa On-Chain, Ownership ya mali inachukuliwa kuhamishiwa kwa Alice. Wallet ya Alice, ikifuatilia shughuli ya Mining, inaona Owned State mpya ikionekana katika Stash yake.

Katika sura inayofuata, tutaangalia kwa karibu kuunganisha RGB kwenye Lightning Network.

## RGB kwenye Lightning Network

<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>

:::video id=be25a165-6e23-488c-91d8-3dcfccc6eca1:::

Katika sura hii, ninapendekeza kuchunguza jinsi RGB inaweza kutumika ndani ya Lightning Network, kuunganisha na kuhamisha mali za RGB (tokeni, NFTs, nk) kupitia njia za malipo za off-chain.

Wazo la msingi ni kwamba RGB State Transition (*State Transition*) inaweza kujitolea kwa shughuli ya Bitcoin ambayo, kwa upande wake, inaweza kubaki off-chain hadi chaneli ya Umeme imefungwa. Kwa hivyo, kila wakati kituo kinasasishwa, RGB State Transition mpya inaweza kuingizwa katika shughuli mpya ya kufanya, ambayo inabatilisha mpito wa zamani. Kwa njia hii, njia za Umeme zinaweza kutumika kuhamisha mali za RGB, na zinaweza kupitishwa kwa njia sawa na malipo ya kawaida ya Umeme.

### Uundaji wa kituo na ufadhili

Ili kuunda chaneli ya Umeme inayobeba mali ya RGB, tunahitaji Elements mbili:


- Ufadhili wa Bitcoin ili kuunda 2/2 Multisig ya kituo (UTXO ya msingi kwa kituo);
- Ufadhili wa RGB, ambao hutuma mali kwa Multisig sawa.

Katika masharti ya Bitcoin, shughuli ya ufadhili lazima iwepo ili kufafanua marejeleo ya UTXO, hata ikiwa ina kiasi kidogo tu cha Sats (ni suala la kila pato katika shughuli za siku zijazo za Commitment zilizosalia juu ya kikomo cha Dust sawa). Kwa mfano, Alice anaweza kuamua kutoa 10k Sats na 500 USDT (iliyotolewa kama mali ya RGB). Kwenye shughuli ya ufadhili, tunaongeza Commitment (`Opret` au `Tapret`) ambayo inasimamia RGB State Transition.

![RGB-Bitcoin](assets/fr/091.webp)

Baada ya shughuli ya ufadhili kutayarishwa (lakini bado haijatangazwa), miamala ya Commitment inaundwa ili pande zote mbili ziweze kufunga kituo kwa upande mmoja wakati wowote. Shughuli hizi zinafanana na miamala ya kawaida ya Lightning ya Commitment, isipokuwa tunaongeza pato la ziada lililo na RGB Anchor (OP_RETURN au Taproot) iliyounganishwa na State Transition mpya.

RGB State Transition kisha huhamisha mali kutoka 2/2 Multisig ya ufadhili hadi matokeo ya Commitment Transaction. Faida ya mchakato huu ni kwamba usalama wa hali ya RGB inalingana kabisa na mechanics ya Umeme ya adhabu: ikiwa Bob atatangaza hali ya zamani ya kituo, Alice anaweza kumuadhibu na kutumia matokeo, ili kurejesha ishara zote za Sats na RGB. Kwa hivyo motisha ni nguvu zaidi kuliko katika chaneli ya Umeme bila mali ya RGB, kwani mshambuliaji anaweza kupoteza sio Sats tu, bali pia mali ya kituo cha RGB.

Commitment Transaction iliyotiwa saini na Alice na kutumwa kwa Bob ingeonekana kama hii:

![RGB-Bitcoin](assets/fr/092.webp)

Na Commitment Transaction inayoandamana, iliyosainiwa na Bob na kutumwa kwa Alice, itaonekana kama hii:

![RGB-Bitcoin](assets/fr/093.webp)

### Sasisho la kituo

Malipo yanapotokea kati ya washiriki wawili wa kituo (au wangependa kubadilisha mgao wa mali), wanaunda jozi mpya ya miamala ya Commitment. Kiasi katika Sats kwa kila pato kinaweza au kisichobadilika, kulingana na utekelezaji, kwani jukumu lake kuu ni kuwezesha ujenzi wa UTXO halali. Kwa upande mwingine, pato la OP_RETURN (au Taproot) lazima lirekebishwe ili liwe na RGB Anchor mpya, inayowakilisha usambazaji mpya wa mali katika chaneli.

Kwa mfano, ikiwa Alice atahamisha USDT 30 kwa Bob katika chaneli, State Transition mpya itaakisi salio la 400 USDT kwa Alice na 100 USDT kwa Bob. Muamala wa ahadi huongezwa kwa (au kurekebishwa na) OP_RETURN/Taproot Anchor ili kujumuisha mpito huu. Kumbuka kwamba, kutoka kwa mtazamo wa RGB, ingizo la mpito linabaki kuwa Multisig ya awali (ambapo mali ya On-Chain imetengwa hadi kituo kifungwe). Ni matokeo ya RGB pekee (mgao) yanayobadilika, kulingana na ugawaji upya ulioamuliwa.

Commitment Transaction iliyotiwa saini na Alice, tayari kusambazwa na Bob :

![RGB-Bitcoin](assets/fr/094.webp)

Commitment Transaction iliyotiwa saini na Bob, tayari kusambazwa na Alice :

![RGB-Bitcoin](assets/fr/095.webp)

### Usimamizi wa HTLC

Kwa uhalisia, Lightning Network huwezesha malipo kuelekezwa kupitia chaneli nyingi, kwa kutumia HTLC (*Mikataba ya Hashed Time-Locked*). Ni sawa na RGB: kwa kila malipo ya usafiri kupitia chaneli, pato la HTLC huongezwa kwenye shughuli inayofanyika, na mgao wa RGB unaohusishwa na HTLC hii. Kwa hivyo, yeyote anayetumia pato la HTLC (shukrani kwa siri au baada ya kumalizika kwa muda) anapata mali zote za Sats na RGB zinazohusiana. Kwa upande mwingine, ni wazi unahitaji kuwa na pesa za kutosha barabarani kulingana na mali ya Sats na RGB.

![RGB-Bitcoin](assets/fr/096.webp)

Uendeshaji wa RGB kwenye Umeme kwa hiyo lazima uzingatiwe sambamba na ule wa Lightning Network yenyewe. Ikiwa ungependa kuzama zaidi katika somo hili, ninapendekeza sana uangalie kozi hii nyingine ya kina ya mafunzo:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
### RGB ramani ya kanuni

Hatimaye, kabla ya kuendelea hadi sehemu inayofuata, ningependa kukupa muhtasari wa msimbo unaotumika katika RGB. Itifaki inategemea seti ya maktaba za Rust na vipimo vya chanzo huria. Hapa kuna muhtasari wa hazina kuu na makreti:

![RGB-Bitcoin](assets/fr/097.webp)

#### Client-side Validation


- Hazina**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Kreti** : [client_side_validation](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)

Usimamizi wa uthibitishaji wa off-chain na mantiki ya Matumizi Moja ya Mihuri.

#### Ahadi za Dhahiri za Bitcoin (DBC)


- Hazina**: [bp-core](https://github.com/BP-WG/bp-core)
- Crate**: [bp-dbc](https://crates.io/crates/bp-dbc)

Usimamizi wa uwekaji nanga wa kuamua katika shughuli za Bitcoin (Tapret, OP_RETURN, nk).

#### Multi Protocol Commitment (MPC)


- Hazina**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- Crate** : [commit_verify](https://crates.io/crates/commit_verify)

Michanganyiko mingi ya ushiriki na ujumuishaji na itifaki tofauti.

#### Aina Kali & Usimbaji Mkali


- Maelezo**: [tovuti strict-types.org](https://www.strict-types.org/)
- Hazina**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- Kreti** : [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)

Mfumo madhubuti wa uandishi na ufuataji bainifu unaotumika kwa Client-side Validation.

#### Msingi wa RGB


- Hazina**: [RGB-core](https://github.com/RGB-WG/RGB-core)
- Crate**: [RGB-core](https://crates.io/crates/RGB-core)

Msingi wa itifaki, ambayo inajumuisha mantiki kuu ya uthibitishaji wa RGB.

#### Maktaba ya Kawaida ya RGB & Wallet


- Hazina**: [RGB-std](https://github.com/RGB-WG/RGB-std)
- Crate** : [RGB-std](https://crates.io/crates/RGB-std)

Utekelezaji wa kawaida, usimamizi wa Stash na Wallet.

#### RGB CLI


- Hazina**: [RGB](https://github.com/RGB-WG/RGB)
- Kreti**: [RGB-CLI](https://crates.io/crates/RGB-CLI), [RGB-Wallet](https://crates.io/crates/RGB-Wallet)

`RGB` CLI na kreti Wallet, kwa ajili ya uendeshaji wa kandarasi kwa njia ya amri.

#### RGB Schema


- Hazina**: [RGB-schemata](https://github.com/RGB-WG/RGB-schemata/)

Ina mifano ya michoro (NIA, UDA, n.k.) na utekelezaji wake.

#### AluVM


- Maelezo** : [AluVM.org](https://www.AluVM.org/)
- Hazina**: [AluVM-spec](https://github.com/AluVM/AluVM-spec), [alure](https://github.com/AluVM/alure)
- Kreti**: [AluVM](https://crates.io/crates/AluVM), [aluasm](https://crates.io/crates/aluasm)

Mashine pepe ya msingi ya Usajili inayotumika kuendesha hati za uthibitishaji.

#### Itifaki ya Bitcoin - BP


- Hazina** : [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-Wallet](https://github.com/BP-WG/bp-Wallet)

Viongezi vya kusaidia itifaki ya Bitcoin (shughuli, njia za kupita, nk).

#### Ubiquitous Deterministic Computing - UBIDECO


- Hazina**: [UBIDECO](https://github.com/UBIDECO)

Mfumo ikolojia unaohusishwa na maendeleo ya ubainishaji wa chanzo huria.

# Jengo kwenye RGB

<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>

## DIBA na mradi wa Bitmask

<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>

:::video id=2ec9a181-a8b0-4da2-b7b5-9dfaaaeb10ba:::

Sehemu hii ya mwisho ya kozi inategemea mawasilisho yaliyotolewa na wasemaji mbalimbali kwenye kambi ya boot ya RGB. Inajumuisha ushuhuda na tafakari kuhusu RGB na mfumo wake wa ikolojia, pamoja na mawasilisho ya zana na miradi kulingana na itifaki. Sura hii ya kwanza imesimamiwa na Hunter Beast, na sura mbili zinazofuata na Frederico Tenga.

### Kutoka JavaScript hadi Rust, na kwenye mfumo ikolojia wa Bitcoin

Mwanzoni, Hunter Beast alifanya kazi hasa katika JavaScript. Kisha akagundua **Rust**, ambayo sintaksia yake ilionekana kutopendeza na kukatisha tamaa mwanzoni. Hata hivyo, alikuja kufahamu uwezo wa lugha, udhibiti wa kumbukumbu (*lundo* na *stack*), na usalama na utendaji unaokuja nayo. Anasisitiza kuwa Rust ni uwanja bora wa mafunzo kwa uelewa wa kina wa jinsi kompyuta inavyofanya kazi.

Hunter Beast anasimulia historia yake katika miradi mbalimbali katika mfumo ikolojia wa *Altcoin*, kama vile Ethereum (pamoja na Solidity, TypeScript, n.k.), na baadaye Filecoin. Anaeleza kuwa hapo awali alivutiwa na baadhi ya itifaki, lakini aliishia kuhisi kukatishwa tamaa na wengi wao, sio kwa sababu ya tokenomics zao. Anashutumu motisha za kifedha zenye kutiliwa shaka, uundaji wa mfumuko wa bei wa tokeni ambao unapunguza wawekezaji, na kipengele kinachoweza kuwa cha unyonyaji cha miradi hii. Kwa hiyo aliishia kuchukua msimamo wa **Bitcoin Maximalist**, si haba kwa sababu baadhi ya watu walifungua macho yake kwa mifumo ya kiuchumi ya Bitcoin yenye nguvu zaidi, na uimara wa mfumo huu.

### Rufaa ya RGB na kujenga juu ya tabaka

Kilichomshawishi kwa hakika juu ya umuhimu wa Bitcoin, kwa maneno yake, ilikuwa ugunduzi wa RGB na dhana ya tabaka. Anaamini kuwa utendakazi uliopo kwenye blockchains zingine zinaweza kutolewa tena kwenye tabaka za juu, juu ya Bitcoin, bila kubadilisha itifaki ya msingi.

Mnamo Februari 2022, alijiunga na **DIBA** kufanya kazi mahsusi kwenye RGB, na haswa kwenye **Bitmask** Wallet. Wakati huo, Bitmask ilikuwa bado katika toleo la 0.01 na ilikuwa inaendesha RGB katika toleo la 0.4, tu kwa ajili ya usimamizi wa ishara moja. Anabainisha kuwa hii ilikuwa na mwelekeo mdogo wa kujilinda kuliko leo, kwani mantiki hiyo ilikuwa ya msingi wa seva. Tangu wakati huo, usanifu umebadilika kuelekea mfano huu, unaothaminiwa sana na bitcoiners.

### Misingi ya itifaki ya RGB

Itifaki ya **RGB** ndiyo mfano halisi wa hivi punde na wa juu zaidi wa dhana ya _colored coins_, ambayo tayari imegunduliwa karibu 2012-2013. Wakati huo, timu kadhaa zilikuwa zikitafuta kuhusisha thamani tofauti za Bitcoin kwenye UTXO, ambayo ilisababisha utekelezaji mwingi uliotawanyika. Ukosefu huu wa viwango na mahitaji ya chini wakati huo yalizuia masuluhisho haya kupata nafasi ya kudumu.

Leo, RGB inajulikana kwa uthabiti wake wa kidhana na vipimo vilivyounganishwa kupitia muungano wa LNP/BP. Kanuni hiyo inategemea Client-side Validation. Bitcoin Blockchain huhifadhi tu ahadi za kriptografia (_commitments_, kupitia Taproot au OP_RETURN), huku data nyingi (fasili za Contract, historia za uhamishaji, n.k.) huhifadhiwa na watumiaji wanaohusika. Kwa njia hii, mzigo wa kuhifadhi unasambazwa na usiri wa kubadilishana unaimarishwa, bila kupima Blockchain. Mbinu hii huwezesha uundaji wa vipengee vinavyoweza kuvutwa (**RGB20** kawaida) au vipengee vya kipekee (**RGB21** kiwango), ndani ya mfumo wa msimu na unaoweza kupanuka.

### Kazi ya ishara (RGB20) na mali ya kipekee (RGB21)

Kwa **RGB20**, tunafafanua tokeni inayoweza kuvu kwenye Bitcoin. Mtoaji huchagua _supply_, _precision_, na kuunda _mkataba_ ambapo anaweza kufanya uhamisho. Kila uhamishaji unarejelewa kwa Bitcoin UTXO, ambayo hufanya kazi kama *Single-Use Seal*. Mantiki hii inahakikisha kwamba mtumiaji hataweza kutumia mali sawa mara mbili, kwa kuwa ni mtu pekee anayeweza kutumia UTXO ndiye anayeshikilia ufunguo wa kusasisha hali ya Contract ya upande wa mteja.

**RGB21** inalenga vipengee vya kipekee (au "NFT"). Kipengee hiki kina Supply kati ya 1, na kinaweza kuhusishwa na metadata (faili ya picha, sauti, n.k.) iliyofafanuliwa kupitia uga mahususi. Tofauti na NFTs kwenye minyororo ya kuzuia umma, data na vitambulishi vyake vya MIME vinaweza kubaki vya faragha, kusambazwa kati ya rika-kwa-rika kwa hiari ya mmiliki.

### Suluhisho la Bitmask: Wallet kwa RGB

Ili kutumia uwezo wa RGB kiutendaji, mradi wa **DIBA** umeunda Wallet inayoitwa [Bitmask](https://bitmask.app/). Wazo ni kutoa zana isiyo ya uhifadhi, yenye msingi wa Taproot, inayoweza kufikiwa kama programu ya wavuti au kiendelezi cha kivinjari. Bitmask inasimamia mali zote za RGB20 na RGB21, na inaunganisha njia mbalimbali za usalama:


- Msimbo wa msingi umeandikwa katika Rust, kisha kukusanywa katika WebAssembly ili kukimbia katika mazingira ya JavaScript (React);
- Vifunguo huzalishwa ndani ya nchi, kisha kuhifadhiwa kwa njia fiche ndani ya nchi;
- Data ya serikali (Stash) inahifadhiwa katika kumbukumbu, kuratibiwa na kusimbwa kwa njia fiche kupitia **Carbonado** maktaba, ambayo hufanya ukandamizaji, urekebishaji wa makosa, usimbaji fiche na uthibitishaji wa mtiririko kwa kutumia Blake3.

Shukrani kwa usanifu huu, shughuli zote za mali hufanyika kwa upande wa mteja. Kutoka nje, muamala wa Bitcoin si chochote zaidi ya shughuli ya kawaida ya matumizi ya Taproot, ambayo hakuna mtu angeshuku kuwa pia ina uhamishaji wa tokeni zinazoweza kuvuliwa au NFTs. Kutokuwepo kwa upakiaji kupita kiasi wa On-Chain (hakuna metadata iliyohifadhiwa hadharani) huhakikisha kiwango fulani cha busara na hurahisisha kupinga majaribio ya udhibiti yanayowezekana.

### Usalama na usanifu uliosambazwa

Kwa kadiri itifaki ya RGB inahitaji kila mshiriki kuhifadhi historia yake ya muamala (ili kuthibitisha uhalali wa uhamisho anaopokea), swali la uhifadhi hutokea. Bitmask inapendekeza kusasisha Stash hii ndani ya nchi, kisha itume kwa seva au mawingu kadhaa (hiari). Data inasalia imesimbwa kwa njia fiche na mtumiaji kupitia **Carbonado**, kwa hivyo seva haiwezi kuisoma. Katika tukio la uharibifu wa sehemu, marekebisho ya makosa ya Layer yanaweza kuunda upya maudhui.

Matumizi ya CRDT (_aina ya data iliyojirudia isiyo na migogoro_) huwezesha matoleo tofauti ya Stash kuunganishwa, iwapo yatatofautiana. Kila mtu yuko huru kupangisha data hii popote anapotaka, kwa kuwa hakuna Full node hata moja inayobeba maelezo yote yaliyounganishwa na kipengee. Hii inaonyesha hasa falsafa ya *Client-side Validation*, ambapo kila mmiliki ana wajibu wa kuhifadhi ushahidi wa uhalali wa mali yake ya RGB.

### Kuelekea mfumo mpana wa ikolojia: sokoni, ushirikiano na kazi mpya

Kampuni nyuma ya Bitmask haina kikomo yenyewe kwa maendeleo rahisi ya Wallet. DIBA inakusudia kuendeleza:


- **soko** la kubadilishana tokeni, hasa katika fomu ya **RGB21**;
- Utangamano na pochi zingine (kama vile *Iris Wallet*);
- Uhamisho wa batching** mbinu, yaani uwezekano wa kujumuisha uhamisho kadhaa mfululizo wa RGB katika muamala mmoja.

Wakati huo huo, tunashughulikia **WebBTC** au **WebLN** (viwango vinavyowezesha tovuti kuuliza Wallet kutia sahihi Bitcoin au miamala ya Umeme), na pia uwezo wa "kuchoma kwa simu" maingizo ya Ordinals (ikiwa tunataka kurejesha Ordinals kwa umbizo la busara na nyumbufu la GW-2).

### Hitimisho

Mchakato mzima unaonyesha jinsi mfumo ikolojia wa RGB unavyoweza kutumwa na kupatikana kwa watumiaji wa mwisho kupitia suluhu thabiti za kiufundi. Mpito kutoka kwa mtazamo wa Altcoin hadi maono zaidi ya Bitcoin-centric, pamoja na ugunduzi wa *Client-side Validation*, unaonyesha njia ya kimantiki: tunaelewa kwamba inawezekana kutekeleza utendaji mbalimbali (ishara za kuvu, NFT, mikataba ya smart ...) bila kugawanya Client-side Validation kwa faida ya GW-215 kwa kutumia GW-215 kwa faida ya GW-215 kwa urahisi wa GW-215. shughuli au OP_RETURNs.

**Bitmask** Wallet ni sehemu ya mbinu hii: kwa upande wa Blockchain, unachoona ni shughuli ya kawaida ya Bitcoin; kwa upande wa mtumiaji, unadhibiti mtandao wa Interface ambapo unaunda, Exchange na kuhifadhi kila aina ya vipengee vya off-chain. Mtindo huu kwa uwazi hutenganisha miundombinu ya fedha (Bitcoin) kutoka kwa mantiki ya utoaji na uhamisho (RGB), huku ukihakikisha kiwango cha juu cha usiri na uboreshaji bora.

## Kazi ya Bitfinex kwenye RGB

<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>

:::video id=04555813-516f-4eea-9767-7082c2ea6f01:::

Katika sura hii, kulingana na uwasilishaji wa Frederico Tenga, tunaangalia seti ya zana na miradi iliyoundwa na timu ya Bitfinex iliyojitolea kwa RGB, kwa lengo la kukuza kuibuka kwa mfumo wa ikolojia tajiri na tofauti karibu na itifaki hii. Lengo la awali la timu si kutoa bidhaa mahususi ya kibiashara, bali ni kutoa vizuizi vya ujenzi wa programu, kuchangia itifaki yenyewe ya RGB, na kupendekeza marejeleo madhubuti ya utekelezaji kama vile Wallet ya simu ya mkononi (*Iris Wallet*) au nodi ya Umeme inayotangamana na RGB.

### Usuli na malengo

Tangu karibu 2022, timu ya Bitfinex RGB imekuwa ikijikita katika kutengeneza rundo la teknolojia linalowezesha RGB kutumiwa vibaya na kufanyiwa majaribio kwa ufanisi. Michango kadhaa imetolewa:


- Kushiriki katika msimbo wa chanzo na vipimo vya itifaki, ikiwa ni pamoja na kuandika mapendekezo ya uboreshaji, kurekebisha hitilafu, n.k;
- Zana za watengenezaji kurahisisha ujumuishaji wa RGB katika programu zao;
- Muundo wa simu ya mkononi ya Wallet inayoitwa [Iris](https://iriswallet.com/) ili kujaribu na kuonyesha mbinu bora za kutumia RGB ;
- Uundaji wa nodi ya Umeme iliyobinafsishwa, yenye uwezo wa kudhibiti chaneli zilizo na mali ya RGB;
- Kusaidia timu nyingine kujenga suluhu kwenye RGB, ili kuhimiza utofauti na mfumo ikolojia thabiti.

Mbinu hii inalenga kushughulikia mlolongo mzima wa mahitaji: kuanzia maktaba ya kiwango cha chini (*[RGBlib](https://github.com/RGB-Tools/RGB-lib)*), inayowezesha utekelezaji wa Wallet, hadi kipengele cha uzalishaji (nodi ya Umeme, Wallet, n.k. kwa Android).

### Maktaba ya RGBlib: kurahisisha ukuzaji wa programu za RGB

Jambo muhimu katika kuleta demokrasia uundaji wa pochi na programu za RGB ni kufanya uondoaji upatikane rahisi vya kutosha ili wasanidi wasilazimike kujifunza kila kitu kuhusu mantiki ya ndani ya itifaki. Hili ndilo lengo haswa la **RGBlib**, iliyoandikwa katika Rust.

RGBlib hufanya kazi kama daraja kati ya mahitaji yanayonyumbulika sana (lakini wakati mwingine changamano) ya RGB ambayo tumeweza kusoma katika sura zilizopita, na mahitaji madhubuti ya msanidi programu. Kwa maneno mengine, Wallet (au huduma) inayotaka kudhibiti uhamishaji wa tokeni, utoaji wa mali, uthibitishaji, n.k., inaweza kutegemea RGBlib bila kujua kila undani wa kriptografia au kila kigezo cha RGB kinachoweza kugeuzwa kukufaa.

Kitabu cha vitabu kinatoa:


- Vipengele vya utendakazi vya Turnkey kwa kutoa (_issuance_) vipengee (vinafaa au la);
- Uwezo wa kuhamisha (kutuma / kupokea) mali kwa kuendesha vitu rahisi (anwani, kiasi, UTXOs, nk);
- Utaratibu wa kuhifadhi na kupakia taarifa ya hali (*shehena*) inayohitajika kwa Client-side Validation.

Kwa hivyo RGBlib inategemea dhana changamano mahususi kwa RGB (Client-side Validation, Tapret/Opret nanga), lakini inaziweka ndani ili programu ya mwisho isilazimike kupanga upya kila kitu au kufanya maamuzi hatari. Zaidi ya hayo, RGBlib tayari imeunganishwa katika lugha kadhaa (Kotlin na Python), ikifungua mlango wa kutumia zaidi ya ulimwengu rahisi wa Rust.

### Iris Wallet: mfano wa RGB Wallet kwenye Android

Ili kuthibitisha ufanisi wa RGBlib, timu ya Bitfinex imetengeneza **Iris Wallet**, pekee kwenye Android katika hatua hii. Ni simu ya mkononi ya Wallet ambayo inaonyesha matumizi ya mtumiaji sawa na yale ya kawaida ya Bitcoin Wallet: unaweza kutoa kipengee, kutuma, kukipokea, na kutazama historia yake, huku ukibaki kwenye muundo wa kujilinda.

Iris ina idadi ya vipengele vya kuvutia:

**Kwa kutumia seva ya Electrum:**

Kama Wallet yoyote, Iris anahitaji kujua kuhusu uthibitishaji wa miamala kwenye Blockchain. Badala ya kupachika nodi kamili, Iris chaguomsingi kwa seva ya Electrum inayodumishwa na timu ya Bitfinex. Watumiaji wanaweza, hata hivyo, kusanidi seva yao wenyewe au huduma nyingine ya mtu wa tatu. Kwa njia hii, shughuli za Bitcoin zinaweza kuthibitishwa na habari kurejeshwa (indexing) kwa njia ya kawaida.

**Seva ya proksi ya RGB:**

Tofauti na Bitcoin, RGB inahitaji Exchange ya metadata ya off-chain (*shehena*) kati ya mtumaji na mpokeaji. Ili kurahisisha mchakato huu, Iris hutoa suluhisho ambapo mawasiliano hufanyika kupitia seva ya wakala. Wallet inayopokea hutengeneza *Invoice* inayotaja mahali ambapo mtumaji anapaswa kutuma data ya *upande wa mteja*. Kwa chaguomsingi, URL inaelekeza kwa seva mbadala inayopangishwa na timu ya Bitfinex, lakini unaweza kubadilisha seva mbadala hii (au kupangisha yako mwenyewe). Wazo ni kurudi kwenye hali ya utumiaji inayofahamika ambapo mpokeaji anaonyesha msimbo wa QR, na mtumaji huchanganua msimbo huu kwa ajili ya muamala, bila upotoshaji wowote changamano wa ziada.

**Chelezo endelevu:**

Katika muktadha madhubuti wa Bitcoin, kuhifadhi nakala ya seed yako kwa ujumla inatosha (ingawa siku hizi tunapendekeza kuhifadhi nakala za seed na vifafanuzi badala yake). Ukiwa na RGB, hii haitoshi: unahitaji pia kuhifadhi historia ya eneo lako (*shehena*) ikithibitisha kuwa kweli unamiliki mali ya RGB. Kila wakati unapopokea risiti, kifaa huhifadhi data mpya, ambayo ni muhimu kwa matumizi ya baadaye. Iris hudhibiti kiotomatiki hifadhi rudufu iliyosimbwa kwa njia fiche katika Hifadhi ya Google ya mtumiaji. Hili halihitaji uaminifu maalum kwa Google, kwani hifadhi rudufu imesimbwa kwa njia fiche, na chaguo thabiti zaidi (kama vile seva ya kibinafsi) zimepangwa kwa siku zijazo ili kuepusha hatari yoyote ya udhibiti au kufutwa na opereta wa wahusika wengine.

**Sifa zingine:**


- Unda Faucet ili kujaribu au kusambaza kwa haraka tokeni za majaribio au ukuzaji;
- Mfumo wa uidhinishaji (uliopo kati kwa sasa) ili kutofautisha tokeni halali na ile bandia inayonakili tiki maarufu. Katika siku zijazo, uthibitishaji huu unaweza kugawanywa zaidi (kupitia DNS au mifumo mingine).

Kwa ujumla, Iris hutoa hali ya utumiaji inayokaribiana na ile ya Bitcoin Wallet ya kawaida, inayofunika utata wa ziada (usimamizi wa Stash, historia ya *Consignment*, n.k.) shukrani kwa RGBlib na matumizi ya seva mbadala.

### Seva ya wakala na uzoefu wa mtumiaji

Seva ya proksi iliyoletwa hapo juu inastahili kufafanuliwa, kwa kuwa ndiyo ufunguo wa matumizi laini ya mtumiaji. Badala ya mtumaji kulazimika kusambaza *shehena* kwa mpokeaji mwenyewe, muamala wa RGB hufanyika chinichini kupitia :


- Mpokeaji huzalisha *Invoice* (iliyo na, kati ya mambo mengine, wakala Address);
- Mtumaji hutuma (kupitia ombi la HTTP) mradi wa mpito (*Consignment*) kwa wakala ;
- Mpokeaji hupata mradi huu, hutekeleza uthibitishaji wa *upande wa mteja* ndani ya nchi;
- Kisha mpokeaji huchapisha, kupitia proksi, kukubalika (au ikiwezekana kukataliwa) kwa State Transition;
- Mtumaji anaweza kuona hali ya uthibitishaji na, ikikubaliwa, atangaze muamala wa Bitcoin unaokamilisha uhamishaji.

Kwa njia hii, Wallet hufanya karibu kama Wallet ya kawaida. Mtumiaji hajui hatua zote za kati. Hakika, seva mbadala ya sasa haijasimbwa kwa njia fiche wala haijathibitishwa (ambayo inaacha wasiwasi kuhusu usiri na uadilifu), lakini maboresho haya yanawezekana katika matoleo ya baadaye. Dhana ya seva mbadala inasalia kuwa muhimu sana kwa kuunda tena matumizi ya "Ninatuma msimbo wa QR, unachanganua ili ulipe".

### Ushirikiano wa RGB kwenye Lightning Network

Lengo lingine muhimu la kazi ya timu ya Bitfinex ni kufanya Lightning Network iendane na mali ya RGB. Lengo ni kuwasha chaneli za umeme katika USDT (au tokeni nyingine yoyote), na kufaidika kutokana na manufaa sawa na ya Bitcoin kwenye Umeme (miamala ya karibu, uelekezaji, n.k.). Kwa maneno madhubuti, hii inajumuisha kuunda nodi ya Umeme iliyorekebishwa kuwa:


- Fungua chaneli kwa kuweka sio satoshi tu, bali pia mali moja au zaidi ya RGB katika ufadhili wa UTXO Multisig;
- Shughuli za generate Lightning Commitment (upande wa Bitcoin) zikiambatana na mabadiliko ya hali ya RGB yanayolingana. Kila wakati kituo kinasasishwa, mpito wa RGB hufafanua upya usambazaji wa mali katika matokeo ya Umeme;
- Washa kufungwa kwa upande mmoja, ambapo kipengee kinarejeshwa katika UTXO ya kipekee, kwa kutii sheria za Lightning Network (HTLC, kufunga saa, adhabu, n.k.).

Suluhisho hili, linaloitwa "**RGB Nudi ya Umeme**", hutumia LDK (*Lightning Dev Kit*) kama msingi, na huongeza mbinu zinazohitajika kuingiza tokeni za RGB kwenye chaneli. Ahadi za umeme huhifadhi muundo wa kawaida (matokeo yanayoweza kuangaziwa, muda wa saa...), na kwa kuongeza Anchor RGB State Transition (kupitia `Opret` au `Tapret`). Kwa mtumiaji, hii hufungua njia ya chaneli za Umeme katika sarafu za sarafu au katika mali nyingine yoyote iliyotolewa kupitia RGB.

### Uwezo wa DEX na athari kwenye Bitcoin

Mara tu mali kadhaa zinapodhibitiwa kupitia Umeme, inakuwa rahisi kufikiria **atomiki Exchange** kwenye njia moja ya Umeme, kwa kutumia mantiki sawa ya siri na vifunga saa. Kwa mfano, mtumiaji A anashikilia Bitcoin kwenye chaneli moja ya Umeme, na mtumiaji B anashikilia USDT RGB kwenye chaneli nyingine ya Umeme. Wanaweza kuunda njia inayounganisha chaneli zao mbili na kwa wakati mmoja Exchange BTC kwa USDT, bila hitaji la uaminifu. Hili si lolote zaidi ya **mabadilishano ya atomiki** yanayofanyika katika humle kadhaa, na kuwafanya washiriki wa nje kukaribia kutozingatia ukweli kwamba wanafanya biashara, si uelekezaji tu. Mbinu hii inatoa:


- Muda wa kusubiri wa chini sana, kwani kila kitu kinasalia kuwa off-chain kwenye Umeme.
- **faragha** bora zaidi: hakuna anayejua ni biashara, na si njia ya kawaida;
- Kuepuka utangulizi, tatizo la mara kwa mara kwa On-Chain DEX ;
- Gharama zilizopunguzwa (hulipi nafasi ya kizuizi, ada za uelekezaji wa Umeme tu).

Kisha tunaweza kufikiria mfumo ikolojia ambapo nodi za Umeme hutoa bei za kubadilishana (kwa kutoa ukwasi). Kila nodi, ikitaka, inaweza kuchukua nafasi ya _market maker_, kununua na kuuza mali mbalimbali kwenye Umeme. Matarajio haya ya _layer-2_ DEX yanaimarisha wazo kwamba si lazima kwa Fork au kutumia minyororo ya watu wengine kupata ubadilishanaji wa mali uliogatuliwa.

Athari kwa Bitcoin inaweza kuwa chanya: Miundombinu ya Umeme (nodi, chaneli na huduma) itatumika kikamilifu zaidi kutokana na kiasi kinachotolewa na hizi *sarafu za sarafu*, derivatives na tokeni nyinginezo. Wauzaji wanaovutiwa na malipo ya USDT kwenye Umeme wangegundua malipo ya BTC kwenye Umeme (yanadhibitiwa kwa rafu sawa). Matengenezo na ufadhili wa miundombinu ya Lightning Network pia yanaweza kufaidika kutokana na kuzidisha mitiririko hii isiyo ya BTC, ambayo ingefaidi kwa njia isiyo ya moja kwa moja watumiaji wa Bitcoin.

### Hitimisho na rasilimali

Timu ya Bitfinex iliyojitolea kwa RGB inaonyesha, kupitia kazi yake, utofauti wa kile kinachoweza kufanywa juu ya itifaki. Kwa upande mmoja, kuna RGBlib, maktaba ambayo huwezesha muundo wa pochi na programu. Kwa upande mwingine, tuna Iris Wallet, onyesho la vitendo kwenye Android la mtumiaji nadhifu wa mwisho Interface. Hatimaye, ushirikiano wa RGB na Umeme unaonyesha kuwa njia za stablecoin zinawezekana, na kufungua njia ya uwezekano wa DEX ya ugatuzi kwenye Umeme.

Mbinu hii inasalia kuwa ya majaribio na inaendelea kubadilika: maktaba ya RGBlib inaboreshwa tunapoendelea, Iris Wallet inapokea nyongeza za mara kwa mara, na nodi maalum ya Umeme bado si mteja mkuu wa Umeme.

Kwa wale wanaotaka kujifunza zaidi au kuchangia, nyenzo kadhaa zinapatikana, zikiwemo:


- [Hazina za Zana za GitHub RGB](https://github.com/RGB-Tools);
- [Tovuti ya maelezo iliyoundwa kwa Iris Wallet](https://iriswallet.com/) ili kujaribu Wallet kwenye Android.

Katika sura inayofuata, tutaangalia kwa undani jinsi ya kuzindua nodi ya Umeme ya RGB.

## RLN - RGB Njia ya Umeme

<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>

:::video id=d1e9753e-6093-4a47-bcdc-da1aebaefffc:::

Katika sura hii ya mwisho, Frederico Tenga anakuchukua hatua kwa hatua kusanidi nodi ya Umeme ya RGB kwenye mazingira ya Regtest, na kukuonyesha jinsi ya kuunda tokeni za RGB juu yake. Kwa kuzindua nodi mbili tofauti, utagundua pia jinsi ya kufungua chaneli ya Umeme kati yao na vipengee vya Exchange RGB.

Video hii inatumika kama mafunzo, sawa na yale tuliyoshughulikia katika sura iliyotangulia, lakini ililenga hasa Umeme wakati huu!

Nyenzo kuu ya video hii ni hazina ya Github [RGB Lightning Node](https://github.com/RGB-Tools/RGB-lightning-node), ambayo hukurahisishia kuzindua usanidi huu katika Regtest.

### Inapeleka nodi ya Umeme inayolingana na RGB

Mchakato unachukua na kutekeleza dhana zote zilizoangaziwa katika sura zilizopita:


- Wazo kwamba **UTXO** imefungwa kwenye 2/2 Multisig ya kituo cha Umeme inaweza kupokea sio tu bitcoins, lakini pia kuwa Single-Use Seal ya mali ya RGB (fungible au la) ;
- Nyongeza, katika kila shughuli ya ushiriki wa Umeme, ya pato (`Tapret` au `Opret`) inayotolewa kwa kutia nanga RGB State Transition;
- Miundombinu inayohusiana (bitcoind/indexer/proksi) ili kuthibitisha miamala ya Bitcoin na data ya Exchange *upande wa mteja*.

### Tunakuletea RGB-nodi ya umeme

Mradi wa **`RGB-nodi-umeme`** ni Rust daemon kulingana na `Rust-umeme` (LDK) Fork iliyorekebishwa ili kuzingatia kuwepo kwa mali ya RGB katika chaneli. Wakati kituo kinafunguliwa, uwepo wa mali unaweza kutajwa, na kila wakati hali ya kituo inasasishwa, mpito wa RGB huundwa, unaoonyesha usambazaji wa mali katika matokeo ya Umeme. Hii inawezesha:


- Fungua njia za umeme katika USDT, kwa mfano;
- Elekeza tokeni hizi kupitia mtandao, mradi tu njia za uelekezaji ziwe na ukwasi wa kutosha;
- Tumia adhabu ya Umeme na mantiki ya kufunga saa bila marekebisho: kwa urahisi Anchor mpito wa RGB katika pato la ziada la Commitment Transaction.

Nambari bado iko katika hatua ya alpha: tunapendekeza uitumie katika **regtest** au kwenye **Testnet** pekee.

### Ufungaji wa nodi

Kukusanya na kusakinisha binary `RGB-umeme-nodi`, tunaanza kwa kutengeneza hazina na moduli zake ndogo, kisha tunaendesha :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RGB-Bitcoin](assets/fr/098.webp)


- Chaguo la `--recurse-submodules` pia huiga vifaa vidogo vinavyohitajika (pamoja na toleo lililobadilishwa la `Rust-umeme`);
- Chaguo la `--shallow-submodules` huzuia kina cha clone ili kuharakisha upakuaji, huku ikiendelea kutoa ufikiaji wa ahadi muhimu.

Kutoka kwa mzizi wa mradi, endesha amri ifuatayo ya kuunda na kusakinisha binary :

```bash
cargo install --locked --debug --path .
```

![RGB-Bitcoin](assets/fr/099.webp)


- `--imefungwa` inahakikisha kwamba toleo la vitegemezi linaheshimiwa kikamilifu;
- `--debug` si lazima, lakini inaweza kukusaidia kuzingatia (unaweza kutumia `--release` ukipenda);
- `--path .` inaambia `cargo install` kusakinisha kutoka kwenye saraka ya sasa.

Mwishoni mwa amri hii, `RGB-nodi-umeme` inayoweza kutekelezeka itapatikana katika `$CARGO_HOME/bin/` yako. Hakikisha njia hii iko kwenye `$PATH` yako ili uweze kuomba amri kutoka kwa saraka yoyote.

### Mahitaji ya utendaji

Ili kufanya kazi, nodi ya `RGB-umeme` daemon inahitaji uwepo na usanidi wa :


- Nodi ya `bitcoind`**

Kila mfano wa RLN utahitaji kuwasiliana na `bitcoind` ili kutangaza na kufuatilia miamala yake ya On-Chain. Uthibitishaji (kuingia/nenosiri) na URL (mwenyeji/mlango) utahitaji kutolewa kwa daemon.


- Kielezo** (Electrum au Esplora)

daemon lazima iweze kuorodhesha na kuchunguza miamala ya On-Chain, hasa kupata UTXO ambayo mali imewekewa nanga. Utahitaji kubainisha URL ya seva yako ya Electrum au Esplora.


- Seva mbadala ya RGB**

Kama inavyoonekana katika sura zilizopita, **seva mbadala** ni sehemu (ya hiari, lakini inapendekezwa sana) ili kurahisisha Exchange ya *shehena* kati ya programu zingine za Lightning. Kwa mara nyingine tena, ni lazima URL ibainishwe.

Vitambulisho na URL huwekwa wakati daemon _imefunguliwa_ kupitia API. Zaidi juu ya hili baadaye.

### Uzinduzi wa regt

Kwa matumizi rahisi, kuna hati ya `regtest.sh` ambayo huanza kiotomatiki, kupitia Docker, seti ya huduma: `bitcoind`, `electrs` (indexer), `RGB-proxy-server`.

![RGB-Bitcoin](assets/fr/100.webp)

Hii hukuruhusu kuzindua mazingira ya ndani, ya pekee, yaliyosanidiwa mapema. Inaunda na kuharibu vyombo na saraka za data kwenye kila kuwasha upya. Tutaanza kwa kuanza:

```bash
./regtest.sh start
```

Hati hii itakuwa:


- Unda saraka ya `docker/` kuhifadhi;
- Endesha `bitcoind` kwa ukali, pamoja na kiashiria `electrs` na `RGB-proxy-server` ;
- Subiri hadi kila kitu kiko tayari kutumika.

![RGB-Bitcoin](assets/fr/101.webp)

Ifuatayo, tutazindua nodi kadhaa za RLN. Katika ganda tofauti, endesha, kwa mfano (kuzindua nodi 3 za RLN) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RGB-Bitcoin](assets/fr/102.webp)


- Kigezo cha `--network regtest` kinaonyesha matumizi ya usanidi wa regtest;
- `--daemon-mlango-wa-kusikiliza` inaonyesha ni kwenye mlango gani wa REST ambapo nodi ya Umeme itasikiliza kwa simu za API (JSON);
- `--ldk-peer-listening-bandari` hubainisha ni mlango gani wa Umeme wa P2P wa kusikiliza;
- `dataldk0/`, `dataldk1/` ni njia za saraka za hifadhi (kila nodi huhifadhi maelezo yake kivyake).

Unaweza pia kuendesha amri kwenye nodi zako za RLN kutoka kwa kivinjari chako:

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Ili nodi ifungue chaneli, lazima kwanza iwe na bitcoins kwenye Address zinazozalishwa na amri ifuatayo (kwa nodi n°1, kwa mfano):

```bash
curl -X POST http://localhost:3001/address
```

Jibu litakupa Address.

![RGB-Bitcoin](assets/fr/103.webp)

Kwenye Regtest ya `bitcoind`, tutachimba bitcoins chache. Endesha:

```bash
./regtest.sh mine 101
```

![RGB-Bitcoin](assets/fr/104.webp)

Tuma pesa kwa nodi ya Address iliyotolewa hapo juu:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RGB-Bitcoin](assets/fr/105.webp)

Kisha piga block ili kudhibitisha shughuli:

```bash
./regtest.sh mine 1
```

![RGB-Bitcoin](assets/fr/106.webp)

### Uzinduzi wa Testnet (bila Docker)

Ikiwa unataka kujaribu hali ya kweli zaidi, unaweza kuzindua nodi 3 za RLN kwenye Testnet badala ya Regtest, ukielekeza kwenye huduma za umma :

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Kwa chaguo-msingi, ikiwa hakuna usanidi unaopatikana, daemon itajaribu kutumia :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`

Kwa kuingia:


- `bitcoind_rpc_jina_la_mtumiaji`: `mtumiaji`
- `bitcoind_rpc_jina_la_mtumiaji`: `nenosiri`

Unaweza pia kubinafsisha Elements hizi kupitia `init`/`fungua` API.

### Kutoa tokeni ya RGB

Ili kutoa ishara, tutaanza kwa kuunda UTXO "za rangi":

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RGB-Bitcoin](assets/fr/107.webp)

Unaweza, bila shaka, kurekebisha utaratibu. Ili kuthibitisha muamala, tunachimba:

```bash
./regtest.sh mine 1
```

Sasa tunaweza kuunda kipengee cha RGB. Amri itategemea aina ya mali unayotaka kuunda na vigezo vyake. Hapa ninaunda tokeni ya NIA (*Non Inflatable Asset*) inayoitwa "PBN" yenye Supply ya vitengo 1000. `usahihi` hukuruhusu kufafanua mgawanyiko wa vitengo.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RGB-Bitcoin](assets/fr/108.webp)

Jibu linajumuisha kitambulisho cha kipengee kipya kilichoundwa. Kumbuka kutambua kitambulisho hiki. Katika kesi yangu, ni:

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RGB-Bitcoin](assets/fr/109.webp)

Kisha unaweza kuihamisha On-Chain, au kuitenga kwa njia ya Umeme. Hivyo ndivyo tutakavyofanya katika sehemu inayofuata.

### Kufungua kituo na kuhamisha mali ya RGB

Lazima kwanza uunganishe nodi yako kwa rika kwenye Lightning Network kwa kutumia `/connectpeer` amri. Katika mfano wangu, ninadhibiti nodi zote mbili. Kwa hivyo nitapata ufunguo wa umma wa nodi yangu ya pili ya Umeme na amri hii:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

Amri inarudisha ufunguo wa umma wa nodi yangu n°2 :

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RGB-Bitcoin](assets/fr/110.webp)

Kisha, tutafungua kituo kwa kubainisha kipengee husika (`PBN`). Amri ya `/openchannel` hukuruhusu kufafanua ukubwa wa kituo katika satoshis na uchague kujumuisha kipengee cha RGB. Inategemea kile unachotaka kuunda, lakini kwa upande wangu, amri ni:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Pata maelezo zaidi hapa:


- `peer_pubkey_and_opt_addr`: Kitambulisho cha programu rika tunayotaka kuunganisha kwake (ufunguo wa umma tuliopata hapo awali);
- `capacity_sat`: Jumla ya uwezo wa chaneli katika satoshi;
- `push_msat`: Kiasi katika millisatoshis kilihamishiwa awali kwa rika wakati kituo kinafunguliwa (hapa mara moja ninahamisha 10,000 Sats ili aweze kufanya uhamisho wa RGB baadaye);
- `kiasi_cha_kipengee`: Kiasi cha mali ya RGB kitakachowekwa kwenye kituo ;
- `asset_id` : Kitambulisho cha kipekee cha kipengee cha RGB kinachohusika katika kituo;
- `umma`: Inaonyesha kama kituo kinapaswa kuwekwa hadharani kwa kuelekeza kwenye mtandao.

![RGB-Bitcoin](assets/fr/111.webp)

Ili kudhibitisha shughuli hiyo, vitalu 6 vinachimbwa:

```bash
./regtest.sh mine 6
```

![RGB-Bitcoin](assets/fr/112.webp)

Kituo cha Umeme sasa kimefunguliwa na pia kina tokeni 500 za `PBN` kwenye upande wa nodi n°1. Ikiwa nodi n°2 inataka kupokea tokeni za `PBN`, ni lazima generate iwe Invoice. Hapa ni jinsi ya kufanya hivyo:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

Na:


- `amt_msat`: Invoice kiasi katika millisatoshis (kiwango cha chini 3000 Sats) ;
- `expiry_sec` : Invoice muda wa kuisha kwa sekunde ;
- `asset_id` : Kitambulisho cha kipengee cha RGB kinachohusishwa na Invoice;
- `asset_amount`: Kiasi cha mali ya RGB kitakachohamishwa na Invoice hii.

Kwa kujibu, utapata RGB Invoice (kama ilivyoelezwa katika sura zilizopita):

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RGB-Bitcoin](assets/fr/113.webp)

Sasa tutalipa Invoice hii kutoka nodi ya kwanza, ambayo inashikilia pesa taslimu zinazohitajika na ishara ya `PBN`:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RGB-Bitcoin](assets/fr/114.webp)

Malipo yamefanywa. Hii inaweza kuthibitishwa kwa kutekeleza amri:

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RGB-Bitcoin](assets/fr/115.webp)

Hivi ndivyo jinsi ya kupeleka nodi ya Umeme iliyorekebishwa ili kubeba vipengee vya RGB. Maonyesho haya yanatokana na:


- Mazingira ya regtest (kupitia `./regtest.sh`) au Testnet ;
- Nodi ya umeme (`RGB-nodi-umeme`) kulingana na `bitcoind`, faharasa na `RGB-proxy-server` ;
- Msururu wa API za JSON REST za kufungua/kufunga chaneli, kutoa tokeni, kuhamisha mali kupitia Umeme, n.k.

Shukrani kwa mchakato huu:


- Shughuli za ushiriki wa umeme ni pamoja na pato la ziada (OP_RETURN au Taproot) na uwekaji wa mpito wa RGB;
- Uhamisho unafanywa kwa njia sawa kabisa na malipo ya jadi ya Umeme, lakini kwa kuongeza ishara ya RGB;
- Nodi nyingi za RLN zinaweza kuunganishwa kwenye njia na majaribio ya malipo kwenye nodi nyingi, mradi tu kuna ukwasi wa kutosha katika bitcoins na mali ya RGB kwenye njia.

Mradi unabaki katika hatua ya alpha. Kwa hivyo inashauriwa sana ujiwekee kikomo kwa mazingira ya majaribio (regtest, Testnet).

Fursa zilizofunguliwa na utangamano huu wa LN-RGB ni kubwa: stablecoins kwenye Umeme, DEX Layer-2, uhamisho wa ishara za fungible au NFTs kwa gharama ya chini sana ... Sura za awali zimeelezea usanifu wa dhana na mantiki ya uthibitishaji. Sasa una mtazamo wa vitendo wa jinsi ya kupata nodi kama hiyo, kwa maendeleo yako ya baadaye au majaribio.

# Hitimisho

<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>

## Ukaguzi na Ukadiriaji

<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>

<isCourseReview>true</isCourseReview>
## Hitimisho

<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>

<isCourseConclusion>true</isCourseConclusion>