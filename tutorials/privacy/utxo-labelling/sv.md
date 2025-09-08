---
name: Märkning UTXO
description: Hur märker jag din UTXO på rätt sätt?
---
![cover](assets/cover.webp)


I den här handledningen kommer du att upptäcka allt du behöver veta om märkning av UTXO:er i din Bitcoin Wallet och om myntkontroll. Vi börjar med ett teoretiskt avsnitt för att fullt ut förstå dessa begrepp, innan vi går vidare till en praktisk del där vi utforskar hur man konkret använder etiketter i huvudprogramvaran Bitcoin Wallet.


## Vad är UTXO-märkning?

"Märkning" är en teknik som innebär att man associerar en anteckning eller etikett med en specifik UTXO inom en Bitcoin Wallet. Dessa anteckningar lagras lokalt av Wallet-programvaran och överförs aldrig via Bitcoin-nätverket. Märkning är således ett verktyg för personlig hantering.


Om jag till exempel får en UTXO från en P2P-transaktion via Bisq med Charles, kan jag tilldela den etiketten `Bisq P2P Purchase Charles`.


Märkningen gör det möjligt att komma ihåg UTXO:s ursprung eller avsedda destination, vilket förenklar fondhanteringen och optimerar användarens integritet. Märkning blir ännu mer relevant när den kombineras med "coin control"-funktionen. Coin control är ett alternativ som finns i bra Bitcoin-plånböcker, vilket ger användaren möjlighet att manuellt välja vilka specifika UTXO:er som ska användas som input när en transaktion skapas.


Genom att använda en Wallet med myntkontroll, i kombination med UTXO-märkning, kan användare exakt urskilja och välja UTXO:er för sina transaktioner och därmed undvika att slå samman UTXO:er från olika källor. Denna praxis minskar riskerna med Common Input Ownership Heuristic (CIOH), som föreslår gemensamma Ownership för inmatningarna i en transaktion, vilket kan äventyra användarens integritet.


Låt oss gå tillbaka till exemplet med min icke-KYC UTXO från Bisq; jag vill undvika att kombinera den med en UTXO som kommer, säg, från en reglerad Exchange-plattform som känner till min identitet. Genom att placera en distinkt etikett på min no-KYC UTXO och på min KYC UTXO, kommer jag enkelt att kunna identifiera vilken UTXO som ska konsumeras som input för att uppfylla en utgift, med hjälp av myntkontrollfunktionaliteten.


## Hur märker man UTXO på rätt sätt?

Det finns ingen universell metod för märkning av UTXO:er som passar alla. Det är upp till dig att definiera ett märkningssystem så att du enkelt kan hitta runt i din Wallet.

Ett avgörande kriterium vid märkning är källan till UTXO. Du bör helt enkelt ange hur det här myntet hamnade i din Wallet. Är det från en Exchange-plattform? En räkningsavveckling av en kund? En peer-to-peer Exchange? Eller representerar det växel från ett köp? Således kan du specificera:


- `Withdrawal Exchange.com`;
- "Betalning till kund David";
- `P2P Purchase Charles`;
- förändring jämfört med köp av soffa.

![labelling](assets/en/1.webp)

För att förfina din UTXO-hantering och följa dina strategier för fondsegregering inom din Wallet kan du berika dina etiketter med en ytterligare indikator som återspeglar dessa separationer. Om din Wallet innehåller två kategorier av UTXO:er som du inte vill blanda, kan du integrera en markör i dina etiketter för att tydligt skilja dessa grupper åt.


Dessa separationsmarkörer beror på dina egna kriterier, t.ex. skillnaden mellan KYC UTXO (kännedom om din identitet) och no-KYC (anonym), eller mellan professionella och privata medel. Med de tidigare nämnda exemplen på etiketter skulle detta kunna översättas som:


- `KYC - Uttag Exchange.com`;
- `KYC - Payment Client David`;
- `NO KYC - P2P Köp Charles`;
- `NO KYC - Ändring från soffköp`.

![labelling](assets/en/2.webp)

Tänk i alla fall på att bra märkning är märkning som du kommer att kunna förstå när du behöver den. Om din Bitcoin Wallet i första hand är avsedd för sparande kan det hända att etiketterna kommer att vara användbara för dig först om flera decennier. Se därför till att de är tydliga, exakta och heltäckande.


Det är också tillrådligt att fortsätta märkningen av ett mynt under alla transaktioner. Till exempel, under en no-KYC UTXO konsolidering, se till att markera den resulterande UTXO inte bara som `konsolidering`, utan specifikt som `no-KYC konsolidering` för att upprätthålla ett tydligt spår av myntets ursprung.


Slutligen är det inte obligatoriskt att sätta ett datum på en etikett. De flesta Wallet-programvaror visar redan transaktionsdatumet, och det är alltid möjligt att hämta denna information på en Block explorer med hjälp av dess txid.


## Självstudier: Märkning på Specter Desktop


Anslut och öppna din Wallet på Specter Desktop, välj sedan fliken `Addresser`.


![labelling](assets/notext/3.webp)

Här ser du listan över alla dina adresser, samt alla bitcoins som är låsta på dem. Som standard identifieras adresserna med sitt index under kolumnen "Etikett". Om du vill ändra en etikett klickar du bara på den, anger önskad etikett och bekräftar sedan genom att klicka på den blå ikonen.

![labelling](assets/notext/4.webp)


Din etikett kommer då att visas i listan över dina adresser.


![labelling](assets/notext/5.webp)


Du kan också tilldela en etikett i förväg, när du delar din mottagande Address med avsändaren. Detta gör du genom att gå till fliken `Receive` och anteckna din etikett i det avsedda fältet.


![labelling](assets/notext/6.webp)


## Självstudier: Märkning på elektrum


På Electrum Wallet, efter att ha loggat in på din Wallet, klickar du på den transaktion som du vill tilldela en etikett från fliken `History`.


![labelling](assets/notext/7.webp)


Ett nytt fönster öppnas. Klicka på rutan `Description` och skriv in din etikett.


![labelling](assets/notext/8.webp)


När etiketten är inmatad kan du stänga detta fönster.


![labelling](assets/notext/9.webp)


Din etikett har sparats framgångsrikt. Du hittar den under fliken `Beskrivning`.


![labelling](assets/notext/10.webp)


I fliken "Mynt", där du kan utföra myntkontroll, finns din etikett i kolumnen "Etikett".


![labelling](assets/notext/11.webp)


## Självstudier: Märkning på Green Wallet


I appen Green Wallet öppnar du din Wallet och väljer den transaktion som du vill märka. Klicka sedan på den lilla pennikonen för att notera din etikett.


![labelling](assets/notext/12.webp)


Skriv din etikett och klicka sedan på Green `Save`-knappen.


![labelling](assets/notext/13.webp)


Du kommer att kunna hitta din etikett både i detaljerna för din transaktion och på instrumentpanelen i din Wallet.


![labelling](assets/notext/14.webp)


## Självstudier: Märkning på Samourai Wallet


I Samourai Wallet finns det olika metoder som gör att du kan tilldela en etikett till en transaktion. För den första metoden börjar du med att öppna din Wallet och välja den transaktion som du vill lägga till en etikett på. Tryck sedan på knappen "Lägg till", som finns bredvid rutan "Anteckningar".


![labelling](assets/notext/15.webp)


Skriv in din etikett och bekräfta genom att klicka på den blå knappen "Lägg till".


![labelling](assets/notext/16.webp)


Du hittar din etikett i detaljerna för din transaktion, men också på instrumentpanelen i din Wallet.


![labelling](assets/notext/17.webp)

För den andra metoden klickar du på de tre små prickarna längst upp till höger på skärmen och sedan på menyn `Show Unspent Transaction Outputs`.

![labelling](assets/notext/18.webp)


Här hittar du en omfattande lista över alla UTXO:er som finns i din Wallet. Den visade listan gäller mitt insättningskonto, men denna operation kan replikeras för Whirlpool-konton genom att navigera från den dedikerade menyn.


Klicka sedan på den UTXO som du vill märka, följt av knappen `Add`.


![labelling](assets/notext/19.webp)


Skriv in din etikett och bekräfta genom att klicka på den blå knappen "Lägg till". Du kommer sedan att hitta din etikett både i detaljerna för din transaktion och på din Wallet:s instrumentpanel.


![labelling](assets/notext/20.webp)


## Självstudier: Märkning på Sparrow wallet


Med Sparrow wallet-programvaran är det möjligt att tilldela etiketter på flera olika sätt. Den enklaste metoden är att lägga till en etikett i förväg, när du kommunicerar en mottagande Address till avsändaren. För att göra detta, i menyn `Receive`, klicka på fältet `Label` och ange den etikett du vill ha. Detta kommer att bevaras och vara tillgängligt i hela programvaran så snart bitcoins tas emot på Address.


![labelling](assets/notext/21.webp)


Om du glömde att märka din Address vid mottagandet är det fortfarande möjligt att lägga till en senare via menyn `Transaktioner`. Klicka bara på din transaktion i kolumnen `Label` och ange sedan önskad etikett.


![labelling](assets/notext/22.webp)


Du har också möjlighet att lägga till eller ändra dina etiketter från menyn "Adresser".


![labelling](assets/notext/23.webp)


Slutligen kan du visa dina etiketter i menyn "UTXO". Sparrow wallet lägger automatiskt till parenteser bakom din etikett om vilken typ av utdata det rör sig om, vilket hjälper till att skilja UTXO:er som beror på ändringar från dem som tas emot direkt.


![labelling](assets/notext/24.webp)