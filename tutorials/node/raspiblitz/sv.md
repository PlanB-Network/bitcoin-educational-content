---
name: RaspiBlitz
description: Guide för att ställa in din RaspiBlitz
---

![image](assets/0.webp)


RaspiBlitz är en gör-det-själv Lightning-nod (LND och/eller Core Lightning) som körs tillsammans med en Bitcoin-Fullnode på en RaspberryPi (1TB SSD) och en fin skärm för enkel installation och övervakning.


RaspiBlitz är främst inriktat på att lära sig hur man driver sin egen nod decentraliserat hemifrån - eftersom: Inte din nod, inte dina regler. Upptäck och utveckla det växande ekosystemet i Lightning Network genom att bli en fullvärdig del av det. Bygg den som en del av en workshop eller som ett helgprojekt själv.


![video](https://youtu.be/DTHlSPMz3ns)

RASPIBLITZ - Hur man kör en blixt och Bitcoin Full node av BTC-session


# Parman's Raspiblitz installationsguide


Raspiblitz är ett utmärkt system för att köra en Bitcoin-nod och tillhörande appar. Jag rekommenderar detta och My Node-noden till de flesta användare (Ha helst två noder för redundans.) En stor fördel är att Raspiblitz-noden är "Free Open Source Software", till skillnad från MyNode eller Umbrel. Varför är det viktigt? Vlad Costa förklarar. Du kan också köra RaspbiBlitz med en WiFi-anslutning snarare än ethernet - här är en kompletterande guide för det. (Jag har inte hittat något sätt att göra detta med MyNode).


Du kan köpa en färdig nod med en monterad miniskärm, eller så kan du bygga den själv (du behöver ingen skärm).


Guiden på github-sidan är utmärkt, men möjligen för detaljerad för en måttligt erfaren användare. Mina instruktioner kommer att vara mer kortfattade och förhoppningsvis lättare att följa.


I grund och botten är processen mycket lik processen för att ställa in en MyNode-nod med en Raspberry Pi 4. Raspiblitz-guiden föreslår att du köper en bildskärm, men du behöver verkligen inte en, och jag skulle inte rekommendera det. Du behöver inte ens ett extra tangentbord eller mus. Öppna bara enhetens terminalmeny via en dator i samma hemnätverk och använd ssh-kommandot med hjälp av terminal. Detta är möjligt med Linux/Mac (enkelt) och lite svårare med Windows.


## Steg 1: Köp utrustningen.


Du behöver exakt samma utrustning som du behöver för att köra en MyNode-nod. Du kan prova det ena eller det andra, den enda skillnaden är data på micro SD-kortet.



- Raspberry Pi 4, 4Gb minne eller 8Gb (4Gb räcker gott och väl)
- Officiell Raspberry Pi Power (Mycket viktigt! Få inte generisk, allvarligt)
- Ett fodral för Pi. (FLIRC-fodralet är fantastiskt. Hela fodralet är en kylfläns och du behöver inte en fläkt, som kan vara bullrig)
- 32 Gb microSD-kort (du behöver ett, men några är praktiska. )
- En minneskortläsare (de flesta datorer har inte plats för ett microSD-kort).
- Extern SSD 1Tb Hard-enhet.
- En Ethernet-kabel (för att ansluta till din hemrouter).


Du behöver ingen bildskärm (eller tangentbord eller mus)


Obs: Det här är fel Hard-enhet: Detta är en bärbar extern Hard-enhet. Det är inte en SSD. SSD är avgörande. Det är därför det är billigt (Pris i AUD)


![image](assets/1.webp)


Detta är rätt typ att få:


![image](assets/2.webp)


Detta går snabbare, men är onödigt dyrt:


![image](assets/3.webp)


## Steg 2: Ladda ner Raspiblitz-bilden


Navigera till Raspiblitz github-webbplats och hitta länken "download image":


![image](assets/4.webp)


Den nedladdade filens sha-256 Hash tillhandahålls på webbplatsen. Det kommer att ändras med varje uppdatering. Om du inte förstår vad det här handlar om bör du göra det, så jag skrev en guide som du kan läsa här.


![image](assets/5.webp)


## Steg 3: Verifiera bilden


Innan du fortsätter, om du inte känner till filsystemet på kommandoraden, är det lätt att lära sig, och du borde göra det.


Här är en användbar video för Linux, men den gäller även för Mac.


För Windows finns här en enkel handledning.


Mac/Linux


Vänta tills filen har laddats ner (viktigt!) och navigera sedan till den plats där du laddade ner filen med terminalen öppen och skriv följande kommando:

```bash
shasum -a 256 xxxxxxxxxxxxxx
```


där `xxxxxxxxxxxxxx` är namnet på den fil du just hämtade. Om du inte befinner dig i den katalog där filen finns måste du skriva in hela sökvägen.


Datorn funderar i ungefär 20 sekunder. Kontrollera att den utgående hashfilen matchar den som hämtades från webbplatsen i föregående steg. Om den är identisk kan du fortsätta.

Fönster


Öppna kommandotolken och navigera till den plats där filen har laddats ner och skriv följande kommando:


```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```


där `xxxxxxxxxxxxxx` är namnet på filen som du just hämtade. Om du inte befinner dig i den katalog där filen finns, måste du skriva in hela sökvägen.


Datorn funderar i ungefär 20 sekunder. Kontrollera att den utgående hashfilen matchar den som hämtades från webbplatsen i föregående steg. Om den är identisk kan du fortsätta.


## Steg 4: Flasha SD-kortet


Du kan använda Balena Etcher för att göra detta. Ladda ner den här.


Etcher är självförklarande att använda. Sätt i ditt micro SD-kort och flasha Raspiblitz-programvaran (.img-fil) på SD-kortet.


![image](assets/6.webp)


![image](assets/7.webp)


![image](assets/8.webp)


![image](assets/9.webp)


När du har gjort det är enheten inte längre läsbar. Du kan få ett felmeddelande från operativsystemet och hårddisken bör försvinna från skrivbordet. Dra ut kortet.


## Steg 5: Konfigurera Pi och sätt i SD-kortet


Delarna (fodralet visas inte):


![image](assets/10.webp)


![image](assets/11.webp)


Anslut Ethernet-kabeln och USB-kontakten till Hard-enheten (inte strömmen ännu). Undvik att ansluta till de blåfärgade USB-portarna i mitten. De är USB 3. Använd USB 2-portarna, även om enheten kan vara USB 3-kompatibel (mer tillförlitlig).


![image](assets/12.webp)


Micro SD-kortet placeras här:


![image](assets/13.webp)


Anslut slutligen strömmen:


![image](assets/14.webp)


## Steg 6: Hitta IP Address för Pi


Du behöver aldrig en bildskärm med Raspiblitz. Däremot behöver du en annan dator i hemnätverket. Om din Pi inte är ansluten via ethernet och du vill förlita dig på WiFi, kräver det lite datorkunskaper att hitta IP. Jag kan inte hjälpa dig, tyvärr. Du behöver en Ethernet-anslutning. (Problemet är att du behöver tillgång till en bildskärm och operativsystemet för att ansluta WiFi och ange ett lösenord)


Kontrollera routern för att få en lista över alla IP-adresser för alla anslutna enheter.


Jag skrev 192.168.0.1 i webbläsaren (instruktioner som följde med min router), loggade in och kunde se min enhet med IP 192.168.0.191. Observera att dessa IP-adresser inte är synliga för allmänheten på internet (de går först genom routern), de är bara identifierare för enheter i ditt hemnätverk.


Att hitta IP är avgörande.


**Du kan använda terminalen på en Mac eller Linux-maskin för att hitta IP Address för alla Ethernet-anslutna enheter i hemnätverket med kommandot "arp -a". Resultatet är inte lika snyggt som det som routern visar, men all information du behöver finns där. Om det inte är uppenbart vilken som är Pi, gör försök och fel.


## Steg 7: SSH till Pi


Kom ihåg att sätta in SD-kortet i Pi:n innan du slår på den. Vänta några minuter och öppna sedan terminalen på en annan Linux/Mac.


För Mac/Linux, skriv i terminalen:


```bash
ssh admin@You_Pi's_IP_address
```


För Windows måste du installera putty för att ssh:a in i Pi. Skriv samma kommando som ovan.


Första gången du gör detta, eller när du byter operativsystem på Pi genom att byta SD-kort, kan du få det här felet eller inte..


![image](assets/15.webp)


Du löser problemet genom att navigera till filen "known_hosts" (det står i felmeddelandet) och ta bort den. Kommandot är "rm known_hosts"


Upprepa sedan ssh-kommandot för att logga in. Detta kommer att hända..


![image](assets/16.webp)


Skriv ja (hela ordet) för att fortsätta.


Om det lyckas kommer du att bli ombedd att ange ett lösenord. Detta är inte för din dator, utan för raspiblitz. Det generiska lösenordet är "raspiblitz", och du kommer att ändra det senare. Terminalfönstret blir blått och du får menyalternativ som i de gamla DOS-menyerna. Navigera med piltangenterna eller musen.


![image](assets/17.webp)


Följ anvisningarna, ställ in dina lösenord och sedan kommer den att upptäcka din Hard-enhet och ge dig möjlighet att formatera den om det behövs.


Sedan får du frågan om du vill kopiera Blockchain-data från en annan källa eller ladda ner den på nytt. Att kopiera det är en inlärningsprocess och instruktionerna är ganska bra och bra att hålla praktiskt....


![image](assets/18.webp)


Det enkla men långsammare sättet är att ladda ner hela kedjan från början..


![image](assets/19.webp)


Massor av text blinkar över terminalskärmen. Du kanske misstar det för processen för nedladdning av Blockchain, men för mig ser det ut som att den genererar en privat nyckel för kommunikation.


Då visas blixtalternativ.


![image](assets/20.webp)


Skapa ett nytt lösenord för att låsa din belysning Wallet, då kommer en ny Wallet att skapas och du får 24 ord att skriva ner..


![image](assets/21.webp)


Se till att skriva ner det och förvara det på ett säkert sätt. Jag hörde talas om en person som inte gjorde det eftersom han inte planerade att använda blixten, men som ett år senare bestämde sig för att använda den och öppnade kanaler. När han sedan insåg att hans ord inte var säkerhetskopierade, och jag minns att det inte var möjligt att extrahera orden igen från enheten, var han tvungen att stänga alla sina kanaler och börja om från början. Han kom undan med det, men andra kanske inte har samma tur.


Efter detta rullar några minuters text ner i terminalfönstret. Och sedan..


![image](assets/22.webp)


Du kommer att loggas ut från ssh-sessionen. Logga in igen, den här gången med ditt nya lösenord, lösenord A. När du är inloggad kommer du att bli ombedd att ange lösenord C för att låsa upp din Lightning Wallet.


Nu väntar vi. Vi ses om två veckor. Du kan stänga terminalen, det gör inget med Pi, det är bara ett kommunikationsfönster.


![image](assets/23.webp)


Om du av någon anledning vill stänga av Pi innan Blockchain har avslutat nedladdningen går det bra så länge du gör det på rätt sätt. Blockchain kommer att fortsätta nedladdningen där den slutade när du återansluter.


Tryck på CTRL+c för att lämna den blå skärmen. Du kommer nu åt Pi-enhetens Linux-terminal. Här kan du skriva "menu" som laddar följande skärm, och därifrån kan du stänga av Pi.


![image](assets/24.webp)


Slut på guiden


Så från och med nu är din nod si redo att gå. Om du fortfarande hjälper till att navigera mer alternativ, hänvisa till github för mer handledning och guide https://github.com/raspiblitz/raspiblitz#feature-documentation