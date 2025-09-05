---
name: Proton Wallet
description: Installera och använda Proton Bitcoin Wallet
---
![cover](assets/cover.webp)


Proton är ett schweiziskt företag som specialiserar sig på digital integritet och grundades 2014 av forskare från CERN. Proton är känt för sina lösningar med öppen källkod och erbjuder en rad tjänster, inklusive Proton Mail, Proton VPN och Proton Drive.


Proton introducerade nyligen Proton Wallet, en Bitcoin Wallet med öppen källkod och egen förvaring, tillgänglig som en mobilapp eller webbklient, länkad till ditt Proton-konto. Wallet:s funktioner är relativt klassiska för tillfället, med de väsentliga verktyg som förväntas av en bra Bitcoin Wallet, såsom RBF (* Replace-by-fee*), taggning eller möjligheten att lägga till en BIP39 passphrase.


Specialfunktionen i denna Wallet är möjligheten att skicka bitcoins med hjälp av mottagarens e-post Address, för vilken Proton automatiskt genererar en tom Bitcoin Address länkad till användarens Wallet. Proton planerar att lägga till nya funktioner i framtiden, inklusive Lightning och coinjoins (förmodligen med Whirlpool, som föreslagits av aktivitet på deras GitHub-arkiv).


## Skapa ett Proton-konto


För att använda Proton Wallet behöver du ett Proton-konto. Du kan skapa ett gratis genom att följa de första stegen i denna handledning som är avsedd för att skapa en Proton-brevlåda (endast avsnittet "* Skapa ett Proton-konto*"). När ditt konto har konfigurerats kan du fortsätta med resten av denna handledning.


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

## Anslut till Proton Wallet


Gå till [Proton Wallet:s webbplats] (https://proton.me/Wallet) och klicka på knappen "*Get Proton Wallet*".


![Image](assets/fr/01.webp)


Välj prenumerationsalternativet "*Free*" och klicka sedan på "*Sign In*".


![Image](assets/fr/02.webp)


Ange den e-postadress och det lösenord som är kopplat till ditt Proton-konto för att logga in.


![Image](assets/fr/03.webp)


Ditt konto bör nu visas. Klicka på "*Börja använda Proton Wallet nu*".


![Image](assets/fr/04.webp)


## Skapa en Bitcoin Wallet


Välj standard fiatvaluta för ditt konto och klicka sedan på "*Create new Wallet*".


![Image](assets/fr/05.webp)


Din Bitcoin Wallet har nu skapats. Du kan teoretiskt sett börja använda den omedelbart, men det är mycket viktigt att du sparar din Mnemonic först. Detta gör du genom att klicka på "*Säkra din Wallet*" i det övre högra hörnet på Interface.


![Image](assets/fr/06.webp)


Om du inte redan har gjort det på Proton kommer du att bli ombedd att skapa en säkerhetskopia för ditt konto och säkra det med en 2FA-metod. Dessa säkerhetsåtgärder, även om de är tillämpliga på hela ditt Proton-konto, är ännu mer relevanta när din Bitcoin Wallet är integrerad i det. Jag rekommenderar starkt att du implementerar dem.


![Image](assets/fr/07.webp)


För att spara din Mnemonic-fras klickar du på "*Backup this Wallet's seed phrase*".


![Image](assets/fr/08.webp)


Ange ditt lösenord för Proton.


![Image](assets/fr/09.webp)


Klicka sedan på "*Visa Wallet seed fras*" för att visa din Wallet:s Mnemonic fras.


![Image](assets/fr/10.webp)


Proton Wallet visar din 12-ords Mnemonic fras. **Den här Mnemonic ger dig full, obegränsad tillgång till alla dina bitcoins**. Vem som helst som har den här frasen kan stjäla dina pengar, även utan tillgång till ditt Proton-konto. Frasen på 12 ord kan användas för att återställa åtkomsten till dina bitcoins om du förlorar åtkomsten till ditt konto. Det är därför mycket viktigt att spara den noggrant och förvara den på en säker plats.


Du kan skriva det på ett papper, eller för extra säkerhet rekommenderar jag att du graverar det på en bas av rostfritt stål för att skydda det mot brand, översvämning eller kollaps.


![Image](assets/fr/11.webp)


För mer information om det rätta sättet att spara och hantera din Mnemonic-fras rekommenderar jag starkt att du följer den här andra handledningen, särskilt om du är nybörjare:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

du ska naturligtvis aldrig ta en bild av dessa ord, till skillnad från vad jag gör i den här handledningen


Klicka på knappen "*Done*" när du har sparat din fras.


![Image](assets/fr/12.webp)


## Upptäck Interface


Proton Wallet:s Interface är mycket intuitiv. Till vänster hittar du dina olika plånböcker och deras tillhörande konton. Kontot "*Primary*" är ditt huvudkonto. Av sekretesskäl placeras bitcoins som tas emot via Proton-mejlet Address på ett separat konto med namnet "*Bitcoin via e-post*".


![Image](assets/fr/13.webp)


För att lägga till ett nytt konto, klicka på "*Lägg till konto*".


![Image](assets/fr/14.webp)


För att skapa en ny Wallet, klicka på symbolen "*+*" bredvid "*Wallets*".


![Image](assets/fr/15.webp)


Det är här du kan lägga till en BIP39 passphrase till en ny Wallet.


![Image](assets/fr/16.webp)


För att fördjupa dina kunskaper om passphrase rekommenderar jag den här handledningen:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Ta emot bitcoins


För att ta emot bitcoins i din Wallet väljer du önskat konto till vänster om Interface och klickar sedan på knappen "*Receive*".


![Image](assets/fr/17.webp)


Protonen Wallet genererar sedan automatiskt en ny, tom Address.


![Image](assets/fr/18.webp)


När transaktionen har slutförts hittar du den i avsnittet "*Transaktioner*". Klicka på "*+Add*" för att tilldela transaktionen en etikett.


![Image](assets/fr/19.webp)


## Skicka bitcoins


Nu när du har bitcoins i din Wallet kan du skicka dem. Välj det konto du vill ha på vänster sida av Interface och klicka sedan på "*Sänd*".


![Image](assets/fr/20.webp)


Ange mottagarens Bitcoin Address. Du kan skanna en QR-kod genom att klicka på den lilla logotypen. För att skicka till ett e-postmeddelande Address, ange det direkt i detta fält. När du har angett Bitcoin Address klickar du på den lilla pilen och sedan på "*Bekräfta*".


![Image](assets/fr/21.webp)


Ange det belopp som ska skickas, antingen i fiatvaluta eller i bitcoins, och klicka sedan på "*Review*".


![Image](assets/fr/22.webp)


Välj transaktionsavgift baserat på den aktuella marknadssituationen.


![Image](assets/fr/23.webp)


Lägg till en etikett på din transaktion och dubbelkolla sedan alla detaljer. Om allt är korrekt klickar du på "*Bekräfta och skicka*" för att signera och skicka transaktionen.


![Image](assets/fr/24.webp)


Din transaktion kommer nu att visas i väntan på bekräftelse i avsnittet "*Transaktioner*" på ditt konto.


![Image](assets/fr/25.webp)


## Logga in på applikationen


Förutom webbklienten är Proton Wallet också tillgänglig via en mobilapplikation. Genom att länka Wallet till ditt Proton-konto kan du synkronisera din Wallet mellan webbklienten och mobilappen.


Ladda ner Proton Wallet från din applikationsbutik:




- [På App Store] (https://apps.apple.com/us/app/proton-Wallet-secure-btc/id6479609548);
- [I Google Play Store] (https://play.google.com/store/apps/details?id=me.proton.Wallet.android).


![Image](assets/fr/26.webp)


Efter installationen klickar du på "*Log in*" och anger din e-post Address och Proton-lösenord.


![Image](assets/fr/27.webp)


Du får då tillgång till din Bitcoin Wallet, med samma funktioner som i webbklienten.


![Image](assets/fr/28.webp)


Gratulerar, du vet nu hur du ställer in och använder Proton Wallet. Om du tyckte att den här handledningen var användbar skulle jag vara tacksam om du lämnar en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack för att du delar med dig!


Om du vill gå längre rekommenderar jag den här handledningen om Jade Plus, Blockstreams senaste Hardware Wallet:


https://planb.network/tutorials/wallet/hardware/jade-plus-sparrow-938abf16-e10a-4618-860d-cd771373a262