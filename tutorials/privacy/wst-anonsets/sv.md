---
name: Whirlpool Statistikverktyg - Anonsets
description: Förstå begreppet anonset och hur man beräknar det med WST
---
![cover](assets/cover.webp)


*** VARNING:** Efter arresteringen av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april är Whirlpool Stats Tool inte längre tillgängligt för nedladdning, eftersom det var värd på Samourais Gitlab. Även om du tidigare hade laddat ner det här verktyget lokalt till din maskin, eller om det var installerat på din RoninDojo-nod, kommer WST inte att fungera just nu. Det förlitade sig på data som tillhandahölls av OXT.me för sin drift, och den här webbplatsen är inte längre tillgänglig. För närvarande är WST inte särskilt användbart eftersom Whirlpool-protokollet är inaktivt. Det är dock fortfarande möjligt att dessa programvaror kan komma att återinföras under de kommande veckorna. Dessutom är den teoretiska delen av denna artikel fortfarande relevant för att förstå principerna och målen för coinjoins i allmänhet (inte bara Whirlpool), samt för att förstå effektiviteten i Whirlpool-modellen. Du kan också lära dig hur du kvantifierar integriteten som tillhandahålls av CoinJoin-cykler.*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

> *Bryt länken som dina mynt lämnar efter sig*

I denna handledning kommer vi att studera begreppet anonsets, indikatorer som gör det möjligt för oss att uppskatta kvaliteten på en CoinJoin-process på Whirlpool. Vi kommer att gå igenom beräkningsmetoder och tolkning av dessa indikatorer. Efter den teoretiska delen går vi över till praktiken genom att lära oss att beräkna anonsets för en specifik transaktion med hjälp av Python-verktyget *Whirlpool Stats Tools* (WST).


## Vad är en CoinJoin på Bitcoin?

**CoinJoin är en teknik som bryter spårbarheten för bitcoins på Blockchain**. Den förlitar sig på en samarbetstransaktion med en specifik struktur med samma namn: CoinJoin-transaktionen.


CoinJoin-transaktioner förbättrar Bitcoin-användarnas integritet genom att komplicera kedjeanalysen för externa observatörer. Deras struktur gör det möjligt att slå samman flera mynt från olika användare till en enda transaktion, vilket döljer spåren och gör det svårt att fastställa länkarna mellan in- och utmatningsadresser.


CoinJoin-principen bygger på en samarbetsstrategi: flera användare som vill blanda sina bitcoins sätter in identiska belopp som input i samma transaktion. Dessa belopp omfördelas sedan i outputs av motsvarande värde. I slutet av transaktionen blir det omöjligt att associera en specifik output med en viss användare. Det finns ingen direkt länk mellan inmatningarna och utmatningarna, vilket bryter kopplingen mellan användarna och deras UTXO, liksom varje mynts historia.


![coinjoin](assets/notext/1.webp)


Exempel på en CoinJoin-transaktion:

[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://Mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)


För att genomföra en CoinJoin och samtidigt säkerställa att varje användare hela tiden har kontroll över sina medel börjar processen med att en koordinator skapar transaktionen, som sedan överförs till varje deltagare. Varje användare signerar sedan transaktionen efter att ha verifierat att den passar dem. Alla insamlade signaturer integreras slutligen i transaktionen. Om en användare eller koordinatorn försöker avleda medel genom att ändra utdata från CoinJoin-transaktionen kommer signaturerna att visa sig vara ogiltiga, vilket leder till att noderna avvisar transaktionen.


Det finns flera implementeringar av CoinJoin, till exempel Whirlpool, JoinMarket eller Wabisabi, som alla syftar till att hantera samordningen mellan deltagarna och öka effektiviteten i CoinJoin-transaktioner.

I den här handledningen kommer vi att fokusera på min favoritimplementering: Whirlpool, som är tillgänglig på Samourai Wallet och Sparrow Wallet. Enligt min mening är det den mest effektiva implementeringen för coinjoins på Bitcoin.


## Vad är nyttan med CoinJoin på Bitcoin?


Nyttan med CoinJoin ligger i dess förmåga att skapa trovärdig förnekelse genom att dränka ditt mynt i en grupp av oskiljaktiga mynt. Målet med denna åtgärd är att bryta spårbarhetslänkarna, både från det förflutna till nutiden och från nutiden till det förflutna.


Med andra ord bör en analytiker som känner till din initiala transaktion vid starten av CoinJoin-cyklerna inte med säkerhet kunna identifiera din UTXO vid slutet av remixcyklerna (analys från cykelstart till cykelavslut).


![coinjoin](assets/en/2.webp)


Omvänt bör en analytiker som känner till din UTXO vid utgången av CoinJoin-cyklerna inte kunna fastställa den ursprungliga transaktionen vid ingången av cyklerna (analys från cykelutgång till cykelingång).


![coinjoin](assets/en/3.webp)


För att bedöma svårigheten för en analytiker att koppla det förflutna till nutiden och vice versa är det nödvändigt att kvantifiera storleken på de grupper inom vilka ditt mynt är dolt. Detta mått anger hur många analyser som har samma sannolikhet. Om den korrekta analysen drunknar bland tre andra analyser med samma sannolikhet är din nivå av döljande således mycket låg. Om den korrekta analysen å andra sidan finns bland 20.000 analyser som alla är lika sannolika, är ditt mynt mycket väl dolt.


Och just storleken på dessa grupper representerar indikatorer som kallas "anonsets".


## Förståelse av anonsets

Anonsets fungerar som indikatorer för att utvärdera graden av integritet för en viss UTXO. Mer specifikt mäter de antalet oskiljaktiga UTXO:er inom den uppsättning som inkluderar det studerade myntet. Kravet på en homogen UTXO-uppsättning innebär att anonsets vanligtvis beräknas över CoinJoin-cykler. Användningen av dessa indikatorer är särskilt relevant för myntsammanslagningar Whirlpool på grund av deras enhetlighet.


Anonsets gör det möjligt att, där så är lämpligt, bedöma kvaliteten på coinjoins. En stor anonset-storlek innebär en ökad anonymitetsnivå, eftersom det blir svårt att urskilja en specifik UTXO inom uppsättningen.


Det finns två typer av anonsets:


- Den potentiella anonymitetsuppsättningen;**
- Den retrospektiva anonymitetsuppsättningen.**

Den första indikatorn visar storleken på den grupp bland vilken den studerade UTXO är dold i slutet av cykeln, med kännedom om UTXO vid ingången, det vill säga antalet oskiljaktiga mynt som finns i denna grupp. Denna indikator gör det möjligt att mäta motståndet hos myntets konfidentialitet mot en analys från förflutet till nutid (inträde till utgång). På engelska heter denna indikator "*forward anonset*", eller "*forward-looking metrics*".

![coinjoin](assets/en/4.webp)


Det här måttet uppskattar i vilken utsträckning din UTXO är skyddad mot försök att rekonstruera dess historia från dess ingångspunkt till dess utgångspunkt i CoinJoin-processen.


Om t.ex. din transaktion deltog i sin första CoinJoin-cykel och två andra nedåtgående cykler fullbordades, skulle den förväntade anonsettiden för ditt mynt vara "13":


![coinjoin](assets/en/5.webp)


Den andra indikatorn visar antalet möjliga källor för ett visst mynt, med kännedom om UTXO i slutet av cykeln. Denna indikator mäter motståndet hos myntets konfidentialitet mot en analys från nutid till förflutet (exit to entry), det vill säga hur svårt det är för en analytiker att spåra tillbaka till ursprunget till ditt mynt, innan CoinJoin cyklerna. På engelska är namnet på denna indikator "*backward anonset*", eller "*backward-looking metrics*".


![coinjoin](assets/en/6.webp)


Genom att känna till din UTXO vid utgången av cyklerna bestämmer den retrospektiva anonset antalet potentiella Tx0-transaktioner som kunde ha utgjort ditt inträde i CoinJoin-cyklerna. I diagrammet nedan motsvarar detta summan av alla de orange bubblorna.


![coinjoin](assets/en/7.webp)


## Beräkning av anonsets med Whirlpool Stats Tools (WST)

För att beräkna dessa indikatorer på dina egna mynt som har gått igenom CoinJoin-cykler kan du använda ett verktyg som är speciellt utvecklat av Samourai Wallet: *Whirlpool Statistikverktyg*.


Om du har en RoninDojo är WST förinstallerat på din nod. Du kan därför hoppa över installationsstegen och direkt följa användningsstegen. För dig som inte har en RoninDojo-nod, låt oss se hur du går vidare med installationen av detta verktyg på en dator.


Du kommer att behöva: Tor Browser (eller Tor), Python 3.4.4 eller högre, git och pip. Öppna en terminal. För att kontrollera förekomsten och versionen av dessa programvaror på ditt system anger du följande kommandon:

```plaintext
python --version
git --version
pip --version
```


Om det behövs kan du ladda ner dem från deras respektive webbplatser:


- https://www.python.org/downloads/ (pip levereras direkt med Python sedan version 3.4);
- https://www.torproject.org/download/;
- https://git-scm.com/downloads.

När alla dessa program är installerade, klonar du WST-arkivet från en terminal:

```plaintext
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```


![WST](assets/notext/8.webp)


Navigera till WST-katalogen:

```plaintext
cd whirlpool_stats
```


Installera beroendena:

```plaintext
pip3 install -r ./requirements.txt
```


![WST](assets/notext/9.webp)


Du kan också installera dem manuellt (valfritt):

```plaintext
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```


Navigera till undermappen `/whirlpool_stats`:

```plaintext
cd whirlpool_stats
```


Starta WST:

```plaintext
python3 wst.py
```


![WST](assets/notext/10.webp)


Starta Tor eller Tor Browser i bakgrunden.


**-> För RoninDojo-användare kan du återuppta handledningen direkt här.**


Ställ in proxyn till Tor (RoninDojo),

```plaintext
socks5 127.0.0.1:9050
```


eller till Tor Browser beroende på vad du använder:

```plaintext
socks5 127.0.0.1:9150
```


Denna manipulation gör att du kan ladda ner data på OXT via Tor, för att inte läcka information om dina transaktioner. Om du är nybörjare och det här steget verkar komplicerat, vet att det helt enkelt handlar om att rikta din internettrafik genom Tor. Den enklaste metoden består av att starta Tor Browser i bakgrunden på din dator och sedan bara utföra det andra kommandot för att ansluta via den här webbläsaren (`socks5 127.0.0.1:9150`).


![WST](assets/notext/11.webp)


Navigera sedan till den arbetskatalog från vilken du avser att hämta WST-data med kommandot `workdir`. I den här mappen lagras de transaktionsdata som du hämtar från OXT i form av .csv-filer. Denna information är viktig för att beräkna de indikatorer som du vill få fram. Du kan fritt välja plats för denna katalog. Det kan vara klokt att skapa en mapp speciellt för WST-data. Som ett exempel, låt oss välja nedladdningsmappen. Om du använder RoninDojo är det här steget inte nödvändigt:

```plaintext
workdir path/to/your/directory
```


Kommandotolken bör då ha ändrats så att den visar din arbetskatalog.


![WST](assets/notext/12.webp)


Hämta sedan data från den pool som innehåller din transaktion. Om jag till exempel är i poolen `100,000 Sats`, är kommandot:

```plaintext
download 0001
```


![WST](assets/notext/13.webp)


Denomineringskoderna på WST är följande:


- Pool 0,5 bitcoins: `05`
- Pool 0,05 bitcoins: `005``
- Pool 0,01 bitcoins: `001`
- Pool 0,001 bitcoins: `0001`

När data har laddats ner laddar du dem. Om jag till exempel är i poolen med `100 000 Sats`, är kommandot:

```plaintext
load 0001
```


Detta steg tar några minuter beroende på vilken dator du har. Nu är det en bra tid att göra dig en kaffe! :)


![WST](assets/notext/14.webp)


När du har laddat data skriver du kommandot `score` följt av din txid (transaktionsidentifierare) för att få dess anonsets:

```plaintext
score TXID
```


**Valet av txid som ska användas varierar beroende på vilken anonset man vill beräkna. För att bedöma ett mynts prospektiva anonset måste man, via kommandot "score", ange det txid som motsvarar dess första CoinJoin, vilket är den initiala mixning som utförts med denna UTXO. För att fastställa den retrospektiva anonset måste du å andra sidan ange txid för den senast utförda CoinJoin. Sammanfattningsvis beräknas den prospektiva anonset från txid för den första mixen, medan den retrospektiva anonset beräknas från txid för den sista mixen.


WST visar sedan den retrospektiva poängen (*Backward-looking metrics*) och den prospektiva poängen (*Forward-looking metrics*). Jag tog till exempel txid på ett slumpmässigt mynt på Whirlpool som inte tillhör mig.


![WST](assets/notext/15.webp)


Transaktionen i fråga: [7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://Mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)


Om vi betraktar denna transaktion som den första CoinJoin som utfördes för det berörda myntet, så har det en framtida anonset på 86 871 euro. Detta innebär att det är gömt bland 86 871 oskiljaktiga mynt. För en extern observatör som känner till detta mynt i början av CoinJoin-cyklerna och försöker spåra dess produktion, kommer de att ställas inför `86 871` möjliga UTXO:er, var och en med en identisk sannolikhet att vara det eftertraktade myntet.


Om vi betraktar denna transaktion som myntets sista CoinJoin har den en retrospektiv anonset på 42 185 euro. Detta innebär att det finns 42 185` potentiella källor för denna UTXO. Om en extern observatör identifierar detta mynt i slutet av cyklerna och försöker spåra dess ursprung, kommer denne att ställas inför 42 185 möjliga källor, alla med lika stor sannolikhet att vara det sökta ursprunget.

Förutom anonset-poängen ger WST dig också spridningshastigheten för din produktion inom poolen baserat på anonset. Denna andra indikator gör det helt enkelt möjligt för dig att bedöma potentialen för förbättring av ditt verk. Denna siffra är särskilt användbar för den blivande anonset. Om ditt verk har en spridningsgrad på 15 % betyder det att det kan förväxlas med 15 % av verken i poolen. Det är bra, men du har fortfarande en mycket stor marginal för förbättringar genom att fortsätta att remixa. Om ditt verk å andra sidan har en spridningsgrad på 95 % börjar du närma dig poolens gränser. Du kan fortsätta att remixa, men din anonset kommer inte att öka mycket.


Det är viktigt att notera att de anonsets som beräknas av WST inte är helt exakta. Med tanke på den enorma mängd data som ska bearbetas använder WST algoritmen *HyperLogLogPlusPlus* för att avsevärt minska den börda som är förknippad med lokal databehandling och det minne som krävs. Detta är en algoritm som gör det möjligt att uppskatta antalet distinkta värden i mycket stora datauppsättningar samtidigt som resultatet bibehåller hög noggrannhet. Därför är de angivna poängen tillräckligt bra för att användas i dina analyser, eftersom de är mycket verklighetsnära uppskattningar, men de bör inte tolkas som exakta värden för enheten.


Sammanfattningsvis, kom ihåg att det inte är absolut nödvändigt att systematiskt beräkna anonsets för var och en av dina bitar i coinjoins. Själva utformningen av Whirlpool ger redan garantier. Faktum är att den retrospektiva anonset sällan är ett problem. Från din första mix får du en särskilt hög retrospektiv poäng tack vare arvet från tidigare mixar sedan Genesis CoinJoin. När det gäller den prospektiva anonset räcker det att hålla din bit på post-mix-kontot under en tillräckligt lång period.


Det är därför jag anser att användningen av Whirlpool är särskilt relevant i en * HODL -> Mix -> Spend -> Replace*-strategi. Enligt min mening är det mest logiska tillvägagångssättet att hålla huvuddelen av sina Bitcoin-besparingar i en Cold Wallet, samtidigt som man kontinuerligt håller ett visst antal bitar i coinjoins på Samourai för att täcka dagliga utgifter. När bitcoins från coinjoins har använts ersätts de med nya för att återgå till det definierade tröskelvärdet av blandade bitar. Denna metod gör att man kan frigöra sig från oron för våra UTXO anonsets, samtidigt som den tid som krävs för effektiviteten av coinjoins blir mycket mindre begränsande.


**Externa resurser:**



- [Podcast på franska on chain-analys] (https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [Wikipedia-artikel om HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog)
- Samourais förvaringsplats för Whirlpool-statistik
- Whirlpool webbplats av Samourai
- [Medium artikel på engelska om integritet och Bitcoin av Samourai](https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [Medium-artikel på engelska om anonymitetsbegreppet av Samourai] (https://medium.com/samourai-Wallet/diving-head-first-into-Whirlpool-anonymity-sets-4156a54b0bc7)