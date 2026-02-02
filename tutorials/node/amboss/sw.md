---
name: Amboss
description: Chunguza na uchanganue Lightning Network
---

![cover](assets/cover.webp)



Lightning Network ni Layer ya itifaki ya Bitcoin, ambayo ilitengenezwa kimsingi ili kukuza upitishwaji wa malipo ya Bitcoin siku hadi siku kwa kuongeza kasi ya uchakataji wa kila shughuli. Kulingana na kanuni ya ugatuaji, Lightning Network inajumuisha nodi (kompyuta zinazoendesha utekelezaji wa Umeme) zinazowasiliana na wenzao, zikitoa data (malipo na uthibitishaji wa malipo) kwa kila mmoja.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Kama ilivyo kwenye msururu mkuu, imekuwa muhimu kuwawezesha watumiaji kujua taarifa na hali ya mtandao, ili kuwezesha miunganisho kati ya nodi na kupunguza tatizo la ukwasi ambalo kwa ujumla hujitokeza katika mtandao. Hakika, kwenye Lightning Network, tunapendekeza malipo madogo ya kiasi kidogo zaidi kuliko yale ya miamala kwenye msururu mkuu wa Bitcoin.



Ni muhimu kutambua kwamba sio nodi zote za Umeme zinapatikana kwenye jukwaa la Amboss.



Kama vile [Mempool Space](https://Mempool.space), ambayo hutoa maelezo muhimu kuhusu msururu mkuu wa itifaki ya Bitcoin, tangu 2022 [Amboss](https://amboss.space) hutoa maelezo kuhusu :





- Nodi kwenye Lightning Network
- Njia za malipo na uwezo wao wa malipo
- Mageuzi ya Lightning Network kwa wakati
- Takwimu za gharama za kutuma nodi za malipo yako.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Katika somo hili, tutakuchukua kwenye ziara ya jukwaa hili, ambalo ni nyenzo muhimu kwa watumiaji wa Lightning Network, wale wanaotaka kuunganisha nodi zao ili kupanua mtandao, n.k.




## Tafuta jozi



Moja ya malengo ya jukwaa la Amboss ni kuwezesha nodi mbalimbali kwenye mtandao kuungana na kuwasiliana habari kwa kila mmoja. Kwenye ukurasa wa nyumbani wa jukwaa, unaweza kutafuta moja kwa moja jina la nodi ambayo tayari unajua, au kupata nodi kutoka kwa jalada maarufu la Umeme unalotumia.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Kwenye ukurasa wa nyumbani, utapata pia nodi zilizoainishwa kulingana na:




- Capacity evolution: idadi ya Bitcoin inayohusishwa na ufunguo wa umma wa nodi na jumla inayopatikana katika chaneli zake zote.
- Mageuzi ya kituo: idadi ya miunganisho mipya kwa nodi zingine kwenye mtandao.
- Umaarufu wa nodi: mara ngapi node hutumiwa.



![nodes](assets/fr/03.webp)



Kuchagua nodi sahihi ya kuunganishwa kwa hivyo inakuja chini kwa kuangalia vigezo vifuatavyo:





- Hakikisha kwamba node ina kiasi cha kutosha cha bitcoins; uwezo mkubwa wa node, kiasi kikubwa cha bitcoins unaweza kulipa.





- Hakikisha kwamba nodi ina idadi kubwa ya viunganisho na njia wazi na nodi nyingine kwenye mtandao.





- Hakikisha nodi inatumika na bado inathaminiwa na wenzao kwa kuangalia idadi ya vituo vipya; njia mpya zaidi nodi hii imefunguliwa, ndivyo inavyothaminiwa na nodi zingine kwenye mtandao.



Mara tu unapopata nodi sahihi, bonyeza kwenye jina lake ili kuelekezwa kwenye ukurasa wa habari wa nodi.



Kwenye Interface hii, kwa kuangalia Timestamp ya chaneli mpya iliyoundwa, utapata kidokezo cha shughuli ya nodi hii. Utapata pia maelezo kuhusu uwezo wa vituo vya nodi hii: maelezo haya ni muhimu ikiwa ungependa kutumia nodi hii kikamilifu kufanya malipo yako.




![node_info](assets/fr/04.webp)



Katika sehemu ya mkono wa kushoto, utapata maelezo zaidi kuhusu eneo la nodi hii. Kwa mfano, unaweza kutazama:




- Kitufe cha umma: kitambulisho chini ya jina la nodi.
- Nafasi ya kijiografia ya nodi hii.




![channels](assets/fr/05.webp)



Interface hii inakuambia muunganisho wa Address wa nodi hii: inachukua fomu `pubkey@ip:port`. Katika mfano wetu, tunataka kuunganishwa na nodi ambayo :




- ufunguo wa umma `pubkey` ni: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- Bandari: `9735`



![geoinfo](assets/fr/06.webp)



Katika sehemu ya **Vituo**, utaona orodha ya njia zilizo wazi na miunganisho ya nodi kwenye nodi nyingine kwenye mtandao. Kwenye Interface hii, taarifa kadhaa ni muhimu ili kuthibitisha kwamba nodi hii inalingana na mahitaji yetu au inategemewa:





- Uwiano unaoingia**: Kiasi ambacho nodi itakutoza kwa kila milioni Satoshi itapokea, kulingana na kituo kilichochaguliwa.
- Uwiano (sehemu kwa milioni)** : ambayo inawakilisha idadi ya Satoshi kwa kila milioni ambayo nodi itakutoza unapoamua kufanya malipo kupitia mojawapo ya chaneli zake. Tuseme umeamua kufanya malipo ya `10_000 Sats` kupitia chaneli ambayo uwiano wake wa ppm ni `500 Sats`, itabidi ulipe nodi `10_000 * 500 / 1_000_000` satoshis, sawa na `5 Sats`.
- Kiwango cha juu zaidi cha [HTLC](https://planb.academy/resources/glossary/htlc)** : Kiasi cha juu zaidi cha nodi hii hukuruhusu kupita kupitia mojawapo ya vituo hivi.



Kwa kushauriana na jedwali katika Interface hii, unaweza pia kupata maelezo haya yote kwenye nodi ambayo inalinganishwa nayo.



![channels_info](assets/fr/07.webp)



Katika sehemu ya **Ramani za vituo**, unaweza kuona usambazaji na uwezo wa chaneli mbalimbali kwenye nodi hii. Unaweza kubadilisha kigezo cha usambazaji kinachoonyeshwa kwa kuchagua moja ya chaguo kwenye orodha kunjuzi iliyo upande wa kulia.



![cha_maps](assets/fr/08.webp)



Sehemu ya **Vituo vilivyofungwa** hupanga chaneli zote za zamani za nodi kulingana na aina ya kufungwa:




- Kufunga kwa pande zote**: kunawakilisha makubaliano ya pande zote mbili, ambao hutumia ufunguo wao wa kibinafsi kutia saini muamala unaoashiria kufungwa kwa chaneli na usambazaji wa salio ndani yake.
- **Kufungwa kwa lazima**: kunawakilisha kufungwa kwa ghafla, kwa upande mmoja kwa sehemu moja ya kituo. Aina hii ya kufungwa haipendekezwi, kwa kuwa Lightning Network ni itifaki inayozingatia adhabu: unapojaribu kulaghai salio la kituo, una hatari ya kupoteza salio lako lote linalopatikana katika kituo hicho.



![closed](assets/fr/09.webp)



Pata maelezo kuhusu ada za usafiri za kuelekeza malipo yako kupitia kituo kwenye nodi unayotumia



![fees](assets/fr/10.webp)



## Taarifa za mtandao



Amboss inazingatia sio tu habari za wanachama wa mtandao, lakini pia juu ya hali ya mtandao yenyewe.



Katika sehemu ya **Takwimu**, chini ya menyu ya upande wa kushoto ya "Uigaji", utapata grafu inayoonyesha uwezekano wa malipo yaliyofanikiwa kama kipengele cha malipo.



Kwa hakika, utaona kwamba mkondo unapungua kwa sababu, kadri kiasi cha malipo yako kinavyoongezeka, unakuwa na nafasi ndogo ya kuona malipo hayo yakifanyika. Hii inaonyesha tatizo halisi la ukwasi kwenye Lightning Network. Kwa mfano, malipo yako ya `10_000` satoshis yana nafasi `79%` ya kufanywa. Kwa upande mwingine, kwa malipo ya `3_000_000` satoshi una nafasi chini ya `13%` ya kufaulu.



![network](assets/fr/11.webp)



Menyu ya **Takwimu za Mtandao** hukuruhusu kuonyesha takwimu za :




- Njia za malipo
- Nodi
- Uwezo
- Ada
- Mageuzi ya kituo.



![network_stat](assets/fr/12.webp)



Katika menyu ya **Takwimu za Soko**, chaguo la **Maelezo ya Agizo** hukuruhusu kuona mahitaji ya ukwasi kwenye Lightning Network. Grafu hii pia inaweza kuonyesha ni chaneli zipi zinazohitajika zaidi na/au ambazo zina uwezo mkubwa.



![markets](assets/fr/13.webp)




## Zana



Amboss inatoa zana kadhaa ili kukusaidia kuboresha utafutaji na vitendo vyako.



### Avkodare ya Lightning Network



Zana hii ina jukumu kubwa la kukupa maelezo ya muundo wa Umeme Invoice, Umeme Address au URL ya Umeme.



Kwenye ukurasa wa nyumbani, katika sehemu ya **Zana**, wasilisha Umeme Address yako, kwa mfano.



![decoder](assets/fr/14.webp)



Kutoka kwa avkodare hii, unaweza kupata taarifa kama vile:




- ufunguo wa umma wa nodi unaohusishwa na Umeme Address yako;
- Muda wa kuisha kwa Invoice kutoka kwa Address yako;
- Kiwango cha chini na cha juu unaweza kutuma;
- Nodi ya Nostr inayohusishwa na Address yako, ikiwa Nostr imewezeshwa kwenye nodi hii.



![decode](assets/fr/15.webp)



### Magma IA



Gundua zana ya hivi punde iliyozinduliwa na Amboss ili kudhibiti vyema miunganisho yako kwenye nodi za Lightning Network. Magma AI hutumia akili ya kujitolea ya bandia ili kuzingatia tatizo muhimu: kufanya uteuzi mzuri wa nodi za kuunganisha.



![magma](assets/fr/16.webp)



### Kikokotoo cha Satoshi



Jua bei ya sasa ya Bitcoin katika sarafu ya nchi yako (EUR/USD). Kwenye ukurasa wa nyumbani, tumia kikokotoo cha satoshis ili kujua bei ya sasa ya soko.



![calculator](assets/fr/17.webp)




Sasa umetembelea kikamilifu vipengele na zana za uchambuzi wa jukwaa. Tafadhali pata chini ya makala yetu juu ya mchunguzi wa Bitcoin **Mempool.space**.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f