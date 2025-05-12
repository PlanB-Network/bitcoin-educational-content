---
name: Passport Core
description: Konfigurera och använda Passport Hardware Wallet i manuellt läge
---
![cover](assets/cover.webp)


Passport är en Hardware Wallet med endast Bitcoin, designad av Foundation Devices, ett amerikanskt företag som grundades i april 2020 i Boston.


Passport "*Batch 2*" som presenteras i denna handledning är efterföljaren till "*Founder's Edition*". Den sticker ut med sin premiumdesign, högupplösta färgskärm och ergonomiska fysiska tangentbord. Den fungerar i "*Air-Gap*"-läge, vilket säkerställer att din Wallet:s privata nycklar förblir helt isolerade, med kommunikation möjlig via ett MicroSD-kort eller QR-koder. Enheten är utrustad med ett löstagbart, uppladdningsbart Nokia BL-5C-batteri med en kapacitet på 1200 mAh. Detta icke-proprietära batteri kan enkelt bytas ut, eftersom BL-5C-modellen är allmänt tillgänglig i butikerna.

💡 **Uppdatering:** Sedan mars 2025 heter denna hårdvaruplånbok inte längre "Passport" eller "Passport V2", utan "Passport Core".

När det gäller anslutningsmöjligheter är Passport utrustad med en MicroSD-port, en USB-C-port för laddning och en bakre kamera för att skanna QR-koder.


När det gäller säkerhet har Passport ett säkert element och enhetens källkod är helt öppen. Den erbjuder alla de funktioner som förväntas av en bra Bitcoin Hardware Wallet. Observera att Passport ännu inte stöder miniscript, men denna funktion är planerad till andra kvartalet 2025.


Med ett pris på 199 USD är Passport positionerad som en avancerad Hardware Wallet, som konkurrerar med Coldcard Q, Jade Plus, Tezor Safe 5 och Ledger:s toppmodeller.


![Image](assets/fr/01.webp)


För att hantera din säkra Wallet på ett Passport har du flera alternativ. Denna Hardware Wallet är kompatibel med de flesta Wallet-hanteringsprogram på marknaden, inklusive Sparrow Wallet, Spectre Desktop, Nunchuk, Keeper, bland andra. I denna handledning lär vi oss hur man använder den med Sparrow Wallet.


Om du är nybörjare är det enklaste alternativet att använda ditt Passport med den inbyggda Envoy-applikationen, utvecklad av Foundation. För att ta reda på hur du använder Envoy med ditt pass, kolla in den här andra handledningen :


https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb

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


## Starta pass


Tryck på på/av-knappen på sidan av enheten för att starta den.


![Image](assets/fr/04.webp)


Tryck på bekräftelseknappen för att komma till nästa meny.


![Image](assets/fr/05.webp)


I den här handledningen använder vi Sparrow Wallet för att hantera den passsäkrade Wallet. Välj "*Manual Setup*".


![Image](assets/fr/06.webp)


Acceptera sedan användarvillkoren.


![Image](assets/fr/07.webp)


Nästa steg är att kontrollera din enhet. Detta bekräftar att ditt pass är äkta och säkerställer att det inte har manipulerats under transporten. Du kommer att bli ombedd att skanna en QR-kod.


![Image](assets/fr/08.webp)


Gå till [den officiella verifieringssidan] (https://validate.foundationdevices.com/) och välj "*Passport*".


![Image](assets/fr/09.webp)


Använd kameran i ditt pass för att skanna QR-koden som visas på webbplatsen.


![Image](assets/fr/10.webp)


Din enhet kommer då att visa 4 ord.


![Image](assets/fr/11.webp)


Ange dessa ord på webbplatsen för att bekräfta att ditt pass är äkta och klicka på "*Validate*".


![Image](assets/fr/12.webp)


Om meddelandet "*Passed*" visas är din Hardware Wallet äkta. Du kan nu använda den för att säkra en Bitcoin Wallet.


![Image](assets/fr/13.webp)


Bekräfta testresultatet i ditt pass.


![Image](assets/fr/14.webp)


## Ställa in PIN-koden


Därefter kommer steget med PIN-koden. PIN-koden låser upp ditt pass. Den ger därför skydd mot obehörig fysisk åtkomst. PIN-koden är inte inblandad i härledningen av din Wallet:s kryptografiska nycklar. Så även utan tillgång till PIN-koden kan du genom att inneha din Mnemonic-fras på 12 eller 24 ord återfå tillgång till dina bitcoins.


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


För att göra detta använder du MicroSD-kortet som medföljde i Passport-boxen (eller ett annat) och sätter in det i din dator. Ladda ner den senaste firmwareversionen från [stiftelsens dokumentationswebbplats](https://docs.foundation.xyz/firmware-updates/passport/) eller [deras GitHub-arkiv](https://github.com/Foundation-Devices/passport2/releases).


![Image](assets/fr/21.webp)


Innan du installerar den på din enhet rekommenderar vi starkt att du kontrollerar äktheten och integriteten hos den nedladdade firmware. Om du behöver hjälp med detta, se denna handledning :


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Efter att ha kontrollerat `.bin`-filen, placera den på din MicroSD och sätt sedan in den i Passport. Filutforskaren i Passport öppnas. Välj filen `vN.N.N-passport.bin`.


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


Om du bestämmer dig för att använda denna "*Backup Code*", se till att förvara den på en annan plats än ditt MicroSD-minne som innehåller den krypterade säkerhetskopian av din Wallet. Du kan dock välja att inte använda detta system om du anser att en bra säkerhetskopia av din Mnemonic-fras är tillräcklig.


![Image](assets/fr/31.webp)


Ange din "*Backup Code*" för att bekräfta att du har sparat den korrekt.


![Image](assets/fr/32.webp)


Om ett MicroSD-kort har satts i har den krypterade säkerhetskopian av din Wallet sparats där.


![Image](assets/fr/33.webp)


Ditt pass kommer att visa din Mnemonic-fras med 12 ord. Denna Mnemonic ger dig full, obegränsad tillgång till alla dina bitcoins. Vem som helst som har tillgång till denna fras kan stjäla dina pengar, även utan fysisk tillgång till ditt pass.


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


## Upptäckt av meny


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


Du kan också ange en BIP39 passphrase (se nästa avsnitt) eller använda en tillfällig seed.


![Image](assets/fr/41.webp)


### Meny "Inställningar


I menyn "*Settings*" hittar du alla dina Wallet- och enhetsinställningar.


![Image](assets/fr/42.webp)


Undermenyn "*Device*" ger dig möjlighet att anpassa ljusstyrkan på skärmen, ställa in fördröjningen innan automatisk låsning, ändra PIN-koden eller byta namn på enheten.


![Image](assets/fr/43.webp)


I undermenyn "*Backup*" kan du exportera din krypterade Wallet-säkerhetskopia, kontrollera giltigheten för en befintlig säkerhetskopia eller leta upp din "*Backup Code*" igen.


![Image](assets/fr/44.webp)


Undermenyn "*Firmware*" är avsedd för uppdatering av den fasta programvaran i din Passport. Vi rekommenderar att du utför dessa uppdateringar regelbundet för att dra nytta av de senaste korrigeringarna och funktionerna.


![Image](assets/fr/45.webp)


I undermenyn "*Bitcoin*" kan du ändra den enhet som visas (BTC eller satoshis), hantera en eventuell Multisig Wallet eller växla till läget "*Testnet*".


![Image](assets/fr/46.webp)


I "*Avancerat*" kan du se orden i din Mnemonic-fras, utföra åtgärder på det isatta MicroSD-kortet, återställa ditt Passport till fabriksinställningarna eller utföra en äkthetskontroll, som tidigare.


![Image](assets/fr/47.webp)


Du kan aktivera "*Security Words*", en funktion som ger en Layer av säkerhet genom att visa två specifika ord när du låser upp enheten efter att ha angett de fyra första siffrorna i PIN-koden. Dessa ord, som sparas under konfigurationen, säkerställer att Passport inte har bytts ut eller manipulerats. Om det vid ett senare tillfälle skulle uppstå en avvikelse, rekommenderar vi att du inte använder enheten. Jag råder dig att aktivera det här alternativet för att förhindra de flesta risker för fysisk kompromettering av enheten.


![Image](assets/fr/48.webp)


Slutligen kan du i undermenyn "*Extensions*" aktivera funktioner som är specifika för vissa användningsområden för apparaten, t.ex. Whirlpool CoinJoin-protokollet.


![Image](assets/fr/49.webp)


## Lägg till en BIP39 passphrase


Innan du fortsätter kan du, om du vill, lägga till en BIP39 passphrase. En BIP39 passphrase är ett valfritt lösenord som du kan välja fritt, och som läggs till din Mnemonic-fras för att förstärka Wallet-säkerheten. När den här funktionen är aktiverad krävs både Mnemonic och passphrase för att få tillgång till din Bitcoin Wallet. Utan någon av dem skulle det vara omöjligt att återställa Wallet.


Innan du konfigurerar det här alternativet på ditt Passport rekommenderas det starkt att du läser den här artikeln för att fullt ut förstå den teoretiska driften av passphrase och undvika fel som kan leda till förlust av dina bitcoins:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

För att aktivera den, gå till menyn "*More*" och klicka på "*Enter passphrase*".


![Image](assets/fr/50.webp)


Ange din passphrase med hjälp av aA1-knappsatsen och se till att du sparar den en eller flera gånger på fysiska medier (papper eller metall). I exemplet använder jag en mycket svag passphrase, men du bör välja en stark, slumpmässig passphrase, som innehåller alla typer av tecken och är tillräckligt lång (som ett starkt lösenord).


![Image](assets/fr/51.webp)


Observera att BIP39-passfraser är skiftläges- och skrivfelskänsliga. Om du anger en passphrase som är något annorlunda än den som ursprungligen konfigurerades, kommer Passport inte att rapportera ett fel, utan kommer att härleda en annan uppsättning kryptografiska nycklar som inte kommer att vara de i din ursprungliga Wallet.


Det är därför viktigt att du, när du konfigurerar, någonstans antecknar det huvudnyckelfingeravtryck som du kommer att få i nästa steg. Till exempel, med mitt passphrase `Plan B-nätverk`, är mitt huvudnyckelfingeravtryck `745D526B`.


![Image](assets/fr/52.webp)


Varje gång du låser upp ditt Passport måste du återvända till den här menyn för att ange din passphrase och använda den på din Wallet. Passport sparar inte passphrase.


Varje gång du låser upp, efter att ha skrivit ner passphrase, kontrollerar du på denna bekräftelseskärm att det fingeravtryck som ges är detsamma som det du skrev ner under konfigurationen. Om så är fallet är din passphrase korrekt och du har tillgång till rätt Bitcoin Wallet. Om det inte är det, är du på fel Wallet och måste försöka igen och se till att inte göra några inmatningsfel.


Innan du får dina första bitcoins på din Wallet, ** rekommenderar jag starkt att du utför ett tomt återställningstest**. Anteckna viss referensinformation, till exempel din xpub eller första mottagande Address, och radera sedan din Wallet på passet medan den fortfarande är tom (`Inställningar -> Avancerat -> Radera pass`). Försök sedan återställa din Wallet med hjälp av dina pappersbackuper av Mnemonic-frasen och alla passphrase. Kontrollera att cookie-informationen som genereras efter återställningen matchar den som du ursprungligen skrev ner. Om den gör det kan du vara säker på att dina pappersbackuper är tillförlitliga. Om du vill veta mer om hur du utför en teståterställning kan du läsa den här andra handledningen :


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

![Image](assets/fr/53.webp)


## Konfigurera Wallet på Sparrow Wallet


I den här handledningen visar jag dig en avancerad användning av Passport med Sparrow Wallet. Denna Hardware Wallet är dock också kompatibel med Envoy (Foundation-applikationen), Keeper, BlueWallet, Nunchuk, Specter och många andra...


Börja med att ladda ner och installera Sparrow Wallet [från den officiella webbplatsen] (https://sparrowwallet.com/) på din dator, om du inte redan har gjort det.


![Image](assets/fr/54.webp)


Se till att kontrollera programvarans äkthet och integritet före installationen. Om du inte vet hur du gör det kan du läsa den här handledningen:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

När Sparrow Wallet är öppen klickar du på fliken "*File*" och sedan på "*New Wallet*".


![Image](assets/fr/55.webp)


Ge din Wallet ett namn och klicka sedan på "*Create Wallet*".


![Image](assets/fr/56.webp)


Välj "*Airgapped Hardware Wallet*".


![Image](assets/fr/57.webp)


Klicka på "*Scan...*" bredvid alternativet "*Passport*". Detta kommer att öppna din webbkamera.


![Image](assets/fr/58.webp)


På din Hardware Wallet går du till menyn "*Account*", väljer undermenyn "*Manage Account*" och klickar på "*Connect Wallet*".


![Image](assets/fr/59.webp)


I rullgardinsmenyn som visas väljer du "*Sparrow*".


![Image](assets/fr/60.webp)


Välj sedan "*Single-sig*" för en normal konfiguration utan Multisig.


![Image](assets/fr/61.webp)


Välj alternativet "*QR Code*".


![Image](assets/fr/62.webp)


Ditt pass kommer sedan att generate dynamiska QR-koder. Använd datorns webbkamera för att skanna in dem i Sparrow-programvaran.


![Image](assets/fr/63.webp)


Du bör nu se din xpub och ditt fingeravtryck för huvudnyckeln, som bör matcha det som visas på ditt pass när du anger din passphrase. Klicka på knappen "*Apply*".


![Image](assets/fr/64.webp)


Ange ett starkt lösenord för att säkra åtkomsten till din Sparrow Wallet. Detta lösenord skyddar dina publika nycklar, adresser, etiketter och transaktionshistorik från obehörig åtkomst. Det är en bra idé att spara lösenordet i en lösenordshanterare så att du inte glömmer det.


![Image](assets/fr/65.webp)


Your Passport uppmanar dig sedan att skanna den första mottagningen Address för att bekräfta att importen har lyckats.


![Image](assets/fr/66.webp)


I Sparrow går du till fliken "*Receive*" och skannar QR-koden för den första Address.


![Image](assets/fr/67.webp)


Om operationen lyckas kommer ditt pass att visa "*Verified*".


![Image](assets/fr/68.webp)


Detta bekräftar att importen var lyckad.


![Image](assets/fr/69.webp)


## Ta emot bitcoins


Nu när ditt Passport är konfigurerat är du redo att ta emot din första Sats på din nya Bitcoin Wallet. För att göra detta klickar du på Sparrow på menyn "*Receive*".


![Image](assets/fr/70.webp)


Sparrow kommer att visa det första tomma kvittot Address i din Wallet. Du kan lägga till en etikett.


![Image](assets/fr/71.webp)


Innan vi använder den ska vi kontrollera Address på Passport-skärmen för att se till att den tillhör vår Bitcoin Wallet. På Sparrow kan du förstora QR-koden för Address genom att klicka på den om det behövs. I menyn "*Account*" i ditt Passport väljer du "*Account Tools*".


![Image](assets/fr/72.webp)


Klicka på "*Verify Address*" och skanna sedan QR-koden som visas på Sparrow Wallet.


![Image](assets/fr/73.webp)


Kontrollera att den Address som visas på passet exakt motsvarar den som visas på Sparrow, och att "*Verified*" visas.


![Image](assets/fr/74.webp)


Du kan nu använda den för att ta emot bitcoins. När transaktionen sänds i nätverket kommer den att visas på Sparrow. Vänta tills du har fått tillräckligt många bekräftelser för att betrakta transaktionen som slutgiltig.


![Image](assets/fr/75.webp)


## Skicka bitcoins


Nu när du har några Sats i din Wallet kan du också skicka några. För att göra det, klicka på menyn "*UTXOs*".


![Image](assets/fr/76.webp)


Välj de UTXO:er som du vill använda som inmatningar för den här transaktionen och klicka sedan på "*Send Selected*".


![Image](assets/fr/77.webp)


Ange mottagarens Address, en etikett som påminner dig om syftet med transaktionen och det belopp som du vill skicka till denna Address.


![Image](assets/fr/78.webp)


Justera avgiftssatsen enligt rådande marknadsförhållanden och klicka sedan på "*Create Transaction*".


![Image](assets/fr/79.webp)


Kontrollera att alla transaktionsparametrar är korrekta och klicka sedan på "*Finalize Transaction for Signing*".


![Image](assets/fr/80.webp)


Klicka på "*Show QR*" för att visa PSBT (*Partially Signed Bitcoin Transaction*). Sparrow har byggt transaktionen, men den saknar fortfarande signaturerna för att låsa upp bitcoins som används i inmatningen. Dessa signaturer kan endast utföras av Passport, som är värd för din seed som ger tillgång till de privata nycklar som behövs för att signera transaktionen.


![Image](assets/fr/81.webp)


Gå till menyn "*Account*" i ditt pass och klicka på "*Signera med QR-kod*".


![Image](assets/fr/82.webp)


Skanna PSBT (*Partially Signed Bitcoin Transaction*) som visas på Sparrow Wallet.


![Image](assets/fr/83.webp)


Kontrollera att den mottagande Address och det skickade beloppet är korrekta och tryck sedan på bekräftelseknappen.


![Image](assets/fr/84.webp)


Kontrollera Exchange Address. I mitt exempel finns det ingen, eftersom transaktionen innehåller en enda utgång.


![Image](assets/fr/85.webp)


Kontrollera att avgiften är den som du har valt.


![Image](assets/fr/86.webp)


Om all information är korrekt klickar du på bekräftelseknappen för att signera transaktionen.


![Image](assets/fr/87.webp)


På Sparrow Wallet klickar du på "*Scan QR*" och skannar QR-koden som visas på ditt pass.


![Image](assets/fr/88.webp)


Din signerade transaktion är nu redo att sändas ut i Bitcoin-nätverket och inkluderas i ett block av en Miner. Om allt är korrekt klickar du på "*Broadcast Transaction*".


![Image](assets/fr/89.webp)


Din transaktion har sänts och väntar på bekräftelse.


![Image](assets/fr/90.webp)


Gratulerar, du vet nu hur du konfigurerar och använder Passport. Om du tyckte att denna handledning var användbar skulle jag vara tacksam om du lämnade en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack för att du delar med dig!


För ytterligare information, se vår handledning om Liana-programvaran:


https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
