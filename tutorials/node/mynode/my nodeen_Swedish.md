namn: Min Node
beskrivning: Installera din bitcoin MinNode

# Installera Bitcoin Core på Mac eller Windows

![bild](assets/0.jpeg)

https://mynodebtc.com/

Det enklaste och mest kraftfulla sättet att köra en Bitcoin- och Lightning-nod! Vi kombinerar den bästa öppna källkodsprogramvaran med vår gränssnitt, hantering och support så att du enkelt, privat och säkert kan använda Bitcoin och Lightning.

## Typer av nodinstallationer

Det finns olika nodinstallationer. MinNode är utmärkt. Det finns många appar som följer med den, och ännu fler om du betalar för premiumversionen. Det är annars mycket tråkigt att ladda ner alla dessa appar själv. MinNode gör det ganska enkelt som du kommer att se.

Ett alternativ och liknande alternativ är RaspiBlitz. GUI: n är inte lika trevlig och apparna överlappar mycket med apparna som följer med MinNode, men Raspiblitz är fri öppen källkodsprogramvara (FOSS) och MinNode är inte riktigt det. En annan skillnad är att MinNode körs i en Docker-container. Jag tycker att Docker är skrämmande och svårt att felsöka. Detta är bara ett problem om du stöter på fel eller buggar. Utvecklaren erbjuder hjälp för premiumanvändare och det finns också en Telegram-chattgrupp.

RaspiBlitz är bara flera program installerade på Linux, utan Docker. Den externa hårddisken kan enkelt anslutas till en annan Linux-dator med Bitcoin Core, och sedan är du igång om du behöver det.

Ett annat alternativ är att bara installera Bitcoin Core och en variant av Electrum Server (det finns flera) på ett operativsystem. Jag har guider för Linux (Raspberry Pi), Mac och Windows.

## Inköpslista

- Raspberry Pi 4, 4 GB minne eller 8 GB (4 GB är tillräckligt)

- Officiell Raspberry Pi-strömadapter (Mycket viktigt! Skaffa inte generisk, allvarligt talat)

- Ett skal för Pi. FLIRC-skalet är fantastiskt. Hela skalet fungerar som en värmeavledare och du behöver ingen fläkt, vilket kan vara bullrigt

- 16 GB microSD-kort (du behöver ett, men några är praktiska)

- Ett minneskortläsare (de flesta datorer har inte en plats för ett microSD-kort).

- Extern SSD 1Tb hårddisk.  
  Observera: SSD är avgörande. Använd inte en bärbar extern hårddisk även om den är billigare

- En Ethernet-kabel (för att ansluta till din hemmarouter)

- Du behöver inte en skärm

## Ladda ner MyNode-bild

Gå till MyNode-webbplatsen Länk

![bild](assets/1.jpeg)

Klicka på <Ladda ner nu>

Ladda ner versionen för Raspberry Pi 4:

![bild](assets/2.jpeg)

Det är en stor fil:

![bild](assets/3.jpeg)

Ladda ner SHA 256-hasharna

![bild](assets/4.jpeg)

Öppna terminalen på Mac eller Linux eller Kommandotolken för Windows. Skriv:

```bash
shasum -a 256 NEDLADDADFILENAMN # <--- Mac/Linux
certUtil -hashfile NEDLADDADFILENAMN SHA256 # <--- Windows
```

Datorn tänker i cirka 20 sekunder. Kontrollera sedan att hashfilen som genereras matchar den som laddades ner från webbplatsen i föregående steg. Om de är identiska kan du fortsätta.
Flasha SD-kortet

## Ladda ner och installera Balena Etcher. Länk

Jag kunde inte hitta den digitala signaturen för detta. Om du vet hur, låt mig veta så uppdaterar jag den här artikeln.

Etcher är självförklarande att använda. Sätt in ditt micro SD-kort och flasha Raspberry Pi-programvaran (.img-fil) på SD-kortet.

![bild](assets/5.jpeg)
![bild](assets/6.jpeg)
![image](assets/7.jpeg)![image](assets/8.jpeg)
![image](assets/9.jpeg)
![image](assets/10.jpeg)
![image](assets/11.jpeg)

När det är klart är enheten inte längre läsbar. Du kan få ett fel från operativsystemet och enheten bör försvinna från skrivbordet. Dra ut kortet.

## Installera Pi och sätt i SD-kortet

Delarna (hölje visas inte):

![image](assets/12.jpeg)
![image](assets/13.jpeg)

Anslut Ethernet-kabeln och USB-anslutningen för hårddisken (inte strömmen ännu). Undvik att ansluta till de blåfärgade USB-portarna i mitten. De är USB 3. MyNode rekommenderar att du använder USB 2-porten, även om enheten kan vara USB 3-kompatibel.

![image](assets/14.jpeg)

Det mikro-SD-kortet placeras här:

![image](assets/15.jpeg)

Slutligen, anslut strömmen:

![image](assets/16.jpeg)

## Hitta IP-adressen för Pi

Du behöver aldrig en skärm med MyNode. Du behöver dock en annan dator i det hemma nätverket. Om din Pi inte är ansluten via Ethernet och du vill använda WiFi krävs det hög nivå av datorfärdigheter för att hitta IP-adressen. Kan inte hjälpa dig, tyvärr. Du behöver en Ethernet-anslutning. (Problemet uppstår genom att du behöver tillgång till en skärm och operativsystemet för att ansluta till WiFi och ange ett lösenord).

Kontrollera din router för en lista över alla IP-adresser för alla anslutna enheter.

Jag skrev 192.168.0.1 i webbläsaren (instruktioner som följde med min router), loggade in och kunde se en enhet "MyNode" med IP-adressen 192.168.0.18. Observera att dessa IP-adresser inte är synliga för allmänheten (de går genom routern först), de är bara identifierare för enheter i ditt hemnätverk.

Att hitta IP-adressen är avgörande.

> UPPDATERING: Du kan använda terminalen på en Mac- eller Linux-dator för att hitta IP-adressen för alla Ethernet-anslutna enheter i hemnätverket med kommandot "arp -a". Utmatningen är inte lika snygg som vad routern kommer att visa, men all information du behöver finns där. Om det inte är uppenbart vilken enhet som är Pi, prova och fel.

## SSH till Pi

Du har möjlighet att logga in på enheten på distans med SSH-kommando, men det är inte nödvändigt (det är om det är en RaspiBlitz Node). Jag kommer ändå att visa dig hur, eftersom det är mycket praktiskt.

Öppna en Mac- eller Linux-dator (för Windows, ladda ner putty, ett SSH-verktyg) och skriv:

```bash
ssh admin@192.168.0.18
```

Använd din egen IP-adress. Användarnamnet för MyNode-enheten är "admin" som standard. Lösenordet är "bolt" som standard.

Om du har använt din Pi tidigare och bytt plats på mikro-SD-kortet kommer du att få detta felmeddelande:

![image](assets/17.jpeg)

Det du behöver göra är att navigera till var "known_hosts"-filen finns och ta bort den. Det är säkert att göra det. Felmeddelandet visar sökvägen. För mig var det /Användare/MittAnvändarnamn/.ssh/

Glöm inte punkten före ssh, det indikerar att det är en dold mapp.

Försök sedan ssh-kommandot igen.

Den här gången kommer du att se denna utmatning:

![image](assets/18.jpeg)

Filen du raderade har raderats och du lägger till ett nytt fingeravtryck. Skriv ja och <enter>.

Du kommer att bli ombedd att ange lösenordet. Det är "bolt".
Du har nu terminalåtkomst till MyNode Pi, utan en skärm, och kan bekräfta att allt har laddats in korrekt.
![image](assets/19.jpeg)

## Åtkomst via webbläsaren

Öppna en webbläsare. Det måste vara en dator i ditt hemnätverk, du kan inte göra detta utifrån. Det finns ett sätt, men det är svårt. Jag har inte testat det.

Skriv in IP-adressen i webbläsarens adressfält. Detta kommer att hända:

![image](assets/20.jpeg)

Ange lösenordet "bolt" - ändra det senare.

Då kommer detta att hända:

![image](assets/21.jpeg)

Välj "Format Drive"

![image](assets/22.jpeg)

Nu väntar vi.

Vid något tillfälle kommer du att bli ombedd om du vill ange din produktnyckel eller använda den gratis "community edition" - jag kommer att visa Premium-utgåvan. Jag rekommenderar att betala för premiumversionen om du har råd, det är verkligen värt det.

![image](assets/23.jpeg)

Du kommer sedan att se framsteg för nedladdade block. Det tar dagar:

![image](assets/24.jpeg)

Det är säkert att stänga av maskinen under nedladdningen om du behöver det. Gå till inställningar och hitta knappen för att stänga av maskinen. Dra inte bara ut sladden, du kan korrumpera installationen eller hårddisken.

Se till att tidigt gå till "Inställningar" och inaktivera quicksync. Det kommer att börja nedladdningen av de initiala blocken från början.

![image](assets/25.jpeg)

Jag ville fortsätta med att skapa guiden, så här är en annan MyNode som jag förberett tidigare. Så här ser sidan ut när blockkedjan är synkroniserad och flera "appar" har aktiverats och synkroniserats:

![image](assets/26.jpeg)

Observera att Electrum Server också måste synkroniseras, så så snart Bitcoin-blockkedjan är synkroniserad, klicka på knappen för att starta den processen - tar en eller två dagar. Allt annat aktiveras inom några minuter när du väljer att aktivera det. Du kan klicka på saker och utforska. Du kommer inte att förstöra något. Om något går sönder (detta hände mig, men jag tror att det berodde på att jag hade billiga delar) måste du återflasha och börja ladda ner igen. Problemet jag har med MyNode är att om du behöver "återflasha" måste du börja synkronisera blockkedjan igen från början. Det finns tekniska sätt att komma runt detta, men det är inte enkelt.

Om du också vill prova en annan nod, som till exempel en RaspiBlitz, behöver du en extra extern SSD-hårddisk och ett annat micro SD-kort att flasha. Annars är det samma utrustning, du kan bara inte köra MyNode och RaspiBlitz samtidigt, uppenbarligen. Om du vill göra det, är det dags att köpa en annan Raspberry Pi.

Nu när du har en nod igång, använd den, låt den inte bara sitta där och inte göra något för dig. Följ min artikel (och video) om hur du ansluter din Electrum Desktop Wallet till Electrum Server och Bitcoin Core här.