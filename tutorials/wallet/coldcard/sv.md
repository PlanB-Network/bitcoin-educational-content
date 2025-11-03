---
name: COLDCARD Mk

description: Skapa, säkerhetskopiera och använda en privat Bitcoin-nyckel med en Coldcard-enhet och Bitcoin Core
---

![cover](assets/cover.webp)


_Creating, back-up, and using a Bitcoin private key with a Coldcard device and Bitcoin Core_ (Skapa, säkerhetskopiera och använda en privat Bitcoin-nyckel med en Coldcard-enhet och Bitcoin Core)


## Komplett guide för att generera en privat nyckel med ett Coldcard och använda den via Interface i din Bitcoin Core-nod!


Kärnan i Bitcoin:s nätverksanvändning är konceptet asymmetrisk kryptografi: ett par nycklar - en privat och en offentlig - som krypterar och dekrypterar data, ett koncept som säkerställer kommunikationens integritet.


I fallet Bitcoin kan vi, genom att generera ett sådant par av privata och publika nycklar, lagra bitcoins (UTXO eller Unspent Transaction Output) och signera transaktioner för att spendera dem.


Idag finns det flera verktyg tillgängliga för att underlätta den slumpmässiga genereringen av en privat nyckel och dess säkerhetskopiering i textform med hjälp av BIP 39 - en standard som bestämmer hur plånböcker associerar en Mnemonic-fras (seed-fras) med krypteringsnycklar. Oftast består Mnemonic-frasen av 12 eller 24 ord, som måste säkerhetskopieras på ett säkert sätt för att kunna återställa en Wallet och dess bitcoins.


I den här artikeln kommer vi att lära oss hur man generate en privat nyckel med hjälp av ett Coldcard Mk4, en av de mest använda och säkra enheterna i Bitcoin-världen, med hjälp av tärningsrullningsmetoden för att säkerställa maximal entropi, och hur man använder den med Bitcoin Core på ett luftgapat sätt!


**Note:🧰** Skaffa följande verktyg för att använda guiden:



- Coldcard-enhet (Mk3 eller Mk4)
- MicroSD-kort (4 GB är tillräckligt)
- Magnetisk USB-kabel för strömförsörjning (mini-usb för Mk3, usb-c för Mk4)
- En eller flera kvalitetstärningar


## Generera en ny Mnemonic-fras med ett Coldcard


Vi börjar med att skapa en privat nyckel från början, med ett nyuppackat Coldcard där en PIN-kod redan har ställts in (följ stegen på Coldcard under initieringen av enheten).


**Note🚨:** Gör så här för att återställa den privata nyckeln för ett redan konfigurerat Coldcard:

_Avancerat/Verktyg > Farozonen > seed Funktioner > Förstöra seed > ✓_


**Attention:** ditt Coldcard kommer att glömma den privata nyckeln efter dessa steg. Se till att du har säkerhetskopierat din Mnemonic-fras ordentligt om du vill kunna återställa den senare.


## Steg att följa:


Anslut till Coldcard med PIN-kod > Nya seed-ord > Tärningsslag med 24 ord


Utför 100 tärningskast och skriv ner resultatet från 1 till 6 på Coldcard efter varje kast. Genom att praktisera denna metod skapar du 256 byte entropi, vilket gynnar skapandet av en helt slumpmässig privat nyckel. Coinkite tillhandahåller också nödvändig dokumentation för oberoende verifiering av deras entropigenereringssystem.


![Visual Cold Card Screenshot](assets/guide-agora/1.webp)


När de 100 tärningskastningarna är klara trycker du på ✓ och skriver sedan ner de 24 erhållna orden i ordning. Verifiera två gånger och tryck på ✓. Slutligen är allt som återstår att slutföra verifieringstestet av de 24 orden på Coldcard, och voila, din nya privata nyckel är skapad!


Välj sedan om du vill aktivera NFC (Mk4)- och USB-funktionerna genom att följa de steg som visas. Väl i huvudmenyn är det nu dags att uppdatera enhetens firmware. Gå till Advanced/Tools > Upgrade Firmware > Show Version och kontrollera den officiella webbplatsen för att validera och ladda ner den senaste tillgängliga versionen. Det är lämpligt att uppdatera Coldcard för att dra nytta av maximal säkerhet.


Innan du fortsätter rekommenderas att du noterar Master Key Fingerprint (XFP) som är kopplat till den privata nyckeln. Dessa data möjliggör en snabb validering av om du befinner dig i rätt Wallet, t.ex. vid återställning. Gå till Advanced/Tools > View Identity > Master Key Fingerprint (XFP) och skriv ner den serie om åtta alfanumeriska tecken som erhålls. XFP kan noteras på samma ställe som Mnemonic frasen, det är inte känslig data.


** Notera: 💡** det rekommenderas att testa din Mnemonic-fras säkerhetskopiering i en annan programvara. För att göra detta säkert, se vår artikel Verifiera säkerhetskopian av en Bitcoin Wallet med Tails på mindre än 5 minuter.


## Säkerhetsbonus: den "hemliga frasen" (valfritt)


En passphrase (hemlig fras) är ett bra element att lägga till i en Wallet-konfiguration för att lägga till en Layer av säkerhet för att skydda dina bitcoins. passphrase fungerar som ett slags 25:e ord till Mnemonic-frasen. När den har lagts till skapas en helt ny Wallet tillsammans med en privat nyckel och dess associerade Mnemonic-fras. Det är inte nödvändigt att skriva ner den nya Mnemonic-frasen, eftersom denna Wallet kan nås genom att kombinera den ursprungliga Mnemonic-frasen med den valda passphrase.


Målet är att notera passphrase separat från Mnemonic-fras eftersom en angripare som har tillgång till båda objekten kommer att ha tillgång till medlen. Å andra sidan kommer en angripare som bara har tillgång till en av dessa poster inte att ha tillgång till pengarna, och det är denna specifika fördel som optimerar säkerhetsnivån för Wallet-konfigurationen.


![Adding a passphrase leads to a completely different wallet](assets/guide-agora/2.webp)


## Steg för att lägga till en passphrase med Coldcard:


passphrase > Lägg till ord (rekommenderas) > Tillämpa. Enheten kommer att visa XFP för den nyligen genererade Wallet med passphrase, som bör noteras med passphrase av samma skäl som nämnts tidigare.


**Tips💡** Här finns ytterligare resurser relaterade till passphrase:



- [Här](https://blog.trezor.io/is-your-passphrase-strong-enough-d687f44c63af) finns den första av _Trezor_;
- [Här](https://blog.coinkite.com/everything-you-need-to-know-about-passphrases/) kan du hitta den andra av _Coinkite_;
- Och [här](https://armantheparman.com/passphrase/) hittar du den sista av _armantheparman_.


## Exportera kärnan Wallet till Bitcoin


Wallet är nu redo att exporteras till programvara för att kunna interagera med Bitcoin-nätverket. I den här guiden kommer vi att använda Bitcoin Core (v24.1).


Se våra installations- och konfigurationsguider för Bitcoin Core:



- **Kör din egen nod med Bitcoin Core:** https://agora256.com/faire-tourner-son-propre-noeud-avec-Bitcoin-core/
- **Konfigurera Tor för en Bitcoin Core-nod:** https://agora256.com/configuration-tor-Bitcoin-core/


Sätt först i ett micro SD-kort i Coldcard och exportera sedan Wallet till Bitcoin Core genom att följa dessa steg: Avancerat/Verktyg > Exportera Wallet > Bitcoin Core. Två filer kommer att skrivas till micro SD-kortet: Bitcoin-core.sig & Bitcoin-core.txt. Sätt i micro SD-kortet i den dator där Bitcoin Core är installerat och öppna .txt-filen. Du kommer att se raden "För Wallet med huvudnyckelns fingeravtryck." Kontrollera att den åtta tecken långa XFP:n matchar den du noterade när du skapade din privata nyckel

Innan vi följer instruktionerna i filen börjar vi med att förbereda Wallet i Bitcoin Core Interface genom att följa dessa steg: gå till fliken Arkiv > Skapa en Wallet. Välj ett namn för din Wallet (utbytbar term med "porte-monnaie" i Core) och kontrollera alternativen Inaktivera privata nycklar, Skapa en tom Wallet och Wallet-descriptors enligt bilden nedan. Tryck sedan på knappen Create.


![create a wallet](assets/guide-agora/3.webp)


När Wallet har skapats i Bitcoin Core går du till fliken Fönster > Konsol och kontrollerar att den valda Wallet längst upp på sidan visar namnet på den du skapade.


I den .txt-fil som genererades av Coldcard tidigare kopierar du nu raden som börjar med importdescriptors och klistrar sedan in den i Bitcoin Core-konsolen. Ett svar som innehåller raden "success": true bör returneras.


![nodes window](assets/guide-agora/4.webp)


Om svaret innehåller "message": "Avståndsbeskrivare ska inte ha en etikett", radera posten "etikett": "Coldcard xxxx0000" i den kopierade raden från .txt-filen och klistra sedan in hela raden igen i Bitcoin Core-konsolen.


Om det behövs kan du hitta lite hjälp [här] (https://github.com/Coldcard/firmware/blob/master/docs/Bitcoin-core-usage.md) på Coldcard Github.


## Validering av Wallet-import i Bitcoin-kärnan


För att säkerställa att operationen var framgångsrik är det nödvändigt att validera att önskad Wallet har importerats till Bitcoin Core. En enkel metod för att bekräfta detta är att verifiera att de adresser som genereras i Coldcard motsvarar de adresser som genereras i Bitcoin Core.


Bitcoin Core: Mottagning > Skapa en ny mottagning Address

Coldcard: Address Explorer > Välj den Address som börjar med bc1q. Coldcard Address "bc1q" bör matcha den Address som visas i Bitcoin Core.

Mottagning och sändning av transaktioner i "air-gapped"-läge


Att ta emot en transaktion är extremt enkelt; tryck bara på Receive, märk transaktionen (valfritt men rekommenderas) och Skapa en ny mottagande Address. Sedan är allt som återstår att dela Address med avsändaren.


Det viktigaste elementet i denna Coldcard + Bitcoin Core-konfiguration är att skicka transaktioner utan att Coldcard och dess privata nyckel är anslutna till internet, en metod som kallas air-gapped som använder TBSP-funktionen (PSBT - Partiellt signerade Bitcoin-transaktioner) i Bitcoin.

I grund och botten använder vi Bitcoin Core Interface för att konstruera en transaktion, som vi sedan exporterar via micro SD-kortet till Coldcard för signering, och sedan returnerar den signerade transaktionsfilen till Bitcoin Core och sänder transaktionen till nätverket. Vi måste göra det på det här sättet eftersom Wallet som importeras till Bitcoin Core inte har en privat nyckel, bara den offentliga nyckeln (som gör att vi kan generate våra mottagaradresser), så det är omöjligt för oss att signera en transaktion direkt i programvaran för att spendera våra bitcoins.


Innan du fortsätter ska du kontrollera att följande alternativ är aktiverade i Inställningar > Wallet:



- Aktivera funktioner för myntkontroll
- Spendera obekräftade mynt (valfritt)
- Aktivera TBPS-kontroller


![option ](assets/guide-agora/5.webp)


### Steg för att skicka i luftgapat läge:


Skicka > Ingångar > välj önskad UTXO och ange sedan mottagarens Address i Betala till. Transaktionsavgift: Välj... > Anpassad > Ange transaktionsavgiften (Bitcoin Core beräknar i Sats/kilobyte istället för sat/byte som de flesta alternativa Wallet-lösningar. Så 4000 Sats/kilobyte = 4 Sats/byte). Skapa en osignerad transaktion > spara filen på ditt micro SD-kort och sätt in det i Coldcard.


På Coldcard trycker du på Klar att signera, verifierar transaktionsuppgifterna och trycker sedan på ✓ och sätter tillbaka micro SD-kortet i datorn när de signerade filerna har genererats.


Tillbaka i Bitcoin Core går du till fliken File > Load TBSP from file och anger den signerade transaktionsfilen .PSBT. PSBT Operations-rutan visas på skärmen och bekräftar att transaktionen är fullständigt signerad och redo att sändas ut. Allt som återstår är att trycka på Broadcast transaction.


![PSBT operations](assets/guide-agora/6.webp)


### Slutsats


Kombinationen av Coldcard-enheten med Bitcoin Core, som du kör din egen nod på, är kraftfull. Lägg därtill en privat nyckel som genereras med 100 tärningskast och en hemlig fras, och din Wallet-konfiguration blir en sofistikerad och robust fästning.


Kontakta oss gärna för att dela med dig av dina kommentarer och frågor! Vårt mål är att dela med oss av kunskap och öka vår förståelse dag för dag.