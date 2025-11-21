---
name: SwapMarket
description: Bitcoin na kijumlishi cha huduma za kubadilishana umeme
---

![cover](assets/cover.webp)



Uhamisho wa fedha kati ya Bitcoin on-chain na Lightning Network kwa ujumla huhitaji kufungua mwenyewe chaneli za Umeme (kiufundi na gharama kubwa), au utumizi wa majukwaa ya kubadilishana ya kati na KYC. SwapMarket inatoa njia mbadala: ubadilishaji wa atomiki usioaminika kupitia watoa huduma washindani, bila KYC.



Ubunifu: ingawa watoa huduma ni wasuluhishi, HTLC (*Mikataba Iliyofungwa kwa Muda wa Hash*) inakuhakikishia kihisabati kuwa pesa zako zitaendelea kuwa chini ya udhibiti wako. Mkusanyiko wa watoa huduma kadhaa (Boltz, ZEUS Swaps, Eldamar, Njia ya Kati) huleta ushindani wa bei. Interface mtandao wa chanzo huria unaoweza kujitegemea.



## SwapMarket ni nini?



Kijumlishi cha programu huria kilichozinduliwa mnamo 2024, SwapMarket hufanya kazi kama kilinganishi cha watoa huduma wa kubadilishana Bitcoin/Lightning. Mtumiaji hulinganisha hali (ada, ukwasi, mipaka) na kuchagua mtoaji bora zaidi.



### Usanifu wa kiufundi



**Upande wa mteja wa mbele**: 100% ya maombi ya upande wa mteja (fork Boltz Web App) iliyopangishwa kwenye Kurasa za GitHub. Msimbo huendesha katika kivinjari bila seva ya nyuma. Historia iliyohifadhiwa ndani (vidakuzi/cache). Msimbo wa chanzo wa umma na unaoweza kukaguliwa.



**Ugunduzi wa mtoa huduma** : Orodha yenye msimbo mgumu katika `src/configs/mainnet.ts`. Watoa huduma wapya waliongezwa kupitia Ombi la Kuvuta au barua pepe.



**Njema zinazojitegemea**: Kila mtoa huduma anaendesha mazingira yake ya nyuma ya Boltz. Kiolesura huuliza API kwa wakati halisi ili kulinganisha manukuu papo hapo.



**Mabadilishano ya Atomiki ya HTLC**: Mikataba Iliyofungwa kwa Muda wa Hash inahakikisha atomiki: ama ubadilishaji utatekelezwa, au kila mhusika kurejesha pesa zake. Hatari ya vyama pinzani imeondolewa kihisabati.



### Falsafa



SwapMarket inapunguza uwekaji kati kwa kuunda ushindani kati ya watoa huduma kwa ada na ukwasi. Hakuna KYC, msimbo wa kujihifadhi wa chanzo huria, kuzidisha waendeshaji wa kujitegemea ili kuepuka pointi moja ya kushindwa.



## Sifa kuu



### Soko la Mtoa huduma



Kiolesura kinaonyesha watoa huduma wote wanaotumika: jina la mtoa huduma, ada zinazotumika (asilimia na/au zisizobadilika), kiasi cha chini/kiwango cha juu zaidi kinachopatikana, na aina za kubadilishana zinazotumika. Programu inaulizia moja kwa moja API za kila mtoa huduma aliyerejelewa katika faili ya usanidi ili kupata nukuu kwa wakati halisi. Ushindani kati ya watoa huduma huhakikisha viwango bora, kwa ujumla karibu 0.5% kwa ubadilishaji wa kawaida.



### Ubadilishanaji wa pande mbili



**Badilika (on-chain → Umeme)**: Badilisha on-chain BTC kuwa satoshi za Umeme. Kipochi cha matumizi: washa umeme wa simu ya wallet, pata uwezo unaoingia kwenye nodi, au uwe na ukwasi wa papo hapo.



**Kubadilishana (Umeme → on-chain)**: Badilisha satoshi za Umeme hadi on-chain BTC. Kisa cha matumizi: safisha umeme wa wallet kwenye hifadhi baridi au kusawazisha ukwasi kati ya tabaka.



### Usalama na kupona



**Mabadilishano ya atomiki ya Trustless**: HTLCs huhakikisha kwamba ubadilishanaji huo umekamilika kikamilifu, au kila mhusika kurejesha hisa yake. Hatari ya vyama pinzani imeondolewa kihisabati.



**Njia ya ulipaji**: Kila ubadilishaji una muda wa kufunga. Ikiwa ubadilishaji hautafaulu, pesa zitarejeshwa kiotomatiki baada ya kuisha. Mtumiaji daima anakuwa na chaguo la kurejesha bitcoins zake.



**Vifunguo vya kurejesha uwezo wa kufikia akaunti**: SwapMarket hukuwezesha kuhamisha vitufe vya urejeshaji kwa mabadilishano yanayoendelea. Katika tukio la tatizo, funguo hizi zinaweza kutumika kukamilisha au kughairi ubadilishanaji kutoka kwa kifaa chochote.



## Ufungaji na ufikiaji



### Mtandao wa Interface



SwapMarket haihitaji usakinishaji. Ufikiaji ni kupitia kivinjari kwa kutembelea https://swapmarket.github.io. Kwa usiri wa hali ya juu, tumia Brave, Firefox iliyo na viendelezi vya kuzuia ufuatiliaji, au LibreWolf. Kivinjari cha Tor kinapendekezwa kwa kutokujulikana kwa mtandao.



Hakuna usajili, barua pepe au uthibitishaji wa utambulisho unaohitajika.



### Mwenyeji mwenyewe (si lazima)



Kwa watumiaji wa kiufundi wanaotaka kuondoa utegemezi wowote kwenye kikoa rasmi cha Kurasa za GitHub, SwapMarket inaweza kuendeshwa ndani ya nchi :



**Kupitia npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Kupitia Docker** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



Programu itafikiwa katika `http://localhost:3000`. Upangishaji wa kibinafsi huhakikisha udhibiti kamili wa kiolesura, huondoa hatari ya udhibiti wa kikoa rasmi, na huruhusu msimbo wa chanzo kukaguliwa kabla ya utekelezaji.



### Usanidi wa awali



**Umeme wa Wallet**: Hakikisha una Umeme wa wallet unaofanya kazi (Phoenix, Zeus, BlueWallet, n.k.). Kwa kubadilishana, utakuwa generate ankara ya Umeme. Kwa kubadilishana, utalipa ankara ya Umeme.



**Wallet on-chain**: Kwa kubadilishana, utahitaji wallet Bitcoin on-chain kutuma pesa. Kwa kubadilishana, tayarisha anwani ya kupokea ya Bitcoin.



**Usanidi wa hiari**: SwapMarket huhifadhi historia ya kubadilishana na mapendeleo katika vidakuzi vya kivinjari. Hakuna haja ya kuunda akaunti.



## Ufikiaji wa mipangilio na Ufunguo wa Uokoaji



Kabla ya kufanya mabadilishano yako ya kwanza, tunapendekeza kwa dhati kwamba upakue **Ufunguo wako wa Uokoaji**. Ufunguo huu wa dharura hukuwezesha kurejesha pesa zako kukitokea tatizo la kiufundi au kupoteza uwezo wa kufikia kifaa chako.



### Vigezo vya ufikiaji



Kutoka kwa ukurasa mkuu wa SwapMarket, bofya kwenye ikoni ya gia (⚙️) iliyo upande wa juu kulia wa kiolesura, karibu na fomu ya kubadilishana.



![Accès aux paramètres](assets/fr/01.webp)



### Mipangilio ya Ukurasa



Ukurasa wa Mipangilio unafungua, kuonyesha chaguzi kadhaa za usanidi:





- Dhehebu**: Chaguo la BTC au sats
- Kitenganishi cha decimal**: Kitenganishi cha decimal (, au .)
- Arifa za Sauti/Kivinjari**: Arifa za sauti na kivinjari
- Ufunguo wa Uokoaji** : Pakua ufunguo wa kurejesha
- Kumbukumbu**: Tazama, pakua au futa kumbukumbu



![Page Settings](assets/fr/02.webp)



### Pakua Ufunguo wa Uokoaji



Bofya kwenye kitufe cha **Pakua ** karibu na "Ufunguo wa Uokoaji".



**Mambo muhimu** :




- Ufunguo wa Uokoaji ni **ufunguo wa dharura wa kituo kimoja** ambao hufanya kazi kwa mabadilishano yako yote yajayo
- Weka ufunguo huu mahali **salama na ya kudumu** (kidhibiti cha nenosiri, salama ya dijitali)
- Katika tukio la tatizo la kubadilishana (muda umeisha, kushindwa kiufundi), ufunguo huu utapata kurejesha fedha zako



## Kuunda ubadilishaji hatua kwa hatua



### Kubadilishana nje: Umeme → Bitcoin



Mfano huu wa kwanza unaonyesha jinsi ya kubadilisha satoshi ya umeme kuwa bitcoins za on-chain.



**Hatua ya 1: Badilisha usanidi



Kutoka kwa ukurasa kuu, chagua fomu ya kubadilishana:




- UMEME** (uwanja wa juu): Weka kiasi unachotaka kutuma katika Umeme wa sats (mfano: 30,000 sats)
- BITCOIN** (sehemu ya chini): Kiasi utakachopokea kitaonyeshwa kiotomatiki baada ya ada kukatwa (mfano: 29,320 sats)



Katika sehemu ya chini, bandika **anwani yako ya kupokea Bitcoin** ambapo ungependa kupokea pesa. Angalia anwani hii kwa uangalifu.



Mtoa huduma chaguo-msingi kwa kawaida ni Boltz Exchange. Ada za mtandao na ada za mtoa huduma zinaonyeshwa wazi.



![Configuration swap-out](assets/fr/03.webp)



**Hatua ya 2: Uchaguzi wa mtoa huduma**



Bofya kwenye menyu kunjuzi ya mtoa huduma (chaguo-msingi: "Boltz Exchange") ili kuonyesha watoa huduma wote wa ukwasi wanaopatikana.



Dirisha la modal linafungua, kuonyesha jedwali la kulinganisha:




- Hali**: Kiashiria cha Green ikiwa mtoaji anatumika
- Lakabu**: Jina la mtoa huduma (Boltz Exchange, Njia ya Kati, Eldamar, Mabadiliko ya ZEUS)
- Ada**: Ada zinazotozwa na mtoa huduma (kwa ujumla kati ya 0.49% na 0.5%)
- Ubadilishaji wa Juu**: Kiasi cha juu zaidi kinachokubaliwa kwa ubadilishaji



Linganisha ada na kiasi cha juu zaidi, kisha uchague mtoaji huduma unayemtaka.



**Tafadhali kumbuka**: Kiolesura cha uteuzi cha mtoa huduma haionyeshi **kiasi cha chini zaidi** kwa kila mtoa huduma. Taarifa hii inaonekana tu katika kiolesura cha uundaji wa kubadilishana, baada ya mtoa huduma kuchaguliwa. Kiasi cha chini na cha juu zaidi kinaweza kutofautiana kutoka kwa mtoaji hadi mtoaji, na kinaweza kubadilika kwa wakati. **Daima angalia vikomo hivi wakati wa kubadilishana**: ikiwa kiasi unachotaka kubadilisha kiko nje ya mipaka ya mtoa huduma, unaweza kuchagua nyingine inayofaa zaidi kwa muamala wako.



![Sélection du provider](assets/fr/04.webp)



**Hatua ya 3: Uundaji wa kubadilishana na Umeme** malipo



Bofya kwenye kibonye cha manjano **"UNDA BADILISHA YA ATOMI"** kitufe. SwapMarket itakupatia generate ** ankara ya Umeme** (BOLT11) ili ulipe kutoka kwa Umeme wa wallet yako.



Ukurasa unaonyesha:




- Kitambulisho cha Badili**: Kitambulisho cha kipekee cha kubadilishana (mfano: J4ymFIMVR6Hm)
- Hali**: "swap.created" (mabadilishano yameundwa, yanasubiri malipo)
- Msimbo wa QR**: Ichanganue kwa Umeme wako wa wallet
- Umeme wa Invoice**: Mfuatano wa herufi unaoanza na "lnbc" (mfano: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Lipa ankara hii kutoka kwa Umeme wa wallet (Phoenix, Zeus, BlueWallet, n.k.). Kiasi halisi cha kulipwa kinaonyeshwa (mfano: 30,000 sats).



![Paiement Lightning](assets/fr/05.webp)



**Hatua ya 4: Uthibitisho na ukubali**



Baada ya malipo ya umeme kuthibitishwa, SwapMarket hupokea malipo yako papo hapo na mtoa huduma atatangaza muamala wa Bitcoin kwa anwani yako.



Hali inabadilika kuwa **"invoice.settled "** (ankara imelipwa), na ujumbe wa uthibitisho utaonyeshwa.



Bitcoins zako za on-chain zitapatikana punde tu muamala utakapothibitishwa (kwa kawaida ni dakika chache hadi saa chache, kulingana na ada za mining zilizochaguliwa na mtoa huduma).



![Confirmation swap-out](assets/fr/06.webp)



Unaweza kubofya kwenye **"FUNGUA SHUGHULI YA MADAI "** ili kutazama muamala wa Bitcoin kwenye kivinjari cha blockchain.



### Badilishana: Bitcoin → Umeme



Mfano huu wa pili unaonyesha jinsi ya kubadilisha bitcoins za on-chain kuwa satoshi za Umeme.



**Hatua ya 1: Badilisha usanidi



Kutoka kwa ukurasa kuu, chagua fomu ya kubadilishana:




- BITCOIN** (sehemu ya juu): Weka kiasi unachotaka kutuma katika sats Bitcoin (mfano: 63,400 sats)
- UMEME** (uwanja wa chini): Kiasi utakayopokea huonyeshwa kiotomatiki baada ya kukatwa kwa ada (mfano: 62 884 sats)



Katika sehemu ya chini, bandika ankara ya Umeme** (BOLT11) inayotokana na Umeme wa wallet yako, au tumia anwani yako ya LNURL ikiwa wallet yako inaitumia.



![Configuration swap-in](assets/fr/07.webp)



**Hatua ya 2: Angalia Ufunguo wa Uokoaji**



Baada ya kubofya **"UNDA BADILISHANO LA ATOMI"**, dirisha la modal linaonekana, likikuuliza uthibitishe Ufunguo wako wa Uokoaji.



![Modal Rescue Key](assets/fr/08.webp)



**Ufunguo wa Uokoaji wa Boltz**: Kwa vile tayari umepakia ufunguo wako wa uokoaji wakati wa usanidi wa awali (angalia sehemu iliyotangulia), bofya kwenye **"THIBITISHA UFUNGUO ULIOPO "** ili kuleta ufunguo uliohifadhi.



Chagua faili ya Ufunguo wa Uokoaji iliyopakuliwa hapo awali. Baada ya uthibitishaji uliofanikiwa, kiolesura hubadilika kiotomatiki hadi hatua inayofuata.



**Hatua ya 3: Bitcoin** anwani ya amana



SwapMarket sasa inazalisha **anwani ya kipekee ya Bitcoin** iliyo na mkataba wa HTLC uliounganishwa na ankara yako ya Umeme.



Ukurasa unaonyesha:




- Kitambulisho cha kubadilisha**: Kitambulisho cha kipekee (mfano: 1kGmB6JyGqU4)
- Hali**: "invoice.set" (seti ya ankara, inasubiri malipo Bitcoin)
- Msimbo wa QR**: Anwani ya bohari ya Bitcoin
- Anwani ya Bitcoin**: Kwa kawaida huanza na "bc1p..." (mfano: bc1p5mvtwxapjkds...9d4n9f)
- Onyo kwa manjano** : "Hakikisha kuwa muamala wako unathibitisha ndani ya ~ saa 24 baada ya kuunda ubadilishanaji huu!"



Kipindi hiki cha ~saa 24 ni **muda kuisha** wa mkataba wa HTLC. Ikiwa muamala wako wa Bitcoin haujathibitishwa ndani ya muda uliowekwa, ubadilishaji hautafaulu na utahitaji kutumia Ufunguo wako wa Uokoaji kurejesha pesa zako.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Unaweza kunakili anwani kwa kubofya kitufe cha **"ANWANI "**, au changanua msimbo wa QR moja kwa moja kutoka kwa wallet on-chain yako.



**Hatua ya 4: Kutuma bitcoins**



Kutoka kwa wallet Bitcoin on-chain yako, tuma **haswa** kiasi kilichoonyeshwa (k.m. 63,400 sats) kwa anwani iliyozalishwa.



**Muhimu**: Tumia ada zinazofaa za mining ili kuhakikisha uthibitisho wa haraka. Ikiwa ada ni ya chini sana na muamala utabaki kwenye kumbukumbu zaidi ya muda ulioisha (~24h), ubadilishanaji hautafaulu.



Mara tu muamala utakapotumwa, SwapMarket hugundua kuwa iko kwenye kumbukumbu na inaonyesha :




- Hali** : "transaction.mempool
- Ujumbe**: "Muamala uko kwenye mempool - Inasubiri uthibitisho ili kukamilisha ubadilishanaji"



![Transaction en mempool](assets/fr/10.webp)



**Hatua ya 5: Uthibitisho na Umeme** mapokezi



Mara tu muamala wa Bitcoin unapopokea uthibitisho wake wa kwanza, mtoa huduma hulipa kiotomati ankara yako ya Umeme. Unapokea satoshi papo hapo kwenye Umeme wako wa wallet.



Hali inabadilika kuwa **"transaction.claim.pending "**, kisha ujumbe wa uthibitisho utaonyeshwa:



![Confirmation swap-in](assets/fr/11.webp)



Satoshi zako za Umeme zinapatikana mara moja katika wallet yako.



## Faida na mapungufu



### Faida



**Ushindani wa viwango**: Ujumlisho wa watoa huduma huunda shindano la asili la kupunguza ada (0.49% hadi 0.5%).



**Usiri**: Hakuna KYC, kiolesura cha 100% cha upande wa mteja (hakuna utumaji wa data ya kibinafsi), Kivinjari cha Tor kinachooana.



**Isiyo ya ulezi**: HTLC inakuhakikishia kihisabati udhibiti wa kipekee wa pesa zako. Labda ubadilishaji utafaulu, au unarudisha bitcoins zako.



**inayoweza kujiendesha yenyewe kwenye Chanzo huria**: msimbo wa umma unaoweza kukaguliwa, unaoweza kutumika ndani ya nchi kwa upinzani wa juu zaidi kwa udhibiti.



### Mapungufu



**Upeo mdogo**: Idadi ndogo ya watoa huduma amilifu (Boltz, Eldamar, MiddleWay kulingana na kipindi). Kiasi cha juu kinaweza kupunguzwa.



**Muda wa mwisho wa matumizi**: Muda umekwisha kutoka 24h hadi 48h. Ikiwa muamala wa on-chain haujathibitishwa kabla ya kuisha, urejeshaji wa mikono unahitajika.



**Uwekaji kati wa Interface**: Ingawa unaweza kujipangia, kiolesura rasmi kinapangishwa kwenye Kurasa za GitHub. Ikiwa GitHub itadhibiti repo, ufikiaji kupitia swapmarket.github.io utazuiwa (suluhisho: upangishaji wa kibinafsi).



**on-chain Traces**: Hati za HTLC zinaweza kutambulika kwa uchanganuzi wa kina wa blockchain.



## Mbinu bora



### Configuration salama



**Pakua Ufunguo wako wa Uokoaji**: Kabla ya kubadilishana kwako mara ya kwanza, pakua Ufunguo wako wa Uokoaji kutoka kwa Mipangilio (angalia sehemu maalum hapo juu). Ufunguo huu wa kipekee utafanya kazi kwa mabadilishano yako yote yajayo, kukuwezesha kurejesha pesa zako kukitokea tatizo.



**Tumia Kivinjari cha Tor**: Kwa usiri wa hali ya juu, fikia SwapMarket kupitia Kivinjari cha Tor ili kuficha anwani yako ya IP.



**Fikiria upangishaji binafsi**: Kwa watumiaji wa kiufundi, kuendesha mfano wako binafsi wa SwapMarket huondoa utegemezi kwenye kikoa rasmi cha Kurasa za GitHub.



### Uboreshaji wa ubadilishaji



**Fuatilia kumbukumbu**: Angalia mempool.space kabla ya kubadilishana. Chagua nyakati za shughuli za chini ili kupunguza gharama za mining.



**Angalia anwani**: Kwa kubadilishana, angalia kwa uangalifu anwani yako ya kupokea. Tumia nakala na ubandike na uangalie herufi 5 za kwanza na 5 za mwisho.



**Jaribio kwa kiasi kidogo**: Anza na kiwango cha chini kinachoruhusiwa (25,000 hadi 50,000 sats). Ongeza hatua kwa hatua mara tu unapomaliza mchakato.



**Weka hati mabadilishano yako**: Andika kitambulisho cha kila ubadilishaji, anwani ya utumiaji na tarehe ya mwisho wa matumizi. Taarifa hii hurahisisha ufuatiliaji na urejeshaji katika tukio la tatizo la kiufundi.



### Mkakati wa matumizi



**Sawazisha mtiririko wako wa pesa**: Tumia SwapMarket kurekebisha mgao wako kati ya on-chain (akiba, usalama wa muda mrefu) na Umeme (gharama za kila siku, malipo ya papo hapo) kulingana na mahitaji yako halisi.



**Kokotoa faida**: Kwa mahitaji ya kudumu ya ukwasi wa Umeme, linganisha gharama limbikizi ya kubadilishana mara kwa mara dhidi ya kufungua chaneli ya Umeme moja kwa moja. SwapMarket inafaulu kwa marekebisho ya mara moja, si lazima kwa mtiririko mkubwa wa kawaida.



## SwapMarket vs Boltz: Kuna tofauti gani?



### Boltz: Teknolojia dhidi ya Huduma



**Boltz ni teknolojia ya programu huria** (`boltz-backend` kwenye GitHub) ambayo hutumia ubadilishaji wa atomiki kupitia HTLC kati ya Bitcoin, Radi na Liquid.



**Hatua muhimu**: Watoa huduma wote wa SwapMarket (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) wanatumia mfano wao wenyewe wa mazingira ya nyuma ya Boltz. Kwa hivyo, teknolojia ya msingi ni sawa. Athari katika mazingira ya nyuma ya Boltz inaweza kuathiri watoa huduma wote, lakini asili ya chanzo huria ya mfumo inaruhusu ukaguzi wa jamii.



**Boltz Exchange** ni huduma moja inayoendeshwa na timu ya Boltz, huku **SwapMarket** inawaleta pamoja watoa huduma kadhaa wote kwa kutumia teknolojia ya Boltz, na kuunda mazingira pinzani ya bei.



Tazama mafunzo yetu ya Kubadilisha Boltz na Zeus kwa maelezo zaidi:



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Tofauti kuu



| Kipengele    | Boltz Exchange       | SwapMarket                           |
| ------------ | -------------------- | ------------------------------------ |
| Asili         | Huduma ya kipekee    | Muunganisha wa watoa huduma wengi    |
| Watoa huduma  | Boltz pekee          | Boltz, ZEUS, Eldamar, Middle Way     |
| Ushindani     | Ada zilizowekwa      | Ushindani huria                      |
| Kiolesura     | boltz.exchange       | swapmarket.github.io (inaweza kujihostisha) |
| Usalama       | Non-custodial (HTLC) | Non-custodial (HTLC)                 |

**Faida za SwapMarket**: Ushindani wa bei, utofauti wa matukio ya nyuma, ulinganisho wa wakati halisi.



**Njia mbadala za kiteknolojia** (hazitumii SwapMarket): Kitanzi cha Umeme (Maabara ya Umeme), Muun Wallet, NLoop, Breez Wallet. Suluhu hizi hutumia utekelezaji wao wenyewe wa ubadilishaji wa manowari.



**Pendekezo**: Tumia Boltz Exchange kwa unyenyekevu au SwapMarket ili kuongeza gharama kupitia ushindani. Zote mbili ni sawa katika usalama (HTLC isiyo ya chini ya ulinzi).



## Hitimisho



SwapMarket huwezesha ubadilishanaji wa Bitcoin/Lightning kwa kuwakusanya watoa huduma wengi kwenye kiolesura kimoja. Usanifu wa HTLC unahakikisha hali ya ubadilishanaji isiyodhibitiwa, kukosekana kwa KYC huhifadhi usiri, na msimbo wa chanzo huria unaoweza kupangishwa huimarisha upinzani dhidi ya udhibiti.



Ushindani kati ya watoa huduma huboresha viwango na kuzidisha vyanzo vya ukwasi. Ili kuboresha usimamizi wa safu mbili (akiba ya on-chain, gharama za Umeme), SwapMarket ni zana inayotumika ambayo huhifadhi uhuru wa kifedha na usiri.



## Rasilimali



### Nyaraka rasmi




- [SwapMarket - Programu ya Wavuti](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Nyaraka za kiufundi](https://docs.boltz.exchange/)
- [Elekeza upangishaji binafsi](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Miradi inayohusiana




- [Boltz Exchange](https://boltz.exchange) - Huduma asili ya kubadilishana atomiki
- [Mabadiliko ya ZEUS](https://zeusln.com) - Mtoa huduma za kubadilishana umeme