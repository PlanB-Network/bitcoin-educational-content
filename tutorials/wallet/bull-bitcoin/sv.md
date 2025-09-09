---
name: Bull Bitcoin Wallet
description: Ta reda på hur du använder Wallet Bull Bitcoin
---

![cover](assets/cover.webp)



Den här guiden tar dig igenom installation, konfiguration och användning av Bull Bitcoin Mobile. Du får lära dig hur du tar emot och skickar pengar i de tre nätverken: onchain, Liquid och Lightning, och hur du överför din Bitcoin från ett nätverk till ett annat. I bilagorna finns resurser och kontakter, bakgrundsinformation och korta förklaringar av tekniska begrepp.



## Inledning



**Bull Bitcoin Mobile**, utvecklad av **[Bull Bitcoin](https://www.bullbitcoin.com/)** ([skapa konto](https://app.bullbitcoin.com/registration/orangepeel)), är en **self-custodial** Bitcoin Wallet, vilket innebär att du har full kontroll över dina privata nycklar och därmed dina pengar, utan att vara beroende av en tredje part. Denna Wallet är öppen källkod och har sina rötter i en Cypherpunk-filosofi och kombinerar enkelhet, sekretess och avancerade funktioner som swappar över nätverk och PayJoin-stöd. Den låter dig hantera dina bitcoins på tre nätverk: **Bitcoin onchain**, **Liquid** och **Lightning**, vart och ett skräddarsytt för specifika användningsområden.



### Utvecklingssammanhang



Wallet svarar på en stor utmaning: Bitcoin-nätverksavgifter är olämpliga för små betalningar eller för att öppna små självhanterade Lightning-kanaler. Wallet Bull Bitcoin Mobile erbjuder en lösning för självförvar samtidigt som den förlitar sig på de 3 största Bitcoin-nätverken:





- Bitcoin-nätverk (onchain)**: Idealisk för medel- till långtidslagring av UTXO:er och transaktioner med stora värden, där avgifterna proportionellt sett är försumbara.
- Liquid Network**: Utformad för snabba (~2 minuter), mer konfidentiella (dolda belopp) och billiga transaktioner, perfekt för att samla små belopp eller skydda din integritet.
- Lightning**-nätverk: Optimerat för omedelbara betalningar till låg kostnad, lämpligt för dagliga transaktioner med små till medelstora värden.



Med Bull Bitcoin Mobile kan du till exempel samla små belopp i portföljerna **Liquid** eller **Lightning** och sedan, när du har nått ett betydande belopp, kan du :





- Överföring till onchain-nätverket för säker lagring på medellång eller lång sikt, med förbättrad sekretess med Liquid och/eller Lightning uppströms, och med onchain-avgifter för en enda transaktion



### Kontinuerlig utveckling



Wallet utvecklas ständigt, så bli inte förvånad om du hittar avvikelser mellan den här handledningen och din uppdaterade applikation.




- Till exempel, från och med 19/07/2025, är **"Köp / Sälj / Betala"** -knapparna synliga men gråtonade i applikationen, eftersom dessa alternativ, tillgängliga på Exchange [bullbitcoin.com] (https://app.bullbitcoin.com/registration/orangepeel), snart kommer att integreras för en enhetlig upplevelse. Användningen av dem kommer att förbli helt valfri. Många andra utvecklingar pågår eller planeras: multi-Wallet-hantering, passphrase, kompatibilitet med hårdvaruplånböcker ...
- På [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49) kan du kolla in aktuella ämnen och kommande utveckling. Eftersom projektet är 100% öppen källkod och "byggt i allmänhet" kan du också skicka oss dina förslag och eventuella buggar du stöter på.




## 1. Förkunskapskrav



Innan du börjar använda **Bull Bitcoin Mobile** ska du se till att du har följande saker:





- Kompatibel smartphone**: En **iOS** (iPhone eller iPad) eller **Android** enhet
- Internetanslutning
- Säkra backup-media**: Skriv ner din **återställningsfras** (12 ord) på papper eller metall och förvara den på en säker plats.
- Grundläggande kunskaper**: En minimiförståelse för Bitcoin-koncept (adresser, transaktioner, avgifter) är användbar, även om denna handledning förklarar varje steg för nybörjare.



## 2. Installation





- Ladda ner ansökan** :
 - [Google Play Store] (https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&pcampaignid=web_share)** Ladda ner från applikationsbutiken för Android-enheter
 - [GitHub] (https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) Ladda ner APK för Android-enheter direkt**
 - [iOS] (https://testflight.apple.com/join/FJbE4JPN)** Ladda ner via TestFlight för Apple-enheter
 - Kontrollera utvecklarens namn (Bull Bitcoin) för att undvika bedrägliga applikationer.
 - Se till att den nedladdade versionen motsvarar den senaste stabila versionen som anges på GitHub.
 - Bull Bitcoin Mobile är **öppen källkod**. För att se koden: [BullBitcoin GitHub](https://github.com/orgs/SatoshiPortal/projects/49)





- Installera programmet




## 3. Inledande konfiguration



### 3.1 Starta programmet :



Programmet använder en unik återställningsfras på 12 ord för båda portföljerna:




 - säkra Bitcoin' Wallet**: För transaktioner i Bitcoin-nätverket (onchain)
 - omedelbara betalningar" Wallet**: För omedelbara transaktioner på Liquid- och Lightning-nätverk



Vid öppnandet uppmanas du att importera en befintlig återställningsfras eller att skapa en ny Wallet :



![image](assets/fr/02.webp)



### 3.2 Återvinningsfras :



Om du vill återanvända en befintlig Wallet klickar du på "**återanvänd Wallet**" och fyller i de 12 orden i din återanvändningsfras.



Annars klickar du på "**Create New Wallet**":




- Skriv ner din återställningsfras med största försiktighet. Skriv ner den på papper eller metall och förvara den på en säker plats (bankfack, offlineplats). Denna fras är ditt enda sätt att få tillgång till dina bitcoins om du förlorar din enhet eller raderar applikationen.
- Det är också viktigt att notera att vem som helst med den här frasen kan stjäla alla dina bitcoins. Förvara dem aldrig digitalt:
 - Ingen skärmdump
 - Ingen säkerhetskopiering i molnet, via e-post eller meddelanden
 - Ingen kopiera/klistra in (risk för att spara i urklipp)



**! Denna punkt är kritisk**. För ytterligare hjälp :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### 3.3 Säkra åtkomst :





- Gå till inställningar och klicka sedan på **PIN-kod**.
- Skapa en robust **PIN-kod** för att skydda åtkomsten till applikationen.
- Detta steg är valfritt, men rekommenderas starkt för att förhindra att någon med tillgång till din telefon får tillgång till din Wallet.



![image](assets/fr/03.webp)



### 3.4 Anslutning till en personlig nod (tillval):



Wallet BullBitcoin ansluter som standard till Electrum-servrar: den första som hanteras av Bull Bitcoin och en sekundär server från Blockstream, som båda anses inte föra några loggar, vilket minskar risken för spårning.



För större sekretess kan du ansluta applikationen till din egen Bitcoin-nod via en Electrum-server (instruktioner finns på [BullBitcoins GitHub](https://github.com/orgs/SatoshiPortal/projects/49) ).




## 4. Mottagande av medel



Att ta emot pengar med **Bull Bitcoin Mobile** är enkelt och anpassat efter dina behov, oavsett om du använder :




  - **Bitcoin (onchain)**-nätverket för långsiktigt bevarande,
  - **Liquid**-nätverket för snabb, mer Confidential Transactions,
  - **Lightning**-nätverket för omedelbara betalningar med lågt värde.



Programmet genererar automatiskt adresser för Lightning-mottagning eller Invoice, beroende på vilket nätverk som valts. Så här går du tillväga för varje nätverk.



### 4.1. onchain (Bitcoin-nätverk)



På startskärmen kan du :




- eller välj **Secure Bitcoin Wallet** och klicka sedan på "**Receive"** :



![image](assets/fr/04.webp)





- eller klicka på "**Receive"** och välj sedan nätverket **Bitcoin**:



![image](assets/fr/05.webp)



#### 4.1.1. Alternativet "Kopiera eller skanna endast Address" är avaktiverat (standard)



![image](assets/fr/06.webp)





- Detta ger tillgång till valfria avancerade parametrar. Du kan ange :
 - Ett **belopp** i BTC, Sats eller fiat.
 - En **personlig anteckning** som ska inkluderas i kopian av URI-/QR-koden.
 - Aktivering av **PayJoin** (se bilaga 3 för detaljer), som förbättrar sekretessen genom att kombinera avsändar- och mottagaruppgifter.





- Exempel på en automatiskt genererad URI** :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=2.1e-7&message=Exemple+de+note&pj=HTTPS%3A%2F%2FPAYJO.IN%2FUJA9LJ6L4CMHY%23RK1QT3YSGFC6PMKRUXND2DSGQMLESTUNH29AY0305XAQ678742CVT5ES+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1RRH8C6Q
```





- Användning**: Kopiera URI:n för att dela den med avsändaren, eller låt honom skanna QR-koden.



#### 4.1.2. Alternativet "Kopiera eller skanna endast Address" aktiverat



![image](assets/fr/07.webp)





- Med alternativet **"Kopiera eller skanna endast Address"** aktiverat genererar programmet en enkel Bitcoin Address i SegWit (bech32)-format.





- Exempel:



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```



Även om du anger ett belopp eller en anteckning kommer de inte att inkluderas i QR-koden eller i kopian av Address





- Användning**: Kopiera Address för att dela den med avsändaren, eller låt honom skanna QR-koden.



#### 4.1.3. Generering av en ny Address





- Varför använda en ny Address för varje transaktion? Detta **skyddar din integritet** genom att förhindra att flera betalningar kopplas till samma Address och begränsar möjligheterna till spårning på Blockchain.
 - Som standard genererar Bull Bitcoin automatiskt en oanvänd Address.**
 - Du kan tvinga fram skapandet av en ny Address genom att klicka på **"New Address"** längst ned på skärmen.
 - Alla dina adresser är länkade till din seed-fras: oavsett hur många adresser du använder kommer din portfölj att visa ett enda saldo och kan automatiskt konsolidera medel när en leverans görs.





- Tips: Använd alltid den nya Address** som tillhandahålls av Bull Bitcoin, såvida du inte har ett specifikt behov (t.ex. en offentlig Address för att ta emot donationer).



### 4.2. Liquid



På startskärmen kan du :




- eller välj **Instantbetalningar Wallet** och klicka sedan på **"Mottag"** och sedan **"Liquid"** :



![image](assets/fr/08.webp)





- eller klicka på "**Receive"** och välj sedan nätverket **Liquid**:



![image](assets/fr/09.webp)



När du är på **"Receive"**-skärmen kopierar du en Liquid Address:





- Inget belopp eller nota. Exempel:



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```





- Eller genom att ange ett **belopp** (i BTC, Sats eller fiat) och/eller en **personlig anteckning** som ska inkluderas i kopian av URI/QR-koden. Exempel på detta:



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



**Användning**: Kopiera Address/URI för att dela med dig till avsändaren, eller låt honom skanna QR-koden.



### 4.3. Blixten



På startskärmen kan du :




- eller välj **Instant payments Wallet** och klicka sedan på "**Receive"** :



![image](assets/fr/10.webp)





- eller klicka på "**Receive"**, och välj sedan **Lightning**-nätverket:



![image](assets/fr/11.webp)



#### 4.3.1. Funktion, begränsningar och fördelar





- Mekanism**: Bull Bitcoin Wallet är en Wallet som gör det möjligt att göra och ta emot betalningar via Lightning. Medel som tas emot via Lightning lagras i **Liquid**-nätverket (i Wallet Instant Payments) tack vare en automatisk swap via **Boltz**. Detta ger dig möjlighet att interagera med Lightning utan att behöva hantera likviditetskanaler, samtidigt som du förblir i självförvar.





- Gränser:**
 - Ett minimibelopp** på 100 satoshis (fr.o.m. 19/07/2025) när du generate Invoice.
 - Du betalar kostnaderna**, som dras av från det belopp som avsändaren skickar, till skillnad från mottagande med Wallet Lightning native, där endast avsändaren betalar överföringskostnaderna utöver det skickade beloppet. Per 2025-07-19 dras 47 Sats av från det skickade beloppet.





- Förmåner** :
 - Självförvaltande**: Dina pengar förblir under din kontroll, lagrade på Liquid Network.
 - Inga höga avgifter på kedjan**: Lagring på Liquid undviker kostsamma insättningar på kedjan för att öppna din Lightning-kanal eller lägga till likviditet. Dessa åtgärder kan utföras senare, när det belopp som ackumulerats på Liquid motiverar avgifterna.





- Tips:** Om avsändaren har Wallet Bull Bitcoin, använd Liquid Network direkt för att undvika bytesavgifter



#### 4.3.2. generate Invoice





- Ange ett **belopp** (i BTC, Sats eller fiat)





- Lägg till en **personlig anteckning** som kommer att integreras i Invoice. Om avsändaren betalar Invoice kommer din Wallet också att inkludera det i transaktionsuppgifterna.





- Giltighetstid Invoice:** Blixten Invoice är giltig i **12 timmar**. Efter denna tid upphör den att gälla och kan inte längre betalas. En ny Invoice måste genereras.





- Användning**: Kopiera Invoice för att dela den med avsändaren, eller låt honom skanna QR-koden.




## 5. Skicka pengar



### 5.1. Grundläggande princip



Antingen från hemsidan eller från plånböcker :



![image](assets/fr/12.webp)



för att komma till sändningsskärmen:



![image](assets/fr/13.webp)



**Bull Bitcoin Mobile** gör det enkelt att skicka pengar genom att automatiskt upptäcka nätverket (Bitcoin, Liquid eller Lightning) baserat på den Address eller Invoice som anges (kopierad eller skannad via QR-kod).



### 5.2. onchain-överföring (Bitcoin-nätverk)



#### 5.2.1. Skärmen Skicka



**Åtgärd**: Ange eller skanna en Bitcoin på kedjan Address





- Om beloppet inte har definierats, t.ex. :



```
bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq
```





- Sedan kan du välja på sändningsskärmen :
 - Belopp i BTC, sat eller fiat. Lägsta belopp: 546 satoshis den 22/07/2025.
 - En valfri anteckning för att identifiera transaktionen. Endast synlig för dig i transaktionsinformationen.



![image](assets/fr/14.webp)





- Om beloppet redan har definierats, t.ex. :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Du kommer då direkt till bekräftelsefönstret nedan.



#### 5.2.2 Bekräftelseskärm



Ta dig tid att kontrollera alla parametrar, särskilt belopp, destination Address och avgifter.


Därefter kan du justera parametrarna:



![image](assets/fr/15.webp)




- Avgifter**: Du kan välja :
  - Antingen beräknas transaktionshastigheten** för din transaktion och de tillhörande avgifterna
  - Antingen avgifterna**, i Absolut avgifter (totala avgifter i satoshis) eller Relativa avgifter (avgifter per byte), och hastigheten på din transaktion kommer att uppskattas





- Avancerade inställningar** :





 - Replace-by-fee (RBF)** : Denna funktion är aktiverad som standard och påskyndar transaktionen genom att en högre avgift betalas (se bilaga 4 för mer information).





 - Manuellt val av UTXO**: Om dina medel förvaras på flera olika Wallet-adresser kan du välja från vilka adresser du vill skicka medlen. Varför bör du göra detta? Med den ökande användningen av Bitcoin stiger överföringsavgifterna. Att skicka från flera adresser med små belopp är dyrare än att skicka från en enda Address, men om du gör det nu undviker du att behöva göra det senare, när avgifterna kommer att vara ännu högre. Detta kallas **konsolidering av UTXO.**



![image](assets/fr/16.webp)





- Sändning med PayJoin**: Om funktionen har aktiverats av den mottagare som angav URI:n, t.ex. :



```
bitcoin:bc1qyv76arrcu7bullbitcoin9mgugjvcgelcjfcycjq?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F7GAEA52UMTYQ7%23RK1QVJZYR38X2MC585ZPZ60QY72DMXHWT67LERFWW6GQ4LDEA7MRP78X+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1EJ78U6Q
```



Sedan konfigurerar Bull Bitcoin Mobile sändningen genom att kombinera dina UTXO:er med mottagarens UTXO:er som input, vilket förbättrar sekretessen (se bilaga 3 för detaljer).



### 5.3. Skicka till Liquid



#### 5.3.1 Skärmen Skicka



Nätverket **Liquid** möjliggör snabba transaktioner (~2 minuter tack vare ett block per minut), mer konfidentiella (maskerade belopp) än i onchain-nätverket och med mycket låga avgifter. Pengar tas ut från **Instant Payments Wallet**.



**Åtgärd**: Ange eller skanna en Liquid Address





- Om beloppet inte har definierats, t.ex. :



```
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz
```



Sedan kan du välja på sändningsskärmen :




- Belopp i BTC, sat eller fiat. Inget minimum, 1 Satoshi möjligt;
- En valfri anteckning för att identifiera transaktionen. Endast synlig för dig i transaktionsinformationen.



![image](assets/fr/17.webp)





- Om beloppet redan har definierats, t.ex. :



```
liquidnetwork:lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7x53ahpz?amount=2.1e-7&message=Test+de+note+Liquid&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```



Du kommer då direkt till bekräftelsefönstret nedan.



#### 5.3.2 Bekräftelseskärm



Ta dig tid att kontrollera alla parametrar, särskilt mängden och destinationen Address.



![image](assets/fr/18.webp)





- Avgifter**: Proportionell mot transaktionens komplexitet, i allmänhet 0,1 sat/vB, dvs. 20-40 satoshis för en enkel transaktion (33 Sats per 22/07/2025).



### 5.4. Skicka till Lightning



#### 5.4.1 Skärmen Skicka



**Lightning**-nätverket möjliggör omedelbara betalningar till låg kostnad för små belopp, vilket är perfekt för små dagliga transaktioner.



**Åtgärd**: Ange eller skanna en blixt Invoice





- Om du skannar en LN-URL Address som låter dig ställa in beloppet


Exempel: `orangepeel@walletofsatoshi.com`.


så kan du välja på sändningsskärmen :




 - Belopp i BTC, sat eller fiat. Lägsta belopp på 1000 satoshis den 23/07/2025
 - En valfri anteckning för att identifiera transaktionen. Den kommer att skickas till mottagaren.



![image](assets/fr/19.webp)





- Om du skannar en Lightning Invoice som innehåller en definierad mängd


Exempel:



```
lnbc210n1p58hhk6bullbitcoint4a9jq34dmrmcrursjmw3wjf8elz0nxtdsw9pscqzyssp52jg9dm8vc3xy26er5rc965lxjllhd82je97au7ysvv6lpq7r7shs9q7sqqqqqqqqqqqqqqqqqqqsqqqqqysgqdqqmqz9gxqyjw5qrzjqwryaup9lh50kkranzgcdnn2fgvx390wgj5jd07rwr3vxeje0glclle6wrlm37k39uqqqqlgqqqqqeqqjqnf7w9f2evnzptm2vtdknk7483hsndkl98c4mv2kfe64v5pkq0j6x2dqt9y9wayszv3z33az7c8hkj3yqj9jd7ans7ugq8xv0xefp23gqltph72
```



Du kommer då direkt till bekräftelsefönstret nedan.



Obs: beloppet måste vara större än 21 Sats den 23/07/2025



#### 5.4.2 Drift, begränsningar och fördelar





- Mekanism**: Medel dras från **Instant Payments Wallet** (Liquid) och omvandlas via en **Liquid → Lightning**-swap med **Boltz**.





- Gränser:**
 - Ett minimibelopp** högre än en Wallet Lightning native (se ovan)
 - Kostnader** plus Liquid → Lightning swap via Boltz





- Förmåner** :
 - Självförvaltande**: Dina pengar förblir under din kontroll, lagras på Liquid Network och kan överföras via Lightning om så krävs
 - Inga höga avgifter på kedjan**: Lagring på Liquid har sparat dig kostsamma onchain-insättningar för att öppna din Lightning-kanal eller lägga till likviditet. Dessa operationer kan utföras senare, när det belopp som ackumulerats på Liquid motiverar avgifterna.





- Tips:** Om mottagaren har Wallet Bull Bitcoin, använd Liquid Network direkt för att undvika byteskostnader



#### 5.3.3 Bekräftelseskärm



Ta dig tid att kontrollera alla parametrar, särskilt mängden och destinationen Address.



![image](assets/fr/20.webp)




## 6. Visa historik



**Bull Bitcoin Mobile** gör det enkelt att spåra dina transaktioner i nätverken **Bitcoin (onchain)**, **Liquid** och **Lightning**. Historiken kan nås på två sätt och visar detaljerad information för varje typ av transaktion. Du kan också kontrollera dina transaktioner med hjälp av externa blockwebbläsare.



### 6.1. Åtkomsthistorik





- Via startskärmen** :
 - Klicka på **Secure Bitcoin Wallet** för att se **onchain**-transaktioner, eller på **Instant Payments Wallet** för **Liquid**- och **Lightning**-transaktioner.
 - Historiken visas direkt under portföljens totalvärde, filtrerad enligt den typ av Wallet som valts.



![image](assets/fr/21.webp)





- Via den särskilda sidan** :
 - På startskärmen klickar du på **historiesymbolen** (klocksymbol eller liknande).
 - Öppna en sida som listar alla transaktioner, med filter efter typ av åtgärd: **Send**, **Receive**, **Swap**, **PayJoin**, **Sell**, **Buy** (Obs: Sell och Buy är under utveckling och är inte tillgängliga för närvarande, 20 juli 2025).



![image](assets/fr/22.webp)



### 6.2. Transaktionsuppgifter



Varje transaktion visar specifik information beroende på nätverk och typ av åtgärd (sändning eller mottagning). Här är de tillgängliga detaljerna för en **transaktion på kedjan** :



![image](assets/fr/23.webp)



### 6.3. Kontroll via Block explorer



Listan över utforskare för **Bitcoin onchain**-, **Liquid**- och **Lightning**-nätverken finns i bilaga 4.



För **Lightning** är transaktioner inte synliga i offentliga webbläsare. Kontrollera detaljer (inklusive Swap ID för Boltz) i ansökan.




## 7. Inställningar



Sidan "Settings" kan nås direkt från startsidan för Bull Bitcoin-applikationen och används för att konfigurera och hantera olika aspekter av portföljen och användarupplevelsen.



![image](assets/fr/24.webp)





- Wallet Säkerhetskopiering**: Visar portföljens återställningsfras för säker säkerhetskopiering. Se avsnitt 3. om skapande av portföljer för bästa praxis för hantering och lagring av återställningsfrasen.





- Wallet Detaljer** :
 - Pubnyckel**: Publik nyckel associerad med Wallet, används för att generate Bitcoin mottagningsadresser.
 - Avledningssökväg**: Härledningsväg som används för att generate Wallet adresser från den privata nyckeln.





- Electrum-server (Bitcoin-nod)**: Skapa en anslutning till en anpassad Bitcoin-nod för transaktioner i kedjan.





- PIN-kod**: Aktivera och/eller ändra säkerhetskoden för att skydda åtkomsten till applikationen och Wallet-funktionerna.





- Valuta**: Välj om du vill visa belopp i BTC eller Sats, och standardvalutan för fiat (dollar, euro etc.).





- Inställningar för automatisk swap**: Med funktionen _Auto Swap_ kan du automatisera överföringen av din BTC från **Instant Payments Wallet (Liquid)** till din **Bitcoin On-Chain** Wallet, så snart beloppet når en tröskel som du anser vara tillräckligt hög för att motivera transaktionsavgiften.





- Loggar**: Visningsbara aktivitetsloggar som kan delas med teknisk support för att underlätta felsökning.





- Telegramåtkomst för support** : Direktlänk till den officiella Telegram-kanalen för användarhjälp.





- Github-åtkomst** : Länk till [Bull Bitcoin Github repository] (https://github.com/SatoshiPortal) för att visa öppen källkod eller rapportera problem.




## BILAGOR



### A1. Förklaring av PayJoin (P2EP)



![image](assets/fr/25.webp)



**Definition** :




- PayJoin, eller **Pay-to-EndPoint (P2EP)**, är en Bitcoin-transaktionsteknik som förbättrar sekretessen i **onchain**-nätverket. Den kombinerar sändar- och mottagarposter i en enda transaktion, vilket gör belopp och adresser svårare att spåra.



**Operation:**




- I en PayJoin-transaktion samarbetar avsändaren och mottagaren via en kompatibel PayJoin-server för att generate genomföra en gemensam transaktion.
- I stället för att endast avsändaren tillhandahåller poster (UTXO) bidrar mottagaren också med en av sina egna UTXO:er. Detta gör att den information som syns på Blockchain blir otydlig: i stället för en enda post som motsvarar det faktiska beloppet finns det nu två poster, och utgångarna återspeglar inte direkt det belopp som utväxlats.
- Den slutliga transaktionen liknar en vanlig Bitcoin-transaktion (multi-input/multi-output), men döljer det faktiska beloppet som skickas och länkarna mellan adresserna tack vare en steganografisk struktur.



**För användning i Bull Bitcoin Mobile**




- Mottagning** (Address Supply): PayJoin är aktiverad som standard.
- Skicka** : Wallet upptäcker automatiskt en PayJoin URI och konfigurerar transaktionen i enlighet med detta, t.ex:



```
bitcoin:bc1qp2nxbullbticoinzt6tx7x5tlnpzhv37?amount=0.000006&pj=HTTPS%3A%2F%2FPAYJO.IN%2F475QR36G3ZCFZ%23...
```




**Förmåner**




- Förbättrad sekretess**: PayJoin ogiltigförklarar antagandet att alla poster i en transaktion tillhör en enda enhet. Med PayJoin kommer inmatningar från både avsändare och mottagare, vilket bryter detta antagande.
- Maskering av belopp** : Det faktiska utväxlade beloppet visas inte direkt i utdata. Det beräknas som skillnaden mellan mottagarens inkommande och utgående UTXO, vilket gör analysen missvisande.



**Begränsningar**




- PayJoin kräver att avsändaren och mottagaren använder kompatibla plånböcker, annars används en standard onchain-transaktion.
- Transaktionen är något mer komplex (fler in- och utgångar), vilket leder till något högre kostnader.
- Även om den är utformad för att likna en standardtransaktion kan avancerad heuristik (t.ex. tvetydiga utdata, kända PayJoin-servrar) leda till att man misstänker att den används, om än utan absolut säkerhet.



**Mer info:**




- [Ordlista] (https://planb.network/fr/resources/glossary/payjoin)
- Chapitre [Les transactions PayJoin](https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c/c1e90b95-f709-4574-837b-2ec26b11286f)




### A2. Förklaring av Replace-by-fee (RBF)



**Definition**: Replace-by-fee (RBF) är en funktion i Bitcoin-nätverket som gör det möjligt för avsändaren att påskynda bekräftelsen av en **onchain**-transaktion genom att gå med på att betala en högre avgift.



**Begränsningar** :




- RBF är inte tillgänglig för Liquid eller Lightning-transaktioner.
- Den första transaktionen måste markeras som RBF-kompatibel när den skapas, vilket Bull Bitcoin Mobile gör automatiskt om den inte inaktiveras.



**Mer info:**




- [Ordlista] (https://planb.network/fr/resources/glossary/rbf-replacebyfee)




### A3. Bästa praxis



Följ dessa rekommendationer för att använda **Bull Bitcoin Mobile** på ett säkert och effektivt sätt. De hjälper dig att skydda dina pengar, optimera dina transaktioner och bevara din sekretess i nätverken **Bitcoin (onchain)**, **Liquid** och **Lightning**.





- Säkra din återställningsfras** :
 - Självstudier: [Save your Mnemonic phrase](https://planb.network/fr/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270)
 - Cours [La phrase mnémonique](https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f/8f9340c1-e6dc-5557-a2f2-26c9669987d5)





- Använd säker autentisering** :
 - Aktivera en **stark PIN-kod** eller **biometrisk autentisering** (fingeravtryck eller ansiktsigenkänning) för att skydda åtkomsten till programmet.
 - Dela aldrig med dig av din PIN-kod eller biometriska data.





- Skydda din integritet** :
 - generate en ny Address för varje onchain eller Liquid-mottagning för att begränsa spårning på Blockchain.
 - Använd PayJoin när det är tillgängligt för att öka sekretessen avseende det belopp som skickas vidare i kedjan
 - För maximal sekretess, anslut din Wallet till din egen Bitcoin-nod via en Electrum-server istället för att använda den offentliga noden





- Välj det nätverk som passar bäst för dina behov** :
 - Onchain**: Företrädesvis för långvarig förvaring eller transaktioner med stora värden (avgifter försumbara i förhållande till beloppet).
 - Liquid**: Används för snabba, billiga överföringar med ökad sekretess.
 - Blixten**: Välj omedelbara överföringar till låg kostnad för små belopp. Om ni är två Wallet Bull Bitcoin användare, välj Liquid för att undvika Lightning <> Liquid swapavgifter via Boltz.





- Kontrollera alltid leveransadresser** :
 - Innan du skickar pengar, kontrollera Address noggrant. Pengar som skickas till fel Address är förlorade för alltid. Använd kopiera/klistra in eller QR-kodskanning, kopiera/ändra aldrig en Address för hand.





- Optimera kostnaderna** :
 - För transaktioner i kedjan ska du välja lämpliga avgifter (långsam, medelhög, snabb) beroende på hur brådskande ärendet är och hur mycket nätverket är överbelastat.
 - Använd Liquid eller Lightning för små mängder.
 - Aktivera Replace-by-fee (RBF) (se bilaga 4) för kedjeförsändelser om du förväntar dig ett behov av att påskynda bekräftelsen.





- Håll ansökan uppdaterad




### A4. Ytterligare resurser





- Officiella länkar och support:**
 - [staff@bitcoinsupport.com](mailto:staff@bitcoinsupport.com)**, support@bullbitcoin.com : e-post för support
 - [Bull Bitcoin officiella webbplats](https://bullbitcoin.com/) :** Information om Bull Bitcoin tjänster, skapande av konto, tillgång till applikationen
 - [GitHub Bull Bitcoin Mobile] (https://github.com/SatoshiPortal/bullbitcoin-mobile) :** Se kod, utveckling och färdplan, bidra till utvecklingen av...
 - [Konto X - Twitter Bull Bitcoin](https://x.com/BullBitcoin_)**
 - Telegram**-grupp för Wallet mobile: gruppchatt med support, se sidan "Inställningar".





- Block Explorers :**
 - on chain : **[Mempool.space](https://Mempool.space/)**
 - Liquid : **[Blockstream Info](https://blockstream.info/Liquid)**
 - Blixten: **[1ML (Lightning Network)](https://1ml.com/)**





- Utbildning och handledning:** **[Plan ₿ Network](https://planb.network/)** :
 - Säkra din återställningsfras



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f




- Liquid Network** :
 - [Ordlista] (https://planb.network/resources/glossary/liquid-network)**




https://planb.network/courses/6d26bcff-51a3-405f-bcdd-9af8297ce727





- Lightning Network** :
 - [Ordlista] (https://planb.network/resources/glossary/lightning-network)**




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


### A5. Bull Bitcoin



#### Översikt över företaget



**[Bull Bitcoin](https://www.bullbitcoin.com/fr)**, är den äldsta Exchange-plattformen utan depå som uteslutande är avsedd för Bitcoin, grundad 2013 på Bitcoin-ambassaden i Montreal, Kanada. Företaget leds av Francis Pouliot, en erkänd pionjär inom Bitcoin-ekosystemet, och positionerar sig som en nyckelaktör för att främja finansiell suveränitet och användarautonomi. Dess uppdrag är att göra det möjligt för individer att återfå kontrollen över sina pengar genom att använda Bitcoin som ett verktyg för frihet och betalning, samtidigt som man avvisar fiatvalutor och andra kryptovalutor än Bitcoin.



![image](assets/fr/26.webp)



[Skapa ditt konto] (https://app.bullbitcoin.com/registration/orangepeel) med 0,25% rabatt på Bitcoin inköp och försäljning.



#### Värderingar och filosofi



Bull Bitcoin utmärker sig för sina Commitment till Cypherpunk-principer och Bitcoin-etik:





- Exklusivt fokus på Bitcoin** : Plattformen är trogen visionen om en decentraliserad, censurresistent valuta.





- Icke-förvaltare** : Användare behåller full kontroll över sina Bitcoins genom att skicka medel till sina egna portföljer.





- Konfidentialitet**: Minimerad insamling av personuppgifter, med KYC-fria köpalternativ för transaktioner under 999 USD. Uppgifterna skyddas i enlighet med gällande regler (FINTRAC i Kanada, AMF i Frankrike).





- Öppenhet**: Inga dolda avgifter, kostnaderna ingår i spreaden (skillnaden mellan köp- och försäljningspris).





- Finansiell suveränitet**: Bull Bitcoin främjar oberoende från traditionella banksystem och centraliserade institutioner.



#### Huvudsakliga tjänster





- Fiat-insättning** : Användare kan fylla på sitt Bull Bitcoin-konto med fiatvaluta (CAD, EUR, etc.) via banköverföring eller kontant-/betalkort på utvalda kanadensiska postkontor.





- Köp av Bitcoin** : Användare kan köpa Bitcoin som skickas direkt till deras portfölj utan depå, vilket garanterar total kontroll över sina medel.





- Schemalagt köp av Bitcoin**: Bull Bitcoin erbjuder en automatiserad återkommande köptjänst (DCA - Dollar Cost Averaging) med jämna mellanrum, med utnyttjande av ditt tillgängliga saldo, med direkt överföring av Bitcoins till en användarkontrollerad Wallet, vilket minskar effekten av prisvolatilitet.



Observera att ett alternativ som kallas "AutoBuy" låter dig konvertera dina fiats så snart de berör ditt Bull Bitcoin-saldo och skicka dina Bitcoins till din egen Wallet. Detta alternativ kan också kombineras med en återkommande banköverföring som planeras med din bank för att göra en DCA. Detta alternativ automatiserar din Bitcoin-ackumulering utan att du någonsin behöver öppna applikationen.






- Köp Bitcoin till ett fast pris 'Limit Order'**: Låter dig köpa Bitcoin till ett pris som anges i förväg av användaren, vilket automatiskt verkställs när Bull Bitcoin-indexpriset når eller faller under den inställda gränsen.





- Försäljning av Bitcoin**: Användare kan sälja sina Bitcoins och få pengarna i fiatvaluta direkt till sitt bankkonto via bank- eller SEPA-överföring.





- Betalningar från tredje part**: Bull Bitcoin gör det möjligt för användare att skicka fiat-pengar till bankkonton från sina Bitcoins, helt transparent för mottagaren.





- Bull Bitcoin Prime**: Bull Bitcoin Prime är en premiumtjänst för förmögna kunder och företagskunder som erbjuder skräddarsydda lösningar och premiumsupport. Detta inkluderar tillgång till reducerade avgifter, en dedikerad kontoansvarig och skräddarsydda företagstjänster. Denna tjänst riktar sig till institutioner, professionella handlare och företagskunder som söker djupgående expertis och prioriterad behandling.





- Mobil Wallet**: Bull Bitcoin erbjuder en öppen källkod, självförvaltande mobil Wallet, tillgänglig på Android och iOS, som stöder onchain-, Liquid- och Lightning Network-transaktioner.





- Pedagogiskt stöd**: Gratis guider och personlig coachning för att hjälpa användare att skapa, säkra och hantera sina Bitcoin-portföljer, vilket stärker den finansiella självständigheten.



#### Efterlevnad och säkerhet





- Reglerande**: Bull Bitcoin är registrerad hos FINTRAC (Kanada) och AMF (Frankrike) och uppfyller kraven för KYC/AML.





- Säkerhet**: Användning av säkra portföljer och rekommendationer för offline-lagring. Personuppgifter lagras på Bulls Bitcoin-infrastruktur, som är 100% självhanterande och inte förlitar sig på någon tredje part.