# Kör din egen Bitcoin Core-nod (Linux)

En introduktion till Bitcoin och nodkonceptet, tillsammans med en komplett installationsguide för Linux.

En av de mest spännande aspekterna med Bitcoin är möjligheten att köra programmet själv och därmed delta på en granulär nivå i nätverket och verifieringen av den offentliga transaktionsregistret.

Bitcoin, ett öppen källkodsprojekt, har varit offentligt tillgängligt och gratis sedan 2009. Nästan 15 år efter sin framkomst är Bitcoin idag ett robust och ostoppbart digitalt monetärt nätverk som drar nytta av en kraftfull organisk nätverkseffekt. För sina insatser och vision förtjänar Satoshi Nakamoto vår tacksamhet. För övrigt, vi värdar Bitcoin-vitboken här på Agora 256 (notera: även på universitetet).

## Bli din egen bank

Att köra sin egen nod har blivit en nödvändighet för Bitcoin-anhängare. Utan att behöva be om tillstånd från någon kan du ladda ner blockkedjan från början och därmed verifiera alla transaktioner från A till Ö enligt Bitcoin-protokollet.

Programmet innehåller också en plånbok. På så sätt har vi kontroll över de transaktioner vi skickar till resten av nätverket, utan några mellanhänder eller tredje parter. Du blir din egen bank.

Fortsättningen av denna artikel är en installationsguide för Bitcoin Core - den mest populära Bitcoin-programvaran - specifikt för Debian-baserade Linux-distributioner som Ubuntu och Pop!/\_OS. Följ denna guide för att ta ett steg närmare individens suveränitet.

## Installationsguide för Bitcoin Core på Debian/Ubuntu

> Förutsättningar
>
> - Minst 6 GB lagringsutrymme (för en beskuren nod) - 1 TB lagringsutrymme (för en komplett nod)
> - Räkna med minst 24 timmar för att slutföra IBD (Initial Block Download eller Initial nedladdning av block). Denna operation är obligatorisk även för en beskuren nod.
> - Räkna med ~600 GB bandbredd för IBD, även för en beskuren nod.

> 💡 Följande kommandon är fördefinierade för Bitcoin Core version 24.1.

## Hämta och verifiera filerna

1. Ladda ner bitcoin-24.1-x86_64-linux-gnu.tar.gz, samt filerna SHA256SUMS och SHA256SUMS.asc. (https://bitcoincore.org/bin/bitcoin-core-24.1/bitcoin-24.1-x86_64-linux-gnu.tar.gz)

2. Öppna en terminal i mappen där de nedladdade filerna finns. Exempel: cd ~/Downloads/.
3. Kontrollera att checksumman för versionsfilen finns med i checksumfilen genom att använda kommandot sha256sum --ignore-missing --check SHA256SUMS.
4. Resultatet av detta kommando bör inkludera namnet på den nedladdade versionsfilen samt "OK". Exempel: bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK.

5. Installera git med kommandot sudo install git. Sedan klona repo:t som innehåller Bitcoin Core-signatärernas PGP-nycklar med kommandot git clone https://github.com/bitcoin-core/guix.sigs.
6. Importera PGP-nycklarna för alla signatärer med kommandot gpg --import guix.sigs/builder-keys//\*
7. Kontrollera att checksumfilen är korrekt signerad med signatärernas PGP-nycklar med kommandot gpg --verify SHA256SUMS.asc.

Varje signatur kommer att returnera en rad som börjar med: gpg: Good signature och en annan rad som slutar med Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (exempel på fingeravtrycket för Pieter Wuilles PGP-nyckel).

> 💡 Det är inte nödvändigt att alla signatärnycklar returnerar "OK". I själva verket kan bara en vara nödvändig. Det är upp till användaren att bestämma sin egen valideringströskel för PGP-verifiering.
>
> Du kan ignorera meddelandena WARNING: This key is not certified with a trusted signature!

    There is no indication that the signature belongs to the owner.

## Installation av Bitcoin Core-gränssnittet

1. I terminalen, fortfarande i mappen där Bitcoin Core versionsfilen finns, använd kommandot tar xzf bitcoin-24.1-x86_64-linux-gnu.tar.gz för att extrahera filerna från arkivet.

2. Installera de tidigare extraherade filerna med kommandot sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-24.1/bin//\*

3. Installera nödvändiga beroenden med kommandot sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev

4. Starta bitcoin-qt (Bitcoin Core-gränssnittet) med kommandot bitcoin-qt.

5. För att välja en pruned nod, markera Limit blockchain storage och konfigurera datagränsen:

![welcome](assets/1.jpeg)

## Slutsats för del 1: installationsguide

När Bitcoin Core är installerat rekommenderas det att låta det köra så mycket som möjligt för att bidra till Bitcoin-nätverket genom att verifiera transaktioner och skicka nya block till andra noder.

Ändå är det en bra praxis att köra och synkronisera sin nod med jämna mellanrum, även om det bara är för att validera mottagna och utfärdade transaktioner.

![Creation wallet](assets/2.jpeg)

# Konfiguration av Tor för en Bitcoin Core-nod
💡 Denna guide är avsedd för Bitcoin Core 24.0.1 på Linux-distributioner som är kompatibla med Ubuntu/Debian.
## Installation och konfiguration av Tor för Bitcoin Core

Först måste vi installera Tor (The Onion Router), ett nätverk som används för anonym kommunikation, vilket kommer att möjliggöra anonymisering av våra interaktioner med Bitcoin-nätverket. För en introduktion till verktyg för online-privatliv, inklusive Tor, hänvisar vi till vår artikel om ämnet.

För att installera Tor, öppna en terminal och skriv sudo apt -y install tor. När installationen är klar kommer tjänsten normalt att startas automatiskt i bakgrunden. Kontrollera att den körs korrekt med kommandot sudo systemctl status tor. Svaret bör innehålla Active: active (exited). Tryck på Ctrl+C för att avsluta detta.

> I alla fall kan du använda följande kommandon i terminalen för att starta, stoppa eller starta om Tor:

```bash
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```

Starta sedan Bitcoin Core-gränssnittet med kommandot bitcoin-qt. Aktivera sedan den automatiska funktionen i programvaran för att dirigera våra anslutningar via en Tor-proxy: Inställningar > Nätverk, och där kan vi markera Anslut via SOCKS5-proxy (standardproxy) samt Använd en separat SOCKS5-proxy för att nå noder via Tor Onion Services.

![option](assets/3.jpeg)

Bitcoin Core upptäcker automatiskt om Tor är installerat och kommer i så fall att skapa utgående anslutningar (Outbound) till andra noder som också använder Tor, förutom anslutningar till noder som använder IPv4/IPv6-nätverken (clearnet).

> 💡 För att ändra språket till franska, gå till fliken Visa i Inställningar.

## Avancerad konfiguration av Tor (valfritt)

Det är möjligt att konfigurera Bitcoin Core för att endast använda Tor-nätverket för att ansluta till noder och därigenom optimera vår anonymitet genom vår nod. Eftersom det inte finns någon funktion för detta i det grafiska gränssnittet måste vi manuellt skapa en konfigurationsfil. Gå till Inställningar och sedan till Alternativ.

![option 2](assets/4.jpeg)

Här klickar du på Öppna konfigurationsfil. När du är i textfilen bitcoin.conf lägger du helt enkelt till en rad onlynet=onion och sparar filen. Du måste starta om Bitcoin Core för att detta kommando ska träda i kraft.

Vi kommer sedan att konfigurera Tor-tjänsten så att Bitcoin Core kan ta emot inkommande anslutningar via en proxy, vilket gör att våra noder i nätverket kan använda vår nod för att ladda ner blockchain-data utan att kompromettera säkerheten på vår maskin.
I terminalen, skriv sudo nano /etc/tor/torrc för att komma åt konfigurationsfilen för Tor-tjänsten. I denna fil, leta efter raden #ControlPort 9051 och ta bort # för att aktivera den. Lägg nu till två nya rader i filen: HiddenServiceDir /var/lib/tor/bitcoin-service/ och HiddenServicePort 8333 127.0.0.1:8334. För att lämna filen och spara ändringarna, tryck på Ctrl+X > Y > Enter. Återgå till terminalen och starta om Tor genom att skriva kommandot sudo systemctl restart tor.

Med denna konfiguration kan Bitcoin Core nu etablera inkommande och utgående anslutningar endast via Tor-nätverket (Onion). För att bekräfta detta, klicka på fliken "Fönster" och sedan "Noder".

![Fönster för noder](assets/5.jpeg)

## Ytterligare resurser

Att endast använda Tor-nätverket (onlynet=onion) kan göra dig sårbar för en Sybil-attack. Därför rekommenderar vissa att behålla en multi-nätverkskonfiguration för att motverka denna typ av risk. Dessutom kommer alla IPv4/IPv6-anslutningar att dirigeras genom Tor-proxyt när det väl är konfigurerat, som tidigare nämnts.

Som ett alternativ, för att endast vara ansluten till Tor-nätverket och minska risken för en Sybil-attack, kan du lägga till adressen för en annan nod som du litar på i din bitcoin.conf-fil genom att lägga till raden addnode=trusted_address.onion. Du kan lägga till denna rad flera gånger om du vill ansluta till flera betrodda noder.

För att se loggarna för din Bitcoin-nod som är specifika för dess interaktion med Tor, lägg till debug=tor i din bitcoin.conf-fil. Du kommer nu att ha relevant information om Tor i din debugglogg, som du kan se i fliken "Information" med knappen "Debugglogg". Det är också möjligt att se dessa loggar direkt i terminalen med kommandot bitcoind -debug=tor.

> 💡 Några intressanta länkar:
>
> - Wiki-sida som förklarar Tor och dess relation till Bitcoin
> - Bitcoin Core-konfigurationsgenerator av Jameson Lopp
> - Tor-konfigurationsguide av Jon Atack

Som alltid, om du har några frågor, tveka inte att dela dem med Agora256-communityn. Vi lär oss tillsammans för att vara bättre imorgon än vi är idag!