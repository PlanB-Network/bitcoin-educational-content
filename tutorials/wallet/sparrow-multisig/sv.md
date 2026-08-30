---
name: Sparrow Wallet - Multisig
description: Skapa en Multisig Wallet på Sparrow
---
![cover](assets/cover.webp)


En Multisig Wallet (ofta kallad "*Multisig*") är en Bitcoin Wallet-struktur som kräver flera kryptografiska signaturer, från olika nycklar, för att auktorisera en utgift. Till skillnad från en konventionell ("*singlesig*") Wallet, där en enda privat nyckel räcker för att låsa upp en UTXO, bygger Multisig på en **m-av-n**-modell: av de _n_ nycklar som är kopplade till Wallet måste _m_ ovillkorligen samsignera varje transaktion.


Denna mekanism gör det möjligt att dela kontrollen över en Wallet mellan flera enheter eller enheter. I en 2-av-3-konfiguration genereras till exempel tre oberoende nyckeluppsättningar, men bara två behövs för att frigöra medel. Denna arkitektur minskar drastiskt riskerna kopplade till att en nyckel äventyras eller går förlorad: en tjuv med tillgång till bara en nyckel kan inte tömma Wallet, och en användare som förlorar en kan fortfarande komma åt sina medel med de återstående två.


![Image](assets/fr/01.webp)


Denna ökade säkerhet kommer dock med större komplexitet. Att konfigurera en Multisig Wallet kräver att man säkrar flera återställningsfraser (en per signaturfaktor) och utökade publika nycklar ("*xpub*"). Om du använder en Multisig 2-av-3-Wallet måste du, för att återfå Wallet, antingen ha alla tre återställningsfraserna eller åtminstone två av de tre. Men om du bara har två av de tre fraserna behöver du också tillgång till de tre *xpub*:erna, utan vilka det blir omöjligt att återfå de publika nycklar som krävs för att komma åt de bitcoins de skyddar.


Sammanfattningsvis, för att återställa en Multisig Wallet måste du :


- Antingen ha tillgång till alla återställningsfraser som hör till varje signaturfaktor;
- Eller ha det minsta antal återställningsfraser som krävs enligt tröskelvärdet för att kunna signera, och dessutom ha tillgång till xpub:erna för samtliga faktorer för att kunna återfå de nödvändiga publika nycklarna.


![Image](assets/fr/02.webp)


Denna hantering av säkerhetskopior för Multisig Wallet underlättas av *Output Script Descriptors*, som samlar all publik data som krävs för att komma åt medlen. Denna funktionalitet är dock ännu inte implementerad i alla Wallet-hanteringsprogram.


Multisig passar särskilt bra för bitcoiners som söker ökad säkerhet eller kollektiv förvaltning av medel: företag, föreningar, familjer eller enskilda användare som innehar en betydande mängd bitcoins. Den kan användas för att skapa decentraliserade styrningsmodeller, till exempel för att fördela signaturbehörighet mellan flera förvaltare eller teammedlemmar.


I den här handledningen lär vi oss hur man skapar och använder en klassisk Multisig Wallet med **Sparrow Wallet**. Om du vill skapa en anpassad Multisig Wallet med timelocks rekommenderar jag att du använder Liana istället:


https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Förutsättningar


I den här handledningen visar jag hur man skapar en Multisig med [Wallet-hanteringsprogramvaran Sparrow Wallet](https://sparrowwallet.com/download/). Om du inte redan har installerat den här programvaran, gör det nu. Om du behöver hjälp har vi också en detaljerad handledning om hur du konfigurerar Sparrow Wallet :


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

För att skapa en Multisig behöver du olika Hardware Wallets. För en Multisig 2-av-3 skulle du till exempel kunna använda :


- En Trezor Model One;
- Ledger Flex;
- En Passport Core.


![Image](assets/fr/03.webp)


Det är en bra idé att använda olika märken av Hardware Wallet i din Multisig-konfiguration. Detta säkerställer att om en specifik modell drabbas av ett allvarligt problem, påverkar det inte den övergripande säkerheten för din Multisig. Dessutom kan du dra nytta av de specifika fördelarna hos varje enhet. I min konfiguration, till exempel :



- Trezor Model One är helt öppen källkod, vilket gör det möjligt att verifiera seed-genereringen. Eftersom den dock inte har ett Secure Element är den fortfarande sårbar för fysiska attacker;



- Ledger Flex å andra sidan drar nytta av overifierbar proprietär firmware, men innehåller ett Secure Element som ger utmärkt fysiskt skydd;



- Passport Core kombinerar helt öppen källkodsfirmware, ett Secure Element och air-gapped QR-kodutbyten. Det är en oberoende tredje signerare som kan verifiera adresser och signera PSBT:er utan en USB-dataanslutning.


Innan du konfigurerar din Multisig Wallet, se till att varje Hardware Wallet är korrekt konfigurerad (generering och sparande av återställningsfras, PIN-definition). För detaljerade instruktioner kan du läsa våra handledningar för varje Hardware Wallet, till exempel :


https://planb.academy/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.academy/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Som vi kommer att se längre fram i den här handledningen är det också möjligt att i din Multisig-konfiguration integrera en faktor som inte är kopplad till en Hardware Wallet, men vars privata nycklar lagras på din dator. Denna metod är uppenbarligen mindre säker än att uteslutande använda Hardware Wallets, men den kan vara relevant i vissa fall. För en Multisig 2-av-3 skulle du till exempel kunna välja två Hardware Wallets och en Software Wallet.

> ⚠️ **Säkerhetsmeddelande för Coldcard MK3:** skapa inte en ny seed på en MK3 som kör firmware äldre än 4.2.0. Seeds som genererats på äldre firmware måste bytas ut och medlen flyttas. Den här handledningen använder därför Passport Core som sin air-gapped referenssignerare.


## Skapa en Multisig Wallet


Öppna Sparrow Wallet, klicka på fliken "*File*" och välj sedan "*New Wallet*".


![Image](assets/fr/04.webp)


Tilldela ett namn till din Multisig Wallet och klicka sedan på "*Create Wallet*" för att bekräfta.


![Image](assets/fr/05.webp)


I rullgardinsmenyn "*Policy Type*" väljer du alternativet "*Multi Signature*".


![Image](assets/fr/06.webp)


I det övre högra hörnet kan du nu definiera det totala antalet nycklar i din Multisig, samt antalet medsignerare som krävs för att auktorisera en utgift. I mitt exempel är detta ett 2-av-3-schema.


![Image](assets/fr/07.webp)


Längst ner i fönstret visar Sparrow Wallet tre "*Keystore*". Var och en representerar en nyckeluppsättning. Här använder jag tre Hardware Wallets, så varje "*Keystore*" motsvarar en av dem. Vi ska nu konfigurera dem.


Jag börjar med Passport Core. I fliken "*Keystore 1*" väljer jag alternativet "*Airgapped Hardware Wallet*".


![Image](assets/fr/08.webp)


På Passport öppnar du det konto du vill använda och väljer sedan "*Connect Wallet*" > "*Sparrow*" > "*Connect as Multisig*". Passport visar en animerad QR-kod som innehåller dess publika nyckelinformation.

I Sparrow väljer du "*Scan...*" bredvid "*Passport*" och skannar den animerade QR-koden med datorns webbkamera. Kontrollera fingeravtrycket för huvudnyckeln som visas av Sparrow mot det som visas av Passport, och importera sedan Keystore.

Din Passport-xpub har nu importerats. Upprepa motsvarande procedur för Ledger Flex och Trezor Model One.


För Ledger Flex väljer jag "*Keystore 2*" och klickar sedan på "*Connected Hardware Wallet*". Se till att Ledger är ansluten till datorn, upplåst, och att Bitcoin-applikationen är öppen.


![Image](assets/fr/15.webp)


Klicka sedan på knappen "*Scan...*".


![Image](assets/fr/16.webp)


Bredvid namnet på din Hardware Wallet klickar du på "*Import Keystore*".


![Image](assets/fr/17.webp)


Den andra undertecknaren är nu korrekt registrerad i Sparrow Wallet.


![Image](assets/fr/18.webp)


Jag upprepar exakt samma procedur med Trezor One för att slutföra Multisig-konfigurationen.


![Image](assets/fr/19.webp)


I min konfiguration täcker vi inte det här fallet, men om du vill inkludera en signatur via en Software Wallet i Sparrow (Hot Wallet) i din Multisig klickar du bara på knappen "*New or Imported Software Wallet*".


Nu när alla dina signaturenheter är importerade till Sparrow Wallet kan du slutföra skapandet av Multisig genom att klicka på "*Apply*".


![Image](assets/fr/20.webp)


Välj ett starkt lösenord för att säkra åtkomsten till din Sparrow Wallet-Wallet. Detta lösenord skyddar dina publika nycklar, adresser, etiketter och transaktionshistorik från obehörig åtkomst.


Kom ihåg att spara det här lösenordet på ett säkert ställe, till exempel i en lösenordshanterare, för att undvika att förlora det.


![Image](assets/fr/21.webp)


## Säkerhetskopiera en Multisig Wallet


Vi ska nu spara *Output Script Descriptor* på ett oberoende medium och behålla flera kopior av den.


*Descriptor* innehåller alla xpub:er i din Multisig Wallet, samt de härledningsvägar som används för att generera nycklarna. Kom ihåg vad vi såg i del 1: för att återställa en Multisig Wallet måste du antingen ha **alla** återställningsfraser, eller bara det minsta antal som krävs för att nå signaturtröskeln. I det senare fallet är det dock också avgörande att ha **xpub:erna** för de saknade undertecknarna. *Descriptor* innehåller alla din Multisigs xpub:er.


Om detta inte är klart, kom bara ihåg detta: för att återfå en Multisig behöver du det minsta antalet återställningsfraser för varje använd Hardware Wallet, beroende på tröskelvärdet (i mitt fall: 2 fraser), samt *Descriptor*.


Denna *Descriptor* innehåller inga privata nycklar, endast publika. Det innebär att den inte ger tillgång till medlen. Den är därför inte lika kritisk som återställningsfraserna, som ger fullständig tillgång till dina bitcoins. Risken med *Descriptor* handlar uteslutande om sekretess: om den äventyras skulle en tredje part kunna observera alla dina transaktioner, men inte kunna spendera dina medel.


Jag rekommenderar starkt att du skapar flera kopior av denna *Descriptor* och förvarar dem tillsammans med varje signaturenhet i din Multisig. I mitt fall skriver jag till exempel ut *Descriptor* på papper och förvarar en kopia med Passport, en annan med Trezor och en med Ledger. Jag sparar också denna *Descriptor* som en PDF-fil på tre USB-minnen, var och en förvarad tillsammans med en av Hardware Wallets. På så sätt maximerar jag mina chanser att aldrig förlora denna *Descriptor*, och jag är säker på att ha två kopior (en fysisk och en digital) med varje enhet.


När din Multisig Wallet har skapats tillhandahåller Sparrow automatiskt denna *Descriptor* till dig. Klicka på knappen "*Save PDF...*" för att spara den både som text och som QR-kod.


![Image](assets/fr/22.webp)


Du kan sedan skriva ut denna PDF och kopiera den till dina USB-minnen.


![Image](assets/fr/23.webp)


Passport använder Multisig-konfigurationen som importerats av Sparrow för att visa och verifiera relevant nyckelinformation under QR-parkopplingen och signeringsflödet. Förvara *Descriptor* separat: den förblir avgörande för att återställa Wallet om en undertecknare inte är tillgänglig.


Utöver att spara *Descriptor*, glöm inte att ägna särskild uppmärksamhet åt att spara återställningsfraserna för var och en av dina signaturenheter. Om du precis har börjat rekommenderar jag starkt att du läser den här andra handledningen för att lära dig hur du sparar och hanterar dem korrekt:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Innan du tar emot dina första bitcoins på din Multisig **rekommenderar jag starkt att du utför ett återställningstest med en tom Wallet**. Anteckna viss referensinformation, till exempel den första mottagningsadressen, och återställ sedan dina Hardware Wallets till fabriksinställningarna medan Wallet fortfarande är tom. Försök sedan återställa din Multisig Wallet på Hardware Wallets med hjälp av dina återställningsfraser i pappersform, och sedan på Sparrow med hjälp av *Descriptor*. Kontrollera att den första adress som genereras efter återställningen matchar den du ursprungligen skrev ner. Om den gör det kan du vara säker på att dina pappersbaserade säkerhetskopior är tillförlitliga.


För att lära dig mer om hur du utför ett återställningstest föreslår jag att du läser den här andra handledningen:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Ta emot bitcoins på din Multisig


Din Wallet är nu redo att ta emot bitcoins. I Sparrow klickar du på fliken "*Receive*".


![Image](assets/fr/30.webp)


Innan du använder den adress som genereras av Sparrow Wallet, ta dig tid att kontrollera den direkt på skärmen på dina Hardware Wallets. Detta säkerställer att adressen inte har ändrats, och att dina enheter har de privata nycklar som krävs för att spendera de tillhörande medlen. Detta hjälper till att skydda dig mot ett antal attackvektorer.


För att göra detta, klicka på "*Display Address*" för att visa adressen på din Trezor eller Ledger, när den är ansluten med kabel.


![Image](assets/fr/31.webp)


Med Passport väljer du Multisig-kontot och väljer "*Verify Address*". Skanna QR-koden för den mottagningsadress som visas av Sparrow. Passport bekräftar på sin skärm om adressen tillhör Multisig Wallet.


Kontrollera att adressen som visas på varje Hardware Wallet exakt motsvarar den i Sparrow Wallet. Det är lämpligt att göra detta precis innan du delar adressen med betalaren, för att vara säker på dess integritet.


Du kan sedan tilldela en "*Label*" till denna adress för att ange ursprunget för de mottagna bitcoinsen. Detta är ett bra sätt att organisera hanteringen av dina UTXO:er.


![Image](assets/fr/34.webp)


När detta har verifierats kan du använda adressen för att ta emot bitcoins.


![Image](assets/fr/35.webp)


## Skicka bitcoins med din Multisig


Nu när du har tagit emot dina första sats på din Multisig Wallet kan du också spendera dem! I Sparrow går du till fliken "*Send*" för att bygga en ny transaktion.


![Image](assets/fr/36.webp)


Om du vill använda *Coin Control*, dvs. manuellt välja de UTXO:er du vill spendera, går du till fliken "*UTXOs*". Välj de UTXO:er du vill spendera och klicka sedan på "*Send Selected*". Du omdirigeras automatiskt till fliken "*Send*", med UTXO:erna redan förifyllda.


![Image](assets/fr/37.webp)


Ange destinationsadressen. Flera adresser kan läggas till genom att klicka på "*+ Add*".


![Image](assets/fr/38.webp)


Lägg till en "*Label*" för att beskriva syftet med denna utgift, för att göra det lättare att spåra dina transaktioner.


![Image](assets/fr/39.webp)


Ange det belopp som ska skickas till den valda adressen.


![Image](assets/fr/40.webp)


Justera avgiftsnivån utifrån aktuella nätverksförhållanden. Kontrollera till exempel [Mempool.space](https://Mempool.space/) för att välja en lämplig avgiftsnivå.


Efter att ha kontrollerat alla transaktionsparametrar klickar du på "*Create Transaction*".


![Image](assets/fr/41.webp)


Om du är nöjd med allt klickar du på "*Finalize Transaction for Signing*".


![Image](assets/fr/42.webp)


Längst ner på skärmen ser du att Sparrow väntar på 2 signaturer. Detta är normalt: Wallet som används här är en Multisig 2-av-3.


![Image](assets/fr/43.webp)


Jag börjar signera med min Passport. I Sparrow klickar du på "*Show QR*" för att visa PSBT:n (*Partially Signed Bitcoin Transaction*) som animerade QR-koder. På Passport väljer du Multisig-kontot och väljer "*Sign with QR Code*", och skannar sedan QR-koden som visas av Sparrow.


På skärmen på din Hardware Wallet, kontrollera noggrant transaktionsparametrarna: mottagarens adress, det skickade beloppet och avgifterna. När transaktionen har bekräftats validerar du för att fortsätta till signeringen.


Efter att du godkänt transaktionen visar Passport den signerade PSBT:n som animerade QR-koder. I Sparrow klickar du på "*Scan QR*" och skannar dessa koder med din webbkamera. Passports signatur läggs sedan till. Jag använder nu Ledger för den andra nödvändiga signaturen: jag ansluter och låser upp den, och klickar sedan på "*Sign*" i Sparrow.


![Image](assets/fr/48.webp)


Klicka på "*Sign*" bredvid namnet på din Hardware Wallet.


![Image](assets/fr/49.webp)


Första gången du använder din Ledger med denna Multisig kommer Sparrow att be dig verifiera de utökade publika nycklarna (xpub:erna) för medsignerarna. Precis som med Passport förhindrar detta steg dig från att signera blint senare. För att validera denna information jämför du xpub:en som visas på Ledger-skärmen med dem som tillhandahålls direkt av dina andra Hardware Wallets.


![Image](assets/fr/50.webp)


Kontrollera mottagarens adress, det överförda beloppet och transaktionsavgiften, och signera sedan transaktionen.


![Image](assets/fr/51.webp)


Tryck på skärmen för att signera.


![Image](assets/fr/52.webp)


Sparrow har nu de två signaturer som krävs för att frigöra medlen från Multisig Wallet. Kontrollera transaktionen en sista gång, och om allt ser bra ut klickar du på "*Broadcast Transaction*" för att sända ut den i nätverket.


![Image](assets/fr/53.webp)


Du hittar denna transaktion i fliken "*Transactions*" i Sparrow Wallet.


![Image](assets/fr/54.webp)


Grattis, nu vet du hur man konfigurerar och använder en Multisig Wallet på Sparrow. Om du fann den här handledningen användbar skulle jag uppskatta om du lämnade en grön tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack för att du delar!


För att gå vidare rekommenderar jag att du läser den här handledningen om en annan metod för att öka säkerheten för din Bitcoin Wallet, BIP39-lösenfrasen :


https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
