---
name: Specter DIY
description: Installationsguide för Spectre DIY
---

![cover](assets/cover.webp)


## Specter-DIY


> Cypherpunks skriver kod. Vi vet att någon måste skriva programvara för att försvara integriteten, och eftersom vi inte kan få integritet om vi inte alla gör det, kommer vi att skriva det.

*En Cypherpunk:s manifest - Eric Hughes - 9 mars 1993*


Tanken med projektet är att bygga en hårdvaru-wallet av komponenter som inte finns i hyllan.

Även om vi har ett förlängningskort som ger allt en snygg formfaktor och hjälper dig att undvika lödning, kommer vi att fortsätta att stödja och upprätthålla kompatibilitet med standardkomponenter.


![image](assets/fr/01.webp)


Vi vill också hålla projektet flexibelt så att det kan fungera på vilken annan uppsättning komponenter som helst med minimala ändringar. Du kanske vill göra en hårdvaru-wallet på en annan arkitektur (RISC-V?), med ett ljudmodem som kommunikationskanal - det ska du kunna göra. Det ska vara lätt att lägga till eller ändra funktionalitet i Specter och vi försöker abstrahera logiska moduler så mycket vi kan.


QR-koder är ett standardiserat sätt för Specter att kommunicera med värden. QR-koder är ganska praktiska och gör att användaren kan kontrollera dataöverföringen - varje QR-kod har en mycket begränsad kapacitet och kommunikationen sker enkelriktat. Och det är airgapped - du behöver inte ansluta wallet till datorn när som helst.


För lagring av hemligheter stöder vi agnostiskt läge (wallet glömmer alla hemligheter när den stängs av), hänsynslöst läge (lagrar hemligheter i flash i applikationens mikrokontroller) och secure element-integrering kommer snart.


Vårt huvudfokus är multisignaturinstallation med andra hårdvaruplånböcker, men wallet kan också fungera som en enda undertecknare. Vi försöker göra den kompatibel med Bitcoin Core där vi kan - PSBT för osignerade transaktioner, wallet-beskrivare för import/export av multisig-plånböcker. För att kommunicera med Bitcoin Core enklare arbetar vi också med [Specter Desktop app](https://github.com/cryptoadvance/specter-desktop) - en liten python flask server som pratar med din Bitcoin Core nod.


Det mesta av den inbyggda programvaran är skriven i MicroPython, vilket gör koden lätt att granska och ändra. Vi använder biblioteket [secp256k1](https://github.com/bitcoin-core/secp256k1) från Bitcoin Core för beräkningar av elliptiska kurvor och biblioteket [LittlevGL](https://lvgl.io/) för GUI.


## Ansvarsfriskrivning


Projektet har utvecklats så pass mycket att säkerhetsnivån för Specter-DIY nu är jämförbar med kommersiella hårdvaruplånböcker på marknaden. Vi har implementerat en säker bootloader som verifierar uppgraderingar av firmware, så att du kan vara säker på att endast signerad firmware kan laddas upp till enheten efter den första installationen. Till skillnad från kommersiella signeringsenheter måste dock bootloadern installeras manuellt av användaren och ställs inte in i fabriken av enhetsleverantören. Var därför extra uppmärksam under den första installationen av den fasta programvaran och se till att du verifierar PGP-signaturer och flashar den fasta programvaran från en säker dator.


Om något inte fungerar kan du öppna ett ärende här eller ställa en fråga i vår [Telegramgrupp](https://t.me/+VEinVSYkW5TUl5Ai).


## Inköpslista för Specter-DIY


Här beskriver vi vad du ska köpa, och i nästa del förklarar vi hur du monterar ihop det och några anteckningar om kortet - strömbyglar, USB-portar etc.


### Upptäcktstavla


Huvuddelen av enheten är utvecklarkortet:



- STM32F469I-DISCO-utvecklarkort (t.ex. från [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) eller [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Mini**USB-kabel
- Standard MicroUSB-kabel för kommunikation via USB


Valfritt men rekommenderas:


- [Waveshare QR code scanner](https://www.waveshare.com/barcode-scanner-module.htm) med långa stifthuvuden som [dessa](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) eller [dessa](https://www.amazon.com/gp/product/B015KA0RRU/) för att ansluta skannern till kortet (4 stifthuvuden behövs).


Vi arbetar för närvarande på ett förlängningskort som innehåller en smartkortplats, QR-kodläsare, batteri och ett 3d-tryckt fodral, men det innehåller inte huvuddelen - upptäcktskortet som du måste beställa separat. På så sätt är en attack mot leveranskedjan fortfarande inte ett problem eftersom de säkerhetskritiska komponenterna köps från en slumpmässig elektronikbutik.


Du kan börja använda Specter även utan några extra komponenter, men du kommer att kunna kommunicera med den via USB eller den inbyggda SD-kortplatsen. Om du använder Specter via USB innebär det att den inte är airgappad, vilket innebär att du förlorar en viktig säkerhetsegenskap.


### QR-skanner


För QR-kodläsare har du flera alternativ.


** Alternativ 1. Rekommenderad ** Resonably bra skanner från Waveshare (40 $)


[Waveshare scanner](https://www.waveshare.com/barcode-scanner-module.htm) - du måste hitta ett sätt att montera det snyggt, kanske använda någon form av Arduino Prototype-sköld och lite ducktape.


Ingen lödning krävs, men om du har lödningskunskaper kan du göra wallet mycket snyggare ;)


** Alternativ 2.** Mycket fin skanner från Mikroe men ganska dyr (150 $):


[Streckkodsklick](https://www.mikroe.com/barcode-click) + [Adapter](https://www.mikroe.com/arduino-uno-click-shield)


**Alternativ 3: Alla andra QR-skannrar


Du kan hitta några billiga skannrar i Kina. Deras kvalitet är ofta inte så bra, men du kan ta en chans. Kanske till och med ESPcamera skulle göra jobbet. Du behöver bara ansluta ström, UART (stift D0 och D1) och trigger till D5.


**Alternativ 4: Ingen skanner.


Då kan du bara använda Specter med USB / SD-kort.


Såvida du inte bygger en egen kommunikationsmodul som använder något annat istället för QR-koder - audiomodem, bluetooth eller vad som helst annat. Så snart den kan triggas och skicka data över seriell väg kan du göra vad du vill.


### Valfria komponenter


Om du lägger till en liten powerbank eller en batteri- och strömladdare/booster blir din wallet helt självförsörjande ;)



## Montering av Specter-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### Ansluta Waveshare Streckkodsläsare


wallet:s firmware konfigurerar skannern åt dig vid första körningen, så ingen manuell förkonfiguration krävs.


Så här ansluter du skannern till kortet:


![image](assets/fr/02.webp)


För enkelhetens skull kan du köpa en Arduino Protype-sköld och löda och montera allt på den (t.ex. [den här](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Energihantering


På ovansidan av kortet finns en jumper som definierar var den ska få ström. Du kan ändra jumperns position och välja strömkälla till en av USB-portarna eller VIN-pin och ansluta ett externt batteri där (bör vara 5V).


### Skåp för DIY


Kolla in mappen [enclosures](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures).


### Var kreativ!


Sätt ihop din egen Specter-DIY och skicka bilderna till oss (gör en pull request eller kontakta oss).


Kolla in [Gallery](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) med Specters som har sammanställts av communityn!




## Installera den kompilerade koden


Med den säkra bootloadern är den första installationen av den fasta programvaran något annorlunda. Uppgraderingar är enklare och kräver inte att hårdvaran wallet ansluts till datorn.


![video](https://youtu.be/eF4cgK_L6T4)


### Flashning av första firmware


**Note** Om du inte vill använda binärfiler från utgåvorna, kolla in [bootloader documentation](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md) som förklarar hur du kompilerar och konfigurerar den så att den använder dina offentliga nycklar istället för våra.



- Om du uppgraderar från versioner under `1.4.0` eller laddar upp den fasta programvaran för första gången, använd `initial_firmware_<version>.bin` från sidan [releases](https://github.com/cryptoadvance/specter-diy/releases).
 - Verifiera signaturen i filen `sha256.signed.txt` mot [Stepans PGP-nyckel](https://stepansnigirev.com/ss-specter-release.asc)
 - Verifiera hashen i filen `initial_firmware_<version>.bin` mot hashen som lagras i filen `sha256.signed.txt`
- Om du uppgraderar från en tom bootloader eller om du ser bootloader-felmeddelandet att den fasta programvaran inte är giltig, läs nästa avsnitt - Flasha signerad Specter-firmware.
- Kontrollera att strömbygeln på ditt discovery-kort är i STLK-läge
- Anslut discovery-kortet till din dator via **miniUSB**-kabeln på kortets ovansida.
    - Kortet bör visas som en flyttbar disk med namnet `DIS_F469NI`.
- Kopiera filen `initial_firmware_<version>.bin` till roten av filsystemet `DIS_F469NI`.
- När kortet är färdigt med att flasha den fasta programvaran återställer kortet sig självt och startar om till bootloader. Bootloader kontrollerar den fasta programvaran och startar i den fasta huvudprogramvaran. Om du ser ett felmeddelande om att ingen firmware hittas - följ uppdateringsinstruktionerna och ladda upp firmware via SD-kort.
- Nu kan du sätta strömbygeln där du vill ha den och driva kortet från powerbanken eller batteriet.


Flashning av första firmware via copy-paste av filen `.bin` misslyckas ibland - ofta på grund av kabeln, eller om du ansluter enheten via en USB-hubb. I det här fallet kan du försöka några gånger till (fungerar normalt i 2-3 försök).


Om det misslyckas hela tiden kan du använda [stlink](https://github.com/stlink-org/stlink/releases/latest) öppen källkodsverktyg. Installera det och skriv in i din terminal: `st-flash write <path/to/initial_firmare.bin> 0x8000000`. Det fungerar vanligtvis mycket mer tillförlitligt.


### Uppgradering av firmware



- Hämta `specter_upgrade_<version>.bin` från [releases](https://github.com/cryptoadvance/specter-diy/releases).
- Kopiera denna binärfil till roten på SD-kortet (FAT-formaterat, max 32 GB)
 - Kontrollera att endast en fil `specter_upgrade***.bin` finns i rotkatalogen
- Sätt i SD-kortet i SD-kortplatsen på discovery-kortet och slå på kortet
- Bootloader flashar den inbyggda programvaran och meddelar dig när det är klart.
- Starta om kortet - du kommer att se Specter-DIY-gränssnittet nu, det kommer att föreslå att du väljer din PIN-kod


När en ny version släpps är det bara att ladda ner `specter_upgrade_<version>.bin` från versionerna, släppa den till SD-kortet och uppgradera enheten precis som i föregående steg. Bootloader kommer att se till att endast signerad firmware kan laddas till kortet.


### Hur man tar reda på firmware-versionen


Gå till menyn `Enhetsinställningar` - där visas versionsnumret under titeln på skärmen.


## Använd Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Säkerhet för Specter-DIY


### Hårdvara


Displayen styrs av applikationens MCU.


Integrationen av säkra element har inte kommit så långt ännu - för närvarande lagras även hemligheter på huvud-MCU:n. Men du kan använda wallet utan att lagra hemligheten - du måste ange din återställningsfras varje gång. Varför ska man komma ihåg en lång passphrase om man kan komma ihåg hela mnemoniken?


Enheten använder extern flash för att lagra vissa filer (QSPI), men alla användarfiler signeras av wallet och kontrolleras när de laddas.


QR-skanningsfunktionen ligger på en separat mikrokontroller, så all bildbehandling sker utanför den säkerhetskritiska MCU:n. För närvarande hanteras USB och SD-kort fortfarande av huvud-MCU:n, så använd inte SD-kort och USB om du vill minska attackytan.


### PIN-skydd (autentisering av användare)


Under den första uppstarten genereras en unik hemlighet på huvud-MCU:n. Med hjälp av denna hemlighet kan du verifiera att enheten inte har ersatts av en skadlig enhet - när du anger PIN-koden ser du en lista med ord som förblir desamma så länge hemligheten finns kvar.


Din PIN-kod tillsammans med denna unika hemlighet används för att generate en dekrypteringsnyckel för dina Bitcoin nycklar (om du lagrar dem). Så om angriparen skulle kunna kringgå PIN-skärmen kommer dekrypteringen ändå att misslyckas.


Om du har låst firmware (TODO: lägg till instruktionslänk här) kommer det effektivt att låsa hemligheten också, så om angriparen flashar en annan firmware till kortet raderas hemligheten och du kommer att kunna känna igen den när du börjar ange PIN-koden - ordsekvensen kommer att vara annorlunda.


### Generering av återställningsfrasen


Detta är en av de viktigaste delarna av wallet - att generate nyckeln på ett säkert sätt. För att göra detta på ett bra sätt använder vi flera entropikällor:



- Mikrokontrollerns TRNG. Proprietär, certifierad och förmodligen bra men vi litar inte på den
- Pekskärm. Varje gång du trycker på skärmen mäter vi positionen och ögonblicket när denna beröring inträffade (i mikrokontroller tickar på 180MHz).
- Inbyggda mikrofoner - inte ännu. Kortet har två mikrofoner, så att hårdvaran wallet kan lyssna på dig och blanda in dessa data i entropipoolen.


All denna entropi hashas ihop och konverteras till din återställningsfras. Den resulterande entropin är alltid bättre än någon av de enskilda källorna.


### Logik på hög nivå - plånböcker


Specter fungerar som en nyckellagring. Den innehåller privata HD-nycklar som kan ingå i plånböcker. Plånböckerna definieras av sina deskriptorer. Vi stöder även miniscript.


Varje wallet hör till ett visst nätverk. Det innebär att om du importerar en wallet på `testnet` kommer den inte att vara tillgänglig på `mainnet` eller `regtest` - du måste byta till det här nätverket och importera wallet separat.


### Verifiering av transaktioner


Följande regler gäller för transaktioner som wallet kommer att underteckna:



- om blandade inmatningar från olika plånböcker hittas varnas användaren ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- change-utgångar visar namnet på den wallet som de skickas till
- för att använda en multisig eller miniscript måste du först importera wallet genom att lägga till wallet descriptor (via QR, USB eller SD-kort)


## Stöd för deskriptorer


Alla normala Bitcoin-descriptorer fungerar. Bortsett från det har vi några tillägg:


### Flera grenar i deskriptorer


För att spara utrymme i QR-koderna tillåter vi att du lägger till beskrivningar med flera grenar på en gång. Om du vill använda `wpkh(xpub/0/*)` för mottagningsadresser och `wpkh(xpub/1/*)` för ändringsadresser kan du kombinera dem i en enda deskriptor: `wpkh(xpub/{0,1}/*)` - wallet kommer att behandla det första indexet i `{}`-uppsättningsdelen som gren för mottagningsadresser och det andra som ändringsadresser.


Du kan också ange fler än två grenar, och grenindex kan vara olika för olika cosigners, så den här beskrivningen är mycket konstig men helt giltig:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


För att ta emot adress nummer 17 kommer wallet att använda skriptet från `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))`.


Det enda kravet är att antalet index i alla uppsättningar är detsamma (3 i fallet ovan).


### Standardavledningar


Om deskriptorn innehåller publika huvudnycklar men inte innehåller jokerteckenavledningar läggs standardavledningen `/{0,1}/*` till alla utökade nycklar i deskriptorn. Om minst en av xpubarna har en jokerteckenavledning ändras inte beskrivningen.


Deskriptorn `wpkh(xpub)` kommer att konverteras till `wpkh(xpub/{0,1}/*)`.


### Miniscript


Specter stöder miniscript, men stöder inte kompilering av policy-till-miniscript (eftersom det är alldeles för dyrt). Vi utför vissa kontroller på miniscriptet, så att endast `B`-skript tillåts på den översta nivån och alla argument i underminiscript måste ha egenskaper enligt [spec](http://bitcoin.sipa.be/miniscript/).


Du kan använda [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) för att generate en deskriptor från en policy och sedan importera den till wallet.


Till exempel kan en policy "Jag kan spendera nu, eller om 100 dagar kan min fru spendera" omvandlas till wallet på följande sätt:


Policy: `eller(9@pk(xpubA),and(older(14400),pk(B)))` (min nyckel är 9 gånger mer sannolik)


Miniscript: `eller_d(pk(xpubA),och_v(v:pkh(xpubB),äldre(14400)))`


Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))``


Eftersom vi inte har några jokertecken för avledningar kommer standardavledningarna `/{0,1}/*` att läggas till i xpubarna.



---

MIT-licens


Upphovsrätt (c) 2019 cryptoadvance


---