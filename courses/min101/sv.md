---
name: Introduktion till Bitcoin mining
goal: Förstå Bitcoin mining och proof-of-work från grunden
objectives: 


  - Förstå proof-of-work och dess roll i Bitcoin.
  - Analysera mekanismen för justering av svårighetsgraden.
  - Känna till vad de tekniska termer som är förknippade med mining faktiskt betyder.
  - Beskriv de steg som ingår i byggandet av ett Bitcoin-block och dess komponenter.
  - Identifiera viktiga utvecklingar inom mining-industrin.


---

# Upptäck grunderna i Bitcoin mining



Att förstå proof of work är att förstå hur Bitcoin fungerar. Utan denna uppfinning och dess geniala användning hade Bitcoin helt enkelt inte kunnat existera. Den här kursen ger dig all den mining-teori du behöver för din bitcoinresa.



MIN 101 vänder sig i första hand till nybörjare, eftersom alla begrepp förklaras från grunden. Men om du redan har en viss kunskapsnivå kan du med hjälp av den här kursen befästa din förståelse, korrigera vissa ungefärliga intuitioner och utforska detaljer som ofta saknas i vanliga förklaringar.



I slutet av den här kursen kommer du att kunna förklara hur proof-of-work fungerar på ett enkelt och stringent sätt. MIN 101 är också en idealisk introduktion till alla andra mer avancerade kurser som ägnas åt Bitcoin mining på Plan ₿ Academy, oavsett om de är teoretiska eller praktiska.



+++


# Inledning


<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>



## Kursöversikt


<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>



Välkommen till MIN 101-kursen, där du kommer att upptäcka de grundläggande teoretiska begreppen mining och Proof-of-Work inom Bitcoin-systemet. Den här kursen är det första steget i din bitcoiner-resa för att förstå hur mining fungerar. När du har slutfört den kommer du att kunna gå vidare till mer avancerade teorikurser, eller gå in i praktiken och bli en bitcoinminer själv!



I denna MIN 101-kurs kommer vi inte att gå tillbaka till de grundläggande begreppen i Bitcoin, eftersom vi kommer att gå rakt in i sakens kärna: mining. Om du aldrig har hört talas om Bitcoin, eller om dess grunder fortfarande är lite oklara för dig, rekommenderar jag starkt att du börjar med vår introduktionskurs BTC 101. När du har förvärvat dessa grundläggande kunskaper kommer du att kunna ta itu med MIN 101 med tillförsikt:



https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Del 1 - Inledning



Vi kommer att börja den här kursen med ett valfritt första kapitel, där jag ger en mycket förenklad förklaring av mining för att ge dig en tydlig mental bild innan vi går in på de tekniska mekanismerna.



Syftet här är inte att ge dig alla tekniska detaljer (de kommer senare i kursen), utan att ge dig en röd tråd. När detta ramverk väl är på plats kommer varje mer avancerat koncept som introduceras efterhand att naturligt passa in i denna struktur.



### Del 2 - Hur proof of work fungerar



Efter introduktionen utgör del 2 den tekniska grunden för utbildningsprogrammet. Syftet är att steg för steg förklara hur Bitcoin producerar giltiga block. Vi börjar med att upptäcka strukturen i ett block innan vi går in på proof-of-work-mekanismen: målets roll, noncen och hashfunktionen. Slutligen ser vi hur Bitcoin lyckas upprätthålla en stabil blockproduktionstakt trots variationer i hashkraften, tack vare mekanismen för svårighetsjustering. I slutet av detta avsnitt kommer du att ha en fullständig förståelse för de grundläggande principerna för Bitcoin:s proof-of-work.



### Del 3 - Incitamentssystemet Bitcoin mining



I den tredje delen tittar vi på varför gruvarbetare uppmuntras att delta ärligt i mining. Vi kommer att beskriva principen om blockbelöning, dess sammansättning och beräkningsmetod, dess utveckling över tid genom halveringar och den specifika rollen för coinbase-transaktionen.



### Del 4 - Bitcoin mining-industrin



Den fjärde delen sätter mining tillbaka i sin operativa verklighet. Den spårar utvecklingen av mining-maskiner, från början av Bitcoin till den moderna ASIC, för att förstå nuvarande hårdvarubegränsningar. Vi tittar också på grunderna i mining-pooler för att förstå hur gruvarbetare lyckas minska variansen i sina inkomster.



### Del 5 - Sista avsnittet



I den avslutande delen av kursen kan du testa dina kunskaper i mining genom att ta ditt diplom.



Syftet med denna MIN 101-kurs är därför att du ska kunna lämna den med en tydlig, strukturerad och bestående förståelse för Bitcoin mining, både tekniskt och ekonomiskt.



Är du redo att upptäcka Bitcoin mining? Låt oss komma igång!




## Bitcoin mining enkelt gjort


<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>



Innan jag går vidare till en detaljerad och mer teknisk förklaring av Bitcoin [mining](https://planb.academy/resources/glossary/mining) vill jag ge dig en översikt över principen, som är avsiktligt enkel och schematisk. Om du redan har vissa grundläggande kunskaper kan du gå direkt till sakens kärna i nästa kapitel, efter att ha svarat på frågesportsfrågorna. Detta kapitel vänder sig i första hand till nybörjare, så att du får en mjukstart.



Föreställ dig Bitcoin som en stor offentlig anteckningsbok, delad av alla, där vi skriver ner vem som skickade bitcoins till vem. Denna anteckningsbok kallas [blockkedjan](https://planb.academy/resources/glossary/blockchain). Den kan inte innehas av bara en person, för då skulle den behöva vara pålitlig. Istället fungerar Bitcoin kollektivt: tusentals datorer verifierar och underhåller samma version av den här anteckningsboken.



![Image](assets/fr/049.webp)



I Bitcoin skapar du en [transaktion](https://planb.academy/resources/glossary/transaction-tx) när du gör en betalning. Den här transaktionen läggs inte omedelbart till i anteckningsboken. Den skickas först till nätverket och väntar sedan på att integreras i nästa transaktionspaket. Detta paket kallas för ett [block](https://planb.academy/resources/glossary/block).



![Image](assets/fr/050.webp)



Ett block är helt enkelt en uppsättning transaktioner som är grupperade tillsammans. När ett block är klart räcker det inte med att publicera det. Du måste bevisa för nätverket att blocket är värt att läggas till i poolen. Det är här mining kommer in i bilden.



Mining är arbetet med att validera ett block genom att förbruka energi. Aktörer som kallas [miners](https://planb.academy/resources/glossary/miner) använder specialiserade datorer. Dessa maskiner förbrukar elektricitet för att utföra ett mycket stort antal tester, i en loop, tills de hittar ett bevis som nätverket accepterar. När en miner hittar detta bevis anses hans block vara giltigt.



När blocket har validerats sänds det ut till nätverket. De andra [noderna](https://planb.academy/resources/glossary/node) kontrollerar snabbt att det överensstämmer med reglerna och lägger sedan till det i sekvensen av tidigare block. Det är därför det kallas en "blockkedja": varje nytt block kommer efter de andra, i sekventiell ordning, och denna kedja växer lite i taget.



![Image](assets/fr/051.webp)



Sammanfattningsvis skapas transaktioner först. Sedan grupperas de ihop i ett block. Sedan validerar en gruvarbetare detta block genom att förbruka elektricitet. Slutligen läggs blocket till i blockkedjan och de transaktioner det innehåller [bekräftas](https://planb.academy/resources/glossary/confirmation).



Om gruvarbetare förbrukar el är det inte för att de är frivilliga. De gör det för att det finns en belöning. När en gruvarbetare validerar ett block får han två typer av inkomster. Å ena sidan får han nyskapade bitcoins. Å andra sidan samlar han in de [avgifter](https://planb.academy/resources/glossary/transaction-fees) som användarna betalar för de transaktioner som ingår i blocket. Med andra ord kompenseras utvinnaren både genom programmerad monetär utgivning och genom transaktionsavgifter som bestäms av en marknad.



I det här skedet får du medvetet en mycket enkel bild av mining. Den förklarar ännu inte hur blocket är konstruerat i detalj, eller hur exakt beviset som miners letar efter fungerar, eller hur Bitcoin håller en stadig takt, eller hur belöningen beräknas exakt, eller hur den görs anspråk på. Det är okej, det är allt vi kommer att se i resten av denna MIN 101-kurs!



Syftet med det här kapitlet var helt enkelt att ge dig en tydlig mental struktur: transaktioner → block → mining → blockchain → belöning. Håll denna kedja av idéer i åtanke. I resten av kursen kommer varje kapitel att lägga till ett lager av tekniska detaljer om ett av dessa element, tills du inte bara förstår vad som händer, utan hur och varför det fungerar tillförlitligt, i stor skala, utan en chef och utan att behöva förtroende.



# Hur proof of work fungerar


<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>



## Bitcoin:s transaktionsväg


<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>



För att förstå vad Bitcoin mining handlar om måste vi först följa vägen för en typisk Bitcoin-transaktion. Detta kommer att visa dig exakt var blocket kommer in i bilden och varför det är hjärtat i systemet. Det är vad jag vill att du ska upptäcka i det här första kapitlet.



I Bitcoin är en transaktion en datastruktur som överför ägandet av bitcoins från en användare till en annan. I konkreta termer konsumerar den "[utdata](https://planb.academy/resources/glossary/output)" från tidigare transaktioner (så kallade [UTXO](https://planb.academy/resources/glossary/utxo)) och hänvisar till dem som "[inmatningar](https://planb.academy/resources/glossary/input)" och skapar sedan nya "utdata" som definierar vem dessa bitcoins nu tillhör och under vilka villkor de kan spenderas senare.



![Image](assets/fr/001.webp)



En viktig punkt när det gäller Bitcoin är bemyndigandet att spendera. Bitcoin finns inte på ett konto, som dina pengar på banken kan vara, utan är låsta av utgiftsvillkor. När en [wallet](https://planb.academy/resources/glossary/wallet) vill använda en UTXO som indata måste den tillhandahålla kryptografiskt bevis på att den har rätt att låsa upp den. Detta bevis tar ofta formen av en [digital signatur](https://planb.academy/resources/glossary/digital-signature) generated från en [privat nyckel](https://planb.academy/resources/glossary/private-key). Det är därför bitcoiners insisterar på att säkra dina privata nycklar: det är dessa som låser upp åtkomsten till dina bitcoins och följaktligen gör det möjligt för dig att spendera dem.



![Image](assets/fr/002.webp)



Den digitala signaturen i Bitcoin spelar två viktiga roller:




- Auktorisera utgifter: detta bevisar att användaren har den privata nyckel som förväntas av UTXO:s utgiftsvillkor;
- Integritetsskydd: kopplar auktorisationen till exakta detaljer i transaktionen (mottagare, belopp, avgifter etc.). Om någon ändrar transaktionen i efterhand är signaturen inte längre giltig.



När transaktionen har konstruerats korrekt och signerats av användarens Bitcoin wallet, måste den sändas ut i Bitcoin-nätverket.



### Bitcoin-nodens roll i distributionen



Bitcoin är ett [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p)-nätverk: det finns ingen central server som tar emot och behandlar alla transaktioner. Denna roll spelas kollektivt av noderna. En Bitcoin-nod är en mjukvara (t.ex. [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core)) som är ansluten till andra noder i Bitcoin-nätverket och vars huvuduppgift är att verifiera, lagra och vidarebefordra transaktioner och block.



När du skickar en transaktion från en wallet vidarebefordrar wallet den till en nod (din egen eller en tjänsts). Denna nod kommer först att kontrollera att transaktionen uppfyller olika regler, t.ex:




- signaturer är giltiga;
- ingångarna refererar till befintliga UTXO (dvs. bitcoins som existerar);
- dessa UTXO inte redan har spenderats på annat håll;
- mängden utgångar är mindre än eller lika med mängden ingångar (bitcoins skapas inte från ingenting);
- etc.



Om transaktionen klarar alla dessa kontroller vidarebefordrar noden den till de andra noderna i nätverket som den är ansluten till. De kontrollerar den i sin tur och vidarebefordrar den, och så vidare. Inom loppet av några sekunder sprids transaktionen och blir känd för hela, eller åtminstone en stor del av, Bitcoin-nätverket.



![Image](assets/fr/003.webp)



### Mempool: Transaktionernas väntrum



Mellan det ögonblick då en transaktion sänds och det ögonblick då den bekräftas i ett block måste den vänta. Detta vänteområde kallas **[mempool](https://planb.academy/resources/glossary/mempool)** (sammandragning av `memory` och `pool`). En mempool är därför ett tillfälligt lagringsutrymme för giltiga, men ännu inte bekräftade, transaktioner.



Viktig punkt: det finns inget sådant som en enda mempool, bara mempools. Varje nod upprätthåller sin egen mempool, med sina egna lokala begränsningar. Detta innebär att två noder vid varje givet tillfälle kan ha något olika innehåll i mempoolen (beroende på vad de har tagit emot, vad de har avvisat eller vad de har rensat).



![Image](assets/fr/004.webp)



I det här skedet känner nätverket till transaktionen, har verifierat den och håller den i minnet tills den bekräftas. Men bekräftelsen av transaktionen kommer först när en miner lägger in den i ett block och detta block accepteras av nätverket.



### Blockchain: ett offentligt register för tidsstämpling



Eftersom bitcoin är en immateriell valuta måste den ta itu med ett problem: att förhindra [dubbelutgifter](https://planb.academy/resources/glossary/double-spending-attack) utan en central myndighet. Om två transaktioner försöker spendera samma UTXO måste alla kunna konvergera till ett enda, sammanhängande tillstånd. Satoshi Nakamoto sammanfattar denna fråga med denna berömda mening:



> Det enda sättet att bekräfta att en transaktion inte har ägt rum är att vara medveten om alla transaktioner.

Med andra ord, för att veta att en bitcoin inte redan har spenderats behöver du ett gemensamt register över tidigare utgifter.



Detta är blockkedjans roll: ett offentligt register som innehåller transaktionshistoriken. Men i stället för att skriva ner varje transaktion när den sker grupperar Bitcoin dem i block. Varje block fungerar som en historiksida, och systemet fungerar därmed som en tidsstämpelserver: det beställer transaktioner över tid på ett verifierbart sätt.



Detta register kan inte skrivas om, tack vare en enkel princip: varje block innehåller det kryptografiska fingeravtrycket ([hash](https://planb.academy/resources/glossary/hash-function)) för det föregående blocket. Blocken är alltså länkade: om du ändrar ett block från det förflutna ändras dess hash, vilket bryter länken till nästa block, som bryter länken till blocket efter det, och så vidare. Det är denna kedja av beroenden som ger "*blockchain*" dess namn.



![Image](assets/fr/005.webp)



När vi har förstått dessa grundläggande principer för Bitcoin kan vi beskriva en miners mål i mer konkreta termer: att bygga ett nytt block som förlänger den befintliga kedjan genom att skriva in väntande transaktioner och sedan försöka göra det giltigt (detta är den berömda "[proof of work](https://planb.academy/resources/glossary/proof-of-work)" som vi kommer att studera i ett senare kapitel). Men låt oss först tillsammans i nästa kapitel upptäcka hur ett kandidatblock konstrueras.



## Bygga ett Bitcoin-block


<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>



Du har nu förstått hur en Bitcoin-transaktion fungerar och vilken roll blockkedjan har. Men innan vi tittar mer i detalj på hur proof-of-work fungerar finns det fortfarande ett viktigt steg som gruvarbetaren måste utföra: konstruktionen av ett [kandidatblock](https://planb.academy/resources/glossary/candidate-block). Låt oss tillsammans ta reda på vad ett kandidatblock är och hur mineraren konstruerar det, innan vi börjar leta efter ett giltigt bevis.



### Kandidatblocket



Miner:or måste själva bygga sina block innan de försöker bryta dem. Varje gruvarbetare konstruerar i sin tur ett så kallat kandidatblock från de transaktioner som väntar i hans mempool. Att bygga ett kandidatblock består därför av:




- välja vilka transaktioner som ska ingå;
- organisera dessa transaktioner på ett sätt som är förenligt med Bitcoin:s regler;
- producerar blockets metadata, som lagras i dess [rubrik](https://planb.academy/resources/glossary/block-header).



Valet av transaktioner följer en enkel ekonomisk logik: ett block har en kapacitet som begränsas av Bitcoin-protokollet, så utvinnaren försöker maximera vad han tjänar för detta utrymme. Han väljer i första hand de transaktioner som ger de högsta avgifterna i förhållande till det utrymme de upptar i blocket (detta kallas "fee rate" och uttrycks i sats/vB). Detaljerna kring avgifter kommer att behandlas senare; kom bara ihåg idén om att sortera efter utrymmeseffektivitet.



Ett Bitcoin-block består därför av två huvuddelar:




- en lista över transaktioner;
- ett blockhuvud, som på sätt och vis fungerar som blockets identitetskort.



![Image](assets/fr/006.webp)



Rubriken är viktig eftersom den används som grund för proof-of-work: i Bitcoin bryter man inte ett helt block direkt utan endast rubriken för ett block, som sammanfattar den information som behövs för att länka blocket till kedjan och överföra dess innehåll. För att göra det möjligt för rubriken att representera alla transaktioner använder Bitcoin ett kryptografiskt verktyg: [Merkle-trädet](https://planb.academy/resources/glossary/merkle-tree).



### Merkle-trädet: sammanfattning av en stor uppsättning transaktioner



Att lista alla transaktioner i rubriken skulle vara omöjligt: ett block kan innehålla tusentals transaktioner, medan rubriken har en fast storlek (80 byte). Lösningen är därför att beräkna en unik hash som beror på alla transaktioner i blocket: detta är [Merkle-roten](https://planb.academy/resources/glossary/merkle-root).



Principen är följande:




- det kryptografiska fingeravtrycket (hash) för varje transaktion beräknas;
- dessa hashvärden paras ihop, sammankopplas och hashas sedan igen för att bilda ett nytt lager av hashvärden;
- denna process upprepas tills en enda slutlig hash erhålls: Merkle-roten.



![Image](assets/fr/007.webp)



Så om en enskild transaktion ändras, om så bara med en enda bit, blir resultatet en ändring av dess fingeravtryck, som sprids till Merkle-roten. Denna rot ingår i blockhuvudet. Så att ändra en tidigare transaktion innebär att ändra blockhuvudet där den ingår, och därmed blockets fotavtryck och sedan länken till efterföljande block.



Sedan [SegWit](https://planb.academy/resources/glossary/segwit) har vi separerat signaturerna från resten. Så i verkligheten finns det två Merkle-träd i varje block. Den här separationen har konsekvenser för hur vi räknar storleken på ett block och för vissa kryptografiska åtaganden, men grundidén är densamma: huvudet måste på ett kompakt sätt bekräfta allt innehåll i blocket.



### Blockets rubrik



Blockhuvudet är 80 byte långt och innehåller exakt 6 fält. Det är dessa sex element som kommer att hashas vid sökning efter en proof of work (se nästa kapitel):





- Versionen (`version`): Detta anger vilka regler eller uppdateringssignaler som blocket följer. Det fungerar som en mekanism för att upprätthålla protokollkompatibilitet och utveckling.




- Hash för föregående block (`previousblockhash`): Detta är hashen i det föregående blockets header. Det är detta som länkar samman blocken. Utan det här fältet skulle vi ha oberoende block. Genom att inkludera hashen i det föregående blockets header får vi en kedja, där varje nytt block bygger på det föregående.





- Merkle-rot (`merkleroot`): Detta är fingeravtrycket av alla transaktioner i blocket (via Merkle-trädet). Den länkar rubriken till innehållet: om utvinnaren ändrar urvalet eller ordningen på transaktionerna ändras roten.





- [Tidsstämpel](https://planb.academy/resources/glossary/timestamp): Detta är en tidsstämpel (Unix-tid) som väljs av utvinnaren (med giltighetsbegränsningar) och som måste ange när blocket utvanns. Den behöver inte vara helt exakt på sekunden, men den måste uppfylla vissa villkor för att vara godtagbar för nätverket.





- Kodat [svårighetsmål](https://planb.academy/resources/glossary/difficulty-target) (`nbits`): Detta fält kodar det aktuella svårighetsmålet. Vi kommer att gå in mer i detalj i kapitlet om svårighet, men kom ihåg att denna parameter är en del av rubriken.





- [Nonce](https://planb.academy/resources/glossary/nonce) (`nonce`): Detta är ett värde som gruvarbetaren fritt kan ändra. Det fungerar som en justerbar variabel under proof-of-work. Jag kommer att förklara dess roll mer i detalj i nästa kapitel, men det är viktigt att förstå att nonce är en del av blockhuvudet och är utformat för att tillåta successiva försök.



För att göra det lättare att visualisera detta följer här ett exempel på en blockrubrik i hexadecimalt format (80 byte):



```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```



Här är en uppdelning fält-för-fält:



```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```



Detta kandidatblockhuvud, som konstruerats av gruvarbetaren, utgör grunden för deras arbete. När man söker efter en giltig proof-of-work är det inte hela listan med transaktioner som hashas direkt i en loop, utan snarare detta 80-byte-block, som innehåller allt som behövs för att länka blocket till det förflutna och binda dess innehåll, samtidigt som det också innehåller de parametrar som krävs för mining-mekanismen, som vi kommer att utforska i nästa kapitel.



## Hashen, målet och noncen


<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>



I de tidigare kapitlen följde du vägen för en Bitcoin-transaktion: skapad och signerad av en wallet, vidarebefordrad av noder, lagrad i mempools och sedan bekräftad när en miner inkluderar den i ett block som accepteras av nätverket. Men vi har ännu inte sett hur en gruvarbetare kan lägga till sitt block i blockkedjan. Vad är processen bakom mining?



Att förstå mining-processen är ganska okomplicerat. Det handlar om 3 koncept som går hand i hand: en hashfunktion, ett målvärde och en variabel som gruvarbetaren kan modifiera. Låt oss ta en titt på hur det hela fungerar.



### Hash-funktionen



En hashfunktion är ett verktyg som tar ett meddelande som indata och producerar en utdata av fast storlek, kallad "*fingeravtryck*" eller "*hash*".



![Image](assets/fr/010.webp)



Hashfunktionen är intressant i datorsystem eftersom den har vissa egenskaper:





- Om du ändrar en enda bit i inmatningen ändras den resulterande utmatningshashen helt och hållet och oförutsägbart;



![Image](assets/fr/011.webp)





- Det är omöjligt att gå från utmatningen till inmatningen: funktionen är irreversibel;



![Image](assets/fr/012.webp)





- Det är omöjligt att hitta två olika meddelanden som ger exakt samma hash.



![Image](assets/fr/013.webp)



Den hashfunktion som används i Bitcoin för mining är `SHA256`, som tillämpas två gånger i följd. Detta kallas dubbel [SHA256](https://planb.academy/resources/glossary/sha256), eller `SHA256d`. Det är denna dubbla hashing som ger blockets fingeravtryck.



```text
hash = SHA256(SHA256(message))
```



I vårt fall motsvarar `message` i själva verket blockets header, som du såg i föregående kapitel. Som en påminnelse är rubriken en liten struktur som sammanfattar allt i blocket.



![Image](assets/fr/014.webp)



### Bevis på arbete: hitta en hash som är mindre än målet



Proof-of-Work beskrivs ofta som lösningen på ett komplext problem. I själva verket är det inte så mycket ett problem som en trial-and-error-sökning: utvinnaren måste hitta en version av rubriken vars hash (efter att ha passerat genom hashfunktionen `SHA256d`) respekterar ett enkelt villkor: den måste vara mindre än ett visst mål.



Detta villkor formuleras på följande sätt:




- blockhuvudets hash beräknas med hjälp av en hashfunktion;
- tolkar vi denna hash som ett nummer;
- för att blocket ska vara giltigt måste detta tal vara mindre än eller lika med ett värde som kallas "*svårighetsmål*".



Med andra ord är ett block giltigt om:



```text
SHA256d(block_header) <= target
```



![Image](assets/fr/015.webp)



Målet är ett 256-bitars tal. Eftersom hashen som produceras av `SHA256d` också är 256 bitar kan de jämföras som två tal. Ju lägre målet är, desto svårare är villkoret, eftersom det finns färre möjliga resultat under detta tröskelvärde. Omvänt gäller att ju högre målet är, desto lättare är villkoret att uppfylla och desto lättare blir det att bryta ett block. Vi kommer att titta närmare på hur detta mål bestäms i senare kapitel.



I det här systemet är hashfunktionen intressant. Kom ihåg att det är lätt att beräkna utdata från indata, men omöjligt att hitta en indata genom att bara känna till funktionens utdata. I mining ombeds miners inte att hitta en exakt hash, utan snarare att hitta en hash under ett målvärde. Det enda sättet att uppnå detta är att göra ett mycket stort antal försök, tills en viss header i deras kandidatblock, när den hashas, ger en hash som är mindre än detta mål.



När målet är tillräckligt lågt blir denna process kostsam. Mineraren beräknar hashvärdet för sitt kandidatblocks header, kontrollerar resultatet och, om villkoret inte är uppfyllt, ändrar headern och upprepar beräkningen. Denna loop upprepas tills en giltig header hittas. När rubrikens hash slutligen uppfyller villkoret etableras proof of work, blocket anses giltigt och kan sändas i Bitcoin-nätverket så att noderna kan lägga till det i sin blockkedja. Den vinnande gruvarbetaren får sedan den tillhörande belöningen (vi kommer att beskriva dess sammansättning senare), medan alla gruvarbetare omedelbart ger sig ut på jakt efter en ny, giltig header för nästa block.



Den grundläggande fördelen med denna mekanism ligger i dess asymmetri. Att producera en proof of work är kostsamt för miners, eftersom det kräver ett stort antal hashberäkningar. För verifierare, dvs. nätverksnoder, är verifieringen å andra sidan extremt enkel: allt de behöver göra är att hasha blockhuvudet som tillhandahålls av utvinnaren och kontrollera att den resulterande hashen verkligen är lägre än målet. Att hitta ett bevis kräver därför mycket arbete och resurser, medan det går snabbt och är billigt att verifiera dess giltighet. Det är just den här egenskapen som definierar ett effektivt proof-of-work-system.



### Nonce



En praktisk fråga kvarstår: om kandidatblockets header, som konstruerats av utvinnaren, inte ger en giltig hash, hur kan utvinnaren då försöka igen? Han måste modifiera något i huvudet för att få en annan hash. Det är just detta som är noncens roll.



Kom ihåg den första egenskapen hos en hashfunktion: det räcker att ändra en enda bit av indata för att producera en helt annan och oförutsägbar utgångshash. Varje hashberäkning är därför som en slumpmässig dragning.



![Image](assets/fr/016.webp)



För att pröva lyckan igen behöver gruvarbetaren inte ändra hela huvudet på sitt kandidatblock: han behöver bara ändra en liten del av det, eftersom även en enda annorlunda bit kommer att resultera i en helt ny hash, potentiellt giltig om den är mindre än målet.



Det är just därför som blockhuvudet innehåller en nonce. Noncen är ett 32-bitars värde som används en gång och sedan ersätts. I praktiken kan en gruvarbetare för samma kandidatblock testa cirka 4,29 miljarder möjliga värden (från "0" till "2^32 - 1"). Varje variation av nonce ändrar blockhuvudet och ändrar följaktligen helt den hash som produceras efter tillämpning av hashfunktionen `SHA256d`.



mining-processen är mycket enkel:




- gruvarbetaren bygger ett kandidatblock (transaktioner + rubrik);
- beräknar sedan hashvärdet för `SHA256d(header)`;
- om resultatet är större än målet ändras noncen;
- börjar om;
- etc.



![Image](assets/fr/017.webp)



Faktum är att nonce inte är det enda fält som kan modifieras. Varje ändring inom transaktionerna i ett block resulterar i en ändring av roten i Merkle-trädet och därmed en ändring av blockets rubrik. Med modern datorkraft kan det gå relativt snabbt att gå igenom de 4,29 miljarder möjliga värdena för noncen. Det är därför det finns ett annat fält, allmänt kallat "*[extra-nonce](https://planb.academy/resources/glossary/extra-nonce)*", som ytterligare multiplicerar möjligheterna till rubrikvariation. Vi återkommer till denna mekanism mer i detalj i ett senare kapitel.



### Vad är poängen med proof of work?



Vi kallar det "bevis" eftersom resultatet är omedelbart verifierbart: när ett block har producerats kan vilken nod som helst på en bråkdel av en sekund kontrollera att den kryptografiska hashen av dess header verkligen ligger under det mål som krävs. Vi kallar det "arbete" eftersom det krävs en mängd försök för att uppnå denna hash, och därmed en verklig kostnad i form av beräkning och energi.



I Bitcoin [White Paper](https://planb.academy/resources/glossary/white-paper) lyfter Satoshi Nakamoto fram två fördelar med att använda ett proof-of-work-system i Bitcoin:





- Sealing den ekonomiska historien:**



När beräkningsbelastningen har använts är blocket låst: om det ska ändras måste blockets proof of work göras om. Och eftersom blocken är sammanlänkade skulle en ändring av ett gammalt block också innebära att alla efterföljande block måste räknas om, för att sedan komma ikapp och överträffa det pågående arbetet i den ärliga kedjan.



proof-of-work fungerar med andra ord som ryggraden i tidsstämplingssystemet, vilket gör det allt dyrare att förfalska det förflutna i takt med att blocken ackumuleras. När ett nytt block bryts tillämpas säkerheten som tillhandahålls av proof of work samtidigt och enhetligt på alla befintliga UTXO. För varje block som läggs till ackumulerar således varje UTXO ytterligare en säkerhet från Proof-of-Work.





- Definiera majoritetsregeln ([konsensus](https://planb.academy/resources/glossary/consensus)) och neutralisera Sybil:**



Proof-of-Work gör det också möjligt för Bitcoin att nå konsensus utan att förlita sig på röstningsregeln "ett ID = en röst", som lätt skulle kunna förfalskas genom det massiva skapandet av identiteter (IP, noder, nycklar...).



I Bitcoin är "*majoriteten*" inte det största antalet deltagare, utan den **kedja som ackumulerar mest arbete**. Som Satoshi uttrycker det är detta en "en CPU = en röst"-princip, dvs. en röst som viktas av den faktiska datorkraft som används för att producera giltiga block. Så att distribuera tusentals noder ger ingen fördel i sig jämfört med Bitcoin. Utan ytterligare datorkraft ackumuleras inga fler arbetsbevis och [Sybil-attacken](https://planb.academy/resources/glossary/sybil-attack) blir värdelös, medan beslutsregeln förblir objektiv och inte kräver någon identifiering av deltagarna.



![Image](assets/fr/018.webp)



[Nakamoto, S. (2008) *Bitcoin: A Peer-to-Peer Electronic Cash System.*](https://bitcoin.org/bitcoin.pdf)



Principerna om minderårigas användbarhet och befogenheter är ett mycket komplext ämne, som jag inte kommer att gå in närmare på i den här kursen. Vi kommer dock att återkomma till detta ämne på djupet i framtida MIN 201-kurser.



För tillfället kan du sammanfatta hur mining fungerar så här: gruvarbetare bygger ett kandidatblock med de transaktioner som väntar i mempoolerna och letar sedan efter en hash av dess rubrik (via `SHA256d`) som är mindre än eller lika med ett mål. De uppnår detta genom att testa nonces genom försök och misstag.



I nästa kapitel gör vi en kort historisk avstickare till proof-of-work-principen för att förstå dess bakgrund, och sedan tittar vi på hur svårighetsmålet bestäms av systemet.



## Historien om proof of work


<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>



Proof-of-work uppfanns inte för Bitcoin. [Satoshi Nakamoto](https://planb.academy/resources/glossary/nakamoto-satoshi) tog upp och sammanställde flera äldre idéer, som redan utforskats i olika sammanhang.



### Hashcash



I slutet av 1990-talet blev problemet med e-postspam alltmer påtagligt. Om det kostar nästan ingenting att skicka ett e-postmeddelande kan en spammare skicka miljontals. Men om varje meddelande kräver en liten beräkningsinsats är det fortfarande enkelt för en normal användare att skicka ett enda legitimt meddelande, medan det blir mycket dyrt att skicka miljontals meddelanden.



Detta är syftet med [Hashcash](https://planb.academy/resources/glossary/hashcash), som föreslogs av Adam Back 1997 och som anses vara uppfinningen av proof-of-work-principen. Hashcash-principen är mycket lik mining: producera en hash som uppfyller ett villkor (att ha ett visst antal nollor i början av hashen). Beviset följer sedan med meddelandet och kan verifieras mycket snabbt av mottagaren. Om det kommer ett e-postmeddelande som inte innehåller detta bevis kan det omedelbart betraktas som skräppost och därför filtreras bort. Spammare tvingas då lägga ner en avsevärd mängd energi på att skicka miljontals meddelanden, vilket drastiskt minskar (eller till och med helt omintetgör) lönsamheten för denna typ av verksamhet, oavsett om det handlar om marknadsföring eller bedrägeri.



Numera används inte Hashcash för e-post. Spamfiltrering är nu till stor del baserad på centraliserade system. Hashcashs fördel jämfört med nuvarande lösningar ligger i att det inte kräver någon centraliserad filtrering: vem som helst kan justera parametrarna enligt sina egna kriterier. Det kräver inte heller identifiering, eftersom en hashsökning kan utföras anonymt. Framför allt förlitar den sig inte på ett ryktessystem, som tenderar att införa subjektiva former av filtrering.



Hashcash handlade inte om att skapa pengar. Den försökte införa en marginalkostnad för en lätt automatiserbar digital åtgärd.



![Image](assets/fr/008.webp)



### Bit guld



I slutet av 1990-talet och början av 2000-talet utforskade Nick Szabo idén om digital knapphet baserad på proof of work. Hans konceptuella projekt, kallat Bit Gold, går ut på att skapa värdeenheter genom att lösa en kostsam proof of work och sedan registrera dessa bevis i ett register för att etablera en form av ägande.



Bit Gold resulterade inte i ett distribuerat system som Bitcoin, men det innehåller flera viktiga insikter: idén om att beräkningar kan skapa knapphet och idén om att tidsstämpla element över tid för att skapa en historia som är svår att skriva om.



### RPOW



År 2004 föreslog Hal Finney RPOW (*Reusable Proofs of Work*). Tanken var att ta fram arbetsbevis som sedan kunde utbytas, snarare än att bara förbrukas. RPOW syftade till att skapa digitala token baserat på proof of work, med ett system för att verifiera och överföra dessa token utan att duplicera dem. RPOW löste inte heller problemet med ett helt decentraliserat register på ett tillfredsställande sätt, vilket Bitcoin senare skulle göra, men det är fortfarande en av de stora föregångarna till Bitcoin.



![Image](assets/fr/009.webp)



Hashcash, Bit Gold och RPOW använder proof-of-work för att införa en kostnad och skapa en form av knapphet. Bitcoin tar upp denna mekanism, men ger den en central och kollektiv roll: proof-of-work används inte bara för att skapa något, det används också för att bestämma vem som har rätt att skriva nästa sida i registret (nästa block), och för att göra detta register kostsamt att förfalska.



## Justering av svårighetsmålet


<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>



I tidigare kapitel såg du kärnan i proof-of-work: gruvarbetare hashar rubriken på sitt kandidatblock med `SHA256d`, och blocket anses endast giltigt om den resulterande hashen är numeriskt mindre än eller lika med ett referensvärde som kallas målet. Frågan kvarstår då: var kommer detta mål ifrån och hur säkerställer systemet att det förblir konsekvent över tiden?



Bitcoin siktar på en genomsnittlig takt på ett block som hittas var 10:e minut. Självklart är denna takt inte garanterad till sekunden. I praktiken hittas vissa block några sekunder efter det föregående, medan andra hittas efter mer än en timme. Det som är viktigt här är genomsnittet under en tillräckligt lång period.



![Image](assets/fr/019.webp)



Denna variation beror på mining:s probabilistiska natur: varje hash är ett oberoende försök, med en konstant sannolikhet (förutsatt att målet förblir oförändrat) att ge ett resultat som är lägre än målet. Det kan därför jämföras med ett lotteri med en kontinuerlig dragning: ju fler hashningar miners gör per sekund, desto kortare blir den förväntade fördröjningen innan ett giltigt block visas, men utan att någonsin eliminera slumpmässigheten från en dragning till nästa.



### Varför ska man sikta på 10 minuter mellan blocken?



Även om det inte finns några bevis för detta valde Satoshi Nakamoto säkert 10 minuter som en praktisk kompromiss mellan effektivitet och säkerhet. Ett kortare intervall skulle ge mer frekventa bekräftelser, men skulle orsaka fler tillfälliga nätverkssplittringar. För att förstå detta måste vi gå tillbaka till hur ett block sprids.



När en miner hittar ett giltigt block distribuerar han det omedelbart till sina kollegor. De noder som tar emot det kontrollerar dess giltighet (transaktioner, proof of work, konsensusregler etc.) och vidarebefordrar det sedan i sin tur. Denna spridning tar en viss tid, som begränsas av internetlatens, bandbredd och varje nods förmåga att verifiera blocket.



![Image](assets/fr/020.webp)



Om en annan gruvarbetare under denna diffusionsfördröjning också upptäcker ett giltigt block på samma höjd kan nätverket tillfälligt delas upp: en del av noderna och gruvarbetarna förlitar sig på block A, medan den andra delen förlitar sig på block B. Detta är en tillfällig uppdelning av nätverket.



![Image](assets/fr/021.webp)



Dessa uppdelningar är inte katastrofala. Nakamotos konsensus förutspår att på lång sikt kommer endast en gren att råda: den som ackumulerar mest arbete. Så snart ett nytt block utvinns ovanpå block A, till exempel, resynkroniseras hela nätverket på den här grenen och överger block B, som då blir ett "*[stale block](https://planb.academy/resources/glossary/stale-block)*", ibland felaktigt kallat ett "*orphan block*" i vardagsspråket.



![Image](assets/fr/022.webp)



Å andra sidan har de en kostnad: under några minuter arbetar en bråkdel av gruvarbetarna på en gren som kommer att överges. Detta arbete är sedan bortkastat ur den övergripande säkerhetssynvinkeln, eftersom det inte har bidragit till den slutliga kedjan. Ju snabbare intervallet mellan varje block är, desto större är sannolikheten för sådana splitsar, eftersom spridningstiden utgör en större andel av tiden mellan varje block.



Intervallet på 10 minuter ger i allmänhet tillräckligt med tid för att det vinnande blocket ska kunna spridas brett innan ett konkurrerande block på samma höjd hittas. Det är en kompromiss som begränsar antalet splits, minskar slöseriet med datorkraft och hjälper nätverket att hålla sig synkroniserat på global nivå.



### Förståelse av hashrate



*"[Hashrate](https://planb.academy/resources/glossary/hashrate)*" avser den mängd hashberäkningar som produceras per sekund, oavsett om det är av en enskild minare, en grupp minare eller alla minare i Bitcoin. Det uttrycks i "H/s" (hashes per sekund), med multiplar som "TH/s" (terahashes per sekund) eller "EH/s" (exahashes per sekund). Detta representerar antalet försök som miners kan göra varje sekund för att försöka få en hash som är lägre än målet.



Om målet förblir oförändrat, då:




- varje försök har en fast sannolikhet att lyckas;
- om man gör fler försök per sekund ökar sannolikheten för att ett vinnande försök kommer att dyka upp snabbt


Med andra ord, om morgondagens Bitcoin-nätverk fördubblar sin datorkraft genom att ansluta dubbelt så många mining-maskiner, utan en korrigerande mekanism, skulle block hittas i genomsnitt dubbelt så snabbt. Målet måste därför justeras för att kompensera för hashrate-variationer.



### Justering av svårighetsmålet



Bitcoin löser detta problem med en periodisk måljusteringsmekanism, som justerar svårighetsgraden för mining. Principen är följande: varje 2016-block (ungefär varannan vecka) räknar varje nod om svårighetsmålet genom att observera hur mycket tid som faktiskt behövdes för att producera dessa 2016-block.



Syftet med denna mekanism är att minska den genomsnittliga produktionstiden för ett block till cirka 10 minuter, samtidigt som nätverkets totala hashrate ständigt förändras på grund av att maskiner kopplas bort eller tvärtom nya maskiner läggs till.



![Image](assets/fr/023.webp)



Beräkningen baseras på den observerade tiden för den period som har förflutit:




- om de sista blocken 2016 hittades för snabbt innebär det att hashrate ökade under denna period; Bitcoin försvårar då tillståndet genom att sänka målet för nästa period;
- om 2016 års block hittades för långsamt innebär detta att hashrate har minskat; Bitcoin lindrar tillståndet genom att öka målet.



Formeln är som följer:



```txt
Tn = To * (Ta / Tt)
```



Med:




- `tn`: nytt mål
- `to`: gammalt mål
- `Ta`: förfluten realtid för de senaste 2016 blocken
- `Tt`: måltid (i sekunder)



Med en måltid på två veckor, d.v.s. `Tt = 1.209.600` sekunder:



```txt
Tn = To * (Ta / 1 209 600)
```



För att förstå hur man justerar svårighetsgraden för Bitcoin mining, här är ett exempel med fiktiva värden:



```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```


Med:



- `**To = 18.045.755.102**`: Gammalt mål, d.v.s. referensvärdet före justering.
- `**ta = 1.000.000 sekunder**`: Tid som faktiskt använts för att producera de senaste 2016 blocken. Eftersom den här tiden är kortare än måltiden har nätverket utvunnit för snabbt.
- `**1 209 600 sekunder**`: Måltid motsvarande 10 minuter per block för 2016 års block, används som referens för justering.
- `**tn = 14 918 779 020**`: Nytt mål beräknat efter [svårighetsjustering](https://planb.academy/resources/glossary/difficulty-adjustment).



Här är det nya målet lägre än det gamla, vilket innebär att mining blir hårdare för att bromsa blockproduktionen under nästa period.


*Målvärdena i detta exempel är förenklade och skalade i undervisningssyfte; det faktiska målet som används i Bitcoin är ett 256-bitars heltal av en helt annan storleksordning.*



Denna beräkning utförs lokalt av varje nod, baserat på de tidsstämplar som anges i blocken. Eftersom alla noder tillämpar samma regler kommer de fram till samma resultat, och det nya målet blir den gemensamma referensen för de kommande 2016-blocken.



Det finns en viktig detalj att notera om denna justering: **den är begränsad**. Bitcoin begränsar variationen i svårighetsgrad per period för att undvika alltför abrupta förändringar som kan blockera den. Faktum är att den faktiska tid som tas med i beräkningen begränsas till att ligga inom ett intervall som motsvarar en faktor 4 (minst en fjärdedel av det gamla målet, högst fyra gånger det gamla målet). Detta förhindrar extrema ominriktningar om tidsstämplarna är mycket atypiska eller manipulerade.



### Målrepresentation



I blockhuvudet visas inte målet i sin fullständiga 256-bitarsform, eftersom detta skulle ta upp för mycket utrymme. Istället kodar 32-bitarsfältet `nBits` målet i ett kompakt format som kan jämföras med vetenskaplig notation i bas 256: en exponent (1 byte) och en koefficient (3 byte). Det kompletta målet rekonstrueras sedan från dessa två värden. Vi kommer inte att gå in på detaljer här, eftersom ämnet är relativt komplext och inte tillför något till förståelsen av mining. Kom bara ihåg att målet inte lagras i rå form i blockhuvudet, utan i kompakt form.



Med detta sista kapitel i del I har vi tagit en rundtur i hur proof-of-work fungerar i Bitcoin: gruvarbetaren bygger ett kandidatblock genom att välja transaktioner från sin mempool, beräknar kandidatblockets rubrik, hashar den, jämför den resulterande hashen med periodmålet och börjar sedan om genom att modifiera noncen tills en giltig hash erhålls. Slutligen, vart 2016:e block, räknar nätverket om ett nytt mål för att bibehålla en genomsnittlig tid på cirka 10 minuter per block, trots de ständiga variationerna i hashrate.




# Incitamentssystemet Bitcoin mining


<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>



## Block reward


<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>



Som du kan föreställa dig är Bitcoin mining inte en altruistisk verksamhet. Miner:or har verkliga kostnader: el för att driva sina mining-datorer, inköp av specialutrustning, löner för underhåll, ibland lokaler och kylsystem. För att Bitcoin-systemet ska fungera måste gruvarbetarnas privata intressen vara i linje med nätverkets kollektiva intressen. Detta är exakt den roll som mining-belöningen har. Den uppmuntrar miners att investera i proof of work, att inkludera giltiga transaktioner och att respektera protokollets regler snarare än att försöka korrumpera det.



Den här logiken bygger på spelteori: protokollet gör ärlighet rationellt. En gruvarbetare tjänar pengar när han producerar ett giltigt block som accepteras av noderna. Om han däremot försöker fuska kommer hans block att avvisas av noderna och han får ingenting. Eftersom det är en kostnad att producera ett block innebär ett avvisat block en direkt förlust. I en konkurrensutsatt miljö där tusentals spelare samtidigt söker efter ett giltigt block är därför den mest lönsamma strategin för det mesta att följa reglerna strikt och maximera sin inkomst på ett ärligt sätt.



För att uppnå detta föreskriver Bitcoin-protokollet att den utvinnare som hittar ett giltigt block vinner rätten att inkludera en viss transaktion i det, vilket ger utvinnaren en viss summa BTC. Detta kallas **[blockbelöning](https://planb.academy/resources/glossary/block-reward)**. I det här första kapitlet i det här avsnittet är syftet att förstå vad den består av och hur den bestäms. Senare kommer vi att se hur den penningskapande delen utvecklas över tid (med halvings) och hur den faktiskt samlas in tekniskt (via coinbase-transaktionen).



### Vad består blockbelöningen av?



I tidigare kapitel har vi sett hur miners lyckas hitta ett giltigt block. När en utvinnare har hittat en header vars hash är mindre än målet anses hans kandidatblock vara giltigt. Han kan då distribuera det till hela Bitcoin-nätverket. Blocket läggs till i resten av blockkedjan och bekräftar de transaktioner som det innehåller.



Det är just denna händelse (det faktiska tillägget av blocket till blockkedjan) som utlöser en belöning till den vinnande gruvarbetaren. Denna belöning består av två olika element som läggs ihop:




- [blocktillskott](https://planb.academy/resources/glossary/block-subsidy)**;
- transaktionsavgifter**.



![Image](assets/fr/024.webp)



Låt oss ta en titt på vad dessa två delar av belöningen motsvarar.



### Blocksubvention



Blocksubventionen motsvarar den monetära skapande delen av belöningen. När en miner producerar ett giltigt block ger protokollet honom rätt att skapa ett visst antal nya bitcoins och tilldela dem till sig själv som en belöning. Dessa bitcoins skapas ex nihilo. De existerade inte tidigare.



Mängden nyskapade bitcoins är dock inte på något sätt godtycklig. Den definieras strikt av Bitcoin-protokollets regler och är identisk för alla gruvarbetare. Vi kommer att titta närmare på denna mekanism i nästa kapitel, eftersom subventionen inte är ett fast värde på obestämd tid: den delas upp regelbundet enligt ett exakt schema. För tillfället är det bara att komma ihåg det:




- blocksubventionen är en av de två komponenterna i blockbelöningen;
- det är begränsat och bestäms av protokollet, inte av utvinnaren (även om utvinnaren tekniskt sett kan begära mindre än det maximala beloppet);
- den skapar bitcoins ur tomma intet.



Denna subvention spelar två huvudroller inom Bitcoin-protokollet. Den första är att uppmuntra spelare att delta i mining. Under de första åren med Bitcoin (och ibland fortfarande idag) var transaktionsavgifterna mycket låga. Subventionen har därför garanterat tillräcklig kompensation för att locka till sig miners och upprätthålla en säkerhetsnivå för systemet.



Den andra rollen handlar om valutadistribution. Alla nya valutor ställs inför frågan om hur de monetära enheterna ska fördelas rättvist till befolkningen. Blocksubventionen ger ett svar på detta problem. Genom att skapa bitcoins via mining möjliggörs deras initiala distribution på ett öppet och neutralt sätt: vem som helst kan få tag på dem, förutsatt att de deltar i mining, utan krav på förhandsgodkännande eller identifiering.



Å andra sidan, eftersom dessa bitcoins skapas ur tomma intet, är deras värde inte utan grund. Genom att öka mängden pengar i omlopp späder subventionen mekaniskt ut värdet på befintliga bitcoins. Det introducerar därför en form av monetär inflation. Vi kommer dock att se i nästa kapitel att denna subvention är avsedd att försvinna gradvis och att inflationen så småningom kommer att upphöra.



![Image](assets/fr/025.webp)



### Transaktionsavgifter



Den andra komponenten i blockbelöningen är kopplad till systemanvändningen: när en användare lägger upp en transaktion vill han att den ska bekräftas. Blockutrymmet är dock begränsat och blocken visas i genomsnitt bara var 10:e minut eller så. Blockutrymme är därför en knapp resurs. När efterfrågan överstiger utbudet stiger priset: detta är marknaden för transaktionsavgifter. Varje miner som lyckas producera ett giltigt block får rätt att för egen räkning ta ut hela transaktionsavgiften för alla de transaktioner som han har inkluderat i sitt block.



Du kan tänka på det som ett auktionssystem: varje transaktion föreslår ett avgiftsbelopp och miners prioriterar de transaktioner som maximerar deras intäkter, under utrymmesbegränsningar. Denna mekanism anpassar naturligt intressen:




- användare som har bråttom betalar mer för att bli inkluderade snabbt;
- gruvarbetare uppmuntras att inkludera transaktioner som betalar de högsta avgifterna för blockutrymme.
- nätverket undviker spam, eftersom det kostar att publicera en transaktion.



#### Hur beräknas transaktionsavgifter?



I motsats till vad många tror är avgifter inte en output i en Bitcoin-transaktion. Faktum är att en transaktion spenderar inmatningar och skapar utmatningar. Inmatningar representerar källan till bitcoins som används, medan utmatningar representerar betalningens destination. Transaktionsavgifter är helt enkelt **skillnaden mellan totala inmatningar och totala utmatningar**.



Med andra ord skapar användarens bitcoininmatningar, som tillhör dem, utmatningar för mottagarna, men reproducerar inte hela det belopp som förbrukas av inmatningarna. Skillnaden mellan de två utgör de transaktionsavgifter som gruvarbetaren kan ta ut.



Låt oss ta ett exempel. En transaktion förbrukar två inputs, en på 100 000 sats` och den andra på 150 000 sats`, och skapar tre outputs på 35 000 sats`, 42 000 sats` och 170 000 sats`.



![Image](assets/fr/027.webp)



Summan av inputs är därför 250 000 sats`, medan summan av outputs är 247 000 sats`. Detta innebär att 3 000 sats` har förbrukats i insatser utan att återskapas i insatser: detta belopp motsvarar de avgifter som föreslås i denna transaktion.



![Image](assets/fr/028.webp)



Om en miner inkluderar den här transaktionen i ett giltigt block har han rätt att få tillbaka dessa 3 000 sats, utöver avgifterna för alla andra transaktioner som ingår i blocket. Det finns dock ingen direkt on-chain-länk mellan den transaktion som betalar avgiften och de sats som faktiskt inkasseras av mineraren. Tekniskt sett förstörs de 3 000 sats i avgifter, och i gengäld får utvinnaren rätt att återskapa samma belopp för sig själv.



#### Avgiftsförhållandet



Ett block begränsas inte av antalet transaktioner, utan av dess totala kapacitet (idag i praktiken av blockets vikt). Vissa transaktioner tar mer plats än andra: en transaktion med många in- och utgångar blir större än en enkel transaktion med en enda ingång och två utgångar. De skript som används påverkar också storleken.



![Image](assets/fr/026.webp)



Två transaktioner kan därför betala samma avgiftsbelopp i absoluta tal, men inte vara ekonomiskt likvärdiga ur minarens synvinkel. Om den ena är dubbelt så stor kostar den dubbelt så mycket utrymme i blocket. Utrymme är en bristvara, så utvinnaren försöker maximera sina intäkter per utrymmesenhet.



Det är därför som vi i praktiken uttrycker en transaktions konkurrenskraft med en avgiftskvot, vanligtvis i sats/vB ([satoshi](https://planb.academy/resources/glossary/satoshi-sat) per virtuell byte). Att beräkna denna kvot är enkelt:



```text
fee rate = fee / weight (in vB)
```



Om vi t.ex. har en transaktion som väger 141 vB` och som tilldelas 1 974 sats` i avgifter, kommer den att ha en avgiftssats på 14 sats/vB`.



```text
1 974 / 141 ≈ 14 sats/vB
```



Detta förhållande förklarar de ekonomiska val som görs av miners: vid fast kapacitet maximerar inkludering av högpristransaktioner blockets totala avgifter, och därmed miners ersättning. Det förklarar också varför lågkostnadstransaktioner står kvar i kö i mempooler under långa perioder: de konkurrerar med andra transaktioner som betalar mer per utrymmesenhet.



### Nätverksskydd mot skräppost



Avgifter har också ett operativt säkerhetssyfte: de medför en kostnad för multipliceringen av transaktioner. Om det vore gratis att publicera en transaktion skulle det vara lätt att översvämma nätverket med värdelösa transaktioner och mätta mempooler, vilket skulle öka belastningen på noderna.



I praktiken tillämpar noderna lokala vidarebefordringspolicyer (mempool-regler) och fastställer ofta en lägsta avgiftströskel under vilken de inte vidarebefordrar en transaktion (som standard `0,1 sat/vB` i Bitcoin Core via `minRelayTxFee`). En transaktion kan vara giltig i strikt mening enligt konsensusreglerna, men inte vidarebefordras av de flesta noder om avgifterna är för låga. Följden blir att den inte cirkulerar, inte når utvinnarna och har mycket liten chans att bli bekräftad.



Vid det här laget har du fått kärnan i blockbelöningen: den motsvarar kompensationen för den vinnande gruvarbetaren och består av två distinkta element. Å ena sidan en blocksubvention, definierad av protokollreglerna, som skapar nya bitcoins ex nihilo. Och å andra sidan avgifterna för transaktioner som ingår i det minerade blocket.



I nästa kapitel kommer vi att fokusera mer i detalj på blocksubventionen för att förstå exakt hur den beräknas och hur den utvecklas över tid enligt reglerna i Bitcoin-protokollet.



## Halving


<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>



I föregående kapitel såg vi att miners som producerar ett giltigt block får en belöning som består av avgifterna för de transaktioner som ingår i blocket plus en blocksubvention. Vi har dock ännu inte förklarat hur storleken på denna subvention bestäms. Den mekanism som fastställer och utvecklar detta värde kallas ***[halving](https://planb.academy/resources/glossary/halving)***.



### Vad är halvering?



Halving är en händelse som är inprogrammerad i Bitcoin-protokollet och som halverar blocksubventionen, dvs. det maximala antalet nya bitcoins som den vinnande mineraren får skapa för varje block. Det påverkar inte transaktionsavgifterna: avgifterna existerar oberoende och bestäms fortfarande av användaraktivitet och konkurrens om blockutrymme.



När Bitcoin lanserades 2009 sattes blocksubventionen till 50 BTC för varje utvunnet block. Sedan dess har denna subvention halverats flera gånger för varje halvering.



![Image](assets/fr/029.webp)



Halving utlöses inte av ett datum, utan av blockhöjden. Den exekveras **var 210 000:e block**. Eftersom Bitcoin siktar på ett genomsnittligt intervall på cirka 10 minuter per block, motsvarar 210 000 block ungefär fyra år.



```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```



Om vi således noterar `n` antalet halveringar som redan skett, kan blocksubventionen i BTC beräknas enligt följande:



```text
subsidy(n) = 50 / 2^n
```



### Tidigare halvningar



Här följer en sammanfattande tabell över redan genomförda halveringar, med blockhöjd, datum och den nya blocksubvention som gäller efter händelsen:



| Event               |   Height  | Date                        | Subsidy    |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 july 2016                 |   12,5 BTC |
| Halving 3           |   630 000 | 11 may 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 april 2024               |  3,125 BTC |
| Halving 5 (upcoming) | 1 050 000 | Spring   2028 (estimation) | 1,5625 BTC |

### När och hur upphör subventionen?



Halving upprepas så länge som subventionen kan uttryckas i systemets minsta enhet: satoshi.



```text
1 BTC = 100 000 000 sats
```



När subventionen halveras når vi så småningom fraktioner av en bitcoin som är så små att de blir mindre än 1 satoshi. Vid denna punkt är det inte längre möjligt att skapa en halv enhet av satoshi. Skapandet av pengar genom blocksubventionen upphör och miners kompenseras enbart på basis av transaktionsavgifter. Från och med denna tidpunkt kommer alla bitcoins att vara i omlopp och det kommer inte längre att vara möjligt att producera nya enheter.



Det definitiva slutet på blocksubventionerna kommer att inträffa på blocknivå 6.930.000, dvs. vid den 33:e och sista halveringen. Denna händelse förväntas äga rum omkring år 2140, även om det är omöjligt att ange ett exakt datum, eftersom det beror på den faktiska hastigheten med vilken block hittas fram till dess.



Eftersom blocksubventionen följer en geometrisk sekvens med förhållandet 1/2 vid varje halvering var penningskapandet extremt högt under Bitcoin:s tidiga dagar, för att sedan minska mycket snabbt. Vid den 7:e halveringen kommer över 99% av bitcoins redan att ha satts i omlopp. Tröskeln på 99% förväntas passeras mellan 2032 och 2036. Detta innebär att det då kommer att ta över 100 år att utvinna de sista återstående 1% av bitcoins. Medan den monetära inflationen var mycket hög när Bitcoin lanserades, för att möjliggöra en omfattande distribution av valutan, är den nu mycket låg och kommer att fortsätta att sjunka tills den når nivån för en riktig hårdvaluta, vars cirkulerande utbud inte längre kan öka.



![Image](assets/fr/030.webp)



### Varför kommer det aldrig att finnas 21 miljoner BTC?



Bitcoin:s maximala monetära tillgång presenteras ofta som 21 miljoner BTC. Detta är en bra approximation för att förstå dess penningpolitik, men ur en strikt teknisk synvinkel kommer det totala utbudet faktiskt aldrig att nå exakt 21 000 000 bitcoins.



Huvudskälet är mekaniskt. Genom successiva halveringar faller blocksubventionen så småningom under minimivärdet på 1 sat, vilket slutar utfärda innan den når den exakta teoretiska summan. Som ett resultat av denna minsta granularitet och avrundningsreglerna är det totala antalet bitcoins som skapats av subventionen något mindre än 21 miljoner.



Dessutom kan marginella protokollrelaterade avvikelser också lägga till detta. I sällsynta fall kan till exempel vissa gruvarbetare inte ha gjort anspråk på sin fulla subvention, vilket definitivt minskar mängden bitcoins som faktiskt utfärdats. Vi kan också nämna [genesisblocket](https://planb.academy/resources/glossary/genesis-block), producerat av Satoshi den 3 januari 2009, vars skapade bitcoins inte är en del av [UTXO set](https://planb.academy/resources/glossary/utxo-set), samt vissa historiska händelser kopplade till buggar, till exempel duplicerade coinbase-transaktionsidentifierare.



Slutligen måste vi också ta hänsyn till alla bitcoins som har förstörts eller blockerats:




- bitcoins inlåsta i olösliga skript;
- de som avsiktligt förstörts av `OP_RETURN`-skript;
- eller förlust av privata nycklar på applikationsnivå.



I teorin är Bitcoin:s tillgång därför begränsad till 21 miljoner. I praktiken kommer det dock aldrig att finnas 21 miljoner bitcoins i omlopp.



## Coinbase-transaktionen


<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>



I de tidigare kapitlen har vi presenterat två viktiga punkter. För det första får den miner som lyckas producera och distribuera ett giltigt block en belöning. Å andra sidan såg vi att denna belöning består av två distinkta element:




- en blocksubvention (bitcoins som skapas ex nihilo, vars maximala belopp fastställs av protokollet och gradvis minskas via halveringar);
- alla transaktionsavgifter som betalats av användare vars transaktioner har inkluderats i blocket.



En fråga kvarstår dock: genom vilken mekanism samlar gruvarbetaren in denna belöning i Bitcoin? Det är just detta som är rollen för en viss transaktion som kallas "coinbase".



### Hur coinbase-transaktionen fungerar



Som vi såg i den första delen av kursen innehåller varje Bitcoin-block en lista över väntande transaktioner som det kommer att bekräfta. Den allra första av dessa är alltid [coinbase-transaktionen](https://planb.academy/resources/glossary/coinbase-transaction). Det är den som gör det möjligt för den vinnande gruvarbetaren att få sin belöning.



![Image](assets/fr/031.webp)



Vid första anblicken ser det ut som en klassisk Bitcoin-transaktion: den har en [TXID](https://planb.academy/resources/glossary/txid-transaction-identifier), utgångar och ingår i blockets Merkle-träd. Den skiljer sig dock i ett viktigt avseende: den spenderar inte någon befintlig UTXO.



I en klassisk Bitcoin-transaktion refererar "inputs" till tidigare outnyttjade outputs (UTXO), som ger inputvärdet. Utgångarna omfördelar sedan detta värde till nya UTXO, med nya utgiftsvillkor. Med andra ord, för att skicka bitcoins måste du redan äga dem. Coinbase-transaktionen, å andra sidan, förbrukar inga bitcoins i input: den skapar bitcoins i output direkt från grunden.



Det är just denna mekanism som gör det möjligt att sätta nya bitcoins i omlopp via blocksubventionen och krediterar mineraren med de avgifter som är förknippade med de transaktioner som ingår i blocket. Coinbase-transaktionen kan inte referera till en verkligt existerande UTXO (i själva verket refererar den till en fiktiv UTXO), eftersom dess roll är just att skapa en del av värdet (subventionen) och återvinna den andra delen (avgifterna), utan att ta emot dem från en tidigare transaktion. För att hela systemet ska förbli konsekvent måste den del som motsvarar avgifterna exakt motsvara summan av bitcoins som förbrukats i input men inte återskapats i output i blockets övriga transaktioner.



![Image](assets/fr/032.webp)



Den här transaktionen är inte valfri. Ett block som inte innehåller en coinbase-transaktion är ogiltigt och kommer systematiskt att avvisas av nätverksnoderna.



⚠️ Observera: termen "*coinbase*" har ingen koppling till utbytesplattformen med samma namn. I Bitcoin hänvisar "*coinbase*" historiskt sett till den transaktion som skapar blockbelöningen. Företaget har helt enkelt antagit denna term för sitt namn.



Coinbase-transaktionen fyller faktiskt flera roller samtidigt:




- Den första är den som vi just har beskrivit: den tilldelar utvinnaren den belöning som denne har rätt till för att ha producerat ett giltigt block.
- Dess andra, mer tekniska, roll är att förankra det kryptografiska åtagandet till vittnena (signaturerna) för de SegWit-transaktioner som ingår i blocket.
- En tredje roll, den här gången inte direkt protokollrelaterad men kopplad till den moderna industrialiseringen av mining, är att myntbasen nu ofta används för att förankra godtyckliga tekniska data. Dessa data är i allmänhet kopplade till driften av mining-pooler och deras interna organisation.



För att hjälpa dig att förstå dessa olika användningsområden ska vi nu titta närmare på strukturen för coinbase-transaktionen.



### Den grundläggande strukturen för coinbase-transaktionen



En coinbase-transaktion måste innehålla exakt en input. För enkelhetens skull säger vi ibland att den inte har någon input, eftersom denna input inte spenderar någon verklig UTXO. I själva verket finns det en inmatning med en refererad källa, men den pekar avsiktligt på en icke-existerande UTXO.



Som vi redan har sett måste varje Bitcoin-transaktion konsumera UTXO som input för att skapa giltiga outputs. I Bitcoin-transaktionen sker denna förbrukning genom att en befintlig UTXO refereras som indata. Denna hänvisning görs helt enkelt genom att ange identifieraren för den föregående transaktionen (den i vilken UTXO skapades), samt dess index bland utdata i denna transaktion. I konkreta termer definieras en UTXO av en hash (den tidigare TXID) och ett index.



Men i fallet med coinbase-transaktionen, istället för att hänvisa till en verklig existerande UTXO, måste inmatningen nödvändigtvis peka på denna speciella falska UTXO, med ett TXID fullt av nollor, som inte motsvarar något verkligt TXID:



```text
0000000000000000000000000000000000000000000000000000000000000000
```


Direkt följt av det falska indexet:


```text
0xffffffff
```


![Image](assets/fr/033.webp)



I det grundläggande Bitcoin-protokollet, som beskrivs i Satoshi Nakamoto, är denna falska inmatning den enda begränsningen för coinbase-transaktionen.



Liksom alla UTXO som refereras till i en transaktions inmatning är den associerad med ett `scriptSig`-fält. I en konventionell transaktion innehåller detta `scriptSig`-fält de element som behövs för att tillfredsställa `scriptPubKey` och därmed låsa upp den använda UTXO. Men i det speciella fallet med coinbase, eftersom den UTXO som refereras till är avsiktligt fiktiv, är fältet `scriptSig` helt fritt. Miner kan därför ange vilken data de vill. Vi kommer senare att titta på hur denna frihet används.


Förutom denna falska input finns det en eller flera helt vanliga outputs, som gör det möjligt för mineraren att samla in bitcoins från belöningen på en av deras Bitcoin-adresser. Dessa utgångar är UTXO-adresser som är låsta med en `scriptPubKey` (t.ex. ett skript som pekar på en adress som kontrolleras av gruvarbetaren eller poolen). Den enda egenheten här ligger i regeln för beräkning av deras värde: den totala summan av myntbasens utgångar får aldrig överstiga den maximalt tillåtna subventionen, till vilken blockavgifterna läggs till.



Historiskt sett har alltså coinbase-transaktionen kokats ner till detta enkla schema: en falsk input som hänvisar till en icke-existerande UTXO, och en eller flera outputs som är utformade för att distribuera blockbelöningen till den vinnande mineraren. Idag är dock myntbasen inte längre begränsad till denna distributionsroll. Dess speciella position i blocket och den stora flexibiliteten i dess struktur har lett till nya användningsområden, både i själva protokollet och i mining poolhanteringsmekanismer.



### Andra användningsområden för coinbase



Med tiden har coinbase-transaktionen blivit en särskilt bekväm införingspunkt för att integrera en mängd olika information som är användbar för mining och för själva blockstrukturen. Låt oss ta en titt på dem för att bättre förstå den övergripande coinbase-organisationen.



#### BIP-34



[BIP-34](https://planb.academy/resources/glossary/bip0034) är en mjuk fork som implementerades i mars 2013, med början med block 227,930, som introducerade version 2 av Bitcoin block. Denna nya version kräver att varje block inkluderar, i `scriptSig` för coinbase-transaktionen, höjden på det block som skapas.



Å ena sidan klargör denna utveckling det sätt på vilket nätverket samtycker till att utveckla blockstruktur och konsensusregler. För det andra säkerställer den att varje block och coinbase-transaktion är unik.



Således är coinbases `scriptSig` inte helt fri. Sedan aktiveringen av BIP-34 är den helt enkelt begränsad till att börja med höjden på det block där denna coinbase-transaktion ingår.



![Image](assets/fr/035.webp)



#### Den extra-nonan



Som vi såg i de första kapitlen i den här kursen har utvinnaren ett 32-bitars noncefält i blockhuvudet, som de modifierar genom att pröva sig fram för att hitta en hash som är mindre än eller lika med målet. Detta 32-bitars utrymme tillåter redan ett mycket stort antal kombinationer som kan utforskas, men när mining-svårigheten är hög kan detta intervall vara helt uttömt på relativt kort tid och därmed kanske inte ge någon kombination som ger en giltig hash. Om alla möjliga värden för `nonce` har testats utan framgång måste utvinnaren sedan modifiera ett annat element för att ändra blockhuvudet och starta en ny serie försök.



Eftersom coinbase-transaktionen erbjuder ett fritt fält via `scriptSig` av dess inmatning, är lösningen som används för att utöka nonce-utrymmet att utnyttja en del av denna `scriptSig`. Detta kallas i allmänhet extra-nonce. Genom att ändra extra-nonce ändrar gruvarbetaren coinbases `scriptSig`, dvs. transaktionsidentifieraren, sedan Merkle-roten för blocket och slutligen själva blockhuvudet. På så sätt får de ett nytt sökutrymme av hashar att utforska, utan att behöva ändra de andra komponenterna i deras kandidatblock.



![Image](assets/fr/036.webp)



#### Identifiering av pooler och gruvarbetare



Idag är en mycket stor andel av världens hashrate organiserad i mining-pooler. Dessa strukturer sammanför enskilda gruvarbetare för att kombinera deras arbete och minska variationen i deras inkomster.



Av operativa skäl utnyttjar mining-pooler också det fria fältet i coinbase-ingångens `scriptSig` för att infoga olika bitar av information. Dessa varierar från pool till pool och från nätverksprotokoll till nätverksprotokoll, men inkluderar i allmänhet en unik identifierare (ofta en extra nonce strukturerad i flera underdelar) som tilldelas varje gruvarbetare för att undvika dubbelarbete inom poolen. En identifieringstagg för poolen läggs vanligtvis till och används för offentlig tilldelning av hittade block, mining-statistik och andra spårningsändamål.



![Image](assets/fr/037.webp)



#### SegWit:s åtagande



Sedan SegWit mjuk fork aktiverades 2017 har vittnesdata (dvs. i allmänhet signaturer) separerats från transaktionsmasterdata, framför allt för att korrigera [formbarhetsproblemet med Bitcoin-transaktioner](https://planb.academy/resources/glossary/malleability-transaction). Denna separation introducerar därför ett nytt element som ska begås i blocket.



För att göra detta grupperas vittnena tillsammans i ett annat dedikerat Merkle-träd, vars rot sedan är engagerad i coinbase-transaktionen via en `OP_RETURN` -utgång.



![Image](assets/fr/038.webp)



Jag kommer inte att gå in mer i detalj på denna mekanism i den här kursen, eftersom det ligger utanför ramen för den här artikeln, men kom bara ihåg att sedan introduktionen av SegWit fungerar coinbase-transaktionen som ett medel för att förankra i blocket ett fingeravtryck som sammanfattar alla SegWit-vittnen. Vittnena placeras i ett oberoende Merkle-träd, roten till detta träd skrivs till en utgång från coinbase-transaktionen, och denna coinbase-transaktion ingår i sin tur i det huvudsakliga Merkle-trädet tillsammans med alla andra transaktioner, vars rot visas i blockhuvudet. Det är på detta sätt som vittnena, som lagras separat från huvudtransaktionsdata, fortfarande är kopplade till blockhuvudet.



![Image](assets/fr/039.webp)



#### Godtyckliga meddelanden



Eftersom `scriptSig` tillåter fritt införande av godtycklig information som väljs av minern, har vissa utnyttjat möjligheten att lägga till meddelanden av mer personlig karaktär, snarare än tekniska. Det mest kända fallet är naturligtvis Satoshi Nakamoto, med sitt numera ikoniska meddelande:



> The Times 03/Jan/2009 Finansministern på randen till en andra räddningsaktion för bankerna

Detta meddelande, som finns i Genesis-blocket (det allra första blocket i Bitcoin), är faktiskt kodat i hexadecimal i `scriptSig` i coinbase-transaktionen:



```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```


![Image](assets/fr/034.webp)



### Förfallotid


När blocket har utvunnits och distribuerats visas coinbase-transaktionen på blockkedjan som vilken annan transaktion som helst. Den skapar UTXO:or för den vinnande minern, vilket gör det möjligt för dem att hämta sin belöning. Dessa UTXO är dock inte omedelbart spenderbara: de är föremål för en [löptid](https://planb.academy/resources/glossary/maturity-period). Denna löptid är satt till 100 block efter det block som innehåller coinbase. I konkreta termer måste därför coinbase-transaktionen totalt ha 101 bekräftelser för att dess utgångar ska kunna spenderas av den vinnande gruvarbetaren.


![Image](assets/fr/040.webp)


Syftet med denna regel är att begränsa effekterna av kedjeomorganisationer på ekonomin. Som vi har sett i tidigare kapitel kan det hända att två olika giltiga block på samma höjd hittas nästan samtidigt av olika miners. För ett kort ögonblick kan nätverket splittras: vissa noder får block A först, medan andra ser block B först. Under de efterföljande blocken får sedan en av de två grenarna mer arbete och blir referensgrenen. Den andra grenen överges och dess block blir obsoleta. De transaktioner som den innehöll kan då, i teorin, återvända till mempoolerna i väntan på bekräftelse.



I praktiken händer detta sällan, eftersom avgiftsmarknaden ofta resulterar i att nästan samma transaktioner förekommer i två konkurrerande block på samma höjd. Detta är en av anledningarna till att en Bitcoin-transaktion vanligen anses bli oföränderlig efter sex bekräftelser: omorganisationer på mer än sex block är så osannolika att de rimligen kan betraktas som omöjliga.



![Image](assets/fr/041.webp)



Problemet med dessa omorganisationer i fallet med coinbase-transaktionen är att det inte är någon vanlig transaktion. Den introducerar helt nya bitcoins i omlopp. Om blockbelöningen skulle kunna spenderas omedelbart skulle en problematisk kaskadsituation kunna uppstå:




- en gruvarbetare spenderar bitcoins från en coinbase,
- dessa bitcoins cirkulerar i ekonomin,
- sedan övergavs det ursprungliga kvarteret slutligen under en omorganisation.



De bitcoins som är i omlopp skulle då aldrig ha funnits i den slutliga kedjan och en serie transaktioner som var giltiga vid tidpunkten för utfärdandet skulle bli ogiltiga i efterhand.



Förfallotiden innebär en tidsram som är tillräckligt lång för att göra detta scenario orealistiskt. En omorganisation av 101 block anses i praktiken vara omöjlig (även om det fortfarande finns en försvinnande liten sannolikhet). Vi vet inte exakt varför Satoshi valde ett så högt värde för löptid, men det är troligt att det valdes så att mekanismen skulle förbli funktionell, även i händelse av stora nätverksfel.



Denna regel förhindrar att nyskapade blockbelöningspengar börjar cirkulera innan det block som generated de har blivit säkert begravda under en stor mängd ackumulerat arbete.



---

Vi har nu kommit till slutet av vår förklaring av hur Bitcoin mining fungerar. Du bör nu ha en klar bild av de grundläggande mekanismer som är inblandade.



I den sista delen av kursen återvänder vi till mer konkreta aspekter för att visa hur Bitcoin mining materialiseras i den verkliga världen: dess industrialisering, de maskiner som används, grupperingen av spelare och så vidare. Målet är att ge dig en övergripande bild av Bitcoin mining, både från det teoretiska och protokollära perspektivet som vi just har sett, och även från dess praktiska och operativa sida.



# Bitcoin mining-industrin


<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>



## Utvecklingen av mining-maskiner


<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>



Under Bitcoin:s tidiga dagar var mining inte en industriell verksamhet. Det var en del av Bitcoin-programvaran som lanserades på en persondator, ofta av nyfikenhet, ibland för att stödja nätverket och sekundärt för att få bitcoins som då praktiskt taget inte hade något marknadsvärde.



Under årens lopp har denna aktivitet genomgått en omvandling: maskinerna har förändrats, svårighetsgraden har exploderat och mining har blivit en industri i sig själv. Låt oss ta en titt på de operativa aspekterna av Bitcoin mining.



### Så här kommer du igång: mining med en CPU



Under 2009 och de första åren utfördes mining huvudsakligen med hjälp av CPU:n i en vanlig dator. Bitcoin var då bara en enkel mjukvara som fungerade som en wallet, en nod och en miner. Det räckte med att starta Satoshi Nakamoto:s programvara på sin dator för att delta i mining-processen och i många fall hitta block.



En CPU kan göra allt, men den är inte optimerad för någonting. Den utför mycket allmänna instruktioner med komplex logik. För en uppgift som repetitiv hashing av blockheaders är det inte det perfekta verktyget, men vid nätverksstart är svårighetsgraden så låg att det är mer än tillräckligt för att hitta block.



Denna period är viktig, eftersom den påminner oss om en viktig punkt: proof of work är inte beroende av en viss kategori av utrustning. Det som räknas är förmågan att beräkna hashar snabbare än andra, till en given kostnad. Så snart en teknisk fördel dyker upp omvandlas den automatiskt till en ekonomisk fördel. Men i absoluta termer är det fortfarande möjligt att försöka hitta Bitcoin-block med hjälp av en konventionell CPU. Detta är till exempel det tillvägagångssätt som används av NerdMiner-projektet. Chansen att hitta ett block är i stort sett obefintlig, men sannolikheten är ändå försvinnande liten.



https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Byte till GPU:er



Snart nog insåg gruvarbetarna att flaskhalsen inte var kraft, utan förmågan att utföra ett stort antal liknande operationer parallellt. Det var precis vad grafikprocessorer (GPU:er) kunde göra. Ursprungligen hade en GPU utformats för att utföra samma operationer på stora mängder data. Den här arkitekturen passade perfekt för en uppgift som upprepad hashing: istället för att ha några få mycket mångsidiga kärnor har du hundratals, sedan tusentals enheter som kan utföra samma instruktioner samtidigt.



Med jämförbar strömförbrukning kan en GPU producera betydligt fler hashvärden per sekund än en CPU. Samtidigt hade bitcoin en växelkurs mot dollarn, dess värde ökade och växlingsplattformar dök upp. Från och med då började mining:s karaktär att förändras. Det handlade inte längre bara om att delta, utan om att tjäna pengar. Dedikerade konfigurationer dök upp: maskiner byggda kring flera grafikkort, ibland utan skärmar, med ett minimalt system och specialiserad programvara, vars enda syfte var att bryta.



Det var vid denna tidpunkt som svårigheten med mining började explodera. Mellan mitten av 2010 och mitten av 2011 ökade den till och med med en faktor 1 000. Mekaniskt sett börjar specialiseringen, precis som de tidiga formerna av industrialisering, och vanliga användare - som nöjer sig med att köra Bitcoin-programvaran på sina persondatorer - har nu bara en mycket liten chans att hitta ett giltigt block.



![Image](assets/fr/044.webp)



*Källa: [CoinWarz.com [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*



Mellan GPU-eran och den moderna [ASIC](https://planb.academy/resources/glossary/asic)-eran fanns en mellanliggande fas: användningen av FPGA:er. En FPGA är en omprogrammerbar komponent: den kan konfigureras för att direkt implementera en logisk krets som är avsedd för en viss beräkning, i det här fallet `SHA256d`. Tanken var att man skulle komma ännu längre bort från den generella hårdvaran (CPU/GPU) för att öka energieffektiviteten. Men snart skulle de förbättringar som gjorts virtuellt på FPGA:er tillämpas fysiskt på själva chipen: det är ankomsten av ASIC.



### Ankomsten av ASIC



Det sista steget i specialiseringen av mining-hårdvaran var uppkomsten av ASIC (*Application-Specific Integrated Circuits*). En ASIC är ett chip som är utformat för en enda uppgift. I fallet med Bitcoin mining är denna uppgift just exekveringen av `SHA256d` vid maximal hastighet och med optimal energieffektivitet. Till skillnad från en GPU används en ASIC inte för att köra spel, 3D-rendering eller AI. Den är till för hashing, och det är allt.



![Image](assets/fr/045.webp)



*ASIC S21 XP tillverkad av Bitmain*



Denna specialisering har två viktiga konsekvenser:




- Den första är ett språng i prestanda och effektivitet. För enheter av jämförbar generation producerar en ASIC betydligt fler hashningar per sekund än en GPU, samtidigt som den förbrukar mindre ström. Mining med GPU blev snabbt inte konkurrenskraftig: även om det fungerade tekniskt var elkostnaden långt större än den förväntade intäkten i de flesta sammanhang;
- Den andra är en förändring av modellen: investeringarna har huvudsakligen flyttats till hårdvara av industriell kvalitet. Mining innebär nu att man köper maskiner som är utformade för detta ändamål, driver dem kontinuerligt, kyler dem, underhåller dem och absorberar deras föråldring. Eftersom en ASIC inte är ekonomiskt evig: när en ny, effektivare generation kommer ut på marknaden blir de gamla maskinerna gradvis mindre lönsamma, även om de förblir funktionsdugliga.



Från och med då talar vi inte längre bara om en hobby. Vi talar om en sektor där konkurrenskraften är beroende av en ekvation:




- kostnaden för elektricitet;
- kostnader för utrustning och avskrivningar;
- förmåga att kyla och arbeta i stor skala;
- maskinens tillgänglighet och tillförlitlighet;
- snabbhet i kommunikationerna;
- etc.



### Mining gårdar



En isolerad maskin kan bedriva gruvdrift, men genom att gruppera hundratals, och till slut tusentals ASIC på en enda plats, delar vi fasta kostnader, optimerar logistiken och närmar oss en specialiserad datacentermodell.



En [mining-farm](https://planb.academy/resources/glossary/mining-farm) är i sin enklaste form en byggnad (eller en uppsättning containrar) fylld med ASIC:or som körs 24/7. Utmaningen är nu att upprätthålla stabila driftsförhållanden:




- leverera stora mängder billig och stabil elkraft;
- hantera värmen för att undvika strypning, eftersom energitätheten är betydande;
- filtrera damm, kontrollera luftfuktigheten, rengör;
- realtidsövervakning av maskinens prestanda (temperaturer, hårdvarufel, hashrate-fall etc.)



![Image](assets/fr/043.webp)



*En av de sju byggnader som är dedikerade till Bitcoin mining på Riot Platforms Rockdale-anläggning, nära Austin i Texas. Den här är särskilt tillägnad inlevelse mining*



Mining drivs nu av industriella aktörer, några av dem börsnoterade, som bygger och driver mycket storskaliga odlingar. Bland dessa finns MARA Holdings (Nasdaq: "MARA") och Riot Platforms (Nasdaq: "RIOT").



![Image](assets/fr/042.webp)



Även utan att gå in på detaljerna i lönsamhetsmodellerna är det viktigt att förstå varför mining har tagit denna form. Proof-of-work är en konkurrensmekanism: sannolikheten för att hitta ett block, och därmed tjäna pengar, är proportionell mot den andel hashrate som du använder. Som ett resultat av detta finns det ett konstant tryck på att öka datorkraften, minska kostnaden per beräkningsenhet och begränsa förlusterna. Som ett resultat blir miljöer som erbjuder billigare el, ett klimat som främjar kylning eller en riklig energiinfrastruktur naturligtvis mer attraktiva.



Mining Bitcoin har således utvecklats från en aktivitet som var tillgänglig för alla i början till en aktivitet som domineras av specialutrustning och professionell verksamhet. Detta ändrar inte protokollets regler. I teorin kan vem som helst bryta med vilken maskin som helst. Men i praktiken har svårighetsgraden och effektiviteten hos ASIC gjort att inhemska mining i de flesta sammanhang inte längre är konkurrenskraftiga.



Naturligtvis finns det fortfarande situationer där mining för hemmabruk kan vara av intresse, till exempel om du drar nytta av mycket billig el eller om du använder värmen generated från din gruvmaskin för att värma upp ditt hem på vintern. Men i vilket fall som helst måste du fortfarande köpa en maskin som är utrustad med ett ASIC-chip. Eftersom din mining-kraft kommer att förbli extremt liten i förhållande till Bitcoin-nätverket måste du dessutom hitta ett sätt att minska variansen i din inkomst: detta är just rollen för mining-pooler, som vi kommer att diskutera i nästa kapitel.



Om du vill utforska mining-lösningar med värmeåtervinning i hemmet har vi handledningar om olika verktyg, både färdiga att använda och DIY:



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## Gruppering i mining-pooler


<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>



Mining Bitcoin medför löpande och oundvikliga kostnader, främst för maskinens energiförbrukning. Dessa kostnader uppstår oberoende av eventuella resultat, även om intäkterna från mining till sin natur är sällsynta och slumpmässiga. Upptäckten av ett block beror uteslutande på gruvarbetarens andel av hashrate, vilket gör intäkterna desto mer oförutsägbara ju mindre denna andel är. Det är just detta praktiska problem som snabbt ledde till den utbredda användningen av [mining-pooler](https://planb.academy/resources/glossary/pool-mining). I detta sista kapitel av MIN 101-kursen erbjuder jag en introduktion till principerna och driften av mining-pooler i Bitcoin.



### Vad är en mining-pool?



En mining-pool är en organisation (ofta en onlinetjänst) som samlar datorkraften hos många oberoende miners, för att öka frekvensen med vilken deras grupp hittar block. När poolen hittar ett block omfördelas blockbelöningen sedan mellan deltagarna enligt interna poolregler (som kommer att behandlas i kursen MIN 201, eftersom de är för komplexa för MIN 101).



Deltagare i en mining-pool kallas då ofta "[hashare](https://planb.academy/resources/glossary/hasher)", snarare än "miners", eftersom de inte längre utför allt mining-arbete utan bara hashar de data som överförs till dem av poolen.



Var försiktig så att du inte blandar ihop mining-poolen med mining-gården. Detta är två olika koncept. Som vi såg i föregående kapitel är en farm en fysisk plats där en enda enhet driver ett stort antal mining-maskiner. En pool, å andra sidan, är framför allt en virtuell gruppering: tusentals maskiner, ofta geografiskt utspridda, arbetar under en gemensam samordning. En farm kan dock delta i en pool, och gör det ofta.



![Image](assets/fr/048.webp)



### Minska inkomstvariationen



Så varför gå med i en pool? Helt enkelt för att resultatet av mining-aktivitet är probabilistiskt: för varje hashförsök finns det en mycket liten chans att det kommer att uppfylla svårighetsmålet och därför producera ett giltigt block.



På mycket lång sikt bör din genomsnittliga vinst vara proportionell mot din andel av den totala hashrate. Denna princip följer direkt av sannolikhetslagarna: varje hashberäkning utgör en oberoende slumpmässig dragning, och enligt lagen om stora tal konvergerar frekvensen med vilken du upptäcker block matematiskt mot din andel av nätverkets totala hashrate. På kort till medellång sikt kan dock dina faktiska intäkter vara extremt oregelbundna. Det är denna diskrepans mellan teoretiskt genomsnitt och slumpmässig verklighet som vi kallar **varians** inom matematiken.



Här är ett enkelt exempel för att illustrera principen:




- Bitcoin-nätverket producerar i genomsnitt 144 block per dag (ungefär ett block var 10:e minut);
- Om du har "0,0001 %" av det totala antalet hashrate, är din förväntan "144 × 0,000001" eller "0,000144" block/dag;
- Med andra ord bör du hitta ett block i genomsnitt var `1 / 0,000144` dag, dvs. var 6.944:e dag eller cirka 19 år.



Men detta värde motsvarar bara en matematisk förväntan: fördelningen av upptäcktstider följer en slumpmässig lag, så det är fullt möjligt att i praktiken aldrig upptäcka ett enda block, inte ens under en mycket lång period. Du kan ha otur och inte hitta något under en mycket lång tid, samtidigt som du betalar återkommande kostnader (el, underhåll, avskrivning av utrustning ...).



mining-poolen ändrar karaktären på detta problem: genom att kombinera hashrate hittar poolen block oftare. Varje deltagare går sedan med på att endast få en bråkdel av varje block som hittas, men mycket oftare. Det är en omvandling från en mycket volatil inkomst med stora mellanrum till en mer regelbunden inkomst, till priset av att dela belöningarna och betala serviceavgifter.



### Varför sjunker variansen när ni grupperar er tillsammans?



Ju högre datorkraft, desto högre blir den förväntade frekvensen av block som hittas. Ännu viktigare är att ju oftare händelserna inträffar, desto närmare ligger de observerade resultaten det statistiska genomsnittet under en viss period.



På solobasis kan en småskalig gruvarbetare gå i åratal utan ett enda block, sedan få en stor utbetalning en dag och sedan ingenting. I en pool gäller fortfarande samma probabilistiska verklighet, men den jämnas ut på kollektiv nivå: poolen hittar block oftare, och omfördelning omvandlar dessa händelser till mer regelbundna utbetalningar för varje deltagare. ** mining-poolen säljer därför förutsägbarhet på mining-aktiviteten**.



### Historiska landmärken



Som vi såg i föregående kapitel kunde mining i början göras på egen hand med en vanlig dator, eftersom svårighetsgraden var mycket låg. Men när det globala hashrate exploderade (GPU, sedan ASIC) blev solo mining ett mycket tidskrävande vågspel för de flesta deltagare.



De första poolerna skapades just som ett svar på denna nya verklighet. Braiins Pool (tidigare Slush Pool / Bitcoin.cz) är den första Bitcoin mining-poolen: den minade sitt första block den 16 december 2010. Framgången för denna första mining-pool var snabb, eftersom den på bara några dagar erövrade nästan 3,5% av den globala hashrate.



![Image](assets/fr/047.webp)



På den tekniska sidan strukturerades pooler sedan runt specialiserade kommunikationsprotokoll mellan poolen och gruvarbetarna (t.ex. [Stratum](https://planb.academy/resources/glossary/stratum), sedan Stratum V2) för att effektivt orkestrera distribuerat arbete. Vi kommer att titta närmare på dessa begrepp i vår MIN 201-kurs.



### Den moderna situationen



I skrivande stund (tidigt 2026) ligger den globala Bitcoin hashrate på en storleksordning av zetta-hash per sekund (= 1 000 EH/s = 1 000 000 000 000 000 000 hashes per sekund), och nästan alla block som hittas kommer från mining-pooler.



Här är en ranking, hittills, av de viktigaste mining-poolerna och deras respektive andel av hashrate. Denna ranking kommer sannolikt att ändras när du läser denna kurs. För uppdaterade uppgifter, besök [mempool.space](https://mempool.space/graphs/mining/pools).



![Image](assets/fr/046.webp)



| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Källa [mempool.space] (https://mempool.space/graphs/mining/pools), en månads data, 16 december 2025 till 16 januari 2025.*



I en mer avancerad kurs kommer vi att gå djupare in i poolernas interna arbete (aktier, nätverksprotokoll, betalningsmetoder ...), eftersom det är här detaljerna som avgör både gruvarbetarens lönsamhet och de potentiella konsekvenserna för Bitcoin spelar in.



---

Vi har nu kommit till slutet av MIN 101. Tack för att du har följt kursen ända till slutet. Om du vill utvärdera de kunskaper som du har förvärvat under kursens gång väntar ett slutprov i nästa avsnitt.



Med de grundläggande kunskaper som du just har förvärvat kan du nu gå mer avancerade kurser om mining på Plan ₿ Academy, antingen i teori, som den här, eller mer praktiska kurser, så att du också kan börja delta i Bitcoin mining!



# Sista delen


<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>



## Recensioner & betyg


<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>


<isCourseReview>true</isCourseReview>

## Slutlig examination


<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>


<isCourseExam>true</isCourseExam>

## Slutsats


<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>


<isCourseConclusion>true</isCourseConclusion>