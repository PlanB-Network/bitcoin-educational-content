---
name: Public Pool
description: Introduktion till Public Pool
---

![signup](assets/cover.webp)


**Public Pool** är inte vilken pool som helst; det är vad som också kallas en **Solo Pool**. Om din Miner lyckas med Mining i ett block samlar du in hela Block reward, som inte delas med andra deltagare i poolen eller med poolen själv.


**Public Pool** tillhandahåller endast en **blockmall** för din Miner så att den kan utföra sin uppgift utan att du behöver ha en **Bitcoin-nod** och den programvara som kommunicerar med din Miner. Eftersom du inte poolar din datorkraft med andra deltagares är dina chanser att lyckas med Mining ett block uppenbarligen mycket låga, vilket liknar något av ett lotterisystem, där ibland en lycklig individ vinner jackpotten.


![signup](assets/1.webp)


På **Dashboard** för **Public Pool** har du fortfarande viss statistik som poolens **Total Hashrate** samt en fördelning av de olika typerna av gruvarbetare som är anslutna till poolen.


![signup](assets/2.webp)


På de första raderna kan vi se **Bitaxe** med 1323 **Bitaxe** anslutna för totalt 649TH/s. **Bitaxe** är ett **Open source**-projekt som gör det möjligt att enkelt återanvända ett chip från en **ASIC** som **Antminer S19** på ett **opensource** elektroniskt kort för att skapa en liten Miner på 0,5TH/s för 15W. Detta är den Miner vi kommer att använda som exempel för denna handledning.


## Lägga till en **Arbetstagare** 👷‍♂️


![signup](assets/cover.webp)


Längst upp på sidan kan du kopiera poolen Address **stratum+tcp://public-pool.io:21496**.


Därefter anger du i fältet **användare** en **Bitcoin** Address som du äger.


Om du har flera gruvarbetare kan du ange samma Address för dem alla så att deras **hashrates** kombineras och visas som en enda Miner. Du kan också skilja dem åt genom att lägga till ett distinkt namn för var och en. För att göra detta lägger du helt enkelt till **.arbetsnamn** efter **Bitcoin** Address.


Slutligen, för fältet **lösenord**, använd **'x'**.


Exempel: Om din **Bitcoin** Address är **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv'** och du vill namnge din Miner **" Brrrr"**, så anger du följande information i din Miner:s Interface:



- **URL**: stratum+tcp://public-pool.io:21496
- **ANVÄNDARE**: **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr'**
- **Lösenord**: **'x'**

Om din Miner är en **Bitaxe** är fälten lite annorlunda, men informationen är densamma:


- **URL**: public-pool.io (här måste du ta bort delen i början **'stratum+tcp://'** och delen i slutet **':21496'** som kommer att rapporteras i portfältet)
- **Port**: 21496
- **Användare**: **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr'**
- **Lösenord**: **'x'**


![signup](assets/3.webp)


Några minuter efter att du har startat Mining kommer du att kunna se dina data på webbplatsen **Public Pool** genom att söka efter din Address.


## Instrumentpanel


![signup](assets/4.webp)


När du är ansluten till **Public Pool** kan du komma åt din **Dashboard** genom att söka med din **Bitcoin** Address som du angav i fältet **User**. I vårt fall här är det **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv'**.


På **Dashboard** visas olika information både om dina data och om nätverket.


![signup](assets/5.webp)


Du har **Network Hash Rate** som motsvarar den totala arbetsstyrkan i **Bitcoin**-nätverket.


**Network Difficulty** anger den svårighetsgrad som måste uppnås för att validera ett block.


Och **Din bästa svårighetsgrad** är den högsta svårighetsgrad du har uppnått. Om du av en slump 🍀 når nätverkssvårigheten vinner du hela Block reward... efter 100 block. Du skulle behöva vänta 100 block innan du kunde spendera dem.


Du har också **Blockhöjd** som är numret på det senaste blocket som utvanns samt dess vikt uttryckt i WU, med ett maximum på 4.000.000.


Nedan kan du se all statistik för var och en av dina enheter individuellt om du har gett dem ett distinkt namn genom att lägga till **.name** bakom din **Bitcoin** Address i fältet **User**.