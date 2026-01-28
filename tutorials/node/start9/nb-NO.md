---
name: Start9

description: Veiledning om hvordan du setter opp en privat Start9-server

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Her er en videoveiledning fra Southern Bitcoiner, en videoguide som viser deg hvordan du setter opp og bruker en Start9 / StartOS personlig server, og hvordan du kjører en bitcoin-node.*


## 1️⃣ Innledning


### Hva er egentlig Start9?


Start9 er et selskap som ble grunnlagt i 2020, og som er mest kjent for å ha utviklet [**StartOS**,](https://github.com/Start9Labs/start-os) et Linux-basert operativsystem designet for personlige servere. Det gjør det mulig for brukere å enkelt selv hoste et bredt spekter av programvaretjenester - for eksempel Bitcoin- og Lightning-noder, meldingsapper eller passordadministratorer - samtidig som de opprettholder full kontroll over dataene sine og eliminerer avhengigheten av sentraliserte teknologiske plattformer. StartOS har et brukervennlig, nettleserbasert grensesnitt, en kuratert markedsplass for installasjon av tjenester og innebygde personvernverktøy som Tor-integrering og systemomfattende HTTPS-kryptering. Start9 tilbyr også maskinvareenheter som er forhåndsinstallert med operativsystemet, men programvaren kan også installeres på kompatibel maskinvare eller virtuelle maskiner (VM-er).


### Hvilke alternativer er tilgjengelige?


Start9 tilbyr både ferdigbygde og gjør-det-selv-alternativer. [**Server One**](https://store.start9.com/collections/servers/products/server-one) og [**Server Pure**](https://store.start9.com/collections/servers/products/server-pure) er offisielle maskinvareenheter med komponenter med høy ytelse: Server One bruker en **AMD Ryzen 7 5825U**-prosessor med konfigurerbar RAM (16 GB-64 GB) og lagringsplass (2 TB-4 TB NVMe SSD), mens Server Pure er utstyrt med en **Intel i7-10710U**, som også tilbyr konfigurerbare RAM- og lagringsalternativer. Begge inkluderer **teknisk support for livstid** når de kjøpes direkte fra Start9. For brukere som foretrekker fleksibilitet, kan StartOS installeres gratis på et bredt spekter av eksisterende maskinvare, inkludert bærbare datamaskiner, stasjonære datamaskiner, mini-PC-er og enkeltkortdatamaskiner, eller i VM-er.


![image](assets/en/01.webp)


### Hva er forskjellen fra Umbrel?


StartOS og Umbrel forenkler begge installasjonen av selvbetjente tjenester, men de skiller seg fra hverandre når det gjelder arkitektur og funksjoner. Umbrel fungerer som et applikasjonslag på Debian/Ubuntu-systemer eller VM-er, mens Start9 er et dedikert operativsystem som krever direkte maskinvare- eller VM-installasjon. Umbrel har et polert, macOS-inspirert grensesnitt, mens Start9 prioriterer et funksjonelt, minimalistisk design. Umbrel tilbyr et større [utvalg av applikasjoner](https://apps.umbrel.com/), mens [Start9 Marketplace](https://marketplace.start9.com/) kompenserer med avanserte tekniske muligheter. Start9 forenkler tilgangen til avanserte innstillinger gjennom validerte brukergrensesnittskjemaer, noe som reduserer behovet for kommandolinjeinteraksjon. Det utmerker seg også når det gjelder sikkerhetskopiering med kryptert systemsikkerhetskopiering med ett klikk, en funksjon som Umbrel mangler. StartOS har innebygde overvåkingsverktøy og håndhever HTTPS-kryptering for lokal nettverkstilgang, noe som øker sikkerheten. Umbrel bruker ukryptert HTTP lokalt, selv om begge plattformene støtter sikker ekstern tilgang via Tor. Umbrel passer for brukere som prioriterer et rikt app-økosystem og et polert brukergrensesnitt. Start9 er et godt valg for de som verdsetter sikkerhet, konfigurerbarhet, pålitelig sikkerhetskopiering og avansert tjenesteadministrasjon uten å måtte ha kommandolinjeekspertise. Hvis du vil lære mer om Umbrel og forskjellene fra Start9, kan du besøke dette kurset:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ DIY-forutsetninger: Minimum og anbefalte spesifikasjoner


For grunnleggende bruk med minimale tjenester er **minimumsspesifikasjonene**: **1 vCPU-kjerne (2,0 GHz + boost), 4 GB RAM, 64 GB lagringsplass** og en Ethernet-port. Når det er sagt, vil jeg anbefale å gå langt utover dette, spesielt hvis du kjører en Bitcoin Node. Selv startet jeg med 1 TB, men gikk raskt tom for plass. Du bør sikte deg inn på **mindst 2 TB lagringsplass**, sammen med en **firekjerners CPU (2,5 GHz+)** og **8 GB+ RAM**. Det gjør en enorm forskjell i ytelse og levetid. Hvis du vil dykke dypt, her er en oppdatert fellestråd om [Maskinvare som kan kjøre StartOS](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ Last ned og flashing av fastvaren


For å starte installasjonen, bruk en separat datamaskin til å gå til [Start9-nettstedet](https://start9.com/), og naviger til dokumentasjonsdelen ved å klikke på `DOCS`. Gå deretter til `Flashing Guides` for å finne den riktige versjonen av StartOS. To alternativer er tilgjengelige:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Denne veiledningen dekker alternativet `x86/ARM`.


Den nyeste OS-versjonen kan lastes ned fra [Github release page](https://github.com/Start9Labs/start-os/releases/latest). [Pre-release](https://github.com/Start9Labs/start-os/releases) versjoner er også tilgjengelige for brukere som ønsker å teste nye funksjoner. Nederst på siden, under `Assets`, kan du laste ned `x86_64` eller `x86_64-nonfree.iso`.  Image `x86_64-nonfree.iso` inneholder ikke-fri (lukket kildekode) programvare som kreves for Server One og de fleste DIY-maskinvarene, spesielt for støtte for grafikk og nettverksenheter.


Det anbefales å verifisere filens integritet ved å sjekke SHA256-hashverdien mot den som er oppført på GitHub. For Linux kan kommandoen `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso` brukes, mens andre operativsystemer er dekket i dokumentasjonen.


Etter at StartOS-imaget er lastet ned og verifisert, må det flashes over på en USB-stasjon. balenaEtcher er en anbefalt programvare for denne oppgaven. Det er et gratis verktøy med åpen kildekode for å skrive OS-bildefiler til USB-stasjoner og SD-kort, tilgjengelig for Windows, macOS og Linux. Last ned den aktuelle versjonen fra det offisielle [Balena Etcher-nettstedet](https://www.balena.io/etcher/) og kjør installasjonsprogrammet. Koble til USB-stasjonen eller SD-kortet, åpne Balena Etcher og klikk på "Flash from file" for å velge det nedlastede OS-bildet. Etcher vil automatisk oppdage tilkoblede stasjoner; velg riktig mål hvis det finnes flere. Klikk på "Flash" for å begynne å skrive avbildningen. Etcher validerer automatisk skriveprosessen når den er fullført. Når du er ferdig, kan du trygt fjerne stasjonen og bruke den til å starte enheten.


![image](assets/en/19.webp)


## 4️⃣ Førstegangsoppsett


For førstegangsoppsett, se Start9 [documentation](https://docs.start9.com/0.3.5.x/) under `USER MANUAL` etterfulgt av `Getting Started - Initial Setup`.  Denne offisielle veiledningen bør konsulteres for å få den mest oppdaterte informasjonen.


To alternativer presenteres:



- Begynn på nytt
- Alternativer for gjenoppretting


For en ny serverinstallasjon velger du `Start på nytt`. Først kobler du serveren til strøm og en Ethernet-kabel. Sørg for at datamaskinen som brukes til oppsettet, er på samme lokale nettverk. Ta ut den nylig flashede USB-stasjonen fra datamaskinen og sett den inn i serveren.


Du kan fjernstyre serveren fra en hvilken som helst datamaskin i samme nettverk. Åpne en nettleser og naviger til `http://start.local`.


**Merknad**: Hvis det oppstår tilkoblingsproblemer med denne adressen, skyldes det ofte at hjemmenettverk ikke klarer å løse opp `.local`-domenenavn. Problemet kan løses ved å få tilgang til serveren direkte via IP-adressen. IP-adressen finner du ved å logge deg inn på ruterens administrasjonsgrensesnitt (vanligvis på `192.168.1.1` eller en lignende adresse) og finne enheten i listen over DHCP-klienter eller nettverkskart. Deretter skriver du inn hele IP-adressen (f.eks. `http://192.168.1.105`) i nettleseren. Dette omgår DNS-oppløsningen. Hvis problemene vedvarer, kan du gå til [siden for vanlige problemer](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) eller [ta kontakt med kundestøtte](https://start9.com/contact/)


StartOS-oppsettskjermbildet bør vises. Klikk på `Start Fresh` for å starte oppsettet av den nye serveren.


![image](assets/en/03.webp)


Neste trinn er å velge lagringsenheten der StartOS-dataene skal lagres.


![image](assets/en/04.webp)


Angi et sterkt passord for serveren. Skriv det inn som anbefalt av Start9, og klikk deretter på "FERDIG".


![image](assets/en/05.webp)


Et skjermbilde vil vise at StartOS initialiserer og konfigurerer serveren. Neste trinn er å `Laste ned adresseinfo`, ettersom `start.local`-adressen kun er for oppsettformål og ikke vil fungere etterpå.


![image](assets/en/06.webp)


Konfigurasjonsfilen inneholder to kritiske tilgangsadresser: én for det lokale nettverket (LAN) og én for sikker tilgang via Tor. Begge adressene bør lagres i en sikker passordbehandling. Neste trinn er å `Trust your Root CA`. Åpne en ny nettleserfane, og følg instruksjonene for å stole på rotsertifiseringsinstansen og logge inn. Root CA-sertifikatet kan også lastes ned ved å klikke på `Last ned sertifikat` i den nedlastede filen.


## 5️⃣ Stol på rot-CA-en din


Etter at sertifikatet er lastet ned, må serverens `Root CA` være klarert av operativsystemet. Klikk på `Vis instruksjoner` og finn retningslinjene for det spesifikke operativsystemet.


![image](assets/en/07.webp)


For et Linux-system brukes følgende kommandoer. Først åpner du en terminal og installerer de nødvendige pakkene:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Naviger til katalogen der sertifikatet ble lastet ned, vanligvis `~/Downloads` . Utfør disse kommandoene for å legge til sertifikatet i operativsystemets tillitslager. Gå til nedlastingsmappen med `cd ~/Downloads`. Opprett den nødvendige katalogen med `sudo mkdir -p /usr/share/ca-certificates/start9`. Kopier sertifikatfilen, og erstatt `ditt-filnavn.crt` med det faktiske filnavnet, ved å bruke `sudo cp "ditt-filnavn.crt" /usr/share/ca-certificates/start9/`. Registrer sertifikatet permanent ved å legge til banen til sertifikatet i systemkonfigurasjonen med `sudo bash -c "echo 'start9/ditt-filnavn.crt' >> /etc/ca-certificates.conf"`. Til slutt gjenoppbygger du tillitslageret med `sudo update-ca-certificates`. Det er viktig å bruke det faktiske sertifikatfilnavnet og verifisere alle baner før du utfører disse kommandoene. Denne prosessen etablerer permanent tillit for Start9-serverens HTTPS-tilkoblinger.


En vellykket installasjon vil indikeres av en utdata som sier `1 lagt til`. De fleste applikasjoner vil da kunne koble seg til på en sikker måte via `https`. Hvis du bruker Firefox, kreves det et ekstra [siste trinn](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff). For Chrome eller Brave er det nødvendig med et annet [siste trinn](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome) for å konfigurere nettleseren til å respektere rot-CA-en. Test tilkoblingen ved å oppdatere siden. Hvis problemet vedvarer, avslutter du nettleseren og åpner den på nytt før du besøker siden på nytt.


![image](assets/en/08.webp)


## 6️⃣ Komme i gang med StartOS


Det skal nå være mulig å logge inn ved hjelp av en sikker HTTPS-tilkobling. Skriv inn `Passordet` for å få tilgang til `Velkomstskjermen`.


![image](assets/en/09.webp)


Dette skjermbildet inneholder nyttige snarveier for å komme i gang. Venstre sidefelt inneholder hovedmenyelementene for navigering.


## 7️⃣ System


Fanen Systemer i StartOS gir tilgang til sentrale systemfunksjoner for administrasjon av den personlige serveren. Her finner du verktøy for systemvedlikehold, sikkerhet, diagnostikk og konfigurasjon uten at du trenger å ha kompetanse på kommandolinjen.


I delen "Sikkerhetskopier" kan du ta sikkerhetskopier av hele systemet, inkludert tjenester, konfigurasjoner og data, som kan gjenopprettes senere. Dette er viktig for katastrofegjenoppretting eller migrering til ny maskinvare. Sikkerhetskopier kan lagres på eksterne stasjoner og krypteres ved hjelp av hovedpassordet.


Under "Administrer" i System-fanen kan du kontrollere viktige systemfunksjoner. Brukerne kan manuelt se etter og bruke StartOS-oppdateringer, slik at de har kontroll over systemoppdateringsprosessen. Det er mulig å laste inn egendefinerte tjenester eller tjenester fra tredjeparter som ikke er tilgjengelige på den offisielle markedsplassen. Hvis serveren ikke er koblet til via Ethernet, kan Wi-Fi-innstillinger konfigureres fra denne delen. Avanserte brukere kan aktivere SSH-tilgang for systemadministrasjon på terminalnivå.


![image](assets/en/10.webp)


Innsikt-delen gir sanntidsovervåking av serverens ytelse og tilstand, og viser CPU-, RAM- og diskbruk i form av grafer. Den viser også systemtemperaturen, noe som er nyttig for enheter som Raspberry Pi, som mangler aktiv kjøling. Gjennomsnittlig oppetid og belastning hjelper deg med å vurdere systemets stabilitet, og live-logger er tilgjengelige for feilsøking av service- eller systemproblemer.


I `Support`-delen får du tilgang til innebygde vanlige spørsmål og svar, offisiell dokumentasjon og støttekanaler i fellesskapet. Feilsøkingslogger kan lastes ned fra denne delen og deles med Start9s kundestøtte for raskere problemløsning.


![image](assets/en/11.webp)


## 8️⃣ Markedsplass


Markedsplassen brukes til å finne, installere og administrere tjenester på den personlige serveren. Det gir tilgang til programvare som Bitcoin Core, BTCPay Server og electrs. StartOS støtter flere markedsplasser, inkludert det offisielle Start9-registeret og fellesskapsdrevne registre. Disse kan legges til ved å klikke på "Change" og bytte til "Community Registry", som gir tilgang til et bredere utvalg av tjenester.


![image](assets/en/12.webp)


## 9️⃣ Installere en Bitcoin Full Node


Installering av en Bitcoin full node på StartOS gir full suverenitet over Bitcoin-opplevelsen. Det muliggjør validering av transaksjoner og forbedrer personvernet og sikkerheten ved å fjerne avhengigheten av eksterne tjenester som kan logge aktivitet. Du får full kontroll over transaksjonene, slik at de kan sendes direkte til nettverket. Standardalternativet er `Bitcoin Core`, som integreres med StartOS og gjør det mulig å koble til lommebøker som Specter, Sparrow eller Electrum for et selvforvaringsoppsett. Et alternativ, `Bitcoin Knots`, er også tilgjengelig gjennom Community Registry.


For å installere Bitcoin Core, naviger til Marketplace. Under standardregisteret finner du og installerer Bitcoin Core-tjenesten. Etter installasjonen vises en melding om "Needs Config", som krever at innstillingene må fullføres før tjenesten kan kjøre. Dette skjer vanligvis etter oppdateringer eller nye installasjoner, og krever en gjennomgang av `RPC-innstillingene`. Fortsett med standardkonfigurasjonen, og klikk på `Lagre`.


![image](assets/en/13.webp)


Når noden din er fullstendig synkronisert, kan den fungere som en privat backend for lommebøker som Sparrow, noe som gir bedre personvern og transaksjonsvalidering. For brukere som lagrer betydelige beløp, er det imidlertid viktig å forstå sikkerhetsavveiningene ved denne direkte tilkoblingen. Når en wallet kobles direkte til Bitcoin Core, kan sensitive data eksponeres, ettersom Bitcoin Core lagrer offentlige nøkler (xpubs) og wallet-saldoer ukryptert på vertsmaskinen. Et kompromittert system kan gjøre det mulig for en angriper å oppdage beholdningen din og angripe deg.


For å redusere denne risikoen og oppnå en mer robust sikkerhetsmodell kan du sette opp en privat Electrum Server. Denne serveren fungerer som et mellomledd, og indekserer blokkjeden uten å lagre wallet-spesifikk informasjon. Ved å koble wallet til din egen Electrum-server i stedet for direkte til Bitcoin Core, forhindrer du wallet fra å få tilgang til nodens sensitive data.


![image](assets/en/14.webp)


## 🔟 Sette opp valg


`electrs` (Electrum Rust Server) er en rask og effektiv indekserer som kobles til din Bitcoin Core-node og gjør det mulig for Electrum-kompatible lommebøker å spørre etter transaksjonshistorikk og saldoer i sanntid. Ved å kjøre electrs på StartOS eliminerer du avhengigheten av tredjeparts Electrum-servere, noe som forbedrer personvernet og sikkerheten betydelig - wallet-spørringene dine går direkte til noden du selv hoster.


For å sette det opp må du først installere electrs-tjenesten fra StartOS Marketplace. Systemet vil kreve at Bitcoin Core er fullstendig synkronisert før du fortsetter. Etter installasjonen bekrefter du `Needs Config`-innstillingene med de anbefalte standardverdiene, og electrs begynner å indeksere blokkjeden, noe som kan ta opptil en dag, avhengig av maskinvaren din.


![image](assets/en/15.webp)


Når du er ferdig, kan du koble til lommebøker som Sparrow eller Spectre. En vellykket tilkobling gjør at wallet kan synkroniseres direkte med noden din, noe som gir en sikker, privat og selvdrevet Bitcoin-opplevelse.


## 1️⃣1️⃣ Connect Sparrow Wallet


For å koble `Sparrow Wallet` til StartOS-noden din ved hjelp av electrs-implementeringen, må du først sørge for at Bitcoin Core er fullstendig synkronisert og at electrs er installert og kjører. Åpne Sparrow Wallet på enheten din og naviger til `File` -> `Settings` -> `Server`. Velg deretter `Private Electrum Server`. I URL-feltet skriver du inn `Tor hostname` og `Port` for electrs, som du finner i StartOS under `Services` -> `electrs` -> `Properties` (som vanligvis slutter på `.onion:50001`).


![image](assets/en/16.webp)


Deretter aktiverer du Tor ved å merke av for `Bruk proxy`, angi proxy-adressen til `127.0.0.1` og porten til `9050`. Klikk på `Test Connection` og vent et øyeblikk. Hvis tilkoblingen er vellykket, vises en bekreftelsesmelding, for eksempel `Connected to electrs`. Når dette er bekreftet, lukker du innstillingene og fortsetter med å opprette eller gjenopprette wallet. Dette oppsettet sikrer at wallet spør etter din egen node via electrs, noe som gir fullt personvern og tillitsløs drift.


![image](assets/en/17.webp)


## 🎯 Konklusjon


StartOS by Start9 er en brukervennlig, personvernfokusert plattform designet for selvhosting av viktige tjenester som Bitcoin- og Lightning-noder, lommebøker og personlige apper. Den eliminerer behovet for kommandolinjeferdigheter ved å tilby et rent grafisk grensesnitt, automatiserte sikkerhetskopier, helseovervåking og sikker Tor-tilgang, noe som gjør den ideell for ikke-tekniske brukere. Den modulære arkitekturen støtter sømløs integrering med verktøy som electrs eller Sparrow, noe som gir deg full kontroll over din økonomiske og digitale suverenitet. Med et sterkt fokus på åpenhet, lokal kontroll og utvidelsesmuligheter gir StartOS brukerne mulighet til å ta tilbake eierskapet fra sentraliserte plattformer og drive sin egen private, robuste infrastruktur.