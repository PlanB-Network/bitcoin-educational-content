---
name: Introduksjon til de kryptografiske algoritmene til Bitcoin
goal: Forstå opprettelsen av en Bitcoin-lommebok fra et kryptografisk perspektiv
objectives:
  - Avmystifisere kryptografi-terminologi relatert til Bitcoin.
  - Mestre opprettelsen av en Bitcoin-lommebok.
  - Forstå strukturen til en Bitcoin-lommebok.
  - Forstå adresser og avledningsveier.
---

# En reise inn i kryptografi

Er du fascinert av Bitcoin? Lurer du på hvordan en Bitcoin-lommebok fungerer? Gjør deg klar til å legge ut på en fengslende reise inn i kryptografien! Loïc, vår ekspert, vil veilede deg gjennom kompleksiteten ved å opprette en Bitcoin-lommebok, og avdekke mysteriene bak skremmende tekniske termer som hashing, nøkkelavledning og elliptiske kurver.

Denne opplæringen vil ikke bare utstyre deg med kunnskapen til å forstå strukturen til en Bitcoin-lommebok, men også forberede deg på å dykke dypere inn i den spennende verdenen av kryptografi. Så, er du klar til å legge ut på denne reisen? Bli med oss og gjør din nysgjerrighet til ekspertise!

+++

# Introduksjon
<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>

## Introduksjon til kryptografi
<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>

### Er dette opplæringen for deg? JA!

Vi er glade for å ønske deg velkommen til det nye opplæringskurset med tittelen "Krypto 301: Introduksjon til kryptografi og HD-lommebøker", ledet av eksperten på feltet, Loïc Morel. Dette kurset vil fordype deg i den fascinerende verdenen av kryptografi, den grunnleggende disiplinen innen matematikk som sikrer kryptering og sikkerhet av dataene dine.

I våre daglige liv, og spesielt innenfor Bitcoin, spiller kryptografi en avgjørende rolle. Konsepter relatert til kryptografi, som private nøkler, offentlige nøkler, adresser, avledningsveier, seed og entropi, er kjernen i bruk og opprettelse av en Bitcoin-lommebok. Gjennom dette kurset vil Loïc forklare i detalj hvordan private nøkler genereres og hvordan de er knyttet til adresser. Loïc vil også vie en time til å forklare de matematiske detaljene ved elliptiske kurver. I tillegg vil du forstå hvorfor bruken av HMAC SHA512 er viktig for å sikre lommeboken din og hva forskjellen er mellom en seed og en mnemonic frase.
Det ultimate målet med denne opplæringen er å gjøre deg i stand til å forstå de tekniske prosessene som er involvert i å opprette en HD-lommebok og de kryptografiske metodene som brukes. Gjennom årene har Bitcoin-lommebøker utviklet seg til å bli enklere å bruke, mer sikre og standardiserte takket være spesifikke BIP-er. Loïc vil hjelpe deg med å forstå disse BIP-ene for å gripe valgene som er gjort av Bitcoin-utviklere og kryptografer. Som alle opplæringene som tilbys av universitetet vårt, er denne helt gratis og åpen kildekode. Dette betyr at du er fri til å ta den og bruke den som du ønsker. Vi ser frem til å motta din tilbakemelding ved slutten av dette spennende kurset.

### Ordet er ditt, professor!

Hei alle sammen, jeg er Loïc Morel, din guide gjennom denne tekniske utforskningen av kryptografien som brukes i Bitcoin-lommebøker.

Vår reise begynner med et dypdykk i de kryptografiske hash-funksjonenes dyp. Sammen vil vi dissekere de indre arbeidene til den essensielle SHA256 og utforske ulike algoritmer dedikert til avledning.

Vi vil fortsette vårt eventyr ved å dechiffrere den mystiske verdenen av digitale signaturer. Du vil oppdage hvordan magien med elliptiske kurver gjelder for disse signaturene, og vi vil kaste lys over hvordan man beregner den offentlige nøkkelen fra den private nøkkelen. Og selvfølgelig, vi vil dykke inn i prosessen med digital signatur.
Neste skal vi gå tilbake i tid for å se på utviklingen av Bitcoin-lommebøker, og vi vil dykke inn i konseptene entropi og tilfeldige tall. Vi vil gjennomgå den berømte mnemonic-frasen, samtidig som vi også tar for oss passfrasen. Du vil til og med få muligheten til å oppleve noe unikt ved å skape et frø fra 128 terningkast!
Med disse solide grunnlagene, vil vi være klare for den avgjørende delen: å skape en Bitcoin-lommebok. Fra fødselen av frøet og hovednøkkelen, til studiet av utvidede nøkler, og derivasjonen av barne nøkkelpar, vil hvert steg bli dissekert. Vi vil også diskutere strukturen til lommeboken og derivasjonsveier.

For å toppe det hele, vil vi avslutte reisen vår med å undersøke Bitcoin-adresser. Vi vil forklare hvordan de blir skapt og hvordan de spiller en essensiell rolle i funksjonen til Bitcoin-lommebøker.

Bli med meg på denne fengslende reisen, og gjør deg klar til å utforske kryptografiverdenen som aldri før. Legg dine forutinntatte meninger til side og åpne sinnet ditt for en ny måte å forstå Bitcoin og dets fundamentale struktur på.

# Hashfunksjoner
<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>

## Introduksjon til kryptografiske hashfunksjoner relatert til Bitcoin
<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>

Velkommen til dagens økt dedikert til en grundig fordypning i den kryptografiske verdenen av hashfunksjoner, en avgjørende hjørnestein i sikkerheten til Bitcoin-protokollen. Forestill deg en hashfunksjon som en ultraeffektiv kryptografisk dekrypteringsrobot som transformerer informasjon av hvilken som helst størrelse til et unikt og fast størrelse digitalt fingeravtrykk, kalt en "hash", "digest", eller "checksum".
Oppsummert tar en hashfunksjon en inngangsmelding av vilkårlig størrelse og konverterer den til et fast størrelse utgangsfingeravtrykk.

Å beskrive profilen til kryptografiske hashfunksjoner krever forståelse av to essensielle kvaliteter: deres irreversibilitet og deres motstandsdyktighet mot forfalskning.

Irreversibilitet, eller motstandsdyktighet mot preimage, betyr at det å beregne utgangen gitt inngangen kan gjøres enkelt, men å beregne inngangen fra utgangen er umulig.
Det er en enveisfunksjon.

![bilde](assets/image/section1/0.webp)

Motstandsdyktighet mot forfalskning kommer av det faktum at selv den minste modifikasjonen av inngangen vil resultere i et dypt forskjellig utgangspunkt.
Disse funksjonene tillater verifisering av integriteten til nedlastet programvare.

![bilde](assets/image/section1/1.webp)

En annen avgjørende egenskap de besitter er deres motstandsdyktighet mot kollisjoner og andre preimage. En kollisjon oppstår når to distinkte innganger produserer samme utgang.
Sikkert, i hashuniverset, er kollisjoner uunngåelige, men en utmerket kryptografisk hashfunksjon minimerer dem betydelig. Risikoen må være så lav at den kan anses som ubetydelig. Det er som om hver hash var et hus i en enorm by; til tross for det enorme antallet hus, sikrer en god hashfunksjon at hvert hus har en unik adresse.

Motstandsdyktighet mot andre preimage avhenger av motstandsdyktighet mot kollisjoner; hvis det er motstandsdyktighet mot kollisjoner, så er det motstandsdyktighet mot andre preimage.
Gitt en inngangsinformasjon som er pålagt oss, må vi finne en andre inngang, forskjellig fra den første, som produserer en kollisjon i utgangshashen til funksjonen. Motstandsdyktighet mot andre preimage er lik motstandsdyktighet mot kollisjoner, bortsett fra at inngangen er pålagt.
La oss nå navigere gjennom de turbulente vannene av utdaterte hash-funksjoner. SHA0, SHA1 og MD5 anses nå som rustne skall i havet av kryptografisk hashing. De frarådes ofte ettersom de har mistet sin motstand mot kollisjoner. Duehullsprinsippet forklarer hvorfor, til tross for våre beste anstrengelser, unngåelse av kollisjoner er umulig på grunn av begrensningen av utdatastørrelsen. For å virkelig anses som sikker, må en hash-funksjon motstå kollisjoner, andre prebilder og prebilder.
Et nøkkelelement i Bitcoin-protokollen, SHA-256 hash-funksjonen, er kapteinen på skipet. Andre funksjoner, som SHA-512, brukes til derivasjon med HMAC og PBKDF. I tillegg brukes RIPMD160 for å redusere et fingeravtrykk til 160 bits. Når vi refererer til HASH256 og HASH160, snakker vi om bruk av dobbel hashing med SHA-256 og RIPMD.

For HASH256, er det en dobbel hash av meldingen ved bruk av SHA256-funksjonen.
$$
SHA256(SHA256(melding))
$$
For HASH160, er det en dobbel hash av meldingen ved bruk av SHA256 først, deretter RIPMD160.
$$
RIPMD160(SHA256(melding))
$$
Bruken av HASH160 er spesielt fordelaktig ettersom det tillater sikkerheten til SHA-256 samtidig som størrelsen på fingeravtrykket reduseres.

Oppsummert er det ultimate målet med en kryptografisk hash-funksjon å transformere informasjon av vilkårlig størrelse til et fingeravtrykk med fast størrelse. For å bli anerkjent som sikker, må den ha flere styrker: irreversibilitet, motstand mot manipulering, motstand mot kollisjoner, og motstand mot andre prebilder.

![bilde](assets/image/section1/2.webp)

Ved slutten av denne utforskningen har vi avmystifisert kryptografiske hash-funksjoner, belyst deres bruk i Bitcoin-protokollen, og dissekert deres spesifikke mål. Vi har lært at for at hash-funksjoner skal anses som sikre, må de være motstandsdyktige mot prebilder, andre prebilder, kollisjoner og manipulering. Vi har også dekket rekkevidden av forskjellige hash-funksjoner brukt i Bitcoin-protokollen. I vår neste økt vil vi dykke inn i kjernen av SHA256 hash-funksjonen og oppdage den fascinerende matematikken som gir den sine unike egenskaper.

## Det indre arbeidet til SHA256
<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>

Velkommen til fortsettelsen av vår fascinerende reise gjennom de kryptografiske labyrintene av hash-funksjonen. I dag avdekker vi mysteriene med SHA256, en kompleks, men genial prosess som vi introduserte tidligere.

Som en påminnelse, formålet med SHA256 hash-funksjonen er å ta en inngangsmelding av hvilken som helst størrelse og generere en 256-bits hash som utdata.

### Forbehandling

La oss ta et skritt videre i denne labyrinten ved å starte med forbehandlingen av SHA256.

#### Padding-biter

Målet med dette første steget er å ha en melding som er liketil et multiplum av 512 bits. For å oppnå dette, vil vi legge til padding-biter til meldingen.

La M være den opprinnelige meldingsstørrelsen.
La 1 være en bit reservert for separator.
La P være antall bits brukt for padding, og 64 være antall bits satt til side for den andre forbehandlingsfasen.
Totalen skal være et multiplum av 512 bits, som er representert ved n.

![bilde](assets/image/section1/3.webp)

Eksempel med en inngangsmelding på 950 bits:

```
Steg 1: Bestem størrelsen; det endelige ønskede antallet av bits.
Det første multiplum av 512 > (M + 64 + 1) (med M = 950) er 1024. 1024 = 2 * 512
Så n = 2.

Steg 2: Bestem P, antall fyllbits som trengs for å nå det endelige ønskede antall bits.
-> M + 1 + P + 64 = n * 512
-> M + 1 + P + 64 = 2 * 512
-> 950 + 1 + P + 64 = 1024
-> P = 1024 - 1 - 64 - 950
-> P = 9

Derfor må 9 fyllbits legges til for å ha en melding lik et multiplum av 512.

```
melding + 1 000 000 000
```

#### Størrelsesfylling

Vi går nå videre til den andre fasen av forbehandlingen, som innebærer å legge til den binære representasjonen av størrelsen på den opprinnelige meldingen i bits.

La oss gjenbesøke eksemplet med en inngang på 950 bits:

```
Den binære representasjonen av tallet 950 er: 11 1011 0110

Vi bruker våre 64 reserverte bits fra det forrige steget. Vi legger til nuller for å runde våre 64 bits til vår likestilte inngang. Deretter fusjonerer vi den opprinnelige meldingen, fyllbitsene, og størrelsesfyllingen for å oppnå vår likestilte inngang.
```

Her er resultatet:

![bilde](assets/image/section1/4.webp)

### Behandling

#### Forstå Forutsetninger

##### Konstanter og Initialiseringsvektorer

Nå forbereder vi oss på de innledende stegene for behandling av SHA-256-funksjonen. Akkurat som i enhver god oppskrift, trenger vi noen grunnleggende ingredienser, som vi kaller konstanter og initialiseringsvektorer.

Initialiseringsvektorene, fra A til H, er de første 32 bits av desimaldelene av kvadratrøttene til de første 8 primtallene. De vil tjene som basisverdier i de innledende behandlingstrinnene. Deres verdier er i heksadesimalt format.

Konstantene K, fra 0 til 63, representerer de første 32 bits av desimaldelene av kubikkrøttene til de første 64 primtallene. De brukes i hver runde av kompresjonsfunksjonen. Deres verdier er også i heksadesimalt format.

![bilde](assets/image/section1/5.webp)

##### Brukte Operasjoner

Innen kompresjonsfunksjonen bruker vi spesifikke operatorer som XOR, AND og NOT. Vi behandler bitsene en etter en i henhold til deres posisjon, ved å bruke XOR-operatoren og en sannhetstabell. AND-operatoren brukes til å returnere 1 kun hvis begge operander er lik 1, og NOT-operatoren brukes til å returnere den motsatte verdien av en operand. Vi bruker også SHR-operasjonen for å skifte bitsene til høyre med et valgt antall.

Sannhetstabellen:

![bilde](assets/image/section1/6.webp)

Bitforskyvningsoperasjoner:

![bilde](assets/image/section1/7.webp)

#### Kompresjonsfunksjonen

Før vi anvender kompresjonsfunksjonen, deler vi inngangen inn i blokker på 512 bits. Hver blokk vil bli behandlet uavhengig av de andre.

Hver 512-bits blokk deles deretter videre inn i 32-bits biter kalt W. På denne måten representerer W(0) de første 32 bits av 512-bits blokken. W(1) representerer de neste 32 bits, og så videre, til vi når 512 bits av blokken.
Når alle konstantene K og bitene W er definert, kan vi utføre følgende beregninger for hver bit W i hver runde.
Vi utfører 64 runder med beregninger i kompresjonsfunksjonen. I den siste runden, på "Output av funksjonen"-nivået, vil vi ha en mellomliggende tilstand som vil bli lagt til den opprinnelige tilstanden til kompresjonsfunksjonen.

Deretter gjentar vi alle disse trinnene i kompresjonsfunksjonen på neste 512-bits blokk, til den siste blokken.

Alle tillegg i kompresjonsfunksjonen er modulo 2^32 tillegg for å alltid beholde en 32-bits sum.

![bilde](assets/image/section1/9.webp)

![bilde](assets/image/section1/8.webp)

##### En runde av kompresjonsfunksjonen

![bilde](assets/image/section1/11.webp)

![bilde](assets/image/section1/10.webp)

Kompresjonsfunksjonen vil bli utført 64 ganger. Vi har våre biter W og våre tidligere definerte konstanter K som inngang.
De røde kvadratene/kryssene tilsvarer en modulo 2^32-bits tillegg.

Inngangene A, B, C, D, E, F, G, H vil bli assosiert med en 32-bits verdi for å utgjøre totalt 32 * 8 = 256 bits.
Vi har også en ny sekvens A, B, C, D, E, F, G, H som utgang. Denne utgangen vil deretter bli brukt som inngang for neste runde og så videre til slutten av den 64. runden.

Verdiene av inngangssekvensen for den første runden av kompresjonsfunksjonen tilsvarer de forhåndsdefinerte initialiseringsvektorene nevnt tidligere.
Som en påminnelse representerer initialiseringsvektorene de første 32 bitene av desimaldelene av kvadratroten av de første 8 primtallene.

Her er et eksempel på en runde:

![bilde](assets/image/section1/12.1.webp)

##### Mellomliggende Tilstand

Som en påminnelse, meldingen er delt inn i blokker på 512 bits, som deretter er delt inn i 32-bits biter. For hver 512-bits blokk, anvender vi de 64 rundene av kompresjonsfunksjonen.
Den mellomliggende tilstanden tilsvarer slutten av de 64 rundene av en blokk. Verdiene av utgangssekvensen fra denne 64. runden brukes som innledende verdier for inngangssekvensen av den første runden av neste blokk.

![bilde](assets/image/section1/12.2.webp)

#### Oversikt over hash-funksjonen

![bilde](assets/image/section1/13.webp)

Vi kan legge merke til at utgangen av det første 512-bits meldingsstykket tilsvarer våre initialiseringsvektorer som inngang for det andre 512-bits meldingsstykket, og så videre.

Utgangen av den siste runden, av det siste stykket, tilsvarer det endelige resultatet av SHA256-funksjonen.

Til slutt ønsker vi å understreke den avgjørende rollen til beregningene utført i CH, MAJ, σ0, og σ1 boksene. Disse operasjonene, blant andre, er vokterne som sikrer robustheten til SHA256 hash-funksjonen mot angrep, noe som gjør den til et foretrukket valg for å sikre mange digitale systemer, spesielt innenfor Bitcoin-protokollen. Det er tydelig at, selv om kompleks, ligger skjønnheten i SHA256 i dens evne til å finne inngangen fra hashen, mens verifiseringen av hashen for en gitt inngang er en mekanisk enkel handling.

## Algoritmene brukt for derivasjon
<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>
HMAC og PBKDF2-derivatalgoritmene er nøkkelkomponenter i sikkerhetsmekanismen til Bitcoin-protokollen. De forhindrer en rekke potensielle angrep og sikrer integriteten til Bitcoin-lommebøker. HMAC og PBKDF2 er kryptografiske verktøy brukt for ulike oppgaver i Bitcoin. HMAC brukes primært for å motvirke lengdeutvidelsesangrep når man utleder Hierarkiske Deterministiske (HD) lommebøker, mens PBKDF2 brukes til å konvertere en mnemonic frase til et frø.

#### HMAC-SHA512

HMAC-SHA512-paret har to innganger: en melding m (Inngang 1) og en nøkkel K vilkårlig valgt av brukeren (Inngang 2). Det har også en fast størrelse på utdata: 512 bits.

La oss merke:
- m: vilkårlig stor melding valgt av brukeren (inngang 1)
- K: vilkårlig nøkkel valgt av brukeren (inngang 2)
- K': likestilt nøkkel K. Den har blitt justert til størrelsen B på blokkene.
- ||: konkateneringsoperasjon.
- opad: konstant definert av byten 0x5c gjentatt B ganger.
- ipad: konstant definert av byten 0x36 gjentatt B ganger.
- B: Størrelsen på blokkene til hashfunksjonen som brukes.

![bilde](assets/image/section1/14.webp)

HMAC-SHA512, som tar en melding og en nøkkel som innganger, genererer en fast størrelse på utdata. For å sikre uniformitet, justeres nøkkelen basert på størrelsen på blokkene som brukes i hashfunksjonen. I konteksten av HD-lommebokderivat, brukes HMAC-SHA-512. Den opererer med 1024-bit (128-byte) blokker og justerer nøkkelen deretter. Den bruker konstantene OPAD (0x5c) og IPAD (0x36), gjentatt etter behov for å forbedre sikkerheten.

HMAC-SHA-512-prosessen involverer konkatenering av resultatet av SHA-512 anvendt på nøkkelen XOR OPAD og nøkkelen XOR IPAD med meldingen. Når den brukes med 1024-bit (128-byte) blokker, blir inngangsnøkkelen om nødvendig fylt med nuller, deretter XORet med IPAD og OPAD. Den modifiserte nøkkelen blir deretter konkateneret med meldingen.

![bilde](assets/image/section1/15.webp)

Inkluderingen av et salt i strengkoden øker sikkerheten til avledede nøkler. Uten det, kunne et angrep kompromittere hele lommeboken og stjele alle bitcoins.

PBKDF2 brukes til å konvertere en mnemonic frase til et frø. Denne algoritmen utfører 2048 runder ved hjelp av HMAC SHA512. Gjennom disse derivatalgoritmene kan forskjellige innganger produsere et unikt og fast utdata, som reduserer problemet med mulige lengdeutvidelsesangrep på SHA-2 familiefunksjoner.
Et lengdeutvidelsesangrep utnytter en spesifikk egenskap ved visse kryptografiske hashfunksjoner. I et slikt angrep kan en angriper som allerede besitter hashen av en ukjent melding bruke den til å beregne hashen av en lengre melding, som er en utvidelse av den opprinnelige meldingen. Dette er ofte mulig uten å kjenne innholdet i den opprinnelige meldingen, noe som kan føre til betydelige sikkerhetsproblemer hvis denne typen hashfunksjon brukes til oppgaver som integritetsverifisering.

![bilde](assets/image/section1/16.webp)

Konklusjonen er at HMAC og PBKDF2-algoritmene spiller essensielle roller i sikkerheten til HD-lommebokderivat i Bitcoin-protokollen. HMAC-SHA-512 brukes for å beskytte mot lengdeutvidelsesangrep, mens PBKDF2 tillater konverteringen av mnemonic frasen til et frø. Strengkoden legger til en ekstra kilde til entropi i nøkkelderivat, noe som sikrer systemets robusthet.

# Digitale Signaturer
## Digitale Signaturer og Elliptiske Kurver

Hvor er disse berømte bitcoinene lagret? Ikke i en Bitcoin-lommebok, som man kanskje skulle tro. I virkeligheten lagrer en Bitcoin-lommebok de private nøklene som er nødvendige for å bevise eierskap til bitcoinene. Bitcoinene selv er registrert på blockchain, en desentralisert database som arkiverer alle transaksjoner.

I Bitcoin-systemet er enheten for kontoen bitcoin (merk den lille "b"). Den er delelig opp til åtte desimaler, med den minste enheten som satoshi. UTXOer, eller "Unspent Transaction Outputs," representerer de ubrukte transaksjonsutgangene som tilhører en offentlig nøkkel som er matematisk koblet til en privat nøkkel. For å bruke disse bitcoinene, må man kunne oppfylle transaksjonens betingelse for bruk. En typisk betingelse for bruk innebærer å bevise for resten av nettverket at brukeren er den legitime eieren av den offentlige nøkkelen assosiert med UTXOen. For å gjøre dette, må brukeren demonstrere besittelse av den private nøkkelen som tilsvarer den offentlige nøkkelen koblet til hver UTXO uten å avsløre den private nøkkelen.

Dette er hvor den digitale signaturen kommer inn. Den fungerer som matematisk bevis på besittelse av en privat nøkkel assosiert med en spesifikk offentlig nøkkel. Denne databeskyttelsesteknikken er primært basert på et fascinerende felt innen kryptografi kalt elliptisk kurvekryptografi (ECC).

Signaturen kan matematisk verifiseres av andre deltakere i Bitcoin-nettverket.

![bilde](assets/image/section2/0.webp)

For å sikre sikkerheten til transaksjoner, stoler Bitcoin på to digitale signaturprotokoller: ECDSA (Elliptic Curve Digital Signature Algorithm) og Schnorr. ECDSA har vært en signaturprotokoll integrert i Bitcoin siden lanseringen i 2009, mens Schnorr-signaturer ble lagt til mer nylig i november 2021. Selv om begge protokollene er basert på elliptisk kurvekryptografi og bruker lignende matematiske mekanismer, skiller de seg hovedsakelig i form av signaturstruktur.

I dette kurset vil vi presentere ECDSA-algoritmen.

### Hva er en elliptisk kurve?

Elliptisk kurvekryptografi er et sett med algoritmer som bruker en elliptisk kurve for sine ulike geometriske og matematiske egenskaper i en kryptografisk kontekst, med sikkerhet basert på vanskeligheten med å beregne den diskrete logaritmen.

Elliptiske kurver er nyttige i en rekke kryptografiske applikasjoner i Bitcoin-protokollen, som spenner fra nøkkelutvekslinger til asymmetrisk kryptering og digitale signaturer.

Elliptiske kurver har interessante egenskaper:

- Symmetri: Enhver ikke-vertikal linje som krysser to punkter på den elliptiske kurven, vil krysse kurven ved et tredje punkt.
- Enhver ikke-vertikal linje som er tangent til kurven ved et punkt, vil alltid krysse kurven ved et unikt andre punkt.

Bitcoin-protokollen bruker en spesifikk elliptisk kurve kalt Secp256k1 for sine kryptografiske operasjoner.

Før vi går dypere inn i disse signaturmekanismene, er det viktig å forstå hva en elliptisk kurve er. En elliptisk kurve er definert av ligningen y² = x³ + ax + b. Hvert punkt på denne kurven har en distinkt symmetri som er nøkkelen til dens nytte i kryptografi.

![bilde](assets/image/section2/1.webp)

Til slutt er ulike elliptiske kurver anerkjent som sikre for kryptografisk bruk. Den mest kjente kan være secp256r1-kurven. Men for Bitcoin valgte Satoshi Nakamoto en annen kurve: secp256k1.
Denne kurven er definert av parameterne a=0 og b=7, og dens ligning er y² = x³ + 7 modulo n, der n representerer primtallet som bestemmer kurvens orden.
![bilde](assets/image/section2/2.webp)

Det første bildet representerer secp256k1-kurven over det reelle feltet og dens ligning.
Det andre bildet er en representasjon av secp256k1-kurven over feltet ZP, feltet av positive naturlige tall, modulo p der p er et primtall. Det ser ut som en sky av punkter. Vi bruker dette feltet av positive naturlige tall for å unngå tilnærminger.
p er et primtall, og det er kurvens orden som brukes.
Til slutt er ligningen som brukes i Bitcoin-protokollen:$$
y^2 = (x^3 + 7) mod(p) $$
Ligningen til den elliptiske kurven i Bitcoin tilsvarer den siste ligningen i det forrige bildet.

I neste del av dette kurset vil vi bruke kurver som er på det reelle feltet, kun for å lette forståelsen.

## Beregning av den offentlige nøkkelen fra den private nøkkelen
<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>

For å begynne, la oss dykke inn i verdenen til Elliptic Curve Digital Signature Algorithm (ECDSA). Bitcoin benytter denne digitale signaturalgoritmen for å koble private og offentlige nøkler. I dette systemet er den private nøkkelen et tilfeldig eller pseudo-tilfeldig 256-bits tall. Det totale antallet muligheter for en privat nøkkel er teoretisk 2^256, men i virkeligheten er det litt mindre enn det. For å være nøyaktig, noen 256-bits private nøkler er ikke gyldige for Bitcoin.

For å være kompatibel med Bitcoin, må en privat nøkkel være mellom 1 og n-1, der n representerer ordenen til den elliptiske kurven. Dette betyr at det totale antallet muligheter for en Bitcoin privat nøkkel er nesten lik 1.158 x 10^77. For å sette dette i perspektiv, det er omtrent det samme antallet atomer som er til stede i det observerbare universet.

![bilde](assets/image/section2/3.webp)

Den unike private nøkkelen, betegnet som k, brukes deretter til å bestemme en offentlig nøkkel.

Den offentlige nøkkelen, betegnet som K, er et punkt på den elliptiske kurven som er avledet fra den private nøkkelen ved hjelp av irreversible algoritmer som ECDSA. Når vi har kunnskap om den private nøkkelen, er det veldig enkelt å hente den offentlige nøkkelen, men når vi bare har den offentlige nøkkelen, er det umulig å hente den private nøkkelen. Denne irreversibiliteten er hjørnesteinen i sikkerheten til Bitcoin-lommebøker.

Den offentlige nøkkelen er 512 bits lang ettersom den tilsvarer et punkt på kurven med en x-koordinat på 256 bits og en y-koordinat på 256 bits. Imidlertid kan den komprimeres til et 264-bits tall.

![bilde](assets/image/section2/4.webp)

Generatorenpunktet (G) er punktet på kurven hvorfra alle offentlige nøkler genereres i Bitcoin-protokollen. Det har spesifikke x- og y-koordinater, vanligvis representert i heksadesimalt. For secp256k1 er koordinatene til G, i heksadesimalt:

- `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
- `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8` Dette punktet er nyttig for å utlede alle offentlige nøkler. For å beregne den offentlige nøkkelen K, multipliser punktet G med den private nøkkelen k, slik at: K = k.G

Vi vil nå studere hvordan man legger til og multipliserer punkter på elliptiske kurver.

#### Addisjon og dobling av punkter på elliptiske kurver

##### Legge til to punkter M + L

En av de bemerkelsesverdige egenskapene til elliptiske kurver er at en ikke-vertikal linje som krysser kurven ved to punkter, også vil krysse den ved et tredje punkt, kalt punkt O i vårt eksempel. Denne egenskapen brukes til å bestemme punkt U, som er det motsatte av punkt O.

M + L = U

![bilde](assets/image/section2/5.webp)

##### Legge til et punkt til seg selv = Punktdobling

Å legge til et punkt G til seg selv gjøres ved å tegne en tangent til kurven ved det punktet. Denne tangenten, i henhold til egenskapene til elliptiske kurver, vil krysse kurven ved et annet unikt punkt -J. Det motsatte av dette punktet, J, er resultatet av å legge til punkt G til seg selv.
G + G = J

Faktisk er punkt G utgangspunktet for å beregne alle offentlige nøkler til brukere av Bitcoinsystemet.

![bilde](assets/image/section2/6.webp)

#### Skalarmultiplikasjon på elliptiske kurver

Skalarmultiplikasjon av et punkt med n er ekvivalent med å legge til det punktet til seg selv n ganger.

Likt som med punktdobling, utføres skalarmultiplikasjon av punkt G med et punkt n ved å tegne en tangent til kurven ved punkt G. Denne tangenten, i henhold til egenskapene til elliptiske kurver, vil krysse kurven ved et annet unikt punkt -2G. Det motsatte av dette punktet, 2G, er resultatet av å legge til punkt G til seg selv.

Hvis n = 4, gjentas operasjonen til man når 4G.

![bilde](assets/image/section2/7.webp)

Her er et eksempel på beregning for 3G:

![bilde](assets/image/section2/8.webp)

Disse operasjonene på punkter av en elliptisk kurve er grunnlaget for å beregne offentlige nøkler. Å utlede en offentlig nøkkel ved å kjenne den private nøkkelen er veldig enkelt.
En offentlig nøkkel er et punkt på den elliptiske kurven, det er resultatet av vår addisjon og dobling av punkt G k ganger. Med k = privat nøkkel.

I dette eksemplet:

- Den private nøkkelen k = 4
- Den offentlige nøkkelen K = kG = 4G

![bilde](assets/image/section2/9.webp)

Ved å kjenne den private nøkkelen k, er det enkelt å beregne den offentlige nøkkelen K. Det er imidlertid umulig å hente den private nøkkelen basert på den offentlige nøkkelen. Er dette resultatet av en addisjon eller en dobling av punkter?

I vår neste leksjon vil vi utforske hvordan en digital signatur blir opprettet ved bruk av ECDSA-algoritmen med en privat nøkkel for å bruke bitcoins.

## Signering med den private nøkkelen
<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>

Prosessen med digital signatur er en nøkkelmetode for å bevise at du er innehaveren av en privat nøkkel uten å avsløre den. Dette oppnås ved bruk av ECDSA-algoritmen, som innebærer å bestemme en unik nonce, beregne et spesifikt tall V, og skape en digital signatur bestående av to deler, S1 og S2.
Det er avgjørende å alltid bruke en unik nonce for å unngå sikkerhetsangrep. Et beryktet eksempel på hva som kan skje når denne regelen ikke følges, er hackingen av PlayStation 3, som ble kompromittert på grunn av gjenbruk av nonce.
![](assets/image/section2/10.webp)

Steg:

- Bestem en nonce v, som er et unikt tilfeldig tall.
  Nonce = Nummer Kun Brukt En Gang.
  Den bestemmes av den som utfører signaturen.
- Beregn ved å legge til og doble punkter på en elliptisk kurve fra punkt G, posisjonen til V på den elliptiske kurven.
  Slik at V = v.G
  x og y er koordinatene til V på planet.
- Beregn S1.
  S1 = x mod n med n = kurvens orden og x en koordinat av V på planet.
  Merk: Antallet mulige offentlige nøkler er større enn antallet punkter på den elliptiske kurven i det endelige feltet av positive heltall brukt i Bitcoin.
  Kurvens orden tilsvarer kun de mulighetene som den offentlige nøkkelen kan ta på kurven.
- Beregn S2.
  H(Tx) = Hash av transaksjonen
  k = den private nøkkelen
- Beregn signaturen: sammenkjedningen av S1 + S2.
- Beregn P, beregningen for verifisering av signaturen.
  K = den offentlige nøkkelen

For eksempel, for å oppnå den offentlige nøkkelen 3G, tegner du en tangent til punkt G, beregner motsatt av -G for å oppnå 2G, og deretter legger du til G og 2G. For å utføre en transaksjon, må du bevise at du kjenner tallet 3 ved å låse opp bitcoinsene assosiert med den offentlige nøkkelen 3G.

For å opprette en digital signatur og bevise at du kjenner den private nøkkelen assosiert med den offentlige nøkkelen 3G, beregner du først en nonce, deretter punktet V assosiert med denne noncen (i det gitte eksemplet er det 4G). Deretter beregner du punktet T ved å legge til den offentlige nøkkelen 3G og punktet V, som gir 7G.

![image](assets/image/section2/11.webp)

La oss forenkle prosessen med digital signatur.
I det forrige bildet er den private nøkkelen k = 3.
Vi kan enkelt beregne den offentlige nøkkelen K assosiert med denne private nøkkelen: K = 3G.
Deretter genererer vi en nonce pseudo-tilfeldig: v = 4.
Fra denne noncen er det mulig å beregne V slik at: V = v.G = 4G.

Fra dette punktet V, beregner vi punktet T slik at:
T = t.G = 7G (med t = 7).

Nå er det på tide å fortsette med verifiseringen av den digitale signaturen.

Å verifisere en digital signatur er et avgjørende skritt i bruk av ECDSA-algoritmen, som tillater bekreftelse av autentisiteten til en signert melding uten behov for avsenderens private nøkkel. Her er hvordan det fungerer i detalj:

I vårt eksempel har vi to viktige verdier: t og V.
t er en numerisk verdi (7 i dette eksemplet), og V er et punkt på den elliptiske kurven (representert ved 4G her). Disse verdiene genereres under opprettelsen av den digitale signaturen og sendes deretter sammen med meldingen for å muliggjøre verifisering.

Når verifisereren mottar meldingen, vil de også motta disse to verdiene, t og V.

Her er stegene som verifisereren vil følge for å validere signaturen:

1. Først vil de beregne hashen av meldingen, som vi vil kalle H.
2. Deretter vil de beregne u1 og u2. For å gjøre dette, vil de bruke følgende formler:
- u1 = H /* (S2)^-1 mod n   - u2 = T /* (S2)^-1 mod n
     Der S2 er den andre delen av den digitale signaturen, n er ordenen til den elliptiske kurven, og (S2)^-1 er inversen av S2 mod n.
3. Verifisereren vil deretter beregne et punkt P' på den elliptiske kurven ved hjelp av formelen: P' = u1 _ G + u2 _ K
   - G er generatorens punkt på kurven
   - K er avsenderens offentlige nøkkel
4. Verifisereren vil deretter beregne I', som rett og slett er x-koordinaten til punktet P' modulo n.
5. Til slutt vil verifisereren bekrefte at I' er lik t. Hvis dette er tilfellet, anses signaturen som gyldig. Hvis ikke, er signaturen ugyldig.
Denne prosedyren sikrer at kun avsenderen som besitter den tilsvarende private nøkkelen kunne ha produsert en signatur som passerer denne verifiseringsprosessen.

![bilde](assets/image/section2/12.webp)

I enklere termer:
Personen som produserer signaturen vil gi tallet t (i vårt eksempel, t = 7) og punktet V til personen som verifiserer det.

Det er umulig å bestemme den offentlige nøkkelen eller den private nøkkelen fra tallet 7 og tallet V.

Stegene for å verifisere den digitale signaturen er som følger:

- På kurven legger verifisereren til punktet til den offentlige nøkkelen med punktet V for å hente punktet T'.
- Verifisereren beregner tallet t.G.
- Verifisereren sjekker at resultatet av t.G faktisk er lik tallet T'.

Konklusjonen er at verifisering av en digital signatur er en essensiell prosedyre i Bitcoin-transaksjoner. Det sikrer at den signerte meldingen ikke har blitt endret under overføring og at avsenderen faktisk er innehaveren av den private nøkkelen. Denne digitale autentiseringsteknikken er basert på komplekse matematiske prinsipper, inkludert aritmetikk for elliptiske kurver, samtidig som den opprettholder konfidensialiteten til den private nøkkelen. Det gir et solid sikkerhetsfundament for kryptografiske transaksjoner.

Det sagt, håndteringen av disse nøklene, samt deres opprettelse, er et annet essensielt spørsmål i Bitcoin. Hvordan generere et nytt nøkkelpar? Hvordan organisere et mangfold av nøkler på en sikker og effektiv måte? Hvordan gjenopprette dem om nødvendig?

For å svare på disse spørsmålene og fordype din forståelse av kryptografisikkerhet, vil vårt neste kurs fokusere på konseptet med Hierarkiske Deterministiske Lommebøker (HD-lommebøker) og bruken av mnemoniske fraser. Disse mekanismene tilbyr elegante måter å effektivt håndtere dine kryptovalutanøkler på samtidig som de forbedrer sikkerheten.

# Den mnemoniske frasen
<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>

## Utviklingen av Bitcoin-lommebøker
<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>

Den Hierarkiske Deterministiske Lommeboken, mer kjent som HD-lommeboken, spiller en fremtredende rolle i kryptovalutaøkosystemet. Begrepet "lommebok" kan virke misvisende for de som er nye på dette feltet, da det ikke innebærer å holde penger eller valutaer. I stedet refererer det til en samling av kryptografiske private nøkler.

De tidlige lommebøkene var programvare som grupperte privat bestemte nøkler på en pseudo-tilfeldig måte, men hadde ingen forbindelse mellom dem. Disse lommebøkene kalles "Just a Bunch Of Keys" (JBOK).

Siden nøklene ikke har noen forbindelse mellom dem, er brukeren nødt til å lage en ny sikkerhetskopi for hvert nytt par nøkler som genereres.
Enten brukeren alltid bruker det samme nøkkelparet og kompromitterer konfidensialiteten, eller genererer et nytt nøkkelpar tilfeldig og derfor trenger å lage en ny sikkerhetskopi av disse nøklene.
Imidlertid blir kompleksiteten ved å håndtere disse nøklene balansert av et sett med protokoller kalt Bitcoin Improvement Proposals (BIPs). Disse oppgraderingsforslagene er kjernen i funksjonaliteten og sikkerheten til HD-lommebøker. For eksempel, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), lansert i 2012, revolusjonerte måten disse nøklene genereres og lagres på ved å introdusere konseptet med deterministisk og hierarkisk avledede nøkler. Ideen er å avlede alle nøkler deterministisk og hierarkisk fra et unikt stykke informasjon: frøet. Dette forenkler prosessen med å sikkerhetskopiere disse nøklene samtidig som deres sikkerhetsnivå opprettholdes.
Deretter introduserte [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) en betydelig innovasjon: den 24-ords mnemonic-frasen. Dette systemet transformerte en kompleks og vanskelig-å-huske sekvens av tall til en serie med vanlige ord, noe som gjorde det mye enklere å memorere og lagre. I tillegg foreslo [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) å legge til en ekstra passfrase for å forbedre sikkerheten til individuelle nøkler. Disse påfølgende forbedringene førte til BIP43- og BIP44-standardene, som standardiserte strukturen og hierarkiseringen av HD-lommebøker, og gjorde dem mer tilgjengelige og brukervennlige for allmennheten.

I de følgende seksjonene vil vi dykke dypere inn i hvordan HD-lommebøker fungerer. Vi vil diskutere prinsipper for nøkkelavledning og undersøke de grunnleggende konseptene av entropi og generering av tilfeldige tall, som er essensielle for å sikre sikkerheten til din HD-lommebok.

Oppsummert er det essensielt å fremheve den sentrale rollen til BIP32 og BIP39 i designet og sikkerheten til HD-lommebøker. Disse protokollene tillater generering av flere nøkler fra et enkelt frø, som antas å være et tilfeldig eller pseudo-tilfeldig tall. I dag er disse standardene adoptert av flertallet av kryptovaluta-lommebøker, enten de er dedikert til en enkelt kryptovaluta eller støtter flere typer valutaer.

## Entropi og Tilfeldige Tall
<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>

Viktigheten av privatnøkkelsikkerhet i Bitcoin-økosystemet er ubestridelig. De er faktisk hjørnesteinen som sikrer sikkerheten til Bitcoin-transaksjoner. For å unngå enhver sårbarhet assosiert med forutsigbarhet, må disse nøklene genereres på en virkelig tilfeldig måte, noe som raskt kan bli en arbeidskrevende øvelse. Problemet er at i datavitenskap er det umulig å generere et virkelig tilfeldig tall siden det nødvendigvis er avledet fra en deterministisk prosess; en kode. Derfor er det essensielt å lære om de forskjellige Random Number Generators (RNG). Typene RNG varierer, fra Pseudo-Random Number Generators (PRNG) til True Random Number Generators (TRNG), samt PRNG-er som inkorporerer en kilde til entropi.

Entropi refererer til "uorden"-tilstanden til et system. Fra en ekstern entropi, det vil si en ekstern informasjonskilde, er det mulig å bruke en tilfeldig tallgenerator for å oppnå et tilfeldig tall.

![bilde](assets/image/section3/2.webp)

La oss se på hvordan en Pseudo-Random Number Generator (PRNG) fungerer.

Den tar et frø som inndata, som tilsvarer den interne tilstanden 0.
På denne interne tilstanden blir en transformasjonsfunksjon anvendt, og resultatet, som er et pseudo-tilfeldig tall, tilsvarer den interne tilstanden 1.
På denne interne tilstanden 1, igjen, blir en transformasjonsfunksjon anvendt, noe som resulterer i et nytt tilfeldig tall = intern tilstand 2.
Og så videre.
Hovedulempen er at ethvert identisk frø alltid vil produsere det samme resultatet. Også, hvis vi kjenner resultatet av de innledende transformasjonsfunksjonene, vil vi kunne hente det tilfeldige tallet ved utgangen av prosessen.
Et eksempel på en transformasjonsfunksjon er PBKDF2-funksjonen.

**Oppsummert må en kryptografisk sikker PRNG:**

- være statistisk tilfeldig
- være uforutsigbar
- være motstandsdyktig selv om resultatene avsløres
- ha en tilstrekkelig lang periode

![bilde](assets/image/section3/3.webp)

I tilfellet med Bitcoin genereres private nøkler fra et enkelt stykke informasjon i bunnen av lommeboken. Denne informasjonen muliggjør deterministisk og hierarkisk derivasjon av barne nøkkelpar. Entropi er grunnlaget for hver HD-lommebok, selv om det ikke finnes en standard for å generere dette tilfeldige tallet. Derfor er generering av tilfeldige tall en stor utfordring i sikringen av Bitcoin-transaksjoner.

## Den mnemoniske frasen
<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>

Sikkerheten til en Bitcoin-lommebok er en stor bekymring for alle brukerne. En essensiell måte å sikre sikkerhetskopien av lommeboken på, er å generere en mnemonisk frase basert på entropi og sjekksum.

![bilde](assets/image/section3/5.webp)

For å konvertere entropi til en mnemonisk frase, beregn ganske enkelt sjekksummen av entropien og konkatener entropien og sjekksummen.

Når entropien er generert, brukes SHA256-funksjonen på entropien for å skape en hash.
De første 8 bitene av hashen hentes ut, som er sjekksummen.
Den mnemoniske frasen er resultatet av entropien lagt til sjekksummen.

Sjekksummen sikrer verifiseringen av nøyaktigheten til gjenopprettingsfrasen. Uten denne sjekksummen kan en feil i frasen resultere i opprettelsen av en annen lommebok og derfor tap av midler. Sjekksummen oppnås ved å sende entropien gjennom SHA256-funksjonen og hente de første 8 bitene av hashen.

![bilde](assets/image/section3/6.webp)

Forskjellige standarder eksisterer for den mnemoniske frasen avhengig av størrelsen på entropien. Den mest brukte standarden for en gjenopprettingsfrase på 24 ord er en entropi på 256 bit. Størrelsen på sjekksummen bestemmes ved å dele størrelsen på entropien med 32.

For eksempel genererer en entropi på 256 bit en 8-bit sjekksum. Konkateneringen av entropien og sjekksummen fører deretter til respektive størrelser på 128 bit, 160 bit, osv. Avhengig av størrelsen på entropien, vil gjenopprettingsfrasen bestå av 12 ord for 128 bit, 15 ord for 160 bit, og 24 ord for 256 bit.

**Koding av den mnemoniske frasen:**

![bilde](assets/image/section3/7.webp)

De siste 8 bitene tilsvarer sjekksummen.
Hvert 11-bit segment konverteres til desimal.
Hvert desimal tilsvarer et ord fra en liste over 2048 ord på BIP39. Det er viktig å merke seg at ingen ord har samme rekkefølge av de første fire bokstavene.

Det er essensielt å sikkerhetskopiere den 24-ords gjenopprettingsfrasen for å bevare integriteten til Bitcoin-lommeboken. De to mest brukte standardene er basert på en entropi på 128 eller 256 bit og en konkatenering av 12 eller 24 ord. Å legge til en passfrase er et ekstra alternativ for å forbedre sikkerheten til lommeboken.

Avslutningsvis er generering av en mnemonisk frase for å sikre en Bitcoin-lommebok en avgjørende prosess. Det er viktig å følge standardene for den mnemoniske frasen basert på størrelsen på entropien. Å sikkerhetskopiere den 24-ords gjenopprettingsfrasen er essensielt for å forhindre ethvert tap av midler.

## Passfrasen
<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>
Passordfrasen er et ekstra passord som kan integreres i en Bitcoin-lommebok for å øke sikkerheten. Bruken er valgfri og er opp til brukeren. Ved å legge til vilkårlig informasjon som, sammen med den mnemoniske frasen, tillater beregning av lommebokens seed, forbedrer passordfrasen sikkerheten.

![image](assets/image/section3/8.webp)

Passordfrasen er et valgfritt kryptografisk salt av en størrelse valgt av brukeren. Den forbedrer sikkerheten til en HD-lommebok ved å legge til vilkårlig informasjon som, når den kombineres med den mnemoniske frasen, vil tillate beregning av seeden.

Når den er etablert under opprettelsen av en lommebok, er den nødvendig for derivasjonen av alle lommebokens nøkler. pbkdf2-funksjonen brukes til å generere seeden fra passordfrasen. Denne seeden tillater derivasjonen av alle barnenøkkelparene til lommeboken. Hvis passordfrasen endres, blir Bitcoin-lommeboken helt annerledes.

Passordfrasen er et essensielt verktøy for å forbedre sikkerheten til Bitcoin-lommebøker. Den kan muliggjøre implementeringen av ulike sikkerhetsstrategier. For eksempel kan den brukes til å lage duplikater og lette sikkerhetskopiering av den mnemoniske frasen. Den kan også forbedre sikkerheten til lommeboken ved å redusere risikoene forbundet med tilfeldig generering av den mnemoniske frasen.

En effektiv passordfrase bør være lang (20 til 40 tegn) og variert (bruk av store bokstaver, små bokstaver, tall og symboler). Den bør ikke være direkte relatert til brukeren eller deres miljø. Det er tryggere å bruke en tilfeldig sekvens av tegn enn et enkelt ord som passordfrase.

![image](assets/image/section3/9.webp)

En passordfrase er sikrere enn et enkelt passord. Den ideelle passordfrasen er lang, variert og tilfeldig. Den kan forbedre sikkerheten til en lommebok eller varm programvare. Den kan også brukes til å lage redundante og sikre sikkerhetskopier.

Det er avgjørende å ta vare på sikkerhetskopier av passordfrasen for å unngå å miste tilgangen til lommeboken. En passordfrase er et alternativ for en HD-lommebok. Den kan genereres tilfeldig med terninger eller en annen pseudo-tilfeldig tallgenerator. Det anbefales ikke å memorere en passordfrase eller mnemonisk frase.

I vår neste leksjon vil vi undersøke funksjonen til seeden og det første nøkkelparet generert fra den i detalj. Føl deg fri til å følge dette kurset for å fortsette læringen din. Vi ser frem til å se deg igjen veldig snart.

# Opprettelse av Bitcoin-lommebøker
<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>

## Opprettelse av Seed og Master Key
<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>

I denne delen av kurset vil vi utforske stegene for å derivere en Hierarchical Deterministic Wallet (HD Wallet), som tillater den hierarkiske og deterministiske opprettelsen og forvaltningen av private og offentlige nøkler.

![image](assets/image/section4/0.webp)

Grunnlaget for HD-lommeboken støtter seg på to essensielle elementer: den mnemoniske frasen og passordfrasen (valgfritt ekstra passord). Sammen utgjør de seeden, en alfanumerisk sekvens på 512 bits som fungerer som grunnlaget for å derivere lommebokens nøkler. Fra denne seeden er det mulig å derivere alle barnenøkkelparene til Bitcoin-lommeboken. Seed er nøkkelen som gir tilgang til alle bitcoins assosiert med lommeboken, enten du bruker en passordfrase eller ikke.

![image](assets/image/section4/1.webp)
For å oppnå frøet, brukes pbkdf2-funksjonen (Password-Based Key Derivation Function 2) med den mnemoniske frasen og passfrasen. Utdataen fra pbkdf2 er et 512-bit frø.
Fra frøet er det mulig å bestemme den master private nøkkelen og kjedekoden ved bruk av HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512)-algoritmen. Denne algoritmen krever en melding og en nøkkel som inndata for å generere et resultat. Den master private nøkkelen beregnes fra frøet og frasen "Bitcoin SEED". Denne frasen er identisk for alle derivasjoner av alle HD-lommebøker, noe som sikrer konsistens på tvers av lommebøker.

Opprinnelig var ikke SHA-512-funksjonen implementert i Bitcoin-protokollen, derfor brukes HMAC SHA-512. Bruken av HMAC SHA-512 med frasen "Bitcoin SEED" begrenser brukeren til å generere en lommebok spesifikk for Bitcoin. Resultatet av HMAC SHA-512 er et 512-bit tall, delt inn i to deler: de venstre 256 bitene representerer den master private nøkkelen, mens de høyre 256 bitene representerer master kjedekoden.

![bilde](assets/image/section4/2.webp)

Den master private nøkkelen er foreldrenøkkelen til alle fremtidige nøkler i lommeboken, mens master kjedekoden er involvert i derivasjonen av barnenøkler. Det er viktig å merke seg at det er umulig å derivere et barnenøkkelpar uten å kjenne den tilsvarende kjedekoden til foreldreparet.

Et nøkkelpar i lommeboken består av en privat nøkkel, en offentlig nøkkel og en kjedekode. Kjedekoden introduserer en kilde til tilfeldighet i derivasjonen av barnenøkler og isolerer hvert nøkkelpar for å forhindre lekkasje av informasjon.
Det er viktig å merke seg at den master private nøkkelen er den første private nøkkelen som er avledet fra frøet og har ingen tilknytning til de utvidede nøklene i lommeboken.

I neste leksjon vil vi utforske utvidede nøkler i detalj, som xPub, xPRV, zPub, og forstå hvorfor de brukes og hvordan de er konstruert.

## Utvidede Nøkler
<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>

I denne delen av leksjonen vil vi studere utvidede nøkler (xPub, zPub, yPub) og deres prefikser, som spiller en viktig rolle i derivasjonen av barnenøkler i en Hierarchical Deterministic Wallet (HD Wallet).

![bilde](assets/image/section4/3.webp)

Utvidede nøkler er forskjellige fra master nøkler. En HD-lommebok genererer en mnemonisk frase og et frø for å oppnå master nøkkelen og master kjedekoden. Utvidede nøkler brukes til å derivere barnenøkler og krever både foreldrenøkkelen og den tilsvarende kjedekoden. En utvidet nøkkel kombinerer disse to informasjonsbitene for å forenkle derivasjonsprosessen.

![bilde](assets/image/section4/4.webp)

Utvidede offentlige nøkler kan kun derivere normale barn offentlige nøkler, mens utvidede private nøkler kan derivere både barn offentlige og private nøkler, enten gjennom normal eller hardnet derivasjon. Hardnet derivasjon er derivasjon fra foreldrenes private nøkkel, mens normal derivasjon tilsvarer derivasjon fra foreldrenes offentlige nøkkel.

Bruk av utvidede nøkler med XPUB-prefikset tillater derivasjon av nye adresser uten å gå tilbake til de tilsvarende private nøklene, og gir dermed bedre sikkerhet. Metadataene assosiert med utvidede nøkler gir viktig informasjon om deres rolle og posisjon i nøkkelhierarkiet.
Utvidede nøkler er identifisert av spesifikke prefikser (XPRV, XPUB, YPUB, ZPUB) som indikerer om det er en utvidet privat eller offentlig nøkkel, samt dens spesifikke formål. Metadataene assosiert med en utvidet nøkkel inkluderer versjonen (prefiks), dybden, foreldrenøkkelens fingeravtrykk, indeks, og nyttelast (kjedekode og foreldrenøkkel).
![image](assets/image/section4/5.webp)

Versjonen tilsvarer typen nøkkel: xpub, xprv, ...

Dybden tilsvarer antall derivasjoner mellom foreldre- og barnenøkler siden hovednøkkelen.

Foreldrefingeravtrykket er de første 4 bytene av hash 160 av foreldrenøkkelen.
Indeksen er nummeret på paret som brukes til å generere den utvidede nøkkelen blant dens søsken. (søsken = nøkler av samme dybde) For eksempel, hvis vi ønsker å derivere xpub for vår 3. konto, vil dens indeks være 2 (fordi indeksen starter på 0).

Nyttelasten består av kjedekoden (32 bytes) og foreldrenøkkelen (33 bytes).

Komprimerte offentlige nøkler har en størrelse på 33 bytes, mens rå offentlige nøkler er 512 bits. Komprimerte offentlige nøkler beholder den samme informasjonen som rå nøkler, men med redusert størrelse. Utvidede nøkler har en størrelse på 82 bytes og deres prefiks er representert i base 58 gjennom en konvertering til heksadesimalt. Sjekksummen er beregnet ved bruk av HASH256 hash-funksjonen.

![image](assets/image/section4/6.webp)

Forbedrede derivasjoner starter fra indekser som er potenser av 2 (2^31). Det er interessant å merke seg at de mest brukte prefiksene er xpub og zpub, som henholdsvis tilsvarer legacy-standarder og segwit v1 og segwit v0.

I vår neste leksjon vil vi fokusere på derivasjonen av barnenøkkelpar ved bruk av kunnskapen ervervet om utvidede nøkler og hovednøkkelen til lommeboken.

## Derivasjon av barnenøkkelpar
<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>

Som en påminnelse har vi diskutert beregningen av frøet og hovednøkkelen, som er de første essensielle elementene for den hierarkiske organiseringen og derivasjonen av HD (Hierarchical Deterministic) lommeboken. Frøet, med en lengde på 128 til 256 bits, genereres tilfeldig eller fra en hemmelig frase. Det spiller en deterministisk rolle i derivasjonen av alle andre nøkler. Hovednøkkelen er den første nøkkelen som er avledet fra frøet, og den tillater derivasjonen av alle andre barnenøkkelpar.

Hovedkjedekoden spiller en viktig rolle i gjenopprettingen av lommeboken fra frøet. Det bør bemerkes at alle nøkler avledet fra samme frø vil ha samme hovedkjedekode.

![image](assets/image/section4/7.webp)

Den hierarkiske organiseringen og derivasjonen av HD-lommeboken tilbyr en mer effektiv håndtering av nøkler og lommebokstrukturer. Utvidede nøkler tillater derivasjonen av et barnenøkkelpar fra et foreldrenøkkelpar ved bruk av matematiske beregninger og spesifikke algoritmer.
Det finnes forskjellige typer barnenøkkelpar, inkludert forsterkede nøkler og normale nøkler. Den utvidede offentlige nøkkelen tillater kun derivasjonen av normale barn offentlige nøkler, mens den utvidede private nøkkelen tillater derivasjonen av alle barnenøkler, både offentlige og private, enten de er i normal eller forsterket modus. Hvert nøkkelpar har en indeks som lar dem skilles fra hverandre.

![image](assets/image/section4/8.webp)
Utviklingen av barne nøkler bruker HMAC-SHA512-funksjonen ved å bruke den overordnede nøkkelen sammenkjedet med indeksen og kjedekoden som er assosiert med nøkkelparet. Normale barne nøkler har en indeks som varierer fra 0 til 2 opphøyd i 31 minus 1, mens forsterkede barne nøkler har en indeks som varierer fra 2 opphøyd i 31 til 2 opphøyd i 32 minus 1.
![bilde](assets/image/section4/9.webp)

![bilde](assets/image/section4/10.webp)

Det er to typer barne nøkkelpar: forsterkede par og normale par. Prosessen med å utlede barne nøkler bruker offentlige nøkler for å generere betingelser for bruk, mens private nøkler brukes for signering. Den utvidede offentlige nøkkelen tillater kun utledning av normale barne offentlige nøkler, mens den utvidede private nøkkelen tillater utledning av alle barne nøkler, både offentlige og private, i normal eller forsterket modus.

![bilde](assets/image/section4/11.webp)
![bilde](assets/image/section4/12.webp)

Forsterket utledning bruker den overordnede private nøkkelen, mens normal utledning bruker den overordnede offentlige nøkkelen. HMAC-SHA512-funksjonen brukes for forsterket utledning, mens normal utledning bruker et 512-bits sammendrag. Den barne offentlige nøkkelen oppnås ved å multiplisere den barne private nøkkelen med elliptisk kurvegenerator.

![bilde](assets/image/section4/13.webp)
![bilde](assets/image/section4/14.webp)

Hierarkisk utledning og deterministisk utledning av mange nøkkelpar tillater opprettelsen av en trestruktur for hierarkisk utledning. I neste leksjon av denne opplæringen vil vi studere strukturen til HD-lommeboken samt utledningsveier, med et spesielt fokus på notasjoner for utledningsvei.

## Lommebokstruktur og Utledningsveier
<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>

I dette kapittelet vil vi studere strukturen til utledningstreet i en Hierarkisk Deterministisk Lommebok (HD Wallet). Vi har allerede utforsket beregning av frø, hovednøkkelen og utledningen av barne nøkkelpar. Nå vil vi fokusere på organisering av nøkler innenfor lommeboken.

HD-lommeboken bruker dybdenivåer for å organisere nøkler. Hver utledning fra et foreldrepar til et barne par tilsvarer et dybdenivå.

![bilde](assets/image/section4/15.webp)

- Dybde 0 tilsvarer hovednøkkelen og hovedkjedekoden.

- Dybde 1 brukes til å utlede barne nøkler for et spesifikt formål, bestemt av indeksen. Formålene overholder BIP 84 og Segwit v0/v1-standardene.

- Dybde 2 tillater differensiering av kontoer for forskjellige kryptovalutaer eller nettverk. Dette tillater organisering av lommeboken basert på forskjellige kilder til midler. For bitcoin vil indeksen være 0.

- Dybde 3 brukes til å organisere lommeboken i forskjellige kontoer, noe som gir en klarere og mer organisert struktur.

- Dybde 4 tilsvarer de eksterne og interne kjedene, som brukes for adresser ment for offentlig kommunikasjon. Indeks 0 er assosiert med den eksterne kjeden, mens indeks 1 er assosiert med den interne kjeden. Hver konto har to kjeder: den eksterne kjeden (0) og den interne kjeden (1). Dybde 4 brukes også til å håndtere skripttyper i tilfelle av multisignatur-lommebøker.

- Dybde 5 brukes for mottaksadresser i en standard lommebok. I neste seksjon vil vi undersøke utledningen av barne nøkkelpar mer detaljert.

![bilde](assets/image/section4/16.webp)

For hvert dybdenivå bruker vi indekser for å differensiere barne nøkkelpar.
Indeksen uten apostrof tilsvarer den faktisk brukte indeksen, mens indeksen med apostrof tilsvarer den faktiske indeksen + 2^31. Herdede derivasjoner bruker indekser fra 2^31 til 2^32-1. For eksempel, indeks 44' tilsvarer den faktiske indeksen 2^31 + 44.
For å generere en spesifikk mottaksadresse, deriverer vi et barnenøkkelpar fra hovednøkkelen og hovedkjedekoden. Deretter bruker vi indeksen for å skille mellom forskjellige barnenøkkelpar på samme dybde.

Utvidede nøkler, som XPUB, lar deg dele lommeboken din med flere personer. Derivasjonsstien brukes for å skille mellom den eksterne kjeden (adresser ment for å deles) og den interne kjeden (vexeladresser).

I neste kapittel skal vi studere mottaksadresser, deres fordeler ved bruk, og trinnene som er involvert i deres konstruksjon.

# Hva er en Bitcoin-adresse?
<partId>81ec8d17-f8ee-5aeb-8035-d370866f4281</partId>

## Bitcoin-adresser
<chapterId>0a887ed8-3424-5a52-98e1-e4b406150475</chapterId>

I dette kapittelet skal vi utforske mottaksadresser, som spiller en avgjørende rolle i Bitcoin-systemet. De tillater midler å bli mottatt i en transaksjon og genereres fra par av private og offentlige nøkler. Selv om det finnes en skripttype kalt Pay2PublicKey som lar bitcoins bli låst til en offentlig nøkkel, foretrekker brukere generelt å bruke mottaksadresser i stedet for dette skriptet.

![bilde](assets/image/section5/0.webp)

Når en mottaker ønsker å motta bitcoins, gir de en mottaksadresse til avsenderen i stedet for sin offentlige nøkkel. En adresse er faktisk en hash av en offentlig nøkkel, med et spesifikt format. Den offentlige nøkkelen er avledet fra den private barnenøkkelen ved hjelp av matematiske operasjoner som punktlegging og dobling på elliptiske kurver.

![bilde](assets/image/section5/1.webp)

Det er viktig å merke seg at det ikke er mulig å reversere fra en adresse til den offentlige nøkkelen, eller fra den offentlige nøkkelen til den private nøkkelen. Bruk av en adresse reduserer størrelsen på den offentlige nøkkelinformasjonen, som opprinnelig er 512 bits.

Bitcoin-adresser har blitt redusert i størrelse for å lette deres bruk. De har en kontrollsum, som muliggjør oppdagelse av skrivefeil og reduserer risikoen for å miste bitcoins. På den annen side har ikke offentlige nøkler en kontrollsum, noe som betyr at skrivefeil kan resultere i tap av tilsvarende midler.

Adresser gir også et andre lag med sikkerhet mellom offentlig og privat informasjon, noe som gjør det vanskeligere å ta kontroll over den private nøkkelen.

Det er essensielt å understreke at hver adresse bør brukes kun én gang. Gjenbruk av samme adresse medfører personvernproblemer og bør unngås.

Forskjellige prefikser brukes for Bitcoin-adresser. For eksempel, BC1Q tilsvarer en Segwit V0-adresse, BC1P til en Taproot/Segwit V1-adresse, og prefiksene 1 og 3 er assosiert med Pay2PublicKeyH/Pay2ScriptH (legacy) adresser. I neste leksjon vil vi forklare trinn for trinn hvordan man kan avlede en adresse fra en offentlig nøkkel.

## Hvordan lage en Bitcoin-adresse?
<chapterId>6dee7bf3-7767-5f8d-a01b-659b95cfe0a5</chapterId>

I dette kapittelet skal vi diskutere konstruksjonen av en mottaksadresse for Bitcoin-transaksjoner. En mottaksadresse er en alfanumerisk representasjon av en komprimert offentlig nøkkel. Konverteringen av en offentlig nøkkel til en mottaksadresse involverer flere trinn.

### Trinn 1: Komprimering av den offentlige nøkkelen
![bilde](assets/image/section5/14.webp)
En adresse er avledet fra en barn offentlig nøkkel.

En offentlig nøkkel er et punkt på den elliptiske kurven. Takket være symmetrien til den elliptiske kurven, vil et punkt på den elliptiske kurven ha en x-koordinat assosiert med kun to mulige verdier for y: positiv eller negativ.
Imidlertid, i Bitcoin-protokollen, jobber vi med et endelig sett av positive heltall i stedet for med settet av reelle tall. For å skille mellom de to mulige verdiene av y, er det tilstrekkelig å indikere om y er partall eller oddetall.

Komprimeringen av en offentlig nøkkel reduserer størrelsen fra 520 bits til 264 bits.

Vi bruker prefikset 0x02 for et partall y og 0x03 for et oddetall y. Dette er den komprimerte formen av den offentlige nøkkelen.

### Steg 2: Hashing av den komprimerte offentlige nøkkelen

![bilde](assets/image/section5/3.webp)

Hashing av den komprimerte offentlige nøkkelen utføres ved bruk av SHA256-funksjonen. Deretter påføres RIPEMD160-funksjonen på digesten.

### Steg 3: Nyttelasten = Adresse nyttelast

![bilde](assets/image/section5/4.webp)

Den binære digesten av RIPEMD160(SHA256(K)) brukes til å danne grupper av 5 bits. Hver gruppe transformeres til base16 (Heksadesimal) og/eller base 10.

### Steg 4: Legge til metadata for sjekksumberegning med BCH-programmet

![bilde](assets/image/section5/5.webp)

I tilfellet med legacy-adresser bruker vi dobbel SHA256-hashing for å generere adressens sjekksum. Imidlertid, for Segwit V0 og V1-adresser, stoler vi på BCH-sjekksumteknologien for å sikre feildeteksjon. BCH-programmet er i stand til å foreslå og korrigere feil med en ekstremt lav sannsynlighet for feil. For øyeblikket brukes BCH-programmet til å oppdage og foreslå endringer som skal gjøres, men det utfører dem ikke automatisk på vegne av brukeren.

BCH-programmet krever flere inngangsinformasjoner, inkludert HRP (Human Readable Part) som trenger å bli utvidet. Utvidelse av HRP innebærer koding av hver bokstav i base 2 i henhold til deres ASCII-kode. Deretter, ved å ta de første 3 bitene av resultatet for hver bokstav og konvertere dem til base 10 (i blått på bildet). Sett inn en separator 0. Deretter konkatener de følgende 5 bitene av hver bokstav tidligere konvertert til base 10 (i gult på bildet).

Utvidelse av HRP i base 10 tillater isolering av de siste fem bitene av hver karakter, og dermed forsterke sjekksummen.

Segwit V0-versjonen er representert ved koden 00 og "nyttelasten" er i svart, i base 10. Dette følges av seks reserverte tegn for sjekksummen.

### Steg 5: Beregning av sjekksummen med BCH-programmet

![bilde](assets/image/section5/6.webp)

Inndataene som inneholder metadataene blir deretter sendt inn til BCH-programmet for å oppnå sjekksummen i base 10.

Her har vi sjekksummen.

### Steg 6: Adressekonstruksjon og konvertering til Bech32

![bilde](assets/image/section5/7.webp)

Konkateneringen av versjonen, nyttelasten og sjekksummen tillater bygging av adressen. Tegnene i base 10 konverteres deretter til Bech32-tegn ved hjelp av en korrespondansetabell. Bech32-alfabetet inkluderer alle alfanumeriske tegn, unntatt 1, b, i og o, for å unngå forvirring.

### Steg 7: Legge til HRP og separator

![bilde](assets/image/section5/8.webp)

I rosa, sjekksummen.
I svart, lasten = hashen av den offentlige nøkkelen. I blått, versjonen.

Alt konverteres til Bech32, deretter legges 'bc' til for bitcoin og '1' som en separator, og her er adressen.

# Gå videre
<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>

## Lage et frø fra 128 terningkast!
<chapterId>0f4d40a7-cf0e-5faf-bc4d-691486771ac1</chapterId>

Å lage en mnemonic frase er et avgjørende skritt i å sikre din kryptovaluta-lommebok. Det finnes flere metoder for å generere en mnemonic frase, men vi vil fokusere på den manuelle genereringsmetoden ved bruk av terninger. Det er viktig å merke seg at denne metoden ikke er egnet for en lommebok med høy verdi. Det anbefales å bruke åpen kildekode-programvare eller en maskinvarelommebok for å generere mnemonic frasen. For å lage en mnemonic frase, vil vi bruke terninger for å generere binær informasjon. Målet er å forstå prosessen med å lage mnemonic frasen.

**Steg 1 - Forberedelse:**
Sørg for at du har en amnesisk Linux-distribusjon, som Tails OS, installert på en USB-nøkkel for ekstra sikkerhet. Merk at denne veiledningen ikke bør brukes til å lage en hovedlommebok.
**Steg 2 - Generere et tilfeldig binært tall:**
Vi vil bruke terninger for å generere binær informasjon. Kast en terning 128 ganger og registrer hvert resultat (1 for oddetall, 0 for partall).

**Steg 3 - Organisere binære tall:**
Organiser de oppnådde binære tallene i rader med 11 sifre for å lette videre beregninger. Den tolvte raden skal kun ha 7 sifre.

**Steg 4 - Beregne kontrollsummen:**
De siste 4 sifrene for den tolvte raden tilsvarer kontrollsummen. For å beregne denne kontrollsummen, trenger vi å bruke en terminal fra en Linux-distribusjon. Det anbefales å bruke [TailOs](https://tails.boum.org/index.fr.html), som er en oppstartbar minneløs distribusjon fra en USB-nøkkel. Når du er på terminalen din, skriv inn kommandoen `echo <binært tall> | shasum -a 254 -0`. Erstatt `<binært tall>` med din liste over 128 nuller og enere. Utdataen er en heksadesimal hash. Noter det første tegnet av denne hashen og konverter det til binært. Du kan bruke denne [tabellen](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) for hjelp. Legg til den binære kontrollsummen (4 sifre) til den tolvte raden på arket ditt.

**Steg 5 - Konvertering til desimal:**
For å finne ordene som er assosiert med hver av radene dine, må du først konvertere hver serie på 11 bits til desimaltall. Her kan du ikke bruke en nettbasert konverter fordi disse bitene representerer din mnemonic-frase. Derfor må du konvertere ved hjelp av en kalkulator og et triks som følger: hver bit er assosiert med en potens av 2, så fra venstre mot høyre har vi 11 rangeringer som tilsvarer 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. For å konvertere din serie på 11 bits til desimaltall, legger du ganske enkelt sammen kun rangeringene som inneholder en 1. For eksempel, for serien 00110111011, tilsvarer dette følgende addisjon: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Du kan nå konvertere hver rad til desimaltall. Og før du går videre til koding i ord, legg til +1 til alle radene fordi indeksen til BIP39-ordlisten starter fra 1, ikke 0.
**Steg 8 - Generering av mnemonic-frasen:**
Start med å skrive ut [listen over 2048 ord](https://seedxor.com/files/wordlist.pdf) for å konvertere mellom dine desimaltall og BIP39-ordene. Det unike med denne listen er at intet ord deler de første 4 bokstavene med noe annet ord i denne ordboken. Søk deretter etter ordet som er assosiert med hvert av dine raders desimaltall.
**Steg 9 - Test av mnemonic-frasen:**
Test umiddelbart din mnemonic-frase på Sparrow Wallet ved å opprette en lommebok fra den. Hvis du mottar en feilmelding om ugyldig kontrollsum, er det sannsynlig at du har gjort en regnefeil. Rett opp denne feilen ved å gå tilbake til steg 4 og test igjen på Sparrow Wallet. Voilà! Du har nettopp opprettet en ny Bitcoin-lommebok fra 128 terningkast.

Å generere en mnemonic-frase er en viktig prosess for å sikre din kryptovaluta-lommebok. Det anbefales å bruke sikrere metoder, som å bruke åpen kildekode-programvare eller en maskinvarelommebok, for å generere mnemonic-frasen. Imidlertid hjelper det å fullføre dette verkstedet til å bedre forstå hvordan vi kan opprette en Bitcoin-lommebok fra et tilfeldig tall.

## BONUS: Intervju med Théo Pantamis
<chapterId>39f0ec5a-e258-55cb-9789-bc46d314d816</chapterId>

En annen mye brukt kryptografisk metode i Bitcoin-protokollen er metoden for digitale signaturer.

![video](https://youtu.be/c9MvtGJsEvY?si=bQ1N5NCd6op0G6nW)

## Evaluer kurset
<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>
<isCourseReview>true</isCourseReview>

## Avsluttende eksamen
<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>
<isCourseExam>true</isCourseExam>

## Konklusjon og avslutning
<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

### Takk og fortsett å utforske kaninhullet

Vi vil gjerne takke deg oppriktig for at du fullførte Crypto 301-kurset. Vi håper denne opplevelsen har vært berikende og lærerik for deg. Vi har dekket mange spennende emner, fra matematikk til kryptografi til hvordan Bitcoin-protokollen fungerer.
Hvis du ønsker å fordype deg ytterligere i emnet, har vi en ekstra ressurs å tilby deg. Vi gjennomførte et eksklusivt intervju med Théo Pantamis og Loïc Morel, to anerkjente eksperter innen kryptografi. Dette intervjuet utforsker ulike aspekter av emnet i dybden og gir interessante perspektiver.
Føl deg fri til å se dette intervjuet for å fortsette utforskingen av det fascinerende feltet kryptografi. Vi håper det vil være nyttig og inspirerende på din reise. Igjen, takk for din deltakelse og engasjement gjennom dette kurset.

### Støtt Oss

Dette kurset, sammen med alt innholdet på denne universiteten, har blitt tilbudt deg gratis av vårt fellesskap. For å støtte oss, kan du dele det med andre, bli medlem av universitetet, og til og med bidra til utviklingen via GitHub. På vegne av hele teamet, takk!

### Vurder kurset

Et vurderingssystem for opplæringen vil snart bli integrert i denne nye E-læringsplattformen! I mellomtiden, tusen takk for at du tok kurset, og hvis du likte det, vennligst vurder å dele det med andre.