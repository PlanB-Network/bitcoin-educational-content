---
name: Remix - Whirlpool
description: Hur många remixer ska göras på Whirlpool?
---
![cover remix- wp](assets/cover.webp)


*** VARNING:** Efter arresteringen av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april är Whirlpool Stats Tool inte längre tillgängligt för nedladdning, eftersom det var värd på Samourais Gitlab. Även om du tidigare hade laddat ner det här verktyget lokalt till din maskin, eller om det var installerat på din RoninDojo-nod, kommer WST inte att fungera just nu. Det förlitade sig på data som tillhandahölls av OXT.me för sin drift, och den här webbplatsen är inte längre tillgänglig. För närvarande är WST inte särskilt användbart eftersom Whirlpool-protokollet är inaktivt. Det är dock fortfarande möjligt att dessa programvaror kan komma att återinföras under de kommande veckorna. Dessutom är den teoretiska delen av denna artikel fortfarande relevant för att förstå principerna och målen för coinjoins i allmänhet (inte bara Whirlpool), samt för att förstå effektiviteten i Whirlpool-modellen. Du kan också lära dig hur du kvantifierar integriteten som tillhandahålls av CoinJoin-cykler.*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

> *Bryt länken som dina mynt lämnar efter sig*

Det här är en fråga som jag ofta får. **När man gör coinjoins med Whirlpool, hur många remixer ska man göra för att uppnå tillfredsställande resultat?


Syftet med CoinJoin är att erbjuda en trovärdig förnekelse genom att blanda ditt mynt med en grupp mynt som inte går att skilja från varandra. Målet med denna åtgärd är att bryta spårbarhetslänkarna, både från det förflutna till nutid och från nutid till det förflutna. Med andra ord bör en analytiker som känner till din initiala transaktion vid ingången av CoinJoin-cyklerna inte definitivt kunna identifiera din UTXO vid utgången av remixcyklerna (analys från ingångscykler till utgångscykler).

![past-present links diagram](assets/en/1.webp)


Omvänt bör en analytiker som känner till din UTXO vid utgången av CoinJoin-cyklerna inte kunna fastställa den ursprungliga transaktionen vid ingången av cyklerna (analys från utgångscykler till ingångscykler).

![present-past links diagram](assets/en/2.webp)

Antalet remixer är dock inte ett tillförlitligt kriterium för att bedöma hur svårt det är för en analytiker att upprätta kopplingar mellan det förflutna och nutiden, eller vice versa. En mer relevant indikator skulle vara storleken på de grupper där ditt mynt gömmer sig. Dessa indikatorer kallas för "anonsets". När det gäller Whirlpool finns det två typer av anonsets.


För det första kan vi bestämma storleken på den grupp där din UTXO är gömd vid utgången av CoinJoin-cyklerna, dvs. antalet oskiljaktiga mynt som finns i denna grupp.

![probable UTXOs at exit](assets/en/3.webp)

Denna indikator, som kallas "prospective anonset" på franska, "forward anonset" på engelska eller "framåtblickande metrik", gör det möjligt för oss att bedöma ditt mynts motståndskraft mot analyser som spårar dess väg från inträdet till utgången av CoinJoin-cyklerna. Detta mått uppskattar i vilken utsträckning din UTXO är skyddad mot försök att rekonstruera dess historia från dess ingångspunkt till dess utgångspunkt i CoinJoin-processen. Till exempel, om din transaktion deltog i sin första CoinJoin-cykel och ytterligare två nedströmscykler utfördes, skulle den prospektiva anonset för ditt mynt vara `13`:

![forward anonset](assets/en/4.webp)

För det andra kan en annan indikator beräknas för att utvärdera motståndet hos din pjäs mot en analys från nutid till dåtid. Genom att känna till din UTXO i slutet av cyklerna, bestämmer denna indikator antalet potentiella Tx0-transaktioner som kunde ha utgjort din input i CoinJoin-cyklerna (analys från slutet till början av cyklerna). Denna indikator mäter hur svårt det är för en analytiker att spåra ursprunget till ditt mynt efter att det har gått igenom coinjoins.![Troliga källor vid inmatning](assets/en/5.webp)

Namnet på denna indikator är "backward anonset" eller "backward-looking metrics". På franska vill jag kalla det "anonset rétrospectif". I diagrammet nedan motsvarar detta alla de orangea Tx0-bubblorna:

![backward anonset](assets/en/6.webp)

För att lära dig mer om beräkningsmetoden för dessa indikatorer rekommenderar jag att du läser [min Twitter-tråd] (https://twitter.com/Loic_Pandul/status/1550850558147395585?s=20) om detta ämne. Vi förbereder också en mer omfattande artikel om PlanB Network.


Jag är medveten om att det givna svaret kan verka otillfredsställande eftersom du hoppades på ett specifikt antal remixer, och jag hänvisar dig till dokumentation. Anledningen till detta är att antalet remixer är en opålitlig indikator för att utvärdera den anonymitet som uppnåtts i CoinJoin-cykler. Därför är det inte möjligt att definiera ett fast antal remixer som en absolut och universell säkerhetströskel.


Det är sant att varje ytterligare remix av ditt stycke ökar dess anonymitetsuppsättningar. Det är dock viktigt att förstå att det främst är de remixer som utförs av dina kollegor som bidrar till ökningen av din potentiella anonset. Med Whirlpool-modellen kan din transaktion uppnå betydande nivåer av prospektiv anonset med bara två eller tre CoinJoin-cykler, enbart genom aktiviteten hos peers som är involverade i tidigare coinjoins.


Den retrospektiva anonset är å andra sidan inte ett problem i vårt fall. Faktum är att du från din första CoinJoin drar nytta av ett arv från tidigare pooltransaktioner, vilket omedelbart ger ditt verk en hög bakåtriktad anonset, med en marginell ökning i varje efterföljande cykel.

Det är också viktigt att förstå att skapandet av en trovärdig förnekelse aldrig är fullständigt. Det är beroende av sannolikheten för att spåra ditt mynt. Denna sannolikhet minskar i takt med att storleken på de grupper som döljer myntet ökar. Därför bör du justera dina mål när det gäller anonsets efter dina personliga förväntningar. Fråga dig själv vilka skäl som får dig att använda coinjoins och vilka nivåer av anonymitet som krävs för att uppnå dessa mål. Till exempel, om användningen av coinjoins helt enkelt syftar till att bevara integriteten för din Wallet när du skickar några Sats till ditt gudbarn på deras födelsedag, är mycket höga nivåer av anonymitet inte nödvändiga. Ditt gudbarn kan förmodligen inte utföra en djupgående kedjeanalys, och även om de skulle göra det skulle återverkningarna på ditt liv inte vara katastrofala. Men om du är måltavla för en auktoritär regim där minsta lilla information kan leda till fängelsestraff, måste dina handlingar vägledas av mycket striktare kriterier.


För att fastställa dessa berömda anonset-indikatorer kan du använda ett Python-verktyg som heter **WST** (Whirlpool Stats Tool).


Det är dock inte alltid nödvändigt att beräkna anonsets för vart och ett av dina coinjoined-mynt. Själva utformningen av Whirlpool ger dig redan garantier. Som tidigare nämnts är retrospektiv anonset sällan ett bekymmer. Från din ursprungliga mix erhåller du redan en särskilt hög retrospektiv poäng. När det gäller prospektiv anonset behöver du bara hålla ditt mynt på post-mix-kontot under en tillräckligt lång tidsperiod. Här är till exempel anonset-poängen för ett av mina 100 000 Sats-mynt efter att ha tillbringat två månader i CoinJoin-poolen:

![WST anonsets](assets/en/7.webp)

Det visar ett retrospektivt resultat på 34 593 och ett prospektivt resultat på 45 202. I konkreta termer betyder detta två saker:


- Om en analytiker känner till mitt mynt i slutet av cyklerna och försöker spåra dess ursprung, kommer de att stöta på "34 593" potentiella källor, var och en med lika stor sannolikhet att vara mitt.
- Om en analytiker känner till mitt mynt i början av cyklerna och försöker bestämma dess korrespondens i slutet, kommer de att ställas inför "45 202" möjliga UTXO, var och en med samma sannolikhet att vara mitt.

Det är därför jag anser att användningen av Whirlpool är särskilt relevant i en `HODL -> Mix -> Spend -> Replace`-strategi. Enligt min mening är det mest logiska tillvägagångssättet att hålla majoriteten av sina besparingar i bitcoins i en Cold Wallet, samtidigt som man ständigt håller ett visst antal mynt i CoinJoin på Samourai för att täcka dagliga utgifter. När bitcoins från coinjoins har använts ersätts de med nya för att återgå till det definierade tröskelvärdet för blandade mynt. Denna metod gör att vi kan frigöra oss från oron för anonsets av våra UTXO, samtidigt som den tid som krävs för att coinjoins ska vara effektiva blir mycket mindre restriktiv.


Jag hoppas att detta svar har kastat lite ljus över Whirlpool-modellen. Om du vill lära dig mer om hur coinjoins fungerar på Bitcoin rekommenderar jag att du läser min omfattande artikel om detta ämne:


https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2

**Externa resurser:**


- Samourai Wallet Whirlpool
- https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://estudiobitcoin.com/como-instalar-y-utilizar-Whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/
- https://medium.com/samourai-Wallet/diving-head-first-into-Whirlpool-anonymity-sets-4156a54b0bc7.