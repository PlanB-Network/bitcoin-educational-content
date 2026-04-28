---
name: Betjänt Bitcoin
description: Valet ger dig en Lightning-nod utan förvaring i fickan
---

![cover_valet](assets/cover.webp)



## Inledning


Valet är en lätt, självförvaltande, Bitcoin och Lightning wallet som erbjuder en enkel och bekväm onboardingprocess för nybörjare. Den är särskilt skräddarsydd för att betjäna Bitcoin-samhällen och cirkulära ekonomier, särskilt i avlägsna områden.


Det är en fork av **Simple Bitcoin Wallet (SBW)**, med en avancerad Hosted Lightning-kanalfunktion som kallas **Fiat Channels**, utformad för att göra det möjligt för alla att acceptera Lightning-betalningar utan volatilitetsrisker.


Valet är för närvarande endast tillgängligt för Android-enheter och kan laddas ner och installeras från flera appbutiker med öppen källkod. Valet finns dock **inte** i **Google Play Store** på grund av integritets- och kundkännedomsproblem för utvecklare.



## Ladda ner och installera Valet


Valet kan laddas ner som en APK-fil från Standard Sats 'GitHub-sida. [Standard Sats](https://standardsats.github.io/) är företaget som utvecklade Valet.


👉 För att ladda ner Valet, besök Standard Sats [GitHub-sidan] (https://github.com/standardsats/valet/releases) och leta reda på den **nyaste ** versionen (detta är ofta den översta).


👉 Gå till **Assets** och klicka på filen med endast ett **.apk**-tillägg. Din nedladdning startar automatiskt.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


👉 När nedladdningen är klar går du till din enhets **Filhanterare** > **Nedladdningar** och väljer Valet apk-filen.


![Select_valet_apk](assets/en/002.webp)


👉 Installera den, och om några sekunder är din app klar och visas på din startskärm.


![valet_icon_on_homescreen](assets/en/003.webp)


Alternativt kan du också ladda ner Valet från **F-Droid** app store. Om du inte har F-Droid-appen på din enhet kan du ladda ner och installera den [här] (https://f-droid.org/en/).


👉 Öppna F-Droid på din startskärm och sök efter **Valet**. Välj det första alternativet med en **lila och vit ikon** från de två alternativen som visas och klicka på **Download**.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


👉 När du har laddat ner klickar du på **Installera** och följer instruktionerna på skärmen. När installationen är klar kan du starta Valet från F-Droid genom att klicka på **Öppna** eller starta den från enhetens startskärm.



## Skapa en Bitcoin Wallet


Du kan ställa in en Bitcoin wallet på Valet i två enkla steg.


👉 Starta Valet från din enhets startskärm eller från F-Droid-appen. En wallet-inställningsskärm visas, med två alternativ: ** Skapa ny Wallet** och ** Återställ befintlig Wallet**.


👉 Välj **Create New Wallet**, och omedelbart kommer en ny wallet att skapas och du kommer att omdirigeras till hemsidan.


![set_up_a\_new_wallet](assets/en/006.webp)



## Säkerhetskopiera din startfras


👉 På wallet-hemsidan klickar du på **Green-kortet** som har en inskription **"Tryck för att spara wallet återställningsfras om du någonsin förlorar eller byter ut din enhet".**


![seed_phrase_green_card](assets/en/007.webp)


👉 En uppsättning med 12 engelska ord kommer att visas. Skriv ner dem på papper, i ordningen 1 till 12, och förvara dem säkert.


![the_seed_phrase](assets/en/008.webp)


### Var uppmärksam ⚠️:


Var uppmärksam på följande element:


- Som du redan vet är Valet en självförvaltande wallet, så din seed-fras är den enda tillgången till att återhämta din Wallet.
- Om du någonsin förlorar din seed-fras kommer du **aldrig** att få tillgång till din wallet.
- Om någon får tag på din seed-fras kan de oåterkalleligen stjäla alla dina Bitcoin:or.


Så du måste skriva ner din seed-fras på 12 ord och förvara den på en säker plats. Du ska aldrig ta en skärmdump, spara den som ett utkast i din e-post eller spara den på någon elektronisk enhet som någonsin har varit ansluten till internet.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Mottagning och sändning av Bitcoin på Valet


Valet är en självförvarande wallet med både on-chain- och Lightning Bitcoin-kapacitet. Detta innebär att du kan ta emot och skicka Bitcoin ut från Valet antingen via en **On-chain** eller via en **Lightning Network**.


För att kunna ta emot eller skicka Bitcoin via Lightning måste du dock skapa en Lightning-kanal med dina on-chain Bitcoin som Liquidity. Eller så kan du köpa lite Lightning-kanallikviditet från leverantörer.



## Generering av en kedja Bitcoin Address


För att kunna ta emot Bitcoin via on-chain måste du skapa en Bitcoin-adress.


👉 På hemsidan för wallet ser du ett **Orange** och ett **Lila kort**, märkta **Bitcoin** respektive **Lightning**.


👉 Klicka på det orange kortet märkt **Bitcoin**. Du kommer att omdirigeras till en skärm som visar en Bitcoin-adress.


![click_on_Bitcoin_card](assets/en/009.webp)


👉 Du kan **kopiera** adressen och skicka den till den person som skickar Bitcoin till dig, eller klicka på **dela**-knappen för att skicka QR-koden till personen via sociala medier eller andra kommunikationskanaler.


👉 Du kan också klicka på knappen **Edit** för att ställa in hur många Bitcoin som ska skickas till den adressen.


**Attention:** Precis som en faktura är redigeringsfunktionen praktisk i scenarier där du kanske vill ta emot ett visst antal Bitcoin till en adress vid en tidpunkt; detta betyder dock inte att adressen inte kan ta emot högre eller lägre belopp.


👉Klicka på **Fler nya adresser** för att generera nya slumpmässiga adresser.


![generating_a\_bitcoin_add](assets/en/010.webp)


👉 Du kan också generera en on-chain Bitcoin-adress genom att klicka på **Receive**-knappen längst ner på din wallet-hemsida. Välj sedan **Mottag till bitcoinadress** och fortsätt med samma process ovan.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Skickar Bitcoin via kedjan On-chain


Att skicka ut Bitcoin från Valet wallet via on-chain är en okomplicerad uppgift.


👉 Längst ner på din wallet:s hemsida klickar du på knappen **Sänd**, anger Bitcoin-adressen eller klickar på **Skanna** för att skanna adressens QR-kod och klickar sedan på **Ok**.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


👉 Ange det Bitcoin-belopp som du vill skicka. Du kan manuellt ange ett belopp i termer av Sats eller i Fiat-valuta, eller så kan du klicka på **Max** för att använda hela ditt on-chain-saldo.


👉 Du kan också justera de avgifter du vill betala för transaktionen genom att klicka på den lilla gröna rutan märkt **avgift** och sedan skjuta den vita punkten åt höger eller vänster för att öka respektive minska avgifterna. Klicka på **Ok** för att skicka transaktionen.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Ställa in en Lightning Network-kanal


Som nämnts ovan är Valet en självförvaltande Bitcoin och Lightning wallet; för att kunna skicka och ta emot Bitcoin via Lightning-nätverket måste du därför först ställa in en Lightning-kanal genom att följa dessa steg:


👉 På startskärmen klickar du på det **lila kortet** märkt **Blixt**. Du kommer att tas till en sida med följande alternativ:



- Skanna noden QR
- Köp hos LNBIG.COM
- Köp hos BITREFILL.COM
- Begär omsynkronisering av LN-grafen.


När du väljer **Purchase from lnbig.com** eller **Purchase from bitrefill.com** kommer du att omdirigeras till dessa företags webbplatser, där du kan köpa en inkommande likviditet med flera kapaciteter. Ignorera det sista alternativet **Request LN graph resync** för tillfället.


Så vårt val här är att **Skanna en Node QR**. Vid denna tidpunkt måste du ha bestämt dig och fått **QR-koden** för den nod du vill öppna en kanal till. Du kan öppna kanaler till alla offentliga noder du väljer. Kolla in [1ML](https://1ml.com/) eller [Amboss](https://amboss.space/), välj vilken offentlig nod du vill och skanna den tillhörande QR-koden för den nod du valde.


![channel_opening_options](assets/en/016.webp)


👉 Du kommer automatiskt att omdirigeras till nästa sida, där du nu måste finansiera din kanal. Återigen kräver självförvaltande Lightning-nätverksanvändning att du använder dina Bitcoin för att finansiera en kanal. Det betyder att du måste ha Bitcoin i din on-chain wallet som du kan finansiera Lightning-kanalen med. Se den här artikeln av [Hacken](https://hacken.io/discover/lightning-network/), läs mer om Lightning-nätverket.


![fund_channel](assets/en/017.webp)


👉 Ange det **belopp** Bitcoin som du vill finansiera kanalen med, eller klicka på **Max** för att använda hela ditt on-chain Bitcoin-saldo. Du kan justera **avgiften**, eller lämna standardinställningen för avgiften och klicka på **Ok**.


**Det belopp som du finansierar kanalen med kommer att vara kapaciteten för din nya kanal (dvs. den totala volymen av Sats som kan överföras till och från den kanalen)


Det är också viktigt att du använder mer än **100 000 Sats** som finansieringsbelopp när du öppnar en kanal. Detta beror på att många Lightning-noder kräver en kapacitet på minst 100 000 Sats för att öppna en kanal till dem. Så för att undvika försök och fel, använd helt enkelt belopp som är högre än det intervallet.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


👉 När du nu kontrollerar din wallet-hemsida kommer du att se att ditt finansieringsbelopp nu har flyttats från **Bitcoin-kortet** till **Lightning-kortet**. På din transaktionshistorik ser du att finansieringstransaktionen behandlas.


![channel_funding_processing](assets/en/020.webp)


👉 Om du klickar på Lightning-kortet kommer du att se information som visar att din Lightning-kanal öppnas. Du kommer också att se **channel funding transaction** på din lista över transaktioner. Vänta tills din finansieringstransaktion har bekräftats på blockchain och din Lightning-kanal är klar.


![channel_opening](assets/en/021.webp)


👉 Så snart finansieringstransaktionen har bekräftats klickar du på **Lightning-kortet** på din startsida och du kommer att se informationen om din Lightning-kanal enligt följande:



- RANDOM SET OF NUMBERS SEPARATED BY DOTS:** Detta är nodernas IP-adresser. (IPV4 respektive IPV6)
- CAPACITY:** Detta är den totala volymen Sats som kan sändas och tas emot via denna kanal
- KAN SÄNDA:** Detta är den mängd Sats som du kan skicka ut vid denna punkt. Du kommer att märka att det är nästan samma siffra som **Capacity**. Detta beror på att du inte har skickat ut några betalningar genom kanalen.
- KAN MOTTA:** Detta är antalet Sats som du kan ta emot till den här kanalen för tillfället. (Det kommer att vara lite eller inget vid denna tidpunkt eftersom du för att kunna ta emot måste du först skicka ut några Sats för att skapa en inkommande Liquidity)
- Återbetalningsbart:** Här visas det belopp som betalas tillbaka till din on-chain-adress när du stänger din kanal. Detta kallas också för din **Kanals lokala saldo**. Observera att det är bara något mindre än kanalens kapacitet, och det beror på att när du stänger en kanal måste du betala en avgift för att publicera stängningstransaktionen på blockchain, precis som du gjorde när du finansierade kanalen. Så systemet har dragit av det ungefärliga lägsta belopp som du kommer att betala)
- VALUE IN FLIGHT:** När någon skickar sats till din kanal, eller när du försöker skicka sats till någon, och transaktionen av någon anledning blir försenad, visas det ofta i det här fältet.


![channel_info](assets/en/022.webp)


## Sänder Sats genom din kanal


Att skicka Sats genom Lightning Network är en okomplicerad uppgift.


👉 Längst ner på startsidan klickar du på **Sänd** och **klistrar in** Lightning-fakturan (du måste ha kopierat den) i det angivna fältet, eller klickar på **Skanna** för att skanna Lightning-fakturans QR-kod.


![click_send_or_scan](assets/en/023.webp)


De flesta Lightning-fakturor kommer med ett förinmatat belopp som ska betalas. Men i några fall kan det vara en öppen faktura där du måste fylla i beloppet.


👉 Ange beloppet i **Dollars** eller **Sats**, eller klicka på **Max**, för att använda hela saldot på din Lightning-kanal, och klicka sedan på **Ok**. Så snart en bra väg har hittats kommer din betalning att skickas och slutföras inom några sekunder. Håll ett öga på startsidan för att se om betalningen har slutförts. Den kommer att få en grön bock när den har slutförts.


![enter_the_amount](assets/en/024.webp)


## Mottagning av Sats genom din kanal


Att ta emot betalningar på din Lightning-kanal är till stor del beroende av om du har en inkommande Liquid-likviditet eller inte. När du har öppnat en kanal kommer du inte att kunna ta emot betalningar förrän du åtminstone har skickat några Sats för att **skapa inkommande likviditet** i den andra änden av kanalanslutningen. För att bekräfta om du kan ta emot Sats och hur mycket Sats du kan ta emot, kontrollera fältet **Kan ta emot** i din kanalinformation. Detta kommer att visa dig hur många Sats du tar emot vid varje tidpunkt.


Låt oss nu anta att du har skickat ut några Sats från din kanal, att du nu har inkommande likviditet och kan ta emot Sats.


För att ta emot på Lightning-kanalen måste du generera en faktura. Till skillnad från Bitcoin on-chain, som använder adresser, använder Lightning-nätverket fakturor. Det finns två sätt att generera en faktura på Valet.


#### ALTERNATIV 1


👉 Längst ner på startsidan klickar du på **Mottagning**, välj **Mottagning till blixtfaktura**. Fyll i det belopp som ska tas emot i fakturan och klicka på **Ok**. Kopiera fakturan eller dela QR-koden med betalaren.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### ALTERNATIV 2


👉 Klicka på det lila Lightning-kortet på din wallet-hemsida. Tryck var som helst på din kanal, och en lista med alternativ kommer att dyka upp. Välj **Mottagning till kanal** och ange beloppet du tar emot (antingen i Sats eller dollar). Du kommer också att se hur många Sats du kan ta emot (inkommande kapacitet) när du fyller i fakturan. Klicka på **Ok** och kopiera fakturan eller dela QR-koden med betalaren.


![receive_to_channel](assets/en/028.webp)


**Det första alternativet är ett universellt alternativ, vilket innebär att om du har mer än en aktiv kanal och du använder det första alternativet, kommer systemet automatiskt att välja en av dina kanaler för mottagning av Sats.


Så i det här scenariot är det andra alternativet bäst att använda om du vill ta emot Sats till en viss kanal.


### Förklaring av popup-alternativ för din kanal


När du trycker på din kanal visas följande alternativfält:


![channel_pop_ups](assets/en/029.webp)


**SHARE LIGHTNING CHANNEL DETAILS:** Detta gör att du kan dela dina kanaldetaljer, till exempel fjärrpeer-ID, lokalt kanal-ID, finansieringstransaktion, datum för skapande etc.


**STÄNG KANAL TILL WALLET:** Du kan stänga din blixtkanal när du vill. För att stänga din kanal kontrollerar systemet det Bitcoin-saldo du har på din egen sida av kanalen (kom ihåg fältet **"Kan skicka"**, även känt som ditt lokala saldo) och skickar tillbaka det till dig. I Valet får du välja vart du vill att Bitcoin ska skickas när kanalen stängs. Så **Stäng kanal till wallet** är ett av dina två alternativ.


👉 Klicka på det här alternativet och välj **Bitcoin**. Kanalstängningen kommer att påbörjas och saldot för din kanal Bitcoin kommer att skickas tillbaka till din wallet:s on-chain-adress.


![close_channel_to_wallet](assets/en/030.webp)


**CLOSE CHANNEL TO ADDRESS:** Detta är det andra alternativet för att stänga en kanal. När du väljer detta alternativ kommer du att uppmanas att ange en wallet-adress till vilken Bitcoin-saldot på din kanal kommer att skickas. Observera att i det här alternativet kan du bara skanna QR-koden för den Bitcoin-adress som du vill stänga kanalen till. För närvarande finns det inget alternativ för manuell klistring av adressen.


👉 Klicka på det här alternativet, skanna Bitcoin-adressen och klicka på **Ok**. Kanalstängningen kommer att påbörjas och ditt Lightning Bitcoin-saldo kommer att skickas till den adress du skannade.


![scan_address_and_Ok](assets/en/031.webp)


**RECEIVE TO CHANNEL:** Detta är samma sak som att skapa en faktura, men i vissa fall kan du ha mer än en kanal, inklusive Fiat-kanaler (en unik typ av Lightning-kanal som kan erhållas i Valet wallet). Så om du har flera kanaler öppna säkerställer det här alternativet att du kan ta emot betalning till en specifik kanal.


** PÅFYLLNING FRÅN ANDRA KANALER:** Detta alternativ är en funktion som gör att du kan fylla på en kanal från andra befintliga kanaler. Om du t.ex. har två olika Lightning-kanaler (A och B) och Bitcoin-saldot på kanal A har tömts, kan du med det här alternativet enkelt och automatiskt fylla på saldot för kanal A från kanal B.


**DIRECT NOT PRIVATE RECEIVE:** Detta är också ett alternativ för att generera en faktura för att ta emot betalning, men när du använder det här alternativet betalar avsändaren dig direkt. Det innebär att betalningen inte hoppar genom olika noder innan den når dig, som en vanlig Lightning-betalning gör. Så i princip vet avsändaren att det är dig de betalat, känner till ditt kanal-ID osv. Det här alternativet kan ofta användas när du tar emot betalning från en källa som du litar på och inte behöver skydda din integritet.


## Hostade kanaler och Fiat-kanaler


Precis som många andra Bitcoin wallet är Valet en enkel, lätt Bitcoin och Lightning wallet. Men den har en unik Lightning-funktion som skiljer den från de flesta andra Bitcoin wallet. Den funktionen kallas **Hostade och Fiat-kanaler**.


Fiat-kanaler är en typ av Lightning-implementering som möjliggör enkel ombordstigning och användning av Lightning-nätverket. Det är en förvaringslösning som tillåter full anonymitet, precis som med en vanlig Lightning-kanal. Tekniken med Fiat-kanaler gör det också möjligt att skapa Bitcoin-derivat i Lightning-nätverket. Ett exempel är att med Fiat-kanaler kan handlare acceptera Bitcoin-betalningar med stabilt värde utan att oroa sig för Bitcoin:s volatilitet.


Den nuvarande implementeringen av Fiat-kanaler på Valet gör det möjligt att skapa stabila syntetiska Fiat-valutor som backas upp av Sats. Den använder ett värd-klient-förhållande där värden är en Lightning-nod som erbjuder denna tjänst och kunden är Valet-användaren. Det är en förvaringslösning eftersom alla Sats finns på värdens sida; fakturagenerering, tor-routing och preimage-generering sker dock fortfarande på klientsidan som i en vanlig Lightning-kanal.


Att öppna en Fiat-kanal tar samma process som att öppna en Lightning-kanal. Den enda betydande skillnaden är att i det här fallet behöver kunden (Valet-användaren) inte binda någon likviditet on-chain för att skapa kanalkapacitet. Värden ställer in kanalens kapacitet och dirigerar alla betalningar för kunden.


👉 För att öppna en Fiat-kanal, klicka på det lila **Lightning-kortet** på din wallet-hemsida. Välj **Scan Node QR** (Vid det här laget måste du ha identifierat en värd som du vill öppna en kanal till och fått nodens QR. Ett exempel på en värdnod som du kan öppna en Fiat-kanal till är SATM-noden i standard Sats)


**Attention:** Det är viktigt att notera att vem som helst kan vara en värd. Allt du behöver är att köra en Lightning-nod med **Fiat channel plugin** och en **Hedging-tjänst**. Fiat channels är ett öppen källkodsprojekt av *Standard Sats*. Läs mer om det [här](https://github.com/standardsats/fiat-channels-rfc) och [här](https://standardsats.github.io/).


SATM-noden QR nedan:


![SATM_node_QR](assets/en/032.webp)


👉 När du har skannat nodens QR klickar du på **Begära USD fiat-kanal** eller **Begära EUR fiat-kanal** (Detta är den fiat-denominering som dina Fiat-saldon kommer att noteras i). För tillfället väljer du USD och klickar på **OK**. Kanalen kommer att öppnas automatiskt och du kan börja ta emot Sats direkt. Du förstår, det är så enkelt!!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉 Gå till startsidan för din wallet, du kommer att se ett **ljusgrönt** kort märkt **USD**, det är din **Fiat-kanal**.


![fiat_channel_card](assets/en/035.webp)


**När du tar emot Sats på en Fiat-kanal kommer fiat-värdet av den Sats du tog emot att låsas in som en stabil balans, medan Sats-volymen flyter med Bitcoin-priset. Den här lösningen utformades främst för handlare som vill acceptera Sats för betalning men inte vill möta volatilitetsutmaningarna med Bitcoin. Detta hjälper dem att upprätthålla ett stabilt värde hela tiden, samtidigt som de fortfarande kan göra transaktioner i Lightning-nätverket och dra nytta av den globala räckvidden och snabba avvecklingen av Bitcoin som ett bytesmedel på Lightning Network.


När din Fiat-kanal skapas ser du följande Value-fält och vad vart och ett av dem betyder:


![fiat_channel_info](assets/en/036.webp)



- RANDOM SET OF NUMBERS SEPARATED BY DOTS:** Detta är nodernas IP-adresser. (IPV4 respektive IPV6)
- SERVER RATE:** Detta är Bitcoin-marknadspriset som värden erbjuder tjänsterna till dig. Detta kommer ofta att skilja sig något från det dominerande marknadspriset, eftersom en värd kan lägga till en liten premie. Det är helt upp till en värd att bestämma denna ränta; därför skulle detta också variera från värd till värd.
- FIAT BALANCE:** Detta är det låsta stabila fiat-värdet för varje sat du får på den här kanalen. Kom ihåg, som förklarats tidigare, när du tar emot Sats på din Fiat-kanal, låses fiat-värdet för Sats vid tidpunkten för mottagandet omedelbart in som ett syntetiskt stabilt fiat-värde i detta fält. Ditt **Fiat-saldo**-värde fluktuerar inte med marknadspriset för Bitcoin. När du vill göra betalningar från den här kanalen kan du bara skicka Sats-ekvivalenten av detta Fiat-saldo. Så tänk på detta som en digital fiatvaluta som backas upp av Sats.
- CAPACITY:** Detta är den totala volymen Sats som kan skickas och tas emot via denna kanal. (Detta ställs också in av värden. Och till skillnad från en vanlig Lightning-kanal kan denna kapacitet justeras av värden om så behövs)
- KAN SÄNDA:** Detta är volymen Sats som du kan skicka ut vid varje punkt baserat på ditt fiat-saldo. Detta skiljer sig helt från vad du har i en normal blixtkanal, eftersom detta värde flyter med Bitcoin-priset. Därför är det du ser här Sats-värdet av ditt Fiat-saldo när som helst baserat på ** Server Rate**.
- CAN RECEIVE:** Detta är det antal Sats som du kan ta emot till den här kanalen för tillfället. När du har skapat din kanal bör detta värde vara detsamma som kanalens kapacitet.
- VALUE IN FLIGHT:** När någon skickar sats till din kanal, eller när du försöker skicka sats till någon, och transaktionen av någon anledning blir försenad, visas det ofta i det här fältet.


Här är viktiga saker att notera om Fiat-kanaler:



- Till skillnad från en vanlig Lightning-kanal kan du omedelbart börja ta emot Sats när du öppnar en fiat-kanal, men du kan inte skicka. Du kan bara skicka ut Sats när du har tagit emot Sats.
- Vid alla tidpunkter är tillgången som skickas till och från Sats. *Fiat Balance* är bara en syntetisk IOU-representation av ett Bitcoin-värde som tas emot vid vilken tidpunkt som helst. Så det är inte en token-skapelse eller en ny kryptovaluta.
- Fiat-kanalen är mest användbar för handlare / företag som är skeptiska till att acceptera Bitcoin-betalningar på grund av oro för volatilitet. Det kan också vara användbart för företag som vill betala sina anställdas löner i Bitcoin utan att bära konsekvenserna av Bitcoin-volatilitet, vilket kan göra deras lönekapital instabilt. Det kan också vara användbart för individer som bor i ett område med övervägande Bitcoin-användning, men som har fasta levnadskostnader.
- Lägg märke till att det inte finns något fält som heter **REFUNDABLE**. Detta beror på att du tekniskt sett inte kan stänga en Fiat-kanal. Du kan bara sluta använda en Fiat-kanal genom att tömma dess saldo till din normala Lightning-kanal.


### Förklaring av alternativen för popup-fönster på din Fiat-kanal


När du trycker på din Fiat Lightning-kanal kommer följande fält att visas:


![fiat_channel_pop_up](assets/en/037.webp)


**SHARE HOSTED CHANNEL DETAILS:** Detta gör att du kan dela din Fiat-kanalinformation, till exempel fjärrpeer-ID, lokalt kanal-ID, datum för skapande etc.


**EXPORT CHANNEL STATE:** Detta gör att du kan exportera statusen för en kanal vid vilken tidpunkt som helst. Detta är vanligtvis användbart för att åtgärda kanalfel, och en värd kan be dig att dela detta om det finns ett behov av det.


**DRAIN CHANNEL BALANCE:** Som tidigare nämnts kan du tekniskt sett inte stänga en Fiat-kanal, men du kan dränera balansen i din kanal till din befintliga normala Lightning-kanal. Detta flyttar automatiskt Sat-ekvivalenten av ditt Fiat-saldo till din normala Lightning-kanal.


**RECEIVE TO CHANNEL:** Detta är samma sak som att generera en faktura, men i vissa fall kan en användare ha mer än en Fiat-kanal med olika värdar, inklusive normala Lightning-kanaler. Så om en användare har flera kanaler öppna säkerställer det här alternativet att de kan ta emot betalning till en specifik kanal.


** PÅFYLLNING FRÅN ANDRA KANALER:** Detta alternativ är en funktion som gör det möjligt för en användare att fylla på en kanal från andra befintliga kanaler. Så med det här alternativet kan du fylla på din Fiat-kanal från en normal kanal eller andra Fiat-kanaler du har, precis på samma sätt som du kan tömma.


**DIRECT NOT PRIVATE RECEIVE:** Detta är också ett alternativ för att generera en faktura för att ta emot betalning, men när du använder det här alternativet betalar avsändaren dig direkt. Det innebär att betalningen inte hoppar genom olika noder innan den når dig. Så i princip vet avsändaren att det är dig de betalat, känner till ditt kanal-ID osv. Det här alternativet kan ofta användas när du tar emot betalning från en källa som du litar på och inte behöver skydda din integritet.


## Valet inställningar:


Som alla andra applikationer har Valet appinställningar som du kan justera efter eget tycke och smak. Du kan komma åt inställningssidan från startskärmen.


👉 På startskärmen klickar du på ikonen **Gear** längst upp till höger på skärmen för att komma åt inställningarna. Nedan visas komponenterna i inställningsavsnittet.


![settings_icon](assets/en/038.webp)


**LOCAL CHANNEL BACKUP IS ENABLED:** Om detta annars är **Disabled,** bör du aktivera det eftersom det är det enda sättet du kan återställa dina normala blixtkanaler om du avinstallerar och installerar om Valet. Vi kommer att förklara detta senare. Så klicka på detta och ge Valet tillstånd till din ** medielagring** eftersom det är där säkerhetskopian sparas.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**VAR LÅGGER DU LOKALA BACKUP:** Så länge du gav Valet behörighet till din lagring kommer detta fält automatiskt att ställas in för att lagra lokala säkerhetskopior i din **Downloads**-mapp. Men du kan ändra det genom att klicka här och välja vilken mapp du vill.


**HANTERA KEDJEWALLETS** Detta är lite tekniskt, och du behöver inte bry dig om det om du inte är tillräckligt erfaren. Standardinställningen här är helt okej.


**ADD HARDWARE WALLET:** Du bör inte heller bry dig om detta, såvida du inte har en hårdvaru-wallet som du vill ansluta och övervaka. Med den här inställningen kan du skanna och ansluta din hårdvara wallet, t.ex. Trezor eller Cold-kort, och övervaka dess aktiviteter. Det här är en funktion för endast övervakning, vilket innebär att du inte kan utföra transaktioner på hårdvaran wallet härifrån. Du kan bara observera och övervaka wallet aktiviteter, saldon etc.


**SET CUSTOM ELECTRUM NODE:** Detta är också tekniskt, och om du inte är tillräckligt kunnig bör du inte bry dig om detta. Standardinställningen är tillräckligt bra.


**BITCOIN UNITS:** Det här är hur du vill att ditt Bitcoin-saldo ska visas. Det första alternativet visar ditt saldo i Satoshi-termer, t.ex. 1 000 000 Sats, medan det andra alternativet visar det i BTC decimaler. t.ex. 0,01BTC


**ANVÄND PIN-AUTENTIFIERING** Om du markerar den här rutan måste du ställa in en PIN-kod eller ett fingeravtryck som du måste använda för att logga in på din wallet och autentisera transaktioner.


**ANVÄND TOR-ANSLUTNING:** Om du markerar den här rutan kommer dina transaktioner att dirigeras via Tor-nätverket. Det ger ett extra lager av integritet men kan leda till försenad betalning, särskilt för Lightning-betalningar.


** VISA BIP39 ÅTERUPPRÄPARINGSFRAS:** Det är här du kan komma åt din 12-ords seed-fras för säkerhetskopiering. Så om du inte skrev ner det tidigare, eller om du inte kan hitta var du skrev ner det, så länge du fortfarande har tillgång till din Wallet, kan du kopiera den härifrån.


**USAGE STATISTICS:** Här visas en sammanfattning av alla dina transaktioner och aktiviteter sedan wallet skapades


![usage_stats](assets/en/041.webp)


## Wallet Återvinning


Valet är en icke-förvarad wallet, så om du tappar bort din enhet eller avinstallerar din wallet-app måste du göra en wallet-återställning för att få tillbaka dina Bitcoin och Lightning-kanaler. I början av denna handledning nämnde vi vikten av att skriva ner din **12-ords seed-fras** eftersom det är nyckeln till att återställa din wallet. Det finns inga kundtjänstrepresentanter som kan hjälpa dig att komma tillbaka till din wallet.


Det finns två viktiga verktyg som behövs för att återställa din Valet wallet, beroende på om du hade en aktiv Lightning-kanal eller inte. För en användare som inte hade en aktiv normal Lightning-kanal är allt de behöver deras **12-ords seed-fras**, genom att följa de enkla stegen nedan:


👉 Installera en ny Valet-app och starta/starta appen.


👉 Välj **Återställ befintlig Wallet**


![restore_existing_wallet](assets/en/042.webp)


👉 Välj ** Endast återställningsfras**.


![select_recovery_phrase](assets/en/043.webp)


👉 Ange din 12-ords återhämtningsfras och klicka på **OK**.


![input_12_words](assets/en/044.webp)


Din wallet kommer att återställas. I detta fall kommer endast ditt saldo för on-chain Bitcoin att återställas.


Men om du hade en aktiv normal blixtkanal och du återställer din wallet med endast återställningsfrasen, kommer din blixtkanal att tvingas stängas, och allt Bitcoin-saldo du har på det kommer automatiskt att skickas till ditt on-chain-saldo.


Det andra sättet att återställa din Valet wallet, särskilt om du hade en normal Lightning-kanal öppen innan du avinstallerade Valet, är att ** använda den lokala säkerhetskopieringsfilen som sparats på din enhet, tillsammans med din 12-ords seed-fras **. Om du använder dessa två kommer ditt blixtkanaltillstånd att återställas, varför din blixtkanal inte kommer att tvingas stängas.


Så här går du tillväga:


👉 Installera en ny Valet-app och starta/starta appen.


👉 Välj **Restore Existing Wallet**.


👉 Välj **Backup + Återställningsfras**.


![select_backup_and_recovery_seed](assets/en/045.webp)


👉 Välj Backup-filen från telefonens filhanterare. (Den lagras alltid i din **Downloads**-mapp som standard.)


![local_backup_file_in_download_folder](assets/en/046.webp)


När rätt backupfil har valts visas en prompt som bekräftar att en **"Backupfil finns"** och du ombeds sedan att ange din seed-fras på 12 ord.


![enter_12_words](assets/en/047.webp)


👉 Ange din återställningsfras på 12 ord och klicka på **OK**. Du kommer att tas till din wallet-hemsida.


👉 Vänta på att Bitcoin-nätverkssynkroniseringen (**SYNC**) och Lightning-nodsynkroniseringen (**LN Sync**) ska slutföras, och din wallet kommer att återställas helt, inklusive dina Lightning-kanaler.


![LN_sync](assets/en/048.webp)


## Slutsats


Valet är en spännande wallet-lösning med funktioner som gör den lämplig för onboarding av nya användare. Den har också en Fiat-kanal, en inte helt ny teknik som säkerställer integration av fiat-drivna företag på Bitcoin-standarden.


Ladda ner Valet idag och ge det ett försök !!! 🧡