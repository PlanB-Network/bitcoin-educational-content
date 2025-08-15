---
name: Mini Miner Braiins
description: Gör Mining enkelt från hemmet.
---
![cover](assets/cover.webp)



### Inledning



Mini Miner Braiins BMM 100 är en produkt skapad av Mining pool Braiins. Denna enhet har en attraktiv design och är extremt tyst. Den producerar 1,1 Th/s datorkraft och förbrukar cirka 40 watt. Till skillnad från andra enheter är den inte öppen källkod, men den är väldigt lätt att installera, det tar verkligen bara några klick! Mini Miner BMM 100 är den första versionen som släpptes. Nu är version 2 i produktion, kallad BMM 101, som skiljer sig från den första genom att ha en större skärm och närvaron av Wi-Fi, men installationsprocedurerna är desamma.



Du kan också hitta mycket mer viktig information genom att läsa den fullständiga handboken direkt på [tillverkarens webbplats] (https://braiins.com/hardware/mini-Miner-bmm-100).



### Översikt över BMM 100



enheten ser ut som en parallellpiped med en skärm på framsidan



![image](assets/en/01.webp)



en fläkt på den övre sidan



![image](assets/en/02.webp)



och på baksidan finns: hålet för strömmen, plats för ett SD-kort (som kan behövas för eventuella uppdateringar), en liten knapp med texten "IP REPORT" som visar mini Miner:s IP Address, vilken Address som behövs för att komma åt enhetens instrumentpanel. När du trycker på knappen visas IP Address i ca 5 sekunder, sedan försvinner den och den inställda skärmen visas igen. Men om du behöver ändra några inställningar är det bara att trycka på knappen i fråga igen så visas IP Address på skärmen igen. Fortsätter vi med listan hittar vi en Ethernet-port och en åtkomst för att utföra en enhetsåterställning, för vilken du måste ta tag i en stift och hålla i 10 sekunder för att återställa alla inställningar för mini Miner. Slutligen hittar vi två indikatorlampor, en Green och en röd, som indikerar Miner:s status för oss.



![image](assets/en/03.webp)



### Anslutning av Mini Miner



Du måste ansluta enheten till internet via ethernet, men notera att detta inte längre är nödvändigt med den nya versionen (BMM 101). Tillbaka till denna mini Miner, när vi har lokaliserat platsen måste vi först ansluta den till internetlinjen och sedan till strömmen: enheten slås på automatiskt och visar sin IP Address på skärmen.



### Konfiguration



Vi måste öppna en webbläsare och ange IP Address som visar oss mini Miner i sökfältet. Jag påminner dig om att för att hitta enheten i nätverket måste du vara lokal, så du måste ha den dator du använder ansluten till samma nätverk som mini Miner. när vi anger IP Address trycker vi på enter och inloggningssidan till mini Miner: s operativsystem, som är Braiins OS, kommer att visas på skärmen.



![image](assets/en/06.webp)



För att logga in måste du ange `root` som ditt användarnamn, medan du kan lämna lösenordet tomt. Klicka på login och din mini Miner instrumentpanel kommer att visas.



![image](assets/en/07.webp)



### Allmänna inställningar



Låt oss gå till System



![image](assets/en/24.webp)



i inställningarna hittar vi några allmänna inställningar som tema (ljust eller mörkt), språk, tidszon och lösenordsbyte.



![image](assets/en/25.webp)



Om vi går till "Mini Miner Screen" istället har vi inställningarna för vår mini Miner, till exempel skärmvisningen. Vi kan välja om vi vill visa tiden eller priset på Bitcoin, eller skärmen med maskinens statusinformation som produkt Hash, temperatur, förbrukade watt och så vidare. Här är det upp till dig att välja vad du vill se på skärmen; vi kan också ändra ljusstyrkan på skärmen, ställa in nattläget och visa tiden med 12-timmars eller 24-timmarsformat.



![image](assets/en/26.webp)



När du har gjort ändringarna klickar du på `Spara ändringar` så ser du ändringarna på din enhets skärm



![image](assets/en/27.webp)



### Anslutning till Mining pool



Nu är vi ännu inte i drift, eftersom vi måste ansluta till en pool för att starta Mining, så vi måste gå till "Konfiguration"



![image](assets/en/08.webp)



och den första posten är bara `Pools`.



![image](assets/en/09.webp)



Här måste vi bestämma vilken pool vi ska använda. I den här handledningen kommer jag att visa dig två alternativ. Det första är att ansluta oss till Mining pool Braiins som också används av professionella gruvarbetare, som du kan se från den här handledningen:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Det andra alternativet är att ansluta oss till en Mining pool som mina i solo, som Public Pool, följ den här guiden för att göra det:



https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

#### Braiins pool



För att ansluta till den här poolen måste vi skapa ett konto. den här poolen gör också betalningar med Lightning Network, så vi kommer att kunna få några Sats per dag. För att göra detta måste vi skapa en Address blixt som vi kan ta emot belöningarna på. Om du inte vet hur du skapar ett konto på braiins pool eller hur du ställer in din Address-blixt kan du följa den här guiden:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

När det är gjort är vi i Braiins poolinstrumentpanel. Vad vi måste göra är att berätta för poolen att vi vill ansluta till en av våra gruvarbetare, så på vänster sida av skärmen hittar du ett antal poster. Vi måste gå till "arbetare"



![image](assets/en/04.webp)



och vi måste klicka på den lila knappen till höger som säger "Connect workers."



![image](assets/en/05.webp)



Här kommer fönstret med den information vi behöver för att ansluta vår mini Miner till poolen. Här är den enda ändringen vi kan göra att välja Stratum V2. För att ta reda på vad Stratum v2 är, se denna post i [ordlistan] (https://planb.network/en/resources/glossary/stratum-v2).



![image](assets/en/10.webp)



Nu behöver vi kopiera den här strängen som börjar med stratumv2. Så vi klickar på den lilla "kopiera" -symbolen, sedan går vi till instrumentpanelen för vår mini Miner som vi hade kvar i konfiguration och pooler. Vi klickar på lägg till ny pool



![image](assets/en/11.webp)



och klistra in den sträng vi kopierade i utrymmet under Pool URL.



![image](assets/en/12.webp)



Nu måste vi lägga till användarnamn och lösenord. Låt oss gå tillbaka till poolens dashboad. Därunder har vi också ett användarID och lösenord. Användar-ID och vårt användarnamn, det vi gav när vi skapade kontot, plus namnet på Miner som vi vill lägga in. du kan välja om du vill ge ett namn till enheten du ansluter till poolen eller inte, det är valfritt, men det är tillrådligt att lägga in det, så om du ansluter flera enheter blir det lättare att identifiera dem direkt. Om du inte vill ange något istället kan du lämna `workerName`.



![image](assets/en/13.webp)



Vi går sedan till vår mini Miner och skriver in användarnamnet. Här kommer vi att ange i mitt fall "finalstepbitcoin" som är mitt användarID, miniminer dot. Detta är det namn jag bestämde mig för att ge enheten. Om du inte vill namnge det skriver du bara userid dot workername. I mitt fall skulle det vara finalstepbitcoin.workername. När du har angett användarnamnet kan du välja ett lösenord och skriva det i det tomma fältet. Du kan också lägga till anithing123, vilket är det som också visas på poolskärmen, men det vill helt enkelt indikera att du kan lägga till vilket lösenord du vill.



När du har matat in alla data måste du trycka på spara-knappen till höger (den som är formad som en diskett) och på så sätt har du konfigurerat pooldata i mini Miner.



![image](assets/en/14.webp)



Nu måste du gå tillbaka till poolens instrumentpanel och klicka på "Ansluten! Gå tillbaka."



![image](assets/en/15.webp)



Vi har anslutit vår mini Miner till braiins pool! Du kan nu se den i listan över arbetare. Om den inte dyker upp gör du en uppdatering och väntar en stund. När den dyker upp, kontrollera att den har statusen "OK" med en Green bockmarkering.



![image](assets/en/17.webp)



om du går tillbaka till instrumentpanelen bör du börja se rörelse i diagrammet och se Hashrate för vår enhet. Detta innebär att poolen tar emot vårt arbete och därför underminerar vi i alla avseenden och syften.



![image](assets/en/16.webp)



#### Allmän pool



Genom denna pool kan man pröva lyckan och bryta ensam, lutad mot en pool. I detta fall kommer vi inte att få någon belöning, men vi kommer att få full belöning om vi någonsin lyckas bryta ett block. Vi kommer sedan att länka till public pool, en Mining-pool som är helt öppen källkod. Vi öppnar ett nytt fönster i webbläsaren och går till [web.public-pool.io] (https://web.public-pool.io/#/).



![image](assets/en/18.webp)



där finns en sida med all information vi behöver. Vi kopierar sedan dit stratumet Address



![image](assets/en/19.webp)



sedan går vi tillbaka till instrumentpanelen för vår mini Miner, går till konfiguration och till pooler, klickar på lägg till ny pool (samma process som ovan) och klistrar in "stratum Address under pool url.



![image](assets/en/20.webp)



Låt oss nu gå tillbaka till poolsidan och se att som användarnamn måste vi ange en Bitcoin Address, som kommer att vara den som vi kommer att få belöningen om vi undergräver ett block, sedan en punkt och sedan namnet på vår enhet, som vi gjorde tidigare med Braiins Pool, medan lösenordet vi kan välja själva.



![image](assets/en/21.webp)



Vi går tillbaka till mini Miner och under användarnamn klistrar vi in en Address Bitcoin följt av punkt och namnet, jag kommer att skriva `miniminer`. I lösenordet sätter jag istället test, du skriver vad du vill.



![image](assets/en/22.webp)



Nu sparar vi inställningarna och avaktiverar Braiins pool.



![image](assets/en/23.webp)



Bra! Vi är nu Mining på allmän pool!



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)