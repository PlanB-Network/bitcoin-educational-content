---
name: Ontwikkelingsfilosofie Bitcoin
goal: Ontwikkel een diep filosofisch begrip van de ontwerpprincipes van Bitcoin.
objectives: 

  - Analyseer de fundamentele afwegingen en architectuurbeslissingen van Bitcoin
  - Leren hoe je voorgestelde wijzigingen en innovaties aan het Bitcoin protocol kunt evalueren
  - Meer dan een decennium aan Bitcoin ontwikkelingsgeschiedenis en gemeenschapsdebatten samenvatten
  - Kaders voor kritisch denken toepassen bij het beoordelen van nieuwe BIP's


---

# Diep duiken in de filosofie van Bitcoin ontwikkeling



De Bitcoin Ontwikkelfilosofie is een cursus voor Bitcoin ontwikkelaars die de basis van concepten en processen zoals Proof-of-Work, blokbouw en de transactionele levenscyclus al begrijpen, en die een hoger niveau willen bereiken door een dieper begrip te krijgen van de afwegingen en filosofie van Bitcoin.

Het moet nieuwe ontwikkelaars helpen om de belangrijkste lessen van meer dan een decennium Bitcoin ontwikkeling en publiek debat te verwerken, terwijl het hen een nuttige context biedt voor het evalueren van nieuwe ideeën (goede en slechte!).


### Wat kunt u verwachten?


Zoals hierboven vermeld, is dit een praktische gids voor Bitcoin ontwikkelaars. Bitcoin is echter een breed en complex onderwerp en we kunnen hier onmogelijk alle aspecten behandelen. Met deze cursus hopen we de noodzakelijke functies te bespreken om je ontwikkelactiviteit op te starten en je in staat te stellen het zelf verder te verkennen.


Er zijn veel mensen betrokken bij Bitcoin; omdat sommigen van hen tegengestelde meningen hebben, kun je hier bronnen vinden met tegenstrijdige ideeën. We proberen ons echter altijd te beperken tot het domein van de feiten, waar meningen er niet toe doen.


### Wie heeft dit geschreven?


Deze cursus is een bewerking van het gelijknamige boek met Kalle Rosenbaum als hoofdauteur en Linnéa Rosenbaum als co-auteur.

Het boek is geschreven en gefinancierd door [Chaincode Labs](https://learning.chaincode.com/), een ontwikkelingscentrum dat educatieve programma's verzorgt voor ontwikkelaars die willen leren over Bitcoin ontwikkeling.


+++



# Inleiding

<partId>58c48e9b-e285-4dc6-8952-6cc5140b1313</partId>


## Cursusoverzicht

<chapterId>28b7256b-9cb0-463e-a82d-d732be86c98c</chapterId>


Welkom bij deze cursus PHI 301 over Bitcoin ontwikkelingsfilosofie.


Bitcoin is meer dan alleen een cryptocurrency, het belichaamt een filosofische visie over decentralisatie, privacy, vertrouwen en veerkracht. Deze cursus is speciaal ontworpen voor ontwikkelaars die al bekend zijn met de technische fundamenten van Bitcoin en die nu hun inzicht willen verdiepen in de principes die ten grondslag liggen aan het ontwerp en bestuur van Bitcoin.


Tijdens deze cursus zul je duidelijkheid krijgen over de essentiële waarden en strategieën die de evolutie van Bitcoin al meer dan tien jaar leiden. Door deze thema's uit te diepen, ontwikkel je het kritische perspectief dat nodig is om toekomstige ontwikkelingen met vertrouwen te evalueren en eraan bij te dragen.


### De centrale waarden van Bitcoin


Wat maakt Bitcoin uniek? Dit gedeelte onthult de fundamentele waarden die ten grondslag liggen aan het ontwerp van Bitcoin. U verkent **decentralisatie**, de hoeksteen die ervoor zorgt dat geen enkele entiteit het netwerk controleert; **vertrouweloosheid**, de sleutel tot het wegnemen van de afhankelijkheid van derden; **privacy**, essentieel voor zowel individuele vrijheid als systeemintegriteit; en **definite Supply**, de gecodeerde garantie van schaarste die vorm geeft aan de economische identiteit van Bitcoin. Als je deze concepten beheerst, kun je de sterke en zwakke punten van Bitcoin volledig begrijpen.


### Bitcoin Bestuur


Het navigeren door het complexe bestuurslandschap van Bitcoin vereist meer dan technische expertise, het vereist inzicht in Bitcoin's unieke benadering van consensus en besluitvorming. In dit deel zul je de mechanismen en filosofieën achter kritieke processen zoals protocol upgrades, de noodzaak van tegenstrijdig denken, de kracht van open-source samenwerking, de voortdurende uitdagingen van schaalvergroting en de genuanceerde strategieën die nodig zijn wanneer dingen onvermijdelijk fout gaan, onder de loep nemen. Met deze kennis ben je niet alleen voorbereid om deel te nemen, maar ook om de toekomst van Bitcoin effectief en verantwoord vorm te geven.


Klaar om de volgende stap te zetten in jouw Bitcoin reis? Laten we beginnen!


***N.B.**: Als u tijdens de cursus onbekende termen met betrekking tot Bitcoin tegenkomt, raadpleeg dan de [woordenlijst](https://planb.network/resources/glossary) om definities te vinden.*




# Bitcoin centrale waarden

<partId>2d6c683b-54c8-5465-b2ca-4e96a6828834</partId>


## Decentralisatie

<chapterId>9397c84b-0038-5d0e-88d5-11767ce8182d</chapterId>




Dit analyseert wat decentralisatie is en waarom het essentieel is voor het functioneren van Bitcoin. We maken onderscheid tussen de

decentralisatie van miners en die van volledige nodes, en bespreken wat ze bijdragen aan de censuurbestendigheid, een van de meest centrale eigenschappen van Bitcoin.


De discussie verschuift dan naar het begrijpen van neutraliteit - of toestemmingsloosheid tegenover gebruikers, miners en ontwikkelaars - wat een noodzakelijke eigenschap is van elk gedecentraliseerd systeem. Tot slot bespreken we hoe Hard het kan zijn om een gedecentraliseerd systeem als Bitcoin te begrijpen, en presenteren we enkele mentale modellen die je kunnen helpen om het te begrijpen.


Een systeem zonder centraal controlepunt wordt *gedecentraliseerd* genoemd. Bitcoin is ontworpen om een centraal controlepunt te vermijden, of beter gezegd een *centraal punt van censuur*.


Decentralisatie is een middel om *censuurbestendigheid* te bereiken.


Er zijn twee belangrijke aspecten van decentralisatie in Bitcoin: Miner decentralisatie en Full node decentralisatie.


Miner decentralisatie verwijst naar het feit dat transactieverwerking niet wordt uitgevoerd of gecoördineerd door een centrale entiteit. Full node decentralisatie verwijst naar het feit dat validatie van de blokken, d.w.z. de gegevens die miners uitvoeren, aan de rand van het netwerk gebeurt, uiteindelijk door de gebruikers, en niet door een paar vertrouwde autoriteiten.


![](assets/decentralization-banner.webp)


### Miner decentralisatie



Er waren al pogingen geweest om digitale munteenheden te creëren vóór Bitcoin, maar de meeste mislukten door een gebrek aan bestuurlijke decentralisatie en weerstand tegen censuur.


Miner decentralisatie in Bitcoin betekent dat het *ordenen van transacties* niet wordt uitgevoerd door een enkele entiteit of vaste groep entiteiten. Het wordt collectief uitgevoerd door alle actoren die eraan willen deelnemen; dit miners' collectief is een dynamische verzameling gebruikers. Iedereen kan naar believen meedoen of weggaan. Deze eigenschap maakt Bitcoin censuurbestendig.


Als Bitcoin gecentraliseerd zou zijn, zou het kwetsbaar zijn voor degenen die het zouden willen censureren, zoals overheden. Het zou hetzelfde lot beschoren zijn als eerdere pogingen om digitaal geld te creëren. In de inleiding van [een paper] (https://www.blockstream.com/sidechains.pdf) getiteld "Enabling Blockchain Innovations with Pegged Sidechains", leggen de auteurs uit hoe vroege versies van digitaal geld niet waren uitgerust voor een vijandige omgeving (zie ook het hoofdstuk over vijandig denken in het volgende deel).


David Chaum introduceerde digitaal geld als een onderzoeksonderwerp in 1983, in een omgeving met een centrale server die vertrouwd wordt om Double-spending te voorkomen. Om het privacyrisico voor individuen van deze centrale vertrouwde partij te beperken en om fungibiliteit af te dwingen, introduceerde Chaum de blinde handtekening, die hij gebruikte om een cryptografische manier te bieden om het koppelen van de handtekeningen van de centrale server (die munten vertegenwoordigen) te voorkomen, terwijl de centrale server nog steeds dubbele uitgaven kon voorkomen.

De vereiste van een centrale server werd de achilleshiel van digitaal geld[Gri99]. Hoewel het mogelijk is om dit "single point of failure" te verdelen door de handtekening van de centrale server te vervangen door een drempelhandtekening van meerdere ondertekenaars, is het voor de controleerbaarheid belangrijk dat de ondertekenaars verschillend en identificeerbaar zijn. Dit maakt het systeem nog steeds kwetsbaar voor fouten, omdat elke ondertekenaar één voor één kan falen of kan worden gedwongen te falen.


Het werd duidelijk dat het gebruik van een centrale server om transacties te bestellen geen haalbare optie was vanwege het grote risico op censuur. Zelfs als men de centrale server zou vervangen door een federatie van een vaste set van n servers, waarvan er minstens m een bestelling moeten goedkeuren, zouden er nog steeds problemen zijn. Het probleem zou namelijk verschuiven naar een probleem waarbij gebruikers het eens moeten worden over deze set van n servers en over hoe ze kwaadwillende servers kunnen vervangen door goede zonder afhankelijk te zijn van een centrale autoriteit.


Laten we eens nadenken over wat er zou kunnen gebeuren als Bitcoin censureerbaar zou zijn. De censor zou gebruikers onder druk kunnen zetten om zich te identificeren, om aan te geven waar hun geld vandaan komt of wat ze ermee kopen, voordat ze hun transacties toelaten tot Blockchain.


Ook zou het gebrek aan censuurweerstand de censor in staat stellen gebruikers te dwingen nieuwe systeemregels aan te nemen. Ze zouden bijvoorbeeld een verandering kunnen opleggen waardoor ze het geld Supply kunnen opblazen en zichzelf zo verrijken. In zo'n geval zou een gebruiker die blokken controleert drie opties hebben om met de nieuwe regels om te gaan:



- Goedkeuren: Accepteer de wijzigingen en neem ze over in hun Full node.
- Weigeren: Weigeren om de wijzigingen over te nemen; dit laat de gebruiker achter met een systeem dat geen transacties meer verwerkt, omdat de blokkades van de censor nu ongeldig worden geacht door de Full node van de gebruiker.
- Verplaatsing: Stel een nieuw centraal controlepunt aan; alle gebruikers moeten uitzoeken hoe ze kunnen coördineren en vervolgens overeenstemming bereiken over het nieuwe centrale controlepunt.


Als ze daarin slagen, zullen dezelfde problemen in de toekomst waarschijnlijk weer de kop opsteken, aangezien het systeem net zo censureerbaar is gebleven als voorheen.


Geen van deze opties is gunstig voor de gebruiker.


Weerstand tegen censuur door decentralisatie is wat Bitcoin onderscheidt van andere geldsystemen, maar het is niet eenvoudig te realiseren vanwege het *Double-spending probleem*. Dit is het probleem om ervoor te zorgen dat niemand dezelfde munt twee keer kan uitgeven, een probleem waarvan veel mensen dachten dat het onmogelijk was om het op een gedecentraliseerde manier op te lossen. Satoshi Nakamoto schrijft in zijn [Bitcoin whitepaper](https://planb.network/bitcoin.pdf) over hoe het Double-spending probleem opgelost kan worden:


> In dit artikel stellen we een oplossing voor voor het Double-spending probleem met behulp van een peer-to-peer gedistribueerde Timestamp server om generate rekenkundig bewijs te leveren van de chronologische volgorde van transacties.


Hier gebruikt hij de vreemd klinkende uitdrukking "peer-to-peer gedistribueerde Timestamp server". Het sleutelwoord hier is *gedistribueerd*, wat in deze context betekent dat er geen centraal controlepunt is. Vervolgens legt Nakamoto uit hoe Proof-of-Work de oplossing is.

Toch legt niemand het beter uit dan

[Gregory Maxwell op Reddit](https://www.reddit.com/r/Bitcoin/comments/ddddfl/question_on_the_vulnerability_of_bitcoin/f2g9e7b/), waar hij reageert op iemand die voorstelt om het Hash vermogen van miners te beperken om mogelijke 51% aanvallen te voorkomen:


> Een gedecentraliseerd systeem zoals Bitcoin gebruikt openbare verkiezingen. Maar je kunt in een gedecentraliseerd systeem niet zomaar een stemming van 'mensen' houden, want dan zou een gecentraliseerde partij mensen moeten machtigen om te stemmen. In plaats daarvan gebruikt Bitcoin een stemming van rekenkracht, omdat het mogelijk is om rekenkracht te verifiëren zonder de hulp van een gecentraliseerde partij
derde partij.


Het bericht legt uit hoe het gedecentraliseerde Bitcoin netwerk tot een overeenkomst kan komen over het bestellen van transacties door Proof-of-Work te gebruiken.


Hij concludeert dan door te zeggen dat de 51% aanval niet bijzonder zorgwekkend is, vergeleken met mensen die niets geven om of niets begrijpen van de decentralisatie-eigenschappen van Bitcoin:


> Een veel groter risico voor Bitcoin is dat het publiek dat het gebruikt het niet begrijpt, er niet om geeft en de decentralisatie-eigenschappen die het waardevoller maken dan gecentraliseerde alternatieven niet beschermt.

De conclusie is belangrijk. Als mensen de decentralisatie van Bitcoin niet beschermen, wat een proxy is voor de censuurbestendigheid, kan Bitcoin het slachtoffer worden van centraliserende krachten, totdat het zo gecentraliseerd is dat censuur een ding wordt. Dan is de meeste, zo niet alle, waarde propositie verdwenen. Dit brengt ons bij de volgende paragraaf over de decentralisatie van Full node.


### Full node decentralisatie



In de paragrafen hierboven hebben we het vooral gehad over Miner decentralisatie en hoe centralisatie van miners censuur mogelijk kan maken. Maar er is ook een ander aspect van decentralisatie, namelijk *Full node decentralisatie*.


Het belang van Full node decentralisatie is gerelateerd aan de vertrouwensloosheid. Stel dat een gebruiker stopt met het runnen van zijn eigen Full node, bijvoorbeeld door een onbetaalbare stijging in de operationele kosten. In dat geval moeten ze op een andere manier communiceren met het Bitcoin netwerk, mogelijk door gebruik te maken van web wallets of lichtgewicht wallets, wat een bepaald niveau van vertrouwen vereist in de aanbieders van deze diensten.


De gebruiker gaat van het direct afdwingen van de netwerkconsensusregels naar het vertrouwen dat iemand anders dat zal doen. Stel nu dat de meeste gebruikers de handhaving van de consensus delegeren aan een vertrouwde entiteit. In dat geval kan het netwerk snel in een spiraal van centralisatie terechtkomen en kunnen de netwerkregels veranderd worden door samenzwerende kwaadwillende actoren.


In [a

Bitcoin Magazine artikel](https://bitcoinmagazine.com/technical/decentralist-perspective-Bitcoin-might-need-small-blocks-1442090446) interviewt Aaron van Wirdum Bitcoin ontwikkelaars over hun visie op decentralisatie en de risico's die gepaard gaan met het vergroten van de maximale blokgrootte van Bitcoin. Deze discussie was een Hot-onderwerp in het tijdperk 2014-2017, toen veel mensen discussieerden over het verhogen van de limiet voor de blokgrootte om meer transactiedoorvoer mogelijk te maken.


Een sterk argument tegen het verhogen van de blokgrootte is dat het de verificatiekosten verhoogt Als de verificatiekosten stijgen, zal dit sommige gebruikers ertoe aanzetten om hun volledige nodes niet meer te gebruiken. Dit zal er op zijn beurt toe leiden dat meer mensen het systeem niet op een Trustless manier kunnen gebruiken.


Pieter Wuille wordt geciteerd in het artikel, waarin hij de risico's van Full node centralisatie uitlegt:


> Als veel bedrijven een Full node draaien, betekent dit dat ze allemaal overtuigd moeten worden om een andere regelset te implementeren. Met andere woorden: de decentralisatie van de blokvalidatie geeft de consensusregels hun gewicht.
> Maar als het aantal Full node erg laag zou worden, bijvoorbeeld omdat iedereen dezelfde web-wallets, exchanges en SPV of mobiele wallets gebruikt, zou regulering een realiteit kunnen worden. En als autoriteiten de consensusregels kunnen reguleren, betekent dit dat ze alles kunnen veranderen wat Bitcoin Bitcoin maakt. Zelfs de limiet van 21 miljoen Bitcoin.

Alsjeblieft. Bitcoin gebruikers zouden hun eigen volledige nodes moeten beheren om regelgevers en grote bedrijven ervan te weerhouden om te proberen de consensusregels te veranderen.


### Neutraliteit



Bitcoin is neutraal, of toestemmingsvrij, zoals mensen het graag noemen. Dit betekent dat het Bitcoin niet uitmaakt wie je bent of waarvoor je het gebruikt.


Bitcoin is neutraal, wat goed is, en de enige manier waarop het kan werken. Als het bestuurd zou worden door een organisatie, zou het gewoon weer een virtueel object zijn en zou ik er geen interesse in hebben


Zolang je je aan de regels houdt, ben je vrij om het te gebruiken zoals je wilt, zonder iemand om toestemming te vragen. Dit omvat *Mining*, *transacties* in, en *het bouwen van protocollen en diensten* bovenop Bitcoin:



- Als *Mining* een toegestaan proces zou zijn, dan zouden we een centrale autoriteit nodig hebben om te selecteren wie er mag mijnen. Dit zou er waarschijnlijk toe leiden dat mijnwerkers legale contracten moeten tekenen waarin ze akkoord gaan met

om transacties te censureren volgens de grillen van de centrale autoriteit, wat in de eerste plaats het doel van Mining tenietdoet.



- Als mensen die *transacties* verrichten in Bitcoin persoonlijke informatie moeten geven, moeten verklaren waar hun transacties voor zijn, of op een andere manier moeten bewijzen dat ze het waard zijn om transacties te verrichten, dan hebben we ook een centraal autoriteitspunt nodig om gebruikers of transacties goed te keuren. Nogmaals, dit zou leiden tot censuur en uitsluiting.



- Als ontwikkelaars toestemming zouden moeten vragen om *protocollen* te bouwen bovenop Bitcoin, dan zouden alleen de protocollen ontwikkeld worden die toegestaan zijn door de centrale commissie die ontwikkelaars toestemming geeft. Dit zou door overheidsinterventie onvermijdelijk alle privacy beschermende protocollen en alle pogingen om decentralisatie te verbeteren uitsluiten.


Op alle niveaus zal het opleggen van beperkingen aan wie Bitcoin waarvoor mag gebruiken, Bitcoin zodanig schaden dat het niet meer voldoet aan zijn waardepropositie.


Pieter Wuille https://Bitcoin.stackexchange.com/a/92055/69518[beantwoordt een vraag over Stack Exchange] over hoe de Blockchain zich verhoudt tot normale databases. Hij legt uit hoe toestemmingsloosheid bereikt kan worden door het gebruik van Proof-of-Work in combinatie met economische prikkels.


Hij concludeert:


> Het gebruik van Trustless consensusalgoritmen zoals PoW voegt iets toe dat geen enkele andere constructie je geeft (permissievrije deelname, wat betekent dat er geen vaste groep deelnemers is die jouw veranderingen kan censureren), Het gebruik van Trustless consensusalgoritmen zoals PoW voegt iets toe nee, maar er zijn hoge kosten aan verbonden en de economische aannames maken het vrijwel alleen bruikbaar voor systemen die hun eigen cryptocurrency definiëren.
> Er is waarschijnlijk maar plaats in de wereld voor één of een paar van deze echt gebruikte exemplaren.

Hij legt uit dat, om toestemmingsloosheid te bereiken, het systeem hoogstwaarschijnlijk zijn eigen valuta nodig heeft, waardoor "de gebruikssituaties beperkt worden tot feitelijk alleen cryptocurrencies". Dit komt omdat toestemmingsvrije deelname, of Mining, economische prikkels vereist die in het systeem zelf zijn ingebouwd.


### Kijken naar decentralisatie



Een fascinerend aspect van Bitcoin is hoe Hard het is om te begrijpen dat niemand het controleert. Er zijn geen commissies of leidinggevenden in Bitcoin. Gregory Maxwell, opnieuw [op de Bitcoin subreddit](https://www.reddit.com/r/Bitcoin/comments/s82t2n/comment/htdte7w/?utm_source=share&utm_medium=web2x&context=3), vergelijkt dit op een intrigerende manier met de Engelse taal:


> Veel mensen hebben een Hard tijd om autonome systemen te begrijpen, er zijn er veel in hun leven, zoals de engelse taal, maar mensen nemen ze gewoon voor lief en zien ze niet eens als systemen. Ze zitten vast in een gecentraliseerde manier van denken waarbij alles wat ze als een 'ding' beschouwen een autoriteit heeft die het controleert.
>

> Bitcoin richt zich nergens op. Verschillende mensen die Bitcoin hebben geadopteerd hebben uit vrije wil gekozen om het te promoten, en hoe ze dat doen is hun eigen zaak. Autoriteit gefixeerde mensen kunnen deze activiteiten zien en geloven dat het een operatie is van de Bitcoin autoriteit, maar zo'n autoriteit bestaat niet.


De manier waarop Bitcoin werkt door decentralisatie lijkt op de buitengewone collectieve intelligentie die we bij veel diersoorten in de natuur aantreffen. Computerwetenschapper Radhika Nagpal spreekt in een [Ted talk] (https://www.ted.com/talks/radhika_nagpal_what_intelligent_machines_can_learn_from_a_school_of_fish) over het collectieve gedrag van visscholen en hoe wetenschappers dit proberen na te bootsen met robots.


> Ten tweede, en dat vind ik nog steeds het meest opmerkelijk, weten we dat er geen leiders zijn die toezicht houden op deze school vissen. In plaats daarvan ontstaat dit ongelooflijke collectieve gedrag puur uit de interacties van de ene vis met de andere.
> Op de een of andere manier zijn er deze interacties of omgangsregels tussen naburige vissen die ervoor zorgen dat het allemaal goed komt.

Ze wijst erop dat veel systemen, zowel natuurlijke als kunstmatige, zonder leiders kunnen werken en dat ook doen, en dat ze krachtig en veerkrachtig zijn. Elk individu heeft alleen interactie met zijn directe omgeving, maar samen vormen ze iets geweldigs.


![](assets/fishschool.webp)

*Visscholen hebben geen leiders*


Wat je ook denkt over Bitcoin, het gedecentraliseerde karakter maakt het moeilijk te controleren. Bitcoin bestaat en je kunt er niets aan doen. Het is iets om te bestuderen, niet om over te discussiëren.


### Conclusie over decentralisatie


We maken onderscheid tussen Full node decentralisatie en Mining decentralisatie. Mining decentralisatie is een middel om censuurbestendigheid te bereiken, terwijl Full node decentralisatie ervoor zorgt dat de consensusregels van het netwerk Hard kunnen veranderen zonder brede steun onder de gebruikers.


De gedecentraliseerde aard van Bitcoin zorgt voor neutraliteit tegenover ontwikkelaars, gebruikers en miners. Iedereen is vrij om deel te nemen zonder toestemming te vragen.


Gedecentraliseerde systemen kunnen Hard zijn om je hoofd in te wikkelen, maar er zijn enkele mentale modellen die kunnen helpen, bijvoorbeeld de Engelse taal of visscholen.


## Onbetrouwbaarheid

<chapterId>0506ba61-16a3-543c-95fa-3f3e2dd64121</chapterId>



![](assets/trustlessness-banner.webp)


Dit hoofdstuk ontleedt het concept van vertrouweloosheid, wat het betekent vanuit een computerwetenschappelijk perspectief en waarom Bitcoin Trustless moet zijn om zijn waardepropositie te behouden.

Daarna bespreken we wat het betekent om Bitcoin te gebruiken op een Trustless manier, en welke garanties een Full node je wel en niet kan geven.

In de laatste sectie kijken we naar de interactie in de echte wereld tussen Bitcoin en daadwerkelijke software of gebruikers, en de noodzaak om afwegingen te maken tussen gemak en onbetrouwbaarheid om überhaupt iets gedaan te krijgen.


Mensen zeggen vaak dingen als "Bitcoin is geweldig omdat het Trustless is".


Wat bedoelen ze met Trustless? Pieter Wuille legt deze veelgebruikte term uit op [Stack Exchange](https://Bitcoin.stackexchange.com/a/45674/69518):


> Het vertrouwen waar we het over hebben in "Trustless" is een abstracte technische term. Een gedistribueerd systeem wordt Trustless genoemd als het geen vertrouwde partijen nodig heeft om correct te functioneren.

In het kort verwijst het woord *Trustless* naar een eigenschap van het Bitcoin protocol waardoor het logisch kan functioneren zonder "vertrouwde partijen". Dit is anders dan het vertrouwen dat je onvermijdelijk moet stellen in de software of hardware die je gebruikt. Meer over dit laatste aspect van vertrouwen wordt verderop in dit hoofdstuk besproken.


In gecentraliseerde systemen vertrouwen we op de reputatie van een centrale speler om er zeker van te zijn dat deze de beveiliging op orde heeft of terugdraait in geval van problemen, en op het rechtssysteem om eventuele overtredingen te bestraffen. Deze vertrouwensvereisten zijn problematisch in pseudonieme gedecentraliseerde systemen - er is geen mogelijkheid tot verhaal dus er kan echt geen vertrouwen zijn. In de inleiding van [het Bitcoin whitepaper] (https://Bitcoin.org/Bitcoin.pdf) beschrijft Satoshi Nakamoto dit probleem:


> De handel op het internet is vrijwel uitsluitend afhankelijk geworden van financiële instellingen die als vertrouwde derde partij fungeren voor het verwerken van elektronische betalingen.
> Hoewel het systeem goed genoeg werkt voor de meeste transacties, heeft het nog steeds te lijden onder de inherente zwakheden van het op vertrouwen gebaseerde model.  Volledig onomkeerbare transacties zijn niet echt mogelijk, omdat financiële instellingen niet kunnen voorkomen dat geschillen worden bemiddeld. De kosten van bemiddeling verhogen de transactiekosten, waardoor de minimale praktische transactiegrootte wordt beperkt en de mogelijkheid voor kleine toevallige transacties wordt afgesneden, en er is een bredere kostenpost in het verlies van de mogelijkheid om niet-omkeerbare betalingen te doen voor niet-omkeerbare diensten.
> Met de mogelijkheid van omkering neemt de behoefte aan vertrouwen toe. Handelaren moeten op hun hoede zijn voor hun klanten en hen om meer informatie vragen dan ze anders nodig zouden hebben.  Een bepaald percentage fraude wordt als onvermijdelijk geaccepteerd. Deze kosten en betalingsonzekerheden kunnen persoonlijk worden vermeden door fysiek geld te gebruiken, maar er bestaat geen mechanisme om betalingen te verrichten via een communicatiekanaal zonder een vertrouwde partij

Het lijkt erop dat we geen gedecentraliseerd systeem kunnen hebben dat gebaseerd is op vertrouwen, en daarom is vertrouwensloosheid belangrijk in Bitcoin.


Om Bitcoin op een Trustless manier te gebruiken, moet je een volledig validerende Bitcoin node draaien. Alleen dan kun je verifiëren dat de blokken die je van anderen ontvangt, de consensusregels volgen; bijvoorbeeld, dat het uitgifteschema voor munten wordt nageleefd en dat er geen dubbele uitgaven plaatsvinden op de Blockchain. Als je geen Full node beheert, besteed je de verificatie van Bitcoin blokken uit aan iemand anders en vertrouw je erop dat zij je de waarheid vertellen, wat betekent dat je Bitcoin niet zonder vertrouwen gebruikt.


David Harding heeft [een artikel op de Bitcoin.org website](https://Bitcoin.org/en/Bitcoin-core/features/validation) geschreven waarin hij uitlegt hoe het draaien van een Full node - of het gebruik van Bitcoin zonder vertrouwen - je eigenlijk helpt:


> De Bitcoin valuta werkt alleen als mensen bitcoins in Exchange accepteren voor andere waardevolle dingen. Dat betekent dat het de mensen zijn die bitcoins accepteren die het waarde geven en die mogen beslissen hoe Bitcoin moet werken.
>

> Wanneer je bitcoins accepteert, heb je de macht om de regels van Bitcoin af te dwingen, zoals het voorkomen van inbeslagname van de bitcoins van een persoon zonder toegang tot de privésleutels van die persoon.
>

> Helaas besteden veel gebruikers hun handhavingsbevoegdheid uit. Dit laat de decentralisatie van Bitcoin in een verzwakte staat waar een handvol miners kan samenspannen met een handvol banken en gratis diensten om de regels van Bitcoin te veranderen voor al die niet-verifiërende gebruikers die hun macht hebben uitbesteed.
>

> In tegenstelling tot andere wallets, dwingt Bitcoin Core de regels af - dus als de miners en banken de regels veranderen voor hun niet-verifiërende gebruikers, zullen deze gebruikers niet in staat zijn om Bitcoin Core-gebruikers met volledige validatie, zoals jij, te betalen.


Hij zegt dat je met een Full node elk aspect van de Blockchain kunt verifiëren zonder iemand anders te vertrouwen, zodat je zeker weet dat de munten die je van anderen ontvangt echt zijn. Dit is geweldig, maar er is één belangrijk ding waar een Full node je niet mee kan helpen: het kan geen dubbele uitgaven voorkomen door chain rewrites:


> Merk op dat hoewel alle programma's - inclusief Bitcoin Core - kwetsbaar zijn voor chain rewrites, Bitcoin een verdedigingsmechanisme biedt: hoe meer bevestigingen uw transacties hebben, hoe veiliger u bent. Er is geen gekende gedecentraliseerde verdediging beter dan dat.

Hoe geavanceerd je software ook is, je moet er nog steeds op vertrouwen dat de blokken met je munten niet worden herschreven. Zoals Harding al aangaf, kun je echter een aantal bevestigingen afwachten, waarna je de kans op een herschrijving van de keten klein genoeg acht om acceptabel te zijn.


De stimulans om Bitcoin op een Trustless manier te gebruiken komt overeen met de behoefte van het systeem aan Full node decentralisatie. Hoe meer mensen hun eigen volledige nodes gebruiken, hoe meer Full node decentralisatie, en dus hoe sterker Bitcoin staat tegen kwaadwillige wijzigingen aan het protocol. Maar helaas, zoals uitgelegd in de Full node decentralisatie sectie, kiezen gebruikers vaak voor vertrouwde diensten als gevolg van de onvermijdelijke afweging tussen onbetrouwbaarheid en gemak.


De vertrouwensloosheid van Bitcoin is absoluut noodzakelijk vanuit een systeemperspectief. In 2018, Matt Corallo, [sprak over vertrouweloosheid](https://btctranscripts.com/baltic-honeybadger/2018/trustlessness-scalability-and-directions-in-security-models/) op de Baltic Honeybadger conferentie in Riga.


![video](https://youtu.be/66ZoGUAnY9s?t=4019)


De essentie van dat gesprek is dat je geen Trustless systemen kunt bouwen bovenop een vertrouwd systeem, maar wel vertrouwde systemen - bijvoorbeeld een bewarend Wallet - bovenop een Trustless systeem.



![width=50%](assets/trust.webp)


Een Trustless basis Layer maakt verschillende afwegingen op hogere niveaus mogelijk


Met dit beveiligingsmodel kan de systeemontwerper afwegingen maken

die voor hen zinvol zijn zonder die afwegingen aan anderen op te dringen.


### Vertrouw niet, controleer



Bitcoin werkt zonder vertrouwen, maar je moet nog steeds tot op zekere hoogte je software en hardware vertrouwen. Dat komt omdat je software of hardware misschien niet geprogrammeerd is om te doen wat er op de doos staat. Bijvoorbeeld:



- De CPU kan kwaadaardig zijn ontworpen om cryptografische bewerkingen met een privésleutel te detecteren en de gegevens van de privésleutel te lekken.
- De willekeurige nummergenerator van het besturingssysteem is mogelijk niet zo willekeurig als wordt beweerd.
- Bitcoin Core heeft misschien code ingesloten die jouw privésleutels naar een slechte speler stuurt.


Dus, naast het draaien van een Full node, moet je er ook voor zorgen dat je draait wat je van plan bent. Reddit gebruiker brianddk [schreef een artikel](https://www.reddit.com/r/Bitcoin/comments/smj1ep/bitcoin_v220_and_guix_stronger_defense_against/) over de verschillende vertrouwensniveaus waaruit je kunt kiezen bij het verifiëren van je software. In de sectie "De bouwers vertrouwen", heeft hij het over reproduceerbare builds:


> Reproduceerbare builds zijn een manier om software zo te ontwerpen dat veel ontwikkelaars uit de gemeenschap elk de software kunnen bouwen en er zeker van kunnen zijn dat het uiteindelijk gebouwde installatieprogramma identiek is aan wat andere ontwikkelaars produceren. Bij een zeer openbaar, reproduceerbaar project als Bitcoin hoeft geen enkele ontwikkelaar volledig vertrouwd te worden. Veel ontwikkelaars kunnen allemaal de build uitvoeren en bevestigen dat ze hetzelfde bestand produceerden als het bestand dat de originele bouwer digitaal ondertekende.

Het artikel definieert 5 niveaus van vertrouwen: vertrouwen op de site, de bouwers, de compiler, de kernel en de hardware.


Om het onderwerp van reproduceerbare builds verder uit te diepen, gaf Carl Dong [een presentatie over Guix](https://btctranscripts.com/breaking-Bitcoin/2019/Bitcoin-build-system/) waarin hij uitlegde waarom het vertrouwen op het besturingssysteem, bibliotheken en compilers problematisch kan zijn, en hoe dat opgelost kan worden met een systeem genaamd Guix, dat vandaag de dag gebruikt wordt door Bitcoin Core.


> Dus wat kunnen we doen aan het feit dat onze toolchain een aantal vertrouwde binaries kan hebben die reproduceerbaar kwaadaardig kunnen zijn? We moeten meer dan reproduceerbaar zijn. We moeten bootstrappable zijn. We kunnen niet zoveel binaire tools hebben die we moeten downloaden en vertrouwen van externe servers die beheerd worden door andere organisaties.
>

> We moeten weten hoe deze tools gebouwd zijn en precies weten hoe we het proces kunnen doorlopen om ze opnieuw te bouwen, bij voorkeur vanuit een veel kleinere verzameling vertrouwde binaries. We moeten onze vertrouwde set van binairen zoveel mogelijk beperken en een gemakkelijk controleerbaar pad hebben van die toolchains naar wat we gebruiken om Bitcoin te bouwen. Hierdoor kunnen we verificatie maximaliseren en vertrouwen minimaliseren.

Vervolgens legt hij uit hoe Guix ons toestaat om alleen een minimale binary van 357 bytes te vertrouwen die geverifieerd en volledig begrepen kan worden als je weet hoe je de instructies moet interpreteren. Dit is heel opmerkelijk: men verifieert dat de 357 bytes binary doet wat het moet doen, gebruikt het vervolgens om het volledige buildsysteem te bouwen vanaf de broncode en eindigt met een Bitcoin Core binary die een exacte kopie zou moeten zijn van de build van iemand anders.


Er is een mantra dat veel bitcoiners onderschrijven en dat veel van het bovenstaande goed samenvat:


> Vertrouw niet, maar controleer.

Dit verwijst naar de zin "[trust, but verify](https://en.wikipedia.org/wiki/Trust,_but_verify)" die de voormalige Amerikaanse president Ronald Reagan gebruikte in de context van nucleaire ontwapening. [Bitcoiners](https://twitter.com/Truthcoin/status/1491415722123153408?s=20&t=ZyROxZxlBppdRpuuzsiF5w) hebben het omgedraaid om de afwijzing van vertrouwen en het belang van een Full node te benadrukken.


Het is aan de gebruikers om te beslissen in welke mate ze de software die ze gebruiken en de Blockchain gegevens die ze ontvangen willen controleren. Zoals met zoveel andere dingen in Bitcoin, is er een afweging tussen gemak en betrouwbaarheid. Het is bijna altijd handiger om een Wallet te gebruiken dan Bitcoin Core op je eigen hardware te draaien. Echter, nu de Bitcoin software volwassen wordt en de gebruikersinterfaces verbeteren, zou het na verloop van tijd beter moeten worden in het ondersteunen van gebruikers die willen werken aan vertrouwelijkheid. Ook zouden gebruikers, naarmate ze meer kennis vergaren, in staat moeten zijn om geleidelijk het vertrouwen uit de vergelijking te halen.


Sommige gebruikers denken tegendraads en verifiëren de meeste aspecten van de software die ze draaien. Als gevolg daarvan beperken ze de behoefte aan vertrouwen tot het absolute minimum, omdat ze alleen hun computerhardware en besturingssysteem hoeven te vertrouwen. Hiermee helpen ze ook mensen die hun hardware niet zo grondig verifiëren door publiekelijk te waarschuwen voor problemen die ze zouden kunnen vinden. Een goed voorbeeld hiervan is een [gebeurtenis die plaatsvond in 2018](https://bitcoincore.org/en/2018/09/20/notice/), toen iemand een bug ontdekte waardoor miners een output twee keer konden uitgeven in dezelfde transactie:


> CVE-2018-17144, waarvoor een fix werd vrijgegeven op 18 september in Bitcoin Core versies 0.16.3 en 0.17.0rc4, bevat zowel een Denial of Service component als een kritieke kwetsbaarheid voor inflatie. Het werd oorspronkelijk gemeld aan verschillende ontwikkelaars die werken aan Bitcoin Core, evenals projecten die andere cryptocurrencies ondersteunen, waaronder ABC en Unlimited op 17 september als een Denial of Service bug alleen, maar we hebben snel vastgesteld dat het probleem ook een inflatie kwetsbaarheid was met dezelfde hoofdoorzaak en fix.

Hier meldde een anoniem persoon een probleem dat veel erger bleek dan de melder zich realiseerde. Dit benadrukt het feit dat mensen die de code verifiëren vaak veiligheidslekken melden in plaats van ze uit te buiten. Dit is gunstig voor degenen die niet alles zelf kunnen verifiëren.


Gebruikers moeten er echter niet op vertrouwen dat anderen hen veilig houden, maar zelf controleren waar en wanneer ze maar kunnen; zo blijft men zo soeverein mogelijk en bloeit Bitcoin op. Hoe meer ogen op de software, hoe kleiner de kans dat kwaadaardige code en veiligheidslekken er doorheen glippen.


### Conclusie over Vertrouweloosheid



Het Bitcoin protocol is Trustless omdat gebruikers ermee kunnen communiceren zonder een derde partij te vertrouwen. In de praktijk zijn de meeste mensen echter niet in staat om de volledige stack van software en hardware waarop ze Bitcoin draaien te verifiëren. Bekwame mensen die software of hardware verifiëren zijn in staat om andere, minder bekwame mensen te waarschuwen wanneer ze kwaadaardige code of bugs vinden.


Zonder vertrouwensloosheid kunnen we geen decentralisatie hebben, omdat vertrouwen onvermijdelijk een centraal punt van autoriteit met zich meebrengt. Je kunt een vertrouwd systeem bouwen bovenop een Trustless systeem, maar je kunt geen Trustless systeem bouwen bovenop een vertrouwd systeem.


## Privacy

<chapterId>1b960afe-0008-589b-b2f4-007d60d264c6</chapterId>



![](assets/privacy-banner.webp)


Dit hoofdstuk gaat over hoe je je financiële privégegevens voor jezelf kunt houden. Het legt uit waar privacy voor staat in de context van Bitcoin, waarom het belangrijk is, en wat het betekent om te zeggen dat Bitcoin pseudoniem is. Het gaat ook in op hoe privégegevens kunnen lekken, zowel On-Chain als off-chain.


Daarna gaat het over het feit dat bitcoins fungibel zouden moeten zijn, wat betekent dat ze inwisselbaar zijn voor andere bitcoins, en hoe fungibiliteit en privacy hand in hand gaan. Tot slot introduceert het hoofdstuk enkele maatregelen die u kunt nemen om uw privacy en die van anderen te verbeteren.


Bitcoin kan worden beschreven als een pseudoniem systeem, waarbij gebruikers meerdere pseudoniemen hebben in de vorm van publieke sleutels. Op het eerste gezicht lijkt dit een vrij goede manier om gebruikers te beschermen tegen identificatie, maar het is in feite heel gemakkelijk om onbedoeld financiële privégegevens te lekken.


### Wat betekent privacy?



Privacy kan verschillende dingen betekenen in verschillende contexten. In Bitcoin betekent het over het algemeen dat gebruikers hun financiële informatie niet aan anderen hoeven te onthullen, tenzij ze dat vrijwillig doen.


Er zijn veel manieren waarop u uw privégegevens naar anderen kunt lekken, met of zonder dat u het weet. Gegevens kunnen lekken via het openbare Blockchain of op een andere manier, bijvoorbeeld wanneer kwaadwillenden je internetcommunicatie onderscheppen.


### Waarom is privacy belangrijk?


Het lijkt misschien duidelijk waarom privacy belangrijk is in Bitcoin, maar er zijn enkele aspecten waar je misschien niet meteen aan denkt. [Op het Bitcoin Talk forum](https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908), geeft Gregory Maxwell ons een overzicht van een heleboel goede redenen waarom hij denkt dat privacy belangrijk is. Daaronder zijn vrije markt, veiligheid en menselijke waardigheid:


> Financiële privacy is een essentieel criterium voor de efficiënte werking van een vrije markt: als je een bedrijf runt, kun je niet effectief prijzen bepalen als je leveranciers en klanten tegen je wil al je transacties kunnen zien.
> U kunt niet effectief concurreren als uw concurrentie uw verkopen volgt.  Individueel gaat je informatieve hefboomwerking verloren in je privézaken als je geen privacy hebt over je rekeningen: als je je huisbaas betaalt in Bitcoin zonder voldoende privacy, ziet je huisbaas wanneer je loonsverhoging hebt gekregen en kan hij je om meer huur vragen.
>

> Financiële privacy is essentieel voor persoonlijke veiligheid: als dieven je uitgaven, inkomen en bezittingen kunnen zien, kunnen ze die informatie gebruiken om je aan te vallen en uit te buiten. Zonder privacy hebben kwaadwillenden meer mogelijkheden om je identiteit te stelen, je grote aankopen afhandig te maken of zich voor te doen als bedrijven waar je transacties mee doet... ze kunnen precies zien voor hoeveel ze je moeten proberen op te lichten.
>

> Financiële privacy is essentieel voor de menselijke waardigheid: niemand wil dat de snotterige barista in de coffeeshop of hun nieuwsgierige buren commentaar geven op hun inkomen of bestedingsgewoonten. Niemand wil dat hun babygekke schoonfamilie vraagt waarom ze anticonceptie (of seksspeeltjes) kopen. Je werkgever mag niet weten aan welke kerk je doneert. Alleen in een perfect verlichte, discriminatievrije wereld waar niemand ongepaste autoriteit heeft over iemand anders, kunnen we onze waardigheid behouden en onze wettige transacties vrij uitvoeren zonder zelfcensuur als we geen privacy hebben.

Maxwell gaat ook in op fungibiliteit, dat later in dit hoofdstuk wordt besproken, en op het feit dat privacy en wetshandhaving niet tegenstrijdig zijn.


### Pseudonimiteit


We zeiden hierboven al dat Bitcoin pseudoniem is en dat de pseudoniemen publieke sleutels zijn. In de media hoor je vaak dat Bitcoin anoniem is, wat niet klopt. Er is een onderscheid tussen anonimiteit en pseudonimiteit.


Andrew Poelstra [legt in een Bitcoin Stack Exchange post](https://Bitcoin.stackexchange.com/a/29473/69518) uit hoe anonimiteit eruit zou zien in transacties:


> Totale anonimiteit, in de zin dat wanneer je geld uitgeeft er geen spoor is van waar het vandaan komt of waar het naartoe gaat, is theoretisch mogelijk door gebruik te maken van de cryptografische techniek van zero-knowledge proofs.

Het verschil lijkt te zijn dat je bij een pseudonieme vorm van geld betalingen tussen pseudoniemen kunt traceren, terwijl je dat bij een anonieme vorm van geld niet kunt. Aangezien Bitcoin betalingen traceerbaar zijn tussen pseudoniemen, is het geen anoniem systeem.


We hebben ook gezegd dat de pseudoniemen openbare sleutels zijn, maar het zijn eigenlijk adressen die zijn afgeleid van openbare sleutels. Waarom gebruiken we adressen als pseudoniemen en niet iets anders, bijvoorbeeld een beschrijvende naam, zoals "watchme1984"? Dit is [goed uitgelegd] (https://Bitcoin.stackexchange.com/a/25175/69518) door gebruiker Tim S., ook op Bitcoin Stapel Exchange:


> Om Bitcoin's idee te laten werken, moet je munten hebben die alleen uitgegeven kunnen worden door de eigenaar van een bepaalde privésleutel. Dit betekent dat alles waarnaar je stuurt op de een of andere manier verbonden moet zijn met een publieke sleutel.
>

> Het gebruik van willekeurige pseudoniemen (bijv. gebruikersnamen) zou betekenen dat je het pseudoniem op de een of andere manier zou moeten koppelen aan een publieke sleutel om crypto met publieke/private sleutels mogelijk te maken. Dit zou de mogelijkheid wegnemen om offline veilig adressen/pseudoniemen aan te maken (bv. voordat iemand geld kan sturen naar de gebruikersnaam "tdumidu", zou je in de Blockchain moeten aankondigen dat "tdumidu" eigendom is van publieke sleutel "a1c...", en een vergoeding toevoegen zodat anderen een reden hebben om het aan te kondigen), anonimiteit verminderen (door je aan te moedigen om pseudoniemen te hergebruiken), en de grootte van de Blockchain nodeloos vergroten. Het zou ook een vals gevoel van veiligheid geven dat je stuurt naar wie je denkt dat je bent (als ik de naam "Linus Torvalds" aanneem voordat hij dat doet, dan is het van mij en zouden mensen geld kunnen sturen in de veronderstelling dat ze de maker van Linux betalen en niet mij).

Door gebruik te maken van adressen, of publieke sleutels, bereiken we belangrijke doelen, zoals het wegnemen van de noodzaak om een pseudoniem vooraf op de een of andere manier te registreren, het verminderen van de stimulans voor hergebruik van pseudoniemen, het vermijden van Blockchain bloat en het moeilijker maken om je als andere mensen voor te doen.


### Blockchain privacy



Blockchain privacy verwijst naar de informatie die u vrijgeeft door transacties op Blockchain. Het is van toepassing op alle transacties, zowel de transacties die u verzendt als de transacties die u ontvangt.


Satoshi Nakamoto denkt na over On-Chain privacy in sectie 7 van zijn [Bitcoin whitepaper] (https://Bitcoin.org/Bitcoin.pdf):


> Als extra firewall moet voor elke transactie een nieuw sleutelpaar worden gebruikt om te voorkomen dat ze aan een gemeenschappelijke eigenaar worden gekoppeld. Enige koppeling is nog steeds onvermijdelijk bij transacties met meerdere ingangen, die noodzakelijkerwijs onthullen dat hun ingangen eigendom waren van dezelfde eigenaar. Het risico is dat als de eigenaar van een sleutel wordt onthuld, het linken andere transacties onthult die van dezelfde eigenaar waren.

Het artikel vat de belangrijkste problemen van Blockchain privacy samen, namelijk Address hergebruik en Address clustering. Het eerste is zelfverklarend, het laatste verwijst naar de mogelijkheid om met enige mate van zekerheid te beslissen dat een set verschillende adressen aan dezelfde gebruiker toebehoort.


![](assets/address-reuse-clustering.webp)


Typische privacylekken op de Blockchain


Chris Belcher [schreef zeer gedetailleerd](https://en.Bitcoin.it/Privacy#Blockchain_attacks_on_privacy) over de verschillende soorten privacylekken die kunnen gebeuren op de Bitcoin Blockchain. We raden je aan tenminste de eerste paar subsecties onder "Blockchain aanvallen op privacy" te lezen


De conclusie is dat privacy in Bitcoin niet perfect is. Het vereist een aanzienlijke hoeveelheid werk om privé transacties te doen. De meeste mensen zijn niet bereid om zo ver te gaan voor privacy. Er lijkt een duidelijke afweging te zijn tussen privacy en bruikbaarheid.


Een ander belangrijk aspect van privacy is dat de maatregelen die je neemt om je eigen privacy te beschermen ook andere gebruikers beïnvloeden. Als je slordig bent met je eigen privacy, kunnen andere mensen ook een verminderde privacy ervaren. Gregory Maxwell legt dit heel duidelijk uit op dezelfde Bitcoin Talk discussie [waar we hierboven naar verwezen] (https://bitcointalk.org/index.php?topic=334316.msg3589252#msg3589252), en sluit af met een voorbeeld:


> Dit werkt in de praktijk ook... Een aardige whitehat hacker op IRC was aan het spelen met het kraken van hersenportefeuilles en raakte een zin met ~250 BTC erin.  We konden de eigenaar alleen al identificeren aan de hand van Address, omdat ze betaald waren door een Bitcoin service die adressen hergebruikte en hij kon ze ompraten om de contactinformatie van de gebruiker op te geven. Hij kreeg de gebruiker daadwerkelijk aan de telefoon, ze waren geschokt en in de war, maar dankbaar dat ze niet zonder geld zaten.  Een goede afloop dus. (Dit is lang niet het enige voorbeeld, maar wel een van de leukere).

In dit geval ging het allemaal goed dankzij de filantropisch ingestelde hacker, maar reken daar de volgende keer niet op.


### Niet-Blockchain privacy


Terwijl de Blockchain een beruchte bron van privacy lekken blijkt te zijn, zijn er genoeg andere lekken die geen gebruik maken van de Blockchain, sommige geniepiger dan andere. Deze variëren van key-loggers tot analyse van netwerkverkeer. Om meer te weten te komen over enkele van deze methodes, kun je nog eens kijken naar [Chris Belcher's stuk](https://en.Bitcoin.it/Privacy#Non-blockchain_attacks_on_privacy), in het bijzonder het gedeelte "Niet-Blockchain aanvallen op privacy".


Belcher noemt als een van de vele aanvallen de mogelijkheid dat iemand je internetverbinding afluistert, bijvoorbeeld je internetprovider:


> Als de aanvaller een transactie of blok uit jouw node ziet komen die nog niet eerder binnenkwam, dan kan hij met bijna zekerheid weten dat de transactie door jou werd gedaan of dat het blok door jou werd gemined. Omdat er internetverbindingen bij betrokken zijn, kan de tegenstander het IP Address koppelen aan de ontdekte Bitcoin informatie.

Tot de meest voor de hand liggende privacylekken behoren echter exchanges. Als gevolg van wetten, meestal aangeduid als KYC (Know Your Customer) en AML (Anti-Money Laundering), die gelden in de jurisdicties waarin ze actief zijn, moeten exchanges en gerelateerde bedrijven vaak persoonlijke gegevens over hun gebruikers verzamelen en grote databases opbouwen over welke gebruikers welke bitcoins bezitten. Deze databases zijn geweldige honeypots voor kwaadaardige overheden en criminelen die altijd op zoek zijn naar nieuwe slachtoffers. Er zijn echte markten voor dit soort gegevens, waar hackers

gegevens verkopen aan de hoogste bieder.


Tot overmaat van ramp hebben de bedrijven die deze databases beheren vaak weinig ervaring met het beschermen van financiële gegevens, in feite zijn veel van hen jonge start-ups, en we weten zeker dat er al verschillende lekken hebben plaatsgevonden. Enkele voorbeelden zijn

[Het Indiase MobiQwik](https://bitcoinmagazine.com/business/probably-the-largest-kyc-data-leak-in-history-demonstrates-the-importance-of-Bitcoin-privacy) en [HubSpot](https://bitcoinmagazine.com/business/hubspot-security-breach-leaks-Bitcoin-users-data).


Nogmaals, het beschermen van gegevens tegen dit brede scala aan aanvallen is Hard, en het is waarschijnlijk dat je niet volledig in staat zult zijn om dit te doen. Je zult moeten kiezen voor de afweging tussen gemak en privacy die voor jou het beste werkt.


### Zwambaarheid


Fungibiliteit, in de context van valuta, betekent dat een munt inwisselbaar is voor elke andere munt van dezelfde valuta. Dit grappige

dit woord werd eerder in het hoofdstuk al kort aangestipt.


In het artikel dat daar wordt besproken, [stelt] Gregory Maxwell (https://bitcointalk.org/index.php?topic=334316.msg3588908#msg3588908):


> Financiële privacy is een essentieel element voor fungibiliteit in Bitcoin: als je de ene munt zinvol kunt onderscheiden van de andere, dan is hun fungibiliteit zwak. Als onze fungibiliteit in de praktijk te zwak is, dan kunnen we niet gedecentraliseerd zijn: als een belangrijk iemand een lijst van gestolen munten aankondigt waarvan hij geen munten accepteert, dan moet je zorgvuldig de munten die je accepteert vergelijken met die lijst en de munten die niet voldoen terugsturen.  Iedereen zit vast aan het controleren van zwarte lijsten die zijn uitgegeven door verschillende autoriteiten, want in die wereld willen we allemaal niet opgescheept zitten met slechte munten. Dit voegt wrijving en transactiekosten toe en maakt Bitcoin minder waardevol als geld.

Hier spreekt hij over de gevaren die voortkomen uit een gebrek aan fungibiliteit. Stel dat je een UTXO hebt. De geschiedenis van die UTXO kan normaal gezien verschillende hops terug gevolgd worden, uitwaaierend naar massa's vorige outputs. Als één van die outputs betrokken was bij illegale, ongewenste of verdachte activiteiten, dan zouden sommige potentiële ontvangers van jouw munt deze kunnen verwerpen. Als u denkt dat uw begunstigden uw munten zullen verifiëren aan de hand van een gecentraliseerde witte of zwarte lijst, dan zou u voor de zekerheid ook de munten die u ontvangt kunnen gaan controleren. Het resultaat is dat slechte fungibiliteit nog slechtere fungibiliteit zal versterken.


Adam Back en Matt Corallo [gaven een presentatie over fungibiliteit](https://btctranscripts.com/scalingbitcoin/milan-2016/fungibility-overview/) op Scaling Bitcoin in Milaan in 2016. Zij dachten in dezelfde richting:


> Je hebt fungibiliteit nodig om Bitcoin te laten functioneren. Als je munten ontvangt en ze niet kunt uitgeven, ga je twijfelen of je ze wel kunt uitgeven. Als er twijfels zijn over de munten die je ontvangt, dan gaan mensen naar taint services om te controleren of "deze munten gezegend zijn" en dan gaan mensen weigeren om te handelen. Dit verandert Bitcoin van een gedecentraliseerd systeem zonder toestemming in een gecentraliseerd systeem met toestemming waarbij je een "IOU" hebt van de leveranciers van de zwarte lijst.

Het lijkt erop dat privacy en fungibiliteit hand in hand gaan. De fungibiliteit zal verzwakken als de privacy zwak is, bijvoorbeeld omdat munten van ongewenste personen op een zwarte lijst kunnen komen te staan. Op dezelfde manier wordt privacy verzwakt als de fungibiliteit zwak is: als er een zwarte lijst is, moet je de aanbieders van de zwarte lijst vragen welke munten te accepteren, waardoor je mogelijk je IP Address, e-mail Address en andere gevoelige informatie onthult. Deze twee functies zijn zo met elkaar verweven dat het Hard is om over een van beide afzonderlijk te praten.


### Privacymaatregelen



Er zijn verschillende technieken ontwikkeld om mensen te helpen zichzelf te beschermen tegen privacylekken. Een van de meest voor de hand liggende is, zoals Nakamoto eerder opmerkte, het gebruik van unieke

adressen voor elke transactie, maar er bestaan nog verschillende andere. We gaan je niet leren hoe je een privacy ninja wordt. Bitcoin Q+A heeft echter een [snel overzicht van privacyverbeterende technologieën](https://bitcoiner.guide/privacytips/), enigszins geordend op hoe Hard ze te implementeren. Als je het leest, zul je merken dat Bitcoin privacy vaak te maken heeft met dingen buiten Bitcoin. Je moet bijvoorbeeld niet opscheppen over je bitcoins en je moet Tor en VPN gebruiken.


De post somt ook enkele maatregelen op die rechtstreeks verband houden met Bitcoin:


- Full node: Als je geen eigen Full node gebruikt, lek je veel informatie over je Wallet naar servers op het internet. Het gebruik van een Full node is een goede eerste stap.
- Lightning Network: Er bestaan verschillende protocollen bovenop Bitcoin, bijvoorbeeld Lightning Network en Liquid Sidechain van Blockstream.
- CoinJoin: Een manier voor meerdere mensen om hun transacties samen te voegen, waardoor het moeilijker wordt om ketenanalyses te doen.


In [een toespraak](https://btctranscripts.com/breaking-Bitcoin/2019/breaking-Bitcoin-privacy/) op de Breaking Bitcoin conferentie gaf Chris Belcher een interessant praktisch voorbeeld van hoe privacy is verbeterd:


> Ze waren een Bitcoin casino. Online gokken is niet toegestaan in de VS. Van alle klanten van Coinbase die rechtstreeks geld stortten naar Bustabit zouden de rekeningen worden afgesloten omdat Coinbase hierop controleerde. Bustabit deed een paar dingen. Ze hebben iets gedaan dat wisselgeldvermijding heet, waarbij je doorloopt en kijkt of je een transactie kunt construeren die geen wisselgelduitvoer heeft. Dit bespaart Miner kosten en belemmert ook de analyse.
>

> Ook importeerden ze hun veelgebruikte hergebruikte stortingsadressen in joinmarket. Op dit punt werden klanten van coinbase.com nooit gebanned. Het lijkt erop dat de surveillancedienst van Coinbase de analyse hierna niet meer kon uitvoeren, dus het is mogelijk om deze algoritmes te breken.

Hij noemde dit voorbeeld ook, onder andere, op de [Privacy pagina](https://en.Bitcoin.it/Privacy) op de Bitcoin wiki.


Merk op hoe betere privacy bereikt kan worden door systemen bovenop Bitcoin te bouwen, zoals het geval is bij Lightning Network:


![image](assets/privacy.webp)


Lagen bovenop Bitcoin kunnen privacy toevoegen


We merkten in de vorige chaper op dat de behoefte aan vertrouwen alleen maar kan toenemen met lagen erbovenop, maar dat lijkt niet het geval te zijn voor privacy, die willekeurig kan worden verbeterd of verslechterd met lagen erbovenop. Hoe komt dat? Elke Layer bovenop Bitcoin, zoals uitgelegd in de paragraaf Gelaagd Schalen in het toekomstige hoofdstuk Schalen, moet af en toe On-Chain transacties gebruiken, anders zou het niet "bovenop Bitcoin" liggen. Privacyverhogende lagen proberen over het algemeen de basis Layer zo min mogelijk te gebruiken om de hoeveelheid informatie die onthuld wordt te minimaliseren.


Het bovenstaande zijn enigszins technische manieren om je privacy te verbeteren. Maar er zijn andere manieren. Aan het begin van dit hoofdstuk zeiden we dat Bitcoin een pseudoniem systeem is. Dit betekent dat gebruikers in Bitcoin niet bekend zijn bij hun echte naam of andere persoonlijke gegevens, maar bij hun publieke sleutel. Een publieke sleutel is een pseudoniem voor een gebruiker, en een gebruiker kan meerdere pseudoniemen hebben. In een ideale wereld is je persoonlijke identiteit losgekoppeld van je Bitcoin pseudoniemen. Helaas, door de privacyproblemen die in dit hoofdstuk beschreven worden, wordt deze ontkoppeling na verloop van tijd minder.


Om de risico's van het onthullen van je persoonlijke gegevens te beperken, moet je ze in de eerste plaats niet geven en ze ook niet aan gecentraliseerde diensten geven, die grote databases opbouwen die kunnen lekken. Een artikel van Bitcoin Q+A [geeft uitleg over KYC](https://bitcoiner.guide/nokyconly/) en de gevaren die daaruit voortvloeien. Het stelt ook enkele stappen voor die je kunt nemen om je situatie te verbeteren:


> Gelukkig zijn er enkele opties om Bitcoin te kopen zonder KYC. Dit zijn allemaal P2P (peer to peer) exchanges waar je direct handelt met een ander individu en niet met een gecentraliseerde derde partij. Helaas verkopen sommige naast Bitcoin ook andere munten, dus wees voorzichtig.

Het artikel suggereert dat je het gebruik van exchanges die KYC/AML vereisen vermijdt en in plaats daarvan privé handelt, of gedecentraliseerde exchanges gebruikt zoals [bisq](https://bisq.network/).


https://planb.network/en/tutorials/exchange/peer-to-peer/bisq-fe244bfa-dcc4-4522-8ec7-92223373ed04

Raadpleeg voor meer informatie over tegenmaatregelen het eerder genoemde [wiki-artikel over privacy](https://en.Bitcoin.it/wiki/Privacy#Methods_for_improving_privacy_.28non-Blockchain.29), te beginnen bij "Methoden voor het verbeteren van privacy (niet-Blockchain)".


### Conclusie over privacy



Privacy is erg belangrijk, maar Hard om te bereiken. Er bestaat geen wondermiddel voor privacy.


Om fatsoenlijke privacy te krijgen in Bitcoin, moet je actieve maatregelen nemen, waarvan sommige duur en tijdrovend zijn.


## Eindig Supply

<chapterId>af125ba2-ef98-5905-8895-41a538fe5ea5</chapterId>



![](assets/finitesupply-banner.webp)


Dit hoofdstuk gaat over de Bitcoin Supply limiet van 21 miljoen BTC, of hoeveel is het eigenlijk? We bespreken hoe deze limiet wordt afgedwongen en wat je kunt doen om te controleren of hij wordt gerespecteerd. Bovendien nemen we een kijkje in de kristallen bol en bespreken we de dynamiek die zal ontstaan wanneer Block reward verandert van subsidie- naar fee-gebaseerd.


De bekende eindige Supply van 21 miljoen BTC wordt beschouwd als een fundamentele eigenschap van Bitcoin. Maar is het echt in steen gebeiteld?


Laten we beginnen met te kijken naar wat de huidige consensusregels zeggen over de Supply van Bitcoin, en hoeveel daarvan daadwerkelijk bruikbaar zal zijn. Pieter Wuille schreef hierover een stuk [over Stack Exchange](https://Bitcoin.stackexchange.com/a/38998/69518), waarin hij telde hoeveel bitcoins er zouden zijn als alle munten gemined waren:


> Als je al deze getallen bij elkaar optelt, krijg je 20999999.9769 BTC.

Maar door een aantal redenen -- zoals vroege problemen met coinbase transacties, miners die onbedoeld minder claimen dan toegestaan en verlies van privésleutels -- zal die bovengrens nooit bereikt worden. Wuille concludeert:


> Dit laat ons met 20999817.31308491 BTC (rekening houdend met alles tot en met blok 528333)

Er zijn echter verschillende portemonnees verloren gegaan of gestolen, transacties zijn naar de verkeerde Address gestuurd, mensen vergaten dat ze Bitcoin bezaten. De totalen hiervan kunnen in de miljoenen lopen. Mensen hebben geprobeerd bekende verliezen op te tellen [hier] (https://bitcointalk.org/index.php?topic=7253.0).


Dan blijft over: ??? BTC.


We kunnen er dus zeker van zijn dat de Bitcoin Supply maximaal 20999817.31308491 BTC zal zijn. Verloren of oncontroleerbaar verbrande munten zullen dit getal lager maken, maar we weten niet met hoeveel. Het interessante is dat het er niet echt toe doet, of beter nog, het doet er wel toe op een positieve manier voor Bitcoin houders,

[zoals uitgelegd] (https://bitcointalk.org/index.php?topic=198.msg1647#msg1647) door Satoshi Nakamoto:


> Verloren munten maken de munten van alle anderen alleen maar iets meer waard.  Zie het als een donatie aan iedereen.

Het eindige Supply zal krimpen en dit zou, althans in theorie, prijsdeflatie moeten veroorzaken.


Belangrijker dan het exacte aantal munten in omloop is de manier waarop de Supply limiet wordt afgedwongen zonder centrale autoriteit. Alias chytrik zegt het goed op [Stack Exchange](https://Bitcoin.stackexchange.com/a/106830/69518):


> Het antwoord is dus dat je er niet op hoeft te vertrouwen dat iemand de Supply niet verhoogt. Je hoeft alleen maar een code te draaien die controleert of dat niet zo is.

Zelfs als sommige volledige knooppunten zich naar de duistere kant keren en beslissen om blokken met munttransacties met een hogere waarde te aanvaarden, zullen alle overblijvende volledige knooppunten hen gewoon negeren en doorgaan met hun gewone gang van zaken. Sommige volledige nodes kunnen, opzettelijk of onopzettelijk, kwaadaardige software draaien, maar het collectief zal de Blockchain robuust beveiligen. Kortom, je kunt ervoor kiezen het systeem te vertrouwen zonder iemand te hoeven vertrouwen.


### Bloksubsidie en transactiekosten



Een Block reward bestaat uit de bloksubsidie plus transactiekosten. De Block reward moet de beveiligingskosten van Bitcoin dekken. We kunnen met zekerheid zeggen dat onder de huidige omstandigheden met betrekking tot bloksubsidie, transactiekosten, Bitcoin prijs, Mempool grootte, Hash macht, mate van decentralisatie etc., de stimulans voor elke speler om zich aan de regels te houden groot genoeg is om een veilig monetair systeem te behouden.


Wat gebeurt er als de bloksubsidie bijna nul is? Laten we, om het eenvoudig te houden, aannemen dat het eigenlijk gelijk is aan nul. Op dat moment worden de beveiligingskosten van het systeem alleen gedekt door transactiekosten. Wat de toekomst ons brengt als dit gebeurt, kunnen we niet weten. De onzekerheidsfactoren zijn talrijk en we zijn aangewezen op speculaties. Paul Sztorc's bijdrage aan het onderwerp [in zijn Truthcoin blog] (https://www.truthcoin.info/blog/security-budget/) is bijvoorbeeld vooral speculatie, maar hij heeft ten minste één solide punt (merk op dat M2, zoals bedoeld door Sztorc, een meting is van fiatgeld Supply):


> Hoewel de twee worden gemengd in hetzelfde "veiligheidsbudget", zijn de bloksubsidie en de txn-vergoedingen volkomen en totaal verschillend. Ze verschillen net zo veel van elkaar als "de totale winst van VISA in 2017" van de "totale toename van M2 in 2017".

Vandaag zijn het de houders die betalen voor de veiligheid (via monetaire inflatie). Morgen is het de beurt aan de spenders om deze last op de een of andere manier te dragen, zoals hieronder wordt geïllustreerd.


![image](assets/finitesupply.webp)


Naarmate de tijd verstrijkt, zal het dragen van de beveiligingskosten verschuiven van houders naar spenders


Wanneer transactievergoedingen de belangrijkste motivatie zijn voor Mining, verschuiven de stimulansen. In het bijzonder, als de Mempool van een Miner niet genoeg transactievergoedingen bevat, kan het winstgevender worden voor die Miner om de geschiedenis van Bitcoin te herschrijven in plaats van deze uit te breiden. Bitcoin Optech heeft een specifieke [sectie over dit gedrag] (https://bitcoinops.org/en/topics/fee-sniping/), genaamd *fee sniping*, geschreven door David Harding:


> Fee sniping is een probleem dat kan optreden als de subsidie van Bitcoin blijft afnemen en transactiekosten de blokbeloningen van Bitcoin beginnen te domineren. Als transactiekosten het enige zijn dat telt, dan heeft een Miner met `x` procent van het Hash tarief een `x` procent kans op Mining het volgende blok, dus de verwachte waarde voor hen van eerlijk Mining is `x` procent van de [best feerate set van transacties](https://bitcoinops.org/en/newsletters/2021/06/02/#candidate-set-based-csb-block-template-construction) in hun Mempool.
>

> Als alternatief kan een Miner oneerlijk proberen om het vorige blok opnieuw te delven plus een geheel nieuw blok om de keten uit te breiden. Dit gedrag wordt fee sniping genoemd, en de kans dat de oneerlijke Miner hierin slaagt als elke andere Miner eerlijk is, is `(x/(1-x))^2`. Ook al heeft fee sniping over het algemeen een lagere kans van slagen dan eerlijke Mining, toch kan het proberen van oneerlijke Mining de meer winstgevende keuze zijn als transacties in het vorige blok aanzienlijk hogere feerates betaalden dan de transacties die momenteel in de Mempool zitten-een kleine kans op een groot bedrag kan meer waard zijn dan een grote kans op een klein bedrag.

Een natte deken over onze hoop voor de toekomst werpt het feit dat als miners beginnen met fee sniping, dit anderen zal stimuleren om hetzelfde te doen, waardoor er nog minder eerlijke miners overblijven. Dit zou de algemene veiligheid van Bitcoin ernstig kunnen schaden. Harding somt verder een aantal tegenmaatregelen op die genomen kunnen worden, zoals het vertrouwen op vergrendelingen van transactietijden om te beperken waar in Blockchain de transactie kan verschijnen.


Dus, aangezien de consensus over eindige Supply blijft bestaan, zal de bloksubsidie - dankzij [BIP42](https://github.com/Bitcoin/bips/blob/master/bip-0042.mediawiki) die een zeer langdurige inflatiebug repareerde - rond het jaar 2140 op nul uitkomen. Zullen de transactiekosten daarna genoeg zijn om het netwerk veilig te stellen?


Het is onmogelijk te zeggen, maar we weten wel een paar dingen:


- Een eeuw is een *lange* tijd vanuit het Bitcoin perspectief. Als het er nog is, is het waarschijnlijk enorm geëvolueerd.
- Als een overweldigende economische meerderheid het nodig vindt om de regels te veranderen en bijvoorbeeld een eeuwigdurende jaarlijkse monetaire inflatie van 0,1% of 1% in te voeren, dan zal de Supply van Bitcoin niet langer eindig zijn.
- Met nul bloksubsidie en een leeg of bijna leeg Mempool kunnen de dingen wankel worden door het sluipen van vergoedingen.


Omdat de overgang naar een fee-only Block reward zo ver in de toekomst ligt, is het misschien verstandig om niet te snel conclusies te trekken en te proberen de potentiële problemen op te lossen nu het nog kan. Peter Todd denkt bijvoorbeeld dat er een reëel risico bestaat dat het veiligheidsbudget van Bitcoin in de toekomst niet genoeg zal zijn, en pleit daarom voor een kleine eeuwigdurende inflatie in Bitcoin. Hij denkt echter ook dat het geen goed idee is om een dergelijke kwestie op dit moment te bespreken, zoals [hij zei in de What Bitcoin podcast] (https://www.whatbitcoindid.com/podcast/peter-todd-on-the-essence-of-Bitcoin):


> Maar dat is een risico van 10, 20 jaar in de toekomst. Dat is erg lang. En wie weet er tegen die tijd wat de risico's zijn?

Misschien kunnen we Bitcoin zien als iets organisch. Stel je een kleine, langzaam groeiende eikenplant voor. Stel je ook voor dat je nog nooit in je leven een volgroeide boom hebt gezien. Zou het dan niet verstandig zijn om je controleproblemen te beteugelen in plaats van op voorhand alle regels te bepalen over hoe deze plant zou mogen evolueren en groeien?


### Conclusie over eindige Supply



Of de Bitcoin Supply voorbij de 21 miljoen zal groeien kunnen we vandaag niet zeggen, en dat is waarschijnlijk niet zo erg. Ervoor zorgen dat het veiligheidsbudget hoog genoeg blijft is cruciaal, maar niet urgent. Laten we deze discussie over 10-50 jaar voeren, als we meer weten. Als het dan nog relevant is.


# Bitcoin Bestuur

<partId>411bf53f-af4b-50f1-b71b-e40fe3ff64b7</partId>


## Upgraden

<chapterId>3ffa84d1-adfa-5fbc-9b13-384ea783fcdd</chapterId>



![](assets/upgrading-banner.webp)


Bitcoin op een veilige manier upgraden kan extreem moeilijk zijn. Bij sommige veranderingen duurt het meerdere jaren om ze uit te rollen. In dit hoofdstuk leren we over de algemene woordenschat rond het upgraden van Bitcoin en onderzoeken we enkele voorbeelden van historische upgrades van het protocol en de inzichten die we daaruit hebben opgedaan. Tot slot bespreken we ketensplitsingen en de risico's en kosten die daaraan verbonden zijn.


Om in de stemming te komen voor dit hoofdstuk, moet je [David Harding's stuk over harmonie en disharmonie](https://bitcointalk.org/dec/p1.html) lezen:


> Bitcoin experts hebben het vaak over consensus, waarvan de betekenis abstract en Hard moeilijk vast te pinnen is. Maar het woord consensus is geëvolueerd van het Latijnse woord concentus, "een samen zingende harmonie", dus laten we het niet hebben over Bitcoin consensus, maar over Bitcoin harmonie.
>

> Harmonie is wat Bitcoin doet werken. Duizenden volledige knooppunten werken elk onafhankelijk om te verifiëren of de transacties die ze ontvangen geldig zijn en produceren zo een harmonieuze overeenkomst over de toestand van Bitcoin Ledger zonder dat een knooppuntoperator iemand anders hoeft te vertrouwen. Het is vergelijkbaar met een koor waar elk lid hetzelfde lied zingt op hetzelfde moment om iets te produceren dat veel mooier is dan elk van hen alleen zou kunnen produceren.
>

> Het resultaat van Bitcoin harmonie is een systeem waar bitcoins niet alleen veilig zijn voor kleine dieven (op voorwaarde dat je je sleutels veilig bewaart), maar ook voor eindeloze inflatie, massale of gerichte confiscatie, of gewoon het bureaucratische moeras dat het bestaande financiële systeem is.

Dit hoofdstuk bespreekt hoe Bitcoin opgewaardeerd kan worden zonder onenigheid te veroorzaken. In harmonie blijven, d.w.z. consensus behouden, is inderdaad één van de grootste uitdagingen bij de ontwikkeling van Bitcoin. Er zijn veel nuances in de opwaardeermechanismen, die het best begrepen kunnen worden door het bestuderen van eerdere opwaarderingen. Om deze reden legt het hoofdstuk veel nadruk op historische voorbeelden, en het begint met het opzetten van een nuttig vocabulaire.


### Woordenschat



Volgens Wikipedia verwijst [voorwaartse compatibiliteit](https://en.wikipedia.org/wiki/Forward_compatibility) naar de toestand waarin een oude software gegevens kan verwerken die zijn gemaakt door nieuwere software, waarbij de delen die het niet begrijpt worden genegeerd:


Een standaard ondersteunt voorwaartse compatibiliteit als een product dat voldoet aan eerdere versies "netjes" invoer kan verwerken die is ontworpen voor latere versies van de standaard, waarbij nieuwe onderdelen die het niet begrijpt worden genegeerd.


Omgekeerd verwijst [achterwaartse compatibiliteit] (https://en.wikipedia.org/wiki/Backward_compatibility) naar wanneer gegevens van oude software bruikbaar zijn in nieuwere software. Er wordt gezegd dat een verandering volledig compatibel is als deze zowel voorwaarts als achterwaarts compatibel is.


Een verandering aan de Bitcoin consensusregels wordt een *Soft Fork* genoemd als het volledig compatibel is. Dit is de meest gebruikelijke manier om Bitcoin op te waarderen, om een aantal redenen die we verder in dit hoofdstuk zullen bespreken. Als een verandering aan de Bitcoin consensusregels achterwaarts compatibel is, maar niet voorwaarts, dan wordt het een *Hard Fork* genoemd.


Voor een technisch overzicht van Soft vorken en Hard vorken, lees [hoofdstuk 11 van Grokking Bitcoin](https://rosenbaum.se/book/grokking-Bitcoin-11.html). Het legt deze termen uit en duikt ook in de upgrade mechanismen. Het is aan te raden, hoewel niet strikt noodzakelijk, om dit te begrijpen voordat je verder leest.


### Historische upgrades



Bitcoin is vandaag de dag niet meer hetzelfde als toen het Genesis blok werd gemaakt. Door de jaren heen zijn er verschillende upgrades gemaakt. In 2018 [sprak Eric Lombrozo op de Breaking Bitcoin conferentie](https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) over de verschillende upgradingmechanismen van Bitcoin, waarbij hij aangaf hoezeer ze in de loop der tijd zijn geëvolueerd. Hij legde zelfs uit hoe Satoshi Nakamoto ooit Bitcoin opwaardeerde via een Hard Fork:


> Er was eigenlijk een Hard-Fork in Bitcoin dat Satoshi deed dat we het nooit op deze manier zouden doen- het is een behoorlijk slechte manier om het te doen. Als je kijkt naar de git commit beschrijving hier [[757f076](https://github.com/Bitcoin/Bitcoin/commit/757f0769d8360ea043f469f3a35f6ec204740446)], zegt hij iets over teruggedraaide makefile.unix wx-config versie 0.3.6. Klopt. Dat is alles wat er staat. Er staat helemaal niets over een brekende wijziging. Hij verborg het daar eigenlijk. Hij [postte ook op bitcointalk](https://bitcointalk.org/index.php?topic=626.msg6451#msg6451) en zei, upgrade alsjeblieft zo snel mogelijk naar 0.3.6. We hebben een implementatie bug gerepareerd waarbij het mogelijk is dat valse transacties kunnen worden weergegeven als geaccepteerd. Accepteer geen Bitcoin betalingen totdat u heeft geüpgraded naar 0.3.6. Als je niet meteen kunt upgraden, kun je het beste je Bitcoin node afsluiten totdat je dat doet. En daar bovenop, ik weet niet waarom hij besloot om dit ook te doen, besloot hij om wat optimalisaties toe te voegen in dezelfde code. Een bug oplossen en wat optimalisaties toevoegen.

Hij wijst erop dat, opzettelijk of niet, deze Hard Fork mogelijkheden creëerde voor toekomstige Soft forks, namelijk de Script operators (opcodes) OP_NOP1-OP_NOP10. We zullen meer kijken naar deze code verandering in cve-2010-5141. Deze opcodes zijn tot nu toe gebruikt voor twee Soft forks:


- [BIP65](https://github.com/Bitcoin/bips/blob/master/bip-0065.mediawiki) (OP_CHECKLOCKTIMEVERIFY)
- [BIP113](https://github.com/Bitcoin/bips/blob/master/bip-0112.mediawiki) (OP_SEQUENCEVERIFY).


Lombrozo geeft ook een overzicht van de manier waarop de upgrade-mechanismen door de jaren heen zijn geëvolueerd, tot 2017. Sindsdien is slechts één andere grote upgrade, Taproot, ingezet. Het lange en enigszins chaotische proces dat leidde tot de activering ervan, heeft ons geholpen om meer inzicht te krijgen in de opwaardeermechanismen in Bitcoin.


#### SegWit upgrade



Terwijl alle upgrades voor SegWit min of meer pijnloos waren verlopen, was deze anders. Toen de SegWit activeringscode werd vrijgegeven, in oktober 2016, leek er overweldigende steun voor te zijn onder Bitcoin gebruikers, maar om de een of andere reden gaven miners geen steun aan voor deze upgrade, waardoor de activering stagneerde zonder dat er een oplossing in zicht was.


Aaron van Wirdum beschrijft deze kronkelige weg in zijn Bitcoin Magazine artikel [The Long Road To SegWit] (https://bitcoinmagazine.com/technical/the-long-road-to-SegWit-how-bitcoins-biggest-protocol-upgrade-became-reality). Hij begint met uit te leggen wat SegWit is en hoe dat inhaakt op het blokgrootte debat. Daarna schetst Van Wirdum de gebeurtenissen die leidden tot de uiteindelijke activering. Centraal in dit proces stond een upgrade mechanisme genaamd *user activated Soft Fork*, of kortweg UASF, dat werd voorgesteld door gebruiker Shaolinfry:


> Shaolinfry stelde een alternatief voor: een door de gebruiker geactiveerde Soft Fork (UASF). In plaats van Hash stroomactivering, zou een door de gebruiker geactiveerde Soft Fork een "'flag day activation' hebben, waarbij nodes op een vooraf bepaald tijdstip in de toekomst beginnen met de handhaving." Zolang zo'n UASF afgedwongen wordt door een economische meerderheid, zou dit een meerderheid van mijnwerkers moeten dwingen om de Soft Fork te volgen (of te activeren).

Hij haalt onder andere Shaolinfry's e-mail aan de Bitcoin-dev mailinglijst aan. In die gelegenheid [pleitte Shaolinfry tegen Miner geactiveerde Soft vorken](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-February/013643.html), waarbij hij een aantal problemen opsomde:


> Ten eerste moet je erop kunnen vertrouwen dat de Hash macht zal valideren na activering.  De BIP66 Soft Fork was een geval waarbij 95% van de Hashrate gereedheid signaleerde, maar in werkelijkheid valideerde ongeveer de helft de opgewaardeerde regels niet en mijnde per ongeluk op een ongeldig blok.
>

> Ten tweede heeft Miner signalering een natuurlijk veto waardoor een klein percentage van Hashrate een veto kan uitspreken tegen knooppunt activering van de upgrade voor iedereen. Tot nu toe hebben Soft forks geprofiteerd van het relatief gecentraliseerde Mining landschap waar er relatief weinig Mining pools zijn die geldige blokken bouwen; als we meer naar Hashrate decentralisatie gaan, is het waarschijnlijk dat we meer en meer last zullen krijgen van "upgrade inertie" die de meeste upgrades zal vetoën.

Shaolinfry vestigde ook de aandacht op een veel voorkomende misinterpretatie van Miner signalering: mensen dachten over het algemeen dat het een middel was waarmee mijnwerkers konden beslissen over protocol upgrades, in plaats van een actie die hielp upgrades te coördineren. Door dit misverstand voelden mijnwerkers zich misschien ook verplicht om publiekelijk hun mening te verkondigen over een bepaalde Soft Fork, alsof dat gewicht gaf aan het voorstel.


Het UASF-voorstel is, in een notendop, een "vlaggetjesdag" waarop knooppunten beginnen met het afdwingen van specifieke nieuwe regels. Op die manier hoeven miners geen collectieve inspanning te leveren om de upgrade te coördineren, maar *kan* de activering eerder starten dan de vlaggetjesdag als genoeg blokken aangeven dat ze dit ondersteunen:


> Mijn voorstel is om het beste van beide werelden te hebben. Aangezien een door de gebruiker geactiveerde Soft Fork een relatief lange aanlooptijd nodig heeft voor activering, kunnen we dit combineren met BIP9 om de optie te geven van een snellere Hash power gecoördineerde activering of activering per vlaggetjesdag, afhankelijk van wat het eerst komt.
> In beide gevallen kunnen we gebruik maken van de waarschuwingssystemen in BIP9. De wijziging is relatief eenvoudig, het toevoegen van een activeringstijdparameter die de BIP9-status naar LOCKED_IN zet voor het einde van de BIP9-implementatietime-out.

Dit idee kreeg veel belangstelling, maar leek niet op bijna unanieme steun te kunnen rekenen, waardoor er bezorgdheid ontstond over een mogelijke kettingsplitsing. Het artikel van Aaron van Wirdum legt uit hoe dit uiteindelijk werd opgelost dankzij [BIP91](https://github.com/Bitcoin/bips/blob/master/bip-0091.mediawiki), geschreven door James Hilliard:


> Hilliard stelde een ietwat complexe maar slimme oplossing voor die alles compatibel zou maken: Gesegregeerde Getuige activering zoals voorgesteld door het Bitcoin Core ontwikkelingsteam, de BIP148 UASF en het New York Agreement activeringsmechanisme. Zijn BIP91 zou Bitcoin heel kunnen houden - tenminste gedurende de SegWit activering.

Er waren wat meer complicerende factoren in het spel (bijv. de zogenaamde "New York Agreement"), waar dit GIP rekening mee moest houden. We raden je aan om het artikel van Van Wirdum volledig te lezen om meer te weten te komen over de vele interessante details in dit verhaal.


#### Discussie na SegWit


Na de inzet van SegWit ontstond er een discussie over inzetmechanismen. Zoals opgemerkt door Eric Lombrozo in [zijn toespraak op de Breaking Bitcoin conferentie](https://btctranscripts.com/breaking-Bitcoin/2017/changing-consensus-rules-without-breaking-Bitcoin/) en door Shaolinfry, is een Miner geactiveerde Soft Fork niet het ideale upgrade mechanisme:


> Op een gegeven moment zullen we waarschijnlijk meer functies willen toevoegen aan het Bitcoin protocol. Dit is een grote filosofische vraag die we onszelf stellen. Doen we een UASF voor de volgende? Hoe zit het met een hybride aanpak? Miner op zichzelf geactiveerd is uitgesloten. bip9 gaan we niet opnieuw gebruiken.

In januari 2020 stuurde Matt Corallo [een e-mail](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2020-January/017547.html) naar de Bitcoin-dev mailinglijst die een discussie op gang bracht over toekomstige Soft Fork inzetmechanismen. Hij noemde vijf doelen die volgens hem essentieel waren in een upgrade. David Harding [vat ze samen in een Bitcoin Optech nieuwsbrief](https://bitcoinops.org/en/newsletters/2020/01/15/#discussion-of-Soft-Fork-activation-mechanisms) als:


> De mogelijkheid om af te breken als er ernstige bezwaren zijn tegen de voorgestelde wijzigingen van de consensusregels . De toewijzing van voldoende tijd na het uitbrengen van bijgewerkte software om er zeker van te zijn dat de meeste economische knooppunten geüpgraded zijn om deze regels af te dwingen . De verwachting dat de Hash snelheid van het netwerk ruwweg hetzelfde zal zijn voor en na de verandering, evenals tijdens elke overgang . Het zoveel mogelijk voorkomen van het aanmaken van blokken die ongeldig zijn onder de nieuwe regels, wat zou kunnen leiden tot valse bevestigingen bij niet-geüpgraded nodes en SPV clients . De zekerheid dat de afbreekmechanismen niet misbruikt kunnen worden door griefers of partizanen om een alom gewenste upgrade zonder bekende problemen tegen te houden

Wat Corallo voorstelt is een combinatie van een Miner geactiveerde Soft Fork en een door de gebruiker geactiveerde Soft Fork:


> Dus, als iets concreters, denk ik dat een activeringsmethode die het juiste precedent schept en op de juiste manier rekening houdt met de bovenstaande doelen, zou zijn:
>

> 1) een standaard BIP 9-implementatie met een tijdshorizon van één jaar voor
activering met 95% Miner paraatheid, +

> 2) als er binnen een jaar geen activering plaatsvindt, een termijn van zes maanden
rustperiode waarin de gemeenschap kan analyseren en discussiëren

de redenen voor geen activering en +

> 3) in het geval dat het zinvol is, zou een eenvoudige command-line/Bitcoin.conf parameter die werd ondersteund sinds de oorspronkelijke inzet release gebruikers in staat stellen om te kiezen voor een BIP 8 inzet met een 24-maanden tijdhorizon voor vlag-dag activering (evenals een nieuwe Bitcoin Core release die de vlag universeel mogelijk maakt).
>

> Dit biedt een zeer lange tijdshorizon voor meer standaard activering, terwijl de doelen in #5 nog steeds gehaald worden, zelfs als in die gevallen de tijdshorizon aanzienlijk verlengd moet worden om de doelen van #3 te halen. Bitcoin ontwikkelen is geen race. Als het moet, zorgen 42 maanden wachten ervoor dat we geen negatief precedent scheppen waar we spijt van krijgen als Bitcoin blijft groeien.

#### Taproot upgrade - Snelrecht



Toen Taproot in oktober 2020 klaar was om ingezet te worden, wat betekende dat alle technische details rond de consensusregels geïmplementeerd waren en brede goedkeuring hadden gekregen binnen de gemeenschap, begonnen de discussies over hoe Taproot daadwerkelijk ingezet zou moeten worden op te laaien. Deze discussies waren tot op dat moment vrij bescheiden.


Er deden veel voorstellen voor activeringsmechanismen de ronde en David Harding

[samengevat op de Bitcoin Wiki] (https://en.Bitcoin.it/wiki/Taproot_activation_proposals). In zijn artikel legde hij enkele eigenschappen uit van BIP8, dat op dat moment enkele recente wijzigingen had ondergaan om het flexibeler te maken.


> Op het moment dat dit document wordt geschreven, is [BIP8] (https://github.com/Bitcoin/bips/blob/master/bip-0008.mediawiki) opgesteld op basis van de lessen die in 2017 zijn geleerd. Een opmerkelijke verandering na BIP's 9+148 is dat gedwongen activering nu gebaseerd is op blokhoogte in plaats van mediane verstreken tijd; een tweede opmerkelijke verandering is dat gedwongen activering een booleaanse parameter is die wordt gekozen wanneer de activeringsparameters van een Soft Fork worden ingesteld voor de eerste inzet of bijgewerkt in een latere inzet.

BIP8 zonder geforceerde activering lijkt erg op [BIP9](https://github.com/Bitcoin/bips/blob/master/bip-0009.mediawiki) versie bits met time-out en vertraging, met als enige significante verschil dat BIP8 blokhoogtes gebruikt in vergelijking met BIP9's gebruik van mediane verstreken tijd. Deze instelling staat toe dat de poging mislukt (maar later opnieuw kan worden geprobeerd).


BIP8 met gedwongen activering wordt afgesloten met een verplichte signaleringsperiode waarin alle blokken die in overeenstemming met de regels zijn geproduceerd, gereedheid voor Soft Fork moeten signaleren op een manier die activering zal triggeren in een eerdere inzet van dezelfde Soft Fork met niet-verplichte activering. Met andere woorden, als knooppuntversie x wordt vrijgegeven zonder gedwongen activering en later versie y wordt vrijgegeven die met succes mijners dwingt om gereedheid te signaleren binnen dezelfde tijdsperiode, zullen beide versies op hetzelfde moment beginnen met het afdwingen van de nieuwe consensusregels.


Deze flexibiliteit van het herziene BIP8-voorstel maakt het mogelijk om een aantal andere ideeën uit te drukken in termen van hoe ze eruit zouden zien met behulp van BIP8. Dit biedt een gemeenschappelijke factor die kan worden gebruikt om veel verschillende voorstellen te categoriseren.


Vanaf dit punt werden de discussies erg verhit, vooral over de vraag of `lockinontimeout` `true` moest zijn (zoals in een door de gebruiker geactiveerde Soft Fork, door Harding aangeduid als "BIP8 met geforceerde activering") of `false` (zoals in een Miner geactiveerde Soft Fork, door Harding aangeduid als "BIP8 zonder geforceerde activering").


Een van de voorstellen was getiteld "Laten we kijken wat er gebeurt". Om de een of andere reden kreeg dit voorstel pas zeven maanden later veel aandacht.


Gedurende deze zeven maanden ging de discussie door en het leek erop dat er geen brede consensus bereikt kon worden over welk implementatiemechanisme gebruikt moest worden. Er waren voornamelijk twee kampen: een die de voorkeur gaf aan `lockinontimeout=true` (de UASF menigte) en de andere die de voorkeur gaf aan `lockinontimeout=false` (de "probeer en als het mislukt heroverweeg" menigte). Aangezien er geen overweldigende steun was voor één van deze opties, draaide het debat in cirkels rond zonder dat er een uitweg leek te zijn. Sommige van deze discussies werden gehouden op IRC, in een kanaal genaamd ##Taproot-activation, maar [op 5 maart 2021](https://gnusha.org/Taproot-activation/2021-03-05.log), veranderde er iets:


```
06:42 < harding> roconnor: is somebody proposing BIP8(3m, false)?  I mentioned that the other day but I didn't see any responses.
[...]
06:43 < willcl_ark_> Amusingly, I was just thinking to myself that, vs this, the SegWit activation was actually pretty straightforward: simply a LOT=false and if it fails a UASF.
06:43 < maybehuman> it's funny, "let's see what happens" (i.e. false, 3m) was a poular choice right at the beginning of this channel iirc
06:44 < roconnor> harding: I think I am.  I don't know how much that is worth.  Mostly I think it would be a widely acceptable configuration based on my understanding of everyone's concerns.
06:44 < willcl_ark_> maybehuman: becuase everybody actually wants this, even miners reckoned they could upgrade in about two weeks (or at least f2pool said that)
06:44 < roconnor> harding: BIP8(3m,false) with an extended lockin-period.
06:45 < harding> roconnor: oh, good.  It's been my favorite option since I first summarized the options on the wiki like seven months ago.
06:45 <@michaelfolkson> UASF wouldn't release (true,3m) but yeah Core could release (false, 3m)
06:45 < willcl_ark_> harding: It certainly seems like a good approach to me. _if_ that fails, then you can try an understand why, without wasting too much time
```


De "laten we zien wat er gebeurt"-benadering leek eindelijk te klikken in de hoofden van de mensen. Dit proces zou later worden aangeduid als "Speedy Trial" vanwege de korte signaleringsperiode. David Harding legt dit idee uit aan de bredere gemeenschap in een

[e-mail naar de Bitcoin-dev mailinglijst] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-March/018583.html):

> De eerdere versie van dit voorstel werd meer dan 200 dagen geleden gedocumenteerd en de onderliggende code van Taproot werd meer dan 140 dagen geleden samengevoegd in Bitcoin Core. Als we Speedy Trial hadden gestart op het moment dat Taproot werd samengevoegd (wat een beetje onrealistisch is), dan zouden we minder dan twee maanden verwijderd zijn van Taproot of we zouden al meer dan een maand geleden verder zijn gegaan met de volgende activeringspoging.
>

> In plaats daarvan hebben we lang gedebatteerd en lijken we niet dichter te zijn bij wat ik een algemeen aanvaardbare oplossing vind dan toen de mailinglijst meer dan een jaar geleden begon met het bespreken van activeringsprogramma's na SegWit. Ik denk dat Speedy Trial een manier is om generate snel vooruitgang te boeken die ofwel het debat zal beëindigen (voorlopig, als de activering succesvol is) of ons wat feitelijke gegevens zal geven waarop we toekomstige Taproot activeringsvoorstellen kunnen baseren.

Dit inzetmechanisme werd in de loop van twee maanden verfijnd en vervolgens vrijgegeven in [Bitcoin Core versie 0.21.1](https://github.com/Bitcoin/Bitcoin/blob/master/doc/release-notes/release-notes-0.21.1.md#Taproot-Soft-Fork). De miners begonnen al snel met het signaleren van deze upgrade, waarbij de deployment-status naar `LOCKED_IN` werd verplaatst, en na een aflossingsvrije periode werden de Taproot regels midden november 2021 geactiveerd in blok [709632](https://Mempool.space/block/0000000000000000000687bca986194dc2c1f949318629b44bb54ec0a94d8244).


#### Toekomstige uitrolmechanismen


Gezien de problemen met de recente Soft vorken, SegWit en Taproot, is het niet duidelijk hoe de volgende upgrade zal worden ingezet. Speedy Trial werd gebruikt om Taproot uit te rollen, maar het werd gebruikt om de kloof tussen de UASF en de MASF menigte te overbruggen, niet omdat het het bekendste implementatiemechanisme is geworden.


### Risico's


Tijdens de activering van Fork, of het nu Hard of Soft is, Miner geactiveerd of geactiveerd door de gebruiker, bestaat het risico van een langdurige kettingsplitsing. Een split die langer dan een paar blokken blijft hangen, kan ernstige schade toebrengen aan het sentiment rond Bitcoin en aan de prijs ervan. Maar bovenal zou het grote verwarring veroorzaken over wat Bitcoin is. Is Bitcoin deze keten of die keten?


Het risico van een door gebruikers geactiveerde Soft Fork is dat de nieuwe regels geactiveerd worden, zelfs als de meerderheid van de Hash macht ze niet ondersteunt. Dit scenario zou resulteren in een langdurige kettingsplitsing, die zou blijven bestaan tot de meerderheid van de Hash macht de nieuwe regels aanneemt. Het zou vooral Hard kunnen zijn om mijnwerkers te stimuleren over te schakelen naar de nieuwe keten als ze al blokken hadden gemijnd na de splitsing op de oude keten, omdat ze door over te schakelen hun eigen blokbeloningen zouden opgeven. Het is echter de moeite waard om een opmerkelijke episode te vermelden: in maart 2013 vond een langdurige splitsing plaats als gevolg van een onbedoelde Hard Fork en, in tegenstelling tot deze stimulans, namen twee grote Mining pools de beslissing om hun tak van de splitsing te verlaten om de consensus te herstellen.


Aan de andere kant is het risico met een Miner geactiveerde Soft Fork een gevolg van het feit dat miners aan false signaling kunnen doen, wat betekent dat het werkelijke aandeel van de Hash macht dat de verandering steunt kleiner kan zijn dan het lijkt. Als de werkelijke steun niet een meerderheid van de Hash macht omvat, zouden we waarschijnlijk een langdurige kettingsplitsing zien, vergelijkbaar met die beschreven in de vorige paragraaf. Dit, of op zijn minst een soortgelijk probleem, is in werkelijkheid gebeurd toen BIP66 werd ingezet, maar het werd binnen 6 blokken of zo opgelost.


#### Kosten van een splitsing



Jimmy Song [sprak over de kosten die gepaard gaan met Hard vorken](https://btctranscripts.com/breaking-Bitcoin/2017/socialized-costs-of-Hard-forks/) tijdens Breaking Bitcoin in Parijs, maar veel van wat hij zei is ook van toepassing op een kettingsplitsing als gevolg van een mislukte Soft Fork. Hij sprak over *negatieve externaliteiten*, en definieerde ze als de prijs die iemand anders moet betalen voor jouw eigen acties:


> Het klassieke voorbeeld van een negatieve externaliteit is een fabriek. Misschien produceren ze - misschien is het een olieraffinaderij en produceren ze een goed dat goed is voor de economie, maar ze produceren ook iets dat een negatieve externaliteit is, zoals vervuiling. Het is niet alleen iets waar iedereen voor moet betalen, dat moet worden opgeruimd of waar iedereen onder lijdt. Maar het zijn ook 2e en 3e orde effecten, zoals meer verkeer richting de fabriek als gevolg van meer werknemers die er naartoe moeten. Het kan ook zijn dat je daar in de buurt wilde dieren in gevaar brengt. Het is niet zo dat iedereen moet betalen voor de negatieve externaliteiten, het kunnen specifieke mensen zijn, zoals mensen die voorheen die weg gebruikten of dieren die in de buurt van die fabriek waren, en zij betalen ook voor de kosten van die fabriek.

In de context van Bitcoin illustreert hij negatieve externaliteiten aan de hand van Bitcoin Cash (bcash), een Hard Fork van Bitcoin die kort voor die conferentie in 2017 werd gecreëerd. Hij categoriseert de negatieve externe effecten van een Hard Fork in eenmalige kosten en permanente kosten.


Onder de vele voorbeelden van eenmalige kosten noemt hij de kosten die worden gemaakt door beurzen:


> We hebben dus een heleboel beurzen en die hadden veel eenmalige kosten die ze moesten betalen. Het eerste dat gebeurde, was dat stortingen en opnames voor deze exchanges een dag of twee moesten worden stilgelegd omdat ze niet wisten wat er zou gebeuren. Veel van deze exchanges moesten Cold-opslag aanspreken omdat hun gebruikers om bcash vroegen. Het maakt deel uit van hun fiduciaire plicht, ze moeten dat doen. Je moet ook de nieuwe software controleren. Dit is iets wat we bij itbit moesten doen. We willen bcash uitgeven- hoe doen we dat? Moeten we electron cash downloaden? Zit er malware in? We moeten het gaan controleren. We hadden ongeveer 10 dagen om uit te zoeken of dit goed was of niet. En dan moet je beslissen, gaan we gewoon een eenmalige opname toestaan, of gaan we deze nieuwe munt op de lijst zetten? Voor een Exchange om een nieuwe munt op de lijst te zetten, zijn er allerlei nieuwe procedures voor Cold opslag, ondertekening, stortingen, opnames. Of je kunt gewoon een eenmalige gebeurtenis houden waarbij je ze op een bepaald moment hun bcash geeft en er daarna nooit meer aan denkt. Maar dat heeft ook zijn problemen. En tot slot, op welke manier je het ook doet, opnames of noteringen - je hebt een nieuwe infrastructuur nodig om op de een of andere manier met deze token te werken, zelfs al is het een eenmalige opname. Je hebt een manier nodig om deze tokens aan je gebruikers te geven. Nogmaals, korte termijn. Toch? Geen tijd om dit te doen, het moet snel gebeuren.

Hij somt ook de eenmalige kosten op voor handelaars, betalingsverwerkers, wallets, miners en gebruikers, evenals enkele permanente kosten, zoals verlies van privacy en een hoger risico op reorgs.


Inderdaad, als er een splitsing plaatsvindt en de keten met de meest algemene regels sterker wordt dan de keten met de strengere regels, zal er een reorg plaatsvinden. Dit zal een ernstige impact hebben op alle transacties die uitgevoerd worden in de weggevaagde tak. Om deze redenen is het echt belangrijk om te allen tijde te proberen ketensplitsingen te vermijden.


### Conclusie over upgraden


Bitcoin groeit en evolueert met de tijd. In de loop der jaren zijn verschillende upgrade-mechanismen gebruikt en de leercurve is steil. Er worden steeds geavanceerdere en robuustere methoden uitgevonden naarmate we meer leren over hoe het netwerk reageert.


Om Bitcoin in harmonie te houden, hebben Soft vorken bewezen de weg vooruit te zijn, maar de grote vraag is nog steeds niet volledig beantwoord: hoe zetten we Soft vorken veilig in zonder onenigheid te veroorzaken?


## Tegenstrijdig denken

<chapterId>d4982f3d-4694-51cc-99be-28f54b03a2a2</chapterId>


![](assets/adversarialthinking-banner.webp)


Dit hoofdstuk gaat over *tegenstrijdig denken*, een denkwijze die zich richt op wat er fout zou kunnen gaan en hoe tegenstanders zouden kunnen handelen. We beginnen met het bespreken van Bitcoin's beveiligingsaannames en beveiligingsmodel, waarna we uitleggen hoe gewone gebruikers hun zelfsoevereiniteit en Bitcoin's Full node decentralisatie kunnen verbeteren door adversair te denken. Daarna kijken we naar enkele actuele bedreigingen voor Bitcoin en in de geest van de tegenstander. Tot slot praten we over het *axioma van verzet*, dat je kan helpen begrijpen waarom mensen überhaupt aan Bitcoin werken.


Bij het bespreken van beveiliging binnen verschillende systemen is het belangrijk om te begrijpen wat de beveiligingsaannames zijn. Een typische beveiligingsaanname in Bitcoin is "het discrete logaritme probleem is Hard op te lossen", wat simpel gezegd betekent dat het praktisch onmogelijk is om een private sleutel te vinden die overeenkomt met een bepaalde publieke sleutel. Een andere vrij sterke beveiligingsaanname is dat een meerderheid van de hashpower van het netwerk eerlijk is, wat betekent dat ze zich aan de regels houden. Als deze aannames onjuist blijken, dan zit Bitcoin in de problemen.


In 2015 gaf Andrew Poelstra [een lezing](https://btctranscripts.com/scalingbitcoin/hong-kong-2015/security-assumptions/) op de Scaling Bitcoin conferentie in Hong Kong, waarin hij de beveiligingsaannames van Bitcoin analyseerde. Hij begint met op te merken dat veel systemen tot op zekere hoogte geen rekening houden met tegenstanders; het is bijvoorbeeld echt Hard om een gebouw te beschermen tegen alle soorten vijandige gebeurtenissen. In plaats daarvan accepteren we over het algemeen de mogelijkheid dat iemand het gebouw platbrandt en voorkomen we tot op zekere hoogte dit en ander vijandig gedrag door wetshandhaving, enz.


Zie Greg Maxwells analogie van het gebouw:


![](https://youtu.be/Gs9lJTRZCDc?t=2799)


Maar online zijn de dingen anders:


> Online hebben we dit echter niet. We hebben pseudoniem en anoniem gedrag, iedereen kan verbinding maken met iedereen en het systeem beschadigen. Als het mogelijk is om het systeem tegen te werken, dan zullen ze dat doen. We kunnen er niet van uitgaan dat ze zichtbaar zullen zijn en dat ze gepakt zullen worden.

Het gevolg is dat alle bekende zwakke plekken in Bitcoin op de een of andere manier moeten worden aangepakt, anders worden ze uitgebuit. Bitcoin is tenslotte de grootste honingpot ter wereld.


Poelstra gaat verder met te vermelden dat Bitcoin een nieuw soort systeem is; het is neveliger dan bijvoorbeeld een ondertekeningsprotocol dat heel duidelijke veiligheidsaannames heeft.


Op zijn persoonlijke blog [duikt software engineer Jameson Lopp hierin] (https://blog.lopp.net/bitcoins-security-model-a-deep-dive/):


> In werkelijkheid werd en wordt het Bitcoin protocol gebouwd zonder een formeel gedefinieerde specificatie of veiligheidsmodel. Het beste wat we kunnen doen is de prikkels en het gedrag van actoren binnen het systeem bestuderen om het beter te begrijpen en proberen te beschrijven.

We hebben dus een systeem dat in de praktijk lijkt te werken, maar waarvan we formeel niet kunnen bewijzen dat het veilig is. Een bewijs is waarschijnlijk niet mogelijk vanwege

de complexiteit van het systeem zelf.


### Niet alleen voor Bitcoin experts



Het belang van tegendraads denken strekt zich tot op zekere hoogte ook uit tot alledaagse Bitcoin gebruikers, niet alleen tot hardcore Bitcoin ontwikkelaars en experts. Ragnar Lifthasir vermeldt in een [tweetstorm](https://bitcoinwords.github.io/tweetstorm-on-adversarial-thinking) hoe simplistische verhalen rond Bitcoin - bijvoorbeeld "gewoon HODL" - vernederend kunnen zijn voor Bitcoin zelf, en besluit met de volgende woorden


> Om Bitcoin en onszelf sterker te maken, moeten we denken als de software engineers die bijdragen aan Bitcoin. Ze reviewen, zoeken genadeloos naar fouten. Op hun technische evenementen praten ze over alle manieren waarop een voorstel kan mislukken. Ze denken tegendraads. Ze zijn conservatief

Hij noemt deze simplistische verhalen monomanieën. Met deze definitie zegt hij dat je door je op één ding te richten - bijvoorbeeld "alleen HODL"- het risico loopt dat je de aantoonbaar belangrijkere dingen over het hoofd ziet, zoals het veilig houden van je Bitcoin of je best doen om Bitcoin op een Trustless manier te gebruiken.


### Bedreigingen



Er zijn veel bekende zwakheden in Bitcoin, en veel daarvan worden actief uitgebuit. Om daar een glimp van op te vangen, kun je een kijkje nemen op de [Zwakke punten pagina](https://en.Bitcoin.it/wiki/Weaknesses) op Bitcoin wiki. Er wordt een grote verscheidenheid aan problemen genoemd, zoals

Wallet diefstal en denial-of-service-aanvallen:


> Als een aanvaller probeert het netwerk te vullen met clients die hij controleert, dan is de kans groot dat je alleen verbinding maakt met aanvallende nodes. Hoewel Bitcoin nooit een telling van knooppunten voor iets gebruikt, kan het volledig isoleren van een knooppunt van het eerlijke netwerk nuttig zijn bij het uitvoeren van andere aanvallen.

Dit type aanval wordt een *Sybil aanval* genoemd en treedt op wanneer een enkele entiteit meerdere knooppunten in een netwerk controleert en deze gebruikt om zich voor te doen als meerdere entiteiten.


Zoals het citaat ook vermeldt, is de Sybil-aanval niet effectief op het Bitcoin netwerk omdat er geen stemming plaatsvindt via nodes of andere numerieke entiteiten, maar via rekenkracht. Desalniettemin maakt deze platte structuur het systeem vatbaar voor andere aanvallen. De Bitcoin wikipagina beschrijft ook andere mogelijke aanvallen, zoals het verbergen van informatie (vaak aangeduid als *eclips aanval*), en de manier waarop Bitcoin Core enkele heuristische tegenmaatregelen tegen zulke aanvallen implementeert.


Het bovenstaande zijn voorbeelden van echte bedreigingen die aangepakt moeten worden.


### Eenvoudig sabotageveld


![](assets/sabotage-manual.webp)


Uittreksel uit de Eenvoudige Sabotage Veldhandleiding


Om de geest van de tegenstander beter te begrijpen, kan het nuttig zijn om een kijkje te nemen in hoe ze te werk gaan. Een Amerikaanse overheidsinstantie met de naam Office of Strategic Services, die tijdens de Tweede Wereldoorlog opereerde en onder andere spionage, sabotage en propaganda tot doel had, produceerde een [handboek](https://www.gutenberg.org/ebooks/26184) voor hun personeel over hoe de vijand op de juiste manier te saboteren. De titel was "Simple Sabotage Field Manual" en bevatte concrete tips over het infiltreren in de vijand om hun leven Hard te maken. De tips varieerden van het afbranden van magazijnen tot het veroorzaken van slijtage aan boren om het leven van de vijand te verminderen

efficiëntie.


Er is bijvoorbeeld een sectie over hoe een infiltrant organisaties kan verstoren. Het is niet Hard in te zien hoe zulke tactieken gebruikt zouden kunnen worden om het Bitcoin ontwikkelingsproces aan te vallen, dat voor iedereen openstaat om aan deel te nemen. Een toegewijde aanvaller kan de voortgang blijven tegenhouden door eindeloze discussies over irrelevante zaken, marchanderen over precieze formuleringen en discussies proberen te herhalen die al uitgebreid aan de orde zijn geweest. De aanvaller kan ook een trollenleger inhuren om zijn eigen effectiviteit te vermenigvuldigen; we kunnen dit een sociale Sybil-aanval noemen. Met een sociale Sybil-aanval kunnen ze het laten lijken alsof er meer weerstand is tegen een voorgestelde verandering dan er in werkelijkheid is.


Dit laat zien hoe een vastberaden staat er alles aan kan en zal doen om de vijand te vernietigen, inclusief het van binnenuit afbreken. Aangezien Bitcoin een vorm van geld is die concurreert met gevestigde fiatvaluta's, is de kans groot dat staten Bitcoin als een vijand zullen beschouwen.


### Axiome van Weerstand


Eric Voskuil [schrijft op zijn Cryptoeconomics wikipagina](https://github.com/libbitcoin/libbitcoin-system/wiki/Axiom-of-Resistance) over wat hij het "axioma van weerstand" noemt:


> Met andere woorden, er wordt aangenomen dat het mogelijk is voor een systeem om zich te verzetten tegen staatscontrole. Dit wordt niet geaccepteerd als een feit, maar wordt beschouwd als een redelijke aanname, dankzij empirisch onderzoek naar het gedrag van vergelijkbare systemen, waarop het systeem kan worden gebaseerd.
>

> Wie het axioma van weerstand niet accepteert, overweegt een heel ander systeem dan Bitcoin. Als je aanneemt dat het niet mogelijk is voor een systeem om weerstand te bieden tegen staatscontrole, dan kloppen conclusies niet in de context van Bitcoin - net zoals conclusies in sferische geometrie in tegenspraak zijn met Euclides. Hoe kan Bitcoin toestemmingsvrij of censuurbestendig zijn zonder het axioma? De tegenstrijdigheid leidt tot voor de hand liggende fouten in een poging het conflict te rationaliseren.


Wat hij in wezen zegt is dat het alleen zinvol is om het te proberen als je ervan uitgaat dat het mogelijk is om een systeem te creëren dat staten niet kunnen controleren.


Dit betekent dat om aan Bitcoin te werken je het axioma van weerstand moet accepteren, anders kun je je tijd beter aan andere projecten besteden. Het erkennen van dat axioma helpt je om je ontwikkelingsinspanningen te richten op de echte problemen: coderen rond tegenstanders op staatsniveau. Met andere woorden, denk tegendraads.


### Conclusie over tegenstrijdig denken



Een gedecentraliseerd systeem kan geen verantwoording buiten het systeem zelf hebben, daarom moet Bitcoin kwaadaardig gedrag rigoureuzer voorkomen dan traditionele systemen. In een dergelijk systeem is tegendraads denken noodzakelijk.


Om Bitcoin veilig te houden, moet je de vijanden en hun drijfveren kennen. De meeste bedreigingen lijken neer te komen op natiestaten, die enorme economische macht hebben door belastingen en het drukken van geld. Ze zullen hun privileges om geld te drukken waarschijnlijk niet snel opgeven.


## Open Bron

<chapterId>427a160c-f893-5b2c-afba-7b24e71ba899</chapterId>



![](assets/opensource-banner.webp)


Bitcoin is gebouwd met open source software. In dit hoofdstuk analyseren we wat dit betekent, hoe het onderhoud van de software werkt, en hoe open source software in Bitcoin toestemmingsvrije ontwikkeling mogelijk maakt. We duiken in *selectie cryptografie*, dat gaat over de selectie en het gebruik van bibliotheken in cryptografische systemen. Het hoofdstuk bevat een sectie over Bitcoin's beoordelingsproces, gevolgd door een andere over de manieren waarop Bitcoin ontwikkelaars gefinancierd worden. Het laatste deel gaat over hoe Bitcoin's open source cultuur er van buitenaf heel vreemd uit kan zien, en waarom deze vermeende vreemdheid eigenlijk een teken van goede gezondheid is.


De meeste Bitcoin software, en vooral Bitcoin Core, is open source. Dit betekent dat de broncode van de software beschikbaar is voor het algemene publiek om te bekijken, sleutelen, wijzigen en opnieuw te distribueren. De definitie van open source op [](https://opensource.org/osd) bevat onder andere de volgende belangrijke punten:


> Vrije herdistributie: De licentie zal geen enkele partij verbieden om de software te verkopen of weg te geven als onderdeel van een softwaredistributie die programma's van verschillende bronnen bevat. De licentie vereist geen royalty of andere vergoeding voor een dergelijke verkoop.
>

> Broncode: Het programma moet een broncode bevatten en moet zowel in broncode als in gecompileerde vorm kunnen worden verspreid. Als een product in een bepaalde vorm niet wordt verdeeld met broncode, moet er een goed gepubliceerde manier zijn om de broncode te verkrijgen voor niet meer dan redelijke reproductiekosten, bij voorkeur gratis downloaden via het internet. De broncode moet de geprefereerde vorm zijn waarin een programmeur het programma zou wijzigen. Opzettelijk versleutelde broncode is niet toegestaan. Tussenvormen zoals de uitvoer van een preprocessor of vertaler zijn niet toegestaan.
>

> Afgeleide werken: De licentie moet wijzigingen en afgeleide werken toestaan, en moet toestaan dat deze verspreid worden onder dezelfde voorwaarden als de licentie van de originele software.

Bitcoin Core voldoet aan deze definitie door gedistribueerd te worden onder de [MIT Licentie] (https://github.com/Bitcoin/Bitcoin/blob/master/COPYING):


```
The MIT License (MIT)

Copyright (c) 2009-2022 The Bitcoin Core developers
Copyright (c) 2009-2022 Bitcoin Developers

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
```


Zoals opgemerkt in Hoofdstuk "Vertrouw niet, controleer", is het belangrijk voor gebruikers om te kunnen verifiëren dat de Bitcoin software die ze draaien "werkt zoals geadverteerd". Om dat te kunnen doen, moeten ze onbeperkte toegang hebben tot de broncode van de software die ze willen verifiëren.


In de komende paragrafen duiken we in enkele andere interessante aspecten van open source software in Bitcoin.


### Onderhoud van software



De broncode van Bitcoin Core wordt onderhouden in een Git repository die gehost wordt op [GitHub](https://github.com/Bitcoin/Bitcoin). Iedereen kan die repository klonen zonder toestemming te vragen, en het dan lokaal inspecteren, bouwen of wijzigen. Dit betekent dat er vele duizenden kopieën van de repository over de hele wereld verspreid zijn. Dit zijn allemaal kopieën van dezelfde repository, dus wat maakt deze specifieke GitHub Bitcoin Core repository zo speciaal? Technisch gezien is het helemaal niet speciaal, maar sociaal gezien is het het middelpunt geworden van de Bitcoin ontwikkeling.


Bitcoin en beveiligingsexpert Jameson Lopp legt dit heel goed uit in een [blog post](https://blog.lopp.net/who-controls-Bitcoin-core-/) getiteld "Who Controls Bitcoin Core?":


> Bitcoin Core is eerder een brandpunt voor de ontwikkeling van het Bitcoin protocol dan een commando- en controlepunt. Als het om wat voor reden dan ook zou ophouden te bestaan, zou er een nieuw brandpunt ontstaan - het technische communicatieplatform waarop het gebaseerd is (momenteel de GitHub repository) is eerder een kwestie van gemak dan van definitie / projectintegriteit. In feite hebben we al gezien dat Bitcoin's brandpunt voor ontwikkeling van platform en zelfs van naam verandert!

Hij legt verder uit hoe de software van Bitcoin Core wordt onderhouden en beveiligd tegen kwaadaardige codewijzigingen. De algemene conclusie van dit volledige artikel is samengevat aan het einde:


> Niemand controleert Bitcoin.
>

> Niemand controleert het brandpunt voor de ontwikkeling van Bitcoin.

Bitcoin Core ontwikkelaar Eric Lombrozo vertelt meer over het ontwikkelingsproces in zijn [Medium post](https://medium.com/@elombrozo/the-Bitcoin-core-merge-process-74687a09d81d) getiteld "The Bitcoin Core Merge Process":


> Iedereen kan Fork de code base repository en willekeurige wijzigingen aanbrengen in hun eigen repository. Ze kunnen een client bouwen vanuit hun eigen repository en die in plaats daarvan draaien als ze dat willen. Ze kunnen ook binaire builds maken die andere mensen kunnen draaien.
>

> Als iemand een wijziging die ze hebben gemaakt in hun eigen repository wil samenvoegen in Bitcoin Core, kunnen ze een pull request indienen. Eenmaal ingediend, kan iedereen de wijzigingen bekijken en er commentaar op geven, ongeacht of ze wel of geen commit toegang hebben tot Bitcoin Core zelf.

Het moet opgemerkt worden dat het erg lang kan duren voordat pull requests worden samengevoegd in het repository door beheerders, en dat is meestal te wijten aan een gebrek aan review, wat vaak te wijten is aan een gebrek aan *reviewers*.


Lombrozo heeft het ook over het proces rondom consensuswijzigingen, maar dat valt een beetje buiten het bereik van dit hoofdstuk. Zie het vorige hoofdstuk "Upgraden" voor meer informatie over hoe het Bitcoin protocol wordt geüpgraded.


### Ontwikkeling zonder vergunning



We hebben vastgesteld dat iedereen code kan schrijven voor Bitcoin Core zonder toestemming te vragen, maar dat het niet noodzakelijkerwijs samengevoegd wordt in de Git repository. Dit heeft invloed op elke wijziging, van het veranderen van kleurenschema's van de grafische gebruiker Interface, tot de manier waarop peer-to-peer berichten worden geformatteerd, en zelfs consensusregels, d.w.z. de verzameling regels die een geldige Blockchain definiëren.


Waarschijnlijk net zo belangrijk is dat gebruikers vrij zijn om systemen te ontwikkelen bovenop Bitcoin, zonder toestemming te vragen. We hebben talloze succesvolle softwareprojecten gezien die gebouwd zijn bovenop Bitcoin, zoals:



- Lightning Network: Een betalingsnetwerk dat snelle betaling van zeer kleine bedragen mogelijk maakt. Het vereist zeer weinig On-Chain Bitcoin transacties. Er bestaan verschillende interoperabele implementaties, zoals [Core Lightning](https://github.com/ElementsProject/lightning), [LND](https://github.com/lightningnetwork/LND), [Eclair](https://github.com/ACINQ/eclair), en [Lightning Dev Kit](https://github.com/lightningdevkit).
- CoinJoin: Meerdere partijen werken samen om hun betalingen in een enkele transactie te combineren om Address clustering moeilijker te maken. Er bestaan verschillende implementaties.
- Sidechains: Dit systeem kan een munt vergrendelen op Bitcoin's Blockchain om hem te ontgrendelen op een andere Blockchain. Hierdoor kunnen bitcoins worden verplaatst naar een andere Blockchain, namelijk een Sidechain, om de functies te gebruiken die beschikbaar zijn op die Sidechain. Voorbeelden zijn [Blockstream's Elements](https://github.com/ElementsProject/Elements).
- OpenTimestamps: Hiermee kun je [Timestamp een document](https://opentimestamps.org/) op Bitcoin's Blockchain op een privé manier opslaan. Je kunt dan die Timestamp gebruiken om te bewijzen dat een document voor een bepaalde tijd moet hebben bestaan.


Zonder ontwikkeling zonder toestemming zouden veel van deze projecten niet mogelijk zijn geweest. Zoals vermeld in het hoofdstuk over Neutraliteit, als ontwikkelaars toestemming zouden moeten vragen om protocollen bovenop Bitcoin te bouwen, zouden alleen de protocollen ontwikkeld worden die zijn toegestaan door de centrale ontwikkelaars toelatingscommissie.


Het is gebruikelijk dat systemen zoals de hierboven genoemde zelf een licentie hebben als open source software, waardoor mensen hun code kunnen bijdragen, hergebruiken of beoordelen zonder toestemming te vragen. Open source is de gouden standaard geworden voor Bitcoin software licenties.


### Pseudonieme ontwikkeling



Het niet hoeven vragen om toestemming om Bitcoin software te ontwikkelen brengt een interessante en belangrijke optie op tafel: je kunt code schrijven en publiceren, in Bitcoin Core of elk ander open source project, zonder je identiteit te onthullen.


Veel ontwikkelaars kiezen voor deze optie door onder een pseudoniem te werken en proberen het los te houden van hun ware identiteit. De redenen hiervoor kunnen van ontwikkelaar tot ontwikkelaar verschillen. Eén gebruiker met een pseudoniem is ZmnSCPxj. Naast andere projecten draagt hij bij aan Bitcoin Core en Core Lightning, één van de verschillende implementaties van Lightning Network. [Hij schrijft](https://zmnscpxj.github.io/about.html) op zijn webpagina:


> Ik ben ZmnSCPxj, een willekeurig gegenereerd internetpersoon. Mijn voornaamwoorden zijn hij/hem/his.
>

> Ik begrijp dat mensen instinctief verlangen om mijn identiteit te kennen. Ik denk echter dat mijn identiteit grotendeels immaterieel is en ik laat me liever beoordelen door mijn werk.
>

> Als je je afvraagt of je wel of niet moet doneren en je je afvraagt wat mijn kosten van levensonderhoud of mijn inkomen zijn, begrijp dan dat je eigenlijk aan mij zou moeten doneren op basis van het nut dat je mijn
artikelen en mijn werk aan Bitcoin en de Lightning Network.


In zijn geval moet de reden voor het gebruik van een pseudoniem worden beoordeeld op zijn verdiensten en niet op wie de persoon of personen achter het pseudoniem is of zijn. Interessant genoeg onthulde hij in een [artikel op CoinDesk] (https://www.coindesk.com/markets/2020/06/29/many-Bitcoin-developers-are-choosing-to-use-pseudonyms-for-good-reason/) dat het pseudoniem om een andere reden werd gecreëerd.


> Mijn oorspronkelijke reden [voor het gebruik van een pseudoniem] was simpelweg dat ik me zorgen maakte [over] het maken van een grote fout; ZmnSCPxj was dus oorspronkelijk bedoeld als een wegwerppseudoniem dat in zo'n geval kon worden opgegeven. Het lijkt echter een overwegend positieve reputatie te hebben opgebouwd, dus heb ik het behouden

Het gebruik van een pseudoniem stelt je inderdaad in staat om vrijer te spreken zonder je persoonlijke reputatie op het spel te zetten als je iets stoms zegt of een grote fout maakt. Zoals bleek, kreeg zijn pseudoniem een goede naam en in 2019 [kreeg hij zelfs een ontwikkelingssubsidie](https://twitter.com/spiralbtc/status/1204815615678177280), wat op zich al een bewijs is van de toestemmingsvrije aard van Bitcoin.


Het bekendste pseudoniem in Bitcoin is ongetwijfeld Satoshi Nakamoto. Het is onduidelijk waarom hij voor een pseudoniem koos, maar achteraf gezien was het waarschijnlijk om meerdere redenen een goede beslissing:


- Omdat veel mensen speculeren dat Nakamoto veel Bitcoin bezit, is het noodzakelijk voor zijn financiële en persoonlijke veiligheid om zijn identiteit onbekend te houden.
- Omdat zijn identiteit onbekend is, is er geen mogelijkheid om iemand te vervolgen, wat verschillende overheidsinstanties een Hard tijd geeft.
- Er is geen gezaghebbend persoon om naar op te kijken, waardoor Bitcoin meer meritocratisch is en beter bestand tegen chantage.


Merk op dat deze punten niet alleen gelden voor Satoshi Nakamoto, maar voor iedereen die in Bitcoin werkt of aanzienlijke hoeveelheden van de munteenheid bezit, in verschillende mate.


### Selectie cryptografie


Open source-ontwikkelaars maken vaak gebruik van open source-bibliotheken die door andere mensen zijn ontwikkeld. Dit is een natuurlijk en geweldig onderdeel van elk gezond ecosysteem. Maar Bitcoin software gaat om met echt geld en daarom moeten ontwikkelaars extra voorzichtig zijn bij het kiezen van bibliotheken van derden waar ze afhankelijk van moeten zijn.


In een filosofisch [gesprek over cryptografie] (https://btctranscripts.com/greg-maxwell/2015-04-29-gmaxwell-Bitcoin-selection-cryptography/), wil Gregory Maxwell de term "cryptografie" herdefiniëren die hij te eng vindt. Hij legt uit dat *informatie fundamenteel vrij wil zijn*, en baseert daarop zijn definitie van cryptografie:


> Cryptografie is de kunst en wetenschap die we gebruiken om de fundamentele aard van informatie te bestrijden, om het naar onze politieke en morele wil te buigen en om het naar menselijke doelen te leiden tegen alle toevalligheden en pogingen in.

Hij introduceert dan de term *selectie cryptografie*, waarnaar verwezen wordt als de kunst van het selecteren van cryptografische hulpmiddelen, en legt uit waarom het een belangrijk onderdeel is van cryptografie. Het draait om hoe cryptografische bibliotheken, gereedschappen en praktijken te selecteren, of zoals hij zegt "het cryptosysteem van het kiezen van cryptosystemen".


Aan de hand van concrete voorbeelden laat hij zien hoe selectiecryptografie gemakkelijk gruwelijk mis kan gaan en hij stelt ook een lijst met vragen voor die je jezelf zou kunnen stellen als je ermee oefent. Hieronder staat een gedistilleerde versie van die lijst:


- Is de software bedoeld voor jouw doeleinden?
- Worden de cryptografische overwegingen serieus genomen?
- Wat is het beoordelingsproces? Is dat er?
- Wat is de ervaring van de auteurs?
- Is de software gedocumenteerd?
- Is de software draagbaar?
- Is de software getest?
- Past de software best practices toe?


Hoewel dit niet de ultieme gids voor succes is, kan het erg nuttig zijn om deze punten door te nemen wanneer je aan selectiecryptografie doet.


Vanwege de problemen die Maxwell hierboven noemde, probeert Bitcoin Core echt Hard om [de blootstelling aan bibliotheken van derden te minimaliseren] (https://github.com/Bitcoin/Bitcoin/blob/master/doc/dependencies.md). Natuurlijk kun je niet alle externe afhankelijkheden uitbannen, anders zou je alles zelf moeten schrijven, van font rendering tot implementatie van system calls.


### Beoordeling



Deze sectie heet "Herziening", in plaats van "Code Herziening", omdat de veiligheid van Bitcoin zwaar leunt op herziening op meerdere niveaus, niet alleen op de broncode. Bovendien vereisen verschillende ideeën een review op verschillende niveaus: een verandering van de consensusregel vereist een diepere review op meer niveaus dan een verandering van het kleurenschema of een typefout.


Op weg naar de uiteindelijke goedkeuring doorloopt een idee meestal verschillende fasen van discussie en beoordeling. Enkele van deze fasen worden hieronder opgesomd:



- Er is een idee gepost op de Bitcoin-dev mailinglijst
- Het idee is geformaliseerd in een Bitcoin Verbeteringsvoorstel (BIP)
- De BIP is geïmplementeerd in een pull request (PR) naar Bitcoin Core
- Inzetmechanismen worden besproken
- Enkele concurrerende implementatiemechanismen zijn geïmplementeerd in pull requests voor Bitcoin Core
- Pull requests worden samengevoegd naar de master branch
- Gebruikers kiezen of ze de software willen gebruiken of niet


In elk van deze fasen beoordelen mensen met verschillende standpunten en achtergronden de beschikbare informatie, of dat nu de broncode, een BIP of gewoon een losjes beschreven idee is. De fasen worden meestal niet op een strikte top-down manier uitgevoerd, er kunnen inderdaad meerdere fasen tegelijkertijd plaatsvinden en soms ga je ertussen heen en weer. Verschillende mensen kunnen ook feedback geven tijdens verschillende fasen.


Een van de meest productieve code reviewers op Bitcoin Core is Jon Atack. Hij schreef [een blogpost](https://jonatack.github.io/articles/how-to-review-pull-requests-in-Bitcoin-core) over hoe pull requests te reviewen in Bitcoin Core. Hij benadrukt dat een goede code reviewer zich richt op hoe hij het beste waarde kan toevoegen.


> Als nieuwkomer is het doel om te proberen waarde toe te voegen, met vriendelijkheid en nederigheid, terwijl je zoveel mogelijk leert.
>

> Een goede benadering is om het niet over jou te hebben, maar eerder over "Hoe kan ik het beste van dienst zijn?"

Hij benadrukt dat beoordeling echt een beperkende factor is in Bitcoin Core. Veel goede ideeën blijven hangen in een limbo waar geen review plaatsvindt, in afwachting van review. Merk op dat reviewen niet alleen goed is voor Bitcoin, maar ook een geweldige manier om te leren over de software en er tegelijkertijd waarde aan toe te voegen. Atacks vuistregel is om 5-15 PR's te beoordelen voordat je zelf een PR maakt. Nogmaals, je focus moet liggen op hoe je de gemeenschap het beste van dienst kunt zijn, niet op hoe je je eigen code gemerged kunt krijgen. Bovendien benadrukt hij het belang van review op het juiste niveau: is dit het moment voor nits en typefouten, of heeft de ontwikkelaar meer behoefte aan een conceptueel georiënteerde review? Jon Attack voegt hieraan toe:


> Een nuttige eerste vraag bij het begin van een evaluatie kan zijn: "Wat is hier op dit moment het meest nodig?" Het beantwoorden van deze vraag vereist ervaring en verzamelde context, maar het is een nuttige vraag om te beslissen hoe je de meeste waarde kunt toevoegen in de minste tijd.

De tweede helft van de post bestaat uit wat nuttige praktische technische begeleiding over hoe je de review daadwerkelijk uitvoert en bevat links naar belangrijke documentatie om verder te lezen.


Bitcoin Core ontwikkelaar en code reviewer Gloria Zhao heeft [een artikel] geschreven (https://github.com/glozow/Bitcoin-notes/blob/master/review-checklist.md) met vragen die ze zichzelf meestal stelt tijdens een review. Ze geeft ook aan wat zij als een goede review beschouwt:


> Persoonlijk vind ik een goede recensie er een waarbij ik mezelf veel gerichte vragen heb gesteld over de PR en tevreden ben met de antwoorden
aan hen. [...] Natuurlijk begin ik met conceptuele vragen, dan benaderingsgerelateerde vragen en dan implementatievragen. Over het algemeen denk ik persoonlijk dat het nutteloos is om C++ syntax-gerelateerd commentaar achter te laten op een concept PR, en ik zou het onbeleefd vinden om terug te gaan naar "klopt dit" nadat de auteur 20+ van mijn suggesties voor code-organisatie heeft behandeld.


Haar idee dat een goede beoordeling zich moet richten op wat op een bepaald moment het meest nodig is, sluit goed aan bij het advies van Jon Atack. Zij

stelt een lijst met vragen voor die je jezelf kunt stellen op verschillende niveaus van het reviewproces, maar benadrukt dat deze lijst op geen enkele manier uitputtend is, noch een regelrecht recept. De lijst wordt geïllustreerd met praktijkvoorbeelden van GitHub.


### Financiering



Veel mensen werken aan Bitcoin open source ontwikkeling, voor Bitcoin Core of voor andere projecten. Velen doen dit in hun vrije tijd zonder enige compensatie, maar sommige ontwikkelaars krijgen er ook voor betaald.


Bedrijven, individuen en organisaties die belang hebben bij het voortdurende succes van Bitcoin kunnen geld doneren aan ontwikkelaars, rechtstreeks of via organisaties die het geld op hun beurt verdelen onder individuele ontwikkelaars. Er zijn ook een aantal Bitcoin-gerichte bedrijven die bekwame ontwikkelaars inhuren om hen fulltime aan Bitcoin te laten werken.


### Cultuurschok



Mensen krijgen soms de indruk dat er veel strijd en eindeloze verhitte debatten zijn tussen Bitcoin ontwikkelaars en dat ze niet in staat zijn om beslissingen te nemen.


Bijvoorbeeld, het Taproot inzetmechanisme, het werd gedurende een lange periode besproken waarbij twee "kampen" zich vormden. Het ene kamp wilde de upgrade "laten mislukken" als mijnwerkers na een bepaald moment niet overweldigend voor de nieuwe regels hadden gestemd, terwijl het andere kamp de regels na dat moment hoe dan ook wilde handhaven. Michael Folkson vat de argumenten van de twee kampen samen in een [email](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2021-February/018380.html) aan de Bitcoin-dev mailinglijst.


Het debat ging schijnbaar eindeloos door en het was echt Hard om op korte termijn een consensus hierover te zien ontstaan. Hierdoor raakten mensen gefrustreerd en als gevolg daarvan verhevigde de hitte. Gregory Maxwell (als gebruiker nullc) maakte zich [op Reddit](https://www.reddit.com/r/Bitcoin/comments/hrlpnc/technical_taproot_why_activate/fyqbn8s/?utm_source=share&utm_medium=web2x&context=3) zorgen dat de lange discussies de upgrade minder veilig zouden maken:


> Op dit moment zorgt extra wachten niet voor meer controle en zekerheid. In plaats daarvan vermindert extra uitstel de inertie en neemt het risico mogelijk iets toe, omdat mensen details beginnen te vergeten, het werk aan downstream gebruik uitstellen (zoals Wallet ondersteuning) en niet zoveel extra controle-inspanningen investeren als ze zouden doen als ze vertrouwen hadden in het activeringstijdschema.

Uiteindelijk werd dit geschil opgelost dankzij een nieuw voorstel van David Harding en Russel O'Connor genaamd Speedy Trial, dat een relatief kortere signaleringsperiode inhoudt voor mijnwerkers om de activering van Taproot vast te leggen, of snel te falen. Als ze het in die periode activeerden, zou Taproot ongeveer 6 maanden later worden ingezet.


Iemand die niet gewend is aan het ontwikkelingsproces van Bitcoin zou waarschijnlijk denken dat deze verhitte debatten er vreselijk slecht en zelfs giftig uitzien. Er zijn minstens twee factoren waardoor ze er in de ogen van sommigen slecht uitzien:



- Vergeleken met closed source-bedrijven vinden alle debatten in het openbaar plaats, ongecorrigeerd. Een softwarebedrijf als Google zou zijn werknemers nooit in het openbaar laten debatteren over voorgestelde functies, het zou hooguit een verklaring publiceren over het standpunt van het bedrijf over het onderwerp. Hierdoor zien bedrijven er harmonischer uit dan Bitcoin.
- Omdat Bitcoin rechtenvrij is, mag iedereen zijn mening geven. Dit is fundamenteel anders dan bij een closed source bedrijf waar slechts een handjevol mensen een mening heeft, meestal gelijkgestemden. De overvloed aan meningen die binnen Bitcoin geuit worden, is gewoon onthutsend vergeleken met bijvoorbeeld PayPal.


De meeste Bitcoin ontwikkelaars zouden beweren dat deze openheid een goede en gezonde omgeving creëert en zelfs noodzakelijk is voor het beste resultaat.


Zoals gehint in het hoofdstuk Bedreiging, kan de tweede bullet hierboven erg voordelig zijn, maar heeft ook een keerzijde. Een aanvaller kan gebruik maken van vertragingstactieken, zoals beschreven in de [Simple Sabotage Field Manual] (https://www.gutenberg.org/ebooks/26184), om de besluitvorming en het ontwikkelingsproces te verstoren.


Iets anders dat het vermelden waard is, is dat, aangezien Bitcoin geld is en Bitcoin Core onpeilbare hoeveelheden geld beveiligt, beveiliging in deze context niet lichtvaardig wordt opgevat. Daarom is doorgewinterde Bitcoin Core

ontwikkelaars misschien erg Hard-achtig overkomen, en die houding is meestal gerechtvaardigd. Inderdaad, een functie met een zwakke rationale erachter zal niet worden geaccepteerd. Hetzelfde zou gebeuren als het de

reproduceerbare builds, nieuwe afhankelijkheden toegevoegd, of als de code niet voldeed aan de [best practices] van Bitcoin (https://github.com/Bitcoin/Bitcoin/blob/master/doc/developer-notes.md).


Nieuwe (en oude) ontwikkelaars kunnen hierdoor gefrustreerd raken. Maar, zoals gebruikelijk in open source software, kun je altijd Fork de repository, samenvoegen wat je wilt Fork, en bouw en draai je eigen binary.


### Conclusie over Open Source


Bitcoin Core en de meeste andere Bitcoin software is open source, wat betekent dat iedereen vrij is om de software te distribueren, aan te passen en te gebruiken zoals zij willen. De Bitcoin Core repository op GitHub is momenteel het middelpunt van de Bitcoin ontwikkeling, maar die status kan veranderen als mensen de beheerders of de website zelf gaan wantrouwen.


Open source maakt ontwikkeling in en bovenop Bitcoin zonder toestemming mogelijk. Of je nu code schrijft, code reviewt of protocollen maakt; open source maakt het mogelijk, pseudonoom of niet.


Het ontwikkelingsproces rond Bitcoin is radicaal open, wat Bitcoin er giftig en inefficiënt uit kan laten zien, maar dat is wat Bitcoin veerkrachtig houdt tegen kwaadwillende actoren.


## Schalen

<chapterId>bb3f3924-202c-5cdd-b2e9-e0c1cab0e48e</chapterId>



![](assets/scaling-banner.webp)



In dit hoofdstuk onderzoeken we hoe Bitcoin wel en niet schaalt. We beginnen met te kijken hoe mensen in het verleden redeneerden over schalen. Daarna legt het grootste deel van dit hoofdstuk verschillende benaderingen uit om Bitcoin te schalen, met name verticaal, horizontaal, naar binnen en gelaagd schalen. Elke beschrijving wordt gevolgd door overwegingen of de aanpak ingrijpt in de waardepropositie van Bitcoin.


In de Bitcoin-ruimte geven verschillende mensen verschillende definities aan het woord "schaal". Sommigen zien het als het vergroten van de transactiecapaciteit van Blockchain, anderen geloven dat het gelijk staat aan het efficiënter gebruiken van Blockchain en weer anderen zien het als het ontwikkelen van systemen bovenop Bitcoin.


In de context van Bitcoin, en voor de doeleinden van dit boek, definiëren we schalen als *het vergroten van de gebruikscapaciteit van Bitcoin zonder de censuurbestendigheid in gevaar te brengen*. Deze definitie omvat verschillende

soorten veranderingen, bijvoorbeeld:


- Transactie-inputs minder bytes laten gebruiken
- Prestaties van handtekeningverificatie verbeteren
- Het peer-to-peer netwerk minder bandbreedte laten gebruiken
- Batching van transacties
- Gelaagde architectuur


We zullen binnenkort duiken in de verschillende benaderingen van schaalvergroting, maar laten we beginnen met een kort overzicht van de geschiedenis van Bitcoin binnen de context van schaalvergroting.


### Geschiedenis van schaalvergroting



Schalen is al sinds de Genesis van Bitcoin een belangrijk punt van discussie. De allereerste zin van de [allereerste e-mail] (https://www.metzdowd.com/pipermail/cryptography/2008-November/014814.html) in reactie op Satoshi's aankondiging van de Bitcoin whitepaper op de Cryptography mailinglijst ging inderdaad over schalen:


> Satoshi Nakamoto schreef:
>

> "Ik heb gewerkt aan een nieuw elektronisch geldsysteem dat volledig peer-to-peer is, zonder vertrouwde derde partij.  Het artikel is beschikbaar op http://www.Bitcoin.org/Bitcoin.pdf"
>

> We hebben zo'n systeem heel erg nodig, maar zoals ik uw voorstel begrijp, lijkt het niet op de vereiste schaalgrootte te passen.

Het gesprek op zich is misschien niet erg interessant of accuraat, maar het laat zien dat schaalvergroting vanaf het begin een zorg is geweest.


Discussies over het schalen bereikten hun hoogtepunt rond 2015-2017, toen er veel verschillende ideeën circuleerden over de vraag of en hoe de maximale blokgroottelimiet kon worden verhoogd. Dat was een nogal oninteressante discussie over het veranderen van een parameter in de broncode, een verandering die niet fundamenteel iets oploste, maar het probleem van het schalen verder naar de toekomst schoof, waardoor technische schuld werd opgebouwd.


In 2015 werd een conferentie genaamd [Scaling Bitcoin](https://scalingbitcoin.org/) gehouden in Montreal, met een vervolgconferentie zes maanden later in Hong Kong en daarna op een aantal andere locaties over de hele wereld. De focus lag juist op hoe Address te schalen. Veel Bitcoin ontwikkelaars en andere enthousiastelingen verzamelden zich op deze conferenties om verschillende schaalproblemen en voorstellen te bespreken. De meeste van deze discussies gingen niet over het vergroten van de blokgrootte, maar over oplossingen voor de langere termijn.


Na de conferentie in Hongkong in december 2015 [vatte Gregory Maxwell zijn visie samen](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-December/011865.html) op veel van de kwesties die waren besproken, te beginnen met wat algemene schaalfilosofie:


> Met de beschikbare technologie zijn er fundamentele afwegingen tussen schaal en decentralisatie. Als het systeem te duur is, zullen mensen gedwongen worden om derden te vertrouwen in plaats van zelfstandig de regels van het systeem af te dwingen. Als het middelengebruik van Bitcoin Blockchain, in verhouding tot de beschikbare technologie, te groot is, verliest Bitcoin zijn concurrentievoordelen ten opzichte van legacysystemen, omdat validatie te duur wordt (waardoor veel gebruikers worden weggeconcurreerd).  Als de capaciteit te laag is en onze transactiemethoden te inefficiënt, zal toegang tot de keten voor geschillenbeslechting te duur zijn, waardoor het vertrouwen weer terug in het systeem wordt gedreven.

Hij heeft het over de afweging tussen doorvoer en decentralisatie. Als je grotere blokken toestaat, zul je sommige mensen van het netwerk duwen omdat ze niet meer de middelen hebben om de blokken te valideren. Maar aan de andere kant, als toegang tot blokruimte duurder wordt, zullen minder mensen het zich kunnen veroorloven om het te gebruiken als geschillenbeslechtingsmechanisme. In beide gevallen worden gebruikers naar vertrouwde diensten geduwd.


Hij gaat verder met het samenvatten van de vele benaderingen van schaalvergroting die op de conferentie zijn gepresenteerd. Daaronder zijn rekenkundig efficiëntere handtekeningverificaties, *segregated witness* inclusief een verandering in de limiet van de blokgrootte, een ruimte-efficiënter blokpropagatiemechanisme en het bouwen van protocollen bovenop Bitcoin in lagen. Veel van deze

benaderingen zijn sindsdien geïmplementeerd.


### Benaderingen voor schaalvergroting



Zoals hierboven al is aangegeven, hoeft het schalen van Bitcoin niet per se te gaan over het vergroten van de blokgrootte of andere limieten. We gaan nu door een aantal algemene benaderingen voor het schalen, waarvan sommige niet lijden onder de doorvoer-decentralisatie afweging die in de vorige sectie is genoemd.


#### Verticaal schalen



Verticaal schalen is het proces van het vergroten van de rekenkracht van de machines die gegevens verwerken. In de context van Bitcoin zijn dit de volledige knooppunten, namelijk de machines die Blockchain valideren namens hun gebruikers.


De meest besproken techniek voor verticale schaling in Bitcoin is het verhogen van de limiet voor de blokgrootte. Hierdoor zouden sommige volledige knooppunten hun hardware moeten upgraden om aan de toenemende rekenbehoeften te kunnen voldoen. Het nadeel is dat dit ten koste gaat van de centralisatie.


Naast de negatieve effecten op de Full node decentralisatie, zou verticaal schalen ook op minder voor de hand liggende manieren een negatieve invloed kunnen hebben op de Bitcoin decentralisatie en veiligheid. Laten we eens kijken naar hoe miners "zouden moeten" werken. Stel, een Miner mijnt een blok op hoogte 7 en publiceert dat blok op het Bitcoin netwerk. Het zal enige tijd duren voordat dit blok brede acceptatie bereikt, wat voornamelijk te wijten is aan twee factoren:


- De overdracht van het blok tussen peers kost tijd vanwege bandbreedtebeperkingen.
- Validatie van het blok kost tijd.


Terwijl blok 7 door het netwerk wordt verspreid, zijn veel miners nog steeds Mining bovenop blok 6 omdat ze blok 7 nog niet hebben ontvangen en gevalideerd. Gedurende deze tijd, als één van deze miners een nieuw blok vindt op hoogte 7, zullen er twee concurrerende blokken zijn op die hoogte. Er kan maar één blok zijn op hoogte 7 (of eender welke andere hoogte), wat betekent dat één van de twee kandidaten oud moet worden.


Kortom, oudbakken blokken komen voor omdat het tijd kost voor elk blok om zich voort te planten, en hoe langer de voortplanting duurt, hoe groter de kans op oudbakken blokken.


Stel dat de blokgroottelimiet wordt opgeheven en dat de gemiddelde blokgrootte aanzienlijk toeneemt. Blokken zouden zich dan langzamer over het netwerk verspreiden vanwege bandbreedtebeperkingen en verificatietijd. Een toename in propagatietijd zal ook de kans op oude blokken vergroten.


Mijnwerkers houden er niet van als hun blokken staled zijn omdat ze dan hun Block reward verliezen, dus zullen ze er alles aan doen om dit te voorkomen

scenario. De maatregelen die ze kunnen nemen zijn onder andere:



- Het uitstellen van de validatie van een binnenkomend blok, ook bekend als *validationless Mining*. Miners kunnen gewoon de Proof-of-Work van de blokkop controleren en daarop mijnen, terwijl ze ondertussen het volledige blok downloaden en valideren.
- Aansluiten op een Mining pool met grotere bandbreedte en connectiviteit.


Mining zonder validatie ondermijnt verder de decentralisatie van Full node, omdat de Miner terugvalt op het vertrouwen van binnenkomende blokken, tenminste tijdelijk. Het schaadt ook de veiligheid tot op zekere hoogte, omdat een deel van de rekenkracht van het netwerk mogelijk bouwt op een ongeldige Blockchain, in plaats van op de sterkste en geldige keten.


Het tweede opsommingsteken heeft een negatief effect op Miner decentralisatie, omdat meestal de pools met de beste netwerkconnectiviteit en bandbreedte ook de grootste zijn, waardoor miners naar een paar grote pools toegaan.


#### Horizontaal schalen



Horizontaal schalen verwijst naar technieken die de werklast verdelen over meerdere machines. Hoewel dit een veelgebruikte schaalbenadering is bij populaire websites en databases, is het niet eenvoudig om dit te doen in Bitcoin.


Veel mensen noemen deze Bitcoin schaalbenadering *sharding*. Het komt erop neer dat elke Full node slechts een deel van de Blockchain verifieert. Peter Todd heeft veel nagedacht over het concept van sharding. Hij schreef een [blog post](https://petertodd.org/2015/why-scaling-Bitcoin-with-sharding-is-very-Hard) waarin hij sharding in algemene termen uitlegt en ook zijn eigen idee genaamd *treechains* presenteert. Het artikel is moeilijk te lezen, maar Todd maakt een aantal punten die goed verteerbaar zijn:


> In sharded systemen werkt de "Full node verdediging" niet, tenminste niet direct. Het hele punt is dat niet iedereen alle gegevens heeft, dus je moet beslissen wat er gebeurt als ze niet beschikbaar zijn.

Daarna presenteert hij verschillende ideeën over hoe je sharding, of horizontaal schalen, kunt aanpakken. Tegen het einde van de post concludeert hij:


> Er is echter een groot probleem: Holy !@#$ is het bovenstaande complex vergeleken met Bitcoin! Zelfs de "kiddy" versie van sharding - mijn linearisatie schema in plaats van zk-SNARKS - is waarschijnlijk één of twee orden van grootte complexer dan het gebruik van het Bitcoin protocol op dit moment is, toch lijkt op dit moment een groot deel van de bedrijven in deze ruimte hun handen in de lucht te hebben gestoken en in plaats daarvan gecentraliseerde API providers te gebruiken. Het daadwerkelijk implementeren van het bovenstaande en het in handen krijgen van eindgebruikers zal niet eenvoudig zijn.
>

> Aan de andere kant is decentralisatie niet goedkoop: het gebruik van PayPal is één of twee orden van grootte eenvoudiger dan het Bitcoin protocol.

De conclusie die hij trekt is dat sharding *misschien* technisch mogelijk is, maar het zou ten koste gaan van een enorme complexiteit. Gezien het feit dat veel gebruikers Bitcoin al te complex vinden en in plaats daarvan liever gecentraliseerde diensten gebruiken, zal het Hard worden om ze te overtuigen iets te gebruiken dat nog complexer is.


#### Inwaartse schaalvergroting



Terwijl horizontaal en verticaal schalen historisch goed werken in gecentraliseerde systemen zoals databases en webservers, lijken ze niet geschikt voor een gedecentraliseerd netwerk zoals Bitcoin vanwege hun centraliserende effecten.


Een aanpak die veel te weinig waardering krijgt is wat we *inward scaling* kunnen noemen, wat zich vertaalt in "meer doen met minder". Het verwijst naar het voortdurende werk dat veel ontwikkelaars doen om de algoritmen die er al zijn te optimaliseren, zodat we meer kunnen doen binnen de bestaande grenzen van het systeem.


De verbeteringen die zijn bereikt door naar binnen te schalen zijn op zijn zachtst gezegd indrukwekkend. Om je een algemeen idee te geven van de verbeteringen door de jaren heen, Jameson Lopp [heeft benchmark tests](https://blog.lopp.net/Bitcoin-core-performance-evolution/) uitgevoerd op Blockchain synchronisatie, waarbij veel verschillende versies van Bitcoin Core zijn vergeleken, teruggaand tot versie 0.8.


![](assets/Bitcoin-Core-Sync-Performance-1.webp)


Initiële blokdownloadprestaties van verschillende versies van Bitcoin Core. Op de Y-as staat de gesynchroniseerde blokhoogte en op de X-as de tijd die het duurde om die hoogte te bereiken


De verschillende lijnen staan voor verschillende versies van Bitcoin Core. De meest linkse lijn is de nieuwste, versie 0.22, die in september 2021 werd uitgebracht en er 396 minuten over deed om volledig te synchroniseren. De meest rechtse is versie 0.8 uit november 2013, die er 3452 minuten over deed. Al deze - ruwweg 10x - verbetering is te danken aan naar binnen schalen.


De verbeteringen kunnen worden gecategoriseerd als het besparen van ruimte (RAM, schijf, bandbreedte, etc.) of het besparen van rekenkracht. Beide categorieën dragen bij aan de verbeteringen in het bovenstaande diagram.


Een goed voorbeeld van rekenkundige verbetering is te vinden in de bibliotheek [libsecp256k1](https://github.com/Bitcoin-core/secp256k1), die onder andere de cryptografische primitieven implementeert die nodig zijn om digitale handtekeningen te maken en te verifiëren. Pieter Wuille is een van de bijdragers aan deze bibliotheek en hij schreef een [Twitter thread](https://twitter.com/pwuille/status/1450471673321381896) die de prestatieverbeteringen laat zien die zijn bereikt door verschillende pull requests.


![](assets/libsecp256k1speedups.webp)


Prestaties van handtekeningverificatie in de loop der tijd, met significante pull requests gemarkeerd op de tijdlijn


De grafiek toont de trend voor twee verschillende 64-bits CPU-typen, namelijk ARM en x86. Het verschil in prestaties komt door de meer gespecialiseerde instructies die beschikbaar zijn op x86 in vergelijking met de ARM-architectuur, die minder en meer generieke instructies heeft. De algemene trend is echter hetzelfde voor beide architecturen. Merk op dat de Y-as logaritmisch is, waardoor de verbeteringen minder indrukwekkend lijken dan ze in werkelijkheid zijn.


Er zijn ook verschillende goede voorbeelden van ruimtebesparende verbeteringen die bijdroegen aan prestatieverbetering. In een

[Medium blog post](https://murchandamus.medium.com/2-of-3-Multisig-inputs-using-Pay-to-Taproot-d5faf2312ba3) over de bijdrage van Taproot aan het besparen van ruimte, gebruiker Murch vergelijkt hoeveel blokruimte een 2-van-3 drempel handtekening zou vereisen, waarbij Taproot op verschillende manieren wordt gebruikt en helemaal niet wordt gebruikt.


![](assets/murch-taproot.webp)


Ruimtebesparing voor verschillende typen uitgaven, Taproot en oudere versies.


Een 2-of-3 Multisig met native SegWit zou in totaal 104,5+43 vB = 147,5 vB vereisen, terwijl het meest ruimtebesparende gebruik van Taproot slechts 57,5+43 vB = 100,5 vB zou vereisen in het standaard gebruik. In het slechtste geval en in zeldzame gevallen, zoals wanneer een standaard ondertekenaar om een of andere reden niet beschikbaar is, zou Taproot 107,5+43 vB = 150,5 vB gebruiken. Je hoeft niet alle details te begrijpen, maar dit zou je een idee moeten geven van hoe ontwikkelaars denken over ruimtebesparing - elke kleine byte telt.


Afgezien van binnenwaartse schaalvergroting in Bitcoin software, zijn er ook enkele manieren waarop gebruikers kunnen bijdragen aan binnenwaartse schaalvergroting. Ze kunnen hun transacties intelligenter maken om te besparen op transactiekosten en tegelijkertijd hun voetafdruk op de Full node vereisten verminderen. Twee veelgebruikte technieken om dit doel te bereiken, heten transaction batching en output consolidation.


Het idee achter transaction batching is om meerdere betalingen te combineren in één enkele transactie, in plaats van één transactie per betaling. Dit kan je veel kosten besparen en tegelijkertijd de belasting van de blokruimte verminderen.


![](assets/tx-batching.webp)


Transaction batching combineert meerdere betalingen in één transactie om kosten te besparen.


Consolidatie van uitvoer verwijst naar het profiteren van perioden met weinig vraag naar blokruimte om meerdere uitvoer te combineren tot één uitvoer. Dit kan je kosten later verlagen, wanneer je een betaling moet doen terwijl de vraag naar blokruimte hoog is.


![](assets/utxo-consolidation.webp)


Consolidatie van uitvoer: Smelt je munten samen in één grote munt wanneer de kosten laag zijn om later kosten te besparen.


Het is misschien niet duidelijk hoe consolidatie van de uitvoer bijdraagt aan naar binnen schalen. De totale hoeveelheid Blockchain gegevens wordt met deze methode immers zelfs iets groter. Niettemin krimpt de UTXO set, d.w.z. de database die bijhoudt wie welke munten bezit, omdat je meer UTXO's uitgeeft dan je creëert. Dit verlicht de last voor volledige knooppunten om hun UTXO sets te onderhouden.


Helaas kunnen deze twee technieken van *UTXO beheer* echter slecht zijn voor je eigen privacy of die van je begunstigden. In het geval van batching zal elke begunstigde weten dat alle gebatchte outputs van jou naar andere begunstigden gaan (behalve mogelijk de wijziging). In het geval van UTXO consolidatie, zal je onthullen dat de outputs die je consolideert tot dezelfde Wallet behoren. Het kan dus zijn dat je een afweging moet maken tussen kostenefficiëntie en privacy.


#### Gelaagd schalen



De meest impactvolle benadering van schalen is waarschijnlijk layering. Het algemene idee achter layering is dat een protocol betalingen tussen gebruikers kan afhandelen zonder transacties toe te voegen aan de Blockchain.


Een gelaagd protocol begint met twee of meer mensen die het eens zijn over een starttransactie die op de Blockchain wordt gezet, zoals geïllustreerd in de afbeelding hieronder.


![](assets/scaling-layer.webp)

Een typisch Layer 2 protocol bovenop Bitcoin, Layer 1.


Hoe deze starttransactie tot stand komt verschilt per protocol, maar een gemeenschappelijk thema is dat de deelnemers een niet-ondertekende starttransactie en een aantal vooraf ondertekende straftransacties creëren, die de uitvoer van de starttransactie op verschillende manieren uitgeven. Vervolgens wordt de starttransactie volledig ondertekend en gepubliceerd naar de Blockchain, en de straftransacties kunnen volledig ondertekend en gepubliceerd worden om een zich misdragende partij te straffen. Dit stimuleert de deelnemers om zich aan hun beloften te houden, zodat het protocol op een Trustless manier kan werken.


Zodra de starttransactie op de Blockchain staat, kan het protocol doen wat het moet doen. Het zou bijvoorbeeld supersnelle betalingen tussen deelnemers kunnen doen, wat privacyverbeterende technieken kunnen implementeren, of meer geavanceerde scripts kunnen uitvoeren die niet door de Bitcoin Blockchain worden ondersteund.


We zullen niet in detail treden hoe specifieke protocollen werken, maar zoals je in de vorige figuur kunt zien, wordt de Blockchain zelden gebruikt tijdens de levenscyclus van het protocol. Alle sappige actie gebeurt *off-chain*. We hebben gezien hoe dit een voordeel kan zijn voor privacy als het goed gedaan wordt, maar het kan ook een voordeel zijn voor schaalbaarheid.


In een [Reddit post](https://www.reddit.com/r/Bitcoin/comments/438hx0/a_trip_to_the_moon_requires_a_rocket_with/) getiteld "Een reis naar de maan vereist een raket met meerdere trappen anders eet de raketvergelijking je lunch op... iedereen in clown-auto stijl in een trebuchet inpakken en hopen op succes is uit den boze.", legt Gregory Maxwell uit waarom gelaagdheid onze beste kans is om Bitcoin op schaal te krijgen met ordes van grootte.


Hij begint met het benadrukken van de denkfout in het zien van Visa of Mastercard als Bitcoin's belangrijkste concurrenten en benadrukt hoe het vergroten van de maximale blokgrootte een slechte aanpak is om deze concurrentie het hoofd te bieden. Daarna praat hij over hoe je echt verschil kunt maken door lagen te gebruiken:


> Betekent dit dat Bitcoin geen grote winnaar kan zijn als betalingstechnologie? Nee. Maar om de capaciteit te bereiken die nodig is om aan de betalingsbehoeften van de wereld te voldoen, moeten we intelligenter werken.
>

> Vanaf het begin is Bitcoin ontworpen om lagen op een veilige manier in te bouwen door middel van de slimme contracteringsmogelijkheid (Wat, denk je dat dit er alleen maar in is gestopt zodat mensen konden wax-filosoferen over betekenisloze "DAO's"?). In feite zullen we het Bitcoin systeem gebruiken als een zeer toegankelijke en perfect betrouwbare robotrechter en het grootste deel van onze zaken buiten de rechtszaal afhandelen - maar op zo'n manier dat als er iets fout gaat, we al het bewijs en de gemaakte afspraken hebben, zodat we erop kunnen vertrouwen dat de robotrechter het goed zal maken. (Geek sidebar: Als dit onmogelijk lijkt, lees dan deze oude post over het doorsnijden van transacties)
>

> Dit is mogelijk vanwege de kerneigenschappen van Bitcoin. Een censureerbaar of omkeerbaar basissysteem is niet erg geschikt om krachtige bovenste Layer transactieverwerking op te bouwen... en als de onderliggende waarde niet deugdelijk is, heeft het weinig zin om er überhaupt transacties mee te doen.

De analogie met de rechter is heel illustratief voor hoe lagen werken: deze rechter moet onomkoopbaar zijn en nooit van gedachten veranderen, anders zullen de lagen boven Bitcoin's basis Layer niet betrouwbaar werken.


Hij vervolgt met een opmerking over gecentraliseerde diensten. Er is meestal geen probleem met het vertrouwen op een centrale server met triviale hoeveelheden Bitcoin om dingen gedaan te krijgen: dat is ook gelaagd schalen.


Er zijn al heel wat jaren verstreken sinds Maxwell het stuk hierboven schreef, en zijn woorden zijn nog steeds correct. Het succes van de Lightning Network bewijst dat layering inderdaad een manier is om het nut van de Bitcoin te vergroten.



### Conclusie over schalen



We hebben verschillende manieren besproken waarop men Bitcoin zou willen schalen, de gebruikscapaciteit van Bitcoin zou willen verhogen. Het schalen van Bitcoin is al sinds het prille begin een punt van zorg.


We weten nu dat Bitcoin niet goed verticaal ("koop grotere hardware") of horizontaal ("verifieer alleen delen van de data") schaalt, maar eerder naar binnen ("doe meer met minder") en in lagen ("bouw protocollen bovenop Bitcoin").


## Als er stront aan de knikker is

<chapterId>fe39c13c-310f-51fd-84ff-6b92dd01c9e7</chapterId>



![](assets/shtf-banner.webp)

Bitcoin wordt gebouwd door mensen. Mensen schrijven de software en mensen draaien deze software. Wanneer een beveiligingslek of een ernstige bug wordt ontdekt - is er echt een onderscheid tussen die twee? - wordt het altijd ontdekt door mensen van vlees en bloed. Dit hoofdstuk gaat over wat mensen doen, zouden moeten doen en niet zouden moeten doen wanneer er stront aan de knikker is. Het eerste deel legt de term *verantwoorde openbaarmaking* uit, die verwijst naar hoe iemand die een kwetsbaarheid ontdekt verantwoordelijk kan handelen om de schade ervan te beperken. De rest van het hoofdstuk neemt je mee op een tour langs enkele van de ernstigste kwetsbaarheden die door de jaren heen ontdekt zijn en hoe ze behandeld werden door ontwikkelaars, miners en gebruikers. In de vroege kinderjaren van Bitcoin waren de dingen niet zo rigoureus als vandaag.


### Verantwoordelijke openbaarmaking



Stel je voor dat je een bug ontdekt in Bitcoin Core, een bug die iedereen in staat stelt om op afstand een Bitcoin Core node uit te schakelen door gebruik te maken van enkele speciaal gemaakte netwerkberichten. Stel je ook voor dat je niet kwaadaardig bent en wilt dat dit probleem ongebruikt blijft. Wat doe je dan? Als je erover zwijgt, zal iemand anders het probleem waarschijnlijk ontdekken en je kunt er niet zeker van zijn dat die persoon niet kwaadaardig zal zijn.


Wanneer een beveiligingsprobleem wordt ontdekt, moet de persoon die het ontdekt _responsible disclosure_ toepassen, een term die vaak wordt gebruikt onder Bitcoin ontwikkelaars. De term is [uitgelegd op Wikipedia] (https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure):


> Ontwikkelaars van hardware en software hebben vaak tijd en middelen nodig om hun fouten te herstellen. Vaak zijn het ethische hackers die deze fouten vinden
kwetsbaarheden. Hackers en computerbeveiligingswetenschappers zijn van mening dat het hun sociale verantwoordelijkheid is om het publiek bewust te maken van kwetsbaarheden. Het verbergen van problemen kan een gevoel van schijnveiligheid veroorzaken. Om dit te voorkomen, stemmen de betrokken partijen af en onderhandelen ze over een redelijke termijn om de kwetsbaarheid te verhelpen. Afhankelijk van de potentiële impact van de kwetsbaarheid, de verwachte tijd die nodig is om een noodoplossing of workaround te ontwikkelen en toe te passen en andere factoren, kan deze periode variëren van enkele dagen tot enkele maanden.


Dit betekent dat als je een beveiligingsprobleem vindt, je dit moet melden aan het team dat verantwoordelijk is voor het systeem. Maar wat betekent dit in de context van Bitcoin? Niemand beheert Bitcoin, maar er is momenteel een centraal punt voor de ontwikkeling van Bitcoin, namelijk de [Bitcoin Core Github repository] (https://github.com/Bitcoin/Bitcoin). De beheerders van dit repository zijn verantwoordelijk voor de code die erin staat, maar ze zijn niet verantwoordelijk voor het systeem als geheel - dat is niemand. Desondanks is het de beste gewoonte om een e-mail te sturen naar security@bitcoincore.org.


In een [email thread] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/015002.html) met de titel "Responsible disclosure of bugs" uit 2017, probeerde Anthony Towns samen te vatten wat hij zag als de huidige best practices. Hij had input verzameld van verschillende bronnen en verschillende mensen om zijn visie op het onderwerp te onderbouwen.




- Kwetsbaarheden moeten worden gerapporteerd via security at bitcoincore.org
- Een kritiek probleem (dat onmiddellijk kan worden uitgebuit of al wordt uitgebuit en grote schade veroorzaakt) wordt aangepakt door:
  - zo snel mogelijk een vrijgegeven patch
  - brede kennisgeving van de noodzaak om te upgraden (of om aangetaste systemen uit te schakelen)
  - minimale onthulling van het werkelijke probleem, om aanvallen te vertragen
- Een niet-kritieke kwetsbaarheid (omdat het moeilijk of duur is om uit te buiten) wordt aangepakt door:
  - patch en beoordeling uitgevoerd in de gewone ontwikkelingsstroom
  - backport van een fix of workaround van master naar de huidige vrijgegeven versie
- Ontwikkelaars zullen proberen ervoor te zorgen dat de publicatie van de fix de aard van de kwetsbaarheid niet onthult door de voorgestelde fix aan ervaren ontwikkelaars te geven die niet op de hoogte zijn van de kwetsbaarheid, hen te vertellen dat het een kwetsbaarheid verhelpt en hen te vragen de kwetsbaarheid te identificeren.
- Ontwikkelaars kunnen andere Bitcoin implementaties aanbevelen om kwetsbaarheden te verhelpen voordat de oplossing wordt vrijgegeven en op grote schaal wordt toegepast, als ze dit kunnen doen zonder de kwetsbaarheid te onthullen; bijvoorbeeld, als de oplossing significante prestatievoordelen heeft die de opname rechtvaardigen.
- Voordat een kwetsbaarheid openbaar wordt, zullen ontwikkelaars over het algemeen aan bevriende Altcoin ontwikkelaars aanraden om de fixes in te halen. Maar dit gebeurt pas nadat de fixes op grote schaal zijn uitgerold in het Bitcoin netwerk.
- Over het algemeen zullen ontwikkelaars Altcoin niet op de hoogte brengen als ze zich vijandig gedragen (bijvoorbeeld kwetsbaarheden gebruiken om anderen aan te vallen of embargo's schenden).
- Bitcoin ontwikkelaars zullen geen details over kwetsbaarheden vrijgeven totdat >80% van de Bitcoin knooppunten de fixes hebben toegepast. Ontdekte kwetsbaarheden worden aangemoedigd en verzocht om hetzelfde beleid te volgen. [1] [6]


Deze lijst laat zien hoe voorzichtig men moet zijn bij het publiceren van patches voor Bitcoin, omdat de patch zelf de kwetsbaarheid zou kunnen verraden. De vierde bullet is vooral interessant omdat deze uitlegt hoe je kunt testen of een patch goed genoeg is vermomd. Inderdaad, als een paar echt ervaren ontwikkelaars de kwetsbaarheid niet kunnen ontdekken, zelfs als ze weten dat de patch er een verhelpt, zal het waarschijnlijk echt Hard zijn voor anderen om het te ontdekken.


De thread die leidde tot deze e-mail ging over de vraag of, wanneer en hoe kwetsbaarheden van altcoins en andere implementaties van Bitcoin openbaar gemaakt moeten worden. Er is hier geen duidelijk antwoord. "De goeden helpen" lijkt verstandig, maar wie bepaalt wie dat zijn en waar ligt de grens? Bryan Bishop [betoogde](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014983.html) dat het helpen van altcoins en zelfs scamcoins om zich te verdedigen tegen beveiligingsproblemen een morele plicht is:


> Het is niet genoeg om Bitcoin en haar gebruikers te verdedigen tegen actieve bedreigingen, er is een meer algemene verantwoordelijkheid om alle soorten gebruikers en verschillende software te verdedigen tegen vele soorten bedreigingen in welke vorm dan ook, zelfs als mensen domme en onveilige software gebruiken die je persoonlijk niet onderhoudt of waar je niet aan bijdraagt of voor pleit. Omgaan met kennis over een kwetsbaarheid is een delicate zaak en je zou kennis kunnen ontvangen met ernstiger directe of indirecte gevolgen dan oorspronkelijk beschreven.

Ook in de aanloop naar Town's e-mail hierboven was een [post](https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2017-September/014977.html) van Gregory Maxwell, waarin hij betoogde dat beveiligingsproblemen ernstiger kunnen zijn dan ze lijken:


> Ik heb meerdere keren gezien dat een Hard te misbruiken probleem triviaal bleek te zijn als je de juiste truc vond, of dat een klein dos probleem veel ernstiger bleek te zijn.
>

> Eenvoudige prestatie bugs, vakkundig ingezet, kunnen mogelijk gebruikt worden om het netwerk op te delen-- Miner A en Exchange B gaan in één partitie, alle anderen in een andere... en dubbelspelen.
>

> En ga zo maar door.  Dus hoewel ik het er absoluut mee eens ben dat verschillende dingen verschillend moeten en kunnen worden behandeld, is het niet altijd zo duidelijk. Het is verstandig om dingen als ernstiger te behandelen dan je weet dat ze zijn.

Dus zelfs als een kwetsbaarheid Hard lijkt om uit te buiten, kan het het beste zijn om aan te nemen dat het gemakkelijk uit te buiten is en dat je er alleen nog niet achter bent hoe.


Hij zegt ook dat "het enigszins onjuist is om deze thread iets over openbaarmaking te noemen, deze thread gaat niet over openbaarmaking. Openbaarmaking is wanneer je het de verkoper vertelt.  Deze thread gaat over openbaarmaking en dat heeft heel andere implicaties. Openbaarmaking is wanneer je zeker weet dat je het de potentiële aanvallers hebt verteld". Deze laatste opmerking over het onderscheid tussen openbaarmaking en publicatie is een belangrijke. Het makkelijke deel is verantwoordelijke openbaarmaking; het Hard deel is verstandig publiceren.


### Bitcoin's traumatische jeugd



Bitcoin begon als een eenmansproject (dat is tenminste wat het pseudoniem van de maker suggereert) en Bitcoin had aanvankelijk weinig tot geen waarde. Daarom werden kwetsbaarheden en bugfixes niet zo rigoureus behandeld als tegenwoordig.


De Bitcoin wiki heeft een [lijst van gemeenschappelijke kwetsbaarheden en blootstellingen](https://en.Bitcoin.it/wiki/Common_Vulnerabilities_and_Exposures) (CVE's) die Bitcoin heeft doorlopen. Dit gedeelte is een kleine uiteenzetting van enkele beveiligingsproblemen en incidenten uit de beginjaren van Bitcoin. We zullen ze niet allemaal behandelen, maar we hebben er een paar uitgekozen die we bijzonder interessant vinden.


#### 2010-07-28: Geef iemands munten uit (CVE-2010-5141)



Op 28 juli 2010 ontdekte een pseudonieme persoon met de naam ArtForz een bug in versie 0.3.4 waardoor iedereen munten van iemand anders kon afpakken. ArtForz *verantwoordelijk* rapporteerde dit aan Satoshi Nakamoto en aan een andere Bitcoin ontwikkelaar genaamd Gavin Andresen.


Het probleem was dat de scriptoperator `OP_RETURN` de programma-uitvoering gewoon zou afsluiten, dus als de scriptPubKey `<pubkey> OP_CHECKSIG` was en scriptSig was `OP_1 OP_RETURN`, zou het deel van het programma in de scriptPubKey nooit worden uitgevoerd. Het enige dat zou gebeuren is dat `1` op de stack wordt gezet en dat `OP_RETURN` ervoor zorgt dat het programma wordt afgesloten. Elke waarde op de stack die niet nul is nadat het programma is uitgevoerd, betekent dat aan de bestedingsvoorwaarde is voldaan. Aangezien het bovenste stackelement `1` niet nul is, zou het uitgeven OK zijn.


Dit was de code voor de afhandeling van `OP_RETURN`:


```
case OP_RETURN:
{
pc = pend;
}
break;
```

Het effect van `pc = pend;` was dat de rest van het programma werd overgeslagen, wat betekende dat elk vergrendelingsscript in scriptPubKey zou worden genegeerd. De oplossing bestond uit het veranderen van de betekenis van `OP_RETURN` zodat het in plaats daarvan direct mislukte.


```
case OP_RETURN:
{
return false;
}
break;
```


Satoshi maakte deze wijziging lokaal en bouwde er een uitvoerbare binary met versie 0.3.5 van. Vervolgens postte hij op het Bitcointalk-forum `AlERT 🬁 Upgrade naar 0.3.5 ASAP`, waarbij hij gebruikers aanspoorde om deze binaire versie van hem te installeren, zonder de broncode ervan te laten zien:


> Upgrade alsjeblieft zo snel mogelijk naar 0.3.5!  We hebben een implementatie bug gerepareerd waarbij het mogelijk was dat valse transacties geaccepteerd konden worden.  Accepteer geen Bitcoin transacties als betaling totdat je upgrade naar versie 0.3.5!

Het oorspronkelijke bericht werd later bewerkt en is niet meer in zijn volledige vorm beschikbaar. Het bovenstaande fragment komt uit een [citeer antwoord] (https://bitcointalk.org/index.php?topic=626.msg6458#msg6458). Sommige gebruikers probeerden Satoshi's binary, maar kregen er problemen mee. Kort daarna schreef [Satoshi](https://bitcointalk.org/index.php?topic=626.msg6469#msg6469):


> Ik heb nog geen tijd gehad om de SVN bij te werken.  Wacht op 0.3.6, die ben ik nu aan het bouwen.  Je kunt in de tussentijd je node afsluiten.

En 35 minuten later, [schreef hij](https://bitcointalk.org/index.php?topic=626.msg6480#msg6480):


> SVN is bijgewerkt met versie 0.3.6.
>

> Windows build van 0.3.6 wordt nu geüpload naar Sourceforge, daarna wordt linux herbouwd.

Op dit punt leek hij ook de originele post te hebben bijgewerkt om 0.3.6 te vermelden in plaats van 0.3.5:


> Upgrade alsjeblieft zo snel mogelijk naar 0.3.6!  We hebben een implementatie bug gerepareerd waarbij het mogelijk was dat valse transacties konden worden weergegeven als geaccepteerd.  Accepteer geen Bitcoin transacties als betaling totdat je upgrade naar versie 0.3.6!
>

> Als je niet meteen kunt upgraden naar 0.3.6, kun je het beste je Bitcoin knooppunt afsluiten totdat je dat gedaan hebt.
>

> Ook in 0.3.6, snellere hashing:
> - midstate cache optimalisatie dankzij tcatm
> - Crypto++ ASM SHA-256 dankzij BlackEye
> Totale generatorsnelheid 2,4x sneller.
>

> Downloaden:
>

> http://sourceforge.net/projects/Bitcoin/files/Bitcoin/Bitcoin-0.3.6/
>

> Windows- en Linux-gebruikers: als je 0.3.5 hebt, moet je nog steeds upgraden naar 0.3.6.

Let op het verschil in karakterisering van het probleem met het eerste bericht: "zou kunnen worden weergegeven als geaccepteerd" vs "zou kunnen worden geaccepteerd". Misschien bagatelliseerde Satoshi de ernst van de bug in zijn communicatie om niet teveel aandacht te vestigen op het eigenlijke probleem. Hoe dan ook, mensen hebben een upgrade naar 0.3.6 uitgevoerd en het werkte zoals verwacht. Dit specifieke probleem werd opgelost, verbazingwekkend genoeg, zonder Bitcoin verliezen.


Het bericht van Satoshi beschreef ook een optimalisatie van de prestaties voor Mining. Het is onduidelijk waarom dat was opgenomen in een kritieke beveiligingsoplossing, het is mogelijk dat het doel was om het echte probleem te verdoezelen. Het lijkt echter waarschijnlijker dat hij gewoon uitbracht wat er aan het hoofd stond van de ontwikkelingstak van het Subversion repository, met de beveiligingsfix eraan toegevoegd.


In die tijd waren er lang niet zoveel gebruikers als nu en de waarde van Bitcoin was bijna nul. Als deze reactie op bugs vandaag de dag zou plaatsvinden, zou het om meerdere redenen als een complete shit-show worden beschouwd:



- Satoshi maakte een binaire release van 0.3.5 met de fix. Er werd geen patch of code meegeleverd, misschien om het probleem te verdoezelen.
- 0.3.5 [werkte niet eens] (https://bitcointalk.org/index.php?topic=626.msg6455#msg6455).
- De fix in 0.3.6 was eigenlijk een Hard Fork.


Een andere discutabele kwestie is of het goed of slecht is dat gebruikers werd gevraagd om hun nodes af te sluiten. Dit zou vandaag de dag niet meer mogelijk zijn, maar in die tijd volgden veel gebruikers actief de forums voor updates en zaten ze meestal bovenop de dingen. Gezien het feit dat het mogelijk was om dit te doen, was het misschien verstandig om te doen.


#### 2010-08-15 Gecombineerde uitvoeroverloop (CVE-2010-5139)



Midden augustus 2010 maakte Bitcointalk-forumgebruiker jgarzik, ook bekend als Jeff Garzik,

[ontdekte dat](https://bitcointalk.org/index.php?topic=822.msg9474#msg9474) een bepaalde transactie op blokhoogte 74638 twee uitgangen had met een ongewoon hoge waarde:


```
"out" : [
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0xB7A73EB128D7EA3D388DB12418302A1CBAD5E890 OP_EQUALVERIFY OP_CHECKSIG"
},
{
"value" : 92233720368.54277039,
"scriptPubKey" : "OP_DUP OP_HASH160 0x151275508C66F89DEC2C5F43B6F9CBE0B5C4722C OP_EQUALVERIFY OP_CHECKSIG"
}
]
```


> De "value out" in dit blok #74638 is nogal vreemd:
>

> 92233720368.54277039 BTC?  Is dat UINT64_MAX, vraag ik me af?

Vermoedelijk was er een bug waardoor de som van twee int64 (niet uint64, zoals Garzik veronderstelde) uitgangen overliep naar een negatieve waarde -0.00997538 BTC. Wat de som van de ingangen ook was, de "som" van de uitgangen zou kleiner zijn, waardoor deze transactie OK was volgens de toenmalige code.


In dit geval was de bug onthuld en gepubliceerd via een echte exploit. Een ongelukkige uitkomst hiervan was dat er ongeveer 2x92 miljard Bitcoin waren gecreëerd, waardoor het geld Supply van ongeveer 3,7 miljoen munten dat op dat moment bestond, ernstig werd verdund.


In een verwante thread postte [Satoshi](https://bitcointalk.org/index.php?topic=823.msg9531#msg9531) dat hij het op prijs zou stellen als mensen zouden stoppen met Mining (of *genereren*, zoals ze het toen noemden):


> Het zou helpen als mensen stoppen met genereren.  We zullen waarschijnlijk een nieuwe branch moeten maken rond de huidige, en hoe minder je generate, hoe sneller dat zal gaan.
>

> Een eerste patch zal in SVN rev 132 zitten.  Deze is nog niet geüpload.  Ik ben eerst wat andere misc veranderingen aan het wegwerken, daarna zal ik de patch hiervoor uploaden.

Zijn plan was om een Soft Fork te maken om transacties zoals hier besproken ongeldig te maken, waardoor de blokken (vooral blok 74638) die zulke transacties bevatten ongeldig werden. Minder dan een uur later committeerde hij een [patch in revisie 132](https://sourceforge.net/p/Bitcoin/code/132/) van het Subversion repository en [postte op het forum](https://bitcointalk.org/index.php?topic=823.msg9548#msg9548) waarin hij beschreef wat gebruikers volgens hem moesten doen:


> Patch is geüpload naar SVN rev 132!
>

> Voor nu, aanbevolen stappen:
> 1) Uitschakelen.
> 2) Download de blk-bestanden van knightmb.  (vervang je blk0001.dat en blkindex.dat bestanden)
> 3) Upgrade.
> 4) Het zou moeten beginnen met minder dan 74000 blokken. Laat het de rest opnieuw downloaden.
>

> Als je de bestanden van knightmb niet wilt gebruiken, zou je gewoon je blk*.dat bestanden kunnen verwijderen, maar het zal het netwerk zwaar belasten als iedereen de hele blokindex in één keer downloadt.
>

> Ik zal binnenkort releases bouwen.

Hij wilde dat mensen blokgegevens konden downloaden van een specifieke gebruiker, namelijk knightmb, die zijn Blockchain had gepubliceerd zoals die op zijn schijf stond, de bestanden blkXXXX.dat en blkindex.dat. De reden om de Blockchain gegevens op deze manier te downloaden, in tegenstelling tot het synchroniseren vanaf nul, was om knelpunten in de netwerkbandbreedte te verminderen.


Dit had een groot nadeel: de gegevens die gebruikers downloadden van knightmb [werden niet geverifieerd door de Bitcoin software] (https://Bitcoin.stackexchange.com/a/113682/69518) bij het opstarten. Het blkindex.dat bestand bevatte de UTXO set en de software accepteerde alle gegevens daarin alsof die al geverifieerd waren. knightmb kon de gegevens manipuleren om zichzelf of iemand anders wat bitcoins te geven.


Opnieuw leken mensen hierin mee te gaan, en de omkering van het ongeldige blok en zijn opvolgers was succesvol. Miners begonnen te werken aan een nieuwe opvolger voor blok [74637](https://Mempool.space/block/0000000000606865e679308edf079991764d88e8122ca9250aef5386962b6e84) en volgens de Timestamp van het blok verscheen er een opvolger om 23:53 UTC, ongeveer 6 uur nadat het probleem was ontdekt. Om 08:10 de volgende dag, op 16 augustus, rond blok 74689, had de nieuwe keten de oude keten ingehaald, daarom gingen alle niet-geüpgraded knooppunten opnieuw samenvoegen om de nieuwe keten te volgen. Dit is de diepste reorg - 52 blokken - in de geschiedenis van Bitcoin.


Vergeleken met de OP_RETURN-kwestie werd deze kwestie iets netter afgehandeld:


- Geen binaire patch-release
- De vrijgegeven software werkte zoals bedoeld
- Nee Hard Fork


Gebruikers werd ook gevraagd om te stoppen met Mining tijdens deze kwestie. We kunnen erover discussiëren of dit een goed idee is of niet, maar stel je voor dat je een Miner bent en je bent ervan overtuigd dat alle blokken bovenop het slechte blok uiteindelijk weggevaagd zullen worden in een diepe reorg: waarom zou je dan middelen verspillen aan Mining gedoemde blokken?


Je zou ook kunnen denken dat het een beetje verdacht is om te doen wat Nakamoto voorstelt en de Blockchain, inclusief de UTXO set, te downloaden van de Hard schijf van een willekeurige gast. Als dat zo is, heb je gelijk: dat is verdacht. Maar gezien de omstandigheden was dit een verstandige noodreactie.


Er is een belangrijk verschil tussen deze zaak en de vorige OP_RETURN zaak: dit probleem werd in het wild uitgebuit en dus kon een fix eenvoudiger worden gemaakt. In het geval van OP_RETURN moesten ze de fix verdoezelen en publieke verklaringen afleggen die niet direct onthulden wat het probleem was.


#### 2013-03-11 Probleem met DB-vergrendelingen 0.7.2 - 0.8.0 (CVE-2013-3220)



In maart 2013 dook een zeer interessante en leerzame kwestie op. Het bleek dat de Blockchain was gesplitst (hoewel het woord "Fork" wordt gebruikt in het onderstaande citaat) na blok 225429. De details van dit incident werden [gerapporteerd in BIP50](https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki). De samenvatting zegt:


> Een blok dat een groter aantal totale transactie-ingangen had dan eerder gezien, werd gemined en uitgezonden. Bitcoin 0.8 knooppunten konden dit aan, maar sommige pre-0.8 Bitcoin knooppunten wezen het af, wat een onverwachte Fork van de Blockchain veroorzaakte. De pre-0.8-incompatibele keten (vanaf hier, de 0.8 keten) had op dat moment ongeveer 60% van de Mining Hash kracht waardoor de splitsing niet automatisch werd opgelost (zoals zou zijn gebeurd als de pre-0.8 keten de 0.8 keten in totaal werk overtrof, waardoor 0.8 knooppunten gedwongen werden zich te reorganiseren naar de pre-0.8 keten).
>

> Om zo snel mogelijk een canonieke keten te herstellen, downgradeerden BTCGuild en Slush hun Bitcoin 0.8 nodes naar 0.7 zodat hun pools ook het grotere blok zouden weigeren. Dit plaatste de meeste hashpower op de keten zonder het grotere blok, waardoor de 0.8 knooppunten uiteindelijk reorganiseerden naar de pre-0.8 keten.

De snelle actie van de Mining pools BTCGuild en Slush was noodzakelijk in deze noodsituatie. Ze waren in staat om de meerderheid van de Hash macht over te hevelen naar de pre-0.8 tak van de splitsing en zo de consensus te herstellen. Dit gaf ontwikkelaars de tijd om een duurzame oplossing te bedenken.


Wat ook erg interessant is in dit probleem is dat versie 0.7.2 incompatibel was met zichzelf, zoals ook het geval was met eerdere versies. Dit wordt uitgelegd in de [Oorzaak sectie van BIP50](https://github.com/Bitcoin/bips/blob/master/bip-0050.mediawiki#root-cause):


> Met de onvoldoende hoge BDB slotconfiguratie was het impliciet een netwerkconsensusregel geworden die de geldigheid van een blok bepaalde (zij het een
inconsistente en onveilige regel, omdat het lockgebruik van knooppunt tot knooppunt kan verschillen).


Kortom, het probleem is dat het aantal databasesloten dat de Bitcoin Core software nodig heeft om een blok te verifiëren niet deterministisch is. Het ene knooppunt kan X sloten nodig hebben, terwijl een ander knooppunt X+1 sloten nodig kan hebben. De knooppunten hebben ook een limiet op het aantal sloten dat Bitcoin kan gebruiken. Als het aantal benodigde sloten de limiet overschrijdt, wordt het blok als ongeldig beschouwd. Dus als X+1 de limiet overschrijdt maar niet X, dan zullen de twee knooppunten de Blockchain splitsen en het oneens zijn over welke tak geldig is.


Naast de onmiddellijke acties die de twee pools ondernamen om de consensus te herstellen, werd gekozen voor de volgende oplossing



- beperk de blokken in termen van zowel grootte als benodigde sloten op versie 0.8.1
- patch oude versies (0.7.2 en enkele oudere) met dezelfde nieuwe regels en verhoog de globale slotlimiet.


Behalve de verhoogde globale slotlimiet in de tweede bullet, werden deze regels tijdelijk geïmplementeerd voor een vooraf bepaalde tijd. Het plan was om deze limieten te verwijderen zodra de meeste knooppunten geüpgraded waren.


Deze Soft Fork verminderde het risico op het mislukken van de consensus dramatisch, en een paar maanden later, op 15 mei, werden de tijdelijke regels gezamenlijk gedeactiveerd in het hele netwerk. Merk op dat deze deactivering in feite een Hard Fork was, maar het was niet controversieel. Bovendien werd het vrijgegeven samen met de voorafgaande Soft Fork, dus mensen die de Soft-forked software draaiden wisten dat er een Hard Fork op zou volgen. Daarom bleef de overgrote meerderheid van de knooppunten in consensus toen Hard Fork geactiveerd werd. Helaas gingen er echter een paar nodes verloren die niet geüpgraded hadden.


Je kunt je afvragen of dit vandaag de dag nog haalbaar zou zijn. Het Mining landschap is tegenwoordig complexer en, afhankelijk van de Hash macht aan elke kant van de splitsing, zou het Hard kunnen zijn om een patch zoals die in BIP50 snel genoeg uit te rollen. Het zou waarschijnlijk Hard zijn om mijnwerkers van de "verkeerde" tak te overtuigen hun blokbeloningen los te laten.


#### BIP66



BIP66 is interessant omdat het het belang benadrukt van:



- goede selectie cryptografie
- verantwoorde openbaarmaking
- inzet zonder de kwetsbaarheid te onthullen
- Mining bovenop geverifieerde blokken


BIP66 was een voorstel om de regels voor handtekeningcoderingen in Bitcoin Script aan te scherpen. De [motivatie](https://github.com/Bitcoin/bips/blob/master/bip-0066.mediawiki#motivation) was om handtekeningen te kunnen parsen met andere software of bibliotheken dan OpenSSL en zelfs recente versies van OpenSSL. OpenSSL is een bibliotheek voor algemene cryptografie die Bitcoin Core op dat moment gebruikte.


Het BIP werd geactiveerd op 4 juli 2015. Hoewel het bovenstaande waar is, lost BIP66 ook een veel ernstiger probleem op dat niet in het BIP wordt genoemd.


##### De kwetsbaarheid



De volledige onthulling van deze kwestie werd op 28 juli 2015 gepubliceerd door Pieter Wuille in een

[e-mail naar de Bitcoin-dev mailinglijst] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-July/009697.html):


> Hallo allemaal,
>

> Ik wil graag een kwetsbaarheid onthullen die ik in september 2014 heb ontdekt en die niet meer kan worden misbruikt toen eerder deze maand de 95% drempel van BIP66 werd bereikt.
>

> Korte beschrijving:
>

> Een speciaal gemaakte transactie zou de Blockchain tussen knooppunten kunnen forken:
>

> - openSSL gebruiken op 32-bits systemen en op 64-bits Windows-systemen
> - openSSL gebruiken op niet-Windows 64-bit systemen (Linux, OSX, ...)
> - sommige niet-OpenSSL codebases gebruiken voor het parsen van handtekeningen

In de e-mail worden verder de details uiteengezet over hoe het probleem werd ontdekt en wat het precies veroorzaakte. Aan het einde geeft hij een tijdlijn van de gebeurtenissen, waarvan we hier een aantal van de belangrijkste herhalen. Sommige daarvan zijn, zoals de figuur hierboven laat zien, al beschreven.


![](assets/bip66-timeline-1.webp)


Tijdlijn van gebeurtenissen rond BIP66. Items in zwart zijn hierboven uitgelegd.


##### Voor ontdekking



Zonder dat iemand op de hoogte was van het probleem, had het opgelost kunnen worden door het nu breed uitgemeten BIP62, wat een voorstel was om de mogelijkheden van transactiemisleiding te verminderen. Een van de voorgestelde wijzigingen in BIP62 was het aanscherpen van de consensusregels voor het coderen van handtekeningen, oftewel "strikte DER codering". Pieter Wuille stelde in juli 2014 enkele aanpassingen aan de BIP voor die het probleem zouden hebben opgelost:


> 2014-jul-18: Om ervoor te zorgen dat de regels voor het coderen van handtekeningen in Bitcoin niet afhankelijk zijn van de specifieke parser van OpenSSL, heb ik het BIP62-voorstel aangepast zodat de strikte eis voor DER-handtekeningen ook geldt voor versie 1-transacties. Op dat moment werden er geen niet-DER-handtekeningen meer gemined in blokken, dus werd aangenomen dat dit geen invloed zou hebben. Zie https://github.com/Bitcoin/bips/pull/90 en http://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2014-July/006299.html. Destijds onbekend, maar als dit zou worden toegepast, zou de kwetsbaarheid zijn opgelost.

Vanwege de breedte van deze BIP, die aanzienlijk meer omvatte dan alleen "strikte DER-codering", werd deze voortdurend gewijzigd en kwam hij nooit in de buurt van implementatie. De BIP werd later teruggetrokken omdat Segregated Witness, BIP141, de vervormbaarheid van transacties op een andere en completere manier oploste.


##### Na ontdekking



OpenSSL bracht nieuwe versies van hun software uit met patches die, als ze vanaf het begin in Bitcoin werden gebruikt, het probleem zouden hebben opgelost. Echter, het gebruik van elke nieuwe versie van OpenSSL alleen in een nieuwe release van Bitcoin Core zou de zaken erger maken. Gregory Maxwell legt dit uit in een andere [email thread] (https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2015-January/007097.html) in januari 2015:


> Terwijl het voor de meeste toepassingen over het algemeen acceptabel is om sommige handtekeningen gretig te verwerpen, is Bitcoin een consensus systeem waarbij alle deelnemers het over het algemeen eens moeten zijn over de exacte geldigheid of ongeldigheid van de invoergegevens.  In zekere zin is consistentie belangrijker dan "juistheid".
> [...]
> De bovenstaande patches lossen echter slechts één symptoom van het algemene probleem op: vertrouwen op software die niet ontworpen of gedistribueerd is voor consensusgebruik (in het bijzonder OpenSSL) voor consensus-normatief gedrag.  Daarom stel ik, als een incrementele verbetering, een gerichte Soft-Fork voor om binnenkort strikte DER-conformiteit af te dwingen, gebruikmakend van een subset van BIP62.

Hij wijst erop dat het gebruik van code die niet bedoeld is voor gebruik in consensus systemen serieuze risico's met zich meebrengt, en stelt voor dat Bitcoin strikte DER codering implementeert. Dit is een duidelijk voorbeeld van het belang van goede selectiecryptografie.


Deze gebeurtenissen zouden je de indruk kunnen geven dat Gregory Maxwell op de hoogte was van de kwetsbaarheid die Pieter Wuille later publiceerde, maar dat hij wilde helpen om een fix binnen te smokkelen die vermomd was als een voorzorgsmaatregel, zonder al te veel aandacht te vestigen op het echte probleem. Dat zou zo kunnen zijn, maar het is puur speculatie.


Vervolgens werd, zoals voorgesteld door Maxwell, BIP66 gemaakt als een subset van BIP62 die alleen strikte DER codering specificeerde. Deze BIP werd blijkbaar breed geaccepteerd en ingezet in juli, hoewel er ironisch genoeg twee Blockchain splitsingen plaatsvonden als gevolg van *validatieloze Mining*. Deze splitsingen worden in de volgende sectie besproken.


![](assets/bip66-timeline-2.webp)


Een belangrijke afgeleide hiervan is dat BIP's min of meer *atomisch* moeten zijn, wat betekent dat ze compleet genoeg moeten zijn om iets nuttigs te bieden of een specifiek probleem op te lossen, maar klein genoeg om brede ondersteuning onder gebruikers mogelijk te maken. Hoe meer dingen je in een BIP stopt, hoe kleiner de kans op acceptatie.


##### Splitsingen door validatie zonder Mining



Helaas eindigde het verhaal van BIP66 daar niet. Toen BIP66 werd geactiveerd, werd het een rommeltje omdat sommige miners de blokken die ze probeerden uit te breiden niet verifieerden. Dit wordt validatieloze Mining genoemd, of SPV-Mining (als in Simplified Payment Verification). Er werd een waarschuwingsbericht verstuurd naar Bitcoin knooppunten met een link naar [een webpagina die het probleem beschrijft] (https://Bitcoin.org/en/alert/2015-07-04-spv-Mining):


> In de vroege ochtend van 4 juli 2015 werd de 950/1000 (95%) drempel bereikt. Kort daarna minde een kleine Miner (deel van de niet-geüpgraded 5%) een ongeldig blok, zoals te verwachten was. Helaas bleek dat ongeveer de helft van het netwerk Hash was zonder volledig gevalideerde blokken (SPV Mining genoemd), en nieuwe blokken bovenop dat ongeldige blok bouwde.

De waarschuwingspagina instrueerde mensen om 30 extra bevestigingen te wachten dan ze normaal zouden doen in het geval ze oudere versies van Bitcoin Core gebruikten.


De bovengenoemde splitsing vond plaats op 2015-07-04 om 02:10 UTC na blokhoogte [363730] (https://Mempool.space/block/000000000000000006a320d752b46b532ec0f3f815c5dae467aff5715a6e579e). Dit probleem werd opgelost om 03:50 dezelfde dag, nadat 6 ongeldige blokken waren gemined. Helaas gebeurde hetzelfde probleem de volgende dag opnieuw, namelijk op 2015-07-05 om 21:50, maar deze keer duurde de ongeldige tak slechts 3 blokken.


![](assets/bip66-timeline-3.webp)

De gebeurtenissen die leidden tot BIP66, de inzet ervan en de nasleep zijn een zeer goede casestudy voor hoe voorzichtig Bitcoin ontwikkelaars moeten zijn. Een paar belangrijke conclusies van BIP66:



- De balans tussen openheid en het niet publiceren van een kwetsbaarheid is delicaat.
- Het uitrollen van fixes voor niet-gepubliceerde kwetsbaarheden is een lastig spelletje.
- Behoudende consensus is Hard.
- Software die niet bedoeld is voor consensus-systemen is over het algemeen riskant.
- BIP's moeten enigszins atomair zijn.


### Conclusie over When Shit Hits The Fan



Bitcoin heeft bugs. Mensen die bugs ontdekken, worden aangemoedigd deze op verantwoorde wijze aan de Bitcoin ontwikkelaars te melden, zodat zij de bug kunnen repareren zonder deze publiekelijk te onthullen. Idealiter kan de bug worden vermomd als een prestatieverbetering, of een ander rookgordijn.


We hebben gekeken naar enkele van de ernstigere problemen die in de loop der jaren zijn opgedoken en hoe ze werden aangepakt. Sommige werden publiekelijk ontdekt door exploits, terwijl andere op verantwoorde wijze openbaar werden gemaakt en konden worden verholpen voordat kwaadwillenden de kans kregen om er misbruik van te maken.


## Discussievragen

<chapterId>91462ca7-f09c-55da-a5b9-3e211de31da5</chapterId>


Deze discussievragen zijn niet alleen een samenvatting van de inhoud van "Ontwikkelingsfilosofie Bitcoin", ze zijn bedoeld om je aan te moedigen om verder onderzoek te doen, dus ga zeker op onderzoek uit.


Je kunt de diepgang van je begrip testen door een [mini-essay](https://www.youtube.com/watch?v=N4YjXJVzoZY) van 100-300 woorden te schrijven door een onderwerp te kiezen uit deze pool met vragen. Als je feedback op je werk wilt, kun je het sturen naar mini-essay@planb.network, we zullen het graag beoordelen.


#### Decentralisatie



- Decentralisatie is Hard. Waarom doen we al dit gedoe om het te laten werken? Kunnen we kiezen voor een hybride aanpak, waarbij sommige onderdelen gecentraliseerd zijn en andere niet?
- Brengt decentralisatie het probleem van dubbele uitgaven met zich mee, of vereist het probleem van dubbele uitgaven decentralisatie? Hoe loste Satoshi het probleem van dubbele uitgaven op?
- In welke aspecten is Bitcoin nog het meest vatbaar voor censuur, en waarom is censuur zo'n slechte zaak? Zijn er argumenten voor censuur?
- Er staat dat Bitcoin zonder toestemming is. Zijn er nog andere betaalmethoden die je als toestemmingsvrij kunt beschouwen?



#### Onbetrouwbaarheid




- Vertrouwensloosheid is vaak een spectrum, niet binair. Welke aspecten van Bitcoin zijn eerder Trustless, en welke hebben meestal een hoger niveau van vertrouwen nodig? Kunnen deze worden verminderd?
- Je wilt een Full node draaien om alle transacties volledig te kunnen valideren. U downloadt Bitcoin Core van https://Bitcoin.org/en/download. Waar heb je vertrouwen geplaatst en waar ben je volledig Trustless?
- Kun je een Trustless systeem bouwen bovenop een vertrouwd systeem?



#### Privacy




- Wat zijn enkele belangrijke voordelen voor een gebruiker als hij een goede privacy behoudt bij interactie met Bitcoin? Wat zijn enkele altruïstische voordelen voor het netwerk?
- Hoe beïnvloedt het hergebruik van adressen je privacy?
- Bitcoin gebruikt een UTXO model, terwijl sommige alternatieve cryptocurrencies een accountmodel gebruiken. Wat zijn de gevolgen van deze keuze voor de privacy?



#### Eindig Supply




- Wat is de relatie tussen de eindige Bitcoin en de muntuitgifte via de Coinbase Transaction? Wat is de relatie tussen de uitgifte van munten en het veiligheidsbudget, en hoe staan deze haaks op elkaar?
- Welke parameters had Satoshi kunnen aanpassen om Bitcoin's Supply limiet te veranderen? Wat zou er veranderen als hij had besloten de Supply te beperken tot 1 miljoen? Wat dacht je van 1 biljoen?
- Waarom pleiten sommige mensen voor een verhoging van Bitcoin Supply? Denkt u dat dit zal gebeuren?


#### Upgraden



- Wat is Speedy Trial en waarom was het nodig om Taproot te activeren?
- Waarom hebben we zo'n hoog percentage miners nodig om te upgraden in een softfork? Waarom is de drempel niet gewoon 51%?



#### Tegenstrijdig denken




- Wat is een sybil-aanval en waarom is een gedecentraliseerd netwerk er zo vatbaar voor?
- Waarom is het belangrijk dat alle spelers in het Bitcoin netwerk - en niet alleen ontwikkelaars - tegendraads denken?



#### Open bron




- Slechts een handjevol beheerders heeft de benodigde GitHub rechten om code samen te voegen in de [Bitcoin Core](https://github.com/Bitcoin/Bitcoin) repository. Is dat niet in strijd met een toestemmingsvrij netwerk?
- Is het open source ontwikkelingsproces gevoelig voor een sybil-aanval? Zo ja, hoe zou u dat tegengaan?
- Wat zijn de voor- en nadelen van het vertrouwen op open source bibliotheken van derden en wat is de aanpak van Bitcoin Core?
- Op welke manieren hebben we meer review nodig dan alleen code review? Hoe bepaal je hoeveel review genoeg is?
- Hoe zorgen we ervoor dat er altijd voldoende mensen met expertise aan Bitcoin werken? Wat gebeurt er als die er niet zijn en hoe beoordelen we hun integriteit en intenties?



#### Schalen




- Er wordt beweerd dat sharding schaalvoordelen biedt ten koste van complexiteit. Waarom zouden we technologische verbeteringen wel of niet aannemen omdat ze moeilijk te begrijpen zijn, zelfs als ze technologisch goed lijken?
- Wat zijn enkele voorbeelden van binnenwaartse schaalmethoden die in Bitcoin worden geïntroduceerd?
- Waarom is verticaal schalen veel moeilijker in een gedecentraliseerd systeem? Hoe zit het met horizontaal schalen?
- We lijken nog lang geen consensus te hebben over hoe we de hele wereld op Bitcoin kunnen laten instappen. Had Satoshi niet op zijn minst een pad moeten bedenken om daar te komen, voordat Mining het eerste blok in 2009 vormde?
- Hoe zou je elk van de volgende punten classificeren (verticaal, horizontaal, naar binnen, of geen schalingstechniek): sharding, toename van de blokgrootte, SegWit, SPV-knooppunten, gecentraliseerde uitwisselingen, Lightning Network, afname van het blokinterval, Taproot, sidechains?



# Laatste Sectie


<partId>4b6ff4ef-b9ea-4c48-b05f-62d41a38fbbb</partId>


## Beoordelingen


<chapterId>d334a837-df46-4989-9cad-8d8779147dbe</chapterId>


<isCourseReview>true</isCourseReview>

## Conclusie


<chapterId>b77ed55c-b13a-430b-a212-37aab527b9e7</chapterId>


<isCourseConclusion>true</isCourseConclusion>