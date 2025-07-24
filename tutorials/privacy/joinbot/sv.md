---
name: JoinBot
description: Förstå och använda JoinBot
---

![DALL·E – samurai robot in a red forest, 3D render](assets/cover.webp)


***VARNING:** Efter gripandet av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april är **tjänsten JoinBot inte längre tillgänglig**. Från och med nu är det inte längre möjligt att använda detta verktyg. Du kan dock fortfarande utföra Stonewall X2, men du måste hitta en samarbetspartner och manuellt Exchange PSBT. Denna tjänst kan komma att återlanseras under de kommande månaderna beroende på hur ärendet fortskrider*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

JoinBot är ett nytt verktyg som läggs till i Samourai Wallet-sviten med den senaste uppdateringen 0.99.98f av den berömda Bitcoin Wallet-programvaran. Det gör att du enkelt kan göra en samarbetstransaktion för att optimera din integritet utan att behöva hitta en partner.


*Tack till den utmärkta Fanis Michalakis för idén att använda DALL-E som miniatyrbild!


## Vad är en samarbetsbaserad transaktion på Bitcoin?


Bitcoin är baserat på ett distribuerat och transparent konto Ledger. Vem som helst kan spåra transaktionerna för användare av detta elektroniska kontantsystem. För att säkerställa en viss nivå av integritet kan Bitcoin-användare göra transaktioner med en specifik struktur för att lägga till trovärdig förnekbarhet i sin tolkning.


Tanken är inte att direkt dölja informationen, utan att förvirra den bland andra. Detta mål används i Coinjoins, transaktioner som bryter ett mynts historia på Bitcoin och gör dess spårning komplex. För att uppnå detta resultat måste flera inmatningar och utmatningar av samma belopp skapas i transaktionen.


Ingångar är ingångarna i en Bitcoin-transaktion och utgångar representerar utgångarna. Transaktionen förbrukar sina inputs för att skapa nya outputs genom att ändra utgiftsvillkoren för ett mynt. Denna mekanism gör att bitcoins kan flyttas mellan användare.

Jag diskuterar detta i detalj i den här artikeln: Bitcoin Transaktionsmekanism: UTXO, ingångar och utgångar.


Ett sätt att sudda ut spåren i en Bitcoin-transaktion är att göra en samarbetstransaktion. Som namnet antyder handlar det om ett avtal mellan flera användare, som var och en sätter in en summa bitcoins som input i samma transaktion och får en summa som output.


Som tidigare nämnts är den mest välkända strukturen för en samarbetstransaktion CoinJoin. Till exempel, på CoinJoin Whirlpool-protokollet, involverar transaktioner 5 deltagare som in- och utgångar, var och en med samma mängd bitcoins.


![Diagram of a Coinjoin transaction on Whirlpool](assets/1.webp)


En extern observatör av denna transaktion kommer inte att kunna veta vilken output som tillhör vilken användare som input. Om vi tar exemplet med användare #4 (lila) kan vi känna igen deras input UTXO, men vi kommer inte att veta vilken av de 5 outputs som faktiskt är deras. Den initiala informationen är inte dold, utan snarare förvirrad inom en grupp.

Användaren kan förneka innehav av en viss UTXO som utdata. Detta fenomen kallas "plausibel förnekbarhet" och möjliggör integritet i en transparent Bitcoin-transaktion.


För att lära dig mer om CoinJoin förklarar jag ALLT i den här långa artikeln: Förstå och använda CoinJoin på Bitcoin.


Även om CoinJoin är mycket effektiv för att bryta spårningen av en UTXO, är den inte lämplig för direkta utgifter. Dess struktur innebär att man måste använda inmatningar av ett fördefinierat belopp och utmatningar av samma värde (modulo Mining-avgifter). Utgiftstransaktionen på Bitcoin är dock ett kritiskt ögonblick för integriteten eftersom den ofta skapar en fysisk länk mellan användaren och dennes On-Chain-aktivitet. Det verkar därför viktigt att använda integritetsverktyg för utgifter. Det finns andra samarbetsstrukturer för transaktioner som är särskilt utformade för faktiska betalningstransaktioner.


## Transaktionen StonewallX2


Bland den myriad av utgiftsverktyg som erbjuds på Samourai Wallet finns den samarbetande transaktionen StonewallX2. Det är en mini CoinJoin mellan två användare utformad för betalning. Från utsidan kan denna transaktion leda till flera möjliga tolkningar. Den ger således en trovärdig förnekelse och följaktligen integritet för användaren.


Denna StonewallX2 samarbetsinställning för transaktioner är tillgänglig på Samourai Wallet och Sparrow wallet. Detta verktyg är driftskompatibelt mellan de två programvarorna.


Dess mekanism är ganska enkel att förstå. Så här fungerar det i praktiken:



- En användare vill göra en betalning i bitcoins (t.ex. hos en handlare).
- De hämtar den mottagande Address för den faktiska betalningsmottagaren (handlaren).
- De konstruerar en specifik transaktion med flera olika ingångar: minst en som tillhör dem själva och en som tillhör en extern samarbetspartner.
- Transaktionen kommer att ha 4 utgångar, inklusive 2 av samma belopp: en till handlarens Address för betalning, en som växel som återgår till användaren, en utgång av samma värde som betalningen som går till medarbetaren och en annan utgång som också återgår till medarbetaren.


Här är till exempel en typisk StonewallX2-transaktion där jag gjorde en betalning på 50 125 Sats. Den första inmatningen på 102 588 Sats kommer från min Samourai Wallet. Den andra inmatningen på 104 255 Sats kommer från min samarbetspartners Wallet:


![StonewallX2 transaction diagram](assets/2.webp)


Vi kan observera 4 utgångar, inklusive 2 av samma belopp för att förvirra spåren:



- 50 125 Sats` som går till den faktiska mottagaren av min betalning.
- `52 306 Sats` som representerar min förändring och återgår därför till en Address i min Wallet.
- 50 125 Sats` som går tillbaka till min samarbetspartner.
- `53 973 Sats` återgår till min samarbetspartner.


I slutet av transaktionen har samarbetspartnern fått sitt ursprungliga saldo återställt (minus Mining-avgifter) och användaren har betalat handlaren. Detta tillför en betydande mängd entropi till transaktionen och bryter de obestridliga länkarna mellan avsändaren och mottagaren av betalningen.


Styrkan med Stonewall X2-transaktionen är att den helt motverkar en av de empiriska regler som används av kedjeanalytiker: den vanliga Ownership av inputs i en transaktion med flera inputs. Med andra ord kan vi i de flesta fall, om vi observerar en Bitcoin transaktion med flera inmatningar, anta att alla dessa inmatningar tillhör samma person. Satoshi Nakamoto hade redan identifierat detta problem för användarnas integritet i sin vitbok:


> Som en extra brandvägg kan ett nytt nyckelpar användas för varje transaktion för att förhindra att de länkas till en gemensam ägare. Kopplingen är dock oundviklig med transaktioner med flera inmatningar, som med nödvändighet avslöjar att deras inmatningar ägdes av samma ägare.

Detta är en av de många empiriska regler som används i On-Chain-analysen för att konstruera Address-kluster. För att lära dig mer om dessa heuristiker rekommenderar jag att du läser den här serien med fyra artiklar av Samourai, som introducerar ämnet underbart.


Styrkan i StonewallX2-transaktionen ligger i att en utomstående betraktare kommer att tro att transaktionens olika ingångar tillhör en gemensam ägare. I själva verket är det två olika användare som samarbetar. Analysen av betalningen leds alltså till ett lockbete och användarnas integritet bevaras.


Från utsidan kan en StonewallX2-transaktion inte särskiljas från en Stonewall-transaktion. Den enda faktiska skillnaden mellan dem är att Stonewall inte är ett samarbete. Den använder bara en enda användares UTXO:er. I sina strukturer på kontot Ledger är dock Stonewall och StonewallX2 helt identiska. Detta möjliggör ännu fler möjliga tolkningar av denna transaktionsstruktur eftersom en extern observatör inte kommer att kunna avgöra om inmatningarna kommer från samma person eller från två samarbetspartners.


Fördelen med StonewallX2 jämfört med en PayJoin av fripassagerartyp är dessutom att den kan användas i alla situationer. Den faktiska mottagaren av betalningen bidrar inte med några inmatningar till transaktionen. Således kan en StonewallX2 användas för att betala hos alla handlare som accepterar Bitcoin, även om handlaren inte använder Samourai eller Sparrow.

Å andra sidan är den största nackdelen med denna transaktionsstruktur att den kräver en samarbetspartner som är villig att använda sina bitcoins för att delta i din betalning. Om du har Bitcoin-vänner som är villiga att hjälpa dig i alla situationer är detta inte ett problem. Men om du inte känner några andra Samourai Wallet-användare, eller om ingen är tillgänglig för att samarbeta, då är du fast.


För att lösa detta problem har Samourai-teamet nyligen lagt till en ny funktion i sin applikation: JoinBot.


## Vad är JoinBot?


Principen för JoinBot är enkel. Om du inte kan hitta någon att samarbeta med för en StonewallX2-transaktion kan du samarbeta med JoinBot. I praktiken kommer du faktiskt att genomföra en samarbetstransaktion direkt med Samourai Wallet.


Den här tjänsten är mycket bekväm, särskilt för nybörjare, eftersom den är tillgänglig 24/7. Om du behöver göra en brådskande betalning och vill göra en StonewallX2 behöver du inte längre kontakta en vän eller leta efter en online-samarbetspartner. JoinBot kommer att hjälpa dig.


En annan fördel med JoinBot är att de UTXO:er som den tillhandahåller som input uteslutande kommer från postmix Whirlpool, vilket förbättrar integriteten för din betalning. Eftersom JoinBot alltid är online bör du dessutom samarbeta med UTXO:er som har stora potentiella Anonsets.


Självklart har JoinBot vissa kompromisser som bör noteras:



- Precis som med en klassisk StonewallX2 är din samarbetspartner nödvändigtvis medveten om de UTXO:er som används och deras destination. När det gäller JoinBot känner Samourai till detaljerna i denna transaktion. Detta är inte nödvändigtvis en dålig sak, men det bör hållas i åtanke.
- För att undvika skräppost tar Samourai ut en serviceavgift på 3,5 % av beloppet för den faktiska transaktionen, med en högsta gräns på 0,01 BTC. Om jag till exempel skickar en verklig betalning på 100 kilosats med JoinBot, kommer serviceavgiftsbeloppet att vara 3 500 Sats.
- För att kunna använda JoinBot måste du ha minst två obundna och tillgängliga UTXO:er i din Wallet.
- I en klassisk StonewallX2 delas Mining-avgifterna lika mellan de två samarbetspartnerna. Med JoinBot kommer du självklart att behöva betala hela Mining-avgiften.
- För att en JoinBot-transaktion ska vara exakt densamma som en klassisk StonewallX2- eller Stonewall-transaktion sker betalningen av serviceavgifter i en helt separat transaktion. Återbetalningen av hälften av Mining-avgifterna som ursprungligen betalades av Samourai kommer att göras under denna andra transaktion. För att optimera din integritet till slutet görs avgiftsavräkningen med hjälp av en Stowaway (PayJoin) strukturerad transaktion.


## Hur man använder JoinBot?


För att utföra en JoinBot-transaktion måste du ha en Samourai Wallet. Du kan ladda ner den här, eller från Google Playstore.


Till skillnad från de flesta verktyg som utvecklats av Samourai har Sparrow wallet ännu inte meddelat implementeringen av JoinBot. Det här verktyget är därför endast tillgängligt på Samourai.


Upptäck steg för steg hur du utför en StonewallX2-transaktion med JoinBot i den här videon:


![How to use Joinbot](https://youtu.be/80MoMz2Ne5g)


Här är transaktionsdiagrammet som vi just visade i videon:


![Diagram of my StonewallX2 transaction with JoinBot.](assets/3.webp)


Vi kan se 5 ingångar:



- 3 inmatningar av 100 kilosats kommer från Samourai (JoinBot).
- 2 ingångar kommer från min personliga Wallet, av 3.524 Sats och 1,8 megasat.


Transaktionens 4 utgångar är följande:



- 1 av 212.452 Sats till den faktiska mottagaren av min betalning.
- Ytterligare en på samma belopp som går tillbaka till en Samourai Address.
- 1 förändring som också går tillbaka till Samourai för 87 302 Sats. Detta motsvarar skillnaden mellan summan av deras inmatningar (300 000 Sats) och fördunklingsresultatet (212 452 Sats) minus Mining-avgifterna.
- 1 förändring som går tillbaka till en annan Address i min Wallet. Det motsvarar skillnaden mellan summan av mina inmatningar och den faktiska betalningen, minus Mining-avgifterna.


Som en påminnelse representerar Mining-avgifter inte transaktionsutgångar. De representerar helt enkelt skillnaden mellan de totala inmatningarna och de totala utmatningarna.


## Slutsats


JoinBot är ett extra verktyg som ger Samourai-användare fler valmöjligheter och större frihet. Det möjliggör en samarbetande StonewallX2-transaktion direkt med Samourai som samarbetspartner. Denna typ av transaktion hjälper till att förbättra användarnas integritet.


Om du kan utföra en klassisk StonewallX2 med en vän rekommenderar jag fortfarande att du använder det här verktyget. Men om du sitter fast och inte kan hitta några medarbetare för att göra en betalning, vet du att JoinBot kommer att vara tillgänglig 24/7 för att samarbeta med dig.


**Externa resurser:**


- https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin