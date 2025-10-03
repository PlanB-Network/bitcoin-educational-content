---
name: Sette opp din første Bitcoin-node
goal: Forstå, installere, konfigurere og bruke en Bitcoin-node
objectives: 


  - Forstå rollen til og formålet med en Bitcoin-node.
  - Identifisere de ulike maskinvare- og programvareløsningene som er tilgjengelige.
  - Installer og konfigurer en Full node (Bitcoin core).
  - Bruk Interface Umbrel og legg til nyttige applikasjoner.
  - Koble en personlig Wallet til sin egen node.
  - Utforsk avanserte innstillinger og beste sikkerhetspraksis.


---
# Bli en suveren bitcoiner



Du er sikkert kjent med ordtaket "Ikke dine nøkler, ikke dine mynter", som oppfordrer til å ta vare på bitcoinsene dine selv. Å ha dine egne nøkler er et viktig første skritt, men det er ikke nok. For å oppnå ekte monetær suverenitet må du også installere og bruke din egen Bitcoin-node. Dette kurset er designet for å veilede deg gjennom dette grunnleggende trinnet i din Bitcoin-reise!



BTC 202 er et lett tilgjengelig kurs som er utviklet for å lære deg å spinne din egen Bitcoin-knute, selv om du ikke er en teknisk ekspert. Vi begynner med å definere hva en Bitcoin-knute er, hva den brukes til, og hvorfor det er helt avgjørende å spinne en selv. Deretter guider jeg deg trinn for trinn gjennom valg av maskinvare, installering av nødvendig programvare, tilkobling av Wallet og de første mulige optimaliseringene for å ta den videre.



Å kjøre en Bitcoin-node er ikke bare et alternativ for eksperter; det er en nødvendighet. Det er et motstandsdyktig verktøy som alle brukere må forstå og implementere. Dette kurset er ditt utgangspunkt for å bli en suveren bitcoiner!




+++




# Innledning


<partId>fc46ccd7-5d6d-40c3-9e9f-fbbb323c760a</partId>




## Kursoversikt


<chapterId>916b1f86-38a4-4ede-bdb7-83841d5a7abe</chapterId>



Velkommen til BTC 202, der du lærer hvordan du installerer, konfigurerer og bruker en Bitcoin-node på en enkel og uavhengig måte. Men det er ikke alt: Du vil også lære mer om nodenes plass og funksjon i Bitcoin-systemet. Kurset veksler mellom teoretiske forklaringer og veiledet praktisk øvelse.



### Del 1 - Innledning



I denne første delen av kurset vil vi klargjøre de grunnleggende begrepene, før vi går videre til mer presise definisjoner. Hva er en node? Hva er forskjellen mellom node, Wallet og Miner? Deretter lærer du om Bitcoin core og protokollens implementasjoner. Målet er å snakke samme språk, unngå forvirring og etablere et solid teoretisk grunnlag.



### Del 2 - Å bli en suveren bitcoiner



I denne andre delen begynner jeg med å forklare hvorfor det er viktig å ha sin egen Bitcoin-node. Deretter ser vi nærmere på de ulike typene noder som finnes (komplett, pruned, SPV...), hvordan de fungerer og hvilke tekniske implikasjoner de har.



Deretter gir vi deg en oversikt over programvaren som er tilgjengelig for å kjøre en Bitcoin-node, inkludert fordeler og ulemper. Til slutt kommer vi med noen praktiske anbefalinger om hvordan du velger riktig maskinvare for dine behov og ditt budsjett.



Denne delen illustrerer derfor veien til den suverene bitcoiner: forstå hvorfor det er nødvendig å kjøre en node, velge type node, basert på dette valget, velge programvare, og, avhengig av programvaren som er valgt, bestemme passende maskinvare.



### Del 3 - Enkel installasjon av en Bitcoin-node



Når disse forberedelsene er fullført, er det på tide å gå over til det praktiske med del 3, som handler om Umbrel: operativsystemet for hjemmeskyen som forenkler selvhosting og installasjon av en Bitcoin- og Lightning-node.



Etter en kort introduksjon til Umbrel gir vi deg en detaljert veiledning for å guide deg gjennom installasjons- og konfigurasjonsprosessen på din egen DIY-maskin. Målet med denne delen er klart: å ha din første fullt funksjonelle og synkroniserte Bitcoin-node.



### Del 4 - Koble Wallet til noden din



Nå som du har satt opp en Bitcoin-node, er det på tide å bruke den! I denne delen lærer du hvordan du kobler Wallet-administrasjonsprogramvaren din (som Sparrow wallet) til din egen Address-indekser (Electrs eller Fulcrum), eller direkte til Bitcoin core, slik at du ikke lenger er avhengig av offentlige servere.



Vi ser også på indeksørens rolle og de ulike metodene for å koble til noden din (LAN, Tor, Tailscale, osv.). Til slutt, i det siste kapittelet, går vi gjennom de mest nyttige applikasjonene som er tilgjengelige på Umbrel for den daglige bitcoiner.



### Del 5 - Avanserte konsepter og beste praksis



I denne siste delen av BTC 202 er målet å utdype kunnskapen din. Først skal vi se på hva som er best å gjøre med den nye Bitcoin-noden din, og hvordan du vedlikeholder den på lang sikt.



Deretter tar vi oss tid til å gå gjennom noe av teorien som er gjennomgått tidligere i kurset, blant annet IBD-prosessen og peer discovery i detalj, anatomiutforskningen av en node og til slutt hvordan du bruker filen `Bitcoin.conf` til å finjustere innstillingene dine.



### Del 6 - Siste del



Som med alle Plan ₿ Network-kurs, finner du en avsluttende eksamen i den siste delen for å teste kunnskapen din om Bitcoin-noder.



Er du klar til å slå på din første Bitcoin-node? Sett kurs mot suverenitet!



## Hva er en Bitcoin-node?


<chapterId>0a9fd4e0-94ab-405e-924c-023397393027</chapterId>



Slik skaperen, Satoshi Nakamoto, beskriver det, presenterer Bitcoin seg selv som et elektronisk peer-to-peer-kontantsystem. Denne enkle setningen, som er tittelen på hvitboken, inneholder mange ledetråder til Bitcoins natur:




- For det første beskriver Satoshi Bitcoin som et "system", med andre ord et sammenhengende sett med maskinvare- og programvarekomponenter som samhandler for å levere en bestemt tjeneste eller utføre en bestemt funksjon;
- Deretter forklarer han at dette systemet muliggjør bruk av elektroniske kontanter, altså en form for immateriell valuta;
- Til slutt påpeker han at dette systemet ikke er avhengig av noen sentral enhet: Det er "peer-to-peer", det vil si at det er brukerne selv som driver systemet.



Siden Bitcoin er et system, må det nødvendigvis kjøres på datamaskiner. Og på grunn av dets peer-to-peer-karakter er det brukerne selv som tar ansvar for å drive disse maskinene. Det vi kaller en "Bitcoin-node" er nettopp den datamaskinen som programvaren som implementerer Bitcoin-protokollen (som Bitcoin core, men det kommer vi tilbake til senere) kjører på. Det er dette som gjør at Bitcoin kan operere uten en sentral autoritet: Valideringen utføres på en distribuert måte, av tusenvis av uavhengige maskiner som tilhører tusenvis av brukere.



![Image](assets/fr/047.webp)



Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Det er nettopp disse brukerne som sørger for Bitcoins sikkerhet. Som Eric Voskuil forklarer i boken *Cryptoeconomics*, er sikkerheten til Bitcoin verken avhengig av Blockchain, hashingkraft, validering, desentralisering, kryptografi, åpen kildekode eller spillteori. Sikkerheten til Bitcoin avhenger først og fremst av individene som er villige til å utsette seg for personlig risiko. Desentralisering gjør det mulig å spre denne risikoen på et stort antall individer, og det er bare deres evne til å stå imot som sikrer systemets robusthet.



Dette prinsippet er lett å forstå: Hvis Bitcoin var avhengig av én enkelt node eid av én enkelt person, ville det være nok å fengsle denne personen for å stenge nettverket, siden vedkommende alene ville påta seg all risiko. Med titusenvis av noder spredt over hele verden er risikoen spredt: Hver av disse operatørene må nøytraliseres for å stenge ned Bitcoin.



![Image](assets/fr/048.webp)



Vi kan dermed skille ut og navngi flere begreper for å klargjøre ting for resten av dette kurset:




- Bitcoin-valuta: den regningsenheten som brukes for transaksjoner i dette systemet;
- Bitcoin-nettverket: mengden av alle tilkoblede noder;
- Bitcoin-noder: maskiner som kjører en implementering av Bitcoin;
- Bitcoin-implementeringer: programvare som oversetter protokollen til kjørbare instruksjoner;
- Bitcoin-protokoll: settet med regler som styrer systemets drift;
- Bitcoin-systemet: den sammenhengende kombinasjonen av alle disse Elements.



### Bitcoin-knutepunktets rolle



Bitcoin-nodene danner til sammen det som kalles Bitcoin-nettverket. De gjør det mulig for hele systemet å operere autonomt, uten å måtte forholde seg til en sentral autoritet eller et hierarki av servere.



Fra starten av ble Bitcoin utviklet for at hver bruker skulle kunne kjøre en personlig node. Dette gjelder fortsatt med dagens Bitcoin core-programvare, som kombinerer rollene som Wallet og node. Men i dag er denne funksjonen ofte adskilt: Mange moderne Bitcoin-lommebøker er bare lommebøker som kobles til eksterne noder (eid av samme person eller ikke).



### Behold Blockchain



Den første oppgaven til en node er å vedlikeholde en lokal kopi av Blockchain. For å forhindre Double-spending på Bitcoin uten å involvere en sentral autoritet, må hver bruker kontrollere at det ikke finnes noen transaksjon i systemet. Den eneste måten å være sikker på dette på, er å kjenne til alle transaksjonene som er gjort på Bitcoin. Derfor er alle transaksjoner tidsstemplet og gruppert i blokker, og hver node lagrer hele Blockchain.



> Den eneste måten å bekrefte fraværet av en transaksjon på, er å være klar over alle transaksjoner.

Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Blockchain er derfor et register i utvikling: Hver gang en ny blokk publiseres av en Miner, sjekker noden dens gyldighet før den legges til i sin egen lokale kopi av kjeden. Per i dag (juli 2025) er hele Blockchain på mer enn 675 GB, og denne størrelsen fortsetter å vokse ettersom en ny blokk legges til i gjennomsnitt hvert tiende minutt.



![Image](assets/fr/049.webp)



Noden har også en lokal oversikt over alle UTXO-er som finnes til enhver tid, kjent som **UTXO-settet**. Denne databasen inneholder alle de ubrukte Bitcoin-fragmentene. Vi kommer tilbake til dette emnet i detalj i siste del av kurset.



### Verifisere og distribuere transaksjoner



Den andre rollen en node har, er å sørge for verifisering og videreformidling av transaksjoner. Når en ny transaksjon når noden (enten via Wallet-programvaren eller en annen node), kontrollerer den at den er i samsvar med et sett regler (konsensusregler og reléregler). For eksempel




- brukte bitcoins må finnes i UTXO-settet (databasen med ubrukte utganger);
- signaturen må være gyldig, og alle utgiftsbetingelser må være oppfylt (gyldig skript);
- den totale mengden output må ikke overstige den totale mengden input, noe som betyr at kostnadene ikke kan være negative.



![Image](assets/fr/050.webp)



Etter validering lagres transaksjonen i nodens Mempool, et midlertidig minneområde som er reservert for ubekreftede transaksjoner, og videresendes deretter til de andre nettverksmotpartene som den er koblet til. Denne distribusjons- og valideringsmekanismen fortsetter fra node til node. På denne måten forplantes transaksjonen på tvers av Bitcoin-nettverket, og hver node lagrer den i Mempool til den blir inkludert i en gyldig blokk av en Miner, som deretter handler på den første bekreftelsen.



### Kontrollere og distribuere blokker



Nodens tredje rolle er å administrere utvunnede blokker. Når en Miner oppdager en ny blokk med en gyldig Proof of Work, sendes den ut i nettverket. Nodene mottar den, kontrollerer at den er i samsvar med alle protokollreglene og integrerer den i sin egen lokale kopi av Blockchain hvis den er gyldig. På samme måte som med transaksjoner, blir nyvaliderte blokker sendt videre til alle andre noder som er koblet til noden. Denne prosessen fortsetter til alle nodene i Bitcoin-nettverket er klar over den nye blokken.



![Image](assets/fr/051.webp)



## Hva er forskjellen mellom en bue og en Wallet?


<chapterId>de5af634-a628-4b90-b869-468c208e178b</chapterId>



Det er viktig å skille mellom to forskjellige typer programvare når du bruker Bitcoin: noden og Wallet.



En Bitcoin-node er, som nevnt ovenfor, en programvare som deltar aktivt i peer-to-peer-nettverket. Den utfører tre hovedoppgaver:




- backup av Blockchain,
- validering og videreformidling av transaksjoner,
- blokkvalidering og videresending.



En Bitcoin Wallet er derimot en programvare som er designet for å lagre og administrere de private nøklene dine. Disse nøklene gjør det mulig for deg å bruke bitcoins ved å tilfredsstille låseskriptene (vanligvis gjennom en signatur). En Wallet kan koble seg til en node (enten den er lokal eller ekstern) for å se statusen til Blockchain og kringkaste transaksjonene den bygger, men den er ikke som sådan en deltaker i nettverket.



I noen tilfeller kan disse to funksjonene sameksistere i samme programvare, slik tilfellet er med Bitcoin core, som fungerer som både en Full node og en Wallet. Mange populære Wallet-programmer (Sparrow, BlueWallet osv.) krever imidlertid en tilkobling til en ekstern node (enten det er din egen eller en tredjeparts) for å kringkaste transaksjoner og bestemme Wallet-saldoen.



![Image](assets/fr/052.webp)



## Hva er forskjellen mellom en node og en Miner?


<chapterId>d2992614-7ab7-4bf9-81b1-f548cda67257</chapterId>



Begrepene node og Miner forveksles ofte. Likevel har disse to Elements radikalt forskjellige funksjoner i systemet.



Da Bitcoin ble lansert av Satoshi Nakamoto i 2009, var det forventet at alle brukere skulle delta i nettverket som en helhet. Dermed kombinerte den opprinnelige Bitcoin-programvaren flere funksjoner samtidig: Den fungerte som en Wallet, en node, og også som en Miner, som var i stand til å generere nye blokker. På den tiden var vanskelighetsgraden til Mining veldig lav. Alt du trengte å gjøre var å kjøre Bitcoin-programvaren på datamaskinen din for å finne blokker og motta bitcoins som belønning.



Men med den gradvise populariseringen av Bitcoin og økningen i antall gruvearbeidere, har konkurranselandskapet i Mining gjennomgått et radikalt skifte. I dag har Mining blitt en ekstremt konkurranseutsatt aktivitet, dominert av industrielle aktører utstyrt med spesialisert infrastruktur. Kraften som kreves for å utvinne en ny blokk, er nå så stor at det er praktisk talt umulig for en enkelt bruker å oppnå dette ved hjelp av bare en vanlig datamaskin. Derfor utføres Mining nå primært ved hjelp av spesialiserte maskiner som kalles ASICs (*Application-Specific Integrated Circuits*). Disse brikkene er optimalisert utelukkende for å kjøre dobbel SHA-256, algoritmen som brukes for Mining på Bitcoin.



![Image](assets/fr/053.webp)



I møte med denne utviklingen har rollene til Bitcoin-noden og Miner-noden blitt klart forskjellige. Som vist ovenfor, er rollen til en Bitcoin-node rent informasjons- og valideringsbasert. Miner-noden har en annen rolle:




- Den velger ventende transaksjoner i Mempool.
- Den bygger en kandidatblokk som integrerer disse transaksjonene.
- Han prøver seg frem for å finne en gyldig Proof of Work.
- Hvis den finner et gyldig bevis, sender den blokken via sin egen node til de andre nodene.



En Miner trenger en Bitcoin-node for å samhandle med nettverket.



Rollen til Miner skilles også noen ganger fra rollen til hakkeren. En hakker er en maskin som har som oppgave å Hash malblokker levert av en pool-server, på jakt etter hasher som tilfredsstiller vanskelighetsmålet som er definert for aksjer, og ikke Bitcoin. Resten av Mining-prosessen, som inkluderer faktisk blokkkonstruksjon, transaksjonsvalg eller Proof-of-Work-søk i henhold til Bitcoins egen vanskelighetsgrad, samt distribusjon, utføres direkte av poolene.



![Image](assets/fr/054.webp)



Til slutt er det en viktig forskjell mellom Miner og noden når det gjelder økonomiske insentiver. Å drive en Bitcoin-node gir ingen direkte økonomiske fordeler. På den annen side gir deltakelse i Mining belønning (subsidier og transaksjonsgebyrer) for hver blokk som blir funnet.



I del 2 skal vi se nærmere på de praktiske og personlige fordelene ved å installere og bruke en Bitcoin-node, utover de rent økonomiske.



## Bitcoin core og protokollimplementeringer


<chapterId>72381876-9317-4faa-8d41-2b252a945b8a</chapterId>



Bitcoin-protokollen er ikke programvare: Den er et sett med stilltiende regler som deles mellom nettverksbrukere. Den definerer transaksjonsgyldighetsbetingelser, mekanismer for opprettelse av penger, blokkformat, Proof-of-Work-betingelser og mange andre spesifikasjoner. For å samhandle med denne protokollen må brukerne kjøre programvare som implementerer disse reglene: dette kalles en **implementering** av Bitcoin.



En implementering er derfor nodeprogramvare: et program som kan samhandle med andre maskiner i Bitcoin-nettverket, laste ned, verifisere, lagre og spre blokker og transaksjoner, og lokalt håndheve konsensus- og reléregler. Hver implementering er en konkret tolkning av protokollen, skrevet i et gitt programmeringsspråk, med sin egen arkitektur, ytelse og ergonomi. Hver implementering vil også ha sin egen utviklingsorganisasjon, med sin egen ansvarsfordeling.



Blant disse implementeringene er det én som dominerer stort: **Bitcoin core**.



![Image](assets/fr/055.webp)



### En historisk implementering som har blitt en referanse



Bitcoin core er referanseprogramvaren for Bitcoin-protokollen. Den er avledet fra den opprinnelige koden skrevet av Satoshi Nakamoto i 2008-2009, og er en direkte videreføring av den. Opprinnelig kjent som "*Bitcoin*", deretter "*Bitcoin QT*" (på grunn av tillegget av en grafisk Interface via Qt-biblioteket), ble den omdøpt til "*Bitcoin core*" i 2014 for å skille programvaren tydelig fra nettverket. Siden versjon 0.5 har den blitt distribuert med to komponenter: `Bitcoin-qt` (den grafiske Interface) og `bitcoind` (kommandolinje-Interface).



I teorien representerer ikke Bitcoin core Bitcoin-protokollen, men er bare én implementering blant mange. Den utmerker seg imidlertid ved at den har fått stor utbredelse, er gammel, har en robust kode og en grundig utviklingsprosess. I praksis er derfor reglene som brukes av Bitcoin core, de facto de samme som i Bitcoin-protokollen: brukere, utviklere, utvinnere og økosystemtjenester refererer nesten utelukkende til den.



### Nåværende fordeling av implementeringer



Ifølge [data samlet inn i august 2025 av Luke Dashjr](https://luke.dashjr.org/programs/Bitcoin/files/charts/software.html) (en velkjent utvikler i økosystemet) er fordelingen av implementeringer blant nettverkets offentlige noder som følger:




- Bitcoin core**: 87.3 % av nodene
- Bitcoin Knots**: 12.5
- Andre kumulative implementeringer**: 0.2 % (btcsuite, Bcoin, BTCD ...)



![Image](assets/fr/056.webp)



Med andre ord kjører rundt 9 av 10 offentlige noder Bitcoin core. Resten av nettverket er avhengig av mer marginale klienter (selv om Knots' andel har økt kraftig de siste månedene, ikke minst i kjølvannet av debattene om størrelsesgrensen på `OP_RETURN`). Disse alternative implementeringene vedlikeholdes ofte av en enkelt person eller et lite team.



**Disse tallene er imidlertid fortsatt estimater, ettersom de først og fremst er basert på *lyttende noder*, dvs. noder som godtar innkommende tilkoblinger (med port 8333 åpen). Ikke-lyttende noder* er mye mer komplekse å telle, siden det er umulig å koble seg direkte til dem: Du må vente på at initiativet kommer fra dem, i form av en utgående tilkobling. Luke Dashjrs nettsted hevder å prøve å telle disse *ikke-lyttende nodene* også, men det er fortsatt umulig å få helt nøyaktige data om dem, og oppdateringen av denne statistikken henger uunngåelig etter virkeligheten.



### Intern drift av Bitcoin core



Bitcoin core er skrevet i C++. Det er også et åpen kildekode-prosjekt som vedlikeholdes av et fellesskap av utviklere som jobber frivillig eller blir betalt av ulike enheter (ofte av selskaper i økosystemet som har en egeninteresse i utviklingen av Core). [Koden ligger på GitHub] (https://github.com/Bitcoin/Bitcoin), og utviklingen følger en streng plan:




- Bidragsytere** sender inn forslag i form av _pull requests_ (PR). I prinsippet kan hvem som helst foreslå en endring, men den må testes, dokumenteres og gå gjennom en fagfellevurderingsprosess.
- **Vedlikeholderne** har rett til å godkjenne og slå sammen PR-er. Det er de som garanterer sammenhengen og stabiliteten i prosjektet. I juli 2025 er det fem av dem: Hennadii Stepanov, Michael Ford, Andrew Chow, Gloria Zhao og Ryan Ofsky.
- Det har ikke vært noen **hovedvedlikeholder** siden februar 2023. Denne rollen ble først innehatt av Satoshi Nakamoto ved lanseringen av Bitcoin, deretter av Gavin Andresen etter Nakamotos avgang tidlig i 2011, og til slutt av Wladimir J. Van Der Laan fra 2014 til 2023.



![Image](assets/fr/057.webp)



Utviklingen av Bitcoin core følger en meritokratisk logikk: Nye bidragsytere oppfordres til å gå gjennom og teste koden før de selv foreslår endringer. Beslutninger er basert på teknisk konsensus, og større endringer (spesielt på områder der det er konsensus) krever oppstrømsdiskusjoner på offentlige kanaler, for eksempel postlister eller PR-gjennomgangsklubber.



### Andre Bitcoin-implementeringer



Selv om de er marginale når det gjelder adopsjon, finnes det andre klienter. Den viktigste er Bitcoin Knots, utviklet av Luke Dashjr, en Fork av Bitcoin core som inneholder flere alternativer og en mer konservativ tilnærming til utvikling. Disse inkluderer strengere restriksjoner på transaksjonsformater.



![Image](assets/fr/058.webp)



Vi kan også nevne:




- Libbitcoin**: et modulært C++-bibliotek utviklet av Amir Taaki og vedlikeholdt av Eric Voskuil;
- Bcoin**: en JavaScript-implementasjon som ikke lenger vedlikeholdes aktivt;
- BTCD/btcsuit**e: en implementering i Go.



Disse prosjektene bidrar til mangfoldet i økosystemet, men de blir i svært begrenset grad tatt i bruk, noe som gjør det vanskelig for Bitcoin core å utvikle seg uavhengig.



### Kraften til Core-utviklere



Du tror kanskje at Bitcoin core-utviklerne har direkte kontroll over Bitcoin, men det er ikke tilfelle. De kan ikke pålegge en endring i protokollen. Deres rolle er å foreslå kode. Det er opp til hver enkelt bruker, via noden sin, å bestemme om de vil bruke denne koden eller ikke.



Dette betyr at hvis en endring i Bitcoin core ikke oppnår konsensus, kan nodene ignorere den, enten ved ikke å oppdatere Bitcoin core eller ved ganske enkelt å endre implementasjonen. Hvis en funksjon som brukerne ønsker, blir blokkert i Core-utviklingsprosessen, er det derimot alltid mulig å bytte til en annen implementering eller Fork prosjektet.



Som vi skal diskutere senere i dette kurset, er det nodene, i henhold til deres økonomiske vekt (dvs. kjøpmennene), som gir nytteverdi til en versjon av protokollen (og dermed til den tilsvarende valutaen) ved å akseptere enheter som respekterer dens regler. Den reelle styringsmakten over Bitcoin ligger derfor hos disse kjøpmennene, ikke hos utviklerne.




# Bli en suveren bitcoiner


<partId>df64cad2-e92d-4949-9cca-14394aad0bc6</partId>




## Hvorfor vri din egen knute?


<chapterId>39c0cd19-67f9-4c64-bfb3-dbd6eec0bf42</chapterId>



Det er en utbredt oppfatning at det å drive en Bitcoin-node er en rent altruistisk handling, uten personlig vinning, utelukkende i desentraliseringens tjeneste. Noen anser det som en form for plikt for bitcoinere å støtte systemet og vise sin takknemlighet til Bitcoin.



Som vi har påpekt i de foregående kapitlene, er det ingen direkte økonomisk gevinst ved å spinne en knute. Man skulle derfor tro at det ikke er noen personlig interesse i å gjøre det. Likevel er det mange personlige fordeler ved å drive sin egen knute. For å overbevise deg om dette skal jeg i dette kapittelet presentere alle grunnene, både tekniske og strategiske, til hvorfor du bør installere og bruke din egen Bitcoin-node.



### Mer konfidensiell formidling av transaksjoner



Når Wallet-programvaren kobler seg til en ekstern node, overfører den transaksjonene til en infrastruktur som ikke er under din kontroll. Dette medfører en åpenbar risiko for overvåking: Operatøren av den eksterne noden kan analysere detaljene i transaksjonene dine, inkludert beløp og frekvenser, og ved å kryssjekke visse metadata (som IP-adresser, tidspunkter og steder) kan de potensielt knytte dem til identiteten din.



Som påpekt i et tidligere kapittel kommuniserer ikke lommebøker med Bitcoin-nettverket ved hjelp av magi; de må koble seg til en node for å kunne konsultere saldoer eller kringkaste transaksjoner. Hvis du aldri har satt opp din egen node, betyr dette at din Wallet er avhengig av infrastrukturen til en tredjepart (vanligvis selskapet som står bak programvaren). Denne tredjeparten, spesielt hvis det er et selskap, kan observere, utnytte eller til og med avsløre disse dataene: enten det er av kommersielle grunner, under juridiske begrensninger eller som et resultat av piratkopiering.



![Image](assets/fr/059.webp)



Ved å bruke din egen node sender du transaksjonene dine direkte til nettverket, uten mellomledd. Forutsatt at du sikrer noden din på riktig måte (som vi skal diskutere senere) eller overholder visse standarder, blir ingen informasjon eksponert: Verken din IP Address eller detaljene i transaksjonene dine passerer gjennom en enhet du ikke kontrollerer. Dette er en grunnleggende forutsetning for å bevare konfidensialiteten din på Bitcoin.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Ikke-kvotepliktige transaksjoner



Av de samme grunnene som er nevnt ovenfor, er Wallet-programvare basert på en tredjepartsnode sårbar for sensurrisiko: Operatøren av den eksterne noden kan nekte å videresende visse transaksjoner av ulike årsaker. De kan anse dem som mistenkelige eller i strid med egne retningslinjer. Transaksjonen kan også bli blokkert hvis den ikke er i samsvar med nodens regler for videreformidling. Til slutt kan operatøren spesifikt rette seg mot din IP Address for å blokkere kringkastingen av transaksjonene dine.



Ved å bruke din egen node sikrer du derimot spredningen av transaksjonene dine i peer-to-peer-nettverket. Dette betyr at du beholder full kontroll over distribusjonen av transaksjonene dine, uten å være avhengig av et mellomledd. Så lenge transaksjonen er i samsvar med konsensus- og videresendingsreglene til nodene som er koblet til din node, vil den bli kringkastet i nettverket og deretter, forutsatt at tilstrekkelige avgifter er inkludert, integrert i en blokk av en Miner. Å ha din egen node garanterer nøytral, tillatelsesfri bekreftelse av transaksjonene dine.



### Uavhengig dataverifisering



Uten en personlig node er du avhengig av en tredjepart for å få tilgang til informasjon, for eksempel Address-saldoen din, status for transaksjonsbekreftelse og blokkens gyldighet. Dette innebærer implisitt tillit til nøyaktigheten og integriteten til den eksterne noden.



![Image](assets/fr/060.webp)



Når du kjører en Full node, kan du kontrollere alle protokollreglene selv, for hver transaksjon og hver blokk. Resultatet er at saldoen som vises på din Wallet ikke er data som mottas fra en ekstern server, men et resultat som beregnes lokalt fra en komplett kopi av Blockchain, validert blokk for blokk. Denne tilnærmingen gir full mening til bitcoiners' maksime:



> Ikke stol på, bekreft.

### Bedre fordeling av systemsikkerhet



Hver node som slutter seg til nettverket, styrker Bitcoins redundans og robusthet. Det gjør det lettere å spre informasjon og gjør det mulig for nye peers å koble seg til hverandre. Uten nodene ville systemet rett og slett vært ubrukelig.



Som vi har sett, er ikke Bitcoins sikkerhet basert på desentralisering, Mining eller kryptografi: Som med alle andre systemer er den avhengig av enkeltpersoner. Mer presist avhenger det av nodeoperatørenes evne til å motstå tvang.



Det som kjennetegner desentraliserte systemer som Bitcoin, er fordelingen av risiko mellom alle som er involvert i driften. Når du driver din egen Bitcoin-node, aksepterer du en del av denne risikoen ved å sørge for sikkerheten til din egen instans, og på den måten letter du også risikobyrden for andre nodeoperatører.



Det er altså ikke en direkte personlig fordel: Det å drive en node gjør deg delvis ansvarlig for sikkerheten i nettverket. Fremfor alt er det en kollektiv fordel, fordi ditt engasjement bidrar til å spre risikoen. I sin tur øker du din egen evne til å bruke Bitcoin på en pålitelig måte.



### Få en dypere forståelse av systemet



Installasjon av en Full node er ingen triviell operasjon. Det innebærer å installere programvare, forstå grunnleggende drift, overvåke synkronisering, undersøke logger i tilfelle problemer og til og med bruke terminalen. Dette vil nødvendigvis føre til at du får en dypere forståelse av protokollen. Dette er en indirekte, men ikke ubetydelig fordel.



Å tilegne seg denne kunnskapen styrker tilliten til verktøyet og kan redusere risikoen for å gjøre feil eller bli utsatt for svindel. Å spinne sin egen knute er også en form for læring.



### Velge hvilke regler som skal gjelde



Et viktig aspekt, som ofte blir misforstått, er at du kan velge hvilke regler du vil bruke lokalt. Det finnes to hovedtyper av regler:





- Konsensusregler**:



Dette er de grunnleggende reglene i Bitcoin-protokollen, som sikrer systemets integritet og fastsetter kriteriene for validering av transaksjoner og blokker. Transaksjoner som ikke overholder disse konsensusreglene, kan aldri inkluderes i en gyldig blokk. For eksempel vil en transaksjon med en ugyldig signatur på en av oppføringene systematisk bli ekskludert.



Å endre disse reglene er det samme som å endre protokollen, og dermed valutaen (Hard Fork). Men selv om man ikke prøver å endre dem, gir det enkle faktum at de eksisterende reglene anvendes strengt, en viss makt: Hvis en blokk bryter med reglene, avviser noden den umiddelbart.





- Stafettregler**:



Dette er regler som er spesifikke for hver Bitcoin-node, og som legges til konsensusreglene for å definere strukturen til ubekreftede transaksjoner som aksepteres i Mempool og videresendes til motparter. Hver node konfigurerer og bruker disse reglene lokalt, noe som forklarer hvorfor de kan variere fra node til node. De gjelder bare for ubekreftede transaksjoner: En transaksjon som anses som "ikke-standard" av en node, vil bare bli akseptert hvis den allerede finnes i en gyldig blokk. Endring av disse reglene ekskluderer ikke noden fra Bitcoin-systemet.



For eksempel er en transaksjon uten gebyrer, i henhold til konsensusreglene, helt gyldig, men den vil bli avvist som standard i henhold til Bitcoin core-relépolitikken, fordi parameteren `minRelayTxFee` er satt til `0,00001` (i BTC/kB). Det er imidlertid mulig, på din egen node, å senke denne terskelen for å videresende transaksjoner med lavere gebyrer, eller omvendt å øke grensen, for eksempel til 2 Sats/vB, for å unngå å videresende transaksjoner med lave gebyrer.



Å spinne sin egen node betyr å hevde: "Jeg validerer det jeg velger å validere, i henhold til de reglene jeg selv har vedtatt"*. Du blir dermed en aktør i styringen av systemet, og kan avvise en utvikling som virker uakseptabel for deg, eller godkjenne en oppdatering i henhold til dine egne kriterier.



Så vi kan raskt prøve å forstå hvor mye makt du har over reglene takket være noden din. Og omfanget av denne makten vil avhenge av regeltypen.



#### For stafettregler



Når det gjelder regler for videreformidling, er det essensielle rett og slett å eie en node, uavhengig av dens økonomiske aktivitet. Det som står på spill her, er hvorvidt du godtar å videreformidle visse typer transaksjoner eller ikke.



Hvis du for eksempel mener at transaksjoner med gebyrer på mindre enn 1 sat/vB bør aksepteres på Bitcoin, kan du justere denne regelen på noden din slik at den kringkaster disse transaksjonene, og dermed legger til rette for at de sprer seg i nettverket til en Miner til slutt inkluderer dem i en gyldig blokk. I bunn og grunn handler det altså om makt over spredningen av transaksjoner: Hver node har beslutningsmakt, siden det å godta å videresende en type transaksjon er ensbetydende med å fremme aksept av den i Bitcoin-nettverket. Hvis du driver flere noder, har du derfor større innflytelse over videresendingspolicyen, ettersom hver node har sine egne forbindelser og påvirkningsområder i nettverket.



Når en eller flere noder er konfigurert med spesifikke regler for videreformidling, betyr det at man bestemmer hvilken del av nettverket som aksepterer å spre en gitt type transaksjon. Spredning av en melding i en peer-to-peer-graf, slik tilfellet er for Bitcoin-transaksjoner, følger logikken i perkolasjonsteorien. Se for deg hver node som et sted som kan være aktivt (`p` = det videreformidler) eller inaktivt (`1-p`). Så snart andelen `p` krysser en kritisk terskel (`p_c`), oppstår det en gigantisk komponent: Transaksjonen klarer å krysse nettverket og har alle muligheter til å nå en Miner. I et nettverk som Bitcoin, der hver node i gjennomsnitt har åtte utgående forbindelser, er `p_c`-terskelen vanligvis satt til bare noen få prosent, og enda lavere hvis noen noder har svært mange forbindelser.



![Image](assets/fr/061.webp)



Så lenge `p` er under `p_c`, forblir en transaksjon begrenset til isolerte lommer og når ikke en Miner. Så snart denne terskelen overskrides, sprer den seg nesten umiddelbart gjennom hele nettverket.



Til syvende og sist er det alltid utvinnerne som bestemmer om en transaksjon skal inkluderes i en blokk eller ikke. Nodene griper imidlertid inn oppstrøms ved å påvirke distribusjonen av transaksjoner: De avgjør om utvinnerne får kjennskap til en gitt transaksjon eller ikke. Hvis en transaksjon ikke blir videresendt til utvinnerne, er det selvsagt umulig for dem å inkludere den i en blokk.



Å legge til noen flere noder vil derfor bare ha en marginal innvirkning hvis nettverket allerede er i perkolasjonsfasen for en gitt type transaksjon, men det kan vise seg å være avgjørende når perkolasjonsterskelen nærmer seg. Å eie eller påvirke flere noder, spesielt hvis de har gode forbindelser, kan øke eller redusere verdien av `p` og dermed indirekte styre reléreglene som avgjør hvilke transaksjoner som blir sett og til slutt akseptert av utvinnerne.



#### For konsensusregler



Når det gjelder din nodes innflytelse på konsensusreglene, er det først og fremst dens økonomiske vekt som vil være avgjørende. Dette er et avgjørende konsept: verdien av enhver valuta er direkte relatert til dens evne til å legge til rette for Exchange. Hvis et objekt ikke aksepteres av noen i Exchange for varer eller tjenester, har det i teorien ingen monetær nytteverdi. Hvis for eksempel ingen kjøpmann aksepterer småstein som betalingsmiddel, har de ingen nytte som penger. Selvfølgelig er nytte et subjektivt begrep på en individuell skala, men jo flere kjøpmenn som aksepterer en gjenstand som betalingsmiddel i et gitt territorium, desto mer sannsynlig er det at gjenstanden har en monetær nytteverdi for menneskene som bor i dette territoriet.



La oss ta et eksempel med en landsby der mange kjøpmenn aksepterer gull i Exchange for varer: Sjansen er stor for at gull har en monetær nytteverdi for landsbyboerne. Dette indikerer at nytten av en valuta avhenger direkte av kjøpmennenes beslutning om å akseptere eller avvise den.



Dette konseptet er avgjørende for å forstå maktdynamikken i Bitcoin-systemet. Satoshi gjør det klart: Bitcoin er et elektronisk kontantsystem; med andre ord tilbyr det en tjeneste som tilbyr en form for valuta, Bitcoin (eller BTC). Når protokollreglene endres på en måte som ikke er bakoverkompatibel (Hard Fork), er dette det samme som å skape et nytt system og dermed en ny valuta. Hvor vellykket eller mislykket denne Fork blir, avhenger av størrelsen på økonomien, som igjen bestemmes av hvor mange kjøpmenn som aksepterer denne nye formen for valuta.



![Image](assets/fr/062.webp)



La oss ta et eksempel: La oss anta at Bitcoin lider en Hard Fork. Det vil da være to forskjellige former for valuta: BTC-1 (den opprinnelige, uforandrede versjonen) og BTC-2 (den nye valutaen med andre konsensusregler). Hvis alle kjøpmenn som aksepterte BTC-1 fortsetter å gjøre det, men avviser BTC-2, vil sistnevnte i teorien ha svært begrenset monetær nytteverdi. Som bruker ville jeg ikke ha noen interesse av å beholde og bruke BTC-2, vel vitende om at ingen kjøpmenn ville ønske å bruke den i Exchange for varer eller tjenester. Omvendt, hvis 50 % av kjøpmennene velger å akseptere BTC-2 utelukkende, og de resterende 50 % bare tar BTC-1, vil nytten av BTC-1 i teorien ha halvert seg. Jeg bruker uttrykket "i teorien" fordi nytten forblir subjektiv på individnivå og avhenger av en rekke faktorer (som territorium og forbruksvaner) som er vanskelige å forstå fra sak til sak.



På Bitcoin inkluderer rollen som "kjøpmann", forstått som enhver enhet med en viss økonomisk vekt, selvfølgelig virksomheter (fysiske butikker, nettbaserte salgssider, tjenesteleverandører osv.), men også Exchange-plattformer, siden de godtar Bitcoin i Exchange for andre valutaer, og utvinnere, siden de godtar Bitcoin via gebyrer i Exchange for tjenesten med å inkludere en transaksjon i en blokk.



Når det gjelder konsensusreglene, lar noden din deg styre den økonomiske aktiviteten din mot den ene eller andre valutaen. Hvis du for eksempel har 10 fulle noder hjemme, men ingen betydelig økonomisk aktivitet, vil innflytelsen din under en Fork være nesten lik null. En enkelt node som brukes til å administrere en kjede med 200 butikker som aksepterer Bitcoin, gir derimot betydelig økonomisk tyngde.



Det er altså ikke antallet noder som betyr noe, men betydningen av den økonomiske aktiviteten de støtter. Hvis den økonomiske aktiviteten din er avhengig av en node du ikke kontrollerer, er det eieren av noden som bestemmer hvilken valuta du skal bruke, så lenge du er koblet til den. Derfor er det å drive og bruke din egen node spesielt viktig i forbindelse med systemstyring:



> Ikke din knute, ikke dine regler.


## De ulike typene Bitcoin-noder


<chapterId>be8f0baa-41f2-4b54-b011-092f4ccc93aa</chapterId>



En Bitcoin-node er derfor en maskin som kjører en implementering av Bitcoin-protokollen. Bak denne felles definisjonen av noder finnes det flere mulige konfigurasjoner, og ikke alle gir samme grad av autonomi, ressursforbruk og nytteverdi for nettverket. I dette kapittelet skal vi forsøke å forstå disse forskjellene, slik at du kan velge en nodearkitektur som passer til dine bruksområder og maskinvarebegrensninger.



### Den komplette knuten



En Full node er ganske enkelt en Bitcoin-node som laster ned hele Blockchain fra Genesis-blokken, validerer hver blokk uavhengig, og lagrer historikken til alle Blockchain lokalt. Dette er den "normale" formen for en Bitcoin-node, slik Satoshi Nakamoto forestilte seg den.



![Image](assets/fr/063.webp)



Full node trenger ikke å stole på noen, fordi den validerer og kjenner all informasjonen i systemet. Det er den typen node som gir deg flest garantier: Du vet, uten å stole på en tredjepart, om en betaling er gyldig, om en blokk er gyldig, om en omorganisering er legitim, og så videre.



I praksis krever en Full node ikke ubetydelige ressurser, inkludert flere hundre gigabyte for blokkfiler, en prosessor som kan validere skript, RAM for Mempool og cacher, og stabil båndbredde. Den første synkroniseringen (*IBD*) leser og verifiserer hele historikken: Det er intensivt, men skjer bare én gang. En Full node deltar aktivt i nettverket, videresender blokker og transaksjoner, og kan ta imot innkommende tilkoblinger for å hjelpe andre peers.



Avhengig av behovene dine kan du legge til en indekserer i Full node. Bitcoin core tilbyr transaksjonsindeksering som en valgfri funksjon (deaktivert som standard), noe som kan være nyttig for spesifikke formål. Den inkluderer imidlertid ikke en Address-indekser, som ofte er den mest etterspurte funksjonen for individuelle brukere. For å bøte på dette kan du installere dedikert programvare på noden din, for eksempel Electrs eller Fulcrum, for å øke hastigheten på Address-balanseverifiseringsspørringer fra tilknyttede UTXO-er. Vi kommer tilbake til indeksererens rolle i mer detalj i et eget kapittel.



### pruned-knuten



pruned-noden validerer alt som en Full node, fra Genesis-blokken til hodet av kjeden med mest arbeid, men **beholder bare den nyeste delen av blokkfilene**. Når de gamle blokkene har blitt sjekket, slettes de gradvis for å holde seg under en plassgrense du kan angi. Denne konfigurasjonen er ideell hvis du har begrenset diskplass: Du beholder uavhengigheten til blokkvalidering, uten å lagre hele Blockchain-historikkarkivet. Dette alternativet er spesielt nyttig hvis du bare ønsker å installere Bitcoin core på din personlige datamaskin, uten å bruke en dedikert maskin.



![Image](assets/fr/064.webp)



De tekniske implikasjonene av dette alternativet er ganske enkle: pruned-noden er fullt ut i stand til å kringkaste transaksjonene dine, delta i reléet, verifisere blokker og transaksjoner og spore kjeden. På den annen side kan den ikke fungere som en kilde til historiske data utover sine begrensninger for andre applikasjoner (f.eks. fullstendige utforskere, indeksører, lommebøker). Funksjoner som krever arkivet (eller en global indeks), vil derfor ikke være tilgjengelige.



I praksis kan du bruke en pruned-node til å koble til Wallet-administrasjonsprogramvare, for eksempel Sparrow wallet. Du vil imidlertid ikke kunne skanne transaksjoner på Wallet som er eldre enn beskjæringsgrensen. Hvis du for eksempel har en transaksjon registrert i blokk 901 458, men noden din bare beholder blokker fra 905 402 og oppover (fordi de eldste har vært pruned), vil du ikke kunne skanne denne transaksjonen. Hvis du derimot allerede hadde skannet den da noden din fortsatt hadde denne blokkhøyden, vil Wallet-administrasjonsprogramvaren lagre informasjonen og vise saldoen for de tilsvarende UTXO-ene på riktig måte.



Kort sagt fungerer Wallet-sporing problemfritt på en pruned-node hvis du oppretter en ny Wallet mens programvaren din allerede er koblet til noden. På den annen side kan du støte på problemer hvis du gjenoppretter en gammel Wallet, ettersom tidligere transaksjoner som ikke lenger beholdes av noden, selvsagt ikke vil kunne hentes frem.



### Den lette knuten / SPV



En SPV-node (*Simplified Payment Verification*), eller lettvektsnode, beholder bare blokkoverskrifter, ikke transaksjonsdetaljer, og er avhengig av andre fullstendige noder for å få bevis på at en transaksjon er i en blokk (Merkle-bevis via trær) som den har overskriften for. Konseptet med forenklet betalingsverifisering er ikke nytt, og ble foreslått av Satoshi Nakamoto selv i del 8 av hvitboken.



![Image](assets/fr/066.webp)



Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*. https://Bitcoin.org/Bitcoin.pdf



Denne typen node er åpenbart mye lettere når det gjelder lagringsplass og CPU-bruk enn en Full node- eller til og med en pruned-node. SPV-noden egner seg derfor godt til mindre enheter og intermitterende tilkoblinger. Faktisk er den ofte integrert direkte i Wallet, spesielt i mobil programvare som Blockstream-appen.



Kompromisset er tillit og konfidensialitet: En SPV-klient sjekker ikke skript eller valideringspolicyer selv; den antar at kjeden med mest arbeid er gyldig, og er avhengig av en eller flere fulle noder for å få svar. Å bruke denne typen noder er derfor et bedre alternativ enn å koble seg til en tredjepartsnode, men det er fortsatt mindre fordelaktig enn å ha en Full node- eller til og med en pruned-node.



![Image](assets/fr/065.webp)



### Hvilken node for hvilket behov?





- Mobil / nybegynnerbruker



For en nybegynner som bare har en Wallet på en mobilapp, er det å bruke en SPV-node helt klart den beste måten å komme i gang på. Installasjonen er rask, krever få ressurser, og opplevelsen er enkel og flytende. Dette betyr at du kan verifisere visse opplysninger selv, og derfor er mindre avhengig av tredjepartsnoder, samtidig som du er mer uavhengig når det gjelder kringkasting av transaksjoner.





- PC / middels bruker



En mellombruker med en PC kan installere en pruned-node for å dra nytte av nesten alle fordelene med en Full node, uten å overbelaste maskinen sin på daglig basis: full validering, moderat diskbruk og enkelt vedlikehold. Det er en ideell løsning for å koble til skrivebordslommebøker og forbli uavhengig i distribusjonen av transaksjonene dine, uten å investere i en dedikert maskin eller overbelaste diskplassen din.





- Sovereign Bitcoiner / avansert



En Full node er fortsatt den beste løsningen hvis du vil være helt uavhengig i bruken av Bitcoin og ikke begrense deg senere til avanserte bruksområder som en indekserer, en Lightning-node eller til og med en Block explorer. Det er akkurat det vi skal utforske i dette kurset!



## Oversikt over programvareløsninger


<chapterId>0d48b89a-e8b5-441e-a707-537a035fc15e</chapterId>



På programvaresiden er det to hovedmåter å kjøre en Bitcoin-node på:




- installere en protokollimplementering direkte, for eksempel Bitcoin core (anbefalt) eller Bitcoin Knots,
- eller bruke en nøkkelferdig distribusjon (ofte kalt "_node-in-a-box_") som integrerer en Bitcoin-implementering på samme måte, men som også inkluderer et Interface-administrasjonssystem, en applikasjonsbutikk og verktøy som er klare til bruk (Lightning, nettlesere, indeksservere, til og med applikasjoner for selvhosting utenfor Bitcoin...).



Begge tilnærmingene fører til samme mål: å ha din egen node, men de er forskjellige når det gjelder installasjon og bruk av Interface, vedlikehold, utvidelsesmuligheter og kostnader. Det er dette vi skal se nærmere på i dette kapittelet.



### Rå Bitcoin node-implementeringer



Installering av en rå implementering betyr direkte bruk av programvaren til en Bitcoin-protokollimplementering (for eksempel Core), uten noen ekstra programvare Layer. Du administrerer konfigurasjonen, oppdateringene og tilknyttede tjenester (indeksering, API, Lightning, sikkerhetskopier osv.) selv, i henhold til dine behov.



Dette er den mest suverene og fleksible tilnærmingen: Du vet nøyaktig hva som kjører, hvor dataene er, og hvordan alt fungerer. På den annen side blir det mer komplekst så snart du ønsker å gå utover den enkle driften av en Bitcoin-node. Hvis målet ditt bare er å ha en node, er kompleksiteten sammenlignbar med en node-in-a-box, eller til og med mindre, siden det bare handler om å installere programvare.



#### Bitcoin core (kunde med ultramajoritet)



[Bitcoin core er nettverkets ultra-majoritetsklient] (https://bitcoincore.org/). Den laster ned, validerer og vedlikeholder Blockchain, tilbyr RPC/REST API-er og kan integrere en Wallet. Hvis du foretrekker standardverktøy og føler deg komfortabel med å legge til tjenester selv (for eksempel Electrum-server, explorer og LND), er det bedre å bruke Core som den er.



**Fordeler:** Maksimal stabilitet, forutsigbar oppførsel, rå opplevelse, enkel å installere og konfigurere.



**Ulemper:** Du må bygge resten av stakken manuelt for å skape et komplett applikasjonsmiljø, i stedet for bare en Bitcoin-node.



https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

#### Bitcoin Knots (hovedalternativ kunde)



[Bitcoin Knots er en Fork av Bitcoin core] (https://bitcoinknots.org/), vedlikeholdt av Luke Dashjr. Det er den viktigste alternative klienten til Core for implementering av Bitcoin-protokollen. Den er fullt kompatibel med resten av nettverket (den er på ingen måte en Hard Fork som Bitcoin Cash), men tilbyr likevel flere funksjoner, blant annet relépolicyalternativer som ikke finnes i Core, eller som brukes strengere som standard for å begrense det noen anser som spam.



Det er to mulige grunner til å velge Knots fremfor Core:




- Teknikker**: Forskjellige alternativer fra Core, spesielt når det gjelder reléhåndtering, ved å bestemme hvilke transaksjoner som skal aksepteres og kringkastes av noden din.
- Policy**: Noen foretrekker å bruke alternative klienter som Knots av ikke-tekniske grunner, særlig for å støtte et alternativ til Core og dermed redusere Core-monopolet. Hvis Core noen gang skulle bli kompromittert, ville det være nyttig ikke bare å ha solide, godt vedlikeholdte alternative klienter, men også å vite hvordan man bruker dem effektivt. Andre bruker Knots i protest, fordi de har mistet tilliten til Core-utviklerne eller misliker majoriteten av klientens ledelse.


https://planb.network/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Personlig anbefaler jeg at du velger Core, hovedsakelig for å få raskere tilgang til sikkerhetsoppdateringer. Noen sårbarheter som oppdages i Knots, blir faktisk rettet med en forsinkelse. Mer generelt er utviklingsprosessen i Core solid strukturert og støttes av et stort antall bidragsytere, mens Knots vedlikeholdes av en enkelt person og har et mye mindre fellesskap. På den annen side har reléregler en tendens til å miste sin nytteverdi i dag, spesielt når de bare brukes av en liten del av nettverket (som i perkolasjonsteorien).



### Node-i-en-boks-distribusjoner



Den _node-i-en-boks_ kombinerer Bitcoin core (eller Knots) med et forhåndskonfigurert operativsystem, en Interface Web og en App Store med selvhosting-tjenester (Lightning, explorers, Electrum-server, Mempool, BTCPay Server, Nextcloud, etc.). Med bare ett klikk kan du installere, oppdatere og koble sammen disse ulike modulene.



Det er en mye enklere løsning for å starte opp og administrere en rekke tilleggsapplikasjoner fra dag til dag. Ulempen er at når det oppstår et problem (f.eks. Docker-image-konflikt, feilaktig oppdatering, ødelagt database), kan feilsøking bli svært komplisert, ettersom du er avhengig av distribusjonens egen integrasjon. I tillegg er det ofte komplisert å få støtte fra fellesskapet eller offisiell support.



En node-in-a-box er altså svært enkel å bruke så lenge alt fungerer som det skal, men hvis det oppstår en feil, må du være forberedt på å utføre lange søk, vente på hjelp og skitne til hendene.



De fleste av disse løsningene er tilgjengelige i to formater:




- Ferdigmontert maskin: en komplett datamaskin med allerede installert operativsystem. Disse "pay-as-you-go"-maskinene trenger bare å kobles til strømnettet og kobles til Internett for å være i drift. Hvis budsjettet ditt tillater det, har dette alternativet den fordelen at det er veldig enkelt å sette opp, ofte tilbyr prioritert support og bidrar til finansieringen av utviklingen, siden forretningsmodellen til disse selskapene generelt er basert på salg av maskinvare.
- Gjør-det-selv: Installer distribusjonssystemet på din egen maskin (gammel PC, NUC, Raspberry Pi, hjemmeserver...). Dette er den mest økonomiske løsningen, siden du kan resirkulere en gammel maskin eller velge maskinvare som passer akkurat til dine behov og ditt budsjett. Det er også det mest fleksible alternativet, og det mest tilfredsstillende å konfigurere. Det er denne tilnærmingen vi skal utforske i den praktiske delen av kurset.



Her er en oversikt over de viktigste node-in-a-box-løsningene som er tilgjengelige (i 2025):



### Umbrel (umbrelOS og Umbrel Home)



[Umbrel er i dag ledende innen node-in-a-box-løsninger (https://umbrel.com/). Suksessen skyldes i stor grad den enkle installasjonen (da den ble lansert på en enkel Raspberry Pi), den elegante og intuitive Interface og et økosystem av applikasjoner som har vokst raskt og nå er ekstremt omfattende.



![Image](assets/fr/067.webp)



Umbrel ble lansert i 2020 som en enkel Bitcoin-node sammen med noen få tilleggsapplikasjoner, og har gradvis utviklet seg til en moderne hjemmesky med alle funksjoner.



Jeg vil ikke gå nærmere inn på hvordan det fungerer og de spesifikke funksjonene her, da vi skal se nærmere på disse i første kapittel i neste del. I dette BTC 202-kurset har jeg valgt å bruke UmbrelOS, som jeg mener er den beste node-in-a-box-løsningen for nybegynnere og viderekomne brukere.



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

### Start9 (StartOS)



[Start9 tilbyr StartOS (https://start9.com/), et system som er utviklet for "sovereign computing": Målet er at alle skal eie og administrere sin egen private server, utvidet med en markedsplass for selvhusholdte applikasjoner. Du kan kjøpe en Start9-server (Server One til 619 dollar, Server Pure til 899 dollar) eller sette sammen din egen i DIY-modus på din egen maskin.



På Bitcoin-siden lar StartOS deg installere en Full node, en Lightning-node, BTCPay Server, Electrs og mange andre tjenester. Start9s appell strekker seg imidlertid lenger enn dette: det tilbyr muligheten til å oppdage, konfigurere og eksponere ulike programvarer (filsky, meldinger, overvåking) på en enhetlig måte, med full kontroll. Prosjektet er derfor rettet mot brukere som ønsker en robust plattform for selvhosting, ikke bare en enkel Bitcoin-node. Det er sannsynligvis det mest komplette økosystemet etter Umbrel.



![Image](assets/fr/068.webp)



Hovedforskjellen med Umbrel ligger i Interface. Umbrel baserer seg på en svært polert UX, mens Start9 tilbyr en råere, mer funksjonell Interface. Start9s applikasjonsøkosystem er mindre rikholdig enn Umbrels, men det kompenserer for dette med flere tekniske fordeler: Tilgangen til avanserte applikasjonsinnstillinger er forenklet, mens Umbrel raskt blir restriktiv hvis det ønskede alternativet ikke tilbys av Interface. Start9 utmerker seg også når det gjelder sikkerhetskopiering: Bortsett fra Umbrels effektive løsning for LND, finnes det ingen enhetlig mekanisme, i motsetning til Start9. I tillegg tilbyr Start9 mer tilgjengelige overvåkingsverktøy og en kryptert ekstern tilkobling (`https`), mens lokal tilgang til Umbrel er via `http`.



Kort sagt, hvis du bare trenger de viktigste applikasjonene for Bitcoin, ikke er spesielt interessert i Umbrels svært rike økosystem, og Interface-brukeren ikke er en prioritet, så er Start9 et bedre alternativ. Ellers er Umbrel det beste valget.



https://planb.network/tutorials/node/bitcoin/start9-8c8b6827-8423-4929-bcba-89057670ed6a

### MinNode



[MyNode er en distribusjon som utelukkende fokuserer på Bitcoin og Lightning (https://mynodebtc.com/), og som tilbyr en web-Interface, en applikasjonsmarkedsplass og oppgraderinger med ett klikk. Du kan enten kjøpe maskinvare som er klar til bruk (*Model Two* er tilgjengelig for 549 dollar) eller installere MyNode gratis på din egen maskin. Prosjektet tilbyr også en *Premium*-versjon av programvaren (94 dollar), som inkluderer prioritert support og avanserte funksjoner.



![Image](assets/fr/069.webp)



I praksis samler MyNode alle de grunnleggende byggesteinene som trengs for å drifte en Full node, i tillegg til applikasjonene som er viktige for Bitcoin-brukere. Derfor er det en passende løsning hvis du ikke trenger applikasjoner utenfor Bitcoin-økosystemet, som for eksempel selvhostede apper som finnes i Start9- og Umbrel-systemer.



https://planb.network/tutorials/node/bitcoin/mynode-a481fef3-2fd3-4df3-91c0-112cffa094eb

### RaspiBlitz



[RaspiBlitz er et 100% åpen kildekode-prosjekt] (https://docs.raspiblitz.org/) (MIT-lisens) for montering av en Bitcoin-node og en Lightning-node på en Raspberry Pi. Bare last ned avbildningen, start opp, og følg deretter veiviseren for å få en fungerende node-in-a-box på Raspberry Pi. Ferdigmonterte sett er også tilgjengelige fra tredjeparter, vanligvis mellom 300 og 400 dollar, avhengig av maskinvaren. RaspiBlitz tilbyr også en rekke tilleggsprogrammer som er enkle å installere.



![Image](assets/fr/070.webp)



Hvis du eier en Raspberry Pi, er dette et utmerket alternativ, ettersom mer komplette systemer som Umbrel blir stadig tyngre for denne typen mini-PC.



https://planb.network/tutorials/node/bitcoin/raspiblitz-d8cdba2e-a682-46cf-9fdc-d8602fbeac02

### RoninDojo



[RoninDojo er en personvernfokusert node-in-a-box] (https://wiki.ronindojo.io/en/home) som automatiserer distribusjonen av Samurai Dojo og Whirlpool, med en dedikert Interface og plugins som er spesielt utviklet for Samurai-økosystemet.



Prinsippet er enkelt: Hvis du bruker Ashigaru Wallet (Fork-etterfølgeren til Samurai Wallet, etter at utviklerne ble arrestert) eller hvis du ønsker å dra nytte av avanserte personvernverktøy, er RoninDojo noe for deg.



![Image](assets/fr/071.webp)



Prosjektet har tidligere tilbudt en forhåndskonfigurert maskin kalt Tanto, men denne er for øyeblikket ikke tilgjengelig. Den kan komme tilbake på et senere tidspunkt. I mellomtiden er det mulig å installere RoninDojo på en Rock5B+ eller Rockpro64, eller til og med indirekte på en Raspberry Pi.



https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

### Nodl



En annen [node-in-a-box-løsning er Nodl] (https://www.nodl.eu/). Som med de foregående prosjektene kan du enten kjøpe den forhåndskonfigurerte maskinvaren (mellom € 599 og € 799, avhengig av modell) eller installere den selv i DIY-modus.



På programvaresiden integrerer Nodl Bitcoin core, LND, BTCPay Server, Electrs, Dojo, Whirlpool, Lightning Terminal, RTL, samt BTC RPC Explorer, alle med en integrert oppdateringskjede og åpen kildekode under MIT-lisensen.



![Image](assets/fr/072.webp)



Etter å ha utforsket de ulike programvareløsningene, er det nå på tide å velge hvilken maskin som skal være vert for noden din!




## Oversikt over maskinvareløsninger


<chapterId>245d6add-9cda-46b9-9343-31dcdd70456e</chapterId>



Nå som vi har utforsket alle programvaremulighetene, skal vi fokusere på maskinvaren som kreves for noden din. Jeg skal gi deg noen konkrete råd om valg av komponenter, samt konfigurasjoner som er skreddersydd for ulike budsjetter. Dette er selvfølgelig min personlige mening og tilbakemelding: Det finnes helt sikkert andre relevante alternativer i tillegg til de som presenteres her. Jeg kommer heller ikke til å gå inn på de ferdigmonterte maskinene som tilbys av node-in-a-box-prosjekter, som vi allerede har omtalt i forrige kapittel. Her vil vi utelukkende fokusere på DIY-løsninger.



### Trenger du virkelig en dedikert maskin?



I løpet av de siste årene har bitcoinere blitt stadig mer oppmerksomme på en vanlig misforståelse, særlig med populariseringen av node-in-a-box på begynnelsen av 2020-tallet: En Bitcoin-node bør nødvendigvis kjøre på en maskin som er dedikert utelukkende til dette formålet. Men dette er ikke sant. Du trenger ikke nødvendigvis en dedikert datamaskin for å kjøre en Bitcoin-node: Bitcoin core kan fint kjøres på din vanlige PC. Hvis du har tilstrekkelig diskplass for Blockchain eller aktiverer beskjæring, kan du validere kjeden, koble til Wallet og til og med lukke programmet når du er ferdig med å bruke det. Fordelen med denne tilnærmingen er betydelig: null initialinvestering og minimal kompleksitet.



![Image](assets/fr/074.webp)



Når det er sagt, er det ofte mer komfortabelt å bruke en dedikert maskin. Den kan kjøre kontinuerlig (24/7), være tilgjengelig på avstand til enhver tid, ikke legge beslag på ressursene til hovedmaskinen din og, fremfor alt, isolere bruksområder (en god sikkerhetspraksis: Hvis den personlige PC-en din får et problem, fortsetter noden å fungere, og vice versa). Så spørsmålet er ikke "Trenger jeg å dedikere en maskin?", men heller "Trenger jeg en node som hele tiden er online, tilgjengelig for andre enheter og i stand til å utvikle seg?" (Lightning, indekserere, tilleggsapplikasjoner ...). Hvis svaret er ja, vil det være mye enklere å velge en separat maskin.



### 3 anskaffelsesmetoder: resirkulering, brukt og nytt



#### Resirkulering av en gammel PC



Det er den mest økonomiske løsningen. De fleste av oss har en gammel PC som samler Dust hjemme, eller hos venner og familie: Dette er den perfekte muligheten til å ta den i bruk igjen! For å tilpasse den til bruk som en Bitcoin-node, trenger du bare å legge til en 2 TB SSD og, avhengig av behovene dine, bytte ut eller legge til RAM-stenger for å øke RAM-en. Du må regne med å betale mellom 100 og 200 euro for en fullt funksjonell maskin.



Før du kjøper maskinvare, bør du sjekke antall tilgjengelige diskplasser, type tilkobling (M.2 eller SATA), RAM-format (SODIMM eller DIMM) og generasjon (DDR4 osv.). Du bør også benytte anledningen til å rengjøre maskinen, spesielt viften, for å sikre optimal ytelse.



Vær imidlertid forsiktig hvis du bruker en bærbar datamaskin: Batteriet kan bli et problem over tid (mer om dette senere i kapittelet).



#### Rekonditionert eller brukt



Markedet er fullt av oppussede mini-PC-er for bedrifter, for eksempel * Lenovo ThinkCentre Tiny*, *HP EliteDesk Mini* eller *Dell OptiPlex Micro*. Disse maskinene er solide, kompakte, stillegående og energieffektive. Prisen ligger godt under nypris, og det er lett å finne modeller utstyrt med 6. til 10. generasjons i5/i7-prosessorer og 8 til 16 GB RAM, alt til svært attraktive priser, vanligvis mellom €70 og €200, avhengig av konfigurasjon. Etter min mening er dette sannsynligvis det beste alternativet hvis du er på utkikk etter en dedikert maskin til Bitcoin-noden din.



![Image](assets/fr/075.webp)



Det er også mulig å finne brukte PC-er og bærbare datamaskiner som er noen år gamle, med interessante konfigurasjoner og god valuta for pengene.



**Merk:** Maskiner fra bedriftsflåter, som for eksempel *ThinkCentre Tiny*, er ofte bare utstyrt med en *DisplayPort* (DP)-port for skjermen, uten HDMI-utgang. Så ikke glem å ta med en adapter eller en DP-til-HDMI-kabel hvis du trenger en.



#### Kjøpe nytt



Hvis budsjettet ditt tillater det, kan du også velge en ny maskin. Dette er et godt alternativ hvis du vil ha nyere maskinvare med god ytelse, spesielt hvis du planlegger å bruke Umbrel eller Start9 med flere applikasjoner utenfor Bitcoin-økosystemet for selvhosting.



### Hvilken type maskin bør jeg velge?



#### Mini-PC "NUC" / barebone



Mini-PC-er er etter min mening det beste kompromisset for å ha en Bitcoin-node hjemme. De er plassbesparende, får enkelt plass på en hylle, bruker minimalt med strøm og egner seg for enkle maskinvaremodifikasjoner, som å legge til RAM eller bytte ut SSD-en.



Personlig foretrekker jeg *Lenovo ThinkCentre Tiny*, som er svært utbredt på bruktmarkedet (fra bedriftsflåter); de er spesielt robuste og enkle å modifisere. Det finnes selvfølgelig mange tilsvarende fra andre produsenter: *Dell OptiPlex Micro*, *HP ProDesk / EliteDesk Mini / Micro*, *Intel NUC*, *Gigabyte BRIX*, *MSI Cubi*...



![Image](assets/fr/001.webp)



**Høydepunkter:** lite fotavtrykk, moderat strømforbruk, lavt støynivå, skalerbarhet (avhengig av modell) og pålitelighet.



**Svakheter:** Litt dyrere enn en SBC av typen Raspberry Pi, ingen innebygd skjerm (fjerntilgang eller via ekstern skjerm), ingen batteri (plutselig nedstengning ved strømbrudd).



#### Dedikert bærbar PC



Det er et utmerket lavprisalternativ til mini-PC-en: I dag kan du finne brukte eller til og med nye bærbare datamaskiner til lave priser, utstyrt med anstendige prosessorer, mange porter, samt en integrert skjerm og tastatur (veldig praktisk for førstegangsinstallasjon). Fremfor alt fungerer batteriet som en naturlig UPS: I tilfelle strømbrudd slår ikke noden seg brått av, og kan til og med forbli i drift i flere timer.



![Image](assets/fr/076.webp)



**Høydepunkter:** Alt-i-ett-løsning, batteriet fungerer som en UPS (ingen strømbrudd), forenklet installasjon takket være integrert skjerm og tastatur, integrert Wi-Fi-kort og et bredt utvalg av brukt- og nymarkeder (noe som ofte betyr at du kan forhandle om priser).



**Svakheter:** Litt høyere strømforbruk enn en ren Mini-PC, gradvis batterislitasje ved 24/7-drift med tap av kapasitet, sjelden, men reell risiko for at batteriet svulmer opp eller går varmgang med alderen. Det er hovedsakelig dette aspektet som gjør at jeg anser mini-PC-en som et bedre alternativ enn den bærbare PC-en: den gradvise nedbrytningen av batteriet og de tilhørende risikoene.



Hvis du velger denne løsningen, anbefaler jeg at du holder et våkent øye med batteriets tilstand for å unngå fare. Hold øye med overdreven varme, uvanlig lukt, ustabilitet eller deformert skall. Hvis det oppstår en alarm, må du slå av og koble fra datamaskinen umiddelbart, og deretter kaste batteriet på et spesialisert gjenvinningsanlegg.



**Tips:** Hvis BIOS/UEFI eller produsentens verktøy tillater det, kan du sette en belastningsgrense (f.eks. 60 % eller 80 %) for å forlenge batteriets levetid.



#### Raspberry Pi og andre SBC-er: feil idé



På begynnelsen av 2020-tallet, med fremveksten av node-in-a-box-programvare, dukket også Raspberry Pi-bølgen opp som et middel til å kjøre en Bitcoin-node. Ideen virket attraktiv: billig, kompakt og tilgjengelig.



![Image](assets/fr/073.webp)



I praksis kan en Raspberry Pi være tilstrekkelig hvis målet ditt kun er å kjøre en Bitcoin-node uten tilleggsapplikasjoner. Men så snart du ønsker å bruke Umbrel, Start9 eller et rikere økosystem (Block explorer, Address-indekser, Lightning-node, selvhostende apper...), når maskinen raskt sine grenser.



Raspberry Pi har en rekke ulemper:




- prosessorer som er for tynne, med en ARM-arkitektur som noen ganger er inkompatibel med visse programvarer eller krever mer håndtering;
- Loddet RAM, umulig å oppgradere, med begrensede konfigurasjoner (ofte maksimalt 8 GB);
- eksterne bokser for SSD-er som er koblet til med kabel, hyppige kilder til feil, som krever kjøp av et spesifikt kort for en stabil SSD;
- tendens til å varme seg raskt opp og vanskeligheter med å sikre riktig kjøling;
- trenger å kjøpe ekstra maskinvare (kabinett, vifte, SSD-kort osv.);
- svært begrensede tilkoblingsmuligheter.



Historisk sett var den store fordelen med SBC-er som Raspberry Pi prisen: for noen titalls euro kunne du få en dedikert maskin. I dag har imidlertid prisene steget kraftig, og når du har lagt til all nødvendig tilleggsmaskinvare, nærmer kostnadene seg prisen på de første brukte eller oppussede x86-miniperson PC-ene, som etter min mening gir langt flere fordeler. Av denne grunn anbefaler jeg ikke å velge en SBC.



### Velge komponenter



#### Disklagring: SSD obligatorisk, minimum 2 TB



Teknisk sett er det mulig å kjøre en Bitcoin-node på en HDD. Problemet er at alt vil gå betydelig saktere, spesielt IBD, som vil bli ekstremt lang på grunn av Bitcoin cores intensive bruk av disken som cache (spesielt for UTXO-settet). Dette er grunnen til at jeg på det sterkeste fraråder å bruke en HDD: Det skaper en reell flaskehals, begrenser fremtidig utvikling (f.eks. for en Lightning-node), og kan til og med føre til en synkroniseringsfeil med Blockchain-hodet. Dessuten øker konstant stress på den mekaniske disken risikoen for for tidlig slitasje.



SSD-er endrer brukeropplevelsen din radikalt: Alt blir raskere og smidigere, med langt større pålitelighet. Bruk av SSD er derfor (nesten) obligatorisk for noden din, og du kommer ikke til å angre på det, spesielt siden høykapasitetsmodeller nå er relativt rimelige.



![Image](assets/fr/077.webp)



Når det gjelder kapasitet, er 2 TB gradvis i ferd med å etablere seg som det nye rimelige minimumet. Sommeren 2025 nærmer Blockchain seg allerede 700 GB, og hvis du legger til Umbrel, en Address-indekser og noen få applikasjoner, vil en 1 TB SSD raskt bli mettet. Med 2 TB har du en komfortabel margin i årene som kommer (anslagsvis mellom 5 og 15 år). Du kan også velge 4 TB hvis du planlegger å bruke mange applikasjoner på Umbrel, lagre store filer i selvhosting, eller hvis du ønsker å forutse diskplassbehovet ditt i stor grad.



![Image](assets/fr/078.webp)



Når det gjelder formatet, avhenger dette av hvilke porter som er tilgjengelige på maskinen din, men hvis det er mulig, anbefaler jeg å bruke en NVMe M.2 SSD.



#### Minne (RAM): 8 til 16 GB



For Bitcoin core alene (uten Umbrel-overlegg) anbefaler utvikleren minimum 256 MB RAM med innstillinger justert til laveste innstilling, 512 MB med standardinnstillinger og 1 GB for normal bruk.



Hvis du derimot bruker et node-i-en-boks-system som Umbrel eller Start9, er RAM-kravene betydelig høyere. Umbrel-utviklerne anbefaler minimum 4 GB RAM. Dette kan være nok til å kjøre Core only, men du vil fort bli begrenset. De anbefaler derfor 8 GB, som jeg også anser som et minimum for en grunnleggende konfigurasjon rundt Bitcoin (Core, LND, indekser og noen få applikasjoner). Min erfaring er at med Umbrel og noen få tilleggstjenester er 8 GB fortsatt litt lite. For å være virkelig komfortabel og ha litt margin, vil jeg anbefale 16 GB RAM.



#### Prosessor (CPU)



For en Umbrel-node er minimumskravet en 64-biters dual-core-prosessor fra Intel eller AMD. Hvis du ønsker å bruke noen få applikasjoner i tillegg til Bitcoin core, vil en firekjerners prosessor (eller høyere) utgjøre en reell forskjell når det gjelder flyt. For eksempel er 6. til 10. generasjons i5/i7-prosessorer utmerkede alternativer på bruktmarkedet.



### Eksempler på konkrete konfigurasjoner



Nedenfor foreslår jeg tre konkrete konfigurasjoner, tilpasset ulike budsjetter og behov, med presise modeller som støtter dem. Disse valgene er gitt som eksempler for å illustrere informasjonen i dette kapittelet; du er ikke forpliktet til å velge akkurat disse modellene. Ettersom jeg anser Mini-PC-en som det beste alternativet på lang sikt, vil jeg basere meg på dette formatet for de tre foreslåtte konfigurasjonene.



*Prisene nedenfor er kun veiledende og kan variere avhengig av region, leverandør og periode*



Først og fremst trenger du en SSD som er stor nok til å romme Blockchain, samtidig som den gir deg manøvreringsrom. SSD-er har en begrenset levetid når det gjelder skrivesykluser og totalt volum av data som skrives. En Bitcoin-node legger imidlertid en betydelig belastning på disken når den skriver. Derfor anbefaler jeg ikke innstegsmodellene, men i stedet en NVMe SSD, som gir betydelig bedre ytelse.



I forbindelse med dette kurset har jeg for eksempel valgt følgende modell: *Samsung 990 EVO Plus NVMe M.2 SSD 2Tb*, tilgjengelig for rundt €120 på Amazon. Du kan også velge andre kjente merker som Crucial, Western Digital eller Kingston.



![Image](assets/fr/046.webp)



#### Lavbudsjett-konfigurasjon



Hvis budsjettet ditt er svært begrenset (under 200 euro), vil jeg selvsagt råde deg til å ikke investere i en dedikert maskin, men heller installere Bitcoin core direkte på din vanlige PC (i pruned-modus hvis du har lite diskplass).



Ellers anbefaler jeg *HP EliteDesk 800 G2 Mini* for et innstegsbudsjett. Jeg fant en renovert modell for € 96 på Amazon, utstyrt med en 6. generasjons Intel Core i5-prosessor og 8 GB RAM. Dette er et spesielt interessant alternativ for nybegynnere: Denne prosessoren og denne mengden minne er mer enn nok til å kjøre Core på Umbrel, samt flere applikasjoner samtidig, for eksempel en Electrs-indekser, en Lightning-node og en Mempool-forekomst, forutsatt at du ikke tildeler for mye cache til Core. Dessuten gjør denne typen mini-PC det enkelt å øke RAM-minnet til for eksempel 16 GB hvis det skulle være behov for det (du må regne med å betale rundt 30-40 euro ekstra for en eller to minnepinner av god kvalitet).



![Image](assets/fr/045.webp)



Da er det bare å legge til SSD-en i budsjettet. Med utgangspunkt i Samsung 2TB til € 120, får vi en total kostnad på € 216 for en komplett, funksjonell maskin.



#### Konfigurasjon med middels budsjett



Hvis du har et gjennomsnittlig budsjett på rundt 300 euro for maskinen som skal være vert for noden din, anbefaler jeg for eksempel en *Lenovo ThinkCentre Tiny*, som er utstyrt med en høytytende prosessor og tilstrekkelig RAM. Jeg fant en renovert modell på Amazon til 180 euro, med en 6. generasjons Intel Core i7-prosessor og 16 GB RAM. Med en 2 TB SSD til 120 euro blir totalkostnaden 300 euro.



![Image](assets/fr/044.webp)



Med denne maskinen har du en komfortabel konfigurasjon: en rask IBD og muligheten til å kjøre en rekke applikasjoner på Umbrel eller Start9 uten problemer. Det er nettopp denne konfigurasjonen jeg bruker i dette BTC 202-kurset.



#### Avansert konfigurasjon



Med et større budsjett blir mulighetene betydelig større. Du kan velge en gjør-det-selv-konfigurasjon, eller til og med velge en ferdigmontert maskin som tilbys direkte av et node-in-a-box-prosjekt.



For eksempel er *ASUS NUC 14 Pro* tilgjengelig ny fra Amazon for €540. For denne prisen får du en Intel Core Ultra 5-prosessor (ny og spesielt høy ytelse), ledsaget av 16 GB DDR5 RAM. Med en slik konfigurasjon vil du kunne fullføre en IBD på rekordtid og installere krevende applikasjoner uten problemer.



Dette er en ekstremt komfortabel konfigurasjon, til og med overkill hvis det opprinnelige målet bare er å kjøre en Bitcoin-node. Hvis du derimot ønsker å dra full nytte av alle de selvbetjente applikasjonene som er tilgjengelige på Umbrel og Start9, er dette effektnivået helt riktig for deg.



![Image](assets/fr/043.webp)



Avhengig av hva du skal bruke den til, kan du velge enten en 2 TB SSD, som i de andre konfigurasjonene, eller direkte en 4 TB SSD til €260 hvis du også vil lagre personlige filer og utvide bruken av selvhosting. Med en 2 TB SSD er den totale kostnaden for konfigurasjonen € 660, mens den med en 4 TB SSD når € 800.



### Noen flere tips





- Hvis du ønsker å kjøpe brukt utstyr og betale i bitcoins, kan du bli med på et møte nær deg! Ved å chatte med andre deltakere kan du garantert finne passende utstyr til en god pris, samtidig som du bidrar til å holde sirkulærøkonomien rundt Bitcoin i live. Det er også en mulighet til å dra nytte av gode råd fra fellesskapet.





- For Internett-tilkoblingen trenger du selvfølgelig en RJ45 Ethernet-kabel, i hvert fall for systeminstallasjonen.





- I noen miljøer, for eksempel Umbrel, kan du bruke Wi-Fi, men ytelsen vil generelt være dårligere (spesielt hvis du ønsker å bruke Lightning-noden eksternt, da dette kan ha innvirkning). Hvis du velger Wi-Fi, må du sørge for at maskinen din har et innebygd kort eller legge til en kompatibel dongle.





- Bruk alltid originalprodusentens strøm Supply til maskinen din. Dette er avgjørende for å unngå skader på utstyret og for å forebygge risikoen for å starte en brann.





- Hvis maskinen ikke har et innebygd batteri, er det en god idé å investere i en omformer for å unngå plutselige driftsstans.





- Avhengig av utstyrets verdi og den geografiske beliggenheten kan det også være aktuelt med et lynavlederanlegg, enten direkte på tavlen eller på strømskinnen som brukes.





- Til slutt må du huske å optimalisere maskinens kjøling: Rengjør den regelmessig, og installer den på et kjølig, godt ventilert og oversiktlig sted for å unngå overoppheting, noe som kan føre til throttling (frivillig begrensning av prosessorens hastighet).



# Enkel installasjon av en Bitcoin-node


<partId>ca6cf2a5-0bcc-41d9-b556-0d38865bf98f</partId>




## Umbrel: mye mer enn en Bitcoin-node


<chapterId>dd4c04f1-924a-43e1-94f3-ea9fbc83dd43</chapterId>



Umbrel er et personlig serveroperativsystem som er utviklet for å gjøre selvhosting tilgjengelig: Du installerer Umbrel, åpner en nettleser på `umbrel.local`, og administrerer alt via en enkel ekstern Interface.



Prosjektet populariserte først ideen om en Bitcoin- og Lightning-node med ett klikk, og ble deretter utvidet til en veritabel "hjemmesky": fil- og fotolagring, strømming av multimedia, nettverksverktøy, hjemmeautomatisering, lokal AI og hundrevis av apper som kan installeres fra en integrert App Store.



I Umbrel kjører hver applikasjon i en Docker-container (isolering, atomiske oppdateringer, uavhengig start/stopp). Interface sentraliserer tilgangen til alle disse appene, og tilbyr enkel pålogging (med valgfri 2FA), oppdateringer med ett klikk for operativsystem og apper, live-overvåking av maskinen (CPU, RAM, temperatur, lagring), administrasjon av tillatelser mellom apper og en oversikt over forbruket.



Umbrels mål er derfor å gi deg tilbake kontrollen og konfidensialiteten over dataene dine, uten å være avhengig av skytjenester, utover det å bare drifte en Bitcoin-node.



### Umbrel Home vs umbrelOS



Umbrel tilbyr to forskjellige tilnærminger:





- [**Umbrel Home**] (https://umbrel.com/umbrel-home): Dette er en bruksklar miniserver som er spesialdesignet og optimalisert for umbrelOS. Den er kompakt, lydløs, Ethernet-tilkoblet og utstyrt med en NVMe SSD (opptil 4 TB valgfritt), 16 GB RAM og en firekjerners CPU. Du bestiller den, plugger den inn og går til `umbrel.local`. Du kan ha en operativ Umbrel oppe og gå på få minutter. Det er plug-and-play-alternativet.



![Image](assets/fr/081.webp)





- [**umbrelOS**](https://umbrel.com/umbrelos): Dette er operativsystemet du kan installere selv på din egen maskinvare (mini-PC, NUC, tower, dedikert laptop...). Du har samme Interface og samme App Store som på Umbrel Home.



![Image](assets/fr/080.webp)



I begge tilfeller er brukeropplevelsen identisk på programvaresiden: nettleserbasert administrasjon, oppdateringer med ett klikk, installering av applikasjoner på forespørsel... Gjør-det-selv-løsningen er ofte mer økonomisk enn å kjøpe en Umbrel Home (avhengig av hvilken maskin som brukes). Jeg vil imidlertid ikke nødvendigvis anbefale at du alltid velger gjør-det-selv-alternativet, ettersom **kjøp av en Umbrel Home bidrar direkte til å finansiere utviklingen av prosjektet**, siden forretningsmodellen er basert på salg av maskinvare. Og ærlig talt, med en pris på 389 euro for 2 TB lagringsplass, er prisen fortsatt veldig rimelig med tanke på kvaliteten på maskinen som tilbys.



![Image](assets/fr/079.webp)



I neste kapittel skal vi se nærmere på hvordan du installerer umbrelOS DIY på din egen maskin. Du kan imidlertid følge dette BTC 202-kurset på samme måte hvis du har valgt en Umbrel Home.



### Brukstilfelle: fra Bitcoin-noden til hjemmeskyen



Umbrel kan forbli minimalistisk og fokusere utelukkende på Bitcoin, eller utvikle seg til en ekte multifunksjonell personlig server, avhengig av dine behov. Her er de viktigste bruksområdene for Umbrel:





- Enkel Bitcoin-node**: Dette er den grunnleggende bruken som Umbrel har basert seg på fra starten av. Du kan kjøre Bitcoin core (eller Knots), koble lommebøkene dine direkte til noden din, eksponere en Electrum-server, være vert for Mempool Block explorer for å se Blockchain, og estimere kostnader... Det er disse bruksområdene vi skal fokusere på i dette kurset.



![Image](assets/fr/082.webp)





- Lightning Network**: Umbrel lar deg også distribuere LND eller Core Lightning, to implementeringer av Lightning Network, for å administrere din egen Lightning-node. Du kan åpne kanaler, administrere likviditeten din, foreta betalinger, automatisere balansering, tilby tjenester, koble til en ekstern Wallet eller dra nytte av avansert Interface-administrasjon takket være de mange applikasjonene som er tilgjengelige. Vi skal se nærmere på dette spesifikke bruksområdet i vårt neste LNP 202-kurs.



![Image](assets/fr/083.webp)





- Generell selvhosting**: med Nextcloud, Immich, Jellyfin/Plex, DNS-omfattende annonseblokkere (Pi-hole/AdGuard), VPN-er (WireGuard, Tailscale), hjemmeautomatisering (Home Assistant), sikkerhetskopiering, notatadministrasjon, kontorverktøy, lokal AI (Ollama + Open WebUI)... Umbrel kan bli din personlige server, slik at du kan gjenvinne kontrollen over dataene dine. Du er selv vert for tjenestene du bruker hver dag, med en polert brukeropplevelse som ligger tett opp til eksterne løsninger, samtidig som du beholder full kontroll over dataene og personvernet ditt.



Ved å distribuere applikasjoner i containere kan du forme Umbrel slik du ønsker: Start med en enkel Bitcoin-node og noen få apper knyttet til økosystemet, installer deretter en Lightning-node ved siden av Bitcoin-noden, og berik gradvis instansen din med de selvhusholdningsapplikasjonene du trenger.



### Fellesskap og gjensidig hjelp



En av Umbrels viktigste fordeler i forhold til konkurrentene er det store og svært aktive brukerfellesskapet. Du kan nå dem hovedsakelig via [deres Discord] (https://discord.gg/efNtFzqtdx) og [deres nettforum] (https://community.umbrel.com/). Her finner du ikke bare praktiske råd, men fremfor alt løsninger for å løse problemer eller fikse feil. Det er et flott sted å starte, utvikle seg og til slutt hjelpe andre brukere, slik at du ikke blir stående alene med din Coin.



![Image](assets/fr/084.webp)



### UmbrelOS-lisens



Umbrels kode er offentlig tilgjengelig (du kan se, Fork og modifisere den), men den er ikke under en ekte åpen kildekode-lisens. Faktisk distribueres umbrelOS under [*PolyForm Noncommercial 1.0*]-lisensen (https://polyformproject.org/licenses/noncommercial/1.0.0/), selv om noen tilknyttede utviklingsverktøy er tilgjengelige under MIT-lisensen.



I praksis kan du gjøre stort sett hva du vil med umbrelOS, så lenge det er for personlig, ikke-kommersiell bruk: modifisering, videredistribusjon til ideelle formål, opprettelse av derivater for deg selv eller for ideelle organisasjoner, forutsatt at du respekterer de juridiske merknadene.



Det er imidlertid forbudt å selge Umbrel eller derivater av Umbrel (for eksempel en ferdig montert maskin med umbrelOS forhåndsinstallert), å tilby Umbrel-relaterte tjenester kommersielt, eller å integrere koden i et produkt for å tjene penger.



Teknisk sett begrenser ikke denne lisensen installasjon, revisjon eller tilpasning av Umbrel til personlig bruk. Juridisk sett beskytter den prosjektet mot uautorisert videresalg eller kommersiell hosting, spesielt av skyleverandører. Umbrel er derfor ikke åpen kildekode, selv om koden fortsatt er offentlig tilgjengelig.



Hver applikasjon i Store har imidlertid sin egen lisens, ofte med åpen kildekode.




## Installere en Full node med paraply


<chapterId>61bc09c7-787d-4649-b142-457ec018b0f4</chapterId>



Nå som vi har all den nødvendige informasjonen, er det på tide å gå inn i detaljene. I denne veiledningen viser vi deg hvordan du installerer en komplett Bitcoin-node ved hjelp av UmbrelOS.



### Nødvendige materialer



Her bruker vi UmbrelOS x86-image (mer presist, x86_64-versjonen). Du kan følge denne guiden på hvilken som helst maskin du velger, så lenge den ikke er utstyrt med en prosessor med ARM-arkitektur (ikke Apple Silicon, Raspberry Pi, etc.). Det betyr at en hvilken som helst datamaskin med en 64-biters Intel- eller AMD-prosessor vil være tilstrekkelig, så lenge den oppfyller minimumskravene, avhengig av hvordan du har tenkt å bruke Umbrel (minst en dobbeltkjerneprosessor anbefales).



Hvis du har valgt en Raspberry Pi 5 (et alternativ jeg ikke anbefaler, som nevnt i forrige avsnitt), er installasjonen litt annerledes. Du kan da følge denne dedikerte veiledningen og gå tilbake til kurset mitt en gang på Interface-nettstedet `http://umbrel.local`:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Som nevnt i forrige avsnitt valgte jeg å kjøre denne opplæringen på en liten, renovert PC som jeg fant til en god pris: en *Lenovo ThinkCentre M900 Tiny* utstyrt med en Intel Core i7-prosessor og 16 GB RAM. Dette er en svært komfortabel konfigurasjon for å kjøre Umbrel, spesielt for en Bitcoin-node. Jeg valgte imidlertid denne konfigurasjonen fordi jeg ønsker å installere en Lightning-node og andre mer krevende applikasjoner senere. Jeg har også lagt til en 2 TB SSD i ThinkCentre for å beholde hele Blockchain og fortsatt ha en komfortabel margin. Med denne konfigurasjonen er totalkostnaden 270 euro, inkludert alle utgifter.



![Image](assets/fr/001.webp)



Jeg er spesielt glad i Lenovos ThinkCentre Tiny-serie, som er kompakte, stillegående og svært robuste maskiner. Disse maskinene er svært populære blant bedrifter og er derfor svært utbredt på bruktmarkedet, der du kan finne interessante konfigurasjoner til mellom 70 og 200 euro.



Hvis du, som meg, har valgt en PC uten skjerm, **må du bare koble til en skjerm og et tastatur** under installasjonen. Etterpå kan du få fjerntilgang fra en annen datamaskin i samme nettverk (eller via andre metoder som vi kommer tilbake til i senere kapitler). Du trenger også en RJ45 Ethernet-kabel for å koble maskinen til det lokale nettverket, og en USB-nøkkel på minst 4 GB for å lagre installasjonsbildet.



For å oppsummere, her er kravene til utstyret:




- Datamaskin med x86_64-prosessor (minimum Dual-core, anbefalt Quad-core);
- RAM-minne (minimum 4 GB, 8 GB anbefalt eller mer for utvidet bruk);
- SSD (anbefalt + 2 TB);
- USB-nøkkel (+ 4 GB) for installasjon av UmbrelOS-image;
- Skjerm og tastatur (kun nyttig ved førstegangsinstallasjon hvis PC-en ikke er utstyrt med dette);
- RJ45 Ethernet-kabel.



### Trinn 1 - Montering av datamaskinen



Avhengig av hvilken maskinvare du har valgt, er det første trinnet å montere de ulike komponentene i datamaskinen. I mitt tilfelle hadde for eksempel den opprinnelige SSD-en bare en kapasitet på 256 GB, så jeg vil resirkulere den til annen bruk og erstatte den med en 2 TB SSD. Hvis du også vil bytte ut RAM-modulene, er det på tide å gjøre det nå.



### Trinn 2: Klargjør en oppstartbar USB-nøkkel



Før du installerer UmbrelOS på maskinen din, må du opprette en oppstartbar USB-nøkkel som inneholder operativsystemet. Alle trinnene i trinn 2 må utføres på din egen datamaskin (og ikke direkte på den datamaskinen som skal bli noden din).





- Start med å laste ned den nyeste versjonen av UmbrelOS i USB-format:



Gå til [det offisielle Umbrel-nettstedet for å laste ned ISO-bildet] (https://download.umbrel.com/release/latest/umbrelos-amd64-usb-installer.iso) for installasjon via USB-nøkkel. Sørg for at du velger den versjonen som er kompatibel med x86_64-arkitekturen (filen heter `umbrelos-amd64-usb-installer.iso`). Nedlastingen kan ta litt tid, da avbildningen er ganske stor.



![Image](assets/fr/002.webp)





- Installer Balena Etcher:



For å lage en oppstartbar USB-minnepinne bruker du et enkelt, plattformuavhengig verktøy som heter [Balena Etcher] (https://www.balena.io/etcher/). Last ned og installer det på datamaskinen din.



![Image](assets/fr/003.webp)





- Sett inn en tom USB-nøkkel på minst 4 GB:



Plugg en USB-nøkkel inn i datamaskinen (den du nettopp har lastet ned UmbrelOS- og Balena Etcher-imaget til). **Advarsel: Alle data på nøkkelen vil bli slettet**. Pass på at den ikke inneholder noen viktige filer.





- Brenn ISO-bildet til USB-pinnen med Balena Etcher:



Start Balena Etcher og velg ISO-filen `umbrelos-amd64-usb-installer.iso` som du nettopp har lastet ned, ved å klikke på "*Flash from file*"-knappen. Velg deretter USB-nøkkelen som målenhet og klikk på "*Flash!*" for å begynne å skrive.



![Image](assets/fr/004.webp)



Når operasjonen er fullført, har du en oppstartbar USB-nøkkel som inneholder UmbrelOS, klar til å starte opp og installere Umbrel på maskinen din.



![Image](assets/fr/005.webp)



### Trinn 3: Starte datamaskinen fra USB-nøkkelen



Nå som den oppstartbare USB-nøkkelen med UmbrelOS er klar, kan du starte datamaskinen på den for å starte systeminstallasjonen. Koble USB-nøkkelen fra hoveddatamaskinen og sett den inn i enheten som du ønsker å installere Umbrel og Bitcoin-noden på.



Som forklart i begynnelsen av dette kapittelet, trenger du en skjermenhet og en inndataenhet for å fullføre installasjonen. Koble til en skjerm via HDMI (eller en annen port, avhengig av PC-en din) og et tastatur via USB til maskinen. Disse enhetene er kun nødvendige for installasjonen; du trenger dem ikke etterpå, siden Umbrel kan fjernstyres fra en annen datamaskin. Koble disse to enhetene til PC-en din.



**Tips: Hvis du ikke har en ekstern skjerm hjemme, kan du bruke TV-en din. Med HDMI-inngang (eller annen inngang) kan den brukes som midlertidig skjerm mens du installerer operativsystemet.



Umbrel krever selvsagt en Internett-tilkobling. Koble RJ45 Ethernet-kabelen mellom enheten og ruteren.



![Image](assets/fr/006.webp)



Slå på maskinen din. I de fleste tilfeller bør den automatisk oppdage USB-nøkkelen og starte opp fra den. Du vil da se skjermbildet for installasjon av UmbrelOS Interface.



Hvis enheten starter opp på et annet system eller viser en feilmelding, betyr det sannsynligvis at den ikke starter opp automatisk fra USB-nøkkelen. I så fall må du starte på nytt og gå inn i BIOS/UEFI-innstillingene (vanligvis ved å trykke på `DEL`, `F2`, `F12` eller `ESC`, avhengig av datamaskinprodusent). Endre deretter oppstartsrekkefølgen slik at USB-nøkkelen får prioritet. Start deretter enheten på nytt for å starte UmbrelOS.



### Trinn 4: Installer UmbrelOS på datamaskinen din



Når enheten har startet opp fra USB-minnepinnen, blir du møtt av Interface UmbrelOS-installasjonen. Dette trinnet innebærer å installere systemet direkte på maskinens interne Hard-disk.



Skjermbildet som vises, inneholder en liste over alle de interne lagringsenhetene som er oppdaget av datamaskinen. Hver disk har et nummer, et navn og en lagringskapasitet. Finn disken du ønsker å installere Umbrel på. **Advarsel: Alle filer på denne disken vil bli slettet permanent



![Image](assets/fr/007.webp)



Når du har funnet den riktige disken (vanligvis den med størst kapasitet for Blockchain), noterer du nummeret som er tilordnet den. Hvis disken du har valgt, for eksempel vises under nummeret `2`, skriver du bare inn `2` og trykker deretter på `Enter` på tastaturet.



![Image](assets/fr/008.webp)



Programmet formaterer den valgte disken, installerer UmbrelOS og konfigurerer systemet automatisk. Dette kan ta noen minutter. La prosessen gå uten avbrudd.



![Image](assets/fr/009.webp)



Når installasjonen er fullført, blir du bedt om å slå av enheten. Trykk på en hvilken som helst tast for å slå av datamaskinen.



![Image](assets/fr/010.webp)



Du kan nå fjerne USB-nøkkelen, tastaturet og skjermen, som ikke lenger er nødvendige for Umbrel. Det eneste som er igjen av noden, er strømforsyningen Supply og RJ45 Ethernet-kabelen.



![Image](assets/fr/011.webp)



Før du starter enheten på nytt, må du kontrollere følgende to punkter:





- USB-nøkkelen er frakoblet**: Hvis den forblir tilkoblet, kan det hende at systemet starter på nytt på den i stedet for på den interne disken;
- Ethernet-kabelen er koblet til**: Enheten må være koblet til ruteren for å fungere.



Trykk på strømknappen. Systemet starter automatisk fra den interne disken der UmbrelOS ble installert. Den første oppstarten kan ta omtrent **5 minutter**. I løpet av denne tiden initialiserer Umbrel sine tjenester og Interface.



Fra en annen datamaskin (din vanlige PC) som er koblet til **samme lokale nettverk**, åpner du en nettleser (Firefox, Chrome...) og går til:



```
http://umbrel.local
```



Denne Address brukes til å få tilgang til Umbrel Interface grafisk bruker Interface eksternt og starte konfigurasjonen.



Hvis Address `http://umbrel.local` ikke fungerer i nettleseren din etter å ha ventet i minst 5 minutter, er det bare å prøve:



```
http://umbrel
```



Hvis dette fortsatt ikke fungerer, kan du skrive inn Umbrels lokale IP Address direkte i nettleseren. For eksempel (erstatt `42` med nummeret til maskinen som er vert for Umbrel på det lokale nettverket):



```
http://192.168.1.42
```



Det finnes flere metoder for å identifisere Umbrels IP Address, fra de enkleste til de mest avanserte:





- Gå inn i ruterens administrasjon Interface og finn IP Address til Umbrel-enheten i det lokale nettverket.





- Bruk nettverksskanningsprogramvare som Angry IP Scanner for å oppdage tilkoblede enheter og finne Umbrels IP Address.



![Image](assets/fr/012.webp)



https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d



- Som en siste utvei kan du koble en skjerm og et tastatur til enheten igjen, logge på (standard pålogging: `umbrel`, passord: `umbrel`) og deretter skrive inn følgende kommando:



```
hostname -I
```



Nå er du klar til å bruke Umbrel!



### Trinn 5: Kom i gang med Umbrel



For å begynne å konfigurere Umbrel klikker du på "*Start*"-knappen.



![Image](assets/fr/013.webp)



#### Opprett en konto



Velg et pseudonym eller skriv inn navnet ditt, og angi deretter et sterkt passord. Vær forsiktig: Dette passordet er den eneste barrieren som beskytter tilgangen til Umbrel fra nettverket ditt (og dermed potensielt til bitcoinsene dine hvis du kjører en Lightning-node på Umbrel). Det beskytter også ekstern tilgang via Tor eller VPN, hvis disse tjenestene er aktivert.



Velg et sterkt passord, og sørg for å ta minst én sikkerhetskopi (det anbefales å bruke en passordbehandler).



https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Når du har skrevet inn passordet ditt, klikker du på "*Opprett*"-knappen.



![Image](assets/fr/014.webp)



Umbrel-konfigurasjonen er nå fullført.



![Image](assets/fr/015.webp)



#### Oppdagelsen av Interface



Umbrels Interface er ganske intuitiv:





- På startsiden kan du se de installerte programmene og widgetene dine.



![Image](assets/fr/016.webp)





- I "*App Store*" kan du installere nye applikasjoner,



![Image](assets/fr/017.webp)





- Menyen "*Files*" samler alle dokumenter som er lagret på Umbrel.



![Image](assets/fr/018.webp)





- I menyen "*Settings*" kan du endre Umbrels innstillinger og få tilgang til informasjon om den, inkludert
    - Oppdater, start på nytt eller stopp maskinen;
    - Se tilgjengelig lagringsplass, RAM-bruk og prosessortemperatur;
    - Endre bakgrunnsbilde;
    - Administrer ekstern tilgang via Tor, aktiver Wi-Fi eller 2FA.



![Image](assets/fr/019.webp)



#### Sikkerhets- og tilkoblingsinnstillinger



Først og fremst anbefaler jeg på det sterkeste at du aktiverer tofaktorautentisering (2FA). Dette gir passordet ditt en ekstra Layer av sikkerhet. Det er nesten uunnværlig hvis du planlegger å bruke Umbrel til å lagre personlige filer, kjøre en Lightning-node eller utføre andre sensitive aktiviteter.



https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Dette gjør du ved å klikke på den aktuelle boksen i innstillingene.



![Image](assets/fr/020.webp)



Skann deretter QR-koden som vises ved hjelp av autentiseringsprogrammet ditt. Skriv deretter inn den 6-sifrede dynamiske koden i feltet på Umbrel.



Fra nå av vil hver nye tilkobling til Umbrel kreve både passordet og den sekssifrede koden som genereres av tofaktorautentiseringsapplikasjonen (2FA).



![Image](assets/fr/021.webp)



Når det gjelder ekstern tilgang via Tor, anbefaler jeg at du lar dette alternativet være deaktivert for å begrense angrepsflaten til Umbrel hvis du ikke trenger det. Som standard kan noden din bare nås fra en maskin som er koblet til det samme lokale nettverket. Hvis du aktiverer tilgang via Tor, kan du likevel administrere Umbrel mens du er på farten.



Hvis du aktiverer denne funksjonen, blir det i teorien mulig for alle maskiner i hele verden å forsøke å koble seg til noden din, forutsatt at de kjenner Tor Address. Passordet ditt og 2FA vil imidlertid fortsatt beskytte deg.



Hvis du aktiverer dette alternativet, må du sørge for at tofaktorautentisering (2FA) er aktivert, at du har et sterkt passord, og at du aldri avslører Tor-tilkoblingen din Address.



Bare skriv inn denne Tor Address i Tor-nettleseren din for å få tilgang til Umbrels Interface fra et hvilket som helst nettverk.



![Image](assets/fr/026.webp)



Til slutt kan du på denne innstillingssiden også aktivere Wi-Fi-tilkoblingen. Hvis maskinen som er vert for Umbrel har et Wi-Fi-nettverkskort eller en Wi-Fi-dongle, kan du få tilgang til Internett uten å bruke RJ45-kabelen. Avhengig av konfigurasjonen din kan denne løsningen imidlertid gjøre tilkoblingen tregere, noe som kan påvirke den første synkroniseringen (IBD) og fremtidig bruk av noden (f.eks. for Lightning-transaksjoner). Personlig anbefaler jeg ikke dette alternativet, ettersom en node ikke er beregnet for mobil bruk: Den er alltid tilgjengelig eksternt, så du kan like gjerne la den være koblet til.



### Trinn 6: Installer en Bitcoin-node på Umbrel



Nå som UmbrelOS er riktig installert og konfigurert på maskinen din, kan du fortsette med å installere Bitcoin-noden. Ingenting kan være enklere: Gå til App Store, åpne kategorien "*Bitcoin*", og velg deretter applikasjonen "*Bitcoin Node*" (det er faktisk Bitcoin core).



![Image](assets/fr/022.webp)



Klikk deretter på "*Install*"-knappen.



![Image](assets/fr/023.webp)



Når installasjonen er fullført, vil Bitcoin-noden starte sin IBD (*Initial Block Download*): Den vil laste ned og validere alle transaksjoner og blokker siden Bitcoin ble opprettet i 2009.



![Image](assets/fr/024.webp)



Denne fasen er spesielt tidkrevende, siden varigheten avhenger av flere faktorer, blant annet hvor mye RAM som er allokert til nodebufferen, diskhastighet, hastighet på Internett-tilkoblingen og prosessorkraft. Varigheten er derfor svært varierende, avhengig av konfigurasjonen. Med en PC med høy ytelse (NVMe SSD, +32 GB RAM, kraftig prosessor og god Internett-tilkobling) kan IBD fullføres på rundt ti timer. På den annen side kan en gammel prosessor, lite RAM eller, enda verre, en mekanisk Hard-disk (frarådes på det sterkeste) forlenge denne operasjonen til flere uker.



Med en PC med normal konfigurasjon (en anstendig prosessor, 8 til 16 GB RAM og en SSD) er det mulig å bruke den i rundt 2 til 7 dager.



For å gjøre IBD litt raskere kan du øke RAM-minnet som er allokert til nodebufferen (som først og fremst brukes til UTXO-settet, som vi kommer tilbake til senere i kurset) ved hjelp av parameteren `dbcache`. På Umbrel gjøres denne endringen i nodeparametrene dine, under fanen "*Optimization*".



![Image](assets/fr/025.webp)



Som standard er verdien for parameteren `dbcache` i Bitcoin core satt til 450 MiB, eller rundt 472 MB. Ved å øke denne verdien kan du øke hastigheten på IBD noe. Jeg vil imidlertid ikke nødvendigvis anbefale å sette denne parameteren for høyt: Selv om du setter den til 4 GiB, vil synkroniseringen bare bli omtrent 10 % raskere, og det kan føre til at du mister tid i tilfelle et avbrudd under IBD.



Vær forsiktig så du ikke allokerer en verdi som er for stor for maskinen din. Hvis RAM-minnet som er tilgjengelig for UmbrelOS tar slutt, kan noden stoppe brått, slik at IBD-en avbrytes og du må starte den manuelt på nytt, noe som kan føre til et betydelig tidstap.



For å finne ut mer om virkningen av parameteren `dbcache` på den innledende synkroniseringen, anbefaler jeg denne analysen av Jameson Lopp: [*Effects of DBcache Size on Bitcoin Node Sync Speed*] (https://blog.lopp.net/effects-dbcache-size-Bitcoin-node-sync-speed/)



Når IBD for noden din er fullført (100 % synkronisering), har du nå en fullt operativ Bitcoin-node. Gratulerer, du er nå en integrert del av Bitcoin-nettverket!



![Image](assets/fr/027.webp)



I neste del skal vi se nærmere på den praktiske bruken av den nye noden din: hvordan du kobler Wallet til den, og hvilke applikasjoner du bør installere for å bli en suveren Bitcoiner.





# Koble Wallet til noden din


<partId>418d0afd-3a61-4b5a-9db4-203c0335fd29</partId>



## Indekserere: rolle, drift og løsninger


<chapterId>4f93c07a-f0cb-435f-8b68-162f316d7039</chapterId>



Hvis du allerede har utforsket Bitcoin-noder før du tok dette kurset, har du kanskje støtt på begrepet "indekser". Dette er verktøy som Electrs eller Fulcrum, som kan legges til i en Bitcoin core-node. Men hva er egentlig deres rolle? Hvordan fungerer de i praksis? Og bør du installere en på din nye Bitcoin-node? Det er det vi skal se nærmere på i dette kapittelet.



### Hva er en indekserer?



Generelt sett er en indekser et program som skanner et sett med rådata, trekker ut relevante nøkler (for eksempel ord, identifikatorer og adresser) og bygger en hjelpefil, kalt en "indeks", der hver nøkkel refererer til den nøyaktige plasseringen av dataene i korpuset. Denne forbehandlingsfasen bruker CPU-tid og krever noe diskplass, men den eliminerer behovet for å behandle hele korpuset hver gang databasen blir forespurt.



Enkelt forklart er det samme prinsipp som et register i en bok: Hvis du er på utkikk etter en spesifikk opplysning, kan du i stedet for å lese hele boken på nytt, slå opp i registeret for å finne siden der informasjonen du leter etter, står.



I en Bitcoin-node, som Bitcoin core, lagres Blockchain-data i sin rå, kronologiske form. Hver blokk inneholder transaksjoner, som igjen inneholder inndata og utdata, uten noen spesiell klassifisering etter Address, identifikator eller Wallet. Denne lineære organiseringen er optimalisert for blokkvalidering, men er uegnet for målrettede søk. Hvis du for eksempel vil finne alle transaksjoner som er knyttet til en bestemt Address i en ikke-indeksert node, må du gå gjennom hele Blockchain manuelt, blokk for blokk og transaksjon for transaksjon. Det er nettopp her indekseringsenheten på Bitcoin-noden din kommer inn i bildet.



![Image](assets/fr/085.webp)



En indekserer er et spesialisert program som analyserer denne massen av rådata (Blockchain-, Mempool- og UTXO-settet) og trekker ut nøkler, for eksempel transaksjonsidentifikatorer, adresser og blokkhøyder. Ut fra disse nøklene bygger den indeksen sin, og knytter hver nøkkel til den nøyaktige plasseringen av informasjonen i nodens lager.



![Image](assets/fr/086.webp)



Med indeksering kan du søke etter informasjon på noden raskt, nøyaktig og effektivt. Når du for eksempel kobler en Wallet som Sparrow til noden din, kan den vise saldoen til en Address nesten umiddelbart. Konkret spør den indekseren med en forespørsel som f.eks: "_Hvilke UTXO-er er knyttet til dette skriptet - Hash?_" Indeksereren svarer nesten umiddelbart, uten å måtte lese hele Blockchain på nytt, ettersom disse dataene allerede er oppført i databasen.



### Har Bitcoin core en indekseringsenhet?



Uten behov for tilleggsprogramvare tilbyr Bitcoin core strengt tatt ikke en komplett Address-indeksering som kan sammenlignes med den man finner i programvare som Electrs eller Fulcrum. Likevel inneholder den flere interne indekseringsmekanismer, i tillegg til valgfrie alternativer for å utvide spørringsmulighetene. For å forstå situasjonen fullt ut, må vi ta en omvei inn i prosjektets historie.



Frem til Bitcoin core versjon 0.8.0 var transaksjonsvalidering basert på en global transaksjonsindeks, kjent som "txindex". Denne indeksen refererte til alle Blockchain-transaksjoner og utdataene deres. Når en node mottok en ny transaksjon, konsulterte den denne indeksen for å verifisere at de forbrukte utdataene (i inndata) faktisk eksisterte og ikke allerede hadde blitt brukt. `txindex` var derfor uunnværlig for transaksjonsvalidering på den tiden.



Denne tilnærmingen hadde imidlertid sine begrensninger: Den var treg, kostbar i form av lagringsplass og overflødig informasjon. For å bøte på dette introduserer versjon 0.8.0 en overhaling av valideringsmodellen kalt ***Ultraprune***. I stedet for å lagre alt i form av transaksjonsindekser, vedlikeholder Bitcoin core en enkel database som kun er dedikert til UTXO-er, kalt `chainstate` (i dagligtalen kalles dette "UTXO set"), og oppdaterer listen etter hvert som utganger forbrukes og opprettes.



Denne metoden er mye raskere og lagrer bare registerets nåværende tilstand, noe som gjør `txindex`-indeksereren unødvendig. I stedet for å slette `txindex`-koden har utviklerne valgt å beholde denne funksjonaliteten bak en enkel parameter (`txindex=1`). Ved å aktivere dette alternativet på noden din, kan du søke etter alle transaksjoner fra dens `txid`.



I motsetning til hva mange tror, tilbyr ikke Bitcoin core Address-basert indeksering som Electrs eller Fulcrum. Det er flere grunner til dette valget:





- Bitcoin cores rolle er ikke å bli en komplett Block explorer, og heller ikke å tilby et API som er skreddersydd for hver bruk. Integrering av en Address-basert indeks vil innebære et langsiktig vedlikehold av Commitment som går utover programvarens opprinnelige omfang.





- De fleste bruksområder kan allerede dekkes på andre måter. Hvis du for eksempel vil estimere balansen i en Address, kan du bruke kommandoen `scantxoutset`, som spør direkte i UTXO-settet uten å kreve en fullstendig indeks.





- Hvert program har spesifikke krav til formatet eller typen data som skal indekseres (Address, Hash-skript, proprietær tag osv.). Det er mer fleksibelt og logisk å la disse programmene bygge sine egne tilpassede indekser enn å fikse en generisk løsning i Bitcoin core.



Bitcoin core har en valgfri transaksjonsindeksering (`txindex`), en levning fra den historiske driften, men den gir ikke en Address-indeks, og heller ikke en direkte Interface-indeksering for komplekse søk. I noen tilfeller kan det derfor være nyttig å legge til en ekstern indekserer.



### Bør du legge til en Address-indekser til noden din?



Det er ikke obligatorisk å legge til en Address-indekser, for eksempel Electrs eller Fulcrum; det avhenger av dine spesifikke behov.



Hvis du bare vil koble en Wallet, for eksempel Sparrow, til noden din for å se saldoer og kringkaste transaksjoner, er dette fullt mulig direkte via Bitcoin cores Interface RPC, enten lokalt eller eksternt via Tor.



På den annen side, for å bruke mer avansert programvare, for eksempel å kjøre en Mempool.lokalt, blir installasjonen av en Address-indekser uunnværlig for plassen Block explorer.



Indeksereren krever en viss synkroniseringstid (mindre enn IBD) og vil oppta ekstra diskplass. Hvis SSD-en din fortsatt har nok ledig plass etter nedlasting av Blockchain, kan du enkelt legge til en indekser.



### Hvilken indekserer skal jeg velge?



To programvareprogrammer brukes ofte til å bygge opp denne typen Address-indekser og gjøre dem tilgjengelige: **Electrs** og **Fulcrum**. Disse verktøyene indekserer Blockchain i henhold til script-Hash (adresser) og foreslår deretter en standardisert Interface (Electrum-protokollen), som mange lommebøker, for eksempel Electrum Wallet, Sparrow eller Phoenix, kobler seg til.



![Image](assets/fr/087.webp)



Enkelt sagt er Electrs ganske kompakt: Den indekserer Blockchain raskere og tar opp mindre diskplass, men gir litt dårligere resultater enn Fulcrum på spørringer. Fulcrum bruker derimot mer diskplass og bruker lengre tid på å indeksere, men gir bedre ytelse på spørringer.



For individuell bruk anbefaler jeg Electrs: den bruker mindre plass, er godt vedlikeholdt, og selv om den er litt tregere på visse forespørsler enn Fulcrum, er den fortsatt mer enn tilstrekkelig for daglig bruk. Hvis du har tid og diskplass, kan du også prøve Fulcrum, som vil prestere betydelig bedre, spesielt på lommebøker med mange adresser som skal verifiseres.



Konkret vil Electrs i august 2025 kreve ca. 56 GB lagringsplass, sammenlignet med ca. 178 GB for Fulcrum. Valget av indekserer avhenger derfor også av lagringskapasiteten din:




- Hvis du har svært begrenset diskplass, må du nøye deg med Bitcoin core uten en ekstern Address-indekserer.
- Hvis du ønsker å bruke en indekseringsenhet, men fortsatt er begrenset av kapasitet, bør du velge Electrs.
- Hvis du har nok diskplass, kan Fulcrum være akkurat det du er ute etter.



I resten av dette BTC 202-kurset vil jeg bruke Electrs, men du kan enkelt følge med med Fulcrum: Installasjonsprosedyren er identisk, og det samme er Interface-tilkoblingen til Wallet, siden begge eksponerer en Electrum-server.



### Hvordan installerer jeg en indekserer på Umbrel?



For å installere Electrs (eller Fulcrum) på Umbrel er prosedyren enkel: Gå til App Store, søk etter den aktuelle applikasjonen (som ligger i Bitcoin-fanen), og klikk deretter på "*Install*"-knappen.



![Image](assets/fr/028.webp)



Når installasjonen er fullført, fortsetter Electrs med en synkroniseringsfase (indeksering), som kan ta flere timer.



![Image](assets/fr/029.webp)



Når synkroniseringen er fullført, kan du koble Wallet-programvaren til Electrum-serveren din, som ligger på Umbrel.



## Hvordan kobler jeg Wallet til Bitcoin-noden min?


<chapterId>35519b1a-f681-4a69-a652-9fbe510cd17f</chapterId>



Nå som du har en komplett Bitcoin-node, er det på tide å ta den i bruk! I neste kapittel skal vi se nærmere på andre potensielle bruksområder for Umbrel-instansen din. La oss imidlertid begynne med det grunnleggende: koble til Wallet-programvaren din for å bruke informasjon fra din egen Blockchain og distribuere transaksjoner gjennom din egen node.



Som nevnt ovenfor finnes det to hovedgrensesnitt for tilkobling:




- Direkte tilkobling til Bitcoin core via RPC;
- Eller koble til en Electrum-server (Electrs eller Fulcrum).



I denne veiledningen konsentrerer vi oss om å koble til noden din via Tor, siden dette er en både enkel og sikker løsning for nybegynnere. Jeg fraråder på det sterkeste å eksponere nodens RPC-port i klartekst, da feilkonfigurasjon utgjør en betydelig risiko for sikkerheten og konfidensialiteten til dataene dine. Den største ulempen med kommunikasjon via Tor er at den er treg. I neste kapittel skal vi se nærmere på et raskt og sikkert alternativ til Tor for ekstern tilgang til noden din: VPN.



Vi bruker Sparrow som eksempel i dette kapittelet, men fremgangsmåten er den samme for alle andre Wallet-administrasjonsprogrammer som godtar tilkoblinger til Electrum-servere. Du finner ganske enkelt den tilsvarende innstillingen i programparametrene (vanligvis i "*Server*", "*Nettverk*", "*Node*"...).



På Sparrow åpner du "*File*"-fanen og går til "Settings"-menyen.



![Image](assets/fr/030.webp)



Klikk deretter på "*Server*" for å få tilgang til tilkoblingsparametrene.



![Image](assets/fr/031.webp)



Deretter finner du tre alternativer for å koble programvaren din til en Bitcoin-node:




- Public Server* (gul): Hvis du ikke eier en Bitcoin-node, kobler dette alternativet deg som standard til en offentlig node du ikke eier (vanligvis en bedriftsnode). Dette alternativet er ikke relevant her, siden du har din egen node på Umbrel.
- Bitcoin core* (Green): Dette alternativet tilsvarer tilkobling via Interface RPC, dvs. direkte til Bitcoin core.
- Private Electrum* (blå): Med dette alternativet kan du koble til via indeksererens Interface Electrum-server (Electrs eller Fulcrum).



### Tilkobling til Bitcoin core RPC



Hvis Umbrel-noden din ikke har en indekser, er det dette alternativet du må velge. På Sparrow klikker du på "*Bitcoin core*".



![Image](assets/fr/032.webp)



Deretter må du oppgi en rekke opplysninger for å opprette forbindelsen til noden din. Alle disse dataene er tilgjengelige fra applikasjonen "*Bitcoin Node*" på Umbrel ved å klikke på "*Connect*"-knappen øverst til høyre på Interface.



![Image](assets/fr/033.webp)



Fanen "*RPC Details*" viser all nødvendig informasjon for tilkobling. Velg å koble til via Tor Address (i `.onion`).



![Image](assets/fr/034.webp)



Skriv inn disse dataene i de tilsvarende feltene på Sparrow wallet, og klikk deretter på knappen "*Test Connection*".



![Image](assets/fr/035.webp)



Hvis tilkoblingen er vellykket, vises et Green-merke og en bekreftelsesmelding.



![Image](assets/fr/036.webp)



Krysset nederst til høyre på Interface Sparrow wallet vil nå være Green (noe som indikerer en direkte forbindelse til Bitcoin core).



**Merk: For at tilkoblingen skal lykkes, må noden din være 100 % synkronisert. Hvis dette ikke er tilfelle, må du vente til slutten av IBD-en.



### Koble til Electrs



Hvis noden din har en indekser, er det bedre å koble seg til den enn å bruke Bitcoin core direkte, ettersom spørringene dine blir behandlet raskere.



På Sparrow går du til "*Private Electrum*"-fanen.



![Image](assets/fr/037.webp)



Deretter må du legge inn en rekke opplysninger for å opprette forbindelse med indekseringsenheten. Du finner disse opplysningene i applikasjonen "*Electrs*" (eller eventuelt "*Fulcrum*") på Umbrel.



Velg fanen "*Tor*" for å få `.onion`-tilkoblingen Address. Hvis du ønsker å koble til en mobil Wallet-programvare, kan du også skanne QR-koden direkte.



![Image](assets/fr/038.webp)



Bare skriv inn Tor Address for Electrum-serveren din i "*URL*"-feltet, og klikk deretter på "*Test Connection*"-knappen.



![Image](assets/fr/039.webp)



Hvis tilkoblingen er vellykket, vises en hake og en bekreftelsesmelding.



![Image](assets/fr/040.webp)



Haken nederst i høyre hjørne på Interface Sparrow wallet blir blå (fargen som forbindes med tilkobling til en Electrum-server).



**Merk: For at tilkoblingen skal fungere, må indekseringsenheten være 100 % synkronisert. Hvis dette ikke er tilfelle, må du vente til indekseringsprosessen er fullført.



Nå vet du hvordan du kobler Wallet til Bitcoin-noden din! I neste kapittel vil jeg introdusere deg for flere applikasjoner som er tilgjengelige på Umbrel, som jeg er spesielt glad i, og som vil gjøre det mulig for deg å forbedre den daglige bruken av Bitcoin gjennom noden din.




## Oversikt over tilgjengelige applikasjoner


<chapterId>2a5ccfbe-0b17-44c9-863c-b7e8cb4b4594</chapterId>



Umbrel tilbyr en omfattende applikasjonsbutikk. Som du vil se, finnes det mange verktøy relatert til Bitcoin, men også et bredt utvalg av applikasjoner innen svært forskjellige områder: selvhosting-løsninger for tjenester og filer, produktivitetsapplikasjoner, mer generelle økonomiverktøy, mediehåndtering, nettverkssikkerhet og -administrasjon, utvikling, kunstig intelligens, sosiale nettverk og til og med hjemmeautomatisering.



I dette BTC 202-kurset konsentrerer vi oss utelukkende om Bitcoin-relaterte applikasjoner. Du er imidlertid velkommen til å utforske resten av katalogen for å finne verktøy som kan være nyttige for deg.



Det ville selvfølgelig være umulig å liste opp alle Bitcoin-applikasjonene her. I dette kapittelet vil jeg introdusere deg for de viktigste verktøyene som vil forenkle og berike din daglige bruk av Bitcoin.



### Mempool.space



Hvis det er ett verktøy som er helt uunnværlig i den daglige bruken av Bitcoin, så er det Block explorer. Enten det er tilgjengelig på nettet eller installert lokalt, forvandler det Blockchains rådata til et strukturert, oversiktlig og lettlest format. Det har også en søkemotor som lar brukerne raskt finne en bestemt blokk, transaksjon eller Address.



Helt konkret kan du med utforskeren estimere gebyrene som kreves for at transaksjonen din skal bli inkludert i en blokk, og deretter følge med på fremdriften: finne ut om det er sannsynlig at den blir inkludert i nær fremtid, avhengig av gebyrmarkedet, og til slutt bekrefte at den faktisk har blitt inkludert i en blokk. Det gir også muligheten til å analysere tidligere transaksjoner og se historikken deres. Kort sagt, det er bitcoinerens sveitsiske lommekniv.



Som nevnt tidligere kan en explorer ligge på et nettsted på nettet eller kjøres lokalt på maskinen din. En stor ulempe med nettbaserte tjenester er at de kan kompromittere personvernet ditt. Uten VPN eller Tor kan serveren som er vert for utforskeren, koble din IP Address til transaksjonene du ser på, noe som kan gi en ideell inngangsport for kjedeanalyse.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

I tillegg kan internettleverandøren din vite at du ser på en bestemt transaksjon via Block explorer-nettstedet. Dette reiser også et spørsmål om tillit: Du må stole på at nettjenesten gir deg nøyaktig informasjon om transaksjonene dine, uten at du selv kan verifisere sannhetsgehalten.



Derfor er det alltid best å bruke din egen lokale Block explorer. På denne måten vil ingen data relatert til søkeaktiviteten din lekke ut, siden alle spørringer behandles direkte på en maskin du kontrollerer, uten å passere gjennom Internett. I tillegg er en lokal utforsker avhengig av data fra din egen Bitcoin-node, som du selv har validert i henhold til dine egne regler, og som du kan stole på.



Umbrel tilbyr flere blokkutforskere:




- Mempool.Space
- Bitfeed
- BTC RPC Explorer



Jeg er spesielt glad i Mempool.Space, som jeg har installert på noden min. Merk: For å bruke de fleste blokkutforskere på Umbrel, kreves det en Address-indekser. Du trenger derfor applikasjonen Bitcoin Node (eller Bitcoin Knots), som har en 100 % synkronisert Blockchain, samt en indekserer som Electrs eller Fulcrum, som også er 100 % synkronisert.



Når applikasjonen er installert, er det bare å åpne den for å få tilgang til din egen utforsker.



![Image](assets/fr/041.webp)



Hvis du vil lære mer om hvordan du bruker Mempool.Space Explorer, anbefaler jeg denne omfattende veiledningen:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

### Lightning Node



Nå som du har din egen Bitcoin-node, kan du også sette opp din egen Lightning-node for å utføre off-chain-transaksjoner, uten å være avhengig av en tredjeparts infrastruktur.



Umbrel tilbyr en rekke applikasjoner som hjelper deg med å få Lightning-noden i gang. Du kan allerede velge mellom to hovedimplementeringer:




- LND, via applikasjonen *Lightning Node*;
- Core Lightning.



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

Du kan deretter administrere noden din fra Interface, eller du kan installere *Ride The Lightning* eller *ThunderHub* for å få enda bedre funksjonalitet og avanserte alternativer. Disse verktøyene gir deg et mye mer omfattende nettbasert Interface-administrasjonssystem for noden din.



https://planb.network/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.network/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

![Image](assets/fr/088.webp)



Til slutt anbefaler jeg *Lightning Network+*-applikasjonen, som lar deg finne jevnaldrende som du kan åpne kanaler med, noe som muliggjør både utgående og innkommende kontanttransaksjoner.



![Image](assets/fr/089.webp)



Takket være Umbrel er det blitt mye enklere å administrere en personlig Lightning-node, men det er fortsatt relativt komplisert. Derfor kommer vi til å se nærmere på dette emnet i et fremtidig kurs som er viet denne bruken.



### Haleskala



En annen applikasjon jeg liker spesielt godt på Umbrel er Tailscale. Det er en VPN-applikasjon som er designet for å forenkle opprettelsen av sikre nettverk mellom flere enheter, uansett hvor de befinner seg i verden. I motsetning til tradisjonelle VPN-er, som er avhengige av sentraliserte servere, bruker Tailscale WireGuard-protokollen til å etablere ende-til-ende-krypterte forbindelser mellom de ulike maskinene dine. Dette betyr at du kan distribuere et fungerende VPN på bare noen få minutter, uten behov for kompliserte nettverkskonfigurasjoner.



På Umbrel kobler Tailscale-installasjonen din Bitcoin-node til ditt eget virtuelle private nettverk. Når noden er konfigurert, får den en privat Tailscale IP Address, som kun er tilgjengelig fra andre enheter som er koblet til det samme Tailscale-nettverket (for eksempel datamaskiner, smarttelefoner og nettbrett). Denne tilkoblingen er ende-til-ende-kryptert og går ikke gjennom et ubeskyttet offentlig nettverk, noe som øker sikkerheten betydelig sammenlignet med en ukryptert tilkobling.



![Image](assets/fr/090.webp)



Helt konkret gir Tailscale deg flere fordeler når du bruker din Umbrel:





- Du kan administrere Interface Umbrel eller få tilgang til applikasjonene som er knyttet til noden din (for eksempel Mempool, Ride The Lightning, ThunderHub ...) fra hvor som helst, som om du var på det samme lokale nettverket, uten å eksponere porter på Internett og uten å gå gjennom Tor, som er veldig tregt;





- Du kan koble deg til Electrum-serveren din (Electrs eller Fulcrum) eller direkte til Bitcoin core via VPN, utenom Tor. Dette gir en sikker tilkobling som kan sammenlignes med å bruke Tor, men med mye høyere hastighet og redusert ventetid. Kort sagt beholder du personvernet og sikkerhetsfordelene ved Tor, samtidig som du får hastigheten til en Clearnet-tilkobling. For en On-Chain Wallet kan denne gevinsten virke marginal, men hvis du planlegger å sette opp din egen Lightning-node på et senere tidspunkt, er forskjellen betydelig. Å foreta betalinger via noden din på farten på Tor er ekstremt tregt på grunn av de mange utvekslingene som kreves, mens det fungerer perfekt med Tailscale.





- Du trenger ikke å konfigurere NAT-regler, åpne porter eller sette opp en vanlig VPN-server. Når applikasjonen er installert på Umbrel og enhetene dine, etableres nettverket automatisk.



Tailscale på Umbrel er derfor en svært interessant løsning hvis du ønsker å få tilgang til noden din fra hvor som helst i verden på en sikker, høytytende og lettkonfigurert måte, uten å ofre personvern eller sikkerhet.



For å installere og konfigurere Tailscale på din Umbrel, se denne veiledningen, avsnitt 4: "*Bruke Tailscale på Umbrel*":



https://planb.network/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Nostr



Nostr, en forkortelse for "*Notes and Other Stuff Transmitted by Relays*", er en åpen, desentralisert protokoll som er utviklet for å gjøre det mulig å publisere og utveksle meldinger på Internett uten å være avhengig av en sentralisert plattform. Hver bruker har et par kryptografiske nøkler: den offentlige nøkkelen (`npub`), som fungerer som en identifikator, og den private nøkkelen (`nsec`), som brukes til å signere meldinger og garantere deres autentisitet.



Meldinger overføres via et nettverk av uavhengige reléer. Denne distribuerte arkitekturen gjør Nostr motstandsdyktig mot sensur: Ingen enkelt server kontrollerer tilgang eller distribusjon, og en bruker kan koble seg til så mange reléer han eller hun ønsker.



Denne protokollen er svært populær i Bitcoin-fellesskapet fordi Nostr, i likhet med Bitcoin, tar opp spørsmål om digital suverenitet og datakontroll. Skaperen, Fiatjaf, er en utvikler som allerede er anerkjent i økosystemet for sine mange bidrag.



Med din Umbrel kan du optimalisere din bruk av Nostr. Ved å installere ***Nostr Relay***-applikasjonen kan du være vert for ditt eget private relé direkte på maskinen din, noe som sikrer at alle innleggene og interaksjonene dine på Nostr lagres lokalt og ikke kan gå tapt gjennom sletting av offentlige reléer.



Nostr-klientene ***noStrudel*** eller ***Snort*** er også tilgjengelige på Umbrel. Takket være disse applikasjonene kan du publisere, lese, søke etter profiler og samhandle med Nostr-økosystemet direkte fra Interface-nettverket på Umbrel.



Til slutt er det ***Nostr Wallet Connect***-appen på Umbrel, som muliggjør innfødte Lightning-betalinger i Nostr. Konkret kan du koble din fremtidige Lightning-node til Nostr-kundene dine for å sende mikrobetalinger, kalt "*zaps*", for å belønne innhold eller samhandle på en inntektsgivende måte, uten å måtte gå gjennom en tredjeparts tjeneste. Disse betalingene sendes direkte fra din personlige node via dine kanaler.



For å finne ut hvordan du bruker alle disse programmene, anbefaler jeg at du tar en titt på denne komplette veiledningen:



https://planb.network/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

### BTCPay-server



BTCPay Server er en gratis betalingsprosessor med åpen kildekode som gjør det mulig for deg å akseptere betalinger via Bitcoin og Lightning Network uten mellomledd, samtidig som du beholder egenbevaringen av midlene.



BTCPay Servers arkitektur er basert på en Bitcoin-node og, for Lightning, på en kompatibel implementering (LND, Core Lightning ...), noe som gjør den til en av de eneste PoS-løsningene som ikke er helt frihetsberøvende. Det er også den mest omfattende programvaren for sporing og regnskap.



![Image](assets/fr/091.webp)



Hvis du eier en bedrift og ønsker å ta imot Bitcoin-betalinger direkte via Umbrel-noden din, er BTCPay Server-applikasjonen ideell for deg. For å finne ut mer om dette emnet, anbefaler jeg at du konsulterer følgende ressurser:





- BIZ 101-kurset om bruk av Bitcoin i virksomheten din:



https://planb.network/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a



- POS 305-kurset om bruk av BTCPay Server:



https://planb.network/courses/6fc12131-e464-4515-9d3f-9255365d5fa1



- BTCPay Server-veiledningen:



https://planb.network/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


# Avanserte konsepter og beste praksis


<partId>fc77a62a-8d9f-4144-9080-3057b04db2c6</partId>



## Vedlikehold av Umbrel-knuten din


<chapterId>06d77d09-bf24-4555-b2ba-c08bbda477c7</chapterId>



Før jeg går videre til mer avansert teori, vil jeg i dette siste kapittelet ta for meg beste praksis og konkrete tiltak du kan iverksette når Umbrel-noden din er installert, synkronisert og riktig konfigurert. Hvordan vedlikeholder du den på daglig basis?



### Hold utstyret friskt



En pålitelig node starter med stabil maskinvare. Sørg for at maskinen som huser noden, er godt ventilert, Dust-fri og installert i et tørt miljø, borte fra kilder til varme og fuktighet. Unngå å stappe den inn i et trangt rom, og velg et godt ventilert sted.



På Raspberry Pi og mini-PC-er tetter Dust til slutt kjøleribbene, noe som øker temperaturen og fører til struping (frivillig begrensning av ressursbruken), noe som igjen resulterer i at nodens effektivitet synker. Derfor anbefaler jeg å rengjøre luftinntaket og viften med jevne mellomrom, helst med noen måneders mellomrom.



Sørg for at du bruker en høykvalitets strøm Supply, da ustabil spenning kan føre til systemkorrupsjon og til og med utgjøre en brannfare. Ideelt sett bør du bruke den originale strømforsyningen Supply som leveres av produsenten av maskinen din. Vær også oppmerksom på overoppheting på grunn av Joule-effekten på strømskinner: Overhold alltid den maksimalt tillatte effekten, og koble aldri til flere strømskinner i kaskade.



Jeg anbefaler også at du investerer i en UPS. Dette beskytter noden din mot plutselige nedstengninger, gjør det mulig for Umbrel å stenge ned rent i tilfelle strømbrudd, og sikrer kontinuitet i driften ved mikroavbrudd eller kortvarige feil.



På lagringssiden bør du holde et øye med utviklingen: Hvis disken nærmer seg metning, bør du vurdere å frigjøre plass (avinstaller ubrukte apper, juster indekseringsinnstillingene) eller migrere til en større SSD. Ulempen med en full Bitcoin-node er at lagringskravene øker kontinuerlig, ettersom det genereres en ny blokk hvert 10. minutt, og gamle blokker ikke kan slettes (med mindre noden er pruned). Jeg anbefaler deg derfor å planlegge for en tilstrekkelig stor kapasitet når du kjøper maskinvare (minimum 2 TB).



### Oppdatering



Nodeoppdateringer er viktige av tre hovedgrunner: for det første sikkerhet (sårbarhetsoppdateringer, nettverksherding og DoS-beskyttelse); for det andre kompatibilitet (endringer i relépolicyer, formatendringer og protokolloppgraderinger); og for det tredje pålitelighet og ytelse (feilrettinger, ressursforbruk og andre forbedringer). Sjekk derfor med jevne mellomrom at UmbrelOS og appene dine er oppdaterte:





- Slik oppdaterer du systemet: Åpne innstillingsmenyen, og klikk deretter på knappen "*Sjekk etter oppdatering*" ved siden av parameteren "*UmbrelOS*".



![Image](assets/fr/042.webp)





- Slik oppdaterer du programmer: Gå til App Store. Hvis noen av applikasjonene dine må oppdateres, vises en knapp med en rød boble øverst til høyre på Interface. Klikk på den, og oppdater deretter hver enkelt applikasjon.



Utfør denne operasjonen regelmessig for å holde operativsystemet og programmene oppdatert.



### Sikkerhetskopier



Hvis du bare bruker din Bitcoin-node til å validere og distribuere transaksjonene dine, men lommebøkene dine administreres utenfor Umbrel (f.eks. med en Hardware Wallet og Sparrow wallet), er det ingenting å sikkerhetskopiere direkte til Umbrel. I dette tilfellet er den viktigste sikkerhetskopien fortsatt gjenopprettingsfrasen og Descriptor til din eksterne Wallet, og dette gjelder uansett om du bruker din egen node eller ikke. Så ingenting endres fra din tidligere konfigurasjon.



På den annen side kan det være behov for ytterligere sikkerhetskopier, avhengig av hvilke andre applikasjoner du bruker på Umbrel. Dette gjelder spesielt hvis du bruker en Lightning-node på Umbrel. I dette tilfellet er det helt avgjørende å ta sikkerhetskopi av seed som ble levert da du installerte Lightning-noden. I tillegg til seed trenger du en oppdatert ***Static Channel Backup (SCB)*** for å kunne gjenopprette Lightning-noden hvis det skulle oppstå et problem. SCB gjør at du kan gjenopprette midlene dine ved å tvangslukke kanaler. Hvis enten seed eller SCB mangler, er det umulig å gjenopprette en Lightning-node.



Umbrel tilbyr også muligheten til automatisk og dynamisk sikkerhetskopiering av denne SCB-en på serverne deres, via Tor, for å sikre at en oppdatert fil alltid er tilgjengelig. I dette tilfellet er det bare seed som trengs for å gjenopprette noden.



Vi kommer tilbake til disse aspektene i detalj i neste LNP202-kurs.



### Daglig driftssikkerhet



Når det gjelder sikkerhet, må du bruke et langt, unikt og tilfeldig passord for Interface Umbrel, og husk å aktivere tofaktorautentisering (2FA). For applikasjoner som tilbyr både passord- og 2FA-beskyttelse, bør du alltid aktivere begge deler og endre standardpassordene.



Eksponer aldri dashbordet for Internett uten å bruke en sikker gateway (for eksempel et VPN, Tor eller kun lokal tilgang). Begrens antallet applikasjoner du installerer, og slett regelmessig de du ikke lenger trenger, for å redusere angrepsflaten.



Hvis du vil fordype deg i datasikkerhet generelt, anbefaler jeg deg å sjekke ut dette andre gratiskurset:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Diagnose og hjelp til selvhjelp



Hvis det oppstår en feil på Umbrel, må du først generate en diagnostikkpakke via feilsøkingsdelen i UmbrelOS eller det aktuelle programmet, og deretter starte programmet på nytt. Om nødvendig kan du også prøve å starte systemet på nytt.



Hvis problemet vedvarer, anbefaler jeg at du [blir med i Umbrel-brukerfellesskapet på deres Discord] (https://discord.gg/efNtFzqtdx). Begynn med å gjøre et søk for å finne ut om noen allerede har støtt på samme problem og funnet en løsning. Hvis ikke, kan du legge inn en melding i kanalen `general-support`. Du kan også bruke [Umbrel-forumet](https://community.umbrel.com/).



På disse områdene kan du ikke bare følge med på sikkerhetsmeldinger og -oppdateringer, men også stille spørsmål og hjelpe andre brukere. Det er ofte i disse utvekslingene at man oppdager beste praksis.



Med disse enkle vanene vil Umbrel-noden forbli stabil, trygg og nyttig, både for deg og for Bitcoin-nettverket.




## Forståelse av IBD og peer discovery-prosessen


<chapterId>175ac9d1-ea23-45d9-9918-d3e7352435cd</chapterId>



Bitcoin-noden starter opp uten noen forhåndskunnskap om transaksjonshistorikk. Til å begynne med er den bare en datamaskin som kjører programvare (Bitcoin core eller lignende). For å bli en fullt synkronisert og operativ Bitcoin-node må den rekonstruere tilstanden til Ledger lokalt ved å sjekke alle blokker som er publisert siden Genesis-blokken (blokk 0, publisert av Satoshi Nakamoto den 3. januar 2009). Dette trinnet kalles **IBD (_Initial Block Download_)**.



IBD består i å laste ned og verifisere hver blokk og transaksjon individuelt, ved hjelp av konsensusreglene, for å bygge sin egen versjon av Blockchain. Målet er ikke bare å hente en kopi av ubekreftede data, men å komme frem til samme konklusjon helt uavhengig, som det ærlige flertallet i nettverket.



![Image](assets/fr/092.webp)



### IBD-milepæler



Synkroniseringen begynner med _**headers-first**_-trinnet. Noden din ber om sekvensen av blokkoverskrifter fra flere peers, og for hver av dem verifiserer den Proof of Work, justering av vanskelighetsgrad, syntaks, samt Timestamp og versjonsnummerregler. Kort sagt sikrer den at hvert mottatte header er i samsvar med konsensusreglene.



![Image](assets/fr/093.webp)



Som en påminnelse består en Bitcoin-blokk av et 80 byte stort hode og en liste over transaksjoner. Blokkens fingeravtrykk oppnås ved å bruke en dobbel SHA-256 Hash på dette overskriften, som inneholder 6 felt:




- versjon
- Hash fra forrige blokk
- Merkle Root av transaksjoner
- Timestamp (større enn mediantiden for de foregående 11 blokkene)
- vanskelighetsmål
- Nonce



![Image](assets/fr/094.webp)



Transaksjoner blir forpliktet til en Merkle Tree. Dette er en struktur som oppsummerer et stort sett med data (i dette tilfellet alle transaksjonene i blokken) ved å aggregere hashene to og to ned til en enkelt "rot", og dermed bevise at et element tilhører settet (og oppdage eventuelle endringer). På denne måten vil enhver endring av en transaksjon også endre roten til Merkle Tree og dermed blokkoverskriftens fingeravtrykk. SegWit har introdusert en separat ekstra Commitment for informasjonskapsler (signaturer), plassert i myntbasen.



![Image](assets/fr/095.webp)



Dette _**headers-first**_-trinnet gjør det mulig for noden å identifisere grenen med mest arbeid (uavhengig av antall blokker), som er den grenen som Bitcoin-nodene synkroniseres på. Når denne grenen er identifisert, laster noden ned innholdet i blokkene parallelt fra flere tilkoblinger, og validerer deretter hver transaksjon: format, skriptenes gyldighet (unntatt `assumevalid=1`), beløp og fravær av dobbeltutgifter. For hver vellykket sjekk oppdateres den nåværende statusen for ubrukte mynter (UTXO-settet) i `chainstate/`-databasen: brukte utganger fjernes, mens nye gyldige utganger legges til.



Mempool, derimot, kommer bare inn i bildet når man nærmer seg toppen av kjeden: Så lenge noden er sent ute, har den ingen ventende transaksjoner å lagre.



Når IBD er fullført, går noden inn i sin normale fase: Den validerer nye blokker etter hvert som de publiseres, vedlikeholder Mempool med ventende transaksjoner i henhold til sine reléregler, reléerer transaksjoner og blokker og håndterer eventuelle omorganiseringer av kjeden.



### AssumeValid



Bitcoin core inneholder en mekanisme som er utformet for å redusere tiden det tar før en node er fullt operativ, samtidig som essensen i det autonome verifiseringsprinsippet beholdes: AssumeValid.



Parameteren `assumevalid` er basert på en tidligere referanseblokk, som Hash er integrert i hver programvareversjon. Hvis noden under IBD finner ut at denne blokken faktisk er på grenen med mest arbeid, kan den ignorere skriptverifisering for alle transaksjoner før dette punktet.



Alle andre regler (blokkstruktur, Proof of Work, størrelsesgrenser, transaksjonsbeløp, UTXO osv.) forblir fullstendig verifisert. Det er bare beregningen av skript før denne referanseblokken som ignoreres. Ytelsesgevinsten er betydelig på IBD, ettersom signaturverifisering står for en stor del av CPU-belastningen. Etter denne referanseblokken går verifiseringen tilbake til normal tilstand.



Du kan tvinge frem full validering av alle skript ved å deaktivere denne mekanismen, på bekostning av en mye lengre IBD, ved hjelp av parameteren `assumevalid=0` i filen `Bitcoin.conf`.



### AntaUTXO



`assumeutxo` er en annen eksisterende parameter, men i motsetning til `assumevalid` er den ikke aktivert som standard. Denne mekanismen gjør det mulig for programvaren å laste inn et øyeblikksbilde av UTXO-settet, sammen med metadataene, og foreløpig betrakte det som en referansetilstand, etter å ha verifisert at overskriftene faktisk fører til den Blockchain som har mest arbeid.



Noden blir dermed raskt operativ for vanlige bruksområder (RPC, tilkobling av lommebøker osv.), samtidig som den starter en fullstendig, verifisert rekonstruksjon av sitt eget UTXO-sett i bakgrunnen. Når denne fasen er fullført, erstattes det opprinnelige øyeblikksbildet av den lokalt rekonstruerte tilstanden. Denne tilnærmingen skiller rask nodeoppretting fra full verifisering, uten at det går på bekostning av sistnevnte.



### Peer-oppdagelse: Hvordan finner noden din Bitcoin-nettverket?



Når en node starter opp for første gang, kjenner den ennå ingen andre noder. Den må imidlertid finne andre Bitcoin-noder på Internett for å be om headere, og deretter blokker, for å fullføre IBD-en. For å initiere disse forbindelsene følger Bitcoin core en prioritert logikk.



![Image](assets/fr/096.webp)



Når noden starter på nytt etter å ha vært i bruk, forsøker Core først å koble seg til utgående peers som ble registrert før nedstengningen, informasjon som er lagret i filen `anchors.dat`. Deretter konsulterer den IP Address-boken **`peers.dat`**, som lagrer listen over tidligere motparter, for å koble seg til dem på nytt. Dette er ganske enkelt en lokal fil som oppdateres og oppbevares av Core. For en ny node som nettopp har blitt lansert, er disse to filene derimot tomme, siden den aldri har kommunisert med andre Bitcoin-noder.



I dette tilfellet spør programvaren _**DNS seeds**_. Dette er [servere som vedlikeholdes av anerkjente økosystemutviklere] (https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp), som returnerer en liste over IP-adresser til antatt aktive noder. Disse adressene gjør det mulig for den nye noden å starte sine første tilkoblinger og be om de nødvendige dataene fra IBD-en. Her er listen over *DNS-frø* som er aktive til dags dato (august 2025):




- Pieter Wuille: `seed.Bitcoin.sipa.be.`
- Matt Corallo: `dnsseed.bluematt.me.`
- Luke Dashjr: `dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us.``
- Jonas Schnelli: `seed.Bitcoin.jonasschnelli.ch.`
- Peter Todd: `seed.btc.petertodd.net.`
- Sjors Provoost: `seed.Bitcoin.sprovoost.nl.`
- Stephan Oeste: `dnsseed.emzy.de.`
- Jason Maurice: `seed.Bitcoin.wiz.biz.`
- Ava Chow: "seed.Mainnet.achownodes.xyz



I de aller fleste tilfeller er *DNS seeds*-trinnet tilstrekkelig for å etablere de første forbindelsene med andre noder. Hvis disse serverne unntaksvis ikke svarer innen 60 sekunder, bytter noden til en annen metode: [En statisk liste med over 1000 adresser (https://github.com/Bitcoin/Bitcoin/blob/master/src/chainparamsseeds.h) over _seed-noder_ er innebygd i Bitcoin core-koden og oppdateres jevnlig. Hvis de to første metodene for å skaffe IP-adresser mislykkes, etablerer denne siste løsningen en første forbindelse, som noden deretter kan bruke til å be om nye IP-adresser.



![Image](assets/fr/097.webp)



Som en siste utvei kan du manuelt tvinge frem bestemte tilkoblinger ved hjelp av filen `peers.dat`.



Etter oppstart diversifiserer den interne Address-administratoren kildene (separate autonome nettverk, clearnet og Tor, samt ulike geografiske områder) for å redusere risikoen for topologisk isolasjon. Noden etablerer disse utgående forbindelsene (forbindelser som den selv velger, og som derfor er sikrere).



Hvis noden din lytter på en åpen port (standard er 8333), godtar den innkommende tilkoblinger. Disse forsterker nettverkets generelle robusthet ved å tilby et kontaktpunkt for nye noder, uten at det gir noen spesiell fordel for din egen IBD. Hvis noden din kjører på Tor, forblir logikken den samme, men adressene som brukes er `.onion`-tjenester.




## Bitcoin-knutens anatomi


<chapterId>b420bd9d-7e2a-4984-bc70-2b732a94c8ce</chapterId>



Når noden har fullført den innledende synkroniseringen, lagrer den flere utfyllende datasett lokalt, slik at den kan validere blokker og transaksjoner, betjene nettverkskolleger og starte raskt på nytt samtidig som den opprettholder tilstanden sin. 3 hovedklosser er essensielle på en node:




- gW-402 **blokker** lagret på disk,
- **UTXO-settet** som vedlikeholdes i en nøkkelverdidatabase,
- og **Mempool** lagres i RAM og serialiseres med jevne mellomrom.



I tillegg finnes det flere hjelpefiler (jevnaldrende, avgiftsestimater, eksklusjonslister, lommebøker osv.) som kompletterer bildet. La oss finne ut hvilken rolle alle disse filene spiller.



### Hvor befinner dataene til noden seg egentlig?



Som standard lagrer Bitcoin core dataene sine i en bestemt arbeidskatalog. Under GNU/Linux er dette vanligvis i `~/.Bitcoin/`, under Windows i `%APPDATA%\Bitcoin/`, og under macOS i `~/Library/Application Support/Bitcoin/`. Hvis du bruker en pakkeløsning (f.eks. i en node-distribusjon), kan denne katalogen være montert et annet sted, men strukturen forblir den samme. De viktige undermappene og filene som er beskrevet nedenfor, ligger fortsatt her.



![Image](assets/fr/098.webp)



### Blokkene



Blockchain er derfor en samling av blokker. En Full node lagrer disse blokkene som sekvensielle flate filer og opprettholder en parallell indeks for rask gjenfinning. Ved behov (omorganisering, Wallet rescanning, peer-service) leses disse dataene inn på nytt.



**En omorganisering, eller resynkronisering, er et fenomen der Blockchain gjennomgår en endring i strukturen fordi det finnes konkurrerende blokker i samme høyde. Dette skjer når en del av Blockchain erstattes av en annen kjede med en større mengde akkumulert arbeid. Disse resynkroniseringene er en naturlig del av Bitcoins drift, der forskjellige utvinnere kan finne nye blokker nesten samtidig, og dermed dele Bitcoin-nettverket i to. I slike tilfeller kan nettverket midlertidig splittes i konkurrerende kjeder. Etter hvert som en av disse kjedene akkumulerer mer arbeid, blir de andre kjedene forlatt av nodene, og blokkene deres blir kjent som "foreldede blokker" eller "orphan blocks" Denne prosessen med å erstatte en kjede med en annen kalles resynkronisering.



#### Blk*.dat-filer (rå blokkdata)



Mottatte og validerte blokker skrives til sekvensielle containere med navnet `blkNNNNNNN.dat`, som lagres i mappen `blocks/`. Hver fil fylles i rekkefølge til den når en maksimal størrelse på 128 MiB, og Core åpner da neste fil. Hver blokk er serialisert i nettverksformat, innledet med en magisk identifikator og en lengde. Denne organiseringen muliggjør rask skriving til disk og gjør det enklere å synkronisere jevnaldrende.



![Image](assets/fr/099.webp)



I pruned-modus beholder noden bare et nylig vindu av disse filene for å begrense diskavtrykket. Den sletter de eldste `blk*.dat`-containerne så snart det konfigurerte plassmålet er nådd, samtidig som den beholder tilstrekkelig historikk til å forbli konsistent med den best kjente kjeden. Indeksen og UTXO-settet forblir normale, slik at de neste transaksjonene og blokkene kan valideres.



#### Rev*.dat-filer (kanselleringsdata)



For å kunne gå tilbake i tid under en omorganisering, lagrer Core, parallelt med hver `blk`-fil, en `revNNNNNNN.dat`-fil i `blocks/`. Denne filen inneholder informasjonen som trengs for å oppheve effekten av en blokk på UTXO-settet: For hver utgang som forbrukes av blokken, lagres den forrige tilstanden til den tilsvarende UTXO (mengde, skript, høyde ...). Hvis en blokk avbrytes, kan noden raskt rekonstruere den forrige tilstanden uten å måtte skanne hele kjeden på nytt.



![Image](assets/fr/100.webp)



#### Blokkindeks (blokker/indeks)



Det ville være for tidkrevende å søke etter en blokk direkte i flatfilene. Core vedlikeholder derfor en LevelDB-database i `blocks/index/`, som for hver kjent blokk viser metadata som Hash, høyde, valideringsstatus, `blk`-fil og offset der den er plassert. Når en peer ber om en blokk, eller når en intern komponent trenger tilgang til en bestemt blokk, gir denne indeksen rask tilgang. Uten denne indeksen ville det vært nødvendig med for mange operasjoner.



![Image](assets/fr/101.webp)



#### Valgfrie indekser (indekser/)



Noen indekser er valgfrie og deaktiveres som standard, ettersom de øker diskplassforbruket:




- `indexes/txindex/`, som vi allerede har nevnt, inneholder en transaksjons → lokasjonstilordningstabell, som gjør det mulig å hente en bekreftet transaksjon uten å vite hvilken blokk den ligger i. Dette er nyttig for RPC-spørringer av typen `getrawtransaction` utenfor Wallet , men er ganske dyrt.
- indexes/blockfilter/`, som kan inneholde kompakte blokkfiltre (BIP157/158) for tynne klienter. Disse strukturene fremskynder verifisering på klientsiden på bekostning av ekstra lagringsplass på indekseringsnoden.



### UTXO-sett (kjedestatus)



UTXO-modellen (*Ubrukt transaksjonsutgang*) er den regnskapsmessige representasjonen av Bitcoin: Hver ubrukt utgang er en tilgjengelig "Coin" som kan brukes som inndata for en fremtidig transaksjon.



![Image](assets/fr/102.webp)



Summen av alle disse delene på et gitt tidspunkt T utgjør UTXO-settet: en stor liste over alle delene som nå er tilgjengelige. Det er denne tilstanden noden konsulterer for å avgjøre om en transaksjon bruker legitime enheter som ikke allerede er brukt i en tidligere transaksjon (for å unngå Double-spending).



![Image](assets/fr/103.webp)



UTXO-settet lagres i mappen `chainstate/` som en kompakt LevelDB-database. Hver del assosierer en nøkkel avledet fra Hash for transaksjonen og utgangsindeksen med en verdi som inneholder: beløpet, `scriptPubKey`-låsen, høyden på opprettelsesblokken og en coinbase-indikator.



![Image](assets/fr/104.webp)



Noden opprettholder en minnebuffer over LevelDB for å absorbere hyppige lese- og skriveoperasjoner. Parameteren `dbcache` kan brukes til å endre størrelsen på denne hurtigbufferen: Jo større den er, desto mer minnetilgang får IBD og gjeldende validering nytte av, på bekostning av høyere RAM-forbruk. Når en Miner finner en ny blokk, sletter noden utdataene som er brukt (eller forbrukt) av transaksjonene som inngår i blokken, fra UTXO-settet, og legger til de nyopprettede utdataene.



Teoretisk sett kan vi validere en transaksjon ved å skanne blokkhistorikken på nytt for å kontrollere at en utbetaling aldri har blitt brukt. I praksis ville dette imidlertid være altfor tidkrevende, ettersom hele Blockchain måtte skannes for hver nye transaksjon. UTXO-settet gir derfor den minste oversikten som kreves for å bevise lokalt og innen rimelig tid at Double-spending ikke finnes.



Merk at UTXO-settet ofte er kjernen i bekymringene om Bitcoins desentralisering, ettersom størrelsen naturlig nok øker raskt. Dette skyldes delvis den stigende prisen på Bitcoin, som oppmuntrer til fragmentering av deler, og delvis den økende bruken av systemet: jo flere brukere det er, desto større er etterspørselen etter UTXO-er.



![Image](assets/fr/105.webp)



Veksten i UTXO-settet stammer også fra strukturen til enkle betalingstransaksjoner på Bitcoin. Når du foretar en betaling, bruker du en enkelt UTXO som input og oppretter to nye UTXO-er som output (én for betalingen og én for Exchange). Til slutt gir en kjedeanalyseheuristikk, kalt CIOH (*Common Input Ownership Heuristic*), et ytterligere insentiv til å unngå Coin-konsolidering.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Siden en del av den må oppbevares i RAM for å verifisere transaksjoner innen rimelig tid, kan UTXO-settet gradvis gjøre driften av en Full node for kostbar. Det finnes allerede noen få forslag for å løse dette problemet, blant annet [Utreexo] (https://planb.network/resources/glossary/utreexo).



### Mempool



Mempool er det lokale settet med gyldige transaksjoner som er mottatt, men ennå ikke bekreftet. Som en påminnelse er en "bekreftet transaksjon" en transaksjon som er inkludert i en gyldig blokk. Hver node opprettholder sin egen Mempool, som kan avvike fra andre noder i nettverket avhengig av:




- størrelsen som er allokert til Mempool via parameteren `maxmempool`: en node med en større Mempool vil kunne romme flere transaksjoner enn en node med en mindre Mempool (med mindre sistnevnte blir tom);
- gW-433-regler: Disse er en delmengde av nodens reléregler og definerer egenskapene som en ubekreftet transaksjon må oppfylle for å bli akseptert i Mempool;
- transaksjonsperkolasjon: På grunn av ulike faktorer kan en gitt transaksjon ha blitt distribuert til én del av nettverket, men ennå ikke nådd en annen.



Det er viktig å merke seg at node-mempooler ikke har noen konsensusverdi. Bitcoin fungerer perfekt selv om hver node har en annen Mempool. Til syvende og sist er de autoritative blokkene alltid de som legges til i Blockchain. Selv om en node for eksempel først avviser en gitt transaksjon i sin Mempool (som er gyldig i henhold til konsensusreglene), vil den være forpliktet til å godta den hvis den til slutt inkluderes i en blokk med en gyldig Proof of Work. Hvis den ikke gjør det og avviser denne blokken, selv om den overholder konsensusreglene, vil den utløse en Hard Fork, det vil si at det opprettes en ny, separat Bitcoin som den vil være alene om.



#### Retningslinjer og håndtering av minne



Når en transaksjon mottas, utfører Core en rekke kontroller mot konsensusregler (syntaks, gyldige skript, ingen dobbeltutgifter osv.) og Mempool-regler, som er en lokal policy (RBF, minimumsgrenser for belastning, datagrense i `OP_RETURN` osv.) Hvis transaksjonen overholder disse reglene, lagres den i minnet.



Størrelsen på Mempool er begrenset av parameteren `maxmempool` i filen `Bitcoin.conf` (mer om dette i neste kapittel). Som standard er grensen 300 MB. Når den er full, hever noden dynamisk minimumsgrensen for ladning og utviser de minst lønnsomme transaksjonene først (det vil si at den beholder transaksjoner som bør utvinnes først). Transaksjoner som er for gamle, kan også utløpe etter en konfigurert forsinkelse.



#### Mempool utholdenhet på disk



For å gjøre det raskere å starte opp igjen, serialiserer Core med jevne mellomrom tilstanden til Mempool i filen `Mempool.dat` når noden slås av. I tillegg til selve Mempool, som forblir i minnet, lagrer Core denne `Mempool.dat`-filen på disken. Neste gang noden startes, lastes dette øyeblikksbildet inn på nytt, og alt som ikke lenger er gyldig for den aktuelle Blockchain, slettes.



### Hjelpefiler og databaser



Flere andre filer på samme nivå som `blocks/`, `chainstate/` og `indexes/` bidrar til at systemet fungerer som det skal:




- `peers.dat` inneholder en IP Address-bok med potensielle peers, som er matet inn gjennom innledende DNS-oppdagelse, nettverksutveksling og manuelle tillegg. Når noden starter opp, kan den bruke denne filen til å etablere utgående tilkoblinger.
- Når noden slås av, lagrer `anchors.dat` adressene til utgående peers, slik at du raskt kan prøve å kontakte dem igjen neste gang du starter opp.
- `banlist.json` inneholder lokale forbud som er besluttet av operatøren eller av noden (gjentatt ugyldig oppførsel), for å hindre noden i å koble seg til eller godta tilkoblinger fra disse spesifikke motpartene.
- `fee_estimates.dat` lagrer tidshorisontstatistikk over observerte bekreftelser, som brukes av gebyrestimatoren til å foreslå gebyrsatser som er i samsvar med forsinkelsesmålene som velges når en transaksjon opprettes.
- gW-446.conf` inneholder nodens konfigurasjonsparametere. Det er her du kan justere reléreglene. Jeg skal fortelle deg mer om dette i neste kapittel.
- `settings.json` inneholder flere parametere til `Bitcoin.conf`.
- `debug.log` er den diagnostiske tekstloggen, som kan brukes til å forstå nodeaktiviteten hvis det oppstår en feil.
- gW-448.pid` lagrer prosessidentifikatoren ved kjøring, slik at andre programmer eller skript enkelt kan identifisere bitcoind (*Bitcoin daemon*) og samhandle med den om nødvendig. Den opprettes ved oppstart av noden og slettes ved avslutning.
- `ip_asn.map` er en IP → ASN-tilordningstabell (frittstående system) som brukes til bucketing og peer-diversifisering (`-asmap`-alternativet).
- `onion_v3_private_key` lagrer den private nøkkelen til Tor v3-tjenesten når alternativet `-listenonion` er aktivert, for å holde en stabil onion Address mellom omstarter.
- `i2p_private_key` lagrer den private I2P-nøkkelen når `-i2psam=` brukes til å opprette utgående og eventuelt innkommende tilkoblinger på I2P.
- `.cookie` inneholder en kortvarig RPC autentisering token (opprettet ved oppstart, slettet ved avslutning) når cookie-autentisering brukes. Denne kan for eksempel brukes til å koble til Wallet-programvare.
- `.lock` er låsen for datakatalogen, som hindrer flere instanser i å skrive til samme datadir samtidig.
- `guisettings.ini.bak` er den automatiske lagringen av GUI-innstillinger (*Bitcoin Qt*) når alternativet `resetguisettings` brukes.



Som vi så i de første delene av dette BTC 202-kurset, er Bitcoin core både Bitcoin nodeprogramvare og Wallet. Det er imidlertid ikke nødvendigvis løsningen jeg vil anbefale for å administrere lommebøkene dine, ettersom Interface forblir grunnleggende og funksjonalitetene er begrenset sammenlignet med moderne programvare som Sparrow eller Liana. Core inneholder også filer for å administrere lommebøkene dine:





- `wallets/` er standardkatalogen som inneholder en eller flere;
- `wallets/<name>/Wallet.dat` er SQLite-databasen til Wallet (nøkler, deskriptorer, transaksjonsmetadata osv.);
- wallets/<name>/Wallet.dat-journal` er SQLite-tilbakestillingsloggen.



For å oppsummere, her er Bitcoin core-filstrukturen:



```
~/.bitcoin/
├── bitcoin.conf
├── blocks/
│   ├── blk00000.dat
│   ├── blk00001.dat
│   ├── rev00000.dat
│   ├── rev00001.dat
│   └── index/
├── chainstate/
├── indexes/
│   ├── txindex/
│   ├── blockfilter/
│   │   └── basic/
│   │       ├── db/
│   │       └── fltrNNNNN.dat
│   └── coinstats/
│       └── db/
├── wallets/
│   └── <wallet_name>/
│       ├── wallet.dat
│       └── wallet.dat-journal
├── peers.dat
├── anchors.dat
├── banlist.json
├── mempool.dat
├── fee_estimates.dat
├── bitcoind.pid
├── debug.log
├── ip_asn.map
├── onion_v3_private_key
├── i2p_private_key
├── settings.json
├── guisettings.ini.bak
├── .cookie
└── .lock
```



### Valideringsstien for en ny blokk



Når noden mottar en ny blokk, sjekker den Proof of Work og, mer generelt, samsvar med konsensusreglene. Hvis alt er i orden, bruker den endringene transaksjon for transaksjon på sitt UTXO-sett: Den kontrollerer at hver oppføring bruker eksisterende UTXO-er med et gyldig skript, sletter disse UTXO-ene og legger til de nye utgangene. Hvis alt er gyldig, blir endringene overført til `chainstate/`.



Parallelt skrives angre-data til `rev*.dat` og metadata til indeksen `blocks/index/`. Blokken blir deretter serialisert til den riktige filen `blk*.dat`. I tilfelle en omorganisering leser noden `rev*.dat` i revers for å koble fra de forlatte blokkene, gjenopprette UTXO-settet og deretter koble til blokkene i den nye beste kjeden.





## Forståelse av Bitcoin.conf


<chapterId>c54a629a-ddb1-41cb-9a88-21dfd9be50ca</chapterId>



Filen `Bitcoin.conf` er den viktigste konfigurasjonsfilen for Interface for Bitcoin core. Den lar deg justere oppførselen og parametrene til noden din uten å måtte rekompilere kildekoden eller gjøre endringer på kommandolinjen. Konkret er det en ren tekstfil som er strukturert i nøkkel-verdi-par, noe som betyr at hver linje i filen refererer til en bestemt parameter (nøkkelen) og den tilhørende verdien, som kan endres for å justere den aktuelle parameteren.



Parametere for nettverk, transaksjonsformidling, ytelse, indeksering, logging og RPC-tilgang kan defineres i `Bitcoin.conf`. Denne konfigurasjonsfilen endrer imidlertid aldri protokollens konsensusregler: Den angir bare nodens lokale policy (videresendingsregler), måten den kobler seg til, indekserer og eksponerer tjenester på.



### Plassering og prioritering



Som standard ligger `Bitcoin.conf` i Bitcoin core-datakatalogen. Dette er den berømte katalogen vi nevnte i forrige kapittel. Denne filen opprettes imidlertid ikke automatisk av Bitcoin core, bortsett fra i visse miljøer, for eksempel Umbrel. Hvis den ikke allerede finnes, må du generate lage den selv ved å opprette en fil med navnet `Bitcoin.conf`, og deretter åpne den i en teksteditor for å gjøre endringene dine.



Parametrene som er definert i `Bitcoin.conf` kan overstyres av 2 lag:




- `settings.json` (skrevet dynamisk av Interface graphics eller noen RPC),
- og alternativer som endres via kommandolinjer.



Vær oppmerksom på at alle endringer i `Bitcoin.conf` krever en omstart av noden for å tre i kraft.



### Format og struktur



Formatet på `Bitcoin.conf` er derfor svært enkelt: én linje per opsjon, på formen `option=value`. Unødvendige mellomrom og blanke linjer ignoreres, og kodekommentarer begynner med `#`.



Nesten alle boolske alternativer kan deaktiveres med et `no`-prefiks. For eksempel er `listen=0` og `nolisten=1` ekvivalente, avhengig av versjon.



For å segmentere konfigurasjonen etter nettverk kan du bruke seksjoner: `[main]`, `[test]` (testnet3), `[testnet4]`, `[bookmark]`, `[regtest]`. Alternativt kan du sette `regtest.maxmempool=100` foran navnet på opsjonen.



### Hva Bitcoin.conf kan og ikke kan gjøre



Som forklart ovenfor kan konsensusregler åpenbart ikke konfigureres i `Bitcoin.conf`, da dette kan skape en Hard Fork. På den annen side er det mange andre aspekter som kan konfigureres. Det er tre nyttige klasser å huske på:




- Rent lokale parametere. Disse påvirker bare noden din: bufferstørrelse (`dbcache`), pruned-modus (`prune`), valgfrie indekser... De påvirker maskinens ytelse, men ikke nettverket.
- Retningslinjer for relé og Mempool. Disse bestemmer hva noden din aksepterer, beholder og videresender før bekreftelse: minimumsavgiftsterskel (`minrelaytxfee`), Mempool-størrelse og oppbevaringstid (`maxmempool`, `mempoolexpiry`), transaksjonserstatning (RBF)... Disse reglene er ikke en del av konsensus, så to forskjellige noder kan ha forskjellige retningslinjer og likevel være fullt kompatible. På den annen side vil disse parameterne påvirke Bitcoin-nettverket (som forklart i den første delen, særlig med perkolasjonsteori).
- Nettverkstilkobling. Disse alternativene bestemmer hvordan noden finner jevnaldrende, lytter, krysser en NAT, bruker Tor eller en proxy, eller begrenser båndbredden. De former topologien, men endrer ikke videresendingen av transaksjoner.



Det er avgjørende å forstå dette skillet: Hvis en transaksjon ikke overholder konsensusreglene, vil noden din uansett avvise den. Men en strengere lokal policy kan nekte å videresende en transaksjon som er gyldig i konsensusforstand.



### Nettverk og topologi



Først og fremst er det viktig å skille tydelig mellom de to tilkoblingstypene en Bitcoin-node kan ha:




- Utgående forbindelser, som initieres av vår node til en annen node;



![Image](assets/fr/106.webp)





- Innkommende tilkoblinger, initiert av en annen node til vår.



![Image](assets/fr/107.webp)



Disse to forbindelsestypene kan utveksle de samme dataene i begge retninger. Det er ikke et spørsmål om å begrense retningen på datastrømmen, men bare om hvem som er initiativtaker til forbindelsen. Fra vår nodes synspunkt anses utgående tilkoblinger generelt som tryggere, siden vi initierer dem og velger nøyaktig hvilken node vi skal koble oss til, noe som gjør det usannsynlig at tilkoblingen er ondsinnet. Som standard opprettholder Bitcoin core 10 utgående tilkoblinger (8 "*full-relay*" + 2 "*block-relay-only*").



En Full node tilfører mer verdi til nettverket ved å akseptere innkommende tilkoblinger. Parameteren `listen=1` aktiverer lytting på standardporten 8333 i det aktuelle nettverket, slik at disse innkommende tilkoblingene kan mottas på clearnet. For at dette skal fungere, må denne porten også være åpen på ruteren din. Hvis den ikke er det, vil noden din fortsette å fungere med kun utgående tilkoblinger, noe som ikke vil ha noen innvirkning på din personlige bruk av Bitcoin. Du velger selv om du vil tillate innkommende tilkoblinger; det finnes ikke noe "beste valg"



Hvis du foretrekker å ikke åpne en port på ruteren din, men likevel godta innkommende tilkoblinger, kan du aktivere parameteren `listenonion=1`. Dette vil oppnå samme resultat, men bare gjennom Tor-nettverket i stedet for clearnet.



På nettverksnivå har vi også




- `addnode`: legger til en vennlig motpart å kontakte i tillegg til den vanlige oppdagelsen (kan spesifiseres flere ganger).
- connect`: begrenser tilkoblinger strengt til den oppgitte Address (kan angis flere ganger). Kjernen vil ikke koble seg til noen annen node.
- `seednode`: brukes bare til å fylle ut bok-Address når du kobler til en node, og kobler deretter fra.
- `maxconnections`: definerer det globale taket for innkommende + utgående tilkoblinger. Som standard er denne parameteren satt til 125, noe som betyr at noden aldri vil akseptere mer enn 125 tilkoblinger.
- maxuploadtarget`: begrenser opplastinger for å begrense båndbredden over et glidende 24-timers vindu. Dette taket går ikke på bekostning av spredningen av viktige, nylige Elements.
- `onlynet`: begrenser utgående tilkoblinger til kun utvalgte nettverk (`ipv4`, `ipv6`, `onion`, `i2p`, `cjdns`). Hvis du for eksempel vil at noden din bare skal koble seg til Bitcoin-nettverket via Tor, kan du aktivere parameteren `onlynet=onion` og deaktivere innkommende tilkoblinger (eller bare tillate tilkoblinger via Tor også).
- `dnsseed`: Tillater eller forbyr _DNS seeds_ å be om motparter når den lokale Address-poolen er lav (standard: `1`, med mindre `-connect` eller `-maxconnections=0`).
- `forcednsseed`: tvinger _DNS seeds_ til å bli forespurt ved oppstart, selv om du allerede har adresser på lager (standard: `0`).
- `fixedseeds`: Tillat bruk av *seed-noder* (hardkodet Address-liste) hvis _DNS seeds_ mislykkes eller er deaktivert (standard: `1`).
- `dns`: Godkjenner DNS-oppløsninger generelt (f.eks. for `-addnode`/`-seednode`/`-connect`).



Som standard kommuniserer noden din over clearnet, Tor og I2P. Dette betyr at de andre nodene den kobler seg til på clearnet kan se din offentlige IP Address, og Internett-leverandøren din vil sannsynligvis kunne oppdage at du kjører en Bitcoin-node (selv om P2P Transport V2 gjør det vanskeligere for en Internett-leverandør å avlytte). Dette er ikke nødvendigvis et problem, men hvis du vil unngå lekkasje av denne informasjonen, kan du koble noden din utelukkende via Tor-nettverket.



For å være fullt Tor-aktivert må du tvinge Bitcoin core til å bruke bare dette nettverket og opprette en skjult tjeneste for innkommende tilkoblinger (hvis du ønsker å aktivere dem). I `Bitcoin.conf` må du legge til denne konfigurasjonen:




- `onlynet=onion`,
- `proxy=127.0.0.1:9050`,
- `listenonion=1`,
- `torcontrol=127.0.0.1:9051`,
- `proxyrandomize=1`,
- `listen=1`,
- bind=127.0.0.1`,
- `upnp=0`,
- `natpmp=0`.



Alle P2P-tilkoblingene dine går gjennom Tor. Noden din mottar en `.onion` Address for innkommende tilkoblinger, så ingen porter trenger å åpnes på ruteren. Internett-leverandøren din ser bare Tor-trafikk, og de andre brukerne dine er ikke klar over din faktiske offentlige IP Address.



For å unngå DNS-oppløsning i klartekst kan du legge til `dnsseed=0` og `dns=0` i konfigurasjonen. Du må da manuelt oppgi `.onion`-peers via `seednode=` eller `addnode=`, siden det ellers vil være vanskelig å finne nye noder.



Hvis du er nybegynner, vil jeg selvsagt råde deg til å la alle disse nettverksinnstillingene være i fred inntil videre. Standardkonfigurasjonen er ofte tilstrekkelig.



### Mempool og relépolicy



#### Grunnleggende parametere



Her er de grunnleggende parameterne du kan endre i `Bitcoin.conf` når det gjelder administrering av Mempool og videresending av ubekreftede transaksjoner:





- `maxmempool=<n>`: Begrenser den maksimale størrelsen på den lokale Mempool til `<n>` megabyte (standard: `300`). Når grensen er nådd, hever noden dynamisk den effektive gebyrterskelen og prioriterer de minst lønnsomme transaksjonene (basert på gebyrsatsen, ikke den absolutte verdien) for å holde seg under grensen. Du kan la denne innstillingen være standard. Det kan være nyttig å øke den hvis du er Mining alene, eller hvis du ønsker å få en mer nøyaktig oversikt over Mempool overbelastning og forbedre gebyrestimeringen. Hvis du derimot reduserer den, sparer du RAM og, i mindre grad, andre systemressurser.





- `mempoolexpiry=<n>`: Maksimal oppbevaringstid for ubekreftede transaksjoner i Mempool (i timer, standard: `336`). Etter denne tiden fjernes transaksjoner selv om det fortsatt er ledig plass.





- `persistmempool=1`: Lagrer et øyeblikksbilde av Mempool ved stillstand og laster det inn på nytt ved omstart (standard: `1`). Dette gir raskere gjenoppretting etter omstart, slik at du slipper å lære deg tilstanden på nytt via nettverket.





- `maxorphantx=<n>`: Maksimalt antall foreldreløse transaksjoner som beholdes (avhengige inndata fra UTXO-er som ennå ikke er sett i UTXO-settet, standard: `100`). Utover denne terskelen slettes de eldste transaksjonene for å unngå ukontrollert vekst i hurtigbufferen.





- blocksonly=1`: Deaktiverer aksept og videresending av ubekreftede transaksjoner mottatt fra motparter (med mindre spesielle tillatelser er gitt). Noden laster nå bare opp og annonserer blokker. Transaksjoner som opprettes lokalt, kan fortsatt kringkastes (for å bruke noden med Wallet-programvaren). Dette reduserer båndbredde- og RAM-kravene betraktelig, selv om det går på bekostning av redusert nytteverdi for reléet og total uvitenhet om Mempool.





- `minrelaytxfee=<n>`: Minste avgiftssats (i BTC/kvB) under hvilken transaksjoner ikke aksepteres i nodens Mempool og ikke videresendes til motparter (standard: `0,00001` = 1 sat/vB). Jo høyere denne verdien er, desto mer aggressivt filtrerer noden lavkosttransaksjoner.





- `mempoolfullrbf=1`: Godta RBF-transaksjoner selv uten eksplisitt RBF-signalering i den erstattede transaksjonen. Med denne "*full-RBF*"-policyen kan en transaksjon som tilbyr en høyere avgiftssats, erstatte en annen i Mempool hvis de andre erstatningsvilkårene er oppfylt.



Som en påminnelse er RBF en transaksjonsmekanisme som gjør det mulig for avsenderen å erstatte en transaksjon med en som har høyere avgifter for å fremskynde bekreftelsen. Hvis en transaksjon med for lav avgift forblir blokkert, kan avsenderen bruke *Replace-by-fee* til å øke avgiften og prioritere erstatningstransaksjonen i mempools og hos utvinnere.



#### Avanserte og spesifikke innstillinger



Her er de avanserte innstillingene for Mempool og relépolicy. Hvis du er nybegynner, trenger du ikke å endre disse innstillingene:





- datacarrier=1`: Tillater videresending og (hvis Mining via node) inkludering av transaksjoner som inneholder ikke-finansielle data via en `OP_RETURN`-utgang (standard: `1`). Deaktivering av denne parameteren reduserer overflaten for spam med ikke-finansielle data noe, på bekostning av redusert kompatibilitet med visse bruksområder. I alle tilfeller må du akseptere mined `OP_RETURN`.





- `datacarriersize=<n>`: Maksimal størrelse (i byte) på `OP_RETURN` som noden videresender (standard: `83`). Ved å senke denne verdien begrenses nyttelasten som transporteres via `OP_RETURN`. Merk at denne grensen vil bli fjernet som standard i en fremtidig versjon av Bitcoin core.





- `bytespersigop=<n>`: Parameter som konverterer signaturtransaksjoner til ekvivalente byte for evaluering av relegrenser (standard: `20`). Dette vil påvirke aksepten av `sigops`-rike transaksjoner i henhold til lokale policyregler.





- `permitbaremultisig=1`: Tillater videresending av *bare-Multisig* P2MS-transaksjoner (standard: `1`). Dette er den eldste skriptmalen for å etablere multisignaturbetingelser på en UTXO (oppfunnet i 2011 av Gavin Andresen).





- `whitelistrelay=1`: Gir automatisk relétillatelse til innkommende peers som er hvitelistet (standard: `1`). Transaksjonene til disse motpartene blir akseptert av reléet selv om noden ikke er i generell relémodus.





- `whitelistforcerelay=1`: Tildeler "*forcerelay*"-tillatelse til hvitelistede peers med standardtillatelser (standard: `0`). Noden videresender deretter transaksjonene deres selv om de allerede er til stede i Mempool, og omgår dermed anti-redundansmekanismer.





- `whitebind=<[permissions@]addr>` / `whitelist=<[permissions@]CIDR>`: Binder et Interface- eller Address-område og tildeler finkornede tillatelser til de tilsvarende motpartene: `relay`, `forcerelay`, `Mempool` (Mempool-innholdsforespørsel), `noban`, `download`, `addr`, `bloomfilter`. Dette kan være nyttig for å gi privilegert behandling til betrodde motparter (for eksempel gatewayer, LAN og interne tjenester).





- peerbloomfilters=1`: Aktiver støtte for Bloom-filtre (BIP37) for å servere filtrerte blokker/transaksjoner til tynne klienter (standard: `0`). Advarsel: Dette øker belastningen på ressursene dine.





- peerblockfilters=1`: Serverer BIP157 (*Neutrino*) kompakte filtre til motparter (standard: `0`).





- `blockreconstructionextratxn=<n>`: Ekstra antall transaksjoner som beholdes i minnet for å gjenoppbygge kompakte blokker (standard: `100`). Forbedrer rekonstruksjonenes suksess under kompakte synkroniseringer, på bekostning av litt minne.



Som en påminnelse: Alle disse reléreglene har ingen innvirkning på gyldigheten av transaksjoner som inngår i en gyldig blokk. De tjener til å justere ditt bidrag til reléet, beskytte ressursene dine og gjøre noden din forutsigbar i begrensede miljøer, men de gir deg aldri mulighet til å nekte blokker som respekterer konsensusreglene.



### Lommebøker



Du kan også justere måten lommebøkene dine administreres på i filen `Bitcoin.conf`. Hvis du ikke bruker Wallet direkte i Core, men heller ekstern administrasjonsprogramvare som Sparrow eller Liana, vil disse parameterne være av liten betydning:





- addresstype=<legacy|P2SH-SegWit|bech32|bech32m>`: Definerer formatet på Wallet-genererte adresser for mottak.





- `changetype=<legacy|P2SH-SegWit|bech32|bech32m>`: Tving Exchange Address-format (resten av en inngang på en enkelt betaling).





- `Wallet=<sti>`: Laster inn en eksisterende Wallet ved oppstart (kan gjentas for å laste inn flere lommebøker).





- `walletdir=<dir>`: Katalog som inneholder lommebøker (standard: `<datadir>/wallets` hvis den finnes, ellers `<datadir>`). Dette kan være nyttig hvis du ønsker å lagre lommebøker på et dedikert eller kryptert volum.





- `walletbroadcast=1`: Sender automatisk transaksjoner som er opprettet av innlastede lommebøker (standard: `1`). Sett til `0` hvis du ønsker å administrere kringkasting via en annen kanal.





- `walletrbf=1`: Aktiverer RBF opt-in for å signalisere RBF på alle transaksjoner (standard: `1`). Gjør at du kan øke gebyrene senere i tilfelle en transaksjon blokkeres.





- `txconfirmtarget=<n>`: Bekreftelsesmål for transaksjonen (i antall blokker, standard: `6`). Wallet vil automatisk sette gebyret for at transaksjonen skal bekreftes innen dette antallet blokker.





- `paytxfee=<amt>`: Fast gebyrsats (BTC/kvB) som brukes på Wallet-transaksjoner. Unngå generelt: bruk adaptiv estimering via `txconfirmtarget`.





- fallbackfee=<amt>`: Fallback-rate (BTC/kvB) som brukes hvis estimatoren går tom for data (standard: `0,00`). Hvis du setter den til 0, deaktiveres fallback helt.





- `mintxfee=<amt>`: Minimumsterskel (BTC/kvB) for at Wallet skal opprette transaksjoner (standard: `0,00001`). Wallet vil nekte å opprette en transaksjon under denne terskelen.





- `maxtxfee=<amt>`: Absolutt tak på totale gebyrer for en Wallet-transaksjon (standard: `0,10` BTC). Beskytter mot unormalt høye gebyrer som unødvendig ødelegger bitcoins.





- `unngå delvise utgifter=1`: Velger UTXO-er etter Address-klynger for å unngå delvise utgifter.





- `spendzeroconfchange=1`: Tillater at en ubekreftet UTXO Exchange kan gjenbrukes som en oppføring i en ny transaksjon (standard: `1`).





- `consolidatefeerate=<amt>`: Maksimal hastighet (BTC/kvB) som Wallet unngår å legge til flere innsatsfaktorer enn nødvendig for å konsolidere. Dette muliggjør opportunistiske konsolideringer til lave priser og reduserer kostnadene når kostnadene er høye.





- `maxapsfee=<n>`: Budsjett for ekstra kostnader (BTC, absolutt verdi) som Wallet godtar å betale for å aktivere alternativet "*unngå delvise utgifter*".





- `discardfee=<amt>`: Sats (BTC/kvB) som angir toleransen for å kaste Exchange ved å legge det til avgiften. Utganger som vil koste mer enn en tredjedel av verdien med denne satsen, blir droppet.





- `keypool=<n>`: Størrelsen på det forhåndsgenererte Address-biblioteket (standard: `1000`). For små verdier øker risikoen for ufullstendige gjenopprettinger.





- `disablewallet=1`: Starter Bitcoin core uten Wallet-undersystemet og deaktiverer tilknyttede RPC-er. Reduserer angrepsflaten og fotavtrykket hvis noden bare brukes til validering/utgivelse.



### Lagring, indeksering og ytelse



Konfigurasjonsfilen gir deg også mulighet til å justere parametrene for maskinen din. Dette kan være spesielt relevant hvis du har begrensede ressurser, eller tvert imot har mye ledig kapasitet:





- `datadir=<dir>`: Angir Bitcoin cores hoveddatakatalog.





- `blocksdir=<dir>`: Kobler plasseringen av blocks-filene (`blocks/blk*.dat` og `blocks/rev*.dat`) fra `datadir`. Dette kan for eksempel være nyttig hvis du vil plassere blokkarkivet på et annet volum, mens du beholder tilstandsbasen (`chainstate/`) på et raskere medium.





- `dbcache=<n>`: Tildeler `<n>` MiB til databasebufferen (*LevelDB*) som brukes av blokkindeksen og `chainstate` (standard: `450`). Jo høyere verdi, desto raskere blir IBD og strømvalidering, men på bekostning av høyere RAM-forbruk.





- `prune=<n>`: Aktiverer beskjæring av blokkfiler og angir et mål for diskplass i MiB (standard: `0` = deaktivert; `1` = manuell beskjæring via RPC; `>=550` = automatisk beskjæring under målet). Inkompatibel med `txindex=1`. Noden forblir en fullstendig valideringsnode, men kan ikke lenger levere den gamle historikken. Dette alternativet er spesielt nyttig hvis du har begrenset diskplass, for eksempel når du installerer en node på hjemmedatamaskinen din.





- txindex=1`: Bygger og vedlikeholder en global indeks over bekreftede transaksjoner. Nødvendig for visse spørringer (`getrawtransaction`, ikke Wallet) og for utforskningsformål, men øker diskavtrykket betydelig. Inkompatibel med pruned-modus.





- `assumevalid=<hex>`: Angir en blokk som antas å være gyldig, slik at du kan hoppe over skriptsjekker for dens forfedre (sett `0` for å sjekke alt). Se forrige kapittel for mer informasjon.





- `reindex=1`: Rekonstruerer blokkindekser og tilstand (`chainstate`) fra `blk*.dat`-filer på disken. Gjenoppbygger også valgfrie aktive indekser. Dette er en tidkrevende operasjon for å reparere en ødelagt database eller for å aktivere/deaktivere tunge indekser på en ren måte.





- `reindex-chainstate=1`: Gjenoppbygger bare `chainstate` fra den gjeldende blokkindeksen. Foretrukket når blokkfilene er friske.





- `blockfilterindex=<type>`: Opprettholder indekser for kompakte blokkfiltre (f.eks. `basic`) som brukes av tynne klienter (BIP157/158) og noen RPC-er. Deaktivert som standard (`0`). Forbruker ekstra diskplass og indekseringstid.





- `coinstatsindex=1`: Opprettholder en UTXO-settstatistikkindeks som drives av `gettxoutsetinfo`-kallet. Nyttig for revisjoner og beregninger, og eliminerer behovet for kostbar omberegning. Deaktivert som standard.





- `loadblock=<fil>`: Importerer blokker ved oppstart fra en ekstern `blk*.dat`-fil. Brukes til å forhåndslaste historikk fra en frakoblet kilde (lokal kopi, eksternt medium) for å gjøre initialiseringen raskere.





- `par=<n>`: Angir antall skriptverifiseringstråder (fra `-10` til `15`, `0` = automatisk, `<0` = lar dette antallet kjerner være ledig). Gjør det mulig å justere CPU-parallellisme under validering. Automodus er egnet i de fleste tilfeller.





- `debuglogfile=<fil>`: Angir plasseringen til `debug.log`-loggen.





- `shrinkdebugfile=1`: Reduserer størrelsen på `debug.log` ved oppstart (standard: `1` når `debug` ikke er aktiv).





- `settings=<fil>`: Sti til den dynamiske innstillingsfilen `settings.json`.



### RPC tilgang og driftssikkerhet



Til slutt kan du i filen `Bitcoin.conf` også konfigurere tilgangsparametrene for noden din. Vær forsiktig med disse innstillingene, spesielt hvis du er nybegynner: Unngå å endre dem uten å ha en grundig forståelse av konsekvensene, da dette kan introdusere sårbarheter.





- `server=1`: Aktiverer JSON-RPC-serveren. Viktig hvis du kjører `bitcoind` via `bitcoin-cli` eller en tredjepartsapplikasjon. Deaktiver (`0`) på en ren valideringsnode som ikke eksponerer noe API, eller som allerede bruker en Electrum-server.





- `rpcbind=<addr>[:port]`: RPC-server lytter Address/port. Som standard lyttes det kun lokalt (`127.0.0.1` og `::1`). Denne parameteren ignoreres hvis `rpcallowip` ikke også er definert. Bruk den for å eksplisitt begrense Interface.





- `rpcport=<port>`: RPC-port (standard: `8332` på Mainnet, `18332` på Testnet, `38332` på bookmark, `18443` på regtest).





- `rpcallowip=<ip|cidr>`: Tillater RPC-klienter fra en gitt IP eller et subnett (kan gjentas). Brukes sammen med `rpcbind` for å eksponere API-et bare for et betrodd segment (LAN/VPN).





- `rpcauth=<USERNAME>:<SALT>$<Hash>`: Anbefalt RPC-autentiseringsmetode (hashet passord). Tillater flere oppføringer og unngår å lagre en hemmelighet i klartekst.





- `rpccookiefile=<sti>`: Sti til autentiseringsinformasjonskapsel (standard: `.cookie`-fil under `datadir/`). Denne brukes for lokal tilgang av samme bruker uten å administrere vedvarende passord. Du kan for eksempel bruke den til å koble Liana Wallet til Bitcoin core på samme maskin.





- `rpcuser=<user>` / `rpcpassword=<pw>`: Klassisk RPC-autentisering med passord i klartekst. Unngå å bruke dette til fordel for `rpcauth` eller en informasjonskapsel.





- `rpcthreads=<n>`: Antall tråder som skal betjene RPC-anrop (standard: `4`). Øk dette hvis du har høye anropstopper på overvåknings-/eksterne verktøy-siden.





- `rpcwhitelist=<USERNAME>:<rpc1>,<rpc2>,...`: Hviteliste over autoriserte API-er. Reduserer angrepsflaten ved å begrense tilgjengelige metoder.





- `rpcwhitelistdefault=1|0`: Standard whitelist-atferd: Hvis den er aktivert og en whitelist brukes, blir anrop som ikke er oppført, avvist. Dette kan også tvinge frem et tomt standardsett (ingen anrop tillatt) så lenge ingenting er eksplisitt oppført.





- `rest=1`: Aktiver offentlig REST API (deaktivert som standard). Skal kun eksponeres på et klarert nettverk (samme forsiktighet som med JSON-RPC).





- `conf=<fil>`: Angir, kun på kommandolinjen, en skrivebeskyttet konfigurasjonsfil. Nyttig for å fryse en kjøringsprofil (uforanderlig) på ops-siden.





- `includeconf=<fil>`: Laster inn en ekstra konfigurasjonsfil (sti relativ til `datadir/`). Tillater separasjon av roller: felles base + sensitiv lokal overbelastning.





- `daemon=1` / `daemonwait=1`: Starter `bitcoind` i bakgrunnen, og med `daemonwait` venter den på at initialiseringen er ferdig før den overleveres. Dette forenkler integrasjonen med supervisorer (systemd, runit).





- `pid=<fil>`: Plassering av PID-fil.





- `sandbox=<log-og-abort|abort>`: Aktiverer eksperimentell sandboxing av syscalls: bare forventede syscalls er tillatt.





- `startupnotify=<cmd>` / `shutdownnotify=<cmd>`: Utfører en kommando ved oppstart eller avslutning.





- `alertnotify=<cmd>`: Utløser en kommando ved mottak av et varsel.





- `blocknotify=<cmd>`: Utfører en kommando for hver nye blokk.





- `debug=<category>|1` / `debugexclude=<category>`: Aktiverer/deaktiverer detaljerte loggkategorier (f.eks. `net`, `Mempool`, `RPC`, `validering`...).





- `logips=1`: Logger IP-adresser.





- `logsourcelocations=1` / `logthreadnames=1` / `logtimestamps=1`: Legger til henholdsvis kildelokasjoner, trådnavn og nøyaktige tidsstempler i loggene.





- `printtoconsole=1`: Sender spor/feilrettinger til konsollen (*stdout*).





- `help-debug=1`: Viser hjelp til feilsøkingsalternativet og avslutter.





- `uacomment=<cmt>`: Legger til en kommentar til User-Agent P2P.



Vi er nå ferdige med å liste opp de fleste konfigurasjonsparametrene. Denne `Bitcoin.conf`-filen utgjør dermed det virkelige dashbordet for noden din: den definerer nettverkskonfigurasjon, Mempool-styring, disk- og minnebruk, indeksering og generell administrasjon. Hvis du vil lære mer om denne filen og lage en som er skreddersydd til dine behov, anbefaler jeg at du bruker [Jameson Lopps generator] (https://jlopp.github.io/Bitcoin-core-config-generator/).



Vi har nådd konklusjonen av dette BTC 202-kurset, som vil ha gjort deg i stand til ikke bare å forstå det grunnleggende om hvordan noder fungerer og hvordan de samhandler i systemet, men også til å sette opp din egen. Du er nå en suveren Bitcoiner, med din egen selvforvaltende Wallet, som sender transaksjonene dine via din egen node. Gratulerer så mye!



Du kan nå gå videre til den siste delen av kurset, der du kan evaluere BTC 202, og deretter ta vitnemålet ditt for å sjekke at du behersker alle konseptene som er dekket.



Du har nå flere alternativer åpne for deg. Det neste logiske steget er å sette opp din egen Lightning-node, slik at du kan være helt uavhengig for off-chain-transaksjonene dine. Dette vil være temaet for et kommende kurs, som vil bli publisert i høst 2025 på Plan ₿ Network.



I mellomtiden inviterer jeg deg til å ta BTC 204-opplæringen, som vil gjøre deg i stand til å forstå og mestre prinsippene for personvern i din bruk av Bitcoin:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


# Siste del


<partId>679169f5-b990-47e1-9a00-45098ba8096b</partId>





## Anmeldelser og rangeringer


<chapterId>c18f672d-1074-427e-9505-eecd7ae43e71</chapterId>




<isCourseReview>true</isCourseReview>


## Avsluttende eksamen


<chapterId>a4c97701-996c-4cc5-81fa-37d2dc4ee856</chapterId>




<isCourseExam>true</isCourseExam>


## Konklusjon


<chapterId>28c5cf1f-7b9c-4b68-8b8f-eee109629764</chapterId>




<isCourseConclusion>true</isCourseConclusion>