---
name: OXT - Kedjeanalys
description: Behärska grunderna i kedjeanalys på Bitcoin
---
![cover](assets/cover.webp)


***VARNING:** Efter gripandet av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april är **webbplatsen OXT.me för närvarande otillgänglig**. Det är dock fortfarande möjligt att detta verktyg kan komma att återlanseras under de kommande veckorna. Under tiden kan du fortfarande dra nytta av denna handledning för att förstå grunderna i kedjeanalys på Bitcoin. Alla heuristiker och mönster som presenteras här förblir tillämpliga på Bitcoin-transaktioner. Även om dessa verktyg är mindre optimerade än OXT kan du tillfälligt använda [Mempool.space](https://Mempool.space/) eller [Bitcoin Explorer](https://bitcoinexplorer.org/) för att omsätta de teoretiska begreppen i denna artikel i praktiken.*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

I den här artikeln kommer du att lära dig de väsentliga teoretiska grunderna som behövs för att påbörja grundläggande kedjeanalyser på Bitcoin, och ännu viktigare, för att förstå hur de som observerar dig fungerar. Även om den här artikeln inte är en praktisk handledning om OXT-verktyget (ett ämne som vi kommer att behandla i en framtida handledning), sammanställer den en uppsättning viktiga kunskaper för dess användning. För varje modell, mätvärde och indikator som presenteras finns en länk till en exempeltransaktion i OXT, så att du bättre kan förstå hur den används och öva dig parallellt med att du läser.


## Inledning

En av pengarnas funktioner är att lösa problemet med att behov sammanfaller två gånger. I ett system som bygger på byteshandel kräver en Exchange inte bara att man hittar en individ som erbjuder en vara som uppfyller mitt behov, utan också att man förser denne med en vara av motsvarande värde som uppfyller dennes behov. Att hitta denna balans visar sig vara komplicerat. Det är därför vi använder oss av pengar, som gör det möjligt för oss att flytta värde både i tid och rum.


För att pengar ska lösa detta problem är det viktigt att den part som tillhandahåller en vara eller tjänst är övertygad om sin förmåga att spendera summan senare. Varje rationell individ som är villig att ta emot en peng, oavsett om den är digital eller fysisk, kommer därför att se till att den uppfyller två grundläggande kriterier:


- Myntet måste vara intakt och äkta;
- och det får inte spenderas dubbelt.


Om vi använder fysiska pengar är det den första egenskapen som är svårast att hävda. Under olika perioder i historien har metallmyntens integritet ofta påverkats av metoder som klippning eller borrning. Under det antika Rom var det t.ex. vanligt att medborgarna skrapade kanterna på guldmynt för att samla in lite ädelmetall, samtidigt som de behöll dem för framtida transaktioner. Det var bland annat därför som man senare stämplade spår på kanten av mynten. Äkthet är också en egenskap som är svår att verifiera på ett fysiskt monetärt medium. Numera är teknikerna för att bekämpa förfalskning alltmer komplexa, vilket tvingar handlare att investera i dyra verifieringssystem.


Å andra sidan är dubbla utgifter inte ett problem för fysiska valutor på grund av deras natur. Om jag ger dig en 10-eurosedeln lämnar den oåterkalleligen min ägo för att komma in i din, vilket utesluter varje möjlighet till dubbelutnyttjande av de monetära enheter som den representerar.

För digital valuta är utmaningen en annan. Det är ofta enklare att säkerställa ett mynts äkthet och integritet, men det är mer komplicerat att säkerställa att det inte förekommer dubbla utgifter. Varje digital vara är i grunden information. Till skillnad från fysiska varor delas inte information under utbytet, utan sprids genom att multipliceras. Om jag t.ex. skickar ett dokument till dig via e-post, så dupliceras det. Du kan inte med säkerhet verifiera att jag har raderat originaldokumentet.


Det enda sättet att undvika denna duplicering av en digital vara är att vara medveten om alla utbyten i systemet. På så sätt kan man veta vem som äger vad och uppdatera allas konton baserat på de transaktioner som gjorts. Detta är vad som till exempel görs med skripturala pengar. När du betalar 10 euro till en handlare med kreditkort noterar banken denna Exchange och uppdaterar Ledger.


På Bitcoin sker förhindrandet av dubbla utgifter på samma sätt. Det försöker bekräfta att det inte finns någon transaktion som redan har använt mynten i fråga. Om dessa mynt aldrig har använts kan vi vara säkra på att inga dubbla utgifter kommer att ske. Detta är den berömda frasen från Satoshi Nakamoto i vitboken: "*Det enda sättet att bekräfta frånvaron av en transaktion är att vara medveten om alla transaktioner.*"


Till skillnad från bankmodellen vill vi i Bitcoin inte behöva lita på en central enhet. Därför måste alla användare kunna bekräfta att det inte förekommer några dubbla utgifter, utan att förlita sig på en tredje part. Därför måste alla vara medvetna om alla Bitcoin-transaktioner.


Det är just denna offentliga spridning av information som komplicerar skyddet av privatlivet på Bitcoin. I det traditionella banksystemet är det i teorin bara finansinstitutet som känner till de transaktioner som görs. Men på Bitcoin informeras alla användare om alla transaktioner via sina respektive noder.


På grund av denna begränsning av spridningen skiljer sig Bitcoin:s integritetsmodell från banksystemets. I det senare är transaktionerna kopplade till användarens identitet, men informationsflödet är avskuret mellan den betrodda tredje parten och allmänheten. Med andra ord vet din bankman att du köper din baguette varje morgon på det lokala bageriet, men din granne känner inte till alla dessa transaktioner. Eftersom informationsflödet inte kan brytas mellan transaktionerna och den offentliga domänen i fallet Bitcoin, bygger sekretessmodellen på att användarens identitet separeras från själva transaktionerna.

![analysis](assets/en/1.webp)

*Diagram inspirerat av Satoshi Nakamotos i vitboken: Bitcoin: A Peer-to-Peer Electronic Cash System, avsnitt 10 "Sekretess".*

Eftersom Bitcoin-transaktioner offentliggörs blir det möjligt att skapa länkar mellan dem för att härleda information om de inblandade parterna. Denna aktivitet utgör till och med en specialitet i sig, vanligen kallad "kedjeanalys". I den här artikeln inbjuder jag dig att utforska grunderna i kedjeanalys för att förstå hur dina bitcoins spåras.


Majoriteten av de företag som specialiserar sig på kedjeanalys arbetar som svarta lådor och avslöjar inte sina metoder. Därför är det svårt att få information om denna praxis. När jag skrev den här artikeln förlitade jag mig främst på de få öppna resurser som finns tillgängliga:


- Huvuddelen av min artikel är hämtad från serien med fyra artiklar med namnet: [Understanding Bitcoin Privacy with OXT] (https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923), producerad av Samourai Wallet 2021;
- Jag har också använt olika rapporter från [OXT Research] (https://medium.com/oxt-research), samt deras kostnadsfria verktyg för kedjeanalys;
- Mer allmänt kommer min kunskap från de olika tweetsen och innehållet från [@LaurentMT] (https://twitter.com/LaurentMT) och [@ErgoBTC] (https://twitter.com/ErgoBTC);
- Jag blev också inspirerad av [Space Kek #19] (https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) där jag deltog tillsammans med [@louneskmt] (https://twitter.com/louneskmt), [@TheoPantamis] (https://twitter.com/TheoPantamis), [@Sosthene___] (https://twitter.com/Sosthene___) och [@LaurentMT] (https://twitter.com/LaurentMT).


Jag skulle vilja tacka deras författare, utvecklare och producenter. Utan deras olika innehåll och programvara skulle denna artikel inte finnas. Jag tackar också de granskare som noggrant har korrigerat texten och bistått mig med sina expertråd:


- [Gilles Cadignan](https://twitter.com/gillesCadignan);
- [Ludovic Lars](https://twitter.com/lugaxker) ([https://viresinnumeris.fr/](https://viresinnumeris.fr/)).


*För din information har jag lagt till en teknisk minileklista i slutet av artikeln för att definiera vissa termer. Om du ser ett ord som du inte förstår med en asterisk, finns definitionen längst ner på sidan.*


## Vad är kedjeanalys?

Kedjeanalys är en metod som omfattar alla metoder för att spåra Bitcoin-flöden på Blockchain. Generellt bygger kedjeanalys på att man observerar egenskaper i stickprov av tidigare transaktioner. Det handlar sedan om att identifiera samma egenskaper i en transaktion som man vill analysera och dra slutsatser om rimliga tolkningar. Denna problemlösningsmetod, som bygger på ett praktiskt tillvägagångssätt för att hitta en tillräckligt bra lösning, är vad som kallas en heuristik.


Förenklat kan sägas att kedjeanalysen görs i två huvudsakliga steg:

1. Identifiering av kända egenskaper;

2. Utledning av hypoteser.


Ett av syftena med kedjeanalys är att gruppera olika aktiviteter på Bitcoin för att fastställa hur unik den användare är som utfört dem. Därefter kommer det att vara möjligt att försöka koppla denna bunt av aktiviteter till en verklig identitet.


Kom ihåg min introduktion. Jag förklarade varför Bitcoin:s integritetsmodell ursprungligen byggde på att separera användarens identitet från dennes transaktioner. Det skulle därför vara frestande att tro att kedjeanalys är onödig, eftersom även om man lyckas gruppera On-Chain-aktiviteter kan de inte kopplas till en riktig identitet. Teoretiskt sett är detta uttalande korrekt. Kryptografiska nyckelpar används för att fastställa villkor för UTXO:erna. Dessa nyckelpar avslöjar i princip inte någon information om innehavarens identitet. Även om man lyckas gruppera aktiviteter som är kopplade till olika nyckelpar, säger detta oss ingenting om den enhet som ligger bakom dessa aktiviteter.


Den praktiska verkligheten är dock mycket mer komplex. Det finns en mängd olika beteenden som riskerar att koppla en verklig identitet till en On-Chain-aktivitet. I analysen kallas detta för en ingångspunkt, och det finns många av dem. Den vanligaste är naturligtvis KYC (Know Your Customer). Om du tar ut dina bitcoins från en reglerad plattform till en av dina personliga mottagningsadresser kan vissa personer koppla din identitet till denna Address. Mer allmänt kan en ingångspunkt vara vilken form av interaktion som helst mellan ditt verkliga liv och en Bitcoin-transaktion. Om du till exempel publicerar en mottagande Address på dina sociala nätverk kan detta vara en ingångspunkt för analys. Om du gör en betalning i bitcoins till din bagare kan de associera ditt ansikte (som är en del av din identitet) med en Bitcoin Address.

Dessa ingångspunkter är nästan oundvikliga när man använder Bitcoin. Även om man kan försöka begränsa deras omfattning kommer de att finnas kvar. Det är därför det är viktigt att kombinera metoder som syftar till att bevara din integritet. Att upprätthålla en acceptabel åtskillnad mellan din verkliga identitet och dina transaktioner är ett lovvärt tillvägagångssätt, men det är fortfarande otillräckligt. Om alla dina On-Chain-aktiviteter kan grupperas tillsammans kan till och med den minsta ingångspunkten äventyra den enda Layer av integritet som du har upprättat.


Därför är det också nödvändigt att hantera kedjeanalys i vår användning av Bitcoin. Genom att göra det kan vi minimera aggregeringen av våra aktiviteter och begränsa effekterna av en ingångspunkt på vår integritet. Exakt, för att bättre motverka kedjeanalys, vilket bättre tillvägagångssätt än att bekanta sig med de metoder som används i kedjeanalys? Om du vill veta hur du kan förbättra din integritet på Bitcoin måste du förstå dessa metoder. Detta gör att du bättre kan förstå tekniker som [CoinJoin](https://planb.network/tutorials/privacy/On-Chain/CoinJoin-samourai-Wallet-e566803d-ab3f-4d98-9136-5462009262ef) eller [PayJoin](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f) och minska de misstag du kan göra.


I detta kan vi dra en analogi med kryptografi och kryptoanalys. En duktig kryptograf är först och främst en duktig kryptoanalytiker. För att kunna föreställa sig en ny krypteringsalgoritm måste man veta vilka attacker den kommer att utsättas för, och även studera varför tidigare algoritmer bröts. Samma princip gäller för sekretess på Bitcoin. Att förstå metoderna för kedjeanalys är nyckeln till att skydda sig mot den. Det är därför jag erbjuder dig den här artikeln.


Det är viktigt att förstå att kedjeanalys inte är någon exakt vetenskap. Den förlitar sig på heuristik som härrör från tidigare observationer eller logiska tolkningar. Dessa regler möjliggör ganska tillförlitliga resultat, men aldrig med absolut precision. Med andra ord innebär kedjeanalys alltid en dimension av sannolikhet i de slutsatser som dras. Vi kan med mer eller mindre säkerhet uppskatta att två adresser tillhör samma enhet, men total säkerhet kommer alltid att vara utom räckhåll.


Hela syftet med kedjeanalys ligger just i sammanställningen av olika heuristiker för att minimera risken för fel. Det är på sätt och vis en ackumulering av bevis som gör att vi kan komma närmare verkligheten.


Dessa berömda heuristiker kan grupperas i olika kategorier som vi kommer att beskriva tillsammans:


- Transaktionsmönster (eller transaktionsmodeller);
- Intern heuristik för transaktionen;
- Extern heuristik till transaktionen.


Det är värt att notera att de två första heuristikerna på Bitcoin formulerades av Satoshi Nakamoto själv. Han diskuterar dem i del 10 av vitboken. Som vi kommer att se senare är det intressant att observera att dessa två heuristiker fortfarande har en framträdande roll i kedjeanalys idag. Dessa är:


- cIOH (Common Input Ownership Heuristic);
- och återanvändning av Address.


Låt oss tillsammans utforska de observerbara egenskaperna och de tolkningar som kan göras för att genomföra en analys.


## Transaktionsmönster (eller transaktionsmodeller)

Ett transaktionsmönster är helt enkelt en typisk transaktionsmodell som kan hittas på Blockchain och vars tolkning sannolikt är känd. När vi studerar mönster kommer vi att fokusera på en enda transaktion som vi analyserar på en hög nivå. Med andra ord kommer vi bara att titta på antalet in- och utgångar, utan att gå in på mer specifika detaljer eller dess miljö. Utifrån den observerade modellen kommer vi att kunna tolka transaktionens karaktär. Vi kommer sedan att leta efter egenskaper hos dess struktur och härleda en tolkning.


### En enkel sändning (eller enkel betalning)

Denna modell kännetecknas av att en eller flera UTXO:er konsumeras som input och att två UTXO:er produceras som output.


![analysis](assets/en/2.webp)


Tolkningen av denna modell är att vi befinner oss i en sändnings- eller betalningstransaktion. Användaren har konsumerat sina egna UTXO:er som input för att i output tillfredsställa en betalning UTXO och en förändring UTXO (förändring som kommer tillbaka till samma användare). Vi vet därför att den observerade användaren sannolikt inte längre är i besittning av en av de två UTXO:erna i utdata (betalningen), men fortfarande är i besittning av den andra UTXO (förändringen).


I det här läget är det omöjligt för oss att specificera vilken utgång som representerar vilken UTXO, eftersom det inte är målet med den här modellen. Vi kommer att kunna göra det genom att förlita oss på de heuristiker som vi kommer att studera i följande del. I detta skede är vårt mål begränsat till att identifiera vilken typ av transaktion det rör sig om, vilket i detta fall är en enkel sändning.


Här är till exempel en Bitcoin-transaktion som använder sig av det enkla sändningsmönstret:

### Sweep ("sopa" på engelska)

Denna modell kännetecknas av konsumtion av en enda UTXO som input och produktion av en enda UTXO som output.


![analysis](assets/en/3.webp)


Tolkningen av denna modell är att vi befinner oss i närvaro av en självöverföring. Användaren har överfört sina bitcoins till sig själv, till en annan Address som de äger. Eftersom det inte sker någon förändring i transaktionen är det faktiskt mycket osannolikt att vi har att göra med en betalning. Vi vet då att den observerade användaren sannolikt fortfarande är i besittning av denna UTXO.


Här är till exempel en Bitcoin-transaktion som använder sig av svepmönstret:

[35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d](https://Mempool.space/tx/35f1072a0fda5ae106efb4fda871ab40e1f8023c6c47f396441ad4b995ea693d)


Denna typ av mönster kan dock också avslöja en självöverföring till ett Exchange-konto (kryptovaluta Exchange-plattform). Det kommer att vara studien av kända adresser och transaktionens sammanhang som gör att vi kan veta om det är en svepning till en självförvarad Wallet eller ett uttag till en plattform.


### Konsolidering

Denna modell kännetecknas av att flera UTXO:er förbrukas som input och att en enda UTXO produceras som output.


![analysis](assets/en/4.webp)


Tolkningen av denna modell är att vi befinner oss i en konsolidering. Detta är en vanlig praxis bland Bitcoin-användare, som syftar till att slå samman flera UTXO i väntan på en eventuell ökning av transaktionsavgifterna. Genom att utföra denna operation under en period då avgifterna är låga är det möjligt att spara på framtida avgifter.


Vi kan dra slutsatsen att användaren bakom den här transaktionen sannolikt hade alla UTXO:er i input och fortfarande har UTXO i output. Därför är det säkert en självöverföring.


Precis som svepningen kan denna typ av mönster också avslöja en självöverföring till ett Exchange-konto. Det kommer att vara studien av kända adresser och transaktionens sammanhang som gör att vi kan veta om det är en konsolidering till en självförvarad Wallet eller ett uttag till en plattform.


Här är till exempel en Bitcoin-transaktion som följer konsolideringsmönstret:

[77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94](https://Mempool.space/tx/77c16914211e237a9bd51a7ce0b1a7368631caed515fe51b081d220590589e94)

### Batch-utgiftsmodellen

Denna modell kännetecknas av att ett fåtal UTXO förbrukas som input (ofta bara en) och att många UTXO produceras som output.


![analysis](assets/en/5.webp)


Tolkningen av denna modell är att vi befinner oss i en situation med batch spending. Detta är en praxis som sannolikt avslöjar betydande ekonomisk aktivitet, som till exempel en Exchange, till exempel. Batchutgifter gör det möjligt för dessa enheter att spara på avgifter genom att kombinera sina utgifter i en enda transaktion.


Vi kan dra slutsatsen att UTXO-inmatningen kommer från ett företag med betydande ekonomisk aktivitet och att UTXO-utmatningarna kommer att spridas. En del kommer att tillhöra företagets kunder. Andra kan gå till partnerföretag. Slutligen kommer det säkert att finnas en förändring som återvänder till det utfärdande företaget.


Här är till exempel en Bitcoin-transaktion som antar batchutgiftsmönstret:

[8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43](https://Mempool.space/tx/8a7288758b6e5d550897beedd13c70bcbaba8709af01a7dbcc1f574b89176b43)


### Protokollspecifika transaktioner

Bland transaktionsmönstren kan vi också identifiera modeller som avslöjar användningen av ett specifikt protokoll. Till exempel kommer Whirlpool coinjoins att ha en lätt identifierbar struktur som gör att de kan särskiljas från andra klassiska transaktioner.


![analysis](assets/en/6.webp)


Analysen av detta mönster tyder på att vi sannolikt är i närvaro av en samarbetstransaktion. Det är också möjligt att observera en CoinJoin. Om den senare hypotesen visar sig vara korrekt, kan antalet utgångar ge oss en ungefärlig uppskattning av antalet deltagare.


Här är till exempel en Bitcoin-transaktion som följer mönstret för den samarbetsinriktade transaktionstypen CoinJoin:

[00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea](https://Mempool.space/tx/00601af905bede31086d9b1b79ee8399bd60c97e9c5bba197bdebeee028b9bea)


Det finns många andra protokoll som har sina egna specifika strukturer. Vi kan till exempel skilja mellan transaktioner av typen Wabisabi och transaktioner av typen Stamps.


## Heuristik för interna transaktioner

En intern heuristik är en specifik egenskap som identifieras i själva transaktionen, utan att man behöver undersöka dess omgivning, och som gör det möjligt för oss att dra slutsatser. Till skillnad från mönster som fokuserar på transaktionens övergripande struktur baseras interna heuristiker på den uppsättning data som kan extraheras. Detta inkluderar:


- Mängderna av olika UTXO, både inkommande och utgående;
- Allt som har med skript att göra: mottagningsadresser, versionshantering, locktimes...


I allmänhet gör denna typ av heuristik det möjligt för oss att identifiera förändringen i en specifik transaktion. På så sätt kan vi sedan fortsätta att spåra en enhet över flera olika transaktioner.


Jag vill än en gång påminna er om att dessa heuristiska metoder inte är helt exakta. Var och en för sig gör de det bara möjligt för oss att identifiera rimliga scenarier. Det är ackumuleringen av flera heuristiker som bidrar till att minska osäkerheten, utan att någonsin helt eliminera den.


### Interna likheter

Denna heuristik innebär att man studerar likheterna mellan inputs och outputs i samma transaktion. Om samma egenskap observeras på inputs och på endast en av outputs i transaktionen, är det troligt att denna output utgör förändringen.


Den mest uppenbara egenskapen är återanvändningen av en mottagande Address i samma transaktion.


![analysis](assets/en/7.webp)


Denna heuristik lämnar lite utrymme för tvivel. Om inte deras privata nyckel har äventyrats avslöjar samma mottagande Address oundvikligen en enda användares aktivitet. Tolkningen som följer är att förändringen av transaktionen är utdata med samma Address som indata. Detta gör att vi kan fortsätta spåra individen från denna förändring.


Här är till exempel en transaktion där denna heuristik sannolikt kan tillämpas:

[54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0](https://Mempool.space/tx/54364146665bfc453a55eae4bfb8fdf7c721d02cb96aadc480c8b16bdeb8d6d0)


Dessa likheter mellan in- och utdata stannar inte vid återanvändning av Address. Alla likheter i användningen av skript kan möjliggöra tillämpning av en heuristik. Ibland kan till exempel samma versionering mellan en inmatning och en av transaktionens utmatningar observeras.


![analysis](assets/en/8.webp)

I det här diagrammet kan vi se att ingångsnummer 0 låser upp ett P2WPKH-skript (SegWit V0 som börjar med "bc1q"). Utgångsnummer 0 använder samma typ av skript. Utgångsnummer 1 använder dock ett P2TR-skript (SegWit V1 som börjar med "bc1p"). Tolkningen av detta kännetecken är att det är troligt att Address med samma versionering som ingången är den ändrade Address. Den skulle därför fortfarande tillhöra samma användare.

Här är en transaktion där denna heuristik sannolikt kan tillämpas:

[db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578](https://Mempool.space/tx/db07516288771ce5d0a06b275962ec4af1b74500739f168e5800cbcb0e9dd578)


I den här transaktionen kan vi se att ingång nummer 0 och utgång nummer 1 använder P2WPKH-skript (SegWit V0), medan utgång nummer 0 använder en annan skripttyp, P2PKH (Legacy).


### Betalningar med runda tal

En annan intern heuristik som kan hjälpa oss att identifiera förändringen är det runda talet. När man står inför ett enkelt betalningsmönster (1 inmatning och 2 utmatningar) är det i allmänhet så att om en av utmatningarna spenderar ett runt belopp, så representerar det betalningen.


![analysis](assets/en/9.webp)


Genom uteslutning kan vi konstatera att om en output representerar betalningen, så representerar den andra förändringen. Därför kan vi tolka det som att det är sannolikt att användaren i input fortfarande har den output som identifierats som förändringen.


Det bör noteras att denna heuristik inte alltid är tillämplig, eftersom majoriteten av betalningarna fortfarande görs i fiatvalutaenheter. Faktum är att när en handlare i Frankrike accepterar Bitcoin, visar de i allmänhet inte stabila priser i Sats. De väljer hellre en konvertering mellan priset i euro och det belopp i bitcoins som ska betalas. Därför bör det inte finnas ett runt tal i transaktionsutgången. En analytiker kan dock försöka utföra denna konvertering med hänsyn till den Exchange-kurs som gällde när transaktionen sändes ut i nätverket.


Om Bitcoin en dag blir den föredragna beräkningsenheten på våra börser kan denna heuristik bli ännu mer användbar för analys.


Här är till exempel en transaktion där denna heuristik sannolikt kan tillämpas:

### De stora utgifterna


När ett tillräckligt stort gap upptäcks mellan två transaktionsutfall i en enkel betalningsmodell kan det uppskattas att det större utfallet sannolikt är förändringen.


![analysis](assets/en/10.webp)


Denna heuristik för största utdata är förmodligen den mest oprecisa av alla. Om den identifieras på egen hand är den ganska svag. Denna egenskap kan dock kombineras med andra heuristiker för att minska osäkerheten i vår tolkning.


Om vi t.ex. undersöker en transaktion med ett utflöde med ett runt belopp och ett annat utflöde med ett större belopp, kan vi minska vår osäkerhetsnivå genom att tillämpa heuristiken för runda betalningar och heuristiken för det största utflödet tillsammans.


Här är till exempel en transaktion där denna heuristik sannolikt kan tillämpas:

[b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf](https://Mempool.space/tx/b79d8f8e4756d34bbb26c659ab88314c220834c7a8b781c047a3916b56d14dcf)


## Extern heuristik till transaktionen

Studien av externa heuristiker är analysen av likheter, mönster och egenskaper hos vissa Elements som inte är inneboende i själva transaktionen. Med andra ord, om vi tidigare begränsade oss till att utnyttja Elements som är inneboende i transaktionen med interna heuristiker, utvidgar vi nu vårt analysfält till transaktionens omgivning tack vare externa heuristiker.


### Address Återanvändning

Detta är en av de mest välkända heuristikerna bland Bitcoiners. Återanvändning av Address gör det möjligt att upprätta en länk mellan olika transaktioner och olika UTXO:er. Det observeras när en Bitcoin som tar emot Address används flera gånger.


Tolkningen av återanvändning av Address är att alla UTXO:er som är låsta på denna Address tillhör (eller har tillhört) samma enhet. Denna heuristik lämnar lite utrymme för osäkerhet. När den identifieras har den tolkning som följer en stor chans att motsvara verkligheten.

Som förklarades i inledningen upptäcktes denna heuristik av Satoshi Nakamoto själv. I vitboken nämner han specifikt en lösning för att förhindra användare från att producera den, vilket helt enkelt är att använda en ny Address för varje ny transaktion: "* Som en extra brandvägg kan ett nytt nyckelpar användas för varje transaktion för att hålla dem olänkade till en gemensam ägare.*"


Här är till exempel en Address som återanvänds i flera transaktioner:

[bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0](https://Mempool.space/Address/bc1qqtmeu0eyvem9a85l3sghuhral8tk0ar7m4a0a0)


### Likheten mellan skript och Wallet-fingeravtryck

Utöver återanvändning av Address finns det många andra heuristiska metoder som kan koppla åtgärder till samma Wallet eller till ett kluster av adresser.


För det första kan en analytiker använda likheter i skriptanvändning. Till exempel kan vissa minoritetsskript som Multisig lättare upptäckas än SegWit V0-skript. Ju större grupp vi gömmer oss i, desto svårare är det att upptäcka oss. Det är bland annat därför som alla deltagare i CoinJoin Whirlpool-protokollet använder exakt samma typ av skript.


I ett vidare perspektiv kan en analytiker också fokusera på de karakteristiska fingeravtrycken hos en Wallet. Dessa är specifika processer för en användning som man kan försöka identifiera för att utnyttja dem som spårningsheuristik. Med andra ord, om man observerar en ackumulering av samma interna egenskaper i transaktioner som tillskrivs den spårade enheten, kan man försöka identifiera samma egenskaper i andra transaktioner.


Till exempel kan det identifieras att den spårade användaren systematiskt skickar sina ändringar till P2TR*-adresser (bc1p...). Om denna process upprepas kan den användas som en heuristik för att fortsätta vår analys. Andra fingeravtryck kan också användas, t.ex. ordningen på UTXO:erna, placeringen av ändringen i utgångarna, signaleringen av RBF (Replace-by-fee), eller till och med versionsnumret och låsningstiden.

Som [@LaurentMT](https://twitter.com/LaurentMT) anger i [Space Kek #19](https://podcasters.spotify.com/pod/show/decouvrebitcoin/episodes/SpaceKek-19---Analyse-de-chane--anonsets-et-entropie-e1vfuji) (en franskspråkig podcast) ökar användbarheten av Wallet-fingeravtryck i kedjeanalys avsevärt med tiden. Det växande antalet skripttyper och den alltmer gradvisa implementeringen av dessa nya funktioner av Wallet-programvaran accentuerar faktiskt skillnaderna. Det händer till och med att man exakt kan identifiera den programvara som används av den spårade enheten. Därför är det viktigt att förstå att studien av en Wallet:s fingeravtryck är särskilt relevant för nyligen genomförda transaktioner, mer än för dem som inleddes i början av 2010-talet.

Sammanfattningsvis kan ett fingeravtryck vara en specifik metod, som utförs automatiskt av Wallet eller manuellt av användaren, som kan hittas på andra transaktioner för att hjälpa till i vår analys.


### CIOH

CIOH, för "Common Input Ownership Heuristic", som kan översättas med "heuristik för gemensam Ownership för inputs" eller "samutnyttjandeheuristik", är en heuristik som säger att när en transaktion har flera inputs kommer dessa sannolikt alla från en enda enhet. Följaktligen är deras Ownership gemensam.


För att tillämpa CIOH observerar man först en transaktion som har flera inputs. Det kan röra sig om två ingångar eller trettio ingångar. När denna egenskap har upptäckts kontrollerar man om transaktionen inte passar in i ett känt mönster. Om den till exempel har 5 ingångar med ungefär samma belopp och 5 utgångar med exakt samma belopp, vet vi att det är strukturen hos en CoinJoin Whirlpool. Därför kan CIOH inte tillämpas.


Om transaktionen däremot inte passar in i något känt mönster av samarbetstransaktioner kan det tolkas som att alla indata sannolikt kommer från samma enhet. Detta kan vara mycket användbart för att utvidga ett redan känt kluster eller för fortsatt spårning.


![analysis](assets/en/11.webp)


CIOH upptäcktes av Satoshi Nakamoto. Han diskuterar det i del 10 av vitboken: "*[...] länken är oundviklig med transaktioner med flera inmatningar, som nödvändigtvis avslöjar att deras inmatningar ägdes av samma ägare. Risken är att om ägaren till en nyckel avslöjas, kan länkarna avslöja andra transaktioner som tillhörde samma ägare.*"

Det är särskilt fascinerande att notera att Satoshi Nakamoto, redan innan den officiella lanseringen av Bitcoin, hade identifierat de två största sårbarheterna för användarnas integritet, nämligen CIOH och Address återanvändning. En sådan framsynthet är anmärkningsvärd, eftersom dessa två heuristiker än idag är de mest användbara i kedjeanalyser.


### off-chain Data

Självklart är kedjeanalys inte begränsad till On-Chain-data. Alla data från en tidigare analys eller som finns tillgängliga på Internet kan också användas för att förfina en analys.


Om det t.ex. observeras att de spårade transaktionerna systematiskt sänds från samma Bitcoin-nod och dess IP Address kan identifieras, kan det vara möjligt att upptäcka andra transaktioner från samma enhet.


Analytikern har också möjlighet att förlita sig på analyser som tidigare gjorts i öppen källkod eller på sina egna tidigare analyser. Kanske kan man hitta en output som pekar på ett kluster av adresser som redan har identifierats. Ibland är det också möjligt att förlita sig på utdata som pekar på en Exchange, eftersom adresserna till dessa plattformar är allmänt kända.


På samma sätt kan man utföra en analys genom eliminering. Om till exempel en transaktion med två utgångar analyseras och en av dem kopplas till ett känt men distinkt kluster av adresser från den enhet som spåras, kan man tolka det som att den andra utgången sannolikt representerar förändringen.


I kedjeanalysen ingår även en del OSINT (Open Source Intelligence) som är lite mer generalistisk med internetsökningar. Det är därför som det avråds från att lägga ut mottagaradresser direkt på sociala medier eller på en webbplats, oavsett om det är under pseudonym eller inte.


### Temporala modeller

Man kanske inte tänker på det direkt, men vissa mänskliga beteenden är igenkännbara On-Chain. Det mest användbara i en studie är ditt sömnmönster! Ja, när du sover sänder du antagligen inte Bitcoin-transaktioner. Eftersom du i allmänhet sover ungefär samma tider är det vanligt att använda temporala analyser i On-Chain-analyser. Det handlar helt enkelt om att registrera de tidpunkter då en viss enhets transaktioner sänds till Bitcoin-nätverket. Genom att analysera dessa tidsmönster kan vi härleda många olika typer av information.

Först och främst kan en temporal analys ibland identifiera vilken typ av enhet som spåras. Om man observerar att transaktioner sänds konsekvent under 24 timmar kan detta tyda på en stark ekonomisk aktivitet. Enheten bakom dessa transaktioner är sannolikt ett företag, eventuellt internationellt, och kanske med automatiserade förfaranden internt.


Till exempel kände jag igen detta mönster för några veckor sedan när jag analyserade en transaktion som felaktigt hade tilldelat 19 bitcoins i avgifter. En enkel temporal analys hade gjort det möjligt för mig att anta att vi hade att göra med en automatiserad tjänst, och därför sannolikt en stor enhet som en Exchange: https://twitter.com/Loic_Pandul/status/1701127409712452072


Några dagar senare upptäcktes det att pengarna tillhörde PayPal, via Paxos Exchange.


Om man däremot ser att det tidsmässiga mönstret är ganska utspritt över 16 specifika timmar kan man anta att det rör sig om en enskild användare, eller kanske ett lokalt företag beroende på de volymer som utväxlas.


Utöver den observerade enhetens natur kan det temporala mönstret också ge oss en ungefärlig plats för användaren. Vi kan alltså korrelera andra transaktioner och använda Timestamp för dessa som en ytterligare heuristik som kan läggas till i vår analys.


På den Address som återanvänds flera gånger och som jag tidigare nämnde kan man till exempel se att transaktionerna, oavsett om de är inkommande eller utgående, är koncentrerade till ett 13-timmarsintervall.

![analysis](assets/notext/12.webp)

*Kredit: OXT*


Detta intervall motsvarar sannolikt Europa, Afrika eller Mellanöstern. Därför kan det tolkas som att användaren bakom dessa transaktioner bor där.


I ett annat register är det också en tidsanalys av den här typen som möjliggjorde hypotesen att Satoshi Nakamoto inte arbetade från Japan utan faktiskt från USA: [https://medium.com/@insearchofsatoshi/the-time-zones-of-Satoshi-nakamoto-aa40f035178f](https://medium.com/@insearchofsatoshi/the-time-zones-of-Satoshi-nakamoto-aa40f035178f)


### Analys av volymer

En annan extern heuristik som kan användas är analys av handelsvolymer. Baserat på de belopp som förekommer i varje transaktion som hänförs till en enhet kan denna information användas som en ytterligare heuristik för resten av analysen.

Denna heuristik är naturligtvis ganska svag, men den kan bidra till att minska osäkerheten när den läggs till andra heuristiker.


## Hur skyddar man sig mot kedjeanalys?

Som Bitcoin-användare har du rätt att skydda din integritet. Detta härrör från dina naturliga rättigheter att äga och förfoga över dig själv, som är inneboende för varje individ, oavsett lagstiftningsbegränsning.


Denna naturliga rätt att skydda sitt privatliv har också omvandlats till en anspråksrätt, som finns inskriven i artikel 12 i den allmänna förklaringen om de mänskliga rättigheterna, där det anges att "*Ingen får utsättas för godtyckligt ingripande i sitt privatliv, sin familj, sitt hem eller sin korrespondens eller för angrepp på sin heder och sitt anseende. Var och en har rätt till lagens skydd mot sådana ingripanden eller angrepp*."


Kärnverksamheten för företag som specialiserar sig på kedjeanalys består dock just i att tränga sig in i din privata sfär och därmed äventyra sekretessen i din korrespondens. Även om man skulle kunna hoppas att staterna, i enlighet med den ovannämnda anspråksrätten, kraftfullt skulle försvara vår integritet, underlåter de inte bara att göra det, utan de finansierar också i hög grad dessa analysföretag. Det skulle också vara fåfängt att hoppas på stöd från branschorganisationer, som verkar villiga att göra alla eftergifter inför lagstiftaren.


De facto existerar inte denna rätt till integritet på Bitcoin. Det är därför upp till dig, användaren, att hävda din naturliga rättighet och skydda sekretessen för din korrespondens. Detta innebär att anta olika tekniker och användningsmetoder som gör att du kan förhindra eller lura de heuristiker som används för kedjeanalys.


### Undvik att falla in i heuristiken

Först och främst, innan vi överväger mer radikala metoder, är det lämpligt att begränsa vår exponering för de heuristiker som används för kedjeanalys så mycket som möjligt. Som tidigare nämnts är de två mest kraftfulla heuristikerna Address återanvändning och CoinJoin.


Den grundläggande principen för att säkerställa din integritet på Bitcoin ligger i att använda en ny, ren Address för varje inkommande transaktion till din Wallet. Återanvändning av Address är verkligen det största hotet mot sekretessen på Bitcoin.

För en enskild användare är det mycket enkelt att generera en ny Address för varje inkommande betalning. Moderna plånböcker gör detta automatiskt så snart du klickar på "Ta emot". Så om du lägger minsta vikt vid integriteten i dina transaktioner är det absolut nödvändigt att använda nya adresser. Om du någonsin behöver en statisk kontaktpunkt på internet, istället för att sätta en mottagande Address, kan du använda lösningar [som PayNym som implementerar BIP47] (https://planb.network/tutorials/privacy/On-Chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093).

Om du vill motverka kedjeanalys ska du undvika att slå samman UTXO:er vid inmatningen av en transaktion. Om du verkligen behöver slå samman, föredra åtminstone UTXO:er som har samma källa. Denna rekommendation innebär att du har god hantering av dina UTXO:er. När du köper dina bitcoins, föredra överföringar som involverar stora belopp för att maximera antalet betalningar du kan göra utan att behöva slå samman. Jag råder dig också att märka dina UTXO:er i din programvara för att identifiera deras ursprung och undvika sammanslagningar från olika källor.


Mer allmänt gäller för alla andra heuristiker att man måste känna till dem för att försöka undvika att hamna i dem:


- Använd inte minoritetsskript. Föredrar SegWit V0 eller möjligen SegWit V1;
- Gör inte betalningar i runda tal. Om du till exempel behöver skicka 100 000 Sats till en vän, skicka dem 114 486 Sats. De kommer att bjuda dig på en drink i gengäld;
- Försök att inte alltid ha en förändring som är mycket större än betalningsutgången;
- Lägg inte ut dina mottagningsadresser på sociala medier;
- Använd din egen nod under Tor för att sända dina transaktioner;
- Försök att inte alltid sända dina Bitcoin-transaktioner samtidigt..


### Använda sekretessverktyg

Du kan också vända dig till metoder som gör din användning av Bitcoin tvetydig för att förhindra eller lura kedjeanalys.


Den mest populära tekniken är säkert CoinJoin, en samarbetsbaserad transaktionsstruktur som mobiliserar flera UTXO:er med samma belopp. Målet här är att bryta deterministiska länkar och därmed förhindra analyser från nutid till dåtid och från dåtid till nutid. CoinJoin möjliggör trovärdig förnekelse genom att gömma dina mynt i en stor grupp av oskiljbara mynt. Om du vill lära dig mer om CoinJoin, både tekniskt och praktiskt, föreslår jag att du läser dessa andra artiklar och handledningar:


- [CoinJoin - SAMOURAI Wallet](https://planb.network/tutorials/privacy/On-Chain/CoinJoin-samourai-Wallet-e566803d-ab3f-4d98-9136-5462009262ef);
- [CoinJoin - SPARROW Wallet](https://planb.network/tutorials/privacy/On-Chain/CoinJoin-sparrow-Wallet-84def86d-faf5-4589-807a-83be60720c8b);
- [Whirlpool STATS TOOLS - ANONSETS](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375).

![analysis](assets/en/13.webp)


CoinJoin är ett utmärkt verktyg för att skapa trovärdig förnekelse för mynt, men det är inte optimerat för alla användares integritetsbehov. CoinJoin var inte utformad för att bli ett betalningsverktyg. Det är mycket strikt när det gäller de belopp som utbyts för att göra produktionen av trovärdig förnekelse perfekt. Eftersom man inte fritt kan välja mängden transaktionsutgångar kan CoinJoin inte användas för att göra betalningar i bitcoins.


Föreställ dig till exempel att jag vill betala för min baguette i bitcoins samtidigt som jag optimerar min integritet. Eftersom det är omöjligt att välja beloppet för den resulterande UTXO från CoinJoin, skulle jag inte kunna anpassa beloppet för min utgift till det pris som bagaren har fastställt. Därför visar sig CoinJoin vara otillräcklig för betalningstransaktioner.


Andra verktyg har tagits fram för att tillgodose integritetsbehoven i mer specifika användningsfall. Vi har till exempel [PayJoin] (https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f), ett slags mini-CoinJoin, som bara involverar två deltagare och bygger på en struktur som möjliggör betalning.


Det unika med PayJoin ligger i dess förmåga att producera en transaktion som ser vanlig ut, men som i själva verket är en mini-CoinJoin mellan två användare. I denna struktur deltar mottagaren av transaktionen bland inmatningarna vid sidan av den faktiska avsändaren. Mottagaren lägger alltså in en betalning till sig själv i transaktionen som underlättar den faktiska betalningen.


Om du till exempel köper en baguette av din bagare för 6 000 Sats från ett UTXO på 10 000 Sats, och du vill göra ett PayJoin, kommer din bagare att lägga till ett UTXO på 15 000 Sats som tillhör dem som en input till din ursprungliga transaktion, som de kommer att återvinna helt som en output, för att lura heuristiken:


![analysis](assets/en/14.webp)


Transaktionsavgifter försummas för att förenkla förståelsen av systemet.


Målen med PayJoin är tvåfaldiga. För det första syftar den till att lura en extern observatör genom att skapa ett lockbete genom COH. När en analytiker observerar denna transaktion kommer denne att tro att han eller hon kan tillämpa COH och därmed anta att de olika ingångarna har en gemensam Ownership. I själva verket är detta antagande felaktigt, eftersom den ena inmatningen tillhör avsändaren, medan den andra ägs av mottagaren. Därför korrumperar PayJoin kedjeanalysen genom att leda analytikern in på fel väg.

Det andra målet med PayJoin är att lura analytikern om det faktiska transaktionsbeloppet, tack vare den specifika strukturen på dess utdata. PayJoin faller således inom området steganografi. Den gör det möjligt att dölja det verkliga transaktionsbeloppet i en vilseledande transaktion.


Om vi återgår till vårt exempel med att använda PayJoin för att köpa en baguette kan en extern observatör tro att vi har att göra med en betalning på 4 000 Sats eller 21 000 Sats. I själva verket är betalningen för baguetten 6 000 Sats: 21 000 - 15 000 = 6 000. Betalningens verkliga värde är därför dolt i en falsk betalning som fungerar som ett lockbete för kedjeanalysen.


Utöver PayJoin och CoinJoin finns det många andra Bitcoin-transaktionsstrukturer som antingen blockerar kedjeanalys eller lurar den. Bland dessa kan jag nämna transaktionerna [Stonewall] (https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4) och [StonewallX2] (https://planb.network/tutorials/privacy/On-Chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b), som gör det möjligt att antingen skapa en flexibel mini CoinJoin eller att imitera en flexibel mini CoinJoin. Det finns också [Ricochet](https://planb.network/tutorials/privacy/On-Chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589) transaktioner som simulerar en förändring av Ownership av bitcoins genom att göra en mängd falska överföringar till sig själv.


Alla dessa verktyg finns tillgängliga på Samourai Wallet på mobil och Sparrow Wallet på PC. Om du vill lära dig mer om dessa specifika transaktionsstrukturer rekommenderar jag att du upptäcker mina självstudier:


- [PayJoin](https://planb.network/tutorials/privacy/On-Chain/PayJoin-848b6a23-deb2-4c5f-a27e-93e2f842140f);
- [PayJoin - SAMOURAI Wallet](https://planb.network/tutorials/privacy/On-Chain/PayJoin-samourai-Wallet-48a5c711-ee3d-44db-b812-c55913080eab);
- [PayJoin - SPARROW Wallet](https://planb.network/tutorials/privacy/On-Chain/PayJoin-sparrow-Wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62);
- [STONEWALL](https://planb.network/tutorials/privacy/On-Chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4);
- [STONEWALL X2](https://planb.network/tutorials/privacy/On-Chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b);
- [RICOCHET] (https://planb.network/tutorials/privacy/On-Chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589).


## Slutsats

Kedjeanalys är en metod som innebär att man försöker spåra flödet av bitcoins On-Chain. För att göra detta letar analytiker efter mönster och egenskaper för att kunna dra mer eller mindre rimliga hypoteser och tolkningar.


Noggrannheten i dessa heuristiker varierar: vissa ger en högre grad av säkerhet än andra, men ingen kan göra anspråk på att vara ofelbar. Ackumuleringen av flera konvergerande heuristiker kan dock mildra detta inneboende tvivel, även om det fortfarande är omöjligt att helt eliminera det.

Vi kan kategorisera dessa metoder i tre olika huvudkategorier:


- Patterns, med fokus på den övergripande strukturen i varje transaktion;
- Intern heuristik, som gör det möjligt att göra en uttömmande granskning av alla detaljer i en transaktion utan att ta hänsyn till dess sammanhang;
- Extern heuristik, som omfattar analys av transaktionen i dess omgivning, samt all extern data som kan ge insikt.


Som Bitcoin-användare är det viktigt att behärska de grundläggande principerna för kedjeanalys för att effektivt motverka den och därmed skydda din integritet.


## Teknisk mini-ordlista:

**P2PKH:** akronym för Pay to Public Key Hash. Det är en standardskriptmodell som används för att fastställa utgiftsvillkor på en UTXO. Det gör det möjligt att låsa bitcoins på en Hash av en offentlig nyckel, det vill säga på en mottagande Address. Detta skript är associerat med Legacy-standarden och introducerades i de första versionerna av Bitcoin av Satoshi Nakamoto. Till skillnad från P2PK, där den publika nyckeln uttryckligen ingår i skriptet, använder P2PKH ett kryptografiskt avtryck av den publika nyckeln, med vissa metadata, även kallat en "mottagande Address". Detta skript innehåller RIPEMD160 Hash av SHA256 för den publika nyckeln och föreskriver att mottagaren, för att få tillgång till medlen, måste tillhandahålla en publik nyckel som matchar denna Hash, samt en giltig digital signatur som genererats från den tillhörande privata nyckeln. P2PKH-adresser kodas med Base58Check-formatet, vilket ger dem motståndskraft mot typografiska fel genom användning av en kontrollsumma. Dessa adresser börjar alltid med siffran 1.

**P2TR:** akronym för Pay to Taproot ("betala till roten"). Det är en standardskriptmodell som används för att fastställa utgiftsvillkor för en UTXO. P2TR introducerades i samband med implementeringen av Taproot i november 2021. Den använder Schnorr-protokollet för att aggregera kryptografiska nycklar, samt Merkle-träd för alternativa skript, känt som MAST (Merkelized Alternative Script Tree). Till skillnad från traditionella transaktioner där utgiftsvillkoren är offentligt exponerade (ibland vid mottagandet, ibland vid utgifterna), gör P2TR det möjligt att dölja komplexa skript bakom en enda uppenbar offentlig nyckel. Tekniskt sett låser ett P2TR-skript bitcoins på en unik Schnorr-offentlig nyckel, betecknad som K. Denna K-nyckel är dock i själva verket ett aggregat av en offentlig nyckel P och en offentlig nyckel M, där den senare beräknas från Merkle Root av en lista med ScriptPubKeys. Nyckelaggregeringen utförs med hjälp av Schnorr-signaturprotokollet. Bitcoins som är låsta med ett P2TR-skript kan användas på två olika sätt: antingen genom att publicera en signatur för den publika nyckeln P, eller genom att uppfylla ett av skripten i Merkle Tree. Det första alternativet kallas "nyckelväg" och det andra "skriptväg" P2TR gör det alltså möjligt för användare att skicka bitcoins antingen till en publik nyckel eller till flera skript som de själva väljer. En annan fördel med detta skript är att även om det finns flera sätt att spendera en P2TR-utgång, behöver endast den som används avslöjas vid utgifterna, vilket gör att de oanvända alternativen kan förbli privata. Tack vare Schnorrs nyckelaggregering kan till exempel den publika nyckeln P i sig vara en aggregerad nyckel, som potentiellt kan representera en Multisig. P2TR är en version 1 SegWit-utgång, vilket innebär att signaturer för P2TR-ingångar lagras i vittnet för en transaktion, och inte i ScriptSig. P2TR-adresser använder Bech32m-kodning och börjar med bc1p.

**P2WPKH:** Akronym för Pay to Witness Public Key Hash. Det är en standardskriptmodell som används för att fastställa utgiftsvillkor för en UTXO. P2WPKH introducerades i samband med implementeringen av SegWit i augusti 2017. Detta skript liknar P2PKH (Pay to Public Key Hash) genom att det också låser bitcoins baserat på Hash för en offentlig nyckel, det vill säga en mottagande Address. Skillnaden ligger i hur signaturer och skript inkluderas i transaktionen. I fallet med P2WPKH flyttas informationen om signaturskript (ScriptSig) från den traditionella transaktionsstrukturen till ett separat avsnitt som kallas Witness. Denna flytt är en del av uppdateringen SegWit (Segregated Witness). Denna teknik har fördelen att den minskar storleken på transaktionsdata i huvuddelen, samtidigt som den nödvändiga skriptinformationen för validering behålls i ett separat avsnitt. Följaktligen är P2WPKH-transaktioner i allmänhet mindre kostsamma i fråga om avgifter jämfört med Legacy-transaktioner. P2WPKH-adresser skrivs med Bech32-kodning, vilket bidrar till en mer kortfattad och mindre felbenägen skrivning tack vare BCH-kontrollsumman. Dessa adresser börjar alltid med bc1q, vilket gör dem lätta att skilja från Legacy-mottagningsadresser. P2WPKH är en version 0 SegWit-utgång.


**UTXO:** Akronym för outnyttjad transaktionsutgång. En UTXO är en transaktionsutgång som ännu inte har spenderats eller använts som input för en ny transaktion. UTXO:er representerar den del av bitcoins som en användare äger och som för närvarande är tillgängliga för att spenderas. Varje UTXO är associerad med ett specifikt utdataskript, som definierar de nödvändiga villkoren för att spendera bitcoins. Transaktioner i Bitcoin förbrukar dessa UTXO:er som input och skapar nya UTXO:er som output. UTXO-modellen är grundläggande för Bitcoin, eftersom den gör det möjligt att enkelt verifiera att transaktioner inte försöker spendera bitcoins som inte finns eller redan har spenderats. I grund och botten är en UTXO en del av Bitcoin.