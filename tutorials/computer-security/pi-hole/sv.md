---
name: Pi-Hole
description: En annonsblockerare för hela ditt nätverk
---
![cover](assets/cover.webp)



___



*Denna handledning är baserad på originalinnehåll av Florian Duchemin publicerat på [IT-Connect](https://www.it-connect.fr/). Licens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Ändringar kan ha gjorts i originaltexten.*



___



## I. Presentation



Vi har alla gjort det så snart vi startar upp vår favoritwebbläsare: installera en **adblocker** (annonsblockerare). Men när du använder TV-webbläsaren eller en Android-enhet etc ... Det är lite knepigare att hitta något som fungerar. Och om det finns mer än en enhet i huset, ja, då måste du upprepa operationen för varje webbläsare!



I den här handledningen ska vi lösa ett enkelt problem**: tillhandahålla en annonsblockerare till alla maskiner i vårt nätverk och hantera den centralt.**



För att göra detta kommer vi att använda ett verktyg som utvecklats för detta ändamål: **Pi-hål**



Pi-Hole är ett DNS-sänkhål. Den använder de DNS-förfrågningar som görs av dina enheter för att validera eller neka trafik och skyddar dig därmed från adresser och domäner som är kända för att distribuera reklam, skadlig kod och så vidare.



DNS står för Domain Name System. Så vad är ett domännamn? Tja, "it-connect.fr" är bara ett exempel. Ett domännamn är en unik identifierare för en eller flera resurser, som vanligtvis administreras av en enda enhet.



Maskinens namn plus domännamnet kallas FQDN för *Fully Qualified Domain Name*. Det gör att du kan nå en viss maskin bara genom att "ringa" den. När du t.ex. skriver "www.trucmachin.com" ringer du faktiskt upp maskinen "www", som tillhör domänen "trucmachin.com".



Men våra datorer förstår inte mänskligt språk, allt de förstår är binärt, så de behöver en IP Address, som motsvarar ett telefonnummer, för att nå webbplatsen.



Så varje gång du anger namnet på en webbplats i din webbläsare eller klickar på en länk, frågar din dator först en DNS-server efter den IP Address som motsvarar namnet.



**Pi-Hole kommer sedan att inspektera dessa förfrågningar (det finns hundratals varje dag!) och automatiskt blockera dem som är kända för att vara värd för reklam eller till och med skadliga filer



## II. Installera Pi-Hole



Med ett namn som Pi-Hole kan man med rätta anta att man behöver en Raspberry-Pi... Men det är inte riktigt sant. **Pi-Hole kan installeras på vilken Linux-dator som helst (Debian, Fedora, Rocky, Ubuntu, etc.)



Å andra sidan måste du komma ihåg att **den här enheten måste köras 24 timmar om dygnet av en enkel anledning: ingen DNS, inget Internet!** Raspberry är därför en bra idé, eftersom den nästan inte förbrukar någon energi.



För att installera ansluter du bara till din Linux-maskin via SSH och anger följande kommando som "*root*":



```
curl -sSL https://install.pi-hole.net | bash
```



> **Note**: Under normala omständigheter är det inte tillrådligt att "hacka" ett skript utan att först veta vad det gör. Om du är osäker kan du gå till sidan med en webbläsare eller ladda ner innehållet som en fil.
>


> **Note: På minimala versioner av Debian 11 är Curl inte installerat, så du måste installera det manuellt med kommandot **apt-get install curl** innan du skriver ovanstående kommando.

När skriptet har körts kommer en rad tester att utföras och själva installationen sköter sig själv:



![Image](assets/fr/019.webp)



Installera Pi-Hole



När installationen är klar kommer du till den här skärmen:



![Image](assets/fr/020.webp)



Startskärm för Pi-Hole



> **Note**: Om du använder DHCP på din maskin får du ett varningsmeddelande om detta. För korrekt användning rekommenderar vi naturligtvis starkt att du tilldelar en fast IP till din maskin.

Efter den här skärmen får du några informationsmeddelanden och sedan kommer du till konfigurationsguiden, som först frågar dig vilken DNS-server Pi-Hole ska vidarebefordra förfrågningar till. För min del har jag valt Quad9, som har en stadga för användarintegritet.



![Image](assets/fr/021.webp)



Val av DNS - Pi-Hole



> **Om du arbetar på ett företag är det troligt att din nuvarande DNS-server är Active Directory-domänkontrollanten. Men oroa dig inte, du kan senare ange en villkorlig omdirigering för en domän som du själv väljer. Vanligtvis kan du omdirigera alla förfrågningar som rör din lokala domän till din DNS-server.

Du kommer att märka att vissa val inkluderar ett DNSSEC-alternativ. I grund och botten är DNS-protokollet inte säkert (det utformades inte med detta i åtanke vid den tiden). DNSSEC löser detta problem genom att lägga till en Layer av säkerhet genom kryptering och signering av utbyten, vilket förklaras i motsvarande artikel: [DNS-säkerhet](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Alla annonsblockerare förlitar sig på en eller flera listor för att göra sitt jobb. Pi-Hole levereras med en enda lista som standard, så välj den och lägg till fler senare.



![Image](assets/fr/022.webp)



Kom frågan om Interface-webben, dess installation är valfri, eftersom verktyget har sin egen kommandorad för hantering och visualisering. Men den här Interface är ganska trevlig och välgjord, så jag rekommenderar att du installerar den samtidigt:



![Image](assets/fr/023.webp)



Om du installerar Pi-Hole på en maskin som redan har en webbserver kan du svara "nej" på följande fråga. Observera dock att PHP och flera moduler krävs för att detta ska fungera. Annars kommer **lighttpd att installeras med alla nödvändiga moduler**.



![Image](assets/fr/024.webp)



Du får sedan frågan om du vill registrera DNS-förfrågningar. **Om du vill spara en historik ställer du in detta på ja, annars ställer du in detta på nej, men då förlorar du en del av funktionaliteten** (se nästa skärm).



![Image](assets/fr/025.webp)



För sin Interface-webb använder Pi-Hole en egen funktion som heter FTLDNS, som tillhandahåller ett API och genererar statistik från DNS-förfrågningar. Den här funktionen kan innehålla ett "sekretessläge" som maskerar de domäner som begärs, kunderna bakom begäran eller båda. Praktiskt om du vill göra övervakning utan att kränka människors integritet, eller helt enkelt om du vill följa relevanta bestämmelser vid användning i ett offentligt nätverk.



![Image](assets/fr/026.webp)



Val av privat livsstil



När den sista frågan har besvarats kommer skriptet att göra vad det ska: ladda ner GitHub-repositorierna och konfigurera Pi-Hole. I slutet av installationen visas en sammanfattningsskärm med viktig information:



![Image](assets/fr/027.webp)



Skärmbild för installationssammanfattning



Anteckna Interface:s webblösenord och nätverksinformation. Nu är det dags att konfigurera DHCP-tjänsten på vår nuvarande plats.



## III. DHCP-konfiguration



För att fungera måste Pi-Hole "lösa" DNS-förfrågningar från klienter, så att de vet att det är till den de ska skicka dem. Det finns flera sätt att göra detta på:





- Ändra DNS-inställningarna i din DHCP-server (t.ex. din Box)
- Inaktivera den här servern och använd den som tillhandahålls av Pi-Hole
- Ändra varje enhet manuellt så att den använder Pi-Hole som DNS



Jag väljer personligen den första lösningen. Chansen är stor att **du har en DHCP-server där du är** (vanligtvis din box). Så det finns ingen anledning att bry sig.



Eftersom det finns ett stort antal möjligheter, mellan de olika operatörernas boxar (som jag inte känner till alla) och de som har sin egen router, kommer jag inte att tillhandahålla en skärmdump för dessa modifieringar. I vilket fall som helst måste du gå till DHCP-inställningarna och ändra "DNS"-parametern så att den inkluderar IP Address för din Pi-Hole.



När detta har gjorts, om några enheter har slagits på tidigare, kommer de att ha behållit de gamla inställningarna, så du måste starta om konfigurationsbegäran.



På Windows-arbetsstationer, med en kommandotolk:



```
ipconfig /renew
```



På en Linux-arbetsstation:



```
dhclient
```



För alla andra enheter gäller att de måste stängas av och sättas på igen.



Så de bör få rätt parametrar för att kontrollera:



```
ipconfig /all
```



I DNS-fältet ska du ha Address för din Pi-Hole, i mitt fall 192.168.1.42:



![Image](assets/fr/029.webp)



## IV. Användning av Interface web Pi-Hole



För att underlätta administrationen har **Pi-Hole** en väl utformad Interface webb Interface. Den är användarvänlig och tillgänglig och låter dig:





- Se antalet förfrågningar, blockerade förfrågningar etc. i realtid.
- Hantera din vitlista och svartlista
- Lägg till statiska poster, alias etc.
- Lägg till listor
- Och många andra funktioner!



För egen del kommer jag att lägga till en blockeringslista. Som nämnts ovan installerades endast en lista samtidigt som Soft. Det finns många listor för annonssajter, men det är bäst att välja minst en som är specifik för det land du bor i. En av de mest kända listorna är **EasyList**, och en av dem är specifik för Frankrike: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



För att lägga till det, anslut först till Interface-admin: **http://<ip_du_PiHole>/admin**



Administratörslösenordet har redan genererats (se skärmdump efter avslutad installation), så du behöver bara ange det för att komma åt Interface:



![Image](assets/fr/030.webp)



Interface från Pi-Hole



Vi kan t.ex. se att det finns två kunder anslutna till Pi-Hole, att den har behandlat 442 förfrågningar och att 8 av dessa har blockerats. Dessa grafer kan vara en bra informationskälla, särskilt i ett professionellt sammanhang.



För att lägga till vår lista, gå till menyerna "**Group Management**" och "**Adlists**":



![Image](assets/fr/031.webp)



Vi kan se vår första lista "**StevenBlack**", för att lägga till vår kopierar du länken jag gav dig ovan och infogar den i fältet "**Address**", för beskrivningen väljer jag att sätta namnet på listan:



![Image](assets/fr/032.webp)



Lägga till en lista i Pi-Hole



Allt som återstår är att klicka på "**Add**" för att lägga till den. För att aktivera det måste vi utföra ytterligare ett steg för att "varna" Pi-Hole för att ta över den här listan. För att göra detta:





- Använd antingen den inbyggda kommandoraden
- Antingen Interface-webben



Jag valde personligen det andra alternativet, för om du har tittat noga så finns länken till PHP-skriptet som utför uppdateringen direkt på sidan vi är på (ordet "online"). Så allt du behöver göra är att klicka på den, vilket kommer att ta dig till en sida med bara ett alternativ:



![Image](assets/fr/033.webp)



När skriptet är klart visas resultatet på sidan, vilket innebär att listan har tagits med i beräkningen (om inte ett felmeddelande visas, förstås).



Som meddelades i början av denna handledning låter Pi-Hole dig också **blockera domäner som är kända för att distribuera skadlig kod. För att förstärka denna funktion föreslår jag att du också lägger till den regelbundet uppdaterade domänlistan som distribueras av Abuse.ch**, vilket kommer att stärka säkerheten i ditt nätverk avsevärt, tillgänglig på [this Address] (https://urlhaus.abuse.ch/downloads/hostfile/).



Du kan naturligtvis lägga till alla listor som du tycker är relevanta eller hantera din svarta lista manuellt via menyn för svarta listor.



## V. Pi-Hole-test



Nu när allt är på plats behöver du bara testa lösningen för att se till att den fungerar som den ska.



Jag kommer till exempel att försöka nå domänen *http://admin.gentbcn.org/* som finns på listan Abuse.ch eftersom den är känd för att hysa skadlig kod:



![Image](assets/fr/034.webp)



Uppenbarligen har jag blivit blockerad någonstans. För att vara säker på att det är Pi-Hole som har gjort jobbet kan vi kontrollera frågeloggen i Interface-webben "Query Log" för att se att det är en blockering från en listpost:



![Image](assets/fr/035.webp)



## VI. Slutsatser



I den här handledningen har vi visat hur du ställer in en DNS-server som inte bara eliminerar de flesta annonser för din surfkomfort, utan också lägger till **en Layer av säkerhet genom att blockera nätfiske och domäner som sprider skadlig kod**.



Allt är kostnadsfritt och ekonomiskt om det installeras på en Raspberry-Pi (när det gäller strömförbrukning).