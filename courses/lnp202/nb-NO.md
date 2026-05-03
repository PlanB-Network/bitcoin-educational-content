---
name: Sette opp din første Lightning-node
goal: Forstå, installere, konfigurere og bruke en Lightning-node
objectives: 


  - Forstå rollen til og formålet med en Lightning-node.
  - Identifisere de ulike programvareløsningene som er tilgjengelige.
  - Installer og konfigurer en Lightning-node (LND).
  - Koble til en utgiftskonto.
  - Kjenn til risikoen ved å bruke en Lightning-node.


---

# Ditt første skritt mot selvstendighet på Lightning



Du har allerede anskaffet din første sats, sikret deg midler til selvforvaring og utplassert en Bitcoin-node for å være suveren i on-chain-bruken din. Det neste trinnet er å oppnå den samme autonomien på Lightning: det er nettopp det som er målet med dette kurset.



LNP202 er rettet mot viderekomne brukere, og veileder deg trinn for trinn gjennom installasjonen av din første Lightning-node, uten avanserte tekniske ferdigheter.



Du lærer hvordan du installerer LND på Umbrel, åpner og administrerer kanalene dine, overvåker noden din og kobler til en mobil wallet, slik at du kan nyte en opplevelse som kan sammenlignes med en depotbasert wallet, samtidig som du beholder full kontroll over midlene dine.



+++


# Innledning


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Kursoversikt


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



LNP202 er et praktisk kurs som er utviklet for å gjøre deg autonom på Lightning ved å drifte din egen node. Målet er enkelt: start med en Bitcoin-node som allerede er på plass, installer LND på Umbrel, sikre den ordentlig, åpne og administrer de første kanalene dine, og bruk deretter noden din på daglig basis fra en mobil wallet. Dette kurset forutsetter at du allerede har tatt BTC 202, ettersom jeg antar at Bitcoin-noden din på Umbrel er på plass og synkronisert. Vi går ikke tilbake til hvordan du setter opp en Bitcoin-node her.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

For en bedre forståelse av Lightnings interne mekanikk anbefales også kurset LNP 201, selv om det ikke er en forutsetning for dette kurset:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

I den første delen av dette LNP202-kurset tar vi en titt på hva en Lightning-node egentlig er, hvordan den skiller seg fra en enkel wallet, og hvorfor det å drive en personlig node er den eneste måten å bruke Lightning på uten å delegere sats til en betrodd tredjepart. Denne delen avsluttes med et strategisk valg: hvilken løsning som passer for deg, fra de enkleste tilnærmingene til den klassiske Lightning-noden, som er den vi skal implementere i dette kurset.



I del 2 av kurset installerer du LND på Umbrel, og deretter får du på plass elementene som forhindrer de mest kostbare feilene: en realistisk backup-strategi og beskyttelse mot juks via et vakttårn. Når disse grunnleggende elementene er på plass, åpner du din første kanal, slik at du kan begynne å betale på Lightning med din egen infrastruktur.



I dette LNP202-kurset skal vi sette opp en Lightning-node i plug-and-play-modus via Umbrel, i stedet for den klassiske kommandolinjetilnærmingen, for å gjøre det egnet for viderekomne brukere. Hvis du foretrekker en kommandolinjeinstallasjon, anbefaler jeg at du følger veiledningen nedenfor. Andre, mer avanserte, kommandolinjeorienterte Lightning-kurs er også under utarbeidelse.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Del 3 tar deg fra en node som fungerer, til en node som du vet hvordan du skal kontrollere. Du starter med å bestemme Lightning-nodeoperatørprofilen din (forbruker, forhandler eller ruter), og deretter tar du i bruk en komplett administrasjonsprogramvarepakke for å spore kanalene dine og handle rent på topologien din. Til slutt tar du for deg et svært viktig Lightning-punkt: hvordan du skaffer inngående likviditet, enten det er via betalte eller kooperative løsninger.



Del 4 vil fokusere på hverdagsbruk. Du skal sette opp en forbindelse mellom noden din og en mobilkunde, slik at du kan betale og hente penger enkelt fra smarttelefonen din, uten å gi fra deg selvforvaringen. Vi ser først på en nettverkstilnærming via *Tailscale*, deretter på en protokolltilnærming via *Nostr Wallet Connect*, med deres respektive fordeler og kompromisser. Kurset avsluttes med et siste kapittel som vil gi deg de rette vanene for å opprettholde din egen forvaring, både operasjonelt og pedagogisk.



Hvis du følger dette LNP202-kurset i riktig rekkefølge, vil du ved slutten av kurset ha en komplett konfigurasjon for Lightning-noden din, funksjonell for daglig bruk og, fremfor alt, under kontroll.




## Forståelse av Lightning-noder


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Før du lanserer din egen node, vil dette kapittelet gi en kort gjennomgang av den grunnleggende teorien bak [Lightning Network](https://planb.academy/resources/glossary/lightning-network). Det er viktig å forstå mekanismene som ligger bak, slik at du kan identifisere risikoer og ta i bruk gode fremgangsmåter for å begrense dem. Jeg vil imidlertid ikke gå i detalj her, siden dette ikke er hovedmålet med dette kurset. Hvis du ønsker å gå dypere inn i emnet, anbefaler jeg på det sterkeste at du leser Fanis Michalakis' LNP 201-kurs, som er en referanse på området:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Hva er en Lightning-node?



La oss gå tilbake til det grunnleggende: Før vi definerer hva en node er, må vi forstå hva Lightning Network er. Det er en topplagsprotokoll, bygget på toppen av Bitcoin, designet for å muliggjøre BTC-transaksjoner utenfor kjeden som er raske (med nesten øyeblikkelig finalitet) og generelt billige. "[Offchain](https://planb.academy/resources/glossary/offchain)" betyr at transaksjoner som utføres på Lightning, ikke er ment å vises på den viktigste [Bitcoin-blokkjeden](https://planb.academy/resources/glossary/blockchain). Lightning er også et delvis svar på den økende bruken av Bitcoin og på overbelastning [i kjeden](https://planb.academy/resources/glossary/onchain), noe som gir grunn til bekymring for systemets [skalerbarhet](https://planb.academy/resources/glossary/scalability).



For å fungere er Lightning avhengig av at det åpnes [betalingskanaler](https://planb.academy/resources/glossary/payment-channel) mellom deltakerne, der transaksjoner kan utføres nesten umiddelbart, ofte med minimale gebyrer, uten at det er nødvendig å registrere dem én etter én på Bitcoin-blokkjeden. Disse kanalene kan forbli åpne i svært lang tid, og krever kun transaksjoner i kjeden når de åpnes og lukkes.



En [Lightning-node](https://planb.academy/resources/glossary/lightning-node) er en deltaker i Lightning-nettverket, som åpner kanaler og utfører betalinger med andre noder. Konkret er en Lightning-node en programvare som kjører på en datamaskin og implementerer Lightning Network-protokollen. Eksempler på dette er LND, Core Lightning eller Eclair. Hovedoppgaven til denne programvaren er å




- koble seg til en [Bitcoin-node](https://planb.academy/resources/glossary/full-node) for å innhente informasjon fra hovedblokkjeden;
- opprette og administrere toveis betalingskanaler med andre noder;
- utveksle meldinger med hele Lightning-nettverket.



![Image](assets/fr/001.webp)



### Node vs. Lightning Wallet: en viktig forskjell



På Bitcoin (onchain) refererer "*[wallet](https://planb.academy/resources/glossary/wallet)*" til programvare som administrerer dine [private nøkler](https://planb.academy/resources/glossary/private-key), beregner saldoen din fra dine [UTXO](https://planb.academy/resources/glossary/utxo)-er og bygger transaksjonene dine. Denne wallet kan være basert på din egen Bitcoin-node eller på en annens, men i dag er nodens rolle og rollen til wallet i kjeden klart adskilt.



På Lightning er det vanskeligere å gjenbruke denne typen vokabular uten å skape forvirring. Begrepet "*Lightning wallet*" er ganske vagt, fordi det i realiteten ikke finnes noe slikt som en virkelig selvforvaltende Lightning wallet, med mindre den er basert på en node. Bare to situasjoner er derfor mulige:



- For å ha en ekte Lightning-node (dvs. ikke-frihetsberøvende): programvaren du bruker (f.eks. en mobilapp som Phoenix eller en LND-instans på Umbrel) kjører faktisk en node, og du har faktisk nøklene til å hente ut bitcoinsene dine. I dette tilfellet er "*Lightning wallet*" egentlig bare et brukergrensesnitt på toppen av en Lightning-node, enten den er innebygd eller ekstern.



- Slik bruker du en depottjeneste: Du bruker en applikasjon som viser deg en saldo i [sats](https://planb.academy/resources/glossary/satoshi-sat) på Lightning, men i bakgrunnen befinner midlene seg på en leverandørs node (f.eks. Wallet of Satoshi). Du har verken nøkler eller kontroll over kanalene. Saldoen din er bare en regnskapspost i selskapets database. Det kan sammenlignes med å la bitcoinsene dine ligge på en vekslingsplattform, med alle de tilhørende risikoene. I dette tilfellet er din "*Lightning wallet*" bare en tilgang til en konto som administreres av en operatør, som i sin tur driver en ekte Lightning-node.



Det finnes altså ingen mellomting når det gjelder Lightning: Enten har du en node (selv en innebygd en), og da er du selvforvalter, eller så har du det ikke, og da er det et selskap som eier din sats. Men som vi skal se i de neste kapitlene, kan det noen ganger være vanskelig å skille mellom disse to bruksområdene. Phoenix er for eksempel en mobilapplikasjon som inneholder en ekte Lightning-node, men brukeren er ikke nødvendigvis klar over det, ettersom den fulle kompleksiteten i driften er nesten helt skjult.



### En påminnelse om hvordan Lightning Network fungerer



I denne delen vil jeg gi deg en rask påminnelse om hvordan Lightning fungerer. Hvis du ønsker en mer grundig presentasjon av de teoretiske konseptene, vil jeg igjen oppfordre deg til å ta en titt på det dedikerte LNP 201-kurset.



#### Betalingskanaler: åpne, oppdatere og lukke



Hjertet i Lightning-nettverket er basert på toveis betalingskanaler. En kanal kan åpnes (dvs. opprettes), oppdateres etter hvert som Lightning-transaksjoner finner sted, og til slutt lukkes. Fra kjedens synspunkt er en kanal ikke noe annet enn en 2/2 [multisignaturutgang](https://planb.academy/resources/glossary/output).



![Image](assets/fr/002.webp)



Fra Lightnings synspunkt er det en betalingskanal med [likviditet](https://planb.academy/resources/glossary/liquidity-lightning) delt mellom de to deltakerne.



![Image](assets/fr/003.webp)





- Åpne en kanal:**



To noder bestemmer seg for å åpne en kanal. En av dem forplikter bitcoins i en transaksjon i kjeden som kalles *finansieringstransaksjon*. Denne transaksjonen skaper en utgang basert på et 2-av-2 [multisignaturskript](https://planb.academy/resources/glossary/script), noe som betyr at bruk av disse midlene på Bitcoin krever [signatur](https://planb.academy/resources/glossary/digital-signature) fra begge nodene i kanalen. Før denne transaksjonen utstedes, ber den parten som gir pengene, den andre parten om å signere en *uttakstransaksjon*, som ikke utstedes i kjeden, men som gjør det mulig å få tilbake pengene hvis det skulle oppstå et problem.



![Image](assets/fr/004.webp)





- Commitment transaksjoner:**



Kanalens tilstand (dvs. fordelingen av sats mellom A og B) representeres av en *[commitment transaction](https://planb.academy/resources/glossary/commitment-transaction)*, som er kjent for begge nodene, men som ikke umiddelbart kringkastes på blokkjeden. Denne transaksjonen beskriver hvordan kanalens midler skal omfordeles i kjeden i henhold til betalingene som er gjort på Lightning.



Ved hver lynbetaling signerer de to nodene en ny tilstand som erstatter den forrige. Den gamle tilstanden tilbakekalles takket være en tilbakekallingsnøkkelmekanisme: Hvis en av deltakerne prøver å kringkaste en gammel tilstand, kan den andre gjenopprette hele beløpet som en straff.



Den viktige ideen her er at det alltid finnes en signert Bitcoin-transaksjon, som ikke kringkastes i kjeden, og som nodene oppbevarer, og som gjør det mulig å omfordele hverandres sats i henhold til betalingene som er gjort på Lightning Network.



![Image](assets/fr/005.webp)





- Nedleggelse av kanaler:**



En kanal kan lukkes på en ren måte via en kooperativ lukking, når begge parter er enige om kanalens endelige tilstand, eller unilateralt (en tvungen lukking) hvis en av deltakerne slutter å samarbeide eller blir utilgjengelig. I alle tilfeller skjer stengingen i form av en transaksjon i kjeden som bruker 2/2-utgangen og fordeler midlene mellom deltakerne i henhold til kanalens siste gyldige tilstand.



![Image](assets/fr/006.webp)



Lightning fungerer dermed som et sekundært lag forankret på Bitcoin: Bare visse hendelser (åpning og lukking av kanaler) vises på hovedblokkjeden. Mellomliggende betalinger forblir utenfor kjeden.



Før vi går videre, vil vi ta for oss to viktige begreper for å forstå hvordan man administrerer en Lightning-kanal:




- Liquidity*: mengden sats som er tilgjengelig på den ene siden av kanalen;
- [Kapasiteten](https://planb.academy/resources/glossary/lightning-channel-capacity)*: Det er det totale beløpet som er låst i 2/2 multisig-utgangen, dvs. summen av likviditeten på begge sider av kanalen.



#### Et nettverk av kanaler og likviditet



En kanal er ikke bare for betalinger mellom to noder: Den er en del av et globalt nettverk av sammenkoblede kanaler. Noden din kan rute betalinger for andre brukere gjennom sine egne kanaler, og du kan sende sats til en Lightning-node som du ikke har noen direkte kanal med, så lenge det finnes en gyldig sti mellom de to nodene.



Hver node kjenner, via [sladreprotokollen](https://planb.academy/resources/glossary/gossip), et kart over dette nettverket: hvilke kanaler som finnes, hvilke noder som er forbundet med en toveis kanal, og hvilke kapasiteter som er publisert. For å sende en betaling til en mottaker uten en direkte kanal beregner noden din en rute som består av flere hopp: noden din → node X → node Y → mottakernode. Ved hvert hopp går betalingen gjennom en kanal som må ha tilstrekkelig likviditet i betalingsretningen.



![Image](assets/fr/007.webp)



Likviditeten i en kanal er derfor ikke symmetrisk: Den ene siden kan være tungt belastet, mens den andre er nesten tom. Å håndtere denne likviditeten, det vil si å vite hvor sats befinner seg og i hvilken retning de kan strømme, er et av de viktigste aspektene ved driften av en Lightning-node. Vi skal se nærmere på dette i de praktiske kapitlene som kommer.



#### HTLC: Transport av betaling uten å bli ranet



For at betalinger skal kunne gå gjennom mellomliggende noder uten behov for tillit, bruker Lightning [smartkontrakter](https://planb.academy/resources/glossary/smart-contract) kalt *[HTLC](https://planb.academy/resources/glossary/htlc)* (*Hashed Time-Locked Contracts*). Enkelt forklart gjør en HTLC overføring av penger betinget av at en hemmelighet avsløres, og inneholder en tidsbegrensning for å beskytte avsenderen i tilfelle transaksjonen mislykkes. Hver betaling er derfor betinget av at det presenteres et forhåndsbilde (en hemmelighet hvis [hash](https://planb.academy/resources/glossary/hash-function)-kode tilsvarer en avtalt verdi). Hvis den endelige mottakeren oppgir dette forhåndsbildet, kan han eller hun gjøre krav på pengene, noe som i sin tur gjør det mulig for hver mellomliggende node å få tilbake sine egne midler.



![Image](assets/fr/008.webp)



Jeg skal spare deg for de tekniske detaljene om hvordan HTLC fungerer, da de ikke er avgjørende for dette kurset. Du finner en grundig forklaring i teorikurset LNP 201. Bare husk at HTLC muliggjør atomutvekslinger: Enten fullføres overføringen, og ingen blir skadet i rutingen, eller så mislykkes den, og hver deltaker får tilbake sine opprinnelige midler. Det finnes ingen mellomting.



### De viktigste Lightning node-implementeringene



I likhet med Bitcoin finnes det flere implementeringer av Lightning-protokollen. En rekke uavhengige team utvikler sine egne versjoner, som alle er interoperable siden de følger de samme spesifikasjonene ([BOLT](https://planb.academy/resources/glossary/bolt)-ene). Her er de viktigste implementeringene som er i bruk i dag.



#### LND (*Lightning Network Daemon*)



LND er en komplett implementering av Lightning-protokollen, skrevet i Go og utviklet av Lightning Labs.



![Image](assets/fr/009.webp)



#### Core Lightning (*CLN*)



Core Lightning (tidligere *C-Lightning*) er implementasjonen som er utviklet av Blockstream. Den er skrevet i C, med noen komponenter i Rust.



![Image](assets/fr/010.webp)



#### Eclair



Eclair er en implementering skrevet i Scala og utviklet av det franske selskapet ACINQ. ACINQ drifter en av de viktigste rutingknutepunktene i Lightning-nettverket med Eclair, og bruker denne implementasjonen som programvaregrunnlag for sine egne produkter, for eksempel applikasjonen Phoenix.



![Image](assets/fr/011.webp)



#### LDK (*Lightning Development Kit*)



LDK (*Lightning Development Kit*) er et Rust-utviklingssett som vedlikeholdes av Spiral (Block, tidligere Square). Det er ikke en ferdig daemon som LND eller CLN, men et bibliotek for utviklere som ønsker å integrere Lightning direkte i applikasjonene sine.



![Image](assets/fr/012.webp)



I dette LNP202-kurset konsentrerer vi oss hovedsakelig om LND: den implementasjonen som oftest brukes i nøkkelferdige løsninger for privatkunder, som Umbrel.



Det var denne korte påminnelsen om hvordan Lightning fungerer. Nok en gang, hvis det er noen konsepter du ikke forstår, eller hvis du ønsker å gå litt dypere inn i dem før du tar dem i bruk i praksis, er Fanis Michalakis' kurs den uunnværlige referansen om emnet:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Hvorfor drive din egen Lightning-node?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



Det er ganske enkelt å svare på dette spørsmålet, siden det er retorisk: Uten din egen node bruker du ikke lenger Lightning, men bare illusjonen av Lightning på tvers av selskapets infrastruktur.



Å bruke en Lightning custodial wallet betyr at bitcoinsene teknisk sett tilhører selskapet som driver noden. Du har ikke de private nøklene, og du kontrollerer ikke kanalene. wallet-saldoen din er bare en linje i tjenesteleverandørens database. Denne situasjonen er sikkert veldig praktisk for nybegynnere, og brukeropplevelsen er ofte flytende, men det grunnleggende spørsmålet er: Hva er fordelen med å bruke Bitcoin og Lightning hvis du ender opp med å gi avkall på nettopp de aspektene som skiller dem fra tradisjonelle valutaer og banker?



Bitcoins to viktigste verdiforslag er monetær suverenitet (ikke lenger avhengig av en sentral myndighet for utstedelse og oppbevaring) og sensurmotstand (umulighet for en tredjepart å forhindre eller filtrere betalinger). Et depotsystem på Lightning går direkte imot begge disse målene: Du kan ikke sjekke plattformens interne pengemengde, og per definisjon kan en operatør som har alle midlene og alle kanalene, sensurere, forsinke, prioritere eller blokkere betalingene dine. Under disse forholdene kan vi med rette spørre oss selv: **Hva er poenget med å bruke bitcoin via Lightning hvis det kommer til å reprodusere de samme mønstrene av tillit og avhengighet som med tradisjonelle statlige valutasystemer**?



> Det som trengs, er et elektronisk betalingssystem basert på kryptografiske bevis i stedet for tillit, slik at to villige parter kan handle direkte med hverandre uten behov for en betrodd tredjepart.
*Satoshi Nakamoto, Bitcoin Hvitbok


Bortsett fra filosofien, er de mer konkrete ulempene for deg som følger. For det første har du ingen mulighet til å verifisere at selskapet faktisk har de bitcoinsene som tilsvarer saldoen som vises. Det kan operere med fraksjonell reserve, bli hacket, gå konkurs eller rett og slett forsvinne. I dette tilfellet er du bare nok en kreditor, uten noen reell garanti for at du får pengene dine tilbake.



For det andre er selskapet utsatt for regulatorisk risiko: pålegg, frysing av midler, forespørsler om å blokkere brukere eller transaksjoner, forsterket overvåking eller til og med direkte forbud mot aktivitet i visse jurisdiksjoner. Alle begrensninger som hviler på tjenesteleverandøren, reflekteres mekanisk over på deg.



Når det gjelder konfidensialitet, er situasjonen ikke bedre. En depotoperatør ser alle strømmene dine: beløp, frekvenser, mottakere, saldoer, forbruksvaner. Kombinert med informasjon fra applikasjonen og eventuelt den underliggende kjedeanalysen på Bitcoin, kan denne informasjonen gi en svært presis profil av den økonomiske aktiviteten din. Igjen, det er langt fra Bitcoins mål om å redusere den økonomiske overvåkingen.



Den gode nyheten er at det i dag ikke lenger er forbeholdt tekniske eksperter å drive sin egen Lightning-node, slik det kanskje var på slutten av 2010-tallet. Det finnes relativt enkle løsninger for hjemmebrukere, som vi skal forklare i detalj i neste kapittel.




## Velge riktig løsning for jobben


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



I dag er det mulig å ha en brukeropplevelse som ligger svært nær den til en wallet med Lightning-depot, samtidig som man er i egen varetekt. Målet med dette kapittelet er å hjelpe deg med å velge den veien som passer best til din profil.



### Alternativ 1: Ikke bruk Lightning direkte



Den første løsningen er rett og slett ikke å bruke Lightning nativt, men å bruke en Bitcoin eller [Liquid](https://planb.academy/resources/glossary/liquid-network) wallet som bygger inn [atomic swaps](https://planb.academy/resources/glossary/atomic-swap). Aqua- eller BULL Wallet-applikasjoner bruker for eksempel denne metoden, ved å gjøre det mulig å betale [Lightning-fakturaer](https://planb.academy/resources/glossary/invoice-lightning) uten å drifte en Lightning-node selv, samtidig som de forblir i eget depot.



Prinsippet er enkelt: Pengene dine forblir i Bitcoin, enten on-chain eller Liquid, og du får tilgang til dem via en wallet der du holder nøklene på tradisjonell måte. Når du skanner en Lightning-faktura, initierer wallet en transaksjon (on-chain eller Liquid) til en atomic swap-tjeneste. Denne tjenesten administrerer deretter Lightning-betalingen gjennom sin egen node, ved hjelp av bitcoinsene du har gitt on-chain eller via Liquid. Dermed trenger du ikke å håndtere noen Lightning-kanaler selv, men du kan likevel gjøre opp Lightning-fakturaer sømløst.



![Image](assets/fr/013.webp)



Den største fordelen med denne tilnærmingen, sammenlignet med en konvensjonell Lightning-depot wallet, er at du til enhver tid har 100 % kontroll over midlene dine. Bitcoinsene er i din onchain eller Liquid wallet, med din egen [mnemoniske frase](https://planb.academy/resources/glossary/seed). Selv under byttet forblir du i besittelse av midlene dine, fordi byttet er atomisk. Den er avhengig av en kryptografisk mekanisme som sikrer at det bare er to mulige utfall: enten lykkes byttet helt, eller så mislykkes det, og tjenesten kan ikke tilegne seg pengene dine.



De fleste porteføljer som tilbyr denne typen funksjonalitet, er avhengige av [Boltz](https://boltz.exchange/) for den tekniske delen av byttehandelen.



Denne løsningen gir også interessante fordeler når det gjelder konfidensialitet, spesielt når den kombineres med Liquid. For en nybegynner er det også veldig enkelt å sette opp og lagre: en klassisk huskeregel, ingen kanaler, ingen likviditet å balansere...



På den annen side har denne tilnærmingen sine begrensninger. For det første er den ikke uforanderlig: Du er avhengig av byttetjenestens tilgjengelighet og velvilje. Hvis den ikke lenger ønsker å behandle kontoen din, eller opphører å fungere, kan du ikke lenger betale lynfakturaer gjennom den. I tillegg kommer de ikke ubetydelige gebyrene: Du betaler både [transaksjonsgebyrene](https://planb.academy/resources/glossary/transaction-fees) i kjeden eller Liquid og swap-tjenestens provisjon. Hvis onchain-gebyrene stiger kraftig, kan det dessuten bli svært dyrt å bruke Lightning.



Så for sporadisk bruk er det fortsatt akseptabelt, men for en svært aktiv Lightning-bruker er det bedre å gjøre ting riktig med en ekte Lightning-node.



### Alternativ 2: Innebygde Lightning-noder



Den andre kategorien av løsninger er basert på Lightning-noder som er integrert direkte i en mobilapplikasjon. Phoenix Wallet var først ute med denne modellen og er fortsatt en referanse. I dag finnes det andre prosjekter som tilbyr sammenlignbare tilnærminger, for eksempel Zeus (i innebygd modus) eller BitKit.



Ideen er enkel: Applikasjonen kjører faktisk en Lightning-node, men alle de komplekse operasjonene håndteres automatisk i bakgrunnen. Du har et "*Lightning wallet*"-grensesnitt med en huskeregel for sikkerhetskopiering, du ser saldo og betaler fakturaer, men du administrerer ikke kanaler, likviditet eller de fleste parametere.



![Image](assets/fr/014.webp)



Disse løsningene er alltid selvforvaltende. Nøklene som kontrollerer midlene er generated og lagret på telefonen din, og sikkerhetskopiering skjer via en seed eller tilsvarende mekanisme. Du har ikke bare en konto hos en tjenesteleverandør, du eier faktisk bitcoins som er låst i kanaler som tilhører deg og ikke kan stjeles.



Fordelene med LNs innebygde noder er mange:




- ekstremt enkel å installere og bruke;
- brukeropplevelse som ligger nær brukeropplevelsen til en Lightning wallet, men med selvoppbevaring;
- ingen manuell styring av kanaler eller likviditet;
- relativt enkel sikkerhetskopiering.



Men disse innebygde wallet-ene har også betydelige begrensninger. For det første, når det gjelder konfidensialitet, har tjenesteoperatøren (f.eks. ACINQ når det gjelder Phoenix) en ganske detaljert oversikt over strømmene som går gjennom noden din: mengder, frekvenser, mottakere, selv om dette sikkert vil bli bedre, spesielt med den gradvise innføringen av *Trampoline Nodes*. For det andre er du svært avhengig av denne operatøren som din viktigste Lightning-peer. Hvis ACINQ-noden blir utilgjengelig (i tilfellet Phoenix), hvis selskapet kommer under regulatorisk press eller endrer forretningsmodell, kan brukeropplevelsen din bli alvorlig forringet eller til og med kompromittert.



Denne enkelheten har imidlertid en pris. Innebygde LN-nodetjenester krever vanligvis spesifikke gebyrer for innskudd, uttak eller visse kanaladministrasjonsoperasjoner. Etter min mening er denne modellen fornuftig med tanke på tjenesten som tilbys, men for intensiv bruk kan den være mye dyrere enn en godt administrert konvensjonell Lightning-node.



### Alternativ 3: den klassiske Lightning-noden



Den tredje løsningen, som vi skal se nærmere på i dette LNP202-kurset, er å drive en konvensjonell Lightning-node på en dedikert server eller enhet.



Med "klassisk" mener jeg at du selv installerer og konfigurerer en Lightning-implementering (f.eks. LND) på toppen av din egen Bitcoin-node. Du velger dine peers, åpner kanalene dine, administrerer [innkommende og utgående likviditet](https://planb.academy/resources/glossary/inbound-capacity) og fastsetter retningslinjene for rutingavgifter.



Når det gjelder suverenitet, er det den beste løsningen. Du er ikke lenger avhengig av et spesifikt selskap for kanalene eller betalingene dine: Hvis en motpart sensurerer deg eller stenger en kanal, kan du åpne en annen med en annen node. Hvis en tjeneste forsvinner, forblir sats i kanalene du kontrollerer, og du kan ta dem tilbake i kjeden. Du kan også optimalisere de langsiktige kostnadene dine: Når kanalene dine er riktig dimensjonert og administrert, kan de samlede betalingskostnadene bli svært lave.



Når det gjelder konfidensialitet, er du selvsagt underlagt begrensningene i Lightnings egen modell, men du overlater ikke hele virksomheten din til en enkelt operatør.



Derimot er det åpenbart mer komplekst å sette opp en klassisk Lightning-node: Du må installere, konfigurere, vedlikeholde, overvåke oppdateringer, forstå logikken i kanaler og avgiftspolicyer, administrere kanaler og kontantstrøm, og så videre. Feilkonfigurasjon, slurvete sikkerhetskopiering eller uforsiktig administrasjon kan lettere føre til tap av sats. Noden må også kjøre kontinuerlig.



Det er nettopp denne veien jeg foreslår at du følger i dette kurset, og jeg følger deg hele veien for å begrense risikoen og strukturere fremgangsmåten din.



### Hvilken løsning for hvilken brukerprofil?



For å velge riktig løsning for Lightning-brukerprofilen din må du ta hensyn til to faktorer: hvor ofte du bruker Lightning, og hvor stor appetitt du har på teknisk administrasjon.



Hvis du ikke foretar mange Lightning-betalinger av og til, men likevel ønsker å kunne gjøre opp LN-fakturaer fra telefonen din fra tid til annen, uten å gi avkall på selvforvaring: En Bitcoin eller Liquid wallet med swap-funksjonalitet er sannsynligvis det beste alternativet. Du beholder eierskapet til midlene dine, administrerer ingen noder og aksepterer litt høyere gebyrer i bytte mot enkelhet.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Hvis du bruker Lightning ganske regelmessig og vil ha fordelene med en ekte node, men ikke vil bruke tid på å administrere kanaler, gebyrer eller infrastruktur, er en mobil innebygd Lightning-node en god løsning. Du beholder kontrollen over midlene dine, UX-en er fortsatt svært tilgjengelig, og all kompleksiteten er skjult, til prisen av en markant avhengighet av en operatør.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Hvis du er en middels eller avansert bruker, villig til å investere tid i å forstå og administrere infrastrukturen din, og ønsker maksimal kontroll over kanalene, likviditeten og kostnadene dine: en klassisk serverbasert Lightning-node er veien å gå. Det er den mest krevende løsningen, men også den som er mest i samsvar med Bitcoins idé om suverenitet.




# Opprette din første Lightning-node


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## Installere LND med Umbrel


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Nå som vi har gjennomgått det grunnleggende om Lightning og de tilgjengelige løsningene, er det på tide å komme til saken. For å ta dette kurset trenger du en Bitcoin-node som er synkronisert med Umbrel. Dette LNP202-kurset er en fortsettelse av BTC 202. Hvis du ennå ikke har en Bitcoin-node, vil jeg oppfordre deg til å ta dette andre kurset før du kommer tilbake hit når noden din er synkronisert. Jeg anbefaler på det sterkeste at du leser det, ettersom jeg ikke vil gå i detalj om drift, konfigurasjon og sikkerhetstiltak.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

I dette første kapittelet skal vi se på hvordan du installerer LND på din Umbrel. Umbrel fungerer på en slik måte at dette trinnet er svært enkelt, siden alt du trenger å gjøre er å installere et program.



Fra startsiden åpner du `App Store` nederst i grensesnittet.



![Image](assets/fr/015.webp)



Skriv inn `Lightning Node` i søkefeltet, og klikk deretter på applikasjonen.



![Image](assets/fr/016.webp)



Klikk deretter på knappen `Install` for å starte installasjonen.



![Image](assets/fr/017.webp)



Klikk på applikasjonen på startsiden for å åpne den, og velg deretter `Setup a new node`.



![Image](assets/fr/018.webp)



Du får en huskeseddel med 24 ord. Oppbevar den på et trygt sted. I neste kapittel skal vi se nærmere på hvordan du får tilbake tilgangen til Lightning-noden (dette er en mye mer kompleks prosess enn for en enkel Bitcoin wallet), men husk at denne frasen spiller en avgjørende rolle og må oppbevares med største forsiktighet.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Lagre denne frasen på samme måte som en vanlig huskeseddel: på et fysisk medium (papir eller metall) som er lagret på et sikkert sted, og klikk deretter på knappen `NESTE`.



![Image](assets/fr/019.webp)



Skriv deretter inn ordene i setningen for å kontrollere at du har skrevet dem riktig.



![Image](assets/fr/020.webp)



En advarsel vil minne deg på at programmet er i betaversjon, og at Lightning Network fortsatt er en eksperimentell teknologi. Du må selvsagt aldri forplikte deg til å bruke beløp på Lightning-noden som du ikke er forberedt på å tape.



Du kommer da til Lightning-nodens hovedgrensesnitt. Til venstre finner du Bitcoin i kjeden wallet som ligger på noden din. Dette er den ene generated fra 24-ordsfrasen du nettopp har lagret.



I midten finner du din Lightning wallet. Den representerer faktisk dine [utgående kontanter](https://planb.academy/resources/glossary/outbound-capacity), dvs. bitcoinsene du eier i Lightning-kanalene dine.



Til høyre ser du flere viktige opplysninger om noden din:




- Antall tilkoblinger og åpne kanaler;
- Din totale utgående kontantstrøm, dvs. hva du teoretisk sett kan bruke på Lyn;
- Din totale innkommende likviditet, dvs. hva du teoretisk kan motta på Lightning.



![Image](assets/fr/021.webp)



La oss begynne med å tilpasse noden vår. Klikk på de tre små prikkene øverst til høyre i grensesnittet, og deretter på `Avanserte innstillinger`. I undermenyen `Personalisering` kan du definere et offentlig navn for noden din (unngå å bruke ditt virkelige navn) og velge farge.



![Image](assets/fr/046.webp)



Klikk deretter på den grønne knappen "LAGRE OG GJENSTART" for å starte noden på nytt og ta i bruk endringene.



Lightning-noden er nå klar til å åpne sine første betalingskanaler. Men først skal vi ta en titt på hvordan du beskytter sats!



## Lagre Lightning-noden din


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



Før du sender din første sats til noden din, er det viktig å forstå hvordan sikkerhetskopieringen fungerer og hvilke risikoer som er forbundet med den. I motsetning til en enkel Bitcoin-portefølje i kjeden, er sikkerhetskopiering av en Lightning-node ganske komplisert: feil strategi kan føre til permanent tap av midlene dine. I dette kapittelet skal vi se på hva som egentlig må sikkerhetskopieres, og hvordan Umbrel håndterer denne prosessen med LND.



I dette kurset skal vi bruke LND (*Lightning Network Daemon*)-implementeringen. Selv om prinsippene er like for de andre implementeringene, er gjenopprettingsfilene og prosedyrene jeg skal snakke om, spesifikke for LND.



### Hva bør jeg spare på en Lightning node?



På en Lightning-node er det ikke nok å lagre seed og håpe at alt går tilbake til det normale. Flere elementer spiller forskjellige roller, så det er viktig å skille mellom dem.



#### seed (*aezeed*)



Når du initialiserer LND, mottar du en seed på 24 ord. Dette er et LND-spesifikt format som kalles "*aezeed*". Det er ikke en klassisk seed BIP39, selv om det ligner mye på en. Fra denne seed utleder LND de private nøklene til din wallet i kjeden som er knyttet til Lightning-noden, dvs. adressene du kan motta eller sende tilbake bitcoins til etter kanalstengninger.



![Image](assets/fr/019.webp)



Denne seed kan derfor brukes til å gjenskape wallet i kjeden som er knyttet til noden din, og til å hente tilbake midler som allerede har blitt repatriert i kjeden (f.eks. etter en kanalstenging). På den annen side er seed alene ikke tilstrekkelig til å gjenopprette Lightning-kanaler som fortsatt er åpne, ettersom den ikke inneholder den nødvendige informasjonen om statusen til kanalene dine.



#### Kanaldatabasen (`channel.db`)



LND lagrer den detaljerte statusen til kanalene dine i en database med navnet `channel.db`. Denne databasen inneholder:




- listen over de åpne kanalene dine;
- dine kolleger og identifikatorene deres;
- de siste commitment transaction-ene for hver kanal (de suksessive tilstandene som definerer hvem som eier hva i kanalen og gjør det mulig å få tilbake midler i kjeden i tilfelle et problem);
- informasjonen som trengs for å straffe en kollega som prøver å kringkaste en gammel rapport.



Problemet med denne databasen er at den er i konstant endring: Hver betaling, hver ruting, hver åpning eller lukking av en kanal endrer innholdet. Derfor er en konvensjonell sikkerhetskopi (f.eks. en periodisk kopi av `channel.db`) farlig. Hvis du gjenoppretter en for gammel versjon av `channel.db` og setter sammen noden på nytt med denne foreldede tilstanden, kan dine motparter tro at du kringkaster en gammel kanaltilstand. I dette tilfellet gir protokollen en straff: motparten din kan kreve tilbake hele kanalens midler, som om du hadde forsøkt å jukse.



I praksis er `channel.db` altså ikke et backup-medium i seg selv. Det er den levende tilstanden til noden din. Den eneste situasjonen der det gir mening å bruke den til å gjenopprette noden, er når du gjenoppretter denne databasen direkte fra en maskin som nettopp har feilet (f.eks. en disk som fremdeles kan leses). I dette tilfellet gjenoppretter du den nyeste tilstanden og kan starte LND på nytt på en annen maskin basert på denne databasen, i trygg forvissning om at denne tilstanden er så oppdatert som mulig, siden den gamle maskinen ikke lenger kjører. En annen situasjon der denne metoden kan fungere som en relevant sikkerhetskopi, er i en konfigurasjon med to disker, med en dynamisk, permanent kopi fra den ene til den andre. Denne typen oppsett er imidlertid mer komplisert å implementere.



Men det er en veldig dårlig idé å lage periodiske kopier av `channel.db` og lagre dem som sikkerhetskopier som skal gjenopprettes senere: Den dagen du bruker dem, risikerer du å straffe deg selv og miste alle dine sats.



#### Sikkerhetskopiering av statisk kanal (SCB)



For å gjøre katastrofegjenoppretting mulig har LND innført mekanismen *Static Channel Backup* (SCB). Dette er en spesiell fil, ofte kalt `channel.backup`, som inneholder statisk informasjon om kanalene dine: hvem som er dine peers, hvordan du kan kontakte dem og hva kanalene dine er.



Denne filen inneholder ikke detaljert kanalstatus eller oppdateringshistorikk. Den lar deg ikke gjenåpne kanaler i nøyaktig samme tilstand som de var i, eller fortsette å bruke denne Lightning-noden. Dens rolle er heller å fungere som et ankerpunkt for å be dine likemenn om å hjelpe deg med å lukke alle kanalene dine, og dermed motta din sats onchain, på nøkler som du kan hente takket være seed. Så i motsetning til filen `channel.db`, som endres ved hver betaling eller ruting, oppdateres SCB-filen bare når en kanal åpnes eller lukkes.



Ved gjenoppretting via SCB er prosessen som følger:




- Du gjenoppretter seed (*aezeed*), som gjenskaper din wallet i kjeden som er knyttet til Lightning-noden;
- Du gir LND den siste SCB-en din;
- LND bruker SCB til å finne listen over dine peers og kanalene du har med dem;
- Den kontakter hver enkelt motpart, forteller dem at du har mistet data og ber dem om å "tvangslukke" kanalen din med dem, slik at du kan gjenopprette onchain-delen din.



Tanken er at dine kolleger, når de oppdager at du rapporterer tap av data, vil kringkaste sin siste commitment transaction og stenge kraftkanalen. Når disse transaksjonene er bekreftet, dukker pengene dine opp igjen i kjedeporteføljen din (knyttet til seed).



Denne gjenopprettingsmekanismen er imidlertid ikke perfekt. For det første gjenoppretter den ikke Lightning-noden din, siden alle kanaler blir stengt. Du må da bygge en ny Lightning-node fra bunnen av. For det andre garanterer den ikke 100 % gjenoppretting, selv om den øker sjansene betraktelig for å gjenopprette saldoen i kjeden hvis det skulle oppstå et problem. Denne gjenopprettingsprotokollen avhenger nemlig av at de andre aktørene samarbeider og er tilgjengelige: Hvis en av dem er frakoblet, har mistet sine egne data eller nekter å samarbeide, kan pengene dine forbli blokkert, eller til og med gå tapt permanent. Derfor er det viktig at du ikke holder kanaler åpne på Lightning-noden din med peers som ikke kan nås, i lange perioder. Hvis du opplever et datatap på det tidspunktet og motparten forblir utilgjengelig, vil det være umulig å gjenopprette via SCB, og pengene dine vil forbli tapt til motparten kommer på nett igjen (kanskje for alltid).



For å oppsummere kan vi si at en god Lightning-backupstrategi på LND hviler på tre pilarer:




- Din seed (*aezeed*), for kjedelaget;
- Pålitelig automatisk SCB-sikkerhetskopiering;
- God kanalstyring ved å velge pålitelige samarbeidspartnere og preventivt stenge de som ofte er utilgjengelige.



### Hvordan håndterer Umbrel sikkerhetskopieringen av LND-noden?



Umbrel tilbyr en forenklet sikkerhetskopimekanisme for LND-noden, basert nettopp på SCB. Tanken er å spare deg for bryet med å manipulere denne filen selv, ta en sikkerhetskopi av den og automatisere prosessen så langt det er mulig.



Når du oppretter noden din på Umbrel, får du en seed som spiller en dobbeltrolle:




- den utleder Bitcoin på kjeden wallet som er knyttet til Lightning-noden din;
- brukes den til å utlede en sikkerhetskopiidentifikator og krypteringsnøkkel som brukes til eksterne SCB-sikkerhetskopier.



Takket være denne mekanismen tar Umbrel automatisk en kryptert sikkerhetskopi av SCB-en din og lagrer den på serverne sine via Tor. SCB-en lagres kryptert, takket være en nøkkel som stammer fra din seed. Så i tilfelle datatap er alt du trenger å gjøre å gjenskape en Bitcoin og Lightning-node på Umbrel, på samme eller en annen maskin, og deretter gå inn på din seed. Deretter kan du hente den nyeste SCB-statusen fra Umbrel-serverne, dekryptere den og starte prosessen med å gjenopprette midlene dine.



Disse sikkerhetskopiene krypteres lokalt av noden din før de sendes, noe som garanterer konfidensialiteten til dataene dine: Umbrel kan ikke lese innholdet i SCB-en. Overføringen skjer via Tor, noe som forhindrer at IP-adressen din blir lekket. I tillegg legger Umbrel til støy i trafikken (tilfeldig utfylling og falske sikkerhetskopier som sendes med uregelmessige intervaller) for å hindre serveren i å finne ut nøyaktig når du åpner eller lukker en kanal.



Den største fordelen med denne metoden er at den forenkler sikkerhetskopieringen av Lightning-noden betraktelig: Du trenger bare å ta sikkerhetskopi av seed én gang under initialiseringen av noden. Dette innebærer en viss risiko, siden det bare er en sikkerhetskopi av SCB-en, men for rimelige beløp er det et akseptabelt kompromiss.



### Beste praksis for å begrense risikoen for tap



Selv med Umbrel-backup kan noen enkle, gode rutiner redusere risikoen for å miste sats betraktelig:





- Overvåk tilgjengeligheten til kollegaene dine:



Hvis en viktig kanal ofte er knyttet til en motpart som ikke kan nås eller er ustabil, er det tryggere å stenge den mens noden fortsatt fungerer. En forebyggende kooperativ eller tvungen stenging eliminerer en potensiell kilde til problemer i tilfelle SCB gjenopprettes.





- Unngå å konsentrere for mye likviditet på ukjente peers:



Jo større kanal en node har med deg, desto viktigere er det at den er pålitelig. Velg seriøse, aktive noder med god forbindelse, slik at en eventuell fremtidig gjenoppretting via SCB kan skje uten problemer.





- Suppler Umbrel med lokale sikkerhetskopier:



I tillegg til Umbrels automatiske sikkerhetskopiering kan du også oppbevare en kryptert kopi av SCB-filen din (`channel.backup`) på et eksternt medium og oppdatere den med jevne mellomrom. Ideelt sett bør du fornye den hver gang du åpner eller lukker en kanal. Dette gir deg en reserveløsning hvis Umbrels automatiske sikkerhetskopieringstjeneste av en eller annen grunn blir utilgjengelig.





- Administrer seed på riktig måte



seed Umbrel gjenoppretter ikke bare din wallet i kjeden, men henter også ut krypteringsnøkkelen for sikkerhetskopier. En angriper med tilgang til den kan derfor starte en gjenoppretting og overføre pengene dine til sin egen wallet, uten engang å ha fysisk tilgang til noden din.



Så hvis du trenger å gjenopprette noden din, men ikke lenger har seed, vil du ikke kunne gjenopprette noe som helst: alle dine sats vil gå tapt. Det er derfor svært viktig å lagre seed med den største forsiktighet, kun på fysiske medier (papir eller metall), og å oppbevare den på et trygt sted. Hvis du vil ha mer informasjon om hvordan du administrerer en seed, kan du se denne veiledningen:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Hvordan lagrer jeg Lightning-noden min på Umbrel?



Nå som du har forstått hvordan teorien fungerer, la oss komme til det praktiske. Fra Lightning Node-applikasjonen din (som faktisk er LND) klikker du på de tre små prikkene øverst i høyre hjørne.



![Image](assets/fr/022.webp)



Det er tre elementer som er av interesse for sikkerhetskopien:




- Kontroller at alternativet `Automatisk sikkerhetskopiering` er aktivert. Dette vil automatisk sende den krypterte SCB-en din til Umbrels servere.
- Deretter kan du velge om du vil sende via Tor eller clearnet, ved å bruke alternativet `Backup over Tor`. Som forklart i de foregående avsnittene, anbefaler jeg på det sterkeste at du bruker Tor for å bevare konfidensialiteten din.
- Til slutt finnes det en "Last ned sikkerhetskopi av kanal"-knapp, som lar deg laste ned en "channel.backup"-fil, dvs. et kryptert øyeblikksbilde av SCB-en, til datamaskinen din. Dette gjør at du kan ta flere lokale sikkerhetskopier fra tid til annen, i tillegg til de som automatisk sendes til Umbrel-serverne.



Nå vet du hvordan du beskytter Lightning-nodens sats mot tap av data. I neste kapittel skal vi se på hvordan du kan sikre noden mot forsøk på juks.




## Watchtower: rolle og oppsett


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



I Lightning er hver kanal basert på en sekvens av suksessive tilstander, representert av upubliserte commitment transaction-er. Ved hver Lightning-betaling eller -ruting bygger de to deltakerne i kanalen et nytt par commitment transaction, som gjenspeiler den gjeldende fordelingen av midler i kanalen. Gamle commitment transaction blir foreldet.



Hvis en av partene publiserer en utdatert tilstand, har den andre parten rett til å sanksjonere den og kreve tilbake hele kanalens beløp. I dette kapittelet skal vi ta en kort titt på hvordan denne mekanismen fungerer, og deretter forklare hvordan du setter opp et ***watchtower***: et system for å beskytte Lightning-noden din mot mulige juksforsøk.



### Forstå hvordan vakttårn fungerer


Hver part i kanalen har til enhver tid en commitment transaction som, hvis den blir publisert, vil gjøre det mulig for dem å stenge kanalen og få tilbake sin andel av midlene. Denne prosessen kalles *tvungen stenging*. Men hvis de forsøker å publisere en eldre commitment transaction, som tilsvarer en tidligere tilstand i kanalen der den hadde flere sats, vil denne transaksjonen bli ansett som et forsøk på juks. I dette tilfellet kan motparten bruke tilbakekallingsnøkkelen som er knyttet til denne eldre tilstanden, til å gjenopprette hele beløpet i kanalen, mens juksemakeren er midlertidig blokkert av tidssperren.


Dette systemet betyr at det er svært risikabelt å publisere en gammel tilstand, dvs. å forsøke å jukse: Hvis den andre parten ser denne transaksjonen på mempoolen eller i blokkjeden før tidslåsen utløper, kan de bruke tilbakekallingsnøkkelen og få tilbake alle midlene. **Sikkerheten til Lightning-kanalen din avhenger derfor av din evne til å oppdage et juksforsøk innenfor tidsvinduet som tidslåsen setter**.



#### Hvorfor er vakttårn nødvendige?



Straffemekanismen fungerer bare hvis den skadelidte er i stand til det:




- overvåke hver nye Bitcoin-blokk for å se om en kanal commitment transaction har blitt publisert;
- avgjøre om denne transaksjonen tilsvarer den siste gyldige tilstanden eller en opphevet tilstand;
- i tilfelle en tilbakekalt status, for å kringkaste den lovlige transaksjonen i tide, ved å bruke tilbakekallingsnøkkelen til å gjenopprette alle midler før tidssperren utløper.



![Image](assets/fr/023.webp)



I et ideelt scenario er Lightning-noden din online 24/7, den er synkronisert og overvåker blokkjeden kontinuerlig. Derfor kan den på egen hånd oppdage et juksforsøk og reagere. I praksis kan imidlertid en personlig Lightning-node slå seg av, særlig i tilfelle langvarig strømbrudd eller svikt i internettforbindelsen.



Det er nettopp i disse periodene med nedetid at risikoen blir reell: Hvis en uærlig motpart publiserer en gammel status mens noden din er frakoblet, og tidssperren går ut uten at du reagerer, blir jukset effektivt. Du mister noen av eller alle pengene dine i kanalen.



Watchtower ble innført for å redusere denne risikoen. Et vakttårn er en ekstern tjeneste som overvåker blokkjeden på dine vegne, skanner etter mulig publisering av en gammel status på en av kanalene dine og, om nødvendig, automatisk sender ut straffetransaksjonen på dine vegne. Så selv om Lightning-noden din er frakoblet i en lengre periode, vil vakttårnet du bruker, så lenge det er i drift, kunne beskytte midlene dine ved å overvåke eventuelle forsøk på juks og påføre den tilsvarende straffen så snart det oppdager et forsøk.



#### Hvordan et vakttårn fungerer



Et vakttårn er utformet for å minimere informasjonen det får om kanalene dine, samtidig som det gir det mulighet til å handle hvis det oppstår et problem:




- For hver ny kanalstatus med en motpart forbereder noden din en potensiell straffetransaksjon på forhånd. Hvis motparten jukser, vil denne transaksjonen gjøre det mulig for deg å få tilbake alle pengene i kanalen;
- Noden krypterer deretter denne straffetransaksjonen ved hjelp av TXID-en til den tilsvarende commitment transaction (den som ville blitt brukt hvis juksemakeren skulle forsøke å svindle). Så lenge det ikke skjer noen stenging, kan ikke vakttårnet dekryptere denne transaksjonen, ettersom det ikke kjenner TXID-en til juksetransaksjonen;
- Noden din sender vakttårnet en pakke som inneholder den krypterte straffetransaksjonen og halvparten av TXID-en til den potensielle juksetransaksjonen.



Ettersom TXID-en som sendes til vakttårnet er ufullstendig, kan det ikke dekryptere rettferdighetstransaksjonen. Den kan imidlertid overvåke blokkjeden for en TXID som samsvarer med den delen den eier. Hvis den oppdager en slik transaksjon, forsøker den å bruke den fullstendige TXID-en til å dekryptere straffetransaksjonen din. Hvis dekrypteringen lykkes, vet den at det er et forsøk på juks, og publiserer umiddelbart straffetransaksjonen for deg.



![Image](assets/fr/024.webp)



Vakttårnet har derfor ikke innsyn i detaljene i kanalene dine: verken identiteten til de andre deltakerne, saldoen eller strukturen i transaksjonene. Den ser bare krypterte pakker. Den eneste informasjonen den kan utlede, er hvor raskt kanalene dine oppdateres, siden den mottar en pakke for hver nye tilstand, men ikke kan vite innholdet i den. I tilfelle juks, vil den helt sikkert oppdage kanalinformasjonen ved å dekryptere straffetransaksjonen, men sats vil i det minste bli reddet.



Denne mekanismen er basert på et kompromiss: Du delegerer muligheten til å publisere en forhåndssignert straffetransaksjon til vakttårnet, men denne transaksjonen forblir helt ugjennomsiktig for vakttårnet inntil noe juks finner sted. Vakttårnet kan verken endre mottakerne eller omdirigere midlene, siden det bare har en transaksjon som allerede er signert, med utgangene frosset i din favør. Den kan heller ikke kjenne detaljene i en kanal i en legitim tvungen eller kooperativ avslutning, ettersom TXID-ene ikke stemmer overens. På den annen side er Watchtower fortsatt en minimal betrodd tredjepart: Du må stole på at den er på nett og sender rettferdighetstransaksjonen din på riktig måte når du trenger det.



#### Å bli et vakttårn



I teorien kan enhver Lightning-node fungere som et vakttårn for andre noder (hvis de bruker samme implementering, f.eks. LND), samtidig som den selv blir beskyttet av andre noder som spiller denne rollen for den. I de følgende praktiske avsnittene skal jeg vise deg hvordan du setter opp denne enkle mekanismen på din LND under Umbrel.


En interessant strategi kan derfor være å bli enige med pålitelige bitcoiner-venner om å fungere som hverandres vakttårn. Du overvåker deres kanaler, og de overvåker dine.



### Finn et altruistisk vakttårn



Hvis du ikke kjenner noen rundt deg som kan tilby en vakttårntjeneste, finnes det en rekke altruistiske offentlige vakttårn du kan koble deg til. I dette LNP202-kurset foreslår jeg for eksempel at du kobler deg til vakttårntjenesten som tilbys i fellesskap av LN+ og Voltage, som er et vakttårn for LND.


Her har du påloggingsinformasjonen:



- Via Tor:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- Via Clearnet:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

For å takke dem for at de tilbyr denne gratis vakttårntjenesten, [du kan gi en donasjon via Lightning](https://lightningnetwork.plus/donation).


Nå som vi bruker en altruistisk vakttårntjeneste, skal vi se hvordan vi konfigurerer den på LND-noden vår under Umbrel.


### Sette opp et vakttårn


Fra applikasjonen `Lightning Node` klikker du på de tre prikkene øverst til høyre i grensesnittet, og velger deretter `Avanserte innstillinger`.


![Image](assets/fr/025.webp)


Gå deretter til menyen `Watchtower`.


![Image](assets/fr/026.webp)



Aktiver alternativet `Watchtower Client`, og klikk deretter på knappen `SAVE AND RESTART NODE`. Vent til LND starter på nytt.


![Image](assets/fr/027.webp)


Når omstarten er fullført, går du tilbake til den samme menyen og skriver inn ID-en til det altruistiske vakttårnet du har valgt i feltet. Klikk deretter på knappen "ADD" for å bekrefte. Du kan også justere parameteren `Watchtower Client Sweep Fee Rate`: dette er gebyrsatsen du er villig til å betale for en mulig rettferdighetstransaksjon kringkastet av vakttårnet. Det er ingen grunn til å velge en for høy sats, men du bør også unngå en for lav sats, ellers vil ikke den juridiske transaksjonen bli bekreftet i tide.


Start noden på nytt ved hjelp av knappen "LAGRE OG GJENSTART NODE" for å ta i bruk endringene.


![Image](assets/fr/028.webp)



Hvis du går tilbake til den samme menyen, vil du se at Lightning-noden nå er beskyttet av vakttårnet du nettopp har lagt til.



![Image](assets/fr/029.webp)



Et altruistisk vakttårn er som regel tilstrekkelig, spesielt hvis du ikke plasserer store pengebeløp på lynnoden din og hvis du forvalter noden godt (ikke la den være avslått for lenge). For enda større sikkerhet kan du også legge til flere ved å gjenta den samme prosessen.



## Åpne din første Lightning-kanal


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Hvis du har kommet så langt, vet du allerede at en Lightning-node uten en kanal er litt som en tom wallet: Den finnes, men den er ubrukelig. For å kunne sende eller motta betalinger må noden din være koblet til minst én annen node i Lightning-nettverket via en kanal. I fremtiden anbefaler vi på det sterkeste å åpne flere kanaler, av hensyn til robusthet og rutingseffektivitet. I de følgende kapitlene skal vi også se på hvordan du administrerer likvide midler, optimaliserer kanaltopologien og bruker mer avanserte verktøy enn det grunnleggende LND-grensesnittet på Umbrel.



Men i dette introduksjonskapitlet er målet ganske enkelt å forstå hvordan du velger en god Lightning-peer, hvor du finner informasjonen du trenger for å velge peers, og til slutt hvordan du åpner din første kanal via det grunnleggende LND-grensesnittet.



### Hvordan velge en god Lightning-peer?



Når du åpner en kanal, må du velge en peer: en annen Lightning-node som noden din skal være direkte koblet til via en kanal. Valget av motpart er viktig, ettersom det vil ha direkte innvirkning på:




- gjør det enklere for betalingene dine å finne veien;
- påliteligheten til kanalene dine over tid;
- rutingskostnadene dine.



Det finnes ikke en perfekt match for alle, men det finnes en rekke pålitelige kriterier for å identifisere gode kandidater.



#### 1. Knutepunkttilkobling



En god peer er en node som er godt koblet til Lightning-nettverket. Dette betyr ikke bare at den har et stort antall kanaler (selv om dette kan være en indikator), men først og fremst at den er koblet til andre pålitelige noder og har en tilstrekkelig sentral posisjon i nettverksgrafen.



En godt tilkoblet node øker sjansene for å finne en effektiv rute til de fleste betalingsdestinasjoner. Det reduserer også behovet for mellomliggende noder, noe som holder kostnadene nede.



Hvis du derimot åpner din første kanal til en isolert eller svakt tilkoblet node, kan det begrense mulighetene dine: Du vil kunne betale denne motparten, men det vil være mye vanskeligere å betale resten av nettverket.



#### 2. Kapitalisering og kanalkapasitet



En god node er også en node med tilstrekkelig kapital. Dette vises ved den totale kanalkapasiteten (summen av sats som er forpliktet til alle kanalene) og den gjennomsnittlige kanalkapasiteten (det er ofte bedre å ha noen få, godt kapitaliserte kanaler enn mange små).



En node med latterlig liten kapasitet, eller som bare har små kanaler, vil ikke være i stand til å rute betalinger med store beløp, noe som kan føre til feil i rutingen for deg.



#### 3. Retningslinjer for utgifter



Hver node fastsetter sine egne rutingavgifter (grunnavgift og avgiftssats). En god node vil ikke kreve ublu gebyrer for strategiske kanaler. For en første kanal er det best å velge en node med relativt moderate avgifter, slik at du ikke skader dine egne betalinger.



Husk at dine egne rutingavgifter også påvirker hvordan andre oppfatter deg som node: En node som stadig endrer avgiftene sine eller pålegger absurde kostnader, blir sjelden verdsatt.



#### 4. Stabilitet og ansiennitet



Peer-stabilitet er et svært viktig kriterium. En god node har høy oppetid (den er svært sjelden offline), den holder kanalene åpne over lang tid, og den åpner og lukker ikke kanaler uten grunn.



Gamle og fortsatt aktive kanaler er et godt signal: De tyder på at forholdet er lønnsomt for motparten, at noden vet hvordan den skal forvalte kapitalen sin, og at den ikke stenger når som helst, slik at du slipper å betale onchain-avgifter for stenging og gjenåpning.



Omvendt kan en kollega som ofte er offline, eller som raskt stenger kanaler, være en kilde til problemer for deg, og til ekstra kostnader for å åpne nye kanaler.



Selv med disse kriteriene vil du ikke gjøre et perfekt valg første gang. Det er normalt: Den virkelige kvaliteten til en kollega avsløres ved bruk. Derfor er det viktig å gjøre det:




- overvåke kanalaktiviteten (rutet volum, tilgjengelighet osv.);
- stenge kanaler som ikke tjener noe formål, eller som for ofte er offline;
- omallokere kapitalen din til bedre konkurrenter over tid.



Tanken er ikke å åpne og stenge kanaler hver dag (noe som ville vært kostbart i form av kjedekostnader), men å gradvis utvikle topologien slik at den konvergerer mot et sett med pålitelige, godt tilkoblede motparter som er kompatible med dine behov.



### Hvordan finner jeg en likemann?



For å kunne bruke disse kriteriene trenger du verktøy som gir oversikt over Lightning-nettverket. Det finnes flere utforskere og tjenester som kan gjøre dette. Blant de mest kjente Lightning-utforskerne er [1ML](https://1ml.com/) og [Amboss](https://amboss.space/).



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

Her foreslår jeg imidlertid at du bruker [Lightning Terminal-verktøyet fra Lightning Labs](https://terminal.lightning.engineering/), som gir en rangering (riktignok basert på delvis subjektive kriterier) av de Lightning-nodene som anses som mest relevante for å åpne en kanal.



![Image](assets/fr/030.webp)



Problemet med de veldig store Lightning-nodene på toppen av denne rangeringen er at de fleste ikke godtar kanalåpninger under svært høye beløp. Mange har også strenge retningslinjer for peer management, noe som kan føre til at kanalen din blir stengt. På den annen side har disse nodene generelt sett ikke behov for innkommende likviditet, gitt antallet tilkoblinger.



Jeg vil derfor råde deg til å jobbe deg nedover i rangeringen for å finne en node som er godt tilkoblet, pålitelig og tilstrekkelig sentral i nettverksgrafen, uten at den er for stor. Her har jeg for eksempel identifisert Lightning-noden på stacker.news, som har svært gode forbindelser, høy kapasitet og en sentral posisjon i nettverksgrafen.



![Image](assets/fr/031.webp)



En annen interessant tilnærming er å åpne en kanal til en node som har behov for innkommende likviditet, for eksempel en kjøpmann du kjenner, en forening eller et lokalsamfunn. Denne strategien har tre fordeler:




- Siden den valgte enheten trenger innkommende likviditet, vil den logisk sett ha mindre insentiv til å stenge kanalen din uten grunn;
- Den økonomiske aktiviteten øker sjansene for ruting på denne kanalen, og dermed for å kreve inn noen avgifter;
- Du gjør økosystemet en tjeneste og gir et verdifullt bidrag til andre bitcoinere.



Når du har identifisert en relevant node, kan du hente ut node-ID-en. Dette er ganske enkelt en sammenkjeding av nodens offentlige nøkkel, et `@`-skilletegn, IP- eller Tor-adressen og porten som brukes. Denne ID-en er lett tilgjengelig fra nodens profil i Lightning Explorer.



### Åpne din første kanal via LND



Nå som vi har identifisert noden som vi skal åpne vår første kanal med, trenger vi sats for å låse oss inn i den. For å gjøre dette må du mate Bitcoin på kjeden wallet som er assosiert med LND.



Fra hovedgrensesnittet til LND finner du `Bitcoin Wallet`, og klikker deretter på `Deposit`-knappen. En mottaksadresse i kjeden er da generated: send sats til den. Hvor mye du trenger å overføre avhenger av kapasiteten du ønsker å allokere til din første kanal, men husk at du trenger å sende litt mer enn den ønskede kapasiteten. Hvis du for eksempel ønsker å åpne en 500 000 sats-kanal, må du ikke sende nøyaktig 500 000 sats, men et høyere beløp.



![Image](assets/fr/032.webp)



Når transaksjonen er sendt, vises den i grensesnittet. Vent på bekreftelse før du åpner kanalen. Du vil se en grønn pil ved siden av den når den er bekreftet.



![Image](assets/fr/033.webp)



Bla ned til hovedgrensesnittet, og klikk deretter på "+ OPEN CHANNEL".



![Image](assets/fr/034.webp)



Skriv inn `Node ID` for noden du ønsker å åpne en kanal med, angi beløpet du ønsker å låse inn, og juster deretter åpningstransaksjonsgebyret i henhold til tilstanden på onchain-gebyrmarkedet. Sørg selvfølgelig for at du har tilstrekkelig med midler i LND onchain-porteføljen din på forhånd.



Når alle parametrene er stilt inn, klikker du på knappen `ÅPNE KANAL`.



![Image](assets/fr/035.webp)



Vent på at åpningstransaksjonen blir bekreftet på kjeden. Din første kanal er nå offisielt i drift: gratulerer!



Du kan se at 100 % av kanalens likviditet for øyeblikket er på min side: Det er normalt, siden det er jeg som har åpnet kanalen. Etter hvert som betalinger og ruting utvikler seg, vil denne fordelingen endre seg, men kanalens totale kapasitet vil alltid forbli den samme.



![Image](assets/fr/036.webp)



Nå som du har en kanal, kan du foreta dine første Lightning-betalinger, forutsatt at den valgte noden er riktig koblet til nettverket. I senere kapitler skal vi selvfølgelig se på hvordan du kan sette opp en mer praktisk metode for å betale Lightning-fakturaer fra mobilen. Men la oss nå prøve å foreta en første betaling direkte fra LND til Umbrel.



For å gjøre dette, klikk på `SEND`-knappen i `Lightning Wallet`-seksjonen, og lim deretter inn fakturaen som skal settes.



![Image](assets/fr/037.webp)



Fakturabeløpet vises. Bekreft betalingen ved å klikke på knappen `SEND`.



![Image](assets/fr/038.webp)



Hvis en gyldig rute blir funnet, bør den første lynbetalingen din være vellykket.



![Image](assets/fr/039.webp)



Hvis vi så ser på fordelingen av likviditet i kanalen, ser vi at min motpart nå har 5 002 sats på sin side. Dette tilsvarer de 5000 sats av betalingen jeg nettopp foretok, som han dirigerte til mottakerens node. De ekstra 2 sats representerer rutingsgebyrene jeg betalte, siden mottakeren mottok nøyaktig 5 000 sats.



![Image](assets/fr/040.webp)



For å forbedre påliteligheten til betalingene våre vil det åpenbart være nødvendig å åpne opp andre kanaler. Avhengig av målene våre må vi også finne en måte å gjøre innkommende likviditet tilgjengelig på, slik at vi kan motta betalinger på Lightning. Dette er temaet for neste avsnitt.



# Administrere Lightning-noden din


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Definer nodeoperatørprofilen din


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Nå som Lightning-noden din er oppe og går, er neste trinn å definere traderprofilen din. Dette er et viktig valg, ettersom det bestemmer kanalåpningsstrategien din, hvilken type motparter du foretrekker, og hvordan du håndterer likviditet.



For at dette skal fungere på Lightning, trenger du likviditet i riktig retning. Utgående likviditet tilsvarer din evne til å betale (sats tilgjengelig på din side av kanalene). Innkommende likviditet tilsvarer din kapasitet til å motta (sats tilgjengelig på dine motparters side). Med andre ord koker profilen din ned til et enkelt spørsmål: For det meste forlater sats noden din, eller kommer de inn i den?



### Forbrukeren



Dette er profilen til de aller fleste brukere. Du bruker noden din til å utføre Lightning-betalinger: til å kjøpe varer og tjenester, betale regninger, sende tips - kort sagt, til å bruke Lightning som et raskt betalingsmiddel. På den annen side mottar du lite fra Lightning, eller bare marginalt, for eksempel noen få donasjoner, refusjoner mellom venner eller noen få mikrobetalinger.



Denne profilen er enklest å håndtere, fordi hovedbehovet ditt er å kunne betale. I praksis betyr dette at du trenger utgående likviditet. Når du har åpnet en eller flere kanaler av riktig størrelse til stabile noder med god forbindelse, vil de utgående betalingene dine mekanisk flytte likviditet til den andre siden av kanalene dine. Det er nettopp denne bevegelsen som naturlig nok skaper en rimelig mengde innkommende likviditet. Selv om du ikke ønsker å motta på regelmessig basis, vil du derfor kunne motta fra tid til annen uten å implementere en kompleks strategi. Du trenger altså ikke å bekymre deg for den innkommende likviditeten.



I dette LNP202-kurset skal vi fokusere på denne "forbruker"-nodeoperatørprofilen, siden det er den som tilsvarer nesten alle Bitcoin-brukere på Lightning.



### Forhandleren



Selgeren er på en måte det motsatte av forbrukeren. Her er ikke hovedformålet å betale, men å samle inn penger. En bedrift, tjenesteleverandør, nettbutikk eller et utsalgssted som aksepterer Lightning, vil motta mange inngående betalinger og foreta relativt få utgående betalinger fra denne noden.



Denne profilen er mer krevende, ettersom en nektet betaling på Lightning potensielt representerer et tapt salg. Prioriteten blir derfor inngående likviditet. Hvis noden din ikke har nok inngående likviditet, vil kundene dine oppleve at betalingene deres mislykkes, selv om de har pengene, rett og slett fordi det ikke finnes noen rute for å få likviditeten til deg i riktig retning.



Den største utfordringen for forhandleren kommer også fra den naturlige utviklingen av kanaler. Hvis alt du gjør er å motta, vil kanalene dine gradvis fylles opp på din side. Du trenger derfor mekanismer for å opprettholde og fornye den innkommende likviditeten.



Det finnes imidlertid et enklere tilfelle: den blandede forbruker-/forhandlerprofilen. Hvis du samler inn penger på Lightning, men også bruker penger på Lightning (forretningsutgifter, betalinger til leverandører eller til og med personlige utgifter), gjenskaper de utgående betalingene naturlig nok de inngående. Styringen blir smidigere, ettersom strømmene utligner hverandre, og du har mindre behov for å ty til kunstige mekanismer som utelukkende er utformet for å gjenvinne inngående likviditet.



### Ruteren



Ruteren er en spesifikk profil. Den bruker ikke sin Lightning-node til å betale eller kreve inn penger, men til å dirigere andres betalinger og kreve inn gebyrer. Målet er å være en nyttig, pålitelig og økonomisk konkurransedyktig rute i Lightning-grafen.



For å være ærlig med deg, er det å være en ruter på Lightning en mer kompleks virksomhet enn det ser ut, og det er vanskelig å oppnå lønnsomhet. Først og fremst er det dyrt å åpne og stenge kanaler i form av kjedekostnader. For å rute effektivt må du ofte justere topologien, teste, stenge underpresterende kanaler, åpne nye og jevnlig rebalansere likviditeten. For det andre er konkurransen knallhard: Store, etablerte noder tar naturlig nok en stor del av trafikken, og det er vanskelig å få fotfeste uten å binde opp betydelig kapital i store kanaler.



Det stilles også høye krav til driften. En routing-node må være ekstremt stabil, overvåket, ha skikkelig sikkerhetskopi og være strengt administrert. Du må overvåke kanalens ytelse, tilpasse avgiftspolitikken, opprettholde en balansert likviditet, administrere peers og raskt løse tekniske problemer. Dette nivået av engasjement kan være interessant som en teknisk hobby eller som et bidrag til infrastrukturen, men hvis målet ditt bare er å bruke Lightning på en suveren måte, er det sjelden relevant å gå inn i ruting for å tjene penger. Derfor dekker ikke dette LNP202-kurset denne profilen i dybden.



### Finn ut hvor du befinner deg før du går videre



Hvis du passer inn i forbrukerprofilen, vil du prioritere å kunne betale på en pålitelig måte med enkel administrasjon. Hvis du er en kjøpmann, vil du prioritere å få inn penger uten å mislykkes, noe som innebærer en strategi for innhenting av inngående likviditet. Hvis du vurderer ruting, må du se på det som en krevende, økonomisk usikker og tidkrevende aktivitet.



Ved å definere denne profilen nå kan du unngå en klassisk fallgruve: å bruke en kanalstrategi som er utformet for en forhandler eller ruter, når du bare er en bruker som ønsker å betale.



## Bruke en Lightning node manager


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



I forrige del av dette LNP202-kurset brukte vi det grunnleggende grensesnittet i applikasjonen `Lightning Node` på Umbrel. Dette grensesnittet er tilstrekkelig for viktige operasjoner (sjekke saldoer, se kontantfordeling, åpne og lukke kanaler), men det er bevisst svært forenklet. Denne enkelheten begrenser de tilgjengelige alternativene og gir ikke tilgang til mange av de avanserte funksjonene i LND-noden. Derfor vil vi nå bruke en annen, mer omfattende Lightning-programvare for nodeadministrasjon.



Denne tilleggsprogramvaren vil ganske enkelt være et supplerende administrasjonsgrensesnitt for noden din. Det betyr at du kan fortsette å bruke Lightning Node-grensesnittet parallelt, og til og med bruke flere ulike grensesnitt hvis du ønsker det. Dette er ganske enkelt forskjellige måter å samhandle med den samme Lightning-noden på.



Blant de mest kjente programvarene er:




- [Alby Hub](https://albyhub.com/);
- [Ride The Lightning](https://www.ridethelightning.info/);
- [ThunderHub](https://thunderhub.io/).



Alle tre er gode løsninger. Hvis du ønsker det, kan du teste alle tre med noden din før du velger den som passer deg best. Personlig bruker jeg ThunderHub av gammel vane og fordi det virker mer komplett enn de andre. Det er dette verktøyet jeg vil presentere i dette kurset, men du kan også velge ett av de to andre alternativene. Vi har en egen veiledning for hvert av disse programmene på Plan ₿ Academy.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### Installer ThunderHub



Alle disse programmene kan enkelt installeres fra Umbrel App Store. Som sagt skal vi bruke ThunderHub her, men hvis du ønsker å teste et annet program senere, er fremgangsmåten den samme.



![Image](assets/fr/041.webp)



Umbrel gir deg et standardpassord for å få tilgang til ThunderHub. Kopier det: du trenger det med en gang. Husk også å lagre det i passordbehandleren din, siden du vil bli bedt om det hver gang du åpner programvaren.



![Image](assets/fr/042.webp)



Klikk på `Login`, og lim deretter inn passordet du fikk av Umbrel for å logge inn.



![Image](assets/fr/043.webp)



Du kommer da til startsiden til ThunderHub, som viser hovedinformasjonen om Lightning-noden din.



![Image](assets/fr/044.webp)



Til å begynne med anbefaler jeg at du aktiverer tofaktorautentisering (2FA). I innstillingene klikker du bare på "Aktiver" ved siden av "Aktiver 2FA", og følger deretter den vanlige prosessen.



![Image](assets/fr/045.webp)



### Bruk ThunderHub



ThunderHub er relativt enkelt å lære seg. Alle menyene er tilgjengelige fra venstre kolonne i grensesnittet. For å oppsummere, her er hva hver enkelt meny gjør:




- home: nodeoversikt, saldoer og raske handlinger;
- dashbord: tilpassbart dashbord med widgeter og beregninger;
- jevnaldrende: Vis og administrer tilkoblinger til andre Lightning-noder;
- kanaler": fullstendig kanaladministrasjon (likviditet, gebyrer, stenging osv.);
- rebalance": et verktøy for rebalansering av kanaler via sirkulære betalinger;
- transaksjoner: historikk over sendte og mottatte Lightning-betalinger;
- forwards`: rutingstatistikk og kostnader generated av noden din;
- `Kjede`: Bitcoin onchain-portefølje (UTXO og transaksjoner);
- gW-201-integrasjon for overvåking og sikkerhetskopiering;
- verktøy: avanserte verktøy (sikkerhetskopier, rapporter, makroner, signaturer osv.);
- bytte: Lyn-/kjedebytte via Boltz;
- `Stats`: overordnet statistikk og ytelse for Lightning-noden din.



Med dette settet av funksjoner har du alle verktøyene du trenger for å administrere Lightning-noden din på en effektiv måte. Det er ikke nødvendig å beherske alle funksjonene i detalj med en gang: Vi kommer til å utforske dem gradvis gjennom dette kurset. Men hvis du ønsker å gå mer i dybden på programvaren, kan du ta en titt på veiledningen vår ThunderHub:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

Menyen vi er mest interessert i her, er `Channels`. Her får du en detaljert oversikt over alle kanalene i noden din, med deres likviditetsfordeling. Du kan spesielt se hvilke kanaler som er åpne i `Open`, hvilke som venter på å bli åpnet eller stengt i `Pending`, og hvilke som allerede er stengt i `Closed`.



![Image](assets/fr/047.webp)



For en gitt kanal kan du klikke på motpartens navn eller kanal-ID for å åpne Amboss-siden og få mer informasjon. Du kan også klikke på blyantikonet for å endre kanalens parametere, inkludert gebyrpolicyen som gjelder for kanalen hvis noden din videresender betalinger til noden til motparten.



![Image](assets/fr/048.webp)



Hvis du hovedsakelig bruker Lightning-noden din som en "forbruker", trenger du ikke å endre disse avgiftene: Du kan beholde standardverdiene. Hvis du derimot ønsker å forstå bedre hvordan rutingavgifter fungerer på Lightning, anbefaler jeg LNP 201-opplæringen, og spesielt kapittel 4.1:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Ved å klikke på det lille krysset ved siden av en motpart kan du starte stenging av en kanal. Hvis du for eksempel merker at en motpart regelmessig er inaktiv, kan det være hensiktsmessig å stenge denne kanalen for å omfordele kapitalen din til en mer pålitelig motpart.



Da har du to alternativer. Det første, som alltid er å foretrekke, er kooperativ lukking. Ved å bekrefte denne handlingen ber noden din motparten om å stenge kanalen i fellesskap. Hvis han aksepterer, kan du kringkaste transaksjonen i kjeden og få tilbake din andel av midlene. Fordelene med denne metoden er at du velger onchain-gebyrene for transaksjonen, slik at du unngår unødvendige kostnader, og at midlene utbetales raskere, uten tidslås.



![Image](assets/fr/049.webp)



Det andre alternativet er tvungen lukking. I dette tilfellet ber du ikke om motpartens samtykke, men sender direkte ut den siste commitment transaction du har. Jeg vil ikke anbefale denne metoden med mindre det er siste utvei, for eksempel hvis motparten systematisk nekter å samarbeide om nedleggelser eller ikke lenger svarer. Tvungen stenging har to store ulemper: Avgiftene er ofte svært høye, ettersom de er fastsatt på forhånd for å forutse en økning i kjedegebyrene, og det er en forsinkelse i tilbakebetalingen av midlene, ettersom de er blokkert av en tidslås. Denne tidslåsen gir motparten tid til å reagere i tilfelle et juksforsøk (noe som åpenbart ikke er tilfelle her, men du må likevel vente).



![Image](assets/fr/050.webp)



Til slutt, for å åpne en ny kanal, går du til `Home`-menyen og klikker på `Open a Channel` i `Liquidity`-delen. Du vil da kunne angi ID-en til den valgte noden, kanalkapasiteten, ønsket Lightning-routing-avgift og onchain-avgiften for åpningstransaksjonen.



![Image](assets/fr/051.webp)



Dette er de viktigste handlingene du trenger å utføre på ThunderHub. Vi vil oppdage andre funksjoner etter hvert som vi går videre i dette LNP202-kurset.



## Innhenting av inngående likviditet


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Som du kan se, er det ikke spesielt komplisert å ha utgående likviditet for å utføre betalinger på Lightning. Det er bare å åpne kanaler på eget initiativ til andre noder og begynne å sende sats. På den annen side er det mer komplisert å ha innkommende likviditet for å motta betalinger på Lightning, siden du enten må få andre noder til å åpne kanaler til deg, eller du må flytte likviditeten selv ved å foreta betalinger.



Hvis du har en "forbrukerprofil", trenger du som regel ikke å bekymre deg for innkommende likviditet. Din bruk av Lightning-noden vil hovedsakelig være betalingsorientert, snarere enn innbetaling. Ved å foreta noen få Lightning-betalinger vil du naturlig nok skape inngående likviditet over tid.



Hvis du derimot har en "merchant"-profil, er situasjonen omvendt: Du vil hovedsakelig samle inn betalinger og foreta få av dem. Du kan altså ikke bare stole på dine egne betalinger for innkommende likviditet. Det blir derfor nødvendig for andre Lightning-noder å åpne kanaler til din. Men hvordan kan dette oppnås? Hvordan får du andre operatører til å binde opp kapital for deg? Det er nettopp det vi skal se nærmere på i dette kapittelet.



### Kjøp av inngående likviditet



Som du forventer, er den mest effektive måten å få noen til å handle på å betale dem. For innkommende likviditet til Lightning-noden din er prinsippet nøyaktig det samme. Den enkleste måten å få kanaler til noden din på, er å betale for tjenesten og kapitalbindingen som er involvert.



Hvis du er en bedrift eller forhandler, betyr denne tilnærmingen at du raskt kan få pålitelige kanaler for å innhente betalinger fra kundene dine uten friksjon.



Det finnes mange måter å kjøpe inngående likviditet på. Den jeg personlig bruker og anbefaler er Ambosss [Magma](https://magma.amboss.tech/) plattform. Den er veldig enkel å bruke, det går raskt å åpne en kanal, og prisene er generelt rimelige. Magma fungerer som en markedsplass med tilbydere og etterspørrere, men versjon 2 har forenklet opplevelsen betraktelig: Du oppretter ganske enkelt en forespørsel, betaler prisen via Lightning, og Magma matcher den automatisk med det beste tilgjengelige tilbudet. Etter seks bekreftelser i kjeden er kanalen din med innkommende likviditet oppe og går. Slik fungerer det:



Gå til [Magma-nettstedet](https://magma.amboss.tech/buy), i `Buy Channels`-delen.



![Image](assets/fr/052.webp)



Hvis du ønsker det, kan du opprette en konto for å spore kjøpene dine, men dette er ikke obligatorisk. Hvis du ikke oppretter en konto, vil Magma bare gi deg en økt-ID, som gjør det mulig for deg å hente frem kjøpene dine på et senere tidspunkt.



Når du er på nettstedet, fyller du ut informasjonen som kreves for å kjøpe likviditet. Velg `One Time` for et engangskjøp, og angi deretter beløpet du er villig til å betale for innkommende likviditet. Jo høyere beløp du betaler, desto større kapasitet får kanalen som åpnes for noden din. Nedenfor vises et estimat av kanalens kapasitet: Dette er en tilnærming, ettersom det endelige beløpet vil avhenge av det beste tilbudet Magma finner, som noen ganger er høyere, andre ganger lavere.



![Image](assets/fr/053.webp)



Skriv deretter inn node-ID-en din. Du finner den for eksempel i menyen `Node ID` i applikasjonen `Lightning Node` på Umbrel.



![Image](assets/fr/054.webp)



Når alle opplysningene er fylt ut, klikker du på knappen "Gjennomgå og åpne bestilling".



![Image](assets/fr/055.webp)



Hvis du ikke har opprettet en konto, vil Magma gi deg en øktnøkkel og en sikkerhetskopifil. Oppbevar disse to elementene på et trygt sted, slik at du kan hente tilbake bestillingen på et senere tidspunkt eller spore statusen hvis det skulle oppstå et problem. Når du har lagret filen, klikker du på knappen "Betal med Lightning".



![Image](assets/fr/056.webp)



Magma sender deretter en lynfaktura på det beløpet du har valgt. Du må betale den. Hvis du allerede har kanaler på Lightning-noden din, kan du betale direkte fra den, eller bruke en annen ekstern Lightning wallet.



![Image](assets/fr/057.webp)



Når betalingen er utført, vises transaksjonen som behandlet i Magma-grensesnittet.



![Image](assets/fr/058.webp)



Etter noen minutter blir forespørselen behandlet: en kanal med sats blir åpnet til Lightning-noden din. Når åpningstransaksjonen er bekreftet i kjeden, får du tilgang til den tilsvarende innkommende likviditeten.



![Image](assets/fr/059.webp)



Magma er også integrert direkte i ThunderHub. I `Home`-fanen blar du ned til `Liquidity`-delen og klikker på `Buy Inbound Liquidity`. Alt du trenger å gjøre er å angi ønsket beløp og bekrefte. Du trenger ikke å betale noen fakturaer manuelt, ettersom ThunderHub automatisk tar seg av betalingen fra noden din.



![Image](assets/fr/060.webp)



Hvis du er en kjøpmann, er denne typen tjeneste spesielt egnet, ettersom den gjør det mulig for deg å raskt få en stor mengde innkommende likviditet fra pålitelige noder, noe som garanterer at kundene dine vil kunne betale deg uten problemer. Hvis du derimot er privatperson, eller hvis du ikke ønsker å betale for innkommende likviditet, finnes det også gratisløsninger. La oss ta en titt.



### Samarbeid om inngående likviditet



Hvis du ikke er trader, men likevel trenger innkommende likviditet (for eksempel for å prime noden din ved oppstart, mens du venter på at noen betalinger skal utføres), trenger du ikke nødvendigvis å betale for det. En av mine foretrukne løsninger er å samarbeide med andre nodeoperatører som også har behov for inngående likviditet, og åpne lynkanaler for hverandre. På denne måten får du utgående likviditet ved å åpne en kanal, samtidig som du får innkommende likviditet, helt gratis (med unntak av onchain-avgifter for åpning).



Du kan selvfølgelig ordne dette direkte med andre bitcoinere. Det finnes imidlertid en plattform dedikert til denne typen sirkulære åpninger: [Lightning Network +](https://lightningnetwork.plus/). Prinsippet er ikke å åpne to kanaler mellom de samme personene, men å sette opp sirkulære åpninger som involverer minst tre deltakere, eller enda flere.



La oss ta et eksempel for å forstå hvordan Lightning Network + fungerer:




- En nodeoperatør, kalt `A`, publiserer en kunngjøring om at han ønsker å åpne en 1 million sats-kanal med to andre personer;
- Annonsen forblir aktiv til flere deltakere legges til;
- Senere slutter to operatører, `B` og `C`, seg til kunngjøringen av `A`-noden. Triangelet er nå komplett, og åpningsfasen kan begynne.
- Node `A` åpner en kanal til node `B`;
- Node `B` åpner en kanal til node `C`;
- Node `C` åpner en kanal til node `A`.



Ved slutten av operasjonen har hver node 1 million sats i utgående likviditet og 1 million sats i inngående likviditet. Denne ordningen kan utvides til fire eller fem deltakere.



Det finnes selvsagt ingen teknisk mekanisme som kan garantere at en deltaker faktisk åpner kanalen de har forpliktet seg til å opprette. Derfor har plattformen opprettet et omdømmesystem, basert på positive anmeldelser når operatørene oppfyller forpliktelsene sine. Og i verste fall, hvis du støter på noen som ikke samarbeider, har du ikke tapt penger: Du har bare gått glipp av en mulighet til å få inn likviditet.



Denne løsningen er spesielt egnet for en "forbrukerprofil", ettersom den lar deg få innkommende likviditet gratis, samtidig som du kobler noden din til andre små aktører. Hvis du derimot er trader, er denne tilnærmingen generelt ikke relevant: Hver sat av innkommende likviditet krever at du blokkerer en sat av utgående likviditet, og ditt store behov for innkommende likviditet vil da innebære at du binder opp for mye kapital.



For å bruke Lightning Network+ har du to alternativer: enten bruke applikasjonen som er integrert i Umbrel, eller bruke det klassiske nettstedet og opprette en konto ved å logge inn fra noden din. Jeg anbefaler sistnevnte, ettersom den integrerte applikasjonen ikke tilbyr alle tilgjengelige funksjoner.



Gå til nettstedet [Lightning Network +](https://lightningnetwork.plus/) og klikk på "Logg inn"-knappen øverst til høyre i grensesnittet.



![Image](assets/fr/061.webp)



For å autentisere deg selv må du signere meldingen ved hjelp av den private nøkkelen til Lightning-noden din. Med ThunderHub er denne operasjonen veldig enkel. Begynn med å kopiere meldingen som vises av LN+.



![Image](assets/fr/062.webp)



I ThunderHub går du til fanen `Verktøy` og klikker deretter på knappen `Signer` i delen `Meldinger`.



![Image](assets/fr/063.webp)



Lim inn autentiseringsmeldingen fra LN+, og klikk deretter på `Signer`.



![Image](assets/fr/064.webp)



ThunderHub signerer deretter denne meldingen ved hjelp av nodens private nøkkel. Kopier generated-signaturen.



![Image](assets/fr/065.webp)



Lim inn denne signaturen i det tilsvarende feltet på LN+-nettstedet, og klikk deretter på `Logg på`.



![Image](assets/fr/066.webp)



Du er nå koblet til LN+ med Lightning-noden din. Denne prosessen gjør det mulig for LN+ å verifisere at du er den rettmessige eieren av noden du gjør krav på på plattformen deres.



![Image](assets/fr/067.webp)



Hvis du ønsker det, kan du tilpasse LN+-profilen din, for eksempel ved å legge til en kort biografi.



For å delta i din første sirkulære kanalåpning, går du til menyen `Swaps` øverst i grensesnittet. Her finner du alle tilgjengelige bytter, avhengig av nodens egenskaper.



![Image](assets/fr/068.webp)



For å bli med i et eksisterende byttetilbud klikker du bare på det og registrerer deg. På LN+ kan imidlertid skaperen av et byttetilbud stille visse betingelser for deltakerne, for eksempel et minimum antall kanaler eller en minimum total nodekapasitet. Det er derfor mulig, spesielt i begynnelsen, at få tilbud vil være tilgjengelige for noden din. I mitt tilfelle var ingen tilbud tilgjengelige for noden min, til tross for at noen få kanaler allerede var åpne. Så jeg opprettet mitt eget bytte, og du kan gjøre det samme hvis du er i samme situasjon.



Klikk på `Start Liquidity Swap`, og skriv deretter inn tilbudsparametrene dine:




- Velg det totale antallet deltakere (3, 4 eller 5);
- Angi hvor mange kanaler som skal åpnes (sørg for at du har minst dette antallet i onchain wallet);
- Definer kanalens åpningstid. Dette er den perioden deltakerne er enige om ikke å stenge dem;
- Til høyre kan du angi begrensninger for deltakerne: minste antall kanaler, minste totale kapasitet og hvilken type tilkobling som godtas.



Når alle parametrene er stilt inn, klikker du på knappen `Start Liquidity Swap`.



![Image](assets/fr/069.webp)



Byttetilbudet ditt er nå opprettet. Nå trenger du bare å vente på at andre nodeoperatører registrerer seg. Hvis vilkårene dine ikke er for restriktive, bør ikke dette ta for lang tid. Husk å følge med på statusen for byttet ditt i timene eller dagene som følger.



![Image](assets/fr/070.webp)



Alle bytteplassene er tatt: Vi går nå videre til kanalåpningsfasen. Hver deltaker kan se fra sitt LN+-grensesnitt hvilken node han må åpne en Lightning-kanal til.



![Image](assets/fr/084.webp)



På din side åpner du kanalen ved hjelp av Node-ID-en som leveres av LN+, og respekterer det angitte beløpet. Som vi har sett i tidligere kapitler, kan du gjøre dette enten via ThunderHub, med en annen Lightning Node Manager eller direkte fra det grunnleggende Lightning Node-applikasjonsgrensesnittet.



![Image](assets/fr/085.webp)



Når åpningen er lansert, kan du se at den vises i delen med ventende kanaler. I mitt tilfelle er det kanalen med noden `Plebian_fr`.



![Image](assets/fr/086.webp)



Du kan deretter gå tilbake til LN+ for å bekrefte at du har startet kanalåpningen. Klikk ganske enkelt på knappen `Kanalåpning startet`.



![Image](assets/fr/087.webp)



Når alle de andre deltakerne også har åpnet kanalen de har forpliktet seg til, må du huske å gi dem en positiv anmeldelse.



![Image](assets/fr/088.webp)



Hvis det oppstår problemer eller forsinkelser, kan du kontakte fagfellene dine direkte via kommentarfeltet nederst på siden.



![Image](assets/fr/089.webp)



Noen deltakere ønsker kanskje å balansere de sirkulære kanalene fra begynnelsen av, ved å foreta en betaling til seg selv. Dette sikrer en balansert fordeling av kontanter i hver kanal. Hvis du har en "forbruker"-profil, er dette ikke nødvendig, men du kan enten gjøre denne rebalanseringen selv hvis du ønsker det, eller midlertidig sette kanalavgiftene dine til null for å gjøre det enklere for den som ønsker å gjøre det. Noen ganger er det ingen som ønsker å gjøre det.



![Image](assets/fr/090.webp)




# Frigjør potensialet i Lightning-noden din


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Koble til en mobil wallet via Tailscale


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



Nå har du en godt tilkoblet Lightning-node, med både innkommende og utgående likviditet. Så du er klar til å bruke Lightning-noden din i det virkelige liv. Frem til nå har vi alltid brukt grensesnitt direkte på Umbrel, enten applikasjonen `Lightning Node` eller grensesnittet `ThunderHub`. Disse verktøyene fungerer for å sende og motta betalinger, men er helt klart ikke optimalisert for daglige Lightning-betalinger. Grensesnittet er designet for bruk på en datamaskin, upraktisk på en smarttelefon, og krever også en tilkobling til det samme nettverket for å fungere skikkelig (selv om det er teknisk mulig å koble seg til eksternt via Tor).



I praksis er det vi som bitcoinere er ute etter et klassisk Lightning wallet-grensesnitt på smarttelefonen: muligheten til å skanne fakturaer via QR-kode, og et enkelt grensesnitt for å betale og ta ut sats. Det er nettopp dette vi skal implementere i dette og neste kapittel. Den generelle ideen er å ha en mobil Lightning wallet-applikasjon på smarttelefonen din, som kan brukes fra hvor som helst (ikke bare det lokale nettverket), men som i bakgrunnen er avhengig av din egen Lightning-node for å sende og motta betalinger.



### Hvilke løsninger finnes for å koble til en mobil kunde?



I dag finnes det flere måter å gjøre dette på, både når det gjelder mobilapplikasjonen og typen tilkobling mellom noden og denne applikasjonen. De tre viktigste tilkoblingsmåtene er




- via ***Tor***;
- via VPN ***Tailscale***;
- via ***Nostr Wallet Connect***.



For noen år siden pleide jeg å koble meg opp via ***Tor***, men jeg sluttet raskt: antallet feil og kommunikasjonsforsinkelsene var altfor store. I teorien fungerer det, men i praksis var brukeropplevelsen katastrofal. Jeg vil derfor fraråde denne tilnærmingen.



Alternativet jeg da valgte, var å bruke en ***Tailscale*** VPN for å sikre kommunikasjonen mellom mobilapplikasjonen og noden. Denne løsningen fungerer veldig bra: Selv på mobilnettverk med lav gjennomstrømning går betalingene mine alltid gjennom uten problemer. Det er denne metoden jeg kommer til å introdusere først i dette kapittelet, med Zeus-applikasjonen.



I neste kapittel skal vi se på en annen, nyere løsning, som også fungerer svært godt: ***Nostr Wallet Connect***. Denne gangen bruker vi Alby Go-applikasjonen for å presentere et alternativ, selv om Zeus også er kompatibel med NWC hvis du ønsker det.



### Installere og konfigurere Tailscale



For denne første metoden trenger vi Tailscale. Dette er en VPN-løsning basert på WireGuard, som lar deg koble til enheter spredt over hele Internett på en sikker måte, samtidig som den automatisk håndterer kryptering, autentisering og NAT-traversering. Enkelt sagt er det som om alle enhetene dine var koblet til samme LAN som ruteren din, selv om de kan befinne seg hvor som helst på Internett.



For å bruke den må du først opprette en konto. Gå til Tailscale-nettstedet, og klikk deretter på "Kom i gang"-knappen.



![Image](assets/fr/071.webp)



Velg deretter en identitetsleverandør for Tailscale-kontoen din. Personlig brukte jeg en av GitHub-kontoene mine til å logge inn.



![Image](assets/fr/072.webp)



Når du har logget inn, blir du stilt noen spørsmål om bruken din. Svar kort på dem for å fortsette.



![Image](assets/fr/073.webp)



Tailscale tilbyr deretter å installere en klient på maskinen din. For øyeblikket er det ikke det vi er interessert i: Gå direkte til Umbrel og installer Tailscale-applikasjonen fra App Store.



![Image](assets/fr/074.webp)



Når applikasjonen åpnes, klikker du på `Logg inn`, og følger deretter autentiseringsprosessen ved å bruke samme metode som da du opprettet kontoen din.



![Image](assets/fr/075.webp)



Klikk på `Connect` for å bekrefte. Din Umbrel er nå koblet til VPN-nettverket ditt.



![Image](assets/fr/076.webp)



Last deretter ned Tailscale-applikasjonen til smarttelefonen din, og logg inn med samme konto. Merk: På Android er det ikke mulig å bruke to VPN-er samtidig. For at Tailscale skal fungere, må du deaktivere alle andre aktive VPN-er. Hver gang du vil bruke Lightning-noden din via Zeus, må du dessuten aktivere Tailscale VPN, ellers vil ikke tilkoblingen bli opprettet.



![Image](assets/fr/077.webp)



Nå som minst to klienter er tilkoblet på Tailscale-siden, kan du få tilgang til administrasjonskonsollen med en liste over alle enhetene som er koblet til nettverket, og deres Tailscale-IP-adresser.



![Image](assets/fr/078.webp)



### Koble til Zeus



Installer Zeus-applikasjonen på telefonen din. Når den åpnes, velger du "Avansert oppsett" og deretter "Opprett eller koble til en wallet".



![Image](assets/fr/079.webp)



I delen `Wallet-grensesnitt` velger du `LND (REST)`. Skriv deretter inn Tailscale-adressen til Umbrel, som du finner fra Tailscale-dashbordet eller direkte i Tailscale-applikasjonen på Umbrel. For porten skriver du inn `8080`.



![Image](assets/fr/080.webp)



Zeus ber deg deretter om å oppgi en `Macaroon`. Dette er en autorisasjon token som lar deg nøyaktig definere rettighetene som er gitt til en applikasjon (i dette tilfellet Zeus) for å samhandle med Lightning-noden din. Det er mulig å generate lage en macaroon fra ThunderHub menyen `Tools`, undermenyen `Bakery`, men for dette formålet er det enklest å hente den direkte fra applikasjonen `Lightning Node`.



Klikk på de tre små prikkene øverst til høyre i grensesnittet, og deretter på `Connect Wallet`. Velg `REST (lokalt nettverk)`. Du vil da kunne kopiere en makron med de riktige rettighetene.



![Image](assets/fr/081.webp)



Lim den inn i det tilsvarende feltet i Zeus, og klikk deretter på knappen `SAVE WALLET CONFIG`.



![Image](assets/fr/082.webp)



Du kan nå få tilgang til Lightning-noden din fra Zeus-appen. Det betyr at du kan motta generate-fakturaer for å motta betalinger direkte på Lightning-noden din fra smarttelefonen din, og du kan også betale Lightning-fakturaer uansett hvor du er.



![Image](assets/fr/083.webp)



Tips: Tailscale er ikke begrenset til å bruke Lightning-noden eksternt. Den gir deg tilgang til alle Umbrel-verktøyene fra annen programvare, til og med eksternt. Du kan for eksempel bruke Tailscale-IP-adressen til Umbrel til å koble Bitcoin-noden (via Electrs eller Fulcrum) til Sparrow Wallet, uten å gå gjennom Tor. Igjen, dette unngår tregheten som ligger i Tor. Bare installer Tailscale-klienten på datamaskinen din og koble den til nettverket ditt.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

I neste kapittel skal vi se på en annen, like effektiv måte å koble en mobil klient til Lightning-noden på: Nostr Wallet Connect. Vi skal bruke en annen applikasjon enn Zeus (selv om Zeus også er kompatibel med NWC), nemlig Alby Go.



## Koble til en mobil wallet via NWC


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Hvis du ikke er overbevist av Tailscale-tilkoblingen, eller hvis det virker for vanskelig å administrere et dobbelt VPN, foreslår dette kapittelet en annen måte å bruke en ekstern mobilklient til å betale for og motta sats via Lightning-noden din: ***Nostr Wallet Connect***.



I dette eksemplet bruker vi mobilapplikasjonen Alby Go, som er svært godt utformet og spesielt enkel å lære seg. Når det er sagt, kan du også bruke Zeus eller en annen NWC-kompatibel mobilapplikasjon. Du finner en liste over kompatible applikasjoner på [the `awesome-nwc` GitHub repository](https://github.com/getAlby/awesome-nwc).



### Hvordan fungerer Nostr Wallet Connect?



Nostr Wallet Connect er en standardisert protokoll som gjør det mulig for en applikasjon eller et nettsted å utløse handlinger på en ekstern Lightning-node uten å opprette en direkte nettverkstilkobling til den noden (ingen API LND eksponert, ingen VPN, ingen `.onion`-tjeneste...). NWC definerer hvordan en applikasjon formulerer en intensjon (f.eks. `pay_intece`) og mottar resultatet.



Det fungerer ganske enkelt. Du initialiserer en økt ved å skanne en QR-kode eller via en deeplink `nostr+walletconnect:`. Denne strengen inneholder øktparametrene og en autorisasjonshemmelighet. Når applikasjonen ønsker å betale, serialiserer den forespørselen, krypterer den og publiserer den som en hendelse på et Nostr-relé. Noden leser hendelsen på reléet, dekrypterer den, kontrollerer at forfatteren er autorisert for denne økten, utfører betalingen og returnerer deretter et kryptert svar (suksess med forhåndsbilde eller feil). Reléet fungerer bare som et transportledd: Det kan ikke lese innholdet, men det kan observere tidspunktet og hyppigheten av forespørsler.



Sammenlignet med en tilkobling via Tailscale eller Tor er den største fordelen med NWC at noden din ikke er direkte tilgjengelig fra utsiden. Dette forenkler mobil bruk betraktelig: noden din trenger ikke å akseptere innkommende tilkoblinger, den trenger bare å kunne kommunisere med et relé. På den annen side introduserer du en funksjonell avhengighet av Nostr-reléene: Hvis de ikke er tilgjengelige, blir opplevelsen dårligere. Selv om meldingene er krypterte, kan reléet observere et visst nivå av aktivitetsmetadata.



Forskjellen i sikkerhetsmodeller er også viktig. Med Tailscale eller Tor eksponerer du direkte tilgang til noden din (via API eller LND), beskyttet av svært sensitive hemmeligheter. Dette er kraftig, fordi du kan administrere alt, men det er også en angrepsflate på lavere nivå. Med NWC er tilgangen mer applikativ: Du delegerer en økt token som kun autoriserer visse handlinger.



### Installer Alby Hub på Lightning-noden din



Tidligere fantes det en applikasjon som var spesielt dedikert til NWC-tilkoblinger i Umbrel App Store, men denne er dessverre ikke lenger tilgjengelig. Du må nå bruke Alby Hub for å etablere denne typen tilkobling. For å gjøre dette må du starte med å installere Alby Hub-applikasjonen direkte fra butikken.



![Image](assets/fr/091.webp)



Når du åpner programmet, hopper du over introduksjonsskjermbildene og klikker på knappen `Get Started (LND)`. Det er viktig å sjekke at det står `LND`, og ikke `LDK`, i parentes. Hvis `LND` vises, betyr det at Alby Hub har funnet den eksisterende Lightning-noden din og vil konfigurere seg selv som grensesnitt for den. Hvis `LDK` derimot vises, indikerer dette at Alby Hub ikke har oppdaget noden din og er i ferd med å opprette en ny, noe som ikke er målet her.



![Image](assets/fr/092.webp)



Du vil deretter bli bedt om å opprette en Alby-konto. For bruk begrenset til NWC er dette ikke nødvendig, men det kan være lurt å gjøre det hvis du ønsker å dra nytte av Albys spesifikke tjenester. Hvis ikke, klikker du på `Måskje senere` for å fortsette.



![Image](assets/fr/093.webp)



Velg deretter et sterkt, unikt passord. Dette vil beskytte tilgangen til Alby Hub på noden din. Husk å lagre det i passordbehandleren din.



![Image](assets/fr/094.webp)



Dette bringer deg til Alby Hub-grensesnittet. Du trenger ikke å gå gjennom hele konfigurasjonsprosessen, med mindre du vil bruke den som hovedadministrator for Lightning-noden din. Som vi så tidligere, kan Alby Hub faktisk erstatte bruken av ThunderHub til administrasjon av noden din. Hvis du vil finne ut mer om alternativene i Alby Hub, kan du ta en titt på den dedikerte veiledningen vår:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Gå til menyen `Connections`.



![Image](assets/fr/095.webp)



Her kan du se alle programmene som kan koble seg til Lightning-noden din via NWC. Blant disse er Zeus, som allerede er nevnt i forrige kapittel. Her skal vi bruke Alby Go. Klikk på Alby Go og deretter på knappen `Connect to Alby Go` for å starte tilkoblingsprosessen.



![Image](assets/fr/096.webp)



### Installere og koble til Alby Go



Installer Alby Go-applikasjonen på smarttelefonen din:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



I Alby Hub konfigurerer du rettighetene du ønsker å gi til Alby Go -applikasjonen på Lightning-noden. Du kan for eksempel angi utgiftsgrenser per periode, en utløpsdato for NWC-koblingen eller gi total kontroll. Når du har angitt parameterne, klikker du på knappen `Neste`.



![Image](assets/fr/097.webp)



Alby Hub sender deretter en QR-kode til generate for å opprette NWC-forbindelsen mellom Lightning-noden og Alby Go.



![Image](assets/fr/098.webp)



Når Alby Go-applikasjonen åpnes første gang, klikker du på "Koble til Wallet" og skanner deretter QR-koden som følger med Alby Hub.



![Image](assets/fr/099.webp)



Velg et navn for å identifisere denne wallet. Du har nå ekstern tilgang til Lightning-noden din via Alby Go. Du kan generate fakturaer for å motta sats på noden din, eller sette Lightning-fakturaer direkte med den.



![Image](assets/fr/100.webp)



Jeg sendte for eksempel 1543 sats fra Alby Go-grensesnittet.



![Image](assets/fr/101.webp)



Hvis jeg går til det grunnleggende grensesnittet til Lightning-noden min på Umbrel, kan jeg se at denne betalingen faktisk har blitt utført av noden min.



![Image](assets/fr/102.webp)



Nå vet du hvordan du enkelt kan bruke Lightning-noden din fra hvor som helst.



## Langvarig autonomi på Lightning


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



Vi har nå kommet til slutten av dette praktiske LNP202-kurset. Du har nå det grunnleggende du trenger for å bruke Lightning Network på en suveren måte: Du forstår den virkelige rollen til en node, avveiningene mellom ulike tilnærminger, og du har satt opp en LND-forekomst på Umbrel med en konsekvent strategi for sikkerhetskopiering og beskyttelse. Du har også åpnet dine første kanaler, lært hvordan du håndterer likviditet og gjør betalingene dine pålitelige på daglig basis.



Fra et driftsmessig synspunkt bør noden din nå gå inn i en vedlikeholdsrytme. Det viktigste er å overvåke den (oppetid, synkronisering, kanalstatus, betalingsfeil osv.), bruke oppdateringene som tilbys av Umbrel når stabile versjoner er tilgjengelige, og med jevne mellomrom kontrollere at sikkerhetskopiene og vakttårnkonfigurasjonen fortsatt er aktive.



Når det gjelder kanaler, bør du ha en pragmatisk tilnærming: Behold de kanalene som er nyttige for deg, steng de som er permanent inaktive eller knyttet til ustabile kolleger, og omalloker gradvis kapitalen din mot en mer robust topologi.



**En av de vanligste fallgruvene på dette stadiet er å allokere for mye kapital til Lightning-noden. Husk at Lightning-noden er mye mindre sikker enn en maskinvare-wallet, og at tilgjengeligheten av midler som er avsatt til kanalene dine, er avhengig av sikkerhetskopieringsmekanismer som er ufullkomne. Det er derfor svært viktig å holde seg til rimelige beløp, som du har råd til å miste i tilfelle et problem, og alltid ha mesteparten av sats på en maskinvare-wallet i kjeden.



Når det gjelder verktøy, anbefaler jeg at du er nysgjerrig og oppmerksom på nye utviklinger. I denne opplæringsøkten oppdaget vi flere av dem, enten det gjelder administrasjon av noden din, tilkoblingen eller fjernbruk for å utføre betalinger. Lightning er imidlertid et spesielt dynamisk felt. Hvert år dukker det opp nye og relevante verktøy, og mange nye applikasjoner dukker også opp på Umbrel. Hvis du holder deg oppdatert på denne utviklingen, kan du oppdage kraftigere eller mer praktiske løsninger enn de som er presentert i dette kurset.



Hvis du ikke allerede har gjort det, anbefaler jeg deg på det sterkeste å ta Fanis Michalakis' teorikurs LNP 201, som er viet driften av Lightning Network. Det vil hjelpe deg med å forstå manipulasjonene som utføres i dette LNP202-kurset, og gi deg større selvtillit i den daglige driften av noden din.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

I en annen retning, men like viktig for bitcoin-reisen din, anbefaler jeg også Ludovic Lars' utmerkede kurs om historien bak opprettelsen av Bitcoin.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Men før du går videre, kan du skrive en anmeldelse av dette LNP202-kurset og, selvfølgelig, ta vitnemålet for å bekrefte at du har forstått alt innholdet.



# Siste del


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Anmeldelser og rangeringer


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Avsluttende eksamen


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Konklusjon


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>