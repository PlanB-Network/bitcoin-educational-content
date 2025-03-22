---
name: GrapheneOS

description: Graphene OS opplæring
---

> "[GrapheneOS](https://grapheneos.org/) er et personvern- og sikkerhetsfokusert mobilt OS med kompatibilitet for Android-apper, utviklet som et ideelt åpen kildekode-prosjekt."

GrapheneOS, opprinnelig grunnlagt i 2014 som 'CopperheadOS', er basert på den tradisjonelle Android-koden (AOSP), men med mange endringer og forbedringer rettet mot å forbedre brukerens personvern og sikkerhet. GrapheneOS gir brukeren kontroll over telefonen sin, ikke de store teknologiselskapene.

### Innholdsfortegnelse:

- Introduksjon
- Forberedelser
- Installasjon
- App-alternativer
- Ulemper
- Nyttig informasjon

Guide av https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md

## Hvorfor bruke GrapheneOS?

Moderne telefoner er $500-$1000 sporing- og datahøstingsenheter. Hver eneste del av livet vårt går gjennom dem, og dessverre deles mye av denne dataen med tredjeparter i en eller annen form.
GrapheneOS er spesielt bygget for å redusere denne datadelingen og forbedre enhetens sikkerhet mot potensielle angrepsvektorer. Det finnes ikke noe som en GrapheneOS-konto. Du trenger ikke en for å laste ned apper eller samhandle med OS-et. Enkelt sagt, du er ikke produktet.

GrapheneOS gir ekstra sikkerhet til din Android-opplevelse gjennom noen enkle grunnprinsipper.

1. **Reduksjon av angrepsflate** - Fjerne unødvendig kode (eller bloatware).
2. **Forebygging av eksponering for sårbarheter** - Tillate brukeren nok granularitet til å velge de kompromissene de er komfortable med.
3. **Sandkasse-inneslutning** - GrapheneOS forsterker eksisterende Android-sandkasser, ytterligere låser ned hver apps evne til å kommunisere med resten av telefonen din.

Lær mer om de tekniske detaljene i GrapheneOS-funksjonssettet [her](https://grapheneos.org/features).

### Lettelse av overgangen

Hvis du har vært dypt inne i Google- eller Apple-økosystemet i årevis, kan tanken på å miste all den bekvemmeligheten over natten være en skremmende en. Men med noen nøye vurderte appinstallasjonsbeslutninger (dekket senere), kan mye av denne forventede vanskeligheten reduseres eller fjernes.

Så gode som alternativene blir, kan tanken på en slik endring fortsatt være avskrekkende. Hvis du finner deg selv i denne situasjonen, er mitt beste råd å kjøre din nye GrapheneOS-enhet ved siden av din eksisterende telefon en stund. Derfra kan du sakte venne deg av med 2-3 apper per uke til du finner deg selv kun nå for din GrapheneOS-enhet.

Hvis du tar denne tilnærmingen, vær streng med deg selv og kutt avhengigheten av de overvåkede alternativene så raskt som mulig. Vi mennesker er late og vil ofte ta veien med minst motstand. Husk hvorfor du gjorde byttet i utgangspunktet.

**I stedet for å betale med dine personlige data, valgte du å betale med din tid, og noen ganger dine hardt opptjente penger (avhengig av alternative apper du installerer).**

## Komme i gang

GrapheneOS er for øyeblikket kun i produksjon for _(ganske ironisk)_ [Google Pixel](https://grapheneos.org/faq#supported-devices)-serien av telefoner. Dette kommer ikke uten god grunn, though. Pixel-telefonene tilbyr den beste maskinvarebaserte sikkerheten for å komplementere arbeidet som er gjort for å styrke OS-et. Dette inkluderer ting som spesifikk komponentisolering og verifisert oppstart.

### Velge en enhet

Når du velger Pixel du ønsker å installere GrapheneOS på, sørg for at du sjekker hvor lenge enheten vil fortsette å få standard [sikkerhetsoppdateringer](https://support.google.com/pixelphone/answer/4457705?hl=no#zippy=%2Cpixel-xl-a-a-g-a-g) for.
På tidspunktet for skriving er Pixel 6a den billigste modellen tilgjengelig med god langsiktig støtte, garantert til juli 2027. Hvis du velger denne modellen, vil ikke OEM-opplåsing fungere med versjonen av det originale operativsystemet fra fabrikken. Du må oppdatere den til juni 2022-utgivelsen eller senere via en over-the-air oppdatering. Etter at du har oppdatert den, må du også tilbakestille enheten til fabrikkinnstillingene for å fikse OEM-opplåsing. Alle andre modeller som er operatørlåst opp, vil være klare for GrapheneOS rett ut av boksen.
Når du velger en enhet, vil du også sørge for at du kjøper en ulåst versjon. Visse operatører som Verizon sender enhetene sine som er bootloader-låst, noe som fullstendig forhindrer følgende prosess.

### Installere GrapheneOS

GrapheneOS [nettinstallatør](https://grapheneos.org/install/web) gjør hele prosessen til en lek, og en som kan fullføres av hvem som helst på under 10 minutter.
Følgende instruksjoner er en forkortet versjon tatt fra lenken ovenfor.

Alt du trenger tilgjengelig er:

- Pixel-enheten
- En USB-kabel for å koble telefonen til datamaskinen din
- En datamaskin for å kjøre en nettleser (enhver Chromium-basert nettleser: Chrome, Edge, Brave, osv.)

1. Det første steget er å gå til **Innstillinger** > **Om telefonen** og gjentatte ganger trykke på byggnummeret til du ser **'Utviklermodus'** er aktivert.
2. Gå deretter til **Innstillinger** > **System** > **Utvikleralternativer** og aktiver **'OEM-opplåsing'**.
3. Nå omstart enheten og hold volum ned-knappen mens telefonen slår seg på igjen.
4. Koble telefonen til din bærbare datamaskin og hvis du blir bedt om autorisasjon, tillat tilkoblingen.
5. På nettinstallatørens side, klikk på 'Lås opp bootloaderen'.
6. Du vil da se telefonalternativene endre seg. Bruk volumknappen til å endre valget til `unlock` og bruk av/på-knappen for å akseptere.
7. Klikk deretter på last ned utgivelse på nettinstallatørens side.
8. Når den er fullstendig nedlastet, gå videre til neste steg og klikk 'Flash utgivelse'. Dette vil ta et minutt eller to og du trenger ikke å røre telefonen i det hele tatt.
9. Til slutt, gå til neste steg av nettinstallatøren og klikk **Lås Bootloader**. Du må endre valget og bekrefte med av/på-knappen på samme måte som du gjorde tidligere i prosessen.
10. Når du ser ordet `Start`, bekreft dette med av/på-knappen og enheten vil starte opp i ditt nye Google-frie operativsystem.

![bilde](assets/2.webp)

GrapheneOS startskjerm


_Etter første oppstart og oppsett, er det god praksis å deaktivere OEM-opplåsing fra Innstillinger > System > Utvikleralternativer._

_Du vil kanskje også ta det ekstra, valgfrie, men anbefalte steget med å verifisere installasjonen via Auditor-appen. Du trenger en separat Android-telefon med appen installert for å fullføre dette steget. Instruksjoner for dette kan finnes [her](https://attestation.app/tutorial)._


![video](https://www.youtube.com/embed/L1KZWjZVnAw)

Video som detaljerer de enkle stegene nevnt ovenfor


Hvis disse enkle stegene virker som et skritt for langt, kan du vurdere å kjøpe en Pixel med GrapheneOS-programvaren [forhåndsinstallert](https://ronindojo.io/en/roninmobile). Vær bare klar over at du legger en liten mengde tillit i leverandøren.

### Forhåndsinstallerte apper

Nå som du er satt opp, kan du legge merke til hvor skjelett GrapheneOS ser ut ved første installasjon. Som standard vil du ha disse appene installert:

![bilde](assets/3.webp)

Standard apper
De eneste to du kanskje ikke er kjent med er 'Auditor' og 'Vanadium'.
- '[Auditor-appen](https://play.google.com/store/apps/details?id=app.attestation.auditor) bruker maskinvarebaserte sikkerhetsfunksjoner for å validere identiteten til en enhet sammen med autentisiteten og integriteten til operativsystemet. Den vil verifisere at enheten kjører det originale operativsystemet med bootloader låst og at det ikke har skjedd noen manipulering med operativsystemet.'
- [Vanadium](https://github.com/GrapheneOS/Vanadium) er en variant av Chromium-nettleseren som er forsterket med tanke på personvern og sikkerhet.

## Tilpasning

Telefoninnstillinger er en personlig sak, men her er noen av de første tingene jeg endrer når jeg installerer GrapheneOS for å føle meg mer hjemme.

### Sette et bakgrunnsbilde og oppdatere temaet

Gå til Innstillinger > Bakgrunnsbilde og stil. Herfra:

- Oppdaterer jeg bakgrunnsbildene for hjemme- og låseskjermen med bilder lastet ned fra nettet.
- Velger jeg aksentfargene som brukes gjennom hele brukergrensesnittet.
- Aktiverer jeg Mørkt tema.

### Vise batteriprosent

Gå til **Innstillinger** > **Batteri**, deretter aktiver **Vis batteriprosent** i statuslinjen.

### Importere kontakter

**Fra en annen Android-telefon** - Gå til Kontakter-appen og se etter alternativet Eksporter til VCF.

**Fra iOS** - Bruk en app som Export Contact og bruk 'vCard'-eksportalternativet for å eksportere en VCF-fil.
Når du har VCF-filen, kan du overføre den til din GrapheneOS-enhet med et eksternt lagringsalternativ som microSD-kort eller USB-stasjon. Hvis du ikke har noen av disse for hånden, kan du velge å dele via en av de mange appene som er nevnt nedenfor.

![bilde](assets/4.webp)

Personlig tilpasset hjemmeskjerm


## Alternative Apper

For å gjøre telefonen din nyttig, kommer du til å ønske å installere noen applikasjoner! Alternativene som følger er inkludert fordi jeg personlig har brukt dem alle, eller fordi de mottar sterke anbefalinger fra personvernsamfunnet for øvrig. Det finnes mange andre flotte alternativer som ikke er nevnt, og [Awesome Privacy](https://awesome-privacy.xyz) tilbyr en utrolig omfattende liste over personvernbevarende applikasjoner for alle typer enheter.

Bare fordi en app er gratis og åpen kildekode-programvare (FOSS) betyr ikke det at den er fri for potensielle personvernlekkasjer. Bruk [Exodus](https://reports.exodus-privacy.eu.org/en/) for å se hvordan dine foretrukne apper presterer mot deres personvernauditer.

### F-Droid

[F-Droid](https://f-droid.org/) er en installerbart katalog av FOSS-applikasjoner for Android. Klienten gjør det enkelt å bla gjennom, installere og oppdatere applikasjoner på enheten din. Det er verdt å nevne at oppdateringer via F-Droid noen ganger kan være tregere enn med andre appbutikker. Dette avhenger hovedsakelig av om appen er funnet via hovedrepositoryet til F-Droid eller et tilpasset ett.

For å installere F-Droid, gå ganske enkelt til deres nettsted via en nettleser på din GrapheneOS-telefon og trykk på nedlasting. Dette vil laste ned en `.apk`-fil. Du vil deretter bli spurt om du ønsker å installere appen.

I tillegg til applikasjoner funnet innenfor standardrepositoryet i F-Droid, vil mange Open Source-prosjekter også være vert for sitt eget repository som kan legges til i F-Droid-appinnstillingene. Hvis dette er tilfellet, vil prosjektet i spørsmålet veilede deg gjennom de veldig enkle trinnene som kreves for å oppnå dette på deres nettsted.

![bilde](assets/5.webp)

F-Droid hjemmeskjerm

### Aurora Store
[Aurora Store](https://auroraoss.com/) er en FOSS-versjon av Google Play-butikken. Aurora ser ut og føles veldig lik den tradisjonelle Play-butikken og lar deg laste ned og oppdatere enhver app du vanligvis ville finne via Google-alternativet.
Den viktigste funksjonen til Aurora er anonym innlogging. Dette betyr at du kan laste ned noen av dine favorittapper som ikke er tilgjengelige via F-Droid eller direkte APK, uten å måtte være logget inn på din Google-konto.

Før du haster med å gjøre dette til ditt standard installasjonsalternativ, husk at mange av applikasjonene vi prøver å komme bort fra, ble installert fra Play-butikken. Bare fordi de er tilgjengelige fra Aurora, endrer ikke det faktum at noen kan ha sporingsegenskaper innebygd. Det vil ikke alltid være mulig, men når du kan, se etter et F-Droid-alternativ før du laster ned via Aurora.

For å installere Aurora, søk bare etter 'Aurora Store' i F-Droid.

Aurora har også noen potensielle angrepsvektorer, ettersom de "anonyme kontoene" egentlig er opprettet og kontrollert av Aurora. De kunne, i teorien, levere ondsinnede oppdateringer eller dytte apper til telefonen din, selv om du fortsatt må akseptere installasjonsprompten på enheten. Aurora har også noen ganger problemer med at apper ikke vises på grunn av region- og enhetsfeiltolkninger. Dette kan vanligvis omgås med trinnene nedenfor.

**Topp tips** - Noen ganger vil Aurora Store oppleve ratebegrensning som begrenser evnen din til å søke og installere apper. For å komme rundt dette, gå til **Innstillinger** > **Apper** > **Aurora** > **Åpne som standard**, og legg til domenet `play.google.com`. Nå, når du navigerer til et produkts eller tjenestes nettsted som har 'Last ned via Play-butikken'-lenken, vil å trykke på den åpne den appen innenfor Aurora for deg å laste ned.


![bilde](assets/6.webp)

Aurora Store hjemskjerm

### APK-nedlasting

Apper på Android kan også lastes ned og installeres via en `.apk`-fil. Dette er et flott alternativ som krever null tredjeparts appbutikker, bare last ned filen direkte fra prosjektet eller tjenestens nettsted eller GitHub-repositorium.

Ulempen med denne tilnærmingen er at du ikke får automatiske oppdateringer, så du må overvåke den tjenestens kommunikasjonskanaler for å lære om nye utgivelser. Det finnes imidlertid et flott prosjekt kalt Obtanium som sikter på å fikse dette. [Obtainium](https://github.com/ImranR98/Obtainium) lar deg installere og oppdatere Open-Source-apper direkte fra deres utgivelsessider, og motta varsler når nye utgivelser blir tilgjengelige.

![bilde](assets/7.webp)

Obtanium forhåndsvisning

### Web-apper

For tider hvor du kanskje vil bruke en tjeneste sjelden og ikke ønsker å laste ned en innfødt applikasjon, kan du enkelt få tilgang til webversjonen. Mange nettsteder tilbyr nå også støtte for Progressive Web App (PWA). Dette er når du kan bokmerke et spesifikt nettsted (f.eks Twitter.com) til hjemmeskjermen på telefonen din. Deretter, når du trykker på ikonet, åpnes det som en fullskjermsapplikasjon uten de vanlige distraksjonene som kommer med den typiske nettleseropplevelsen. Du kan se et eksempel på hvordan dette ser ut nedenfor.

For å oppnå dette i Vanadium, GrapheneOS' native nettleser, naviger bare til nettstedet du velger, trykk på de tre vertikale prikkene i øvre høyre hjørne av skjermen og deretter trykk på **'Legg til på hjem-skjerm'**.

Den eneste ulempen med denne tilnærmingen er at siden dette bare er en bokmerket nettside, vil du ikke få noen form for varslinger. Selv om noen kanskje ser det som en positiv ting!

![bilde](assets/8.webp)

Twitter PWA

### Nettlesere
Du kan egentlig ikke gå galt med det forhåndspakkede alternativet, Vanadium. Appen oppfører seg identisk til enhver annen mobilnettleser jeg har prøvd, og jeg har ikke en eneste gang hatt noen kompatibilitetsproblemer.
For tider når du trenger å få tilgang til Tor-native `.onion`-sider, kan du laste ned Tor Browser APK direkte fra deres [nettsted](https://www.torproject.org/download/#android) eller via F-Droid.

### VPN-er

For å beskytte din online aktivitet fra din nysgjerrige internettleverandør (ISP), er en app for et Virtuelt Privat Nettverk (VPN) et godt alternativ. En VPN sender din internett-trafikk i en kryptert tunnel til en delt IP-adresse kontrollert av VPN-tjenesteleverandøren for å sikre at din enhetsaktivitet ikke kan knyttes til deg.

Følgende er 3 velrespekterte alternativer som lar deg betale for tjenesten i Bitcoin og uten å oppgi noen personlige opplysninger. Alle 3 alternativene er tilgjengelige via F-Droid.

- [Mullvad](https://f-droid.org/packages/net.mullvad.mullvadvpn/)
- [Proton](https://f-droid.org/en/packages/ch.protonvpn.android/)
- [iVPN](https://f-droid.org/en/packages/net.ivpn.client/)

### Meldingstjenester

I de siste årene har det blitt rikelig med løsninger for kryptert meldingsutveksling. Problemet forblir dog, du kan ha det beste og mest private alternativet installert på telefonen din, men hvis du ikke har noen kontakter som bruker det, hva er poenget?

De fleste som ikke er interessert i privatlivsrommet, vil sannsynligvis bruke WhatsApp eller iMessage. Førstnevnte kan lastes ned via Aurora Store, men sistnevnte kommer ikke til å fungere på GrapheneOS (åpenbart!).

- [Signal](https://signal.org/) er en av de mer populære meldingstjenestene med ende-til-ende-kryptering (E2EE) som har et sterkt rykte og rikt funksjonssett. Signal krever et telefonnummer for registrering, så hvis du planlegger å chatte med folk som du heller ikke vil skulle kjenne ditt telefonnummer, kanskje se på noen av alternativene. Signal må lastes ned via Aurora Store.
- [Simplex](https://f-droid.org/en/packages/chat.simplex.app/) er en ganske ny E2EE-meldingstjeneste. Den krever ingen bruker-ID, telefonnummer eller personlig informasjon. Folk finner deg ved å skanne din personlige QR-kode eller ved å besøke din unike lenke. Simplex lar også avanserte brukere kjøre sin egen server for ytterligere å redusere avhengigheten av enhver sentralisert enhet. Simplex har ikke en skrivebordsklient, så det kan ikke være egnet hvis fler-enhetsbruk er på prioriteringslisten din. Simplex for Android er tilgjengelig via F-Droid.
- [Threema](https://threema.ch/en/faq/libre_installation) tilbyr en lignende opplevelse som Simplex, men har vært rundt lenger og som et resultat, føles litt mer polert. Threema er ikke gratis, en livstidslisens koster $4.99 og kan kjøpes med Bitcoin. Threema tilbyr en webklient og native skrivebordsapplikasjoner. Android-applikasjonen er tilgjengelig via F-Droid.
- [Telegram FOSS](https://f-droid.org/en/packages/org.telegram.messenger/) er en uoffisiell FOSS-fork av den offisielle Telegram-appen for Android. Telegram har E2EE 'hemmelige chatter', men standardalternativet er ikke privat. Telegram FOSS kan lastes ned fra F-Droid.

![bilde](assets/9.webp)
Venstre: Threema
Høyre: Simplex

### Media
- [Spotube](https://f-droid.org/packages/oss.krtirtho.spotube/) er en plattformuavhengig Spotify-klient som ikke krever en Premium-konto. Spotube er tilgjengelig via F-Droid.
- [ViMusic](https://f-droid.org/en/packages/it.vfsfitvnm.vimusic/) er en fantastisk applikasjon for å strømme all musikk fra YouTube Music, gratis. ViMusic er tilgjengelig fra F-Droid.
- [Newpipe](https://f-droid.org/packages/org.schabi.newpipe/) tilbyr en YouTube-opplevelse uten irriterende reklamer og tvilsomme tillatelser. Med NewPipe kan du abonnere på kanaler, lytte i bakgrunnen og til og med laste ned for offline visning. NewPipe er tilgjengelig via F-Droid.
- [AntennaPod](https://f-droid.org/packages/de.danoeh.antennapod/) er en podcast-spiller som lar deg abonnere og administrere alle dine favorittprogrammer. AntennaPod er tilgjengelig via F-Droid.

![bilde](assets/11.webp)

Venstre: Spotube
Høyre: ViMusic

### Kart

Hvis du ønsker stemmeassistanse mens du kjører og bruker en kart-app i GrapheneOS, må du installere [RHVoice](https://rhvoice.org/installation/) og [konfigurere](https://discuss.grapheneos.org/d/2488-organic-maps-app-voice-instructions-are-not-available) det.

- [Magic Earth](https://www.magicearth.com/) er et kartalternativ som støtter navigasjon sving-for-sving, 3D og offline kart. Magic Earth kan lastes ned fra Aurora Store.
- [Organic Maps](https://f-droid.org/en/packages/app.organicmaps/) er et kartalternativ for reisende, turister, vandrere og syklister basert på folkefinansierte OpenStreetMap-data. Det er en personvern-fokusert, åpen kildekode-fork av Maps.me-appen (tidligere kjent som MapsWithMe). Den støtter 100% av funksjonene uten en aktiv internettforbindelse og kan lastes ned fra F-Droid.
- [OsmAnd](https://f-droid.org/en/packages/net.osmand.plus/) er et annet flott kartalternativ som støtter alle de ovennevnte funksjonene.

![bilde](assets/13.webp)

Venstre: Magic Earth
Høyre: Organic Maps

### E-post

- [Proton Mail](https://proton.me/mail) tilbyr en gratis privat e-posttjeneste som støtter revidert E2EE. Proton tilbyr også en betalt versjon som støtter egendefinerte domener og [aliaser](https://proton.me/support/creating-aliases). Proton Mail kan lastes ned som en direkte APK eller via Aurora.
- [Tutanota](https://tutanota.com/) tilbyr de samme funksjonene som Proton Mail, inkludert valgfrie betalte tjenester og kan lastes ned som en direkte APK eller via F-Droid.
- [K-9 Mail](https://f-droid.org/en/packages/com.fsck.k9/) er en åpen kildekode e-postklient som fungerer med nesten alle e-postleverandører. Den støtter flere kontoer, en samlet innboks og OpenPGP-krypteringsstandarden.

![bilde](assets/15.webp)

Venstre: Proton Mail
Høyre: Tutanota

### Produktivitet

- [Syncthing](https://f-droid.org/packages/com.nutomic.syncthingandroid/) er et filsynkroniseringsprogram. Det synkroniserer filer mellom to eller flere enheter i sanntid, trygt beskyttet fra nysgjerrige øyne. Dine data er dine egne, og du fortjener å velge hvor de lagres, om de deles med en tredjepart, og hvordan de overføres over internett. Syncthing er tilgjengelig via F-Droid.
- [KDE Connect](https://f-droid.org/packages/org.kde.kdeconnect_tp/) kobler sammen alle enhetene dine slik at de enkelt kan kommunisere med hverandre når de er koblet til hjemmenettverket ditt. Send enkelt filer, bilder, utklippstavledata på tvers av alle enhetene dine (også på iOS!). KDE Connect kan lastes ned fra F-Droid.
- [Notesnook](https://f-droid.org/en/packages/com.streetwriters.notesnook/) er en E2EE notatapplikasjon for å synkronisere tankene dine og gjøremålslistene på tvers av alle enhetene dine. Deres gratisplan burde dekke de fleste personlige brukstilfeller. Notesnook er tilgjengelig på F-Droid.
- [Standard Notes](https://f-droid.org/en/packages/com.standardnotes/) er veldig lik Notesnook, men krever en betalt plan for å matche funksjonssettet. Standard Notes er tilgjengelig gjennom F-Droid.
- [Anysoft Keyboard](https://f-droid.org/packages/com.menny.android.anysoftkeyboard/) er en tastaturapp som lar deg tilpasse så å si alt du kan tenke deg når det kommer til skriveopplevelsen på telefonen din. Den kan lastes ned via F-Droid.
- [GBoard](https://play.google.com/store/apps/details?id=com.google.android.inputmethod.latin&hl=en&gl=US) er den standard Google tastaturappen. Etter min erfaring tilbyr den langt den beste skrive- og sveipeopplevelsen. Hvis du laster ned denne appen, sørg for å fullstendig deaktivere alle nettverksrelaterte tillatelser. Den kan lastes ned via Aurora.

![bilde](assets/17.webp)

Venstre: Notesnook
Høyre: KDE Connect

### Livsstil

- [Geometric Weather](https://f-droid.org/en/packages/wangdaye.com.geometricweather/) er en vakkert designet Open Source værapp tilgjengelig via F-Droid. Den støtter også mange forskjellige størrelser på widgets slik at du kan se været på ditt valgte sted rett fra hjemmeskjermen din.
- [Translate You](https://f-droid.org/packages/com.bnyro.translate/) er en Open Source og personvernbevarende oversettelsesapp som støtter mer enn 200 språk. Translate You er tilgjengelig via F-Droid.
- [Proton Calendar](https://proton.me/calendar/download) er enkel å bruke E2EE som samhandler sømløst med dine Proton e-postkontoer. Proton Calendar kan lastes ned som en APK eller via Aurora-butikken.
- [PassAndroid](https://f-droid.org/en/packages/org.ligi.passandroid/) er en app for å vise og lagre ombordstigningskort, kuponger, kinobilletter og medlemskort osv. Last ned den relevante `pkpass` eller `espass` filen og åpne med appen. PassAndroid er tilgjengelig via F-Droid.

![bilde](assets/19.webp)
Venstre: Geometric Weather
Høyre: Proton Calendar

### Sikkerhet/Personvern

- [Bitwarden](https://mobileapp.bitwarden.com/fdroid/) tilbyr en gratis og E2EE tverrplattform passordbehandlerløsning for alle enhetene dine. Deres betalte tjeneste lar deg integrere 2FA-koder i appen. Serverdelen av Bitwarden kan være selvhostet og Android-appen er tilgjengelig via F-Droid.
- [Proton Pass](https://proton.me/pass/download) tilbyr en lignende gratis tjeneste som Bitwarden, men [Proton Unlimited](https://proton.me/pricing) kunder kan få tilgang til ytterligere avanserte funksjoner. Proton Pass er tilgjengelig via APK eller Aurora.
- [FreeOTP](https://f-droid.org/packages/org.fedorahosted.freeotp/) er en tofaktor-autentiseringsapplikasjon for systemer som bruker engangspassordprotokoller. Token kan enkelt legges til ved å skanne en QR-kode. FreeOTP er tilgjengelig via F-Droid.
- [Aegis](https://f-droid.org/en/packages/com.beemdevelopment.aegis/) er en gratis, sikker og Open Source-app for Android for å håndtere dine 2-trinns verifiseringstoken for dine nettjenester. Aegis er tilgjengelig via F-Droid.
- [Cryptomator](https://f-droid.org/en/packages/org.cryptomator.lite/) er en betalt, plattformuavhengig tjeneste som krypterer dataene dine lokalt slik at du trygt kan laste dem opp til din favoritt skytjeneste. Cryptomator kan lastes ned via F-Droid.

![bilde](assets/21.webp)
Venstre: Proton Pass
Høyre: Bitwarden

### Skytjenester

- [Proton Drive](https://proton.me/drive/download) er en betalt E2EE skytjeneste for sikkerhetskopiering og lagring av alle filene dine. På skrivetidspunktet har de nettopp annonsert en Windows-skrivebordsklient, men Mac- og Linux-brukere må fortsette å bruke webversjonen for å synkronisere fra sine datamaskiner (foreløpig). Android-klienten er tilgjengelig som en APK eller via Aurora.
- [Skiff](https://skiff.com/download) tilbyr også betalt E2EE skyoppbevaring og filsamhandlingsverktøy. De tilbyr en skrivebordsklient for Mac og Windows (samt en webapp) og deres Android-klienter må lastes ned fra Aurora.
- [Nextcloud](https://f-droid.org/en/packages/com.nextcloud.client/) tilbyr en fullverdig skybasert løsning for samarbeid, kryssenhetsynkronisering og fillagring. Mer avanserte brukere kan velge å selv-hoste deres gratis og Open Source-programvare på hvilken som helst maskinvare de liker. Android-klientene kan lastes ned via F-Droid.
- [Cryptpad](https://cryptpad.fr/) tilbyr et gratis, webbasert, E2EE alternativ til Google Docs.

![bilde](assets/23.webp)

Proton Drive

## Ulempene

De Open Source og personvernbevarende alternativene til teknologikonglomeratapplikasjonene du har blitt vant til å bruke er mange, og noen av dem er ofte bedre enn de lukkede kildene, spionvareinfiserte alternativene.

Men når du flytter til GrapheneOS, er det noen komfortfunksjoner du må gi slipp på grunnet mangel på alternativer. Disse inkluderer:

- **Apple CarPlay/Android Auto** - Du må holde deg til god gammeldags Bluetooth, USB eller Aux.
- **Apple/Google Pay** - Stort sett alle har med seg lommeboken uansett!
- **Bankapplikasjoner** - Det er ikke slik at disse ikke fungerer i det hele tatt. Noen gjør det, perfekt faktisk. Andre fungerer kun med Google Play-tjenester aktivert (les mer om det nedenfor) og andre fungerer bare ikke i det hele tatt. Les rapporten om banken din [her](https://privsec.dev/posts/android/banking-applications-compatibility-with-grapheneos/) for å se den nåværende situasjonen. Frykt ikke hvis din er på listen som ikke fungerer, husk at du bare kan lagre URL-en som en webapp på hjemmeskjermen din.
- **Push-varsler** - De fleste applikasjoner som sender deg oppdateringer når du ikke bruker en spesifikk app, vil gjøre dette gjennom Google Play-tjenester. Disse er ikke installert som standard med GrapheneOS, så hvis du finner deg selv ikke å bli varslet umiddelbart når vennen din sender deg en e-post, er dette sannsynligvis hvorfor. Den gode nyheten er at noen av appene nevnt ovenfor har implementert sin egen bakgrunnsforbindelse for å periodisk sjekke etter oppdateringer og deretter gi deg et varsel der det er nødvendig

### Sandkasset Google Play
GrapheneOS har et kompatibilitetslag som gir muligheten til å installere og bruke de offisielle utgavene av Google Play i den standard app-sandkassen. Google Play mottar absolutt ingen spesielle tilganger eller privilegier på GrapheneOS i motsetning til å omgå app-sandkassen og motta en massiv mengde høyt privilegert tilgang.

Hvis du finner ut at du rett og slett ikke kan leve uten disse push-varslingene for din favorittapp, eller en viss "må ha"-app er ubrukelig uten Play-tjenester, tillater GrapheneOS deg å [installere](https://grapheneos.org/usage#sandboxed-google-play-installation) disse tjenestene i et helt sandkassert miljø. Når installert, krever disse tjenestene ingen Google-konto for å fungere, og hver enkelts tillatelser kan stramt kontrolleres.

Før du haster med å installere disse fra dag 1, oppfordrer jeg deg til å se hvor langt du kommer uten dem. Du vil sannsynligvis bli overrasket over hvor mange apper som fungerer helt normalt uten.

Hvis du ønsker å installere dem, trykk bare på den forhåndsinstallerte "Apps"-applikasjonen etterfulgt av "Google Play-tjenester". Vurder å installere dem sammen med de mindre private appene du ikke kan leve uten, inne i en helt separat brukerprofil for å gi det ekstra laget av adskillelse fra resten av telefonen din.

![bilde](assets/24.webp)

Installasjonsskjerm for Play-tjenester

### Profiler

GrapheneOS lar deg ha en separat telefonopplevelse, innenfor telefonen din. Ekstra profiler kan installere sine egne apper og tjenester og kan ikke få tilgang til noen filer eller data fra eierkontoen.
Hvis du bare har en eller to av de "må ha"-appene som krever Play-tjenester, men bare brukes veldig sjelden, kan det å installere disse sammen med Play-tjenester i en separat profil være en flott idé for å ytterligere styrke eventuelle minimale personvernimplikasjoner som er igjen ved å ha dem kjørende i eierprofilen.

Du kan lese mer om dette bruksområdet [her](https://discuss.grapheneos.org/d/168-ideas-for-user-profiles/2).

Hvis du bestemmer deg for å legge til en separat profil for å passe ditt bruksområde, kan appen [Insular](https://f-droid.org/en/packages/com.oasisfeng.island.fdroid/) være nyttig for deg. Insular lar deg enkelt klone noen av dine eksisterende apper over til den nye profilen uten behov for å gå via noen av de tradisjonelle installasjonsrutene som ble dekket tidligere i denne guiden. Insular lar deg også raskt "fryse" noen av disse appene for å fullstendig deaktivere alle appens bakgrunnstjenester fra å kjøre.

![bilde](assets/24.webp)

Skjerm for brukerprofiladministrasjon

### e-SIM

Hvis du ønsker å ta personvernet på telefonen din til neste nivå og ha en mobilservice som er løsrevet fra din virkelige identitet, kan en eSIM være noe for deg. En eSIM er et virtuelt SIM-kort som du kan kjøpe på nettet og legge til telefonen din via en QR-kode. Selskaper som tilbyr slike tjenester som kan betales for anonymt med Bitcoin inkluderer [Silent.Link](https://silent.link/) og [Bitrefill](https://www.bitrefill.com/gb/en/esims/).

eSIM bør ikke betraktes som en komplett løsning for telefonpersonvern. De kan være et nyttig verktøy når de er i de rette hendene, men vennligst gjør din forskning på [kompromissene](https://grapheneos.org/faq#cellular-tracking) ved å bruke enhver type mobilservice hvis din intensjon er å gå helt "off grid".

Sandkasserte Play-tjenester må installeres for eSIM-provisjonering i GrapheneOS.

## Sikkerhetskopiering
Etter at du har satt opp din nye de-Google'de Pixel-telefon, er det en god idé å opprette en sikkerhetskopi for deg selv. Denne sikkerhetskopien vil gjøre det mulig for deg å gjenopprette telefonen til en identisk tilstand i tilfelle du mister telefonen eller den blir mistet/stjålet.
Du kan velge å lagre sikkerhetskopifilen på et hvilket som helst eksternt lagringsmedium, eller til en selvhostet sky-løsning som Nextcloud, selv om noen brukere rapporterer om varierende suksessnivåer med sistnevnte alternativ.

For å opprette din første sikkerhetskopi:

1. Gå til **Innstillinger** > **System** > **Sikkerhetskopi**, og skriv ned din 12-ords gjenopprettingskode. Denne koden er nødvendig for å dekryptere sikkerhetskopifilen på et senere tidspunkt. Mister du koden, mister du tilgangen til telefonens sikkerhetskopi.
2. Velg deretter lagringsplasseringen din. Jeg vil anbefale et eksternt USB-drev eller et industrigradert microSD-kort.
3. Velg dataene som skal sikkerhetskopieres. Hvis du har plass på det angitte lagringsmediet, vil jeg råde deg til å velge alt.
4. Trykk på de tre prikkene øverst til høyre, og velg **Sikkerhetskopier nå**.

![bilde](assets/26.webp)

Sikkerhetskopi-skjerm

Husk at hvis du lager offline sikkerhetskopier til eksterne lagringsmedier, gir det mening å fullføre dette steget regelmessig for å sikre at eventuelle nylige viktige oppdateringer til telefonen din ikke går tapt hvis det verste skulle skje.

![video](https://www.youtube.com/embed/eyWmcItzisk)

Video som detaljerer sikkerhetskopiprosessen

## Konklusjon

I løpet av de siste årene har GrapheneOS-programvaren modnet betydelig. Den er mer stabil og kompatibel enn noensinne. Dette, sammen med det blomstrende økosystemet av Open Source og personvernbevarende apper, gjør GrapheneOS til et virkelig levedyktig alternativ til standard Android eller iOS, selv for 'normale' mennesker akkurat som deg!

Datainnbrudd og masseovervåkning er så vanlige i dagens verden at de knapt lager overskrifter lenger. Det er opp til deg å beskytte deg selv. Det vil være justeringer og ofre som må gjøres underveis, men å redusere din eksponering for slike inngrep er ikke i nærheten så vanskelig som du tror det vil være.

Jeg håper denne guiden går noen vei for å hjelpe deg på din reise. Hvis du fant denne guiden nyttig og ønsker å støtte mitt arbeid, vennligst vurder å sende en [donasjon](/tips).

Hvis du allerede er en GrapheneOS-bruker, eller blir en som et resultat av denne guiden, vurder å [donere](https://grapheneos.org/donate) for å støtte deres viktige arbeid.

### Lær mer

GrapheneOS er et kaninhull enhver kunne lett tilbringe uker på å utforske. Det er bare så mye du kan lære og tukle med for å skreddersy opplevelsen til dine krav og trusselmodeller. Nedenfor er noen lenker hvor du kan fortsette din reise:

- [GrapheneOS Offisiell Brukerguide](https://grapheneos.org/usage) - Offisiell Nettside
- [GrapheneOS Forum](https://discuss.grapheneos.org/) - Offisiell Nettside
- [GrapheneOS Innstillinger Masterclass](https://www.youtube.com/watch?app=desktop&v=GLJyD9MJgIQ) - Video av 'The Privacy Wayfinder'
- [GrapheneOS Generell Podcast](https://www.youtube.com/watch?app=desktop&v=UCPX0mFFRNA) - Podcast av 'Watchman Privacy'

full kreditt til: https://github.com/BitcoinQnA/Bitcoiner.Guide/blob/main/grapheneos.md