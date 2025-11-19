---
name: Braiins Pool

description: Introduktion till Braiins Pool
---

![signup](assets/cover.webp)


Braiins Pool, tidigare känd som Slush Pool, är den allra första Bitcoin Mining pool. Den grundades i november 2010 och utvann sitt första block den 16 december 2010, block 97834.


I maj 2024 har Braiins Pool en datorkraft på 13 EH/s, vilket motsvarar cirka 1,8% av den totala Bitcoin Hashrate. Den har utvunnit totalt 1 307 188 bitcoins, vilket är cirka 6% av de maximala 21 miljoner bitcoins som någonsin kommer att existera.


### Ersättningssystem


Sedan slutet av 2023 har Braiins Pool ändrat sitt ersättningssystem till att anta FPPS-systemet (Full Pay Per Share). Det innebär att gruvarbetare får belöningar varje dag för allt sitt arbete från föregående dag, även om poolen inte hittade ett block. Detta skiljer sig från det gamla systemet där gruvarbetarna endast fick en belöning när poolen hittade ett block.


** Det är värt att notera, [enligt en tweet av Mononaut] (https://x.com/mononautical/status/1777686545715089605) som analyserar Bitcoin TimeChain, att många Mining-pooler som använder FPPS-systemet skulle skicka de utvunna bitcoins till en Address av AntPool, vilket skulle innebära att AntPool kontrollerar Hashrate för alla dessa pooler, cirka 47% av den globala Bitcoin Hashrate. Detta är mycket dåliga nyheter för decentraliseringen av nätverket.**


### Poolavgifter


Avgifterna för Braiins Pool är 2,5%, men om du använder BraiinsOS på dina maskiner kommer avgifterna att vara 0%


### Uttag av pengar


**Blixtrande uttag**

Med Lightning withdrawals kan du ta ut dina belöningar utan minimibelopp en gång om dagen via en Lightning Address.

För att använda den här metoden måste du ha en Wallet som är kompatibel med Lightning-adresser.


**On-Chain Uttag**

On-Chain-uttag är begränsade till ett minimibelopp och kan vara föremål för avgifter.

Lägsta belopp: 20 000 Sats

Avgifter: 10.000 Sats för belopp under 500.000 Sats

Gratis för belopp över 500.000 Sats

Uttag kan utlösas av tidsintervall eller av belopp.


## Skapande av konto


För att börja använda Braiins Pool [gå till deras webbplats](https://braiins.com/pool) och klicka på "SIGN UP" längst upp till höger



![signup](assets/3.webp)


Ange dina uppgifter och validera, du kommer sedan att få ett e-postmeddelande med en begäran om bekräftelse av din Address. Bekräfta med länken i e-postmeddelandet du fick och logga sedan in på plattformen


![signup](assets/4.webp)



## Lägga till en "arbetare"

En arbetare är den Miner som du kommer att ansluta till poolen. För att lägga till en ny Miner klickar du på "Workers" i menyn till vänster.

![signup](assets/7.webp)


Klicka sedan på den lila knappen "Connect Workers +".


I det här fönstret väljer du ditt geografiska område.


Om den Miner som du vill ansluta använder BraiinsOS väljer du protokollet "Stratum V2". I annat fall väljer du "Stratum V1".


![signup](assets/8.webp)


Du kommer att ha informationen att ange på din Miner:s webbsida (se din Miner:s dokumentation för att veta var du ska ange denna information).


Här är **"stratum+tcp://eu.stratum.braiins.com:3333"** poolens URL.


**JimZap.workerName** är din identifierare och namnet på din Miner, där JimZap är identifieraren och .workerName är namnet på Miner. Om du har flera gruvarbetare kan du antingen ge dem samma namn, i vilket fall deras datorkraft kommer att läggas ihop på instrumentpanelen, eller ge dem olika namn för att övervaka dem individuellt.


Och lösenordet är alltid detsamma **"anything123"**


När du har angett denna information på din Miner:s webbsida och den har startat Mining, kommer du att se den visas efter några minuter på Braiins Pool Dashboard.


## Översikt över instrumentpanelen


![signup](assets/9.webp)


I den övre bannern kan du se den genomsnittliga totala Hashrate för alla dina miners under 5 minuter, 1 timme och 24 timmar. Och en sammanfattning av antalet gruvarbetare online eller offline.

Nedan finns ett diagram som gör det möjligt att följa utvecklingen av din datorkraft.


![signup](assets/10.webp)


Under detta diagram har du flera olika typer av information om dina belöningar i Sats.


**"Dagens Mining-belöningar"** Anger antalet Sats som du har utvunnit idag. I slutet av dagen kommer detta värde att återställas till 0 och Sats kommer att skickas till ditt konto.


**"Yesterday's Total Reward"** Antalet Sats som du utvann dagen innan


**"Est. Profitability (1 TH/s)"** Är en uppskattning av antalet Sats som du tjänar på en dag för en datorkraft på 1 TH/s. Om värdet t.ex. är 77 Sats och du har en datorkraft på 10 TH/s kontinuerligt under hela dagen, skulle du teoretiskt tjäna 77 x 10 = 770 Sats per dag.


**"All Time Reward"** Det totala antalet Sats som du har utvunnit med Braiins Pool


**"Belöningssystem"** Den avgiftssats som tillämpas av poolen


**"Next Payout ETA"** Uppskattning av den tid det tar innan du kan ta ut Sats från plattformen. Här visar uppskattningen ingenting eftersom Mining bara har varit på gång i några minuter.


**"Kontosaldo"** Antalet Sats som finns tillgängliga på ditt konto och som du sedan kan ta ut.

## Konfigurera uttag

Du kan ta ut dina belöningar antingen On-Chain eller via blixt med en Address.


Klicka på "Fonder" högst upp på sidan. Som standard har du ett "Bitcoin-konto". Du kan skapa andra för att dela belöningarna. Vi återkommer till detta i nästa avsnitt.


För tillfället klickar du på "Set up".


![signup](assets/17.webp)


I det nya fönstret kan du välja "Onchain-utbetalning".


Namnge denna Wallet, ange en BTC Address och välj vilken typ av trigger du vill ha. "Threshold" innebär att betalningen utlöses när du har samlat en viss mängd BTC, och med "Time interval" utlöses betalningen med regelbundna intervall (dag/vecka/månad).


Observera att minimibeloppet är 0,0002 BTC och att under 0,005 BTC kommer en avgift på 0,0001 BTC att tillämpas.


![signup](assets/18.webp)


Om du vill använda Lightning-uttag behöver du en Wallet som tillhandahåller en Lightning Address. Du kan till exempel använda getAlby.


Klicka på "Blixtsnabb utbetalning" högst upp i fönstret.


Ange din Lightning Address och kryssa i rutan "Jag förstår..." och bekräfta sedan.


Med denna uttagsmetod kommer dina belöningar att skickas till din Wallet varje dag.


![signup](assets/14.webp)


När du har validerat dina utbetalningsinställningar får du ett bekräftelsemeddelande.


![signup](assets/15.webp)


## Delning av belöningar


Med Braiins Pool kan du också dela dina belöningar mellan flera plånböcker.


För att göra detta klickar du högst upp på "Mining" och sedan till vänster på "Inställningar".


![signup](assets/19.webp)


På denna sida kommer du att kunna lägga till andra "Finansiella konton" genom att klicka på "Lägg till ett annat finansiellt konto" och fördela dina belöningar i % över dessa olika konton som du måste koppla en Wallet till. För att associera en ny Wallet med ett finansiellt konto, se föregående avsnitt.