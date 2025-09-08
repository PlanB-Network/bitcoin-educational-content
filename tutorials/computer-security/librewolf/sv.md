---
name: LibreWolf
description: Så här använder du LibreWolfs sekretesswebbläsare
---

![cover](assets/cover.webp)



Varje klick, varje sökning, varje besökt webbplats: din webbläsare har blivit en sofistikerad tjallare som matar ett globalt kommersiellt övervakningssystem. Google Chrome, som används av över 3 miljarder människor, förvandlar din dagliga surfning till lukrativ data för reklamjättarna. Även Firefox, trots sitt rykte som en "etisk" webbläsare, aktiverar som standard telemetri-mekanismer som överför dina surfvanor till Mozilla.



Denna verklighet väcker en viktig fråga: Är det fortfarande möjligt att surfa fritt på Internet utan att ständigt bli uttittad och profilerad? Lyckligtvis är svaret ja, tack vare samhällsprojekt som sätter användaren tillbaka i centrum för sina bekymmer.



LibreWolf förkroppsligar denna filosofi om digitalt motstånd. Denna webbläsare är skapad av en grupp oberoende utvecklare och förvandlar Firefox till en veritabel sköld mot övervakning på nätet. Där kommersiella webbläsare försöker tjäna pengar på din uppmärksamhet gör LibreWolf tvärtom: gör dig osynlig för spårare samtidigt som du bevarar en flytande, modern surfupplevelse.



I den här handledningen kommer vi att upptäcka hur LibreWolf kan förändra hur du surfar på webben och erbjuda ett robust skydd mot spårning utan att offra prestanda eller webbkompatibilitet.



![LIBREWOLF](assets/fr/01.webp)


*Marknadsandel för webbläsare: Chrome dominerar med 65% av marknaden, följt av Safari och Edge. Denna dominans väcker frågor om mångfald på webben och integritet*



## Vi presenterar LibreWolf



**FreeWolf** är en webbläsare med öppen källkod som bygger på Mozilla Firefox och som utvecklas och underhålls av en oberoende grupp entusiaster som arbetar med fri programvara. Huvudsyftet är att erbjuda surfning med fokus på användarens integritet, säkerhet och frihet.



Konkret använder LibreWolf Firefox Gecko-motor, men med en radikalt annorlunda filosofi: där Firefox måste balansera integritet och användarvänlighet, väljer LibreWolf integritet som standard. Projektet tar bort allt som kan inkräkta på din integritet (telemetri, datainsamling, sponsrade moduler) och integrerar samtidigt förbättrade säkerhetsinställningar.



### Mål: integritet och frihet



LibreWolf syftar till att maximera skyddet mot spårning och fingeravtryck och samtidigt förbättra webbläsarens säkerhet. Dess huvudsakliga mål inkluderar:





- Avlägsna all telemetri och datainsamling** i Firefox
- Inaktivera funktioner som strider mot användarfriheten**, t.ex. proprietära DRM-moduler
- Tillämpa sekretess-/säkerhetsinställningar** och specifika korrigeringar från början
- Gemenskapsutveckling garanterar öppenhet och oberoende** från kommersiella intressen



Kort sagt presenterar LibreWolf sig som "Firefox som det skulle ha varit om integritet var högsta prioritet" - en webbläsare som respekterar dig som standard, utan ytterligare konfiguration krävs.



### Huvudsakliga egenskaper



Redan från början erbjuder LibreWolf en rad integritetsinriktade funktioner:



** Ingen telemetri eller datainsamling:** Till skillnad från Chrome eller Firefox, som skickar viss användningsstatistik, samlar LibreWolf absolut ingenting från din surfning. Inga kraschrapporter, inga användarstudier, inga sponsrade förslag.



**LibreWolf integrerar nativt uBlock Origin-tillägget, en av de bästa annonsblockerarna och spårarna på marknaden. Som standard filtrerar LibreWolf aggressivt bort allt som kan spåra dig online (påträngande annonser, spårningsskript, kryptovaluta Mining).



**Privat sökmotor som standard:** LibreWolf använder som standard DuckDuckGo som sin första sökmotor, som inte sparar någon historik över dina frågor. Andra integritetsinriktade alternativ (Searx, Qwant, Whoogle) finns också tillgängliga.



**Förstärkt anti-fingeravtrycksskydd:** Fingeravtryck gör att en webbläsare kan identifieras unikt via dess konfiguration, även utan cookies. För att motverka detta aktiverar LibreWolf RFP-teknik (Resist Fingerprinting) från Tor-projektet för att göra din webbläsare så generisk som möjligt. Tester visar att en standard Firefox är ~90% unik på verktyg som coveryourtracks.eff.org, jämfört med endast ~10-20% för LibreWolf (dessa siffror är vägledande och kan variera beroende på mjukvaru- och hårdvarukonfiguration och installerade tillägg).



![LIBREWOLF](assets/fr/07.webp)


*EFF:s testsida [Cover Your Tracks] (https://coveryourtracks.eff.org/) med knappen TEST YOUR BROWSER. Den här sidan används för att utvärdera skyddet mot spårare och fingeravtryck



![LIBREWOLF](assets/fr/08.webp)


*Testresultat för att dölja dina spår. Meddelandet "du har ett starkt skydd mot webbspårning" visas, vilket visar att LibreWolf.* är ett effektivt skydd



**LibreWolf aktiverar strikta säkerhetsinställningar som standard. Firefox förbättrade spårningsskydd har flyttats till nivån Strikt för att blockera tusentals spårare, tredjepartscookies och skadligt innehåll. Den aktiverar också webbplats- och cookieisolering (*Total Cookie Protection*) för att dela upp data för varje domän och begränsar WebRTC (begränsar *ICE-kandidater* och routing via proxy när en proxy finns) för att minska risken för IP Address-läckage.



**Snabba motoruppdateringar:** Projektet följer Firefox utveckling mycket noga: LibreWolf är alltid baserat på den senaste stabila versionen av Firefox, och underhållarna strävar efter att släppa en ny version inom 24 till 72 timmar efter varje officiell Firefox-version.



## Fördelar och nackdelar



### Fördelar





- Ingen telemetri eller oönskade anslutningar:** LibreWolf överför inga användningsdata, vilket garanterar total respekt för din integritet.





- Öppen källkod och samhällsbaserad:** Projektet är 100% öppen källkod och underhålls av volontärer. Detta oberoende garanterar att ingen reklammodell kommer att påverka utvecklingen.





- Förkonfigurerad för integritet:** LibreWolf sparar dig dyrbar tid: det finns ingen anledning att spendera timmar på att härda Firefox-inställningar, allt är redan gjort.





- Inbyggd annonsblockerare/spårare:** uBlock Origin är integrerad som standard, så du behöver inte göra någonting för att skydda dig mot annonser och buggar.





- Utmärkt skydd mot fingeravtryck:** Tack vare RFP och många sekretessinställningar minskar LibreWolf drastiskt ditt unika digitala fotavtryck på webben.





- Förbättrad prestanda och låg vikt:** Genom att ta bort telemetri och vissa icke-väsentliga funktioner kan LibreWolf vara något snabbare och mindre strömkrävande än standard Firefox.



### Nackdelar och begränsningar





- Inga inbyggda automatiska uppdateringar:** LibreWolf uppdaterar inte sig själv. Det är upp till dig att installera nya versioner så snart de släpps för att hålla dig säker.





- Minskad kompatibilitet med vissa tjänster:** På grund av sina mycket strikta inställningar kan LibreWolf stöta på problem på vissa webbplatser. Netflix och Disney+ streamingplattformar kommer inte att fungera, eftersom LibreWolf inaktiverar Widevine DRM som standard.





- Inget inbyggt anonymt nätverk:** Till skillnad från Tor Browser dirigerar LibreWolf inte trafik via Tor eller ett VPN på egen hand. Om du behöver nätverksanonymitet måste du manuellt konfigurera en proxy/VPN.





- Icke-beständiga cookies och sessioner (standard):** Av sekretesskäl raderar LibreWolf cookies, historik och webbplatsdata varje gång du stänger din webbläsare. Du kommer att behöva logga in på dina konton igen varje gång du loggar in.





- Ingen mobilversion eller molnsynkronisering:** LibreWolf är endast tillgänglig på skrivbordet (Windows, Linux, macOS). Det finns ingen mobilapplikation, och därför ingen synkronisering av konton eller bokmärken via ett moln.



## Installera LibreWolf



**Officiell hemsida:** [librewolf.net](https://librewolf.net)



LibreWolf är tillgängligt för alla större operativsystem för datorer: Linux, Windows och macOS. För att ladda ner LibreWolf, besök den officiella webbplatsen:



![LIBREWOLF](assets/fr/02.webp)


*LibreWolfs hemsida (librewolf.net) med webbläsarens logotyp, en blå installationsknapp och länkar till källkod och dokumentation. En stor blå pil pekar på Install-knappen*



Klicka på knappen "Installation" för att komma till detaljerade instruktioner för ditt operativsystem:



![LIBREWOLF](assets/fr/03.webp)


*Välj operativsystem för LibreWolf.* nedladdning



Installationen skiljer sig åt beroende på ditt operativsystem:



### På Linux


LibreWolf erbjuder builds för många distributioner. På Debian/Ubuntu och derivat finns ett officiellt APT-förvar tillgängligt. Alternativt publiceras LibreWolf i Flatpak på Flathub:


```
flatpak install flathub io.gitlab.librewolf-community
```



### På Windows


Ladda ner installationsprogrammet (.exe) från den officiella webbplatsen eller använd:




- Chocolatey:** `choco install librewolf`
- WinGet:** `winget installera librewolf`



### På macOS


LibreWolf finns tillgängligt som ett .dmg-paket för Mac. Ladda ner diskavbildningen från den officiella webbplatsen och dra och släpp LibreWolf-programmet i mappen Program. Alternativt kan du installera det via Homebrew.




## Konfiguration och första användning



Vid första uppstarten kommer du att märka den välbekanta Firefox Interface, förutom att den är mer avskalad: hemsidan innehåller bara sökfältet och inga sponsrade förslag. Du kommer att se uBlock Origin-ikonen i verktygsfältet - ett tecken på att blockeraren är aktiv.



![LIBREWOLF](assets/fr/04.webp)


*LibreWolfs startsida med tillägg och meny. En blå pil i det övre högra hörnet visar menyikonen (tre horisontella staplar)



LibreWolf laddar automatiskt dina sidor i "strikt" (antispårning) läge, och standardsökmotorn kommer att vara DuckDuckGo. Du kan försöka besöka en testsida för spårning (t.ex. amiunique.org) för att observera det exponerade fotavtrycket - det bör vara mycket mer generiskt än med en standardwebbläsare.



### Inställningar för sekretess



LibreWolf är redan optimalt konfigurerad för integritet. I Meny → Alternativ → Sekretess och säkerhet ser du att LibreWolf är inställd på läget Enhanced Tracking Protection: Strikt. Detta läge blockerar:




- Spårare mellan webbplatser
- Cookies från tredje part
- Känt spårningsinnehåll
- Kryptomining
- Digitala fingeravtrycksdetektorer



![LIBREWOLF](assets/fr/05.webp)


*Säkerhet och integritet fliken sida som visar LibreWolf.* säkerhetsinställningar



WebRTC är inaktiverat (förhindrar IP-läckor) och Total Cookie Protection är på plats. Telemetri och Firefox-undersökningar är helt avaktiverade.



### Hantering av cookies och historik



Som standard raderar LibreWolf cookies och lokal lagring varje gång den stängs. Om detta beteende stör dig kan du justera det i Sekretess och säkerhet → Cookies och webbplatsdata genom att avmarkera "Ta bort cookies och webbplatsdata när du stänger LibreWolf".



![LIBREWOLF](assets/fr/06.webp)


*Samma sida lite längre ner, med möjlighet att radera cookies när webbläsaren stängs*



### Lägga till användbara tillägg



Som en principfråga avråder LibreWolf från att lägga till onödiga tillägg, eftersom varje tillägg kan vara en spårningsvektor. Ändå kan vissa välrenommerade tillägg förbättra din upplevelse:




- Firefox Multi-Account Containers** (av Mozilla) för uppdelad surfning
- Decentraleyes** eller **LocalCDN** för att betjäna gemensamma bibliotek lokalt



Undvik särskilt "gratis VPN"-tillägg eller tvivelaktiga proxyer - uBlock Origin täcker redan 99% av dina behov.



## Vardaglig användning



### Daglig webbsökning


Använd LibreWolf för dina dagliga aktiviteter på Internet. Den stora skillnaden mot andra webbläsare är att du lämnar mycket färre reklamspår. Banners med "acceptera kakor" försvinner på många webbplatser tack vare uBlocks filtreringslistor.



### Använd privata flikar för att dela upp


Även om LibreWolf raderar allt i slutet av sessionen kan det vara användbart att öppna ett privat webbläsarfönster (Ctrl+Shift+P) för vissa uppgifter under sessionen, för att avskärma en specifik identitet.



### Dra nytta av containrar med flera konton


Att installera tillägget Multi-Account Containers kan hjälpa dig att segmentera dina aktiviteter i vattentäta silos. Du kan till exempel definiera en "Banking"-container för dina banksidor, en "Social Networks"-container för Facebook/Twitter osv. Varje behållare har sina egna cookies, sessioner och isolerad lagring. Varje behållare har sina egna cookies, sessioner och isolerad lagring.



### Finjusterad hantering av behörigheter per anläggning


LibreWolf låter dig kontrollera de behörigheter du ger till webbplatser (Plats, Kamera, Mikrofon, Meddelanden) från fall till fall. Ge endast behörigheter till webbplatser som du litar på och där det är nödvändigt.



## Bästa praxis med LibreWolf



1. **Håll LibreWolf uppdaterad:** Kontrollera webbplatsen regelbundet för nya versioner, särskilt efter en stabil Firefox-utgåva.



2. ** Undvik att blanda personlig identitet och privat surfning:** Helst ska du inte logga in med dina personliga konton på samma session där du gör känslig forskning.



3. **Överbelasta inte LibreWolf med onödiga tillägg:** Varje tillägg som du installerar kan medföra säkerhets- eller fingeravtrycksrisker.



4. **Använd en VPN- eller Tor-proxy i tillägg:** LibreWolf gör dig inte anonym för din internetleverantör. För nätverksanonymitet kan du använda LibreWolf bakom ett pålitligt VPN.



5. **Spara viktiga data:** Bokmärken, lösenord om de lagras lokalt. Överväg en extern lösenordshanterare (KeePassXC, Bitwarden) i stället för webbläsarens grundläggande lösenordshanterare.



## Jämförelse med andra webbläsare



LibreWolf är en del av "verktygslådan" med integritetsinriktade webbläsare:



**LibreWolf vs. Firefox:** LibreWolf levereras redan härdad och utan någon telemetri. Firefox behåller fördelen med synkronisering av flera enheter och en mycket stor användarbas, men kräver manuell konfiguration för att uppnå LibreWolfs sekretessnivå.



**Brave använder Chrome/Chromium-kod och integrerar en affärsmodell via sitt valfria reklamprogram. LibreWolf, som är en Fork för Firefox, behåller Mozillas fria ekosystem och har inga band till Google.



**LibreWolf vs Tor Browser:** Tor Browser är oersättlig när det gäller anonymitet inför kraftfull övervakning, men den är långsam och obekväm i vardagen. LibreWolf, för vardagssurfning på den klassiska webben, är mycket snabbare och mer praktisk.



**LibreWolf vs Mullvad Browser:** Mullvad Browser går ännu längre i standardisering, men på bekostnad av minskad användbarhet (omöjligt att behålla en inloggningskaka). LibreWolf skapar en balans: mycket privat, men användbar på daglig basis.



## Slutsats



LibreWolf är en utmärkt lösning för dem som letar efter en ultra-privat "vardaglig" webbläsare utan att gå så långt som till den extrema anonymiteten i Tor. Det är ett perfekt val för aktivister, journalister, utvecklare eller avancerade användare som vill ha klassisk webbsurfning (snabb, kompatibel med moderna webbplatser) och samtidigt slippa annonsspårning och Big Tech.



Trots att LibreWolf har vissa begränsningar (inga automatiska uppdateringar, begränsad kompatibilitet med vissa tjänster) är det ett värdefullt verktyg för alla som vill återfå kontrollen över sin digitala integritet. Dess användarvänlighet och standardkonfiguration gör det till ett klokt val för integritetsmedvetna användare.



## Resurser



### Officiell dokumentation




- [LibreWolfs officiella webbplats](https://librewolf.net)
- [Källkod på Codeberg](https://codeberg.org/librewolf)
- [Officiell FAQ](https://librewolf.net/docs/faq)



### Guider och jämförelser




- [Sekretessguider](https://www.privacyguides.org/en/desktop-browsers/)
- [Jämförande integritetstester] (https://privacytests.org)



### Stöd från gemenskapen




- [Subreddit r/LibreWolf] (https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf] (https://matrix.to/#/#librewolf:matrix.org)