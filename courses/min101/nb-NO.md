---
name: Introduksjon til Bitcoin mining
goal: Forstå Bitcoin mining og proof-of-work fra bunnen av
objectives: 


  - Forstå proof-of-work og dens rolle i Bitcoin.
  - Analyser mekanismen for justering av vanskelighetsgrad.
  - Vet hva de tekniske begrepene knyttet til mining faktisk betyr.
  - Beskriv trinnene i byggingen av en Bitcoin-blokk og dens komponenter.
  - Identifisere viktige utviklingstrekk i mining-bransjen.


---

# Oppdag det grunnleggende om Bitcoin mining



Å forstå proof of work er å forstå hvordan Bitcoin fungerer. Uten denne oppfinnelsen og den geniale bruken av den kunne Bitcoin rett og slett ikke ha eksistert. Dette kurset gir deg all mining-teorien du trenger for bitcoin-reisen din.



MIN 101 er først og fremst rettet mot nybegynnere, ettersom det forklarer alle konseptene helt fra bunnen av. Men hvis du allerede har et middels kunnskapsnivå, vil dette kurset gi deg mulighet til å konsolidere forståelsen din, korrigere noen omtrentlige intuisjoner og utforske detaljer som ofte mangler i de vanlige forklaringene.



Ved slutten av dette kurset vil du være i stand til å forklare hvordan proof-of-work fungerer på en enkel og stringent måte. MIN 101 er også en ideell introduksjon til alle de andre mer avanserte kursene som omhandler Bitcoin mining på Plan ₿ Academy, enten de er teoretiske eller praktiske.



+++


# Innledning


<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>



## Kursoversikt


<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>



Velkommen til MIN 101-kurset, der du vil oppdage de grunnleggende teoretiske konseptene mining og Proof-of-Work innenfor Bitcoin-systemet. Dette kurset er det første steget i din bitcoiner-reise for å forstå hvordan mining fungerer. Når du har fullført det, kan du gå videre til mer avanserte teorikurs, eller du kan bli bitcoin-gruvearbeider selv!



I dette MIN 101-kurset vil vi ikke gå tilbake til de grunnleggende konseptene i Bitcoin, da vi vil gå rett til sakens kjerne: mining. Hvis du aldri har hørt om Bitcoin, eller hvis de grunnleggende prinsippene fortsatt er litt uklare for deg, anbefaler jeg på det sterkeste at du starter med vårt introduksjonskurs BTC 101. Når du har tilegnet deg disse grunnleggende kunnskapene, vil du kunne ta fatt på MIN 101 med selvtillit:



https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Del 1 - Innledning



Vi kommer til å starte dette kurset med et valgfritt første kapittel, der jeg gir en svært forenklet forklaring av mining, slik at du får et klart mentalt bilde før vi går inn på de tekniske mekanismene.



Målet her er ikke å gi deg alle de tekniske detaljene (de kommer senere i kurset), men å gi deg en rød tråd. Når dette rammeverket er på plass, vil hvert av de mer avanserte konseptene som introduseres senere, passe naturlig inn i denne strukturen.



### Del 2 - Hvordan proof of work fungerer



Etter introduksjonen er del 2 det tekniske grunnlaget for opplæringsprogrammet. Målet er å forklare, trinn for trinn, hvordan Bitcoin produserer gyldige blokker. Vi begynner med å se på strukturen til en blokk, før vi går inn på proof-of-work-mekanismen: rollen til målet, noncen og hashfunksjonen. Til slutt ser vi hvordan Bitcoin klarer å opprettholde en stabil blokkproduksjonsrate til tross for variasjoner i hashkraften, takket være mekanismen for justering av vanskelighetsgrad. På slutten av denne delen vil du ha en fullstendig forståelse av de grunnleggende prinsippene i Bitcoins proof-of-work.



### Del 3 - Insentivsystemet Bitcoin mining



I den tredje delen ser vi på hvorfor utvinnere oppfordres til å delta ærlig i mining. Vi beskriver prinsippet om blokkbelønning, dens sammensetning og beregningsmetode, dens utvikling over tid gjennom halveringer og den spesifikke rollen til coinbase-transaksjonen.



### Del 4 - Bitcoin mining-industrien



Den fjerde delen setter mining tilbake i sin operative virkelighet. Den sporer utviklingen av mining-maskiner, fra begynnelsen av Bitcoin til den moderne ASIC, for å forstå dagens maskinvarebegrensninger. Vi ser også på det grunnleggende ved mining-pooler, for å forstå hvordan utvinnerne klarer å redusere variansen i inntektene sine.



### Del 5 - Siste del



I den siste delen av kurset kan du teste kunnskapen din om mining ved å ta diplomet ditt.



Målet med dette MIN 101-kurset er derfor å gi deg en klar, strukturert og varig forståelse av Bitcoin mining, både teknisk og økonomisk.



Er du klar til å oppdage Bitcoin mining? La oss komme i gang!




## Bitcoin mining gjort enkelt


<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>



Før jeg går videre til en detaljert og mer teknisk forklaring av Bitcoin [mining](https://planb.academy/resources/glossary/mining), vil jeg gjerne gi deg en oversikt over prinsippet, som med vilje er enkelt og skjematisk. Hvis du allerede har noen grunnleggende kunnskaper, kan du gå rett til sakens kjerne i neste kapittel, etter at du har svart på quizspørsmålene. Dette kapittelet er først og fremst rettet mot nybegynnere, for å gi deg en myk start.



Se for deg Bitcoin som en stor offentlig notatbok som deles av alle, der vi skriver ned hvem som har sendt bitcoins til hvem. Denne notatboken kalles [blokkjeden](https://planb.academy/resources/glossary/blockchain). Den kan ikke oppbevares av bare én person, for da må den være til å stole på. I stedet fungerer Bitcoin kollektivt: Tusenvis av datamaskiner verifiserer og vedlikeholder den samme versjonen av denne notisboken.



![Image](assets/fr/049.webp)



Når du foretar en betaling i Bitcoin, oppretter du en [transaksjon](https://planb.academy/resources/glossary/transaction-tx). Denne transaksjonen blir ikke umiddelbart lagt til i notatboken. Den sendes først til nettverket, og venter deretter på å bli integrert i neste transaksjonspakke. Denne pakken kalles en [blokk](https://planb.academy/resources/glossary/block).



![Image](assets/fr/050.webp)



En blokk er ganske enkelt et sett med transaksjoner som er gruppert sammen. Når en blokk er klar, er det ikke nok å publisere den. Du må bevise for nettverket at blokken er verdig til å bli lagt til i bassenget. Det er her mining kommer inn i bildet.



Mining er arbeidet med å validere en blokk ved å forbruke energi. Aktører som kalles [utvinnere](https://planb.academy/resources/glossary/miner), bruker spesialiserte datamaskiner. Disse maskinene bruker strøm til å utføre et svært stort antall tester i en loop, helt til de finner et bevis som nettverket godtar. Når en utvinner finner dette beviset, anses blokken hans som gyldig.



Når blokken er validert, sendes den ut i nettverket. De andre [nodene](https://planb.academy/resources/glossary/node) sjekker raskt at den er i samsvar med reglene, og legger den deretter til i sekvensen av tidligere blokker. Det er derfor det kalles en "blokkjede": Hver nye blokk kommer etter de andre, i sekvensiell rekkefølge, og kjeden vokser litt etter litt.



![Image](assets/fr/051.webp)



For å oppsummere: Først opprettes transaksjoner. Deretter grupperes de sammen i en blokk. Deretter validerer en utvinner denne blokken ved å forbruke strøm. Til slutt legges denne blokken til i blokkjeden, og transaksjonene den inneholder, blir [bekreftet](https://planb.academy/resources/glossary/confirmation).



Hvis gruvearbeidere bruker strøm, er det ikke fordi de er frivillige. De gjør det fordi det er en belønning. Når en utvinner validerer en blokk, får han to typer inntekt. På den ene siden mottar han nyopprettede bitcoins. På den andre siden får han [gebyrene](https://planb.academy/resources/glossary/transaction-fees) som brukerne betaler for transaksjonene som inngår i blokken. Med andre ord kompenseres utvinneren både gjennom programmert pengeutstedelse og gjennom transaksjonsgebyrer som fastsettes av et marked.



På dette stadiet får du bevisst en veldig enkel visning av mining. Den forklarer ennå ikke hvordan blokken er konstruert i detalj, eller hvordan beviset utvinnerne leter etter fungerer, eller hvordan Bitcoin holder et jevnt tempo, eller hvordan belønningen beregnes nøyaktig, eller hvordan den kreves inn. Det er greit, det er alt vi kommer til å se i resten av dette MIN 101-kurset!



Målet med dette kapittelet var ganske enkelt å gi deg en klar mental struktur: transaksjoner → blokker → mining → blokkjede → belønning. Husk denne kjeden av ideer. I resten av kurset vil hvert kapittel legge til et lag med tekniske detaljer om ett av disse elementene, helt til du ikke bare forstår hva som foregår, men også hvordan og hvorfor det fungerer pålitelig, i stor skala, uten en sjef og uten behov for tillit.



# Hvordan proof of work fungerer


<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>



## Bitcoin-transaksjonsveien


<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>



For å forstå hva Bitcoin mining handler om, må vi først følge en typisk Bitcoin-transaksjon. Dette vil vise deg nøyaktig hvor blokken kommer inn i bildet, og hvorfor den er kjernen i systemet. Det er det jeg vil at du skal oppdage i dette første kapittelet.



I Bitcoin er en transaksjon en datastruktur som overfører eierskap av bitcoins fra en bruker til en annen. Konkret bruker den "[utganger](https://planb.academy/resources/glossary/output)" fra tidligere transaksjoner (såkalte [UTXO](https://planb.academy/resources/glossary/utxo)-transaksjoner), og refererer til dem som "[innganger](https://planb.academy/resources/glossary/input)", og oppretter deretter nye "utganger" som definerer hvem disse bitcoinsene nå tilhører, og under hvilke betingelser de kan brukes senere.



![Image](assets/fr/001.webp)



Et viktig poeng med Bitcoin er autorisasjonen til å bruke. Bitcoin er ikke på en konto, slik pengene dine i banken kan være, men er låst av utgiftsbetingelser. Når en [wallet](https://planb.academy/resources/glossary/wallet) ønsker å bruke en UTXO som input, må den fremlegge kryptografisk bevis på at den har rett til å låse den opp. Dette beviset tar ofte form av en [digital signatur](https://planb.academy/resources/glossary/digital-signature) generated fra en [privat nøkkel](https://planb.academy/resources/glossary/private-key). Det er derfor bitcoinere insisterer på å sikre de private nøklene dine: Det er disse som låser opp tilgangen til bitcoinsene dine, og dermed gjør det mulig for deg å bruke dem.



![Image](assets/fr/002.webp)



Den digitale signaturen i Bitcoin spiller to viktige roller:




- Autoriser utgifter: Dette beviser at brukeren har den private nøkkelen som forventes av UTXO-utgiftsbetingelsen;
- Integritetsbeskyttelse: knytter autorisasjonen til de nøyaktige detaljene i transaksjonen (mottakere, beløp, gebyrer osv.). Hvis noen endrer transaksjonen i ettertid, vil signaturen ikke lenger være gyldig.



Når transaksjonen er korrekt konstruert og signert av brukerens Bitcoin wallet, må den kringkastes i Bitcoin-nettverket.



### Bitcoin-nodens rolle i distribusjonen



Bitcoin er et [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p)-nettverk: Det finnes ingen sentral server som mottar og behandler alle transaksjoner. Denne rollen spilles kollektivt av nodene. En Bitcoin-node er et stykke programvare (f.eks. [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core)) som er koblet til andre noder i Bitcoin-nettverket, og som har som hovedoppgave å verifisere, lagre og videresende transaksjoner og blokker.



Når du sender en transaksjon fra en wallet, videresender wallet den til en node (din egen eller en tjenestes). Denne noden vil først kontrollere at transaksjonen overholder ulike regler, for eksempel:




- signaturer er gyldige;
- inndataene refererer til eksisterende UTXO-er (dvs. bitcoins som finnes);
- disse UTXO ikke allerede er brukt andre steder;
- mengden output er mindre enn eller lik mengden input (bitcoins skapes ikke fra ingenting);
- osv.



Hvis transaksjonen passerer alle disse kontrollene, sender noden den videre til de andre nodene i nettverket som den er koblet til. De sjekker den igjen og videresender den, og så videre. I løpet av noen sekunder er transaksjonen spredt og blir kjent for hele, eller i det minste en stor del av, Bitcoin-nettverket.



![Image](assets/fr/003.webp)



### Mempool: venterommet for transaksjoner



Mellom det øyeblikket en transaksjon sendes ut og det øyeblikket den bekreftes i en blokk, må den vente. Dette venteområdet kalles **[mempool](https://planb.academy/resources/glossary/mempool)** (sammentrekning av `memory` og `pool`). En mempool er derfor en midlertidig lagringsplass for gyldige, men ennå ubekreftede transaksjoner.



Et viktig poeng: Det finnes ikke én enkelt mempool, bare mempools. Hver node opprettholder sin egen mempool, med sine egne lokale begrensninger. Det betyr at to noder til enhver tid kan ha litt ulikt innhold i mempoolen (avhengig av hva de har mottatt, hva de har avvist eller hva de har slettet).



![Image](assets/fr/004.webp)



På dette stadiet vet nettverket om transaksjonen, har verifisert den og holder den i minnet til den blir bekreftet. Men bekreftelsen av transaksjonen kommer først når en utvinner legger den inn i en blokk, og denne blokken blir akseptert av nettverket.



### Blockchain: et offentlig tidsstemplingsregister



Ettersom bitcoin er en immateriell valuta, må den løse ett problem: å forhindre [dobbeltbruk](https://planb.academy/resources/glossary/double-spending-attack) uten en sentral myndighet. Hvis to transaksjoner forsøker å bruke den samme UTXO, må alle kunne konvergere mot en enkelt, sammenhengende tilstand. Satoshi Nakamoto oppsummerer dette problemet med denne berømte setningen:



> Den eneste måten å bekrefte fraværet av en transaksjon på, er å være klar over alle transaksjoner.

For å vite at en bitcoin ikke allerede har blitt brukt, trenger du med andre ord en felles oversikt over tidligere bruk.



Dette er blokkjedens rolle: et offentlig register som inneholder transaksjonshistorikken. Men i stedet for å skrive ned hver transaksjon etter hvert som den skjer, grupperer Bitcoin dem i blokker. Hver blokk fungerer som en historikkside, og systemet fungerer dermed som en tidsstempelserver: Det ordner transaksjoner over tid på en verifiserbar måte.



Dette registeret kan ikke skrives om, takket være et enkelt prinsipp: Hver blokk inneholder det kryptografiske fingeravtrykket ([hashen](https://planb.academy/resources/glossary/hash-function)) til den forrige blokken. Dermed er blokkene knyttet sammen: Hvis du endrer en blokk fra fortiden, endres dens hash, noe som bryter koblingen til neste blokk, som igjen bryter koblingen til blokken etter den, og så videre. Det er denne kjeden av avhengigheter som gir "*blockchain*" navnet sitt.



![Image](assets/fr/005.webp)



Når vi har forstått disse grunnleggende prinsippene i Bitcoin, kan vi beskrive en utvinners mål i mer konkrete termer: å bygge en ny blokk som utvider den eksisterende kjeden, ved å skrive inn ventende transaksjoner, og deretter forsøke å gjøre den gyldig (dette er den berømte "[proof of work](https://planb.academy/resources/glossary/proof-of-work)" som vi skal studere i et senere kapittel). Men først skal vi i neste kapittel sammen finne ut hvordan en kandidatblokk konstrueres.



## Bygge en Bitcoin-blokk


<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>



Du har nå forstått hvordan en Bitcoin-transaksjon fungerer, og hvilken rolle blokkjeden spiller. Før vi ser nærmere på hvordan proof-of-work fungerer, er det imidlertid fortsatt ett viktig trinn som utvinneren må utføre: konstruksjonen av en [kandidatblokk](https://planb.academy/resources/glossary/candidate-block). La oss sammen finne ut hva en kandidatblokk er, og hvordan utvinneren konstruerer den, før vi begir oss ut på leting etter et gyldig bevis.



### Kandidatblokken



Miners må bygge blokkene sine selv før de prøver å utvinne dem. Hver gruvearbeider konstruerer i sin tur en såkalt kandidatblokk ut fra transaksjonene som venter i hans mempool. Å bygge en kandidatblokk består derfor av følgende:




- velge hvilke transaksjoner som skal inkluderes;
- organisere disse transaksjonene på en måte som er kompatibel med Bitcoin-reglene;
- produserer blokkens metadata, som er lagret i [overskriften](https://planb.academy/resources/glossary/block-header).



Valget av transaksjoner følger en enkel økonomisk logikk: En blokk har en kapasitet som er begrenset av Bitcoin-protokollen, så utvinneren forsøker å maksimere det han tjener for denne plassen. Han prioriterer de transaksjonene som gir de høyeste avgiftene i forhold til plassen de opptar i blokken (dette kalles "avgiftsraten", uttrykt i sats/vB). Vi kommer tilbake til detaljene om gebyrer senere, men husk ideen om å sortere etter arealeffektivitet.



En Bitcoin-blokk består derfor av to hoveddeler:




- en liste over transaksjoner;
- et blokkhode, som på sett og vis fungerer som blokkens identitetskort.



![Image](assets/fr/006.webp)



Headeren er viktig, siden den brukes som grunnlag for proof-of-work: I Bitcoin utvinner du ikke en hel blokk direkte, men kun headeren til en blokk, som oppsummerer informasjonen som trengs for å koble blokken til kjeden og forplikte innholdet. For å gjøre det mulig for overskriften å representere alle transaksjoner, bruker Bitcoin et kryptografisk verktøy: [Merkle-treet](https://planb.academy/resources/glossary/merkle-tree).



### Merkle-treet: oppsummering av et stort sett med transaksjoner



Det ville være umulig å liste opp alle transaksjonene i headeren: En blokk kan inneholde tusenvis av transaksjoner, mens headeren har en fast størrelse (80 byte). Løsningen er derfor å beregne en unik hash som avhenger av alle transaksjonene i blokken: dette er [Merkle-roten](https://planb.academy/resources/glossary/merkle-root).



Prinsippet er som følger:




- beregnes det kryptografiske fingeravtrykket (hash) for hver transaksjon;
- disse hashene pares, sammenkjedes og hashes på nytt for å danne et nytt lag med hasher;
- denne prosessen gjentas helt til man får én endelig hash: Merkle-roten.



![Image](assets/fr/007.webp)



Så hvis en enkelttransaksjon endres, selv med bare én bit, blir resultatet en endring av fingeravtrykket, som forplanter seg til Merkle-roten. Denne roten er inkludert i blokkhodet. Så hvis man endrer en tidligere transaksjon, betyr det at man endrer blokkhodet som den inngår i, og dermed blokkens fotavtrykk, og deretter koblingen til påfølgende blokker.



Siden [SegWit](https://planb.academy/resources/glossary/segwit) har vi skilt signaturene fra resten. Så i virkeligheten er det to Merkle-trær i hver blokk. Denne separasjonen har konsekvenser for måten vi teller størrelsen på en blokk på og for visse kryptografiske forpliktelser, men grunntanken er den samme: Headeren må forplikte alt innholdet i blokken på en kompakt måte.



### Blokkhode



Blokkhodet er 80 byte langt og inneholder nøyaktig 6 felt. Det er disse seks elementene som blir hashet når man søker etter en proof of work (se neste kapittel):





- Versjonen (`version`): Dette angir hvilke regler eller oppdateringssignaler blokken følger. Den fungerer som en mekanisme for å opprettholde protokollkompatibilitet og evolusjon.




- Hash for forrige blokk (`previousblockhash`): Dette er hashen til den forrige blokkens header. Det er dette som knytter blokkene sammen. Uten dette feltet ville vi hatt uavhengige blokker. Ved å inkludere hashen til den forrige blokkens header får vi en kjede, der hver nye blokk bygger videre på den forrige.





- Merkle-rot (`merkleroot`): Dette er fingeravtrykket til alle transaksjonene i blokken (via Merkle-treet). Den knytter overskriften til innholdet: Hvis utvinneren endrer utvalget eller rekkefølgen på transaksjonene, endres roten.





- [Tidsstempel](https://planb.academy/resources/glossary/timestamp): Dette er et tidsstempel (Unix-tid) valgt av utvinneren (med gyldighetsbegrensninger), som må angi når blokken ble utvunnet. Det trenger ikke å være helt nøyaktig på sekundet, men det må oppfylle visse betingelser for å være akseptabelt for nettverket.





- Kodet vanskelighetsmål (`nbits`): Dette feltet koder det gjeldende [vanskelighetsmålet](https://planb.academy/resources/glossary/difficulty-target). Vi går nærmere inn på dette i kapittelet om vanskelighetsgrad, men husk at denne parameteren er en del av toppteksten.





- [Nonce](https://planb.academy/resources/glossary/nonce) (`nonce`): Dette er en verdi som gruvearbeideren fritt kan endre. Den fungerer som en justerbar variabel under proof-of-work. Jeg skal forklare dens rolle mer detaljert i neste kapittel, men det er viktig å forstå at nonce er en del av blokkhodet og er utformet for å tillate flere forsøk.



For å gjøre dette enklere å visualisere, ser du her et eksempel på et blokkhode i heksadesimalt format (80 byte):



```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```



Her er en oversikt over de ulike feltene:



```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```



Denne kandidatblokkoverskriften, konstruert av utvinneren, danner grunnlaget for arbeidet deres. Når man søker etter en gyldig proof-of-work, er det ikke hele listen over transaksjoner som hashes direkte i en løkke, men heller denne 80-byte-blokken, som inneholder alt som trengs for å koble blokken til fortiden og forplikte innholdet, samtidig som den også inkluderer parameterne som er nødvendige for mining-mekanismen, som vi skal se nærmere på i neste kapittel.



## Hash, mål og nonce


<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>



I de foregående kapitlene har du fulgt veien til en Bitcoin-transaksjon: opprettet og signert av en wallet, videresendt av noder, lagret i mempools, og deretter bekreftet når en utvinner inkluderer den i en blokk som er akseptert av nettverket. Men vi har ennå ikke sett hvordan en utvinner kan legge til blokken sin i blokkjeden. Hva er prosessen bak mining?



Det er ganske enkelt å forstå mining-prosessen. Den koker ned til tre konsepter som går hånd i hånd: en hash-funksjon, en målverdi og en variabel som gruvearbeideren kan modifisere. La oss ta en titt på hvordan det hele fungerer.



### Hash-funksjonen



En hashfunksjon er et verktøy som tar en melding som input og produserer en output av fast størrelse, kalt "*fingeravtrykk*" eller "*hash*".



![Image](assets/fr/010.webp)



Hash-funksjonen er interessant i datasystemer fordi den har visse egenskaper:





- Hvis du endrer en eneste bit av inndataene, endres den resulterende hashen fullstendig og uforutsigbart;



![Image](assets/fr/011.webp)





- Det er umulig å gå fra output til input: funksjonen er irreversibel;



![Image](assets/fr/012.webp)





- Det er umulig å finne to forskjellige meldinger som gir nøyaktig samme hash.



![Image](assets/fr/013.webp)



Hashfunksjonen som brukes i Bitcoin for mining er `SHA256`, brukt to ganger etter hverandre. Dette kalles dobbel [SHA256](https://planb.academy/resources/glossary/sha256), eller `SHA256d`. Det er denne doble hashingen som produserer blokkens fingeravtrykk.



```text
hash = SHA256(SHA256(message))
```



I vårt tilfelle tilsvarer `message` faktisk blokkhodet, som du så i forrige kapittel. Som en påminnelse er headeren en liten struktur som oppsummerer alt i blokken.



![Image](assets/fr/014.webp)



### Bevis på arbeid: finne en hash som er mindre enn målet



Proof-of-Work blir ofte beskrevet som en løsning på et komplekst problem. I virkeligheten er det ikke så mye et problem som et prøving og feiling-søk: utvinneren må finne en versjon av headeren som (etter å ha passert gjennom hashfunksjonen `SHA256d`) oppfyller en enkel betingelse: den må være mindre enn et bestemt mål.



Denne betingelsen er formulert på følgende måte:




- blokkoverskriftens hash beregnes ved hjelp av en hash-funksjon;
- tolker vi denne hashen som et tall;
- for at blokken skal være gyldig, må dette tallet være mindre enn eller lik en verdi som kalles "*vanskelighetsgradsmål*".



Med andre ord er en blokk gyldig hvis:



```text
SHA256d(block_header) <= target
```



![Image](assets/fr/015.webp)



Målet er et 256-biters tall. Ettersom hashen som produseres av `SHA256d` også er 256 bits, kan de sammenlignes som to tall. Jo lavere målet er, desto vanskeligere er betingelsen, ettersom det er færre mulige resultater under denne terskelen. Omvendt, jo høyere målet er, desto lettere er betingelsen å oppfylle, og desto lettere blir det å utvinne en blokk. Vi skal se nærmere på hvordan dette målet fastsettes i senere kapitler.



I dette systemet er hashfunksjonen interessant. Husk at det er enkelt å beregne utdata fra inndata, men umulig å finne en inndata ved kun å kjenne til funksjonens utdata. I mining blir ikke utvinnerne bedt om å finne en presis hash, men snarere å finne en hash under en målverdi. Den eneste måten å oppnå dette på er å gjøre et svært stort antall forsøk, helt til en bestemt header i kandidatblokken, når den hashes, gir en hash som er mindre enn dette målet.



Når målet er tilstrekkelig lavt, blir denne prosessen kostbar. Utvinneren beregner hashverdien av headeren til sin kandidatblokk, sjekker resultatet, og hvis betingelsen ikke er oppfylt, endrer han headeren og gjentar beregningen. Denne sløyfen gjentas til en gyldig header er funnet. Når hashen av headeren til slutt oppfyller betingelsen, er proof of work etablert, blokken anses som gyldig og kan kringkastes i Bitcoin-nettverket slik at nodene kan legge den til i blokkjeden sin. Vinneren mottar da den tilhørende belønningen (vi skal gå nærmere inn på sammensetningen senere), mens alle utvinnerne umiddelbart setter i gang med å lete etter en ny, gyldig header til neste blokk.



Den grunnleggende fordelen med denne mekanismen ligger i asymmetrien. Det er kostbart for utvinnere å produsere en proof of work, ettersom det krever et stort antall hash-beregninger. På den annen side er verifiseringen svært enkel for verifikatorene, det vil si nettverksnodene: Alt de trenger å gjøre, er å hashe blokkhodet som utvinneren har levert, og sjekke at den resulterende hashen faktisk er lavere enn målet. Å finne et bevis krever derfor mye arbeid og ressurser, mens det er raskt og billig å verifisere gyldigheten. Det er nettopp denne egenskapen som definerer et effektivt proof-of-work-system.



### Nonce



Et praktisk spørsmål gjenstår: Hvis kandidatblokkens header konstruert av utvinneren ikke gir en gyldig hash, hvordan kan utvinneren prøve igjen? Han må endre noe i headeren for å få en annen hash. Det er nettopp dette som er nonce-elementets rolle.



Husk den første egenskapen ved en hashfunksjon: Det er nok å endre en eneste bit i inndataene for å få en helt annen og uforutsigbar utdata-hash. Hver hashberegning er derfor som en tilfeldig trekning.



![Image](assets/fr/016.webp)



For å prøve lykken igjen trenger ikke utvinneren å endre hele headeren til kandidatblokken sin: Han trenger bare å endre en bitteliten del av den, for selv en eneste annen bit vil resultere i en helt ny hash, som potensielt er gyldig hvis den er mindre enn målet.



Det er nettopp derfor blokkhodet inneholder en nonce. Noncen er en 32-biters verdi som brukes én gang og deretter erstattes. I praksis kan en utvinner teste 4,29 milliarder mulige verdier (fra `0` til `2^32 - 1`) for den samme kandidatblokken. Hver variasjon av nonce-verdien endrer blokkhodet, og følgelig endres hashen som produseres etter bruk av hashfunksjonen `SHA256d` fullstendig.



mining-prosessen er veldig enkel:




- bygger gruvearbeideren en kandidatblokk (transaksjoner + header);
- beregner deretter hashen til `SHA256d(header)`;
- hvis resultatet er større enn målet, endres nonce;
- begynner igjen;
- osv.



![Image](assets/fr/017.webp)



Nonce er faktisk ikke det eneste feltet som kan endres. Enhver endring i transaksjonene i en blokk resulterer i en endring av roten i Merkle-treet, og dermed en endring av blokkens header. Med moderne datakraft kan det gå relativt raskt å gå gjennom de 4,29 milliarder mulige verdiene i nonce. Derfor finnes det et annet felt, vanligvis kalt "*[extra-nonce](https://planb.academy/resources/glossary/extra-nonce)*", som ytterligere mangedobler mulighetene for variasjon i headeren. Vi kommer nærmere tilbake til denne mekanismen i et senere kapittel.



### Hva er poenget med proof of work?



Vi kaller det "bevis" fordi resultatet er umiddelbart verifiserbart: Når en blokk er produsert, kan enhver node i løpet av en brøkdel av et sekund kontrollere at den kryptografiske hashen av headeren faktisk er under det nødvendige målet. Vi kaller det "arbeid" fordi det å oppnå denne hashen krever en rekke forsøk, og dermed en reell kostnad i form av beregning og energi.



I Bitcoin [White Paper](https://planb.academy/resources/glossary/white-paper) legger Satoshi Nakamoto frem to fordeler ved å bruke et proof-of-work-system i Bitcoin:





- Seal den økonomiske historien:**



Når beregningsbelastningen er brukt opp, er blokken låst: Hvis den skal endres, må blokkens proof of work beregnes på nytt. Og siden blokkene er kjedet sammen, vil en endring av en gammel blokk også bety at alle de påfølgende blokkene må beregnes på nytt, og deretter ta igjen og overgå det pågående arbeidet i den ærlige kjeden.



proof-of-work fungerer med andre ord som ryggraden i tidsstemplingssystemet, noe som gjør det stadig mer kostbart å forfalske fortiden etter hvert som blokkene akkumuleres. Når en ny blokk utvinnes, brukes sikkerheten som proof of work gir, samtidig og jevnt på alle eksisterende UTXO-er. For hver blokk som legges til, akkumulerer hver UTXO dermed en ekstra mengde sikkerhet fra Proof-of-Work.





- Definere flertallsstyre ([konsensus](https://planb.academy/resources/glossary/consensus)) og nøytralisere Sybil:**



Proof-of-Work gjør det også mulig for Bitcoin å oppnå konsensus uten å basere seg på avstemningsregelen "én ID = én stemme", som lett kan forfalskes ved massiv opprettelse av identiteter (IP-er, noder, nøkler...).



I Bitcoin er "*flertallet*" ikke det største antallet deltakere, men den **kjeden som akkumulerer mest arbeid**. Som Satoshi uttrykker det, er dette et "én CPU = én stemme"-prinsipp, dvs. en stemme vektet av den faktiske datakraften som brukes til å produsere gyldige blokker. Så utplassering av tusenvis av noder gir ingen fordel i seg selv i forhold til Bitcoin. Uten ekstra datakraft akkumuleres det ikke flere arbeidsbevis, og [Sybil-angrepet](https://planb.academy/resources/glossary/sybil-attack) blir ubrukelig, mens beslutningsregelen forblir objektiv og ikke krever noen identifisering av deltakerne.



![Image](assets/fr/018.webp)



[Nakamoto, S. (2008) *Bitcoin: A Peer-to-Peer Electronic Cash System*] (https://bitcoin.org/bitcoin.pdf)



Prinsippene knyttet til mindreåriges nytteverdi og fullmakter er et svært komplekst tema, som jeg ikke vil gå nærmere inn på i dette kurset. Vi vil imidlertid komme tilbake til dette temaet i fremtidige MIN 201-kurs.



For øyeblikket kan du oppsummere hvordan mining fungerer slik: utvinnere bygger en kandidatblokk med transaksjonene som venter i mempoolene, og ser deretter etter en hash av overskriften (via `SHA256d`) som er mindre enn eller lik et mål. De oppnår dette ved å teste nonces gjennom prøving og feiling.



I neste kapittel tar vi en kort historisk omvei inn i proof-of-work-prinsippet for å forstå bakgrunnen for det, og deretter ser vi på hvordan vanskelighetsmålet bestemmes av systemet.



## Historien om proof of work


<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>



Proof-of-work ble ikke oppfunnet for Bitcoin. [Satoshi Nakamoto](https://planb.academy/resources/glossary/nakamoto-satoshi) tok opp og samlet flere eldre ideer som allerede var utforsket i ulike sammenhenger.



### Hashcash



På slutten av 1990-tallet ble problemet med e-postspam et stort problem. Hvis det koster nesten ingenting å sende en e-post, kan en spammer sende millioner av meldinger. Men hvis hver melding krever en liten beregningsinnsats, er det enkelt for en vanlig bruker å sende én legitim melding, mens det blir svært dyrt å sende millioner av meldinger.



Dette er målet med [Hashcash](https://planb.academy/resources/glossary/hashcash), som ble foreslått av Adam Back i 1997, og som anses for å være oppfinnelsen av proof-of-work-prinsippet. Hashcash-prinsippet er svært likt mining: Produser en hash som overholder en betingelse (et visst antall nuller i begynnelsen av hashen). Beviset følger deretter med meldingen og kan verifiseres svært raskt av mottakeren. Hvis en e-post som ikke inneholder dette beviset, kan den umiddelbart betraktes som spam og dermed filtreres bort. Spammerne blir da tvunget til å bruke mye energi på å sende millioner av meldinger, noe som drastisk reduserer (eller til og med helt opphever) lønnsomheten i denne typen virksomhet, enten det dreier seg om markedsføring eller svindel.



I dag brukes ikke Hashcash til e-post. Spamfiltrering er nå i stor grad basert på sentraliserte systemer. Hashcash' fordel i forhold til dagens løsninger ligger i at den ikke krever sentralisert filtrering: hvem som helst kan justere parametrene etter egne kriterier. Den krever heller ikke identifikasjon, siden et hashsøk kan utføres anonymt. Fremfor alt er den ikke avhengig av et omdømmesystem, som har en tendens til å innføre subjektive former for filtrering.



Hashcash handlet ikke om å skape penger. Det handlet om å pålegge en marginalkostnad på en lett automatiserbar digital handling.



![Image](assets/fr/008.webp)



### Bit Gold



På slutten av 1990-tallet og begynnelsen av 2000-tallet utforsket Nick Szabo ideen om digital knapphet basert på proof of work. Hans konseptuelle prosjekt, kalt Bit Gold, går ut på å skape verdienheter ved å løse en kostbar proof of work, og deretter registrere disse bevisene i et register for å etablere en form for eierskap.



Bit Gold resulterte ikke i et utplassert system som Bitcoin, men det inneholder flere viktige innsikter: ideen om at beregning kan skape knapphet, og ideen om å tidsstemple elementer over tid for å skape en historie som er vanskelig å omskrive.



### RPOW



I 2004 foreslo Hal Finney RPOW (*Reusable Proofs of Work*). Tanken var å produsere arbeidsbevis som kunne utveksles, i stedet for bare å forbrukes. RPOW tok sikte på å skape digitale token basert på proof of work, med et system for å verifisere og overføre disse token uten å duplisere dem. RPOW løste ikke problemet med et fullstendig desentralisert register på en tilfredsstillende måte, slik Bitcoin senere skulle gjøre, men det er fortsatt en av de store forløperne til Bitcoin.



![Image](assets/fr/009.webp)



Hashcash, Bit Gold og RPOW bruker proof-of-work til å pålegge en kostnad og skape en form for knapphet. Bitcoin tar opp denne mekanismen, men gir den en sentral og kollektiv rolle: proof-of-work brukes ikke bare til å skape noe, den brukes også til å bestemme hvem som har rett til å skrive neste side i registeret (neste blokk), og til å gjøre dette registeret kostbart å forfalske.



## Justering av vanskelighetsmålet


<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>



I de foregående kapitlene så du kjernen i proof-of-work: utvinnere hasher overskriften til kandidatblokken med `SHA256d`, og blokken anses bare som gyldig hvis den resulterende hashen er numerisk mindre enn eller lik en referanseverdi som kalles target. Spørsmålet er hvor dette målet kommer fra, og hvordan sikrer systemet at det forblir konsistent over tid?



Bitcoin har som mål å finne en blokk hvert tiende minutt i gjennomsnitt. Dette tempoet er selvsagt ikke garantert på sekundet. I praksis blir noen blokker funnet noen sekunder etter den forrige, mens andre blir funnet etter mer enn en time. Det som betyr noe her, er gjennomsnittet over en tilstrekkelig lang periode.



![Image](assets/fr/019.webp)



Denne variasjonen skyldes minings probabilistiske natur: Hver hash er et uavhengig forsøk, med en konstant sannsynlighet (forutsatt at målet forblir uendret) for å produsere et resultat under målet. Det kan derfor sammenlignes med et lotteri med kontinuerlig trekning: Jo flere hashinger utvinnerne gjør per sekund, desto kortere blir den forventede forsinkelsen før det dukker opp en gyldig blokk, men uten at tilfeldighetene fra én trekning til den neste elimineres.



### Hvorfor skal man ha 10 minutter mellom blokkene?



Selv om det ikke finnes noen bevis for dette, valgte Satoshi Nakamoto sikkert 10 minutter som et praktisk kompromiss mellom effektivitet og sikkerhet. Et kortere intervall ville gi hyppigere bekreftelser, men ville føre til flere midlertidige splittelser i nettverket. For å forstå dette poenget må vi gå tilbake til hvordan en blokk forplanter seg.



Når en utvinner finner en gyldig blokk, distribuerer han den umiddelbart til sine kolleger. Nodene som mottar den, sjekker gyldigheten (transaksjoner, proof of work, konsensusregler osv.), og videresender den deretter i tur og orden. Denne spredningen tar en viss tid, begrenset av internettforsinkelse, båndbredde og hver enkelt nodes evne til å verifisere blokken.



![Image](assets/fr/020.webp)



Hvis en annen utvinner i løpet av denne diffusjonsforsinkelsen også oppdager en gyldig blokk i samme høyde, kan nettverket bli midlertidig splittet: En del av nodene og utvinnerne er avhengige av blokk A, mens den andre er avhengige av blokk B. Dette er en midlertidig oppdeling av nettverket.



![Image](assets/fr/021.webp)



Disse splittelsene er ikke katastrofale. Nakamoto-konsensus forutsier at på lang sikt vil bare én gren seire: den som akkumulerer mest arbeid. Så snart en ny blokk utvinnes på toppen av for eksempel blokk A, resynkroniserer hele nettverket seg på denne grenen og forlater blokk B, som da blir en "*[stale block](https://planb.academy/resources/glossary/stale-block)*", av og til feilaktig kalt en "*orphan block*" i dagligtalen.



![Image](assets/fr/022.webp)



På den annen side har de en kostnad: I noen få minutter arbeider en brøkdel av utvinnerne på en gren som vil bli forlatt. Dette arbeidet er da bortkastet med tanke på den generelle sikkerheten, ettersom det ikke har bidratt til den endelige kjeden. Jo kortere intervall det er mellom hver blokk, desto større er sannsynligheten for slike splittinger, siden formeringstiden utgjør en større andel av tiden mellom hver blokk.



Intervallet på 10 minutter gir vanligvis nok tid til at vinnerblokken rekker å spre seg bredt før en konkurrerende blokk i samme høyde blir funnet. Det er et kompromiss som begrenser splittinger, reduserer bortkastet datakraft og bidrar til at nettverket holder seg synkronisert på global skala.



### Forståelse av hashrate



*"[Hashrate](https://planb.academy/resources/glossary/hashrate)*" refererer til mengden hashberegninger som produseres per sekund, enten det er av en enkelt utvinner, en gruppe utvinnere eller alle utvinnerne i Bitcoin. Det uttrykkes i `H/s` (hashes per sekund), med multipler som `TH/s` (terahashes per sekund) eller `EH/s` (exahashes per sekund). Dette representerer antall forsøk utvinnere kan gjøre hvert sekund for å prøve å få en hash som er lavere enn målet.



Hvis målet forblir fast, da:




- hvert forsøk har en fast sannsynlighet for å lykkes;
- flere forsøk per sekund øker sannsynligheten for at et vinnende forsøk dukker opp raskt


Med andre ord: Hvis morgendagens Bitcoin-nettverk dobler datakraften ved å koble til dobbelt så mange mining-maskiner, vil blokkene i gjennomsnitt bli funnet dobbelt så raskt uten en korrigerende mekanisme. Målet må derfor justeres for å kompensere for hashrate-variasjoner.



### Justering av vanskelighetsmålet



Bitcoin løser dette problemet med en periodisk måljusteringsmekanisme, som justerer [vanskelighetsgraden](https://planb.academy/resources/glossary/difficulty-adjustment) i mining. Prinsippet er som følger: Hver 2016-blokk (omtrent hver andre uke) beregner hver node vanskelighetsmålet på nytt ved å observere hvor mye tid som faktisk gikk med til å produsere disse 2016-blokkene.



Målet med denne mekanismen er å redusere den gjennomsnittlige produksjonstiden for en blokk til rundt 10 minutter, samtidig som den samlede hashrate i nettverket er i konstant endring, fordi maskiner kobles fra eller, tvert imot, nye maskiner kommer til.



![Image](assets/fr/023.webp)



Beregningen er basert på den observerte tiden for den perioden som har gått:




- hvis de siste blokkene i 2016 ble funnet for raskt, betyr det at hashrate økte i denne perioden; Bitcoin gjør da tilstanden vanskeligere ved å senke målet for neste periode;
- hvis 2016-blokkene ble funnet for sakte, betyr dette at hashrate har blitt redusert; Bitcoin letter tilstanden ved å øke målet.



Formelen er som følger:



```txt
Tn = To * (Ta / Tt)
```



Med:




- `tn`: nytt mål
- `til`: gammelt mål
- `Ta`: forløpt sanntid for de siste 2016 blokkene
- `Tt`: måltid (i sekunder)



Med en måltid på to uker, dvs. `Tt = 1 209 600` sekunder:



```txt
Tn = To * (Ta / 1 209 600)
```



For å forstå hvordan du kan justere vanskelighetsgraden til Bitcoin mining, her er et eksempel med fiktive verdier:



```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```


Med:



- `**To = 18 045 755 102**`: Gammelt mål, dvs. referanseverdien før justering.
- `**ta = 1 000 000 sekunder**`: Tiden som faktisk ble brukt på å produsere de siste 2016 blokkene. Siden denne tiden er mindre enn måltiden, har nettverket utvunnet for raskt.
- `**1 209 600 sekunder**`: Måltid som tilsvarer 10 minutter per blokk for 2016-blokker, brukt som referanse for justering.
- `**tn = 14 918 779 020**`: Nytt mål beregnet etter justering av vanskelighetsgrad.



Her er det nye målet lavere enn det gamle, noe som betyr at mining blir vanskeligere for å bremse blokkproduksjonen i neste periode.


*Målverdiene i dette eksempelet er forenklet og skalert for undervisningsformål; det faktiske målet som brukes i Bitcoin, er et 256-biters heltall av en helt annen størrelsesorden*



Denne beregningen utføres lokalt av hver node, basert på tidsstemplene som er lagt inn i blokkene. Ettersom alle nodene bruker de samme reglene, kommer de frem til det samme resultatet, og det nye målet blir den felles referansen for de neste 2016-blokkene.



Det er en viktig detalj å merke seg når det gjelder denne justeringen: **den er begrenset**. Bitcoin begrenser variasjonen i vanskelighetsgrad per periode for å unngå for brå endringer som kan blokkere den. Faktisk er den faktiske tiden som tas i betraktning, begrenset til å holde seg innenfor et område som tilsvarer en faktor på 4 (minimum en fjerdedel av det gamle målet, maksimum fire ganger det gamle målet). Dette forhindrer ekstrem retargeting hvis tidsstemplene er svært atypiske eller manipulerte.



Legg også merke til at Bitcoins vanskelighetsjustering i virkeligheten ikke er helt nøyaktig. Vi har sett at den er programmert til å beregne vanskelighetsgraden på nytt hver 2016. blokk, ved å sammenligne den faktiske tiden som har gått med måltiden på 14 dager (2016 × 10 minutter). Men Satoshis originale kode inneholder en såkalt "*off-by-one*"-feil: i stedet for å måle tiden mellom de siste blokkene i hver periode (altså 2016 intervaller), måler den tiden mellom den første og den siste blokken, som bare er 2015 intervaller. Konkret beregnes vanskelighetsgraden som om perioden bare besto av 2015 blokker i stedet for 2016. Konsekvensen er at vanskelighetsgraden systematisk er litt overvurdert, noe som gjør at blokker i gjennomsnitt utvinnes litt saktere enn målet på 10 minutter (omtrent 0,05 % saktere). Denne feilen er godt kjent, men har aldri blitt rettet, da en endring ville kreve en hard fork og dens innvirkning forblir ubetydelig i praksis, bortsett fra det teoretiske angrepet kalt "*time warp*".

### Målrepresentasjon



I blokkhodet vises ikke målet i sin fulle 256-biters form, da dette ville tatt for mye plass. I stedet koder 32-biters `nBits`-feltet målet i et kompakt format, som kan sammenlignes med vitenskapelig notasjon i base 256: en eksponent (1 byte) og en koeffisient (3 byte). Det komplette målet rekonstrueres deretter ut fra disse to verdiene. Vi skal ikke gå i detalj her, da emnet er relativt komplekst og ikke tilfører noe til forståelsen av mining. Husk bare at målet ikke lagres i rå form i blokkhodet, men i kompakt form.



Med dette siste kapittelet i del I har vi tatt en omvisning i hvordan proof-of-work fungerer i Bitcoin: Gruvearbeideren bygger en kandidatblokk ved å velge transaksjoner fra sin mempool, beregner kandidatblokkens overskrift, hasher den, sammenligner den resulterende hashen med periodemålet, og starter deretter på nytt ved å endre nonce til en gyldig hash er oppnådd. Til slutt beregner nettverket et nytt mål for hver 2016. blokk for å opprettholde en gjennomsnittlig tid på rundt 10 minutter per blokk, til tross for de konstante variasjonene i hashrate.




# Insentivsystemet Bitcoin mining


<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>



## Block reward


<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>



Som du kan forestille deg, er ikke Bitcoin mining en altruistisk aktivitet. Miner har reelle kostnader: strøm til å drive mining-datamaskinene sine, innkjøp av spesialutstyr, lønn til vedlikehold, og noen ganger lokaler og kjølesystemer. For at Bitcoin-systemet skal fungere, må de private interessene til utvinnerne være på linje med nettverkets kollektive interesser. Det er nettopp dette som er mining-belønningen. Den oppmuntrer utvinnere til å investere i proof of work, til å inkludere gyldige transaksjoner og til å respektere protokollens regler i stedet for å prøve å ødelegge den.



Denne logikken er basert på spillteori: Protokollen gjør ærlighet rasjonelt. En gruvearbeider tjener penger når han produserer en gyldig blokk som aksepteres av nodene. Hvis han derimot prøver å jukse, vil blokken hans bli avvist av nodene, og han vil ikke få noe. Siden det koster penger å produsere en blokk, representerer en avvist blokk et direkte tap. I et konkurransepreget miljø der tusenvis av spillere samtidig søker etter en gyldig blokk, er den mest lønnsomme strategien derfor som oftest å følge reglene strengt og maksimere inntekten på ærlig vis.



For å oppnå dette fastsetter Bitcoin-protokollen at utvinneren som finner en gyldig blokk, vinner retten til å inkludere en bestemt transaksjon i den, noe som gir utvinneren en viss sum BTC. Dette er kjent som **[blokkbelønning](https://planb.academy/resources/glossary/block-reward)**. I dette første kapittelet av denne delen er målet å forstå hva den består av og hvordan den bestemmes. Senere skal vi se hvordan pengeskapingsdelen utvikler seg over tid (med halveringer) og hvordan den faktisk samles inn teknisk (via coinbase-transaksjonen).



### Hva består blokkbelønningen av?



I de foregående kapitlene har vi sett hvordan utvinnere klarer å finne en gyldig blokk. Når en utvinner har funnet en header som har en hashverdi som er mindre enn målet, anses kandidatblokken hans som gyldig. Han kan deretter distribuere den til hele Bitcoin-nettverket. Blokken legges til resten av blokkjeden, og bekrefter transaksjonene den inneholder.



Det er nettopp denne hendelsen (selve tilføyelsen av blokken til blokkjeden) som utløser en belønning til den vinnende gruvearbeideren. Denne belønningen består av to forskjellige elementer som legges sammen:




- [blokktilskudd](https://planb.academy/resources/glossary/block-subsidy)**;
- transaksjonsgebyrer**.



![Image](assets/fr/024.webp)



La oss ta en titt på hva disse to delene av belønningen tilsvarer.



### Blokktilskudd



Blokktilskuddet tilsvarer den monetære skapelsesdelen av belønningen. Når en utvinner produserer en gyldig blokk, gir protokollen ham tillatelse til å skape et visst antall nye bitcoins og tildele dem til seg selv som belønning. Disse bitcoinsene skapes ex nihilo. De eksisterte ikke før.



Mengden nyopprettede bitcoins er imidlertid på ingen måte vilkårlig. Den er strengt definert av Bitcoin-protokollens regler og er identisk for alle utvinnere. Vi skal se nærmere på denne mekanismen i neste kapittel, ettersom tilskuddet ikke er en fast verdi på ubestemt tid: Det deles opp med jevne mellomrom i henhold til en nøyaktig tidsplan. Inntil videre er det bare å huske det:




- blokktilskuddet er en av de to komponentene i blokkbelønningen;
- er begrenset og bestemmes av protokollen, ikke av gruvearbeideren (selv om gruvearbeideren teknisk sett kan be om mindre enn maksimumsbeløpet);
- skaper den bitcoins ut av løse luften.



Denne subsidien spiller to hovedroller i Bitcoin-protokollen. Den første er å oppmuntre spillere til å delta i mining. I de første årene av Bitcoin (og noen ganger fortsatt i dag) var transaksjonsgebyrene svært lave. Tilskuddet har derfor garantert tilstrekkelig kompensasjon for å tiltrekke seg utvinnere og opprettholde et sikkerhetsnivå for systemet.



Den andre rollen er knyttet til valutadistribusjon. Enhver ny valuta står overfor spørsmålet om hvordan pengeenhetene skal fordeles rettferdig til befolkningen. Blokksubsidiet gir et svar på dette problemet. Ved å skape bitcoins via mining muliggjør det den første distribusjonen på en åpen og nøytral måte: hvem som helst kan få tak i dem, forutsatt at de deltar i mining, uten at det kreves forhåndsgodkjenning eller identifikasjon.



På den annen side, siden disse bitcoinsene er skapt ut av ingenting, er verdien deres ikke uten grunnlag. Ved å øke pengemengden i omløp, utvanner subsidien mekanisk verdien av eksisterende bitcoins. Det introduserer derfor en form for monetær inflasjon. Vi skal imidlertid se i neste kapittel at denne subsidien gradvis vil forsvinne, og at inflasjonen etter hvert vil opphøre.



![Image](assets/fr/025.webp)



### Transaksjonsgebyrer



Den andre komponenten i blokkbelønningen er knyttet til systembruk: Når en bruker legger ut en transaksjon, ønsker han at den skal bekreftes. Blokkplassen er imidlertid begrenset, og blokker vises i gjennomsnitt bare hvert tiende minutt eller så. Blokkplass er derfor en knapp ressurs. Når etterspørselen overstiger tilbudet, stiger prisen: Dette er markedet for transaksjonsgebyrer. Hver utvinner som klarer å produsere en gyldig blokk, får rett til å kreve inn, for egen regning, de fulle transaksjonsgebyrene knyttet til alle transaksjonene han har inkludert i blokken.



Du kan se på det som et auksjonssystem: Hver transaksjon foreslår et avgiftsbeløp, og utvinnerne prioriterer de transaksjonene som maksimerer inntektene deres, under plassbegrensninger. Denne mekanismen utjevner interessene på en naturlig måte:




- brukere som har det travelt, betaler mer for å bli inkludert raskt;
- utvinnere oppfordres til å inkludere transaksjoner som betaler de høyeste avgiftene for blokkplass.
- nettverket unngår spam, fordi det koster å publisere en transaksjon.



#### Hvordan beregnes transaksjonsgebyrene?



I motsetning til hva mange tror, er ikke gebyrer en output i en Bitcoin-transaksjon. Faktisk bruker en transaksjon input og skaper output. Inputs representerer kilden til bitcoins som brukes, mens outputs representerer destinasjonen for betalinger. Transaksjonsgebyrer er ganske enkelt **differansen mellom totale inndata og totale utdata**.



Med andre ord skaper brukerens bitcoin-input, som tilhører dem, output for mottakerne, men reproduserer ikke hele beløpet som forbrukes av inputen. Differansen mellom de to representerer transaksjonsgebyrene som utvinneren kan kreve inn.



La oss ta et eksempel. En transaksjon bruker to inndata, en på 100 000 sats` og en på 150 000 sats`, og skaper tre utdata på 35 000 sats`, 42 000 sats` og 170 000 sats`.



![Image](assets/fr/027.webp)



Summen av input er derfor 250 000 sats`, mens summen av output er 247 000 sats`. Dette betyr at 3 000 sats` har blitt forbrukt i input uten å bli gjenskapt i output: dette beløpet tilsvarer avgiftene som foreslås i denne transaksjonen.



![Image](assets/fr/028.webp)



Hvis en utvinner inkluderer denne transaksjonen i en gyldig blokk, vil han ha rett til å få tilbakebetalt disse "3 000 sats", i tillegg til avgiftene for alle andre transaksjoner som er inkludert i blokken. Det er imidlertid ingen direkte on-chain-kobling mellom transaksjonen som betaler gebyret og de sats som utvinneren faktisk krever inn. Teknisk sett blir de 3 000 sats` i gebyrer ødelagt, og til gjengjeld får utvinneren rett til å gjenskape det samme beløpet for seg selv.



#### Avgiftsforholdet



En blokk er ikke begrenset av antall transaksjoner, men av dens totale kapasitet (i dag i praksis av blokkens vekt). Noen transaksjoner tar mer plass enn andre: En transaksjon med mange innganger og utganger vil være større enn en enkel transaksjon med én inngang og to utganger. Skriptene som brukes, vil også påvirke størrelsen.



![Image](assets/fr/026.webp)



To transaksjoner kan derfor betale like mye i absolutte termer, men ikke være økonomisk likeverdige sett fra utvinnerens ståsted. Hvis den ene er dobbelt så stor, koster den dobbelt så mye plass i blokken. Det er knapphet på plass, så utvinneren forsøker å maksimere inntekten per enhet plass.



Derfor uttrykker vi i praksis konkurransedyktigheten til en transaksjon med et gebyrforhold, vanligvis i `sats/vB` ([satoshis](https://planb.academy/resources/glossary/satoshi-sat) per virtuell byte). Det er enkelt å beregne dette forholdet:



```text
fee rate = fee / weight (in vB)
```



Hvis vi for eksempel har en transaksjon som veier 141 vB og tildeler 1 974 sats i gebyrer, vil den ha en gebyrsats på 14 sats/vB.



```text
1 974 / 141 ≈ 14 sats/vB
```



Dette forholdet forklarer de økonomiske valgene utvinnerne tar: Ved fast kapasitet maksimerer inkludering av transaksjoner med høy pris blokkens totale avgifter, og dermed utvinnerens kompensasjon. Det forklarer også hvorfor lavpristransaksjoner blir stående i kø i mempools i lange perioder: De konkurrerer med andre transaksjoner som betaler mer per enhet plass.



### Nettverksbeskyttelse mot spam



Avgifter tjener også et operasjonelt sikkerhetsformål: De innfører en kostnad for multiplikasjon av transaksjoner. Hvis det var gratis å publisere en transaksjon, ville det være lett å oversvømme nettverket med unyttige transaksjoner og mette mempools, noe som ville øke belastningen på nodene.



I praksis bruker noder lokale videresendingsregler (mempool-regler) og setter ofte en minimumsgrense for når de ikke vil videresende en transaksjon (som standard `0,1 sat/vB` i Bitcoin Core via `minRelayTxFee`). En transaksjon kan være gyldig i henhold til konsensusreglene, men ikke videresendes av de fleste noder hvis avgiftene er for lave. Resultatet er at den ikke sirkulerer, ikke når utvinnerne og har svært liten sjanse for å bli bekreftet.



På dette punktet har du fått kjernen i blokkbelønningen: den tilsvarer kompensasjonen for den vinnende gruvearbeideren og består av to forskjellige elementer. På den ene siden et blokktilskudd, definert av protokollreglene, som skaper nye bitcoins ex nihilo. Og på den andre siden avgiftene for transaksjoner som er inkludert i den utvunnede blokken.



I neste kapittel skal vi se nærmere på blokktilskuddet, for å forstå nøyaktig hvordan det beregnes og hvordan det utvikler seg over tid i henhold til reglene i Bitcoin-protokollen.



## Halving


<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>



I forrige kapittel så vi at utvinnere som produserer en gyldig blokk, får en belønning som består av avgiftene for transaksjonene som inngår i blokken, pluss et blokktilskudd. Vi har imidlertid ennå ikke forklart hvordan størrelsen på dette tilskuddet bestemmes. Mekanismen som fastsetter og utvikler denne verdien, kalles ***[halving](https://planb.academy/resources/glossary/halving)***.



### Hva er halvering?



Halving er en hendelse som er programmert inn i Bitcoin-protokollen, og som halverer blokksubsidien, dvs. det maksimale antallet nye bitcoins som den vinnende utvinneren får lov til å skape for hver blokk. Det påvirker ikke transaksjonsgebyrene: Gebyrene eksisterer uavhengig og bestemmes fortsatt av brukeraktivitet og konkurranse om blokkplass.



Da Bitcoin ble lansert i 2009, ble blokksubsidien satt til 50 BTC for hver utvunnet blokk. Siden den gang har denne subsidien blitt halvert flere ganger for hver halvering.



![Image](assets/fr/029.webp)



Halving utløses ikke av en dato, men av blokkhøyde. Den utføres **hver 210 000 blokk**. Siden Bitcoin sikter mot et gjennomsnittlig intervall på rundt 10 minutter per blokk, tilsvarer 210 000 blokker omtrent fire år.



```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```



Hvis vi noterer `n` som antall halveringer som allerede har funnet sted, kan blokktilskuddet i BTC beregnes på følgende måte:



```text
subsidy(n) = 50 / 2^n
```



### Tidligere halveringer



Her er en oversiktstabell over halveringer som allerede har funnet sted, med blokkhøyde, dato og det nye blokktilskuddet som gjelder etter hendelsen:



| Event               |   Height  | Date                        | Subsidy    |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 july 2016                 |   12,5 BTC |
| Halving 3           |   630 000 | 11 may 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 april 2024               |  3,125 BTC |
| Halving 5 (upcoming) | 1 050 000 | Spring   2028 (estimation) | 1,5625 BTC |

### Når og hvordan opphører tilskuddet?



Halving gjentas så lenge tilskuddet kan uttrykkes i systemets minsteenhet: satoshi.



```text
1 BTC = 100 000 000 sats
```



Etter hvert som subsidien halveres, når vi til slutt brøkdeler av en bitcoin som er så små at de blir mindre enn 1 satoshi. På dette punktet er det ikke lenger mulig å skape en halv satoshi-enhet. Pengeskapingen gjennom blokksubsidieringen opphører, og utvinnerne kompenseres utelukkende på grunnlag av transaksjonsgebyrer. Fra dette tidspunktet vil alle bitcoins være i omløp, og det vil ikke lenger være mulig å produsere nye enheter.



Den endelige slutten på blokksubsidiene vil komme på blokknivå 6 930 000, dvs. ved den 33. og siste halveringen. Denne hendelsen forventes å finne sted rundt år 2140, selv om det er umulig å gi en eksakt dato, ettersom det vil avhenge av hvor raskt det faktisk blir funnet blokker frem til da.



Siden blokksubsidien følger en geometrisk sekvens med et forhold på 1/2 ved hver halvering, var pengeskapingen ekstremt høy i Bitcoins tidlige dager, og avtar deretter veldig raskt. Ved den syvende halveringen vil over 99 % av bitcoins allerede ha blitt satt i omløp. Terskelen på 99 % forventes å bli passert mellom 2032 og 2036. Det betyr at det da vil ta over 100 år å utvinne den siste gjenværende 1 % av bitcoinsene. Mens den monetære inflasjonen var svært høy da Bitcoin ble lansert, for å muliggjøre utbredt distribusjon av valutaen, er den nå svært lav og vil fortsette å falle, helt til den når nivået til en ekte hard valuta, der det sirkulerende tilbudet ikke lenger kan øke.



![Image](assets/fr/030.webp)



### Hvorfor vil det aldri bli 21 millioner BTC?



Bitcoins maksimale pengemengde presenteres ofte som 21 millioner BTC. Dette er en god tilnærming for å forstå pengepolitikken, men fra et rent teknisk synspunkt vil den totale tilførselen aldri nå nøyaktig 21 000 000 bitcoins.



Hovedårsaken er mekanisk. Gjennom suksessive halveringer faller blokksubsidiet til slutt under minimumsverdien på 1 sat, noe som avslutter utstedelsen før den eksakte teoretiske totalen nås. Som et resultat av denne minste granulariteten og avrundingsreglene, er det totale antallet bitcoins som er opprettet av tilskuddet, litt mindre enn 21 millioner.



I tillegg kan marginale protokollrelaterte avvik også bidra til dette. I sjeldne tilfeller kan det for eksempel hende at noen utvinnere ikke har gjort krav på hele tilskuddet sitt, noe som definitivt reduserer mengden bitcoins som faktisk er utstedt. Vi kan også nevne [genesis-blokken](https://planb.academy/resources/glossary/genesis-block), produsert av Satoshi den 3. januar 2009, hvis bitcoins som ble opprettet ikke er en del av [UTXO set](https://planb.academy/resources/glossary/utxo-set), samt visse historiske hendelser knyttet til feil, for eksempel dupliserte coinbase-transaksjonsidentifikatorer.



Til slutt må vi også ta hensyn til alle bitcoins som har blitt ødelagt eller blokkert:




- bitcoins låst i uløselige skript;
- de som bevisst ble ødelagt av `OP_RETURN`-skript;
- eller tap av private nøkler på applikasjonsnivå.



I teorien er derfor Bitcoin-tilgangen begrenset til 21 millioner. I praksis vil det imidlertid aldri være 21 millioner bitcoins i omløp.



## Coinbase-transaksjonen


<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>



I de foregående kapitlene har vi presentert to viktige punkter. For det første får utvinneren som lykkes med å produsere og distribuere en gyldig blokk, en belønning. For det andre så vi at denne belønningen består av to forskjellige elementer:




- en blokksubsidie (bitcoins opprettet ex nihilo, hvis maksimale beløp er fastsatt av protokollen og gradvis reduseres via halveringer);
- alle transaksjonsgebyrer som er betalt av brukere hvis transaksjoner er inkludert i blokken.



Et spørsmål gjenstår imidlertid: Ved hjelp av hvilken mekanisme samler gruvearbeideren inn denne belønningen i Bitcoin? Dette er nettopp rollen til en bestemt transaksjon som kalles en "coinbase".



### Slik fungerer Coinbase-transaksjonen



Som vi så i første del av kurset, inneholder hver Bitcoin-blokk en liste over ventende transaksjoner som den vil bekrefte. Den aller første av disse er alltid [coinbase-transaksjonen](https://planb.academy/resources/glossary/coinbase-transaction). Det er den som gjør det mulig for den vinnende gruvearbeideren å motta belønningen sin.



![Image](assets/fr/031.webp)



Ved første øyekast ser den ut som en klassisk Bitcoin-transaksjon: Den har en [TXID](https://planb.academy/resources/glossary/txid-transaction-identifier), utganger og er inkludert i blokkens Merkle-tre. Den skiller seg imidlertid ut på ett viktig punkt: Den bruker ikke noen eksisterende UTXO.



I en klassisk Bitcoin-transaksjon refererer "input" til tidligere ubrukte outputs (UTXO), som gir inputverdien. Utgangene omfordeler deretter denne verdien til nye UTXO-er, med nye utgiftsbetingelser. Med andre ord, for å sende bitcoins må du allerede eie dem. Coinbase-transaksjonen bruker derimot ingen bitcoins i input: den skaper bitcoins i output direkte fra bunnen av.



Det er nettopp denne mekanismen som gjør det mulig å introdusere nye bitcoins i sirkulasjon via blokksubsidiet, og krediterer utvinneren med avgiftene knyttet til transaksjonene som inngår i blokken. Coinbase-transaksjonen kan ikke referere til en reell eksisterende UTXO (faktisk refererer den til en fiktiv UTXO), siden dens rolle nettopp er å skape en del av verdien (subsidiet) og gjenopprette den andre delen (gebyrene), uten å motta dem fra en tidligere transaksjon. For at hele systemet skal være konsistent, må den delen som tilsvarer avgiftene være nøyaktig lik summen av bitcoins som er forbrukt i input, men ikke gjenskapt i output i de andre transaksjonene i blokken.



![Image](assets/fr/032.webp)



Denne transaksjonen er ikke valgfri. En blokk som ikke inneholder en coinbase-transaksjon, er ugyldig og vil systematisk bli avvist av nettverksnoder.



⚠️ Vær oppmerksom på at begrepet "*coinbase*" ikke har noen forbindelse med utvekslingsplattformen med samme navn. I Bitcoin refererer "*coinbase*" historisk sett til transaksjonen som skaper blokkbelønningen. Selskapet har ganske enkelt tatt i bruk dette begrepet som navn.



Coinbase-transaksjonen fyller faktisk flere roller samtidig:




- Den første er den vi nettopp har beskrevet: Den tildeler utvinneren belønningen han eller hun har rett til for å ha produsert en gyldig blokk.
- Den andre, mer tekniske rollen er å forankre den kryptografiske forpliktelsen til vitnene (signaturene) til SegWit-transaksjonene som inngår i blokken.
- En tredje rolle, denne gangen ikke direkte protokollrelatert, men knyttet til den moderne industrialiseringen av mining, er at myntbasen nå ofte brukes til å forankre vilkårlige tekniske data. Disse dataene er generelt knyttet til driften av mining-bassenger og deres interne organisasjon.



For å hjelpe deg med å forstå disse ulike bruksområdene, skal vi nå se nærmere på strukturen til coinbase-transaksjonen.



### Den grunnleggende strukturen i Coinbase-transaksjonen



En coinbase-transaksjon må inneholde nøyaktig én input. For enkelhets skyld sier vi noen ganger at den ikke har noen inngang, fordi denne inngangen ikke bruker noen ekte UTXO. I virkeligheten finnes det en inngang med en referert kilde, men den peker bevisst på en ikke-eksisterende UTXO.



Som vi allerede har sett, må alle Bitcoin-transaksjoner bruke UTXO-er som input for å kunne skape gyldige outputs. I Bitcoin-transaksjonen tar dette forbruket form av å referere til en eksisterende UTXO som input. Denne referansen gjøres ganske enkelt ved å angi identifikatoren til den forrige transaksjonen (den som UTXO ble opprettet i), samt dens indeks blant utdataene i denne transaksjonen. Konkret defineres en UTXO av en hash (den forrige TXID-en) og en indeks.



Men når det gjelder coinbase-transaksjonen, i stedet for å referere til en ekte eksisterende UTXO, må inngangen nødvendigvis peke på denne spesielle falske UTXO, med en TXID full av nuller, som ikke samsvarer med noen ekte TXID:



```text
0000000000000000000000000000000000000000000000000000000000000000
```


Direkte etterfulgt av den falske indeksen:


```text
0xffffffff
```


![Image](assets/fr/033.webp)



I den grunnleggende Bitcoin-protokollen, som beskrevet i Satoshi Nakamoto, er denne falske inndataen den eneste begrensningen som pålegges coinbase-transaksjonen.



I likhet med alle UTXO som er referert til i en transaksjons input, er den tilknyttet et `scriptSig`-felt. I en konvensjonell transaksjon inneholder dette `scriptSig`-feltet elementene som trengs for å tilfredsstille `scriptPubKey` og dermed låse opp den brukte UTXO. Men i det spesielle tilfellet med coinbase, siden UTXO referert til bevisst er fiktiv, er `scriptSig`-feltet helt fritt. Miner-er kan derfor legge inn hvilke data de vil. Vi skal senere se på hvordan denne friheten brukes.


I tillegg til denne falske inngangen finnes det én eller flere helt standard utganger, som gjør det mulig for utvinneren å hente bitcoins fra belønningen på en av Bitcoin-adressene sine. Disse utgangene er UTXO-adresser som er låst av en `scriptPubKey` (f.eks. et skript som peker til en adresse kontrollert av gruvearbeideren eller bassenget). Det eneste særegne her ligger i regelen for beregning av verdien: Den totale summen av myntbasens utganger må aldri overstige det maksimalt tillatte tilskuddet, som blokkavgiftene legges til.



Historisk sett er coinbase-transaksjonen kokt ned til dette enkle skjemaet: en falsk inngang som refererer til en ikke-eksisterende UTXO, og en eller flere utganger designet for å distribuere blokkbelønningen til den vinnende gruvearbeideren. I dag er imidlertid coinbase ikke lenger begrenset til denne distribusjonsrollen. Dens spesielle posisjon i blokken og den store fleksibiliteten i strukturen har ført til nye bruksområder, både i selve protokollen og i mining-pooladministrasjonsmekanismer.



### Andre bruksområder for Coinbase



Over tid har coinbase-transaksjonen blitt et spesielt praktisk innsettingspunkt for å integrere en rekke informasjon som er nyttig for mining og for selve blokkstrukturen. La oss ta en titt på dem for å bedre forstå den generelle coinbase-organisasjonen.



#### BIP-34



[BIP-34](https://planb.academy/resources/glossary/bip0034) er en fork soft som ble distribuert i mars 2013, og startet med blokk 227,930, som introduserte versjon 2 av Bitcoin-blokker. Denne nye versjonen krever at hver blokk inkluderer høyden på blokken som opprettes, i `scriptSig` i coinbase-transaksjonen.



På den ene siden tydeliggjør denne utviklingen hvordan nettverket blir enige om å utvikle blokkstrukturen og konsensusreglene. For det andre sikrer den at hver blokk og coinbase-transaksjon er unik.



Dermed, coinbase er `scriptSig` er ikke helt gratis. Siden aktiveringen av BIP-34, er det rett og slett begrenset til å starte med høyden på blokken der denne coinbase-transaksjonen er inkludert.



![Image](assets/fr/035.webp)



#### Den ekstra-nonne



Som vi så i de første kapitlene i dette kurset, har utvinneren et 32-biters nonce-felt i blokkhodet, som de modifiserer ved å prøve og feile for å finne en hash som er mindre enn eller lik målet. Dette 32-biters feltet gir allerede mulighet til å utforske et svært stort antall kombinasjoner, men når mining-vanskelighetsgraden er høy, kan dette området bli fullstendig utnyttet på relativt kort tid, og dermed kan det hende at ingen kombinasjoner gir en gyldig hash. Hvis alle mulige verdier av `nonce` har blitt testet uten å lykkes, må utvinneren modifisere et annet element for å endre blokkoverskriften og starte en ny serie med forsøk.



Ettersom coinbase-transaksjonen tilbyr et fritt felt via `scriptSig` i inndataene, er løsningen som brukes for å utvide nonce-rommet å utnytte en del av denne `scriptSig`. Dette kalles vanligvis ekstra-nonce. Ved å modifisere extra-nonce endrer utvinneren myntbasens `scriptSig`, dvs. transaksjonsidentifikatoren, deretter Merkle-roten til blokken, og til slutt selve blokkhodet. På denne måten får de et nytt søkerom av hasher å utforske, uten å måtte endre de andre komponentene i kandidatblokken.



![Image](assets/fr/036.webp)



#### Identifisere bassenger og utvinnere



I dag er en svært stor andel av verdens hashrate organisert i mining-pooler. Disse strukturene samler individuelle gruvearbeidere for å kombinere arbeidet og redusere variasjonen i inntektene deres.



Av operasjonelle årsaker utnytter mining-bassenger også det frie feltet i coinbase-inngangens `scriptSig` til å sette inn ulike opplysninger. Disse varierer fra basseng til basseng og fra nettverksprotokoll til nettverksprotokoll, men inkluderer vanligvis en unik identifikator (ofte en ekstra nonce strukturert i flere underdeler) som tildeles hver gruvearbeider, for å unngå duplisering av arbeid i bassenget. Det legges vanligvis til en identifikasjonskode for bassenget, som brukes til offentlig attribusjon av blokker som er funnet, mining-statistikk og andre sporingsformål.



![Image](assets/fr/037.webp)



#### SegWits forpliktelse



Siden den myke SegWit fork ble aktivert i 2017, har vitnedata (dvs. generelt signaturer) blitt separert fra transaksjonsstammedata, særlig for å rette opp problemet med [manipulerbarhet i Bitcoin-transaksjoner](https://planb.academy/resources/glossary/malleability-transaction). Denne separasjonen introduserer derfor et nytt element som skal forpliktes i blokken.



For å gjøre dette grupperes vitnene sammen i et annet dedikert Merkle-tre, hvis rot deretter blir overført til coinbase-transaksjonen via en `OP_RETURN`-utgang.



![Image](assets/fr/038.webp)



Jeg vil ikke gå nærmere inn på denne mekanismen i dette kurset, da det er utenfor omfanget av denne artikkelen, men husk bare at siden introduksjonen av SegWit fungerer coinbase-transaksjonen som et middel til å forankre et fingeravtrykk som oppsummerer alle SegWit-vitner i blokken. Vitnene plasseres i et uavhengig Merkle-tre, roten til dette treet skrives til en utgang fra coinbase-transaksjonen, og denne coinbase-transaksjonen inkluderes selv i det viktigste Merkle-treet sammen med alle de andre transaksjonene, hvis rot vises i blokkoverskriften. Slik blir vitnene, som er lagret separat fra hovedtransaksjonsdataene, fortsatt forpliktet til blokkoverskriften.



![Image](assets/fr/039.webp)



#### Vilkårlige meldinger



Siden `scriptSig` tillater fri innsetting av vilkårlig informasjon valgt av gruvearbeideren, har noen benyttet seg av muligheten til å legge til meldinger av mer personlig karakter, i stedet for tekniske. Det mest kjente tilfellet er selvfølgelig Satoshi Nakamoto, med sin nå ikoniske melding:



> The Times 03/Jan/2009 Forbundskansleren på randen av en ny redningsaksjon for bankene

Denne meldingen, som finnes i Genesis-blokken (den aller første blokken i Bitcoin), er faktisk kodet i heksadesimal i `scriptSig` av coinbase-transaksjonen:



```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```


![Image](assets/fr/034.webp)



### Forfallsperioden


Når blokken er utvunnet og distribuert, vises coinbase-transaksjonen i blokkjeden som en hvilken som helst annen transaksjon. Den oppretter UTXOs for den vinnende utvinneren, slik at vedkommende kan motta belønningen sin. Disse UTXO-ene kan imidlertid ikke brukes umiddelbart: De er underlagt en [forfallsperiode](https://planb.academy/resources/glossary/maturity-period). Denne løpetiden er satt til 100 blokker etter blokken som inneholder coinbase. Konkret må coinbase-transaksjonen derfor ha 101 bekreftelser for at den vinnende utvinneren skal kunne bruke den.


![Image](assets/fr/040.webp)


Målet med denne regelen er å begrense effekten av kjedeomorganiseringer på økonomien. Som vi har sett i tidligere kapitler, kan det skje at to forskjellige gyldige blokker blir funnet nesten samtidig av forskjellige utvinnere på samme høyde. I et kort øyeblikk kan nettverket splittes: Noen noder mottar blokk A først, mens andre ser blokk B først. I løpet av de påfølgende blokkene akkumulerer én av de to grenene mer arbeid og blir referansegrenen. Den andre grenen forlates, og blokkene blir foreldet. Transaksjonene den inneholdt, kan da i teorien gå tilbake til mempoolene i påvente av bekreftelse.



I praksis skjer dette sjelden, fordi gebyrmarkedet ofte resulterer i at nesten de samme transaksjonene dukker opp i to konkurrerende blokker på samme høyde. Dette er en av grunnene til at en Bitcoin-transaksjon vanligvis anses å bli uforanderlig etter seks bekreftelser: Omorganiseringer av mer enn seks blokker er så usannsynlige at de med rimelighet kan anses som umulige.



![Image](assets/fr/041.webp)



Problemet med disse omorganiseringene i tilfellet med coinbase-transaksjonen er at det ikke er noen vanlig transaksjon. Den introduserer helt nye bitcoins i sirkulasjon. Hvis blokkbelønningen kunne brukes umiddelbart, kunne det oppstå en problematisk kaskadesituasjon:




- en gruvearbeider bruker bitcoins fra en myntbase,
- sirkulerer disse bitcoinsene i økonomien,
- så ble den opprinnelige blokken til slutt forlatt under en omorganisering.



Bitcoins i omløp ville da aldri ha eksistert i den endelige kjeden, og en rekke transaksjoner som var gyldige på utstedelsestidspunktet, ville bli ugyldige i ettertid.



Forfallsperioden er såpass lang at dette scenariet er urealistisk. En omorganisering av 101 blokker anses i praksis som umulig (selv om sannsynligheten er forsvinnende liten). Vi vet ikke nøyaktig hvorfor Satoshi valgte en så høy verdi for løpetid, men det er sannsynlig at den ble valgt for at mekanismen skulle forbli funksjonell, selv i tilfelle store nettverksfeil.



Denne regelen forhindrer at nyopprettede blokkbelønningspenger begynner å sirkulere før blokken som generated dem har blitt trygt begravd under en stor mengde akkumulert arbeid.



---

Vi har nå kommet til slutten av vår forklaring av hvordan Bitcoin mining fungerer. Du bør nå ha et klart bilde av de grunnleggende mekanismene som er involvert.



I siste del av kurset går vi tilbake til mer konkrete aspekter, for å vise deg hvordan Bitcoin mining materialiserer seg i den virkelige verden: industrialiseringen, maskinene som brukes, grupperingen av aktører, og så videre. Målet er å gi deg et helhetlig bilde av Bitcoin mining, både fra det teoretiske og protokollmessige perspektivet vi nettopp har sett, og også fra den praktiske og operasjonelle siden.



# Bitcoin mining-industrien


<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>



## Utviklingen av mining-maskiner


<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>



I Bitcoins tidlige dager var mining ikke en industriell aktivitet. Det var en del av Bitcoin-programvaren, som ble lansert på en personlig datamaskin, ofte av nysgjerrighet, noen ganger for å støtte nettverket, og sekundært for å skaffe bitcoins som da praktisk talt ikke hadde noen markedsverdi.



I årenes løp har denne aktiviteten gjennomgått en forvandling: maskinene har endret seg, vanskelighetsgraden har eksplodert, og mining har blitt en egen industri. La oss ta en titt på de operasjonelle aspektene ved Bitcoin mining.



### Kom godt i gang: mining med en CPU



I 2009 og i de første årene ble mining hovedsakelig utført ved hjelp av CPU-en på en vanlig datamaskin. Bitcoin var da bare en enkel programvare som fungerte som en wallet, en node og en miner. Det var nok å starte Satoshi Nakamoto-programvaren på datamaskinen din for å delta i mining-prosessen og i mange tilfeller finne blokker.



En CPU kan gjøre alt, men den er ikke optimalisert for noe som helst. Den utfører svært generelle instruksjoner med kompleks logikk. For en oppgave som repeterende hashing av blokkhoder er det ikke det ideelle verktøyet, men ved oppstart av nettverket er vanskelighetsgraden så lav at det er mer enn nok til å finne blokker.



Denne perioden er viktig, fordi den minner oss på et viktig poeng: proof of work er ikke avhengig av en bestemt kategori av utstyr. Det som teller, er evnen til å beregne hasher raskere enn andre, til en gitt kostnad. Så snart en teknisk fordel dukker opp, blir den automatisk omgjort til en økonomisk fordel. Men i absolutte termer er det i dag fortsatt mulig å forsøke å finne Bitcoin-blokker ved hjelp av en vanlig CPU. Det er for eksempel NerdMiner-prosjektet som har valgt denne tilnærmingen. Sjansen for å finne en blokk er tilnærmet lik null, men sannsynligheten er likevel forsvinnende liten.



https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Bytte til GPU-er



Snart innså utvinnerne at flaskehalsen ikke var kraft, men evnen til å utføre et stort antall lignende operasjoner parallelt. Det var akkurat dette grafikkprosessorenheter (GPU-er) kunne gjøre. Opprinnelig var en GPU designet for å utføre de samme operasjonene på store datamengder. Denne arkitekturen var perfekt egnet for en oppgave som gjentatt hashing: I stedet for å ha noen få, svært allsidige kjerner har du hundrevis, og deretter tusenvis av enheter som kan utføre de samme instruksjonene samtidig.



Med sammenlignbart strømforbruk kan en GPU produsere langt flere hasher per sekund enn en CPU. Samtidig hadde bitcoin en vekslingskurs mot dollaren, verdien økte, og det dukket opp vekslingsplattformer. Fra da av begynte mining å endre karakter. Det handlet ikke lenger bare om å delta, men om å tjene penger. Dedikerte konfigurasjoner dukket opp: maskiner bygget rundt flere grafikkort, noen ganger uten skjerm, med et minimalt system og spesialisert programvare, hvis eneste formål var å utvinne.



Det var på dette tidspunktet at vanskelighetsgraden for mining begynte å eksplodere. Mellom midten av 2010 og midten av 2011 økte den til og med med en faktor på 1000. Mekanisk sett begynner spesialiseringen, akkurat som de tidlige formene for industrialisering, og vanlige brukere - som nøyer seg med å kjøre Bitcoin-programvaren på PC-ene sine - har nå bare en svært liten sjanse til å finne en gyldig blokk.



![Image](assets/fr/044.webp)



*Kilde: [CoinWarz.com]() [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*



Mellom GPU-æraen og den moderne [ASIC](https://planb.academy/resources/glossary/asic)-æraen var det en mellomfase: bruken av FPGAer. En FPGA er en omprogrammerbar komponent: Den kan konfigureres til å implementere en logisk krets som er dedikert til en bestemt beregning, i dette tilfellet `SHA256d`. Tanken var å bevege seg enda lenger bort fra generell maskinvare (CPU/GPU) for å øke energieffektiviteten. Men snart ville forbedringene som ble gjort virtuelt på FPGA-er, bli brukt fysisk på selve brikkene: det er ankomsten av ASIC.



### Ankomsten av ASIC



Det siste trinnet i spesialiseringen av mining-maskinvaren var fremveksten av ASIC (*Application-Specific Integrated Circuits*). En ASIC er en brikke som er konstruert for en enkelt oppgave. I tilfellet med Bitcoin mining er denne oppgaven nettopp å utføre `SHA256d` med maksimal hastighet og optimal energieffektivitet. I motsetning til en GPU brukes ikke en ASIC til å kjøre spill, 3D-rendering eller AI. Den brukes til hashing, og det er alt.



![Image](assets/fr/045.webp)



*ASIC S21 XP produsert av Bitmain*



Denne spesialiseringen har to viktige konsekvenser:




- Det første er et sprang i ytelse og effektivitet. For enheter av sammenlignbar generasjon produserer en ASIC langt flere hasher per sekund enn en GPU, samtidig som den bruker mindre strøm. Mining med GPU ble raskt lite konkurransedyktig: Selv om det fungerte teknisk, var strømkostnadene langt høyere enn den forventede inntekten i de fleste sammenhenger;
- For det andre har modellen endret seg: Investeringene har hovedsakelig gått til maskinvare av industriell kvalitet. Mining innebærer nå at man kjøper maskiner som er designet for dette formålet, driver dem kontinuerlig, kjøler dem, vedlikeholder dem og absorberer foreldelsen av dem. En ASIC er nemlig ikke evigvarende: Når en ny, mer effektiv generasjon kommer på markedet, blir de gamle maskinene gradvis mindre lønnsomme, selv om de fortsatt fungerer.



Fra da av snakker vi ikke lenger bare om en hobby. Vi snakker om en sektor der konkurransekraften avhenger av en ligning:




- kostnader for elektrisitet;
- kostnader til utstyr og avskrivninger;
- evne til å kjøle ned og operere i stor skala;
- maskinens tilgjengelighet og pålitelighet;
- kommunikasjonshastighet;
- osv.



### Mining gårder



En isolert maskin kan drive gruvedrift, men ved å gruppere hundrevis, og deretter tusenvis av ASIC-maskiner på ett enkelt sted, deler vi faste kostnader, optimaliserer logistikken og nærmer oss en spesialisert datasentermodell.



En [mining-farm](https://planb.academy/resources/glossary/mining-farm) er i sin enkleste form en bygning (eller et sett med containere) fylt med ASIC-er som kjører 24/7. Utfordringen nå er å opprettholde stabile driftsforhold:




- levere store mengder billig og stabil elektrisk kraft;
- håndtere varmen for å unngå struping, ettersom energitettheten er betydelig;
- filtrer støv, kontroller fuktighet, rengjør;
- sanntidsovervåking av maskinens ytelse (temperaturer, maskinvarefeil, hashrate-fall osv.).



![Image](assets/fr/043.webp)



*En av de sju bygningene som er dedikert til Bitcoin mining på Riot Platforms' anlegg i Rockdale, nær Austin i Texas. Denne er spesielt dedikert til nedsenking mining*



Mining drives nå av industrielle aktører, noen av dem børsnoterte, som bygger og driver svært store oppdrettsanlegg. Blant disse er MARA Holdings (Nasdaq: `MARA`) og Riot Platforms (Nasdaq: `RIOT`).



![Image](assets/fr/042.webp)



Selv uten å gå inn på detaljene i lønnsomhetsmodellene, er det viktig å forstå hvorfor mining har tatt denne formen. Proof-of-work er en konkurransemekanisme: Sannsynligheten for å finne en blokk, og dermed tjene penger, er proporsjonal med andelen av hashrate du distribuerer. Derfor er det et konstant press for å øke datakraften, redusere kostnadene per beregningsenhet og begrense tapene. Derfor blir miljøer som tilbyr billigere strøm, et klima som bidrar til kjøling eller en rikholdig energiinfrastruktur, naturlig nok mer attraktive.



Mining Bitcoin har dermed utviklet seg fra å være en aktivitet som var tilgjengelig for alle i begynnelsen, til å bli en aktivitet som domineres av spesialutstyr og profesjonell drift. Dette endrer ikke reglene i protokollen. I teorien kan hvem som helst utvinne med hvilken som helst maskin. Men i praksis har vanskelighetsgraden og effektiviteten til ASIC gjort innenlandsk mining lite konkurransedyktig i de fleste sammenhenger.



Det finnes selvfølgelig fortsatt situasjoner der mining hjemme kan være interessant, for eksempel hvis du drar nytte av svært billig strøm, eller hvis du bruker varmen generated fra gruvearbeideren din til å varme opp hjemmet ditt om vinteren. Men uansett må du fortsatt kjøpe en maskin utstyrt med en ASIC-brikke. Siden mining-kraften din vil forbli ekstremt liten i forhold til Bitcoin-nettverket, må du dessuten finne en måte å redusere variansen i inntekten din på: Dette er nettopp rollen til mining-pooler, som vi skal diskutere i neste kapittel.



Hvis du ønsker å utforske mining-løsninger med varmegjenvinning i hjemmet, har vi veiledninger om ulike verktøy, både ferdige til bruk og gjør-det-selv-løsninger:



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## Gruppering i mining-pooler


<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>



Mining Bitcoin innebærer løpende og uunngåelige kostnader, først og fremst maskinens strømforbruk. Disse utgiftene påløper uavhengig av eventuelle resultater, selv om inntektene fra mining i sin natur er sjeldne og tilfeldige. Oppdagelsen av en blokk avhenger utelukkende av utvinnerens andel av hashrate, noe som gjør inntjeningen desto mer uforutsigbar jo mindre denne andelen er. Det er nettopp dette praktiske problemet som raskt førte til den utbredte bruken av [mining-pooler](https://planb.academy/resources/glossary/pool-mining). I dette siste kapittelet av MIN 101-kurset gir jeg en innføring i prinsippene og driften av mining-bassenger i Bitcoin.



### Hva er et mining-basseng?



Et mining-basseng er en organisasjon (ofte en nettbasert tjeneste) som samler datakraften til mange uavhengige utvinnere, for å øke frekvensen som gruppen finner blokker med. Når gruppen finner en blokk, blir blokkbelønningen omfordelt mellom deltakerne i henhold til interne regler for gruppen (som vil bli dekket i MIN 201-kurset, ettersom de er for komplekse for MIN 101).



Deltakerne i en mining-pool blir da ofte referert til som "[hashere](https://planb.academy/resources/glossary/hasher)" i stedet for "minere", ettersom de ikke lenger utfører alt mining-arbeidet, men bare hasher dataene som overføres til dem fra poolen.



Vær forsiktig så du ikke forveksler mining-poolen med mining-farmen. Dette er to forskjellige konsepter. Som vi så i forrige kapittel, er en farm et fysisk sted der en enkelt enhet driver en rekke mining-maskiner. En pool, derimot, er først og fremst en virtuell gruppering: tusenvis av maskiner, ofte geografisk spredt, arbeider under en felles koordinering. En farm kan imidlertid delta i en pool, og gjør det ofte.



![Image](assets/fr/048.webp)



### Redusere inntektsvariansen



Så hvorfor bli med i en pool? Ganske enkelt fordi resultatet av mining-aktiviteten er sannsynlighetsbasert: For hvert hashforsøk er det en svært liten sjanse for at det vil oppfylle vanskelighetsmålet og dermed produsere en gyldig blokk.



På svært lang sikt bør den gjennomsnittlige inntjeningen din være proporsjonal med din andel av den samlede hashrate. Dette prinsippet følger direkte av sannsynlighetsloven: Hver hash-beregning utgjør en uavhengig tilfeldig trekning, og i henhold til loven om store tall vil hyppigheten du oppdager blokker med, konvergere matematisk mot din andel av nettverkets totale hashrate. På kort til mellomlang sikt kan den faktiske inntjeningen din imidlertid være ekstremt uregelmessig. Det er dette avviket mellom det teoretiske gjennomsnittet og den tilfeldige virkeligheten som vi kaller **varians** i matematikken.



Her er et enkelt eksempel for å illustrere prinsippet:




- Bitcoin-nettverket produserer i gjennomsnitt 144 blokker per dag (omtrent én blokk hvert 10. minutt);
- Hvis du har "0,0001 %" av den totale hashrate, er forventningen din "144 × 0,000001", eller "0,000144" blokker/dag;
- Med andre ord bør du finne en blokk i gjennomsnitt hver `1 / 0,000144` dag, dvs. hver 6 944. dag, eller rundt 19 år.



Men denne verdien tilsvarer bare en matematisk forventning: Fordelingen av funntider følger en tilfeldig lov, så det er i praksis fullt mulig å aldri finne en eneste blokk, selv over en svært lang periode. Du kan være uheldig og ikke finne noe på svært lang tid, samtidig som du betaler løpende kostnader (strøm, vedlikehold, avskrivning av utstyr...).



mining-poolen endrer dette problemets natur: Ved å kombinere hashrate-er finner poolen blokker oftere. Hver deltaker går da med på å motta bare en brøkdel av hver blokk som blir funnet, men mye oftere. Det er en transformasjon fra en svært volatil inntekt med stor spredning til en mer regelmessig inntekt, på bekostning av deling av belønningene og betaling av serviceavgifter.



### Hvorfor synker variansen når man grupperer sammen?



Jo høyere datakraft du har, desto høyere er den forventede frekvensen av blokker som blir funnet. Enda viktigere er det at jo hyppigere hendelsene er, desto nærmere er de observerte resultatene det statistiske gjennomsnittet over en gitt periode.



På solobasis kan en småskala gruvearbeider gå i årevis uten en eneste blokk, for så å få en stor utbetaling en dag, og deretter ingenting. I et basseng gjelder fortsatt den samme sannsynlighetsbaserte virkeligheten, men den glattes ut på kollektiv skala: Bassenget finner blokker oftere, og omfordeling konverterer disse hendelsene til mer regelmessige utbetalinger for hver deltaker. **mining-poolen selger derfor forutsigbarhet på mining-aktiviteten**.



### Historiske landemerker



Som vi så i forrige kapittel, kunne mining i begynnelsen gjøres alene med en vanlig datamaskin, ettersom vanskelighetsgraden var svært lav. Men etter hvert som det globale hashrate eksploderte (GPU, deretter ASIC), ble solo mining et svært tidkrevende sjansespill for de fleste deltakerne.



De første bassengene ble opprettet nettopp som svar på denne nye virkeligheten. Braiins Pool (tidligere Slush Pool / Bitcoin.cz) er det første Bitcoin mining-bassenget: Det utvunnet sin første blokk 16. desember 2010. Dette første mining-bassenget ble raskt en suksess, og i løpet av bare noen få dager tok det nesten 3,5 % av den globale hashrate.



![Image](assets/fr/047.webp)



På den tekniske siden ble bassengene deretter strukturert rundt spesialiserte kommunikasjonsprotokoller mellom bassenget og utvinnerne (f.eks. [Stratum](https://planb.academy/resources/glossary/stratum), deretter Stratum V2), for å kunne organisere distribuert arbeid på en effektiv måte. Vi skal se nærmere på disse konseptene i MIN 201-kurset vårt.



### Den moderne situasjonen



I skrivende stund (tidlig i 2026) er den globale Bitcoin hashrate på en størrelsesorden av zetta-hash per sekund (= 1000 EH/s = 1 000 000 000 000 000 000 000 000 hashes per sekund), og nesten alle blokkene som finnes, kommer fra mining-bassenger.



Her er en rangering av de viktigste mining-poolene og deres respektive andel av hashrate. Denne rangeringen vil sannsynligvis endre seg når du leser dette kurset. For oppdaterte data, besøk [mempool.space] (https://mempool.space/graphs/mining/pools).



![Image](assets/fr/046.webp)



| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Kilde [mempool.space] (https://mempool.space/graphs/mining/pools), én måneds data, 16. desember 2025 til 16. januar 2025.*



I et mer avansert kurs vil vi gå nærmere inn på hvordan bassengene fungerer internt (aksjer, nettverksprotokoller, betalingsmetoder ...), fordi det er her detaljene som avgjør både gruvearbeiderens lønnsomhet og de potensielle konsekvensene for Bitcoin kommer inn i bildet.



---

Vi har nå kommet til slutten av MIN 101. Takk for at du har fulgt kurset helt til slutten. Hvis du ønsker å vurdere ferdighetene du har tilegnet deg gjennom kurset, venter en avsluttende eksamen i neste avsnitt.



Med den grunnleggende kunnskapen du nettopp har tilegnet deg, kan du nå ta mer avanserte kurs om mining på Plan ₿ Academy, enten det er i teori, som dette, eller mer praktiske kurs, slik at du også kan begynne å delta i Bitcoin mining!



# Siste del


<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>



## Anmeldelser og rangeringer


<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>


<isCourseReview>true</isCourseReview>

## Avsluttende eksamen


<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>


<isCourseExam>true</isCourseExam>

## Konklusjon


<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>


<isCourseConclusion>true</isCourseConclusion>