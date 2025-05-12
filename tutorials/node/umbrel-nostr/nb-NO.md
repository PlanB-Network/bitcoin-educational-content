---
name: Umbrel Nostr
description: Konfigurere og bruke Nostr-applikasjoner på Umbrel
---

![cover](assets/cover.webp)



## Forutsetninger: Installasjon av Umbrel



Umbrel er en plattform med åpen kildekode som gjør det enkelt å hoste Bitcoin-applikasjoner og andre tjenester på din egen personlige server. Det er en alt-i-ett-løsning som forenkler selvhosting av Bitcoin-noder og desentraliserte applikasjoner.



Sørg for at du har installert Umbrel ved å følge vår installasjonsveiledning:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Introduksjon til Nostr



**Nostr** er en åpen, desentralisert nettverksprotokoll utviklet for sosiale nettverk. Navnet står for _"Notes and Other Stuff Transmitted by Relays"_. Den gjør det mulig for hvem som helst å publisere meldinger (notater), som håndteres som JSON-hendelser, og spre dem via relay-servere i stedet for en sentralisert plattform. Hver bruker har et par kryptografiske nøkler (private/offentlige) som fungerer som en identifikator: Den offentlige nøkkelen (npub) identifiserer brukeren, og den private nøkkelen (nsec) gjør det mulig å signere meldinger. Takket være denne distribuerte arkitekturen er **Nostr motstandsdyktig mot sensur** og svært fleksibel: Du kan bruke flere klienter og koble deg til så mange reléer du vil, uten å være avhengig av én enkelt server.



Kort fortalt er Nostr en desentralisert kommunikasjonsprotokoll der **klienter** (brukerapplikasjoner) sender og mottar hendelser via **relayers** (servere). Denne protokollen har vært spesielt populær i Bitcoin-fellesskapet siden 2023, på grunn av dens desentraliserings- og datasuverenitetsverdier.



**For å bruke Nostr trenger du din private nøkkel (generert av en Nostr-klient eller via en dedikert utvidelse). **Del aldri din private nøkkel**, da det vil gjøre det mulig for andre å utgi seg for å være deg. Oppbevar den på et trygt sted og bruk sikre verktøy for nøkkeladministrasjon (se tips nedenfor).



## Paraplyapplikasjoner for Nostr



Umbrel tilbyr et økosystem av integrerte applikasjoner for å dra full nytte av Nostr på din personlige node. Vi skal beskrive bruken av de viktigste Nostr-relaterte appene: **Nostr Relay**, **noStrudel**, **Snort** og **Nostr Wallet Connect**. Hver av dem dekker et spesifikt behov: _Nostr Relay_ er en **privat relay-server**, _noStrudel_ og _Snort_ er **Nostr-klienter** (grensesnitt for å lese/publisere notater), mens _Nostr Wallet Connect_ er et verktøy for å koble din **Lightning-portefølje** til Nostr.



### Nostr Relay - ditt private relé på Umbrel



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** er Umbrels offisielle applikasjon for å kjøre ditt **eget Nostr-relé** på din node. Hovedmålet er å ha et **privat** og pålitelig relé for å **backup av all din Nostr**-aktivitet i sanntid. Med andre ord, ved å bruke dette personlige reléet i tillegg til de offentlige reléene, sikrer du at alle dine notater, meldinger og reaksjoner blir kopiert hjem, trygt fra sensur eller tap av data.



**Installasjon:** Installer _Nostr Relay_ fra Umbrel App Store (kategori _Social_). Når applikasjonen er lansert, kjører den i bakgrunnen (docker-tjeneste).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Du ser Interface-nettverket via Umbrel: Det inneholder grunnleggende informasjon og, fremfor alt, URL-en til reléet ditt (øverst til høyre), som du må kopiere for videre bruk. En synkroniseringsknapp (globusikon) er også tilgjengelig.



**For å dra nytte av Umbrel-reléet ditt :



**Legg til reléet i Nostr-klienten din:** I klientapplikasjonen din (f.eks. Damus på iOS, Amethyst på Android, Snort eller noStrudel på Umbrel osv.) legger du til URL-en til det private reléet som du kopierte tidligere. Som standard lytter Umbrel-reléet på port **4848**. Hvis du får tilgang til det på det lokale nettverket, gir dette en URL som: `ws://umbrel.local:4848` (eller bruk Umbrels lokale IP).



Hvis du bruker Tailscale (se nedenfor), kan du til og med bruke MagicDNS DNS-aliaset (vanligvis `umbrel` eller et autogenerert navn) for å få tilgang til det fra hvor som helst, alltid på port 4848.



Hvis du foretrekker Tor, kan du hente Umbrels .onion Address og bruke den med port 4848 via en Tor-kompatibel nettleser eller klient (se Tor-delen)



Når URL-en er lagt til i Nostr-klientens relékonfigurasjon, kobler du deg til dette reléet. Du bør se i klienten din at Umbrel-reléet er tilkoblet (vanligvis indikert med en Green-prikk eller lignende).



**Synkroniser historikk (valgfritt)**: I Interface-nettverket til _Nostr Relay_ på Umbrel klikker du på **globe** 🌐-ikonet (øverst på siden). Denne handlingen vil tvinge Umbrel-reléet ditt til å koble seg til de andre reléene dine (de som er konfigurert i klienten din) for å **importere dine gamle offentlige** aktiviteter. Dette betyr at tidligere notater du har publisert eller lest via offentlige reléer også vil bli lastet ned og lagret på ditt private relé. Vennligst vent på at synkroniseringen skal finne sted.



**Bruk Nostr som vanlig:** Fra nå av vil all ny aktivitet (publiserte notater, reaksjoner, krypterte private meldinger osv.) du utfører på Nostr bli videresendt som vanlig til de offentlige reléene **og parallelt til Umbrel-reléet ditt**. Hvis Nostr-klienten din er riktig konfigurert, vil den sende hver hendelse til alle reléene (inkludert ditt eget). Ditt private relé vil fungere som en sanntids backup. Selv i tilfelle en midlertidig frakobling vil kundene dine kunne resynkronisere manglende data senere takket være dette reléet. dette gir deg full kontroll over Nostr-dataene dine



I bakgrunnen er Umbrels _Nostr Relay_ basert på åpen kildekode-prosjektet **nostr-rs-relay** (Rust-protokollimplementering). Den støtter hele Nostr-protokollen og en rekke standard NIP-er (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33, osv.), noe som garanterer maksimal kompatibilitet med kundene.



### noStrudel - Nostr-klient for oppdagelsesreisende



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** er en brukerorientert Nostr-nettklient som er ideell for å forstå og utforske Nostr-nettverket i detalj. Det er en slags sandkasse for å inspisere hendelser og reléer, og for å eksperimentere med protokollens avanserte funksjoner. Interface er på engelsk og relativt teknisk, noe som gjør den ideell for erfarne brukere som er nysgjerrige på hvordan Nostr fungerer.



**Installasjon:** Installer _noStrudel_ fra Umbrel App Store (kategori _Social_). Når den er lansert, kan du få tilgang til den via nettleseren din på Umbrels Address (f.eks. `http://umbrel.local` eller via .onion/Tailscale, se avsnittet om ekstern tilgang).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Konfigurer releer:** Når du åpner noStrudel, ser du en "Setup Relays"-knapp øverst i høyre hjørne. Klikk på den for å konfigurere reléene dine.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



På denne siden limer du inn URL-adressen til Umbrel-reléet som du kopierte tidligere. Du kan også legge til andre reléer som er foreslått som standard av applikasjonen. Når du har konfigurert reléene dine, klikker du på "Sign in" nederst til venstre for å fortsette.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Tilkobling:** noStrudel tilbyr deg flere tilkoblingsalternativer. I vårt tilfelle velger vi "Private Key" og limer inn din tidligere genererte private Nostr-nøkkel. Hvis du ennå ikke har en nøkkel, kan du installere utvidelsen [Nostr Connect] (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) for å opprette og/eller lagre Nostr-nøklene dine og dermed kommunisere sikrere med de ulike Nostr-applikasjonene.



![Interface principale de noStrudel](assets/fr/07.webp)



Når du er tilkoblet, kan du bruke noStrudel til å dele notatene dine via Nostr. Interface gir deg tilgang til :





- Komplett Nostr-dashbord med tidslinje for notater, varsler, meldinger og profilsøk
- Reléhåndtering og tilkoblingsstatus
- Avanserte verktøy for å undersøke hendelser og JSON-innholdet i dem
- Konfigurasjonsalternativer for tidslinjefiltre og PIN-koder



**Tips:** På _noStrudel_ kan du sette opp _tidslinjefiltre_ eller teste forskjellige _NIP-er (Nostr Implementation Possibilities)_. Sjekk for eksempel støtte for NIP-05 (desentraliserte identifikatorer) eller nyere funksjoner. Dette gjør _noStrudel_ til et utmerket verktøy for eksperimentering i et kontrollert miljø.



### Snort - Moderne Nostr-kunde på Umbrel



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** er en annen Nostr-nettklient tilgjengelig på Umbrel, og tilbyr en moderne, rask og oversiktlig **Interface** for interaksjon med det desentraliserte sosiale nettverket. I motsetning til noStrudel, som retter seg mot avanserte brukere, tar _Snort_ sikte på enkel bruk uten å ofre funksjonalitet. Den er bygget i React, og tilbyr en ryddig UX som minner om klassiske sosiale nettverk, noe som gjør den egnet for hverdagsbruk.



**Installasjon:** Installer _Snort_ fra Umbrel App Store (kategori _Social_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Når du åpner Snort, ser du en "Register"-knapp nederst i venstre hjørne.



![Options de connexion dans Snort](assets/fr/10.webp)



Du kan velge å registrere deg eller koble deg til en eksisterende konto (som er det vi skal gjøre i denne veiledningen).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort tilbyr flere tilkoblingsmetoder. Du kan bruke den tidligere installerte Nostr Connect-utvidelsen eller andre tilgjengelige metoder. Når du er tilkoblet, kan du bruke programmet fullt ut.



Interface fra _Snort_ tilbyr :





- En **Posts/Conversations/Global**-skjerm for å navigere mellom notatene dine, diskusjonstrådene eller den globale feeden
- Faner for **Varsler**, **Meldinger** (DM), **Søk**, **Profil** osv.
- En **+**- eller _Write_-knapp for å publisere et nytt notat
- Administrasjon av **abonnementer (følgende)** og **lister**
- Meny for reléadministrasjon for å legge til/ta bort reléer og spore tilgjengeligheten deres



**Anbefalt relékonfigurasjon:** For å legge til Umbrel-reléet ditt, gå til Innstillinger - Reléer. Skriv inn URL-en til reléet ditt (`ws://umbrel:4848` eller en annen URL avhengig av konfigurasjonen din) i Snorts liste over reléer. På denne måten vil Snort publisere notatene dine på ditt private relé i tillegg til de offentlige.



### Nostr Wallet Connect - Koble din Lightning Wallet til Nostr



**Nostr Wallet Connect (NWC)** er en applikasjon som **kobler Umbrel (Lightning)**-noden din til kompatible Nostr-applikasjoner for å utføre Lightning-betalinger (for eksempel ved å sende _zaps_, disse mikrobetalingene for "liking" av innhold). I denne veiledningen skal vi se på hvordan du kobler noStrudel til Lightning-noden din for å utføre betalinger direkte fra Interface.



**Installasjon og konfigurasjon:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Installer _Nostr Wallet Connect_ fra Alby-butikken på Umbrel.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



I noStrudel klikker du på profilen din øverst i høyre hjørne, og deretter på "administrer"-knappen.



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Klikk på "Lightning" og deretter på "connect Wallet".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Velg "Umbrel" blant de tilgjengelige tilkoblingsalternativene.



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Klikk på "Connect" for å bli automatisk omdirigert til Umbrel Nostr Wallet Connect-økten din.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



På Nostr Wallet Connect-siden kan du :




   - Definer ditt maksimale budsjett
   - Valider autorisasjoner
   - Angi en utløpstid for tilkoblingen


Klikk på "koble til" for å fullføre.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Du blir omdirigert til noStrudel med en bekreftelsesmelding: Du kan nå zappe hele verden fra din Wallet/LND-node!



Takket være NWC starter dine **Lightning-betalinger via Nostr** (zaps til belønningsposter, _Value for Value_-betalinger osv.) fra **din egen node**. Du trenger ikke lenger å rute transaksjonene dine gjennom eksterne tjenester eller skanne en QR-kode fra telefonen hver gang. Brukeropplevelsen forbedres betraktelig, samtidig som den forblir _ikke-depotbasert_ og personvernvennlig.



Hvis du vil vite hvordan du setter opp din egen Lightning-node på Umbrel, anbefaler jeg at du tar en titt på denne andre omfattende veiledningen:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Avansert konfigurasjon og sikkerhet



Avansert bruk av Umbrel og Nostr sammen krever spesiell oppmerksomhet på **sikkerhet** og **tilkobling**. Her er noen tips om hvordan du kan beskytte konfigurasjonen din og få optimal tilgang til den, uansett hvor du befinner deg.



### Sikker ekstern tilgang: Tor og Tailscale



Av sikkerhetsgrunner er Umbrel som standard bare tilgjengelig på ditt lokale nettverk (og via Tor). For å samhandle med Nostr utenfor hjemmet har du to foretrukne løsninger: **Tor** (anonym tilgang via løk-nettverk) og **Tailscale** (privat VPN-nettverk).





- Tilgang via Tor:** Umbrel konfigurerer automatisk en **Tor-tjeneste (.onion)** for Interface-nett og -applikasjoner. Dette betyr at du kan få tilgang til Interface Umbrel (inkludert _noStrudel_ eller _Snort_) fra hvor som helst, ved hjelp av Tor-nettleseren, uten å eksponere din offentlige IP. _Tor brukes til å få tilgang til Umbrel-tjenestene dine utenfor ditt lokale nettverk, uten å eksponere enheten din for Internett ([Setup Tor on your system - Guides - Umbrel Community](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww))._ For å bruke dette alternativet, gå til Umbrel-innstillinger og hent Umbrels .onion URL (eller skann QR-koden som følger med). I en Tor-nettleser får du tilgang til denne .onion Address: du får den samme Interface som lokalt. Deretter kan du bruke Nostr-appene dine akkurat som hjemme.


**Nostr-relé via Tor:** Hvis du ønsker at Nostr-reléet ditt skal kunne nås via Tor av kundene dine (eller autoriserte venner), er dette mulig. Umbrel tilbyr ikke reléets .onion Address direkte, men siden det kjører på port 4848, kan du enten :





    - Bruk UI Umbrels .onion Address og konfigurer klienten din til å koble til via denne Interface (upraktisk for WebSocket),





    - Eller** eksponere port 4848 som en egen løktjeneste. Dette krever at du fikler med Tor-konfigurasjonen på Umbrel (forbeholdt avanserte brukere som er komfortable med SSH). Alternativt kan du vurdere en **Tor-tunnel** på en annen server som viderekobler til Umbrel: for personlig bruk er det imidlertid enklest å bruke Tailscale.





- Tilgang via Tailscale:** [Tailscale] (https://tailscale.com/) er en mesh VPN-løsning som skaper et virtuelt privat nettverk mellom enhetene dine og Umbrel. Fordelen: Det fungerer som om du var på et LAN, men over Internett, kryptert og uten komplisert konfigurasjon. **Tailscale tildeler din Umbrel en fast IP og et privat domenenavn, uavhengig av hvor den befinner seg i nettverket ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard))**. I praksis, når du har installert Tailscale på Umbrel (fra Umbrel App Store, kategori _Networking_) **og** på dine enheter (mobil, PC...), vil du kunne nå Umbrel via en Address som `100.x.y.z` (Tailscale IP) eller et navn som `umbrel.tailnet123.ts.net`.


for Nostr_ er Tailscale ekstremt nyttig: mobilen din, hvis den har Tailscale aktiv, vil kunne koble seg til `ws://umbrel:4848` (takket være MagicDNS) eller direkte til Tailscale IP og port 4848 for å bruke reléet. Klienter som Damus eller Amethyst vil se din Umbrel som om den var på det samme lokale nettverket. **Tips:** Aktiver **MagicDNS**-alternativet i Tailscale for å bruke vertsnavnet `umbrel` i stedet for å huske IP-en. Dette sikrer en problemfri tilkobling til reléet ditt selv når du er på farten ([Nostr Relay | Umbrel App Store] (https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Tailscale gir deg dessuten tilgang til Interface Umbrel (og dermed _noStrudel/Snort_-nettklientene) via en enkel nettleser, ved hjelp av den private IP-en eller det tildelte domenenavnet. Det er ikke behov for en Tor-nettleser, og dataoverføringshastighetene er generelt bedre enn via Tor-nettverket.




**Tor og Tailscale utelukker ikke hverandre. Du kan holde Tor aktiv for anonymisert tilgang eller spesifikke tjenester, og bruke Tailscale til daglig for enkelhetens skyld. I begge tilfeller trenger du ikke å åpne en port på ruteren din, noe som styrker sikkerheten.



### Sikring av Nostr-reléet (anbefalte fremgangsmåter)



Hvis du er vert for et Nostr-relé på Umbrel, spesielt i en avansert kontekst, må du sørge for å følge noen gode fremgangsmåter:





- Privat eller begrenset relé:** Som standard er Umbrel-reléet ditt privat (ikke offentlig kunngjort), og hvis du bare får tilgang til det via Tailscale eller ditt LAN, vil det forbli utilgjengelig for fremmede. **Hold lenken konfidensiell ** Ikke kringkast den på offentlige Nostr-nettverk med mindre du frivillig vil være vert for andre brukere, noe som er et helt annet problem (moderering, båndbredde osv.). For personlig bruk anbefaler vi å begrense tilgangen til deg selv og, om nødvendig, til noen få betrodde venner og familiemedlemmer.





- Hviteliste / Auth**: Nostr-rs-relay-implementeringen støtter en **NIP-42**-autentiseringsmekanisme samt _hvitlister_ med offentlige nøkler. Ved å aktivere disse alternativene kan du begrense reléet ditt slik at det **kun aksepterer hendelser signert av visse nøkler (dine)**, eller at klienter må autentisere seg for å publisere. å sette opp dette krever redigering av reléets konfigurasjonsfil `config.toml` i Umbrel (via SSH i Docker-containeren)._ Det er en avansert manipulasjon, men du kan for eksempel liste opp annonsene som er tillatt (`pubkey_whitelist`). På denne måten, selv om noen oppdager reléet ditt, vil de ikke kunne publisere noe der hvis de ikke er på listen.





- Oppdateringer og vedlikehold:** Hold Umbrel og _Nostr Relay_-appen oppdatert. Oppdateringer kan omfatte ytelsesforbedringer (f.eks. bedre håndtering av søppelpost) og sikkerhetsoppdateringer. På Umbrel sjekker du App Store regelmessig for oppdateringer til _Nostr Relay_, og bruker dem etter behov.





- Overvåking og begrensninger:** Hold et øye med hvordan reléet ditt brukes. Hvis du åpner det for andre, bør du holde et øye med belastningen (CPU/RAM-lagring) på Umbrel, ettersom et relé raskt kan samle opp mye data. nostr-rs-relay tilbyr konfigurerbare **hastighets- og lagringsgrenser** (`grenser` i konfigurasjonen, f.eks. antall hendelser per sekund, maks hendelsesstørrelse, rensing av gamle hendelser ...). For privat bruk trenger du sannsynligvis ikke å røre disse, men vær oppmerksom på at disse parameterne finnes hvis du trenger dem ([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- Sikring av Nostr-nøkler:** Dette punktet har allerede blitt nevnt, men det er avgjørende: Skriv aldri inn dine private Nostr-nøkler i en Interface du ikke stoler fullt ut på. Bruk i stedet nettleserutvidelser eller eksterne enheter (for eksempel Nostr _signers_ på separate telefoner) til å signere sensitive handlinger. På Umbrel kan nettklienter som _Snort_ og _noStrudel_ fungere uten å kjenne til den hemmelige nøkkelen din, via NIP-07. Benytt deg av denne muligheten til å kombinere komfort og sikkerhet.




Ved å følge disse tipsene vil integrasjonen av en Umbrel-node med Nostr være både kraftig **og** sikker. Du vil ha et komplett miljø: en Bitcoin-node for Lightning-betalinger, et privat Nostr-relé for datasuverenitet og høytytende Nostr-nettklienter for å navigere i dette nye desentraliserte sosiale nettverket. God fornøyelse med å utforske Nostr med Umbrel!