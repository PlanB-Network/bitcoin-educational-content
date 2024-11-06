---
name: RoninDojo

description: Installere og bruke din RoninDojo Bitcoin-node.
---
***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, er visse funksjoner i RoninDojo, som Whirlpool, ikke lenger operative. Det er imidlertid mulig at disse verktøyene kan bli gjeninnført eller relansert på en annen måte i de kommende ukene. I tillegg, siden RoninDojo-koden var hostet på Samourais GitLab, som også ble beslaglagt, er det for øyeblikket ikke mulig å laste ned koden eksternt. RoninDojo-teamene jobber sannsynligvis med å publisere koden på nytt.*

_Vi følger nøye med på utviklingen i denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen så snart ny informasjon blir tilgjengelig._

_Denne opplæringen er gitt kun for utdannings- og informasjonsformål. Vi støtter eller oppfordrer ikke til bruk av disse verktøyene til kriminelle formål. Det er brukerens ansvar å overholde lovene i sin jurisdiksjon._

_Denne opplæringen er dedikert til installasjonen av RoninDojo v1. For å dra nytte av de siste forbedringene og funksjonene, anbefaler jeg sterkt å konsultere vår opplæring dedikert til direkte installasjon av RoninDojo v2 på din Raspberry Pi:_ [https://planb.network/tutorials/node/ronin-dojo-v2](https://planb.network/tutorials/node/ronin-dojo-v2)

---

Å kjøre og bruke din egen node er essensielt for å virkelig delta i Bitcoin-nettverket. Selv om det å kjøre en Bitcoin-node ikke gir noen økonomiske fordeler for brukeren, lar det dem bevare sin personvern, handle uavhengig og ha kontroll over sin tillit til nettverket.

I denne artikkelen vil vi ta en detaljert titt på RoninDojo, en flott løsning for å kjøre din egen Bitcoin-node.

### Innholdsfortegnelse:

- Hva er RoninDojo?
- Hvilket maskinvare å velge?
- Hvordan installere RoninDojo?
- Hvordan bruke RoninDojo?
- Konklusjon

Hvis du ikke er kjent med hvordan en Bitcoin-node fungerer og dens rolle, anbefaler jeg å starte med å lese denne artikkelen: The Bitcoin Node - Del 1/2: Tekniske Konsepter.

![Samourai](assets/1.webp)

## Hva er RoninDojo?

Dojo er en fullverdig Bitcoin-node-server utviklet av Samourai Wallet-teamet. Du kan fritt installere den på hvilken som helst maskin.

RoninDojo er en installasjonsassistent og administrasjonsverktøy for Dojo og ulike andre verktøy. RoninDojo tar den opprinnelige implementasjonen av Dojo og legger til mange andre verktøy i den, samtidig som installasjon og administrasjon blir enklere.

De tilbyr også en "plug-and-play" maskinvare, RoninDojo Tanto, med RoninDojo forhåndsinstallert på en maskin sammensatt av deres team. Tanto er en betalt løsning, egnet for de som ikke ønsker å få hendene skitne.

Koden for RoninDojo er åpen kildekode, så det er også mulig å installere denne løsningen på din egen maskinvare. Dette alternativet er kostnadseffektivt, men krever litt mer manipulasjon, noe som er det vi vil gjøre i denne artikkelen.

RoninDojo er en Dojo, så det tillater enkel integrasjon av Whirlpool CLI i din Bitcoin-node for å ha den best mulige CoinJoin-opplevelsen. Med Whirlpool CLI kan du ikke bare la dine bitcoins remixe 24/7 uten å måtte holde din personlige datamaskin på, men du kan også sterkt forbedre ditt personvern.
RoninDojo integrerer mange andre verktøy som er avhengige av din Dojo, som Boltzmann-kalkulatoren, som bestemmer personvernnivået til en transaksjon, Electrum-serveren for å koble dine forskjellige Bitcoin-lommebøker til din node, eller Mempool-serveren for å privat observere dine transaksjoner. Sammenlignet med en annen node-løsning som Umbrel, som jeg presenterte for deg i denne artikkelen, er RoninDojo dypt fokusert på "On Chain"-løsninger og verktøy som optimaliserer brukerens personvern. Derfor tillater ikke RoninDojo interaksjon med Lightning Network.
RoninDojo tilbyr færre verktøy sammenlignet med Umbrel, men de få essensielle funksjonene for en Bitcoiner tilstede på Ronin er utrolig stabile.

Så hvis du ikke trenger alle funksjonene til en Umbrel-server og bare ønsker en enkel og stabil node med noen få essensielle verktøy som Whirlpool eller Mempool, så er RoninDojo sannsynligvis en god løsning for deg.

Etter min mening er Umbrels utviklingsfokus tungt på Lightning Network og allsidige verktøy. Det er fortsatt en Bitcoin-node, men målet er å gjøre den til en multitasking mini-server. I kontrast er RoninDojos utviklingsfokus mer i tråd med teamene hos Samourai Wallet og fokuserer på de essensielle verktøyene for en Bitcoiner, som tillater full uavhengighet og optimalisert håndtering av personvern på Bitcoin.

Vær oppmerksom på at oppsettet av en RoninDojo-node er litt mer komplekst enn en Umbrel-node.

Nå som vi har klart å male et bilde av RoninDojo, la oss se på hvordan vi setter opp denne noden sammen.

## Hvilket maskinvare å velge?

For å velge maskinen som huser og kjører RoninDojo, har du flere alternativer.

Som forklart tidligere, er det enkleste valget å bestille Tanto, en plug-and-play-maskin designet spesifikt for dette formålet. For å bestille din, gå hit: [link](https://shop.ronindojo.io/product-category/nodes/).

Siden RoninDojo-teamene produserer åpen kildekode, er det også mulig å implementere RoninDojo på andre maskiner. Du kan finne de nyeste versjonene av installasjonsveiviseren på denne siden: [link](https://ronindojo.io/en/downloads.html), og de nyeste versjonene av koden på denne siden: [link](https://code.samourai.io/ronindojo/RoninDojo).

Personlig installerte jeg den på en Raspberry Pi 4 8GB og alt fungerer perfekt.

Vær imidlertid oppmerksom på at RoninDojo-teamene indikerer at det ofte er problemer med kassen og SSD-adapteren. Det anbefales derfor ikke å bruke et kabinett med en kabel for din maskins SSD. I stedet er det å foretrekke å bruke et lagringsutvidelseskort spesifikt designet for hovedkortet ditt, som dette: Raspberry Pi 4 Storage Expansion Card.

Her er et eksempel på hvordan du setter opp din egen RoninDojo-node:

- En Raspberry Pi 4.
- Et kabinett med en vifte.
- Et kompatibelt lagringsutvidelseskort.
- En strømkabel.
- Et industrielt micro SD-kort på 16GB eller mer.
- En SSD på 1TB eller større.
- En RJ45 Ethernet-kabel, kategori 8 anbefales.

## Hvordan installere RoninDojo?

### Steg 1: Forbered det oppstartbare micro SD-kortet.

Når du har montert maskinen din, kan du begynne installasjonen av RoninDojo. For å gjøre dette, start med å lage et oppstartbart micro SD-kort ved å brenne det passende diskbildet på det.

Sett inn micro SD-kortet ditt i din personlige datamaskin, og gå deretter til den offisielle RoninDojo-nettsiden for å laste ned RoninOS-diskbildet: https://ronindojo.io/en/downloads.html.
Last ned diskbildet som tilsvarer maskinvaren din. I mitt tilfelle lastet jeg ned "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ" bildet:
![Last ned RoninOS diskbilde](assets/2.webp)

Når bildet er lastet ned, verifiser integriteten ved å bruke den tilsvarende .SHA256-filen. Jeg vil beskrive i detalj hvordan du gjør dette i denne artikkelen: Hvordan verifisere integriteten til Bitcoin-programvare på Windows?

Spesifikke instruksjoner for å verifisere integriteten til RoninOS er også tilgjengelig på denne siden: https://wiki.ronindojo.io/en/extras/verify.

For å brenne dette bildet på ditt micro SD-kort, kan du bruke programvare som Balena Etcher, som du kan laste ned her: https://www.balena.io/etcher/.

For å gjøre dette, velg bildet i Etcher og flash det på micro SD-kortet:

![Brenn diskbilde med Etcher](assets/3.webp)

Når operasjonen er fullført, kan du sette inn det oppstartbare micro SD-kortet i Raspberry Pi og slå på maskinen.

### Steg 2: Konfigurer RoninOS.

RoninOS er operativsystemet til din RoninDojo-node. Det er en modifisert versjon av Manjaro, en Linux-distribusjon. Etter at du har startet maskinen og ventet noen minutter, kan du begynne konfigurasjonen.

For å fjernkoble til den, må du finne IP-adressen til din RoninDojo-maskin. For å gjøre dette, kan du for eksempel koble til administrasjonspanelet til din internettboks, eller du kan også laste ned programvare som https://angryip.org/ for å skanne ditt lokale nettverk og finne maskinens IP.

Når du har funnet IP-en, kan du ta kontroll over maskinen din fra en annen datamaskin koblet til samme lokale nettverk ved hjelp av SSH.

Fra en datamaskin som kjører macOS eller Linux, åpne terminalen. Fra en datamaskin som kjører Windows, kan du bruke et spesialisert verktøy som Putty eller direkte bruke Windows PowerShell.

Når terminalen er åpen, skriv følgende kommando:

> ssh root@192.168.?.?

Erstatt bare de to spørsmålstegnene med IP-en til din tidligere funnet RoninDojo.
Tips: I en Shell, høyreklikk for å lime inn et element.

Deretter vil du ankomme Manjaro-kontrollpanelet. Velg riktig tastaturoppsett ved å bruke pilene for å endre målet i rullegardinlisten.

![Manjaro Tastaturoppsett Konfigurasjon](assets/4.webp)

Velg et brukernavn og passord for økten din. Bruk et sterkt passord og lag en sikker sikkerhetskopi. Du kan eventuelt bruke et svakt passord under installasjonen, og senere enkelt endre det ved å "kopiere-lime" det inn i RoninUI. Dette vil tillate deg å bruke et veldig sterkt passord uten å bruke for mye tid på å manuelt skrive det under oppsettet av Manjaro.

![Manjaro Brukernavn Konfigurasjon](assets/5.webp)

Deretter vil du også bli bedt om å velge et root-passord. For root-passordet, skriv inn et sterkt passord direkte. Du vil ikke kunne endre det fra RoninUI. Husk også å sikkerhetskopiere dette root-passordet sikkert.

Deretter skriv inn din lokasjon og tidssone.

![Manjaro Tidssone Konfigurasjon](assets/6.webp)

![Manjaro Lokasjon Konfigurasjon](assets/7.webp)

Deretter velger du et vertsnavn.

![Manjaro Vertsnavn Konfigurasjon](assets/8.webp)

Til slutt, verifiser Manjaro-konfigurasjonsinformasjonen og bekreft.

![Verifisering av ManjaroOS Konfigurasjonsinformasjon](assets/9.webp)

### Steg 3: Last ned RoninDojo.
Den første konfigurasjonen av RoninOS vil bli gjennomført. Når dette er ferdig, som vist i skjermbildet over, vil maskinen starte på nytt. Vent noen øyeblikk, og skriv deretter inn følgende kommando for å koble deg til din RoninDojo-maskin på nytt:
> ssh brukernavn@192.168.?.?

Erstatt bare "brukernavn" med brukernavnet du tidligere valgte, og erstatt spørsmålstegnene med IP-adressen til din RoninDojo.

Skriv deretter inn ditt brukerpassord.

I terminalen vil det se slik ut:

![SSH-tilkobling til RoninOS](assets/10.webp)

Du er nå koblet til maskinen din, som for øyeblikket kun har RoninOS. Nå må du installere RoninDojo på den.

Last ned den nyeste versjonen av RoninDojo ved å skrive inn følgende kommando:

> git clone https://code.samourai.io/ronindojo/RoninDojo

Nedlastingen vil være rask. I terminalen vil du se dette:

![Kloning av RoninDojo](assets/11.webp)

Vent til nedlastingen er ferdig, og installer deretter og få tilgang til RoninDojo brukergrensesnittet ved å bruke følgende kommando:

> ~/RoninDojo/ronin

Du vil bli bedt om å skrive inn ditt brukerpassord:

![Bitcoin Node Passordverifisering](assets/12.webp)

Denne kommandoen er bare nødvendig første gang du får tilgang til din RoninDojo. Etterpå, for å få tilgang til RoninCLI via SSH, trenger du bare å skrive inn kommandoen [SSH brukernavn@192.168.?.?] ved å erstatte "brukernavn" med ditt brukernavn og skrive inn IP-adressen til noden din. Du vil bli bedt om ditt brukerpassord.

Deretter vil du se denne fantastiske animasjonen:

![RoninCLI oppstartsanimasjon](assets/13.webp)

Deretter vil du endelig ankomme RoninDojo CLI brukergrensesnittet.

### Steg 4: Installer RoninDojo.

Fra hovedmenyen, naviger til "System"-menyen ved hjelp av piltastene på tastaturet. Trykk enter-tasten for å bekrefte ditt valg.

![RoninCLI navigasjonsmeny til System](assets/14.webp)

Gå deretter til "System Setup & Install"-menyen.

![RoninCLI navigasjonsmeny til RoninDojo systeminstallasjon](assets/15.webp)

Til slutt, merk av for "System Setup" og "Install RoninDojo" ved hjelp av mellomromstasten, og velg "Accept" for å starte installasjonen.

![RoninDojo installasjonsbekreftelse](assets/16.webp)

La installasjonen gå sin gang i ro og mak. I mitt tilfelle tok det omtrent 2 timer. Hold terminalen åpen under prosessen.

Sjekk terminalen din av og til, da du vil bli bedt om å trykke på en tast ved visse stadier av installasjonen, som her for eksempel:

![RoninDojo installasjon pågår](assets/17.webp)

Ved slutten av installasjonen vil du se de forskjellige containerne starte:

![Node container oppstart](assets/18.webp)

Deretter vil noden din starte på nytt. Koble deg til RoninCLI igjen for neste steg.

![Bitcoin node omstart](assets/19.webp)

### Steg 5: Last ned proof-of-work-kjeden og få tilgang til RoninUI.

Når installasjonen er fullført, vil noden din begynne å laste ned Bitcoin proof-of-work-kjeden. Dette kalles Initial Block Download (IBD). Det tar vanligvis mellom 2 og 14 dager avhengig av internettforbindelsen og enheten din.

Du kan spore fremdriften til kjedenedlastingen ved å få tilgang til RoninUI webgrensesnittet.

For å få tilgang til det fra et lokalt nettverk, skriv følgende i adressefeltet til nettleseren din:

- Enten skriv direkte inn IP-adressen til maskinen din (192.168.?.?)

- Eller skriv inn: ronindojo.local
Husk å deaktivere VPN-en din hvis du bruker en.
### Mulig vri

Hvis du ikke klarer å koble til RoninUI fra nettleseren din, sjekk at applikasjonen fungerer som den skal fra Terminalen din koblet til noden din via SSH. Koble til hovedmenyen ved å følge de tidligere trinnene:

- Skriv: SSH brukernavn@192.168.?.? og erstatt med dine legitimasjoner.

- Skriv inn ditt brukerpassord.

Når du er i hovedmenyen, gå til:

> RoninUI > Restart

Hvis applikasjonen starter på nytt korrekt, er det et problem med tilkoblingen fra nettleseren din. Sjekk at du ikke bruker en VPN og sørg for at du er koblet til samme nettverk som noden din.

Hvis omstarten produserer en feil, prøv å oppdatere operativsystemet og deretter reinstallere RoninUI. For å oppdatere OS:

> System > Programvareoppdateringer > Oppdater Operativsystem

Når oppdateringen og omstarten er fullført, koble til noden din via SSH og installer RoninUI på nytt:

> RoninUI > Installer på nytt

Etter å ha lastet ned RoninUI på nytt, prøv å koble til RoninUI gjennom nettleseren din.

> Tips: Hvis du ved et uhell avslutter RoninCLI og finner deg selv på Manjaro-terminalen, skriv inn kommandoen "ronin" for å gå direkte tilbake til hovedmenyen til RoninCLI.

### Web innlogging

Du kan også logge inn på RoninUI-webgrensesnittet fra hvilket som helst nettverk ved å bruke Tor. For å gjøre dette, hent Tor-adressen til din RoninUI fra RoninCLI:

> Legitimasjoner > Ronin UI

Hent Tor-adressen som slutter på .onion og logg deretter inn på Ronin UI ved å skrive inn denne adressen i din Tor-nettleser. Vær forsiktig så du ikke lekker dine ulike legitimasjoner, da de er sensitiv informasjon.

![RoninUI web login interface](assets/20.webp)

Når du er logget inn, vil du bli bedt om ditt brukerpassord. Det er det samme passordet du bruker for å logge inn via SSH.

![RoninUI web interface management panel](assets/21.webp)

Vi kan se fremgangen av IBD (Initial Block Download) her. Vær tålmodig, du henter alle transaksjonene som er gjort på Bitcoin siden 3. januar 2009.

Etter å ha lastet ned hele blokkjeden, vil indeksereren komprimere databasen. Denne operasjonen tar omtrent 12 timer. Du kan også følge fremgangen under "Indexer" på RoninUI.

Din RoninDojo-node vil være fullt funksjonell etter dette:

![Indexer synchronized at 100% functional node](assets/22.webp)

Hvis du ønsker å endre brukerpassordet til et sterkere, kan du gjøre det nå fra "Innstillinger"-fanen. På RoninDojo er det ikke noe ekstra sikkerhetslag, så jeg anbefaler å velge et virkelig sterkt passord og ta vare på sikkerhetskopien av det.

## Hvordan bruke RoninDojo?

Når kjeden er lastet ned og komprimert, kan du begynne å nyte tjenestene som tilbys av din nye RoninDojo-node. La oss se hvordan vi bruker dem.

### Koble lommebokprogramvare til electrs.

Den første nytten av din nylig installerte og synkroniserte node vil være å kringkaste transaksjonene dine til Bitcoin-nettverket. Derfor vil du sannsynligvis ønske å koble dine ulike lommebokstyringsprogrammer til den.

Du kan gjøre dette ved å bruke Electrum Rust Server (electrs). Applikasjonen er normalt forhåndsinstallert på din RoninDojo-node. Hvis ikke, kan du manuelt installere den fra RoninCLI-grensesnittet.

Gå enkelt til:

> Applikasjoner > Administrer Applikasjoner > Installer Electrum Server

For å få Tor-adressen til din Electrum Server, fra RoninCLI-menyen, gå til:

> Legitimasjoner > Electrs
Du trenger bare å skrive inn .onion-lenken i programvaren din for lommebok. For eksempel, i Sparrow Wallet, gå til fanen:
> Fil > Innstillinger > Server

I servertypen, velg "Privat Electrum", deretter skriv inn Tor-adressen til din Electrum Server i det tilsvarende feltet. Til slutt, klikk på "Test forbindelse" for å teste og lagre din tilkobling.

![Sparrow Wallet tilkoblingsgrensesnitt til en electrs](assets/23.webp)

### Koble lommebokprogramvare til Samourai Dojo.

I stedet for å bruke Electrs, kan du også bruke Samourai Dojo for å koble din kompatible programvarelommebok til din RoninDojo-node. For eksempel tilbyr Samourai Wallet denne muligheten.

For å gjøre dette, skann ganske enkelt tilkoblings-QR-koden til din Dojo. For å få tilgang til den fra RoninUI, klikk på "Dashboard"-fanen og deretter på "Administrer"-knappen i boksen til din Dojo. Du vil da kunne se tilkoblings-QR-kodene for din Dojo og BTC-RPC Explorer. For å vise dem, klikk på "Vis verdier".

![Hente tilkoblings-QR-koden til Dojo](assets/24.webp)

For å koble din Samourai Wallet til din Dojo, må du skanne denne QR-koden under installasjonen av applikasjonen:

![Koble til Dojo fra Samourai Wallet-applikasjonen](assets/25.webp)

### Bruke din egen Mempool Explorer.

Et essensielt verktøy for Bitcoinere, utforskeren lar deg sjekke ulike informasjoner om Bitcoin-kjeden. Med Mempool, for eksempel, kan du i sanntid sjekke gebyrene som andre brukere anvender for å justere dine deretter. Du kan også sjekke bekreftelsesstatusen for en av dine transaksjoner eller se saldoen til en adresse.

Disse utforsker-verktøyene kan eksponere deg for personvernrisikoer og krever at du stoler på en tredjeparts database. Når du bruker dette online verktøyet uten å gå gjennom din egen node:

- Du risikerer å lekke informasjon om din lommebok.

- Du stoler på nettstedets administrator for proof-of-work-kjeden de hoster.

For å unngå disse risikoene, kan du bruke din egen Mempool-instans på din node via Tor-nettverket. Med denne løsningen, ikke bare bevarer du ditt personvern når du bruker tjenesten, men du trenger heller ikke å stole på en leverandør siden du spør din egen database.

For å gjøre dette, start med å installere Mempool Space Visualizer fra RoninCLI:

> Applikasjoner > Administrer Applikasjoner > Installer Mempool Space Visualizer

Når installert, hent lenken til din Mempool. Tor-adressen vil tillate deg å få tilgang til den fra hvilket som helst nettverk. På samme måte henter vi denne lenken via RoninCLI:

> Legitimasjon > Mempool

![Hente Tor Mempool-adresse](assets/26.webp)

Skriv ganske enkelt inn din Mempool Tor-adresse i Tor-nettleseren for å nyte din egen Mempool-instans, basert på dine egne data. Jeg anbefaler å legge til denne Tor-adressen i dine favoritter for raskere tilgang. Du kan også lage en snarvei på skrivebordet ditt.

![Mempool Space grensesnitt](assets/27.webp)

Hvis du ikke har Tor-nettleseren ennå, kan du laste den ned her: https://www.torproject.org/download/

Du kan også få tilgang til den fra din smarttelefon ved å installere Tor Browser og skrive inn samme adresse. Fra hvor som helst, kan du se tilstanden til Bitcoin-kjeden ved å bruke din egen node.

### Bruke Whirlpool CLI.

Din RoninDojo-node inkluderer også WhirlpoolCLI, et fjernkommandolinjegrensesnitt for å automatisere Whirlpool-mikser.
Når du utfører en CoinJoin med Whirlpool-implementeringen, må applikasjonen du bruker forbli åpen for å utføre mikser og remikser. Denne prosessen kan være kjedelig for brukere som ønsker å ha høye anon-sett, ettersom enheten som hoster applikasjonen med Whirlpool må være konstant på. I praktiske termer betyr dette at hvis du ønsker å engasjere dine UTXOer i 24/7 remikser, må du holde din personlige datamaskin eller telefon konstant på med applikasjonen åpen.
En løsning på denne begrensningen er å bruke WhirlpoolCLI på en maskin som er ment å være konstant på, som en Bitcoin-node. Med dette kan våre UTXOer bli remixet 24/7 uten behov for å holde en annen maskin enn vår Bitcoin-node i gang.
WhirlpoolCLI brukes med WhirlpoolGUI, et grafisk grensesnitt som skal installeres på en personlig datamaskin for enkel håndtering av Coinjoins. Jeg vil forklare i detalj hvordan du setter opp Whirlpool CLI med ditt eget dojo i denne artikkelen: [lenke](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).

For å lære mer om Coinjoin generelt, forklarer jeg alt i denne artikkelen: [lenke](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).

### Bruke Whirlpool Stat-verktøyet.

Etter å ha utført CoinJoins med Whirlpool, kan du ønske å vite det faktiske personvernivået til dine miksete UTXOer. Whirlpool Stat-verktøyet lar deg enkelt gjøre dette. Med dette verktøyet kan du beregne den prospektive poengsummen og den retrospektive poengsummen til dine miksete UTXOer. For å lære mer om beregning av disse Anon-settene og hvordan de fungerer, anbefaler jeg å lese denne seksjonen: [lenke](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment).

Verktøyet er forhåndsinstallert på din RoninDojo. For øyeblikket er det kun tilgjengelig fra RoninCLI. For å starte det fra hovedmenyen, gå til:

> Samourai Toolkit > Whirlpool Stat-verktøyet

Instruksjonene for bruk vil vises. Når du er ferdig, trykk på en hvilken som helst tast for å få tilgang til kommandolinjene:

![Whirlpool Stats Tool software home](assets/28.webp)

Terminalen vil bli vist:

> wst#/tmp>

For å avslutte dette grensesnittet og returnere til RoninCLI-menyen, skriv inn kommandoen:

> quit

For å starte, vil vi sette proxyen på Tor for å trekke ut OXT-data med fullstendig personvern. Skriv inn kommandoen:

> socks5 127.0.0.1:9050

Deretter laster du ned dataene fra bassenget som inneholder transaksjonen din:

> download 0001
>
> Erstatt 0001 med bassengbetegnelseskoden som interesserer deg.

Betegnelseskodene er som følger på WST:

- Basseng 0.5 bitcoins: 05

- Basseng 0.05 bitcoins: 005

- Basseng 0.01 bitcoins: 001

- Basseng 0.001 bitcoins: 0001
![Nedlasting av data fra pool 0001 fra OXT](assets/29.webp)
Når dataene er lastet ned, last dem med kommandoen:

> load 0001
>
> Erstatt 0001 med koden for den poolen du er interessert i.

![Laster inn data fra pool 0001](assets/30.webp)
La innlastingsprosessen finne sted, det kan ta noen minutter. Etter at dataene er lastet inn, skriv inn kommandoen score etterfulgt av din TXID (transaksjonsidentifikator) for å få dens Anon Sets:

> score TXID
>
> Erstatt TXID med identifikatoren for transaksjonen din.

![Skriver ut de prospektive og retrospektive scorene for den gitte TXID](assets/31.webp)

WST vil deretter vise den retrospektive scoren (tilbakeblikkende metrikker) etterfulgt av den prospektive scoren (fremtidsrettede metrikker). I tillegg til scorene for Anon Sets, gir WST deg også diffusjonsraten for din output i poolen basert på anon settet.

Vær oppmerksom på at den prospektive scoren for din UTXO beregnes basert på TXID-en for din første miks, ikke din siste miks. Omvendt beregnes den retrospektive scoren for en UTXO basert på TXID-en for den siste syklusen.

Hvis du ikke forstår disse konseptene med Anon Sets, anbefaler jeg å lese denne delen av artikkelen min om Coinjoin hvor jeg forklarer alt i detalj med diagrammer: [https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)

### Bruke Boltzmann-kalkulatoren.

Boltzmann-kalkulatoren er et verktøy som lar deg enkelt beregne ulike avanserte metrikker på en Bitcoin-transaksjon, inkludert dens entropinivå. Alle disse dataene vil tillate deg å kvantifisere nivået av personvern for en transaksjon og oppdage eventuelle potensielle feil. Dette verktøyet er forhåndsinstallert på din RoninDojo-node.

For å få tilgang til det fra RoninCLI, koble til via SSH, og gå deretter til menyen:

> Samourai Toolkit > Boltzmann Calculator

Før jeg forklarer hvordan du bruker den på RoninDojo, vil jeg forklare hva disse metrikkene representerer, hvordan de beregnes, og hva de brukes til.

Disse indikatorene kan brukes for enhver Bitcoin-transaksjon, men de er spesielt interessante for å studere kvaliteten på en Coinjoin-transaksjon.

1. Den første indikatoren som beregnes av denne programvaren er antall mulige kombinasjoner. Det er notert på kalkulatoren som "nb combinations". Gitt verdiene av UTXOene, representerer denne indikatoren antall mulige kartlegginger fra innganger til utganger.

> Hvis du ikke er kjent med begrepet "UTXO", anbefaler jeg å lese denne korte artikkelen: Mekanismen til en Bitcoin-transaksjon: UTXO, innganger og utganger.

Med andre ord representerer denne indikatoren antall mulige tolkninger for en gitt transaksjon. For eksempel vil en Whirlpool 5x5 Coinjoin-struktur ha et antall mulige kombinasjoner lik 1496:

![Skjema av en Coinjoin-transaksjon på kycp.org](assets/32.webp)

Kreditt: KYCP
2. Den andre beregnede indikatoren er entropien til en transaksjon. Siden antallet mulige kombinasjoner kan være veldig høyt for en transaksjon, kan man velge å bruke entropi isteden. Entropi representerer den binære logaritmen til antallet mulige kombinasjoner. Formelen er som følger:
- E: entropien til transaksjonen.
- C: antall mulige kombinasjoner for transaksjonen.

> E = log2(C)

I matematikk er den binære logaritmen (base 2) den inverse funksjonen av potensen av 2-funksjonen. Med andre ord, den binære logaritmen til x er potensen som tallet 2 må heves til for å oppnå verdien x.

Således:

> E = log2(C)
> C = 2^E

Denne indikatoren uttrykkes i bits. For eksempel, her er beregningen av entropien til en Whirlpool 5x5 Coinjoin-transaksjon, med et tidligere nevnt antall mulige kombinasjoner lik 1496:

> C = 1496
>
> E = log2(1496)
>
> E = 10.5469 bits

Derfor har denne Coinjoin-transaksjonen en entropi på 10.5469 bits, noe som er veldig bra.

Jo høyere denne indikatoren er, desto flere forskjellige tolkninger av transaksjonen finnes det, og derfor er transaksjonen mer konfidensiell.

La oss ta et annet eksempel. Her er en "klassisk" transaksjon som har ett inngangspunkt og to utgangspunkter:

![Bitcoin transaksjonsskjema på oxt.me](assets/34.webp)

Kreditt: OXT

Denne transaksjonen har bare én mulig tolkning:

> [(inp 0) > (Outp 0 ; Outp 1)]

Så dens entropi vil være lik 0:

> C = 1
>
> E = log2(C)
>
> E = 0

3. Den tredje indikatoren som returneres av Boltzmann-kalkulatoren er effektiviteten til Tx kalt "Wallet Efficiency". Denne indikatoren lar oss sammenligne inngangstransaksjonen med den best mulige transaksjonen i samme konfigurasjon.

Vi vil nå introdusere konseptet med maksimal entropi, som representerer den høyeste oppnåelige entropien for en gitt transaksjonsstruktur. For eksempel vil en Whirlpool 5x5 Coinjoin-struktur ha en maksimal entropi på 10.5469. Effektivitetsindikatoren sammenligner denne maksimale entropien med den faktiske entropien til inngangstransaksjonen. Formelen er som følger:

- ER: Faktisk entropi uttrykt i bits.
- EM: Maksimal entropi med samme struktur uttrykt i bits.
- Ef: Effektivitet uttrykt i bits.

> Ef = ER - EM
>
> Ef = 10.5469 - 10.5469
>
> Ef = 0 bits

Denne indikatoren uttrykkes også som en prosentandel, så formelen blir:

- CR: Faktisk antall mulige kombinasjoner.
- CM: Maksimalt antall mulige kombinasjoner med samme struktur.
- Ef: Effektivitet uttrykt som en prosentandel.

> Ef = CR/CM
>
> Ef = 1496/1496
>
> Ef = 100%

En effektivitet på 100% betyr at denne transaksjonen har den høyest mulige personvernet i forhold til sin struktur.

4. Den fjerde beregnede indikatoren er entropitetthet. Den lar oss forholde entropien til hver inngang eller utgang. Denne indikatoren kan brukes til å sammenligne effektiviteten mellom transaksjoner av forskjellige størrelser.

Beregningen er veldig enkel: vi deler transaksjonens entropi med antall innganger og utganger som er til stede. For eksempel, for en Whirlpool 5x5 Coinjoin, ville vi ha:

    ED: Entropitetthet uttrykt i bits.
    E: Transaksjonens entropi uttrykt i bits.
    T: Totalt antall innganger og utganger i transaksjonen.

T = 5 + 5 = 10
ED = E / TED = 10.5469 / 10
ED = 1.054 bits

Det femte stykket informasjon som tilbys av Boltzmann-kalkulatoren er sannsynlighetstabellen for koblinger mellom innganger og utganger. Denne tabellen gir deg ganske enkelt sannsynligheten (Boltzmann-score) for at en gitt inngang tilsvarer en gitt utgang.

Hvis vi tar vårt eksempel med en Whirlpool Coinjoin, ville sannsynlighetstabellen se slik ut:

| %       | Utgang 0 | Utgang 1 | Utgang 2 | Utgang 3 | Utgang 4 |
|---------|----------|----------|----------|----------|----------|
| Inngang 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Inngang 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Inngang 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Inngang 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Inngang 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Her kan vi se at hver inngang har en lik sannsynlighet for å være koblet til hver utgang.

Men, hvis vi tar eksemplet med en transaksjon med én inngang og to utganger, ville det se slik ut:

| Inngang | Utgang 0 | Utgang 1 |
| ------- | -------- | -------- |
| 0       | 100%     | 100%     |

I dette eksemplet kan vi se at sannsynligheten for at hver utgang kommer fra inngang 0 er 100%.

Jo lavere denne sannsynligheten er, desto høyere er konfidensialitetsnivået.

6. Det sjette stykket informasjon som beregnes er antallet deterministiske koblinger. Forholdet mellom deterministiske koblinger vil også bli oppgitt. Denne indikatoren fremhever antallet koblinger mellom innganger og utganger i den gitte transaksjonen som har en sannsynlighet på 100%, noe som betyr at de er utvetydige.

Forholdet indikerer antallet deterministiske koblinger i transaksjonen sammenlignet med det totale antallet koblinger.

For eksempel har en Coinjoin Whirlpool-transaksjon ingen deterministiske koblinger mellom innganger og utganger. Indikatoren vil være null og forholdet vil også være 0%.

Men, for den andre transaksjonen som ble studert (1 inngang og 2 utganger), er indikatoren 2 og forholdet er 100%.

Derfor, hvis denne indikatoren er null, indikerer det god konfidensialitet.

Nå som vi har studert indikatorene, la oss se hvordan vi kan beregne dem ved hjelp av denne programvaren. Fra RoninCLI, gå til menyen:

> Samourai Toolkit > Boltzmann Calculator

![Boltzmann Calculator programvarens hjemmeside](assets/35.webp)

Når programvaren er lansert, skriv inn transaksjons-ID-en du ønsker å studere. Du kan skrive inn flere transaksjoner på en gang ved å skille dem med et komma, deretter trykke enter:

![Skriv inn en TXID for å studere på Boltzmann Calculator](assets/36.webp)

Kalkulatoren vil deretter returnere alle indikatorene vi har sett før:

![Utskrift av Boltzmann Calculator data for denne TXID](assets/37.webp)

Skriv kommandoen "Quit" for å avslutte programvaren og returnere til RoninCLI-menyen.

For å lære mer om Boltzmann-kalkulatoren, anbefaler jeg å lese disse artiklene:

- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159

- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
### Koble til Bisq.
Bisq er en peer-to-peer utvekslingsplattform som lar deg kjøpe og selge bitcoins. Den brukes med en skrivebordsprogramvare som kjører på Tor og lar deg utveksle bitcoins uten å måtte oppgi din identitet.
Bisq sikrer peer-to-peer utvekslinger gjennom et 2/2 multi-signatur system. Du kan bruke denne programvaren med din egen RoninDojo-node for å optimalisere personvernet for dine utvekslinger og stole på data fra din egen nodes blockchain.

For å laste ned Bisq-programvaren, gå til deres offisielle nettsted: https://bisq.network/

For å komme i gang med programvaren, anbefaler jeg å lese denne siden: https://bisq.network/getting-started/

For å hente tilkoblingslenken fra din RoninDojo, må du koble til RoninCLI via SSH. Gå deretter til menyen:

> Applikasjoner > Administrer Applikasjoner

Skriv inn passordet ditt, og merk av boksen med mellomromstasten:

> [ ] Aktiver Bisq-tilkobling

Bekreft valget ditt. La noden din installere, og hent deretter Tor V3-adressen fra:

> Legitimasjoner > Bitcoind

Kopier adressen under "Bitcoin Daemon".

Du kan også hente din Bitcoind Tor V3-adresse fra RoninUI-grensesnittet ved enkelt å klikke på "Administrer" i "Bitcoin Core"-boksen på "Dashboard":

![Hent TorV3 Bitcoin Daemon-adresse på RoninUI](assets/38.webp)

For å koble noden din fra Bisq, gå til menyen:

> Innstillinger > Nettverksinfo

![Tilgang til nodetilkoblingsgrensesnittet fra Bisq-programvaren](assets/39.webp)

Klikk på boblen "Bruk egendefinerte Bitcoin Core-noder". Skriv deretter inn din Bitcoin TorV3-adresse i den angitte boksen, med ".onion" men uten "http://".

![Boks for å angi TorV3-adressen til noden din i Bisq-programvaren](assets/40.webp)

Start Bisq-programvaren på nytt. Noden din er nå koblet til din Bisq.

### Andre funksjoner.

Din RoninDojo-node inkluderer også andre grunnleggende funksjoner. Du har muligheten til å skanne spesifikk informasjon for å sikre at den blir tatt hensyn til.

For eksempel er det noen ganger mulig at lommeboken din koblet til din RoninDojo ikke finner bitcoinsene som tilhører deg. Saldoen er 0 selv om du er sikker på at du har bitcoin i denne lommeboken. Det er mange mulige årsaker å vurdere, inkludert en feil i avledningsveiene, og blant dem er det også mulig at noden din ikke observerer adressene dine.

For å fikse dette, kan du sjekke at noden din sporer din xpub med "xpub-verktøyet". For å få tilgang til det fra RoninUI, gå til menyen:

> Vedlikehold > XPUB-verktøy

Skriv inn den problematiske xpub-en og klikk "Sjekk" for å verifisere denne informasjonen.

![XPUB-verktøy fra RoninUI](assets/41.webp)

Hvis din xpub blir sporet av noden, vil du se dette vises:

![XPUB-verktøy resultat som viser vellykket analyse](assets/42.webp)

Sjekk at alle transaksjoner vises korrekt. Verifiser også at avledningstypen stemmer overens med den i lommeboken din. Her kan vi se at noden tolker denne xpub-en som en BIP44-avledning. Hvis denne avledningstypen ikke stemmer overens med den i lommeboken din, klikk på "Skriv om" knappen, og velg deretter BIP44/BIP49/BIP84 etter ditt valg:

![Endre avledningstypen til den studerte xpub-en fra RoninUI](assets/43.webp)

Hvis din xpub ikke spores av noden din, vil du se denne skjermen som inviterer deg til å importere den:
![Importer en xpub med XPUB-verktøyet på RoninUI](assets/44.webp)
Du kan også bruke andre vedlikeholdsverktøy:

- Transaksjonsverktøy: Lar deg observere detaljene til en spesifikk transaksjon.
- Adresseverktøy: Lar deg verifisere at en spesifikk adresse blir sporet av din Dojo.
- Reskann Blokker: Tvinger noden din til å skanne et valgt område av blokker på nytt.

Du vil også finne "Push Tx"-verktøyet på RoninUI. Det lar deg kringkaste en signert transaksjon til Bitcoin-nettverket. Den må tastes inn i heksadesimalt format:

![Verktøy for å kringkaste en signert transaksjon fra RoninUI](assets/45.webp)

## Konklusjon.

Vi har sett hvordan man installerer og kommer i gang med dette fantastiske verktøyet som er RoninDojo. Det er et utmerket valg for å kjøre din egen Bitcoin-node. Det er en stabil løsning som integrerer og holder alle de essensielle verktøyene for en Bitcoiner oppdatert.

Hvis bruk av terminalen ikke skremmer deg og hvis du ikke trenger verktøy relatert til Lightning Network, så kan RoninDojo appellere til deg.

Hvis du kan, vurder å donere til utviklerne som fritt produserer denne åpen kildekode-programvaren for deg: https://donate.ronindojo.io/

For å lære mer om RoninDojo, anbefaler jeg å sjekke ut lenkene i mine eksterne ressurser nedenfor.

### Videre lesning:

- Forstå og bruke CoinJoin på Bitcoin.
- Hash-funksjoner - utdrag fra e-boken Bitcoin Démocratisé 1.
- Alt du trenger å vite om Bitcoin Passphrase.

### Eksterne ressurser:

- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/introducing-boltzmann-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/