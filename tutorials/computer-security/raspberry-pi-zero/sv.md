---
name: Raspberry Pi Zero
description: Hur man bygger en minimal, isolerad och lågkostnadsdator med en Raspberry Pi Zero och ett tillbehörskit.
---
![cover](assets/cover.webp)



Om du har varit på sidorna i Plan ₿ Network ett tag har du redan lärt dig att en av de mest förespråkade säkerhetsinställningarna, nästan ett måste, ** är förvaltningen av medel genom offline-lagring av dina privata nycklar **.



Om du inte har upptäckt det ännu hittar du i den här handledningen länkar till resurser med öppen källkod som du kan använda för att lära dig mer om det.



För att hantera privata nycklar offline krävs därför en enhet som är permanent frånkopplad från nätverket, antingen en [hårdvaruplånbok](https://planb.network/resources/glossary/hardware-wallet) eller en airgap-dator, avsedd för denna specifika funktion.



Hur gör man om man t.ex. inte har möjlighet att köpa in hårdvara som bara utför denna uppgift, men man inte vill ge upp detta säkerhetssteg?



## Lösningen


Vad händer om jag säger att du kan göra en offline-enhet i form av en luftgapsdator som är lika stor och tung som ett USB-minne och kostar 35 euro? Skulle du inte tro på det?



Fortsätt läsa.



Jag ska säga dig mer: läs hela vägen igenom. Den föreslagna lösningen är billig, men den är inte precis den enklaste. Först får du den allmänna idén, sedan bestämmer du dig för att investera lite av din tid i lite personlig forskning och väljer, med så mycket sinnesfrid som möjligt, om och hur du ska gå vidare.



## Krav och önskemål


**1** En [Raspberry PI Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/): PI Zero (utan något suffix) är grunden för att bygga en dator med minimal prestanda, men saknar framför allt Wi-Fi- och Bluetooth-kort, krav som är oumbärliga för syftet med denna övning.





- Kostnad**: ca 15,00 vid tidpunkten för skrivandet av denna handledning (augusti 2025).
- Kontinuitet i produktionen**: Raspberry garanterar produktion fram till januari 2030.



PI Zero utan Wi-Fi och Bluetooth har tyvärr blivit praktiskt taget otillgängliga. Du kanske kan hitta PI Zero W- och PI Zero 2W-alternativen lättare. I det här fallet kan du inaktivera anslutningsfunktionerna genom att ändra konfigurationsfilen. När du har installerat operativsystemet måste du lägga till dessa objekt i config:



```
dtoverlay=disable-wifi
dtoverlay=disable-bt
```



ett avsnitt i den här guiden visar dig hur och var du ska göra det. Men om du verkligen vill vara säker kan du hitta flera handledning på webben för att ta bort Wi-Fi-chipet med en liten skärare, den typ som är lämplig för att arbeta på elektroniska kort.



**2** Ett _startkit_ för Raspberry PI Zero: som brukligt är i Raspberry-världen, med bara ben, utan externt hölje. Dessutom begränsar de begränsade resurserna för ett sådant litet kort möjligheterna till anslutning till omvärlden.



När jag bestämde mig för att gå vidare hittade jag [det här kitet](https://www.amazon.it/-/en/GeeekPi-Raspberry-Aluminum-Passive-Heatsink/dp/B0BJ1WWHGF?crid=1NAFFVHG3IFBU&sprefix=raspberry+pi+zero+kit+geeek+pi%2Caps%2C88&sr=8-65) fullt av tillbehör, för att dra full nytta av PI Zeros fulla potential. Faktum är att kitet innehåller en USB A -> micro USB power Supply, en liten USB-hubb, en mini-HDMI -> HDMI-adapter, en kylfläns i koppar och ett ytterhölje i aluminium. I kitet ingår också de skruvar och den insexnyckel som behövs för att sätta PI Zero i det nya höljet.





- Kostnad**: 19.99 euro.



**3** Denna handledning kräver inte att du spenderar stora budgetar på airgap-datorn. Du bör dock veta att du kommer att behöva ett USB-tangentbord och en mus (endast trådbundna, undvik Bluetooth) och en bildskärm. Beroende på ingången till din bildskärm kan du behöva en adapter från mini-HDMI, den enda tillgängliga utgången på PI Zero. Slutligen, se Hard för det faktum att vi alla har ett icke-trådlöst tangentbord och mus i huset någonstans - det är dags att Dust dem av.



## Extra budget



**4** Du kan få den ursprungliga strömmen Supply från Raspberry, som kostar cirka 15,00 euro.



**5** Själv valde jag att använda strömmen Supply som medföljer i _startpaketet_, men kombinerade den med en USBA → miniUSB så kallad `no data`-kabel, som kostar 3,70 euro.



**6** Ett micro SD-kort med minst 32 GB lagringsutrymme; om det är av industriell kvalitet/nivå är det bättre.



**7** Du behöver ett system, en USB till micro SD-adapter, som den du ser på bilden. Operativsystemet och minnet i din PI Zero kommer att fungera på det mediet.



![img](assets/it/06.webp)



## Installation av operativsystemet


Innan du stänger in din PI Zero i lådan rekommenderar jag att du installerar operativsystemet. Du kommer då att kunna kontrollera lysdioden som indikerar drift direkt.



För att välja och bränna operativsystemet valde jag det enklaste sättet: att använda Raspberrys `PI Imager`-verktyg.



![img](assets/it/01.webp)



Gå därför till [Raspberry Github](https://github.com/raspberrypi/rpi-imager/releases) för att ladda ner den senaste versionen av Imager och välj den som passar bäst för ditt operativsystem (v. 1.9.6 vid skrivtillfället). Du kommer att märka att bredvid varje fil finns även hash-värdet för motsvarande fil. Detta blir användbart för verifiering.



![img](assets/it/02.webp)



Jag rekommenderar att du verifierar det operativsystem som du kommer att använda på din airgap-dator, för din egen personliga sinnesfrid. På så sätt kan du vara säker på att du arbetar med en legitim (inte skadlig) version av Imager och därmed Raspi OS.



Gör verifieringen omedelbart efter nedladdningen, med den maskin du normalt använder ansluten till Internet



Öppna sedan Linux-terminalen och förbered nedladdningen genom att skapa en `raspios`-katalog som är användbar för att arbeta med den.



![img](assets/it/19.webp)



Ladda ner Imager för din Linux-distribution med `wget`.



![img](assets/it/20.webp)



Slutligen kör du kommandot `sha256sum` och jämför Hash med den som Raspberry tillhandahåller i sin Github.



![img](assets/it/21.webp)



Om du har Windows kan du öppna Power Shell och skriva följande kommando:



```
Get-FileHash -Path <yourpath>\imager-1.9.6.exe
```



![img](assets/it/04.webp)



Du kommer att få Hash som måste matcha den som publiceras på Raspberry Github.



När du har verifierat nedladdningen kan du installera Imager på din dagliga dator och öppna den. Imager är det verktyg du behöver för att bränna operativsystemet till micro SD, som kommer att vara "systemdisken" i PI Zero.



Processen är extremt enkel: välj först den Raspberry-enhet du ska använda (så var uppmärksam på **din modell** av Raspi Zero), sedan OS-versionen och slutligen monteringspunkten för det micro SD-kort som du ska flasha operativsystemet till.



### Första steget



![img](assets/it/03.webp)



### Andra steget



![img](assets/it/07.webp)



**Observera väl**: välj `PI OS 32-bit`, det är det enda som fungerar med PI Zero.



### Tredje steget



![img](assets/it/08.webp)



(Var mycket noga med att lämna _Exclude System Drive_ markerad för att undvika att bli ombedd att installera Raspis operativsystem på din dator)



När allt är klart frågar Imager dig om du vill använda anpassade inställningar. Välj vad du vill, eller klicka på _No_ för att fortsätta med standardalternativen.



![img](assets/it/09.webp)



Bekräfta att du vill radera innehållet på micro SD-kortet



![img](assets/it/10.webp)



Imager börjar flasha operativsystemet till micro SD-kortet, och en rullningslist visar hur långt överföringen har kommit.



![img](assets/it/11.webp)



I slutet finns det automatisk verifiering, jag råder dig att inte stoppa den.



![img](assets/it/12.webp)



Slutligen visas ett meddelande på skärmen, och om allt gick bra ser det ut som på bilden.



![img](assets/it/13.webp)



Nu kan du verkligen ta bort microSD-kortet från läsaren och sätta det i PI Zero-sloten. Starta den lilla Raspberry och observera LED-lampan: vi förväntar oss att den är grön och blinkar, vilket indikerar normal inläsning av operativsystemet, för att sedan förbli tänd kontinuerligt. Om du har andra indikationer, till exempel om LED-lampan blinkar regelbundet eller är röd, se FAQ eller [supportsidorna i forumet](https://forums.raspberrypi.com/).



## Första konfigurationen


Den första uppstarten av Raspi OS är lite långsammare än vanligt eftersom den måste utföra ett antal faktiska installationsuppgifter. Men om allt har gått bra kommer du att se en välkomstskärm.



![img](assets/it/14.webp)



Klicka på _Next_ för att ställa in den geografiska regionen, särskilt för att ladda rätt tangentbord. Var särskilt uppmärksam på det sistnämnda.



![img](assets/it/15.webp)



Klicka på _Nästa_ och du kommer att bli ombedd att skapa din användare, skriv ner dina inloggningsuppgifter och spara dem väl.



![img](assets/it/16.webp)



Guiden ber dig att välja en standardwebbläsare, mellan Chromium och Firefox; den kan också fråga dig om Wi-Fi-nätverksinställningar om du arbetar med en Zero W eller 2W PI. Fortsätt och klicka på _Skip_.



Vid något tillfälle kommer du att bli uppmanad att uppgradera den inbyggda programvaran och operativsystemet. Välj _Skip_: i den här övningen bygger vi faktiskt en offline-maskin, som måste förbli offline från och med nu.



Slutligen kan du bli ombedd att aktivera `ssh`, men avböj även detta steg eftersom det är en IP med noll luftgap.



![img](assets/it/17.webp)



Det finns inte mycket mer att konfigurera. När du är klar startar du om Raspberry för att ändringarna ska börja gälla.



![img](assets/it/18.webp)



## En ny dator Airgap


Efter omstart är din nya airgap-dator klar. PI Zero visar dig det nya skrivbordet, som du kan arbeta med antingen via GUI eller från kommandoraden.



![img](assets/it/22.webp)



### Första stegen för PI Zero W eller 2W


Om du arbetar med en Raspberry PI Zero W- eller 2W-serie har ditt kort chip för Wi-Fi och Bluetooth ombord. Under den första installationen hoppade du över anslutningskonfigurationen, så PI Zero är inte ansluten till Internet. Nu kan du inaktivera de två chipen permanent via programvara.



Faktum är att Raspi OS tillhandahåller en `config.txt`-fil som du kan redigera efter eget tycke och smak. Filen `config` ligger på `boot`-partitionen i katalogen `firmware` och du kan redigera och spara den med `root`-rättigheter.



Öppna terminalen från ikonen längst upp till vänster och den blir `root`.(1)



![img](assets/it/23.webp)



(1) Om du inte skapade lösenordet för `root` i Raspi OS under de föregående stegen, rekommenderar jag att du gör det nu med kommandot `passwd`. Att ha `root`-användaren oberoende av din personliga användare kan visa sig vara mycket praktiskt i återställningssituationer.



Leta efter filen `config.txt` i terminalen och var beredd att redigera den med redigeringsprogrammet `nano`.



![img](assets/it/24.webp)



Redigeringen ska göras längst ner i hela `config`, efter orden `[All]`. Det är vid denna punkt som du lägger till kommandona `dtoverlay` som visades i början av handledningen.



![img](assets/it/25.webp)



Spara, stäng och starta om. I följande steg kommer vi att utforska den lilla Raspberry.



## Vad kan man förvänta sig av denna enhet?


Enligt de [tekniska specifikationerna](https://www.raspberrypi.com/products/raspberry-pi-zero/) på Raspberrys webbplats har PI Zero en BCM2835-processor med en kärna och 512 MB RAM, och verkar därför inte särskilt kraftfull.



Eftersom terminalen är lättare kommer vi att använda kommandoraden för att utforska systemkonfigurationer.



När du slår på strömmen kommer du att se en kort regnbågsfärgad skärm, följt av ett välkomstmeddelande från Raspberry och, i det nedre vänstra hörnet, kernelmeddelanden relaterade till uppstart.



När PI OS-skrivbordet visas öppnar du terminalen och skriver:



```bash
uname -a
```


Detta kommando visar den kärnversion som för närvarande används på skärmen, plus annan information.



![img](assets/it/26.webp)



Du kan också se information om CPU och maskinvara genom att skriva:



```bash
lscpu
```



![img](assets/it/27.webp)



Och se även `proc/mem/info`.



![img](assets/it/28.webp)



För att ta reda på versionen av Debian och utgivningens kodnamn:



``` bash


lsb_release -a


```

![img](assets/it/29.webp)

Infine, due comandi per controllare la memoria di massa e i dischi:

``` bash
fdisk -l
```



![img](assets/it/31.webp)



``` bash


df


```
![img](assets/it/30.webp)

Per controllare come lavora la CPU:

``` bash
top
```



![img](assets/it/32.webp)



## Användning


Även om prestandan verkar begränsad (på papperet och jämfört med kraften i dagens maskiner) är PI Zero mycket högpresterande, särskilt som terminal.





- Först kan du gå till huvudmenyerna och låta dig inspireras av panelen _Add/Remove software_, där du hittar ett antal verktyg för att programmera och öva. Kom ihåg att du också kan göra detta från terminalen, men alltid med `root`-behörighet.



![img](assets/it/33.webp)





- Du kan "adoptera" denna offline-enhet för att lagra en mängd konfidentiella dokument, som kommer att vara tillgängliga när det behövs, utan att någonsin exponeras för Internet.
- Du kan använda den här konfigurationen för att generate dina GPG-nycklar på ett säkert sätt.
- Du skulle till och med kunna använda denna nya "leksak" som en airgap-signaturenhet, [genom att följa råden från Arman The Parman](https://armantheparman.medium.com/how-to-set-up-a-raspberry-pi-zero-air-gapped-running-latest-version-of-electrum-desktop-wallet-85e59ecaddc0).



Bland de plånböcker som jag känner till är Electrum den enda som tillhandahåller en 32-bitarsversion. Tja: Zero IP som vi förberedde det i den här handledningen skulle låta dig hålla de privata nycklarna offline inställningen för Wallet luftgap som vi täckte i den här handledningen:



https://planb.network/tutorials/wallet/desktop/electrum-airgap-62b5a4c6-a221-4d41-9a62-4618c53d8223

## Slutsatser


Upplägget har förmodligen en stor svaghet: micro SD är ett medium som kan ge problem. Det är sårbart för tung användning; kanske har du redan erfarenhet av detta, från att ha använt det med din telefon. Efter att ha installerat all programvara som du vill använda på Zero airgap IP, gör du en bra säkerhetskopia av den värdefulla micro SD, med hjälp av Raspi OS-verktyget som du har tillgängligt.



![img](assets/it/34.webp)



I takt med att dina behov växer, och med dem dina budgetmöjligheter, kan du utforska andra Raspberry eller liknande lösningar. På tal om minne, till exempel, erbjuder PI 5 möjligheten att montera en M2 NVME-enhet, som verkligen är mer robust än microSD.



Glöm inte att göra anteckningar och dokumentera varje steg i installationen av programvaran som du ska använda offline. **Förr eller senare kommer ett uppdaterat Raspi OS ut** som du definitivt kommer att vilja dra nytta av. Vid den tidpunkten måste du radera allt och göra allt om igen (kanske med en ny micro SD 😂).



Den övning vi just gjorde, förutsatt att det är ditt första experiment också, kommer du att komma ihåg länge. Det är inte alltid möjligt att ägna hårdvara åt `inbäddade` operationer offline, utan att försumma uppmärksamheten på en airgapped maskin att slå på och kontrollera då och då.



Du fick det gjort, men grattis! Och du kommer att kunna föreslå den här lösningen till alla dem som behöver hålla nere sina budgetar.