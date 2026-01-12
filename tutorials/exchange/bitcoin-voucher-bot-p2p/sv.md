---
name: BitcoinVoucherBot P2P
description: Hur man köper och säljer Bitcoin P2P med BitcoinVoucherBot
---

![image](assets/cover.webp)



Vi hör fortfarande om BitcoinVoucherBot, en Telegram-bot skapad för att köpa Bitcoin utan [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) via SEPA-banköverföring. Tyvärr, från och med november 2025, är BitcoinVoucherBot i sin centraliserade form inte längre tillgänglig som en tjänst utan KYC.



I den här guiden kommer vi att titta på hur den nya implementeringen fungerar som gör det möjligt för användare att köpa och sälja Bitcoin direkt på den nya P2P (Peer-To-Peer) marknadsplatsen, så ingen KYC. För att motverka nya restriktioner som alltmer hotar digital frihet och integritet skapade utvecklarna detta tillägg, vilket ger användarna möjlighet att köpa och sälja Bitcoin med en hög grad av anonymitet genom P2P (Peer-To-Peer). Låt oss tillsammans se hur denna nya utbytesmetod fungerar.



För att använda tjänsten måste du göra överföringar via Lightning Network. Se därför till att du har en wallet som stöder det här protokollet och som låter dig använda en "LNURL" eller "Lightning Address" för att ta emot och skicka pengar.



Bland de plånböcker som stöds kan vi hitta:





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Vårdnadshavare)
- [Wallet av Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (depåförvaring med swap till icke depåförvaring)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



Eller någon wallet som har en "Lightning Address" och genererar en Bolt11-faktura. plånböcker som generate en Bolt12-faktura stöds inte för närvarande. För mer information se definitionen av [Bolt](https://planb.academy/resources/glossary/bolt).



I den här handledningen kommer vi att använda Wallet of Satoshi, eftersom den är lätt att använda direkt.



**Försiktighet**: Wallet of Satoshi, även om den är populär bland nybörjare, är förvaring, med begränsad kontroll över medel; använd den endast tillfälligt och överför omedelbart till en icke-förvaring för full suveränitet. Från och med oktober 2025 innehåller den ett stabilt självförvaltande läge över hela världen på iOS/Android (uppdatera appen), med autonoma privata nycklar, växling mellan lägen, anpassade blixtadresser och seed 12-ordssäkerhetskopiering. Det förblir dock en tillfällig lösning fram till konsolidering, där man föredrar wallet non-custodial mature för långsiktig hantering.



Mycket bra! Nu kan vi börja vår resa, som kommer att vägleda dig steg för steg när du skapar ditt konto, hanterar köp- och säljmatchningar och använder ditt begränsade område.



## Wallet och inskrivning



Om du inte redan har det installerat på din smartphone ska du först ladda ner Wallet of Satoshi.





- [Google Play](https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Om du aldrig har använt Wallet of Satoshi och vill förstå hur det fungerar föreslår jag att du följer den här handledningen så att du kan aktivera det på rätt sätt och säkerhetskopiera det på ett säkert sätt.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Nu när din wallet är klar kan du börja skicka en liten mängd sats. Tänk på att du, för att slutföra din P2P (Peer-To-Peer) plattformsregistrering, kommer att behöva skicka 1000 sats som en kontrollåtgärd: detta är för att skapa en barriär mot eventuella attacker av typen fantommatchning (bluff), vilket förhindrar att någon registrerar sig utan något spamfilter.



![image](assets/it/02.webp)



Vi kan nu öppna P2P (Peer-To-Peer)-plattformen för att fortsätta med registreringen. Du kan logga in från stationära datorer eller webbläsare på smartphones, via Telegram BitcoinVoucherBot eller via .onion-länkar för att ge en ännu högre nivå av integritet.



om du väljer att använda Tor .onion-länken rekommenderar jag också "Tor Browser". Om du inte känner till det ännu kan du lära dig mer om det på den här länken:



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Välj nu hur du vill nå plattformen.





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Desktop / Webbläsare Smartphone](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Du kommer att omdirigeras till huvudsidan.



tryck på "Get Starter" för att komma igång direkt



![image](assets/it/03.webp)



På nästa skärm måste du välja ett lösenord och ange det (ruta A) och sedan upprepa det (ruta B). Jag rekommenderar att du omedelbart sparar lösenordet på ett backupmedium, t.ex. på en säker digital enhet som "Bitwarden":



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

eller spara ditt lösenord på ett pappersmedium (**varning**: detta är inte en bra lösning, det är dock okej om det är avsett som en tillfällig lösning).



Kryssa i kontrollrutan där du intygar att du inte är en robot (ruta C). Observera Aktivera inte RSA-kryptering om du inte vet exakt vad det är och hur det fungerar. Du behöver inte göra någonting i det här skedet. Klicka på "Generate Avatar" ("Generera avatar") (ruta D).



![image](assets/it/04.webp)



Nu måste du betala 1000 sats för att slutföra registreringen.



1. Börja uppifrån och se först ditt slumpmässigt genererade och extremt viktiga "Avatar ID" Spara det noggrant, precis som jag rådde dig att göra med lösenordet.


2. Du måste sedan ange din "Lightning Address" i fältet nedan. Detta gör att du kan ta emot betalningar om du köper Bitcoin, eller få återbetalningar. Om du använder Wallet eller Satoshi kommer du att kunna kopiera din Address genom att klicka på receive.


3. Kryssa i verifieringsrutan där du anger att du inte är en robot.


4. Gör betalningen på 1000 sats för att få tillgång till ditt begränsade område. Om du inte kan rama in den, klicka på den med musen (på PC) eller tryck på den med fingret (på webbläsare/Telegram smartphones) för att kopiera adressen som du behöver klistra in i Wallet of Satoshi och slutföra fakturabetalningen.



![image](assets/it/05.webp)



Det här är din LNURL Address.



![image](assets/it/06.webp)



Gratulerar!!! Du har skapat din Avatar permanent och du kan se sammanfattningen här. Återigen rekommenderar jag att du sparar både din avatar och ditt lösenord, som jag har föreslagit tidigare.



Klicka på "Jag har sparat mina inloggningsuppgifter, fortsätt" (översatt som: "Jag har sparat mina inloggningsuppgifter, fortsätt")



![image](assets/it/07.webp)



Du befinner dig nu i hjärtat av plattformen, där du kan se alla handelsmatchningar med deras detaljer. För en tydligare bild ser du nedan de bilder som finns på webbplatsen från stationära datorer.





- "Type" ("Type") definierar om det är en "Sell" ("sälj") försäljning eller ett "buy" köp
- "Amount" ("Belopp"): anger hur många sats som användaren säljer om matchningen är av typen "Sell", eller hur många Bitcoin som användaren är villig att köpa om matchningen är av typen "Buy".
- "BTC Price with Margin" ("BTC Price with Margin"): visar priset med hänsyn till den marginal som tillämpas över det markerade värdet.
- "Marginal" ("Margin") är den procentsats som tillämpas på marknadspriset, Med ett minustecken (-) får du en rabatt på marknadspriset, Med ett plustecken (+) tillämpas en premie på marknadspriset.
- "Metod" ("Metod") anger med vilken metod användaren föredrar att bli betald.
- "Creator" är den unika avatar som användaren använder på plattformen.
- "Rep" (Reputation) Användarens reputationsnivå sträcker sig från -5 opålitlig till +5 extremt pålitlig.
- "Status" ("Status"): anger matchens status. I exemplet på skärmdumpen verkar alla matcher vara "Open" ("Öppna").
- "Expiration" ("Expiration"): visar hur mycket tid som återstår innan matchen löper ut och avbryts om den inte valdes av någon.



![image](assets/it/08.webp)



Klicka på din avatar längst upp till höger för att komma till din profil.



![image](assets/it/09.webp)



Här kan du se ditt Avatar-namn, användar-ID, skapandedatum och rykte, som kommer att återspegla positivt eller negativt på ditt beteende i förhandlingar.



![image](assets/it/10.webp)



I avsnittet Inställningar kan du se din "Lightning Address", som du angav under registreringen, och ändra den vid behov. Du har också möjlighet att skapa en offentlig nyckel, som du som sagt bara bör göra om du har rätt kunskaper. Den används för att kryptera de meddelanden som du kommer att utbyta med din motpart direkt från din dator.



Telegram Notifieringsfunktionen rekommenderas starkt. Genom att aktivera den visas en QR-kod som du kan rama in med Telegram-appen: på så sätt får du realtidsaviseringar om alla åtgärder relaterade till dina matcher, direkt i botchatten på Telegram.



![image](assets/it/11.webp)



Slutligen hittar du din värvningssektion, med de intäkter som genereras av de användare du har bjudit in. Härifrån kan du använda knappen för att dela din länk eller QR-kod och, lite längre ner, visa en lista över matcher för att spåra ditt rykte tillsammans med motsvarande poäng.



![image](assets/it/12.webp)



## Skapa en order för att köpa Bitcoin



Gå in på Marketplace: från huvudnavigeringsfältet klickar du på vagnssymbolen "Marketplace"("Marketplace") för att öppna orderboken. starta sedan en ny order: tryck på knappen "Ny order" ("Ny order") för att starta processen.



![image](assets/it/13.webp)





- Ange orderinformation:
- Välj alternativet "Köp Bitcoin"("Köp Bitcoin").
- Ange det antal sats som du vill ha.
- Definiera prismarginalen (mellan -20% och +20% från marknadsvärdet).
- Välj betalningsmetod (Instant SEPA, etc.).
- Anger önskad valuta.
- Bekräfta order: klicka på "Skapa order"("Bekräfta order") för att gå vidare till arkiveringsfasen.



![image](assets/it/14.webp)



Deposition krävs: en deposition motsvarande 10% av det totala beloppet, plus en serviceavgift, krävs för att aktivera beställningen.




- Depositionsbetalning: när ordern skapas genererar systemet automatiskt en Lightning-faktura. Depositionen är endast tillfällig och återbetalas när ordern är slutförd.
- Huvudsakliga egenskaper:
- Säkerhetsdeposition: 10% av ordervärdet.
- Serviceavgift: kostnad för att använda plattformen.
- Tidsgräns: Du har 5 minuter på dig att genomföra betalningen, annars förfaller transaktionen.



![image](assets/it/15.webp)



Efter genomförd betalning kommer ordern att visas i boken och vara synlig för alla användare, som kan välja och acceptera den. För att skapa en säljorder behöver du bara klicka på "Sälj Bitcoin" ("Sell Bitcoin"), ange den mängd satoshi du vill sälja, ange marginalen, välja betalningsmetod och valuta och sedan fortsätta med insättningen på 10 % som en säkerhetsdeposition. När du är klar kommer din matchning att synas i listan.



![image](assets/it/16.webp)



## Hur man accepterar en order



1. Säljarna kan se en lista över alla tillgängliga order i boken.


2. Kontrollera detaljerna: varje order visar information som t.ex:




  - Kvantitet av Bitcoin,
  - Marginal på priset,
  - Betalningsmetod,
  - Användarens rykte.



![image](assets/it/17.webp)



3. Klicka på ordern för att öppna det fullständiga bladet med all information.


4. Tryck på "Sälj Bitcoin"("Sälj Bitcoin") för att acceptera förslaget.



![image](assets/it/18.webp)



## Deposition krävs av säljaren



När ordern är accepterad genererar systemet en faktura för betalning. Depositionen inkluderar:



- Det totala beloppet för beställningen,



- servicekommissionen.



Depositionsbetalningen måste göras inom den angivna tidsfristen, annars kommer transaktionen inte att bekräftas.



![image](assets/it/19.webp)



## Skicka betalningsinstruktioner



Efter att insättningen har gjorts visas transaktionen i säljarens personliga instrumentpanel, som måste tillhandahålla detaljerna till köparen för att slutföra betalningen i fiatvaluta.



1. Säljaren visar den aktiva transaktionen i sin panel.


2. Klicka på "Skicka betalningsinstruktioner"


3. Ange all nödvändig information för fiat-betalningen (IBAN, mottagare, adress, orsak till betalningen etc.).


4. Klicka på "Skicka meddelande"("Send Message") för att överföra uppgifterna till köparen.



![image](assets/it/20.webp)



## Betalningsförfarande



Köparen får, inom plattformens chatt, ett meddelande med alla nödvändiga uppgifter för att göra betalningen i fiatvaluta:




- Bankuppgifter: IBAN med namn och adress till säljarens kontoinnehavare.
- Exakt belopp: exakt fiatbelopp som ska överföras.
- Causal/description: text som ska ingå i transaktionen.
- Tidsfrist: tidsfrist inom vilken betalningen ska vara genomförd.



Överföringen sker utanför P2P-systemet och måste göras via den egna bankinstitutionen.



⚠️ **Viktigt att notera:** bekräftelse på plattformen bör göras först efter att du faktiskt har ordnat överföringen eller fiat-betalningen via din bank.



![image](assets/it/21.webp)



## Bekräftelse av betalning fiat



Detta steg är avgörande för köparen och bör utföras först efter att man har kontrollerat att betalningen faktiskt har skickats.



1. Mottagningsdata: köparen har mottagit betalningsinstruktioner från säljaren.


2. Betalningsutförande: fiat-överföring ordnas från ens bankkonto.


3. Verifiering: kontrollera att operationen har behandlats korrekt.


4. Bekräfta på plattformen: klicka på "Bekräfta fiat-betalning"("Bekräfta fiat-betalning") på handelssidan.


Knappen "Confirm Payment fiat" visas i transaktionsavsnittet och ska endast användas efter att du har kontrollerat att betalningen verkligen har skickats.



![image](assets/it/22.webp)



Det sista steget i processen är att säljaren bekräftar mottagandet av fiat-betalningen, varefter satss släpps till köparen.



![image](assets/it/23.webp)



## Slutsats



I hopp om att denna handledning kommer att hjälpa dig att använda en ny metod för att handla Bitcoins eller till och med bara köpa dem, antingen för din egen värdebutik eller för att börja få dagliga betalningar till liv. Ändå är det fortfarande en dörr att utforska för att klara av vad som håller på att hända i vår digitala värld.



Snaran som drivs av de organ som kontrollerar oss dras åt för att föda ett alltmer kontrollerat internet. Genom att köpa P2P kommer du att hålla dina inköp i total anonymitet, utan att lämna några spår och inga uppföljande återverkningar från tredje part.