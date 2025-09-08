---
name: Teoretisk introduktion till Lightning Network
goal: Upptäck Lightning Network ur ett tekniskt perspektiv
objectives: 

  - Förstå hur nätverkets kanaler fungerar.
  - Bekanta dig med begreppen HTLC, LNURL och UTXO.
  - Likställa likviditetshanteringen och avgifterna för LNN.
  - Känna igen Lightning Network som ett nätverk.
  - Förstå de teoretiska användningsområdena för Lightning Network.

---

# En resa till Bitcoin:s andra Layer


Dyk in i hjärtat av Lightning Network, ett viktigt system för framtidens Bitcoin-transaktioner. LNP201 är en teoretisk kurs om det tekniska arbetet med Lightning. Den avslöjar grunderna och mekanismerna i detta andra Layer-nätverk, som är utformat för att göra Bitcoin-betalningar snabba, ekonomiska och skalbara.


Tack vare sitt nätverk av betalningskanaler möjliggör Lightning snabba och säkra transaktioner utan att registrera varje Exchange på Bitcoin Blockchain. Genom kapitlen lär du dig hur öppning, hantering och stängning av kanaler fungerar, hur betalningar dirigeras genom mellanliggande noder på ett säkert sätt samtidigt som behovet av förtroende minimeras och hur man hanterar likviditet. Du kommer att upptäcka vad Commitment-transaktioner, HTLC:er, återkallningsnycklar, straffmekanismer, onion routing och fakturor är.


Oavsett om du är Bitcoin-nybörjare eller mer erfaren användare kommer den här kursen att ge värdefull information för att förstå och använda Lightning Network. Även om vi kommer att täcka några grundläggande delar av Bitcoin:s funktion i de första delarna, är det viktigt att behärska grunderna i Satoshi:s uppfinning innan du dyker in i LNP201.


Njut av din upptäckt!


+++

# Inledning

<partId>9da7290a-3895-49a2-93ea-2a6272ca4af4</partId>


## Kursöversikt

<chapterId>f2e71062-5121-4114-a7f8-27df69884ce8</chapterId>


Välkommen till LNP201-kursen!


Denna utbildning syftar till att ge dig en djupgående teknisk förståelse för Lightning Network, ett overlay-nätverk som är utformat för att underlätta snabba och ofta billiga Bitcoin-transaktioner. Du kommer gradvis att upptäcka de grundläggande begrepp som styr detta system, från att öppna betalningskanaler till routningstekniker och likviditetshantering.


**Avsnitt 1: Grundläggande kunskaper**

Vi börjar med en allmän introduktion till Lightning Network, där vi lägger grunden för Bitcoin, dess adresser, UTXO:er och hur transaktioner fungerar. Denna grundläggande genomgång är nödvändig för att förstå hur Lightning Network förlitar sig på de underliggande Blockchain-mekanismerna för att fungera säkert.


**Avsnitt 2: Öppna och stänga kanaler**

I det här avsnittet kommer vi att utforska kanalöppningsprocessen, som är hörnstenen i Lightning Network. Du kommer att lära dig hur Commitment-transaktioner skapas, vilken roll återkallningsnycklar har för säkerheten och hur kanaler kan stängas antingen gemensamt eller ensidigt. Varje steg kommer att förklaras exakt och tekniskt för att hjälpa dig att förstå alla finesser.


**Avsnitt 3: Ett likviditetsnätverk**

Lightning Network är inte begränsat till enskilda kanaler, utan är ett verkligt betalningsnätverk. Vi kommer att se hur transaktioner kan dirigeras genom mellanliggande noder med hjälp av HTLC. I det här avsnittet får du också en introduktion till utmaningarna med inkommande och utgående likviditet.


**Avsnitt 4: Lightning Network-verktyg**

I det här avsnittet presenteras praktiska verktyg i Lightning Network, till exempel *Invoices*, *LNURL* och *Keysend*. Du kommer också att lära dig hur du hanterar dina kanalers likviditet, en viktig aspekt för att säkerställa smidiga betalningar och maximera effektiviteten i dina transaktioner på Lightning.


**Avsnitt 5: Att gå vidare**

Slutligen kommer vi att avsluta utbildningen genom att sammanfatta de begrepp som behandlats och bana väg för mer avancerade ämnen för dem som vill fördjupa sina kunskaper om Lightning Network.


Är du redo att avslöja de tekniska mekanismerna i Lightning Network? Låt oss dyka in!


# De grundläggande principerna


<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>


## Förståelse av Lightning Network


<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>


:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::



Lightning Network är ett nätverk av betalningskanaler som bygger på Bitcoin-protokollet och syftar till att möjliggöra snabba transaktioner till låg kostnad. Det gör det möjligt att skapa betalningskanaler mellan deltagare, inom vilka transaktioner kan göras nästan omedelbart och med minimala avgifter, utan att behöva registrera varje transaktion individuellt på Blockchain. Lightning Network syftar således till att förbättra Bitcoin:s skalbarhet och göra den användbar för betalningar av lågt värde.


Innan du utforskar "nätverksaspekten" är det viktigt att förstå konceptet med en **betalningskanal** på Lightning, hur det fungerar och dess detaljer. Detta är ämnet för detta första kapitel.


### Begreppet betalningskanal


En betalningskanal tillåter två parter, här **Alice** och **Bob**, att Exchange medel över Lightning Network. Varje huvudperson har en nod, symboliserad av en cirkel, och kanalen mellan dem representeras av ett linjesegment.


![LNP201](assets/en/01.webp)


I vårt exempel har Alice 100 000 satoshis på sin sida av kanalen och Bob har 30 000, för totalt 130 000 satoshis, vilket utgör **kanalkapaciteten**.


**Men vad är en Satoshi?


**Satoshi** (eller "sat") är en beräkningsenhet på Bitcoin. I likhet med en cent för euron är en Satoshi helt enkelt en bråkdel av Bitcoin. En Satoshi är lika med **0,00000001 Bitcoin**, eller en hundra miljondels Bitcoin. Att använda Satoshi blir alltmer praktiskt i takt med att värdet på Bitcoin stiger.


### Fördelningen av medel i kanalen


Låt oss återgå till betalningskanalen. Nyckelbegreppet här är "**sidan av kanalen**". Varje deltagare har medel på sin sida av kanalen: Alice 100.000 satoshis och Bob 30.000. Som vi har sett utgör summan av dessa medel kanalens totala kapacitet, en siffra som fastställs när den öppnas.


![LNP201](assets/en/02.webp)


Låt oss ta ett exempel på en Lightning-transaktion. Om Alice vill skicka 40 000 satoshis till Bob är detta möjligt eftersom hon har tillräckligt med pengar (100 000 satoshis). Efter den här transaktionen har Alice 60 000 satoshis på sin sida och Bob 70 000.


![LNP201](assets/en/03.webp)


Kanalens **kapacitet** på 130.000 satoshis förblir oförändrad. Det som förändras är tilldelningen av medel. Detta system tillåter inte att man skickar mer pengar än man har. Om Bob till exempel vill skicka tillbaka 80 000 satoshis till Alice kan han inte göra det, eftersom han bara har 70 000.


Ett annat sätt att föreställa sig fördelningen av medel är att föreställa sig en **markör** som visar var medlen finns inom kanalen. Inledningsvis, med 100 000 satoshis för Alice och 30 000 för Bob, är markören mer på Bob:s sida, eftersom Alice har mycket mer pengar. Efter transaktionen på 40 000 satoshis kommer markören att skifta något mot Alice, som nu har 60 000 satoshis.


![LNP201](assets/en/04.webp)


Denna representation kan vara användbar för att föreställa sig balansen av medel i en kanal.


### De grundläggande reglerna för en betalningskanal


Den första punkten att komma ihåg är att **kanalkapaciteten** är fast. Det är ungefär som diametern på ett rör: det bestämmer den maximala mängden pengar som kan skickas genom kanalen på en gång.

Låt oss ta ett exempel: om Alice har 130 000 satoshis på sin sida kan hon bara skicka högst 130 000 satoshis till Bob i en enda transaktion. Bob kan dock sedan skicka tillbaka dessa medel till Alice, antingen helt eller delvis.


Vad som är viktigt att förstå är att kanalens fasta kapacitet begränsar det maximala beloppet för en enskild transaktion, men inte det totala antalet möjliga transaktioner eller den totala volymen av medel som utväxlas inom kanalen.


**Vad ska du ta med dig från detta kapitel?



- Kapaciteten för en kanal är fast och bestämmer det maximala belopp som kan skickas i en enda transaktion.
- Pengarna i en kanal fördelas mellan de två deltagarna, och var och en kan bara skicka till den andra de pengar de äger på sin sida.
- Lightning Network möjliggör således en snabb och effektiv Exchange av medel, samtidigt som de begränsningar som följer av kanalernas kapacitet respekteras.


Detta är slutet på detta första kapitel, där vi har lagt grunden för Lightning Network. I de kommande kapitlen kommer vi att se hur man öppnar en kanal och fördjupa oss i de begrepp som diskuterats här.


## Bitcoin, Adresser, UTXO och Transaktioner


<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>


:::video id=75323eef-ea03-45ac-9a6e-46d73ca255de:::


Detta kapitel är lite speciellt eftersom det inte kommer att vara direkt tillägnad Lightning, utan till Bitcoin. Lightning Network är i själva verket en Layer ovanpå Bitcoin. Det är därför viktigt att förstå vissa grundläggande begrepp i Bitcoin för att korrekt förstå hur Lightning fungerar i de efterföljande kapitlen. I detta kapitel kommer vi att gå igenom grunderna för Bitcoin-mottagningsadresser, UTXO:er samt hur Bitcoin-transaktioner fungerar.


### Bitcoin Adresser, privata nycklar och offentliga nycklar


En Bitcoin Address är en serie tecken som härleds från en **public key**, som i sin tur beräknas från en **private key**. Som du säkert vet används den för att låsa bitcoins, vilket är likvärdigt med att ta emot dem i vår Wallet.


Den privata nyckeln är ett hemligt element som **aldrig bör delas**, medan den offentliga nyckeln och Address kan delas utan säkerhetsrisk (deras avslöjande utgör endast en risk för din integritet). Här är en gemensam representation som vi kommer att använda under hela den här utbildningen:



- De **privata nycklarna** kommer att representeras **vertikalt**.
- De **offentliga nycklarna** kommer att representeras **horisontellt**.
- Deras färg anger vem som äger dem (Alice i orange och Bob i svart...).


### Bitcoin Transaktioner: Skicka pengar och skript


På Bitcoin innebär en transaktion att skicka pengar från en Address till en annan. Låt oss ta exemplet med Alice som skickar 0,002 Bitcoin till Bob. Alice använder den privata nyckeln som är associerad med hennes Address för att **signera** transaktionen, och bevisar därmed att hon verkligen kan spendera dessa pengar. Men vad är det egentligen som händer bakom den här transaktionen? Pengarna på en Bitcoin Address är låsta av ett **skript**, ett slags miniprogram som ställer vissa villkor för att använda pengarna.


Det vanligaste skriptet kräver en signatur med den privata nyckel som är kopplad till Address. När Alice signerar en transaktion med sin privata nyckel **låser hon upp skriptet** som blockerar pengarna, och de kan då överföras. Överföringen av medel innebär att ett nytt skript läggs till dessa medel, där det anges att **Bob:s** privata nyckelsignatur krävs för att spendera dem den här gången.


![LNP201](assets/en/05.webp)


### UTXO: Utgångar för oanvända transaktioner


På Bitcoin är det vi faktiskt Exchange inte direkt bitcoins, utan **UTXOs** (_Unspent Transaction Outputs_), vilket betyder "outnyttjade transaktionsutgångar".


En UTXO är en del av Bitcoin som kan ha vilket värde som helst, till exempel **2 000 bitcoins**, **8 bitcoins** eller till och med **8 000 Sats**. Varje UTXO är låst av ett skript, och för att spendera den måste man uppfylla skriptets villkor, ofta en signatur med den privata nyckeln som motsvarar en given mottagande Address.


UTXO:er kan inte delas. Varje gång de används för att spendera det belopp i bitcoins som de representerar måste det göras i sin helhet. Det är lite som en sedel: om du har en räkning på 10 euro och är skyldig bagaren 5 euro kan du inte bara dela räkningen på mitten. Du måste ge honom 10-eurosedeln och han ger dig 5 euro i växel. Detta är exakt samma princip för UTXO:er på Bitcoin! När Alice till exempel låser upp ett skript med sin privata nyckel, låser hon upp hela UTXO. Om hon vill skicka endast en del av de medel som representeras av denna UTXO till Bob, kan hon "fragmentera" den i flera mindre. Hon kommer då att skicka 0,0015 BTC till Bob och skicka resten, 0,0005 BTC, till en **change Address**.


Här följer ett exempel på en transaktion med 2 utgångar:



- En UTXO på 0,0015 BTC för Bob, låst av ett skript som kräver Bob:s privata nyckelsignatur.
- En UTXO på 0,0005 BTC för Alice, låst av ett skript som kräver hennes egen signatur.


![LNP201](assets/en/06.webp)


### Adresser med flera signaturer


Förutom enkla adresser som genereras från en enda publik nyckel är det möjligt att skapa **adresser med flera signaturer** från flera publika nycklar. Ett särskilt intressant fall för Lightning Network är **2/2 multisignatur Address**, som genereras från två publika nycklar:


![LNP201](assets/en/07.webp)


För att spendera de medel som är låsta med denna 2/2 multisignatur Address måste man signera med de två privata nycklar som är associerade med de offentliga nycklarna.


![LNP201](assets/en/08.webp)


Denna typ av Address är just representationen på Bitcoin Blockchain av betalningskanaler på Lightning Network.


**Vad ska du ta med dig från detta kapitel?



- En **Bitcoin Address** härleds från en publik nyckel, som i sin tur härleds från en privat nyckel.
- Medel på Bitcoin är låsta av **skript**, och för att spendera dessa medel måste man uppfylla skriptet, vilket i allmänhet innebär att man tillhandahåller en signatur med motsvarande privata nyckel.
- UTXO** är bitar av bitcoins som är låsta av skript, och varje transaktion på Bitcoin består av att låsa upp en UTXO och sedan skapa en eller flera nya i gengäld.
- 2/2 multisignaturadresser** kräver signatur av två privata nycklar för att spendera pengarna. Dessa specifika adresser används i samband med Lightning för att skapa betalningskanaler.


Detta kapitel om Bitcoin har gjort det möjligt för oss att granska några viktiga begrepp för vad som följer. I nästa kapitel kommer vi specifikt att upptäcka hur öppningen av kanaler på Lightning Network fungerar.


# Öppning och stängning av kanaler


<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>


## Öppning av kanal


<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>


:::video id=6098fee1-735e-4d8d-9f57-0faf5fef6d76:::


I det här kapitlet kommer vi att se mer exakt hur man öppnar en betalningskanal på Lightning Network och förstå kopplingen mellan denna operation och det underliggande Bitcoin-systemet.


### Blixtkanaler


Som vi såg i det första kapitlet kan en **betalningskanal** på Lightning jämföras med ett "rör" för att utbyta pengar mellan två deltagare (**Alice** och **Bob** i våra exempel). Kapaciteten i denna kanal motsvarar summan av de tillgängliga medlen på varje sida. I vårt exempel har Alice **100.000 satoshis** och Bob har **30.000 satoshis**, vilket ger en **total kapacitet** på **130.000 satoshis**.


![LNP201](assets/en/09.webp)


### Nivåer av information Exchange


Det är viktigt att tydligt skilja mellan de olika nivåerna av Exchange på Lightning Network:



- Peer-to-peer-kommunikation (Lightning-protokollet)**: Detta är de meddelanden som Lightning-noderna skickar till varandra för att kommunicera. Vi kommer att representera dessa meddelanden med streckade svarta linjer i våra diagram.
- Betalningskanaler (Lightning-protokoll)**: Det här är vägarna för att utbyta pengar på Lightning, som vi kommer att representera med solida svarta linjer.
- Bitcoin-transaktioner (Bitcoin-protokoll)**: Det här är de transaktioner som görs på kedjan, som vi kommer att representera med orange linjer.


![LNP201](assets/en/10.webp)


Det är värt att notera att en Lightning-nod kan kommunicera via P2P-protokollet utan att öppna en kanal, men för Exchange-fonder är en kanal nödvändig.


### Steg för att öppna en Lightning Channel



- Meddelande Exchange**: Alice vill öppna en kanal med Bob. Hon skickar ett meddelande till honom som innehåller det belopp hon vill sätta in i kanalen (130 000 Sats) och sin publika nyckel. Bob svarar genom att dela med sig av sin egen publika nyckel.


![LNP201](assets/en/11.webp)



- Skapande av en Address med flera signaturer**: Med dessa två publika nycklar skapar Alice en **2/2 multisignatur Address**, vilket innebär att de medel som senare kommer att sättas in på denna Address kommer att kräva båda signaturerna (Alice och Bob) för att användas.


![LNP201](assets/en/12.webp)



- Insättningstransaktion**: Alice förbereder en Bitcoin-transaktion för att sätta in pengar på denna multisignatur Address. Hon kan till exempel bestämma sig för att skicka **130 000 satoshis** till denna multisignatur Address. Den här transaktionen är **konstruerad men ännu inte publicerad** på Blockchain.


![LNP201](assets/en/13.webp)



- Uttagstransaktion**: Innan Alice publicerar insättningstransaktionen konstruerar hon en uttagstransaktion så att hon kan återfå sina medel i händelse av ett problem med Bob. När Alice publicerar insättningstransaktionen kommer hennes Sats att vara låst på en 2/2 multisignatur Address som kräver både hennes signatur och Bob:s signatur för att låsas upp. Alice skyddar sig mot denna förlustrisk genom att konstruera en uttagstransaktion som gör det möjligt för henne att återfå sina medel.


![LNP201](assets/en/14.webp)



- Bob:s underskrift**: Alice skickar insättningstransaktionen till Bob som bevis och ber honom att underteckna uttagstransaktionen. När Bob:s underskrift har erhållits på uttagstransaktionen är Alice säker på att kunna återfå sina medel när som helst, eftersom endast hennes egen underskrift nu behövs för att låsa upp multisignaturen.


![LNP201](assets/en/15.webp)



- Publicering av insättningstransaktionen**: När Bob:s signatur har erhållits kan Alice publicera insättningstransaktionen på Bitcoin Blockchain och därigenom officiellt öppna Lightning-kanalen mellan de två användarna.


![LNP201](assets/en/16.webp)


### När är kanalen öppen?


Kanalen anses vara öppen när insättningstransaktionen ingår i ett Bitcoin-block och den har nått ett visst antal bekräftelser (antal följande block).


**Vad ska du komma ihåg från det här kapitlet?



- Öppnandet av en kanal börjar med Exchange av **meddelanden** mellan de två parterna (Exchange av belopp och publika nycklar).
- En kanal bildas genom att skapa en **2/2 multisignatur Address** och sätta in pengar i den via en Bitcoin-transaktion.
- Den person som öppnar kanalen säkerställer att de kan **återfå sina medel** genom en uttagstransaktion som undertecknas av den andra parten innan de publicerar insättningstransaktionen.


I nästa kapitel kommer vi att utforska det tekniska arbetet med en Lightning-transaktion inom en kanal.


## Commitment Transaction


<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>


:::video id=c17454f3-14c5-47a0-8c9c-42ee12932bd3:::


I det här kapitlet kommer vi att upptäcka den tekniska funktionen för en transaktion inom en kanal på Lightning Network, det vill säga när medel flyttas från ena sidan av kanalen till den andra.


### Påminnelse om kanalens livscykel


Som tidigare nämnts börjar en Lightning-kanal med en **öppning** via en Bitcoin-transaktion. Kanalen kan **stängas** när som helst, också via en Bitcoin-transaktion. Mellan dessa två tillfällen kan ett nästan oändligt antal transaktioner utföras inom kanalen, utan att gå igenom Bitcoin Blockchain. Låt oss se vad som händer under en transaktion i kanalen.


![LNP201](assets/en/17.webp)


### Kanalens initiala tillstånd


Vid tidpunkten för öppnandet av kanalen satte Alice in **130 000 satoshis** på kanalens multisignatur Address. I det initiala tillståndet är således alla medel på Alice:s sida. Innan Alice öppnade kanalen fick Alice även Bob att underteckna en **uttagstransaktion**, som skulle göra det möjligt för henne att återfå sina medel om hon ville stänga kanalen.


![LNP201](assets/en/18.webp)


### Opublicerade transaktioner: Commitment-transaktionerna


När Alice gör en transaktion i kanalen för att skicka pengar till Bob, skapas en ny Bitcoin-transaktion för att återspegla denna förändring i fördelningen av pengar. Denna transaktion, som kallas **Commitment Transaction**, publiceras inte på Blockchain men representerar kanalens nya tillstånd efter Lightning-transaktionen.


Låt oss ta ett exempel där Alice skickar 30 000 satoshis till Bob:



- Ursprungligen**: Alice har 130.000 satoshis.
- Efter transaktionen**: Alice har 100 000 satoshis och Bob 30 000 satoshis.

För att validera denna överföring skapar Alice och Bob en ny **opublicerad Bitcoin-transaktion** som skulle skicka **100 000 satoshis till Alice** och **30 000 satoshis till Bob** från multisignaturen Address. Båda parter konstruerar denna transaktion oberoende av varandra, men med samma uppgifter (belopp och adresser). När den är konstruerad signerar var och en transaktionen och utbyter sin signatur med den andra. Detta gör att endera parten kan publicera transaktionen när som helst om det behövs för att återfå sin andel av kanalen på huvud Bitcoin Blockchain.

![LNP201](assets/en/19.webp)


### Överföringsprocess: Invoice


När Bob vill ta emot pengar skickar han en **_faktura_** på 30 000 satoshis till Alice. Alice fortsätter sedan att betala denna Invoice genom att starta överföringen inom kanalen. Som vi har sett är denna process beroende av skapandet och undertecknandet av en ny **Commitment Transaction**.


Varje Commitment Transaction representerar den nya fördelningen av medel i kanalen efter överföringen. I det här exemplet har Bob 30 000 satoshis och Alice 100 000 satoshis efter transaktionen. Om någon av de två deltagarna bestämmer sig för att publicera denna Commitment Transaction på Blockchain, kommer det att leda till att kanalen stängs och att medlen fördelas enligt denna sista fördelning.


![LNP201](assets/en/20.webp)


### Nytt tillstånd efter en andra transaktion


Låt oss ta ett annat exempel: efter den första transaktionen där Alice skickade 30 000 satoshis till Bob, beslutar Bob att skicka **10 000 satoshis tillbaka till Alice**. Detta skapar ett nytt tillstånd i kanalen. Den nya **Commitment Transaction** kommer att representera denna uppdaterade fördelning:



- Alice** har nu **110 000 satoshis**.
- Bob** har **20.000 satoshis**.


![LNP201](assets/en/21.webp)


Även denna transaktion publiceras inte på Blockchain men kan göra det när som helst om kanalen är stängd.


Sammanfattningsvis, när medel överförs inom en Lightning-kanal:



- Alice och Bob skapar en ny **Commitment Transaction**, som återspeglar den nya fördelningen av medel.
- Denna Bitcoin-transaktion är **undertecknad** av båda parter, men **inte publicerad** på Bitcoin Blockchain så länge kanalen förblir öppen.
- Commitment-transaktionerna säkerställer att varje deltagare när som helst kan återfå sina medel på Bitcoin Blockchain genom att publicera den senast signerade transaktionen.


Det här systemet har dock en potentiell brist, som vi kommer att Address i nästa kapitel. Vi ska se hur varje deltagare kan skydda sig mot att den andra parten försöker fuska.


## Nyckel för återkallande


<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

:::video id=1d850f23-eff1-4725-b284-ce12456a2c26:::

I det här kapitlet kommer vi att fördjupa oss i hur transaktioner fungerar på Lightning Network genom att diskutera de mekanismer som finns för att skydda mot fusk och se till att varje part följer reglerna inom en kanal.


### Påminnelse: Commitment-transaktioner


Som tidigare sett förlitar sig transaktioner på Lightning på opublicerade ** Commitment-transaktioner**. Dessa transaktioner återspeglar den aktuella fördelningen av medel i kanalen. När en ny Lightning-transaktion görs skapas en ny Commitment Transaction som undertecknas av båda parter för att återspegla det nya tillståndet i kanalen.


Låt oss ta ett enkelt exempel:



- Initialt tillstånd**: Alice har **100 000 satoshis**, Bob **30 000 satoshis**.
- Efter en transaktion där Alice skickar **40 000 satoshis** till Bob, fördelar det nya Commitment Transaction medlen enligt följande:
  - Alice: **60 000 satoshis**
  - Bob: **70 000 satoshis**


![LNP201](assets/en/22.webp)


Båda parter kan när som helst publicera den **senaste Commitment Transaction** som undertecknats för att stänga kanalen och återfå sina medel.


### Felet: Fusk genom att publicera en gammal transaktion


Ett potentiellt problem uppstår om en av parterna beslutar sig för att **fuska** genom att publicera en gammal Commitment Transaction. Alice kan till exempel publicera en äldre Commitment Transaction där hon hade **100 000 satoshis**, även om hon nu bara har **60 000** i verkligheten. Detta skulle göra det möjligt för henne att stjäla **40 000 satoshis** från Bob.


![LNP201](assets/en/23.webp)


Ännu värre är att Alice skulle kunna publicera den allra första uttagstransaktionen, den innan kanalen öppnades, där hon hade **130 000 satoshis**, och därmed stjäla hela kanalens medel.


![LNP201](assets/en/24.webp)


### Lösning: Återkallande nyckel och tidslås


För att förhindra denna typ av fusk från Alice, på Lightning Network, läggs **säkerhetsmekanismer** till Commitment-transaktionerna:



- Tidslåset**: Varje Commitment Transaction innehåller en tidslåsning för Alice:s medel. Tidslåset är en Smart contract-primitiv som anger ett tidsvillkor som måste uppfyllas för att en transaktion ska läggas till i ett block. Det innebär att Alice inte kan återfå sina medel förrän ett visst antal block har passerat om hon publicerar en av Commitment-transaktionerna. Denna tidslåsning börjar gälla från och med bekräftelsen av Commitment Transaction. Dess varaktighet är i allmänhet proportionell mot kanalens storlek, men den kan också konfigureras manuellt.
- Återkallelse nyckel**: Alice:s medel kan också omedelbart spenderas av Bob om han innehar **revocation key**. Denna nyckel består av en hemlighet som innehas av Alice och en hemlighet som innehas av Bob. Observera att denna hemlighet är olika för varje Commitment Transaction.

Tack vare dessa 2 kombinerade mekanismer har Bob tid att upptäcka Alice:s försök att fuska och att straffa henne genom att hämta sin utgång med återkallningsnyckeln, vilket för Bob innebär att återställa alla medel i kanalen. Vår nya Commitment Transaction kommer nu att se ut så här:


![LNP201](assets/en/25.webp)


Låt oss tillsammans gå igenom hur denna mekanism fungerar i detalj.


### Process för uppdatering av transaktioner


När Alice och Bob uppdaterar kanalens tillstånd med en ny blixttransaktion, Exchange de i förväg sina respektive **hemligheter** för den tidigare Commitment Transaction (den som kommer att bli föråldrad och kan göra det möjligt för en av dem att fuska). Detta innebär att i det nya tillståndet för kanalen:



- Alice och Bob har en ny Commitment Transaction som representerar den aktuella fördelningen av medel efter Lightning-transaktionen.
- Båda har den andras hemlighet för den föregående transaktionen, vilket gör att de kan använda återkallningsnyckeln endast om en av dem försöker fuska genom att publicera en transaktion med ett gammalt tillstånd i Bitcoin-nodernas mempooler. För att straffa den andra parten är det faktiskt nödvändigt att hålla båda hemligheterna och den andra partens Commitment Transaction, som innehåller den signerade inmatningen. Utan denna transaktion är enbart återkallningsnyckeln värdelös. Det enda sättet att få tag på denna transaktion är att hämta den från mempoolerna (i de transaktioner som väntar på bekräftelse) eller i de bekräftade transaktionerna på Blockchain under tidslåset, vilket bevisar att den andra parten försöker fuska, avsiktligt eller inte.


Låt oss ta ett exempel för att förstå denna process väl:



- Initialtillstånd**: Alice har **100 000 satoshis**, Bob **30 000 satoshis**.


![LNP201](assets/en/26.webp)



- Bob vill ta emot 40 000 satoshis från Alice via deras Lightning-kanal. För att göra detta:
   - Han skickar en Invoice till henne tillsammans med sin hemlighet för återkallningsnyckeln för hans tidigare Commitment Transaction.
   - Som svar tillhandahåller Alice sin signatur för Bob:s nya Commitment Transaction, samt sin hemlighet för återkallningsnyckeln för hennes tidigare transaktion.
   - Slutligen skickar Bob sin signatur för Alice:s nya Commitment Transaction.
   - Dessa utbyten gör det möjligt för Alice att skicka **40 000 satoshis** till Bob på Lightning via deras kanal, och de nya Commitment-transaktionerna återspeglar nu denna nya fördelning av medel.


![LNP201](assets/en/27.webp)



- Om Alice försöker publicera den gamla Commitment Transaction där hon fortfarande ägde **100 000 satoshis**, kan Bob, som har erhållit återkallningsnyckeln, omedelbart återfå pengarna med hjälp av denna nyckel, medan Alice blockeras av tidslåset.


![LNP201](assets/en/28.webp)


Även om Bob i det här fallet inte har något ekonomiskt intresse av att försöka fuska, om han ändå gör det, drar Alice också nytta av ett symmetriskt skydd som ger henne samma garantier.


**Vad ska du ta med dig från detta kapitel?


**Commitment-transaktionerna** på Lightning Network innehåller säkerhetsmekanismer som minskar både risken för fusk och incitamenten att göra det. Innan en ny Commitment Transaction undertecknas, Alice och Bob Exchange deras respektive **hemligheter** för de tidigare Commitment-transaktionerna. Om Alice försöker publicera en gammal Commitment Transaction kan Bob använda **revocation key** för att återfå alla medel innan Alice kan göra det (eftersom hon är blockerad av tidslåset), vilket straffar henne för att ha försökt fuska.


Detta säkerhetssystem säkerställer att deltagarna följer reglerna i Lightning Network och att de inte kan tjäna pengar på att publicera gamla Commitment-transaktioner.


Vid denna punkt i utbildningen vet du nu hur Lightning-kanaler öppnas och hur transaktioner inom dessa kanaler fungerar. I nästa kapitel kommer vi att upptäcka de olika sätten att stänga en kanal och återfå dina bitcoins på huvudwebbplatsen Blockchain.


## Stängning av kanal


<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>


:::video id=4d8ad4e6-32ff-46d3-bd17-343929aa863b:::


I det här kapitlet kommer vi att diskutera **stängning av en kanal** på Lightning Network, vilket görs genom en Bitcoin-transaktion, precis som att öppna en kanal. Efter att ha sett hur transaktioner inom en kanal fungerar är det nu dags att se hur man stänger en kanal och återfår pengarna på Bitcoin Blockchain.


### Påminnelse om kanalens livscykel


En kanals **livscykel** börjar med att den **öppnas**, via en Bitcoin-transaktion, sedan görs Lightning-transaktioner inom den, och slutligen, när parterna vill återfå sina medel, **stängs** kanalen genom en andra Bitcoin-transaktion. De mellanliggande transaktionerna som görs på Lightning representeras av opublicerade **Commitment-transaktioner**.


![LNP201](assets/en/29.webp)


### De tre typerna av kanalstängning


Det finns tre huvudsakliga sätt att stänga den här kanalen, som kan kallas **the good, the brute, and the truant** (inspirerad av Andreas Antonopoulos i _Mastering the Lightning Network_):



- Det goda**: den **samarbetsinriktade stängningen**, där Alice och Bob kommer överens om att stänga kanalen.
- Det dåliga**: den **tvingade stängningen**, där en av parterna beslutar att stänga kanalen ärligt, men utan den andras samtycke.
- Det fula**: **avslut med fusk**, där en av parterna försöker stjäla medel genom att publicera en gammal Commitment Transaction (vilken som helst, men inte den sista, som återspeglar den faktiska och rättvisa fördelningen av medel).


Låt oss ta ett exempel:



- Alice äger **100.000 satoshis** och Bob **30.000 satoshis**.
- Denna fördelning återspeglas i **2 Commitment-transaktioner** (en per användare) som inte publiceras, men som kan komma att publiceras om kanalen stängs.


![LNP201](assets/en/30.webp)


### Det goda: den kooperativa stängningen


I en **kooperativ stängning** kommer Alice och Bob överens om att stänga kanalen. Så här går det till:



- Alice skickar ett meddelande till Bob via Lightning-kommunikationsprotokollet för att föreslå att kanalen stängs.
- Bob samtycker och de två parterna gör inga ytterligare transaktioner i kanalen.


![LNP201](assets/en/31.webp)



- Alice och Bob förhandlar tillsammans om avgifterna för den **avslutande transaktionen**. Dessa avgifter beräknas i allmänhet baserat på Bitcoin:s avgiftsmarknad vid tidpunkten för stängningen. Det är viktigt att notera att **det alltid är den person som öppnade kanalen** (Alice i vårt exempel) som betalar avslutsavgifterna.
- De konstruerar en ny **avslutande transaktion**. Denna transaktion liknar en Commitment Transaction, men utan tidslås eller återkallelsemekanismer, eftersom båda parter samarbetar och det inte finns någon risk för fusk. Denna kooperativa avslutande transaktion skiljer sig därför från Commitment-transaktioner.


Till exempel, om Alice äger **100 000 satoshis** och Bob **30 000 satoshis**, kommer den avslutande transaktionen att skicka **100 000 satoshis** till Alice:s Address och **30 000 satoshis** till Bob:s Address, utan tidsbegränsningar. När denna transaktion har undertecknats av båda parter publiceras den av Alice. När transaktionen har bekräftats på Bitcoin Blockchain kommer Lightning-kanalen att stängas officiellt.


![LNP201](assets/en/32.webp)


**Kooperativ stängning** är den föredragna metoden för stängning eftersom den är snabb (ingen tidslåsning) och transaktionsavgifterna justeras enligt de aktuella Bitcoin-marknadsförhållandena. På så sätt undviker man att betala för lite, vilket kan riskera att blockera transaktionen i mempoolerna, eller att betala för mycket i onödan, vilket leder till onödiga ekonomiska förluster för deltagarna.


### Det dåliga: den påtvingade stängningen


När Alice:s nod skickar ett meddelande till Bob:s och ber om en kooperativ stängning, och Alice inte svarar (t.ex. på grund av ett internetavbrott eller ett tekniskt problem), kan Alice fortsätta med en **tvingad stängning** genom att publicera den **sista signerade Commitment Transaction**.

I detta fall kommer Alice helt enkelt att publicera den senaste Commitment Transaction, som återspeglar kanalens tillstånd vid den tidpunkt då den senaste blixttransaktionen ägde rum med korrekt fördelning av medel.


![LNP201](assets/en/33.webp)


Denna transaktion inkluderar en **tidsspärr** för Alice:s medel, vilket gör stängningen långsammare.


![LNP201](assets/en/34.webp)


Avgifterna för Commitment Transaction kan också vara olämpliga vid tidpunkten för stängningen, eftersom de fastställdes när transaktionen skapades, ibland flera månader tidigare. I allmänhet överskattar Lightning-kunder avgifterna för att undvika framtida problem, men detta kan leda till för höga avgifter, eller omvänt för låga.


Sammanfattningsvis är **tvingad stängning** en sista utväg när motparten inte längre svarar. Det är långsammare och mindre ekonomiskt än en kooperativ stängning. Därför bör det undvikas så mycket som möjligt.


### Fusk: fusk


Slutligen inträffar en stängning med **fusk** när en av parterna försöker publicera en gammal Commitment Transaction, ofta där de hade mer pengar än de borde. Till exempel kan Alice publicera en gammal transaktion där hon ägde **120 000 satoshis**, medan hon faktiskt bara äger **100 000** nu.


![LNP201](assets/en/35.webp)


Bob, för att förhindra detta fusk, övervakar Bitcoin Blockchain och dess Mempool för att säkerställa att Alice inte publicerar en gammal transaktion. Om Bob upptäcker ett fuskförsök kan han använda **revocation key** för att återställa Alice:s medel och straffa henne genom att ta hela kanalens medel. Eftersom Alice är blockerad av tidslåset på sin utgång har Bob tid att spendera den utan tidslås på sin sida för att återfå hela summan på en Address som han äger.


![LNP201](assets/en/36.webp)


Det är uppenbart att fusk potentiellt kan lyckas om Bob inte agerar inom den tid som tidslåset på Alice:s produktion innebär. I det här fallet är Alice:s output upplåst, vilket gör att hon kan konsumera det för att skapa en ny output till en Address som hon kontrollerar.


**Vad ska du ta med dig från detta kapitel?


Det finns tre sätt att stänga en kanal:



- Kooperativ stängning**: Snabbt och billigare, där båda parter är överens om att stänga kanalen och publicera en skräddarsydd stängningstransaktion.
- Tvångsnedläggning**: Mindre önskvärt, eftersom det är beroende av att publicera en Commitment Transaction, med potentiellt olämpliga avgifter och en tidsspärr, vilket fördröjer stängningen.
- Fusk**: Om en av parterna försöker stjäla pengar genom att publicera en gammal transaktion, kan den andra parten använda återkallningsnyckeln för att bestraffa detta fusk.


I de kommande kapitlen kommer vi att utforska Lightning Network ur ett bredare perspektiv, med fokus på hur dess nätverk fungerar.


# Ett likviditetsnätverk


<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>


## Lightning Network


<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>


:::video id=38419c23-5592-4573-b0a7-84824a5bfb77:::


I det här kapitlet kommer vi att undersöka hur betalningar på Lightning Network kan nå en mottagare även om de inte är direkt anslutna via en betalningskanal. Lightning är i själva verket ett **nätverk av betalningskanaler**, som gör det möjligt att skicka pengar till en avlägsen nod via andra deltagares kanaler. Vi kommer att upptäcka hur betalningar dirigeras över nätverket, hur likviditet rör sig mellan kanaler och hur transaktionsavgifter beräknas.


### Nätverket av betalningskanaler


På Lightning Network motsvarar en transaktion en överföring av pengar mellan två noder. Som vi sett i tidigare kapitel är det nödvändigt att öppna en kanal med någon för att utföra Lightning-transaktioner. Denna kanal möjliggör ett nästan oändligt antal off-chain-transaktioner innan den stängs för att återfå On-Chain-saldot. Den här metoden har dock nackdelen att det krävs en direktkanal med den andra personen för att ta emot eller skicka pengar, vilket innebär en öppningstransaktion och en stängningstransaktion för varje kanal. Om jag planerar att göra ett stort antal betalningar med den här personen blir det kostnadseffektivt att öppna och stänga en kanal. Om jag däremot bara behöver utföra ett fåtal Lightning-transaktioner är det inte fördelaktigt att öppna en direktkanal, eftersom det skulle kosta mig 2 On-Chain-transaktioner för ett begränsat antal off-chain-transaktioner. Detta fall kan till exempel inträffa när man vill betala med Lightning hos en handlare utan att planera att återvända.


För att lösa detta problem gör Lightning Network det möjligt att dirigera en betalning genom flera kanaler och mellanliggande noder, vilket möjliggör en transaktion utan en direktkanal med den andra personen.


Tänk dig till exempel det:



- Alice** (i orange) har en kanal med **Suzie** (i grått) med **100 000 satoshis** på sin sida och **30 000 satoshis** på Suzies sida.
- Suzie** har en kanal med **Bob** i vilken hon äger **250 000 satoshis** och där Bob inte har några satoshis.


![LNP201](assets/en/37.webp)


Om Alice vill skicka pengar till Bob utan att öppna en direktkanal med honom måste hon gå via Suzie, och varje kanal måste justera likviditeten på vardera sidan. **De skickade satoshierna stannar inom sina respektive kanaler**; de "korsar" faktiskt inte kanalerna, utan överföringen görs via en justering av den interna likviditeten i varje kanal.


Antag att Alice vill skicka **50 000 satoshis** till Bob:



- Alice** skickar 50 000 satoshis till **Suzie** i deras gemensamma kanal.
- Suzie** replikerar denna överföring genom att skicka 50 000 satoshis till **Bob** i deras kanal.


![LNP201](assets/en/38.webp)


Betalningen dirigeras således till Bob via en likviditetsrörelse i varje kanal. I slutet av transaktionen slutar Alice med 50 000 Sats. Hon har verkligen överfört 50 000 Sats eftersom hon ursprungligen hade 100 000. Bob, å sin sida, får ytterligare 50 000 Sats. För Suzie (den mellanliggande noden) är denna operation neutral: initialt hade hon 30 000 Sats i sin kanal med Alice och 250 000 Sats i sin kanal med Bob, totalt 280 000 Sats. Efter operationen har hon 80 000 Sats i sin kanal med Alice och 200 000 Sats i sin kanal med Bob, vilket är samma summa som vid starten.


Denna överföring begränsas således av den **tillgängliga likviditeten** i överföringsriktningen.


### Beräkning av Route- och likviditetslimiterna


Låt oss ta ett teoretiskt exempel på ett annat nätverk med:



- 130.000 satoshis** på Alice:s sida (i orange) i hennes kanal med **Suzie** (i grått).
- 90.000 satoshis** på **Suzie's** sida och **200.000 satoshis** på **Carol's** sida (i rosa).
- 150.000 satoshis** på **Carols** sida och **100.000 satoshis** på **Bob:s** sida.


![LNP201](assets/en/39.webp)


Det maximala belopp som Alice kan skicka till Bob i denna konfiguration är **90 000 satoshis**, eftersom hon begränsas av den minsta tillgängliga likviditeten i kanalen från **Suzie till Carol**. I motsatt riktning (från Bob till Alice) är ingen betalning möjlig eftersom **Suzus** sida i kanalen med **Alice** inte innehåller några satoshis. Därför finns det **ingen rutt** som kan användas för en överföring i den här riktningen.

Alice skickar **40 000 satoshis** till Bob genom kanalerna:



- Alice överför 40 000 satoshis till sin kanal med Suzie.
- Suzie överför 40 000 satoshis till Carol i deras gemensamma kanal.
- Carol överför slutligen 40 000 satoshis till Bob.


![LNP201](assets/en/40.webp)


De **satoshis som skickas** i varje kanal **förblir i kanalen**, så de satoshis som skickas av Carol till Bob är inte desamma som de som skickas av Alice till Suzie. Överföringen görs endast genom att justera likviditeten i varje kanal. Dessutom förblir kanalernas totala kapacitet oförändrad.


![LNP201](assets/en/41.webp)


Precis som i det föregående exemplet har källnoden (Alice) 40 000 satoshis mindre efter transaktionen. De mellanliggande noderna (Suzie och Carol) behåller samma totala belopp, vilket gör transaktionen neutral för dem. Slutligen får destinationsnoden (Bob) ytterligare 40 000 satoshis.


De mellanliggande nodernas roll är därför mycket viktig för Lightning Network:s funktion. De underlättar överföringar genom att erbjuda flera vägar för betalningar. För att uppmuntra dessa noder att tillhandahålla sin likviditet och delta i routningen av betalningar betalas **routingavgifter** till dem.


### Avgifter för routning


De mellanliggande noderna tillämpar avgifter för att tillåta betalningar att passera genom deras kanaler. Dessa avgifter fastställs av **varje nod för varje kanal**. Avgifterna består av 2 Elements:



- "**Base fee**": ett fast belopp per kanal, ofta **1 sat** som standard, men kan anpassas.
- "**Variabel avgift**": en procentandel av det överförda beloppet, beräknad i **delar per miljon (ppm)**. Som standard är den **1 ppm** (1 sat per miljon överförda satoshis), men den kan också justeras.


Avgifterna skiljer sig också åt beroende på i vilken riktning överföringen sker. Till exempel, för en överföring från Alice till Suzie, gäller Alice:s avgifter. Omvänt, från Suzie till Alice, används Suzies avgifter.


Till exempel, för en kanal mellan Alice och Suzie, skulle vi kunna ha:



- Alice**: Grundavgift på 1 sat och 1 ppm för rörliga avgifter.
- Suzie**: Grundavgift på 0,5 procent och 10 procent för rörliga avgifter.


![LNP201](assets/en/42.webp)


För att bättre förstå hur avgifterna fungerar, låt oss studera samma Lightning Network som tidigare, men nu med följande routingavgifter:



- Kanal **Alice - Suzie**: Grundavgift på 1 Satoshi och 1 ppm för Alice.
- Kanal **Suzie - Carol**: grundavgift på 0 Satoshi och 200 ppm för Suzie.
- Carol - Bob** Kanal: grundavgift på 1 Satoshi och 1 ppm för Suzie 2.

![LNP201](assets/en/43.webp)


För samma betalning på **40 000 satoshis** till Bob måste Alice skicka lite mer, eftersom varje mellanliggande nod drar av sina avgifter:



- Carol** drar av 1,04 satoshis på kanalen med Bob:

$$ f*{\text{Carol-Bob}} = \text{basavgift} + \left(\frac{\text{ppm} \times \text{belopp}}{10^6}\right) $$$

$$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0,04 = 1,04 \text{ Sats} $$



- Suzie** drar av 8 satoshis i avgifter på kanalen med Carol:

$$ f*{\text{Suzie-Carol}} = \text{basavgift} + \left(\frac{\text{ppm} \times \text{belopp}}{10^6}\right) $$$

$$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ Sats} $$


De totala avgifterna för denna betalning på denna väg är därför **9,04 satoshis**. Således måste Alice skicka **40 009,04 satoshis** för att Bob ska få exakt **40 000 satoshis**.


![LNP201](assets/en/44.webp)


Likviditeten är därför uppdaterad:


![LNP201](assets/en/45.webp)


### Routning av lökar


För att dirigera en betalning från avsändaren till mottagaren använder Lightning Network en metod som kallas "**onion routing**". Till skillnad från routning av klassiska data, där varje router bestämmer riktningen för data baserat på deras destination, fungerar onion routing annorlunda:



- Den sändande noden beräknar hela rutten**: Alice bestämmer t.ex. att hennes betalning måste gå via Suzie och Carol innan den når Bob.
- Varje mellanliggande nod känner bara till sin närmaste granne**: Suzie vet bara att hon har fått pengar från Alice och att hon måste överföra dem till Carol. Suzie vet dock inte om Alice är källnoden eller en mellanliggande nod, och hon vet inte heller om Carol är mottagarnoden eller bara en annan mellanliggande nod. Denna princip gäller även för Carol och alla andra noder på vägen. Onion routing bevarar således transaktionernas konfidentialitet genom att maskera avsändarens och den slutliga mottagarens identitet.

För att säkerställa att den sändande noden kan beräkna en komplett rutt till mottagaren i onion routing måste den upprätthålla en **nätverksgraf** för att känna till sin topologi och bestämma möjliga rutter.

**Vad ska du ta med dig från detta kapitel?



- På Lightning kan betalningar dirigeras mellan noder som är indirekt anslutna via mellanliggande kanaler. Var och en av dessa mellanliggande noder underlättar likviditetsreläet.
- Förmedlande noder får en provision för sin tjänst, bestående av fasta och rörliga avgifter.
- Onion routing gör det möjligt för den sändande noden att beräkna hela rutten utan att mellanliggande noder känner till källan eller slutdestinationen.


I det här kapitlet har vi utforskat betalningsrouting på Lightning Network. Men en fråga uppstår: vad hindrar mellanliggande noder från att acceptera en inkommande betalning utan att vidarebefordra den till nästa destination, i syfte att snappa upp transaktionen? Det är just HTLC:ernas roll som vi kommer att studera i följande kapitel.


## HTLC - Hashed Time Locked Contract


<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>


:::video id=6f204b92-55a5-4939-9440-7c5b96a297bf:::


I det här kapitlet kommer vi att upptäcka hur Lightning gör det möjligt för betalningar att passera genom mellanliggande noder utan att behöva lita på dem, tack vare **HTLC** (_Hashed Time-Locked Contracts_). Dessa smarta kontrakt säkerställer att varje mellanliggande nod endast får pengarna från sin kanal om den vidarebefordrar betalningen till den slutliga mottagaren, annars valideras inte betalningen.


Den fråga som uppstår för betalningsdirigering är därför den nödvändiga tilliten till mellanliggande noder och mellan de mellanliggande noderna själva. För att illustrera detta, låt oss återgå till vårt förenklade Lightning Network-exempel med 3 noder och 2 kanaler:



- Alice har en kanal med Suzie.
- Suzie har en kanal med Bob.


Alice vill skicka 40 000 Sats till Bob men hon har ingen direktkanal med honom och vill inte öppna en. Hon letar efter en väg och bestämmer sig för att gå genom Suzies nod.


![LNP201](assets/en/46.webp)


Om Alice naivt skickar 40 000 satoshis till Suzie i hopp om att Suzie ska överföra denna summa till Bob, kan Suzie behålla pengarna för sig själv och inte överföra något till Bob.


![LNP201](assets/en/47.webp)

För att undvika den här situationen använder vi på Lightning HTLC:er (Hashed Time-Locked Contracts), som gör betalningen till den mellanliggande noden villkorad, vilket innebär att Suzie måste uppfylla vissa villkor för att få tillgång till Alice:s medel och överföra dem till Bob.


### Hur HTLC:er fungerar


En HTLC är en speciell Contract som bygger på två principer:



- Villkor för åtkomst**: Mottagaren måste avslöja en hemlighet för att låsa upp betalningen som ska betalas till dem.
- Förfallodatum**: Om betalningen inte är helt genomförd inom en definierad period avbryts den och pengarna återgår till avsändaren.


Så här fungerar den här processen i vårt exempel med Alice, Suzie och Bob:


![LNP201](assets/en/48.webp)


**Skapande av hemligheten**: Bob genererar en slumpmässig hemlighet med beteckningen _s_ (förbilden) och beräknar dess Hash med beteckningen _r_ med Hash-funktionen med beteckningen _h_. Vi har:


$$
r = h(s)
$$


Om man använder en Hash-funktion är det omöjligt att hitta _s_ med endast _h(s)_, men om _s_ tillhandahålls är det lätt att verifiera att den motsvarar _h(s)_.


![LNP201](assets/en/49.webp)


**Skickar begäran om betalning**: Bob skickar en **Invoice** till Alice med en begäran om betalning. Denna Invoice inkluderar särskilt Hash _r_.


![LNP201](assets/en/50.webp)


**Skickar den villkorade betalningen**: Alice skickar en HTLC på 40 000 satoshis till Suzie. Villkoret för att Suzie ska få dessa pengar är att hon förser Alice med en hemlig _s'_ som uppfyller följande ekvation:


$$
h(s') = r
$$


![LNP201](assets/en/51.webp)


**Överföring av HTLC till den slutliga mottagaren**: För att få de 40 000 satoshierna från Alice måste Suzie överföra en liknande HTLC på 40 000 satoshier till Bob, som har samma villkor, nämligen att han måste förse Suzie med en hemlig _s'_ som uppfyller ekvationen:


$$
h(s') = r
$$


![LNP201](assets/en/52.webp)


**Validering genom hemliga _s_**: Bob ger _s_ till Suzie för att få de 40 000 satoshis som utlovades i HTLC. Med denna hemlighet kan Suzie sedan låsa upp Alice:s HTLC och få de 40 000 satoshierna från Alice. Betalningen dirigeras sedan korrekt till Bob.


![LNP201](assets/en/53.webp)

Denna process hindrar Suzie från att behålla Alice:s medel utan att slutföra överföringen till Bob, eftersom hon måste skicka betalningen till Bob för att få hemliga _s_ och därmed låsa upp Alice:s HTLC. Operationen förblir densamma även om rutten innehåller flera mellanliggande noder: det är helt enkelt en fråga om att upprepa Suzies steg för varje mellanliggande nod. Varje nod skyddas av villkoren för HTLC:erna, eftersom upplåsning av den sista HTLC av mottagaren automatiskt utlöser upplåsning av alla andra HTLC:er i en kaskad.


### Utgångsdatum och hantering av HTLC i händelse av problem


Om en av de förmedlande noderna eller mottagarnoden slutar svara under betalningsprocessen, särskilt vid ett internet- eller strömavbrott, kan betalningen inte slutföras eftersom den hemlighet som behövs för att låsa upp HTLC:erna inte överförs. I vårt exempel med Alice, Suzie och Bob uppstår detta problem till exempel om Bob inte sänder hemligheten _s_ till Suzie. I detta fall blockeras alla HTLC:er uppströms vägen och de medel som de säkrar likaså.


![LNP201](assets/en/54.webp)


För att undvika detta har HTLC:er på Lightning en utgångsdatum som gör det möjligt att ta bort HTLC om den inte är slutförd efter en viss tid. Utgången följer en specifik ordning eftersom den börjar först med den HTLC som är närmast mottagaren och sedan successivt flyttas upp till transaktionens utfärdare. I vårt exempel, om Bob aldrig ger hemligheten _s_ till Suzie, skulle detta först leda till att Suzies HTLC mot Bob upphör att gälla.


![LNP201](assets/en/55.webp)


Sedan HTLC från Alice till Suzie.


![LNP201](assets/en/56.webp)


Om utgångsordningen var omvänd skulle Alice kunna återfå sin betalning innan Suzie kunde skydda sig mot potentiellt fusk. Om Bob kommer tillbaka för att göra anspråk på sin HTLC medan Alice redan har tagit bort sin, skulle Suzie faktiskt vara i underläge. Denna kaskadordning av HTLC-utgång säkerställer således att ingen mellanliggande nod lider av orättvisa förluster.


### Representation av HTLC:er i Commitment-transaktioner


Commitment-transaktioner representerar HTLC:er på ett sådant sätt att de villkor de ställer på Lightning kan överföras till Bitcoin i händelse av en påtvingad kanalstängning under livslängden för en HTLC. Som en påminnelse representerar Commitment-transaktioner det aktuella tillståndet för kanalen mellan de två användarna och möjliggör en ensidig tvingad stängning i händelse av problem. För varje nytt tillstånd i kanalen skapas 2 Commitment-transaktioner: en för varje part. Låt oss återgå till vårt exempel med Alice, Suzie och Bob, men titta närmare på vad som händer på kanalnivå mellan Alice och Suzie när HTLC skapas.

![LNP201](assets/en/57.webp)


Innan betalningen av 40 000 Sats mellan Alice och Bob påbörjas har Alice 100 000 Sats i sin kanal med Suzie, medan Suzie har 30 000. Deras Commitment-transaktioner är följande:


![LNP201](assets/en/58.webp)


Alice har just fått Bob:s Invoice, som innehåller _r_, hemlighetens Hash. Hon kan således konstruera en HTLC på 40 000 satoshis med Suzie. Denna HTLC representeras i de senaste Commitment-transaktionerna som en utgång som kallas "**_HTLC Out_**" på Alice:s sida, eftersom medlen är utgående, och "**_HTLC In_**" på Suzies sida, eftersom medlen är inkommande.


![LNP201](assets/en/59.webp)


Dessa utgångar som är förknippade med HTLC har exakt samma villkor, nämligen:



- Om Suzie kan tillhandahålla de hemliga _s_ kan hon låsa upp denna utdata omedelbart och överföra den till en Address som hon kontrollerar.
- Om Suzie inte har hemligheten _s_ kan hon inte låsa upp denna utgång, och Alice kommer att kunna låsa upp den efter en tidslåsning för att skicka den till en Address som hon kontrollerar. Tidslåset ger alltså Suzie en period att reagera om hon får tag på _s_.


Dessa villkor gäller endast om kanalen är stängd (dvs. en Commitment Transaction publiceras On-Chain) medan HTLC fortfarande är aktiv på Lightning, vilket innebär att betalningen mellan Alice och Bob ännu inte har slutförts och HTLC:erna ännu inte har löpt ut. Tack vare dessa villkor kan Suzie återfå de 40 000 satoshis av HTLC som hon är skyldig genom att tillhandahålla _s_. Annars återfår Alice medlen efter att tidslåset har löpt ut, för om Suzie inte känner till _s_ betyder det att hon inte har överfört de 40 000 satoshierna till Bob, och därför är Alice:s medel inte skyldiga henne.


Om kanalen stängs medan flera HTLC:er pågår kommer det dessutom att finnas lika många ytterligare utgångar som det finns pågående HTLC:er.

Om kanalen inte är stängd skapas nya Commitment-transaktioner efter att Lightning-betalningen har löpt ut eller lyckats för att återspegla kanalens nya, nu stabila, tillstånd, det vill säga utan några väntande HTLC:er. Utgångarna som är relaterade till HTLC:erna kan därför tas bort från Commitment-transaktionerna.

![LNP201](assets/en/60.webp)


Slutligen, i händelse av en kooperativ kanalstängning medan en HTLC är aktiv, slutar Alice och Suzie att acceptera nya betalningar och väntar på upplösningen eller utgången av de pågående HTLC:erna. Detta gör det möjligt för dem att publicera en lättare stängningstransaktion utan utdata relaterade till HTLC:erna, vilket minskar avgifterna och undviker väntan på en eventuell tidslåsning.


**Vad ska du ta med dig från detta kapitel?


HTLC:er gör det möjligt att dirigera Lightning-betalningar genom flera noder utan att behöva lita på dem. Här är de viktigaste punkterna att komma ihåg:



- HTLC säkerställer betalningars säkerhet genom en hemlighet (preimage) och en expeditionstid.
- Upplösningen eller utgången av HTLC följer en specifik ordning: sedan från destinationen mot källan, för att skydda varje nod.
- Så länge som en HTLC varken är löst eller utgången bibehålls den som en utgång i de senaste Commitment-transaktionerna.


I nästa kapitel kommer vi att se hur en nod som utfärdar en Lightning-transaktion hittar och väljer vägar för att betalningen ska nå mottagarnoden.


## Hitta din väg


<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>


:::video id=e5baa834-111d-46f5-a28b-3538bed2bbb0:::


I de tidigare kapitlen har vi sett hur man kan använda andra noders kanaler för att dirigera betalningar och nå en nod utan att vara direkt ansluten till den via en kanal. Vi diskuterade också hur man kan garantera säkerheten i överföringen utan att lita på de mellanliggande noderna. I det här kapitlet fokuserar vi på att hitta den bästa möjliga vägen för att nå en målnod.


### Problemet med routing i blixtnedslag


Som vi har sett är det i Lightning den betalningsavsändande noden som måste beräkna hela vägen till mottagaren, eftersom vi använder ett onion routing-system. De mellanliggande noderna känner inte till vare sig ursprungspunkten eller slutdestinationen. De vet bara varifrån betalningen kommer och till vilken nod de ska överföra den. Detta innebär att den sändande noden måste upprätthålla en dynamisk lokal topologi över nätverket, med de befintliga Lightning-noderna och kanalerna mellan dem, med hänsyn till öppningar, stängningar och statusuppdateringar.


![LNP201](assets/en/61.webp)

Även med denna topologi för Lightning Network finns det viktig information för routning som förblir otillgänglig för den sändande noden, nämligen den exakta fördelningen av likviditet i kanalerna vid varje givet ögonblick. Varje kanal visar bara sin **totala kapacitet**, men den interna fördelningen av medel är bara känd av de två deltagande noderna. Detta innebär utmaningar för en effektiv routing, eftersom framgången för betalningen framför allt beror på om beloppet är lägre än den lägsta likviditeten på den valda rutten. Alla likviditeter är dock inte synliga för den sändande noden.

![LNP201](assets/en/62.webp)


### Uppdatering av nätverkskarta


För att hålla sin nätverkskarta uppdaterad skickar noderna regelbundet Exchange-meddelanden genom en algoritm som kallas "**_gossip_**". Detta är en distribuerad algoritm som används för att sprida information på ett epidemiskt sätt till alla noder i nätverket, vilket möjliggör Exchange och synkronisering av Global State i kanalerna på några få kommunikationscykler. Varje nod sprider information till en eller flera grannar som väljs slumpmässigt eller inte, dessa sprider i sin tur informationen till andra grannar och så vidare tills ett globalt synkroniserat tillstånd har uppnåtts.


De två viktigaste meddelandena som utväxlas mellan Lightning-noderna är följande:



- "**Channel Announcements**": meddelanden som signalerar öppnandet av en ny kanal.
- "**Channel Updates**": uppdateringsmeddelanden om läget för en kanal, särskilt om utvecklingen av avgifter (men inte om fördelningen av likviditet).


Lightning-noderna övervakar även Bitcoin Blockchain för att upptäcka transaktioner som stänger kanaler. Den stängda kanalen tas sedan bort från kartan eftersom den inte längre kan användas för att dirigera våra betalningar.


### Routning av en betalning


Låt oss ta ett exempel på en liten Lightning Network med 7 noder: Alice, Bob, 1, 2, 3, 4 och 5. Föreställ dig att Alice vill skicka en betalning till Bob men måste gå via mellanliggande noder.


![LNP201](assets/en/63.webp)


Så här ser den faktiska fördelningen av medel i dessa kanaler ut:



- Kanal mellan Alice och 1**: 250.000 Sats på Alice:s sida, 80.000 på 1:s sida (total kapacitet på 330.000 Sats).
- Kanal mellan 1 och 2**: 300.000 Sats på 1:ans sida, 200.000 på 2:ans sida (total kapacitet 500.000 Sats).
- Kanal mellan 2 och 3**: 50.000 Sats på 2:ans sida, 60.000 på 3:ans sida (total kapacitet på 110.000 Sats).
- Kanal mellan 2 och 5**: 90.000 Sats på sida 2, 160.000 på sida 5 (total kapacitet på 250.000 Sats).
- Kanal mellan 2 och 4**: 180.000 Sats på sida 2, 110.000 på sida 4 (total kapacitet 290.000 Sats).
- Kanal mellan 4 och 5**: 200.000 Sats på sida 4, 10.000 på sida 5 (total kapacitet på 210.000 Sats).
- Kanal mellan 3 och Bob**: 50.000 Sats på sida 3, 250.000 på sida Bob (total kapacitet på 300.000 Sats).
- Kanal mellan 5 och Bob**: 260.000 Sats på sidan 5, 100.000 på sidan Bob (total kapacitet på 360.000 Sats).


![LNP201](assets/en/64.webp)


För att göra en betalning på 100 000 Sats från Alice till Bob begränsas dirigeringsalternativen av den tillgängliga likviditeten i varje kanal. Den optimala rutten för Alice, baserat på de kända likviditetsfördelningarna, skulle kunna vara sekvensen `Alice → 1 → 2 → 4 → 5 → Bob`:


![LNP201](assets/en/65.webp)


Men eftersom Alice inte känner till den exakta fördelningen av medel i varje kanal måste hon uppskatta den optimala rutten probabilistiskt, med beaktande av följande kriterier:



- Sannolikhet för framgång**: en kanal med högre total kapacitet är mer sannolik att innehålla tillräcklig likviditet. Till exempel har kanalen mellan nod 2 och nod 3 en total kapacitet på 110 000 Sats, så det är osannolikt att hitta 100 000 Sats eller mer på sidan av nod 2, även om det fortfarande är möjligt.
- Transaktionsavgifter**: När den sändande noden väljer den bästa rutten tar den också hänsyn till de avgifter som varje mellanliggande nod tar ut och försöker minimera den totala rutten.
- Utgångsdatum för HTLC**: För att undvika blockerade betalningar är utgångsdatumet för HTLC också en parameter att ta hänsyn till.
- Antal mellanliggande noder**: Slutligen, och mer allmänt, kommer den sändande noden att försöka hitta en rutt med så få noder som möjligt för att minska risken för misslyckande och begränsa avgifterna för blixttransaktioner.


Genom att analysera dessa kriterier kan den sändande noden testa de mest sannolika rutterna och försöka optimera dem. I vårt exempel skulle Alice kunna rangordna de bästa rutterna enligt följande:



- `Alice → 1 → 2 → 5 → Bob`, eftersom det är den kortaste vägen med den högsta kapaciteten.
- `Alice → 1 → 2 → 4 → 5 → Bob`, eftersom denna rutt erbjuder god kapacitet, även om den är längre än den första.
- `Alice → 1 → 2 → 3 → Bob`, eftersom denna rutt inkluderar kanalen `2 → 3`, som har mycket begränsad kapacitet, men som fortfarande är potentiellt användbar.


### Verkställande av betalning


Alice beslutar sig för att testa sin första rutt (`Alice → 1 → 2 → 5 → Bob`). Hon skickar därför en HTLC på 100 000 Sats till nod 1. Denna nod kontrollerar att den har tillräcklig likviditet med nod 2 och fortsätter överföringen. Node 2 tar sedan emot HTLC från nod 1, men inser att den inte har tillräckligt med likviditet i sin kanal med nod 5 för att dirigera en betalning på 100 000 Sats. Den skickar då ett felmeddelande tillbaka till nod 1, som sänder det till Alice. Den här rutten har misslyckats.


![LNP201](assets/en/66.webp)


Alice försöker sedan dirigera sin betalning genom att använda sin andra rutt (`Alice → 1 → 2 → 4 → 5 → Bob`). Hon skickar en HTLC på 100 000 Sats till nod 1, som sänder den till nod 2, sedan till nod 4, till nod 5 och slutligen till Bob. Den här gången är likviditeten tillräcklig och rutten fungerar. Varje nod låser upp sin HTLC i kaskad med hjälp av förbilden som tillhandahålls av Bob (hemligheten _s_), vilket gör att Alice:s betalning till Bob kan slutföras.


![LNP201](assets/en/67.webp)


Sökningen efter en rutt går till på följande sätt: den sändande noden börjar med att identifiera de bästa möjliga rutterna och försöker sedan med betalningar successivt tills en fungerande rutt hittas.


Det är värt att notera att Bob kan förse Alice med information i **Invoice** för att underlätta dirigeringen. Han kan till exempel ange närliggande kanaler med tillräcklig likviditet eller avslöja förekomsten av privata kanaler. Dessa indikationer gör det möjligt för Alice att undvika rutter med liten chans att lyckas och att först försöka de vägar som rekommenderas av Bob.


**Vad ska du ta med dig från detta kapitel?



- Noderna upprätthåller en karta över nätverkstopologin genom meddelanden och genom att övervaka kanalstängningar på Bitcoin Blockchain.
- Sökandet efter en optimal rutt för en betalning är fortfarande probabilistisk och beror på många kriterier.
- Bob kan ge indikationer i **Invoice** för att vägleda Alice:s routing och rädda henne från att testa osannolika rutter.


I följande kapitel kommer vi särskilt att studera hur fakturor fungerar, utöver några andra verktyg som används på Lightning Network.


# Lightning Network:s verktyg


<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>


## Invoice, LNURL och Keysend


<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

:::video id=309c3412-506e-4189-ad46-5e5088c55008:::


I det här kapitlet tittar vi närmare på hur Lightning **fakturor** fungerar, det vill säga betalningsbegäran som skickas från mottagarnoden till avsändarnoden. Målet är att förstå hur man betalar och tar emot betalningar på Lightning. Vi kommer också att diskutera 2 alternativ till klassiska fakturor: LNURL och Keysend.


![LNP201](assets/en/68.webp)


### Strukturen för blixtfakturor


Som förklaras i kapitlet om HTLC:er börjar varje betalning med att mottagaren genererar en **Invoice**. Denna Invoice överförs sedan till betalaren (via en QR-kod eller genom att kopiera och klistra in) för att initiera betalningen. En Invoice består av två huvuddelar:



- The Human Readable Part**: detta avsnitt innehåller tydliga metadata för att förbättra användarupplevelsen.
- Payload**: Detta avsnitt innehåller information som är avsedd för maskiner som ska behandla betalningen.


Den typiska strukturen för en Invoice börjar med en identifierare `LN` för "Lightning", följt av `bc` för Bitcoin, sedan mängden Invoice. En separator `1` skiljer den mänskligt läsbara delen från datadelen (nyttolasten).


Låt oss ta följande Invoice som ett exempel:


```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```


Vi kan redan dela upp den i 2 delar. Först är det den mänskliga läsbara delen:


```invoice
lnbc100u
```


Sedan den del som är avsedd för nyttolasten:


```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```


De två delarna är åtskilda med ett `1`. Denna separator valdes istället för ett specialtecken för att göra det möjligt att enkelt kopiera och klistra in hela Invoice genom att dubbelklicka.


I den första delen kan vi se det:



- `LN` indikerar att det är en Lightning-transaktion.
- `bc` indikerar att Lightning Network är på Bitcoin Blockchain (och inte på Testnet eller på Litecoin).
- `100u` anger mängden Invoice, uttryckt i **microbitcoins** (`u` betyder "mikro"), vilket här motsvarar 10 000 Sats.


För att beteckna betalningsbeloppet uttrycks det i underenheter av Bitcoin. Här är de enheter som används:



- Millibitcoin (betecknas "m"):** Representerar en tusendel av en Bitcoin.


$$
1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
$$



- Microbitcoin (betecknad `u`):** Även ibland kallad "bit", representerar en miljondel av en Bitcoin.


$$
1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
$$



- Nanobitcoin (betecknas "n"):** Representerar en miljarddel av en Bitcoin.


$$
1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
$$



- Picobitcoin (betecknas "p"):** Representerar en biljondel av en Bitcoin.

$$
1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
$$


### Nyttolasten i en Invoice


Nyttolasten i en Invoice innehåller flera delar av den information som krävs för att behandla betalningen:



- Timestamp:** Tidpunkten för Invoice:s skapande, uttryckt i Unix Timestamp (antalet sekunder som har förflutit sedan den 1 januari 1970).
- Hashning av hemligheten**: Som vi såg i avsnittet om HTLC:er måste den mottagande noden förse den sändande noden med Hash för förbilden. Detta används i HTLC:er för att säkra transaktionen. Vi refererade till det som "_r_".
- Betalningshemligheten**: En annan hemlighet genereras av mottagaren, men den här gången överförs den till den sändande noden. Den används i onion routing för att förhindra att mellanliggande noder kan gissa om nästa nod är den slutliga mottagaren eller inte. På så sätt upprätthålls en form av konfidentialitet för mottagaren i förhållande till den sista mellanliggande noden på rutten.
- Mottagarens publika nyckel**: Anger för betalaren identifikationskoden för den person som ska betalas.
- Utgångstiden**: Den maximala tid som Invoice ska betalas (1 timme som standard).
- Tips om betalningsväg**: Ytterligare information som tillhandahålls av mottagaren för att hjälpa avsändaren att optimera betalningsvägen.
- Signaturen**: Garanterar Invoice:s integritet genom att autentisera all information.


Fakturorna kodas sedan i **bech32**, samma format som för Bitcoin SegWit-adresser (format som börjar med `bc1`).


### LNURL Återkallande


I en traditionell transaktion, till exempel ett köp i en butik, genereras Invoice för det totala belopp som ska betalas. När Invoice har presenterats (i form av en QR-kod eller teckensträng) kan kunden skanna den och slutföra transaktionen. Betalningen följer sedan den traditionella process som vi studerade i föregående avsnitt. Denna process kan dock ibland vara mycket besvärlig för användarupplevelsen, eftersom den kräver att mottagaren skickar information till avsändaren via Invoice.


För vissa situationer, som att ta ut bitcoins från en onlinetjänst, är den traditionella processen för besvärlig. I sådana fall förenklar **LNURL** uttagslösningen denna process genom att visa en QR-kod som mottagarens Wallet skannar för att automatiskt skapa Invoice. Tjänsten betalar sedan Invoice, och användaren ser helt enkelt ett omedelbart uttag.


![LNP201](assets/en/69.webp)


LNURL är ett kommunikationsprotokoll som specificerar en uppsättning funktioner som är utformade för att förenkla interaktioner mellan Lightning-noder och klienter samt tredjepartsapplikationer. LNURL-återkallandet, som vi just har sett, är alltså bara ett exempel bland andra funktionaliteter.

Detta protokoll är baserat på HTTP och gör det möjligt att skapa länkar för olika operationer, t.ex. en betalningsbegäran, en uttagsbegäran eller andra funktioner som förbättrar användarupplevelsen. Varje LNURL är en bech32-kodad URL med prefixet lnurl, som när den har skannats utlöser en serie automatiska åtgärder på Lightning Wallet.

Funktionen LNURL-Withdraw (LUD-03) gör det till exempel möjligt att ta ut pengar från en tjänst genom att skanna en QR-kod, utan att manuellt behöva generate och Invoice. På samma sätt gör LNURL-auth (LUD-04) det möjligt att logga in på onlinetjänster med hjälp av en privat nyckel på ens Lightning Wallet istället för ett lösenord.


### Skicka en Lightning-betalning utan Invoice: Keysend


Ett annat intressant fall är överföringen av pengar utan att ha fått en Invoice i förväg, så kallad "**Keysend**". Detta protokoll gör det möjligt att skicka pengar genom att lägga till en förbild i de krypterade betalningsuppgifterna, som endast mottagaren har tillgång till. Denna förbild gör det möjligt för mottagaren att låsa upp HTLC och på så sätt hämta pengarna utan att ha genererat en Invoice i förväg.


För att förenkla är det i detta protokoll avsändaren som genererar den hemlighet som används i HTLC:erna, snarare än mottagaren. I praktiken innebär det att avsändaren kan göra en betalning utan att behöva interagera med mottagaren i förväg.


![LNP201](assets/en/70.webp)


**Vad ska du ta med dig från detta kapitel?



- En **Lightning Invoice** är en betalningsbegäran som består av en del som kan läsas av människor och en del med maskindata.
- Invoice är kodad i **bech32**, med en `1`-separator för att underlätta kopiering och en datadel som innehåller all information som krävs för att behandla betalningen.
- Andra betalningsprocesser finns på Lightning, särskilt **LNURL-Withdraw** för att underlätta uttag och **Keysend** för direktöverföringar utan en Invoice.


I följande kapitel kommer vi att se hur en nodoperatör kan hantera likviditeten i sina kanaler, för att aldrig bli blockerad och alltid kunna skicka och ta emot betalningar på Lightning Network.


## Hantera din likviditet


<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>


:::video id=96096aef-e4ce-4c44-a022-57e27082232a:::


I det här kapitlet kommer vi att utforska strategier för att effektivt hantera likviditeten på Lightning Network. Likviditetshanteringen varierar beroende på typ av användare och sammanhang. Vi kommer att titta på huvudprinciperna och befintliga tekniker för att bättre förstå hur man optimerar denna hantering.


### Likviditetsbehov


Det finns tre huvudsakliga användarprofiler på Lightning, var och en med specifika likviditetsbehov:



- Betalaren**: Det här är den som gör betalningar. De behöver utgående likviditet för att kunna överföra pengar till andra användare. Det kan till exempel vara en konsument.
- Säljaren (eller betalningsmottagaren)**: Detta är den som tar emot betalningar. De behöver inkommande likviditet för att kunna ta emot betalningar till sin nod. Det kan till exempel vara ett företag eller en webbutik.
- Routern**: En förmedlande nod, ofta specialiserad på att dirigera betalningar, som måste optimera sin likviditet i varje kanal för att dirigera så många betalningar som möjligt och tjäna avgifter.


Dessa profiler är naturligtvis inte fasta, utan en användare kan växla mellan betalare och betalningsmottagare beroende på transaktionerna. Bob kan till exempel få sin lön på Lightning från sin arbetsgivare, vilket placerar honom i positionen som "säljare" som kräver inkommande likviditet. Om han sedan vill använda sin lön för att köpa mat blir han en "betalare" och måste då ha utgående likviditet.


För att förstå bättre kan vi ta ett exempel på ett enkelt nätverk som består av tre noder: köparen (Alice), routern (Suzie) och säljaren (Bob).


![LNP201](assets/en/71.webp)


Föreställ dig att köparen vill skicka 30 000 Sats till säljaren och att betalningen går via routerns nod. Varje part måste då ha en minsta mängd likviditet i betalningsriktningen:



- Betalaren måste ha minst 30.000 satoshis på sin sida av kanalen med routern.
- Säljaren måste ha en kanal där 30.000 satoshis finns på motsatt sida för att kunna ta emot dem.
- Routern måste ha 30.000 satoshis på betalarens sida i sin kanal och även 30.000 satoshis på sin sida i kanalen med säljaren för att kunna dirigera betalningen.


![LNP201](assets/en/72.webp)


### Strategier för likviditetshantering


Betalare måste se till att upprätthålla tillräcklig likviditet på sin sida av kanalerna för att garantera utgående likviditet. Detta visar sig vara relativt enkelt, eftersom det räcker att öppna nya Lightning-kanaler för att ha denna likviditet. De initiala medlen som är låsta i Multisig On-Chain är faktiskt helt på betalarens sida i Lightning-kanalen i början. Betalningskapaciteten är således säkerställd så länge kanaler öppnas med tillräckligt med medel. När den utgående likviditeten är uttömd räcker det att öppna nya kanaler.

Å andra sidan är uppgiften mer komplex för säljaren. För att kunna ta emot betalningar måste de ha likviditet på den motsatta sidan av sina kanaler. Därför räcker det inte med att öppna en kanal: de måste också göra en betalning i denna kanal för att flytta likviditeten till den andra sidan innan de själva kan ta emot betalningar. För vissa Lightning-användarprofiler, till exempel handlare, finns det en tydlig disproportion mellan vad deras nod skickar och vad den tar emot, eftersom målet för ett företag i första hand är att samla in mer än det spenderar, för att generate göra en vinst. Lyckligtvis finns det flera lösningar för dessa användare med specifika behov av inkommande likviditet:



- Attrahera kanaler**: Handlaren har en fördel tack vare den volym av inkommande betalningar som förväntas på deras nod. Med hänsyn till detta kan de försöka locka till sig routingnoder som är ute efter intäkter från transaktionsavgifter och som kan öppna kanaler mot dem i hopp om att routa deras betalningar och ta ut de tillhörande avgifterna.



- Likviditetsrörelse**: Säljaren kan också öppna en kanal och överföra en del av pengarna till den motsatta sidan genom att göra fiktiva betalningar till en annan nod, som kommer att returnera pengarna på ett annat sätt. Vi kommer att se i nästa del hur man utför denna operation.



- Triangulär öppning**: Det finns plattformar för noder som vill öppna kanaler tillsammans, så att var och en kan dra nytta av omedelbart inkommande och utgående likviditet. Till exempel erbjuder [LightningNetwork+](https://lightningnetwork.plus/) den här tjänsten. Om Alice, Bob och Suzie vill öppna en kanal med 100 000 Sats kan de på denna plattform komma överens om att Alice ska öppna en kanal mot Bob, Bob mot Suzie och Suzie mot Alice. På detta sätt har var och en 100 000 Sats i utgående likviditet och 100 000 Sats i inkommande likviditet, samtidigt som de endast har låst upp 100 000 Sats.


![LNP201](assets/en/73.webp)



- Köpa kanaler**: Tjänster för att hyra Lightning-kanaler finns också för att få inkommande likviditet, som [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) eller [Lightning Labs Pool](https://lightning.engineering/pool/). Alice kan till exempel köpa en kanal på en miljon satoshis mot sin nod för att kunna ta emot betalningar.


![LNP201](assets/en/74.webp)


Slutligen, för routrar, vars mål är att maximera antalet betalningar som behandlas och de avgifter som tas ut, måste de:



- Öppna välfinansierade kanaler med strategiska noder.
- Regelbundet justera fördelningen av medel i kanalerna enligt nätverkets behov.


### The Loop Out Service


Tjänsten [Loop Out] (https://lightning.engineering/loop/), som erbjuds av Lightning Labs, gör det möjligt att flytta likviditet till den motsatta sidan av kanalen och samtidigt återkräva medlen på Bitcoin Blockchain. Till exempel skickar Alice 1 miljon satoshis via Lightning till en loop-nod, som sedan returnerar dessa medel till henne i On-Chain bitcoins. Detta balanserar hennes kanal med 1 miljon satoshis på varje sida, vilket optimerar hennes kapacitet att ta emot betalningar.


![LNP201](assets/en/75.webp)


Därför möjliggör denna tjänst inkommande likviditet samtidigt som man återkräver sina bitcoins On-Chain, vilket bidrar till att begränsa immobiliseringen av kontanter som behövs för att acceptera betalningar med Lightning.


**Vad ska du ta med dig från detta kapitel?



- För att skicka betalningar på Lightning måste du ha tillräckligt med likviditet på din sida i dina kanaler. För att öka denna sändningskapacitet öppnar du helt enkelt nya kanaler.
- För att ta emot betalningar måste du ha likviditet på den motsatta sidan i dina kanaler. Att öka denna mottagningskapacitet är mer komplicerat, eftersom det kräver att andra öppnar kanaler mot dig eller gör (fiktiva eller verkliga) betalningar för att flytta likviditeten till den andra sidan.
- Att upprätthålla önskad likviditet kan vara en ännu större utmaning beroende på hur kanalerna används. Det är därför det finns verktyg och tjänster som hjälper till att balansera kanalerna på önskat sätt.


I nästa kapitel kommer jag att gå igenom de viktigaste begreppen i denna utbildning.


# Gå vidare


<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>


## Sammanfattning av kursen



<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>


:::video id=5f4f4344-ef27-4765-8f09-8262e6833bde:::


I det här sista kapitlet som markerar slutet på LNP201-utbildningen föreslår jag att vi går igenom de viktiga begrepp som vi har behandlat tillsammans.


Målet med denna utbildning var att ge dig en omfattande och teknisk förståelse av Lightning Network. Vi upptäckte hur Lightning Network förlitar sig på Bitcoin Blockchain för att utföra off-chain-transaktioner, samtidigt som den behåller de grundläggande egenskaperna hos Bitcoin, särskilt avsaknaden av behovet av att lita på andra noder.


### Betalningskanaler


I de inledande kapitlen undersökte vi hur två parter, genom att öppna en betalningskanal, kan genomföra transaktioner utanför Bitcoin Blockchain. Här är de steg som behandlades:



- Öppnande av kanal**: Skapandet av kanalen sker genom en Bitcoin-transaktion som låser medlen i en 2/2 multisignatur Address. Denna insättning representerar Lightning-kanalen på Blockchain.


![LNP201](assets/en/76.webp) 2. **Transactions in the Channel**: In this channel, it is then possible to carry out numerous transactions without having to publish them on the blockchain. Each Lightning transaction creates a new state of the channel reflected in a commitment transaction.

![LNP201](assets/en/77.webp)



- Säkring och stängning**: Deltagarna förbinder sig till kanalens nya tillstånd genom att utbyta återkallningsnycklar för att säkra medlen och förhindra fusk. Båda parter kan stänga kanalen i samarbete genom att göra en ny transaktion på Bitcoin Blockchain, eller som en sista utväg genom en påtvingad stängning. Det senare alternativet är visserligen mindre effektivt eftersom det tar längre tid och ibland är dåligt utvärderat vad gäller avgifter, men det gör det ändå möjligt att återfå pengarna. Vid fusk kan offret straffa den som fuskar genom att återvinna alla medel från kanalen på Blockchain.


![LNP201](assets/en/78.webp)


### Nätverket av kanaler


Efter att ha studerat isolerade kanaler utvidgade vi vår analys till nätverket av kanaler:



- Routing**: När två parter inte är direkt anslutna via en kanal möjliggör nätverket routing via mellanliggande noder. Betalningarna går då från en nod till en annan.


![LNP201](assets/en/79.webp)



- HTLC:er**: Betalningar som går via mellanliggande noder säkras av "_Hash Time-Locked Contracts_" (HTLC), som gör det möjligt att låsa pengarna tills betalningen har slutförts från början till slut.


![LNP201](assets/en/80.webp)



- Onion Routing**: För att säkerställa betalningens konfidentialitet maskerar onion routing slutdestinationen för mellanliggande noder. Den sändande noden måste därför beräkna hela rutten, men i avsaknad av fullständig information om kanalernas likviditet fortsätter den genom successiva försök att dirigera betalningen.


![LNP201](assets/en/81.webp)


### Likviditetshantering


Vi har sett att likviditetshantering är en utmaning på Lightning för att säkerställa ett smidigt betalningsflöde. Att skicka betalningar är relativt enkelt: det kräver bara att man öppnar en kanal. För att ta emot betalningar krävs dock att man har likviditet på motsatt sida av sina kanaler. Här är några strategier som diskuterats:



- Locka till sig kanaler**: Genom att uppmuntra andra noder att öppna kanaler mot en själv erhåller en användare inkommande likviditet.



- Flyttning av likviditet**: Genom att skicka betalningar till andra kanaler flyttas likviditeten till den motsatta sidan.


![LNP201](assets/en/82.webp)



- Använda tjänster som Loop och Pool**: Dessa tjänster gör det möjligt att ombalansera eller köpa kanaler med likviditet på motsatt sida.

![LNP201](assets/en/83.webp)


- Öppningar i samarbete**: Det finns också plattformar tillgängliga för att ansluta för att utföra triangulära öppningar och för att ha inkommande likviditet.


![LNP201](assets/en/84.webp)


# Sista avsnittet


<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>


## Recensioner & betyg


<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>

<isCourseReview>true</isCourseReview>

## Slutlig tentamen


<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>

<isCourseExam>true</isCourseExam>

## Slutsats


<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>

<isCourseConclusion>true</isCourseConclusion>