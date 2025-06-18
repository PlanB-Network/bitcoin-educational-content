---
name: Sändebud
description: Konfigurera och använda ett pass med Envoy-applikationen
---
![cover](assets/cover.webp)


Envoy är en Bitcoin Wallet-hanteringsapplikation som utvecklats av Foundation. Den är speciellt utformad för att användas med Passport Hardware Wallet.


Passport "*Batch 2*" som presenteras i denna handledning med Envoy-appen är efterföljaren till "*Founder's Edition*". Den sticker ut med sin premiumdesign, högupplösta färgskärm och ergonomiska fysiska tangentbord. Den fungerar i "*Air-Gap*"-läge, vilket säkerställer att din Wallet:s privata nycklar förblir helt isolerade, med kommunikation möjlig via ett MicroSD-kort eller QR-koder. Enheten är utrustad med ett löstagbart, uppladdningsbart Nokia BL-5C-batteri med en kapacitet på 1200 mAh. Detta icke-proprietära batteri kan enkelt bytas ut, eftersom BL-5C-modellen är allmänt tillgänglig i butikerna.


När det gäller anslutningsmöjligheter är Passport utrustad med en MicroSD-port, en USB-C-port för laddning och en bakre kamera för att skanna QR-koder.


När det gäller säkerhet har Passport ett säkert element och enhetens källkod är helt öppen. Den erbjuder alla de funktioner som förväntas av en bra Bitcoin Hardware Wallet. Observera att Passport ännu inte stöder miniscript, men denna funktion är planerad till andra kvartalet 2025.


Med ett pris på 199 USD är Passport positionerad som en avancerad Hardware Wallet, som konkurrerar med Coldcard Q, Jade Plus, Tezor Safe 5 och Ledger:s toppmodeller.


![Image](assets/fr/01.webp)


För att hantera din säkra Wallet på ett Passport har du flera alternativ. Denna Hardware Wallet är kompatibel med de flesta Wallet-hanteringsprogram på marknaden, inklusive Sparrow Wallet, Spectre Desktop, Nunchuk, Keeper, bland andra.


I den här handledningen, som riktar sig till nybörjare och avancerade användare, kommer vi att upptäcka hur man använder Envoy-applikationen med din Passport. Det är det enklaste sättet att få ut så mycket som möjligt av din Hardware Wallet.


Om du är en avancerad användare och vill utforska mer komplexa funktioner rekommenderar jag att du tittar på den här andra handledningen där vi konfigurerar Passport med Sparrow Wallet:


https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

## Uppackning av passet


När du får ditt Passport ska du kontrollera att kartongen och Seal på kartongen är intakta för att bekräfta att paketet inte har öppnats. En programvaruverifiering av enhetens äkthet och integritet kommer också att utföras när den installeras.


![Image](assets/fr/02.webp)


Innehållet i lådan inkluderar :




- Pass;
- En bit kartong för att skriva ner din Mnemonic-fras;
- En USB-C-kabel för laddning;
- MicroSD-kort ;
- Två MicroSD till Lightning- eller USB-C-adaptrar ;
- Klistermärken.


På enheten hittar du :




- Ett tangentbord (1) ;
- USB-C-port (2);
- En raderingsknapp (3);
- A Returknapp (4) ;
- En bekräftelseknapp (5);
- Styrplatta (6);
- På/av-knapp (7);
- En statusindikator (8);
- MicroSD-port (9) ;
- En knapp för att ändra läge aA1 (10) ;
- En bakre kamera.


![Image](assets/fr/03.webp)


## Ladda ner Envoy-applikationen


Gå till din appbutik för att ladda ner Envoy :




- På [Google Play Store] (https://play.google.com/store/apps/details?id=com.foundationdevices.envoy);
- På [App Store] (https://apps.apple.com/us/app/envoy-by-foundation/id1584811818);
- På [F-Cold] (https://foundation.xyz/fdroid/).


![Image](assets/fr/50.webp)


Du kan också ladda ner APK-filen direkt [från Foundation's GitHub-arkiv] (https://github.com/Foundation-Devices/envoy/releases).


![Image](assets/fr/51.webp)


När applikationen är öppen väljer du "*Manage Passport*".


![Image](assets/fr/52.webp)


Välj om du vill aktivera Tor-anslutningen för att förstärka sekretessen och tryck sedan på "*Continue*".


![Image](assets/fr/53.webp)


Välj "*Connect an existing Passport*" om ditt Passport redan är konfigurerat, eller "*Set up a new Passport*" om du initierar din Hardware Wallet för första gången.


![Image](assets/fr/54.webp)


Acceptera användarvillkoren.


![Image](assets/fr/55.webp)


Du kommer sedan att bli ombedd att verifiera passets äkthet. Klicka på "*Nästa*".


![Image](assets/fr/56.webp)


## Starta pass


Tryck på på/av-knappen på sidan av enheten för att starta den.


![Image](assets/fr/04.webp)


Tryck på bekräftelseknappen för att komma till nästa meny.


![Image](assets/fr/05.webp)


I den här handledningen använder vi Envoy för att hantera den passsäkrade Wallet. Välj "*Envoy App*".


![Image](assets/fr/57.webp)


Klicka på "*Fortsätt på Envoy*".


![Image](assets/fr/58.webp)


Nästa steg är att kontrollera din enhet. Detta bekräftar att ditt pass är äkta och säkerställer att det inte har manipulerats under transporten. Du kommer att bli ombedd att skanna en QR-kod.


![Image](assets/fr/08.webp)


Skanna de dynamiska QR-koderna som visas i applikationen med ditt pass. När skanningen är klar klickar du på "*Nästa*".


![Image](assets/fr/59.webp)


Använd sedan din telefon för att skanna QR-koden som visas på ditt pass.


![Image](assets/fr/60.webp)


Om meddelandet "*Your Passport is secure*" visas bekräftar det att din Hardware Wallet är äkta. Du kan nu använda den för att säkra en Bitcoin Wallet.


![Image](assets/fr/61.webp)


Bekräfta testresultatet i ditt pass.


![Image](assets/fr/14.webp)


## Ställa in PIN-koden


Därefter kommer steget med PIN-koden. PIN-koden låser upp ditt pass. Den ger därför skydd mot obehörig fysisk åtkomst. PIN-koden är inte inblandad i härledningen av din Wallet:s kryptografiska nycklar. Så även om du inte har tillgång till PIN-koden kan du få tillgång till dina bitcoins om du har din Mnemonic-fras på 12 eller 24 ord.


![Image](assets/fr/15.webp)


Vi rekommenderar att du väljer en PIN-kod som är så slumpmässig som möjligt. Var också noga med att spara denna kod på en annan plats än där ditt pass förvaras (t.ex. i en lösenordshanterare).


Du kan välja en PIN-kod på mellan 6 och 12 siffror. Jag råder dig att göra den så lång som möjligt.


Ange din PIN-kod med hjälp av knappsatsen. När du är klar klickar du på bekräftelseknappen.


![Image](assets/fr/16.webp)


Bekräfta din PIN-kod en gång till.


![Image](assets/fr/17.webp)


Din PIN-kod har registrerats.


![Image](assets/fr/18.webp)


## Uppdatera firmware för Passport


Din Hardware Wallet föreslår att du uppdaterar dess firmware. Jag rekommenderar att du uppdaterar omedelbart för att dra nytta av de förbättringar och korrigeringar som de senaste versionerna medför. För att fortsätta, klicka på bekräftelseknappen till höger.


![Image](assets/fr/19.webp)


Din Passport är redo att ta emot den nya firmware via ett MicroSD-kort.


![Image](assets/fr/20.webp)


### Utan Envoy-applikation


För att göra detta använder du MicroSD-kortet som medföljde i Passport-boxen (eller ett annat) och sätter in det i din dator. Ladda ner den senaste firmwareversionen från [stiftelsens dokumentationswebbplats](https://docs.foundation.xyz/firmware-updates/passport/) eller [deras GitHub-arkiv](https://github.com/Foundation-Devices/passport2/releases).


![Image](assets/fr/21.webp)


Innan du installerar den på din enhet rekommenderar vi starkt att du kontrollerar äktheten och integriteten hos den nedladdade firmware. Om du behöver hjälp med detta, se denna handledning :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### Med Envoy-applikationen


Det andra, enklare alternativet är att använda Envoy-programmet direkt. Klicka på "*Download Firmware*".


![Image](assets/fr/62.webp)


Använd den adapter som medföljer ditt Passport för att ansluta MicroSD-kortet till din telefon.


![Image](assets/fr/63.webp)


Välj MicroSD-kortet i din filutforskare för att spara den fasta programvaran.


![Image](assets/fr/64.webp)


Den inbyggda programvaran är nu sparad. Ta ut MicroSD-kortet från din smartphone och sätt in det i Passport.


![Image](assets/fr/65.webp)


Filutforskaren för Passport öppnas. Välj filen `vN.N.N-passport.bin`.


![Image](assets/fr/22.webp)


Klicka på "*Välj*".


![Image](assets/fr/23.webp)


Bekräfta sedan installationen av firmware.


![Image](assets/fr/24.webp)


Vänta tills uppdateringen är klar.


![Image](assets/fr/25.webp)


När uppdateringen är klar anger du din PIN-kod för att låsa upp enheten och fortsätta konfigurationen.


![Image](assets/fr/26.webp)


## Skapa en ny Bitcoin Wallet


Nu är det dags att skapa en ny Bitcoin Wallet. Klicka på bekräftelseknappen.


![Image](assets/fr/27.webp)


För att skapa en ny Wallet, klicka på "*Create New seed*".


![Image](assets/fr/28.webp)


Du kan välja mellan en Mnemonic-fras på 12 eller 24 ord. De båda alternativen ger samma säkerhet, så du kan välja det som är enklast att spara, dvs. 12 ord.


![Image](assets/fr/29.webp)


Klicka på "*Fortsätt*".


![Image](assets/fr/30.webp)


Ditt pass kommer nu att generate din "*Backup Code*". Detta är en serie siffror som kan användas för att dekryptera en säkerhetskopia av din Wallet som finns lagrad på ett MicroSD-minne. Detta säkerhetskopieringssystem, som är specifikt för Foundation-enheter, utgör en ytterligare säkerhetskopia till din Mnemonic-fras, men är inte kompatibel med annan Bitcoin-programvara.


Om du bestämmer dig för att använda denna "*Backup Code*", se till att förvara den på en annan plats än ditt MicroSD-minne som innehåller den krypterade säkerhetskopian av din Wallet. Du kan dock välja att inte använda det här systemet om du anser att en bra säkerhetskopia av din Mnemonic-fras är tillräcklig.


![Image](assets/fr/31.webp)


Ange din "*Backup Code*" för att bekräfta att du har sparat den korrekt.


![Image](assets/fr/32.webp)


Om ett MicroSD-kort har satts i har den krypterade säkerhetskopian av din Wallet sparats där.


![Image](assets/fr/33.webp)


Ditt pass kommer att visa din Mnemonic-fras på 12 ord. Denna Mnemonic ger dig full, obegränsad tillgång till alla dina bitcoins. Vem som helst som har tillgång till denna fras kan stjäla dina pengar, även utan fysisk tillgång till ditt pass.


Frasen på 12 ord återställer tillgången till dina bitcoins i händelse av förlust, stöld eller brott på ditt pass. Det är därför mycket viktigt att spara det noggrant och förvara det på en säker plats.


Du kan skriva den på kartongen som medföljer i lådan, eller för extra säkerhet rekommenderar jag att du graverar den på en bas av rostfritt stål för att skydda den mot brand, översvämning eller kollaps.


Klicka på bekräftelseknappen för att se din Mnemonic-fras.


![Image](assets/fr/34.webp)


För mer information om det rätta sättet att spara och hantera din Mnemonic-fras rekommenderar jag starkt att du följer den här andra handledningen, särskilt om du är nybörjare:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

naturligtvis får du aldrig dela dessa ord på Internet, som jag gör i den här handledningen. Detta prov Wallet kommer endast att användas på Testnet och kommer att raderas i slutet av handledningen.**_


Gör en fysisk säkerhetskopia av denna mening.


![Image](assets/fr/35.webp)


Ditt pass har konfigurerats på ett framgångsrikt sätt. Klicka på bekräftelseknappen för att fortsätta.


![Image](assets/fr/36.webp)


## Konfigurera Wallet på Envoy


I den här guiden visar jag hur du använder Passport med Envoy-applikationen. Denna Hardware Wallet är dock också kompatibel med Sparrow Wallet, Keeper, BlueWallet, Nunchuk, Specter och många andra...


![Image](assets/fr/66.webp)


Använd Envoy-applikationen för att skanna QR-koden som visas på ditt pass.


![Image](assets/fr/67.webp)


Dina publika nycklar är nu importerade till applikationen. Klicka på "*Validera mottagande av Address*".


![Image](assets/fr/68.webp)


Använd ditt pass för att skanna Address som visas på Envoy.


![Image](assets/fr/69.webp)


Ditt pass kommer att bekräfta om den Wallet som importeras med Envoy är giltig. Bekräfta det i ansökan.


![Image](assets/fr/70.webp)


Du kan nu komma åt din Wallet:s offentliga information på Envoy, men för att spendera bitcoins måste du använda ditt pass.


![Image](assets/fr/71.webp)


## Upptäck Passport-menyerna


Din Passport Interface har tre huvudmenyer:




- "*Account*";
- "*Mer*";
- "*Inställningar*".


För att navigera mellan dessa menyer använder du vänster- och högerpilarna på styrplattan.


### *Meny "Konto*


I menyn "*Account*" hittar du de viktigaste funktionerna i din Bitcoin Wallet. Du kan signera en transaktion antingen via kameran eller via MicroSD-porten.


![Image](assets/fr/37.webp)


Undermenyn "*Account Tools*" erbjuder alternativ som att verifiera en Address, signera ett meddelande eller konsultera adresserna i din Wallet.


![Image](assets/fr/38.webp)


I undermenyn "*Manage Account*" kan du ansluta din Bitcoin Wallet till en Wallet-hanteringsprogramvara (som vi kommer att gå igenom i nästa steg i denna handledning), eller visa och byta namn på ditt konto.


![Image](assets/fr/39.webp)


### Meny "Mer


I menyn "*More*" kan du skapa ett nytt konto i din Wallet, kopplat till samma Mnemonic-fras.


![Image](assets/fr/40.webp)


Du kan också ange en BIP39 passphrase eller använda en tillfällig seed.


![Image](assets/fr/41.webp)


### Meny "Inställningar


I menyn "*Settings*" hittar du alla dina Wallet- och enhetsinställningar.


![Image](assets/fr/42.webp)


Undermenyn "*Device*" ger dig möjlighet att anpassa ljusstyrkan på skärmen, ställa in fördröjningen innan automatisk låsning, ändra PIN-koden eller byta namn på enheten.


![Image](assets/fr/43.webp)


Med undermenyn "*Backup*" kan du exportera din krypterade Wallet-säkerhetskopia, kontrollera giltigheten för en befintlig säkerhetskopia eller leta upp din "*Backup Code*" igen.


![Image](assets/fr/44.webp)


Undermenyn "*Firmware*" är avsedd för uppdatering av den fasta programvaran i din Passport. Vi rekommenderar att du utför dessa uppdateringar regelbundet för att dra nytta av de senaste korrigeringarna och funktionerna.


![Image](assets/fr/45.webp)


I undermenyn "*Bitcoin*" kan du ändra den enhet som visas (BTC eller satoshis), hantera en eventuell Multisig Wallet eller växla till läget "*Testnet*".


![Image](assets/fr/46.webp)


I "*Advanced*" kan du se orden i din Mnemonic-fras, utföra åtgärder på den isatta MicroSD-enheten, återställa ditt Passport till fabriksinställningarna eller utföra en äkthetskontroll, som tidigare.


![Image](assets/fr/47.webp)


Du kan aktivera "*Security Words*", en funktion som ger en Layer av säkerhet genom att visa två specifika ord när du låser upp enheten efter att ha angett de fyra första siffrorna i PIN-koden. Dessa ord, som kan sparas under konfigurationen, säkerställer att Passport inte har bytts ut eller manipulerats. Om det vid ett senare tillfälle skulle uppstå en avvikelse, rekommenderar vi att du inte använder enheten. Jag råder dig att aktivera det här alternativet för att förhindra de flesta risker för fysisk kompromettering av enheten.


![Image](assets/fr/48.webp)


Slutligen kan du i undermenyn "*Extensions*" aktivera funktioner som är specifika för vissa användningsområden för apparaten, t.ex. Whirlpool CoinJoin-protokollet.


![Image](assets/fr/49.webp)


## Ta emot bitcoins


Nu när ditt Passport är konfigurerat är du redo att ta emot din första Sats på din nya Bitcoin Wallet. För att göra detta klickar du på ditt "*Primary 0*"-konto på Envoy.


![Image](assets/fr/72.webp)


Klicka på knappen "*Receive*".


![Image](assets/fr/73.webp)


Ditt Envoy-program visar den första tillgängliga tomma Address på din Wallet. Innan vi använder den, låt oss kontrollera Address på Passport-skärmen för att se till att den verkligen tillhör vår Bitcoin Wallet. I menyn "*Account*" i ditt Passport väljer du "*Account Tools*".


![Image](assets/fr/74.webp)


Klicka på "*Verify Address*" och skanna sedan QR-koden som visas på Envoy.


![Image](assets/fr/75.webp)


Kontrollera att den Address som visas på passet exakt motsvarar den som visas på Sparrow, och att "*Verified*" visas.


![Image](assets/fr/76.webp)


Du kan nu använda den för att ta emot bitcoins. När transaktionen sänds i nätverket kommer den att visas på Envoy. Vänta tills du har fått tillräckligt många bekräftelser för att betrakta transaktionen som slutgiltig.


![Image](assets/fr/77.webp)


## Skicka bitcoins


Nu när du har några Sats i din Wallet kan du också skicka några. För att göra det, klicka på knappen "*Sänd*".


![Image](assets/fr/78.webp)


Ange mottagarens Address, antingen genom att klistra in den direkt eller genom att skanna QR-koden med kameran i din smartphone.


![Image](assets/fr/79.webp)


Bestäm det belopp du vill skicka och klicka sedan på "*Bekräfta*".


![Image](assets/fr/80.webp)


Välj transaktionsavgiften enligt den aktuella marknadssituationen och kontrollera sedan transaktionsinformationen. Om allt är korrekt klickar du på "*Signera med pass*".


![Image](assets/fr/81.webp)


Lägg till en etikett till din transaktion för att hålla en tydlig förteckning över dess syfte.


![Image](assets/fr/82.webp)


Envoy visar sedan en PSBT (*Partially Signed Bitcoin Transaction*). Programmet har byggt upp transaktionen, men saknar fortfarande signatur(er) för att låsa upp de bitcoins som används i inmatningen. Dessa signaturer kan endast utföras av Passport, som är värd för din seed och ger tillgång till de privata nycklar som behövs för att signera transaktionen.


![Image](assets/fr/83.webp)


Gå till menyn "*Account*" i ditt pass och klicka på "*Signera med QR-kod*".


![Image](assets/fr/84.webp)


Skanna PSBT (*Partially Signed Bitcoin Transaction*) som visas på Envoy.


![Image](assets/fr/85.webp)


Bekräfta att den mottagande Address och det skickade beloppet är korrekta och tryck sedan på bekräftelseknappen.


![Image](assets/fr/86.webp)


Kontrollera Exchange Address. I mitt exempel finns det ingen, eftersom transaktionen innehåller en enda utgång.


![Image](assets/fr/87.webp)


Kontrollera att avgiften är den som du har valt.


![Image](assets/fr/88.webp)


Om all information är korrekt klickar du på bekräftelseknappen för att signera transaktionen.


![Image](assets/fr/89.webp)


I ditt pass ser du din signerade transaktion i form av en QR-kod.


![Image](assets/fr/90.webp)


I Envoy-applikationen klickar du på QR-kodikonen och skannar sedan PSBT som visas på din passskärm.


![Image](assets/fr/91.webp)


Kontrollera dina transaktionsuppgifter en sista gång. Om allt är korrekt trycker du på "*Send Transaction*" för att sända den i Bitcoin-nätverket.


![Image](assets/fr/92.webp)


Din transaktion väntar nu på bekräftelse. Du kan följa dess status direkt från ditt konto.


![Image](assets/fr/93.webp)


Grattis, du vet nu hur du konfigurerar och använder Passport med Envoy-applikationen. Om du tyckte att denna handledning var användbar skulle jag vara tacksam om du lämnade en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack för att du delar med dig!


För ytterligare information, se vår handledning om Liana-programvaran:


https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04