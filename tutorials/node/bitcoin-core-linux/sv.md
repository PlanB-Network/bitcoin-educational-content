---
name: Bitcoin Core (Linux)
description: Kör din egen nod med Bitcoin core på Linux
---

![cover](assets/cover.webp)


## Kör din egen nod med Bitcoin core


Introduktion till Bitcoin och konceptet med en nod, kompletterat med en omfattande installationsguide för Linux.


En av de mest spännande aspekterna av Bitcoin är möjligheten att köra programmet själv och därmed delta på detaljnivå i nätverket och verifieringen av den offentliga transaktionen Ledger.


Bitcoin, som är ett projekt med öppen källkod, har varit fritt tillgängligt och distribuerats offentligt sedan 2009. Nästan 17 år efter starten är Bitcoin nu ett robust och ostoppbart digitalt monetärt nätverk som drar nytta av en kraftfull organisk nätverkseffekt. För sina ansträngningar och visioner förtjänar Satoshi Nakamoto vår tacksamhet. Förresten, vi är värd för Bitcoin whitepaper här på Agora 256 (notera: även på universitetet).


### Bli din egen bank


Att driva en egen nod har blivit viktigt för anhängare av Bitcoin-etoset. Utan att be om någons tillstånd är det möjligt att ladda ner Blockchain från början och därmed verifiera alla transaktioner från A till Ö enligt Bitcoin-protokollet.


Programmet innehåller också sin egen Wallet. På så sätt har vi kontroll över de transaktioner vi skickar till resten av nätverket, utan någon mellanhand eller tredje part. Du är din egen bank.


Resten av den här artikeln är därför en guide för att installera Bitcoin core - den mest använda Bitcoin-programvaruversionen - specifikt på Debian-kompatibla Linux-distributioner som Ubuntu och Pop!OS. Följ den här guiden för att ta ett steg närmare din individuella suveränitet.


## Bitcoin core Installationsguide för Debian/Ubuntu


**Förkunskaper**


- Minst 6 GB datalagring (pruned-nod) - 1 TB datalagring (Full node)
- Räkna med att *Initial Block Download* (IBD) tar minst 24 timmar. Denna operation är obligatorisk även för en pruned-nod.
- Tillåt ~600 GB bandbredd för IBD, även för en pruned-nod.


** Notera: 💡** följande kommandon är fördefinierade för Bitcoin core version 24.1.


### Ladda ner och verifiera filer



- [Download](https://bitcoincore.org/en/download/) `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, samt filerna `SHA256SUMS` och `SHA256SUMS.asc` (du måste naturligtvis ladda ner den senaste versionen av programvaran).



- Öppna en terminal i den katalog där de nedladdade filerna finns. Exempel: `cd ~/Downloads/`.



- Kontrollera att kontrollsumman för versionsfilen finns i kontrollsummefilen med hjälp av kommandot `sha256sum --ignore-missing --check SHA256SUMS`.



- Utdata från detta kommando bör innehålla namnet på den nedladdade versionsfilen följt av `OK`. Example: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK`.



- Installera git med kommandot `sudo apt install git`. Klona sedan förvaret som innehåller PGP-nycklarna för Bitcoin core-signaturerna med kommandot `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Importera PGP-nycklarna för alla undertecknare med kommandot `gpg --import guix.sigs/builder-keys/*`



- Verifiera att checksummefilen är signerad med undertecknarnas PGP-nycklar med kommandot `gpg --verify SHA256SUMS.asc`.



Varje giltig signatur kommer att visa en rad som börjar med: `gpg: Bra signatur` och en annan rad som slutar med: `Primär nyckel fingeravtryck: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (exempel på Pieter Wuille's PGP-nyckelfingeravtryck).


**Det är inte nödvändigt att alla signeringsnycklar returnerar ett "OK". Faktum är att endast en kan vara nödvändig. Det är upp till användaren att bestämma sin egen valideringströskel för PGP-verifiering.


Du kan ignorera varningarna:



- `Den här nyckeln är inte certifierad med en betrodd signatur!`



- "Det finns inget som tyder på att signaturen tillhör ägaren


### Installation av den grafiska Bitcoin core Interface



- I terminalen, fortfarande i den katalog där Bitcoin core-versionens fil finns, använder du kommandot `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` för att extrahera filerna i arkivet.



- Installera de tidigare extraherade filerna med kommandot `sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin/*`



- Installera de nödvändiga beroendena med kommandot `sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev`



- Starta _bitcoin-qt_ (Bitcoin core grafisk Interface) med kommandot `Bitcoin-qt`.



- Om du vill välja en pruned-nod markerar du _Limit Blockchain storage_ och konfigurerar den datagräns som ska lagras:


![welcome](assets/fr/02.webp)


### Slutsats av del 1: Installationsguide


När Bitcoin core har installerats rekommenderas att du håller den igång så mycket som möjligt för att bidra till Bitcoin-nätverket genom att verifiera transaktioner och överföra nya block till andra peers.


Att köra och synkronisera noden med jämna mellanrum, till och med bara för att validera mottagna och skickade transaktioner, är dock fortfarande en bra metod.


![Creation wallet](assets/fr/03.webp)


## Konfigurera Tor för en Bitcoin core-nod


**Den här guiden är utformad för Bitcoin core 24.0.1 på Ubuntu/Debian-kompatibla Linux-distributioner.


### Installera och konfigurera Tor för Bitcoin core


Först måste vi installera Tor-tjänsten (The Onion Router), ett nätverk som används för anonym kommunikation, vilket gör det möjligt för oss att anonymisera våra interaktioner med Bitcoin-nätverket. En introduktion till verktyg för integritetsskydd online, inklusive Tor, finns i vår artikel om detta ämne.


För att installera Tor, öppna en terminal och ange `sudo apt -y install tor`. När installationen är klar kommer tjänsten normalt att startas automatiskt i bakgrunden. Kontrollera att den körs korrekt med kommandot `sudo systemctl status tor`. Svaret bör visa `Active: active (exited)`. Tryck på `Ctrl+C` för att avsluta denna funktion.


**Tips:** Du kan i alla fall använda följande kommandon i terminalen för att starta, stoppa eller starta om Tor:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Låt oss sedan starta den grafiska Bitcoin core Interface med kommandot `Bitcoin-qt`. Aktivera sedan programvarans automatiska funktion för att dirigera våra anslutningar via en Tor-proxy: _Inställningar > Nätverk_, och därifrån markerar du _Connect through SOCKS5 proxy (default proxy)_ samt _Use a separate SOCKS5 proxy to reach peers via Tor onion services_.


![option](assets/fr/04.webp)


Bitcoin core upptäcker automatiskt om Tor är installerat och kommer i så fall som standard att skapa utgående anslutningar till andra noder som också använder Tor, utöver anslutningar till noder som använder IPv4/IPv6-nätverk (clearnet).


**För att ändra språket på displayen till franska, gå till fliken Display i Inställningar.


### Avancerad Tor-konfiguration (tillval)


Det är möjligt att konfigurera Bitcoin core så att den endast använder Tor-nätverket för att ansluta till peers, vilket optimerar vår anonymitet via vår nod. Eftersom det inte finns någon inbyggd funktion för detta i den grafiska Interface måste vi manuellt skapa en konfigurationsfil. Gå till Inställningar och sedan Alternativ.


![option 2](assets/fr/05.webp)


Klicka här på _Öppna konfigurationsfil_. Väl i textfilen `Bitcoin.conf` lägger du bara till en rad `onlynet=onion` och sparar filen. Du måste starta om Bitcoin core för att detta kommando ska träda i kraft.


Vi kommer sedan att konfigurera Tor-tjänsten så att Bitcoin core kan ta emot inkommande anslutningar via en proxy, vilket gör att andra noder i nätverket kan använda vår nod för att ladda ner Blockchain-data utan att äventyra säkerheten för vår maskin.


I terminalen skriver du `sudo nano /etc/tor/torrc` för att komma åt konfigurationsfilen för Tor-tjänsten. I den här filen letar du efter raden `#ControlPort 9051` och tar bort `#` för att aktivera den. Lägg nu till två nya rader i filen:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Om du vill avsluta filen medan du sparar den trycker du på `Ctrl+X > Y > Enter`. Tillbaka i terminalen startar du om Tor genom att ange kommandot `sudo systemctl restart tor`.


Med den här konfigurationen kan Bitcoin core upprätta inkommande och utgående anslutningar med andra noder i nätverket endast via Tor-nätverket (Onion). För att bekräfta detta klickar du på fliken _Window_ och sedan på _Peers_.


![Nodes Window](assets/fr/06.webp)


### Ytterligare resurser


Om du bara använder Tor-nätverket (`onlynet=onion`) kan det i slutändan göra dig sårbar för en Sybil Attack. Det är därför som vissa rekommenderar att man upprätthåller en konfiguration med flera nätverk för att minska denna typ av risk. Dessutom kommer alla IPv4/IPv6-anslutningar att dirigeras genom Tor-proxyn när den har konfigurerats, som tidigare angivits.


Alternativt, om du vill vara kvar enbart i Tor-nätverket och minska risken för en Sybil Attack, kan du lägga till Address för en annan betrodd nod i din `Bitcoin.conf`-fil genom att lägga till raden `addnode=trusted_address.onion`. Du kan lägga till den här raden flera gånger om du vill ansluta till flera betrodda noder.


Om du vill visa loggarna för din Bitcoin-nod som är specifikt relaterade till dess interaktion med Tor, lägger du till `debug=tor` i filen `Bitcoin.conf`. Du kommer nu att ha relevant Tor-information i din debugglogg, som du kan visa i fönstret _Information_ med knappen _Debug File_. Det är också möjligt att se dessa loggar direkt i terminalen med kommandot `bitcoind -debug=tor`.


**Tips💡:** här är några intressanta länkar:


- [Wiki-sida som förklarar Tor och dess förhållande till Bitcoin] (https://en.Bitcoin.it/wiki/Tor)
- [Bitcoin core konfigurationsfilgenerator av Jameson Lopp](https://jlopp.github.io/Bitcoin-core-config-generator/)
- [Tor-konfigurationsguide av Jon Atack](https://github.com/Bitcoin/Bitcoin/blob/master/doc/tor.md)


Som alltid, om du har några frågor är du välkommen att dela dem med Agora256-communityn. Vi lär oss tillsammans för att bli bättre imorgon än vad vi är idag!