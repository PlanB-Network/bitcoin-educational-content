---
name: IP-nettverk fra teori til praksis
goal: Beherske det grunnleggende om IP-nettverk for å kunne konfigurere og feilsøke dem bedre.
objectives: 


  - Forstå arkitekturen og virkemåten til TCP/IP-protokollen
  - Forklare forskjellene, fordelene og begrensningene ved IPv4 og IPv6
  - Identifisere og skille mellom ulike typer IP Address
  - Konfigurere og verifisere IP-adressering på Unix/Linux-systemer
  - Bruke de viktigste diagnoseverktøyene for å analysere og løse nettverksproblemer


---

# Nødvendige ferdigheter for å navigere i IP-verdenen


Dykk ned i hjertet av IP-verdenen og skaff deg kunnskapen du trenger for å forstå og administrere nettverkene dine på en effektiv måte. I dette kurset lærer du alt du trenger å vite om datanettverk på en oversiktlig og praktisk måte.


Du lærer hvordan nettverk og IP-adressering fungerer, hvordan du skiller mellom IPv4 og IPv6, hvordan du identifiserer og bruker de ulike Address-kategoriene, og hvordan du forstår den fulle betydningen av TCP/IP-protokollen og koblingene den skaper mellom IP-adresser, fysiske adresser og DNS-navn.


NET 302 er først og fremst rettet mot studenter, Linux-brukere eller rett og slett nysgjerrige som ønsker å forstå det grunnleggende om nettverk og styrke sin selvstendighet når det gjelder administrasjon, feilsøking og optimalisering av infrastrukturer.


Bli med oss og gjør kunnskapen din om til reell driftskompetanse!


___


Dette NET 302-kurset er en tilpasning av *Les bases du réseau: TCP/IP, IPv4 et IPv6*, skrevet av Philippe Pierre på fransk og publisert på [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), under Creative Commons Attribution - ShareAlike 4.0 International ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)).



Loïc Morel har gjort betydelige endringer i forhold til originalversjonen: Teksten er fullstendig omskrevet, utvidet og beriket for å gi et oppdatert og dyptgående innhold, samtidig som den pedagogiske ånden i Philippe Pierres opprinnelige verk er bevart. Diagrammene har også blitt revidert.


+++


# Innledning


<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>



## Kursoversikt


<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>


Dette kurset gir en komplett innføring i de grunnleggende prinsippene for IP-nettverk. Det er delt inn i fire hoveddeler, som hver dekker et viktig aspekt for å forstå, konfigurere og diagnostisere problemer i et datanettverk.


### TCP/IP-protokoll


I denne første delen legger vi grunnlaget ved å utforske nettverksbegrepet og TCP/IP-protokollens historie. Vi studerer hovedkomponentene: IP, TCP, samt en kort titt på IPv5 QoS-protokollen. Vi går også gjennom tjenesteprimitiver for å forstå logikken i data Exchange.


### IPv4-adressering


Deretter går vi videre til en modul om IPv4-adressering. Du lærer hvordan IPv4 brukes i praksis, de ulike Address-typene (privat, offentlig, kringkasting osv.), den grunnleggende rollen til DNS, samt hvordan Ethernet-adresser og ARP-protokollen fungerer. Du vil også lære om NAT (Network Address Translation) og grunnleggende nettverkskonfigurasjon.


### IPv6-adressering


Den tredje delen fokuserer på IPv6-adressering, som er nødvendig for å Address begrensningene til IPv4. Vi går gjennom standarder og definisjoner, Address Assignment i et lokalt nettverk, Address blokkadministrasjon og forholdet mellom IPv6 og DNS.


### Verktøy for nettverksdiagnostikk


Til slutt presenterer vi de viktigste verktøyene for nettverksdiagnostikk. Med disse kan du analysere, kontrollere og feilsøke feil. Denne delen vil være strukturert etter lag: Nettverkstilgang, nettverk, transport og øvre lag.


Etter dette kurset vil du ha grunnleggende kunnskaper som gjør deg i stand til å administrere en nettverksinfrastruktur på en effektiv måte og diagnostisere potensielle problemer.


Er du klar til å dykke ned i datanettverkenes verden? Da setter vi i gang!


**MERKNAD**: Beskrivelsene er basert på et GNU/Linux CentOS 7-system. Nettverkskonfigurasjonene er imidlertid stort sett de samme når man sammenligner et Debian- og et CentOS-system. Så vi vil ikke gjøre noen forskjell. Når det er et skille, vil vi prefiksere det med en spesifikk logo.


**N.B.**: Hvis du støter på ukjente begreper i løpet av kurset, kan du slå opp i [ordlisten] (https://planb.network/resources/glossary) for å finne definisjoner.



# TCP/IP-protokoller


<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>



## Hva er et nettverk?


<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>



I denne første modulen tar vi en grundig titt på TCP/IP-protokollen, hjørnesteinen i moderne digital kommunikasjon. Vi tar for oss protokollens opprinnelse, dens grunnleggende prinsipper og adresseringssystemet den bruker, som er avgjørende for å sikre informasjonsflyten mellom tilkoblede enheter.


Vi vil også gå nærmere inn på hovedkomponentene som strukturerer denne modellen, og forklare hvordan de samhandler for å danne et operativt, pålitelig og skalerbart nettverk. Men først er det viktig å gå tilbake til begrepet nettverk.


Etymologisk sett refererer et nettverk til et sett med punkter som er koblet til hverandre og danner en sammenkoblet struktur. Innenfor telekommunikasjon og databehandling betyr denne definisjonen en gruppe enheter (datamaskiner, rutere, svitsjer, aksesspunkter osv.) som kan utveksle data via fysiske eller trådløse medier. Et nettverk muliggjør dermed kontinuerlig eller periodisk informasjonsflyt, avhengig av behov, hvilke protokoller som brukes og hvordan arkitekturen er utformet.


Over tid har det blitt utviklet flere klassiske topologier for å møte ulike behov når det gjelder kostnader, ytelse, robusthet og enkelt vedlikehold. Disse inkluderer


- ringnettverk,
- tre nettverk,
- bussnettverk,
- stjernenettverk,
- mesh-nettverk.



### Ringnettverk


I en ringtopologi er enhetene koblet sammen i en lukket sløyfe: Hver stasjon er koblet til den neste, og den siste kobler seg tilbake til den første. I dette oppsettet fungerer hver enhet som et relé, som sender data videre til neste lenke. Avhengig av nettverkstypen kan informasjonen sirkulere i én retning, eller i begge.


Fordelen med denne løsningen er at kablingen er enkel og at man ikke er avhengig av noe sentralt utstyr. Kontinuiteten i hele nettverket er imidlertid avhengig av at hvert enkelt element fungerer: Hvis en enkelt stasjon svikter, kan hele kommunikasjonssystemet bli satt ut av spill. Derfor er det ofte innført redundans- eller bypass-mekanismer.



![Image](assets/fr/001.webp)



### Tre-nettverk


Tre-nettverket, eller den hierarkiske topologien, er modellert etter strukturen til et familietre. Det består av flere nivåer: En rotnode på toppen er koblet til flere noder på lavere nivåer, som igjen kan være koblet til andre noder, og så videre.


Denne hierarkiske oppbygningen fungerer spesielt godt for store nettverk som trenger en tydelig ansvarsfordeling og segmentert administrasjon. Det gjør imidlertid også nettverket sårbart for feil i noder på høyere nivå: Hvis roten eller en hovedgren faller ut, kan hele deler av infrastrukturen bli avskåret.



![Image](assets/fr/002.webp)



### Bussnettverk


I en busstopologi deler alle enhetene det samme overføringsmediet, vanligvis en koaksial linje eller optisk fiber. Hver enhet er passivt tilkoblet, noe som betyr at den ikke aktivt endrer signalet, og den kan sende eller motta data over denne delte kanalen.


Busstopologiens største fordel er lave installasjonskostnader, takket være forenklet kabling.  I eldre koaksialbaserte implementeringer (Ethernet 10BASE2/10BASE5) kunne imidlertid frakobling eller tap av en enkelt stasjon forstyrre eller til og med stanse all trafikk, ettersom bussens elektriske kontinuitet og termineringsimpedans ikke lenger ville bli opprettholdt. Det er også en kritisk svakhet at man bare har ett fysisk medium: Ethvert brudd eller feil stopper kommunikasjonen for hele nettverket.



![Image](assets/fr/003.webp)



### Stjernenettverk


Stjernetopologien, også kjent som "hub and spoke", er den vanligste i dag, spesielt i Ethernet-nettverk i hjemmet og på kontoret. Her kobles alle enhetene til én sentral enhet.


Dette oppsettet gjør det enkelt å administrere og vedlikeholde: Hvis én periferienhet svikter, forblir resten av nettverket upåvirket. Ulempen er at den sentrale enheten er et enkelt feilpunkt: Hvis den går ned, stopper kommunikasjonen overalt. Kabelkvalitet og lenkelengder må også vurderes nøye for å opprettholde god ytelse.



![Image](assets/fr/004.webp)



**Merk**: Det finnes fortsatt nettverk som er organisert i en lineær, busslignende topologi, der utstyret er koblet til etter hverandre. Selv om denne løsningen er billig i drift, har den den store ulempen at et enkelt brudd isolerer noen av vertene og splitter nettverket i uavhengige undergrupper.


### Mesh-nettverk


Mesh-nettverket er designet for maksimal redundans: Hver enhet er direkte koblet til alle andre enheter. Dette sikrer kontinuitet i tjenesten selv om flere koblinger eller enheter skulle svikte, ettersom trafikken kan omdirigeres langs alternative veier.


Ulempen er at antallet forbindelser som må opprettes, øker raskt med antallet terminaler. For `N` tilkoblingspunkter kreves det `N × (N-1) / 2` separate koblinger, noe som gjør denne topologien dyr og kompleks å implementere. Den brukes derfor hovedsakelig i kritiske nettverk som krever svært høy tilgjengelighet, for eksempel visse deler av Internett eller sensitive industrisystemer.



![Image](assets/fr/005.webp)



Det finnes andre varianter, for eksempel grid- eller hyperkubenettverk, som er utviklet for spesielle behov innen distribuert databehandling eller parallellprosessering.


På global skala er Internett en massiv sammenkobling av nettverk med ulike topologier, som forenes av felles adressering (IPv4 og IPv6) og en samling standardiserte protokoller definert av IETF (*Internet Engineering Task Force*). Dette mangfoldet betyr at Internett ikke følger én enkelt topologi: strukturen er fleksibel, skalerbar og uavhengig av det logiske adresseringsskjemaet som gjør det brukbart.



## Opprinnelsen til TCP/IP


<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>



Opprinnelsen til TCP-protokollen ligger hos **ARPA** (*Advanced Research Projects Agency*, omdøpt til "DARPA" i 1972), som lanserte **ARPANET**-prosjektet i 1966. Det første ARPANET-segmentet ble satt i drift i oktober 1969, og sammenkoblet universitetene UCLA og Stanford. Målet var å knytte sammen forskningssentre gjennom et pakkekoblet nettverk som kunne holde kommunikasjonen i gang selv i tilfelle delvis svikt i infrastrukturen.


Som et ledd i denne dynamikken finansierte ARPA universitetet i Berkeley for å integrere de første TCP/IP-protokollene i BSD Unix-systemet. Dette spilte en viktig rolle i spredningen og standardiseringen av protokollen, først i den akademiske verden, og senere i industrien.


**Note**: På den tiden hadde dataforskere ennå ikke Linux (som ikke dukket opp før tidlig på 1990-tallet), og heller ikke Minix, det pedagogiske systemet utviklet av Andrew Tanenbaum.  De viktigste alternativene var Unix, eller noen ganger proprietære stormaskiner som OpenVMS. Takket være sin fleksibilitet og åpenhet bidro Unix til å spre de første nettverkskonseptene.


Strengt tatt er TCP/IP ikke én enkelt protokoll, men en pakke med protokoller bygget rundt TCP og IP. Den ble kjent fordi den ga en standardisert programmerings-Interface for utveksling av data mellom maskiner i samme nettverk. Denne Interface, basert på primitiver kalt "sockets", gjorde det mulig å opprette pålitelige og fleksible forbindelser samtidig som viktige applikasjonsprotokoller ble integrert.


ARPANET er derfor det historiske grunnlaget for dagens Internett. Internett er et globalt nettverk basert på prinsippet om pakkesvitsjing, der informasjon sirkulerer ved hjelp av et sett med standardiserte protokoller som sikrer kompatibilitet og interoperabilitet mellom heterogene systemer. Denne åpne arkitekturen har gjort det mulig å utvikle og ta i bruk utallige tjenester og applikasjoner, blant annet


- e-poster,
- world Wide Web (www),
- filoverføring og fildeling...


Styringen og utviklingen av disse protokollene overvåkes av ***Internet Architecture Board*** (IAB).

Denne organisasjonen koordinerer tekniske retninger gjennom to hovedstrukturer:


- IRTF** (_Internet Research Task Force_), som driver langsiktig forskning på utvikling og forbedring av protokoller.
- IETF** (_Internet Engineering Task Force_), som utvikler, standardiserer og dokumenterer driftsprotokollene som brukes på Internett


Fordelingen av nettverksressurser (IP Address-områder, autonome systemnumre, rotdomenenavn osv.) koordineres internasjonalt av **IANA/ICANN**. Den operative forvaltningen er avhengig av: **RIR** (*Regional Internet Registries*): **RIPE NCC** (Europa, Midtøsten, Sentral-Asia), **ARIN**, **APNIC**, **LACNIC** og **AFRINIC**.


Alle TCP/IP-protokollspesifikasjoner er nedtegnet i dokumenter som kalles **RFC** (_Request For Comments_), som fungerer som autoritative tekniske referanser. RFC-er oppdateres og nummereres kontinuerlig for å gjenspeile den løpende utviklingen av protokollsuiten.


TCP/IP-stakken fremstilles ofte som en stabel med fire funksjonelle lag, som ofte sammenlignes med den syv-Layer **OSI** (_Open Systems Interconnection_)-modellen som er utviklet av **ISO** (_International Standards Organization_), og som fungerer som en konseptuell referanse for nettverksbygging.


De fire lagene i TCP/IP-modellen er


- nETWORK ACCESS Layer, som sørger for den fysiske koblingen og protokoller for kontroll av medietilgang;
- iNTERNET Layer, som håndterer ruting og IP-adressering;
- tRANSPORT Layer, som garanterer pålitelighet og styring av datastrømmer ved hjelp av protokoller som TCP eller UDP ;
- aPPLICATION Layer, som samler bruker- og programvareprotokoller som HTTP, FTP, SMTP og DNS.



![Image](assets/fr/006.webp)



I dag er IPv4 den mest brukte versjonen av IP, men dens 32-bits Address-område har klare begrensninger. Dette førte til opprettelsen av IPv6, som bruker 128-bits adressering og tilbyr praktisk talt ubegrenset kapasitet: avgjørende for å støtte den eksplosive veksten av tilkoblede enheter og møte utfordringene knyttet til tingenes internett, mobilitet og sikkerhet.


Hver Layer av TCP/IP-stakken tilbyr spesifikke tjenester, noe som gjør det mulig å Address ulike nettverksbehov på en modulær måte: fysisk overføring, logisk adressering, dataintegritet og tjenester på applikasjonsnivå.


| Device example    | Description                                                                               | 	TCP/IP layer |
| ---------------------- | ----------------------------------------------------------------------------------------- | ----------------------- |
| Web server            | Application services closest to end users                                      | Application             |
| Gateway or proxy    | 	Encodes, encrypts, compresses useful data                                              | Application             |
| Session switch | Establishes sessions between applications                                               | Application             |
| Firewall or L4 router | Establishes, maintains, and terminates sessions between endpoint devices                  | Transport               |
| Router                | Globally addresses interfaces and determines optimal paths through a network | Network                  |
| Switch   | Locally addresses interfaces and forwards traffic via MAC                            | Network Access         |
| Network Interface Card (NIC)     | Signal encoding, cabling, connectors, physical specifications                        | Network Access         |

https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864

## IPv5 QoS-protokoll


<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>



Headeren i en IP-pakke er en viktig datastruktur som er delt inn i flere felt, hvert med en spesifikk rolle for å sikre at pakkene overføres og behandles riktig når de reiser gjennom nettverket. Disse feltene inkluderer destinasjons-IP Address (som er nødvendig for å rute pakken til den tiltenkte mottakeren), headerlengden angitt i IHL-feltet (*Internet Header Length*), den totale pakkelengden registrert i *Total Length-feltet*, kontroll- og verifiseringsinformasjon og andre parametere for å styre kommunikasjonsflyt og -kvalitet.


Det aller første feltet i headeren kalles Version. Denne 4-biters verdien angir hvilken versjon av IP-protokollen pakken følger. Det er viktig fordi det forteller hver ruter eller mellomliggende enhet hvordan de skal tolke og håndtere de innkapslede dataene.


**Merk: Administrasjon og Assignment av IP-protokollversjoner håndteres av **IANA**. Et 4-biters felt gir mulighet for 16 binære kombinasjoner (verdiene 0 til 15). Deres nåværende Assignment er:



| Version Number | Protocol   | Version Description         | Reference               |
| -------------- | ---------- | --------------------------- | ----------------------- |
| 0–1            | Reserved   | Reserved                    |                         |
| 2–3            | Unassigned | Unassigned                  |                         |
| 4              | IP         | Internet Protocol           | RFC 791                 |
| **5**          | **ST**     | **ST Datagram mode**        | **RFC 1190** / RFC 1819 |
| 6              | IPv6       | Internet Protocol version 6 | RFC 8200                |
| 7              | TP/IX      | The Next Internet           | RFC 1475                |
| 8              | PIP        | The P Internet Protocol     | RFC 1621                |
| 9              | TUBA       | Tuba                        | RFC 1347                |
| 10–14          | Unassigned | Unassigned                  |                         |
| 15             | Reserved   | Reserved                    |                         |

Blant disse er IPv5, som, selv om den stort sett er ukjent for offentligheten, eksisterte som ST (_Stream Protocol_). IPv5 ble utviklet på 1980-tallet for å dekke et voksende behov på den tiden: å tilby "_Quality of Service_" (QoS) for visse datastrømmer som krevde kontinuerlig og stabil overføring, for eksempel Voice over IP eller multimediastrømmer. Målet var å garantere båndbredde og prioritet fra ende til ende, et konsept som ligner på det RSVP (_Resource Reservation Protocol_) tilbyr i dag for dynamisk reservasjon av nettverksressurser på moderne rutere.


IPv5 forble imidlertid eksperimentelt og ble bare implementert på et lite antall nettverksenheter. Den begrensede utbredelsen, kombinert med det raskt voksende behovet for mer Address-plass, førte til at Internett-designerne hoppet direkte fra IPv4 til IPv6. Dermed unngikk man både IPv4s Address-begrensninger og risikoen for forvirring eller inkompatibilitet med IPv5s eksperimentelle spesifikasjoner.


Selv om IPv5 aldri ble tatt i bruk i stor skala, spilte den en viktig rolle i utformingen av den tidlige tenkningen rundt QoS og trafikkstyring. I dag er den mer en historisk markør enn en fungerende standard.


**En protokoll er et sett med kommunikasjonsregler: datastrukturer, algoritmer, pakkeformater og konvensjoner som gjør det mulig for ulike enheter å Exchange informasjon på en pålitelig og forståelig måte. En tjeneste er den konkrete implementeringen av en protokoll gjennom spesifikke programmer (klienter, servere) som følger disse reglene og gjør funksjonaliteten tilgjengelig for brukere og applikasjoner.


Nå kan vi se nærmere på hvordan IP-protokollen, som er selve grunnlaget for all nettverkskommunikasjon, er bygd opp og fungerer.



## IP-protokollen


<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>



### Definisjoner og generell informasjon


IP-protokollen, eller "***Internet Protocol***", er ryggraden i TCP/IP-modellen. Den transporterer datapakker fra én vert til en annen i et nettverk, enten det er lokalt eller verdensomspennende. Den har to nøkkelroller: å administrere den logiske adresseringen av enheter, og å sørge for at pakker rutes på tvers av ofte heterogene og sammenkoblede nettverk.


På det fysiske nivået er overføring avhengig av maskinvaregrensesnitt for å etablere punkt-til-punkt-forbindelser mellom noder. Det er imidlertid IP-protokollen som gjør ende-til-ende-kommunikasjon mulig, ved å gi hver pakke den informasjonen den trenger for å navigere gjennom flere mulige veier til målet.


Tre nettverkskonfigurasjoner Elements bestemmer hvordan en pakke sendes på vei:


- IP Address**: identifiserer destinasjonsverten på en unik måte i nettverket.
- Subnettmaske**: spesifiserer hvilken del av Address som identifiserer nettverket og hvilken del som identifiserer verten, noe som muliggjør logisk inndeling i subnett.
- Gateway**: angir den mellomliggende ruteren som pakken skal passere gjennom for å nå et eksternt nettverk eller et annet segment av det lokale nettverket.


På Internett flyter ikke data som en sammenhengende strøm, men sendes som **datagrammer**: uavhengige datablokker som hver for seg er innkapslet med all den informasjonen som trengs for levering. Dette er prinsippet for **pakkesvitsjing**, der informasjonen deles opp i selvstendige enheter som kan ta ulike veier for å nå samme mottaker.


I tillegg til nyttelasten (*payload*) inneholder hvert IP-datagram et strukturert hode med felter som destinasjons-Address, kilde-Address, tjenestetype, protokollversjonsnummer og annen kontrollinformasjon som er nødvendig for å administrere overføringen.


Den teoretiske maksimumsstørrelsen på et IP-datagram er **65 536 oktetter**, en grense som settes av feltet for total lengde i headeren. I praksis blir denne størrelsen sjelden nådd, ettersom de fysiske nettverkene som bærer pakkene (Ethernet, Wi-Fi, fiberoptikk ...) vanligvis har en strengere grense, kjent som **MTU** (_Maximum Transmission Unit_). Hvis et datagram overskrider MTU for den fysiske koblingen, må det deles opp i mindre pakker, som sendes hver for seg og settes sammen igjen ved ankomst.


Denne tilpasningsdyktigheten gjør IP til en robust og fleksibel protokoll som kan brukes på en lang rekke underliggende teknologier, samtidig som den opprettholder universell kompatibilitet mellom heterogene systemer og nettverk.



### Fragmentering av IP-datagrammer


Når et IP-datagram skal passere gjennom et nettverk som har mindre overføringskapasitet enn selve datagrammet, må det **fragmenteres** slik at det kan sendes uten problemer. Denne fysiske størrelsesgrensen kalles **MTU** (Maximum Transmission Unit): den største rammestørrelsen som kan passere over et gitt nettverk uten å bli delt opp.


Hver nettverksteknologi har sin egen MTU, som bestemmes av maskinvare- og protokollegenskapene. Vanlige verdier inkluderer:


- ARPANET**: 1000 byte
- Ethernet**: 1500 byte
- FDDI**: 4470 byte


Når et datagram overskrider MTU-en for et nettverkssegment det skal krysse, vil rutingsutstyret dele det opp i mindre **fragmenter** som overholder grensen. Dette skjer vanligvis når man beveger seg fra et nettverk med høy MTU til et nettverk med lavere kapasitet. For eksempel kan det hende at et datagram som kommer fra et FDDI-nettverk, må fragmenteres før det sendes over et Ethernet-segment.



![Image](assets/fr/008.webp)



Fragmenteringsprosessen fungerer slik:


- Ruteren deler datagrammet opp i fragmenter som ikke er større enn målnettverkets MTU.
- Størrelsen på hvert fragment er et multiplum av 8 byte, siden IP-protokollen bruker denne enheten til å kode for reassembleringsoffset.
- Hvert fragment får sitt eget IP-hode, som inneholder informasjonen den endelige mottakeren trenger for å sette dem sammen igjen i riktig rekkefølge.


Når de er fragmentert, reiser delene uavhengig av hverandre gjennom nettverket. De kan ta forskjellige ruter, avhengig av rutingstabeller, koblingsbelastninger eller avbrudd. Det er ingen garanti for at de kommer frem i den rekkefølgen de ble sendt.


Ved ankomst håndterer mottaksmaskinen **reassemblering**. Ved hjelp av informasjonen i headerne (delt identifikator, offset og fragmenteringsflagg) setter den fragmentene sammen i riktig rekkefølge for å rekonstruere det opprinnelige datagrammet før det sendes videre til neste Layer. Hvis så mye som ett fragment går tapt eller blir ødelagt, blir hele datagrammet vanligvis forkastet, for uten alle fragmentene ville resultatet blitt ufullstendig eller ubrukelig.


Selv om fragmentering og reassemblering er effektivt, har det sine ulemper: ekstra prosessering for rutere og verter, og større sjanse for pakketap, noe som kan føre til flere retransmisjoner. Derfor er nøye MTU-styring og optimalisering av pakkestørrelsen viktig for å sikre smidig og effektiv IP-kommunikasjon.



### Innkapsling av data


For å sikre at data rutes riktig gjennom lagene i TCP/IP-modellen, spiller prosessen med **innkapsling** en nøkkelrolle. På hvert trinn når en melding sendes fra avsenderens applikasjon til mottakerens maskin, legges det til ekstra informasjon, såkalte headere. Disse overskriftene gir mellomliggende enheter og programvarelag instruksjonene de trenger for å behandle, levere og, om nødvendig, sette sammen dataene på nytt.


Når en melding sendes, passerer den gjennom de fire lagene i TCP/IP-stakken. Ved hver Layer legges det til en ny header foran de eksisterende dataene: Hver header inneholder spesifikke metadata, for eksempel logiske eller fysiske adresser, kommunikasjonsporter, sekvensnumre, feilkontrollflagg og annen informasjon som er nødvendig for å administrere overføring og ruting.


Overføringen følger dermed en strukturert prosess:


- Applikasjonen Layer oppretter den første **meldingen**, som inneholder rådataene.
- Transport Layer kapsler den inn i et **segment**, og legger til kilde- og destinasjonsporter, sekvensnummer og flytkontrollmekanismer.
- Internet Layer legger til et IP-hode i segmentet for å danne et **datagram**, med angivelse av kilde- og mål-IP-adresser.
- Network Access Layer pakker datagrammet inn i en **frame**, og legger til MAC-adresser og integritetskontrollkoder (CRC).



![Image](assets/fr/009.webp)



Denne innkapslingsprosessen sikrer både integriteten og sporbarheten til dataene, og også tilpasningsdyktigheten: Når du beveger deg fra ett nettverk til et annet, gir overskriftene enhetene den informasjonen som trengs for å velge rute, kontrollere gyldigheten eller utføre fragmentering om nødvendig.


Ved ankomst reverseres prosessen: Mottakermaskinen får rammen på Network Access Layer, som leser og fjerner det tilsvarende overskriften. Datagrammet sendes deretter til Internet Layer, som leser IP-hodet og fjerner det i sin tur for å levere segmentet til Transport Layer. Transport Layer behandler transporthodene, kontrollerer integriteten til strømmen og leverer til slutt **meldingen** til målapplikasjonen i sin opprinnelige tilstand.



![Image](assets/fr/010.webp)



Transformasjonen av dataene ved hver Layer kan oppsummeres som følger:


- Melding**: informasjonsblokk på applikasjonen Layer.
- Segment**: dataenhet etter innkapsling av Transport Layer.
- Datagram**: form som er tatt etter at IP-hodet er lagt til av Internet Layer.
- Frame**: den siste blokken som er klar for overføring over det fysiske mediet av Network Access Layer.



![Image](assets/fr/011.webp)



Denne prosessen, som er avgjørende for påliteligheten og universaliteten i Internett-kommunikasjonen, sikrer at alle data, uansett hvor fragmenterte eller komplekse de er, kan transporteres fra ende til ende samtidig som de forblir forståelige og brukbare for mottakeren.



### IP-adressering


Selv med pakkesvitsjing, fragmentering og innkapsling på plass, kan et nettverk fortsatt ikke fungere uten et pålitelig adresseringssystem. For å sikre at hver datapakke når frem til riktig mottaker, bruker Internet Layer en unik identifikator: **IP Address**.

I IPv4 er en IP Address kodet på **32 bits** og skrives som fire desimaltall atskilt med prikker, i det velkjente N1.N2.N3.N4-formatet (for eksempel: 192.168.1.12).


En IP Address består av to deler:


- _netid_**: identifiserer nettverket som verten tilhører
- _hostid_**: identifiserer den spesifikke verten i det aktuelle nettverket

Denne separasjonen gjør at det globale Internett kan struktureres logisk i mange sammenkoblede nettverk.


Historisk sett baserte IPv4-systemet seg på et klassebasert system, merket fra A til E, som definerte rekkevidden av Address og den tiltenkte bruken av dem. Hver klasse tildelte et bestemt antall biter til _netid_ og _hostid_, noe som direkte påvirket det mulige antallet nettverk og verter.



| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Ikke alle mulige verdier kan tilordnes verter. I en **klasse C** Address har for eksempel den siste byten 8 bits (256 verdier). Men to av disse er reservert:


- 0: identifiserer selve nettverket
- 255: er **broadcast** Address, som brukes til å sende en pakke til alle verter i nettverket på én gang.

Det gir 254 adresser som kan brukes til enheter.


Antallet tilgjengelige adresser varierer mye fra klasse til klasse: fra store offentlige nettverk i klasse A, til bedriftsnettverk i klasse B og mindre lokale nettverk i klasse C.



![Image](assets/fr/013.webp)



Noen Address-områder er reservert for privat bruk og rutes aldri direkte på Internett. Disse er kjent som **private adresser**, og brukes i organisasjoner, bedrifter eller hjem, og krever Address-oversettelse, vanligvis NAT (*Network Address Translation*), for å nå det offentlige Internett. Disse er


- Klasse A**: fra 10.0.0.0.0 til 10.255.255.255.255
- Klasse B**: fra 172.16.0.0 til 172.31.255.255
- Klasse C**: fra 192.168.0.0 til 192.168.255.255


Når en enhet med en privat Address får tilgang til Internett, erstatter en NAT-aktivert ruter eller gateway den med en gyldig offentlig Address.


Eksempel: Hvis en vert har Address **192.168.7.5**, kan vi utlede dette:


- 192.168.7.0: nettverk Address
- 192.168.7.1: ofte den lokale ruteren
- 192.168.7.5: selve verten


Et annet spesialtilfelle er **127.0.0.1**, kjent som "***loopback***".

På Linux-systemer er den knyttet til Interface **lo**. Denne Address gjør det mulig for en maskin å Address seg selv for lokal testing eller diagnostikk, uten å gå gjennom en fysisk Interface. Hele **127.0.0.0/8**-området er reservert for dette formålet.


For å optimalisere bruken av Address og designe komplekse nettverk er **subnettmasken** (_nettmaske_) avgjørende. Denne binære masken skiller _netid_ fra _hostid_ i en IP Address.

Hver klasse har en standardmaske:


- 255.0,0,0** for klasse A,
- 255.255.0.0.0** for klasse B,
- 255.255.255.0** for klasse C.


God nettverksdesign følger en grunnleggende regel: Enheter som må kommunisere direkte, bør være i samme nettverk eller subnett. For å segmentere et nettverk bruker vi subnett, der vi deler nettverket inn i mindre subnett ved hjelp av en mer spesifikk maske.


Eksempel på subnetting:

Et **klasse C**-nettverk: 192.168.1.0/24 med en standardmaske på 255.255.255.255.0.

Vi ønsker fire undernett med opptil 60 verter hver.


**Steg 1**: Antall adresser som trengs per delnett = 60 + 2 reserverte adresser (nettverk + kringkasting) = 62.


**Trinn 2**: Finn nærmeste potens av 2 ≥ 62. -> 2⁶ = 64.


**Trinn 3: Juster masken. Behold _netid_-bitene og reserver de nødvendige _hostid_-bitene. Vi får en binær maske som, når den er konvertert, gir **255.255.255.255.192**.


```
11111111 11111111 11111111 11000000
```


**Trinn 4**: Beregn Address-områdene for hvert delnett, og varier bitene som er reservert for verten.



| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Trinn 5**: Dette skaper fire undernettverk, som hver støtter opptil 62 maskiner, samtidig som det overordnede adresseringsskjemaet forblir effektivt. _hostid_-delen deles opp i en _subnetid_-del og en host-del.



![Image](assets/fr/016.webp)



Dette grunnleggende prinsippet for subnetting er fortsatt uunnværlig i moderne nettverksteknikk, og muliggjør presis IP-allokering, bedre trafikkontroll, sterk segmentisolering og skalerbar nettverksadministrasjon.



### CIDR-adressering


På begynnelsen av 1990-tallet, da Internett spredte seg raskt blant bedrifter og organisasjoner, begynte det tradisjonelle IP-adresseringssystemet basert på klasser (A, B, C) å vise sine begrensninger.

Den rigide strukturen førte til betydelig sløsing med IP-adresser og gjorde rutingstabellene stadig større, mer komplekse og vanskelige å vedlikeholde.

For å løse disse problemene ble det innført en mer fleksibel og effektiv metode: **CIDR** (_Classless Inter-Domain Routing_). CIDR har etter hvert blitt standard, og har i stor grad erstattet det gamle klassebaserte systemet.


Kjerneideen bak CIDR er muligheten til å gruppere flere tilstøtende nettverk, spesielt klasse C-blokker, i én logisk enhet som kalles et **supernett** (_supernet_). Med denne aggregeringen kan én enkelt oppføring i rutingstabellen representere flere undernettverk, noe som reduserer antallet rutere ruterne må håndtere og forbedrer ytelsen.


Mens klasse C-nettverk opprinnelig hadde størst behov for aggregering på grunn av sin mindre kapasitet, har prinsippet også blitt brukt på klasse B-nettverk og i teorien til og med klasse A-nettverk, selv om sistnevnte er mindre berørt takket være deres store Address-rekkevidde.


Med CIDR forsvinner konseptet med faste klasser. Address-området behandles som et kontinuerlig område som kan deles opp eller aggregeres etter behov. CIDR-blokker defineres ved hjelp av undernettmasker som ikke er begrenset til standardinnstillingene for A-, B- eller C-klasser. En CIDR-blokk kan enten representere ett enkelt nettverk eller et sammenhengende sett med undernettverk som deler samme prefiks.


En CIDR-blokk skrives i formatet "Address/prefiks", der tallet etter skråstreken angir hvor mange biter som utgjør nettverksdelen. For eksempel betyr /17 at de første 17 bitene identifiserer nettverket, mens de resterende 15 bitene identifiserer verter.


Eksempel:

En /17-blokk inneholder 2^(32-17) adresser, så 2^15 = 32 768 adresser totalt. Hvis du trekker fra de to reserverte adressene (nettverk og kringkasting), gjenstår 32 766 brukbare vertsadresser. På denne måten kan nettverksadministratorer dimensjonere subnettene sine nøyaktig slik at de passer til behovene i den virkelige verden, og unødvendig sløsing unngås.


For å gjøre CIDR-dimensjonering enklere å forstå, følger her en tabell over vanlige prefikser og deres tilsvarende nettverksmasker og brukbare adresser:


| CIDR Prefix | Available Host Bits | Subnet Mask     | Usable Host Addresses         |
| ----------- | ------------------- | --------------- | ----------------------------- |
| /8          | 24                  | 255.0.0.0       | 2^24 - 2 = 16,777,214         |
| /12         | 20                  | 255.240.0.0     | 2^20 - 2 = 1,048,574          |
| /16         | 16                  | 255.255.0.0     | 2^16 - 2 = 65,534             |
| /20         | 12                  | 255.255.240.0   | 2^12 - 2 = 4,094              |
| /24         | 8                   | 255.255.255.0   | 2^8 - 2 = 254                 |
| /26         | 6                   | 255.255.255.192 | 2^6 - 2 = 62                  |
| /27         | 5                   | 255.255.255.224 | 2^5 - 2 = 30                  |
| /28         | 4                   | 255.255.255.240 | 2^4 - 2 = 14                  |
| /29         | 3                   | 255.255.255.248 | 2^3 - 2 = 6                   |
| /30         | 2                   | 255.255.255.252 | 2^2 - 2 = 2                   |
| /31         | 1                   | 255.255.255.254 | 2^1 = 2 (point-to-point only) |
| /32         | 0                   | 255.255.255.255 | 1 (host address only)         |


**MERKNAD**: Tidligere frarådet RFC 950 bruk av subnett null, hovedsakelig for å unngå forvirring i ruting.  Denne begrensningen ble foreldet med RFC 1878, som tillater bruk av subnett null fullt ut. Den gamle begrensningen skyldtes hovedsakelig manglende kompatibilitet med eldre maskinvare som ikke kunne håndtere CIDR på riktig måte. Moderne utstyr har ikke slike problemer.


For eksempel er subnettet **1.0.0.0.0** med subnettmasken **255.255.0.0.0**, som tidligere var tvetydig med klasse A-nettverksidentifikatoren, nå helt gyldig og brukbart.


**TIP**: For feilfrie subnettberegninger og rask konvertering av adresser til CIDR-notasjon finnes det praktiske verktøy som ***ipcalc***. Denne "nettverkskalkulatoren" viser tydelig Address-oppdelinger, tilgjengelige områder og tilhørende masker, noe som er ideelt for både administratorer og studenter som skal lære seg CIDR.


```shell
sudo apt install ipcalc
```


https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## TCP-protokollen


<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>



Protokollen **TCP** (_Transmission Control Protocol_) spiller en sentral rolle i TRANSPORT Layer i TCP/IP-modellen. Den fungerer som en bro mellom applikasjoner og Internett Layer, og sørger for pålitelig overføring av data mellom to fjerntliggende maskiner.

Mens IP-protokollen bare sender pakker uten å garantere levering eller rekkefølge, sørger TCP for integriteten og konsistensen i datastrømmen ved å levere dem uten tap, i riktig rekkefølge og uten duplikater.


TCP har blant annet følgende hovedansvarsområder:


- Omorganisering av mottatte segmenter;
- Overvåker dataflyten for å unngå overbelastning;
- Deler opp eller setter sammen datablokker i passende enheter (segmenter);
- Håndtering av etablering og avslutning av forbindelser mellom begge ender av kommunikasjonen.


TCP er en tilkoblingsorientert protokoll, noe som betyr at den etablerer et eksplisitt, løpende forhold mellom klient og server. For å gjøre dette bruker den **sekvensnumre** og **bekreftelser**: For hvert segment som sendes, tildeles en unik identifikator slik at mottakeren kan kontrollere både rekkefølgen og integriteten til dataene. Mottakeren returnerer deretter et bekreftelsessegment med **ACK-flagget** satt til 1, som bekrefter mottakelsen og angir neste forventede sekvensnummer.



![Image](assets/fr/018.webp)



For å forbedre påliteligheten bruker TCP en tidtaker: Når et segment er sendt, starter en nedtelling. Hvis det ikke kommer noen bekreftelse innen tidsavbruddsperioden, sender avsenderen automatisk segmentet på nytt, i den tro at det har gått tapt under overføringen. Denne automatiske retransmitteringsmekanismen kompenserer for tap i IP-nettverk, som kan oppstå ved overbelastning, rutingsfeil eller maskinvarefeil.



![Image](assets/fr/019.webp)



TCP er i stand til å oppdage og håndtere duplikater. Hvis det kommer et nytt segment, men originalen også dukker opp, bruker mottakeren sekvensnumrene til å identifisere duplikatet og bare beholde den riktige kopien, slik at det ikke oppstår noen tvetydighet.


For at denne prosessen skal fungere, må begge maskinene ha en felles forståelse av sine opprinnelige sekvensnumre. Dette sikres ved å følge en streng tilkoblingsprosedyre: På den ene siden lytter **serveren** på en bestemt port og venter på en innkommende forespørsel (passiv modus); på den andre siden initierer **klienten** aktivt tilkoblingen ved å sende en forespørsel til serveren på den samme tjenesteporten.


**MERKNAD**: En "port" er en numerisk identifikator (fra 0 til 65 535) som er tilordnet en nettverksapplikasjon på en datamaskin. Den brukes til å skille mellom flere tjenester som kjører samtidig på samme IP Address. Når en klient sender data, spesifiserer den portnummeret slik at serverens operativsystem vet hvilket program som skal motta dem (f.eks. 80 for HTTP, 443 for HTTPS, 25 for SMTP). Portene fungerer som egne dører som leder trafikk inn og ut, forhindrer sammenblanding mellom tjenester og gir mulighet for finkornet tilgangskontroll gjennom brannmurer eller filtreringsregler.


Sekvenssynkroniseringen Exchange er basert på den berømte **"*treveis håndtrykk*"**-mekanismen, som ligner på måten to mennesker hilser på hverandre for å etablere kontakt. Denne initialiseringsfasen, som sikrer TCP's pålitelighet, foregår i tre trinn:

1. **SYN:** Klienten sender et innledende synkroniseringssegment (**SYN**) med riktig flagg satt og et innledende sekvensnummer (f.eks. C);

2. **SYN-ACK:** Mottakende server svarer med et bekreftelsessegment (**SYN-ACK**), den bekrefter klientens sekvensnummer og oppgir sitt eget opprinnelige sekvensnummer;

3. **ACK:** Klienten sender en endelig bekreftelse (**ACK**) som bekrefter mottak av serverens sekvensnummer, og avslutter synkroniseringen. SYN-flagget er nå deaktivert, og ACK-flagget forblir satt, noe som indikerer at forbindelsen er opprettet.



![Image](assets/fr/020.webp)



Denne Exchange-protokollen sikrer at begge parter har samme nummerbase før de overfører nyttelastdata. Når denne synkroniseringen er fullført, åpnes økten: Segmenter kan nå sendes i begge retninger, og hver av dem bekreftes ved mottak, noe som sikrer maksimal pålitelighet i dataflyten.


Dette ***treveis håndtrykket*** gjelder kun opprettelse av forbindelse. For å lukke bruker TCP et *fireveis håndtrykk*: FIN → ACK → FIN → ACK, som garanterer at ingen segmenter i transitt går tapt før forbindelsen er fullstendig frigjort.


Selv om denne prosessen er utformet med tanke på robusthet og pålitelighet, har den også gitt opphav til sårbarheter som kan utnyttes. Angrep som **IP-spoofing** tar for eksempel sikte på å omgå eller ødelegge dette tillitsforholdet ved å utgi seg for å være en autorisert maskin ved hjelp av forfalskede sekvensnumre, noe som skaper et brudd som gjør det mulig å avlytte eller manipulere datastrømmen.


For å begrense risikoen for kapring av sekvenssynkronisering og for å styre nettverksbelastningen bruker TCP-protokollen en flytstyringsteknikk som kalles "**_Sliding Window_**". Dette systemet regulerer hvor mye data som kan sendes uten at det kreves umiddelbar bekreftelse for hvert segment, noe som reduserer unødvendig overbelastning av nettverket og samtidig opprettholder god pålitelighet.


I praksis definerer skyvevinduet en rekke sekvensnumre som kan sirkulere fritt mellom avsender og mottaker uten at hvert enkelt segment blir kvittert for. Etter hvert som avsendersystemet mottar bekreftelser, "glir" vinduet: Det glir mot høyre og gir plass til nye segmenter som skal sendes. Størrelsen på dette vinduet (som er avgjørende for å optimalisere gjennomstrømningen og samtidig unngå overbelastning) spesifiseres i "*Window*"-feltet i TCP-hodet.


**Eksempel**: Hvis det opprinnelige sekvensnummeret er 3 og vinduet strekker seg til sekvens 5, kan segmentene nummerert fra 3 til 5 sendes uten å vente på individuelle bekreftelser.



![Image](assets/fr/021.webp)



Størrelsen på skyvevinduet er ikke fast, men tilpasser seg dynamisk til nettverksforholdene og mottakerens prosesseringskapasitet.  Hvis mottakeren kan håndtere en større datamengde, gir den beskjed om dette gjennom Window-feltet, noe som får avsenderen til å utvide vinduet sitt. Motsatt kan mottakeren be om å redusere vinduet ved overbelastning eller fare for metning, og avsenderen vil da vente med å sende flere segmenter til vinduet flyttes fremover.


Protokollen har en symmetrisk prosedyre for å stenge en TCP-tilkobling for å sikre en ren og ryddig avslutning. Hver av maskinene kan starte avslutningen ved å sende et segment med **FIN**-flagget satt til 1, noe som signaliserer at de har til hensikt å avslutte kommunikasjonen. Deretter venter den til alle segmenter i overføring er mottatt, og ignorerer eventuelle ytterligere data.


Når den andre maskinen mottar dette segmentet, sender den en bekreftelse, også merket med FIN-flagget. Deretter avslutter den sendingen av gjenværende data før den lokale applikasjonen informeres om at forbindelsen er avsluttet. Denne doble bekreftelsen sikrer en ryddig avslutning og minimerer risikoen for tap av data.


Denne presise styringen, som kombinerer IPs fleksible ruting med TCPs strenge kontroll, illustreres ofte med et diagram som kontrasterer hastigheten til IP-protokollen (som fungerer på **"best effort"**-basis, uten leveringsgaranti) mot påliteligheten til TCP-protokollen (som styrer overføringen ved hjelp av bekreftelser og forhandlede sekvenser).



![Image](assets/fr/022.webp)



I noen tilfeller er det imidlertid ikke absolutt pålitelighet som prioriteres, men hastighet og enkelhet. Dette gjelder for applikasjoner som direktestrømming eller VoIP, som tåler noe pakketap uten at det går ut over brukeropplevelsen. I slike tilfeller er **UDP** (_User Datagram Protocol_) å foretrekke.


UDP fungerer etter et prinsipp som er fundamentalt forskjellig fra TCP: Det er **forbindelsesløst**, noe som betyr at det ikke opprettes noen forhåndsrelasjon mellom avsender og mottaker. Når en maskin sender pakker via UDP, sendes de én vei; mottakeren sender ingen bekreftelser, og avsenderen har ingen bekreftelse på at meldingen er kommet frem. UDP-hodet er med vilje minimalt og inneholder bare kildeport, destinasjonsport, segmentlengde og en kontrollsum, uten noen innebygd bekreftelses- eller tilstandskontrollmekanisme. IP-adresser bæres som alltid av det underliggende IP-hodet.


En vanlig analogi er at TCP er som en **telefonsamtale**, der en krets blir etablert, fulgt og kontrollert gjennom hele samtalen. UDP-protokollen er som å **postlegge et brev**, der avsenderen legger et brev i en postkasse uten umiddelbar bekreftelse på levering eller systematisk tilbakemelding.


Denne komplementariteten mellom TCP og UDP gjør det mulig for moderne nettverk å tilpasse seg en rekke ulike behov, ved å velge maksimal pålitelighet eller prioritere hastighet, avhengig av bruksområde.



## Primitive tjenester


<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>



### Lagdelt arkitektur og Exchange-organisering


Som vi har sett, er **tjenester** den konkrete implementeringen av protokollene vi har beskrevet så langt. Selv om TCP/IP-modellen skiller seg fra **OSI**-modellen, har den samme lagdelte tilnærming: Hver Layer er designet for å utføre en spesifikk funksjon og for å levere **tjenester** til Layer rett over seg, noe som resulterer i en modulær, robust og lett vedlikeholdbar arkitektur.


Hver Layer bygger på funksjonene til den under seg, og gir i sin tur Layer over seg en konsekvent Interface for datahåndtering. I denne arkitekturen har hver Layer sine egne **datastrukturer**, som er nøye definert for å sikre perfekt kompatibilitet med de andre lagene. Denne kompatibiliteten er avgjørende for at kommunikasjonen fra ett endepunkt til et annet skal være jevn, pålitelig og tydelig.


To viktige aspekter styrer disse utvekslingene:


- Vertikalt aspekt**: forholdet mellom en Layer og den som ligger over eller under den (fra Layer N til Layer N+1, og omvendt).



![Image](assets/fr/023.webp)




- Horisontalt aspekt**: interaksjonen mellom eksterne applikasjoner, dvs. dialogen mellom en **klient** og en **server**, i begge retninger.



![Image](assets/fr/024.webp)



Den lagdelte arkitekturen følger prinsippet om at hver Layer kun behandler den informasjonen som ligger innenfor dens virkeområde: Datastrukturer, overskrifter og kontrollmekanismer varierer fra en Layer til en annen, men sammen utgjør de et sammenhengende system som sørger for at data gradvis blir rutet til sin endelige destinasjon.


**Påminnelse**: Det brukes en spesifikk terminologi for å beskrive dataenhetene som utveksles mellom lagene:


- melding** for applikasjonen Layer,
- segment** for Transport Layer (TCP),
- datagram** for Internett Layer (IP),
- ramme** for Network Access Layer.


Tabellen nedenfor oppsummerer begrepene for TCP- og UDP-kontekster:


| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Tjenesteprimitiver og dataenheter


Kjernen i dette systemet er **tjenesteprimitiver**, som fungerer som kommunikasjonsgrensesnitt. Disse primitivene fungerer som serviceskranker, lytter på reserverte, spesifikke **porter** og gjør det mulig for prosesser å opprette, vedlikeholde og avslutte nettverkstilkoblinger på en kontrollert måte. Mens protokollene organiserer formatet og overføringen av data i nettverket, er det **tjenestene og deres primitiver** som utgjør den vertikale koblingen mellom lagene.


Ved å kombinere det horisontale aspektet (kommunikasjon mellom distribuerte applikasjoner) med det vertikale aspektet (intern interaksjon mellom lagene) gir TCP/IP-modellen en komplett, skalerbar arkitektur. Ved å overlappe disse to perspektivene får man en klar oversikt over hvordan data utveksles i strukturert nettverkskommunikasjon.



![Image](assets/fr/026.webp)



### Del sammendrag


I denne første hoveddelen utforsket vi kjernearkitekturen som styrer konfigurasjonen og driften av dagens Internett-tilkoblede nettverk. Denne arkitekturen er basert på en **fire-Layer-modell**, inspirert av OSI-modellen, og bygget rundt **TCP/IP**-protokollpakken, som er ryggraden i moderne kommunikasjon. Vi så at TCP, med sin tilkoblingsorienterte tilnærming, sikrer pålitelige overføringer, mens UDP, som er lettere og raskere, er å foretrekke når hastighet er viktigere enn pålitelighet.


For at denne modellen skal fungere korrekt, er den avhengig av at protokoller implementeres gjennom **tjenesteprimitiver**. Disse sikrer koblingen mellom lagene, slik at databehandlingen kan tilpasses de spesifikke kravene på hvert nivå, fra transport til applikasjon, inkludert Internett og nettverkstilgang. Denne modulære tilnærmingen gjør systemet både fleksibelt og robust.


IP-adressering er en annen hjørnestein i denne infrastrukturen. Alle tilkoblede enheter identifiseres med en **unik IP Address**, hentet fra et Address-rom som er organisert i **klasser** (fra A til E). Noen av disse adressene er reservert for spesielle formål, for eksempel lokal loopback eller multicast, mens andre, kjent som "private adresser", ikke rutes over Internett uten oversettelse (NAT). Denne klassifiseringen muliggjør en logisk, hierarkisk organisering av nettverk.


Vi har også sett nærmere på konseptet **undernett**, som gjør det mulig å dele opp et nettverk i segmenter for bedre å kunne administrere IP-ressurser og optimalisere dataflyten. Selv om manuell inndeling ved hjelp av subnettmasker fortsatt er et viktig prinsipp, har det i stor grad blitt modernisert takket være **CIDR** (_Classless Inter-Domain Routing_). Denne metoden har forandret Address-administrasjonen ved å muliggjøre en mer fleksibel og rasjonell allokering av IP-områder, samtidig som størrelsen på rutingstabellene reduseres.


Ved å beherske disse konseptene - lag, protokoller, tjenesteprimitiver, adressering og subnetting - får du et solid grunnlag for å forstå hvordan moderne nettverk fungerer teknisk, og for effektivt å konfigurere en nettverksinfrastruktur som dekker dagens behov.


I neste avsnitt skal vi se nærmere på IPv4-adressering.



# IPv4-adressering


<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>



## Bruk av IPv4


<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>



I denne delen skal vi gå dypere og se på hvordan **IPv4**-adresser faktisk implementeres i et nettverk i den virkelige verden. Vi går gjennom formatet, logikken bak dem og hvordan de henger sammen med andre viktige Elements-nettverk som **DNS-navn**, **MAC-adresser**, **subnettverk** og **oversettelsesteknikker**.


En IP Address er en unik numerisk identifikator som tildeles hver **nettverks-Interface** på en enhet. Den gjør det mulig å lokalisere denne enheten i et nettverk og nå den for å overføre data. En ruter, server, arbeidsstasjon, nettverksskriver eller til og med et overvåkningskamera har for eksempel minst én egen IP Address. IP Address muliggjør **routing**, dvs. flytting av pakker fra punkt A til punkt B, selv om de fysisk er langt fra hverandre.


IP-adresser kan tildeles på to hovedmåter:


- Statisk**: Stilles inn manuelt på enheten.
- Dynamisk**: Tilordnes automatisk på forespørsel av en DHCP-server (_Dynamic Host Configuration Protocol_). DHCP forenkler nettverksadministrasjonen, eliminerer behovet for manuell konfigurasjon og muliggjør presis kontroll gjennom reservasjoner og leieperioder.


**IPv4-adresser** skrives i et **32-biters** format som er delt inn i **fire byte**. Hver byte inneholder 8 bits og representerer et desimaltall fra 0 til 255. De fire bytebitene er atskilt med prikker for å danne en tydelig og leselig notasjon.


eksempel: Address 172.16.254.1_



![Image](assets/fr/027.webp)



Hver bit i en byte har en verdi (eller "vekt"): Den venstre biten (den mest signifikante biten) er verdt 128, den neste 64, deretter 32, 16, 8, 4, 2 og 1 for den høyre biten (den minst signifikante biten). På denne måten konverteres binær skriving til desimal ved enkel addisjon av de innstilte vektene.


Tabellen nedenfor illustrerer denne sammenhengen:



| Binary Code | Activated Bit Values          | Decimal Value |
|-------------|-------------------------------|---------------|
| 00000000    | 0                             | 0             |
| 00000001    | 1                             | 1             |
| 00000011    | 1 + 2                         | 3             |
| 00000111    | 1 + 2 + 4                     | 7             |
| 00001111    | 1 + 2 + 4 + 8                 | 15            |
| 00011111    | 1 + 2 + 4 + 8 + 16            | 31            |
| 00111111    | 1 + 2 + 4 + 8 + 16 + 32       | 63            |
| 01111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64  | 127           |
| 11111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 | 255      |

For å konvertere binær til desimal, legger du sammen vektene til de bitene som er satt til 1.


| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

En IP Address identifiserer en enkelt **nettverks-Interface**, ikke hele enheten. En ruter eller brannmur med flere porter har flere grensesnitt, hvert med sin egen IP Address. En Interface kan til og med ha flere IP-adresser (for eksempel for å betjene flere virtuelle nettverk eller tjenester).


Hver IP-pakke inneholder to IP-adresser i toppteksten:


- Kilden Address (**sender**)
- Destinasjonen Address (**mottaker**)

Rutere leser disse adressene for å finne ut hvilken vei som er best å sende pakken frem til målet. Uten strenge regler for adressering ville nettverkstrafikken ikke kunne rutes korrekt, og global sammenkobling av nettverk ville vært umulig.


En IPv4 Address består av to deler:


- NetID**: identifiserer nettverket
- HostID**: identifiserer en enhet i det aktuelle nettverket

**Subnettmasken** bestemmer hvor NetID slutter og HostID begynner, og angir hvor mange bits som hører til hver del. Jo lenger NetID er, desto flere undernett er det mulig å opprette, men antallet verter per undernett reduseres tilsvarende.


Opprinnelig var IPv4-nettverk delt inn i fem **klasser**: (A, B, C, D og E). Hver klasse tilsvarer et bestemt NetID-område og definerer en fast granularitet:


- Klasse A: svært store nettverk med et stort antall verter
- Klasse B: mellomstore nettverk
- Klasse C: små nettverk
- Klasse D: adresser reservert for multicasting (_multicast_)
- Klasse E: eksperimentelle adresser, ikke brukt til konvensjonell adressering



| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Spesielle adresser:


- Nettverk Address**: Identifiserer selve nettverket (brukes i rutingstabeller).
- Kringkasting Address**: Sender data til alle enheter i delnettet samtidig (alle HostID-biter er satt til 1).


Følgende områder er reservert for intern bruk:


- 10.0.0.0/8** (Privat klasse A)
- 127.0.0.0/8** (lokal loopback eller _loopback_)
- 172.16.0.0 til 172.31.255.255** (privat klasse B)
- 192.168.0.0 til 192.168.255.255** (privat klasse C)


Adressene **127.0.0.1** og, mer generelt, hele 127.0.0.0/8-området brukes til intern testing: Alle forespørsler som sendes til dem, forlater aldri maskinen. Dette er nyttig for å kontrollere at en lokal nettverkstjeneste fungerer uten å involvere det større nettverket.


For å utnytte Address-plassen bedre deler administratorer ofte opp nettverk i **subnett** ved hjelp av subnettmasker eller **CIDR**-notasjon (_Classless Inter-Domain Routing_). CIDR gir mer presis administrasjon og bidrar til å unngå sløsing med adresser. I dag er CIDR viktig for å finjustere IP-områder og redusere størrelsen på rutingstabeller.


I moderne nettverk er IP-adressering vanligvis koblet sammen med andre identifikatorer:



- domenenavn** registrert i et **DNS** (_Domain Name System_): Det knytter en numerisk IP Address til et menneskevennlig navn.
- MAC Address**: en fysisk identifikator som er gravert inn i nettverkskortet, og som brukes til lokal transport (_Ethernet_). Når en IP-pakke skal overføres fysisk, matcher ARP-tabellen IP Address med MAC Address for destinasjonen.


For å håndtere IPv4 Address-mangel og for å legge til en Layer sikkerhet, bruker nettverk ofte Address-oversettelse (_NAT_). NAT gjør det mulig for mange private enheter å dele en enkelt offentlig IP Address når de får tilgang til Internett.


**Note**: Nettbaserte og innebygde OS-verktøy, for eksempel [Grenoble CRIC calculator] (http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/), gjør det mye enklere å beregne subnett og masker.

Disse verktøyene hjelper deg med å planlegge nettverksdeling på en effektiv måte.


Avslutningsvis er broadcast Address fortsatt en praktisk funksjon for å sende den samme meldingen til alle enheter som er koblet til et segment: Dette oppnås ved å sette alle bitene i HostID-delen til 1, slik at alle verter er i målgruppen.



## De forskjellige typene IPv4 Address


<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>



IPv4-adresser kan deles inn i to hovedkategorier: offentlige adresser, som er direkte tilgjengelige på Internett, og private adresser, som er beregnet for intern bruk i et lokalt nettverk.


En offentlig IPv4 Address er globalt unik og kan dirigeres over Internett. Den tildeles av offisielle myndigheter og er nødvendig for tjenester som henvender seg til offentligheten, for eksempel nettsteder, e-postservere eller skyinfrastruktur.

At disse adressene er unike over hele verden, er avgjørende for å unngå rutingskonflikter eller kollisjoner.


**IANA** (_Internet Assigned Numbers Authority_), som opererer under **ICANN** (_Internet Corporation for Assigned Names and Numbers_), administrerer fordelingen av disse IP-områdene. Konkret deler IANA IPv4-området inn i 256 blokker av størrelsen /8, i henhold til CIDR-notasjonen. Hver blokk representerer litt over 16,7 millioner adresser (2³² / 2⁸).


Disse unicast Address-blokkene overlates av IANA til **Regional Internet Registries** (RIRs). Disse RIR-ene er ansvarlige for å omfordele adressene på regionalt nivå, i henhold til de reelle behovene til tilgangsleverandører, selskaper eller administrasjoner. Unicast Address-området strekker seg fra blokkene **1/8 til 223/8**, med deler som enten er reservert for spesielle formål (forskning, dokumentasjon, testing), eller som er tildelt direkte til et nettverk eller RIR for videredistribusjon.


Hvis du vil sjekke hvem som eier en offentlig IP Address, kan du konsultere RIR-databasene ved hjelp av kommandoen **whois**, eller ved å bruke webgrensesnittene som tilbys av hvert register. Disse verktøyene kan brukes til å spore Address tilbake til organisasjonen eller leverandøren som har deklarert den.


På den andre siden finnes det private IPv4-adresser, som er et praktisk svar på mangelen på offentlige adresser. Disse adressene, som ikke kan rutes på Internett, er forbeholdt lokale miljøer: bedriftsnettverk, hjemmenettverk, datasentre eller dataklynger. De er ikke unike i hele verden: Mange private nettverk kan gjenbruke de samme IP-intervallene uten forstyrrelser, så lenge de er isolerte eller bruker en Address-oversettelsesenhet for å få tilgang til Internett.


For å gi en enhet med en privat IP Address tilgang til Internett, bruker nettverk NAT (Network Address Translation). NAT fungerer ved dynamisk å erstatte den private Address med en offentlig, slik at dusinvis (eller til og med hundrevis) av enheter kan dele en enkelt offentlig IP Address. Denne metoden optimaliserer bruken av IPv4-plass og gir også en Layer av sikkerhet ved å skjule den interne nettverksstrukturen.


En annen spesiell kategori er **uspesifiserte** adresser. IPv4-notasjonen **0.0.0.0** eller IPv6-versjonen **::/128** betyr "ingen spesifikk Address". En slik Address er ugyldig som Address-destinasjon i nettverket, men den kan brukes lokalt av en vert for å indikere "alle grensesnitt" eller "ingen Address tildelt ennå". Dette er vanlig i DHCP-dynamiske Assignment eller for å lytte på alle servergrensesnitt.


IPv6 støtter også privat adressering, men standarden anbefaler generelt offentlig adressering for å unngå å stable flere NAT-lag. De **lokale adressene** (_site-local_) i **fec0::/10**-blokken ble utfaset av **RFC 3879** av hensyn til konsistens og sikkerhet. De ble erstattet med **Unique Local Addresses** (_ULA_) i **fc00::/7**-blokken. ULA-er gjør det mulig å opprette private IPv6-nettverk med ren intern ruting, ved hjelp av en tilfeldig generert 40-biters identifikator for å sikre lokal unikhet.


I 2011 ble det offisielt bekreftet at IPv4 var utslitt. For å forlenge levetiden har internettfellesskapet tatt i bruk flere strategier:


- Gradvis overgang til **IPv6**
- Utbredt bruk av **NAT**
- Strengere allokeringspolitikk fra RIR-ene, noe som krever nøyaktig begrunnelse og styring av Address-behov
- Gjenvinning av ubrukte eller frivillig returnerte Address-blokker fra selskaper


Disse tiltakene viser at IP-adressering ikke bare er en teknisk utfordring, men også et spørsmål om global styring, noe som er sentralt for den pågående utvidelsen av Internett.



## DNS, en Address-katalog


<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>



La oss være ærlige: Mennesker er ikke flinke til å huske lange tallrekker, verken i binær eller desimal form. Denne utfordringen blir enda større med IP-adresser, som kan være komplekse, og en enkelt IP Address kan noen ganger maskere flere adresser, spesielt når teknikker som NAT eller virtuell hosting er involvert.


For å gjøre ting enklere bruker applikasjonen Layer et system som kobler en IP Address til et logisk, menneskelig lesbart navn. Dette er rollen til **DNS** (*Domain Name System*), en massiv, hierarkisk, distribuert katalog som matcher lesbare domenenavn med IP-adresser. Systemet er basert på et sett med protokoller og tjenester. Den mest brukte DNS-serverprogramvaren er **BIND** (_Berkeley Internet Name Domain_), en programvarepakke med åpen kildekode som refererer til store deler av DNS-infrastrukturen på Internett.


Kjerneideen bak DNS er enkel: For alle tilkoblede tjenester, enten det er et nettsted, en e-postserver eller en annen nettverkstjeneste, finnes det en post som tilordner et domenenavn til en eller flere IP-adresser. Dette fungerer i to retninger:


- Videresending: oversetter et navn til en IP Address.
- Omvendt oppløsning: finne domenenavnet som er knyttet til en gitt IP Address.

Dette gjør nettverksadresseringen brukbar for mennesker, samtidig som ruterne beholder den presisjonen de trenger for å flytte data korrekt.


Et domenenavn er alltid hierarkisk strukturert, og hvert nivå er atskilt med en prikk: Det fulle navnet kalles **FQDN** (_Fully Qualified Domain Name_). Delen lengst til høyre er **TLD** (_Top Level Domain_), for eksempel `.com`, `.org` eller `.fr`. Delen lengst til venstre angir verten, dvs. den spesifikke maskinen eller tjenesten som er knyttet til IP Address.


DNS-systemet er utformet som et **trær av soner**. En **sone** er en del av domenenavnområdet som administreres av en bestemt DNS-server. En enkelt sone kan inneholde flere **underdomener**, som i sin tur kan være delegert til andre soner som administreres av forskjellige servere. Administratorer er ansvarlige for å vedlikeholde sonene sine: håndtering av oppdateringer, delegeringer og generell administrasjon.


Denne strukturen gjør det mulig ikke bare å peke på et hoveddomene (f.eks. `example.com`), men også å finjustere poster for individuelle verter (`www`, `mail`, `ftp`, osv.). I nettverkets barndom ble denne mappingen håndtert med statiske filer som `/etc/hosts` (på Unix-systemer), men en slik metode ble raskt upraktisk for et raskt voksende, sammenkoblet Internett.


Det er viktig å forstå at en **DNS-server** kanskje bare har et begrenset omfang. For eksempel kan det hende at en bedrifts interne DNS-server ikke er direkte tilgjengelig fra Internett. Hvis denne DNS-serveren ikke er konfigurert til å videresende forespørsler, eller ikke har et klarert forhold til andre servere, vil noen forespørsler mislykkes: verken navnet eller IP Address kan da løses utenfor den definerte sonen.


DNS spiller også en rolle i ruting av e-post. En **MX**-post (_Mail Exchange_) angir for eksempel hvilke e-postservere som er ansvarlige for å motta e-post for et gitt domene. Disse postene definerer prioriteringer (vektingsfaktor) og failover-løsninger. Sonefilen til en DNS-server må inneholde en **SOA** (_Start Of Authority_)-oppføring, som angir serveren som den offisielle informasjonskilden for den aktuelle sonen.


Takket være sin hierarkiske, distribuerte struktur er DNS fortsatt en hjørnestein i Internett, og gjør det mulig for brukere å få tilgang til tjenester gjennom tydelige, minneverdige domenenavn i stedet for lange, tekniske IP-adresser.


I neste kapittel skal vi se nærmere på et annet grunnleggende konsept: **Ethernet-adresser**, også kjent som **MAC-adresser**, som sørger for datalevering på den fysiske Layer i lokale nettverk.



## Finne Ethernet-adresser og ARP


<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>



### Definisjoner


For at datarutingprotokollen skal fungere pålitelig og konsekvent, er det én nøkkelkomponent som er avgjørende. Som mennesker kan vi enkelt identifisere en maskin ved hjelp av dens IP Address eller ved hjelp av navnet som hentes via DNS. En maskin må imidlertid være i stand til å utvetydig gjenkjenne destinasjonsenheten for å kunne levere pakker. For å gjøre dette er den avhengig av en spesifikk maskinvareidentifikator som brukes direkte av nettverkets Interface: MAC Address (_Media Access Control_).


**Merknad**: Dette har ingenting å gjøre med en "fysisk Address" i minnearkitekturen. I databehandling refererer et fysisk Address-minne til en bestemt plassering på minnebussen, i motsetning til et virtuelt Address-minne som administreres av operativsystemet. En MAC Address er derimot knyttet til nettverksmaskinvare.


En MAC Address tildeles permanent og entydig av produsenten utstyret er produsert av. MAC Address identifiserer nettverkskortet på en entydig måte, uansett om det er en datamaskin, smarttelefon, skriver eller en annen tilkoblet enhet. I motsetning til en IP Address, som kan endres dynamisk (via en DHCP-server eller manuell konfigurasjon), forblir MAC Address normalt den samme gjennom hele enhetens levetid, med mindre den bevisst endres.


Hvert nettverk Interface, kablet eller trådløst, har sin egen MAC Address. Denne Address brukes i datalink Layer (Layer 2 i OSI-modellen) til å sette inn og administrere maskinvare Address i hver nettverksramme som utveksles. Dette kalles noen ganger _Ethernet-adressen_ eller _UAA_ (_Universally Administered Address_). Den er standardisert med en lengde på 48 bits, eller 6 byte, og skrives i heksadesimal notasjon, vanligvis i form av byte atskilt med `:` eller `-`.


For eksempel: `5A:BC:17:A2:AF:15`


I denne strukturen identifiserer de tre første byte nettverkskortets produsent: dette er kjent som **OUI** (*Organisationally Unique Identifier*). Disse prefiksene, som er tildelt av IEEE, brukes også i andre maskinvareadresseringsordninger, som Bluetooth og LLDP, for å garantere unikhet over hele verden.


### Endre en MAC Address (MAC-spoofing)


I teorien er MAC Address utformet for å være fast, men det finnes måter å modifisere den på, særlig for å dekke spesielle behov eller omgå visse begrensninger. Denne operasjonen, som ofte kalles _spoofing MAC_, innebærer å erstatte den opprinnelige maskinvare-Address med en annen verdi, definert på programvarenivå. Noen operativsystemer legger til rette for denne modifikasjonen, spesielt når den faktiske Ethernet Address ikke brukes direkte av driveren.


Årsakene til en slik endring kan være mange. Det kan være at et gitt program krever en bestemt Ethernet Address for å fungere korrekt, eller for å løse en konflikt med identiske adresser mellom to enheter som deler det samme lokale nettverket.


Endring av MAC Address kan også være motivert av personvernhensyn: Ved å skjule den unike identifikatoren som er gravert inn på kortet, reduserer brukerne muligheten for at enheten deres kan spores av nettverk eller overvåkningstjenester. Denne praksisen er imidlertid ikke uten konsekvenser. Bytte av MAC Address kan forstyrre visse filtreringsenheter, eller kreve at brannmurer må konfigureres på nytt for å godkjenne den nye maskinvaren.


Noen nettverk, særlig Wi-Fi-nettverk, bruker MAC Address-filtrering for å kun tillate enheter med godkjente adresser. Selv om dette gir et grunnleggende nivå av kontroll, er det ikke sikkert i seg selv. En angriper kan fange opp en gyldig MAC Address som allerede er autorisert i nettverket, og klone den for å omgå restriksjonene. Derfor bør MAC-filtrering alltid kombineres med sterkere sikkerhetstiltak.


### MAC/IP-korrespondanse


For at et lokalt nettverk skal fungere effektivt, må det være en tydelig mapping mellom fysiske adresser (MAC-adresser) og logiske adresser (IP-adresser). Uten denne koblingen kan en datamaskin kjenne IP-adressen til en destinasjon, men ikke vite hvordan den fysisk skal sende data til den i det lokale nettverket.

Denne mappingen håndteres automatisk av ARP (_Address Resolution Protocol_).


I praksis kan brukeren bruke verktøyet `arp` når han eller hun vil vite hvilken MAC Address som svarer til en bestemt IP Address. Dette verktøyet sjekker maskinens lokale ARP-tabell for å vise kjente treff mellom IP-adresser og MAC-adresser i det lokale nettverket. På denne måten er det mulig å raskt verifisere den effektive koblingen mellom det logiske og det fysiske laget.


Praktisk eksempel: Hvis du vil sjekke hvilket nettverkskort som tilsvarer IP Address `192.168.1.5`, kan du bruke følgende kommando:


```bash
arp –a 192.168.1.5
```


Utdataene viser den tilknyttede fysiske Address (MAC), typen inngang (statisk eller dynamisk) og den aktuelle Interface.


```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```


Det er viktig å huske at MAC Address og IP Address er to helt forskjellige identifikatorer, men at de utfyller hverandre. MAC Address er unikt inngravert i hver nettverks-Interface av produsenten og brukes til å fysisk identifisere enheten i det lokale nettverket. IP Address er derimot en logisk Address som tildeles enten dynamisk eller statisk, slik at maskinen kan koble seg til IP-nettverket og Exchange-pakker utenfor det lokale nettverket.



- Visuelt eksempel på MAC Address:


![Image](assets/fr/032.webp)




- Visuelt eksempel på en IP Address:


![Image](assets/fr/027.webp)



I et bedriftsmiljø kan ikke disse to adresseringsnivåene fungere separat. Når en DHCP-server for eksempel automatisk tildeler en IP Address, brukes utstyrets MAC Address som utgangspunkt. Datamaskinen sender en DHCP-kringkastingsforespørsel som inneholder MAC Address, slik at serveren kan tildele en tilgjengelig IP Address til riktig enhet. Uten denne maskinvareidentifikasjonen ville DHCP-serveren ikke vite hvilken enhet Address skal leveres til.


ARP-protokollen er derfor grunnleggende: Den sørger for koblingen mellom IP-adresser og fysiske adresser, slik at maskinene kan oversette en logisk destinasjon til en faktisk fysisk destinasjon. Når en datamaskin skal sende en pakke til en maskin i samme nettverk, konsulterer den først ARP-tabellen sin for å sjekke om mottakerens MAC Address allerede er kjent. Hvis ikke, sender den en ARP-forespørsel til alle verter i det lokale nettverket. Maskinen som gjenkjenner mål-IP Address i denne forespørselen, svarer ved å oppgi sin MAC Address. Avsenderen skriver deretter dette IP/MAC-paret til ARP-cachen sin, slik at han slipper å gjenta operasjonen hver gang forespørselen sendes.


Denne ARP-tabellen fungerer som en minikartleggingskatalog, som oppdateres dynamisk på samme måte som DNS knytter domenenavn til IP-adresser. Uten ARP ville det ikke vært mulig med en lokal Exchange, ettersom datalink Layer må kjenne MAC Address for å kunne kapsle inn Ethernet-rammer på riktig måte.


RARP-protokollen (_Reverse Address Resolution Protocol_) ble derimot utviklet for den motsatte situasjonen: å gjøre det mulig for en maskin som bare kjenner sin MAC Address, å finne sin IP Address. Dette var vanlig for eldre arbeidsstasjoner uten en lokal Hard-disk, som måtte starte opp over nettverket og be om en IP Address. RARP ble etter hvert erstattet av **BOOTP** og deretter **DHCP**, som er mer fleksible og automatiserte.


Disse assosiasjonsprotokollene spiller en viktig rolle i ruting. En ruter er egentlig en maskin med flere nettverksgrensesnitt som forbinder ulike segmenter. Når en ruter mottar en ramme, behandler den den for å trekke ut IP-datagrammet og undersøker IP-hodet for å finne destinasjonen. Hvis destinasjonen befinner seg i et direkte tilkoblet nettverk, blir datagrammet levert direkte etter oppdatering av headeren. Hvis destinasjonen tilhører et annet nettverk, konsulterer ruteren rutingstabellen sin for å finne den beste veien, eller _next hop_, til destinasjonen.


Dette deler ruten opp i kortere, mer håndterbare segmenter. Hver mellomliggende ruter kjenner bare neste steg, ikke nødvendigvis den endelige destinasjonen.


**Husk:** Direkte levering skjer når avsender og mottaker befinner seg i samme fysiske nettverk. Ellers er leveransen indirekte og går gjennom en eller flere rutere.


Rutetabellen, som enten administreres manuelt (statisk ruting) eller dynamisk (dynamisk ruting), inneholder informasjonen som trengs for å avgjøre hvilken rute som skal tas. I små nettverk er det nok med en statisk konfigurasjon. I større infrastrukturer er dynamisk ruting avgjørende for å kunne justere rutene automatisk når topologien endres eller en kobling går ned.


Routing-tabellen fungerer som en mapping-tabell mellom IP-adresser og neste gateway. Den lagrer vanligvis nettverksidentifikatorer (_nettverks-ID_) i stedet for hver enkelt host Address, noe som reduserer størrelsen kraftig.


| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Ved hjelp av disse oppføringene kan ruteren raskt finne ut hvilken Interface og til hvilken node hvert datagram skal sendes. Kombinert med ARP for å løse de matchende MAC-adressene, sikrer dette effektiv og pålitelig dataoverføring over nettverket.


Dynamiske rutingsprotokoller omfatter standarder som RIP (_Routing Information Protocol_), som er basert på avstandsalgoritmen, og OSPF (_Open Shortest Path First_), som beregner de korteste veiene i en kompleks topologi. Disse protokollene oppdaterer kontinuerlig Exchange for å optimalisere rutene, redusere overføringskostnadene og forbedre motstandsdyktigheten mot strømbrudd eller overbelastning.



## NAT: Address Oversettelse


<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>



### Definisjon


Network Address Translation_ (NAT) er en teknikk som er utviklet for å Address den gradvise uttømmingen av tilgjengelige IPv4-adresser. NAT ble utviklet som en midlertidig løsning før IPv6 ble tatt i bruk i stor skala, og gjorde det mulig for bedrifter og enkeltpersoner å fortsette å koble til et stort antall maskiner samtidig som de bare brukte et begrenset sett med offentlige IP-adresser.


**Viktig påminnelse:** Overgangen fra IPv4 til IPv6 løser i teorien utmattelsesproblemet ved å utvide Address-området fra 32 bits til 128 bits, noe som gir et nesten ubegrenset antall adresser (2^128). I praksis er overgangen imidlertid fortsatt ufullstendig, og NAT er fortsatt mye brukt i dag.


Prinsippet bak NAT er enkelt, men svært effektivt: I stedet for å tildele en unik offentlig IP Address til hver enhet i det interne nettverket, brukes én enkelt adresserbar Address (eller en liten gruppe adresser) for alle private enheter. NAT-gatewayen, som ofte er integrert i ruteren eller brannmuren, oversetter deretter den interne IP Address dynamisk sammen med informasjonen som trengs for å rute trafikken riktig til omverdenen, og sørger for at svarene returneres til den opprinnelige avsenderen.


Denne tilnærmingen har en umiddelbar fordel: Den skjuler den interne nettverksarkitekturen fullstendig. For en utenforstående observatør ser alle forespørsler fra arbeidsstasjoner, servere eller skrivere ut til å komme fra den samme offentlige identiteten. Private adresser, som vanligvis hentes fra reserverte områder (f.eks. 192.168.x.x eller 10.x.x.x), forblir usynlige fra Internett.


I tillegg til å løse problemet med IPv4-knapphet styrker NAT også sikkerheten ved å skape en første logisk barriere mellom det interne og det offentlige nettverket. Uønsket innkommende kommunikasjon blokkeres naturlig nok, siden bare forbindelser som initieres fra innsiden av nettverket, får den nødvendige oversettelsen for å motta svar.



![Image](assets/fr/035.webp)



### Oversettelsestyper


NAT kan implementeres på ulike måter for å dekke spesifikke behov. De to viktigste driftsmåtene er statisk oversettelse og dynamisk oversettelse.


**Statisk oversettelse** skaper en fast mapping mellom en privat IP Address og en offentlig IP Address. Hver interne maskin er permanent knyttet til sin dedikerte offentlige Address. En intern enhet konfigurert som 192.168.20.1 kan for eksempel være knyttet til den rutbare Address 157.54.130.1. Når en utgående pakke forlater det lokale nettverket, erstatter ruteren pakkens kilde-Address med den offentlige Address, og utfører den omvendte operasjonen for innkommende trafikk. Denne toveisoversettelsen er transparent for brukeren.


**Selv om denne metoden isolerer det interne nettverket, løser den ikke mangelen på offentlige IP-adresser, siden du fortsatt trenger like mange offentlige adresser som det finnes maskiner å eksponere. Statisk oversettelse brukes derfor hovedsakelig når visse interne ressurser må kunne nås fra utsiden (webserver, e-postserver ...).


**Dynamisk oversettelse** bruker derimot en pool med offentlige IP-adresser. Når en intern vert starter en tilkobling, tildeler ruteren midlertidig en av disse offentlige adressene til vertens private Address så lenge økten varer. Koblingen er 1-til-1, men midlertidig: Når tilkoblingen avsluttes, blir den offentlige Address tilgjengelig for en annen enhet. Dynamisk NAT reduserer derfor antallet offentlige adresser som trengs når ikke alle maskinene er på nettet samtidig, men det krever fortsatt en blokk med eksterne adresser som er minst like stor som det maksimale antallet samtidige tilkoblinger.


**Port translation** (PAT), også kjent som *NAT overload* eller *IP masquerading*, går et skritt videre: Alle private enheter deler en enkelt offentlig IP Address (eller et svært lite antall). For å skille mellom økter endrer gatewayen ikke bare kilden Address, men også kildeporten. Den fører en tabell som kobler hvert *(privat Address, privat port)*-par til et unikt *(offentlig Address, offentlig port)*-par. Denne formen for NAT brukes i nesten alle hjemmerutere, slik at dusinvis av enheter (datamaskiner, smarttelefoner, tilkoblede objekter osv.) kan dele den samme offentlige IP-Address, samtidig som kommunikasjonen opprettholdes.


NAT forlenger derfor IPv4s levetid, samtidig som det tilfører en verdifull Layer segmentering og sikkerhet. Etter hvert som IPv6 blir mer utbredt og det enorme Address-området blir tatt i bruk, vil NAT trolig få mindre betydning, selv om det av kompatibilitets- og kontrollhensyn fortsatt vil bli brukt i enkelte miljøer for å segmentere og filtrere trafikk.


### NAT-implementering


For å sikre at Address-oversettelsen fungerer som den skal, må NAT-ruteren eller gatewayen ha en nøyaktig oversikt over tilordningene som er opprettet mellom hver private Address i det interne nettverket og den offentlige Address som brukes til å kommunisere med omverdenen. Denne informasjonen lagres i den såkalte "NAT-oversettelsestabellen", som spiller en sentral rolle i håndteringen av nettverkstrafikken.


Hver oppføring i denne tabellen kobler sammen minst ett par: den interne IP Address på avsendermaskinen og den eksterne IP Address som vil bli eksponert på Internett. Når en pakke fra det private nettverket sendes til en offentlig destinasjon, fanger NAT-ruteren opp rammen, analyserer IP- og TCP/UDP-overskriftene og erstatter deretter den private kilde-Address med gatewayens offentlige Address. På returveien fanger den samme gatewayen opp den innkommende pakken, sjekker tilordningstabellen og utfører den omvendte operasjonen for å omdirigere flyten til den opprinnelige interne IP Address.


Dette dynamiske oversettelsesprinsippet baserer seg på presis tabellhåndtering: Hver oppføring forblir gyldig så lenge det er aktiv trafikk som rettferdiggjør den. Etter en konfigurerbar periode med inaktivitet slettes oppføringen og kan brukes på nytt for nye tilkoblinger.


_Eksempel på en forenklet NAT-oversettelsestabell:_


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

I dette eksempelet er den andre oppføringen merket som gjenbrukbar hvis det ikke har gått noen pakke gjennom den på over en time (3600 sekunder). En varighet på null indikerer derimot at kommunikasjonen er aktiv, og at mappingen er låst.


Selv om NAT fungerer transparent for de vanligste bruksområdene (nettsurfing, e-post, filoverføring osv.), kan det skape ekstra utfordringer for enkelte nettverksapplikasjoner. Noen teknologier baserer seg på eksplisitt utveksling av IP-adresser eller porter i pakkens nyttelast. Etter å ha passert gjennom en NAT-gateway blir denne informasjonen inkonsekvent.


Typiske eksempler på begrensninger inkluderer:


- Peer-to-peer-protokoller (P2P), som krever direkte forbindelser mellom enheter, hindres av NAT-barrieren, siden alle interne maskiner deler samme eksterne IP Address og ikke kan nås direkte uten spesifikk konfigurasjon (for eksempel *port forwarding* eller UPnP);
- IPSec-protokollen, som brukes til å sikre nettverkskommunikasjon, krypterer pakkehodene. Fordi NAT må modifisere disse overskriftene for å erstatte IP-adresser, gjør kryptering dette umulig uten tilpasningsmekanismer som NAT-T (*NAT Traversal*);
- X Window-protokollen, som gjør det mulig å vise grafiske programmer på avstand under Unix/Linux, fungerer slik at X-serveren aktivt sender TCP-tilkoblinger til klientene. Denne reverseringen av den vanlige forbindelsesretningen kan blokkeres av NAT.


Generelt vil alle protokoller som eksplisitt inkluderer den interne IP Address i pakkens nyttelast, bli påvirket, siden denne Address ikke lenger vil samsvare med den virkelige, synlige Address på Internett etter oversettelsen.


**Viktig merknad:** For å løse disse problemene tilbyr noen NAT-rutere _Deep Packet Inspection_ (DPI) eller _Protocol Helpers_ , som inspiserer pakkeinnholdet for å identifisere og dynamisk erstatte adresser eller portnumre i applikasjonsdata. Dette krever inngående kunnskap om protokollformatet, og kan skape sikkerhetsproblemer eller øke ressursbruken.


**Forsiktig: Selv om NAT bidrar til å skjule det interne nettverket og kontrollere innkommende trafikk, er det ikke en erstatning for en dedikert brannmur. Oversettelse alene er ikke en fullstendig sikkerhetsbarriere: Den må alltid suppleres med klare filtreringsregler for å blokkere uønsket eller uønsket trafikk.


for å illustrere hvordan dette fungerer i praksis, kan vi se på følgende eksempel



![Image](assets/fr/037.webp)



I dette scenariet kan en intern arbeidsstasjon få tilgang til den interne webserveren ved å ringe URL-en `http://192.168.1.20:80`. Det er valgfritt å angi porten her, siden `80` er standard HTTP-port. Hvis en forespørsel derimot kommer utenfra, vil brukeren gå inn på den offentlige Address `http://85.152.44.14:80`. NAT-ruteren mottar forespørselen, konsulterer tilordningstabellen og oversetter automatisk den offentlige Address til en privat Address, og omdirigerer forbindelsen til `http://192.168.1.20:80`.


Det samme prinsippet gjelder for alle andre servere som er autorisert til å motta Internett-tilkoblinger, for eksempel Extranet-serveren (blå krets i diagrammet).


**I virtualiserte miljøer er det vanlig å bruke nettverksgrensesnitt som kalles _virbrX_ (for _Virtual Bridge X_). Disse virtuelle broene, som særlig leveres av libvirt-biblioteket eller Xen-hypervisoren, kobler det virtuelle interne nettverket til gjestemaskinene til det fysiske nettverket samtidig som de bruker NAT. De konfigureres vanligvis via skript i `/etc/sysconfig/network-scripts/`, som vist nedenfor for `virbr0`:


```ini
NAME=""
BOOTPROTO=none
MACADDR=""
TYPE=Bridge
DEVICE=virbr0
NETMASK=255.255.255.0
MTU=""
BROADCAST=192.168.0.255
IPADDR=192.168.0.1
NETWORK=192.168.0.0
ONBOOT=yes
```


Når den virtuelle broen er på plass, må du aktivere IP-ruting og konfigurere portoversettelse med `iptables`:


```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```


```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```


Med denne konfigurasjonen rutes utgående trafikk, og NAT-oversettelse brukes, slik at virtuelle maskiner kan kommunisere med omverdenen uten å eksponere sine interne IP-adresser direkte.


I neste kapittel skal vi se nærmere på IP Address-konfigurasjon under Linux, med både enkle og avanserte metoder som passer til ulike administrasjonssammenhenger.



https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## Hvordan konfigurerer jeg nettverket med `ip`?


<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>



### Standard konfigurasjon


Etter å ha gjennomgått det teoretiske grunnlaget for nettverk og forstått hvordan IP-adresser, masker, ruting og oversettelse fungerer sammen, er det på tide å gå videre til praktisk konfigurasjon. På GNU/Linux håndteres nettverksoppsett nå med kommandoen **`ip`** (_iproute2_-pakken), som erstatter den eldre `ifconfig`.


med `ip` kan du når som helst tildele eller endre en IP Address, endre en maske, starte eller stoppe en Interface eller sjekke dens status.


**TIPS:** for å vise alle grensesnitt (aktive eller ikke): `ip addr show`


Eksempel: tilordne en statisk Address og aktivere Interface


Legg Address `192.168.1.2/24` til Interface `eth0`:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Aktiver Interface:


```shell
ip link set dev eth0 up
```


Deaktiver den samme Interface:


```shell
ip link set dev eth0 down
```


Vis statusen til en spesifikk Interface:


```shell
ip addr show dev eth2
```


**Praktisk tips:** Med `ip` er det ikke lenger nødvendig med suffikset `:1` for å legge til en ekstra Address til en Interface. Bare legg til en ny `ip addr add ...`-linje:


```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Aktiveringsskript: ifup / ifdown


Verktøyene `ifup` og `ifdown` leser statiske konfigurasjonsfiler fra `/etc/sysconfig/network-scripts/` (på RHEL, CentOS, Rocky Linux, AlmaLinux...) eller `/etc/network/interfaces` (på Debian/Ubuntu) for å ta grensesnitt opp eller ned på en ren måte.


```shell
ifup eth1
ifdown eth2
```


Konfigurasjonsfiler (RHEL-lignende):


- /etc/sysconfig/network**: globale innstillinger (NETWORKING, HOSTNAME, GATEWAY...).
- ifcfg-**: innstillinger som er spesifikke for hver Interface.


Statisk eksempel (ifcfg-eth0):


```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```


Eksempel på DHCP:


```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```


Denne modulære strukturen er fortsatt gyldig og kan enkelt automatiseres i dagens systemer.


### Avansert konfigurasjon: bonding


I profesjonelle miljøer er målet å garantere tjenestekontinuitet og/eller å aggregere båndbredde. *Bonding* (eller *teaming* med _teamd_) oppfyller disse behovene: Flere fysiske grensesnitt fungerer som én logisk Interface, ofte kalt `bond0` eller `team0`.



![Image](assets/fr/039.webp)



Forkunnskapskrav:


- Last inn `bonding`-modulen (eller bruk `teamd`) ;
- Ha minst to fysiske grensesnitt tilgjengelig.


#### De ulike vanlige limingsmetodene:


|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Sette opp med `ip link



- Deaktiver fysiske grensesnitt:


```shell
ip link set eth0 down
ip link set eth1 down
```



- Opprett den limte Interface:


```shell
ip link add bond0 type bond mode balance-alb
```



- Konfigurer alternativer etter oppretting


```shell
ip link set bond0 type bond miimon 100
```



- Tilordne MAC- og IP-adresser:


```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```



- Koble til slave-grensesnitt:


```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```



- Få alt opp igjen:


```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```


**Tips:** for å koble fra en slave uten å ta ned bindingen: `ip link set eth1 nomaster`


#### Permanent konfigurasjon (RHEL-lignende)


Opprett tre filer i `/etc/sysconfig/network-scripts`:


_ifcfg-bond0_ _ifcfg-bond0___ifcfg-bond0___ifcfg-bond0


```ini
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=none
IPADDR=192.168.2.3
NETMASK=255.255.255.0
BROADCAST=192.168.2.255
GATEWAY=192.168.2.1
BONDING_OPTS="mode=balance-alb miimon=100"
```


_ifcfg-eth0_


```ini
DEVICE=eth0
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


_ifcfg-eth1_


```ini
DEVICE=eth1
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```


Så..:


```shell
systemctl restart network
```


#### Ekstra IP Address (moderne alias)


Med `ip` kan du ganske enkelt legge til en ekstra Address til samme enhet:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


For å gjøre dette aliaset vedvarende etter en omstart, må du enten legge til en ny `IPADDR2=...` / `PREFIX2=...`-blokk i `ifcfg-eth0`, eller opprette en ny *NetworkManager*-tilkobling via `nmcli`.


Takket være `ip` og relaterte kommandoer (`ip link`, `ip addr`, `ip route`) er nettverkskonfigurasjonen mer konsekvent, skriptbar og oversiktlig. Bonding er en nøkkelkomponent i arkitekturer med høy tilgjengelighet, og det har blitt mye enklere å tilordne flere adresser til en enkelt Interface.


I neste kapittel skal vi se nærmere på detaljene og implementeringen av IPv6-adressering.


# IPv6-adressering


<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: Standarder og definisjoner


<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>



Vi går nå over til neste generasjon IP-adressering: IPv6-protokollen, opprinnelig kjent som IPng (_IP Next Generation_). Denne protokollen er utviklet for å overvinne de strukturelle begrensningene ved IPv4, og introduserer en kraftig utvidet adresseringsarkitektur samt en rekke tekniske optimaliseringer.


Motivasjonen bak innføringen av IPv6 er mangfoldig og Address avgjørende for utviklingen av Internett. For det første skal IPv6 støtte den eksponentielle veksten i antall tilkoblede enheter (et mål som er uoppnåelig med IPv4s begrensede Address-plass). For det andre har protokollen som mål å redusere størrelsen på rutingstabellene, noe som gjør utvekslingene mer effektive og reduserer arbeidsbelastningen på ruterne på lang sikt.


IPv6 søker også å forenkle visse aspekter ved pakkehåndteringen, forbedre datagramflyten og optimalisere overføringshastigheten mellom nettverk. Fra et sikkerhetssynspunkt er AH/ESP-headerne i *IPsec*-protokollen inkludert i basisspesifikasjonen, og alle IPv6-noder må kunne støtte dem (RFC 6434). Bruken av dem er imidlertid valgfri: Det er opp til administratoren å aktivere dem avhengig av konteksten.


Andre mål er mer presis håndtering av tjenestetyper, særlig for å sikre bedre kvalitet for sanntidsapplikasjoner (VoIP, videokonferanser osv.). IPv6 er også utformet for å muliggjøre mer fleksibel mobilitetsstyring: En enhet kan bytte aksesspunkt uten å endre Address på en måte som er synlig for de andre enhetene.


Endelig er IPv6 utformet for å kunne sameksistere med eldre protokoller. Selv om den ikke er direkte binærkompatibel med IPv4, er den fullt interoperabel med høyere Layer-protokoller som TCP, UDP, ICMPv6 og DNS, samt med rutingsprotokoller som OSPF og BGP, med forbehold om visse justeringer. For multicast-administrasjon bruker IPv6 MLD-protokollen (*Multicast Listener Discovery*), som er det funksjonelle motstykket til IGMP i IPv4-miljøet.


### Notasjonsregler


En av de viktigste endringene i IPv6 er formatet på selve IP Address. For å avhjelpe den kroniske mangelen på IPv4-adresser har lengden på Address blitt økt fra 32 bits til 128 bits, altså 16 byte. I teorien gir dette et mulig Address-rom på:


$$3,4 ganger 10^{38}$$$


Dette sikrer praktisk talt ubegrenset kapasitet for alt nåværende og fremtidig utstyr.


IPv6-adresser skrives på en helt annen måte enn den velkjente prikkete desimalnotasjonen. En IPv6 Address består av åtte 16-bits grupper, skrevet heksadesimalt og atskilt med kolon `:`.


For eksempel:


```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```


For å forenkle notasjonen kan ledende nuller i hver gruppe utelates. Eksemplet ovenfor blir da


```
1987:c02:0:84c2:0:0:cf2a:9077
```


I tillegg kan en enkelt sammenhengende sekvens av nullgrupper erstattes med::, noe som forkorter Address ytterligere:


```
1987:c02:0:84c2::cf2a:9077
```


**Advarsel:** Denne regelen er streng: bare én sekvens med påfølgende nuller kan erstattes av `::`. Hvis en Address inneholder flere nullsekvenser, er det bare den lengste som kondenseres. Dette sikrer både entydighet og lesbarhet.


**Viktig detalj:** tegnet `:`, som brukes til å skille heksadesimale blokker, kan føre til tvetydighet i URL-er, siden `:` også brukes til å indikere en tjenesteport. For å unngå forvirring må IPv6-adresser i URL-adresser settes i hakeparenteser `[ ]`.


Eksempel på HTTP-tilgang til en bestemt port for Address `2002:400:2A41:378::34A2:36`:


```
http://[2002:400:2A41:378::34A2:36]:8080
```


Når du representerer en IPv4 Address i en IPv6-kontekst, kan du bruke en blandet notasjon i prikket desimalform, innledet med `::`:


```
::192.168.1.5
```


Denne kompatibiliteten bidrar til å lette overgangen mellom de to protokollene ved at IPv4-blokker kan inkluderes i IPv6 Address-området.


**For å standardisere hvordan adresser skrives, definerer RFC 5952 et kanonisk format med forkortelsesregler for å unngå flere representasjoner av samme Address. Ved å følge disse anbefalingene unngår du feiltolkninger og sikrer konsekvente nettverkskonfigurasjoner.


### IPv6 Address-typer


IPv6 skiller seg fra sin forgjenger gjennom et bredt spekter av Address-kategorier, hver utformet for spesifikke bruksområder, samtidig som den gir mulighet for fleksibel ruting og nettverksadministrasjon. Som med IPv4 kan adressene være globale, lokale, reserverte eller spesifikke for visse overgangsmekanismer.


En uspesifisert IPv6 Address representeres av `::` eller, mer eksplisitt, `::0.0.0.0`. Denne spesielle formen brukes under anskaffelse av Address, eller som en standardverdi for å indikere at det ikke finnes en Address.



| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *På et privat LAN foretrekkes prefikset `fd00::/8` for å tildele interne adresser som ikke kan rutes på Internett


#### Reserverte adresser


Visse IPv6-områder er eksplisitt reservert og må ikke brukes som globale adresser. De har spesifikke tekniske formål:


- `::/128`**: uspesifisert Address, aldri permanent tilordnet en enhet, men brukt som en kilde-Address av en maskin som venter på konfigurasjon.
- `::1/128`**: _loopback_ Address, den direkte ekvivalenten til `127.0.0.1` i IPv4, som gjør det mulig for en maskin å Address seg selv.
- `64:ff9b::/96`**: Reservert for protokolloversettere for å muliggjøre IPv4/IPv6-samtrafikk, som definert i RFC 6052.
- `::ffff:0:0/96`**: kompatibilitetsblokk for å representere en IPv4 Address i en spesifikk IPv6-struktur, ofte brukt internt av applikasjoner.


Disse blokkene sikrer interoperabilitet og gjør det enklere å migrere mellom de to protokollversjonene.


#### Globale unicast-adresser


Globale unicast-adresser utgjør mesteparten av det offentlige rutbare IPv6-området, og representerer omtrent 1/8 av Address-området. Siden 1999 har IANA tildelt disse blokkene, for eksempel prefikset `2001::/16`, i CIDR-blokker (fra `/23` til `/12`) til regionale registre, som deretter distribuerer dem videre til leverandører og organisasjoner.


Noen områder har spesielle dokumenterte bruksområder:


- `2001:2::/48`**: Reserveres for testing av ytelse og interoperabilitet (RFC 5180).
- `2001:db8::/32`**: Reservert for dokumentasjon og eksempler (RFC 3849).
- `2002::/16`**: Brukes for 6to4-mekanismen, som gjør det mulig for IPv6-trafikk å reise over en IPv4-infrastruktur (nyttig i overgangsfasen mellom de to protokollene).


**En stor andel av de globale adressene forblir ubrukte, og fungerer som en reserve for fremtidig vekst på Internett.


#### Unike lokale adresser (ULA)


Unike lokale adresser (`fc00::/7`) er IPv6-ekvivalenten til private IPv4-adresser (RFC1918). De gjør det mulig å opprette isolerte interne nettverk uten å risikere konflikter med offentlig adressering. I praksis er det effektive prefikset `fd00::/8`, med den åttende biten satt til 1 for å indikere lokal bruk. Hver ULA-blokk inneholder en 40-biters pseudotilfeldige identifikator, noe som minimerer Address-kollisjoner ved tilkobling av separate private nettverk.


#### Lenkelokale adresser


Link-lokale adresser (`fe80::/64`) brukes utelukkende til kommunikasjon innenfor samme Layer 2-segment (samme VLAN eller svitsj). De rutes aldri utenfor den lokale koblingen. Hver nettverks-Interface genererer automatisk en lenkelokal Address, ofte avledet fra sin MAC-Address ved hjelp av EUI-64-ordningen.


**Spesiell funksjon**: Samme maskin kan bruke samme lenkelokale Address på flere grensesnitt, men Interface må spesifiseres ved kommunikasjon for å unngå tvetydighet.


#### Multicast-adresser


I IPv6 er broadcast erstattet av multicast, som er en mer effektiv måte å levere pakker til en definert gruppe mottakere. Multicast-adresser har prefikset `ff00::/8`. Dette inkluderer adresser som `ff02::1`, som er rettet mot alle noder på den lokale linken. Denne Address er praktisk, men anbefales ikke lenger for applikasjoner, ettersom den kan generate ukontrollerte sendinger.


En vanlig bruk av multicast er _Neighbor Discovery Protocol_ (NDP), som erstatter ARP i IPv6. NDP bruker spesifikke multicast-adresser, for eksempel `ff02::1:ff00:0/104`, for automatisk å oppdage andre verter som er koblet til samme lenke.


Ved å kombinere disse Address-typene gir IPv6 et komplett sett med alternativer for å dekke behovene for global ruting, lokal kommunikasjon, IPv4/IPv6-migrering og automatisk enhetskonfigurasjon, samtidig som overføringseffektiviteten forbedres.


### Address omfang


Omfanget av en IPv6 Address definerer det nøyaktige domenet der den er gyldig og unik. Å forstå dette konseptet er nøkkelen til å mestre pakkeruting og logisk organisering av et IPv6-nettverk. IPv6-adresser deles vanligvis inn i tre hovedkategorier basert på omfang og bruk: unicast, anycast og multicast.


**Unicast-adresser** er de vanligste og omfatter flere forskjellige undertyper.

Disse inkluderer _loopback_ (`::1`) Address, som er begrenset til verten som bruker den, og som brukes til å teste nettverksstakken internt uten å sende trafikk over det fysiske nettverket.

Så finnes det lenkelokale adresser (_link-local_), som er begrenset til et enkelt nettverkssegment: De brukes til direkte kommunikasjon mellom enheter på samme fysiske eller logiske lenke (f.eks. en enkelt svitsj eller VLAN).

Til slutt er unike lokale adresser (_ULA_, for _Unique Local Addresses_) interne i et privat nettverk. De kan rutes mellom flere private segmenter, men er aldri synlige på Internett.


Konseptuelt er IPv6-adresser ofte representert som en binær struktur der den første halvdelen (de første 64 bitene) identifiserer nettverksprefikset, og den andre halvdelen (også 64 bits) unikt identifiserer enhetens Interface i det nettverket. Denne oppdelingen gjør Address autokonfigurasjon enklere gjennom mekanismer som SLAAC (_Stateless Address Autoconfiguration_), som lar maskiner automatisk generate velge en stabil Address basert på MAC Address eller en pseudo-tilfeldig identifikator.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

IPv6-arkitekturen følger den hierarkiske globale rutingsmodellen i dagens Internett. Prefikspartisjonering gjør det mulig for regionale registre og nettverksoperatører å administrere Address-tildeling på en desentralisert måte, samtidig som global unikhet sikres. Innenfor dette rammeverket kan den samme verten samtidig ha en global unicast Address for Internett-kommunikasjon og en link-lokal Address for lokale interaksjoner, f.eks. med det umiddelbare nabolaget eller for ruteroppdagelsesmeldinger.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Anycast-adresser** representerer et mellomliggende konsept som bygger på unicast-modellen, men som i visse tilfeller kan oppføre seg som multicast. En anycast Address er i bunn og grunn en unicast Address som er tilordnet flere grensesnitt fordelt på forskjellige nettverksnoder. Når en pakke sendes til en anycast Address, forsøker IPv6-protokollen å levere den til en av vertene som deler denne Address-en, vanligvis den som ligger nærmest når det gjelder rutingstopologi. Denne tilnærmingen optimaliserer hastigheten på behandlingen av forespørsler og forbedrer robustheten til distribuerte tjenester. Et klassisk eksempel er DNS-rotserverne, der anycast-adressering automatisk leder forespørsler til det nærmeste punktet for tilstedeværelse.



| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

I IPv6 erstatter **multicast-adresser** kringkastingsmekanismen, som ble ansett som for kostbar og uegnet for et globalt nettverk. En multicast Address identifiserer en gruppe grensesnitt, vanligvis på tvers av flere verter, som ønsker å motta de samme pakkene samtidig.

Hver multicast Address inneholder et spesielt 4-biters _scope_-felt, som definerer den geografiske eller logiske grensen for sendingen:


- Et omfang på `1` betyr at pakken kun er for den lokale enheten.
- Et scope på `2` begrenser pakken til den lokale lenken: alle enheter på samme fysiske eller virtuelle segment kan motta den.
- Et omfang på `5` utvider rekkevidden til et område, vanligvis et helt bedriftsnettverk.
- Et omfang på `8` utvider rekkevidden til en organisasjon, noe som muliggjør levering på tvers av alle undernett i samme enhet.
- Et scope på `e` (14 i heksadesimal) indikerer en global rekkevidde, noe som gjør multicast-gruppen tilgjengelig fra hvor som helst på Internett hvis rutingsinfrastrukturen støtter det.


Strukturen til en IPv6 multicast Address inkluderer:


- et _Flag_-felt (4 bits) som angir om gruppen er permanent eller midlertidig,
- et _Scope_-felt (4 bits) definerer omfanget,
- et identifikasjonsfelt (112 bits) som identifiserer multicast-gruppens nummer.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Et velkjent eksempel på IPv6-multicast i praksis er _Neighbor Discovery Protocol_ (NDP). I stedet for å bruke ARP som i IPv4, bruker NDP multicast-adresser som `ff02::1:ff00:0/104` til å kringkaste nabooppdagelsesforespørsler, kun rettet mot de relevante vertene på samme kobling.


Ved å definere Address-scopes så nøyaktig strukturerer IPv6 hvordan datastrømmer sendes, mottas og rutes. Denne detaljeringsgraden gjør protokollen mer fleksibel og effektiv når det gjelder å håndtere både lokal og global kommunikasjon, samtidig som man unngår ulempene ved generalisert kringkasting.


## Address Assignment i et lokalt nettverk


<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


I dette kapittelet skal vi se på et av de mest praktiske aspektene ved IPv6-distribusjon: tildeling av IP-adresser til verter i et lokalt nettverk. IPv6-arkitekturen er utformet med tanke på fleksibilitet, slik at hver enhet kan generate sin egen Address automatisk, samtidig som den kan konfigureres helt manuelt ved behov.


Et lokalt IPv6-nettverk deler Address systematisk inn i to deler:


- de første 64 bitene representerer subnettprefikset, vanligvis oppgitt av en ruter eller en Address-autoritet;
- de resterende 64 bitene brukes av verten til å identifisere seg selv på det segmentet.

Denne modellen forenkler ruteaggregering og administrasjon av Address-blokker betraktelig.


To hovedmetoder brukes for å tildele adresser til enheter:


- Manuell konfigurasjon, der administratoren spesifiserer hver Interfaces nøyaktige Address;
- Automatisk konfigurasjon, der enhetene generate eller generate får sine egne adresser dynamisk.


Ved manuell konfigurasjon tilordner administratoren hele IPv6 Address til hver Interface. Enkelte verdier forblir reservert:


- `::/128`: uspesifisert Address, aldri permanent tildelt ;
- `::1/128`: loopback Address (_loopback_), IPv4-ekvivalent: `127.0.0.1`.


I motsetning til IPv4 finnes det ikke noe _broadcast_-konsept; kombinasjoner av "alle nuller" eller "alle enere" i vertsdelen har ingen spesiell betydning.

Manuell konfigurasjon er fortsatt nyttig i kontrollerte miljøer, men blir vanskelig å vedlikeholde i stor skala.


Det finnes flere metoder for automatisk konfigurasjon:


- Protokollen **NDP** (_Neighbor Discovery Protocol_), spesifisert i RFC4862, muliggjør *stateless* autokonfigurasjon. I denne modusen mottar verten et nettverksprefiks fra en lokal ruter, og fullfører Address selv med en identifikator basert på sin MAC Address. Denne metoden er enkel å ta i bruk, og krever ingen sentral server.
- Implementeringer som de i Windows kan generate vertsdelen pseudotilfeldige for å forbedre personvernet ved å unngå direkte eksponering av MAC Address. Avsløring av MAC Address i IPv6-pakker kan skape personvernproblemer, ettersom det gjør det mulig å spore en enhet på tvers av ulike nettverk.
- DHCPv6-protokollen: Definert i RFC3315 og ligner på DHCP som brukes for IPv4, men muliggjør en mer kontrollert og sentralisert konfigurasjon, inkludert leieavtaleadministrasjon, ekstra alternativer (DNS, MTU...) og registrering av databaser. DHCPv6 kan fungere alene eller sammen med tilstandsløs konfigurasjon for å gi ekstra parametere uten å tildele IP Address selv.


**I den MAC-baserte metoden konverteres MAC Address til en 64-bits identifikator ved hjelp av EUI-64-formatet. Denne mekanismen setter inn bytene `FF:FE` i midten av den opprinnelige MAC Address (i 48 bits), og inverterer den 7. biten for å indikere global unikhet. Resultatet er en stabil Interface-identifikator som brukes i den fullstendige IPv6 Address.


Her er et eksempel på hvordan du forvandler en MAC Address til EUI-64:


![Image](assets/fr/045.webp)



På grunn av økende bekymring for sporing av enheter aktiverer moderne operativsystemer (særlig Linux, Windows 10+, macOS og Android) nå personvernutvidelser som standard. Disse bruker tilfeldig genererte Interface-identifikatorer som fornyes med jevne mellomrom for utgående tilkoblinger, samtidig som de beholder en stabil identifikator for intern kommunikasjon (for eksempel DNS eller DHCPv6).


I likhet med DHCP i IPv4 kan automatisk tildelte IPv6-adresser ha to levetider, definert av DHCPv6-rutere eller -servere:


- Preferred lifetime*: Etter denne perioden forblir Address gyldig, men brukes ikke lenger til å initiere nye tilkoblinger;
- Gyldig levetid*: Når denne tiden utløper, fjernes Address helt fra Interface-konfigurasjonen.


Dette systemet gjør det mulig å håndtere nettverksendringer dynamisk, for eksempel ved å sikre en smidig overgang fra én Internett-leverandør til en annen. Ved å oppdatere prefikset som annonseres av rutere og justere DNS-poster parallelt, kan IPv6-migreringen gjennomføres uten merkbare tjenesteavbrudd.


**Tips:** Den kombinerte bruken av Address og DNS-livssykluser gjør det mulig å implementere en gradvis overgangsstrategi, der nye tilkoblinger flyttes til en ny topologi, mens eksisterende tilkoblinger fortsetter til deres naturlige slutt.


Kort sagt tilbyr IPv6 et bredt spekter av fleksibilitet for Address Assignment: manuell konfigurasjon, tilstandsløs eller tilstandsbasert autokonfigurasjon, DHCPv6 eller tilfeldig generering. Hver tilnærming har sine egne fordeler og begrensninger, og kan tilpasses i henhold til ønsket kontrollnivå, størrelsen på nettverket eller personvernbehov.


## Tildeling av IPv6 Address-blokker


<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### Address-distribusjon


IPv6 Address-allokeringsplanen er strukturert for å oppfylle to mål: å garantere global Address-unikthet og å muliggjøre et logisk hierarki som favoriserer aggregering og forenkling av rutingstabeller.

Som med IPv4 sitter *Internet Assigned Numbers Authority* (IANA) på toppen av dette hierarkiet. Den forvalter det globale unicast Address-området og delegerer Address-blokker til de fem regionale Internett-registrene (_RIR_).


De fem eksisterende RIR-ene er


- ARIN (Nord-Amerika),
- RIPE NCC (Europa, Midtøsten, Sentral-Asia),
- APNIC (Asia-Stillehavsregionen),
- AFRINIC (Afrika),
- LACNIC (Latin-Amerika og Karibia).


IANA tildeler IPv6-blokker av varierende størrelse til hver RIR, vanligvis mellom /23 og /12. Denne tilnærmingen gir fleksibilitet samtidig som den sikrer langsiktig skalerbarhet. RIR-ene videredistribuerer i sin tur disse blokkene til Internett-leverandører (ISP-er), store selskaper og offentlige institusjoner.


Siden 2006 har hver RIR mottatt en IPv6 /12-blokk fra IANA, en fast størrelse som er utformet for å sikre en stabil og tilstrekkelig stor reserve for fremtidig vekst. RIR-ene deler vanligvis opp disse i /23-, /26- eller /29-blokker. Internett-leverandører mottar oftest /32-blokker, selv om denne størrelsen kan variere avhengig av leverandørens størrelse og geografiske område. De tildeler vanligvis /48-blokker til kundene. Hver /48 gir 65 536 forskjellige /64-undernett (en enorm kapasitet sammenlignet med IPv4).


**Viktig merknad:** En /32-blokk inneholder nøyaktig 65 536 /48-underblokker. Dette betyr at hver ISP kan betjene titusenvis av kunder uten å bruke opp allokeringen sin. Takket være /48 vil hver kunde ha en gigantisk mengde plass til å strukturere sitt eget interne nettverk med så mange /64-segmenter som de ønsker.


Det typiske allokeringshierarkiet ser slik ut:


| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Med denne overfloden av adresser er det ikke lenger nødvendig med NAT (*Network Address Translation*), som en gang i tiden var nødvendig i IPv4 for å takle mangelen på Address. Hver vert kan ha en unik, globalt rutbar offentlig Address, noe som forenkler ende-til-ende-tilkobling og gjør det enklere å bruke protokoller som IPSec, VoIP eller innkommende tilkoblinger.


For å sjekke hvilken organisasjon en IPv6 Address tilhører, kan du bruke `whois`-kommandoen til å spørre i offentlige RIR-databaser. Denne åpenheten gjør det mulig å identifisere organisasjonen som eier et prefiks, noe som kan være nyttig for nettverks-, analyse- eller sikkerhetsformål.


### PA vs PI-adressering


Opprinnelig var IPv6-tildelingsmodellen utelukkende basert på PA-blokker (*Provider Aggregatable*), som betyr at de er knyttet til Internett-leverandøren. I denne modellen får en organisasjon sitt prefiks fra sin ISP, noe som betyr at bytte av leverandør krever omnummerering av hele infrastrukturen.


Selv om IPv6s autokonfigurasjonsfunksjoner og Address-levetid gjør det enklere å omnummerere, er det fortsatt upraktisk for organisasjoner med kritisk infrastruktur eller flere leverandørtilkoblinger for redundansbehov.


Siden 2009 har allokeringspolicyer åpnet for PI-blokker (*Provider Independent*). Disse blokkene (vanligvis /48 i størrelse) tildeles direkte til et selskap eller en institusjon av en RIR, uavhengig av en ISP. Denne modellen er spesielt godt egnet for organisasjoner som praktiserer *multihoming* (dvs. som er koblet til flere operatører samtidig). I Europa er det for eksempel RIPE-512 som beskriver retningslinjene for PI-tildelinger.


### Notasjon for subnettmaske


Som i IPv4 bruker IPv6 CIDR (*Classless Inter-Domain Routing*). Dette består i å angi antall biter som prefikset består av etter Address, ved hjelp av tegnet `/`.


Ta følgende eksempel:


```
2001:db8:1:1a0::/59
```


Dette betyr at de første 59 bitene er faste og identifiserer nettverket. Alle de resterende bitene (her 69 bits) kan brukes til å identifisere undernett eller verter.


Denne notasjonen dekker dermed adresser fra `2001:db8:1:1a0:0:0:0:0:0` til `2001:db8:1:1bf:ffff:ffff:ffff:ffff:ffff`.


Denne blokken dekker derfor et sett med 8 /64 subnett, som hver kan romme et stort antall enheter.


CIDR-notasjon muliggjør presis planlegging av Address -plass, fra store nettverk til hjemmeoppsett og virtualiserte miljøer, og oppmuntrer til ruteaggregering, noe som reduserer belastningen på ruterne og forbedrer skalerbarheten.


### IPv6-pakker og -hoder


IPv6-pakkeformatet skiller seg fra IPv4 ved å være både enklere og mer utvidbart. Et IPv6-datagram begynner alltid med en header av fast størrelse på 40 byte som inneholder all viktig rutingsinformasjon. Denne strømlinjeformede tilnærmingen, sammenlignet med IPv4s variable header-lengde (fra 20 til 60 byte), gjør det mulig for ruterne å behandle pakkene raskere og mer effektivt.


IPv6 fjerner imidlertid ikke funksjonalitet: I stedet for å integrere en rekke valgfrie felter i hovedhodet, innfører IPv6 et system med utvidelseshoder som plasseres umiddelbart etter hovedhodet. Disse valgfrie headerne gjør det mulig å legge til data eller instruksjoner som er spesifikke for bestemte funksjoner, uten å belaste vanlige pakker unødig.


Noen utvidelseshoder følger en fast struktur, mens andre kan inneholde et variabelt antall alternativer. I Disse alternativene er kodet som `{Type, Length, Value}`-tripletter:


- Feltet "Type" (1 byte) angir hva slags opsjon det er snakk om;
- De to første bitene i "Type" angir hva ruterne skal gjøre hvis alternativet ikke gjenkjennes:
 - Ignorer alternativet og fortsett behandlingen,
 - Slipp datagrammet,
 - Slipp og send en ICMP-feilmelding til kilden.
 - Slipp datagrammet uten varsel (i tilfelle multicast-pakker).
- Feltet "Length" (1 byte) angir størrelsen på feltet "Value", fra 0 til 255 byte;
- Feltet "Verdi" inneholder dataene som er knyttet til alternativet.


Her er en oversikt over de ulike typene utvidelseshoder som er definert av IPv6.


#### Hop-for-Hop-overskrift


Dette overskriften, hvis den finnes, plasseres alltid umiddelbart etter basisoverskriften. Det inneholder informasjon som må behandles av alle rutere langs pakkens vei, i motsetning til de fleste andre hoder, som vanligvis bare håndteres av destinasjonsnoden. Typiske bruksområder er å signalisere globale parametere eller be om spesifikke behandlingstrinn når pakken beveger seg gjennom nettverket.


![Image](assets/fr/047.webp)


#### Rutehode


Rutehodet angir en liste over mellomliggende adresser som pakken må passere gjennom. Det finnes to hovedmodi for ruting:


- Streng ruting: den nøyaktige banen er forhåndsdefinert
- Løs ruting: Bare visse obligatoriske trinn er spesifisert.


De fire første feltene i dette rooting-headeret er


- Next Header**: identifiserer typen av neste header;
- Routing Type**: definerer rutingsmetoden (vanligvis `0`);
- Segmenter igjen**: antall segmenter som gjenstår å krysse ;
- Address[n]**: liste over mellomliggende adresser.


Feltet "Segmenter igjen" starter med det totale antallet gjenværende segmenter og reduseres med én for hvert hopp.


![Image](assets/fr/048.webp)


#### Fragmenteringshode


I IPv6 er det bare kildeverten som har lov til å fragmentere et datagram, i motsetning til IPv4 der rutere også kan gjøre det. Alle IPv6-noder må kunne håndtere pakker på minst 1280 byte. Hvis en ruter støter på en pakke som er større enn MTU-en for neste lenke, sender den en *ICMPv6 Packet Too Big*-melding tilbake til kilden, som deretter justerer størrelsen på sine sendinger.


Fragmenteringshodet inneholder følgende felt:


- Identifikasjon**: unik datagramidentifikator for reassemblage.
- Fragmentoffset**: fragmentets posisjon i det opprinnelige datagrammet.
- M-flagg**: indikerer om flere fragmenter følger.


![Image](assets/fr/049.webp)


#### Autentiseringshode (AH)


Dette overskriften er utformet for å sikre kommunikasjon ved å verifisere både avsenderens autentisitet og dataenes integritet. Det brukes ofte sammen med IPsec-protokollen. Ved hjelp av en autentiseringskode kan mottakeren bekrefte at meldingen virkelig kommer fra den forventede avsenderen, og at den ikke har blitt endret under overføringen.


Hvis det gjøres et uredelig modifikasjonsforsøk, vil autentiseringskoden ikke lenger stemme overens, og datagrammet kan bli avvist. Denne mekanismen beskytter også mot replay-angrep ved å oppdage uautoriserte dupliseringer.


![Image](assets/fr/050.webp)


#### Overskrift for destinasjonsalternativer


Dette headeren er kun beregnet på den endelige mottakeren av datagrammet. Det kan brukes til å legge til opsjoner eller metadata som er spesifikke for applikasjonen, uten at mellomliggende rutere tar hensyn til det.


Opprinnelig var det ikke definert noe slikt alternativ i protokollen. Dette toppteksten ble imidlertid innført da IPv6 ble utviklet, slik at fremtidige utvidelser kunne legges til uten å endre den generelle pakkestrukturen. Null-alternativet brukes for eksempel bare til å fylle ut headeren til et multiplum av 8 byte av hensyn til minnejustering.


![Image](assets/fr/051.webp)


IPv6-pakkedesignet bygger på et klart skille mellom et minimalt basishode og modulære utvidelseshoder. Denne arkitekturen sikrer både standard prosesseringsytelse og den fleksibiliteten som trengs for å utvikle protokollen og integrere sikkerhet, kompleks ruting eller mekanismer for tjenestekvalitet, samtidig som kompatibiliteten med fremtidige infrastrukturer opprettholdes.


## Forholdet mellom IPv6 og DNS


<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


I moderne nettverk oversetter DNS (*Domain Name System*) domenenavn til IP-adresser som maskinene kan bruke. Med innføringen av IPv6 måtte DNS tilpasse seg for å støtte 128-bits adresser, samtidig som bakoverkompatibiliteten med IPv4 ble opprettholdt. Denne sameksistensen er spesielt viktig i dual-stack-miljøer, der begge IP-versjonene fungerer samtidig.


### IPv6-spesifikke DNS-poster


For å knytte et domenenavn til en IPv6 Address bruker DNS en AAAA-post (*quad-A*), tilsvarende "A"-posten for IPv4-adresser. AAAA-oppføringen tilordner eksplisitt et domenenavn til en IPv6 Address.

Eksempel:


```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```


Denne oppføringen indikerer at domenet `ipv6.mydmn.org` løses opp til IPv6 Address `2001:66c:2a8:22::c100:68b`. Det er mulig, og til og med anbefalt for maksimal kompatibilitet, å knytte det samme domenenavnet til flere IP-adresser, enten det er IPv4 (via en A-post) eller IPv6 (via en AAAA-post). Dette gjør det mulig for IPv6-kompatible kunder å foretrekke IPv6, samtidig som man sikrer at klienter som kun bruker IPv4, fortsatt støttes.


I tillegg støtter DNS omvendt oppløsning, noe som betyr at den kan slå opp domenenavnet som er knyttet til en gitt IP Address. Når det gjelder IPv6, bruker denne operasjonen PTR-poster som er plassert i sonen `ip6.arpa`. Denne sonen er spesifikt reservert for IPv6 reversoppløsning. For IPv4 er det sonen `in-addr.arpa`.


### Omvendt oppløsning


Omvendt oppløsning av en IPv6 Address følger en streng prosess:

1) Utvid Address til full heksadesimal notasjon (16 byte, dvs. 32 heksadesimale sifre).

Eksempel:


```shell
2001:66c:2a8:22::c100:68b
```


Blir:


```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```


2) Snu rekkefølgen på hvert heksadesimalt siffer (nibble), skill dem med prikker og legg til `ip6.arpa`:


```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```


Denne strukturen sikrer standardiserte, unike omvendte oppslag i IPv6 Address-området.


**Vær oppmerksom på**: DNS-forespørsler kan sendes over enten IPv4 eller IPv6. Hvilken transportprotokoll som brukes, har ingen innvirkning på hvilken type oppføringer som returneres.

For eksempel:


- En klient som er tilkoblet via IPv6, kan be om en IPv4-post.
- En klient som er tilkoblet via IPv4, kan be om en IPv6-post.

DNS-serveren svarer ganske enkelt med de postene den har, uavhengig av spørringens transportprotokoll.


Når et vertsnavn er mappet til både IPv4 og IPv6, styres valget av hvilken Address som skal brukes, av RFC 6724, som definerer en algoritme for valg av Address basert på faktorer som prefikspreferanse, omfang og rekkevidde. Som standard foretrekkes IPv6, med mindre dette overstyres av system- eller nettverkskonfigurasjon.


**Viktig påminnelse**: Når du legger inn en IPv6 Address i en URL (*Uniform Resource Locator*), må den være omgitt av hakeparenteser (`[]`). Slik unngår du forvirring mellom kolon (`:`) inne i IPv6 Address og kolon som skiller vertsnavnet fra porten i URL-adressen.


Gyldig eksempel:


```shell
http://[2001:db8::1]:8080
```


Dette sikrer at nettadressen behandles riktig av både nettlesere og webservere.


Integrering av IPv6 i DNS-systemet er derfor avhengig av nye record-typer, en streng metode for omvendt oppløsning og presise regler for valg og formatering for å sikre kompatibilitet og konsistens i rutingen.


### Del sammendrag


I denne delen har vi utforsket de grunnleggende prinsippene for IPv6-adressering. Vi begynte med å se på strukturen i IPv6 Address: 128-biters lengde, heksadesimal notasjon og forenklingsreglene som brukes til å forkorte gjentatte sekvenser av nuller. Denne utformingen gjør det mulig for IPv6 å overvinne begrensningene i IPv4s Address-område, samtidig som den garanterer skalerbarhet og effektivt hierarki.


Deretter tok vi for oss de ulike kategoriene av IPv6-adresser: unicast, anycast og multicast, og beskrev deres omfang, typiske bruk og representasjon i Address-rommet.


Deretter gjennomgikk vi metodene for å tildele IPv6-adresser i et lokalt nettverk, enten ved manuell konfigurasjon, via DHCPv6-protokollen eller ved hjelp av tilstandsløse autokonfigurasjonsmekanismer, slik som NDP tilbyr. Disse metodene gjør det mulig for enheter å automatisk generate sin egen Address ut fra det angitte prefikset og MAC Address (via EUI-64), samtidig som de gir fleksibilitet når det gjelder levetidsstyring og personvern.


Vi har også beskrevet hvordan Address-blokker allokeres, med utgangspunkt i IANA, som distribuerer dem til de fem RIR-ene (*Registered Internet Regions*), og deretter til Internett-leverandørene, som videredistribuerer dem til kundene sine som undernett (ofte i /48, noe som tillater 65536 /64-undernettverk). Skillet mellom _Provider Aggregatable_ (PA)- og _Provider Independent_ (PI)-blokker bidrar til å håndtere _multihoming_ eller leverandørbyttescenarioer.


Vi så at DNS har tilpasset seg IPv6 med innføringen av AAAA-posten, og at mekanismene for omvendt oppløsning nå baserer seg på sonen `ip6.arpa`. Det er viktig å merke seg at DNS forblir uavhengig av hvilken transportprotokoll som brukes (IPv4 eller IPv6), noe som sikrer sømløs interoperabilitet i et dual-stack-miljø.


IPv6 er derfor ikke bare en inkrementell forbedring i forhold til IPv4, men en fullstendig redesign av adresseringssystemet, bygget for å møte både dagens og fremtidens utfordringer på det globale Internett.


I den siste delen av dette NET 302-kurset går vi over til praksis og fokuserer på verktøy for nettverksdiagnostikk.



# Verktøy for nettverksdiagnostikk


<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Verktøy for nettverkstilgang Layer


<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


I dette første kapittelet i den siste delen om nettverksdiagnostikk fokuserer vi på verktøy for analyse av nettverkstilgangen Layer i TCP/IP-modellen. Denne Layer er ansvarlig for direkte kommunikasjon mellom enheter i det samme fysiske nettverket, særlig gjennom bruk av MAC-adresser og fysiske nettverksgrensesnitt som Ethernet-kort eller Wi-Fi-grensesnitt.


Målet her er å gi administratorer praktiske verktøy for å inspisere, teste og optimalisere denne essensielle Layer av lavnivåtilkobling. Disse verktøyene kan brukes til å verifisere at grensesnittene fungerer som de skal, feilsøke konfigurasjonsproblemer for nettverkskort eller oppdage avvik som kollisjoner, pakketap eller koblingsfeil.


### Verktøy for IP/MAC-nabolag


#### verktøyet `Arp


Et av de eldste diagnoseverktøyene i Network Access Layer er kommandoen `arp`. Selv om den i økende grad erstattes av moderne alternativer som `ip neigh` (som vi snart skal se nærmere på). `Arp` finnes fortsatt på mange systemer for å vise eller manipulere ARP-cachen (*Address Resolution Protocol*). Denne cachen lagrer tilordningene mellom IP-adresser og MAC-adresser som er kjent lokalt på en maskin. Med andre ord kan du finne ut hvilken fysisk (MAC) Address som tilsvarer en gitt IP Address i det lokale nettverket.


I praksis må en vert som ønsker å sende en pakke til en IP Address innenfor samme delnett, først kjenne til målmaskinens MAC Address. Denne tilordningen håndteres av ARP, som sender ut en forespørsel i det lokale nettverket og mottar et svar som inneholder den tilsvarende MAC Address. Dette resultatet lagres midlertidig i en lokal tabell som kalles "ARP-cache", slik at man unngår å gjenta forespørselen for hver nye pakke.


Hvis du vil vise innholdet i denne hurtigbufferen og sjekke hvilke oppføringer som er kjent for maskinen, bruker du :


```bash
arp -a
```


Denne kommandoen viser en liste over alle lokalt registrerte IP/MAC-tilordninger på tvers av alle grensesnitt. Hver linje inneholder vertsnavnet (hvis det kan løses), IP Address, den tilsvarende MAC Address og Interface der tilordningen er observert.


Hvis du vil filtrere visningen til en bestemt IP Address, angir du den ganske enkelt:


```bash
arp -a 192.168.1.5
```


Dette gjør det enkelt å sjekke om en bestemt IP Address finnes i hurtigbufferen, noe som kan bidra til å diagnostisere kommunikasjonsfeil mellom to verter i samme nettverk.


På samme måte kan du bruke for å vise bare ARP-oppføringene som er knyttet til et bestemt nettverk Interface (for eksempel et Ethernet-kort med navnet `eth0`):


```bash
arp -a -i eth0
```


Dette er spesielt nyttig i miljøer med flere Interface (kablet, trådløst, VPN osv.), der én vert kan ha flere nettverkskort.


Kommandoen `arp` er ikke begrenset til skrivebeskyttet bruk. Den kan også brukes til å redigere ARP-cachen manuelt, noe som er en uvurderlig funksjon i visse avanserte feilsøkingsscenarier eller ved simulering av spesifikke forhold. Du kan for eksempel legge til en IP/MAC-tilordning manuelt:


```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```


Denne kommandoen oppretter en statisk oppføring i den lokale ARP-tabellen og knytter IP Address `192.168.1.7` til MAC Address `00:17:BC:56:4F:25` på Interface `eth2`. Hvis ingen Interface er spesifisert, bruker systemet automatisk den første aktuelle Interface.


Du kan også fjerne en oppføring fra ARP-cachen, enten for å rette en feil eller for å fremtvinge en ny gjenoppdagelse:


```bash
arp -d 192.168.1.7
```


Dette sletter oppføringen og sikrer at neste kommunikasjonsforsøk utløser en ny ARP-forespørsel.


**MERK**: Slettealternativet aksepterer også et Interface-navn, slik at du kan målrette fjerningen av en spesifikk oppføring mer nøyaktig.


Oppsummert kan man si at verktøyet `arp` gir diagnostikk på lavt nivå, noe som er spesielt nyttig i lokale nettverk der tilkoblingsproblemer ofte kan spores tilbake til feil eller foreldet Address-oppløsning. På nyere systemer, spesielt på moderne Linux-distribusjoner, blir imidlertid dette verktøyet i økende grad erstattet av kommandoen `ip neigh` fra `iproute2`-verktøysettet, som tilbyr lignende funksjonalitet i et mer enhetlig rammeverk.


#### verktøyet `Ip neigh`


På moderne systemer, særlig nyere Linux-distribusjoner, er kommandoen `ip neigh` det foretrukne verktøyet for å inspisere og administrere mappinger mellom IP- og MAC-adresser. Denne kommandoen er en del av `iproute2`-pakken, som gradvis erstatter eldre verktøy som `arp`, og som gir et mer konsistent og fleksibelt rammeverk for diagnostikk på datalink Layer.


Kommandoen `ip neigh` spør etter den lokale IP-nabo-cachen, som tilsvarer ARP-cachen for IPv4 og NDP-cachen (_Neighbor Discovery Protocol_) for IPv6. Denne hurtigbufferen lagrer kjente assosiasjoner mellom IP-adresser (v4 eller v6) og MAC-adresser, sammen med deres status (gyldig, ventende, utløpt...).


Den grunnleggende kommandoen for å vise hurtigbufferen er


```bash
ip neigh
```


Dette gir en liste over oppføringer som viser destinasjonens IP Address, det relevante nettverket Interface, den tilknyttede MAC Address (hvis tilgjengelig) og oppføringens status (f.eks. `REACHABLE`, `STALE`, `DELAY`, `FAILED`...).


Eksempel på utdata:


```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```


Denne linjen indikerer at maskinen kjenner til en gyldig mapping mellom IP Address `192.168.1.5` og MAC Address `00:17:BC:56:4F:25` via Interface `eth0`.


Du kan også filtrere oppføringer etter kriterier som IP Address, Interface eller tilstand. For eksempel, for å søke etter bare Address `192.168.1.7`:


```bash
ip neigh show 192.168.1.7
```


Eller for å vise alle oppføringer for Interface `eth1`:


```bash
ip neigh show dev eth1
```


I tillegg til konsultasjon kan `ip neigh` også brukes til å redigere hurtigbufferen manuelt. For eksempel for å legge til en statisk oppføring:


```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```


Dette knytter IP Address `192.168.1.7` permanent til den angitte MAC Address på Interface `eth1`. Alternativet `nud permanent` (for _Neighbor Unreachability Detection_) sikrer at oppføringen ikke blir ugyldiggjort automatisk.


Motsatt for å slette en cache-oppføring:


```bash
ip neigh del 192.168.1.7 dev eth1
```


Dette tvinger systemet til å løse mappingen på nytt neste gang det kommuniserer med den aktuelle Address.


**MERKNAD**: Verktøyet `ip neigh` fungerer både for IPv4 og IPv6. For IPv4 har det et grensesnitt mot ARP, mens det for IPv6 samhandler med NDP. Dette gir en enhetlig, konsistent tilnærming til håndtering av IP/MAC-relasjoner på tvers av protokollfamilier, noe som gjør `ip neigh` til den moderne standarden for nabohåndtering på Linux-systemer.


### Verktøy for pakkeanalyse


For å kunne analysere hva som skjer i et datanettverk, trenger administratorer verktøy som kan fange opp pakkene som utveksles mellom maskinene. To verktøy skiller seg ut som referansepunkter: `tcpdump` og `Wireshark`. Disse verktøyene er avgjørende for å diagnostisere unormal oppførsel, overvåke protokollutvekslinger eller studere nettverkssikkerhet ved å inspisere rammeinnholdet.


#### `ttcpdump`: kommandolinjeanalyse


`tcpdump` er et svært kraftig kommandolinjeverktøy som er utviklet for å fange opp og vise pakker som beveger seg gjennom et nettverk Interface. Det fungerer i sanntid, og takket være den lette designen kan det brukes på systemer uten en grafisk Interface eller med begrensede ressurser. Det er avhengig av `libpcap`-biblioteket, som tilbyr maskinvareuavhengige lavnivåfunksjoner for innfanging.


En vanlig bruk av `tcpdump` er å overvåke nettverksaktiviteten til en maskin eller et nettverkssegment ved å filtrere pakker i henhold til bestemte kriterier. Resultatene kan videresendes til en fil, slik at trafikken kan arkiveres for senere analyse eller avspilles på nytt i et annet verktøy, for eksempel Wireshark.


Den generelle kommandosyntaksen er


```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```



- `-w` skriver innfangede pakker til en fil i `libpcap`-format (utvidelse `.cap` eller `.pcap`);
- `-i` angir nettverket Interface som skal overvåkes (f.eks. `eth0`, `wlan0`);
- `-s` angir den maksimale mengden data som fanges opp per pakke. Ved å angi `0` fanges alle pakkene opp;
- `-n` deaktiverer DNS- og tjenestenavnoppløsning, noe som forbedrer ytelsen.


Med uttrykksfiltre på slutten av kommandoen kan du begrense datafangsten til en delmengde av trafikken. Du kan kombinere nøkkelordene `host`, `port`, `src`, `dst` osv. for å avgrense utvalget.


Eksempel: for å fange HTTP-pakker (port 80) til eller fra serveren `192.168.25.24`, og lagre dem i en `fichier.cap`-fil:


```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```


Den resulterende filen kan senere analyseres i et grafisk verktøy eller spilles av på et annet system.


#### Wireshark: avansert visuell analyse


Wireshark, tidligere kjent som *Ethereal*, er et komplett nettverksanalyseprogram med en grafisk Interface. I motsetning til `tcpdump` gir det strukturert, detaljert visualisering av pakker, inkludert protokolldisseksjon, flytdiagrammer, trafikkstatistikk og interaktive filtre. Det er også avhengig av `libpcap`, noe som betyr at det kan åpne og behandle fangstfiler generert av `tcpdump`.


Wireshark er tilgjengelig på mange operativsystemer, inkludert Linux og Windows. Installasjon krever administratorrettigheter for å få tilgang til opptaksgrensesnittene. Når programmet er startet, kan du velge et nettverk Interface fra *Capture*-menyen. Ved å klikke på *Start* starter du sanntidsopptak av pakker. Skjermbildet er delt inn i tre ruter:


- listen over bilder som er tatt ;
- protokollavkodede detaljer,
- rå heksadesimale data.



![Image](assets/fr/052.webp)



Wireshark er utmerket i scenarier der du trenger å observere kompleks protokollatferd, rekonstruere applikasjonsdialoger (for eksempel en HTTP- eller DNS-økt) eller studere responstider for tjenester. Den støtter også svært spesifikke visningsfiltre ved hjelp av en egen syntaks (forskjellig fra `tcpdump`) for å fokusere kun på relevante pakker.


#### Utfyllende verktøy


Det er viktig å merke seg at `tcpdump` og Wireshark ikke er utskiftbare: De har hver sine styrker. `tcpdump` er bedre egnet for kommandolinjemiljøer, automatiserte skript og eksterne serverintervensjoner, mens Wireshark er ideell for detaljert, interaktiv og pedagogisk trafikkanalyse.


De to verktøyene kan kombineres: Man kan foreta en oppsamling på et eksternt system med `tcpdump`, og deretter overføre `.cap`-filen for analyse med Wireshark på en lokal maskin. Denne tilnærmingen er mye brukt i praksis.


### Analyseverktøy for Interface


På Network Access Layer er det ofte nødvendig å spørre og konfigurere fysiske nettverksgrensesnitt for å diagnostisere funksjonsfeil, optimalisere ytelsen eller verifisere tilkoblingsintegriteten. Et av de kraftigste verktøyene som er tilgjengelige under Linux for dette formålet, er `ethtool`, et kommandolinjeverktøy som ikke bare gir detaljert teknisk informasjon om en Ethernet Interface, men som også gjør det mulig å justere noen av parameterne i sanntid.


#### Se spesifikasjonene for Interface


En av kjernefunksjonene i `ethtool` er muligheten til å spørre etter en Interface og vise dens nåværende egenskaper. Dette gjør at du kan sjekke:


- koblingshastighet (f.eks. 100 Mbit/s, 1 Gbit/s eller 10 Gbit/s) ;
- forhandlingsmodus (halv dupleks eller full dupleks) ;
- om autonegotiasjon er aktivert;
- type port (kobber, fiber osv.) ;
- koblingsstatus (aktiv eller ikke) ;
- støtte for avanserte funksjoner som *Wake-on-LAN*.


Denne informasjonen er spesielt nyttig for å diagnostisere problemer knyttet til fysisk tilkobling eller uoverensstemmende forhandlingsinnstillinger mellom vertens nettverkskort og utstyret det er koblet til (svitsj, ruter osv.).


For å få denne informasjonen, kjører du ganske enkelt:


```bash
ethtool enp0s3
```


Denne kommandoen gir en detaljert rapport om `enp0s3` Interface, en vanlig navnekonvensjon på CentOS- eller RHEL-baserte systemer.



![Image](assets/fr/053.webp)



#### Dynamisk modifisering av Interface-parametere


`ethtool` er ikke begrenset til observasjon: Det lar deg også justere visse Interface-parametere uten å starte maskinen på nytt. Dette gjør det for eksempel mulig å tvinge frem en bestemt koblingshastighet eller aktivere funksjoner i henhold til behovene i det lokale nettverket.


Alternativet `-s` brukes til dynamisk konfigurering av parametere som f.eks:


- linkhastighet (`speed`), angis eksplisitt (f.eks. 1000 for 1 Gbit/s) ;
- dupleksmodus (`duplex`), enten `half` eller `full` ;
- aktivere eller deaktivere autonegotiasjon (`autoneg`) ;
- aktivering av *Wake-on-LAN* (`wol`) ;
- havnetype.


Eksempel 1: Aktiver autonegotiation på en Interface:


```bash
ethtool -s enp0s3 autoneg on
```


Eksempel 2: aktiver *Wake-on-LAN*-funksjonen (slik at maskinen kan vekkes eksternt via en magisk pakke):


```bash
ethtool -s enp0s3 wol p
```


I dette eksemplet angir alternativet `p` at oppvåkning skal skje så snart en *Wake-on-LAN*-pakke blir oppdaget. Dette oppsettet brukes ofte i bedriftsmiljøer for å utføre oppdateringer eller fjernvedlikehold over natten.


#### Installasjon av verktøy


Det er viktig å merke seg at `ethtool` ikke alltid er installert som standard. På Red Hat/CentOS-distribusjoner kan det installeres med kommandoen:


```bash
yum install -y ethtool
```


På Debian og Ubuntu er den tilsvarende kommandoen


```bash
sudo apt install ethtool
```


**ADVARSEL**: I alle `ethtool`-kommandoer må navnet på nettverket Interface angis umiddelbart etter alternativet (som `-s`). Enhver syntaksfeil i plasseringen av parametere vil gjøre kommandoen ugyldig eller ineffektiv.



## Layer-nettverksverktøy


<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Verktøy for trafikkanalyse


I nettverksdiagnostikk er `ping`-kommandoen fortsatt et av de enkleste, men samtidig kraftigste verktøyene for å teste forbindelsen mellom to maskiner. Den sjekker om en ekstern vert kan nås på et gitt tidspunkt, samtidig som den gir informasjon om ventetid, linkstabilitet og DNS-oppløsning.


Kommandoen `ping` er avhengig av ICMP-protokollen (*Internet Control Message Protocol*). Når en bruker sender en `ping`-forespørsel, sender systemet en ICMP "Echo Request"-pakke til en IP Address eller et vertsnavn. Hvis målmaskinen er online og nettverksbanen er gyldig, svarer den med en ICMP "Echo Reply"-pakke. Denne enkle mekanismen kan brukes til å måle ventetid og oppdage problemer med tilkobling eller navneløsning.


Eksempel på en klassisk kommando:


```bash
ping 172.17.18.19
```


Typisk svar:


```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```


I dette eksemplet har navneoppløsningen blitt utført automatisk: domenet `mydmn.org` er knyttet til IP Address `172.17.18.19`, noe som bekrefter at DNS-oppløsningen fungerer som den skal. Kommandoen gir også tekniske detaljer som f.eks:


- iCMP-sekvensnummer (`icmp_seq`), nyttig for å sjekke rekkefølgen på svarene;
- TTL (*Time-To-Live*), som angir antall gjenværende hopp før pakken forkastes;
- round-trip time/delay (`time`), uttrykt i millisekunder, som gir et estimat av forsinkelsen på lenken.


#### Mer detaljert analyse av ICMP-parametere


TTL er et kritisk felt i IP-protokollen. Hvert datagram initialiseres med en TTL-verdi av avsenderen (ofte 64, 128 eller 255). Hver ruter langs stien reduserer denne verdien med 1. Hvis TTL-verdien når 0 før den når destinasjonen, forkastes pakken, og en ICMP-feilmelding sendes tilbake til avsenderen. Denne mekanismen forhindrer uendelige rutingsløyfer.


Forplantningstiden (*rundreiseforsinkelse/tid*) måler forsinkelsen det tar for en pakke å forlate avsenderen, nå målet og komme tilbake. I praksis anses en forsinkelse på under 200 ms som akseptabel for en stabil kobling. Unormalt høye forsinkelser kan tyde på overbelastning i nettverket, ineffektiv ruting eller dårlig koblingskvalitet.


#### Avansert `ping`-bruk


`ping` gir muligheter for å avgrense tester og observere spesifikk nettverksatferd.


Hvis du vil sende broadcast-forespørsler, kan du bruke alternativet `-b` for å sende til alle verter i et delnett:

```bash
ping -b 192.168.1.255
```


Dette er nyttig i lokale nettverk for raskt å oppdage aktive verter eller teste hvordan nettverket håndterer kringkastingsforespørsler. I mange oppsett blokkerer imidlertid rutere og brannmurer kringkastingspinger for å forhindre forsterkningsangrep.


Du kan også angi et egendefinert intervall mellom forespørsler med alternativet `-i` (standard: 1 sekund):


```bash
ping -i 0.2 -c 10 192.168.1.7
```


Denne sender 10 ICMP-forespørsler med 0,2 sekunders intervaller. Slike tester er nyttige for å oppdage svingninger i latenstid over en kort periode eller for å utsette en kobling for lett stress for å evaluere stabiliteten.


### Analyseverktøy for rutetabeller


Kommandoen `ip route`, som er en del av `iproute2`-pakken, er det anbefalte standardverktøyet på moderne Linux-systemer for å inspisere og administrere kjernens IP-rutingstabell. Den erstatter den foreldede `route`-kommandoen, og tilbyr klarere syntaks, større konsistens og utvidet støtte for moderne funksjoner (IPv6, flere tabeller, navneområder osv.).


#### Vise rutingstabellen


Slik viser du den gjeldende rutingstabellen:


```bash
ip route show
```


Denne utdataene viser alle ruter som er kjent for kjernen, det vil si hvilke veier utgående pakker tar avhengig av destinasjonen.


Eksempel på utdata:


```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```


Hver linje representerer en rute. Viktige felt inkluderer:


- default**: standardruten, som brukes når det ikke finnes noen mer spesifikk rute.
- via**: gatewayen som brukes for å nå destinasjonen.
- dev**: nettverket Interface som brukes.
- proto**: hvordan ruten ble opprettet (manuell, DHCP, kjernen osv.).
- metric**: rutekostnad, brukes til å prioritere flere mulige stier.
- scope**: ruteomfang (f.eks. `link` for en direkte tilkoblet rute).
- src**: kilde-IP Address som brukes for utgående pakker på denne Interface.


#### Legge til og slette ruter


Du kan også endre rutingstabellen dynamisk, for eksempel ved å legge til eller fjerne statiske ruter.


Legge til en statisk rute:


```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```


Dette konfigurerer en rute til nettverket `192.168.1.0/24` via gatewayen `192.168.1.1` på Interface `eth0`.


Fjern denne ruten:


```bash
ip route del 192.168.1.0/24
```


Denne kommandoen sletter den tidligere definerte ruten.


#### Nyttige kommandoer


Her er noen nyttige varianter for analyse eller skripting:


- `ip -4 route`: viser bare IPv4-ruter;
- `ip -6 route`: viser bare IPv6-ruter;
- `ip route list table main`: viser hovedrutetabellen for ruting (standardverdi) ;
- `ip route get <Address>`: viser hvilken Interface og gateway en pakke til den gitte Address vil bruke.


Eksempel:


```bash
ip route get 8.8.8.8
```


Dette viser den nøyaktige ruten en pakke vil ta for å nå `8.8.8.8.8`.


### Sporingsverktøy


Et av de mest effektive verktøyene for å analysere ruten som IP-pakker tar mellom en kildevert og en måldestinasjon, er kommandoen `traceroute`. Den viser steg for steg hvilken vei pakkene følger, og identifiserer de mellomliggende ruterne de passerer. I tilfelle feil på en nettverkslenke eller et tjenesteavbrudd kan `traceroute` bidra til å lokalisere problemet nøyaktig.


Som med kommandoen `ping` kan målet spesifiseres enten ved hjelp av det fullt kvalifiserte domenenavnet (FQDN) eller ved hjelp av IP Address. For eksempel


```bash
traceroute mydmn.org
```


#### Driftsprinsipp


`traceroute` baserer seg på TTL-feltet (*Time To Live*) i IP-pakkenes header. Som forklart tidligere, er dette feltet en teller som reduseres av hver ruter langs stien. Når TTL når null, forkastes pakken, og ruteren returnerer en ICMP-melding om "Time Exceeded" til avsenderen. Denne mekanismen forhindrer uendelige løkker i tilfelle feilruting.


`traceroute` utnytter denne atferden til å kartlegge ruterne mellom avsender og mottaker:


- Den sender først en serie UDP-pakker (vanligvis tre) med en TTL på 1. Den første ruteren får en TTL på 0, så den forkaster pakken og svarer deretter med en ICMP-melding som avslører IP Address og responstid.
- Deretter sender den en ny serie med pakker med en TTL på 2, noe som avslører den andre ruteren.
- Prosessen gjentas til destinasjonen er nådd, og da svarer verten med en ICMP Port Unreachable-melding, som indikerer at endepunktet er nådd.


Som standard bruker `traceroute` UDP-pakker som sendes til ubrukte porter (vanligvis fra 33434), men kan også konfigureres til å bruke ICMP (som `ping`) eller til og med TCP, avhengig av system eller kommandovarianter.


Eksempel på utdata:


```bash
traceroute to www.google.fr (216.58.210.35), 64 hops max, 52 byte packets

1  par81-024.ff.avast.com (62.210.189.205)   25.107 ms  24.235 ms  24.383 ms
2  62-210-189-1.rev.poneytelecom.eu (62.210.189.1)  27.341 ms  27.119 ms  28.184 ms
3  a9k1-45x-s43-1.dc3.poneytelecom.eu (195.154.1.92)  25.910 ms  25.040 ms  25.558 ms
4  72.14.218.182 (72.14.218.182)  36.234 ms  39.907 ms  38.130 ms
5  108.170.244.177 (108.170.244.177)  25.880 ms
108.170.244.240 (108.170.244.240)  25.791 ms
108.170.244.177 (108.170.244.177)  26.449 ms
6  216.239.62.143 (216.239.62.143)  26.491 ms
216.239.43.157 (216.239.43.157)  26.414 ms
216.239.62.139 (216.239.62.139)  26.400 ms
...
9  108.170.246.161 (108.170.246.161)  33.174 ms
108.170.246.129 (108.170.246.129)  34.342 ms
108.170.246.161 (108.170.246.161)  33.707 ms
10  108.170.232.105 (108.170.232.105)  33.845 ms  33.846 ms
108.170.232.103 (108.170.232.103)  34.206 ms
11  lhr25s11-in-f35.1e100.net (216.58.210.35)  34.094 ms  33.353 ms  33.718 ms
```


Hver linje tilsvarer en ruter som er passert, med opptil tre tidsmålinger (i millisekunder) som angir latenstiden for rundturen til den aktuelle ruteren. Disse verdiene bidrar til å vurdere ytelsen til hvert nettverkssegment.


#### Tolkning av resultat


Hvis en ruter ikke svarer eller filtrerer ICMP-meldinger, vises asterisker `*` i stedet for svartiden. Dette kan være en indikasjon:


- en brannmur som blokkerer ICMP-svar,
- en enhet som er konfigurert til ikke å svare, eller
- et midlertidig tilkoblingsproblem langs stien.


Traceroute identifiserer ikke bare ruten som er tatt, men fremhever også punkter med unormal ventetid eller avbrudd.


På noen systemer kan den tilsvarende kommandoen `tracepath` brukes, som ikke krever root-rettigheter. For IPv6 kan du bruke `traceroute6` eller `tracepath6`.


Eksempel for IPv6-sporing:


```bash
traceroute6 ipv6.google.com
```


### Verktøy for å sjekke aktive tilkoblinger


For å diagnostisere aktive nettverkstilkoblinger og overvåke nettverksaktiviteten på et Linux-system er kommandoen `ss` (forkortelse for _socket statistics_) det moderne referanseverktøyet. Den er en del av `iproute2`-pakken, og erstatter den nå utdaterte `netstat`, som gir bedre ytelse og mer nøyaktige resultater.


`ss` viser aktive TCP- og UDP-tilkoblinger, lytteporter, lokale og eksterne adresser, tilkoblingsstatus og tilknyttede prosesser.


#### Generell bruk


Når kommandoen `ss` kjøres uten alternativer, viser den aktive TCP-tilkoblinger. Grunnleggende syntaks:


```bash
ss [options]
```


Noen vanlige alternativer for å avgrense analysen:


- `-t`: viser bare TCP-tilkoblinger;
- `-u`: viser bare UDP-tilkoblinger;
- `-l`: viser bare lyttestikkontakter;
- `-n`: deaktiverer navneløsning (rå IP-er og portnumre) ;
- `-p`: viser hver socket-tilknyttede prosess (PID og programnavn),
- `-a`: viser alle tilkoblinger, inkludert inaktive,
- `-s`: viser socketstatistikk på høyt nivå.


#### Casestudier


Slik viser du alle aktive tilkoblinger som bruker TCP-port 80 (HTTP):


```bash
ss -ant | grep ':80'
```


Dette viser aktive TCP-tilkoblinger som involverer port 80. Tilstander som `LISTEN`, `ESTABLISHED`, `TIME-WAIT` angir gjeldende status for hver Exchange.


Eksempel på utdata:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```


Slik viser du alle nettverkstilkoblinger med tilhørende prosesser:


```bash
ss -tulnp
```


For å få en samlet oversikt over socketbruken:

```bash
ss -s
```


For å filtrere kun UDP-tilkoblinger:

```bash
ss -unp
```


Disse kommandoene er spesielt nyttige for å oppdage mistenkelige tilkoblinger, uventede lytteporter eller overvåke aktiviteten til en bestemt tjeneste.


## Transport og topp Layer-verktøy


<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### Verktøy for DNS-spørring


I de øvre lagene av TCP/IP-modellen, spesielt i applikasjons-Layer, er det viktig å forstå hvordan navneløsning fungerer. Med DNS-spørringsverktøy kan du kontrollere om et domenenavn er korrekt knyttet til en IP Address, og du kan også diagnostisere problemer med DNS-servere, for eksempel feilkonfigurasjon, spredningsforsinkelser eller manglende tilgjengelighet. Disse verktøyene er uunnværlige for alle nettverksadministratorer og brukere som ønsker en dypere forståelse av DNS-utveksling i et IP-miljø.


#### Kommandoen `nslookup`


Det enkleste DNS-spørringsverktøyet er `nslookup`. Det sender en forespørsel til en DNS-server og returnerer IP Address som er knyttet til et domenenavn (eller omvendt). Som standard spørres det etter systemets konfigurerte DNS-server, men du kan også angi en server direkte i kommandoen.


Eksempel på et direkte oppslag:

```bash
nslookup mydmn.org
```


Forespørsel til en bestemt DNS-server:

```bash
nslookup mydmn.org 192.6.23.4
```


Forespørselen ber DNS-serveren på `192.6.23.4` om å løse navnet `mydmn.org`. Dette er spesielt nyttig for å sjekke om en gitt DNS-server gjenkjenner et domenenavn eller for å kontrollere at serveren fungerer som den skal.


#### Kommandoen `dig


`dig` (*Domain Information Groper*) er et mer moderne, komplett og fleksibelt verktøy enn `nslookup`. Det støtter komplekse forespørsler og gir detaljert informasjon om oppløsningsprosessen, hierarkiet av involverte servere, typen oppføring som returneres (A, AAAA, MX, TXT osv.), og eventuelle feil som har oppstått.


Eksempel på grunnleggende spørring:

```bash
dig mydmn.org
```


Forespørsel til en bestemt DNS-server:

```bash
dig @192.6.23.4 mydmn.org
```


Denne kommandoen kontrollerer tilgjengeligheten av en DNS-oppføring på en gitt server.

En av de viktigste fordelene med `dig` er at den viser detaljene i DNS-svaret, noe som gjør den svært nyttig for å diagnostisere konfigurasjonsfeil.


#### Manuell konfigurasjon av DNS-oppløsere


Noen ganger er det nødvendig å overstyre DNS-serverne som brukes lokalt, for eksempel i testmiljøer eller for å tvinge frem bruk av bestemte servere. Dette kan gjøres ved å redigere filen `/etc/resolv.conf`, som definerer systemets DNS-oppløsningsinnstillinger.


Eksempel på konfigurasjon:


```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```



- Feltet `search` angir et domene som skal legges til automatisk ved oppløsning av korte navn.
- Oppføringene `nameserver` definerer hvilke DNS-servere som skal brukes, i prioritert rekkefølge.


På mange moderne distribusjoner (spesielt de som bruker `systemd-resolved`), er endringer i `/etc/resolv.conf` midlertidige og kan bli overskrevet ved omstart eller ny tilkobling til nettverket. Mer permanente metoder inkluderer bruk av `resolvconf`, `systemd-resolved` eller modifisering av *NetworkManager*-konfigurasjoner.


#### `host`-kommandoen


Et annet enkelt, men effektivt DNS-verktøy er `host`. Det løser domenenavn til IP-adresser (eller omvendt) og kan bidra til å diagnostisere DNS-feil eller feilkonfigurasjoner i et nettverk Interface.


Eksempler:

```bash
host mydmn.org
```


Omvendt oppslag:

```bash
host 192.6.23.4
```


`host` er spesielt nyttig for raske kontroller, spesielt når den brukes i kommandolinjeskript.


Gjentatte eller intensive forespørsler til tredjeparts DNS-servere uten tillatelse kan tolkes som forsøk på innbrudd eller ondsinnet aktivitet. Brukt på feil måte, eller mot nettverk du ikke kontrollerer, kan disse kommandoene ligne på rekognoseringsskanninger, som ofte er første trinn i et angrep. Begrens alltid bruken av dem til miljøer du administrerer, eller der du har eksplisitt autorisasjon.


### Verktøy for nettverksskanning


Når du skal overvåke eller sikre et lokalt nettverk eller et bredbåndsnettverk, er det avgjørende å identifisere aktive enheter og tjenestene de eksponerer. Det er nettopp dette verktøyet `nmap` (*Network Mapper*) gjør.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Vi introduserer `nmap`


`nmap` gjør det mulig å skanne en eller flere verter for å oppdage åpne porter, tilgjengelige tjenester (HTTP, SSH, DNS osv.) og noen ganger til og med hvilket operativsystem som er i bruk. Takket være de mange alternativene gir `nmap` en presis oversikt over nettverkets eksponeringsoverflate, noe som er avgjørende i revisjons- eller herdingsfasene av infrastrukturadministrasjon.


Akkurat som kommandoen `host` må `nmap` aldri brukes på nettverk eller infrastrukturer du ikke eier, eller uten eksplisitt autorisasjon. Uautoriserte portskanninger kan flagges som ondsinnede rekognoseringsforsøk, blir ofte oppdaget av sikkerhetssystemer (brannmurer, IDS/IPS) og kan til og med føre til juridiske konsekvenser.


#### Grunnleggende bruk


Slik skanner du en bestemt vert og viser de åpne portene:

```bash
nmap 192.168.0.1
```


Denne kommandoen skanner de 1000 vanligste portene på verten `192.168.0.1` og viser hvilke tjenester og protokoller som brukes. Hvis DNS-oppløsning er konfigurert, kan du også bruke vertsnavnet i stedet for IP Address.


#### Fullstendig nettverksskanning


En av fordelene med `nmap` er muligheten til å skanne et helt adresseområde med én enkelt kommando. Dette gjør det for eksempel enkelt å raskt få oversikt over alle aktive maskiner i et nettverk:


```bash
nmap 192.168.0.0/24
```


I dette tilfellet vil alle verter i området `192.168.0.0` til `192.168.0.255` bli forespurt. For hver IP Address viser resultatene en liste over åpne porter, status (åpen, filtrert osv.) og, hvis mulig, navnet på den tilsvarende tjenesten.



![Image](assets/fr/055.webp)



En administrator kan bruke `nmap` til flere oppgaver:


- Detektere aktive verter**: Identifiser hvilke maskiner som svarer i et delnett;
- Tjenestelager**: Sørg for at bare de nødvendige portene er tilgjengelige (prinsippet om minste privilegium);
- Samsvarskontroll**: Sammenlign åpne porter med organisasjonens sikkerhetspolicy;
- Sårbarhetsforebygging**: oppdage usikre eller utdaterte tjenester som kjører på kritiske maskiner.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Verktøy for prosessavhør


For å få en grundig analyse av aktive prosesser og åpne filer, spesielt i nettverkssammenheng, bruker Linux-administratorer ofte kommandoen `lsof` (*List Open Files*). Til tross for navnet er `lsof` ikke begrenset til tradisjonelle filer: På UNIX-systemer regnes alt som en fil, inkludert nettverksstikkontakter, enheter og kommunikasjonskanaler.


Verktøyet gir derfor et tverrsnitt av systemet ved å korrelere aktive prosesser, åpne nettverksporter, filer som er åpnet, og hvilke brukere som er involvert.


#### Nettverksanalyse med `lsof`


Alternativet `-i` begrenser utdataene til nettverkstilkoblinger (TCP, UDP, IPv4 eller IPv6). Dette gjør det enkelt å se hvilke prosesser som kommuniserer over nettverket:


```bash
lsof -i
```


Denne kommandoen viser en liste over alle prosesser som kjører ved hjelp av en nettverkskontakt, og viser porten som brukes, protokoll (TCP/UDP), tilkoblingsstatus, samt PID og tilhørende bruker.


#### Filtrering etter IP Address eller port


Du kan avgrense søkene ved å spesifisere en IP Address og en port, og dermed isolere en bestemt nettverksflyt. For eksempel for å sjekke en SMTP-økt (port 25) med en bestemt vert:


```bash
lsof -n -i @192.168.2.1:25
```


Dette viser bare aktive nettverkstilkoblinger med verten `192.168.2.1` på port 25, noe som er nyttig for å diagnostisere mistenkelig aktivitet eller SMTP-flytproblemer.


#### Sporing av enhetstilgang


En annen styrke ved `lsof` er sporing av spesielle filer, for eksempel diskpartisjoner. For eksempel for å sjekke hvilke prosesser som har åpnet filer på `/dev/sda1`:


```bash
lsof /dev/sda1
```


Dette er nyttig når et avmonteringsforsøk mislykkes fordi enheten fortsatt er i bruk, eller når du skal undersøke hvilke programmer som har tilgang til en partisjon.


#### Kryssanalyse: prosess og nettverk


Alternativene kan kombineres for å få presis innsikt. Du kan for eksempel se alle nettverksporter som er åpnet av en prosess med PID 1521:


```bash
lsof -i -a -p 1521
```


Alternativet `-a` krysser kriteriene (`-i` og `-p`), noe som begrenser utdataene til kun nettverkstilkoblinger i den aktuelle prosessen.


#### Sporing av flere brukere


`lsof` kan også brukes til å analysere aktiviteten til bestemte brukere, med en liste over alle filene de har åpnet, eventuelt filtrert etter PID:


```bash
lsof -p 1521 -u 500,phil
```


Dette viser filene eller nettverkstilkoblingene som brukes av brukeren `phil` eller UID 500, begrenset til prosess 1521.


### Sammendrag av seksjonen


I denne siste delen har vi utforsket et bredt spekter av uunnværlige verktøy for å diagnostisere, analysere og administrere datanettverk. Denne studien er strukturert rundt lagene i TCP/IP-modellen, og den tydeliggjør ikke bare hvordan nettverkskommunikasjon fungerer, men etablerer også en streng metodikk for å identifisere, isolere og løse potensielle problemer.


Disse verktøyene gir administratorer et sammenhengende sett med tekniske verktøy for å overvåke nettverkstilstanden, analysere trafikk, kontrollere tilkoblinger og raskt gripe inn ved feil på utstyr eller tjenester.


#### Nettverkstilgang Layer


Verktøy som gir direkte innsyn i grensesnitt og rammer:


- arp / ip neigh**: inspiser og modifiser ARP/NDP-cachen for å kontrollere eller korrigere IP-MAC-tilknytninger;
- tcpdump**: kommandolinjepakkeopptak som kan filtreres og eksporteres;
- Wireshark**: grafisk pakkeanalyse med dyp protokollavkoding;
- ethtool**: spør etter og justerer Ethernet-kortets fysiske parametere (hastighet, dupleks, WoL osv.).


#### Nettverk Layer


Verktøy for vurdering av IP-tilkobling, ruting og pakketrafikk:


- ping**: test rekkevidde og mål ventetid med ICMP;
- ip route**: inspiser og modifiser rutingstabellen for å kontrollere pakkeveiene;
- traceroute**: identifisering av rutere langs ruten til en destinasjon, hopp-for-hop;
- ss**: detaljert oversikt over TCP/UDP-sokler og tilhørende prosesser (etterfølger til netstat).


#### Transport- og applikasjonslag


Verktøy for diagnostisering av tjenester og prosesser:


- nslookup / dig / host**: DNS-spørringer for å validere navneløsning og analysere poster;
- nmap**: Utforsk åpne porter og eksponerte tjenester for å vurdere angrepsflaten;
- lsof**: viser en liste over filer og stikkontakter som er åpnet av prosesser, og korrelerer system- og nettverksaktivitet.


Ved å beherske disse verktøyene, som hver er tilpasset et spesifikt trinn i TCP/IP-modellen, kan man gå metodisk til verks: fra den fysiske Layer, via ruting og opp til applikasjonstjenester. Denne kompetansekjeden gjør administratorer i stand til å diagnostisere, sikre og optimalisere infrastrukturen, noe som sikrer både nettverksytelse og tilgjengelighet.


# Siste del


<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>


## Anmeldelser og rangeringer


<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>

## Avsluttende eksamen


<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>

## Konklusjon


<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>