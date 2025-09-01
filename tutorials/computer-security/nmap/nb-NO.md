---
name: Nmap
description: Master Nmap for nettverkskartlegging og sårbarhetsskanning
---

![cover](assets/cover.webp)



*Denne opplæringen er basert på originalt innhold av Mickael Dorigny publisert på [IT-Connect](https://www.it-connect.fr/). Lisens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Det er gjort endringer i den opprinnelige teksten



___



Velkommen til denne introduksjonen til Nmap, som er utviklet for alle som ønsker å mestre dette kraftige verktøyet for nettverksskanning. Målet er å gi deg den grunnleggende kunnskapen du trenger for å bruke Nmap effektivt i det daglige.



Nmap er et allsidig verktøy som er mye brukt av IT-, nettverks- og cybersikkerhetsfolk til diagnostikk, nettverksoppdagelse og sikkerhetsrevisjon. Denne opplæringen er rettet mot deg som er ny på disse feltene, og som ønsker å lære det grunnleggende om Nmap. Vi anbefaler at du har grunnleggende kunnskaper om system- og nettverksadministrasjon.



Du lærer det grunnleggende om Nmap, hvordan du utfører portskanninger, identifiserer aktive verter i et nettverk, oppdager tjenesteversjoner og operativsystemer, utfører sårbarhetsskanninger og mye mer. Hver del inneholder detaljerte forklaringer og praktiske eksempler som hjelper deg med å mestre bruken av Nmap i en rekke ulike sammenhenger.



Når du er ferdig med denne opplæringen, vil du ha en solid forståelse av Nmap og kunne bruke det effektivt til å forbedre sikkerheten og administrasjonen av nettverkene dine. God fornøyelse med lesingen.



## 1 - Introduksjon til Nmap: Hva er Nmap?



### I. Presentasjon



I denne første delen tar vi en titt på nettverksskanningsverktøyet Nmap. Vi skal se på de viktigste Elements du trenger å vite om dette verktøyet, og hvordan det fungerer generelt. Dette vil hjelpe oss til å forstå resten av opplæringen bedre.



### II. Introduksjon til Nmap-verktøyet



Nmap, for _Network Mapper_, er et gratis verktøy med åpen kildekode som brukes til **nettverksoppdagelse, kartlegging og sikkerhetsrevisjon**. Det kan også brukes til andre oppgaver, for eksempel **nettverksinventering, diagnostikk eller overvåking**.



Den kan avgjøre om verter i et bestemt nettverk er aktive og tilgjengelige, hvilke nettverkstjenester som er eksponert, hvilke versjoner og teknologier som er i bruk, og annen nyttig analyseinformasjon. Nmap kan brukes til å skanne en enkelt tjeneste på en bestemt maskin, eller over store deler av nettverket, opp til hele Internett.



Nmap har mange sterke sider:





- Kraftig og fleksibel**: Nmap kan skanne store nettverk og bruke avanserte deteksjonsteknikker. Den støtter UDP, TCP, ICMP, IPv4 og IPv6, og kan utføre versjonsdeteksjon, sårbarhetsskanninger eller protokollspesifikke interaksjoner. Arkitekturen er modulær, særlig takket være NSE-skript (Nmap Scripting Engine), som vi skal se nærmere på senere i denne veiledningen.
- Brukervennlighet**: Den offisielle dokumentasjonen er rikholdig og av høyeste kvalitet. Det finnes også mange fellesressurser som kan hjelpe deg med å komme i gang.
- Popularitet og lang levetid**: Nmap har vært en referanse innen sitt felt siden 1998. Den nåværende versjonen, på tidspunktet for denne oppdateringen, er 7.95. Selv om det finnes andre verktøy for spesifikke oppgaver, er Nmap fortsatt et must for nettverkskartlegging og -analyse.



**Nmap på kino**



Nmap er et av de få sikkerhetsverktøyene som har oppnådd en viss berømmelse blant allmennheten. Det dukker opp i filmen _Matrix Reloaded_, i en symbolsk scene der Trinity bruker det til å hacke seg inn i et system:



![nmap-image](assets/fr/01.webp)



matrise: Reloaded-scenen med Nmap



Han dukker også opp i andre filmverk.



**Tilbakemelding



Som systemadministrator og senere cybersikkerhetsrevisor og pentester bruker jeg Nmap nesten daglig, og jeg anbefaler det jevnlig til systemadministratorer som ønsker å styrke sin kontroll over nettverk og forbedre sine diagnostiske evner.



### III. Operasjon på høyt nivå



Nmap er tilgjengelig for Linux, Windows og macOS. Det er hovedsakelig skrevet i C, C++ og Lua (for NSE-skript). Det brukes hovedsakelig på kommandolinjen, selv om grafiske grensesnitt som Zenmap også er tilgjengelige. Vi anbefaler imidlertid på det sterkeste at du begynner med kommandolinjen for å få en bedre forståelse av hvordan det fungerer.



Et enkelt eksempel:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Denne kommandoen vil bli forklart i detalj senere. I denne veiledningen skal vi bruke Nmap på Linux, men den kan brukes på samme måte på andre systemer. Under Windows er Nmap avhengig av **Npcap**-biblioteket (som erstatter det nå foreldede WinPcap) for å fange opp og injisere nettverkspakker.



Nmap brukes som et vanlig binært program, for eksempel `ls` eller `ip`. Noen avanserte funksjoner kan kreve utvidede rettigheter, ettersom verktøyet noen ganger manipulerer pakker på ukonvensjonelle måter for å fremprovosere spesifikke reaksjoner på målsystemene (særlig for å oppdage tjenester eller sårbarheter).



### IV. Konsekvenser av å bruke Nmap



Før du tar i bruk Nmap, er det viktig å være klar over den potensielle effekten det kan ha på nettverk og systemer:





- Den kan sende **tusener eller til og med millioner av pakker** på kort tid, noe som kan mette visse nettverksinfrastrukturer.
- Det kan generate **malformede eller ikke-standardiserte** pakker, noe som kan forstyrre visse typer utstyr (spesielt industrielle systemer).
- Den kan produsere **angrepslignende atferd**, noe som kan utløse varsler i sikkerhetssystemer (brannmurer, IDS/IPS osv.).



Generelt sett er **Nmap et svært snakkesalig verktøy**, ettersom det genererer mye trafikk for å hente ut så mye informasjon som mulig. Det anbefales derfor at man setter seg godt inn i hvordan det fungerer før man bruker det i sensitive miljøer eller produksjonsmiljøer.



### V. Konklusjon



I dette avsnittet introduseres Nmap og dets hovedfunksjoner. Vi har sett at det er et viktig, kraftig og fleksibelt verktøy for nettverkskartlegging. Vi har også diskutert hvordan det fungerer og hvilke forholdsregler du må ta når du bruker det, for å sette scenen for de følgende delene av opplæringen.



## 2 - Hvorfor bruke Nmap?



### I. Presentasjon



I denne delen tar vi en titt på de viktigste bruksområdene for nettverksskanningsverktøyet Nmap. Vi skal se at det er et verktøy som er mye brukt i mange sammenhenger og yrker, og at det definitivt er en nyttig ferdighet å ha det i verktøykassen og vite hvordan man behersker det.



### II. Bruk av Nmap for diagnostikk og overvåking



Nmap kan brukes til nettverksdiagnostikk og, mer generelt, til overvåking. På samme måte som en ping kan brukes til å finne ut om to verter kommuniserer, kan Nmap brukes til raskt å finne ut om en vert er aktiv, eller om en bestemt tjeneste er i drift. Takket være [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap") kan vi få nøyaktige data om en verts svartid, ruten som pakkene tar, svaret fra en bestemt tjeneste osv.



Følgende kommando og resultat kan for eksempel brukes til raskt å finne ut om en webserver på host **192.168.1.18** er aktiv og svarer som den skal:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Bruk Nmap til å hente webtjenestestatus fra en ekstern server



Nmap går altså lenger enn den berømte "ping-testen" i feilsøkings- eller diagnostiseringsfasen. Vi skal senere se at det finnes flere metoder som Nmap bruker for å identifisere hvilken tjeneste som lytter på en gitt port, inkludert hvilken versjon den har.



### III. Bruk av Nmap for nettverkskartlegging



Som _Network Mapper_ er hovedformålet med dette verktøyet å kartlegge nettverk. Det kan brukes i et lokalt nettverk, eller på tvers av flere nettverk, subnett og VLAN, for å liste opp alle verter og tjenester som kan nås. Nmap gjør denne oppgaven mye raskere og mer effektiv enn noen manuell metode.



Følgende kommando kan for eksempel brukes til raskt å identifisere aktive verter i nettverket **192.168.1.0/24**:



```
nmap -sn 192.168.1.0/24
```



*Merk: `-sP`-alternativet er foreldet og har blitt erstattet av `-sn`.*



![nmap-image](assets/fr/03.webp)



*Bruke Nmap til å finne tilgjengelige verter i et nettverk*



Vi skal senere se at det finnes flere metoder som Nmap bruker for å avgjøre om en host kan anses som "aktiv", selv om den på forhånd ikke eksponerer noen tjenester.



### IV. Bruke Nmap til å evaluere en filtreringspolicy



Nmap har fordelen av å være faktabasert: Resultatene gjør det mulig å fastslå konkrete funn, i motsetning til ethvert arkitekturdokument eller filtreringspolicy. Det er et nøkkelverktøy for å vurdere effektiviteten av informasjonssystemets oppdeling, ettersom det gjør det mulig å **verifisere om filtreringspolicyen faktisk blir brukt**.



I et bedriftsnettverk tilsier beste praksis at systemer segmenteres i henhold til rolle, kritikalitet eller plassering. Filtreringsregler (ofte implementert via brannmurer) må begrense kommunikasjonen mellom sonene. Men disse konfigurasjonene er ofte kompliserte og utsatt for feil.



For å validere at policyen er overholdt, er det ingenting som slår en konkret test. Du kan for eksempel kontrollere at sensitive administrasjonstjenester (SSH, WinRM, MSSQL, MySQL osv.) ikke er tilgjengelige fra en brukersone.



Bruk av **Nmap for å teste filtreringspolicyen** bør være systematisk før en slik policy settes i produksjon. Dessverre blir denne kontrollen ofte forsømt.



Min erfaring er at mange konfigurasjonsfeil går ubemerket hen når det ikke finnes valideringstester. En enkel feil i et IP-område eller en regeloversikt kan gjøre en tilsynelatende isolert sone sårbar.



### V. Bruk av Nmap til sikkerhetsrevisjon og inntrengningstesting



Nmap har **mange nyttige funksjoner for sikkerhetsvurdering**, penetrasjonstesting (pentester), og dessverre også for angripere.



Funksjoner for nettverksoppdagelse er avgjørende for en angriper, som trenger å forstå nettverkstopologien etter en første kompromittering. Men Nmap tilbyr mye mer enn dette: Det integrerer en skriptmotor, hvorav **mange er dedikert til sårbarhetsdeteksjon**.



Denne kommandoen kan for eksempel brukes til å sjekke om en FTP-tjeneste tillater anonym tilkobling, uten at du trenger å koble til manuelt:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Bruke et NSE-skript for å sjekke anonym FTP-godkjenning via Nmap.*



Nmap-sårbarhetsdeteksjon er et av de første trinnene i en revisjon eller penetrasjonstest. Det gjør at du raskt kan identifisere visse svake punkter og optimalisere analysearbeidet.



Men vær oppmerksom på dette: **verktøy for sårbarhetsskanning har sine begrensninger**. Nmap dekker bare en brøkdel av truslene, og garanterer ikke at et system er trygt hvis det ikke oppdages noen problemer. Det er derfor viktig å **forstå hvordan skriptene som brukes fungerer**, og ikke bare stole på dommen deres.



### VI. Konklusjon



Vi har sett at det å beherske Nmap kan dekke et bredt spekter av bruksområder, fra diagnostikk og overvåking til kartlegging, evaluering av sikkerhetspolicyer og sårbarhetsskanning. I neste avsnitt skal vi gå ned til de små detaljene og installere Nmap.




## 3 - Installere og konfigurere Nmap



### I. Presentasjon



I denne delen lærer vi hvordan du installerer nettverksskanningsverktøyet Nmap på Linux og Windows OS. På slutten av denne delen vil vi ha alt vi trenger for å begynne å bruke Nmap for fremtidige moduler. Til slutt ser vi hvilke privilegier det kan kreve når det brukes, og hvorfor.



### II. Installere Nmap under Linux



Nmap ble opprinnelig utviklet for å kjøre på GNU/Linux-operativsystemer. Som et resultat av dette, og takket være dets lange levetid og popularitet, finner du det i alle de offisielle repositoriene til de største Unix-distribusjonene. I denne veiledningen bruker jeg et Debian-basert operativsystem [Kali Linux] (https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Men du kan bruke det på nøyaktig samme måte fra en klassisk Debian, CentOS, Red Hat eller hva som helst!



Under Debian kan du bruke følgende kommando for å sjekke at Nmap finnes i de aktuelle repositoriene dine:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



Svaret her indikerer tydelig at "nmap" -pakken eksisterer i depotene (her, de av Kali [Linux] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). Fra nå av kan du installere Nmap via de vanlige installasjonskommandoene, ikke noe avvæpnende for øyeblikket 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



For å kontrollere at Nmap er riktig installert, vil vi vise versjonen:



```
nmap --version
```



Her er det forventede resultatet:



![nmap-image](assets/fr/05.webp)



resultat av å vise den gjeldende versjonen av Nmap._ _



Legg merke til at biblioteket "libpcap" (_Packet Capture Library_) og versjonen av det er til stede i denne visningen. "libpcap" brukes også av Wireshark, og brukes av Nmap til å opprette og manipulere pakker og lytte til nettverkstrafikk.



### III Installere Nmap på Windows



For å installere på et Windows-operativsystem, begynner du med å laste ned binærfilen fra det offisielle nettstedet (og ingen andre!):





- Nmap-nedlastingssiden på den offisielle nettsiden: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




Deretter må du laste ned den binære filen `nmap-<VERSION>-setup.exe`:



![nmap-image](assets/fr/06.webp)



nedlastingsside for binærinstallasjon av nmap for Windows



Når du har denne binærfilen på systemet ditt, er det bare å kjøre den for å installere Nmap. Dette er en enkel installasjon, og du kan la alle alternativene være som standard.



Min refleks er å fjerne merket for "zenmap (GUI Frontend)". Dette er en grafisk Interface for Nmap som jeg ikke bruker, og som ikke vil bli dekket i denne opplæringen, men prøv den gjerne ut når du har mestret Nmap-kommandolinjeverktøyet!



![nmap-image](assets/fr/07.webp)



valgfritt fravalg av Zenmap ved installasjon av Nmap på Windows



På slutten av Nmap-installasjonen foreslås en ny installasjon, nemlig av "Npcap"-biblioteket:



![nmap-image](assets/fr/08.webp)



installasjon av "Npcap"-biblioteket ved installasjon av Nmap under Windows



Dette er biblioteket som Nmap er avhengig av for å håndtere nettverkskommunikasjon, dvs. å bygge, sende og motta nettverkspakker. Du har sannsynligvis allerede støtt på dette biblioteket hvis du bruker Wireshark på Windows, siden det også bruker det og krever installasjon.



Som med Linux kan du kontrollere at Nmap er installert ved å åpne en kommandoprompt eller en [Powershell]-terminal (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") og skrive inn følgende kommando:



```
nmap --version
```



Her er det forventede resultatet:



![nmap-image](assets/fr/09.webp)



resultat av å vise den gjeldende versjonen av Nmap._ _



Nmap er nå installert på Windows. Du kan bruke det på nøyaktig samme måte som på Linux, ved å følge denne veiledningen.



### IV. Lokale rettigheter som kreves for å bruke Nmap



Men forresten, når du bruker Nmap, **er det nødvendig å ha forhøyede lokale rettigheter på systemet?** Svaret er: **det kommer an på**.



I sin helt grunnleggende form, dvs. uten å gå veldig langt i å bruke alternativene, krever Nmap ikke nødvendigvis privilegerte rettigheter. Du vil imidlertid snart innse at det er bedre å bruke Nmap i en privilegert kontekst ("root" under Linux, "administrator" eller tilsvarende under Windows) for å kunne utnytte det fulle potensialet, med fare for å få en feilmelding som denne:



![nmap-image](assets/fr/10.webp)



feilmelding under Linux når Nmap-alternativer krever root-rettigheter



Enten du bruker Linux eller Windows, er det mange tilfeller der Nmap vil be deg om privilegert tilgang. De viktigste grunnene er som følger (ikke-uttømmende liste):





- Konstruksjon av "rå" nettverkspakker**: Nmap er i stand til å bruke et bredt spekter av skannemetoder, inkludert avansert pakkemanipulering og -konstruksjon. Dette er for eksempel tilfelle når vi ønsker å utføre TCP SYN-skanninger, som ikke respekterer det klassiske _treveis håndtrykket_ i TCP-utvekslinger. For å gjøre dette må Nmap bruke andre funksjoner enn de som er innfødte i operativsystemer, som bare vet hvordan man respekterer god praksis i nettverkskommunikasjon (det kaller på bibliotekene "Npcap" og "libcap" som er sett ovenfor). Det er fordi Nmap ikke gjør ting på "standard" måte at det er i stand til å utlede viss informasjon om operativsystemer, tjenester og visse sårbarheter.





- Lytt til nettverkstrafikk**: Noen av Nmaps alternativer krever at den lytter til nettverket for å hente ut visse typer informasjon. Denne handlingen anses som sensitiv på operativsystemer, siden den også gjør det mulig å lytte på kommunikasjonen til andre applikasjoner på systemet. Akkurat som Wireshark trenger Nmap spesifikke privilegier for å gjøre dette, noe som er lettere å oppnå ved å være direkte i en privilegert økt.





- Lytting på privilegerte porter**: På operativsystemer er porter fra 0 til 1024 (både TCP og UDP) såkalt privilegerte, dvs. at de på en eller annen måte er reservert for helt spesifikke bruksområder og derfor beskyttet. Selv om dette er en noe foreldet grunn i dag, er det fortsatt nødvendig å ha visse privilegier for å lytte på disse portene, noe Nmap kan være nødt til å gjøre avhengig av hvordan det skal brukes.





- Sende UDP-pakker:** På samme måte krever det å lytte til en nettverksapplikasjon på UDP-porter (en tilstandsløs protokoll) privilegerte rettigheter på operativsystemer. Det kreves derfor en økt med privilegerte rettigheter hvis du ønsker å utføre en UDP-skanning, der Nmap må lytte etter svar for å kunne analysere svarene på skanningene.




For å være mer presis er det mulig, i hvert fall under Linux, å kjøre Nmap med alle dens funksjoner og alternativer uten å være root. Dette oppnås ved å gi de rette _kapabilitetene_ til den binære filen. Dette krever imidlertid avansert manipulering og er kanskje ikke like praktisk som å kjøre Nmap direkte med rettigheter. Denne tilnærmingen er dessuten mindre vanlig og kan skape sikkerhetsproblemer hvis den er feilkonfigurert.



Dette er imidlertid litt annerledes enn Nmap-veiledningen vår, så vi dropper det for denne gang.



I resten av denne veiledningen antar vi at Nmap alltid kjøres som "root" (fra et skall som "root" eller via kommandoen "sudo"), eller i en administratorterminal under Windows, selv om dette ikke er angitt. I motsatt fall kan du oppleve subtile, men merkbare forskjeller fra veiledningen.



### V. Konklusjon



Og det var det! Nmap er nå installert på operativsystemet vårt og klar til bruk, og krever ingen ytterligere konfigurasjon. Denne delen avslutter introduksjonen og presentasjonen av Nmap. Jeg håper det har fått det til å renne i munnen på deg, og at du er ivrig etter å begynne å øve.



Nå har vi fått en bedre forståelse av hva Nmap-kartleggingsverktøyet er, hva som er de vanligste bruksområdene, og hvilke begrensninger det har. La oss gå videre!




## 4 - TCP- og UDP-portskanninger med Nmap



### I. Presentasjon



I denne delen lærer vi hvordan vi utfører våre første portskanninger ved hjelp av nettverksskanningsverktøyet Nmap. Vi skal se hvordan vi bruker det til å lage en liste over nettverkstjenester som er eksponert på en vert, enten de bruker TCP- eller UDP-protokoller.



Fra nå av må du huske å bare skanne verter i et kontrollert miljø som du har eksplisitt autorisasjon for.





- Som en påminnelse: [Straffeloven: Kapittel III: Angrep på automatiserte databehandlingssystemer] (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Hvis du ikke har en slik løsning tilgjengelig**, anbefaler jeg følgende gratisløsninger, som er helt perfekte!





- [Hack The Box] (https://app.hackthebox.com/ "Hack The Box")**: Hack The Box er en plattform for opplæring i hacking, og tilbyr kontinuerlig sårbare systemer som du kan angripe etter eget ønske. Flere hundre systemer er tilgjengelige, men en fornyet pool på 20 maskiner tilbys gratis hele året, med tilgang via en OpenVPN VPN.





- [Vulnhub] (https://www.vulnhub.com/ "Vulnhub")**: Denne plattformen tilbyr en rekke bevisst sårbare systemer for nedlasting, som kan brukes via VirtualBox (også en gratis løsning) eller på andre måter. Når du har lastet ned, er det ikke behov for VPN - alt er lokalt.




Du står også fritt til å **opprette en virtuell maskin** på ditt favorittoperativsystem og installere ulike tjenester på den som testmål. Fordelen her er at du også vil kunne se hva som skjer på serversiden under en skanning, spesielt med Wireshark, og ha en finger med i spillet i den lokale brannmuren når vi gjør mer avanserte tester.



La oss gjøre noe praktisk!



### II. Skanning av en verts TCP-porter via Nmap



#### A. Første TCP-portskanning med Nmap



Vi skal nå utføre våre første skanninger via Nmap. Målet vårt her er enkelt: Vi ønsker å finne ut hvilke tjenester som er eksponert av webserveren vi nettopp har distribuert, for å se om det er noe uventet, for eksempel en administrasjonstjeneste som ikke burde være tilgjengelig, eller eksponering av en port til en applikasjon som vi trodde var deaktivert.



I mitt eksempel har verten som skal skannes, IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



Her er et mulig resultat. Vi ser en klassisk Nmap-retur med mye informasjon:



![nmap-image](assets/fr/11.webp)



resultatene av en enkel TCP-skanning utført med Nmap._ _



En rask titt på dette resultatet viser at portene TCP/22 og TCP/80 er tilgjengelige på denne verten.



Som standard, og hvis du ikke ber den om det, vil Nmap bare skanne TCP-porter.



#### B. Forstå resultatene av en enkel Nmap-skanning



La oss imidlertid gå et skritt videre for å forstå denne utdataen: Hver linje er viktig, for det første for å vite hva som nettopp er gjort, og for det andre for å kunne tolke selve skanneresultatene riktig.



Den første linjen er egentlig en påminnelse om skanneversjonen og -datoen (nyttig for logging og arkivering, tross alt!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



Den andre linjen viser skanneresultatene for verten "debian.home (192.168.1.19)". Denne informasjonen vil være nyttig når vi begynner å skanne flere verter samtidig:



```
Nmap scan report for debian.home (192.168.1.19)
```



Den tredje linjen forteller oss at den aktuelle verten er "Up", dvs. aktiv:



```
Host is up (0.00022s latency).
```



Til slutt informerer Nmap oss om at 998 TCP-porter som er identifisert som lukkede, ikke vises i:



```
Not shown: 998 closed tcp ports (conn-refused)
```



Dette sparer oss for nesten 1000 linjer med utdata som ser ut som:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Takk til ham for at han sparte oss for dette!



Hvorfor 998 "lukkede" porter? Hvis du legger til de to åpne portene, blir det 1000, og det er det antallet porter Nmap vil skanne i standardkonfigurasjonen, ikke de 65535 eksisterende TCP-portene! Vi skal senere se at dette kan tilpasses helt og holdent. Men hvis den aktuelle verten har en tjeneste som lytter på en ganske eksotisk port, vil denne "standard"-skanningen ikke avdekke den.



Etter denne informasjonen finner vi det som er mest interessant: en tabell organisert i henhold til de tre kolonnene "PORT - STATE - SERVICE":





- Den første "PORT"-kolonnen angir ganske enkelt den porten/protokollen som skal brukes, og her er det viktig å se på om det er en TCP-port (`<port>/tcp`) eller UDP (`<port>/udp`).





- Kolonnen "STATE" angir statusen til nettverkstjenesten som er oppdaget på denne porten, og som Nmap har bestemt på grunnlag av svaret som er innhentet. Denne kan være "open", "closed", "filtered" eller "unknown". Vi skal senere se hvordan Nmap skiller mellom disse ulike tilstandene.





- Kolonnen "SERVICE" angir tjenesten som er eksponert på den aktuelle porten. Vær imidlertid oppmerksom på at vi ikke har brukt aktive tjenesteoppdagelsesalternativer her. Nmap baserer seg på en lokal referanse mellom en port/protokoll og den antatt tildelte tjenesten: filen "/etc/services"




Hvis du tar en titt på filen "/etc/services" på et Linux-system, vil du finne en "port/protocol - service"-lenke som ligner på den som vises av Nmap:



![nmap-image](assets/fr/12.webp)



henter ut innholdet i filen "/etc/services" under Linux._ _



Det er viktig å forstå at Nmap foreløpig ikke har utført noen aktiv tjenesteoppdagelse. Det ville for eksempel ikke ha vært i stand til å identifisere SSH-tjenesten bak en TCP/80-port hvis dette hadde vært tilfellet. Derfor er det viktig å vite hvordan du bruker de riktige alternativene - det kommer snart!



Å vite hvordan du skal tolke Nmapps utdata er en viktig del av det å mestre verktøyet. Den gode nyheten er at utdataene i stor grad vil være de samme, uansett hvilke alternativer du bruker.



#### C. Under panseret: nettverksanalyse via Wireshark



Hvis du tar en nærmere titt på hva som skjer på nettverket Interface til verten som skanner serveren, eller på selve serveren, vil Nmaps handlinger bli mye tydeligere. Det er det vi skal gjøre her.



Det jeg kan vise deg her, er bare en del av det som er synlig i Wireshark. Hvis du vil gå lenger, kan du gjerne gjøre en nettverksregistrering selv under en skanning, og deretter bla gjennom det som er registrert.



I denne testen befinner skanneverten (192.168.1.18) og målverten (192.168.1.19) seg på samme lokale nettverk.



Nmap starter med å finne ut om målverten er aktiv i det lokale nettverket ved å sende en ARP-forespørsel. Hvis den mottar et svar, vet den at verten er aktiv og begynner å skanne nettverket:



![nmap-image](assets/fr/13.webp)



_ARP-forespørsel utstedt av Nmap for å finne ut om en målvert er til stede i det lokale nettverket._ _ARP request issued by Nmap to determine whether a target host is present on the local network



Hvis verten som skal skannes, befinner seg på et eksternt nettverk, starter Nmap med å sende en ping-forespørsel og prøver å nå noen av de mest utsatte portene (TCP/80, TCP/443):



![nmap-image](assets/fr/14.webp)



ping-forespørsel utstedt av Nmap for å finne ut om en målvert kan nås i et eksternt nettverk



Hvis den får svar på noen av disse testene, anser den målet for å være aktivt.



Når Nmap har fastslått at målet er aktivt, vil den prøve å løse domenenavnet med DNS-serveren som er konfigurert på nettverkskortet:



![nmap-image](assets/fr/15.webp)



dNS-oppløsning på Nmap-skannemål



Nå som Nmap har identifisert målet og vet at det er aktivt, begynner det å skanne TCP-porten:



![nmap-image](assets/fr/16.webp)



tCP SYN-pakkeoverføring og RST/ACK-mottak under Nmap-skanning



For å gjøre dette vil den, på hver TCP-port i standardområdet, **sende TCP SYN-pakker og vente på svar**. I skjermbildet ovenfor mottar den TCP RST/ACK-pakker fra den skannede serveren, noe som betyr "gå videre, det er ingenting å se her" - med andre ord er disse portene stengt. Som vi så i resultatet, vil dette være tilfelle for de fleste av de skannede portene. Med to unntak:



![nmap-image](assets/fr/17.webp)



svar på en TCP SYN-pakke sendt på port 22, aktiv på skannemålet



I skjermbildet ovenfor ser vi en TCP SYN/ACK-pakke sendt av målverten**. Porten er aktiv og eksponerer en tjeneste. Nmap kvitterer for mottak av svaret, og avslutter deretter forbindelsen (TCP RST/ACK). **Slik visste den at port TCP/22 var aktiv**.



Vi har sett her at Nmap respekterer "Three Way Handshake" når den skanner et TCP-nettverk. Av ytelseshensyn er det mulig å be den om ikke å svare på serverens retur, og dermed spare flere tusen pakker når du skanner et stort nettverk. Men vi skal se på disse alternativene og optimaliseringene senere i veiledningen.



Vi har nå en bedre forståelse av hvordan man utfører en TCP-skanning og hva som faktisk skjer når den utføres. Vi har også sett at Nmap som standard utfører en TCP-portskanning på et begrenset antall porter.



### III. Skanning av UDP-porter med Nmap



#### A. Første UDP-portskanning med Nmap



La oss nå se hvordan du skanner en verts UDP-porter. Som vi har sett, vil Nmap som standard alltid skanne TCP-porter. Dette kan bety at vi går glipp av mye informasjon hvis vi ikke er klar over det.



Som en påminnelse: I denne testen befinner skanneverten (192.168.1.18) og målverten (192.168.1.19) seg på samme lokale nettverk.



```
nmap -sU 192.168.1.19
```



Her har returen samme format som for en TCP-skanning, men de aktive tjenestene som vises, er i `<port>/UDP`, som ønsket!



![nmap-image](assets/fr/18.webp)



resultatet av en enkel UDP-skanning utført med Nmap._ _



Alternativet "-sU" brukes til å fortelle Nmap at du ønsker å jobbe med UDP, i stedet for TCP som er standard.



For øvrig vil du sikkert legge merke til at Nmap krever "root"-rettigheter for UDP-skanninger, som nevnt tidligere i veiledningen.



merk: Siden de nyeste versjonene av Nmap anbefales det alltid å kjøre UDP-skanninger med administratorrettigheter for å sikre pålitelige resultater, ettersom noen funksjoner krever rå tilgang til nettverksstikkontakter._ _



UDP-skanninger kan ta svært lang tid (1100 sekunder for å skanne 1000 porter i mitt eksempel), på grunn av fraværet av "Three Way Handshake" i UDP, noe som betyr at Nmap vil vente på et svar for hver UDP-pakke som sendes, og vil bestemme porten som "lukket" bare hvis det ikke kommer noe svar etter en viss tid (timeout). Denne responsen fra skannede verter er ikke systematisk og er ofte begrenset når det gjelder antall svar per sekund, for å unngå visse forsterkningsangrep. Dette står i kontrast til TCP, der det er en umiddelbar respons fra den skannede verten, uansett om porten er åpen eller lukket. Vi skal senere se hvordan dette kan optimaliseres.



Et annet problem med UDP er **at tjenester ikke alltid svarer på innkommende pakker**, ganske enkelt fordi dette ikke alltid er nødvendig, og det er prinsippet i UDP. Når dette er tilfelle, og ingen ICMP "port unreachable" mottas, blir tjenesten merket som "open|filtered" av Nmap, som vist i skjermbildet ovenfor.



#### B. Under panseret: nettverksanalyse via Wireshark



Som med TCP-skanningen vår, skal vi se nærmere på hva som skjer på nettverksnivå under en UDP-skanning ved hjelp av en Wireshark-analyse. Nmap oppfører seg på samme måte når den avgjør om en vert er aktiv.



Den eneste reelle forskjellen ved skanning av UDP er at Nmap ikke venter på et "Three Way Handshake", siden denne mekanismen ikke finnes i UDP (statsløs protokoll):



![nmap-image](assets/fr/19.webp)



overføring av uDP-pakker og mottak av ICMP-pakker (port utilgjengelig) under Nmap-skanning



Vi kan se på skjermbildet ovenfor at Nmap vil sende et stort antall UDP-pakker, og motta en ICMP "Destination unreachable (Port unreachable)"-pakke som svar på de fleste av dem. Dette er normalt, ettersom det er det riktige svaret som er definert av [RFC 1122] (https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") når en UDP-port ikke kan nås:



![nmap-image](assets/fr/20.webp)



utdrag fra RFC 1122._ _



La oss ta en nærmere titt på dette Wireshark-opptaket, som viser **de tre mulige scenariene** i UDP:



![nmap-image](assets/fr/21.webp)



nettverksopptak under en UDP-skanning på forskjellige porter med Nmap._ _



De tre casene er som følger:





- Den første Exchange består av pakkene nr. 3, 4 og 8, 9. Nmap sender UDP-pakker på den klassiske SNMP-porten og **konstruerer derfor protokollkonforme pakker på forhånd**. Deretter innhenter den et svar fra serveren (pakke nr. 8 og 9). Resultat: Nmap har mottatt et svar, tjenesten er "åpen".





- Den andre Exchange består av pakkene 6 og 7. Nmap sender en "tom" UDP-pakke (uten protokollstruktur) til port UDP/165, og mottar en ICMP-pakke som svar: "Destinasjon utilgjengelig (port utilgjengelig)". Resultat: Nmap har mottatt et (negativt) svar, verten er oppe, men tjenesten den prøvde å nå, er ikke operativ på denne porten, som vil bli merket som "stengt".





- Den siste Exchange består av pakke nr. 12: Nmap sender en "tom" UDP-pakke til port UDP/1235. Det kommer ikke noe svar, ikke engang et eksplisitt avslag fra den skannede verten. Resultat: Nmap markerer porten som "åpen|filtrert", da den ikke kan si om dette skyldes tilstedeværelsen av en brannmur som er konfigurert til ikke å svare, eller en aktiv UDP-tjeneste som uansett ikke returnerer noe svar (ikke obligatorisk i UDP).




Her er resultatet som vises av Nmap etter disse tre tilfellene:



![nmap-image](assets/fr/22.webp)



mulige resultater av en UDP-skanning utført via Nmap._ _



Vi har nå en bedre idé om hvordan man gjør en UDP-skanning, og hva som faktisk skjer når den utføres. Så langt har vi bare brukt Nmap på en veldig enkel måte, uten å bestemme hvilke porter vi skal skanne, men det er i ferd med å endre seg!



### IV. Finjustering av portskanning med Nmap



#### A. Påminnelse om Nmapps standardoppførsel



Som vi har sett, velger Nmap selv antall og porter som skal skannes hvis du ikke angir noen alternativer. Dette er "standardkonfigurasjonen" som brukes av Nmap når du ikke forteller den nøyaktig hva den skal gjøre. Disse standardalternativene er utformet for å gi et inntrykk av de viktigste portene som er eksponert, og disse velges etter eksponeringsfrekvens (vanligste eller hyppigste porter) i stedet for i numerisk rekkefølge (port 1, 2, 3 osv.), og også for å unngå å starte en skanning av de 65535 mulige portene hvis du ikke spesifiserer de riktige alternativene, noe som ville være for langt og ordrikt for et "standard" brukstilfelle.



**Hvordan velges disse portene?



De 1000 portene som skannes i standardmodus, er valgt ut i henhold til hvor ofte de forekommer. Denne statistikken vedlikeholdes av Nmap og oppdateres på samme måte som selve binærfilen og dens skript (moduler). Du kan selv se denne statistikken i filen "/usr/shares/nmap/nmap/nmap-services":



![nmap-image](assets/fr/23.webp)



hentet fra filen "/usr/shares/nmap/nmap/nmap-services"._



Her, i den tredje kolonnen, ser vi noe som ser ut som sannsynligheter (mellom 0 og 1) eller en prosentfordeling. Dette er hyppigheten av forekomsten av hvert port-/protokollpar. Vi kan se at de mest kjente portene (FTP, SSH, TELNET og SMTP i dette uttrekket) har en mye høyere verdi enn de andre.



#### B. Spesifiser målportene for en Nmap-skanning nøyaktig



I den virkelige verden kan vi imidlertid ha behov for å skanne bare en bestemt port, eller flere porter, eller et bestemt utvalg av porter. Nmap gjør det enkelt å gjøre nettopp det, på en enhetlig måte for både UDP- og TCP-skanninger.



**Skann en spesifikk port via Nmap**



Hvis vi ønsker å skanne en enkelt port, og ikke 1000, kan vi spesifisere denne porten via Nmaps "-p" eller "--port"-alternativ:



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Resultatet er at skanningen naturligvis blir mye raskere, og Nmap sender bare ut de pakkene som trengs for å finne ut om verten er aktiv, og deretter om den angitte porten er tilgjengelig. Dette sparer tid hvis du bare vil kjøre en rask test for å se om webtjenesten på utstillingsvinduet ditt fortsatt er oppe.



**Skann flere porter via Nmap**



På samme måte kan vi spesifisere flere porter til Nmap ved å bruke det samme alternativet og sette sammen de spesifiserte portene med et komma:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Uansett rekkefølge vil Nmap sjekke alle disse portene, og bare de på den aktuelle verten. Du vil legge merke til at Nmap **eksplisitt forteller oss alle portene og deres status**, selv om de er "lukket". I motsetning til standardoppførselen, der denne komplette utdataene ville ha tatt opp altfor mye plass:



![nmap-image](assets/fr/24.webp)



*Resultatet av en Nmap TCP-skanning på de angitte portene*



**Skann en rekke porter



Hvis antallet porter du ønsker å skanne, er for stort, kan du angi dem etter intervall, for eksempel:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Du kan selvfølgelig mikse og matche som det passer deg, for eksempel:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**TCP- og UDP-portskanning



Du kan også utføre UDP- og TCP-skanninger samtidig, på utvalgte porter:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



I dette siste eksempelet ser du at "U:" indikerer en UDP-port og "T:" indikerer en TCP-port. Her er et mulig resultat av denne typen skanning:



![nmap-image](assets/fr/25.webp)



*Resultatet av en TCP- og UDP-portskanning med Nmap.*



Det er en interessant måte å tilpasse skanningene dine på!



**Søk alle porter



Til slutt er det mulig å spesifisere mye større eller mindre områder til Nmap. Vi har sett at standardlisten som velges av Nmap, inneholder 1000 porter. Vi kan også be om de 100 hyppigste portene, eller de 200 hyppigste, ved å bruke alternativet "--top-ports":



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Til slutt kan vi be den om å skanne alle mulige porter (alle 65535) ved å bruke notasjonen "-p-":



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



Sistnevnte vil ta lengre tid, spesielt med UDP, men du vil være sikker på at du ikke går glipp av noen åpne porter.



*Merk: Alternativet "-p-" er den anbefalte metoden for skanning av alle TCP-porter. For UDP-skanninger anbefales det å begrense antall porter av ytelseshensyn, ettersom fullstendige skanninger av alle UDP-porter kan ta svært lang tid



Senere i veiledningen skal vi se hvordan vi kan optimalisere hastigheten på Nmap-skanninger slik at de passer til våre behov, noe som vil være spesielt nyttig for skanninger på alle TCP- og UDP-porter.



### V. Konklusjon



I denne delen har vi endelig fått litt praktisk øvelse, så vi vet nå **hvordan vi bruker Nmap på en grunnleggende måte til å skanne en verts TCP- og UDP-porter**. Vi har også sett nærmere på hva som skjer på nettverksnivå, og **hvordan Nmap avgjør om en TCP- eller UDP-port er aktiv eller ikke**. Til slutt vet vi hvordan vi velger portene vi ønsker å skanne, og **hvad Nmaps standardalternativer faktisk gjør**. I det følgende skal vi gjenbruke denne kunnskapen og bruke den til å skanne et helt nettverk, inkludert global kartlegging og nettverksoppdagelse.




## 5 - Kartlegging og oppdagelse av nettverk med Nmap



### I. Presentasjon



I denne delen skal vi lære hvordan du bruker nettverksskanningsverktøyet Nmap til å kartlegge nettverket ditt. Vi skal se hvor effektivt det kan være i denne oppgaven, ved hjelp av de ulike alternativene. Til slutt ser vi på ulike måter å spesifisere målene for skanningene til Nmap på.



Vi skal særlig bruke det vi lærte i forrige avsnitt om hvordan Nmap avgjør om en host er aktiv og tilgjengelig.



Som nevnt i introduksjonen til Nmap, er dette en Network Mapper. Som sådan er det det perfekte verktøyet for å lage en liste over tilgjengelige verter i et nettverk, enten det er lokalt eller eksternt.



**Forfatterens tilbakekomst



Som cybersikkerhetsrevisor og pentester bruker jeg faktisk Nmap systematisk når jeg utfører interne inntrengningstester for å finne ut hvor jeg er, hvem naboene mine er i det lokale nettverket og hvilke andre nettverk som er tilgjengelige, samt systemene som befinner seg på dem. Målet mitt er enkelt: å kartlegge nettverket, bestemme størrelsen på informasjonssystemet og ikke minst skissere angrepsflaten.



Nettverkskartlegging kan også være nyttig i forbindelse med nettverksdiagnostikk, overvåking og kartlegging av ressurser (er du virkelig sikker på at IS-en din bare består av det som finnes i Active Directory eller i GLPI/OCS-inventaret? Den kan også brukes til å oppdage forekomsten av skygge-IT i informasjonssystemet.



### II. Bruke Nmap til å skanne et nettverksområde



#### A. Oppdage et nettverk med en Nmap-skanning



Nå vil vi gå et hakk videre og analysere hele det lokale nettverket vårt. Ingenting kunne vært enklere: Alt vi trenger å gjøre er å gjenbruke kommandoene vi så i forrige avsnitt, men spesifisere en CIDR i stedet for en enkel IP Address.



CIDR (**Classless Inter Domain Routing**) er den "klassiske" notasjonen for å angi et nettverksområde og dets utstrekning (ved hjelp av masken). For eksempel er "192.168.0.0/24" en "oversettelse" av den desimale maskenotasjonen "255.255.255.0".



Hvis du vil bruke Nmap ved å angi en CIDR, kan du gjøre det på følgende måte:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



Det er også mulig å spesifisere flere verter, flere nettverk eller et område, på samme måte som med porter i forrige avsnitt:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



Her er et eksempel på resultatene vi kan få når vi kjører en skanning på et nettverk:



![nmap-image](assets/fr/26.webp)



resultatene av en Nmap-skanning for å kartlegge flere nettverk



Vi ser flere aktive verter, og hver vertsseksjon begynner med en linje som denne:



```
Nmap scan report for <name> (<IP>)
```



Dette gjør at vi tydelig kan se hvilken host de følgende resultatene refererer til. Den aller siste linjen er også viktig:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Vi vet at Nmap oppdaget fem aktive verter i nettverkene som ble skannet.



#### B. Under panseret: nettverksanalyse via Wireshark



Vi skal nå se nærmere på hva som skjer på nettverksnivå under en nettverksoppdagelse utført via Nmap.



Som vi så i forrige avsnitt, vil Nmap som standard bruke ARP-protokollen til å oppdage tilstedeværelsen av verter i det lokale nettverket:



![nmap-image](assets/fr/27.webp)



aRP-pakker som fanges opp ved skanning av et lokalt nettverk ved hjelp av Nmap og standardalternativer



Den kan dermed oppdage praktisk talt alle verter i det lokale nettverket, siden svaret på en ARP-forespørsel vanligvis kommer fra alle verter som er aktive i nettverket, og ikke virker mistenkelig på noen måte.



For eksterne nettverk bruker Nmap en kombinasjon av teknikker:



![nmap-image](assets/fr/28.webp)



iCMP- og TCP-pakker som fanges opp når du skanner et eksternt nettverk ved hjelp av Nmap og standardalternativene



For å være mer presis bruker Nmap en ICMP-ekopakke (det klassiske tilfellet av pinging) og en ICMP Timestamp-pakke, som vanligvis brukes til å beregne transittider for pakker. Den håper å få svar fra verter på eksterne nettverk.



Men det er mer enn det. Du kan se i Wireshark-opptaket ovenfor at **TCP SYN**-pakker systematisk sendes på TCP/443-portene til alle potensielle verter i nettverkene som skal skannes, i tillegg til **TCP ACK**-pakker på TCP/80-porten.



**Hvorfor sende TCP-pakker til porter som en del av nettverksoppdagelsen?



Ved å sende en SYN-pakke til en gitt port kan Nmap **avgjøre om en tjeneste lytter på den porten**. Hvis en host svarer på en SYN-pakke med en SYN/ACK-pakke, indikerer dette at den er aktiv og at en tjeneste lytter på denne porten. Nmap prøver derfor lykken på denne tjenesten, **selv om det ikke kommer noe svar på pingen**.



Ved å sende en ACK-pakke til en gitt port kan Nmap **avgjøre om det finnes en brannmur på den aktuelle verten**. Hvis en vert svarer på en ACK-pakke med en RST-pakke (Reset), indikerer dette at det sannsynligvis finnes en brannmur på denne verten som blokkerer uoppfordret trafikk. Verten avslører dermed sin tilstedeværelse i nettverket, selv om den ikke har svart på andre forespørsler.



Det er imidlertid viktig å merke seg at brannmurdeteksjon ved hjelp av denne teknikken kanskje ikke er helt pålitelig i alle tilfeller. Noen verter kan generate RST-svar av andre grunner enn tilstedeværelsen av en brannmur, for eksempel på grunn av en bestemt tjeneste- eller operativsystemkonfigurasjon. I tillegg kan moderne brannmurer konfigureres til ikke å svare på denne typen oppdagelsesforsøk.



Vi har nå kommet et godt stykke på vei og kan utføre grunnleggende nettverksoppdagelse. Vi skal nå se på noen flere alternativer som vil gi oss større kontroll over Nmaps oppførsel.



### III. Nettverksoppdagelse uten portskanning med Nmap



Som du kanskje har lagt merke til, utfører Nmap **som standard en portskanning etter at den oppdager en aktiv vert**, noe som gir en enorm mengde pakker og venting på svar til skanningen vår. Hvis du har 5 verter på nettverket ditt, vil Nmap prøve å sjekke statusen til rundt 5000 porter, noe som vil ta lengre tid.



Det er imidlertid mulig å bruke Nmaps alternativer til å utføre **kun en oppdagelse av aktive verter** i et nettverk, uten å oppdage tjenestene deres.



Hvis vi bare vil vite hvilke verter som er tilgjengelige, uten informasjon om tjenestene og portene de eksponerer, kan vi bruke alternativet "-sn" til å utføre **kun en skanning ved hjelp av ICMP Echo (ping) og ARP-forespørsler**. Med andre ord kan du deaktivere portskanning helt og holdent:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Her er resultatet av en Nmap-nettverksoppdagelse utført uten portskanning:



![nmap-image](assets/fr/29.webp)



Resultatet av en nettverksoppdagelse uten portskanning med Nmap.



Vi har allerede nevnt de mulige begrensningene ved å bruke ICMP alene for å finne verter (for eksterne nettverk). Derfor bruker Nmap også noen triks som kan avsløre tilstedeværelsen av en brannmur eller en bestemt tjeneste på verter. Ved hjelp av alternativer kan vi gjenbruke disse triksene og til og med utvide dem, uten å måtte starte på nytt med en fullstendig portskanning av hver vert som oppdages.



For å gjøre dette bruker vi alternativene "-PS" (TCP SYN) og "-PA" (TCP ACK), som lar oss spesifisere portene vi ønsker å koble oss til som en del av vertsoppdagelsen, i tillegg til alternativet "-PP":



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Denne skanningen sørger allerede for at vertsoppdagelsen er litt mer fullstendig enn med standardalternativene.



Vi begynner å få ganske omfattende kommandoer, med flere alternativer. Dette er fordi vi vet hvordan Nmap fungerer og hvilke begrensninger "standardalternativene" har, noe som noen ganger kan føre til at vi kaster bort tid eller går glipp av viktige Elements. Det er hele poenget med å ta seg tid til å mestre det!



For å detaljere alternativene i vår siste bestilling:





- "`-sn`: deaktiverer portskanning for hver aktive vert som oppdages av Nmap.





- "PP": aktiverer ICMP-ekko (ping-skanning) for å finne verter.





- "`-PS <PORT>`": sender en TCP SYN-pakke på de(n) angitte porten(e) for å oppdage eventuelle aktive tjenester som avslører tilstedeværelsen av en vert som ikke har svart på pingen.





- "`-PA <PORT>`": sender en TCP ACK-pakke på porten(e) som er angitt, for å oppdage en eventuell aktiv brannmur som avslører tilstedeværelsen av en vert som ikke har svart på pingen.




I eksemplet ovenfor spesifiserer jeg de portene jeg anser som de mest eksponerte i Nmap-kontekstene mine for "-PS"-alternativet. Disse ulike portene vil deretter bli testet på hver vert, ikke for å se om tjenesten de er vert for virkelig er aktiv, men for å se om dette gjør det mulig for oss å oppdage en vert som ikke har svart på vårt ICMP Echo, men som fortsatt er aktiv (via et svar fra tjenesten eller vertens brannmur).



Her ser du hva som kan ses i et nettverksopptak som er tatt på tidspunktet for en slik skanning, i dette tilfellet et uttrekk på en enkelt målvert:



![nmap-image](assets/fr/30.webp)



pakker sendt av Nmap under avansert nettverksoppdagelse, uten portskanning



Vi finner TCP SYN-pakkene våre, TCP ACK på port TCP/80 og ICMP-ekko. Nmap vil utføre alle disse testene for hver vert som er målet for nettverksoppdagelsesskanningen vår.



### IV. Bruke en fil med ressurser som mål med Nmap



Det kan fort vise seg å være komplisert å spesifisere mål i virkelige informasjonssystemer, som noen ganger kan bestå av dusinvis eller hundrevis av nettverk, subnett og VLAN-er. Derfor er det enklere å bruke en fil som kilde for Nmap enn å spesifisere dem én etter én på kommandolinjen.



Til å begynne med oppretter du en enkel fil som inneholder én oppføring per linje:



![nmap-image](assets/fr/31.webp)



fil som inneholder ett mål (vert eller nettverk) per linje



Deretter kan vi bruke alle Nmap-alternativene vi har sett så langt, og spesifisere alternativet "-iL <sti/fil>":



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Nmap vil da inkludere alle målene i filen vår i skanningen.



Hvis du vil være sikker på at alle målene dine blir tatt i betraktning, kan du bruke alternativet "-sL -n". Nmap vil da bare tolke CIDR-adressene og vertene i filen og vise dem til deg, uten å sende noen pakker over nettverket:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Dette sikrer at listen over verter som skal skannes, er nøyaktig.



Et siste viktig tips jeg gjerne vil dele med dere, gjelder **utelukkelse av verter eller nettverk som en del av en skanning**. Dette behovet for å ekskludere en vert kan være nødvendig i en rekke tilfeller, spesielt hvis vi vil være sikre på at **en sensitiv komponent i informasjonssystemet ikke forstyrres eller forstyrres av skanningen**.



Et vanlig eksempel på slike behov er når en bedrift eier industrielt utstyr (PLS) eller utstyr i helsevesenet. Slikt utstyr er noen ganger dårlig utformet, og slett ikke beregnet på å motta dårlig formaterte pakker, eller for mange av dem. Av åpenbare årsaker knyttet til tilgjengelighet eller forretningsmessig/menneskelig risiko, er det å foretrekke å utelukke dem fra testing.



For å ekskludere IP-adresser eller nettverk fra skanningen kan vi bruke Nmaps "--exclude"-alternativ, for eksempel:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



I dette eksempelet skanner jeg nettverket "192.168.1.0/24", men ekskluderer verten "192.168.1.140" som befinner seg der. Ingen pakker vil bli sendt av Nmap til denne verten. Et annet eksempel med ekskludering av subnett:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



På samme måte skanner jeg det store nettverket "10.0.0.0/16", men nettverket "10.0.100.0/24" vil ikke bli skannet. Igjen anbefaler jeg å bruke alternativet "-sL -n" for å få en veldig klar oversikt over hvilke verter som skal skannes og hvilke som skal utelukkes fra skanningen, spesielt hvis du opererer i en sensitiv kontekst.



### V. Nettverksoppdagelse og portskanning



Vi kan nå kombinere det vi har lært i dette avsnittet med det vi lærte i forrige avsnitt om alternativer for portskanning. Som standard har vi sett at Nmap vil skanne de 1000 hyppigste portene på alle aktive verter den oppdager. Vi har sett hvordan vi kan forhindre dette hvis vi ikke ønsker det, men vi kan kontrollere det fullt ut, og til og med utvide det hvis det passer våre behov.



Følgende kommando vil for eksempel sjekke om det finnes en lyttetjeneste på port TCP/22 på hver skannede vert:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap vil først utføre en nettverksoppdagelse for å liste opp de aktive vertene, og for hver av dem kontrollere at det finnes en tjeneste på port TCP/22.



På samme måte kan vi utføre en fullstendig skanning av alle TCP-porter på alle verter som er oppdaget i nettverket "192.168.0.0/24", med unntak av verten "192.168.0.4", for eksempel:



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Du kan fritt kombinere alle alternativene vi har lært så langt, slik at de passer til dine egne behov.



### VI. Konklusjon



I denne delen har vi sett hvordan du bruker Nmap til å kartlegge nettverket ved hjelp av ulike alternativer. Vi har nå en finjustert forståelse av målene for skanningene våre, samt Nmaps portskanningsatferd og vertsoppdagelsesmetode. Og viktigst av alt, vi vet hva som er Nmaps standardoppførsel og begrensninger, og hvordan vi kan bruke de viktigste alternativene for å komme lenger.



I neste avsnitt ser vi på mekanismene og alternativene for å finne ut hvilke versjoner av tjenester og operativsystemer som skannes av Nmap.




## 6 - Oppdage tjeneste- og operativsystemversjoner med Nmap



### I. Presentasjon



I denne delen skal vi lære hvordan du bruker Nmap til å oppdage og nøyaktig detektere versjonene av tjenester og operativsystemer som brukes av skannede verter. Vi tar en detaljert titt på hvordan Nmap utfører denne oppgaven, samt på verktøyets begrensninger for å bedre forstå og tolke resultatene.



Som vi har sett i tidligere deler av denne veiledningen, vil Nmap som standard ikke se etter hvilken tjeneste som er eksponert på portene den skanner og anser som åpne. Så hvis du lytter til en webtjeneste på port TCP/22, vil Nmap fortsette å rapportere den som åpen, men som en `SSH`-tjeneste. Dette er fordi den bruker en [database] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) lokalt på systemet ditt til å lete etter en relasjon mellom en port/protokoll og navnet på en tjeneste (filen `/etc/services/`).



I de fleste tilfeller vil [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) gi deg riktig informasjon, da det er sjelden man finner slike tilfeller i et produksjonsmiljø. De resterende tilfellene vil imidlertid være situasjoner der en klassisk tjeneste ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP osv.) er eksponert på en ikke-klassisk port (f.eks. 2022 for en SSH-tjeneste), og i slike tilfeller vil Nmap ikke finne en match i sin lokale database, eller en som ikke stemmer overens med virkeligheten, og du vil gå glipp av viktig informasjon.



Heldigvis tilbyr Nmap svært presise alternativer og mekanismer for å finne ut nøyaktig hvilken tjeneste som kan skjule seg bak en åpen port. Det har til og med en database med spørringer og signaturer for å identifisere eksakte teknologier og versjoner. I tillegg til tjenester kan Nmap også identifisere teknologien som brukes, og hvilken versjon den har.



Det er det vi skal se nærmere på i denne delen.



### II. Hvordan oppdage en teknologi eller versjon



#### A. Påminnelse om hvordan du identifiserer en teknologi eller versjon



Identifisering av en teknologi og en versjon innebærer å finne navnet på tjenesten, CMS, applikasjonen eller programvaren som lytter på den aktuelle porten. En nettside administreres for eksempel av et CMS (`WordPress`), kjøres av en webtjeneste (`Apache`, IIS, Nginx) og hostes av en server (Linux eller Windows). Men hvordan vet du hvilken webtjeneste som kjører?



Den klassiske metoden for å finne ut denne informasjonen er _banner grabbing_, som ganske enkelt går ut på å finne ut hvor den aktuelle tjenesten viser denne informasjonen og lese dataene. I standardkonfigurasjonen eller -behandlingen viser tjenestene ofte navnet og til og med versjonen som det første svaret etter en tilkobling.



![nmap-image](assets/fr/32.webp)



vise en versjon så snart en TCP-tilkobling er opprettet av en FTP-tjeneste



Her ser vi at en enkel TCP-tilkobling til denne tjenesten via `telnet` resulterer i en TCP-pakke som inneholder dens teknologi og versjon.



Når du har fått en idé om hvilken type tjeneste du har med å gjøre, kan du også sende spesifikke kommandoer eller forespørsler til den aktuelle tjenesten for å hente ut informasjon fra den. Disse forespørslene/kommandoene kan også sendes blindt (uten å være sikker på at det dreier seg om riktig type tjeneste), i håp om at en av dem vil fremprovosere et svar fra den aktuelle tjenesten.



I andre, mer avanserte tilfeller er det nødvendig å sende spesifikke pakker for å utløse en reaksjon, for eksempel en feilmelding, som gir detaljert informasjon om hvilken versjon eller teknologi som brukes.



Som du kan forestille deg, vil Nmap bruke alle disse teknikkene til å prøve å identifisere den nøyaktige typen tjeneste som finnes på en port, samt navnet på teknologien og versjonen.



#### B. Forstå Nmap-sonderinger og treff



For å utføre alle disse kontrollene på hver port som skannes, bruker Nmap en lokal database som oppdateres ofte (akkurat som binærfilen eller modulene). Dette er en tekstfil på flere tusen linjer: `/usr/share/nmap/nmap/nmap-service-probes`.



Denne filen består av en rekke oppføringer, som alle er organisert rundt to hovedretningslinjer:





- `Probe`: Dette er definisjonen av pakken som Nmap vil sende i et forsøk på å fremprovosere en reaksjon fra tjenesten som skal identifiseres. Tenk på det som et blindt forsøk som _Hello? Guten Tag? Hallo? Um... Buenos Dias kanskje? Så snart den aktuelle tjenesten mottar en probe som den forstår (dvs. som snakker riktig protokoll), vil den svare Nmap, som da vil få bekreftet hvilken type tjeneste det dreier seg om.





- Match": Dette er regulære uttrykk som Nmap bruker på svaret som er innhentet. Hvis en HTTP GET-forespørsel har fremprovosert et svar fra tjenesten, vil den bruke dusinvis av regulære uttrykk på dette svaret for å identifisere tilstedeværelsen av for eksempel ordet `Apache`, `Nginx`, `Microsoft IIS` osv.




Det finnes noen få andre direktiver for spesifikke tilfeller, men de viktigste for å forstå hvordan Nmap fungerer og tilpasse bruken av det, er disse. For å gjøre denne teoridelen mer konkret, her er et eksempel:



![nmap-image](assets/fr/33.webp)



eksempel på en probe i Nmaps `/usr/share/nmap/nmap/nmap-service-probes`-fil



I den første linjen i dette eksempelet ser vi en lettfattelig probe med navnet `GetRequest`. Dette er en TCP-pakke som inneholder en tom HTTP GET-forespørsel til webtjenestens rot ved hjelp av HTTP/1.0, etterfulgt av en linjeskift og en tom linje.



`ports`-linjen forteller Nmap hvilken port denne proben skal sendes til. Dette gjør at du kan prioritere tester og spare tid.



Til slutt har vi to eksempler på `match`. Det første vil for eksempel kategorisere den skannede webtjenesten som `ajp13` hvis det regulære uttrykket i denne linjen samsvarer med det mottatte tjenestesvaret.



For å hjelpe deg med å forstå hvordan prober kan se ut, følger her en liste over noen av probene du finner i denne filen (det er 188 i alt når denne veiledningen skrives).



![nmap-image](assets/fr/34.webp)



eksempel på flere prober som brukes av Nmap og som finnes i filen `/usr/share/nmap/nmap/nmap-service-probes`._



De to første (kalt `NULL` og `GenericLines`) er av spesiell interesse her, ettersom de ganske enkelt sender en tom TCP-pakke eller en pakke som inneholder et linjeskift. Servertjenester annonserer ofte seg selv så snart en tilkobling er mottatt, uten noen spesifikk handling, kommando eller forespørsel fra klienten.



Her er tilfellet med en litt mer kompleks _match_:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



Det eksakte regulære uttrykket står her mellom `m|` og `|`, som avgrenser ethvert regulært uttrykk i denne filen. Ta deg tid til å lese hele dette eksemplet. Du vil legge merke til en markering i det regulære uttrykket: `([\d.]+)`, som brukes til å isolere en versjon. Dette eksemplet definerer også andre Elements som produktnavnet `p/nginx/`, den hentede versjonen `v/$1/` og CPE med versjonen `cpe:/a:igor_sysoev:nginx:$1/`.



CPE (Common Platform Enumeration) er et standardisert notasjonssystem som brukes til å identifisere og beskrive programvare og maskinvare. Dette formatet muliggjør en mer effektiv håndtering av sårbarheter og sikkerhetskonfigurasjoner, og fremfor alt en enhetlig måte å representere dem på, uansett hvilket produkt det er snakk om. Her er to eksempler på CPE: `cpe:/o:microsoft:windows_8.1:r1` og `cpe:/a:apache:http_server:2.4.35`



Her identifiserer vi tydelig typene `o` for operativsystem, `a` for applikasjon, leverandør, produkt og versjoner.



Hvis vi får en _match_ med et av disse regulære uttrykkene, får vi ikke bare navnet på tjenesten, men også versjonen og den nøyaktige CPE-en, noe som gjør det enklere å finne CVE-er som påvirker denne versjonen. Du finner denne informasjonen i Nmaps standardutdata, og du vil se at den er svært nyttig for andre formål som vi skal se nærmere på i noen få avsnitt.



Den nøyaktige syntaksen til _matches_ og, mer generelt, direktivene i filen `/usr/share/nmap/nmap/nmap-service-probes` stopper ikke der, og kan virke ganske kompleks hvis du ikke er vant til å manipulere Nmap og dets resultater. Men du bør i det minste huske på filens eksistens og generelle funksjon, noe som vil komme til nytte senere når du ønsker å forstå eller feilsøke et resultat, tilpasse en skanning eller til og med bidra til Nmap-utviklingen.



### III. Bruke Nmap til å oppdage versjoner



Nå skal vi bruke all denne komplekse _Probe_- og _Match_-mekanikken via en enkel opsjon: `-sV`. Dette forteller ganske enkelt Nmap: prøv å finne ut nøyaktig hvilke tjenester og versjoner av porter du har angitt som åpne.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



Her er et komplett eksempel på resultatet av en slik kommando:



![nmap-image](assets/fr/35.webp)



resultater av Nmaps versjonsdeteksjon av applikasjoner som er eksponert på nettverket



Her ser vi at Nmap har klart å identifisere alle versjonene av nettverkstjenester som er eksponert av dette målet, og viser denne informasjonen i en ny `VERSION`-kolonne. Det er mulig å se ganske presis informasjon, til og med ned til operativsystemet, hvis denne informasjonen er en del av den gjenopprettede signaturen.



For å forstå i detalj hva som skjer under en sårbarhetsskanning, kan vi bruke alternativet `--version-trace`. Dette gir en feilsøkingsmodusvisning som viser _Probe_ som førte til oppdagelsen:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



Resultatet er at vi får mye informasjon å gå gjennom. Prøv å identifisere linjer som begynner med `Service scan Hard match`. Du vil da se linjer som disse:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Vi kan tydelig se hvilke _Probes_ som ble brukt til å oppdage teknologien og versjonen (i dette tilfellet `NULL` og `GetRequest` _Probes_), samt informasjonen som ble hentet.



### IV. Mestringstester og deteksjonsnøyaktighet



Vi skal nå gå tilbake til et direktiv i filen `/usr/share/nmap/nmap/nmap-service-probes` som vi ikke har sett på tidligere:



![nmap-image](assets/fr/36.webp)



probes `rarity`-direktivet i filen `/usr/share/nmap/nmap/nmap-service-probes`._



Dette direktivet brukes til å angi sjeldenheten (dvs. prioritet/sannsynlighet) knyttet til en _Probe_. Denne notasjonen fra 1 til 9 lar deg kontrollere fullstendigheten av analysen som utføres av Nmap når du sender _Probes_. I Nmaps "notasjonssystem" gir en sjeldenhet på 1 informasjon i de aller fleste tilfeller, mens en sjeldenhet på 8 eller 9 representerer et svært spesielt tilfelle, spesifikt for en konfigurasjon eller tjeneste som sjelden er til stede.



For å være tydeligere: I standardtilfellet vil Nmap sende til hver tjeneste som skal identifiseres, de _Probes_ som har en sjeldenhet fra 1 til 7. For å gi deg et bedre inntrykk av fordelingen av _Probes_ etter _sjeldenhet_, her er antallet:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Det kan virke kontraintuitivt, men det er flere `raritet` 8 og 9 enn resten. Dette skyldes nettopp at sjeldenhet 1-prober er generiske og fungerer i de fleste tilfeller, uavhengig av tjenesten (husk `NULL`-proben, som ganske enkelt sender en tom TCP-pakke). Mens de mer komplekse probene er nesten unike for hver tjeneste.



Hvis vi ønsker å styre manuelt hvilke prober vi ønsker å bruke i versjonsskanningen, kan vi bruke alternativet `--version-intensity`. Her er to eksempler:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



For å avslutte med dette emnet, her er et eksempel på _Probe_ 9 og 8:



![nmap-image](assets/fr/37.webp)



eksempler på Probe ved sjeldenhet 8 og 9 i filen `/usr/share/nmap/nmap/nmap-service-probes`._



Disse to _Probes_ detekterer Quake1- og Quake2-servere (videospillet). Interessant for nostalgikeren, men neppe til særlig nytte i hverdagen.



Avhengig av dine behov for presisjon eller hastighet, må du huske at dette "sjeldenhetsprinsippet" eksisterer og kan påvirke resultatet.



### V. Bruke Nmap til å oppdage operativsystemer



Vi skal nå se på hvordan Nmap kan hjelpe oss med å oppdage operativsystemene til verter som skannes og oppdages i et nettverk. For å gjøre dette bruker du Nmaps `-O` (for `OS Scan`).



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



Her er et eksempel på resultatene. Her forteller Nmap oss at det sannsynligvis er et Linux-operativsystem, og gir oss diverse statistikk om den nøyaktige versjonen.



![nmap-image](assets/fr/38.webp)



deteksjon av sannsynligheten for identifisering av et operativsystem ved hjelp av Nmap



For å oppnå dette bruker Nmap en rekke teknikker som fungerer på samme måte som _Probes_ og _Matches_ for teknologi- og versjonsdeteksjon. Hovedforskjellen er at Nmap vil bruke parametere på ganske "lavt nivå" for ICMP, TCP, UDP og andre protokoller. Her er to testeksempler for å oppdage et Microsoft Windows 11-operativsystem:



![nmap-image](assets/fr/39.webp)



eksempler på tester utført av Nmap for å oppdage et Windows 11 OS



Disse testene er svært vanskelige å tolke, og vi skal ikke prøve å forstå dem i dybden i forbindelse med en introduksjon til Nmap. Hvis du ønsker å grave dypere i emnet, er filen som inneholder denne informasjonen `/usr/share/nmap/nmap/nmap-os-db`.



Du må imidlertid være klar over at Nmap ikke kan garantere at operativsystemet blir oppdaget, men at det er mer sannsynlig.



### VI. Konklusjon



I denne delen har vi lært hvordan vi bruker Nmaps alternativer for å oppdage teknologier, versjoner og operativsystemer for skannede verter og tjenester. Vi har nå en god forståelse av hvordan Nmap går frem for å innhente denne informasjonen eksternt. Vi har også gjennomgått alternativene for å administrere ordbruk og testnøyaktighet, samt verktøyets begrensninger på disse områdene.



I neste avsnitt skal vi lære hvordan vi bruker Nmaps NSE-skript til å utføre en sikkerhetsanalyse av informasjonssystemet vårt. Ta deg tid til å lese de siste avsnittene på nytt hvis du trenger det, og ikke nøl med å øve deg og dykke ned i verktøyets innvoller selv for å bedre mestre det vi har lært så langt.




## 7 - Sikkerhetsanalyse: oppdage sårbarheter



### I. Presentasjon



I denne delen lærer vi hvordan vi bruker nettverksskanningsverktøyet Nmap til å oppdage og analysere sårbarheter på målene for skanningene våre. Vi skal se nærmere på de ulike alternativene som er tilgjengelige for å utføre denne oppgaven, og studere grensene for verktøyets muligheter for bedre å kunne forstå og tolke resultatene.



I denne første delen tar vi en titt på Nmaps sårbarhetsskanner, og ser hvordan du bruker de grunnleggende alternativene for sårbarhetsdeteksjon. I de neste avsnittene skal vi se nærmere på hvordan denne funksjonen fungerer, og hvordan den kan tilpasses.



### II. Bruke Nmap til å oppdage sårbarheter



Vi ønsker nå å bruke nettverksskanneren Nmap til å oppdage sårbarheter i tjenestene og systemene i informasjonssystemet vårt. Det betyr at Nmap i tillegg til å finne aktive verter, telle opp eksponerte tjenester og oppdage versjoner og teknologier, også vil lete etter sårbarheter.



For å oppnå dette er Nmap avhengig av NSE-skript (_Nmap Scripting Engine_), som kan ses på som moduler som muliggjør en detaljert tilnærming til testing.



Med de riktige alternativene vil vi be Nmap om å bruke de ulike NSE-skriptene på hver tjeneste som oppdages, slik at vi kan oppdage:





- Konfigurasjonsfeil ;





- Ytterligere og mer avanserte versjoner og OS-oppdagelser ;





- Kjente sårbarheter (CVE-er) ;





- Svake identifikatorer ;





- Karakteristisk Elements for en infeksjon av skadelig programvare ;





- Muligheter for tjenestenekt;





- Og så videre.




Som du ser, utvider NSE-skript Nmaps muligheter betydelig når det gjelder nettverksoperasjoner som kan utføres. Og dette for å utføre langt mer avanserte oppgaver enn noen gang før. Den gode nyheten er at disse funksjonene som vanlig kan brukes enkelt via et alternativ og i en standardkontekst. Det er dette vi skal se i det neste avsnittet.



### III. Eksempel på en sårbarhetsskanning



NSE-skript kan brukes når du bruker Nmap til å skanne en enkelt port på en vert, alle tjenester på denne verten eller alle tjenester som er oppdaget på flere nettverk. Vi kan derfor bruke alternativene vi skal se i alle sammenhengene vi har studert så langt.



For å aktivere sårbarhetsskanning via en Nmap-skanning, må vi bruke `-sC`-alternativet:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Husk at hvis du ikke spesifiserer noe, vil Nmap som standard bare skanne de 1000 vanligste portene. Den vil ikke oppdage sårbarheter på de mer eksotiske portene som målene dine kan eksponere.



Før du tar i bruk denne funksjonaliteten i et produksjonsinformasjonssystem, bør du fortsette å lese veiledningen. I de neste avsnittene skal vi se nærmere på hvordan du bedre kan kontrollere effekten og hvilke typer tester som kjøres.



Ved å gjenbruke det vi har lært tidligere, kan vi for eksempel være mer omfattende og skanne alle TCP-portene til et mål:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Her er resultatet av en Nmap-skanning ved hjelp av NSE-skript:



![nmap-image](assets/fr/40.webp)



eksempel på resultatene av en sårbarhetsskanning på en vert via Nmap._



Her ser vi visning av tilleggsinformasjon som er av interesse i forbindelse med en sårbarhetsanalyse:





- FTP-tjenesten kan brukes anonymt, og er ikke beskyttet av autentisering. NSE-skriptet som står for denne verifiseringen, forteller oss dette, og viser til og med en del av FTP-tjenestens trestruktur. Her ser vi at vi har tilgang til katalogen `C` i Windows-systemet!





- NSE-skriptet som har ansvaret for avansert innhenting av webtjenester, viser sidetittelen, slik at vi får et bedre inntrykk av hva webtjenesten inneholder.





- Vi har også en minianalyse av SMB-tjenestekonfigurasjonen (skriptene `smb2-time`, `smb-security-mode` og `smb2-security-mode`). Informasjonen vises på en litt annen måte, etter resultatet av nettverksskanningen, for å gjøre den lettere å lese. Denne informasjonen indikerer spesielt fraværet av SMB Exchange-signaturer. Denne svakheten i konfigurasjonen gjør at målet kan brukes i et SMB Relay-angrep, en bemerkelsesverdig sikkerhetsbrist som ofte utnyttes i inntrengings-/cyberangrepstester.




Dette er selvfølgelig bare ett eksempel. Nmap har NSE-skript for mange tjenester, rettet mot et bredt spekter av sårbarheter. Vi skal se nærmere på disse mulighetene i neste avsnitt.



Som en avslutning på denne introduksjonen til sårbarhetsskanning får du her en komplett kommando for nettverksoppdagelse, TCP-portskanning, versjons- og sårbarhetsdeteksjon:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



Her er en kommando som begynner å ligne på mer realistiske brukstilfeller for Nmap!



### IV. Forstå Nmaps begrensninger i sårbarhetsskanning



La det være sagt med en gang: Nmap er ikke i stand til å utføre en fullstendig penetrasjonstest av informasjonssystemet ditt, eller simulere en Red Team-operasjon. Det har flere begrensninger som du må være klar over hvis du ikke skal ha en falsk følelse av sikkerhet:





- Begrenset dekning**: Selv om Nmaps NSE-skript er kraftige, kan testdekningen være begrenset sammenlignet med andre spesialiserte verktøy for oppdagelse av sårbarheter. Noen sårbarheter dekkes kanskje ikke av de tilgjengelige NSE-skriptene, for eksempel Active Directory-sårbarheter, eksponering av sensitive data eller mer avanserte tilfeller av sårbare webapplikasjoner.





- Sårbarhetskompleksitet**: Enkelte typer sårbarheter kan være vanskelige å oppdage ved hjelp av NSE-skript på grunn av deres kompleksitet. Sårbarheter som krever kompleks interaksjon med en ekstern tjeneste, kan for eksempel ikke oppdages effektivt av Nmap (som i tilfellet med for mange tillatelser i en fildeling eller en feil i en nettapplikasjon).





- Passiv deteksjon**: Nmap fokuserer primært på aktive skanninger for å oppdage sårbarheter, noe som betyr at den kanskje ikke effektivt oppdager potensielle sårbarheter uten å etablere en aktiv forbindelse med målvertene. Sårbarheter som ikke manifesterer seg under en aktiv skanning, kan derfor bli oversett (som i tilfellet med en kodeinjeksjon i en webapplikasjon).





- Avhengighet av oppdateringer**: Nmaps [database](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) med NSE-skript er i stadig utvikling, men det kan være en forsinkelse mellom oppdagelsen av en ny sårbarhet og tilføyelsen av et tilsvarende skript til Nmap. Derfor er det ikke sikkert at Nmap alltid er oppdatert med de nyeste sårbarhetene.





- Falske positive og falske negative resultater**: Som med alle andre sikkerhetsverktøy kan Nmaps NSE-skript produsere falske positive (falske varsler om sårbarheter) eller falske negative (reelle sårbarheter som ikke oppdages). Dette er noe du bør ha i bakhodet når du analyserer Nmap-resultater.




Det er derfor viktig å forstå hva Nmap gjør og ikke gjør, og å vite hvordan man tolker resultatene. Vi har i denne veiledningen sett at standardalternativer kan føre til at vi går glipp av viktige Elements som kan avdekkes ved forsiktig bruk.



Enten du er systemadministrator, sikkerhetsingeniør eller CISO, kan du bruke Nmap til å få oversikt over sikkerhetsstatusen til et informasjonssystem. Dette er et viktig første skritt i arbeidet med å sikre et system, og det kan utføres regelmessig av IT-teamet. Det bør imidlertid ikke erstatte inngripen og råd fra [cybersikkerhets]eksperter (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), som vil være i stand til å avdekke svakheter på en langt mer omfattende måte enn Nmap.



### V. Konklusjon



I denne første delen av modul 3 har vi introdusert sårbarhetsskanning via Nmap. Vi vet nå hvordan vi bruker hovedalternativet til å utføre denne oppgaven, men vi kjenner også begrensningene i øvelsen. I neste avsnitt skal vi se nærmere på denne funksjonaliteten, og vi skal bruke NSE-skript for å tidoble Nmaps kapasitet.



## 8 - Bruk av Nmaps NSE-skript



### I. Presentasjon



I denne delen tar vi en grundig titt på NSE-skript (_Nmap Scripting Engine_). Vi ser spesielt på hvorfor de er en av de store styrkene ved dette verktøyet, hvordan de fungerer og hvordan du kan bla gjennom og bruke de mange eksisterende skriptene.



Denne delen er en videreføring av den forrige veiledningen, der vi lærte å bruke Nmaps funksjoner for sårbarhetsskanning på en grunnleggende måte. Vi skal nå se nærmere på hvordan [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) fungerer i denne sammenheng, slik at vi igjen kan utføre mer presise og kontrollerte skanninger.



### II. Konseptet med Nmap NSE-skript



Med Nmaps NSE-skript kan du utvide funksjonene på en svært fleksibel måte. De er skrevet i LUA, et skriptspråk som er enklere å håndtere og få tilgang til enn C eller C#, som brukes av Nmap. Fordelen med å bruke et LUA-skript sammen med Nmap i stedet for et frittstående verktøy er at vi kan dra nytte av Nmaps utførelseshastighet og standardfunksjoner (verts-, port- og versjonsoppdagelse osv.).



Skriptene er organisert etter kategori, og et enkelt skript kan tilhøre mer enn én kategori:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Teknisk sett er kategoriene som et skript tilhører, angitt direkte i koden.



![nmap-image](assets/fr/41.webp)



nSE-skriptkategorier `ftp-anon`._



Dette eksemplet viser en del av koden til NSE-skriptet `ftp-anon.nse`, som vi så kjørt i forrige avsnitt.



### III. Liste over eksisterende NSE-skript



Som standard er Nmaps NSE-skript plassert i katalogen `/usr/share/nmap/scripts/`, uten noen spesifikk trestruktur eller hierarki. Her er en oversikt over innholdet i denne katalogen:



![nmap-image](assets/fr/42.webp)



henter ut innholdet i katalogen `/usr/share/nmap/scripts/` som inneholder NSE-skript._ _



Denne katalogen inneholder over 5000 NSE-skript. I de fleste tilfeller inneholder den første delen av skriptnavnet protokollen eller kategorien det tilhører. Dette gjør det mulig å sortere listen, for eksempel hvis vi ønsker å liste opp alle skript som er rettet mot FTP-tjenesten:



![nmap-image](assets/fr/43.webp)



liste over NSE Nmap-skript med navn som begynner med `ftp-`._



Nmap tilbyr egentlig ikke noe alternativ for å bla gjennom og liste opp NSE-skript; du kan bruke kommandoen `--script-help` etterfulgt av navnet på en kategori eller et ord:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



Resultatet blir imidlertid navnet på hvert skript og en beskrivelse av det, noe som ikke er optimalt hvis søket gir flere titalls skript:



![nmap-image](assets/fr/44.webp)



resultatet av å bruke Nmaps `--script-help`-kommando



Etter min mening er den mest effektive metoden å bruke de klassiske Linux-kommandoene i katalogen `/usr/share/nmap/scripts/`:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Bla gjerne gjennom koden til de modulene som passer for deg, for å få en bedre forståelse av hvordan et NSE-skript fungerer.



### IV. Bruke Nmaps NSE-skript



Nå skal vi lære hvordan vi utfører sårbarhetsskanninger ved å nøye velge ut de NSE-skriptene vi er interessert i.



#### A. Velg skript etter kategori



Til å begynne med kan vi velge å kjøre alle skript som tilhører en bestemt kategori. Vi må angi denne kategorien eller disse kategoriene til Nmap med argumentet `--script <category>`:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Denne første kommandoen tilsvarer kommandoen `nmap -sC`. Som standard vil Nmap velge skript i kategorien `default`, men det er bare for argumentets skyld. Den neste kommandoen vil for eksempel bruke alle skriptene i kategorien `discovery`:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Som vi har sett, lar noen kategorier oss raskt identifisere hva de relaterte NSE-skriptene gjør (`discovery`, `vuln`, `exploit`), mens andre definerer risikonivået, deteksjonsnivået eller stabiliteten til den utførte testen. Hvis vi befinner oss i en sensitiv kontekst og ikke har god oversikt over de ulike handlingene som utføres av skriptutvalget vårt, kan vi velge å kombinere valgene for å velge bare de skriptene som er i kategoriene `discovery` og `safe`:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Hvis du absolutt og eksplisitt ønsker å ekskludere skript fra kategoriene `dos` og `intrusive`, kan du bruke følgende notasjon:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Vær oppmerksom på at hvis du spesifiserer ekskluderingsbetingelser som ovenfor, vil alle andre kategorier som ikke er eksplisitt ekskludert, bli brukt. For å være mer rettferdig kan vi for eksempel spesifisere



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Her er noen eksempler på hvordan du kan håndtere NSE-skript etter kategori, spesielt når du bruker Nmap til sårbarhetsanalyse i virkelige sammenhenger.



#### B. Velg skript som en enhet



Vi kan også velge å utføre en enkelt spesifikk test under en analyse, en test som tilsvarer et NSE-skript. For å gjøre dette må vi spesifisere navnet på skriptet i parameteren `-script <name>`. Vi tar skriptet `ftp-anon.nse` som eksempel:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



Da har vi et veldig presist resultat:



![nmap-image](assets/fr/45.webp)



resultat av å bruke NSE `ftp-anon`-skriptet på en FTP-port via Nmap._



Vi ser resultatet av å kjøre `ftp-anon`-skriptet på port 21, og ingen andre porter, fordi vi spesifiserte alternativet `-p 21`. Vi kunne også ha utført en grunnleggende portskanning og kjørt NSE-skriptet `ftp-anon` bare på de FTP-tjenestene som ble oppdaget:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Nmap ville dermed også ha utført denne anonyme tilkoblingstesten hvis den hadde funnet en FTP-tjeneste på en annen port.



Hvis du vil ha en kort beskrivelse av hva et NSE-skript gjør, kan du bruke `--script-help`-alternativet som er nevnt ovenfor:



![nmap-image](assets/fr/46.webp)



hjelp til å vise resultat for NSE-skriptet `sshv1`._



Kort sagt kan vi nok en gang gjenbruke alle alternativene, tjenestene, versjonene og teknologiene vi har brukt til nå!



#### C. Håndtering av skriptargumenter



Når du bruker Nmap, vil du støte på enkelte NSE-skript som krever inngangsargumenter for å fungere korrekt. Vi skal nå se på hvordan du kan sende argumenter til disse skriptene via Nmaps alternativer.



La oss ta skriptet `ssh-brute` som eksempel, som lar deg utføre et brute force-angrep på SSH-tjenesten.



Et klassisk brute force-angrep består i å teste flere passord (noen ganger millioner) i et forsøk på å autentisere seg til en bestemt konto. Ved å prøve så mange passord satser angriperen på sannsynligheten for at brukeren har brukt et svakt passord i passordordboken som brukes til angrepet.



Dette skriptet har "standardalternativer", som vi kan tilpasse slik at de passer til vår kontekst. I forbindelse med dette angrepet kan vi for eksempel gi Nmap listen over brukere og passordordboken som skal brukes. Så vidt jeg vet, er det ikke mulig å enkelt liste opp argumentene som kreves for et skript, så den mest pålitelige måten er å besøke den offisielle Nmap-nettsiden. En direkte lenke til dokumentasjonen for et NSE-skript kan fås som svar på `--script-help`-alternativet:



![nmap-image](assets/fr/47.webp)



resultat av å vise hjelp for NSE `ssh-brute`-skriptet med en lenke til nmap.org._ _



Ved å klikke på den angitte lenken kommer vi til denne nettsiden på nettstedet [https://nmap.org](https://nmap.org/):



![nmap-image](assets/fr/48.webp)



liste over argumenter som kan sendes til Nmaps NSE-skript `ssh-brute`



Her har vi en klar oversikt over argumentene som kan brukes, der de viktigste i vår sammenheng er `passdb` (fil som inneholder en liste med passord) og `userdb` (fil som inneholder en liste med brukere). Dokumentasjonen her refererer til interne Nmap-biblioteker, ettersom disse brute force-mekanismene og tilhørende opsjoner er gjensidige for å kunne brukes på samme måte i flere skript (`ssh-brute`, `mysql-brute`, `mssql-brute`, osv.) og derfor vil ha mer eller mindre de samme argumentene:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Som du kan se i denne siste kommandoen, kan vi spesifisere de nødvendige argumentene til et Nmap-skript ved hjelp av `--scripts-args key=value,key=value`-alternativet. Her er et mulig resultat av Nmap-utdataene når du utfører en SSH-brute force via NSE-skriptet `ssh-brute`:



![nmap-image](assets/fr/49.webp)



resultat av SSH-bruteforce-kjøring via Nmap._ _



Som du kan se, er informasjonen som genereres av NSE-skript, foranstilt med `NSE: [skriptnavn]` i den interaktive utdataen (terminalutdata), noe som gjør det lettere å finne den. I den vanlige visningen av Nmap-resultater har vi bare et sammendrag som angir om det er oppdaget svake identifikatorer (inkludert passord, husk det).



For å ta ting et skritt videre, og for å minne deg på at alt dette kan brukes i tillegg til alle alternativene vi allerede har sett på, kommer her en kommando som vil oppdage `10.10.10.0/24`-nettverket, skanne de 2000 mest frekvente TCP-portene og kjøre et anonymt tilgangssøk på FTP-tjenester og en brute force-kampanje på SSH-tjenester:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Dette er bare ett eksempel på de mange tilgjengelige skriptene og deres alternativer. Men nå har vi fått et bedre inntrykk av hvordan vi kan bruke NSE-skript, om de krever argumenter, og hvordan vi kan sende disse argumentene til Nmap.



### V. Konklusjon



I denne delen har vi lært hvordan du kan bruke Nmaps NSE-skript til å utføre ulike oppgaver. Jeg inviterer deg til å ta deg tid til å oppdage de ulike skriptkategoriene og skriptene i seg selv, for å se hvor mange tester de kan automatisere.



I flere seksjoner har vi nå samlet mer eller mindre avanserte alternativer for oppdagelse, skanning og opptelling. Nå bør du være klar over at Nmaps utdata og resultatvisning begynner å bli ganske omfattende, noen ganger til og med for omfattende for terminalen vår. I neste avsnitt skal vi lære hvordan vi kan mestre denne utdataen, særlig ved å lagre den i filer i ulike formater.






## 9 - Administrere utdata fra Nmap




### I. Presentasjon



I dette avsnittet skal vi se nærmere på utdataene som produseres av Nmap, og spesielt på de ulike alternativene for å formatere disse utdataene. Vi skal se at Nmap kan produsere flere utdataformater som passer til ulike behov, og at dette også er en av de store styrkene ved dette verktøyet.



Som standard tilbyr Nmap en detaljert visning av resultatene av skanningene og testene som utføres. Dette inkluderer skannede verter og tjenester, de som oppdages som tilgjengelige, spesifikke åpne porter, deres status og versjon. I tillegg er detaljer om NSE-skript også tilgjengelig i terminalutdataene. Selv med tydelig formatering av informasjonen kan denne utdataene imidlertid fort bli omfangsrike, noe som kan gjøre det vanskelig å finne presis informasjon i resultatene.



### II. Beherske Nmap-utdataformater



#### A. Lagre skanneresultatene i en tekstfil



For å gjøre ting enklere, gjør [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) det veldig enkelt å lagre utdataene i en tekstfil. Dette kan være nyttig for arkivering, sammenligning med andre tester, men også for å bla gjennom utdataene med spesialiserte tekstbehandlingsverktøy eller skriptspråk, for eksempel Sublime text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed osv. For å lagre Nmaps standardutdata i en tekstfil kan vi bruke alternativet `-oN <filnavn>` (N-en i "normal"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Det er ingen overraskelse, for Nmap vil vise den vanlige standardutdataen i terminalen vår, men også i den angitte filen.



#### B. generate Nmap-utdata i komprimert format



Det finnes også et annet utdataformat i "tekst"-stilen som enkelt kan tolkes av et menneske: "greppable"-formatet.



Dette formatet ble laget for å gi en "komprimert" visning av Nmap-utdataene, strukturert på en måte som gjør det lettere å behandle dem med verktøy som `grep`. La oss se på et eksempel på denne typen utdata:



![nmap-image](assets/fr/50.webp)



nmap-nettverksskanning og utdata i "greppbart" format



Her har jeg utført en nettverksoppdagelse samt en portskanning og en analyse av teknologier og versjoner på et /24-nettverk, og deretter lagret utdataene i en fil i "greppbart" format. Jeg ender opp med en fil som inneholder 2 linjer per aktiv vert:





- Den første linjen forteller meg at den og den verten er _Opp_;





- En annen linje forteller meg hvilke porter som har blitt skannet, hvilken status de har, og hvilken teknologi og versjonsinformasjon som er hentet i et veldig spesifikt format: `<port>/<status/<protokoll>//<tjeneste>//<versjon>/,``




Denne formateringen med et fast skilletegn gjør det mulig å behandle dataene raskt med tekstbehandlingsverktøy som `grep`, eller skript- og programmeringsspråk. Følgende kommando gjør det for eksempel mulig for meg å enkelt hente ut informasjon om verten `10.10.10.5` i tilfelle en stor skanning utført av Nmap, hvis utdata ville være vanskelig å bla gjennom:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



Omvendt kan jeg også enkelt liste opp alle verter som har port 21 åpen, siden porter og IP står på samme linje:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



For å generate slik utdata, må vi bruke `-oG <filnavn>.gnmap`-alternativet (G-en i "grep"). Av gammel vane bruker jeg `.gnmap` som filtype for en slik fil, men du kan bruke den du vil:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Dette formatet kan brukes til en rekke formål og er spesielt nyttig for rask skripting/sortering. Likevel har det en tendens til å bli forlatt til fordel for formatet vi skal se nærmere på.



merk: `-oG` greppable-formatet har offisielt blitt forkastet siden Nmap 7.90. Det kan fortsatt brukes av kompatibilitetshensyn. Det kan fortsatt brukes for kompatibilitetsformål, men det anbefales at du bruker XML- eller normalformatet for all utvikling eller automatisert parsing



#### C. XML-format for Nmap-utdata



Det siste formatet som er verdt å nevne i denne veiledningen, er XML. I motsetning til de to foregående formatene er dette formatet ikke utviklet for å leses av mennesker, men av andre verktøy eller skript.



XML (_eXtensible Markup Language_) er et markeringsspråk som brukes til å lagre og transportere data, og som tilbyr en hierarkisk struktur via egendefinerte tagger.



I Nmap brukes XML-formatet til å generate detaljerte rapporter om utførte skanninger, inkludert informasjon om verter, porter og oppdagede sårbarheter, samt tilleggsinformasjon som ikke vises i standardutdataene fra Nmap.



For å generate en utdatafil i XML-format, må vi bruke `-oX`-alternativet ("O" fra "XML"):



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



Resultatet er Nmaps standardutdata i terminalen, samt en fil i XML-format i den aktuelle katalogen.



XML-formatet er selvfølgelig ikke utformet for å kunne leses og tolkes av mennesker. Hvis du ønsker å utføre skripting eller automatisert analyse på dette formatet av Nmap-utdata, må du likevel ha en idé om hvilke tagger og strukturer som brukes. Her er for eksempel en del av innholdet i XML-filen som er opprettet av Nmap, som viser skanneresultatene for 1 vert:



![nmap-image](assets/fr/51.webp)



eksempel på en XML-oppføring for 1 vert under en Nmap-skanning



Det er mye informasjon her, og vi er spesielt interessert i de to åpne portene:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Vi forstår at dette formatet vil gjøre det enklere å analysere resultatene automatisk, ettersom hver del av informasjonen er ordnet i en egen, navngitt tagg eller attributt. Vi finner spesielt en opplysning som vi ikke har støtt på før: CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Vi nevnte kort CPE i avsnitt 2 i modul 2, og denne informasjonen bestemmes i treff under versjonsdeteksjon. Nmap bruker sine mekanismer for tjeneste-, teknologi- og versjonsdeteksjon for å finne den tilknyttede CPE-en.



Dette gjør at vi kan gjenbruke denne informasjonen i databasene og applikasjonene som bruker den. Jeg tenker spesielt på NVD-databasen, som refererer til CVE-er. For hver CVE inneholder den CPE-ene som er berørt av sårbarheten. Her er et eksempel på en CVE som gjelder `a:microsoft:internet_information_services:7.5` fra NVD-databasen:



![nmap-image](assets/fr/52.webp)



forekomst av en CPE i detaljene til en CVE i NVD-databasen



Vi har nå en bedre forståelse av fordelene med dette formatet, som gir en svært tydelig informasjonsstruktur og inneholder alle data som er samlet inn eller behandlet av Nmap.



Som en refleks lagrer jeg systematisk Nmap-skanningene mine i alle tre formatene samtidig. Dette er mulig ved hjelp av `-oA <name>` ("A" for "All"), som oppretter en `<name>.nmap`-fil, en `<name>.xml`-fil og en `<name>.gnmap`-fil. På denne måten er jeg sikker på at jeg ikke går tom for noe når jeg trenger å gå tilbake til resultatene.



Med disse tre formatene bør du ha alt du trenger for å lagre og til slutt behandle Nmap-resultater på en automatisert måte. Vi kommer til å bruke XML-formatet igjen i neste avsnitt, når vi ser på bruk av Nmap sammen med andre sikkerhetsverktøy.



#### III. Generering av en HTML-rapport fra en Nmap-skanning



XML-formatet byr på mange muligheter, ikke minst som grunnlag for å generere en rapport i HTML-format, som vil være mer visuelt tiltalende å bla gjennom.



For å omforme en Nmap-fil i XML-format til en webside bruker vi verktøyet `xsltproc`, som vi må installere først:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Når dette verktøyet er installert, er det bare å gi det XML-filen som skal konverteres, og navnet på HTML-rapporten som skal genereres:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Resultatet er at hele skanningen blir strukturert på en fin måte, med til og med noen farger og klikkbare lenker i innholdsfortegnelsen!



![nmap-image](assets/fr/53.webp)



utdrag fra en Nmap-skannerapport i HTML-format generert av xsltproc._



XML-filen som lagres av Nmap, inneholder en referanse til en annen fil i XSL-format:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



Konvertering til HTML er derfor en funksjon som tilbys og tilrettelegges av Nmap, og `xsltproc` er et vanlig og anerkjent verktøy for å utføre denne oppgaven (som ikke kommer fra Nmap-verktøypakken).



XSLT (_Extensible Stylesheet Language Transformations_) er en delmengde av XSL som gjør det mulig å vise XML-data på en webside og "transformere" dem, parallelt med XSL-stiler, til lesbar, formatert informasjon i HTML-format.



kilde: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_ _ [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



Informasjonsnivået i rapporten tilsvarer Nmaps XML-format og er høyere enn i standard terminalutdata (_interactive output_).



### IV. Administrere Nmaps ordrikhetsnivå



Vi skal nå ta en titt på noen alternativer for Debugger Nmap eller for å spore fremdriften.



Det første alternativet vi bør nevne er `-v`, som øker Nmaps ordrikhet. Her er et eksempel:



![nmap-image](assets/fr/54.webp)



nmapps verbose-utdata ved hjelp av `-v`._-alternativet



Ved skanning av mange verter og porter vil terminalutdataene bli vanskelige å utnytte på grunn av mengden informasjon som vises. Av denne grunn bør dette alternativet brukes i kombinasjon med de tidligere nevnte alternativene, som lar deg lagre Nmaps standardutdata i en fil. Informasjon relatert til bruk av verbosity vil ikke bli inkludert i denne utdatafilen. Som du kan se av eksemplet ovenfor, gjør denne verbositeten at du kan spore Nmaps handlinger og funn på en tydelig og direkte måte. For lengre skanninger der datavisningen kan ta lang tid, unngår du å være blind for Nmaps nåværende aktivitet og å vite at ting går fremover og i hvilket tempo. Hvis du vil øke ordrikheten ytterligere, kan du bruke alternativet `-vv`.



For å følge Nmaps aktivitet under skanningen ytterligere, kan du bruke alternativet `--packet-trace`. Med `-v`-alternativet får vi en direkte logg over alle åpne porter som oppdages av Nmap, mens vi med dette alternativet får en logglinje for hver pakke som sendes til en port. Dette gir naturligvis en svært ordrik utdata, men gjør det mulig å overvåke Nmaps aktivitet i detalj:



![nmap-image](assets/fr/55.webp)



detaljert overvåking av Nmap-aktivitet via `--packet-trace`._



Heller ikke denne informasjonen vil bli registrert i utdatafilen som produseres av Nmap hvis alternativene `-oN`, `-oG`, `-oX` eller `-oA` brukes.



Til slutt tilbyr Nmap også to feilsøkingsalternativer: `-d` og `-dd`. Disse alternativene fungerer på samme måte som `-v`, men legger til ytterligere teknisk informasjon, for eksempel et sammendrag av tekniske parametere i starten av skanningen:



![nmap-image](assets/fr/56.webp)



tidsalternativer vises i Nmapps feilsøkingsvisning



I de neste avsnittene skal vi se nærmere på hva "Timing"-alternativene er, og hvorfor det er verdt å kjenne til dem.



Til slutt, hvis du bare vil ha en grunnleggende, syntetisk oversikt over fremdriften i Nmap-skanningen, kan du bruke alternativet `--stats-every 5s`. "5s" her betyr 5 sekunder og kan endres for å passe til dine behov. Dette er frekvensen vi vil motta tilbakemeldinger fra Nmap om fremdriften:



![nmap-image](assets/fr/57.webp)



informasjon som vises av Nmaps `--stats-every`-alternativ



Vi kan få en prosentandel av fremdriften, samt en indikasjon på hvilken fase den befinner seg i: vertsoppdagelsesfasen via [ping] (https://www.it-connect.fr/le-ping-pour-les-debutants/), oppdagelsesfasen av eksponerte TCP-porter osv. Denne informasjonen kan også hentes ut i terminalutdataene ved å trykke på "Enter" under en skanning.



Nmap er imidlertid ikke særlig god til å anslå hvor lang tid en oppgave vil ta, ikke minst fordi den ikke vet på forhånd hvor mange verter og tjenester den må skanne.



### V. Konklusjon



I denne delen har vi sett på en rekke muligheter for å lagre Nmap-skanneresultater i ulike filformater. Dette vil være svært nyttig, ettersom skanneresultater i realistiske sammenhenger kan ta opp hundrevis eller tusenvis av linjer! Vi har også sett hvordan du kan øke Nmaps verbositetsnivå for feilsøkingsformål eller for å få en rapport om fremdriften i skanningen.



XML-formatet vil være spesielt nyttig i neste avsnitt, der vi skal se på noen få verktøy som kan arbeide med Nmap-resultater.




## 10 - Bruk av Nmap sammen med andre sikkerhetsverktøy



### I. Presentasjon



I denne delen tar vi en titt på noen av de klassiske bruksområdene for Nmap sammen med andre gratis sikkerhetsverktøy med åpen kildekode. Vi vil spesielt bruke det vi har lært i de foregående avsnittene til å forbedre Nmaps kraft og effektivitet ytterligere.



Muligheten til å lagre Nmap-skanneresultater i XML gjør dataene kompatible med en rekke andre verktøy. Siden nesten alle programmerings- og skriptspråk i dag har biblioteker som kan parse XML, gjør dette det mye enklere å behandle disse dataene. En rekke verktøy, særlig de som er rettet mot offensiv sikkerhet, har funksjoner for å behandle XML-formatet som genereres av Nmap. La oss ta en nærmere titt.



Jeg kommer til å nevne noen få offensive verktøy uten å gå i detalj på hvordan de brukes eller hvordan de fungerer. Jeg forutsetter at leseren er kjent med den grunnleggende bruken av dem, og at de allerede er operative. Denne delen vil være av særlig interesse for fagpersoner innen [cybersikkerhet] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), personer under opplæring eller de som har bestemt seg for å fordype seg i emnet.



### II. Importere Nmap-resultater til Metasploit



Det første verktøyet vi skal se på for gjenbruk av Nmap-data i offensiv sikkerhets- og sårbarhetsforskning, er Metasploit.



Metasploit er et rammeverk for utnyttelse og angrep. Det er en gratis løsning og et anerkjent verktøy som inneholder et stort antall moduler skrevet i Ruby eller Python. Disse gjør det mulig å utnytte sårbarheter, utføre angrep, generere bakdører, administrere callbacks (C&C eller Communication and Control-funksjoner) og bruke alt på en enhetlig måte.



Dette velkjente og mye brukte driftsrammeverket kan fungere med en postgreSQL [database] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) der verter, porter, tjenester, autentiseringsinformasjon og mer er lagret.





- Offisiell Metasploit-dokumentasjon: [https://docs.metasploit.com/](https://docs.metasploit.com/)




Det er her Nmap og Nmap-utdataene kommer inn i bildet, ettersom XML-formatet til Nmap-utdataene enkelt kan importeres til Metasploits database for å fylle ut databasen med verter og tjenester, som deretter raskt kan utpekes som mål for det ene eller det andre angrepet.



Når jeg er inne i det interaktive Metasploit-skallet mitt, begynner jeg med å opprette et arbeidsområde, et slags rom som er spesifikt for dagens miljø:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Når arbeidsområdet mitt er opprettet, må vi kontrollere at kommunikasjonen med databasen fungerer:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Til slutt kan vi bruke Metasploit-kommandoen `db_import` til å importere Nmap-skanningen vår i XML-format:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Her er resultatet av å utføre alle disse kommandoene:



![nmap-image](assets/fr/58.webp)



importere en Nmap-skanning i XML-format til Metasploit-databasen



Her kan du se at hver vert er importert, sammen med tjenestene. Disse dataene kan deretter vises via kommandoen `services` eller `services -p <port>` for en bestemt tjeneste:



![nmap-image](assets/fr/59.webp)



liste over tjenester importert fra XML-filen til Metasploit-databasen



Til slutt kan vi raskt og enkelt gjenbruke disse dataene i en modul takket være `-R`-alternativet, som vil "konvertere" listen over tjenester som er innhentet som input for `RHOSTS`-direktivet, som brukes til å spesifisere målene for angrepet som skal utføres. Her er et eksempel med modulen `ssh_login`, som gjør det mulig å utføre et brute force-angrep på [SSH]-tjenester (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



bruk alternativet `services -R` for å importere tjenestene som er angitt som mål for angrepet



Dette er bare et lite eksempel på hva som kan gjøres med Nmap-data i Metasploit, men det gir deg en liten idé om hvor raskt og enkelt denne informasjonen kan gjenbrukes som en del av en penetrasjonstest, sårbarhetsskanning eller cyberangrep. Det er også verdt å nevne at Nmap kan kjøres direkte fra Metasploit for å importere resultatene til databasen (kommandoen `db_nmap`), et annet interessant tema å dekke!



### III. Bruke Nmap med Aquatone-nettskanneren



Det andre verktøyet jeg vil introdusere i denne delen om gjenbruk av Nmap-resultater for offensiv sikkerhets- og sårbarhetsanalyse, er Aquatone.



Aquatone er en webskanner som er utviklet for effektiv utforskning av webapplikasjoner i et nettverk. Den tilbyr avanserte funksjoner for oppdagelse av webtjenester, identifisering av underdomener, portanalyse og fingeravtrykk av webapplikasjoner. Alt presenteres klart og tydelig i HTML-, JSON- og tekstrapporter for enkel analyse av websikkerhet.



I likhet med Metasploit kan Aquatone behandle Nmaps XML-format direkte og bruke det som mål for skanning. Den kan spesielt trekke ut kun de vertene og tjenestene som er av interesse (webtjenester) fra alle dataene en Nmap-rapport kan inneholde.





- Verktøylink: [Github - Michenriksen/aquatone] (https://github.com/michenriksen/aquatone)




For å bruke Nmaps XML-utdata med Aquatone, sender du ganske enkelt XML-filen i en pipe som vil bli brukt av Aquatone. Her er et eksempel:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Der Aquatone normalt utfører portoppdagelse på verter for å finne nettjenester, vil den i denne sammenhengen kun stole på resultatene fra Nmap, som allerede har utført denne operasjonen, noe som sparer tid:



![nmap-image](assets/fr/61.webp)



bruker Nmap-resultater i XML-format med `aquatone`._



Her er et utdrag fra rapporten som Aquatone har utarbeidet:



![nmap-image](assets/fr/62.webp)



eksempel på en `aquatone`-rapport



Selv bruker jeg ofte Aquatone til å få en rask oversikt over hvilke typer nettsteder som finnes i nettverket, særlig takket være skjermbildefunksjonen.



Også her er det tidsbesparende å ha en komplett Nmap-rapport i XML-format, og det gjør det enkelt å gjenbruke den i et annet verktøy.



### IV. Konklusjon



Disse to eksemplene viser tydelig at XML-formatet til Nmap gjør det enkelt for andre verktøy å bruke resultatene, siden det er et strukturert og brukervennlig dataformat. Det finnes mange andre verktøy som kan behandle disse resultatene, for eksempel automatiserte rapporteringsverktøy, grafiske fremstillinger eller mer komplekse, proprietære sårbarhetsskannere.



Du kan selvfølgelig også utvikle dine egne skript og verktøy i Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) eller et hvilket som helst annet språk med et XML-parsingbibliotek for å manipulere og gjenbruke Nmap-resultatdata slik du ønsker.



Med dette avsnittet avslutter vi opplæringsmodulen om mer avansert bruk av Nmap, spesielt for sårbarhetsskanning ved hjelp av NSE-skript.



Den neste delen av veiledningen vil blant annet fokusere på noen flere, mer tekniske beste fremgangsmåter og tips om de spesifikke skanningene som Nmap kan utføre. Vi tar også en titt på alternativer for optimalisering av skanneytelsen, som er spesielt nyttige når du skanner store nettverk.




## 11 - Forbedre ytelsen ved nettverksskanning



### I. Presentasjon



I dette kapittelet lærer vi hvordan vi kan optimalisere hastigheten på nettverksskanninger utført med Nmap ved hjelp av ulike spesifikke alternativer. Vi lærer mer om hvordan Nmap fungerer innvendig, fra _timeout_-styring til verktøyets forhåndslagrede konfigurasjoner.



Nå som vi har sett nærmere på Nmaps funksjoner, skal vi ta fatt på beistet og dets kraft. Hvis du noen gang har brukt verktøyet på store nettverk, har du sikkert lagt merke til at noen skanninger kan ta lang tid, til tross for verktøyets kraft. Og med god grunn: En enkel `nmap`-kommando med noen få alternativer kan generate millioner av pakker rettet mot hundretusener av potensielle systemer og tjenester.



I tillegg kan enkelte nettverksutstyrskonfigurasjoner med vilje pålegge en lavere hastighet (antall pakker per sekund), med risiko for å avvise pakkene dine eller forby IP Address av sikkerhetsmessige årsaker.



Avhengig av konteksten kan det lønne seg å prøve å optimalisere alt dette, som vi skal se i dette kapittelet.



Uansett kan du sjekke standardverdiene for parameterne vi skal se på, samt om alternativene du skal bruke, er korrekt tatt i betraktning, via Nmap debug (alternativ `-d` som vi så i et tidligere kapittel):



![nmap-image](assets/fr/63.webp)



se Timing-alternativer via Nmaps `-d`-alternativ



### II. Administrere hastigheten på Nmap-skanninger



#### A. Håndtering av parallellisering



Som standard bruker Nmap parallellisering i skanningene for å optimalisere dem, og alle parametrene den bruker kan endres via ulike alternativer. Det er imidlertid ganske sjelden at det er nødvendig å endre disse parameterne, så vi vil ikke gå nærmere inn på dem i denne veiledningen:





- `--min-hostgroup/max-hostgroup <størrelse>`: størrelsen på parallelle vertsskanngrupper.





- `--min-parallellisme/maks-parallellisme <numprobes>`: parallellisering av Probes.





- `--scan-delay/--max-scan-delay <time>`: justerer forsinkelsen mellom sonder.




Bare vit at de finnes og kan brukes.



#### B. Håndtering av antall pakker per sekund



Som standard justerer Nmap selv antall pakker per sekund som sendes i henhold til nettverksresponsen. Det er imidlertid mulig å tvinge frem denne innstillingen ved å definere den høyeste og/eller laveste verdien som skal følges når det gjelder antall pakker per sekund. Denne innstillingen gjøres ved hjelp av opsjonene `--min-rate <number>` og `--max-rate <number>`, der `number` representerer et antall pakker per sekund. Eksempel:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Med disse alternativene kan du justere hastigheten på skanninger i henhold til dine spesifikke behov, enten for å øke hastigheten på prosessen eller for å begrense båndbredden som brukes. Det er sistnevnte tilfelle (å begrense hastigheten på skanninger) som mest sannsynlig vil føre deg til disse alternativene, spesielt hvis du opplever ventetid i nettverket når du bruker Nmap (noe som er ganske sjeldent).



### III. Håndtering av tilkoblingsfeil og tidsavbrudd



En annen parameter vi kan leke med for å optimalisere hastigheten på Nmap-skanninger (eller garantere større nøyaktighet), er _timeout_ og _retry_.



For _timeouts_ er dette tidsavbruddet **no response timeout** etter hvilket Nmap vil slutte å vente på svar og anse tjenesten eller verten som utilgjengelig. For _retry_ er dette **antallet påfølgende forsøk på en operasjon** som Nmap vil utføre før den går videre.



I likhet med parallellisering kan _timeout_ og _retry_-styring brukes på verts- eller tjenesteoppdagelsesfasene:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`: spesifiserer round-trip-tiden for en Exchange. Også denne parameteren beregnes og tilpasses underveis i skanningen. Det er lite sannsynlig at du trenger å bruke den, ettersom Nmap beregner denne tiden underveis i henhold til nettverksreaksjonen.





- `--max-retries <number>`: begrenser antall nye sendinger av en pakke under portskanning. Som standard kan Nmap gjøre opptil 10 nye forsøk for en enkelt tjeneste, spesielt hvis den finner forsinkelser eller tap på nettverksnivå, men i de fleste tilfeller utføres bare ett forsøk.





- `--host-timeout <time>`: angir den maksimale tiden Nmap vil bruke på en host for alle operasjoner, inkludert portskanning, tjenestedeteksjon og andre operasjoner knyttet til denne host. Hvis dette tidsintervallet overskrides uten at det kommer noe svar eller **fullføring av operasjoner**, vil Nmap forlate denne verten uten å vise noen resultater om den, og gå videre til neste på listen. På denne måten kan du kontrollere den maksimale tiden Nmap bruker på en gitt host, slik at du unngår å bli sittende fast på gjenstridige hosts og optimaliserer den totale skanningstiden.




I mitt daglige arbeid bruker jeg alternativene `--max-retries` og `--host-timeout` for å optimalisere skanningene mine:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Disse parameterne gir ekstra fleksibilitet når det gjelder å tilpasse skanneoppførselen til spesifikke behov og nettverksforhold. Du må imidlertid være klar over hva de innebærer når det gjelder belastning på skannede verter og potensielt tap av nøyaktighet.



### IV. Bruk av forberedte konfigurasjoner



De ulike alternativene vi har sett i dette kapittelet, kan brukes enkeltvis eller som en del av de ferdige konfigurasjonene som tilbys av Nmap. Alternativet som gjør det mulig å bruke disse _malene_ (konfigurasjonsmalene) er `-T <number>` eller `-T <name>`. Det finnes 5 nivåer av _maler_ som kan brukes:



```
-T<0-5>: Set timing template (higher is faster)
```



Som standard bruker Nmap _template_ 3 (_normal_), noe som vanligvis er tilstrekkelig.



For min egen del opererer jeg vanligvis i sammenhenger der jeg må være ganske rask (samtidig som jeg må være så komplett som mulig), og jeg bruker ofte alternativet `-T4`.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Her er hva feilsøkingsinformasjonen for denne skanningen viser oss:



![nmap-image](assets/fr/64.webp)



bruk av `-T4`-oppsett under en Nmap-skanning



### V. Konklusjon



I dette kapittelet har vi sett på ulike teknikker og alternativer du kan bruke for å styre Nmaps kraft, aggressivitet og ytelse. Disse alternativene er spesielt nyttige når du skanner store nettverk, og mer sjelden for stealth-formål.



I neste kapittel skal vi se nærmere på noen av de beste fremgangsmåtene for å bruke Nmap og sørge for sikkerheten.




## 12 - Datasikkerhet og konfidensialitet ved bruk av Nmap



### I. Presentasjon



I dette kapittelet skal vi se på en rekke gode fremgangsmåter som bør følges når det gjelder sikkerhet og, fremfor alt, konfidensialitet for data som produseres, behandles og lagres av Nmap.



Bruk av Nmap i et informasjonssystem kan fort bli kategorisert som en offensiv handling. Derfor må det tas en rekke forholdsregler for å kunne handle innenfor et juridisk rammeverk, samtidig som man garanterer sikkerheten til de tiltenkte målene, dataene som samles inn og systemet som brukes til skanningen.



### II. Innhenting av nødvendige autorisasjoner



Før du skanner et nettverk eller system, må du sørge for at du har innhentet de nødvendige autorisasjonene. Skanning av systemer etter sårbarheter (NSE-skript) uten autorisasjon kan være ulovlig, og kan få juridiske konsekvenser, spesielt hvis sikkerhet i informasjonssystemer ikke er en del av ditt offisielle ansvarsområde.





- Som en påminnelse: [Straffeloven: Kapittel III: Angrep på automatiserte databehandlingssystemer] (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Beskyttelse av sensitive data



Resultatene fra Nmap kan anses som sensitive, særlig når de inneholder informasjon om svakheter i informasjonssystemet som kan utnyttes av en angriper. Men også når de gjelder systemer som ikke er tilgjengelige for alle (f.eks. sensitive, industrielle, helsefaglige eller [backup]-informasjonssystemer (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



Vi har også sett at NSE-skanneresultatene fra [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) også kan inneholde identifikatorer, avhengig av NSE-skriptet som brukes.



En ondsinnet person som klarer å få tilgang til disse skanneresultatene, vil dermed ha tilgang til et kart over informasjonssystemet og et vell av teknisk informasjon, uten å ha utført disse handlingene selv, med risiko for å bli oppdaget.



Det er derfor viktig å passe på at du ikke samler inn eller lagrer sensitiv informasjon på en upassende måte når du bruker Nmap, inkludert, men ikke begrenset til, følgende:





- Kryptering av utdata: Hvis du trenger å lagre eller overføre resultatene av Nmap-skanningene dine, må du sørge for å kryptere dem for å beskytte datakonfidensialiteten. Dette vil forhindre uautorisert avlytting av sensitiv informasjon. Ideelt sett bør data krypteres så snart de forlater systemet som ble brukt til å utføre skanningen (et ZIP-arkiv kryptert med et sterkt passord er en veldig god start).





- Sett opp tilgangskontroller: Sørg for at bare autoriserte personer har tilgang til resultatene av Nmap-skanningene der de skal lagres. Sett opp passende tilgangskontroller for å beskytte sensitiv informasjon mot uautorisert tilgang.





- Vær på vakt når du håndterer data: Når du overfører, kopierer eller behandler skannedata, må du sørge for å holde datasikkerheten under streng kontroll. Det betyr at du ikke må la dem ligge og slenge i katalogen `Download` på en arbeidsstasjon som er koblet til Internett, ikke la dem gå gjennom det interne HTTP-filprogrammet Exchange, ikke la Notisblokken være åpen uten å låse arbeidsstasjonen i lunsjpausen, osv.




### IV. Håndtering av aggressive skanninger



Som vi har sett i denne veiledningen, kan Nmap være svært omfattende på nettverksnivå. Den kan også sende pakker som ikke er riktig formatert, og som ikke strengt respekterer protokollstrukturen i nettverksrammene og -pakkene den genererer. Alle disse handlingene kan påvirke visse systemer og tjenester, noen ganger så mye at det kan føre til funksjonsfeil eller overbelastning av system- og nettverksressurser.



For å unngå hendelser må du beherske Nmaps oppførsel og vite hvordan du tilpasser den til konteksten den brukes i, ved hjelp av de ulike alternativene som omtales i denne veiledningen. Nmap brukes ikke nødvendigvis på samme måte i et informasjonssystem som inneholder industriell [maskinvare] (https://www.it-connect.fr/actualites/actu-materiel/) som i et brukernettverk bestående av Windows-systemer beskyttet av en lokal brannmur eller i en nettverkskjerne.



Forhåpentligvis har de ulike leksjonene i denne opplæringen lært deg hvordan du mestrer og analyserer Nmapps oppførsel, men den beste måten å lære på er ved å gjøre det. Så sørg for at du er kjent med Nmap-alternativene du skal bruke.



### V. Beskyttelse av skanningssystemet



I det første kapittelet så vi at Nmap i de fleste tilfeller må kjøres som `root` eller lokal administrator. Dette skyldes at programmet utfører nettverksoperasjoner, noen ganger på et ganske lavt nivå, gjennom nettverksbiblioteker som krever høye og risikable tillatelser med tanke på systemstabilitet eller andre applikasjoners konfidensialitet.



Nmap kan derfor betraktes som en sensitiv komponent i systemet det er installert på. Sørg for å bruke den nyeste versjonen av Nmap, ettersom eldre versjoner kan inneholde kjente sikkerhetshull. Ved å bruke en oppdatert versjon kan du minimere risikoen forbundet med å bruke verktøyet.



Hvis du har valgt å bruke Nmap ikke via en økt som `root`, men ved å gi spesifikke privilegier til en privilegert bruker slik at han har alt han trenger for å bruke Nmap (`sudo` eller _capabilities_), må du være oppmerksom på at Nmap kan brukes som en del av en fullstendig heving av privilegier:



![nmap-image](assets/fr/65.webp)



heving av Nmap-rettigheter via `sudo`._



Her bruker jeg Nmap-kommandoen gjennom `sudo`, men dette gjør at jeg får et interaktivt skall som `root` på systemet, noe som ikke var det opprinnelige målet.



Det er også svært uheldig å installere Nmap på systemer som ikke er designet for å utføre nettverksskanninger. Jeg tenker spesielt på servere eller arbeidsstasjoner. På den ene siden vil dette legge til en potensiell vektor for rettighetsheving, men fremfor alt vil det gi angriperen enkel tilgang til et offensivt verktøy.



Til slutt må sikkerheten til systemet som brukes til skanning, ivaretas mer generelt, slik at det ikke i seg selv blir en vektor for innbrudd eller informasjonslekkasje. Som systemadministrator er det bedre å bruke et dedikert system, helst med begrenset levetid, i stedet for din egen arbeidsstasjon.



### VI. Konklusjon



Avslutningsvis bør du sørge for at du behersker Nmap godt før du bruker det i det virkelige liv eller i produksjonssammenheng, og være årvåken når du behandler og håndterer resultatene. Det ville være synd å forårsake skade, lekke data eller legge til rette for kompromittering, når målet i utgangspunktet er å forbedre bedriftens sikkerhet.



## 13 - Portskanning via TCP: SYN, Connect og FIN



### I. Presentasjon



I dette og neste kapittel skal vi se nærmere på de ulike typene TCP-skanning som er tilgjengelige i Nmap, og vi begynner med de mest brukte: SYN-, Connect- og FIN-skanninger.



Som du kanskje har lagt merke til, tilbyr Nmap flere alternativer for TCP-skanninger:



![nmap-image](assets/fr/66.webp)



skanningsteknikker som er tilgjengelige i Nmap._ _



Her vil vi forklare noen av disse metodene for å hjelpe deg å forstå forskjellene, fordelene og begrensningene ved dem. Du vil se at avhengig av konteksten eller hva du ønsker å vite, er det bedre å velge det ene eller det andre alternativet.



### II. TCP SYN-skanning eller "Half Open"-skanning



Den første typen TCP-skanning vi skal se på, er `TCP SYN Scan`, også kjent som `Half Open Scan`. Hvis du husker nettverksskanningene vi gjorde etter de første portskanningene, er dette den typen skanning som brukes som standard av [Nmap] (https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) når den kjøres med root-rettigheter.



Oversettelsen vil hjelpe deg å forstå hvordan denne skanningen fungerer. En TCP SYN-skanning vil faktisk sende en TCP SYN-pakke til hver målport, som er den første pakken som sendes av en klient (den som ber om å opprette en forbindelse) som en del av det berømte _Three way handshake_ TCP. Hvis porten er åpen på målserveren, med en tjeneste som kjører bak den, vil serveren normalt sende tilbake en TCP SYN/ACK-pakke for å validere klientens SYN og initialisere TCP-tilkoblingen. Dette svaret kommer i form av en TCP-pakke med SYN- og ACK-flaggene satt til 1, slik at vi kan bekrefte at porten er åpen og fører til en tjeneste.



Hvis porten derimot er stengt, vil serveren sende oss en `TCP`-pakke med RST- og ACK-flaggene satt til 1 for å avslutte tilkoblingsforespørselen, slik at vi vet at ingen tjeneste ser ut til å være aktiv bak denne porten:



![nmap-image](assets/fr/67.webp)



tCP SYN Scan-atferdsdiagram for åpne og lukkede porter



For å få et mer konkret bilde av `TCP SYN Scan`, utførte jeg en skanning av port TCP/80 til en vert som hadde en aktiv webserver på denne porten. Ved å kjøre en nettverksskanning med Wireshark, kan vi se følgende flyt (skannekilde: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



nettverksopptak under en TCP SYN-skanning etter en åpen port



På den første linjen ser vi at skannekilden sender en TCP-pakke til verten `10.10.10.203` på port TCP/80. I denne TCP-pakken er SYN-flagget satt til 1 for å indikere at dette er en TCP-tilkoblingsinitialiseringsforespørsel.



På den andre linjen ser vi at målet svarer med en `TCP SYN/ACK`, noe som betyr at det aksepterer å initialisere en forbindelse og derfor å motta strømmer på port TCP/80. Vi kan derfor utlede at port TCP/80 er åpen og at en webserver er til stede på den skannede serveren.



Verten vår sender deretter en RST-pakke tilbake for å stenge forbindelsen, slik at den skannede verten ikke trenger å opprettholde en åpen TCP-forbindelse som venter på svar. Ved skanning på mange porter kan det å ikke stenge TCP-tilkoblinger føre til tjenestenekt, fordi antallet tilkoblinger som venter på svar som serveren kan opprettholde, mettes (se [Wikipedia - Syn flood] (https://fr.wikipedia.org/wiki/SYN_flood))



I Wireshark vil du kunne se statusen til TCP-flaggene for hver test vi utfører. Dette vil vise om pakken er en SYN-, SYN/ACK-, ACK- osv. pakke:



![nmap-image](assets/fr/69.webp)



se en pakkes TCP-flagg i Wireshark (TCP SYN her)



Jeg kjørte den samme testen mellom de to maskinene, men denne gangen skannet jeg en TCP/81-port som ingen tjeneste er aktiv på (skannekilde: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



nettverksopptak under en TCP SYN-skanning for en lukket port



Den skannede verten returnerer en `TCP RST/ACK` som svar på min `TCP SYN` når porten ikke er åpen.



Som nevnt er TCP SYN Scan standardmodus når Nmap kjøres fra en privilegert terminal, og kan tvinges frem ved hjelp av alternativet `-sS` (`scan SYN`):



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




TCP SYN-skanning er den mest brukte skanningen på grunn av hastigheten. På den annen side kan en klients manglende fullføring av _Three Way Handshake_ (dvs. manglende sending av ACK etter serverens SYN/ACK) virke mistenkelig hvis det observeres for mange ganger på en server eller fra samme kilde i nettverket. Den normale oppførselen til en klient etter å ha mottatt en TCP SYN/ACK-pakke som svar på en TCP SYN er å sende en "bekreftelse" (ACK) og deretter starte Exchange.



Likevel gir den en litt raskere skanning, siden den ikke gidder å sende en ACK for hvert positive svar. Fordelen med SYN Scan er hastigheten, siden det bare sendes én pakke per port som skal skannes, på bekostning av en større sjanse for å bli oppdaget.



I tillegg kan TCP SYN-skanning oppdage om en port er filtrert (beskyttet) av en brannmur. En brannmur foran målverten kan faktisk oppdages ved at den oppfører seg slik den gjør når den mottar en TCP SYN-pakke på en port som den skal beskytte. Den vil rett og slett ikke svare. Men som vi har sett, kommer det i begge tilfeller (åpen eller lukket port) et svar fra verten. Denne tredje atferden vil avsløre tilstedeværelsen av en brannmur mellom den skannede verten og maskinen som kjører skanningen. Her er resultatet Nmap kan returnere når en skannet port filtreres av en brannmur:



![nmap-image](assets/fr/71.webp)



nmap-visning ved skanning av en filtrert port



Når vi utfører en nettverksregistrering på skanningstidspunktet, kan vi faktisk se at det ikke gis noe svar:



![nmap-image](assets/fr/72.webp)



nettverksopptak under en TCP SYN-skanning for en port filtrert av en brannmur



Forskjellen mellom en lukket og en filtrert port er som følger: En filtrert port er en port som er beskyttet av en brannmur, mens en lukket port er en port der det ikke kjører noen tjeneste, og som derfor ikke kan behandle TCP-pakkene våre. Noen typer TCP-skanning, for eksempel TCP SYN-skanning, kan oppdage om en port er filtrert, mens andre typer skanning ikke kan det.



### III. TCP Connect-skanning eller Full Open-skanning



Den andre typen TCP-skanning er `TCP Connect-skanning`, også kjent som _Full Open Scan_. Den fungerer på samme måte som TCP SYN-skanningen, men denne gangen returnerer den en `TCP ACK` etter et positivt svar fra serveren (en SYN/ACK). Dette er grunnen til at den kalles "Full Open", ettersom forbindelsen er fullstendig åpnet og initiert på hver port som åpnes under skanningen, og dermed respekterer TCP _Three Way Handshake_:



![nmap-image](assets/fr/73.webp)



tCP Connect Scan-atferdsdiagram for åpne og lukkede porter



Her ser du hva som passerer gjennom nettverket under en `TCP Connect-skanning` rettet mot en åpen port:



![nmap-image](assets/fr/74.webp)



nettverkssniffing under en TCP Connect-skanning etter en åpen port



Vi kan se at den første TCP-pakken som sendes er en `TCP SYN` sendt av klienten, og serveren vil deretter svare med en `TCP SYN/ACK`, noe som indikerer at porten er åpen og er vert for en aktiv tjeneste. For å simulere en legitim klient hele veien, vil Nmap deretter sende en `TCP ACK` tilbake til serveren. Omvendt, når du skanner en lukket port:



![nmap-image](assets/fr/75.webp)



nettverksopptak under en TCP Connect-skanning for en lukket port



Legg merke til at serverens svar på `SYN`-pakken vår nok en gang er en `TCP RST/ACK`-pakke, så vi kan utlede at porten er stengt og at ingen tjenester kjører på den.



Når du bruker Nmap, brukes alternativet `-sT` (`scan Connect`) til å utføre en TCP Connect-skanning. Vær oppmerksom på at når Nmap brukes fra en ikke-privilegert økt, er dette standard TCP-skannemodus:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



`TCP Connect Scan` simulerer en mer legitim tilkoblingsforespørsel, med en oppførsel som ligner mest på en lambda-klient, slik at det er vanskeligere å oppdage en skanning på et redusert antall porter. Den er imidlertid langsommere, ettersom den initialiserer alle TCP-tilkoblinger på de åpne portene på den skannede maskinen.



En Nmap-skanning av 10 000 porter vil fortsatt være lett å oppdage hvis det er installert tjenester for deteksjon og beskyttelse mot nettverksinntrenging (IDS, IPS, EDR). Når en angriper ønsker å holde en lav profil, fokuserer han gjerne på et lite antall strategisk utvalgte porter, for eksempel 445 (SMB) eller 80 (HTTP), som ofte er åpne på servere og utgjør vanlige sårbarheter.



Siden TCP Connect Scan forventer et svar i begge tilfeller, kan den også oppdage om det finnes en brannmur som filtrerer porter på målverten.



### IV. TCP FIN-skanning eller "Stealth Scan



TCP FIN Scan, også kjent som _Stealth Scan_, bruker atferden til en klient som avslutter en TCP-tilkobling, til å oppdage en åpen port.



I TCP betyr "end of session" at det sendes en TCP-pakke med FIN-flagget satt til 1. I en normal Exchange avslutter serveren all kommunikasjon med klienten (ingen respons). Hvis serveren ikke har noen aktiv TCP-forbindelse med klienten, vil den sende en `RST/ACK`. Vi kan derfor skille mellom åpne og lukkede porter ved å sende `TCP FIN`-pakker til et sett med porter:



![nmap-image](assets/fr/76.webp)



tCP FIN-skanningsdiagram for åpne og lukkede porter



Jeg tok igjen bilder av nettverket under et _Stealth-skann, og dette er hva du ser når den skannede porten er åpen:



![nmap-image](assets/fr/77.webp)



nettverksopptak under en TCP FIN-skanning etter en åpen port



Vi kan se at klienten sender én eller to pakker for å avslutte en TCP-tilkobling, og at serveren ikke svarer. Den aksepterer ganske enkelt at forbindelsen er avsluttet og avslutter kommunikasjonen.



Dette ser vi nå når vi skanner en lukket port:



![nmap-image](assets/fr/78.webp)



nettverksopptak under en TCP FIN-skanning for en lukket port



Vi ser at serveren sender tilbake en `TCP RST/ACK`-pakke, så det er en forskjell i oppførsel mellom en åpen og en lukket port, og vi kan liste opp de åpne portene på en server ved å sende en TCP FIN-pakke. I Nmap brukes alternativet `-sF` (`scan FIN`) til å utføre en TCP FIN-skanning:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN Scan fungerer ikke på Windows-verter, fordi operativsystemet har en tendens til å ignorere TCP FIN-pakker når de sendes til porter som ikke er åpne. Hvis du kjører en TCP FIN Scan på en Windows-vert, vil du derfor få inntrykk av at alle porter er stengt.



Derfor er det viktig å kjenne til flere skannemetoder, og forstå forskjellen mellom dem.



Siden TCP FIN i begge tilfeller ikke venter på svar, vil den ikke kunne oppdage om det finnes en brannmur mellom målverten og skannekilden.



Her er et eksempel på resultatet av Nmaps TCP FIN-skanning:



![nmap-image](assets/fr/79.webp)



resultatene av en TCP FIN-skanning med Nmap._ _



Faktisk kan et manglende svar fra verten på en gitt port bety at porten er filtrert, men også at den er åpen og aktiv.



Denne skanningen kalles "stealth", ettersom den ikke generate mye trafikk og vanligvis ikke forårsaker loggføring i målsystemene. Den kan brukes til å diskret oppdage porter i et nettverk uten å utløse noen alarmer. Som nevnt ovenfor kan imidlertid effektiviteten variere avhengig av målsystemet, og det samme kan diskresjonen avhengig av konfigurasjonen av sikkerhetsutstyret.



### V. Konklusjon



Så mye for det første av to kapitler om de ulike TCP-skanningstypene som tilbys av Nmap! I neste kapittel skal vi se nærmere på TCP-skanningstypene XMAS, Null og ACK, som fungerer på ulike måter for å oppdage åpne porter på en host.





## 14 - Portskanning via TCP: XMAS, Null og ACK



### I. Presentasjon



I denne delen skal vi fortsette å utforske de ulike TCP-skanningsmetodene som Nmap tilbyr. Her skal vi se på metodene `XMAS`, `Null` og `ACK`, som bruker TCP-spesifikke funksjoner for å hente informasjon om portene og tjenestene som er åpne på et gitt mål.



### II. TCP XMAS-skanning



XMAS Scan TCP er litt uvanlig i den forstand at den ikke simulerer normal bruker- eller maskinatferd på et nettverk i det hele tatt. XMAS Scan sender TCP-pakker med flaggene `URG` (Urgent), `PSH` (Push) og `FIN` (Finish) satt til 1, for å omgå visse brannmurer eller filtreringsmekanismer.



Navnet XMAS kommer av at det er uvanlig å se disse flaggene på. Når alle tre flaggene er satt på samtidig i en TCP-pakke, ser det ut som et opplyst juletre:



![nmap-image](assets/fr/80.webp)



tCP-flagg som brukes i XMAS-skanning



Uten å gå i detalj om disse flaggenes rolle her, er det viktig å vite at når du sender en pakke med disse tre flaggene aktivert, vil en aktiv tjeneste bak målporten ikke returnere noen pakker. Hvis porten derimot er stengt, vil vi motta en TCP RST/ACK-pakke. Nå kan vi skille mellom hvordan en åpen og en lukket port oppfører seg når vi lister opp porter på en maskin:



![nmap-image](assets/fr/81.webp)



tCP XMAS Scan-atferdsdiagram for åpne og lukkede porter



Fortsatt etter samme logikk viser en nettverksskanning på port TCP/80 på en vert med en aktiv webserver følgende oppførsel når den oppdager en åpen port (skannekilde `10.10.14.84`):



![nmap-image](assets/fr/82.webp)



nettverksopptak under en TCP XMAS-skanning etter en åpen port



Vi kan se at skannekilden sender to TCP XMAS-pakker (med flaggene `FIN`, `PSH` og `URG` satt til 1) til verten `10.10.10.203`, og at det ikke kommer noe svar tilbake fra målet, noe som indikerer at porten er åpen. Når du derimot utfører en `TCP XMAS Scan` på en lukket port, får du følgende resultat:



![nmap-image](assets/fr/83.webp)



nettverksopptak under en TCP XMAS-skanning for en lukket port



Svaret på TCP-pakken vår er da en `TCP RST/ACK`, som indikerer at porten er stengt. For å bruke denne teknikken med Nmap, kan du bruke alternativet `-sX` (`scan XMAS`) til å utføre en TCP XMAS-skanning:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



Det er viktig å merke seg at TCP XMAS-skanning ikke er i stand til å oppdage brannmurer som kan befinne seg mellom målet og skannemaskinen, i motsetning til andre typer skanning, for eksempel TCP SYN eller Connect. En aktiv brannmur mellom de to vertene vil sørge for at det ikke kommer noen TCP-retur hvis målporten er filtrert (dvs. beskyttet av brannmuren). Ved manglende svar er det derfor umulig å vite om porten er beskyttet av brannmuren eller om den er åpen og aktiv. Du bør også være oppmerksom på at visse programmer eller operativsystemer, for eksempel Windows, kan forvrenge resultatene av denne typen skanning, i likhet med TCP FIN-skanningen.



merk: Støtten for XMAS/FIN/NULL-skanninger på nyere versjoner av Windows er fortsatt begrenset, og resultatene kan være inkonsekvente på denne typen mål. (Oppdatering 2025)



### III. TCP Null-skanning



I motsetning til TCP XMAS scan vil TCP Null scan sende TCP scan-pakker med alle flaggene satt til 0. Dette er også en oppførsel som aldri vil forekomme i en normal Exchange mellom maskiner, ettersom det å sende en TCP-pakke uten flagg ikke er spesifisert i RFC-en som beskriver TCP-protokollen. Derfor er det lettere å oppdage.



I likhet med TCP XMAS-skanningen kan denne skanningen forstyrre visse brannmurer eller filtreringsmoduler, slik at pakker slipper gjennom:



![nmap-image](assets/fr/84.webp)



tCP Null Scan-atferdsdiagram for åpne og lukkede porter



Her ser du hva som kan vises på nettverket under en TCP Null-skanning på en åpen port:



![nmap-image](assets/fr/85.webp)



nettverksopptak under en TCP Null-skanning etter en åpen port



Skannemaskinen sender en flaggløs pakke (`[<None>]` i Wireshark) uten noe svar fra serveren. Motsatt, når målporten er stengt:



![nmap-image](assets/fr/86.webp)



nettverksopptak under en TCP Null-skanning for en lukket port



For å utføre en TCP Null-skanning med Nmap, bruker du ganske enkelt alternativet `-sN` (`scan Null`):



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Siden responsen er identisk når en port er åpen og når en brannmur er aktiv (ingen tilbakemelding fra serveren i begge tilfeller), kan ikke TCP Null-skanning oppdage tilstedeværelsen av en brannmur. I tillegg kan brannmuren til og med forfalske resultatet ved å antyde at en port er åpen, siden den ikke svarer på TCP-pakker uten flagg, selv om porten er filtrert. Dette er viktig informasjon å være klar over når man bruker skanninger som ikke kan skille mellom en åpen og en filtrert (brannmurbeskyttet) port, for eksempel `TCP Null`-, `XMAS`- eller `FIN`-skanninger, for å være konsekvent i tolkningen av resultatene man får.



### IV. TCP ACK-skanning



TCP ACK-skanning brukes til å oppdage om det finnes en brannmur på målverten eller mellom målet og skannekilden.



I motsetning til andre skanninger prøver ikke TCP ACK-skanningen å identifisere hvilke porter som er åpne på verten, men snarere om et filtreringssystem er aktivt, og svarer for hver port med `filtered` eller `unfiltered`. Noen TCP-skanninger, for eksempel `TCP SYN` eller `TCP Connect`, kan gjøre begge deler samtidig, mens andre, for eksempel `TCP FIN` eller `TCP XMAS`, ikke kan avgjøre om det finnes filtrering i det hele tatt. Dette er grunnen til at TCP ACK-skanning kan være nyttig:



![nmap-image](assets/fr/87.webp)



tCP ACK Scan-atferdsdiagram for filtrerte og ufiltrerte porter



Vi bruker Nmaps `-sA`-alternativ for å utføre denne typen skanning. Her er resultatet av en TCP ACK-skanning hvis porten er filtrert, dvs. blokkert og beskyttet av en brannmur:



![nmap-image](assets/fr/88.webp)



nmap-visning under TCP ACK Scan._ _



Eksempel på resultat for en host med brannmur og en uten. Nmap returnerer `filtered` på portene TCP/80 og TCP/81 på verten `10.10.10.203`. På en nettverksanalyse via Wireshark er oppførselen som følger:



![nmap-image](assets/fr/89.webp)



nettverksopptak under en TCP ACK-skanning for en port som ikke filtreres av en brannmur



Målmaskinen returnerer ingenting hvis det finnes en brannmur.



For å starte denne skanningen med Nmap, bruk alternativet `-sA` (`scan ACK`):



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Konklusjon



Vi har sett på tre ulike metoder for skanning via TCP i tillegg til de som allerede er presentert. Disse ulike metodene skal brukes under helt spesifikke forhold og i helt spesifikke sammenhenger, særlig i forbindelse med penetrasjonstester eller Red Team-operasjoner, der diskresjon er en viktig faktor.



## 15 - Nmap CheatSheet - Oppsummering av opplæringskommandoer



### I. Presentasjon



Her er en kort oppsummering av Nmapps mange kommandoer og bruksområder, slik at du raskt kan finne og gjenbruke dem i det daglige.



### II. Nmap: CheatSheet IT-Connect



Her er et jukseark med kommandoene som presenteres. Denne siden gjør det enkelt å finne de vanligste bruksområdene for Nmap.





- Portskanning




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Oppdage aktive verter




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



merk: Alternativet `-sP` har vært foreldet i flere år og bør erstattes av `-sn`. (Oppdatering 2025)_ _



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Deteksjon av versjon




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- NSE-skript: på jakt etter sårbarheter




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Håndtering av Nmap-utdata




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Optimalisering av ytelse




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- Typer TCP-skanning




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Jeg håper du finner disse kommandoene nyttige. Ikke glem å tilpasse målet for skanningen til din kontekst, og se den offisielle dokumentasjonen for å få full kontroll over testene som utføres.



### III. Konklusjon



Opplæringen i Nmap er nå fullført. Du har nå det grunnleggende du trenger for å bruke dette omfattende og kraftige verktøyet. Vi anbefaler på det sterkeste at du øver på kontrollerte miljøer (Hack The Box, VulnHub, virtuelle maskiner) før du bruker det i produksjon.



Det gjenstår fortsatt mye å utforske om verktøyets indre virkemåte og avanserte funksjoner. Men hvis du behersker kommandoene og konseptene som presenteres her, vil du kunne bruke Nmap på en trygg og relevant måte.