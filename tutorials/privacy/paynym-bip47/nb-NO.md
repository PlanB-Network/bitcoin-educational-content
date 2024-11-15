---
name: BIP47 - PayNym

description: Hvordan PayNyms fungerer
---
***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, kan ikke applikasjonen lenger brukes av brukere som ikke har sin egen Dojo. BIP47 forblir brukbart på Sparrow Wallet for alle brukere og **på Samourai Wallet kun for brukere som har en Dojo**.*

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne veiledningen så snart ny informasjon blir tilgjengelig._

_Denne veiledningen er gitt kun for utdannings- og informasjonsformål. Vi støtter eller oppfordrer ikke til bruk av disse verktøyene til kriminelle formål. Det er brukerens ansvar å overholde lovene i sin jurisdiksjon._

---

> "Han er for stor," sa de alle, og kalkunhanen, som var født med sporer og trodde han var en keiser, blåste seg opp som et skip med alle seil satt, og marsjerte rett opp til ham i stor raseri, øynene røde som ild. Den stakkars lille andungen visste ikke om han skulle stå imot eller løpe vekk, og var veldig ulykkelig fordi han var foraktet av alle endene i gården.

![BIP47, den stygge andungen illustrasjon](assets/1.webp)

Et av de mest betydelige problemene i Bitcoin-protokollen er gjenbruk av adresser. Gjennomsiktigheten og distribusjonen av nettverket gjør denne praksisen farlig for brukerens personvern. For å unngå problemer relatert til dette, anbefales det å bruke en ny blank mottaksadresse for hver ny innkommende betaling til en lommebok, noe som kan være komplisert å oppnå i noen tilfeller.

Dette kompromisset er like gammelt som White Paper. Satoshi advarte oss allerede om denne risikoen i sitt arbeid publisert i slutten av 2008:

> "Som en ekstra brannmur, bør et nytt nøkkelpar brukes for hver transaksjon for å hindre at de blir knyttet til en felles eier."

Det finnes mange løsninger tilgjengelig for å motta flere betalinger uten gjenbruk av adresser. Hver av dem har sine kompromisser og ulemper. Blant alle disse løsningene finnes det [BIP47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki), et forslag utviklet av Justus Ranvier og publisert i 2015, som tillater generering av gjenbrukbare betalingskoder. Målet er å muliggjøre flere transaksjoner til samme person uten å gjenbruke en adresse.

Opprinnelig ble dette forslaget møtt med forakt av en del av fellesskapet, og det ble aldri lagt til i Bitcoin Core. Imidlertid valgte noen programvarer fortsatt å implementere det på egen hånd. For eksempel utviklet Samourai Wallet sin egen implementering av BIP47: PayNym. I dag er denne implementeringen tilgjengelig på Samourai Wallet for smarttelefoner, samt på [Sparrow Wallet](https://sparrowwallet.com/) for PCer.

Over tid har Samourai programmert nye funksjoner direkte relatert til PayNym. Nå finnes det et helt økosystem av verktøy tilgjengelig for å optimalisere brukerens personvern basert på PayNym og BIP47.
I denne artikkelen vil du oppdage prinsippet bak BIP47 og PayNym, mekanismene til disse protokollene, og de praktiske anvendelsene som følger av dem. Jeg vil kun adressere den første versjonen av BIP47, som for øyeblikket brukes for PayNym, men versjoner 2, 3, og 4 fungerer praktisk talt på samme måte.
Den eneste store forskjellen finnes i varslingstransaksjonen. Versjon 1 bruker en enkel adresse med OP_RETURN for varsling, versjon 2 bruker et multisig-skript (bloom-multisig) med OP_RETURN, og versjoner 3 og 4 bruker rett og slett et multisig-skript (cfilter-multisig). Mekanismene som diskuteres i denne artikkelen, inkludert de kryptografiske metodene som er studert, er derfor anvendelige på alle fire versjonene. Til dags dato bruker PayNym-implementeringen på Samourai Wallet og Sparrow den første versjonen av BIP47.
## Sammendrag:

1- Problemet med gjenbruk av adresser.

2- Prinsippene for BIP47 og PayNym.

3- Veiledninger: Bruk av PayNym.

- Bygging av en BIP47-transaksjon med Samourai Wallet.
- Bygging av en BIP47-transaksjon med Sparrow Wallet.

4- Hvordan BIP47 fungerer.

- Den gjenbrukbare betalingskoden.
- Den kryptografiske metoden: Diffie-Hellman nøkkelutveksling etablert på elliptiske kurver (ECDH).
- Varslingstransaksjonen.
- Konstruksjon av varslingstransaksjonen.
- Mottak av varslingstransaksjonen.
- BIP47-betalingstransaksjonen.
- Mottak av BIP47-betalingen og derivasjon av den private nøkkelen.
- Refundering av BIP47-betalingen.

5- Avledede bruksområder for PayNym.

6- Min personlige mening om BIP47.

## Problemet med gjenbruk av adresser.

En mottaksadresse brukes til å motta bitcoins. Den genereres fra en offentlig nøkkel ved å hashe den og anvende et spesifikt format. Dermed tillater den opprettelsen av en ny betingelse for utgifter på en mynt for å endre eieren.

> For å lære mer om generering av en mottaksadresse, anbefaler jeg å lese den siste delen av denne artikkelen: The Bitcoin Wallet - utdrag fra [ebook Bitcoin Démocratisé 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2#viewer-epio7).

Videre har du sannsynligvis allerede hørt fra en kunnskapsrik bitcoiner at mottaksadresser er for engangsbruk, og at du bør generere en ny for hver ny innkommende betaling til lommeboken din. Ok, men hvorfor?
Grunnleggende sett setter ikke gjenbruk av adresser dine midler direkte i fare. Bruken av kryptografi på elliptiske kurver lar deg bevise for nettverket at du er i besittelse av en privat nøkkel uten å avsløre den nøkkelen. Derfor kan du låse flere forskjellige UTXOer (Unspent Transaction Outputs) på samme adresse og bruke dem på forskjellige tidspunkter. Hvis du ikke avslører den private nøkkelen som er assosiert med den adressen, kan ingen få tilgang til dine midler. Problemet med gjenbruk av adresser er mer relatert til personvern.

Som nevnt i introduksjonen, betyr transparensen og distribusjonen av Bitcoin-nettverket at enhver bruker med tilgang til en node kan observere transaksjonene i betalingssystemet. Som et resultat kan de se de forskjellige saldoene på adressene. Satoshi Nakamoto nevnte deretter muligheten for å generere nye nøkkelpar, og dermed nye adresser, for hver ny innkommende betaling til en lommebok. Målet ville være å ha en ekstra brannmur i tilfelle en assosiasjon mellom brukerens identitet og ett av deres nøkkelpar.

I dag, med tilstedeværelsen av kjedeanalysefirmaer og utviklingen av KYC (Know Your Customer), er bruken av blanke adresser ikke lenger en ekstra brannmur, men en forpliktelse for alle som bryr seg så lite som litt om sitt personvern.

Jakten på personvern er ikke en komfort eller en fantasi av maksimalistiske Bitcoiners. Det er en spesifikk parameter som direkte påvirker din personlige sikkerhet og sikkerheten til dine midler. For å hjelpe deg med å forstå dette, her er et veldig konkret eksempel:
- Bob kjøper Bitcoin gjennom Dollar Cost Averaging (DCA), noe som betyr at han anskaffer en liten mengde Bitcoin med jevne mellomrom for å gjennomsnittlig sin inngangspris. Bob sender systematisk de kjøpte midlene til samme mottaksadresse. Han kjøper 0,01 Bitcoin hver uke og sender det til denne samme adressen. Etter to år har Bob samlet en hel Bitcoin på denne adressen.
- Bakeren på hjørnet aksepterer Bitcoin-betalinger. Begeistret for å kunne bruke Bitcoin, går Bob for å kjøpe sin baguette i satoshier. For å betale, bruker han midlene låst med sin adresse. Bakeren hans vet nå at han eier en Bitcoin. Dette betydelige beløpet kunne tiltrekke seg misunnelse, og Bob risikerer potensielt et fysisk angrep i fremtiden.

Adressebruk på nytt lar en observatør lage en ubestridelig kobling mellom dine forskjellige UTXOer og noen ganger mellom din identitet og hele lommeboken din.
Dette er grunnen til at de fleste Bitcoin-lommebokprogramvare automatisk genererer en ny mottaksadresse når du klikker på "Motta"-knappen. For vanlige brukere er det ikke en stor ulempe å venne seg til å bruke nye adresser. Imidlertid, for en nettbedrift, en børs, eller en donasjonskampanje, kan denne begrensningen raskt bli uhåndterlig.
Det finnes mange løsninger for disse organisasjonene. Hver av dem har sine fordeler og ulemper, men til dags dato, og som vi vil se senere, skiller BIP47 seg virkelig ut fra de andre.

Dette problemet med adressebruk på nytt er langt fra ubetydelig i Bitcoin. Som du kan se i grafen nedenfor tatt fra oxt.me-nettstedet, er den totale adressen bruk på nytt-raten blant Bitcoin-brukere for øyeblikket 52%:
Graf fra OXT.me som viser utviklingen av den totale adressen bruk på nytt-raten på Bitcoin-nettverket.

![bilde](assets/2.webp)

Kreditt: OXT

Majoriteten av disse gjenbruken kommer fra børser, som, av effektivitets- og bekvemmelighetsgrunner, gjenbruker samme adresse mange ganger. Til dags dato ville BIP47 være den beste løsningen for å demme opp for dette fenomenet blant børser. Dette ville bidra til å redusere den totale adressen bruk på nytt-raten uten å forårsake for mye friksjon for disse enhetene.

Dette globale tiltaket over hele nettverket er spesielt relevant i dette tilfellet. Faktisk er ikke adressebruk på nytt bare et problem for personen som engasjerer seg i denne praksisen, men også for alle som gjennomfører transaksjoner med dem. Tap av personvern på Bitcoin oppfører seg som et virus, som sprer seg fra bruker til bruker. Å studere et globalt tiltak på alle nettverkstransaksjoner lar oss forstå omfanget av dette fenomenet.

## Prinsipper for BIP47 og PayNym.

BIP47 har som mål å tilby en enkel måte å motta flere betalinger uten adressebruk på nytt. Dets drift er basert på bruk av en gjenbrukbar betalingskode.

Slik kan flere avsendere sende flere betalinger til en enkelt gjenbrukbar betalingskode til en annen bruker, uten at mottakeren trenger å oppgi en ny tom adresse for hver ny transaksjon.

En bruker kan fritt dele sin betalingskode (på sosiale nettverk, på deres nettsted...) uten risiko for tap av personvern, i motsetning til en vanlig mottaksadresse eller en offentlig nøkkel.
For å gjennomføre en utveksling, må begge brukerne ha en Bitcoin-lommebok med en BIP47-implementering, som PayNym på Samourai Wallet eller Sparrow Wallet. Assosiasjonen av betalingskodene til de to brukerne vil etablere en hemmelig kanal mellom dem. For å ordentlig etablere denne kanalen, må avsenderen gjøre en transaksjon på Bitcoin-blockchainen: varslingstransaksjonen (jeg vil forklare mer om dette senere).

Assosiasjonen av betalingskodene til de to brukerne genererer delte hemmeligheter som selv genererer et stort antall unike Bitcoin mottaksadresser (nøyaktig 2^32). Så, i virkeligheten, blir betalingen med BIP47 ikke sendt til betalingskoden, men til helt normale adresser, avledet fra betalingskodene til de involverte partene.
Betalingskoden fungerer som en virtuell identifikator, avledet fra lommebokens seed. I HD-lommebokens avledningsstruktur er betalingskoden plassert på dybde 3, på lommebokkontoens nivå.
![bilde](assets/3.webp)

Dens avledningsformål er notert som 47' (0x8000002F) med henvisning til BIP47. For eksempel ville en avledningssti for en gjenbrukbar betalingskode være:

> m/47'/0'/0'/

For å gi deg en ide om hvordan en betalingskode ser ut, her er min:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Den kan også kodes som en QR-kode for å lette kommunikasjon:

![bilde](assets/4.webp)

Når det gjelder PayNym Bots, de robotene du ser på Twitter, er de rett og slett visuelle representasjoner av din betalingskode, skapt av Samourai Wallet. De genereres ved hjelp av en hash-funksjon, som gjør dem nesten unike. Her er min med dens identifikator:

> +throbbingpond8B1

![bilde](assets/5.webp)

Disse Bots har ingen reell teknisk nytte. I stedet letter de interaksjoner mellom brukere ved å skape en virtuell visuell identitet.

For brukeren er prosessen med å gjøre en BIP47-betaling med PayNym-implementeringen ekstremt enkel. La oss forestille oss at Alice ønsker å sende betalinger til Bob:

1. Bob deler sin QR-kode eller direkte sin gjenbrukbare betalingskode. Han kan plassere den på sin nettside, på sine ulike offentlige sosiale nettverk, eller sende den til Alice gjennom et annet kommunikasjonsmiddel.
2. Alice åpner sin Samourai- eller Sparrow-programvare og skanner eller limer inn Bobs betalingskode.
3. Alice kobler sin PayNym med Bobs ("Follow" på engelsk). Denne operasjonen gjøres off-chain og forblir helt gratis.

4. Alice kobler sin PayNym med Bobs ("Connect" på engelsk). Denne operasjonen gjøres "on-chain". Alice må betale transaksjonsgruvegebyrene samt et fast gebyr på 15 000 sats for tjenesten på Samourai. Tjenestegebyrene er frafalt på Sparrow. Dette trinnet er det vi kaller varslingstransaksjonen.

5. Når varslingstransaksjonen er bekreftet, kan Alice opprette en BIP47-betalings transaksjon til Bob. Hennes lommebok vil automatisk generere en ny blank mottaksadresse som kun Bob har den private nøkkelen til.

Å utføre varslingstransaksjonen, det vil si å koble sin PayNym, er et obligatorisk forhåndskrav for å gjøre BIP47-betalinger. Men, når dette er gjort, kan avsenderen gjøre flere betalinger til mottakeren (nøyaktig 2^32) uten å måtte utføre en ny varslingstransaksjon.

Du har kanskje lagt merke til at det er to forskjellige operasjoner for å koble PayNyms sammen: "follow" og "connect". Tilkoblingsoperasjonen ("connect") tilsvarer BIP47-varslingstransaksjonen, som rett og slett er en Bitcoin-transaksjon med visse opplysninger overført gjennom en OP_RETURN-utgang. Således hjelper den med å etablere kryptert kommunikasjon mellom de to brukerne for å produsere de delte hemmelighetene som er nødvendige for å generere nye blanke mottaksadresser.

På den annen side tillater koblingsoperasjonen ("follow" eller "relier") en kobling på Soroban, et kryptert kommunikasjonsprotokoll basert på Tor, spesielt utviklet av Samourai-teamene.

For å oppsummere:
- Å koble to PayNyms ("følge") er helt gratis. Det hjelper med å etablere kryptert kommunikasjon utenfor kjeden, spesielt for bruk av Samourais samarbeidende transaksjonsverktøy (Stowaway eller StonewallX2). Denne operasjonen er spesifikk for PayNym og er ikke beskrevet i BIP47.
- Å koble sammen to PayNyms medfører en kostnad. Dette innebærer å utføre varslingstransaksjonen for å initiere tilkoblingen. Kostnaden består av eventuelle tjenestegebyrer, transaksjonsminingsgebyrer og 546 sats sendt til mottakerens varslingadresse for å varsle dem om tunnelåpningen. Denne operasjonen er relatert til BIP47. Når dette er fullført, kan avsenderen gjøre flere BIP47-betalinger til mottakeren.

For å koble sammen to PayNyms, må de allerede være koblet.

## Veiledninger: Bruk av PayNym.

Nå som vi har sett teorien, la oss studere praksisen sammen. Ideen med veiledningene nedenfor er å koble min PayNym på min Sparrow-lommebok med min PayNym på min Samourai-lommebok. Den første veiledningen viser deg hvordan du gjør en transaksjon ved hjelp av den gjenbrukbare betalingskoden fra Samourai til Sparrow, og den andre veiledningen beskriver samme mekanisme fra Sparrow til Samourai.

> Jeg utførte disse veiledningene på Testnet. Dette er ikke ekte bitcoins.

### Bygge en BIP47-transaksjon med Samourai Wallet.

For å starte trenger du selvfølgelig Samourai Wallet-applikasjonen. Du kan laste den ned direkte fra Google Play Store eller med APK-filen som er tilgjengelig på det offisielle Samourai-nettstedet.

Når lommeboken er initialisert, hvis du ikke allerede har gjort det, be om din PayNym ved å klikke på pluss (+) nederst til høyre, deretter på "PayNym".

Det første steget for å gjøre en BIP47-betaling er å hente den gjenbrukbare betalingskoden fra mottakeren vår. Deretter vil vi kunne koble oss til dem og deretter koble:

![video](assets/6.mp4)

Når varslingstransaksjonen er bekreftet, kan jeg sende flere betalinger til mottakeren min. Hver transaksjon vil automatisk bli gjort med en ny blank adresse som mottakeren har nøklene til. Mottakeren trenger ikke å gjøre noe, alt beregnes på min side.

Slik gjør du en BIP47-transaksjon på Samourai Wallet:

![video](assets/7.mp4)

### Bygge en BIP47-transaksjon med Sparrow Wallet.

Akkurat som med Samourai, trenger du selvfølgelig å ha Sparrow-programvaren. Denne er tilgjengelig på datamaskinen din. Du kan laste den ned fra deres [offisielle nettsted](https://sparrowwallet.com/).

Sørg for å verifisere utviklerens signatur og integriteten til programvaren du laster ned før du installerer den på maskinen din.

Opprett en lommebok og be om din PayNym ved å klikke på "Vis PayNym" fra "Verktøy"-menyen i toppbaren:

![image](assets/8.webp)

Deretter må du koble og koble din PayNym med mottakerens. For å gjøre dette, skriv inn deres gjenbrukbare betalingskode i "Finn kontakt"-vinduet, følg dem, og utfør deretter varslingstransaksjonen ved å klikke på "Koble kontakt":

![image](assets/9.webp)

Når varslingstransaksjonen er bekreftet, kan du sende betalinger til den gjenbrukbare betalingskoden. Slik gjør du det:

![video](assets/10.mp4)

Nå som vi har vært i stand til å studere den praktiske aspekten av PayNym-implementeringen av BIP47, la oss se hvordan alle disse mekanismene fungerer og hvilke kryptografiske metoder som brukes.
For å studere mekanismene til BIP47, er det essensielt å forstå strukturen til den hierarkiske deterministiske (HD) lommeboken, mekanismene for å avlede barne nøkkelpar, samt prinsippene for elliptisk kurvekryptografi. Heldigvis kan du finne all nødvendig informasjon for å forstå denne delen på bloggen min:
- [Forståelse av avledningsveiene til en Bitcoin-lommebok](https://www.pandul.fr/post/comprendre-les-chemins-de-d%C3%A9rivation-d-un-portefeuille-bitcoin)

- [Bitcoin-lommeboken - utdrag fra e-boken Bitcoin Democratized 2](https://www.pandul.fr/post/le-portefeuille-bitcoin-extrait-ebook-bitcoin-d%C3%A9mocratis%C3%A9-2)

### Den gjenbrukbare betalingskoden.

Som forklart i den andre delen av denne artikkelen, er den gjenbrukbare betalingskoden lokalisert på dybde tre av HD-lommeboken. Den kan på en måte sammenlignes med en xpub, både i sin plassering og struktur, samt i sin rolle.

Her er de forskjellige delene som utgjør en 80-byte betalingskode:

- Byte 0: Versjonen. Hvis du bruker den første versjonen av BIP47, vil denne byten være lik 0x01.

- Byte 1: Bitfeltet. Dette området er reservert for å gi ytterligere indikasjoner i tilfelle spesifikk bruk. Hvis du bare bruker PayNym, vil denne byten være lik 0x00.

- Byte 2: Y-pariteten. Denne byten indikerer 0x02 eller 0x03 avhengig av pariteten (partall eller oddetall) av verdien til y-koordinaten til vår offentlige nøkkel. For mer informasjon om denne praksisen, vennligst les trinn 1 i "adresseavlednings"-seksjonen av denne artikkelen.

- Fra byte 3 til byte 34: X-verdien. Disse bytene indikerer x-koordinaten til vår offentlige nøkkel. Sammenslåingen av x og y-pariteten gir oss vår komprimerte offentlige nøkkel.

- Fra byte 35 til byte 66: Kjedekoden. Dette området er reservert for kjedekoden assosiert med den nevnte offentlige nøkkelen.

- Fra byte 67 til byte 79: Polstring. Dette området er reservert for mulige fremtidige utviklinger. For versjon 1, fyller vi det ganske enkelt med nuller for å nå 80 bytes, som er størrelsen på dataene for en OP_RETURN-utgang.

Her er den heksadesimale representasjonen av min gjenbrukbare betalingskode, presentert i den forrige seksjonen, med farger som tilsvarer bytene presentert ovenfor:
Videre må du også legge til prefiksbyten "P" for å raskt identifisere at vi har med en betalingskode å gjøre. Denne byten er 0x47.

> 0x47010002a0716529bae6b36c5c9aa518a52f9c828b46ad8d907747f0d09dcd4d9a39e97c3c5f37c470c390d842f364086362f6122f412e2b0c7e7fc6e32287e364a7a36a00000000000000000000000000

Til slutt beregner vi sjekksummen av denne betalingskoden ved hjelp av HASH256, som betyr dobbel hashing med SHA256-funksjonen. Vi henter de første fire bytene av dette sammendraget og konkatenerer dem på slutten (i rosa).
Betalingskoden er klar, nå trenger vi bare å konvertere den til Base 58:

> PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qDudE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5

Som du kan se, ligner denne konstruksjonen sterkt på strukturen til en utvidet offentlig nøkkel av typen "xpub".

I denne prosessen for å få vår betalingskode, brukte vi en komprimert offentlig nøkkel og en kjedekode. Disse to elementene er resultatet av en deterministisk og hierarkisk derivasjon fra lommebokfrøet, som følger denne derivasjonsstien: m/47'/0'/0'/
Konkret, for å få den offentlige nøkkelen og kjedekoden til den gjenbrukbare betalingskoden, vil vi beregne den master private nøkkelen fra frøet, deretter derivere et barnepar med indeksen 47 + 2^31 (hardened derivasjon). Deretter derivere vi to flere barnepar med indeksen 2^31 (hardened derivasjon).

> Hvis du vil lære mer om derivasjon av barnenøkkelpar innenfor en hierarkisk deterministisk Bitcoin-lommebok, anbefaler jeg å ta CRYPTO301.

### Den kryptografiske metoden: Elliptic Curve Diffie-Hellman nøkkelutveksling (ECDH).

Den kryptografiske metoden som brukes i kjernen av BIP47 er ECDH (Elliptic-Curve Diffie-Hellman). Denne protokollen er en variant av den klassiske Diffie-Hellman nøkkelutvekslingen.

Diffie-Hellman, i sin første versjon, er et nøkkelavtaleprotokoll presentert i 1976 som lar to parter, hver med et par av offentlige og private nøkler, bestemme et delt hemmelig ved å utveksle informasjon over en usikker kommunikasjonskanal.

![bilde](assets/11.webp)

Dette delte hemmeliget (den røde nøkkelen) kan deretter brukes til andre oppgaver. Typisk kan dette delte hemmeliget brukes til å kryptere og dekryptere kommunikasjon over et usikkert nettverk:

![bilde](assets/12.webp)

For å oppnå denne utvekslingen, bruker Diffie-Hellman modulær aritmetikk for å beregne det delte hemmeliget. Her er en forenklet forklaring på hvordan det fungerer:

- Alice og Bob blir enige om en felles farge, i dette tilfellet, gul. Denne fargen er kjent for alle. Det er offentlig informasjon.

- Alice velger en hemmelig farge, i dette tilfellet, rød. Hun blander de to fargene, noe som resulterer i oransje.

- Bob velger en hemmelig farge, i dette tilfellet, teal blå. Han blander de to fargene, noe som resulterer i himmelblå.

- Alice og Bob kan utveksle fargene de oppnådde: oransje og himmelblå. Denne utvekslingen kan skje over et usikkert nettverk og kan observeres av angripere.

- Alice blander den himmelblå fargen hun mottok fra Bob med sin hemmelige farge (rød). Hun oppnår brun.

- Bob blander den oransje fargen han mottok fra Alice med sin hemmelige farge (teal blå). Han oppnår også brun.

![bilde](assets/13.webp)
> z er lik A opphøyd i b modulo p:
> z = A^b % p

- Som en påminnelse, A = g^a % p. Derfor:

  > z = A^b % p
  > z = (g^a)^b % p
  >
  > I henhold til reglene for eksponentiering:
  >
  > (x^n)^m = x^nm
  >
  > Derfor:
  >
  > z = g^ab % p

I denne forenklingen representerer den brune fargen hemmeligheten delt mellom Alice og Bob. Det bør forestilles at det i virkeligheten er umulig for angriperen å skille de oransje og himmelblå fargene for å hente ut Alice eller Bobs hemmelige farger.

Nå, la oss studere dens faktiske funksjon. Ved første øyekast kan Diffie-Hellman virke kompleks å forstå. I virkeligheten er driftsprinsippet nesten barnslig enkelt. Før vi detaljerer mekanismene, vil jeg raskt minne deg på to matematiske konsepter som vi vil trenge (og som for øvrig også brukes i mange andre kryptografiske metoder).

1. Et primtall er et naturlig tall som kun har to divisorer: 1 og seg selv. For eksempel er tallet 7 primt fordi det kun kan deles av 1 og 7 (seg selv). På den andre siden er tallet 8 ikke primt fordi det kan deles av 1, 2, 4, og 8. Det har derfor ikke kun to divisorer, men fire hele og positive divisorer.

2. "Modulo" (betegnet "mod" eller "%") er en matematisk operasjon som lar to heltall returnere resten av den euklidiske divisjonen av det første tallet med det andre tallet. For eksempel er 16 mod 5 lik 1.

Nøkkelutvekslingen mellom Alice og Bob med Diffie-Hellman fungerer som følger:

- Alice og Bob bestemmer to felles tall: p og g. p er et primtall. Jo større dette tallet p er, desto sikrere vil Diffie-Hellman være. g er en primitiv rot av p. Disse to tallene kan kommuniseres i klartekst over et usikret nettverk, de er ekvivalenter til den gule fargen i forenklingen ovenfor. Alice og Bob trenger bare å ha nøyaktig de samme verdiene for p og g.

- Når parameterne er valgt, bestemmer Alice og Bob hver sitt hemmelige tilfeldige tall på egen hånd. Det tilfeldige tallet som Alice får, er navngitt a (ekvivalent til den røde fargen) og det tilfeldige tallet som Bob får, er navngitt b (ekvivalent til den turkise fargen). Disse to tallene må forbli hemmelige.

- I stedet for å utveksle disse tallene a og b, vil hver part beregne A (stor bokstav) og B (stor bokstav) slik at:

> A er lik g opphøyd i kraften av a modulo p:
> A = g^a % p

> B er lik g opphøyd i kraften av b modulo p:
> B = g^b % p

- Disse tallene A (ekvivalent til den oransje fargen) og B (ekvivalent til den himmelblå fargen) vil bli utvekslet mellom de to partene. Utvekslingen kan gjøres i klartekst over et usikret nettverk.

- Alice, som nå kjenner B, vil beregne verdien av z slik at:

> z er lik B opphøyd i kraften av a modulo p:
> z = B^a % p

- Som en påminnelse, B = g^b % p. Derfor:

  > z = B^a % p
  > z = (g^b)^a % p
  >
  > I henhold til reglene for eksponentiering:
  >
  > (x^n)^m = x^nm
  >
  > Derfor:
  >
  > z = g^ba % p
> z er lik A opphøyd i b modulo p:
> z = A^b % p
>
> Derfor:
>
> z = (g^a)^b % p
> z = g^ab % p
> z = g^ba % p

Takket være distributiviteten til modulo-operatoren, finner Alice og Bob nøyaktig den samme verdien for z. Dette tallet representerer deres delte hemmelighet, som tilsvarer fargen brun i den tidligere forklaringen. De kan bruke denne delte hemmeligheten til å kryptere kommunikasjon mellom dem på et usikkert nettverk.

![Diffie-Hellman teknisk operasjonsdiagram](assets/14.webp)

En angriper som er i besittelse av p, g, A, og B vil ikke kunne beregne a, b, eller z. Å utføre denne operasjonen ville kreve å reversere eksponentiering, noe som er umulig å gjøre annet enn ved å prøve alle muligheter en etter en siden vi jobber med et endelig felt. Dette ville være tilsvarende å beregne den diskrete logaritmen, som er det motsatte av eksponentiering i en syklisk endelig gruppe.

Derfor, så lenge vi velger tilstrekkelig store verdier for a, b, og p, er Diffie-Hellman sikker. Vanligvis, med parametere på 2,048 bits (et tall med 600 sifre i desimal), ville det være upraktisk å teste alle muligheter for a og b. Til dags dato, med tall av denne størrelsen, anses algoritmen for å være sikker.

Dette er nettopp hvor hovedulempen med Diffie-Hellman-protokollen ligger. For å være sikker, må algoritmen bruke store tall. Som et resultat, foretrekkes nå ECDH-algoritmen, som er en variant av Diffie-Hellman som bruker en algebraisk kurve, spesifikt en elliptisk kurve. Dette lar oss jobbe med mye mindre tall mens vi opprettholder tilsvarende sikkerhet, og dermed reduserer de beregningsmessige og lagringsressursene som kreves.

Det generelle prinsippet for algoritmen forblir det samme. Imidlertid, i stedet for å bruke et tilfeldig tall a og et tall A beregnet fra a ved hjelp av modulær eksponentiering, vil vi bruke et par nøkler etablert på en elliptisk kurve. I stedet for å stole på distributiviteten til modulo-operatoren, vil vi bruke gruppeloven på elliptiske kurver, spesifikt assosiativiteten av denne loven.
Hvis du ikke har kunnskap om hvordan private og offentlige nøkler fungerer på en elliptisk kurve, vil jeg forklare grunnleggende om denne metoden i de første seks delene av denne artikkelen.

For å oppsummere grovt, er en privat nøkkel et tilfeldig tall mellom 1 og n-1 (hvor n er kurvens orden), og en offentlig nøkkel er et unikt punkt på kurven bestemt av den private nøkkelen gjennom punktaddisjon og dobling fra generatorenpunktet, som følger:

> K = k·G

Hvor K er den offentlige nøkkelen, k er den private nøkkelen, og G er generatorenpunktet.

En av egenskapene til dette nøkkelparet er at det er veldig enkelt å bestemme K hvis du kjenner k og G, men det er for øyeblikket umulig å bestemme k hvis du kjenner K og G. Det er en enveisfunksjon.

Med andre ord, du kan enkelt beregne den offentlige nøkkelen hvis du kjenner den private nøkkelen, men det er umulig å beregne den private nøkkelen hvis du kjenner den offentlige nøkkelen. Denne sikkerheten er igjen basert på umuligheten av å beregne den diskrete logaritmen.

Vi vil bruke denne egenskapen til å tilpasse vår Diffie-Hellman-algoritme. Således er driftsprinsippet for ECDH som følger:

- Alice og Bob blir enige om en kryptografisk sikker elliptisk kurve og dens parametere. Denne informasjonen er offentlig.
- Alice genererer et tilfeldig tall ka, som vil være hennes private nøkkel. Denne private nøkkelen må forbli hemmelig. Hun bestemmer sin offentlige nøkkel Ka ved å legge til og doble punkter på den valgte elliptiske kurven.
> Ka = ka·G

- Bob genererer også et tilfeldig tall kb, som vil være hans private nøkkel. Han beregner den tilknyttede offentlige nøkkelen Kb.

> Kb = kb·G

- Alice og Bob utveksler sine offentlige nøkler Ka og Kb over et usikret offentlig nettverk.

- Alice beregner et punkt (x, y) på kurven ved å anvende sin private nøkkel ka på Bobs offentlige nøkkel Kb.

> (x, y) = ka·Kb

- Bob beregner et punkt (x, y) på kurven ved å anvende sin private nøkkel kb på Alices offentlige nøkkel Ka.

> (x, y) = kb·Ka

- Alice og Bob oppnår det samme punktet på den elliptiske kurven. Det delte hemmeligheten vil være x-koordinaten til dette punktet.

De oppnår den samme delte hemmeligheten fordi:

> (x, y) = ka·Kb = ka·kb·G = kb·ka·G = kb·Ka

En potensiell angriper som observerer det usikrede offentlige nettverket kan kun oppnå de offentlige nøklene til hver part og de valgte kurveparametrene. Som forklart tidligere, alene tillater ikke disse to stykkene informasjon å bestemme de private nøklene, så angriperen kan ikke få tilgang til hemmeligheten.
ECDH er en algoritme som tillater nøkkelutveksling. Den brukes ofte sammen med andre kryptografiske metoder for å definere en protokoll. For eksempel, ECDH brukes i kjernen av TLS (Transport Layer Security), en krypterings- og autentiseringsprotokoll brukt for internettets transportlag. TLS bruker ECDHE for nøkkelutveksling, en variant av ECDH hvor nøklene er efemere for å gi vedvarende konfidensialitet. I tillegg til ECDHE, bruker TLS også en autentiseringsalgoritme som ECDSA, en krypteringsalgoritme som AES, og en hash-funksjon som SHA256.

TLS definerer "s" i "https" og det lille låsikonet du ser i nettleseren din øverst til venstre, som garanterer kryptert kommunikasjon. Så, du bruker for øyeblikket ECDH ved å lese denne artikkelen, og du bruker det sannsynligvis daglig uten å innse det.

### Varslingstransaksjonen.

Som vi oppdaget i forrige seksjon, er ECDH en variant av Diffie-Hellman-utvekslingen som involverer nøkkelpar etablert på en elliptisk kurve. Heldigvis har vi mange nøkkelpar som møter denne standarden i våre Bitcoin-lommebøker!

Ideen er å bruke nøkkelparene fra de hierarkiske deterministiske Bitcoin-lommebøkene til begge parter for å etablere delte og efemere hemmeligheter mellom dem. Innen BIP47, brukes ECDHE (Elliptic Curve Diffie-Hellman Ephemeral) i stedet.

ECDHE brukes opprinnelig i BIP47 for å overføre avsenderens betalingskode til mottakeren. Dette er den berømte varslingstransaksjonen. For at BIP47 skal kunne brukes, må begge parter (avsenderen som sender betalinger og mottakeren som mottar betalinger) være klar over hverandres betalingskode. Dette er nødvendig for å utlede de efemere offentlige nøklene og derfor de dedikerte mottaksadressene.
Før denne utvekslingen, vet avsenderen logisk sett allerede mottakerens betalingskode siden de kunne ha fått den off-chain, for eksempel fra deres nettside eller sosiale medier. Imidlertid, mottakeren vet ikke nødvendigvis avsenderens betalingskode. Den må overføres til dem, ellers vil de ikke være i stand til å utlede sine efemere nøkler og derfor vil de ikke kunne vite hvor deres bitcoins er og låse opp sine midler. Den kunne bli overført til dem off-chain, ved bruk av et annet kommunikasjonssystem, men dette ville utgjøre et problem hvis lommeboken gjenopprettes fra frøet. Faktisk, som jeg allerede har nevnt, er BIP47-adresser ikke utledet fra mottakerens frø (ellers ville det være bedre å bruke en av deres xpubs direkte), men er resultatet av en beregning som involverer både mottakerens betalingskode og avsenderens betalingskode. Derfor, hvis mottakeren mister sin lommebok og prøver å gjenopprette den fra sitt frø, vil de nødvendigvis måtte ha alle betalingskodene til folkene som har sendt dem bitcoins via BIP47.

Det ville være mulig å bruke BIP47 uten denne varslingstransaksjonen, men hver bruker ville trenge å sikkerhetskopiere betalingskodene til sine jevnaldrende. Denne situasjonen vil forbli uhåndterlig til en enkel og robust måte å opprette, lagre og oppdatere disse sikkerhetskopiene er funnet. Varslingstransaksjonen er derfor nesten obligatorisk i den nåværende tilstanden av ting.

I tillegg til sin rolle med å sikkerhetskopiere betalingskoder, som navnet antyder, fungerer denne transaksjonen også som en varsling til mottakeren. Den informerer deres klient om at en tunnel nettopp har blitt åpnet.

Før jeg forklarer mer detaljert den tekniske funksjonen til varslingstransaksjonen, vil jeg gjerne snakke litt om personvernmodellen. Faktisk, BIP47 personvernmodellen rettferdiggjør visse forholdsregler tatt når man konstruerer denne innledende transaksjonen.

Betalingskoden i seg selv utgjør ikke direkte en risiko for personvernet. I motsetning til den klassiske Bitcoin-modellen, som tillater å bryte informasjonsflyten mellom brukerens identitet og transaksjoner, spesielt ved å holde de offentlige nøklene anonyme, kan betalingskoden direkte assosieres med en identitet. Dette er ikke obligatorisk, men denne koblingen er ikke farlig.

Faktisk, betalingskoden utleder ikke direkte adressene som brukes til å motta BIP47-betalinger. I stedet, adressene blir oppnådd ved å anvende ECDHE mellom barnenøkler av betalingskodene til begge parter.

Derfor utgjør en betalingskode alene ikke en direkte risiko for personvernet siden bare varslingadressen er utledet fra den. Noe informasjon kan utledes fra den, men normalt kan man ikke vite med hvem du handler.

Det er derfor avgjørende å opprettholde en streng separasjon mellom brukernes betalingskoder. I denne forbindelse er det innledende kommunikasjonstrinnet av koden et kritisk øyeblikk for betalingspersonvernet, og likevel er det obligatorisk for den riktige funksjonen av protokollen. Hvis en av betalingskodene kan offentlig hentes (for eksempel fra en nettside), bør den andre koden, dvs. avsenderens kode, ikke assosieres med den første.

For eksempel, la oss forestille oss at jeg ønsker å gjøre en donasjon med BIP47 til en fredelig protestbevegelse i Canada:

- Denne organisasjonen har publisert sin betalingskode direkte på sin nettside eller sosiale medieplattformer.
- Denne koden er derfor assosiert med bevegelsen.

- Jeg henter denne betalingskoden.

- Før jeg kan sende dem en transaksjon, må jeg sørge for at de er klar over min personlige betalingskode, som også er assosiert med min identitet siden jeg bruker den til å motta transaksjoner fra mine sosiale nettverk.

Hvordan kan jeg overføre den til dem? Hvis jeg sender den til dem ved hjelp av et konvensjonelt kommunikasjonsmiddel, kan informasjonen lekke, og jeg kan bli identifisert som en person som støtter fredelige bevegelser.
Varslingstransaksjonen er definitivt ikke den eneste løsningen for å hemmelig overføre avsenderens betalingskode, men den oppfyller for øyeblikket denne rollen perfekt ved å anvende flere lag med sikkerhet.
I diagrammet nedenfor representerer de røde linjene øyeblikket når informasjonsflyten må brytes, og de svarte pilene representerer de ubestridelige koblingene som kan gjøres av en ekstern observatør:

![Privacy model diagram for reusable payment code](assets/15.webp)

I virkeligheten, for den klassiske personvernmodellen til Bitcoin, er det ofte vanskelig å fullstendig bryte informasjonsflyten mellom nøkkelparet og brukeren, spesielt ved fjerntransaksjoner. For eksempel, i tilfellet med en donasjonskampanje, vil mottakeren være nødt til å avsløre en adresse eller offentlig nøkkel på deres nettsted eller sosiale medieplattformer. Riktig bruk av BIP47, dvs. med varslingstransaksjonen, løser dette problemet gjennom ECDHE og krypteringslaget som vi vil studere.

Åpenbart blir den klassiske personvernmodellen til Bitcoin fortsatt observert på nivået av de flyktige offentlige nøklene som er avledet fra sammenslåingen av de to betalingskodene. De to modellene er gjensidig avhengige. Jeg ønsker bare å fremheve her at, i motsetning til den klassiske bruken av en offentlig nøkkel for å motta bitcoins, kan betalingskoden assosieres med en identitet fordi informasjonen "Bob gjør en transaksjon med Alice" brytes på et annet øyeblikk. Betalingskoden brukes til å generere betalingsadresser, men ved kun å observere blockchain, er det umulig å assosiere en BIP47 betalingstransaksjon med betalingskodene som ble brukt for å gjøre den.

### Konstruksjon av varslingstransaksjonen.

Nå, la oss se hvordan denne varslingstransaksjonen fungerer. La oss forestille oss at Alice ønsker å sende midler til Bob ved bruk av BIP47. I mitt eksempel opptrer Alice som avsender og Bob som mottaker. Bob har allerede publisert sin betalingskode på sitt nettsted, så Alice er allerede klar over Bobs betalingskode.

1. Alice beregner et delt hemmelig med ECDH:

- Hun velger et par nøkler fra sin HD-lommebok som er lokalisert på en annen gren enn hennes betalingskode. Merk at dette paret ikke bør være lett assosiert med Alices varslingadresse eller Alices identitet (se forrige seksjon).
- Alice velger den private nøkkelen fra dette paret. Vi vil kalle den "a" (liten bokstav).

> a

- Alice henter den offentlige nøkkelen assosiert med Bobs varslingadresse. Denne nøkkelen er det første barnet avledet fra Bobs betalingskode (indeks 0). Vi vil kalle denne offentlige nøkkelen "B" (stor bokstav). Den private nøkkelen assosiert med denne offentlige nøkkelen kalles "b" (liten bokstav). "B" er bestemt ved punktaddisjon og dobling på elliptisk kurve fra "G" (generatorenpunktet) med "b" (den private nøkkelen).

> B = b·G

- Alice beregner et hemmelig punkt "S" (stor bokstav) på den elliptiske kurven ved punktaddisjon og dobling, ved å anvende sin private nøkkel "a" på Bobs offentlige nøkkel "B".

> S = a·B

- Alice beregner blendingsfaktoren "f" som vil bli brukt til å kryptere hennes betalingskode. For å gjøre dette, vil hun generere et pseudo-tilfeldig tall ved hjelp av HMAC-SHA512-funksjonen. Som det andre inndata til denne funksjonen, bruker hun en verdi som kun Bob vil kunne hente: (x), som er x-koordinaten til det tidligere beregnede hemmelige punktet. Det første inndata er (o), som er UTXO forbrukt som inndata til denne transaksjonen (utpoint).

> f = HMAC-SHA512(o, x)

2. Alice konverterer sin personlige betalingskode til base 2 (binær).
3. Hun bruker denne blendingsfaktoren som en nøkkel for å utføre symmetrisk kryptering på nyttelasten av betalingskoden sin. Krypteringsalgoritmen som brukes er simpelthen XOR. Operasjonen som utføres er lik Vernam-chifferet, også kjent som "engangsblokk":
- Alice deler først sin blendingsfaktor i to deler: de første 32 bytene kalles "f1" og de siste 32 bytene kalles "f2". Så vi har:

> f = f1 || f2

- Alice beregner chifferteksten (x') av x-koordinaten til den offentlige nøkkelen (x) til betalingskoden sin, og beregner separat chifferteksten (c') til hennes kjedekode (c). "f1" og "f2" fungerer som krypteringsnøkler, og XOR-operasjonen brukes.

> x' = x XOR f1
>
> c' = c XOR f2

- Alice erstatter de faktiske verdiene av den offentlige nøkkelens absisse (x) og kjedekoden (c) i betalingskoden sin med de krypterte verdiene (x') og (c').

Før vi fortsetter med den tekniske beskrivelsen av denne varslingstransaksjonen, la oss ta et øyeblikk for å diskutere XOR-operasjonen. XOR er en bitvis logisk operator basert på boolsk algebra. Gitt to bit-operander, returnerer den 1 hvis de tilsvarende bitene er forskjellige, og den returnerer 0 hvis de tilsvarende bitene er like. Her er sannhetstabellen for XOR basert på verdiene til operandene D og E:

| D   | E   | D XOR E |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

For eksempel:

> 0110 XOR 1110 = 1000

Eller:

> 010011 XOR 110110 = 100101

Med ECDH er bruken av XOR som et krypteringslag spesielt sammenhengende. Først, takket være denne operatoren, er krypteringen symmetrisk. Dette lar mottakeren dekryptere betalingskoden med samme nøkkel som ble brukt for kryptering. Krypterings- og dekrypteringsnøkkelen beregnes fra det delte hemmelige ved hjelp av ECDH.

Denne symmetrien er muliggjort av kommutativitets- og assosiativitetsegenskapene til XOR-operatøren:

- Andre egenskaper:
  -> D ⊕ D = 0
  -> D ⊕ 0 = D

- Kommutativitet:
  D ⊕ E = E ⊕ D

- Assosiativitet:
  D ⊕ (E ⊕ Z) = (D ⊕ E) ⊕ Z = D ⊕ E ⊕ Z

- Symmetri:
  Hvis: D ⊕ E = L
  Da: D ⊕ L = D ⊕ (D ⊕ E) = D ⊕ D ⊕ E = 0 ⊕ E = E
  -> D ⊕ L = E
Videre er denne krypteringsmetoden veldig lik Vernam-chifferet (One-Time Pad), den eneste krypteringsalgoritmen kjent til dags dato som har ubetinget (eller absolutt) sikkerhet. For at Vernam-chifferet skal ha denne egenskapen, må krypteringsnøkkelen være fullstendig tilfeldig, være av samme størrelse som meldingen, og kun brukes én gang. I krypteringsmetoden som brukes her for BIP47, er nøkkelen faktisk samme størrelse som meldingen, blendingsfaktoren er nøyaktig samme størrelse som sammenkjedningen av x-koordinaten til den offentlige nøkkelen med betalingskodekjedekoden. Denne krypteringsnøkkelen brukes faktisk bare én gang. Imidlertid er ikke denne nøkkelen avledet fra en perfekt tilfeldig kilde ettersom den er en HMAC. Den er heller pseudotilfeldig. Derfor er det ikke et Vernam-chiffer, men metoden er lik.

La oss gå tilbake til vår konstruksjon av varslingstransaksjonen:

4. Alice har nå sin betalingskode med en kryptert nyttelast. Hun vil konstruere og kringkaste en transaksjon som involverer hennes offentlige nøkkel "A" som inndata, en utgang til Bobs varslingadresse, og en OP_RETURN-utgang bestående av hennes betalingskode med den krypterte nyttelasten. Denne transaksjonen er varslingstransaksjonen.

OP_RETURN er en Opcode, som er et skript som markerer en Bitcoin-transaksjonsutgang som ugyldig. I dag brukes den til å kringkaste eller forankre informasjon på Bitcoin-blockchainen. Den kan lagre opptil 80 bytes med data som blir registrert på kjeden og derfor synlige for alle andre brukere.

Som vi så i forrige avsnitt, brukes Diffie-Hellman til å generere en delt hemmelighet mellom to brukere som kommuniserer over et usikkert nettverk, potensielt observert av angripere. I BIP47 brukes ECDH for å kommunisere på Bitcoin-nettverket, som av natur er et transparent kommunikasjonsnettverk observert av mange angripere. Den delte hemmeligheten beregnet gjennom Diffie-Hellman nøkkelutveksling på den elliptiske kurven brukes deretter til å kryptere den hemmelige informasjonen som skal overføres: avsenderens (Alices) betalingskode.

Her er et diagram hentet fra BIP47 som illustrerer det vi nettopp beskrev:

![Diagram Alice sender sin maskerte betalingskode til Bobs varslingadresse](assets/16.webp)

Kreditt: Gjenbrukbare Betalingskoder for Hierarkiske Deterministiske Lommebøker, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Hvis vi matcher dette diagrammet med det jeg beskrev tidligere:

- "Wallet Priv-Key" på Alices side tilsvarer: a.

- "Child Pub-Key 0" på Bobs side tilsvarer: B.
- "Notification Shared Secret" tilsvarer: f.
- "Masked Payment Code" tilsvarer den krypterte betalingskoden, dvs. med den krypterte nyttelasten: x' og c'.

- "Notification Transaction" er transaksjonen som inneholder OP_RETURN.

La oss oppsummere stegene vi nettopp gikk gjennom for å utføre en varslingstransaksjon:

- Alice henter Bobs betalingskode og varslingadresse.

- Alice velger en UTXO som tilhører henne i hennes HD-lommebok med det tilsvarende nøkkelparet.

- Hun beregner et hemmelig punkt på den elliptiske kurven ved hjelp av ECDH.

- Hun bruker dette hemmelige punktet til å beregne en HMAC, som er blendingsfaktoren.

- Hun bruker denne blendingsfaktoren til å kryptere nyttelasten av sin personlige betalingskode.

- Hun bruker en OP_RETURN-transaksjonsutgang for å overføre den maskerte betalingskoden til Bob.

For å bedre forstå hvordan det fungerer, spesielt bruken av OP_RETURN, la oss studere en ekte varslingstransaksjon sammen. Jeg utførte en transaksjon av denne typen på Testnet, som du kan finne ved å klikke her:
Ved å observere denne transaksjonen, kan vi allerede se at den har en enkelt inngang og 4 utganger:

- Den første utgangen er OP_RETURN som inneholder min maskerte betalingskode.

- Den andre utgangen på 546 sats peker til mottakerens varselsadresse.

- Den tredje utgangen på 15 000 sats representerer tjenesteavgiften, ettersom jeg brukte Samourai Wallet for å konstruere denne transaksjonen.

- Den fjerde utgangen på to millioner sats representerer vekslepengene, dvs. den gjenværende differansen fra min inngang som går tilbake til en annen adresse som tilhører meg.

Det mest interessante å studere er åpenbart utgang 0 som bruker OP_RETURN. La oss ta en nærmere titt på hva den inneholder:

Vi oppdager det heksadesimale skriptet til utgangen:

> 6a4c50010002b13b2911719409d704ecc69f74fa315a6cb20fdd6ee39bc9874667703d67b164927b0e88f89f3f8b963549eab2533b5d7ed481a3bea7e953b546b4e91b6f50d800000000000000000000000000

I dette skriptet kan vi bryte ned flere deler:
Blant opcodes, kan vi gjenkjenne 0x6a som refererer til OP_RETURN og 0x4c som refererer til OP_PUSHDATA1. Byten som følger denne opcode indikerer størrelsen på nyttelasten som følger. Den indikerer 0x50, som er 80 bytes.

Deretter kommer betalingskoden med den krypterte nyttelasten.

Her er min betalingskode brukt i denne transaksjonen:

> I base 58:
>
> PM8TJQCyt6ovbozreUCBrfKqmSVmTzJ5vjqse58LnBzKFFZTwny3KfCDdwTqAEYVasn11tTMPc2FJsFygFd3YzsHvwNXLEQNADgxeGnMK8Ugmin62TZU
>
> I base 16 (HEX):
> 4701000277507c9c17a89cfca2d3af554745d6c2db0e7f6b2721a3941a504933103cc42add94881210d6e752a9abc8a9fa0070e85184993c4f643f1121dd807dd556d1dc000000000000000000000000008604e4db

Hvis vi sammenligner min betalingskode med OP_RETURN, kan vi se at HRP (i brun) og sjekksummen (i rosa) ikke overføres. Dette er normalt, ettersom denne informasjonen er ment for mennesker.
Neste kan vi gjenkjenne (i grønt) versjonen (0x01), bitfeltet (0x00), og offentlige nøkkelpariteten (0x02). Og, på slutten av betalingskoden, de tomme bytene i svart (0x00) som tillater utfylling for å nå totalt 80 bytes. All denne metadataen overføres i klartekst (ukryptert). Til slutt kan vi observere at x-koordinaten til den offentlige nøkkelen (i blått) og kjedekoden (i rødt) har blitt kryptert. Dette utgjør nyttelasten til betalingskoden.

### Motta varslingstransaksjonen.

Nå som Alice har sendt varslingstransaksjonen til Bob, la oss se hvordan han tolker den.

Som en påminnelse, må Bob kunne få tilgang til Alices betalingskode. Uten denne informasjonen, som vi vil se i neste seksjon, vil han ikke kunne utlede nøkkelparene skapt av Alice, og derfor, vil han ikke kunne få tilgang til sine bitcoins mottatt med BIP47. For nå er Alices betalingskode nyttelast kryptert. La oss se sammen hvordan Bob dekrypterer den.

1. Bob overvåker transaksjoner som skaper utganger med hans varslingadresse.

2. Når en transaksjon har en utgang til hans varslingadresse, analyserer Bob den for å se om den inneholder en OP_RETURN-utgang som overholder BIP47-standarden.

3. Hvis det første bytet av OP_RETURN-nyttelasten er 0x01, starter Bob søket etter et mulig delt hemmelighet med ECDH:

- Bob velger den offentlige nøkkelen i transaksjonsinngangen. Det vil si, Alices offentlige nøkkel kalt "A" med:

> A = a·G

- Bob velger den private nøkkelen "b" assosiert med hans personlige varslingadresse:

> b

- Bob beregner det hemmelige punktet "S" (ECDH delt hemmelighet) på den elliptiske kurven ved å legge til og doble punkter, og anvender sin private nøkkel "b" på Alices offentlige nøkkel "A":

> S = b·A

- Bob bestemmer blendingsfaktoren "f" som vil tillate ham å dekryptere Alices betalingskode nyttelast. På samme måte som Alice beregnet det tidligere, vil Bob finne "f" ved å anvende HMAC-SHA512 på (x) x-koordinatverdien av det hemmelige punktet "S", og til (o) UTXOen brukt som inngang i denne varslingstransaksjonen:

> f = HMAC-SHA512(o, x)

4. Bob tolker dataene i OP_RETURN av varslingstransaksjonen som en betalingskode. Han dekrypterer ganske enkelt nyttelasten av denne potensielle betalingskoden ved hjelp av blendingsfaktoren "f".

- Bob deler blendingsfaktoren "f" i to deler: de første 32 bytene av "f" vil være "f1" og de siste 32 bytene vil være "f2".
- Bob dekrypterer den krypterte x-koordinatverdien (x') av Alices betalingskode offentlige nøkkel:

> x = x' XOR f1

- Bob dekrypterer den krypterte kjedekodeverdien (c') av Alices betalingskode:

> c = c' XOR f2

5. Bob sjekker om verdien av Alices betalingskode offentlige nøkkel er en del av secp256k1-gruppen. Hvis den er det, tolker han den som en gyldig betalingskode. Ellers ignorerer han transaksjonen.

Nå som Bob kjenner Alices betalingskode, kan hun sende ham opptil 2^32 betalinger uten å noen gang trenge å utføre en varslingstransaksjon som denne igjen.

Hvorfor fungerer dette? Hvordan kan Bob bestemme den samme blendingsfaktoren som Alice og dekryptere hennes betalingskode? La oss undersøke ECDH-prosessen mer detaljert basert på det vi nettopp beskrev.
Først og fremst har vi med symmetrisk kryptering å gjøre. Dette betyr at krypteringsnøkkelen og dekrypteringsnøkkelen er den samme verdien. I dette tilfellet er nøkkelen i varslingstransaksjonen blinding-faktoren (f = f1 || f2). Alice og Bob trenger å oppnå den samme verdien for f uten å overføre den direkte, ettersom en angriper kunne avlytte den og dekryptere den hemmelige informasjonen.
Denne blinding-faktoren oppnås ved å anvende HMAC-SHA512 på to verdier: x-koordinaten til et hemmelig punkt og den brukte UTXO i transaksjonsinngangen. Derfor trenger Bob å ha disse to stykkene informasjon for å dekryptere Alices betalingskode-last.

For inngangs-UTXOen kan Bob enkelt hente den ved å observere varslingstransaksjonen. For det hemmelige punktet, vil Bob måtte bruke ECDH.

Som sett i avsnittet om Diffie-Hellman, ved å utveksle sine respektive offentlige nøkler og hemmelig anvende sine private nøkler på den andres offentlige nøkkel, kan Alice og Bob finne et spesifikt og hemmelig punkt på den elliptiske kurven. Varslingstransaksjonen er avhengig av denne mekanismen:

> Bobs nøkkelpar:
>
> B = b·G
>
> Alices nøkkelpar:
>
> A = a·G
>
> For et hemmelig punkt S (x,y):
>
> S = a·B = a·b·G = b·a·G = b·A

![Diagram av generering av et delt hemmelig med ECDHE](assets/19.webp)
Nå som Bob kjenner Alices betalingskode, vil han kunne oppdage hennes BIP47-betalinger og utlede de private nøklene som blokkerer de mottatte bitcoinene.
![Bob tolker Alices varslingstransaksjon](assets/20.webp)

Kreditt: Gjenbrukbare Betalingskoder for Hierarkiske Deterministiske Lommebøker, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Hvis vi matcher dette diagrammet med det jeg beskrev for deg tidligere:

- "Wallet Pub-Key" på Alices side tilsvarer: A.

- "Child Priv-Key 0" på Bobs side tilsvarer: b.

- "Notification Shared Secret" tilsvarer: f.

- "Masked Payment Code" tilsvarer Alices maskerte betalingskode, dvs. med den krypterte lasten: x' og c'.

- "Notification Transaction" er transaksjonen som inneholder OP_RETURN.

La meg oppsummere stegene vi nettopp har sett sammen for å motta og tolke en varslingstransaksjon:

- Bob overvåker transaksjonsutganger til sin varslingadresse.

- Når han oppdager en, henter han informasjonen som er inneholdt i OP_RETURN.

- Bob velger den offentlige nøkkelen til inngangen og beregner et hemmelig punkt ved hjelp av ECDH.

- Han bruker dette hemmelige punktet til å beregne en HMAC, som er blinding-faktoren.

- Han bruker denne blinding-faktoren til å dekryptere Alices betalingskode-last som er inneholdt i OP_RETURN.

### BIP47-betalingstransaksjonen.

La oss nå studere betalingsprosessen med BIP47. For å minne deg på den nåværende situasjonen:

- Alice er klar over Bobs betalingskode, som hun enkelt hentet fra hans nettsted.

- Bob er klar over Alices betalingskode takket være varslingstransaksjonen.

- Alice vil gjøre en innledende betaling til Bob. Hun kan gjøre mange flere på samme måte.

Før jeg forklarer denne prosessen for deg, tror jeg det er viktig å minne deg på hvilke indekser vi for øyeblikket jobber med:

Vi beskriver avledningsstien til en betalingskode som følger: m/47'/0'/0'/. 

Neste dybde distribuerer indeksene som følger:
- Det første normale (ikke-herdede) barneparet brukes til å generere varslingsadressen vi diskuterte i forrige seksjon: m/47'/0'/0'/0/.
- Normale barnenøkkelpar brukes innen ECDH for å generere BIP47 betalingsmottaksadresser, som vi vil se i denne seksjonen: m/47'/0'/0'/ fra 0 til 2,147,483,647/.

- Herdede barnenøkkelpar er flyktige betalingskoder: m/47'/0'/0'/ fra 0' til 2,147,483,647'/.
  Hver gang Alice ønsker å sende en betaling til Bob, utleder hun en ny unik blank adresse, nok en gang takket være ECDH-protokollen:
- Alice velger den første private nøkkelen utledet fra hennes personlige gjenbrukbare betalingskode:

> a

- Alice velger den første ubrukte offentlige nøkkelen utledet fra Bobs betalingskode. Denne offentlige nøkkelen, vi vil kalle den "B". Den er assosiert med den private nøkkelen "b" som bare Bob kjenner.

> B = b·G

- Alice beregner et hemmelig punkt "S" på den elliptiske kurven ved å legge til og doble punkter, ved å anvende sin private nøkkel "a" på Bobs offentlige nøkkel "B":

> S = a·B

- Fra dette hemmelige punktet vil Alice beregne det delte hemmelige "s" (små bokstaver). For å gjøre dette, velger hun x-koordinaten til det hemmelige punktet "S" kalt "Sx", og hun passerer denne verdien inn i SHA256 hash-funksjonen.

> s = SHA256(Sx)

Ikke stol. Verifiser! Hvis du vil forstå de grunnleggende prinsippene for en hash-funksjon, vil du finne det du trenger i denne artikkelen. Og hvis du ikke stoler på NIST (du har rett), og du vil kunne forstå i detalj hvordan SHA256 fungerer, forklarer jeg alt i denne artikkelen på fransk.

- Alice bruker dette delte hemmelige "s" til å beregne en Bitcoin betalingsmottaksadresse. Først sjekker hun at "s" er innenfor rekkevidden av secp256k1-kurven. Hvis ikke, øker hun indeksen til Bobs offentlige nøkkel for å utlede et annet delt hemmelig.

- For det andre beregner hun en offentlig nøkkel "K0" ved å legge til punktene "B" og "s·G" på den elliptiske kurven. Med andre ord, Alice legger til den offentlige nøkkelen utledet fra Bobs betalingskode "B" med et annet punkt beregnet på den elliptiske kurven ved å legge til og doble punkter med det delte hemmelige "s" fra generasjonspunktet til secp256k1-kurven "G". Dette nye punktet representerer en offentlig nøkkel, og vi kaller det "K0":

> K0 = B + s·G

- Med denne offentlige nøkkelen "K0" kan Alice utlede en blank mottaksadresse på en standard måte (for eksempel, SegWit V0 i Bech32).

Når Alice har denne mottaksadressen "K0" som tilhører Bob, kan hun konstruere en standard Bitcoin-transaksjon ved å velge en UTXO som tilhører henne på en annen gren av hennes HD-lommebok, og bruke den til Bobs "K0"-adresse.

![Alice sender bitcoins med BIP47 til Bob](assets/21.webp)

Kreditt: Gjenbrukbare Betalingskoder for Hierarkiske Deterministiske Lommebøker, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
Hvis vi matcher dette diagrammet med det jeg beskrev til deg tidligere:

- "Child Priv-Key" på Alices side tilsvarer: a.
- "Child Pub-Key 0" på Bobs side tilsvarer: B.
- "Payment Secret 0" tilsvarer: s.
- "Payment Pub-Key 0" tilsvarer: K0.
La meg oppsummere stegene vi nettopp gikk gjennom sammen for å sende en BIP47-betaling:

- Alice velger den første avledede barneprivate nøkkelen fra sin personlige betalingskode.
- Hun beregner et hemmelig punkt på den elliptiske kurven ved å bruke ECDH fra den første ubrukte avledede barneoffentlige nøkkelen fra Bobs betalingskode.
- Hun bruker dette hemmelige punktet til å beregne et delt hemmelig med SHA256.
- Hun bruker dette delte hemmelige til å beregne et nytt hemmelig punkt på den elliptiske kurven.
- Hun legger til dette nye hemmelige punktet til Bobs offentlige nøkkel.
- Hun oppnår en ny efemer offentlig nøkkel som kun Bob har den tilhørende private nøkkelen til.
- Alice kan sende en vanlig transaksjon til Bob med den avledede efemere mottaksadressen.

Hvis hun ønsker å gjøre en andre betaling, vil hun gjenta de ovennevnte stegene, bortsett fra at hun vil velge den andre avledede offentlige nøkkelen fra Bobs betalingskode. Det vil si, den neste ubrukte nøkkelen. Hun vil da ha en andre mottaksadresse som tilhører Bob, "K1".

![Alice avleder tre BIP47 mottaksadresser for Bob](assets/22.webp)

Kreditt: Gjenbrukbare Betalingskoder for Hierarkiske Deterministiske Lommebøker, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Hun kan fortsette slik og avlede opptil 2^32 blanke adresser som tilhører Bob.

Fra et eksternt perspektiv, ved å observere Bitcoin-blockchainen, er det teoretisk umulig å skille en BIP47-betaling fra en vanlig betaling. Her er et eksempel på en BIP47-betalings transaksjon på Testnet:

https://blockstream.info/testnet/tx/94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

TXID:

> 94b2e59510f2e1fa78411634c98a77bbb638e28fb2da00c9f359cd5fc8f87254

Det ser ut som en vanlig transaksjon med et brukt inngang, en betalingsutgang på 210,000 sats, og veksling.

![Bitcoin-betalingstransaksjon med BIP47](assets/23.webp)

Kreditt: https://blockstream.info/

### Motta BIP47-betalingen og avlede den private nøkkelen.

Alice har nettopp gjort sin første betaling til en blank BIP47-adresse eid av Bob. Nå la oss se hvordan Bob mottar denne betalingen. Vi vil også se hvorfor Alice ikke har tilgang til den private nøkkelen til adressen hun nettopp genererte, og hvordan Bob henter denne nøkkelen for å bruke bitcoinene han nettopp har mottatt.

Så snart Bob mottar varslingstransaksjonen fra Alice, avleder han BIP47-offentlige nøkkelen "K0" selv før hun sender noen betaling til den. Han observerer derfor enhver betaling til den tilknyttede adressen. Faktisk avleder han umiddelbart flere adresser som han vil observere (K0, K1, K2, K3...). Her er hvordan han avleder denne offentlige nøkkelen "K0":

- Bob velger den første barneprivate nøkkelen avledet fra sin betalingskode. Denne private nøkkelen er navngitt "b". Den er assosiert med den offentlige nøkkelen "B" som Alice brukte i det forrige steget:

> b

- Bob velger Alices første avledede offentlige nøkkel fra hennes betalingskode. Denne nøkkelen er navngitt "A". Den er assosiert med den private nøkkelen "a" som Alice brukte i sine beregninger, og som kun Alice er klar over. Bob kan utføre denne prosessen fordi han kjenner Alices betalingskode som ble overført til ham med varslingstransaksjonen.

> A = a·G
- Bob beregner det hemmelige punktet "S" ved å legge til og doble punkter på den elliptiske kurven, og anvender sin private nøkkel "b" på Alices offentlige nøkkel "A". Her bruker vi ECDH, som garanterer at dette punktet "S" vil være det samme for både Bob og Alice.
> S = b·A

- Akkurat som Alice gjorde, isolerer Bob x-koordinaten til dette punktet "S". Vi har kalt denne verdien "Sx". Han sender denne verdien gjennom SHA256-funksjonen for å finne det delte hemmelige "s" (små bokstaver).

> s = SHA256(Sx)

- På samme måte som Alice, beregner Bob punktet "s·G" på den elliptiske kurven. Deretter legger han til dette hemmelige punktet til sin offentlige nøkkel "B". Han får da et nytt punkt på den elliptiske kurven som han tolker som en offentlig nøkkel "K0":

> K0 = B + s·G

Når Bob har denne offentlige nøkkelen "K0", kan han utlede den tilhørende private nøkkelen for å bruke sine bitcoins. Han er den eneste som kan generere dette tallet.

- Bob legger til sin avledede barnenøkkel "b" fra sin personlige betalingskode. Han er den eneste som kan oppnå verdien av "b". Deretter legger han til "b" til det delte hemmelige "s" for å oppnå k0, den private nøkkelen til K0:

> k0 = b + s
> Takket være gruppeloven for den elliptiske kurven, får Bob nøyaktig den private nøkkelen som tilsvarer den offentlige nøkkelen brukt av Alice. Så vi har:
> K0 = k0·G

![Bob genererer sine BIP47 mottaksadresser](assets/24.webp)

Kreditt: Gjenbrukbare Betalingskoder for Hierarkiske Deterministiske Lommebøker, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Hvis vi matcher dette diagrammet med det jeg beskrev for deg tidligere:

- "Child Priv-Key 0" på Bobs side tilsvarer: b.

- "Child Pub-Key 0" på Alices side tilsvarer: A.

- "Payment Secret 0" tilsvarer: s.

- "Payment Pub-Key 0" tilsvarer: K0.

- "Payment Priv-Key 0" tilsvarer: k0.

La meg oppsummere stegene vi nettopp har sett sammen for å motta en BIP47-betaling og beregne den tilsvarende private nøkkelen:

- Bob velger den første avledede barnenøkkelen fra sin personlige betalingskode.

- Han beregner et hemmelig punkt på den elliptiske kurven ved hjelp av ECDH fra den første avledede barnenøkkelen fra Alices kjedekode.

- Han bruker dette hemmelige punktet til å beregne et delt hemmelig med SHA256.

- Han bruker dette delte hemmelige til å beregne et nytt hemmelig punkt på den elliptiske kurven.

- Han legger til dette nye hemmelige punktet til sin personlige offentlige nøkkel.

- Han oppnår en ny efemer offentlig nøkkel, som Alice vil sende sin første betaling til.

- Bob beregner den private nøkkelen assosiert med denne efemere offentlige nøkkelen ved å legge til sin avledede barnenøkkel fra sin betalingskode og det delte hemmelige.

Siden Alice ikke kan oppnå "b", Bobs private nøkkel, er hun ute av stand til å bestemme k0, den private nøkkelen assosiert med Bobs BIP47 mottaksadresse.

Skjematisk kan vi representere beregningen av det delte hemmelige "S" som følger:

![Beregning av det delte hemmelige med ECDHE](assets/25.webp)

Når det delte hemmelige er funnet med ECDH, beregner Alice og Bob BIP47 betalings offentlige nøkkel "K0", og Bob beregner også den assosierte private nøkkelen "k0":
### Tilbakebetaling av BIP47-betalingen.

Siden Bob er klar over Alices gjenbrukbare betalingskode, har han allerede all nødvendig informasjon for å sende henne en tilbakebetaling. Han trenger ikke å kontakte Alice for å be om informasjon. Han vil ganske enkelt varsle henne med en varslingstransaksjon, spesielt slik at hun kan gjenopprette sine BIP47-adresser med sin seed, og deretter kan han også sende henne opptil 2^32 betalinger.
Bob kan deretter tilbakebetale Alice på samme måte som hun sendte ham betalinger. Rollene er reversert:

![Bob sender en tilbakebetaling til Alice med BIP47](assets/27.webp)

Kreditt: Gjenbrukbare Betalingskoder for Hierarkiske Deterministiske Lommebøker, Justus Ranvier. https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki

Du kjenner nå alle detaljene i denne fantastiske løsningen som BIP47 representerer.

## Avledede bruksområder av PayNym.

Implementeringen av denne BIP47 på Samourai Wallet har resultert i PayNyms, identifikatorer beregnet fra brukernes betalingskoder. I dag går deres nytte langt utover bruken av BIP47.

Samourai-teamet utvikler gradvis et helt økosystem av verktøy og tjenester basert på brukerens PayNym. Blant disse er det selvfølgelig alle utgiftsverktøyene som tillater optimalisering av brukerens personvern ved å legge til entropi i en transaksjon, og dermed legge til plausibel benektelse.

Den kombinerte bruken av Soroban, det krypterte kommunikasjonsnettverket basert på Tor, og PayNyms har sterkt optimalisert brukeropplevelsen ved oppbygging av samarbeidstransaksjoner, samtidig som det opprettholdes et godt sikkerhetsnivå. Dermed er det enkelt å utføre Stowaway (PayJoin) og StonewallX2-transaksjoner uten manuelt å utføre de mange utvekslingene av usignerte transaksjoner som kreves for å sette opp en slik samarbeidstransaksjon.

I motsetning til bruken av BIP47, siden disse samarbeidstransaksjonene ikke krever en varslingstransaksjon, er det tilstrekkelig å koble PayNyms for å bruke disse verktøyene. Det er ikke nødvendig å koble dem.

Hvis du vil lære mer om samarbeidstransaksjoner, og mer bredt om alle utgiftsverktøyene til Samourai Wallet, kan du lese "Spending Tools"-delen i denne artikkelen. Du vil finne en teknisk forklaring og en detaljert opplæring for hvert verktøy.

I tillegg til disse samarbeidstransaksjonene, har det nylig blitt observert at Samourai-teamet jobber med et autentiseringsprotokoll knyttet til PayNym: Auth47. Dette verktøyet er allerede implementert og tillater for eksempel autentisering med et PayNym på et nettsted som aksepterer denne metoden. I fremtiden tror jeg at utover denne muligheten for autentisering på nettet, vil Auth47 være en del av et større prosjekt rundt BIP47/PayNym/Samourai-økosystemet. Kanskje vil denne protokollen bli brukt til å ytterligere optimalisere brukeropplevelsen av Samourai Wallet, spesielt i bruk av utgiftsverktøy. Det gjenstår å se...

## Min personlige mening om BIP47.

Åpenbart er hovedulempen med BIP47 varslingstransaksjonen. Den fører til at brukeren må bruke gebyrer for gruvedriften, noe som kan være irriterende for noen. Imidlertid er argumentet om "spam" på Bitcoin-blockchainen absolutt uakseptabelt. Alle som betaler gebyrene for sin transaksjon, må kunne registrere den i hovedboken, uavhengig av formålet. Å hevde noe annet er å gå inn for sensur.

Det er mulig at det i fremtiden vil bli funnet andre mindre kostbare løsninger for å kommunisere avsenderens betalingskode til mottakeren, og for mottakeren å sikkert lagre den. Men for nå forblir varslingstransaksjonen løsningen med færrest kompromisser.
Denne ulempen forblir ubetydelig når man vurderer alle fordelene med BIP47. Blant alle de eksisterende forslagene for å løse dette problemet med gjenbruk av adresser, fremstår det for meg som den beste løsningen. Som forklart tidligere, kommer flertallet av adressebruken fra børser. BIP47 er den eneste fornuftige løsningen som faktisk løser dette problemet ved kilden. Ethvert forslag som sikter på å redusere antallet adressegjenbruk bør fokusere på dette aspektet og tilpasse løsningen til hovedkilden til problemet.

Når det gjelder brukervennlighet, selv om dens indre mekanismer er ganske komplekse, er BIP47-betalingsprosedyren enkel. Gjenbrukbare betalingskoder kan derfor enkelt adopteres, selv av nybegynnere.

Når det gjelder personvern, er BIP47 veldig interessant. Som jeg forklarte i seksjonen om varslingstransaksjonen, avslører ikke betalingskoden noen informasjon om de avledede flyktige adressene. Den bryter derfor informasjonsflyten mellom Bitcoin-transaksjonen og mottakerens identifikator, i motsetning til den tradisjonelle bruken av en mottaksadresse.

Og fremfor alt, PayNym-implementeringen av BIP47 fungerer! Den har vært tilgjengelig på Samourai Wallet siden 2016 og på Sparrow Wallet siden begynnelsen av dette året. Det er ikke et vitenskapelig prosjekt, men en løsning som ble testet i går og er fullt funksjonell i dag.

Forhåpentligvis vil disse gjenbrukbare betalingskodene i fremtiden bli adoptert av aktører i økosystemet, implementert i lommebokprogramvare, og brukt av Bitcoinere.

Enhver virkelig positiv løsning for brukerens personvern må debatteres, fremmes og forsvares, slik at Bitcoin ikke blir lekeplassen til CA-er og overvåkningsverktøyet til regjeringer.
Han tenkte på hvordan han hadde blitt forfulgt og fornærmet overalt, og nå hørte han alle si at han var den vakreste av alle disse vakre fuglene! Og selv svarthyllen bøyde sine grener mot ham, og solen spredte et så varmt og velvillig lys! Da svulmet fjærene hans, hans slanke hals rettet seg opp, og han utbrøt med hele sitt hjerte, "Hvordan kunne jeg ha drømt om så mye lykke da jeg bare var en stygg liten andunge."

## For å gå videre:

- Forstå og bruke CoinJoin på Bitcoin.

- Forstå avledningsveiene til en Bitcoin-lommebok.

- Installere og bruke din RoninDojo Bitcoin-node.

### Eksterne ressurser og anerkjennelser:

Takk til LaurentMT og Théo Pantamis for de mange konseptene de forklarte meg, som jeg har brukt i denne artikkelen. Jeg håper jeg har formidlet dem nøyaktig.

Takk til Fanis Michalakis for korrekturlesing av denne teksten og hans ekspertise.

- https://bitcoiner.guide/paynym/
- https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman
- https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman_bas%C3%A9_sur_les_courbes_elliptiques
- https://security.stackexchange.com/questions/46802/what-is-the-difference-between-dhe-and-ecdh#:~:text=The%20difference%20between%20DHE%20and%20ECDH%20in%20two%20bullet%20points,a%20type%20of%20algebraic%20curve).
- https://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art060
- https://ee.stanford.edu/~hellman/publications/24.pdf
- https://www.researchgate.net/publication/317339928_A_study_on_diffie-hellman_key_exchange_protocols