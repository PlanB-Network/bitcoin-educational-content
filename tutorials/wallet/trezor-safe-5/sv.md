---
name: Trezor Safe 5
description: Konfigurera och använda Hardware Wallet Safe 5
---
![cover](assets/cover.webp)



*Bildkredit: [Trezor.io] (https://trezor.io/)*


![video](https://youtu.be/LI_EMXn6_Ss)


Trezor Safe 5 är en Hardware Wallet av senaste generationen som designats av SatoshiLabs och lanserades 2024. Den är positionerad som en high-end version av Safe 3, med fokus på ergonomi och hållbarhet. Den drar nytta av samma säkerhetsframsteg som sin föregångare Safe 3, jämfört med Model One och Model T.



Med ett pris på 169 euro är Safe 5 placerad i den avancerade Hardware Wallet-kategorin och konkurrerar med modeller som Coldcard, Ledger Nano X och Flex, Jade Plus, Passport och Bitbox.



Safe 5 kännetecknas av sin 1,54-tums färgpekskärm, skyddad av *Gorilla Glass 3*, som står emot stötar och repor. Den är också utrustad med en *Trezor Touch* haptisk motor som avger små vibrationer vid beröring. Precis som Safe 3 har den ett Secure Element och drivs via en USB-C-anslutning, med tillägg av en Micro SD-port.



Den största skillnaden mellan Safe 3 och Safe 5 ligger i enhetens kvalitet, bortsett från säkerhetsaspekterna. Den förbättrar användarupplevelsen avsevärt, med smidigare drift och en mer bekväm skärm. När det gäller säkerhet är den likvärdig.



![Image](assets/fr/01.webp)



Safe 5 har alla de viktiga funktioner som du kan förvänta dig av en bra Hardware Wallet, inklusive utmärkt integrering av passphrase BIP39. Den har dock ännu inte stöd för Miniscript.



Denna modell är särskilt lämpad för nybörjare och användare på mellannivå. Å andra sidan kanske den inte uppfyller alla förväntningar hos avancerade användare som letar efter mer specifika funktioner som finns på enheter som Coldcard. Om du inte behöver dessa avancerade alternativ kan Trezor Safe 5 ändå vara ett utmärkt val.



## Säkerhetsmodellen Trezor Safe 5



Precis som Safe 3 är Trezor Safe 5 utrustat med ett EAL6+-certifierat **Secure Element**, ett betydande framsteg jämfört med tidigare modeller som Model One och Model T. Detta är OPTIGA Trust M V3-chipet, som inte lagrar seed direkt, utan fungerar som en kryptografisk komponent för att säkra åtkomsten till den. Secure Element lagrar en hemlighet som endast kan nås när användaren har angett PIN-koden korrekt. Denna hemlighet används sedan för att dekryptera seed, som lagras krypterad i enhetens huvudminne.



Detta hybrida säkerhetssystem ger förbättrat fysiskt skydd, särskilt mot extraktionsattacker eller invasiv analys, problem som Model One var utsatt för, särskilt när det gäller PIN-hantering. Dessa sårbarheter kringgås nu tack vare användningen av Secure Element. Denna modell har också en mjukvaruarkitektur med öppen källkod: den kod som hanterar generering och användning av privata nycklar förblir fullt tillgänglig och verifierbar. OPTIGA-chipet hanterar endast PIN-koden, ett element som inte ingår i Bitcoin Wallet:s nyckelhantering. Det är begränsat till att släppa en hemlighet som kan användas för att dekryptera seed. OPTIGA Trust M V3-chipet drar också nytta av en relativt fri licens, som tillåter SatoshiLabs att fritt publicera potentiella sårbarheter (NDA-Free).



Den här säkerhetsmodellen är enligt min mening en av de bästa kompromisser som finns på marknaden idag. Den kombinerar fördelarna med ett Secure Element med programvaruhantering med öppen källkod. Tidigare var användarna tvungna att välja mellan förbättrad fysisk säkerhet med ett chip och öppenhet med öppen källkod; med Trezor Safe är det möjligt att dra nytta av båda.



I denna handledning lär du dig hur du konfigurerar och använder din Trezor Safe 5 på ett säkert sätt.



## Uppackning av Trezor Safe 5



När du får din Safe 5, se till att lådan och Seal är intakta för att bekräfta att paketet inte har öppnats. En programvarukontroll av enhetens äkthet och integritet kommer också att utföras när den installeras senare.



Innehållet i lådan inkluderar :




- Trezor Safe 5;
- En påse som innehåller kartong för att spela in din Mnemonic-fras, klistermärken och instruktioner;
- USB-C till USB-C-kabel.



När du öppnar din Trezor Safe 5 ska den skyddas av en skyddande plast och USB-C-porten ska säkras av en holografisk Seal. Se till att den finns där.



![Image](assets/fr/02.webp)



Navigeringen på enheten är ganska intuitiv:




- Tryck på den nedre halvan av skärmen för att flytta framåt;
- Skjut ner för att gå tillbaka ;
- Håll skärmen intryckt för att bekräfta en åtgärd.



## Förkunskapskrav



I den här handledningen ska jag visa dig hur du använder Trezor Safe 5 med [Sparrow wallet Wallet management software] (https://sparrowwallet.com/download/). Om du ännu inte har installerat den här programvaran ska du göra det nu. Om du behöver hjälp har vi också en detaljerad handledning om hur du konfigurerar Sparrow wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Du behöver också programvaran Trezor Suite för att konfigurera Safe 5, kontrollera dess äkthet och installera den fasta programvaran. Vi kommer endast att använda den här programvaran för detta, och därefter kommer den endast att behövas för uppdateringar av den fasta programvaran. För den dagliga hanteringen av Wallet kommer vi att använda Sparrow wallet exklusivt, eftersom den är optimerad för Bitcoin och enkel att använda, även för nybörjare (Sparrow stöder endast Bitcoin, inte altcoins).



[Ladda ner Trezor Suite från den officiella webbplatsen] (https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



För båda dessa program rekommenderar jag starkt att du kontrollerar både deras äkthet (med GnuPG) och deras integritet (via Hash) innan du installerar dem på din maskin. Om du inte vet hur du gör detta kan du följa den här andra handledningen :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Starta upp Trezor Safe 5



Anslut din Safe 5 till din dator där Trezor Suite och Sparrow wallet redan är installerade.



![Image](assets/fr/04.webp)



Öppna Trezor Suite och klicka sedan på "*Set up my Trezor*".



![Image](assets/fr/05.webp)



Välj "*Bitcoin-only firmware*" och klicka sedan på "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



Trezor Suite kommer sedan att installera den fasta programvaran på din Safe 5. Vänligen vänta under installationen.



![Image](assets/fr/07.webp)



Klicka på "*Fortsätt*".



![Image](assets/fr/08.webp)



Fortsätt sedan till äkthetstestet för att se till att din Hardware Wallet inte är falsk eller komprometterad.



![Image](assets/fr/09.webp)



På din Safe 5, tryck på skärmen för att bekräfta.



![Image](assets/fr/10.webp)



Om din Trezor är äkta kommer ett bekräftelsemeddelande att visas i Trezor Suite.



![Image](assets/fr/11.webp)



Du kan sedan hoppa över fönstren med de grundläggande bruksanvisningarna.



![Image](assets/fr/12.webp)



## Skapa en Bitcoin Wallet



På Trezor Suite klickar du på knappen "*Create new Wallet*".



![Image](assets/fr/13.webp)



För att skapa en standard BIP39 Wallet, börja med att välja "*Legacy Wallet backup types*" från rullgardinsmenyn och välj sedan mellan en Mnemonic-fras på 12 eller 24 ord (12 ord rekommenderas för närvarande). Detta gör att du kan skapa en klassisk Wallet med en enda signering. Jag råder dig att välja BIP39-kompatibla parametrar här för att underlätta hämtning och undvika att begränsas till en specifik miljö. För att slutföra, klicka på "*Skapa Wallet*".



Om du vill lära dig mer om de andra säkerhetskopieringsalternativen som finns tillgängliga på Trezor, inklusive *Multi-share Backup*, rekommenderar jag att du också läser den här handledningen:



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e


![Image](assets/fr/14.webp)



Acceptera användarvillkoren på Hardware Wallet.



![Image](assets/fr/15.webp)



Håll skärmen intryckt för att skapa en ny Wallet.



![Image](assets/fr/16.webp)



I Trezor Suite klickar du på "*Fortsätt att säkerhetskopiera*".



![Image](assets/fr/17.webp)



Programvaran innehåller instruktioner om hur du hanterar din Mnemonic-fras.



Denna Mnemonic ger dig full, obegränsad tillgång till alla dina bitcoins. Vem som helst som har den här frasen kan stjäla dina pengar, även utan fysisk tillgång till ditt Trezor Safe 5.



Frasen på 12 ord återställer åtkomsten till dina bitcoins i händelse av förlust, stöld eller sönderslagning av din Hardware Wallet. Det är därför mycket viktigt att spara den noggrant och förvara den på en säker plats.



Du kan skriva den på kartongen som medföljer i lådan, eller för extra säkerhet rekommenderar jag att du graverar den på en bas av rostfritt stål för att skydda den mot brand, översvämning eller kollaps.



Bekräfta instruktionerna och klicka sedan på knappen "*Create Wallet backup*".



![Image](assets/fr/18.webp)



Safe 5 kommer att skapa din Mnemonic-fras med hjälp av sin slumptalsgenerator. Se till att du inte blir iakttagen under denna operation. Skriv ner de ord som visas på skärmen på det fysiska medium du väljer. Beroende på din säkerhetsstrategi kan du överväga att göra flera fullständiga fysiska kopior av frasen (men framför allt, dela inte upp den). Det är viktigt att hålla orden numrerade och i sekventiell ordning.



***Du får naturligtvis aldrig dela med dig av dessa ord på Internet, vilket jag gör i den här handledningen. Detta exempel Wallet kommer endast att användas på Testnet och kommer att raderas i slutet av handledningen



För mer information om det rätta sättet att spara och hantera din Mnemonic-fras rekommenderar jag starkt att du följer den här andra handledningen, särskilt om du är nybörjare:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/19.webp)



För att gå vidare till nästa ord klickar du längst ner på skärmen. Du kan gå bakåt genom att glida nedåt. När du har skrivit ner alla ord håller du kvar fingret på skärmen för att gå vidare till nästa steg.



![Image](assets/fr/20.webp)



Markera orden i din Mnemonic-fras enligt deras ordning för att bekräfta att du har skrivit ner dem korrekt.



![Image](assets/fr/21.webp)



När verifieringsproceduren är klar klickar du på skärmen för att fortsätta.



![Image](assets/fr/22.webp)



## Ställa in PIN-koden



Därefter kommer steget med PIN-koden. PIN-koden låser upp din Trezor. Den ger därför skydd mot obehörig fysisk åtkomst. Denna PIN-kod är inte inblandad i härledningen av din Wallet:s kryptografiska nycklar. Så även utan tillgång till PIN-koden kommer du att kunna få tillgång till dina bitcoins om du har din Mnemonic-fras med 12 ord.



På Trezor Suite klickar du på "*Continue to PIN*" och sedan på knappen "*Set PIN*".



![Image](assets/fr/23.webp)



Bekräfta med Safe 5.



![Image](assets/fr/24.webp)



Vi rekommenderar att du väljer en PIN-kod som är så slumpmässig som möjligt. Var noga med att spara denna kod på en annan plats än där din Trezor lagras (t.ex. i en lösenordshanterare). Du kan definiera en PIN-kod med mellan 8 och 50 siffror. Jag rekommenderar att du väljer en PIN-kod som är så lång som möjligt för att öka säkerheten.



Använd pekplattan för att ange din PIN-kod.



![Image](assets/fr/25.webp)



När du är klar klickar du på Green-symbolen längst ned till höger och bekräftar sedan din PIN-kod en andra gång.



![Image](assets/fr/26.webp)



Din PIN-kod har registrerats.



![Image](assets/fr/27.webp)



På Trezor Suite, klicka på knappen "*Complete setup*".



![Image](assets/fr/28.webp)



Konfigurationen av din Safe 5 är nu klar. Om du vill kan du ändra namn och startsida för din Hardware Wallet.



![Image](assets/fr/29.webp)



Vi kommer inte att behöva Trezor Suite-programvaran längre, förutom för att utföra regelbundna firmwareuppdateringar på din Hardware Wallet, eller om du vill köra ett återställningstest. Vi kommer nu att använda Sparrow för att hantera Wallet, eftersom den här programvaran är perfekt lämpad för användning av enbart Bitcoin.



## Konfigurera Wallet på Sparrow wallet



Börja med att ladda ner och installera Sparrow wallet [från den officiella webbplatsen] (https://sparrowwallet.com/) på din dator, om du inte redan har gjort det.



När du har öppnat Sparrow wallet ska du se till att programmet är anslutet till en Bitcoin-nod, vilket indikeras av krysset i det nedre högra hörnet av Interface. Om du har problem med att ansluta Sparrow rekommenderar jag att du läser i början av denna handledning:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klicka på fliken "*File*" och sedan på "*New Wallet*".



![Image](assets/fr/30.webp)



Ge din Wallet ett namn och klicka sedan på "*Create Wallet*".



![Image](assets/fr/31.webp)



I rullgardinsmenyn "*Script Type*" väljer du vilken typ av script som ska användas för att säkra dina bitcoins. Jag rekommenderar "*Taproot*", eller om det inte går, "*Native SegWit*".



![Image](assets/fr/32.webp)



Klicka på knappen "*Connected Hardware Wallet*". Din Safe 5 måste naturligtvis vara ansluten till datorn och upplåst.



När du ansluter din Safe 5 till en dator med Sparrow wallet öppen, kommer du att uppmanas att ange en passphrase BIP39 på Hardware Wallet-skärmen. Detta avancerade alternativ kommer att behandlas i en framtida handledning. För närvarande kan du helt enkelt klicka på Green-fästet i det övre högra hörnet för att bekräfta att du vill använda en tom passphrase (dvs. utan en passphrase). För att förhindra att din Trezor ber dig att ange en passphrase varje gång du startar, gå till Trezor Suite, öppna inställningarna och ändra alternativet i "*Device*" > "*Wallet default*" till "*Standard*" istället för "*passphrase*".



![Image](assets/fr/33.webp)



Klicka på knappen "*Scan*". Din Safe 5 bör visas. Klicka på "*Importera Keystore*".



![Image](assets/fr/34.webp)



Du kan nu se detaljerna för din Wallet, inklusive den utökade publika nyckeln för ditt första konto. Klicka på knappen "*Apply*" för att slutföra skapandet av Wallet.



![Image](assets/fr/35.webp)



Välj ett starkt lösenord för att säkra åtkomsten till Sparrow wallet. Detta lösenord garanterar säker åtkomst till dina Sparrow wallet-data och skyddar dina offentliga nycklar, adresser, etiketter och transaktionshistorik från obehörig åtkomst.



Jag råder dig att spara det här lösenordet i en lösenordshanterare så att du inte glömmer det.



![Image](assets/fr/36.webp)



Och nu har din Wallet importerats till Sparrow wallet!



![Image](assets/fr/37.webp)



Innan du får dina första bitcoins i din Wallet, **råder jag dig starkt att utföra ett tomt återställningstest**. Skriv ner lite referensinformation, t.ex. din xpub, och återställ sedan din Trezor Safe 5 medan Wallet fortfarande är tom. Försök sedan återställa din Wallet på Trezor med hjälp av dina pappersbackuper. Kontrollera att den xpub som genereras efter återställningen matchar den som du ursprungligen skrev ner. Om den gör det kan du vara säker på att dina pappersbackuper är tillförlitliga.



Om du vill veta mer om hur du utför ett återställningstest föreslår jag att du läser den här andra handledningen:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Hur kan jag ta emot bitcoins med Trezor Safe 5?



På Sparrow klickar du på fliken "*Receive*".



![Image](assets/fr/38.webp)



Innan du använder den Address som föreslås av Sparrow wallet, kontrollera den på din Trezors skärm. Denna metod gör att du kan bekräfta att Address som visas på Sparrow inte är bedräglig och att Hardware Wallet verkligen har den privata nyckel som behövs för att därefter spendera de bitcoins som är säkrade med denna Address. Detta hjälper dig att undvika flera typer av attacker.



För att utföra denna kontroll klickar du på knappen "*Display Address*".



![Image](assets/fr/39.webp)



Kontrollera att den Address som visas på din Trezor stämmer överens med den på Sparrow wallet. Det är också lämpligt att utföra denna kontroll strax innan du kommunicerar din Address till avsändaren, för att vara säker på att den är giltig. Du kan trycka på skärmen för att bekräfta.



![Image](assets/fr/40.webp)



Du kan sedan lägga till en "*Label*" för att beskriva källan till bitcoins som kommer att säkras med denna Address. Det här är en bra metod som gör att du kan hantera dina UTXO:er bättre.



![Image](assets/fr/41.webp)



Du kan sedan använda denna Address för att ta emot bitcoins.



![Image](assets/fr/42.webp)



## Hur skickar jag bitcoins med Trezor Safe 5?



Nu när du har fått dina första Satss på din Safe 5-säkrade Wallet kan du spendera dem också! Anslut din Trezor till din dator, lås upp den med PIN-koden, starta Sparrow wallet och gå sedan till fliken "*Send*" för att skapa en ny transaktion.



![Image](assets/fr/43.webp)



Om du vill *Coin Control*, dvs. välja specifikt vilka UTXO:er som ska användas i transaktionen, går du till fliken "*UTXO:er*". Välj de UTXO:er du vill använda och klicka sedan på "*Send Selected*". Du kommer att omdirigeras till samma skärm på fliken "*Send*", men med dina UTXO:er redan valda för transaktionen.



![Image](assets/fr/44.webp)



Ange destinationen Address. Du kan också ange flera adresser genom att klicka på knappen "*+ Add*".



![Image](assets/fr/45.webp)



Skriv ner en "*Label*" för att komma ihåg syftet med denna kostnad.



![Image](assets/fr/46.webp)



Välj det belopp som ska skickas till denna Address.



![Image](assets/fr/47.webp)



Justera avgiftssatsen för din transaktion enligt den aktuella marknaden. Du kan t.ex. använda [Mempool.space] (https://Mempool.space/) för att välja en lämplig avgiftssats.



Kontrollera att alla dina transaktionsparametrar är korrekta och klicka sedan på "*Create Transaction*".



![Image](assets/fr/48.webp)



Om allt är till belåtenhet klickar du på "*Finalize Transaction for Signing*".



![Image](assets/fr/49.webp)



Klicka på "*Signera*".



![Image](assets/fr/50.webp)



Klicka på "*Sign*" bredvid din Trezor Safe 5.



![Image](assets/fr/51.webp)



Kontrollera transaktionsparametrarna på din Hardware Wallet-skärm, inklusive mottagarens mottagande Address, det skickade beloppet och avgiften. När transaktionen har verifierats på Trezor trycker du på skärmen och håller den intryckt för att signera den.



![Image](assets/fr/52.webp)



Din transaktion är nu signerad. Kontrollera en sista gång att allt är OK och klicka sedan på "*Broadcast Transaction*" för att sända den i Bitcoin-nätverket.



![Image](assets/fr/53.webp)



Du hittar den under fliken "*Transaktioner*" i Sparrow wallet.



![Image](assets/fr/54.webp)



Gratulerar, du har nu lärt dig den grundläggande användningen av Trezor Safe 5 med Sparrow wallet! För att ta saker ett steg längre rekommenderar jag denna omfattande handledning om hur du använder en Trezor Hardware Wallet med en passphrase BIP39 för att förbättra din säkerhet:



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Om du tyckte att den här handledningen var användbar skulle jag vara tacksam om du lämnar en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!