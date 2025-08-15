---
name: Breez försäljningsställe

description: Guide för att börja acceptera Bitcoin med Breez POS
---

![cover](assets/cover.webp)

_Den här texten kommer från webbplatsen för Breez-dokumentation: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_


## Vad är Breez POS?


**Breez** är en fullservice, icke-vårdnadshavande blixtapp. Låt oss bryta ner det:



- Lightning** är ett Bitcoin-betalningsnätverk som minskar transaktionstiderna från minuter till millisekunder och transaktionsavgifterna från flera dollar till några cent eller mindre. Lightning förvandlar Bitcoin från digitalt guld till digital valuta samtidigt som alla de fördelar som gör Bitcoin fantastiskt bevaras.
- Non-custodial** innebär att Breez inte tar användarnas pengar i besittning. Många Lightning-appar tar sina användares pengar i besittning. De är i princip Bitcoin-banker. Med en icke-vårdnadshavande app som Breez är alla användare sina egna banker.
- Fullservice** innebär att Breez tar hand om nästan alla tekniska operationer automatiskt och i bakgrunden. Saker som skapande av kanaler, inkommande likviditet och routing stannar under huven. (Men Breez är också öppen källkod, så de som är intresserade av att granska tekniken är välkomna att göra det!)


**Breez POS** är en förkortning för vårt försäljningsställeläge. Med andra ord fungerar Breez som ett digitalt kassaregister för företag och handlare som vill acceptera Lightning-betalningar (utöver sitt "standard"-läge, som är som den digitala versionen av en Wallet i läder för Bitcoin och en nästa generations podcastspelare). Låt oss nu titta på hur du ställer in Breez som ett Lightning-kassaregister för ditt företag.


## Hur kommer man igång med Breez?


1. Det första steget är att ladda ner appen. Den finns tillgänglig för Android och iOS (installera TestFlight och klicka på länken från din enhet).

2. Breez kan säkerhetskopiera sig själv automatiskt till Google Drive, iCloud eller någon WebDav-server.

** Notera:** varje enhet kör sin egen Lightning-nod. Du kan köra POS-läge på så många enheter som du vill, men saldona förblir separata.

3. När appen är öppen klickar du på ikonen längst upp till vänster för att hitta Point of Sale-läget.


## Inställning av POS


För att ställa in POS klickar du på ikonen längst upp till vänster och sedan på Point of Sale > POS-inställningar.


### Chefens lösenord


I POS-inställningarna har du möjlighet att skapa ett lösenord för chefen. Lösenordet för chefen gör det omöjligt att skicka utgående betalningar från Breez-appen utan tillstånd. Säljpersonal kommer endast att kunna ta emot betalningar från enheten. Observera att om du använder det här alternativet kanske du också vill förhindra åtkomst till Breez backup, så att använda ett externt WebDav-konto (t.ex. Nextcloud) rekommenderas för detta användningsfall.


### Föremålslistan


Artikelförteckningen är en katalog över artiklar som är till salu och deras priser. Det finns två sätt att lägga till artiklar i listan:



- Om du vill ange artiklar en i taget klickar du på Artiklar längst upp i POS-huvudvyn och sedan på "+"-tecknet längst ned till höger. Här kan du ange namnet på en enskild typ av artikel, priset (visas i den valuta du väljer) och SKU (en unik intern identifierare för den typen av artikel; den är valfri).
- Om du vill ange många artiklar samtidigt klickar du på kalkylatorikonen längst upp till vänster, sedan på Point of Sale > Preferences > POS Settings och sedan på de tre punkterna till höger om Items List och sedan på Import from CSV. Då kan du importera en CSV-fil som du har förberett i förväg och som innehåller namn, priser och SKU:er för dina artiklar.


### Fiat Display


Breez skickar och tar bara emot Bitcoin, och för de flesta transaktioner på Lightning, som tenderar att vara för mindre belopp, visas summan vanligtvis i Satoshis, även känt som Sats (1 BTC = 100 000 000 Sats). Många handlare tycker dock att det är praktiskt att kunna se (och berätta för kunderna) värdet av köpet i den lokala fiatvalutan.


I POS-huvudvyn visas den valuta som för närvarande visas till höger (standard är SAT). Det finns också en rullgardinslista med andra valutor som kan visas. Om du vill lägga till eller ta bort valutor från den här rullgardinslistan klickar du på Point of Sale > Preferences > Fiat Currencies. Markera sedan de valutor som du vill ha i rullgardinsmenyn och avmarkera dem som du inte vill ha med.


De värden som visas kommer från yadio, en respekterad källa för Exchange-ränteuppgifter, och de uppdateras nästan i realtid. Men kom ihåg: oavsett vilket valutavärde som för närvarande visas, är själva betalningen i Bitcoin.


### Debitering av en order


För att komponera ordern kan du antingen lägga till artiklar från artikellistan eller helt enkelt ange en summa i knappsatsen. Klicka sedan på Charge högst upp i POS-huvudvyn. Du kommer då att se en QR-kod som kunden kan skanna med sin Lightning-app, som du kan dela direkt från en annan app på din enhet eller som du kan kopiera och klistra in där det behövs.


När kunden skannar koden eller klickar på den delade/klistrade Invoice:an ser kunden Invoice:an i sin Lightning-app och har möjlighet att betala den och reglera transaktionen omedelbart.


När du ser animationen Betalning godkänd! i Breez-appen på handlarens enhet kan du klicka på skrivarikonen för att generate ett kvitto till kunden. Om du vill använda en kvittoskrivare i Android kan du prova att använda den här drivrutinen. Observera att du också kan skriva ut tidigare transaktioner via skärmen Transaktioner.


### Försäljningsrapport


Om du vill visa en daglig, veckovis och/eller månatlig rapport över din försäljning (för bokföringsändamål eller annat) klickar du på ikonen längst upp till vänster och sedan på Transaktioner. Klicka på rapportikonen för att visa rapporten och på kalenderikonen för att ändra det valda datumintervallet.


### Exportera transaktioner


För att se en lista över de betalningar som mottagits i Breez, klicka på ikonen längst upp till vänster och klicka sedan på Transaktioner. Klicka på de tre prickarna uppe till höger och sedan på Export för att exportera en lista över inkommande betalningar i CSV-format. Om du vill begränsa listan till en viss tidsperiod klickar du på kalenderikonen för att ange ett datumintervall.


### Skriva ut kvitton


Om du vill skriva ut ett försäljningskvitto klickar du på utskriftsikonen längst upp till höger i dialogrutan för betalningsbekräftelse. Alternativt kan du klicka på ikonen längst upp till vänster och sedan klicka på Transaktioner. Leta reda på försäljningen som ska skrivas ut, öppna den och klicka på utskriftsikonen uppe till höger.


**Använd den här drivrutinen för att skriva ut på en bärbar 58 mm/80 mm Bluetooth/USB-termoskrivare.


## Jag vill lära mig mer



- För mer information om Lightning and Breez, besök vår [blogg](https://breez.technology/blog).
- Mer tekniska tips om hur du får ut mesta möjliga av appen och utför vanliga åtgärder finns i vår [dokumentation] (https://breez.technology/documentation).
- Om du kör fast och inte hittar svaret i någon av våra hjälplitteraturer kan du nå oss på [Telegram] (https://t.me/breez_labs) eller skicka ett [e-postmeddelande] (mailto:support@breez.technology).
- Om du vill se några demonstrationsvideor av Breez POS-läget i aktion gjorda av våra fans och användare, [här](https://www.youtube.com/watch?v=xxxx) är en bra kort video, och [här](https://www.youtube.com/watch?v=xxxx) är en längre, mer detaljerad video.