---
name: Min nod
description: Ställ in din Bitcoin MyNode
---

![image](assets/0.webp)


[My Node](https://mynodebtc.com/) är det enklaste och mest kraftfulla sättet att driva en Bitcoin och Lightning-nod! Vi kombinerar den bästa programvaran med öppen källkod med vår Interface, hantering och support så att du enkelt, privat och säkert kan använda Bitcoin och Lightning.


## Typer av noduppsättningar


Det finns olika Node-konfigurationer. MyNode är utmärkt. Det finns många appar som följer med, och ännu fler om man betalar för premiumversionen. Det är annars väldigt tråkigt att ladda ner alla dessa appar själv. MyNode gör det ganska enkelt som du kommer att se.


Ett alternativt och liknande alternativ är RaspiBlitz. GUI:t är inte lika snyggt och apparna överlappar mycket med de appar som följer med MyNode, men Raspiblitz är gratis programvara med öppen källkod (FOSS) och MyNode är inte riktigt det. En annan skillnad är att MyNode körs i en Docker-container. Jag tycker att Docker är skrämmande och Hard att felsöka. Detta är bara ett problem om du stöter på fel eller buggar. Utvecklaren erbjuder hjälp för premiumanvändare och det finns också en Telegram-chattgrupp.


RaspiBlitz är bara flera program installerade på Linux, utan Docker. Den externa Hard-enheten kan enkelt anslutas till en annan Linux-maskin med Bitcoin Core, och så är man igång om man behöver.


Ett annat alternativ är att bara installera Bitcoin Core och en Electrum Server-variant (det finns flera) på ett operativsystem. Jag har guider för Linux (Raspberry Pi), Mac och Windows.


## Inköpslista



- Raspberry Pi 4, 4Gb minne eller 8Gb (4Gb räcker gott och väl)
- Officiell Raspberry Pi Power (Mycket viktigt! Få inte generisk, allvarligt)
- Ett fodral för Pi. FLIRC-fodralet är fantastiskt. Hela fodralet är en kylfläns och du behöver inte en fläkt, som kan vara bullrig
- 16 Gb microSD-kort (du behöver ett, men några är praktiska)
- En minneskortläsare (de flesta datorer har inte plats för ett microSD-kort).
- Extern SSD 1Tb Hard-enhet.

Obs: SSD är avgörande. använd inte bärbar extern Hard-enhet även om den är billigare


- En Ethernet-kabel (för anslutning till din hemrouter)
- Du behöver inte en bildskärm


## Ladda ner MyNode Image


Navigera till MyNodes webbplats Länk


![image](assets/1.webp)


Klicka på "Ladda ner nu


Ladda ner Raspberry Pi 4-versionen:


![image](assets/2.webp)


Det är en stor fil:


![image](assets/3.webp)


Ladda ner SHA 256-hasharna


![image](assets/4.webp)


Öppna terminalen på Mac eller Linux eller kommandotolken i Windows. Skriv in:


```bash
shasum -a 256 DOWNLOADEDFILENAME # <--- Mac/Linux
certUtil -hashfile DOWNLOADEDFILENAME SHA256 # <--- Windows
```


Datorn tänker i 20 sekunder eller så. Kontrollera sedan att den utgående hashfilen matchar den som hämtades från webbplatsen i föregående steg. Om den är identisk kan du fortsätta.

Flasha SD-kortet


## Ladda ner och installera Balena Etcher. Länk till


Jag kunde inte hitta den digitala signaturen för detta. Om du vet hur, vänligen meddela mig så uppdaterar jag den här artikeln.


Etcher är självförklarande att använda. Sätt i ditt micro SD-kort och flasha Raspberry Pi-programvaran (.img-fil) på SD-kortet.


![image](assets/5.webp)

![image](assets/6.webp)

![image](assets/7.webp)

![image](assets/8.webp)

![image](assets/9.webp)

![image](assets/10.webp)

![image](assets/11.webp)


När du har gjort det är enheten inte längre läsbar. Du kan få ett felmeddelande från operativsystemet och hårddisken bör försvinna från skrivbordet. Dra ut kortet.


## Installera Pi och sätt i SD-kortet


Delarna (fodralet visas inte):


![image](assets/12.webp)

![image](assets/13.webp)


Anslut Ethernet-kabeln och USB-kontakten till Hard-enheten (inte strömmen ännu). Undvik att ansluta till de blåfärgade USB-portarna i mitten. De är USB 3. MyNode rekommenderar att du använder USB 2-porten, även om enheten kan vara USB 3-kompatibel.


![image](assets/14.webp)


Micro SD-kortet placeras här:


![image](assets/15.webp)


Anslut slutligen strömmen:


![image](assets/16.webp)


## Hitta IP-adressen Address för Pi


Du behöver aldrig någon bildskärm med MyNode. Däremot behöver du en annan dator i hemnätverket. Om din Pi inte är ansluten via Ethernet och du vill förlita dig på WiFi, kräver det datorvana på hög nivå att hitta IP:n. Jag kan inte hjälpa dig, tyvärr. Du behöver en Ethernet-anslutning. (Problemet kommer från att du behöver tillgång till en bildskärm och operativsystemet för att ansluta till WiFi och ange ett lösenord).


Kontrollera din router för att få en lista över alla IP-adresser för alla anslutna enheter.


Jag skrev 192.168.0.1 i webbläsaren (instruktioner som följde med routern), loggade in och kunde se en enhet "MyNode" med IP 192.168.0.18. Observera att dessa IP-adresser inte är allmänt synliga på internet (de går först genom routern), de är bara identifierare för enheter i ditt hemnätverk.


Att hitta IP är avgörande.


**Du kan använda terminalen på en Mac eller Linux-maskin för att hitta IP Address för alla Ethernet-anslutna enheter i hemnätverket med kommandot "arp -a". Utmatningen är inte lika vacker som den som routern visar, men all information du behöver finns där. Om det inte är uppenbart vilken som är Pi, gör försök och fel.


## SSH till Pi


Du har möjlighet att logga in på enheten på distans med SSH-kommando, men det är inte nödvändigt (det är det om RaspiBlitz Node). Jag ska ändå visa dig hur, eftersom det är mycket praktiskt.


Öppna en Mac- eller Linux-dator (för Windows, ladda ner SSH-verktyget putty) och skriv:


```bash
ssh admin@192.168.0.18
```


Använd din egen IP Address. Användarnamnet för MyNode-enheten är som standard "admin". Lösenordet är "Bolt" som standard.


Om du har använt din Pi tidigare och bytt ut micro SD-kortet kommer du att få det här felet:


![image](assets/17.webp)


Vad du behöver göra är att navigera till var filen "known_hosts" finns och ta bort den. Det är säkert att göra det. Felmeddelandet visar dig sökvägen. För mig var det /Användare/MittAnvändarnamn/.ssh/


Glöm inte "." före ssh, det indikerar att det är en dold katalog.


Försök sedan med ssh-kommandot igen.


Den här gången kommer du att se denna utdata:


![image](assets/18.webp)


Filen som du raderade har raderats och du lägger till ett nytt fingeravtryck. Skriv ja och <enter>.


Du kommer att bli ombedd att ange lösenordet. Det är "Bolt"


Du har nu terminalåtkomst till MyNode Pi, utan skärm, och kan bekräfta att allt laddas smidigt.


![image](assets/19.webp)


## Åtkomst via webbläsaren


Öppna en webbläsare. Det måste vara en dator i ditt hemnätverk, du kan inte göra det från utsidan. Det finns ett sätt, men det är Hard. Jag har inte testat det.


Skriv in IP Address i webbläsarfönstret Address. Detta kommer att hända:


![image](assets/20.webp)


Ange lösenordet "Bolt" - ändra det senare.


Då kommer detta att hända:


![image](assets/21.webp)


Välj Formatera enhet


![image](assets/22.webp)


Nu väntar vi.


Vid någon tidpunkt kommer du att bli tillfrågad om du vill lägga in din produktnyckel eller använda den kostnadsfria "community edition" - jag ska visa Premium-utgåvan. Jag rekommenderar att du betalar för premiumversionen om du har råd med det, det är mycket värt det.


![image](assets/23.webp)


Du kommer då att se hur långt nedladdningen av blocken har kommit. Det tar flera dagar:


![image](assets/24.webp)


Det är säkert att stänga av maskinen under nedladdningen om du behöver det. Gå till inställningar och leta reda på knappen för att stänga av maskinen. Dra inte bara i sladden, du kan förstöra installationen eller Hard-enheten.


Se till att du tidigt går till "Inställningar" och inaktiverar quicksync. Det kommer att påbörja den första blocknedladdningen från början.


![image](assets/25.webp)


Jag ville gå vidare med att skapa guiden, så här är en annan MyNode som jag förberedde tidigare. Så här ser sidan ut när Blockchain har synkroniserats och flera "appar" har aktiverats och synkroniserats:


![image](assets/26.webp)


Observera att Electrum Server också måste synkroniseras, så så snart Bitcoin Blockchain har synkroniserats klickar du på knappen för att starta den processen - det tar en dag eller två. Allt annat är aktiverat på några minuter när du väljer att aktivera det. Du kan klicka på saker och utforska. Du kommer inte att ha sönder något. Om något går sönder (detta hände mig, men jag tror att det beror på att jag hade billiga delar) måste du blinka igen och börja ladda ner igen. Problemet jag har med MyNode är att om du behöver "re-flasha" måste du starta Blockchain-synkroniseringen igen från början. Det finns tekniska sätt runt detta, men det är inte lätt.


Om du vill prova en annan nod också, till exempel en RaspiBlitz, behöver du en extra SSD extern Hard-enhet och ett annat micro SD-kort för att flasha. Annars är det samma utrustning, du kan bara inte köra MyNode och RaspiBlitz samtidigt, uppenbarligen. Om du vill göra det är det dags att köpa en annan Raspberry Pi.


Nu när du har en nod igång, använd den, låt den inte bara sitta där och göra ingenting för dig. Följ min artikel (och video) om hur du ansluter din Electrum Desktop Wallet till Electrum Server och Bitcoin Core här.