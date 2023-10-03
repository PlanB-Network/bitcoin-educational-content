# En teoretisk introduktion till Lightning Network

Målet med detta material är att ge en teknisk förståelse för Lightning Network.

Välkommen till den spännande världen av Lightning Network, en andra lager för Bitcoin som är både sofistikerad och full av potential. Vi kommer att dyka ner i den tekniska funktionen av denna teknologi, utan att fokusera på specifika handledningar eller användningsscenarier. För att dra nytta av denna utbildning krävs en gedigen förståelse för Bitcoin. Detta är en seriös och koncentrerad upplevelse. Du kan också överväga att parallellt ta kursen LN 202, som ger en mer praktisk inblick i denna utforskning. Förbered dig på en resa som kan förändra din uppfattning om Bitcoin-ekosystemet.

Lycka till med upptäckten!

+++

# Grundläggande principer

## Förstå Lightning Network

![Förstå Lightning Network](https://youtu.be/PszWk046x-I)

Lightning-nätverket är en andra lager betalningsinfrastruktur som bygger på Bitcoin-nätverket och möjliggör snabba och kostnadseffektiva transaktioner. För att fullt ut förstå hur Lightning-nätverket fungerar är det viktigt att förstå vad betalningskanaler är och hur de fungerar.

En betalningskanal på Lightning är en slags "privat väg" mellan två användare som möjliggör snabba och upprepade Bitcoin-transaktioner. När en kanal öppnas har den en fast kapacitet som bestäms i förväg av användarna. Denna kapacitet representerar det maximala beloppet av Bitcoin som kan överföras genom kanalen vid en given tidpunkt.

Betalningskanaler är tvåvägskommunikation, vilket innebär att de har två "sidor". Till exempel, om Alice och Bob öppnar en betalningskanal kan Alice skicka Bitcoin till Bob och Bob kan skicka Bitcoin till Alice. Transaktioner inom kanalen påverkar inte kanalens totala kapacitet, men de påverkar fördelningen av denna kapacitet mellan Alice och Bob.

![förklaring](assets/chapitre1/0.JPG)

För att en transaktion ska vara möjlig i en Lightning-betalningskanal måste användaren som skickar pengarna ha tillräckligt med Bitcoin på sin sida av kanalen. Om Alice vill skicka 1 Bitcoin till Bob genom deras kanal måste hon ha minst 1 Bitcoin på sin sida av kanalen.

Begränsningar och funktioner för betalningskanaler på Lightning.
Även om kapaciteten för en Lightning-betalningskanal är fast begränsar det inte antalet transaktioner eller den totala volymen av Bitcoin som kan överföras genom kanalen. Till exempel, om Alice och Bob har en kanal med en kapacitet på 1 Bitcoin, kan de genomföra hundratals transaktioner på 0,01 Bitcoin eller tusentals transaktioner på 0,001 Bitcoin, så länge den totala kapaciteten för kanalen inte överskrids vid någon given tidpunkt.
Trots dessa begränsningar är Lightning-betalningskanaler ett effektivt sätt att genomföra snabba och billiga Bitcoin-transaktioner. De gör det möjligt för användare att skicka och ta emot Bitcoin utan att behöva betala höga transaktionsavgifter eller vänta länge på bekräftelseperioder i Bitcoin-nätverket.

Sammanfattningsvis erbjuder Lightning-betalningskanaler en kraftfull lösning för dem som vill genomföra snabba och billiga Bitcoin-transaktioner. Det är dock viktigt att förstå hur de fungerar och deras begränsningar för att kunna dra full nytta av dem.

Exempel:

- Alice har 100 000 SAT
- Bob har 30 000 SAT

Detta är det nuvarande tillståndet för kanalen. Vid en transaktion bestämmer sig Alice för att skicka 40 000 SAT till Bob. Hon kan göra det eftersom 40 000 < 100 000.

Det nya tillståndet för kanalen blir då:

- Alice 60 000 SAT
- Bob 70 000 SAT

```
Ursprungligt tillstånd för kanalen:
Alice (100 000 SAT) ============== Bob (30 000 SAT)

Efter att Alice har överfört 40 000 SAT till Bob:
Alice (60 000 SAT) ============== Bob (70 000 SAT)

```

Nu vill Bob skicka 80 000 SAT till Alice. Eftersom han inte har tillräckligt med likviditet kan han inte göra det. Kanalens maximala kapacitet är 130 000 SAT, med en möjlig utgift på upp till 60 000 SAT för Alice och 70 000 SAT för Bob.

## Bitcoin, adresser, UTXO och transaktioner

![bitcoin, adresser, utxo och transaktioner](https://youtu.be/cadCJ2V7zTg)

I det här andra kapitlet tar vi oss tid att studera hur Bitcoin-transaktioner faktiskt fungerar, vilket kommer att vara till nytta för att förstå Lightning. Vi tar också en kort titt på begreppet multi-signaturadress, vilket är avgörande för att förstå nästa kapitel som handlar om att öppna kanaler på Lightning-nätverket.

- Privat nyckel > Offentlig nyckel > Adress: Vid en transaktion skickar Alice pengar till Bob. Bob tillhandahåller en adress som genereras av hans offentliga nyckel. Alice, som själv har fått pengar till en adress via sin offentliga nyckel, använder nu sin privata nyckel för att signera transaktionen och därmed låsa upp bitcoins från adressen.
- Vid en transaktion inom Bitcoin måste alla bitcoins röra sig. Kallad UTXO (Unspend Transaction Output), kommer bitcoin-bitarna att lämna ägaren för att sedan återvända till ägaren själv:
  Alice har 0,002 BTC, Bob har 0 BTC. Alice bestämmer sig för att skicka 0,0015 BTC till Bob. Hon kommer att signera en transaktion på 0,002 BTC där 0,0015 går till Bob och 0,0005 kommer att återgå till hennes plånbok.

![förklaring](assets/chapitre2/0.JPG)

Här har vi en UTXO (Alice har 0,0002 BTC på en adress), så vi har skapat 2 UTXO (Bob har 0,0015 och Alice har fått en ny UTXO (oberoende av den föregående) på 0,0005 BTC).

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

I Lightning Network använder vi multi-signaturer. Det krävs därför 2 signaturer för att låsa upp medlen, det vill säga två privata nycklar för att flytta pengarna. Det kan vara både Alice och Bob som tillsammans måste godkänna att låsa upp pengarna (UTXO). I LN är det specifikt 2/2-transaktioner, så båda signaturerna krävs, till skillnad från multi-signaturer 2/3 eller 3/5 där endast en kombination av det totala antalet nycklar krävs.

![förklaring](assets/chapitre2/1.JPG)

# Öppning och stängning av kanaler

## Öppning av kanal

![öppna en kanal](https://youtu.be/B2caBC0Rxko)

Nu tittar vi närmare på öppningen av en kanal och hur den utförs genom en Bitcoin-transaktion.

Lightning Network har olika kommunikationsnivåer:

- P2P-kommunikation (Lightning Network-protokoll)
- Betalningskanal (Lightning Network-protokoll)
- Bitcoin-transaktion (Bitcoin-protokoll)

![förklaring](assets/chapitre3/0.JPG)

För att öppna en kanal kommunicerar de två noderna via en kommunikationskanal:

- Alice: "Hej, jag vill öppna en kanal!"
- Bob: "Ok, här är min publika adress."

![förklaring](assets/chapitre3/1.JPG)

Alice har nu 2 publika adresser för att skapa en 2/2 multi-signaturadress. Hon kan nu göra en Bitcoin-transaktion för att skicka pengar till den.

Låt oss anta att Alice har en UTXO på 0,002 BTC och vill öppna en kanal med Bob på 0,0013 BTC. Hon kommer då att skapa en transaktion med 2 utgående UTXO:

- en UTXO på 0,0013 till den 2/2 multi-signaturadressen
- en UTXO på 0,0007 till en av hennes växlingsadresser (återbetalning av UTXO).
  Denna transaktion är ännu inte offentlig eftersom om den är det vid detta skede, litar den på Bob för att kunna låsa upp pengarna från multi-sig.
  Men hur gör man då?

Alice kommer att skapa en andra transaktion som kallas "uttags transaktion" innan hon publicerar insättningen av medel i multi-sig.

![förklaring](assets/chapitre3/2.JPG)

Uttags transaktionen kommer att spendera medlen från multi-sig adressen till hennes egen adress (detta innan något är publicerat).

När de två transaktionerna är byggda meddelar hon Bob att det är klart och ber honom om en signatur med sin publika nyckel och förklarar för honom att på så sätt kan hon återfå sina medel om något skulle gå fel. Bob accepterar eftersom han inte är oärlig.

Alice kan därför återfå medlen själv, hon har redan Bobs signatur. Hon publicerar sedan transaktionerna. Kanalen är nu öppen med 0,0013 BTC (130 000 SAT) på Alice sida.

![förklaring](assets/chapitre3/3.JPG)

## Lightning Transaktion & Engagemang

![lightning transaktion & engagemang](https://youtu.be/aPqI34tpypM)

![omslag](assets/chapitre4/1.JPG)

Nu ska vi analysera vad som faktiskt händer bakom kulisserna när vi överför medel från en sida till en annan på Lightning-nätverket, med särskild fokus på begreppet engagemangstransaktion. On-chain uttags/avslutningstransaktionen representerar kanalens tillstånd, vilket garanterar vem som äger medlen efter varje överföring.

Så efter en Lightning-nätverksöverföring uppdateras denna transaktion/kontakt som inte genomförs mellan de två noderna, Alice och Bob skapar därför samma transaktion med den aktuella kanalens tillstånd i händelse av en avslutning:

- Alice skapar en kanal med Bob med 130 000 SAT på hennes sida. Uttags transaktionen, som båda accepterar vid avslutning, säger att 130 000 SAT kommer att gå till Alice vid avslutningen, Bob håller med eftersom det är rättvist.

![omslag](assets/chapitre4/2.JPG)

- Alice skickar 30 000 SAT till Bob. Det finns då en ny uttags transaktion som säger att vid avslutning kommer Alice att få 100 000 SAT och Bob 30 000 SAT. Båda håller med eftersom det är rättvist.

![omslag](assets/chapitre4/3.JPG)

- Alice skickar 10 000 SAT till Bob, en ny uttags transaktion skapas igen för att säga att Alice får tillbaka 90 000 SAT och Bob 40 000 SAT. Båda håller med eftersom det är rättvist.

![omslag](assets/chapitre4/4.JPG)

```
Kanalens initiala tillstånd:
Alice (130 000 SAT) =============== Bob (0 SAT)

Efter den första överföringen:
Alice (100 000 SAT) =============== Bob (30 000 SAT)

Efter den andra överföringen:
Alice (90 000 SAT) =============== Bob (40 000 SAT)

```

Pengarna rör sig aldrig, men den slutliga balansen uppdateras genom en signerad men inte publicerad on-chain-transaktion. Uttagstransaktionen är därför en engagemangstransaktion. Överföringar av satoshis är en annan, mer nyligen uppdaterad engagemangstransaktion som uppdaterar balansen.

## Engagemangstransaktioner

![transaktioner del 2](https://youtu.be/RRvoVTLRJ84)

Om engagemangstransaktionerna dikterar en kanalstatus med likviditet vid tidpunkt X, kan man fuska genom att publicera en äldre och därmed en äldre status? Svaret är ja, eftersom vi redan har förhandsunderskriften från båda deltagarna i den osläppta transaktionen.

![instruktion](assets/Chapitre5/0.JPG)

För att lösa detta problem kommer vi att lägga till komplexitet:

- Timelock = medel blockerade fram till block N
- Återkallelseckel = Alice hemlighet och Bob hemlighet

Dessa två element läggs till i engagemangstransaktionen. Således måste Alice vänta tills Timelock är över, och vem som helst som har återkallelseckeln kan flytta medlen utan att behöva vänta på att Timelock är över. Om Alice försöker fuska använder Bob återkallelseckeln för att stjäla och straffa Alice.

![instruktion](assets/Chapitre5/1.JPG)

Nu (och i verkligheten) är inte engagemangstransaktionen densamma för Alice och Bob, de är symmetriska men med olika begränsningar, de ger varandra sina hemligheter för att skapa återkallelseckeln för den tidigare engagemangstransaktionen. Så vid skapandet skapar Alice kanalen med Bob, 130 000 SAT på hennes sida, hon har en Timelock som hindrar henne från att omedelbart få tillbaka sina pengar, hon måste vänta lite. Återkallelseckeln kan låsa upp pengarna, men bara Alice har den (Alice engagemangstransaktion). När det finns en överföring kommer Alice att ge sin gamla hemlighet till Bob och därmed kan Bob tömma kanalen till det tidigare tillståndet om Alice försöker fuska (Alice blir då straffad).

![instruktion](assets/Chapitre5/2.JPG)

På samma sätt kommer Bob att ge sin hemlighet till Alice. Så att om han försöker fuska kan Alice straffa honom. Operationen upprepas vid varje ny engagemangstransaktion. En ny hemlighet beslutas och en ny återkallelseckel. Så för varje ny transaktion måste den tidigare engagemangstransaktionen förstöras genom att ge återkallelsehemligheten. På så sätt kan om Alice eller Bob försöker fuska, den andra agera först (tack vare Timelock) och undvika fusk. Vid transaktion nr 3 ges därför hemligheten från transaktion nr 2 för att möjliggöra att Alice och Bob kan försvara sig mot Alice eller Bob.

![instruktion](assets/Chapitre5/3.JPG)
Personen som skapar transaktionen med Timelock (den som skickar pengarna) kan endast använda återkallelse nyckeln efter Timelock. Men personen som tar emot pengarna kan använda den före Timelock om det förekommer fusk från den ena sidan till den andra i en kanal på Lightning-nätverket. Specifikt går vi igenom mekanismerna som skyddar mot eventuellt fusk från ens partner i kanalen.

## Stängning av kanal

![stänga en kanal](https://youtu.be/FVmQvNpVW8Y)

Vi är intresserade av att stänga en kanal genom en Bitcoin-transaktion, som kan ta olika former beroende på situationen. Det finns 3 typer av kanalstängningar:

- Den goda: samarbetsvillig stängning
- Den brutala: tvingad stängning (icke-samarbetsvillig)
- Den skurken: stängning av en bedragare

![instruktion](assets/chapitre6/1.JPG)
![instruktion](assets/chapitre6/0.JPG)

### Den goda

De två parterna pratar med varandra och kommer överens om att stänga kanalen. De slutar därför alla transaktioner och bekräftar en slutlig status för kanalen. De kommer överens om nätverksavgifterna (personen som öppnar kanalen betalar stängningsavgifterna). De skapar nu stängningstransaktionen. Det finns alltså en stängningstransaktion, som skiljer sig från engagemangstransaktionerna eftersom det inte finns någon Timelock eller återkallelse nyckel. Transaktionen publiceras och Alice och Bob får sina respektive saldon. Denna typ av stängning är snabb (eftersom det inte finns någon Timelock) och generellt sett inte särskilt kostsam.

![instruktion](assets/chapitre6/3.JPG)

### Den brutala

Alice vill stänga kanalen, hon kommunicerar men Bob svarar inte eftersom han är offline (internetavbrott eller strömavbrott). Alice kommer därför att publicera den senaste engagemangstransaktionen (den sista). Transaktionen publiceras och Timelock aktiveras. Då har avgifterna bestämts vid skapandet av denna transaktion för X tid sedan! MemPool är nätverket som har förändrats sedan dess, protokollet använder som standard avgifter som är 5 gånger högre än de nuvarande vid skapandet av transaktionen. Skapandeavgift på 10 SAT så transaktionen ansåg 50 SAT. Vid tvingad publicering är stängningstransaktionen i nätverket:

- 1 SAT = överbetald med 50\*
- 100 SAT = underbetald med 2\*

Detta gör att den tvingade stängningen tar längre tid (Timelock) och framför allt är mer osäker när det gäller avgifter och därmed möjlig validering av gruvarbetare.

![instruktion](assets/chapitre6/4.JPG)

### Den skurken

Alice försöker fuska genom att publicera en gammal engagemangstransaktion. Men Bob övervakar MemPoolen och väntar på om det finns transaktioner som försöker publicera gamla transaktioner. Om han hittar några använder han återkallelseckeln för att straffa Alice och ta alla SAT från kanalen.
![instruction](assets/chapitre6/5.JPG)

Sammanfattningsvis är stängningen av en kanal i Lightning-nätverket en avgörande fas som kan ske på olika sätt. I en samarbetsvillig stängning kommunicerar båda parterna och kommer överens om en slutlig kanalstatus. Detta är det snabbaste och minst kostsamma alternativet. Å andra sidan sker en tvångsstängning när en av parterna inte svarar. Detta är en dyrare och längre process på grund av oförutsägbara transaktionsavgifter och aktivering av timelock. Slutligen, om en deltagare försöker fuska genom att publicera en gammal engagemangstransaktion, kan bedragaren straffas genom att förlora alla SAT i kanalen. Det är därför viktigt att förstå dessa mekanismer för en effektiv och rättvis användning av Lightning-nätverket.

# Ett likviditetsnätverk

## Lightning-nätverket

![lightning-nätverket](https://youtu.be/RAZAa3v41DM)

I detta sjunde kapitel studerar vi hur Lightning fungerar som ett nätverk av kanaler och hur betalningar routas från källan till destinationen.

Lightning är ett nätverk av betalkanaler. Det är tusentals par med sina likviditetskanaler som är anslutna till varandra och används för att genomföra transaktioner mellan oanslutna par.

![cover](assets/Chapitre7/0.JPG)
![cover](assets/Chapitre7/1.JPG)

Likviditeten i kanalerna kan inte flyttas till andra likviditetskanaler.

`Alice -> Eden -> Bob`. Satoshis har inte flyttats från `Alice -> Bob`, utan från `Alice -> Eden` och från `Eden -> Bob`.

Varje person och kanal har därför olika likviditet. För att genomföra betalningar måste man hitta en rutt i nätverket med tillräckligt med likviditet. Om det saknas likviditet kommer betalningen inte att lyckas.

Låt oss ta följande nätverk som exempel:

```
Initialt tillstånd för nätverket:
Alice (130 SAT) ==== (0 SAT) Susie (90 SAT) ==== (200 SAT) Eden (150 SAT) ==== (100 SAT) Bob
```

![cover](assets/Chapitre7/2.JPG)

Om Alice vill överföra 40 SAT till Bob kommer likviditeten att omfördelas längs rutten mellan de båda parterna.

```
Efter överföringen från Alice till Bob på 40 SAT:
Alice (90 SAT) ==== (40 SAT) Susie (50 SAT) ==== (240 SAT) Eden (110 SAT) ==== (140 SAT) Bob
```

![cover](assets/Chapitre7/4.JPG)
I det ursprungliga tillståndet kan Bob inte skicka 40 SAT till Alice eftersom Susie inte har något likviditet med Alice för att skicka henne 40 SAT, så betalningen är inte möjlig via denna väg. Det behövs därför en annan väg där transaktionen är möjlig.
I det första exemplet kan vi se att varken Susie eller Eden har förlorat eller vunnit något. För att acceptera att användas för att routa transaktionen begär Lightning-noderna avgifter!

Det finns olika avgifter beroende på var likviditeten finns.

Alice - Bob

- Alice avgift = Alice -> Bob
- Bob avgift = Bob -> Alice

![cover](assets/Chapitre7/5.JPG)

Det finns två typer av avgifter:

- en fast avgift oavsett belopp: 1 SAT (standard men kan ändras)
- en variabel avgift (0,01% som standard)

Exempel på avgifter:

- Alice - Susie; 1/1 (1 i fast avgift och 1 i variabel avgift)
- Susie - Eden; 0/200
- Eden - Bob; 1/1

Så:

- Avgift 1: (betald av Alice till sig själv) 1 + (40 000 / \* 0,000001)
- Avgift 2: 0 + 40 000 / \* 0,0002 = 8 SAT
- Avgift 3: 1 + 40 000 / \* 0,000001 = 0,4 SAT

![cover](assets/Chapitre7/6.JPG)

Sändning:

1. Sändning av 40 009,04 Alice -> Susie; Alice betalar sina egna avgifter så det räknas inte
2. Susie utför tjänsten att skicka 40 001,04 till Eden, hon tar sin provision på 8 SAT
3. Eden utför tjänsten att skicka 40 000 till Bob, han tar sina 1,04 SAT i avgift.

Alice har betalat 9,04 SAT i avgifter och Bob har fått 40 000 SAT.

![cover](assets/Chapitre7/7.JPG)

I LN är det alltså Alice-noden som kommer att bestämma rutten innan sändningen. Det finns alltså en sökning efter den bästa rutten och Alice är den enda som känner till rutten och priset. Betalningen skickas men Susie har ingen information.

![cover](assets/Chapitre7/9.JPG)

För Susie eller Eden: de vet inte vem den slutliga mottagaren är eller vem som skickar. Detta är en lök-routing. Noden måste därför ha en plan över nätverket för att hitta sin väg, men ingen av mellanhänderna har någon information.

## HTLC - Hashed Time Locked Contract

![HTLC](https://youtu.be/-JC4mkq7H48)

I ett vanligt routingssystem, hur kan man vara säker på att Eden inte fuskar och följer sin del av kontraktet?

HTLC är därför en betalningskontrakt där man bara kan låsa upp det med en hemlighet. Om hemligheten inte avslöjas löper kontraktet ut. Det är alltså en villkorlig betalning. Hur används de?
Låt oss titta på följande situation:
`Alice (100 000 SAT) ==== (30 000 SAT) Susie (250 000 SAT) ==== (0 SAT) Bob`

- Bob genererar en hemlighet S (preimage) och beräknar hashen r = hash(s)
- Bob skickar en faktura till Alice med "r" som en av detaljerna
- Alice skickar en HTLC på 40 000 SAT till Susie med villkoret att avslöja "s'" så att hash(s') = r
- Susie skickar en liknande HTLC till Bob
- Bob låser upp Susies HTLC genom att visa "s"
- Susie låser upp Alices HTLC genom att visa "S"

Om Bob är offline och aldrig får reda på hemligheten som ger honom rätt att ta emot pengarna, kommer HTLC:en att löpa ut efter ett visst antal block.

HTLC:er löper ut i omvänd ordning: först Susie - Bob och sedan Alice - Susie.
På så sätt spelar det ingen roll om Bob kommer tillbaka. Å andra sidan, om Alice avbryter när Bob kommer tillbaka, blir det kaos och folk kan ha arbetat för ingenting.

Och så, frågan är: vad händer vid avslutning? Faktum är att våra engagemangstransaktioner är ännu mer komplexa. Vi måste representera den mellanliggande balansen om kanalen stängs.

Det finns alltså en HTLC-ut på 40 000 satoshis (med de tidigare begränsningarna) i engagemangstransaktionen via utdata nr 3.

Så Alice har i engagemangstransaktionen:

- Utdata nr 1: 60 000 SAT till Alice via en tidslås och återkallelseckey (vad som är kvar för henne)
- Utdata nr 2: 30 000 som redan tillhör Susie
- Utdata nr 3: 40 000 i HTLC

Alices engagemangstransaktion har en HTLC-ut eftersom hon skickar en HTLC-in till mottagaren, Susie.

Så om vi publicerar denna engagemangstransaktion kan Susie få pengarna från HTLC:en med prebilden "s". Om hon inte har prebilden får Alice pengarna när HTLC:en löper ut. Tänk på utgångarna (UTXO) som olika betalningar med olika villkor.
När betalningen har skett (genom utgång eller utförande) ändras kanalens tillstånd och transaktionen med HTLC:en existerar inte längre. Vi återgår till något mer konventionellt.
Vid samarbetsavslutning: slutar vi betalningarna och väntar på överföringarnas/HTLC:ens utförande, transaktionen är lätt och billig eftersom det bara finns högst 1 eller 2 utdata.

Vid tvångsavslutning: publicerar vi med alla pågående HTLC:er, vilket blir mycket tungt och dyrt. Och det blir kaos.
Sammanfattningsvis använder Lightning Network-routingssystemet Hash Time-Locked Contracts (HTLC) för att säkerställa en säker och verifierbar betalning. HTLC gör det möjligt att genomföra villkorliga betalningar där pengarna endast kan låsas upp med en hemlighet, vilket garanterar att deltagarna uppfyller sina åtaganden. I det presenterade exemplet vill Alice skicka SAT till Bob via Susie. Bob genererar en hemlighet, skapar en hash av den och skickar den till Alice. Alice och Susie upprättar en HTLC baserad på denna hash. När Bob låser upp Susies HTLC genom att visa hemligheten kan Susie sedan låsa upp Alices HTLC.

Om Bob inte avslöjar hemligheten inom en viss tidsram löper HTLC ut. Utgången sker i omvänd ordning, från sista till första, vilket säkerställer att om Bob kommer tillbaka online finns det inga oönskade konsekvenser.

Vid kanalavslutning, om det är ett samarbetsavslut, avbryts betalningarna och HTLC:erna löses, vilket vanligtvis är mindre kostsamt. Om avslutningen är tvingad publiceras alla pågående HTLC-transaktioner, vilket kan bli mycket dyrt och rörigt. Sammanfattningsvis lägger HTLC-mekanismen till ett extra lager av säkerhet i Lightning Network, vilket säkerställer att betalningar utförs korrekt och att användarna uppfyller sina åtaganden.

För att hitta vägen

Den enda offentliga informationen är den totala kapaciteten för kanalen (Alice + Bob), men vi vet inte var likviditeten finns. För att få mer information lyssnar vår nod på LN-kommunikationskanalen för annonser om nya kanaler och uppdateringar av kanalavgifterna. Din nod övervakar också blockkedjan för kanalavslutningar.

Eftersom vi inte har all information måste vi söka efter en graf/rutt med den information vi har (maximal kapacitet för kanaler och inte var likviditeten finns).

Kriterier:

- Sannolikhet för framgång
- Avgifter
- HTLC:ernas utgångsdatum
- Antal mellannoder
- Slumpmässighet

Så om det finns 3 möjliga rutter:

- Alice > 1 > 2 > 5 > Bob
- Alice > 1 > 2 > 4 > 5 > Bob
- Alice 1 > 2 > 3 > Bob

Söker vi den bästa teoretiskt med lägst avgifter och störst chans att lyckas: maximal likviditet och så få hopp som möjligt.

Om till exempel 2-3 bara har en kapacitet på 130 000 SAT, är det mycket osannolikt att skicka 100 000, så alternativ 3 har ingen chans att lyckas.
Från och med nu har algoritmen gjort sina 3 val och kommer nu att prova det första:

Val 1:

- Alice skickar en HTCL till 1 på 100 000 SAT;
- 1 gör en HTLC på 100 000 SAT till 2
- 2 gör en HTLC på 100 000 SAT till 5, men 5 kan inte göra det, så det misslyckas.

Informationen skickas tillbaka så Alice bestämmer sig för att prova den andra rutten:

- Alice skickar en HTLC på 100 000 till 1
- 1 gör en HTLC på 100 000 till 2
- 2 gör en HTLC på 100 000 till 4
- 4 gör en HTLC på 100 000 till Bob. Bob har likviditet så det är okej.
- Bob använder prebilden (hash) av HTLC och använder därför hemligheten för att få tillbaka 100 000 SAT
- 5 har nu hemligheten för HTLC för att få tillbaka den blockerade HTLC från 4
- 4 har nu hemligheten för HTLC för att få tillbaka den blockerade HTLC från 2
- 2 har nu hemligheten för HTLC för att få tillbaka den blockerade HTLC från 1
- 1 har nu hemligheten för HTLC för att få tillbaka den blockerade HTLC från Alice

Alice såg inte misslyckandet med rutten 1, hon väntade bara en sekund till. En betalningsmisslyckande inträffar när det inte finns någon möjlig rutt. För att underlätta sökandet efter en rutt kan Bob ge information till Alice för att hjälpa till med hennes faktura:

- Beloppet
- Hans adress
- Hashen för prebilden så att Alice kan skapa HTLC
- Indikationer om Bobs kanaler

Bob känner till likviditeten i kanalerna 5 och 3 eftersom han är direkt ansluten till dem, han kan informera Alice om det. Han informerar Alice om att nod 3 är onödig, vilket förhindrar Alice från att eventuellt försöka den rutten.
En annan faktor är privata kanaler (alltså inte offentligt tillgängliga i nätverket) som Bob kan ha. Om Bob har en privat kanal med 1 kan han be Alice att använda den, vilket skulle ge Alice > 1 > Bob.

![graf](assets/chapitre9/3.JPG)

Sammanfattningsvis är routing av transaktioner på Lightning-nätverket en komplex process som kräver hänsyn till olika faktorer. Medan den totala kapaciteten för kanalerna är offentlig är den exakta fördelningen av likviditeten inte direkt tillgänglig. Detta tvingar noderna att uppskatta de mest sannolika framgångsrika ruterna, med hänsyn till faktorer som avgifter, HTLC: s utgångsdatum, antalet mellannoder och en slumpfaktor.
När det finns flera möjliga vägar försöker noderna minimera kostnaderna och maximera chanserna till framgång genom att välja kanaler med tillräcklig likviditet och ett minimalt antal hopp. Om en transaktionsförsök misslyckas på grund av otillräcklig likviditet, försöks en annan väg tills en transaktion lyckas.
För att underlätta sökningen efter en väg kan mottagaren tillhandahålla ytterligare information, som adress, belopp, hash för preimage och information om sina kanaler. Detta kan hjälpa till att identifiera kanaler med tillräcklig likviditet och undvika onödiga transaktionsförsök.
I slutändan är Lightning Network:s routing-system utformat för att optimera hastighet, säkerhet och effektivitet för transaktioner samtidigt som användarnas integritet bevaras.

# Verktyg för Lightning Network

## Faktura, LNURL, Keysend

![faktura, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)

![omslag](assets/chapitre10/0.JPG)

En LN-faktura (eller invoice) är lång och inte trevlig att läsa, men den representerar på ett kompakt sätt en betalningsförfrågan.

Exempel:
lnbc1m1pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3

- lnbc1m = läsbar del
- 1 = avskiljare från resten
- Sedan resten
- Bc1 = Bech32-kodning (bas 32), så vi använder 32 tecken.
- 10 = 1.2.3.4.5.6.7.8.9.0
- 26 = abcdefghijklmnopqrstuvwxyz
- 32 = inte "b-i-o" och inte "1"

### lnbc1m

- ln = Lightning
- Bc = bitcoin (huvudnät)
- 1 = belopp
- M = milli (10*-3 / u = mikro 10*-6 / n = nano 10*-9 / p = pico 10*-12

Här betyder 1m = 1 /\* 0.0001btc = 100 000 BTC
"Ombedd att betala 100 000 SAT på bitcoin-huvudnätets Lightning-nätverk till pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3"

### Tidsstämpel (när det skapades)

Den innehåller 0 eller flera ytterligare delar:

- Hash av prebilden
- Betalningshemlighet (lökrouting)
- Godtyckliga data
- Mottagarens LN-offentliga nyckel
- Utgångstid (standard 1 timme)
- Routningsanvisningar
- Signatur för hela innehållet

Det finns andra typer av fakturor. LNURL-metaprotokollet gör det möjligt att ange en direkt summa i satoshis istället för att göra en begäran. Det är mycket flexibelt och möjliggör många förbättringar när det gäller användarupplevelsen.

![omslag](assets/chapitre10/2.JPG)

En Keysend gör det möjligt för Alice att skicka pengar till Bob utan att ha en begäran från Bob. Alice får Bobs ID, skapar en prebild utan att fråga Bob och inkluderar den i sin betalning. Så Bob kommer att få en överraskningsbegäran där han kan låsa upp pengarna eftersom Alice redan har gjort jobbet.

![omslag](assets/chapitre10/3.JPG)

Sammanfattningsvis kodar en Lightning Network-faktura, även om den vid första anblicken kan verka komplex, effektivt en betalningsbegäran. Varje avsnitt i fakturan innehåller nyckelinformation, inklusive beloppet att betala, mottagaren, skapandets tidsstämpel och potentiellt annan information som hash av prebilden, betalningshemligheten, routningsanvisningar och utgångstiden. Protokoll som LNURL och Keysend erbjuder betydande förbättringar när det gäller flexibilitet och användarupplevelse, vilket till exempel gör det möjligt att skicka pengar utan föregående begäran från den andra parten. Dessa teknologier gör betalningsprocessen smidigare och mer effektiv på Lightning-nätverket.

## Hantera likviditet

![hantera likviditet](https://youtu.be/YuPrbhEJXbg)

Vi ger några allmänna riktlinjer för att svara på den eviga frågan om att hantera likviditet på Lightning.

![instruktion](assets/chapitre11/0.JPG)

Inom LN finns det 3 typer av personer:

- Köpare: de har utgående likviditet, vilket är enklast eftersom det bara kräver att man öppnar kanaler
- Handlarna: Det är mer komplicerat eftersom de behöver inkommande likviditet via andra noder och aktörer. De måste ha människor som är anslutna till dem.
- Routingnoder: De vill vara balanserade med likviditet från båda sidor och ha en bra anslutning till många noder för att användas så mycket som möjligt.

Så om du behöver inkommande likviditet kan du köpa det från tjänster.

![instruction](assets/chapitre11/1.JPG)

Alice köper en kanal med Susie för 1 miljon satoshis, så hon öppnar en kanal med direkt 1 000 000 SAT på ingående sidan. Hon kan då acceptera upp till 1 miljon SAT i betalning från kunder som är anslutna till Susie (som är mycket ansluten).

En annan lösning skulle vara att göra betalningar; du betalar 100 000 för X anledning, och du kan nu ta emot 100 000.

![instruction](assets/chapitre11/2.JPG)

### Lösning Loop Out: Atomic swap LN - BTC

Alice 2 miljoner - Susie 0

![instruction](assets/chapitre11/3.JPG)

Alice vill skicka likviditeten till Susie, så hon gör en Loop out (en speciell nod som erbjuder en professionell LN/BTC-balansjusteringstjänst). Alice skickar 1 miljon till loop via Susies nod, så Susie har likviditeten och Loop skickar tillbaka balansen on-chain till Alice nod.

![instruction](assets/chapitre11/4.JPG)

Så de 1 miljonerna går till Susie, hon skickar 1 miljon till Loop, Loop skickar 1 miljon till Alice. Alice har alltså flyttat likviditeten till Susie till priset av några avgifter som betalas till Loop för tjänsten.

Det svåraste med LN är att behålla likviditeten.

![instruction](assets/chapitre11/5.JPG)

Sammanfattningsvis är hanteringen av likviditet på Lightning Network en nyckelfråga som beror på användartypen: köpare, handlare eller routingnoder. Köparna, som behöver utgående likviditet, har den enklaste uppgiften: de öppnar helt enkelt kanaler. Handlare, som behöver inkommande likviditet, måste vara anslutna till andra noder och aktörer. Routingnoder strävar efter att behålla en balans av likviditet från båda sidor. Det finns flera lösningar för att hantera likviditet, som att köpa kanaler eller betala för att öka mottagningskapaciteten. Alternativet "Loop Out", som möjliggör en Atomic Swap mellan LN och BTC, erbjuder en intressant lösning för att balansera likviditeten. Trots dessa strategier förblir det en utmaning att behålla likviditeten på Lightning Network.

# Gå vidare

## Sammanfattning av utbildningen

![conclusion](https://youtu.be/MaWpD0rbkVo)

Vårt mål var att förklara hur Lightning-nätverket fungerar och hur det bygger på Bitcoin för att fungera.
Blixtnätverket är ett nätverk av betalningskanaler. Vi har sett hur en betalningskanal fungerar mellan två parter, men vi har också utvidgat vår syn till hela nätverket, till konceptet av ett nätverk av betalningskanaler.
![instruction](assets/chapitre12/0.JPG)

Kanalerna öppnas genom en Bitcoin-transaktion och kan rymma så många transaktioner som möjligt. Kanalens tillstånd representeras av en engagemangstransaktion som skickar till varje part vad de äger på sin sida av kanalen. När en transaktion sker inom kanalen åtar sig parterna det nya tillståndet genom att återkalla det gamla tillståndet och bygga en ny engagemangstransaktion.

![instruction](assets/chapitre12/1.JPG)

Paren skyddar sig mot fusk med återkallelseckar och en tidsfördröjning. Ömsesidigt överenskommen stängning föredras för att stänga kanalen. Vid tvångsstängning publiceras den sista engagemangstransaktionen.

![instruction](assets/chapitre12/3.JPG)

Betalningar kan gå genom andra noders kanaler. Betingade betalningar med hashlås (HTLC) låser pengarna tills betalningen är helt löst. Lökrouting används i Blixtnätverket. Mellannoderna känner inte till betalningens slutdestination. Alice måste beräkna betalningsrutten, men har inte all information om likviditeten i mellankanalerna.

![instruction](assets/chapitre12/4.JPG)

Det finns en sannolikhetskomponent när man skickar en betalning via Blixtnätverket.

![instruction](assets/chapitre12/5.JPG)

För att ta emot betalningar måste man hantera likviditeten i kanalerna, vilket kan göras genom att be andra personer att öppna kanaler till oss, genom att själv öppna kanaler och genom att använda verktyg som Loop eller genom att köpa/hyra kanaler på marknadsplatser.

## Intervju med Fanis

![intervju med Fanis](https://youtu.be/VeJ4oJIXo9k)

Här är en sammanfattning av intervjun:

Blixtnätverket är en extremt snabb betalningslösning på Bitcoin som gör det möjligt att kringgå begränsningarna i nätverkets skalbarhet. Men bitcoins på Blixtnätverket är inte lika säkra som de på Bitcoin-blockkedjan eftersom decentralisering och säkerhet prioriteras framför skalbarhet.

En överdriven ökning av blockstorleken är inte en bra lösning eftersom det innebär kompromisser när det gäller noder och datorkapacitet. Istället gör Blixtnätverket det möjligt att skapa betalningskanaler mellan två Bitcoin-användare utan att transaktionerna syns på blockkedjan, vilket sparar utrymme på blocken och gör att Bitcoin kan skalas idag.
Det finns dock kritik angående skalbarheten och centraliseringen av Lightning Network, med potentiella problem relaterade till stängning av kanaler och höga transaktionsavgifter. För att lösa dessa problem rekommenderas det att undvika att öppna små kanaler för att undvika framtida problem och att öka transaktionsavgifterna med Child Pay for Parent.
Framtida lösningar för Lightning Network inkluderar batchning och skapande av kanaler i grupper för att minska transaktionsavgifterna, samt långsiktigt öka blockstorleken. Det är dock viktigt att notera att bitcoins på Lightning inte är lika säkra som bitcoins på Bitcoin-kedjan.

Sekretessen på Bitcoin och Lightning är relaterade, med lök-routing som garanterar en viss nivå av sekretess för transaktioner. Men på Bitcoin är allt som standard transparent, med heuristik som används för att spåra bitcoins från adress till adress på Bitcoin-kedjan.

Att köpa bitcoins med KYC gör att utbytet kan känna till uttagstransaktionerna, medan runda belopp och växlingsadresser gör det möjligt att veta vilken del av en transaktion som är avsedd för en annan person och vilken del som är avsedd för en själv.

För att förbättra sekretessen kan sammanhängande åtgärder och coinjoins användas för att bryta sannolikhetsberäkningarna genom att göra transaktioner där flera personer gör en transaktion tillsammans. Företag som analyserar kedjor har svårare att avgöra vad du gör med dina bitcoins genom att följa dem.

På Lightning är det bara två personer som känner till transaktionen och det är mer konfidentiellt än Bitcoin. Lökrouting innebär att en mellannod inte känner till betalningens avsändare och mottagare.

För att använda Lightning Network rekommenderas det att följa en utbildning på din YouTube-kanal eller direkt på upptäck Bitcoin-webbplatsen, eller att använda utbildningen på Umbrell. Det är också möjligt att skicka godtycklig text vid en betalning på Lightning genom att använda ett dedikerat fält för detta, vilket kan vara användbart för donationer eller meddelanden.

Det är dock viktigt att notera att routningsnoder på Lightning kan regleras i framtiden, med vissa stater som kommer att försöka reglera routningsnoder.

För handlare är det nödvändigt att hantera likviditeten för att kunna acceptera betalningar via Lightning Network, med nuvarande begränsningar som kan övervinnas med lämpliga lösningar.

Slutligen är framtiden för Bitcoin lovande med en möjlig projicering av en miljon inom fem år. För att säkerställa professionaliseringen av branschen och skapandet av ett alternativt system till det befintliga banksystemet är det viktigt att bidra till nätverket och sluta lita på.

## Tack och fortsätt gräva kaninhålet

Grattis! 🎉

Du har slutfört LN 201 - Introduktion till Lightning Network-utbildningen!
Du kan vara stolt över dig själv eftersom det inte är lätt. Veta att det är få personer som går så djupt ner i Bitcoin-kaninhålet.
Först och främst, ett stort tack till Fanis Makalakis för att ha gett oss denna fantastiska gratis kurs om en mer etnisk aspekt av Lightning. Tveka inte att följa honom på Twitter, på hans blogg eller genom hans arbete på LN market.

Därefter, om du vill hjälpa till med projektet, tveka inte att sponsra oss på Patreon. Dina donationer kommer att användas för att producera innehåll för nya kurser och självklart kommer du att vara de första som hålls informerade (inklusive för Fanis nästa kurs som är på gång!).

Äventyret med Lightning Network fortsätter med kursen om Umbrel och installationen av en Lightning Network-nod. Sluta med teorin och ge plats åt praktiken med LN 202-kursen nu!

Puss och vi ses snart!

Rogzy
