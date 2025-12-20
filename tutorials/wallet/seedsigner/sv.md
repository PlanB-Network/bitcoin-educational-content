---
name: SeedSigner
description: DIY, statslös, prisvärd och helt lufttät wallet-hårdvara
---

![cover](assets/cover.webp)



SeedSigner är en wallet Bitcoin-hårdvara med öppen källkod som vem som helst kan bygga själv med hjälp av billiga elektroniska komponenter för allmänt bruk. Till skillnad från kommersiella produkter som Ledger, Coldcard eller Trezor är det här inte en färdig enhet som tillverkas av ett företag: det är ett community-projekt som gör det möjligt för vem som helst att skapa sin egen enhet och kontrollera varje steg.



SeedSigner är utformad för att vara 100% ***air-gapped***: den ansluter aldrig till Internet, har ingen Wi-Fi eller Bluetooth (i fallet med Raspberry Pi Zero v1.3) och är aldrig ansluten till en dator för att utbyta data. Kommunikationen sker uteslutande via ett system för utbyte av QR-koder. Rent konkret visar din programvara för portföljhantering (t.ex. Sparrow Wallet) den transaktion som ska signeras i form av QR-koder; du skannar dem med SeedSigners kamera, sedan signerar enheten transaktionen med hjälp av dina privata nycklar som tillfälligt lagras i dess RAM-minne. Slutligen genererar den QR-koder som innehåller den signerade transaktionen, som du skannar med din programvara för att skicka den till Bitcoin-nätverket.



![Image](assets/fr/001.webp)



SeedSigner är också ***stateless***. Med andra ord sparar den inte dina seed eller dina privata nycklar permanent, till skillnad från andra hårdvaruplånböcker. Varje gång du startar om är minnet helt tomt, såvida du inte konfigurerar enheten så att dina inställningar sparas på ett microSD-kort. Du måste därför ange din seed på nytt varje gång du använder den, och den mest praktiska metoden är att lagra den i form av en QR-kod som skannas vid uppstart med SeedSigners kamera. Detta driftsätt minskar avsevärt attackytan: även om en tjuv stjäl din enhet kommer han inte att hitta någon information på den, eftersom den alltid är tom som standard.



Ett annat alternativ för att lagra din seed och använda den med SeedSigner är att använda ett *SeedKeeper* smartkort tillsammans med en kompatibel läsare. Detta ger dig ett mycket robust *Secure Element* för att lagra din seed, samtidigt som du använder SeedSigner-skärmen för att signera transaktioner. Men denna speciella konfiguration är föremål för en annan dedikerad handledning. Här kommer vi att koncentrera oss på den grundläggande användningen av SeedSigner:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

SeedSigner-projektet intar en viktig plats i Bitcoin-ekosystemet, eftersom det erbjuder alla, överallt i världen, möjligheten att dra nytta av avancerad säkerhet för att skydda sina bitcoins. Dess främsta fördel ligger i dess tillgänglighet: den hårdvara som krävs kan köpas för mindre än 50 dollar. Dessutom gör den det möjligt för människor som bor i länder med restriktioner att bygga sin egen wallet-hårdvara av vanliga datorkomponenter, som är lätta att hitta och mindre föremål för reglerande begränsningar.



Men även utanför dessa specifika sammanhang kan SeedSigner vara ett intressant alternativ för dig: det är öppen källkod, fungerar statslöst och airgapped och minskar attackvektorerna kopplade till leveranskedjan för din wallet-hårdvara.



## 1. Nödvändig utrustning



För att bygga din SeedSigner behöver du följande komponenter:





- Raspberry Pi Zero
    - Version 1.3 rekommenderas, eftersom den varken har Wi-Fi eller Bluetooth, vilket garanterar fullständig isolering.
 - Versionerna W och v2 är också kompatibla, men innehåller ett Wi-Fi/Bluetooth-chip. Det är därför lämpligt att fysiskt avaktivera det genom att ta bort radiomodulen från kortet. Operationen är relativt enkel, men kräver precision (en fin tång räcker för Zero W, medan en het penna behövs för v2 för att ta bort metallplattan som döljer modulen). Jag kommer inte att gå in på detaljerna i den här handledningen, men du hittar alla instruktioner i det här dokumentet: *[Inaktivera WiFi/Bluetooth med hårdvara](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Observera: vissa Raspberry Pi Zero-modeller säljs utan förlödda GPIO-stift. Du kan antingen köpa en version med integrerade stift direkt (enklaste lösningen), eller köpa stiften separat och löda dem själv (mer komplex lösning).
 - Glöm inte att inkludera en mikro-USB-strömförsörjning.



![Image](assets/fr/002.webp)





- Waveshare 1,3"-skärm (240×240 px)** (på franska)
    - Det är viktigt att välja just den här modellen: det finns andra liknande skärmar, men med en annan upplösning. Utan 240×240 px definition kommer skärmen att vara oanvändbar.
    - På skärmen finns tre knappar och en mini-joystick för användargränssnittet.



![Image](assets/fr/003.webp)





- Raspberry Pi Zero**-kompatibel kamera
    - Alternativ 1: standardkameran med en bred guldmatta (kontrollera kompatibiliteten med ditt hus).
    - Alternativ 2: den mer kompakta kameran "*Zero*", som är särskilt utformad för Pi Zero.



![Image](assets/fr/004.webp)





- MicroSD**-kort
    - Rekommenderad kapacitet: mellan 4 och 32 GB.





- Bostäder (frivilligt men rekommenderas)** (frivilligt men rekommenderas)** (frivilligt men rekommenderas)** (frivilligt men rekommenderas)** (frivilligt men rekommenderas)**)
    - Skyddar enheten och gör den enkel att använda.
    - Den mest populära modellen är "*Orange Pill Case*", för vilken [STL-filer med öppen källkod finns tillgängliga för 3D-utskrift](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Boxar finns också tillgängliga från [oberoende återförsäljare som är kopplade till projektet](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Du kan köpa dessa komponenter separat eller, för större enkelhet, välja färdiga paket som innehåller all nödvändig hårdvara. Personligen beställde jag mitt paket [på den här franska webbplatsen](https://bitcoinbazar.fr/), men du hittar också en lista över leverantörer för varje region i världen på [SeedSigner-projektets hårdvarusida](https://seedsigner.com/hardware/). Om du föredrar att köpa komponenterna individuellt finns de tillgängliga på de stora e-handelsplattformarna eller i specialbutiker.



## 2. Förbereda programvaran



När du har fått ihop din hårdvara måste du förbereda microSD-kortet genom att installera SeedSigner-systemet på det. För att göra detta, gå till din vardagliga persondator och anslut din microSD avsedd för SeedSigner.



### 2.1. Ladda ner



Gå till [projektets officiella GitHub-repository](https://github.com/SeedSigner/seedsigner/releases). För den senaste versionen av programvaran, ladda ner :




- Den `.img`-bild som motsvarar din Pi-modell.
- Filen `.sha256.txt`.
- Filen `.sha256.txt.sig`.



![Image](assets/fr/006.webp)



Innan vi påbörjar installationen ska vi kontrollera programvaran.



### 2.2 Verifiering under Linux och macOS



Börja med att importera den officiella offentliga nyckeln för SeedSigner-projektet direkt från Keybase :



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Terminalen bör tala om för dig att en nyckel har importerats eller uppdaterats. Kör sedan verifieringskommandot på signaturfilen (kom ihåg att ändra kommandot enligt din version, här `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Om allt är korrekt ska utmatningen vara `God signatur`. Det betyder att filen `.sha256.txt` har signerats med den nyckel som du just importerade och att signaturen är giltig. Ignorera varningsmeddelandet `WARNING: This key is not certified with a trusted signature`: detta är normalt, eftersom det nu är upp till dig att kontrollera att den nyckel som används tillhör SeedSigner-projektet.



För att göra detta jämför du de sista 16 tecknen i det fingeravtryck som visas med de som finns på [Keybase.io/SeedSigner](https://keybase.io/seedsigner), på deras [officiella Twitter](https://twitter.com/SeedSigner/status/1530555252373704707) eller i filen som publicerats på [SeedSigner.com](https://seedsigner.com/keybase.txt). Om dessa identifierare matchar exakt kan du vara säker på att nyckeln verkligen är projektets. Om du är osäker, sluta omedelbart och be SeedSigner-communityn (Telegram, X, GitHub ...) om hjälp.



När nyckeln har validerats kan du kontrollera att den nedladdade bilden inte har ändrats (kom ihåg att ändra kommandot enligt din version, här `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- Under Linux är det här kommandot inbyggt.
- Varning: macOS-versioner före `Big Sur (11)` känner inte igen alternativet `--ignore-missing`. I så fall ska du ta bort det och ignorera varningar om saknade filer.



Det förväntade resultatet är ett "OK" bredvid filen "img". Detta bekräftar att den uppladdade bilden är identisk med den som publicerats av projektet och inte har ändrats.



### 2.3 Verifiering av Windows



På Windows är proceduren liknande men kommandona är annorlunda. Börja med att installera [Gpg4win](https://www.gpg4win.org/) och öppna programmet *Kleopatra*. Importera den publika nyckeln för SeedSigner-projektet från URL Keybase :



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Öppna sedan PowerShell i den mapp där dina nedladdade filer finns (`Shift` + högerklicka > `Öppna PowerShell här`). Kör följande kommando för att kontrollera manifestsignaturen (kom ihåg att ändra kommandot enligt din version, här `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Om allt är korrekt ska utmatningen vara `God signatur`. Det betyder att filen `.sha256.txt` har signerats med den nyckel som du just importerade och att signaturen är giltig. Ignorera varningsmeddelandet `WARNING: This key is not certified with a trusted signature`: detta är normalt, eftersom det nu är upp till dig att kontrollera att den nyckel som används tillhör SeedSigner-projektet.



För att göra detta jämför du de sista 16 tecknen i det fingeravtryck som visas med de som finns på [Keybase.io/SeedSigner](https://keybase.io/seedsigner), på deras [officiella Twitter](https://twitter.com/SeedSigner/status/1530555252373704707) eller i filen som publicerats på [SeedSigner.com](https://seedsigner.com/keybase.txt). Om dessa identifierare matchar exakt kan du vara säker på att nyckeln verkligen är projektets. Om du är osäker, sluta omedelbart och be SeedSigner-communityn (Telegram, X, GitHub ...) om hjälp.



När nyckeln har validerats måste du kontrollera att bildfilen inte har korrumperats. För att göra detta använder du följande kommando i PowerShell :



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Exempel för en Raspberry Pi Zero 2 (kom ihåg att ändra kommandot enligt din version, här `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



PowerShell beräknar sedan SHA256-hashen för din bildfil. Jämför denna hash med motsvarande värde i `seedsigner.0.8.6.sha256.txt`.




- Om de två värdena är helt identiska är kontrollen framgångsrik och du kan fortsätta.
- Om de skiljer sig åt är filen skadad eller skadad. Använd den inte och starta nedladdningen igen.



![Image](assets/fr/013.webp)



En lyckad verifiering garanterar att din `.img`-fil är både autentisk (signerad av SeedSigner) och oförändrad (omodifierad). Du kan då tryggt gå vidare till nästa steg.



### 2.4. Flasha bilden



Om du inte redan har det, ladda ner programvaran [Balena Etcher](https://etcher.balena.io/), sedan :




- Sätt i microSD-kortet i din dator.
- Launch Etcher.
- Välj den nedladdade och verifierade filen `.img`.
- Välj microSD-kort som mål.
- Klicka på `Flash!`.



![Image](assets/fr/014.webp)



Vänta tills processen är klar: ditt microSD-kort är klart för användning. Nu är det dags för montering!



## 3. SeedSigner-montering



När ditt microSD-kort har förberetts och flasherats med SeedSigner-programvaran kan du fortsätta med slutmonteringen. Ta god tid på dig, eftersom vissa delar är ömtåliga (särskilt bordsduken, kameran och GPIO-stiften).



### 3.1 Förberedelse av höljet



Först av allt, öppna ditt fodral. Kontrollera att det är rent och att det inte finns några rester av 3D-printingplast i vägen för de invändiga fästelementen. Håll utkik efter :




- Kamerans placering (litet cirkulärt hål på framsidan).
- Öppningen för skärmen.
- Utskärningarna för Raspberry Pi Zeros mikro-USB-portar och microSD-kortplats.



### 3.2 Installation av kamera



Leta reda på kamerans bandkontakt på Raspberry Pi Zero: det är en tunn svart remsa på sidan av kortet, som kan lyftas något för att öppnas. Lyft upp den försiktigt, utan att tvinga den: den ska bara luta några millimeter.



![Image](assets/fr/015.webp)



Sätt i kamerahöljet. Den bruna/kopparfärgade delen ska vara vänd nedåt. Se till att den sitter ordentligt fast i kontakten, utan att vridas.



![Image](assets/fr/016.webp)



Stäng det svarta fältet för att låsa bordsduken (du kommer att känna ett litet klick). Kontrollera försiktigt att den sitter kvar på plats och inte rör sig.



![Image](assets/fr/017.webp)



Placera sedan kameramodulen i lämpligt hål i höljet. Beroende på modell kan den snäppas fast direkt eller kräva en liten självhäftande remsa för att hålla den på plats. Linsen måste vara perfekt inriktad och vänd utåt.



### 3.3 Installera Raspberry Pi Zero



Om du använder ett fodral ska du sätta in Raspberry Pi Zero-kortet i fodralet. Rikta försiktigt in portarna med de öppningar som finns.



Placera sedan Waveshare-displayen ovanpå Raspberry Pi Zero. Pi-enhetens GPIO-stift ska vara i perfekt linje med displayens honkontakt. Tryck långsamt fast skärmen på stiften, med ett jämnt tryck på varje sida för att undvika att de böjs.



![Image](assets/fr/018.webp)



Om du har ett fodral kan du slutföra monteringen genom att lägga till frontpanelen och joysticken.



Slutligen sätter du in microSD-kortet med den flashade programvaran i Raspberry Pi Zeros kantmonterade kortplats. Se till att det klickar på plats.



### 3.4 Första uppstarten



Anslut en mikro-USB-strömkabel till den dedikerade porten. Vänta ungefär en minut. SeedSigner-logotypen bör visas, följt av startskärmen.



![Image](assets/fr/019.webp)



Kontrollera till att börja med att de olika komponenterna fungerar som de ska genom att gå till menyn "Inställningar > I/O-test".



![Image](assets/fr/020.webp)



Testa alla knappar och se till att de reagerar korrekt. Klicka sedan på knappen `KEY1` för att kontrollera att kameran fungerar som förväntat. Detta kommer att ta en bild.



![Image](assets/fr/021.webp)



### 3.5 Justering av kameran



Beroende på hur du har monterat din SeedSigner kan det hända att kameran visar en inverterad bild. För att rätta till detta, gå till `Inställningar > Avancerat > Kamerarotation` och välj en 180° rotation om det behövs.



![Image](assets/fr/022.webp)



Om du har ändrat kamerans orientering eller vill ändra andra inställningar (t.ex. gränssnittsspråket) vid ett senare tillfälle måste du aktivera persistens av inställningar på microSD-kortet. Annars kommer dina inställningar att återgå till standardinställningarna varje gång du startar om, eftersom Raspberry Pi Zero inte har något permanent minne.



För att göra detta öppnar du menyn `Inställningar > Permanenta inställningar` och väljer sedan `Aktiverad`.



![Image](assets/fr/023.webp)



Om allt fungerar som det ska är din SeedSigner nu klar att användas!



## 4. SeedSigner inställningar



Innan du skapar din Bitcoin wallet, låt oss konfigurera SeedSigner. Eftersom den körs på en Raspberry Pi Zero utan permanent minne sparas dess inställningar inte automatiskt om du inte sparar dem på microSD-kortet. Se därför till att du har aktiverat det här alternativet, annars försvinner inställningarna vid omstart (se steg 3.5).



### 4.1 Åtkomst till parametermeny



Starta din SeedSigner och vänta på att startskärmen ska visas. Använd joysticken för att navigera till alternativet "Inställningar" och bekräfta sedan genom att trycka på mittknappen. Du kommer nu till huvudmenyn för inställningar.



![Image](assets/fr/024.webp)



### 4.2 Att välja programvara för portföljhantering



Gå sedan till menyn `Coordinator software`.



![Image](assets/fr/025.webp)



Med "koordinator" avses den programvara för portföljhantering som din SeedSigner kommunicerar med via QR-koder. Denna programvara installeras antingen på din dator eller på din smartphone. Det gör det möjligt för dig att hantera dina bitcoins, men utan att någonsin ha tillgång till dina privata nycklar. SeedSigner förblir den enda enhet som kan signera dina transaktioner.



Den aktuella firmwareversionen stöder flera program: Sparrow, Spectre, BlueWallet, Nunchuk och Keeper. I mitt fall använder jag **Sparrow Wallet**, som jag särskilt rekommenderar för dess enkelhet och rika funktionalitet.



Om du inte vet hur du installerar det kan du följa den här guiden:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Välj helt enkelt den programvara du vill ha i menyn.



![Image](assets/fr/026.webp)



### 4.3 Visning av enheter och belopp



I menyn `Denomination Display` kan du välja i vilken enhet beloppen ska visas:




- `BTC`
- mBTC` (milli-bitcoin, eller 0,001 BTC)
- gW-15 (satoshis, eller 1/100 000 000 BTC)



Enheten **sats** är i allmänhet den mest praktiska för små mängder.



![Image](assets/fr/027.webp)



### 4.4 Avancerade inställningar



Gå nu till menyn "Avancerat". Här hittar du flera användbara alternativ:




- gW-17 network`: ska endast ändras om du vill använda SeedSigner på Testnet.
- qR code density`: justerar mängden information som finns i varje QR-kod. Du kan behålla standardvärdet om du inte tycker att det är svårt att läsa när du skannar.
- xpub export: aktiverar eller inaktiverar export av din utökade publika nyckel (xpub, ypub, zpub) till programvara för portföljhantering via QR-kod (en funktion som vi kommer att använda senare, så låt den vara aktiverad tills vidare).
- `Script types`: definierar de skripttyper som tillåts för att låsa dina bitcoins. Du behöver inte ändra den här parametern, eftersom skripttypen kommer att ställas in direkt till Sparrow. Här berörs endast skript som SeedSigner är behörig att manipulera.



### 4.5 Val av språk



Slutligen kan du i menyn "Language" ändra gränssnittets språk så att det passar dina önskemål.



![Image](assets/fr/028.webp)



## 5. Skapa och spara seed



seed (eller den mnemoniska frasen) utgör grunden för din Bitcoin-portfölj. Den används för att härleda dina privata nycklar och adresser, och ger tillgång till dina medel. SeedSigner erbjuder flera metoder för att generera den, som vi kommer att titta på i det här avsnittet.



Innan vi börjar, några viktiga påminnelser:




- Denna fras ger full, obegränsad tillgång till alla dina bitcoins.** Den som har tillgång till denna fras kan stjäla dina pengar, även utan fysisk tillgång till din SeedSigner ;
- Vanligtvis används en fras på 12 ord för att återställa en wallet i händelse av förlust eller stöld av wallet-hårdvara. Men eftersom SeedSigner är en *stateless* enhet registrerar den aldrig din seed. Så dina fysiska säkerhetskopior är inte bara säkerhetskopior, utan ** det enda sättet att använda din wallet**. Om du förlorar dessa säkerhetskopior kommer dina bitcoins att gå förlorade permanent. Så säkerhetskopiera dem noggrant, på flera medier och på säkra platser;
- Om du precis har börjat rekommenderar jag starkt att du läser den här handledningen för att få en detaljerad förståelse för riskerna med att hantera en minnesfras :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Åtkomst till verktyget för skapande av seed



Från SeedSigners startskärm, gå till menyn "Verktyg".



![Image](assets/fr/029.webp)



Du kommer nu att generate din seed. En seed är helt enkelt ett stort slumpmässigt nummer. Ju mer slumpmässigt det genereras, desto säkrare är det. SeedSigner erbjuder två sätt att göra detta på:




- kamera": seed genereras från det visuella bruset i ett fotografi. Du tar en bild av en slumpmässig miljö (objekt, landskap, ansikte etc.) vars pixelvariationer används för att generate entropi. Det är en snabb metod, men inte reproducerbar.
- dice Rolls": man kastar tärning för att skapa den nödvändiga entropin. Det är mer tidskrävande, men reproducerbart och därför verifierbart. Om du väljer den här metoden ska du följa råden i den här handledningen (du behöver inte beräkna kontrollsumman här, SeedSigner tar hand om det):



https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Skapa seed med fotot



Om du väljer fotometoden klickar du på `Ny seed` (med kameraikonen), tar en bild och validerar. Välj sedan längden på din mening (12 eller 24 ord), som kommer att visas på skärmen för att sparas. Följande steg är identiska med del 5.3.



### 5.3 Skapa seed med tärningar



I denna handledning använder vi metoden **Tärningsrullar**. Klicka på `Ny seed` (med tärningsikonen).



![Image](assets/fr/030.webp)



Välj sedan längden på din mnemoniska fras. 12 ord erbjuder redan en tillräcklig säkerhetsnivå, så det är det val jag rekommenderar.



![Image](assets/fr/031.webp)



Slå tärningen och ange de resulterande siffrorna med hjälp av markören. Tryck på mittknappen för att validera varje post. Om du gör ett misstag kan du gå tillbaka. Använd flera olika tärningar för att minska påverkan av obalanserade tärningar. Se till att du inte blir iakttagen under spelets gång.



![Image](assets/fr/032.webp)



När du har angett dina 50 kast genererar SeedSigner din mening. **Följ instruktionerna i denna handledning noggrant om du precis har börjat:**



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Visa och spara seed



Skriv försiktigt ner orden i din minnesfras på ett lämpligt fysiskt underlag (papper eller metall).



![Image](assets/fr/033.webp)



### 5.5 Kontroll av säkerhetskopian



För att undvika fel i säkerhetskopieringen ber SeedSigner dig att verifiera din säkerhetskopia. Klicka på "Verifiera".



![Image](assets/fr/034.webp)



Ange sedan det önskade ordet enligt dess ordning i meningen. Här måste jag till exempel välja det tredje ordet i min mening.



![Image](assets/fr/035.webp)



Om du gör ett misstag kommer SeedSigner att informera dig, och du måste börja om igen och se till att notera din mnemoniska fras när den ges till dig. Detta verifieringssteg säkerställer att din säkerhetskopia är korrekt och fullständig. När den har validerats visas `Backup Verified` på skärmen.



![Image](assets/fr/036.webp)



För ett mer komplett restaureringstest, följ denna handledning :



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Förstå begreppet "statslös enhet



SeedSigner är en enhet utan permanent minne. Det innebär att din seed aldrig lagras inuti enheten (till skillnad från t.ex. en Ledger, Trezor eller Coldcard). Så snart du stänger av strömmen försvinner seed helt från dess RAM-minne. När du startar om SeedSigner återgår den till ett tomt tillstånd: du måste då ge den din seed igen, så att den kan signera dina transaktioner.



Detta ger ett viktigt skydd. Till skillnad från andra hårdvaruplånböcker är SeedSigner baserad på en Raspberry Pi Zero, som inte har något fysiskt skydd, inklusive *Secure Element*. Men eftersom inga känsliga data lagras skulle inte ens en fysiskt komprometterad enhet göra det möjligt för en angripare att extrahera dina privata nycklar eller spendera dina bitcoins.



Å andra sidan innebär denna arkitektur ett extra ansvar: utan en säkerhetskopia är dina pengar definitivt förlorade. Det är därför jag rekommenderar en **dubbel säkerhetskopia**. Du har redan din återställningsfras: det här är din huvudsakliga långsiktiga säkerhetskopia, som ska förvaras på ett säkert ställe. Nu ska vi skapa en kopia av den här frasen i form av **QR-kod**.



Varje gång du använder SeedSigner skannar du denna QR-kod med enhetens kamera så att den tillfälligt laddar dina seed i sitt minne medan du signerar dina transaktioner. Denna andra säkerhetskopia, som är avsedd för daglig användning, måste också förvaras med största försiktighet: alla som har denna QR-kod har full tillgång till dina bitcoins.


Jag råder dig också att lagra din QR-kod och din mnemoniska fras på två separata platser för att undvika att förlora allt i händelse av ett krav.



Ett mer avancerat och säkert alternativ är att använda SeedSigner med en **SeedKeeper**, som lagrar seed i en secure element. Om du vill veta mer kan du titta på den här handledningen:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Skriva huvudnyckel fingeravtryck



När verifieringen är klar visar SeedSigner fingeravtrycket från din wallet:s huvudnyckel. Detta fingeravtryck identifierar din wallet och säkerställer att du använder rätt återställningsfras i framtiden. Det avslöjar inte någon information om dina privata nycklar, så du kan säkert lagra det på ett digitalt medium. Se bara till att du har en tillgänglig kopia och att du aldrig tappar bort den.



![Image](assets/fr/037.webp)



Det är också i det här skedet som du kan lägga till en **passphrase BIP39** för att förstärka säkerheten för din wallet. Beroende på din backup-strategi kan det här alternativet vara värt det, men det medför också risker: om du förlorar passphrase kommer tillgången till dina bitcoins att förloras permanent.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Om du ännu inte är bekant med passphrase-konceptet inbjuder jag dig att läsa denna omfattande handledning i ämnet:



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 Spara seed i QR-format (*SeedQR*)



Med SeedSigner kan du konvertera din seed till en QR-kod i pappersformat, kallad *SeedQR*. Den här metoden förenklar omladdningen av din wallet, eftersom du slipper skriva in varje ord manuellt.



För att göra detta behöver du ett tomt papper eller en QR-kod i metall som motsvarar längden på din mnemoniska fras. Om du har köpt ett komplett paket för din SeedSigner ingår mallarna vanligtvis. Om inte, kan du ladda ner och skriva ut dem (eller reproducera dem för hand) här :




- [12-ordsformat](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [24 ords format](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Kompakt format 12 ord](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Kompakt format 24 ord](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Välj `Backup Seed` på din seed-skärm.



![Image](assets/fr/039.webp)



Välj sedan `Exportera som SeedQR`.



![Image](assets/fr/040.webp)



Välj sedan önskat format (normal eller kompakt) beroende på vilken pappersmall som finns tillgänglig.



![Image](assets/fr/041.webp)



Klicka på `Begin` för att börja skapa *SeedQR*. SeedSigner kommer sedan att visa en serie rutnät (A1, A2, B1, etc.), som var och en motsvarar en del av koden.



![Image](assets/fr/042.webp)



Återge noggrant varje svart punkt på ditt sparark och använd sedan joysticken för att gå vidare till nästa block. Ta god tid på dig: en enkel felinställning kan göra QR-koden oanvändbar.



Några tips:




- Börja med en blyertspenna så att du kan rätta till eventuella misstag, och gå sedan tillbaka till en fin svart penna när du är klar;
- En väl centrerad punkt i mitten av rutan är allt du behöver, du behöver inte fylla den helt.



![Image](assets/fr/043.webp)



Klicka sedan på `Confirm SeedQR`, och skanna din QR-kod för att kontrollera att den fungerar korrekt.



![Image](assets/fr/044.webp)



Om meddelandet `Success` visas är din *SeedQR* giltig: du kan gå vidare till nästa steg.



![Image](assets/fr/045.webp)



**Bevara detta ark lika strikt som din återställningsfras. Vem som helst som har denna QR-kod kan rekonstruera dina privata nycklar och stjäla dina bitcoins.**



Grattis, din Bitcoin-portfölj är nu igång och fungerar! Vi ska nu importera dess publika komponenter till **Sparrow Wallet** för att hantera den enkelt.



## 6. Importera wallet till Sparrow



När din SeedSigner har konfigurerats och din seed har genererats och sparats korrekt, är nästa steg att länka denna portfölj till förvaltningsprogram som Sparrow Wallet. Din seed kommer alltid att förbli offline, eftersom endast den publika delen av din portfölj kommer att överföras till Sparrow. Detta gör det möjligt för programvaran att visa dina adresser, transaktioner och bygga nya transaktioner, utan att någonsin kunna spendera dina bitcoins. För att spendera dina bitcoins måste din SeedSigner alltid signera den transaktion som förberetts av Sparrow.



### 6.1 Förberedelse av SeedSigner



Sätt i microSD-kortet som innehåller operativsystemet, slå på din SeedSigner och ladda sedan den seed som du just har skapat från din backup-QR-kod. Välj `Scan` på startskärmen och skanna sedan din SeedQR med SeedSigner.



![Image](assets/fr/046.webp)



Kontrollera att fingeravtrycket på din huvudnyckel matchar fingeravtrycket på din wallet. Om du använder en passphrase ska du ange den i detta skede.



![Image](assets/fr/047.webp)



Då kommer du till menyn för din portfölj, som i mitt fall heter `d4149b27`. Om du är tillbaka på startskärmen, välj `Seeds` och välj sedan det tryck som motsvarar din portfölj. Klicka sedan på `Export Xpub`.



![Image](assets/fr/048.webp)



Välj portföljtyp. I vårt fall är det en singelportfölj: välj `Single Sig`.



![Image](assets/fr/049.webp)



Därefter kommer valet av skriptstandard. Den senaste och mest ekonomiska när det gäller transaktionskostnader är `Taproot`. Jag råder dig därför att välja denna standard.



![Image](assets/fr/050.webp)



Ett varningsmeddelande kommer att visas. Detta är normalt: med denna utökade publika nyckel (`xpub`) kan du visa alla adresser som härrör från din seed (på det första kontot). Det tillåter dig inte att spendera dina pengar, men det avslöjar strukturen i din portfölj. Om det någonsin läcker ut är det ett problem för din integritet, men inte för säkerheten för dina bitcoins: det låter dig se dem, men inte spendera dem.



Klicka på "Jag förstår" och sedan på "Exportera Xpub" om du är nöjd med den information som visas.



SeedSigner genererar sedan din xpub i form av en dynamisk QR-kod som innehåller alla uppgifter du behöver för att hantera din portfölj i Sparrow Wallet.



![Image](assets/fr/051.webp)



Du kan använda joysticken för att justera skärmens ljusstyrka så att det blir lättare att läsa QR-koder.



### 6.2 Importera en ny portfölj till Sparrow Wallet



Se till att du har programvaran Sparrow Wallet installerad på din dator. Om du inte vet hur du laddar ner, kontrollerar och installerar den korrekt kan du läsa vår fullständiga handledning i ämnet:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Öppna Sparrow Wallet på datorn och klicka sedan på `Fil → Importera Wallet` i menyraden.



![Image](assets/fr/052.webp)



Bläddra ner till `SeedSigner` och välj sedan `Scan...`. Din webbkamera öppnas: skanna den dynamiska QR-koden som visas på din SeedSigner-skärm.



![Image](assets/fr/053.webp)



Tilldela ett namn till din portfölj och klicka sedan på `Create Wallet`. Sparrow kommer då att be dig att ställa in ett lösenord för att låsa lokal åtkomst till denna wallet. Välj ett starkt lösenord: det skyddar åtkomst till dina portföljdata i Sparrow (offentliga nycklar, adresser, etiketter och transaktionshistorik). Detta lösenord behövs inte för att återställa portföljen vid ett senare tillfälle: endast din mnemoniska fras (och eventuellt din passphrase) krävs för detta ändamål.



Jag rekommenderar att du sparar lösenordet i en lösenordshanterare så att du inte tappar bort det.



![Image](assets/fr/054.webp)



Din keystore har nu importerats framgångsrikt.



![Image](assets/fr/055.webp)



Kontrollera sedan att det `Master fingeravtryck` som visas i Sparrow överensstämmer med det som tidigare noterats i din SeedSigner.



Din SeedSigner och Sparrow Wallet är nu säkert sammankopplade. Sparrow fungerar som ett komplett hanteringsgränssnitt, medan SeedSigner förblir den enda enheten som kan signera dina transaktioner. Du är nu redo att ta emot och skicka bitcoins i en helt luftgapad konfiguration.



## 7. Ta emot och skicka bitcoins



Din SeedSigner och Sparrow Wallet är nu konfigurerade för att fungera tillsammans. I det här sista avsnittet tittar vi på hur du tar emot och skickar bitcoins med hjälp av den här konfigurationen.



### 7.1 Ta emot bitcoins



#### 7.1.1 Skapa en mottagningsadress



Öppna Sparrow Wallet på din dator och lås upp din SeedSigner wallet med hjälp av ditt lösenord. Kontrollera att programvaran är ansluten till en server (skåran längst ner till höger). I sidofältet klickar du på `Receive`.



![Image](assets/fr/056.webp)



En ny Bitcoin-adress visas. Du kommer att se :




- Textadressen (börjar med `bc1p...` om du använder P2TR som jag gör),
- Den motsvarande QR-koden,
- Ett "Label"-fält för att spåra dina transaktioner.



Jag rekommenderar starkt att du lägger till en etikett på varje bitcoin-kvitto på din wallet. Detta gör att du enkelt kan identifiera varifrån varje UTXO kommer och förbättra din integritetshantering. För att gå djupare in i detta viktiga ämne kan du kolla in den dedikerade utbildningen på Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

För att lägga till en etikett anger du bara ett namn i fältet "Etikett" och bekräftar sedan.



Till exempel:



```txt
Label : Sale of the Raspberry Pi Zero
```



Din adress är nu kopplad till denna etikett i alla Sparrow-avsnitt.



![Image](assets/fr/057.webp)



#### 7.1.2 Address-verifiering på SeedSigner



Innan du delar din mottagningsadress är det mycket viktigt att kontrollera att den tillhör din seed. Detta steg säkerställer att din SeedSigner kommer att kunna signera transaktioner som är associerade med denna adress. Det skyddar också mot eventuella attacker där Sparrow visar en bedräglig adress. Kom ihåg att Sparrow körs i en osäker miljö (din dator), som har en mycket större attackyta än din SeedSigner, som är helt isolerad. Därför bör du aldrig blint tro på de mottagningsadresser som presenteras på Sparrow förrän du har verifierat dem med din wallet-hårdvara.



På Sparrow, klicka på QR-koden för adressen för att förstora den: den kommer då att visas i helskärm.



![Image](assets/fr/058.webp)



På din SeedSigner, från huvudmenyn, välj `Scan`. Skanna QR-koden som visas på din datorskärm och välj sedan den seed som motsvarar din wallet (i mitt fall fingeravtrycket "d4149b27").



![Image](assets/fr/059.webp)



Om den skannade adressen matchar den som härrör från din seed, kommer SeedSigner-skärmen att visa meddelandet: `Address verifierad`.



![Image](assets/fr/060.webp)



Detta bekräftar att adressen tillhör din wallet och att du tryggt kan ta emot bitcoins från den.



#### 7.1.3 Mottagande av medel



Du kan nu kommunicera denna adress (i form av text eller QR-kod) till den person eller avdelning som behöver skicka dig satss. När transaktionen har sänts ut i nätverket kommer den att visas under fliken Transaktioner i Sparrow Wallet.



![Image](assets/fr/061.webp)



### 7.2 Skicka bitcoins



Att skicka bitcoins med en SeedSigner är en 3-stegsprocess:




- Skapande av transaktioner i Sparrow ;
- Underskrift av transaktionen på SeedSigner ;
- Slutlig distribution av transaktionen via Sparrow.



Alla utbyten mellan de två enheterna sker uteslutande med hjälp av QR-koder.



#### 7.2.1 Skapa en transaktion i Sparrow



I Sparrow Wallet kan du klicka på fliken `Sänd` i den vänstra sidofältet. Jag föredrar dock att använda fliken `UTXOs`, som låter dig öva "* Coin Control*". Den här metoden ger dig exakt kontroll över de UTXO:er som används, så att du kan kontrollera den information du avslöjar under transaktionen.



Välj de mynt du vill spendera på fliken `UTXOs` och klicka sedan på `Send Selected`.



![Image](assets/fr/062.webp)



Fyll sedan i transaktionsfälten:




- I `Pay to` klistrar du in mottagarens adress eller klickar på kameraikonen för att skanna QR-koden;
- I `Label`, lägg till en etikett för att spåra denna kostnad;
- I `Amount` anger du det belopp som ska skickas;
- Slutligen väljer du avgiftssats utifrån rådande marknadsförhållanden (uppskattningar finns på [mempool.space](https://mempool.space/)).



När fälten har fyllts i, kontrollera informationen noggrant och klicka sedan på `Create Transaction >>`.



![Image](assets/fr/063.webp)



Kontrollera transaktionsuppgifterna för att se till att allt är korrekt och klicka sedan på `Finalize Transaction for Signing`.



![Image](assets/fr/064.webp)



Transaktionen är nu klar, men ännu inte signerad. För att visa [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) som en QR-kod, klicka på "Visa QR".



![Image](assets/fr/065.webp)



#### 7.2.2 Signera transaktionen med SeedSigner



Slå på din SeedSigner och skanna din SeedQR för att komma åt din portfölj, som vanligt. Från startskärmen, välj `Scan` och skanna sedan QR-koden som visas på Sparrow.



![Image](assets/fr/066.webp)



Välj sedan seed för att matcha din portfölj.



![Image](assets/fr/067.webp)



SeedSigner upptäcker automatiskt att detta är en PSBT och visar en sammanfattning av transaktionen:




   - Det belopp som skickats,
   - Utgångsadresser,
   - Förknippade transaktionskostnader.



Klicka på `Review Details` och kontrollera noggrant all information direkt på SeedSigner-skärmen. Det viktigaste att kontrollera är det skickade beloppet, mottagarens adress och beloppet på de avgifter som har tagits ut.



![Image](assets/fr/068.webp)



Om allt är korrekt väljer du `Godkänn PSBT` för att signera transaktionen med motsvarande privata nyckel(n).



![Image](assets/fr/069.webp)



När den är signerad genererar SeedSigner en ny QR-kod som innehåller den signerade transaktionen, redo att skannas av Sparrow.



![Image](assets/fr/070.webp)



#### 7.2.3 Sändning av transaktionen från Sparrow



Nu när transaktionen är giltig måste den sändas ut i Bitcoin-nätverket så att den når en miner som lägger till den i ett block.



På Sparrow, klicka på `QR Scan`.



![Image](assets/fr/071.webp)



Presentera QR-koden som visas av din SeedSigner (den för den signerade transaktionen) för webbkameran. Sparrow kommer att avkoda signaturen och visa alla detaljer om transaktionen. Gör en sista kontroll av att all information är korrekt och klicka sedan på Broadcast Transaction för att sända den i Bitcoin-nätverket.



![Image](assets/fr/072.webp)



Din transaktion har nu skickats till Bitcoin-nätverket. Du kan följa dess framsteg på fliken `Transaktioner` i Sparrow Wallet.



![Image](assets/fr/073.webp)



Du har nu lärt dig grunderna i hur du använder SeedSigner. För att fördjupa dina kunskaper och utforska mer avancerade användningsområden, inbjuder jag dig att läsa följande handledning:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Du kan också stödja utvecklingen av SeedSigners öppen källkodsprojekt genom att göra en donation i bitcoins!](https://seedsigner.com/donate/)**



*Några av bilderna i den här handledningen kommer från [SeedSigner-projektets officiella webbplats](https://seedsigner.com/) och [GitHub-arkivet](https://github.com/SeedSigner/seedsigner).*