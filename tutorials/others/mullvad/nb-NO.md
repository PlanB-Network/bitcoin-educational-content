---
name: Mullvad VPN
description: Oppsett av en VPN betalt med bitcoins
---
![cover](assets/cover.webp)

En VPN ("*Virtual Private Network*") er en tjeneste som etablerer en sikker og kryptert forbindelse mellom telefonen eller datamaskinen din og en ekstern server administrert av en VPN-leverandør.

Teknisk sett, når du kobler til en VPN, blir internett-trafikken din omdirigert gjennom en kryptert tunnel til VPN-serveren. Denne prosessen gjør det vanskelig for tredjeparter, som internettleverandører (ISPs) eller ondsinnede aktører, å avlytte eller lese dataene dine. VPN-serveren fungerer deretter som en mellommann som kobler deg til tjenesten du ønsker å bruke på dine vegne. Den tildeler en ny IP-adresse til tilkoblingen din, noe som bidrar til å skjule din virkelige IP-adresse fra nettstedene du besøker. Imidlertid, i motsetning til hva noen online annonser kan antyde, tillater ikke bruk av VPN deg å surfe på internett anonymt, ettersom det krever et tillitsnivå til VPN-leverandøren som kan se all trafikken din.
![MULLVAD VPN](assets/fr/01.webp)
Fordelene med å bruke en VPN er mange. For det første bevarer det personvernet til din online aktivitet fra ISPs eller regjeringer, forutsatt at VPN-leverandøren ikke deler informasjonen din. For det andre sikrer det dataene dine, spesielt når du er koblet til offentlige Wi-Fi-nettverk, som er sårbare for MITM ("**man-in-the-middle**") angrep. For det tredje, ved å skjule IP-adressen din, tillater en VPN deg å omgå geografiske restriksjoner og sensur, for å få tilgang til innhold som ellers ville vært utilgjengelig eller blokkert i din region.

Som du kan se, flytter VPN risikoen for trafikkobservasjon til VPN-leverandøren. Derfor, når du velger din VPN-leverandør, er det viktig å vurdere personopplysningene som kreves for registrering. Hvis leverandøren ber om informasjon som telefonnummeret ditt, e-postadresse, bankkortdetaljer, eller verre, din postadresse, øker risikoen for å assosiere din identitet med trafikken din. I tilfelle et kompromiss av leverandøren eller en juridisk beslagleggelse, ville det være enkelt å assosiere trafikken din med dine personopplysninger. Derfor anbefales det å velge en leverandør som ikke krever noen personopplysninger og aksepterer anonyme betalinger, som med bitcoins.

I denne veiledningen vil jeg presentere en enkel, effektiv, rimelig priset VPN-løsning som ikke krever noen personopplysninger for bruk.

## Introduksjon til Mullvad VPN
Mullvad VPN er en svensk tjeneste som skiller seg ut for sitt engasjement for brukerens personvern. I motsetning til mainstream VPN-leverandører, krever Mullvad ingen personopplysninger ved registrering. Det er ikke nødvendig å oppgi en e-postadresse, telefonnummer eller navn; i stedet tildeler Mullvad deg et anonymt kontonummer som brukes for betaling og tilgang til tjenesten. I tillegg hevder Mullvad at de ikke beholder noen aktivitetslogger som passerer gjennom serverne deres.
![MULLVAD VPN](assets/notext/02.webp)
For betaling er det ikke nødvendigvis påkrevd å oppgi kredittkortinformasjon, ettersom Mullvad aksepterer bitcoin-betalinger (kun onchain på deres offisielle nettsted, men det finnes en uoffisiell metode for å betale via Lightning). De aksepterer også kontantbetalinger gjennom posten.

Mullvad VPN skiller seg også ut gjennom sin transparens og sikkerhet. Deres programvare er åpen kildekode, og de gjennomgår regelmessig uavhengige sikkerhetsrevisjoner for å vurdere sine applikasjoner og infrastruktur, hvis resultater er [publisert på deres nettside](https://mullvad.net/fr/blog/tag/audits). Selskapet bak Mullvad er basert i Sverige, et land kjent for sine strenge personvernlover. De bruker utelukkende selvhostede servere, og eliminerer dermed risikoene forbundet med å bruke tredjeparts skytjenester, som hyperskalere AWS, Google Cloud, eller Microsoft Azure.
Når det gjelder funksjoner, tilbyr Mullvad alt man forventer fra en god VPN-klient, inkludert en nødstopp som beskytter trafikken din hvis VPN-en kobles fra, et alternativ for å deaktivere VPN for spesifikke applikasjoner, og muligheten til å rute trafikken din gjennom flere VPN-servere.
Naturligvis kommer denne kvaliteten på tjenesten til en pris, men en rettferdig pris er ofte en indikator på kvalitet og ærlighet. Det kan signalisere at selskapet har en forretningsmodell uten behov for å selge dine personlige data til tredjeparter. Mullvad VPN tilbyr en fast pris på 5 euro per måned, brukbar på opptil 5 forskjellige enheter.
![MULLVAD VPN](assets/notext/03.webp)
I motsetning til mainstream VPN-leverandører, har Mullvad en modell for kjøp av tilgangstid til tjenesten i stedet for et tilbakevendende, automatisk abonnement. Du gjør ganske enkelt en engangsbetaling i bitcoins for den valgte varigheten. For eksempel, hvis du kjøper ett års tilgang, kan du bruke tjenesten for den perioden, hvorpå du må returnere til Mullvads nettsted for å fornye tilgangstiden din.
Sammenlignet med IVPN, en annen høykvalitets VPN-leverandør, er Mullvad litt mer økonomisk. For eksempel, selv når man velger et treårs kjøp med IVPN, beløper den månedlige kostnaden seg til omtrent €5.40. IVPN tilbyr imidlertid noen ekstra tjenester og har også en billigere plan enn Mullvads (Standardplanen), men denne er begrenset til kun 2 enheter og ekskluderer "multi-hop"-protokollen.
Jeg gjennomførte også noen uformelle hastighetstester for å sammenligne IVPN og Mullvad. Selv om IVPN viste en liten overlegenhet i form av ytelse, var hastighetene hos Mullvad fortsatt veldig tilfredsstillende. Sammenlignet med mainstream VPN-leverandører, viste IVPN og Mullvad seg å være minst like effektive, om ikke overlegne i noen tilfeller.

## Hvordan installere Mullvad VPN på en datamaskin?

Besøk [den offisielle Mullvad-nettsiden](https://mullvad.net/en/download/) og klikk på "*Nedlastinger*" menyen.
![MULLVAD VPN](assets/notext/04.webp)
For Windows- eller macOS-brukere, last ned programvaren direkte fra nettstedet og følg instruksjonene gitt av installasjonsveiviseren for å fullføre installasjonen.
![MULLVAD VPN](assets/notext/05.webp)
For Linux-brukere, kan du finne instruksjonene spesifikke for din distribusjon i ["*Linux*"](https://mullvad.net/en/download/vpn/linux)-seksjonen.
![MULLVAD VPN](assets/notext/06.webp)
Når installasjonen er fullført, må du angi din konto-ID. Vi vil se hvordan man skaffer dette i de følgende seksjonene av denne veiledningen.

## Hvordan installere Mullvad VPN på en smarttelefon?

Last ned Mullvad VPN fra appbutikken din, enten det er [AppStore](https://apps.apple.com/us/app/mullvad-vpn/id1488466513) for iOS-brukere, [Google Play Store](https://play.google.com/store/apps/details?id=net.mullvad.mullvadvpn) for Android, eller [F-Droid](https://f-droid.org/packages/net.mullvad.mullvadvpn/). Hvis du bruker Android, har du også muligheten til å laste ned `.apk`-filen direkte fra [Mullvad-nettstedet](https://mullvad.net/en/download/vpn/android).
![MULLVAD VPN](assets/notext/07.webp)
Ved første bruk av appen, vil du bli logget ut. Du må angi din konto-ID for å aktivere tjenesten.
![MULLVAD VPN](assets/notext/08.webp)Nå, la oss gå videre til å aktivere Mullvad på enhetene dine.

## Hvordan betale for og aktivere Mullvad VPN?

Gå til [den offisielle Mullvad-nettsiden](https://mullvad.net/) og klikk på "*Kom i gang*" knappen.
![MULLVAD VPN](assets/notext/09.webp)
Klikk på "*Generer kontonummer*" knappen.
![MULLVAD VPN](assets/notext/10.webp)Mullvad vil da opprette kontoen din. Du trenger ikke å oppgi noen personlige opplysninger. Det er kun kontonummeret ditt som vil tillate deg å logge inn. Det fungerer noe som en tilgangsnøkkel. Lagre det på et sikkert sted som din passordbehandler, for eksempel. Du kan også lage en papirkopi.
![MULLVAD VPN](assets/notext/11.webp)
Deretter klikker du på "*Legg til tid på kontoen din*" knappen.
![MULLVAD VPN](assets/notext/12.webp)
Du vil da komme til innloggingssiden for kontoen din. Skriv inn kontonummeret ditt og klikk deretter på "*Logg inn*" knappen.
![MULLVAD VPN](assets/notext/13.webp)
Velg betalingsmetode. Jeg anbefaler å betale med bitcoins, da du vil dra nytte av en 10% rabatt, som reduserer kostnaden til €4,50 per måned. Hvis du foretrekker å betale via Lightning, vil jeg gi en alternativ metode i den følgende delen.
![MULLVAD VPN](assets/notext/14.webp)
Klikk på "*Opprett en engangs betalingsadresse*" knappen.
![MULLVAD VPN](assets/notext/15.webp)
Betal deretter med din Bitcoin-lommebok det angitte beløpet til mottaksadressen som er gitt deg.
![MULLVAD VPN](assets/notext/16.webp)
Det kan ta noen minutter før nettstedet oppdager betalingen din, når transaksjonen er bekreftet. Når betalingen er oppdaget av Mullvad, vil varigheten av abonnementet ditt vises øverst til venstre på siden, i stedet for påskriften "*Ingen tid igjen*".
![MULLVAD VPN](assets/notext/17.webp)
Du kan deretter skrive inn kontonummeret ditt på programvaren for å aktivere VPN-en.
![MULLVAD VPN](assets/notext/18.webp)
For å aktivere VPN på mobilapplikasjonen din, er prosessen nøyaktig den samme. Du trenger bare å skrive inn kontonummeret ditt.
![MULLVAD VPN](assets/notext/19.webp)
## Hvordan betale for Mullvad VPN med Lightning?

Som du har forstått, aksepterer ikke Mullvad ennå betalinger via Lightning Network. Imidlertid, takket være en anbefaling fra [Lounès](https://x.com/louneskmt), oppdaget jeg en uformell tjeneste som lar deg omgå denne begrensningen. Denne tjenesten, tilgjengelig på [vpn.sovereign.engineering](https://vpn.sovereign.engineering/), aksepterer dine betalinger på Lightning og gir deg i retur en gyldig plan for Mullvad.
![MULLVAD VPN](assets/notext/20.webp)
Du har 2 forskjellige alternativer på dette nettstedet: du kan stole på nettstedets leder og skrive inn kontonummeret ditt direkte, deretter klikke på "*Logg inn*" for at ditt Mullvad-pakke automatisk skal valideres. Eller, du kan klikke på "*Heck yeah!*" knappen for å kjøpe en Voucher i Lightning, som du deretter kan bruke på den offisielle Mullvad-nettsiden for å få pakken din. ![MULLVAD VPN](assets/notext/21.webp) I begge tilfeller vil du deretter bli bedt om å velge varigheten på pakken din. Du kan velge mellom 6 måneder og 1 år. ![MULLVAD VPN](assets/notext/22.webp) Deretter klikker du på "*Fyll på med Lightning*" knappen. ![MULLVAD VPN](assets/notext/23.webp) For å fullføre kjøpet, betal fakturaen med din Lightning-lommebok. ![MULLVAD VPN](assets/notext/24.webp) Hvis du valgte å kjøpe en Voucher, på Mullvad-nettsiden, velg "*Voucher*" blant betalingsmetodene tilgjengelig på kontoen din. Deretter, skriv inn Voucher-nummeret du mottok fra vpn.sovereign.engineering-nettstedet i det angitte feltet. ![MULLVAD VPN](assets/notext/25.webp) ## Hvordan bruke og konfigurere Mullvad VPN?
Nå som du har en aktiv konto og har skrevet inn kontonummeret ditt i Mullvad-programvaren eller appen, kan du fullt ut nyte tjenestene til din VPN. ![MULLVAD VPN](assets/notext/26.webp) For å koble fra VPN-en, klikk ganske enkelt på "*Koble fra*" knappen. ![MULLVAD VPN](assets/notext/27.webp) Den lille røde pilen ved siden av "*Koble fra*" knappen lar deg bytte servere uten å endre gjeldende plassering. ![MULLVAD VPN](assets/notext/28.webp) Hvis du ønsker å bytte byer for din VPN-server, klikk på "*Bytt plassering*" for å velge en ny lokasjon. ![MULLVAD VPN](assets/notext/29.webp) Øverst på skjermen vil du se enhetens kallenavn samt den gjenværende varigheten av pakken din. ![MULLVAD VPN](assets/notext/30.webp) Ved å klikke på ikonet av den lille mannen, vil du få tilgang til detaljert informasjon om kontoen din. ![MULLVAD VPN](assets/notext/31.webp) For å få tilgang til innstillinger, klikk på tannhjulet. ![MULLVAD VPN](assets/notext/32.webp) I menyen "*Brukergrensesnittinnstillinger*", kan du tilpasse innstillingene for programvaren din, inkludert grensespråket og oppførselen på systemet ditt. ![MULLVAD VPN](assets/notext/33.webp) I menyen "*VPN-innstillinger*", vil du finne alternativer relatert til din VPN. Jeg anbefaler å aktivere "*Start app ved oppstart*" og "*Auto-koble til*" alternativene slik at din VPN-tilkobling automatisk starter når maskinen din starter.
![MULLVAD VPN](assets/notext/34.webp) I undermenyen "*DNS-innholdsblockere*", har du muligheten til å filtrere og blokkere DNS-forespørsler til skadelige, reklame, eller uønskede nettsteder.
![MULLVAD VPN](assets/notext/35.webp)
Til slutt, menyen "*Split tunneling*" lar deg velge spesifikke applikasjoner på maskinen din for hvilke internett-trafikk ikke vil bli rutet gjennom VPN-en.
![MULLVAD VPN](assets/notext/36.webp)
For å få en oversikt over din Mullvad-konto og administrere de forskjellige tilkoblede enhetene, kan du klikke på "*Enheter*" menyen på nettsiden.
![MULLVAD VPN](assets/notext/37.webp)Og der har du det, du er nå utstyrt til å fullt ut nyte Mullvad VPN. Hvis du er interessert i å oppdage en annen VPN-leverandør som ligner på Mullvad, både når det gjelder funksjoner og prising, anbefaler jeg også å sjekke ut vår veiledning om IVPN:

https://planb.network/tutorials/others/general/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68