---
name: Ente Auth
description: En öppen källkod, end-to-end-krypterad 2FA-autentisering
---
![cover](assets/cover.webp)



Tvåfaktorsautentisering (2FA) har blivit oumbärligt för att säkra våra onlinekonton. Förutom ditt vanliga lösenord krävs en tillfällig kod, som vanligtvis genereras av en särskild applikation. Den här mekanismen, som kallas TOTP (Time-Based One-Time Password), garanterar att en angripare inte kan komma åt ditt konto utan att ha den här andra faktorn, som förnyas var 30:e sekund, även om ditt lösenord avslöjas.



Att välja rätt autentiseringsapplikation är dock inte trivialt. Google Authenticator är visserligen populär, men har stora begränsningar: proprietär kod som är omöjlig att granska, synkronisering utan end-to-end-kryptering och risk för total förlust av koder om det skulle uppstå problem med telefonen. Andra lösningar, som Authy, kräver ett telefonnummer och garanterar inte total sekretess.



**Ente Auth** framstår som ett modernt och säkert alternativ. Denna kostnadsfria applikation med öppen källkod och flera plattformar, som utvecklats av teamet bakom [Ente Photos] (https://ente.io), erbjuder krypterade molnbackuper från början till slut och sömlös synkronisering mellan alla dina enheter. Till skillnad från proprietära lösningar ger Ente Auth dig total kontroll över dina autentiseringskoder utan att kompromissa med din integritet.



I den här handledningen visar vi dig steg för steg hur du installerar och använder Ente Auth och varför den här lösningen skiljer sig från traditionella autentiserare.



## Vi presenterar Ente Auth



Ente Auth utvecklades av teamet bakom Ente Photos, en end-to-end krypterad och integritetsvänlig fotolagringstjänst. I enlighet med Ente-filosofin ("Ente" betyder "min" på malayalam, vilket symboliserar kontroll över dina data) har Ente Auth utformats för att ge användarna full kontroll över sina tvåfaktorsautentiseringskoder.



### Huvudsakliga egenskaper



** Standard TOTP-koder **: Ente Auth genererar tillfälliga koder som är kompatibla med de flesta tjänster (GitHub, Google, Binance, ProtonMail, etc.). Du kan lägga till så många 2FA-konton som du behöver, och applikationen beräknar koderna baserat på de hemligheter som tillhandahålls.



**End-to-end krypterad molnbackup**: Dina koder lagras säkert online. Endast du kan dekryptera dem - krypteringsnyckeln härrör från ditt lösenord och är endast känd av dig. Ente (servern) har ingen kännedom om dina hemligheter eller ens om dina kontonummer, eftersom allt krypteras på klientsidan med hjälp av en nollkunskapsarkitektur.



**Synkronisering av flera enheter**: Du kan installera Ente Auth på flera enheter (smartphone, surfplatta, dator) och komma åt dina koder på dem alla. Eventuella ändringar sprids automatiskt och omedelbart till dina andra enheter via det krypterade molnet, vilket ger dig stor flexibilitet i ditt dagliga arbete.



**Minimalistisk, intuitiv Interface**: Applikationen erbjuder en strömlinjeformad Interface som är lätt att lära sig även för icke-tekniska användare. 2FA-konton visas med tjänstens namn, din inloggning och den 6-siffriga koden, som uppdateras i realtid. Ente Auth visar också nästa kod några sekunder i förväg för att undvika att bli överraskad av utgångna koder.



**Öppen källkod och granskad**: Ente Auths källkod är [offentlig på GitHub] (https://github.com/ente-io/auth) under AGPL v3.0-licensen. Alla utvecklare kan granska den för att kontrollera om det finns brister eller oönskat beteende. Den implementerade kryptografin har varit föremål för en [oberoende extern revision](https://ente.io/blog/cryptography-audit/), en garanti för att applikationens säkerhet är seriös.



### Fördelar och begränsningar



**Förmåner:**




- Inbyggd sekretess med kryptering från början till slut
- Säker synkronisering mellan alla dina enheter
- Revisionsbar öppen källkod
- Interface tydlig, intuitiv användare Interface
- Automatisk back-up för att förhindra förlust av koder
- Tillgänglig på alla plattformar (mobil och dator)



**Begränsningar:**




- Internetanslutning krävs för synkronisering
- Avancerade användare kan föredra 100% offline-lösningar som Aegis (endast Android)
- Relativt ny jämfört med etablerade lösningar



## Installation



Ente Auth är tillgänglig på de flesta populära plattformar. Du kan ladda ner applikationen från [den officiella webbplatsen](https://ente.io/auth) eller från de officiella butikerna.



![Installation d'Ente Auth](assets/fr/01.webp)



*Ente Auth nedladdningssida med alla tillgängliga plattformar*



### Android


Du har flera alternativ:




- Google Play Store**: Sök efter "Ente Auth" för klassisk installation
- F-Droid**: Tillgänglig från Androids applikationskatalog med öppen källkod, med en garanti för verifierad konstruktion och inget proprietärt innehåll
- Manuell installation** : APK-filer kan laddas ner från [projektets GitHub-sida] (https://github.com/ente-io/auth/releases) med integrerad avisering av nya versioner



### iOS (iPhone/iPad)


Installera Ente Auth direkt från Apple App Store genom att söka efter appens namn. IOS-appen kan också köras på Mac-datorer utrustade med Apple Silicon-chip (M1/M2) via Mac App Store.



### Datorer (Windows, macOS, Linux)


Ente Auth erbjuder inbyggda skrivbordsapplikationer. Besök [ente.io/download](https://ente.io/download) eller [Release-avsnittet på GitHub](https://github.com/ente-io/auth/releases) :





- Windows**: Ett EXE-installationsprogram medföljer
- macOS**: Dra och släpp DMG-diskavbildningar i program
- Linux** : Flera format tillgängliga (AppImage portabel, .deb för Debian/Ubuntu, .rpm för Fedora/Red Hat)



**Denna handledning är baserad på Ente Auth v4.4.4 och senare. Tidigare versioner kan ha mindre Interface-skillnader.



### Interface Webb


Utan installation kan du komma åt dina koder via [auth.ente.io] (https://auth.ente.io) från vilken webbläsare som helst. Interface web är begränsad till att visa koder (användbart för felsökning), eftersom tillägg av konton av säkerhetsskäl kräver en mobil- eller datorapplikation.



## Första konfigurationen



### Skapa konto



När du först startar Ente Auth har du två alternativ:



![Premier lancement d'Ente Auth](assets/fr/02.webp)



*Startskärm för Ente Auth med alternativ för att skapa konto*



**Med konto (rekommenderas)**: Välj "Create Account" och ange ditt e-postmeddelande Address och ett lösenord. **Viktigt**: detta lösenord fungerar som huvudlösenord för kryptering av dina data. Välj ett starkt, unikt lösenord, eftersom det inte finns någon konventionell återställningsprocedur utan dataförlust. Om du tappar bort det går det inte att återskapa dina krypterade data.



**Offline-läge**: Välj "Använd utan säkerhetskopior" för att använda programmet lokalt utan moln. I det här läget finns dina koder kvar på enheten, men du måste exportera dem manuellt för att inte förlora dem.



![Vérification email et récupération de clé](assets/fr/03.webp)



*E-postverifieringsprocess och generering av 24 ords återställningsnyckel*



En e-postverifiering kan begäras för att validera skapandet av kontot och möjliggöra återställning på en ny enhet. Ente Auth kommer också att förse dig med en återställningsnyckel på 24 ord (baserad på BIP39-metoden). **Det är viktigt att du sparar den här nyckeln** på en säker plats: det är ditt enda sätt att återställa dina data om du glömmer ditt lösenord.



### Lokal säkerhet



Jag rekommenderar starkt att du aktiverar lokalt skydd med kod eller biometri. Gå till **Inställningar → Säkerhet → Låsskärm** och konfigurera :





- Biometrisk upplåsning**: Face ID, fingeravtryck beroende på din enhets funktioner
- Applikationsspecifik PIN/lösenord**
- Fördröjning av autolåsning**: t.ex. "Omedelbart" eller efter 30 sekunders inaktivitet



Detta skydd förhindrar obehörig åtkomst till dina koder om någon får tillgång till din olåsta telefon. Observera att det här låset är en extra barriär: dina data förblir krypterade från början till slut även utan det här skyddet.



## Lägg till 2FA-konton



### Standardförfarande



För att lägga till ett nytt 2FA-konto, låt oss ta det konkreta exemplet med att aktivera 2FA på Bull Bitcoin :



![Configuration du premier compte](assets/fr/04.webp)



*Ente Auths huvud Interface redo att lägga till första 2FA*-kontot



**Tjänstesida (Bull Bitcoin)**: Logga in på ditt Bull Bitcoin-konto, gå till säkerhetsinställningar och aktivera tvåfaktorsautentisering.



![Paramètres de sécurité Bull Bitcoin](assets/fr/05.webp)



*Interface Bull Bitcoin* meny för säkerhetsinställningar



![Activation 2FA Bull Bitcoin](assets/fr/06.webp)



*Möjlighet att aktivera tvåfaktorsautentisering på Bull Bitcoin*



Tjänsten visar sedan en QR-kod som du kan skanna med din autentiseringsapplikation:



![QR code 2FA Bull Bitcoin](assets/fr/07.webp)



*QR-kod genererad av Bull Bitcoin som ska skannas med din autentiseringsenhet*



**In Ente Auth**: Klicka på "Enter a setup key" och skanna sedan QR-koden som visas av Bull Bitcoin. Ente Auth kommer automatiskt att känna igen kontot och fylla i fälten.



![Ajout du compte dans Ente Auth](assets/fr/08.webp)



*Konfigurera kontouppgifter för Bull Bitcoin i Ente Auth*



Du kan anpassa namnet på tjänsten och din inloggning för att göra det lättare att hitta den. Avancerade inställningar (SHA1-algoritm, 30 sekunders period, 6 siffror) är i allmänhet korrekta som standard.



**Validering på serviceplatsen**: Gå tillbaka till Bull Bitcoin och ange den 6-siffriga koden som genererats av Ente Auth för att slutföra aktiveringen.



![Saisie du code 2FA](assets/fr/09.webp)



*Ange kod som genererats av Ente Auth för att validera 2FA*-aktivering



![2FA activée](assets/fr/10.webp)



*Bekräftelse på lyckad 2FA-aktivering på Bull Bitcoin*



**Backup-koder**: Bull Bitcoin kommer att förse dig med återställningskoder. **Spara dem på en säker plats, separat från din autentiserare.



![Gestion des codes de sauvegarde](assets/fr/11.webp)



*Tillval till generate reservkoder för nödsituationer på Bull Bitcoin*



![Codes de récupération](assets/fr/12.webp)



*Lista över återvinningskoder att förvara på ett säkert ställe*



### Organisation och ledning



Ente Auth erbjuder flera praktiska funktioner:



**Snabb kopia**: Tryck på koden för att automatiskt kopiera den till urklippet.



**Kontextkänsliga åtgärder**: Tryck och håll (eller högerklicka på skrivbordet) för att redigera, ta bort, dela eller fästa en post.



**Taggar och sökning**: Organisera dina konton med taggar (personligt/professionellt, per tjänstekategori) och använd sökfältet för att snabbt filtrera.



![Création d'un tag](assets/fr/17.webp)



*Process för att skapa taggar: kontextuell meny och dialogruta för skapande*



![Tag appliqué](assets/fr/18.webp)



*Tagg "Bitcoin" framgångsrikt applicerad på Bull Bitcoin*-konto



**Automatiska ikoner**: Varje post kan illustreras med tjänstens logotyp tack vare integrationen av ikonpaketet [Simple Icons] (https://simpleicons.org/).



**Temporär säker delning**: En unik funktion i Ente Auth, säker delning, gör att du kan överföra en 2FA-kod till en kollega utan att avslöja den underliggande hemligheten. generate en krypterad länk som är giltig i högst 2, 5 eller 10 minuter - mottagaren ser koden i realtid, men kan inte exportera den eller komma åt kontodata. Den här metoden är idealisk för teknisk assistans eller tillfälligt samarbete och erbjuder en säkerhetsnivå som inte är möjlig med en enkel skärmdump eller ett textmeddelande.



![Partage sécurisé](assets/fr/19.webp)



*Interface tillfällig säker delning: välj varaktighet (5 min)*



**Säker export/import**: Med Ente Auth kan du exportera dina koder till andra applikationer eller importera dem från Google Authenticator och andra lösningar. Exporten sker via en krypterad fil eller QR-kod, vilket garanterar portabilitet av dina data utan att kompromissa med säkerheten.



**BIP39 återställningsnyckel**: Programmet genererar automatiskt en 24 ord lång återställningsfras enligt BIP39-standarden (Bitcoin Improvement Proposal), identisk med kryptovalutaplånböcker. Den här frasen är din ultimata återställningsnyckel, så att du kan återställa alla dina koder även om du glömmer ditt huvudlösenord.



## Konfiguration och inställningar



Ente Auth erbjuder många anpassningsmöjligheter som är tillgängliga via programmets inställningar:



![Paramètres principaux d'Ente Auth](assets/fr/13.webp)



*Översikt över parametrar som är tillgängliga i Ente Auth*



### Konto- och datahantering



![Paramètres de sécurité](assets/fr/14.webp)



*Avancerade säkerhetsalternativ: e-postverifiering, PIN-kod, aktiva sessioner*



Med hjälp av säkerhetsinställningarna kan du :




- Aktivera e-postverifiering för nya anslutningar
- Aktivera passnyckeln
- Visa aktiva sessioner på dina olika enheter
- Konfigurera en PIN-kod eller biometri



### Interface och användningsalternativ



![Paramètres généraux](assets/fr/15.webp)



*Interface parametrar och applikationsanpassning*



Allmänna inställningar inkluderar :




- Språk**: Interface flerspråkig
- Display**: Stora ikoner, kompakt läge
- Sekretess**: Dölj koder, snabb sökning
- Telemetri**: Felrapportering (kan avaktiveras)



## Säkerhetskopiering och synkronisering



### Hur kryptering fungerar



När du lägger till ett konto med ett anslutet Ente-konto krypterar programmet omedelbart dessa känsliga uppgifter lokalt med hjälp av din huvudnyckel (härledd från ditt lösenord). De krypterade uppgifterna skickas sedan till Ente-servern för lagring.



Tack vare denna mekanism är en end-to-end-krypterad molnbackup av dina koder alltid tillgänglig. Om du tappar bort din enhet är det bara att installera om Ente Auth och återansluta: programmet laddar automatiskt ner och dekrypterar alla dina koder.



### Synkronisering av flera enheter



Om du använder Ente Auth på både smartphone och dator visas alla tillägg eller ändringar på den ena enheten inom några sekunder på den andra. Denna synkronisering går via Entes moln, men eftersom data är krypterad från början till slut ser servern bara oläsbart krypterat innehåll.



![Synchronisation mobile](assets/fr/16.webp)



*Synkroniseringsdemo: samma Bull Bitcoin-konto tillgängligt på mobil och dator*



Synkroniseringen är sömlös: installera Ente Auth på din smartphone, logga in med dina inloggningsuppgifter och alla dina 2FA-koder (här Bull Bitcoin) visas automatiskt. Exemplet ovan visar perfekt synkronisering mellan dator och mobil - samma Bull Bitcoin-kod är tillgänglig på båda enheterna.



När det gäller sekretess har varken Ente eller någon tredje part tillgång till dina 2FA-hemligheter. Även metadata (taggar, anteckningar, tjänstenamn) krypteras innan de skickas. Denna nollkunskapsarkitektur säkerställer att endast du kan dechiffrera dina koder.



### Offline-användning



Synkronisering kräver internet, men Ente Auth fungerar perfekt offline på alla enheter, eftersom all data lagras lokalt. Offlineändringar köas och synkroniseras så snart anslutningen återställs.



## Säkerhet och integritet



### Kryptografiska garantier



Ente Auth bygger på robust end-to-end-kryptering med zero-knowledge-arkitektur. Dina koder krypteras med en nyckel som du är ensam om att inneha och som härleds från ditt huvudlösenord med hjälp av avancerade nyckeldrivningsfunktioner.



**Zero-knowledge-arkitektur: Ente kan inte fysiskt komma åt dina data. Även metadata (tjänstenamn, taggar, anteckningar) krypteras på klientsidan före överföring. Detta tillvägagångssätt säkerställer att Ente, i händelse av en attack mot dina servrar eller en myndighetsförfrågan, endast kan avslöja krypterade data som inte kan läsas utan ditt lösenord.



**Lokal kryptering**: Krypteringsprocessen sker helt och hållet på din enhet innan den skickas till molnet. Entes servrar tar emot och lagrar endast krypterad data, vilket gör obehörig åtkomst omöjlig, även för serviceadministratörer.



### Öppenhet och revisioner



Eftersom koden är [öppen källkod] (https://github.com/ente-io/auth) kan samhället verifiera att det inte finns några bakdörrar. Ente har fått [flera externa revisioner](https://ente.io/blog/cryptography-audit/) utförda för att validera säkerheten i sin implementering:





- Cure53** (Tyskland): Granskning av applikations- och kryptografisäkerhet
- Symbolic Software** (Frankrike): Specialiserad kryptografisk expertis
- Fallible** (Indien): Penetrationstestning och sårbarhetsanalys



Dessa oberoende granskningar, som utförs av erkända företag, garanterar att Ente Auths kryptografiska implementering överensstämmer med bästa säkerhetspraxis och inte har några kritiska brister.



### Integritetspolicy



Ente Auth tillämpar en [exemplarisk integritetspolicy] (https://ente.io/privacy/) som bygger på minimal datainsamling. Endast information som är absolut nödvändig för att tjänsten ska fungera sparas: din e-post Address för autentisering och kontoåterställning.



**Ingen spårning eller telemetri**: Till skillnad från de flesta applikationer samlar Ente Auth inte in några användningsmått, inga identifierande kraschdata och ingen beteendeinformation. Applikationen fungerar utan påträngande reklam eller analytiska spårare.



**GDPR-överensstämmelse**: Ente följer helt och hållet den europeiska allmänna dataskyddsförordningen. Du har rätt att när som helst få tillgång till, korrigera eller radera dina uppgifter. Dataexport] (https://ente.io/take-control/) är bara ett klick bort, och om du raderar ditt konto permanent raderas alla dina uppgifter från servrarna.



**Decentraliserad, säker lagring**: Dina krypterade data replikeras på 3 olika leverantörer i 3 olika länder, vilket garanterar optimal tillgänglighet samtidigt som du undviker att vara beroende av en enda molnleverantör.



Entes affärsmodell baseras på betaltjänsten Ente Photos, vilket gör det möjligt för oss att erbjuda Ente Auth **gratis och utan begränsningar** utan att kompromissa med din integritet genom att tjäna pengar på dina uppgifter. Detta tillvägagångssätt garanterar tjänstens hållbarhet utan att förlita sig på reklam eller återförsäljning av personuppgifter.



## Jämförelse med andra lösningar



| Application              | Open Source | Sauvegarde Cloud | E2EE | Sync multi-devices | Plateformes                                        |
| ------------------------ | ----------- | ---------------- | ---- | ------------------ | -------------------------------------------------- |
| **Ente Auth**            | ✅           | ✅                | ✅    | ✅                  | Android, iOS, Linux, macOS, Windows                |
| **Google Authenticator** | ❌           | ✅ (sans E2EE)    | ❌    | ✅                  | Android, iOS                                       |
| **Aegis**                | ✅           | ❌                | ✅    | ❌                  | Android                                            |
| **Authy**                | ❌           | ✅                | ❌    | ✅                  | Android, iOS *(apps desktop supprimées août 2024)* |
| **Proton Auth**          | ✅           | ✅                | ✅    | ✅                  | Android, iOS *(récent, moins établi)*              |

Ente Auth utmärker sig som en av få lösningar som kombinerar alla fördelar: transparens i källkoden, krypterad molnbackup och synkronisering mellan plattformar.



## Rekommenderade användningsområden



### Enskilda användare



Ente Auth är perfekt för säkerhetsmedvetna personer som systematiskt aktiverar 2FA. Du behöver inte längre oroa dig för att tappa bort dina koder när du byter telefon eller behöva välja mellan bekvämlighet och säkerhet.



### Familj och användning av flera enheter



Appen kommer till sin rätt om du använder flera enheter. Du kan spara dina koder på smartphones och surfplattor, eller dela vissa familjekoder (Netflix, familjemoln) synkront och säkert.



### Professionell användning



För team som hanterar känsliga konton underlättar Ente Auth samarbetet samtidigt som säkerheten bibehålls, tack vare de avancerade delningsfunktionerna som är integrerade i avsnittet "Organisation och hantering".



## Bästa praxis





- Spara dina nödkoder**: Förvara de återställningskoder som tillhandahålls av varje tjänst borta från din telefon.





- Använd ett starkt huvudlösenord**: Ditt huvudlösenord för Ente Auth måste vara unikt och robust, eftersom det skyddar alla dina koder.





- Aktivera lokalt skydd**: Konfigurera PIN-kod eller biometri för att förhindra obehörig fysisk åtkomst.





- Anpassa inte för mycket**: Undvik avancerade modifieringar som kan äventyra synkroniseringen.





- Håll programmet uppdaterat**: Uppdateringar korrigerar säkerhetsbrister och förbättrar funktionaliteten.





- Testa återställning**: Kontrollera ibland att du kan återställa dina koder på en annan enhet.



## Slutsats



Ente Auth är en modern och heltäckande lösning för tvåfaktorsautentisering. Genom att kombinera säkerhet, transparens och användarvänlighet uppfyller denna applikation med öppen källkod behoven hos krävande användare utan att göra avkall på bekvämligheten.



Till skillnad från proprietära lösningar som låser in dig i ett ogenomskinligt ekosystem ger Ente Auth dig tillbaka kontrollen över dina autentiseringsdata och skyddar dig samtidigt mot oavsiktlig förlust tack vare krypterade säkerhetskopior.



Oavsett om du är en privatperson som vill säkra dina personliga konton eller ett team som hanterar åtkomst för företag är Ente Auth ett smart val för att modernisera din strategi för digital säkerhet utan att kompromissa med integriteten.



## Resurser och stöd



### Officiell dokumentation




- Officiell webbplats**: [ente.io/auth](https://ente.io/auth)
- Hjälpcenter**: [help.ente.io/auth] (https://help.ente.io/auth)
- Teknisk blogg**: [ente.io/blog](https://ente.io/blog)



### Källkod och transparens




- GitHub**: [github.com/ente-io/auth](https://github.com/ente-io/auth)
- Kryptografi-revision**: [ente.io/blog/cryptography-audit](https://ente.io/blog/cryptography-audit)



### Gemenskap




- Discord**: [discord.gg/z2YVKkycX3] (https://discord.gg/z2YVKkycX3)
- Reddit**: [r/enteio](https://reddit.com/r/enteio)