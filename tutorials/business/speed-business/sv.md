---
name: Hastighet Wallet - PoS
description: Integrera enkelt betalningar med Bitcoin och stablecoin i din verksamhet
---
![cover](assets/cover.webp)



Den världsomspännande användningen av Bitcoin baseras på konkreta användningsfall i vardagen. Användningen av Bitcoin i omedelbara kommersiella transaktioner runt om i världen förstärker denna adoption hos både stora institutioner och små företag. I den här handledningen tittar vi på Speed Business, en enhetlig betalningsplattform som gör det möjligt för ditt företag att acceptera Bitcoin-betalningar via Lightning.



![btc-session](https://www.youtube.com/watch?v=ywUNZ_sxr0Q)



## Att komma igång med Speed Business



[Speed Business] (https://www.tryspeed.com/) är en plattform utvecklad av [Speed Wallet] (https://www.speed.app/) som gör det möjligt för alla handlare att integrera omedelbara, billiga Bitcoin- och stablecoin-betalningar.



Speed har ett brett utbud av funktioner för att täcka de ekonomiska aspekterna av ditt företag. Du kommer att hitta:





- Konfiguration av onlinebetalningar**: Ta emot betalningar från dina kunder var de än befinner sig, tack vare din webbplats.





- Betalningar på plats**: Perfekt för butiker och företag som tar emot kontanter i butiken.





- Uttag**: Ta ut dina tillgångar smidigt och använd dina bitcoins för att betala tillbaka dina kunder och löner.





- Koppling till andra plattformar**: Använder du externa verktyg för att hantera dina betalningar? Speed erbjuder dig möjligheten att ansluta dem till sin plattform, för ett allt-i-ett-ekosystem som speglar din verksamhet.



Skapa ditt konto på [Speed] (https://app.tryspeed.com/register/) så börjar vi lägga upp betalningar för ditt företag.



![account-creation](assets/fr/01.webp)



Ge information till Speed Wallet så att han kan hjälpa dig att förenkla plattformen enligt din erfarenhet av Bitcoin och Lightning Network



![onboard](assets/fr/02.webp)



Speed levereras med ett mjukvaruutvecklingskit som gör att du kan anpassa din integration och ett tillägg för standardintegration.



I den här handledningen kommer vi att arbeta med en standardintegration med hjälp av tillägget från Speed.



För att göra din upplevelse enklare erbjuder Speed ett testläge som låter dig prova de olika funktionerna utan att behöva oroa dig för deras inverkan på din butikshantering.



![test-data](assets/fr/03.webp)



Du kan testa alla aspekter som behandlas i den här handledningen med hjälp av testläget.



När du avaktiverar testläget måste du konfigurera din Wallet i uttaget.



![configure-wallet](assets/fr/04.webp)



Om du ännu inte äger en Bitcoin och/eller Lightning Wallet rekommenderar vi att du tar en titt på våra [mobila plånböcker] tutorials(https://planb.network/tutorials/wallet).



https://planb.network/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

⚠️ **VIKTIGT**: När du konfigurerar din Wallet ska du välja typen **BTC (On-Chain)** när du tar emot stora belopp, i storleksordningen tusentals euro, för att säkerställa tillförlitlig bekräftelse på Bitcoin, och typen **LN Address** när du vill ta emot omedelbara mikrobetalningar i din verksamhet.



![setup-wallet](assets/fr/05.webp)



Bekräfta sedan tillägget av din Wallet med hjälp av verifieringsmeddelandet som skickats av Speed.



![verfication](assets/fr/06.webp)



Definiera det lägsta uttaget och det lägsta saldo under vilket du inte kan ta ut dina tillgångar.



![payout](assets/fr/07.webp)



## Lägg till dina produkter



I avsnittet **Produkter** lägger du till din katalog med produkter som du säljer i din butik.



![product-creation](assets/fr/08.webp)



Tryck på **Nästa** för att fortsätta definiera din produkt och dess funktioner.



![product-details](assets/fr/09.webp)



Definiera sedan försäljningspriset för din produkt.



![product-price](assets/fr/10.webp)



Dessa produkter gör det möjligt för dig att generate betalningslänkar så att dina kunder kan betala för dem.



## Mottagande av betalningar



Speed Wallet ger dig möjlighet att använda flera metoder för att ta emot betalningar online eller på plats i ditt företag.



I menyn **Receive Payments > Payments** hittar du historiken för mottagna betalningar och deras status (betald, utgången, obetald, annullerad).



![payments](assets/fr/11.webp)





- Betalningslänkar finns i alternativet **Checkout Links** och gör det möjligt för dig att skapa unika betalningssidor för dina produkter.



![checkout-link](assets/fr/12.webp)



Beroende på dina behov kan du konfigurera och anpassa betalningssidan så att den tar emot betalningar på ett visst belopp.



![configure-checkout](assets/fr/13.webp)



![finalize-checkout](assets/fr/14.webp)



Du kan hitta listan över betalningslänkar som du har ställt in på ditt konto i menyn **Payment Links**.





- Fakturor: Speed låter dig generate offerter och fakturor till dina kunder.



![invoices](assets/fr/16.webp)



Välj en kund som du redan har registrerat, eller skapa enkelt en egen.



Genom att ange valuta får du tillgång till listan över produkter som konfigurerats i den valutan.



Du kan skicka denna Invoice i PDF-format, via e-post eller generate en QR-kodlänk att skanna (perfekt för butiker som samlar in på plats) så att din kund kan betala Invoice.



![configure-invoice](assets/fr/17.webp)






- I menyn **Payment Addresses** kan du skapa en Lightning Address till vilken du kan ta emot flera betalningar med olika belopp.



![addresses](assets/fr/19.webp)



⚠️ Du kan lägga till och använda andra domännamn än Speeds. För första gången rekommenderar vi dock att du använder standardkonfigurationen för att dra nytta av all den expertis som finns hos Speed Business tekniska support.





- Den **enda QR-koden**: Perfekt för betalningar på plats, skapa en QR-kod som är kopplad till ditt företag så att dina kunder kan betala för dina produkter.



![one-qr](assets/fr/20.webp)



## Gör betalningar från Speed



Speed business samlar inte bara in betalningar för ditt företag, det är en Wallet som låter dig hantera hela den finansiella sidan av ditt företag utan problem.



I menyn **Sänd betalningar** hittar du alla alternativ för överföring av pengar som Speed har att erbjuda.





- Omedelbara betalningar**: Med alternativet Instant Send kan du skicka bitcoins direkt från ditt handelskonto på ett säkert sätt.





- generate uttagslänkar** för att göra det möjligt för dina partners och leverantörer att få tillgång till sin betalning vid ett senare tillfälle utan att du behöver vara närvarande online.



I alternativet **Withdrawal Links** skapar du en ny uttagslänk och konfigurerar den sedan genom att ange valuta, belopp och ett lösenord för att säkra mottagarens transaktion.



![withdrawal-links](assets/fr/21.webp)



⚠️Les uttagslänkar kan endast användas en gång, vi rekommenderar starkt att du anger ett unikt lösenord för varje länk, annars kan vem som helst som har länken ta ut det belopp som anges på uttagslänken.





- Utbetalningar**: I menyn Utbetalningar initierar du uttag från ditt Speed Business-saldo till din personliga Wallet.



![payouts](assets/fr/22.webp)





- Rabatter**: Uppmuntra dina stamkunder genom att ställa in rabattalternativ för att tjäna bonusar.



![cashbacks](assets/fr/23.webp)



## Explorer Speed Business



Speed Business är en plattform för flera valutor som gör att du kan hålla separata plånböcker på ett enda system.



I alternativet **Balanser** hittar du saldot i dina plånböcker Bitcoin, USDT och USDC.



![balance](assets/fr/24.webp)



Precis som Speed Wallet, i **Swap**-menyn, låter Speed Business dig Exchange valutor mellan dina olika valutaplånböcker (BTC, USDT, USDC) för så lite som Sats 20 000 (cirka 20 $ till nuvarande kurs).



![swap](assets/fr/25.webp)



I menyn **Transfer** kan du kommunicera med andra handlare och enkelt överföra bitcoins med hjälp av deras Speed ID.



![transferts](assets/fr/26.webp)



I menyn **Kunder** kan du spara och se listan över dina kunder (privatpersoner eller företag).



![customers](assets/fr/27.webp)



Tjäna belöningar genom att delta i Speed's affiliateprogram.



I menyn **Partners** kan du bjuda in handlare att starta upp sin verksamhet på Speed business och få passiva inkomster.



![partners](assets/fr/28.webp)



## Integrera Speed i ditt företags webbplats



Speed Business har ett Development Kit som gör att du kan integrera betalningslösningen på din egen webbplats.



I menyn **Developers** skapar du dina offentliga och privata nycklar för att använda API-metoderna Speed Wallet.



Hitta den fullständiga [dokumentationen] (https://apidocs.tryspeed.com/reference/introduction) för en bättre integration av Speed Business.



![developers](assets/fr/29.webp)



## Anpassa ditt företag



I menyn **Settings** kan du konfigurera din handelsprofil och företagsinformation.



I avsnittet **Business Settings**:





- Redigera dina kontouppgifter för handlare, t.ex. namn, plats och tidszon.





- Kontrollera vilka behörigheter som är aktiverade (ta emot betalning, skicka Bitcoin, Exchange, överföring, uttag) på ditt konto i menyn **Kontostatus**.





- Definiera dina uttagsplånböcker i menyn **Payout Wallets** och konfigurera dem i menyn **Payout Scheduling**.





- Definiera de grafiska riktlinjerna för ditt företag och anpassa betalningssidor, e-postmeddelanden, QR-koder och fakturor efter dina önskemål i menyn **Branding**.





- Konfigurera betalningsmetoder i accepterade valutor i menyn **Payment Method**.



![payment-method](assets/fr/30.webp)



⚠️ Toleransen motsvarar den procentuella minskning som du accepterar på Invoice-beloppet för att en betalning ska anses vara giltig. Om din kund måste betala 100 USD och din tolerans är 1%, kommer varje betalning på 99 USD att validera Invoice på 100 USD.





Du har en bra förståelse för Speed, integrera Bitcoin i din verksamhet och utveckla din lokala cirkulära ekonomi baserat på Bitcoin. Om du tyckte att den här handledningen var användbar är vi säkra på att du kommer att tycka lika mycket om vår handledning om schweizisk Bitcoin-betalning.



https://planb.network/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a