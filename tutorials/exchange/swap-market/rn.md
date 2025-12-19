---
name: SwapMarket
description: Bitcoin n'umuravyo guhindura ibikorwa
---

![cover](assets/cover.webp)



Kwimurira amafaranga hagati ya Bitcoin on-chain na Lightning Network muri rusangi bisaba gufungura n’amaboko imirongo ya Lightning (ivy’ubuhinga n’ibihenda), canke gukoresha ama platforms y’uguhinduranya amafaranga hamwe na KYC. SwapMarket itanga ubundi buryo: uguhinduranya atome ata kwizigirwa biciye ku batanga amafaranga, ata KYC.



Ivyiza bishasha: naho abatanga amafaranga ari abahuza, HTLC (*Amasezerano y’Igihe Gifunze ya Hash*) mu mibare yemeza ko amahera yawe aguma munsi y’ububasha bwawe. Ihuriro ry’abatanga amakuru benshi (Boltz, ZEUS Swaps, Eldamar, Inzira yo hagati) rituma haba uguhiganwa kw’ibiciro. Interface urubuga rwuguruye-inkomoko ukwikira.



## Isoko ry’uguhinduranya ni iki?



Igikoresho co gukoranya amakuru gifunguye catangujwe mu 2024, SwapMarket gikora nk’ikigereranyo c’abatanga amakuru y’ubuhinga bwa Bitcoin/Lightning. Uwukoresha aca agereranya ivyangombwa (amahera, amahera, imipaka) maze agahitamwo uwutanga ubufasha bwiza.



### Ubwubatsi bw'ubuhinga



**Uruhande rw'umukiriya rw'imbere**: 100% uruhande rw'umukiriya (fork Boltz Web App) rwakira kuri paji za GitHub. Kode ikora mu mucukumbuzi ata server y'inyuma. Amateka abitswe aho hantu (ibifungurwa/ububiko). Kode y’inkomoko ya bose kandi ishobora gusuzumwa.



**Ukuvumbura kw'abatanga** : Urutonde rw'amakode akomeye muri `src/imiterere/mainnet.ts`. Abatanga ubufasha bashasha bongeweko biciye ku Gusaba canke kuri email.



**Ivyuma vy’inyuma vyigenga**: Buri mutanga amakuru akoresha ivy’inyuma vyiwe vya Boltz. Ikigaragara kibaza APIs mu gihe nyaco kugira ngo ugereranye amajambo avugwa ubwo nyene.



**HTLC Atomic Swaps**: Amasezerano ya Hash y’Igihe Gifunze atanga icemezo c’uko atome ari: canke iyo swap irashitsa, canke buri ruhande rugasubirana amahera yayo. Ico kibazo c’abafatanyabikorwa kirakurwaho mu biharuro.



### Filozofiya



SwapMarket igabanya ugushira hamwe mu kurema uguhiganwa hagati y’abatanga amafaranga n’amahera. Nta KYC, kode y’ukwikira y’inkomoko yuguruye, ugukuza abakoresha bigenga kugira ngo ntihagire ingingo zimwe zimwe zishobora kunanirwa.



## Ibirango nyamukuru



### Isoko ry'abatanga



Igikoresho kigaragaza abatanga ubufasha bose bakora: izina ry’uwutanga ubufasha, amafaranga akoreshwa (ijanisha na/canke ataco akora), amafaranga make/manini ariho, n’ubwoko bw’uguhindura bushigikiwe. Porogaramu irasaba ataco ihinduye APIs z'umutanga buri wese yerekanwa muri dosiye y'imiterere kugira ngo ibone amajambo mu gihe nyaco. Amahiganwa hagati y’abatanga amafaranga atanga ibiciro vyiza, muri rusangi hafi 0,5% ku bipimo bisanzwe.



### Guhinduranya inzira zibiri



**Guhindura (on-chain → Umuravyo)**: Guhindura on-chain BTCs mu satoshis z’umuravyo. Ikoreshwa ry’ikibazo: guha ubushobozi umuravyo wallet ugendagenda, kuronka ubushobozi bwo kwinjira ku nzira, canke kugira amahera ako kanya.



**Guhindura-inyuma (Umuravyo → on-chain)**: Guhindura satoshis z’umuravyo mu on-chain BTC. Ikoreshwa ry’ikibazo: gukura ubusa wallet Lightning mu kubika ibintu bikonje canke gusubiramwo uburinganire bw’amazi hagati y’ibice.



### Umutekano n'ugukira



**Trustless atomic swaps**: HTLCs zitanga icemezo c’uko iyo nzira y’uguhinduranya irangiriye mu buryo bushitse, canke ko buri ruhande ruzosubirana umugabane waryo. Ico kibazo c’abafatanyabikorwa kirakurwaho mu biharuro.



**Uburyo bwo kwishura**: Buri swap irafise igihe co gufunga. Iyo iyo swap inaniwe, ayo mahera arasubirwamwo ubwo nyene amaze guhera. Uwukoresha yama afise uburenganzira bwo gusubira gusaba amahera yiwe.



**Imfunguruzo zo gusubiza**: SwapMarket iragufasha kwohereza hanze imfunguruzo zo gusubiza amahinduka ariko arakorwa. Iyo habaye ingorane, izo mfunguruzo zirashobora gukoreshwa mu gusozera canke gukuraho uguhinduranya kuva ku gikoresho ico ari co cose.



## Gushiramwo no kuronka



### Interface urubuga



SwapMarket ntibisaba gushiramwo. Ushobora kubironka biciye ku mucukumbuzi usuye kuri https://swapmarket.github.io. Kugira ngo ubone ibanga ryinshi, koresha Brave, Firefox ifise ivyungura birwanya gukurikirana, canke LibreWolf. Tor Browser ni nziza kugira ngo urubuga ntirumenyekane.



Nta kwiyandikisha, email canke ukugenzura akaranga bisabwa.



### Ukwakira (ubusabe)



Ku bakoresha b'ubuhinga bipfuza gukuraho ukuvyifatamwo kwose ku rubuga rwemewe rwa GitHub Pages, SwapMarket ishobora gukoreshwa mu karere :



**Biciye kuri npm** :


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Biciye kuri Docker** :


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



Ivyo bikoresho bizoboneka kuri `http://umushitsi w'aho hantu:3000`. Ukwiyakira bituma umuntu ashobora kugenzura neza interface, bikuraho ingorane zo gucengera urubuga rwemewe, kandi bituma kode y’inkomoko igenzurwa imbere y’uko ikoreshwa.



### Imiterere y'intango



**Imiravyo ya Wallet**: Urabe neza ko ufise imiravyo ya wallet ikora (Phoenix, Zewu, BlueWallet, n’ibindi). Ku bijanye n’uguhinduranya, uzo generate invoice y’umuravyo. Ku bijanye n’uguhinduranya, uzoriha invoice y’umuravyo.



**Wallet on-chain**: Ku bijanye n’uguhinduranya, uzokenera wallet Bitcoin on-chain kugira ngo wohereze amahera. Ku bijanye n’uguhinduranya, nutegure aderesi y’ukwakira Bitcoin.



**Imiterere y'ubusa**: SwapMarket ibika amateka y'uguhindura n'ivyo ukunda mu makuru y'umucukumbuzi. Nta guhingura konti bisabwa.



## Ugushika ku miterere n'urufunguzo rwo gukiza



Imbere yo guhindura ibintu vyawe vya mbere, turagusavye cane gukuraho **Urufunguzo rwawe rwo Gukiza**. Urufunguzo rw’ivyihutirwa ruragufasha gusubirana amahera yawe iyo habaye ingorane y’ubuhinga canke iyo utakaje uburenganzira bwo gukoresha igikoresho cawe.



### Ukwinjira mu mirongo ngenderwako



Kuva kuri paji nyamukuru ya SwapMarket, fyonda ku kimenyetso c’ivyuma (⚙️) kiri hejuru iburyo bw’ibarabara, iruhande y’urupapuro rwo guhindura.



![Accès aux paramètres](assets/fr/01.webp)



### Amagenamiterere ya paji



Paje y'imiterere irafunguka, yerekana amahitamwo menshi yo gutunganya:





- Idini**: Guhitamwo BTC canke sats
- Igitandukanya c'icumi**: Igitandukanya c'icumi (, canke .)
- Amatangazo y'amajwi/umucukumbuzi**: Amatangazo y'amajwi n'umucukumbuzi
- Urufunguzo rwo gukiza** : Gukuraho urufunguzo rwo gukira
- Inyandiko**: Raba, gukuraho canke gukuraho inyandiko



![Page Settings](assets/fr/02.webp)



### Gukuraho urufunguzo rwo gukiza



Fyonda kuri buto **Download** iri iruhande y'"Urufunguzo rwo gukiza".



**Ingingo zihambaye** :




- Urufunguzo rwo gukiza ni **urufunguzo rw'ivyihutirwa rwo guhagarara rimwe** rukora ku bindi vyose uzohindura muri kazoza
- Bika urufunguzo ahantu **hatekanye kandi hahoraho** (umucungerezi w'ijambobanga, ububiko bwa digitale)
- Iyo habaye ingorane yo guhindura (igihe kirangiye, ubuhinga butari bwiza), uru rufunguzo ruragufasha gusubirana amahera yawe .



## Guhingura intambwe ku yindi



### Guhindura-inyuma: Umuravyo → Bitcoin



Aka karorero ka mbere kerekana ingene wohindura ama satoshis y’umuravyo mu bitcoins za on-chain.



**Intambwe ya 1: Guhindura imiterere



Kuva kuri paji nyamukuru, hitamwo urupapuro rwo guhindura :




- UMURIRA** (aho hejuru): Shiramwo amahera wipfuza kohereza muri sats Umuravyo (akarorero: 30.000 sats)
- BITCOIN** (ahantu hasi): Amahera uzoronka azoca yerekanwa ubwo nyene inyuma y’aho amafaranga akuweko (akarorero: 29.320 sats)



Mu kibanza co hasi, ushire **aderesi yawe yo kwakira Bitcoin** aho wipfuza kwakira ayo mahera. Suzuma neza iyi aderesi.



Igikoresho gisanzwe ni Boltz Exchange. Amafaranga y’urubuga n’ay’abatanga amakuru yerekanwa neza.



![Configuration swap-out](assets/fr/03.webp)



**Intambwe ya 2: Guhitamwo umutanga**



Fyonda ku rutonde rw'abatanga amafaranga (imbere: "Boltz Exchange") kugira ngo ugaragaze abatanga amafaranga bose bariho.



Idirisha ry'uburyo rifunguka, ryerekana imbonerahamwe y'ukugereranya:




- Uko bimeze**: Ikimenyetso ca Green nimba uwutanga ubufasha akora
- Izina ry'umutanga **: Izina ry'umutanga (Boltz Exchange, Inzira yo Hagati, Eldamar, ZEUS Ihindura)
- Amafaranga**: Amafaranga akoreshwa n’uwutanga (muri rusangi hagati ya 0,49% na 0,5%)
- Max Swap**: Amahera menshi yemerewe guhindura



Gereranya amafaranga n’amahera menshi, hanyuma uhitemwo uwuguha ivyo ushaka.



**Iciyumviro**: Igikoresho co guhitamwo abatanga ubufasha ntikigaragaza **amafaranga makeyi** y'umutanga ubufasha wese. Aya makuru aboneka gusa mu nzira yo kurema swap, inyuma y'aho umutanga amakuru atoranijwe. Igiciro gitoyi n’ikinini gishobora gutandukanywa n’uwutanga, kandi gishobora guhinduka uko igihe kigenda kirarenga. **Igihe cose urabe ivyo bipimo igihe uriko urahindura**: nimba amahera wipfuza guhindura ari hanze y’ibipimo vy’umuguzi, urashobora guhitamwo uwundi akwiriye cane ku bijanye n’uguhindura kwawe.



![Sélection du provider](assets/fr/04.webp)



**Intambwe ya 3: Guhindura irema n'Umuriro** kwishura



Fyonda ku buto bw'umuhondo **"REMA ATOMIC SWAP "**. SwapMarket izoguha **Ifacture y’umuravyo** (BOLT11) kugira ngo uyihe ukoresheje umuravyo wawe wa wallet.



Urupapuro rwerekana :




- Guhindura ID**: Ikimenyetso c'uguhindura kidasanzwe (akarorero: J4ymFIMVR6Hm)
- Uko bimeze**: "swap.created" (swap yaremwe, irindiriye kwishurwa)
- Kode ya QR**: Icapura ukoresheje umuravyo wawe wallet
- Invoice Umuravyo**: Urudodo rw'inyuguti rutangura na "lnbc" (akarorero: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Ishura iyi fagitire ukoresheje umuravyo wawe wallet (Phoenix, Zewu, BlueWallet, n’ibindi). Amahera nyayo akwiye kwishurwa aragaragazwa (akarorero: 30.000 sats).



![Paiement Lightning](assets/fr/05.webp)



**Intambwe ya 4: Kwemeza no kwemera**



Igihe ukwishyura kwa Lightning kwemejwe, SwapMarket ica ironka ubwo nyene ukwishyura kwawe maze uwutanga amahera agaca atangaza amahera ya Bitcoin kuri aderesi yawe.



Ivyo bihinduka **"invoice.settled "** (invoice yishuwe), kandi ubutumwa bwo kwemeza buragaragazwa.



Ama bitcoins yawe ya on-chain azoboneka igihe nyene iyo nzira yemejwe (kenshi iminota mikeyi gushika ku masaha makeyi, bivanye n’amahera ya mining yatowe n’uwutanga).



![Confirmation swap-out](assets/fr/06.webp)



Ushobora gukanda kuri **"GUFUNGURA IVYO GUSHIRAHO "** kugira ngo ubone ibikorwa vya Bitcoin ku mucukumbuzi wa blockchain.



### Guhinduranya: Bitcoin → Umuravyo



Aka karorero ka kabiri kerekana ingene wohindura ama bitcoins ya on-chain mu ma satoshis y’umuravyo.



**Intambwe ya 1: Guhindura imiterere



Kuva kuri paji nyamukuru, hitamwo urupapuro rwo guhindura :




- BITCOIN** (aho hejuru): Shiramwo amahera wipfuza kohereza mu sats Bitcoin (akarorero: 63.400 sats)
- LIGHTNING** (aho hasi): Amahera uzoronka azoca yerekanwa ubwo nyene umaze gukurako amahera (akarorero: 62 884 sats)



Mu kibanza co hasi, shiramwo invoice ya Lightning** (BOLT11) yavuye mu wallet Lightning yawe, canke ukoreshe aderesi yawe ya LNURL nimba wallet yawe ibishigikira.



![Configuration swap-in](assets/fr/07.webp)



**Intambwe ya 2: Gusuzuma urufunguzo rwo gukiza**



Uhejeje gukanda kuri **"CREATE ATOMIC SWAP "**, idirisha ry'uburyo riraboneka, rigusaba kugenzura Urufunguzo rwawe rwo Gukiza.



![Modal Rescue Key](assets/fr/08.webp)



**Boltz Rescue Key**: Nk'uko umaze gushiramwo urufunguzo rwawe rwo gusubirana mu gihe c'ugutunganya kwa mbere (raba igice c'imbere), fyonda ku buto **"VERIFY EXISTING KEY "** kugira ngo ushiremwo urufunguzo wabitse.



Hitamwo dosiye y’Urufunguzo rw’Ugukiza wari warakuweho mbere. Inyuma y’ugusuzuma neza, iyo interface irahita ihindukira ikaja ku ntambwe ikurikira.



**Intambwe ya 3: Bitcoin** aderesi yo kubika



SwapMarket ubu itanga **aderesi yihariye ya Bitcoin** irimwo amasezerano ya HTLC ahuye n’inyandiko yawe ya Lightning.



Urupapuro rwerekana :




- Guhindura ID**: Ikimenyetso kidasanzwe (akarorero: 1kGmB6JyGqU4)
- Uko bimeze**: "invoice.set" (invoice iteguwe, irindiriye kwishurwa Bitcoin)
- Kode ya QR**: Aderesi y'ububiko bwa Bitcoin
- Bitcoin** aderesi: Kenshi itangura na "bc1p..." (akarorero: bc1p5mvtwxapjkds...9d4n9f)
- Imburi mu muhondo** : "Urabe neza ko amafaranga yawe yemezwa mu masaha ~24 inyuma y'aho ukoreye iyi swap!"



Ico kiringo c'amasaha ~24 ni **igihe co guhera** c'amasezerano ya HTLC. Iyo amafaranga yawe ya Bitcoin ataremejwe muri iki gihe, iyo swap izonanirwa kandi uzokenera gukoresha Urufunguzo rwawe rwo Gukiza kugira ngo ugarure amahera yawe.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Ushobora gukopa aderesi ukanda kuri buto **"ADERESI "**, canke ugacapura kode ya QR ukoresheje wallet on-chain yawe.



**Intambwe ya 4: Kwohereza ama bitcoins**



Kuva kuri wallet Bitcoin on-chain yawe, wohereze **neza neza** umubare werekanwa (nk'akarorero 63.400 sats) kuri aderesi yashizweho.



**Igihambaye**: Koresha amafaranga akwiye ya mining kugira ngo ushobore kwemezwa vyihuse. Iyo amafaranga ari make cane kandi igikorwa kiguma muri mempool kirenze igihe (~24h), swap izonanirwa.



Igihe amafaranga yoherejwe, SwapMarket ibona ko ari muri mempool maze igaragaza :




- Igihugu** : "ibikorwa.mempool
- Ubutumwa**: "Igurisha riri muri mempool - Ririndiriye kwemezwa kugira ngo rirangize guhindura"



![Transaction en mempool](assets/fr/10.webp)



**Intambwe ya 5: Kwemeza n'Ukwakira Umuravyo**



Igihe nyene igikorwa ca Bitcoin kironka icemezo ca mbere, uwugutanga aca ariha ubwo nyene invoice yawe ya Lightning. Uca ubona ubwo nyene ama satoshis ku ndege yawe wallet Lightning.



Uko bimeze bihinduka **"ugucuruza.ikirego.kurindiriye "**, hanyuma ubutumwa bwo kwemeza buragaragazwa:



![Confirmation swap-in](assets/fr/11.webp)



Ivyo bikoresho vyawe vy’umuravyo biraca biboneka muri wallet yawe.



## Inyungu n'aho bigarukira



### Inyungu



**Ihiganwa ry’ibiciro**: Ugukoranya abatanga ubufasha bituma haba uguhiganwa kw’ibiciro (0.49% gushika kuri 0.5%).



**Ibanga**: Nta KYC, 100% interface y’uruhande rw’umukiriya (nta gutanga amakuru y’umuntu ku giti ciwe), Tor Browser ihuye.



**Ibitagira ububiko**: HTLC mu mibare itanga icemezo c’uko ari yo yonyene igenzura amahera yawe. Canke iyo swap iraroranirwa, canke ugasubira kuronka ama bitcoins yawe.



**Open-source self-hostable**: kode ya bose ishobora gusuzumwa, ishobora gukoreshwa mu karere kugira ngo ishobore kurwanya cane ugucengera.



### Ivyo bigarukira



**Ivyuma bike**: Umubare muto w’abatanga ubufasha (Boltz, Eldamar, MiddleWay bivanye n’igihe). Amahera menshi yoshobora kuba make.



**Igihe co guhera**: Igihe co guhera kuva isaha 24h gushika isaha 48h. Iyo igikorwa ca on-chain kitaremejwe imbere y’uko gihera, birakenewe ko umuntu asubirana n’amaboko.



**Interface gushiramwo**: Naho ishobora kwakira, urubuga rwemewe rwakira kuri GitHub Pages. Iyo GitHub igenzura repo, ukwinjira biciye kuri swapmarket.github.io bizobuzwa (umuti: kwiyakira).



**Ivyiyumviro vya on-chain**: Ivyanditswe vya HTLC birashobora kumenyekana biciye ku gusesangura kw’ivy’ubuhinga bwa none.



## Ibikorwa vyiza



### Gutunganya bitekanye



**Kura Urufunguzo rwawe rwo Gukiza**: Imbere y’uko uhinduranya ubwa mbere, gukura Urufunguzo rwawe rwo Gukiza mu Mitunganyirize (raba igice kigenewe haruguru). Urufunguzo rudasanzwe ruzokora ku bindi vyose uzohindura muri kazoza, bigufashe gusubirana amahera yawe iyo habaye ingorane.



**Koresha Tor Browser**: Kugira ngo ubone ibanga ryinshi, genda kuri SwapMarket uciye kuri Tor Browser kugira ngo uhishe aderesi yawe ya IP.



**Iyumvire ukwiyakira**: Ku bakoresha b'ubuhinga, gukoresha instance yawe bwite ya SwapMarket bikuraho kwizigira ku rwego rwa GitHub Pages.



### Guhindura neza



**Guma ushize ijisho kuri mempool**: Suzuma mempool.space imbere yo guhindura. Hitamwo ibihe vy’ibikorwa bike kugira ngo ugabanye igiciro ca mining.



**Suzuma amaderesi**: Ku bijanye n’uguhinduranya, suzuma neza aderesi yawe yo kwakira. Koresha copy and paste maze usuzume inyuguti 5 za mbere n’inyuguti 5 za nyuma.



**Igerageza n’amahera make**: Utangure n’amahera makeyi yemerewe (25.000 gushika 50.000 sats). Wongere buhoro buhoro umaze kumenya neza ingene ivyo bigenda.



**Inyandiko y'ivyo uhinduye**: Niwandike ID y'ivyo uhinduye vyose, aderesi y'ugucungura n'itariki bizoherako. Aya makuru arafasha gukurikirana no gusubirana iyo habaye ingorane y’ubuhinga.



### Ingamba zo gukoresha



**Uringanize amafaranga yawe**: Koresha SwapMarket kugira ngo utunganye amafaranga yawe hagati ya on-chain (amahera uzigamye, umutekano w’igihe kirekire) na Lightning (amahera ukoresha ku musi, amahera ukoresha ubwo nyene) bivanye n’ivyo ukeneye vy’ukuri.



**Harurira inyungu**: Ku bikenewe vy’amahera vya Lightning bihoraho, gereranya igiciro c’amahera y’ugusubiramwo n’ugufungura umurongo wa Lightning ataco uhinduye. SwapMarket iraruta ayandi ku guhindura rimwe gusa, si ngombwa ku bijanye n’imigenderanire myinshi idasanzwe.



## SwapMarket na Boltz: Ni igiki gitandukanye?



### Boltz: Ikoranabuhanga n'Ibikorwa



**Boltz ni ubuhinga bufunguye** (`boltz-backend` kuri GitHub) bushira mu ngiro uguhinduranya atome biciye kuri HTLC hagati ya Bitcoin, Umuravyo na Liquid.



**Iciyumviro gihambaye**: Abatanga SwapMarket bose (Boltz Exchange, ZEUS Swaps, Eldamar, Inzira yo Hagati) bakoresha urugero rwabo rw’inyuma rwa Boltz. Ubuhinga bushingiyeko rero burasa. Igihombo kiri mu nyuma ya Boltz coshobora gutera ingaruka ku batanga amakuru bose, ariko uburyo bw’inkomoko yuguruye bw’uburyo bushobora gutuma habaho igenzura ry’abanyagihugu.



**Boltz Exchange** ni igikorwa kimwe gikoreshwa n’umugwi wa Boltz, mu gihe **SwapMarket** ihuriza hamwe abatanga amakuru benshi bose bakoresha ubuhinga bwa Boltz, bikaba bituma habaho uguhiganwa kw’ibiciro.



Raba inyigisho zacu za Boltz na Zeus Swap kugira ngo umenye vyinshi:



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Ubutandukane nyamukuru



| Igice        | Boltz Exchange       | SwapMarket                           |
| ------------ | -------------------- | ------------------------------------ |
| Kamere        | Serivisi idasanzwe   | Uhuza ba-provider benshi             |
| Abatanga      | Boltz gusa           | Boltz, ZEUS, Eldamar, Middle Way     |
| Amahiganwa    | Amafaranga ahamye    | Amahiganwa adafashe                  |
| Imigaragarire | boltz.exchange       | swapmarket.github.io (ishobora kwihangira) |
| Umutekano      | Non-custodial (HTLC) | Non-custodial (HTLC)                 |

**Ivyiza vya SwapMarket**: Guhiganwa mu biciro, guhindura instances z’inyuma, kugereranya igihe nyaco.



**Ibindi bikoresho vy'ubuhinga** (ntibihuye n'isoko rya Swap): Umuravyo (Ibikorwa vy'umuravyo), Muun Wallet, NLoop, Breez Wallet. Ivyo bisubizo bikoresha uburyo bwavyo bwite bwo guhinduranya amato yo munsi y’amazi.



**Impanuro**: Koresha Boltz Exchange kugira ngo vyorohe canke SwapMarket kugira ngo ushiremwo ibiciro vyiza biciye mu guhiganwa. Ivyo vyose birangana mu bijanye n’umutekano (HTLC idashobora gucungerwa).



## Iciyumviro



SwapMarket yorohereza uguhanahana kwa Bitcoin/Lightning mu gukoranya abatanga amakuru benshi mu nzira imwe. Ubwubatsi bwa HTLC buratanga icemezo c’uko ama swap ataco akora, ukutagira KYC birazigama ibanga, kandi kode y’inkomoko yuguruye yikorera ikomeza ukurwanya ugucengera.



Guhiganwa hagati y’abatanga ubuvuzi biratuma ibiciro bitera imbere kandi bikagwiza amasoko y’amahera. Kugira ngo uburongozi bw’ibice bibiri bube bwiza (ubuzigama bwa on-chain, amafaranga y’umuravyo), SwapMarket ni igikoresho gikora kizigama ubusegaba bw’ivy’ubutunzi n’ibanga.



## Ubutunzi



### Inyandiko zemewe




- [Isoko ry'Impinduka - Ubukoresho bw'Urubuga](https://isoko ry'Impinduro.github.io)
- [Isoko ry'Ibihindurwa rya GitHub](Isoko ry'Ibihindurwa/Isoko ry'Ibihindurwa.github.io)
- [Inyandiko z'ubuhinga](https://inyandiko.boltz.guhanahana/)
- [Iyobora ry'ukwiyakira](https://github.com/Isoko ry'Impinduka/Isoko ry'Impinduka.github.io/blob/ikuru/README.md)



### Imigambi ijana




- [Boltz Exchange](uburyo bwo guhindura) - Ubuhinga bwo guhindura atome y'umwimerere
- [Impinduro za ZEUS](https://zeusln.com) - Uwutanga impinduka z'umuravyo