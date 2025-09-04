---
name: Mullvad Browser
description: Så här använder du Mullvad Browser för att skydda din integritet
---

![cover](assets/cover.webp)



I en värld där digital övervakning blir allt vanligare har det aldrig varit viktigare att skydda din integritet på nätet. Företag använder sofistikerade tekniker för att spåra dig:





- Tredjepartscookies**: små filer som deponeras av externa webbplatser för att följa dig från en webbplats till en annan
- Fingerprinting**: samlar in unika egenskaper hos din webbläsare och enhet (skärmupplösning, installerade teckensnitt, plugins etc.) för att identifiera dig utan cookies
- Spårningsskript**: osynliga JavaScript-koder som analyserar ditt surfbeteende (klick, skrollning, spenderad tid)
- IP Address-analys**: geografisk plats och identifiering av din internetleverantör



Dessa uppgifter kombineras sedan för att skapa detaljerade profiler av ditt beteende på nätet och genererar intäkter, ofta utan att du vet om det. Denna verklighet väcker en grundläggande fråga: hur kan du surfa på Internet samtidigt som du bevarar din anonymitet och sekretess?



Svaret ligger till stor del i ditt val av webbläsare. Detta verktyg, som vi använder varje dag för att få tillgång till information, göra inköp eller kommunicera, spelar en avgörande roll när det gäller att skydda våra personuppgifter. Tyvärr är populära webbläsare som Google Chrome (som har cirka 65% av den globala marknaden) utformade kring affärsmodeller som bygger på massiv insamling av användardata.



![MULLVAD BROWSER](assets/fr/01.webp)


*Mullvad Browser utmärker sig för sin exceptionellt effektiva blockering av spårare, som vida överträffar konsumentwebbläsare*



Inför denna utmaning dyker det upp nya aktörer med en annan filosofi: att sätta integriteten i centrum för sin design. Bland dem utmärker sig Mullvad Browser som en innovativ lösning som kombinerar det bästa integritetsskyddet med en smidig och tillgänglig surfupplevelse.



Till skillnad från traditionella webbläsare som försöker anpassa din upplevelse genom att samla in dina uppgifter, väljer Mullvad Browser det motsatta tillvägagångssättet: att få alla sina användare att se identiska ut på webbplatser, vilket gör individualiserad spårning praktiskt taget omöjlig.



I den här handledningen kommer vi tillsammans att upptäcka hur Mullvad Browser kan förändra hur du surfar på Internet, vilket ger dig ett robust skydd mot övervakning utan att offra användarvänligheten.




## Vi presenterar Mullvad Browser



**Mullvad Browser** är en integritetsfokuserad webbläsare som utvecklats i samarbete med Tor-projektet och distribueras gratis av det svenska företaget Mullvad VPN. Den lanserades i april 2023 och presenterar sig själv som en ** "Tor Browser utan Tor-nätverket"**, utformad för att minimera spårning och fingeravtryck online samtidigt som användare kan surfa via ett betrott VPN snarare än Tor-nätverket.



Mullvad Browser är en gratis webbläsare med öppen källkod som bygger på Firefox ESR (den långlivade versionen av Mozilla Firefox) och som har förstärkts av experter från Tor Project. Konkret innebär det att den innehåller de flesta **skyddsfunktionerna i Tor Browser**, men **dirigerar inte trafiken via Tor-nätverket**. Istället kan (och bör) användare länka den till ett betrott krypterat VPN för att anonymisera sin IP Address.



När det gäller användarupplevelsen liknar Mullvad Browser en klassisk webbläsare och erbjuder flytande navigering. Den är tillgänglig kostnadsfritt på Windows, macOS och Linux (ingen mobilversion). Du behöver inte vara en Mullvad VPN-prenumerant för att använda den, men ** att använda Mullvad Browser utan att maskera din IP ger inte fullständig anonymitet** - så det rekommenderas starkt att använda den tillsammans med ett pålitligt VPN.



### Mål: integritet och antispårning



Webbläsaren Mullvad har utformats med ett huvudmål i åtanke: **skydda användarnas integritet** på nätet och motverka vanliga spårnings- och profileringstekniker. Dess huvudsakliga mål inkluderar:





- Drastiskt minska annonsspårning och spårning** av webbplatser och reklambyråer. Som standard blockerar Mullvad Browser tredjepartsspårare, spårningscookies och fingeravtrycksskript som kan identifiera dig.





- Standardisera din webbläsares fingeravtryck** för att **"smälta in i mängden"**. Fingeravtrycket är som ett unikt "identitetskort" som skapas genom att kombinera alla egenskaper hos din webbläsare. Mullvad Browser ser till att alla dess användare har exakt samma "identitetskort", vilket gör det omöjligt att skilja dem åt individuellt.





- Erbjuder omedelbart skydd utan ytterligare tillägg**. Mullvad Browser levereras i en konfiguration som är "klar att använda": användaren behöver inte installera en rad tillägg eller ändra några inställningar för att skyddas.





- Gör inte avkall på prestanda eller ergonomi** mer än nödvändigt. I avsaknad av Tor-routing erbjuder Mullvad Browser mycket snabbare surfning än Tor Browser, vilket närmar sig prestandan för en standardwebbläsare i kombination med ett VPN.



### Viktiga funktioner i Mullvad Browser



Mullvad Browser innehåller en rad ** säkerhets- och sekretessfunktioner** direkt inspirerade av Tor Browser:





- Privat surfning hela tiden:** Läget för privat surfning är aktiverat som standard och kan inte avaktiveras. **Ingen historik, cookies eller cache lagras från en session till nästa**. Så snart du stänger Mullvad Browser raderas all surfdata.





- Förbättrat skydd mot fingeravtryck:** Webbläsaren tillämpar strikta inställningar för att motverka digitala fingeravtryck. Detta inkluderar:
 - Standardisering av användaragent** och webbläsarversion
 - Tidszon inställd på UTC** för alla användare
 - Letterboxing**: en teknik som automatiskt lägger till gråa marginaler runt webbsidor för att standardisera visningsstorleken och förhindra identifiering av dina skärmdimensioner
 - Blockera API:er för fingeravtryck**: Teknikerna Canvas (2D-ritning), WebGL (3D-grafik) och AudioContext (ljudbearbetning) är inaktiverade eftersom de kan avslöja unika detaljer om din maskinvara
 - Standardiserade systemteckensnitt** för att undvika identifiering av installerade teckensnitt





- Blockering av spårare och reklam:** Mullvad Browser integrerar naturligt tillägget **uBlock Origin** (förinstallerat) med ytterligare skyddslistor för att blockera **spårare från tredje part, reklamskript och annat skadligt innehåll**. Detta skydd åtföljs av **First-Party Isolation**: en teknik som lagrar cookies i separata "krukor" för varje webbplats, vilket förhindrar en webbplats från att läsa cookies som deponerats av en annan.





- Återställningsknapp för session:** Precis som Tor Browser har en "Ny identitet"-knapp erbjuder Mullvad Browser en knapp för att **snabbt starta om webbläsaren med en ny, tom session**.





- Justerbara säkerhetsnivåer:** Du kan justera säkerhetsnivån (*Normal*, *Safer*, *Safest*) i inställningarna, precis som i Tor Browser.



## Inbyggda tillägg som standard



Mullvad Browser innehåller **tre förinstallerade tillägg** som utgör kärnan i dess antispårningsskydd. **Det är viktigt att aldrig ta bort dem eller ändra deras konfigurationer**, eftersom det skulle göra dig unik bland Mullvad Browser-användare:



### **uBlockera ursprung**


Detta tillägg för blockering av annonser och spårare kommer förkonfigurerat med **optimerade filterlistor** för att blockera:




- Påträngande reklam
- Tredjepartsspårare som samlar in dina uppgifter
- Skadliga skript
- Beteendespårning Elements



uBlock Origin i Mullvad Browser använder standardiserade parametrar för att säkerställa att alla användare blockerar exakt samma Elements, vilket bevarar enhetligheten i digitala fotspår.



### **IngetScript**


NoScript körs i bakgrunden för att hantera webbläsarens **säkerhetsnivåer**. Denna:




- Kontrollerar JavaScript**-körning enligt vald nivå (Normal/Most Secure/Most Secure)
- Filtrerar automatiskt bort XSS**-attacker (Cross-Site Scripting)
- Blockerar farligt** aktivt innehåll på icke-HTTPS-webbplatser
- Dess ikon är dold som standard, men kan visas via "Anpassa verktygsfältet"



### **Mullvad Browser** tillägg


Detta Mullvad-specifika tillägg erbjuder olika funktioner beroende på om du är en Mullvad VPN-kund eller inte:



#### **Utan Mullvad VPN-prenumeration:**




- Grundläggande anslutningskontroll**: visar din aktuella offentliga IP och viss anslutningsinformation
- Integritetsrekommendationer**: tips om hur du kan förbättra dina säkerhetsinställningar (DNS, endast HTTPS, sökmotor)
- WebRTC**-kontroll: aktivera/inaktivera för att förhindra IP Address-läckor
- Kan raderas utan påverkan** på ditt digitala fotavtryck om du inte använder Mullvad VPN



#### **Med Mullvad VPN-abonnemang: **


Tillägget avslöjar sin fulla potential med avancerade funktioner:





- Integrerad SOCKS5-proxy**: anslutning med ett klick till Mullvad VPN-serverproxy
 - Fast IP Address**: till skillnad från ett VPN, som kan ändra sin IP Address, garanterar en proxy alltid samma utdata Address
 - Automatisk kill switch**: om VPN kopplas bort blockeras webbläsartrafiken omedelbart
 - Stöd för IPv6**: IPv6-anslutning även om din VPN-anslutning inte har det aktiverat





- Multihop (dubbel VPN)**: möjlighet att ändra proxyposition för att skapa en tunnel i tunneln
 - Din trafik passerar först genom din VPN-server och "hoppar" sedan till en annan Mullvad-server
 - Använd en annan lokalisering endast för webbläsaren





- Avancerad anslutningsövervakning**: realtidsövervakning av din VPN-status, ansluten server och upptäckt av DNS-läckage





- Tillgång till Mullvad Leta**: privat sökmotor reserverad för abonnenter (rekommenderas dock inte av Mullvad på grund av korrelation med ditt konto)



Dessa tre tillägg arbetar tillsammans för att skapa ett sammanhängande ekosystem av skydd, där varje användare drar nytta av exakt samma försvar utan möjlighet till anpassning som skulle äventyra den kollektiva anonymiteten.



## Fördelar och nackdelar med Mullvad Browser



### Fördelar





- Utmärkt integritetsskydd som standard:** Mullvad Browser tillämpar mycket strikta integritetsinställningar redan från början, utan behov av manuell konfiguration.





- Bättre prestanda än Tor Browser:** I avsaknad av onion routing är Mullvad Browser **notabelt snabbare och mer responsiv** än Tor Browser för klassisk webbsökning.





- Välbekant Interface-enkelhet:** Mullvad Browser är baserad på Firefox Interface. Om du är van vid Firefox eller till och med Tor Browser kommer du inte att känna dig malplacerad.





- Pålitligt samarbete och granskad kod:** Mullvad Browser drar nytta av expertisen i Tor-projektet, och all källkod är tillgänglig för extern granskning.



### Nackdelar





- Ingen nätverksanonymitet utan VPN:** Den viktigaste punkten är att **Mullvad Browser inte döljer din IP Address av sig själv** (som alla andra webbläsare, utom Tor Browser). Din IP Address är som din "post Address" på Internet: den avslöjar din plats och din ISP. Den är därför **beroende av ett VPN** (virtuellt privat nätverk) för att dölja denna viktiga information.





- Ingen mobilversion:** Hittills är Mullvad Browser endast tillgängligt på PC (Windows, Mac, Linux).





- Oförenligt med vissa vanor:** Det **permanenta privata läget** innebär att du inte kan behålla en session från en användning till nästa. Det är omöjligt att vara ansluten till ett webbkonto från en session till en annan.





- Begränsade funktioner:** För att bevara fingeravtryckets enhetlighet har Mullvad Browser **inaktiverat flera funktioner** som finns i Firefox och är inte avsedd för anpassning.



## Installera Mullvad Browser



Mullvad Browser finns tillgängligt gratis för Windows, macOS och Linux. För att installera den, gå till [den officiella Mullvad-webbplatsen] (https://mullvad.net/browser).



![MULLVAD BROWSER](assets/fr/02.webp)



*Officiell hemsida för Mullvad Browser med nedladdningsknappen markerad *



![MULLVAD BROWSER](assets/fr/03.webp)



*Välj ditt operativsystem på nedladdningssidan för Mullvad Browser.*



Klicka på knappen **"Download"** som motsvarar ditt operativsystem.



För Linux kan du välja mellan olika format beroende på din distribution. När nedladdningen är klar:



### På Windows


Kör den nedladdade filen `.exe` och följ installationsanvisningarna.



### På macOS


Öppna den nedladdade filen `.dmg` och dra programmet Mullvad Browser till mappen Program.



### På Linux


Extrahera arkivet `.tar.xz` till den katalog du väljer och kör filen `start-mullvad-browser.desktop`.



## Konfiguration och första användning



När du först startar Mullvad Browser ser du en Interface som liknar den i Tor Browser. Webbläsaren är förkonfigurerad för integritet och kräver inga speciella ändringar.



![MULLVAD BROWSER](assets/fr/04.webp)



*Interface Mullvad Browser-hemsida med tillägg, kvastikon till generate en ny identitet och applikationsmeny längst upp till höger.*



**Viktigt:** Mullvad Browser maskerar inte din IP Address som standard. För fullständigt skydd rekommenderar vi starkt att du använder ett VPN parallellt. Du kan använda Mullvad VPN eller någon annan betrodd VPN-tjänst.



Webbläsaren innehåller också **DNS-over-HTTPS (DoH)** med hjälp av Mullvads DNS-tjänst: denna teknik krypterar dina DNS-förfrågningar (översätter webbplatsnamn till IP-adresser) för att förhindra att din internetleverantör övervakar de webbplatser du besöker.



### Säkerhetsinställningar



Du kan justera säkerhetsnivån genom att klicka på **applikationsmenyn** (tre horisontella staplar) längst upp till höger, sedan **"Inställningar"** och sedan fliken **"Sekretess och säkerhet"**. Bläddra ner till avsnittet **"Säkerhet"**:



![MULLVAD BROWSER](assets/fr/05.webp)



*Val av säkerhetsnivåer: pilarna visar vägen från applikationsmenyn till fliken "Privacy & Security" till säkerhetsalternativen*



Mullvad Browser erbjuder tre säkerhetsnivåer:





- Normal** (nuvarande standardnivå): Alla webbläsar- och webbplatsfunktioner aktiverade





- Säkrare**: Inaktiverar ofta farliga webbplatsfunktioner, vilket kan leda till att vissa webbplatser inte fungerar som de ska:
 - JavaScript är inaktiverat för icke-HTTPS-webbplatser
 - Vissa teckensnitt och matematiska symboler är inaktiverade
 - Ljud och video (HTML5 media) samt WebGL är "klicka för att spela"





- Den säkraste**: Tillåter endast de webbplatsfunktioner som krävs för statiska webbplatser och grundläggande tjänster:
 - JavaScript är inaktiverat som standard för alla webbplatser
 - Vissa teckensnitt, ikoner, bilder och matematiska symboler är inaktiverade
 - Ljud och video (HTML5 media) samt WebGL är "klicka för att spela"



### Ny sessionsknapp



För att starta om med en tom session utan att stänga webbläsaren, klicka på kvastikonen eller använd applikationsmenyn > **"Ny session"**.



![MULLVAD BROWSER](assets/fr/06.webp)



*Funktionen "Återställ din identitet" för att starta om webbläsaren med en helt ny session*



## Vardaglig användning



### Normal navigering



Mullvad Browser beter sig som en klassisk webbläsare för vardagssurfning. Alla webbplatser är tillgängliga som vanligt, med den extra fördelen av förbättrat skydd mot spårning.



### Cookiehantering och inloggning



På grund av det permanenta privata läget måste du återansluta till dina konton varje gång du loggar in. Detta är priset du betalar för maximal sekretess.



### Tillägg



Mullvad Browser låter dig tekniskt sett installera ytterligare tillägg från Firefox-katalogen, men **det är viktigt att förstå konsekvenserna**. Varje tillägg ändrar ditt digitala fotavtryck och skiljer dig från andra Mullvad Browser-användare, vilket strider mot webbläsarens grundläggande princip: att få alla användare att framstå som identiska.



Som Mullvad förklarar: *"Ibland är det bättre att inte ha något specifikt försvar än att ha ett. Genom att vilja öka integriteten på nätet installerar du tillägg som i slutändan gör dig ännu mer synlig. "*



Om du ändå väljer att installera tillägg bör du vara medveten om att du skapar ett unikt fingeravtryck som kan användas för att spåra dig från webbplats till webbplats. För maximalt skydd är det bäst att hålla sig till de tre förinstallerade tilläggen, som är identiska för alla användare.



## Bästa praxis med Mullvad Browser



1. **Använd alltid ett VPN: Mullvad Browser maskerar inte din IP. Ett VPN är viktigt för fullständig anonymitet.



2. **Anpassa inte webbläsaren**: Undvik att ändra inställningar eller lägga till tillägg, eftersom detta kan göra dig identifierbar.



3. **Använd knappen för ny session**: Mellan olika aktiviteter kan du använda återställningsfunktionen för att dela upp dina sessioner.



4. **Välj den säkerhetsnivå som bäst passar dina behov**:




   - Normal (rekommenderad)**: För vardagssurfning. Ger redan utmärkt skydd samtidigt som webbplatserna fortsätter att fungera. Detta är den bästa balansen för 95 % av användarna.
   - Säkrare**: Om du besöker okända eller potentiellt farliga webbplatser, eller för extra skydd på offentliga Wi-Fi-nätverk. Vissa webbplatser kan fungera felaktigt.
   - Mest säker**: Reserverad för högrisklägen (undersökande journalistik, känslig kommunikation, fientliga miljöer). De flesta moderna webbplatser kommer att vara trasiga, men det är priset för maximal säkerhet.



5. **Kontrollera regelbundet om det finns uppdateringar**: Håll din webbläsare uppdaterad med de senaste säkerhetsuppdateringarna.



6. **Använd integritetsvänliga sökmotorer**: Välj DuckDuckGo, Startpage eller Searx i stället för Google.



7. ** Aktivera endast HTTPS-läge**: I inställningarna ska du se till att läget "Endast HTTPS" är aktiverat för att tvinga fram säkra anslutningar.



8. **Ändra INTE några avancerade inställningar**: Till skillnad från andra webbläsare är Mullvad Browser utformad så att ALLA användare har exakt samma konfiguration. Att ändra inställningar i `about:config` eller ändra uBlock Origin/NoScript-inställningar skulle göra dig unik och helt upphäva webbläsarens anonymitet.



## Rekommenderad DNS-konfiguration



Mullvad Browser integrerar automatiskt Mullvad DNS-over-HTTPS. Om du använder Mullvad VPN kommer tillägget att rekommendera att du ** inaktiverar Mullvad DoH** eftersom det är snabbare att använda din VPN-servers DNS-server. Om du inte använder Mullvad VPN, behåll Mullvad DoH aktiverat för att undvika DNS-övervakning av din internetleverantör.



## Slutsats



Mullvad Browser är en utmärkt lösning för dig som vill ha en integritetsvänlig webbläsare utan Tor-nätverkets prestandabegränsningar. Kombinerat med ett VPN av hög kvalitet ger det ett robust skydd mot spårning och övervakning online.



Även om Mullvad Browser har vissa begränsningar (ingen mobilversion, icke-persistenta sessioner) är den ett värdefullt verktyg för alla som vill återfå kontrollen över sin digitala integritet. Dess användarvänlighet och standardkonfiguration gör det till ett klokt val för integritetsmedvetna användare, oavsett om de är nybörjare eller erfarna.



## Resurser



### Officiell dokumentation




- [Officiell webbplats för Mullvad Browser](https://mullvad.net/fr/browser)
- [Nedladdningssida för Mullvad Browser] (https://mullvad.net/en/download/browser)
- [Detaljerade tekniska specifikationer] (https://mullvad.net/en/browser/Hard-facts)
- [Mullvad Browser Extension] (https://mullvad.net/en/help/mullvad-browser-extension)



### Guider och förklaringar




- [Varför integritet är viktigt] (https://mullvad.net/en/why-privacy-matters/how-mass-surveillance-companies-collect-your-data)
- [Tor utan Tor: Mullvad Browser-koncept] (https://mullvad.net/en/browser/tor-without-tor)
- [Så här väljer du en integritetsvänlig webbläsare] (https://mullvad.net/en/browser/things-to-look-for-when-choosing-a-browser)
- [Förståelse för fingeravtryck i webbläsare] (https://mullvad.net/en/browser/browser-fingerprinting)



### Support och hjälp




- [Hjälpcenter för Mullvad Browser] (https://mullvad.net/en/help/tag/mullvad-browser)
- [Första stegen till integritet på nätet] (https://mullvad.net/en/help/first-steps-towards-online-privacy)



### Gemenskapens resurser




- [Mullvad Browser Guide - Sekretessguider](https://www.privacyguides.org/en/desktop-browsers/)
- [Samhällsdiskussioner](https://discuss.privacyguides.net/t/about-changing-settings-in-mullvad-browser/18330)