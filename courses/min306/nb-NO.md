---
name: Bitaxe Open Source Mining Mastery
goal: Behersk hele Bitaxe-økosystemet, fra maskinvaresammenstilling til avansert tilpasning og ytelsesoptimalisering
objectives: 

  - Forstå filosofien bak Bitcoin mining-maskinvare med åpen kildekode
  - Bygg Bitaxe mining-enheter fra bunnen av
  - Konfigurere og optimalisere mining-programvare, inkludert AxeOS og Public Pool
  - Implementere avanserte ytelsesoptimaliseringer, inkludert overklokking og benchmarking

---

# Din Bitaxe Mining-guide


Velkommen til det omfattende Bitaxe-kurset, der du vil lære deg å mestre den revolusjonerende Bitcoin mining-maskinvaren med åpen kildekode som demokratiserer tilgangen til mining-teknologi. Dette kurset tar deg fra å forstå det filosofiske grunnlaget for desentralisert mining til avanserte teknikker for maskinvaretilpasning og ytelsesoptimalisering.


Bitaxe-prosjektet representerer et paradigmeskifte innen Bitcoin mining, og bryter monopolet til proprietære ASIC-produsenter ved å tilby design, fastvare og programvare med helt åpen kildekode. Gjennom disse praktiske kapitlene får du praktiske ferdigheter i maskinvaremontering, programvarekonfigurasjon, PCB-design og ytelsesoptimalisering.


Ingen tidligere mining-erfaring er påkrevd, men grunnleggende elektronikkunnskaper og kjennskap til GitHub vil være nyttig. Kurset vil forvandle deg fra en nysgjerrig observatør til en dyktig Bitaxe-bygger og bidragsyter.


+++


# Innledning


<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>


## Kursoversikt


<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>


Velkommen til kurset MIN 306 _**Bitaxe Open Source Mining Mastery**_, en omfattende reise inn i Bitaxe mining-verdenen. Dette kurset er designet for deg som ønsker å forstå, bygge og optimalisere din egen Bitaxe mining-maskinvare, samtidig som du utforsker det filosofiske og tekniske grunnlaget som gjør dette prosjektet unikt innenfor Bitcoin-økosystemet.


### Forståelse av Bitaxe


Den første delen legger det grunnleggende grunnlaget: Du får vite mer om Bitaxe-prosjektets opprinnelse, dets utvikling og verdiene desentralisering og åpenhet som definerer det. Du får vite hva en Bitaxe egentlig er, hvordan den skiller seg fra proprietære ASIC-er, og hvor du kan finne ressurser i fellesskapet for å tilegne deg mer kunnskap. Denne delen gir deg konteksten du trenger for å forstå hvorfor Bitaxe representerer et vendepunkt i Bitcoin mining-historien.


### Programvare og drift


Den andre delen fokuserer på programvaremiljøet, med en detaljert presentasjon av *AxeOS*: operativsystemet med åpen kildekode som er utviklet spesielt for Bitaxe-enheter. Du lærer hovedfunksjonene og hvordan du konfigurerer og samhandler med enheten din for å starte din første mining-operasjon.


### Fellesskap og samarbeid


Den tredje delen belyser samarbeidsaspektet ved prosjektet. Her får du lære om åpen kildekode-filosofien som ligger til grunn for både maskinvare- og programvareutviklingen av Bitaxe. Gjennom praktiske øvelser lærer du hvordan du kan bidra direkte til kildekoden, og du får også lære om _Public Pool_, en felles plattform for å samle datakraft. Du lærer også hvordan du installerer den på en Umbrel-node for lokal og suveren integrasjon.


### Montering av maskinvare og feilsøking


I den fjerde delen dykker du ned i selve maskinvaren. Du lærer å identifisere verktøyene som trengs for å sette sammen en Bitaxe, fikse loddeproblemer og utføre en komplett diagnostikk ved hjelp av *AxeOS* og USB-verktøy. Denne delen legger vekt på praktisk øvelse og en dyp forståelse av hvordan maskinvare- og programvarekomponenter samhandler.


### Avansert tilpasning


Den femte delen er viet tilpasning. Her lærer du hvordan du modifiserer kretskortet (PCB), lager en fabrikkfil og bruker _Bitaxe Web Flasher_. Denne delen er rettet mot deg som ønsker å gå lenger enn til enkel montering og virkelig designe tilpassede versjoner av din egen enhet.


### Optimalisering av ytelse


Den sjette delen tar for seg avanserte optimaliseringsteknikker. Her lærer du hvordan du kan måle ytelsen til Bitaxe for å evaluere ytelsen, og hvordan du kan overklokke den effektivt. Disse ferdighetene vil hjelpe deg med å få mest mulig ut av maskinvaren din, samtidig som du respekterer dens fysiske begrensninger.


Som med alle kurs på Plan ₿ Academy inneholder den avsluttende delen en evaluering som er utformet for å styrke kunnskapen din.


Dyk rett inn i dette tekniske eventyret - fremtiden til Bitcoin mining ligger i dine hender!


# Forståelse av Bitaxe

<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>


## Historien

<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>

:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

Bitaxe-prosjektet representerer et banebrytende skifte i utviklingen av Bitcoin mining-maskinvare, og bringer åpen kildekode-prinsipper til en bransje som domineres av proprietære løsninger. Denne undervisningsserien utforsker Bitaxes omfattende historie, tekniske innovasjoner og samfunnsdrevne utvikling, og gir innsikt i hvordan en enkelt ingeniørs visjon ble forvandlet til et blomstrende økosystem av desentralisert mining-maskinvare. Gjennom å undersøke prosjektets opprinnelse, utfordringer og prestasjoner får vi en verdifull forståelse av både den tekniske kompleksiteten i ASIC-utviklingen og kraften i åpen kildekode-samarbeid på Bitcoin-området.


### Opprinnelseshistorien: Fra oppdagelsen av Silkeveien til visjonen om Solar Mining


Skot, grunnleggeren av Bitaxe, begynte sin reise inn i Bitcoin på en collegefest der han først fikk vite om Bitcoin gjennom noen som kjøpte varer på Silk Road. Denne første eksponeringen for Bitcoin til omtrent 20 dollar per mynt utløste en nysgjerrighet som senere skulle utvikle seg til et revolusjonerende mining-prosjekt. Det tekniske grunnlaget for det fremtidige arbeidet ble lagt under studietiden, der han hadde tilgang til omfattende FPGA-ressurser i et laboratorium. Sammen med veilederen sin begynte Skot å eksperimentere med FPGA-bitstrømmer med åpen kildekode for Bitcoin mining, i utgangspunktet med det beskjedne målet om å mining nok Bitcoin til å kjøpe en pizza til kontoret.


Overgangen fra akademisk eksperimentering til seriøs utvikling skjedde mange år senere, da Skot jobbet med solcelledrevne gatewayer for fjernstyrt datainnsamling i Afrika. Denne profesjonelle erfaringen med solenergisystemer utløste en erkjennelse av at Bitcoin mining ASICs, som i bunn og grunn er lavspente likestrømsenheter, ville passe perfekt sammen med solcellepaneler. Konseptet virket naturlig og elegant. Da Skot begynte å undersøke eksisterende løsninger, oppdaget han imidlertid et betydelig hull i markedet: I motsetning til de første dagene med Bitcoin mining, da FPGA-design var åpent tilgjengelig, hadde ASIC-ene ført til at bransjen hadde beveget seg i retning av fullstendig proprietære løsninger med lukket kildekode.


Mangelen på mining-maskinvare med åpen kildekode ble en drivende frustrasjon for Skot, spesielt med tanke på hans bakgrunn innen programvareutvikling med åpen kildekode og hans tro på at Bitcoins åpen kildekode-karakter burde utvides til mining-infrastrukturen. Denne filosofiske tilnærmingen til åpen kildekode-prinsipper, kombinert med den tekniske utfordringen med å reversere proprietær ASIC-design, satte scenen for det som skulle bli Bitaxe-prosjektet. Den opprinnelige visjonen var ambisiøs, men likevel praktisk: å skape en soldrevet Bitcoin-gruvedriver som kunne operere uavhengig uten å kreve en separat datamaskin for kontroll, noe som gjorde den egnet for utplassering på avsidesliggende steder under solcellepaneler.


### Tekniske utfordringer og gjennombrudd innen omvendt utvikling


Utviklingen av Bitaxe krevde at man overvant betydelige tekniske hindringer, først og fremst knyttet til den totale mangelen på dokumentasjon av Bitmains ASIC-brikker. Skots tilnærming til denne utfordringen var et godt eksempel på den besluttsomheten og oppfinnsomheten som kreves for å lykkes med reverse engineering. Uten tilgang til offisielle datablad eller tekniske spesifikasjoner måtte han undersøke brikkene under mikroskop, måle pin-plasseringer med skyvelære og til og med skanne brikkene for å finne ut nøyaktig hvor stort fotavtrykk de trengte. Denne møysommelige prosessen resulterte i flere mislykkede prototyper, og de to første iterasjonene av "day miner" fungerte ikke som de skulle på grunn av feilaktige fotavtrykksberegninger.


Gjennombruddet kom med den tredje iterasjonen i mai 2022, da Skot lyktes med å lage en fungerende tobrikkedesign ved hjelp av BM1387-brikker hentet fra Antminer S9-enheter. Denne prestasjonen markerte fødselen til Bitaxe-navnet, inspirert av konseptet med en hakke for Bitcoin mining. Suksessen med denne designen validerte reverse engineering-metoden og viste at uavhengige utviklere kunne lage funksjonell mining-maskinvare uten støtte fra produsenten. De tekniske utfordringene strakte seg imidlertid lenger enn til grensesnittet mellom brikkene, og omfattet også kompleks design av strømforsyningen, ettersom ASIC-ene krevde presis spenningsregulering ved høye strømmer, og ofte opererte ved så lave spenninger som 0,6 volt samtidig som de trakk betydelig strømstyrke.


Utviklingen av fastvaren utgjorde et annet lag av kompleksitet, ettersom prosjektet krevde at det ble utviklet mining-programvare som kunne kjøres direkte på en ESP32-mikrokontroller i stedet for å være avhengig av eksterne datamaskiner som kjørte programvare som CGMiner. Denne selvstendige tilnærmingen var avgjørende for Skots visjon om utplasserbare, uavhengige mining-enheter. Kombinasjonen av reverse engineering av maskinvare og utvikling av innebygd fastvare skapte en omfattende teknisk utfordring som krevde ekspertise på tvers av flere fagområder, fra elektroteknikk og PCB-design til innebygd programmering og nettverksprotokoller.


### Samfunnsdannelse og samarbeid om åpen kildekode


Transformasjonen av Bitaxe fra et soloprosjekt til et blomstrende samfunnsinitiativ representerer et av de viktigste aspektene ved suksessen. Til å begynne med ble Skots forsøk på å vekke generate-interesse gjennom Bitcoin-fora og sosiale medier møtt med begrenset respons og tidvis skepsis. Gjennombruddet kom da medlemmer av fellesskapet, som SirVapesAlot, innså potensialet i mining med åpen kildekode og etablerte Discord-serveren Open Source Miners United (OSMU). Denne plattformen skapte det samarbeidsmiljøet som var nødvendig for at prosjektet skulle blomstre, og tiltrakk bidragsytere med ulik bakgrunn som delte en felles interesse i å demokratisere Bitcoin mining-teknologien.


Den fellesskapsdrevne utviklingsmodellen viste seg å være bemerkelsesverdig effektiv, med viktige bidragsytere som johnny9 og Ben som tok tak i spesifikke tekniske utfordringer. Johnny9s ekspertise innen fastvareutvikling løste kritiske problemer med programvareimplementering, mens Bens ferdigheter innen frontend-utvikling skapte det intuitive AxeOS-dashbordet som forenklet konfigurasjon og overvåking av enheten. Ben bidro også med å etablere produksjonskapasitet og opprette Public Pool, en mining-pool med åpen kildekode som er optimalisert for Bitaxe-enheter. Denne samarbeidstilnærmingen demonstrerte hvordan åpen kildekode-prinsipper kan akselerere utviklingen utover det en enkelt bidragsyter kan oppnå alene.


OSMU-fellesskapet skapte også et inkluderende miljø der nykommere kunne lære og bidra uavhengig av deres opprinnelige tekniske ekspertise. Bens egen reise fra nybegynner til stor produsent er et eksempel på denne innbydende tilnærmingen til utvikling av ferdigheter. Fellesskapets engasjement for utdanning og gjensidig støtte skapte en god sirkel der erfarne medlemmer veiledet nykommere, som deretter selv ble bidragsytere. Denne modellen viste seg å være avgjørende for å skalere prosjektet utover dets opprinnelige omfang og etablere et bærekraftig økosystem for fortsatt innovasjon og vekst.


### Visjon for desentralisert Mining og fremtidig innvirkning


Skots langsiktige visjon for Bitaxe strekker seg langt utover å skape enda en mining-enhet: det er en grunnleggende transformasjon av Bitcoins mining-landskap. Det ambisiøse målet om å produsere én million en-terahash-utvinnere vil skape en exahash av distribuert mining-kraft, noe som representerer et betydelig skritt mot mining-desentralisering. Denne visjonen tar for seg kritiske bekymringer rundt mining-sentralisering, der store bassenger og industrivirksomheter potensielt kan bli utsatt for press fra myndighetene eller reguleringer. Ved å distribuere mining-kraft på tvers av utallige hjemmearbeidere, blir nettverket mer robust og i tråd med Bitcoins desentraliserte prinsipper.


Den økonomiske modellen som støtter denne visjonen, baserer seg på de unike egenskapene til mining i hjemmet, der infrastrukturkostnadene er tilnærmet null og utvinnerne kan drive med minimalt tilsyn. I motsetning til industriell mining-drift som krever massive kapitalinvesteringer i anlegg, kraftinfrastruktur og kjølesystemer, kan utvinnere i hjemmet ganske enkelt koble enheter til eksisterende stikkontakter og internettforbindelser. Denne tilnærmingen kan i teorien gi en betydelig hashrate på nettet uten de tradisjonelle inngangsbarrierene som kjennetegner storskala mining-operasjoner.


Prosjektets suksess har allerede begynt å påvirke det bredere Bitcoin mining-økosystemet, og har potensial til å inspirere andre produsenter til å omfavne utviklingsmodeller med åpen kildekode. Den økonomiske levedyktigheten som Bitaxe-produsentene har demonstrert, viser at maskinvare med åpen kildekode kan være kommersielt vellykket samtidig som åpenhet og samfunnsengasjement opprettholdes. Prosjektet fortsetter å utvikle seg med nye chipintegrasjoner, forbedret design og utvidede produksjonspartnerskap, og fungerer som et bevis på hvordan Bitcoin mining kan vende tilbake til sine desentraliserte røtter og samtidig omfavne moderne ASIC-teknologi. Det endelige målet strekker seg lenger enn bare distribusjon av hashfrekvenser, og omfatter også utdanningseffekt, ved å bringe flere mennesker i direkte kontakt med Bitcoins grunnleggende mining-prosess og fremme en dypere forståelse av nettverkets sikkerhetsmodell.


## Hva er Bitaxe?

<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>

:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Oversikt over maskinvare og funksjoner


Bitaxe-økosystemet omfatter flere maskinvare-iterasjoner, som hver er designet for å optimalisere ulike aspekter av mining-opplevelsen, samtidig som kjernefilosofien om tilgjengelighet med åpen kildekode opprettholdes. Disse enhetene fungerer ikke bare som funksjonell mining-maskinvare, men også som pedagogiske verktøy som gjør det mulig for brukerne å forstå det kompliserte forholdet mellom ASIC-brikker, mikrokontrollere og Bitcoin mining-prosessen. Forståelsen av Bitaxes designfilosofi og tekniske implementering gir verdifull innsikt i hvordan moderne mining-maskinvare fungerer både på komponent- og systemnivå.



### Bitaxe Max, første generasjons implementering


Bitaxe Max representerer den grunnleggende implementeringen av Bitaxe-konseptet, og bruker BM1397 ASIC-brikken som opprinnelig ble utviklet av Bitmain for deres S17 mining-serie. Denne brikkeintegrasjonen demonstrerer hvordan maskinvare med åpen kildekode kan gjenbruke eksisterende ASIC-teknologi for å skape tilgjengelige mining-løsninger. Bitaxe Max leverer en estimert hash-hastighet på mellom 300 og 400 gigahashes per sekund, noe som posisjonerer den som en pedagogisk og eksperimentell mining-plattform snarere enn en løsning i kommersiell skala.


Integreringen av BM1397-brikken i Bitaxe Max krevde nøye vurdering av strømstyring, termisk kontroll og kommunikasjonsprotokoller. Kortets design tar hensyn til de spesifikke kravene til denne ASIC-brikken, samtidig som den inneholder de nødvendige støttekretsene for stabil drift. Denne implementeringen viser hvordan maskinvareutvikling med åpen kildekode kan utnytte eksisterende halvlederteknologi til å skape nye bruksområder og læringsmuligheter i mining-fellesskapet.


### Bitaxe Ultra, avansert chipteknologi


Bitaxe Ultra representerer en videreutvikling av Bitaxe-plattformen, med den mer avanserte BM1366 ASIC-brikken fra Bitmains S19-serie. Denne nyere chipteknologien gir Bitaxe-plattformen forbedret effektivitet og ytelse, samtidig som den samme grunnleggende designfilosofien opprettholdes. Oppgraderingen til BM1366-brikken demonstrerer plattformens tilpasningsevne og fellesskapets forpliktelse til å innlemme teknologiske fremskritt i mining-løsninger med åpen kildekode.


Overgangen fra BM1397- til BM1366-brikken krevde endringer i kortets strømforsyningssystemer, varmestyring og kontrollalgoritmer. Disse endringene illustrerer hvor iterativ maskinvareutvikling er, og hvor viktig det er å opprettholde kompatibilitet samtidig som ytelsen forbedres. Implementeringen av Bitaxe Ultra gir brukerne tilgang til nyere ASIC-teknologi, samtidig som plattformens pedagogiske og eksperimentelle karakter bevares.


### Mikrokontroller og kommunikasjonssystemer


I hjertet av hver Bitaxe-enhet ligger en ESP-mikrokontroller som fungerer som det primære grensesnittet mellom brukeren og ASIC-brikken. Denne mikrokontrolleren kjører spesialisert programvare utviklet av Open Source Miners United (OSMU)-fellesskapet, noe som muliggjør nøyaktig kontroll over ASICs driftsparametere. Kommunikasjonen mellom mikrokontrolleren og ASIC skjer gjennom nøye utformede serielle kommunikasjonslinjer som er etset direkte på kretskortet som synlige spor.


Mikrokontrolleren har mer enn bare kontroll over ASIC. Den har også funksjoner for strømstyring, temperaturovervåking og brukergrensesnitt. Via den integrerte skjermen kan brukerne overvåke kritiske driftsparametere som temperatur, hashfrekvens, IP-adresse og annen relevant mining-statistikk. Dette tilbakemeldingssystemet i sanntid gir verdifull innsikt i enhetens ytelse og hjelper brukerne med å optimalisere driften av mining, samtidig som de lærer mer om den underliggende maskinvareatferden.


### Strømstyring og sikkerhetshensyn


Bitaxe-plattformen opererer med et strengt strømkrav på 5 volt, noe som gjør riktig valg av strømforsyning avgjørende for enhetens levetid og sikkerhet. Strømstyringssystemet på Bitaxe-kortene omfatter sofistikerte kretser som er utformet for å regulere spenningen som leveres til ASIC-brikken, samtidig som strømforbruket overvåkes i ulike driftsmoduser. Denne strømstyringen gjør at enheten kan fungere effektivt på tvers av en rekke interne frekvenser og spenninger, med et typisk forbruk på mellom 5 og 25 watt avhengig av konfigurasjon.


Forståelse av strømkravene blir avgjørende når man tar i betraktning at feil spenningsbruk kan skade enheten permanent. Forholdet mellom frekvens, spenning, strømforbruk og hash-hastighet demonstrerer grunnleggende prinsipper for ASIC-drift som gjelder for all mining-maskinvare. Brukere kan eksperimentere med ulike strøminnstillinger for å forstå effektivitetsavveiningene som ligger i mining-operasjoner, og få praktisk erfaring med konsepter som gjelder for mining-implementeringer i større skala.


### Solo Mining Fokus og nettverksdeltakelse


Bitaxe-plattformen er spesielt rettet mot solo mining-applikasjoner, der individuelle utvinnere forsøker å løse Bitcoin-blokker uavhengig av hverandre i stedet for å delta i store mining-pooler. Selv om hashfrekvensen til Bitaxe-enheter gjør det statistisk sett usannsynlig å finne vellykkede blokker, tjener denne tilnærmingen viktige pedagogiske og filosofiske formål i Bitcoin-fellesskapet. Solo mining med Bitaxe-enheter hjelper brukerne med å forstå den grunnleggende mekanikken i Bitcoins proof-of-work-system, samtidig som det bidrar til desentralisering av nettverket.


Vektleggingen av solo mining gjenspeiler OSMU-fellesskapets forpliktelse til å oppmuntre til individuell deltakelse i Bitcoins sikkerhetsmodell. Ved å tilby tilgjengelig maskinvare som kan fungere uavhengig, gjør Bitaxe-plattformen det mulig for brukere å kjøre sine egne mining-operasjoner uten å være avhengig av felles infrastruktur. Denne tilnærmingen fremmer en dypere forståelse av Bitcoins konsensusmekanisme, samtidig som den støtter nettverkets desentraliserte natur gjennom økt mangfold av gruvearbeidere.


### Maskinvareutvikling og produksjonsforbedringer


Bitaxe-plattformen fortsetter å utvikle seg gjennom tilbakemeldinger fra brukerne og produksjonsoptimalisering, og nyere versjoner inneholder forbedringer som forbedrer produserbarheten og brukeropplevelsen. Versjonsoppdateringer fokuserer vanligvis på produksjonseffektivitet i stedet for grunnleggende ytelsesendringer, noe som sikrer at eksisterende brukere ikke blir utsatt for foreldelsespress. Funksjoner som overgangen fra mikro-USB- til USB-C-kontakter og forbedrede strømtilkoblingssystemer gjenspeiler fellesskapets fokus på praktiske forbedringer av brukervennligheten.


Denne evolusjonære tilnærmingen demonstrerer fordelene ved maskinvareutvikling med åpen kildekode, der innspill fra fellesskapet fører til trinnvise forbedringer som kommer alle brukere til gode. Filosofien "hvis det hasher, så hasher det" understreker plattformens fokus på funksjonalitet fremfor stadige oppgraderinger, og oppfordrer brukerne til å vedlikeholde og bruke enhetene sine i stedet for å jakte på de nyeste versjonene. Denne tilnærmingen støtter bærekraftig maskinvarepraksis, samtidig som den opprettholder den pedagogiske verdien av Bitaxe.


## Hvor kan jeg lære mer?

<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>

:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

Bitaxe-prosjektet representerer et omfattende mining-initiativ med åpen kildekode som strekker seg langt utover en enkelt enhet. Det er avgjørende for alle som ønsker å engasjere seg i dette økosystemet, å vite hvor man finner pålitelig informasjon, tekniske ressurser og støtte fra fellesskapet. Dette kapittelet gir en komplett guide til de viktigste plattformene og ressursene som danner grunnlaget for Bitaxe- og OSMU-fellesskapet (Open Source Miners United).


### Bitaxe.org, det sentrale knutepunktet


Nettstedet Bitaxe.org fungerer som den primære inngangsporten til all prosjektrelatert informasjon og ressurser. Denne sentraliserte plattformen fungerer som ditt første referansepunkt når du trenger å lære mer om Bitaxe-enheter eller utforske andre prosjekter i OSMU-fellesskapet. Nettstedets design prioriterer tilgjengelighet og organisering, og presenterer besøkende med nøye utvalgte lenker som kobler til ulike spesialiserte ressurser i hele økosystemet.


Betydningen av dette sentrale knutepunktet kan ikke overvurderes, ettersom det eliminerer forvirringen som ofte følger med desentraliserte åpen kildekode-prosjekter. I stedet for å lete gjennom flere plattformer eller stole på potensielt utdatert informasjon fra uoffisielle kilder, kan brukerne stole på at Bitaxe.org tilbyr oppdaterte, bekreftede lenker til alle viktige ressurser. Denne tilnærmingen sikrer at både nykommere og erfarne medlemmer av fellesskapet effektivt kan finne den spesifikke informasjonen de trenger for prosjektene sine.


### Tekniske ressurser og utviklingsmateriell


Arkivet for maskinvaredesignfiler på GitHub er en av de mest verdifulle ressursene for alle som er interessert i å forstå eller bygge Bitaxe-enheter. Dette offentlige arkivet inneholder omfattende dokumentasjon som dekker alle aspekter av maskinvaredesignprosessen, fra de første konseptene til de endelige produksjonsspesifikasjonene. Repositoryet inneholder detaljerte bilder, prosjektmål, funksjonsbeskrivelser og innebygde komponentforklaringer som gir både teknisk dybde og praktisk veiledning.


For dem som er interessert i å produsere sine egne enheter, inneholder depotet spesifikke dokumentasjonsfiler, for eksempel building.md, som inneholder trinnvise instruksjoner for hele produksjonsprosessen. Dokumentasjonen omfatter programvareverktøyene som kreves for å designe kretskort, prosedyrene for å sende filer til produsentene og trinnene for mottak og validering av produserte kretskort. Dette detaljnivået sikrer at enkeltpersoner eller små organisasjoner kan navigere i produksjonsprosessen uten omfattende tidligere erfaring med maskinvareproduksjon.


ESP-Miner-depotet fungerer som det sentrale stedet for all fastvarerelatert kode og dokumentasjon. Dette GitHub-depotet inneholder hver eneste kodelinje som er skrevet for Bitaxe-fastvaren, sammen med omfattende dokumentasjon som forklarer systemkrav, maskinvarespesifikasjoner og konfigurasjonsalternativer. Depotstrukturen er utformet for å imøtekomme både brukere som foretrekker forhåndskompilerte binære filer, og utviklere som ønsker å bygge fastvaren fra kildekoden.


Dokumentasjonen i dette repositoriet inneholder detaljerte avsnitt om maskinvarekrav, forhåndskonfigurasjonsalternativer og anbefalte verdier for ulike innstillinger. Denne informasjonen er uvurderlig for brukere som ønsker å tilpasse enhetene sine eller feilsøke spesifikke problemer. I tillegg inneholder depotet informasjon om nyere utviklinger, for eksempel Raspberry Pi-integrering, noe som sikrer at dokumentasjonen er oppdatert i takt med den pågående prosjektutviklingen.


### Verktøy for enhetsadministrasjon og vedlikehold


Bitaxe web flasher representerer en praktisk løsning for vedlikehold og oppdateringer av enheter. Med dette nettbaserte verktøyet kan brukerne flashe fastvaren til enhetene sine uten å måtte bruke spesialprogramvare eller kompliserte kommandolinjeprosedyrer. Blinkprogrammet støtter flere enhetsvarianter, inkludert Bitaxe Ultra med ulike portversjoner og de eldre Bitaxe Max-modellene. Brukerne kan velge mellom å oppdatere eksisterende fastvare via webgrensesnittet eller å utføre komplette tilbakestillinger ved hjelp av USB-tilkoblinger.


Dette verktøyet tar for seg en av de vanligste utfordringene maskinvareentusiaster står overfor: vedlikehold og oppdatering av enhetens fastvare. Ved å tilby et brukervennlig webgrensesnitt eliminerer flasher mange av de tekniske hindringene som ellers kan hindre brukerne i å holde enhetene sine oppdatert med de nyeste fastvareversjonene. Verktøyet er designet med fokus på enkelhet, samtidig som det gir den fleksibiliteten som trengs for ulike enhetskonfigurasjoner og oppdateringsscenarioer.


### Fellesskapsplattformer og kommunikasjonskanaler


Discord-serveren representerer hjertet av sanntidsinteraksjon og -støtte i Bitaxes økosystem. Serverens organisering gjenspeiler de ulike interessene og behovene til medlemmene i fellesskapet, med nøye strukturerte kanaler som legger til rette for fokuserte diskusjoner om spesifikke emner. Nye medlemmer gjennomgår en verifiseringsprosess som krever at de leser og godtar fellesskapets regler, noe som sikrer at alle deltakerne forstår forventningene til respektfull og produktiv samhandling.


Serverens kanalstruktur inkluderer generelle diskusjonsområder som dekker emner som integrering av solenergi, mining-bassenger og Bitcoin-relaterte diskusjoner. Mer spesialiserte seksjoner fokuserer på spesifikke enheter, inkludert dedikerte kanaler for Bitaxe Ultra-, Hex- og Supra-variantene. Fastvarekanalen er et fokusert område for tekniske diskusjoner om programvareutvikling og feilsøking, mens kanalen for offisielle utgivelser sørger for at medlemmene mottar varsler om nye utviklinger i tide.


Den har også et abonnentområde som gir ekstra fordeler for medlemmer som velger å støtte prosjektet økonomisk. Denne differensierte tilnærmingen gjør det mulig å tilby utvidede tjenester samtidig som man opprettholder åpen tilgang til viktig informasjon og støttekanaler. Hjelpekanalen fungerer som et dedikert område for feilsøking og teknisk assistanse, slik at brukerne kan få rask hjelp når de støter på problemer.



Open Source Miners United-wikien (osmu.wiki) inneholder omfattende dokumentasjon som utfyller sanntidsdiskusjonene som foregår på Discord. I motsetning til chat-baserte plattformer tilbyr wikien strukturert, søkbar dokumentasjon som dekker alle aspekter av Bitaxe-prosjektet og relaterte initiativer. Organiseringen gjenspeiler prosjektets struktur, med egne seksjoner for ulike enhetsserier og omfattende installasjonsveiledninger.


Wikien er åpen kildekode, noe som gjør det mulig for medlemmene å bidra direkte til dokumentasjonen. Brukerne kan redigere sider, sende inn rettelser og legge til ny informasjon via GitHub-integrering, noe som sikrer at kunnskapsbasen forblir oppdatert og åpen. Denne samarbeidstilnærmingen utnytter den kollektive ekspertisen i fellesskapet, samtidig som kvalitetskontrollen opprettholdes gjennom en gjennomgangsprosess for innsendte endringer.


Wikien inneholder praktiske ressurser, for eksempel installasjonsveiledninger i PDF-format som gir trinnvise instruksjoner for konfigurasjon og bruk av enheten. Disse veiledningene fungerer som verdifulle referanser for både nye brukere og erfarne medlemmer som trenger rask tilgang til spesifikke prosedyrer eller konfigurasjonsdetaljer.


### Innkjøps- og leverandørinformasjon


Bitaxes legitime liste dekker et kritisk behov i maskinvaresamfunnet med åpen kildekode: å identifisere pålitelige leverandører og unngå falske selgere. Denne kuraterte listen inneholder verifiserte forhandlere og produsenter som oppfyller spesifikke kriterier for legitimitet og støtte fra fellesskapet. Hver liste inneholder direkte lenker til leverandørens nettsted, regional informasjon og selskapsbeskrivelser som hjelper brukerne med å ta informerte kjøpsbeslutninger.


Det er viktig at listen viser om hver leverandør bidrar tilbake til OSMU-fellesskapet, enten økonomisk eller gjennom andre former for støtte. Denne åpenheten hjelper medlemmene i fellesskapet med å forstå hvilke leverandører som aktivt støtter prosjektets utvikling og bærekraft. Listen fungerer også som et beskyttende tiltak mot vanlige svindelforsøk, for eksempel uautoriserte forhåndsbestillinger av uutgitte produkter, noe som historisk sett har skapt problemer i fellesskapet.


Vektleggingen av ikke-tilknyttede lenker viser fellesskapets forpliktelse til å gi objektive leverandøranbefalinger. Brukerne kan stole på at anbefalingene er basert på leverandørens legitimitet og bidrag til fellesskapet, og ikke på økonomiske insentiver, noe som sikrer at innkjøpsbeslutningene støtter både individuelle behov og fellesskapets bærekraft.



# Programvare og drift

<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>


## Hva er AxeOS?

<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>

:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

AxeOS er et fastvare- og webgrensesnitt for Bitaxe mining-enheter, som gir brukerne full kontroll og overvåkningsmuligheter gjennom et intuitivt nettleserbasert dashbord. Dette systemet forvandler den komplekse oppgaven med ASIC-administrasjon til en tilgjengelig opplevelse, slik at gruvearbeidere kan overvåke ytelse, justere innstillinger og administrere flere enheter fra ett enkelt grensesnitt. Det er viktig å forstå AxeOS for å maksimere Bitaxe-enhetens potensial og opprettholde optimal mining-drift.


### Oversikt over dashbord og kjernemålinger


AxeOS-dashbordet fungerer som ditt primære vindu inn til Bitaxe-enhetens ytelse, og presenterer kritiske mining-målinger i et organisert sanntidsformat. Når du navigerer til IP-adressen til Bitaxe-enheten din, får du umiddelbart opp fire viktige ytelsesindikatorer som definerer mining-driftens nåværende tilstand. Hash-hastigheten viser den faktiske beregningshastigheten ASIC-brikken produserer når den behandler den gjeldende blokkmalen, noe som gir umiddelbar tilbakemelding om enhetens kjernefunksjonalitet.


I tillegg til hashfrekvensen sporer aksjetelleren hver gyldige løsning Bitaxe-enheten din sender inn til mining-poolen, og den øker for hver vellykkede innsending og fungerer som et direkte mål på enhetens bidrag til poolens mining-innsats. Effektivitetsberegningen gir deg viktig innsikt i enhetens strømforbruk ved å beregne forholdet mellom hashfrekvensen og strømforbruket, noe som hjelper deg med å optimalisere lønnsomheten i driften. Indikatoren for høyeste vanskelighetsgrad registrerer den høyeste vanskelighetsgraden enheten din noensinne har funnet, og opprettholder denne prestasjonen selv gjennom omstarter og oppdateringer, og tilbakestilles bare når du utfører en fullstendig fabrikkblink.


Dashbordets utvidbare menysystem, som styres med en vippeknapp, gir tilgang til all AxeOS-funksjonalitet samtidig som grensesnittet er oversiktlig. Grafen over hashfrekvensen i sanntid er en av de mest verdifulle funksjonene, og viser ytelsesdata i sanntid som blir mer nøyaktige og informative jo lenger du holder økten din. Strøm-, varme- og ytelsesdelene gir omfattende overvåking av enhetens driftsstatus, inkludert advarsler om inngangsspenning som varsler deg om potensielle problemer med strømforsyningen, samtidig som du sikrer fortsatt drift innenfor trygge parametere.


### Avansert overvåking og systeminformasjon


Overvåkingsfunksjonene i AxeOS strekker seg langt utover grunnleggende hashfrekvenssporing, og gir detaljert innsikt i alle aspekter ved driften av Bitaxe-enheten. Strømseksjonen viser beregnet strømforbruk utledet fra innebygde integrerte kretser, inngangsspenningsmålinger fra strømtilkoblingen og forespurte ASIC-spenningsnivåer. Når spenningsfall oppstår, viser AxeOS umiddelbart advarsler, selv om disse vanligvis ikke påvirker driften av mining, men bare indikerer potensielle muligheter for optimalisering av strømforsyningen.


Temperaturovervåking fokuserer på termisk styring av ASIC-brikken, med målinger fra strategiske steder på enheten for å gi nøyaktige termiske data med passende forskyvninger for nøyaktighet på brikkenivå. Frekvens- og spenningsdisplayene gir tilbakemelding i sanntid om innstillingsparametrene for ASIC, og den målte spenningen representerer den mest nøyaktige avlesningen som er tilgjengelig, tatt direkte på ASIC-brikken. Denne presisjonen muliggjør finjustering av ytelsesparametere samtidig som sikre driftsforhold opprettholdes.


Tilkoblingsstatusdelen gir umiddelbar oversikt over konfigurasjonen av mining-bassenget ditt, og viser gjeldende stratum-URL, port og brukeridentifikasjon. For enheter som er koblet til offentlige bassenger, genererer AxeOS praktiske hurtigkoblinger som tar deg direkte til nettgrensesnittet for bassenget, der du kan få tilgang til detaljert statistikk, enhetsoversikter og historiske ytelsesdata. Denne integrasjonen effektiviserer overvåkingsprosessen ved å koble sammen informasjon på enhetsnivå og bassengnivå i en sømløs arbeidsflyt.


### Svermstyring og kontroll av flere enheter


Swarm-funksjonaliteten representerer AxeOS' løsning på kompleksiteten ved å administrere flere Bitaxe-enheter på tvers av et nettverk, og eliminerer behovet for å huske og navigere til mange IP-adresser. Dette sentraliserte administrasjonssystemet lar deg legge til enheter ved å skrive inn IP-adressene deres, og detekterer automatisk aktive Bitaxe-minere og integrerer dem i et samlet kontrollpanel. Når Swarm er konfigurert, gir det omfattende kontroll over hele mining-operasjonen fra ett enkelt grensesnitt.


Via Swarm-grensesnittet kan du utføre viktige administrasjonsoppgaver på tvers av flere enheter samtidig eller enkeltvis, inkludert endringer i gruppekonfigurasjon, omstart av enheter, frekvensjusteringer og ytelsesovervåking. Denne sentraliserte tilnærmingen reduserer de administrative kostnadene ved å administrere store mining-operasjoner betydelig, samtidig som den sikrer konsekvent konfigurasjon på tvers av alle enhetene. Systemet opprettholder den individuelle enhetsidentiteten samtidig som det tilbyr kollektive administrasjonsfunksjoner, noe som gir en optimal balanse mellom detaljert kontroll og driftseffektivitet.


Swarm-instrumentbordet viser hver administrert enhet med gjeldende status, ytelsesmålinger og hurtigtilgangskontroller, noe som gjør det mulig å reagere raskt på ytelsesproblemer eller konfigurasjonsendringer. Denne funksjonaliteten er spesielt verdifull for utvinnere som driver flere enheter på forskjellige steder, eller som ofte justerer mining-parametere basert på markedsforhold eller bassengytelse.


### Konfigurasjonsstyring og systeminnstillinger


Innstillingsdelen i AxeOS gir omfattende kontroll over alle konfigurerbare aspekter ved Bitaxe-enheten din, fra nettverkstilkobling til mining-parametere og maskinvareoptimalisering. Nettverkskonfigurasjonen begynner med Wi-Fi-oppsett, der du angir nettverksnavn og passord, og AxeOS anbefaler nettverksnavn med ett ord uten mellomrom for å sikre pålitelig tilkobling. Systemet håndterer hele den trådløse konfigurasjonsprosessen, og gir mulighet for fjernadministrasjon og overvåking.


Mining-konfigurasjonen er sentrert rundt stratum-innstillinger, der du angir URL-adressen til det valgte mining-bassenget uten protokollprefikser eller portnumre, som håndteres i separate felt. Stratum-brukerfeltet imøtekommer ulike krav til bassenger, og støtter både Bitcoin-adresser for solo mining og brukernavnsystemer for mining-basseng, med mulighet for å legge til enhetsidentifikatorer for operasjoner med flere enheter. Den nylig tilføyde stratum-passordfunksjonaliteten støtter bassenger som krever autentisering, selv om de fleste offentlige bassenger opererer uten dette kravet.


Maskinvareoptimalisering gjennom justering av frekvens og kjernespenning er AxeOS' kraftigste ytelsesinnstillingsmulighet. Avhengig av enhetsversjon og nettleser kan disse innstillingene vises som nedtrekksmenyer med forhåndsinnstilte konfigurasjoner eller som åpne felter med mulighet for tilpassede verdier. Standardinnstillingene på 485 MHz frekvens og 1200 mV kjernespenning gir stabil drift ved første gangs testing, mens avanserte brukere kan optimalisere disse parameterne for maksimal ytelse eller effektivitet basert på deres spesifikke krav og driftsforhold.


### Systemvedlikehold og avanserte funksjoner


AxeOS inneholder sofistikerte systemvedlikeholdsfunksjoner som er utformet for å holde Bitaxe-enheten din i toppform, samtidig som det gir diagnostisk informasjon for feilsøking og optimalisering. Oppdateringssystemet effektiviserer fastvareadministrasjonen ved å vise den nyeste tilgjengelige versjonen direkte i grensesnittet og tilby direkte nedlastingslenker til offisielle fastvarefiler. Denne integrasjonen eliminerer behovet for å navigere manuelt i GitHub-arkiver eller administrere filnedlastinger, og forenkler oppdateringsprosessen til noen få klikk.


Oppdateringsgrensesnittet godtar fastvarefiler med riktig navn, spesielt esp-miner.bin og www.bin, noe som sikrer kompatibilitet og forhindrer installasjonsfeil. For brukere som har problemer med standardoppdateringsprosessen, gir AxeOS referanser til omfattende fabrikkflashprosedyrer som kan gjenopprette enhetene til opprinnelig funksjonalitet. Denne doble tilnærmingen tar hensyn til både rutinemessige oppdateringer og gjenopprettingsscenarioer.


Loggsystemet gir sanntidsinnsikt i enhetens drift, og viser detaljert informasjon om ASIC-brikkemodeller, systemets oppetid, Wi-Fi-tilkoblingsstatus, tilgjengelig minne, fastvareversjoner og kortrevisjoner. Disse loggene er uvurderlige for utviklere og avanserte brukere som ønsker å forstå hvordan enheten oppfører seg, diagnostisere problemer eller optimalisere ytelsen. Loggvisningen i sanntid viser driftsdata i sanntid, inkludert nonce-behandling, vanskelighetsberegninger og mining-innleveringsparametere, noe som gir enestående innsyn i selve mining-prosessen.


Ytterligere systemfunksjoner inkluderer kontroll av skjermretning for enheter som brukes i tilpassede kabinetter, invertering av viftepolaritet for spesialiserte kjølekonfigurasjoner og automatisk viftekontroll som justerer kjølingen basert på ASIC-temperaturen. Manuell viftehastighetskontroll gir presis kjølehåndtering når automatiske systemer ikke oppfyller spesifikke krav. Alle konfigurasjonsendringer krever lagring og omstart av enheten for å tre i kraft, noe som sikrer stabil drift og forhindrer delvise konfigurasjonstilstander som kan påvirke mining-ytelsen.



# Fellesskap og samarbeid

<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>


## Oversikt over bidrag til åpen kildekode

<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>

:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### GitHub og dens rolle i programvareutvikling


GitHub representerer et fundamentalt skifte i hvordan programvareutviklingsprosjekter administreres og deles på tvers av det globale programmeringsmiljøet. GitHub er en skybasert plattform som er vert for programvareutviklingsprosjekter ved hjelp av Git, et distribuert versjonskontrollsystem, og gjør det mulig for utviklere å samarbeide sømløst om prosjekter uavhengig av hvor de befinner seg. Plattformen fungerer både som et teknisk verktøy og et sosialt nettverk for programmerere, slik at de kan spore endringer, slå sammen oppdateringer, vedlikeholde ulike versjoner av koden sin og bidra til åpen kildekode-initiativer som BitX-prosjektet fra Open Source Miners United.


Styrken til GitHub ligger i dens evne til å forenkle den komplekse prosessen med utviklingssamarbeid. Når flere utviklere jobber på samme prosjekt, tilbyr GitHub en infrastruktur som gjør det mulig å administrere bidrag, gjennomgå endringer, håndtere prosjektproblemer og vedlikeholde omfattende dokumentasjon. Denne samarbeidstilnærmingen har gjort GitHub til en viktig komponent i moderne arbeidsflyter for programvareutvikling, og har endret hvordan både individuelle utviklere og store organisasjoner tilnærmer seg prosjektledelse og kodedeling.


### Navigere i GitHub Interface og arkivstrukturen


For å forstå GitHub-grensesnittet må du først kjenne igjen de viktigste elementene som utgjør en depotside. Den øverste navigasjonslinjen inneholder flere viktige seksjoner, inkludert Code, Issues, Pull Requests, Discussions, Actions, Projects, Security og Insights. Hver seksjon har et spesifikt formål i prosjektstyringsøkosystemet, der Code-delen viser de faktiske filene og mappene som prosjektet består av.


Selve arkivstrukturen gjenspeiler den organisatoriske tilnærmingen til prosjektvedlikeholderne. Noen repositorier inneholder bare én enkelt fil, kanskje et enkelt skallskript, mens andre, som BitX-maskinvareprosjektet, inneholder mange filer organisert i kataloger og underkataloger. Navnet på depotet vises tydelig og fungerer både som en identifikator og en kort beskrivelse av prosjektets formål. Viktige interaktive elementer inkluderer Watch-knappen for å motta varsler om oppdateringer av depotet, Fork-knappen for å opprette personlige kopier av depotet og Star-knappen, som fungerer som et system for støtte fra fellesskapet, på samme måte som en "tommelen opp"-funksjon.


Om-delen inneholder viktig prosjektinformasjon i et kortfattet format, inkludert en beskrivelse på én linje, lisensinformasjon og viktige prosjektdetaljer. For BitX-prosjektet identifiserer denne delen det som "open source ASIC Bitcoin miner hardware" og spesifiserer GPL 3.0-lisensen. Det er spesielt viktig å forstå lisensene fordi GitHub fungerer som en åpen kildekode-plattform der offentlige repositorier er tilgjengelige for hele samfunnet, men innholdet kan bare brukes og distribueres i henhold til hver lisens' regler for samsvar.


### Arbeide med grener og prosjektversjoner


Konseptet med grener er en av GitHubs kraftigste funksjoner for å håndtere ulike versjoner og utviklingsspor i ett og samme prosjekt. En gren oppretter i hovedsak en kopi eller modifisert versjon av hovedkodebasen, slik at utviklere kan jobbe med spesifikke funksjoner, feilrettinger eller eksperimentelle endringer uten å påvirke den primære utviklingslinjen. Master-grenen fungerer vanligvis som standard og den mest stabile versjonen av prosjektet, mens andre grener kan brukes til ulike iterasjoner, testfaser eller helt andre produktvarianter.


I BitX-maskinvareprosjektet finnes det flere grener for å håndtere ulike maskinvareversjoner og -konfigurasjoner. Ultra v2-grenen inneholder for eksempel filer som er spesifikke for den maskinvare-iterasjonen, mens Super 401-grenen fokuserer på implementasjoner som bruker S21 ASIC-brikken for forbedret effektivitet. Hver gren kan ligge flere commits foran eller bak hovedgrenen, noe som indikerer omfanget av endringer og utviklingsaktivitet. Når du undersøker de ulike grenene, vil du legge merke til helt forskjellige filstrukturer, dokumentasjon og til og med visuelle representasjoner, noe som gjenspeiler de unike kravene og spesifikasjonene for hver maskinvarevariant.


Gren-systemet forhindrer forvirring blant bidragsytere og brukere ved å skille tydelig mellom ulike utviklingsspor. I stedet for å blande eksperimentelle funksjoner med stabile utgivelser, eller kombinere ulike maskinvareversjoner på ett og samme sted, sørger grener for et tydelig skille, samtidig som vellykkede endringer kan flettes tilbake til hovedutviklingslinjen når det er hensiktsmessig. Denne organisatoriske tilnærmingen sikrer at brukerne enkelt kan finne den spesifikke versjonen de trenger, mens utviklerne kan jobbe med forbedringer uten å forstyrre hovedprosjektet.


### Bidra gjennom problemer


Problemseksjonen fungerer som den primære kommunikasjonskanalen mellom brukere og prosjektvedlikeholdere for rapportering av problemer, forslag til forbedringer og dokumentasjon av feil. Det er imidlertid viktig å forstå at Issues-delen er spesielt utformet for legitime tekniske problemer, og ikke for generelle spørsmål eller supportforespørsler. Når brukere støter på faktiske funksjonsfeil, uventet oppførsel eller identifiserer potensielle forbedringer, kan det å opprette et veldokumentert problem hjelpe hele fellesskapet ved å rette oppmerksomheten mot problemer som kan påvirke flere brukere.


Effektiv problemrapportering krever detaljert dokumentasjon av problemet, inkludert omstendighetene som førte til problemet, fremgangsmåten for å reprodusere problemet og alle relevante tekniske detaljer. BitX-prosjektet demonstrerer dette prinsippet gjennom ulike lukkede problemer som viser løsningsprosessen, fra den første problemidentifiseringen via diskusjon i fellesskapet til den endelige løsningen. Noen problemer resulterer i maskinvareforbedringer, for eksempel at det legges til monteringshull for å øke kjølemulighetene, mens andre kan løses gjennom brukeropplæring eller programvareoppdateringer.


Skillet mellom Issues og Discussions er viktig for å opprettholde en organisert interaksjon i fellesskapet. Mens Issues fokuserer på spesifikke tekniske problemer, tilbyr Discussions-delen et forumlignende miljø for spørsmål, ideer og generelt samfunnsengasjement. Selv om Discord-serveren har blitt den primære kommunikasjonskanalen for BitX-fellesskapet, er GitHub Discussions-delen fortsatt tilgjengelig for mer formelle eller søkbare samtaler som har nytte av permanent dokumentasjon og enkel referanse.


### Forstå pull-forespørsler


Pull-forespørsler er en mekanisme der eksterne bidragsytere foreslår endringer i et prosjektarkiv. Når noen identifiserer en forbedring, feilretting eller ny funksjon som kan komme prosjektet til gode, kan de opprette en pull-forespørsel for å sende inn endringene sine for gjennomgang og potensiell integrering i hovedkodebasen. Denne prosessen sikrer at alle endringer blir gjennomgått før de blir en del av det offisielle prosjektet, noe som opprettholder kodekvaliteten og prosjektets koherens, samtidig som det muliggjør bidrag fra fellesskapet.


Arbeidsflyten for pull-forespørsler begynner vanligvis med at en bidragsyter forker depotet, oppretter sin egen kopi der han eller hun kan gjøre endringer, og deretter sender disse endringene tilbake til det opprinnelige prosjektet gjennom en pull-forespørsel. Prosjektvedlikeholderne kan deretter gå gjennom de foreslåtte endringene, diskutere endringene med bidragsyteren og til slutt bestemme om endringene skal slås sammen med hovedprosjektet. Denne samarbeidsprosessen bidrar til å opprettholde prosjektstandardene, samtidig som den oppmuntrer til deltakelse og forbedring i fellesskapet.


Forståelse av tagger og utgivelser tilfører et nytt lag til prosjektstyring og versjonskontroll. Tagger fungerer som markører på utviklingstidslinjen, og identifiserer spesifikke punkter som representerer bestemte versjoner eller milepæler. I maskinvareprosjekter som BitX tilsvarer tagger ofte spesifikke modellnumre eller maskinvarerevisjoner, noe som gir tydelige referansepunkter for brukere som søker bestemte versjoner. Utgivelser, som er mer vanlig i programvareprosjekter, representerer formelle distribusjoner av ferdige funksjoner og feilrettinger, ofte ledsaget av detaljerte utgivelsesnotater og nedlastbare pakker.


GitHub-økosystemet skaper et omfattende miljø for samarbeid med åpen kildekode som strekker seg langt utover enkel fildeling. Ved å forstå disse ulike komponentene og hvordan de brukes på riktig måte, kan bidragsytere delta effektivt i prosjekter, bidra til å forbedre programvare- og maskinvaredesign og dra nytte av den kollektive kunnskapen og innsatsen til det globale utviklingsmiljøet. Enten det gjelder å rapportere problemer, foreslå forbedringer eller bidra med kode, gir GitHub verktøyene og strukturen som er nødvendig for meningsfylt samarbeid i åpen kildekode-verdenen.


## Praktisk bidrag til åpen kildekode

<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>

:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

Dette kapittelet bygger på grunnlaget for å opprette problemer og utforske åpen kildekode-prosjekter, og fokuserer på de praktiske aspektene ved å bidra direkte gjennom pull requests og repository management. Å forstå hvordan man bruker fork-repositorier, gjør endringer og sender inn pull-forespørsler, er en avgjørende ferdighet for alle utviklere som ønsker å bidra på en meningsfull måte til åpen kildekode-prosjekter, enten det dreier seg om programvareutvikling eller maskinvaredesign.


Prosessen med å bidra med kodeendringer følger en standardisert arbeidsflyt som sikrer prosjektintegritet samtidig som den åpner for utviklingssamarbeid. Denne arbeidsflyten innebærer at du oppretter din egen kopi av et prosjektrepositorium, gjør endringer i et kontrollert miljø og deretter foreslår disse endringene tilbake til det opprinnelige prosjektet gjennom en formell gjennomgangsprosess. Selv om eksemplene i dette kapittelet først og fremst fokuserer på programvarebidrag, gjelder de samme prinsippene og prosedyrene også for maskinvareprosjekter som involverer PCB-design, skjemaer og annen teknisk dokumentasjon.


### Forståelse av gafler og repository-struktur


Grunnlaget for å bidra til et hvilket som helst åpen kildekode-prosjekt begynner med å opprette en fork, som fungerer som din personlige kopi av det opprinnelige depotet. Når du navigerer til et GitHub-repository og klikker på "fork"-knappen, oppretter du en uavhengig kopi under din egen GitHub-konto som opprettholder en tydelig forbindelse til originalkilden. Dette forkede depotet vises i kontoen din med en tydelig indikasjon på opprinnelsen, og viser tekst som "forked from [original-owner]/[repository-name]" under tittelen på depotet.


Det forkede depotet ditt fungerer uavhengig av det opprinnelige, slik at du kan gjøre endringer uten å påvirke hovedprosjektet. Det opprettholder imidlertid bevissthet om oppdateringer til det opprinnelige depotet gjennom GitHubs synkroniseringsfunksjoner. Når det opprinnelige depotet mottar oppdateringer som fork mangler, viser GitHub statusinformasjon som "Denne grenen ligger X commits bak" eller "X commits foran", noe som gir tydelig innsyn i forholdet mellom fork og oppstrømsdepotet. Du kan når som helst synkronisere fork med det opprinnelige depotet ved å klikke på "Synkroniser fork"-knappen, som henter inn de nyeste endringene fra oppstrømskilden.


Forholdet mellom fork og det opprinnelige repositoriet blir spesielt viktig når du begynner å gjøre endringer. Etter hvert som du implementerer endringer og overfører dem til fork, sporer GitHub disse forskjellene og viser dem som overføringer foran det opprinnelige depotet. Dette sporingssystemet muliggjør pull request-prosessen, der du kan foreslå endringene dine for inkludering i hovedprosjektet, samtidig som du opprettholder en tydelig historikk over hva som har blitt endret.


### Sette opp utviklingsmiljøet ditt


For å skape et effektivt utviklingsmiljø må man ta hensyn til både generelle utviklingsverktøy og prosjektspesifikke krav. Visual Studio Code er et utmerket integrert utviklingsmiljø (IDE) for de fleste bidrag med åpen kildekode, og tilbyr viktige funksjoner for kodedigering, integrasjon med versjonskontroll og prosjektstyring. Den første kritiske komponenten innebærer å installere og konfigurere Git-utvidelsen, som muliggjør sømløs integrasjon med GitHub-repositorier direkte fra utviklingsmiljøet.


Moderne versjoner av Visual Studio Code inkluderer vanligvis Git-støtte som standard, men du må autentisere deg med GitHub-kontoen din for å aktivere full funksjonalitet. Denne autentiseringsprosessen innebærer at du logger deg på GitHub via IDE-en, som deretter lar deg klone repositorier, overføre endringer og pushe oppdateringer direkte fra utviklingsmiljøet ditt. GitHub-integrasjonen vises som et ikon i venstre sidefelt, og gir tilgang til kloning av repositorier, grenadministrasjon og synkroniseringsfunksjoner uten å kreve kommandolinjeoperasjoner.


For prosjekter som involverer innebygde systemer eller spesifikke maskinvareplattformer, er det nødvendig med ekstra verktøy. ESP-IDF-utvidelsen er en viktig komponent for prosjekter som er rettet mot ESP32-mikrokontrollere, og krever spesifikk versjonskompatibilitet for å sikre riktig funksjonalitet. Installasjonsprosessen innebærer å velge riktig ESP-IDF-versjon, konfigurere verktøystier og sette opp utviklingscontainermiljøet. Versjon 5.1.3 er for øyeblikket den anbefalte konfigurasjonen for mange ESP32-baserte prosjekter, men disse kravene kan endre seg etter hvert som prosjektene oppdaterer sine avhengigheter og verktøykjeder.


### Gjør endringer og håndter forpliktelser


Når utviklingsmiljøet ditt er riktig konfigurert, begynner prosessen med å gi meningsfulle bidrag med å laste ned eller klone det forkede repositoriet til din lokale maskin. Du kan gjøre dette enten ved å laste ned en ZIP-fil med innholdet i depotet eller ved å bruke Visual Studio Codes integrerte kloningsfunksjonalitet, som gir en mer strømlinjeformet arbeidsflyt for løpende utvikling. Kloningsprosessen oppretter en lokal kopi av depotet ditt som forblir synkronisert med GitHub fork, slik at du kan jobbe offline samtidig som du opprettholder versjonskontrollfunksjonene.


Når du arbeider med det lokale repositoriet, får du tilgang til hele prosjektstrukturen, inkludert kildekodefiler, konfigurasjonsfiler, dokumentasjon og eventuelle maskinvaredesignfiler. De fleste fastvareprosjekter bruker programmeringsspråk som C for kjernefunksjonalitet, med tilleggskomponenter skrevet i TypeScript for brukergrensesnitt eller Java for spesifikke verktøy. Ved å forstå prosjektstrukturen kan du finne ut hvilke filer du skal endre, og sikre at endringene dine er i tråd med prosjektets arkitekturmønstre og kodingsstandarder.


Commit-prosessen er et grunnleggende aspekt ved versjonskontroll som krever at man er nøye med både teknisk nøyaktighet og tydelig kommunikasjon. Før du gjør endringer, bør du sette deg grundig inn i den eksisterende koden og teste eventuelle endringer i ditt lokale miljø. Hovedregelen for bidrag med åpen kildekode er at man aldri skal publisere kode som ikke er testet, da dette kan introdusere feil eller sikkerhetshull som påvirker hele prosjektfellesskapet. I tillegg må du aldri legge ut sensitiv informasjon som passord, API-tokens eller personlig legitimasjon i offentlige repositorier, da denne informasjonen blir permanent tilgjengelig for alle med tilgang til repositoriet.


### Opprette og administrere pull-forespørsler


Kulminasjonen av ditt bidrag innebærer å opprette en pull-forespørsel, som fungerer som et formelt forslag om å slå sammen endringene dine i det opprinnelige prosjektdepotet. Denne prosessen begynner i GitHub fork, der du kan se forskjellene mellom ditt eget depot og oppstrømskilden. GitHubs grensesnitt viser tydelig antall commits foran eller bak, noe som gir umiddelbar oversikt over omfanget av de foreslåtte endringene dine. Før du oppretter en pull-forespørsel, bør du sørge for at fork er synkronisert med de nyeste oppstrømsendringene for å minimere potensielle konflikter.


Å lage en effektiv pull-forespørsel krever mer enn bare å sende inn kodeendringene dine. Beskrivelsen av pull-forespørselen er din mulighet til å kommunisere formålet, omfanget og virkningen av endringene dine til prosjektets vedlikeholdere og fellesskap. En velskrevet beskrivelse forklarer hvilke problemer endringene dine løser, hvordan du har implementert løsningen, og eventuelle konsekvenser for andre deler av prosjektet. Denne dokumentasjonen blir spesielt viktig for komplekse endringer som kanskje ikke er umiddelbart åpenbare bare ved å undersøke kodeforskjellene.


Gjennomgangsprosessen representerer et samarbeidsaspekt ved utvikling av åpen kildekode, der prosjektvedlikeholdere og erfarne bidragsytere vurderer de foreslåtte endringene dine. Du kan be om spesifikke korrekturlesere som har ekspertise på de områdene endringene dine påvirker, slik at du sikrer at kunnskapsrike medlemmer av fellesskapet ser på arbeidet ditt. Gjennomgangsprosessen kan involvere flere iterasjoner, der korrekturleserne gir tilbakemeldinger, ber om endringer eller ber om ytterligere testing. Denne samarbeidsprosessen bidrar til å opprettholde kodekvaliteten, samtidig som den gir verdifulle læringsmuligheter for bidragsytere på alle erfaringsnivåer.


Forståelsen av at ikke alle pull-forespørsler blir akseptert, bidrar til å skape riktige forventninger til bidragsprosessen. Prosjektansvarlige kan avvise pull-forespørsler av ulike grunner, for eksempel fordi de ikke er i tråd med prosjektets mål, ikke er tilstrekkelig testet eller fordi det finnes alternative løsninger som allerede er under utvikling. I stedet for å se på et avslag som en fiasko, bør man se på det som en mulighet til å lære av tilbakemeldingene, forbedre tilnærmingen og eventuelt bidra med alternative løsninger som bedre oppfyller prosjektets behov. Open source-fellesskapet trives med denne iterative prosessen med forslag, gjennomgang og forbedring, som til syvende og sist driver prosjekter fremover gjennom kollektiv innsats og delt ekspertise.



## Hva er Public-Pool?

<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>


:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

Public Pool representerer en revolusjonerende tilnærming til Bitcoin mining som løser mange av bekymringene utvinnere har med tradisjonelle mining-bassenger. Public Pool er et Bitcoin mining-basseng med åpen kildekode og endrer fundamentalt modellen for belønningsfordeling som utvinnere har blitt vant til. I motsetning til konvensjonelle mining-basseng der deltakerne deler belønningene når en utvinner i bassenget finner en blokk, fungerer Public Pool etter et solo mining-prinsipp der individuelle utvinnere beholder 100 % av blokkbelønningene når de lykkes med å utvinne en blokk.


Den mest overbevisende egenskapen ved Public Pool er dens gebyrfrie struktur. Når utvinnere finner en blokk ved hjelp av Public Pool, mottar de hele blokkbelønningen sammen med alle tilknyttede transaksjonsgebyrer, uten fradrag for driftskostnader for bassenget. Dette står i sterk kontrast til tradisjonelle mining-bassenger, som vanligvis tar gebyrer på 1-3 % av mining-belønningen. Modellen med null gebyrer gjør Public Pool spesielt attraktiv for utvinnere som ønsker å maksimere sin potensielle avkastning samtidig som de opprettholder full kontroll over mining-operasjonene sine.


For å forstå Public Pools unike posisjon er det viktig å forstå den grunnleggende forskjellen mellom solo mining og pooled mining. Ekte solo mining betyr at du utvinner uavhengig og mottar hele blokkbelønningen (for øyeblikket 3,125 BTC + avgifter) hvis du finner en blokk, men sannsynligheten er proporsjonal med hashfrekvensen din i forhold til hele nettverket - noe som skaper ekstrem varians som kan spenne over måneder eller år mellom belønningene. Tradisjonelle bassenger kombinerer hashkraft for å finne blokker oftere, fordele belønningene proporsjonalt og gi en jevn, forutsigbar inntekt. For utvinnere som har investert betydelig kapital i maskinvare og driftskostnader, er ren solo mining vanligvis upraktisk, uavhengig av de filosofiske fordelene - variansen gjør det nesten umulig å dekke strømkostnadene og få tilbake investeringene. Denne økonomiske realiteten betyr at de fleste utvinnere vil velge mining i en pool av praktiske, økonomiske årsaker. Public Pool fungerer som et solo mining-basseng, noe som betyr at du fortsatt står overfor variansen til solo mining (du blir bare belønnet når du personlig finner en blokk), men du drar nytte av bassengets infrastruktur og gjennomsiktige, avgiftsfrie drift.


### Fordelen med åpen kildekode og teknisk implementering


Public Pools satsing på utvikling med åpen kildekode gir utvinnere enestående åpenhet og kontroll over mining-operasjonene sine. Hele kodebasen er tilgjengelig på GitHub, slik at utvinnere kan undersøke nøyaktig hvordan programvaren fungerer, endre den i henhold til deres behov og til og med bidra til utviklingen av den. Denne åpenheten adresserer en betydelig bekymring i mining-miljøet angående de ukjente konfigurasjonene og praksisene til tradisjonelle mining-pooler.


Programvarearkitekturen omfatter både kjernefunksjonaliteten til mining Pool og et eget brukergrensesnitt, som begge er fritt tilgjengelige for nedlasting og modifisering. Utvinnere kan kjøre Public Pool i ulike konfigurasjoner, inkludert Docker-containere, noe som gjør det mulig å tilpasse det til ulike maskinvareoppsett og tekniske preferanser. Den omfattende dokumentasjonen i GitHub-lagrene inneholder detaljerte installasjonsveiledninger, konfigurasjonsalternativer og modifikasjonsinstruksjoner, noe som gjør den tilgjengelig for utvinnere med varierende teknisk kompetanse.


Tilkobling til Public Pool krever minimal konfigurasjon sammenlignet med tradisjonelle mining-oppsett. Utvinnere trenger bare å konfigurere mining-enhetene sine med Stratum-tilkoblingsdetaljer og oppgi Bitcoin-adressen sin som brukernavn. Et valgfritt arbeidsnavn kan legges til etter en punktseparator for organisatoriske formål.


### Samfunnsfunksjoner og bærekraftsmodell


Public Pool har flere innovative funksjoner som styrker Bitcoin mining-fellesskapet, samtidig som det opprettholder nullavgiftsdriften. Plattformen viser omfattende statistikk, inkludert den totale hashraten til tilkoblede utvinnere, som vanligvis lå på mellom 1 og 2 PetaHash per sekund i 2024 og rundt 40 PH/s i november 2025, og gir detaljert informasjon om tilkoblede mining-enheter. Spesielt bemerkelsesverdig er plattformens vektlegging av mining-maskinvare med åpen kildekode, med enheter merket med stjerner som indikerer design med åpen kildekode, komplett med lenker til deres respektive GitHub-repositorier.


Bærekraften til Public Pools avgiftsfrie drift er avhengig av et kreativt partnerskap med mining-maskinvareleverandører. Når utvinnere kjøper utstyr fra partnerselskaper med rabattkoden "SOLO", går femti prosent av inntektene til Public Pools driftskostnader, mens de resterende femti prosentene deles ut som belønning til utvinnere som oppnår de høyeste vanskelighetsgradene hver måned. Denne modellen skaper et symbiotisk forhold der utvinnerne får rabatter på utstyrskjøp, leverandørene får kunder, og Public Pool opprettholder driften uten å kreve direkte gebyrer.


### Desentraliseringsfilosofi og beste praksis


Public Pool er et utmerket alternativ til tradisjonelle mining-bassenger, men det er viktig å forstå dens rolle i en bredere sammenheng med Bitcoin-desentralisering. Plattformen fungerer som et springbrett mot det endelige målet om at individuelle utvinnere skal drive sine egne mining-bassenger. Å drive ditt eget mining-basseng representerer det høyeste nivået av desentralisering, ettersom det eliminerer avhengighet av tredjeparts infrastruktur eller programvare, uavhengig av hvor gjennomsiktig eller velmenende denne tredjeparten måtte være.


Public Pools åpne kildekode gjør det til en ideell læringsplattform for utvinnere som ønsker å forstå driften av bassenget før de implementerer sine egne løsninger. Tilgjengeligheten av installasjonsveiledninger for flere operativsystemer og den omfattende dokumentasjonen gir utvinnere kunnskapen som trengs for å gå fra å bruke Public Pool til å drifte sin egen mining-infrastruktur. Dette pedagogiske aspektet er i tråd med Bitcoins grunnleggende prinsipper om selvsuverenitet og desentralisering, og gir individuelle utvinnere mulighet til å ta full kontroll over mining-operasjonene sine, samtidig som de bidrar til den generelle sikkerheten og desentraliseringen av Bitcoin-nettverket.


Plattformens brukergrensesnitt gir utvinnere detaljerte overvåkingsfunksjoner, inkludert arbeiderstatus, hashfrekvensstatistikk og ytelsesmålinger. Disse funksjonene hjelper utvinnerne med å optimalisere driften, samtidig som de lærer om prinsipper for bassengadministrasjon som de senere kan bruke i sine egne mining-bassengimplementeringer.


## Slik installerer du Public-Pool på Umbrel

<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>


:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

Det har blitt stadig lettere å drive et eget Bitcoin mining-basseng hjemme med moderne maskinvare og forenklede programvareløsninger. Dette kapittelet tar for seg den praktiske implementeringen av et hjemmebasert offentlig basseng ved hjelp av rimelig mini-PC-maskinvare og strømlinjeformet programvare for nodeadministrasjon. Når du er ferdig med denne veiledningen, vil du forstå maskinvarekravene, programvareoppsettprosessen og den grunnleggende konfigurasjonen som trengs for å etablere din egen mining-bassenginfrastruktur.


### Krav til maskinvare og oppsett


Grunnlaget for ethvert mining-bassengoppsett i hjemmet begynner med å velge passende maskinvare som balanserer ytelse, kostnader og energieffektivitet. En mini-PC er en ideell løsning for dette bruksområdet, fordi den har tilstrekkelig prosessorkraft samtidig som den er kompakt og har et rimelig strømforbruk. Den anbefalte konfigurasjonen inkluderer en Intel N100-prosessor, som gir tilstrekkelige beregningsressurser for bassengoperasjoner, sammen med minst én terabyte NVMe-lagringsplass for å romme Bitcoin-blokkjeden og tilhørende data.


Lagringskravet er spesielt kritisk siden det å kjøre en mining-pool krever at man opprettholder en fullstendig synkronisert Bitcoin-node. NVMe-stasjonen på én terabyte sikrer raske lese-/skriveoperasjoner som er avgjørende for blokkjedesynkronisering og pågående transaksjonsbehandling. I tillegg støtter tilstrekkelig RAM-allokering jevn drift av både det underliggende Linux-operativsystemet og nodeadministrasjonsprogramvaren som skal koordinere aktiviteter i bassenget.


### Programvarearkitektur og nodeadministrasjon


Programvarestakken for en hjemme mining-pool bygger på et Linux-grunnlag som gir den stabiliteten og sikkerheten som er nødvendig for Bitcoin-drift. På toppen av dette basissystemet skaper spesialisert programvare for nodeadministrasjon, som Umbrel, et intuitivt grensesnitt for administrasjon av Bitcoin-infrastruktur. Denne tilnærmingen fjerner mye av kompleksiteten som tradisjonelt er forbundet med å drive Bitcoin-noder, og gjør driften av bassenget tilgjengelig for brukere uten omfattende teknisk bakgrunn.


Umbrel fungerer som en omfattende nodeadministrasjonsplattform som håndterer installasjon, synkronisering og løpende vedlikehold av Bitcoin Core gjennom et nettbasert grensesnitt. Plattformens app store-modell gjør det enkelt å installere tilleggstjenester, inkludert mining-programvare for bassenger, ved hjelp av enkle pek-og-klikk-operasjoner. Denne arkitekturen sikrer at brukerne kan fokusere på bassengdrift i stedet for systemadministrasjon, samtidig som de opprettholder full kontroll over Bitcoin-infrastrukturen.


### Installasjon og konfigurasjon av offentlige basseng


Installasjon av programvare for offentlige bassenger via Umbrel-plattformen viser hvor strømlinjeformet moderne Bitcoin-infrastrukturdistribusjon er. Prosessen begynner med å gå til Umbrels appbutikk via nettgrensesnittet, der et enkelt søk etter "public pool" avslører den tilgjengelige mining-programvaren. Installasjonen krever bare noen få klikk: velg applikasjonen, bekreft installasjonen og vent på at den automatiske installasjonsprosessen skal fullføres.


Installasjonsprosessen konfigurerer automatisk de nødvendige tilkoblingene mellom programvaren for det offentlige utvinnerbassenget og den underliggende Bitcoin-noden. Denne integrasjonen sørger for at bassenget kan validere transaksjoner, konstruere blokkmaler og distribuere arbeid til tilkoblede utvinnere uten at det kreves manuell konfigurering av komplekse nettverksparametere. Når installasjonen er fullført, blir pool-grensesnittet umiddelbart tilgjengelig via det lokale nettverket, noe som gir mulighet for overvåking og administrasjon i sanntid.


### Tilkobling av gruvearbeidere og nettverkshensyn


For å koble mining-maskinvare til det nyetablerte bassenget må du konfigurere innstillingene for gruvearbeiderens basseng til å peke mot din lokale infrastruktur. Dette innebærer å erstatte standard bassengadresse med din lokale IP-adresse og det riktige portnummeret som ble tildelt under installasjonen av det offentlige bassenget. Konfigurasjonsendringen omdirigerer mining-maskinvarens beregningsinnsats fra eksterne bassenger til din hjemmebaserte infrastruktur, slik at du kan beholde full kontroll over mining-driften og potensielle belønninger.


Nettverkskonfigurasjonen spiller en avgjørende rolle for bassengets tilgjengelighet og funksjonalitet. Oppsett av lokale nettverk innebærer vanligvis standard IP-adressering, men brukere kan støte på variasjoner i DNS-oppløsningen avhengig av ruterkonfigurasjonen. Noen rutere tilbyr lokale DNS-tjenester som oppretter egne navn for lokale tjenester, mens andre krever direkte tilgang til IP-adresser. For å få bredere tilgjengelighet utenfor det lokale nettverket kan det være nødvendig å konfigurere portvideresending på ruteren, men dette medfører ytterligere sikkerhetshensyn som krever en nøye vurdering av risiko og fordeler.


En vellykket etablering av en mining-pool i hjemmet representerer et viktig skritt mot en desentralisert Bitcoin-infrastruktur, som gir både pedagogisk verdi og praktiske mining-muligheter, samtidig som du beholder full kontroll over Bitcoin-driften.


# Montering av maskinvare og feilsøking

<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>


## Hvilke verktøy skal jeg bruke?

<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>


:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

Når det gjelder lodding av overflatemonterte komponenter (SMD), og særlig når du arbeider med Bitaxe-prosjekter, er det de riktige verktøyene som utgjør forskjellen mellom frustrasjon og suksess. Denne omfattende veiledningen tar for seg det essensielle utstyret du trenger for å løse SMD-loddeprosjekter på en effektiv måte, fra grunnleggende håndverktøy til spesialutstyr som vil forbedre dine loddeegenskaper.


Hvis du vil se noe dokumentasjon om skjemaene, kan du sjekke denne [GitHub repo](https://github.com/skot/bitaxe-doc/tree/main).


### Grunnleggende håndverktøy og presisjonsinstrumenter


Grunnlaget for ethvert SMD-loddeoppsett begynner med en kvalitetspinsett, som fungerer som det primære verktøyet for plassering av komponenter. To typer pinsetter er mest verdifulle i dette arbeidet: standard pinsetter med rett spiss og pinsetter med en lett bøyd spiss. Den med rett spiss kan brukes til de fleste SMD-komponenter som finnes i typiske Bitaxe-sett, mens pinsetten med bøyd spiss utmerker seg når du arbeider med ekstremt små komponenter som krever presis plassering. Disse verktøyene følger ofte med i reparasjonssett, for eksempel iFixit-sett for telefonreparasjoner, noe som gjør dem lett tilgjengelige for de fleste hobbyister.


Som et supplement til pinsetten er en god saks uunnværlig når du skal klippe elektrotape, som har flere formål i elektronikkprosjekter. Elektrotape er en viktig isolasjon for kabler og komponenter, og god kvalitetstape gjør loddeprosessen enklere. Disse grunnleggende forsyningene kan kjøpes i jernvareforretninger eller nettbutikker, uten at det er nødvendig med spesialiserte elektronikkleverandører.


### Påføring og håndtering av loddepasta


Påføring av loddepasta er et av de mest kritiske aspektene ved SMD-lodding, og de riktige verktøyene gjør denne prosessen både nøyaktig og behagelig. Små, ikke-skarpe sprøyter fylt med loddepasta gir eksepsjonell kontroll over plasseringen av pastaen. Denne metoden gjør det mulig å påføre nøyaktig den mengden loddepasta som trengs for hver skjøt, og de fleste utvikler raskt riktig teknikk for å kontrollere trykk og strømningshastighet gjennom praktisk øvelse.


Valget av loddepasta har stor betydning for hvor vellykket loddingen blir. ChipQuik TS391SNL50 skiller seg ut som en eksepsjonell loddepasta for Bitaxe-prosjekter og generelt SMD-arbeid. Denne pastaen har riktig konsistens og smelteegenskaper, slik at man unngår problemene som er forbundet med billigere alternativer med for lavt smeltepunkt. Loddepasta av lav kvalitet kan skape problemer der tidligere loddede skjøter blir flytende igjen når tilstøtende områder varmes opp, noe som fører til forskyvning av komponenter og dårlige forbindelser. Selv om loddepasta av høy kvalitet representerer en høyere initialinvestering, rettferdiggjør de forbedrede resultatene og den reduserte frustrasjonen utgiften.


### Verktøy for problemløsning og opprydding


Selv erfarne loddere støter på problemer som må rettes opp, noe som gjør avloddeutstyr til en viktig del av ethvert komplett verktøysett. En avloddingsrigg, som egentlig er et oppvarmet vakuumverktøy, fjerner overflødig loddetinn og korrigerer broforbindelser mellom komponentpinnene. Disse verktøyene fungerer mest effektivt når de kombineres med flussmiddel, noe som forbedrer loddeflyten og gjør avloddeprosessen mer effektiv.


Flussmiddel finnes i ulike former, både i fast og flytende form, og har flere formål enn bare å avlodde. Når loddepastaen begynner å miste sin effektivitet under lengre arbeidsøkter, kan man bruke ekstra flussmiddel for å gjenopprette riktig flyt og sikre pålitelige forbindelser. Et lite skje-lignende verktøy, som ofte finnes i presisjonsreparasjonssett, gjør det enklere å påføre flussmiddel på bestemte områder uten å forurense omkringliggende komponenter.


Rengjøring av tavler er det siste trinnet i et profesjonelt kvalitetsarbeid, og krever isopropanolalkohol og en dedikert rengjøringsbørste. En gammel tannbørste fungerer perfekt til dette formålet, og en klemmeflaske med isopropanol gjør det mulig å påføre rengjøringsløsningen på en kontrollert måte. Denne kombinasjonen fjerner flussmiddelrester og pastarester, og etterlater kortene med et rent, profesjonelt utseende som også gjør det lettere å inspisere loddeskjøtene.


### Spesialisert utstyr og avanserte verktøy


For prosjekter som involverer komplekse integrerte kretser, spesielt ASIC-er, forvandler sjablongene loddeprosessen fra kjedelig håndplassering til effektiv og nøyaktig påføring av pasta. Disse presisjonskuttede malene sikrer jevn limtykkelse og plassering, noe som reduserer tidsforbruket for komplekse komponenter dramatisk og samtidig forbedrer påliteligheten. Investeringen i kvalitetsstenciler lønner seg i form av både tidsbesparelser og bedre resultater.


Varmestyring blir avgjørende når man arbeider med strømkomponenter, noe som gjør termisk pasta eller termisk fett til viktige forsyninger. Disse materialene sørger for riktig varmeoverføring mellom kjøleribber og integrerte kretser, forhindrer termiske skader og sikrer pålitelig drift. Materialer av høy kvalitet til termiske grensesnitt er en liten investering som beskytter mye dyrere komponenter.


Hjertet i ethvert SMD-loddeoppsett er varmluftsstasjonen, som gir den kontrollerte varmen som er nødvendig for overflatemontert arbeid. Selv om budsjettstasjoner i prisklassen 30-50 dollar kan fungere tilfredsstillende, er de ofte ikke like pålitelige og presise som utstyr av høyere kvalitet. Disse stasjonene fungerer vanligvis effektivt ved 355 °C og inkluderer automatisk temperaturreduksjon når håndstykket settes tilbake i holderen. Påliteligheten kan imidlertid være varierende, og noen enheter svikter for tidlig. For seriøst arbeid er det bedre å investere i utstyr av høyere kvalitet fra spesialiserte elektronikkleverandører, noe som gir bedre langsiktig verdi gjennom bedre pålitelighet og mer presis temperaturkontroll.


Kombinasjonen av disse verktøyene gir deg en komplett SMD-loddekompetanse som strekker seg langt utover Bitaxe-prosjekter til generelt elektronikkarbeid. Ved å forstå hvert enkelt verktøys rolle og velge kvalitetsutstyr som passer til ditt ferdighetsnivå og prosjektkrav, sikrer du vellykkede resultater og en hyggelig loddeopplevelse.



## Løs problemer med lodding

<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>


:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


Bitaxe-transceiversettet byr på unike utfordringer under monteringen, noe som krever nøye oppmerksomhet på komponentorientering, forebygging av loddebroer og riktig varmestyring. Det er viktig å forstå disse vanlige problemene og løsningene på dem for å lykkes med byggingen av settet og unngå kostbare komponentskader. Dette kapittelet tar for seg de vanligste loddeproblemene som oppstår under Bitaxe-montering, og gir praktiske teknikker for å identifisere og løse dem.


### Orientering og identifikasjon av komponenter


Riktig komponentorientering er et av de mest kritiske aspektene ved vellykket Bitaxe-montering, spesielt når det gjelder MOSFET Q1 og Q2. Disse komponentene har særegne orienteringsmarkører som må følges nøye under installasjonen. Hver MOSFET har en liten prikkmarkering som korresponderer med en bestemt plassering av puter på kretskortet. Nøkkelen til riktig orientering ligger i å forstå den fysiske strukturen til disse komponentene, som har fire pinner arrangert med én stor pute og tre mindre puter som ikke har noen forbindelse til den store puten.


Når du installerer Q1 og Q2, må du undersøke både komponenten og kretskortet nøye. Kretskortets layout viser tydelig den tiltenkte retningen gjennom putekonfigurasjonen, med fire pinner plassert slik at de passer med MOSFET-strukturen. Før du lodder på en stor komponent, må du alltid verifisere retningen ved å sammenligne komponentens fysiske markører med kretskortets putearrangement. Dette enkle verifiseringstrinnet gjør at du slipper å avlodde og montere feilorienterte komponenter på nytt.


Konsekvensene av feil orientering strekker seg lenger enn til enkle funksjonsproblemer. Feilorienterte MOSFET-er kan føre til kretsfeil som er vanskelige å diagnostisere, og som kan kreve fullstendig utskifting av komponenter. Hvis du tar deg tid til å verifisere orienteringen før du påfører varme, sikrer du at kretsen fungerer som den skal og unngår unødvendig feilsøking senere i monteringsprosessen.


### Håndtering av loddebroer og overskuddslodd


Loddebroer er en annen vanlig utfordring ved Bitaxe-montering, spesielt rundt komponenter med fin pitch som U10. Disse uønskede forbindelsene mellom tilstøtende pinner kan forårsake funksjonsfeil i kretsen, og krever forsiktige teknikker for fjerning. Den mest effektive metoden er å bruke avloddingsveke, et kobberflettet materiale som absorberer overflødig loddetinn når det varmes opp. Denne teknikken krever tålmodighet og riktig valg av verktøy for å unngå å skade ømfintlige komponenter.


Når du arbeider med loddebroer på integrerte kretser, må du bruke en PCB-holder eller en leddet klemme for å holde komponenten sikkert mens du arbeider. Påfør forsiktig varme på det berørte området, og trekk forsiktig avloddeveken over de brodannede forbindelsene. Kobberflettet absorberer naturlig det overflødige loddetinnet, slik at de uønskede forbindelsene skilles fra hverandre. Denne prosessen kan kreve flere forsøk, men utholdenhet gir rene, korrekt separerte forbindelser.


Forebygging er fortsatt den beste måten å håndtere loddebroer på. Ved å bruke passende mengder loddepasta og holde en stødig hånd under komponentplasseringen reduseres brodannelsen betydelig. Når det oppstår broer, må du ta tak i dem umiddelbart i stedet for å håpe at de ikke påvirker kretsens funksjon. Selv tilsynelatende små broer kan forårsake betydelige funksjonsproblemer som er vanskelige å diagnostisere når kretskortet er ferdig montert.


### Kritiske komponenter og spesielle hensyn


Buck-omformeren U9 fortjener spesiell oppmerksomhet på grunn av dens kritiske rolle i konverteringen av 5 volt til 1,2 volt for ASIC-brikken. Denne komponenten byr på unike utfordringer på grunn av de fem små tilkoblingene og tendensen til feil. Riktig installasjon krever presis påføring av loddepasta og nøye varmestyring. Utilstrekkelig loddepasta under U9 kan føre til dårlige tilkoblinger som hindrer riktig spenningskonvertering, mens overflødig pasta kan skape broer som forårsaker funksjonsfeil i kretsen.


U9 produserer særegne lydsignaturer når det oppstår problemer med loddebroen, og genererer høyfrekvent støy som avviker fra normal ASIC-drift. Denne auditive diagnoseteknikken kan bidra til å identifisere problemer, selv om det krever god høyfrekvent hørsel for å oppdage dem. Når lyddiagnose ikke er mulig, er visuell inspeksjon avgjørende. Undersøk alle tilkoblinger nøye, og se etter broer eller utilstrekkelig loddebelegg.


Hvis U9 ikke gir ut de nødvendige 1,2 volt til tross for at den ser ut til å være riktig loddet, er det sannsynlig at årsaken er utilstrekkelig loddepasta. Fjern komponenten, påfør en liten mengde ekstra loddepasta, og sett den inn igjen. I tilfeller der enkelte pinner ikke er tilstrekkelig loddet med loddepasta, kan du forsiktig påføre små mengder loddepasta på bestemte steder ved hjelp av en pinsett. Loddepastaen vil flyte naturlig under komponenten når den varmes opp, og skape riktige forbindelser ved hjelp av kapillærvirkning.


### Varmestyring og beskyttelse av komponenter


Riktig varmestyring beskytter følsomme komponenter mot termiske skader og sikrer samtidig pålitelige loddeskjøter. Komponenter som krystalloscillatoren Y1 og U1 er spesielt følsomme for langvarig varmeeksponering og krever nøye temperaturkontroll. Hold loddeboltens temperatur på 350 grader Celsius, men minimer varmetilførselen for å unngå skade på komponentene. Raske, effektive loddeteknikker beskytter disse følsomme komponentene samtidig som du oppnår pålitelige tilkoblinger.


ASIC-brikken krever spesielle håndteringsteknikker på grunn av den komplekse pinnestrukturen og følsomheten for mekanisk belastning. Når du bruker sjablonger for påføring av loddepasta, må du sørge for jevn dekning over alle pinnene for å unngå ujevn plassering av komponentene. Hvis for mye loddepasta fører til at ASIC sitter ujevnt, må du la monteringen avkjøles helt før du foretar korrigeringer. Trykk forsiktig kun på komponentens merkede kanter, aldri på det sentrale matriseområdet, under gjenoppvarming for å oppnå riktig plassering.


Komponent U8 byr på unike utfordringer på grunn av de mange pinnene og muligheten for bøyde ledninger. Hvis pinnene bøyes under håndteringen, må du bruke en kretskortholder eller en leddet klemme for å sikre komponenten og forsiktig rette ut de berørte pinnene. Arbeid sakte og tålmodig for å unngå å knekke de skjøre ledningene. Det kan forenkle feilsøkingen å forstå at visse pinnegrupper på U8 er internt koblet sammen, ettersom broene mellom disse spesifikke pinnene ikke påvirker kretsens funksjon. Broer mellom andre pinner må imidlertid fjernes forsiktig for å sikre at de fungerer som de skal.


## Slik feilsøker du Bitaxe ved hjelp av AxeOS

<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>

:::video id=d23d748b-510e-4748-9617-b875da757031:::

Når du arbeider med Bitaxe mining-enheter, kan maskinvarefeil manifestere seg på ulike måter som kanskje ikke er umiddelbart åpenbare. Hvis du forstår hvordan du systematisk kan diagnostisere disse problemene ved hjelp av AxeOS-operativsystemet, kan du spare mye tid og unngå unødvendige komponentutskiftninger. Dette kapittelet tar for seg diagnoseteknikkene og feilsøkingsmetodene som erfarne teknikere bruker for å identifisere spesifikke maskinvareproblemer ved hjelp av programvareanalyse.


### Forstå strømforbruksindikatorene


Den første og mest kritiske diagnostiske indikatoren i AxeOS er overvåking av strømforbruket. Normale Bitaxe-enheter, inkludert Bitaxe Ultra- og Bitaxe Supra-modellene, bruker vanligvis mellom 10 og 17 watt under standard drift. Denne grunnlinjemålingen fungerer som din primære helseindikator for hele systemet. Når strømforbruket faller betydelig under dette området, spesielt under 3 watt, signaliserer det et grunnleggende problem med ASIC-brikken eller dens støttekretser.


Scenarier med lavt strømforbruk krever umiddelbar oppmerksomhet, fordi de indikerer at mining-brikken enten ikke fungerer, eller at den er svært degradert. Denne målingen alene kan hjelpe deg med å raskt skille mellom ytelsesproblemer og komplette maskinvarefeil. Strømmålingen i AxeOS gir deg tilbakemelding i sanntid, slik at du kan overvåke effektiviteten av eventuelle reparasjonsforsøk du gjør på enheten.


### Analyse av ASIC spenningsmålinger


ASIC-spenningsmålefunksjonen i AxeOS gir viktig diagnostisk informasjon som hjelper deg med å finne den nøyaktige årsaken til maskinvareproblemer. Når du undersøker spenningsavlesninger, må du forstå forholdet mellom målt spenning og forespurt spenning for å kunne diagnostisere problemer på riktig måte. Systemet viser både spenningen som leveres til ASIC-brikken, og spenningen som brikken ber om fra strømstyringssystemet.


Når du observerer en ASIC-spenningsmåling på nøyaktig 1,2 volt kombinert med et strømforbruk på under 3 watt, indikerer denne spesifikke kombinasjonen enten et loddeproblem med ASIC-brikken eller en fullstendig defekt ASIC. Denne spenningsmålingen tyder på at strømmen når frem til brikken, men at selve brikken ikke fungerer som den skal. Fysisk inspeksjon av ASIC-brikken kan avdekke sprekker eller andre synlige skader som kan forklare dette atferdsmønsteret.


Et annet diagnostisk scenario dukker opp når du ser lavt strømforbruk kombinert med svært lave forespurte spenningsverdier, for eksempel 100 millivolt eller 0,5 volt. Dette mønsteret indikerer at ASIC-brikken ikke får tilstrekkelig spenningsforsyning, noe som vanligvis peker mot problemer med U9 buck converter-komponenten. Buck-omformeren er ansvarlig for å sørge for den nøyaktige spenningsreguleringen som ASIC-brikkene trenger for å fungere korrekt.


### Tolkning av loggdata og ASIC-kommunikasjon


AxeOS-loggføringssystemet gir verdifull innsikt i om ASIC-brikken kommuniserer med kontrollsystemet. Når du åpner loggene via funksjonen "show logs", bekrefter tilstedeværelsen av "ASIC results"-oppføringer at brikken ikke bare er strømforsynt, men at den også aktivt behandler arbeid og returnerer resultater. Denne kommunikasjonen indikerer at ASIC er riktig loddet og opprettholder forbindelsen til kontrollkretsen.


Fraværet av ASIC-resultater i loggene, spesielt i kombinasjon med andre symptomer, gjør det lettere å avgrense problemet til spesifikke komponenter eller tilkoblingsproblemer. Denne diagnostiske tilnærmingen gjør det mulig å skille mellom brikker som ikke reagerer, og brikker som kan ha intermitterende tilkoblingsproblemer. Logganalysen er spesielt verdifull ved feilsøking av komplekse problemer der flere symptomer kan tyde på ulike rotårsaker.


### Systematisk tilnærming til feilsøking


Når du skal diagnostisere Bitaxe-maskinvareproblemer, bør du følge en systematisk fremgangsmåte for å unngå å overse kritiske problemer og sikre effektive reparasjonsprosesser. Begynn med å dokumentere strømforbruket og spenningsavlesningene, og korrelér deretter disse målingene med loggdataene for å danne deg et komplett bilde av systemets oppførsel. Denne metodiske tilnærmingen bidrar til å identifisere om problemene stammer fra selve ASIC-brikken, strømforsyningssystemet eller kommunikasjonsveiene mellom komponentene.


I tilfeller der U9 buck-konverteren ser ut til å være problemet, kan det være nødvendig med fysisk inspeksjon og eventuell omlodding. U9-komponenten er spesielt utsatt for loddeproblemer, spesielt i førstegangsmonteringssituasjoner. Ved mistanke om problemer med spenningsreguleringen kan man bruke et multimeter for å kontrollere at det faktisk er 1,2 volt på ASIC-pinnene, for å få en endelig bekreftelse på at det er problemer med strømforsyningen. Hvis det er spenning på pinnene, men ASIC fortsatt ikke fungerer, og fysisk inspeksjon ikke avdekker noen skade, er det neste logiske trinnet å bytte ut ASIC-brikken. Hvis problemene vedvarer selv etter utskifting av ASIC, kan U2-komponenten, som driver ASIC-brikken, kreve oppmerksomhet som det siste elementet i feilsøkingssekvensen.


## Hvordan feilsøke ved hjelp av USB?

<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>


:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


Ved feilsøking av Bitaxe mining-enheter gir direkte tilgang til enhetens interne loggsystem uvurderlig innsikt som nettbaserte grensesnitt ikke kan tilby. I dette kapittelet forklarer vi hvordan du oppretter en direkte seriell USB-tilkobling til Bitaxe-enheten din ved hjelp av ESP-IDF-rammeverket, slik at du kan overvåke systemlogger, oppstartssekvenser og feilmeldinger i sanntid. Denne feilsøkingsmetoden er spesielt viktig når man har å gjøre med enheter som ofte starter på nytt eller har maskinvarefeil, ettersom den fanger opp all diagnostisk informasjon som kan gå tapt under omstart av systemet.


Feilsøkingsprosessen krever Visual Studio Code med ESP-IDF-utvidelsen, men alle kompatible IDE-er kan brukes. Denne metoden fungerer med alle Bitaxe-varianter som har en USB-port, inkludert Bitaxe Ultra 204 og andre modeller i serien. Den direkte serielle tilkoblingen omgår potensielle begrensninger i nettgrensesnittet og gir ufiltrert tilgang til enhetens interne tilstandsinformasjon.


### Sette opp seriell kommunikasjon


Kommunikasjonen med Bitaxe-enheten begynner med at du kobler til USB-kabelen og åpner ESP-IDF-terminalen i utviklingsmiljøet ditt. Kommandoen `idf.py monitor` starter tilkoblingsprosessen, og skanner automatisk tilgjengelige COM-porter for å etablere UART-kommunikasjon med ESP32-brikken på Bitaxe-enheten. Systemet går vanligvis gjennom tilgjengelige porter (COM3, COM4, COM16 osv.) til det finner den riktige tilkoblingen.


Når terminalen er tilkoblet, viser den hele oppstartssekvensen og pågående driftslogger. Den første tilkoblingsprosessen kan ta noen øyeblikk mens systemet identifiserer riktig kommunikasjonsport. Hvis den automatiske portdeteksjonen mislykkes, kan du angi COM-porten manuelt via IDE-grensesnittet for portvalg. Denne direkte kommunikasjonskanalen forblir aktiv under hele driften av enheten, noe som gir kontinuerlig tilgang til systemdiagnostikk og ytelsesmålinger.


### Tolkning av oppstartsekvens og logger for normal drift


Oppstartssekvensen gir viktig informasjon om Bitaxe-enhetens maskinvarekonfigurasjon og initialiseringsprosess. Normale oppstartslogger begynner med informasjon om ESP-IDF-versjonen, etterfulgt av den karakteristiske meldingen "Welcome to the Bitaxe. Hack the planet", som bekrefter at innlastingen av fastvaren er vellykket. Deretter viser systemet ASIC-frekvenskonfigurasjon, identifikasjon av enhetsmodell og detaljer om kortversjon.


En velfungerende enhet vil vise vellykket I2C-initialisering og ASIC spenningsregulering satt til 1,2 volt. Loggene viser GPIO-statusinformasjon og Wi-Fi-initialiseringssekvenser, etterfulgt av DHCP-serverkonfigurasjon og IP-adressetildeling. En av de viktigste indikatorene er meldingen om ASIC-brikkeoppdagelse, som skal rapportere "oppdaget en ASIC-brikke" for en enhet med én brikke. Denne bekreftelsen bekrefter at mining-maskinvaren er riktig tilkoblet og kommuniserer med ESP32-kontrolleren.


Driftsloggene avslører flere samtidige oppgaver som kjører på enheten, inkludert stratum API-kommunikasjon, koordinering av hovedoppgaver, ASIC-oppgavehåndtering og stratumoppgavebehandling. Disse ulike oppgaveidentifikatorene bidrar til å isolere problemer til spesifikke systemkomponenter. Normal drift inkluderer etablering av bassengtilkobling, meldinger om justering av vanskelighetsgrad, jobb i og utenfor kø og rapportering av nonce-generering. Vellykkede mining-operasjoner viser ASIC-resultater med vanskelighetsberegninger, og mining sender inn bekreftelser når andelene oppfyller den nødvendige terskelen.


### Identifisere maskinvarefeil og feilmønstre


Maskinvarefeil manifesterer seg i loggene gjennom spesifikke feilmønstre som indikerer hvilke komponenter som ikke fungerer som de skal. Den vanligste feilmodusen involverer I2C-kommunikasjonsfeil med spesifikke integrerte kretser på Bitaxe-kortet. For eksempel vises DS4432U-kommunikasjonsfeil som "ESP_ERROR_CHECK failed"-meldinger med tidsavbruddsindikatorer, noe som tyder på problemer med spenningsregulering eller loddeproblemer som påvirker U10-komponenten som er ansvarlig for skjermkommunikasjon.


Disse feilmeldingene inneholder detaljert feilsøkingsinformasjon, for eksempel den spesifikke kildefilen (main_ds4432u.c), det mislykkede funksjonsanropet og prosessorkjernen som håndterer oppgaven. Tilbakesporingsinformasjonen gir ytterligere kontekst for avansert feilsøking. Lignende feilmønstre kan oppstå med EMC2101 temperatur- og viftekontrollbrikken, og hver av dem genererer særegne loggsignaturer som bidrar til å identifisere komponenten som feiler.


Fysiske maskinvareproblemer viser seg ofte som gjentatte feilsykluser etterfulgt av omstart av systemet. Hvis enheten produserer hørbar støy under drift, indikerer dette vanligvis loddeproblemer, for eksempel broer mellom komponentpinner eller utilstrekkelige loddefuger. Selv om disse mekaniske problemene ikke alltid generate spesifikke loggoppføringer, skaper de ustabile driftsforhold som manifesterer seg som hyppige krasj og omstartsykluser i overvåkningsutdataene.


### Avanserte feilsøkingsstrategier


Seriell overvåking gir flere fordeler i forhold til nettbaserte feilsøkingsgrensesnitt, spesielt ved periodiske feil eller enheter som ofte starter på nytt. Den kontinuerlige loggføringen sikrer at ingen diagnostisk informasjon går tapt under omstart av systemet, i motsetning til webgrensesnitt som kan miste data ved frakobling. Denne omfattende loggfunksjonen gjør det mulig å identifisere mønstre i feil og korrelere spesifikke feiltilstander med maskinvare- eller miljøfaktorer.


Når du analyserer problematiske enheter, bør du fokusere på sekvensen av hendelser som fører til feil i stedet for isolerte feilmeldinger. Vellykket ASIC-kommunikasjon bør vise regelmessig jobbbehandling, nonce-generering og sykluser for innsending av aksjer. Manglende ASIC-resultater i loggene indikerer kommunikasjonsfeil mellom ESP32 og mining-brikken, ofte forårsaket av problemer med strømforsyningen, ødelagte spor eller komponentfeil.


For systematisk feilsøking bør du dokumentere feilmønstre og komponentspesifikke feil før du søker støtte fra fellesskapet. De detaljerte feilloggene, inkludert spesifikke brikkeidentifikatorer og feilmodi, gjør det mulig for erfarne brukere å gi målrettet reparasjonsveiledning, for eksempel prosedyrer for komponentbytte eller loddekorrigeringer. Denne metodiske tilnærmingen til feilsøking av maskinvare forbedrer reparasjonsfrekvensen betydelig og reduserer feilsøkingstiden for komplekse problemer.


# Avansert tilpasning

<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>


## Modifiser kretskortet

<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>


:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

KiCad er et av de kraftigste open source-verktøyene som finnes for design og ruting av kretskort (PCB). Med denne profesjonelle programvaren kan ingeniører og hobbybrukere lage komplekse elektroniske konstruksjoner ved å plassere komponenter på virtuelle kretskort og rute de intrikate sporene som forbinder disse komponentene med hverandre. Det som gjør KiCad spesielt verdifullt for utdannings- og utviklingsformål, er at det er fullstendig åpen kildekode, slik at brukerne kan modifisere, tilpasse og lære av eksisterende design uten lisensbegrensninger.


Bitaxe-prosjektet er et godt eksempel på kraften i maskinvareutvikling med åpen kildekode, og tilbyr et komplett kretskortdesign som brukerne kan undersøke, modifisere og tilpasse etter egne behov. Denne tilgjengeligheten skaper et utmerket læringsmiljø der studenter og praktikere kan utforske PCB-design fra den virkelige verden samtidig som de utvikler sin forståelse av elektroniske systemer. Muligheten til å tilpasse visuelle elementer som logoer gir en lett tilgjengelig inngang for brukere som kan bli skremt av den tekniske kompleksiteten i elektronisk design.


### Sette opp KiCad-miljøet ditt


Før du begynner med tilpasningsarbeidet, er det viktig at du konfigurerer utviklingsmiljøet ditt på riktig måte. Bitaxe-depotet må lastes ned til din lokale maskin, noe som vanligvis gjøres ved hjelp av GitHubs ZIP-nedlastingsfunksjonalitet. Dette depotet inneholder alle nødvendige prosjektfiler, inkludert KiCad-prosjektfiler, komponentbiblioteker og designdokumentasjon som kreves for vellykket modifisering.


KiCad-installasjonen bør fullføres ved hjelp av den offisielle distribusjonen fra KiCad-nettstedet, noe som sikrer kompatibilitet med prosjektfilene og tilgang til de nyeste funksjonene. Når både depotet og KiCad er riktig installert, kan du åpne prosjektet ved å navigere til Bitaxe Ultra KiCad-prosjektfilen i den nedlastede depotstrukturen. Denne prosjektfilen fungerer som det sentrale navet som kobler sammen alle tilknyttede designfiler, komponentbiblioteker og konfigurasjonsinnstillinger.


Den første visningen av en kompleks PCB-design kan virke overveldende, med mange komponenter, spor og lag som skaper et tett visuelt landskap. KiCads 3D-visning er imidlertid et uvurderlig verktøy for å forstå den fysiske layouten og de romlige relasjonene i designet. Det tredimensjonale perspektivet forvandler den abstrakte skjematiske fremstillingen til en realistisk visualisering av det ferdige produktet, noe som gjør det lettere å forstå komponentplasseringen og den generelle designestetikken.


### Prosess for logotilpasning


Tilpasning av logoer på kretskortdesign er en av de mest tilgjengelige modifikasjonene for brukere som er nye i KiCad, og krever minimal teknisk kunnskap samtidig som det gir umiddelbare visuelle resultater. Prosessen begynner med bildekonverteringsverktøyet, som omdanner standard bildefiler til fotavtrykkformater som er kompatible med PCB-designprogramvaren. Denne konverteringsprosessen krever nøye oppmerksomhet på størrelsesparametrene, som vanligvis måles i millimeter for å sikre riktig skalering på det ferdigproduserte kretskortet.


Arbeidsflyten for bildekonvertering omfatter flere kritiske trinn som avgjør det endelige utseendet og plasseringen av de tilpassede logoene. Ved valg av bildekilde bør man prioritere design med høy kontrast som egner seg godt til silketrykkprosessen som brukes i kretskortproduksjonen. Størrelsesspesifikasjonen blir avgjørende, ettersom logoene må være store nok til å være leselige etter produksjonen, samtidig som de ikke må forstyrre komponentplasseringen eller funksjonaliteten. Valget mellom silketrykk på for- og baksiden påvirker både synlighet og produksjonshensyn.


Håndtering av fotavtrykksbiblioteker er et grunnleggende aspekt ved tilpasning av KiCad, og krever at brukerne forstår hvordan programvaren organiserer og gir tilgang til designelementer. Når man legger til egendefinerte logoer, må man opprette nye fotavtrykksbiblioteker eller endre eksisterende, og deretter koble disse bibliotekene til prosjektstrukturen på riktig måte. Denne prosessen sikrer at egendefinerte elementer forblir tilgjengelige på tvers av ulike designøkter, og at de enkelt kan deles med andre teammedlemmer eller samarbeidspartnere.


### Avansert utforskning og forståelse av design


I tillegg til enkel logo-tilpasning tilbyr KiCad kraftige verktøy for å utforske og forstå komplekse PCB-design. Lagstyringssystemet gjør det mulig for brukerne å vise ulike aspekter av designen, fra komponentplassering og ruting til produksjonsspesifikasjoner og monteringsinformasjon. Denne lagdelte tilnærmingen muliggjør detaljert analyse av spesifikke designelementer uten visuelt rot fra urelaterte komponenter.


Analyse av sporruting er et av de mest lærerike aspektene ved utforsking av kretskort, fordi det viser hvordan elektriske forbindelser flyter mellom komponenter og delsystemer. Ved å følge individuelle spor eller grupper av relaterte signaler kan brukerne utvikle forståelse for kretsfunksjonalitet og designbeslutninger. Ved å undersøke strømdistribusjonsnettverk kan man for eksempel se hvordan spenningsregulering og filtreringskomponenter fungerer sammen for å gi ren og stabil strøm til følsomme elektroniske komponenter.


Sammenhengen mellom skjematisk design og fysisk layout blir tydelig når man nøye undersøker komponentplassering og rutingsbeslutninger. Å forstå hvorfor spesifikke komponenter er plassert på bestemte steder, hvordan termiske hensyn påvirker layoutbeslutninger, og hvordan krav til signalintegritet styrer rutingsvalg, gir verdifull innsikt i profesjonell PCB-designpraksis. Denne kunnskapen er uvurderlig for brukere som utvikler sine egne design eller modifiserer eksisterende design for spesifikke bruksområder.


KiCads omfattende verktøy for kontroll og verifisering av konstruksjonsregler sikrer at modifikasjoner opprettholder elektrisk og produksjonsmessig kompatibilitet. Disse automatiserte systemene bidrar til å forhindre vanlige konstruksjonsfeil, samtidig som brukerne lærer om bransjestandarder og beste praksis. Integrasjonen av 3D-visualisering med elektriske designdata skaper et effektivt læringsmiljø der teoretiske konsepter blir håndgripelige gjennom visuell representasjon og interaktiv utforskning.


## Hvordan oppretter jeg en fabrikkfil?

<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>


:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

Å bygge tilpasset fastvare for ESP-baserte mining-enheter krever nøye oppmerksomhet på konfigurasjon, avhengigheter og riktig byggeprosess. Denne omfattende veiledningen går gjennom hele prosessen med å lage både standard firmware-binærfiler og fabrikkfiler som inkluderer forhåndskonfigurerte innstillinger, noe som gjør distribusjonen mer effektiv og reduserer installasjonstiden for sluttbrukerne.


Merk at dette kapittelet er ganske teknisk, og at du bare kan skumme gjennom det hvis du er nysgjerrig på det.


### Sette opp utviklingsmiljøet


For å starte utviklingen av ESP-Miner-fastvare bør du først etablere det riktige utviklingsmiljøet i Visual Studio Code, ideelt sett på en linux-distribusjon. ESP-IDF-utvidelsen fungerer som hjørnesteinen i dette oppsettet, og gir de nødvendige verktøyene og rammeverksintegrasjonen for ESP32-utvikling. Når ESP-IDF-utvidelsen installeres for første gang, får brukeren en installasjonsveiledning som gjør konfigurasjonsprosessen enklere.


Et viktig moment i installasjonsprosessen er å velge riktig ESP-IDF-versjon. Tidligere ble versjon 5.1.3 anbefalt, men praktisk erfaring har vist at denne versjonen kan forårsake byggeproblemer som kompliserer utviklingsprosessen. Nå anbefales det å bruke ESP-IDF versjon 5.3 Beta 1, som har vist seg å løse disse komplikasjonene og sikrer at Bitaxe-enhetene fungerer som de skal. Installasjonsprosessen krever at du velger alternativet Express-installasjon og spesifikt velger versjon 5.3 Beta 1 blant de tilgjengelige alternativene.


Oppsettet av utviklingsmiljøet omfatter ikke bare ESP-IDF-installasjonen, men også riktig terminalkonfigurasjon. Visual Studio Code tilbyr flere metoder for å få tilgang til ESP-IDF-funksjonalitet, inkludert kommandopaletten for å åpne en ESP-IDF-terminal eller ved hjelp av det dedikerte terminalikonet i grensesnittet. Dette spesialiserte terminalmiljøet sikrer at alle ESP-IDF-kommandoer fungerer som de skal, og gir tilgang til hele verktøykjeden.


### Konfigurere innstillinger for ESP-Miner


Konfigurasjonsfilen er kjernen i ESP-Miner-tilpasningsprosessen, og inneholder alle viktige parametere som definerer hvordan enheten skal fungere i målmiljøet. Konfigurasjonen omfatter nettverksinnstillinger, mining-gruppetilkoblinger og maskinvarespesifikke parametere som må skreddersys til det spesifikke distribusjonsscenarioet.


Nettverkskonfigurasjonen er den viktigste komponenten i installasjonsprosessen, og krever spesifisering av Wi-Fi-legitimasjon, inkludert SSID og passord. I stedet for å bruke plassholderverdier som "test", bør produksjonskonfigurasjoner inneholde den faktiske nettverkslegitimasjonen som enheten vil bruke i driftsmiljøet. Konfigurasjonen har også plass til ulike mining-bassengoppsett, og støtter både private bassengkonfigurasjoner med spesifikke IP-adresser og offentlige bassenger som public-pool.io med tilhørende portinnstillinger.


Mining-spesifikke konfigurasjonsparametere inkluderer stratum-brukerinnstillingen, som vanligvis tilsvarer Bitcoin-adressen som mining-belønninger skal sendes til. Ytterligere maskinvareparametere som frekvensinnstillinger, spenningskonfigurasjoner og ASIC-typespesifikasjoner må samsvare med målmaskinvareplattformen. GitHub-arkivet inneholder forhåndskonfigurerte eksempler for ulike maskinvarevarianter, for eksempel BM1368-konfigurasjonen som er utformet for Super-enheter og BM1366-innstillinger for Ultra-varianter. Spesifikasjoner for kortversjoner, for eksempel å sette portversjonen til 401 for nyere maskinvarerevisjoner, sikrer kompatibilitet med målenhetens spesifikke egenskaper.


### Bygge Web Interface og kjernefastvare


ESP-Miner-prosjektet inneholder et sofistikert webgrensesnitt som krever separat kompilering før hovedprosessen med å bygge fastvaren kan starte. Dette webgrensesnittet, som kalles AxeOS-fastvaren, gir brukerne et omfattende administrasjonsgrensesnitt for overvåking og kontroll av mining-enhetene sine.


Byggeprosessen for webgrensesnittet begynner med å navigere til HTTP-serverkatalogen i hoveddepotstrukturen, nærmere bestemt AxeOS-underkatalogen. Denne plasseringen inneholder den Node.js-baserte webapplikasjonen som krever installasjon av avhengigheter gjennom kommandoen npm install. Byggesystemet forutsetter at Node.js er riktig installert på utviklingssystemet, da dette er et grunnleggende krav for kompileringsprosessen for webgrensesnittet.


Etter installasjonen av avhengigheter kompilerer npm run build-kommandoen webgrensesnittkomponentene, og oppretter de nødvendige filene som skal bygges inn i ESP32-fastvaren. Denne kompileringsprosessen genererer optimaliserte nettressurser som gir brukergrensesnittfunksjonalitet og samtidig opprettholder effektiv minnebruk på den begrensede ESP32-plattformen. Det er viktig å fullføre dette kompileringstrinnet før du går videre til hovedkompileringen av fastvaren, ettersom ESP-Miner-fastvaren inneholder disse webgrensesnittkomponentene som en integrert funksjonalitet.


### Opprette fabrikkfiler med innebygd konfigurasjon


Opprettelsen av fabrikkfiler representerer en avansert distribusjonsstrategi som integrerer konfigurasjonsinnstillinger direkte i den binære fastvaren, noe som eliminerer behovet for manuell konfigurasjon under oppsettet av enheten. Denne tilnærmingen er spesielt verdifull i forbindelse med storskala distribusjon eller i situasjoner der konsekvent konfigurasjon på tvers av flere enheter er avgjørende.


Prosessen med å opprette en fabrikkfil begynner med å generere en binær konfigurasjonsfil fra CSV-konfigurasjonsfilen ved hjelp av ESP-IDFs NVS partition generator-verktøy. Dette verktøyet, som ligger i ESP-IDF-komponentkatalogen under nvs-flash/nvs-partition-generator, konverterer den lesbare konfigurasjonen til et binært format som er egnet for direkte lagring i flash-minnet. Skriptet nvs-partition-gen.py behandler config.csv-filen og genererer en config.binary-fil som er rettet mot 0x6000-minneadresseområdet.


Den endelige sammenstillingen av fabrikkfiler skjer ved hjelp av spesialiserte sammenslåingsskript som kombinerer binærfiler for fastvare med konfigurasjonsdata. Repositoryet tilbyr flere sammenslåingsalternativer, inkludert et standard sammenslåingsskript for grunnleggende fabrikkfiler og et sammenslåingsskript som inkluderer konfigurasjon, for omfattende fabrikkfiler. Skriptet merge-bin-with-config.sh oppretter fabrikkfiler som inkluderer både fastvarefunksjonaliteten og de forhåndskonfigurerte innstillingene, noe som resulterer i en komplett distribusjonspakke. Denne tilnærmingen gjør det mulig å opprette enhetsspesifikke fabrikkfiler, for eksempel versjoner som er skreddersydd for Bitaxe Ultra-enheter med spesifikke kortrevisjoner, samtidig som man opprettholder fleksibiliteten til å generate generiske fabrikkfiler uten innebygde konfigurasjoner for scenarier som krever manuell oppsettfleksibilitet.


De ferdige fabrikkfilene gir utrullingsteamene ferdige binære filer som inkluderer alle nødvendige fastvarekomponenter og konfigurasjonsinnstillinger, noe som effektiviserer klargjøringsprosessen for enheten og sikrer konsistente driftsparametere på tvers av utplasserte mining-enheter.


## Hvordan bruker jeg Bitaxe Web Flasher?

<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>


:::video id=291757b9-f459-48f6-8766-56387f907859:::

Bitaxe Web Installer representerer en strømlinjeformet tilnærming til fastvareadministrasjon for Bitaxe-enheter, og gir brukerne flere installasjonsalternativer gjennom et nettbasert grensesnitt. Dette omfattende verktøyet eliminerer kompleksiteten som tradisjonelt er forbundet med fastvareoppdateringer og nyinstallasjoner, og gjør enhetsadministrasjon tilgjengelig for brukere uavhengig av deres tekniske ekspertise. Det er avgjørende å forstå hvordan dette installasjonsprogrammet skal brukes for å opprettholde optimal enhetsytelse og unngå vanlige fallgruver som kan gjøre enhetene midlertidig ubrukelige.


### Krav til tilgang og nettleserkompatibilitet


Bitaxe Web Installer er tilgjengelig via den dedikerte URL-adressen [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) (den som ble presentert i videoen, er nå utdatert), og fungerer som det sentrale knutepunktet for alle installasjonsaktiviteter for fastvare. For å kunne bruke dette nettbaserte verktøyet må du imidlertid ha en nettleser som er kompatibel, ettersom installasjonsprogrammet er avhengig av spesifikke webteknologier som ikke støttes av alle nettlesere. Chrome er den primære nettleseren som anbefales for installasjonsprogrammet, og gir full kompatibilitet med alle funksjoner og egenskaper. Selv om andre Chromium-baserte nettlesere kan tilby lignende funksjonalitet, mangler populære alternativer som Brave og Firefox den nødvendige støtten for webserien API, noe som gjør dem inkompatible med installasjonsprogrammets kjerneoperasjoner.


Denne nettleserbegrensningen skyldes at installatøren er avhengig av direkte seriell kommunikasjon med Bitaxe-enheter via webgrensesnittet. Den serielle nettstandarden API, som muliggjør denne kommunikasjonen, er fortsatt en relativt ny nettstandard som ennå ikke er tatt i bruk av alle nettlesere. Brukere som prøver å få tilgang til installasjonsprogrammet via nettlesere som ikke støttes, vil oppleve feil i tilkoblingen og manglende evne til å kommunisere med enhetene sine, noe som gjør det nødvendig å bytte til en kompatibel nettleser før installasjonsaktivitetene kan fortsette.


### Strømkrav og klargjøring av enheten


Bitaxe-enheter har ulike strømkrav avhengig av modell og versjon, noe som gjør riktig strømstyring avgjørende for en vellykket fastvareinstallasjon. Enheter som kjører versjon 204 eller lavere, kan drives utelukkende via USB-strøm, og trekker tilstrekkelig strøm fra den tilkoblede datamaskinen til å opprettholde driften under blinkingsprosessen. Denne forenklede strømforsyningen gjør disse tidligere versjonene spesielt praktiske for fastvareoppdateringer, ettersom brukerne bare trenger å koble til én enkelt USB-kabel for å starte installasjonsprosessen.


Enheter som kjører versjon 205 og nyere krever imidlertid eksterne strømkilder i tillegg til USB-tilkoblingen, noe som gjenspeiler endringer i strømforbruk og kretsdesign i nyere maskinvareversjoner. Disse enhetene kan ikke trekke tilstrekkelig strøm via USB alene, og må derfor kobles til standard strømforsyning under installasjonen av fastvaren. Hvis disse nyere enhetene ikke får tilstrekkelig strøm, vil det føre til feil i installasjonen og mulig ødeleggelse av fastvareoppdateringsprosessen.


Den fysiske tilkoblingsprosessen krever spesifikk timing og knappemanipulering for å sikre riktig kommunikasjon mellom installasjonsprogrammet og enheten. Brukerne må trykke på og holde inne oppstartsknappen på Bitaxe-enheten før de kobler USB-C-kabelen til datamaskinen. Denne sekvensen setter enheten i oppstartsmodus, slik at installasjonsprogrammet kan kommunisere direkte med enhetens fastvarelager. Hvis USB-kabelen kobles til før oppstartsknappen trykkes inn, vil enheten fungere normalt i stedet for i bootloader-modus, som kreves for fastvareinstallasjon, og installasjonsprogrammet vil ikke kunne etablere den nødvendige kommunikasjonskanalen.


### Installasjonsalternativer og bruksområder


Bitaxe Web Installer tilbyr fire forskjellige installasjonsalternativer, hver utformet for spesifikke brukstilfeller og enhetskonfigurasjoner. Bitaxe Superboard versjon 4.0.1 representerer den nyeste fastvaren for enheter av Super-modellen, med versjon 4.0.2 planlagt for fremtidig utgivelse. Dette alternativet inkluderer både fabrikk- og oppdateringsvarianter, noe som gir fleksibilitet i installasjonsmetoden basert på brukerens behov og enhetens status.


Fabrikkinstallasjoner representerer komplette fastvareutskiftninger som speiler den opprinnelige produksjonsprosessen, inkludert omfattende selvtestprosedyrer som verifiserer enhetens funksjonalitet på tvers av alle systemer. Når brukere velger en fabrikkinstallasjon, utfører installatøren en fullstendig sletting av eksisterende fastvare og konfigurasjonsdata, og erstatter dem med en ny, ren installasjon som er identisk med den som ble brukt under produksjonen. Denne prosessen inkluderer automatisk selvtesting som validerer at maskinvaren fungerer som den skal, og krever at brukerne starter enheten på nytt før normal drift kan gjenopptas. Fabrikkinstallasjoner er spesielt verdifulle når enheter opplever vedvarende problemer, eller når brukere ønsker å tilbakestille enhetene til de opprinnelige fabrikkspesifikasjonene.


Oppdateringsinstallasjoner gir en mer konservativ tilnærming, der eksisterende konfigurasjonsdata bevares mens bare kjernekomponentene i fastvaren oppdateres. Dette alternativet er ideelt for brukere som har tilpasset enhetsinnstillingene sine og ønsker å opprettholde sine personlige konfigurasjoner samtidig som de drar nytte av forbedringer og feilrettinger i fastvaren. Oppdateringsprosessen retter seg kun mot de fastvarekomponentene som må endres, slik at brukerspesifikke innstillinger, WiFi-legitimasjon og Bitcoin-adresser forblir intakte gjennom hele installasjonsprosessen.


### Kritiske installasjonshensyn og databeskyttelse


Skillet mellom fabrikkinstallasjoner og oppdateringsinstallasjoner har betydelige konsekvenser for enhetskonfigurasjon og bevaring av brukerdata. Fabrikkinstallasjoner sletter enheten fullstendig, og fjerner alle brukerkonfigurerte innstillinger, inkludert WiFi-legitimasjon, Bitcoin-adresser og alle personlige enhetsparametere. Etter en fabrikkinstallasjon må brukerne koble seg til enhetens standard WiFi-nettverk på nytt og konfigurere alle personlige innstillinger fra bunnen av, slik at enheten behandles som om den var helt ny fra produsenten.


Oppdateringsinstallasjoner krever at man er oppmerksom på alternativet for sletting av enheten som presenteres under installasjonsprosessen. Installasjonsprogrammet vil spørre brukerne "Vil du slette enheten før du installerer Bitaxe Flasher?", og samtidig kommer det en advarsel om at alle data på enheten vil gå tapt. Brukere som utfører oppdateringsinstallasjoner, må avvise dette alternativet ved å klikke på "Neste" i stedet for å bekrefte slettingen. Hvis du godtar slettealternativet under en oppdateringsinstallasjon, fjernes enhetens konfigurasjonsfil, noe som kan føre til at enheten ikke fungerer før riktig konfigurasjon er gjenopprettet. Selv om dette ikke skader enheten permanent, skaper det unødvendige komplikasjoner og krever ytterligere konfigurasjonstrinn for å gjenopprette normal drift.


Selve installasjonsprosessen fortsetter automatisk når brukeren har gjort sine valg og bekreftet dem. Installasjonsprogrammet håndterer alle tekniske aspekter ved overføring og verifisering av fastvare, og gir fremdriftsindikatorer og statusoppdateringer gjennom hele prosessen. Denne automatiserte tilnærmingen eliminerer behovet for at brukerne må sette seg inn i komplekse prosedyrer for fastvareinstallasjon, samtidig som den sikrer pålitelige og konsistente resultater på tvers av ulike enhetsmodeller og fastvareversjoner.


## Hvordan lager og bestiller jeg kretskortet?

<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>


:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

Dette kapittelet fokuserer på den praktiske prosessen med å generere produksjonsfiler fra KiCad-prosjekter og bestille profesjonelle kretskort fra produsenter på nettet. Med Bitaxe-prosjektet som eksempel går vi gjennom hele arbeidsflyten fra filgenerering til bestilling hos en kretskortprodusent.


### Forstå produksjonsprosessen for kretskort


Veien fra en ferdig KiCad-design til et fysisk kretskort omfatter flere kritiske trinn som bygger bro mellom digital design og fysisk produksjon. Når du arbeider med komplekse prosjekter som Bitaxe, gir PCB-editoren i KiCad en omfattende oversikt over designet ditt, og viser alle komponenter og deres sammenkoblinger gjennom fargede spor. De røde og blå linjene du ser, representerer de elektriske forbindelsene mellom de ulike integrerte kretsene og komponentene på kretskortet. Med KiCads 3D-visning kan du visualisere hvordan det ferdig monterte kretskortet vil se ut, noe som gir deg verdifull innsikt i komponentplassering og potensielle mekaniske konflikter.


Produksjonsprosessen krever spesifikke filformater som kretskortprodusentene kan tolke og bruke til å produsere kortene dine. Disse filene inneholder nøyaktig informasjon om kobberlag, borehull, komponentplassering og andre produksjonsspesifikasjoner. Det er viktig å forstå denne arbeidsflyten, enten du jobber med standard Bitaxe-designet eller gjør modifikasjoner, for eksempel legger til egendefinerte logoer, endrer komponentverdier eller justerer kretskortlayouten for å oppfylle spesifikke krav.


### Generering av Gerber-filer for produksjon


Gerber-filer er bransjestandarden for kommunikasjon av PCB-designinformasjon til produsenter. Disse filene inneholder alle nødvendige data for å produsere kretskortet, inkludert kobberlagmønstre, loddemaskedefinisjoner og borehullsplasseringer. For å generate disse filene i KiCad, navigerer du til PCB-editoren og åpner fabrikasjonsutgangene via Filer-menyen. Programvaren konfigurerer automatisk de riktige innstillingene for standard produksjonsprosesser, inkludert riktig utdatakatalogstruktur som vanligvis er organisert som "manufacturing files/gerbers"


Genereringsprosessen oppretter flere Gerber-filer, som hver representerer ulike aspekter av kretskortdesignet. Disse filene fungerer sammen for å gi produsentene komplette produksjonsinstruksjoner. Når filene er generert, må de komprimeres til et ZIP-arkiv, ettersom dette er standardformatet som de fleste kretskortprodusenter forventer. ZIP-filen inneholder alle nødvendige produksjonsdata og sikrer at ingen filer går tapt eller ødelegges under opplastingsprosessen til produsentens nettsted.


Det er verdt å merke seg at mange åpen kildekode-prosjekter, inkludert Bitaxe, ofte inkluderer forhåndsgenererte produksjonsfiler i arkivene sine. Det er imidlertid avgjørende å forstå hvordan du selv kan generate disse filene når du gjør designendringer eller arbeider med ulike kortversjoner. Denne kunnskapen er spesielt verdifull når du skal tilpasse design eller feilsøke produksjonsproblemer.


### Velge PCB-produsent og forstå alternativene


Det finnes flere anerkjente alternativer innen kretskortproduksjon, og JLCPCB og PCBWay er blant de mest populære valgene for både hobby- og proffbrukere. Begge produsentene tilbyr lignende tjenester med konkurransedyktige priser og pålitelig kvalitet, selv om hver av dem har spesifikke fordeler avhengig av prosjektkravene dine. JLCPCB tiltrekker seg ofte førstegangsbrukere med kampanjepriser og brukervennlige grensesnitt, mens PCBWay kan tilby ulike materialalternativer eller spesialiserte tjenester.


Når du laster opp Gerber-filene dine til en produsents nettsted, analyserer systemet automatisk designet ditt og presenterer ulike produksjonsalternativer. Standardinnstillingene som tilbys av disse plattformene, passer vanligvis for de fleste standarddesign, og det anbefales vanligvis å beholde disse innstillingene med mindre du har spesifikke krav. Viktige parametere er blant annet kretskorttykkelse, kobbervekt, overflatefinish og minimumsantall. De fleste produsenter krever minimumsbestillinger på fem kort, noe som faktisk fungerer bra for hobbyprosjekter der det er fordelaktig å ha ekstra kort eller dele med venner.


Fargevalg er et av de få estetiske valgene som er tilgjengelige under produksjonsprosessen. Selv om grønn fortsatt er det tradisjonelle og mest kostnadseffektive alternativet, tilbyr produsentene vanligvis alternativer som blått, rødt, gult, lilla og svart. Fargevalget er rent estetisk og påvirker ikke den elektriske ytelsen til kretskortet, selv om noen farger kan ha små kostnadskonsekvenser eller lengre produksjonstid.


### Avanserte produksjonshensyn og monteringsalternativer


Utover grunnleggende kretskortproduksjon tilbyr moderne produsenter tilleggstjenester som kan effektivisere prosjektgjennomføringen betydelig. Sjablonger er en av de mest verdifulle tilleggstjenestene, spesielt for design med komponenter med fin pitch, som ASIC-brikkene som finnes i Bitcoin mining-prosjekter. En sjablong er i hovedsak en presisjonskuttet aluminiumsmal med åpninger som samsvarer nøyaktig med loddeputene på kretskortet. Dette verktøyet muliggjør konsekvent og nøyaktig påføring av loddepasta, noe som forbedrer monteringskvaliteten dramatisk og reduserer sannsynligheten for loddefeil.


Sjablongene kan være enkle sjablonger med både topp- og bunnmønster, eller separate sjablonger for hver side av platen. For de fleste prosjekter er en kombinert sjablong mer praktisk og kostnadseffektiv. Sjablontykkelsen er nøye beregnet for å avsette riktig mengde loddepasta for de spesifikke komponenttypene og pad-størrelsene. Ved hjelp av en sjablong forvandles det som kan være en kjedelig og feilutsatt manuell prosess, til et raskt og profesjonelt monteringstrinn.


Selv om noen produsenter tilbyr delvis eller fullstendig montering, må disse alternativene vurderes nøye for komplekse prosjekter som Bitaxe. Tilgjengelighet av komponenter, kostnader og den pedagogiske verdien av selvmontering er alle faktorer som spiller inn i denne beslutningen. Mange spesialkomponenter som kreves for Bitcoin mining-prosjekter, er kanskje ikke lett tilgjengelige gjennom standard PCB-monteringstjenester, noe som gjør komponentinnkjøp og manuell montering til den mest praktiske tilnærmingen. Fremtidige episoder i denne serien vil ta for seg strategier for komponentinnkjøp og monteringsteknikker som kan hjelpe deg med å fullføre Bitaxe-prosjektet ditt fra det nakne kretskortet til en funksjonell enhet.


Produksjons- og monteringsprosessen utgjør en avgjørende bro mellom digital design og fysisk implementering. Ved å forstå disse arbeidsflytene kan du ta kontroll over prosjektene dine, redusere kostnadene og få verdifull praktisk erfaring med profesjonelle produksjonsprosesser. Enten du bygger en enkelt prototyp eller planlegger en liten produksjonskjøring, vil det å beherske disse ferdighetene gi deg nye muligheter til å gi liv til dine elektroniske design.


# Optimalisering av ytelse

<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>


## Benchmark din Bitaxe

<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>


:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

Jakten på optimal mining ytelse krever en systematisk tilnærming til maskinvarekonfigurasjon som balanserer hashrate, effektivitet og termisk styring. Bitaxe har mange konfigurasjonsparametere som kan påvirke ytelsen betydelig, men det ville være upraktisk og tidkrevende å teste alle kombinasjoner av innstillinger manuelt. Dette kapittelet tar for seg hvordan du kan bruke automatiserte referanseverktøy til å optimalisere Bitaxe-ens ytelse på en vitenskapelig måte, samtidig som du opprettholder trygge driftsforhold.


### Forståelse av Bitaxes ytelsesmålinger og basiskonfigurasjon


Før vi går nærmere inn på optimaliseringsteknikker, er det viktig å forstå de viktigste ytelsesindikatorene som definerer Bitaxes driftseffektivitet. De viktigste indikatorene inkluderer hashrate målt i terahash per sekund, strømeffektivitet uttrykt i joule per terahash, ASIC-frekvens i megahertz og kjernespenning i volt. En godt konfigurert Bitaxe kan oppnå omtrent 1,1 terahash med en virkningsgrad på rundt 17 joule per terahash, med en frekvens på 550 megahertz og en målt ASIC-spenning på 1,14 volt. Disse referansetallene gir et referansepunkt for å forstå de potensielle forbedringene som er tilgjengelige gjennom systematisk optimalisering.


Forholdet mellom disse parameterne er komplekst og gjensidig avhengig av hverandre. Høyere frekvenser øker vanligvis hashrate, men øker også strømforbruket og varmeutviklingen. På samme måte påvirker spenningsjusteringer både ytelse og termiske egenskaper. Utfordringen ligger i å finne den optimale balansen som maksimerer enten hashrate eller effektiviteten, samtidig som man opprettholder stabil drift innenfor trygge temperaturgrenser. Denne optimaliseringsprosessen krever metodisk testing av flere parameterkombinasjoner, noe som gjør automatiserte verktøy uvurderlige for å oppnå optimale resultater.


### Bitaxe Hashrate Benchmark-verktøyets arkitektur


Verktøyet [Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) er en sofistikert Python-basert løsning som opprinnelig ble utviklet av WhiteCookie og senere forbedret av mrv777. Dette open source-verktøyet, som distribueres under GPLv3-lisensen, automatiserer den komplekse prosessen med å teste flere konfigurasjonskombinasjoner for å identifisere optimale innstillinger for din spesifikke maskinvare. Verktøyets primære styrke ligger i den systematiske tilnærmingen til parametertesting, med trinnvis justering av frekvens- og spenningsinnstillinger samtidig som ytelsesmålinger og termiske forhold overvåkes kontinuerlig.


Benchmarking-prosessen tar vanligvis 30 til 40 minutter å fullføre, der verktøyet metodisk tester ulike kombinasjoner av ASIC-frekvens- og spenningsinnstillinger. Verktøyet begynner med konservative grunninnstillinger, som vanligvis starter på 1,15 volt og 500 megahertz, og øker deretter disse parameterne trinnvis mens hashrate, temperatur og stabilitet overvåkes. Verktøyet prioriterer sikker drift fremfor maksimal ytelse, og reduserer automatisk innstillinger som fører til for høy varmeutvikling eller ustabilitet. Denne konservative tilnærmingen sikrer at optimaliseringsprosessen ikke går på bekostning av maskinvarens levetid eller pålitelighet.


### Krav til installasjon og oppsett


Implementering av Bitaxe Hashrate Benchmark-verktøyet krever flere nødvendige programvarekomponenter på den lokale datamaskinen. De viktigste kravene er Python for kjøring av benchmarking-skript, Git for administrasjon av repository og eventuelt Visual Studio Code for forbedrede funksjoner i utviklingsmiljøet. Selv om verktøyet kan betjenes fra kommandolinjegrensesnitt, gir et integrert utviklingsmiljø som VS Code bedre innsyn i referanseprosessen og resultatanalysen.


Installasjonsprosessen følger standard Python-utviklingspraksis, og begynner med å klone depotet fra GitHub til din lokale maskin. Når depotet er lastet ned, må du opprette et virtuelt miljø for å isolere verktøyets avhengigheter fra systemets Python-installasjon. Denne isoleringen forhindrer potensielle konflikter med andre Python-applikasjoner og sikrer konsekvent drift. Etter at du har aktivert det virtuelle miljøet, installerer du de nødvendige avhengighetene ved hjelp av den medfølgende kravfilen, som automatisk konfigurerer alle nødvendige biblioteker og moduler for at verktøyet skal fungere korrekt.


### Utføre referanseverdier og tolke resultater


For å kjøre referanseindeksen må du utføre en enkelt Python-kommando som inkluderer IP-adressen til din Bitaxe som parameter. Verktøyet kobler seg automatisk til gruvearbeiderens nettgrensesnitt og starter den systematiske testprosessen. Under kjøringen gir verktøyet detaljert logginformasjon som viser gjeldende testiterasjon, spennings- og frekvensinnstillinger, resulterende hashrate, inngangsspenning, temperaturavlesninger og termiske data fra kritiske komponenter som buck-omformeren. Denne tilbakemeldingen i sanntid gjør at du kan overvåke fremdriften i benchmarkingen og forstå hvordan ulike innstillinger påvirker ytelsen til gruvearbeideren din.


Verktøyets intelligente varmestyring blir tydelig når temperaturen nærmer seg sikkerhetsgrensen på 66 grader Celsius. I stedet for å presse ut over sikre driftsgrenser, reduserer referanseindeksen automatisk innstillingene for å opprettholde termisk stabilitet. Denne konservative tilnærmingen sikrer at optimaliseringsprosessen prioriterer langsiktig maskinvarepålitelighet fremfor kortsiktige ytelsesgevinster. Verktøyet genererer omfattende resultater i JSON-format, og rangerer de fem beste konfigurasjonene for både maksimal hashrate og optimal effektivitet. Disse resultatene gir klar veiledning for valg av den konfigurasjonen som best samsvarer med dine driftsprioriteringer, enten du fokuserer på maksimal effekt eller energieffektivitet.


Benchmarking-verktøyet tilbyr også tilpasningsalternativer for avanserte brukere som ønsker å endre testparametrene. Med kommandolinjeargumenter kan du angi egendefinerte startspenninger og -frekvenser, noe som muliggjør mer målrettet optimalisering for spesifikke bruksområder. Hvis du for eksempel allerede vet at maskinvaren din presterer godt ved høyere frekvenser, kan du starte referanseindeksen med høyere innstillinger i stedet for å begynne med de konservative standardinnstillingene. Denne fleksibiliteten gjør verktøyet verdifullt både for nybegynnere som ønsker automatisert optimalisering, og for erfarne utvinnere som vil finjustere spesifikke ytelsesegenskaper.


## Overklokk din Bitaxe

<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>


:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

Overklokking av en Bitaxe-enhet krever nøye vurdering av både maskinvarebegrensninger og kjølebehov. Selv om mange brukere foretrekker å underklokke enhetene sine for å få en mer stillegående drift, er det viktig å forstå riktige overklokkingsteknikker for de som ønsker maksimal ytelse uten å skade maskinvaren. Prosessen innebærer å øke frekvensen og eventuelt justere spenningsinnstillingene utover fabrikkspesifikasjonene, noe som i seg selv øker varmeutviklingen og belastningen på komponentene.


Grunnlaget for vellykket overklokking ligger i tilstrekkelig kjøleinfrastruktur. Før du prøver deg på frekvensendringer, må du sørge for at din Bitaxe har riktig varmespredning. En Bitaxe Gamma med en kjøleribbe og vifte av høy kvalitet gir den nødvendige termiske styringen for sikker overklokking. Enheter med små kjøleribber og utilstrekkelige vifter bør ikke overklokkes, da dårlig kjøling vil føre til termisk struping og potensiell skade på maskinvaren. Det er viktig å forstå forholdet mellom varme og komponentenes levetid - for mye varme skaper stress som forringer elektroniske komponenter over tid, noe som reduserer levetiden til enheten betydelig.


### Strategisk plassering av kjøleribben


Den mest kritiske komponenten som krever ekstra kjøling, er buck-konverteren, en liten svart komponent som er plassert på baksiden av Bitaxe i nærheten av den store spolen. Denne enheten konverterer den innkommende 5 V-strømforsyningen ned til riktig spenning for ASIC-brikken, vanligvis rundt 1,2 V. Buck-omformeren, ofte kalt TPS, genererer betydelig varme under drift og representerer en termisk flaskehals som begrenser overklokkingspotensialet. Ved å montere en liten selvklebende kjøleribbe på denne komponenten kan man ikke bare oppnå høyere overklokkingskapasitet, men også forbedre den generelle effektiviteten ved å redusere varmetapet.


Ytterligere plassering av kjøleribber kan være til fordel for andre områder på kortet med høy strømstyrke. Spenningsreguleringskretsene utsettes for betydelig elektrisk stress når strømmen strømmer fra inngangsseksjonen og ned gjennom ulike kortbaner for å forsyne ASIC-brikken. Mange erfarne overklokkere installerer kjøleribber på forsiden av Bitaxe i disse strømkrevende områdene for å forbedre varmespredningen ytterligere. Selv om det ikke er strengt tatt nødvendig for moderat overklokking, blir disse ekstra kjøletiltakene viktige når man presser frekvensene til ekstreme nivåer.


### Vurderinger og begrensninger for kjølesystemet


ESP32-kontrolleren, som er synlig som den sølvfargede komponenten på kortet, trenger vanligvis ikke ekstra kjøling. Denne komponenten genererer minimalt med varme på egen hånd og blir bare varm på grunn av varmeoverføring fra omkringliggende komponenter. Installering av kjøleribber i nærheten av ESP32 kan potensielt forstyrre den tilstøtende Wi-Fi-antennen, noe som kan forringe den trådløse tilkoblingen og signalkvaliteten. Fokuser kjøleinnsatsen på strømreguleringskomponentene og ASIC-området i stedet for på kontrollkretsene.


Konfigurasjoner med to vifter gir både muligheter og begrensninger. Selv om det å legge til en ekstra vifte for å blåse luft over baksiden av Bitaxe kan forbedre kjøleytelsen, kan enhetens fastvare bare kontrollere én vifte på riktig måte. Bitaxe har to viftehoder, men bare én viftekontroller, noe som betyr at hvis du kobler til to vifter, vil fastvaren bli forvirret når den mottar motstridende RPM-signaler. Denne konfigurasjonen vil fungere, men kan resultere i uforutsigbar viftestyring.


### Grunnleggende ytelsesvurdering


Før du prøver å overklokke, må du etablere en grunnleggende ytelsesmåling ved å kjøre Bitaxe med standardinnstillinger i flere timer. Overvåk ASIC-temperaturen, spenningsregulatorens temperatur og viftehastigheten i prosent via nettgrensesnittet. Optimale driftstemperaturer bør holde ASIC under 60 °C og spenningsregulatoren under 60 °C under normale forhold. Hvis enheten din allerede opererer med temperaturer over 65 °C på ASIC eller 70-80 °C på spenningsregulatoren ved standardinnstillinger, er det nødvendig med ekstra kjøleutstyr før du fortsetter med overklokking.


Den systematiske tilnærmingen til frekvensøkninger innebærer trinnvise økninger ved hjelp av de forhåndsdefinerte frekvensalternativene i innstillingsmenyen. Begynn med å velge det neste tilgjengelige frekvenstrinnet over den gjeldende innstillingen, samtidig som du beholder standard kjernespenning. Denne konservative tilnærmingen gjør at du kan evaluere konsekvensene for varme og stabilitet før du gjør ytterligere endringer. La enheten kjøre med hver nye frekvensinnstilling i minst 30 minutter til én time, og følg med på temperaturutviklingen og stabiliteten i hashfrekvensen gjennom hele evalueringsperioden.


### Avansert tilpasset konfigurasjon


For å få tilgang til tilpassede frekvens- og spenningsinnstillinger må du aktivere det avanserte overklokkingsgrensesnittet ved å legge til "?OC" i URL-adressen til enhetens nettgrensesnitt. Dette låser opp manuelle inndatafelt for presis frekvens- og spenningskontroll, ledsaget av passende advarsler om risikoen ved å operere utenfor de angitte parameterne. Det tilpassede grensesnittet muliggjør finjustering utover standard frekvenstrinn, slik at erfarne brukere kan optimalisere ytelsen for sine spesifikke kjølekonfigurasjoner.


Når du bruker egendefinerte innstillinger, bør du holde deg til konservative trinnstørrelser på 10-15 MHz per justeringstrinn. Denne metodiske tilnærmingen forhindrer plutselige termiske spisser og gjør det mulig å teste stabiliteten på hvert frekvensnivå. Noen avanserte brukere oppnår frekvenser på rundt 700 MHz med kjernespenninger justert til 1,175 V eller lignende verdier, men disse ekstreme innstillingene krever omfattende kjølemodifikasjoner og nøye overvåking. Spenningsregulatoren kan operere ved temperaturer på opptil 100 °C uten umiddelbar skade, men høyere temperaturer reduserer effektiviteten og påliteligheten på lang sikt. Vellykket overklokking krever tålmodighet, systematisk testing og kontinuerlig overvåking for å oppnå stabile ytelsesforbedringer samtidig som maskinvareintegriteten bevares.


# Siste del

<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>


## Evaluer dette kurset

<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>

<isCourseReview>true</isCourseReview>

## Konklusjon

<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>

<isCourseConclusion>true</isCourseConclusion>