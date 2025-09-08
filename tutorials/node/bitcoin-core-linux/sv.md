---
name: Bitcoin Core (Linux)
description: Kör din egen nod med Bitcoin Core
---

![cover](assets/cover.webp)


# Kör din egen nod med Bitcoin Core


Introduktion till Bitcoin och konceptet med en nod, kompletterat med en omfattande installationsguide för Linux.


Ett av de mest spännande förslagen i Bitcoin är möjligheten att köra programmet själv och därmed delta på en detaljerad nivå i nätverket och verifieringen av den offentliga transaktionen Ledger.


Bitcoin, ett projekt med öppen källkod, har distribuerats offentligt och varit tillgängligt gratis sedan 2009. Nästan 15 år efter starten är Bitcoin nu ett robust och ostoppbart digitalt monetärt nätverk som drar nytta av en kraftfull organisk nätverkseffekt. För sina ansträngningar och sin vision förtjänar Satoshi Nakamoto vår tacksamhet. Förresten, vi är värd för Bitcoin whitepaper här på Agora 256 (notera: även på universitetet).


## Bli din egen bank


Att driva en egen nod har blivit viktigt för anhängare av Bitcoin-axiomet. Utan att be någon om lov är det möjligt att ladda ner Blockchain från början och därmed verifiera alla transaktioner från A till Ö enligt Bitcoin-protokollet.


Programmet innehåller också sin egen Wallet. På så sätt har vi kontroll över de transaktioner vi skickar till resten av nätverket, utan någon mellanhand eller tredje part. Du är din egen bank.


Resten av den här artikeln är därför en guide för att installera Bitcoin Core - den mest använda Bitcoin-programvaruversionen - specifikt på Debian-kompatibla Linux-distributioner som Ubuntu och Pop!/\_OS. Följ den här guiden för att ta ett steg närmare din individuella suveränitet.


## Installationsguide för Bitcoin Core för Debian/Ubuntu


**Förkunskaper**


- Minst 6 GB datalagring (beskuren nod) - 1 TB datalagring (Full node)
- Vänta minst 24 timmar med att slutföra IBD (Initial Block Download). Denna åtgärd är obligatorisk även för en beskuren nod.
- Tillåt ~600 GB bandbredd för IBD, även för en beskuren nod.


** Notera: 💡** följande kommandon är fördefinierade för Bitcoin Core version 24.1.


## Ladda ner och verifiera filer


1. Ladda ner Bitcoin-24.1-x86_64-linux-gnu.tar.gz, samt filerna SHA256SUMS och SHA256SUMS.asc. (https://bitcoincore.org/bin/Bitcoin-core-24.1/Bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. Öppna en terminal i den katalog där de nedladdade filerna finns. Till exempel, cd ~/Downloads/.

3. Kontrollera att kontrollsumman för versionsfilen finns i kontrollsummefilen med hjälp av kommandot sha256sum --ignore-missing --check SHA256SUMS.

4. Utdata från detta kommando bör innehålla namnet på den nedladdade versionsfilen följt av "OK". Exempel: Bitcoin-24.0.1-x86_64-linux-gnu: Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK.

5. Installera git med hjälp av kommandot sudo install git. Klona sedan förvaret som innehåller PGP-nycklarna för Bitcoin Core-signers med kommandot git clone https://github.com/Bitcoin-core/guix.sigs.

6. Importera PGP-nycklarna för alla undertecknare med kommandot gpg --import guix.sigs/builder-keys//\*

7. Verifiera att checksummefilen är signerad med undertecknarnas PGP-nycklar med kommandot gpg --verify SHA256SUMS.asc.


Varje signatur returnerar en rad som börjar med: gpg: Good signature och en annan rad som slutar med Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (exempel på Pieter Wuille's PGP-nyckelfingeravtryck).


**Det är inte nödvändigt att alla signeringsnycklar returnerar ett "OK". Faktum är att endast en kan vara nödvändig. Det är upp till användaren att bestämma sin egen valideringströskel för PGP-verifiering.


Du kan ignorera meddelandena VARNING:


- `Den här nyckeln är inte certifierad med en betrodd signatur!`
- "Det finns inget som tyder på att signaturen tillhör ägaren


## Installation av Bitcoin Core grafisk Interface


1. I terminalen, fortfarande i den katalog där filen Bitcoin Core version finns, använder du kommandot tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz för att extrahera filerna i arkivet.


2. Installera de tidigare extraherade filerna med kommandot sudo install -m 0755 -o root -g root -t /usr/local/bin Bitcoin-24.1/bin//\*


3. Installera de nödvändiga beroendena med kommandot sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev


4. Starta Bitcoin-qt (Bitcoin Core graphical Interface) med kommandot Bitcoin-qt.


5. Om du vill välja en beskuren nod markerar du Begränsa Blockchain-lagring och konfigurerar den datagräns som ska lagras:


![welcome](assets/1.webp)


## Slutsats av del 1: Installationsguide


När Bitcoin Core har installerats rekommenderas att du håller den igång så mycket som möjligt för att bidra till Bitcoin-nätverket genom att verifiera transaktioner och överföra nya block till andra peers.


Att köra och synkronisera noden med jämna mellanrum, till och med bara för att validera mottagna och skickade transaktioner, är dock fortfarande en bra metod.


![Creation wallet](assets/2.webp)


# Konfigurera Tor för en Bitcoin Core-nod


**Den här guiden är utformad för Bitcoin Core 24.0.1 på Ubuntu/Debian-kompatibla Linux-distributioner.


## Installera och konfigurera Tor för Bitcoin Core


Först måste vi installera Tor-tjänsten (The Onion Router), ett nätverk som används för anonym kommunikation, vilket gör det möjligt för oss att anonymisera våra interaktioner med Bitcoin-nätverket. En introduktion till verktyg för integritetsskydd online, inklusive Tor, finns i vår artikel om detta ämne.


För att installera Tor öppnar du en terminal och skriver sudo apt -y install tor. När installationen är klar kommer tjänsten normalt att startas automatiskt i bakgrunden. Kontrollera att den körs korrekt med kommandot sudo systemctl status tor. Svaret bör visa Aktiv: aktiv (avslutad). Tryck Ctrl+C för att avsluta denna funktion.


**Tips:** Du kan i alla fall använda följande kommandon i terminalen för att starta, stoppa eller starta om Tor:

```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Låt oss sedan starta Bitcoin Core grafiska Interface med kommandot Bitcoin-qt. Aktivera sedan programvarans automatiska funktion för att dirigera våra anslutningar via en Tor-proxy: Inställningar > Nätverk, och därifrån kan vi markera Anslut via SOCKS5-proxy (standardproxy) samt Använd en separat SOCKS5-proxy för att nå peers via Tor-lök-tjänster.


![option](assets/3.webp)


Bitcoin Core upptäcker automatiskt om Tor är installerat och kommer i så fall som standard att skapa utgående anslutningar till andra noder som också använder Tor, utöver anslutningar till noder som använder IPv4/IPv6-nätverk (clearnet).


**För att ändra språket på displayen till franska, gå till fliken Display i Inställningar.


## Avancerad Tor-konfiguration (tillval)


Det är möjligt att konfigurera Bitcoin Core så att den endast använder Tor-nätverket för att ansluta till peers, vilket optimerar vår anonymitet genom vår nod. Eftersom det inte finns någon inbyggd funktion för detta i den grafiska Interface måste vi manuellt skapa en konfigurationsfil. Gå till Inställningar och sedan Alternativ.


![option 2](assets/4.webp)


Klicka här på Öppna konfigurationsfil. När du är i textfilen Bitcoin.conf lägger du bara till raden onlynet=onion och sparar filen. Du måste starta om Bitcoin Core för att detta kommando ska träda i kraft.

Vi kommer sedan att konfigurera Tor-tjänsten så att Bitcoin Core kan ta emot inkommande anslutningar via en proxy, vilket gör att andra noder i nätverket kan använda vår nod för att ladda ner Blockchain-data utan att äventyra säkerheten för vår maskin.


I terminalen skriver du sudo nano /etc/tor/torrc för att komma åt konfigurationsfilen för Tor-tjänsten. I den här filen letar du efter raden #ControlPort 9051 och tar bort # för att aktivera den. Lägg nu till två nya rader i filen: HiddenServiceDir /var/lib/tor/Bitcoin-service/ och HiddenServicePort 8333 127.0.0.1:8334. Om du vill avsluta filen samtidigt som du sparar den trycker du på Ctrl+X > Y > Enter. När du är tillbaka i terminalen startar du om Tor genom att ange kommandot sudo systemctl restart tor.


Med den här konfigurationen kan Bitcoin Core endast upprätta inkommande och utgående anslutningar med andra noder i nätverket via Tor-nätverket (Onion). För att bekräfta detta klickar du på fliken Window och sedan på Peers.


![Nodes Window](assets/5.webp)


## Ytterligare resurser


Om du bara använder Tor-nätverket (onlynet=onion) kan du i slutändan bli sårbar för en Sybil-attack. Det är därför som vissa rekommenderar att man har en konfiguration med flera nätverk för att minska den här typen av risker. Dessutom kommer alla IPv4/IPv6-anslutningar att dirigeras genom Tor-proxyn när den har konfigurerats, som tidigare nämnts.


Alternativt, om du vill vara kvar enbart i Tor-nätverket och minska risken för en Sybil-attack, kan du lägga till Address för en annan betrodd nod i din Bitcoin.conf-fil genom att lägga till raden addnode=trusted_address.onion. Du kan lägga till den här raden flera gånger om du vill ansluta till flera betrodda noder.


Om du vill visa loggarna för din Bitcoin-nod som är specifikt relaterade till dess interaktion med Tor, lägger du till debug=tor i filen Bitcoin.conf. Du kommer nu att ha relevant Tor-information i din debug-logg, som du kan visa i fönstret Information med knappen Debug File. Det är också möjligt att visa dessa loggar direkt i terminalen med kommandot bitcoind -debug=tor.


**Tips💡:** här är några intressanta länkar:


- Wiki-sida som förklarar Tor och dess förhållande till Bitcoin
- Bitcoin Core konfigurationsfilgenerator av Jameson Lopp
- Konfigurationsguide för Tor av Jon Atack


Som alltid, om du har några frågor är du välkommen att dela dem med Agora256-communityn. Vi lär oss tillsammans för att bli bättre imorgon än vad vi är idag!