---
name: Whirlpool Stats Tools - Anonsets
description: Forstå konseptet med anonset og hvordan man beregner det med WST
---
![cover](assets/cover.webp)

***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, er Whirlpool Stats Tool ikke lenger tilgjengelig for nedlasting, ettersom det var hostet på Samourais Gitlab. Selv om du tidligere hadde lastet ned dette verktøyet lokalt til din maskin, eller det var installert på din RoninDojo-node, vil WST ikke fungere for øyeblikket. Det var avhengig av data levert av OXT.me for sin drift, og dette nettstedet er ikke lenger tilgjengelig. For øyeblikket er WST ikke spesielt nyttig siden Whirlpool-protokollen er inaktiv. Det er imidlertid mulig at disse programmene kan bli gjeninnført i de kommende ukene. Videre er den teoretiske delen av denne artikkelen fortsatt relevant for å forstå prinsippene og målene med coinjoins generelt (ikke bare Whirlpool), samt forstå effektiviteten av Whirlpool-modellen. Du kan også lære hvordan du kvantifiserer personvernet som tilbys av coinjoin-sykluser.*

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen etter hvert som ny informasjon blir tilgjengelig._

_Denne opplæringen er gitt kun til utdannings- og informasjonsformål. Vi støtter eller oppmuntrer ikke bruk av disse verktøyene til kriminelle formål. Det er hver brukers ansvar å overholde lovene i sin jurisdiksjon_

---

*"Bryt lenken myntene dine etterlater seg"*

I denne opplæringen vil vi studere konseptet med anonsets, indikatorer som lar oss estimere kvaliteten på en coinjoin-prosess på Whirlpool. Vi vil dekke beregningsmetoden og tolkningen av disse indikatorene. Etter den teoretiske delen, vil vi gå over til praksis ved å lære å beregne anonsets for en spesifikk transaksjon ved hjelp av Python-verktøyet *Whirlpool Stats Tools* (WST).

## Hva er en coinjoin på Bitcoin?
**Coinjoin er en teknikk som bryter sporbarheten til bitcoins på blokkjeden**. Den støtter seg på en samarbeidstransaksjon med en spesifikk struktur med samme navn: coinjoin-transaksjonen.

Coinjoin-transaksjoner forbedrer personvernet til Bitcoin-brukere ved å komplisere kjedeanalyse for eksterne observatører. Deres struktur tillater å slå sammen flere mynter fra forskjellige brukere i en enkelt transaksjon, dermed tåkelegge sporene og gjøre det vanskelig å bestemme koblingene mellom inngangs- og utgangsadresser.

Prinsippet med coinjoin er basert på en samarbeidstilnærming: flere brukere som ønsker å blande sine bitcoins, setter inn identiske beløp som innganger i samme transaksjon. Disse beløpene blir deretter omfordelt i utganger av tilsvarende verdi. Ved slutten av transaksjonen blir det umulig å knytte en spesifikk utgang til en gitt bruker. Ingen direkte lenke eksisterer mellom inngangene og utgangene, dermed brytes assosiasjonen mellom brukerne og deres UTXO, samt historikken til hver mynt.

![coinjoin](assets/notext/1.webp)

Eksempel på en coinjoin-transaksjon:
[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)
For å gjennomføre en coinjoin samtidig som hver bruker opprettholder kontroll over sine midler til enhver tid, begynner prosessen med konstruksjonen av transaksjonen av en koordinator, som deretter overfører den til hver deltaker. Hver bruker signerer deretter transaksjonen etter å ha verifisert at den passer for dem. Alle innsamlede signaturer integreres til slutt i transaksjonen. Hvis et forsøk på å omdirigere midler blir gjort av en bruker eller koordinatoren, ved å endre utgangene av coinjoin-transaksjonen, vil signaturene vise seg å være ugyldige, noe som fører til at transaksjonen avvises av nodene.
Det finnes flere implementeringer av coinjoin, som Whirlpool, JoinMarket, eller Wabisabi, hver med mål om å håndtere koordineringen mellom deltakerne og øke effektiviteten av coinjoin-transaksjoner.
I denne opplæringen vil vi fokusere på min favorittimplementering: Whirlpool, som er tilgjengelig på Samourai Wallet og Sparrow Wallet. Etter min mening er det den mest effektive implementeringen for coinjoins på Bitcoin.
## Hva er nytten av coinjoin på Bitcoin?
Nytten av coinjoin ligger i dens evne til å produsere plausibel fornektelse, ved å drukne din mynt innenfor en gruppe av uatskillelige mynter. Målet med denne handlingen er å bryte sporbarhetslenkene, både fra fortiden til nåtiden og fra nåtiden til fortiden.

Med andre ord, en analytiker som kjenner din opprinnelige transaksjon ved inngangen av coinjoin-syklusene, bør ikke kunne identifisere med sikkerhet din UTXO ved utgangen av remix-syklusene (analyse fra syklusinngang til syklusutgang).

![coinjoin](assets/en/2.webp)

Omvendt, en analytiker som kjenner din UTXO ved utgangen av coinjoin-syklusene, bør ikke kunne bestemme den opprinnelige transaksjonen ved inngangen av syklusene (analyse fra syklusutgang til syklusinngang).

![coinjoin](assets/en/3.webp)

For å vurdere vanskeligheten for en analytiker til å koble fortiden til nåtiden og omvendt, er det nødvendig å kvantifisere størrelsen på gruppene innenfor hvilke din mynt er skjult. Dette målet forteller oss antall analyser som har en identisk sannsynlighet. Så, hvis den korrekte analysen er druknet blant 3 andre analyser med lik sannsynlighet, er ditt nivå av skjuling veldig lavt. På den annen side, hvis den korrekte analysen er innenfor et sett av 20 000 analyser alle like sannsynlige, er din mynt veldig godt skjult.

Og nettopp, størrelsen på disse gruppene representerer indikatorer som kalles "anonsets".

## Forståelse av anonsets
Anonsets fungerer som indikatorer for å evaluere graden av personvern for en spesifikk UTXO. Mer spesifikt måler de antall uatskillelige UTXOer innenfor settet som inkluderer den studerte mynten. Kravet om et homogent UTXO-sett betyr at anonsets vanligvis beregnes over coinjoin-sykluser. Bruken av disse indikatorene er spesielt relevant for Whirlpool coinjoins på grunn av deres uniformitet.

Anonsets tillater, der det er hensiktsmessig, å bedømme kvaliteten på coinjoins. En stor anonset-størrelse betyr et økt nivå av anonymitet, ettersom det blir vanskelig å skille en spesifikk UTXO innenfor settet.

Det er to typer anonsets:
- **Det prospektive anonymitetssettet;**
- **Det retrospektive anonymitetssettet.**
Den første indikatoren viser størrelsen på gruppen blant hvilken den studerte UTXO er skjult ved slutten av syklusen, med kjennskap til UTXO ved inngangen, det vil si antallet uatskillelige mynter til stede innenfor denne gruppen. Denne indikatoren tillater måling av myntens konfidensialitetsmotstand mot en analyse fra fortid til nåtid (inngang til utgang). På engelsk er navnet på denne indikatoren "*forward anonset*", eller "*forward-looking metrics*".
![coinjoin](assets/en/4.webp)
Denne metrikken anslår i hvilken grad din UTXO er beskyttet mot forsøk på å rekonstruere historikken fra inngangspunktet til utgangspunktet i coinjoin-prosessen.

For eksempel, hvis transaksjonen din deltok i sin første coinjoin-syklus og to andre etterkommende sykluser ble fullført, ville det fremtidige anonsetet for mynten din være `13`:

![coinjoin](assets/en/5.webp)

Den andre indikatoren viser antall mulige kilder for en gitt mynt, med kjennskap til UTXOen ved slutten av syklusen. Denne indikatoren måler motstanden av myntens konfidensialitet mot en analyse fra nåtid til fortid (utgang til inngang), det vil si hvor vanskelig det er for en analytiker å spore tilbake til opprinnelsen til mynten din, før coinjoin-syklusene. På engelsk er navnet på denne indikatoren "*backward anonset*", eller "*backward-looking metrics*".

![coinjoin](assets/en/6.webp)

Ved å kjenne din UTXO ved utgangen av syklusene, bestemmer det retrospektive anonsetet antall potensielle Tx0-transaksjoner som kunne ha utgjort din inngang i coinjoin-syklusene. I diagrammet nedenfor tilsvarer dette summen av alle de oransje boblene.

![coinjoin](assets/en/7.webp)

## Beregning av anonsets med Whirlpool Stats Tools (WST)
For å beregne disse indikatorene på dine egne mynter som har gått gjennom coinjoin-sykluser, kan du bruke et verktøy spesielt utviklet av Samourai Wallet: *Whirlpool Stats Tools*.

Hvis du har en RoninDojo, er WST forhåndsinstallert på noden din. Du kan derfor hoppe over installasjonstrinnene og direkte følge bruksstegene. For de som ikke har en RoninDojo-node, la oss se hvordan vi skal gå frem med installasjonen av dette verktøyet på en datamaskin.

Du trenger: Tor Browser (eller Tor), Python 3.4.4 eller høyere, git og pip. Åpne en terminal. For å sjekke tilstedeværelsen og versjonen av disse programmene på systemet ditt, skriv inn følgende kommandoer:
```plaintext
python --version
git --version
pip --version
```

Om nødvendig, kan du laste dem ned fra deres respektive nettsteder:
- https://www.python.org/downloads/ (pip kommer direkte med Python siden versjon 3.4);
- https://www.torproject.org/download/;
- https://git-scm.com/downloads.
Når alle disse programmene er installert, fra en terminal, klone WST-repositoriet:
```plaintext
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```

![WST](assets/notext/8.webp)

Naviger til WST-katalogen:
```plaintext
cd whirlpool_stats
```

Installer avhengighetene:
```plaintext
pip3 install -r ./requirements.txt
```

![WST](assets/notext/9.webp)

Du kan også installere dem manuelt (valgfritt):
```plaintext
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```

Naviger til `/whirlpool_stats` undermappen:
```plaintext
cd whirlpool_stats
```

Start WST:
```plaintext
python3 wst.py
```

![WST](assets/notext/10.webp)

Start Tor eller Tor Browser i bakgrunnen.

**-> For RoninDojo-brukere, kan du gjenoppta opplæringen direkte her.**

Sett proxyen til Tor (RoninDojo),
```plaintext
socks5 127.0.0.1:9050
```
eller til Tor Browser, avhengig av hva du bruker:```plaintext
socks5 127.0.0.1:9150
```

Denne manipulasjonen vil tillate deg å laste ned data på OXT via Tor, for å ikke lekke informasjon om transaksjonene dine. Hvis du er nybegynner og dette steget virker komplekst, vit at det enkelt innebærer å dirigere internett-trafikken din gjennom Tor. Den enkleste metoden består av å starte Tor Browser i bakgrunnen på datamaskinen din, deretter utføre kun det andre kommandoen for å koble til via denne nettleseren (`socks5 127.0.0.1:9150`).

![WST](assets/notext/11.webp)

Naviger deretter til arbeidskatalogen fra hvilken du har tenkt å laste ned WST-data ved å bruke `workdir`-kommandoen. Denne mappen vil tjene til å lagre transaksjonsdataene som du vil hente fra OXT i form av `.csv`-filer. Denne informasjonen er essensiell for å beregne indikatorene du ser etter å oppnå. Du står fritt til å velge plasseringen av denne katalogen. Det kan være lurt å opprette en mappe spesifikt for WST-data. Som et eksempel, la oss velge nedlastingsmappen. Hvis du bruker RoninDojo, er dette steget ikke nødvendig:
```plaintext
workdir path/to/your/directory
```

Kommandoprompten skal da ha endret seg for å indikere din arbeidskatalog.

![WST](assets/notext/12.webp)

Last deretter ned dataene fra bassenget som inneholder transaksjonen din. For eksempel, hvis jeg er i `100,000 sats`-bassenget, er kommandoen:
```plaintext
download 0001
```

![WST](assets/notext/13.webp)

Valørkodene på WST er som følger:
- Bassenget 0.5 bitcoins: `05`
- Bassenget 0.05 bitcoins: `005`
- Bassenget 0.01 bitcoins: `001`
- Bassenget 0.001 bitcoins: `0001`
Når dataene er lastet ned, last dem inn. For eksempel, hvis jeg er i bassenget av `100,000 sats`, er kommandoen:
```plaintext
load 0001
```

Dette steget tar noen minutter avhengig av datamaskinen din. Nå er et godt tidspunkt å lage deg en kaffe! :)

![WST](assets/notext/14.webp)

Etter å ha lastet inn dataene, skriv `score`-kommandoen etterfulgt av din TXID (transaksjonsidentifikator) for å få dens anonsets:
```plaintext
score TXID
```

**Oppmerksomhet**, valget av TXID å bruke varierer avhengig av anonsettet du ønsker å beregne. For å vurdere det fremtidige anonsettet til en mynt, er det nødvendig å angi, via `score`-kommandoen, TXID som tilsvarer dens første coinjoin, som er den første blandingen utført med denne UTXO. På den annen side, for å bestemme det retrospektive anonsettet, må du angi TXID for den siste coinjoin utført. For å oppsummere, beregnes det fremtidige anonsettet fra TXID av den første blandingen, mens det retrospektive anonsettet beregnes fra TXID av den siste blandingen.

WST viser deretter det retrospektive resultatet (*Backward-looking metrics*) og det fremtidige resultatet (*Forward-looking metrics*). For eksempel tok jeg TXID til en tilfeldig mynt på Whirlpool som ikke tilhører meg.

![WST](assets/notext/15.webp)
Transaksjonen det er snakk om: [7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)
Hvis vi betrakter denne transaksjonen som den første coinjoin utført for den aktuelle mynten, så nyter den godt av et potensielt anonset på `86,871`. Dette betyr at den er skjult blant `86,871` ugjenkjennelige mynter. For en ekstern observatør som kjenner denne mynten ved starten av coinjoin-syklusene og forsøker å spore dens utgang, vil de stå overfor `86,871` mulige UTXOer, hver med en identisk sannsynlighet for å være den ettertraktede mynten.

Hvis vi betrakter denne transaksjonen som den siste coinjoin for mynten, har den da et retrospektivt anonset på `42,185`. Dette betyr at det er `42,185` potensielle kilder for denne UTXOen. Hvis en ekstern observatør identifiserer denne mynten ved slutten av syklusene og søker å spore dens opprinnelse, vil de stå overfor `42,185` mulige kilder, alle med lik sannsynlighet for å være den søkte opprinnelsen.
I tillegg til anonset-poengene, gir WST deg også diffusjonsraten for din utgang innenfor bassenget basert på anonsetet. Denne andre indikatoren lar deg ganske enkelt vurdere potensialet for forbedring av ditt stykke. Denne raten er spesielt nyttig for det potensielle anonsetet. Faktisk, hvis ditt stykke har en diffusjonsrate på 15%, betyr det at det kan forveksles med 15% av stykkene i bassenget. Det er bra, men du har fortsatt en veldig stor margin for forbedring ved å fortsette å remixe. På den annen side, hvis ditt stykke har en diffusjonsrate på 95%, så nærmer du deg grensene for bassenget. Du kan fortsette å remixe, men ditt anonset vil ikke øke mye.

Det er viktig å merke seg at anonsetene beregnet av WST ikke er helt nøyaktige. Gitt det enorme volumet av data som må behandles, bruker WST *HyperLogLogPlusPlus*-algoritmen for å betydelig redusere byrden forbundet med lokal databehandling og nødvendig minne. Dette er en algoritme som tillater estimering av antall distinkte verdier i veldig store datasett mens man opprettholder høy nøyaktighet i resultatet. Derfor er poengene som tilbys gode nok til å brukes i analysene dine, ettersom de er veldig nære estimater til virkeligheten, men de bør ikke tolkes som eksakte verdier til enheten.

Til slutt, husk at det ikke er avgjørende å systematisk beregne anonsetene for hver av dine stykker i coinjoins. Selv designet av Whirlpool gir allerede garantier. Faktisk er det retrospektive anonsetet sjelden en bekymring. Fra din første blanding, oppnår du en spesielt høy retrospektiv score takket være arven fra tidligere blandinger siden Genesis coinjoin. Når det gjelder det potensielle anonsetet, er det nok å holde ditt stykke i post-mix-kontoen for en tilstrekkelig lang periode.
Dette er grunnen til at jeg anser bruken av Whirlpool som spesielt relevant i en *Hodl -> Mix -> Spend -> Replace* strategi. Etter min mening er den mest logiske tilnærmingen å holde hoveddelen av ens bitcoin-sparing i en kald lommebok, mens man kontinuerlig opprettholder et visst antall biter i coinjoins på Samourai for å dekke daglige utgifter. Når bitcoinene fra coinjoins er brukt, erstattes de med nye, for å returnere til det definerte terskelnivået av blandete biter. Denne metoden lar en frigjøre seg fra bekymringen for våre UTXO anonsets, samtidig som tiden som er nødvendig for effektiviteten av coinjoins blir mye mindre begrensende.
**Eksterne Ressurser:**

- [Podcast på fransk om kjedeanalyse](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [Wikipedia-artikkel om HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog)
- Samourais repositorium for Whirlpool-statistikk
- Whirlpool-nettstedet av Samourai
- [Medium-artikkel på engelsk om personvern og Bitcoin av Samourai](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [Medium-artikkel på engelsk om konseptet med anonymitetssett av Samourai](https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7)