---
term: ADA ZA UAMINIFU
---

Ada za muamala zinawakilisha jumla ambayo inalenga kulipa fidia wachimbaji kwa ushiriki wao katika utaratibu wa Proof of Work. Ada hizi zinawahimiza wachimbaji kujumuisha miamala katika vitalu wanavyounda. Yanatokana na tofauti kati ya jumla ya kiasi cha pembejeo na jumla ya kiasi cha matokeo katika muamala:


```text
fees = inputs - outputs
```


Zinaonyeshwa kwa `Sats/vBytes`, ikimaanisha kuwa ada hazitegemei kiasi cha bitcoins zilizotumwa, lakini kwa uzito wa manunuzi. Wanachaguliwa kwa uhuru na mtumaji wa shughuli na kuamua kasi yake ya kuingizwa kwenye block kupitia utaratibu wa mnada. Kwa mfano, tuseme nitafanya muamala kwa kuingiza `100,000 Sats`, pato la `40,000 Sats`, na pato lingine la `58,500 Sats`. Jumla ya matokeo ni `98,500 Sats`. Ada zilizotengwa kwa shughuli hii ni `1,500 Sats`. Miner inayojumuisha muamala wangu inaweza kuunda `1,500 Sats` katika Coinbase Transaction yao katika Exchange kwa `1,500 Sats` ambayo sikuipata katika matokeo yangu.


Shughuli zilizo na ada ya juu, kulingana na ukubwa wao, zinachukuliwa kama kipaumbele na wachimbaji, ambayo inaweza kuharakisha mchakato wa uthibitishaji. Kinyume chake, miamala iliyo na ada ya chini inaweza kucheleweshwa wakati wa msongamano mkubwa. Ni vyema kutambua kwamba ada za shughuli za Bitcoin ni tofauti na ruzuku ya kuzuia, ambayo ni motisha ya ziada kwa wachimbaji. Block reward ina bitcoins mpya iliyoundwa na kila block iliyochimbwa (ruzuku ya kuzuia), pamoja na ada za ununuzi zilizokusanywa. Ingawa ruzuku ya kuzuia inapungua kwa muda kutokana na kikomo cha jumla cha Supply cha bitcoins, ada za miamala zitaendelea kuwa na jukumu muhimu katika kuhimiza wachimbaji kushiriki.


Katika kiwango cha itifaki, hakuna kinachozuia watumiaji kujumuisha miamala bila ada zozote kwenye kizuizi. Kwa kweli, aina hii ya shughuli isiyo na ada ni ya kipekee. Kwa chaguo-msingi, nodi za Bitcoin hazileti tena miamala kwa ada zilizo chini ya `1 sat/vBytes`. Ikiwa baadhi ya shughuli zisizo na ada zimepita, ni kwa sababu ziliunganishwa moja kwa moja na Miner iliyoshinda, bila kuvuka mtandao wa nodi. Kwa mfano, muamala ufuatao haujumuishi ada:


```text
fd456524104a6674693c29946543f8a0befccce5a352bda55ec8559fc630f5f3
```


Katika mfano huu maalum, ilikuwa shughuli iliyoanzishwa na mkurugenzi wa F2Pool Mining pool. Kama mtumiaji wa kawaida, kikomo cha chini cha sasa ni `1 sat/vBytes`.

Pia ni lazima kuzingatia mipaka ya kusafisha. Wakati wa msongamano mkubwa, kumbukumbu za nodi husafisha shughuli zao zinazosubiri chini ya kiwango fulani, ili kuheshimu kikomo cha RAM kilichotengwa. Kikomo hiki kinachaguliwa kwa uhuru na mtumiaji, lakini wengi huacha thamani ya msingi ya Bitcoin Core kwa 300 MB. Inaweza kurekebishwa katika faili ya `Bitcoin.conf` kwa kigezo cha `maxmempool`.

> ► *Kwa Kiingereza, tunairejelea kama "ada za muamala".*