---
name: Nerdminer
description: Starta Mining Bitcoin med en chans att vinna nära 0
---

![cover](assets/cover.webp)

**Sätta upp din NerdMiner_v2**


I den här handledningen guidar vi dig genom de nödvändiga stegen för att ställa in en NerdMiner_v2, som är en hårdvaruenhet (en ESP-32 S3) avsedd för Bitcoin Mining.

Självklart kan inte datorkraften i en sådan enhet konkurrera med ASIC:erna hos amatörer eller professionella gruvarbetare. Ändå är NerdMiner ett perfekt utbildningsverktyg för att göra Bitcoin Mining påtagligt. Och vem vet, med (mycket) tur kanske du hittar ett block och den belöning som följer med det. För de nyfikna kommer vi att se i avsnittet [Uppskattning av sannolikheten att vinna](#uppskattning-av-la-sannolikhet-av-vinst). När det gäller strömförbrukning förbrukar en NerdMiner 0,5 W; som jämförelse förbrukar en LED-lampa i genomsnitt 20 gånger mer.


Innan vi går igenom de olika stegen, låt oss lista den nödvändiga utrustningen för att göra det:



- en [Lilygo T-display S3] (https://lilygo.cc/products/t-display-s3)
- en [USB-C-ström Supply] (https://amzn.eu/d/gIOot90)
- ett 3D-fodral: om du har en 3D-skrivare kan du ladda ner [3D-filen] (https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons), annars kan du köpa en i [Silexperience onlinebutik] (https://silexperience.company.site/NerdMiner_V2-p544379757).
- en PC med Chrome Browser installerad
- en internetanslutning
- a Bitcoin Address


Du kan också köpa ett färdigmonterat NerdMiner-kit från flera återförsäljare som t.ex:



- [DécouvreBitcoin](https://shop.decouvrebitcoin.com/products/nerd-Miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [BitMaker] (https://bitronics.store/shop/)


Först ska vi se hur man flashar programvaran till ESP-32 S3, och sedan ska vi se hur man startar om den för att ändra wifi-nätverket. Dessa steg är för Windows-användare, om du använder ett Linux OS, vänligen utför de [preliminära stegen] (#etapes-preliminaires-pour-utilisateurs-linux) för att tillåta igenkänning av ESP-32 S3 av ditt system.


**Installationen av NerdMiner_v2 Software** är mycket förenklad tack vare användningen av webflasher.


## Steg 1: Förberedelse av webbflasher


Först måste du gå till [online NM2 flasher] (https://bitmaker-hub.github.io/diyflasher/).


Välj sedan den firmware som motsvarar din ESP-32. För det mesta är det standardversionen: T-Display S3. Klicka sedan på "Flash".


**Note⚠️ :** är det viktigt att du använder webbläsaren Chrome - eftersom den som standard tillåter användning av flash och tillgång till dina USB-portar.


![image](assets/webflasher.webp)


## Steg 2: Ansluta ESP-32


När webflasher har startats öppnas ett popup-fönster som visar de olika USB-portar som webbläsaren känner igen.

Du kan sedan ansluta din ESP-32 och en ny port visas (i det här fallet är det ttyACM0-porten). Du måste då välja den och klicka på "connect".


![image](assets/flasher-port-serial.webp)


Programvaran laddas sedan ner till din ESP32 på några sekunder.


![image](assets/NM2-sucessfully-installed.webp)


## Steg 3: Konfiguration av NerdMiner


Konfigurationen av din NerdMiner görs via en smartphone eller en dator.

Aktivera WiFi och anslut till det lokala NerdMinerAP-nätverket. Om du använder en smartphone öppnas konfigurationsportalen automatiskt. Annars skriver du in Address 192.168.4.1 i en webbläsare.

Välj sedan "Konfigurera WiFi".


Du kan nu konfigurera din NerdMiner.

Börja med att ansluta till ditt WiFi-nätverk genom att välja nätverksnamn och ange det tillhörande lösenordet.


Sedan kan du välja den Mining pool du vill delta i. Det är faktiskt vanligt i Bitcoin Mining-industrin att samla datorkraft för att öka chanserna att hitta ett block i Exchange för att dela belöningen proportionellt mot den tillhandahållna Hashrate.

För NerdMiners kan du välja att ansluta till en av dessa pooler:


| Pool URL          | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Default Solo and open-source mining pool |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Maintained by CHMEX                      |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Maintained by djerfy                     |

När du har valt din pool måste du ange din Bitcoin Address för att få belöningen om (i undantagsfall) ett block hittas.


Välj också din tidszon så att NerdMiner kan visa tiden korrekt.

Du kan nu klicka på "spara".


![image](assets/wifi-configuration.webp)


Grattis, du är nu en del av Bitcoin Mining-nätverket!


## NerdMiner Drift


Programvaran NerdMinerv2 har 3 olika skärmar, som du kan komma åt genom att klicka på den övre knappen till höger på skärmen:



- Huvudskärmen ger tillgång till statistik för din NerdMiner.
- Den andra skärmen ger tillgång till tiden, din Hashrate, priset på Bitcoin och blockhöjden.
- Den tredje skärmen ger tillgång till statistik över det globala Bitcoin Mining-nätverket.

![image](assets/NM2-screens.webp)


Om du vill starta om din NerdMiner, t.ex. för att byta WiFi-nätverk, måste du trycka på den övre knappen i 5 sekunder.


Om du trycker en gång på den nedre knappen stängs NerdMiner av. Om du klickar två gånger roteras skärmens orientering.


### Preliminära steg för Linux-användare


Här är stegen för Chrome för att upptäcka din seriella port på Linux.


1. Identifiera den associerade porten:



- Anslut din ESP-32 till datorn.
- Öppna en terminal.
- Ange följande kommando för att lista alla portar:
  - `dmesg | grep tty`
  - eller `ls /dev/tty*`
- För att vara säker på porten kan du gå vidare genom att upprepa kommandot utan att ESP-32 är ansluten.


2. Ändra behörigheten för den associerade porten:



- Som standard kan åtkomst till serieportar kräva root-behörighet, så vi kommer att göra dem tillgängliga genom att lägga till din användare i gruppen `dialout`.
  - `sudo usermod -a -G dialout YOUR_USERNAME`, ersätt `YOUR_USERNAME` med ditt användarnamn.
  - logga sedan ut och logga in igen som den här användaren, eller starta om systemet för att se till att gruppändringarna träder i kraft.


Nu när ESP-32 känns igen av ditt system kan du gå tillbaka till [första steget](#etape-1-preparation-du-webflasher) för installation av programvaran.


## Slutsats


Och där har du det! Din NerdMiner_v2 är nu konfigurerad och redo att användas.


Grattis på Mining och må lyckan vara på din sida!


### Uppskattning av sannolikheten att vinna


Låt oss ha lite kul att uppskatta sannolikheten för att vinna en Block reward. Denna uppskattning kommer att vara grov och syftar endast till att få sannolikhetens storleksordning.

Poolen som en NerdMiner kan ansluta till är endast "solo Mining pool", vilket innebär att poolen inte delar ut Hashrate till alla anslutna miners utan endast fungerar som en samordnare.

Låt oss nu anta att vår NerdMiner har en Hashrate på cirka 45kH/s.


Med tanke på att den totala Hashrate är cirka 450 EH/s (eller 4,5 x 10^20 hash per sekund) kan vi anta att sannolikheten för att hitta nästa block är 1 på 100 miljoner miljarder, vilket är mycket mycket mycket osannolikt. Så förutom att vara ett pedagogiskt verktyg och ett föremål för nyfikenhet kan en NerdMiner fungera som en lotterilott i Bitcoin Mining till en marginell elektrisk kostnad på 0,5 W - men som vi just har sett är sannolikheten att vinna löjligt låg. Men varför inte utmana lyckan?


### Ytterligare information


Här är några länkar om du vill läsa mer om ämnet:



- [Projektsida för NerdMiner_v2] (http://github.com/BitMaker-hub/NerdMiner_v2)
- [Fullständig dokumentation av NerdMiners] (https://docs.bitwater.ch/nerd-Miner-v2/)