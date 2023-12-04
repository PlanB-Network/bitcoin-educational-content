---
name: Teoretisk introduktion til Lightning-netværket
goal: Opdagelse af Lightning-netværket fra et teknisk perspektiv
objectives:
  - Forståelse af netværkets kanalers funktion.
  - Blive fortrolig med termer som HTLC, LNURL og UTXO.
  - Assimilering af håndtering af likviditet og gebyrer i LNN.
  - Anerkendelse af Lightning-netværket som et netværk.
  - Forståelse af de teoretiske anvendelser af Lightning-netværket.
---

# En rejse til Bitcoins andet lag

Dette kursus er en teoretisk lektion om det tekniske funktion af Lightning-netværket.

Velkommen til den spændende verden af Lightning-netværket, et andet lag af Bitcoin, der er både sofistikeret og fuld af potentiale. Vi er ved at dykke ned i denne teknologis tekniske dybder uden at fokusere på specifikke tutorials eller brugsscenarier. For at få mest muligt ud af dette kursus er det vigtigt at have en solid forståelse af Bitcoin. Dette er en oplevelse, der kræver en seriøs og fokuseret tilgang. Du kan også overveje at tage LN 202-kurset samtidig, som tilbyder en mere praktisk tilgang til denne udforskning. Gør dig klar til at begive dig ud på en rejse, der kan ændre din opfattelse af Bitcoin-økosystemet.

Nyd opdagelsen!

+++

# Grundlæggende
## Forståelse af Lightning-netværket

![Forståelse af Lightning-netværket](https://youtu.be/PszWk046x-I)

Lightning-netværket er en betalingsinfrastruktur på andet lag, der er bygget på Bitcoin-netværket og muliggør hurtige og omkostningseffektive transaktioner. For at forstå, hvordan Lightning-netværket fungerer fuldt ud, er det vigtigt at forstå, hvad betalingskanaler er, og hvordan de fungerer.

En Lightning-betalingskanal er en slags "privat vej" mellem to brugere, der muliggør hurtige og gentagne Bitcoin-transaktioner. Når en kanal åbnes, får den en fast kapacitet, der defineres på forhånd af brugerne. Denne kapacitet repræsenterer det maksimale beløb af Bitcoin, der kan overføres i kanalen på et givet tidspunkt.

Betalingskanaler er tovejs, hvilket betyder, at de har to "sider". For eksempel, hvis Alice og Bob åbner en betalingskanal, kan Alice sende Bitcoin til Bob, og Bob kan sende Bitcoin til Alice. Transaktioner inde i kanalen ændrer ikke kanalens samlede kapacitet, men de ændrer fordelingen af denne kapacitet mellem Alice og Bob.

![forklaring](assets/chapitre1/0.JPG)

For at en transaktion kan være mulig i en Lightning-betalingskanal, skal brugeren, der sender midlerne, have nok Bitcoin på deres side af kanalen. Hvis Alice ønsker at sende 1 Bitcoin til Bob gennem deres kanal, skal hun have mindst 1 Bitcoin på hendes side af kanalen.
Begrænsninger og funktion af betalingskanaler på Lightning.
Selvom kapaciteten af en Lightning-betalingskanal er fast, begrænser dette ikke det samlede antal transaktioner eller det samlede volumen af Bitcoin, der kan overføres gennem kanalen. For eksempel, hvis Alice og Bob har en kanal med en kapacitet på 1 Bitcoin, kan de udføre hundredvis af transaktioner på 0,01 Bitcoin eller tusindvis af transaktioner på 0,001 Bitcoin, så længe kanalens samlede kapacitet ikke overskrides på noget tidspunkt.

Trods disse begrænsninger er Lightning-betalingskanaler en effektiv måde at udføre hurtige og billige Bitcoin-transaktioner på. De giver brugerne mulighed for at sende og modtage Bitcoin uden at skulle betale høje transaktionsgebyrer eller vente på lange bekræftelsesperioder på Bitcoin-netværket.

Samlet set tilbyder Lightning-betalingskanaler en kraftfuld løsning for dem, der ønsker at udføre hurtige og billige Bitcoin-transaktioner. Det er dog vigtigt at forstå deres funktion og begrænsninger for at kunne udnytte dem fuldt ud.

![forklaring](assets/chapitre1/1.JPG)

Eksempel:

- Alice har 100.000 SAT
- Bob har 30.000 SAT
Dette er den nuværende tilstand af kanalen. Under en transaktion beslutter Alice at sende 40.000 SAT til Bob. Hun kan gøre det, fordi 40.000 < 100.000.
Den nye tilstand af kanalen er derfor:

- Alice 60.000 SAT
- Bob 70.000 SAT

```
Kanalens oprindelige tilstand:
Alice (100.000 SAT) ============== Bob (30.000 SAT)

Efter Alices overførsel til Bob på 40.000 SAT:
Alice (60.000 SAT) ============== Bob (70.000 SAT)

```
![forklaring](assets/chapitre1/2.JPG)

Nu vil Bob sende 80.000 SAT til Alice. Da han ikke har likviditet, kan han ikke gøre det. Kanalens maksimale kapacitet er 130.000 SAT, med en mulig udgift på op til 60.000 SAT for Alice og 70.000 SAT for Bob.

![forklaring](assets/chapitre1/3.JPG)

## Bitcoin, adresser, UTXO og transaktioner

![bitcoin, adresser, utxo og transaktioner](https://youtu.be/cadCJ2V7zTg)

I dette andet kapitel tager vi os tid til at studere, hvordan Bitcoin-transaktioner faktisk fungerer, hvilket vil være meget nyttigt for at forstå Lightning. Vi diskuterer også kort begrebet multi-signaturadresser, som er afgørende for at forstå det næste kapitel om åbning af kanaler på Lightning-netværket.

- Privat nøgle > Offentlig nøgle > Adresse: Under en transaktion sender Alice penge til Bob. Sidstnævnte giver en adresse, der er givet af hans offentlige nøgle. Alice, der selv modtog pengene på en adresse via sin offentlige nøgle, bruger nu sin private nøgle til at underskrive transaktionen og dermed låse bitcoins op fra adressen.
- I en Bitcoin-transaktion skal alle bitcoins flytte sig. Kaldet UTXO (Unspend Transaction Output), vil bitcoin-bidderne alle forlade kun for at vende tilbage til ejeren bagefter.
  Alice har 0,002 BTC, Bob har 0 BTC. Alice beslutter at sende 0,0015 BTC til Bob. Hun vil underskrive en transaktion på 0,002 BTC, hvoraf 0,0015 vil gå til Bob, og 0,0005 vil vende tilbage til hendes tegnebog.

![forklaring](assets/chapitre2/0.JPG)

Her har vi fra en UTXO (Alice har 0,0002 BTC på en adresse) skabt 2 UTXO'er (Bob har 0,0015 og Alice har en ny UTXO (uafhængig af den foregående) på 0,0005 BTC).

```
Alice (0,002 BTC)
  |
  V
Bitcoin-transaktion (0,002 BTC)
  |
  |----> Bob (0,0015 BTC)
  |
  V
Alice (ny UTXO: 0,0005 BTC)
```

I Lightning-netværket bruges multi-signaturer. Derfor kræves der 2 underskrifter for at låse midlerne op, dvs. to private nøgler til at flytte pengene. Dette kan være Alice og Bob, der sammen skal blive enige om at låse pengene op (UTXO'en). I LN specifikt er de 2/2-transaktioner, så begge underskrifter er absolut nødvendige, i modsætning til 2/3 eller 3/5 multi-signaturer, hvor kun en kombination af det fulde antal nøgler kræves.

![forklaring](assets/chapitre2/1.JPG)

# Åbning og lukning af kanaler
## Kanalåbning

![åbn en kanal](https://youtu.be/B2caBC0Rxko)

Nu vil vi se nærmere på kanalåbning og hvordan det gøres gennem en Bitcoin-transaktion.
Lightning-netværket har forskellige niveauer af kommunikation:
- P2P-kommunikation (Lightning-netværksprotokol)
- Betalingskanal (Lightning-netværksprotokol)
- Bitcoin-transaktion (Bitcoin-protokol)

![forklaring](assets/chapitre3/0.JPG)

For at åbne en kanal kommunikerer de to parter gennem en kommunikationskanal:

- Alice: "Hej, jeg vil gerne åbne en kanal!"
- Bob: "Okay, her er min offentlige adresse."

![forklaring](assets/chapitre3/1.JPG)

Alice har nu 2 offentlige adresser til at oprette en 2/2 multi-sig adresse. Hun kan nu foretage en bitcoin-transaktion for at sende penge til den.

Lad os sige, at Alice har en UTXO på 0,002 BTC, og hun ønsker at åbne en kanal med Bob på 0,0013 BTC. Hun vil oprette en transaktion med 2 UTXO'er som output:

- En UTXO på 0,0013 til den 2/2 multi-sig adresse
- En UTXO på 0,0007 til en af hendes ændringsadresser (returnering af UTXO'er).

Denne transaktion er endnu ikke offentlig, fordi hvis den er på dette stadie, stoler hun på, at Bob kan låse pengene op fra multi-sig'en.

Men hvordan går man så videre?

Alice vil oprette en anden transaktion kaldet en "udtrækstransaktion" før offentliggørelsen af indbetalingen af midlerne i multi-sig'en.

![forklaring](assets/chapitre3/2.JPG)

Udtrækstransaktionen vil bruge midlerne fra multi-sig-adressen til en af hendes egne adresser (dette gøres før alt bliver offentliggjort).
Når begge transaktioner er oprettet, fortæller Alice Bob, at det er gjort, og beder ham om en underskrift med hans offentlige nøgle, idet hun forklarer, at på denne måde kan hun gendanne sine midler, hvis noget går galt. Bob er enig, fordi han ikke er uærlig.

Alice kan nu gendanne midlerne alene, da hun allerede har Bobs underskrift. Hun offentliggør transaktionerne. Kanalen er nu åben med 0,0013 BTC (130.000 SAT) på Alice's side.

![forklaring](assets/chapitre3/3.JPG)

## Lightning-transaktion og forpligtelsestransaktion

![Lightning-transaktion og forpligtelsestransaktion](https://youtu.be/aPqI34tpypM)

![cover](assets/chapitre4/1.JPG)

Lad os nu analysere, hvad der virkelig sker bag kulisserne, når der overføres midler fra den ene side til den anden i en kanal på Lightning-netværket, med begrebet forpligtelsestransaktion. Den on-chain udtræknings-/lukningstransaktion repræsenterer kanalens tilstand og garanterer, hvem der ejer midlerne efter hver overførsel. Så efter en Lightning-netværksoverførsel er der en opdatering af denne transaktion/kontrakt, der ikke er udført mellem de to parter, Alice og Bob, der opretter den samme transaktion med den aktuelle kanaltilstand i tilfælde af lukning:

- Alice åbner en kanal med Bob med 130.000 SAT på hendes side. Udtrækstransaktionen, som begge accepterer i tilfælde af lukning, angiver, at 130.000 SAT vil gå til Alice ved lukning, og Bob er enig, fordi det er fair.

![cover](assets/chapitre4/2.JPG)

- Alice sender 30.000 SAT til Bob. Der er nu en ny udtrækstransaktion, der angiver, at i tilfælde af lukning vil Alice modtage 100.000 SAT, og Bob vil modtage 30.000 SAT. Begge er enige, fordi det er fair.

![cover](assets/chapitre4/3.JPG)

- Alice sender 10.000 SAT til Bob, og der oprettes en ny udtrækstransaktion, der angiver, at Alice vil modtage 90.000 SAT, og Bob vil modtage 40.000 SAT i tilfælde af lukning. Begge er enige, fordi det er fair.
![cover](assets/chapitre4/4.JPG)

```
Starttilstand for kanalen:
Alice (130.000 SAT) =============== Bob (0 SAT)

Efter den første overførsel:
Alice (100.000 SAT) =============== Bob (30.000 SAT)

Efter den anden overførsel:
Alice (90.000 SAT) =============== Bob (40.000 SAT)

```

Pengene flytter sig aldrig, men den endelige saldo opdateres via en underskrevet, men ikke offentliggjort on-chain transaktion. Udbetalingstransaktionen er derfor en forpligtelsestransaktion. Satoshi-overførslerne er en anden, mere nylig forpligtelsestransaktion, der opdaterer saldoen.

## Forpligtelsestransaktioner

![transaktioner del 2](https://youtu.be/RRvoVTLRJ84)

Hvis forpligtelsestransaktioner dikterer en kanaltilstand med likviditet på tidspunkt X, kan vi snyde ved at offentliggøre en gammel tilstand? Svaret er ja, fordi vi allerede har forhåndsgodkendelsen fra begge deltagere i den ikke-offentliggjorte transaktion.

![instruktion](assets/Chapitre5/0.JPG)

For at løse dette problem vil vi tilføje kompleksitet:

- Timelock = midler låst indtil blok N
- Tilbagekaldelsesnøgle = Alice's hemmelighed og Bob's hemmelighed

Disse to elementer tilføjes forpligtelsestransaktionen. Som et resultat skal Alice vente på afslutningen af Timelock, og enhver, der har tilbagekaldelsesnøglen, kan flytte midlerne uden at vente på afslutningen af Timelock. Hvis Alice forsøger at snyde, bruger Bob tilbagekaldelsesnøglen til at stjæle og straffe Alice.

![instruktion](assets/Chapitre5/1.JPG)

Nu (og i virkeligheden) er forpligtelsestransaktionen ikke den samme for Alice og Bob, de er symmetriske, men hver med forskellige begrænsninger, de giver hinanden deres hemmelighed for at oprette tilbagekaldelsesnøglen for den tidligere forpligtelsestransaktion. Så ved oprettelsen opretter Alice kanalen med Bob, 130.000 SAT på hendes side, hun har en Timelock, der forhindrer hende i at få sine penge tilbage med det samme, hun skal vente lidt. Tilbagekaldelsesnøglen kan låse pengene op, men kun Alice har den (Alice's forpligtelsestransaktion). Når der er en overførsel, vil Alice give sin gamle hemmelighed til Bob, og derfor vil sidstnævnte kunne tømme kanalen til den tidligere tilstand, hvis Alice forsøger at snyde (Alice bliver derfor straffet).

![instruktion](assets/Chapitre5/2.JPG)

På samme måde vil Bob give sin hemmelighed til Alice. Så hvis han forsøger at snyde, kan Alice straffe ham. Operationen gentages for hver ny forpligtelsestransaktion. En ny hemmelighed besluttes, og en ny tilbagekaldelsesnøgle. Så for hver ny transaktion skal den tidligere forpligtelsestransaktion ødelægges ved at give tilbagekaldelseshemmeligheden. Således hvis Alice eller Bob forsøger at snyde, kan den anden handle før (takket være Timelock) og dermed undgå snyd. Under transaktion #3 gives hemmeligheden for transaktion #2 derfor for at tillade Alice og Bob at forsvare sig mod Alice eller Bob.

![instruktion](assets/Chapitre5/3.JPG)

Personen, der opretter transaktionen med Timelock (den, der sender pengene), kan kun bruge tilbagekaldelsesnøglen efter Timelock. Imidlertid kan personen, der modtager pengene, bruge den før Timelock i tilfælde af snyd fra den ene side til den anden i en kanal på Lightning-netværket. Især detaljerer vi mekanismerne, der tillader os at beskytte os mod mulig snyd fra ens peer inden for kanalen.

## Lukning af kanal

![luk en kanal](https://youtu.be/FVmQvNpVW8Y)
Vi er interesserede i kanallukning gennem en Bitcoin-transaktion, der kan tage forskellige former afhængigt af situationen. Der er 3 typer af kanallukning:
- Den gode: samarbejdende lukning
- Den brutale: tvungen lukning (ikke-samarbejdende)
- Snyd: lukning ved en snyder

![instruction](assets/chapitre6/1.JPG)
![instruction](assets/chapitre6/0.JPG)


### Den gode

De to parter kommunikerer og bliver enige om at lukke kanalen. De stopper alle transaktioner og bekræfter en endelig tilstand for kanalen. De bliver enige om netværksgebyrer (personen, der åbnede kanalen, betaler lukningsgebyrerne). Nu opretter de lukningstransaktionen. Der er en lukningstransaktion, der er anderledes end forpligtelsestransaktioner, fordi der ikke er nogen Timelock og tilbagekaldelsesnøgle. Transaktionen bliver derefter offentliggjort, og Alice og Bob modtager deres respektive saldoer. Denne type lukning er hurtig (fordi der ikke er nogen Timelock) og generelt billig.

![instruction](assets/chapitre6/3.JPG)


### Den brutale

Alice ønsker at lukke kanalen, men Bob reagerer ikke, fordi han er offline (internet- eller strømafbrydelse). Alice vil derefter offentliggøre den seneste forpligtelsestransaktion (den sidste). Transaktionen bliver offentliggjort, og Timelock aktiveres. Derefter blev gebyrerne besluttet, da denne transaktion blev oprettet X tid i fortiden! MemPool er netværket, der har ændret sig siden da, så protokollen bruger standardmæssigt gebyrer, der er 5 gange højere end de nuværende, da transaktionen blev oprettet. Oprettelsesgebyr på 10 SAT, så transaktionen betragtes som 50 SAT. Ved tvungen lukning er netværket:

- 1 SAT = overbetalt med 50\*
- 100 SAT = underbetalt med 2\*

Dette gør tvungen lukning længere (Timelock) og især mere risikabelt med hensyn til gebyrer og mulig validering af minearbejdere.

![instruction](assets/chapitre6/4.JPG)

### Snyd

Alice forsøger at snyde ved at offentliggøre en gammel forpligtelsestransaktion. Men Bob overvåger MemPool og holder øje med transaktioner, der forsøger at offentliggøre gamle transaktioner. Hvis han finder nogen, bruger han tilbagekaldelsesnøglen til at straffe Alice og tage alle SAT fra kanalen.

![instruction](assets/chapitre6/5.JPG)

Afslutningsvis er kanallukning i Lightning-netværket et afgørende skridt, der kan tage forskellige former. I en samarbejdende lukning kommunikerer begge parter og bliver enige om en endelig tilstand for kanalen. Dette er den hurtigste og mindst dyre mulighed. På den anden side sker en tvungen lukning, når den ene part ikke reagerer. Dette er en dyrere og længerevarende situation på grund af uforudsigelige transaktionsgebyrer og aktivering af Timelock. Hvis en deltager forsøger at snyde ved at offentliggøre en gammel forpligtelsestransaktion, kan snyderen straffes ved at miste alle SAT fra kanalen. Det er derfor afgørende at forstå disse mekanismer for effektiv og retfærdig brug af Lightning-netværket.

# Et likviditetsnetværk
## Lightning-netværket

![Lightning-netværket](https://youtu.be/RAZAa3v41DM)

I dette syvende kapitel studerer vi, hvordan Lightning fungerer som et netværk af kanaler, og hvordan betalinger rutes fra deres kilde til deres destination.

![cover](assets/Chapitre7/0.JPG)
![cover](assets/Chapitre7/1.JPG)

Lightning er et netværk af betalingskanaler. Tusinder af deltagere med deres egne likviditetskanaler er forbundet med hinanden og bruger sig selv til at udføre transaktioner mellem ikke-forbundne deltagere. Likviditeten i disse kanaler kan ikke overføres til andre likviditetskanaler.
Alice -> Eden -> Bob`. Satoshis er ikke flyttet fra `Alice -> Bob`, men fra `Alice -> Eden` og fra `Eden -> Bob`.
Så hver person og kanal har forskellig likviditet. For at foretage betalinger skal du finde en rute i netværket med tilstrækkelig likviditet. Hvis der ikke er nok, vil betalingen ikke gå igennem.

Overvej følgende netværk:

```
Netværkets oprindelige tilstand:
Alice (130 SAT) ==== (0 SAT) Susie (90 SAT) ==== (200 SAT) Eden (150 SAT) ==== (100 SAT) Bob
```
![cover](assets/Chapitre7/2.JPG)

Hvis Alice skal overføre 40 SAT til Bob, vil likviditeten blive omfordelt langs ruten mellem de to parter.

```
Efter at Alice har overført 40 SAT til Bob:
Alice (90 SAT) ==== (40 SAT) Susie (50 SAT) ==== (240 SAT) Eden (110 SAT) ==== (140 SAT) Bob
```

![cover](assets/Chapitre7/4.JPG)

Men i den oprindelige tilstand kan Bob ikke sende 40 SAT til Alice, fordi Susie ikke har nogen likviditet med Alice til at sende 40 SAT, så betalingen er ikke mulig via denne rute. Vi har derfor brug for en anden rute, hvor transaktionen er mulig.

I det første eksempel er det klart, at Susie og Eden hverken har mistet noget eller fået noget. Lightning Network-noder opkræver et gebyr for at acceptere at blive brugt til at rute transaktionen!

Der er forskellige gebyrer afhængigt af, hvor likviditeten er placeret.

Alice - Bob

- Alices gebyr = Alice -> Bob
- Bobs gebyr = Bob -> Alice

![cover](assets/Chapitre7/5.JPG)

Der er to typer gebyrer:

- et fast gebyr uanset beløbet: 1 SAT (standard, men kan ændres)
- et variabelt gebyr (0,01% som standard)

Gebyreksempel:

- Alice - Susie; 1/1 (1 fast gebyr og 1 variabelt gebyr)
- Susie - Eden; 0/200
- Eden - Bob; 1/1

Derfor:

- Gebyr 1: (betalt af Alice til sig selv) 1 + (40.000 * 0,000001)
- Gebyr 2: 0 + 40.000 * 0,0002 = 8 SAT
- Gebyr 3: 1 + 40.000 * 0,000001 = 0,4 SAT

![cover](assets/Chapitre7/6.JPG)

Forsendelse:

1. Forsendelse af 40.009,04 Alice -> Susie; Alice betaler sine egne udgifter, så det tæller ikke med
2. Susie gør Eden den tjeneste at sende 40.001,04; hun tager dette gebyr på 8 SAT
3. Eden gør tjenesten at sende 40.000 til Bob, han tager sit gebyr på 1,04 SAT.

Alice betalte et gebyr på 9,04 SAT, og Bob modtog 40.000 SAT.

![cover](assets/Chapitre7/7.JPG)

I Lightning Network er det Alice's node, der beslutter ruten, før betalingen sendes. Derfor søges der efter den bedste rute, og kun Alice kender ruten og prisen. Betalingen sendes, men Susie har ingen oplysninger.

![cover](assets/Chapitre7/9.JPG)
For Susie eller Eden: De ved ikke, hvem den endelige modtager er, eller hvem der sender betalingen. Dette er løg-ruting. Noden skal holde styr på netværket for at finde sin rute, men ingen af mellemmændene har nogen information.

## HTLC - Hashed Time Locked Contract

![HTLC](https://youtu.be/-JC4mkq7H48)

I et traditionelt rutesystem, hvordan kan vi sikre, at Eden ikke snyder og overholder deres del af kontrakten?

HTLC er en betalingskontrakt, der kun kan låses op med en hemmelighed. Hvis den ikke afsløres, udløber kontrakten. Det er derfor en betinget betaling. Hvordan bruges de?

![instruktion](assets/chapitre8/0.JPG)

Overvej følgende situation:
`Alice (100.000 SAT) ==== (30.000 SAT) Susie (250.000 SAT) ==== (0 SAT) Bob`

- Bob genererer en hemmelighed S (preimage) og beregner hashen r = hash(s)
- Bob sender en faktura til Alice med "r" inkluderet
- Alice sender en HTLC på 40.000 SAT til Susie med betingelsen om at afsløre "s'", sådan at hash(s') = r
- Susie sender en lignende HTLC til Bob
- Bob låser Susies HTLC op ved at vise hende "s"
- Susie låser Alice's HTLC op ved at vise hende "S"

Hvis Bob er offline og aldrig henter den hemmelighed, der giver ham legitimitet til at modtage pengene, udløber HTLC'en efter et vist antal blokke.

![instruktion](assets/chapitre8/1.JPG)

HTLC'erne udløber i omvendt rækkefølge: Susie-Bob udløb, derefter Alice-Susie udløb. På denne måde ændrer det ikke noget, hvis Bob vender tilbage. Hvis Alice derimod annullerer, mens Bob vender tilbage, vil det være et rod, og folk kan have arbejdet for ingenting.

Så hvad sker der i tilfælde af lukning? Faktisk er vores forpligtelsestransaktioner endnu mere komplekse. Vi skal repræsentere den mellemliggende balance, hvis kanalen lukkes.

Derfor er der en HTLC-ud på 40.000 satoshis (med de tidligere sete begrænsninger) i forpligtelsestransaktionen via output nr. 3.

![instruktion](assets/chapitre8/2.JPG)

Alice har i forpligtelsestransaktionen:

- Output nr. 1: 60.000 SAT til Alice via en tidslås og tilbagekaldelsesnøgle (hvad der er tilbage for hende)
- Output nr. 2: 30.000, der allerede tilhører Susie
- Output nr. 3: 40.000 i HTLC

Alice's forpligtelsestransaktion er med en HTLC-ud, fordi hun sender en HTLC-ind til modtageren, Susie.

![instruktion](assets/chapitre8/3.JPG)

Derfor kan Susie hente HTCL-pengene med billedet "s", hvis vi offentliggør denne forpligtelsestransaktion. Hvis hun ikke har pre-billedet, henter Alice pengene, når HTCL udløber. Tænk på outputs (UTXO) som forskellige betalinger med forskellige betingelser.
Når betalingen er foretaget (udløb eller udførelse), ændres kanaltilstanden, og transaktionen med HTCL eksisterer ikke længere. Vi vender tilbage til noget klassisk.
I tilfælde af samarbejdslukning: stopper vi betalinger og venter derfor på udførelsen af overførsler/HTCL, transaktionen er let, så den er mindre dyr, fordi der er højst 1 eller 2 outputs.
Hvis tvungen lukning: offentliggør vi med alle HTLC'er i gang, så det bliver meget tungt og meget dyrt. Og det er et rod.
I oversættelse, bruger Lightning Network-routing-systemet Hash Time-Locked Contracts (HTLC) til at sikre sikker og verificerbar betaling. HTLC'er tillader betingede betalinger, hvor pengene kun kan låses op med en hemmelighed, hvilket sikrer, at deltagerne opfylder deres forpligtelser. I det præsenterede eksempel ønsker Alice at sende SAT til Bob gennem Susie. Bob genererer en hemmelighed, opretter en hash af den og transmitterer den til Alice. Alice og Susie opretter en HTLC baseret på denne hash. Når Bob låser Susies HTLC op ved at vise hende hemmeligheden, kan Susie derefter låse Alices HTLC op.

Hvis Bob ikke afslører hemmeligheden inden for en vis tidsperiode, udløber HTLC'en. Udløbet sker i omvendt rækkefølge, hvilket sikrer, at der ikke er uønskede konsekvenser, hvis Bob kommer online igen.

Ved lukning af kanalen, hvis det er en samarbejdsmæssig lukning, afbrydes betalingerne, og HTLC'er afvikles, hvilket generelt er mindre omkostningsfuldt. Hvis lukningen er tvungen, offentliggøres alle igangværende HTLC-transaktioner, hvilket kan blive meget dyrt og rodet.

I alt tilføjer HTLC-mekanismen et ekstra lag af sikkerhed til Lightning Network, hvilket sikrer, at betalinger udføres korrekt, og at brugerne opfylder deres forpligtelser.

## Find vej

![find vej](https://youtu.be/wnUGJjOxd9Q)

Den eneste offentlige data er den samlede kanalkapacitet (Alice + Bob), men vi ved ikke, hvor likviditeten er placeret. For at få mere information lytter vores node til LN-kommunikationskanalen for meddelelser om nye kanaler og opdateringer af kanalgebyrer. Din node kigger også på blockchain for kanallukninger.

Da vi ikke har alle oplysninger, skal vi søge efter en graf/rute med de oplysninger, vi har (maksimal kanalkapacitet og ikke hvor likviditeten er placeret).

Kriterier:

- Succes sandsynlighed - Gebyrer
- HTLC udløbstid
- Antal mellemled
- Tilfældighed

![graf](assets/chapitre9/1.JPG)

Så hvis der er 3 mulige ruter:

- Alice > 1 > 2 > 5 > Bob
- Alice > 1 > 2 > 4 > 5 > Bob
- Alice 1 > 2 > 3 > Bob

Vi leder efter den bedste rute i teorien med de laveste gebyrer og den højeste chance for succes: maksimal likviditet og færrest mulige hop.

For eksempel, hvis 2-3 kun har en kapacitet på 130.000 SAT, er det meget usandsynligt at sende 100.000, så valg #3 har ingen chance for succes.

![graf](assets/chapitre9/2.JPG)

Nu har algoritmen foretaget sine 3 valg og vil prøve det første:

Valg 1:

- Alice sender en HTLC på 100.000 SAT til 1;
- 1 laver en HTLC på 100.000 SAT til 2;
- 2 laver en HTLC på 100.000 SAT til 5, men 5 kan ikke gøre det, så det annoncerer det.

Informationen sendes tilbage, så Alice beslutter at prøve den anden rute:

- Alice sender en HTLC på 100.000 til 1;
- 1 laver en HTLC på 100.000 til 2;
- 2 laver en HTLC på 100.000 til 4;
- 4 laver en HTLC på 100.000 til Bob. Bob har likviditeten, så det er okay.
- Bob bruger preimage (hash) af HTLC'en og bruger dermed hemmeligheden til at hente de 100.000 SAT
- 5 har nu hemmeligheden for HTLC'en for at hente den blokerede HTLC fra 4.
- 4 har nu hemmeligheden om HTLC'en for at hente den blokerede HTLC fra 2- 2 har nu hemmeligheden om HTLC'en for at hente den blokerede HTLC fra 1
- 1 har nu hemmeligheden om HTLC'en for at hente Alice's blokerede HTLC

Alice så ikke fejlen i rute 1, hun ventede bare et sekund længere. En betalingsfejl opstår, når der ikke er nogen mulig rute. For at lette søgningen efter en rute kan Bob give information til Alice for at hjælpe med hendes faktura:

- Beløbet
- Hans adresse
- Hashen af preimage, så Alice kan oprette HTLC'en
- Indikationer om Bob's kanaler

Bob kender likviditeten af kanalerne 5 og 3, fordi han er direkte forbundet til dem, han kan angive dette til Alice. Han advarer Alice om, at node 3 er ubrugelig, hvilket forhindrer Alice i potentielt at lave sin rute.
Et andet element ville være de private kanaler (derfor ikke offentliggjort på netværket), som Bob kan have. Hvis Bob har en privat kanal med 1, kan han fortælle Alice at bruge den, og det ville give Alice > 1 > Bob'.

![graf](assets/chapitre9/3.JPG)

Konklusionen er, at routing af transaktioner på Lightning-netværket er en kompleks proces, der kræver overvejelse af forskellige faktorer. Mens den samlede kapacitet af kanaler er offentlig, er den præcise fordeling af likviditet ikke direkte tilgængelig. Dette tvinger noder til at estimere de mest sandsynligt succesfulde ruter, idet der tages hensyn til kriterier som gebyrer, HTLC udløbstid, antallet af mellemliggende noder og en tilfældighedsfaktor. Når der er flere mulige ruter, søger noder at minimere gebyrer og maksimere chancerne for succes ved at vælge kanaler med tilstrækkelig likviditet og et minimum antal hop. Hvis et transaktionsforsøg mislykkes på grund af utilstrækkelig likviditet, prøves en anden rute, indtil en succesfuld transaktion er foretaget.

Desuden kan modtageren for at lette rutesøgningen give yderligere information såsom adressen, beløbet, preimage hashen og indikationer på deres kanaler. Dette kan hjælpe med at identificere kanaler med tilstrækkelig likviditet og undgå unødvendige transaktionsforsøg. I sidste ende er Lightning-netværkets routing-system designet til at optimere hastigheden, sikkerheden og effektiviteten af transaktioner samtidig med at bevare brugerens privatliv.

# Værktøjer i Lightning-netværket
## Faktura, LNURL, Keysend

![faktura, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)

![cover](assets/chapitre10/0.JPG)

En LN-faktura (eller faktura) er lang og ikke behagelig at læse, men den tillader en tæt repræsentation af en betalingsanmodning.

Eksempel:
lnbc1m1pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3

- lnbc1m = læsbar del
- 1 = adskillelse fra resten
- Derefter resten
- Bc1 = Bech32-kodning (base 32), så der bruges 32 tegn.
- 10 = 1.2.3.4.5.6.7.8.9.0- 26 = abcdefghijklmnopqrstuvwxyz
- 32 = ikke "b-i-o" og ikke "1"

### lnbc1m

- ln = Lightning
- Bc = bitcoin (mainnet)
- 1 = beløb
- M = milli (10*-3 / u = mikro 10*-6 / n = nano 10*-9 / p = pico 10*-12'
  Her betyder 1m = 1 \* 0.0001btc = 100.000 BTC
  "Venligst betal 100.000 SAT på Lightning-netværket på Bitcoin mainnet til pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3"

### Tidsstempel (når det blev oprettet)

Den indeholder 0 eller flere yderligere dele:

- Hash af preimage
- Betalingshemmelighed (onion routing)
- Vilkårlige data
- LN offentlig nøgle for modtageren
- Udløbstid (standard 1 time)
- Routing hints
- Signatur på det hele

Der er andre typer fakturaer. LNURL-meta-protokollen tillader at angive et direkte satoshi-beløb i stedet for at foretage en anmodning. Dette er meget fleksibelt og tillader mange forbedringer med hensyn til brugeroplevelse.

![cover](assets/chapitre10/2.JPG)

En Keysend giver Alice mulighed for at sende penge til Bob uden at have Bob's anmodning. Alice henter Bob's ID, opretter en preimage uden at spørge Bob og inkluderer den i hendes betaling. Så Bob vil modtage en overraskelsesanmodning, hvor han kan låse op for pengene, fordi Alice allerede har gjort arbejdet.

![cover](assets/chapitre10/3.JPG)

Konklusionen er, at en Lightning Network-faktura, selvom den ved første øjekast er kompleks, effektivt koder en betalingsanmodning. Hver sektion af fakturaen indeholder nøgleinformation, herunder det beløb, der skal betales, modtageren, oprettelsestidspunktet og potentielt andre oplysninger såsom hash af preimage, betalingshemmelighed, routing hints og udløbstid. Protokoller som LNURL og Keysend tilbyder betydelige forbedringer med hensyn til fleksibilitet og brugeroplevelse, hvilket f.eks. gør det muligt at sende midler uden forudgående anmodning fra den anden part. Disse teknologier gør betalingsprocessen glattere og mere effektiv på Lightning-netværket.

## Håndtering af likviditet

![håndtering af likviditet](https://youtu.be/YuPrbhEJXbg)

![instruktion](assets/chapitre11/0.JPG)


Vi giver nogle generelle retningslinjer for at besvare det evige spørgsmål om håndtering af likviditet på Lightning.

I LN er der 3 typer mennesker:

- Købere: de har udgående likviditet, hvilket er det enkleste, fordi de bare skal åbne kanaler
- Købmænd: det er mere kompliceret, fordi de har brug for indgående likviditet fra andre knudepunkter og andre aktører. De skal have folk forbundet til sig.
- Routing-noder: De ønsker at være afbalanceret med likviditet på begge sider og have en god forbindelse til mange noder for at blive brugt så meget som muligt.
Så hvis du har brug for indgående likviditet, kan du købe det fra tjenester.

![instruktion](assets/chapitre11/1.JPG)

Alice køber en kanal med Susie for 1 million satoshis, så hun åbner en kanal med direkte 1.000.000 SAT på indgående side. Hun kan derefter acceptere op til 1 million SAT som betaling fra kunder, der er forbundet med Susie (som er godt forbundet).

En anden løsning ville være at foretage betalinger; du betaler 100.000 af X årsag, du kan nu modtage 100.000.

![instruktion](assets/chapitre11/2.JPG)

### Loop Out-løsning: Atomic swap LN - BTC

Alice 2 millioner - Susie 0

![instruktion](assets/chapitre11/3.JPG)

Alice ønsker at sende likviditet til Susie, så hun laver en Loop out (en speciel node, der tilbyder en pro-service til at afbalancere LN/BTC).
Alice sender 1 million til Loop via Susies node, så Susie har likviditeten, og Loop sender den on-chain balance tilbage til Alice's node.

![instruktion](assets/chapitre11/4.JPG)

Så de 1 million går til Susie, Susie sender 1 million til Loop, Loop sender 1 million til Alice. Alice har derfor flyttet likviditet til Susie til en vis pris i form af gebyrer betalt til Loop for servicen.

Det mest komplicerede ved LN er at opretholde likviditet.

![instruktion](assets/chapitre11/5.JPG)

Konklusionen er, at likviditetsstyring på Lightning Network er et centralt problem, der afhænger af brugertypen: køber, forhandler eller routing-node. Købere, der har brug for udgående likviditet, har den enkleste opgave: de åbner bare kanaler. Forhandlere, der har brug for indgående likviditet, skal være forbundet til andre noder og aktører. Routing-noder derimod søger at opretholde en balance af likviditet på begge sider. Der findes flere løsninger til likviditetsstyring, såsom køb af kanaler eller betaling for at øge modtagelseskapaciteten. "Loop Out" -muligheden, der tillader en Atomic Swap mellem LN og BTC, tilbyder en interessant løsning til afbalancering af likviditet. På trods af disse strategier forbliver opretholdelse af likviditet på Lightning Network en kompleks udfordring.

# Gå videre
## Resumé af kurset

![konklusion](https://youtu.be/MaWpD0rbkVo)

Vores mål var at forklare, hvordan Lightning Network fungerer, og hvordan det er afhængigt af Bitcoin for at fungere.

Lightning Network er et netværk af betalingskanaler. Vi har set, hvordan en betalingskanal fungerer mellem to interessenter, men vi har også udvidet vores vision til hele netværket, til begrebet et netværk af betalingskanaler.

![instruktion](assets/chapitre12/0.JPG)

Kanaler åbnes via en Bitcoin-transaktion og kan rumme så mange transaktioner som muligt. Kanalens tilstand repræsenteres af en forpligtelsestransaktion, der sender til hver interessent, hvad de har på deres side af kanalen. Når der forekommer en transaktion inden for kanalen, forpligter interessenterne sig til den nye tilstand ved at tilbagekalde den gamle tilstand og opbygge en ny forpligtelsestransaktion.

![instruktion](assets/chapitre12/1.JPG)

Par beskytter sig mod snyd med tilbagekaldelsesnøgler og en tidslås. Gensidig samtykke til lukning foretrækkes for at lukke kanalen. I tilfælde af tvungen lukning offentliggøres den sidste forpligtelsestransaktion.

![instruktion](assets/chapitre12/3.JPG)
Betalinger kan låne kanaler fra andre mellemliggende knudepunkter. Betingede betalinger på hash time lock (HTLC) tillader, at midler låses, indtil betalingen er fuldt afsluttet. Onion routing bruges i Lightning-netværket. Mellemliggende knudepunkter kender ikke den endelige destination for betalinger. Alice skal beregne betalingsruten, men har ikke al information om likviditet i mellemliggende kanaler.
![instruction](assets/chapitre12/4.JPG)

Der er en sandsynlighedskomponent, når en betaling sendes via Lightning-netværket.

![instruction](assets/chapitre12/5.JPG)

For at modtage betalinger skal likviditeten håndteres i kanalerne, hvilket kan gøres ved at bede andre om at åbne kanaler til os, åbne kanaler selv og bruge værktøjer som Loop eller købe/leje kanaler på markedspladser.


## Fanis' Interview

![Fanis interview](https://youtu.be/VeJ4oJIXo9k)

Her er en sammenfatning af interviewet:

Lightning-netværket er en ultrahurtig betalingsløsning på Bitcoin, der tillader at omgå begrænsningerne i forhold til netværkets skalerbarhed. Dog er bitcoins på Lightning ikke lige så sikre som dem på Bitcoin-kæden, fordi decentralisering og sikkerhed prioriteres over skalerbarhed.

En overdreven stigning i blokstørrelsen er ikke en god løsning, da det kompromitterer knudepunkter og datakapacitet. I stedet tillader Lightning-netværket at oprette betalingskanaler mellem to Bitcoin-brugere uden at vise transaktioner på blockchainen, hvilket sparer plads på blokke og tillader Bitcoin at skalere i dag.

Der er dog kritik af skalerbarheden og centraliseringen af Lightning-netværket, med potentielle problemer i forbindelse med lukning af kanaler og høje transaktionsgebyrer. For at løse disse problemer anbefales det at undgå at åbne små kanaler for at undgå fremtidige problemer og at øge transaktionsgebyrerne med Child Pay for Parent.

Løsninger, der overvejes for fremtiden for Lightning-netværket, er batchning og oprettelse af kanaler i grupper for at reducere transaktionsgebyrer samt at øge blokstørrelsen på lang sigt. Det er dog vigtigt at bemærke, at bitcoins på Lightning ikke er lige så sikre som bitcoins på Bitcoin-kæden.

Privatliv på Bitcoin og Lightning er forbundet, hvor onion routing sikrer en vis grad af privatliv for transaktioner. Dog er alt på Bitcoin som standard gennemsigtigt, og heuristikker bruges til at spore bitcoins fra adresse til adresse på Bitcoin-kæden.

Køb af bitcoins med KYC gør det muligt for børsen at kende tilbagetrækningstransaktioner, mens runde beløb og ændringsadresser gør det muligt at vide, hvilken del af en transaktion der er beregnet til en anden person, og hvilken del der er beregnet til en selv.

For at forbedre privatlivet tillader fælles handlinger og coinjoins at bryde sandsynlighedsberegninger ved at lave transaktioner, hvor flere personer foretager en transaktion sammen. Kædeanalysevirksomheder har sværere ved at bestemme, hvad du laver med dine bitcoins ved at følge med.

På Lightning er kun to personer klar over transaktionen, og det er mere fortroligt end Bitcoin. Onion routing betyder, at et mellemliggende knudepunkt ikke kender afsenderen og modtageren af betalingen.

For at bruge Lightning-netværket anbefales det at følge en træning på din YouTube-kanal eller direkte på discover Bitcoin-webstedet eller at bruge træningen på Umbrell. Det er også muligt at sende vilkårlig tekst under en betaling på Lightning ved hjælp af et dedikeret felt til dette, hvilket kan være nyttigt til donationer eller beskeder.
Det er dog vigtigt at bemærke, at Lightning-routingknudepunkter kan blive reguleret i fremtiden, hvor nogle stater forsøger at regulere routingknudepunkter. For handlende er det nødvendigt at håndtere likviditet for at acceptere betalinger på Lightning-netværket, med aktuelle begrænsninger, der kan overvindes med passende løsninger.

Endelig er fremtiden for Bitcoin lovende med en mulig projicering af en million om fem år. For at sikre professionaliseringen af branchen og oprettelsen af et alternativt system til det eksisterende banksystem er det vigtigt at bidrage til netværket og stoppe med at have tillid.

## Anerkendelser og fortsæt med at grave i kaninhullet
Tillykke! 🎉 Du har fuldført LN 201-uddannelsen - Introduktion til Lightning-netværket!
Du kan være stolt af dig selv, for det er ikke nemt. Vid, at kun få mennesker går så dybt ned i Bitcoin-kaninhullet.

Først og fremmest en stor tak til Fanis Makalakis for at tilbyde os denne fantastiske gratis kursus om en mere etnisk aspekt af Lightning. Tøv ikke med at følge ham på Twitter, på hans blog eller gennem hans arbejde hos LN Market.

Hvis du ønsker at hjælpe projektet, så tøv ikke med at støtte os på Patreon. Dine donationer vil blive brugt til at producere indhold til nye træningskurser, og selvfølgelig vil du være den første til at blive informeret (herunder om Fanis' næste kursus, som er under udarbejdelse!).

Lightning-netværkseventyret fortsætter med Umbrel-uddannelsen og implementeringen af en Lightning-netværksnode. Teorien er slut, og det er nu tid til praksis med LN 202-uddannelsen!

Kys og vi ses snart!

Rogzy