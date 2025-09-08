---
name: Haleskala
description: Avansert opplæring i Tailscale
---
![cover](assets/cover.webp)



## 1. Innledning



Tailscale er neste generasjons VPN som oppretter et kryptert mesh-nettverk mellom enhetene dine. Det lar deg koble til eksterne maskiner som om de var på samme lokale nettverk, uten kompleks konfigurasjon eller portåpning.



Ved selvhosting tildeler Tailscale hver enhet en fast privat IP i et virtuelt nettverk, noe som gir stabil tilgang til tjenestene dine selv når din offentlige IP endres. Dette betyr at du kan administrere serverne dine eksternt, uten å eksponere tjenestene dine direkte mot Internett.



**Hovedapplikasjoner:**




- Administrer en personlig server fra utsiden
- Håndtere Umbrel/Lightning-noder raskere enn Tor
- Sikker tilgang til en Raspberry Pi eller NAS
- Koble til tjenestene dine via SSH eller HTTP uten komplisert nettverkskonfigurasjon



Denne enkle tilnærmingen gjør det mulig for selv-hostere å få tilgang til tjenestene sine på en sikker måte, uten å gå i fallgruvene til tradisjonelle VPN-er.



## 2. Slik fungerer Tailscale



I motsetning til tradisjonelle VPN-er, som ruter all trafikk gjennom en sentral server, skaper Tailscale et mesh-nettverk der enhetene kommuniserer direkte med hverandre. Den sentrale serveren håndterer bare autentisering og nøkkeldistribusjon, uten å se brukerdata.



![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)


*Figur 1: Tradisjonell VPN med hub-and-spoke-arkitektur der all trafikk går gjennom en sentral server*



Basert på WireGuard genererer hver enhet sine egne kryptografiske nøkler. Koordineringsserveren distribuerer de offentlige nøklene til nodene, som deretter etablerer ende-til-ende-krypterte tunneler direkte seg imellom. For å komme gjennom brannmurer bruker Tailscale NAT-traversering og, som en siste utvei, DERP-reléer som opprettholder kryptering.



![VPN maillé (mesh)](assets/fr/02.webp)


*Figur 2: Tailscale mesh-nettverk der enhetene kommuniserer direkte med hverandre*



All kommunikasjon er kryptert med WireGuard. Tailscale ser bare metadata (tilkoblinger), men aldri innholdet i utvekslingene. For større suverenitet gjør Headscale det mulig å hoste koordineringsserveren selv.



**Sikkerhet og konfidensialitet:** Takket være WireGuard er all kommunikasjon på Tailscale kryptert fra ende til ende. Tailscale kan ikke lese trafikken din - det er bare enhetene dine som har de nødvendige private nøklene. Tjenesten ser bare metadata: IP-adresser, enhetsnavn, tidsstempler for tilkoblinger og logger for peer-to-peer-tilkoblinger (uten innhold).



Denne arkitekturen er imidlertid avhengig av Tailscale Inc. for nettverkskoordinering. For å eliminere denne avhengigheten tilbyr Headscale et alternativ med åpen kildekode som lar deg selv være vert for kontrollserveren mens du bruker de offisielle Tailscale-klientene, noe som garanterer full suverenitet over nettverksinfrastrukturen din, på bekostning av en mer teknisk konfigurasjon.



**For en detaljert forklaring av hvordan Tailscale fungerer, inkludert kontrollplanadministrasjon, NAT-traversering og DERP-reléer, anbefaler vi den utmerkede artikkelen [How Tailscale Works] (https://tailscale.com/blog/how-tailscale-works) på den offisielle bloggen. Denne artikkelen forklarer i dybden de tekniske konseptene som gjør Tailscale så kraftig.



## 3. Installere Tailscale



Tailscale kjører på de **vanligste** operativsystemene (Windows, macOS, Linux, iOS, Android). Installasjonen sies å være "rask og enkel" på alle plattformer. La oss begynne med å ta en titt på Interface og hvordan du oppretter en konto, og deretter gå videre til installasjonsprosedyrene for ulike miljøer.



### 3.1 Opprettelse av Tailscale-konto



Gå til [https://tailscale.com/](https://tailscale.com/) og klikk på knappen "Kom i gang" øverst til høyre på siden.




![Page d'accueil Tailscale](assets/fr/03.webp)


*Tailscales hjemmeside forklarer konseptet og tilbyr en gratis start*



For å bruke Tailscale må du først opprette en konto via en identitetsleverandør:



![Page de connexion Tailscale](assets/fr/04.webp)


*Valg av identitetsleverandør for tilkobling til Tailscale (Google, Microsoft, GitHub, Apple osv.)*



Etter at du har logget inn, vil Tailscale be deg om litt informasjon om hva du skal bruke den til:



![Questionnaire d'utilisation](assets/fr/05.webp)


*Skjema for å bedre forstå ditt brukstilfelle (privat eller profesjonelt)*



Når du har opprettet kontoen din, kan du installere Tailscale på enhetene dine:



![Ajout du premier appareil](assets/fr/07.webp)


*Med Tailscale kan du installere applikasjonen på forskjellige systemer*



### 3.2 Installasjon på ulike plattformer





- På Windows og macOS:** Last ned den grafiske applikasjonen fra Tailscales offisielle nettsted og installer den (.msi-fil på Windows, .dmg-fil på Mac). Når applikasjonen er installert, starter den en grafisk Interface som lar deg koble deg til Tailscale-kontoen din (via en nettleser) for å autentisere maskinen.



![Connexion d'un appareil macOS](assets/fr/08.webp)


*Koble en MacBook til hekkenettet*



![Connexion réussie](assets/fr/09.webp)


*Bekreftelse på at enheten er koblet til Tailscale*-nettverket





- På Linux (Debian, Ubuntu osv.):** Du har flere alternativer. Den enkleste metoden er å kjøre det offisielle installasjonsskriptet: for eksempel på Debian/Ubuntu:



```bash
curl -fsSL https://tailscale.com/install.sh | sh
```



Dette skriptet vil legge til det offisielle Tailscale-depotet og installere pakken. Du kan også [manuelt legge til APT-repository] (https://pkgs.tailscale.com) eller bruke vanlige Snap- eller apt-pakker. Når den er installert, vil daemon `tailscaled` kjøre i bakgrunnen. Du må deretter **autentisere noden** (se Interface CLI vs web nedenfor). På andre distribusjoner (Fedora, Arch...) er pakken også tilgjengelig via standard repositories eller det universelle installasjonsskriptet. For en hodeløs server, bruk CLI: for eksempel `sudo tailscale up --auth-key <key>` hvis du bruker en forhåndsgenerert autentiseringsnøkkel, eller bare `tailscale up` for en interaktiv innlogging (som vil gi en URL du kan besøke for å autentisere enheten).





- På ARM-baserte systemer (Raspberry Pi osv.):** Vi bruker vanligvis Linux, så samme fremgangsmåte som ovenfor (skript eller pakke). Merk at Tailscale støtter ARM32/ARM64-arkitektur uten problemer. Mange brukere installerer Tailscale på Raspberry Pi OS via apt eller på lettvektsdistribusjoner (DietPi, etc.) for å få tilgang til sin Pi overalt.





- På iOS og Android:** Tailscale tilbyr **offisielle** mobilapplikasjoner. Bare installer *Tailscale* fra [App Store] (https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) eller [Play Store] (https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).



![Installation sur iPhone](assets/fr/11.webp)


*Fremgangsmåte for å installere Tailscale på iPhone: velkomst, personvern, varsler, VPN*



![Connexion sur iPhone](assets/fr/12.webp)


*Koble til tailnet, velg konto og valider på iPhone*



Når appen er installert, vil den ved første lansering be deg om å autentisere deg via den valgte leverandøren (Google, Apple ID, Microsoft osv., avhengig av hva du bruker for Tailscale) - det er samme prosedyre som på andre plattformer, vanligvis en omdirigering til en OAuth-nettside. Deretter oppretter mobilappen VPN-et (på iOS må du godta VPN-konfigurasjonstillegget). Appen kan deretter kjøre i bakgrunnen, slik at du får tilgang til tailnet fra hvor som helst. *Merk:* på mobil kan du bare ha **ett aktivt VPN om gangen** - så sørg for at du ikke har et annet VPN tilkoblet samtidig, ellers vil ikke Tailscale kunne opprette sitt eget. På Android kan du sette opp en separat arbeidsprofil hvis du ønsker å isolere visse bruksområder (f.eks. en profil med Tailscale aktiv for en gitt app).



### 3.3 Legge til flere enheter og validering



Når den første enheten er tilkoblet, ber Tailscale deg om å legge til andre enheter i nettverket:



![Ajout d'appareils supplémentaires](assets/fr/10.webp)


*Interface viser den første enheten som er tilkoblet og venter på andre enheter*



Når du har lagt til flere enheter, kan du kontrollere at de kan kommunisere med hverandre:



![Test de connectivité entre appareils](assets/fr/13.webp)


*Bekreftelse på at enhetene kan kommunisere med hverandre via ping*



Tailscale foreslår deretter ytterligere konfigurasjoner for å forbedre opplevelsen din:



![Suggestions de configuration](assets/fr/14.webp)


*Forslag til hvordan du konfigurerer DNS, deler enheter og administrerer tilgang*



### 3.4 Administrasjonspanel



Med nettadministrasjonskonsollen kan du se og administrere alle tilkoblede enheter:



![Tableau de bord des machines](assets/fr/15.webp)


*Liste over tilkoblede enheter med deres egenskaper og status*



**Interface Web vs Interface CLI:** Tailscale tilbyr to komplementære måter å samhandle med nettverket på: **Interface webadministrasjon** og **kommandolinjeklienten (CLI)**.





- Interface Web (Admin Console)**: Denne nettkonsollen er tilgjengelig på [https://login.tailscale.com](https://login.tailscale.com), og er det sentrale dashbordet for Tailscale-nettverket ditt. Den viser alle enheter (*Maskiner*), deres online/offline-status, deres Tailscale IP-adresser og mer. Her kan du **administrere enheter** (gi nytt navn, utløpe nøkler, autorisere ruter, deaktivere en node), **administrere brukere** (i en organisatorisk kontekst) og definere sikkerhetsregler (ACL-er). Det er også her du konfigurerer globale alternativer som MagicDNS, tagger eller autentiseringsnøkler (autentiseringsnøkler fra før generate for automatisk tillegg av enheter). Interface web er veldig nyttig for å få en oversikt og gjøre endringer som skal forplantes via koordineringsserveren til alle noder. *Eksempel:* Aktivering av en **subnettrute** eller en **exit-node** gjøres med ett enkelt klikk i konsollen, så snart den aktuelle noden har kunngjort seg selv som en slik.





- Interface kommandolinje (CLI):** Kommandoen `tailscale` er tilgjengelig i CLI på alle enheter der Tailscale er installert. Med CLI kan du gjøre alt lokalt: koble til (`tailscale up`), inspisere status (`tailscale status` for å se hvilke peers som er tilkoblet), feilsøke (`tailscale ping <ip>`), og så videre. Noen funksjoner er til og med **eksklusive for CLI** eller mer avanserte, for eksempel:





  - `tailscale up --advertise-routes=192.168.0.0/24` for å annonsere en subnettrute,
  - `tailscale up --advertise-exit-node` for å foreslå maskinen din som en exit-node,
  - `tailscale set --accept-routes=true` (eller `--exit-node=<IP>`) for å bruke en rute eller en exit-node,
  - `tailscale ip -4` for å vise enhetens Tailscale IP,
  - `tailcale lock/unlock` (hvis du bruker *tailnet-lock*, avansert sikkerhetsfunksjon),
  - eller `tailscale file send <node>` for å bruke **Taildrop** (filoverføring mellom enheter).


CLI er svært nyttig på servere uten Interface-grafikk, og for skripting av visse handlinger. **Forskjeller i bruk:** De fleste grunnleggende konfigurasjoner kan gjøres enten via nettet eller via CLI. For eksempel kan du legge til en enhet enten ved å spørre via konsollen, eller ved å kjøre `tailscale up` på enheten og validere via nettet. På samme måte kan du gi nytt navn til en enhet via konsollen eller med `tailscale set --hostname`. **Oppsummert** er nettkonsollen ideell for global nettverksadministrasjon (spesielt med flere maskiner/brukere), mens CLI er praktisk for finkornet kontroll over en gitt maskin, automatiseringsskript eller bruk på et system uten et GUI.



## 4. Bruke Tailscale på Umbrel



Umbrel er en populær plattform for selvhosting (særlig brukt for Bitcoin/Lightning-noder og andre selvhostede tjenester, via App Store). For å installere og konfigurere Umbrel, anbefaler vi at du følger vår dedikerte veiledning:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Det er spesielt interessant å bruke Umbrel og Tailscale sammen, ettersom Umbrel integrerer en Tailscale-modul som er enkel å ta i bruk. Her kan du se hvordan Tailscale integreres med Umbrel og hva det gir:



### 4.1 Installasjon og konfigurasjon av Umbrel





- Installere Tailscale på Umbrel:** Umbrel har en offisiell Tailscale-applikasjon i sin App Store. Installasjonen kunne ikke vært enklere:



![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)


*Tailscale-applikasjonssiden i Umbrel App Store*



Fra Interface Web Umbrel åpner du App Store, søker etter **Tailscale** og klikker på *Install*. Noen sekunder senere er applikasjonen installert på Umbrel. Når du åpner den, viser Umbrel en side der du kan koble noden din til Tailscale.



![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)


*Tilkoblingsskjerm for haleskala i Umbrels Interface*



Bare **klikk på "Logg inn"**, som vil omdirigere deg til Tailscale-godkjenningssiden:



![Page d'authentification Tailscale](assets/fr/18.webp)


*Koble til Tailscale via en identitetsleverandør*



Du kan autentisere deg via Tailscale-kontoen din (Google/GitHub/etc.) eller oppgi e-postadressen din. På Umbrel ber Interface deg vanligvis om å gå til [https://login.tailscale.com](https://login.tailscale.com) og logge inn - dette autentiserer Umbrel Tailscale-appen.



![Confirmation de connexion réussie](assets/fr/19.webp)


*Bekreftelse på at Umbrel-enheten er koblet til Tailscale-nettverket*



Når dette er gjort, er Umbrel "i" Tailscale-nettverket ditt og vises på konsollen med et navn (f.eks. *umbrel*). Du kan deretter klikke på IP Address for enhetene dine for å kopiere den, hente IPv6 Address eller MagicDNS som er knyttet til enheten din.



![Console Tailscale avec appareils connectés](assets/fr/20.webp)


*Tailscale-administrasjonskonsollen viser flere tilkoblede enheter, inkludert Umbrel*




### 4.2 Ekstern tilgang til Umbrel-tjenester



Når Umbrel er koblet til Tailscale, **har du tilgang til Interface Umbrel og applikasjonene som kjører på den, uansett hvor du befinner deg, som om du var på det lokale nettverket**. Dette er en av hovedfordelene i forhold til Tor.



Tilgang er bemerkelsesverdig enkelt: I stedet for å bruke `umbrel.local` (som bare fungerer på ditt lokale nettverk), bruker du Umbrels Tailscale IP Address (`http://100.x.y.z`) direkte fra en hvilken som helst enhet som er koblet til halenettet ditt. Dette fungerer uansett hvor du er eller hvilken internettforbindelse du bruker (4G, offentlig Wi-Fi, bedriftsnettverk).



**Eksempler på Umbrel-hostede applikasjoner som er tilgjengelige via Tailscale:**





- Interface hoved Umbrel**: Få tilgang til Umbrel-dashbordet ditt ved å skrive `http://100.x.y.z` i nettleseren din
- Bitcoin-node**: Administrer Bitcoin-noden uten ventetid, se synkronisering og statistikk
- Lightning Node**: Bruk ThunderHub, RTL eller andre Lightning-administrasjonsgrensesnitt med umiddelbar respons
- Mempool**: Vis Bitcoin-transaksjoner og Mempool uten Tor-forsinkelser
- noStrudel**: Få tilgang til Nostr-tjenestene dine på Umbrel



**Koble eksterne lommebøker til Bitcoin- eller Lightning-nodene dine via Tailscale:**



Tailscale gjør det også mulig for Bitcoin- og Lightning-lommebøker som er installert på andre enheter, å koble seg direkte til Umbrel-noden din:





- Sparrow wallet (Bitcoin)**: Denne eksterne Wallet Bitcoin kan kobles direkte til Umbrels Electrum-server ved hjelp av Tailscale IP Address:



![Configuration Electrum dans Sparrow](assets/fr/21.webp)


*Konfigurere en privat Electrum-server i Sparrow wallet ved hjelp av Umbrels Tailscale IP Address*



![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)


*Liste over Electrum-serveraliaser i Sparrow med Umbrel Tailscale IP Address*



Les vår komplette guide til konfigurering av Sparrow wallet med Bitcoin-noden:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d




- Zeus (Lyn)**: Denne Wallet mobile Lightning kan koble seg til Lightning-noden din på Umbrel. I stedet for å konfigurere endepunktet som `.onion', angir du bare Tailscale-IP-en til Umbrel og Lightning API-porten. Tilkoblingen vil være øyeblikkelig sammenlignet med Tor.



![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)


*Konfigurere Zeus til å koble til Lightning-noden via Tailscale* IP Address



For å konfigurere Zeus med Lightning-noden din, se vår detaljerte veiledning:



https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

For å finne ut mer om Lightning Network og hvordan den fungerer på Umbrel, besøk:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Fordeler i forhold til Tor



Umbrel tilbyr fjerntilgang via Tor (ved å tilby `.onion`-adresser for sine nettjenester). Selv om Tor har fordelen av konfidensialitet (anonymitet) og ikke krever registrering, synes mange brukere at **Tor er tregt og ustabilt** for daglig bruk (sider lastes sakte, tidsavbrudd osv.) - *"Umbrel via Tor er så tregt"*, klager noen.



Tailscale tilbyr en generelt **raskere tilkobling med lav latenstid**, ettersom trafikken går direkte (eller via et raskt relé) i stedet for å sprette gjennom tre Tor-noder. I tillegg gir Tailscale en "lokalt nettverk"-opplevelse: private IP-adresser brukes, og applikasjoner kan mappes direkte (f.eks. SMB-nettverksstasjon på \100.x.y.z).



Når det er sagt, har Tor fordelen av å være desentralisert og "out of the box" på Umbrel, mens Tailscale innebærer å stole på en tredjepart (eller hosting av headscale). Tor er også nyttig for klientløs tilgang (fra en hvilken som helst Tor-nettleser kan du konsultere Umbrel-brukergrensesnittet, mens Tailscale krever at klienten er installert på enheten du bruker).



**For å oppsummere**, for interaktiv bruk (lynlommebøker, hyppige webgrensesnitt), tilbyr Tailscale merkbar komfort og hastighet sammenlignet med Tor, til prisen av en liten ekstern avhengighet. Mange velger å bruke *begge*: Tailscale på daglig basis, og Tor som en reserve eller for å dele tilgang med noen uten å invitere dem inn i VPN-et sitt.



### 4.4 Sikkerhet



Ved å bruke Tailscale med Umbrel unngår du å eksponere Umbrel for Internett. Umbrel-noden er kun tilgjengelig for de andre autentiserte enhetene i halenettet, noe som reduserer angrepsflaten betraktelig (ingen port er åpen for fremmede, ingen risiko for angrep på webtjenesten via Internett).



Kommunikasjonen er kryptert (WireGuard) i tillegg til den krypteringen tjenestene dine allerede gjør (f.eks. er selv intern HTTP i tunnelen). Du kan fortsatt bruke Tailscale ACL-er for å for eksempel hindre at en bestemt tailnet-enhet får tilgang til Umbrel hvis du ønsker å dele opp nettverket. Umbrel selv ser ikke forskjellen - den tror at den serverer lokalt.



---

For å oppsummere denne delen, tar det bare noen få klikk å integrere Tailscale på Umbrel, og **forbedrer tilgjengeligheten** til din selv-hostede node betraktelig. Du vil kunne administrere Umbrel og dens tjenester fra hvor som helst, sikkert og effektivt, akkurat som om du var hjemme. Dette er en spesielt nyttig løsning for sanntidsapplikasjoner (Lightning) som lider av Tor-forsinkelse, eller mer generelt for alle selv-hostere som er ute etter en enkel privat tilkobling. Alt uten å eksponere en eneste port** på boksen din, og uten komplisert nettverkskonfigurasjon.



## 5. Avansert administrasjon og brukstilfeller



### 5.1 Avanserte funksjoner i Tailscale



**Administrasjonskonsollen (login.tailscale.com) lar deg administrere enhetene dine, vise tilkoblinger og konfigurere tilgangsregler.



**MagicDNS:** Oppløser automatisk enhetsnavn (f.eks. `raspberrypi.tailnet.ts.net`) for å unngå å huske IP-adresser.



**ACL og tilgangskontroll:** Definer nøyaktig hvem som har tilgang til hva i nettverket ditt via JSON-regler, noe som er ideelt for å isolere bestemte enheter eller begrense tilgangen til bestemte tjenester.



**Med enhetsdeling kan du invitere noen til å få tilgang til en bestemt maskin uten å gi dem tilgang til hele nettverket.



**En Tailscale-maskin kan fungere som en gateway for et helt undernett, noe som gir tilgang til ikke-Tailscale-enheter (IoT, skrivere osv.) via en enkelt konfigurert maskin.



**Exit Node:** Bruk en maskin som en gateway til Internett for å gå ut med sin IP. Nyttig for offentlig Wi-Fi eller for å omgå geografiske begrensninger.



**Taildrop:** Et sikkert alternativ til AirDrop, som lar deg overføre filer mellom Tailscale-enhetene dine, uansett plattform eller plassering. I motsetning til AirDrop, som er begrenset til Apples økosystem og fysisk nærhet, fungerer Taildrop mellom alle enhetene dine (Windows, Mac, Linux, Android, iOS), selv om de befinner seg i forskjellige land. Filer overføres direkte mellom enhetene med ende-til-ende-kryptering, uten å gå via en sentral server. Bruk kommandolinjen `tailscale file cp` eller det grafiske programmet Interface, avhengig av hvilket system du bruker.



### 5.2 Sammenligning med andre løsninger



**Tailscale er mye enklere å konfigurere (ingen porter å åpne, ingen sertifikatadministrasjon), men innebærer avhengighet av en tredjeparts tjeneste. OpenVPN er fullt kontrollerbart, men krever mer ekspertise.



**Som en direkte konkurrent opererer ZeroTier på Layer 2 (Ethernet), noe som muliggjør broadcast/multicast, mens Tailscale opererer på Layer 3 (IP). ZeroTier tilbyr større nettverksfleksibilitet, mens Tailscale favoriserer enkelhet i bruk.



**Tor tilbyr anonymitet som Tailscale ikke gjør, men er mye tregere. Tor er desentralisert og krever ingen konto, mens Tailscale er raskere og tilbyr en LAN-lignende opplevelse.



**Tailscale automatiserer all nøkkel- og tilkoblingsadministrasjon som WireGuard raw krever at du håndterer manuelt. Det er egentlig WireGuard + en forenklet administrasjon Layer.



Tailscale posisjonerer seg som en moderne, enkel løsning som er ideell for personlig bruk og små team. For purister som ønsker total kontroll, tilbyr Headscale et alternativ for selvhosting.



## 6. Konklusjon



**Tailscale-fordeler:** Tailscale tilbyr flere fordeler for selvhosting:





- Enkelhet og ytelse** - Rask installasjon på alle plattformer uten kompleks nettverkskonfigurasjon. Trafikken følger den mest direkte veien mellom maskinene dine (P2P mesh), med ytelsen til WireGuard-protokollen og ingen sentral server som begrenser gjennomstrømningen.
- Sikkerhet og fleksibilitet** - ende-til-ende-kryptering, redusert angrepsflate og avanserte funksjoner (ACL, SSO/MFA-autentisering). Fungerer selv bak NAT eller på farten, med subnett-rutere og exit-noder for å tilpasse nettverket til dine behov.



**Begrensninger:** Husk også på dette:





- Ekstern avhengighet** - I standardversjonen er tjenesten avhengig av infrastrukturen til Tailscale Inc. Denne avhengigheten kan omgås via Headscale (alternativ for selvhosting).
- Andre begrensninger** - Delvis lukket kildekode, begrensninger i gratisversjonen for visse avanserte bruksområder, ingen støtte for Layer 2 (broadcast/multicast), og behov for Internett-tilgang for å opprette forbindelser.



**Tailscale er ideell for individuelle selv-hostere og små team, utviklere som trenger tilgang til spredte ressurser, VPN-nybegynnere og mobile brukere. For bedrifter som krever total kontroll, kan andre løsninger som Headscale eller WireGuard direkte være å foretrekke.



**Utforsk Headscale for fullstendig selvhosting, API- og DevOps-integrasjoner (Terraform), eller alternativer som Innernet (lignende, men fullstendig selvhosting) og Netmaker.



Tailscale er et viktig verktøy for selvhosting, takket være sin enkelhet og effektivitet, og gjør den private infrastrukturen din like tilgjengelig som om den var i skyen, samtidig som du beholder kontrollen hjemme.



## 7. Nyttige ressurser



### Offisiell dokumentasjon





- Tailscale Dokumentasjonssenter**: [docs.tailscale.com](https://docs.tailscale.com) - Fullstendig engelsk dokumentasjon, installasjonsveiledninger, opplæringsprogrammer og tekniske referanser.
- Hvordan Tailscale fungerer**: [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works) - Detaljert artikkel som forklarer hvordan Tailscale fungerer.
- Changelog**: [tailscale.com/changelog](https://tailscale.com/changelog) - Sporing av oppdateringer og nye funksjoner.



### Praktiske veiledninger





- Homelab**-veiledninger: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Spesifikke veiledninger for selvhosting.
- Konfigurere en Exit Node**: [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Detaljert veiledning for konfigurering av exit-noder.
- Bruk Taildrop**: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Overfør filer mellom Tailscale-enheter.



### Sammenligninger





- Tailscale vs. andre løsninger**: [tailscale.com/compare](https://tailscale.com/compare) - Detaljerte sammenligninger med andre VPN- og nettverksløsninger (ZeroTier, OpenVPN, etc.).



### Fellesskapet





- Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Diskusjoner, spørsmål og tilbakemeldinger.
- GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Kundens kildekode, hvor du kan spore utviklingen og rapportere problemer.
- Discord**: [discord.gg/tailscale] (https://discord.gg/tailscale) - Fellesskap av brukere og utviklere.



Tailscale tilbyr jevnlig nytt innhold og nye funksjoner. Ta en titt på deres [offisielle blogg] (https://tailscale.com/blog/) for de siste nyhetene og casestudiene.