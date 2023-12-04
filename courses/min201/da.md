---
name: Introduktion til Bitcoin Mining
goal: Forstå funktionen af minedriftsindustrien gennem en praktisk øvelse med genbrug af ASIC'er.
objectives:
  - Forstå teorien bag minedrift
  - Forstå minedriftsindustrien
  - Omdan en S9 til en varmelegeme
  - Minedin første satoshi
---

# Dine første skridt i minedrift!

I denne træning vil vi dykke ned i minedriftsindustrien for at afmystificere dette komplekse emne! Træningen er tilgængelig for alle og kræver ingen indledende investering.

Den første sektion vil være teoretisk, hvor Ajelex og jeg vil have en dybdegående diskussion om forskellige emner relateret til minedrift. Dette vil hjælpe os med at få en bedre forståelse af denne industri og de økonomiske og geopolitiske problemer, der er forbundet med den.
I den anden sektion vil vi tackle en praktisk sag. Vi vil faktisk lære, hvordan man omdanner en brugt S9-miner til et hjemmevarmesystem! Gennem skriftlige vejledninger og videoer vil vi vise og forklare alle trinene for at opnå dette hjemme :)

Gennem denne video håber vi at vise dig, at minedriftsindustrien er mere kompleks, end den ser ud til, og at studere den hjælper med at nuancere den økologiske debat, der er forbundet med den!
Hvis du har brug for hjælp til din opsætning, er der oprettet en Telegram-gruppe for studerende, og alle nødvendige komponenter kan findes på vores e-handelsplatform!

+++

# Introduktion

## Velkommen!

Velkommen til MINING 201: en introduktion til minedrift. Ajelex, Jim & Rogzy er spændte på at følge dig i dine første konkrete skridt i denne nye industri. Vi håber, du nyder kurset og deltager i eventyret med hjemmeminedrift!

### Kursusoversigt

I dette kursus vil den første sektion fokusere på teorien om minedrift med Ajelex. Vi vil have dybdegående diskussioner om forskellige emner relateret til minedrift, hvilket vil hjælpe os med at få en bedre forståelse af denne industri og de økonomiske og geopolitiske problemer, der er forbundet med den.

I den anden sektion vil vi kaste os ud i en fascinerende praktisk sag og lære, hvordan man omdanner en brugt S9-miner til et hjemmevarmesystem. Gennem skriftlige vejledninger og videoer vil alle nødvendige trin blive omhyggeligt forklaret, hvilket sikrer din succes i dette innovative projekt.

Denne læringsrejse vil vise dig, at minedriftsindustrien er mere kompleks, end den ser ud til, og tilbyder en afbalanceret perspektiv på den økologiske debat, der er forbundet med den. Kontinuerlig assistance vil være tilgængelig gennem en dedikeret Telegram-gruppe for studerende, og alle nødvendige komponenter vil være let tilgængelige på vores e-handelsplatform.

### Pensum:

Teoretisk sektion:
* Forklaring af minedrift.
* Minedriftsindustrien.
* Nuancer af minedriftsindustrien.
* Minedrift i Bitcoin-protokollen.
* Bitcoin-pris og hashrate, en korrelation? Suverænitet og regulering.
* Interview med en professionel inden for minedriftsindustrien.

Praktisk sektion: Attakai
* Introduktion til Attakai.
* Købsguide.
* Ændring af softwaren på en Antminer S9.
* Udskiftning af blæsere for at reducere støj.
* Poolkonfiguration.
* Konfiguration af Antminer S9 med Braiins OS+.

Er du klar til at begive dig ud på dette fængslende eventyr? Lad os sammen dykke ned i den fascinerende verden af hjemmeminedrift!

# Alt, hvad du behøver at vide om minedrift

## Forklaring af minedrift

![Hvad er Bitcoin Mining?](https://www.youtube.com/watch?v=neEQzEQzmPQ)

### Forklaring af minedrift: Puslespilsanalogi
For at forklare konceptet med mining på en forenklet måde kan en relevant analogi bruges: puslespil. Ligesom et puslespil er mining en kompleks opgave at udføre, men nem at verificere, når den er fuldført. I konteksten af Bitcoin mining stræber minearbejdere efter at løse et digitalt puslespil hurtigt. Den første minearbejder, der løser puslespillet, præsenterer sin løsning for hele netværket, som derefter nemt kan verificere dens gyldighed. Denne succesfulde verificering tillader minearbejderen at validere en ny blok og tilføje den til Bitcoin-tidskæden. Som anerkendelse af deres arbejde, der indebærer betydelige omkostninger, belønnes minearbejderen med et vist antal bitcoins. Denne belønning fungerer som en økonomisk motivationsfaktor for minearbejdere til at fortsætte deres arbejde med at validere transaktioner og sikre Bitcoin-netværket.
![image](assets/overview/puzzle.png)

I begyndelsen af Bitcoin-netværket var belønningen 50 bitcoins hvert tiende minut, parallelt med at minearbejdere i gennemsnit opdagede en blok hvert tiende minut. Denne belønning halveres hver 210.000 blokke, cirka hvert fjerde år. Denne aflønning fungerer som en stærk motivationsfaktor for at opfordre minearbejdere til at deltage i mining-processen på trods af dens energiomkostninger. Uden en belønning ville den energikrævende mining blive opgivet, hvilket ville true sikkerheden og stabiliteten i hele Bitcoin-netværket.
Den nuværende mining-belønning er todelt. På den ene side inkluderer den oprettelsen af nye bitcoins, der er faldet fra 50 bitcoins hvert tiende minut i begyndelsen til 6,25 bitcoins i dag (2023). På den anden side inkluderer den transaktionsgebyrer eller mining-gebyrer fra de transaktioner, som minearbejderen vælger at inkludere i deres blok. Når en bitcoin-transaktion foretages, betales der transaktionsgebyrer. Disse gebyrer fungerer som en slags auktion, hvor brugere angiver, hvor meget de er villige til at betale for at få deres transaktion inkluderet i den næste blok. For at maksimere deres belønning vælger minearbejdere, der handler i deres egen interesse, de mest profitable transaktioner til at inkludere i deres blok, idet de tager hensyn til den begrænsede tilgængelige plads. Således består mining-belønningen af både genereringen af nye bitcoins og transaktionsgebyrer, hvilket sikrer en kontinuerlig motivationsfaktor for minearbejdere og sikrer Bitcoin-netværkets lang levetid og sikkerhed.

### Minearbejdere og deres værktøjer: Mining

Mining-processen involverer at finde en gyldig hash, der accepteres af Bitcoin-netværket. Når denne hash er beregnet og fundet, er den uigenkaldelig, ligesom kartofler, der bliver til mos. Den verificerer en bestemt funktion uden mulighed for at gå tilbage. Minearbejdere bruger maskiner til at beregne disse hashes i konkurrence. Selvom det teoretisk er muligt at finde denne hash manuelt, gør kompleksiteten af ​​operationen denne mulighed uoverkommelig. Computere, der er i stand til at udføre disse beregninger hurtigt, bruges derfor og forbruger en betydelig mængde elektricitet.

I begyndelsen dominerede CPU-æraen, hvor minearbejdere brugte deres personlige computere til Bitcoin mining. Opdagelsen af fordelene ved GPU'er (grafikkort) til denne opgave markerede et vendepunkt, idet hashraten blev væsentligt øget, og energiforbruget blev reduceret. Fremskridtet stoppede ikke der, med den efterfølgende introduktion af FPGAs (field-programmable gate arrays). FPGAs fungerede som en platform for udviklingen af ASIC'er (application-specific integrated circuits).

![image](assets/overview/chip.png)

ASIC'er er chips, der kan sammenlignes med en CPU-chip, men de er udviklet til kun at udføre én bestemt type beregning på den mest effektive måde. Med andre ord er en CPU i stand til at udføre en mangfoldighed af forskellige typer beregninger uden at være specielt optimeret til en bestemt type beregning, hvorimod en ASIC kun vil være i stand til at udføre én type beregning, men meget effektivt. I tilfældet med Bitcoin ASIC'er er de designet til beregningen af ​​SHA256-algoritmen.
Nu til dags bruger minearbejdere udelukkende ASIC'er dedikeret til denne operation, optimeret til at teste det maksimale antal kombinationer med mindst muligt energiforbrug og så hurtigt som muligt. Disse computere, der ikke er i stand til at udføre andre opgaver end Bitcoin-minedrift, er et konkret bevis på den kontinuerlige udvikling og stigende specialisering af Bitcoin-minedriftindustrien. Denne konstante udvikling afspejler den intrinsiske dynamik i Bitcoin, hvor en sværhedsgradsjustering sikrer produktionen af en blok hvert tiende minut, på trods af den eksponentielle stigning i minedriftskapaciteten.

For at illustrere intensiteten af denne proces kan man overveje en typisk minearbejder, der er i stand til at opnå 14 TeraHash per sekund, eller 14 billioner forsøg hvert sekund for at finde den korrekte hash. På Bitcoin-netværkets skala når vi nu cirka 300 HexaHash per sekund, hvilket understreger den kollektive kraft, der mobiliseres i Bitcoin-minedrift.

### Sværhedsgradsjustering:

Sværhedsgradsjustering er en afgørende mekanisme i driften af Bitcoin-netværket, der sikrer, at blokke i gennemsnit mines hvert 10. minut. Denne varighed er et gennemsnit, fordi minedriftsprocessen faktisk er et spil med sandsynligheder, der ligner at rulle terninger i håbet om at få et tal, der er lavere end tallet defineret af sværhedsgraden. Hvert 2016. blok justerer netværket sværhedsgraden for minedriften baseret på den gennemsnitlige tid, der kræves for at mine de foregående blokke. Hvis den gennemsnitlige tid er større end 10 minutter, reduceres sværhedsgraden, og omvendt, hvis den gennemsnitlige tid er lavere, øges sværhedsgraden. Denne justeringsmekanisme sikrer, at minedriftstiden for nye blokke forbliver konstant over tid, uanset antallet af minearbejdere eller den samlede beregningskraft i netværket. Derfor kaldes Bitcoin Blockchain også for Timechain.

![image](assets/overview/chinaban.png)

* Eksempel fra Kina:
Kinas tilfælde illustrerer perfekt denne mekanisme for sværhedsgradsjustering. Med rigelig og billig energi var Kina det vigtigste globale knudepunkt for Bitcoin-minedrift. I 2021 forbød landet pludselig Bitcoin-minedrift på sit territorium, hvilket resulterede i et massivt fald i den globale Bitcoin-netværks hashhastighed, omkring 50%. Denne hurtige nedgang i minedriftskraften kunne have forstyrret Bitcoin-netværket alvorligt ved at øge den gennemsnitlige blokminedriftstid. Imidlertid trådte mekanismen for sværhedsgradsjustering i kraft og reducerede minedriftens sværhedsgrad for at sikre, at blokminedriftsfrekvensen forbliver i gennemsnit 10 minutter. Dette tilfælde demonstrerer effektiviteten og modstandsdygtigheden af ​​Bitcoin's mekanisme for sværhedsgradsjustering, der sikrer stabiliteten og forudsigeligheden af ​​netværket, selv i lyset af pludselige og betydelige ændringer i det globale minedriftslandskab.

### Udviklingen af Bitcoin-minedriftsmaskiner

Hvad angår udviklingen af Bitcoin-minedriftsmaskiner, er det vigtigt at bemærke, at konteksten er mere orienteret mod en traditionel forretningsmodel. Minearbejdere tjener deres indkomst fra blokvalidering, en opgave med en relativt lav sandsynlighed for succes. Den nuværende model i brug, Antminer S9, selvom det er en ældre model lanceret omkring 2016, er stadig i omløb på brugtmarkedet og handles til cirka €100 til €200. Prisen på minedriftsmaskiner varierer dog baseret på værdien af Bitcoin, og en nyere model, Antminer S19, er i øjeblikket estimeret til cirka €3000.

I lyset af konstante teknologiske fremskridt på minedriftsområdet skal fagfolk positionere sig strategisk. Minedriftsindustrien er underlagt kontinuerlige innovationer, som det er blevet demonstreret ved den nylige frigivelse af J-versionen af S19 og den forventede frigivelse af S19 XP, der tilbyder betydeligt højere minedriftskapacitet. Desuden er forbedringerne ikke kun relateret til maskinernes rå ydeevne. For eksempel bruger den nye S19 XP-model et væskekølesystem, en teknisk ændring, der muliggør en betydelig forbedring af energieffektiviteten. Selvom innovation forbliver en konstant, vil fremtidige effektivitetsgevinster sandsynligvis være mindre i forhold til dem, der hidtil er observeret, på grund af nåelse af en vis tærskel for teknologisk innovation.
![image](assets/overview/chipevolution.png)I konklusion fortsætter Bitcoin-minedriftsindustrien med at tilpasse sig og udvikle sig, og aktørerne i branchen skal forvente faldende effektivitetsgevinster i fremtiden og justere deres strategier derefter. Fremtidige teknologiske fremskridt, selvom de stadig er til stede, vil sandsynligvis ske på en mindre skala og afspejle sektorens voksende modenhed.
## Minedriftsindustrien

![Er Bitcoin-minedrift for centraliseret? Risici og løsninger](https://www.youtube.com/watch?v=xkiY8DgkcLQ)

### Minedriftspools

I øjeblikket har Bitcoin-minedrift udviklet sig til en seriøs og betydelig industri, hvor mange aktører nu er offentligt kendte, og antallet af betydelige minere stiger. Denne udvikling har gjort minedrift næsten utilgængelig for små aktører på grund af de høje omkostninger ved at anskaffe nye minedriftsmaskiner. Dette rejser spørgsmålet om fordelingen af hashhastighed blandt forskellige markedsaktører. Situationen er kompleks, fordi det er vigtigt at undersøge både fordelingen af hashhastighed mellem forskellige virksomheder og mellem forskellige minedriftspools.

![image](assets/overview/pool.png)

En minedriftspool er en gruppe af minere, der kombinerer deres beregningsressourcer for at øge deres chancer for minedrift. Dette samarbejde er nødvendigt, fordi en isoleret lille minedriftsmaskine konkurrerer mod industriens giganter og reducerer dens chancer for succes til et ubetydeligt niveau. Minedrift fungerer efter en lotteriprincip, og chancerne for at vinde en blok (og dermed Bitcoin-belønningen) hvert tiende minut er ekstremt lave for en individuel lille miner. Ved at samle deres kræfter kan minere kombinere deres beregningskraft, finde blokke hyppigere og derefter fordele belønningerne proportionelt til hver mineres bidrag til poolen.

For eksempel, hvis en pool finder en blok og vinder 6,25 bitcoins, vil en miner, der bidrager med 1% af den samlede beregningskraft i poolen, modtage 1% af de 6,25 bitcoins, der er tjent. Det skal dog bemærkes, at minedriftspools generelt tager en lille provision (normalt omkring 2%) for at dække de kooperative driftsomkostninger.

### Software anvendt af industrien

I konteksten af Bitcoin-minedrift er softwarens rolle lige så afgørende som hardwaren. Et eksempel på dette illustreres af Bitmains rolle som en produktiv producent, der udviklede Antminer S9. Ud over minedriftshardware er industrien i høj grad afhængig af samarbejdende minedriftspools som f.eks. Brainspool, der kontrollerer cirka 5% af den globale hashhastighed i Bitcoin-netværket.
Akteørerne i denne industri søger konstant at øge effektiviteten gennem hardware og software. Et populært software, der anvendes i denne sammenhæng, er f.eks. BrainsOS Plus. Denne software erstatter den oprindelige operativsystem på minedriftsmaskinen og gør det muligt at udføre de samme operationer mere effektivt. Med en sådan software kan en miner øge effektiviteten af deres maskine med 25%. Dette betyder, at maskinen med en tilsvarende mængde elektricitet kan producere yderligere 25% hashhastighed og dermed øge belønningerne, som mineren modtager. Denne softwareoptimering er et afgørende element for konkurrenceevnen inden for Bitcoin-minedrift og viser vigtigheden af en integreret tilgang, der kombinerer både hardware- og softwareforbedringer for at maksimere effektiviteten og afkastet.

### Regulering og eltariffer

Som det er observeret i Kina og andre steder, har regulering en betydelig indflydelse på minedrift. Selvom der ikke er betydelige minere i Frankrig, udgør regulering og høje eltariffer i Europa store hindringer. Minere søger konstant efter billig elektricitet for at maksimere deres fortjeneste. Derfor tiltrækker de høje omkostninger ved elektricitet i Europa og Frankrig ikke minere til disse regioner.
Miners har en tendens til at søge mod regioner med lave elpriser, ofte i udviklingslande eller lande med energioverskud. For eksempel er en stor del af den globale hashrate placeret i Texas, USA. Texas har et uafhængigt elnet, der ikke deler sine energiressourcer med andre stater. Denne unikke situation fører ofte til, at Texas producerer mere elektricitet end nødvendigt for at undgå mangel, hvilket skaber et overskud. Bitcoin-minere udnytter denne overproduktion ved at etablere operationer i Texas, hvor de kan mine bitcoins til meget lave elpriser i perioder med energioverskud. Denne situation demonstrerer den betydelige indflydelse, som reguleringer og elpriser har på Bitcoin-minedrift og understreger vigtigheden af disse faktorer i minernes beslutningstagning vedrørende placeringen af deres minedriftsoperationer.

### Hvor går minere hen og energistyring?

Ved at fremhæve Bitcoin-mineres indvirkning på energiområdet er kursen klar: Disse aktører søger konstant efter billig elektricitet, ofte den, der spildes eller ikke udnyttes. Dette fænomen er tydeligt i regioner med ny elektrisk infrastruktur, såsom dem der er udstyret med nyere vandkraftdæmninger.

Lad os tage et eksempel. I et land, der er ved at opføre en dæmning, begynder elproduktionen ofte, før distributionslinjerne er fuldt operationelle. Denne tidsforskel kan medføre betydelige omkostninger og afskrække investeringer i sådanne infrastrukturprojekter. Bitcoin-minere kan imidlertid fungere som en fleksibel efterspørgselskilde, der er klar til at forbruge denne "forældreløse" elektricitet og dermed bidrage til at opveje infrastruktursomkostningerne. Implikationen her er, at nye installationer kan være øjeblikkeligt rentable og fremme oprettelsen af nye kilder til elektricitet. Dette princip gælder også på mindre skala. Uanset om det er enkeltpersoner, der bruger et vandkraftværk ved en lille flod eller en husstand, der er udstyret med solpaneler, kan den overskydende elektricitet, der produceres, bruges til at drive bitcoin-minedrift.

I Frankrig injiceres overskydende elektricitet fra solpaneler f.eks. tilbage i nettet, og producenterne kompenseres med et forbrugskredit fra EDF. På samme måde kan man forestille sig en minedarbejder, der opererer på denne overskydende elektricitet og slukker, når den lokale efterspørgsel svarer til udbuddet. Selvom dette kan virke egoistisk og prioritere bitcoin-produktion over støtte til det lokale elnet, præsenterer det en anden vinkel: stabilisering af elnettet. Den komplekse håndtering af overskydende elektricitet, undertiden endda med tilknyttede omkostninger til bortskaffelse, kan blive meget forenklet. Bitcoin-minere kan absorbere disse overskud og fungere som en fleksibel buffer, der justerer efterspørgslen i stedet for udbuddet. I en verden, hvor elproduktion fra vedvarende (ikke-styrbare) kilder konstant stiger, kan minere spille en nøglerolle i at sikre balancen i vores elnet og samtidig drage fordel af billig eller overskydende elektricitet til at drive deres minedriftsoperationer.

### Centralisering af minedrift

Centralisering af minedrift behandles som en stor udfordring. Store aktører som Foundry dominerer markedet, hvilket potentielt kan føre til censur af transaktioner. Denne centralisering kan også gøre netværket sårbart over for angreb, herunder 51%-angrebet, hvor en aktør eller gruppe kontrollerer mere end 50% af netværkets hashkraft og dermed kan kontrollere og manipulere netværket.
Risikoen ved regulering Det understreges, at hvis et land som USA besluttede at regulere eller forbyde visse Bitcoin-transaktioner, kunne det have en betydelig indvirkning på netværket, især hvis en stor del af hashkraften er centraliseret i dette land.

![image](assets/overview/foundry.png)

For at bekæmpe denne centralisering diskuteres forskellige strategier:
* Hjemmeminedrift: Ideen om hjemmeminedrift er baseret på decentraliseringen af minedriftsaktiviteten. Den opfordrer enkeltpersoner til at deltage i minedrift fra deres hjem og dermed sprede hashkraften mere bredt.
* Stratum V2: Stratum V2-protokollen tilbyder en anden tilgang. I modsætning til sin forgænger giver Stratum V2 minearbejdere mulighed for at vælge, hvilke transaktioner de vil inkludere i de blokke, de miner. Denne evne styrker modstanden mod censur og reducerer evnen for store minepuljer til at dominere netværket. Ved at give mere magt til individuelle minearbejdere kan Stratum V2-protokollen spille en afgørende rolle i kampen mod hashhastighedscentralisering. Åbning af minedriftssoftware
* Åbning af minedriftssoftware: Dette er en anden potentielt effektiv strategi. Ved at gøre minedriftssoftware tilgængelig for alle ville små minearbejdere have de samme muligheder som store minevirksomheder for at deltage og bidrage til blockchain-netværket. Denne tilgang ville opfordre til en bredere fordeling af hashhastighed og dermed bidrage til netværksdecentralisering.
* Diversificering af aktører og geografi: At opfordre til deltagelse af forskellige aktører fra forskellige geografiske regioner i kryptomøntminedrift kan også vise sig effektivt. Ved at diversificere hashhastigheden geografisk bliver det sværere for en enkelt aktør eller et enkelt land at udøve uforholdsmæssig kontrol eller indflydelse over netværket. Denne tilgang kan hjælpe med at beskytte netværket mod potentielle angreb og styrke dets decentralisering.

Den generelle konklusion er, at decentralisering er afgørende for sikkerheden og modstandsdygtigheden af Bitcoin-netværket. Selvom centralisering kan tilbyde effektivitetsfordele, udsætter det netværket for betydelige risici, herunder censur og 51% angreb. Initiativer som Takai og vedtagelsen af nye protokoller som Stratum V2 er vigtige skridt mod decentralisering og beskyttelse af Bitcoin-netværket mod disse trusler.

## Nuancer i minedriftsindustrien

![Opvarmning af dit hjem ved at mine bitcoins?](https://www.youtube.com/watch?v=SQaK4_8M0kA)

### Princippet om Attakai
Grænsen for denne decentralisering?
Selvom ideen om at decentralisere minedrift gennem brugen af genereret varme virker lovende, har den visse begrænsninger, og der er stadig spørgsmål, der står åbne. Energiintensive etablissementer som saunaer og pools kunne drage fordel af denne koncept ved at bruge varmen produceret af minearbejdere til at varme vandet i deres faciliteter. Denne praksis implementeres allerede af nogle medlemmer af Bitcoin-fællesskabet, der udforsker forskellige metoder til effektivt at udnytte den varme, der genereres af minedriftsudstyr. For eksempel kunne en festhal teoretisk set opvarmes af tre eller fire S19-minedarbejdere, der hver forbruger 3000 watt og producerer en tilsvarende mængde varme.

Det skal dog bemærkes, at energiforbrug og varmeproduktion er ensbetydende, uanset om energien bruges af en elektrisk varmelegeme eller en minearbejder. For hver kilowatt elektricitet, der bruges, vil mængden af varme, der produceres, være den samme i begge tilfælde. Forskellen ligger i det faktum, at minearbejderen ikke kun giver varme, men også en bitcoin-belønning og dermed tilbyder en økonomisk incitament til at bruge en minearbejder i stedet for en simpel elektrisk varmelegeme. Denne ekstra belønning kan hjælpe med at afhjælpe bekymringer vedrørende de høje energiforbrug af minearbejdere.

Spørgsmålet om den langsigtede effektivitet og gennemførlighed af at bruge bitcoin-minedarbejdere til opvarmning forbliver åbent. Igangværende innovationer inden for minedriftshardware og opvarmningsteknologier kan potentielt åbne nye muligheder for mere effektiv brug af den varme, der genereres af minedrift og dermed bidrage til levedygtigheden af denne tilgang i fremtiden.

### Hvorfor belønninger i BTC?

Spørgsmålet om at belønne i bitcoin i stedet for en anden valuta er afgørende i det system, der er forestillet af Satoshi Nakamoto. Oprettelsen af Bitcoin er kendetegnet ved en fast grænse på 21 millioner enheder. Målet var at finde en retfærdig måde at distribuere disse nyoprettede enheder på. Minearbejdere, ved at levere deres regnekraft til at sikre netværket og gøre ethvert angreb stadig dyrere, beskytter effektivt Bitcoin-netværket. Som tak for denne afgørende bidrag belønnes de med nyoprettede bitcoins, hvilket letter distributionen af mønter inden for økosystemet.
Det er et win-win-system. Miners belønnes både for at sikre netværket og godkende transaktioner. De nyoprettede bitcoins gives som en incitament til at styrke sikkerheden, og transaktionsgebyrer udgør en ekstra indtægt for godkendelse af transaktioner. Disse to elementer udgør tilsammen den samlede belønning for mining. Spørgsmålet om fremtiden for mining opstår på grund af den programmerede reduktion af mining-belønninger, der halveres hvert fjerde år, en begivenhed kendt som "halving". I 2032 vil blokbelønningen være mindre end en bitcoin, og i 2140 vil der ikke blive oprettet nye bitcoins. På dette tidspunkt vil miners udelukkende være afhængige af transaktionsgebyrer som kompensation. Bitcoin-netværket skal kunne understøtte et stort antal transaktioner med tilstrækkeligt høje gebyrer for at sikre miningens rentabilitet. Fremkomsten af Lightning Network, der muliggør hurtige og billige transaktioner uden for hoved-Bitcoin-kæden, rejser spørgsmål om fremtiden for mining. Lightning Network har potentialet til markant at reducere transaktionsgebyrerne, hvilket påvirker miners' indtægter. Dette vil dog afhænge af vedtagelsen og brugen af Lightning Network i forhold til hoved-Bitcoin-netværket. I et pessimistisk scenarie kan miners finde det rentabelt at mine, selvom de lider tab, hvis de har amortiseret deres omkostninger og har adgang til billig elektricitet. I et mere optimistisk scenarie kan transaktionsgebyrerne på hoved-Bitcoin-netværket forblive høje nok til at opretholde miningens rentabilitet.

### Hvad skal inkluderes i en Bitcoin-blok?

Når det kommer til spørgsmålet om, hvad der skal inkluderes i en Bitcoin-blok, er det afgørende at tage hensyn til de forskellige lag i Bitcoin-netværket, der supplerer hinanden. Selvom Lightning Network kan muliggøre hurtigere og billigere transaktioner, er det stadig afhængigt af baselaget i Bitcoin, der ofte kaldes "afviklingslaget", for at åbne og lukke betalingskanaler.

Med den forventede vækst af Lightning Network og den deraf følgende stigning i åbning og lukning af kanaler vil pladsen i Bitcoin-blokke blive stadig mere værdifuld. Bitcoin-fællesskabet værdsætter allerede bevarelsen af denne plads og anerkender dens intrinsikke begrænsning. Denne bevidsthed har ført til diskussioner om den legitime brug af blokplads med bekymringer om "spam" på blockchain fra transaktioner, der anses for ikke-essentielle.

![image](assets/overview/block.png)
Der spekuleres om fremtidig brug af blokplads, men det er generelt accepteret, at det er en knap ressource, der bør bruges klogt. Selvom der er et ønske om at fylde den, er det vigtigt at bevare den for at sikre Bitcoin-netværkets langsigtede levedygtighed og forvente en fremtidig stigning i efterspørgslen efter blokplads. Som i enhver fri markedsøkonomi vil udbud og efterspørgsel regulere brugen af blokplads. Med begrænset udbud vil interessenterne skulle træffe informerede valg om brugen af denne værdifulde plads for at sikre Bitcoin-netværkets langsigtede effektivitet og sikkerhed.

## Mining i Bitcoin-protokollen

![Hvem har magten? Bitcoin, energi og producenter](https://www.youtube.com/watch?v=4wywK6BfDw8)

Miners' rolle i Bitcoin-netværket har været genstand for intens debat under blokkonflikterne. Selvom de er afgørende for netværkets sikkerhed og funktionalitet, har miners ikke nødvendigvis den ultimative magt i Bitcoin-økosystemet. Balancen mellem miners, noder og slutbrugere sikrer netværkets integritet og distribution.

### Blokkonflikterne

Under blokkonflikterne var mange miners imod visse netværksudviklinger, hvilket understreger spændingerne mellem forskellige aktører i økosystemet. Spørgsmålet er stadig, hvordan man balancerer magten mellem miners, noder og brugere for at sikre Bitcoin's langsigtede sikkerhed.

Sikkerhed og magtbalancen

![image](assets/overview/blocksize-wars--BTC-vs-BCH-.webp)
Sikkerhedsdilemmaet for Bitcoin er afhængig af en skrøbelig balance. Mens minearbejdere spiller en afgørende rolle i validering og oprettelse af blokke, opretholder noder integriteten ved at verificere og validere transaktioner og blokke. En forkert eller svigagtig blok vil blive afvist af noder, hvilket censurerer minearbejderen og bevarer netværkets sikkerhed. Magten ligger også hos noder og brugere af Bitcoin-netværket. Noder har magten til verifikation og validering, mens brugere har magten til at vælge hvilken blockchain de vil bruge. Denne magtdeling sikrer distributionen og integriteten af Bitcoin-netværket.
Blokkens krige afslørede den iboende usikkerhed og spænding ved at styre Bitcoin-netværket. Selvom Bitcoin Core i øjeblikket er den dominerende kæde, fortsætter debatten om styring og netværksstyring.
I sidste ende deles ansvaret mellem alle aktører i Bitcoin-netværket. En nedgang i antallet af brugere, noder eller minearbejdere kan svække netværket og øge risikoen for centralisering og sårbarhed over for angreb. Hver aktør bidrager til netværkets robusthed og sikkerhed og understreger vigtigheden af at opretholde en balance mellem magt og ansvar.
### Minearbejdernes magt

Satoshi Nakamotos elegante spilteori etablerede en situation, hvor enhver aktør i Bitcoin-netværket har incitament til at handle korrekt for at beskytte både deres egne interesser og de andre deltagere. Dette skaber en balance, hvor dårlig opførsel kan straffes og dermed styrke sikkerheden og stabiliteten i hele systemet. På trods af denne balance forbliver stater en potentiel trussel. Som det blev angivet i præsentationen på Surfing Bitcoin 2022, kan stater forsøge at angribe minedriftsindustrien og udsætte Bitcoin-netværket for risici for centralisering og angreb. Hypotetiske scenarier som et militært angreb rettet mod produktionsfaciliteter for minedriftshardware understreger vigtigheden af geografisk og industrielt diversificering for Bitcoin-netværkets modstandsdygtighed.

![image](assets/overview/miner.png)

Centraliseringen af minedriftshardwareproduktion i Kina udgør en anden risiko. En afvisning af eksport af minedriftsmaskiner eller en akkumulering af hashrate til et potentiel 51% angreb fra Kina understreger behovet for diversificeret minedriftshardwareproduktion. Konfronteret med disse risici udforsker Bitcoin-fællesskabet aktivt løsninger. Virksomheder som Intel overvejer at producere minedriftsudstyr i USA og bidrage til distributionen af produktionen. Andre initiativer, som f.eks. Blocks open-source Mining Development Kit (MDK), sigter mod at reducere monopoliseringen af minedriftshardware-design og produktion og tillade en bredere distribution af hashrate. I hjertet af disse diskussioner ligger Bitcoins grundlæggende mission: at være et censurresistent værdiudvekslingsnetværk. Bitcoin-fællesskabet stræber konstant efter at styrke distributionen, censurmodstanden og netværkets anti-fragilitet og afviser forslag som overgang til proof of stake, der ikke er i overensstemmelse med disse grundlæggende principper.

### Det fysiske link mellem proof of work og proof of stake
Proof of Work (PoW) er afgørende, fordi det repræsenterer den fysiske forbindelse mellem den virkelige verden og Bitcoin. Selvom bitcoins er immaterielle, kræver deres produktion håndgribelig energi, hvilket etablerer en direkte forbindelse til den fysiske og virkelige verden. Denne forbindelse sikrer, at produktionen og valideringen af bitcoins og blokke har en reel energiomkostning, der forankrer Bitcoin-netværket i fysisk virkelighed og forhindrer dets fuldstændige dominans af magtfulde enheder. PoW fungerer som en barriere mod centralisering og sikrer, at deltagelse i netværket og validering af transaktioner kræver en investering i håndgribelige ressourcer. Dette forhindrer monopoliseringen af netværket af enheder, der ellers kunne overtage kontrollen uden betydelige indgangsbarrierer og sikrer dermed en mere retfærdig fordeling af magt og indflydelse inden for Bitcoin-netværket.

![image](assets/overview/POWPOS.png)

### Begrænsninger ved Proof of Stake
På den anden side garanterer Proof of Stake (PoS), selvom det tillader deltagelse i små skala, ikke en tilsvarende beskyttelse mod centralisering. I et PoS-netværk har de, der allerede ejer en stor mængde valuta, en uforholdsmæssig magt, der afspejler eksisterende magtuligheder i samfundet generelt. Denne dynamik kan potentielt opretholde centralisering og koncentration af magt i få hænder, i modsætning til de grundlæggende mål om at distribuere Bitcoin-netværket. Argumentet om, at alle kan deltage i PoS, selv i lille skala, ved at deltage i puljer, er ikke nødvendigvis stærkt. I et PoW-netværk kan selv en lille bidragyder med beskedent udstyr aktivt deltage og bidrage til sikkerheden og distributionen af netværket.
### Opsummering

For at opsummere, styrker minearbejdere Bitcoin-netværket mod censur ved at bruge elektricitet til at beregne beviset for arbejde for Bitcoin, og de belønnes med nye bitcoins og transaktionsgebyrer. Med professionaliseringen af branchen opstår der forskellige aktører, der spiller forskellige roller, lige fra chipproduktion til drift af minefarme. Derudover blander finanssektoren sig også og udøver kontrol ved at beslutte, hvem der overlever i forskellige markedsfaser. Problemet med centralisering fortsætter, hvor de rigeste enheder potentielt kan dominere markedet. Der udvikles dog alternativer på hardware- og softwareniveauer. Det er op til den enkelte at handle og bidrage til distributionen af netværket. Bitcoin repræsenterer en hidtil uset mulighed, ikke kun med hensyn til frihed, men også energiuafhængighed. På trods af kontroverser omkring dets elforbrug tilbyder Bitcoin en økonomisk incitament til en overgang til en mere rationel og rigelig brug af energi, hvilket realiserer det, der tidligere var en økologisk ideal.

## Bitcoin-pris og hashrate, en sammenhæng?
Minearbejde for profit eller for netværket?

Den nuværende hashrate, selvom prisen på Bitcoin er på $30.000 sammenlignet med sit tidligere højdepunkt på $69.000, understreger den konkrete forbindelse mellem minearbejde og den virkelige verden. Perioder med prisstigninger (bull marked) fører til en høj efterspørgsel efter Bitcoin-minedrift og en stigning i maskinordrer fra producenter som Avalon og Bitmain. Produktion og levering sker dog ikke øjeblikkeligt, hvilket skaber en uoverensstemmelse mellem øget efterspørgsel og senere tilgængelighed. Dette kan føre til levering af maskiner, der er bestilt under et bull marked, i et faldende marked, hvilket fremhæver en bemærkelsesværdig asymmetri mellem lav pris og høj hashrate.

Denne situation illustrerer også Bitcoin's modstandsdygtighed, der ofte vurderes ud fra dens pris. En dybere analyse af Bitcoin's sundhed kræver imidlertid en undersøgelse af dens hashrate, der måler beregningerne pr. sekund i Bitcoin-netværket. Mens prisen på Bitcoin svinger, forbliver dens omkostning, relateret til den elektricitet, der er nødvendig for at drive minedriftsmaskiner, afgørende for at forstå markedets dynamik. Ved at fokusere på omkostninger i stedet for pris opnås et mere konsistent perspektiv på Bitcoin's stabilitet og langsigtede levedygtighed. Generelt er omkostningen ved Bitcoin proportional med dens pris, hvilket giver en bedre forståelse af prisudsving og fremtidige udsigter.

Hashrate og belønning

Minedrift fastsætter en bundpris for Bitcoin, under hvilken minearbejdere ville sælge med tab. Omkostningen ved minedrift påvirker i høj grad prisen, som illustreret ved forbuddet mod minedrift i Kina, hvor hashraten og prisen faldt markant, men hurtigt kom sig igen. At fokusere udelukkende på pris kan være vildledende. Studier af omkostninger gennem profitabilitetsberegninger giver et mere afbalanceret perspektiv. Markedet kan dog opføre sig irrationelt, hvor minearbejdere tvinges til at sælge med tab, hvilket potentielt sænker prisen under minedriftsomkostningerne. For at vurdere Bitcoin's sundhed og decentralisering kan en ligning udvikles, der inkorporerer forskellige faktorer som antallet af noder og prisen. Denne tilgang kunne give en mere nuanceret analyse af Bitcoin i forhold til diskussioner baseret udelukkende på pris.

Minearbejde for profit eller for netværket?
Spørgsmålet er dybtgående og omfatter flere dimensioner af Bitcoin-minedrift. Balancen mellem at søge profit og bidrage til sikkerheden og distributionen af Bitcoin-netværket er en konstant dilemma for minearbejdere. Debatten fortsætter inden for Bitcoin-fællesskabet med stærke argumenter på begge sider.

* Mining for profit:
  - For: Minearbejdere er naturligt tiltrukket af det potentielle overskud, som Bitcoin-minedrift tilbyder. Investering i dyrt minedriftudstyr kan være profitabelt gennem minedriftsbelønninger og transaktionsgebyrer, især når prisen på Bitcoin er høj.
  - Imod: Søgen efter profit kan føre til centralisering af hashkraft, hvis kun få store virksomheder har råd til at investere i high-end minedriftudstyr. Derudover kan energiforbruget ved minedrift for profit have en betydelig miljømæssig indvirkning.

* Mining for netværket:
  - For: Minedrift for at bidrage til sikkerheden og decentraliseringen af Bitcoin-netværket er en ædel initiativ. Det hjælper med at styrke netværkets modstandsdygtighed og modstand mod censur og angreb.
  - Imod: Uden tilstrækkelig økonomisk incitament kan det være svært for minearbejdere at fortsætte med at støtte netværket, især hvis de opererer med tab.

Attakai-initiativet fremhæver vigtigheden af at bidrage til netværket samtidig med at det tilbyder løsninger for at gøre minedrift mere tilgængelig og mindre skadelig. Evnen til at mine derhjemme med mere overkommeligt hardware og løsninger til at reducere støjforurening kan hjælpe med at demokratisere Bitcoin-minedrift. Det opfordrer dem, der er interesseret i Bitcoin, ikke kun til at investere og holde bitcoins, men også til aktivt at deltage i sikringen af netværket. Ved at levere testet udstyr og vejledninger til samling og installation letter Attakai indtræden i verdenen af Bitcoin-minedrift. Det opmuntrer også til innovation og kontinuerlige forbedringer og inviterer fællesskabet til at bidrage og dele deres ideer og erfaringer for at forbedre hjemmeminedrift. Attakai-modellen er et svar på spørgsmålet om minedrift for profit eller for netværket. Det handler ikke kun om at skabe overskud, men også om at styrke distributionen og sikkerheden af Bitcoin-netværket samtidig med at flere mennesker kan deltage i minedrift, lære og forstå denne afgørende industri. Udfordringen med et potentiel minedriftsforbud i Europa forbliver et åbent spørgsmål. Dette rejser bekymringer om fremtiden for Bitcoin-minedrift i regionen og behovet for afbalanceret regulering, der anerkender vigtigheden af minedrift for sikkerheden og levedygtigheden af Bitcoin-netværket, samtidig med at miljømæssige spørgsmål adresseres. Attakai og lignende initiativer kan spille en afgørende rolle i denne debat ved at vise, at det er muligt at mine på en mere bæredygtig og ansvarlig måde samtidig med at man positivt bidrager til Bitcoin-netværket.

## Suverænitet og regulering
### Suverænitet før profit?
For at besvare det afgørende spørgsmål om rigdom gennem minedrift er det vigtigt at overveje forskellige perspektiver og tilgange. Spørgsmål om minedriftens rentabilitet er almindelige, med bekymringer om køb af aktier i virksomheder som Riot eller leje af minedriftsmaskiner i lande med lav energiomkostning som Island eller Rusland. Før man begiver sig ud i minedrift, vil det være vigtigt at sammenligne minedriftens rentabilitet med direkte køb af Bitcoin. Hvis omkostningen ved at mine en Bitcoin overstiger omkostningen ved direkte køb, er det generelt klogere at købe Bitcoin direkte. Dette undgår de mange udfordringer og omkostninger, der er forbundet med minedriftsprocessen.

Dog tilbyder minedrift unikke muligheder for at blive involveret i Bitcoin-økosystemet. For eksempel kan minedrift af Bitcoin om vinteren være en smart måde at opvarme dit hjem på samtidig med at du genererer indkomst i Bitcoin. En anden mulighed er at investere i virksomheder, der sælger minedriftshardware og opbevarer og administrerer maskinerne i lande med lav energiomkostning, hvilket giver adgang til fordelagtige elpriser uden besværet med udstyrsadministration.
Trods disse muligheder præsenterer minedrift betydelige udfordringer. Det velkendte ordsprog i kryptoverdenen, "Ikke dine nøgler, ikke dine Bitcoins," finder en lignende genklang i minedriftsverdenen: "Ikke din hashrate, ikke din belønning." Historier om skuffelser og afbrudte maskiner er almindelige, hvor mange aktører lover exceptionelle resultater, men ikke leverer dem. Problemer med strømforsyning og maskinsvigt kan efterlade investorer magtesløse med dyrt udstyr, som de ikke har kontrol over. I denne sammenhæng er forsigtighed og en dyb forståelse af minedriftssektoren afgørende, før man begiver sig ud i det. Selvom der er muligheder for gevinster, er risiciene betydelige, og en informeret og eftertænksom tilgang er afgørende for at navigere i dette komplekse og ofte uforudsigelige felt. Derfor er grundig research og omhyggelig overvejelse af fordele og ulemper afgørende, før man begiver sig ud i Bitcoin-minedrift.
![billede](assets/overview/self.png)

### Jomfru Bitcoins
Er minedrift forbudt i Europa?

Oversættelse:
Ønsket om at eje sin egen hashrate præsenterer sig som en lovende vej i minedriftens verden. Dog kræver det at navigere i dette komplekse økosystem en forsigtig tilgang. Cloud mining-industrien er præget af et stort antal svindelnumre, drevet af manglende forståelse for minedrift fra mange investorer. Fristende tilbud, pakket ind på forskellige måder, kan nemt føre de uvidende på vildspor. På den anden side tilbyder ejerskab af ens egen minedriftsudstyr betydelige fordele. Udover den personlige tilfredsstillelse ved aktivt at bidrage til sikkerheden i Bitcoin-netværket og se belønningerne falde ind i ens tegnebog, er der også den attraktive faktor ved "jomfru bitcoins". Disse er nyligt mined bitcoins, der aldrig er blevet brugt og ikke har nogen historie knyttet til dem. Disse bitcoins betragtes ofte som mere værdifulde, fordi de aldrig er blevet "besmittet", hvilket giver en vis garanti mod afvisning af reguleringsmyndigheder eller større handelsplatforme.
Evnen til at mine jomfru bitcoins og samtidig undgå know-your-customer (KYC) procedurer er en anden merværdi. Mange minedriftspools kræver ikke, at minearbejdere opgiver deres identitet, hvilket giver dem mulighed for at erhverve bitcoins uden at skulle igennem kedelige identitetsverifikationsprocesser. Jomfru bitcoins opfattes som "rene", uden nogen tidligere historie eller tilknytning. De er særligt eftertragtede af store institutionelle spillere, der kan garantere legitimiteten af deres digitale aktiver over for reguleringsmyndigheder. Dog er det vigtigt at erkende, at minedriftsindustrien forbliver ekstremt konkurrencedygtig og volatil, og uforudsete hændelser kan forstyrre minedriftsoperationer.

I denne sammenhæng virker det klogt at vælge en autonom og velinformeret tilgang til minedrift. At erhverve sin egen hashrate og investere i personligt minedriftsudstyr, samtidig med at man er opmærksom på risici og udfordringer, kan potentielt tilbyde en sikrere og mere tilfredsstillende vej til at erhverve jomfru bitcoins og dermed styrke individuel økonomisk suverænitet samtidig med at man støtter Bitcoin-økosystemet som helhed.

### Er minedrift forbudt i Europa?
Med spørgsmålet om et potentiel forbud mod minedrift i Europa bliver diskussioner om regulering i stigende grad relevante. Den skiftende reguleringsmæssige landskab kan faktisk have en betydelig indvirkning på Bitcoin-minedriftsindustrien. Et forbud mod minedrift i Europa er en tænkelig scenarie, især med tanke på præcedenserne i Kina. Selvom minedriftsoperationer fortsætter i Kina trods forbuddet, kan Europa følge en lignende vej. En bredere fordeling af hashraten i forskellige regioner kan hjælpe med at styrke minedriftssamfundet i Europa og gøre dem i stand til effektivt at imødegå misforståelser og fejlopfattelser om minedrift, dens miljømæssige påvirkning og dens aftryk på elnettet.
![billede](assets/overview/regulation.jpg)
Konfronteret med kampagner som dem fra Greenpeace og de ofte vildledende tal fra visse undersøgelser, forbliver den bedste våben nøjagtig information. Det er afgørende at informere offentligheden og beslutningstagere om virkeligheden ved minedrift, dens kompleksitet og nuancer, i stedet for at lade dem stole på stereotyper og unøjagtig information. Jo mere informerede og opmærksomme mennesker der er om, hvad minedrift virkelig er, desto bedre kan industrien forsvare sig mod potentielt restriktive reguleringer.

Konklusionen er, at på trods af den reguleringsmæssige risiko og muligheden for et forbud mod minedrift i Europa, forbliver den mest kraftfulde våben uddannelse og information. En klar og præcis forståelse af minedrift, hvordan det fungerer, og dets indvirkning kan hjælpe med at afmystificere industrien og bekæmpe misinformation, og dermed tilbyde bedre modstand mod potentielt skadelig regulering. Initiativet til at uddanne og informere folk om minedrift, som denne diskussion gør, er et skridt i den rigtige retning for at sikre bæredygtigheden og væksten af minedrift i Europa og rundt om i verden. Fortsatte bestræbelser på at uddanne og informere er afgørende for at sikre en sikker og velstående fremtid for Bitcoin-minedriftsindustrien.

## Interview med en professionel inden for minedriftsindustrien

### Bag kulisserne i industrielt minedrift - Sebastien Gouspillou

![Bag kulisserne i industrielt minedrift - Sebastien Gouspillou](https://www.youtube.com/watch?v=vYaQRLSDr5E&t=69s)

# Hjemmeminedrift og genbrug af varme

## Attakai - gør hjemmeminedrift mulig og tilgængelig!

![Introduktion til Attakaï!](https://www.youtube.com/watch?v=gKoh44UCSnE&t=3s)

Attakai, der betyder "den ideelle temperatur" på japansk, er navnet på initiativet, der sigter mod at opdage bitcoin-minedrift gennem genbrug af varme, lanceret af @ajelexBTC og @jimzap21 med Découvre Bitcoin.
Denne guide til ASIC-ombygning vil tjene som grundlag for at lære mere om minedrift, dens drift og den underliggende økonomi ved at demonstrere muligheden for at tilpasse en Bitcoin-miner til brug som radiatorer i hjemmet. Dette giver mere komfort og besparelser, og deltagerne kan modtage ikke-KYC BTC-kontanter tilbage på deres elvarmeregning.

Bitcoin justerer automatisk minedriftens sværhedsgrad og belønner minearbejdere for deres deltagelse. Dog kan koncentrationen af hashkraft udgøre risici for netværkets neutralitet. Ved at bruge Bitcoin's regnekraft til varmeløsninger kommer netværket selv til gode ved at øge distributionen af regnekraft.

### Hvorfor genbruge varmen fra en ASIC?

Det er vigtigt at forstå forholdet mellem energi- og varmeproduktion i et elektrisk system.

For en investering på 1 kW elektrisk energi producerer en elektrisk radiator 1 kW varme, hverken mere eller mindre. Nye radiatorer er ikke mere effektive end traditionelle radiatorer. Deres fordel ligger i deres evne til kontinuerligt og jævnt at fordele varme i et rum, hvilket giver mere komfort i forhold til traditionelle radiatorer, der skifter mellem høj varmeeffekt og ingen opvarmning og dermed genererer regelmæssige temperaturvariationer og ubehag.

En computer, eller bredere set et elektronisk kredsløb, forbruger ikke energi til at udføre beregninger, den har simpelthen brug for energi til at strømme gennem dens komponenter for at fungere. Energiforbruget skyldes komponenternes elektriske modstand, der producerer tab og genererer varme, kendt som Joule-effekten.
Nogle virksomheder har fået ideen om at kombinere behovet for computere med behovet for opvarmning gennem radiatorer/servere. Ideen er at fordele en virksomheds servere i små enheder, der kan placeres i hjem eller kontorer. Dog støder denne idé på flere problemer. Behovet for servere er ikke relateret til behovet for opvarmning, og virksomheder kan ikke fleksibelt bruge deres servers regnekraft. Der er også begrænsninger for den båndbredde, enkeltpersoner kan have. Alle disse begrænsninger forhindrer virksomheden i at gøre disse dyre installationer profitable eller at tilbyde en stabil online server uden datacentre, der kan overtage, når der ikke er behov for opvarmning. "Varmen, der genereres af din computer, går ikke til spilde, hvis du har brug for at opvarme dit hjem. Hvis du bruger elektrisk opvarmning, hvor du bor, går varmen fra din computer ikke til spilde. Det koster det samme at generere denne varme med din computer. Hvis du har et billigere opvarmningssystem end elektrisk opvarmning, er spildet kun i prisforskellen. Hvis det er sommer, og du bruger aircondition, er det dobbelt spild. Bitcoin-minedrift bør finde sted, hvor det er billigere. Måske vil det være der, hvor klimaet er koldt, og hvor opvarmning er elektrisk, at minedriften bliver gratis."
> Satoshi Nakamoto - 8. august 2010

Bitcoin og dets proof of work skiller sig ud, fordi de automatisk justerer minedifficulty baseret på den samlede netværks beregningskraft. Denne mængde kaldes hashrate og udtrykkes i hashes per sekund. I dag estimeres det til 380 exahashes per sekund, hvilket svarer til 380 billioner billioner hashes per sekund. Denne hashrate repræsenterer arbejde og dermed en mængde energi, der bruges. Jo højere hashrate, desto højere er sværhedsgraden, og omvendt. Således kan en Bitcoin-miner aktiveres eller deaktiveres når som helst uden at påvirke netværket, i modsætning til radiatorer/servere, der skal forblive stabile for at levere deres service. Minerens deltagelse belønnes i forhold til andre, uanset hvor lille den måtte være.

Sammenfattende producerer en elektrisk radiator og en Bitcoin-miner begge 1 kW varme for 1 kW elektricitet, der forbruges. Dog modtager mineren også bitcoins som belønning. Uanset prisen på elektricitet, prisen på bitcoin eller konkurrencen inden for Bitcoin-minedrift på netværket er det økonomisk mere fordelagtigt at opvarme med en miner frem for en elektrisk radiator.

### Mehrwert für Bitcoin

Det er vigtigt at forstå, hvordan minedrift bidrager til decentraliseringen af Bitcoin. Flere eksisterende teknologier er blevet kombineret på en genial måde for at bringe Nakamotos konsensus til live. Denne konsensus belønner økonomisk ærlige deltagere for deres bidrag til driften af Bitcoin-netværket, samtidig med at det afskrækker uærlige deltagere. Dette er en af de centrale punkter, der gør det muligt for netværket at eksistere bæredygtigt. Ærlige aktører, dem der miner i overensstemmelse med reglerne, konkurrerer alle med hinanden for at opnå den størst mulige del af belønningen for at producere nye blokke. Denne økonomiske incitament fører naturligt til en form for centralisering, da virksomheder vælger at specialisere sig i denne indbringende aktivitet ved at reducere deres omkostninger gennem stordriftsfordele. Disse industrielle aktører har en fordelagtig position for at købe og vedligeholde maskiner samt forhandle om engros elpriser.

> "I starten ville de fleste brugere køre netværksnoder, men når netværket vokser ud over et vist punkt, ville det i stigende grad blive overladt til specialister med serverfarme af specialiseret hardware. En serverfarm ville kun have brug for at have en node på netværket, og resten af LAN'en ville forbinde til den node."
>
> - Satoshi Nakamoto - 2. november 2008
Visse enheder har en betydelig procentdel af den samlede hashrate i store minedriftsfarme. Vi kan observere den seneste kuldebølge i USA, hvor en betydelig del af hashraten blev taget offline for at omdirigere energi til husholdninger med et ekstraordinært behov for elektricitet. I flere dage blev minearbejdere økonomisk tilskyndet til at lukke deres farme, og dette ekstraordinære vejr kan ses på Bitcoin-hashtaktkurven.
Dette problem kan blive problematisk og udgør en betydelig risiko for netværkets neutralitet. En aktør med mere end 51% af hashraten kunne lettere censurere transaktioner, hvis de ønskede det. Derfor er det vigtigt at fordele hashraten mellem flere aktører i stedet for centraliserede enheder, der kunne beslaglægges lettere af en regering, for eksempel.

**Hvis minearbejdere er fordelt i tusindvis eller endda millioner af husstande over hele verden, bliver det meget svært for en stat at tage kontrol over dem.**

Når en miner kommer ud af fabrikken, er den ikke egnet til brug som en varmelegeme i et hjem på grund af to hovedproblemer: overdreven støj og manglende justering. Disse problemer kan dog nemt løses gennem hardware- og softwaremodifikationer, der tillader en meget mere støjsvag miner, der kan konfigureres og automatiseres som moderne elektriske varmelegemer.

**Attakaï er et uddannelsesinitiativ, der lærer dig, hvordan du ombygger Antminer S9 på den mest omkostningseffektive måde.**

Dette er en fremragende mulighed for at lære ved at praktisere, samtidig med at du bliver belønnet for din deltagelse med KYC-fri satoshis.

## Købsguide til en brugt ASIC

![Introduktion til Attakaï: Opvarmning med Bitcoin](https://www.youtube.com/watch?v=U_PLo59lp-g)
I denne sektion vil vi diskutere bedste praksis for køb af en brugt Bitmain Antminer S9, maskinen som denne radiatorombygningsvejledning vil være baseret på. Denne guide gælder også for andre modeller af ASIC'er, da det er en generel købsguide til brugt minedriftshardware.

Antminer S9 er en enhed, der tilbydes af Bitmain siden maj 2016. Den bruger 1400W elektricitet og producerer 13,5 TH/s. Selvom den betragtes som gammel, forbliver den en fremragende mulighed for at starte minedrift. Da den er blevet produceret i store mængder, er det nemt at finde reservedele i overflod i mange regioner af verden. Den kan generelt erhverves peer-to-peer på websteder som eBay eller LeBonCoin, da professionelle forhandlere ikke længere tilbyder den på grund af dens lavere konkurrenceevne i forhold til nyere maskiner. Den er mindre effektiv end ASIC'er som Antminer S19, der er tilbudt siden marts 2020, men dette gør den til en overkommelig brugt hardware og mere egnet til de ændringer, vi vil foretage.

Antminer S9 leveres i flere variationer (i, j), der foretager mindre ændringer i hardwaren fra første generation. Vi mener ikke, at dette bør påvirke dit købsbeslutning, og denne guide fungerer for alle disse variationer.

Prisen på ASIC'er varierer afhængigt af mange faktorer som bitcoin-prisen, netværkets sværhedsgrad, maskineeffektivitet og elektricitetsomkostninger. Det er derfor svært at give et præcist skøn for købet af en brugt maskine. I februar 2023 ligger den forventede pris i Frankrig generelt mellem €100 og €200, men disse priser kan ændre sig hurtigt.

![billede](assets/guide-achat/1.jpeg)

Antminer S9 består af følgende dele:

- 3 hashboards, der indeholder chipsene, der producerer hashkraften.

![billede](assets/guide-achat/2.jpeg)

- Et kontrolkort, der inkluderer en plads til et SD-kort, en Ethernet-port og stik til hashboards og blæsere. Dette er hjernen i din ASIC.
![image](assets/guide-achat/3.jpeg)
- 3 datakabler, der forbinder hashboards til kontrolpanelet.

![image](assets/guide-achat/4.jpeg)

- Strømforsyningen, der fungerer med 220V og kan tilsluttes som en almindelig husholdningsapparat.

![image](assets/guide-achat/5.jpeg)

- 2 120mm blæsere.

![image](assets/guide-achat/6.jpeg)

- Et han-C13-kabel.

![image](assets/guide-achat/7.jpeg)
Når du køber en brugt maskine, er det vigtigt at kontrollere, at alle dele er inkluderet og fungerer. Under udvekslingen bør du bede sælgeren om at tænde maskinen for at kontrollere dens korrekte funktion. Det er vigtigt at verificere, at enheden tændes korrekt, og derefter kontrollere internetforbindelsen ved at tilslutte et Ethernet-kabel og få adgang til Bitmain-login-interfacet via en webbrowser på det samme lokale netværk. Du kan finde denne IP-adresse ved at tilslutte din internetrouter-interface og kigge efter tilsluttede enheder. Denne adresse skal have følgende format: 192.168.x.x
![image](assets/guide-achat/8.gif)

Kontroller også, om standardlegitimationsoplysningerne virker (brugernavn: root, adgangskode: root). Hvis standardlegitimationsoplysningerne ikke virker, skal du nulstille maskinen.

![image](assets/guide-achat/9.jpeg)

Når du er tilsluttet, bør du kunne se status for hver hashboard på instrumentbrættet. Hvis miner er tilsluttet en pool, bør du se, at alle hashboards fungerer. Det er vigtigt at bemærke, at minere laver meget støj, hvilket er normalt. Sørg også for, at blæserne fungerer korrekt.

Du kan derefter fjerne den tidligere ejers mining-pool for at opsætte din egen senere. Hvis du ønsker det, kan du også inspicere hashboards ved at adskille maskinen. Denne proces er dog mere kompleks og kræver mere tid og nogle værktøjer. Hvis du ønsker at fortsætte med denne adskillelse, kan du henvise til næste del af denne vejledning, der detaljerer, hvordan du gør det. Det er vigtigt at bemærke, at minere opsamler meget støv og kræver regelmæssig vedligeholdelse. Du kan observere denne støvophobning og kvaliteten af vedligeholdelsen ved at adskille maskinen.
Efter at have gennemgået alle disse punkter kan du købe din maskine med stor tillid. Hvis du er i tvivl, kan du konsultere fællesskabet.

For at opsummere denne vejledning i en sætning: **"Don't trust, verify."**

[Du kan også henvende dig til fagfolk inden for renovering af minedriftsmaskiner, som vores partner 21energy. De tilbyder testede S9-maskiner, rengjort og med BraiiinOS+ software allerede installeret. Med tilknytningskoden "decouvre" får du 10% rabat på købet af en S9, samtidig med at du støtter Attakai-projektet.](https://21energy.io/en/produkt/bitmain-antminer-s9-bundle/)

## Guide til køb af hardwaremodifikationer til S9

![Introduktion til Attakaï: opvarmning med Bitcoin](https://www.youtube.com/watch?v=U_PLo59lp-g)
Hvis du ejer en Antminer S9, ved du sandsynligvis, hvor højlydt og klodset dette udstyr kan være. Det er dog muligt at omdanne det til en lydløs og forbundet varmelegeme ved at følge nogle få enkle trin. I denne sektion vil vi præsentere det nødvendige udstyr til at foretage disse ændringer.

Hvis du er en dygtig handyman og ønsker at omdanne en miner til en varmelegeme, er denne vejledning til dig. Vi vil gerne advare dig om, at ændringer foretaget på en elektronisk enhed kan medføre elektriske risici. Det er derfor vigtigt at tage alle nødvendige forholdsregler for at undgå skader eller skader.
1. Udskift blæserne
De originale blæsere på Antminer S9 er for støjende til at bruge din Antminer som en varmelegeme. Løsningen er at udskifte dem med mere støjsvage blæsere. Vores team har testet flere modeller fra mærket Noctua og har valgt Noctua NF-A14 iPPC-2000 PWM som det bedste kompromis. Sørg for at vælge 12V-versionen af blæserne. Denne 140mm blæser kan producere op til 1200W varme, samtidig med at den opretholder et teoretisk støjniveau på 31 dB. For at installere disse 140mm blæsere skal du bruge en adapter fra 140mm til 120mm, som du kan finde i DécouvreBitcoin-butikken. Vi vil også tilføje 140mm beskyttelsesgitre.

![image](assets/piece/1.jpeg)
![image](assets/piece/2.jpeg)
![image](assets/piece/3.jpeg)

Også strømforsyningsblæseren er ret støjende og skal udskiftes. Vi anbefaler Noctua NF-A6x25 PWM. Bemærk, at stikforbindelserne på Noctua-blæserne ikke er de samme som de originale, så du skal bruge en stikadapter til at forbinde dem. To vil være nok. Sørg igen for at vælge 12V-versionen af blæseren.

![image](assets/piece/4.jpeg)
![image](assets/piece/5.jpeg)

2. Tilføj en WIFI/Ethernet-bro

I stedet for at bruge et Ethernet-kabel kan du forbinde din Antminer via WIFI ved at tilføje en WIFI/Ethernet-bro. Vi har valgt vonets vap11g-300, fordi den nemt giver dig mulighed for at hente WIFI-signalet fra din internetboks og sende det til din Antminer via Ethernet uden at oprette et subnet. Hvis du har elektriske færdigheder, kan du forsyne den direkte med Antminerens strømforsyning uden behov for at tilføje en USB-oplader. Til dette har du brug for en hunstik med en diameter på 5,5 mm x 2,1 mm.

![image](assets/piece/6.jpeg)
![image](assets/piece/7.jpeg)

3. Valgfrit: Tilføj en smart stikprop
Hvis du vil tænde/slukke din Antminer fra din smartphone og overvåge dens strømforbrug, kan du tilføje en smart stikprop. Vi testede ANTELA-stikproppen i 16A-versionen, der er kompatibel med smartlife-appen. Denne smarte stikprop giver dig mulighed for at se dagligt og månedligt strømforbrug og tilsluttes direkte til din internetrouter via WiFi.
![image](assets/piece/8.jpeg)

Liste over udstyr og links

* 2X 3D adapterstykke 140mm til 120mm

* [2X NF-A14 iPPC-2000 PWM](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)

* [2X 140mm blæsergitre](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
* [Noctua NF-A6x25 PWM](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)
* [Elektrikerens sukker 2.5mm2](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
* [Vonets vap11g-300](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
* [Valgfri ANTELA smart stik](https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1)

# Attakai - Ændring af softwaren på en Antminer S9

## Opsætning af en Vonet WIFI/Ethernet Bridge

![Tilslut en Antminer S9 til dit Wifi-netværk](https://www.youtube.com/watch?v=y4oYURBaPqg)

For at forbinde din ASIC via WIFI skal du bruge en enhed kaldet en bridge. Denne enhed giver dig mulighed for at hente WIFI-signalet fra din router og sende det til en anden enhed via Ethernet.

Mange enheder kan udføre denne funktion, men vi anbefaler VONETS WiFi Bridge/Repeater på grund af dens bekvemmelighed.

Tilslut bridgen ved at forbinde den via USB.

Fra din computer skal du forbinde til VONETS_****** WIFI-netværket med adgangskoden 12345678.

![billede](assets/software/vonet1.png)

Log ind med brugernavnet "admin" og adgangskoden "admin".

![billede](assets/software/vonet2.png)

Vælg Wizard.

![billede](assets/software/vonet3.png)

Vælg det WIFI-netværk, du vil forbinde din miner til, og klik derefter på Næste.

BEMÆRK: Vonet-bridgen fungerer kun på 2,4 GHz-frekvensen. I dag tilbyder routere normalt to WIFI-netværk, et på 2,4 GHz og et på 5 GHz.
Indtast adgangskoden til dit WIFI-netværk i feltet "Kilde WIFI-hotspot-adgangskode". Hvis du ikke ønsker at bruge din Vonet-bro til at udvide dit WIFI-netværk, skal du markere afkrydsningsfeltet "Deaktiver hotspot". Ellers skal du lade det være umarkeret.

Klik derefter på Anvend.

Klik til sidst på genstart for at genstarte broen. Det vil tage et par minutter at genstarte.

Broen skal forbinde til din router og vises under navnet "[VONETS.COM](http://vonets.com/)". Hvis den stadig ikke forbindes efter et par minutter, kan det være nødvendigt at afbryde og tilslutte broen igen.

Når broen er forbundet, skal du tilslutte Ethernet-kablet fra broen til din ASIC og derefter tilslutte ASIC'en til strømstikket. Du kan derefter få adgang til ASIC-grænsefladen på samme måde som hvis den var direkte forbundet til din router via Ethernet.

## Nulstilling af en Antminer S9

Inden du installerer BraiinOS+, kan det være nødvendigt at nulstille din S9 til fabriksindstillingerne.
Denne metode kan anvendes mellem 2 minutter og 10 minutter efter start af miner.
2 minutter efter at have tændt mineren, skal du trykke på "Nulstil" -knappen i 5 sekunder og derefter give slip. Miner vil blive gendannet til fabriksindstillinger inden for 4 minutter og genstarte automatisk (der er ikke behov for at slukke den).

![image](assets/software/1.jpeg)

## Installation af BraiinsOS+ på en Antminer S9

![Installation af Braiins OS+ på din Antminer S9](https://www.youtube.com/watch?v=luqwlvzGsO4)

Den oprindelige software, der er installeret af Antminer på deres minedriftsmaskiner, er begrænset i funktionalitet. Derfor vil vi i denne vejledning installere en anden software kaldet BraiinsOS+. Det er en tredjepartssoftware udviklet af den allerførste Bitcoin-minedriftspool, der har flere funktioner og tillader f.eks. ændring af maskinens strøm.

Der er flere måder at installere Braiins OS+ på en ASIC. Du kan henvise til denne vejledning samt [officiel Braiins-dokumentation](https://academy.braiins.com/en/braiins-os/about/).

Her vil vi se, hvordan du nemt kan installere Braiins OS+ direkte på hukommelsen i din Antminer ved hjælp af BOS toolbox-softwaren, der erstatter det oprindelige operativsystem, gennem de detaljerede trin nedenfor.

1. Tænd din Antminer og tilslut den til din internetboks.
2. Download BOS toolbox til Windows / Linux.
3. Udpak den downloadede fil og åbn bos-toolbox.bat-filen. Vælg sprog, og efter et par øjeblikke vil du se dette vindue:

![image](assets/software/5.jpeg)

4. Bos toolbox vil tillade dig nemt at finde IP-adressen på din Antminer og installere BraiinsOS+. Hvis du allerede kender IP-adressen på din maskine, kan du springe til trin 8. Ellers gå til scan-fanen.

![image](assets/software/6.jpeg)

5. Normalt er IP-adresseområdet på hjemmenetværk mellem 192.168.1.1 og 192.168.1.255, så indtast "192.168.1.0/24" i IP-område-feltet. Hvis dit netværk er anderledes, skal du ændre disse adresser tilsvarende. Klik derefter på "Start".

6. Bemærk, hvis Antminer har en adgangskode, vil det ikke fungere med registreringen. Hvis det er tilfældet, er den enkleste løsning at foretage en nulstilling.

7. Du bør se alle Antminers på dit netværk vises her, og IP-adressen er 192.168.1.37.
Som en dygtig professionel oversætter er din primære opgave at præcist oversætte teknisk indhold fra engelsk til dit modersmål, dansk. Følg venligst følgende retningslinjer for at sikre en høj kvalitet i oversættelsen:

Originalsprog: Indholdet er oprindeligt på engelsk.
Indholdets karakter: Du vil støde på teknisk materiale, potentielt inklusive branchespecifik terminologi.
Links og tekniske ord: Oversæt ikke URL'er eller meget specifikke tekniske termer. Hvis du er i tvivl, behold den originale term.
Konsistent formatering: Bevar den samme markdown-layout og formatering som den originale tekst. Konsistensen i strukturen er afgørende.
YML-egenskaber: Hvis en linje begynder med en YML-egenskab (f.eks. 'name:', 'goal:', 'objectives:'), behold egenskabsnavnet på engelsk.
Kulturel kontekst: For kulturelle eller kontekstspecifikke referencer, der måske ikke kan oversættes direkte, omskriv for at bevare den tilsigtede betydning eller giv en kort forklaring.
Fokus bør være på at bevare integriteten af det tekniske indhold samtidig med at oversættelsen er forståelig og kontekstuelt korrekt på dansk. Dette er teksten, der skal oversættes:
![image](assets/software/7.jpeg)
8. Klik på "Tilbage" og derefter fanen "Installer", indtast den tidligere fundne IP-adresse og klik på "Start".

> Hvis installationen ikke virker, kan det være nødvendigt at foretage en nulstilling og prøve igen (se den tidligere sektion).
![image](assets/software/8.jpeg)
9. Efter et par øjeblikke vil din Antminer genstarte, og du vil kunne få adgang til Braiins OS+ grænsefladen på den angivne IP-adresse, her 192.168.1.37, direkte i adresselinjen i din browser. Standardbrugernavnet er "root", og der er ingen standardadgangskode.

## Konfigurer BraiinsOS+

![Konfigurer din Antminer S9 med Braiins OS+](https://www.youtube.com/watch?v=dK0t8M8kLYg)

Du skal oprette forbindelse til din ASIC ved hjælp af den lokale IP-adresse for din enhed på dit netværk gennem en browser.

Du kan finde IP-adressen for din maskine ved hjælp af BOS toolbox-værktøjet eller direkte på din routers webside.

Standardloginoplysningerne er de samme som for det oprindelige operativsystem.

- Brugernavn: root
- Adgangskode: (ingen)

Du vil derefter blive mødt af Brains OS+ Dashboard.

### Dashboard

![image](assets/software/14.jpeg)

På denne første side kan du observere realtidsydelsen af din maskine.

- Tre realtidsgrafer, der viser temperaturen, hashhastigheden og den generelle status for din maskine.
- Til højre, den faktiske hashhastighed, gennemsnitlig chip-temperatur, estimeret effektivitet i W/THs og strømforbrug.
- Nedenfor, blæserhastigheden som en procentdel af maksimal hastighed og antallet af omdrejninger pr. minut.

![image](assets/software/15.jpeg)

- Længere nede finder du en detaljeret visning af hver hashboard. Den gennemsnitlige temperatur for boardet og de chips, det indeholder, samt spænding og frekvens.
- Detaljer om aktive mining pools i Pools.
- Status for autotuning i Tuner Status.
- Til højre, detaljer om de data, der sendes til poolen.

### Konfiguration

![image](assets/software/16.jpeg)

### System

![image](assets/software/17.jpeg)

### Hurtige handlinger

![image](assets/software/18.jpeg)

# Attakai - Ventilatorændring

## Udskift strømforsyningsventilatoren

![Udskift ventilatorer for at reducere støj](https://www.youtube.com/watch?v=2CNGKZiveuc)

> ADVARSEL: Det er vigtigt at have installeret Braiins OS+ på din miner på forhånd eller anden software, der kan reducere ydeevnen på din maskine. Denne foranstaltning er afgørende, fordi vi vil installere mindre kraftfulde ventilatorer, der kan afgive mindre varme for at reducere støj.

![image](assets/hardware/cover.jpeg)

### Nødvendigt materiale

- 1 Noctua NF-A6x25 PWM-ventilator
- 2,5 mm2 elektrikertråd

> ADVARSEL: Først og fremmest, før du begynder, skal du sørge for at have afbrudt strømmen til din miner for at undgå enhver risiko for elektrisk stød.

![image](assets/hardware/1.jpeg)
Fjern først de 6 skruer på siden af kabinettet, der holder det lukket. Når skruerne er fjernet, åbner du forsigtigt kabinettet for at fjerne plastikbeskyttelsen, der dækker komponenterne.
![image](assets/hardware/2.jpeg)
![image](assets/hardware/3.jpeg)
Næste trin er at fjerne den originale blæser, og pas på ikke at beskadige de andre komponenter. For at gøre dette skal du fjerne skruerne, der holder den på plads, og forsigtigt fjerne det hvide lim omkring stikket. Det er vigtigt at være forsigtig for at undgå at beskadige ledningerne eller stikkene.
![image](assets/hardware/4.jpeg)

Når den originale blæser er fjernet, vil du bemærke, at stikkene på den nye Noctua-blæser ikke passer til dem på den originale blæser. Den nye blæser har faktisk 3 ledninger, herunder en gul ledning, der tillader hastighedsregulering. Dog vil denne ledning ikke blive brugt i dette specifikke tilfælde. For at tilslutte den nye blæser anbefales det derfor at bruge en speciel adapter. Det er dog vigtigt at bemærke, at denne adapter nogle gange kan være svær at finde.

![image](assets/hardware/5.jpeg)

Hvis du ikke har denne adapter, kan du stadig tilslutte den nye blæser ved hjælp af en elektrikersukker. For at gøre dette skal du klippe kablerne til den gamle og den nye blæser.

![image](assets/hardware/6.jpeg)
![image](assets/hardware/7.jpeg)

På den nye blæser skal du bruge en afbryderkniv og forsigtigt skære konturerne af hovedskeden ved 1 cm uden at skære skederne på kablerne nedenunder.

![image](assets/hardware/8.jpeg)

Derefter, ved at trække hovedskeden nedad, skal du skære skederne på de røde og sorte kabler på samme måde som før. Og skær den gule ledning lige.

![image](assets/hardware/9.jpeg)

På den gamle blæser er det mere delikat at skære hovedskeden uden at beskadige skederne på de røde og sorte ledninger. Til dette brugte vi en nål, som vi skubbede mellem hovedskeden og de røde og sorte ledninger.

![image](assets/hardware/10.jpeg)
![image](assets/hardware/11.jpeg)

Når de røde og sorte ledninger er blottet, skal du skære skederne forsigtigt for at undgå at beskadige de elektriske ledninger.

![image](assets/hardware/12.jpeg)

Derefter skal du forbinde kablerne med en sukker, den sorte ledning med den sorte og den røde ledning med den røde. Du kan også tilføje elektrisk tape.

![image](assets/hardware/13.jpeg)
![image](assets/hardware/14.jpeg)
Når forbindelsen er lavet, er det tid til at installere den nye Noctua-blæser med gitteret og de gamle skruer. De nye skruer i æsken vil blive genbrugt senere. Sørg for at placere den i den korrekte orientering. Du vil bemærke en pil på den ene side af blæseren, der angiver luftstrømmens retning. Det er vigtigt at placere blæseren, så pilen peger ind mod indersiden af kabinettet. Tilslut derefter blæseren igen.
![image](assets/hardware/15.jpeg)
![image](assets/hardware/16.jpeg)

> Valgfrit: Hvis du har kendskab til elektricitet, kan du direkte tilføje en kvindelig 5,5 mm jack-connector til 12V-strømudgangen, som direkte vil forsyne Vonet Wi-Fi-broen med strøm. Hvis du dog er usikker på dine elektriske færdigheder, er det bedst at bruge USB-tilslutningen med en oplader af typen til smartphones for at undgå enhver risiko for kortslutning eller elektrisk skade.

![image](assets/hardware/17.jpeg)

Når forbindelserne er lavet, skal du placere plastikdækslet over plastikdækslet og ikke indeni.

![image](assets/hardware/18.jpeg)

Endelig skal du sætte kabinetdækslet tilbage på plads og skrue de 6 skruer på siderne fast for at holde alt på plads. Og så er det, din strømforsyningskasse er nu udstyret med en ny blæser.

## Udskiftning af hovedblæserne
![Udskift fans for at reducere støj](https://www.youtube.com/watch?v=2CNGKZiveuc)
> ADVARSEL: Det er vigtigt at have installeret Braiins OS+ på din miner på forhånd eller anden software, der er i stand til at reducere ydeevnen på din maskine. Denne foranstaltning er afgørende, fordi vi vil installere mindre kraftfulde fans for at reducere støj, hvilket vil resultere i mindre varmeafledning.

![billede](assets/hardware/cover.jpeg)


### Nødvendigt udstyr

- 2 stykker 3D-adapter 140mm til 120mm
- 2 Noctua NF-A14 iPPC-2000 PWM fans
- 2 140mm fan-gittere

> ADVARSEL: Først og fremmest, inden du begynder, skal du sørge for at afbryde din miner for at undgå enhver risiko for elektrisk stød.

1. Først skal du afbryde fansene og skrue dem af.

![billede](assets/hardware/19.jpeg)

2. Stikkene på de nye Noctua-fans passer ikke til de originale, men fortvivl ikke! Tag din kniv og skær forsigtigt de små plastikfaner af, så stikkene passer perfekt på din miner.

![billede](assets/hardware/20.jpeg)
![billede](assets/hardware/21.jpeg)
3. Det er tid til at installere 3D-dele!
Fastgør dem på begge sider af mineren ved hjælp af skruerne, du fjernede fra fansene. Skru dem fast, indtil skruehovedet er i flugt med 3D-delen, og den sidder sikkert fast. Pas på ikke at stramme for meget, da du kan deformere delen, og en af skruerne kan røre en kondensator!

![billede](assets/hardware/22.jpeg)

4. Nu skal vi gå videre til fansene.

Fastgør dem til 3D-delene ved hjælp af skruerne, der følger med i æsken. Vær opmærksom på luftstrømmens retning, pilene på siderne af fansene vil angive retningen at følge. Gå fra Ethernet-port-siden til den anden side. Se fotoet nedenfor.

![billede](assets/hardware/23.jpeg)
![billede](assets/hardware/24.jpeg)
![billede](assets/hardware/25.jpeg)

5. Sidste trin: Tilslut fansene og fastgør gitterne ovenpå med de skruer, der ikke blev brugt i strømforsyningsventilatorens æske. Du har kun 4 af dem, men 2 pr. gitter i modsatte hjørner vil være nok. Hvis det er nødvendigt, kan du også finde lignende skruer i en hardwarebutik.

![billede](assets/hardware/26.jpeg)
![billede](assets/hardware/27.jpeg)

Mens du venter på at kunne tilbyde et mere stilfuldt kabinet til din nye varmelegeme, kan du fastgøre kabinettet og strømforsyningen med elektrikerens kabelbindere.

![billede](assets/hardware/28.jpeg)

Og som den sidste finish, tilslut Vonet-broen til Ethernet-porten og dens strømforsyning.

![billede](assets/hardware/29.jpeg)

Og så er du færdig, tillykke! Du har lige udskiftet hele den mekaniske del af din miner. Du bør nu høre meget mindre støj.

# Attakai - Konfiguration

## Tilslutning til en mining-pool

![Tilslutning til en mining-pool med en Antminer S9](https://www.youtube.com/watch?v=wM-dRog6mls&t=166s)
Man kan forestille sig en minedriftspool som en landbrugsforening. Landmændene samler deres produktion sammen for at reducere variationen i udbud og efterspørgsel og dermed opnå mere stabil indkomst for deres drift. En minedriftspool fungerer på samme måde, hvor den delte ressource er hashes. Faktisk tillader opdagelsen af en enkelt gyldig hash oprettelsen af en blok og vindingen af coinbase eller belønningen, i øjeblikket 6,25 BTC plus transaktionsgebyrerne inkluderet i blokken. Hvis du miner alene, vil du kun blive belønnet, når du finder en blok. Ved at konkurrere mod alle andre minearbejdere på planeten ville du have meget lille chance for at vinde denne lotteri, og du ville stadig skulle betale gebyrerne forbundet med brugen af din minearbejder uden nogen garanti for succes. Minedriftspools løser dette problem ved at samle beregningskraften fra adskillige (tusindvis) minearbejdere og dele deres belønninger baseret på procentdelen af deltagelse i poolens hashrate, når en blok findes. For at visualisere dine chancer for at mine en blok alene, kan du bruge dette værktøj. Ved at indtaste informationen for en Antminer S9 kan vi se, at chancerne for at finde en hash, der tillader oprettelsen af en blok, er 1 ud af 24.777.849 for hver blok eller 1 ud af 172.068 om dagen. I gennemsnit (med en konstant hashrate og sværhedsgrad) ville det tage 471 år at finde en blok.
Dog, da alt i Bitcoin er baseret på sandsynlighed, sker det sommetider, at solo minearbejdere bliver belønnet for at tage denne risiko: Solo Bitcoin Miner Løser Blok Med Hash Rate på Kun 10 TH/s, Slår Ekstremt Usandsynlige Odds - Decrypt

Hvis du kan lide at gamble, kan du prøve det, men vores guide vil ikke fokusere i den retning. I stedet vil vi koncentrere os om minedriftspoolen, der bedst passer til vores behov for at oprette et varmesystem.
Overvejelser, der skal tages i betragtning, når du vælger en minedriftspool, er poolens belønningsoperation, der kan variere, samt det minimumsbeløb, der skal være før man kan trække belønninger til en adresse. For eksempel tilbyder Braiins, som tilbyder den software, vi diskuterer her, også en pool. Denne pool har et belønningssystem kaldet "Score", der opmuntrer minearbejdere til at mine i lange perioder. Deltagelse inkluderer en oppetid faktor udtrykt som en "scoring hashrate". I vores tilfælde, hvor vi ønsker et varmesystem, der kun kan være tændt i få minutter, er dette ikke det ideelle belønningssystem. Vi foretrækker et belønningssystem, der giver os en lige belønning for hver deltagelse. Derudover er det mindste udbetalingsbeløb for Braiins Pool 100.000 sats og On-Chain. Så vi mister nogle sats i transaktionsgebyrer og en del af vores belønning kan være låst, hvis vi ikke miner nok i løbet af vinteren.

Belønningsmodellen, der interesserer os, er PPS, der står for "pay-per-share". Dette betyder, at minearbejderen vil modtage en belønning for hver gyldig deling. Der er også en variant af dette system, FPPS (Full Pay Per Share), som ikke kun deler coinbase belønningen, men også transaktionsgebyrerne inkluderet i blokken. De minedriftspools, vi anbefaler til tilslutning af din minedrift/varmesystem, er Linecoin Pool (FPPS) og Nicehash (PPS).

- Nicehash: Fordelen ved Nicehash er, at udbetaling kan ske ved hjælp af Lightning med minimale gebyrer. Derudover er det mindste udbetalingsbeløb 2000 sats. Ulempen er, at Nicehash bruger sin hashrate til den mest profitable blockchain, uden virkelig at give kontrol til brugeren, så det behøver ikke nødvendigvis bidrage til Bitcoin hashraten.
- Linecoin: Fordelen ved Linecoin er antallet af funktioner, der tilbydes, såsom et detaljeret kontrolpanel, evnen til at foretage udbetalinger med en Paynym (BIP 47) for bedre beskyttelse af privatlivet og integrationen af en Telegram-bot samt direkte konfigurerbare automatiseringer i mobilapplikationen. Denne pool miner kun Bitcoin-blokke, men det mindste beløb, der kan udbetales, forbliver højt på 100.000 sats. Vi vil undersøge grænsefladen for en af disse pools mere detaljeret i en kommende artikel.
For at konfigurere en pool i Braiins OS+ skal du oprette en konto i en af de pools, du vælger. Her vil vi tage eksemplet med Linecoin:

![billede](assets/software/19.jpeg)

Når din konto er oprettet, skal du klikke på "Tilslut til pool"

Kopier derefter Stratum-adressen og dit brugernavn:

![billede](assets/software/20.jpeg)

Du kan nu gå tilbage til Braiins OS+ grænsefladen for at indtaste disse legitimationsoplysninger. Til adgangskoden kan du lade feltet være tomt.

![billede](assets/software/21.jpeg)
## Optimering af ydeevnen for din Antminer S9
![Optimering af ydeevnen for din Antminer S9 med automatisk tilpasning](https://www.youtube.com/watch?v=yh8U9Ay1i-E&t=277s)

Både overclocking og autotuning indebærer justering af frekvenserne på hashing-bordene for at forbedre ASIC'ens ydeevne. Forskellen mellem de to ligger i kompleksiteten af disse frekvensindstillinger.

Overclocking er en simpel justering, der indebærer at øge frekvensen på hashing-bordene for at øge maskinens hashhastighed. Underclocking derimod indebærer at reducere clockfrekvensen for en integreret kreds under dens nominelle frekvens. Ved at reducere clockfrekvensen for en ASIC gennem underclocking reduceres også den varme, der genereres af hardwaren. Dette muliggør en reduktion i hastigheden på de fans, der kræves for at køle ASIC'en, da de ikke behøver at arbejde så hårdt for at opretholde en passende temperatur. Ved at reducere fanhastigheden reduceres også støjen genereret af ASIC'en. Dette kan være særligt nyttigt for brugere, der bruger ASIC'er derhjemme og ønsker at minimere støjforstyrrelser forårsaget af minedriftudstyr.

Braiins OS+ understøtter overclocking, underclocking af ASIC'er og autotuning. Det giver brugerne mulighed for fleksibelt at justere clockfrekvensen for deres hardware for at maksimere ydeevnen eller spare energi i henhold til deres præferencer.

### Optimering af ydeevnen for din Antminer S9 med automatisk tilpasning

Før 2018 havde minearbejdere to måder at opnå en fordel i deres aktivitet på: at finde elektricitet til en rimelig pris og købe mere effektivt hardware. Imidlertid blev der i 2018 opdaget en ny fremskridt inden for minedriftssoftware og firmware, kaldet AsicBoost. Denne teknik giver minearbejdere mulighed for at reducere deres omkostninger med ca. 13% ved at ændre firmwaren, der kører på deres enheder.
I dag er der en ny fremskridt inden for software og firmware til minedriftssektoren kaldet autotuning, som tilbyder en endnu større fordel end AsicBoost. ASIC'er består af mange små computerchips, der udfører hashing. Disse chips er lavet af silicium, det samme element der bredt anvendes i halvledere og andre mikroelektroniske komponenter. Den vigtige forståelse her er, at ikke alle siliciumchips er identiske, hver kan variere lidt i sine elektriske egenskaber. Hardwareproducenter er klar over dette og offentliggør ydeevnespecifikationerne for deres minedriftsmaskiner baseret på den nedre grænse for deres tolerancer. Med andre ord kender producenterne den frekvens, der fungerer bedst for gennemsnitlige chips, og de bruger denne frekvens ensartet for alle chips i maskinen.
Dette sætter en øvre grænse for hashhastigheden, som en maskine kan have. Autotuning er en proces, hvor algoritmer evaluerer de optimale frekvenser for chip-for-chip hashing i stedet for at behandle hele maskinen som en enkelt enhed. Dette betyder, at en chip af højere kvalitet, der kan udføre flere hashes pr. sekund, vil få en højere frekvens, og en chip af lavere kvalitet, der kan udføre relativt færre hashes, vil få en lavere frekvens. Chip-niveau autotuning er i bund og grund en måde at optimere ydeevnen af en ASIC gennem den software og firmware, der kører på den.
Det endelige resultat er en højere hashhastighed pr. watt elektricitet, hvilket betyder større fortjenstmargener for minearbejdere. Årsagen til, at maskiner ikke distribueres med denne type software, er, at maskinevarians er uønsket, da kunderne ønsker at vide præcis, hvad de får, så det er en dårlig idé for producenter at sælge et produkt, der ikke har ensartet og forudsigelig ydeevne fra den ene maskine til den anden. Derudover kræver chip-niveau autotuning betydelige udviklingsressourcer, da det er komplekst at implementere. Producenter bruger allerede mange ressourcer på at udvikle deres egne firmware. Der findes softwareløsninger, der tillader autotuning, såsom Braiins OS+. Udover at forbedre ASIC-ydeevnen med op til 20%.

## Styring af en Antminer S9 fra din smartphone

### Oprettelse af genveje på iOS

![Styring af en Antminer S9 med din smartphone](https://www.youtube.com/watch?v=OsKmdB2iw88&t=60s)
