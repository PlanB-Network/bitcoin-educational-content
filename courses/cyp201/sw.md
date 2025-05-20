---
name: Utendaji wa Ndani wa Pochi za Bitcoin
goal: Ingia kwenye kanuni za kriptografia zinazotumia pochi za Bitcoin.
objectives: 

  - Bainisha dhana za Kina (depth)dharia zinazohitajika ili kuelewa algoriti za kriptografia zinazotumika katika Bitcoin.
  - Kuelewa kikamilifu ujenzi wa Wallet ya kuamua na ya daraja.
  - Jua jinsi ya kutambua na kupunguza hatari zinazohusiana na kusimamia Wallet.
  - Elewa kanuni za utendaji wa Hash, funguo za kriptografia na sahihi za dijitali.

---
# Safari ndani ya Moyo wa Pochi za Bitcoin

Gundua siri za pochi za Bitcoin za kuamua na za hali ya juu kwa kozi yetu ya CYP201! Iwe wewe ni mtumiaji wa kawaida au mpenda shauku unayetafuta kuongeza maarifa yako, kozi hii inakupa mkazo kamili katika utendakazi wa zana hizi ambazo sisi sote hutumia kila siku.

Jifunze kuhusu mbinu za utendakazi wa Hash, sahihi za dijitali (ECDSA na Schnorr), misemo ya Mnemonic, funguo za kriptografia, na uundaji wa anwani za kupokea, yote huku ukigundua mikakati ya hali ya juu ya usalama.

Mafunzo haya sio tu yatakupa maarifa ya kuelewa muundo wa Bitcoin Wallet lakini pia yatakutayarisha kuzama zaidi katika ulimwengu wa kusisimua wa kriptografia.

Kwa ufundishaji wazi, zaidi ya michoro 60 za ufafanuzi, na mifano halisi, CYP201 itakuwezesha kuelewa kutoka A hadi Z jinsi Wallet yako inavyofanya kazi, ili uweze kuabiri ulimwengu wa Bitcoin kwa ujasiri. Chukua udhibiti wa UTXO zako leo kwa kuelewa jinsi pochi za HD zinavyofanya kazi!

+++
# Utangulizi

<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>

## Utangulizi wa Kozi

<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>

Karibu kwenye kozi ya CYP201, ambapo tutachunguza kwa Kina (depth) utendakazi wa pochi za HD Bitcoin. Kozi hii imeundwa kwa ajili ya mtu yeyote ambaye anataka kuelewa misingi ya kiufundi ya kutumia Bitcoin, iwe ni watumiaji wa kawaida, wapenzi walioelimika, au wataalam wa siku zijazo.

Lengo la mafunzo haya ni kukupa funguo za kufahamu zana unazotumia kila siku. Pochi za HD Bitcoin, ambazo ndizo msingi wa uzoefu wako wa mtumiaji, zinatokana na dhana changamano wakati fulani, ambazo tutajaribu kuzifanya zipatikane. Kwa pamoja, tutawaondoa!

Kabla ya kupiga mbizi katika maelezo ya ujenzi na uendeshaji wa pochi za Bitcoin, tutaanza na sura chache juu ya primitives ya cryptographic kujua nini Kina (depth)fuata.

Tutaanza na kazi za kriptografia za Hash, za msingi kwa pochi zote mbili na itifaki ya Bitcoin yenyewe. Utagundua sifa zao kuu, kazi maalum zinazotumiwa katika Bitcoin, na katika sura ya kiufundi zaidi, utajifunza kwa undani kuhusu kazi za malkia wa kazi za Hash: SHA256.

![CYP201](assets/fr/010.webp)

Kisha, tutajadili utendakazi wa kanuni za sahihi za kidijitali unazotumia kila siku kulinda UTXO zako. Bitcoin inatumia mbili: ECDSA na itifaki ya Schnorr. Utajifunza ni kanuni zipi za hisabati zinazozingatia kanuni hizi na jinsi zinavyohakikisha usalama wa miamala.

![CYP201](assets/fr/021.webp)

Mara tu tunapokuwa na ufahamu mzuri wa Elements hizi za kriptografia, hatimaye tutaendelea hadi kiini cha mafunzo: pochi za kuamua na za hierarchical! Kwanza, kuna sehemu iliyowekwa kwa misemo ya Mnemonic, mlolongo huu wa maneno 12 au 24 ambayo inakuwezesha kuunda na kurejesha pochi zako. Utagundua jinsi maneno haya yanatolewa kutoka kwa chanzo cha entropy na jinsi yanavyowezesha matumizi ya Bitcoin.

![CYP201](assets/fr/040.webp)

Mafunzo yataendelea na utafiti wa BIP39 passphrase, seed (bila kuchanganyikiwa na maneno ya Mnemonic), msimbo wa mnyororo mkuu, na Ufunguo (Key) mkuu. Tutaona kwa undani Elements hizi ni nini, majukumu yao husika, na jinsi zinavyohesabiwa.

![CYP201](assets/fr/045.webp)

Hatimaye, kutoka kwa Ufunguo (Key) mkuu, tutagundua jinsi jozi za funguo za kriptografia zinavyotolewa kwa njia ya kubainisha na ya kidaraja hadi anwani zinazopokea.

![CYP201](assets/fr/056.webp)

Mafunzo haya yatakuwezesha kutumia programu yako ya Wallet kwa kujiamini, huku ukiboresha ujuzi wako wa kutambua na kupunguza hatari. Jitayarishe kuwa mtaalam wa kweli katika pochi za Bitcoin!

# Kazi za Hash

<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>

## Utangulizi wa Kazi za Hash

<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>

Aina ya kwanza ya algorithms ya kriptografia inayotumiwa kwenye Bitcoin inajumuisha kazi za Hash. Wanachukua jukumu muhimu katika viwango tofauti vya itifaki, lakini pia ndani ya pochi za Bitcoin. Hebu tugundue pamoja kazi ya Hash ni nini na inatumika kwa nini katika Bitcoin.

### Ufafanuzi na Kanuni ya Hashing

Hashing ni mchakato ambao hubadilisha maelezo ya urefu wa kiholela hadi sehemu nyingine ya habari ya urefu usiobadilika kupitia kitendakazi cha kriptografia Hash. Kwa maneno mengine, kitendakazi cha Hash Kina (depth)chukua pembejeo ya saizi yoyote na kuibadilisha kuwa alama ya vidole ya saizi isiyobadilika, inayoitwa "Hash".

Hash pia wakati mwingine inaweza kujulikana kama "digest", "condensate", "condensed", au "hashed".

Kwa mfano, kazi ya SHA256 Hash inazalisha Hash ya urefu uliowekwa wa bits 256. Kwa hivyo, ikiwa tutatumia ingizo "_PlanB_", ujumbe wa urefu wa kiholela, Hash inayozalishwa itakuwa alama ya vidole 256-bit:

```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```

![CYP201](assets/fr/001.webp)

### Tabia za Kazi za Hash

Vitendaji hivi vya kriptografia vya Hash vina sifa kadhaa muhimu zinazozifanya kuwa muhimu hasa katika muktadha wa Bitcoin na mifumo mingine ya kompyuta:


- Kutoweza kutenduliwa (au upinzani wa picha)
- Upinzani wa tamper (athari ya avalanche)
- Upinzani wa mgongano
- Upinzani wa pili wa picha

#### 1. Kutoweza kutenduliwa (upinzani wa picha):

Kutoweza kutenduliwa kunamaanisha kuwa ni rahisi kuhesabu Hash kutoka kwa taarifa ya pembejeo, lakini hesabu ya kinyume, yaani, kupata pembejeo kutoka kwa Hash, haiwezekani. Sifa hii hufanya kazi za Hash kuwa bora zaidi kwa kuunda alama za vidole za dijiti za kipekee bila kuathiri maelezo asili.

Katika mfano uliotolewa, kupata Hash `24f1b9…` kwa kujua ingizo "_PlanB_" ni rahisi na haraka. Hata hivyo, kupata ujumbe "_PlanB_" kwa kujua tu `24f1b9…` haiwezekani.

![CYP201](assets/fr/002.webp)

Kwa hivyo, haiwezekani kupata taswira ya awali $m$ kwa Hash $h$ kiasi kwamba $h = \text{Hash}(m)$, ambapo $\text{Hash}$ ni kazi ya kriptografia ya Hash.

#### 2. Upinzani wa tamper (athari ya Banguko)

Sifa ya pili ni ukinzani wa tamper, pia inajulikana kama **athari ya maporomoko ya theluji**. Tabia hii inazingatiwa katika kazi ya Hash ikiwa mabadiliko madogo katika ujumbe wa uingizaji husababisha mabadiliko makubwa katika pato la Hash.

Ikiwa tunarudi kwenye mfano wetu na ingizo "_PlanB_" na chaguo la kukokotoa la SHA256, tumeona kwamba Hash iliyotolewa ni kama ifuatavyo:

```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```

Ikiwa tutafanya mabadiliko kidogo sana kwa ingizo kwa kutumia "_Planb_" wakati huu, kisha kubadilisha kutoka kwa herufi kubwa "B" hadi herufi ndogo "b" hubadilisha kabisa pato la SHA256 Hash:

```text
bb038b4503ac5d90e1205788b00f8f314583c5e22f72bec84b8735ba5a36df3f
```

![CYP201](assets/fr/003.webp)

Mali hii inahakikisha kwamba hata mabadiliko madogo ya ujumbe wa awali yanaonekana mara moja, kwani haibadilishi tu sehemu ndogo ya Hash, lakini Hash nzima. Hii inaweza kuwa ya manufaa katika nyanja mbalimbali ili kuthibitisha uadilifu wa ujumbe, programu, au hata miamala ya Bitcoin.

#### 3. Upinzani wa Mgongano

Tabia ya tatu ni upinzani wa mgongano. Chaguo za kukokotoa za Hash ni sugu kwa mgongano ikiwa haiwezekani kwa hesabu kupata jumbe 2 tofauti zinazotoa matokeo sawa ya Hash kutoka kwa chaguo la kukokotoa. Rasmi, ni vigumu kupata jumbe mbili tofauti $m_1$ na $m_2$ kama vile:

$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$

![CYP201](assets/fr/004.webp)

Kwa uhalisia, ni kihisabati kuepukika kwamba migongano ipo kwa kazi za Hash, kwa sababu saizi ya pembejeo inaweza kuwa kubwa kuliko saizi ya matokeo. Hii inajulikana kama kanuni ya droo ya Dirichlet: ikiwa vitu $n$ vitasambazwa katika droo za $m$, na $m <n$, basi angalau droo moja itakuwa na vitu viwili au zaidi. Kwa chaguo za kukokotoa za Hash, kanuni hii inatumika kwa sababu idadi ya ujumbe unaowezekana (karibu) haina kikomo, ilhali idadi ya heshi zinazowezekana ni kikomo ($2^{256}$ katika kesi ya SHA256).

Kwa hivyo, sifa hii haimaanishi kuwa hakuna migongano ya kazi za Hash, lakini badala yake kwamba utendaji mzuri wa Hash hufanya uwezekano wa kupata mgongano kuwa mdogo. Tabia hii, kwa mfano, haijathibitishwa tena kwenye algoriti za SHA-0 na SHA-1, watangulizi wa SHA-2, ambao migongano imepatikana. Majukumu haya kwa hivyo sasa yanashauriwa dhidi ya na mara nyingi huchukuliwa kuwa ya kizamani.

Kwa utendaji wa Hash wa biti $n$, upinzani wa mgongano ni wa mpangilio wa $2^{\frac{n}{2}}$, kwa mujibu wa shambulio la siku ya kuzaliwa. Kwa mfano, kwa SHA256 ($n = 256$), utata wa kupata mgongano ni wa mpangilio wa $2^{128}$ majaribio. Kwa vitendo, hii inamaanisha kwamba ikiwa mtu atapitisha $2^{128}$ ujumbe tofauti kupitia chaguo za kukokotoa, kuna uwezekano wa kupata mgongano.

#### 4. Upinzani kwa Preimage ya Pili

Upinzani kwa preimage ya pili ni sifa nyingine muhimu ya kazi za Hash. Inasema kwamba kutokana na ujumbe $m_1$ na Hash $h$ yake, haiwezekani kupata ujumbe mwingine $m_2 \neq m_1$ kama vile:

$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$

Kwa hivyo, upinzani dhidi ya taswira ya pili ni sawa na upinzani wa mgongano, isipokuwa hapa, shambulio ni gumu zaidi kwa sababu mshambuliaji hawezi kuchagua $m_1$ kwa uhuru.

![CYP201](assets/fr/005.webp)

### Maombi ya Kazi za Hash katika Bitcoin

Chaguo za kukokotoa za Hash zinazotumika zaidi katika Bitcoin ni **SHA256** ("_Secure Hash Algorithm 256 bits"_). Iliyoundwa mwanzoni mwa miaka ya 2000 na NSA na kusawazishwa na NIST, inazalisha pato la 256-bit Hash.

Kitendaji hiki Kina (depth)tumika katika vipengele vingi vya Bitcoin. Katika ngazi ya itifaki, inahusika katika utaratibu wa Proof-of-Work, ambapo hutumiwa kwa hashing mara mbili ili kutafuta mgongano wa sehemu kati ya kichwa cha kizuizi cha mgombea, kilichoundwa na Miner, na lengo la ugumu. Ikiwa mgongano huu wa sehemu utapatikana, kizuizi cha mgombea Kina (depth)kuwa halali na Kina (depth)weza kuongezwa kwa Blockchain.

SHA256 pia inatumika katika ujenzi wa Merkle Tree, ambayo ni kikusanyiko Kina (depth)chotumika kurekodi shughuli kwenye vitalu. Muundo huu pia unapatikana katika itifaki ya Utreexo, ambayo inaruhusu kupunguza ukubwa wa UTXO Set. Zaidi ya hayo, kwa kuanzishwa kwa Taproot mwaka wa 2021, SHA256 inatumiwa katika MAST (_Merkelised Alternative Script Tree_), ambayo inaruhusu kufichua tu masharti ya matumizi yanayotumika katika hati, bila kufichua chaguo zingine zinazowezekana. Pia hutumiwa katika hesabu ya vitambulisho vya shughuli, katika uhamisho wa pakiti juu ya mtandao wa P2P, katika saini za elektroniki ... Hatimaye, na hii ni ya riba hasa katika mafunzo haya, SHA256 hutumiwa katika ngazi ya maombi kwa ajili ya ujenzi wa pochi za Bitcoin na derivation ya anwani.

Mara nyingi, unapokutana na matumizi ya SHA256 kwenye Bitcoin, kwa kweli itakuwa Hash SHA256 mara mbili, iliyobainishwa "**HASH256**", ambayo inajumuisha kutumia SHA256 mara mbili mfululizo:

$$
\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))
$$

Zoezi hili la hashing mara mbili huongeza Layer ya ziada ya usalama dhidi ya mashambulizi fulani yanayoweza kutokea, ingawa SHA256 moja leo inachukuliwa kuwa salama kwa njia fiche.

Kitendaji kingine cha hashi Kina (depth)chopatikana katika lugha ya Hati na Kina (depth)chotumiwa kupata anwani za kupokea ni chaguo la kukokotoa la RIPEMD160. Chaguo hili la kukokotoa hutoa 160-bit Hash (hivyo ni fupi kuliko SHA256). Kwa ujumla huunganishwa na SHA256 kuunda kitendakazi cha HASH160:

$$
\text{HASH160}(m) = \text{RIPEMD160}(\text{SHA256}(m))
$$

Mchanganyiko huu hutumiwa kwa generate heshi fupi, haswa katika kuunda anwani fulani za Bitcoin ambazo zinawakilisha heshi za funguo au heshi za hati, na pia kutoa alama za vidole muhimu.

Hatimaye, katika kiwango cha maombi tu, kazi ya SHA512 wakati mwingine hutumiwa pia, ambayo ina jukumu la moja kwa moja katika utoaji wa Ufunguo (Key) wa pochi. Kazi hii inafanana sana na SHA256 katika uendeshaji wake; zote mbili ni za familia moja ya SHA2, lakini SHA512 inazalisha, kama jina lake linavyoonyesha, Hash ya 512-bit, ikilinganishwa na bits 256 za SHA256. Tutaelezea kwa undani matumizi yake katika sura zifuatazo.

Sasa unajua misingi muhimu kuhusu utendaji wa hashing kwa yale yafuatayo. Katika sura inayofuata, ninapendekeza kugundua kwa undani zaidi utendakazi wa kazi ambayo iko katikati ya Bitcoin: SHA256. Tutaichambua ili kuelewa jinsi inavyofanikisha sifa tulizozielezea hapa. Sura hii inayofuata ni ndefu na ya kiufundi, lakini si muhimu kufuata mafunzo mengine. Kwa hiyo, ikiwa una ugumu kuelewa, usijali na uende moja kwa moja kwenye sura inayofuata, ambayo itakuwa rahisi zaidi kupatikana.

## Kazi za Ndani za SHA256

<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>

Tumeona hapo awali kuwa vitendaji vya hashing vina sifa muhimu zinazohalalisha matumizi yao kwenye Bitcoin. Wacha sasa tuchunguze mifumo ya ndani ya kazi hizi za hashing ambazo huwapa mali hizi, na kwa kufanya hivyo, napendekeza kutenganisha operesheni ya SHA256.

Vitendaji vya SHA256 na SHA512 ni vya familia moja ya SHA2. Utaratibu wao unategemea ujenzi maalum unaoitwa **Merkle-Damgård ujenzi**. RIPEMD160 pia hutumia aina hii ya ujenzi.

Kama ukumbusho, tuna ujumbe wa ukubwa usio na mpangilio kama ingizo kwa SHA256, na tutaupitisha kwenye chaguo la kukokotoa ili kupata 256-bit Hash kama pato.

### Usindikaji wa awali wa pembejeo

Ili kuanza, tunahitaji kutayarisha ujumbe wetu wa ingizo $m$ ili uwe na urefu wa kawaida ambao ni mgawo wa biti 512. Hatua hii ni muhimu kwa utendaji mzuri wa algorithm baadaye.

Ili kufanya hivyo, tunaanza na hatua ya bits ya padding. Kwanza tunaongeza kitenganishi `1` kwenye ujumbe, ikifuatiwa na idadi fulani ya biti `0`. Nambari ya biti `0` zilizoongezwa huhesabiwa ili jumla ya urefu wa ujumbe baada ya nyongeza hii ilingane na modulo 448 512. Kwa hivyo, urefu wa $L$ wa ujumbe wenye vibandiko vya pedi ni sawa na:

$$
L \equiv 448 \mod 512
$$

$\text{mod}$, kwa modulo, ni operesheni ya hisabati ambayo, kati ya nambari mbili kamili, hurejesha salio la mgawanyiko wa Euclidean wa kwanza na wa pili. Kwa mfano: $16 \mod 5 = 1$. Ni operesheni inayotumika sana katika kriptografia.

Hapa, hatua ya padding inahakikisha kwamba, baada ya kuongeza bits 64 katika hatua inayofuata, urefu wa jumla wa ujumbe uliosawazishwa utakuwa nyingi ya 512 bits. Ikiwa ujumbe wa awali una urefu wa biti za $M$, nambari ($N$) ya biti `0` za kuongezwa ni hivi:

$$
N = (448 - (M + 1) \mod 512) \mod 512
$$

Kwa mfano, ikiwa ujumbe wa awali ni biti 950, hesabu itakuwa kama ifuatavyo.

$$
\begin{align*}
M & = 950 \\
M + 1 & = 951 \\
(M + 1) \mod 512 & = 951 \mod 512 \\
& = 951 - 512 \cdot \left\lfloor \frac{951}{512} \right\rfloor \\
& = 951 - 512 \cdot 1 \\
& = 951 - 512 \\
& = 439 \\
\\
448 - (M + 1) \mod 512 & = 448 - 439 \\
& = 9 \\
\\
N & = (448 - (M + 1) \mod 512) \mod 512 \\
N & = 9 \mod 512 \\
& = 9
\end{align*}
$$

Kwa hivyo, tungekuwa na `0` 9 pamoja na kitenganishi `1`. Sehemu zetu za kuweka pedi zitaongezwa moja kwa moja baada ya ujumbe wetu $M$ itakuwa:

```text
1000 0000 00
```

Baada ya kuongeza vipande kwenye ujumbe wetu $M$, pia tunaongeza uwakilishi wa biti 64 wa urefu asili wa ujumbe $M$, unaoonyeshwa kwa njia ya jozi. Hii inaruhusu kazi ya Hash kuwa nyeti kwa mpangilio wa biti na urefu wa ujumbe.

Tukirudi kwenye mfano wetu na ujumbe wa awali wa biti 950, tunabadilisha nambari ya desimali `950` hadi mfumo wa jozi, ambayo inatupa `1110 1101 10`. Tunakamilisha nambari hii kwa sufuri kwenye msingi ili kufanya jumla ya biti 64. Katika mfano wetu, hii inatoa:

```text
0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0011 1011 0110
```

Saizi hii ya pedi huongezwa kufuatia pedi kidogo. Kwa hivyo, ujumbe baada ya usindikaji wetu una sehemu tatu:


- Ujumbe asili $M$;
- `1` kidogo ikifuatiwa na biti kadhaa `0` ili kuunda pedi;
- Uwakilishi wa biti 64 wa urefu wa $M$ ili kuunda pedi yenye ukubwa.

![CYP201](assets/fr/006.webp)

### Uanzishaji wa Vigezo

SHA256 hutumia viasili nane vya hali ya awali, vinavyoashiria $A$ hadi $H$, kila moja ya biti 32. Vigezo hivi huanzishwa kwa viambatisho maalum, ambavyo ni sehemu za sehemu za mizizi ya mraba ya nambari kuu nane za kwanza. Tutatumia maadili haya baadaye wakati wa mchakato wa hashing:


- $A = 0x6a09e667$
- $B = 0xbb67ae85$
- $C = 0x3c6ef372$
- $D = 0xa54ff53a$
- $E = 0x510e527f$
- $F = 0x9b05688c$
- $G = 0x1f83d9ab$
- $H = 0x5be0cd19$

SHA256 pia hutumia viasili vingine 64, vinavyoashiria $K_0$ hadi $K_{63}$, ambavyo ni sehemu za sehemu za mizizi ya mchemraba wa nambari kuu 64 za kwanza:

$$
K[0 \ldots 63] = \begin{pmatrix}
0x428a2f98, & 0x71374491, & 0xb5c0fbcf, & 0xe9b5dba5, \\
0x3956c25b, & 0x59f111f1, & 0x923f82a4, & 0xab1c5ed5, \\
0xd807aa98, & 0x12835b01, & 0x243185be, & 0x550c7dc3, \\
0x72be5d74, & 0x80deb1fe, & 0x9bdc06a7, & 0xc19bf174, \\
0xe49b69c1, & 0xefbe4786, & 0x0fc19dc6, & 0x240ca1cc, \\
0x2de92c6f, & 0x4a7484aa, & 0x5cb0a9dc, & 0x76f988da, \\
0x983e5152, & 0xa831c66d, & 0xb00327c8, & 0xbf597fc7, \\
0xc6e00bf3, & 0xd5a79147, & 0x06ca6351, & 0x14292967, \\
0x27b70a85, & 0x2e1b2138, & 0x4d2c6dfc, & 0x53380d13, \\
0x650a7354, & 0x766a0abb, & 0x81c2c92e, & 0x92722c85, \\
0xa2bfe8a1, & 0xa81a664b, & 0xc24b8b70, & 0xc76c51a3, \\
0xd192e819, & 0xd6990624, & 0xf40e3585, & 0x106aa070, \\
0x19a4c116, & 0x1e376c08, & 0x2748774c, & 0x34b0bcb5, \\
0x391c0cb3, & 0x4ed8aa4a, & 0x5b9cca4f, & 0x682e6ff3, \\
0x748f82ee, & 0x78a5636f, & 0x84c87814, & 0x8cc70208, \\
0x90befffa, & 0xa4506ceb, & 0xbef9a3f7, & 0xc67178f2
\end{pmatrix}
$$

### Mgawanyiko wa Pembejeo

Sasa kwa kuwa tuna pembejeo iliyosawazishwa, sasa tutaendelea hadi awamu kuu ya usindikaji ya algorithi ya SHA256: kazi ya kukandamiza. Hatua hii ni muhimu sana, kwani ndiyo hasa inayoipa kazi ya Hash sifa zake za kriptografia ambazo tulijifunza katika sura iliyopita.

Kwanza, tunaanza kwa kugawanya ujumbe wetu uliosawazishwa (matokeo ya hatua za uchakataji) katika vitalu kadhaa vya $P$ vya biti 512 kila kimoja. Ikiwa ujumbe wetu uliosawazishwa una ukubwa wa jumla wa bits $n \mara 512$, kwa hivyo tutakuwa na vizuizi $n$, kila moja ya bits 512. Kila kitalu cha 512-bit kitachakatwa kibinafsi na kazi ya ukandamizaji, ambayo inajumuisha raundi 64 za shughuli zinazofuatana. Hebu tutaje vitalu hivi $P_1$, $P_2$, $P_3$...

### Uendeshaji wa Kimantiki

Kabla ya kuchunguza kazi ya ukandamizaji kwa undani, ni muhimu kuelewa shughuli za msingi za mantiki zinazotumiwa ndani yake. Operesheni hizi, kulingana na algebra ya Boolean, hufanya kazi katika kiwango kidogo. Shughuli za msingi za kimantiki zinazotumiwa ni:


- **Kiunganishi (NA)**: iliyoashiria $\land$, inalingana na "AND" ya kimantiki.
- **Kitenganisho (AU)**: iliyoashiria $\lor$, inalingana na "OR" ya kimantiki.
- **Kukanusha (SIO)**: iliyoashiria $\lnot$, inalingana na "NOT" ya kimantiki.

Kutoka kwa shughuli hizi za kimsingi, tunaweza kufafanua utendakazi changamano zaidi, kama vile "Exclusive AU" (XOR) inayoashiria $\oplus$, ambayo hutumiwa sana katika cryptography.

Kila operesheni ya kimantiki inaweza kuwakilishwa na jedwali la ukweli, ambalo linaonyesha matokeo ya michanganyiko yote inayowezekana ya maadili ya pembejeo ya binary (endeshaji mbili $p$ na $q$).

Kwa XOR ($\plus$):

| $p$ | $q$ | $p \plus q$ |

| --- | --- | ------------ |

| 0 | 0 | 0 |

| 0 | 1 | 1 |

| 1 | 0 | 1 |

| 1 | 1 | 0 |

Kwa NA ($\land$):

| $p$ | $q$ | $p \nchi q$ |

| --- | --- | ----------- |

| 0 | 0 | 0 |

| 0 | 1 | 0 |

| 1 | 0 | 0 |

| 1 | 1 | 1 |

Kwa NOT ($\lnot p$):

| $p$ | $\lsio p$ |

| --- | --------- |

| 0 | 1 |

| 1 | 0 |

Wacha tuchukue mfano kuelewa utendakazi wa XOR kwa kiwango kidogo. Ikiwa tunayo nambari mbili za binary kwenye bits 6:


- $a = 101100$
- $ b = 001000$

Kisha:

$$
a \oplus b = 101100 \oplus 001000 = 100100
$$

Kwa kutumia XOR kidogo kidogo:

| Nafasi kidogo | $a$ | $b$ | $a \plus b$ |

| ------------ | --- | --- | ------------ |

| 1 | 1 | 0 | 1 |

| 2 | 0 | 0 | 0 |

| 3 | 1 | 1 | 0 |

| 4 | 1 | 0 | 1 |

| 5 | 0 | 0 | 0 |

| 6 | 0 | 0 | 0 |

Matokeo yake ni $100100$.

Mbali na utendakazi wa kimantiki, kazi ya ukandamizaji hutumia shughuli za kubadilisha kidogo, ambazo zitachukua jukumu muhimu katika uenezaji wa bits kwenye algorith.

Kwanza, kuna operesheni ya kimantiki ya zamu ya kulia, inayoashiria $ShR_n(x)$, ambayo huhamisha bits zote za $x$ kulia kwa nafasi $n$, na kujaza bits zilizo wazi upande wa kushoto na sufuri.

Kwa mfano, kwa $x = 101100001$ (kwenye biti 9) na $n = 4$:

$$
ShR_4(101100001) = 000010110
$$

Kwa utaratibu, operesheni sahihi ya mabadiliko inaweza kuonekana kama hii:

![CYP201](assets/fr/007.webp)

Operesheni nyingine inayotumika katika SHA256 kwa upotoshaji kidogo ni mzunguko wa kulia wa duara, unaoashiria $RotR_n(x)$, ambao huhamisha bits za $x$ kwenda kulia kwa nafasi $n$, na kuingiza tena biti zilizohamishwa mwanzoni mwa mfuatano.

Kwa mfano, kwa $x = 101100001$ (zaidi ya biti 9) na $n = 4$:

$$
RotR_4(101100001) = 000110110
$$

Kwa utaratibu, operesheni sahihi ya kuhama kwa mviringo inaweza kuonekana kama hii:

![CYP201](assets/fr/008.webp)

### Kazi ya Ukandamizaji

Sasa kwa kuwa tumeelewa shughuli za kimsingi, hebu tuchunguze kazi ya ukandamizaji ya SHA256 kwa undani.

Katika hatua ya awali, tuligawanya pembejeo yetu katika vipande kadhaa vya 512-bit $P $. Kwa kila block ya 512-bit $P$, tuna:


- **Maneno ya ujumbe $W_i$**: kwa $i$ kutoka 0 hadi 63.
- **Viunga $K_i$**: kwa $i$ kutoka 0 hadi 63, vilivyofafanuliwa katika hatua ya awali.
- **Vigezo vya hali $A, B, C, D, E, F, G, H$**: vilivyoanzishwa kwa thamani kutoka kwa hatua ya awali.

Maneno 16 ya kwanza, $W_0$ hadi $W_{15}$, yametolewa moja kwa moja kutoka kwa kitalu cha bitd 512 $P$ kilichochakatwa. Kila neno $W_i$ linajumuisha biti 32 mfululizo kutoka kwenye kitalu. Kwa hivyo, kwa mfano, tunachukua sehemu yetu ya kwanza ya ingizo $P_1$, na tunaigawanya zaidi katika vipande vidogo-32 ambavyo tunaviita maneno.

Maneno 48 yanayofuata ($W_{16}$ hadi $W_{63}$) yanatolewa kwa kutumia fomula ifuatayo:

$$
W_i = W_{i-16} + \sigma_0(W_{i-15}) + W_{i-7} + \sigma_1(W_{i-2}) \mod 2^{32}
$$

Na:


- $\sigma_0(x) = RotR_7(x) \plus RotR_{18}(x) \plus ShR_3(x)$
- $\sigma_1(x) = RotR_{17}(x) \plus RotR_{19}(x) \plus ShR_{10}(x)$

Katika hali hii, $x$ ni sawa na $W_{i-15}$ kwa $\sigma_0(x)$ na $W_{i-2}$ kwa $\sigma_1(x)$.

Baada ya kuamua maneno yote $W_i$ kwa kipande chetu cha 512-bit, tunaweza kuendelea na kitendakazi cha kubana, ambacho Kina (depth)jumuisha kufanya mizunguko 64.

![CYP201](assets/fr/009.webp)

Kwa kila mzunguko $i$ kutoka 0 hadi 63, tuna aina tatu tofauti za pembejeo. Kwanza, $W_i$ ambayo tumebaini hivi punde, ikiwa ni pamoja na kipande cha ujumbe wetu $P_n$. Ifuatayo, viunga 64 $K_i$. Hatimaye, tunatumia viasili vya hali $A$, $B$, $C$, $D$, $E$, $F$, $G$, na $H$, ambavyo vitabadilika katika mchakato wa hashing na kurekebishwa kwa kila kitendakazi cha kubana. Hata hivyo, kwa kipande cha kwanza $P_1$, tunatumia viasili vya mwanzo vilivyotolewa hapo awali.

Kisha tunafanya shughuli zifuatazo kwenye pembejeo zetu:


- **Kazi $\Sigma_0$:**

$$
\Sigma_0(A) = RotR_2(A) \oplus RotR_{13}(A) \oplus RotR_{22}(A)
$$


- **Kazi $\Sigma_1$:**

$$
\Sigma_1(E) = RotR_6(E) \oplus RotR_{11}(E) \oplus RotR_{25}(E)
$$


- Chaguo za kukokotoa $Ch$ ("_Choose_"):**

$$
Ch(E, F, G) = (E \land F) \oplus (\lnot E \land G)
$$


- Kazi $Maj$ ("_Majority_"):**

$$
Maj(A, B, C) = (A \land B) \oplus (A \land C) \oplus (B \land C)
$$

Kisha tunahesabu vigezo 2 vya muda:


- $ temp1$:

$$
temp1 = H + \Sigma_1(E) + Ch(E, F, G) + K_i + W_i \mod 2^{32}
$$


- $ temp2$:

$$
temp2 = \Sigma_0(A) + Maj(A, B, C) \mod 2^{32}
$$

Ifuatayo, tunasasisha anuwai za state kama ifuatavyo:

$$
\begin{cases}
H = G \\
G = F \\
F = E \\
E = D + temp1 \mod 2^{32} \\
D = C \\
C = B \\
B = A \\
A = temp1 + temp2 \mod 2^{32}
\end{cases}
$$

Mchoro ufuatao unawakilisha duru ya kazi ya ukandamizaji ya SHA256 kama tulivyoelezea hivi punde:

![CYP201](assets/fr/010.webp)


- Mishale inaonyesha mtiririko wa data;
- Sanduku zinawakilisha shughuli zilizofanywa;
- $+$ iliyozungushwa inawakilisha moduli ya nyongeza $2^{32}$.

Tayari tunaweza kuona kwamba raundi hii inatoa hali mpya za hali $A$, $B$, $C$, $D$, $E$, $F$, $G$, na $H$. Vigezo hivi vipya vitatumika kama ingizo la raundi inayofuata, ambayo nayo itazalisha vigeu vipya $A$, $B$, $C$, $D$, $E$, $F$, $G$, na $H$, zitakazotumika kwa raundi ifuatayo. Mchakato huu unaendelea hadi raundi ya 64.

Baada ya raundi 64, tunasasisha maadili ya awali ya vigezo vya state kwa kuziongeza kwa maadili ya mwisho mwishoni mwa raundi ya 64:

$$
\begin{cases}
A = A_{\text{initial}} + A \mod 2^{32} \\
B = B_{\text{initial}} + B \mod 2^{32} \\
C = C_{\text{initial}} + C \mod 2^{32} \\
D = D_{\text{initial}} + D \mod 2^{32} \\
E = E_{\text{initial}} + E \mod 2^{32} \\
F = F_{\text{initial}} + F \mod 2^{32} \\
G = G_{\text{initial}} + G \mod 2^{32} \\
H = H_{\text{initial}} + H \mod 2^{32}
\end{cases}
$$

Nambari hizi mpya za $A$, $B$, $C$, $D$, $E$, $F$, $G$, na $H$ zitatumika kama nambari za mwanzo za block inayofuata, $P_2$. Kwa kitalu hiki $P_2$, tunaiga mchakato sawa wa mbano kwa miduara 64, kisha tunasasisha vigeu vya kitalu $P_3$, na kadhalika hadi kitalu cha mwisho cha ingizo letu lililosawazishwa.

Baada ya kuchakata vizuizi vyote vya ujumbe, tunaambatanisha thamani za mwisho za vibadala $A$, $B$, $C$, $D$, $E$, $F$, $G$, na $H$ ili kuunda mwisho wa 256-bit Hash ya utendaji wetu wa hashing:

$$
\text{Hash} = A \Vert B \Vert C \Vert D \Vert E \Vert F \Vert G \Vert H
$$

Kila kigezo ni nambari kamili ya biti 32, kwa hivyo muunganisho wao daima hutoa matokeo ya biti 256, bila kujali ukubwa wa ingizo letu la ujumbe kwenye kipengele cha kukokotoa cha kuheshi.

### Uthibitishaji wa Sifa za Cryptographic

Lakini basi, ni jinsi gani kitendakazi hiki hakiwezi kutenduliwa, Kina (depth)chostahimili mgongano, na sugu ya tamper?

Kwa upinzani wa tamper, ni rahisi kuelewa. Kuna mahesabu mengi yanayofanywa kwa kuteleza, ambayo hutegemea pembejeo na viunga, kwamba urekebishaji mdogo wa ujumbe wa awali hubadilisha kabisa njia iliyochukuliwa, na hivyo hubadilisha kabisa pato la Hash. Hii ndio inaitwa athari ya avalanche. Mali hii inahakikishwa kwa mchanganyiko wa majimbo ya kati na majimbo ya awali kwa kila kipande.

Ifuatayo, wakati wa kujadili kazi ya kriptografia ya Hash, neno "kutoweza kutenduliwa" halitumiwi kwa ujumla. Badala yake, tunazungumza juu ya "upinzani wa picha," ambayo inabainisha kuwa kwa $y$ yoyote, ni vigumu kupata $x$ vile $h(x) = y$. Upinzani huu wa hakikisho unahakikishwa na ugumu wa algebraic na kutokuwa na usawa kwa nguvu ya shughuli zinazofanywa katika kazi ya ukandamizaji, na pia kwa kupoteza habari fulani katika mchakato. Kwa mfano, kwa matokeo fulani ya modulo ya kuongeza, kuna operesheni kadhaa zinazowezekana:

$$
3+2 \mod 10 = 5 \\
7+8 \mod 10 = 5 \\
5+10 \mod 10 = 5
$$

Katika mfano huu, kujua tu modulo iliyotumiwa (10) na matokeo (5), mtu hawezi kuamua kwa hakika ambayo ni operesheni sahihi zinazotumiwa katika nyongeza. Inasemekana kuwa kuna miunganisho mingi modulo 10.

Kwa operesheni ya XOR, tunakabiliwa na shida sawa. Kumbuka jedwali la ukweli kwa operesheni hii: matokeo yoyote ya 1-bit yanaweza kuamuliwa na usanidi mbili tofauti wa ingizo ambao una uwezekano sawa wa kuwa maadili sahihi. Kwa hiyo, mtu hawezi kuamua kwa hakika uendeshaji wa XOR kwa kujua tu matokeo yake. Ikiwa tunaongeza ukubwa wa uendeshaji wa XOR, idadi ya pembejeo zinazowezekana kujua tu matokeo huongezeka kwa kasi. Zaidi ya hayo, XOR hutumiwa mara nyingi pamoja na shughuli nyingine za kiwango kidogo, kama vile uendeshaji wa $\text{RotR}$, ambao huongeza tafsiri zinazowezekana zaidi kwa matokeo.

Kitendakazi cha kubana pia hutumia utendakazi wa $\text{ShR}$. Uendeshaji huu huondoa sehemu ya maelezo ya msingi, ambayo basi haiwezekani kurejesha baadaye. Kwa mara nyingine tena, hakuna njia za aljebra za kubadilisha operesheni hii. Operesheni hizi zote za njia moja na upotezaji wa habari hutumiwa mara nyingi sana katika vitendaji vya ukandamizaji. Idadi ya ingizo zinazowezekana kwa matokeo fulani ni karibu kutokuwa na kikomo, na kila jaribio la kukokotoa kinyume kungesababisha milinganyo yenye idadi kubwa sana ya zisizojulikana, ambazo zingeongezeka kwa kasi katika kila hatua.

Hatimaye, kwa sifa ya upinzani wa mgongano, vigezo kadhaa vinahusika. Uchakataji wa awali wa ujumbe asili una jukumu muhimu. Bila uchakataji huu wa awali, inaweza kuwa rahisi kupata migongano kwenye chaguo la kukokotoa. Ingawa, Kina (depth)dharia, migongano ipo (kutokana na kanuni ya njiwa), muundo wa kazi ya Hash, pamoja na mali zilizotajwa hapo juu, hufanya uwezekano wa kupata mgongano chini sana.

Ili kitendakazi cha Hash kiwe sugu kwa mgongano, ni muhimu kwamba:


- Matokeo hayatabiriki: Utabiri wowote unaweza kutumiwa kupata migongano kwa haraka kuliko kwa shambulio la nguvu. Chaguo za kukokotoa huhakikisha kwamba kila sehemu ya matokeo inategemea kwa njia isiyo ya kawaida kwenye ingizo. Kwa maneno mengine, chaguo la kukokotoa limeundwa ili kila sehemu ya matokeo ya mwisho iwe na uwezekano huru wa kuwa 0 au 1, hata kama uhuru huu sio kamili katika mazoezi.
- Usambazaji wa heshi ni pseudo-random: Hii inahakikisha kwamba heshi zimesambazwa kwa usawa.
- Ukubwa wa Hash ni kubwa: nafasi kubwa iwezekanavyo kwa matokeo, ni vigumu zaidi kupata mgongano.

Vyombo vya habari husanifu vipengele hivi kwa kutathmini mashambulizi bora zaidi ili kupata migongano, kisha kurekebisha vigezo ili kufanya mashambulizi haya kutofaa.

### Ujenzi wa Merkle-Damgård

Muundo wa SHA256 unatokana na ujenzi wa Merkle-Damgård, unaoruhusu kubadilisha kitendakazi cha mgandamizo kuwa kitendakazi cha Hash ambacho Kina (depth)weza kuchakata ujumbe wa urefu wa kiholela. Hivi ndivyo tulivyoona katika sura hii.

Hata hivyo, baadhi ya vipengele vya zamani vya Hash kama vile SHA1 au MD5, vinavyotumia ujenzi huu mahususi, vinaweza kuathiriwa na mashambulizi ya kuongeza urefu. Hii ni mbinu inayomruhusu mshambulizi anayejua Hash ya ujumbe $M$ na urefu wa $M$ (bila kujua ujumbe wenyewe) kukokotoa Hash ya ujumbe $M'$ unaoundwa kwa kuunganisha $M$ na maudhui ya ziada.

SHA256, ingawa inatumia aina sawa ya ujenzi, Kina (depth)dharia ni sugu kwa aina hii ya mashambulizi, tofauti na SHA1 na MD5. Hili linaweza kueleza fumbo la uharakishaji maradufu uliotekelezwa kote Bitcoin na Satoshi Nakamoto. Ili kuzuia shambulio la aina hii, Satoshi inaweza kuwa ilipendelea kutumia SHA256 mbili:

$$
\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))
$$

Hii huongeza usalama dhidi ya mashambulizi yanayoweza kutokea kuhusiana na ujenzi wa Merkle-Damgård, lakini haiongezi usalama wa mchakato wa hashing katika suala la ukinzani wa mgongano. Zaidi ya hayo, hata kama SHA256 ingekuwa katika hatari ya kushambuliwa kwa aina hii, isingekuwa na madhara makubwa, kwani matukio yote ya matumizi ya kazi za Hash katika Bitcoin yanahusisha data ya umma. Hata hivyo, shambulio la kiendelezi cha urefu linaweza tu kuwa na manufaa kwa mvamizi ikiwa data ya hashed ni ya faragha na mtumiaji ametumia chaguo za kukokotoa za Hash kama mbinu ya uthibitishaji wa data hizi, sawa na MAC. Kwa hivyo, utekelezaji wa hashing mara mbili bado ni siri katika muundo wa Bitcoin.

Sasa kwa kuwa tumeangalia kwa Kina (depth) utendakazi wa vitendaji vya Hash, hasa SHA256, ambayo inatumika sana katika Bitcoin, tutazingatia zaidi algoriti za utokaji wa kriptografia zinazotumiwa katika kiwango cha maombi, hasa kwa kupata funguo za Wallet yako.

## Algorithms kutumika kwa ajili ya derivation

<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>

Katika Bitcoin katika kiwango cha maombi, pamoja na kazi za Hash, algorithi ya derivation ya kriptografia hutumiwa kwa data salama ya generate kutoka kwa pembejeo za awali. Ingawa algoriti hizi hutegemea utendakazi wa Hash, hutumikia malengo tofauti, haswa katika suala la uthibitishaji na utengenezaji muhimu. Kanuni hizi huhifadhi baadhi ya sifa za chaguo za kukokotoa za Hash, kama vile kutoweza kutenduliwa, upinzani wa kubadilika na kuhimili mgongano.

Kwenye wallets za Bitcoin, algorithms 2 za derivation hutumiwa:


- HMAC (Msimbo wa Uthibitishaji wa Ujumbe_msingi wa Hash_)**
- PBKDF2 (_Matendo ya Utoaji wa Ufunguo (Key) 2_ kwa Msingi wa Nenosiri 2_)**

Tutachunguza kwa pamoja utendaji na jukumu la kila mmoja wao.

### HMAC-SHA512

HMAC ni algoriti ya kriptografia inayokokotoa msimbo wa uthibitishaji kulingana na mchanganyiko wa chaguo za kukokotoa za Hash na Ufunguo (Key) wa siri. Bitcoin hutumia HMAC-SHA512, kibadala cha HMAC Kina (depth)chotumia chaguo za kukokotoa za SHA512 Hash. Tayari tumeona katika sura iliyopita kwamba SHA512 ni sehemu ya familia sawa ya kazi za Hash kama SHA256, lakini hutoa pato la 512-bit.

Huu hapa ni mpango wake wa uendeshaji wa jumla $m$ ukiwa ujumbe wa ingizo na $K$ Ufunguo (Key) wa siri:

![CYP201](assets/fr/011.webp)

Wacha tujifunze kwa undani zaidi kile Kina (depth)chotokea katika kisanduku hiki cheusi cha HMAC-SHA512. Kazi ya HMAC-SHA512 iliyo na:


- $m$: ujumbe wa ukubwa wa kiholela uliochaguliwa na mtumiaji (ingizo la kwanza);
- $K$: Ufunguo (Key) wa siri wa kiholela uliochaguliwa na mtumiaji (ingizo la pili);
- $K'$: Ufunguo (Key) $K$ uliorekebishwa kwa ukubwa wa $B$ wa vizuizi vya kazi vya Hash (biti 1024 kwa SHA512, au baiti 128);
- $\text{SHA512}$: chaguo za kukokotoa za SHA512 Hash;
- $\oplus$: operesheni ya XOR (ya kipekee au);
- $\Vert$: mwendeshaji wa uunganishaji, akiunganisha mifuatano midogo-mwisho-hadi-mwisho;
- $\text{opad}$: mara kwa mara inajumuisha byte $0x5c$ iliyorudiwa mara 128
- $\text{ipad}$: mara kwa mara inajumuisha byte $0x36$ iliyorudiwa mara 128

Kabla ya kuhesabu HMAC, ni muhimu kusawazisha Ufunguo (Key) na mara kwa mara kulingana na ukubwa wa kitalu $ B $. Kwa mfano, ikiwa Ufunguo (Key) $K$ ni mfupi kuliko baiti 128, huwekwa sufuri kufikia ukubwa wa $B$. Ikiwa $K$ ni ndefu zaidi ya bits 128, inabanwa kwa kutumia SHA512, kisha sufuri huongezwa hadi ifikie baiti 128. Kwa njia hii, Ufunguo (Key) uliosawazishwa unaoitwa $K'$ unapatikana.

Thamani za $\text{opad}$ na $\text{ipad}$ zinapatikana kwa kurudia base byte ($0x5c$ kwa $\text{opad}$, $0x36$ kwa $\text{ipad}$) hadi ukubwa wa $B$ ufikiwe. Kwa hivyo, na $B = 128$ byte, tunayo:

$$
\text{opad} = \underbrace{0x5c5c\ldots5c}\_{128 \, \text{bytes}}
$$

Baada ya usindikaji kukamilika, algoriti ya HMAC-SHA512 inafafanuliwa na mlinganyo ufuatao:

$$
\text {HMAC-SHA512}\_K(m) = \text{SHA512} \left( (K' \oplus \text{opad}) \parallel \text{SHA512} \left( (K' \oplus \text{ipad}) \parallel m \right) \right)
$$

Equation hii imegawanywa katika hatua zifuatazo:


- XOR Ufunguo (Key) uliorekebishwa $K'$ na $\text{ipad}$ ili kupata $\text{iKpad}$;
- XOR Ufunguo (Key) uliorekebishwa $K'$ na $\text{opad}$ ili kupata $\text{oKpad}$;
- Unganisha $\text{iKpad}$ na ujumbe $m$.
- Hash tokeo hili na SHA512 ili kupata Hash $H_1$ ya kati.
- Unganisha $\text{oKpad}$ na $H_1$.
- Hash tokeo hili na SHA512 kupata matokeo ya mwisho $H_2$.

Hatua hizi zinaweza kufupishwa kwa mpangilio kama ifuatavyo:

![CYP201](assets/fr/012.webp)

HMAC inatumika katika Bitcoin haswa kwa utokezi muhimu katika pochi za HD (Hierarchical Deterministic) (tutazungumza juu ya hili kwa undani zaidi katika sura zinazokuja) na kama sehemu ya PBKDF2.

### PBKDF2

PBKDF2 (_Kazi 2_ ya Upataji Muhimu kwa Msingi wa Nenosiri) ni kanuni kuu ya utohozi iliyoundwa ili kuimarisha usalama wa manenosiri. Algorithm inatumika kazi ya pseudo-random (hapa HMAC-SHA512) kwenye nenosiri na chumvi ya siri, na kisha kurudia operesheni hii mara kadhaa ili kuzalisha Ufunguo (Key) wa pato.

Katika Bitcoin, PBKDF2 inatumika kwa kuzalisha seed ya HD Wallet kutoka kwa maneno ya Mnemonic na passphrase (lakini tutazungumzia kuhusu hili kwa undani zaidi katika sura zijazo).

Mchakato wa PBKDF2 ni kama ifuatavyo, na:


- $m$: Kifungu cha kumbukumbu Mnemonic;
- $s$: passphrase (Funguo la siri) ya hiari ili kuongeza usalama (uga tupu ikiwa hakuna passphrase);
- $n$: idadi ya marudio ya chaguo la kukokotoa, kwa upande wetu, ni 2048.

Chaguo za kukokotoa za PBKDF2 hufafanuliwa mara kwa mara. Kila marudio huchukua matokeo ya ya awali, huipitisha kupitia HMAC-SHA512, na kuchanganya matokeo yanayofuatana ili kutoa Ufunguo (Key) wa mwisho:

$$
\text{PBKDF2}(m, s) = \text{HMAC-SHA512}^{2048}(m, s)
$$

Kwa utaratibu, PBKDF2 inaweza kuwakilishwa kama ifuatavyo:

![CYP201](assets/fr/013.webp)

Katika sura hii, tumechunguza chaguo za kukokotoa za HMAC-SHA512 na PBKDF2, ambazo hutumia kipengele cha kukokotoa ili kuhakikisha uadilifu na usalama wa vitu muhimu katika itifaki ya Bitcoin. Katika sehemu inayofuata, tutaangalia saini za dijiti, njia nyingine ya kriptografia inayotumiwa sana katika Bitcoin.

# Sahihi za Dijitali

<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>

## Sahihi za Dijiti na Mikunjo ya Mviringo

<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>

Njia ya pili ya kriptografia inayotumiwa katika Bitcoin inahusisha kanuni za saini za dijiti. Wacha tuchunguze hii inahusu nini na jinsi inavyofanya kazi.

### Bitcoins, UTXOs, na Masharti ya Matumizi

Neno "_wallet_" katika Bitcoin linaweza kuwachanganya wanaoanza. Hakika, kile Kina (depth)choitwa Bitcoin Wallet ni programu ambayo haishikilii bitcoins zako moja kwa moja, tofauti na Wallet ya kimwili ambayo inaweza kushikilia sarafu au bili. Bitcoins ni vitengo vya Akaunti (Account) tu. Kitengo hiki cha Akaunti (Account) Kina (depth)wakilishwa na **UTXO** (_Matokeo ya Muamala Usiotumika_), ambayo ni matokeo ya malipo ambayo hayajatumika. Ikiwa matokeo haya hayatumiwi, inamaanisha ni ya mtumiaji. UTXO ni, kwa njia, vipande vya bitcoins, vya ukubwa wa kutofautiana, mali ya mtumiaji.

Itifaki ya Bitcoin inasambazwa na kufanya kazi bila mamlaka kuu. Kwa hivyo, si kama rekodi za kitamaduni za benki, ambapo euro ambazo ni zako zinahusishwa tu na utambulisho wako wa kibinafsi. Kwenye Bitcoin, UTXO zako ni zako kwa sababu zinalindwa na masharti ya matumizi yaliyobainishwa katika lugha ya Hati. Ili kurahisisha, kuna aina mbili za hati: hati ya kufunga (_scriptPubKey_), ambayo inalinda UTXO, na hati ya kufungua (_scriptSig_), ambayo inaruhusu kufungua UTXO na hivyo kutumia vitengo vya Bitcoin inayowakilisha.

Uendeshaji wa awali wa Bitcoin yenye hati za P2PK unahusisha kutumia Ufunguo (Key) wa umma kufunga fedha, ikibainisha katika _scriptPubKey_ kwamba mtu anayetaka kutumia UTXO hii lazima atoe saini halali na Ufunguo (Key) wa faragha unaolingana na Ufunguo (Key) huu wa umma. Ili kufungua UTXO hii, kwa hivyo ni muhimu kutoa saini halali katika _scriptSig_. Kama majina yao yanavyopendekeza, Ufunguo (Key) wa umma unajulikana kwa wote kwa vile unaonyeshwa kwenye Blockchain, wakati Ufunguo (Key) wa kibinafsi unajulikana tu na mmiliki halali wa fedha.

Hii ni operesheni ya msingi ya Bitcoin, lakini baada ya muda, operesheni hii imekuwa ngumu zaidi. Kwanza, Satoshi pia ilianzisha hati za P2PKH, ambazo hutumia kupokea Address katika _scriptPubKey_, ambayo inawakilisha Hash ya Ufunguo (Key) wa umma. Kisha, mfumo huo ukawa mgumu zaidi na kuwasili kwa SegWit na kisha Taproot. Hata hivyo, kanuni ya jumla inabakia kimsingi sawa: Ufunguo (Key) wa umma au uwakilishi wa Ufunguo (Key) huu hutumiwa kufunga UTXO, na Ufunguo (Key) wa kibinafsi unaofanana unahitajika ili kuzifungua na hivyo kuzitumia.

Kwa hivyo, mtumiaji anayetaka kufanya muamala wa Bitcoin lazima aunde sahihi ya dijiti kwa kutumia Ufunguo (Key) wake wa faragha kwenye shughuli inayohusika. Sahihi inaweza kuthibitishwa na washiriki wengine wa mtandao. Ikiwa ni halali, hii inamaanisha kuwa mtumiaji anayeanzisha muamala ndiye mmiliki wa Ufunguo (Key) wa kibinafsi, na kwa hivyo mmiliki wa bitcoins wanazotaka kutumia. Watumiaji wengine wanaweza kukubali na kueneza muamala.

Kwa hivyo, mtumiaji ambaye anamiliki bitcoins zilizofungwa kwa Ufunguo (Key) wa umma lazima atafute njia ya kuhifadhi kwa usalama kile Kina (depth)choruhusu kufungua fedha zao: Ufunguo (Key) wa kibinafsi. Bitcoin Wallet ni kifaa haswa ambacho kitakuruhusu kuweka funguo zako zote kwa urahisi bila watu wengine kuzifikia. Kwa hivyo ni kama chain ya vitufe kuliko Wallet.

Kiungo cha hisabati kati ya Ufunguo (Key) wa umma na Ufunguo (Key) wa faragha, pamoja na uwezo wa kutia sahihi ili kuthibitisha umiliki wa Ufunguo (Key) wa faragha bila kuufunua, huwezeshwa na algoriti ya sahihi ya dijiti. Katika itifaki ya Bitcoin, algoriti 2 za sahihi zinatumika: **ECDSA** (_Elliptic Curve Digital Signature Algorithm_) na **Mpango wa sahihi wa Schnorr**. ECDSA ni itifaki ya sahihi ya dijiti iliyotumiwa katika Bitcoin tangu mwanzo. Schnorr ni ya hivi majuzi zaidi katika Bitcoin, kama ilianzishwa mnamo Novemba 2021 na sasisho la Taproot.

Algorithms hizi mbili zinafanana kabisa katika mifumo yao. Zote mbili zinatokana na kriptografia ya curve ya elliptical. Tofauti kuu kati ya itifaki hizi mbili iko katika muundo wa saini na baadhi ya sifa maalum za hisabati. Kwa hivyo tutasoma utendakazi wa kanuni hizi, tukianza na za zamani zaidi: ECDSA.

### Mviringo Curve Cryptography

Elliptic Curve Cryptography (ECC) ni seti ya algoriti zinazotumia mkunjo wa duaradufu kwa sifa zake mbalimbali za hisabati na kijiometri kwa madhumuni ya kriptografia. Usalama wa algoriti hizi unategemea ugumu wa tatizo la logarithmu tofauti kwenye mikunjo ya duaradufu. Miindo ya duaradufu hutumiwa haswa kwa ubadilishanaji muhimu, usimbaji fiche usiolinganishwa, au kuunda sahihi za dijitali.

Sifa muhimu ya mikunjo hii ni kwamba zina ulinganifu kwa heshima na mhimili wa x. Kwa hivyo, mstari wowote usio wima unaokata curve katika sehemu mbili tofauti daima utakatiza mkunjo katika hatua ya tatu. Zaidi ya hayo, tanjiti yoyote kwa mkunjo kwenye sehemu isiyo ya umoja itakatiza mkunjo katika hatua nyingine. Tabia hizi zitakuwa muhimu kwa kufafanua shughuli kwenye curve.

Hapa kuna uwakilishi wa curve ya duaradufu juu ya uwanja wa nambari halisi:

![CYP201](assets/fr/014.webp)

Kila curve ya duaradufu inafafanuliwa na equation ya fomu:

$$
y^2 = x^3 + ax + b
$$

### sehemu ya 256k1

Ili kutumia ECDSA au Schnorr, ni lazima mtu achague vigezo vya curve ya duaradufu, yaani, thamani za $a$ na $b$ katika mlingano wa curve. Kuna viwango tofauti vya mikunjo ya duaradufu ambayo inasifika kuwa salama kwa njia fiche. Inayojulikana zaidi ni _secp256r1_ curve, iliyofafanuliwa na kupendekezwa na NIST (_Taasisi ya Kitaifa ya Viwango na Teknolojia_).

Licha ya hayo, Satoshi Nakamoto, mvumbuzi wa Bitcoin, alichagua kutotumia curve hii. Sababu ya chaguo hili haijulikani, lakini wengine wanaamini alipendelea kutafuta njia mbadala kwa sababu vigezo vya curve hii vinaweza kuwa na mlango wa nyuma. Badala yake, itifaki ya Bitcoin hutumia mkunjo wa kawaida wa **_secp256k1_**. Curve hii inafafanuliwa na vigezo $a = 0$ na $b = 7$. Kwa hivyo equation yake ni:

$$
y^2 = x^3 + 7
$$

Uwakilishi wake wa picha juu ya uwanja wa nambari halisi inaonekana kama hii:

![CYP201](assets/fr/015.webp)

Hata hivyo, katika kriptografia, tunafanya kazi na seti zenye kikomo za nambari. Hasa zaidi, tunafanya kazi kwenye sehemu ya mwisho $\mathbb{F}_p$, ambayo ni sehemu ya nambari kamili ya nambari kuu $p$.

**Ufafanuzi**: Nambari kuu ni nambari asilia kubwa kuliko au sawa na 2 ambayo ina vigawanyiko viwili pekee chanya chanya: 1 na yenyewe. Kwa mfano, nambari 7 ni nambari kuu kwani inaweza tu kugawanywa na 1 na 7. Kwa upande mwingine, nambari 8 sio kuu kwa sababu inaweza kugawanywa na 1, 2, 4, na 8.

Katika Bitcoin, nambari kuu $p$ inayotumika kufafanua sehemu ya mwisho ni kubwa sana. Imechaguliwa kwa namna ambayo utaratibu wa shamba (yaani, idadi ya Elements katika $\mathbb{F}_p$) ni kubwa ya kutosha ili kuhakikisha usalama wa cryptographic.

Nambari kuu $p$ iliyotumika ni:

```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```

Katika nukuu ya decimal, hii inalingana na:

$$
p = 2^{256} - 2^{32} - 977
$$

Kwa hivyo, equation ya curve yetu ya mviringo ni kweli:

$$
y^2 \equiv x^3 + 7 \mod p
$$

Ikizingatiwa kuwa mduara huu umefafanuliwa juu ya uga finyu $\mathbb{F}_p$, haufanani tena na mkunjo unaoendelea bali seti tofauti ya pointi. Kwa mfano, hivi ndivyo curve inayotumika katika Bitcoin inavyoonekana kwa $p = 17$ ndogo sana:

![CYP201](assets/fr/016.webp)

Katika mfano huu, nimepunguza kimaKusudi (Purpose) sehemu ya mwisho iwe $p = 17$ kwa sababu za kielimu, lakini ni lazima mtu afikirie kuwa ile inayotumika katika Bitcoin ni kubwa zaidi, karibu $2^{256}$.

Tunatumia sehemu yenye kikomo ya nambari kamili modulo $p$ ili kuhakikisha usahihi wa utendakazi kwenye mkunjo. Hakika, mikunjo ya duaradufu juu ya uwanja wa nambari halisi inakabiliwa na usahihi kutokana na makosa ya kuzungusha wakati wa hesabu za kukokotoa. Ikiwa shughuli nyingi zinafanywa kwenye curve, makosa haya hujilimbikiza na matokeo ya mwisho yanaweza kuwa sahihi au vigumu kuzaliana. Utumiaji wa kipekee wa nambari kamili huhakikisha usahihi kamili wa hesabu na hivyo kuzaliana kwa matokeo.

Hisabati ya mikondo ya duaradufu juu ya sehemu zenye ukomo ni sawa na zile zilizo juu ya uwanja wa nambari halisi, kwa urekebishaji kwamba shughuli zote hufanywa modulo $p$. Ili kurahisisha maelezo, tutaendelea katika sura zifuatazo ili kuelezea dhana kwa kutumia curve iliyofafanuliwa juu ya nambari halisi, huku tukikumbuka kwamba, katika mazoezi, curve inafafanuliwa juu ya uwanja wa mwisho.

Ikiwa ungependa kujifunza zaidi kuhusu misingi ya hisabati ya kriptografia ya kisasa, ninapendekeza pia kushauriana na kozi hii nyingine kwenye Plan ₿ Network:

https://planb.network/courses/d2fd9fc0-d9ed-4a87-9fa3-0fdbb3937e28
## Kuhesabu Ufunguo (Key) wa Umma kutoka kwa Ufunguo (Key) wa Kibinafsi

<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>

Kama inavyoonekana hapo awali, algorithm za sahihi za dijiti kwenye Bitcoin zinatokana na jozi ya funguo za kibinafsi na za umma ambazo zimeunganishwa kihisabati. Hebu tuchunguze pamoja kiungo hiki cha hisabati ni nini na jinsi vinavyozalishwa.

### Ufunguo (Key) wa Kibinafsi

Ufunguo (Key) wa faragha ni nambari ya nasibu au pseudo-nasibu. Kwa upande wa Bitcoin, nambari hii ina ukubwa wa bits 256. Kwa hivyo, idadi ya uwezekano wa Ufunguo (Key) wa faragha wa Bitcoin Kina (depth)dharia ni $2^{256}$.

**Kumbuka**: "Nambari isiyo ya kawaida" ni nambari ambayo ina sifa zinazokaribiana na zile za nambari nasibu lakini inatolewa na kanuni ya kubainisha.

Hata hivyo, kiutendaji, kuna pointi tofauti za $n$ pekee kwenye curve yetu ya duaradufu secp256k1, ambapo $n$ ni mpangilio wa sehemu ya jenereta $G$ ya mkunjo. Tutaona baadaye nambari hii inalingana na nini, lakini kumbuka tu kwamba Ufunguo (Key) halali wa faragha ni nambari kamili kati ya $1$ na $n-1$, tukijua kwamba $n$ ni nambari inayokaribia lakini chini kidogo ya $2^{256}$. Kwa hivyo, kuna baadhi ya nambari za 256-bit ambazo si halali kwa kuwa Ufunguo (Key) wa faragha katika Bitcoin, haswa, nambari zote kati ya $n$ na $2^{256}$. Ikiwa uzalishaji wa nambari nasibu (Ufunguo (Key) wa kibinafsi) utatoa thamani $k$ kiasi kwamba $k \geq n$, inachukuliwa kuwa batili, na thamani mpya ya nasibu lazima itolewe.

Kwa hivyo, idadi ya uwezekano wa Ufunguo (Key) wa faragha wa Bitcoin ni takriban $n$, ambayo ni nambari inayokaribia $1.158 \mara 10^{77}$. Nambari hii ni kubwa sana hivi kwamba ukichagua Ufunguo (Key) wa faragha bila mpangilio, ni vigumu kitakwimu kutua kwenye Ufunguo (Key) wa faragha wa mtumiaji mwingine. Ili kukupa wazo la ukubwa, idadi ya funguo za kibinafsi zinazowezekana kwenye Bitcoin ni za mpangilio wa ukubwa unaokaribiana na ule wa atomi zinazokadiriwa katika ulimwengu unaoonekana.

Kama tutakavyoona katika sura zinazokuja, leo, funguo nyingi za kibinafsi zinazotumiwa kwenye Bitcoin hazitolewi kwa nasibu lakini ni matokeo ya uamuzi kutoka kwa kifungu cha Mnemonic, yenyewe ya bahati nasibu (hii ni kifungu maarufu cha maneno 12 au 24). Maelezo haya hayabadilishi chochote kwa matumizi ya kanuni sahihi kama vile ECDSA, lakini husaidia kuangazia upya umaarufu wetu kwenye Bitcoin.

Kwa muendelezo wa maelezo, Ufunguo (Key) wa faragha utaonyeshwa kwa herufi ndogo $k$.

### Ufunguo (Key) wa Umma

Ufunguo (Key) wa umma ni sehemu kwenye mkunjo wa duaradufu, unaoonyeshwa kwa herufi kubwa $K$, na hukokotwa kutoka kwa Ufunguo (Key) wa faragha $k$. Sehemu hii $K$ inawakilishwa na jozi ya viwianishi $(x, y)$ kwenye mkunjo wa duaradufu, kila kiratibu kikiwa modulo kamili $p$, nambari kuu inayofafanua sehemu ya mwisho $\mathbb{F}_p$.

Kwa mazoezi, Ufunguo (Key) wa umma ambao haujabanwa unawakilishwa na biti 512 (au baiti 64), zinazolingana na nambari mbili za 256-bit ($ x $ na $ y $) zilizowekwa mwisho hadi mwisho. Nambari hizi ni abscissa ($x$) na kuratibu ($y$) ya uhakika wetu kwenye secp256k1. Tukiongeza kiambishi awali, Ufunguo (Key) wa umma una jumla ya biti 520.

Hata hivyo, inawezekana pia kuwakilisha Ufunguo (Key) wa umma katika fomu iliyobanwa kwa kutumia baiti 33 pekee (biti 264) kwa kuweka tu abscissa $x$ ya uhakika wetu kwenye mkunjo na baiti inayoonyesha usawa wa $y$. Hiki ndicho Kina (depth)chojulikana kama Kitufe cha umma (Public Key) kilichobanwa. Nitazungumza zaidi juu ya hili katika sura za mwisho za mafunzo haya. Lakini unachohitaji kukumbuka ni kwamba Ufunguo (Key) wa umma $K$ ni hoja iliyoelezwa na $x$ na $y$.

Ili kukokotoa nukta $K$ inayolingana na Ufunguo (Key) wetu wa umma, tunatumia utendakazi wa kuzidisha koleo kwenye mikondo ya duaradufu, inayofafanuliwa kama nyongeza inayorudiwa (mara $k$) ya sehemu ya jenereta $G$:

$$
K = k \cdot G
$$

wapi:


- $k$ ni Ufunguo (Key) wa faragha (nambari kamili kati ya $1$ na $n-1$);
- $G$ ni sehemu ya jenereta ya curve ya mviringo inayotumiwa na washiriki wote wa mtandao wa Bitcoin;
- $\cdot$ inawakilisha kuzidisha kwa koleo kwenye ukingo wa duaradufu, ambayo ni sawa na kuongeza nukta $G$ yenyewe mara $k$.

Ukweli kwamba hatua hii $G$ ni ya kawaida kwa funguo zote za umma kwenye Bitcoin huturuhusu kuwa na uhakika kwamba Ufunguo (Key) sawa wa faragha $k$ utatupatia kila mara Ufunguo (Key) sawa wa umma $K$:

![CYP201](assets/fr/017.webp)

Tabia kuu ya operesheni hii ni kwamba ni kazi ya njia moja. Ni rahisi kukokotoa Ufunguo (Key) wa umma $K$ ukijua Ufunguo (Key) wa faragha $k$ na nukta ya jenereta $G$, lakini kwa kweli haiwezekani kukokotoa Ufunguo (Key) wa faragha $k$ ukijua tu Ufunguo (Key) wa umma $K$ na nukta ya jenereta $G$. Kupata $k$ kutoka $K$ na $G$ kunalingana na kusuluhisha tatizo la logarithm tofauti kwenye mikunjo ya duaradufu, tatizo gumu kihisabati ambalo hakuna algoriti bora inayojulikana. Hata vikokotoo vya nguvu zaidi vya sasa haviwezi kutatua tatizo hili kwa wakati unaofaa.

![CYP201](assets/fr/018.webp)

### Kuongeza na kuzidisha maradufu kwa Pointi kwenye Mikondo ya elliptic 

Dhana ya kuongeza kwenye curves ya mviringo inaelezwa kijiometri. Ikiwa tuna pointi mbili $P$ na $Q$ kwenye curve, operesheni $P + Q$ inakokotolewa kwa kuchora mstari unaopita $P$ na $Q$. Laini hii itakatiza curve katika sehemu ya tatu $R'$. Kisha tunachukua picha ya kioo ya hatua hii kwa heshima na mhimili wa x kupata uhakika $R$, ambayo ni matokeo ya nyongeza:

$$
P + Q = R
$$

Kielelezo, hii inaweza kuwakilishwa kama ifuatavyo:

![CYP201](assets/fr/019.webp)

Kwa kurudia mara mbili kwa nukta, hiyo ni operesheni $P + P$, tunachora tangent kwa curve kwa uhakika $P $. Tanjenti hii inakatiza mkunjo katika hatua nyingine $S'$. Kisha tunachukua picha ya kioo ya hatua hii kwa heshima na mhimili wa x ili kupata uhakika $S$, ambayo ni matokeo ya kuzidisha maradufu:

$$
2P = S
$$

Kielelezo, hii inaonyeshwa kama:

![CYP201](assets/fr/020.webp)

Kwa kutumia utendakazi huu wa kujumlisha na kuzidisha maradufu, tunaweza kufanya kuzidisha kwa ukubwa wa nukta kwa nambari kamili $k$, inayoashiria $kP$, kwa kutekeleza marudio na nyongeza mara kwa mara.

Kwa mfano, tuseme tumechagua Ufunguo (Key) wa faragha $k = 4$. Ili kuhesabu Ufunguo (Key) wa umma unaohusishwa, tunafanya:

$$
K = k \cdot G = 4G
$$

Kwa picha, hii inalingana na kufanya safu ya nyongeza na mara mbili:


- Kokotoa $2G$ kwa kuongeza $G$ mara mbili.
- Kokotoa $4G$ kwa kuongeza $2G$ mara mbili.

![CYP201](assets/fr/021.webp)

Ikiwa tunataka, kwa mfano, kukokotoa pointi $3G$, ni lazima kwanza tuhesabu pointi $2G$ kwa kuongeza pointi $G$ mara mbili, kisha tuongeze $G$ na $2G$. Ili kuongeza $G$ na $2G$, chora tu mstari unaounganisha pointi hizi mbili, rudisha sehemu ya kipekee $-3G$ kwenye makutano kati ya mstari huu na mkunjo wa duaradufu, na kisha ubaini $3G$ kama kinyume cha $-3G$.

Tutakuwa na:

$$
G + G = 2G
$$

$$
2G + G = 3G
$$

Kielelezo, hii itawakilishwa kama ifuatavyo:

![CYP201](assets/fr/022.webp)

### Kazi ya Njia Moja

Shukrani kwa shughuli hizi, tunaweza kuelewa kwa nini ni rahisi kupata Ufunguo (Key) wa umma kutoka kwa Ufunguo (Key) wa faragha, lakini kinyume haiwezekani.

Hebu turudi kwenye mfano wetu uliorahisishwa. Na Ufunguo (Key) wa kibinafsi $k = 4$. Ili kuhesabu Ufunguo (Key) wa umma unaohusishwa, tunafanya:

$$
K = k \cdot G = 4G
$$

Kwa hivyo tumeweza kukokotoa Ufunguo (Key) wa umma $K$ kwa urahisi kwa kujua $k$ na $G$.

Sasa, ikiwa mtu anajua tu Ufunguo (Key) wa umma $K$, anakabiliwa na shida ya logarithm: kupata $k$ vile $K = k \cdot G$. Tatizo hili linachukuliwa kuwa gumu kwa sababu hakuna algorithm ya ufanisi ya kulitatua kwenye curve za mviringo. Hii inahakikisha usalama wa kanuni za ECDSA na Schnorr.

Kwa kweli, katika mfano huu uliorahisishwa na $k = 4$, itawezekana kupata $k$ kupitia jaribio na kosa, kwani idadi ya uwezekano ni ndogo. Hata hivyo, kiutendaji kwenye Bitcoin, $k$ ni nambari kamili ya biti 256, na kufanya idadi ya uwezekano kuwa kubwa kiastronomia (takriban $1.158 \mara 10^{77}$). Kwa hivyo, haiwezekani kupata $k$ kwa nguvu ya kikatili.

## Kusaini kwa Ufunguo (Key) wa Faragha

<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>

Sasa kwa kuwa unajua jinsi ya kupata Ufunguo (Key) wa umma kutoka kwa Ufunguo (Key) wa kibinafsi, unaweza tayari kupokea bitcoins kwa kutumia jozi ya funguo kama hali ya matumizi. Lakini jinsi ya kuzitumia? Ili kutumia bitcoins, utahitaji kufungua _scriptPubKey_ iliyoambatishwa kwenye UTXO yako ili kuthibitisha kuwa wewe ni mmiliki wake halali. Ili kufanya hivyo, ni lazima utoe sahihi $s$ inayolingana na Ufunguo (Key) wa umma $K$ uliopo kwenye _scriptPubKey_ ukitumia Ufunguo (Key) wa faragha $k$ ambao ulitumika awali kukokotoa $K$. Kwa hivyo, sahihi ya dijiti ni uthibitisho usioweza kukanushwa kuwa una Ufunguo (Key) wa faragha unaohusishwa na Ufunguo (Key) wa umma unaodai.

### Vigezo vya mviringo vya elliptic

Ili kutekeleza saini ya dijiti, washiriki wote lazima kwanza wakubaliane juu ya vigezo vya curve ya mkunjo iliyotumiwa. Kwa upande wa Bitcoin, vigezo vya **secp256k1** ni kama ifuatavyo:

Sehemu ya mwisho $\mathbb{Z}_p$ imefafanuliwa na:

$$
p = 2^{256} - 2^{32} - 977
$$

```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```

$p$ ni nambari kuu kubwa sana chini ya $2^{256}$.

Mviringo wa duaradufu $y^2 = x^3 + shoka + b$ juu ya $\mathbb{Z}_p$ umefafanuliwa na:

$$
a = 0, \quad b = 7
$$

Sehemu ya jenereta au sehemu ya asili $G$:

```text
G = 0x0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
```

Nambari hii ni fomu iliyobanwa ambayo inatoa tu abscissa ya uhakika $G$. Kiambishi awali `02` hapo mwanzoni huamua ni ipi kati ya thamani mbili zilizo na abscissa $x$ hii itatumika kama sehemu ya kuzalisha.

Agizo $n$ ya $G$ (idadi ya pointi zilizopo) na cofactor $h$:

```text
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
```

$n$ ni nambari kubwa sana chini ya $p$.

$$
h=1
$$

$h$ ni cofactor au idadi ya vikundi vidogo. Sitafafanua nini hii inawakilisha hapa, kwa kuwa ni ngumu sana, na kwa upande wa Bitcoin, hatuhitaji kuizingatia kwani ni sawa na $1$.

Taarifa hizi zote ni za umma na zinajulikana kwa washiriki wote. Shukrani kwao, watumiaji wanaweza kutengeneza saini ya dijiti na kuithibitisha.

### Kutia Saini kwa kutumia ECDSA

Kanuni za ECDSA humruhusu mtumiaji kutia sahihi ujumbe kwa kutumia Ufunguo (Key) wake wa faragha, kwa njia ambayo mtu yeyote anayejua Ufunguo (Key) unaolingana wa umma anaweza kuthibitisha uhalali wa sahihi, bila Ufunguo (Key) wa faragha kufichuliwa. Katika muktadha wa Bitcoin, ujumbe utakaotiwa saini unategemea _sighash_ iliyochaguliwa na mtumiaji. Ni _sighash_ hii ambayo itaamua ni sehemu gani za muamala zimefunikwa na sahihi. Nitazungumza zaidi juu ya hili katika sura inayofuata.

Hapa kuna hatua za kutengeneza sahihi ya ECDSA:

Kwanza, tunakokotoa Hash ($e$) ya ujumbe unaohitaji kusainiwa. Ujumbe $m$ kwa hivyo hupitishwa kupitia kazi ya kriptografia ya Hash, kwa ujumla SHA256 au SHA256 mara mbili katika kesi ya Bitcoin:

$$
e = \text{HASH}(m)
$$

Ifuatayo, tunahesabu Nonce. Katika kriptografia, Nonce ni nambari inayozalishwa kwa njia ya nasibu au isiyo ya kawaida ambayo hutumiwa mara moja tu. Hiyo ni kusema, kila wakati saini mpya ya digital inafanywa na jozi hii ya funguo, itakuwa muhimu sana kutumia Nonce tofauti, vinginevyo, itahatarisha usalama wa Ufunguo (Key) wa kibinafsi. Kwa hivyo inatosha kubainisha nambari kamili na ya kipekee $r$ kiasi kwamba $1 \leq r \leq n-1$, ambapo $n$ ni mpangilio wa sehemu ya kuzalisha $G$ ya mkunjo wa duaradufu.

Kisha, tutahesabu nukta $R$ kwenye curve ya duaradufu na kuratibu $(x_R, y_R)$ kama vile:

$$
R = r \cdot G
$$

Tunatoa thamani ya abscissa ya uhakika $R$ ($x_R$). Thamani hii inawakilisha sehemu ya kwanza ya sahihi. Na hatimaye, tunahesabu sehemu ya pili ya sahihi $s$ kwa njia hii:

$$
s = r^{-1} \left( e + k \cdot x_R \right) \mod n
$$

wapi:


- $r^{-1}$ ni kinyume cha moduli cha $r$ modulo $n$, yaani, nambari kamili kiasi kwamba $r \cdot r^{-1} \equiv 1 \mod n$;
- $k$ ni Ufunguo (Key) wa faragha wa mtumiaji;
- $e$ ni Hash ya ujumbe;
- $n$ ni mpangilio wa sehemu ya jenereta $G$ ya mkunjo wa duaradufu.

Sahihi basi ni muunganisho wa $x_R$ na $s$:

$$
\text{SIG} = x_R \Vert s
$$

### Uthibitishaji wa Sahihi ya ECDSA

Ili kuthibitisha saini $(x_R, s)$, mtu yeyote anayejua Ufunguo (Key) wa umma $K$ na vigezo vya curve ya duaradufu anaweza kuendelea kwa njia hii:

Kwanza, thibitisha kuwa $x_R$ na $s$ ziko ndani ya muda $[1, n-1]$. Hii inahakikisha kwamba saini inaheshimu vikwazo vya hisabati vya kikundi cha mviringo. Ikiwa sivyo hivyo, kithibitishaji hukataa mara moja sahihi kama si sahihi.

Kisha, hesabu Hash ya ujumbe:

$$
e = \text{HASH}(m)
$$

Kokotoa ubadilishaji wa moduli wa $s$ modulo $n$:

$$
s^{-1} \mod n
$$

Kokotoa thamani mbili za vipimo $u_1$ na $u_2$ kwa njia hii:

$$
\begin{align*}
u_1 &= e \cdot s^{-1} \mod n \\
u_2 &= x_R \cdot s^{-1} \mod n
\end{align*}
$$

Na mwishowe, hesabu nukta $V$ kwenye curve ya mviringo ili:

$$
V = u_1 \cdot G + u_2 \cdot K
$$

Sahihi ni halali ikiwa tu $x_V \equiv x_R \mod n$, ambapo $x_V$ ni $x$ kiratibu cha uhakika $V$. Hakika, kwa kuchanganya $u_1 \cdot G$ na $u_2 \cdot K$, mtu hupata pointi $V$ ambayo, ikiwa saini ni halali, lazima ilingane na uhakika $R$ uliotumiwa wakati wa kusaini (modulo $n$).

### Sahihi kwa kutumia Itifaki ya Schnorr

Mpango wa sahihi wa Schnorr ni mbadala wa ECDSA ambao hutoa faida nyingi. Imewezekana kuitumia kwenye Bitcoin tangu 2021 na kuanzishwa kwa Taproot, na mifumo ya hati ya P2TR. Kama ECDSA, mpango wa Schnorr unaruhusu kusaini ujumbe kwa kutumia Ufunguo (Key) wa faragha, kwa njia ambayo saini inaweza kuthibitishwa na mtu yeyote anayejua Ufunguo (Key) wa umma unaolingana.

Kwa upande wa Schnorr, curve sawa kabisa na ECDSA inatumiwa na vigezo sawa. Hata hivyo, funguo za umma zinawakilishwa tofauti kidogo ikilinganishwa na ECDSA. Hakika, zimeteuliwa tu na uratibu wa $x$ wa uhakika kwenye curve ya duaradufu. Tofauti na ECDSA, ambapo funguo za umma zilizobanwa zinawakilishwa na baiti 33 (pamoja na kiambishi awali cha baiti inayoonyesha usawa wa $y$), Schnorr hutumia funguo za umma za bytes 32, zinazolingana tu na kiratibu cha $x$ cha uhakika $K$, na inachukuliwa kuwa $y$ ni hata kwa chaguo-msingi. Uwakilishi huu uliorahisishwa hupunguza ukubwa wa saini na kuwezesha uboreshaji fulani katika kanuni za uthibitishaji.

Kitufe cha umma (Public Key) basi ni kiratibu cha $x$ cha uhakika $K$:

$$
\text{pk} = K_x
$$

Hatua ya kwanza kwa kutengeneza saini ni Hash ujumbe. Lakini tofauti na ECDSA, inafanywa na maadili mengine na kitendakazi kilicho na lebo ya Hash Kina (depth)tumika ili kuzuia migongano katika miktadha tofauti. Chaguo za kukokotoa zilizo na lebo ya Hash huhusisha tu kuongeza lebo kiholela kwa ingizo za chaguo za kukokotoa za Hash pamoja na data ya ujumbe.

![CYP201](assets/fr/023.webp)

Kando na ujumbe huo, kiratibu cha $x$ cha Ufunguo (Key) wa umma $K_x$, pamoja na pointi $R$ iliyokokotwa kutoka kwa Nonce $r$ ($R=r \cdot G$) ambayo yenyewe ni nambari kamili ya kipekee kwa kila sahihi, iliyokokotwa kwa kuamua kutoka kwa Ufunguo (Key) wa faragha na ujumbe wa kuepuka udhaifu unaohusiana na Nonce pia hupitishwa kwenye kipengele cha matumizi. Kama tu kwa Ufunguo (Key) wa umma, kiratibu cha $x$ pekee cha nukta ya Nonce $R_x$ ndicho Kina (depth)chobaki kuelezea uhakika.

Matokeo ya hashing hii iliyobainishwa $e$ inaitwa "changamoto":

$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$

Hapa, $\text{Hash}$ ni chaguo za kukokotoa za SHA256 Hash, na $\text{``BIP0340/challenge''}$ ni tagi mahususi ya hashing.

Hatimaye, kigezo $s$ Kina (depth)kokotolewa kwa njia hii kutoka kwa Ufunguo (Key) wa faragha $k$, Nonce $r$, na changamoto $e$:

$$
s = (r + e \cdot k) \mod n
$$

Sahihi basi ni jozi $Rx$ na $s$.

$$
\text{SIG} = R_x \Vert s
$$

### Uthibitishaji wa Sahihi ya Schnorr

Uthibitishaji wa sahihi ya Schnorr ni rahisi kuliko ule wa sahihi ya ECDSA. Hizi ndizo hatua za kuthibitisha sahihi $(R_x, s)$ na Ufunguo (Key) wa umma $K_x$ na ujumbe $m$:

Kwanza, tunathibitisha kuwa $K_x$ ni nambari kamili na chini ya $p$. Ikiwa hali ndio hii, tunarudisha sehemu inayolingana kwenye mkunjo na $K_y$ ikiwa sawa. Pia tunatoa $R_x$ na $s$ kwa kutenganisha sahihi $\text{SIG}$. Kisha, tunaangalia kuwa $R_x < p$ na $s < n$ (mpangilio wa curve).

Kisha, tunakokotoa changamoto $e$ kwa njia sawa na mtoaji wa saini:

$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$

Halafu, tunahesabu sehemu ya kumbukumbu kwenye curve kwa njia hii:

$$
R' = s \cdot G - e \cdot K
$$

Hatimaye, tunathibitisha kuwa $R'_x = R_x$. Ikiwa viwianishi viwili vya x vinalingana, basi sahihi $(R_x, s)$ ni halali kwa Ufunguo (Key) wa umma $K_x$.

### Kwa nini hii inafanya kazi?

Mtia sahihi amekokotoa $s = r + e \cdot k \mod n$, kwa hivyo $R' = s \cdot G - e \cdot K$ inapaswa kuwa sawa na nukta asili $R$, kwa sababu:

$$
s \cdot G = (r + e \cdot k) \cdot G = r \cdot G + e \cdot k \cdot G
$$

Kwa kuwa $K = k \cdot G$, tuna $e \cdot k \cdot G = e \cdot K$. Hivyo:

$$
R' = r \cdot G = R
$$

Kwa hivyo, tunayo:

$$
R'_x = R_x
$$

### Faida za saini za Schnorr

Mpango wa saini wa Schnorr unatoa faida kadhaa kwa Bitcoin juu ya algoriti asilia ya ECDSA. Kwanza, Schnorr inaruhusu ujumlisho wa funguo na saini. Hii inamaanisha kuwa funguo nyingi za umma zinaweza kuunganishwa kuwa Ufunguo (Key) mmoja.

![CYP201](assets/fr/024.webp)

Na vile vile, sahihi nyingi zinaweza kujumlishwa kuwa sahihi moja halali. Kwa hivyo, katika kesi ya shughuli ya saini nyingi, seti ya washiriki inaweza kusaini na saini moja na Ufunguo (Key) mmoja wa umma uliojumlishwa. Hii inapunguza kwa kiasi kikubwa gharama za kuhifadhi na kukokotoa kwa mtandao, kwani kila nodi inahitaji tu kuthibitisha saini moja.

![CYP201](assets/fr/025.webp)

Zaidi ya hayo, ujumlishaji wa saini huboresha faragha. Kwa Schnorr, inakuwa vigumu kutofautisha muamala wa saini nyingi kutoka kwa muamala wa kawaida wa sahihi moja. Ufanano huu unafanya uchambuzi wa chain kuwa mgumu zaidi, kwani inapunguza uwezo wa kutambua alama za vidole za Wallet.

Hatimaye, Schnorr pia inatoa uwezekano wa uthibitishaji wa kundi. Kwa kuthibitisha saini nyingi kwa wakati mmoja, nodi zinaweza kupata ufanisi, hasa kwa vitalu vilivyo na miamala mingi. Uboreshaji huu hupunguza muda na rasilimali zinazohitajika ili kuthibitisha kizuizi.

Pia, sahihi za Schnorr hazitengenezwi, tofauti na sahihi zinazotolewa na ECDSA. Hii inamaanisha kuwa mshambulizi hawezi kurekebisha saini halali ili kuunda sahihi nyingine halali ya ujumbe sawa na Ufunguo (Key) sawa wa umma. Athari hii ilikuwepo hapo awali kwenye Bitcoin na ilizuia haswa utekelezaji salama wa Lightning Network. Ilisuluhishwa kwa ECDSA na SegWit softfork mwaka wa 2017, ambayo inahusisha kuhamisha saini kwenye hifadhidata tofauti kutoka kwa shughuli ili kuzuia uharibifu wao.

### Kwa nini Satoshi ilichagua ECDSA?

Kama tulivyoona, Satoshi mwanzoni ilichagua kutekeleza ECDSA kwa sahihi za kidijitali kwenye Bitcoin. Hata hivyo, tumeona pia kwamba Schnorr ni bora kuliko ECDSA katika nyanja nyingi, na itifaki hii iliundwa na Claus-Peter Schnorr mnamo 1989, miaka 20 kabla ya uvumbuzi wa Bitcoin.

Kweli, hatujui kwa nini Satoshi haikuichagua, lakini dhana inayowezekana ni kwamba itifaki hii ilikuwa chini ya hataza hadi 2008. Ingawa Bitcoin iliundwa mwaka mmoja baadaye, mnamo Januari 2009, hakuna usawazishaji wa chanzo wazi wa sahihi za Schnorr ulipatikana wakati huo. Labda Satoshi iliona kuwa ni salama zaidi kutumia ECDSA, ambayo tayari ilikuwa inatumika sana na kufanyiwa majaribio katika programu huria na ilikuwa na utekelezaji kadhaa unaotambulika (haswa maktaba ya OpenSSL iliyotumika hadi 2015 kwenye Bitcoin Core, kisha kubadilishwa na libsecp256k1 katika Toleo (version) la 0.10.0). Au labda hakujua kuwa hataza hii ingeisha muda wake mwaka wa 2008. Kwa vyovyote vile, dhana inayowezekana zaidi inaonekana kuhusiana na hataza hii na ukweli kwamba ECDSA ilikuwa na historia iliyothibitishwa na ilikuwa rahisi kutekelezwa.

## Bendera za sighash

<chapterId>231c41a2-aff2-4655-9048-47b6d2d83d64</chapterId>

Kama tulivyoona katika sura zilizopita, saini za dijiti mara nyingi hutumiwa kufungua hati ya ingizo. Katika mchakato wa kutia saini, ni muhimu kujumuisha data iliyotiwa sahihi katika hesabu, iliyobainishwa katika mifano yetu kwa ujumbe $m$. Data hii, ikishatiwa saini, haiwezi kurekebishwa bila kufanya sahihi kuwa batili. Hakika, iwe kwa ECDSA au Schnorr, kithibitishaji sahihi lazima kijumuishe katika hesabu ya ujumbe sawa $m$. Iwapo itatofautiana na ujumbe $m$ uliotumiwa mwanzoni na mtu aliyetia sahihi, matokeo yatakuwa si sahihi na sahihi itachukuliwa kuwa batili. Kisha inasemekana kuwa saini inashughulikia data fulani na kuilinda, kwa njia, dhidi ya marekebisho yasiyoidhinishwa.

### Bendera ya sighash ni nini?

Katika hali mahususi ya Bitcoin, tumeona kuwa ujumbe $m$ unalingana na muamala. Walakini, kwa ukweli, ni ngumu zaidi. Hakika, shukrani kwa bendera za sighash, inawezekana kuchagua data mahususi ndani ya muamala ambayo itafunikwa au la na sahihi.

"Bendera ya sighash" kwa hivyo ni kigezo kilichoongezwa kwa kila ingizo, ikiruhusu uamuzi wa vipengee vya muamala ambavyo vinafunikwa na saini inayohusishwa. Vipengele hivi ni pembejeo na matokeo. Kwa hivyo, chaguo la bendera ya sighash huamua ni pembejeo zipi na ni matokeo gani ya muamala yanarekebishwa na sahihi na ambayo bado yanaweza kurekebishwa bila kuibatilisha. Utaratibu huu huruhusu saini kutekeleza data ya muamala kulingana na nia ya aliyetia sahihi.

Ni wazi, mara shughuli hiyo inapothibitishwa kwenye Blockchain, inakuwa haiwezi kubadilika, bila kujali bendera za sighash zinazotumiwa. Uwezekano wa kurekebisha kupitia bendera za sighash ni mdogo kwa kipindi kati ya kutia saini na uthibitisho.

Kwa ujumla, programu ya Wallet haikupi chaguo la kurekebisha mwenyewe bendera ya sighash ya ingizo lako unapounda muamala. Kwa chaguomsingi, `SIGHASH_ALL` imewekwa. Binafsi, najua tu Sparrow Wallet ambayo inaruhusu marekebisho haya kutoka kwa mtumiaji Interface.

### Je, ni bendera gani za sighash zilizopo kwenye Bitcoin?

Kwenye Bitcoin, kuna kwanza kabisa bendera 3 za kimsingi za sighash:


- `SIGHASH_ALL` (`0x01`): Sahihi inatumika kwa ingizo zote na matokeo yote ya muamala. Kwa hivyo shughuli hiyo inafunikwa kabisa na sahihi na haiwezi kurekebishwa tena. `SIGHASH_ALL` ndiyo sighash inayotumika sana katika shughuli za kila siku wakati mtu anataka tu kufanya muamala bila kurekebishwa.

![CYP201](assets/fr/026.webp)

Katika michoro zote za sura hii, rangi ya machungwa inawakilisha Elements iliyofunikwa na saini, wakati rangi nyeusi inaonyesha wale ambao sio.


- `SIGHASH_NONE` (`0x02`): Sahihi inashughulikia ingizo zote lakini hakuna towe, hivyo basi kuruhusu urekebishaji wa matokeo baada ya sahihi. Kwa maneno madhubuti, hii ni sawa na hundi tupu. Mtia saini hufungua UTXO katika pembejeo lakini huacha uga wa matokeo uweze kurekebishwa kabisa. Mtu yeyote anayejua shughuli hii anaweza kuongeza matokeo ya uchaguzi wao, kwa mfano kwa kubainisha kupokea Address kukusanya fedha zinazotumiwa na pembejeo, na kisha kutangaza shughuli ili kurejesha bitcoins. Sahihi ya mmiliki wa pembejeo haitabatilishwa, kwani inashughulikia pembejeo tu.

![CYP201](assets/fr/027.webp)


- `SIGHASH_SINGLE` (`0x03`): Sahihi inashughulikia ingizo zote pamoja na towe moja, sambamba na faharasa ya ingizo lililotiwa sahihi. Kwa mfano, ikiwa sahihi itafungua _scriptPubKey_ ya ingizo #0, basi itashughulikia pia pato #0. Sahihi pia hulinda pembejeo zingine zote, ambazo haziwezi kurekebishwa tena. Walakini, mtu yeyote anaweza kuongeza pato la ziada bila kubatilisha saini, mradi pato #0, ambalo ndilo pekee lililofunikwa nayo, halijabadilishwa.

![CYP201](assets/fr/028.webp)

Kando na bendera hizi tatu za sighash, pia kuna kirekebishaji `SIGHASH_ANYONECANPAY` (`0x80`). Kirekebishaji hiki Kina (depth)weza kuunganishwa na bendera ya msingi ya sighash ili kuunda bendera tatu mpya za sighash:


- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Sahihi inashughulikia ingizo moja huku ikijumuisha matokeo yote ya muamala. Bendera hii ya pamoja ya sighash inaruhusu, kwa mfano, kuundwa kwa shughuli ya ufadhili wa watu wengi. Mratibu hutayarisha pato kwa kutumia Address yao na kiasi Kina (depth)cholengwa, na kila mwekezaji anaweza kuongeza pembejeo ili kufadhili pato hili. Pesa za kutosha zinapokusanywa ili kukidhi matokeo, shughuli hiyo inaweza kutangazwa.

![CYP201](assets/fr/029.webp)


- `SIGHASH_HAKUNA | SIGHASH_ANYONECANPAY` (`0x82`): Sahihi inashughulikia ingizo moja, bila kujitolea kutoa matokeo yoyote;

![CYP201](assets/fr/030.webp)


- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Sahihi inashughulikia ingizo moja pamoja na towe lenye faharasa sawa na ingizo hili. Kwa mfano, ikiwa sahihi itafungua _scriptPubKey_ ya ingizo #3, itafunika pia pato #3. Muamala uliosalia unabaki kurekebishwa, kulingana na pembejeo zingine na matokeo mengine.

![CYP201](assets/fr/031.webp)

### Miradi ya Kuongeza Bendera Mpya za Sighash

Kwa sasa (2024), ni bendera za sighash pekee zilizowasilishwa katika sehemu iliyotangulia ndizo zinazotumika kwenye Bitcoin. Hata hivyo, baadhi ya miradi inazingatia kuongezwa kwa bendera mpya za sighash. Kwa mfano, BIP118, iliyopendekezwa na Christian Decker na Anthony Towns, inatanguliza bendera mbili mpya za sighash: `SIGHASH_ANYPREVOUT` na `SIGHASH_ANYPREVOUTANYSCRIPT` (_AnyPrevOut = "Pato Lolote Lililotangulia"_).

Bendera hizi mbili za sighash zinaweza kutoa uwezekano wa ziada kwenye Bitcoin: kuunda sahihi ambazo hazijumuishi ingizo lolote mahususi la muamala.

![CYP201](assets/fr/032.webp)

Wazo hili lilitayarishwa awali na Joseph Poon na Thaddeus Dryja katika Karatasi Nyeupe ya Lightning. Kabla ya kubadilishwa jina, bendera hii ya sighash iliitwa `SIGHASH_NOINPUT`.

Ikiwa bendera hii ya sighash itaunganishwa katika Bitcoin, itawezesha matumizi ya maagano, lakini pia ni sharti la lazima la kutekeleza Eltoo, itifaki ya jumla ya tabaka za pili ambayo inafafanua jinsi ya kusimamia kwa pamoja Umiliki wa UTXO. Eltoo iliundwa  kutatua shida zinazohusiana na mifumo ya kujadili hali ya njia za Lightning, ambayo ni, kati ya kufungua na kufunga.

Ili kuongeza ujuzi wako wa Lightning Network, baada ya kozi ya CYP201, ninapendekeza sana kozi ya LNP201 na Fanis Michalakis, ambayo inashughulikia mada kwa undani:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb
Katika sehemu inayofuata, ninapendekeza kugundua jinsi maneno ya Mnemonic kwenye msingi wa Bitcoin Wallet yako inavyofanya kazi.

# Maneno ya Mnemonic

<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>

## Mageuzi ya Wallet za Bitcoin

<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>

Kwa kuwa sasa tumechunguza utendakazi wa kazi za Hash na sahihi za dijitali, tunaweza kusoma jinsi wallet za Bitcoin zinavyofanya kazi. Lengo litakuwa kufikiria jinsi Wallet kwenye Bitcoin inavyoundwa, jinsi inavyotengana, na vipande tofauti vya habari vinavyoiunda vinatumika kwa matumizi gani. Uelewa huu wa taratibu za Wallet utakuruhusu kuboresha matumizi yako ya Bitcoin katika masuala ya usalama na faragha.

Kabla ya kuingia katika maelezo ya kiufundi, ni muhimu kufafanua nini maana ya "Bitcoin Wallet" na kuelewa matumizi yake.

### Bitcoin Wallet ni nini?

Tofauti na mikoba ya jadi, ambayo inakuwezesha kuhifadhi bili za kimwili na sarafu, Bitcoin Wallet haina "bitcoins" kwa kila seti. Hakika, bitcoins hazipo katika fomu ya kimwili au ya dijiti inayoweza kuhifadhiwa, lakini inawakilishwa na vitengo vya Akaunti (Account) vilivyoonyeshwa kwenye mfumo kwa njia ya **UTXOs** (_Toto la Muamala Usiotumika_).

UTXO kwa hivyo huwakilisha vipande vya bitcoins, vya ukubwa tofauti, ambavyo vinaweza kutumika mradi _scriptPubKey_ yao imeridhika. Ili kutumia bitcoins zake, ni lazima mtumiaji atoe _scriptSig_ inayofungua _scriptPubKey_ inayohusishwa na UTXO yake. Uthibitisho huu kwa ujumla hufanywa kupitia sahihi ya dijitali, inayotolewa kutoka kwa Ufunguo (Key) wa faragha unaolingana na Ufunguo (Key) wa umma uliopo katika _scriptPubKey_. Kwa hivyo, kipengele muhimu ambacho mtumiaji lazima alinde ni Ufunguo (Key) wa faragha.

Jukumu la Bitcoin Wallet ni kudhibiti funguo hizi za faragha kwa usalama. Kwa kweli, jukumu lake ni sawa na lile la keychain kuliko Wallet kwa maana ya jadi.

### Wallet za JBOK (_Funguo nyingi tu_)

Pochi za kwanza zilizotumika kwenye Bitcoin zilikuwa pochi za JBOK (_Just a Bunch Of Keys_), ambazo ziliweka pamoja funguo zilizoundwa kwa faragha kwa kujitegemea na bila kiungo chochote kati yao. Pochi hizi zilifanya kazi kwa muundo rahisi ambapo kila Ufunguo (Key) wa faragha ungeweza kufungua Bitcoin ya kipekee inayopokea Address.

![CYP201](assets/fr/033.webp)

Iwapo mtu alitaka kutumia funguo nyingi za faragha, basi ilikuwa ni lazima kutengeneza nakala nyingi ili kuhakikisha ufikiaji wa pesa ikiwa kuna matatizo na kifaa Kina (depth)chopangisha Wallet. Ikiwa unatumia Ufunguo (Key) mmoja wa kibinafsi, muundo huu wa Wallet unaweza kutosha, kwani hifadhi moja inatosha. Walakini, hii inaleta shida: kwenye Bitcoin, inashauriwa sana dhidi ya kila wakati kutumia Ufunguo (Key) sawa wa kibinafsi. Hakika, Ufunguo (Key) wa faragha unahusishwa na Address ya kipekee, na anwani za kupokea za Bitcoin kwa kawaida zimeundwa kwa matumizi ya mara moja. Kila wakati unapopokea pesa, unapaswa generate mpya tupu Address.

Kizuizi hiki Kina (depth)tokana na mtindo wa faragha wa Bitcoin. Kwa kutumia tena Address sawa, hurahisisha waangalizi wa nje kufuatilia miamala yangu yote ya Bitcoin. Ndiyo maana kutumia tena kupokea Address kumekatishwa tamaa sana. Hata hivyo, ili kuwa na anwani nyingi na kutenganisha shughuli zetu hadharani, ni muhimu kudhibiti funguo nyingi za faragha. Kwa upande wa pochi za JBOK, hii inamaanisha kuunda nakala rudufu nyingi kwani kuna jozi mpya za funguo, kazi ambayo inaweza kuwa ngumu na ngumu kudumisha kwa watumiaji haraka.

Ili kupata maelezo zaidi kuhusu muundo wa faragha wa Bitcoin na kugundua mbinu za kulinda faragha yako, ninapendekeza pia kufuata kozi yangu ya BTC204 kwenye Plan ₿ Network:

https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c
### wallet za HD (_Hierarchical Deterministic_)

Kwa Address kizuizi cha pochi za JBOK, muundo mpya wa Wallet ulitumiwa baadaye. Mnamo mwaka wa 2012, Pieter Wuille alianzisha uboreshaji na BIP32, ambayo inaleta pochi za uamuzi wa hierarkia. Kanuni ya HD Wallet ni kupata funguo zote za kibinafsi kutoka kwa chanzo kimoja cha habari, Kina (depth)choitwa seed, kwa njia ya kuamua na ya hierarchical. seed hii inatolewa kwa nasibu wakati Wallet inapoundwa na kuunda hifadhi rudufu ya kipekee inayoruhusu uundaji wa funguo zote za faragha za Wallet. Kwa hivyo, mtumiaji anaweza generate idadi kubwa sana ya funguo za faragha ili kuepuka kutumia tena Address na kuhifadhi faragha yao, huku akihitaji tu kufanya nakala moja ya Wallet yao kupitia seed.

![CYP201](assets/fr/034.webp)

Katika pochi za HD, utokaji wa Ufunguo (Key) unafanywa kulingana na muundo wa kidaraja unaoruhusu funguo kupangwa katika nafasi ndogo zinazotoka, kila nafasi ndogo inaweza kugawanywa zaidi, ili kuwezesha usimamizi wa hazina na ushirikiano kati ya programu tofauti za Wallet. Siku hizi, kiwango hiki Kina (depth)kubaliwa na idadi kubwa ya watumiaji wa Bitcoin. Kwa sababu hii, tutaichunguza kwa undani katika sura zifuatazo.

### Kiwango cha BIP39: Neno la Mnemonic

Kando na BIP32, BIP39 husawazisha umbizo la seed kama maneno ya Mnemonic, ili kuwezesha kuhifadhi nakala na kusomeka kwa watumiaji. Kishazi cha Mnemonic, pia huitwa kishazi cha kurejesha au maneno 24, ni mfuatano wa maneno yaliyotolewa kutoka kwa orodha iliyoainishwa awali ambayo husimba kwa usalama seed ya Wallet.

Kifungu cha maneno cha Mnemonic hurahisisha sana hifadhi rudufu kwa mtumiaji. Katika kesi ya upotevu, uharibifu, au wizi wa kifaa Kina (depth)chohudumia Wallet, kujua tu kifungu hiki cha Mnemonic inaruhusu burudani ya Wallet na kurejesha upatikanaji wa fedha zote zinazolindwa nayo.

Katika sura zijazo, tutachunguza utendakazi wa ndani wa pochi za HD, ikijumuisha njia kuu za utoeji na miundo tofauti ya daraja inayowezekana. Hii itakuruhusu kuelewa vyema misingi ya kriptografia ambayo usalama wa fedha kwenye Bitcoin unategemea. Na kuanza, katika sura inayofuata, ninapendekeza tugundue jukumu la entropy kwenye msingi wa Wallet yako.

## Nambari ya Entropy na Random

<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>

Mikoba ya kisasa ya HD (ya kuamua na ya daraja) hutegemea taarifa moja ya awali inayoitwa "entropy" ili kubainisha generate seti nzima ya funguo za Wallet. Entropy hii ni nambari ya pseudo-random ambayo kiwango cha machafuko huamua usalama wa Wallet.

### Ufafanuzi wa Entropy

Entropy, katika muktadha wa fiche na maelezo, ni kipimo cha kiasi cha kutokuwa na uhakika au kutotabirika kuhusishwa na chanzo cha data au mchakato wa nasibu. Inachukua jukumu muhimu katika usalama wa mifumo ya kriptografia, haswa katika utengenezaji wa funguo na nambari za nasibu. Kiwango cha juu cha entropy huhakikisha kuwa funguo zinazozalishwa hazitabiriki vya kutosha na hustahimili mashambulizi ya nguvu, ambapo mshambuliaji hujaribu michanganyiko yote inayowezekana ili kubashiri Ufunguo (Key).

Katika muktadha wa Bitcoin, entropy inatumika kwa kuzalisha seed. Wakati wa kuunda Wallet ya kuamua na ya hierarchical, ujenzi wa maneno ya Mnemonic unafanywa kutoka kwa nambari ya random, yenyewe inayotokana na chanzo cha entropy. Kisha maneno hutumika kwa kuzalisha funguo nyingi za faragha, kwa njia ya kuamua na ya uongozi, kuunda hali ya matumizi kwenye UTXO.

### Njia za Kuzalisha Entropy

Entropy ya awali inayotumika kwa HD Wallet kwa ujumla ni biti 128 au biti 256, ambapo:


- **Bits 128 za entropy** zinalingana na kifungu cha Mnemonic cha **maneno 12**;
- **Bits 256 za entropy** zinalingana na kifungu cha maneno cha Mnemonic cha **maneno 24**.

Mara nyingi, nambari hii ya nasibu huzalishwa kiotomatiki na programu ya Wallet kwa kutumia PRNG (_Pseudo-Random Number Generator_). PRNG ni kategoria ya algoriti zinazotumiwa kwa mfuatano wa kuzalishwa wa nambari kutoka hali ya awali, ambayo ina sifa zinazokaribia ile ya nambari nasibu, bila kuwa moja. PRNG nzuri lazima iwe na sifa kama vile usawa wa matokeo, kutotabirika, na upinzani dhidi ya mashambulizi ya kutabiri. Tofauti na jenereta za kweli za nambari nasibu (TRNG), PRNG zinaweza kubainishwa na zinaweza kuzaliana tena.

![CYP201](assets/fr/035.webp)

Njia mbadala ni kuzalisha entropy mwenyewe, ambayo inatoa udhibiti bora lakini pia ni hatari zaidi. Ninashauri sana dhidi ya kutengeneza entropy ya HD yako Wallet wewe mwenyewe.

Katika sura inayofuata, tutaona jinsi tunavyotoka kwa nambari isiyo ya kawaida hadi kifungu cha Mnemonic cha maneno 12 au 24.

## Maneno ya Mnemonic

<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>

Kifungu cha maneno cha Mnemonic, pia Kina (depth)itwa "maneno ya seed", "maneno ya kurejesha", "maneno ya siri", au "maneno ya maneno 24", ni mlolongo kwa kawaida unaojumuisha maneno 12 au 24, ambayo hutolewa kutoka kwa entropy. Inatumika kupata funguo zote za HD Wallet. Hii ina maana kwamba kutokana na kifungu hiki, inawezekana kubainisha generate na kuunda upya funguo zote za kibinafsi na za umma za Bitcoin Wallet, na hivyo kufikia pesa ambazo zinalindwa nayo. Madhumuni ya maneno ya Mnemonic ni kutoa njia ya kuhifadhi na kurejesha bitcoins ambayo ni salama na rahisi kutumia. Ilianzishwa katika viwango mwaka 2013 na BIP39.

Wacha tugundue pamoja jinsi ya kutoka kwa entropy hadi kifungu cha Mnemonic.

### Chekisum

Ili kubadilisha entropy kuwa kifungu cha Mnemonic, lazima kwanza mtu aongeze cheki (au "jumla ya kudhibiti") mwishoni mwa entropy. Hundi hii ni mlolongo mfupi wa biti ambao huhakikisha uadilifu wa data kwa kuthibitisha kuwa hakuna urekebishaji wowote ambao umeanzishwa.

Ili kuhesabu hundi, kazi ya SHA256 Hash inatumika kwa entropy (mara moja tu; hii ni moja ya matukio ya kawaida katika Bitcoin ambapo SHA256 Hash moja hutumiwa badala ya Hash mara mbili). Operesheni hii inazalisha 256-bit Hash. Checksum ina bits za kwanza za Hash hii, na urefu wake unategemea ile ya entropy, kulingana na formula ifuatayo:

$$
\text{CS} = \frac{\text{ENT}}{32}
$$

ambapo $\text{ENT}$ inawakilisha urefu wa entropy katika biti, na $\text{CS}$ urefu wa checksum katika biti.

Kwa mfano, kwa entropy ya bits 256, bits 8 za kwanza za Hash zinachukuliwa ili kuunda checksum:

$$
\text{CS} = \frac{256}{32} = 8 \text{ bits}
$$

Mara tu hundi inapokokotolewa, inaunganishwa na entropy ili kupata mlolongo wa biti uliopanuliwa uliobainishwa $\text{ENT} \Vert \text{CS}$ ("concatenate" inamaanisha kuweka mwisho-hadi-mwisho).

![CYP201](assets/fr/036.webp)

### Mawasiliano kati ya Entropy na Neno la Mnemonic

Idadi ya maneno katika kifungu cha Mnemonic inategemea saizi ya entropy ya awali, kama inavyoonyeshwa kwenye jedwali lifuatalo na:


- $\text{ENT}$: saizi katika bits ya entropy;
- $\text{CS}$: saizi katika bits ya checksum;
- $w$: idadi ya maneno katika kifungu cha mwisho cha Mnemonic.

$$
\begin{array}{|c|c|c|c|}
\hline
\text{ENT} & \text{CS} & \text{ENT} \Vert \text{CS} & w \\
\hline
128 & 4 & 132 & 12 \\
160 & 5 & 165 & 15 \\
192 & 6 & 198 & 18 \\
224 & 7 & 231 & 21 \\
256 & 8 & 264 & 24 \\
\hline
\end{array}
$$

Kwa mfano, kwa entropy ya 256-bit, matokeo $\text{ENT} \Vert \text{CS}$ ni biti 264 na hutoa kifungu cha maneno cha Mnemonic cha maneno 24.

### Ubadilishaji wa Mfuatano wa Nambari kuwa Neno la Mnemonic

Mfuatano wa bits $\text{ENT} \Vert \text{CS}$ kisha umegawanywa katika sehemu za biti 11. Kila sehemu ya biti 11, ikibadilishwa kuwa desimali, inalingana na nambari kati ya 0 na 2047, ambayo huashiria nafasi ya neno [katika orodha ya maneno 2048 yaliyosanifiwa na BIP39](https://github.com/Planb-Network/Bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf).

![CYP201](assets/fr/037.webp)

Kwa mfano, kwa entropy ya 128-bits, checksum ni bits 4, na hivyo mlolongo wa jumla hupima bits 132. Imegawanywa katika sehemu 12 za bits 11 (biti za machungwa hutaja cheki):

![CYP201](assets/fr/038.webp)

Kisha kila sehemu inabadilishwa kuwa nambari ya desimali inayowakilisha neno katika orodha. Kwa mfano, sehemu ya jozi `01011010001` ni sawa katika desimali na `721`. Kwa kuongeza 1 ili kupatanisha na faharasa ya orodha (ambayo huanza 1 na si 0), hii inatoa neno cheo `722`, ambalo ni "_focus_" katika orodha.

![CYP201](assets/fr/039.webp)

Mawasiliano haya yanarudiwa kwa kila moja ya sehemu 12, ili kupata kifungu cha maneno 12.

![CYP201](assets/fr/040.webp)

### Sifa za Orodha ya Maneno ya BIP39

Umaalumu wa orodha ya maneno ya BIP39 ni kwamba hakuna neno linaloshiriki herufi nne za kwanza kwa mpangilio sawa na neno lingine. Hii ina maana kwamba kubainisha herufi nne tu za kwanza za kila neno kunatosha kuhifadhi maneno ya Mnemonic. Hii inaweza kuwa ya kuvutia kwa ajili ya kuokoa nafasi, hasa kwa wale ambao wanataka kuchonga juu ya msaada wa chuma.

Orodha hii ya maneno 2048 ipo katika lugha kadhaa. Hizi si tafsiri rahisi, lakini maneno tofauti kwa kila lugha. Hata hivyo, inashauriwa sana kushikamana na Toleo (version) la Kiingereza, kwa kuwa maToleo (version) katika lugha nyingine kwa ujumla hayatumiki na programu ya Wallet.

### Je, ni Urefu Gani wa Kuchagua kwa Kifungu chako cha Maneno cha Mnemonic?

Ili kubainisha urefu kamili wa maneno yako ya Mnemonic, ni lazima mtu azingatie usalama halisi unaotoa. Kishazi cha maneno 12 huhakikisha biti 128 za usalama, huku kifungu cha maneno 24 Kina (depth)toa biti 256.

Hata hivyo, tofauti hii ya usalama wa kiwango cha maneno haiboresha usalama wa jumla wa Bitcoin Wallet, kwani funguo za faragha zinazotokana na maneno haya hunufaika tu na biti 128 za usalama. Hakika, kama tulivyoona hapo awali, funguo za faragha za Bitcoin zinatolewa kutoka kwa nambari nasibu (au hutolewa kutoka chanzo nasibu) kuanzia $1$ na $n-1$, ambapo $n$ inawakilisha mpangilio wa sehemu ya jenereta $G$ ya mkunjo wa secp256k1, nambari iliyo chini kidogo ya $2^{256}$. Kwa hivyo mtu anaweza kufikiria kuwa funguo hizi za kibinafsi hutoa biti 256 za usalama. Hata hivyo, usalama wao upo katika ugumu wa kupata Ufunguo (Key) wa faragha kutoka kwa Ufunguo (Key) wake wa umma unaohusishwa, ugumu ulioanzishwa na tatizo la hisabati la logarithm tofauti kwenye mikondo ya duaradufu (_ECDLP_). Hadi sasa, algorithm inayojulikana zaidi ya kutatua tatizo hili ni rho algorithm ya Pollard, ambayo inapunguza idadi ya shughuli zinazohitajika kuvunja Ufunguo (Key) wa mizizi ya mraba ya ukubwa wake.

Kwa vitufe vya 256-bit, kama vile vinavyotumika kwenye Bitcoin, algoriti ya rho ya Pollard inapunguza uchangamano hadi $2^{128}$ oparesheni:

$$
O(\sqrt{2^{256}}) = O(2^{128})
$$

Kwa hiyo, inachukuliwa kuwa Ufunguo (Key) wa kibinafsi unaotumiwa kwenye Bitcoin hutoa bits 128 za usalama.

Kwa hivyo, kuchagua kifungu cha maneno 24 hakutoi ulinzi wa ziada kwa Wallet, kwani bits 256 za usalama kwenye kifungu hazina maana ikiwa vitufe vilivyotolewa vinatoa tu biti 128 za usalama. Ili kuonyesha kanuni hii, ni kama kuwa na nyumba yenye milango miwili: mlango wa zamani wa mbao na mlango ulioimarishwa. Katika tukio la wizi, mlango ulioimarishwa hautakuwa na manufaa, kwa kuwa mshambulizi angepitia mlango wa mbao. Hii ni hali inayofanana hapa.

Kifungu cha maneno 12, ambacho pia hutoa bits 128 za usalama, kwa hivyo kwa sasa Kina (depth)tosha kulinda bitcoins zako dhidi ya jaribio lolote la wizi. Maadamu algoriti ya sahihi ya dijiti haibadiliki ili kutumia vitufe vikubwa zaidi au kutegemea tatizo la hisabati kando na ECDLP, kishazi cha maneno 24 Kina (depth)salia kuwa cha juu zaidi. Zaidi ya hayo, maneno marefu huongeza hatari ya hasara wakati wa kuhifadhi: chelezo ambayo ni fupi mara mbili huwa rahisi kudhibiti kila wakati.

Ili kwenda mbali zaidi na kujifunza kwa uwazi jinsi ya kutengeneza maneno ya generate ya jaribio la Mnemonic, nakushauri ugundue somo hili:

https://planb.network/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228
Kabla ya kuendelea na upataji wa Wallet kutoka kwa kifungu hiki cha Mnemonic, nitakujulisha, katika sura inayofuata, kwa BIP39 passphrase, kwani ina jukumu katika mchakato wa uundaji, na iko katika kiwango sawa na kifungu cha Mnemonic.

## passphrase

<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>

Kama tulivyoona hivi punde wallet za HD hutengenezwa kutoka kwa maneno ya Mnemonic ambayo kwa kawaida huwa na maneno 12 au 24. Maneno haya ni muhimu sana kwa sababu inaruhusu kurejeshwa kwa funguo zote za Wallet ikiwa kifaa chake cha kimwili (kama Hardware Wallet, kwa mfano) Kina (depth)potea. Hata hivyo, ni hatua moja ya kushindwa, kwa sababu ikiwa imeathiriwa, mshambuliaji anaweza kuiba bitcoins zote. Hapa ndipo BIP39 passphrase inapotumika.

### BIP39 passphrase ni nini?

passphrase ni nenosiri la hiari, ambalo unaweza kuchagua kwa uhuru, ambalo linaongezwa kwa maneno ya Mnemonic katika mchakato wa utoaji muhimu ili kuimarisha usalama wa Wallet.

Kuwa mwangalifu, passphrase haipaswi kuchanganyikiwa na msimbo wa PIN wa Hardware Wallet yako au nenosiri linalotumiwa kufungua ufikiaji wa Wallet yako kwenye kompyuta yako. Tofauti na Elements hizi zote, passphrase ina jukumu katika kupata funguo zako za Wallet. **Hii ina maana kwamba bila hiyo, hutaweza kurejesha bitcoins zako.**

passphrase inafanya kazi sanjari na maneno ya Mnemonic, kurekebisha seed ambayo funguo hutolewa. Kwa hivyo, hata kama mtu atapata kifungu chako cha maneno 12 au 24, bila passphrase, hawezi kufikia pesa zako. Kutumia passphrase kimsingi huunda Wallet mpya na funguo tofauti. Kurekebisha (hata kidogo) passphrase itakuwa generate tofauti Wallet.

![CYP201](assets/fr/041.webp)

### Kwa nini utumie passphrase?

passphrase ni ya kiholela na inaweza kuwa mchanganyiko wowote wa wahusika waliochaguliwa na mtumiaji. Kutumia passphrase hivyo hutoa faida kadhaa. Kwanza kabisa, inapunguza hatari zote zinazohusiana na maelewano ya maneno ya Mnemonic kwa kuhitaji sababu ya pili ya kupata fedha (wizi, upatikanaji wa nyumba yako, nk).

Ifuatayo, inaweza kutumika kimkakati kuunda decoy Wallet, ili kukabiliana na vikwazo vya kimwili ili kuiba pesa zako kama vile "_$5 wrench attack_". Katika hali hii, wazo ni kuwa na Wallet bila passphrase iliyo na kiasi kidogo tu cha bitcoins, kutosha kukidhi mchokozi anayeweza, huku akiwa na Wallet iliyofichwa. Mwisho huu hutumia maneno sawa ya Mnemonic lakini imelindwa na passphrase ya ziada.

Hatimaye, matumizi ya passphrase ni ya kuvutia wakati mtu anataka kudhibiti randomness ya kizazi cha seed ya HD Wallet.

### Jinsi ya kuchagua passphrase nzuri?

Ili passphrase iwe na ufanisi, lazima iwe ndefu na isiyo ya kawaida vya kutosha. Kama ilivyo kwa nenosiri dhabiti, ninapendekeza kuchagua passphrase ambayo ni ndefu na isiyo na mpangilio iwezekanavyo, yenye herufi, nambari na alama tofauti ili kufanya shambulio lolote la kikatili lisiwezekane.

Pia ni muhimu kuokoa vizuri passphrase hii, kwa njia sawa na maneno ya Mnemonic. **Kuipoteza kunamaanisha kupoteza ufikiaji wa bitcoins zako**. Ninashauri sana dhidi ya kukumbuka kwa moyo tu, kwani hii inaongeza hatari ya kupoteza bila sababu. Bora ni kuiandika kwenye nyenzo ya kimwili (karatasi au chuma) tofauti na maneno ya Mnemonic. Nakala hii lazima ihifadhiwe mahali tofauti na ambapo maneno yako ya Mnemonic yamehifadhiwa ili kuzuia zote mbili zisiathiriwe kwa wakati mmoja.

![CYP201](assets/fr/042.webp)

Katika sehemu ifuatayo, tutagundua jinsi Elements hizi mbili kwenye msingi wa Wallet yako - maneno ya Mnemonic na passphrase - hutumika kupata jozi muhimu zinazotumiwa katika _scriptPubKey_ zinazofunga UTXO zako.

# Uundaji wa Pochi za Bitcoin

<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>

## Uundaji wa seed na Ufunguo (Key) Mkuu

<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>

Mara tu maneno ya Mnemonic na passphrase ya hiari yanapozalishwa, mchakato wa kupata Bitcoin HD Wallet unaweza kuanza. Kifungu cha maneno cha Mnemonic Kina (depth)badilishwa kwanza kuwa seed ambayo ni msingi wa funguo zote za Wallet.

![CYP201](assets/fr/043.webp)

### seed ya HD Wallet

Kiwango cha BIP39 Kina (depth)fafanua seed kama mlolongo wa 512-bit, ambayo hutumika kama sehemu ya kuanzia ya kupata funguo zote za HD Wallet. seed inatokana na maneno ya Mnemonic na passphrase inayowezekana kwa kutumia algoriti ya **PBKDF2** (_Kazi 2_ ya Utoaji Muhimu wa Nenosiri 2_) ambayo tayari tumeijadili katika sura ya 3.3. Katika kazi hii ya derivation, tutatumia vigezo vifuatavyo:


- $m$ : maneno ya Mnemonic;
- $p$ : passphrase ya hiari iliyochaguliwa na mtumiaji ili kuimarisha usalama wa seed. Ikiwa hakuna passphrase, uwanja huu unaachwa tupu;
- $\text{PBKDF2}$ : chaguo la kukokotoa lenye $\text{HMAC-SHA512}$ na marudio ya $2048$;
- $s$: 512-bit Wallet seed.

Bila kujali urefu wa maneno ya Mnemonic uliochaguliwa (bits 132 au bits 264), kazi ya PBKDF2 itazalisha pato la 512-bit daima, na seed kwa hiyo itakuwa ya ukubwa huu daima.

### seed Derivation Scheme na PBKDF2

Mlinganyo ufuatao unaonyesha chimbuko la seed kutoka kwa maneno ya Mnemonic na passphrase:

$$
s = \text{PBKDF2}_{\text{HMAC-SHA512}}(m, p, 2048)
$$

![CYP201](assets/fr/044.webp)

Thamani ya seed inaathiriwa na thamani ya maneno ya Mnemonic na passphrase. Kwa kubadilisha passphrase, seed tofauti inapatikana. Hata hivyo, kwa maneno sawa ya Mnemonic na passphrase, seed sawa daima huzalishwa, kwani PBKDF2 ni kazi ya kuamua. Hii inahakikisha kwamba jozi sawa za funguo zinaweza kurejeshwa kupitia nakala zetu.

**Kumbuka:** Katika lugha ya kawaida, neno "seed" mara nyingi hurejelea, kwa matumizi mabaya ya lugha, kwa maneno ya Mnemonic. Hakika, kwa kukosekana kwa passphrase, moja ni encoding ya nyingine. Walakini, kama tulivyoona, katika ukweli wa kiufundi wa Wallet, seed na kifungu cha Mnemonic kwa kweli ni Elements mbili tofauti.

Kwa kuwa sasa tuna seed yetu, tunaweza kuendelea na utengenezaji wa Bitcoin Wallet yetu.

### Ufunguo Mkuu (Master Key)na Msimbo wa Mnyororo Mkuu

Mara tu seed inapopatikana, hatua inayofuata katika kupata HD Wallet inahusisha kukokotoa Ufunguo Mkuu (Master Key)wa faragha na msimbo mkuu wa mnyororo, ambao utawakilisha Kina (depth) cha 0 cha Wallet yetu.

Ili kupata Ufunguo Mkuu (Master Key)wa faragha na msimbo mkuu wa mnyororo, chaguo la kukokotoa la HMAC-SHA512 linatumika kwa seed, kwa kutumia Ufunguo (Key) maalum "_Bitcoin Seed_" unaofanana kwa watumiaji wote wa Bitcoin. Hii mara kwa mara imechaguliwa ili kuhakikisha kwamba derivations muhimu ni maalum kwa Bitcoin. Hapa kuna Elements:


- $\text{HMAC-SHA512}$: kipengele cha kukokotoa;
- $s$: 512-bit Wallet seed;
- $\text{"Bitcoin seed"}$: Toleo (version) la kawaida la pochi zote za Bitcoin.

$$
\text{output} = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)
$$

Matokeo ya chaguo hili la kukokotoa ni biti 512. Kisha imegawanywa katika sehemu 2:


- Bits 256 za kushoto huunda **Ufunguo (Key) mkuu wa faragha**;
- Bits 256 za kulia huunda **msimbo mkuu wa mnyororo**.

Kihesabu, maadili haya mawili yanaweza kutambuliwa kama ifuatavyo na $k_M$ kuwa Ufunguo Mkuu (Master Key)wa faragha na $C_M$ msimbo mkuu wa mnyororo:

$$
k_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[:256]}
$$

$$
C_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[256:]}
$$

![CYP201](assets/fr/045.webp)

### Jukumu la Ufunguo Mkuu (Master Key)na Msimbo wa Mnyororo

Ufunguo (Key) wa kibinafsi wa bwana unachukuliwa kuwa Ufunguo (Key) wa mzazi, ambapo funguo zote za kibinafsi - watoto, wajukuu, wajukuu, nk - zitatolewa. Inawakilisha kiwango cha sifuri katika safu ya utokaji.

Nambari kuu ya mnyororo, kwa upande mwingine, inaleta chanzo cha ziada cha entropy katika mchakato muhimu wa uundaji wa watoto, ili kukabiliana na mashambulizi fulani yanayoweza kutokea. Zaidi ya hayo, katika HD Wallet, kila jozi ya funguo ina msimbo wa kipekee wa mnyororo unaohusishwa nayo, ambayo pia hutumiwa kupata funguo za watoto kutoka kwa jozi hii, lakini tutajadili hili kwa undani zaidi katika sura zinazoja.

Kabla ya kuendelea na utengenezaji wa HD Wallet na Elements ifuatayo, napenda, katika sura inayofuata, kukujulisha kwa funguo zilizopanuliwa, ambazo mara nyingi huchanganyikiwa na Ufunguo (Key) mkuu. Tutaona jinsi yanavyojengwa na ni jukumu gani wanacheza katika Bitcoin Wallet.

## Funguo Zilizopanuliwa

<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>

Ufunguo (Key) uliopanuliwa ni muunganisho wa Ufunguo (Key) (iwe wa faragha au wa umma) na msimbo wake wa mnyororo unaohusishwa. Msimbo huu wa mnyororo ni muhimu kwa upataji wa funguo za watoto kwa sababu, bila hiyo, haiwezekani kupata funguo za watoto kutoka kwa Ufunguo (Key) wa mzazi, lakini tutagundua mchakato huu kwa usahihi zaidi katika sura inayofuata. Vifunguo hivi vilivyopanuliwa hivyo huruhusu kujumlisha taarifa zote muhimu ili kupata funguo za watoto, na hivyo kurahisisha usimamizi wa Akaunti (Account) ndani ya HD Wallet.

![CYP201](assets/fr/046.webp)

Ufunguo (Key) uliopanuliwa una sehemu mbili:


- Upakiaji, ambao una Ufunguo (Key) wa kibinafsi au wa umma pamoja na msimbo wa mnyororo unaohusishwa;
- Metadata, ambayo ni vipande mbalimbali vya maelezo ili kuwezesha ushirikiano kati ya programu na kuboresha uelewa wa mtumiaji.

### Jinsi Vifunguo Vilivyopanuliwa Hufanya Kazi

Wakati Ufunguo (Key) uliopanuliwa una Ufunguo (Key) wa faragha, unajulikana kama Ufunguo (Key) wa faragha uliopanuliwa. Inatambulika kwa kiambishi awali chake ambacho Kina (depth) kutaja `prv`. Kando na Ufunguo (Key) wa faragha, Ufunguo (Key) wa faragha uliopanuliwa pia una msimbo wa mnyororo unaohusishwa. Kwa aina hii ya Ufunguo (Key) uliopanuliwa, inawezekana kupata aina zote za funguo za kibinafsi za mtoto, na kwa hiyo kwa kuongeza na mara mbili ya pointi kwenye curve za mviringo, pia inaruhusu kupatikana kwa ukamilifu wa funguo za umma za watoto.

Wakati Ufunguo (Key) uliopanuliwa hauna Ufunguo (Key) wa faragha, lakini badala yake, Ufunguo (Key) wa umma, unajulikana kama Ufunguo (Key) wa umma uliopanuliwa. Inatambulika kwa kiambishi awali chake ambacho Kina (depth) kutaja `pub`. Kwa wazi, pamoja na Ufunguo (Key), pia ina msimbo wa mnyororo unaohusishwa. Tofauti na Ufunguo (Key) wa faragha uliopanuliwa, Ufunguo (Key) wa umma uliopanuliwa huruhusu kupatikana kwa funguo za umma za "kawaida" pekee za watoto (maana haiwezi kupata funguo "zilizo ngumu" za watoto). Tutaona katika sura ifuatayo maana ya sifa hizi za "kawaida" na "zigumu".

Lakini kwa hali yoyote, Ufunguo (Key) wa umma uliopanuliwa hauruhusu kupatikana kwa funguo za kibinafsi za mtoto. Kwa hivyo, hata kama mtu anaweza kufikia `xpub`, hataweza kutumia pesa zinazohusika, kwani hatakuwa na ufikiaji wa funguo za kibinafsi zinazolingana. Wanaweza tu kupata funguo za umma za watoto ili kuangalia shughuli zinazohusiana.

Kwa yafuatayo, tutapitisha nukuu ifuatayo:


- $K_{\text{PAR}}$: Ufunguo (Key) wa umma wa mzazi;
- $k_{\text{PAR}}$: Ufunguo (Key) wa faragha wa mzazi;
- $C_{\text{PAR}}$: msimbo wa mnyororo wa mzazi;
- $C_{\text{CHD}}$: msimbo wa mnyororo wa watoto;
- $K_{\text{CHD}}^n$: Ufunguo (Key) wa kawaida wa umma wa mtoto;
- $k_{\text{CHD}}^n$: Ufunguo (Key) wa faragha wa kawaida wa mtoto;
- $K_{\text{CHD}}^h$: Ufunguo (Key) mgumu wa umma wa mtoto;
- $k_{\text{CHD}}^h$: Ufunguo (Key) mgumu wa faragha wa mtoto.

![CYP201](assets/fr/047.webp)

### Ujenzi wa Ufunguo (Key) Uliopanuliwa

Ufunguo (Key) uliopanuliwa umeundwa kama ifuatavyo:


- **Toleo (version)**: Msimbo wa Toleo (version) ili kutambua asili ya Ufunguo (Key) (`xprv`, `xpub`, `yprv`, `ypub`...). Tutaona mwishoni mwa sura hii herufi `x`, `y`, na `z` zinahusiana nini.
- **Kina (depth)**: Kiwango cha daraja katika HD Wallet kuhusiana na Ufunguo Mkuu (Master Key)(0 kwa Ufunguo (Key) mkuu).
- **NambarAlama ya Kidole ya Mzazi (Parent Fingerprint)**: Baiti 4 za kwanza za HASH160 Hash za Ufunguo (Key) kuu wa umma zilizotumiwa kupata Ufunguo (Key) uliopo kwenye mzigo.
- **Nambari ya Fahirisi (Index Number)**: Kitambulisho cha mtoto kati ya funguo za ndugu, yaani, kati ya funguo zote zilizo katika kiwango sawa cha utokaji ambazo zina funguo za mzazi sawa.
- **Msimbo wa Chain (Chain Code)**: Msimbo wa kipekee wa baiti 32 wa kupata funguo za watoto.
- **Ufunguo (Key)**: Kitufe cha faragha (Private Key) (kilichoamrishwa na baiti 1 kwa saizi) au Kitufe cha umma (Public Key).
- **Checksum**: Thamani ya hundi inayokokotolewa na chaguo za kukokotoa za HASH256 (SHA256 mbili) pia huongezwa, ambayo inaruhusu uthibitishaji wa uadilifu wa Ufunguo (Key) uliopanuliwa wakati wa uwasilishaji au uhifadhi wake.

Umbizo kamili la Ufunguo (Key) uliopanuliwa kwa hivyo ni bytes 78 bila cheki, na bytes 82 zilizo na hundi. Kisha inabadilishwa kuwa Base58 ili kutoa uwakilishi ambao unaweza kusomeka kwa urahisi na watumiaji. Umbizo la Base58 ni sawa na lile linalotumika kwa anwani za kupokea *Legacy* (kabla ya *SegWit*).

| Element           | Maelezo                                                                                                         | Ukubwa      |
| ----------------- | --------------------------------------------------------------------------------------------------------------- | --------- |
| Version           | Inaonyesha ikiwa ufunguo ni wa umma (`xpub`, `ypub`) au binafsi (`xprv`, `zprv`), na pia toleo la extended key | 4 bytes   |
| Depth             | Ngazi katika mfumo ukilinganisha na ufunguo mkuu                                                              | 1 byte    |
| Parent Fingerprint| Bytes 4 za kwanza za HASH160 ya ufunguo wa umma wa mzazi                                                      | 4 bytes   |
| Index Number      | Nafasi ya ufunguo katika mpangilio wa watoto                                                                  | 4 bytes   |
| Chain Code        | Hutumika kutoa funguo za watoto                                                                               | 32 bytes  |
| Key               | Ufunguo wa binafsi (na prefix ya byte 1) au ufunguo wa umma                                                  | 33 bytes  |
| Checksum          | Checksum kuhakikisha utimilifu                                                                                | 4 bytes   |

Ikiwa byte moja itaongezwa kwa Ufunguo (Key) wa faragha pekee, ni kwa sababu Ufunguo (Key) wa umma uliobanwa ni mrefu kuliko Ufunguo (Key) wa faragha kwa byte moja. Byte hii ya ziada, iliyoongezwa mwanzoni mwa Ufunguo (Key) wa faragha kama `0x00`, inasawazisha ukubwa wao, na kuhakikisha kwamba upakiaji wa Ufunguo (Key) uliopanuliwa ni wa urefu sawa, iwe ni Ufunguo (Key) wa umma au wa faragha.

### Viambishi Muhimu Vilivyopanuliwa

Kama tulivyoona, vitufe vilivyopanuliwa vinajumuisha kiambishi awali Kina (depth)choonyesha Toleo (version) la Ufunguo (Key) uliopanuliwa na asili yake. Nukuu `pub` inaonyesha kuwa inarejelea Ufunguo (Key) uliopanuliwa wa umma, na nukuu `prv` inaonyesha Ufunguo (Key) wa faragha uliopanuliwa. Barua ya ziada kwenye msingi wa Ufunguo (Key) uliopanuliwa husaidia kuonyesha ikiwa kiwango Kina (depth)chofuatwa ni Legacy, SegWit v0, SegWit v1, nk.

Huu hapa ni muhtasari wa viambishi awali vilivyotumika na maana zake:

| Base 58 Prefix  | Base 16 Prefix  | Mtandao | Kusudi (Purpose)             | Hati Zinazohusishwa  | Derivation (Utoaji)   | Key Type (Aina ya Ufunguo (Key)) |
| --------------- | --------------- | ------- | ------------------- | ------------------- | --------------------- | ------------ |
| `xpub`          | `0488b21e`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | public       |
| `xprv`          | `0488ade4`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | private      |
| `tpub`          | `043587cf`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | public       |
| `tprv`          | `04358394`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | private      |
| `ypub`          | `049d7cb2`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | public       |
| `yprv`          | `049d7878`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | private      |
| `upub`          | `049d7cb2`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | public       |
| `uprv`          | `044a4e28`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | private      |
| `zpub`          | `04b24746`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | public       |
| `zprv`          | `04b2430c`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | private      |
| `vpub`          | `045f1cf6`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | public       |
| `vprv`          | `045f18bc`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | private      |



### Maelezo ya Ufunguo (Key) Uliopanuliwa wa Elements

Ili kuelewa vyema muundo wa ndani wa Ufunguo (Key) uliopanuliwa, hebu tuchukue moja kama mfano na kuivunja. Hapa kuna Ufunguo (Key) uliopanuliwa:


- Katika Base58**:

```text
xpub6CTNzMUkzpurBWaT4HQoYzLP4uBbGJuWY358Rj7rauiw4rMHCyq3Rfy9w4kyJXJzeFfyrKLUar2rUCukSiDQFa7roTwzjiAhyQAdPLEjqHT
```


- Katika heksadesimali**:

```text
0488B21E036D5601AD80000000C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A89303772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF50658051F067C3A
```

Ufunguo (Key) huu uliopanuliwa hugawanywa katika Elements kadhaa tofauti:

1.**Toleo (version)**: `0488B21E`

Bytes 4 za kwanza ni Toleo (version). Hapa, inalingana na Ufunguo (Key) uliopanuliwa wa umma kwenye Mainnet wenye madhumuni ya kupata *Legacy* au *SegWit v1*.

2.**Kina (depth)**: `03`

Sehemu hii inaonyesha kiwango cha daraja la Ufunguo (Key) ndani ya HD Wallet. Katika kesi hii, Kina (depth) cha `03` inamaanisha kuwa Ufunguo (Key) huu ni viwango vitatu vya unyambulishaji chini ya Ufunguo (Key) mkuu.

3.**Alama ya vidole ya mzazi**: `6D5601AD`

Hizi ndizo bytes 4 za kwanza za HASH160 Hash za Ufunguo (Key) kuu wa umma ambazo zilitumika kutengeneza `xpub` hii.

4.**Nambari ya faharasa**: `80000000`

Faharasa hii inaonyesha nafasi ya Ufunguo (Key) kati ya watoto wa mzazi wake. Kiambishi awali `0x80` Kina (depth)onyesha kuwa Ufunguo (Key) umetolewa kwa njia ngumu, na kwa kuwa iliyobaki imejaa sufuri, inaonyesha kuwa Ufunguo (Key) huu ni wa kwanza kati ya ndugu zake wanaowezekana.

5.**Msimbo wa mnyororo**: `C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A893`

6.**Ufunguo (Key) wa Umma**: `03772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF5065805`

7.**Cheki**: `1F067C3A`

Cheki inalingana na ka 4 za kwanza za Hash (mara mbili SHA256) ya kila kitu kingine.

Katika sura hii, tuligundua kuwa kuna aina mbili tofauti za funguo za watoto. Pia tulijifunza kuwa utokezaji wa funguo hizi za watoto unahitaji Ufunguo (Key) (wa faragha au wa umma) na msimbo wake wa mfululizo. Katika sura inayofuata, tutachunguza kwa undani asili ya aina hizi tofauti za funguo na jinsi ya kuzipata kutoka kwa Ufunguo (Key) wao wa mzazi na msimbo wa mnyororo.

## Utoaji wa Jozi Muhimu za Mtoto

<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>

Utoaji wa jozi za funguo za watoto katika pochi za Bitcoin HD hutegemea muundo wa kidaraja unaoruhusu kutoa idadi kubwa ya funguo, huku ukipanga jozi hizi katika vikundi tofauti kupitia matawi. Kila jozi ya watoto inayotokana na jozi ya wazazi inaweza kutumika moja kwa moja katika *scriptPubKey* kufunga bitcoins, au kama sehemu ya kuanzia kwa funguo zaidi za watoto za generate, na kadhalika, kuunda mti wa funguo.

MaToleo (version) haya yote huanza na Ufunguo Mkuu (Master Key)na msimbo mkuu, ambao ni wazazi wa kwanza katika kiwango cha Kina (depth) cha 0. Wao ni, kwa njia fulani, Adamu na Hawa wa funguo za Wallet yako, mababu wa kawaida wa funguo zote zinazotolewa.

![CYP201](assets/fr/048.webp)

Wacha tuchunguze jinsi uvumbuzi huu wa kiakili unavyofanya kazi.

### Aina Tofauti za MaToleo (version) Muhimu ya Mtoto

Kama tulivyogusia kwa ufupi katika sura iliyopita: funguo za watoto zimegawanywa katika aina kuu mbili:


- **Vifunguo vya watoto vya kawaida** ($k_{\text{CHD}}^n, K_{\text{CHD}}^n$): Hizi zimetolewa kutoka kwa Ufunguo (Key) uliopanuliwa wa umma ($K_{\text{PAR}}$), au Ufunguo (Key) wa faragha uliopanuliwa ($k_{\text{PAR}}$), kwa kupata Ufunguo (Key) wa umma kwanza.
- **Vifunguo ngumu vya watoto** ($k_{\text{CHD}}^h, K_{\text{CHD}}^h$): Hizi zinaweza tu kutolewa kutoka kwa Ufunguo (Key) wa faragha uliopanuliwa ($k_{\text{PAR}}}$) na kwa hivyo hazionekani kwa watazamaji ambao wana Ufunguo (Key) uliopanuliwa wa umma pekee.

Kila jozi ya vitufe vya mtoto hutambuliwa kwa **faharasa** ya biti 32 (inayoitwa $i$ katika hesabu zetu). Faharasa za vitufe vya kawaida huanzia $0$ hadi $2^{31}-1$, ilhali zile za funguo ngumu huanzia $2^{31}$ hadi $2^{32}-1$. Nambari hizi hutumika kutofautisha jozi muhimu za ndugu wakati wa utokaji. Hakika, kila jozi ya Ufunguo (Key) wa mzazi lazima iwe na uwezo wa kupata jozi nyingi za funguo za watoto. Ikiwa tungetumia hesabu sawa kwa utaratibu kutoka kwa funguo kuu, funguo zote za ndugu zilizopatikana zingekuwa sawa, ambayo haipendekewi. Kwa hivyo faharasa huleta kigezo ambacho hurekebisha hesabu ya uasilia, kuruhusu kila jozi ya ndugu kutofautishwa. Isipokuwa kwa matumizi mahususi katika baadhi ya itifaki na viwango vya utokaji, kwa ujumla tunaanza kwa kupata Ufunguo (Key) wa mtoto wa kwanza kwa faharasa `0`, ya pili na faharasa `1`, na kadhalika.

### Mchakato wa Utoaji na HMAC-SHA512

Utoaji wa kila Ufunguo (Key) wa mtoto unatokana na chaguo za kukokotoa za HMAC-SHA512, ambazo tulijadili katika Sehemu ya 2 kuhusu chaguo za kukokotoa za Hash. Inahitaji ingizo mbili: msimbo wa mnyororo wa mzazi $C_{\text{PAR}}$ na muunganisho wa Ufunguo (Key) wa mzazi (ama Ufunguo (Key) wa umma $K_{\text{PAR}}$ au Ufunguo (Key) wa faragha $k_{\text{PAR}}$, kulingana na aina ya Ufunguo (Key) wa mtoto unaotaka) na faharasa. Matokeo ya HMAC-SHA512 ni mlolongo wa 512-bit, umegawanywa katika sehemu mbili:


- **Bytes 32 za kwanza** (au $h_1$) hutumika kukokotoa jozi mpya ya watoto.
- **Bytes 32 za mwisho** (au $h_2$) hutumika kama msimbo mpya wa $C_{\text{CHD}}$ kwa jozi ya watoto.

Katika mahesabu yetu yote, nitaashiria $\text{Hash}$ pato la kazi ya HMAC-SHA512.

![CYP201](assets/fr/049.webp)

#### Utoaji wa Ufunguo (Key) wa Faragha wa Mtoto kutoka kwa Ufunguo (Key) wa Faragha wa Mzazi

Ili kupata Ufunguo (Key) wa faragha wa mtoto $k_{\text{CHD}}$ kutoka kwa Ufunguo (Key) wa faragha wa mzazi $k_{\text{PAR}}$, matukio mawili yanawezekana kulingana na kama Ufunguo (Key) mgumu au wa kawaida unahitajika.

Kwa **Ufunguo (Key) wa mtoto wa kawaida** ($i <2^{31}$), hesabu ya $\text{Hash}$ ni kama ifuatavyo:

$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, G \cdot k_{\text{PAR}} \Vert i)
$$

Katika hesabu hii, tunaona kwamba utendaji wetu wa HMAC huchukua pembejeo mbili: kwanza, msimbo wa mnyororo wa wazazi, na kisha uunganishaji wa faharasa na Ufunguo (Key) wa umma unaohusishwa na Ufunguo (Key) wa kibinafsi wa mzazi. Ufunguo (Key) wa umma wa mzazi unatumika hapa kwa sababu tunatazamia kupata Ufunguo (Key) wa kawaida wa mtoto, sio ugumu.

Sasa tunayo $\text{Hash}$ ya bytes 64 ambayo tutagawanya katika sehemu 2 za baiti 32 kila moja: $h_1$ na $h_2$:

$$
\text{hash} = h_1 \Vert h_2
$$

$$
h_1 = \text{hash}_{[:32]} \quad, \quad h_2 = \text{hash}_{[32:]}
$$

Ufunguo (Key) wa faragha wa mtoto $k_{\text{CHD}}^n$ kisha huhesabiwa kama ifuatavyo:

$$
k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n
$$

Katika hesabu hii, operesheni $\text{parse256}(h_1)$ inajumuisha kutafsiri baiti 32 za kwanza za $\text{Hash}$ kama nambari kamili ya bytes 256. Kisha nambari hii huongezwa kwa Ufunguo (Key) wa faragha wa mzazi, yote huchukuliwa modulo $n$ ili kukaa ndani ya mpangilio wa mkunjo wa duaradufu, kama tulivyoona katika sehemu ya 3 ya sahihi za dijitali. Kwa hivyo, ili kupata Ufunguo (Key) wa kibinafsi wa kawaida wa mtoto, ingawa Ufunguo (Key) wa umma wa mzazi hutumiwa kama msingi wa kuhesabu katika pembejeo za chaguo za kukokotoa za HMAC-SHA512, daima ni muhimu kuwa na Ufunguo (Key) wa faragha wa mzazi ili kukamilisha hesabu.

Kutoka kwa Ufunguo (Key) huu wa faragha wa mtoto, inawezekana kupata Ufunguo (Key) unaolingana wa umma kwa kutumia ECDSA au Schnorr. Kwa njia hii, tunapata jozi kamili ya funguo.

Kisha, sehemu ya pili ya $\text{Hash}$ inafasiriwa kwa urahisi kuwa msimbo wa mnyororo wa jozi ya vitufe vya mtoto ambayo tumetoa hivi punde:

$$
C_{\text{CHD}} = h_2
$$

Hapa kuna uwakilishi wa kimkakati wa derivation ya jumla:

![CYP201](assets/fr/050.webp)

Kwa **Ufunguo (Key) mgumu wa mtoto** ($i \geq 2^{31}$), hesabu ya $\text{Hash}$ ni kama ifuatavyo:

$$
hash = \text{HMAC-SHA512}(C_{\text{PAR}}, 0x00 \Vert k_{\text{PAR}} \Vert i)
$$

Katika hesabu hii, tunaona kwamba kazi yetu ya HMAC inachukua pembejeo mbili: kwanza, msimbo wa mnyororo wa wazazi, na kisha uunganishaji wa faharisi na Ufunguo (Key) wa kibinafsi wa mzazi. Ufunguo (Key) wa faragha wa mzazi unatumika hapa kwa sababu tunatazamia kupata Ufunguo (Key) mgumu wa mtoto. Zaidi ya hayo, baiti sawa na `0x00` huongezwa mwanzoni mwa Ufunguo (Key). Uendeshaji huu unasawazisha urefu wake ili ulingane na ule wa Ufunguo (Key) wa umma uliobanwa.

Kwa hivyo, sasa tuna 64-byte $\text{Hash}$ ambayo tutagawanya katika sehemu 2 za baiti 32 kila moja: $h_1$ na $h_2$:

$$
\text{hash} = h_1 \Vert h_2
$$

$$
h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]
$$

Ufunguo (Key) wa faragha wa mtoto $k_{\text{CHD}}^h$ kisha huhesabiwa kama ifuatavyo:

$$
k_{\text{CHD}}^h = \text{parse256}(h_1) + k_{\text{PAR}} \mod n
$$

Kisha, tunatafsiri kwa urahisi sehemu ya pili ya $\text{Hash}$ kuwa msimbo wa mnyororo wa jozi ya funguo za watoto ambazo tumetoa hivi punde:

$$
C_{\text{CHD}} = h_2
$$

Hapa kuna uwakilishi wa kimkakati wa derivation ya jumla:

![CYP201](assets/fr/051.webp)

Tunaweza kuona kwamba unyambulishaji wa kawaida na utendakazi wa utokaji mgumu kwa njia ile ile, na tofauti hii: unyambulishaji wa kawaida hutumia Ufunguo (Key) wa umma wa mzazi kama ingizo la chaguo la kukokotoa la HMAC, ilhali unyambulishaji mgumu hutumia Ufunguo (Key) wa kibinafsi wa mzazi.

#### Inaleta Ufunguo (Key) wa umma wa mtoto kutoka kwa Ufunguo (Key) wa umma wa mzazi

Iwapo tunajua Ufunguo (Key) wa umma wa mzazi $K_{\text{PAR}}$ na msimbo wa mnyororo unaohusishwa $C_{\text{PAR}}$, yaani, Ufunguo (Key) wa umma uliopanuliwa, inawezekana kupata funguo za umma za watoto $K_{\text{CHD}}^n$, lakini kwa funguo za kawaida za mtoto pekee (zisizo ngumu). Kanuni hii inaruhusu ufuatiliaji wa mienendo ya Akaunti (Account) katika Bitcoin Wallet kutoka `xpub` (*watch-pekee*).

Ili kufanya hesabu hii, tutakusanya $\text{Hash}$ na faharasa $i <2^{31}$ (chini ya kawaida):

$$
\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, K_{\text{PAR}} \Vert i)
$$

Katika hesabu hii, tunaona kwamba utendaji wetu wa HMAC huchukua pembejeo mbili: kwanza msimbo wa mnyororo wa wazazi, kisha uunganishaji wa faharasa na Ufunguo (Key) wa umma wa mzazi.

Kwa hivyo, sasa tuna $Hash$ ya bytes 64 ambazo tutagawanya katika sehemu 2 za bytes 32 kila moja: $h_1$ na $h_2$:

$$
\text{hash} = h_1 \Vert h_2
$$

$$
h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]
$$

Ufunguo (Key) wa umma wa mtoto $K_{\text{CHD}}^n$ kisha huhesabiwa kama ifuatavyo:

$$
K_{\text{CHD}}^n = G \cdot \text{parse256}(h_1) + K_{\text{PAR}}
$$

Ikiwa $\text{parse256}(h_1) \geq n$ (mpangilio wa mkunjo wa duaradufu) au ikiwa $K_{\text{CHD}}^n$ ndio sehemu ya infinity, unyambulishaji si sahihi, na ni lazima uchaguliwe faharasa nyingine.

Katika hesabu hii, operesheni $\text{parse256}(h_1)$ inahusisha kutafsiri bytes 32 za kwanza za $\text{Hash}$ kama nambari kamili ya bits 256. Nambari hii inatumika kukokotoa ncha kwenye mduara wa duaradufu kupitia kujumlisha na kuzidisha mara mbili kutoka kwa uhakika wa jenereta $G$. Hatua hii inaongezwa kwa Ufunguo (Key) wa umma wa mzazi ili kupata Ufunguo (Key) wa kawaida wa umma wa mtoto. Kwa hivyo, ili kupata Ufunguo (Key) wa umma wa kawaida wa mtoto, Ufunguo (Key) wa umma tu wa mzazi na msimbo wa mnyororo wa mzazi ni muhimu; Ufunguo (Key) wa faragha wa mzazi hauji katika mchakato huu, tofauti na hesabu ya Ufunguo (Key) wa faragha wa mtoto tulioona hapo awali.

Ifuatayo, nambari ya mnyororo wa watoto ni rahisi:

$$
C_{\text{CHD}} = h_2
$$

Hapa kuna uwakilishi wa kimkakati wa derivation ya jumla:

![CYP201](assets/fr/052.webp)

### Mawasiliano kati ya funguo za umma na za kibinafsi za watoto

Swali linaloweza kujitokeza ni jinsi Ufunguo (Key) wa umma wa kawaida wa mtoto unaotokana na Ufunguo (Key) wa umma wa mzazi unavyoweza kuwiana na Ufunguo (Key) wa faragha wa kawaida wa mtoto unaotokana na Ufunguo (Key) wa faragha wa mzazi unaolingana. Kiungo hiki Kina (depth)hakikishwa kwa usahihi na mali ya curves ya mviringo. Hakika, kupata Ufunguo (Key) wa kawaida wa umma wa mtoto, HMAC-SHA512 inatumika kwa njia ile ile, lakini matokeo yake hutumiwa tofauti:


   - **Ufunguo (Key) wa faragha wa kawaida wa mtoto**: $k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n$
   - **Ufunguo (Key) wa kawaida wa umma wa mtoto**: $K_{\text{CHD}}^n = G \cdot \text{parse256}(h_1) + K_{\text{PAR}}$

Shukrani kwa uongezaji na utendakazi maradufu kwenye curve ya duaradufu, mbinu zote mbili hutoa matokeo thabiti: Ufunguo (Key) wa umma unaotokana na Ufunguo (Key) wa faragha wa mtoto unafanana na Ufunguo (Key) wa umma wa mtoto unaotolewa moja kwa moja kutoka kwa Ufunguo (Key) wa umma wa mzazi.

### Muhtasari wa aina za derivation

Kwa muhtasari, hapa kuna aina tofauti zinazowezekana za derivations:

$$
\begin{array}{|c|c|c|c|}
\hline
\rightarrow & \text{PAR} & \text{CHD} & \text{n/h} \\
\hline
k_{\text{PAR}} \rightarrow k_{\text{CHD}} & k_{\text{PAR}} & \{ k_{\text{CHD}}^n, k_{\text{CHD}}^h \} & \{ n, h \} \\
k_{\text{PAR}} \rightarrow K_{\text{CHD}} & k_{\text{PAR}} & \{ K_{\text{CHD}}^n, K_{\text{CHD}}^h \} & \{ n, h \} \\
K_{\text{PAR}} \rightarrow k_{\text{CHD}} & K_{\text{PAR}} & \times & \times \\
K_{\text{PAR}} \rightarrow K_{\text{CHD}} & K_{\text{PAR}} & K_{\text{CHD}}^n & n \\
\hline
\end{array}
$$

Kwa muhtasari, hadi sasa umejifunza kuunda Elements ya msingi ya HD Wallet: maneno ya Mnemonic, seed, na kisha Ufunguo Mkuu (Master Key)na msimbo wa mnyororo mkuu. Pia umegundua jinsi ya kupata jozi muhimu za watoto katika sura hii. Katika sura inayofuata, tutachunguza jinsi viToleo (version) hivi vimepangwa katika pochi za Bitcoin na ni muundo gani wa kufuata ili kupata anwani zinazopokea pamoja na jozi muhimu zinazotumiwa katika *scriptPubKey* na *scriptSig*.

## Wallet Muundo na Njia za Utoaji

<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>

Muundo wa hierarkia wa pochi za HD kwenye Bitcoin inaruhusu shirika la jozi muhimu kwa njia mbalimbali. Wazo ni kupata, kutoka kwa Ufunguo Mkuu (Master Key)wa kibinafsi na nambari ya mnyororo mkuu, viwango kadhaa vya Kina (depth). Kila ngazi iliyoongezwa inalingana na kupatikana kwa jozi ya Ufunguo (Key) wa mtoto kutoka kwa jozi ya Ufunguo (Key) wa mzazi.

Baada ya muda, BIP tofauti zimeanzisha viwango vya njia hizi za utokaji, zikilenga kusawazisha matumizi yao kwenye programu tofauti. Kwa hiyo, katika sura hii, tutagundua maana ya kila ngazi ya derivation katika pochi za HD, kulingana na viwango hivi.

### Undani wa Utoaji wa HD Wallet

Njia za utokaji zimepangwa katika tabaka za Kina (depth), kuanzia Kina (depth) 0, ambacho Kina (depth)wakilisha Ufunguo Mkuu (Master Key)na msimbo mkuu wa chain, hadi tabaka za viwango vidogo vya kupata anwani zinazotumiwa kufunga UTXO. BIPs (*Mapendekezo ya Uboreshaji ya Bitcoin*) hufafanua viwango kwa kila Layer, ambayo husaidia kuoanisha mazoea katika programu mbalimbali za usimamizi wa Wallet.

Kwa hivyo, njia ya utokaji inarejelea mlolongo wa fahirisi zinazotumiwa kupata funguo za watoto kutoka kwa Ufunguo (Key) mkuu.

**Kina (depth) 0: Ufunguo Mkuu (Master Key)(BIP32)**

Kina (depth) hiki Kina (depth)lingana na Ufunguo Mkuu (Master Key)wa faragha wa Wallet na msimbo mkuu wa mnyororo. Inawakilishwa na nukuu $m/$.

**Kina (depth) 1: Kusudi (Purpose) (BIP43)**

Kusudi (Purpose) huamua muundo wa kimantiki wa derivation. Kwa mfano, P2WPKH Address itakuwa na $/84'/$ kwa Kina (depth) 1 (kulingana na BIP84), wakati P2TR Address itakuwa na $/86'/$ (kulingana na BIP86). Layer hii inawezesha utangamano kati ya pochi kwa kuonyesha nambari za fahirisi zinazolingana na nambari za BIP.

Kwa maneno mengine, mara tu unapokuwa na Ufunguo Mkuu (Master Key)na msimbo mkuu, hizi hutumika kama jozi ya Ufunguo (Key) wa mzazi ili kupata jozi ya vitufe vya mtoto. Faharasa inayotumika katika utohozi huu inaweza kuwa, kwa mfano, $/84'/$ ikiwa Wallet inaKusudi (Purpose)wa kutumia hati za aina ya SegWit v0. Jozi hii muhimu basi iko kwenye Kina (depth) cha 1. Jukumu lake si kufunga bitcoins, lakini kutumika tu kama njia katika uongozi wa derivation.

**Kina (depth) 2: Aina ya Sarafu (BIP44)**

Kutoka kwa jozi muhimu kwa Kina (depth) 1, derivation mpya inafanywa ili kupata jozi muhimu kwa Kina (depth) 2. Kina (depth) hiki Kina (depth)ruhusu kutofautisha Akaunti (Account) za Bitcoin kutoka kwa fedha nyingine za crypto ndani ya Wallet sawa.

Kila sarafu ina faharasa ya kipekee ili kuhakikisha uoanifu katika pochi za sarafu nyingi. Kwa mfano, kwa Bitcoin, faharasa ni $/0'/$ (au `0x80000000` katika nukuu ya hexadecimal). Faharasa za sarafu huchaguliwa katika safu kutoka $2^{31}$ hadi $2^{32}-1$ ili kuhakikisha utokaji mgumu.

Ili kukupa mifano mingine, hapa kuna faharasa za baadhi ya sarafu:


- $1'$ (`0x80000001`) kwa bitcoins za Testnet;
- $2'$ (`0x80000002`) kwa Litecoin;
- $60'$ (`0x8000003c`) kwa Ethereum...

**Kina (depth) 3: Akaunti (Account) (BIP32)**

Kila Wallet inaweza kugawanywa katika Akaunti (Account) kadhaa, kuhesabiwa kutoka $2^{31}$, na kuwakilishwa kwa Kina (depth) 3 na $/0'/$ kwa Akaunti (Account) ya kwanza, $/1'/$ kwa ya pili, na kadhalika. Kwa ujumla, unaporejelea Ufunguo (Key) uliopanuliwa `xpub`, hurejelea funguo zilizo katika Kina (depth) hiki cha unyambulishaji.

Mgawanyo huu katika Akaunti (Account) tofauti ni wa hiari. Inalenga kurahisisha shirika la Wallet kwa watumiaji. Katika mazoezi, mara nyingi Akaunti (Account) moja tu hutumiwa, kwa kawaida ya kwanza kwa default. Hata hivyo, katika baadhi ya matukio, ikiwa mtu anataka kutofautisha wazi jozi muhimu kwa matumizi tofauti, hii inaweza kuwa na manufaa. Kwa mfano, inawezekana kuunda Akaunti (Account) ya kibinafsi na Akaunti (Account) ya kitaaluma kutoka kwa seed sawa, na makundi tofauti kabisa ya funguo kutoka kwa Kina (depth) hiki cha derivation.

**Kina (depth) 4: Mnyororo (BIP32)**

Kila Akaunti (Account) iliyofafanuliwa kwa Kina (depth) 3 basi imeundwa katika minyororo miwili:


- **Msururu wa nje**: Katika msururu huu, zile zinazojulikana kama anwani za "umma" zimetolewa. Anwani hizi za kupokea zimeKusudi (Purpose)wa kufunga UTXO zinazotoka kwa miamala ya nje (yaani, inayotokana na utumiaji wa UTXO ambazo si zako). Ili kuiweka kwa urahisi, mlolongo huu wa nje hutumiwa wakati wowote mtu anataka kupokea bitcoins. Unapobofya "*pokea*" katika programu yako ya Wallet, daima ni Address kutoka kwa msururu wa nje unaotolewa kwako. Mlolongo huu unawakilishwa na jozi ya vitufe vinavyotokana na faharasa $/0/$.
- **Msururu wa ndani (mabadiliko)**: Msururu huu umehifadhiwa kwa ajili ya kupokea anwani zinazofunga bitcoins zinazotoka kwa matumizi ya UTXO ambazo ni zako, kwa maneno mengine, kubadilisha anwani. Inatambuliwa na faharasa $/1/$.

**Kina (depth) 5: Kielezo cha Address (Address Index) (BIP32)**

Hatimaye, Kina (depth) cha 5 Kina (depth)wakilisha hatua ya mwisho ya utokaji katika Wallet. Ingawa kitaalam inawezekana kuendelea kwa muda usiojulikana, viwango vya sasa vinakomea hapa. Katika Kina (depth) hiki cha mwisho, jozi za funguo ambazo kwa kweli zitatumika kufunga na kufungua UTXO zimetolewa. Kila index inaruhusu kutofautisha kati ya jozi muhimu za ndugu: kwa hivyo, ya kwanza kupokea Address itatumia index $/0/$, pili index $/1/$, na kadhalika.

![CYP201](assets/fr/053.webp)

### Nukuu ya Njia za Utokaji

Njia ya utokaji imeandikwa kwa kutenganisha kila ngazi kwa kufyeka ($/$). Kwa hivyo kila kufyeka kunaonyesha kutolewa kwa jozi ya vitufe vya mzazi ($k_{\text{PAR}}$, $K_{\text{PAR}}$, $C_{\text{PAR}}$) kwa jozi ya vitufe vya mtoto ($k_{\text{CHD}}$, $K_{\text{CHD}}$, $C_{\text).{CHD}} Nambari iliyobainishwa katika kila Kina (depth) inalingana na faharasa inayotumiwa kupata Ufunguo (Key) huu kutoka kwa wazazi wake. Kiapostrofi ($'$) wakati mwingine huwekwa upande wa kulia wa faharasa huonyesha utohozi mgumu ($k_{\text{CHD}}^h$, $K_{\text{CHD}}^h$). Wakati mwingine, apostrofi hii inabadilishwa na $h$. Kwa kukosekana kwa neno la kiapostrofi au $h$, kwa hiyo ni uasiliaji wa kawaida ($k_{\text{CHD}}^n$, $K_{\text{CHD}}^n$).

Kama tulivyoona katika sura zilizopita, faharasa muhimu ngumu zinaanzia $2^{31}$, au `0x80000000` katika hexadecimal. Kwa hivyo, faharasa inapofuatwa na kiapostrofi katika njia ya utokaji, $2^{31}$ lazima iongezwe kwa nambari iliyoonyeshwa ili kupata thamani halisi inayotumika katika chaguo za kukokotoa za HMAC-SHA512. Kwa mfano, ikiwa njia ya unyambulishaji inabainisha $/44'/$, faharasa halisi itakuwa:

$$
i = 44 + 2^{31} = 2\,147\,483\,692
$$

Katika heksadesimali, hii ni `0x8000002C`.

Sasa kwa kuwa tumeelewa kanuni kuu za njia za derivation, hebu tuchukue mfano! Hapa kuna njia ya kupata Bitcoin inayopokea Address:

$$
m / 84' / 0' / 1' / 0 / 7
$$

Katika mfano huu:


- $84'$ inaonyesha kiwango cha P2WPKH (SegWit v0);
- $0'$ inaonyesha sarafu ya Bitcoin kwenye Mainnet;
- $ 1'$ inalingana na Akaunti (Account) ya pili katika Wallet;
- $0$ inaonyesha kuwa Address iko kwenye mlolongo wa nje;
- $7$ inaonyesha Address ya 8 ya nje ya Akaunti (Account) hii.

### Muhtasari wa muundo wa derivation

| Kina (depth) | Maelezo            | Mfano wa Kiwango                  |
| ----- | ------------------ | --------------------------------- |
| 0     | Ufunguo Mkuu (Master Key)        | $m/$                |
| 1     | Kusudi (Purpose)            | $/86'/$ (P2TR)           |
| 2     | Fedha           | $/0'/$ (Bitcoin)                  |
| 3     | Akaunti (Account)            | $/0'/$ (Akaunti (Account) ya kwanza)        |
| 4     | Mnyororo              | $/0/$ (nje) au $/1/$ (badilisha)  |
| 5     | ha Address (Address Index)      | $/0/$ (anwani ya kwanza)          |

Katika sura inayofuata, tutagundua "*vielezi vya hati ya pato*" ni nini, uvumbuzi ulioanzishwa hivi majuzi katika Bitcoin Core ambao hurahisisha hifadhi rudufu ya Bitcoin Wallet.

## Vielezi vya hati ya pato

<chapterId>e4f1c2d3-9b8a-4d3e-8f2a-7b6c5d4e3f2a</chapterId>

Mara nyingi huambiwa kwamba maneno ya Mnemonic pekee yanatosha kurejesha upatikanaji wa Wallet. Kwa kweli, mambo ni magumu zaidi. Katika sura iliyopita, tuliangalia muundo wa derivation wa HD Wallet, na unaweza kuwa umeona kuwa mchakato huu ni ngumu sana. Njia za utokaji huambia programu mwelekeo wa kufuata ili kupata funguo za mtumiaji. Hata hivyo, wakati wa kurejesha Bitcoin Wallet, ikiwa mtu hajui njia hizi, maneno ya Mnemonic pekee haitoshi. Inaruhusu kupata Ufunguo Mkuu (Master Key)na msimbo mkuu wa chain, lakini ni muhimu kujua faharasa zinazotumiwa kufikia funguo za mtoto.

Kina (depth)dharia, itakuwa muhimu kuokoa sio tu maneno ya Mnemonic ya Wallet yetu lakini pia njia za Akaunti (Account) tunazotumia. Katika mazoezi, mara nyingi inawezekana kurejesha upatikanaji wa funguo za mtoto bila habari hii, ikiwa ni pamoja na kwamba viwango vimefuatwa. Kwa kupima kila kiwango moja baada ya nyingine, kwa ujumla inawezekana kupata tena upatikanaji wa bitcoins. Walakini, hii haijahakikishwa na ni ngumu sana kwa Kompyuta. Pia, pamoja na mseto wa aina za hati na kuibuka kwa usanidi changamano zaidi, maelezo haya yanaweza kuwa magumu kueleza, hivyo basi kubadilisha data hii kuwa taarifa ya faragha na vigumu kurejesha kwa nguvu ya kikatili. Hii ndiyo sababu uvumbuzi umeanzishwa hivi majuzi na unaanza kuunganishwa kwenye programu yako uipendayo ya Wallet: *vielezi vya hati ya pato*.

### "Descriptor" ni nini?

"*vifafanuzi vya hati ya pato*"("*output script descriptors*"), au kwa urahisi "*Descriptor*", ni semi zilizoundwa ambazo zinafafanua kikamilifu hati ya pato (*scriptPubKey*) na kutoa taarifa zote zinazohitajika ili kufuata miamala inayohusishwa na hati fulani. Huwezesha usimamizi wa funguo katika pochi za HD kwa kutoa maelezo sanifu na kamili ya muundo wa Wallet na aina za anwani zinazotumiwa.

Faida kuu ya Descriptor iko katika uwezo wao wa kuingiza taarifa zote muhimu ili kurejesha Wallet katika kamba moja (pamoja na maneno ya kurejesha). Kwa kuhifadhi descriptors na vifungu vinavyohusiana vya Mnemonic, inakuwa rahisi kurejesha funguo za faragha kwa kujua kwa usahihi nafasi yao katika uongozi. Kwa wallet za Multisig, ambazo nakala yake awali ilikuwa ngumu zaidi, descriptor inajumuisha `xpub` ya kila kipengele, hivyo basi kuhakikisha uwezekano wa kuunda upya anwani iwapo kutatokea tatizo.

### Ujenzi wa kielezi

Descriptor ina Elements kadhaa:


- Hati za kufanya kazi kama vile `pk` (*Pay-to-PubKey*), `pkh` (*Pay-to-PubKey-Hash*), `wpkh` (*Pay-to-Witness-PubKey-Hash*), `sh` (*Pay-to-Script-Hash*), `wsh`-GW-GW-8`, `wsh`-GW-8, `Wsh-Pay-8' (*-Wness-8) (*Pay-to-Taproot*), `multi` (*Sahihi nyingi*), na `sortedmulti` (*Sahihi nyingi zenye vitufe vilivyopangwa*);
- Njia za utokaji, kwa mfano, `[d34db33f/44h/0h/0h]` ambayo inaonyesha njia ya Akaunti (Account) inayotolewa na alama ya vidole ya Ufunguo Mkuu (Master Key)mahususi;
- Vifunguo katika miundo mbalimbali kama vile vitufe vya umma vya heksadesimali au vitufe vilivyopanuliwa vya umma (`xpub`);
- Cheki, ikitanguliwa na ishara ya Hash, ili kuthibitisha uadilifu wa kifafanuzi.

Kwa mfano, descriptor ya P2WPKH (SegWit v0) Wallet inaweza kuonekana kama:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7nr4
```

katika descriptor hii, chaguo la kukokotoa `wpkh` linaonyesha aina ya hati *Pay-to-Witness-Public-Key-Hash*. Inafuatwa na njia ya kupatikana ambayo ina:


- `cdeab12f`: alama ya vidole ya Ufunguo (Key) mkuu;
- `84h`: ambayo inaashiria matumizi ya madhumuni ya BIP84, yanayoKusudi (Purpose)wa kwa anwani za SegWit v0;
- `0h`: ambayo inaonyesha kuwa ni sarafu ya BTC kwenye Mainnet;
- `0h`: ambayo inarejelea nambari mahususi ya Akaunti (Account) iliyotumika katika Wallet.

Descriptor pia Kina (depth)jumuisha Ufunguo (Key) uliopanuliwa wa umma unaotumika katika Wallet hii:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Ifuatayo, nukuu `/<0;1>/*` hubainisha kuwa Descriptor hutengeneza anwani kutoka kwenye  chain ya nje(`0`) na chain ya ndani (`1`), na kadi-mwitu (`*`) ikiruhusu utokezi mfuatano wa anwani nyingi kwa njia inayoweza kusanidiwa, sawa na kudhibiti "kikomo cha pengo" kwenye programu ya jadi ya GW-6.

Hatimaye, `#jy0l7nr4` inawakilisha checksum ili kuthibitisha uadilifu wa descriptor.

Sasa unajua kila kitu kuhusu uendeshaji wa HD Wallet kwenye Bitcoin na mchakato wa kupata jozi muhimu. Hata hivyo, katika sura za mwisho, tulijiwekea mipaka kwa kizazi cha funguo za kibinafsi na za umma, bila kushughulikia ujenzi wa kupokea anwani. Hili litakuwa somo la sura inayofuata!

## Kupokea Anwani

<chapterId>ca80a89d-f8da-4e09-8c35-43179b65bced</chapterId>

Anwani za kupokea ni vipande vya maelezo yaliyopachikwa katika *scriptPubKey* ili kufunga UTXO zilizoundwa upya. Kuweka tu, Address hutumikia kupokea bitcoins. Hebu tuchunguze utendaji wao kuhusiana na yale ambayo tumejifunza katika sura zilizopita.

### Jukumu la Anwani za Bitcoin katika Hati

Kama ilivyoelezwa hapo awali, jukumu la shughuli ni kuhamisha Umiliki wa bitcoins kutoka kwa pembejeo hadi kwenye matokeo. Utaratibu huu unahusisha kutumia UTXO kama pembejeo huku ukiunda UTXO mpya kama matokeo. UTXO hizi zimehifadhiwa na maandiko, ambayo hufafanua hali muhimu za kufungua fedha.

Mtumiaji anapopokea bitcoins, mtumaji huunda Toleo (version) la UTXO na kuifunga kwa *scriptPubKey*. Hati hii ina sheria zinazobainisha saini na funguo za umma zinazohitajika ili kufungua UTXO hii. Ili kutumia UTXO hii katika muamala mpya, ni lazima mtumiaji atoe maelezo yaliyoombwa kupitia *scriptSig*. Utekelezaji wa *scriptSig* pamoja na *scriptPubKey* lazima urejeshe "kweli" au `1`. Ikiwa hali hii itafikiwa, UTXO inaweza kutumika kuunda UTXO mpya, yenyewe imefungwa na *scriptPubKey* mpya, na kadhalika.

![CYP201](assets/fr/054.webp)

Ni katika *scriptPubKey* ambapo anwani za kupokea zinapatikana. Walakini, matumizi yao hutofautiana kulingana na kiwango cha maandishi kilichopitishwa. Hapa kuna jedwali la muhtasari wa maelezo yaliyo katika *scriptPubKey* kulingana na kiwango Kina (depth)chotumiwa, pamoja na maelezo yanayotarajiwa katika *scriptSig* ili kufungua *scriptPubKey*.

| Standard (Kawaida) | *scriptPubKey*                                              | *scriptSig*                     | *Hati ya Redeem (redeem script)*     | *shahidi (witness)*                                |
| ------------------ | ----------------------------------------------------------- | ------------------------------- | ------------------- | ---------------------------------------- |
| P2PK               | `<pubkey> OP_CHECKSIG`                                      | `<signature>`                   |                     |                                          |
| P2PKH              | `OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG` | `<signature> <public key>`      |                     |                                          |
| P2SH               | `OP_HASH160 <scriptHash> OP_EQUAL`                          | `<data pushes> <Hati ya Redeem (redeem script) >` | Arbitrary data     |                                          |
| P2WPKH             | `0 <pubKeyHash>`                                            |                                 |                     | `<signature> <public key>`               |
| P2WSH              | `0 <witnessScriptHash>`                                     |                                 |                     | `<data pushes> <witness script>`         |
| P2SH-P2WPKH        | `OP_HASH160 <redeemScriptHash> OP_EQUAL`                    | `<Hati ya Redeem (redeem script) >`               | `0 <pubKeyHash>`    | `<signature> <public key>`               |
| P2SH-P2WSH         | `OP_HASH160 <redeemScriptHash> OP_EQUAL`                    | `<Hati ya Redeem (redeem script) >`               | `0 <scriptHash>`    | `<data pushes> <witness script>`         |
| P2TR (key path)    | `1 <public key>`                                            |                                 |                     | `<signature>`                            |
| P2TR (script path) | `1 <public key>`                                            |                                 |                     | `<data pushes> <script> <control block>` |

*Chanzo: Klabu ya ukaguzi ya Bitcoin Core PR, Julai 7, 2021 - Gloria Zhao*

Opcodes zinazotumiwa katika hati zimeundwa ili kudhibiti habari, na, ikiwa ni lazima, kulinganisha au kuipima. Wacha tuchukue mfano wa hati ya P2PKH, ambayo ni kama ifuatavyo.

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

Kama tutakavyoona katika sura hii, `<pubKeyHash>` inawakilisha mzigo wa Address inayopokea inayotumiwa kufunga UTXO. Ili kufungua *scriptPubKey* hii, ni muhimu kutoa *scriptSig* iliyo na:

```text
<signature> <public key>
```

Katika lugha ya hati, "bunda" ni muundo wa data wa "*LIFO*" ("*Last In, First Out*") unaotumika kuhifadhi kwa muda Elements wakati wa utekelezaji wa hati. Kila utendakazi wa hati huchezea rafu hii, ambapo Elements inaweza kuongezwa (*sukuma*) au kuondolewa (*pop*). Hati hutumia rafu hizi kutathmini vielezi, kuhifadhi vibadilisho vya muda, na kudhibiti hali.

Utekelezaji wa hati niliyotoa kama mfano unafuata mchakato huu:


- Tunayo *scriptSig*, *ScriptPubKey*, na stack:

![CYP201](assets/fr/055.webp)


- *scriptSig* inasukumwa kwenye rafu:

![CYP201](assets/fr/056.webp)


- `OP_DUP` inanakili Ufunguo (Key) wa umma uliotolewa katika *scriptSig* kwenye rafu:

![CYP201](assets/fr/057.webp)


- `OP_HASH160` hurejesha Hash ya Ufunguo (Key) wa umma ambao umenakiliwa hivi punde:

![CYP201](assets/fr/058.webp)


- `OP_PUSHBYTES_20 <pubKeyHash>` husukuma Bitcoin Address iliyo katika *scriptPubKey* kwenye rafu:

![CYP201](assets/fr/059.webp)


- `OP_EQUALVERIFY` inathibitisha kuwa Ufunguo (Key) wa umma uliopokewa unalingana na upokeaji wa Address uliotolewa:

![CYP201](assets/fr/060.webp)

`OP_CHECKSIG` hukagua saini iliyo katika *scriptSig* kwa kutumia Kitufe cha umma (Public Key). Opcode hii kimsingi hufanya uthibitishaji wa sahihi kama tulivyoeleza katika sehemu ya 3 ya mafunzo haya:

![CYP201](assets/fr/061.webp)


- Ikiwa `1` itasalia kwenye rafu, basi hati ni halali:

![CYP201](assets/fr/062.webp)

Kwa hivyo, kwa muhtasari, hati hii inaruhusu uthibitishaji, kwa usaidizi wa sahihi ya dijiti, kwamba mtumiaji anayedai Ownership ya UTXO hii na anayetaka kuitumia ana Ufunguo (Key) wa faragha unaohusishwa na kupokea Address iliyotumiwa wakati wa kuunda UTXO hii.

### Aina tofauti za anwani za Bitcoin

Katika mabadiliko ya Bitcoin, mifano kadhaa ya hati ya kawaida imeongezwa. Kila mmoja wao hutumia aina tofauti ya kupokea Address. Hapa kuna muhtasari wa mifano kuu ya hati inayopatikana hadi sasa:

**P2PK (*Pay-to-PubKey*)**:

Mtindo huu wa hati ulianzishwa katika Toleo (version) la kwanza la Bitcoin na Satoshi Nakamoto. Hati ya P2PK hufunga bitcoins moja kwa moja kwa kutumia Ufunguo (Key) mbichi wa umma (kwa hivyo, hakuna kupokea Address inatumiwa na mtindo huu). Muundo wake ni rahisi: ina Ufunguo (Key) wa umma na inahitaji sahihi sahihi ya digital ili kufungua fedha. Hati hii ni sehemu ya kiwango cha "*Legacy*".

**P2PKH (*Pay-to-PubKey-Hash*)**:

Kama P2PK, hati ya P2PKH ilianzishwa wakati wa uzinduzi wa Bitcoin. Tofauti na mtangulizi wake, hufunga bitcoins kwa kutumia Hash ya Ufunguo (Key) wa umma, badala ya kutumia moja kwa moja Ufunguo (Key) ghafi wa umma. Kisha *scriptSig* lazima itoe Ufunguo (Key) wa umma unaohusishwa na kupokea Address, pamoja na sahihi sahihi. Anwani zinazolingana na muundo huu huanza na `1` na zimesimbwa katika *base58check*. Hati hii pia ni ya kiwango cha "*Legacy*".

**P2SH (*Pay-to-Script-Hash*)**:

Ilianzishwa mwaka wa 2012 kwa BIP16, muundo wa P2SH unaruhusu kutumia Hash ya hati kiholela katika *scriptPubKey*. Hati hii ya haraka, inayoitwa "*redeemscript*", ina masharti ya kufungua fedha. Ili kutumia UTXO iliyofungwa kwa P2SH, ni muhimu kutoa *scriptSig* iliyo na *redeemscript* asili pamoja na data muhimu ili kuithibitisha. Mfano huu hutumiwa haswa kwa multisigs za zamani. Anwani zinazohusishwa na P2SH huanza na `3` na zimesimbwa katika *base58check*. Hati hii pia ni ya kiwango cha "*Legacy*".

**P2WPKH (*Pay-to-Witness-PubKey-Hash*)**:

Hati hii ni sawa na P2PKH, kwani pia inafunga bitcoins kwa kutumia Hash ya Ufunguo (Key) wa umma. Hata hivyo, tofauti na P2PKH, *scriptSig* inahamishwa hadi sehemu tofauti inayoitwa "*shahidi (witness)*". Hii wakati mwingine hujulikana kama "*scriptWitness*" kuashiria seti inayojumuisha saini na Ufunguo (Key) wa umma. Kila ingizo la SegWit lina *Scriptwitness* yake, na mkusanyiko wa *scriptWitnesses* unajumuisha sehemu ya *shahidi (witness)* ya shughuli hiyo. Usogezaji huu wa data ya sahihi ni uvumbuzi ulioanzishwa na sasisho la SegWit, linalolenga hasa kuzuia uharibifu wa shughuli kutokana na sahihi za ECDSA.

Anwani za P2WPKH hutumia usimbaji wa *bech32* na kila mara huanza na `bc1q`. Aina hii ya hati inalingana na Toleo (version) la 0 SegWit matokeo.

**P2WSH (*Hati-ya-Lipa-kwa-shahidi (witness)-Hash*)**:

Mfano wa P2WSH pia ulianzishwa na sasisho la SegWit mnamo Agosti 2017. Sawa na mfano wa P2SH, hufunga bitcoins kwa kutumia Hash ya script. Tofauti kuu iko katika jinsi saini na hati zinavyojumuishwa katika shughuli. Ili kutumia bitcoins zilizofungwa kwa aina hii ya hati, mpokeaji lazima atoe hati asili, inayoitwa *witnessScript* (sawa na *redeemscript* katika P2SH), pamoja na data muhimu ili kuthibitisha *shahidi (witness)Script* hii. Utaratibu huu unaruhusu utekelezaji wa masharti magumu zaidi ya matumizi, kama vile multisigs.

Address za P2WSH hutumia usimbaji wa *bech32* na kila mara huanza na `bc1q`. Hati hii pia inalingana na Toleo (version) la 0 SegWit matokeo.

**P2TR (*Pay-to-Taproot*)**:

Mtindo wa P2TR ulianzishwa kwa kutekelezwa kwa Taproot mnamo Novemba 2021. Inategemea itifaki ya Schnorr ya ujumlishaji wa Ufunguo (Key) wa kriptografia, na pia kwenye Merkle Tree kwa hati mbadala, inayoitwa MAST (*Mti wa Hati Mbadala wa Merkelized*). Tofauti na aina nyingine za hati, ambapo masharti ya matumizi yanafichuliwa hadharani (ama kwa kupokelewa au kwa matumizi), P2TR inaruhusu kufichwa kwa hati ngumu nyuma ya Ufunguo (Key) mmoja, unaoonekana wazi wa umma.

Kitaalam, hati ya P2TR hufunga bitcoins kwenye Ufunguo (Key) wa kipekee wa umma wa Schnorr, unaoashiria $Q$. Ufunguo (Key) huu $Q$ kwa hakika ni jumla ya Ufunguo (Key) wa umma $P$ na Ufunguo (Key) wa umma $M$, wa mwisho ukikokotolewa kutoka Merkle Root ya orodha ya *scriptPubKey*. Bitcoins zilizofungwa na aina hii ya hati zinaweza kutumika kwa njia mbili:


- Kwa kuchapisha saini ya Ufunguo (Key) wa umma $P$ (*njia ya Ufunguo (Key)*).
- Kwa kutosheleza mojawapo ya hati zilizomo kwenye Merkle Tree (*njia ya hati*).

P2TR kwa hivyo inatoa unyumbufu mkubwa, kwani inaruhusu kufunga bitcoins ama kwa Ufunguo (Key) wa kipekee wa umma, na maandishi kadhaa ya chaguo, au zote mbili kwa wakati mmoja. Faida ya muundo huu wa Merkle Tree ni kwamba hati ya matumizi tu inayotumiwa inafichuliwa wakati wa shughuli, lakini maandishi mengine yote mbadala yanabaki kuwa siri.

![CYP201](assets/fr/063.webp)

P2TR inalingana na Toleo (version) la 1 la matokeo ya SegWit, ambayo ina maana kwamba sahihi za pembejeo za P2TR zimehifadhiwa katika sehemu ya shughuli ya *shahidi (witness)*, na si katika *scriptSig*. Anwani za P2TR hutumia usimbaji wa *bech32m* na huanza na `bc1p`, lakini ni za kipekee kabisa kwa sababu hazitumii chaguo za kukokotoa za Hash kwa ujenzi wake. Kwa kweli, zinawakilisha moja kwa moja Ufunguo (Key) wa umma $Q$ ambao umeundwa tu na metadata. Kwa hivyo, ni mfano wa maandishi karibu na P2PK.

Sasa kwa kuwa tumefunika nadharia, wacha tuendelee kufanya mazoezi! Katika sura ifuatayo, ninapendekeza kupata SegWit v0 Address na SegWit v1 Address kutoka kwa jozi ya funguo.

## Utoaji wa Address

<chapterId>3ebdc750-4135-4881-b07e-08965941b93e</chapterId>

Hebu tuchunguze pamoja jinsi ya generate kupokea Address kutoka kwa jozi ya funguo ziko, kwa mfano, kwa Kina (depth) cha 5 cha HD Wallet. Address hii basi inaweza kutumika katika programu ya Wallet kufunga UTXO.

Kwa kuwa mchakato wa kuzalisha Address inategemea mfano wa script iliyopitishwa, hebu tuzingatie kesi mbili maalum: kuzalisha SegWit v0 Address katika P2WPKH na SegWit v1 Address katika P2TR. Aina hizi mbili za anwani hushughulikia matumizi mengi sana leo.

### Mfinyazo wa Ufunguo (Key) wa Umma

Baada ya kutekeleza hatua zote za uundaji kutoka kwa Ufunguo Mkuu (Master Key)hadi Kina (depth) 5 kwa kutumia fahirisi zinazofaa, tunapata jozi ya funguo ($k$, $K$) na $K = k \cdot G$. Ingawa inawezekana kutumia Ufunguo (Key) huu wa umma kama vile kufunga fedha kwa kiwango cha P2PK, hilo si lengo letu hapa. Badala yake, tunalenga kuunda Address katika P2WPKH kwa mara ya kwanza, na kisha katika P2TR kwa mfano mwingine.

Hatua ya kwanza ni kubana Ufunguo (Key) wa umma $K$. Ili kuelewa mchakato huu vizuri, acheni kwanza tukumbuke baadhi ya misingi iliyoangaziwa katika sehemu ya 3.

Ufunguo (Key) wa umma kwenye Bitcoin ni sehemu ya $K$ iliyo kwenye mkunjo wa duaradufu. Inawakilishwa katika fomu $(x, y)$, ambapo $x$ na $y$ ni viwianishi vya uhakika. Katika umbo lake ambalo halijabanwa, Ufunguo (Key) huu wa umma hupima biti 520: biti 8 kwa kiambishi awali (thamani ya awali ya `0x04`), biti 256 kwa kuratibu $x$, na biti 256 kwa kuratibu $y$.

Hata hivyo, mikunjo ya duaradufu ina sifa ya ulinganifu kwa heshima ya mhimili wa x: kwa $x$ ya kuratibu, kuna thamani mbili tu zinazowezekana za $y$: $y$ na $-y$. Pointi hizi mbili ziko kila upande wa mhimili wa x. Kwa maneno mengine, ikiwa tunajua $x$, inatosha kubainisha ikiwa $y$ ni sawa au isiyo ya kawaida ili kutambua uhakika halisi kwenye mkunjo.

![CYP201](assets/fr/064.webp)

Ili kubana Ufunguo (Key) wa umma, $x$ pekee ndiyo iliyosimbwa, ambayo inachukua biti 256, na kiambishi awali Kina (depth)ongezwa ili kubainisha usawa wa $y$. Njia hii inapunguza ukubwa wa Ufunguo (Key) wa umma hadi biti 264 badala ya 520 ya awali. Kiambishi awali `0x02` Kina (depth)onyesha kuwa $y$ ni sawa, na kiambishi awali `0x03` Kina (depth)onyesha kuwa $y$ ni isiyo ya kawaida.

Hebu tuchukue mfano ili kuelewa vizuri, na Ufunguo (Key) mbichi wa umma katika uwakilishi usio na shinikizo:

```text
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Ikiwa tutatenganisha Ufunguo (Key) huu, tunayo:


   - Kiambishi awali: `04`;
   - $x$: `678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6`;
   - $y$: `49f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f`

Herufi ya mwisho ya heksadesimali ya $y$ ni `f`. Katika msingi wa 10, `f = 15`, ambayo inalingana na nambari isiyo ya kawaida. Kwa hivyo, $y$ ni isiyo ya kawaida, na kiambishi awali kitakuwa `0x03` ili kuonyesha hili.

Ufunguo (Key) wa umma uliobanwa huwa:

```text
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```

Uendeshaji huu unatumika kwa miundo yote ya hati kulingana na ECDSA, yaani, yote isipokuwa P2TR ambayo inatumia Schnorr. Kwa upande wa Schnorr, kama ilivyoelezwa katika sehemu ya 3, tunabaki na thamani ya $x$ pekee, bila kuongeza kiambishi awali ili kuonyesha usawa wa $y$, tofauti na ECDSA. Hii inafanywa iwezekanavyo na ukweli kwamba usawa wa kipekee huchaguliwa kiholela kwa funguo zote. Hii inaruhusu kupunguzwa kidogo kwa nafasi ya kuhifadhi inayohitajika kwa funguo za umma.

### Utoaji wa SegWit v0 (bech32) Address

Kwa kuwa sasa tumepata Ufunguo (Key) wetu wa umma uliobanwa, tunaweza kupata SegWit v0 inayopokea Address kutoka kwayo.

Hatua ya kwanza ni kutumia kitendakazi cha HASH160 Hash kwenye Kitufe cha umma (Public Key) kilichobanwa. HASH160 ni muundo wa kazi mbili mfululizo za Hash: SHA256, ikifuatiwa na RIPEMD160:

$$
\text{HASH160}(K) = \text{RIPEMD160}(\text{SHA256}(K))
$$

Kwanza, tunapitisha Ufunguo (Key) kupitia SHA256:

```text
SHA256(K) = C489EBD66E4103B3C4B5EAFF462B92F5847CA2DCE0825F4997C7CF57DF35BF3A
```

Kisha tunapitisha matokeo kupitia RIPEMD160:

```text
RIPEMD160(SHA256(K)) = 9F81322CC88622CA4CCB2A52A21E2888727AA535
```

Tumepata Hash ya 160-bit ya Ufunguo (Key) wa umma, ambayo inajumuisha kile Kina (depth)choitwa malipo ya Address. Upakiaji huu unawakilisha sehemu kuu na muhimu zaidi ya Address. Pia inatumika katika *scriptPubKey* kufunga UTXO.

Hata hivyo, ili kufanya upakiaji huu utumike kwa urahisi zaidi na wanadamu, metadata huongezwa humo. Hatua inayofuata inahusisha kusimba hii Hash katika vikundi vya biti 5 katika desimali. Mabadiliko haya ya desimali yatakuwa muhimu kwa ubadilishaji kuwa *bech32*, inayotumiwa na anwani za post-SegWit. Hash ya binary ya 160-bit imegawanywa katika vikundi 32 vya biti 5:

$$
\begin{array}{|c|c|}
\hline
\text{5 bits} & \text{Decimal} \\
\hline
10011 & 19 \\
11110 & 30 \\
00000 & 0 \\
10011 & 19 \\
00100 & 4 \\
01011 & 11 \\
00110 & 6 \\
01000 & 8 \\
10000 & 16 \\
11000 & 24 \\
10001 & 17 \\
01100 & 12 \\
10100 & 20 \\
10011 & 19 \\
00110 & 6 \\
01011 & 11 \\
00101 & 5 \\
01001 & 9 \\
01001 & 9 \\
01010 & 10 \\
00100 & 4 \\
00111 & 7 \\
10001 & 17 \\
01000 & 8 \\
10001 & 17 \\
00001 & 1 \\
11001 & 25 \\
00111 & 7 \\
10101 & 21 \\
00101 & 5 \\
00101 & 5 \\
10101 & 21 \\
\hline
\end{array}
$$

Kwa hivyo, tunayo:

```text
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
```

Mara tu Hash inaposimbwa katika vikundi vya bits 5, hundi huongezwa kwa Address. Hundi hii inatumika kuthibitisha kuwa malipo ya Address hayajabadilishwa wakati wa kuhifadhi au kutuma. Kwa mfano, inaruhusu programu ya Wallet kuhakikisha kuwa hujaandika wakati wa kuingiza Address inayopokea. Bila uthibitishaji huu, unaweza kutuma bitcoins kwa bahati mbaya kwa Address isiyo sahihi, na kusababisha upotevu wa kudumu wa pesa, kwani humiliki Ufunguo (Key) unaohusishwa wa umma au wa kibinafsi. Kwa hiyo, checksum ni ulinzi dhidi ya makosa ya kibinadamu.

Kwa anwani za zamani za Bitcoin *Legacy*, hundi ilikokotolewa tu tangu mwanzo wa Address Hash na chaguo za kukokotoa za HASH256. Kwa kuanzishwa kwa SegWit na umbizo la *bech32*, misimbo ya BCH (*Bose, Ray-Chaudhuri, na Hocquenghem*) sasa inatumika. Misimbo hii ya kusahihisha makosa hutumiwa kugundua na kusahihisha makosa katika mfuatano wa data. Wanahakikisha kwamba taarifa inayotumwa inafika ikiwa haijakamilika inapopelekwa, hata katika kesi ya mabadiliko madogo. Misimbo ya BCH hutumiwa katika nyanja nyingi, kama vile SSD, DVD, na misimbo ya QR. Kwa mfano, kutokana na misimbo hii ya BCH, msimbo wa QR ambao umefichwa kwa kiasi bado unaweza kusomwa na kuamuliwa.

Katika muktadha wa Bitcoin, misimbo ya BCH hutoa maelewano bora kati ya ukubwa na uwezo wa kutambua makosa ikilinganishwa na chaguo rahisi za Hash zinazotumiwa kwa anwani za *Legacy*. Hata hivyo, kwenye Bitcoin, misimbo ya BCH hutumiwa tu kwa kutambua makosa, sio kurekebisha. Kwa hivyo, programu ya Wallet itaashiria kupokea kwa usahihi Address lakini haitasahihisha moja kwa moja. Kizuizi hiki ni cha kimaKusudi (Purpose): kuruhusu urekebishaji kiotomatiki kungepunguza uwezo wa kutambua makosa.

Ili kuhesabu cheki na nambari za BCH, tunahitaji kuandaa Elements kadhaa:


- HRP (*Sehemu Inayosomeka kwa Binadamu*)**: Kwa Bitcoin Mainnet, HRP ni `bc`;

HRP lazima ipanuliwe kwa kutenganisha kila herufi katika sehemu mbili:


- Kuchukua wahusika wa HRP katika ASCII:
 - `b`: `01100010`
 - `c`: `01100011`
- Kuchimbua bits 3 muhimu zaidi na bits 5 muhimu zaidi:
  - Bits 3 muhimu zaidi: `011` (3 katika desimali)
  - Bits 3 muhimu zaidi: `011` (3 katika desimali)
  - Bits 5 zisizo muhimu zaidi: `00010` (2 katika desimali)
  - Bits 5 zisizo muhimu zaidi: `00011` (3 katika desimali)

Kwa kitenganishi `0` kati ya herufi mbili, kiendelezi cha HRP kwa hivyo ni:

```text
03 03 00 02 03
```


- **Toleo (version) la shahidi (witness)**: Kwa Toleo (version) la 0 la SegWit, ni `00`;
- **Mzigo wa malipo**: Thamani za desimali za Ufunguo (Key) wa umma Hash;
- **Uwekaji nafasi kwa cheki**: Tunaongeza sufuri 6 `[0, 0, 0, 0, 0, 0]` mwishoni mwa mlolongo.

Data yote iliyojumuishwa ili kuingiza kwenye programu ili kukokotoa hundi ni kama ifuatavyo:

```text
HRP = 03 03 00 02 03
SEGWIT v0 = 00
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
CHECKSUM = 00 00 00 00 00 00
INPUT = 03 03 00 02 03 00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 00 00 00 00 00 00
```

Hesabu ya checksum ni ngumu sana. Inahusisha hesabu ya uga yenye ukomo wa polynomial. Hatutaelezea kwa undani hesabu hii hapa na tutasonga moja kwa moja kwenye matokeo. Katika mfano wetu, cheki iliyopatikana katika decimal ni:

```text
10 16 11 04 13 18
```

Sasa tunaweza kuunda Address inayopokea kwa kubatanisha kwa mpangilio ufuatao wa Elements:


- **Toleo (version) la SegWit**: `00`
- **Mzigo wa malipo**: Ufunguo (Key) wa umma Hash
- **Nambari ya hundi**: Thamani zilizopatikana katika hatua ya awali (`10 16 11 04 13 18`)

Hii inatupa katika decimal:

```text
00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 10 16 11 04 13 18
```

Kisha, kila thamani ya desimali lazima itolewe kwa herufi *bech32* kwa kutumia jedwali lifuatalo la ubadilishaji:

$$
\begin{array}{|c|c|c|c|c|c|c|c|c|}
\hline
& 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\hline
+0 & q & p & z & r & y & 9 & x & 8 \\
\hline
+8 & g & f & 2 & t & v & d & w & 0 \\
\hline
+16 & s & 3 & j & n & 5 & 4 & k & h \\
\hline
+24 & c & e & 6 & m & u & a & 7 & l \\
\hline
\end{array}
$$

Ili kubadilisha thamani kuwa herufi _bech32_ kwa kutumia jedwali hili, tafuta tu thamani katika safu wima ya kwanza na safu mlalo ya kwanza ambayo, ikijumuishwa pamoja, hutoa matokeo unayotaka. Kisha, rudisha herufi inayolingana. Kwa mfano, nambari ya desimali `19` itabadilishwa kuwa herufi `n`, kwa sababu $19 = 16 + 3$.

Kwa kuchora maadili yetu yote, tunapata Address ifuatayo:

```
qn7qnytxgsc3v5nxt9ff2y83g3pe84ff42stydj
```

Kilichosalia ni kuongeza HRP `bc`, ambayo inaonyesha kuwa ni Address kwa Bitcoin Mainnet, pamoja na kitenganishi `1`, ili kupata Address kamili ya kupokea:

```
bc1qn7qnytxgsc3v5nxt9ff2y83g3pe84ff42stydj
```

Umaalumu wa alfabeti hii ya _bech32_ ni kwamba inajumuisha herufi zote za alphanumeric isipokuwa `1`, `b`, `i`, na `o` ili kuepuka mkanganyiko wa kuona kati ya herufi zinazofanana, hasa wakati wa kuingia au kusomwa na binadamu.

Kwa muhtasari, hapa kuna mchakato wa kupata:

![CYP201](assets/fr/065.webp)

Hivi ndivyo jinsi ya kupata P2WPKH (SegWit v0) kupokea Address kutoka kwa jozi ya funguo. Hebu sasa tuendelee hadi kwenye anwani za P2TR (SegWit v1 / Taproot) na tugundue mchakato wa uzalishaji wao.

### Utoaji wa SegWit v1 (bech32m) Address

Kwa anwani za Taproot, mchakato wa kizazi hutofautiana kidogo. Hebu tuangalie hili pamoja!

Kutoka kwa hatua ya ukandamizaji wa Ufunguo (Key) wa umma, tofauti ya kwanza inaonekana ikilinganishwa na ECDSA: funguo za umma zinazotumiwa kwa Schnorr kwenye Bitcoin zinawakilishwa tu na abscissa yao ($ x $). Kwa hivyo, hakuna kiambishi awali, na Ufunguo (Key) ulioshinikizwa hupima bits 256 haswa.

Kama tulivyoona katika sura iliyotangulia, hati ya P2TR inafunga bitcoins kwenye Ufunguo (Key) wa kipekee wa umma wa Schnorr, ulioteuliwa na $Q$. Ufunguo (Key) huu $Q$ ni muunganisho wa funguo mbili za umma: $P$, Ufunguo Mkuu (Master Key)wa ndani wa umma, na $M$, Ufunguo (Key) wa umma unaotokana na Merkle Root ya orodha ya _scriptPubKey_. Bitcoins zilizofungwa na aina hii ya hati zinaweza kutumika kwa njia mbili:


- Kwa kuchapisha saini ya Ufunguo (Key) wa umma $P$ (_njia ya Ufunguo (Key)_);
- Kwa kutosheleza mojawapo ya hati zilizojumuishwa kwenye Merkle Tree (_script path_).

Kwa kweli, funguo hizi mbili "hazijaunganishwa." Kitufe cha $P$ badala yake kimebadilishwa na Ufunguo (Key) $M$. Katika cryptography, "tweak" Ufunguo (Key) wa umma inamaanisha kurekebisha Ufunguo (Key) huu kwa kutumia thamani ya ziada inayoitwa "tweak." Uendeshaji huu huruhusu Ufunguo (Key) uliorekebishwa kubaki sambamba na Ufunguo (Key) wa asili wa faragha na tweak. Kitaalam, tweak ni thamani ya scalar $t$ ambayo huongezwa kwa Ufunguo (Key) wa kwanza wa umma. Ikiwa $P$ ndio Ufunguo (Key) asili wa umma, Ufunguo (Key) uliobadilishwa unakuwa:

$$
P' = P + tG
$$

Ambapo $G$ ni jenereta ya curve ya duaradufu inayotumika. Uendeshaji huu hutoa Ufunguo (Key) mpya wa umma unaotokana na Ufunguo (Key) asili, huku ukihifadhi sifa za siri zinazoruhusu matumizi yake.

Iwapo huhitaji kuongeza hati mbadala (kutumia pekee kupitia _key path_), unaweza generate Taproot Address iliyoanzishwa kwa kutumia Kitufe cha umma (Public Key) kilicho katika Kina (depth) cha 5 cha Wallet yako. Katika kesi hii, ni muhimu kuunda hati isiyoweza kutumika kwa _script path_, ili kukidhi mahitaji ya muundo. Tweak $t$ kisha inakokotolewa kwa kutumia chaguo za kukokotoa zilizotambulishwa za Hash, **`TapTweak`**, kwenye Ufunguo (Key) wa ndani wa umma $P$:

$$
t = \text{H}\_{\text{TapTweak}}(P)
$$

wapi:


- $\text{H}_{\text{TapTweak}}$** ni chaguo za kukokotoa za SHA256 Hash zilizowekwa lebo ya `TapTweak`. Iwapo hufahamu kipengele cha kukokotoa chenye alama ya Hash ni nini, ninakualika uangalie sura ya 3.3;
- $P$ ni Ufunguo (Key) wa ndani wa umma, unaowakilishwa katika umbizo lake la biti-256 lililobanwa, kwa kutumia kiratibu cha $x$ pekee.

Ufunguo (Key) wa umma wa Taproot $Q$ kisha hukokotolewa kwa kuongeza kibano $t$, Kina (depth)chozidishwa na jenereta ya mkunjo wa duaradufu $G$, kwa Ufunguo (Key) wa ndani wa umma $P$:

$$
Q = P + t \cdot G
$$

Mara tu Ufunguo (Key) wa umma wa Taproot $Q$ unapopatikana, tunaweza generate kupokea sambamba Address. Tofauti na miundo mingine, anwani za Taproot hazijaanzishwa kwenye Hash ya Ufunguo (Key) wa umma. Kwa hiyo, Ufunguo (Key) wa $ Q$ umeingizwa moja kwa moja kwenye Address, kwa namna ya ghafi.

Kuanza, tunatoa kiratibu cha $x$ cha uhakika $Q$ ili kupata Ufunguo (Key) wa umma uliobanwa. Kwenye mzigo huu wa malipo, hundi inakokotolewa kwa kutumia misimbo ya BCH, kama ilivyo kwa anwani za SegWit v0. Walakini, programu inayotumiwa kwa anwani za Taproot inatofautiana kidogo. Hakika, baada ya kuanzishwa kwa umbizo la _bech32_ na SegWit, hitilafu iligunduliwa: wakati herufi ya mwisho ya Address ni `p`, kuingiza au kuondoa `q` kabla ya `p` hii haifanyi hundi kuwa batili. Ingawa mdudu huyu hana matokeo kwenye SegWit v0 (shukrani kwa kizuizi cha saizi), inaweza kusababisha shida katika siku zijazo. Kwa hivyo hitilafu hii imesahihishwa kwa anwani za Taproot, na umbizo jipya lililosahihishwa linaitwa "_bech32m_".

Taproot Address inatolewa kwa kusimba kiratibu cha $x$ cha $Q$ katika umbizo la _bech32m_, kwa kutumia Elements ifuatayo:


- **HRP (_Sehemu Inayosomeka kwa Binadamu_)**: `bc`, ili kuonyesha mtandao mkuu wa Bitcoin;
- **Toleo (version)**: `1` kuashiria Taproot / SegWit v1;
- **Cheki**.

Address ya mwisho kwa hivyo itakuwa na umbizo:

```
bc1p[Qx][checksum]
```

Kwa upande mwingine, ikiwa ungependa kuongeza hati mbadala pamoja na matumizi na Ufunguo (Key) wa ndani wa umma (_script path_), hesabu ya Address inayopokea itakuwa tofauti kidogo. Utahitaji kujumuisha Hash ya hati mbadala katika hesabu ya tweak. Katika Taproot, kila script mbadala, iko mwisho wa Merkle Tree, inaitwa "jani".

Mara tu maandishi mbadala tofauti yanapoandikwa, lazima uyapitishe kibinafsi kupitia kitendakazi chenye lebo ya Hash `TapLeaf`, Kina (depth)choambatana na baadhi ya metadata:

$$
\text{h}_{\text{leaf}} = \text{H}_{\text{TapLeaf}} (v \Vert sz \Vert S)
$$

Na:


- $v$: nambari ya Toleo (version) la hati (chaguo-msingi `0xC0` kwa Taproot);
- $sz$: ukubwa wa hati iliyosimbwa katika umbizo la _CompactSize_;
- $S$: hati.

Heshi tofauti za hati ($\text{h}_{\text{leaf}}$) hupangwa kwanza kwa mpangilio wa kileksikografia. Kisha, huunganishwa katika jozi na kupitishwa kupitia chaguo la kukokotoa la Hash `TapBranch`. Utaratibu huu unarudiwa mara kwa mara ili kujenga, hatua kwa hatua, Merkle Tree:

$$
\text{h}_{\text{branch}} = \text{H}_{\text{TapBranch}}(\text{h}_{\text{leaf1}} \Vert \text{h}_{\text{leaf2}})
$$

Kisha tunaendelea kwa kuunganisha matokeo mawili baada ya mawili, tukiyapitisha kwa kila hatua kupitia chaguo la kukokotoa la Hash `TapBranch`, hadi tupate mzizi wa Merkle Tree:

![CYP201](assets/fr/066.webp)

Mara tu Merkle Root $h_{\text{root}}$ inakokotolewa, tunaweza kuhesabu tweak. Kwa hili, tunaunganisha Ufunguo (Key) wa ndani wa umma wa Wallet $P$ na mzizi $h_{\text{root}}$, na kisha tupitishe yote kupitia chaguo la kukokotoa la Hash `TapTweak` lililowekwa lebo:

$$
t = \text{H}_{\text{TapTweak}}(P \Vert h_{\text{root}})
$$

Hatimaye, kama hapo awali, Ufunguo (Key) wa umma wa Taproot $Q$ unapatikana kwa kuongeza Ufunguo (Key) wa ndani wa umma $P$ kwa bidhaa ya tweak $t$ na pointi ya jenereta $G$:

$$
Q = P + t \cdot G
$$

Kisha, utengenezaji wa Address hufuata mchakato ule ule, kwa kutumia Ufunguo (Key) ghafi wa umma $Q$ kama upakiaji, unaoambatana na metadata ya ziada.

Na hapo unayo! Tumefika mwisho wa kozi hii ya CYP201. Ikiwa umepata kozi hii kuwa ya manufaa, nitashukuru sana ikiwa ungeweza kuchukua muda mfupi kuipa ukadiriaji mzuri katika sura ifuatayo ya tathmini. Jisikie huru pia kuishiriki na wapendwa wako au kwenye mitandao yako ya kijamii. Hatimaye, ikiwa ungependa kupata diploma yako ya kozi hii, unaweza kufanya mtihani wa mwisho baada ya sura ya tathmini.

# Hitimisho

<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>

## Ukaguzi na Ukadiriaji

<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>

<isCourseReview>true</isCourseReview>
## Mtihani wa Mwisho

<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>

<isCourseExam>true</isCourseExam>
## Hitimisho

<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
