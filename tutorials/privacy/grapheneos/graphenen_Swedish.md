# GrapheneOS

> "[GrapheneOS](https://grapheneos.org/) är ett mobiloperativsystem fokuserat på integritet och säkerhet med Android-appkompatibilitet, utvecklat som ett ideellt open source-projekt."

GrapheneOS, grundat ursprungligen 2014 som 'CopperheadOS', är baserat på den traditionella Android-koden (AOSP), men med många förändringar och förbättringar som syftar till att förbättra användarens integritet och säkerhet. GrapheneOS ger användaren kontroll över sin telefon, inte de stora teknikföretagen.

### Innehållsförteckning:

- Introduktion
- Förberedelse
- Installation
- Appalternativ
- Nackdelar
- Användbar information

Guide av https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md

## Varför använda GrapheneOS?

Moderna telefoner är $500-$1000 spårnings- och dataskördedevicer. Varje aspekt av vårt liv går genom dem, och tyvärr delas mycket av denna data med tredje parter på något sätt. GrapheneOS är byggt specifikt för att minska denna datadelning och förbättra enhetens säkerhet mot potentiella angreppspunkter. Det finns inget sådant som ett GrapheneOS-konto. Du behöver inte ett för att ladda ner appar eller interagera med operativsystemet. Helt enkelt sagt, du är inte produkten.

GrapheneOS ger extra säkerhet till din Android-upplevelse genom några enkla grundprinciper.

1. **Minskning av attackyta** - Ta bort onödig kod (eller bloatware).
2. **Förebyggande av sårbarheter** - Ge användaren tillräckligt med detaljer för att välja de kompromisser de är bekväma med.
3. **Sandbox-isolering** - GrapheneOS förstärker befintliga Android-sandboxar och låser ytterligare ner varje apps förmåga att kommunicera med resten av din telefon.

Läs mer om tekniska detaljer om GrapheneOS funktioner [här](https://grapheneos.org/features).

### Underlätta övergången

Om du har varit fast i Google- eller Apple-ekosystemet i flera år kan tanken på att förlora all den bekvämligheten över en natt vara skrämmande. Men med några noggrant övervägda beslut om appinstallation (som kommer att täckas senare), kan mycket av denna förväntade svårighet minskas eller elimineras.

Så bra som alternativen blir kan tanken på en sådan förändring fortfarande vara avskräckande. Om du befinner dig i den här situationen är mitt bästa råd att köra din nya GrapheneOS-enhet parallellt med din befintliga telefon ett tag. Därifrån kan du successivt vänja dig av med 2-3 appar per vecka tills du bara använder din GrapheneOS-enhet.

Om du väljer detta tillvägagångssätt, var strikt mot dig själv och bryt ditt beroende av övervakade alternativ så snabbt som möjligt. Vi människor är lata och väljer ofta den enklaste vägen. Kom ihåg varför du bytte i första hand.

**Istället för att betala med din personliga data valde du att betala med din tid och ibland dina hårt intjänade pengar (beroende på vilka alternativa appar du installerar).**

## Komma igång

GrapheneOS finns för närvarande endast tillgängligt för _(ganska ironiskt)_ [Google Pixel](https://grapheneos.org/faq#supported-devices)-serien av telefoner. Detta är inte utan goda skäl. Pixel-telefoner erbjuder den bästa hårdvarubaserade säkerheten för att komplettera arbetet med att förstärka operativsystemet. Det inkluderar saker som specifik komponentisolering och verifierad uppstart.

### Välja en enhet

När du väljer den Pixel-enhet du vill installera GrapheneOS på, se till att du kontrollerar hur länge enheten kommer att få standard [säkerhetsuppdateringar](https://support.google.com/pixelphone/answer/4457705?hl=sv#zippy=%2Cpixel-xl-a-a-g-a-g).
Vid tidpunkten för skrivandet är Pixel 6a den billigaste modellen som finns tillgänglig med bra långsiktigt stöd, garanterat fram till juli 2027. Om du väljer denna modell kommer inte OEM-upplåsning att fungera med den version av den ursprungliga operativsystemet från fabriken. Du måste uppdatera den till juni 2022-versionen eller senare via en överföring över luften. Efter att du har uppdaterat den måste du också återställa enheten till fabriksinställningarna för att fixa OEM-upplåsning. Alla andra modeller som är operatörsupplåsta kommer att vara redo för GrapheneOS direkt ur lådan.

När du väljer en enhet vill du också se till att du köper en olåst version. Vissa operatörer som Verizon skickar sina enheter med låst bootloader, vilket helt förhindrar följande process.

### Installation av GrapheneOS

GrapheneOS [webbinstallationsprogram](https://grapheneos.org/install/web) gör hela processen enkel och kan slutföras av vem som helst på mindre än 10 minuter.
Följande instruktioner är en nedkortad version som är hämtad från länken ovan.

Allt du behöver ha till hands är:

- Pixel-enheten
- En USB-kabel för att ansluta telefonen till din dator
- En dator med en webbläsare (vilken Chromium-baserad webbläsare som helst: Chrome, Edge, Brave, etc.)

1. Det första steget är att gå till **Inställningar** > **Om telefonen** och trycka upprepade gånger på byggnumret tills du ser att **'Utvecklarläge'** är aktiverat.
2. Gå sedan till **Inställningar** > **System** > **Utvecklaralternativ** och aktivera **'OEM-upplåsning'**.
3. Starta om enheten och håll volym ned-knappen nedtryckt medan telefonen startar om.
4. Anslut telefonen till din laptop och om du blir ombedd att godkänna anslutningen, tillåt den.
5. På webbinstallationsprogrammets sida klickar du på 'Lås upp bootloader'.
6. Du kommer sedan att se att telefonalternativen ändras. Använd volymknappen för att ändra urvalet till `lås upp` och använd strömbrytaren för att acceptera.
7. Klicka sedan på 'Ladda ner version' på webbinstallationsprogrammets sida.
8. När nedladdningen är klar, gå vidare till nästa steg och klicka på 'Flasha version'. Detta tar en eller två minuter och du behöver inte röra telefonen alls.
9. Slutligen, gå till nästa steg i webbinstallationsprogrammet och klicka på **Lås bootloader**. Du behöver ändra urvalet och bekräfta med strömbrytaren på samma sätt som du gjorde tidigare i processen.
10. När du ser ordet `Start`, bekräfta detta med strömbrytaren och enheten kommer att starta i ditt nya Google-fria operativsystem.

<p align="center">
  <img src="assets/2.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>GrapheneOS startskärm</b>
</p>

_Efter den första starten och inställningen är det bra att inaktivera OEM-upplåsning från Inställningar > System > Utvecklaralternativ._

_Du kan också vilja ta det extra, valfria men rekommenderade steget att verifiera installationen via Auditor-appen. Du behöver en separat Android-telefon med appen installerad för att slutföra detta steg. Instruktioner för detta finns [här](https://attestation.app/tutorial)._

<p align="center">
<iframe width="100%" height="315" src="https://www.youtube.com/embed/L1KZWjZVnAw" class=responsive title="YouTube-videospelare" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>

<p align="center">
  Video som beskriver de enkla stegen ovan
</p>

Om dessa enkla steg verkar vara för mycket kan du överväga att köpa en Pixel med GrapheneOS-programvaran [förinstallerad](https://ronindojo.io/en/roninmobile). Var bara medveten om att du lägger en liten mängd förtroende i leverantören.

### Förinstallerade appar

Nu när du är igång kanske du märker hur avskalad GrapheneOS verkar vid första installationen. Som standard kommer du att ha dessa appar installerade:

<p align="center">
  <img src="assets/3.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>Standardappar</b>
</p>

De enda två du kanske inte är bekant med är 'Auditor' och 'Vanadium'.

- 'Appen [Auditor](https://play.google.com/store/apps/details?id=app.attestation.auditor) använder hårdvarubaserade säkerhetsfunktioner för att validera identiteten hos en enhet tillsammans med äktheten och integriteten hos operativsystemet. Den kommer att verifiera att enheten kör det ursprungliga operativsystemet med låst bootloader och att ingen manipulering av operativsystemet har skett.'
- [Vanadium](https://github.com/GrapheneOS/Vanadium) är en integritets- och säkerhetsförstärkt variant av webbläsaren Chromium.

## Anpassning

Telefoninställningar är en personlig sak, men här är några av de första sakerna jag ändrar när jag installerar GrapheneOS för att känna mig mer hemma.

### Ställa in en bakgrundsbild och uppdatera temat

Gå till Inställningar > Bakgrundsbild och stil. Här gör jag följande:

- Uppdaterar bakgrundsbilderna för hem- och låsskärmen med bilder som laddats ner från webben.
- Väljer accentfärger som används i hela gränssnittet.
- Aktiverar mörkt tema.

### Visa batteriprocent

Gå till **Inställningar** > **Batteri**, och aktivera sedan **Visa batteriprocent** i statusfältet.

### Importera kontakter

**Från en annan Android-telefon** - Gå till Kontakter-appen och leta efter alternativet Exportera till VCF.

**Från iOS** - Använd en app som Export Contact och använd exportalternativet 'vCard' för att exportera en VCF-fil.
När du har VCF-filen kan du överföra den till din GrapheneOS-enhet med en extern lagringsenhet som microSD-kort eller USB-enhet. Om du inte har något av dessa till hands kan du välja att dela via någon av de många appar som listas nedan.

<p align="center">
  <img src="assets/4.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>Personligt anpassad startsida</b>
</p>

## Alternativa appar

För att göra din telefon användbar kommer du att vilja installera några appar! De alternativ som följer är inkluderade eftersom jag personligen har använt dem alla eller för att de får starka rekommendationer från den bredare integritetsgemenskapen. Det finns många andra bra alternativ tillgängliga som inte nämns, och [Awesome Privacy](https://awesome-privacy.xyz) erbjuder en otroligt omfattande lista över integritetsbevarande appar för alla typer av enheter.
Bara för att en app är gratis och öppen källkod (FOSS) betyder det inte att den är fri från potentiella integritetsläckor. Använd [Exodus](https://reports.exodus-privacy.eu.org/en/) för att se hur dina föredragna appar presterar i sina integritetsrevisioner.

### F-Droid

[F-Droid](https://f-droid.org/) är en installerbar katalog med FOSS-applikationer för Android. Klienten gör det enkelt att bläddra, installera och uppdatera applikationer på din enhet. Det är värt att nämna att uppdateringar via F-Droid ibland kan vara långsammare än med andra appbutiker. Detta beror främst på om appen hittas via huvud-F-Droid-förrådet eller ett anpassat förråd.

För att installera F-Droid går du helt enkelt till deras webbplats via en webbläsare på din GrapheneOS-telefon och trycker på nedladdning. Detta kommer att ladda ner en `.apk`-fil. Du kommer sedan att bli ombedd om du vill installera appen.

Förutom applikationer som finns i standardförrådet i F-Droid kommer många öppen källkodsprojekt också att ha sitt eget förråd som kan läggas till i F-Droid-appens inställningar. Om så är fallet kommer projektet i fråga att guida dig genom de mycket enkla stegen som krävs för att uppnå detta på deras webbplats.

<p align="center">
  <img src="assets/5.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>F-Droids startsida</b>
</p>

### Aurora Store

[Aurora Store](https://auroraoss.com/) är en FOSS-version av Google Play-butiken. Aurora ser ut och känns mycket lik den traditionella Play Store och låter dig ladda ner och uppdatera vilken app som helst som du normalt skulle hitta via Google-alternativet.

Auroras killer-funktion är anonym inloggning. Detta innebär att du kan ladda ner vilka av dina favoritappar som inte är tillgängliga via F-Droid eller direkt APK, utan att vara inloggad på ditt Google-konto.

Innan du skyndar dig att göra detta till ditt standardinstallationsalternativ, kom ihåg att många av de applikationer vi försöker komma ifrån installerades från Play Store. Bara för att de är tillgängliga från Aurora förändrar inte det faktum att vissa kan ha spårningsfunktioner inbäddade. Det kommer inte alltid att vara möjligt, men när du kan, leta efter ett F-Droid-alternativ innan du laddar ner via Aurora.

För att installera Aurora, sök helt enkelt efter 'Aurora Store' i F-Droid.

Aurora har också några potentiella attackvektorer, eftersom "anonyma konton" egentligen skapas och kontrolleras av Aurora. De skulle i teorin kunna leverera skadliga uppdateringar eller pusha appar till din telefon, även om du fortfarande måste acceptera installationsprompten på enheten. Aurora har ibland också problem med att appar inte visas på grund av region- och enhetsfelavläsningar. Detta kan vanligtvis åtgärdas med stegen nedan.

**Topp tips** - Ibland kommer Aurora Store att uppleva begränsningar av sökning och installation av appar. För att komma runt detta går du till **Inställningar** > **Appar** > **Aurora** > **Öppna som standard**, och lägg sedan till domänen `play.google.com`. Nu, när du navigerar till en produkts eller tjänsts webbplats som har länken 'Ladda ner via Play Store', kommer att trycka på den öppna den appen inom Aurora för att ladda ner den.

<p align="center">
  <img src="assets/6.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>Aurora Stores startsida</b>
</p>

### APK-nedladdning

Appar på Android kan också laddas ner och installeras via en `.apk`-fil. Detta är ett bra alternativ som inte kräver några tredjepartsappbutiker, helt enkelt ladda ner filen direkt från projektets eller tjänstens webbplats eller GitHub-förvar.
Nackdelen med detta tillvägagångssätt är att du inte får automatiska uppdateringar, så du måste övervaka den tjänstens kommunikationskanaler för att ta reda på nya versioner. Men det finns ett bra projekt som heter Obtanium som syftar till att fixa detta. [Obtainium](https://github.com/ImranR98/Obtainium) låter dig installera och uppdatera öppen källkodsappar direkt från deras versionsidor och få meddelanden när nya versioner blir tillgängliga.

<p align="center">
  <img src="assets/7.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>Förhandsvisning av Obtanium</b>
</p>

### Web Apps

För tillfällen då du kanske vill använda en tjänst sällan och inte vill ladda ner en nativ applikation kan du enkelt komma åt webbversionen. Många webbplatser erbjuder numera också stöd för progressiva webbappar (PWA). Detta innebär att du kan bokmärka en specifik webbplats (t.ex. Twitter.com) på din telefons startsida. När du sedan trycker på ikonen öppnas den som en fullskärmsapplikation utan de vanliga störningarna som följer med den typiska webbläsarupplevelsen. Du kan se ett exempel på hur det ser ut nedan.

För att åstadkomma detta i Vanadium, GrapheneOS' nativa webbläsare, navigerar du helt enkelt till den valda webbplatsen, trycker på de tre vertikala punkterna i det övre högra hörnet av skärmen och trycker sedan på **'Lägg till på startskärmen'**.

Nackdelen med detta tillvägagångssätt är att eftersom det bara är en bokmärkt webbsida får du ingen form av aviseringar. Vissa kan dock se det som en fördel!

<p align="center">
  <img src="assets/8.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>Twitter PWA</b>
</p>

### Webbläsare

Du kan inte riktigt gå fel med den förinstallerade alternativet, Vanadium. Appen fungerar på samma sätt som vilken annan mobilwebbläsare som helst jag har provat och jag har aldrig haft några kompatibilitetsproblem.

För tillfällen när du behöver komma åt Tor-nativa `.onion`-webbplatser kan du ladda ner Tor Browser APK direkt från deras [webbplats](https://www.torproject.org/download/#android) eller via F-Droid.

### VPN

För att skydda din onlineaktivitet från din nyfikna internetleverantör (ISP) är en app för virtuellt privat nätverk (VPN) ett bra alternativ. En VPN skickar din internettrafik i en krypterad tunnel till en delad IP-adress som kontrolleras av VPN-tjänsteleverantören för att säkerställa att din enhetsaktivitet inte kan kopplas till dig.

Följande är 3 välrenommerade alternativ som låter dig betala för tjänsten med Bitcoin och utan att lämna ut någon personlig information. Alla 3 alternativen finns tillgängliga via F-Droid.

- [Mullvad](https://f-droid.org/packages/net.mullvad.mullvadvpn/)
- [Proton](https://f-droid.org/en/packages/ch.protonvpn.android/)
- [iVPN](https://f-droid.org/en/packages/net.ivpn.client/)

### Meddelandetjänster

Under de senaste åren har krypterade meddelandelösningar blivit många. Problemet kvarstår dock, du kan ha den bästa och mest privata alternativet installerat på din telefon, men om du inte har några kontakter som använder det, vad är poängen?
De flesta människor som inte är intresserade av integritet använder förmodligen WhatsApp eller iMessage. Den första kan laddas ner via Aurora Store, men den senare kommer inte att fungera på GrapheneOS (uppenbarligen!).

- [Signal](https://signal.org/) är en av de mer populära slut-till-slut-krypterade (E2EE) meddelandetjänsterna som har en stark track record och rik funktionsuppsättning. Signal kräver ett telefonnummer för registrering, så om du planerar att chatta med personer som du inte vill att de ska veta ditt telefonnummer, kanske du bör titta på några av alternativen. Signal måste laddas ner via Aurora Store.
- [Simplex](https://f-droid.org/en/packages/chat.simplex.app/) är en ganska ny E2EE-meddelandetjänst. Den har inget användar-ID, kräver inget telefonnummer eller personlig information. Människor hittar dig genom att skanna din personliga QR-kod eller genom att besöka din unika länk. Simplex tillåter också avancerade användare att köra sin egen server för att ytterligare minska beroendet av någon centraliserad enhet. Simplex har ingen skrivbordsklient, så det kan vara olämpligt om flera enheter är högt prioriterade. Simplex för Android finns tillgängligt via F-Droid.
- [Threema](https://threema.ch/en/faq/libre_installation) erbjuder en liknande upplevelse som Simplex, men har funnits längre och känns därför lite mer polerad. Threema är inte gratis, en livstidslicens kostar $4.99 och kan köpas med Bitcoin. Threema erbjuder en webbklient och nativa skrivbordsprogram. Android-applikationen finns tillgänglig via F-Droid.
- [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/) är en inofficiell FOSS-fork av den officiella Telegram-appen för Android. Telegram har E2EE "hemliga chattar", men standardalternativet är inte privat. Telegram FOSS kan laddas ner från F-Droid.

<p align="center">
  <img src="assets/9.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  Vänster: <b>Threema</b> &nbsp; &nbsp; &nbsp; Höger: <b>Simplex</b>
</p>

### Media

- [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/) är en plattformsoberoende Spotify-klient som inte kräver ett Premium-konto. Spotube finns tillgängligt via F-Droid.
- [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/) är en fantastisk applikation för att strömma musik från YouTube Music, gratis. ViMusic finns tillgängligt på F-Droid.
- [Newpipe](https://f-droid.org/packages/org.schabi.newpipe/) erbjuder en YouTube-upplevelse utan irriterande annonser och tveksamma behörigheter. Med NewPipe kan du prenumerera på kanaler, lyssna i bakgrunden och till och med ladda ner för offline-visning. NewPipe är tillgängligt via F-Droid.
- [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/) är en podcast-spelare som låter dig prenumerera och hantera alla dina favoritprogram. AntennaPod finns tillgängligt via F-Droid.

<p align="center">
  <img src="assets/11.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  Vänster: <b>Spotube</b> &nbsp; &nbsp; &nbsp; Höger: <b>ViMusic</b>
</p>

### Kartor

Om du vill ha röstassistans när du kör och använder en kartapp i GrapheneOS måste du installera [RHVoice](https://rhvoice.org/installation/) och [konfigurera](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available) det.

- [Magic Earth](https://www.magicearth.com/) är ett alternativ till kartor som stöder steg-för-steg-navigation, 3D och offline-kartor. Magic Earth kan laddas ner från Aurora Store.
- [Organic Maps](https://f-droid.org/en/packages/app.organicmaps/) är ett alternativ till kartor för resenärer, turister, vandrare och cyklister baserat på crowd-sourced OpenStreetMap-data. Det är en integritetsfokuserad, öppen källkodsavstickning av appen Maps.me (tidigare känd som MapsWithMe). Den stöder 100% av funktionerna utan en aktiv internetanslutning och kan laddas ner från F-Droid.
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/) är ytterligare ett utmärkt alternativ till kartor som stöder alla ovan nämnda funktioner.

<p align="center">
  <img src="assets/13.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  Vänster: <b>Magic Earth</b> &nbsp; &nbsp; &nbsp; Höger: <b>Organic Maps</b>
</p>

### E-post

- [Proton Mail](https://proton.me/mail) erbjuder en gratis privat e-posttjänst som stöder granskad E2EE. Proton erbjuder också en betalversion som stöder anpassade domäner och [aliasing](https://proton.me/support/creating-aliases). Proton Mail kan laddas ner som en direkt APK eller via Aurora.
- [Tutanota](https://tutanota.com/) erbjuder samma funktioner som Proton Mail, inklusive valfria betaltjänster och kan laddas ner som en direkt APK eller via F-Droid.
- [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/) är en öppen källkods-e-postklient som fungerar med i stort sett alla e-postleverantörer. Den stöder flera konton, en samlad inkorg och krypteringsstandarden OpenPGP.

<p align="center">
  <img src="assets/15.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  Vänster: <b>Proton Mail</b> &nbsp; &nbsp; &nbsp; Höger: <b>Tutanota</b>
</p>

### Produktivitet

- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/) är ett program för filsynkronisering. Det synkroniserar filer mellan två eller flera enheter i realtid, säkert skyddade från nyfikna ögon. Dina data är bara dina och du förtjänar att välja var de lagras, om de delas med någon tredje part och hur de överförs över internet. Syncthing finns tillgängligt via F-Droid.
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/) kopplar samman alla dina enheter för att enkelt kommunicera med varandra när de är anslutna till ditt hemnätverk. Skicka enkelt filer, foton och urklipp över alla dina enheter (även på iOS!). KDE Connect kan laddas ner från F-Droid.
- [Notesnook](https://f-droid.org/en/packages/com.streetwriters.notesnook/) är en E2EE-anteckningsapplikation för att synkronisera dina tankar och att-göra-listor över alla dina enheter. Deras gratisplan bör täcka de flesta personliga användningsfall. Notesnook finns tillgängligt på F-Droid.
- [Standard Notes](https://f-droid.org/en/packages/com.standardnotes/) är mycket likt Notesnook, men kräver en betalplan för att matcha funktionerna. Standard Notes finns tillgängligt via F-Droid.
- [Anysoft Keyboard](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/) är en tangentbordsapp som låter dig anpassa nästan allt du kan tänka dig när det gäller skrivupplevelsen på din telefon. Den kan laddas ner via F-Droid.
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US) är standardtangentbordsappen från Google. Enligt min erfarenhet erbjuder den överlägset bästa skriv- och svepupplevelsen. Om du laddar ner denna app, se till att helt inaktivera alla nätverksrelaterade behörigheter. Den kan laddas ner via Aurora.

<p align="center">
  <img src="assets/17.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  Vänster: <b>Notesnook</b> &nbsp; &nbsp; &nbsp; Höger: <b>KDE Connect</b>
</p>

### Livsstil

- [Geometric Weather](https://f-droid.org/en/packages/wangdaye.com.geometricweather/) är en vackert designad Open Source-väderapp tillgänglig via F-Droid. Den stöder också många olika storlekar på widgets så att du kan se vädret på din valda plats direkt från startskärmen.
- [Translate You](https://f-droid.org/packages/com.bnyro.translate/) är en Open Source- och integritetsbevarande översättningsapp som stöder över 200 språk. Translate You finns tillgänglig via F-Droid.
- [Proton Calendar](https://proton.me/calendar/download) är en enkel att använda E2EE-kalender som fungerar sömlöst med dina Proton-e-postkonton. Proton Calendar kan laddas ner som en APK eller via Aurora Store.
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/) är en app för att visa och lagra boardingkort, kuponger, biobiljetter och medlemskort osv. Ladda helt enkelt ner den relevanta `pkpass`- eller `espass`-filen och öppna den med appen. PassAndroid finns tillgänglig via F-Droid.

<p align="center">
  <img src="assets/19.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  Vänster: <b>Geometric Weather</b> &nbsp; &nbsp; &nbsp; Höger: <b>Proton Calendar</b>
</p>

### Säkerhet/Integritet

- [Bitwarden](https://mobileapp.bitwarden.com/fdroid/) erbjuder en gratis och E2EE-övergripande lösenordshanteringslösning för alla dina enheter. Deras betaltjänst gör det möjligt att integrera 2FA-koder i appen. Bitwardens serversida kan vara självhostad och Android-appen finns tillgänglig via F-Droid.
- [Proton Pass](https://proton.me/pass/download) erbjuder en liknande gratis tjänst som Bitwarden, men [Proton Unlimited](https://proton.me/pricing)-kunder kan få tillgång till ytterligare avancerade funktioner. Proton Pass finns tillgänglig via APK eller Aurora.
- [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/) är en tvåfaktorsautentiseringsapplikation för system som använder engångslösenord. Tokens kan enkelt läggas till genom att skanna en QR-kod. FreeOTP finns tillgängligt via F-Droid.
- [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/) är en gratis, säker och öppen källkodsapp för Android för att hantera dina tvåstegsverifieringstokens för dina online-tjänster. Aegis finns tillgängligt via F-Droid.
- [Cryptomator](https://f-droid.org/en/packages/org.cryptomator.lite/) är en betald, plattformsoberoende tjänst som krypterar dina data lokalt så att du säkert kan ladda upp dem till din favoritmolntjänst. Cryptomator kan laddas ner via F-Droid.

<p align="center">
  <img src="assets/21.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  Vänster: <b>Proton Pass</b>  &nbsp; &nbsp; &nbsp;    Höger: <b>Bitwarden</b>
</p>

### Molnlösningar

- [Proton Drive](https://proton.me/drive/download) är en betald E2EE-molnlösning för att säkerhetskopiera och lagra alla dina filer. Vid skrivandet av detta har de just meddelat en Windows-skrivbordsklient, men Mac- och Linux-användare måste fortsätta använda webbversionen för att synkronisera från sina datorer (för tillfället). Android-klienten finns tillgänglig som APK eller via Aurora.
- [Skiff](https://skiff.com/download) erbjuder också betald E2EE-molnlagring och filsamarbetsverktyg. De erbjuder en Mac- och Windows-skrivbordsklient (samt en webbapp) och deras Android-klienter måste laddas ner från Aurora.
- [Nextcloud](https://f-droid.org/en/packages/com.nextcloud.client/) erbjuder en fullt utrustad molnbaserad lösning för samarbete, synkronisering mellan olika enheter och filförvaring. Mer avancerade användare kan välja att själva vara värd för sin fria och öppna källkod på valfri hårdvara de vill. Android-klienterna kan laddas ner via F-Droid.
- [Cryptpad](https://cryptpad.fr/) erbjuder ett gratis, webbaserat, E2EE-alternativ till Google Docs.

<p align="center">
  <img src="assets/23.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>Proton Drive</b>
</p>

---

## Nackdelarna

De öppna källkods- och integritetsbevarande alternativen till de teknikjättarnas applikationer som du har vant dig vid att använda är många, och vissa av dem är ofta bättre än de stängda källkods- och spionprogramsfyllda alternativen.

Men när du byter till GrapheneOS finns det vissa bekvämligheter som du måste ge upp på grund av att det inte finns några alternativ. Dessa inkluderar:

- **Apple CarPlay/Android Auto** - Du kommer att behöva hålla fast vid gamla hederliga Bluetooth, USB eller Aux.
- **Apple/Google Pay** - Nästan alla bär ändå med sig sin plånbok!
- **Bankappar** - Det är inte så att dessa inte fungerar alls. Vissa fungerar faktiskt perfekt. Andra fungerar endast med Google Play-tjänster aktiverade (läs mer om det nedan) och andra fungerar helt enkelt inte alls. Läs rapporten om din bank [här](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/) för att se det aktuella läget. Oroa dig inte om din bankapp finns med på listan över appar som inte fungerar, kom ihåg att du bara kan spara URL:en som en webbapp på din startsida.
- **Push-meddelanden** - De flesta appar som skickar uppdateringar när du inte använder en specifik app gör det genom Google Play-tjänster. Dessa är inte installerade som standard med GrapheneOS, så om du märker att du inte får omedelbara meddelanden när din vän skickar dig ett e-postmeddelande är det troligen därför. Den goda nyheten är att några av de appar som nämns ovan har implementerat sin egen bakgrundskoppling för att regelbundet kontrollera efter uppdateringar och sedan ge dig en notifiering vid behov.

### Sandboxed Google Play

> 'GrapheneOS har ett kompatibilitetslager som ger möjlighet att installera och använda officiella versioner av Google Play i den vanliga app-sandboxen. Google Play får absolut ingen speciell åtkomst eller privilegier på GrapheneOS jämfört med att kringgå app-sandboxen och få en massiv mängd högt privilegierad åtkomst.'

Om du finner att du helt enkelt inte kan leva utan de där push-meddelandena för din favoritapp eller att en viss "måste-ha"-app är värdelös utan Play-tjänster, tillåter GrapheneOS dig att [installera](https://grapheneos.org/usage#sandboxed-google-play-installation) dessa tjänster i en helt isolerad miljö. När de är installerade kräver dessa tjänster ingen Google-konto för att fungera, och varje tjänsts behörigheter kan kontrolleras noggrant.

Innan du skyndar dig att installera dem från dag 1, uppmanar jag dig att se hur långt du kommer utan dem. Du kommer förmodligen att bli förvånad över hur många appar som fungerar helt normalt utan dem.

Om du ändå vill installera dem, tryck helt enkelt på den förinstallerade "Appar"-appen följt av "Google Play-tjänster". Överväg att installera dem tillsammans med de mindre privata apparna du inte kan vara utan, i en helt separat användarprofil för att ge en extra nivå av åtskillnad från resten av din telefon.

<p align="center">
  <img src="assets/24.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>Skärmbild för installation av Play-tjänster</b>
</p>

### Profiler

GrapheneOS tillåter dig att ha en separat telefonupplevelse inom din telefon. Ytterligare profiler kan installera sina egna appar och tjänster och kan inte komma åt några filer eller data från ägarprofilen.
Om du bara har en eller två av de där "måste-ha"-apparna som kräver Play-tjänster, men som bara används mycket sällan, kan det vara en bra idé att installera dem tillsammans med Play-tjänster i en separat profil för att ytterligare stärka eventuella små sekretesskonsekvenser som finns kvar genom att ha dem igång i ägarprofilen.

Du kan läsa mer om detta användningsfall [här](https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2).

Om du bestämmer dig för att lägga till en separat profil som passar ditt användningsfall kan appen [Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/) vara användbar för dig. Insular gör det möjligt att enkelt klona någon av dina befintliga appar till den nya profilen utan att behöva gå via någon av de traditionella installationsvägarna som täcktes tidigare i den här guiden. Insular låter dig också snabbt "frysa" någon av dessa appar för att helt inaktivera alla bakgrundstjänster för den appen.

<p align="center">
<img src="assets/24.png" class="responsive" style="max-width: 80%; height: auto;" /></p>

<p align="center">
  <b>Användarprofilhanteringsskärm</b>
</p>

### e-Sims

Om du vill ta din telefonsekretess till nästa nivå och ha en mobilservice som är fristående från din verkliga identitet kan en eSIM vara något för dig. En eSIM är en virtuell SIM-kort som du kan köpa online och lägga till i din telefon via en QR-kod. Företag som erbjuder sådana tjänster som kan betalas anonymt med Bitcoin inkluderar [Silent.Link](https://silent.link/) och [Bitrefill](https://www.bitrefill.com/gb/en/esims/).

eSIM bör inte ses som en fullständig lösning för telefonsekretess. De kan vara ett användbart verktyg när de används på rätt sätt, men var vänlig och undersök [avvägningarna](https://grapheneos.org/faq#cellular-tracking) med att använda någon typ av mobilservice om ditt syfte är att vara helt "off grid".

Sandboxed Play Services måste installeras för eSIM-provisionering i GrapheneOS.

## Säkerhetskopior

Efter att ha konfigurerat din nya Pixel-telefon utan Google är det en bra idé att skapa en säkerhetskopia. Denna säkerhetskopia gör det möjligt för dig att återställa telefonen till ett identiskt tillstånd om du förlorar den eller om den blir borttappad/stulen.

Du kan välja att lagra säkerhetskopieringsfilen på valfri extern lagringsmedia eller på en självhostad molnlösning som Nextcloud, även om vissa användare rapporterar varierande framgångsnivåer med det senare alternativet.

För att skapa din första säkerhetskopia:

1. Gå till **Inställningar** > **System** > **Säkerhetskopiering**, skriv sedan ner din 12-ords återställningskod. Denna kod krävs för att dekryptera säkerhetskopieringsfilen vid senare tillfälle. Förlorar du koden förlorar du tillgången till din telefonbackup.
2. Välj sedan din lagringsplats. Jag rekommenderar en extern USB-enhet eller ett industriellt microSD-kort.
3. Välj vilka data som ska säkerhetskopieras. Om du har tillräckligt med utrymme på den angivna lagringsenheten rekommenderar jag att du väljer allt.
4. Tryck på de tre punkterna längst upp till höger och välj **Säkerhetskopiera nu**.

<p align="center">
  <img src="assets/26.png" class="responsive" style="max-width: 80%; height: auto;" />
</p>

<p align="center">
  <b>Säkerhetskopieringsskärm</b>
</p>

Kom ihåg att om du gör offline-säkerhetskopior till externa lagringsmedier är det vettigt att genomföra detta steg regelbundet för att säkerställa att eventuella nyligen viktiga uppdateringar till din telefon inte går förlorade om det värsta skulle hända.

<p align="center">
<iframe width="100%" height="315" src="https://www.youtube.com/embed/eyWmcItzisk" class=responsive title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

<p align="center">
  <b>Video som beskriver säkerhetskopieringsprocessen</b>
</p>

## Slutsats

Under de senaste åren har GrapheneOS-programvaran mognat betydligt. Den är mer stabil och kompatibel än någonsin tidigare. Tillsammans med den blomstrande Open Source- och integritetsbevarande app-ekosystemet gör detta GrapheneOS till ett verkligt alternativ till stock Android eller iOS, även för "vanliga" människor som dig!
Dataintrång och massövervakning är så vanliga i dagens värld att de knappt får någon uppmärksamhet längre. Det är upp till dig att skydda dig själv. Det kommer att krävas anpassningar och uppoffringar längs vägen, men att minska risken för sådana intrång är inte alls så svårt som du tror att det kommer att vara.
Jag hoppas att den här guiden kan hjälpa dig på din resa. Om du tycker att den här guiden var användbar och vill stödja mitt arbete, överväg att skicka en [donation](/tips).

Om du redan är en användare av GrapheneOS, eller blir det som ett resultat av den här guiden, överväg att [donera](https://grapheneos.org/donate) för att stödja deras viktiga arbete.

### Läs mer

GrapheneOS är ett kaninhål som vem som helst lätt kan spendera veckor med att utforska. Det finns så mycket du kan lära dig och experimentera med för att anpassa upplevelsen efter dina behov och hotmodeller. Nedan finns några länkar där du kan fortsätta din resa:

- [GrapheneOS Officiell Användarguide](https://grapheneos.org/usage) - Officiell webbplats
- [GrapheneOS Forum](https://discuss.grapheneos.org/) - Officiell webbplats
- [GrapheneOS Inställningsmästarklass](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - Video av 'The Privacy Wayfinder'
- [GrapheneOS Allmän Podcast](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - Podcast av 'Watchman Privacy'

full credit to : https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md
