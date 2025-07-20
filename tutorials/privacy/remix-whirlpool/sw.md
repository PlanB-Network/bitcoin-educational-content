---
name: Remix - Whirlpool
description: Je, ni michanganyiko mingapi inapaswa kufanywa kwenye Whirlpool?
---
![cover remix- wp](assets/cover.webp)


***ONYO:** Kufuatia kukamatwa kwa waanzilishi wa Samourai Wallet na kunaswa kwa seva zao mnamo Aprili 24, Zana ya Takwimu ya Whirlpool haipatikani tena kupakuliwa, kwa kuwa iliratibiwa kwenye Gitlab ya Samourai. Hata kama ulikuwa umepakua zana hii kwenye mashine yako hapo awali, au ilisakinishwa kwenye nodi yako ya RoninDojo, WST haitafanya kazi kwa wakati huu. Ilitegemea data iliyotolewa na OXT.me kwa uendeshaji wake, na tovuti hii haipatikani tena. Kwa sasa, WST sio muhimu sana kwa vile itifaki ya Whirlpool haifanyi kazi. Walakini, bado inawezekana kwamba programu hizi zinaweza kurejeshwa katika wiki zijazo. Zaidi ya hayo, sehemu ya kinadharia ya makala hii inabakia kuwa muhimu kwa kuelewa kanuni na malengo ya coinjoins kwa ujumla (sio tu Whirlpool), pamoja na kuelewa ufanisi wa mfano wa Whirlpool. Unaweza pia kujifunza jinsi ya kukadiria faragha inayotolewa na mizunguko ya CoinJoin.*


_Tunafuatilia kwa karibu maendeleo ya kesi hii pamoja na maendeleo kuhusu zana zinazohusiana. Uwe na uhakika kwamba tutasasisha mafunzo haya kadiri habari mpya zinavyopatikana._


_Mafunzo haya yametolewa kwa madhumuni ya elimu na habari pekee. Hatuidhinishi au kuhimiza matumizi ya zana hizi kwa madhumuni ya uhalifu. Ni wajibu wa kila mtumiaji kutii sheria katika eneo la mamlaka yake._


---

> *Vunja kiunga ambacho sarafu zako huacha nyuma*

Hili ni swali ninaloulizwa mara nyingi. **Unapofanya sanjari na Whirlpool, ni michanganyiko mingapi inapaswa kufanywa ili kupata matokeo ya kuridhisha?**


Madhumuni ya CoinJoin ni kutoa ukataaji unaowezekana kwa kuchanganya sarafu yako na kikundi cha sarafu zisizoweza kutofautishwa. Lengo la hatua hii ni kuvunja viungo vya ufuatiliaji, kutoka zamani hadi sasa na kutoka sasa hadi siku za nyuma. Kwa maneno mengine, mchambuzi anayejua shughuli yako ya awali wakati wa kuingia kwa mizunguko ya CoinJoin hapaswi kuwa na uwezo wa kubainisha UTXO yako wakati wa kuondoka kwa mizunguko ya remix (uchambuzi kutoka kwa mizunguko ya kuingia hadi kutoka kwa mizunguko).

![past-present links diagram](assets/en/1.webp)


Kinyume chake, mchambuzi anayejua UTXO yako wakati wa kuondoka kwa mizunguko ya CoinJoin anapaswa kushindwa kubainisha shughuli ya awali wakati wa kuingiza mizunguko (uchambuzi kutoka kwa mizunguko ya kuondoka hadi mizunguko ya kuingia).

![present-past links diagram](assets/en/2.webp)

Hata hivyo, idadi ya mchanganyiko si kigezo cha kutegemewa cha kutathmini ugumu ambao mchambuzi angekumbana nao katika kuanzisha viungo kati ya zamani na sasa, au kinyume chake. Kiashiria kinachofaa zaidi kitakuwa saizi ya vikundi ambavyo sarafu yako imejificha. Viashiria hivi vinajulikana kama "anonsets". Katika kesi ya Whirlpool, kuna aina mbili za anonsets.


Kwanza, tunaweza kubainisha ukubwa wa kikundi ambapo UTXO yako imefichwa wakati wa kutoka kwa mizunguko ya CoinJoin, yaani, idadi ya sarafu zisizoweza kutofautishwa zilizopo ndani ya kikundi hiki.

![probable UTXOs at exit](assets/en/3.webp)

Kiashirio hiki, kinachoitwa "anonset tarajiwa" kwa Kifaransa, "forward anonset" kwa Kiingereza, au "metrics za kuangalia mbele", huturuhusu kutathmini upinzani wa sarafu yako kuchanganua kufuatilia njia yake kutoka kwa kuingia hadi kwa mizunguko ya CoinJoin. Kipimo hiki kinakadiria kiwango ambacho UTXO yako inalindwa dhidi ya majaribio ya kuunda upya historia yake kutoka mahali pake pa kuingilia hadi mahali pake pa kutokea katika mchakato wa CoinJoin. Kwa mfano, ikiwa muamala wako ulishiriki katika mzunguko wake wa kwanza wa CoinJoin na mizunguko miwili ya ziada ya mkondo wa chini ikatekelezwa, uondoaji unaotarajiwa wa sarafu yako utakuwa `13`:

![forward anonset](assets/en/4.webp)

Pili, kiashiria kingine kinaweza kuhesabiwa ili kutathmini upinzani wa kipande chako kwa uchambuzi kutoka kwa sasa hadi siku za nyuma. Kwa kujua UTXO yako mwishoni mwa mizunguko, kiashirio hiki huamua idadi ya miamala inayoweza kutekelezwa ya Tx0 ambayo ingeweza kujumuisha mchango wako katika mizunguko ya CoinJoin (uchambuzi kutoka mwisho hadi mwanzo wa mizunguko). Kiashirio hiki hupima jinsi ilivyo vigumu kwa mchambuzi kufuatilia asili ya kipande chako baada ya kuunganishwa.![Probable sources at input](assets/sw/5.webp)

Jina la kiashirio hiki ni "hali ya nyuma" au "vipimo vinavyoonekana nyuma". Kwa Kifaransa, napenda kuiita "anonset rétrospectif". Katika mchoro ulio hapa chini, hii inalingana na Bubbles zote za machungwa Tx0:

![backward anonset](assets/en/6.webp)

Ili kupata maelezo zaidi kuhusu mbinu ya kukokotoa viashiria hivi, ninapendekeza usome [mazungumzo yangu ya Twitter](https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) kuhusu mada hii. Pia tunatayarisha makala ya kina zaidi kwenye Mtandao wa PlanB.


Ninajua kuwa jibu lililotolewa linaweza kuonekana kuwa lisilo la kuridhisha kwani ulitarajia idadi fulani ya mchanganyiko, na ninakuelekeza kwenye hati. Sababu ya hii ni kwamba idadi ya mchanganyiko ni kiashiria kisichoaminika cha kutathmini kutokujulikana kunakopatikana katika mizunguko ya CoinJoin. Kwa hivyo, haiwezekani kufafanua idadi isiyobadilika ya mchanganyiko kama kiwango cha usalama kamili na cha jumla.


Ni kweli kwamba kila remix ya ziada ya kipande chako huongeza seti zake za kutokujulikana. Hata hivyo, ni muhimu kuelewa kwamba kimsingi ni mchanganyiko unaofanywa na vijana wenzako ambao huchangia ukuaji wa uwezekano wako wa kutokujali. Ukiwa na muundo wa Whirlpool, muamala wako unaweza kufikia viwango vikubwa vya kutokujali kwa mizunguko miwili au mitatu ya CoinJoin pekee, kupitia shughuli za wenzao waliohusika katika miunganisho ya awali.


Anonse ya nyuma, kwa upande mwingine, sio wasiwasi katika kesi yetu. Kwa kweli, kutoka kwa CoinJoin yako ya awali, unafaidika kutokana na urithi wa shughuli za awali za bwawa, mara moja ukipa kipande chako hali ya juu ya kurudi nyuma, na ongezeko la chini katika kila mzunguko unaofuata.

Pia ni muhimu kuelewa kwamba uundaji wa kukataa kwa hakika haujakamilika. Inategemea uwezekano wa kufuatilia sarafu yako. Uwezekano huu hupungua kadri saizi ya vikundi vinavyoificha inavyoongezeka. Kwa hivyo, unapaswa kurekebisha malengo yako katika suala la anonsets kulingana na matarajio yako ya kibinafsi. Jiulize kuhusu sababu zinazokupelekea kutumia coinjoins na viwango vya kutokujulikana vinavyohitajika ili kufikia malengo haya. Kwa mfano, ikiwa matumizi ya coinjoins yanalenga tu kuhifadhi faragha ya Wallet yako wakati wa kutuma Sats chache kwa godchild wako kwa siku yao ya kuzaliwa, viwango vya juu sana vya kutokujulikana si lazima. Mtoto wako wa mungu labda hawezi kufanya uchanganuzi wa kina wa mnyororo, na hata kama wangefanya, athari kwenye maisha yako haingekuwa mbaya. Hata hivyo, ikiwa wewe ndiye mlengwa wa utawala wa kimabavu ambapo taarifa kidogo inaweza kusababisha kufungwa, vitendo vyako vitahitajika kuongozwa na vigezo vikali zaidi.


Kuamua viashiria hivi maarufu vya anoset, unaweza kutumia zana ya Python inayoitwa **WST** (Whirlpool Stats Tool).


Walakini, sio lazima kila wakati kuhesabu anonsets za kila sarafu zako zilizounganishwa. Muundo wa Whirlpool yenyewe tayari unakupa dhamana. Kama ilivyoelezwa hapo awali, kurudi nyuma anonse sio jambo la wasiwasi. Kutoka kwa mchanganyiko wako wa awali, tayari unapata alama ya juu ya retrospective. Kuhusu uondoaji unaotarajiwa, unahitaji tu kuweka sarafu yako kwenye akaunti ya baada ya mchanganyiko kwa kipindi kirefu cha kutosha. Kwa mfano, hizi hapa ni alama za anoset za mojawapo ya sarafu zangu za `100,000 Sats` baada ya kutumia miezi miwili kwenye bwawa la CoinJoin:

![WST anonsets](assets/en/7.webp)

Inaonyesha alama za rejea za `34,593` na alama zinazotarajiwa za `45,202`. Kwa maneno madhubuti, hii inamaanisha mambo mawili:


- Iwapo mchambuzi atajua sarafu yangu mwishoni mwa mizunguko na kujaribu kufuatilia asili yake, atakumbana na vyanzo vinavyowezekana `34,593`, kila kimoja kikiwa na uwezekano sawa wa kuwa wangu.
- Ikiwa mchambuzi anajua sarafu yangu mwanzoni mwa mizunguko na kujaribu kubainisha mawasiliano yake mwishoni, atakabiliwa na `45,202` zinazowezekana za UTXO, kila moja ikiwa na uwezekano sawa wa kuwa wangu.

Ndiyo maana ninachukulia matumizi ya Whirlpool kuwa muhimu hasa katika mkakati wa `HODL -> Mix -> Spend -> Replace`. Kwa maoni yangu, mbinu ya mantiki zaidi ni kuweka akiba nyingi za mtu katika bitcoins katika Cold Wallet, huku kila mara kudumisha idadi fulani ya sarafu katika CoinJoin kwenye Samourai ili kufidia gharama za kila siku. Mara tu bitcoins kutoka kwa sarafu zinatumiwa, hubadilishwa na mpya ili kurudi kwenye kizingiti kilichoelezwa cha sarafu zilizochanganywa. Njia hii inatuwezesha kujiweka huru kutokana na wasiwasi wa anonsets wa UTXOs zetu, huku tukifanya muda unaohitajika kwa coinjoins kuwa na ufanisi mdogo sana.


Natumai jibu hili limetoa mwanga juu ya mfano wa Whirlpool. Ikiwa unataka kujifunza zaidi kuhusu jinsi coinjoins inavyofanya kazi kwenye Bitcoin, napendekeza kusoma makala yangu ya kina juu ya mada hii:


https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2

**Nyenzo za nje:**


- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://estudiobitcoin.com/como-instalar-y-utilizar-Whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/
- https://medium.com/samourai-Wallet/diving-head-first-into-Whirlpool-anonymity-sets-4156a54b0bc7.