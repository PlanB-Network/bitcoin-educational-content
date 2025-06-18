---
name: BitcoinVoucherBot
description: En Telegram-bot för att köpa Bitcoin i sekretess
---
![image](assets/cover.webp)


_Den här handledningen skrevs av_ [Bitcoin Campus] (https://linktr.ee/bitcoincampus_)


# Inledning


BitcoinVoucherBot är ett verktyg med vilket Bitcoins kan köpas i Exchange för euro.


### KYC Ljus


Handlingen att byta euro mot Bitcoin är det första och mest grundläggande steget för att börja studera detta ämne, men det är tydligen också det svåraste och mest komplexa. Det kan finnas många alternativ: att erbjuda Bitcoin genom centraliserade utbyten, Bitcoin-tema möten, vänner, bekanta och mer. Vi ansluter oss till Bitcoiner-samhället och ** vi rekommenderar absolut användning av centraliserade utbyten** för att skydda mer uppmärksamhet åt ens integritet.


Även om detta val kan vara mindre bekvämt är det viktigt att förstå att börserna tillämpar KYC-förordningen (Know Your Cutomer) och därmed tilldelar en identitet, liksom en fysisk plats, till varje Satoshi som köps från dem. "Bekvämlighet" har några slående biverkningar.


### Hur gör man det?


Här kommer tjänsten [BitcoinVoucherBot:] (https://t.me/BitcoinVoucherBot), en Telegram-bot som fungerar som en kanal mellan våra SEPA-överföringar och Sats-köp.


### Förkunskapskrav


För att börja använda BitcoinVoucherBot behöver du inte lämna ut känslig personlig information till Bot-personalen. ** Ingen auktorisering behövs **.


Allt som behövs är ett redan aktivt Telegram-konto och ett bankkonto. **Anmärkning**: Ett konto som öppnats hos Poste Italiane (för italienska kunder) eller, mer allmänt, som hänvisar till ett laddningsbart kort är inte lämpligt.


I Telegram-chatten förbereder vi en beställning, med en banköverföring betalar vi för den, och slutligen genom botten får vi en kupong utfärdad av ett tredjepartsföretag som inte känner till föremålet för köpet.


### Botaktivering och meny


Aktivering är en enkel engångsoperation. Från Telegram, sök efter _@BitcoinVoucherBot_ och så snart du kommer till Bot-chatten, sticker en stor _Start / Start_-knapp ut längst ner. Operationen får Bot att svara, vilket presenterar en meny med de viktigaste kommandona som är tillgängliga för den. De första välkomstmeddelandena visas också, som vi rekommenderar att du läser noggrant.


** Varning **: det finns flera bedragare som poserar som original VoucherBot. Om du inte är säker på sökningen via Telegram, vänligen gå till länken BitcoinVoucherBot från [officiell webbplats](https://www.bitcoinvoucherbot.com/)


![image](assets/it/01.webp)


Alternativ visas genom att klicka på knappen _Menu_ i det nedre vänstra hörnet: du kan klicka på det ord som motsvarar kommandot eller skriva in snedstrecket `/` följt av det skrivna kommandot i meddelanderutan.


![image](assets/it/02.webp)


Större verksamheter inkluderar:




- _/purchase_: är det faktiska inköpsförfarandet. När transaktionen är slutförd genereras QR-koden automatiskt av botten, redo för inlösen.
- _/refill_: finns tillgängligt när denna handledning skrivs, men vi kommer inte att ta upp det eftersom alternativet av tekniska skäl kan tas bort senare.
- _/swap_: öppnar bytesproceduren, som är tillgänglig antingen med en bekväm Telegram-bot eller via webben.
- _/ap_: ackumuleringsplan, som gör det möjligt för dig att upprätta en **Constant Accumulation Plan (CAP)**.
- _/lnaddress_: med vilken vi ombeds att koppla en egen LN Address, för ett särskilt förfarande som vi kommer att se senare.
- _/credits_: för att kontrollera hur mycket kredit som finns kvar till generate vouchers.
- _/myorders_: visar beställningar som gjorts med boten (** Varning** systemet spårar bara de senaste 10 beställningarna och inte hela historiken).
- _/fees_: ett kommando för att kontrollera nätverksavgifter. För att utvärdera dem är det alltid bäst att förlita sig på Mempool.space.
- _/support_: i händelse av behov, dyker upp kontakter för att rapportera problem till supportteamet.


# Bitcoin inköpsförfarande


## Förberedelse av order


Klicka på _/köpa_ i kommandomenyn


![image](assets/it/03.webp)


Ett antal möjligheter dyker upp, men vi väljer _BTC Vouchers_


![image](assets/it/04.webp)


BitcoinVoucherBot låter dig köpa Bitcoin onchain, Lightning och Liquid.


I detta skede väljer du _Onchain & Lightning 🔗⚡️_


![image](assets/it/05.webp)


Skärmen ändras snabbt och VoucherBot föreslår köpbeteckningar. De börjar från minst € 100.00 upp till € 900.00.


Vid ett första köp erbjuds endast valörerna 100,00 €, Onchain och Lightning. För att öka sekretessen föreslår vi att du väljer _Lightning ⚡️_


![image](assets/it/06.webp)


VoucherBot meddelar oss att ett första val har gjorts och att vi måste välja _Proceed_ för att bekräfta det


![image](assets/it/07.webp)


Nu gäller det att välja betalningsmetod. Överföringen sker genom banköverföring **(accepteras endast SEPA)**. VoucherBot föreslår som mottagare ett företag som tillhandahåller två bankkonton, ett i Storbritannien och det andra i Schweiz. Den schweiziska banken valdes för att genomföra denna handledning


![image](assets/it/08.webp)


Här uppmanas vi att ange vårt IBAN-nummer, det IBAN-nummer från vilket överföringen till den valda banken kommer att starta. Denna information utgör ett pussel som gör det möjligt för boten, dvs. en maskin, att sätta ihop viss information för att få köpprocessen att flyta utan att någon människa behöver ingripa.


IBAN måste skrivas i meddelandefältet, kontrolleras och skickas till botten.


![image](assets/it/09.webp)


Ett kontrollmeddelande visas nu i chatten med VoucherBot.


Om allt är korrekt fortsätter du genom att klicka på _Proceed_.


![image](assets/it/10.webp)


## Betalning


Efter några ögonblick, som är nödvändiga för att behandla uppgifterna, svarar VoucherBot med ett meddelande som innehåller alla detaljer som krävs för att slutföra beställningen. Beroende på vad din bank kräver är den relevanta informationen:




- `IBAN`, vilket är nödvändigt för insättningen, liksom för mottagarens Address;
- `det valda beloppet` tidigare genom cutoff, som måste uppfyllas för att VoucherBot ska kunna känna igen ordern när betalningen tas emot;
- `Payment reason`, vilket är anledningen till betalningen. **Måste kopieras och klistras in utan att ta bort eller lägga till något i det lämpliga fältet i din överföring. Eventuella "." eller "-" i betalningsorsaken kan ersättas med "vitt utrymme"**.
- ett unikt "OrderID" att hänvisa till vid begäran om hjälp.


Du kan sedan fortsätta med betalningen, via din app eller bank. När betalningen har accepterats av banken är det viktigt att komma ihåg att trycka på _Notify payment_ i chatten med VoucherBot. Denna enkla åtgärd varnar dig för att en betalning är på väg.


![image](assets/it/11.webp)


VoucherBot svarar med ett meddelande som innehåller en mycket viktig varning: **ta inte bort chatten**, åtminstone inte förrän vouchern har mottagits, eftersom det är det enda sättet att rekonstruera ordern och hålla den igång.


![image](assets/it/12.webp)


---
Vänligen notera:




- endast SEPA-banköverföringar accepteras;
- väntetiderna är enbart relaterade till hur bankerna (som inte arbetar 24/7/365 som Bitcoin) behandlar kupongen. Det kan ta från några timmar upp till 3 arbetsdagar att få vouchern;
- för alla behov har Bitcoin VoucherBot en utmärkt [support](https://t.me/BitcoinVoucherGroup) service på Telegram.


---
## Återlösen


Så snart betalningen är framgångsrik skickar Bitcoin VoucherBot kupongen direkt till chatten. Blixtkupongen är i form av en QR-kod, tryckt på en orange bakgrund.


![image](assets/it/31.webp)


Där finns alla uppgifter som behövs för att tjäna in pengarna:




- beloppet i Sats, motsvarande det som skickas via banköverföring, exklusive serviceavgifter och nätverksavgifter;
- ett referens-ID för vouchern;
- det datum då vouchern måste lösas in, annars går pengarna förlorade, dvs. 25 dagar efter utfärdandet.


Du kan lösa in värdebeviset genom att rama in QR-koden med skanningsfunktionen på en kompatibel Wallet Lightning Network, eller via LNURL, som också visas under QR-koden.


För denna handledning använde vi Wallet Of Satoshi, med hjälp av skanningsfunktionen som aktiveras av _Send_-tangenten


![image](assets/it/32.webp)


Med mobiltelefonens kamera aktiverad, rama in QR-koden i chatten, öppna Telegram från PC


![image](assets/it/34.webp)


Innan du fortsätter, Wallet Av Satoshi från en verifieringsskärm som inkluderar beloppet, som exakt matchar det belopp som uttrycks på kupongen och, som en beskrivning, BitcoinVoucherBot. För att ta ut kupongen, klicka helt enkelt på _Receive_


![image](assets/it/35.webp)


Wallet av Satoshi processer under några ögonblick


![image](assets/it/36.webp)


och slutligen rapporteras insamlingen och är omedelbart tillgänglig i Wallet-saldot.


**Wallet av Satoshi är en förvaringsapp: omedelbart efter att kupongen har lösts in är det lämpligt att flytta Sats till en Wallet som inte är förvaringsapp.**


![image](assets/it/37.webp)


### Hur man löser in en onchain-kupong


Som vi såg i orderförberedelserna tillåter VoucherBot Sats att köpas direkt på kedjan, med valet av den eponymous kupongen.


**Notera**: Orderberedning och betalning ändras inte, de är alltid desamma. Det som ändras är hur en onchain-voucher löses in.


Efter att ha slutfört beställningen, gjort betalningen, tryckt på _Notify payment_ och väntat på bankernas tekniska tid för att överföra överföringen, kommer VoucherBot att svara genom att skicka kupongen direkt till chatten.


Denna kupong är också i form av en QR-kod, men huvudfärgen är kanariegul och - viktigast av allt - i beskrivningen förklaras det väl att det är en onchain-kupong, som du löser in direkt på din Wallet onchain och för att starta utbetalningsproceduren måste du klicka på _Redeem on Telegram_. Onchain-kupongen innehåller också den information som redan har setts för blixten:




- beloppet i Sats, motsvarande det som skickas via banköverföring, exklusive serviceavgifter och nätverksavgifter;
- en kupongkod;
- ett referens-ID för vouchern;
- det datum då vouchern måste lösas in, annars går pengarna förlorade, dvs. 25 dagar efter utfärdandet.


![image](assets/it/22.webp)


** VARNING ⚠️:** klickade som förklarat, pop-up av en annan bot öppnas: ** Voucher RedeemBot.**


Voucher RedeemBot är det verktyg som görs tillgängligt för detta ändamål. Oavsett om detta är första gången eller om det finns tidigare beställningar, måste du alltid klicka på _START_ varje gång en ny inlösen görs.


![image](assets/it/23.webp)


Vid denna tidpunkt laddar RedeemBot onchain-kupongen, lätt igenkänd av Voucher Code och referens-ID. Det låser också upp baren för att skriva meddelanden och börja chatta med boten, som i själva verket inbjuder oss att berätta en onchain Address av vår Wallet.


**Anmärkning**: Denna Address måste vara av typ SegWit.


![image](assets/it/24.webp)


Vi öppnar vår Wallet vid denna tidpunkt och generate en SegWit Address


![image](assets/it/25.webp)


vi kopierar det


![image](assets/it/26.webp)


och klistra in den i chatten med RedeemBot


![image](assets/it/27.webp)


Vi har nu en kontrollskärm för att verifiera att kupongkoden är korrekt, liksom den Address som vi har kommunicerat till RedeemBot. Låt oss kontrollera det ordentligt, för genom att klicka på _Proceed_ startar transaktionen och det kommer inte att finnas något sätt att hitta den igen om vi till exempel har kommunicerat fel Address.


![image](assets/it/28.webp)


Transaktionen har startat och Redeem-proceduren för onchain-vouchern avslutas därmed.


![image](assets/it/29.webp)


medan beloppet kan ses komma i historien för vår Wallet.


![image](assets/it/30.webp)