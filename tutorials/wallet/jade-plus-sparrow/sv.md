---
name: Jade Plus - Sparrow
description: Avancerad konfiguration av Jade Plus med Sparrow wallet
---
![cover](assets/cover.webp)


Jade Plus är en Hardware Wallet för endast Bitcoin som designats av Blockstream. Det är efterföljaren till den klassiska Jade, med mjukvaruförbättringar, fler alternativ och omdesignad ergonomi för mer intuitiv användning. Den här nya versionen har en magnifik 1,9-tums LCD-skärm med ett bredare färgomfång än föregångaren. Knappar och menynavigering har också optimerats.


Jade Plus kan användas på flera olika sätt: via en kabelanslutning via USB-C, i "*Air-Gap*"-läge med ett micro SD-kort (adapter krävs), via Bluetooth eller till och med genom att utbyta QR-koder tack vare den integrerade kameran. Denna Hardware Wallet är batteridriven.


Den finns tillgänglig från 149,99 USD i den svarta grundversionen, och priset kan stiga med upp till 20 USD för versionerna "*Genesis Grey*" eller "*Lunar Silver*". Jade Plus är därför ett intressant val, med avancerade funktioner som kan jämföras med avancerade hårdvaruplånböcker som Coldcard Q eller Passport V2, men till ett ganska lågt pris, nära mellanklassmodeller.


![JADE-PLUS-SPARROW](assets/fr/01.webp)


Jade Plus är kompatibelt med de flesta programvaror för Wallet-hantering. Här är en sammanfattning av kompatibiliteten i skrivande stund (januari 2025):


| Management Software  | Desktop | Mobile | USB | Bluetooth   | QR  | JadeLink |
| -------------------- | ------- | ------ | --- | ----------- | --- | -------- |
| Blockstream Green    | 🟢      | 🟢     | 🟢  | 🟢 (Mobile) | 🟢  | 🔴       |
| Liana                | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Sparrow              | 🟢      | 🔴     | 🟢  | 🔴          | 🟢  | 🟢       |
| Nunchuk              | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Specter              | 🟢      | 🔴     | 🔴  | 🔴          | 🟢  | 🟢       |
| BlueWallet           | 🟢      | 🟢     | 🔴  | 🔴          | 🟢  | 🟢       |
| Electrum             | 🟢      | 🔴     | 🟢  | 🔴          | 🔴  | 🔴       |
| Keeper               | 🔴      | 🟢     | 🔴  | 🔴          | 🟢  | 🔴       |

I den här handledningen ställer vi in en avancerad konfiguration av Jade Plus med den stationära Sparrow wallet-programvaran i QR-kodläge. Den här konfigurationen är idealisk för användare på mellannivå eller erfarna användare. Om du letar efter ett enklare tillvägagångssätt för nybörjare rekommenderar jag att du tar en titt på den här handledningen där vi använder Jade Plus med Green Wallet via en Bluetooth-anslutning:


https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0

## Säkerhetsmodellen Jade Plus


Jade Plus använder en säkerhetsmodell som bygger på ett "virtuellt säkert element", materialiserat av ett "blint orakel". I konkreta termer kombinerar denna mekanism den PIN-kod som användaren valt, en hemlighet som finns på Jade och en hemlighet som finns hos oraklet (en server som drivs av Blockstream) för att skapa en AES-256-nyckel som distribueras över två enheter. Under initieringen säkrar en ECDH Exchange kommunikationen med oraklet och krypterar återställningsfrasen på Hardware Wallet. I praktiken, när du vill komma åt seed för att signera transaktioner, behöver du tillgång till :




- Själva Jade Plus-enheten;
- PIN-kod för att låsa upp enheten ;
- Och till oraklets hemlighet.


Den stora fördelen med detta tillvägagångssätt är att det inte finns någon "single point of failure" på hårdvarunivå, eftersom en angripare som får tillgång till din Jade måste kompromettera både Jade och oraklet för att få ut nycklarna. Den här modellen innebär också att Jade Plus är helt öppen källkod, vilket gör att man undviker de begränsningar som är förknippade med användningen av verkligt fysiskt säkra Elements, som till exempel Ledger.


Nackdelen med detta system är att användningen av Jade Plus är beroende av det orakel som Blockstream upprätthåller. Om detta orakel blir oåtkomligt är det inte längre möjligt att använda Hardware Wallet direkt med PIN-koden. Detta innebär dock inte att dina bitcoins går förlorade, eftersom de fortfarande kan återvinnas med hjälp av din återställningsfras, som du kan ange i Jade Plus i "*stateless*"-läge. För att komma runt det här beroendet kan du också konfigurera och hantera din egen oracle-server.


Ett annat alternativ för att hantera din seed är att helt enkelt inte registrera den på Jade Plus. I det här fallet blir Jade endast en signaturenhet. Under initialiseringen sparar du, förutom den vanliga sparningen av återställningsfrasen som ord, även den som en handgenererad QR-kod. På så sätt kan du, varje gång du använder din Wallet, importera seed med hjälp av din Jades kamera. Detta kan vara ett intressant alternativ för avancerade användare, beroende på din säkerhetsstrategi, men du måste vara noga med att både spara din seed och skydda den, för även som en QR-kod skulle den göra det möjligt för vem som helst att stjäla dina pengar. Vi kommer att titta på det här alternativet i den här handledningen, men det är inte obligatoriskt.


## Uppackning av Jade Plus


När du får din Jade Plus, kontrollera att lådan och Seal är i gott skick för att säkerställa att ditt paket inte har öppnats.


![JADE-PLUS-SPARROW](assets/fr/02.webp)


I lådan hittar du :




- Le Jade Plus;
- USB-C-kabel;
- Kort för att registrera din Mnemonic-fras som ord eller som "*CompactSeedQR*";
- Några instruktioner för användning ;
- En sladd;
- Några klistermärken.


![JADE-PLUS-SPARROW](assets/fr/03.webp)


Enheten har 4 navigeringsknappar:




- Knappen längst ned till höger sätter på Jade;
- Den stora knappen på enhetens framsida används för att välja ett objekt;
- Med de två små knapparna längst upp kan du navigera till vänster och höger;
- Du kan också välja ett objekt genom att samtidigt klicka på de två knapparna längst upp på enheten.


![JADE-PLUS-SPARROW](assets/fr/04.webp)


## Uppsättning av en ny Bitcoin Wallet


Klicka på startknappen.


![JADE-PLUS-SPARROW](assets/fr/05.webp)


Klicka på "*Setup Jade*".


![JADE-PLUS-SPARROW](assets/fr/06.webp)


Välj "Advanced Setup*".


![Image](assets/fr/07.webp)


Klicka sedan på "*Create a New Wallet*" för att generate en ny seed. Du kan välja mellan en Mnemonic-fras på 12 eller 24 ord. Säkerheten för din Wallet förblir likvärdig med båda alternativen, så det kan vara bekvämare att välja det enklaste alternativet att spara, dvs. 12 ord.


![Image](assets/fr/08.webp)


Klicka på knappen "*Continue*" för att visa din nya återställningsfras.


![Image](assets/fr/09.webp)


Din Jade Plus visar din Mnemonic-fras på 12 ord. **Den här Mnemonic ger dig full, obegränsad tillgång till alla dina bitcoins. Vem som helst som har tillgång till denna fras kan stjäla dina pengar, även utan fysisk tillgång till din Jade Plus. Frasen på 12 ord återställer åtkomsten till dina bitcoins i händelse av förlust, stöld eller brott på din Jade. Det är därför mycket viktigt att spara den noggrant och förvara den på en säker plats.


Du kan skriva den på kartongen som medföljer i lådan, eller för extra säkerhet rekommenderar jag att du graverar den på en bas av rostfritt stål för att skydda den mot brand, översvämning eller kollaps.


![Image](assets/fr/10.webp)


För mer information om det rätta sättet att spara och hantera din Mnemonic-fras rekommenderar jag starkt att du följer den här andra handledningen, särskilt om du är nybörjare:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

naturligtvis får du aldrig dela dessa ord på Internet, som jag gör i den här handledningen. Detta prov Wallet kommer endast att användas på Testnet och kommer att raderas i slutet av handledningen.**_


Klicka på pilen till höger på skärmen för att visa följande ord.


![Image](assets/fr/11.webp)


När du har sparat din fras ber Jade Plus dig att bekräfta den. Välj rätt ord enligt ordningen med hjälp av knapparna längst upp på enheten och klicka på mittknappen för att gå vidare till nästa ord.


![Image](assets/fr/12.webp)


Du har sedan 2 alternativ. Som förklarades i inledningen kan du välja att spara din seed direkt på enheten och använda Blockstreams skyddssystem "*Virtual Secure Element*" för att komma åt din Wallet (Alternativ 1), eller spara din seed som en QR-kod och skanna den varje gång du använder den (Alternativ 2).


För alternativ 1 väljer du "*No*" och för alternativ 2 väljer du "*Yes*".


![Image](assets/fr/13.webp)


### Alternativ 1: QR PIN-upplåsning


Om du har valt alternativ 1 (CompactSeedQR: "*No*") kommer du direkt till valet av anslutningsmetod. I den här handledningen vill vi använda enheten i Air-Gap-läge via QR-kodväxling, så välj "*QR*".


![Image](assets/fr/27.webp)


Klicka på "*Fortsätt*".


![Image](assets/fr/28.webp)


PIN-koden används för att låsa upp din Jade och ger skydd mot obehörig fysisk åtkomst. Denna PIN-kod är inte inblandad i härledningen av din Wallet:s kryptografiska nycklar. Så även om du inte har tillgång till PIN-koden kan du få tillgång till dina bitcoins om du har din Mnemonic-fras med 12 ord. Vi rekommenderar att du väljer en PIN-kod som är så slumpmässig som möjligt. Se också till att du sparar den här koden på en annan plats än där din Jade lagras, t.ex. i en lösenordshanterare.


Välj en 6-siffrig PIN-kod på din Jade genom att använda vänster- och högerknapparna för att bläddra igenom siffrorna och mittknappen för att bekräfta varje siffra.


![Image](assets/fr/29.webp)


Bekräfta din PIN-kod en gång till.


![Image](assets/fr/30.webp)


Som förklarats i inledningen lagras din seed krypterad på Jade Plus. För att dekryptera den måste du tillhandahålla :




- Den giltiga PIN-koden (som vi just har ställt in) ;
- Hemligheten bakom det orakel som Blockstream upprätthåller.


I denna avancerade handledning kommer vi att använda Sparrow wallet för att hantera vår Bitcoin Wallet. Men till skillnad från Blockstreams programvara Green Wallet har Sparrow inte tillgång till oraklet på Blockstreams servrar. Vi kommer därför att använda Blockstreams webbplats för att hämta oraklets hemlighet varje gång vi låser upp Jade Plus.


Besök https://jadefw.blockstream.com/pinqr/index.html


Klicka på "*Starta QR-upplåsning*".


![Image](assets/fr/31.webp)


Klicka på "*Done*", eftersom du redan har valt din PIN-kod på Jade Plus.


![Image](assets/fr/32.webp)


Använd datorns kamera för att skanna de QR-koder som visas på Jade-skärmen.


![Image](assets/fr/33.webp)


Bekräfta på din Jade för att komma till nästa skärm.


![Image](assets/fr/34.webp)


Skanna QR-koden som nu syns på webbplatsen för att hämta oraklets hemlighet.


![Image](assets/fr/35.webp)


Nu när din Wallet har skapats kan du gå vidare till nästa steg och hoppa över underavsnittet "*Alternativ 2: CompactSeedQR*".


![Image](assets/fr/36.webp)


Varje gång du startar klickar du på "*QR Mode*".


![Image](assets/fr/37.webp)


Välj "*QR PIN Unlock*".


![Image](assets/fr/38.webp)


Ange din PIN-kod.


![Image](assets/fr/39.webp)


Gå sedan till [Blockstreams webbplats] (https://jadefw.blockstream.com/pinqr/qrpin.html) för att Exchange QR-koder med oraklet.


![Image](assets/fr/40.webp)


Din Jade är nu upplåst.


![Image](assets/fr/41.webp)


### Alternativ 2: CompactSeedQR


Om du har valt alternativ 2 (CompactSeedQR: "*Yes*") klickar du på "*Yes*" igen.


![Image](assets/fr/14.webp)


Klicka på "*Start*".


![Image](assets/fr/15.webp)


Du kan använda QR-kodbasen som medföljer i Jade Plus-boxen. Välj lämplig ruta beroende på om du har valt en mening på 12 eller 24 ord. Du kan också [skriva ut mallen från Blockstreams webbplats] (https://help.blockstream.com/hc/article_attachments/41928319071769).


Din Jade Plus visar varje zon i din QR-kod.


![Image](assets/fr/16.webp)


Använd en penna för att färglägga rutorna och återge din seed som en QR-kod. Var exakt för att säkerställa att Jade Plus-kameran kan skanna den senare. Använd pilen för att gå vidare till nästa område.


![Image](assets/fr/17.webp)


När du är klar klickar du på "*Done*".


![Image](assets/fr/18.webp)


Skanna din handgjorda QR-kod med Jade Plus för att kontrollera dess giltighet.


![Image](assets/fr/19.webp)


Om din pappersbackup är korrekt klickar du på "*Continue*".


![Image](assets/fr/20.webp)


I den här handledningen använder vi ett anslutningsläge som uteslutande baseras på skanning av QR-koder, så välj "*QR*".


![Image](assets/fr/21.webp)


Du kan också välja att lägga till en PIN-kod utöver din CompactSeedQR-backup, som i alternativ 1. Detta ger dig två sätt att komma åt din Wallet: antingen via PIN-koden och Blockstreams "Virtual Secure Element"-system eller via CompactSeedQR.


Om du väljer alternativet med dubbel PIN-kod väljer du "*PIN*" och följer samma steg som i alternativ 1 för att ställa in PIN-koden.


Om du föredrar att fortsätta med endast CompactSeedQR, välj "*SeedQR*".


![Image](assets/fr/22.webp)


Nu när din Wallet har skapats kan du gå vidare till nästa steg.


![Image](assets/fr/23.webp)


Varje gång du startar upp klickar du på knappen "*QR Mode*" och sedan på "*Scan SeedQR*".


![Image](assets/fr/24.webp)


Använd enhetens kamera för att skanna dina sparade seed som en QR-kod.


![Image](assets/fr/25.webp)


Din Jade är nu upplåst.


![Image](assets/fr/26.webp)


## Lägg till en BIP39 passphrase


En BIP39 passphrase är ett valfritt lösenord som du kan välja fritt och som läggs till din Mnemonic-fras för att förstärka Wallet-säkerheten. När den här funktionen är aktiverad krävs både Mnemonic och passphrase för att få tillgång till din Bitcoin Wallet. Utan något av dem skulle det vara omöjligt att återställa Wallet.


Innan du konfigurerar det här alternativet på din Jade Plus rekommenderas det starkt att du läser den här artikeln för att fullt ut förstå den teoretiska driften av passphrase och undvika fel som kan leda till förlust av dina bitcoins :


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

När Jade fortfarande är låst (passphrase kan endast anges när enheten inte är upplåst), öppnar du menyn "*Options*".


![Image](assets/fr/42.webp)


Välj "*BIP39 passphrase*".


![Image](assets/fr/43.webp)


I alternativet "*Frequency*" kan du välja om Jade Plus ska be dig att ange din passphrase varje gång den startar:




- "*Disabled*" inaktiverar användningen av en passphrase;
- "*Next Login Only*" kräver att du återvänder till den här menyn för att aktivera begäran om din passphrase vid nästa start. Detta alternativ gör att du inte kan avslöja dess användning;
- "*Always Ask*" gör att Jade systematiskt frågar efter din passphrase varje gång den startar, och avslöjar därmed att din Wallet skyddas av en passphrase.


Välj det alternativ som passar bäst för din säkerhetsstrategi. Personligen väljer jag "*Alltid fråga*" i exemplet.


![Image](assets/fr/44.webp)


Du kan sedan välja mellan två metoder för att ange din passphrase:




- "*Manuellt*: Med ett virtuellt tangentbord kan du skriva in bokstäver (versaler och gemener), siffror och symboler, tecken för tecken. Det här är standardmetoden för alla hårdvaruplånböcker;
- "*WordList*": Specifik metod utformad av Blockstream för Jade, som påskyndar inmatning av passphrase och ökar dess entropi. Under inmatningen föreslår systemet ord från BIP39-listan, vilket gör upplåsningen enklare. Denna metod genererar automatiskt en mening genom att sammanfoga de valda orden, separerade med mellanslag (exempel: `abandon ability able`).


Personligen rekommenderar jag dig att använda den första metoden, eftersom det är den standard som du hittar på alla andra Wallet-stöd.


![Image](assets/fr/45.webp)


Du kan sedan återgå till startskärmen och låsa upp din Wallet som vanligt, antingen med din PIN-kod eller med din CompactSeedQR (se ovan). Du kommer då att bli ombedd att ange din passphrase.


![Image](assets/fr/46.webp)


Skriv in det på Jade-tangentbordet och se till att göra en eller flera säkerhetskopior på fysiska medier (papper eller metall). I exemplet använder jag en mycket svag passphrase, men du måste välja en stark, slumpmässig passphrase som innehåller alla typer av tecken och är tillräckligt lång (som ett starkt lösenord).


![Image](assets/fr/47.webp)


Om din passphrase är giltig, bekräfta.


![Image](assets/fr/48.webp)


Observera att BIP39- lösenfraser är skiftläges- och skrivfelskänsliga. Om du anger en passphrase som är något annorlunda än den som ursprungligen konfigurerades, kommer Jade inte att rapportera ett fel utan kommer att härleda en annan uppsättning kryptografiska nycklar som inte kommer att vara de i din ursprungliga Wallet.


När du konfigurerar är det därför viktigt att du noterar fingeravtrycket för din huvudnyckel, som finns i det nedre högra hörnet på skärmen. Till exempel, med min passphrase `PBN`, är mitt huvudnyckelfingeravtryck `3AD1AE65`.


![Image](assets/fr/49.webp)


Varje gång du låser upp din Jade med din passphrase ska du kontrollera att fingeravtrycket är detsamma som det du angav under konfigurationen. Om det är det, är din passphrase korrekt och du har tillgång till rätt Bitcoin Wallet. Om det inte är det, är du på fel Wallet och måste försöka igen och se till att inte göra några inmatningsfel.


Innan du får dina första bitcoins i din Wallet, ** rekommenderar jag starkt att du utför ett tomt återställningstest**. Anteckna viss referensinformation, t.ex. din xpub eller första mottagna Address, radera sedan din Wallet på Jade Plus medan den fortfarande är tom (`Optioner -> Enhet -> Fabriksåterställning`). Försök sedan att återställa din Wallet med hjälp av dina pappersbackuper av Mnemonic-frasen och alla passphrase. Kontrollera att cookie-informationen som genereras efter återställningen matchar den som du ursprungligen skrev ner. Om den gör det kan du vara säker på att dina pappersbackuper är tillförlitliga. Om du vill veta mer om hur du utför en teståterställning kan du titta på den här andra handledningen:


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Konfigurera Wallet på Sparrow wallet


I denna handledning presenterar jag en avancerad användning av Jade Plus med hjälp av Sparrow wallet. Denna Hardware Wallet är dock kompatibel med många andra program, t.ex. Liana, Nunchuk, Spectre, Green och Keeper. Dessa kompatibiliteter varierar när det gäller anslutningar: USB, Bluetooth eller QR-kod (se tabellen i inledningen för detaljer).


Börja med att ladda ner och installera Sparrow wallet [från den officiella webbplatsen] (https://sparrowwallet.com/) på din dator, om du inte redan har gjort det.


![Image](assets/fr/50.webp)


Se till att kontrollera programvarans äkthet och integritet före installationen. Om du inte vet hur du gör det kan du läsa den här handledningen:


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

När Sparrow wallet är öppet klickar du på fliken "*File*" och sedan på "*New Wallet*".


![Image](assets/fr/51.webp)


Ge din Wallet ett namn och klicka sedan på "*Create Wallet*".


![Image](assets/fr/52.webp)


Välj "*Airgapped Hardware Wallet*".


![Image](assets/fr/53.webp)


Klicka på "*Scan...*" bredvid alternativet "*Jade*".


![Image](assets/fr/54.webp)


Lås upp din Jade Plus och, om du använder en sådan, ange din passphrase. Gå sedan till menyn "*Options*", välj "*Wallet*" och klicka på "*Export Xpub*".


![Image](assets/fr/55.webp)


Din Jade kommer att visa din Keystore via flera QR-koder. Skanna dem på din maskin med hjälp av Sparrow.


![Image](assets/fr/56.webp)


Du bör nu se din xpub och ditt fingeravtryck för huvudnyckeln, som bör matcha det som finns på din Jade Plus. Klicka på "*Apply*".


![Image](assets/fr/57.webp)


Ange ett starkt lösenord för att säkra åtkomsten till din Sparrow wallet. Detta lösenord skyddar dina publika nycklar, adresser, etiketter och transaktionshistorik från obehörig åtkomst. Det är en bra idé att spara lösenordet i en lösenordshanterare så att du inte glömmer det.


![Image](assets/fr/58.webp)


Din Wallet är nu korrekt konfigurerad på Sparrow.


![Image](assets/fr/59.webp)


## Ta emot bitcoins


Nu när din Jade Plus är konfigurerad är du redo att ta emot din första Sats på din nya Bitcoin Wallet. För att göra detta klickar du på menyn "*Receive*" på Sparrow.


![Image](assets/fr/60.webp)


Sparrow kommer att visa den första tomma mottagningen Address i din Wallet.


![Image](assets/fr/61.webp)


Innan vi använder den, låt oss kontrollera den på Jade Plus-skärmen för att se till att den tillhör vår Bitcoin Wallet. På Jade, klicka på "*Scan QR*" och skanna sedan QR-koden för Address som visas på Sparrow.


![Image](assets/fr/62.webp)


Kontrollera att Address som visas på din Jades skärm motsvarar den som visas på Sparrow wallet. Om det gör det, klicka på bocken för att fortsätta.


![Image](assets/fr/63.webp)


Din Hardware Wallet kommer då att bekräfta att denna Address är en del av din Wallet och att den har den tillhörande privata nyckeln.


![Image](assets/fr/64.webp)


Om Address valideras av din Jade kan du nu använda den för att ta emot bitcoins. När transaktionen sänds ut i nätverket kommer den att visas på Sparrow. Vänta tills du har fått tillräckligt många bekräftelser för att betrakta transaktionen som slutgiltig.


![Image](assets/fr/65.webp)


## Skicka bitcoins


Nu när du har några Sats i din Wallet kan du också skicka några. För att göra det, klicka på menyn "*UTXOs*".


![Image](assets/fr/66.webp)


Välj de UTXO:er som du vill använda som inmatningar för den här transaktionen och klicka sedan på "*Send Selected*".


![Image](assets/fr/67.webp)


Ange mottagarens Address, en etikett som påminner dig om syftet med transaktionen och det belopp som du vill skicka till denna Address.


![Image](assets/fr/68.webp)


Justera avgiftssatsen enligt rådande marknadsförhållanden och klicka sedan på "*Create Transaction*".


![Image](assets/fr/69.webp)


Kontrollera att alla transaktionsparametrar är korrekta och klicka sedan på "*Finalize Transaction for Signing*".


![Image](assets/fr/70.webp)


Klicka på "*Show QR*" för att visa PSBT (*Partially Signed Bitcoin Transaction*). Sparrow har byggt transaktionen, men den saknar fortfarande signaturerna för att låsa upp bitcoins som används i inmatningen. Dessa signaturer kan endast utföras av Jade Plus, som är värd för din seed och ger tillgång till de privata nycklar som behövs för att signera transaktionen.


![Image](assets/fr/71.webp)


På din Jade Plus, klicka på "*Scan QR*" för att skanna PSBT som visas på Sparrow.


![Image](assets/fr/72.webp)


Bekräfta att leveransen Address och det skickade beloppet är korrekta och klicka sedan på pilen för att validera.


![Image](assets/fr/73.webp)


Kontrollera att avgiftsbeloppet är det du har valt och klicka sedan på krysset i det övre vänstra hörnet på Interface för att signera transaktionen.


![Image](assets/fr/74.webp)


På Sparrow wallet, klicka på "*Scan QR*" och skanna QR-koden som visas på din Jade.


![Image](assets/fr/75.webp)


Din signerade transaktion är nu redo att sändas i Bitcoin-nätverket och inkluderas i ett block av en Miner. Om allt är korrekt klickar du på "*Broadcast Transaction*".


![Image](assets/fr/76.webp)


Din transaktion har sänts och väntar på bekräftelse.


![Image](assets/fr/77.webp)


Gratulerar, du vet nu hur du ställer in och använder Jade Plus i QR-läge. Om du tyckte att denna handledning var användbar skulle jag vara tacksam om du lämnade en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack för att du delar med dig!


Om du vill gå vidare rekommenderar jag den här andra handledningen om Jade Plus, där vi konfigurerar den via Bluetooth med Green-mobilappen:


https://planb.network/tutorials/wallet/hardware/jade-plus-green-873099a4-35ec-4be8-b31a-6e7cd6a41ec0