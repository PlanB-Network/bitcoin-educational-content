---
name: Lightning Network+
description: Få gratis inkommande likviditet med kooperativa öppningar på din Lightning-nod
---

![cover](assets/cover.webp)



## Inledning



[LN+ (Lightning Network Plus)](https://lightningnetwork.plus/) är en community-plattform som är utformad för att underlätta samarbetet mellan Lightning Network-nodoperatörer. Huvudsyftet är att förbättra anslutningsmöjligheterna, likviditeten och decentraliseringen av Lightning-nätverket utan behov av centraliserade mellanhänder.



Denna handledning kommer att fokusera på tjänsten **"Swaps"**, som är den mest använda och strukturerande funktionen i LN+ idag. De andra tjänsterna som erbjuds av plattformen kommer också att presenteras.



## LN+ översikt



### Vad är Lightning Network Plus?



Lightning Network Plus (LN+) är en community-plattform för Lightning-nodoperatörer som vill samarbeta direkt och frivilligt. Den syftar till att underlätta skapandet av användbara, balanserade och hållbara Lightning-kanaler, samtidigt som man undviker behovet av centraliserade lösningar eller påtvingade hubbar.



LN+ bygger på en grundläggande princip: peer-to-peer-samarbete, grundat på öppenhet, ömsesidighet och gott rykte.



### LN+ tjänster i korthet



LN+ erbjuder flera tjänster som är utformade för att förbättra topologin och likviditeten i Lightning-nätverket, inklusive :





- Swaps**: Ömsesidigt öppnande av kanaler mellan operatörer (huvudtjänst).
- Ringar**: cirkulära kanalöppningar mellan flera deltagare.
- Förtroendebaserade swappar**: varianter som i högre grad bygger på deltagarnas förtroende och historia.
- Sociala funktioner**: profiler, kommentarer och ryktessystem.



I resten av denna handledning kommer vi att koncentrera oss uteslutande på **Swaps**-tjänsten, som är kärnan i den nuvarande LN+-användningen.



## LN+ "Swaps"-tjänst



### Definition av en LN+ swap



Ett LN+ **swap** är ett frivilligt avtal mellan två Lightning-nodoperatörer om att ömsesidigt öppna Lightning-kanaler med likvärdig (eller på förhand överenskommen) kapacitet. Till skillnad från en konventionell unilateral kanalöppning baseras bytet på **explicit reciprocitet**.



I praktiken :





- Du öppnar en kanal till din partners nod.
- Din partner öppnar en kanal till din nod.
- Båda parter binder upp en liknande mängd on-chain bitcoins.



### Vad är syftet med swappar för nodoperatörer?



Swaps-tjänsten hanterar flera viktiga problem som blixtoperatörer stöter på:





- Förbättrad konnektivitet**: skapande av användbara dubbelriktade kanaler så snart de öppnas.
- Bättre likviditetshantering**: varje part har både inkommande och utgående kapacitet.
- Minskad risk för onödiga kanaler**: partnern uppmuntras att hålla kanalen öppen.
- Större decentralisering**: direkta förbindelser mellan operatörer, utan påtvingade hubbar.



### För vilka nodprofiler är swappar användbara?



Swappar är särskilt användbara för :





- Nya noder som snabbt vill förbättra sin routbarhet.
- Intermediära operatörer som vill öka tätheten i sin kanalgraf.
- Routing-orienterade noder som vill optimera sin topologi.



## Anslut din Lightning-nod till LN+



### Tekniska krav



Innan du börjar behöver du :





- En fungerande Lightning-nod (LND, Core Lightning eller Eclair).
- Åtkomst till din nods administrationsgränssnitt.
- Tillräcklig on-chain-kapacitet för att öppna kanaler.



Gå till webbplatsen [Lightning Network](https://lightningnetwork.plus/) Plus och klicka på knappen "Logga in" längst upp till höger i gränssnittet.



![capture](assets/fr/03.webp)



### Autentisering genom meddelandesignatur



För att autentisera dig måste du signera meddelandet med hjälp av din Lightning-nods privata nyckel. Med ThunderHub är denna operation mycket enkel.



Börja med att kopiera meddelandet som visas av LN+.



![capture](assets/fr/04.webp)



I ThunderHub går du till fliken `Tools` och klickar sedan på `Sign` i avsnittet `Messages`.



![capture](assets/fr/05.webp)



Klistra in autentiseringsmeddelandet som tillhandahålls av LN+ och klicka sedan på `Signera`.



![capture](assets/fr/06.webp)



ThunderHub signerar sedan detta meddelande med din nods privata nyckel. Kopiera den genererade signaturen.



![capture](assets/fr/07.webp)



Klistra in denna signatur i motsvarande fält på LN+-webbplatsen och klicka sedan på "Logga in".



![capture](assets/fr/08.webp)



Du är nu ansluten till LN+ med din Lightning-nod. Denna process gör det möjligt för LN+ att verifiera att du är den rättmätiga ägaren till den nod du gör anspråk på på deras plattform.



![capture](assets/fr/09.webp)



Om du vill kan du anpassa din LN+-profil, till exempel genom att lägga till en kort biografi.



## Delta i en befintlig swap



### Tillgång till byteserbjudanden



För att delta i din första kanalöppning, gå till menyn `Swaps` högst upp i gränssnittet. Här hittar du alla de swappar som för närvarande är tillgängliga, beroende på din nods egenskaper.



![capture](assets/fr/10.webp)



### Villkor för stödberättigande



För att gå med i ett befintligt byteserbjudande väljer du helt enkelt motsvarande annons och registrerar dig. LN+ tillåter dock swap-skaparen att definiera vissa **berättigande villkor**, till exempel :





- ett minsta antal kanaler som redan är öppna ;
- minsta totala nodkapacitet ;
- vissa typer av anslutningar accepteras.



### Senaste noderna



Som ett resultat av detta, särskilt i början av användningen, är det möjligt att **få eller inga erbjudanden är tillgängliga** för din nod. Detta är en vanlig situation för nya noder eller noder som ännu inte är anslutna.



I mitt fall, trots att det fanns några öppna kanaler, uppfyllde inget av anbuden de kriterier som krävdes.



## Skapa ditt eget byteserbjudande



### När bör du skapa din egen swap?



När inget befintligt erbjudande finns tillgängligt är det ofta den bästa lösningen att skapa ett eget swap. Det ger dig också möjlighet att behålla kontrollen över swappens parametrar.



### Konfiguration för byte



Klicka på **Start Liquidity Swap** och konfigurera sedan dina erbjudandeparametrar:





- välj det totala antalet deltagare (3, 4 eller 5);
- anger kapaciteten för de kanaler som ska öppnas;
- definiera den åtagandeperiod under vilken deltagarna samtycker till att inte stänga sina kanaler;
- ange eventuella begränsningar som gäller för deltagarna (minsta antal kanaler, minsta totala kapacitet, typ av anslutning som godtas).



![capture](assets/fr/11.webp)



### Publicering och deltagarnas förväntningar



När alla parametrar har angetts klickar du på **Starta Liquidity Swap** för att publicera ditt erbjudande. Nu är allt du behöver göra att vänta på att andra operatörer ska registrera sig.



![capture](assets/fr/12.webp)



## Slutföra ett byte



### Effektiv kanalöppning



Nu när alla swappositioner har tagits kan varje deltagare se, från sitt LN+-gränssnitt, vilken nod han behöver öppna en Lightning-kanal till.



![capture](assets/fr/13.webp)



På din sida öppnar du kanalen med hjälp av nod-ID:t som tillhandahålls av LN+ och respekterar det angivna beloppet. Denna operation kan utföras via ThunderHub, en annan Lightning node manager eller direkt via din nods grundläggande gränssnitt.



![capture](assets/fr/14.webp)



När kanalen har öppnats visas den i avsnittet med väntande kanaler.



![capture](assets/fr/15.webp)



### Bekräftelse i LN+



Gå sedan tillbaka till LN+ för att bekräfta att du har påbörjat kanalöppningen genom att klicka på knappen "Kanalöppning påbörjad".



![capture](assets/fr/16.webp)



### Slut på swap



När alla deltagare har öppnat de kanaler som de har åtagit sig att använda, anses bytet vara slutfört.



## Rykte och god kommunikationssed



### Reputationssystemet LN+



LN+ innehåller ett ryktessystem som baseras på de åsikter som lämnas av deltagarna i slutet av swappen. Dessa åsikter är offentliga och påverkar direkt en operatörs möjlighet att delta i eller skapa framtida swappar.



![capture](assets/fr/17.webp)



### Rekommenderade bästa metoder



För att bevara ett gott rykte och säkerställa att swapparna går smidigt rekommenderas att :





- respektera tidsfrister för kanalöppning ;
- kommunicera snabbt i händelse av problem eller förseningar;
- använda kommentarsfältet för att utbyta åsikter med andra deltagare;
- att inte stänga en kanal före utgången av åtagandeperioden.




![capture](assets/fr/18.webp)



### Varför rykte är centralt för LN+



LN+ bygger på en modell för frivilligt samarbete, utan några starka tekniska begränsningar. Anseendet är därför det viktigaste incitamentet för att säkerställa deltagarnas tillförlitlighet och pålitlighet.



## Övriga LN+ tjänster



Förutom Swaps erbjuder LN+ andra tjänster som är utformade för att förbättra anslutningen och samordningen mellan Lightning-nodoperatörer. Ringar** gör det möjligt för flera deltagare att skapa en loop av kanalöppningar, vilket förstärker redundansen i routningsvägarna och tätheten i Lightning-grafen. Förtroendebaserade swappar** bygger på liknande principer som klassiska swappar, men erbjuder större flexibilitet för deltagare som redan har ett etablerat rykte på plattformen.



LN+ integrerar även sociala funktioner som offentliga nodprofiler, swap-kommentarer och ett ryktessystem. Dessa verktyg är inte tekniska tjänster i sig, men spelar en central roll för att plattformen ska fungera smidigt och underlätta kommunikation, samordning och förtroende mellan operatörerna.



## Slutsats



LN+:s Swaps-tjänst är ett effektivt verktyg för att förbättra konnektiviteten, likviditeten och decentraliseringen i Lightning-nätverket. Genom att främja ömsesidiga, samordnade kanalöppningar gör LN+ det möjligt för nodoperatörer att stärka sin topologi, samtidigt som de främjar ansvarsfullt, decentraliserat samarbete.