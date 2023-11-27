---
name: Teoretiese Inleiding tot die Lightning Network
goal: Ontdek die Lightning Network vanuit 'n tegniese perspektief
objectives:
  - Verstaan hoe die netwerk se kanale werk.
  - Bekend raak met terme soos HTLC, LNURL en UTXO.
  - Assimileer die bestuur van likiditeit en fooie in LNN.
  - Erken die Lightning Network as 'n netwerk.
  - Verstaan die teoretiese gebruike van die Lightning Network.
---

# 'n Reis na Bitcoin se Tweede Laag

Hierdie kursus is 'n teoretiese les oor die tegniese werking van die Lightning Network.

Welkom in die opwindende wêreld van die Lightning Network, 'n tweede laag van Bitcoin wat beide gesofistikeerd en vol potensiaal is. Ons is besig om in die tegniese dieptes van hierdie tegnologie in te duik, sonder om te fokus op spesifieke tutoriale of gebruiksscenario's. Om die meeste uit hierdie kursus te haal, is 'n soliede begrip van Bitcoin noodsaaklik. Dit is 'n ervaring wat 'n ernstige en gefokusde benadering vereis. Jy kan ook oorweeg om gelyktydig die LN 202-kursus te volg, wat 'n meer praktiese aspek aan hierdie verkenning bied. Maak gereed om op 'n reis te gaan wat jou persepsie van die Bitcoin-ekosisteem kan verander.

Geniet die ontdekking!

+++

# Die Fundamentele
## Verstaan die Lightning Network

![Verstaan die Lightning Network](https://youtu.be/PszWk046x-I)

Die Lightning Network is 'n tweede-laag betalingsinfrastruktuur wat op die Bitcoin-netwerk gebou is en vinnige en goedkoop transaksies moontlik maak. Om ten volle te verstaan hoe die Lightning Network werk, is dit noodsaaklik om te verstaan wat betalingskanale is en hoe hulle werk.

'n Lightning-betalingskanaal is 'n soort "privaat baan" tussen twee gebruikers wat vinnige en herhalende Bitcoin-transaksies moontlik maak. Wanneer 'n kanaal geopen word, word dit 'n vaste kapasiteit gegee, wat deur die gebruikers vooraf bepaal word. Hierdie kapasiteit verteenwoordig die maksimum bedrag Bitcoin wat op enige gegewe tyd in die kanaal oorgedra kan word.

Betalingskanale is bidireksioneel, wat beteken dat hulle twee "kante" het. Byvoorbeeld, as Alice en Bob 'n betalingskanaal oopmaak, kan Alice Bitcoin na Bob stuur en Bob kan Bitcoin na Alice stuur. Transaksies binne die kanaal verander nie die totale kapasiteit van die kanaal nie, maar hulle verander wel die verdeling van daardie kapasiteit tussen Alice en Bob.

![verduideliking](assets/chapitre1/0.JPG)

Vir 'n transaksie om moontlik te wees in 'n Lightning-betalingskanaal, moet die gebruiker wat die fondse stuur genoeg Bitcoin aan sy kant van die kanaal hê. As Alice byvoorbeeld 1 Bitcoin na Bob wil stuur deur hul kanaal, moet sy ten minste 1 Bitcoin aan haar kant van die kanaal hê.
Beperkings en Werking van Betalingskanale op Lightning.
Alhoewel die kapasiteit van 'n Lightning-betalingskanaal vasgestel is, beperk dit nie die totale aantal transaksies of die totale volume van Bitcoin wat deur die kanaal oorgedra kan word nie. Byvoorbeeld, as Alice en Bob 'n kanaal met 'n kapasiteit van 1 Bitcoin het, kan hulle honderde transaksies van 0.01 Bitcoin of duisende transaksies van 0.001 Bitcoin uitvoer, solank die totale kapasiteit van die kanaal nie op enige gegewe tyd oorskry word nie.

Ten spyte van hierdie beperkings is Lightning-betalingskanale 'n effektiewe manier om vinnige en goedkoop Bitcoin-transaksies uit te voer. Dit stel gebruikers in staat om Bitcoin te stuur en te ontvang sonder om hoë transaksiefooie te betaal of lank te wag vir bevestigingsperiodes op die Bitcoin-netwerk.

Kortom, Lightning-betalingskanale bied 'n kragtige oplossing vir diegene wat vinnige en goedkoop Bitcoin-transaksies wil uitvoer. Dit is egter noodsaaklik om hul werking en beperkings te verstaan om ten volle daarvan te kan profiteer.

![verduideliking](assets/chapitre1/1.JPG)

Voorbeeld:

- Alice het 100,000 SAT
- Bob het 30,000 SAT
Hierdie is die huidige toestand van die kanaal. Tydens 'n transaksie besluit Alice om 40,000 SAT na Bob te stuur. Sy kan dit doen omdat 40,000 < 100,000.
Die nuwe toestand van die kanaal is dus:

- Alice 60,000 SAT
- Bob 70,000 SAT

```
Aanvanklike toestand van die kanaal:
Alice (100,000 SAT) ============== Bob (30,000 SAT)

Na Alice se oordrag na Bob van 40,000 SAT:
Alice (60,000 SAT) ============== Bob (70,000 SAT)

```
![verduideliking](assets/chapitre1/2.JPG)

Nou wil Bob 80,000 SAT na Alice stuur. Omdat hy nie die vloeibaarheid het nie, kan hy nie. Die maksimum kapasiteit van die kanaal is 130,000 SAT, met 'n moontlike uitgawe van tot 60,000 SAT vir Alice en 70,000 SAT vir Bob.

![verduideliking](assets/chapitre1/3.JPG)

## Bitcoin, adresse, UTXO en transaksies

![bitcoin, adresse, utxo en transaksies](https://youtu.be/cadCJ2V7zTg)

In hierdie tweede hoofstuk neem ons die tyd om te bestudeer hoe Bitcoin-transaksies werk, wat baie nuttig sal wees vir die verstaan van Lightning. Ons bespreek ook kort die konsep van multi-handtekening adresse, wat noodsaaklik is vir die verstaan van die volgende hoofstuk oor die opening van kanale op die Lightning-netwerk.

- Privaatsleutel > Publieke sleutel > Adres: Tydens 'n transaksie stuur Alice geld na Bob. Laasgenoemde verskaf 'n adres wat deur sy publieke sleutel gegee word. Alice, wat self die geld op 'n adres ontvang het via haar publieke sleutel, gebruik nou haar privaatsleutel om die transaksie te onderteken en sodoende die bitcoins van die adres te ontgrendel.
- In 'n Bitcoin-transaksie moet alle bitcoins beweeg. Genoem UTXO (Ongebruikte Transaksie-uitsette), sal die stukkies bitcoin almal vertrek om slegs daarna terug te keer na die eienaar.
  Alice het 0.002 BTC, Bob het 0 BTC. Alice besluit om 0.0015 BTC na Bob te stuur. Sy sal 'n transaksie van 0.002 BTC onderteken waarvan 0.0015 na Bob sal gaan en 0.0005 na haar beursie sal terugkeer.

![verduideliking](assets/chapitre2/0.JPG)

Hier, van een UTXO (Alice het 0.0002 BTC op 'n adres), het ons 2 UTXOs geskep (Bob het 0.0015 en Alice het 'n nuwe UTXO (onafhanklik van die vorige een) van 0.0005 BTC).

```
Alice (0.002 BTC)
  |
  V
Bitcoin-transaksie (0.002 BTC)
  |
  |----> Bob (0.0015 BTC)
  |
  V
Alice (nuwe UTXO: 0.0005 BTC)
```

In die Lightning-netwerk word multi-handtekeninge gebruik. Daarom is 2 handtekeninge nodig om die fondse te ontgrendel, dit wil sê, twee privaatsleutels om die geld te beweeg. Dit kan Alice en Bob wees wat saam moet saamstem om die geld (die UTXO) te ontgrendel. In LN spesifiek is dit 2/2-transaksies, so beide handtekeninge is absoluut noodsaaklik, in teenstelling met 2/3 of 3/5 multi-handtekeninge waar slegs 'n kombinasie van die volledige aantal sleutels vereis word.

![verduideliking](assets/chapitre2/1.JPG)

# Opening en sluiting van kanale
## Kanaalopening

![open 'n kanaal](https://youtu.be/B2caBC0Rxko)

Nou gaan ons 'n nouer kyk na die opening van 'n kanaal en hoe dit gedoen word deur middel van 'n Bitcoin-transaksie.
Die Lightning Network het verskillende vlakke van kommunikasie:
- P2P kommunikasie (Lightning Network-protokol)
- Betalingskanaal (Lightning Network-protokol)
- Bitcoin-transaksie (Bitcoin-protokol)

![verduideliking](assets/chapitre3/0.JPG)

Om 'n kanaal oop te maak, kommunikeer die twee partye deur middel van 'n kommunikasiekanaal:

- Alice: "Hallo, ek wil 'n kanaal oopmaak!"
- Bob: "Ok, hier is my openbare adres."

![verduideliking](assets/chapitre3/1.JPG)

Alice het nou 2 openbare adresse om 'n 2/2 multi-sig adres te skep. Sy kan nou 'n bitcoin-transaksie maak om geld daarheen te stuur.

Stel dat Alice 'n UTXO van 0.002 BTC het en sy wil 'n kanaal oopmaak met Bob van 0.0013 BTC. Sy sal 'n transaksie skep met 2 UTXO's as uitset:

- 'n UTXO van 0.0013 na die 2/2 multi-sig adres
- 'n UTXO van 0.0007 na een van haar veranderingsadresse (terugkeer van UTXO's).

Hierdie transaksie is nog nie openbaar nie, want as dit op hierdie stadium is, vertrou sy Bob om die geld van die multi-sig te kan ontgrendel.

Maar hoe gaan ons nou voort?

Alice sal 'n tweede transaksie skep wat 'n "onttrekkings-transaksie" genoem word voordat die deposito van fondse in die multi-sig gepubliseer word.

![verduideliking](assets/chapitre3/2.JPG)

Die onttrekkings-transaksie sal die fondse van die multi-sig adres na 'n adres van haar spandeer (dit word gedoen voordat alles gepubliseer word).
Nadat beide transaksies gebou is, vertel Alice aan Bob dat dit klaar is en vra hom vir 'n handtekening met sy openbare sleutel, terwyl sy verduidelik dat sy op hierdie manier haar fondse kan herwin as iets verkeerd gaan. Bob stem in omdat hy nie oneerlik is nie.

Alice kan nou die fondse alleen herwin, aangesien sy reeds Bob se handtekening het. Sy publiseer die transaksies. Die kanaal is nou oop met 0.0013 BTC (130,000 SAT) aan Alice se kant.

![verduideliking](assets/chapitre3/3.JPG)

## Lightning Transaksie & Verbintenis Transaksie

![Lightning Transaksie & Verbintenis Transaksie](https://youtu.be/aPqI34tpypM)

![omslag](assets/chapitre4/1.JPG)

Laten ons nou analiseer wat werklik agter die skerms gebeur wanneer fondse van die een kant na die ander van 'n kanaal op die Lightning Network oorgedra word, met die begrip van 'n verbintenis-transaksie. Die on-chain onttrekking/sluitingstransaksie verteenwoordig die toestand van die kanaal en waarborg wie die fondse besit na elke oordrag. So na 'n Lightning Network-oordrag is daar 'n opdatering van hierdie transaksie/kontrak wat nie uitgevoer word tussen die twee partye, Alice en Bob, wat dieselfde transaksie skep met die huidige kanaaltoestand in geval van sluiting:

- Alice maak 'n kanaal oop met Bob met 130,000 SAT aan haar kant. Die onttrekkings-transaksie wat deur beide aanvaar word in geval van sluiting, stel dat 130,000 SAT na Alice sal gaan by sluiting, en Bob stem in omdat dit regverdig is.

![omslag](assets/chapitre4/2.JPG)

- Alice stuur 30,000 SAT na Bob. Daar is nou 'n nuwe onttrekkings-transaksie wat stel dat in geval van sluiting, Alice 100,000 SAT sal ontvang en Bob 30,000 SAT. Beide stem in omdat dit regverdig is.

![omslag](assets/chapitre4/3.JPG)

- Alice stuur 10,000 SAT na Bob, en 'n nuwe onttrekkings-transaksie word geskep wat stel dat Alice 90,000 SAT sal ontvang en Bob 40,000 SAT in geval van sluiting. Beide stem in omdat dit regverdig is.
![cover](assets/chapitre4/4.JPG)

```
Aanvanklike toestand van die kanaal:
Alice (130,000 SAT) =============== Bob (0 SAT)

Na die eerste oordrag:
Alice (100,000 SAT) =============== Bob (30,000 SAT)

Na die tweede oordrag:
Alice (90,000 SAT) =============== Bob (40,000 SAT)

```

Die geld beweeg nooit, maar die finale balans word opgedateer deur middel van 'n ondertekende, maar nie gepubliseerde transaksie op die ketting nie. Die onttrekkingstransaksie is dus 'n verbintenis-transaksie. Die satoshi-oordragte is 'n ander, meer onlangse verbintenis-transaksie wat die balans opdateer.

## Verbintenis-Transaksies

![transaksies deel 2](https://youtu.be/RRvoVTLRJ84)

As verbintenis-transaksies 'n kanaaltoestand met likiditeit op tydstip X bepaal, kan ons bedrieg deur 'n ou toestand te publiseer? Die antwoord is ja, omdat ons reeds die voor-ondertekening van beide deelnemers in die ongepubliseerde transaksie het.

![instruksie](assets/Chapitre5/0.JPG)

Om hierdie probleem op te los, sal ons kompleksiteit toevoeg:

- Tydsluiting = fondse geblokkeer tot blok N
- Herroepingsleutel = Alice se geheim en Bob se geheim'

Hierdie twee elemente word by die verbintenis-transaksie gevoeg. As gevolg hiervan moet Alice wag vir die einde van die Tydsluiting, en enige persoon wat die herroepingsleutel besit, kan die fondse sonder om te wag vir die einde van die Tydsluiting beweeg. As Alice probeer bedrieg, gebruik Bob die herroepingsleutel om te steel en Alice te straf.

![instruksie](assets/Chapitre5/1.JPG)

Nou (en in werklikheid) is die verbintenis-transaksie nie dieselfde vir Alice en Bob nie, hulle is simmetries, maar elkeen met verskillende beperkings, hulle gee mekaar hul geheim om die herroepingsleutel van die vorige verbintenis-transaksie te skep. So by die skepping, skep Alice die kanaal met Bob, 130,000 SAT aan haar kant, sy het 'n Tydsluiting wat haar verhoed om onmiddellik haar geld te herwin, sy moet 'n bietjie wag. Die herroepingsleutel kan die geld ontsluit, maar slegs Alice het dit (Alice se verbintenis-transaksie). Sodra daar 'n oordrag is, sal Alice haar ou geheim aan Bob verskaf en dus kan laasgenoemde die kanaal na die vorige toestand leegmaak in die geval dat Alice probeer bedrieg (Alice word dus gestraf).

![instruksie](assets/Chapitre5/2.JPG)

Op dieselfde manier sal Bob sy geheim aan Alice verskaf. Sodat as hy probeer bedrieg, kan Alice hom straf. Die operasie word herhaal vir elke nuwe verbintenis-transaksie. 'n Nuwe geheim word besluit en 'n nuwe herroepingsleutel. Dus moet vir elke nuwe transaksie die vorige verbintenis-transaksie vernietig word deur die herroepingsgeheim te gee. Sodoende kan die ander optree voordat Alice of Bob bedrieg (dankie aan die Tydsluiting) en sodoende bedrog voorkom. Gedurende transaksie #3 word die geheim van transaksie #2 dus gegee om Alice en Bob in staat te stel om hulself teen Alice of Bob te verdedig.

![instruksie](assets/Chapitre5/3.JPG)

Die persoon wat die transaksie met die Tydsluiting skep (die een wat die geld stuur), kan die herroepingsleutel slegs na die Tydsluiting gebruik. Die persoon wat die geld ontvang, kan dit egter voor die Tydsluiting gebruik in geval van bedrog van een kant na die ander van 'n kanaal op die Lightning Network. In die besonder beskryf ons die meganismes wat ons in staat stel om ons teen moontlike bedrog deur ons eweknie binne die kanaal te beskerm.

## Kanaal Sluiting

![sluit 'n kanaal](https://youtu.be/FVmQvNpVW8Y)
Ons is belangstel in kanaalsluiting deur middel van 'n Bitcoin-transaksie, wat verskillende vorms kan aanneem, afhangende van die geval. Daar is 3 tipes kanaalsluiting:
- Die goeie: samewerkende sluiting
- Die brute: gedwonge sluiting (nie-samewerkende)
- Die bedrieër: sluiting deur 'n bedrieër

![instruction](assets/chapitre6/1.JPG)
![instruction](assets/chapitre6/0.JPG)


### Die goeie

Die twee partye kommunikeer en stem saam om die kanaal te sluit. Hulle staak alle transaksies en valideer 'n finale toestand van die kanaal. Hulle stem in oor netwerkfooie (die persoon wat die kanaal geopen het, betaal die sluitingsfooie). Hulle skep dan die sluitingstransaksie. Daar is 'n sluitingstransaksie, wat verskil van verbintenistransaksies omdat daar geen Tydslot en herroepingsleutel is nie. Die transaksie word dan gepubliseer en Alice en Bob ontvang hul onderskeie balanse. Hierdie tipe sluiting is vinnig (omdat daar geen Tydslot is nie) en oor die algemeen goedkoop.

![instruction](assets/chapitre6/3.JPG)


### Die brute

Alice wil die kanaal sluit, maar Bob reageer nie omdat hy aflyn is (internet- of kragonderbreking). Alice sal dan die mees onlangse verbintenistransaksie (die laaste een) publiseer. Die transaksie word gepubliseer en die Tydslot word geaktiveer. Die fooie is toe besluit toe hierdie transaksie X tyd in die verlede geskep is! Die MemPool is die netwerk wat sedertdien verander het, so die protokol gaan uit van fooie wat 5 keer hoër is as die huidige een wanneer die transaksie geskep is. Skeppingsfooi teen 10 SAT, so die transaksie word beskou as 50 SAT. Met die tyd van gedwonge sluiting is die netwerk:

- 1 SAT = oorbetaal met 50\*
- 100 SAT = onderbetaal met 2\*

Dit maak gedwonge sluiting langer (Tydslot) en veral meer risikovol in terme van fooie en moontlike validering deur mynwerkers.

![instruction](assets/chapitre6/4.JPG)

### Die bedrieër

Alice probeer bedrieg deur 'n ou verbintenistransaksie te publiseer. Maar Bob monitor die MemPool en kyk vir transaksies wat probeer om oues te publiseer. As hy enige vind, gebruik hy die herroepingsleutel om Alice te straf en al die SAT uit die kanaal te neem.

![instruction](assets/chapitre6/5.JPG)

Ten slotte is kanaalsluiting in die Lightning Network 'n kritieke stap wat verskillende vorms kan aanneem. In 'n samewerkende sluiting kommunikeer beide partye en stem in oor 'n finale toestand van die kanaal. Dit is die vinnigste en goedkoopste opsie. Aan die ander kant vind 'n gedwonge sluiting plaas wanneer een party nie reageer nie. Dit is 'n duurder en langer situasie as gevolg van onvoorspelbare transaksiefooie en die aktivering van die Tydslot. As 'n deelnemer uiteindelik probeer bedrieg deur 'n ou verbintenistransaksie te publiseer, kan die bedrieër gestraf word deur al die SAT uit die kanaal te verloor. Dit is dus noodsaaklik om hierdie meganismes te verstaan vir effektiewe en regverdige gebruik van die Lightning Network.

# 'n Vloeibaarheidsnetwerk
## Lightning Network

![Lightning Network](https://youtu.be/RAZAa3v41DM)

In hierdie sewende hoofstuk bestudeer ons hoe Lightning werk as 'n netwerk van kanale en hoe betalings vanaf hul bron na hul bestemming gerouteer word.

![cover](assets/Chapitre7/0.JPG)
![cover](assets/Chapitre7/1.JPG)

Lightning is 'n netwerk van betalingskanale. Duisende eweknieë met hul eie vloeibaarheidskanale is met mekaar verbind en gebruik hulself dus om transaksies tussen nie-verbonde eweknieë uit te voer. Die vloeibaarheid van hierdie kanale kan nie na ander vloeibaarheidskanale oorgedra word nie.
Alice -> Eden -> Bob`. Satoshis het nie beweeg vanaf `Alice -> Bob`, maar vanaf `Alice -> Eden` en vanaf `Eden -> Bob`.
So elke persoon en kanaal het verskillende likiditeit. Om betalings te maak, moet jy 'n roete in die netwerk vind met genoeg likiditeit. As daar nie genoeg is nie, sal die betaling nie deurkom nie.

Oorweeg die volgende netwerk:

```
Aanvanklike toestand van die netwerk:
Alice (130 SAT) ==== (0 SAT) Susie (90 SAT) ==== (200 SAT) Eden (150 SAT) ==== (100 SAT) Bob
```
![cover](assets/Chapitre7/2.JPG)

As Alice 40 SAT na Bob moet oordra, sal die likiditeit herverdeel word langs die roete tussen die twee partye.

```
Nadat Alice 40 SAT na Bob oordra:
Alice (90 SAT) ==== (40 SAT) Susie (50 SAT) ==== (240 SAT) Eden (110 SAT) ==== (140 SAT) Bob
```

![cover](assets/Chapitre7/4.JPG)

Maar in die aanvanklike toestand kan Bob nie 40 SAT na Alice stuur nie omdat Susie geen likiditeit met Alice het om 40 SAT te stuur nie, so betaling is nie moontlik via hierdie roete nie. Ons het dus 'n ander roete nodig waar die transaksie onmoontlik is.

In die eerste voorbeeld is dit duidelik dat Susie en Eden niks verloor het nie en niks gewen het nie. Lightning Network knooppunte hef 'n fooi vir die instemming om gebruik te word om die transaksie te roeteer!

Daar is verskillende fooie, afhangende van waar die likiditeit geleë is.

Alice - Bob

- Alice se fooi = Alice -> Bob
- Bob se fooi = Bob -> Alice

![cover](assets/Chapitre7/5.JPG)

Daar is twee tipes fooie:

- 'n vaste fooi ongeag die bedrag: 1 SAT (verstek maar kan gewysig word)
- 'n veranderlike fooi (0.01% verstek)

Fooi-voorbeeld:

- Alice - Susie; 1/1 (1 vaste fooi en 1 veranderlike fooi)
- Susie - Eden; 0/200
- Eden - Bob; 1/1

Dus:

- Fooi 1: (betaal deur Alice aan haarself) 1 + (40,000 * 0.000001)
- Fooi 2: 0 + 40,000 * 0.0002 = 8 SAT
- Fooi 3: 1 + 40,000 * 0.000001 = 0.4 SAT

![cover](assets/Chapitre7/6.JPG)

Versending:

1. Versending van 40,009.04 Alice -> Susie; Alice betaal haar eie uitgawes, so dit tel nie mee nie
2. Susie doen Eden die guns om 40 001.04 te stuur; sy neem hierdie kommissie van 8 SAT
3. Eden doen die diens om 40,000 na Bob te stuur, hy neem sy fooi van 1.04 SAT.

Alice het 'n fooi van 9.04 SAT betaal en Bob het 40,000 SAT ontvang.

![cover](assets/Chapitre7/7.JPG)

In die Lightning Network is dit Alice se knooppunt wat die roete besluit voordat die betaling gestuur word. Daarom is daar 'n soektog na die beste roete en Alice is die enigste een wat die roete en die prys ken. Die betaling word gestuur, maar Susie het geen inligting nie.

![cover](assets/Chapitre7/9.JPG)
Vir Susie of Eden: hulle weet nie wie die uiteindelike ontvanger is nie, of wie die betaling stuur nie. Dit is uie-roetering. Die node moet 'n plan van die netwerk behou om sy roete te vind, maar geen van die tussenpersone het enige inligting nie.
## HTLC - Gehashte Tydslotkontrak

![HTLC](https://youtu.be/-JC4mkq7H48)

In 'n tradisionele roeteverbindingstelsel, hoe kan ons verseker dat Eden nie vals speel en hul deel van die kontrak nakom nie?

HTLC is 'n betalingskontrak wat slegs met 'n geheim ontgrendel kan word. As dit nie geopenbaar word nie, verval die kontrak. Dit is dus 'n voorwaardelike betaling. Hoe word hulle gebruik?

![instruksie](assets/chapitre8/0.JPG)

Oorweeg die volgende situasie:
`Alice (100,000 SAT) ==== (30,000 SAT) Susie (250,000 SAT) ==== (0 SAT) Bob`

- Bob genereer 'n geheim S (die prentjie) en bereken die hasj r = hasj(s)
- Bob stuur 'n faktuur aan Alice met "r" ingesluit
- Alice stuur 'n HTLC van 40,000 SAT aan Susie met die voorwaarde om "s'" te openbaar sodat hasj(s') = r
- Susie stuur 'n soortgelyke HTLC aan Bob
- Bob ontgrendel Susie se HTLC deur haar "s" te wys
- Susie ontgrendel Alice se HTLC deur haar "S" te wys

As Bob aflyn is en nooit die geheim herwin wat hom die legitimiteit gee om die geld te ontvang nie, sal die HTLC verval na 'n sekere aantal blokke.

![instruksie](assets/chapitre8/1.JPG)

Die HTLC's verval in omgekeerde volgorde: Susie-Bob verval, dan Alice-Susie verval. Op hierdie manier, as Bob terugkeer, verander dit niks nie. Andersins, as Alice kanselleer terwyl Bob terugkeer, sal dit 'n gemors wees en mense het dalk vir niks gewerk.

So, wat gebeur in geval van sluiting? In werklikheid is ons verbintenistransaksies selfs meer ingewikkeld. Ons moet die tussenbalans verteenwoordig as die kanaal gesluit is.

Daar is dus 'n HTLC-uit van 40,000 satoshis (met die beperkings wat voorheen gesien is) in die verbintenistransaksie via uitset #3.

![instruksie](assets/chapitre8/2.JPG)

Alice het in die verbintenistransaksie:

- Uitset #1: 60,000 SAT vir Alice via 'n Tydslot en herroepingsleutel (wat vir haar oorbly)
- Uitset #2: 30,000 wat reeds aan Susie behoort
- Uitset #3: 40,000 in HTLC

Alice se verbintenistransaksie is met 'n HTLC-uit omdat sy 'n HTLC-in na die ontvanger, Susie, stuur.

![instruksie](assets/chapitre8/3.JPG)

Daarom, as ons hierdie verbintenistransaksie publiseer, kan Susie die HTCL-geld herwin met die "s" prentjie. As sy nie die prentjie het nie, herwin Alice die geld sodra die HTCL verval. Dink aan uitsette (UTXO) as verskillende betalings met verskillende voorwaardes.
Sodra die betaling gedoen is (verval of uitvoering), verander die kanaaltoestand en bestaan die transaksie met HTCL nie meer nie. Ons keer terug na iets klassieks.
In die geval van samewerkende sluiting: ons stop betalings en wag dus vir die uitvoering van oordragte/HTCL, die transaksie is lig, dus minder duur omdat daar 'n maksimum van 1 of 2 uitsette is.
In die geval van gedwonge sluiting: ons publiseer met al die HTLC's wat aan die gang is, dit word dus baie swaar en baie duur. En dit is 'n gemors.
Opsomming: Die Lightning Network roetesisteem maak gebruik van Hash Time-Locked Contracts (HTLC) om sekere en verifieerbare betalings te verseker. HTLC's maak voorwaardelike betalings moontlik waar geld slegs met 'n geheim ontgrendel kan word, wat verseker dat deelnemers hul verpligtinge nakom. In die voorbeeld wat voorgehou word, wil Alice SAT na Bob stuur deur Susie. Bob genereer 'n geheim, skep 'n has daarvan en stuur dit aan Alice. Alice en Susie stel 'n HTLC op gebaseer op hierdie has. Sodra Bob Susie se HTLC ontgrendel deur haar die geheim te wys, kan Susie dan Alice se HTLC ontgrendel.

In die geval dat Bob nie binne 'n sekere tydperk die geheim bekend maak nie, verval die HTLC. Verval gebeur in omgekeerde volgorde, wat verseker dat as Bob weer aanlyn kom, daar geen ongewenste gevolge is nie.

By die sluit van die kanaal, as dit 'n samewerkende sluiting is, word betalings onderbreek en HTLC's opgelos, wat gewoonlik minder duur is. As die sluiting gedwing is, word alle aanhoudende HTLC-transaksies gepubliseer, wat baie duur en rommelig kan raak.

Opsomming: Die HTLC-meganisme voeg 'n addisionele laag van sekuriteit by die Lightning Network, wat verseker dat betalings korrek uitgevoer word en dat gebruikers hul verpligtinge nakom.

## Jou pad vind

![jou pad vind](https://youtu.be/wnUGJjOxd9Q)

Die enigste openbare data is die totale kanaalkapasiteit (Alice + Bob), maar ons weet nie waar die likiditeit geleë is nie.
Om meer inligting te verkry, luister ons node na die LN kommunikasiekanaal vir aankondigings van nuwe kanale en opdaterings van kanaalfooie. Jou node kyk ook na die blokketting vir kanaalsluitings.

Aangesien ons nie al die inligting het nie, moet ons soek na 'n grafiek/route met die inligting wat ons het (maksimum kanaalkapasiteit en nie waar die likiditeit geleë is nie).

Kriteria:

- Sukseswaarskynlikheid - Fooie
- HTLC vervaltyd
- Aantal tussenliggende nodes
- Willekeurigheid

![grafiek](assets/chapitre9/1.JPG)

Dus, as daar 3 moontlike roetes is:

- Alice > 1 > 2 > 5 > Bob
- Alice > 1 > 2 > 4 > 5 > Bob
- Alice 1 > 2 > 3 > Bob

Ons is op soek na die beste roete in teorie met die laagste fooie en die hoogste kans op sukses: maksimum likiditeit en so min moontlike hops.

Byvoorbeeld, as 2-3 slegs 'n kapasiteit van 130,000 SAT het, is dit baie onwaarskynlik om 100,000 te stuur, so keuse #3 het geen kans op sukses nie.

![grafiek](assets/chapitre9/2.JPG)

Nou het die algoritme sy 3 keuses gemaak en sal die eerste een probeer:

Keuse 1:

- Alice stuur 'n HTLC van 100,000 SAT na 1;
- 1 maak 'n HTLC van 100,000 SAT na 2;
- 2 maak 'n HTLC van 100,000 SAT na 5, maar 5 kan dit nie doen nie, so kondig dit aan.

Die inligting word teruggestuur, dus besluit Alice om die tweede roete te probeer:

- Alice stuur 'n HTLC van 100,000 na 1;
- 1 maak 'n HTLC van 100,000 na 2;
- 2 maak 'n HTLC van 100,000 na 4;
- 4 maak 'n HTLC van 100,000 na Bob. Bob het die likiditeit, so dit is reg.
- Bob gebruik die prentjie (has) van die HTLC en gebruik dus die geheim om die 100,000 SAT te herwin.
- 5 het nou die geheim van die HTLC om die geblokkeerde HTLC van 4 te herwin.
- 4 het nou die geheim van die HTLC om die geblokkeerde HTLC van 2 te herwin - 2 het nou die geheim van die HTLC om die geblokkeerde HTLC van 1 te herwin - 1 het nou die geheim van die HTLC om Alice se geblokkeerde HTLC te herwin

Alice het nie die mislukking van roete 1 gesien nie, sy het net een sekonde langer gewag. 'n Betalingsmislukking vind plaas wanneer daar geen moontlike roete is nie. Om die soeke na 'n roete te vergemaklik, kan Bob inligting aan Alice verskaf om haar met haar faktuur te help:

- Die bedrag
- Sy adres
- Die has van die prebeeld sodat Alice die HTLC kan skep
- Aanduidings oor Bob se kanale

Bob weet van die likiditeit van kanale 5 en 3 omdat hy direk daarmee verbind is, hy kan dit aan Alice aandui. Hy waarsku Alice dat node 3 nutteloos is, wat voorkom dat Alice moontlik haar roete maak.
'n Ander element sou die privaat kanale (dus nie op die netwerk gepubliseer nie) wees wat Bob kan hê. As Bob 'n privaat kanaal met 1 het, kan hy vir Alice sê om dit te gebruik en dit sou Alice > 1 > Bob gee.

![grafiek](assets/chapitre9/3.JPG)

Ten slotte is die roete van transaksies op die Lightning Network 'n komplekse proses wat die oorweging van verskeie faktore vereis. Terwyl die totale kapasiteit van kanale openbaar is, is die presiese verspreiding van likiditeit nie direk toeganklik nie. Dit dwing knope om die mees waarskynlike suksesvolle roetes te skat, met inagneming van kriteria soos fooie, HTLC vervaltyd, die aantal tussenliggende knope, en 'n willekeurigheidsfaktor. Wanneer daar verskeie roetes moontlik is, streef knope daarna om fooie te minimeer en die kanse op sukses te maksimeer deur kanale met voldoende likiditeit en 'n minimum aantal hupstoots te kies. As 'n transaksiepoging misluk as gevolg van ontoereikende likiditeit, word 'n ander roete probeer totdat 'n suksesvolle transaksie plaasvind.

Verder kan die ontvanger addisionele inligting verskaf, soos die adres, bedrag, prebeeld-has, en aanduidings oor hul kanale, om die soeke na 'n roete te vergemaklik. Dit kan help om kanale met voldoende likiditeit te identifiseer en onnodige transaksiepogings te vermy. Uiteindelik is die roetesisteem van die Lightning Network ontwerp om die spoed, veiligheid, en doeltreffendheid van transaksies te optimaliseer terwyl gebruikersprivaatheid behou word.

# Gereedskap van die Lightning Network
## Faktuur, LNURL, Keysend

![faktuur, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)

![omslag](assets/chapitre10/0.JPG)

'n LN faktuur (of faktuur) is lank en nie aangenaam om te lees nie, maar dit maak voorsiening vir 'n digte voorstelling van 'n betalingsversoek.

Voorbeeld:
lnbc1m1pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3

- lnbc1m = leesbare gedeelte
- 1 = skeiding van die res
- Dan die res
- Bc1 = Bech32-kodering (basis 32), dus word 32 karakters gebruik.
- 10 = 1.2.3.4.5.6.7.8.9.0- 26 = abcdefghijklmnopqrstuvwxyz
- 32 = nie "b-i-o" en nie "1"

### lnbc1m

- ln = Lightning
- Bc = bitcoin (mainnet)
- 1 = bedrag
- M = milli (10*-3 / u = mikro 10*-6 / n = nano 10*-9 / p = piko 10*-12'
  Hier beteken 1m = 1 \* 0.0001btc = 100,000 BTC
  "Betaal asseblief 100,000 SAT op die Lightning-netwerk van die Bitcoin-hoofnetwerk aan pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3"

### Tydmerk (wanneer dit geskep is)

Dit bevat 0 of meer bykomende dele:

- Hash van die prentjie
- Betalingsgeheim (uienskakeling)
- Willekeurige data
- LN openbare sleutel van die ontvanger
- Vervaltyd (verstek 1 uur)
- Roetehints
- Handtekening van die geheel

Daar is ander tipes faktuur. Die LNURL-meta-protokol maak dit moontlik om 'n direkte satoshi-bedrag te voorsien in plaas van 'n versoek te maak. Dit is baie buigsaam en maak baie verbeterings in terme van gebruikerservaring moontlik.

![cover](assets/chapitre10/2.JPG)

'n Sleutelstuur stel Alice in staat om geld aan Bob te stuur sonder om Bob se versoek te hê. Alice haal Bob se ID op, skep 'n prentjie sonder om Bob te vra, en sluit dit in haar betaling in. Bob sal dus 'n verrassingsversoek ontvang waar hy die geld kan ontgrendel omdat Alice reeds die werk gedoen het.

![cover](assets/chapitre10/3.JPG)

Ten slotte, 'n Lightning Network-faktuur, alhoewel dit op die eerste oog ingewikkeld mag lyk, kodeer effektief 'n betalingsversoek. Elke gedeelte van die faktuur bevat sleutelinligting, insluitend die bedrag wat betaal moet word, die ontvanger, die skeppingstydmerk, en moontlik ander inligting soos die hash van die prentjie, die betalingsgeheim, roetehints en vervaltyd. Protokolle soos LNURL en Sleutelstuur bied aansienlike verbeterings in terme van buigsaamheid en gebruikerservaring, wat byvoorbeeld moontlik maak om fondse te stuur sonder voorafgaande versoek van die ander party. Hierdie tegnologieë maak die betalingsproses vlotter en doeltreffender op die Lightning-netwerk.

## Bestuur van Vloeibaarheid

![bestuur van vloeibaarheid](https://youtu.be/YuPrbhEJXbg)

![instruksie](assets/chapitre11/0.JPG)


Ons bied 'n paar algemene riglyne om die ewige vraag van die bestuur van vloeibaarheid op Lightning te beantwoord.

In LN is daar 3 tipes mense:

- Kopers: hulle het uitgaande vloeibaarheid, wat die eenvoudigste is omdat hulle net kanale moet oopmaak
- Handelaars: dit is meer ingewikkeld omdat hulle inkomende vloeibaarheid van ander knooppunte en ander rolspelers nodig het. Hulle moet mense met hulle verbind hê
- Roetingsknoppies: hulle wil gebalanseer wees met likiditeit aan beide kante en 'n goeie verbinding met baie knoppies hê om soveel as moontlik gebruik te word.
So as jy inkomende likiditeit benodig, kan jy dit koop van dienste.

![instructie](assets/chapitre11/1.JPG)

Alice koop 'n kanaal met Susie vir 1 miljoen satoshis, so sy maak 'n kanaal oop met direk 1,000,000 SAT aan die inkomende kant. Sy kan dan tot 1 miljoen SAT aan betaling van klante aanvaar wat met Susie (wat goed gekoppel is) verbind is.

'n Ander oplossing sou wees om betalings te maak; jy betaal 100,000 vir X rede, jy kan nou 100,000 ontvang.

![instructie](assets/chapitre11/2.JPG)

### Loop Uit Oplossing: Atomic swap LN - BTC

Alice 2 miljoen - Susie 0

![instructie](assets/chapitre11/3.JPG)

Alice wil likiditeit na Susie stuur, so sy doen 'n Loop uit ( 'n spesiale knoppie wat 'n pro-diens bied om LN/BTC te herbalanseer).
Alice stuur 1 miljoen na Loop via Susie se knoppie, so Susie het die likiditeit en Loop stuur die on-chain balans terug na Alice se knoppie.

![instructie](assets/chapitre11/4.JPG)

So gaan die 1 miljoen na Susie, Susie stuur 1 miljoen na Loop, Loop stuur 1 miljoen na Alice. Alice het dus likiditeit na Susie geskuif teen die koste van 'n paar fooie wat aan Loop betaal word vir die diens.

Die mees ingewikkelde ding in LN is om likiditeit te behou.

![instructie](assets/chapitre11/5.JPG)

Ter opsomming, likiditeitsbestuur op die Lightning Network is 'n sleutelkwessie wat afhang van die tipe gebruiker: koper, handelaar, of roetingsknoppie. Kopers, wat uitgaande likiditeit benodig, het die eenvoudigste taak: hulle maak eenvoudig kanaal oop. Handelaars, wat inkomende likiditeit vereis, moet gekoppel wees aan ander knoppies en rolspelers. Roetingsknoppies daarenteen streef daarna om 'n balans van likiditeit aan beide kante te handhaaf. Verskeie oplossings bestaan vir die bestuur van likiditeit, soos die aankoop van kanale of betaling om ontvangskapasiteit te verhoog. Die "Loop Uit" opsie, wat 'n Atomic Swap tussen LN en BTC moontlik maak, bied 'n interessante oplossing vir die herbalansering van likiditeit. Ten spyte van hierdie strategieë bly die handhawing van likiditeit op die Lightning Network 'n komplekse uitdaging.

# Gaan verder
## Opsomming van die kursus

![gevolgtrekking](https://youtu.be/MaWpD0rbkVo)

Ons doel was om te verduidelik hoe die Lightning Network werk en hoe dit op Bitcoin staatmaak om te funksioneer.

Die Lightning Network is 'n netwerk van betalingskanale. Ons het gesien hoe 'n betalingskanaal werk tussen twee belanghebbendes, maar ons het ook ons visie uitgebrei na die hele netwerk, na die begrip van 'n netwerk van betalingskanale.

![instructie](assets/chapitre12/0.JPG)

Kanale word oopgemaak deur middel van 'n Bitcoin-transaksie en kan soveel transaksies as moontlik akkommodeer. Die toestand van die kanaal word verteenwoordig deur 'n verbintenistransaksie wat aan elke belanghebbende stuur wat hulle aan hul kant van die kanaal het. Wanneer 'n transaksie binne die kanaal plaasvind, verbind die belanghebbendes hulself tot die nuwe toestand deur die ou toestand te herroep en 'n nuwe verbintenistransaksie te bou.

![instructie](assets/chapitre12/1.JPG)

Pare beskerm hulself teen bedrog met herroepingsleutels en 'n tydsluiting. Wedersydse toestemming sluiting word verkies om die kanaal te sluit. In geval van gedwonge sluiting word die laaste verbintenistransaksie gepubliseer.

![instructie](assets/chapitre12/3.JPG)
Betalings kan kanale van ander tussenliggende knooppunte leen. Voorwaardelike betalings op die hash tydslot (HTLC) maak dit moontlik om fondse te sluit totdat die betaling volledig opgelos is. Uie-roeteverkoping word in die Lightning-netwerk gebruik. Tussenliggende knooppunte weet nie wat die finale bestemming van betalings is nie. Alice moet die betalingsroete bereken, maar het nie al die inligting oor likiditeit in tussenliggende kanale nie.
![instruksie](assets/chapitre12/4.JPG)

Daar is 'n waarskynlikheidskomponent wanneer 'n betaling via die Lightning-netwerk gestuur word.

![instruksie](assets/chapitre12/5.JPG)

Om betalings te ontvang, moet likiditeit in die kanale bestuur word, wat gedoen kan word deur ander te vra om kanale na ons te open, kanale self te open, en hulpmiddels soos Loop te gebruik of kanale op markplekke te koop/huur.


## Fanis se Onderhoud

![Fanis onderhoud](https://youtu.be/VeJ4oJIXo9k)

Hier is 'n opsomming van die onderhoud:

Die Lightning-netwerk is 'n ultravinnige betalingsoplossing op Bitcoin wat dit moontlik maak om die beperkings wat verband hou met die skaalbaarheid van die netwerk te omseil. Tog is bitcoins op Lightning nie so veilig soos dié op die Bitcoin-ketting nie, omdat desentralisasie en veiligheid prioriteit geniet bo skaalbaarheid.

'n Oormatige toename in blokgrootte is nie 'n goeie oplossing nie, omdat dit knooppunte en datakapasiteit in gevaar stel. In plaas daarvan maak die Lightning-netwerk dit moontlik om betalingskanale tussen twee Bitcoin-gebruikers te skep sonder om transaksies op die blokketting te wys, wat spasie op blokke bespaar en Bitcoin in staat stel om vandag te skaal.

Daar is egter kritiek oor die skaalbaarheid en sentralisasie van die Lightning-netwerk, met moontlike probleme wat verband hou met kanaalsluiting en hoë transaksiefooie. Om hierdie probleme op te los, word dit aanbeveel om te vermy om klein kanale te open om toekomstige probleme te voorkom, en om transaksiefooie te verhoog met Child Pay for Parent.

Oplossings wat oorweeg word vir die toekoms van die Lightning-netwerk is groepering en die skep van kanale in groepe om transaksiefooie te verminder, sowel as die verhoging van die blokgrootte op die lang termyn. Dit is egter belangrik om daarop te let dat bitcoins op Lightning nie so veilig is soos bitcoins op die Bitcoin-ketting nie.

Privaatheid op Bitcoin en Lightning is gekoppel, met uie-roeteverkoping wat 'n sekere vlak van privaatheid vir transaksies verseker. Tog is alles op Bitcoin standaard deursigtig, met heuristieke wat gebruik word om Bitcoins van adres tot adres op die Bitcoin-ketting te volg.

Die koop van Bitcoins met KYC stel die beurs in kennis van onttrekkings-transaksies, terwyl ronde bedrae en wisseladres aandui watter deel van 'n transaksie bedoel is vir 'n ander persoon en watter deel bedoel is vir eenself.

Om privaatheid te verbeter, maak gesamentlike aksies en muntjoins dit moontlik om waarskynlikheidsberekeninge te verbreek deur transaksies waarin verskeie mense saam 'n transaksie maak. Kettinganalise-maatskappye het 'n moeiliker tyd om te bepaal wat jy met jou bitcoins doen deur jou te volg.

Op Lightning is slegs twee mense bewus van die transaksie, en dit is meer vertroulik as Bitcoin. Uie-roeteverkoping beteken dat 'n tussenliggende knooppunt nie weet wie die afsender en ontvanger van die betaling is nie.

Om die Lightning-netwerk te gebruik, word dit aanbeveel om 'n opleiding op jou YouTube-kanaal te volg of direk op die Discover Bitcoin-webwerf, of om die opleiding op Umbrell te gebruik. Dit is ook moontlik om arbitêre teks tydens 'n betaling op Lightning te stuur deur 'n toegewyde veld hiervoor te gebruik, wat nuttig kan wees vir skenkings of boodskappe.
Dit is egter belangrik om daarop te let dat Lightning-roeteknooppunte in die toekoms gereguleer kan word, met sommige state wat probeer om roeteknooppunte te reguleer. Vir handelaars is dit nodig om likiditeit te bestuur om betalings op die Lightning-netwerk te aanvaar, met huidige beperkings wat oorkom kan word met toepaslike oplossings.

Laastens is die toekoms van Bitcoin belowend met 'n moontlike projeksie van een miljoen binne vyf jaar. Om die professionalisering van die bedryf en die skep van 'n alternatiewe stelsel tot die bestaande bankstelsel te verseker, is dit belangrik om by te dra tot die netwerk en om ophou om te vertrou.

## Erkenning en blyf die konynhol ontgin
Geluk! 🎉 Jy het die LN 201 opleiding - Inleiding tot die Lightning Network - voltooi!
Jy kan trots wees op jouself, want dit is nie maklik nie. Weet dat min mense so diep in die Bitcoin konynhol ingaan.

Eerstens, 'n groot dankie aan Fanis Makalakis vir die aanbied van hierdie fantastiese gratis kursus oor 'n meer etniese aspek van Lightning. Moenie huiwer om hom op Twitter te volg, op sy blog, of deur sy werk by LN Market nie.

Dan, as jy die projek wil help, moenie huiwer om ons op Patreon te borg nie. Jou skenkings sal gebruik word om inhoud vir nuwe opleidingskursusse te produseer en natuurlik sal jy die eerste wees om ingelig te word (insluitend vir Fanis se volgende een wat in die maak is!).

Die Lightning Network-avontuur gaan voort met die Umbrel-opleiding en die implementering van 'n Lightning Network-node. Teorie is verby en dit is nou tyd vir praktyk met die LN 202 opleiding!

Drukies en sien jou binnekort!

Rogzy