---
name: Programu Bitcoin
goal: Jenga maktaba kamili ya Bitcoin kuanzia mwanzo na uelewe misingi ya siri ya Bitcoin
objectives: 

 - Tekeleza shughuli za hesabu za uwanja finite na mkunjo wa mviringo katika Python
 - Kuunda na kuchanganua miamala ya Bitcoin kiprogramu
 - Unda anwani za testnet na utangaze miamala kupitia mtandao
 - Jifunze misingi ya hisabati inayotegemea mfumo wa usalama wa Bitcoin

---
# Safari ya Kujifunza Maandiko na Programu za Bitcoin


Kozi hii ya siku mbili yenye nguvu, inayofundishwa na Jimmy Song, inakupeleka ndani kabisa ya misingi ya kiufundi ya Bitcoin kwa kujenga maktaba kamili ya Bitcoin kuanzia mwanzo. Kuanzia na hisabati muhimu ya sehemu zenye kikomo na mikunjo ya mviringo, utaendelea kupitia uchanganuzi wa miamala, utekelezaji wa hati, na mawasiliano ya mtandao. Kupitia mazoezi ya kuandika msimbo kwa mikono katika daftari za Jupyter, utaunda anwani yako mwenyewe ya testnet, utaunda miamala kwa mikono, na kuitangaza moja kwa moja kwenye mtandao—yote huku ukipata uelewa wa kina wa kanuni za kriptografia zinazofanya Bitcoin kuwa salama na isiyoaminika.


Furahia safari!


+++

# Utangulizi


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Muhtasari wa Kozi


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Karibu kwenye kozi ya PRO 202 _**Kupanga Programu ya Bitcoin**_, safari ndefu inayokupeleka kutoka hesabu ya uwanja mdogo hadi kujenga na kutangaza miamala halisi kwenye Testnet ya Bitcoin.


Katika kozi hii, utajenga maktaba ya Bitcoin hatua kwa hatua huko Python huku ukipata misingi ya usimbaji fiche, itifaki, na programu muhimu ili kutafakari kwa usahihi kuhusu usalama na utendaji kazi wa ndani wa Bitcoin. Mbinu ya PRO 202 ni ya vitendo kabisa: kila dhana inatekelezwa mara moja katika daftari za Jupyter, kuhakikisha kwamba nadharia na msimbo vinaimarishana.


### Dhana Muhimu za Hisabati kwa Bitcoin


Sehemu hii ya kwanza inaweka msingi muhimu wa hisabati. Utatekeleza shughuli za hesabu za uwanja finite na mkunjo wa mviringo (sheria ya kikundi, kujumlisha, kuzidisha maradufu, kuzidisha kwa scalar...) — masharti ya ECDSA. Lengo ni mara mbili: kuelewa muundo wa aljebra unaofanya sahihi za kriptografia ziwezekane na kujenga zana za Python zinazoaminika za kuzibadilisha.


Kisha utarasimisha vipengele vya ECDSA: uzalishaji muhimu, umbizo la nukta, uwekaji wa alama kwenye mtandao, uundaji wa sahihi, na uthibitishaji. Sehemu hii inaunganisha moja kwa moja nadharia na utendaji, ikisisitiza maelezo ya utekelezaji na uthabiti wa mfumo wa usalama wa msingi.


### Utendaji wa Ndani wa Muamala wa Bitcoin


Katika sehemu ya pili, utachambua muundo wa muamala wa Bitcoin: UTXO, ingizo/matokeo, mfuatano, hati, usimbaji, na zaidi. Utaandika msimbo ili kuunda, kusaini, na kuthibitisha miamala, na kupata uelewa sahihi wa kile kinachofanywa na hashi na kwa nini.


Kisha, utatekeleza mtekelezaji mdogo wa _Script_, utakagua opcode muhimu, na kuthibitisha njia za matumizi. Lengo ni kukufanya uweze kukagua tabia ya miamala, kugundua hitilafu za uthibitishaji, na kufikiria kuhusu usalama wa sera za matumizi.


### Utendaji wa Ndani wa Mtandao wa Bitcoin


Katika sehemu ya tatu, utaweka miamala ndani ya mfumo mpana zaidi: muundo wa vitalu, vichwa vya habari, ugumu, na utaratibu wa Proof-of-Work. Utashughulikia jumbe za itifaki, vichwa vya habari vya vitalu, na miti ya Merkle.


Hatimaye, utajifunza mawasiliano ya nodi kati ya rika, uboreshaji wa ujumbe, na utangulizi wa SegWit.


Kama ilivyo kwa kila kozi kuhusu Plan ₿ Academy, sehemu ya mwisho inajumuisha tathmini iliyoundwa ili kuimarisha uelewa wako. Uko tayari kufichua utendaji kazi wa ndani wa Bitcoin na kuandika msimbo unaoiwezesha? Tuanze!










# Dhana Muhimu za Hisabati kwa Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Hisabati kwa Utekelezaji wa Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Misingi ya Programu ya Bitcoin: Miundo ya Kimsingi ya Hisabati


Kozi hii inafupisha hesabu muhimu nyuma ya mifumo ya kriptografia ya Bitcoin katika mtiririko wa kazi wenye vitendo sana. Dhana zinaelezewa, zinaonyeshwa kwa mifano, na kisha zinatekelezwa katika Daftari la Jupyter. Wazo elekezi ni rahisi: unaelewa kihalisi tu kriptografia ya awali mara tu unapoiweka msimbo. Katika muundo wa siku mbili, wanafunzi wa generate testnet hushughulikia, huunda na kutangaza miamala, na hatimaye huingiliana na mtandao bila wachunguzi wa block. Yote haya yanahitaji msingi imara katika sehemu zenye kikomo na mikondo ya mviringo.


### Sehemu za Mwisho: Injini ya Hesabu ya Uandishi wa Siri


Sehemu yenye kikomo F(p) ni mfumo wa hesabu unaofafanuliwa na nambari kuu p, yenye vipengele kuanzia 0 hadi p–1. Sehemu kuu huhakikisha kila kipengele kisicho na sifuri kina kinyume na shughuli zote hubaki ndani ya sehemu. Hesabu huzunguka kwa kutumia modulo p kwa ajili ya kujumlisha, kutoa, na kuzidisha. `pow(base, exp, mod)` ya Python huwezesha uainishaji wa moduli wenye ufanisi, muhimu kwa vielelezo vikubwa vinavyotumika katika shughuli halisi za kriptografia.


#### Tabia ya Kuzidisha

Kuzidisha kipengele chochote kisicho na sifuri k kwa vipengele vyote vya sehemu kuu hutoa mabadiliko ya sehemu. Sifa hii inahakikisha usawa na kuzuia udhaifu wa kimuundo, na kufanya sehemu kuu kuwa bora kwa ajili ya uzalishaji salama wa ufunguo na sahihi za kidijitali.


#### Idara na Nadharia Ndogo ya Fermat

Mgawanyiko unatekelezwa kupitia kinyume cha kuzidisha. Nadharia Ndogo ya Fermat inasema kwamba

n^(p–1) ≡ 1 (mod p),

kwa hivyo kinyume chake ni n^(p–2). Python huunga mkono hili moja kwa moja na `pow(n, -1, p)`. Shughuli hizi huonekana kila mara katika utaratibu wa msingi wa kriptografia wa ECDSA na Bitcoin.


### Mikunjo ya Elliptic: Miundo Isiyo ya Mstari kwa Usalama wa Ufunguo wa Umma


Mikunjo ya duaradufu hufuata mlinganyo wa y² = x³ + shoka + b. Bitcoin hutumia secp256k1, iliyofafanuliwa kama y² = x³ + 7 juu ya uwanja wenye kikomo. Pointi kwenye mkunjo wa duaradufu huunda kundi la hisabati chini ya nyongeza ya nukta. Mstari uliochorwa kupitia nukta mbili P na Q huingilia mkunjo katika nukta ya tatu R; kuonyesha R kwenye mhimili wa x hutoa P + Q. Mfumo huu ni wa kiunganishi na unajumuisha kipengele cha utambulisho: nukta katika infinity.


Kuongeza nukta mara mbili hutumia mstari wa tanjenti badala ya mstari wa siri, wenye mteremko unaotokana na derivative ya mkunjo. Ingawa fomula hizi zinahusisha hesabu juu ya nambari halisi, huwa tofauti kabisa na sahihi wakati mkunjo unafafanuliwa juu ya uwanja wenye kikomo—muktadha unaotumika katika Bitcoin.


### Kutoka Hisabati hadi Uandishi wa Faili wa Bitcoin


Sehemu zenye kikomo hutoa hesabu inayoweza kuamuliwa na isiyoweza kugeuzwa; mikunjo ya mviringo hutoa muundo usio wa mstari ambapo kuhesabu k·P ni rahisi lakini kuirudisha nyuma haiwezekani kimahesabu. Kuchanganya zote mbili hutoa msingi wa funguo za umma/binafsi za Bitcoin, sahihi za ECDSA, na usalama wa miamala. Kuelewa misingi hii huwaandaa wanafunzi kutekeleza funguo, miamala, na sahihi moja kwa moja—bila vifupisho au zana za nje.


## Usimbaji wa Umbo la Elliptic

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Sura hii inawasilisha mikunjo ya mviringo iliyofafanuliwa juu ya sehemu zenye kikomo na inaelezea kwa nini huunda uti wa mgongo wa hisabati wa usimbaji fiche wa Bitcoin. Ingawa mikunjo ya mviringo juu ya nambari halisi inaonekana laini na inayoendelea, kutumia milinganyo sawa juu ya sehemu yenye kikomo huunda seti ya nukta zilizotawanyika na zilizotawanyika. Licha ya tofauti ya kuona, fomula zote za kuongeza nukta, miteremko, na sheria za aljebra hufanya kazi sawa kabisa—ni hesabu tu inayobadilika kuwa hesabu ya moduli. Bitcoin inatumia mkunjo y² = x³ + 7 (secp256k1), ambayo huhifadhi ulinganifu na tabia isiyo ya mstari muhimu kwa usalama wa usimbaji fiche.


### Kuthibitisha Pointi na Utekelezaji wa Sehemu ya Mwisho


Pointi iko kwenye mkunjo wa mviringo wa uwanja mdogo ikiwa viwianishi vyake vinakidhi mlinganyo wa mkunjo chini ya modulo p. Kuthibitisha pointi kama vile (73,128) kwenye F₁₃₇ kunahitaji kuangalia kwamba y² mod p ni sawa na x³ + 7 mod p. Kutekeleza hili katika msimbo kunahusisha kuunda madarasa ya vipengele vya uwanja mdogo na pointi za mkunjo. Upakiaji wa opereta unahakikisha kwamba hesabu zote—kuongeza, kuzidisha, uainishaji, mgawanyiko—zinafanywa kiotomatiki modulo p. Mara tu vifupisho hivi vitakapokuwepo, shughuli za hali ya juu zaidi za kriptografia huwa rahisi kuandika na kutafakari.


#### Sifa za Kundi na Nyongeza ya Pointi

Pointi za mkunjo wa duaradufu huunda kundi la hisabati linaloongezwa. Kundi hilo linakidhi kufungwa, ushirika, utambulisho (nukta katika infinity), na kinyume chake (tafakari katika mhimili wa x). Miundo ya kijiometri inathibitisha sifa hizi, na kufanya kuzidisha kwa skala (P imeongezwa yenyewe mara kwa mara) kufafanuliwa vyema. Sheria hizi za kikundi huwezesha usimbaji fiche wa mkunjo wa duaradufu na kuhakikisha tabia thabiti na inayoweza kutabirika chini ya shughuli za nukta zinazorudiwa.


### Vikundi vya Mzunguko na Tatizo la Logariti Isiyotenganishwa


Kuchagua nukta ya jenereta G kwenye mkunjo huturuhusu generate kuwa kundi la mzunguko: G, 2G, 3G, …, nG = 0. Nukta hizo huonekana zisizo za mstari na zisizotabirika, hata zinapozalishwa mfululizo. Kutotabirika huku huunda msingi wa tatizo la logarithm tofauti: kukokotoa P = sG ni rahisi, lakini kubaini s kutoka P haiwezekani kimahesabu kwa vikundi vikubwa. Kitendakazi hiki cha njia moja ndicho kinachofanya usimbaji fiche wa ufunguo wa umma kuwa salama. Scalars (funguo za kibinafsi) zimeandikwa kwa herufi ndogo; nukta (funguo za umma) kwa herufi kubwa.


#### Uzidishaji wa Scalar Ufanisi

Ili kukokotoa sG kwa ufanisi, utekelezaji hutumia algoriti ya mara mbili na kuongeza: kuchanganua uwakilishi wa jozi wa scalar, kuongeza mara mbili nukta kila hatua, na kuongeza G tu wakati biti ni 1. Hii hupunguza hesabu kutoka kwa nyongeza za O(n) hadi O(log n), kuwezesha shughuli za vitendo za kriptografia hata kwa sklari za biti 256.


#### Mkunjo wa secp256k1 katika Bitcoin


Bitcoin hutumia mkunjo secp256k1, unaofafanuliwa na y² = x³ + 7 juu ya sehemu kuu ambapo p = 2²⁵⁶ − 2³² − 977. Sehemu ya jenereta G ina viwianishi vilivyochaguliwa kwa kutumia utaratibu wa NUMS unaoamua ("hakuna kitu juu ya mkono wangu"). Mpangilio wa kikundi n ni sehemu kuu kubwa karibu na 2²⁵⁶, kuhakikisha kwamba kila sehemu isiyo na sifuri hutoa kundi moja. Ukubwa wa 2²⁵⁶ (~10⁷⁷) ni mkubwa kiasili, na kufanya kulazimisha funguo za kibinafsi kuwa jambo lisilowezekana kimwili. Hata kompyuta kubwa trilioni zinazoendesha kwa miaka trilioni hazingepunguza nafasi ya ufunguo kwa njia yenye maana.


### Funguo za Umma, Funguo za Kibinafsi, na Uainishaji wa SEC


Ufunguo wa faragha ni skali isiyo ya kawaida; ufunguo wa umma ni P = sG. Kwa sababu kutatua tatizo la kumbukumbu tofauti hakuwezekani, P inaweza kushirikiwa bila kufichua s. Funguo za umma lazima ziandikwe kwa mfululizo kwa ajili ya uwasilishaji kwa kutumia umbizo la SEC. Umbizo la SEC lisilobanwa hutumia baiti 65: kiambishi awali 0x04 + x kuratibu + y kuratibu. Umbizo lililobanwa hutumia baiti 33 pekee: kiambishi awali 0x02 au 0x03 (kulingana na usawa wa y) + x kuratibu. Bitcoin hapo awali ilitumia funguo ambazo hazibanwa lakini sasa inapendelea zile zilizobanwa kwa ufanisi.


#### Uundaji wa Bitcoin Address


Anwani za Bitcoin ni mizunguko ya funguo za umma, si funguo ghafi zenyewe. Ili kupata anwani ya generate, panga ufunguo wa umma katika umbizo la SEC kwa mpangilio, hesabu hash160 (SHA‑256 kisha RIPEMD‑160), andaa kiambishi awali cha mtandao (0x00 kwa mainnet, 0x6F kwa testnet), hesabu checksum kwa kutumia SHA‑256 maradufu, ongeza baiti nne za kwanza za checksum, na usimbue matokeo kwa kutumia Base58. Usimbaji huu huondoa herufi zisizoeleweka na hujumuisha checksum ili kuzuia makosa ya unukuzi. Bomba la hatua nyingi huficha ufunguo wa umma hadi matumizi yatakapotokea, huongeza utambulisho wa mtandao, na kuhakikisha anwani zinazoweza kusomwa na binadamu na zinazostahimili hitilafu.


# Utendaji wa Ndani wa Muamala wa Bitcoin

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Uchanganuzi wa Muamala wa Bitcoin na Saini za ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### Kuelewa ECDSA: Wakfu wa Saini ya Dijitali wa Bitcoin


Bitcoin inategemea ECDSA, mpango wa sahihi unaotegemea mkunjo wa duaradufu unaotoa usalama imara wenye ukubwa mdogo zaidi wa funguo kuliko RSA. Usalama wake unatokana na tatizo la logarithm tofauti ya mkunjo wa duaradufu: ikizingatiwa P = eG, kuhesabu P ni rahisi, lakini kupata e kutoka P haiwezekani kimahesabu. Ukosefu huu wa ulinganifu huwezesha usimbaji fiche wa funguo za umma huku ukiweka funguo za faragha salama.


#### Usimbaji wa DER wa Saini za ECDSA


Bitcoin husimba sahihi za ECDSA kwa kutumia umbizo la DER:


- 0x30 (alama ya mfuatano)
- baiti ya urefu
- 0x02 + urefu + baiti za R
- 0x02 + urefu + baiti S


Hii inaongeza gharama ya uendeshaji, ikipanua sahihi ya baiti 64 hadi baiti ~71–72. Taproot huondoa utoshelevu huu kwa kutumia sahihi za Schnorr zenye ukubwa usiobadilika.


### Ahadi za Saini na Mchakato wa Kusaini


Saini za ECDSA hutegemea mlinganyo wa ahadi: UG + VP = KG. Mtia sahihi huchagua thamani zisizo sifuri za U na V, na K isiyo na mpangilio nasibu, ikithibitisha ujuzi wa ufunguo wa faragha bila kuufichua. Ujumbe huingizwa kwenye Z, K isiyo na mpangilio nasibu huzalishwa, R ni mratibu wa x wa K, na S = (Z + RE)/K. Saini ni jozi (R, S). Usalama unategemea sana kutumia K ya kipekee, isiyotabirika—ikiwa K itatumika tena au kuvuja, ufunguo wa faragha utaathiriwa. Utekelezaji wa kisasa hutumia kizazi cha K kinachoamua (RFC 6979) ili kuepuka kushindwa kwa RNG.


#### Uthibitishaji wa Saini

Kwa kuzingatia Z, (R, S), na ufunguo wa umma P, kithibitishaji huhesabu U = Z/S na V = R/S, kisha huangalia kama mratibu x wa UG + VP ni sawa na R. Hii inafanya kazi kwa sababu aljebra ya uthibitishaji hujenga upya KG bila kuhitaji ufunguo wa faragha. Kuunda sahihi kutahitaji kutatua tatizo la kumbukumbu tofauti au kuvunja chaguo la kazi la hashi.


#### Saini za Schnorr na Muktadha wa Kihistoria


Saini za Schnorr ni safi zaidi kihisabati na zinaunga mkono vipengele vya ujumuishaji, lakini zilitiwa hati miliki wakati Bitcoin ilipozinduliwa. ECDSA ilitoa mbadala wa bure, ingawa ulikuwa na ugumu zaidi na sahihi kubwa zaidi. Kwa kuwa hati miliki ziliisha muda wake, Bitcoin iliongeza sahihi za Schnorr kupitia Taproot, ikitoa sahihi zisizobadilika za baiti 64 na faragha iliyoboreshwa. ECDSA inasalia kuungwa mkono kwa utangamano wa zamani.



### Muundo wa Muamala na Pembejeo/Matokeo


Muamala wa Bitcoin unajumuisha:


- toleo (baiti 4, little-endian)
- orodha ya ingizo
- orodha ya matokeo
- muda wa kufunga (baiti 4)


Ingizo hurejelea UTXO zilizopita kwa kutumia hash yao ya muamala na faharasa ya matokeo, na hujumuisha hati ya kufungua (scriptSig) na nambari ya mfuatano inayotumika kwa muda wa kufunga au RBF. Matokeo hubainisha kiasi (baiti 8) na hati ya kufunga (scriptPubKey), ikifafanua masharti ya matumizi. Anwani za Bitcoin ni uwakilishi wa hati hizi.


#### Mfano wa UTXO

Bitcoin hufuatilia matokeo ambayo hayajatumika badala ya salio la akaunti. UTXO lazima zitumike kabisa—matumizi ya sehemu haiwezekani. Ili kutumia BTC 1 kutoka kwa BTC 100 UTXO, muamala lazima ujumuishe matokeo ya mabadiliko. Kusahau matokeo ya mabadiliko hubadilisha yaliyobaki kuwa ada ya wachimbaji madini.


#### Uainishaji na Uchanganuzi wa Muamala


Miamala hutumia umbizo la jozi dogo. Baada ya sehemu ya toleo, varint husimba idadi ya ingizo. Ingizo ni pamoja na:


- hash ya tx iliyopita (baiti 32)
- faharasa ya matokeo (baiti 4)
- scriptSig (varstr)
- mfuatano (baiti 4)


Matokeo hujumuisha kiasi cha baiti 8 na scriptPubKey (varstr). Locktime hudhibiti wakati muamala unapokuwa halali. Uainishaji hutumia mpangilio mdogo wa endian kwa nambari nyingi kamili. Vichanganuzi hutumia baiti mfululizo na hugawa kwa madarasa maalum kwa ajili ya ingizo, matokeo, na hati.


### Ada, Mabadiliko, na Unyumbulifu


Ada ni dhahiri:

ada = jumla (thamani za pembejeo) – jumla (thamani za matokeo).

Thamani yoyote isiyogawiwa inakuwa ada, na kufanya ujenzi sahihi wa matokeo ya mabadiliko kuwa muhimu. Kabla ya SegWit, sahihi ziliruhusu ubadilikaji—kubadilisha S hadi N-S kulizalisha muamala mpya halali wenye kitambulisho tofauti. Bitcoin sasa inatekeleza sheria ya chini ya S, na SegWit hutenga sahihi kutoka kwa hesabu ya txid, na kufanya vitambulisho kuwa thabiti na kuwezesha itifaki za safu ya pili kama vile Lightning.


## Hati ya Bitcoin na Uthibitisho wa Muamala

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Hati ya Bitcoin ni lugha ndogo ya mkataba mahiri, inayotegemea mrundiko inayofafanua jinsi sarafu zinavyoweza kutumika. Kila matokeo hubeba scriptPubKey (hati ya kufunga) na kila ingizo hubeba scriptSig (hati ya kufungua). Kwa pamoja huunda programu ambayo lazima itathminiwe kuwa "kweli" ili matumizi yawe halali. Hati haijakamilika kwa makusudi ili njia zote za utekelezaji ziweze kutabirika na rahisi kuthibitisha katika mtandao.


### Mfano wa Uendeshaji wa Hati na Utekelezaji


Hati ni mfuatano wa vipengele vya data na opcode. Visukuma data (saini, funguo za umma, hashi) huwekwa kwenye rundo, huku opcode zinazoanza na `OP_` zikibadilisha rundo. Baada ya utekelezaji, kipengele cha rundo la juu lazima kiwe si sifuri kwa mafanikio. Mifano: `OP_DUP` hurudia kipengele cha juu, `OP_HASH160` hutumia SHA256 kisha RIPEMD160, na `OP_CHECKSIG` huthibitisha sahihi dhidi ya sighash ya muamala na ufunguo wa umma, ikisukuma 1 kwa halali, 0 kwa batili. Sheria za uchanganuzi hutofautisha kati ya data ghafi (iliyoanzishiwa urefu) na opcode (zinazotafutwa kwa thamani ya baiti), na mashine ndogo pepe huzitekeleza kiholela kwenye kila nodi.


### P2PK na P2PKH: Mifumo ya Malipo ya Msingi


Muundo wa mapema zaidi, Pay-to-Pub-Key (P2PK), ulifunga sarafu moja kwa moja kwenye ufunguo kamili wa umma: scriptPubKey ni `<pubkey> OP_CHECKSIG`, na scriptSig ni sahihi tu. Ni rahisi lakini haina nafasi nzuri na hufichua ufunguo wa umma kabla ya sarafu hizo kutumika.


#### P2PKH na Anwani

Kifunguo cha Kulipa-kwa-Umma-Hash (P2PKH) huboresha hili kwa kufunga kwenye hashi ya baiti 20 ya ufunguo wa umma. Kifunguo cha scriptPub ni `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, na scriptSig hutoa `<saini> <pubkey>`. Utekelezaji huangalia kwamba ufunguo wa umma uliotolewa huhamisha thamani iliyoahidiwa na kisha huthibitisha sahihi. Hii huficha ufunguo wa umma hadi utumie muda, hupunguza ukubwa, na inalingana na umbizo la anwani la "1..." la mainnet linalojulikana.


### Uthibitishaji wa Muamala na Uwekaji Hash wa Saini


Nodi inayothibitisha muamala lazima ihakikishe:

1) Kila ingizo hurejelea matokeo yaliyopo, ambayo hayajatumika.

2) Jumla ya thamani ya pembejeo ≥ jumla ya thamani ya matokeo (tofauti ni ada).

3) Kila scriptSig hufungua kwa usahihi scriptPubKey yake iliyorejelewa.


Uthibitishaji wa sahihi unahitaji kujenga ujumbe halisi uliosainiwa, unaoitwa sighash. Kwa ECDSA ya zamani, uthibitishaji huondoa scriptSigs zote, hubadilisha scriptSig ya ingizo la sasa na scriptPubKey inayolingana, huongeza aina ya hash ya baiti 4 (kawaida `SIGHASH_ALL`), na huweka mara mbili matokeo. Thamani hiyo ya biti 256 ndiyo `OP_CHECKSIG` hutumia. Aina mbadala za hash (k.m., `SINGLE`, `HAKUNA`, ikiwa na au bila `ANYOONECANPAY`) hubadilisha sehemu za muamala ambazo zimejitolea, na kuwezesha kesi za matumizi maalum kama vile ufadhili wa ushirikiano au miamala iliyoainishwa kwa kiasi fulani, lakini hazitumiki sana katika vitendo.


#### Hashing ya Quadratic na SegWit

Kwa sababu kila ingizo katika muamala wa zamani linahitaji hesabu yake ya sighash juu ya muundo unaojumuisha ingizo zote, muda wa uthibitishaji unaweza kukua mara nne kulingana na idadi ya ingizo. Miamala mikubwa ya ingizo nyingi hapo awali ilisababisha ucheleweshaji unaoonekana wa uthibitishaji. SegWit ilibadilisha upya hesabu ya sighash ili kuhifadhi sehemu zilizoshirikiwa na kupunguza ugumu hadi wakati wa mstari, ikiboresha uwezo wa kupanuka na kufanya mashambulizi ya kukataa huduma kuwa magumu zaidi.


### Mafumbo ya Hati na Masomo ya Usalama


Hati inaweza kuelezea zaidi ya "saini moja hufungua sarafu hizi." Mafumbo ya hati yanaonyesha hili kwa kusimba masharti yasiyo na msingi—matatizo ya hesabu, changamoto za hash preimage, au hata zawadi za mgongano—ambapo mtu yeyote anayetoa data sahihi anaweza kutumia sarafu hizo. Hata hivyo, matokeo ambayo hutegemea data ya umma pekee (bila sahihi) yanaweza kuathiriwa na uendeshaji wa mbele wa wachimbaji: mara tu suluhisho halali linapoonekana kwenye mempool, mchimbaji yeyote anaweza kuinakili na kuelekeza malipo kwake mwenyewe.


Somo la vitendo ni kwamba mikataba ya ulimwengu halisi karibu kila mara hujumuisha ukaguzi wa sahihi, hata wakati ina mantiki ngumu zaidi kama vile multisig, timelocks, au hashlocks. Saini hufunga suluhisho kwa mhusika maalum, kuhifadhi motisha na kuzuia wengine kuiba malipo. Kuelewa mfumo wa rafu wa Script, mifumo ya kawaida, na mitego midogo ni muhimu kwa kubuni mikataba salama ya Bitcoin na kwa kuzingatia jinsi miamala inavyothibitishwa kwenye mtandao.


## Ujenzi wa Miamala na Malipo kwa Hati Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Kujenga Miamala ya Bitcoin na P2SH


Ujenzi wa muamala wa Bitcoin huunganisha maarifa ya itifaki ya kinadharia na utekelezaji wa vitendo. Muamala huchagua UTXO za kutumia, huunda matokeo kwa kutumia hati za kufunga, huunda sahihi kwa kila ingizo, na huweka kila kitu katika mpangilio sahihi wa nodi zinazotarajiwa. Mchakato unahitaji kuelewa uzalishaji wa sighash, tabia ya Hati, na utunzaji sahihi wa ada na mabadiliko.


### Ujenzi wa Muamala wa Msingi


Kila ingizo la muamala hurejelea matokeo ya awali ya txid na faharasa. Matokeo hubainisha kiasi katika hati za satoshi na kufunga. Tofauti kati ya jumla ya ingizo na jumla ya matokeo ni ada. Ili kusaini ingizo, toleo lililobadilishwa la muamala huorodheshwa kwa mfuatano, pumzi yake huhesabiwa, na ufunguo wa faragha husaini. Saini inayotokana na ufunguo wa umma huunda ScriptSig. Mara tu kila ingizo litakaposainiwa, muamala mbichi unaweza kutangazwa kwenye mtandao.


### Miamala ya Saini Nyingi


Bare multisig hutumia `OP_CHECKMULTISIG` kuhitaji sahihi za m-of-n. Kutokana na hitilafu ya awali ya nje ya moja kwa moja, OP_CHECKMULTISIG hutumia kipengele cha ziada cha raki, kikihitaji `OP_0` ya awali katika ScriptSig. Bare multisig inafanya kazi lakini haifanyi kazi vizuri: funguo zote za umma zinaonekana on-chain, na kufanya scriptPubKeys kuwa kubwa, ghali, na vigumu kusimba kama anwani. Vikwazo hivi vilichochea kuanzishwa kwa hashi ya malipo-kwa-hati-ya-hati.


#### Usanifu wa P2SH

P2SH huficha hati changamano nyuma ya HASH160 ya baiti 20. ScriptPubKey imerekebishwa: `OP_HASH160 <hashi ya baiti 20 OP_EQUAL`. Hati ya msingi ya ukombozi—iliyo na sig nyingi, muda wa kufunga, au hali nyingine—hufunuliwa na kutekelezwa tu wakati wa matumizi. Mtumaji huona hashi pekee, huku mpokeaji akisimamia hati ya ukombozi kwa faragha. Muundo huu hupunguza ukubwa wa on-chain, huboresha faragha, na huwezesha mikataba changamano bila kuwapa mzigo watumaji.


### Matumizi na Utekelezaji wa P2SH


Ili kutumia matokeo ya P2SH, ScriptSig lazima ijumuishe data muhimu ya kufungua *pamoja na* hati ya kukomboa yenyewe. Uthibitishaji hutokea katika hatua mbili:

1) HASH160(redeem_script) lazima ilingane na hashi ya scriptPubKey.

2) Baada ya uthibitishaji, hati ya kukomboa inatekelezwa kwa kutumia data iliyotolewa.


Wakati wa kutengeneza sahihi za ingizo la P2SH, mchakato wa sighash hutumia hati ya kukomboa badala ya scriptPubKey. Kila mtiaji saini lazima awe na hati kamili ya kukomboa kwa sahihi halali za generate. Anwani za P2SH hutumia toleo la baiti 0x05 kwenye mainnet (anwani za ("3...") na 0xC4 kwenye testnet (anwani za ("2...").


#### Mambo ya Kuzingatia Usalama kwa Vitendo


Kupoteza hati ya kukomboa kunamaanisha kupoteza fedha: matumizi yanahitaji funguo za kibinafsi na hati ya kukomboa yenyewe. Washiriki wa Multisig lazima wathibitishe kwamba funguo zao za umma zimejumuishwa kwa usahihi kabla ya kukubali amana. P2SH inasaidia miundo ya hali ya juu kama vile multisig, timelocks, na hashlocks, lakini makosa katika mantiki ya hati yanaweza kufunga fedha kabisa, kwa hivyo majaribio kwenye testnet ni muhimu.


P2SH inaboresha faragha kwa kuficha masharti ya matumizi hadi matumizi ya kwanza, lakini mara tu hati ya ukombozi inapoonekana on-chain, inaonekana kabisa. Licha ya haya, faida za ukubwa uliopunguzwa, utangamano wa nyuma, na usaidizi wa mkataba unaonyumbulika zilifanya P2SH kuwa hatua muhimu, ikishawishi maboresho ya baadaye kama vile SegWit na Taproot.


# Utendaji wa Ndani wa Mtandao wa Bitcoin

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Vitalu vya Bitcoin na Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Bitcoin huzuia miamala ya pamoja na kuilinda kwa kutumia proof of work. Kila kizuizi kina kichwa cha habari cha baiti 80 pamoja na orodha ya miamala. Licha ya gharama kubwa ya nishati ya kutengeneza kizuizi halali, kuthibitisha kimoja ni nafuu: kuhifadhi vichwa vyote vya habari vya ~900k kunahitaji ~72 MB pekee, hivyo kuruhusu hata vifaa vidogo kuthibitisha proof of work ya mnyororo kwa ufanisi.


### Miamala ya Coinbase na Zawadi za Block


Kila kizuizi huanza na muamala mmoja wa Coinbase—njia pekee ambayo bitcoin mpya huingia kwenye mzunguko. Ina hash ya prev-tx iliyo na sifuri na faharisi ya 0xffffffff, ikiitambulisha kipekee. Ruzuku ilianza kwa BTC 50 na nusu kila vitalu 210,000 (50, 25, 12.5, 6.25, 3.125, …). Wachimbaji pia hujumuisha ada za muamala. Kwa sababu nonce ya baiti 4 ni ndogo sana kwa ASIC za kisasa, wachimbaji hubadilisha data katika muamala wa Coinbase ili kubadilisha mzizi wa Merkle na kuunda nafasi ya ziada ya utafutaji. BIP34 inahitaji kupachika urefu wa kizuizi katika hati ya CoinbaseSig ili kuhakikisha kila Coinbase txid ni ya kipekee.


### Sehemu za Kichwa cha Vitalu na Ishara ya Soft Fork


Kichwa cha habari cha baiti 80 kina:


- toleo (baiti 4)
- hashi ya awali ya kizuizi (baiti 32)
- Mzizi wa Merkle (baiti 32)
- muhuri wa muda (baiti 4)
- biti (lengo la ugumu, baiti 4)
- nonce (baiti 4)


Nambari za matoleo zilibadilika na kuwa mfumo wa kuashiria sehemu ndogo kupitia BIP9, na kuruhusu wachimbaji kuratibu utayari wa fork laini. Muhuri wa muda ni thamani ya muda ya Unix ya biti 32 na itahitaji kusasishwa karibu mwaka wa 2106.


#### Sehemu na Malengo ya Vipande

Sehemu ya biti husimba lengwa katika umbo dogo: lengo = mgawo × 256^(kielelezo−3). Hashi halali za vitalu lazima ziwe chini ya lengo hili kwa nambari. Kwa sababu hashi hutafsiriwa kama nambari kamili za endian, hashi halali mara nyingi huonekana na sufuri nyingi zinazofuata zinapoonyeshwa katika heksi.


### Ugumu, Uthibitishaji, na Marekebisho


Ugumu hufafanuliwa kama lengo_la_chini/lengo_la_mkondoni, ikionyesha jinsi mining ilivyo ngumu zaidi leo ikilinganishwa na ugumu rahisi zaidi. Uthibitishaji unahitaji tu kulinganisha hash ya kichwa cha habari na shabaha—nafuu sana ikilinganishwa na mining.


Kila vizuizi vya 2016, Bitcoin hurekebisha ugumu ili kufikia vipindi vya vizuizi vya dakika ~10. Marekebisho hayo yanalinganisha muda halisi wa vizuizi vya 2016 vilivyopita na wiki mbili zinazotarajiwa. Vizuizi huweka marekebisho ndani ya kipindi cha nne. Matukio makubwa ya ulimwengu halisi—kama vile marufuku ya mining ya Uchina—yalionyesha uthabiti wa utaratibu huu wakati kiwango cha hashi kilipungua sana na ugumu kurekebishwa chini ili kufidia.


### Ruzuku ya Vitalu na Jumla ya Supply


Ruzuku katika urefu wa h inahesabiwa kama: ruzuku = 5_000_000_000 >> (h // 210_000). Hii hutoa ratiba ya kupunguza nusu ambayo inaungana na jumla ya usambazaji wa ~21 milioni BTC. Kwa muhtasari wa mfululizo wa kijiometri (50 + 25 + 12.5 + …) × 210,000 inaelezea kikomo. Wachimbaji wanaweza kudai chini ya ruzuku inayoruhusiwa lakini hawataki tena, au kizuizi hicho kinakuwa batili. Ruzuku zinapopungua katika nusu mfululizo, ada za miamala zinakuwa sehemu muhimu zaidi ya mapato ya wachimbaji na usalama wa mtandao wa muda mrefu.


## Mawasiliano ya Mtandao na Miti ya Merkle

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Usanifu wa Mtandao wa Bitcoin


Mtandao wa rika-kwa-rika wa Bitcoin hufanya kazi kama mfumo wa umbea uliogawanywa ambapo nodi husambaza miamala na kuzuia bila kuaminiana. Nodi mpya huongezeka kwa kuwasiliana na mbegu za DNS zenye msimbo mgumu zinazodumishwa na watengenezaji msingi. Mbegu hizi za DNS hurejesha IP za rika zinazofanya kazi, na kuwezesha nodi kugundua mtandao na kisha kuomba rika zaidi kupitia getaddr. Mtandao kwa makusudi si muhimu kwa makubaliano, kwa hivyo utekelezaji unaweza kutofautiana mradi tu sheria za makubaliano zibaki bila kubadilika.


### Muundo wa Ujumbe na Kusalimiana kwa Mkono


Ujumbe wote wa Bitcoin P2P hutumia bahasha isiyobadilika: thamani ya uchawi ya baiti 4 (F9BEB4D9 kwa mainnet), amri ya baiti 12 ya ASCII, urefu wa mzigo mdogo wa endian wa baiti 4, checksum ya baiti 4 (baiti 4 za kwanza za hash256), na mzigo wa malipo. Amri za kawaida ni pamoja na toleo, verack, inv, getdata, tx, block, getheaders, headers, ping, na pong.


Kushikana mikono huanza wakati nodi inayounganisha inapotuma ujumbe wa toleo. Mpokeaji hujibu kwa kutumia verack na toleo lake. Mara tu pande zote mbili zikibadilishana ujumbe huu mbili, muunganisho unakuwa hai na nodi zinaweza kuanza kusambaza orodha na data.


### Miti ya Merkle na Mizizi ya Merkle


Bitcoin huhifadhi mzizi mmoja wa Merkle wa baiti 32 katika kila kichwa cha vitalu kama ahadi ya miamala yote kwenye vitalu. Miamala huharakishwa (hash256), kuoanishwa, kuunganishwa, na kuharakishwa mara kwa mara hadi hashi moja ibaki. Wakati kiwango kina hesabu isiyo ya kawaida, hashi ya mwisho inarudiwa. Kwa ndani, hashi ni kubwa, huku data ya vitalu vilivyosawazishwa ikitumia little-endian, ikihitaji kubadilishwa kabla na baada ya ujenzi wa mti.


#### Merkle Proofs na SPV

Uthibitisho wa Merkle huruhusu kuthibitisha kwamba muamala umejumuishwa kwenye kizuizi bila kupakua kizuizi kizima. Uthibitisho unajumuisha hashes za ndugu kando ya njia ya mzizi. Wateja wepesi wa SPV huhifadhi vichwa vya vitalu pekee na kuomba uthibitisho huu kutoka kwa nodi kamili. Kwa sababu mti wa Merkle hukua kwa mpangilio wa kiotomatiki, kuthibitisha kuingizwa kwenye kizuizi chenye maelfu ya miamala kunahitaji baiti mia chache tu.


Taproot inapanua dhana hii kwa kuweka masharti ya matumizi kwenye mti wa hati ya Merklized (MAST), ikifunua tawi lililotekelezwa pamoja na uthibitisho wa Merkle pekee. Hii inaboresha ufanisi na faragha.


### Uendeshaji wa Mtandao na Usawazishaji wa Vizuizi


Nodi hutumia getdata kuomba miamala au vizuizi, ikibainisha aina ya kitambulisho (1=tx, 2=block, 3=filtered block, 4=compact block) pamoja na kitambulisho cha baiti 32. Kwa usawazishaji wa mnyororo, nodi hutuma getheaders zenye hash ya kuanzia, na kupokea hadi vichwa 2000 katika jibu. Kila kichwa cha habari kinachorejeshwa ni baiti 80 ikifuatiwa na hesabu ya miamala ya sifuri.


Uthibitishaji kamili wa vitalu vilivyopokelewa unahitaji ukaguzi mbili:

1. Hashi ya block lazima iwe chini ya lengo lililosimbwa katika sehemu ya biti.

2. Mzizi wa Merkle unaohesabiwa kutoka kwa miamala yote (kwa utunzaji sahihi wa mwisho) lazima ulingane na mzizi wa kichwa cha habari.


Ni pale tu ambapo hali zote mbili zitafanikiwa ndipo nodi itakubali kizuizi, ikiakisi kanuni ya Bitcoin ya "usiamini, thibitisha".


## Mawasiliano ya Kina ya Nodi na Ushahidi Uliotengwa

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Kipindi hiki kinaunganisha mtandao wa hali ya juu wa P2P na Segregated Witness, kuonyesha jinsi programu ya kisasa ya Bitcoin inavyoingiliana moja kwa moja na nodi huku ikitumia miundo ya miamala inayofahamu SegWit. Wasanidi programu hujifunza kupata vizuizi, kuchanganua miamala husika, na kujenga miamala kwa kutumia mawasiliano ghafi ya mtandao pekee—hakuna wachunguzi wa vizuizi wanaohitajika.


### Urejeshaji wa Muamala Unaotegemea Vizuizi na Faragha


Pochi lazima zigundue malipo yanayoingia kwa kuchanganua vizuizi kwa matokeo yanayolingana na scriptPubKey yao. Kurejesha vizuizi vizima hulinda faragha vizuri zaidi kuliko kuomba miamala ya mtu binafsi, ambayo huvuja ishara kali kuhusu shughuli za mtumiaji. Hata maombi ya vizuizi yanaweza kuvuja taarifa kwenye minyororo ya ujazo mdogo, na kufanya vichujio vya vizuizi vidogo (BIP158) kuwa muhimu kwa kuhifadhi faragha kwa wateja wepesi. Vichujio vinaweza kutoa chanya za uongo lakini kamwe si hasi za uongo, na kuruhusu wateja kupakua vizuizi vinavyoweza kuwa muhimu bila kufichua anwani maalum.


### Mwingiliano wa Mtandao wa Trustless


Mtiririko wa kazi wa `get_block` unaonyesha matumizi sahihi ya mtandao: tuma getdata, pokea kizuizi, kisha uthibitishe kwa kujitegemea mzizi wake wa Merkle na proof of work. Kizuizi kinakubaliwa tu ikiwa hash ya kichwa kilichopokelewa inalingana na hash iliyoombwa na mzizi wake wa Merkle uliokokotolewa unalingana na kichwa. Hii inawakilisha "usiamini, thibitisha," kuhakikisha hata wenzao hasidi hawawezi kudanganya nodi ili kukubali data iliyobadilishwa.


#### Kurejesha Miamala kutoka kwa Vitalu

Miamala ya block inaweza kuchanganuliwa kwa ajili ya kulinganisha scriptPubKeys kwa kutumia marudio rahisi. Pochi za uzalishaji hufanya hivi mfululizo kadri vitalu vipya vinavyowasili, ikithibitisha umiliki wa matokeo kupitia uthibitishaji wa kriptografia badala ya kutegemea API za wahusika wengine.


### Malengo na Ubunifu wa SegWit


Shahidi Aliyetengwa (SegWit) alirekebisha ubadilikaji wa muamala kwa kuondoa data ya sahihi kutoka kwa hesabu ya txid. Hii iliwezesha minyororo ya miamala iliyosainiwa awali inayoaminika na kufanya Lightning Network iwe ya vitendo. SegWit pia iliongeza uwezo wa vitalu kwa kutumia "uzito wa vitalu": ​​nodi za zamani bado zinaona vitalu vya ≤1 MB, huku nodi zilizoboreshwa zikithibitisha hadi 4 MB ikijumuisha data ya mashahidi. Programu za mashahidi zilizobadilishwa (v0–v1 hadi sasa) huunda njia ya uboreshaji iliyopangwa kwa aina za hati za baadaye.


#### P2WPKH (SegWit Asili)


P2WPKH inachukua nafasi ya muundo wa zamani wa P2PKH na hati ya baiti 22: OP_0 + push20 + hash160(pubkey). Matumizi huhamisha sahihi na pubkey kwenye sehemu tofauti ya ushahidi.


- Nodi za Kabla ya SegWit: tazama "mtu yeyote anaweza kutumia," ichukulie kama halali.
- Nodi za baada ya SegWit: tambua OP_0 + hashi ya baiti 20 na uthibitishe kwa kutumia data ya shahidi.


Utenganisho huu hurekebisha urahisi wa kubadilika na hupunguza ada. Shahidi hutumia hesabu ya tofauti ikifuatiwa na sahihi na kitufe cha baa.


#### P2SH-P2WPKH (SegWit Inayoendana na Nyuma)


Ili kuruhusu pochi za zamani kutuma kwa anwani za SegWit, hati za P2WPKH zinaweza kufungwa kwa P2SH.


- scriptPubKey: P2SH hash160 ya kawaida (komboa Hati)
- scriptSig: the redeemScript (programu ya P2WPKH)
- shahidi: sahihi + pubkey


Tabaka za uthibitishaji:

1. Nodi za Pre‑BIP16 zinakubali redemptionScript kama halali.

2. Nodi za Post‑BIP16 huitathmini, na kuacha OP_0 + hash kwenye rundo.

3. Nodi za SegWit hufanya uthibitishaji kamili wa shahidi.


#### P2WSH kwa Hati Changamano


P2WSH hujumuisha SegWit kwa hati nyingi na za hali ya juu kwa kutumia SHA256(hati) badala ya hash160. Mrundiko wa kawaida wa shahidi wa aina nyingi 2 kati ya 3:


- kipengele tupu (hitilafu ya CHECKMULTISIG)
- ishara1
- sig2
- hati ya shahidi (hati ya multisig)


Nodi za SegWit huthibitisha SHA256(witnessScript) inalingana na hashi ya scriptPubKey na kisha kuitekeleza. Kutumia SHA256 na hashi ya baiti 32 huruhusu kutofautisha P2WSH na P2WPKH na kuimarisha usalama.


#### P2SH-P2WSH (Utangamano wa Juu Zaidi)


Hati changamano za SegWit zinaweza pia kufungwa kwa P2SH:


- scriptSig: redeemScript (OP_0 + 32‑heshi ya baiti)
- shahidi: sahihi + hati ya shahidi


Uthibitisho hupitia vizazi vitatu vya sheria kama ilivyo kwa P2SH‑P2WPKH. Kifuniko hiki kilikuwa muhimu kwa uwekaji wa awali wa Umeme unaohitaji multisig bila unyumbufu. Ingawa P2WSH asilia inapendelewa leo, umbo lililofungwa huhakikisha utangamano katika mifumo ya zamani ya wallet.


### Athari ya SegWit


SegWit ilitoa:


- Vitambulisho thabiti vya muamala
- ada za chini kupitia data ya punguzo la mashahidi
- upitishaji wa juu wa vitalu kupitia uzito wa vitalu
- utangamano kwa nodi za zamani
- njia safi ya uboreshaji kwa ajili ya Taproot na viendelezi vya siku zijazo


Pamoja na mwingiliano usioaminika wa mtandao, zana hizi huunda uti wa mgongo wa maendeleo ya kisasa ya Bitcoin.



# Sehemu ya Mwisho


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Mapitio na Ukadiriaji


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Mtihani wa Mwisho


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Hitimisho



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>