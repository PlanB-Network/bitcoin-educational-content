---
name: Dojo
description: En Bitcoin-nod med öppen källkod för integritet och autonomi
---

![cover](assets/cover.webp)



*Denna handledning är baserad på [den officiella Ashigaru-dokumentationen] (https://ashigaru.rs/docs/), som jag har tagit över och utökat. Jag har skrivit om alla avsnitt för att förbättra tydligheten, lagt till ytterligare detaljerade förklaringar samt illustrationer för nybörjare, för att göra installationen och användningen lättare att förstå.*



---

Dojo är ett program med öppen källkod som är utformat för att fungera som en backend-server för vissa integritetsinriktade Bitcoin-plånböcker, baserade på en Bitcoin core-nod. Historiskt sett utvecklades det för att fungera med Samourai Wallet, en mobil Wallet som erbjöd avancerade sekretessfunktioner som Whirlpool (CoinJoin), Ricochet, Stonewall, PayNym ... Samourai Wallet har nu stängts ned efter att dess utvecklare arresterats, men dess efterföljare i samhället, **Ashigaru Wallet**, har tagit över och fortsätter att förlita sig på Dojo för att erbjuda en komplett upplevelse för användare som vill hålla kontroll över sina data när de använder Bitcoin.



![Image](assets/fr/01.webp)



I praktiken fungerar Dojo som en gateway mellan din Wallet och Bitcoin-nätverket. Utan Dojo skulle en lätt mobil Wallet behöva fråga tredjepartsservrar för att få status på dina UTXO:er och din historik, eller för att sända dina transaktioner. Detta innebär ett beroende och läckage av känsliga uppgifter till en tredjepartsserver (använda adresser, belopp, betalningsfrekvens etc.). Med Dojo är du själv värd för denna server, direkt ansluten till din egen Bitcoin-nod. På så sätt passerar alla dina portföljförfrågningar genom en infrastruktur som du kontrollerar, utan mellanhänder, vilket förstärker din sekretess och suveränitet.



## Krav för att sätta upp en Dojo



Att sätta upp en Dojo-server kräver inte en extremt kraftfull maskin. Vem som helst med en nybörjardator, en stabil internetanslutning och förmågan att låta den vara påslagen kontinuerligt (24/7) kan sätta upp en fungerande Dojo.



### Välj din maskintyp



Du kan använda :




- en bärbar dator ;
- en stationär dator ;
- en mini-PC (t.ex. Intel NUC, Lenovo Thincentre Tiny ...).



Varje alternativ har sina för- och nackdelar:




- Pris: en renoverad mini-PC eller stationär dator är ofta billigare än en ny bärbar dator.
- Fotavtryck: en Mini-PC tar upp mindre utrymme.
- Ström Supply: en bärbar dator har fördelen av ett batteri, vilket innebär att den inte stängs av vid strömavbrott, till skillnad från en mini-PC.
- Uppgraderingsmöjligheter: Med barbones kan du i allmänhet lägga till minne eller enkelt byta ut en Hard-disk.



För mer information om hur du väljer din utrustning rekommenderar jag att du går den här kursen:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

### Rekommenderad utrustning



Det finns ingen anledning att köpa en ny maskin. En renoverad dator med nedanstående specifikationer kommer att ge mycket bättre prestanda än enkortselektronik (som Raspberry Pi).



**Minsta specifikationer:**




- X86-64-arkitektur (64-bitars processor).
- 2 GHz dual-core processor eller snabbare.
- minst 8 GB RAM-minne.
- 2 TB eller mer NVMe SSD (för att lagra Blockchain av Bitcoin och nödvändiga index).



**Rekommenderat operativsystem: **




- En Debian-baserad distribution, t.ex. Ubuntu 24.04 LTS.



**Rekommenderad utrustning:**




- HP EliteDesk / EliteBook
- Dell OptiPlex
- Lenovo ThinkCentre / ThinkPad
- Intel NUC
- etc.



Det är fullt möjligt att köra en Dojo-server på andra hårdvarukonfigurationer. För att få bästa möjliga prestanda och begränsa problem rekommenderar vi dock att du följer ovanstående rekommendationer.



I den här handledningen använder jag en gammal ThinkCentre Tiny med en Intel Pentium Dual-Core G4400T-processor, 8 GB RAM och en 2 TB SSD.



## 1 - Installera Ubuntu



*Om du vill installera Dojo på en enhet som redan är konfigurerad kan du hoppa över det här steget och gå direkt till steg 2.*



Efter att ha förberett den valda hårdvaran är det dags att installera ett operativsystem. Du kan använda i stort sett vilken Debian-distribution som helst, men jag rekommenderar att du väljer en LTS-version av Ubuntu, eftersom den passar perfekt för våra syften. Här är stegen som ska följas:



### 1.1. Skapa en startbar USB-nyckel



Från en dator som redan fungerar (din vanliga maskin), ladda ner Ubuntu LTS ISO-image [från den officiella webbplatsen](https://ubuntu.com/download/desktop) (`24.04` i skrivande stund, men ta den senaste om en annan finns tillgänglig).



![Image](assets/fr/02.webp)



Sätt i ett USB-minne på minst 8 GB i den här datorn och skapa sedan ett startbart minne med hjälp av en programvara som [Balena Etcher] (https://etcher.balena.io/). Välj den Ubuntu ISO-bild som du just har laddat ner, välj USB-nyckeln som målenhet och starta sedan skapandeprocessen (ha tålamod, det kan ta flera minuter).



![Image](assets/fr/03.webp)



Sätt i det startbara USB-minnet i den avstängda datorn (den som du vill köra Dojo på). Starta maskinen och tryck omedelbart på **F12** eller **F10** på tangentbordet (beroende på modell) för att komma till startmenyn. Välj sedan din USB-nyckel som den prioriterade enheten i datorns startordning.



![Image](assets/fr/04.webp)



### 1.2. Installera operativsystemet



Startskärmen för Ubuntu visas. Välj "Prova eller installera Ubuntu*".



![Image](assets/fr/05.webp)



Följ sedan den klassiska Ubuntu-installationsprocessen:




- Välj språk.
- Välj typ av tangentbord.
- Om du är ansluten via en RJ45-kabel behöver du inte konfigurera Wi-Fi.
- Klicka på "*Install Ubuntu*" och markera alternativet för att installera programvara från tredje part (Wi-Fi-drivrutiner, multimedia-codecs etc.).
- När guiden frågar efter typ av installation väljer du "*Radera hårddisken och installera Ubuntu*". **Varning**: denna operation kommer att radera innehållet på disken helt och hållet. Kontrollera noga att den disk du har valt motsvarar den NVMe SSD som är avsedd för Dojo.
- Skapa ett enkelt användarnamn (t.ex. "*loic*").
- Tilldela maskinen ett namn (t.ex. "*dojo-node*").
- Ange ett starkt lösenord och förvara det på ett säkert sätt.
- Aktivera alternativet "*Behöva mitt lösenord för att logga in*" för att stärka säkerheten.
- Ange din tidszon och klicka sedan på "*Install*".
- Vänta tills installationen är klar. När den är klar kommer systemet att starta om automatiskt.
- Ta bort USB-installationsnyckeln när du startar om datorn.



För mer information om installationsprocessen för Ubuntu, se vår dedikerade handledning :



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

### 1.3. Uppdatering av systemet



Efter den första uppstarten öppnar du en terminal med tangentkombinationen ***Ctrl + Alt + T*** och kör följande kommandon för att uppdatera systemet:



```bash
sudo apt update
sudo apt upgrade -y
```



![Image](assets/fr/06.webp)



## 2. Installation av uthus



För att Dojo ska fungera korrekt måste vissa programvarublock finnas på ditt system. Dessa används för att hantera programvaruarkiv, kommunikation, arkivdekomprimering och körning av Dojo i Docker-containrar. Alla dessa operationer utförs i terminalen.



### 2.1. Förberedelse



Med följande kommando kommer du tillbaka till din personliga mapp. Detta är en bra metod innan du kör en serie installationer.



```bash
cd ~/
```



Innan du installerar någon programvara ska du kontrollera att databasen med programvara som är tillgänglig på din maskin är uppdaterad. På så sätt undviker du att installera föråldrade versioner.



```bash
sudo apt-get update
```



![Image](assets/fr/07.webp)



### 2.2. Installera verktyg



Flera verktyg behöver läggas till i systemet:




- `apt-transport-https`: gör att du kan ladda ner paket säkert via HTTPS
- `ca-certificates`: hanterar de certifikat som krävs för krypterade anslutningar
- `curl`: för att hämta filer från Internet
- `gnupg-agent`: för hantering av GPG-nycklar
- software-properties-common": tillhandahåller verktyg för att manipulera APT-arkiv
- `unzip`: packar upp filer i ZIP-format



```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common unzip
```



Under installationen kan det hända att systemet ber om en bekräftelse. Tryck på tangenten "*y*" och sedan på "*Enter*".



![Image](assets/fr/08.webp)



### 2.3. Installera Torsocks



Torsocks gör det möjligt att utföra vissa kommandon via Tor-nätverket, vilket förbättrar konfidentialiteten i kommunikationen.



```bash
sudo apt install torsocks
```



![Image](assets/fr/09.webp)



### 2.4. Installera Docker och Docker Compose



Dojo körs inuti Docker-containrar. Det innebär att varje tjänst är isolerad i en egen miljö, vilket förenklar underhåll och säkerhet. För att göra detta måste du installera Docker och verktyget Docker Compose, som gör att du kan hantera flera containrar samtidigt.



#### Lägg till signeringsnyckel för Docker



Docker tillhandahåller sin egen digitala signaturnyckel. Genom att lägga till den verifieras äktheten hos nedladdade paket.



```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```



![Image](assets/fr/10.webp)



#### Officiell Docker-lagringsplats tillagd



Därefter måste du tala om för systemet var de officiella Docker-paketen finns. Det här kommandot lägger till ett nytt arkiv i konfigurationen av din pakethanterare.



```bash
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "*$VERSION_CODENAME*") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```



![Image](assets/fr/11.webp)



#### Installera Docker och Docker Compose



De viktigaste Docker-komponenterna kan nu installeras.



```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```



![Image](assets/fr/12.webp)



#### Auktorisering av användare



Som standard kan endast kommandon som utförs med administratörsrättigheter starta Docker. För större bekvämlighet rekommenderar jag att du lägger till din nuvarande användare i gruppen "*docker*". Detta gör att du kan använda Docker utan att behöva skriva `sudo` varje gång.



```bash
sudo usermod -aG docker $USER
```



![Image](assets/fr/13.webp)



## 3. Skapande av en enda användare (valfritt)



Om du vill förbättra säkerheten i ditt system rekommenderar jag att du skapar en separat användare enbart för att köra Dojo. Denna separation begränsar riskerna: om ett säkerhetsproblem uppstår i Dojo kommer det inte att direkt äventyra ditt huvudkonto.



### 3.1. Skapande av användarkonto



Följande kommando skapar en ny användare med namnet "*dojo*". Den här användaren kommer att ha en hemkatalog `/home/dojo` och tillgång till bash-terminalen. Den kommer också att läggas till i sudo-gruppen för att möjliggöra utförande av administratörskommandon.



```bash
sudo useradd -s /bin/bash -d /home/dojo -m -G sudo dojo
```



### 3.2. Ange ett lösenord



Det är viktigt att tilldela ett starkt lösenord till det här kontot. Helst bör du använda en lösenordshanterare som Bitwarden för att generate en lång Hard-kombination som är svår att gissa sig till.



```bash
sudo passwd dojo
```



Systemet ber dig sedan att ange det lösenord du har valt och sedan bekräfta det en gång till.



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

### 3.3. Auktorisera användaren att använda Docker



För att användaren "*dojo*" ska kunna starta de containrar som behövs för att köra Dojo måste han läggas till i Docker-gruppen. På så sätt slipper man föregå varje kommando med `sudo`.



```bash
sudo usermod -aG docker dojo
```



### 3.4. Omstart av systemet



För att gruppändringarna ska träda i kraft måste maskinen startas om.



```bash
sudo reboot
```



### 3.5. Logga in med ny användare



När systemet startas om loggar du in med ***dojo***-inloggningen och det lösenord som du definierade tidigare. Alla efterföljande steg måste utföras från detta dedikerade konto.



## 4. Ladda ner och kontrollera Dojo



Innan du installerar Dojo är det viktigt att se till att filerna kommer från den officiella utvecklaren och att de inte har ändrats. Detta steg förlitar sig på användningen av PGP och hashar för att verifiera filens äkthet och integritet.



### 4.1. importera utvecklarens PGP-nyckel



Ladda ner utvecklarens publika nyckel via Tor och importera den till din lokala nyckelring. Den här nyckeln kommer att användas för att verifiera signaturerna som är associerade med Dojo-filer.



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/14.webp)



### 4.2. Ladda ner den senaste versionen av Dojo



Hämta det komprimerade arkiv som innehåller Dojos källkod. I det här exemplet är den senaste versionen `1.27.0`: ändra kommandot enligt [den senaste versionen här på det officiella GitHub-arkivet](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases).



```bash
torsocks wget -O samourai-dojo-1.27.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.27.0.zip
```



![Image](assets/fr/15.webp)



### 4.3. Ladda ner fingeravtryck och signatur



Utvecklarna publicerar en fil som listar arkivens digitala fingeravtryck, samt en fil som är signerad med deras PGP-nyckel. Ladda ner dem för att jämföra dina filer lokalt.



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.27.0/samourai-dojo-1.27.0-fingerprints.txt.sig
```



![Image](assets/fr/16.webp)



### 4.4. Kontrollera PGP-signatur



Kontrollera att fingeravtrycksfilen har signerats med den importerade nyckeln.



```bash
gpg --verify samourai-dojo-1.27.0-fingerprints.txt.sig
```



Ett korrekt resultat visar en giltig signatur med nyckeln `E53AD419B242822F19E23C6D3033D463D6E544F6` och den tillhörande Address `dojocoder@pm.me`. En varning kan visas som anger att nyckeln inte är certifierad: du kan ignorera den.



Om signaturen däremot är ogiltig ska du omedelbart avbryta installationsprocessen och börja om från början.



![Image](assets/fr/17.webp)



### 4.5. Kontrollera arkivets integritet



Beräkna SHA256-fingeravtrycket för den nedladdade filen och öppna sedan fingeravtrycksfilen för att jämföra de två värdena.



```bash
sha256sum samourai-dojo-1.27.0.zip
cat samourai-dojo-1.27.0-fingerprints.txt
```



Om de två fingeravtrycken är identiska kan du vara säker på att arkivet inte har ändrats. Om de är olika, gå inte längre och radera filerna.



![Image](assets/fr/18.webp)



### 4.6. Extrahera och organisera filer



När verifieringen har slutförts kan du packa upp arkivet och förbereda en mapp som är avsedd för Dojo-installationen.



```bash
unzip samourai-dojo-1.27.0.zip -d .
mkdir ~/dojo-app
mv ~/samourai-dojo-1.27.0/* ~/dojo-app/
```



![Image](assets/fr/19.webp)



### 4.7. Rensa upp onödiga filer



Ta bort temporära filer och arkiv som inte längre behövs för att hålla miljön ren.



```bash
rm -r samourai-dojo-1.27.0 && rm samourai-dojo-1.27.0.zip && rm samourai-dojo-1.27.0-fingerprints.txt && rm samourai-dojo-1.27.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



![Image](assets/fr/20.webp)



## 5. Dojo-konfiguration



Dojo är en backend-server som samlar flera tjänster för att interagera med din portfölj och hantera din Bitcoin-nod. Konfigurationen kan vara komplex, men projektet erbjuder en förenklad metod som automatiskt installerar och konfigurerar följande komponenter:




- Dojo (huvud-API)
- Bitcoin core (komplett Bitcoin nod)
- BTC-RPC Explorer (webb Block explorer)
- Fulcrum Indexer (snabb indexering av block och transaktioner)
- Fulcrum Electrum Server tillgänglig på Tor-nätverket
- Fulcrum Electrum Server tillgänglig i det lokala nätverket
- Behörighet för administration



### 5.1. Administratörsbehörighet



För att säkra åtkomst till de olika tjänsterna behöver du generate flera unika identifierare:




- `BITCOIND_RPC_USER`
- `BITCOIND_RPC_LÖSENORD`
- `MYSQL_ROOT_PASSWORD`
- mYSQL_ANVÄNDARE
- `MYSQL_LÖSENORD`
- nODE_API_KEY`
- `NODE_ADMIN_KEY`
- `NODE_JWT_SEKRET`



Dessa identifierare **måste vara unika** (detta är mycket viktigt: du får inte använda samma lösenord för flera tjänster), endast bestå av siffror, versaler och gemener (alfanumeriska) och vara cirka 40 tecken långa för att garantera en hög säkerhetsnivå. Återigen rekommenderar jag starkt att du använder en lösenordshanterare.



### 5.2. Åtkomst till konfigurationsfiler



Dojos konfigurationsfiler finns i mappen `conf/`. Flytta till denna katalog:



```bash
cd ~/dojo-app/docker/my-dojo/conf/
```



![Image](assets/fr/21.webp)



### 5.3. Bitcoin core-konfiguration



Öppna konfigurationsfilen för Bitcoin core med textredigeraren nano:



```bash
nano docker-bitcoind.conf.tpl
```



![Image](assets/fr/22.webp)



I den här filen anger du de genererade identifierarna:



```
BITCOIND_RPC_USER=your-ID-here
BITCOIND_RPC_PASSWORD=your-password-here
```



⚠️ *** Ersätt "ditt-ID-här" och "dittlösenord-här" med dina egna inloggningar (med ett starkt lösenord) ***



Du kan också justera storleken på det cacheminne som Bitcoin core använder för att förbättra prestandan (du kan till och med använda mer om du har mycket RAM tillgängligt):



```
BITCOIND_DB_CACHE=2048
```



Spara ändringarna och stäng redigeringsverktyget :




- tryck på `Ctrl + X
- typ `y`
- tryck sedan på "*Enter*"



### 5.4. MySQL-konfiguration



Öppna sedan MySQL-databasens konfiguration:



```bash
nano docker-mysql.conf.tpl
```



Vänligen ange dina inloggningsuppgifter:



```
MYSQL_ROOT_PASSWORD=your-password-here
MYSQL_USER=your-ID-here
MYSQL_PASSWORD=your-password-here
```



⚠️ *** Ersätt "ditt-ID-här" och "ditt-lösenord-här" med dina egna inloggningar (med starka, unika lösenord) ***



Spara på samma sätt (`Ctrl + X`, `y`, "*Enter*").



![Image](assets/fr/23.webp)



### 5.5. Konfiguration av Fulcrum-indexerare



Öppna följande fil:



```bash
nano docker-indexer.conf.tpl
```



Lägg till parametrarna för att aktivera Fulcrum och integrera det korrekt i Dojo :



```
INDEXER_INSTALL=on
INDEXER_TYPE=fulcrum
INDEXER_BATCH_SUPPORT=active
INDEXER_EXTERNAL=on
```



![Image](assets/fr/24.webp)



Därefter finns det 2 möjligheter, beroende på din konfiguration. Om Dojo är installerat på en maskin som är skild från din vanliga dator (på en dedikerad maskin, en server ...) anger du dess IP Address i ditt lokala nätverk, till exempel :



```
INDEXER_EXTERNAL_IP=192.168.1.157
```



![Image](assets/fr/25.webp)



Om du vill ta reda på den lokala IP Address för din maskin öppnar du en annan terminal och skriver in följande kommando:



```bash
hostname -I
```



Andra möjligheten: om Dojo körs direkt på din vanliga dator, behåll det standardvärde som redan finns i konfigurationsfilen :



```
INDEXER_EXTERNAL_IP=127.0.0.1
```



Spara och avsluta redigeringsverktyget (`Ctrl + X`, `y`, "*Enter*").



### 5.6. Konfiguration av nodetjänst



Slutligen öppnar du konfigurationen för Dojos huvudtjänst:



```bash
nano docker-node.conf.tpl
```



Vänligen ange dina inloggningsuppgifter:



```
NODE_API_KEY=your-password-here
NODE_ADMIN_KEY=your-password-here
NODE_JWT_SECRET=your-password-here
```



⚠️ *** Ersätt "ditt lösenord här" med dina egna inloggningsuppgifter (med starka, unika lösenord) ***



![Image](assets/fr/26.webp)



Aktivera sedan den lokala indexeraren:



```
NODE_ACTIVE_INDEXER=local_indexer
```



Spara och avsluta redigeringsverktyget (`Ctrl + X`, `y`, "*Enter*").



### 5.7. Hantering av inloggning



När konfigurationen är klar är det inte nödvändigt att spara alla identifierare som genererats. Den enda som absolut måste sparas är :



```
NODE_ADMIN_KEY
```



Med den här inloggningen kan du senare logga in i underhållsverktyget Dojo. Alla andra inloggningar kan tas bort från din lösenordshanterare eller handskrivna anteckningar. De förblir tillgängliga från Dojos konfigurationsfiler om du skulle behöva hämta dem i framtiden.



## 6. Installation av dojo



I det här skedet kommer Dojo att installeras och startas på din maskin. Operationen kommer att starta flera tjänster (Bitcoin core, Fulcrum indexeraren, Dojo backend, etc.) och initiera fullständig synkronisering av Blockchain Bitcoin. Detta kan ta flera dagar, beroende på din maskinvara och internetanslutning.



### 6.1. Kontrollera att Docker fungerar korrekt



Innan du påbörjar installationen ska du kontrollera att Docker är i drift. Kör följande kommando:



```bash
docker run hello-world
```



Detta kommando laddar ner och startar en liten testbehållare. Om allt fungerar korrekt bör du se ett meddelande som liknar :



```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```



![Image](assets/fr/27.webp)



Om detta meddelande inte visas börjar du med att starta om maskinen med :



```bash
sudo reboot
```



Logga sedan in igen på ditt **dojo**-konto och kör testkommandot igen. Om felet kvarstår har Docker inte installerats korrekt. Gå i så fall tillbaka till steg `2.4.` om installation av Docker och kontrollera varje kommando noggrant.



### 6.2. Gå till installationskatalogen för Dojo



De skript som krävs för installationen finns i mappen `my-dojo`. Flytta till denna katalog:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/28.webp)



Använd kommandot `ls` för att kontrollera att filen `dojo.sh` finns. Detta är huvudskriptet som automatiserar installationen av Dojo och lanseringen av alla dess tjänster.



![Image](assets/fr/29.webp)



### 6.3. Starta installationen



Starta installationen genom att köra :



```bash
./dojo.sh install
```



Bekräfta installationen genom att trycka på "y" och sedan på "*Enter*".



![Image](assets/fr/30.webp)



Detta skript kommer att :




- ladda ner och starta de nödvändiga Docker-containrarna,
- initiera Bitcoin core och påbörja synkronisering av Blockchain,
- starta Fulcrum-indexeraren för att spåra transaktioner och adresser,
- aktivera Dojo-backend och dess API:er.



Du kommer att se en stadig ström av loggar som rullar förbi, med färgglada referenser som `bitcoind`, `soroban`, `nodejs` eller `fulcrum`. Denna rullning indikerar att Dojo är igång och börjar köra de olika tjänsterna.



![Image](assets/fr/31.webp)



### 6.4. Avsluta loggvisning



Loggar visas i realtid i din terminal. Om du vill återgå till kommandotolken medan Dojo körs i bakgrunden skriver du :



```
Ctrl + C
```



Oroa dig inte: om du stoppar loggvisningen stoppas inte tjänsterna. Docker fortsätter att köra Dojo i bakgrunden (du behöver naturligtvis inte stoppa datorn om du vill att IBD ska fortsätta).



### 6.5. Förståelse av *Initial Block Download* (IBD)



Vid uppstart måste Bitcoin core ladda ner och verifiera hela Blockchain sedan 2009. Detta steg kallas ***Initial Block Download* (IBD)**. Det är viktigt, eftersom det gör det möjligt för din Dojo-nod att verifiera varje Bitcoin-block och transaktion oberoende av varandra.



Hur länge denna synkronisering pågår beror på flera faktorer:




- kraften i din processor och mängden RAM-minne som är tillgängligt,
- hastigheten på din disk,
- antalet och kvaliteten på de peers som din nod ansluter till,
- hastigheten på din Internetanslutning.



I praktiken tar denna operation i allmänhet mellan **2 och 7 dagar**. Under denna period kan du låta din maskin vara igång kontinuerligt. Ju längre maskinen är på, desto snabbare kommer synkroniseringen att slutföras. Jag råder dig att kontrollera synkroniseringsstatusen regelbundet genom att läsa Bitcoin core-loggarna eller genom att använda Dojo-underhållsverktyget när det har installerats (se nästa avsnitt).



För att fördjupa dina kunskaper om IBD och, mer allmänt, om hur din Bitcoin-nod fungerar och vilken roll den har, rekommenderar jag att du tar en titt på den här kursen:



https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426


## 7. Övervakning av synkronisering



När du installerar Dojo för första gången måste du vänta på att två huvudåtgärder ska slutföras helt: den fullständiga nedladdningen av Blockchain Bitcoin (*IBD*) och indexeringen av denna Blockchain av Fulcrum. Beroende på din anslutning och maskinkraft kan detta ta flera dagar. Under den här tiden kan du övervaka hur processen fortskrider för att se till att allt går smidigt.



Det finns två sätt att övervaka synkroniseringsstatusen:




- användning av Dojo Maintenance Tool (eller DMT), som är enkelt men ger få detaljer under IBD;
- direkt konsultation av Dojo-loggar på din maskin, mer tekniskt men mycket mer exakt.



### 7.1. Kontrollera via Dojo Maintenance Tool (DMT)



Dojo Maintenance Tool är ett säkert, webbaserat Interface som gör att du kan övervaka anläggningens status och utföra vissa åtgärder. Det är det enklaste och mest lättillgängliga sättet att övervaka IBD:ns framsteg. Under den inledande synkroniseringsfasen kan den information som visas vara begränsad. DMT visar t.ex. inte den detaljerade utvecklingen av Fulcrum-indexeringen. Å andra sidan, när synkroniseringen är klar, kommer DMT tydligt att visa :




- alla lampor på Green;
- det senast validerade blocket för varje tjänst (Node, Indexer, Dojo DB).



För att komma åt den måste du känna till webbadressen till din DMT och ansluta till den [via Tor-webbläsaren] (https://www.torproject.org/download/). För att göra detta öppnar du en terminal och går till katalogen `/my-dojo`:



```bash
cd ~/dojo-app/docker/my-dojo
```



Kör sedan följande kommando:



```bash
./dojo.sh onion
```



![Image](assets/fr/32.webp)



Du får då tillgång till all information som rör anslutningar till din Dojo via Tor. Den vi är intresserade av här är följande URL:



```
Dojo API and Maintenance Tool =
```



För att komma åt DMT från vilken maskin som helst i vilket nätverk som helst (även på distans), öppna Tor Browser och ange denna URL följt av `/admin`. Om din URL till exempel är `wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion`, måste du ange den i fältet [Tor Browser](https://www.torproject.org/download/):



```
wo4zobymdl45gmmzzmpoypeemoukbj74wpibc22rxs2yfgpej62v6dyd.onion/admin
```



⚠️ **Var vänlig håll denna Address strikt konfidentiell



Du kommer då att omdirigeras till en autentiseringssida. DMT loggas in med hjälp av lösenordet `NODE_ADMIN_KEY` som du genererade tidigare.



![Image](assets/fr/33.webp)



När du är inloggad kan du komma åt *Dojo Maintenance Tool*! Under IBD kan du se informationen "*Latest Block*" i menyn "*Full node*", som låter dig veta den aktuella statusen för din Bitcoin-nod.



![Image](assets/fr/34.webp)



Kom ihåg att bokmärka denna Address i Tor Browser för att enkelt kunna hämta den senare.



När din Dojo är helt synkroniserad bör du se Green markera ✅ på alla indikatorer på DMT-hemsidan.



### 7.2. Verifiering via Dojo-loggar



Det andra sättet att följa utvecklingen av din IBD är att titta direkt i maskinens loggar. Detta tillvägagångssätt erbjuder mycket mer exakt övervakning i realtid. Du kan se hur Bitcoin core går framåt när det gäller att ladda ner block och hur Fulcrum indexerar dem.



Anslut till den maskin som är värd för din Dojo och öppna en terminal. Alla kommandon ska utföras från katalogen `my-dojo`. Placera dig i den här mappen:



```bash
cd ~/dojo-app/docker/my-dojo
```



![Image](assets/fr/35.webp)



#### Bitcoin core loggar



Visa Bitcoin core-loggar för att följa IBD-förloppet:



```bash
./dojo.sh logs bitcoind
```



I början ser du en försynkroniseringsfas av blockhuvudena:



```
bitcoind | Pre-synchronizing blockheader, height : NNNNNN
```



När denna siffra når 100% kommer Bitcoin core att påbörja den fullständiga nedladdningen av Blockchain. Du kommer att se IBD-förloppet. För att ta reda på den aktuella blockhöjden, titta på det värde som anges av `height=`. Du kan också följa nyckeln `progress=`, som anger procentandelen av IBD-framstegen.



![Image](assets/fr/36.webp)



Som alltid kan du stänga loggarna och återgå till kommandotolken genom att använda kombinationen "Ctrl + C".



#### Fulcrum stockar



När Bitcoin core har slutfört försynkroniseringen av rubriken börjar Fulcrum indexera Blockchain allt eftersom. Visa dess loggar med :



```bash
./dojo.sh logs fulcrum
```



Du ser då höjden på det senast indexerade blocket, som anges efter `height:`, samt indexeringens framsteg i procent.



![Image](assets/fr/37.webp)



### 7.3. Korruption i Fulcrum-databasen



Fulcrum är en särskilt kraftfull indexerare, men installationen kan vara komplicerad, inte minst på grund av den känsliga databashanteringen. I händelse av strömavbrott eller plötslig maskinstängning under den inledande synkroniseringen kan indexerarens databas skadas. Du kan se detta till exempel om du har följande loggar:



```bash
fulcrum | The database has been corrupted etc...
```



**Denna typ av fel bör rättas till i den kommande versionen av Fulcrum 2.0.



Om detta händer dig har det ingen inverkan på bitcoind (din Bitcoin-nod): dess IBD kommer att fortsätta att utvecklas oberoende av Fulcrum. Du kommer dock inte att kunna använda Fulcrum förrän du har raderat dess korrupta data och startat om synkroniseringen från början. Så här fungerar det:



Stoppa Dojo:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Ta endast bort Fulcrum-behållaren och -volymen:



```bash
docker rm -f fulcrum || true
docker volume ls | grep -i fulcrum
docker volume rm my-dojo_data-fulcrum
```



Normalt är namnet `my-dojo_data-fulcrum`, om detta inte är fallet för dig, anpassa det namn som returneras av föregående kommando.



Återlansera sedan Dojo och bygg upp Fulcrum från grunden:



```bash
./dojo.sh upgrade
```



Du kan sedan kontrollera att Fulcrum fungerar korrekt genom att läsa loggarna:



```bash
docker logs -f fulcrum
```




## 8. Använda underhållsverktyget för Dojo



När din Bitcoin-knut är synkroniserad till varphuvudet med den mest Proof of Work, och Blockchain är 100% indexerad av Fulcrum, kan du börja använda din Dojo.



Din Dojo erbjuder ett brett utbud av funktioner, som regelbundet förbättras med varje ny version. Enligt min mening är de 2 viktigaste :




- möjligheten att ansluta din Ashigaru Wallet för att använda din egen nod för att konsultera Blockchain-data och sända dina transaktioner,
- och Block explorer, vilket ger dig tillgång till information om Blockchain Bitcoin utan att exponera dina data för en extern instans som du inte kontrollerar.



Låt oss ta reda på hur man använder dem.


### 8.1. Anslut Ashigaru till din Dojo



Att ansluta din Ashigaru Wallet till din Dojo är mycket enkelt: när du är på din DMT, öppna menyn "*Pairing*". En QR-kod visas, som du kan skanna direkt med Ashigaru-programmet.



![Image](assets/fr/38.webp)



Första gången du startar Ashigaru-programmet efter att du har skapat eller återställt din Wallet kommer du att omdirigeras till sidan "*Konfigurera din Dojo-server*". Tryck på "*Scan QR*" och skanna sedan QR-koden som visas på din DMT.



![Image](assets/fr/39.webp)



Klicka sedan på knappen "*Fortsätt*".



![Image](assets/fr/40.webp)



Du är nu ansluten till din Dojo.



![Image](assets/fr/41.webp)



### 8.2. Användning av Block explorer



Dojo installerar automatiskt en Block explorer, [BTC-RPC Explorer] (https://github.com/janoside/btc-RPC-explorer), som bygger direkt på data från din egen Bitcoin-nod. Med en explorer kan du få tillgång till råinformation från Blockchain och din Mempool via en lättförståelig Interface-webb. Du kan t.ex. enkelt kontrollera statusen för en pågående transaktion, se saldot för en Address eller undersöka sammansättningen av ett block.



För att komma åt den hämtar du helt enkelt Tor Address från din webbläsare. För att göra detta kör du samma kommando som du använde för att hämta Address för din DMT:



```bash
./dojo.sh onion
```



![Image](assets/fr/42.webp)



Du kommer att ha tillgång till all din Dojo-anslutningsinformation via Tor. Den vi är intresserade av här är följande URL:



```
Block Explorer =
```



Om du redan är ansluten till din DMT kan du också hitta denna Address i menyn "*Pairing*", inuti anslutningen JSON:



![Image](assets/fr/43.webp)



För att komma åt din webbläsare från vilken maskin som helst i vilket nätverk som helst (även på distans), öppna [Tor Browser] (https://www.torproject.org/download/) och ange den URL som du just har hämtat.



⚠️ **Var vänlig håll denna Address strikt konfidentiell



Du kommer då att ha tillgång till din egen Block explorer.



![Image](assets/fr/44.webp)



*Bildkredit: https://ashigaru.rs/.*



För att spåra en transaktion, ange bara dess txid i sökfältet längst upp till höger.



![Image](assets/fr/45.webp)



*Bildkredit: https://ashigaru.rs/.*



För att kontrollera de rörelser som är associerade med en Address, fortsätt på samma sätt genom att ange Address i sökfältet.



![Image](assets/fr/46.webp)



*Bildkredit: https://ashigaru.rs/.*



Du kan också ange ett blocks Hash eller höjd i sökfältet för att visa detaljer.



![Image](assets/fr/47.webp)



*Bildkredit: https://ashigaru.rs/.*



## 9. Underhåll av dojo



### 9.1 Stoppa din Dojo



Stäng aldrig plötsligt av strömmen till Dojo, eftersom det kan skada vissa databaser, särskilt Fulcrum-indexeraren. Om du måste stänga av den, utför alltid en ren avstängning av Dojo och stäng sedan av maskinen när alla procedurer har slutförts:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



### 9.2 Uppdatera din Dojo



Dojo utvecklas regelbundet och nya versioner släpps för att åtgärda buggar, förbättra stabiliteten och lägga till funktioner. Det är därför viktigt [att regelbundet kontrollera om det finns uppdateringar](https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases) och att uppdatera Dojo. Processen liknar den första installationen, men kräver att du ersätter vissa filer med den senaste tillgängliga versionen, samtidigt som du behåller din konfiguration. Här är de detaljerade steg som ska följas för en ren och säker uppdatering:



För att ta reda på den aktuella versionen av din Dojo, kör kommandot :



```bash
./dojo.sh version
```



Även om detta steg är valfritt rekommenderar jag att du börjar med att uppdatera ditt operativsystem. Detta minskar risken för inkompatibilitet och säkerställer att de beroenden som används av Dojo är uppdaterade:



```bash
sudo apt-get update
sudo apt-get upgrade
```



Gå till Dojo-katalogen och stoppa de aktuella tjänsterna:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh stop
```



Starta sedan om systemet för att börja om från början:



```bash
sudo reboot
```



Dojo levereras med digitalt signerade filer. Dessa PGP-signaturer säkerställer att filerna härrör från utvecklaren och inte har ändrats på något sätt. Det är viktigt att du kontrollerar dem varje gång du uppdaterar Dojo, precis som du gjorde när du först installerade det. Börja med att ladda ner utvecklarens publika nyckel via Tor och importera den sedan till :



```bash
torsocks wget http://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion/vks/v1/by-fingerprint/E53AD419B242822F19E23C6D3033D463D6E544F6 && gpg --import E53AD419B242822F19E23C6D3033D463D6E544F6
```



Gå tillbaka till din personliga katalog:



```bash
cd ~/
```



Ladda ner den senaste versionen av Dojo från GitHub via Tor. I det här exemplet är det version `1.28.0` (som ännu inte finns i skrivande stund: detta är bara för att ge ett exempel). Kom ihåg att ersätta filen och länken [med den version du vill installera] (https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases):



```bash
torsocks wget -O samourai-dojo-1.28.0.zip https://github.com/Dojo-Open-Source-Project/samourai-dojo/archive/refs/tags/v1.28.0.zip
```



Ladda också ner filen som innehåller PGP-fingeravtryck och signatur (kom ihåg att justera versionen i kommandot):



```bash
torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt && torsocks wget https://github.com/Dojo-Open-Source-Project/samourai-dojo/releases/download/v1.28.0/samourai-dojo-1.28.0-fingerprints.txt.sig
```



Kontrollera att den nedladdade fingeravtrycksfilen har signerats med utvecklarens nyckel:



```bash
gpg --verify samourai-dojo-1.28.0-fingerprints.txt.sig
```



Ett korrekt resultat bör visas :



```
gpg: Signature made [date + time]
gpg: using EDDSA key E53AD419B242822F19E23C6D3033D463D6E544F6
gpg: Good signature from "dojocoder@pm.me" <dojocoder@pm.me> [unknown]
```



En varning om att nyckeln inte är certifierad kan visas, men det har ingen betydelse. Om signaturen däremot är ogiltig eller motsvarar en annan nyckel, ska du inte gå längre utan börja om och kontrollera länkarna.



Beräkna sedan SHA256-fingeravtrycket för arkivet och jämför det med den officiella fingeravtrycksfilen :



```bash
sha256sum samourai-dojo-1.28.0.zip
cat samourai-dojo-1.28.0-fingerprints.txt
```



Om de två fingeravtrycken matchar varandra perfekt är arkivet äkta och intakt. Om de skiljer sig åt, radera filerna omedelbart och fortsätt inte.



Avkomprimera arkivet i din hemkatalog:



```bash
unzip samourai-dojo-1.28.0.zip -d .
```



Kopiera sedan innehållet till Dojo-katalogen och skriv över den gamla :



```bash
cp -a samourai-dojo-1.28.0/. dojo-app/
```



Denna åtgärd behåller dina konfigurationsfiler som finns i `~/dojo-app/docker/my-dojo/conf`, men ersätter alla andra filer med de uppdaterade versionerna.



Ta bort onödiga filer för att hålla din miljö ren :



```bash
rm -r samourai-dojo-1.28.0 && rm samourai-dojo-1.28.0.zip && rm samourai-dojo-1.28.0-fingerprints.txt && rm samourai-dojo-1.28.0-fingerprints.txt.sig && rm E53AD419B242822F19E23C6D3033D463D6E544F6
```



Gå tillbaka till Dojo-skriptkatalogen och kör kommandot update:



```bash
cd ~/dojo-app/docker/my-dojo
./dojo.sh upgrade -y
```



Detta kommando instruerar Docker att bygga om avbildningarna med de nya filerna och sedan automatiskt starta om alla tjänster. I slutet av processen, kontrollera loggarna för att se till att Bitcoin core, Fulcrum och Dojo alla fungerar korrekt:



```bash
./dojo.sh logs bitcoind
./dojo.sh logs fulcrum
```



Om tjänsterna startar utan fel och loggarna visar att block bearbetas är din Dojo nu uppdaterad och i drift.