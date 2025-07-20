---
name: GrafénOS

description: Graphene OS handledning
---

> [GrapheneOS] (https://grapheneos.org/) är ett integritets- och säkerhetsfokuserat mobilt operativsystem med Android-appkompatibilitet som utvecklats som ett icke-vinstdrivande projekt med öppen källkod.

GrapheneOS, som ursprungligen grundades 2014 som "CopperheadOS", är baserat på den traditionella Android-koden (AOSP), men med många förändringar och förbättringar som syftar till att förbättra användarnas integritet och säkerhet. GrapheneOS ger användaren kontroll över sin telefon, inte de stora teknikföretagen.


### Sommaire:



- Intro
- Förberedelser
- Installera
- Alternativ för appar
- Nackdelar
- Användbar information


Guide från https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md


## Varför använda GrapheneOS?


Moderna telefoner är $ 500- $ 1000 spårnings- och datahanteringsenheter. Varje enskild aspekt av vårt liv går igenom dem, och tyvärr delas mycket av dessa data med tredje part i någon form eller annan.

GrapheneOS är byggt specifikt för att minska denna datadelning och förbättra din enhets säkerhet från potentiella attackvektorer. Det finns inget sådant som ett GrapheneOS-konto. Du behöver inte ett för att ladda ner appar eller interagera med operativsystemet. Enkelt uttryckt är du inte produkten.


GrapheneOS ger ytterligare säkerhet till din Android-upplevelse genom några enkla grundprinciper.


1. **Reduktion av angreppsytan** - Ta bort onödig kod (eller bloatware).

2. **Vulnerability exposure prevention** - Ge användaren tillräckligt med detaljeringsgrad för att välja de kompromisser de är bekväma med.

3. **Sandbox containment** - GrapheneOS förstärker befintliga Android-sandlådor, vilket ytterligare låser varje apps förmåga att kommunicera med resten av din telefon.


Läs mer om de tekniska detaljerna i GrapheneOS funktionsuppsättning [här] (https://grapheneos.org/features).


### Underlätta övergången


Om du har varit fast förankrad i Googles eller Apples ekosystem i flera år kan tanken på att förlora all den bekvämligheten över en natt vara skrämmande. Men med några noggrant övervägda appinstallationsbeslut (behandlas senare) kan mycket av denna förväntade svårighet minskas eller tas bort.


Även om alternativen börjar bli bra kan tanken på en sådan förändring fortfarande vara avskräckande. Om du befinner dig i den här situationen är mitt bästa råd att köra din nya GrapheneOS-enhet tillsammans med din befintliga telefon ett tag. Därifrån kan du långsamt avvänja dig själv från 2-3 appar per vecka tills du bara sträcker dig efter din GrapheneOS-enhet.


Om du väljer detta tillvägagångssätt bör du vara sträng mot dig själv och så snabbt som möjligt sluta förlita dig på de övervakade alternativen. Vi människor är lata och kommer ofta att ta vägen med minst motstånd. Kom ihåg varför du gjorde bytet från första början.


**Istället för att betala med dina personuppgifter valde du att betala med din tid, och ibland med dina Hard-pengar (beroende på vilka alternativa appar du installerar).**


## Komma igång


GrapheneOS är för närvarande endast i produktion för _(ganska ironiskt)_ [Google Pixel](https://grapheneos.org/faq#supported-devices) sortimentet av telefoner. Detta kommer dock inte utan goda skäl. Pixels erbjuder den bästa hårdvarubaserade säkerheten för att komplettera det arbete som gjorts för att härda operativsystemet. Detta inkluderar saker som specifika komponentisoleringar och verifierad start.


### Välja en enhet


När du väljer den Pixel du vill installera GrapheneOS på, se till att du kontrollerar hur länge enheten ska fortsätta att få standard [säkerhetsuppdateringar] (https://support.google.com/pixelphone/answer/4457705?hl=en#zippy=%2Cpixel-xl-a-a-g-a-g) för.


I skrivande stund är Pixel 6a den billigaste modellen som finns tillgänglig med bra långsiktig support, garanterad fram till juli 2027. Om du väljer den här modellen fungerar inte OEM-upplåsning med den version av operativsystemet som kommer från fabriken. Du måste uppdatera det till juni 2022 eller senare via en luftburen uppdatering. När du har uppdaterat den måste du också fabriksåterställa enheten för att fixa OEM-upplåsning. Alla andra modeller som är upplåsta av operatören kommer att vara redo för GrapheneOS direkt ur lådan.


När du väljer en enhet vill du också se till att du köper en olåst version. Vissa operatörer som Verizon skickar sina enheter som är bootloader-låsta vilket helt förhindrar följande process.


### Installera GrapheneOS


GrapheneOS [web installer] (https://grapheneos.org/install/web) gör hela processen till en barnlek, och en process som kan slutföras av vem som helst på mindre än 10 minuter.

Följande instruktioner är en nedkortad version som hämtats från länken ovan.


Allt du behöver göra är..:



- Pixeln
- En USB-kabel för att ansluta telefonen till din dator
- En dator som kan köra en webbläsare (alla Chromium-baserade webbläsare: Chrome, Edge, Brave, etc.)


Låt oss dyka in i det:


1. Det första steget är att gå till **Inställningar** > **Om telefonen** och trycka upprepade gånger på byggnumret tills du ser att **'Developer Mode'** är aktiverat.

2. Gå sedan till **Inställningar** > **System** > **Utvecklaralternativ** och aktivera **'OEM Unlocking'**.

3. Starta nu om enheten och håll ned volymknappen medan telefonen slås på igen.

4. Anslut telefonen till den bärbara datorn och godkänn anslutningen om du uppmanas att godkänna den.

5. Klicka på "Lås upp bootloader" på sidan för webbinstallation.

6. Du kommer då att se att telefonalternativen ändras. Använd volymknappen för att ändra valet till "Lås upp" och använd strömknappen för att acceptera.

7. Klicka sedan på download release på sidan för webbinstallation.

8. När du har laddat ner allt går du vidare till nästa steg och klickar på "Flash release". Detta tar en minut eller två och du behöver inte röra telefonen alls.

9. Slutligen går du till nästa steg i webbinstallationsprogrammet och klickar på **Lock Bootloader**. Du måste ändra valet och bekräfta med strömbrytaren på samma sätt som du gjorde tidigare i processen.

10. När du ser ordet "Starta", bekräfta detta med strömbrytaren och enheten startar upp i ditt nya Google-fria operativsystem.


![image](assets/2.webp)

GrapheneOS startskärm



_Efter den första uppstarten och installationen är det bra att inaktivera OEM-upplåsning från Inställningar > System > Utvecklaralternativ


du kanske också vill ta det extra, valfria men rekommenderade steget att verifiera installationen via Auditor-appen. Du behöver en separat Android-telefon med appen installerad för att slutföra detta steg. Instruktioner för detta finns [här](https://attestation.app/tutorial)._



![video](https://www.youtube.com/embed/L1KZWjZVnAw)

Video som beskriver de enkla steg som beskrivs ovan



Om dessa enkla steg verkar vara ett steg för långt, kan du överväga att köpa en Pixel med GrapheneOS-programvaran [förinstallerad] (https://ronindojo.io/en/roninmobile). Var bara medveten om att du sätter en liten mängd förtroende för leverantören.


### Förinstallerade appar


Nu när du har ställt in kanske du märker hur nakna ben GrapheneOS verkar vid första installationen. Som standard kommer du att ha dessa appar installerade:


![image](assets/3.webp)


Standardappar


De enda två som du kanske inte är bekant med är "Auditor" och "Vanadium".



- [Auditor app] (https://play.google.com/store/apps/details?id=app.attestation.auditor) använder maskinvarubaserade säkerhetsfunktioner för att validera en enhets identitet samt operativsystemets äkthet och integritet. Den verifierar att enheten kör standardoperativsystemet med startladdaren låst och att ingen manipulering av operativsystemet har ägt rum.
- [Vanadium] (https://github.com/GrapheneOS/Vanadium) är en integritets- och säkerhetshärdad variant av webbläsaren Chromium.


## Anpassning


Telefoninställningar är en personlig sak, men här är några av de första sakerna jag ändrar när jag installerar GrapheneOS för att känna mig mer hemma.


### Sätta upp en bakgrundsbild och uppdatera temat


Gå till Inställningar > Bakgrund och stil. Gå härifrån:



- Uppdatera bakgrunderna på hem- och låsskärmen med bilder som hämtats från webben.
- Välja de accentfärger som används i hela användargränssnittet.
- Aktivera mörkt tema.


### Visa batteriprocent


Gå till **Inställningar** > **Batteri** och aktivera sedan **Visa batteriprocent** i statusfältet.


### Importera kontakter


** Från en annan Android-telefon ** - Gå till appen Kontakter och leta efter alternativet Exportera till VCF.


** Från iOS** - Använd en app som Export Contact och använd exportalternativet "vCard" för att exportera en VCF-fil.

När du har VCF-filen kan du överföra den till din GrapheneOS-enhet med ett externt lagringsalternativ som microSD-kort eller USB-enhet. Om du inte har något av dessa till hands kan du välja att dela via en av de många appar som listas nedan.


![image](assets/4.webp)


Personlig startskärm



## Alternativa appar


För att göra din telefon användbar kommer du att vilja installera några applikationer! Alternativen som följer ingår eftersom jag har använt dem alla personligen eller för att de får starka rekommendationer från den bredare integritetsgemenskapen. Det finns många andra bra alternativ tillgängliga som inte nämns, och [Awesome Privacy](https://awesome-privacy.xyz) erbjuder en otroligt omfattande lista över integritetsbevarande applikationer för alla typer av enheter.


Bara för att en app är Free and Open Source Software (FOSS) betyder det inte att den är fri från potentiella integritetsläckor. Använd [Exodus](https://reports.exodus-privacy.eu.org/en/) för att se hur dina föredragna appar presterar mot deras integritetsgranskningar.


### F-Droid


[F-Droid](https://f-droid.org/) är en installerbar katalog med FOSS-program för Android. Klienten gör det enkelt att bläddra bland, installera och uppdatera applikationer på din enhet. Det är värt att nämna att uppdateringar via F-Droid ibland kan vara långsammare än med andra appbutiker. Detta beror främst på om appen hittas via F-Droids huvudarkiv eller ett anpassat arkiv.


För att installera F-Droid går du bara till deras webbplats via en webbläsare på din GrapheneOS-telefon och trycker på nedladdning. Detta kommer att ladda ner en `.apk`-fil. Du kommer då att bli tillfrågad om du vill installera appen.


Förutom applikationer som finns i standardförvaret i F-Droid, kommer många Open Source-projekt också att vara värd för sitt eget arkiv som kan läggas till i F-Droid-appinställningarna. Om så är fallet kommer projektet i fråga att leda dig genom de mycket enkla steg som krävs för att uppnå detta på deras webbplats.


![image](assets/5.webp)


F-Droid startskärm


### Aurora butik


[Aurora Store] (https://auroraoss.com/) är en FOSS-version av Google Play Store. Aurora ser ut och känns mycket lik den traditionella Play Store och låter dig ladda ner och uppdatera alla appar som du normalt skulle hitta via Google-alternativet.


Killerfunktionen i Aurora är anonym inloggning. Det betyder att du kan ladda ner alla dina favoritappar som inte är tillgängliga via F-Droid eller direkt APK, utan att behöva vara inloggad på ditt Google-konto.


Innan du skyndar dig att göra detta till ditt standardinstallationsalternativ, kom ihåg att många av de applikationer vi försöker komma bort från installerades från Play Store. Bara för att de är tillgängliga från Aurora ändrar inte det faktum att vissa kan ha spårningsfunktioner inbäddade. Det kommer inte alltid att vara möjligt, men när du kan, leta efter ett F-Droid-alternativ innan du laddar ner via Aurora.


För att installera Aurora, sök bara efter "Aurora Store" i F-Droid.


Aurora har också några potentiella attackvektorer, eftersom de "anonyma kontona" verkligen skapas och kontrolleras av Aurora. De kan i teorin servera skadliga uppdateringar eller driva appar till din telefon, även om du fortfarande måste acceptera installationsprompten på enheten. Aurora har också ibland några problem med att appar inte dyker upp på grund av felavläsningar av region och enhet. Detta kan vanligtvis arbetas runt med stegen nedan.


**Topptips** - Ibland kommer Aurora Store att uppleva hastighetsbegränsning vilket begränsar din förmåga att söka och installera appar. För att komma runt detta går du till **Inställningar** > **Appar** > **Aurora** > **Öppna som standard** och lägger sedan till domänen `play.google.com`. Nu, när du navigerar till en produkt eller tjänsts webbplats som har länken "Ladda ner via Play Store", trycker du på den för att öppna den appen i Aurora så att du kan ladda ner den.



![image](assets/6.webp)


Aurora Store startskärm


### APK-nedladdning


Appar på Android kan också laddas ner och installeras via en `.apk`-fil. Det här är ett bra alternativ som inte kräver några appbutiker från tredje part, utan det räcker att ladda ner filen direkt från projektets eller tjänstens webbplats eller GitHub-arkiv.


Nackdelen med detta tillvägagångssätt är att du inte får automatiska uppdateringar, så du måste övervaka den tjänstens kommunikationskanaler för att lära dig om nya utgåvor. Det finns dock ett fantastiskt projekt som heter Obtanium som syftar till att åtgärda detta. [Obtainium](https://github.com/ImranR98/Obtainium) låter dig installera och uppdatera Open-Source-appar direkt från deras release-sidor och få meddelanden när nya releaser görs tillgängliga.


![image](assets/7.webp)


Obtanium förhandsgranskning


### Webbappar


När du kanske vill använda en tjänst sällan och inte vill ladda ner en inbyggd applikation kan du helt enkelt komma åt webbversionen. Många webbplatser erbjuder numera också stöd för Progressive Web App (PWA). Det innebär att du kan lägga till ett bokmärke för en viss webbplats (t.ex. Twitter.com) på telefonens startskärm. När du sedan trycker på ikonen öppnas den som en fullskärmsapplikation utan de vanliga distraktionerna som följer med den typiska webbläsarupplevelsen. Du kan se ett exempel på hur detta ser ut nedan.


För att göra detta i Vanadium, GrapheneOS inbyggda webbläsare, navigerar du helt enkelt till önskad webbplats, trycker på de tre vertikala prickarna i skärmens övre högra hörn och trycker sedan på **'Lägg till på startskärmen'**.


Den enda nackdelen med detta tillvägagångssätt är att eftersom detta bara är en bokmärkt webbsida får du inte någon form av meddelanden. Även om vissa kanske ser det som positivt!


![image](assets/8.webp)


Twitter PWA


### Webbläsare


Det går inte att göra fel med det färdigpaketerade alternativet Vanadium. Appen beter sig identiskt med alla andra mobila webbläsare jag har provat och jag har inte en enda gång haft några kompatibilitetsproblem.


För tillfällen när du behöver komma åt Tor native `.onion`-webbplatser kan du ladda ner Tor Browser APK direkt från deras [webbplats] (https://www.torproject.org/download/#android) eller via F-Droid.


### VPN-tjänster


För att skydda din onlineaktivitet från din snokande internetleverantör (ISP) är en VPN-app (Virtual Private Network) ett bra alternativ. Ett VPN skickar din internettrafik i en krypterad tunnel till en delad IP Address som kontrolleras av VPN-tjänsteleverantören för att säkerställa att din enhetsaktivitet inte kan kopplas till dig.


Följande är 3 väl respekterade alternativ som gör att du kan betala för tjänsten i Bitcoin och utan att tillhandahålla någon personlig information. Alla 3 alternativen är tillgängliga via F-Droid.



- [Mullvad] (https://f-droid.org/packages/net.mullvad.mullvadvpn/)
- [Proton] (https://f-droid.org/en/packages/ch.protonvpn.android/)
- [iVPN](https://f-droid.org/en/packages/net.ivpn.client/)


### Meddelanden


På senare år har det blivit allt vanligare med lösningar för krypterade meddelanden. Problemet kvarstår dock: du kan ha det bästa och mest privata alternativet installerat på din telefon, men om du inte har några kontakter som använder det, vad är då poängen?


De flesta människor som inte har något intresse för integritetsutrymmet kommer sannolikt att använda WhatsApp eller iMessage. Den förstnämnda kan laddas ner via Aurora Store men den senare kommer inte att fungera på GrapheneOS (uppenbarligen!).



- [Signal] (https://signal.org/) är en av de mer populära end-to-end-krypterade (E2EE) budbärarna som har en stark meritlista och en rik uppsättning funktioner. Signal kräver ett telefonnummer för att registrera sig, så om du planerar att chatta med människor som du helst inte vill veta ditt telefonnummer, kanske du ska titta på några av alternativen. Signal måste laddas ner via Aurora Store.
- [Simplex](https://f-droid.org/en/packages/chat.simplex.app/) är en ganska ny E2EE messenger. Den har inget användar-ID, kräver inget telefonnummer eller personlig information. Folk hittar dig genom att skanna din personliga QR-kod eller genom att besöka din unika länk. Simplex gör det också möjligt för avancerade användare att köra sin egen server för att ytterligare minska beroendet av någon centraliserad enhet. Simplex har ingen desktop-klient, så det kanske inte är lämpligt om flera enheter är på din prioriteringslista. Simplex för Android finns tillgängligt via F-Droid.
- [Threema] (https://threema.ch/en/faq/libre_installation) erbjuder en liknande upplevelse som Simplex, men har funnits längre och känns därför lite mer polerad. Threema är inte gratis, en livstidslicens kostar 4,99 USD och kan köpas med Bitcoin. Threema erbjuder en webbklient och inbyggda skrivbordsapplikationer. Android-applikationen är tillgänglig via F-Droid.
- [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/) är en inofficiell FOSS Fork av den officiella Telegram-appen för Android. Telegram har E2EE "hemliga chattar", men standardalternativet är inte privat. Telegram FOSS kan laddas ner från F-Droid.


![image](assets/9.webp)

Vänster: Threema, höger: Simplex


### Media



- [Spotube] (https://f-droid.org/packages/oss.krtirtho.spotube/) är en plattformsoberoende Spotify-klient som inte kräver ett Premium-konto. Spotube är tillgängligt via F-Droid.
- [ViMusic] (https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/) är en fantastisk applikation för att ånga all musik från YouTube-musik, gratis. ViMusic är tillgängligt från F-Droid.
- [Newpipe] (https://f-droid.org/packages/org.schabi.newpipe/) erbjuder en YouTube-upplevelse utan irriterande annonser och tvivelaktiga behörigheter. Med NewPipe kan du prenumerera på kanaler, lyssna i bakgrunden och till och med ladda ner för offlinevisning. NewPipe är tillgängligt via F-Droid.
- [AntennaPod] (https://f-droid.org/packages/de.danoeh.antennapod/) är en podcastspelare som låter dig prenumerera på och hantera alla dina favoritprogram. AntennaPod är tillgänglig via F-Droid.


![image](assets/11.webp)

Till vänster: Spotube, till höger: ViMusic


### Kartor


Om du vill ha röstassistans när du kör och använder en kartapp i GrapheneOS måste du installera [RHVoice] (https://rhvoice.org/installation/) och [configure] (https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available).



- [Magic Earth] (https://www.magicearth.com/) är ett kartalternativ som stöder turn-by-turn-navigering, 3D- och offline-kartor. Magic Earth kan laddas ner från Aurora Store.
- [Organic Maps] (https://f-droid.org/en/packages/app.organicmaps/) är kartalternativ för resenärer, turister, vandrare och cyklister baserat på toppen av OpenStreetMap-data från massor. Det är en integritetsfokuserad Fork med öppen källkod av Maps.me-appen (tidigare känd som MapsWithMe). Den stöder 100% av funktionerna utan en aktiv internetanslutning och kan laddas ner från F-Droid.
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/) är ett annat bra kartalternativ som stöder alla funktioner som nämns ovan.


![image](assets/13.webp)

Till vänster: Magic Earth, till höger: Organiska kartor


### E-post



- [Proton Mail] (https://proton.me/mail) erbjuder en gratis privat e-posttjänst som stöder granskad E2EE. Proton erbjuder också en betald version som stöder anpassade domäner och [aliasing] (https://proton.me/support/creating-aliases). Proton Mail kan laddas ner som en direkt APK eller via Aurora.
- [Tutanota] (https://tutanota.com/) erbjuder samma funktioner som Proton Mail, inklusive valfria betaltjänster och kan laddas ner som en direkt APK eller via F-Droid.
- [K-9 Mail] (https://f-droid.org/en/packages/com.fsck.k9/) är en e-postklient med öppen källkod som fungerar med i princip alla e-postleverantörer. Den stöder flera konton, en enhetlig inkorg och OpenPGP-krypteringsstandarden.


![image](assets/15.webp)

Till vänster: Proton Mail, till höger: Tutanota


### Produktivitet



- [Syncthing] (https://f-droid.org/packages/com.nutomic.syncthingandroid/) är ett program för filsynkronisering. Det synkroniserar filer mellan två eller flera enheter i realtid, säkert skyddade från nyfikna ögon. Dina data är enbart dina data och du förtjänar att välja var de lagras, om de delas med någon tredje part och hur de överförs via internet. Syncthing är tillgängligt via F-Droid.
- [KDE Connect] (https://f-droid.org/packages/org.kde.kdeconnect_tp/) alla dina enheter så att de enkelt kan prata med varandra när de är anslutna till ditt hemnätverk. Skicka enkelt filer, foton, urklippsdata över alla dina enheter (även på iOS!). KDE connect kan laddas ner från F-Droid.
- [Notesnook] (https://f-droid.org/en/packages/com.streetwriters.notesnook/) är en E2EE-anteckningsapplikation för att synkronisera dina tankar och att-göra-listor över alla dina enheter. Deras gratis plan bör täcka de flesta personliga användningsfall. Notesnook är tillgängligt på F-Droid.
- [Standard Notes] (https://f-droid.org/en/packages/com.standardnotes/) är mycket lik Notesnook, men kräver en betalplan för att matcha funktionsuppsättningen. Standard Notes är tillgängligt via F-Droid.
- [Anysoft Keyboard] (https://f-droid.org/packages/com.menny.android.anysoftkeyboard/) är en tangentbordsapp som låter dig anpassa i stort sett allt du kan tänka dig när det gäller din telefonskrivningsupplevelse. Den kan laddas ner via F-Droid.
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US) är standardappen för Googles tangentbord. Enligt min erfarenhet erbjuder den den överlägset bästa skriv- och svepupplevelsen. Om du laddar ner den här appen, se till att du helt inaktiverar alla nätverksrelaterade behörigheter. Den kan laddas ner via Aurora.


![image](assets/17.webp)

Till vänster: Notesnook, till höger: KDE Connect


### Livsstil



- [Geometric Weather] (https://f-droid.org/en/packages/wangdaye.com.geometricweather/) är en vackert designad väderapp med öppen källkod som är tillgänglig via F-Droid. Den stöder också widgets i olika storlekar så att du kan se vädret på din valda plats direkt från din startskärm.
- [Translate You] (https://f-droid.org/packages/com.bnyro.translate/) är en öppen källkod och integritetsbevarande översättningsapp som stöder mer än 200 språk. Translate You är tillgänglig via F-Droid.
- [Proton Calendar] (https://proton.me/calendar/download) är en enkel att använda E2EE som interagerar sömlöst med dina Proton-e-postkonton. Proton Calendar kan laddas ner som en APK eller via Aurora-butiken.
- [PassAndroid] (https://f-droid.org/en/packages/org.ligi.passandroid/) är en app för visning och lagring av boardingkort, kuponger, biobiljetter och medlemskort etc. Ladda bara ner den relevanta filen "pkpass" eller "espass" och öppna den med appen. PassAndroid är tillgängligt via F-Droid.


![image](assets/19.webp)

Till vänster: Geometriskt väder, till höger: Protonkalender


### Säkerhet/Privatliv



- [Bitwarden] (https://mobileapp.bitwarden.com/fdroid/) erbjuder en gratis och E2EE cross platform lösenordshanteringslösning för alla dina enheter. Deras betalda tjänst låter dig integrera 2FA-koder i appen. Serversidan av Bitwarden kan vara värd för sig själv och Android-appen är tillgänglig via F-Droid.
- [Proton Pass] (https://proton.me/pass/download) erbjuder en liknande gratistjänst som Bitwarden, men [Proton Unlimited] (https://proton.me/pricing) kunder kan få tillgång till ytterligare avancerade funktioner. Proton Pass är tillgängligt via APK eller Aurora.
- [FreeOTP] (https://f-droid.org/packages/org.fedorahosted.freeotp/) är ett program för tvåfaktorsautentisering för system som använder engångslösenordsprotokoll. Tokens kan enkelt läggas till genom att skanna en QR-kod. FreeOTP är tillgängligt via F-Droid.
- [Aegis] (https://f-droid.org/en/packages/com.beemdevelopment.aegis/) är en gratis, säker och Open Source-app för Android för att hantera dina 2-stegsverifieringstoken för dina onlinetjänster. Aegis är tillgänglig via F-Droid.
- [Cryptomator] (https://f-droid.org/en/packages/org.cryptomator.lite/) är en betald, plattformsoberoende tjänst som krypterar dina data lokalt så att du säkert kan ladda upp dem till din favoritmolntjänst. Cryptomator kan laddas ner via F-Droid.


![image](assets/21.webp)

Till vänster: Proton Pass, till höger: Bitwarden


### Molnlösningar



- [Proton Drive] (https://proton.me/drive/download) är en betald E2EE-molnlösning för säkerhetskopiering och lagring av alla dina filer. I skrivande stund har de just meddelat en Windows desktop-klient, men Mac- och Linux-användare måste fortsätta att använda webbversionen för att synkronisera från sina datorer (för tillfället). Android-klienten är tillgänglig som en APK eller via Aurora.
- [Skiff] (https://skiff.com/download) erbjuder också betalda E2EE molnlagrings- och filsamarbetsverktyg. De erbjuder en Mac- och Windows-skrivbordsklient (såväl som en webbapp) och deras Android-klienter måste laddas ner från Aurora.
- [Nextcloud] (https://f-droid.org/en/packages/com.nextcloud.client/) erbjuder en heltäckande molnbaserad lösning för samarbete, synkronisering mellan enheter och fillagring. Mer avancerade användare kan välja att själva vara värd för sin programvara med fri och öppen källkod på vilken hårdvara de vill. Android-klienterna kan laddas ner via F-Droid.
- [Cryptpad] (https://cryptpad.fr/) erbjuder ett gratis, webbaserat, E2EE-alternativ till Google Docs.


![image](assets/23.webp)

Proton Drive


## Nackdelarna


Det finns gott om alternativ med öppen källkod och integritetsskyddande alternativ till de applikationer från teknikkonglomerat som du har vant dig vid att använda, och vissa av dem är ofta bättre än alternativen med sluten källkod och spionprogram.


Men när du går över till GrapheneOS finns det vissa bekvämligheter som du måste ge upp på grund av att det inte finns några alternativ. Dessa inkluderar:



- Apple CarPlay/Android Auto** - Du kommer att behöva hålla dig till gammal hederlig Bluetooth, USB eller Aux.
- Apple/Google Pay** - I stort sett alla bär med sig sin Wallet i alla fall!
- Bankappar** - Det är inte så att de inte fungerar alls. Vissa gör det, perfekt faktiskt. Andra fungerar bara med Google Play Services aktiverat (läs mer om det nedan) och andra fungerar helt enkelt inte alls. Läs rapporten om din bank [här](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/) för att se hur läget ser ut just nu. Oroa dig inte om din bank finns med på listan över banker som inte fungerar, kom ihåg att du bara kan spara webbadressen som en webbapp på din startskärm.
- Push Notifications** - De flesta applikationer som skickar dig uppdateringar när du inte använder en specifik app gör det via Google Play Services. Dessa installeras inte som standard med GrapheneOS, så om du upptäcker att du inte meddelas omedelbart när din vän skickar ett e-postmeddelande till dig, är det troligtvis därför. Den goda nyheten är att några av de appar som nämns ovan har implementerat sin egen bakgrundsanslutning för att regelbundet söka efter uppdateringar och sedan ge dig ett meddelande där så krävs


### Sandlåda för Google Play


**Observera att:** GrapheneOS har en kompatibilitets-Layer som ger möjlighet att installera och använda de officiella versionerna av Google Play i den vanliga app-sandlådan. Google Play får absolut ingen speciell åtkomst eller privilegier på GrapheneOS i motsats till att kringgå app-sandlådan och få en enorm mängd mycket privilegierad åtkomst.


Om du upptäcker att du helt enkelt inte kan leva utan dessa push-meddelanden för din favoritapp eller att en viss "måste ha"-app är värdelös utan Play Services, låter GrapheneOS dig [installera](https://grapheneos.org/usage#sandboxed-google-play-installation) dessa tjänster i en helt sandboxad miljö. När de väl är installerade kräver dessa tjänster inget Google-konto för att fungera, och varje tjänsts behörigheter kan kontrolleras noggrant.


Innan du skyndar dig att installera dessa på dag 1, uppmanar jag dig att se hur långt du kommer utan dem. Du kommer förmodligen att bli förvånad över hur många appar som fungerar helt normalt utan.


Om du vill installera dem trycker du helt enkelt på den förinstallerade applikationen "Appar" följt av "Google Play Services". Överväg att installera dem tillsammans med de mindre privata appar som du inte kan leva utan, i en helt separat användarprofil för att ge den extra Layer av segregering från resten av din telefon.


![image](assets/24.webp)

Installationsskärm för Play Services


### Profiler


GrapheneOS gör att du kan ha en separat telefonupplevelse, i din telefon. Ytterligare profiler kan installera sina egna appar och tjänster och kan inte komma åt några filer eller data från ägarkontot.

Om du bara har en eller två av dessa måste-ha-appar som kräver Play Services, men som bara används mycket sällan, kan det vara en bra idé att installera dem tillsammans med Play Services i en separat profil för att ytterligare stärka eventuella små integritetskonsekvenser som kvarstår genom att ha dem körda i ägarprofilen.


Du kan läsa mer om detta användningsfall [här] (https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2).


Om du bestämmer dig för att lägga till en separat profil för att passa ditt användningsfall kan appen [Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/) vara användbar för dig. Med Insular kan du enkelt klona någon av dina befintliga appar till den nya profilen utan att behöva gå via någon av de traditionella installationsvägarna som beskrivs tidigare i den här guiden. Med Insular kan du också snabbt "frysa" någon av dessa appar för att helt inaktivera alla appens bakgrundstjänster från att köras.


![image](assets/24.webp)

Skärmen för hantering av användarprofiler


### e-Sims


Om du vill ta din telefonintegritet till nästa nivå och ha en mobiltjänst som är avskild från din identitet i den verkliga världen, kan en eSIM vara något för dig. Ett eSIM är ett virtuellt SIM-kort som du kan köpa online och lägga till i din telefon via en QR-kod. Företag som erbjuder sådana tjänster som kan betalas anonymt med Bitcoin inkluderar [Silent.Link] (https://silent.link/) och [Bitrefill] (https://www.bitrefill.com/gb/en/esims/).


eSIM ska inte ses som ett komplett universalmedel för telefonsekretess. De kan vara ett användbart verktyg när de är i rätt händer, men gör din forskning om [tradeoffs] (https://grapheneos.org/faq#cellular-tracking) för att använda någon typ av mobiltjänst om du tänker gå helt "off grid".


Sandboxed Play Services måste installeras för eSIM-försörjning i GrapheneOS.


## Säkerhetskopior


När du har installerat din nya de-Google'd Pixel-telefon är det en bra idé att skapa en säkerhetskopia. Denna säkerhetskopia gör att du kan återställa telefonen till ett identiskt tillstånd om du tappar bort din telefon eller om den tappas bort / stjäls.


Du kan välja att lagra säkerhetskopian på valfritt externt lagringsmedium eller i en molnlösning som Nextcloud, även om vissa användare rapporterar varierande framgångar med det senare alternativet.


Så här skapar du din första säkerhetskopia:


1. Gå till **Inställningar** > **System** > **Backup** och skriv sedan ner din återställningskod på 12 ord. Denna kod krävs för att dekryptera säkerhetskopian vid ett senare tillfälle. Förlorar du koden förlorar du åtkomsten till telefonens säkerhetskopia.

2. Välj sedan din lagringsplats. Jag rekommenderar ett externt USB-minne eller ett microSD-kort av industriell kvalitet.

3. Välj vilka data som ska säkerhetskopieras. Om du har utrymme på det angivna lagringsmediet rekommenderar jag att du väljer allt.

4. Tryck på de tre prickarna längst upp till höger och välj **Säkerhetskopiera nu**.


![image](assets/26.webp)


Skärm för säkerhetskopiering


Kom ihåg att om du gör offline-säkerhetskopior till externa lagringsmedier är det klokt att slutföra detta steg regelbundet för att säkerställa att viktiga uppdateringar av telefonen inte går förlorade om det värsta skulle hända.


![video](https://www.youtube.com/embed/eyWmcItzisk)


Video som beskriver säkerhetskopieringsprocessen


## Slutsats


Under de senaste åren har GrapheneOS-mjukvaran mognat avsevärt. Den är stabilare och mer kompatibel än någonsin. Detta i kombination med det blomstrande ekosystemet för öppen källkod och integritetsskyddande appar gör GrapheneOS till ett verkligt gångbart alternativ till Android eller iOS, även för "vanliga" människor som du!


Dataintrång och övervakning är så vanligt förekommande i dagens värld att det knappt skapar rubriker längre. Det är upp till dig att skydda dig själv. Det kommer att krävas justeringar och uppoffringar längs vägen, men att minska din exponering för sådana intrång är inte alls så svårt som du tror.


Jag hoppas att den här guiden på något sätt kan hjälpa dig på din resa. Om du tyckte att den här guiden var användbar och vill stödja mitt arbete kan du överväga att skicka en [donation](/tips).


Om du är en befintlig GrapheneOS-användare, eller blir en som ett resultat av denna guide, kan du överväga att [donera](https://grapheneos.org/donate) för att stödja deras viktiga arbete.


### Läs mer om detta


GrapheneOS är ett kaninhål som vem som helst lätt kan spendera veckor på att gå ner. Det finns bara så mycket du kan lära dig och pilla med för att skräddarsy upplevelsen efter dina krav och hotmodeller. Nedan finns några länkar där du kan fortsätta din resa:



- [GrapheneOS officiella användarhandbok](https://grapheneos.org/usage) - Officiell webbplats
- [GrapheneOS Forum](https://discuss.grapheneos.org/) - Officiell webbplats
- [GrapheneOS Settings Masterclass] (https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - Video av 'The Privacy Wayfinder'
- [GrapheneOS General Podcast] (https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - Podcast av "Watchman Privacy


full kredit till: https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md