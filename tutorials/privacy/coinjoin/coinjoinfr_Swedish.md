# Förstå och använda CoinJoin på Bitcoin.

## Introduktion

Ett av de ursprungliga problemen med alla peer-to-peer-betalningssystem är dubbelutgiften. Hur undviker man att illvilliga aktörer utnyttjar betalningsnätverket genom att spendera samma enheter flera gånger utan att behöva använda en central myndighet?

Satoshi Nakamoto löste detta problem med sin Bitcoin-protokoll, ett peer-to-peer-elektroniskt betalningsnätverk som fungerar utan inblandning av någon central myndighet. I sitt White Paper förklarar han att det enda sättet att bekräfta frånvaron av en transaktion, och därmed verifiera att det inte finns något försök till dubbelutgift, är att vara medveten om alla transaktioner som utförs på det distribuerade betalningsnätverket.

För att varje användare ska vara medveten om transaktionerna måste dessa annonseras offentligt. Det peer-to-peer-betalningssystem som föreslås av Bitcoin-protokollet har därför gjorts möjligt genom en helt transparent och distribuerad infrastruktur. Således kan vem som helst med en nod verifiera kedjan av elektroniska signaturer och historiken för varje mynt, från dess skapelse av en gruvarbetare.

> Denna princip om registerdistribution och offentlig annonsering av nya transaktioner används i den senaste kryptovalutan (bitcoin), men den användes redan i tidigare kryptovalutor som b-money, uppfunnen av Wei Dai 1998.
>
> Denna transparens och distribution innebär att varje användare av Bitcoin-nätverket kan spåra och observera transaktionerna från alla andra användare. Sekretess är därför omöjligt på betalningsnivån. Istället sker det på identifieringsnivån för personen.

Istället för att associera varje enhet med en identitet (namn, efternamn...), som i det traditionella banksystemet, är bitcoins associerade med ett par nycklar. Användarna representeras därför anonymt av en kryptografisk identifierare.

Förlusten av sekretess på Bitcoin sker när en observatör kan koppla vissa UTXO till vissa användare. När denna koppling görs mellan en användare och deras enheter blir det möjligt att följa deras betalningar och analysera historiken för deras bitcoins.

CoinJoin är en praxis som bryter detta UTXO-historik för att ge en viss nivå av sekretess till Bitcoin-användaren.
I den här artikeln kommer vi att undersöka vad CoinJoin är, hur det fungerar och hur man använder det på rätt sätt. Vi kommer främst att prata om Whirlpool, enligt mig den mest effektiva implementationen av CoinJoin idag, men vi kommer också att ta upp andra befintliga implementationer. Jag kommer också att prata om indikatorer som gör det möjligt att noggrant beräkna sekretessenivån för dina bitcoins. För att inte bara stanna vid teorin kommer jag konkret att visa hur man gör en CoinJoin-transaktion på olika sätt. Slutligen kommer vi att undersöka bästa praxis för att inte förlora den uppnådda sekretessen efter en serie CoinJoin, och jag kommer att presentera de olika verktygen i Samourai Wallet-plånboken som gör detta möjligt.
Om du gillar den här artikeln, dela den på sociala medier och med personer du känner som kan ha nytta av den.

> Innehållsförteckning:
>
> - CoinJoin och bitcoin-mixning.
> - Olika CoinJoin-implementeringar.
> - Teoretisk funktion av Whirlpool.
> - Guide: Whirlpool på Sparrow Wallet.
> - Guide: Whirlpool CLI på Dojo och Whirlpool GUI.
> - Bästa praxis efter mixning.
> - Utgiftsverktyg.
> - Är det fel att mixa bitcoins?

Om du är en ny användare av Bitcoin rekommenderar jag starkt att du förstår strukturen hos en Bitcoin-transaktion (UTXO, inputs och outputs) genom att läsa den här korta artikeln om ämnet: Mekanismen för en Bitcoin-transaktion: UTXO, inputs och outputs.

_Användning av CoinJoin kan indirekt innebära risker för användaren. Vissa tjänsteleverantörer kan potentiellt blockera dina medel och/eller ditt konto som ett resultat av dina handlingar och begära att du motiverar ursprunget till dessa medel. Informationen i den här artikeln utgör inte råd om system och programvara eller någon uppmaning att genomföra CoinJoin. Att genomföra en CoinJoin innebär att använda en internetansluten mjukvaruplånbok (så kallad "varm plånbok"). Det är möjligt att dina medel går förlorade och/eller blir stulna. Jag rekommenderar att du gör din egen forskning om de olika risker som finns. Den här artikeln kan på inget sätt utgöra en enda informationskälla om dessa ämnen._

## CoinJoin och bitcoin-mixning.

Innan vi börjar är det viktigt att förstå skillnaden mellan CoinJoin och mixning.

Mixning (på engelska: "mixing", "blender" eller "tumbler") är en teknik som används för att blanda UTXO, det vill säga blanda bitcoins, för att bryta deras historik och förvirra spårningen. Syftet med denna typ av operation är att pseudonymisera UTXO så att användaren får ökad sekretess. Pseudonymisering sker när UTXO befinner sig i en grupp av flera andra oåtskiljbara UTXO.
Både mixning och CoinJoin är ursprungligen två tekniker med samma mål, men de fungerar inte på samma sätt. Mixning bygger på en betrodd tredje part som vi kommer att anförtro våra bitcoins att mixa, medan CoinJoin endast förlitar sig på en koordinator som kommer att synkronisera användarnas åtgärder, men som aldrig kommer att ha kontroll över medlen.
Med införandet av CoinJoin blev mixning snabbt föråldrat och användarna vände sig bort från det. Det finns fortfarande några mixningstjänster som ChipMixer. Men idag finns denna teknik bara vid sidan av, medan CoinJoin används av allt fler individer.

Som ett resultat använder många bitcoinanvändare ordet "mixning" för att i slutändan prata om en CoinJoin. Även om denna semantik ursprungligen är felaktig, är den allmänt accepterad bland användarna. Man talar då om "mixade bitcoins" för att hänvisa till UTXO som kommer ut från en CoinJoin-transaktion.

CoinJoin är således en teknik som gör det möjligt att bryta UTXO: s historik. Den bygger på en samarbetsinriktad transaktion med samma namn: CoinJoin-transaktionen. Denna typ av transaktion föreslogs ursprungligen av Gregory Maxwell 2013 på Bitcoin Talk-forumet: https://bitcointalk.org/index.php?topic=279249.0

Den allmänna funktionen är följande: olika användare som vill mixa deponerar en summa som input i en transaktion. Dessa inputs kommer att komma ut som olika outputs med samma belopp (eventuellt med växel, men vi kommer att undersöka detta senare). Vid utgången av transaktionen är det därför omöjligt att avgöra vilken output som tillhör vilken användare. Det finns tekniskt sett ingen koppling mellan ingångarna och utgångarna av CoinJoin-transaktionen. Kopplingen mellan varje användare och varje UTXO bryts, på samma sätt som historiken för varje mynt.

För att möjliggöra CoinJoin utan att någon användare någonsin förlorar kontrollen över sina medel, konstrueras transaktionen först av koordinatorn och skickas sedan till varje användare. Var och en av dem signerar sedan transaktionen på sin sida genom att kontrollera att den passar dem, och alla signaturer läggs till transaktionen. Om en användare eller koordinator försöker stjäla andras medel genom att ändra CoinJoin-transaktionens outputs kommer signaturerna att vara ogiltiga och transaktionen kommer att avvisas av noderna.

Om jag får använda en analogi kan vi tänka oss CoinJoin som en biljakt mellan en helikopter och en bil. Tänk dig en helikopter som försöker följa en vit bil. Helikoptern representerar personen som vill analysera dina betalningar och den vita bilen representerar din UTXO. Helikoptern kan enkelt följa bilen genom att flyga över den.
Låt oss föreställa oss att det nu finns fyra andra liknande vita fordon som kör på denna väg i närheten av bilen som följs. Helikoptern kan fortfarande följa den vita bilen som den ursprungligen följde.
Nu, låt oss föreställa oss att dessa fem bilar tar en tunnel som förhindrar helikoptern från att se bilarna under en kort stund. Vid tunnelns utgång kommer helikoptern inte att kunna veta vilken av de fem vita bilarna som motsvarar den bil den ursprungligen följde. I detta exempel fungerar tunneln som en CoinJoin. Din UTXO efter CoinJoin-transaktionen kommer att vara gömd bland en grupp andra UTXO. En eventuell observatör kommer att veta att din UTXO finns i denna grupp, men kommer inte att kunna avgöra med säkerhet vilken som är din.

Det tekniska målet för CoinJoin-användaren är att ha så stora "Anonymity Sets" som möjligt på sina UTXO. Detta begrepp är mycket viktigt att förstå för fortsättningen. "Anonymity Sets", ibland också kallat "Anon Sets", hänvisar till parametrarna som används för att beräkna anonymitetsnivån för en given UTXO. Det finns två av dem: framtida poäng och retrospektiva poäng.

Framtida poäng ger storleken på gruppen UTXO där vår UTXO gömmer sig. Till exempel, om jag gör en CoinJoin med fyra andra användare, kommer min framtida poäng att vara fem direkt efter CoinJoin-transaktionen.

Om vi återvänder till vårt exempel med helikoptern har varje vit bil vid tunnelns utgång en framtida poäng på 5. Helikoptern vet att sitt mål finns bland denna grupp av fem bilar, men kan inte skilja ut vilken som är dess ursprungliga målbil.

Jag förklarar mer i detalj vad dessa två parametrar representerar i den här delen: Anon Sets. För tillfället, kom ihåg att ju högre Anon Sets är för en mixad UTXO, desto svårare blir det för en observatör att spåra den.

# Olika implementationer av CoinJoin.

En CoinJoin-transaktion kan mycket väl utföras manuellt, direkt med andra Bitcoin-användare som du träffar. Men denna lösning, förutom att vara mycket tidskrävande, är ganska ineffektiv. För att CoinJoin-transaktionen ska vara effektiv, snabb och kunna skala i nätverket, måste du kunna samarbeta med vilken annan användare som helst i världen. Istället använder vi tjänsterna från en koordinator vars roll är att utveckla en implementation med en transaktionsmodell, koppla samman olika användare och överföra informationen som möjliggör genomförandet av den samarbetsinriktade transaktionen.

Det finns huvudsakligen tre implementationer av CoinJoin på Bitcoin:

> JoinMarket.
>
> Wasabi.
>
> Whirlpool.
> Även om det slutliga målet för dessa tre implementationer är detsamma, nämligen att bryta historiken för en UTXO genom att genomföra CoinJoin-transaktioner, är deras funktionssätt mycket olika. Det är därför viktigt att lära sig om hur var och en fungerar för att välja den implementation som bäst motsvarar våra förväntningar.
> Ni har säkert förstått om ni följer mig på Twitter att jag personligen föredrar att använda Whirlpool-implementationen. Jag kommer därför att snabbt förklara den teoretiska funktionen hos de två andra lösningarna och detaljera varför jag anser att de är mindre lämpliga. Sedan kommer vi att studera Whirlpools funktionssätt mer i detalj, implementationen utvecklad av Samourai Wallet-teamet, som enligt mig är den bästa CoinJoin-lösningen för närvarande.

De nämnda egenskaperna för varje implementation gäller för närvarande. Det är möjligt att de har förändrats när du läser den här artikeln.

![Bildtext](assets/2.jpeg)

## JoinMarket.

JoinMarket skiljer sig tydligt från de andra huvudimplementationerna tack vare sitt användarnätverksmodell. Det är faktiskt baserat på en utbytesmarknad mellan användare som tillhandahåller likviditet för att blanda och användare som tar likviditet för att blanda.

När man vill genomföra en CoinJoin på JoinMarket måste man välja mellan att lämna sina bitcoins så att andra kan använda dem för att blanda mot betalning, eller att ta andras likviditet för att direkt blanda genom att betala den begärda ersättningen. Det finns alltså "makers" som lämnar sina bitcoins till förfogande och "takers" som använder likviditeten. "Takers" betalar "makers" för deras tjänst.

Det handlar alltså om en helt fri marknad utan användningsvillkor.

Den främsta nackdelen med denna tjänst är att den är ganska komplicerad att använda. Man måste ha viss kunskap om Linux-kommandoraden för att kunna använda den ordentligt. Denna implementation är relativt effektiv, men den är definitivt inte anpassad för allmänheten.

När det gäller funktionerna relaterade till CoinJoin-transaktionen har JoinMarket vissa svagheter jämfört med Whirlpool. Till exempel, på grund av strukturen för den använda CoinJoin-transaktionen kan det inte vara 0% deterministiska länkar mellan inputs och outputs. Det kan också noteras att JoinMarket inte inkluderar något verktyg för att förhindra en ny CoinJoin mellan mynt som redan har träffats tidigare.

När det gäller de kompletterande tjänsterna som erbjuds användaren inkluderar inte JoinMarket något verktyg för att enkelt beräkna Anon Sets för en UTXO. När det gäller verktyg för att spendera mixade UTXO erbjuder implementationen endast PayJoin.
Slutligen är JoinMarket en intressant implementation av CoinJoin, men den är inte avsedd för alla. Om du är bekväm med kommandoradsgränssnitt, om du har god förståelse för hur CoinJoin fungerar och om du gillar "takers" / "makers"-modellen, kan denna implementation passa dig.

## Wasabi 2.0.

Wasabis CoinJoin-tjänst fungerar i teorin som Whirlpools. Till skillnad från JoinMarket, där organisationen sker på en fri marknad, fungerar Wasabi som en koordinator som automatiskt blandar bitcoins från alla användare av tjänsten.

Själva strukturen för CoinJoin-transaktionen skiljer sig dock mycket från Whirlpools. Som vi kommer att se i nästa avsnitt, ökar den framtida anonymiteten (Anon Set) för de mixade UTXO:erna på Whirlpool genom att ackumulera flera CoinJoin med få användare varje gång. Å andra sidan sker Anon Sets för de mixade UTXO:erna på Wasabi genom få transaktioner med många användare.

Exempel på en CoinJoin som eventuellt utförts på Wasabi 1.0:
https://kycp.org/#/b994a9cbdc20e971207bde4f800b9ce99dba35478a2a997bc48e7f9f80bd2d02

Exempel på en CoinJoin utförd på Whirlpool: https://kycp.org/#/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2

De två implementationerna skiljer sig också åt när det gäller hanteringen av växel. På Whirlpool separeras och isoleras växeln från UTXO:erna innan CoinJoin genomförs med hjälp av TX0 (jag kommer att prata mer om det i nästa avsnitt). På Wasabi är växeln en output från CoinJoin-transaktionen. Valet av denna CoinJoin-struktur på Wasabi innebär att det finns deterministiska länkar mellan inputs och vissa outputs.

I version 2.0 har Wasabi helt ändrat sin CoinJoin-avgiftspolicy. Koordinatoravgifterna är nu 0,3% för UTXO:er över 0,01 bitcoin, och de är gratis för UTXO:er under den summan. Små UTXO:er får också gratis remixes. Observera att även om koordinatoravgifterna är gratis måste användaren fortfarande betala gruvavgifter för alla transaktioner, inklusive remix-transaktioner.
Således, till skillnad från Whirlpool, desto mer du vill ha betydande Anon Sets på dina mixade UTXO med Wasabi, desto mer kommer du att behöva betala i avgifter. Detta gäller både för version 1.0 och version 2.0 av Wasabi. Även om den senare versionen erbjuder koordinatoravgifter till små UTXO, finns det fortfarande gruvavgifter. Dessutom fick jag intrycket när jag använde version 2.0 att den maximala möjliga framtida poängen som kan uppnås är 300 på Wasabi. På Whirlpool kan man lätt nå en framtida poäng med fem siffror på bara några månader, och denna poäng är inte begränsad.
Utöver själva CoinJoin-strukturen, enligt min åsikt, saknar Wasabi allvarligt kompletterande verktyg för CoinJoin, särskilt för att kunna spendera mixade UTXO på ett rent sätt. I version 1.0 finns det inget verktyg för utgifter. I version 2.0 har Wasabi ändå inkluderat ett verktyg för utgifter av mixade UTXO som automatiskt justerar in- och utgångar för att maximera sekretessen genom att ta bort växel. Även om denna funktion kan vara användbar verkar den vara mycket mindre effektiv och praktisk att använda än det stora antalet verktyg som erbjuds på Samourai och Sparrow Wallet för att spendera mixade UTXO med Whirlpool. Jag kommer att prata om alla dessa verktyg längre fram i artikeln, i den här delen: Verktyg för utgifter.
Till skillnad från Whirlpool separerar inte Wasabi de mixade UTXO-kontona från de omixade UTXO-kontona och växelkontona. Denna plånboksstruktur gör det möjligt med adressåteranvändning mellan mixade UTXO och andra UTXO. Om detta inträffar kan det helt förstöra en CoinJoin.
Slutligen, efter att ha provat version 2.0, känner jag verkligen att jag inte har kontroll över min Coinjoin när jag använder Wasabi. Allt är förenklat och automatiserat, användargränssnittet är vackert, men är det vad vi förväntar oss av en CoinJoin-implementering?

## Whirlpools teoretiska funktionssätt.

Till skillnad från de andra nämnda implementeringarna utmärker sig Whirlpool genom att bygga "ZeroLink" CoinJoin-transaktioner, det vill säga transaktioner där det inte finns någon teknisk länk mellan alla inputs och outputs.
Detta är möjligt genom en CoinJoin-transaktion där varje användare sätter in samma belopp som input och får ut lika många outputs med samma belopp.
Med denna typ av restriktiv konstruktion av inputs är Whirlpools CoinJoin-transaktion den enda som tillåter användare att ha 0% deterministiska länkar mellan inputs och outputs. Det innebär att varje output har exakt samma sannolikhet att tillhöra en användare som alla andra outputs i transaktionen.
Antalet deltagare i varje mix är begränsat till 5: 2 ingångar och 3 remixare (vi kommer senare att upptäcka vad det innebär). Varje CoinJoin-transaktion på Whirlpool har alltid 5 ingångar och 5 utgångar.
![Schematisk representation av en Whirlpool CoinJoin-transaktion.](assets/3.jpeg)

## Whirlpools design.

Whirlpools modell är baserad på mycket små transaktioner. Till skillnad från Wasabi och JoinMarket erhålls inte styrkan hos Anon Sets genom antalet användare som deltar i CoinJoin, utan genom följd av flera små CoinJoin med 5 deltagare varje gång.

Användaren kommer att behöva betala en enda gång när de går med i en pool, och sedan kan de remixa så mycket de vill utan kostnad. Det är de nya deltagarna som betalar gruvavgifterna för remixarna.

Anon Sets kommer att öka exponentiellt med varje användares och deras mötande kamraters remixar. Målet är att dra maximal nytta av alla dessa gratis remixar som varje gång lägger till djup till UTXO: s Anon Sets.

Whirlpool har utformats med två huvudkriterier:

- Att implementeringen ska vara användbar på mobila enheter.

- Att remixcyklerna ska ske snabbt.

Det är av dessa två skäl som Samourai-teamen har valt att begränsa antalet användare till 5 per cykel. Ett lägre antal skulle inte ha möjliggjort tillräckligt effektiva CoinJoins och skulle ha minskat Anon Sets för mycket per cykel. Ett högre antal skulle förmodligen inte vara hanterbart på mobila klienter och skulle ha minskat flödet av cykler.

Slutligen behövs det inte ett stort antal deltagare per CoinJoin på Whirlpool eftersom Anon Sets skapas genom ackumulering av flera mixningscykler.

## Pooler och avgifter.

För att dessa flera cykler ska öka UTXO: s Anon Sets måste det finnas vissa ramar för att begränsa användningen av UTXO-belopp. Whirlpool definierar olika pooler.

En pool är en grupp användare som vill mixa och har kommit överens om beloppet för UTXO som används för att optimera CoinJoin-funktionen. Varje pool definierar en fast UTXO-belopp som användaren måste anpassa sig till för att kunna gå med. Konkret måste du välja en pool att gå med i när du vill göra CoinJoins. De olika befintliga poolerna på Whirlpool för närvarande är:

- 0,5 bitcoin.
- 0,05 bitcoin.
- 0,01 bitcoin.
- 0,001 bitcoin (= 100 000 sats).

Alla kan hitta en pool som passar dem.

Varje pool har en maximal beloppsgräns för att kunna gå med:

| Pool (bitcoin) | Maximalt belopp per ingång (bitcoin) |
| -------------- | ------------------------------------ | --- | ---- | --- |
| 0,5            | 35                                   |     | 0,05 | 3,5 |
| 0,01           | 0,7                                  |
| 0,001          | 0,025                                |

För att gå med i en pool måste du betala avgifter. Avgifterna är fasta för varje pool och är avsedda att ersätta teamen som utvecklar och hanterar Whirlpool för deras tjänster. Avgifterna tas endast ut en gång när du går med i poolen. När du väl är med i en pool kan du gratis blanda om så många gånger du vill.

För närvarande är följande avgifter tillämpade för varje pool:

| Pool (bitcoin) | Inträdesavgift (bitcoin) |
| -------------- | ------------------------ |
| 0,5            | 0,0175                   |
| 0,05           | 0,00175                  |
| 0,01           | 0,0005 (50 000 sats)     |
| 0,001          | 0,00005 (5 000 sats)     |

Du kan enkelt beräkna de avgifter som tas ut för dina blandningar med Whirlpool på denna webbplats: https://www.whirlpoolfees.com/

Observera också att dessa avgifter är "inträdesbiljetter" till poolen. Så oavsett om du går med i pool 0,01 med 0,01 btc eller med 0,5 btc, kommer avgifterna att vara exakt desamma. Innan du blandar måste en användare därför fundera på om de vill betala lägre avgifter med en mindre pool, i vilket fall de kommer att få flera små UTXO, eller om de föredrar att använda en större pool och betala högre avgifter, men få färre UTXO.

Det rekommenderas generellt att inte slå samman flera mixade UTXO vid utgången av olika mixningscykler. Detta kan bryta den tidigare hårt vunna sekretessen. Så ibland är det bättre att använda en större pool, även om det innebär högre avgifter, för att få färre UTXO av större storlek.

Andra avgifter att ta hänsyn till är naturligtvis gruvavgifterna för varje Bitcoin-transaktion. Som användare av Whirlpool måste du betala gruvavgifter för Tx0 och gruvavgifter för den första mixningen. Alla andra remixar kommer att vara gratis för dig eftersom Whirlpools avgiftsmodell är baserad på nya deltagare.

Varje CoinJoin består av 5 användare. Av dessa är 2 deltagare och 3 är remixar. Så de två deltagarna i varje mixning kommer att betala gruvavgifterna för alla 5 användare, och sedan kommer dessa två deltagare att kunna dra nytta av gratis remixar i sin tur.

![bildtext](assets/4.jpeg)
Genom denna avgiftsmodell skiljer sig Whirlpool verkligen från andra CoinJoin-tjänster eftersom Anon Sets för UTXO inte är proportionella mot användarens betalda pris. Det är därför möjligt att få mycket höga Anon Sets genom att bara betala poolavgifter och gruvavgifter för två transaktioner (Tx0 och initial mixning).
Självklart måste användaren också betala gruvavgifter när de vill ta ut sina UTXO från poolen efter att ha genomfört sina många remixar.

Som tidigare förklarat säger man att en UTXO är i en pool när den är tillgänglig för mixning. Det betyder inte att användaren förlorar sin äganderätt. Under hela CoinJoin-processen med Whirlpool behåller du full kontroll över dina nycklar och därmed dina bitcoins.

## Konton på Whirlpool.

För att kunna genomföra denna typ av CoinJoin-transaktion måste en plånbok som använder Whirlpool härleda flera konton.

Ett konto är en undersektion i en HD-plånbok. Denna uppdelning sker på nivå 3 i plånboken, det vill säga på xpub/xprv-nivån.

Om du inte är bekant med konceptet av konton inom en HD-plånbok rekommenderar jag att du läser min e-bok om detta ämne som du kan ladda ner gratis genom att klicka här. Jag har också skrivit en hel artikel om hur derivationsvägar fungerar: Förstå derivationsvägar för en Bitcoin-plånbok.

Du behöver självklart inte förstå allt detta för att använda Whirlpool, men kom ihåg att ett konto är en undersektion av en HD-plånbok som är helt separerad från andra konton och har sin egen xpub/zpub.

Det är tack vare denna strikta separation av olika konton som det är omöjligt att återanvända en adress mellan mixade bitcoins och icke-mixade bitcoins på Whirlpool.

På varje HD-plånbok är det möjligt att härleda upp till 2^(32/2) olika konton. Det första kontot, som du använder som standard på din plånbok utan att veta det, är kontot 0'.

När du använder en plånbok som är anpassad för användning med Whirlpool kommer den automatiskt att skapa 5 konton:

    Insättningskontot bestämt av index 0'.

    Bad Bank-kontot (doxxic change) bestämt av index 2 147 483 644'.

    Pre Mix-kontot bestämt av index 2 147 483 645'.

    Post Mix-kontot bestämt av index 2 147 483 646'.

    Ricochet-kontot bestämt av index 2 147 483 647': Detta sista konto används inte direkt inom Whirlpool-protokollet, men det är kopplat till det. Jag kommer att berätta mer om det nedan, i avsnittet om utgiftsverktyg.

Varje konto har sin egen användning och är avsett för en specifik uppgift.
Alla konton är beroende av samma seed. Användaren kan därför enkelt återfå åtkomst till alla sina medel om det uppstår problem med återställningsfrasen och eventuell lösenfras. Du måste dock ange de olika indexen för de använda kontona i återställningsprogramvaran.

Låt oss nu titta på de olika stegen i en CoinJoin Whirlpool inom dessa konton.

## Tx0.

I början av en CoinJoin kommer allt från Deposit-kontot. Detta är det konto du använder som standard när du skapar en ny Bitcoin-plånbok. Detta konto måste krediteras med de bitcoins som användaren vill blanda.

Tx0 är den första transaktionen i Whirlpool-blandningsprocessen. Dess syfte är att rengöra UTXO:erna som ska blandas innan de skickas till en första blandning. Denna transaktion kommer att dela upp ingångs-UTXO:n i flera UTXO som motsvarar poolens belopp. Alla dessa utjämnade UTXO kommer att skickas till Premix-kontot. Den återstående skillnaden som inte kan ingå i den valda poolen kommer att separeras på ett dedikerat konto: Bad Bank (eller "Doxxic Change").

Tx0 kommer också att användas för att betala avgifterna till koordinatorn.

Du måste betala gruvavgifter för Tx0.

![Diagram över en Tx0 CoinJoin Bitcoin!](assets/5.jpeg)

Kredit (modifierad bild): KYCP.org: https://kycp.org/#/a126e48d4a6eb8d19682ec0e23ad45e76cd52b45f6c17be5068ae051d4b2cc24

I detta exempel på en Tx0-transaktion kan vi se en inmatning på 2,2550 bitcoins från användarens insättningskonto som initierar Tx0. Denna inmatning delas upp i flera utgående UTXO som representerar:

- Koordinatorns avgifter, här: 0,0250 B.

- De fyra UTXO som är redo att blandas och som kommer att gå till användarens Premix-konto. Dessa UTXO registreras också hos koordinatorn.

- Skillnaden som inte kan ingå i poolen eftersom den är för liten: det är den giftiga växeln som kommer att gå till sitt dedikerade och isolerade konto.

Avgifterna här skiljer sig från de jag gav er i den tidigare tabellen eftersom Samourai har sänkt sina priser för Whirlpool i mars 2021.

## Doxxic Change-konto.

Växeln som inte kan ingå i poolen skickas till Doxxic Change-kontot (även kallat "Bad Bank") för att helt separera den från resten av kontona.

Denna UTXO är farlig för användarens integritet eftersom den inte bara är kopplad till dess förflutna och potentiellt till ägarens identitet, utan också är markerad som tillhörande en ägare som har gjort en CoinJoin.
Om denna UTXO slås samman med mixade UTXO kommer de senare att förlora all tidigare vunnen konfidentialitet. Om den slås samman med andra Doxxic Changes riskerar användaren att förlora konfidentialitet. Den bör därför hanteras med försiktighet. Jag kommer att förklara exakt hur man hanterar denna giftiga UTXO i denna del.

## Pre Mix-konto.

I Pre Mix-kontot hittar vi UTXO som har utjämnats under Tx0 och är redo att blandas. Dessa UTXO är något högre än poolens belopp eftersom de måste täcka avgifterna för deras initiala mixning.

När dessa UTXO har passerat sin initiala mixning kommer Pre Mix-kontot att vara tomt och nya UTXO kommer att finnas i nästa konto.

## Post Mix-konto.

Post Mix-kontot tar emot nyligen mixade UTXO från deras initiala mixning. Det tar också emot alla andra tillgängliga UTXO för remixar.

Om Whirlpool-klienten körs är UTXO i Post Mix-kontot tillgängliga för remixar. De kommer att slumpmässigt väljas ut för remixning.

När användaren vill spendera mixade UTXO kan denne göra det direkt från detta Post Mix-konto. Det rekommenderas också att lämna de mixade UTXO i detta konto, inte bara för att de ska remixas gratis, utan också för att de inte ska lämna Whirlpool-systemet, annars riskerar de att förlora konfidentialitet.

## Anon Sets.

Som tidigare förklarat är Anon Sets två parametrar som gör det möjligt att beräkna hur konfidentiell en UTXO är och därmed hur effektiv din CoinJoin-session är.

Den första parametern är den framtidsinriktade anonyma uppsättningen (på engelska: "Forward-looking Anon Set"). Även om denna term är felaktig kallas denna poäng ofta direkt "Anon Set" för att förkorta.

En UTXOs framtidsinriktade anonyma uppsättning representerar storleken på gruppen där den är dold vid en given tidpunkt.

För att ge dig en bild är den framtidsinriktade anonyma uppsättningen antalet nuvarande UTXO som kan matcha en given UTXO i det förflutna. Till exempel, låt oss säga att en aktör som övervakar Bitcoin-kedjan spårar en UTXO som tillhör dig innan den går in i CoinJoin-poolen. Efter att din mynt har passerat flera mixningar undrar observatören var den har gått. Han börjar då spåra de olika möjliga vägarna och tack vare CoinJoins natur kommer han att stöta på flera UTXO som potentiellt kan matcha din. Detta antal potentiella UTXO är din UTXOs framtidsinriktade anonyma uppsättning.

Så efter en första Whirlpool CoinJoin kommer en UTXO att ha en framtidsinriktad anonym uppsättning på 5. Det betyder att den kommer att vara dold i en sannolik grupp av 5 UTXO:er.
![Beräkningsschema för en Bitcoin UTXO:s framtida poäng](assets/6.jpeg)
Om någon övervakar min ingående UTXO kommer de inte att kunna veta vilken av dessa 5 utgående UTXO som tillhör mig.

Denna framtida poäng ökar i takt med användarens remixar, men även med remixar från de parter han har träffat under sina tidigare mixar. Låt oss ta vårt exempel med en UTXO som för närvarande har en framtida poäng på 5. Om denna UTXO som tillhör oss remixas, kommer dess poäng att öka till 9.

Det som är mycket intressant med Whirlpool är att även om min UTXO inte remixas, eftersom den tillhör en grupp där den inte kan särskiljas från de andra, kommer dess poäng att öka baserat på remixar från sina tidigare träffade parter.

Låt oss föreställa oss att vår UTXO har genomgått en första mix och har en poäng på 5. Om en UTXO som finns i samma mix går vidare till en ny remix, kommer min UTXO:s poäng att öka till 9, även om den inte har rört sig sedan den första mixen:

![Beräkningsschema för en Bitcoin UTXO:s framtida poäng](assets/7.jpeg)

Denna ökning av den framtida poängen är exponentiell eftersom om en UTXO som möts av UTXO:n jag mötte under min första mix remixas, ökar min Anon Set ännu mer:

![Beräkningsschema för en Bitcoin UTXO:s framtida poäng](assets/8.jpeg)

Denna exponentiella ökning är möjlig tack vare Whirlpools unika modell som bygger på många små efterföljande CoinJoin.

För att påminna, alla dessa remixar är gratis, så det är mycket klokt att låta sina UTXO:er mixas och remixas samtidigt som man drar nytta av remixar från de träffade parterna, så länge man inte behöver spendera dessa UTXO:er som tillhör oss.

![snygg video](assets/7-5.mp3)

Den andra Anon Set som kan bestämmas för en given UTXO för att beräkna dess sekretessnivå är den retrospektiva poängen (på engelska "Backward-looking Anon Set").

Denna retrospektiva poäng är på sätt och vis arvet som de tidigare parterna lämnar efter sig efter din första mix. Den indikerar antalet Tx0 som kan matcha din mixade UTXO.

Den gör det möjligt att bedöma sekretessnivån för en UTXO mot ett försök till spårning som är motsatt det första nämnda.

Kom ihåg att för den framtida poängen, denna parameter bedömer hur konfidentiell vi är vid ett försök till spårning från en ingående UTXO i CoinJoin-cykler till vår utgående UTXO. För den retrospektiva poängen bedömer parametern hur konfidentiell en ingående UTXO är genom att utgå från en utgående UTXO i en cykel. Det vill säga att vi går i motsatt riktning.
Till exempel, låt oss föreställa oss att en observatör av Bitcoin-kedjan känner till en UTXO och vill spåra var den kommer ifrån för att försöka bestämma dess ursprung. Han kommer då att se att denna UTXO har passerat genom CoinJoin och han kommer att stöta på många UTXO som kan potentiellt vara den sökta i ingången till CoinJoin. Detta antal potentiella UTXO är den retrospektiva poängen för den spårade UTXO:n.
För att beräkna denna retrospektiva poäng måste man först räkna från den målade UTXO:n alla UTXO i ingången som kommer från en Tx0. Sedan måste man analysera remix-UTXO:n i ingången till transaktionen och gå tillbaka till de tre tidigare CoinJoin-transaktionerna som de kommer ifrån. För var och en av dessa tre transaktioner utförs samma beräkning. Man fortsätter på samma sätt tills man når CoinJoin Genesis-transaktionen, det vill säga den första CoinJoin-transaktionen i poolen.

![Beräkningsschema för den retrospektiva poängen för en Bitcoin-UTXO](assets/9.jpeg)

I diagrammet ovan motsvarar beräkningen av den retrospektiva poängen för en av UTXO:na i utgången av CoinJoin längst upp att räkna antalet Tx0 (de blå bubblorna) som finns i de stigande CoinJoin-transaktionerna fram till den målade CoinJoin-transaktionen, fram till CoinJoin Genesis.

Till skillnad från den framtida poängen för en UTXO, som börjar på 5 efter dess initiala mixning och sedan ökar, kommer den retrospektiva poängen för en UTXO att vara omedelbart mycket hög när du har gjort din initiala mixning. Ju mer en UTXO har mixats nyligen, desto högre är dess retrospektiva poäng. Du drar nytta av arvet från tidigare mixar i den valda poolen.

## Whirlpool Stats Tool (WST).

För att enkelt beräkna Anon Sets för en av dina mixade UTXO på Whirlpool kan du använda Whirlpool Stats Tool (WST). Ett verktyg speciellt utformat för att beräkna dina Anon Sets på Whirlpool.

Om du är en användare av RoninDojo är verktyget förinstallerat på din nod. För att komma åt det från RoninCLI, gå till: `Samourai Toolkit > Whirlpool Stat Tool`.

Om du inte har en RoninDojo, här är hur du installerar WST-verktyget på en Linux-maskin:

Du kommer att behöva: Tor Browser (eller Tor), Python 3.4.4 eller senare, git och pip3.

För att kontrollera deras version, ange följande kommandon:

```bash
python --version
git --version
pip --version
```

Installera beroendena:

```bash
pip install PySocks
pip install requests[sock5]
pip install plotly
pip install datasketch
pip install numpy
```

Installera Whirlpool Stats Tool:

```bash
# Klona katalogen:
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git

# Gå till katalogen /whirlpool_stats:
cd whirlpool_stats
# Installera beroendena med pip:
pip3 install -r ./requirements.txt
```

Jag hade personligen några problem med den senaste versionen av WST. Om den inte fungerar för dig kan du också klona den tidigare versionen på github som fungerar perfekt: https://github.com/Samourai-Wallet/whirlpool_stats. De följande stegen kommer att vara desamma. Observera bara att poolen 100k sats inte fanns vid den tiden, så du måste lägga till den manuellt i koden om du använder den äldre versionen.

Skapa sedan en arbetskatalog för att lagra transaktionsdata och starta WST:

# Gå till önskad katalog, till exempel home:

```bash
cd ~

# Skapa en dedikerad katalog, till exempel med namnet "wst":
mkdir wst

# Gå till underkatalogen /whirlpool_stats:
cd whirlpool_stats/whirlpool_stats/

# Starta WST:
python3 wst.py
```

När WST är installerat och startat, här är hur du beräknar Anon Sets. Dessa steg är liknande oavsett om du är på en vanlig maskin eller på RoninDojo:

Ange följande kommando för att ställa in proxy på Tor (för RoninDojo måste det vara detta kommando):

```bash
socks5 127.0.0.1:9050
```

Om du använder Tor Browser måste den vara igång och kommandot blir:

```bash
socks5 127.0.0.1:9150
```

Gå sedan till arbetskatalogen som skapades i föregående steg med workdir-kommandot. Om du är på RoninDojo, hoppa över detta steg:

```bash
# Ersätt sökvägen i detta exempel med din egen sökväg.
workdir /home/psyduck/wst
```

![Starta WST kommandorader](assets/10.jpeg)

Ladda sedan ner data från poolen som innehåller din transaktion:

```bash
# Ersätt 0001 med den poolens beteckning som du är intresserad av.
download 0001
```

Följande är beteckningarna för poolerna på WST:

- Pool 0,5 bitcoins: 05
- Pool 0,05 bitcoins: 005
- Pool 0,01 bitcoins: 001
- Pool 0,001 bitcoins: 0001

När data har laddats ner, ladda in den med kommandot:

```bash
# Ersätt 0001 med den poolens beteckning som du är intresserad av.
load 0001
```

![Ladda ner WST-data från OXT kommandorader](assets/11.jpeg)

Efter att ha laddat in data, skriv in kommandot score följt av din TXID (transaktions-ID) för att få dess Anon Sets:

```bash
# Ersätt TXID med din transaktions-ID.
score TXID
```

![Resultatet av att beräkna Anon Sets för en UTXO med WST](assets/11.jpeg)
WST visar dig då den retrospektiva poängen (Backward-looking metrics) och den framtida poängen (Forward-looking metrics). Förutom poängen för Anon Sets ger WST dig också spridningsgraden för din output i poolen baserat på anon set.

Observera att den framtida poängen för din UTXO beräknas utifrån TXID för din initiala mixning, inte från din senaste mixning. Å andra sidan beräknas den retrospektiva poängen för en UTXO utifrån TXID för den senaste cykeln.

## Muuuh xpubs.

Det finns mycket desinformation om hur Whirlpool fungerar. Den vanligaste kritiken är förmodligen att Samourai skulle ha tillgång till användarnas xpubs på en server.

I själva verket fungerar Whirlpool-protokollet utan att behöva komma åt användarnas xpubs. Behovet av xpub finns på plånboksnivå, precis som alla andra program, och begränsas till en specifik användning:

- Om du använder Whirlpool på Samourai Wallet utan att använda din egen Dojo, då känner Samourais Dojo till din xpub.

- Om du använder Whirlpool på Samourai Wallet med din egen Dojo, läcker ingen xpub.

- Om du använder Whirlpool på Sparrow Wallet utan att använda din egen nod, ser den tredje noden du är ansluten till dina transaktioner.

- Om du använder Whirlpool på Sparrow Wallet med din egen nod, läcker ingenting på den fronten.

Precis som med alla andra Bitcoin-plånböcker måste du använda din egen nod. Annars förlorar du oberoende, sekretess och förtroende. Men i slutändan har det inget att göra med Whirlpool-protokollet. På den punkten agerar Samourai Wallet som alla andra befintliga plånböcker.

Nu när vi har sett teorin och den allmänna funktionen, låt oss prova på praktiken!

# Praktiskt avsnitt

## Guide: Whirlpool på Sparrow Wallet.

Det finns många alternativ för att använda Whirlpool. Det första jag vill presentera för dig är implementeringen av Sparrow Wallet, en öppen källkodsprogramvara för hantering av Bitcoin-plånböcker på datorn.

Denna metod har fördelen att den är ganska lätt att komma igång med, snabb att installera och kräver inget annat än en dator och en internetanslutning. Å andra sidan har denna metod en betydande nackdel som inte finns i den andra guiden som du hittar i nästa avsnitt:

- Mixningen sker endast när Sparrow är igång och ansluten. Det betyder att om du vill mixa och remixa dina bitcoins 24/7 måste du konstant ha din dator igång.

Den enda lösningen på detta problem är att använda din egen Dojo. Jag kommer att berätta mer om det i nästa avsnitt.
Om du aldrig har använt Whirlpool tidigare och vill göra det för tillfället mer för att förstå än för effektivitet, rekommenderar jag att du börjar lugnt med Sparrow för att förstå mekanismerna ordentligt.
Låt oss nu se hur du gör:

Först och främst behöver du självklart Sparrow-programvaran. Du kan ladda ner den direkt från Sparrow Wallets officiella webbplats eller från deras GitHub:

- https://sparrowwallet.com/download/

- https://github.com/sparrowwallet/sparrow/releases

Innan du installerar programvaran är det viktigt att kontrollera signaturen och integriteten hos den nedladdade körbara filen. Om du inte vet hur du gör detta, förklarar jag hur du gör det på Windows i den här artikeln: Hur du kontrollerar integriteten hos Bitcoin-programvara på Windows?

När programvaran är installerad måste du skapa en Bitcoin-plånbok. Observera att för att blanda måste du ha en mjukvaruplånbok (kallad "varm plånbok"). Du kan alltså inte blanda med en plånbok som är säkerställd av en hårdvaruplånbok.

Det är inte obligatoriskt, men om du planerar att blanda stora belopp rekommenderar jag starkt att du använder en stark lösenfras för denna plånbok. Om du inte vet hur du skapar en plånbok i Sparrow förklarar jag i detalj hur du gör det i den 5:e delen av följande artikel: Allt du behöver veta om Bitcoin-lösenfrasen.

När plånboken är skapad, skicka dina sats att blanda till den. Klicka bara på "Receive" och skicka dem till en adress som tillhör dig, precis som du skulle göra normalt.

Här kan du se att jag precis har skapat min plånbok och skickat lite mer än 199k sats till den:

![Mottagande av bitcoins på Sparrow Wallet](assets/12.JPEG)

För tillfället använder du ett vanligt konto. Detta konto indexeras som 0' och kommer att bli ditt insättningskonto för att blanda.

För att blanda denna UTXO som du precis har mottagit, gå till listan över UTXO för kontot genom att klicka på "UTXOs" till vänster i gränssnittet:

![Val av UTXO att blanda på Sparrow Wallet](assets/13.JPEG)

Välj sedan de olika UTXO:erna att blanda genom att klicka på dem. Om du vill välja flera, håll ner kontrolltangenten och klicka på var och en av dem. När UTXO:et är valt visas det med blå markering.

Klicka sedan på knappen "Mix Selected" längst ner i gränssnittet:

![Starta processen för att blanda bitcoins på Sparrow Wallet](assets/14.JPEG)

Ett fönster öppnas för att förklara hur Whirlpool fungerar. Detta är en förenkling av det jag förklarade i föregående del.

Klicka på "Next" efter att ha läst det.

![Introduktion till Whirlpools funktionssätt](assets/15.JPEG)
Vi förklarar också hur konton fungerar. Klicka på "Nästa" efter att ha läst.
![Introduktion till hur konton fungerar på Whirlpool](assets/16.JPEG)

På nästa sida kan du ange en SCODE om du har en. En SCODE är en rabattkod som kan användas för att minska avgifterna för poolinträde. Samourai Wallet tillhandahåller ibland dessa koder till sina användare vid speciella tillfällen (exempelvis vid jul). Kom ihåg att följa dem på Twitter för att inte missa kommande SCODES: https://twitter.com/SamouraiWallet

Välj sedan gruvavgifterna du vill tilldela Tx0 och initial mix. Detta kommer att påverka hastigheten med vilken din första mix bekräftas. Kom ihåg att du betalar gruvavgifter för din Tx0 och initiala mix, men du kommer inte att betala gruvavgifter för alla andra remixes.

När du har valt avgifterna, klicka på "Nästa".

![Inställning av gruvavgifter för Whirlpool](assets/17.JPEG)

På det här nya fönstret kan du välja vilken pool du vill gå med i genom att klicka på rullgardinsmenyn. Fönstret visar också de poolavgifter du kommer att betala och antalet UTXO som kommer att ingå i denna pool. Klicka sedan på "Förhandsgranska Premix".

I mitt exempel hade jag en UTXO på 199k sats, så jag kommer att gå med i poolen med bara en UTXO på 100k sats:

![Val av mixningspool](assets/18.JPEG)

Sparrow kommer sedan att be dig ange lösenordet för plånboken som du ställde in vid skapandet av den i programvaran.

![Bekräftelse av lösenord för Bitcoin-plånbok](assets/19.JPEG)

Och du kommer att komma till förhandsgranskningen av din Tx0.

Först kan du se att Sparrow har härlett de olika kontona som behövs för att använda Whirlpool. Du kan se dem till vänster på skärmen.

Du kan också se strukturen för din transaktion med de olika utgångarna:

- Poolavgifter (koordinator).

- UTXO för Premix.

- Doxxic Change.

![Kontroll av slutgiltig Tx0 innan sändning](assets/20.JPEG)

Om transaktionen är korrekt, klicka på knappen "Sänd transaktion" för att sända din Tx0. Annars kan du också ändra inställningarna för denna Tx0 genom att klicka på knappen "Rensa" och börja om konstruktionen av denna transaktion.

![Sändning av Tx0](assets/21.JPEG)

När Tx0 har sänts kan du hitta dina UTXO redo att mixas i Premix-kontot. Din UTXO är nu registrerad av koordinatorn och kommer att skickas till sin initiala mix.

![Tx0 har sänts och väntar på bekräftelse](assets/22.JPEG)
Här kan vi se att min UTXO från Tx0 har bekräftats en gång. Vi kan också se den initiala mixen som har byggts och spridits, men som väntar på bekräftelse:
![Bekräftad Tx0, spridd initial mix](assets/23.JPEG)

Om vi går till Postmix-kontot kan vi se att UTXO från den initiala mixen har spridits, men inte bekräftats ännu. När den väl är bekräftad kommer den automatiskt att vara tillgänglig för framtida remixar som inte kommer att debiteras.

I kolumnen "Mixes" kan du observera antalet remixar av dina olika UTXO. Kom ihåg att det inte är antalet remixar som är viktigt, utan Anon Sets, även om de två uppgifterna är delvis relaterade.

![Bekräftad initial mix, UTXO väntar på remixar](assets/24.JPEG)

Där har du det, din UTXO har blivit mixad. Den befinner sig för närvarande i poolen och väntar på remixar. Om du vill avsluta mixningen, klicka bara på knappen "Stop Mixing". Du kan starta den igen genom att klicka på knappen "Start Mixing".

Om du vill hålla din UTXO tillgänglig för remixning måste du hålla Sparrow Wallet-programvaran öppen och din dator påslagen (inte i viloläge).

Du kan eventuellt inaktivera viloläget i inställningarna för ditt operativsystem. Det finns också ett alternativ att välja i Sparrow-programvaran för att förhindra att din dator går i viloläge:

> Verktyg > Förhindra datorsömn

![Förhindra datorsömn](assets/25.JPEG)

Knappen "Mix to" på ditt Postmix-konto i UTXO-sektionen låter dig ställa in en automatisk sändning av din mixade UTXO till den plånbok du väljer. Du kan välja antalet remixar som ska göras innan sändningen till den plånboken.

Detta alternativ gör det möjligt för dig att till exempel automatiskt skicka din Postmix till din hårdvaruplånbok. Var dock försiktig, det är vanligtvis inte rekommenderat att använda detta alternativ. Jag förklarar varför i avsnittet: Bästa praxis för post-mix.

Här har jag presenterat en av alternativen för att mixa med Whirlpool, men det finns andra. Till exempel kan du direkt mixa från din smartphone med Samourai Wallet-appen på Android. Funktionen kommer att vara liknande som beskrivet i detta avsnitt.

![Samourai](assets/26.JPEG)

## Guide: Whirlpool CLI på Dojo och Whirlpool GUI.

Om du vill gå vidare kan du mixa med Whirlpool på din egen Dojo.

Dojo är en implementation av en Bitcoin-nod utvecklad av Samourai Wallet-teamen. Om du använder din egen Dojo för CoinJoin på Samourai kommer xpub för dina olika konton inte att skickas till tredjepartsservrar. Du kommer därför att öka din integritet genom att eliminera en av riskerna med Whirlpool.
Dessutom integrerar Dojo Whirlpool CLI, vilket gör att du kan köra remixar 24/7 utan att behöva ha din plånbok öppen på en annan enhet hela tiden.
Denna lösning kräver att du kör en Bitcoin-nod och är något mer komplex att sätta upp än det tidigare exemplet. Trots det ger det dig den bästa CoinJoin-upplevelsen på Whirlpool med så lite risk som möjligt.

För att köra din egen Dojo kan du antingen installera din egen Dojo-nod eller använda Dojo på en annan Bitcoin-nod. Följande är de som för närvarande tillåter detta:

- RoninDojo, som är en Dojo med extra verktyg och inkluderar en installationsguide och en administrationsguide. Jag förklarar i detalj hur du installerar och använder RoninDojo i den här artikeln: Installera och använda din Bitcoin-nod RoninDojo.

- Umbrel via "Samourai Server"-appen.

- MyNode med "Dojo"-appen.

- Nodl med "Dojo"-appen.

För vårt exempel kommer vi att använda tre olika gränssnitt:

- Samourai Wallet.

- Whirlpool GUI.

- Whirlpool CLI.

Whirlpool CLI kommer att köras på Dojo för att dra nytta av de tidigare nämnda fördelarna. Det är den som kommer att kommunicera med koordinatorn och hantera mixarna.

Whirlpool GUI är det grafiska gränssnittet som vi kommer att använda för att se vad som händer på Whirlpool CLI och för att initiera mixar på distans. GUI:en kommer att installeras på en annan dator än Dojo för enkel hantering.

Samourai Wallet kommer att vara vår plånbok för CoinJoin. Det är en gratis och öppen källkodsapplikation som du kan ladda ner till Android eller en emulator. Med denna applikation har du alltid kontroll över din mixningsplånbok och kan enkelt spendera dina postmix när du är på språng.

### Steg 1: Förbered din Dojo.

Det första steget är att ha en Dojo. Du måste hämta URL:en för anslutning till Dojo, som är en Tor-adress. Du kan också använda dess QR-kod. Denna adress kommer att användas för att ansluta din Samourai Wallet-plånbok till din nod via Dojo.

Om du använder Umbrel, gå till App Store i vänstermenyn och installera "Samourai Server". När appen har startats hittar du QR-koden för anslutning till Dojo.

Om du använder RoninDojo, gå till RoninUI i din webbläsare, logga in och klicka på "Manage" i blått längst ner i rutan "Dojo". Du kan få tillgång till Samourai Dojo QR-koden genom att klicka på "Display Values".

![Dojo-anslutningsadress](assets/27.JPEG)

### Steg 2: Förbered din plånbok.

För plånboken kommer vi att använda Samourai Wallet. Du kan ladda ner den från Google Play Store eller direkt med APK-filen från deras officiella webbplats.
Starta appen och anslut till din Dojo med hjälp av QR-koden från föregående steg. När du är ansluten, klicka på "Skapa en ny plånbok".

![Anslutning till Dojo från Samourai](assets/28.JPEG)

Samourai kommer sedan att be dig skapa en lösenfras. Om du inte vet vad en lösenfras är och hur du konfigurerar den korrekt, rekommenderar jag starkt att du läser min artikel om detta: Allt du behöver veta om Bitcoin-lösenfras.

Välj en stark lösenfras och gör en fysisk säkerhetskopia av den. Klicka på "Nästa" för att fortsätta.

![Skapa lösenfras för plånboken](assets/29.JPEG)

Därefter måste du välja en PIN-kod för att komma åt appen. Denna PIN-kod är mycket viktig, men den har ingen koppling till din Bitcoin-plånbok. Den är specifik för Samourai-appens funktion. Du kommer att behöva den för att komma åt din plånbok från Samourai-appen. Men om du behöver återställa din plånbok, kommer endast din lösenfras och återställningsfras (mnemonisk) att behövas. Välj en stark PIN-kod, gör en säkerhetskopia och klicka på "Nästa".

![Val av PIN-kod för Samourai-appen](assets/30.JPEG)

Du kommer att bli ombedd att bekräfta denna PIN-kod en andra gång. Sedan kommer du att kunna komma åt återställningsfrasen för din Samourai-plånbok. Precis som lösenfrasen måste denna information säkerhetskopieras på ett fysiskt och säkert medium, annars kan du permanent förlora åtkomsten till dina bitcoins om det uppstår problem. För att lära dig mer om återställningsfrasen rekommenderar jag att du läser den här artikeln: Vad är en Bitcoin-återställningsfras?

Efter att du har bekräftat kommer du att komma till din nya Samourai-plånbok. Innan du gör något, börja med att testa dina säkerhetskopior. Innan du gör det, hämta en xpub från din plånbok för att vara säker på att du är på rätt plats:

> Inställningar > Plånbok > Visa BIP44 XPUB

Du kommer att få en QR-kod med värdet av XPUB. Skriv bara ner de sista 8 tecknen av denna xpub på ett papper. Till exempel:

> X2GGWaLt

Detta kommer att se till att du är på rätt plånbok och att du inte har stavat fel på lösenfrasen.

Sedan kan du antingen radera den tomma plånboken eller installera om Samourai-appen och försöka återställa den med endast dina tidigare säkerhetskopior. För att göra detta, efter att du har anslutit till din Dojo, klicka på "Återställ en befintlig plånbok".
Ange återställningsfrasen och lösenfrasen som finns på dina fysiska säkerhetskopior, välj samma PIN-kod som tidigare och återställ sedan plånboken. Om det inte fungerar betyder det att säkerhetskopieringen av din återställningsfras inte är korrekt. Börja om från steg 2.

Om du lyckas komma åt plånboken, gå och kontrollera att den första XPUB BIP 44 fortfarande är densamma. Gå till:

> Inställningar > Plånbok > Visa BIP44 XPUB

Kontrollera att de sista 8 tecknen överensstämmer med de du tidigare har noterat på papperet. Om så inte är fallet betyder det att säkerhetskopieringen av din lösenfras inte är korrekt (eller så har du gjort ett stavfel). Börja om från steg 2.

Om din säkerhetskopiering fungerar korrekt kan du fortsätta till nästa steg.

> Observera att denna test av en ny plånbokssäkerhetskopiering också bör utföras på vilken annan plånbok som helst, inte bara på Samourai.

### Steg 3: Förbered Whirlpool GUI.

Nu ska vi installera Whirlpool GUI, den grafiska gränssnittet som låter dig hantera dina CoinJoin. Gå till din persondator.

Först måste du installera Java Development Kit (JDK). Du kan till exempel installera OpenJDK gratis från den här webbplatsen: https://adoptopenjdk.net/ Det är det som gör det möjligt att kompilera och köra programvara som är utvecklad i Java.

![Installation av OpenJDK](assets/31.JPEG)

När OpenJDK är installerat kan du installera Whirlpool GUI från Samourai Wallets officiella webbplats: https://samouraiwallet.com/download/whirlpool

Starta Whirlpool GUI. För att Whirlpool GUI ska kunna ansluta måste antingen Tor Daemon eller Tor Browser köras i bakgrunden på din dator. Du måste se till att starta dem innan varje användning av Whirlpool GUI på den här datorn. Om du inte har Tor installerat, installera det från den officiella webbplatsen innan du börjar: https://www.torproject.org/download/

![Val av anslutning för Whirlpool GUI](assets/32.JPEG)

I Whirlpool GUI, klicka på "Advanced: Remote CLI" för att ansluta din Whirlpool CLI till din Dojo. Du kommer att behöva Tor-adressen för din Whirlpool CLI.

- För att hitta den på Umbrel: starta bara Samourai Server-applikationen, du hittar den på sidan.

- För att hitta den på RoninDojo: gå till RoninCLI huvudmenyn och gå till Credentials > Whirlpool.

I Whirlpool GUI, ange den tidigare hittade Tor-adressen i fältet "CLI address". Lämna "http://" men ange inte ":8899". Klistra bara in den adress som har getts till dig.
På nästa ruta, ange 9050 om du använder Tor Daemon eller 9150 om du använder Tor-webbläsaren. Om det är första gången du ansluter till din Whirlpool CLI från en Whirlpool GUI kan du lämna API-nyckelfältet tomt. Annars, fyll i det.
![Anslutning av Whirlpool GUI till Dojo](assets/33.JPEG)

Klicka på "Connect"-knappen för att para ihop din Whirlpool GUI med din Whirlpool CLI. Var tålmodig, det kan ta några ögonblick att upprätta anslutningen.

Därefter kan du para ihop din Samourai-plånbok. Klicka på QR-kodssymbolen till höger på skärmen för att kunna skanna.

![Anslutning av Whirlpool GUI till Samourai-plånboken](assets/34.JPEG)

Från din Samourai-plånbok, gå till:

> ... > Inställningar > Transaktioner > Para ihop med Whirlpool GUI

Skanna QR-koden för din Samourai-plånbok på Whirlpool GUI.

![Para ihop Samourai-plånboken med Whirlpool GUI](assets/35.JPEG)

Kontrollera att anslutningen är etablerad på Whirlpool GUI. På nästa sida, aktivera "Använd Dojo som plånboksbackend". Klicka sedan på "Initialize GUI".

![Konfigurera Whirlpool GUI](assets/36.JPEG)

Därefter blir du ombedd att bekräfta lösenfrasen för din Samourai-plånbok. Klicka på "Sign in" när du är klar.

![Bekräftelse av plånbokens lösenfras](assets/37.JPEG)

Var tålmodig en stund. När konfigurationen är klar kommer du till Whirlpool GUI:

![Åtkomst till Whirlpool GUI-gränssnittet](assets/38.JPEG)

### Steg 4: Blanda!

Allt är klart, du är redo att blanda dina bitcoins. För att göra detta, skicka sats till att blanda till Deposit-kontot i din Samourai-plånbok. Du har också möjlighet att göra det direkt från Whirlpool GUI.

Klicka på "Deposit"-knappen för att generera en mottagningsadress.

![Generera en Bitcoin-mottagningsadress](assets/39.JPEG)

På denna sida kan du se minimibeloppen att sätta in för att gå med i en given pool. Se alltid till att sätta in något mer än detta belopp, annars kan dina UTXO inte gå med i den önskade poolen förrän gruvavgifterna sjunker.

Skicka dina bitcoins att blanda till den genererade adressen. Du kan generera en ny adress genom att klicka på "Renew address".

För extra säkerhet vid insättning, föredra att sätta in dina medel med Samourai Wallet. Klicka helt enkelt på den blå "+" längst ned till höger i appen, och sedan på "Ta emot".
När insättningen har bekräftats kan du se den i "Deposit" -kontot på Whirlpool GUI. För att starta Coinjoin-serien, välj UTXO:erna att skicka till mixen och klicka på "Premix" -knappen. Observera att om du väljer flera olika UTXO samtidigt kommer de att slås samman vid TX0. Detta kan leda till förlust av sekretess, särskilt om källorna till UTXO:erna är olika.
![Starta Tx0 mix](assets/40.JPEG)

Whirlpool-konfigurationssidan öppnas. Välj poolen du vill gå med i. Välj gruvavgifterna som tilldelas TX0 och initial CoinJoin. I botten av sidan visas växelvärdet och antalet och beloppet för utjämnade UTXO:er. Om konfigurationen passar dig, klicka på "Premix" -knappen för att starta CoinJoin-processen.

![Konfigurera Tx0 mix](assets/41.JPEG)

När TX0 har skapats kan du se dina utjämnade UTXO:er i "Premix" -kontot som väntar på bekräftelse. Om du vill att din Premix automatiskt ska mixas och att dina framtida postmix automatiskt remixas 24/7, aktivera alternativet "Automatically mix premix & postmix" från fliken "Configuration" till vänster om ditt fönster.

Du kan nu stänga Whirlpool GUI, dina UTXO:er är tillgängliga för CoinJoin 24/7 med din Whirlpool CLI på din Dojo.

Du kan övervaka dina UTXO:er från "Postmix" -kontot på Whirlpool GUI eller från Whirlpool-gränssnittet på Samourai Wallet. Klicka på den lilla vita Samourai-logotypen längst upp till vänster på skärmen. Whirlpool-konton skiljer sig tydligt på Samourai Wallet med en ljusblå färg:

![Observera CoinJoin-mixar från Samourai](assets/42.JPEG)

För att spendera dina postmix, klicka bara på + längst ned till höger på skärmen och välj en lämplig utgiftsverktyg.

För att enkelt följa dina automatiska mixar rekommenderar jag också att du konfigurerar en Watch-Only-plånbok med Android-appen Sentinel. Ange ZPUB för ditt PostMix-konto och följ utvecklingen av dina CoinJoin i realtid.

# Bästa praxis efter mixning.

Efter att ha mixat är det viktigt att följa några bästa praxis om du inte vill förlora all sekretess du har fått genom att mixa.

## Postmix UTXO:er.

Det bästa alternativet efter mixning är att låta dina UTXO:er vara i din PostMix-plånbok tills du behöver spendera dem. Du kan till och med låta dem remixas obegränsat tills du behöver använda dem för att köpa något.
Vissa användare föredrar att flytta sina mixade bitcoins till en säker hårdvaruplånbok. Du kan göra det, men var mycket försiktig och följ rekommendationerna från Samourai Wallet. Utan detta riskerar du att förlora all tidigare vunnen sekretess.

Det vanligaste felet är att slå samman UTXO. Det är viktigt att inte slå samman, det vill säga att använda mixade UTXO och icke-mixade UTXO som indata i samma transaktion. Detta innebär att du måste hantera dina UTXO i din plånbok och märka dem för att undvika att göra fel. Utöver CoinJoin är sammanslagning av UTXO generellt sett en dålig praxis som ofta leder till förlorad sekretess om den inte hanteras korrekt.

Du måste också vara försiktig med sammanslagningar mellan mixade UTXO. Det är möjligt att göra små sammanslagningar om dina mixade UTXO har stora Anon Sets, men detta kommer att minska sekretessnivån för dina bitcoins.

Var mycket försiktig så att sammanslagningen inte blir för stor eller att den inte sker efter för få remixar, annars kan det vara möjligt att koppla samman dina UTXO före CoinJoin och efter CoinJoin genom enkel deduktion. Om du inte har full kontroll över dessa begrepp är det säkraste att inte sammanslå UTXO efter mixningen och skicka dem en efter en till din hårdvaruplånbok med en ny tom adress varje gång. Kom ihåg att märka varje mottagen UTXO ordentligt.

Jag rekommenderar också att du inte flyttar dina post-mix till en plånbok som använder minoritetsskript. Till exempel, om du kommer in i Whirlpool från en multisig-plånbok som använder P2WSH-skript, är det osannolikt att du blandas med andra användare som har samma typ av plånbok från början. Om du sedan skickar dina post-mix tillbaka till samma multisig-plånbok kommer sekretessnivån för dina mixade bitcoins att minska kraftigt.

Det är också viktigt, som för alla andra Bitcoin-transaktioner, att inte återanvända mottagaradresser. Kom ihåg att mottagaradresser är engångsadresser. Varje ny inkommande transaktion kräver generering av en ny tom adress.

> 1 UTXO = 1 Adress

Det enklaste och säkraste är därför att låta dina mixade UTXO vara i sin PostMix-plånbok. Du kan låta dem remixas och bara röra dem när du vill göra dig av med dem, det vill säga när du vill spendera dem.

## Doxxic change UTXO.

Därefter är det viktigt att vara försiktig med hanteringen av "Doxxic Change", växling som inte kunde ingå i mixningspoolen. Dessa giftiga UTXO som skapas efter användning av Whirlpool är farliga för din integritet eftersom de skapar en koppling mellan dig och din användning av CoinJoin. Det är därför viktigt att inte använda dem till vad som helst och framför allt inte slå samman dem med någon annan UTXO. Här är vad du kan göra med dem:

- Blanda dem i mindre pooler: om din UTXO är tillräckligt stor för att ensam kunna ingå i en mindre pool, blanda den då. Det är förmodligen en av de bästa lösningarna. Å andra sidan bör du absolut inte slå samman flera doxxic change för att komma in i en pool. Det är en dålig idé som kommer att skapa en koppling mellan dina olika inmatningar i Whirlpool.

- Märk dem som "ej spenderbara" och låt dem vara på det dedikerade kontot: en annan bra lösning är helt enkelt att inte röra dem och märka dem som "ej spenderbara" för att vara säker på att inte använda dem. Om bitcoinpriset ökar kommer förmodligen nya mindre pooler att skapas, vilket gör att du kan blanda dina små doxxic change på rätt sätt.

- Donera dem: det är viktigt att göra små donationer, beroende på vad man har råd med, till olika utvecklare som arbetar med Bitcoin och relaterad programvara, samt till innehållsproducenter som hjälper oss att förstå användningen av denna programvara. Du kan också välja att donera till olika organisationer som accepterar betalningar i bitcoin. Om ditt doxxic change är en börda för dig, donera det.

- Använda dem för att köpa presentkort: vissa webbplatser tillåter dig att köpa presentkort med bitcoin för att kunna handla hos olika kända återförsäljare. Du kan bli av med ditt doxxic change genom att köpa den här typen av presentkort.

Det finns säkert andra tekniker för att bli av med en doxxic change. Vissa talar om att anonymisera dem med hjälp av Lightning Network, medan andra använder en swap med Monero. Dessa tekniker kan vara bra, men jag tar inte upp dem i den här artikeln eftersom jag inte behärskar dem. Jag uppmanar dig att göra egna undersökningar om dessa ämnen.

# Utgiftsverktygen.

Som ni förstår är den säkraste metoden efter mixning att låta de mixade UTXO:erna vara på sitt dedikerade konto och inte röra dem förrän man vill göra sig av med dem.

Det kommer att vara viktigt att avsluta arbetet på ett bra sätt och använda verktyg som är speciellt utformade för att optimera vår integritet vid utgiften av en mixad UTXO.
Tillgängligheten av dessa verktyg beror på den plånboksprogramvara som användaren väljer. Samourai Wallet skiljer sig tydligt från sina konkurrenter genom mångfalden och effektiviteten hos de verktyg som erbjuds där. Vissa av dessa verktyg finns också tillgängliga på Sparrow Wallet. Låt oss tillsammans se vilka dessa verktyg är och hur de används.

## PayJoin - Stowaway.

PayJoin är en CoinJoin mellan två personer med en specifik struktur. Den används vid en bitcoin-utgift. Den kan användas både för att spendera blandade bitcoins och för att spendera oblandade bitcoins.

Denna specifika transaktionsstruktur implementerades för första gången av Samourai Wallet med verktyget Stowaway. Ett BIP följde denna implementation och tog upp idén med PayJoin och döpte om den till P2EP (Pay-to-End-Point).

Det speciella med PayJoin är att den producerar en transaktion som verkar vara vanlig, men som faktiskt är en mini CoinJoin mellan två användare. För detta involverar transaktionsstrukturen mottagaren av transaktionen i ingångarna bredvid den verkliga avsändaren. Mottagaren inkluderar därför en betalning till sig själv mitt i transaktionen för att bli betald.

Till exempel, om du köper en baguette från din bagare för 4000 sats från en UTXO på 10 000 sats och vill göra en PayJoin, kommer din bagare att lägga till en UTXO på 15 000 sats som tillhör honom som ingång i din ursprungliga transaktion, som han kommer att ta ut i sin helhet som utgång för att förvirra den heuristiska analysen:

![Schemat för en Bitcoin PayJoin-transaktion](assets/43.JPEG)

I detta exempel kan vi se att bagaren har satt in 15 000 som ingång och kommit ut med 19 000. Skillnaden är verkligen 4 000 sats, vilket är priset på baguetten. Du som vill köpa baguetten för 4 000 sats har kommit in med 10 000 och kommit ut med 6 000. Skillnaden är verkligen -4 000 sats, vilket är priset på baguetten. I detta exempel har jag medvetet försummat gruvavgifterna för att förenkla.

Genom denna struktur bryter PayJoin mot den gemensamma ägandehuristiken för ingångarna i en Bitcoin-transaktion. När någon observerar denna betalning kommer de att tro att du helt enkelt har kombinerat 2 av dina UTXO:er för att köpa en vara för 19 000 sats och att du har fått växel för 6 000 sats. I verkligheten är situationen mycket annorlunda. Kedjeanalysen är därför förvirrad och betalningsparametrarna är svåra att förstå för någon som observerar dem.

Denna typ av transaktion kan vara en utmärkt lösning för att spendera sina nyblandade bitcoins utan att förlora i sekretess.

JoinMarket inkluderar också ett PayJoin-verktyg för utgifter, du kan upptäcka det genom att klicka här.
Som tidigare nämnts har Samourai Wallet också sitt PayJoin-verktyg: Stowaway. Du kan använda det antingen från Sparrow Wallet-programvaran eller från Samourai Wallet-appen.
Stowaway är baserat på en typ av transaktion som de kallar "Cahoots", det vill säga ett samarbete mellan flera användare som kräver en informationsutbyte utanför Bitcoin-nätverket. För närvarande finns det två Cahoots-verktyg på Samourai: Stowaway och StonewallX2 som vi kommer att utforska senare.

Cahoots-samarbetstransaktioner kräver att delvis signerade transaktioner utbyts mellan användarna. Denna process kan vara ganska lång och besvärlig att genomföra, särskilt om man är på distans med den andra användaren. Det är dock fortfarande möjligt att göra detta manuellt med en annan användare av Samourai Wallet, vilket kan vara ett bra alternativ om man är fysiskt närvarande med den samarbetande personen. Den manuella processen innebär att man byter 5 QR-koder som skannas en efter en.

På distans blir denna process för komplicerad. Samourai har därför utvecklat en utmärkt lösning: sin egen krypterade kommunikationsprotokoll som bygger på Tor, Soroban. Tack vare Soroban behöver användarna inte längre göra alla dessa QR-kodutbyten. Utbytena sker automatiskt i bakgrunden, väl dolda bakom en optimerad användargränssnitt.

Krypterade utbyten kräver ändå en form av anslutning och autentisering mellan Cahoots-samarbetarna. Soroban-utbyten etableras därför på användarnas PayNyms. Om du inte vet vad PayNyms är pratar jag om det i detalj i den här artikeln: Vad är PayNym och BIP47?

För att förenkla det är en PayNym en slags identifierare kopplad till din plånbok som möjliggör en mängd olika funktioner, inklusive utbyte av krypterade meddelanden. PayNym representeras av en identifierare och en teckning av en robot. Här är mitt exempelvis (på Testnet):

![PayNym på Sparrow Wallet](assets/44.JPEG)

För att kunna genomföra en distans-Cahoots-transaktion och därmed en PayJoin via Samourai eller Sparrow måste du "följa" en annan användare via deras PayNym. I det här fallet, för att utföra en Stowaway (PayJoin), måste du följa personen som du vill skicka bitcoins till.

För att göra detta från Sparrow Wallet behöver du bara ange PayNym eller skanna samarbetspartnerns QR-kod i rutan "Hitta kontakt" som du kan se på föregående skärmdump.

På Samourai, klicka på den blå "+" längst ner till höger på skärmen, sedan på "PayNyms" i lila. Om du inte har en PayNym ännu kan du generera din genom att följa instruktionerna.
![Bitcoin-plånbok Samourai Wallet](assets/45.JPEG)
**Handledning utförd på Testnet: det är inte riktiga bitcoins.**
När du är inne i PayNym-gränssnittet, tryck på den blå "+"-knappen. Du kan sedan följa din samarbetspartners PayNym genom att klistra in deras ID eller skanna deras QR-kod.

Klicka sedan på "Följ":

![Följ en PayNym](assets/46.JPEG)

Du blir sedan ombedd om du vill "ansluta" till den. Denna funktion gör det möjligt att använda BIP47 senare. Detta kostar en liten avgift. I vårt fall behöver vi inte det, så vi kommer inte att ansluta oss.

![Anslut till en PayNym](assets/47.JPEG)

I mitt exempel gjorde jag en PayJoin mellan min Samourai Wallet och min Sparrow Wallet. För att komma åt PayNym på Sparrow Wallet, klicka bara på "Verktyg" och sedan på "Visa PayNym".

![Visa PayNym på Sparrow Wallet](assets/48.JPEG)

Här kan vi se att min orange PayNym har fått en följförfrågan från min vita PayNym (på Samourai). Jag är snäll, så jag följer tillbaka:

![Följ PayNym på Sparrow Wallet](assets/49.JPEG)

Nu när Nyms är anslutna kan de kommunicera med varandra via Soroban på ett krypterat sätt. Vi kan nu genomföra en Cahoots-transaktion.

För att göra en PayJoin Stowaway från Samourai måste vi bygga en transaktion. Om du vill spendera mixade UTXO, gå till Post-mix-kontot innan du startar transaktionen.

Klicka på den blå "+"-knappen och sedan på "skicka". Du kan också välja specifikt vilka UTXO du vill skicka:

![Skapa en PayJoin Bitcoin från Samourai Wallet](assets/50.JPEG)

Ange sedan beloppet du vill skicka. I mitt exempel skickar jag 45 000 sats Testnet:

![Inställningar för PayJoin Stowaway](assets/51.JPEG)

Klicka sedan på "Cahoots". Detta fönster öppnas, och du kan välja antingen att göra en StonewallX2 eller en Stowaway. Här vill vi göra en Stowaway:

![Välj typ av samarbetsbaserad Cahoots-transaktion för Bitcoin](assets/52.JPEG)

Som tidigare förklarat kan du antingen göra PayJoin manuellt eller på distans. Det är snabbare och enklare att göra det på distans, men det kräver att du är ansluten via PayNym. I vårt fall kommer vi att välja alternativet "Online":

![Välj typ av samarbete, manuellt eller Soroban](assets/53.JPEG)

Du blir sedan ombedd att välja din samarbetspartner bland dina PayNym-kontakter. Här väljer jag "luckyfrost", som är min orange PayNym på Sparrow:

![Välj samarbetspartner](assets/54.JPEG)

Bekräfta sedan genom att klicka på "Verifiera transaktion".

![Verifiera PayJoin Stowaway Bitcoin-transaktionen](assets/55.JPEG)
Du kan sedan välja gruvavgifterna som tilldelas denna transaktion. Observera att dessa avgifter kommer att betalas av den ursprungliga avsändaren av transaktionen. Klicka på "Starta Stowaway".
![Val av gruvavgifter](assets/56.JPEG)

Du ombeds sedan att vänta tills din partner bekräftar att han eller hon är överens om att genomföra denna samarbetsöverföring.

För att bekräfta en cahoot-begäran på Samourai, klicka på den blå "+" -knappen och sedan på den gröna "Ta emot". En adress visas. Klicka på de tre små punkterna längst upp till höger och sedan på "Ta emot online cahoots".

För att bekräfta på Sparrow Wallet, klicka på fliken "Verktyg" och sedan på "Hitta mixpartner". Ett fönster öppnas, klicka på "Nästa" och sedan på "Nästa" igen för att bekräfta den samarbetsöverföringen.

Cahooten pågår. Dina två plånböcker utbyter delvis signerade och krypterade transaktioner via Tor med hjälp av Soroban.

![Cahoots-processen via Soroban för Stowaway](assets/57.JPEG)

När Stowaway-överföringen är konstruerad kan du sprida överföringen för att skicka den till Bitcoin-noderna.

![Cahoots avslutad, spridning av PayJoin Stowaway-överföringen](assets/58.JPEG)

Där har du det, Stowaway-överföringen är spridd. Grattis.

Genom att observera transaktionen kan man se inputs och outputs från båda användarna. Skillnaden mellan PayNym white's output och input är -45 000 sats, och skillnaden för PayNym orange är +45 000 sats, vilket är det belopp jag slutligen skickade.

![Struktur för PayJoin Stowaway-överföringen](assets/59.JPEG)

### Stonewall.

Stonewall är en specifik transaktionsstruktur som kommer att efterlikna en CoinJoin mellan två personer, utan att faktiskt vara en.

Denna transaktion är inte samarbetsinriktad, den involverar endast UTXO som tillhör transaktionens avsändare. Du kan därför skapa en Stonewall-transaktion för vilket tillfälle som helst, utan att behöva komma överens med någon.

Dess funktion är ganska enkel: vi kommer att använda flera UTXO som tillhör avsändaren som input och skapa 4 outputs. 2 av dessa outputs kommer att vara exakt samma belopp, de andra kommer att vara växel. Av dessa 2 liknande outputs kommer bara en att gå till betalningsmottagaren.

Denna struktur lägger till mycket entropi i transaktionen och förvirrar spåren. Genom att observera den utifrån kan man tro att denna transaktion är en CoinJoin mellan två personer. I själva verket är det en betalning. Detta skapar tvivel i kedjeanalysen.

Detta Stonewall-verktyg används som standard i Samourai Wallet om din plånbok uppfyller de nödvändiga villkoren. Låt oss nu se hur man gör en Stonewall. För detta skickar jag 50 125 sats med hjälp av detta verktyg:
Som ni kan se i denna video är Stonewall-alternativet förvalt som standard.

Så här ser Stonewall-transaktionen ut som jag just genomförde i videon:

![Struktur för Stonewall-transaktion](assets/61.JPEG)

Vi kan se att Samourai har aggregerat 2 UTXO som tillhör mig som indata:

- 130 450 S

- 454 504 S

Och vi kan känna igen de 4 utdatorna från Stonewall-transaktionen:

- 50 125 S som utgör den faktiska betalningen jag just genomförde.

- 50 125 S som returneras till en annan adress som tillhör mig.

- De två växlingarna: 80 168 S och 404 222 S som också returneras till mig.

Mottagaren har alltså endast mottagit 50 125 sats, vilket är värdet på betalningen jag ville initiera.

Självklart, om du vill spendera post-mix måste du först gå till din Whirlpool-plånbok innan du utlöser transaktionen.

Samourai kommer inte att ta ut några avgifter för att konstruera en Stonewall-transaktion. Du måste självklart betala gruvavgifter för din transaktion. Dessa kommer att vara högre än en "vanlig" transaktion eftersom den har fler indata och utdata.

Om du vill använda detta verktyg på Sparrow, hänvisar jag dig till den här handledningen som förklarar i detalj hur du utför operationen: https://sparrowwallet.com/docs/spending-privately.html#paying-to-a-paynym

## StonewallX2.

StonewallX2 fungerar precis som Stonewall med skillnaden att transaktionens indata inte bara är avsändarens, utan även en tredje persons. StonewallX2 är därför en samarbetsbaserad transaktion mellan två användare av Samourai. Liksom för Stowaway (PayJoin) kan kommunikationen mellan medarbetarna ske antingen manuellt (om ni är på samma plats) eller på distans med hjälp av Soroban via Tor.

Skillnaden mellan Stowaway och StonewallX2 ligger i medarbetarens roll. I fallet med Stowaway är medarbetaren alltid betalningsmottagaren. I fallet med StonewallX2 ställer medarbetaren helt enkelt sina bitcoins till förfogande för blandningen, men är inte betalningsmottagaren.

Till exempel, om du vill göra en konfidentiell utgift men säljaren du vill skicka bitcoins till inte stöder Stowaway, kan du helt enkelt göra en StonewallX2 med en annan person som inte har något att göra med transaktionen. Mottagaren kommer fortfarande att vara säljaren, men denne behöver inte utföra alla operationer relaterade till Stowaway.
Således är StonewallX2 en mini CoinJoin mellan 2 personer som inkluderar en utgiftsoutput. Detta lägger till mycket entropi i transaktionen. Denna specifika struktur ger statistisk osäkerhet om kopplingarna mellan avsändaren och mottagaren.
Om man tittar på en StonewallX2-transaktion utifrån kommer dess struktur att vara exakt densamma som en Stonewall-transaktion. Detta lägger till ännu mer osäkerhet.

För att genomföra en distans-StonewallX2-transaktion måste du vara ansluten till din medarbetares PayNym, på samma sätt som för stowaway. När du är ansluten till medarbetaren, låt oss tillsammans se hur man gör en distans-StonewallX2-transaktion. I det här exemplet samarbetar jag med min andra PayNym på Sparrow Wallet. Jag visar det inte i videon, men medarbetaren i Cahoot måste bekräfta på sin plånbok att han vill delta i den gemensamma transaktionen.

![video](assets/62.mp4)

Så här ser den StonewallX2-transaktionen ut som jag just genomförde i videon:

![Struktur för samarbetsbetald Bitcoin-transaktion StonewallX2](assets/63.JPEG)

Den första inputen på 102 588 S kommer från min Samourai-plånbok. Den andra inputen på 104 255 S kommer från min medarbetares plånbok. Vi kan se 4 outputs, varav 2 är av samma belopp för att förvirra spåren:

- 50 125 sats som går till mottagaren av min betalning.

- 52 306 sats som representerar mitt växelbelopp och som därför återgår till en adress i min plånbok.

- 50 125 sats som återgår till min medarbetare.

- 53 973 sats som återgår till min medarbetare.

För StonewallX2-transaktioner delas gruvavgifterna mellan de två medarbetarna. Om vi beräknar saldot för var och en efter transaktionen får vi följande:

- Medarbetaren som gick in med 104 255 sats och kom ut med 104 098 sats. Skillnaden representerar hans del av gruvavgifterna. Om vi bortser från dessa avgifter har medarbetaren genomfört en blind handling.

- För avsändaren gick jag in med 102 588 sats och kom ut med 52 306 sats. Skillnaden på 50 282 sats representerar det belopp jag är skyldig mottagaren (50 125 sats) plus min del av gruvavgifterna.

- Mottagaren gick inte in i transaktionen och kommer ut med 50 125 sats, det belopp jag vill betala honom.

Samourai tar inte ut några avgifter för att konstruera en StonewallX2-transaktion. Du måste naturligtvis betala gruvavgifter för din transaktion. Dessa kommer att vara högre än för en "vanlig" transaktion eftersom den har fler in- och utgångar.
Om du vill använda den här funktionen på Sparrow, hänvisar jag dig till den här handledningen som förklarar i detalj hur du utför operationen: https://sparrowwallet.com/docs/spending-privately.html#paying-to-a-paynym

## Ricochet.

Det sista verktyget jag vill presentera för dig är Ricochet. Det här verktyget skiljer sig något från de tidigare verktygen som alla hade som mål att öka framtida konfidentialitet. Ricochet gör det möjligt att minska spåret som en CoinJoin lämnar på en UTXO och därmed öka retroaktiv konfidentialitet.

Om du genomför transaktioner som CoinJoin och skickar dina blandade bitcoins direkt till en börs kan det hända att tjänsteleverantören blockerar ditt konto eller begär att du motiverar ursprunget till dina medel. För att undvika dessa hycklande och orättvisa blockeringar kan du använda Ricochet för att skicka dina blandade medel till en börs.

Således är det enda användningsfallet för Ricochet när du vill dölja det faktum att du tidigare har genomfört en CoinJoin på en UTXO som tillhör dig.

För att minska detta spår kommer Ricochet att genomföra 4 transaktioner där du skickar pengarna till dig själv på olika adresser, och sedan kommer verktyget att skicka pengarna till din slutdestination (börsen). Målet är att lägga till avstånd mellan CoinJoin-transaktionen och insättnings-transaktionen. Genom detta kommer kedjeanalysverktyg att tro att det har skett en ägarförändring sedan CoinJoin, och därför kommer tjänsteleverantören förmodligen inte att ta risken att blockera ditt konto eller begära motiveringar.

Det här verktyget kan vara viktigt om du behöver byta ut blandade bitcoins, eller helt enkelt om du vill minska "spåret" av deras tidigare blandning.

Som vi tidigare har sett är Ricochet-kontot som används för rebound-adresser helt separat från insättningskontot.

Det finns två alternativ för Ricochet:

- Förstärkt Ricochet: även kallat "stegvis leverans", kommer detta alternativ att fördela avgifterna som betalas till Samourai på de fem rebound-transaktionerna. Det kommer också att garantera att varje rebound finns i en annan block. Det här alternativet är därför utformat för att vara långsamt, men det optimerar konfidentialiteten och motståndskraften mot kedjeanalys för din operation.

- Normal Ricochet: detta alternativ gör det möjligt att genomföra operationen snabbt, men det kommer att vara mindre konfidentiellt och motståndskraftigt mot analyser än det föregående alternativet. Det är att föredra för brådskande överföringar.

Ricochet är en betaltjänst. Du måste betala 100 000 sats i avgifter till Samourai.

Så här genomför du en Ricochet på Samourai Wallet:

![video](assets/64.mp4)
Du är nu redo att använda Whirlpool på bästa sätt och spendera dina postmix på ett korrekt sätt. Verktygen för utgifter i Samourai Wallet, som också ingår i Sparrow Wallet för det mesta, har inga hemligheter för dig längre. Jag rekommenderar att du övar och provar alla dessa verktyg. För att inte riskera dina egna medel, tveka inte att först använda dem på Testnet! Detta nätverk är inte bara för utvecklare.

# Är det fel att blanda bitcoins?

I tal av altcoiners eller nybörjare hittar man ofta en beskrivning av CoinJoin som en mörk, tvivelaktig eller farlig praxis. Denna typ av dunkel berättelse beror ofta på en bristande teknisk förståelse av Bitcoin och en fantasi om CoinJoin.

Allt detta är självklart fel. CoinJoin är en ädel användning av Bitcoin som gör det möjligt för varje individ att återta kontrollen över sin betalningssekretess samtidigt som man förbättrar nätverkets externa fungibilitet, utan att falla in i absolut anonymitet.

Som tidigare förklarat gör CoinJoin helt enkelt att en användare kan klippa av historiken för sina bitcoins och därmed öka sekretessen för sina betalningar, särskilt om hans identitet tidigare hade kopplats till en UTXO.

Det är tack vare dessa verktyg som varje användare kan skydda sin sekretess som vi kan uppnå ett fritt och obegränsat betalningsnätverk. Utan respekt för privatlivet finns ingen frihet.

Att arbeta för att skydda Bitcoin-användarnas privatliv är en ädel sak. När du gör en CoinJoin säkerställer du inte bara din egen sekretess utan hjälper också många andra individer att förbättra sin.

Ja, CoinJoin används ibland av oärliga personer. Men det används också i stor utsträckning av personer som är skyldiga, för vilka behovet av sekretess inte är en bekvämlighet utan en skyldighet. Om alla bara använde CoinJoin när det individuellt blir obligatoriskt skulle de personer som verkligen är tvungna att använda detta verktyg bara blandas med de oärliga personerna och därmed bli lättare att upptäcka för en tyrannisk myndighet.

Jag vill också ta upp argumentet från Gregory Maxwell, som presenterades på Bitcoin Talk 2013 vid introduktionen av CoinJoin: "I verkligheten behöver inte riktiga brottslingar CoinJoin, [...] de har råd att köpa sekretess på ett sätt som vanliga användare inte kan, det är bara en extra kostnad för deras verksamhet (ofta mycket lönsam)."

I alla fall, låt oss komma ihåg att CoinJoin är ett verktyg. Som alla verktyg kan det användas konstruktivt eller destruktivt.
Slutligen anser jag att CoinJoin passar perfekt in i Bitcoin-ideologin och den ursprungliga utvecklingslinjen. Cypherpunks skriver kod. De utvecklar verktyg som ger varje individ kontroll över sin integritet och suveränitet på internet, två avgörande egenskaper för att säkerställa individuell frihet.
Själv ägnar Satoshi Nakamoto en hel del av sin White Paper åt att respektera Bitcoin-användarens integritet. I detta dokument framhäver han risken för förlust av integritet om ägaren till ett nyckelpar avslöjas. Han förklarar att om detta inträffar kan man spåra alla ägarens transaktioner. CoinJoin är för närvarande den bästa lösningen för att bryta kopplingen mellan bitcoins och ägare, som beskrivs av Satoshi Nakamoto i White Paper.

Slutligen rekommenderar jag att du studerar de olika resurserna som jag presenterar i avsnittet "Extern information" nedan, som jag har använt för att producera denna artikel, och som säkert kommer att ge dig ännu mer kunskap.

## För att gå djupare:

- [Allt du behöver veta om Bitcoin-passfrasen.](https://www.pandul.fr/post/tout-savoir-sur-la-passphrase-bitcoin)

- [Hur man genererar sin egen Bitcoin-mnemonicfras?](https://www.pandul.fr/post/comment-g%C3%A9n%C3%A9rer-soi-m%C3%AAme-sa-phrase-mn%C3%A9monique-bitcoin)

- [Vad är PayNym och BIP47?](https://www.pandul.fr/post/qu-est-ce-que-paynym-et-bip47)

## Externa resurser:

Twitter-tråd "Why we CoinJoin" av @SamouraiWallet:

https://twitter.com/SamouraiWallet/status/1489220847336308739

Artikel "HOW TO WHIRLPOOL ON DESKTOP WITH RONINDOJO" av ECONOALCHEMIST på https://bitcoinmagazine.com/:

https://bitcoinmagazine.com/guides/how-to-whirlpool-with-ronindojo

Artikel "THE EASIEST WAY TO WHIRLPOOL YOUR BITCOIN AND PRESERVE PRIVACY" av ECONOALCHEMIST på https://bitcoinmagazine.com/:

https://bitcoinmagazine.com/guides/how-to-whirlpool-bitcoin-on-mobile

Artikel "HOW TO WHIRLPOOL YOUR BITCOIN ON DESKTOP WITH SPARROW WALLET" av ECONOALCHEMIST på https://bitcoinmagazine.com/:

https://bitcoinmagazine.com/technical/how-to-whirlpool-bitcoin-sparrow-wallet

Artikel "Diving head first into Whirlpool Anonymity Sets" av Samourai Wallet.

https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7

Twitter-tråd av @BrotherRabbit/\_ om Whirlpool-prospektscore:

https://twitter.com/BrotherRabbit_/status/1528399310227906561

Samouraï-tutorial av JohnOnChain (Integritet), från Youtube-kanalen Découvre Bitcoin:

https://www.youtube.com/watch?v=kS6iC_ovarQ
Resurser om Ricochet:
https://docs.samourai.io/en/wallet/features/ricochet

Resurser om utgiftsverktyg på Sparrow Wallet:
https://sparrowwallet.com/docs/spending-privately.html#paying-to-a-paynym

Resurser om utgiftsverktyg på Samourai Wallet:
https://docs.samourai.io/en/spend-tools#ricochet

Artikel om installation och användning av WST (på spanska):
https://estudiobitcoin.com/como-instalar-y-utilizar-whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/

Artikel om Coinjoin Change Outputs av BitcoinQ+A på https://bitcoiner.guide/:
https://bitcoiner.guide/doxxic/

Serie av 4 artiklar om att förstå Bitcoin-sekretess med OXT av Samourai Wallet:
https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-4-4-16cc0a8759d5

Resurser om Whirlpool av Samourai Wallet:
https://code.samourai.io/whirlpool/Whirlpool/-/blob/whirlpool/README.md

https://docs.samourai.io/whirlpool/basic-concepts

https://docs.samourai.io/en/wallet/features/whirlpool
