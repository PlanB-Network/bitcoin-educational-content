---
name: Satscard
description: Konfigurera och använda ett Satscard med Nunchuk
---
![cover](assets/cover.webp)


Bitcoin är ett elektroniskt kontantsystem som gör det möjligt för oss att utföra peer-to-peer-transaktioner. För att vara övertygad om att en transaktion är oföränderlig är det dock nödvändigt att vänta på flera bekräftelser (vanligtvis 6) för att undvika att avsändaren försöker spendera dubbelt. Denna valideringsfördröjning kan ibland vara obekväm, särskilt när man vill ha en omedelbar slutgiltighet som liknar fysiska kontanter. Till skillnad från kontanter, där innehavet av en sedel överförs omedelbart, innebär Bitcoin-transaktioner en väntetid innan de definitivt anses vara oåterkalleliga.


Det är här Satscard kommer in i bilden. Det erbjuder en metod för att möjliggöra fysisk och omedelbar överföring av bitcoins, utan att behöva utföra en On-Chain-transaktion. Satscard fungerar som ett innehavarkort som möjliggör säker överföring av Bitcoin Ownership, och erbjuder därmed en upplevelse som ligger närmare traditionella kontanter. I denna handledning kommer jag att introducera dig till denna lösning.


## Vad är ett Satscard?


Satscard från Coinkite är efterföljaren till Opendime. Det är ett NFC-kort som möjliggör fysisk överföring av bitcoins, på samma sätt som en sedel eller ett mynt. Till skillnad från ett traditionellt Hardware Wallet är Satscard ett bärarkort, vilket innebär att fysisk besittning av kortet motsvarar Ownership av de bitcoins som är säkrade med nycklarna som lagras på det. Priset varierar mellan 6,99 USD och 17,99 USD beroende på vilken design som väljs.


![SATSCARD](assets/notext/01.webp)


Satscard-chipet är utrustat med 10 kortplatser, vilket gör att det kan lagra bitcoins upp till 10 gånger på 10 olika adresser. Varje kortplats fungerar självständigt och ska teoretiskt sett bara användas en gång för att låsa in bitcoins i den. För att spendera bitcoins är det bara att öppna luckan med en kompatibel applikation, t.ex. Nunchuk, genom att ange den 6-siffriga verifieringskoden som anges på baksidan av Satscard.


Kortet säkerställer att den privata nyckeln som säkrar bitcoins på Blockchain inte kan behållas av den tidigare ägaren när de fysiskt delar med sig av kortet. Mottagaren kan också verifiera giltigheten av en slot och det belopp som lagras i den vid tidpunkten för Exchange.


Detta system är särskilt användbart för att köpa fysiska varor med bitcoins eller för att ge bitcoins som en gåva.


## Hur köper man ett Satscard?


Satscardet finns att köpa [på Coinkites officiella webbplats](https://store.coinkite.com/store/category/satscard). Om du vill köpa det i en fysisk butik kan du också hitta [listan över certifierade återförsäljare](https://coinkite.com/resellers) på webbplatsen.

Du behöver också en telefon som är kompatibel med NFC-kommunikation eller en USB-enhet som kan läsa NFC-kort på standardfrekvensen 13,56 MHz.

## Hur laddar man en kortplats på ett Satscard?


När du har fått ditt Satscard är det första steget att kontrollera förpackningen för att säkerställa att den inte har öppnats. Om paketet är skadat kan det tyda på att kortet har äventyrats och kanske inte är äkta.


För att hantera Satscard kommer vi att använda mobilapplikationen **Nunchuk Wallet**. Se till att din smartphone är NFC-kompatibel och ladda sedan ner Nunchuk från [Google Play Store] (https://play.google.com/store/apps/details?id=io.nunchuk.android), [App Store] (https://apps.apple.com/us/app/nunchuk-Bitcoin-Wallet/id1563190073) eller direkt via dess [`.apk`-fil] (https://github.com/nunchuk-io/nunchuk-android/releases).


![SATSCARD](assets/notext/02.webp)


I teorin kan du skicka bitcoins direkt till den Address som anges på baksidan av ditt Satscard utan att använda Nunchuk. Jag avråder dock från att göra detta, eftersom vi först kommer att verifiera att Address i den första luckan verkligen härrör från en privat nyckel som lagras på Satscard och att det inte är en bedräglig Address.


Om du använder Nunchuk för första gången kommer appen att erbjuda dig att skapa ett konto. I den här handledningen är det inte nödvändigt att skapa ett konto. Välj därför "*Fortsätt som gäst*" för att fortsätta utan konto.


![SATSCARD](assets/notext/03.webp)


Klicka sedan på "*Unassisted Wallet*".


![SATSCARD](assets/notext/04.webp)


Klicka sedan på knappen "*Jag utforskar på egen hand*".


![SATSCARD](assets/notext/05.webp)


När du är på Nunchuks startskärm klickar du på "*NFC*"-logotypen längst upp på skärmen.


![SATSCARD](assets/notext/06.webp)


Håll ditt Satscard mot baksidan av din telefon för att skanna det.


![SATSCARD](assets/notext/07.webp)


Nunchuk visar den mottagande Address som motsvarar den första kortplatsen på ditt Satscard. Normalt ska denna Address vara identisk med den som manuellt skrivs på baksidan av ditt kort. Kopiera denna Address och använd den för att överföra de bitcoins som du vill låsa med denna kortplats.


![SATSCARD](assets/notext/08.webp)


## Hur kontrollerar jag bitcoins på en spelautomat?


När transaktionen är bekräftad kan du kontrollera saldot som är kopplat till en kortplats på ditt Satscard genom att skanna det med Nunchuk. Under en transaktion kan alltså mottagaren av bitcoins omedelbart verifiera, via sin Nunchuk-app, att kortet verkligen innehåller de bitcoins som de är skyldiga.


![SATSCARD](assets/notext/09.webp)

Om motparten inte har Nunchuk-appen kan de ändå verifiera Satscardets giltighet. Man aktiverar helt enkelt NFC på sin smartphone och placerar Satscard på baksidan av enheten. Detta öppnar automatiskt Satscards webbplats i en webbläsare, där man kan kontrollera kortets giltighet samt det belopp i bitcoins som är kopplat till det.

![SATSCARD](assets/notext/10.webp)


## Hur tar man ut bitcoins från en spelautomat?


Nu när Satscards första kortplats har laddats med en viss mängd bitcoins kan du lämna över kortet till betalningsmottagaren.


![SATSCARD](assets/notext/11.webp)


Om du är mottagaren måste du installera Nunchuk. När du är inne i appen klickar du på "*NFC*"-logotypen längst upp på skärmen.


![SATSCARD](assets/notext/12.webp)


Placera ditt Satscard på baksidan av din telefon.


![SATSCARD](assets/notext/13.webp)


Nunchuk visar det belopp som säkrats på Address.


![SATSCARD](assets/notext/14.webp)


För att avsegla den privata nyckeln och flytta bitcoins till en Address som du äger, klicka på knappen "*Avsegla och svep saldo*".


![SATSCARD](assets/notext/15.webp)


Med alternativet "*Sweep to a Wallet*" kan du direkt skicka bitcoins till en Wallet som redan finns i din Nunchuk-app. Om du vill överföra pengarna till en annan mottagande Address väljer du "*Withdraw to an Address*".


![SATSCARD](assets/notext/16.webp)


Ange den mottagande Address där du vill skicka bitcoins som säkrats av Satscard. Kontrollera att den angivna Address är korrekt (det här är enda gången du kan verifiera den) och klicka sedan på knappen "*Skapa transaktion*".


![SATSCARD](assets/notext/17.webp)


Ange PIN-koden för ditt Satscard. Denna 6-siffriga kod finns noterad på baksidan av det fysiska kortet.


![SATSCARD](assets/notext/18.webp)


Håll ditt Satscard på baksidan av din smartphone medan du signerar transaktionen med den privata nyckeln som finns lagrad på NFC-kortet.


![SATSCARD](assets/notext/19.webp)


Din transaktion är nu signerad och sänds ut i Bitcoin-nätverket, vilket innebär att den plats som används på ditt Satscard nu är tom.


![SATSCARD](assets/notext/20.webp)


## Hur återanvänder man Satscard?


Till skillnad från engångslösningar som Opendime är Satscard utrustat med ett chip som innehåller 10 oberoende kortplatser, vilket möjliggör upp till 10 operationer med ett enda kort. Den första kortplatsen, som är förkonfigurerad i fabriken av Coinkite, motsvarar den mottagande Address som står på baksidan av ditt Satscard.


![SATSCARD](assets/notext/21.webp)

För att aktivera de övriga 9 platserna måste du använda nyckelparet generate och Address via Nunchuk-appen. På appens startsida klickar du på "*NFC*"-logotypen högst upp på skärmen.

![SATSCARD](assets/notext/22.webp)


Placera ditt Satscard på baksidan av din telefon.


![SATSCARD](assets/notext/23.webp)


Nunchuk indikerar att ingen slot är aktiv på kortet, vilket är normalt eftersom den första redan har använts och den andra ännu inte har genererats. För att se de tidigare använda kortplatserna, klicka på "*Visa öppna kortplatser*". Det rekommenderas starkt att inte återanvända dessa slots, eftersom detta skulle leda till Address-återanvändning som är skadlig för din On-Chain-integritet. Därför kommer vi att skapa en ny slot genom att klicka på knappen "*Yes*".


![SATSCARD](assets/notext/24.webp)


Du måste nu välja hur du generate din master chain-kod.


Kortplatserna på Satscard följer BIP32-standarden, vilket innebär att härledningen av de kryptografiska nycklar som säkrar bitcoins inte bygger på en Mnemonic-fras som i BIP39-plånböcker, utan direkt på en privat huvudnyckel och en huvudkedjekod. Dessa två Elements används som indata i HMAC-SHA512-funktionen för att generate skapa ett underordnat nyckelpar. Varje slot har sin egen huvudnyckel och sin egen huvudkedjekod. Det finns bara en härledningsnivå för varje slot.


Nyckelparet för den första kortplatsen är förgenererat av Coinkite. Det är därför du har direktåtkomst till det via Nunchuk, och det är därför den mottagande Address står på baksidan av NFC-kortet. För de andra kortplatserna är det dock du som ansvarar för att generera nycklarna.


Den privata huvudnyckeln för varje slot genereras direkt av Satscard, och huvudkedjekoderna måste tillhandahållas utifrån. För kedjekoden för din nya slot har du två alternativ: låt Nunchuk generate göra det automatiskt genom att välja "*Automatic*", eller skapa den själv genom att välja "*Advanced*" och ange den i det avsedda utrymmet. För att kedjekoden ska vara effektiv måste den vara så slumpmässig som möjligt.


![SATSCARD](assets/notext/25.webp)


Ange den 6-siffriga PIN-koden som finns på baksidan av Satscard.


![SATSCARD](assets/notext/26.webp)


Placera ditt Satscard på baksidan av din telefon.


![SATSCARD](assets/notext/27.webp)


En ny slot har framgångsrikt konfigurerats. Du kan nu se den mottagande Address som du kan sätta in bitcoins på. För att fortsätta med laddningen, följ instruktionerna i avsnittet "*Hur laddar man en slot på ett Satscard?*" i denna handledning.

Du kan upprepa den här processen upp till 10 gånger på varje Satscard.


Grattis, du har nu lärt dig hur man använder Satscard! Om du tyckte att den här handledningen var till hjälp, skulle jag uppskatta om du kunde lämna en tumme upp nedan. Du får gärna dela den här artikeln på dina sociala nätverk. Tack så mycket!