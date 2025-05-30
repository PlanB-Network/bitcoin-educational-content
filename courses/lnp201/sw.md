---
name: Utangulizi wa Kinadharia kwa Lightning Network
goal: Gundua Lightning Network kutoka kwa mtazamo wa kiufundi
objectives: 
  - Kuelewa uendeshaji wa njia za mtandao.
  - Jifahamishe na masharti HTLC, LNURL, na UTXO.
  - Kusasisha usimamizi wa ukwasi na ada za LNN.
  - Tambua Lightning Network kama mtandao.
  - Kuelewa matumizi ya kinadharia ya Lightning Network.

---
# Safari ya Bitcoin ya Pili ya safu

Ingia ndani ya moyo wa Lightning Network, mfumo muhimu kwa mustakabali wa shughuli za Bitcoin. LNP201 ni kozi ya kinadharia juu ya utendakazi wa kiufundi wa Umeme. Inafichua misingi na taratibu za mtandao huu wa pili wa safu, iliyoundwa kufanya malipo ya Bitcoin haraka, kiuchumi na kwa kiasi kikubwa.

Shukrani kwa mtandao wake wa njia za malipo, Umeme huwezesha miamala ya haraka na salama bila kurekodi kila ubadilishanaji kwenye Bitcoin Blockchain. Katika sura zote, utajifunza jinsi ufunguzi, usimamizi na kufungwa kwa vituo unavyofanya kazi, jinsi malipo yanavyopitishwa kupitia nodi za mpatanishi kwa usalama huku ukipunguza hitaji la uaminifu na jinsi ya kudhibiti ukwasi. Utagundua miamala ya kujitolea , HTLC, funguo za kubatilisha, mbinu za adhabu, uelekezaji wa vitunguu, na ankara ni nini.

Iwe wewe ni mwanzilishi wa Bitcoin au mtumiaji mwenye uzoefu zaidi, kozi hii itatoa taarifa muhimu ili kuelewa na kutumia Lightning Network. Ingawa tutashughulikia baadhi ya misingi ya uendeshaji wa Bitcoin katika sehemu za kwanza, ni muhimu kujua misingi ya uvumbuzi wa Satoshi kabla ya kupiga mbizi kwenye LNP201.

Furahia ugunduzi wako!

+++
# Utangulizi
<partId>9da7290a-3895-49a2-93ea-2a6272ca4af4</partId>

## Muhtasari wa Kozi
<chapterId>f2e71062-5121-4114-a7f8-27df69884ce8</chapterId>

Karibu kwenye kozi ya LNP201!

Mafunzo haya yanalenga kukupa ufahamu wa kina wa kiufundi wa Mtandao wa Umeme, mtandao wa kuwekelea ulioundwa kuwezesha miamala ya haraka na mara nyingi ya bei nafuu ya Bitcoin. Utagundua hatua kwa hatua dhana za kimsingi zinazotawala mfumo huu, kuanzia kufungua njia za malipo hadi mbinu za uelekezaji na usimamizi wa ukwasi.

**Sehemu ya 1: Misingi**
Tutaanza na utangulizi wa jumla wa Mtandao wa Umeme, tukianzisha misingi muhimu kuhusu Bitcoin, anwani zake, UTXO, na jinsi miamala inavyofanya kazi. Uhakiki huu wa kimsingi ni muhimu ili kuelewa jinsi Mtandao wa Umeme unategemea mifumo ya msingi ya blockchain kufanya kazi kwa usalama.

**Sehemu ya 2: Kufungua na Kufunga Chaneli**
Katika sehemu hii, tutachunguza mchakato wa kufungua chaneli, ambayo ni msingi wa Mtandao wa Umeme. Utajifunza jinsi miamala ya malipo inavyoundwa, jukumu la funguo za kubatilisha usalama, na jinsi vituo vinaweza kufungwa kwa ushirikiano au upande mmoja. Kila hatua itaelezewa kwa usahihi na kiufundi ili kukusaidia kufahamu hila zote.

**Sehemu ya 3: Mtandao wa Ukwasi**
Mtandao wa Umeme sio mdogo kwa njia za mtu binafsi; ni mtandao halisi wa malipo. Tutaona jinsi miamala inaweza kupitishwa kupitia nodi za kati kwa kutumia HTLC. Sehemu hii pia itakujulisha changamoto za ukwasi unaoingia na kutoka nje.

**Sehemu ya 4: Zana za Mtandao wa Umeme**
Sehemu hii inawasilisha zana za vitendo za Mtandao wa Umeme, kama vile *Ankara*, *LNURL*, na *Utumaji Muhimu*. Pia utajifunza jinsi ya kudhibiti ukwasi wa vituo vyako, jambo muhimu ili kuhakikisha malipo mepesi na kuongeza ufanisi wa miamala yako kwenye Umeme.

**Sehemu ya 5: Kwenda Zaidi**
Hatimaye, tutahitimisha mafunzo kwa kurejea dhana zilizoshughulikiwa na kuweka njia ya mada za juu zaidi kwa wale wanaotaka kuongeza ujuzi wao wa Mtandao wa Umeme.

Je, uko tayari kufichua mbinu za kiufundi za Mtandao wa Umeme? Hebu tuzame ndani!

# Misingi

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Kuelewa Lightning Network

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::

Karibu kwenye kozi ya LNP201, ambayo inalenga kueleza utendakazi wa kiufundi wa Lightning Network.

Lightning Network ni mtandao wa njia za malipo zilizojengwa juu ya itifaki ya Bitcoin, inayolenga kuwezesha miamala ya haraka na ya gharama nafuu. Inaruhusu uundaji wa njia za malipo kati ya washiriki, ambapo miamala inaweza kufanywa karibu papo hapo na kwa ada ndogo, bila kulazimika kurekodi kila muamala mmoja mmoja kwenye Blockchain. Kwa hivyo, Lightning Network inalenga kuboresha uimara wa Bitcoin na kuifanya itumike kwa malipo ya bei ya chini.

Kabla ya kuchunguza kipengele cha "mtandao", ni muhimu kuelewa dhana ya njia ya malipo kwenye Umeme, jinsi inavyofanya kazi, na maelezo yake mahususi. Hili ndilo somo la sura hii ya kwanza.

### Dhana ya Njia ya Malipo

Njia ya malipo inaruhusu wahusika wawili, hapa Alice na Bob, kufadhili ubadilishanaji kupitia Lightning Network. Kila mhusika mkuu ana nodi, inayoonyeshwa na duara, na chaneli kati yao inawakilishwa na sehemu ya mstari.

![LNP201](assets/en/01.webp)

Katika mfano wetu, Alice ana satoshi 100,000 kwa upande wake wa chaneli, na Bob ana 30,000, kwa jumla ya satoshi 130,000, ambazo zinajumuisha uwezo wa kituo.

Je,Satoshi ni nini?

Satoshi(au "iliyokaa") ni kitengo cha akaunti kwenye Bitcoin. Sawa na senti ya euro, Satoshi ni sehemu tu ya Bitcoin. Satoshi moja ni sawa na 0.00000001 Bitcoin, au milioni mia moja ya Bitcoin. Kutumia Satoshi kunazidi kutumika kadri thamani ya Bitcoin inavyoongezeka.

### Ugawaji wa Fedha katika Chaneli

Hebu turejee kwenye kituo cha malipo. Dhana kuu hapa ni "upande wa kituo". Kila mshiriki ana pesa upande wao wa chaneli: Alice satoshi 100,000 na Bob 30,000. Kama tulivyoona, jumla ya fedha hizi zinawakilisha jumla ya uwezo wa kituo, takwimu iliyowekwa wakati inafunguliwa.

![LNP201](assets/en/02.webp)

Wacha tuchukue mfano wa shughuli za Umeme. Ikiwa Alice anataka kutuma satoshi 40,000 kwa Bob, hii inawezekana kwa sababu ana pesa za kutosha (satoshi 100,000). Baada ya muamala huu, Alice atakuwa na satoshi 60,000 upande wake na Bob 70,000.

![LNP201](assets/en/03.webp)

Uwezo wa kituo, katika satoshi 130,000, unabaki thabiti. Mabadiliko gani ni mgao wa fedha. Mfumo huu hauruhusu kutuma pesa zaidi ya mtu anazo. Kwa mfano, kama Bob alitaka kurudisha satoshi 80,000 kwa Alice, hangeweza, kwa sababu ana 70,000 tu.

Njia nyingine ya kufikiria mgao wa fedha ni kufikiria kitelezi ambacho kinaonyesha mahali pesa ziko kwenye chaneli. Hapo awali, ikiwa na satoshi 100,000 za Alice na 30,000 za Bob, kitelezi kiko upande wa Alice kimantiki. Baada ya shughuli ya satoshi 40,000, kitelezi kitasogea kidogo kuelekea upande wa Bob, ambaye sasa ana satoshi 70,000.

![LNP201](assets/en/04.webp)

Uwakilishi huu unaweza kuwa na manufaa kwa kuwazia salio la fedha katika kituo.

### Kanuni za Msingi za Njia ya Malipo

Jambo la kwanza kukumbuka ni kwamba uwezo wa kituo umewekwa. Ni kama kipenyo cha bomba: huamua kiwango cha juu cha pesa ambacho kinaweza kutumwa kupitia chaneli mara moja.

Hebu tuchukue mfano: ikiwa Alice ana satoshi 130,000 kwa upande wake, anaweza tu kutuma kiwango cha juu cha satoshi 130,000 kwa Bob katika muamala mmoja. Hata hivyo, Bob anaweza kutuma pesa hizi kwa Alice, ama kwa kiasi au kamili.

Kilicho muhimu kuelewa ni kwamba uwezo usiobadilika wa chaneli huweka mipaka ya kiwango cha juu cha muamala mmoja, lakini si jumla ya idadi ya miamala inayowezekana, wala kiasi cha jumla cha fedha zinazobadilishwa ndani ya chaneli.

Unapaswa kuchukua nini kutoka kwa sura hii?


- Uwezo wa kituo umewekwa na huamua kiwango cha juu kinachoweza kutumwa katika shughuli moja.
- Fedha katika kituo hugawanywa kati ya washiriki wawili, na kila mmoja anaweza tu kutuma kwa mwingine fedha anazomiliki kwa upande wake.
- Kwa hivyo Lightning Network inaruhusu ubadilishanaji ya haraka na wenye ufanisi wa fedha, huku ukiheshimu mapungufu yaliyowekwa na uwezo wa njia.

Huu ndio mwisho wa sura hii ya kwanza, ambapo tumeweka msingi wa Lightning Network. Katika sura zinazokuja, tutaona jinsi ya kufungua chaneli na kuzama zaidi katika dhana zinazojadiliwa hapa.

## Bitcoin, Anwani, UTXO, na Miamala

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

:::video id=75323eef-ea03-45ac-9a6e-46d73ca255de:::

Sura hii ni maalum kidogo kwani haitajitolea moja kwa moja kwa Umeme, lakini kwa Bitcoin. Hakika, Lightning Network nisafu ya juu ya Bitcoin. Kwa hivyo ni muhimu kuelewa dhana fulani za kimsingi za Bitcoin ili kufahamu ipasavyo utendakazi wa Umeme katika sura zinazofuata. Katika sura hii, tutapitia misingi ya Bitcoin kupokea anwani, UTXOs, pamoja na utendaji wa shughuli za Bitcoin.

### Anwani za Bitcoin, Funguo za Kibinafsi, na Funguo za Umma

Anwani ya Bitcoin,ni mfululizo wa vibambo vinavyotokana na ufunguo wa umma, ambao umekokotolewa kutoka kwa ufunguo wa faragha, Kama unavyojua, unatumika kufunga bitcoins, ambayo ni sawa na kuzipokea kwenye Wallet yetu.

Ufunguo wa faragha ni kipengele cha siri ambacho hakipaswi kamwe kushirikiwa,huku ufunguo wa umma na Anwani zinaweza kushirikiwa bila hatari ya usalama (ufichuzi wao unawakilisha hatari kwa faragha yako pekee). Huu hapa ni uwakilishi wa pamoja ambao tutaupitisha katika kipindi chote cha mafunzo haya:


- Vifunguo vya faragha vitawakilishwa wima.
- funguo za umma zitawakilishwa mlalo.
- Rangi yao inaonyesha nani anazo (Alice katika chungwa na Bob katika nyeusi...).

### Miamala ya Bitcoin: Kutuma Pesa na Hati

Kwenye Bitcoin, shughuli inahusisha kutuma fedha kutoka Anwani moja hadi nyingine. Hebu tuchukue mfano wa Alice kutuma 0.002 Bitcoin kwa Bob. Alice hutumia ufunguo wa faragha unaohusishwa na Anwani yake ili kutia sahihi muamala, na hivyo kuthibitisha kwamba kwa hakika anaweza kutumia pesa hizi. Lakini ni nini hasa kinatokea nyuma ya shughuli hii? Fedha kwenye Anwani ya Bitcoin zimefungwa na hati , aina ya programu ndogo ambayo inaweka masharti fulani ya kutumia fedha.

Hati ya kawaida zaidi inahitaji sahihu,iliyo na ufunguo wa faragha unaohusishwa na Anwani. Alice anapotia sahihi muamala kwa kutumia ufunguo wake wa faragha, hufungua hati inayozuia pesa, kisha zinaweza kuhamishwa. Uhamishaji wa fedha unahusisha kuongeza hati mpya kwa fedha hizi, ikibainisha kwamba ili kuzitumia wakati huu, sahihi ya ufunguo wa faragha wa Bob itahitajika.

![LNP201](assets/en/05.webp)

### UTXOs: Matokeo ya Muamala Usiotumika

Kwenye Bitcoin, kile ambacho sisi kwa kweli hubadilishana sio bitcoins moja kwa moja, lakini **UTXOs** (_Matokeo ya Muamala Usiotumia_), ikimaanisha "matokeo ya muamala ambao haujatumika".

UTXO ni kipande cha Bitcoin ambacho kinaweza kuwa na thamani yoyote, kwa mfano,  bitcoins 2,000, bitcoins 8, au hata 8,000 Sats. Kila UTXO imefungwa kwa hati, na ili kuitumia, mtu lazima atimize masharti ya hati, mara nyingi sahihi na ufunguo wa faragha unaolingana na kupokea Anwani.

UTXO haziwezi kugawanywa. Kila wakati hutumiwa kutumia kiasi katika bitcoins wanazowakilisha, lazima zifanyike kwa ukamilifu. Ni kama noti: ikiwa una bili ya €10 na unamdai mwokaji €5, huwezi tu kukata bili katikati. Unapaswa kumpa bili ya €10, na atakupa €5 kama mabadiliko. Hii ni kanuni sawa kwa UTXOs kwenye Bitcoin! Kwa mfano, Alice anapofungua hati kwa ufunguo wake wa faragha, anafungua UTXO nzima. Ikiwa anataka kutuma sehemu tu ya pesa zinazowakilishwa na UTXO hii kwa Bob, anaweza "kuigawanya" kuwa ndogo kadhaa. Kisha atatuma 0.0015 BTC kwa Bob na kutuma salio, 0.0005 BTC, kwa kubadilisha Anwani.

Hapa kuna mfano wa shughuli iliyo na matokeo 2:


- UTXO ya 0.0015 BTC ya Bob, imefungwa kwa hati inayohitaji sahihi ya ufunguo wa kibinafsi wa Bob.
- UTXO ya 0.0005 BTC ya Alice, iliyofungwa na hati inayohitaji sahihi yake mwenyewe.

![LNP201](assets/en/06.webp)

### Anwani zenye saini nyingi

Mbali na anwani rahisi zinazozalishwa kutoka kwa ufunguo mmoja wa umma, inawezekana kuunda anwani zenye saini nyingi kutoka kwa funguo nyingi za umma. Kesi ya kuvutia sana ya Lightning Network ni 2/2 sahihi nyingi za Anwani, zinazotolewa kutoka kwa funguo mbili za umma:

![LNP201](assets/en/07.webp)

Ili kutumia pesa zilizofungwa na Anwani hii ya saini nyingi 2/2, ni muhimu kutia sahihi kwa funguo mbili za kibinafsi zinazohusiana na funguo za umma.

![LNP201](assets/en/08.webp)

Aina hii ya Anwani ndiyo uwakilishwa haswa kwenye Bitcoin Blockchain ya njia za malipo kwenye Lightning Network.

Unapaswa kuchukua nini kutoka kwa sura hii?


- Anwani ya Bitcoin imetolewa kutoka kwa ufunguo wa umma, ambao yenyewe unatokana na ufunguo wa kibinafsi.
- Pesa kwenye Bitcoin zimefungwa na hati, na ili kutumia fedha hizi, ni lazima mtu aridhishe hati, ambayo kwa ujumla inahusisha kutoa sahihi na ufunguo wa faragha unaolingana.
- UTXO ni vipande vya bitcoins vilivyofungwa na maandishi, na kila shughuli kwenye Bitcoin inajumuisha kufungua UTXO na kisha kuunda moja au zaidi mpya kwa kurudi.
- Anwani 2/2 zenye sahihi nyingi zinahitaji sahihi ya funguo mbili za faragha ili kutumia pesa. Anwani hizi mahususi hutumiwa katika muktadha wa Umeme kuunda njia za malipo.

Sura hii ya Bitcoin imeturuhusu kukagua baadhi ya dhana muhimu kwa yale yafuatayo. Katika sura inayofuata, tutagundua hasa jinsi ufunguzi wa njia kwenye Lightning Network inavyofanya kazi.

# Kufungua na Kufunga chaneli

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Ufunguzi wa Kituo

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

:::video id=6098fee1-735e-4d8d-9f57-0faf5fef6d76:::

Katika sura hii, tutaona kwa usahihi zaidi jinsi ya kufungua njia ya malipo kwenye Lightning Network na kuelewa kiungo kati ya operesheni hii na mfumo wa msingi wa Bitcoin.

### Njia za umeme

Kama tulivyoona katika sura ya kwanza, njia ya malipo kwenye Umeme inaweza kulinganishwa na "bomba" la kubadilishana fedha kati ya washiriki wawili (Alice na Bob katika mifano yetu). Uwezo wa kituo hiki unalingana na jumla ya fedha zinazopatikana kwa kila upande. Katika mfano wetu, Alice ana 100,000 satoshi na Bob ana 30,000 satoshi, akitoa jumla ya uwezo wa satoshi 130,000.

![LNP201](assets/en/09.webp)

### Viwango vya Habari vya ubadilishanaji.

Ni muhimu kutofautisha wazi viwango tofauti vya ubadilishanaji kwenye Lightning Network:


- Mawasiliano kati ya rika (Itifaki ya umeme): Hizi ndizo jumbe ambazo nodi za Umeme hutuma kwa kila mmoja ili kuwasiliana. Tutawakilisha jumbe hizi kwa mistari nyeusi iliyokatika katika michoro yetu.
- Njia za malipo (Itifaki ya Umeme): Hizi ndizo njia za kubadilishana fedha kwenye Umeme, ambazo tutawakilisha kwa njia dhabiti nyeusi.
- Shughuli za Bitcoin (Itifaki ya Bitcoin): Hizi ni miamala zilizofanywa kwenye mnyororo, ambazo tutawakilisha kwa laini za chungwa.

![LNP201](assets/en/10.webp)

Ni vyema kutambua kwamba nodi ya Umeme inaweza kuwasiliana kupitia itifaki ya P2P bila kufungua kituo, lakini kwa fedha za kubadilishana, chaneli ni muhimu.

### Hatua za Kufungua Mkondo wa Umeme


- Ujumbe wa ubadilishanaji.: Alice anataka kufungua kituo na Bob. Anamtumia ujumbe ulio na kiasi anachotaka kuweka kwenye chaneli (130,000 Sats) na ufunguo wake wa umma. Bob anajibu kwa kushiriki ufunguo wake wa umma.

![LNP201](assets/en/11.webp)


- Uundaji wa sahihi nyingi za Anwani: Kwa funguo hizi mbili za umma, Alice anaunda 2/2 sahihi nyingi za Anwani, kumaanisha kwamba fedha ambazo baadaye zitawekwa kwenye Anwani hii zitahitaji sahihi zote mbili (Alice na Bob) kutumika.

![LNP201](assets/en/12.webp)


- **Muamala wa amana**: Alice anatayarisha muamala wa Bitcoin ili kuweka fedha kwenye Address hii ya sahihi nyingi. Kwa mfano, anaweza kuamua kutuma Satoshi 130,000 kwa Address hii ya sahihi nyingi. Muamala huu umejengwa lakini bado haujachapishwa kwenye Blockchain.

![LNP201](assets/en/13.webp)


- **Muamala wa uondoaji**: Kabla ya kuchapisha muamala wa amana, Alice hutengeneza muamala wa uondoaji ili aweze kurejesha pesa zake endapo Bob atakabiliwa na tatizo. Hakika, mara tu Alice atakapochapisha shughuli ya kuweka amana, Sats zake zitafungwa kwenye Anwani yenye sahihi 2/2 ambayo inahitaji sahihi yake na sahihi ya Bob kufunguliwa. Alice hulinda dhidi ya hatari hii ya hasara kwa kuunda shughuli ya uondoaji inayomruhusu kurejesha pesa zake.

![LNP201](assets/en/14.webp)


- **Sahihi ya Bob**: Alice anatuma muamala wa amana kwa Bob kama uthibitisho na kumwomba atie sahihi katika shughuli ya uondoaji. Mara tu sahihi ya Bob itakapopatikana kwenye shughuli ya uondoaji, Alice anahakikishiwa kuwa ataweza kurejesha pesa zake wakati wowote, kwani ni sahihi yake pekee ndiyo inayohitajika ili kufungua sahihi nyingi.

![LNP201](assets/en/15.webp)


- **Uchapishaji wa shughuli ya kuweka pesa**: Sahihi ya Bob ikishapatikana, Alice anaweza kuchapisha muamala wa amana kwenye Bitcoin Blockchain, na hivyo kufungua rasmi chaneli ya Umeme kati ya watumiaji hao wawili.

![LNP201](assets/en/16.webp)

### Je, kituo kinafunguliwa lini?

Kituo kinachukuliwa kuwa kimefunguliwa mara tu muamala wa amana unapojumuishwa kwenye kizuizi cha Bitcoin na umefikia kina fulani cha uthibitisho (idadi ya vizuizi vifuatavyo).

**Unapaswa kukumbuka nini kutoka kwa sura hii?**


- Kufungua kituo huanza na ubadilishanaji wa ujumbe kati ya pande hizo mbili (ubadilishanaji wa kiasi na vitufe vya umma).
- Kituo huundwa kwa kuunda 2/2 sahihi nyingi za Anwani na kuweka fedha ndani yake kupitia muamala wa Bitcoin.
- Mtu anayefungua kituo huhakikisha kuwa anaweza kurejesha pesa zake kupitia muamala wa uondoaji uliotiwa sahihi na mhusika mwingine kabla ya kuchapisha muamala wa amana.

Katika sura inayofuata, tutachunguza utendakazi wa kiufundi wa shughuli za Umeme ndani ya chaneli.

## Commitment Transaction

<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

:::video id=c17454f3-14c5-47a0-8c9c-42ee12932bd3:::

Katika sura hii, tutagundua utendakazi wa kiufundi wa shughuli ndani ya kituo kwenye Lightning Network, yaani, wakati fedha zinapohamishwa kutoka upande mmoja wa chaneli hadi mwingine.

### Kikumbusho cha mzunguko wa maisha wa kituo

Kama inavyoonekana hapo awali, chaneli ya Umeme huanza na kufungua kupitia muamala wa Bitcoin. Kituo kinaweza kufungwa wakati wowote, pia kupitia muamala wa Bitcoin. Kati ya dakika hizi mbili, karibu idadi isiyo na kikomo ya shughuli inaweza kufanywa ndani ya chaneli, bila kupitia Bitcoin Blockchain. Hebu tuone kinachotokea wakati wa shughuli katika kituo.

![LNP201](assets/en/17.webp)

### Hali ya awali ya kituo

Wakati wa kufungua chaneli, Alice aliweka Satoshi 130,000 kwenye sahihi nyingi za Address za chaneli. Kwa hivyo, katika hali ya awali, pesa zote ziko upande wa Alice. Kabla ya kufungua kituo, Alice pia alimwagiza Bob atie sahihi muamala wa kujiondoa, ambao ungemruhusu kurejesha pesa zake ikiwa angetaka kufunga kituo.

![LNP201](assets/en/18.webp)

### Miamala ambayo haijachapishwa: Miamala ya kujitegemea.

Wakati Alice anafanya muamala katika kituo kutuma pesa kwa Bob, muamala mpya wa Bitcoin huundwa ili kuonyesha mabadiliko haya katika usambazaji wa fedha. Muamala huu, unaoitwa Commitment Transaction, haujachapishwa kwenye Blockchain lakini unawakilisha hali mpya ya kituo kufuatia shughuli ya Umeme.

Hebu tuchukue mfano na Alice akituma satoshi 30,000 kwa Bob:


- **Hapo awali**: Alice ana satoshi 130,000.
- **Baada ya muamala**: Alice ana satoshi 100,000, na Bob 30,000 satoshi.

Ili kuthibitisha uhamisho huu, Alice na Bob wataunda **muamala mpya wa Bitcoin** ambao haujachapishwa ambao utatuma **satoshi 100,000 kwa Alice** na **satoshi 30,000 kwa Bob** kutoka kwa Address ya sahihi nyingi. Pande zote mbili huunda muamala huu kwa kujitegemea, lakini kwa data sawa (kiasi na anwani). Mara baada ya kujengwa, kila mmoja husaini shughuli na kubadilishana saini yake na nyingine. Hii inaruhusu upande wowote kuchapisha shughuli hiyo wakati wowote ikihitajika ili kurejesha sehemu yao ya kituo kwenye Bitcoin Blockchain kuu.

![LNP201](assets/en/19.webp)

### Mchakato wa Uhamisho: Invoice

Bob anapotaka kupokea pesa, anamtumia Alice _ ankara_kwa Satoshi 30,000. Kisha Alice anaendelea kulipa ankara ya ununuzi hii kwa kuanzisha uhamisho ndani ya chaneli. Kama tulivyoona, mchakato huu unategemea kuundwa na kutiwa sahihi kwa kujitolea kufanya shughuli mpya.

Kila kujitolea shughuli kunawakilisha usambazaji mpya wa fedha katika kituo baada ya uhamisho. Katika mfano huu, baada ya shughuli, Bob ana satoshi 30,000 na Alice ana satoshi 100,000. Iwapo mmoja wa washiriki wawili aliamua kuchapisha kujitolea shughuli hii kwenye Blockchain, ingesababisha kufungwa kwa chaneli na pesa zingegawanywa kulingana na usambazaji huu wa mwisho.

![LNP201](assets/en/20.webp)

### Jimbo Mpya Baada ya Muamala wa Pili

Hebu tuchukue mfano mwingine: baada ya shughuli ya kwanza ambapo Alice alituma satoshi 30,000 kwa Bob, Bob anaamua kutuma satoshi 10,000 kwa Alice. Hii inaunda hali mpya ya kituo. kujitolea shughuli mpya itawakilisha usambazaji huu uliosasishwa:


- Alice sasa ana Satoshi 110,000.
- Bob ina 20,000 Satoshi.

![LNP201](assets/en/21.webp)

Tena, muamala huu haujachapishwa kwenye Blockchain lakini unaweza kuchapishwa wakati wowote iwapo kituo kitafungwa.

Kwa muhtasari, wakati fedha zinapohamishwa ndani ya chaneli ya Umeme:


- Alice na Bob wanaunda kujitolea shughuli mpya, ambayo inaonyesha usambazaji mpya wa fedha.
- Muamala huu wa Bitcoin umetiwa sahihi na pande zote mbili, lakini haujachapishwa kwenye Bitcoin Blockchain mradi tu kituo kibaki wazi.
- Shughuli za kujitolea huhakikisha kwamba kila mshiriki anaweza kurejesha pesa zake wakati wowote kwenye Bitcoin Blockchain kwa kuchapisha muamala wa mwisho uliotiwa sahihi.

Hata hivyo, mfumo huu una dosari inayoweza kutokea, ambayo tutaifanya Anwani katika sura inayofuata. Tutaona jinsi kila mshiriki anaweza kujilinda dhidi ya jaribio la kudanganywa na upande mwingine.

## Ufunguo wa Kubatilisha

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

:::video id=1d850f23-eff1-4725-b284-ce12456a2c26:::

Katika sura hii, tutachunguza kwa undani jinsi miamala inavyofanya kazi kwenye Lightning Network kwa kujadili mbinu zilizopo za kulinda dhidi ya ulaghai, kuhakikisha kwamba kila mhusika anafuata sheria ndani ya mkondo.

### Kikumbusho: Miamala ya kujitolea

Kama inavyoonekana hapo awali, miamala kwenye Umeme inategemea shughuli ambayo haijachapishwa kujitolea. Shughuli hizi zinaonyesha mgawanyo wa sasa wa fedha katika kituo. Wakati shughuli mpya ya Umeme inapofanywa, kujitolea shughuli mpya huundwa na kutiwa sahihi pande zote mbili ili kuonyesha hali mpya ya kituo.

Hebu tuchukue mfano rahisi:


- **Hali ya awali**: Alice ana satoshi 100,000, Bob 30,000 satoshi.
- Baada ya muamala ambapo Alice hutuma **satoshi 40,000** kwa Bob, kujitolea shughuli mpya inasambaza fedha kama ifuatavyo:
  - Alice: **60,000 satoshi**
  - Bob: **70,000 satoshi**

![LNP201](assets/en/22.webp)

Wakati wowote, pande zote mbili zinaweza kuchapisha kujitolea shughuli ya hivi punde iliyotiwa sahihi ili kufunga kituo na kurejesha pesa zao.

### Dosari: Kudanganya kwa Kuchapisha Muamala wa Zamani

Tatizo linaloweza kutokea ikiwa mmoja wa wahusika ataamua kudanganya kwa kuchapisha kujitolea shughuli ya zamani. Kwa mfano, Alice angeweza kuchapisha kujitolea shughuli ya zamani ambapo alikuwa na Satoshi 100,000, ingawa sasa ana 60,000 tu katika uhalisia. Hii ingemruhusu kuiba satoshi 40,000 kutoka kwa Bob.

![LNP201](assets/en/23.webp)

Mbaya zaidi, Alice angeweza kuchapisha shughuli ya kwanza kabisa ya uondoaji, ile kabla ya kituo kufunguliwa, ambapo alikuwa na Satoshi 130,000, na hivyo kuiba fedha za chaneli nzima.

![LNP201](assets/en/24.webp)

### Suluhisho: Ufunguo wa Kubatilisha na Kufunga Muda

Ili kuzuia aina hii ya udanganyifu wa Alice, kwenye Lightning Network, njia za usalama huongezwa kwa miamala ya kujitolea:


- **Saa**: Kila kujitolea shughuli inajumuisha muda wa pesa za Alice. Muda wa kufunga ni Smart contract ya awali ambayo huweka masharti ya muda ambayo lazima yatimizwe ili shughuli iongezwe kwenye kizuizi. Hii inamaanisha kuwa Alice hawezi kurejesha pesa zake hadi idadi fulani ya vitalu ipitishwe ikiwa atachapisha moja ya miamala ya kujitolea. Muda huu unaanza kutumika kutoka kwa uthibitisho wa kujitolea shughuli. Muda wake kwa ujumla ni sawia na ukubwa wa kituo, lakini pia inaweza kusanidiwa kwa mikono.
- **Ufunguo wa Kubatilisha**: Pesa za Alice pia zinaweza kutumiwa mara moja na Bob ikiwa ana ufunguo wa kubatilisha. Ufunguo huu una siri iliyoshikiliwa na Alice na siri iliyoshikiliwa na Bob. Kumbuka kuwa siri hii ni tofauti kwa kila kujitolea shughuli.

Shukrani kwa mifumo hii 2 iliyojumuishwa, Bob ana wakati wa kugundua jaribio la Alice la kudanganya, na kumwadhibu kwa kurudisha matokeo yake kwa ufunguo wa kubatilisha, ambao kwa Bob unamaanisha kurejesha pesa zote za kituo. kujitolea shughuli yetu mpya sasa itaonekana kama hii:

![LNP201](assets/en/25.webp)

Wacha tueleze kwa undani utendaji wa utaratibu huu pamoja.

### Mchakato wa Usasishaji wa Muamala

Wakati Alice na Bob wanasasisha hali ya kituo kwa muamala mpya wa Umeme, wao huweka mapema siri zao kwa kujitolea shughuli husika (ile ambayo itapitwa na wakati na inaweza kuruhusu mmoja wao kudanganya). Hii ina maana kwamba, katika hali mpya ya kituo:


- Alice na Bob wana shughuli ya kujitolea mpya inayowakilisha usambazaji wa sasa wa fedha baada ya shughuli ya Umeme.
- Kila mmoja ana siri ya mwingine kwa shughuli ya awali, ambayo inawaruhusu kutumia ufunguo wa kubatilisha tu ikiwa mmoja wao anajaribu kudanganya kwa kuchapisha shughuli na hali ya zamani katika kumbukumbu za nodi za Bitcoin. Hakika, kuadhibu chama kingine, ni muhimu kushikilia siri zote mbili na kujitolea shughuli ya pili, ambayo inajumuisha pembejeo iliyotiwa sahihi. Bila muamala huu, ufunguo wa kubatilisha pekee hauna maana. Njia pekee ya kupata shughuli hii ni kuipata kutoka kwa kumbukumbu (katika shughuli zinazosubiri uthibitisho) au katika shughuli zilizothibitishwa kwenye Blockchain wakati wa muda, ambayo inathibitisha kwamba upande mwingine unajaribu kudanganya, iwe kwa makusudi au la.

Hebu tuchukue mfano ili kuelewa mchakato huu vizuri:


- **Jimbo la Awali**: Alice ana **satoshi 100,000**, Bob **30,000 satoshi**.

![LNP201](assets/en/26.webp)


- Bob anataka kupokea Satoshi 40,000 kutoka kwa Alice kupitia chaneli yao ya Umeme. Ili kufanya hivi:
   - Anamtumia anwani ya ununuzi pamoja na siri yake kwa ufunguo wa kubatilisha wa shughuli ya kujitolea yake ya awali.
   - Kwa kujibu, Alice anaweka sahihi yake kwa kujitolea shughuli mpya ya Bob, pamoja na siri yake ya ufunguo wa kubatilisha wa shughuli yake ya awali.
   - Hatimaye, Bob anatuma sahihi yake kwa kujitolea shughuli mpya ya Alice.
   - Mabadilishano haya yanamruhusu Alice kutuma satoshi 40,000 kwa Bob on Lightning kupitia chaneli yao, na miamala mipya ya kujitolea sasa inaonyesha usambazaji huu mpya wa fedha.

![LNP201](assets/en/27.webp)


- Ikiwa Alice atajaribu kuchapisha Commitment Transaction ya zamani ambapo bado alikuwa anamiliki satoshi 100,000, Bob, akiwa amepata ufunguo wa kubatilisha, anaweza kurejesha pesa hizo mara moja kwa kutumia ufunguo huu, huku Alice akizuiwa na kipima saa.

![LNP201](assets/en/28.webp)

Hata kama, katika kesi hii, Bob hana nia ya kiuchumi ya kujaribu kudanganya, ikiwa atafanya hivyo hata hivyo, Alice pia ananufaika kutokana na ulinzi wa ulinganifu unaompa dhamana sawa.

**Unapaswa kuchukua nini kutoka kwa sura hii?**

Shughuli za kujitolea kwenye Lightning Network zinajumuisha mbinu za usalama ambazo hupunguza hatari ya kudanganya na motisha ya kufanya hivyo. Kabla ya kusaini kujitolea shughuli mpya, Alice na Bob kubadilishana siri zao kwa miamala ya awali ya kujitolea. Ikiwa Alice atajaribu kuchapisha kujitolea shughuli ya zamani, Bob anaweza kutumia ufunguo wa kubatilisha kurejesha pesa zote kabla Alice hajaweza (kwa sababu amezuiwa na kizuizi cha saa), ambayo humuadhibu kwa kujaribu kudanganya.

Mfumo huu wa usalama huhakikisha kuwa washiriki wanafuata sheria za Lightning Network, na hawawezi kufaidika kutokana na kuchapisha miamala ya zamani ya kujitolea.

Katika hatua hii ya mafunzo, sasa unajua jinsi njia za Umeme hufunguliwa na jinsi miamala ndani ya njia hizi inavyofanya kazi. Katika sura inayofuata, tutagundua njia tofauti za kufunga chaneli na kurejesha bitcoins zako kwenye Blockchain kuu.

## Kufungwa kwa Kituo

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

:::video id=4d8ad4e6-32ff-46d3-bd17-343929aa863b:::

Katika sura hii, tutajadili kufunga **chaneli kwenye Lightning Network**, ambayo hufanywa kupitia muamala wa Bitcoin, kama vile kufungua chaneli. Baada ya kuona jinsi miamala ndani ya kituo inavyofanya kazi, sasa ni wakati wa kuona jinsi ya kufunga chaneli na kurejesha pesa kwenye Bitcoin Blockchain.

### Kikumbusho cha mzunguko wa maisha wa kituo

Mzunguko wa maisha wa kituo huanza na ufunguzi wake, kupitia shughuli ya Bitcoin, kisha miamala ya Umeme hufanywa ndani yake, na hatimaye, wakati wahusika wanataka kurejesha fedha zao, kituo kinafungwa kupitia kwa shughuli ya pili ya Bitcoin. Shughuli za kati zilizofanywa kwenye Umeme zinawakilishwa na shughuli ambazo hazijachapishwa kujitolea.

![LNP201](assets/en/29.webp)

### Aina tatu za kufungwa kwa kituo

Kuna njia tatu kuu za kufunga chaneli hii, ambazo zinaweza kuitwa mzuri, mkatili, na mtoro (iliyoongozwa na Andreas Antonopoulos katika _Mastering the Lightning Network_):


- **The Good**: kufungwa kwa ushirika, ambapo Alice na Bob wanakubali kufunga kituo.
- **Mbaya**: kufungwa kwa lazima, ambapo mmoja wa wahusika anaamua kufunga kituo kwa uaminifu, lakini bila makubaliano ya mwingine.
- **The Ugly**: kufungwa kwa udanganyifu, ambapo mmoja wa wahusika anajaribu kuiba fedha kwa kuchapisha kujitolea shughuli ya zamani (yoyote lakini si ya mwisho, ambayo inaonyesha mgawanyo halisi na wa haki wa fedha).

Hebu tuchukue mfano:


- Alice anamiliki 100,000 satoshi na Bob 30,000 satoshi.
- Usambazaji huu unaakisiwa katika muamala 2 wa kujitolea (moja kwa kila mtumiaji) ambao haujachapishwa, lakini unaweza kuwa katika tukio la kufungwa kwa kituo.

![LNP201](assets/en/30.webp)

### Nzuri: kufungwa kwa ushirika

**Katika kufungwa kwa ushirika**, Alice na Bob wanakubali kufunga kituo. Hivi ndivyo inavyoendelea:


- Alice anatuma ujumbe kwa Bob kupitia itifaki ya mawasiliano ya Umeme kupendekeza kufunga kituo.
- Bob anakubali, na pande hizo mbili hazifanyi miamala zaidi katika kituo.

![LNP201](assets/en/31.webp)


- Alice na Bob wanajadiliana pamoja ada za muamala wa kufunga. Ada hizi kwa ujumla huhesabiwa kulingana na soko la ada la Bitcoin wakati wa kufungwa. Ni muhimu kutambua kwamba daima ni mtu aliyefungua chaneli (Alice katika mfano wetu) ndiye hulipa ada za kufunga.
- Wanaunda muamala mpya wa kufunga. Muamala huu unafanana na kujitolea shughuli, lakini bila kufuli muda au taratibu za ubatilishaji, kwa kuwa pande zote mbili zinashirikiana na hakuna hatari ya kudanganya. Muamala huu wa kufunga ushirika kwa hiyo ni tofauti na shughuli za kujitolea.

Kwa mfano, ikiwa Alice anamiliki satoshi 100,000 na Bob 30,000 satoshi, muamala wa kufunga utatuma Satoshi 100,000 kwa Anwani ya Alice na 30,000 Satoshi kwa Anwani ya Bob ya Anwani, bila vikwazo vya muda. Mara tu shughuli hii inapotiwa saini na pande zote mbili, inachapishwa na Alice. Mara tu muamala utakapothibitishwa kwenye Bitcoin Blockchain, chaneli ya Umeme itafungwa rasmi.

![LNP201](assets/en/32.webp)

kufungwa kwa vyama vya ushirika ndiyo njia inayopendekezwa ya kufunga kwa sababu ni ya haraka (hakuna kufunga saa) na ada za ununuzi hurekebishwa kulingana na hali ya sasa ya soko ya Bitcoin. Hii inaepuka kulipa kidogo sana, ambayo inaweza kuhatarisha kuzuia shughuli katika mempools, au kulipa kupita kiasi bila lazima, ambayo husababisha hasara ya kifedha isiyo ya lazima kwa washiriki.

### Mbaya: kufungwa kwa kulazimishwa

Wakati nodi ya Alice inatuma ujumbe kwa Bob kuomba kufungwa kwa vyama vya ushirika, ikiwa hajibu (kwa mfano, kutokana na kukatika kwa mtandao au tatizo la kiufundi), Alice anaweza kuendelea na kufungwa kwa kulazimishwa kwa kuchapisha kujitolea shughuli iliyosainiwa mwisho .

Katika kesi hii, Alice atachapisha tu kujitolea shughuli ya mwisho, ambayo inaonyesha hali ya kituo wakati shughuli ya mwisho ya Umeme ilifanyika na usambazaji sahihi wa fedha.

![LNP201](assets/en/33.webp)

Muamala huu unajumuisha muda wa muda wa fedha za Alice, hivyo kufanya kufungwa polepole.

![LNP201](assets/en/34.webp)

Pia, ada za kujitolea shughuli zinaweza kuwa zisizofaa wakati wa kufungwa, kwani ziliwekwa wakati shughuli iliundwa, wakati mwingine miezi kadhaa kabla. Kwa ujumla, wateja wa Umeme hukadiria ada kupita kiasi ili kuepuka matatizo ya siku zijazo, lakini hii inaweza kusababisha ada nyingi, au kinyume chake chini sana.

Kwa muhtasari, kufunga kwa lazima ni chaguo la mwisho wakati mwenzi hajibu tena. Ni polepole na chini ya kiuchumi kuliko kufungwa kwa vyama vya ushirika. Kwa hiyo, inapaswa kuepukwa iwezekanavyo.

### Kudanganya: kudanganya

Hatimaye, kufungwa kwa kulaghai hutokea wakati mmoja wa wahusika anajaribu kuchapisha kujitolea shughuli ya zamani, mara nyingi ambapo walikuwa na pesa nyingi kuliko inavyopaswa. Kwa mfano, Alice anaweza kuchapisha muamala wa zamani ambapo alikuwa anamiliki Satoshi 120,000, ilhali anamiliki 100,000 pekee sasa hivi.

![LNP201](assets/en/35.webp)

Bob, ili kuzuia udanganyifu huu, anafuatilia Bitcoin Blockchain na Mempool yake ili kuhakikisha Alice hachapishi shughuli ya zamani. Bob akigundua jaribio la kudanganya, anaweza kutumia kitufe cha kubatilisha  kurejesha pesa za Alice na kumwadhibu kwa kuchukua pesa zote za kituo. Kwa kuwa Alice amezuiwa na kizuizi cha saa kwenye pato lake, Bob ana muda wa kuutumia bila kufunga saa upande wake ili kurejesha pesa zote kwenye Anwani anayomiliki.

![LNP201](assets/en/36.webp)

Ni wazi kwamba kudanganya kunaweza kufaulu ikiwa Bob hatatenda ndani ya muda uliowekwa na kufuli kwa muda kwenye matokeo ya Alice. Katika kesi hii, matokeo ya Alice yamefunguliwa, na kumruhusu kuitumia ili kuunda pato jipya kwa Anwani anayodhibiti.

Unapaswa kuchukua nini kutoka kwa sura hii?

Kuna njia tatu za kufunga chaneli:


- **Kufungwa kwa Ushirika**: Haraka na kwa gharama ya chini, ambapo pande zote mbili zinakubali kufunga kituo na kuchapisha muamala uliowekwa maalum.
- **Kufungwa Kwa Kulazimishwa**: Haifai, kwani inategemea uchapishaji wa kujitolea shughuli, yenye ada zinazoweza kuwa zisizofaa na kizuizi cha muda, ambacho hupunguza kasi ya kufungwa.
- **Kudanganya**: Iwapo mmoja wa wahusika atajaribu kuiba fedha kwa kuchapisha muamala wa zamani, mwingine anaweza kutumia ufunguo wa kubatilisha kuadhibu udanganyifu huu.

Katika sura zijazo, tutachunguza Lightning Network kutoka kwa mtazamo mpana, tukizingatia jinsi mtandao wake unavyofanya kazi.

# Mtandao wa Liquidity

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Lightning Network

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

:::video id=38419c23-5592-4573-b0a7-84824a5bfb77:::

Katika sura hii, tutachunguza jinsi malipo kwenye Lightning Network yanaweza kumfikia mpokeaji hata kama hajaunganishwa moja kwa moja na njia ya malipo. Umeme, kwa kweli, ni mtandao wa njia za malipo, ambao unaruhusu pesa kutumwa kwa nodi ya mbali kupitia chaneli za washiriki wengine. Tutagundua jinsi malipo yanavyopitishwa kwenye mtandao, jinsi ukwasi hupita kati ya vituo na jinsi ada za muamala zinavyokokotolewa.

### Mtandao wa Njia za Malipo

Kwenye Lightning Network, shughuli inafanana na uhamisho wa fedha kati ya nodi mbili. Kama inavyoonekana katika sura zilizopita, ni muhimu kufungua chaneli na mtu ili kufanya miamala ya Umeme. Kituo hiki kinaruhusu karibu idadi isiyo na kikomo ya miamala ya off-chain kabla ya kuifunga ili kurejesha salio la On-Chain. Hata hivyo, njia hii ina hasara ya kuhitaji njia ya moja kwa moja na mtu mwingine kupokea au kutuma fedha, ambayo ina maana ya shughuli ya ufunguzi na shughuli ya kufunga kwa kila channel. Nikipanga kufanya malipo mengi na mtu huyu, kufungua na kufunga kituo kunakuwa kwa gharama nafuu. Kinyume chake, ikiwa ninahitaji tu kufanya shughuli chache za Umeme, kufungua kituo cha moja kwa moja sio faida, kwani ingenigharimu miamala 2 ya On-Chain kwa idadi ndogo ya shughuli za off-chain. Kesi hii inaweza kutokea, kwa mfano, unapotaka kulipa kwa Umeme kwa mfanyabiashara bila kupanga kurudi.

Ili kutatua tatizo hili, Lightning Network inaruhusu kuelekeza malipo kupitia njia kadhaa na nodi za kati, na hivyo kuwezesha shughuli bila njia ya moja kwa moja na mtu mwingine.

Kwa mfano, fikiria kwamba:


- **Alice** (mwenye rangi ya chungwa) ana chaneli iliyo na Suzie (ya kijivu) yenye satoshi 100,000 upande wake na satoshi 30,000 kwa upande wa Suzie.
- **Suzie** ana chaneli na Bob ambamo anamiliki 250,000 Satoshi na ambapo Bob hana Satoshi.

![LNP201](assets/en/37.webp)

Ikiwa Alice anataka kutuma pesa kwa Bob bila kufungua chaneli moja kwa moja naye, italazimika kupitia Suzie, na kila chaneli itahitaji kurekebisha ukwasi kila upande. Satoshi zilizotumwa hubakia ndani ya chaneli zao husika; "havivuki" chaneli, lakini uhamishaji unafanywa kupitia marekebisho ya ukwasi wa ndani katika kila chaneli.

Tuseme Alice anataka kutuma satoshi 50,000 kwa Bob:


- **Alice** hutuma satoshi 50,000 kwa Suzie katika kituo chao cha pamoja.
- **Suzie** anaiga uhamisho huu kwa kutuma satoshi 50,000 kwa Bob katika idhaa yao.

![LNP201](assets/en/38.webp)

Kwa hivyo, malipo yanaelekezwa kwa Bob kupitia harakati ya ukwasi katika kila chaneli. Mwisho wa operesheni, Alice anaishia na 50,000 Sats. Hakika amehamisha 50,000 Sats tangu awali, alikuwa na 100,000. Bob, kwa upande wake, anaishia na 50,000 Sats ya ziada. Kwa Suzie (nodi ya kati), operesheni hii haina upande wowote: mwanzoni, alikuwa na 30,000 Sats kwenye chaneli yake na Alice na 250,000 Sats kwenye chaneli yake na Bob, jumla ya 280,000 Sats. Baada ya upasuaji, anashikilia 80,000 Sats katika chaneli yake na Alice na 200,000 Sats katika chaneli yake na Bob, ambayo ni jumla sawa na mwanzoni.

Uhamisho huu kwa hivyo unazuiliwa na kiasi kinachopatikana katika mwelekeo wa uhamishaji.

### kuhesabu kwa Njia ya Vikomo vya Ukwasi

Wacha tuchukue mfano wa kinadharia wa mtandao mwingine na:


- **Satoshi 130,000** kwa upande wa Alice (mwenye rangi ya chungwa) kwenye chaneli yake akiwa na **Suzie** (mwenye kijivu).
- **Satoshi 90,000** kwa upande wa wa Suzie na satoshi 200,000 kwa upande wa **Carol** (mwenye waridi).
- **150,000 satoshi** kwa upande wa Carol na satoshi 100,000 kwa upande wa **Bob**.

![LNP201](assets/en/39.webp)

Kiwango cha juu zaidi cha Alice anaweza kutuma kwa Bob katika usanidi huu ni **Satoshi 90,000**, kwa kuwa anazuiliwa na kiasi kidogo cha fedha kinachopatikana katika chaneli kutoka kwa Suzie hadi Carol. Katika mwelekeo tofauti (kutoka kwa Bob hadi Alice), hakuna malipo yanayowezekana kwa sababu upande wa wa Suzie katika kituo ulio na Alice hauna satoshi. Kwa hivyo, hakuna njia inayoweza kutumika kwa uhamishaji katika mwelekeo huu.

Alice hutuma **Satoshi 40,000** kwa Bob kupitia chaneli:


- Alice anahamisha Satoshi 40,000 kwenye chaneli yake na Suzie.
- Suzie anahamisha satoshi 40,000 kwa Carol katika chaneli yao ya pamoja.
- Carol hatimaye kuhamisha satoshi 40,000 kwa Bob.

![LNP201](assets/en/40.webp)

Satoshi zilizotumwa katika kila chaneli zinabaki kwenye chaneli, kwa hivyo satoshi zilizotumwa na Carol kwa Bob si sawa na zile zilizotumwa na Alice kwa Suzie. Uhamisho unafanywa tu kwa kurekebisha ukwasi ndani ya kila chaneli. Aidha, uwezo wa jumla wa chaneli bado haujabadilika.

![LNP201](assets/en/41.webp)

Kama katika mfano uliopita, baada ya shughuli, nodi ya chanzo (Alice) ina Satoshi 40,000 chini. Nodi za kati (Suzie na Carol) huhifadhi jumla ya kiasi sawa, na kufanya operesheni kuwa isiyo na usawa kwao. Hatimaye, nodi fikio (Bob) inapokea Satoshi 40,000 za ziada.

Kwa hiyo jukumu la nodes za kati ni muhimu sana katika utendaji wa Lightning Network. Huwezesha uhamishaji kwa kutoa njia nyingi za malipo. Ili kuhimiza nodi hizi kutoa ukwasi wao na kushiriki katika malipo ya uelekezaji, **ada za uelekezaji** hulipwa kwao.

### Ada za Njia

Nodi za kati hutoza ada ili kuruhusu malipo kupitia chaneli zao. Ada hizi zimewekwa na kila nodi kwa kila kituo. Ada hizo zinajumuisha vipengele viwili:


- "**Ada ya msingi**": kiasi kisichobadilika kwa kila kituo, mara nyingi 1 ilikaa kama chaguo-msingi, lakini inayoweza kubinafsishwa.
- "**Ada ya kubadilika**": asilimia ya kiasi kilichohamishwa, kinachokokotolewa katika sehemu kwa milioni (ppm). Kwa chaguo-msingi, ni 1 ppm (1 ilikaa kwa satoshi milioni iliyohamishwa), lakini pia inaweza kurekebishwa.

Ada pia hutofautiana kulingana na mwelekeo wa uhamishaji. Kwa mfano, kwa uhamisho kutoka kwa Alice hadi kwa Suzie, ada za Alice zitatumika. Kinyume chake, kutoka kwa Suzie hadi Alice, ada za Suzie hutumiwa.

Kwa mfano, kwa kituo kati ya Alice na Suzie, tunaweza kuwa na:


- **Alice**: ada ya msingi ya 1 sat na 1 ppm kwa ada zinazobadilika.
- **Suzie**: ada ya msingi ya 0.5 sat na 10 ppm kwa ada zinazobadilika.

![LNP201](assets/en/42.webp)

Ili kuelewa vyema jinsi ada zinavyofanya kazi, hebu tusome Lightning Network sawa na hapo awali, lakini sasa kwa ada zifuatazo za uelekezaji:


- Kituo cha **Alice - Suzie**: ada ya msingi ya 1 Satoshi na 1 ppm kwa Alice.
- Kituo **Suzie - Carol**: ada ya msingi ya 0 Satoshi na 200 ppm kwa Suzie.
- **Carol - Bob** Channeli: ada ya msingi ya 1 Satoshi na 1 ppm kwa Suzie 2.

![LNP201](assets/en/43.webp)

Kwa malipo yale yale ya Satoshi 40,000 kwa Bob, Alice atalazimika kutuma zaidi kidogo, kwani kila nodi ya mpatanishi itakata ada zake:


- Carol anaondoa satoshi 1.04 kwenye kituo na Bob:

$$ f*{\text{Carol-Bob}} = \maandishi{ada ya msingi} + \left(\frac{\text{ppm} \mara \maandishi{kiasi}}{10^6}\kulia) $$

$$ f*{\text{Carol-Bob}} = 1 + \frac{1 \mara 40000}{10^6} = 1 + 0.04 = 1.04 \maandishi{ Sats} $$

- Suzie anakata satoshi 8 katika ada kwenye kituo na Carol:

$$ f*{\text{Suzie-Carol}} = \maandishi{ada ya msingi} + \left(\frac{\text{ppm} \mara \maandishi{kiasi}}{10^6}\kulia) $$

$$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \mara 40001.04}{10^6} = 0 + 8.0002 \takriban 8 \maandishi{ Sats} $$

Jumla ya ada za malipo haya kwenye njia hii ni 9.04 satoshi. Hivyo, ni lazima Alice atume 40,009.04 satoshi ili Bob apokee satoshi 40,000 haswa.

![LNP201](assets/en/44.webp)

Kwa hivyo ukwasi unasasishwa:

![LNP201](assets/en/45.webp)

### Njia ya vitunguu

Ili kuelekeza malipo kutoka kwa mtumaji hadi kwa mpokeaji, Lightning Network hutumia njia inayoitwa "njia ya vitunguu". Tofauti na uelekezaji wa data ya kitamaduni, ambapo kila kipanga njia huamua mwelekeo wa data kulingana na marudio yao, uelekezaji wa vitunguu hufanya kazi tofauti:


- **Njia ya kutuma hukokotoa njia nzima**: Alice, kwa mfano, anaamua kwamba malipo yake lazima yapitie kwa Suzie na Carol kabla ya kufika kwa Bob.
- **Kila nodi ya mpatanishi inafahamu jirani wake wa karibu tu**: Suzie anajua tu kwamba alipokea pesa kutoka kwa Alice na kwamba lazima azihamishe kwa Carol. Walakini, Suzie hajui ikiwa Alice ndiye nodi ya chanzo au nodi ya mpatanishi, na pia hajui kama Carol ndiye nodi ya mpokeaji au nodi nyingine ya mpatanishi. Kanuni hii inatumika pia kwa Carol na nodi zingine zote kwenye njia. Uelekezaji wa kitunguu hivyo huhifadhi usiri wa miamala kwa kuficha utambulisho wa mtumaji na mpokeaji wa mwisho.

Ili kuhakikisha nodi ya utumaji inaweza kukokotoa njia kamili kwa mpokeaji katika uelekezaji wa kitunguu, ni lazima kudumisha grafu ya mtandao ili kujua topolojia yake na kubainisha njia zinazowezekana.

Unapaswa kuchukua nini kutoka kwa sura hii?


- Kwenye Umeme, malipo yanaweza kupitishwa kati ya nodi zilizounganishwa kwa njia isiyo ya moja kwa moja kupitia chaneli za mpatanishi. Kila moja ya nodi hizi za kati huwezesha relay ya ukwasi.
- Node za kati hupokea tume kwa huduma yao, inayojumuisha ada za kudumu na za kutofautiana.
- Uelekezaji wa kitunguu huruhusu kinundu cha kupitisha kukokotoa njia kamili bila nodi za kati kujua chanzo au lengwa la mwisho.

Katika sura hii, tulichunguza njia za malipo kwenye Lightning Network. Lakini swali linatokea: ni nini kinachozuia nodi za mpatanishi kukubali malipo yanayoingia bila kusambaza kwa marudio ya pili, kwa lengo la kukatiza shughuli? Hili ndilo jukumu la HTLCs ambalo tutajifunza katika sura ifuatayo.

## HTLC - Hashed Time Imefungwa Contract

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

:::video id=6f204b92-55a5-4939-9440-7c5b96a297bf:::

Katika sura hii, tutagundua jinsi Umeme huruhusu malipo kupita kupitia nodi za kati bila kuhitaji kuziamini, shukrani kwa **HTLC** (_Kandarasi Zilizofungwa kwa Muda wa Hashed_). Mikataba hii mahiri huhakikisha kwamba kila nodi ya mpatanishi itapokea tu fedha kutoka kwa kituo chake ikiwa itatuma malipo kwa mpokeaji wa mwisho, vinginevyo, malipo hayatathibitishwa.

Suala linalojitokeza kwa uelekezaji wa malipo kwa hivyo ni uaminifu unaohitajika katika nodi za kati, na kati ya nodi za mpatanishi zenyewe. Ili kufafanua hili, hebu tuangalie tena mfano wetu uliorahisishwa wa Lightning Network na nodi 3 na chaneli 2:


- Alice ana chaneli na Suzie.
- Suzie ana chaneli na Bob.

Alice anataka kutuma 40,000 Sats kwa Bob lakini hana chaneli moja kwa moja naye na hataki kufungua moja. Anatafuta njia na anaamua kupitia nodi ya Suzie.

![LNP201](assets/en/46.webp)

Ikiwa Alice atatuma satoshi 40,000 kwa Suzie kwa ujinga akitumaini kwamba Suzie atahamisha kiasi hiki kwa Bob, Suzie anaweza kujiwekea pesa hizo na asitume chochote kwa Bob.

![LNP201](assets/en/47.webp)

Ili kuepuka hali hii, kwenye Umeme, tunatumia HTLCs (Hashed Time-Locked Contracts), ambayo hufanya malipo kwa nodi ya kati iwe na masharti, kumaanisha kwamba Suzie lazima atimize masharti fulani ili kufikia pesa za Alice na kuzihamishia kwa Bob.

### Jinsi HTLCs Hufanya Kazi

HTLC ni mkataba maalum kulingana na kanuni mbili:


- **Hali ya ufikiaji**: Ni lazima mpokeaji afichue siri ili kufungua malipo anayodaiwa.
- **Muda wake wa kuisha**: Ikiwa malipo hayajakamilika kikamilifu ndani ya muda uliobainishwa, yanaghairiwa, na pesa zitarudi kwa mtumaji.

Hivi ndivyo mchakato huu unavyofanya kazi katika mfano wetu na Alice, Suzie, na Bob:

![LNP201](assets/en/48.webp)

Kuunda siri: Bob hutoa siri nasibu iliyobainishwa kama siri (picha), na kukokotoa _h_ yake iliyobainishwa kama _r_ pamoja na chaguo za kukokotoa za Heshi kama _h_. Tunayo:

$$
r = h(s)
$$

Kutumia kitendakazi cha kuficha hufanya isiwezekane kupata _s_ kwa kuficha pekee, lakini ikiwa siri imetolewa, ni rahisi kuthibitisha kuwa inalingana na kufichwa 

![LNP201](assets/en/49.webp)

**Kutuma ombi la malipo**: Bob anatuma anwani ya ununuzi kwa Alice akiomba malipo. anwani hii ya ununuzi inajumuisha haswa kuficha siri.

![LNP201](assets/en/50.webp)

**Kutuma malipo ya masharti**: Alice anatuma HTLC kati ya Satoshi 40,000 kwa Suzie. Masharti ya Suzie kupokea fedha hizi ni kwamba ampe Alice siri inayokidhi mlinganyo ufuatao:

$$
h(s') = r
$$

![LNP201](assets/en/51.webp)

Kuhamisha HTLC kwa mpokeaji wa mwisho: Suzie, ili kupata Satoshi 40,000 kutoka kwa Alice, lazima ahamishe HTLC sawa na satoshi 40,000 kwa Bob, ambaye ana hali sawa, ambayo ni lazima ampe Suzie siri  ambayo inakidhi:

$$
h(s') = r
$$

![LNP201](assets/en/52.webp)

Uthibitishaji kwa siri: Bob hutoa siri kwa Suzie kupokea satoshi 40,000 zilizoahidiwa katika HTLC. Kwa siri hii, Suzie anaweza kufungua HTLC ya Alice na kupata satoshi 40,000 kutoka kwa Alice. Kisha malipo yanaelekezwa kwa Bob kwa usahihi.

![LNP201](assets/en/53.webp)

Utaratibu huu unamzuia Suzie kutunza pesa za Alice bila kukamilisha uhamisho kwa Bob, kwa kuwa ni lazima atume malipo kwa Bob ili kupata siri na hivyo kufungua HTLC ya Alice. Operesheni inasalia kuwa sawa hata ikiwa njia inajumuisha nodi kadhaa za kati: ni suala la kurudia hatua za Suzie kwa kila nodi ya mpatanishi. Kila nodi inalindwa na masharti ya HTLC, kwa sababu kufungua HTLC ya mwisho na mpokeaji huanzisha kiotomatiki kufunguliwa kwa HTLC zingine zote kwenye mteremko.

### Kuisha na usimamizi wa HTLC iwapo kutatokea matatizo

Ikiwa wakati wa mchakato wa malipo, moja ya nodi za kati, au nodi ya mpokeaji, itaacha kujibu, hasa ikiwa mtandao au umeme umekatika, basi malipo hayawezi kukamilika, kwa sababu siri inayohitajika ili kufungua HTLC haisambazwi. Tukichukua mfano wetu na Alice, Suzie, na Bob, tatizo hili hutokea, kwa mfano, ikiwa Bob hatasambaza siri kwa Suzie. Katika hali hii, HTLC zote za upande wa juu wa njia zimezuiwa, na pesa hulindwa pia.

![LNP201](assets/en/54.webp)

Ili kuepuka hili, HTLC kwenye Umeme huwa na muda wa kuisha unaoruhusu kuondolewa kwa HTLC ikiwa haitakamilika baada ya muda fulani. Muda wa mwisho wa matumizi hufuata mpangilio maalum kwani huanza kwanza na HTLC iliyo karibu zaidi na mpokeaji, na kisha kusonga mbele hadi kwa mtoaji wa muamala. Katika mfano wetu, kama Bob hatawahi kutoa siri kwa Suzie, hii ingesababisha kwanza HTLC ya Suzie kuelekea Bob kuisha muda.

![LNP201](assets/en/55.webp)

Kisha HTLC kutoka Alice hadi Suzie.

![LNP201](assets/en/56.webp)

Ikiwa agizo la kumalizika muda wake lingebatilishwa, Alice angeweza kurejesha malipo yake kabla ya Suzie kujilinda dhidi ya uwezekano wa kudanganywa. Hakika, ikiwa Bob atarudi kudai HTLC yake wakati Alice tayari ameondoa yake, Suzie atakuwa katika hali mbaya. Agizo hili la kushuka la kumalizika kwa muda wa HTLC kwa hivyo huhakikisha kwamba hakuna nodi ya kati inayopata hasara isiyo ya haki.

### Uwakilishi wa HTLC katika miamala ya kujitolea

Miamala ya kujitolea inawakilisha HTLC kwa njia ambayo masharti wanayoweka kwenye Umeme yanaweza kuhamishwa hadi Bitcoin iwapo kituo kitafungwa kwa lazima wakati wa muda wa kuishi wa HTLC. Kama ukumbusho, miamala ya kujitolea inawakilisha hali ya sasa ya chaneli kati ya watumiaji hao wawili na kuruhusu kufungwa kwa lazima kwa upande mmoja endapo kutatokea matatizo. Kwa kila hali mpya ya kituo, shughuli 2 za kujitolea zinaundwa: moja kwa kila chama. Hebu tuangalie upya mfano wetu na Alice, Suzie na Bob, lakini tuangalie kwa karibu zaidi kile kinachotokea katika kiwango cha kituo kati ya Alice na Suzie wakati HTLC inapoundwa.

![LNP201](assets/en/57.webp)

Kabla ya kuanza kwa malipo ya 40,000 Sats kati ya Alice na Bob, Alice ana 100,000 Sats katika chaneli yake na Suzie, huku Suzie akishikilia 30,000. Shughuli zao za kujitolea ni kama ifuatavyo:

![LNP201](assets/en/58.webp)

Alice amepokea tu anwani ya ununuzi ya Bob, ambayo ina, kuficha kwa siri. Kwa hivyo anaweza kutengeneza HTLC kati ya Satoshi 40,000 na Suzie. HTLC hii inawakilishwa katika miamala ya hivi punde ya kujitolea kama bidhaa inayoitwa "**_HTLC Out_**" kwa upande wa Alice, kwa kuwa pesa zinatoka, na "**_HTLC In_**" kwa upande wa Suzie, kwa kuwa pesa zinaingia.

![LNP201](assets/en/59.webp)

Matokeo haya yanayohusiana na HTLC yanashiriki hali sawa, ambayo ni:


- Ikiwa Suzie anaweza kutoa siri, anaweza kufungua pato hili mara moja na kuhamishia kwenye Anwani anayoidhibiti.
- Ikiwa Suzie hana siri, hawezi kufungua pato hili, na Alice ataweza kuifungua baada ya kufunga muda ili kuituma kwa Address anayoidhibiti. Hivyo basi, kufunga saa humpa Suzie muda wa kujibu iwapo atapata Siri.

Masharti haya yanatumika tu ikiwa kituo kimefungwa (yaani, kujitolea shughuli kumechapishwa On-Chain) wakati HTLC bado inafanya kazi kwenye Umeme, kumaanisha malipo kati ya Alice na Bob bado hayajakamilishwa, na HTLCs bado hazijaisha muda wake. Shukrani kwa masharti haya, Suzie anaweza kurejesha satoshi 40,000 za HTLC anazodaiwa kwa kutoa _s_. Vinginevyo, Alice anarejesha pesa hizo baada ya kuisha kwa muda, kwa sababu ikiwa Suzie hajui _s_, inamaanisha kuwa hajahamisha satoshi 40,000 kwa Bob, na kwa hivyo, pesa za Alice hazidaiwi kwake.

Zaidi ya hayo, ikiwa kituo kimefungwa huku HTLC kadhaa zikisubiri, kutakuwa na matokeo mengi zaidi kama vile kuna HTLC zinazoendelea.

Ikiwa kituo hakijafungwa, basi baada ya kuisha au kufaulu kwa malipo ya Umeme, miamala mpya ya kujitolea inaundwa ili kuonyesha hali mpya, ambayo sasa ni thabiti, ya kituo, ambayo ni, bila HTLC zozote zinazosubiri. Matokeo yanayohusiana na HTLC kwa hivyo yanaweza kuondolewa kutoka kwa miamala ya kujitolea.

![LNP201](assets/en/60.webp)

Hatimaye, katika kesi ya kufungwa kwa kituo cha ushirika wakati HTLC inatumika, Alice na Suzie huacha kukubali malipo mapya na kusubiri uamuzi au mwisho wa muda wa HTLC unaoendelea. Hii inawaruhusu kuchapisha muamala mwepesi zaidi wa kufunga, bila matokeo yanayohusiana na HTLC, na hivyo kupunguza ada na kuepuka kusubiri kwa muda unaowezekana.

Unapaswa kuchukua nini kutoka kwa sura hii?

HTLC huwezesha uelekezaji wa malipo ya Radi kupitia nodi nyingi bila kuziamini. Hapa kuna mambo muhimu ya kukumbuka:


- HTLCs huhakikisha usalama wa malipo kupitia siri (preimage) na muda wa mwisho wa matumizi.
- Azimio au mwisho wa muda wa HTLCs hufuata mpangilio maalum: kisha kutoka mahali unakoenda kuelekea chanzo, ili kulinda kila nodi.
- Alimradi HTLC haijatatuliwa wala kuisha muda wake, inadumishwa kama matokeo katika miamala ya hivi majuzi zaidi ya Commitment.

Katika sura inayofuata, tutagundua jinsi nodi inayotoa muamala wa Umeme inavyopata na kuchagua njia za malipo yake kufikia nodi ya mpokeaji.

## Kutafuta Njia Yako

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

:::video id=e5baa834-111d-46f5-a28b-3538bed2bbb0:::

Katika sura zilizopita, tuliona jinsi ya kutumia njia za nodi nyingine kuelekeza malipo na kufikia nodi bila kuunganishwa nayo moja kwa moja kupitia chaneli. Pia tulijadili jinsi ya kuhakikisha usalama wa uhamishaji bila kuamini nodi za mpatanishi. Katika sura hii, tutazingatia kutafuta njia bora zaidi ya kufikia nodi inayolengwa.

### Tatizo la Kuelekeza kwenye Umeme

Kama tulivyoona, katika Umeme, ni njia ya kutuma malipo ambayo lazima ihesabu njia kamili kwa mpokeaji, kwa sababu tunatumia mfumo wa uelekezaji wa kitunguu. Nodi za kati hazijui mahali pa asili au mahali pa mwisho. Wanajua tu malipo yanatoka wapi na ni lazima wayahamishe kwa nodi gani inayofuata. Hii ina maana kwamba nodi ya utumaji lazima idumishe topolojia ya ndani ya mtandao inayobadilika, na nodi zilizopo za Umeme na chaneli kati ya kila moja, kwa kuzingatia fursa, kufungwa, na masasisho ya serikali.

![LNP201](assets/en/61.webp)

Hata na topolojia hii ya Lightning Network, kuna taarifa muhimu ya kuelekeza ambayo bado haifikiki kwa nodi ya utumaji, ambayo ni mgawanyo kamili wa ukwasi katika chaneli wakati wowote. Hakika, kila kituo kinaonyesha tu jumla ya uwezo wake, lakini mgawanyo wa ndani wa fedha unajulikana tu kwa nodi mbili zinazoshiriki. Hili, huleta changamoto kwa uelekezaji mzuri, kwa kuwa ufanisi wa malipo unategemea sana ikiwa kiasi chake ni kidogo kuliko ukwasi wa chini zaidi kwenye njia iliyochaguliwa. Walakini, ukwasi wote hauonekani kwa nodi ya kutuma.

![LNP201](assets/en/62.webp)

### Sasisho la Ramani ya Mtandao

Ili kusasisha ramani ya mtandao wao, nodi mara kwa mara ujumbe wa ubadilishanaji kupitia algoriti inayoitwa "_kusengenya_". Hii ni algoriti iliyosambazwa inayotumiwa kueneza habari kwa njia ya janga kwa nodi zote kwenye mtandao, ambayo inaruhusu ubadilishanaji na usawazishaji wa Global State ya chaneli katika mizunguko michache ya mawasiliano. Kila nodi hueneza habari kwa jirani mmoja au zaidi waliochaguliwa kwa nasibu au la, hawa, kwa upande wake, hueneza habari hiyo kwa majirani wengine na kadhalika hadi hali ya usawazishaji wa kimataifa ipatikane.

Ujumbe 2 kuu unaobadilishana kati ya nodi za Umeme ni kama ifuatavyo:


- "**Matangazo ya Kituo**": ujumbe unaoashiria kufunguliwa kwa kituo kipya.
- "**Sasisho za Kituo**": sasisha ujumbe kuhusu hali ya kituo, hasa kuhusu mabadiliko ya ada (lakini si kuhusu usambazaji wa ukwasi).

Nodi za umeme pia hufuatilia Bitcoin Blockchain ili kugundua shughuli za kufunga chaneli. Kisha kituo kilichofungwa huondolewa kwenye ramani kwa sababu hakiwezi kutumika tena kuelekeza malipo yetu.

### Kuelekeza Malipo

Hebu tuchukue mfano wa Lightning Network ndogo yenye nodi 7: Alice, Bob, 1, 2, 3, 4, na 5. Hebu wazia kwamba Alice anataka kutuma malipo kwa Bob lakini lazima apitie nodi za kati.

![LNP201](assets/en/63.webp)

Huu hapa ni mgawanyo halisi wa fedha katika njia hizi:


- **Mkondo kati ya Alice na 1**: 250,000 Sats kwa upande wa Alice, 80,000 kwa upande wa 1 (jumla ya uwezo wa 330,000 Sats).
- **Kituo kati ya 1 na 2**: 300,000 Sats kwa upande wa 1, 200,000 kwa upande wa 2 (jumla ya uwezo wa 500,000 Sats).
- **Kituo kati ya 2 na 3**: 50,000 Sats kwa upande wa 2, 60,000 upande wa 3 (jumla ya uwezo wa 110,000 Sats).
- **Mkondo kati ya 2 na 5**: 90,000 Sats upande wa 2, 160,000 upande wa 5 (jumla ya uwezo wa 250,000 Sats).
- **Mkondo kati ya 2 na 4**: 180,000 Sats upande wa 2, 110,000 upande wa 4 (jumla ya uwezo wa 290,000 Sats).
- **Channel kati ya 4 na 5**: 200,000 Sats upande wa 4, 10,000 upande wa 5 (jumla ya uwezo wa 210,000 Sats).
- **Mkondo kati wa 3 na Bob**: 50,000 Sats upande wa 3, 250,000 upande wa Bob (jumla ya uwezo wa 300,000 Sats).
- **Mkondo kati ya 5 na Bob**: 260,000 Sats upande wa 5, 100,000 upande wa Bob (jumla ya uwezo wa 360,000 Sats).

![LNP201](assets/en/64.webp)

Ili kufanya malipo ya 100,000 Sats kutoka Alice hadi Bob, chaguo za uelekezaji huzuiliwa na ukwasi unaopatikana katika kila kituo. Njia bora zaidi ya Alice, kulingana na mgawanyo wa ukwasi unaojulikana, inaweza kuwa mlolongo `Alice → 1 → 2 → 4 → 5 → Bob`:

![LNP201](assets/en/65.webp)

Lakini kwa kuwa Alice hajui mgawanyo kamili wa fedha katika kila chaneli, lazima akadirie njia bora zaidi, akizingatia vigezo vifuatavyo:


- Uwezekano wa kufaulu: chaneli yenye uwezo wa juu zaidi ina uwezekano mkubwa wa kuwa na ukwasi wa kutosha. Kwa mfano, chaneli kati ya nodi 2 na nodi 3 ina uwezo wa jumla wa 110,000 Sats, kwa hivyo hakuna uwezekano wa kupata 100,000 Sats au zaidi kwa upande wa node 2, ingawa bado inawezekana.
- Ada za muamala: katika kuchagua njia bora zaidi, nodi ya kutuma pia inazingatia ada zinazotumika na kila nodi ya kati na inalenga kupunguza jumla ya gharama ya uelekezaji.
- Muda wa matumizi wa HTLC: ili kuepuka malipo yaliyozuiwa, muda wa mwisho wa matumizi wa HTLCs pia ni kigezo cha kuzingatia.
- Idadi ya nodi za kati: hatimaye, kwa upana zaidi, nodi ya kutuma itatafuta kutafuta njia yenye nodi chache zinazowezekana ili kupunguza hatari ya kushindwa na kupunguza ada za miamala ya Umeme.

Kwa kuchanganua vigezo hivi, nodi ya kutuma inaweza kujaribu njia zinazowezekana zaidi na kujaribu kuziboresha. Katika mfano wetu, Alice anaweza kuorodhesha njia bora kama ifuatavyo:


- `Alice → 1 → 2 → 5 → Bob`, kwa sababu ndiyo njia fupi zaidi yenye uwezo wa juu zaidi.
- `Alice → 1 → 2 → 4 → 5 → Bob`, kwa sababu njia hii inatoa uwezo mzuri, ingawa ni ndefu kuliko ya kwanza.
- `Alice → 1 → 2 → 3 → Bob`, kwa sababu njia hii inajumuisha chaneli `2 → 3`, ambayo ina uwezo mdogo sana, lakini inasalia na uwezekano wa kutumika.

### Utekelezaji wa Malipo

Alice anaamua kujaribu njia yake ya kwanza (`Alice → 1 → 2 → 5 → Bob`). Kwa hiyo anatuma HTLC ya 100,000 Sats kwa nodi 1. Node hii inakagua kuwa ina ukwasi wa kutosha na nodi 2, na inaendelea maambukizi. Node 2 basi inapokea HTLC kutoka nodi 1, lakini inatambua kuwa haina ukwasi wa kutosha katika chaneli yake na nodi 5 ili kuelekeza malipo ya 100,000 Sats. Kisha hutuma ujumbe wa makosa nyuma kwa nodi 1, ambaye huipeleka kwa Alice. Njia hii imeshindwa.

![LNP201](assets/en/66.webp)

Kisha Alice anajaribu kuelekeza malipo yake kwa kutumia njia yake ya pili (`Alice → 1 → 2 → 4 → 5 → Bob`). Anatuma HTLC ya 100,000 Sats kwa nodi 1, ambaye huipeleka kwa nodi 2, kisha kwa nodi 4, kwa nodi 5, na hatimaye kwa Bob. Wakati huu, ukwasi ni wa kutosha, na njia inafanya kazi. Kila nodi hufungua HTLC yake kwa mteremko kwa kutumia taswira ya awali iliyotolewa na Bob (the secret _s_), ambayo inaruhusu malipo ya Alice kwa Bob kukamilishwa kwa mafanikio.

![LNP201](assets/en/67.webp)

Utafutaji wa njia unafanywa kama ifuatavyo: nodi ya kutuma huanza kwa kutambua njia bora zaidi, kisha hujaribu malipo mfululizo hadi njia ya kazi ipatikane.

Inafaa kukumbuka kuwa Bob anaweza kumpa Alice maelezo katika anwani ya ununuzi ili kuwezesha uelekezaji. Kwa mfano, anaweza kuonyesha chaneli zilizo karibu na ukwasi wa kutosha au kufichua uwepo wa chaneli za kibinafsi. Dalili hizi humruhusu Alice kuepuka njia zilizo na nafasi ndogo ya kufaulu na kujaribu kwanza njia zilizopendekezwa na Bob.

Unapaswa kuchukua nini kutoka kwa sura hii?


- Nodi hudumisha ramani ya topolojia ya mtandao kupitia matangazo na kwa kufuatilia kufungwa kwa vituo kwenye Bitcoin Blockchain.
- Utafutaji wa njia bora zaidi ya malipo unabaki kuwa uwezekano na unategemea vigezo vingi.
- Bob anaweza kutoa dalili katika anwani ya ununuzi ili kuelekeza uelekezaji wa Alice na kumwokoa kutokana na majaribio ya njia zisizotarajiwa.

Katika sura ifuatayo, tutasoma mahususi utendakazi wa ankara, pamoja na zana zingine zinazotumiwa kwenye Lightning Network.

# Vyombo vya Lightning Network

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Invoice, LNURL, na Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

:::video id=309c3412-506e-4189-ad46-5e5088c55008:::

Katika sura hii, tutaangalia kwa karibu utendakazi wa Umeme  ankara, yaani, maombi ya malipo yaliyotumwa na nodi ya mpokeaji kwa nodi ya mtumaji. Lengo ni kuelewa jinsi ya kulipa na kupokea malipo kwenye Umeme. Pia tutajadili njia 2 mbadala za ankara za kawaida: LNURL na Keysend.

![LNP201](assets/en/68.webp)

### Muundo wa Ankara za Umeme

Kama ilivyoelezwa katika sura ya HTLC, kila malipo huanza na kutengeneza anwani ya ununuzi na mpokeaji. Kisha anwani ya ununuzi hii hutumwa kwa mlipaji (kupitia msimbo wa QR au kwa kunakili-kubandika) ili kuanzisha malipo. Anwani ya ununuzi ina sehemu kuu mbili:


- Sehemu Inayosomeka ya Binadamu: sehemu hii ina metadata inayoonekana kwa uwazi ili kuboresha matumizi ya mtumiaji.
- Mzigo: sehemu hii inajumuisha maelezo yaliyokusudiwa kwa mashine ya kuchakata malipo.

Muundo wa kawaida wa anwani ya ununuzi huanza na kitambulisho `LN` cha "Umeme", ikifuatiwa na `bc` kwa Bitcoin, kisha kiasi cha anwani ya ununuzi. Kitenganishi `1` hutofautisha sehemu inayoweza kusomeka na binadamu na sehemu ya data (ya malipo).

Wacha tuchukue anwani ya ununuzi ifuatayo kwa mfano:

```anwani ya ununuzi
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Tayari tunaweza kuigawanya katika sehemu 2. Kwanza, kuna Sehemu Inayosomeka ya Binadamu:

```anwani ya ununuzi
lnbc100u
```

Kisha sehemu iliyokusudiwa kwa mzigo wa malipo:

```anwani ya ununuzi
p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Sehemu hizo mbili zimetenganishwa na `1`. Kitenganishi hiki kilichaguliwa badala ya herufi maalum ili kuruhusu kunakili kwa urahisi kwa anwani ya ununuzi nzima kwa kubofya mara mbili.

Katika sehemu ya kwanza, tunaweza kuona kwamba:


- `LN` inaonyesha kuwa ni shughuli ya Umeme.
- `bc` inaonyesha kuwa Lightning Network iko kwenye Bitcoin Blockchain (na sio kwenye Testnet au Litecoin).
- `100u` inaonyesha kiasi cha anwani ya ununuzi, iliyoonyeshwa kwa **microbitcoins** (`u` ikimaanisha "ndogo"), ambayo hapa ni sawa na 10,000 Sats.

Ili kuteua kiasi cha malipo, kinaonyeshwa katika vitengo vidogo vya Bitcoin. Hapa kuna vitengo vilivyotumika:


- Millibitcoin (iliyoashiria `m`):** Inawakilisha elfu moja ya Bitcoin.

$$
1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
$$


- Microbitcoin (iliyoashiria `u`):** Pia wakati mwingine huitwa "bit", inawakilisha milioni moja ya Bitcoin.

$$
1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
$$


- Nanobitcoin (iliyoashiria `n`):** Inawakilisha bilioni moja ya Bitcoin.

$$
1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
$$


- Picobitcoin (iliyoashiria `p`):** Inawakilisha trilioni moja ya Bitcoin.

$$
1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
$$

### Malipo ya anwani ya ununuzi

Upakiaji wa anwani ya ununuzi ni pamoja na vipande kadhaa vya habari muhimu kwa usindikaji wa malipo:


- **Muhuri wa wakati** : Wakati wa kuundwa kwa anwani ya ununuzi, iliyoonyeshwa katika Unix muhuri wa wakati (idadi ya sekunde ambazo zimepita tangu Januari 1, 1970).
- **Kuficha Siri**: Kama tulivyoona katika sehemu ya HTLCs, nodi ya kupokea lazima itoe nodi ya kutuma na Hash ya taswira. Hii inatumika katika HTLC kulinda muamala. Tuliitaja kama "_r_".
- **Siri ya Malipo**: Siri nyingine inatolewa na mpokeaji, lakini wakati huu inapitishwa kwenye nodi ya kutuma. Hutumika katika uelekezaji wa kitunguu ili kuzuia nodi za kati kukisia ikiwa nodi inayofuata ndiyo mpokeaji wa mwisho au la. Kwa hivyo hii hudumisha aina ya usiri kwa mpokeaji kwa heshima na nodi ya mwisho ya kati kwenye njia.
- **Ufunguo wa Umma wa Mpokeaji**: Huonyesha kwa mlipaji kitambulisho cha mtu anayepaswa kulipwa.
- **Muda wa Kuisha**: Muda wa juu zaidi wa anwani ya ununuzi ya kulipwa (saa 1 kwa chaguomsingi).
- **Vidokezo vya Njia**: Maelezo ya ziada yanayotolewa na mpokeaji ili kumsaidia mtumaji kuboresha njia ya malipo.
- **Sahihi**: Inathibitisha uadilifu wa anwani ya ununuzi kwa kuthibitisha taarifa zote.

Kisha ankara husimbwa katika bech32, umbizo sawa na la anwani za Bitcoin SegWit (umbizo linaloanza na `bc1`).

### Uondoaji wa LNURL

Katika shughuli ya kitamaduni, kama vile ununuzi wa duka, anwani ya ununuzi inatolewa kwa jumla ya kiasi kitakacholipwa. Mara tu anwani ya ununuzi inapowasilishwa (katika mfumo wa msimbo wa QR au mfuatano wa herufi), mteja anaweza kuichanganua na kukamilisha muamala. Kisha malipo hufuata mchakato wa kitamaduni ambao tulijifunza katika sehemu iliyotangulia. Hata hivyo, mchakato huu wakati mwingine unaweza kuwa mgumu sana kwa matumizi ya mtumiaji, kwani huhitaji mpokeaji kutuma taarifa kwa mtumaji kupitia anwani ya ununuzi.

Kwa hali fulani, kama vile kutoa bitcoins kutoka kwa huduma ya mtandaoni, mchakato wa jadi ni mgumu sana. Katika hali kama hizi, suluhisho la uondoaji la **LNURL** hurahisisha mchakato huu kwa kuonyesha msimbo wa QR ambao pochi la mpokeaji huchanganua ili kuunda kiotomatiki anwani ya ununuzi. Huduma hiyo hulipa anwani ya ununuzi, na mtumiaji huona tu uondoaji wa papo hapo.

![LNP201](assets/en/69.webp)

LNURL ni itifaki ya mawasiliano inayobainisha seti ya utendakazi iliyoundwa ili kurahisisha mwingiliano kati ya nodi za Umeme na wateja, pamoja na programu za wahusika wengine. Uondoaji wa LNURL, kama tulivyoona, ni mfano mmoja tu kati ya utendaji mwingine.

Itifaki hii inategemea HTTP na inaruhusu kuundwa kwa viungo kwa ajili ya shughuli mbalimbali, kama vile ombi la malipo, ombi la kujiondoa au utendaji mwingine unaoboresha matumizi ya mtumiaji. Kila LNURL ni URL ya bech32 iliyosimbwa yenye kiambishi awali cha lnurl, ambacho, kikichanganuliwa, huanzisha mfululizo wa vitendo otomatiki kwenye Lightning Wallet.

Kwa mfano, kipengele cha LNURL-kuondoa(LUD-03) kinaruhusu kutoa pesa kutoka kwa huduma kwa kuchanganua msimbo wa QR, bila hitaji la kufanya kuzalisha anwani ya ununuzi. Vile vile, LNURL-auth (LUD-04) huwezesha kuingia katika huduma za mtandaoni kwa kutumia ufunguo wa faragha kwenye Lightning Wallet ya mtu badala ya nenosiri.

### Kutuma Malipo ya Umeme bila anwani ya ununuzi: Keysend

Kesi nyingine ya kufurahisha ni uhamishaji wa pesa bila kupokea anwani ya ununuzi hapo awali, inayojulikana kama "Keysend". Itifaki hii inaruhusu kutuma pesa kwa kuongeza picha ya awali katika data ya malipo iliyosimbwa kwa njia fiche, inayoweza kufikiwa na mpokeaji pekee. Taswira hii inamwezesha mpokeaji kufungua HTLC, hivyo kurejesha fedha bila kuzalisha Invoice hapo awali.

Ili kurahisisha, katika itifaki hii, ni mtumaji ndiye hutoa siri inayotumika katika HTLC, badala ya mpokeaji. Kwa kweli, hii huruhusu mtumaji kufanya malipo bila kulazimika kuingiliana na mpokeaji mapema.

![LNP201](assets/en/70.webp)

**Unapaswa kuchukua nini kutoka kwa sura hii?**


- Umeme anwani ya ununuzi ni ombi la malipo linalojumuisha sehemu inayoweza kusomeka na binadamu na sehemu ya data ya mashine.
- Anwani ya ununuzi imesimbwa katika **bech32**, ikiwa na kitenganishi `1` ili kuwezesha kunakili na sehemu ya data iliyo na maelezo yote muhimu ili kuchakata malipo.
- Michakato mingine ya malipo inapatikana kwenye Umeme, hasa **LNURL-Ondosha** ili kuwezesha uondoaji, na Tuma Ufunguo kwa uhamisho wa moja kwa moja bila anwani ya ununuzi.

Katika sura ifuatayo, tutaona jinsi mwendeshaji wa nodi anavyoweza kudhibiti ukwasi katika vituo vyao, ili wasiwahi kuzuiwa na kuwa na uwezo wa kutuma na kupokea malipo kila mara kwenye Lightning Network.

## Kusimamia ukwasi wako

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

:::video id=96096aef-e4ce-4c44-a022-57e27082232a:::

Katika sura hii, tutachunguza mikakati ya kusimamia vyema ukwasi kwenye Lightning Network. Usimamizi wa ukwasi hutofautiana kulingana na aina ya mtumiaji na muktadha. Tutaangalia kanuni kuu na mbinu zilizopo ili kuelewa vyema jinsi ya kuboresha usimamizi huu.

### Mahitaji ya ukwasi

Kuna wasifu kuu tatu za watumiaji kwenye Umeme, kila moja ikiwa na mahitaji maalum ya ukwasi:


- **Mlipaji**: Huyu ndiye anayelipa. Wanahitaji ukwasi unaotoka ili kuweza kuhamisha fedha kwa watumiaji wengine. Kwa mfano, hii inaweza kuwa mtumiaji.
- **Muuzaji (au Mlipwaji)**: Huyu ndiye anayepokea malipo. Wanahitaji ukwasi unaoingia ili waweze kukubali malipo kwenye nodi zao. Kwa mfano, hii inaweza kuwa biashara au duka la mtandaoni.
- **Kipanga njia**: Njia ya kati, ambayo mara nyingi ni maalum katika malipo ya uelekezaji, ambao ni lazima uboreshe ukwasi wake katika kila kituo ili kuelekeza malipo mengi iwezekanavyo na kupata ada.

Profaili hizi ni wazi hazijasasishwa; mtumiaji anaweza kubadilisha kati ya mlipaji na anayelipwa kulingana na miamala. Kwa mfano, Bob angeweza kupokea mshahara wake kwenye Umeme kutoka kwa mwajiri wake, na kumweka katika nafasi ya "muuzaji" anayehitaji ukwasi unaoingia. Baadaye, kama anataka kutumia mshahara wake kununua chakula, anakuwa "mlipaji" na lazima awe na ukwasi unaotoka.

Ili kuelewa vizuri, hebu tuchukue mfano wa mtandao rahisi unaojumuisha nodi tatu: mnunuzi (Alice), router (Suzie), na muuzaji (Bob).

![LNP201](assets/en/71.webp)

Hebu fikiria kwamba mnunuzi anataka kutuma 30,000 Sats kwa muuzaji na kwamba malipo yanapitia nodi ya kipanga njia. Kila mhusika lazima awe na kiwango cha chini zaidi cha ukwasi katika mwelekeo wa malipo:


- Mlipaji lazima awe na angalau satoshi 30,000 kwenye upande wao wa kituo kilicho na kipanga njia.
- Muuzaji lazima awe na chaneli ambapo satoshi 30,000 ziko upande mwingine ili kuweza kuzipokea.
- Kipanga njia lazima kiwe na satoshi 30,000 kwa upande wa walipaji kwenye chaneli yao, na pia satoshi 30,000 upande wao kwenye chaneli iliyo na muuzaji, ili kuweza kuelekeza malipo.

![LNP201](assets/en/72.webp)

### Mikakati ya Usimamizi wa Ukwasi

Walipaji lazima wahakikishe kudumisha ukwasi wa kutosha kwa upande wao wa chaneli ili kuhakikisha ukwasi unaotoka. Hii inathibitisha kuwa rahisi, kwani inatosha kufungua njia mpya za Umeme ili kuwa na ukwasi huu. Hakika, pesa za awali zilizofungwa kwenye Multisig On-Chain ziko kabisa upande wa walipaji kwenye chaneli ya Umeme mwanzoni. Kwa hivyo uwezo wa malipo unahakikishwa mradi tu njia zimefunguliwa na fedha za kutosha. Wakati ukwasi unaotoka umekwisha, inatosha kufungua njia mpya.

Kwa upande mwingine, kwa muuzaji, kazi ni ngumu zaidi. Ili waweze kupokea malipo, ni lazima wawe na ukwasi upande wa pili wa chaneli zao. Kwa hivyo, kufungua chaneli haitoshi: lazima pia wafanye malipo katika kituo hiki ili kuhamisha ukwasi hadi upande mwingine kabla ya wao kupokea malipo. Kwa wasifu fulani wa watumiaji wa Umeme, kama vile wafanyabiashara, kuna tofauti ya wazi kati ya kile nodi yao hutuma na kile inachopokea, kwani lengo la biashara kimsingi ni kukusanya zaidi ya inavyotumia, ili kupata faida ya kuzalisha. Kwa bahati nzuri, kwa watumiaji hawa walio na mahitaji maalum ya ukwasi unaoingia, suluhu kadhaa zipo:


- **Vituo vya kuvutia**: Mfanyabiashara ananufaika kutokana na faida kutokana na wingi wa malipo yanayoingia yanayotarajiwa kwenye nodi zao. Kwa kuzingatia hili, wanaweza kujaribu kuvutia maeneo ya uelekezaji ambao unatafuta mapato kutokana na ada za miamala na ambao wanaweza kufungua njia kuelekea kwao, wakitumai kuelekeza malipo yao na kukusanya ada zinazohusiana.
- **Harakati ya ukwasi**: Muuzaji pia anaweza kufungua chaneli na kuhamisha baadhi ya fedha kwa upande mwingine kwa kufanya malipo ya uwongo kwenye nodi nyingine, ambayo itarudisha pesa kwa njia nyingine. Tutaona katika sehemu inayofuata jinsi ya kutekeleza operesheni hii.
- **Ufunguzi wa pembetatu**: Majukwaa yapo kwa nodi zinazotaka kufungua chaneli kwa ushirikiano, kuruhusu kila moja kunufaika kutokana na ukwasi unaoingia na unaotoka mara moja. Kwa mfano, [LightningNetwork+](https://lightningnetwork.plus/) inatoa huduma hii. Ikiwa Alice, Bob, na Suzie wanataka kufungua chaneli yenye 100,000 Sats, wanaweza kukubaliana kwenye jukwaa hili ili Alice afungue chaneli kuelekea Bob, Bob kuelekea Suzie, na Suzie kuelekea Alice. Kwa njia hii, kila moja ina 100,000 Sats ya ukwasi unaotoka na 100,000 Sats ya ukwasi unaoingia, huku ikiwa imefungia 100,000 Sats tu.

![LNP201](assets/en/73.webp)


- **Kununua chaneli**: Huduma za kukodisha chaneli za Umeme pia zipo ili kupata ukwasi unaoingia, kama vile [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) au [Lightning Labs Pool](https://lightning.engineering/pool/). Kwa mfano, Alice anaweza kununua chaneli ya Satoshi milioni moja kuelekea nodi yake ili aweze kupokea malipo.

![LNP201](assets/en/74.webp)

Hatimaye, kwa ruta, ambazo lengo lao ni kuongeza idadi ya malipo yaliyochakatwa na ada zilizokusanywa, lazima:


- Fungua chaneli zinazofadhiliwa vyema na nodi za kimkakati.
- Rekebisha mara kwa mara mgawanyo wa fedha katika chaneli kulingana na mahitaji ya mtandao.

### Huduma ya Loop Out

Huduma ya [Loop Out](https://lightning.engineering/loop/), inayotolewa na Maabara ya Umeme, inaruhusu kuhamisha ukwasi hadi upande wa pili wa chaneli huku ikidaiwa kurejesha pesa kwenye Bitcoin Blockchain. Kwa mfano, Alice hutuma satoshi milioni 1 kupitia Umeme kwenye nodi ya kitanzi, ambayo kisha inamrudishia pesa hizo katika bitcoins za On-Chain. Hii husawazisha chaneli yake na Satoshi milioni 1 kila upande, na hivyo kuongeza uwezo wake wa kupokea malipo.

![LNP201](assets/en/75.webp)

Kwa hivyo, huduma hii huwezesha ukwasi unaoingia wakati wa kurejesha bitcoins za On-Chain, ambayo husaidia kupunguza uhamishaji wa pesa zinazohitajika kukubali malipo kwa Umeme.

Unapaswa kuchukua nini kutoka kwa sura hii?


- Ili kutuma malipo kwenye Umeme, ni lazima uwe na ukwasi wa kutosha upande wako katika vituo vyako. Ili kuongeza uwezo huu wa kutuma, fungua tu njia mpya.
- Ili kupokea malipo, unahitaji kuwa na ukwasi upande mwingine katika vituo vyako. Kuongeza uwezo huu wa kupokea ni ngumu zaidi, kwani inahitaji wengine kukufungulia njia, au kufanya malipo (ya uwongo au halisi) ili kuhamisha ukwasi hadi upande mwingine.
- Kudumisha ukwasi inapohitajika kunaweza kuwa changamoto zaidi kulingana na matumizi ya chaneli. Ndiyo maana zana na huduma zipo ili kusaidia kusawazisha vituo unavyotaka.

Katika sura inayofuata, ninapendekeza kupitia dhana muhimu zaidi za mafunzo haya.

# Nenda Zaidi

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Hitimisho la Mafunzo

<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

:::video id=5f4f4344-ef27-4765-8f09-8262e6833bde:::

Katika sura hii ya mwisho inayoashiria mwisho wa mafunzo ya LNP201, ninapendekeza kurejea dhana muhimu ambazo tumeshughulikia pamoja.

Lengo la mafunzo haya lilikuwa kukupa uelewa wa kina na wa kiufundi wa Lightning Network. Tuligundua jinsi Lightning Network inategemea Bitcoin Blockchain kufanya miamala ya off-chain, huku tukihifadhi sifa za kimsingi za Bitcoin, haswa kutokuwepo kwa hitaji la kuamini nodi zingine.

### Njia za Malipo

Katika sura za awali, tulichunguza jinsi wahusika wawili, kwa kufungua njia ya malipo, wanaweza kufanya miamala nje ya Bitcoin Blockchain. Hapa kuna hatua zilizofunikwa:


- **Ufunguzi wa Kituo**: Uundaji wa kituo unafanywa kupitia muamala wa Bitcoin ambao hufunga fedha katika Anwani ya sahihi 2/2 nyingi. Amana hii inawakilisha chaneli ya Umeme kwenye Blockchain.

![LNP201](assets/en/76.webp) 2. shughuli kwenye kituo: katika kitui hiki kuna uwezekano wa kufanya shughuli nyingi bila uchapishaji kwenye Blockchain. kila Lightning transaction inaunda chaneli mpya inayoangazia kujitolea shughuli.

![LNP201](assets/en/77.webp)


- **Kulinda na Kufunga**: Washiriki wanajitolea kwa hali mpya ya kituo kwa kubadilishana funguo za ubatilishaji ili kupata pesa na kuzuia udanganyifu wowote. Pande zote mbili zinaweza kufunga chaneli kwa ushirikiano kwa kufanya muamala mpya kwenye Bitcoin Blockchain, au kama suluhu la mwisho kwa kufungwa kwa lazima. Chaguo hili la mwisho, ingawa lina ufanisi mdogo kwa sababu ni refu na wakati mwingine halijatathminiwa vizuri katika suala la ada, bado linaruhusu urejeshaji wa fedha. Katika kesi ya kudanganya, mwathirika anaweza kuadhibu mdanganyifu kwa kurejesha pesa zote kutoka kwa kituo cha Blockchain.

![LNP201](assets/en/78.webp)

### Mtandao wa Vituo

Baada ya kusoma chaneli zilizotengwa, tulipanua uchambuzi wetu kwa mtandao wa chaneli:


- **Uelekezaji**: Wakati pande mbili hazijaunganishwa moja kwa moja na chaneli, mtandao unaruhusu kuelekeza kupitia nodi za kati. Malipo kisha husafirishwa kutoka nodi moja hadi nyingine.

![LNP201](assets/en/79.webp)


- **HTLCs**: Malipo yanayopitishwa kupitia nodi za kati hulindwa na "_Hash Time-Locked Contracts_" (HTLC), ambayo huruhusu pesa kufungwa hadi malipo yakamilishwe mwanzo-mwisho.

![LNP201](assets/en/80.webp)


- **Uelekezaji wa Vitunguu**: Ili kuhakikisha usiri wa malipo, uelekezaji wa kitunguu hufunika mahali pa mwisho kwa nodi za kati. Kwa hivyo nodi ya kutuma lazima ihesabu njia nzima, lakini kwa kukosekana kwa taarifa kamili juu ya ukwasi wa njia, inaendelea kupitia majaribio mfululizo ili kuelekeza malipo.

![LNP201](assets/en/81.webp)

### Usimamizi wa Ukwasi

Tumeona kuwa usimamizi wa ukwasi ni changamoto kwenye Umeme ili kuhakikisha mtiririko mzuri wa malipo. Kutuma malipo ni rahisi kiasi: inahitaji tu kufungua kituo. Hata hivyo, kupokea malipo kunahitaji kuwa na ukwasi upande mwingine wa chaneli za mtu. Hapa kuna baadhi ya mikakati iliyojadiliwa:


- **Vituo vya Kuvutia**: Kwa kuhimiza nodi zingine kufungua njia kuelekea yeye mwenyewe, mtumiaji hupata ukwasi unaoingia.
- **Ushuru wa Kusonga**: Kwa kutuma malipo kwa vituo vingine, ukwasi uhamia upande mwingine.

![LNP201](assets/en/82.webp)


- **Kutumia Huduma kama vile Loop na Pool**: Huduma hizi huruhusu kusawazisha upya au kununua chaneli zenye ukwasi upande mwingine.

![LNP201](assets/en/83.webp)


- **Nafasi za Kushirikiana**: Pia kuna mifumo inayopatikana ya kuunganisha ili kutekeleza fursa za pembe tatu na kuwa na ukwasi unaoingia.

![LNP201](assets/en/84.webp)

# Hitimisho

<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>

## Ukaguzi na Ukadiriaji

<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>

<isCourseReview>true</isCourseReview>
## Mtihani wa mwisho

<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>

<isCourseExam>true</isCourseExam>
## Hitimisho

<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>

<isCourseConclusion>true</isCourseConclusion>
