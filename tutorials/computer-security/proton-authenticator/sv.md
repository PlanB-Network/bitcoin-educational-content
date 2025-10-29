---
name: Proton Authenticator
description: Hur kan jag använda Proton Authenticator för att säkra mina konton med 2FA?
---
![cover](assets/cover.webp)



Tvåfaktorsautentisering (2FA) lägger till en extra säkerhetsbarriär till dina konton genom att, utöver ditt lösenord, kräva ytterligare bevis på att bara du har det. Om du aktiverar 2FA minskar risken för hackning drastiskt, även om ditt lösenord skulle komma på avvägar genom nätfiske eller dataläckage. Utan 2FA skulle en angripare bara behöva ditt lösenord för att komma åt dina konton; med 2FA skulle han också behöva din andra faktor, vilket förhindrar de flesta försök till kontostöld.



Det finns olika typer av 2FA. SMS-koder är bättre än ingenting, men de är fortfarande sårbara för SIM-bytesattacker och avlyssning. Vi rekommenderar inte SMS som en primär 2FA. Autentiseringsapplikationer (TOTP) generate tillfälliga koder lokalt på din enhet, vilket gör dem mycket svårare att fånga upp. Fysiska säkerhetsnycklar erbjuder den bästa säkerheten, men kräver dedikerad hårdvara.



Proton Authenticator är en TOTP-autentiserare. Det är Protons svar på begränsningarna i befintliga applikationer: många är proprietära, innehåller annonsspårare och erbjuder inte krypterad säkerhetskopiering. Proton Authenticator skiljer sig från mängden genom att tillhandahålla en applikation med öppen källkod, fri från annonser och spårare, med krypterad säkerhetskopiering från början till slut.



## Vi presenterar Proton Authenticator



Proton Authenticator är en mobil och stationär TOTP-autentiseringsapplikation utvecklad av Proton, känd för sina integritetsfokuserade tjänster. Liksom alla Proton-produkter är applikationen öppen källkod och har genomgått oberoende säkerhetsrevisioner. Den finns tillgänglig kostnadsfritt på alla plattformar (Android, iOS, Windows, macOS, Linux).



Proton Authenticator erbjuder följande nyckelfunktioner:





- Generering av **TOTP-koder** för dina 2FA-konton, kompatibla med de flesta webbplatser som använder Google Authenticator, Authy, etc.





- **Valfri krypterad molnbackup**: du kan koppla applikationen till ditt Proton-konto för att säkerhetskopiera och synkronisera dina koder med end-to-end-kryptering. Om du tappar bort din enhet är det bara att ansluta en ny för att återställa alla dina koder.





- **Synkronisering av flera enheter**: genom att logga in på Proton i appen synkroniseras dina 2FA-koder automatiskt mellan flera enheter via end-to-end-kryptering. På iOS är ett alternativ synkronisering via iCloud.





- **Lokal låsning med lösenord eller biometri**: applikationen erbjuder PIN- och/eller fingeravtrycks-/Face ID-låsning. Så även om någon fysiskt får tillgång till din olåsta telefon kommer de inte att kunna öppna Proton Authenticator.





- **Ingen datainsamling eller spårare**: Proton har åtagit sig att inte samla in några personuppgifter via applikationen. Det finns ingen dold reklam eller beteendeanalys.





- **Enkel import/export**: en av Proton Authenticators starka sidor är dess importguide för befintliga konton, som är kompatibel med andra applikationer (Google Authenticator, Authy, Aegis, etc.). Du kan också exportera dina koder till en fil om det behövs.



Kort sagt, Proton Authenticator strävar efter att vara en kompromisslös 2FA-lösning: säker, privat, flexibel.



## Installation



Proton Authenticator är tillgänglig gratis på alla plattformar. För att ladda ner applikationen, gå till den officiella sidan: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)



![PROTON AUTHENTICATOR](assets/fr/01.webp)



*Officiell Proton Authenticator-sida som visar applikationens huvudfunktioner och Interface*



På den här sidan hittar du nedladdningslänkar för alla operativsystem: Android, iOS, Windows, macOS och Linux. Klicka bara på det operativsystem du vill ha och följ de vanliga installationsstegen.



I den här guiden visar vi hur du installerar och konfigurerar den på macOS, och sedan tittar vi på hur du installerar appen på iOS och synkroniserar dina koder mellan de två enheterna.



### Installation på macOS



När du har laddat ner och installerat programmet startar du Proton Authenticator. Vid första start guidar programmet dig genom några inledande konfigurationsskärmar:



![PROTON AUTHENTICATOR](assets/fr/02.webp)



*Välkomstskärm för Proton Authenticator med meddelandet "Säkerhet i varje kod" och knappen "Kom igång"*



### Initial import



Om Proton Authenticator upptäcker att du tidigare har använt en annan 2FA-applikation kan en importguide visas. Den stöder direkt import från vissa applikationer (Google Authenticator, 2FAS, Authy, Aegis, etc.). Alternativt kan du hoppa över det här steget och lägga till dina konton manuellt senare.



![PROTON AUTHENTICATOR](assets/fr/03.webp)



*Importguide för att överföra koder från andra autentiseringsprogram*



![PROTON AUTHENTICATOR](assets/fr/04.webp)



*Kompatibla importapplikationer: 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth och Google Authenticator*



### Skydd av lokala applikationer



Ange en PIN-kod för upplåsning eller aktivera biometrisk upplåsning (Touch ID) om det finns tillgängligt. Det här steget är viktigt för att förhindra att någon som använder din Mac får fri tillgång till dina 2FA-koder.



![PROTON AUTHENTICATOR](assets/fr/05.webp)



*Konfigurationsskärm för Touch ID med meddelandet "Skydda dina data" och knappen "Aktivera Touch ID"*



### Synkroniseringsalternativ



Programmet låter dig också aktivera iCloud-synkronisering för att säkerhetskopiera dina data säkert mellan dina Apple-enheter.



![PROTON AUTHENTICATOR](assets/fr/06.webp)



*ICloud-synkroniseringsalternativ med meddelandet "Säkerhetskopiera dina data säkert med krypterad iCloud-synkronisering"*



När dessa steg har slutförts är Proton Authenticator klar att användas.



![PROTON AUTHENTICATOR](assets/fr/07.webp)



*Interface huvudtomt Proton Authenticator med alternativen "Skapa en ny kod" och "Importera koder"*



## Lägg till ett 2FA-konto med ProtonMail



Vi ska nu titta på hur du lägger till din första 2FA-kod, med ProtonMail som exempel. Den här metoden fungerar identiskt för alla tjänster som stöder tvåfaktorsautentisering.



### Aktivera 2FA på ProtonMail



Först och främst kan du läsa vår guide till ProtonMail för mer information:



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Logga in på ditt ProtonMail-konto och gå till säkerhetsinställningarna. Leta efter alternativet "Tvåfaktorsautentisering" och aktivera det.



![PROTON AUTHENTICATOR](assets/fr/08.webp)



*ProtonMail-inställningssida med alternativet "Authenticator app" i avsnittet "Tvåfaktorsautentisering"*



Klicka på knappen för att aktivera autentiseringen och ProtonMail kommer att uppmana dig att välja en autentiseringsapplikation.



![PROTON AUTHENTICATOR](assets/fr/09.webp)



*Konfigurationsfönster för ProtonMail 2FA med knapparna "Avbryt" och "Nästa"*



ProtonMail kommer då att visa en QR-kod som du kan skanna med din autentiseringsapplikation.



![PROTON AUTHENTICATOR](assets/fr/10.webp)



*ProtonMail QR-kod att skanna med din autentiseringsapplikation, med alternativet "Ange nyckel manuellt istället" tillgängligt*



Om du föredrar att ange nyckeln manuellt kan du klicka på "Ange nyckel manuellt istället" för att se den hemliga nyckeln.



![PROTON AUTHENTICATOR](assets/fr/11.webp)



*Manuell inmatning av 2FA-information: Nyckel, Intervall (30) och Siffror (6)*



### Skanna QR-koden med Proton Authenticator



I Proton Authenticator på macOS klickar du på "Skapa en ny kod". Programmet erbjuder dig flera alternativ: **Skanna en QR-kod** eller **Ange nyckeln manuellt**.



Använd kameran på din Mac för att skanna QR-koden som visas på ProtonMail-skärmen. När du har skannat QR-koden kommer du till konfigurationsskärmen för den nya koden.



![PROTON AUTHENTICATOR](assets/fr/12.webp)



*Nytt fönster för skapande av post med titel (ProtonMail), hemlighet, avsändare (Proton), sifferparametrar och intervallfält*



Proton Authenticator kommer automatiskt att fylla i informationen. Du kan anpassa namnet om du vill och sedan klicka på "Spara".



![PROTON AUTHENTICATOR](assets/fr/13.webp)



*TOTP-kod genererad för ProtonMail (848 812) med visning av återstående tid*



### Validera konfigurationen



ProtonMail kommer att be dig att ange en 6-siffrig kod som genereras av Proton Authenticator för att bekräfta att 2FA fungerar korrekt.



![PROTON AUTHENTICATOR](assets/fr/14.webp)



*Valideringsskärm för ProtonMail där du ombeds ange den 6-siffriga koden (848812)*



Kopiera koden från applikationen (genom att klicka på den) och klistra in den i ProtonMail för att slutföra aktiveringen.



När du har validerat kommer ProtonMail att be dig att ladda ner dina återställningskoder. Det är viktigt att spara dem noggrant.



![PROTON AUTHENTICATOR](assets/fr/15.webp)



*ProtonMail återställningskoder skärm med lista över räddningskoder och "Download"* -knappen



### Larmkoder



När du lägger till ett konto ska du behålla de återställningskoder som tillhandahålls av tjänsten. De flesta webbplatser erbjuder statiska återställningskoder för engångsbruk som ska förvaras på ett säkert ställe. Förvara dessa säkerhetskopieringskoder utanför Proton Authenticator så att du kan komma åt ditt konto om du förlorar åtkomsten till 2FA-applikationen.



## IOS-installation och kodimport



Nu när du har ställt in Proton Authenticator på macOS kanske du också vill använda den på din iPhone eller iPad. Så här får du dina 2FA-koder på flera enheter.



### Ladda ner applikationen på iOS



Gå till App Store och sök efter "Proton Authenticator". Ladda ner och installera programmet på din iOS-enhet.



![PROTON AUTHENTICATOR](assets/fr/16.webp)



*Installationsprocess på iOS: välkomstskärm, importguide, val av kompatibla applikationer och slutskärm "Importera koder från Proton Authenticator"*



### Metod 1: Exportera/Importera via fil JSON



Om du inte använder automatisk synkronisering (iCloud eller Proton-konto) måste du manuellt överföra dina koder från din Mac till din iPhone:



**Steg 1 - Exportera från macOS** :



På din Mac öppnar du Proton Authenticator och går till Inställningar (kugghjulsikonen). I menyn klickar du på "Export".



![PROTON AUTHENTICATOR](assets/fr/17.webp)



*Proton Authenticators inställningsmeny på macOS med alternativet "Export" synligt*



![PROTON AUTHENTICATOR](assets/fr/18.webp)



*Exportfönster med filnamnet "Proton_Authenticator_backup_2025" och "Spara"*-knappen



Spara JSON-filen på din Mac. Du kan skicka den med säker e-post eller spara den i iCloud Drive så att du kan komma åt den från din iPhone.



**Steg 2 - Importera på iOS** :



På din iPhone installerar du Proton Authenticator och under konfigurationen väljer du att importera koder. Välj "Proton Authenticator" från listan och importera JSON-filen.



![PROTON AUTHENTICATOR](assets/fr/19.webp)



*Importprocess på iOS: Lokalisering av JSON-fil, importbekräftelse och konfigurationsskärmar med Face ID- och iCloud-alternativ*



### Metod 2: Automatisk synkronisering



**Via Proton-konto (för synkronisering av flera plattformar)** :



Om du ännu inte har skapat ett Proton-konto och vill synkronisera mellan olika operativsystem kommer programmet att uppmana dig att skapa eller ansluta ett Proton-konto.



![PROTON AUTHENTICATOR](assets/fr/20.webp)



*Skärmen för synkronisering av enheter ber dig att skapa ett kostnadsfritt Proton-konto eller ansluta till ett befintligt konto*



**Via iCloud (endast för Apples ekosystem)** :


Om du bara använder Apple-enheter kan du välja iCloud-synkronisering i programinställningarna. Denna metod kommer automatiskt och säkert att synkronisera dina koder mellan alla dina Apple-enheter, utan att du behöver ett Proton-konto.



## Krypterad säkerhetskopiering och återställning



En av Proton Authenticators viktigaste funktioner är dess end-to-end-backup av 2FA-koder, vilket säkerställer att en förlust eller byte av enhet inte innebär att du måste börja om från början.



### End-to-end-kryptering



När det gäller krypterad molnbackup med Proton Authenticator krypteras dina TOTP-hemligheter lokalt på din enhet innan de skickas till Proton-servern. Dekryptering är endast möjlig för dig, på dina enheter som är anslutna till ditt Proton-konto. Proton AG har inte nyckeln till att läsa dina registrerade koder.



På iOS, om du väljer iCloud snarare än Proton-kontot, krypteras dina data enligt Apple-standarder. Med lokal säkerhetskopiering på Android kan du kryptera säkerhetskopian med ett lösenord som du själv väljer.



### Återställande i händelse av förlust



Om din telefon tappas bort, blir stulen eller om du byter telefonlur :



**Med Proton backup aktiverad**: Installera Proton Authenticator på den nya enheten. Under den första installationen loggar du in på samma Proton-konto. Omedelbart kommer applikationen att synkronisera och ladda ner alla dina 2FA-koder från den krypterade säkerhetskopian.



** Med iCloud-säkerhetskopia (iOS)**: Anslut den nya iPhone/iPad med samma Apple-ID och se till att aktivera iCloud Keychain. När du har installerat Proton Authenticator ansluter du till iCloud. Dina koder bör synkroniseras via iCloud och visas.



**Ingen molnbackup**: Du måste importera dina konton manuellt. Om du hade exporterat en backup-fil, använd Import-funktionen i Proton Authenticator. I värsta fall, om du inte hade någon säkerhetskopia, måste du använda säkerhetskopieringskoderna för varje tjänst eller kontakta support.



Med Proton Authenticator kan du när som helst exportera dina konton, antingen som en krypterad fil eller som en QR-kod för flera konton. Dessa alternativ ger dig extra säkerhet.



## Bästa praxis



Att använda en 2FA-autentisering förbättrar din säkerhet avsevärt, men vissa bästa metoder måste följas:



### Spara dina nödkoder



När du aktiverar 2FA på en tjänst får du ofta en lista med återställningskoder. Förvara dem utanför din telefon (på papper, i en krypterad lösenordshanterare etc.). I händelse av total förlust av din autentiserare kommer dessa statiska koder att rädda dig.



### Blanda inte ihop dina lösenord och 2FA-koder



Det är frestande att använda en lösenordshanterare som också lagrar TOTP. Men att hålla lösenordet och 2FA-koden på samma plats skapar en enda felpunkt och försvagar dubbel autentisering. För maximal säkerhet rekommenderar många experter att man separerar de två faktorerna: lösenord i en säker hanterare och 2FA-koder i en separat applikation som Proton Authenticator. Att använda en integrerad hanterare är dock fortfarande bättre än att inte ha någon 2FA alls.



### Aktivera flera 2FA-metoder



Använd helst mer än en andra faktor för dina kritiska konton. Tveka inte att lägga till en fysisk säkerhetsnyckel om tjänsten tillåter det. Se vår handledning om fysiska Yubikey-nycklar för mer information:



https://planb.academy/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Ha också utskrivna nödkoder till hands.



### Håll dig diskret och skydda din enhet



Låt inte någon söka igenom din olåsta telefon. Med Proton Authenticator skyddas dina koder av PIN/biometri - avslöja inte PIN-koden. Akta dig också för nätfiske: även med 2FA kan en angripare använda en kod till en bedräglig webbplats i realtid om du ger den till en sådan.



### Uppdateringar och revisioner



Hålla Proton Authenticator uppdaterad (uppdateringar korrigerar eventuella brister). Eftersom koden är öppen utför gemenskapen informella granskningar och Proton publicerar resultaten av formella granskningar.



## Jämförelse med andra applikationer



Hur står sig Proton Authenticator i jämförelse med andra autentiseringsapplikationer? Här är en jämförande sammanfattning:



**Proton Authenticator**: Öppen källkod, valfri E2EE-krypterad molnbackup, synkronisering av flera enheter, lokal låsning, ingen spårning, tillgänglig på mobil och dator.



**Google Authenticator**: Proprietär, säkerhetskopiering via Google-konto sedan 2023 men utan end-to-end-kryptering (nycklar kan ses av Google), synkronisering av flera enheter tillagd 2023, inget applikationslås som standard, innehåller Google-trackers.



**Aegis Authenticator**: Öppen källkod, endast lokal backup, ingen molnsynkronisering, kod/biometriskt lås, ingen spårning, endast Android.



**Authy**: Egenutvecklad, lösenordskrypterad molnbackup men stängd kod, synkronisering av flera enheter, PIN-lås/fingeravtryck, samlar in telefonnummer, desktop-applikation som upphör i mars 2024.



Du hittar vår guide till Authy nedan:



https://planb.academy/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator är en av de mest omfattande och säkra lösningar som finns: öppen källkod, krypterad synkronisering av flera enheter, ingen kommersiell uppföljning.



## Resurser och stöd



### Officiell dokumentation




- **Officiell webbplats**: [proton.me/authenticator](https://proton.me/authenticator) - Produktpresentation och nedladdningar
- **Nedladdningssida**: [proton.me/en/authenticator/download](https://proton.me/fr/authenticator/download) - Länkar för alla operativsystem
- **Proton support**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Officiell 2FA-aktiveringsguide
- **Proton blogg**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Tillkännagivande och detaljerade funktioner



### Källkod och transparens




- **GitHub Proton Authenticator**: [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Öppen källkod
- **Säkerhetsrevisioner**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Oberoende revisionsrapporter



### Rekommenderade säkerhetstester


Efter konfigurationen ska du testa din installation:




- [Have I Been Pwned] (https://haveibeenpwned.com/) - Kontrollera om dina konton har blivit utsatta för intrång
- [2FA Directory](https://2fa.directory/) - Lista över tjänster som stöder 2FA



### Gemenskaper och diskussioner




- Reddit r/Proton: [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Officiell gemenskap för Proton
- **Forum för integritetsguider**: [discuss.privacyyguides.net](https://discuss.privacyguides.net) - Tekniska diskussioner om integritetsfrågor
- **Reddit r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - Allmänna integritetstips



### Övriga




- [Have I Been Pwned] (https://haveibeenpwned.com/) - Kontrollera om dina konton har blivit utsatta för intrång
- [2FA Directory](https://2fa.directory/) - Lista över tjänster som stöder 2FA