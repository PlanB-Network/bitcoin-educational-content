# RaspiBlitz

RaspiBlitz är en gör-det-själv Lightning Node (LND och/eller Core Lightning) som körs tillsammans med en Bitcoin-Fullnode på en RaspberryPi (1TB SSD) och en fin display för enkel installation och övervakning.

RaspiBlitz är främst avsett för att lära sig hur man kör sin egen nod decentraliserat hemifrån - för att: Inte din nod, inte dina regler. Upptäck och utveckla det växande ekosystemet för Lightning-nätverket genom att bli en fullständig del av det. Bygg det som en del av en workshop eller som ett helgprojekt själv.

# Parman's Raspiblitz installationsguide

Raspiblitz är en utmärkt system för att köra en Bitcoin-nod och tillhörande appar. Jag rekommenderar detta och My Node-noden till de flesta användare (ha två noder för redundans om möjligt). En stor fördel är att Raspiblitz-noden är "Fri och öppen källkod", till skillnad från MyNode eller Umbrel. Varför är det viktigt? Vlad Costa förklarar. Du kan också köra RaspbiBlitz med en WiFi-anslutning istället för Ethernet - här är en tilläggsanvisning för det. (Jag har inte hittat ett sätt att göra detta med MyNode).

Du kan köpa en färdig nod med en bifogad miniskärm, eller så kan du bygga den själv (du behöver inte en skärm).

Guiden på GitHub-sidan är utmärkt, men kanske för detaljerad för en måttligt erfaren användare. Mina instruktioner kommer att vara mer kortfattade och förhoppningsvis lättare att följa.

I stort sett är processen mycket lik processen för att konfigurera en MyNode-nod med en Raspberry Pi 4. Raspiblitz-guiden föreslår att du köper en skärm, men du behöver verkligen inte en, och jag skulle inte rekommendera det. Du behöver inte ens ett extra tangentbord eller en mus. Använd bara enhetens terminalmeny via en dator i samma hemnätverk och använd ssh-kommandot med terminalen. Detta är möjligt med Linux/Mac (enkelt) och lite svårare med Windows.

## Steg 1: Köp utrustningen.

Du behöver exakt samma utrustning som du behöver för att köra en MyNode-nod. Du kan prova antingen den ena eller den andra, den enda skillnaden är datan på micro SD-kortet.

- Raspberry Pi 4, 4 GB minne eller 8 GB (4 GB är tillräckligt)
- Officiell Raspberry Pi-strömadapter (Mycket viktigt! Köp inte generiskt, allvarligt talat)
- Ett skal för Pi (FLIRC-skalet är fantastiskt. Hela skalet fungerar som en värmesänka och du behöver inte en fläkt, vilket kan vara bullrigt)
- 32 GB microSD-kort (du behöver ett, men några är praktiska)
- Ett minneskortläsare (de flesta datorer har inte en plats för ett microSD-kort).
- Extern SSD 1TB hårddisk.
- En Ethernet-kabel (för att ansluta till din hemrouter).

Du behöver inte en skärm (eller tangentbord eller mus)

Observera: Detta är fel typ av hårddisk: Detta är en bärbar extern hårddisk. Det är inte en SSD. SSD är avgörande. Detta är varför den är billig (Pris i AUD)

Detta är rätt typ att få:

Detta är snabbare, men onödigt dyrt:

## Steg 2: Ladda ner Raspiblitz-bild
Navigera till Raspiblitz github-webbplatsen och hitta länken "ladda ner bild":
![image](assets/4.png)

SHA-256 hashvärdet för den nedladdade filen finns på webbplatsen. Det kommer att ändras vid varje uppdatering. Om du inte förstår vad detta handlar om, borde du göra det, så jag har skrivit en guide som du kan läsa här.

![image](assets/5.png)

## Steg 3: Verifiera bilden

Innan du fortsätter, om du inte känner dig bekant med filsystemet på kommandoraden, är det lätt att lära sig och du borde göra det.

Här är en användbar video för Linux, men den gäller även för Mac.

För Windows finns här en enkel handledning.
Mac/Linux

Vänta tills nedladdningen är klar (viktigt!), och öppna sedan terminalen, navigera till platsen där du laddade ner filen och skriv följande kommando...

```bash
shasum -a 256 xxxxxxxxxxxxxx
```

där xxxxxxxxxxxxxx är namnet på filen du just laddade ner. Om du inte är i mappen där filen finns måste du skriva hela sökvägen.

Datorn tänker i cirka 20 sekunder. Kontrollera att hashvärdet i utdatafilen matchar det som laddades ner från webbplatsen i föregående steg. Om de är identiska kan du fortsätta.
Windows

Öppna kommandotolken och navigera till platsen där filen är nedladdad, och skriv följande kommando:

```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```

där xxxxxxxxxxxxxx är namnet på filen du just laddade ner. Om du inte är i mappen där filen finns måste du skriva hela sökvägen.

Datorn tänker i cirka 20 sekunder. Kontrollera att hashvärdet i utdatafilen matchar det som laddades ner från webbplatsen i föregående steg. Om de är identiska kan du fortsätta.

## Steg 4: Flasha SD-kortet

Du kan använda Balena Etcher för att göra detta. Ladda ner det här.

Etcher är självförklarande att använda. Sätt in ditt micro SD-kort och flasha Raspiblitz-programvaran (.img-filen) på SD-kortet.

![image](assets/6.png)

![image](assets/7.png)

![image](assets/8.png)

![image](assets/9.png)

När det är klart kan enheten inte längre läsas. Du kan få ett fel från operativsystemet och enheten ska försvinna från skrivbordet. Dra ut kortet.

## Steg 5: Konfigurera Pi och sätt in SD-kortet

Delarna (hölje visas inte):

![image](assets/10.png)

![image](assets/11.png)

Anslut ethernet-kabeln och USB-anslutningen för hårddisken (inte ström ännu). Undvik att ansluta till de blå färgade USB-portarna i mitten. De är USB 3. Använd USB 2-porten, även om enheten kan vara USB 3-kompatibel (mer pålitlig).

![image](assets/12.png)

Micro SD-kortet sätts in här:

![image](assets/13.png)

Slutligen, anslut strömmen:

![image](assets/14.png)

## Steg 6: Hitta IP-adressen för Pi

Du behöver aldrig en skärm med Raspiblitz. Du behöver dock en annan dator i hemnätverket. Om din Pi inte är ansluten via ethernet och du vill använda WiFi, krävs vissa datorfärdigheter för att hitta IP-adressen. Kan inte hjälpa dig, tyvärr. Du behöver en ethernet-anslutning. (Problemet uppstår från att behöva ha tillgång till en skärm och operativsystemet för att ansluta till WiFi och ange ett lösenord.)

Kontrollera din router för en lista över alla IP-adresser för alla anslutna enheter.
Jag skrev 192.168.0.1 i webbläsaren (instruktioner som följde med min router), loggade in och kunde se min enhet med IP-adressen 192.168.0.191. Observera att dessa IP-adresser inte är synliga för internet (de går genom routern först), de är bara identifierare för enheter i ditt hemnätverk.
Att hitta IP-adressen är avgörande.

> UPPDATERING: Du kan använda terminalen på en Mac- eller Linux-dator för att hitta IP-adressen för alla enheter som är anslutna via Ethernet i hemnätverket med hjälp av kommandot "arp -a". Utdata är inte lika snygg som vad routern visar, men all information du behöver finns där. Om det inte är uppenbart vilken enhet som är Pi, prova och fel.

## Steg 7: SSH till Pi

Kom ihåg att sätta in SD-kortet i Pi innan du slår på den. Vänta några minuter och öppna sedan terminalen på en annan Linux/Mac-dator.

För Mac/Linux, skriv följande i terminalen:

```bash
ssh admin@Pi:ets_IP-adress
```

För Windows måste du installera Putty för att SSH:a till Pi. Skriv samma kommando som ovan.

Första gången du gör detta, eller varje gång du byter operativsystem på Pi genom att byta SD-kort, kan du få följande felmeddelande...

![image](assets/15.png)

För att åtgärda det, navigera till platsen där filen "known_hosts" finns (det står i felmeddelandet) och ta bort den. Kommandot är "rm known_hosts".

Sedan upprepar du SSH-kommandot för att logga in. Detta kommer att hända...

![image](assets/16.png)

Skriv "yes" (utan citationstecken) för att fortsätta.

Om det lyckas kommer du att bli ombedd att ange ett lösenord. Detta är inte för din dator, utan för raspiblitz. Det generiska lösenordet är "raspiblitz", och du kommer att ändra det senare. Terminalfönstret blir blått och du får menyalternativ som de gamla DOS-menyerna. Navigera med piltangenterna eller musen.

![image](assets/17.png)

Följ anvisningarna, ange dina lösenord och sedan kommer den att upptäcka din hårddisk och ge dig möjlighet att formatera den om det behövs.

Sedan kommer du att bli tillfrågad om du vill kopiera blockkedjedata från en annan källa eller ladda ner det igen. Att kopiera det är en läroprocess och instruktionerna är ganska bra och bra att ha till hands...

![image](assets/18.png)

Det enkla men långsammare sättet är att ladda ner hela kedjan från början...

![image](assets/19.png)

Massor av text kommer att flimra över terminalskärmen. Du kan missta det för processen med att ladda ner blockkedjan, men det ser ut som att den genererar en privat nyckel för kommunikation.

Sedan visas blixtalternativ.

![image](assets/20.png)

Skapa ett nytt lösenord för att låsa din blixtplånbok, sedan kommer en ny plånbok att skapas och du kommer att få 24 ord att skriva ner...

![image](assets/21.png)

Se till att du skriver ner och förvarar dem säkert. Jag har hört talas om en person som inte gjorde det eftersom han inte planerade att använda blixt, men sedan ett år senare bestämde sig för att använda det och öppnade kanaler. Då insåg han att hans ord inte var säkerhetskopierade och jag minns att det inte var möjligt att extrahera orden igen från enheten, så han var tvungen att stänga alla sina kanaler och börja om. Han klarade sig, men andra kanske inte är lika lyckligt lottade.

Efter detta kommer några minuter av text att rulla ner i terminalfönstret. Sedan...

![image](assets/22.png)
Du kommer att loggas ut från ssh-sessionen. Logga in igen, denna gång med ditt nya lösenord, lösenord A. När du är inloggad kommer du att bli ombedd att ange lösenord C för att låsa upp din lightning-plånbok.
Nu väntar vi. Vi ses om 2 veckor. Du kan stänga terminalen, den påverkar inte Pi, det är bara ett kommunikationsfönster.

![image](assets/23.png)

Om du av någon anledning vill stänga av Pi innan blockkedjan har laddats ner helt, är det okej så länge du gör det på rätt sätt. Blockkedjan kommer att fortsätta laddas ner där den slutade när du ansluter igen.

Tryck på CTRL+c för att avsluta den blå skärmen. Du kommer att komma åt Pi:s Linux-terminal. Här kan du skriva "menu" för att ladda följande skärm, och därifrån kan du stänga av Pi.

![image](assets/24.png)

SLUT på guiden

Så från och med nu är din nod redo att användas. Om du behöver hjälp med att navigera bland fler alternativ, hänvisa till github för fler handledningar och guider https://github.com/raspiblitz/raspiblitz#feature-documentation