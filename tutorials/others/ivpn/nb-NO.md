---
name: IVPN
description: Oppsett av en VPN betalt med bitcoins
---
![cover](assets/cover.webp)

En VPN ("*Virtual Private Network*") er en tjeneste som etablerer en sikker og kryptert forbindelse mellom telefonen eller datamaskinen din og en ekstern server som administreres av VPN-leverandøren.

Teknisk sett, når du kobler til en VPN, blir internett-trafikken din omdirigert gjennom en kryptert tunnel til VPN-serveren. Denne prosessen gjør det vanskelig for tredjeparter, som internettleverandører (ISPs) eller ondsinnede aktører, å avlytte eller lese dataene dine. VPN-serveren fungerer deretter som en mellommann som kobler seg til tjenesten du ønsker å bruke på dine vegne. Den tildeler en ny IP-adresse til tilkoblingen din, noe som bidrar til å skjule din virkelige IP-adresse fra nettstedene du besøker. Imidlertid, i motsetning til hva noen online annonser kan antyde, tillater ikke bruk av en VPN deg å surfe på internett anonymt, ettersom det krever en form for tillit til VPN-leverandøren som kan se all trafikken din.
![IVPN](assets/fr/01.webp)
Fordelene med å bruke en VPN er mange. For det første bevarer det personvernet til din online aktivitet fra ISPs eller regjeringer, forutsatt at VPN-leverandøren ikke deler informasjonen din. For det andre sikrer det dataene dine, spesielt når du er koblet til offentlige Wi-Fi-nettverk, som er sårbare for MITM (man-in-the-middle) angrep. For det tredje, ved å skjule IP-adressen din, tillater en VPN deg å omgå geografiske restriksjoner og sensur, for å få tilgang til innhold som ellers ville vært utilgjengelig eller blokkert i din region.

Som du kan se, flytter VPN risikoen for trafikkobservasjon til VPN-leverandøren. Derfor, når du velger din VPN-leverandør, er det viktig å vurdere personopplysningene som kreves for registrering. Hvis leverandøren ber om informasjon som ditt telefonnummer, e-postadresse, bankkortdetaljer, eller verre, din postadresse, økes risikoen for å assosiere din identitet med trafikken din. I tilfelle et kompromiss av leverandøren eller en juridisk beslagleggelse, ville det være enkelt å assosiere trafikken din med dine personlige data. Derfor anbefales det å velge en leverandør som ikke krever noen personopplysninger og aksepterer anonyme betalinger, som med bitcoins.

I denne veiledningen presenterer jeg en enkel, effektiv, rimelig priset VPN-løsning som ikke krever noen personlige opplysninger for bruk.

## Introduksjon til IVPN

IVPN er en VPN-tjeneste designet spesielt for brukere som søker en form for personvern. I motsetning til populære VPN-leverandører ofte promotert på YouTube, skiller IVPN seg ut for sin transparens, sikkerhet og respekt for personvern.
IVPNs personvernpolicy er streng: ingen personlige opplysninger kreves ved registrering. Du kan åpne en konto uten å oppgi e-postadresse, navn eller telefonnummer. For betaling er det ikke nødvendig å oppgi kredittkortdetaljer, ettersom IVPN aksepterer betalinger i bitcoins (onchain og Lightning). Videre hevder IVPN å ikke beholde noen aktivitetslogger, noe som betyr at, i teorien, blir ikke internett-trafikken din registrert av selskapet.
IVPN er også [helt åpen kildekode](https://github.com/ivpn), med hensyn til sin programvare, applikasjoner og til og med deres nettsted, noe som tillater hvem som helst å verifisere og gjennomgå koden deres. De gjennomgår også uavhengige sikkerhetsrevisjoner årlig, hvis resultater publiseres på deres nettsted.

IVPN bruker utelukkende selvhostede servere, og eliminerer dermed risikoene forbundet med å bruke tredjeparts skytjenester, som AWS, Google Cloud eller Microsoft Azure.

Tjenesten tilbyr mange avanserte funksjoner, som multi-hop, som ruter trafikk gjennom flere servere lokalisert i forskjellige jurisdiksjoner for å forbedre anonymiteten. IVPN integrerer også en sporings- og annonseblokkerer, og tilbyr muligheten til å velge mellom forskjellige VPN-protokoller.
Selvfølgelig kommer denne kvaliteten på tjenesten til en pris, men en passende pris er ofte en indikator på kvalitet og ærlighet. Det kan signalisere at selskapet har en forretningsmodell uten behov for å selge personlige data. IVPN tilbyr deretter 2 typer planer: Standardplanen, som tillater tilkobling av opptil 2 enheter, og Pro-planen, som tillater opptil 7 tilkoblinger og inkluderer "*Multi-hop*" protokollen som ruter trafikken din gjennom flere servere.
I motsetning til mainstream VPN-leverandører, opererer IVPN på en modell der man kjøper tilgangstid til tjenesten, i stedet for et gjentakende abonnement. Du betaler i bitcoins én gang for den valgte varigheten. For eksempel, hvis du kjøper ett år med tilgang, kan du bruke tjenesten for den perioden, hvorpå du må returnere til IVPN-nettstedet for å kjøpe mer tilgangstid.

[IVPN-prisene](https://www.ivpn.net/en/pricing/) er progressive avhengig av kjøpt tilgangsvarighet. Her er prisene for Standardplanen:
- 1 uke: $2
- 1 måned: $6
- 1 år: $60
- 2 år: $100
- 3 år: $140

Og for Pro-planen:
- 1 uke: $4
- 1 måned: $10
- 1 år: $100
- 2 år: $160
- 3 år: $220

## Hvordan installere IVPN på en datamaskin?
Last ned [den nyeste versjonen av programvaren](https://www.ivpn.net/en/apps-windows/) for ditt operativsystem, og fortsett med installasjonen ved å følge trinnene i installasjonsveiviseren. ![IVPN](assets/notext/02.webp)
For Linux-brukere, se instruksjonene spesifikke for din distribusjon tilgjengelig på [denne siden](https://www.ivpn.net/en/apps-linux/).
![IVPN](assets/notext/03.webp)
Når installasjonen er fullført, må du angi din konto-ID. Vi vil se hvordan vi får den i de følgende delene av denne opplæringen.
![IVPN](assets/notext/04.webp)
## Hvordan installere IVPN på en smarttelefon?

Last ned IVPN fra appbutikken din, enten det er [AppStore](https://apps.apple.com/us/app/ivpn-secure-vpn-for-privacy/id1193122683) for iOS-brukere, [Google Play Store](https://play.google.com/store/apps/details?id=net.ivpn.client) for Android, eller [F-Droid](https://f-droid.org/en/packages/net.ivpn.client). Hvis du bruker Android, har du også muligheten til å laste ned `.apk`-filen direkte fra [IVPN-nettstedet](https://www.ivpn.net/en/apps-android/).
![IVPN](assets/notext/05.webp)
Ved første bruk av appen, vil du bli logget ut. Du må angi din konto-ID for å aktivere tjenesten.
![IVPN](assets/notext/06.webp)
Nå, la oss gå videre til å aktivere IVPN på enhetene dine.

## Hvordan betale for og aktivere IVPN?

Gå til det offisielle IVPN-nettstedet [på betalingssiden](https://www.ivpn.net/en/pricing/).
![IVPN](assets/notext/07.webp)
Velg planen som best passer dine behov. For denne opplæringen vil vi velge Standardplanen, som lar oss aktivere VPN på vår datamaskin og smarttelefon, for eksempel.
![IVPN](assets/notext/08.webp)
IVPN vil da opprette kontoen din. Du trenger ikke å oppgi noen personlige data. Det er kun din konto-ID som vil tillate deg å logge inn. Den fungerer noe som en tilgangsnøkkel. Lagre den på et sikkert sted, som for eksempel din passordbehandler. Du kan også lage en papirkopi. ![IVPN](assets/notext/09.webp)
På samme side, velg varigheten på abonnementet ditt til tjenesten.
![IVPN](assets/notext/10.webp)
Velg deretter betalingsmetoden din. For min del, vil jeg gjøre betalingen via Lightning Network, så jeg klikker på "*Bitcoin*" knappen.
![IVPN](assets/notext/11.webp)
Sjekk at alt er til din tilfredshet og klikk deretter på "*Betal med Lightning*" knappen.
![IVPN](assets/notext/12.webp)
En Lightning-faktura vil bli presentert for deg på deres BTCPay Server. Skann QR-koden med din Lightning-lommebok og fortsett med betalingen.
![IVPN](assets/notext/13.webp) Når fakturaen er betalt, klikk på "*Returner til IVPN*" knappen.
![IVPN](assets/notext/14.webp)
Kontoen din vises nå som "*Aktiv*," og du kan se datoen til hvilken din tilgang til VPN er gyldig. Etter denne datoen, må du fornye betalingen din.
![IVPN](assets/notext/15.webp)
For å aktivere tilkoblingen din via IVPN på din PC, kopier ganske enkelt din konto-ID.
![IVPN](assets/notext/16.webp)
Og lim den inn i programvaren du tidligere lastet ned.
![IVPN](assets/notext/17.webp)
Klikk deretter på "*Logg inn*" knappen.
![IVPN](assets/notext/18.webp)
Klikk på hake for å aktivere VPN-tilkoblingen, og der har du det, din datamaskins internetttrafikk er nå kryptert og rutet gjennom en IVPN-server.
![IVPN](assets/notext/19.webp)
For din smarttelefon, er prosedyren identisk. Lim inn din konto-ID eller skann QR-koden assosiert med din IVPN-konto tilgjengelig fra nettsiden. Deretter, klikk på haken for å etablere tilkoblingen.
![IVPN](assets/notext/20.webp)
## Hvordan bruke og konfigurere IVPN?

Når det gjelder bruk og innstillinger, er det ganske enkelt. Fra hovedgrensesnittet kan du aktivere eller deaktivere tilkoblingen enkelt ved å bruke haken.
![IVPN](assets/notext/21.webp)
Du har også muligheten til å pause din VPN for en spesifikk varighet.
![IVPN](assets/notext/22.webp)
Ved å klikke på den nåværende serveren, kan du velge en annen server fra de tilgjengelige.
![IVPN](assets/notext/23.webp)
Det er også mulig å aktivere eller deaktivere den integrerte brannmuren samt anti-tracker-funksjonen.
![IVPN](assets/notext/24.webp)
For å få tilgang til ytterligere innstillinger, klikk på innstillingsikonet.
![IVPN](assets/notext/25.webp)
I "*Konto*" fanen, vil du finne innstillinger relatert til kontoen din.
![IVPN](assets/notext/26.webp)
I "*Generelt*" fanen, er det flere klientinnstillinger. Jeg råder deg til å sjekke "*Start ved innlogging*" og "*Ved oppstart*" alternativene i "*Autoconnect*" seksjonen for å automatisk etablere tilkoblingen med VPN ved oppstart av maskinen din.
![IVPN](assets/notext/27.webp)
I "*Tilkobling*" fanen, vil du finne ulike alternativer relatert til tilkoblingen. Dette er hvor du kan endre VPN-protokollen som brukes.
![IVPN](assets/notext/28.webp)Fanen "*IVPN Firewall*" lar deg aktivere brannmuren systematisk ved oppstart av datamaskinen, for å sikre at ingen tilkoblinger etableres utenfor VPN.
![IVPN](assets/notext/29.webp)
Fanen "*Split Tunnel*" tilbyr muligheten til å ekskludere visse programmer fra VPN-tilkoblingen. Applikasjoner lagt til her vil fortsette å operere med en normal internettforbindelse selv når VPN er aktivert.
![IVPN](assets/notext/30.webp)
I fanen "*WiFi-kontroll*" har du muligheten til å konfigurere spesifikke handlinger i henhold til nettverkene du er koblet til. For eksempel kan du betegne ditt hjemmenettverk som "*Pålitelig*" og konfigurere VPN til ikke å aktivere på dette nettverket, men til å automatisk aktivere på ethvert annet WiFi-nettverk.
![IVPN](assets/notext/31.webp)
I menyen "*AntiTracker*" velger du blokkeringsprofilen for din anti-tracker. Dette er designet for å blokkere annonser, skadelig programvare og datasporende ved å blokkere forespørsler til sporingstjenester mens du surfer på internett. Dette forbedrer ditt personvern ved å forhindre at selskaper samler inn og selger dine nettleserdata. En "*Hardcore-modus*" er også tilgjengelig for å fullstendig blokkere alle domener eid av Google og Meta, samt alle avhengige tjenester.
![IVPN](assets/notext/32.webp)
Og der har du det, du er nå utstyrt for å fullt ut nyte IVPN. Hvis du også ønsker å forbedre sikkerheten til dine online-kontoer ved å bruke en lokal passordbehandler, inviterer jeg deg til å sjekke ut vår veiledning på KeePass, en gratis og åpen kildekode-løsning:

https://planb.network/tutorials/others/general/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Hvis du er interessert i å oppdage en annen VPN-leverandør som ligner på IVPN, både når det gjelder funksjoner og prising, anbefaler jeg også å sjekke ut vår veiledning på Mullvad:

https://planb.network/tutorials/others/general/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8