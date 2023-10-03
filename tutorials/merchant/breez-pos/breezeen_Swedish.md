# Breez försäljningspunkt

_Beskrivning: Guide för att börja acceptera bitcoin med hjälp av Breez POS_

---

![omslag](assets/cover.jpeg)

# Breez försäljningspunkt

_Denna text kommer från Breez dokumentationssida: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_

## Vad är Breez POS?

**Breez** är en komplett tjänst för Lightning, utan förvaring. Låt oss förklara:

- **Lightning** är ett betalningsnätverk för bitcoin som minskar transaktionstider från minuter till millisekunder och transaktionsavgifter från flera dollar till några cent eller mindre. Lightning förvandlar bitcoin från digitalt guld till digital valuta samtidigt som alla fördelar som gör bitcoin fantastiskt bevaras.
- **Utan förvaring** innebär att Breez inte tar över användarnas pengar. Många Lightning-appar tar över sina användares pengar. De är i princip bitcoin-banker. Med en app utan förvaring som Breez är alla användare sina egna banker.
- **Komplett tjänst** innebär att Breez tar hand om nästan alla tekniska operationer automatiskt och i bakgrunden. Saker som kanalskapande, inkommande likviditet och routing förblir under huven. (Men Breez är också öppen källkod, så de som är intresserade av att granska tekniken är välkomna att göra det!)

**Breez POS** är förkortningen för vår försäljningsläge. Med andra ord fungerar Breez som en digital kassaregister för företag och handlare som vill acceptera Lightning-betalningar (förutom dess "standardläge", som är som den digitala versionen av en läderplånbok för bitcoin, och en podcastspelare i nästa generation). Nu ska vi titta på hur du ställer in Breez som ett Lightning-kassaregister för ditt företag.

## Hur du kommer igång med Breez?

1. Det första steget är att ladda ner appen. Den finns tillgänglig för Android och iOS (installera TestFlight och klicka på länken från din enhet).
2. Breez kan säkerhetskopiera sig själv automatiskt till Google Drive, iCloud eller vilken WebDav-server som helst.
   > Observera att varje enhet kör sin egen Lightning-nod. Du kan köra POS-läge på så många enheter du vill, men saldona kommer att vara separata.
3. Med appen öppen, klicka på ikonen längst upp till vänster för att hitta försäljningsläget.

## Inställning av POS

1. Klicka på den ikonen längst upp till vänster och klicka på Försäljningsläge > POS-inställningar.

### Chefslösenordet

I POS-inställningarna har du möjlighet att skapa ett chefs lösenord. Chefs lösenordet gör det omöjligt att skicka utgående betalningar från Breez-appen utan auktorisation. Försäljningspersonalen kommer bara att kunna ta emot betalningar från enheten. Observera att om du använder den här funktionen kan du också vilja förhindra åtkomst till Breez säkerhetskopiering, så det rekommenderas att använda ett externt WebDav-konto (t.ex. Nextcloud) för detta användningsfall.

### Artikellistan

Artikellistan är en katalog över artiklar till försäljning och deras priser. Det finns två sätt att lägga till artiklar i listan:

- För att ange artiklar en i taget, klicka på Artiklar nära toppen av huvudvyn för POS, sedan på "+"-tecknet längst ned till höger. Här kan du ange namnet på en enskild typ av artikel, priset (visas i valfri valuta) och SKU (en unik intern identifierare för den typen av artikel; det är valfritt).
- För att mata in många objekt samtidigt, klicka på kalkylatorsymbolen längst upp till vänster, sedan Point of Sale > Inställningar > POS-inställningar, och klicka sedan på de tre punkterna till höger om Objektlista, och sedan på Importera från CSV. Detta gör att du kan importera en CSV-fil som du har förberett i förväg med dina objekts namn, priser och SKUs.

### Fiat Display

Breez skickar och tar emot endast bitcoin, och för de flesta transaktioner på Lightning, som tenderar att vara för mindre belopp, visas summan vanligtvis i Satoshis, även kända som sats (1 BTC = 100 000 000 sats). Men många handlare tycker att det är praktiskt att kunna se (och berätta för kunderna) värdet på köpet som visas i den lokala fiatvalutan.

I huvudvyn för POS visas valutan som för närvarande visas på höger sida (standard är SAT). Det finns också en nedrullningsbar lista med andra tillgängliga valutor att visa. För att lägga till eller ta bort valutor från denna nedrullningslista, klicka på Point of Sale > Inställningar > Fiatvalutor. Markera sedan de valutor du vill ha i din nedrullningsmeny och avmarkera de du vill utesluta.

De visas värdena kommer från yadio, en respekterad källa för växelkursdata, och de uppdateras nästan i realtid. Men kom ihåg: oavsett vilket valutavärde som för närvarande visas, är själva betalningen i bitcoin.

### Ladda en beställning

För att sätta ihop beställningen, lägg antingen till objekt från objektlistan eller ange helt enkelt en summa på tangentbordet. Klicka sedan på Ladda på toppen av huvudvyn för POS. Du kommer då att se en QR-kod som kunden kan skanna med sin Lightning-app, som du kan dela direkt från en annan app på din enhet, eller som du kan kopiera och klistra in vid behov.

Vid skanning av den koden eller klicka på den delade/inklistrade fakturan, kommer kunden att se fakturan i sin Lightning-app och ha möjlighet att betala den och slutföra transaktionen omedelbart.

När du ser animationen Betalning godkänd! i Breez-appen på handlarens enhet kan du klicka på skrivarikonen för att generera ett kvitto till kunden. För att använda en kvittoskrivare i Android, försök använda den här drivrutinen. Observera att du också kan skriva ut tidigare transaktioner via skärmen Transaktioner.

### Försäljningsrapport

För att visa en daglig/veckovis/månadsvis rapport över dina försäljningar (för redovisningssyften eller andra ändamål), klicka på ikonen längst upp till vänster och klicka sedan på Transaktioner. Klicka på Rapportikonen för att visa rapporten och Kalenderikonen för att ändra det valda datumintervallet.

### Exportera transaktioner

För att visa en lista över de betalningar som mottagits i Breez, klicka på ikonen längst upp till vänster och klicka sedan på Transaktioner. Klicka på de tre punkterna längst upp till höger och sedan på Exportera för att exportera en lista över inkommande betalningar i CSV-format. För att begränsa listan till en viss tidsperiod, klicka på kalenderikonen för att ange ett datumintervall.

### Skriva ut kvitton

För att skriva ut ett försäljningskvitto, klicka på utskriftsikonen längst upp till höger i betalningsbekräftelsedialogen. Alternativt, klicka på ikonen längst upp till vänster och klicka sedan på Transaktioner. Hitta försäljningen att skriva ut, öppna den och klicka på utskriftsikonen längst upp till höger.

> Observera: använd den här drivrutinen för att skriva ut på en bärbar 58mm/80mm Bluetooth/USB-termisk skrivare.

## Jag vill lära mig mer

- För mer information om Lightning och Breez, kolla in vår [blogg](https://breez.technology/blog).
- För mer tekniska tips om hur du får ut det mesta av appen och utför vanliga operationer, kolla in vår [dokumentation](https://breez.technology/documentation).
- Om du fastnar och inte hittar svaret i någon av våra hjälpartiklar, kan du hitta oss på [Telegram](https://t.me/breez_labs) eller skicka oss ett [e-postmeddelande](mailto:support@breez.technology).
- Om du vill se några demonstrationsvideor av Breez POS-läget i aktion, gjorda av våra fans och användare, [här](https://www.youtube.com/watch?v=xxxx) är en bra kort video, och [här](https://www.youtube.com/watch?v=xxxx) är en längre, mer detaljerad video.
