---
name: Ocean Mining

description: Introduktion till Ocean Mining
---

![signup](assets/cover.webp)


**Maj 2024**


Ocean Mining är en något unik Mining pool. Här krävs inga konton, inga e-postadresser, inga lösenord. Precis som i Bitcoin är allt transparent, pseudonymt, och bidragsgivarna kan välja mellan fyra olika blockmallar.


### Ersättningssystem


Ocean har ett ersättningssystem som kallas TIDES, "Transparent Index of Distinct Extended Shares". Detta system registrerar det arbete som utförs av gruvarbetarna, så kallade "shares". Poolen beräknar procentandelen "aktier" för varje bidragsgivare och lägger sedan till deras Bitcoin Address i poolens blockmall som mottagare av denna procentandel av Block reward.


Blockmallen uppdateras ungefär var 10:e sekund för att ta hänsyn till de mest lukrativa nya transaktionerna och för att ändra fördelningen av Block reward om det behövs.


![signup](assets/rem.webp)


Det spelar ingen roll om dina maskiner är anslutna eller inte vid den tidpunkt då poolen hittar ett nytt block. Det arbete som redan har skickats in sparas för de kommande åtta blocken som poolen hittar.


Att behålla arbetet för åtta block istället för att nollställa räknarna för varje nytt block som bryts innebär att din ersättning blir 100% först när poolen har hittat åtta block efter att du började bidra. Det innebär också att du fortsätter att få ersättning för åtta block om du slutar att bidra till poolen.


Denna mekanism jämnar ut ersättningen och motverkar "poolhopping", vilket innebär att man regelbundet byter pool beroende på vilken som har störst sannolikhet att hitta nästa block.


### Uttag av pengar


Driften av Ocean Mining gör det möjligt för dess bidragsgivare att återvinna "rena" bitcoins, vilket innebär bitcoins som direkt utfärdas av Block reward.


Till skillnad från de flesta andra pooler tar Ocean inte emot de nyligen utvunna bitcoins; bidragsgivarnas adresser är direkt integrerade i blockmallen.


För närvarande är minimibeloppet för att verkligen dra nytta av de rena bitcoins 1 048 576 Sats. För varje block som bryts av poolen måste din andel av "aktier" ge dig rätt till mer än 1 048 576 Sats för att de ska betalas direkt till dig av Block reward.

Annars behålls dina Sats av Ocean tills dina totala belöningar överstiger detta belopp.


Alla bitcoins som tillfälligt förvaras av Ocean finns på denna Address: [37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n, allt är verifierbart på TimeChain.](https://Mempool.space/Address/37dvwZZoT3D7RXpTCpN2yKzMmNs2i2Fd1n)

Det är också möjligt att ta ut dina Sats via Lightning med hjälp av BOLT12. Vi kommer att se hur man ställer in detta.


### Poolavgifter


Avgifterna varierar från 0% till 2% beroende på vilken blockmall som väljs.


## Havets genomskinlighet


### Data om bidragsgivare


![signup](assets/1.webp)


All information om poolen är transparent, inklusive alla användardata. Låt oss ta ett exempel för att förstå den här punkten:


[På Ocean-instrumentpanelen] (https://ocean.xyz/dashboard) har du många informationsbitar som Hashrate under de senaste sex månaderna, antalet deltagare i poolen, det totala antalet bitcoins som utvunnits etc.


Vi kommer att fokusera på avsnittet "Contributors". Du kan se listan över alla bidragsgivare med deras genomsnittliga Hashrate under de senaste tre timmarna samt andelen **"aktier"** och **"Hash"** i förhållande till resten av poolen.


**"Shares %"** är den procentuella andelen av arbetet som tillhandahållits av bidragsgivaren i fönstret för de senaste åtta blocken jämfört med resten av poolen.


**"Hash %"** är procentandelen av den genomsnittliga Hashrate som tillhandahållits av bidragsgivaren under de senaste tre timmarna jämfört med resten av poolen.


![signup](assets/2.webp)


Du kommer att märka att "bidragsgivarna" identifieras med en Bitcoin Address. Du kan klicka på någon av dessa adresser för mer information.


Om vi tar den första, den med den högsta Hashrate [1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ](https://ocean.xyz/stats/1GRfspGGx4Ne66YotWuosUc4WeJLfGE3dZ), kan du se alla detaljer om den här användaren: Hashrate, antal bitcoins som utvunnits, med vilket block och till och med detaljerna för var och en av deras maskiner (ASIC). De förblir dock anonyma, som på Bitcoin.


### Blockmall


Längst upp till vänster på instrumentpanelen har du "Nästa block". På den här sidan finns det fyra olika blockmallar. Ocean låter varje bidragsgivare välja vilken blockmall de vill stödja. Detta har ingen direkt inverkan på din ersättning. När poolen minerar ett block kompenseras alla bidragsgivare oavsett vilken mall de har valt. Detta gör det helt enkelt möjligt för alla att "rösta" på den blockmall som passar dem.


![signup](assets/3.webp)


**CORE:** Avgift 2%, detta är den klassiska Bitcoin Core-mallen utan filter, som skrivet på deras sida "Inkluderar transaktioner och majoriteten av skräppost"


**CORE+ANTISPAM:** Avgift 0%, Bitcoin Core med ett filter mot vissa transaktioner som Ordinals "Inkluderar transaktioner och begränsar spam"


**OCEAN:** Avgift 0%, Bitcoin Knot "Inkluderar endast transaktioner och rimligt små data"


**DATA-FREE:** Avgift 0%, Bitcoin Knot "Inkluderar endast transaktioner utan godtyckliga data"


### Skillnad mellan Bitcoin Core och Bitcoin Knot

Bitcoin Core är den programvara som gör det möjligt för cirka 99 % av Bitcoin-noderna runt om i världen att fungera. Bitcoin är ett protokoll, vilket innebär att det, precis som på Internet där det finns flera olika webbläsare, kan finnas flera olika programvaror som samsas om samma TimeChain. Av kompatibilitetsskäl och för att begränsa risken för buggar som skulle lämna outplånliga spår i TimeChain arbetar dock nästan alla Bitcoin-utvecklare med Bitcoin Core. Bitcoin Knots är en Fork av Bitcoin Core, vilket innebär att den delar majoriteten av sin kod, vilket kraftigt begränsar risken för buggar. Denna Fork skapades av Luke Dashjr, som ville tillämpa mer restriktiva regler än Bitcoin Core utan att skapa en Hard Fork. Nu samexisterar Bitcoin Core och Bitcoin Knots tack vare Nakamotos konsensus.


## Lägga till en arbetare


För att lägga till en arbetare börjar du med att välja din blockmall. Detta val avgör vilken pool-URL som ska anges på dina Miner (ASIC).



- CORE**: `stratum+tcp://core.mine.ocean.xyz:3202`
- CORE+ANTISPAM**: `stratum+tcp://ordis.mine.ocean.xyz:3303`
- OCEAN**: `stratum+tcp://mine.ocean.xyz:3334`
- DATA-FREE**: `stratum+tcp://datafree.mine.ocean.xyz:3404``


Därefter, för användarfältet, ange en Bitcoin Address som du äger. Här är listan över kompatibla Address-typer:


- P2PKH** (Ursprunglig Address-typ. Börjar med "1")
- P2SH** (Multisignatur eller P2SH-SegWit. Börjar med "3")
- Bech32** (SegWit. Börjar med "bc".)
- Bech32m** (Taproot. Börjar på "bc". Längre än Bech32.)


Om du har flera gruvarbetare kan du ange samma Address för dem alla, så att deras Hash-priser kombineras och visas som en enda Miner. Du kan också skilja dem åt genom att lägga till ett distinkt namn för var och en. För att göra detta lägger du bara till ".workername" efter Bitcoin Address.


Slutligen, för lösenordsfältet, använd `x`.


**Exempel:**

Om du väljer mallen **OCEAN**, din Bitcoin Address är `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv` och du vill döpa din Miner till "Brrrr", måste du ange följande information i din Miner:s Interface:



- URL**: `stratum+tcp://mine.ocean.xyz:3334`
- ANVÄNDARE**: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr`
- LÖSENORD**: `x`


Några minuter efter att du har startat Mining kommer du att kunna se dina data på Ocean-webbplatsen genom att söka efter din Address.


### Översikt över instrumentpanelen


- Aktier i belöningsfönstret**: Dessa data anger antalet andelar, det arbete du har skickat till poolen i fönstret för de senaste 8 blocken som poolen har utvunnit.
- Beräknade belöningar i Windows**: Uppskattning av antalet Sats som du kommer att tjäna med det arbete som redan utförts. Detta tar inte hänsyn till transaktionsavgifter, utan endast coinbase, de nya bitcoins som utfärdas av nätverket.
- Beräknad intjäning nästa block**: Uppskattning av antalet Sats som tjänas in om ett block bryts nu. Kom ihåg att om detta värde är mindre än 1 048 576 Sats kommer du inte att få Sats direkt till din Address. De kommer att skickas till Ocean's Address tills dina intäkter överstiger detta tröskelvärde.


Nedan visas en graf som visar din Hashrate-historik upp till 6 månader.


![signup](assets/4.webp)


Här har du din genomsnittliga Hashrate över olika tidsskalor, från 60s till 24h, samt historiken för block som utvunnits av poolen för vilka du har bidragit och blivit belönad.


![signup](assets/5.webp)


Du har möjlighet att exportera en CSV-fil av denna historik med knappen **Download CSV**.


![signup](assets/6.webp)


I följande avsnitt har du en lista över alla gruvarbetare som du har anslutit till poolen med denna Address. Du har naturligtvis deras individuella Hashrate, men också antalet Sats som de individuellt har fått för sitt arbete.


![signup](assets/7.webp)


Du kan klicka på **Nickname** för vilken Miner som helst. Du kommer då att få all den information vi just såg, men specifikt för den Miner.


Längst ner på sidan finns ytterligare information där du kan se betalningshistoriken för din Address, de Sats som du har utvunnit men ännu inte har betalats för och det totala antalet Sats som du har utvunnit.


![signup](assets/8.webp)


Här kan du se att det i rutan ** Uppskattad tid fram till minsta utbetalning** står Blixten eftersom vi har skapat ett BOLT12-erbjudande.


### Konfigurera blixtuttag


Som du har förstått syftar Ocean till att maximera transparensen och minimera förvaringen (att hålla din Sats för din räkning).


Det är därför det är nödvändigt att använda **BOLT12-erbjudanden** för blixtuttag. Detta är ett nytt sätt att göra en betalning på Lightning Network som börjar dyka upp 2024 och möjliggör flera saker:


- Det är en återanvändbar betalningslänk som möjliggör automatiska betalningar och till skillnad från en Lightning Address är BOLT12 inte frihetsberövande.
- Det är också en betalningsmetod som ger bevis för att betalningen har gjorts, vilket inte är fallet med LNURL:er.
- Mycket viktigt är att den kan användas tillsammans med en Bitcoin-signatur för att bevisa att du både är innehavare av BTC Address och BOLT12-erbjudandet.

Idag (maj 2024) finns det få lösningar för att använda den här metoden. I detta exempel kommer vi att använda en Start9-server med Core Lightning. När andra verktyg, som till exempel Phoenix Wallet, har integrerade BOLT12-erbjudanden kommer denna handledning att förbli tillämplig. Se till att du har öppna kanaler med inkommande likviditet, annars kommer betalningarna inte att fungera.


Börja med att gå till din instrumentpanel på Ocean-webbplatsen genom att ange din BTC Address och klicka sedan på fliken **Konfiguration**.


![signup](assets/9.webp)


Vi kopierar texten **Description** hit:

`OCEAN-utbetalningar för bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`


Gå nu till din Core Lightning Interface på din Start9-server (eller någon Wallet som kan tillhandahålla ett BOLT12-erbjudande).


![signup](assets/10.webp)


Klicka på **Receive**.


Markera **Offer** och klistra sedan in den tidigare kopierade texten i fältet **Description** och lämna fältet **Amount** tomt.


![signup](assets/11.webp)


Klicka på **generate Erbjudande**.


![signup](assets/12.webp)


Du har skapat en återanvändbar och permanent betalningslänk som inte kräver en central server, vilket är fallet med blixtadresser. Kopiera länken och gå sedan tillbaka till Ocean-sidan.


I fältet **Lightning BOLT12 Offer** klistrar du in betalningslänken och lämnar fältet **Block Height** till sitt standardvärde. Klicka på **generate**.


![signup](assets/13.webp)


För att Ocean ska kunna säkerställa att den här betalningslänken verkligen är din utan att använda ett kontosystem måste du signera meddelandet som just har genererats med din privata nyckel som motsvarar den Bitcoin Address du använder. Det finns många lösningar för att signera ett meddelande med din privata nyckel. I den här handledningen kommer vi att ta exemplet med BlueWallet, men metoden är densamma för alla plånböcker.


![signup](assets/14.webp)


Förutsatt att din privata nyckel finns i BlueWallet (du kan göra samma sak med en Hardware Wallet), klicka på den berörda Wallet.


![signup](assets/15.webp)


Klicka sedan på **...** längst upp till höger.


![signup](assets/15bis.webp)


Och **Signera/Verifiera meddelande**.


![signup](assets/16.webp)


I detta fönster har du tre fält: **Address**, **Signatur** och **Meddelande**.


I fältet **Address** skriver du in din Bitcoin Address. Om vi går tillbaka till vårt exempel är det Address: `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`.


Lämna fältet **Signatur** tomt.

Och klistra in det genererade meddelandet i fältet **Message** på Oceans sida: `{"height":845900,"lightning_bolt12":"lno1pg7y7s69g98zq5rp09hh2arnypnx7u3qvf3nzufjv4jrs7ncwyuxu6n3wdaxu6msxank5wp5dcc8samv89j8qv3jx36kscfjvempvggz84uzkn26vyzq8y2mr2s8fv0j76wesq43dz72kqrk33nl2tk9j45s"}`

Klicka på **Sign**.


Detta kommer att generate en kryptografisk signatur som bevisar att du är ägare till Address `bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv`, och denna signatur är unik tack vare meddelandet från Ocean, genererat från BOLT12-betalningslänken.


![signup](assets/17.webp)


Kopiera signaturen och klistra in den på Ocean's sida, klicka sedan på **CONFIRM**.


![signup](assets/18.webp)


Du bör se ett bekräftelsemeddelande.


![signup](assets/19.webp)


Gå nu till fliken **Min statistik**. Ytterligare information visas högst upp med betalningslänken BOLT12 som du tidigare genererade med Core Lightning på Start9.


![signup](assets/20.webp)