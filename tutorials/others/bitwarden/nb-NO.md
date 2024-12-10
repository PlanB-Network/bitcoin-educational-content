---
name: Bitwarden
description: Hvordan sette opp en passordbehandler?
---
![cover](assets/cover.webp)

I den digitale tidsalderen trenger vi å håndtere en mengde online kontoer som dekker ulike aspekter av vårt daglige liv, inkludert bankvirksomhet, finansielle plattformer, e-poster, fillagring, helse, administrasjon, sosiale nettverk, videospill, osv.

For å autentisere oss på hver av disse kontoene, bruker vi en identifikator, ofte en e-postadresse, ledsaget av et passord. Faced med umuligheten av å memorere et stort antall unike passord, kan man bli fristet til å gjenbruke samme passord eller lett modifisere en felles base for å huske det enkelt. Imidlertid kompromitterer disse praksisene alvorlig sikkerheten til kontoene dine.

Det første prinsippet å følge for passord er å ikke gjenbruke dem. Hver online konto bør beskyttes av et unikt passord som er helt forskjellig fra de andre. Dette er viktig fordi, hvis en angriper klarer å kompromittere et av passordene dine, vil du ikke at de skal ha tilgang til alle kontoene dine. Å ha et unikt passord for hver konto isolerer potensielle angrep og begrenser deres omfang. For eksempel, hvis du bruker samme passord for en videospillplattform og for din e-post, og det passordet blir kompromittert via en phishing-side relatert til spillplattformen, kunne angriperen da enkelt få tilgang til din e-post og ta kontroll over alle dine andre online kontoer.

Det andre essensielle prinsippet er passordets styrke. Et passord anses som sterkt hvis det er vanskelig å brute force, det vil si å gjette gjennom prøving og feiling. Dette betyr at passordene dine må være så tilfeldige som mulig, lange, og inkludere en variasjon av tegn (små bokstaver, store bokstaver, tall og symboler).

Å anvende disse to prinsippene for passordsikkerhet (unikhet og robusthet) kan vise seg vanskelig i dagliglivet, ettersom det er nesten umulig å memorere et unikt, tilfeldig og sterkt passord for alle våre kontoer. Dette er hvor passordbehandleren kommer inn i bildet.

En passordbehandler genererer og lagrer sterke passord på en sikker måte, og lar deg få tilgang til alle dine online kontoer uten behovet for å memorere dem individuelt. Du trenger bare å huske ett passord, hovedpassordet, som gir deg tilgang til alle dine lagrede passord i behandleren. Å bruke en passordbehandler forbedrer din online sikkerhet fordi det forhindrer gjenbruk av passord og systematisk genererer tilfeldige passord. Men det forenkler også din daglige bruk av kontoene dine ved å sentralisere tilgangen til din sensitive informasjon.
I denne veiledningen vil vi utforske hvordan man setter opp og bruker en passordbehandler for å forbedre din online sikkerhet. Jeg vil introdusere deg for Bitwarden, og i en annen veiledning, vil vi se på en annen løsning kalt KeePass.
https://planb.network/tutorials/others/general/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Advarsel: En passordbehandler er flott for å lagre passord, men **du bør aldri lagre din Bitcoin lommeboks' mnemonic frase i den!** Husk, en mnemonic frase bør eksklusivt lagres i et fysisk format, som et stykke papir eller metall.

## Introduksjon til Bitwarden

Bitwarden er en passordbehandler som passer for både nybegynnere og avanserte brukere. Den tilbyr mange fordeler. Først og fremst er Bitwarden en multi-plattform løsning, noe som betyr at du kan bruke den som en mobilapp, webapplikasjon, nettleserutvidelse, og skrivebordsprogramvare.
![BITWARDEN](assets/notext/01.webp)
Bitwarden lar deg lagre passordene dine online og synkronisere dem på tvers av alle dine enheter, samtidig som den sikrer ende-til-ende-kryptering med ditt hovedpassord. Dette gjør det mulig for deg, for eksempel, å få tilgang til passordene dine på både datamaskinen og smarttelefonen, med synkronisering mellom de to. Siden passordene dine er kryptert, forblir de utilgjengelige for noen, inkludert Bitwarden, uten dekrypteringsnøkkelen som er ditt hovedpassord.
I tillegg er Bitwarden åpen kildekode, noe som betyr at programvaren kan revideres av uavhengige eksperter. Når det gjelder prising, tilbyr Bitwarden tre planer:
- En gratis versjon som vi vil utforske i denne opplæringen. Selv om den er gratis, tilbyr den et sikkerhetsnivå tilsvarende de betalte versjonene. Du kan lagre et ubegrenset antall passord og synkronisere så mange enheter du ønsker;
- En premiumversjon for $10 per år som inkluderer tilleggsfunksjoner som fillagring, sikkerhetskopi av bankkort, muligheten til å sette opp 2FA med en fysisk sikkerhetsnøkkel, og tilgang til TOTP 2FA-autentisering direkte med Bitwarden;
- Og en familieplan for $40 per år som utvider fordelene med premiumversjonen til seks forskjellige brukere.
![BITWARDEN](assets/notext/02.webp)
Etter min mening er disse prisene rimelige. Den gratis versjonen er et utmerket alternativ for nybegynnere, og premiumversjonen tilbyr veldig god verdi for pengene sammenlignet med andre passordadministratorer på markedet, samtidig som den tilbyr flere funksjoner. I tillegg er det faktum at Bitwarden er åpen kildekode en stor fordel. Derfor er det et interessant kompromiss, spesielt for nybegynnere.
En annen funksjon ved Bitwarden er muligheten til å selv-hoste din passordadministrator hvis du for eksempel eier en NAS hjemme. Ved å sette opp denne konfigurasjonen lagres ikke passordene dine på Bitwardens servere, men på dine egne servere. Dette gir deg full kontroll over tilgjengeligheten til passordene dine. Imidlertid krever dette alternativet nøye backuphåndtering for å unngå tap av tilgang. Derfor er Bitwardens selv-hosting mer egnet for avanserte brukere, og vi vil diskutere dette i en annen opplæring.
## Hvordan opprette en Bitwarden-konto?

Besøk [Bitwarden-nettstedet](https://bitwarden.com/) og klikk på "*Kom i gang*".
![BITWARDEN](assets/notext/03.webp)
Start med å oppgi din e-postadresse samt ditt navn eller kallenavn.
![BITWARDEN](assets/notext/04.webp)
Deretter må du sette opp ditt hovedpassord. Som vi så i introduksjonen, er dette passordet veldig viktig fordi det gir deg tilgang til alle dine andre lagrede passord i administratoren. Det presenterer derfor to hovedrisikoer: tap og kompromittering. Hvis du mister tilgangen til dette passordet, vil du ikke lenger kunne få tilgang til alle dine legitimasjoner. Hvis passordet ditt blir stjålet, vil angriperen kunne få tilgang til alle kontoene dine.

For å minimere risikoen for tap, anbefaler jeg å lage en fysisk sikkerhetskopi av hovedpassordet ditt på papir og lagre det på et sikkert sted. Om mulig, forsegl denne sikkerhetskopien i en sikker konvolutt for å regelmessig forsikre deg om at ingen andre har hatt tilgang til den.

For å forhindre kompromittering av hovedpassordet ditt, må det være ekstremt robust. Det bør være så langt som mulig, bruke et bredt utvalg av tegn, og velges tilfeldig. I 2024 er minimumsanbefalingene for et sikkert passord 13 tegn inkludert tall, små og store bokstaver, samt symboler, forutsatt at passordet er virkelig tilfeldig. Jeg anbefaler imidlertid å velge et passord på minst 20 tegn, inkludert alle mulige typer tegn, for å sikre dets sikkerhet lenger.

Skriv inn hovedpassordet ditt i det dedikerte feltet og bekreft det i det følgende feltet.
![BITWARDEN](assets/notext/05.webp)
Om du ønsker, kan du legge til et hint for ditt hovedpassord. Jeg råder imidlertid mot å gjøre dette, ettersom hintet ikke gir en pålitelig metode for gjenoppretting i tilfelle du mister passordet ditt og til og med kan være nyttig for angripere som forsøker å gjette eller brute force ditt passord. Som en generell regel, unngå å lage offentlige hint som kan kompromittere sikkerheten til ditt hovedpassord.
![BITWARDEN](assets/notext/06.webp)
Deretter klikker du på "*Opprett en konto*" knappen.
![BITWARDEN](assets/notext/07.webp)
Du kan nå logge inn på din nye Bitwarden-konto. Skriv inn din e-postadresse.
![BITWARDEN](assets/notext/08.webp)
Skriv deretter inn ditt hovedpassord.
![BITWARDEN](assets/notext/09.webp)
Du er nå på webgrensesnittet til din passordbehandler.
![BITWARDEN](assets/notext/10.webp)
## Hvordan sette opp Bitwarden?

For å starte, vil vi bekrefte vår e-postadresse. Klikk på "*Send e-post*".
![BITWARDEN](assets/notext/11.webp)
Klikk deretter på knappen mottatt på e-post.
![BITWARDEN](assets/notext/12.webp)
Til slutt, logg inn igjen.
![BITWARDEN](assets/notext/13.webp)
Først og fremst, anbefaler jeg sterkt at du setter opp tofaktorautentisering (2FA) for å sikre din passordbehandler. Du har valget mellom å bruke en TOTP-applikasjon eller en fysisk sikkerhetsnøkkel. Ved å aktivere 2FA, hver gang du logger inn på din Bitwarden-konto, vil du bli bedt om ikke bare ditt hovedpassord, men også om bevis på din andre faktor for autentisering. Dette er et ekstra lag med sikkerhet, spesielt nyttig i tilfelle din papirbackup av hovedpassordet blir kompromittert.

Hvis du er usikker på hvordan du setter opp og bruker disse 2FA-enhetene, anbefaler jeg å følge disse 2 andre opplæringene:

https://planb.network/tutorials/others/general/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

https://planb.network/tutorials/others/general/security-key-61438267-74db-4f1a-87e4-97c8e673533e

For å gjøre dette, gå til "*Sikkerhet*" fanen i "*Innstillinger*" menyen.
![BITWARDEN](assets/notext/14.webp)
Klikk deretter på "*To-trinns innlogging*" fanen.
![BITWARDEN](assets/notext/15.webp)
Her kan du velge 2FA-metoden du foretrekker. For eksempel, jeg vil velge 2FA med en TOTP-applikasjon ved å klikke på "*Administrer*" knappen.
![BITWARDEN](assets/notext/16.webp)
Bekreft ditt hovedpassord.
![BITWARDEN](assets/notext/17.webp)
Skann deretter QR-koden med din 2FA-applikasjon.
![BITWARDEN](assets/notext/18.webp)
Skriv inn den 6-sifrede koden notert på din 2FA-applikasjon, deretter klikk på "*Slå på*" knappen. ![BITWARDEN](assets/notext/19.webp)
Tofaktorautentisering har blitt vellykket satt opp på din konto.
![BITWARDEN](assets/notext/20.webp)
Nå, hvis du prøver å logge inn på din manager igjen, må du først skrive inn ditt hovedpassord, deretter den dynamiske 6-sifrede koden generert av din 2FA-applikasjon. Sørg for at du alltid har tilgang til denne dynamiske koden; uten den, vil du være ute av stand til å gjenopprette passordene dine.
![BITWARDEN](assets/notext/21.webp)
I innstillingene har du også muligheten til å tilpasse din manager i "*Preferanser*" fanen. Her kan du endre varigheten før din manager automatisk låses, samt språket og temaet til grensesnittet.
![BITWARDEN](assets/notext/22.webp)Jeg anbefaler sterkt å justere lengden på passordene som genereres av Bitwarden. Som standard er lengden satt til 14 tegn, noe som kan være utilstrekkelig for optimal sikkerhet. Nå som du har en manager for å huske alle passordene dine, kan du like godt dra nytte av det for å bruke veldig sterke passord.

For dette, gå til "*Generator*" menyen.
![BITWARDEN](assets/notext/23.webp)
Her kan du øke lengden på passordene dine til 40, og krysse av for å inkludere symboler.
![BITWARDEN](assets/notext/24.webp)
## Hvordan sikre kontoene dine med Bitwarden?

Nå som passordbehandleren din er konfigurert, kan du begynne å lagre legitimasjonen for dine nettbaserte kontoer. For å legge til en ny gjenstand, klikk direkte på "*Ny gjenstand*" knappen eller på "*Ny*" knappen som ligger øverst til høyre på skjermen, deretter på "*gjenstand*".
![BITWARDEN](assets/notext/25.webp)
I skjemaet som åpnes, start med å bestemme naturen til gjenstanden som skal lagres. For å lagre innloggingsopplysninger, velg "*Login*" alternativet fra nedtrekksmenyen.
![BITWARDEN](assets/notext/26.webp)
I "*Name*" feltet, skriv inn et beskrivende navn for dine legitimasjoner. Dette vil gjøre det lettere å søke etter og organisere passordene dine, spesielt hvis du har et stort antall. For eksempel, hvis du vil lagre dine legitimasjoner for PlanB Network-siden, kan du navngi denne gjenstanden på en måte som gjør den umiddelbart gjenkjennelig under dine fremtidige søk.
![BITWARDEN](assets/notext/27.webp)
"*Folder*" alternativet lar deg klassifisere dine legitimasjoner i mapper. Foreløpig har vi ikke opprettet noen ennå, men jeg vil vise deg hvordan du gjør det senere.
![BITWARDEN](assets/notext/28.webp)
I "*Username*" feltet, skriv inn ditt brukernavn, som vanligvis er din e-postadresse. ![BITWARDEN](assets/notext/29.webp)
Deretter, i "*Password*" feltet, kan du skrive inn passordet ditt. Jeg anbefaler imidlertid sterkt å la Bitwarden generere et langt, tilfeldig og unikt passord for deg. Dette sikrer at du har et sterkt passord. For å bruke denne funksjonen, klikk på dobbeltpilikonet over feltet som skal fylles ut.
![BITWARDEN](assets/notext/30.webp)
Du kan se at passordet ditt har blitt generert.
![BITWARDEN](assets/notext/31.webp)
I "*URI 1*" feltet, kan du skrive inn domenenavnet til nettstedet.
![BITWARDEN](assets/notext/32.webp)
Og til slutt, i "*Notes*" feltet, kan du legge til ytterligere detaljer om nødvendig.
![BITWARDEN](assets/notext/33.webp)
Når du har fylt ut alle disse feltene, klikk på "*Save*" knappen.
![BITWARDEN](assets/notext/34.webp)
Din identifikator vises nå i din Bitwarden manager.
![BITWARDEN](assets/notext/35.webp)
Ved å klikke på den, kan du få tilgang til detaljene og endre dem.
![BITWARDEN](assets/notext/36.webp)
Ved å klikke på de tre små prikkene til høyre, har du rask tilgang til å kopiere passordet eller identifikatoren.
![BITWARDEN](assets/notext/37.webp)
Gratulerer, du har vellykket lagret ditt første passord i din manager! Hvis du ønsker å bedre organisere dine identifikatorer, kan du opprette spesifikke mapper. For å gjøre dette, klikk på "*Ny*" knappen som er plassert øverst til høyre på skjermen, deretter velg "*Mappe*".![BITWARDEN](assets/notext/38.webp)
Skriv inn et navn for mappen din.
![BITWARDEN](assets/notext/39.webp)
Deretter klikker du på "*Lagre*".
![BITWARDEN](assets/notext/40.webp)
Mappen din vises nå i din manager.
![BITWARDEN](assets/notext/41.webp)
Du kan tilordne en mappe til en identifikator når du oppretter den, slik vi gjorde tidligere, eller ved å endre en eksisterende identifikator. For eksempel, ved å klikke på min identifikator for PlanB Network, kan jeg deretter velge å klassifisere den i "*Bitcoin*" mappen.
![BITWARDEN](assets/notext/42.webp)
På denne måten kan du strukturere din passordmanager for å gjøre det lettere å finne dine identifikatorer. Du kan organisere dem med mapper som personlig, profesjonell, banker, e-poster, sosiale nettverk, abonnementer, shopping, administrasjon, strømming, lagring, reise, helse, osv.
Hvis du foretrekker å kun bruke webversjonen av Bitwarden, er det helt mulig å holde seg til det. Jeg anbefaler da å legge til din passordmanager i nettleserens favoritter for enkel tilgang og for å unngå phishing-risiko. Imidlertid tilbyr Bitwarden også et fullt spekter av klienter som lar deg bruke din manager på ulike enheter og forenkle dens daglige bruk. De tilbyr spesielt en mobilapp, en nettleserutvidelse og skrivebordsprogramvare. La oss se hvordan vi setter dem opp sammen.

![BITWARDEN](assets/notext/43.webp)

## Hvordan bruke Bitwarden nettleserutvidelsen?

Først kan du sette opp nettleserutvidelsen hvis du ønsker. Denne utvidelsen fungerer som en redusert versjon av din manager og tilbyr deg muligheten til automatisk å lagre nye passord, generere forslag til sikre passord, og automatisk fylle inn dine legitimasjoner på innloggingssider på nettsteder.

Den daglige bruken av denne utvidelsen er ekstremt praktisk, men den kan også åpne nye vektorer for angrep. Noen cybersikkerhetseksperter råder derfor mot å bruke nettleserutvidelser for passordmanagere. Imidlertid, hvis du velger å bruke Bitwarden-utvidelsen, her er hvordan du går frem:

Start med å gå til [den offisielle Bitwarden nedlastingssiden](https://bitwarden.com/download/#downloads-web-browser).

![BITWARDEN](assets/notext/44.webp)

Velg din nettleser fra listen som tilbys. For dette eksempelet bruker jeg Firefox, så jeg blir omdirigert til den offisielle Bitwarden-utvidelsen på Firefox Add-ons Store. Prosedyren er ganske lik for andre nettlesere.

![BITWARDEN](assets/notext/45.webp)

Klikk på "*Legg til i Firefox*" knappen.

![BITWARDEN](assets/notext/46.webp)

Du kan deretter feste Bitwarden til din utvidelsesbar for enkel tilgang. Klikk på utvidelsen for å logge inn.

![BITWARDEN](assets/notext/47.webp)

Skriv inn din e-postadresse.

![BITWARDEN](assets/notext/48.webp)

Deretter ditt hovedpassord.

![BITWARDEN](assets/notext/49.webp)

Og til slutt, skriv inn den 6-sifrede koden fra din autentiseringsapp.

![BITWARDEN](assets/notext/50.webp)

Du er nå koblet til din Bitwarden manager gjennom nettleserutvidelsen.

![BITWARDEN](assets/notext/51.webp)
For eksempel, hvis jeg går tilbake til PlanB Network-nettstedet og prøver å logge inn på kontoen min, kan du se at Bitwarden-utvidelsen integrert i nettleseren gjenkjenner innloggingsfeltene og automatisk tilbyr meg å velge identifikatoren jeg tidligere lagret.
![BITWARDEN](assets/notext/52.webp)
Hvis jeg velger denne identifikatoren, fyller Bitwarden inn innloggingsfeltene for meg. Denne funksjonen til utvidelsen tillater rask tilkobling til nettsteder, uten behovet for å kopiere og lime inn legitimasjon fra Bitwarden-webapplikasjonen eller programvaren.
![BITWARDEN](assets/notext/53.webp)
Utvidelsen er også designet for å oppdage opprettelsen av nye kontoer. For eksempel, når jeg oppretter en ny konto på PlanB Network, foreslår Bitwarden automatisk å lagre den nye identifikatoren.
![BITWARDEN](assets/notext/54.webp)
Ved å klikke på dette forslaget som vises, åpnes utvidelsen. Den lar meg angi detaljene for den nye identifikatoren og generere et sterkt, unikt passord.
![BITWARDEN](assets/notext/55.webp)
Etter å ha fullført informasjonen og klikket på "*Lagre*", lagrer utvidelsen legitimasjonen.
![BITWARDEN](assets/notext/56.webp)
Deretter fyller utvidelsen automatisk inn legitimasjonen vår i de aktuelle feltene på nettstedet.
![BITWARDEN](assets/notext/57.webp)
## Hvordan bruke Bitwarden-programvaren?

For å installere Bitwarden-skrivebordsprogramvaren, start med å gå til [nedlastingssiden](https://bitwarden.com/download/#downloads-desktop). Velg og last ned versjonen som tilsvarer operativsystemet ditt.
![BITWARDEN](assets/notext/58.webp)
Når nedlastingen er fullført, fortsett med programvareinstallasjonen på datamaskinen din. Ved første oppstart av Bitwarden-programvaren, må du angi legitimasjonen din for å låse opp passordbehandleren din.
![BITWARDEN](assets/notext/59.webp)
Deretter vil du komme til hjemmesiden til din behandler. Grensesnittet er nesten det samme som på webapplikasjonen.
![BITWARDEN](assets/notext/60.webp)
## Hvordan bruke Bitwarden-applikasjonen?

For å få tilgang til passordene dine fra telefonen, kan du installere Bitwarden mobilapplikasjonen. Start med å gå til [nedlastingssiden](https://bitwarden.com/download/#downloads-mobile) og bruk smarttelefonen din til å skanne QR-koden som tilsvarer operativsystemet ditt.
![BITWARDEN](assets/notext/61.webp)
Last ned og installer den offisielle Bitwarden mobilapplikasjonen. Ved første åpning av applikasjonen, skriv inn legitimasjonen din for å låse opp tilgangen til passordbehandleren din.
![BITWARDEN](assets/notext/62.webp)
Når du er tilkoblet, vil du kunne konsultere og administrere alle passordene dine direkte fra applikasjonen.
![BITWARDEN](assets/notext/63.webp)
For å forbedre sikkerheten til applikasjonen din, råder jeg deg til å gå inn i innstillingene og aktivere PIN-beskyttelse. Dette vil legge til et ekstra lag med sikkerhet i tilfelle tap eller tyveri av telefonen din.
![BITWARDEN](assets/notext/64.webp)
## Hvordan ta sikkerhetskopi av Bitwarden?
For å sikre at du aldri mister tilgangen til passordene dine, selv i tilfelle du mister hovedpassordet ditt eller en katastrofe påvirker Bitwardens servere, råder jeg deg til å jevnlig utføre en kryptert sikkerhetskopi av behandleren din på et eksternt medium.
Ideen er å kryptere alle dine Bitwarden-legitimasjoner med et passord som er forskjellig fra ditt hovedpassord og lagre denne krypterte sikkerhetskopien på en USB-stick eller en harddisk som du oppbevarer hjemme, for eksempel. Du kan deretter oppbevare en fysisk kopi av dekrypteringspassordet på et separat sted fra hvor sikkerhetskopimediet er lagret. For eksempel kan du oppbevare USB-sticken hjemme og betro den fysiske kopien av krypteringspassordet til en pålitelig venn.

Denne metoden sikrer at selv om sikkerhetskopimediet ditt blir stjålet, vil dataene dine forbli utilgjengelige uten dekrypteringspassordet. På samme måte vil ikke vennen din kunne få tilgang til dataene dine uten å ha det fysiske mediet.

Men, i tilfelle et problem, kan du bruke passordet og det eksterne mediet for å gjenopprette tilgangen til legitimasjonene dine, uavhengig av Bitwarden. Så selv om Bitwardens servere skulle bli ødelagt, ville du fortsatt ha muligheten til å hente passordene dine.

Derfor råder jeg deg til å utføre disse sikkerhetskopiene regelmessig slik at de alltid inkluderer dine nyeste legitimasjoner. For å unngå å bry vennen din, som har en kopi av krypteringspassordet, med hver ny sikkerhetskopi, kan du lagre dette passordet i passordbehandleren din. Dette er ikke ment som en sikkerhetskopi, siden vennen din allerede har en fysisk kopi, men heller for å forenkle dine fremtidige eksportprosedyrer.

For å fortsette med eksporten, er det ganske enkelt: gå til "*Verktøy*" seksjonen i din Bitwarden-behandler, og velg deretter "*Eksporter hvelv*".
![BITWARDEN](assets/notext/65.webp)
For formatet, velg "*.json (Kryptert)*".
![BITWARDEN](assets/notext/66.webp)
Velg deretter alternativet "*Passordbeskyttet*".
![BITWARDEN](assets/notext/67.webp)
Her er det viktig å velge et sterkt, unikt og tilfeldig generert passord for å kryptere sikkerhetskopien. Dette sikrer at, selv i tilfelle tyveri av din krypterte sikkerhetskopi, vil det være umulig for en angriper å dekryptere den ved brute force.
![BITWARDEN](assets/notext/68.webp)
Klikk på "*Bekreft format*" og skriv inn ditt hovedpassord for å fortsette med eksporten.
![BITWARDEN](assets/notext/69.webp)
Når eksporten er fullført, vil du finne din krypterte sikkerhetskopi i nedlastningene dine. Overfør den til en sikker ekstern lagringsenhet, som en USB-stick eller en harddisk. Gjenta denne operasjonen periodisk avhengig av bruken din. For eksempel kan du fornye sikkerhetskopien hver uke eller hver måned, avhengig av dine behov.