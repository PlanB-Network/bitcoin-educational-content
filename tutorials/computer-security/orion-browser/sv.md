---
name: Orion Browser
description: Hur använder jag Orion Browser för att skydda din integritet på Mac och iPhone?
---

![cover](assets/cover.webp)



## Inledning



I ett sammanhang där de flesta webbläsare samlar in massor av personuppgifter blir valet av en integritetsvänlig webbläsare avgörande. Chrome dominerar med 65% av den globala marknaden, men dess affärsmodell bygger på exploatering av dina surfdata. Safari är visserligen integrerad i Apples ekosystem, men saknar avancerade skyddsfunktioner och stöder inte flexibelt tillägg från tredje part.



![Répartition du marché des navigateurs](assets/fr/01.webp)


*Fördelning av webbläsarmarknaden: Chrome dominerar med en marknadsandel på över 65%, följt av Safari, Edge och Firefox*



**Orion Browser** presenterar sig som ett innovativt alternativ för Apple-användare. Denna webbläsare är utvecklad av Kagi och kombinerar hastigheten hos WebKit-motorn med en filosofi om noll telemetri. Till skillnad från sina konkurrenter skickar Orion inga data till fjärrservrar och blockerar 99,9% av alla annonser och spårare, inklusive YouTube.



Dess unika funktion? Orion är den **enda WebKit**-webbläsare som kan installera Chrome **och** Firefox-tillägg, vilket ger det bästa av två världar. Denna kompatibilitet, i kombination med minnesförbrukning 2 till 3 gånger lägre än andra webbläsare och sömlös integration med Apples ekosystem (iCloud, Keychain), gör det till det perfekta valet för integritetsmedvetna Mac- och iPhone-användare.



## Varför välja Orion Browser?



### Viktiga fördelar



**Maximalt skydd direkt ur lådan**: Orion blockerar 99,9 % av alla annonser (inklusive YouTube) och alla förstaparts- och tredjepartsspårare som standard. Dess teknik kombinerar WebKits intelligenta spårningsskydd med EasyPrivacy-listor för maximal effektivitet. Unik funktion: Orion blockerar fingeravtrycksskript **innan de körs**, vilket gör spårning bokstavligen omöjlig - ett mer radikalt tillvägagångssätt än andra webbläsare som bara försöker "maskera" data.



**Noll verifierbar telemetri**: Orion har en radikal inställning till integritet, med noll telemetri som design. Till skillnad från andra webbläsare, som gör hundratals nätverksförfrågningar vid uppstart (IP-exponent, webbläsarfingeravtryck, personlig information), "ringer" Orion aldrig hem. Denna grundläggande skillnad eliminerar helt risken för oavsiktligt dataläckage.



**Utomordentlig prestanda**: Orion bygger på en optimerad version av WebKit och är lika snabb eller till och med snabbare än Safari på Mac. Speedometer 2.0/2.1-tester placerar den konsekvent på första plats på Apple Silicon-processorer. Native ad blocking accelererar sidladdningen ytterligare med 20-40%.



**Universellt stöd för tillägg**: Orion är en stor innovation som gör att du kan installera tillägg från Chrome Web Store **och** Mozilla Add-ons. WebExtensions-stödet är för närvarande experimentellt, med ett mål på 100% kompatibilitet vid betaversion. Du kan använda många populära tillägg som uBlock Origin, Bitwarden, till och med på iPhone - en världsnyhet på iOS, även om vissa kanske inte fungerar perfekt.



### Begränsningar att vara medveten om





- **Begränsad tillgänglighet**: För närvarande reserverat för macOS och iOS/iPadOS. En Linux-version håller på att nå milstolpar i utvecklingen (milstolpe 2 år 2025), men ingen publik version finns tillgänglig. Windows och Android är inte under utveckling på grund av resursbrist.
- **Stängd källkod**: Även om vissa komponenter har öppen källkod är Orion fortfarande till övervägande del proprietärt, vilket är en fråga som diskuteras i integritetsgemenskapen.
- **Experimentella tillägg**: Stöd för tillägg är fortfarande i betaversion, med frekventa inkompatibiliteter. Tillägg kan påverka prestandan, och vissa fungerar inte alls.
- **WebKit-säkerhet**: Till skillnad från Chromium erbjuder WebKit inte en lika robust processisolering per webbplats, vilket kan innebära säkerhetsrisker i vissa scenarier.
- **Blockering av tester**: Orion presterar avsiktligt dåligt i tester för onlineannonsering (26-35%), eftersom Kagi anser att dessa tester är "fundamentalt felaktiga". Den faktiska effektiviteten vid daglig användning är mycket bättre.



## Installation av Orion Browser



### På macOS



![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)


*På Kagis hemsida presenteras Orion Browser som "en annonsfri webbläsare med totalt integritetsskydd och universellt stöd för tillägg"*





- Gå till [kagi.com/orion] (https://kagi.com/orion/)
- Klicka på "**Hämta Orion för macOS**"



![Page de téléchargement d'Orion Browser](assets/fr/03.webp)


*Nedladdningssida för Orion Browser som visar tillgänglighet för macOS och iOS, med länkar till App Store*





- Öppna den nedladdade filen `.dmg`
- Dra Orion-programmet till mappen Program
- Vid första start kommer macOS att be dig bekräfta att du öppnar



**Alternativt hemmabygge**:


```bash
brew install --cask orion
```



### På iPhone/iPad





- Öppna **App Store**
- Sök efter "**Orion Browser by Kagi**"
- Installera gratisappen (kompatibel med iOS 15+)



### Inledande konfiguration



Vid första uppskjutningen guidar Orion dig genom flera steg:



**1. Välkommen skärm**


![Écran de bienvenue d'Orion](assets/fr/04.webp)


*Orion Browser välkomstskärm med viktiga funktioner: snabbare surfning, ingen telemetri, annonsblockering och stöd för tillägg*



**2. Interface** anpassning


![Options de personnalisation](assets/fr/05.webp)


*Med anpassningsskärmen kan du konfigurera utseendet på flikarna och Interface så att det passar dina önskemål*





- **Dataimport**: Överför enkelt favoriter och lösenord från Safari, Chrome eller Firefox
- **iCloud-synkronisering**: Aktivera för att hitta dina favoriter och flikar på alla dina Apple-enheter



**3. Installation på mobila enheter**


![Installation sur iOS](assets/fr/06.webp)


*Installationsskärm på iOS som visar QR-koden för att snabbt ladda ner Orion Browser från App Store*



**4. Interface välkomsthälsning och viktiga verktyg**



![Page d'accueil Orion](assets/fr/07.webp)


*Orion Browser Interface-hemsida: pilen visar de tre viktigaste verktygen som är tillgängliga direkt från Address-fältet*



När konfigurationen är klar kommer du att upptäcka Orions strömlinjeformade Interface med sina **tre viktiga verktyg** (markerade med pilen):





- **Sköld 🛡️**: Visar integritetsrapport med antal objekt som blockerats på aktuell sida
- **Borste 🖌️**: Anpassa sidvisningen (tema, teckensnitt, ta bort distraherande Elements)
- **Utrustning ⚙️**: Konfigurera webbplatsspecifika parametrar (behörigheter, blockering etc.)



Dessa verktyg är alltid tillgängliga och ger dig möjlighet att kontrollera din surfupplevelse på varje enskild webbplats.



**Viktigt**: Orion är gratis och kräver ingen registrering eller skapande av konto för att fungera.



![Orion+ dans les préférences](assets/fr/08.webp)


*Orion+-prenumerationsskärm i inställningarna, som erbjuder en valfri prenumeration för att stödja utvecklingen*



**Orion+ (valfritt)**: För att stödja projektutveckling erbjuder Kagi Orion+ ($5/månad, $50/år, eller $150 livstid). Denna frivilliga prenumeration möjliggör:




- Kommunicera direkt med utvecklingsteamet
- Påverka webbläsarens utveckling enligt dina behov
- Få tillgång till Nightly-versioner med de senaste experimentella funktionerna
- Dra nytta av den senaste WebKit-motorn
- Få ett distinkt märke på feedbackforumet



Orion+ garanterar projektets oberoende: "Ditt ekonomiska bidrag hjälper oss att förbli oberoende och hålla vårt löfte om att bli den bästa webbläsaren för våra användare". Det är denna användarfinansieringsmodell som håller Orion reklamfritt och telemetrifritt.



## Konfiguration för maximal sekretess



### Viktiga parametrar



Öppna inställningar via **Orion → Preferences** (eller ⌘,):



**1. Sök - privat sökmotor**



![Configuration du moteur de recherche](assets/fr/09.webp)


*Standardkonfiguration av sökmotor: DuckDuckGo är vald för maximal integritet*





- **Standardmotor**: Välj **DuckDuckGo**, **Startpage** eller **Kagi** för optimal integritet (undvik Google/Bing)
- **Sökförslag**: Avaktivera dem för att förhindra att tangenttryckningar läcker ut till sökmotorernas servrar



**2. Sekretess - Allmänt** skydd



![Content Blocker dans les préférences](assets/fr/12.webp)


*Orions sekretessinställningar visar Content Blocker med 119.156 aktiva regler, alternativ för borttagning av spårare och anpassad användaragent*



**Innehållsblockerare är aktiv som standard**:




- **EasyList**: 119k+ regler för annonsblockering
- **EasyPrivacy**: Skydd mot spårning
- **Hantera filterlistor**: Lägg till ytterligare listor (Hagezi rekommenderas)



**Privacy-alternativ**:




- Ta bort spårare från webbadresser: **"Endast för privat surfning"** rensar upp kopierade länkar
- **Dela med dig av kraschrapporter**: "Efter att ha bett om godkännande" respekterar ditt samtycke
- **Anpassad användaragent**: Kan modifieras för att kringgå vissa blockeringar



![YouTube avec Privacy Report](assets/fr/10.webp)


*Exempel på YouTube som visats med Orion: ingen synlig reklam och integritetsrapport som visar de många Elements som blockerats*



**3. Webbplatsinställningar - Kontroll per webbplats**



![Website Settings pour YouTube](assets/fr/11.webp)


*Webbplatsinställningar för YouTube som visar kompatibilitetsalternativ, blockering av innehåll och webbplatsspecifika behörigheter*



**Snabb åtkomst**: Klicka på kugghjulet ⚙️ i Address-fältet för att justera:




- **Kompatibilitetsläge**: Löser visningsproblem genom att stänga av tillägg
- **Innehållsblockerare**: Avaktivera blockering för en specifik webbplats om det behövs
- **JavaScript/Cookies**: Granulär kontroll per webbplats
- **Behörigheter**: Kamera, mikrofon, plats individuellt konfigurerad



**4. Avancerade anpassade filter** (se nedan)



**Skapa anpassade filter** (Sekretess → Hantera filterlistor → Anpassade filter):



**Förenklad syntax** (Adblock Plus-kompatibel):




- `reddit.com##.promotedlink`: Döljer sponsrade Reddit-inlägg
- `||ads.example.com^`: Blockerar helt och hållet en reklamdomän
- `@@||site-utile.com^`: Skapar ett undantag för en webbplats



**Tips:** Besök [FilterLists.com](https://filterlists.com) för tusentals specialiserade listor som är färdiga att använda.



### Rekommenderade förlängningar



Orion stöder inbyggt Chrome och Firefox förlängningar. Installera dem direkt från de officiella butikerna:



**Essentials**:




- **uBlock Ursprung**: Lägger till detaljerad kontroll till den ursprungliga blockeraren
- **Bitwarden**: Lösenordshanterare med öppen källkod
- **ClearURLs**: Raderar URL-spårningsparametrar



**Optionell**:




- **LokalCDN**: Serverar delade bibliotek lokalt
- **Automatisk borttagning av cookies**: Raderar automatiskt cookies när du stänger flikar
- **NoScript**: Total kontroll över JavaScript-körning (avancerade användare)



För att installera en:




- Besök [chrome.google.com/webstore](https://chrome.google.com/webstore) eller [addons.mozilla.org](https://addons.mozilla.org)
- Klicka på "Lägg till i Chrome/Firefox"
- Orion kommer att fånga upp och installera tillägget automatiskt



**Försiktighetsåtgärd**: Eftersom stödet för tillägg är experimentellt kan det hända att många tillägg inte fungerar korrekt eller påverkar prestandan. Om ett problem uppstår (webbplatsen fungerar inte längre, långsamhet) ska du inaktivera tilläggen ett efter ett för att identifiera källan.



## Daglig användning



### Interface och unika egenskaper




![Outil de personnalisation pinceau](assets/fr/13.webp)


*Orions penselmeny för anpassning av skärmen: teckenstorlek, tema (ljust/mörkt), avaktivering av klistriga rubriker och borttagning av distraherande Elements*



**Brush tool: avancerad anpassning**



Orions **brush**-verktyg är en unik funktion som gör att du kan anpassa visningen av varje webbplats:



**Temaalternativ**:




- Växla mellan ljusa och mörka teman för varje webbplats
- Automatisk anpassning till dina systempreferenser



**Typografisk kontroll**:




- **Teckenstorlek**: Justera läsbarheten med knapparna A- och A+
- **Teckensnitt**: Ändra teckensnittsfamilj (standard eller anpassad)



**Interface rengöring**:




- **Inaktivera klibbiga rubriker**: Tar bort rubriker som fastnar längst upp när du skrollar
- **Radera Elements**: Ta permanent bort irriterande Elements (annonser, popup-fönster, cookie-banners)
  - Klicka på "+ Erase" och välj sedan det objekt som ska döljas
  - Mycket användbart för webbplatser med ihållande annonser eller visuell spårning Elements



**Persistens**: Alla dessa inställningar sparas per domän och tillämpas automatiskt nästa gång du besöker den.



**Avancerad flikhantering**:




- **Vertikala flikar**: Aktivera via menyraden (funktion Flikar på sidan)
- **Kompakta flikar**: I Inställningar → Flikar → Layout "Kompakt" för att spara utrymme
- **Flikgrupper**: Organisera dina sessioner efter tema
- **Flera profiler**: Skapa separata identiteter via menyraden (funktionen Profiler) med helt isolerade data



**Lågeffektsläge**: Detta läge, som inspirerats av iPhone, stänger automatiskt av inaktiva flikar efter 5 minuter och kan minska energiförbrukningen med upp till 90%. Aktivera det via Orions menyfält på Mac eller i inställningarna på iOS.



**Inbyggda verktyg** (redigeringsmeny och andra):




- **Redigera text på sidan**: tillfälligt ändra valfri text (menyn Redigera)
- **Tillåt kopiering och klistra in**: Omgår kopieringsbegränsningar (menyn Redigera)
- **Kopiera ren länk**: Högerklicka på en länk för att ta bort spårningsparametrar
- **Focus Mode**: distraktionsfri navigering i helskärmsläge
- **Bild-i-bild**: Titta på videor i ett flytande fönster
- **Öppna i Internet Archive**: Direkt tillgång till arkiverade versioner
- **Sekretessrapport**: Klicka på skölden 🛡️ för att se vilka objekt som blockeras per sida



### Hantering av privat surfning



Orions privata navigering (⌘⇧N) erbjuder:




- Fullständig isolering av cookies och sessioner
- Automatisk radering vid stängning
- Historik och avaktivering av cache
- Förbättrat skydd mot fingeravtryck



**Tips**: För avancerad uppdelning kan du skapa **separata profiler** via menyraden (funktionen Profiler). Varje profil visas som en separat app i Dock, med egna inställningar, tillägg och data som är helt isolerade.



### Prestandaoptimering och integritet



För att hålla Orion snabbt och privat:




- **Tillägg**: Begränsa till det absoluta minimum (kan minska prestandan)
- **Lågeffektsläge**: Aktivera för långa sessioner (90% besparing möjlig)
- **Sekretessrapport**: Klicka på skölden 🛡️ för att se blockeringar i realtid
- **Visuell anpassning**: Använd 🖌️-penseln för att anpassa skärmen och ta bort distraherande Elements
- **Kopiera ren länk**: Högerklicka för att kopiera länkar utan spårare
- **Separata profiler**: Använd särskilda profiler för att dela upp dina aktiviteter
- **Webbplatsinställningar**: Klicka på kugghjulet ⚙️ för att anpassa behörigheterna per webbplats
- **Regelbunden rengöring**: Rensa cacheminnet via Orion → Rensa webbläsardata



## Jämförelse med alternativ



| Critère | Orion | Safari | Chrome | Firefox | Brave |
|---------|-------|--------|---------|----------|--------|
| **Télémétrie** | Aucune | Minimale | Extensive | Modérée | Minimale |
| **Bloqueur natif** | 99,9% efficace | Basique | Absent | Partiel | Complet |
| **Extensions** | Chrome + Firefox | Limitées | Chrome uniquement | Firefox uniquement | Chrome uniquement |
| **Performance Mac** | Excellente | Excellente | Bonne | Moyenne | Bonne |
| **Consommation RAM** | Très faible | Faible | Élevée | Moyenne | Moyenne |
| **Open Source** | Partiel | Partiel (WebKit) | Partiel | Complet | Complet |
| **Plateformes** | Mac/iOS | Mac/iOS | Toutes | Toutes | Toutes |

**I motsats till Safari**: Orion erbjuder ett överlägset skydd med avancerade blockerare och tilläggsstöd, samtidigt som WebKit-prestandan bibehålls.



**Versus Chrome**: oöverträffad integritet utan att kompromissa med kompatibiliteten, tack vare stöd för Chrome-tillägg.



**Förhållande till Firefox**: Snabbare på Mac, Interface mer intuitiv, men mindre detaljerad kontroll och inte öppen källkod.



**Versus Brave**: Liknande filosofi, men Orion undviker krypto/BAT-kontroverser och erbjuder bättre Apple-integration.



## Rekommenderade användningsområden



**Ideal för**:




- Apple-användare vill ha mer integritet än Safari
- Personer som vill blockera alla annonser (inklusive YouTube) utan tillägg
- Utvecklare som behöver WebKit devtools med integrerat integritetsskydd
- IPhone-användare vill ha tillägg till skrivbordet på mobilen (unik innovation)
- Yrkesverksamma som behöver dela upp sina aktiviteter (flera profiler)
- Mobilanvändare som vill ha bättre batterihantering (Low Power Mode)



**Undvik om**:




- Du använder huvudsakligen Windows/Linux (ingen version tillgänglig)
- Helt öppen källkod är avgörande för din hotmodell
- Du är beroende av specifika tillägg som kanske inte fungerar
- Du behöver synkronisering mellan plattformar utanför Apples ekosystem
- Du föredrar en beprövad, stabil lösning (permanent betastatus sedan 2021)



## Uppmärksamhets- och säkerhetspunkter



### Unika säkerhetsfunktioner



**Revolutionärt skydd mot fingeravtryck**: Orion är den enda webbläsaren som helt blockerar exekveringen av fingeravtrycksskript innan de kan skanna ditt system. Denna "inget skript körs = inget fingeravtryck möjligt" -metod överträffar traditionella maskeringsmetoder som används av andra webbläsare.



**Genomskinlig vitlista**: Orion upprätthåller en liten offentlig lista över webbplatser (browserbench.org, wizzair.com) där blockering automatiskt inaktiveras för att undvika funktionsstörningar. Denna transparens gör det möjligt för användare att förstå exakt när och varför blockering lindras.



**Ogranskade tillägg**: Stöd för Chrome/Firefox-tillägg medför ytterligare risker, eftersom dessa tillägg inte har utformats för WebKit och inte är särskilt granskade för denna miljö.



### Underhåll och uppdateringar





- **Automatiska uppdateringar**: Orion uppdateras automatiskt på macOS via Sparkle
- **Spårning av sårbarheter**: Kontrollera regelbundet release notes för säkerhetsuppdateringar
- **Rapportering av fel**: Använd [orionfeedback.org](https://orionfeedback.org) för att rapportera problem




## Slutsats



Orion Browser innebär ett stort steg framåt för integritetsskyddet på macOS och iOS. Dess nolltelemetri, i kombination med en ultraeffektiv inbyggd blockerare och unikt stöd för universella tillägg, gör den till ett utmärkt val för integritetsmedvetna Apple-användare.



**Viktigt**: Orion är fortfarande i permanent beta sedan 2021, med begränsningar för kompatibilitet med tillägg och inneboende WebKit-risker. Bedöm dessa avvägningar enligt din hotmodell.



För daglig användning på en Mac eller iPhone är det förmodligen den bästa kompromissen mellan sekretess, prestanda och användarvänlighet som finns i Apples ekosystem, förutsatt att du accepterar dess begränsningar.



Kom ihåg: att skydda din integritet beror inte bara på din webbläsare. Kombinera Orion med bästa praxis (starka lösenord, 2FA, VPN vid behov) för optimal säkerhet online.



## Resurser och stöd



### Officiell dokumentation




- **Officiell webbplats**: [kagi.com/orion](https://kagi.com/orion/)
- **Fullständig FAQ**: [browser.kagi.com/faq](https://browser.kagi.com/faq)
- **Gemenskapsforum**: [community.kagi.com](https://community.kagi.com)
- **Buggspårning**: [orionfeedback.org](https://orionfeedback.org)
- **GitHub Orion**: [github.com/OrionBrowser](https://github.com/OrionBrowser) - Komponenter med öppen källkod
- **Blogg Kagi**: [blog.kagi.com](https://blog.kagi.com) - Nyheter och uppdateringar



### Rekommenderade verifieringstester



Efter konfigurationen ska du testa din installation:




- [Täck dina spår (EFF)](https://coveryourtracks.eff.org/) - Fingeravtryckstest
- [DNS Leak Test] (https://www.dnsleaktest.com/) - Sök efter DNS-läckor
- [BrowserLeaks] (https://browserleaks.com/) - Komplett uppsättning integritetstester



### Alternativ på Plan ₿ Network


För maximalt skydd, se våra andra guider:




- [Firefox-härdad] (https://planb.network/tutorials/computer-security/communication/firefox-11814cec-3415-4ed9-a06e-f6fda5c9510f) - Avancerad konfiguration för flera plattformar
- [Tor Browser] (https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb) - Fullständig anonymitet på nätet
- [Mullvad Browser] (https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e) - Maximalt skydd för fingeravtryck



Om du vill lära dig mer om webbläsarnas historia och funktion, samt om de viktigaste digitala objekten i ditt dagliga liv, vill jag bjuda in dig att upptäcka vår nya kostnadsfria kurs SCU 202, som finns tillgänglig på Plan ₿ Network:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1