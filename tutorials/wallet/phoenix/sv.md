---
name: Phoenix
description: Installera och använda Phoenix Wallet
---
![cover](assets/cover.webp)


Phoenix är en självförvaltande Lightning Wallet och nod som utvecklats av ACINQ, ett franskt företag som specialiserar sig på Lightning-baserade mjukvarulösningar. Till skillnad från Custodial Lightning-plånböcker som Wallet eller Satoshi, där bitcoins innehas av en tredje part, gör Phoenix det möjligt för användare att behålla full kontroll över sina privata nycklar.


Phoenix fungerar som en äkta Lightning-nod inbäddad i din telefon och öppnar automatiskt en kanal med ACINQ:s Lightning-nod. Applikationen är baserad på Lightning-KMP, en plattformsoberoende implementering av Lightning Network i Kotlin, optimerad för mobila plånböcker. Till skillnad från andra Lightning-nodlösningar förenklar Phoenix hanteringen avsevärt. Användaren behöver inte hantera öppning och stängning av kanaler, köra en Bitcoin-nod eller hantera likviditeten på Lightning Network. Phoenix tar hand om alla dessa tekniska operationer i bakgrunden.


Denna applikation kombinerar användarvänligheten och bekvämligheten hos mobila Lightning-plånböcker med säkerheten och suveräniteten hos en äkta personlig Lightning-nod. Phoenix gör det möjligt att använda Lightning Network på ett säkert, effektivt och självständigt sätt, samtidigt som man får en smidig och intuitiv användarupplevelse.


I gengäld tillkommer vissa avgifter:




- Att skicka med blixt kostar 0,4% av beloppet plus 4 Sats ;
- Om kontanter behövs för att ta emot via Lightning debiteras 1% av beloppet;
- Varje kanal kostar 1000 Sats att öppna.


Phoenix är enligt min mening ett utmärkt mellanting mellan Lightning-portföljer i depå och manuell hantering av en Lightning-nod. Denna applikation är lika lämplig för nybörjare och avancerade användare som föredrar att inte hantera detaljerna i hanteringen av sina egna LND eller Core Lightning. Låt oss ta reda på hur du använder det!


![Image](assets/fr/01.webp)


## Installera programmet


Gå till din applikationsbutik och installera Phoenix :




- På [Google Play Store] (https://play.google.com/store/apps/details?id=fr.acinq.phoenix.Mainnet);
- På [App Store] (https://apps.apple.com/fr/app/phoenix-Wallet/id1544097028?l=en-GB).


![Image](assets/fr/02.webp)


Du kan också installera programmet [med apk-filen på deras GitHub-arkiv] (https://github.com/ACINQ/phoenix/releases).


![Image](assets/fr/03.webp)


## Skapande av portfölj


När programmet har startat klickar du på knappen "*Nästa*" för att hoppa över presentationen och sedan på "*Start*".


![Image](assets/fr/04.webp)


Välj "*skapa en ny Wallet*".


![Image](assets/fr/05.webp)


Och det var det, din Lightning Wallet och nod är nu skapade.


![Image](assets/fr/06.webp)


## Spara Mnemonic fras


Innan vi börjar måste vi spara vår 12-ord långa Mnemonic-fras. Den här frasen ger fullständig, obegränsad tillgång till alla dina bitcoins. Vem som helst som har den här frasen kan stjäla dina pengar, även utan fysisk tillgång till din telefon.


Den 12 ord långa frasen återställer åtkomsten till dina bitcoins i händelse av förlust, stöld eller brott på din telefon. Det är därför mycket viktigt att spara den noggrant och förvara den på ett säkert ställe.


Du kan skriva den på papper eller, för ökad säkerhet, gravera den på rostfritt stål för att skydda den mot brand, översvämning eller kollaps. Valet av medium för din Mnemonic beror på din säkerhetsstrategi, men om du använder Phoenix som en utgiftsportfölj som innehåller måttliga belopp bör papper vara tillräckligt.


För mer information om det rätta sättet att spara och hantera din Mnemonic-fras rekommenderar jag starkt att du följer den här andra handledningen, särskilt om du är nybörjare:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Klicka på meddelandet som visas högst upp på Interface "*Spara din Wallet...*".


![Image](assets/fr/07.webp)


Klicka sedan på "*Spara min Wallet*".


![Image](assets/fr/08.webp)


Klicka sedan på "*Visa min nyckel*" och spara din Mnemonic-fras på ett fysiskt medium.


![Image](assets/fr/09.webp)


Markera de två rutorna längst ned i Interface för att bekräfta att säkerhetskopieringen har slutförts.


![Image](assets/fr/10.webp)


## Inställning av applikation


Innan du gör dina första transaktioner kan du anpassa inställningarna genom att klicka på kugghjulsikonen längst ned till vänster på Interface.


![Image](assets/fr/11.webp)


I menyn "*Display*" kan du välja applikationstema, den valör som används för Bitcoin och din lokala fiatvaluta.


![Image](assets/fr/12.webp)


I "*Payment options*" hittar du olika avancerade inställningar för Lightning-betalningar. Du kan behålla standardinställningarna.


![Image](assets/fr/13.webp)


I "*Channel management*" anger du den maximala avgift du är beredd att betala när du öppnar en Lightning-kanal.


![Image](assets/fr/14.webp)


I menyn "*Access control*" rekommenderar jag starkt att du aktiverar ett autentiseringssystem för att säkra åtkomsten till applikationen på din telefon. Detta kommer att förhindra att någon med tillgång till din olåsta telefon får tillgång till Phoenix och stjäl dina bitcoins.


![Image](assets/fr/15.webp)


I menyn "*Electrum server*" kan du, om du har en Electrs-server, ansluta den för att sända dina transaktioner.


![Image](assets/fr/16.webp)


För att förbättra sekretessen för dina anslutningar kan du aktivera anslutningar via Tor i menyn "*Tor*". Även om användningen av Tor kan göra dina betalningar något långsammare och kräver att Phoenix-programmet är öppet i förgrunden när du tar emot, ökar det din integritet avsevärt.


![Image](assets/fr/17.webp)


## Ta emot bitcoins On-Chain


Vid första användningen har du möjlighet att ladda din Phoenix Wallet med On-Chain-medel. Du kan också göra denna första insättning direkt från Lightning (se nästa avsnitt), men i båda fallen tillkommer ytterligare avgifter för att öppna din första kanal.


Klicka på knappen "*Receive*".


![Image](assets/fr/18.webp)


Svep QR-koden åt vänster för att visa en Bitcoin-mottagningsadress. Skicka det belopp du vill sätta in på Phoenix till den adressen.


![Image](assets/fr/19.webp)


Det belopp som tas emot On-Chain kommer först att visas som väntande under ditt portföljsaldo. Det tar 3 bekräftelser innan pengarna är tillgängliga för användning.


![Image](assets/fr/20.webp)


När pengarna har tagits emot öppnar Phoenix automatiskt en Lightning-kanal åt dig. Du kan nu skicka och ta emot bitcoins via Lightning Network.


![Image](assets/fr/21.webp)


## Ta emot bitcoins via Lightning


För att ta emot Sats via Lightning Network klickar du på knappen "*Motta*".


![Image](assets/fr/22.webp)


Phoenix genererar en blixt Invoice. Du kan antingen skanna den eller skicka den till den person som vill överföra Sats till dig.


![Image](assets/fr/23.webp)


Genom att klicka på knappen "*Edit*" kan du lägga till en beskrivning som kommer att vara synlig för betalaren på Invoice och definiera ett specifikt belopp som betalaren måste skicka.


![Image](assets/fr/24.webp)


De klassiska fakturorna som nämns ovan kan bara användas en gång. För ett återanvändbart betalningsalternativ kan du använda din återanvändbara QR-kod, som är ett BOLT12-erbjudande.


![Image](assets/fr/25.webp)


När erbjudandet Invoice eller BOLT12 har reglerats kommer transaktionen att visas på din Blixt Wallet.


![Image](assets/fr/26.webp)


## Skicka bitcoins via Lightning


Nu när du har Sats på Phoenix är du redo att göra betalningar via Lightning Network. Börja med att klicka på "*Sänd*"-knappen.


![Image](assets/fr/27.webp)


Flera alternativ är tillgängliga för dig. Genom att klicka på "*Scan QR code*" kan du scanna en Lightning Invoice, ett BOLT12-erbjudande eller till och med en mottagande Address för On-Chain-betalning.


![Image](assets/fr/28.webp)


Du kan också ange denna information manuellt via tangentbordet i fältet högst upp på Interface, eller ange en Lightning Address (BOLT12 eller LNURL). Du kan också klistra in informationen direkt med hjälp av knappen "*Pasta*".


![Image](assets/fr/29.webp)


I det här exemplet har jag skannat en Invoice för 10 000 Sats. För att göra betalningen klickar du bara på "*Pay*".


![Image](assets/fr/30.webp)


Transaktionen är genomförd.


![Image](assets/fr/31.webp)


Gratulerar, du vet nu hur du konfigurerar och använder Phoenix. Om du tyckte att denna handledning var användbar skulle jag vara tacksam om du lämnar en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack för att du delar med dig!


För att ta saker ett steg längre, kolla in den här handledningen om Alby Hub, en annan innovativ och lättanvänd lösning för att starta din egen Lightning-nod:


https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Och för att ta reda på mer om den tekniska driften av Lightning Network kan du hitta Fanis Michalakis utmärkta gratisutbildning på Plan ₿ Network :


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb