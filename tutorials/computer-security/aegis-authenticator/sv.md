---
name: Aegis Authenticator
description: Hur kan du använda Aegis Authenticator för att säkra dina konton med dubbel autentisering?
---

![cover](assets/cover.webp)



Idag är tvåfaktorsautentisering (2FA) avgörande för att säkra onlinekonton. Förutom lösenordet läggs en andra faktor till (ofta en 6-siffrig kod) som upphör att gälla efter 30 sekunder, vilket gör det betydligt svårare för hackare. Att använda en dedikerad TOTP-applikation (*Time-based One-Time Password*) är säkrare än SMS, som kan kapas genom SIM-bytesattacker.



Alla autentiseringsapplikationer är dock inte skapade lika. Många proprietära lösningar (Google Authenticator, Authy etc.) innebär problem: de är proprietära och har sluten källkod (omöjligt att granska deras säkerhet), integrerar ibland spårare av reklam, erbjuder inte krypterad säkerhetskopiering av dina koder och kan till och med förhindra export av dina konton för att låsa in dig i deras ekosystem.



Aegis Authenticator, å andra sidan, presenterar sig som ett gratis och etiskt alternativ till dessa applikationer. Aegis är en gratis, säker applikation med öppen källkod för att hantera dina tvåstegsverifieringstoken på Android. Dess utveckling fokuserar på viktiga funktioner som andra appar inte erbjuder, inklusive robust kryptering av lokala data och möjligheten till säkra säkerhetskopior. Sammantaget erbjuder Aegis en lokal, reviderbar lösning för dubbel autentisering, perfekt för alla som vill behålla total kontroll över sina 2FA-koder.



## Vi presenterar Aegis Authenticator



Aegis Authenticator är en 2FA-applikation med öppen källkod för Android, släppt under GPL v3-licensen. Den utmärker sig för sin "privacy by design"-filosofi: applikationen fungerar helt offline och kräver ingen anslutning till en fjärrtjänst. Som ett resultat förblir dina tokens lagrade lokalt på din enhet, i ett säkert kassaskåp som du ensam har nyckeln till.



### Viktiga funktioner



**Krypterat valv:** Alla dina OTP-koder lagras i ett AES-256-krypterat valv (GCM-läge), skyddat av ett användardefinierat huvudlösenord. Du kan låsa upp valvet med lösenord eller biometriska data (fingeravtryck, ansiktsigenkänning) för extra bekvämlighet. Om du inte har något lösenord är uppgifterna okrypterade, så vi rekommenderar starkt att du anger ett sådant.



**Avancerad organisation:** Aegis håller dina många 2FA-konton välorganiserade. Du kan sortera dina poster alfabetiskt eller i den ordning du vill, gruppera dem efter kategori (t.ex. Personlig, Arbete, Social) för enkel hämtning och tilldela varje post en personlig ikon. Ett sökfält ingår för att omedelbart hitta en tjänst eller ett konto med namn.



**Krypterade lokala säkerhetskopior:** För att du aldrig ska förlora åtkomsten till dina konton erbjuder Aegis automatiska säkerhetskopior av ditt kassaskåp. Dessa är krypterade (via ett lösenord) och kan sparas på valfri plats (intern lagring, molnmapp etc.). Programmet kan också exportera din kontodatabas manuellt, i krypterat eller okrypterat format efter behov. Det är lika enkelt att importera konton från andra 2FA-program (Aegis stöder import från Authy, Google Authenticator, FreeOTP, andOTP etc.).



**Säkerhet och integritet:** applikationen är helt offline som standard. Det kräver inga nätverksbehörigheter - vilket innebär att det inte överför några data till omvärlden och inte innehåller några annonsspårare eller beteendeanalysmoduler. Aegis visar inte annonser och kräver inget användarkonto: så snart det har installerats är det igång utan registrering. Eftersom källkoden är offentlig på GitHub kan communityt granska den fritt, vilket garanterar att det inte finns några skadliga eller dolda funktioner.



**Modern Interface:** Aegis har en snygg Material Design, med stöd för mörka teman (inklusive ett AMOLED-läge) och till och med en valfri kakelvy för att visa dina koder som rutnät. Interface är stilrent, utan krusiduller, och förhindrar skärmdumpning av koder som en säkerhetsåtgärd.



## Installation



Eftersom Aegis Authenticator är öppen källkod föredrar dess utvecklare integritetsvänliga distributionskanaler. Det finns två huvudsakliga sätt att installera det:



### Via F-Droid (rekommenderas)



Det säkraste och enklaste sättet är genom F-Droid, den fria alternativa butiken. Om F-Droid ännu inte är installerat på din telefon, börja med att ladda ner det från den officiella webbplatsen [F-Droid.org] (https://f-droid.org). Sedan :





- Öppna F-Droid och se till att du har uppdaterat dina repositories för att få den senaste listan över applikationer
- Sök efter "Aegis Authenticator" i F-Droid. Den officiella applikationen ska visas (utgivare: Beem Development)
- Starta installationen genom att trycka på Install. Eftersom Aegis är en av de applikationer som verifierats av F-Droid, drar du nytta av en pålitlig och säker nedladdning



Om du installerar via F-Droid får du fördelen att du får automatiska uppdateringar av programmet så snart de släpps. Dessutom garanterar F-Droid att applikationen är fri från oönskade proprietära komponenter.



### Via GitHub (signerad APK)



Om du föredrar att installera applikationen utan att gå igenom en butik kan du ladda ner den officiella APK direkt från projektets GitHub-sida. På Aegis-arkivet ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)), gå till avsnittet Releases där stabila versioner publiceras.





- Ladda ner den senaste APK-versionen
- Innan du installerar APK måste du se till att du har godkänt installationen av applikationer från okända källor på din enhet (i Android-inställningar)
- APK som tillhandahålls på GitHub är signerad av utvecklaren med samma nyckel som på F-Droid



Efter manuell installation kommer applikationen att fungera identiskt. Observera att uppdateringar inte kommer att ske automatiskt: du måste kontrollera GitHub regelbundet för nya versioner.



### Google Play Butik vs F-Droid



Aegis Authenticator finns tillgänglig i både Google Play Store och F-Droid, vilket ger dig möjlighet att välja installationsmetod:



**Google Play Store:**




- ✅ Automatiska uppdateringar integrerade i Android-systemet
- ✅ Enkel och välbekant installation
- ✅ Samma signerade APK som på andra kanaler



**F-Droid (rekommenderas) :**




- ✅ Butik med fri och öppen källkod
- ✅ Reproducerbar och verifierbar konstruktion
- ✅ Ingen Google-tjänst krävs
- ✅ Respekt för filosofin om fri programvara



Valet mellan dessa två alternativ beror på dina preferenser när det gäller Googles ekosystem. Om du föredrar enkelhet är Play Store perfekt. Om du vill ha ett mer integritetsvänligt tillvägagångssätt, oberoende av Googles tjänster, är F-Droid det bättre valet.



## Första konfigurationen



När Aegis startas för första gången föreslås en inledande konfigurationsprocedur för att säkra din 2FA-kod:



![Configuration initiale Aegis](assets/fr/01.webp)



*Inledande konfiguration av Aegis: välkomstskärm, säkerhetsval, definition och slutförande av huvudlösenord*



### Ange ett huvudlösenord



Aegis kommer först att be dig att välja ett huvudlösenord. Detta lösenord kommer att användas för att kryptera alla dina autentiseringstoken som lagras i valvet. Vi rekommenderar starkt att du väljer ett starkt och unikt lösenord som bara du känner till.



**⚠️ Varning:** glöm inte det här lösenordet - om du tappar bort det kommer dina krypterade 2FA-koder att bli oåtkomliga (det finns ingen bakdörr). Aegis kommer att be dig att ange lösenordet två gånger för bekräftelse.



### Aktivera biometrisk upplåsning (valfritt)



Om din Android-enhet är utrustad med en fingeravtrycksläsare eller annan biometrisk sensor kommer Aegis att uppmana dig att aktivera biometrisk upplåsning. Det här alternativet är valfritt men mycket praktiskt: det gör att du snabbt kan låsa upp applikationen med ditt fingeravtryck eller ansikte, istället för att skriva in lösenordet varje gång.



Observera att biometri är en extra bekvämlighet: ditt huvudlösenord krävs fortfarande om biometrin ändras eller om enheten startas om.



### Upptäck applikationsinställningar



När du har kommit in i programmet (Interface är till en början tom) ska du bekanta dig med de tillgängliga konfigurationsalternativen. Öppna inställningarna via rullgardinsmenyn längst upp till höger på skärmen (tre vertikala prickar) och välj sedan "Settings".



![Interface principale et paramètres](assets/fr/02.webp)



*Interface huvud Aegis tom vid start, tillgång till parametermeny och översikt över tillgängliga alternativ*



I menyn Aegis-inställningar finns flera viktiga avsnitt samlade:





- **Utseende**: Anpassa tema (ljust, mörkt, AMOLED), språk och andra visuella inställningar
- **Beteende**: Konfigurera programmets beteende när det interagerar med listan över poster
- **Ikonpaket**: hantera och importera ikonpaket för att anpassa utseendet och känslan på dina konton
- **Säkerhet**: Inställningar för kryptering, biometrisk upplåsning, automatisk låsning och andra säkerhetsparametrar
- **Säkerhetskopior**: Konfigurera automatiska säkerhetskopior till en plats som du väljer
- **Import och export**: Importera säkerhetskopior från andra autentiseringsprogram och exportera ditt Aegis-valv manuellt
- **Revisionslogg**: Detaljerad logg över alla viktiga händelser i applikationen



Denna tydliga organisation gör att du kan konfigurera Aegis enligt dina önskemål och säkerhetsbehov.



## Lägg till ett 2FA-konto



När Aegis är konfigurerat kan vi gå vidare till det viktigaste: att lägga till dina tvåfaktorkonton. Processen är enkel och Aegis erbjuder flera metoder för att integrera dina autentiseringskoder.



### De tre tillgängliga tilläggsmetoderna



Från Aegis Interface trycker du på **+**-knappen längst ned till höger för att komma till alternativen för tillägg. Du har tre alternativ:





- **Skanna QR-kod**: Skanna direkt den QR-kod som visas av webbtjänsten
- **Skanna bild**: Skanna en QR-kod från en bild som sparats på din enhet
- **Ange manuellt**: Ange 2FA-kontoinformation manuellt



### Praktiskt exempel: konfigurering av Bitwarden



Låt oss ta ett konkret exempel på 2FA-aktivering på Bitwarden för att illustrera processen:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Exempel på aktivering av 2FA på Bitwarden: Interface webb med autentiseringsalternativ och Aegis-rekommendation*





- **Logga in och få tillgång till inställningar**: Logga in på ditt Bitwarden-konto och gå till inställningarna, fliken "Säkerhet"
- Avsnittet **Providers**: Gå till avsnittet "Providers" och klicka på "Manage" i avsnittet "Authenticator app"



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Fullständig process för att lägga till ett konto: QR-koden visas av tjänsten, den hemliga nyckeln är synlig och verifieringskoden anges*





- **Skanna QR-koden**: Ett popup-fönster öppnas med QR-koden och den hemliga nyckeln
- **Aegis**: Använd "Skanna QR-kod" för att fånga information automatiskt
- **Verifiering**: Ange den 6-siffriga koden som genereras av Aegis i fältet "Verifieringskod"
- **Aktivering**: Klicka på "Slå på" för att slutföra aktiveringen



### Lägg till detaljer manuellt



Om du föredrar eller inte kan skanna QR-koden kan du använda alternativet "Ange manuellt". I formuläret kan du ange :



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Process för att lägga till ett nytt 2FA-konto: töm Interface, lägg till alternativ, manuellt inmatningsformulär och konto har lagts till*





- **Namn**: Tjänstens namn (t.ex. Bitwarden, GitHub ...)
- **Emittent**: Emittenten (ofta identisk med namnet)
- **Grupp**: Valfritt, för att organisera dina konton efter kategori
- **Not**: Personliga anmärkningar på detta konto
- **Hemlig**: Den hemliga nyckel som tillhandahålls av tjänsten (maskerad som standard)
- **Avancerad**: Avancerade parametrar (algoritm, period, antal siffror)



När kontot har lagts till visas det i listan med aktuell kod och en tidsindikator som visar hur lång tid som återstår innan det förnyas.



### Universell kompatibilitet



Aegis är kompatibelt med alla tjänster som använder TOTP- och HOTP-standarderna, inklusive praktiskt taget alla webbplatser som erbjuder 2FA: sociala nätverk, banker, lösenordshanterare, kryptoplattformar etc.



### Organisation av entréer



När du har lagt till flera konton kommer du att uppskatta Aegis organisationsverktyg:





- **Anpassad sortering:** Som standard listas konton i alfabetisk ordning, men du kan ändra ordningen manuellt
- **Grupper och kategorier:** Skapa grupper för att skilja dina personliga konton från dina företagskonton, eller gruppera dem efter typ av tjänst (bank, e-post, sociala nätverk etc.)
- **Anpassade ikoner:** Aegis försöker automatiskt tilldela en lämplig ikon om den finns tillgänglig, annars kan du välja bland många generiska ikoner eller importera en bild
- **Snabbsökning:** I sökfältet längst upp kan du skriva några bokstäver för att omedelbart filtrera bort matchande poster



När du trycker på en post visas OTP-koden i full storlek (om den var dold) och du kan kopiera den till urklipp med en lång tryckning - praktiskt för att klistra in den i det program du vill ansluta till.



## Säkerhet och säkerhetskopiering



Eftersom säkerhet är en central del av Aegis är det viktigt att förstå hur dina 2FA-koder skyddas och hur du säkerställer att de finns kvar om det skulle uppstå problem.



### Säkerhetsarkitektur



**Robust kryptering**: Alla dina koder lagras i ett krypterat kassaskåp med hjälp av algoritmen **AES-256 i GCM-läge**, i kombination med ditt huvudlösenord. Nyckelderivationen baseras på **scrypt**, vilket ger ett förbättrat skydd mot brute-force-attacker.



** Säker upplåsning** : Huvudlösenordet krävs för att dekryptera dina data. Biometri (tillval) använder **Android Secure Keystore** och TEE (Trusted Execution Environment) för att skydda krypteringsnyckeln.



**Minimala behörigheter**: Aegis fungerar offline som standard och kräver endast åtkomst till kameran (QR-skanning), biometri och vibrator. Inga data samlas in eller delas.



### Alternativ för säkerhetskopiering



Aegis erbjuder flera olika backup-strategier för att passa olika behov av säkerhet och bekvämlighet:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface komplett med extra konto, backup-varning, inställningar för automatisk backup och backup-strategier*



**1. Automatiska lokala säkerhetskopior**




- Konfigurera en valfri destinationsmapp
- Anpassningsbar frekvens (efter varje ändring, dagligen, etc.)
- Lösenordsskyddade krypterade filer (.aesvault)
- Kompatibel med synkroniserade mappar (Nextcloud, Dropbox, etc.)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Process för val av mapp för säkerhetskopiering: filutforskare, målmapp och åtkomstbehörighet*



**2. Android** säkerhetskopiering i molnet




- Integrering med Android backup-system som tillval
- Endast tillgängligt för krypterade kassaskåp (säkerhet bevarad)
- Transparent säkerhetskopiering med andra Android-data
- Automatisk återställning vid byte av enhet



**3. Manuell** export




- Exportera på begäran via **Inställningar > Import & Export**
- Val av krypterat (rekommenderas) eller klart format
- Användbart för migreringar eller enstaka säkerhetskopior



### God säkerhetspraxis





- Spara flera **säkerhetskopior** för att förhindra korruption
- **Testa** regelbundet dina säkerhetskopior genom att försöka återställa dem
- **Förvara dina återställningskoder separat**
- Ditt **huvudlösenord** krävs fortfarande även med säkerhetskopiering i molnet
- **Säkra ditt huvudlösenord**: använd ett unikt, starkt lösenord som sparas i en lösenordshanterare
- **Håll din applikation uppdaterad** med de senaste säkerhetsuppdateringarna
- Aktivera **autolås** i inställningarna för att säkra åtkomsten till programmet
- Inaktivera **skärmdumpar** (standardalternativ) för att förhindra att dina koder fångas upp
- Använd biometri sparsamt: välj lösenord för kritisk åtkomst



## Jämförelse med andra applikationer



Hur står sig Aegis i jämförelse med andra populära autentiseringsapplikationer?



### Aegis vs Google Authenticator



**Aegis :**




- ✅ Öppen källkod och granskningsbar
- ✅ Lokal krypterad säkerhetskopia
- ✅ Avancerad organisation (grupper, ikoner, sökning)
- ✅ Ingen datainsamling
- ❌ Endast Android



**Google Authenticator :**




- ✅ Tillgänglig på Android och iOS
- ✅ Molnsynkronisering (sedan 2023)
- ❌ Sluten källkod
- ❌ Begränsad funktionalitet
- ❌ Potentiell insamling av Google-data



### Aegis vs Authy



**Aegis :**




- ✅ Öppen källkod
- ✅ Inget konto krävs
- ✅ Export av kod möjlig
- ✅ Total datakontroll
- ❌ Ingen inbyggd synkronisering av flera enheter



**Authy :**




- ✅ Synkronisering av flera enheter
- ✅ Tillgänglig på Android och iOS
- ❌ Sluten källkod
- ❌ Kräver ett telefonnummer
- ❌ Det går inte att exportera koder
- ❌ Desktop-applikationer tas bort i mars 2024



Aegis är utmärkt för Android-användare som värdesätter transparens, lokal säkerhet och fullständig kontroll över sina data. Alternativ som Authy är bättre lämpade om du absolut behöver automatisk synkronisering av flera enheter.




## Slutsats



Aegis Authenticator är en utmärkt lösning för dig som letar efter en integritetsvänlig, säker och transparent 2FA-applikation. Dess öppna källkod, i kombination med robust kryptering och en snygg Interface, gör det till ett förstklassigt val för att säkra dina onlinekonton.



Även om Aegis är begränsad till Android och saknar inbyggd molnsynkronisering, kompenserar den mer än väl för dessa begränsningar med sin "privacy by design"-filosofi och totala datakontroll. För användare som är måna om sin digitala integritet erbjuder Aegis ett trovärdigt och kraftfullt alternativ till marknadens dominerande proprietära lösningar.



Säkerheten för dina onlinekonton behöver inte vara beroende av kommersiella företags goda vilja. Med Aegis behåller du kontrollen över dina autentiseringskoder, i ett digitalt kassaskåp som du ensam har nyckeln till.



## Resurser



### Officiella webbplatser




- **Officiell webbplats**: [getaegis.app](https://getaegis.app/) - Presentation och nedladdning av ansökan
- **Källkod**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Officiell GitHub-lagringsplats
- **F-Droid**: [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Installation via gratisbutiken



### Teknisk dokumentation




- **Dokumentation om Vault**: [Vault design](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Teknisk beskrivning av kryptering och säker arkitektur
- **Officiell FAQ**: [getaegis.app/#faq](https://getaegis.app/#faq) - Svar på vanliga frågor
- **Projektets wiki**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Fullständig användardokumentation