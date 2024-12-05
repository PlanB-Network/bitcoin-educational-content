---
name: Det indre arbeidet til Bitcoin-lommebøker
goal: Dykk ned i de kryptografiske prinsippene som driver Bitcoin-lommebøker.
objectives:
  - Definere de teoretiske begrepene som er nødvendige for å forstå de kryptografiske algoritmene brukt i Bitcoin.
  - Fullt ut forstå konstruksjonen av en deterministisk og hierarkisk lommebok.
  - Vite hvordan man identifiserer og reduserer risikoene forbundet med å håndtere en lommebok.
  - Forstå prinsippene for hash-funksjoner, kryptografiske nøkler og digitale signaturer.
---

# En reise inn i hjertet av Bitcoin-lommebøker

Oppdag hemmelighetene til deterministiske og hierarkiske Bitcoin-lommebøker med vårt CYP201-kurs! Enten du er en vanlig bruker eller en entusiast som ser etter å fordype din kunnskap, tilbyr dette kurset en komplett fordypning i arbeidet til disse verktøyene som vi alle bruker daglig.

Lær om mekanismene til hash-funksjoner, digitale signaturer (ECDSA og Schnorr), mnemoniske fraser, kryptografiske nøkler og opprettelsen av mottaksadresser, alt mens du utforsker avanserte sikkerhetsstrategier.

Dette opplæringen vil ikke bare utstyre deg med kunnskapen til å forstå strukturen til en Bitcoin-lommebok, men vil også forberede deg til å dykke dypere inn i den spennende verdenen av kryptografi.

Med klar pedagogikk, over 60 forklarende diagrammer og konkrete eksempler, vil CYP201 gjøre det mulig for deg å forstå fra A til Å hvordan lommeboken din fungerer, slik at du kan navigere Bitcoin-universet med selvtillit. Ta kontroll over dine UTXOer i dag ved å forstå hvordan HD-lommebøker fungerer!

+++

# Introduksjon

<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>

## Kursintroduksjon

<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>

Velkommen til CYP201-kurset, hvor vi vil utforske HD Bitcoin-lommebøker i dybden. Dette kurset er designet for alle som ønsker å forstå de tekniske grunnleggende om å bruke Bitcoin, enten de er tilfeldige brukere, opplyste entusiaster eller fremtidige eksperter.

Målet med denne opplæringen er å gi deg nøklene til å mestre verktøyene du bruker daglig. HD Bitcoin-lommebøker, som er i hjertet av brukeropplevelsen din, er basert på noen ganger komplekse konsepter, som vi vil forsøke å gjøre tilgjengelige. Sammen vil vi avmystifisere dem!

Før vi dykker ned i detaljene om konstruksjonen og driften av Bitcoin-lommebøker, vil vi starte med noen kapitler om de kryptografiske primitivene å vite for det som følger.
Vi starter med kryptografiske hash-funksjoner, grunnleggende for både lommebøker og Bitcoin-protokollen selv. Du vil oppdage deres viktigste egenskaper, de spesifikke funksjonene brukt i Bitcoin, og i et mer teknisk kapittel, vil du lære i detalj om arbeidet til dronningen av hash-funksjoner: SHA256.
![CYP201](assets/fr/010.webp)

Deretter vil vi diskutere driften av digitale signaturalgoritmer som du bruker hver dag for å sikre dine UTXOer. Bitcoin bruker to: ECDSA og Schnorr-protokollen. Du vil lære hvilke matematiske primitiver som ligger til grunn for disse algoritmene og hvordan de sikrer transaksjonenes sikkerhet.

![CYP201](assets/fr/021.webp)

Når vi har en god forståelse av disse elementene av kryptografi, vil vi endelig gå videre til hjertet av opplæringen: deterministiske og hierarkiske lommebøker! Først er det en seksjon dedikert til mnemoniske fraser, disse sekvensene av 12 eller 24 ord som lar deg opprette og gjenopprette lommebøkene dine. Du vil oppdage hvordan disse ordene genereres fra en kilde til entropi og hvordan de letter bruken av Bitcoin.

![CYP201](assets/fr/040.webp)
Opplæringen vil fortsette med studiet av BIP39-passfrasen, seeden (ikke å forveksle med den mnemoniske frasen), hovedkjedekoden og hovednøkkelen. Vi vil se i detalj hva disse elementene er, deres respektive roller, og hvordan de beregnes.
![CYP201](assets/fr/045.webp)

Til slutt, fra hovednøkkelen, vil vi oppdage hvordan kryptografiske nøkkelpar er avledet på en deterministisk og hierarkisk måte opp til mottaksadressene.

![CYP201](assets/fr/056.webp)

Denne opplæringen vil gjøre deg i stand til å bruke lommebokprogramvaren din med tillit, samtidig som du forbedrer dine ferdigheter til å identifisere og redusere risikoer. Forbered deg på å bli en ekte ekspert på Bitcoin-lommebøker!

# Hashfunksjoner

<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>

## Introduksjon til Hashfunksjoner

<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>

Den første typen kryptografiske algoritmer brukt på Bitcoin omfatter hashfunksjoner. De spiller en essensiell rolle på forskjellige nivåer av protokollen, men også innenfor Bitcoin-lommebøker. La oss sammen oppdage hva en hashfunksjon er og hva den brukes til i Bitcoin.

### Definisjon og Prinsipp for Hashing

Hashing er en prosess som transformerer informasjon av vilkårlig lengde til et annet stykke informasjon av fast lengde gjennom en kryptografisk hashfunksjon. Med andre ord tar en hashfunksjon en inndata av hvilken som helst størrelse og konverterer den til et fingeravtrykk av fast størrelse, kalt en "hash".
Hashen kan også noen ganger refereres til som "digest", "condensate", "condensed", eller "hashed".

For eksempel produserer SHA256-hashfunksjonen en hash av en fast lengde på 256 bits. Så, hvis vi bruker inndataen "_PlanB_", en melding av vilkårlig lengde, vil den genererte hashen være følgende 256-bits fingeravtrykk:

```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```

![CYP201](assets/fr/001.webp)

### Egenskaper ved Hashfunksjoner

Disse kryptografiske hashfunksjonene har flere essensielle egenskaper som gjør dem spesielt nyttige i konteksten av Bitcoin og andre datasystemer:

1. Irreversibilitet (eller preimage-motstand)
2. Manipulasjonsmotstand (snøskredseffekt)
3. Kollisjonsmotstand
4. Sekundær preimage-motstand

#### 1. Irreversibilitet (preimage-motstand):

Irreversibilitet betyr at det er enkelt å beregne hashen fra inndatainformasjonen, men den inverse beregningen, det vil si å finne inndataen fra hashen, er praktisk talt umulig. Denne egenskapen gjør hashfunksjoner perfekte for å skape unike digitale fingeravtrykk uten å kompromittere den opprinnelige informasjonen. Denne karakteristikken omtales ofte som en enveisfunksjon eller en "_felle dør-funksjon_".

I det gitte eksemplet er det enkelt og raskt å oppnå hashen `24f1b9…` ved å kjenne inndataen "_PlanB_". Imidlertid er det umulig å finne meldingen "_PlanB_" ved kun å kjenne `24f1b9…`.

![CYP201](assets/fr/002.webp)

Derfor er det umulig å finne et preimage $m$ for en hash $h$ slik at $h = \text{HASH}(m)$, hvor $\text{HASH}$ er en kryptografisk hashfunksjon.

#### 2. Manipulasjonsmotstand (snøskredseffekt)

Det andre kjennetegnet er motstandsdyktighet mot manipulering, også kjent som **snøballeffekten**. Dette kjennetegnet observeres i en hash-funksjon hvis en liten endring i inngangsmeldingen resulterer i en radikal endring i utgangshashen.
Hvis vi går tilbake til eksemplet vårt med inngangen "_PlanB_" og SHA256-funksjonen, har vi sett at den genererte hashen er som følger:

```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```

Hvis vi gjør en veldig liten endring til inngangen ved å bruke "_Planb_" denne gangen, så endrer simpelthen endringen fra en stor "B" til en liten "b" helt den utgitte SHA256-hashen:

```text
bb038b4503ac5d90e1205788b00f8f314583c5e22f72bec84b8735ba5a36df3f
```

![CYP201](assets/fr/003.webp)

Denne egenskapen sikrer at selv en mindre endring av den opprinnelige meldingen umiddelbart er oppdagbar, da den ikke bare endrer en liten del av hashen, men hele hashen. Dette kan være av interesse i ulike felt for å verifisere integriteten til meldinger, programvare eller til og med Bitcoin-transaksjoner.

#### 3. Kollisjonsresistens

Det tredje kjennetegnet er kollisjonsresistens. En hash-funksjon er kollisjonsresistent hvis det er beregningsmessig umulig å finne 2 forskjellige meldinger som produserer samme hash-utgang fra funksjonen. Formelt sett er det vanskelig å finne to distinkte meldinger $m_1$ og $m_2$ slik at:

$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$

![CYP201](assets/fr/004.webp)

I virkeligheten er det matematisk uunngåelig at kollisjoner eksisterer for hash-funksjoner, fordi størrelsen på inngangene kan være større enn størrelsen på utgangene. Dette er kjent som Dirichlets skuffprinsipp: hvis $n$ objekter distribueres i $m$ skuffer, med $m < n$, så vil minst en skuff nødvendigvis inneholde to eller flere objekter. For en hash-funksjon gjelder dette prinsippet fordi antallet mulige meldinger er (nesten) uendelig, mens antallet mulige hasher er endelig ($2^{256}$ i tilfellet med SHA256).

Dermed betyr ikke dette kjennetegnet at det ikke finnes kollisjoner for hash-funksjoner, men heller at en god hash-funksjon gjør sannsynligheten for å finne en kollisjon ubetydelig. Dette kjennetegnet, for eksempel, er ikke lenger verifisert på SHA-0 og SHA-1 algoritmene, forgjengerne til SHA-2, for hvilke kollisjoner har blitt funnet. Disse funksjonene er derfor nå frarådet og ofte ansett som foreldet.
For en hash-funksjon på $n$ bits, er kollisjonsresistensen av orden $2^{\frac{n}{2}}$, i samsvar med bursdagsangrepet. For eksempel, for SHA256 ($n = 256$), er kompleksiteten av å finne en kollisjon av orden $2^{128}$ forsøk. I praktiske termer betyr dette at hvis man passerer $2^{128}$ forskjellige meldinger gjennom funksjonen, er man sannsynlig å finne en kollisjon.

#### 4. Motstand mot Sekundært Prebilde

Motstand mot sekundært prebilde er et annet viktig kjennetegn ved hash-funksjoner. Det hevder at gitt en melding $m_1$ og dens hash $h$, er det beregningsmessig uoverkommelig å finne en annen melding $m_2 \neq m_1$ slik at:

$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$

Derfor er motstand mot sekundært prebilde noe lik kollisjonsresistens, bortsett fra at her er angrepet vanskeligere fordi angriperen ikke fritt kan velge $m_1$.

### Bruk av Hashfunksjoner i Bitcoin

Den mest brukte hashfunksjonen i Bitcoin er **SHA256** ("_Secure Hash Algorithm 256 bits"_). Designet på begynnelsen av 2000-tallet av NSA og standardisert av NIST, produserer den et 256-bit hashresultat.

Denne funksjonen brukes i mange aspekter av Bitcoin. På protokollnivå er den involvert i Proof-of-Work-mekanismen, hvor den brukes i dobbel hashing for å søke etter en delvis kollisjon mellom headeren til en kandidatblokk, skapt av en miner, og vanskelighetsmålet. Hvis denne delvise kollisjonen blir funnet, blir kandidatblokken gyldig og kan legges til i blockchain.

SHA256 brukes også i konstruksjonen av et Merkle-tre, som er akkumulatoren brukt for å registrere transaksjoner i blokker. Denne strukturen finnes også i Utreexo-protokollen, som tillater reduksjon av størrelsen på UTXO-settet. I tillegg, med introduksjonen av Taproot i 2021, blir SHA256 utnyttet i MAST (_Merkelised Alternative Script Tree_), som tillater å avsløre kun de brukte utgiftsbetingelsene i et skript, uten å avsløre de andre mulige alternativene. Den brukes også i beregningen av transaksjonsidentifikatorer, i overføring av pakker over P2P-nettverket, i elektroniske signaturer... Til slutt, og dette er av spesiell interesse i denne opplæringen, brukes SHA256 på applikasjonsnivå for konstruksjonen av Bitcoin-lommebøker og derivasjon av adresser.

De fleste ganger, når du kommer over bruken av SHA256 på Bitcoin, vil det faktisk være en dobbel hash SHA256, notert "**HASH256**", som ganske enkelt består av å anvende SHA256 to ganger suksessivt:
HASH256(m) = SHA256(SHA256(m))

Denne praksisen med dobbel hashing legger til et ekstra lag med sikkerhet mot visse potensielle angrep, selv om en enkelt SHA256 i dag anses som kryptografisk sikker.

En annen hashfunksjon tilgjengelig i Script-språket og brukt for å utlede mottaksadresser er RIPEMD160-funksjonen. Denne funksjonen produserer et 160-bit hash (altså kortere enn SHA256). Den kombineres generelt med SHA256 for å danne HASH160-funksjonen:

$$
\text{HASH160}(m) = \text{RIPEMD160}(\text{SHA256}(m))
$$

Denne kombinasjonen brukes til å generere kortere hasher, spesielt i opprettelsen av visse Bitcoin-adresser som representerer hasher av nøkler eller skript-hasher, samt for å produsere nøkkelfingeravtrykk.

Til slutt, kun på applikasjonsnivå, brukes noen ganger også SHA512-funksjonen, som indirekte spiller en rolle i nøkkelderivasjon for lommebøker. Denne funksjonen er veldig lik SHA256 i sin operasjon; begge tilhører samme SHA2-familie, men SHA512 produserer, som navnet indikerer, en 512-bit hash, sammenlignet med 256 bits for SHA256. Vi vil detaljere bruken av den i de følgende kapitlene.

Du kjenner nå til de grunnleggende prinsippene om hashfunksjoner for det som følger. I neste kapittel foreslår jeg å oppdage mer detaljert hvordan funksjonen som er hjertet av Bitcoin: SHA256, fungerer. Vi vil dissekere den for å forstå hvordan den oppnår de karakteristikkene vi har beskrevet her. Dette neste kapittelet er ganske langt og teknisk, men det er ikke essensielt å følge resten av opplæringen. Så, hvis du har vanskeligheter med å forstå det, ikke bekymre deg og gå direkte til det følgende kapittelet, som vil være mye mer tilgjengelig.

## Detaljene i SHA256

<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>
Vi har tidligere sett at hash-funksjoner har viktige egenskaper som rettferdiggjør deres bruk i Bitcoin. La oss nå undersøke de interne mekanismene til disse hash-funksjonene som gir dem disse egenskapene, og for å gjøre dette, foreslår jeg å dissekere driften av SHA256.
SHA256 og SHA512-funksjonene tilhører samme SHA2-familie. Deres mekanisme er basert på en spesifikk konstruksjon kalt **Merkle-Damgård konstruksjonen**. RIPEMD160 bruker også denne samme typen konstruksjon.

Som en påminnelse, vi har en melding av vilkårlig størrelse som input til SHA256, og vi vil sende den gjennom funksjonen for å oppnå en 256-bit hash som output.

### Forbehandling av input

For å begynne, må vi forberede vår inputmelding $m$ slik at den har en standard lengde som er et multiplum av 512 bits. Dette steget er avgjørende for den korrekte funksjonen av algoritmen etterpå.
For å gjøre dette, starter vi med padding bits-steget. Vi legger først til et separatorbit `1` til meldingen, etterfulgt av et visst antall `0` bits. Antallet `0` bits som legges til, beregnes slik at den totale lengden på meldingen etter denne tilleggingen er kongruent med 448 modulo 512. Dermed er lengden $L$ på meldingen med padding bits lik:

$$
L \equiv 448 \mod 512
$$

$\text{mod}$, for modulo, er en matematisk operasjon som, mellom to heltall, returnerer resten av den euklidiske divisjonen av den første ved den andre. For eksempel: $16 \mod 5 = 1$. Det er en operasjon som er mye brukt i kryptografi.

Her sikrer padding-steget at, etter å ha lagt til 64 bits i neste steg, vil den totale lengden på den likestilte meldingen være et multiplum av 512 bits. Hvis den opprinnelige meldingen har en lengde på $M$ bits, er antallet ($N$) av `0` bits som skal legges til slik:

$$
N = (448 - (M + 1) \mod 512) \mod 512
$$

For eksempel, hvis den opprinnelige meldingen er 950 bits, ville beregningen være som følger:

$$
\begin{align*}
M & = 950 \\
M + 1 & = 951 \\
(M + 1) \mod 512 & = 951 \mod 512 \\
& = 951 - 512 \cdot \left\lfloor \frac{951}{512} \right\rfloor \\
& = 951 - 512 \cdot 1 \\
& = 951 - 512 \\
& = 439 \\
\\
448 - (M + 1) \mod 512 & = 448 - 439 \\
& = 9 \\
\\
N & = (448 - (M + 1) \mod 512) \mod 512 \\
N & = 9 \mod 512 \\
& = 9
\end{align*}
$$

Dermed ville vi ha 9 `0`er i tillegg til separator `1`. Våre padding bits som skal legges direkte etter vår melding $M$ ville dermed være:

```text
1000 0000 00
```

Etter å ha lagt til padding bits til vår melding $M$, legger vi også til en 64-bits representasjon av den opprinnelige lengden på meldingen $M$, uttrykt i binært. Dette gjør hash-funksjonen følsom for bitenes rekkefølge og meldingens lengde.
Hvis vi går tilbake til eksemplet vårt med en opprinnelig melding på 950 bits, konverterer vi det desimale tallet `950` til binært, som gir oss `1110 1101 10`. Vi kompletterer dette tallet med nuller i bunnen for å lage totalt 64 bits. I vårt eksempel gir dette:

```text
0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0011 1011 0110
```

Denne padding-størrelsen legges til etter bit-paddingen. Derfor består meldingen etter vår forbehandling av tre deler:

1. Den opprinnelige meldingen $M$;
2. En bit `1` etterfulgt av flere bits `0` for å danne bit-paddingen;
3. En 64-bits representasjon av lengden på $M$ for å danne paddingen med størrelsen.

![CYP201](assets/fr/006.webp)

### Initialisering av Variabler

SHA256 bruker åtte initielle tilstandsvariabler, betegnet $A$ til $H$, hver på 32 bits. Disse variablene initialiseres med spesifikke konstanter, som er de fraksjonelle delene av kvadratrøttene til de første åtte primtallene. Vi vil bruke disse verdiene etterfølgende under hashingprosessen:

- $A = 0x6a09e667$
- $B = 0xbb67ae85$
- $C = 0x3c6ef372$
- $D = 0xa54ff53a$
- $E = 0x510e527f$
- $F = 0x9b05688c$
- $G = 0x1f83d9ab$
- $H = 0x5be0cd19$

SHA256 bruker også 64 andre konstanter, betegnet $K_0$ til $K_{63}$, som er de fraksjonelle delene av kubikkrøttene til de første 64 primtallene:

$$
K[0 \ldots 63] = \begin{pmatrix}
0x428a2f98, & 0x71374491, & 0xb5c0fbcf, & 0xe9b5dba5, \\
0x3956c25b, & 0x59f111f1, & 0x923f82a4, & 0xab1c5ed5, \\
0xd807aa98, & 0x12835b01, & 0x243185be, & 0x550c7dc3, \\
0x72be5d74, & 0x80deb1fe, & 0x9bdc06a7, & 0xc19bf174, \\
0xe49b69c1, & 0xefbe4786, & 0x0fc19dc6, & 0x240ca1cc, \\
0x2de92c6f, & 0x4a7484aa, & 0x5cb0a9dc, & 0x76f988da, \\
0x983e5152, & 0xa831c66d, & 0xb00327c8, & 0xbf597fc7, \\
0xc6e00bf3, & 0xd5a79147, & 0x06ca6351, & 0x14292967, \\
0x27b70a85, & 0x2e1b2138, & 0x4d2c6dfc, & 0x53380d13, \\
0x650a7354, & 0x766a0abb, & 0x81c2c92e, & 0x92722c85, \\
0xa2bfe8a1, & 0xa81a664b, & 0xc24b8b70, & 0xc76c51a3, \\
0xd192e819, & 0xd6990624, & 0xf40e3585, & 0x106aa070, \\
0x19a4c116, & 0x1e376c08, & 0x2748774c, & 0x34b0bcb5, \\
0x391c0cb3, & 0x4ed8aa4a, & 0x5b9cca4f, & 0x682e6ff3, \\
0x748f82ee, & 0x78a5636f, & 0x84c87814, & 0x8cc70208, \\
0x90befffa, & 0xa4506ceb, & 0xbef9a3f7, & 0xc67178f2
\end{pmatrix}
$$


### Inndeling av inndata

Nå som vi har en likestilt inndata, vil vi nå gå videre til hovedbehandlingsfasen av SHA256-algoritmen: kompresjonsfunksjonen. Dette trinnet er veldig viktig, da det primært er det som gir hashfunksjonen dens kryptografiske egenskaper som vi studerte i forrige kapittel.

Først starter vi med å dele vår likestilte melding (resultatet av forbehandlingsstegene) inn i flere blokker $P$ på 512 bits hver. Hvis vår likestilte melding har en total størrelse på $n \times 512$ bits, vil vi derfor ha $n$ blokker, hver på 512 bits. Hver 512-bits blokk vil bli behandlet individuelt av kompresjonsfunksjonen, som består av 64 runder med påfølgende operasjoner. La oss navngi disse blokkene $P_1$, $P_2$, $P_3$...

### Logiske operasjoner

Før vi utforsker kompresjonsfunksjonen i detalj, er det viktig å forstå de grunnleggende logiske operasjonene som brukes i den. Disse operasjonene, basert på boolsk algebra, opererer på bitnivå. De grunnleggende logiske operasjonene som brukes er:

- **Konjunksjon (OG)**: betegnet $\land$, tilsvarer en logisk "OG".
- **Disjunksjon (ELLER)**: betegnet $\lor$, tilsvarer en logisk "ELLER".
- **Negasjon (IKKE)**: betegnet $\lnot$, tilsvarer en logisk "IKKE".

Fra disse grunnleggende operasjonene kan vi definere mer komplekse operasjoner, som "Eksklusiv ELLER" (XOR) betegnet $\oplus$, som er mye brukt i kryptografi.
Hver logisk operasjon kan representeres av en sannhetstabell, som indikerer resultatet for alle mulige kombinasjoner av binære inngangsverdier (to operander $p$ og $q$).
For XOR ($\oplus$):

| $p$ | $q$ | $p \oplus q$ |
| --- | --- | ------------ |
| 0   | 0   | 0            |
| 0   | 1   | 1            |
| 1   | 0   | 1            |
| 1   | 1   | 0            |

For OG ($\land$):

| $p$ | $q$ | $p \land q$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

For NOT ($\lnot p$):

| $p$ | $\lnot p$ |
| --- | --------- |
| 0   | 1         |
| 1   | 0         |

La oss ta et eksempel for å forstå operasjonen av XOR på bitnivå. Hvis vi har to binære tall på 6 bits:

- $a = 101100$
- $b = 001000$

Da:

$$
a \oplus b = 101100 \oplus 001000 = 100100
$$

Ved å anvende XOR bit for bit:

| Bitposisjon | $a$ | $b$ | $a \oplus b$ |
| ----------- | --- | --- | ------------ |
| 1           | 1   | 0   | 1            |
| 2           | 0   | 0   | 0            |
| 3           | 1   | 1   | 0            |
| 4           | 1   | 0   | 1            |
| 5           | 0   | 0   | 0            |
| 6           | 0   | 0   | 0            |

Resultatet blir derfor $100100$.

I tillegg til logiske operasjoner, bruker kompresjonsfunksjonen bit-skiftoperasjoner, som vil spille en essensiell rolle i diffusjonen av bits i algoritmen.

Først har vi den logiske høyre skiftoperasjonen, betegnet $ShR_n(x)$, som skifter alle bitsene til $x$ til høyre med $n$ posisjoner, og fyller de ledige bitsene på venstre side med nuller.

For eksempel, for $x = 101100001$ (på 9 bits) og $n = 4$:

$$
ShR_4(101100001) = 000010110
$$

Skjematisk kan høyre skiftoperasjonen ses slik:

![CYP201](assets/fr/007.webp)
En annen operasjon brukt i SHA256 for bitmanipulasjon er den høyre sirkulære rotasjonen, betegnet $RotR_n(x)$, som skifter bitsene til $x$ til høyre med $n$ posisjoner, og setter de skiftede bitsene inn igjen i begynnelsen av strengen.
For eksempel, for $x = 101100001$ (over 9 bits) og $n = 4$:

$$
RotR_4(101100001) = 000110110
$$

Skjematisk kan den høyre sirkulære skiftoperasjonen ses slik:

![CYP201](assets/fr/008.webp)

### Kompresjonsfunksjon

Nå som vi har forstått de grunnleggende operasjonene, la oss undersøke SHA256 kompresjonsfunksjonen i detalj.

I det forrige steget delte vi vårt inndata i flere 512-bits stykker $P$. For hver 512-bits blokk $P$, har vi:

- **Meldingsordene $W_i$**: for $i$ fra 0 til 63.
- **Konstantene $K_i$**: for $i$ fra 0 til 63, definert i det forrige steget.
- **Tilstandsvariablene $A, B, C, D, E, F, G, H$**: initialisert med verdiene fra det forrige steget.
  De første 16 ordene, $W_0$ til $W_{15}$, er direkte hentet fra den bearbeidede 512-bits blokken $P$. Hvert ord $W_i$ består av 32 påfølgende bits fra blokken. Så, for eksempel, tar vi vår første del av inndata $P_1$, og vi deler den videre inn i mindre 32-bits deler som vi kaller ord.
  De neste 48 ordene ($W_{16}$ til $W_{63}$) genereres ved hjelp av følgende formel:

$$
W_i = W_{i-16} + \sigma_0(W_{i-15}) + W_{i-7} + \sigma_1(W_{i-2}) \mod 2^{32}
$$

Med:

- $\sigma_0(x) = RotR_7(x) \oplus RotR_{18}(x) \oplus ShR_3(x)$
- $\sigma_1(x) = RotR_{17}(x) \oplus RotR_{19}(x) \oplus ShR_{10}(x)$

I dette tilfellet er $x$ lik $W_{i-15}$ for $\sigma_0(x)$ og $W_{i-2}$ for $\sigma_1(x)$.

Når vi har bestemt alle ordene $W_i$ for vår 512-bits del, kan vi gå videre til kompresjonsfunksjonen, som består av å utføre 64 runder.

![CYP201](assets/fr/009.webp)
For hver runde $i$ fra 0 til 63, har vi tre forskjellige typer inndata. Først, $W_i$ som vi nettopp har bestemt, delvis bestående av vår meldingsdel $P_n$. Deretter, de 64 konstantene $K_i$. Til slutt bruker vi tilstandsvariablene $A$, $B$, $C$, $D$, $E$, $F$, $G$ og $H$, som vil utvikle seg gjennom hashingsprosessen og bli modifisert med hver kompresjonsfunksjon. Men for den første delen $P_1$, bruker vi de opprinnelige konstantene gitt tidligere.
Vi utfører deretter følgende operasjoner på våre inndata:

- **Funksjon $\Sigma_0$:**

$$
\Sigma_0(A) = RotR_2(A) \oplus RotR_{13}(A) \oplus RotR_{22}(A)
$$

- **Funksjon $\Sigma_1$:**

$$
\Sigma_1(E) = RotR_6(E) \oplus RotR_{11}(E) \oplus RotR_{25}(E)
$$

- **Funksjon $Ch$ ("_Velg_"):**

$$
Ch(E, F, G) = (E \land F) \oplus (\lnot E \land G)
$$

- **Funksjon $Maj$ ("_Flertall_"):**

$$
Maj(A, B, C) = (A \land B) \oplus (A \land C) \oplus (B \land C)
$$

Deretter beregner vi 2 midlertidige variabler:

- $temp1$:

$$
temp1 = H + \Sigma_1(E) + Ch(E, F, G) + K_i + W_i \mod 2^{32}
$$

- $temp2$:

$$
temp2 = \Sigma_0(A) + Maj(A, B, C) \mod 2^{32}
$$

Deretter oppdaterer vi tilstandsvariablene som følger:

$$
\begin{cases}
H = G \\
G = F \\
F = E \\
E = D + temp1 \mod 2^{32} \\
D = C \\
C = B \\
B = A \\
A = temp1 + temp2 \mod 2^{32}
\end{cases}
$$

Følgende diagram representerer en runde av SHA256-komprimeringsfunksjonen slik vi nettopp har beskrevet:

![CYP201](assets/fr/010.webp)

- Pilene indikerer dataflyten;
- Boksene representerer operasjonene som utføres;
- $+$ omringet representerer addisjon modulo $2^{32}$.

Vi kan allerede observere at denne runden produserer nye tilstandsvariabler $A$, $B$, $C$, $D$, $E$, $F$, $G$, og $H$. Disse nye variablene vil tjene som input for neste runde, som igjen vil produsere nye variabler $A$, $B$, $C$, $D$, $E$, $F$, $G$, og $H$, for å brukes i den følgende runden. Denne prosessen fortsetter opp til den 64. runden.
Etter de 64 rundene, oppdaterer vi de opprinnelige verdiene av tilstandsvariablene ved å legge dem til de endelige verdiene ved slutten av runde 64:

$$
\begin{cases}
A = A_{\text{initial}} + A \mod 2^{32} \\
B = B_{\text{initial}} + B \mod 2^{32} \\
C = C_{\text{initial}} + C \mod 2^{32} \\
D = D_{\text{initial}} + D \mod 2^{32} \\
E = E_{\text{initial}} + E \mod 2^{32} \\
F = F_{\text{initial}} + F \mod 2^{32} \\
G = G_{\text{initial}} + G \mod 2^{32} \\
H = H_{\text{initial}} + H \mod 2^{32}
\end{cases}

$$

Disse nye verdiene av $A$, $B$, $C$, $D$, $E$, $F$, $G$, og $H$ vil tjene som de opprinnelige verdiene for neste blokk, $P_2$. For denne blokken $P_2$, replikerer vi den samme komprimeringsprosessen med 64 runder, deretter oppdaterer vi variablene for blokk $P_3$, og så videre til den siste blokken av vårt likestilte input.

Etter å ha behandlet alle meldingsblokkene, konkatenrer vi de endelige verdiene av variablene $A$, $B$, $C$, $D$, $E$, $F$, $G$, og $H$ for å danne den endelige 256-bit hashen av vår hashfunksjon:


$$

\text{Hash} = A \Vert B \Vert C \Vert D \Vert E \Vert F \Vert G \Vert H

$$

Hver variabel er et 32-bit heltall, så deres konkatenasjon gir alltid et 256-bit resultat, uavhengig av størrelsen på vår meldingsinput til hashfunksjonen.

### Begrunnelse for kryptografiske egenskaper

Men hvordan er denne funksjonen irreversibel, motstandsdyktig mot kollisjoner, og sikker mot manipulering?

For sikkerhet mot manipulering, er det ganske enkelt å forstå. Det utføres så mange beregninger i rekkefølge, som avhenger både av input og konstantene, at den minste modifikasjonen av den opprinnelige meldingen fullstendig endrer banen som tas, og dermed fullstendig endrer output-hashen. Dette er det som kalles lavineeffekten. Denne egenskapen sikres delvis ved å blande de mellomliggende tilstandene med de opprinnelige tilstandene for hvert stykke.
Neste, når vi diskuterer en kryptografisk hashfunksjon, brukes ikke termen "irreversibilitet" generelt. I stedet snakker vi om "preimage resistance", som spesifiserer at for en gitt $y$, er det vanskelig å finne en $x$ slik at $h(x) = y$. Denne preimage-motstanden er garantert av den algebraiske kompleksiteten og den sterke ikke-lineariteten i operasjonene som utføres i kompresjonsfunksjonen, samt ved tap av visse informasjoner i prosessen. For eksempel, for et gitt resultat av en addisjon modulo, er det flere mulige operander:$$
3+2 \mod 10 = 5 \\
7+8 \mod 10 = 5 \\
5+10 \mod 10 = 5
$$

I dette eksemplet, ved å kun vite moduloen brukt (10) og resultatet (5), kan man ikke med sikkerhet bestemme hvilke operander som ble brukt i addisjonen. Det sies at det er flere kongruenser modulo 10.

For XOR-operasjonen står vi overfor samme problem. Husk sannhetstabellen for denne operasjonen: ethvert 1-bit resultat kan bestemmes av to forskjellige inngangskonfigurasjoner som har nøyaktig samme sannsynlighet for å være de korrekte verdiene. Derfor kan man ikke med sikkerhet bestemme operandene til en XOR ved å kun kjenne til resultatet. Hvis vi øker størrelsen på XOR-operander, øker antallet mulige innganger kjent kun ved resultatet eksponentielt. I tillegg brukes XOR ofte sammen med andre bitnivå-operasjoner, som $\text{RotR}$-operasjonen, som legger til enda flere mulige tolkninger av resultatet.

Kompresjonsfunksjonen bruker også $\text{ShR}$-operasjonen. Denne operasjonen fjerner en del av den grunnleggende informasjonen, som deretter blir umulig å hente ut senere. Igjen, det finnes ingen algebraisk måte å reversere denne operasjonen på. Alle disse enveis- og informasjonstap-operasjonene brukes veldig ofte i kompresjonsfunksjoner. Antallet mulige innganger for et gitt utdata er dermed nesten uendelig, og hvert forsøk på omvendt beregning ville føre til ligninger med et veldig høyt antall ukjente, som ville øke eksponentielt ved hvert trinn.

Til slutt, for egenskapen til kollisjonsmotstand, kommer flere parametere i spill. Forbehandlingen av den opprinnelige meldingen spiller en essensiell rolle. Uten denne forbehandlingen, kunne det vært lettere å finne kollisjoner på funksjonen. Selv om kollisjoner teoretisk eksisterer (på grunn av duehullprinsippet), gjør strukturen til hashfunksjonen, kombinert med de nevnte egenskapene, sannsynligheten for å finne en kollisjon ekstremt lav.
For at en hashfunksjon skal være motstandsdyktig mot kollisjoner, er det essensielt at:

- Utdataet er uforutsigbart: Enhver forutsigbarhet kan utnyttes for å finne kollisjoner raskere enn med en brute force-angrep. Funksjonen sikrer at hvert bit av utdataet avhenger på en ikke-triviell måte av inndata. Med andre ord, funksjonen er designet slik at hvert bit av det endelige resultatet har en uavhengig sannsynlighet for å være 0 eller 1, selv om denne uavhengigheten ikke er absolutt i praksis.
- Distribusjonen av hasher er pseudo-tilfeldig: Dette sikrer at hashene er jevnt fordelt.
- Størrelsen på hashen er betydelig: jo større det mulige rommet for resultater, jo vanskeligere er det å finne en kollisjon.

Kryptografer designer disse funksjonene ved å evaluere de beste mulige angrepene for å finne kollisjoner, deretter justere parameterne for å gjøre disse angrepene ineffektive.

### Merkle-Damgård-konstruksjonen

Strukturen til SHA256 er basert på Merkle-Damgård-konstruksjonen, som gjør det mulig å transformere en kompresjonsfunksjon til en hashfunksjon som kan behandle meldinger av vilkårlig lengde. Dette er nettopp hva vi har sett i dette kapittelet.
Imidlertid er noen gamle hash-funksjoner som SHA1 eller MD5, som bruker denne spesifikke konstruksjonen, sårbare for lengdeutvidelsesangrep. Dette er en teknikk som lar en angriper som kjenner hashen av en melding $M$ og lengden på $M$ (uten å kjenne selve meldingen) beregne hashen av en melding $M'$ dannet ved å konkatere $M$ med ekstra innhold.
SHA256, selv om den bruker samme type konstruksjon, er teoretisk motstandsdyktig mot denne typen angrep, i motsetning til SHA1 og MD5. Dette kan forklare mysteriet med dobbel hashing implementert gjennom hele Bitcoin av Satoshi Nakamoto. For å unngå denne typen angrep, kan Satoshi ha foretrukket å bruke en dobbel SHA256:

$$
\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))
$$

Dette forbedrer sikkerheten mot potensielle angrep relatert til Merkle-Damgård-konstruksjonen, men det øker ikke sikkerheten i hash-prosessen når det gjelder kollisjonsmotstand. Videre, selv om SHA256 hadde vært sårbar for denne typen angrep, ville det ikke ha hatt en alvorlig innvirkning, ettersom alle bruksområder for hash-funksjoner i Bitcoin involverer offentlige data. Imidlertid kan lengdeutvidelsesangrepet bare være nyttig for en angriper hvis de hashede dataene er private og brukeren har brukt hash-funksjonen som en autentiseringsmekanisme for disse dataene, lik en MAC. Dermed forblir implementeringen av dobbel hashing et mysterium i utformingen av Bitcoin.
Nå som vi har sett nærmere på virkemåten til hash-funksjoner, spesielt SHA256, som brukes omfattende i Bitcoin, vil vi fokusere mer spesifikt på de kryptografiske derivasjonsalgoritmene som brukes på applikasjonsnivå, spesielt for å utlede nøklene til lommeboken din.

## Algoritmene som brukes for derivasjon

<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>

I Bitcoin på applikasjonsnivå, i tillegg til hash-funksjoner, brukes kryptografiske derivasjonsalgoritmer for å generere sikre data fra innledende inndata. Selv om disse algoritmene er avhengige av hash-funksjoner, tjener de forskjellige formål, spesielt når det gjelder autentisering og nøkkelgenerering. Disse algoritmene beholder noen av egenskapene til hash-funksjoner, som irreversibilitet, manipuleringsmotstand og kollisjonsmotstand.

På Bitcoin-lommebøker brukes hovedsakelig 2 derivasjonsalgoritmer:

1. **HMAC (_Hash-basert meldingsautentiseringskode_)**
2. **PBKDF2 (_Password-Based Key Derivation Function 2_)**

Vi vil utforske funksjonen og rollen til hver av dem.

### HMAC-SHA512

HMAC er en kryptografisk algoritme som beregner en autentiseringskode basert på en kombinasjon av en hash-funksjon og en hemmelig nøkkel. Bitcoin bruker HMAC-SHA512, varianten av HMAC som bruker SHA512 hash-funksjonen. Vi har allerede sett i forrige kapittel at SHA512 er en del av samme familie av hash-funksjoner som SHA256, men den produserer en 512-biters utdata.

Her er dens generelle driftsskjema med $m$ som inngangsmeldingen og $K$ en hemmelig nøkkel:

![CYP201](assets/fr/011.webp)

La oss studere mer i detalj hva som skjer i denne HMAC-SHA512 svarte boksen. HMAC-SHA512-funksjonen med:

- $m$: den vilkårlig store meldingen valgt av brukeren (første inndata);
- $K$: den vilkårlige hemmelige nøkkelen valgt av brukeren (andre inndata);
- $K'$: nøkkelen $K$ justert til størrelsen $B$ på hash-funksjonens blokker (1024 bits for SHA512, eller 128 bytes);
- $\text{SHA512}$: SHA512 hash-funksjonen;
- $\oplus$: XOR (eksklusiv eller) operasjonen;
- $\Vert$: operatøren for sammenkjeding, som kobler bitstrenger ende-til-ende;
- $\text{opad}$: konstant bestående av bytet $0x5c$ gjentatt 128 ganger
- $\text{ipad}$: konstant bestående av bytet $0x36$ gjentatt 128 ganger
  Før man beregner HMAC, er det nødvendig å likestille nøkkelen og konstantene i henhold til blokkstørrelsen $B$. For eksempel, hvis nøkkelen $K$ er kortere enn 128 byte, blir den fylt ut med nuller for å nå størrelsen $B$. Hvis $K$ er lengre enn 128 byte, blir den komprimert ved hjelp av SHA512, og deretter blir nuller lagt til inntil den når 128 byte. På denne måten oppnås en likestilt nøkkel kalt $K'$.
  Verdiene av $\text{opad}$ og $\text{ipad}$ oppnås ved å gjenta deres basisbyte ($0x5c$ for $\text{opad}$, $0x36$ for $\text{ipad}$) inntil størrelsen $B$ er nådd. Således, med $B = 128$ byte, har vi:

$$
\text{opad} = \underbrace{0x5c5c\ldots5c}_{128 \, \text{bytes}}
$$

Når forbehandlingen er gjort, er HMAC-SHA512-algoritmen definert ved følgende ligning:

$$
\text {HMAC-SHA512}_K(m) = \text{SHA512} \left( (K' \oplus \text{opad}) \parallel \text{SHA512} \left( (K' \oplus \text{ipad}) \parallel m \right) \right)
$$

Denne ligningen brytes ned i følgende trinn:

1. XOR den justerte nøkkelen $K'$ med $\text{ipad}$ for å oppnå $\text{iKpad}$;
2. XOR den justerte nøkkelen $K'$ med $\text{opad}$ for å oppnå $\text{oKpad}$;
3. Sammenkjed $\text{iKpad}$ med meldingen $m$.
4. Hash dette resultatet med SHA512 for å oppnå en mellomliggende hash $H_1$.
5. Sammenkjed $\text{oKpad}$ med $H_1$.
6. Hash dette resultatet med SHA512 for å oppnå det endelige resultatet $H_2$.

Disse trinnene kan oppsummeres skjematisk som følger:

![CYP201](assets/fr/012.webp)

HMAC brukes i Bitcoin spesielt for nøkkelavledning i HD (Hierarchical Deterministic) lommebøker (vi vil snakke mer om dette i kommende kapitler) og som en komponent av PBKDF2.

### PBKDF2

PBKDF2 (_Password-Based Key Derivation Function 2_) er en nøkkelavledningsalgoritme designet for å forbedre sikkerheten til passord. Algoritmen anvender en pseudo-tilfeldig funksjon (her HMAC-SHA512) på et passord og en kryptografisk salt, og gjentar deretter denne operasjonen et bestemt antall ganger for å produsere en utgangsnøkkel.

I Bitcoin brukes PBKDF2 til å generere frøet til en HD-lommebok fra en mnemonisk frase og en passfrase (men vi vil snakke mer om dette i detalj i kommende kapitler).

PBKDF2-prosessen er som følger, med:

- $m$: brukerens mnemoniske frase;
- $s$: den valgfrie passfrasen for å øke sikkerheten (tomt felt hvis ingen passfrase);
- $n$: antall iterasjoner av funksjonen, i vårt tilfelle er det 2048.
  PBKDF2-funksjonen er definert iterativt. Hver iterasjon tar resultatet fra den forrige, passerer det gjennom HMAC-SHA512, og kombinerer de påfølgende resultatene for å produsere den endelige nøkkelen:
  $$
  \text{PBKDF2}(m, s) = \text{HMAC-SHA512}^{2048}(m, s)
  $$

Skjematisk kan PBKDF2 representeres som følger:

![CYP201](assets/fr/013.webp)

I dette kapittelet har vi utforsket HMAC-SHA512 og PBKDF2-funksjonene, som bruker hash-funksjoner for å sikre integriteten og sikkerheten til nøkkelavledninger i Bitcoin-protokollen. I neste del vil vi se nærmere på digitale signaturer, en annen kryptografisk metode som er mye brukt i Bitcoin.

# Digitale Signaturer

<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>

## Digitale Signaturer og Elliptiske Kurver

<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>

Den andre kryptografiske metoden som brukes i Bitcoin involverer algoritmer for digitale signaturer. La oss utforske hva dette innebærer og hvordan det fungerer.

### Bitcoins, UTXOer og Betingelser for Bruk

Begrepet "_lommebok_" i Bitcoin kan være ganske forvirrende for nybegynnere. Faktisk, det som kalles en Bitcoin-lommebok er programvare som ikke direkte holder dine bitcoins, i motsetning til en fysisk lommebok som kan holde mynter eller sedler. Bitcoins er rett og slett enheter av konto. Denne kontoenheten representeres av **UTXO** (_Unspent Transaction Outputs_), som er ubrukte transaksjonsutganger. Hvis disse utgangene er ubrukte, betyr det at de tilhører en bruker. UTXOer er på en måte biter av bitcoins, av variabel størrelse, som tilhører en bruker.

Bitcoin-protokollen er distribuert og opererer uten en sentral autoritet. Derfor er den ikke som tradisjonelle bankposter, hvor euroene som tilhører deg er enkelt assosiert med din personlige identitet. På Bitcoin tilhører dine UTXOer deg fordi de er beskyttet av brukerbetingelser spesifisert i Script-språket. For å forenkle, det finnes to typer skript: låseskriptet (_scriptPubKey_), som beskytter en UTXO, og opplåsingsskriptet (_scriptSig_), som tillater opplåsing av en UTXO og dermed bruk av bitcoin-enhetene den representerer.
Den opprinnelige operasjonen av Bitcoin med P2PK-skript involverer bruk av en offentlig nøkkel for å låse midler, og spesifiserer i et _scriptPubKey_ at personen som ønsker å bruke denne UTXOen må gi en gyldig signatur med den private nøkkelen som tilsvarer denne offentlige nøkkelen. For å låse opp denne UTXOen, er det derfor nødvendig å gi en gyldig signatur i _scriptSig_. Som navnene antyder, er den offentlige nøkkelen kjent for alle siden den er kringkastet på blokkjeden, mens den private nøkkelen bare er kjent for den legitime eieren av midlene.
Dette er den grunnleggende operasjonen av Bitcoin, men over tid har denne operasjonen blitt mer kompleks. Først introduserte Satoshi også P2PKH-skript, som bruker en mottaksadresse i _scriptPubKey_, som representerer hashen av den offentlige nøkkelen. Deretter ble systemet enda mer komplekst med ankomsten av SegWit og deretter Taproot. Imidlertid forblir det generelle prinsippet grunnleggende det samme: en offentlig nøkkel eller en representasjon av denne nøkkelen brukes til å låse UTXOer, og en tilsvarende privat nøkkel kreves for å låse dem opp og dermed bruke dem.
En bruker som ønsker å utføre en Bitcoin-transaksjon må derfor opprette en digital signatur ved hjelp av sin private nøkkel på den aktuelle transaksjonen. Signaturen kan verifiseres av andre nettverksdeltakere. Hvis den er gyldig, betyr dette at brukeren som initierer transaksjonen faktisk er eieren av den private nøkkelen, og derfor eieren av bitcoinene de ønsker å bruke. Andre brukere kan deretter akseptere og formidle transaksjonen.
Som et resultat må en bruker som eier bitcoins låst med en offentlig nøkkel finne en måte å sikkert lagre det som tillater opplåsing av deres midler: den private nøkkelen. En Bitcoin-lommebok er nettopp en enhet som vil tillate deg å enkelt holde alle nøklene dine uten at andre mennesker har tilgang til dem. Det er derfor mer som en nøkkelring enn en lommebok.

Den matematiske koblingen mellom en offentlig nøkkel og en privat nøkkel, samt evnen til å utføre en signatur for å bevise besittelsen av en privat nøkkel uten å avsløre den, er muliggjort av en digital signaturalgoritme. I Bitcoin-protokollen brukes 2 signaturalgoritmer: **ECDSA** (_Elliptic Curve Digital Signature Algorithm_) og **Schnorr-signaturordningen**. ECDSA er den digitale signaturprotokollen som brukes i Bitcoin fra begynnelsen. Schnorr er mer nylig i Bitcoin, da den ble introdusert i november 2021 med Taproot-oppdateringen.
Disse to algoritmene er ganske like i sine mekanismer. De er begge basert på elliptisk kurvekryptografi. Den største forskjellen mellom disse to protokollene ligger i strukturen av signaturen og noen spesifikke matematiske egenskaper. Vi vil derfor studere funksjonen til disse algoritmene, og starter med den eldste: ECDSA.

### Elliptisk Kurvekryptografi

Elliptisk Kurvekryptografi (ECC) er et sett med algoritmer som bruker en elliptisk kurve for sine ulike matematiske og geometriske egenskaper til kryptografiske formål. Sikkerheten til disse algoritmene er avhengig av vanskeligheten med det diskrete logaritmeproblemet på elliptiske kurver. Elliptiske kurver brukes spesielt for nøkkelutvekslinger, asymmetrisk kryptering, eller for å skape digitale signaturer.

En viktig egenskap ved disse kurvene er at de er symmetriske med hensyn til x-aksen. Således vil enhver ikke-vertikal linje som skjærer kurven i to distinkte punkter alltid krysse kurven ved et tredje punkt. Videre vil enhver tangent til kurven ved et ikke-singulært punkt krysse kurven ved et annet punkt. Disse egenskapene vil være nyttige for å definere operasjoner på kurven.

Her er en representasjon av en elliptisk kurve over feltet av reelle tall:

![CYP201](assets/fr/014.webp)

Hver elliptisk kurve er definert av en ligning på formen:

$$
y^2 = x^3 + ax + b
$$

### secp256k1

For å bruke ECDSA eller Schnorr, må man velge parametrene for den elliptiske kurven, det vil si verdiene av $a$ og $b$ i kurveligningen. Det finnes forskjellige standarder av elliptiske kurver som er ansett for å være kryptografisk sikre. Den mest kjente er _secp256r1_-kurven, definert og anbefalt av NIST (_National Institute of Standards and Technology_).

Til tross for dette valgte Satoshi Nakamoto, oppfinneren av Bitcoin, å ikke bruke denne kurven. Grunnen til dette valget er ukjent, men noen tror han foretrakk å finne et alternativ fordi parametrene til denne kurven potensielt kunne inneholde en bakdør. I stedet bruker Bitcoin-protokollen standarden **_secp256k1_**-kurven. Denne kurven er definert av parametrene $a = 0$ og $b = 7$. Dens ligning er derfor:

$$
y^2 = x^3 + 7
$$

Dens grafiske representasjon over feltet av reelle tall ser slik ut:
![CYP201](assets/fr/015.webp)
I kryptografi jobber vi med endelige tallmengder. Mer spesifikt jobber vi på det endelige feltet $\mathbb{F}_p$, som er feltet av heltall modulo et primtall $p$.
**Definisjon**: Et primtall er et naturlig heltall større enn eller lik 2 som kun har to distinkte positive heltallsdivisorer: 1 og seg selv. For eksempel er tallet 7 et primtall siden det kun kan deles av 1 og 7. På den andre siden er tallet 8 ikke et primtall fordi det kan deles av 1, 2, 4, og 8.
I Bitcoin er primtallet $p$ som brukes til å definere det endelige feltet veldig stort. Det er valgt på en slik måte at ordenen til feltet (dvs. antallet elementer i $\mathbb{F}_p$) er tilstrekkelig stort for å sikre kryptografisk sikkerhet.

Primtallet $p$ som brukes er:

```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```

I desimal notasjon tilsvarer dette:

$$
p = 2^{256} - 2^{32} - 977
$$

Dermed er ligningen for vår elliptiske kurve faktisk:

$$
y^2 \equiv x^3 + 7 \mod p
$$

Gitt at denne kurven er definert over det endelige feltet $\mathbb{F}_p$, ligner den ikke lenger en kontinuerlig kurve, men heller et diskret sett med punkter. For eksempel, her er hvordan kurven som brukes i Bitcoin ser ut for et veldig lite $p = 17$:

![CYP201](assets/fr/016.webp)

I dette eksemplet har jeg med vilje begrenset det endelige feltet til $p = 17$ av pedagogiske årsaker, men man må forestille seg at den som brukes i Bitcoin er enormt større, nesten $2^{256}$.

Vi bruker et endelig felt av heltall modulo $p$ for å sikre nøyaktigheten av operasjoner på kurven. Faktisk er elliptiske kurver over feltet av reelle tall utsatt for unøyaktigheter på grunn av avrundingsfeil under beregningsberegninger. Hvis mange operasjoner utføres på kurven, akkumuleres disse feilene, og det endelige resultatet kan være feilaktig eller vanskelig å reprodusere. Den eksklusive bruken av positive heltall sikrer perfekt nøyaktighet av beregninger og dermed reproduserbarhet av resultatet.

Matematikken til elliptiske kurver over endelige felt er analog med de over feltet av reelle tall, med tilpasningen at alle operasjoner utføres modulo $p$. For å forenkle forklaringer, vil vi i de følgende kapitlene fortsette å illustrere konsepter ved hjelp av en kurve definert over reelle tall, samtidig som vi husker at, i praksis, er kurven definert over et endelig felt.

Hvis du ønsker å lære mer om de matematiske grunnlagene for moderne kryptografi, anbefaler jeg også å konsultere dette andre kurset på Plan ₿ Network:

https://planb.network/courses/cyp302

## Beregning av den offentlige nøkkelen fra den private nøkkelen

<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>
Som tidligere sett, er de digitale signaturalgoritmene på Bitcoin basert på et par av private og offentlige nøkler som er matematisk koblet. La oss utforske sammen hva denne matematiske koblingen er og hvordan de genereres.

### Den private nøkkelen

Den private nøkkelen er ganske enkelt et tilfeldig eller pseudo-tilfeldig tall. I tilfellet med Bitcoin er dette tallet 256 bits i størrelse. Antall muligheter for en Bitcoin privat nøkkel er derfor teoretisk $2^{256}$.
**Merk**: Et "pseudo-tilfeldig tall" er et tall som har egenskaper nær de til et virkelig tilfeldig tall, men som genereres av en deterministisk algoritme.
Imidlertid, i praksis, finnes det kun $n$ distinkte punkter på vår elliptiske kurve secp256k1, hvor $n$ er ordenen til generatorelementet $G$ på kurven. Vi vil se senere hva dette tallet tilsvarer, men husk enkelt at en gyldig privat nøkkel er et heltall mellom $1$ og $n-1$, med tanke på at $n$ er et tall nær, men litt mindre enn $2^{256}$. Derfor er det noen 256-bits tall som ikke er gyldige for å bli en privat nøkkel i Bitcoin, spesifikt, alle tallene mellom $n$ og $2^{256}$. Hvis genereringen av det tilfeldige tallet (den private nøkkelen) produserer en verdi $k$ slik at $k \geq n$, anses den som ugyldig, og en ny tilfeldig verdi må genereres.

Antallet muligheter for en Bitcoin privat nøkkel er derfor omtrent $n$, som er et tall nær $1.158 \times 10^{77}$. Dette tallet er så stort at hvis du velger en privat nøkkel tilfeldig, er det statistisk nesten umulig å lande på en annen brukers private nøkkel. For å gi deg en ide om skalaen, er antallet mulige private nøkler på Bitcoin av en størrelsesorden nær det estimerte antallet atomer i det observerbare universet.

Som vi vil se i de kommende kapitlene, i dag, genereres flertallet av private nøkler brukt på Bitcoin ikke tilfeldig, men er resultatet av deterministisk derivasjon fra en mnemonisk frase, selv pseudo-tilfeldig (dette er den berømte frasen på 12 eller 24 ord). Denne informasjonen endrer ikke noe for bruken av signaturalgoritmer som ECDSA, men det hjelper til å refokusere vår popularisering på Bitcoin.

For fortsettelsen av forklaringen, vil den private nøkkelen bli betegnet med den lille bokstaven $k$.

### Den Offentlige Nøkkelen

Den offentlige nøkkelen er et punkt på den elliptiske kurven, betegnet med stor bokstav $K$, og beregnes fra den private nøkkelen $k$. Dette punktet $K$ representeres av et par koordinater $(x, y)$ på den elliptiske kurven, hver koordinat er et heltall modulo $p$, primtallet som definerer det endelige feltet $\mathbb{F}_p$.
I praksis representeres en ukomprimert offentlig nøkkel av 512 bits (eller 64 bytes), som tilsvarer to 256-bits tall ($x$ og $y$) plassert ende-til-ende. Disse tallene er absissen ($x$) og ordinaten ($y$) for vårt punkt på secp256k1. Hvis vi legger til prefikset, totaliserer den offentlige nøkkelen 520 bits.

Det er imidlertid også mulig å representere den offentlige nøkkelen i en komprimert form ved å kun beholde absissen $x$ av vårt punkt på kurven og en byte som indikerer pariteten til $y$. Dette er det som er kjent som en komprimert offentlig nøkkel. Jeg vil snakke mer om dette i de siste kapitlene av denne opplæringen. Men det du trenger å huske er at en offentlig nøkkel $K$ er et punkt beskrevet av $x$ og $y$.

For å beregne punktet $K$ som tilsvarer vår offentlige nøkkel, bruker vi operasjonen av skalar multiplikasjon på elliptiske kurver, definert som en gjentatt addisjon ($k$ ganger) av generatorelementet $G$:

$$
K = k \cdot G
$$

hvor:

- $k$ er den private nøkkelen (et tilfeldig heltall mellom $1$ og $n-1$);
- $G$ er generatorelementet til den elliptiske kurven som brukes av alle deltakere i Bitcoin-nettverket;
- $\cdot$ representerer den skalar multiplikasjonen på den elliptiske kurven, som tilsvarer å legge til punktet $G$ til seg selv $k$ ganger.

Det faktum at dette punktet $G$ er felles for alle offentlige nøkler på Bitcoin, gjør at vi kan være sikre på at den samme private nøkkelen $k$ alltid vil gi oss den samme offentlige nøkkelen $K$:

![CYP201](assets/fr/017.webp)

Hovedkarakteristikken til denne operasjonen er at det er en enveisfunksjon. Det er enkelt å beregne den offentlige nøkkelen $K$ ved å kjenne den private nøkkelen $k$ og generatorelementet $G$, men det er praktisk talt umulig å beregne den private nøkkelen $k$ ved å kun kjenne den offentlige nøkkelen $K$ og generatorelementet $G$. Å finne $k$ fra $K$ og $G$ tilsvarer å løse det diskrete logaritmeproblemet på elliptiske kurver, et matematisk vanskelig problem for hvilket det ikke er kjent noen effektiv algoritme. Selv de kraftigste nåværende kalkulatorene er ute av stand til å løse dette problemet på en rimelig tid.

### Addisjon og Dobling av Punkter på Elliptiske Kurver

Konseptet med addisjon på elliptiske kurver er definert geometrisk. Hvis vi har to punkter $P$ og $Q$ på kurven, blir operasjonen $P + Q$ beregnet ved å tegne en linje som passerer gjennom $P$ og $Q$. Denne linjen vil nødvendigvis krysse kurven ved et tredje punkt $R'$. Vi tar deretter speilbildet av dette punktet med hensyn til x-aksen for å få punktet $R$, som er resultatet av addisjonen:

$$
P + Q = R
$$

Grafisk kan dette representeres som følger:

![CYP201](assets/fr/019.webp)

For dobling av et punkt, det vil si operasjonen $P + P$, tegner vi tangenten til kurven ved punkt $P$. Denne tangenten krysser kurven ved et annet punkt $S'$. Vi tar deretter speilbildet av dette punktet med hensyn til x-aksen for å få punktet $S$, som er resultatet av doblingen:

$$
2P = S
$$

Grafisk vises dette som:

![CYP201](assets/fr/020.webp)

Ved å bruke disse operasjonene av addisjon og dobling, kan vi utføre den skalar multiplikasjonen av et punkt med et heltall $k$, betegnet $kP$, ved å utføre gjentatte doblinger og addisjoner.

For eksempel, anta at vi har valgt en privat nøkkel $k = 4$. For å beregne den tilknyttede offentlige nøkkelen, utfører vi:

$$
K = k \cdot G = 4G
$$

Grafisk tilsvarer dette å utføre en serie av addisjoner og doblinger:

- Beregn $2G$ ved å doble $G$.
- Beregn $4G$ ved å doble $2G$.

![CYP201](assets/fr/021.webp)

Hvis vi for eksempel ønsker å beregne punktet $3G$, må vi først beregne punktet $2G$ ved å doble punktet $G$, deretter legge til $G$ og $2G$. For å legge til $G$ og $2G$, tegner man enkelt linjen som forbinder disse to punktene, henter det unike punktet $-3G$ ved krysset mellom denne linjen og den elliptiske kurven, og deretter bestemmer $3G$ som motsatt av $-3G$.

Vi vil ha:

$$
G + G = 2G
$$

$$
2G + G = 3G
$$

Grafisk ville dette bli representert som følger:
![CYP201](assets/fr/022.webp)

### Enveiskryptering

Takket være disse operasjonene, kan vi forstå hvorfor det er enkelt å utlede en offentlig nøkkel fra en privat nøkkel, men det motsatte er praktisk talt umulig.

La oss gå tilbake til vårt forenklede eksempel. Med en privat nøkkel $k = 4$. For å beregne den tilknyttede offentlige nøkkelen, utfører vi:

$$
K = k \cdot G = 4G
$$

Vi har dermed kunnet enkelt beregne den offentlige nøkkelen $K$ ved å kjenne $k$ og $G$.

Nå, hvis noen bare kjenner den offentlige nøkkelen $K$, står de overfor diskret logaritmeproblemet: å finne $k$ slik at $K = k \cdot G$. Dette problemet anses som vanskelig fordi det ikke finnes noen effektiv algoritme for å løse det på elliptiske kurver. Dette sikrer sikkerheten til ECDSA- og Schnorr-algoritmene.

Selvfølgelig, i dette forenklede eksemplet med $k = 4$, ville det være mulig å finne $k$ gjennom prøving og feiling, ettersom antall muligheter er lavt. Men i praksis på Bitcoin, er $k$ et 256-bits heltall, noe som gjør antall muligheter astronomisk stort (omtrent $1.158 \times 10^{77}$). Derfor er det uoverkommelig å finne $k$ ved brute force.

## Signering med den private nøkkelen

<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>

Nå som du vet hvordan du kan utlede en offentlig nøkkel fra en privat nøkkel, kan du allerede motta bitcoins ved å bruke dette nøkkelparet som en betingelse for utgift. Men hvordan bruke dem? For å bruke bitcoins, må du låse opp _scriptPubKey_ knyttet til din UTXO for å bevise at du faktisk er dens legitime eier. For å gjøre dette, må du produsere en signatur $s$ som matcher den offentlige nøkkelen $K$ til stede i _scriptPubKey_ ved å bruke den private nøkkelen $k$ som opprinnelig ble brukt til å beregne $K$. Den digitale signaturen er dermed utvetydig bevis på at du er i besittelse av den private nøkkelen assosiert med den offentlige nøkkelen du hevder.

### Parametere for elliptisk kurve

For å utføre en digital signatur, må alle deltakere først bli enige om parametrene for den elliptiske kurven som brukes. I tilfellet med Bitcoin, er parametrene for **secp256k1** som følger:

Det endelige feltet $\mathbb{Z}_p$ definert av:

$$
p = 2^{256} - 2^{32} - 977
$$

```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```

$p$ er et veldig stort primtall litt mindre enn $2^{256}$.

Den elliptiske kurven $y^2 = x^3 + ax + b$ over $\mathbb{Z}_p$ definert av:

$$
a = 0, \quad b = 7
$$

Generasjonspunktet eller opprinnelsespunktet $G$:

```text
G = 0x0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
```

Dette tallet er den komprimerte formen som bare gir absissen til punkt $G$. Prefikset `02` i begynnelsen bestemmer hvilken av de to verdiene som har denne absissen $x$ skal brukes som generasjonspunkt.
Ordenen $n$ til $G$ (antallet eksisterende punkter) og kofaktoren $h$:

```text
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
```

$n$ er et veldig stort tall som er litt mindre enn $p$.

$$
h=1
$$

$h$ er kofaktoren eller antallet undergrupper. Jeg vil ikke gå nærmere inn på hva dette representerer her, ettersom det er ganske komplekst, og i tilfellet med Bitcoin, trenger vi ikke å ta det i betraktning siden det er lik $1$.

All denne informasjonen er offentlig og kjent for alle deltakere. Takket være dem, kan brukere lage en digital signatur og verifisere den.

### Signatur med ECDSA

ECDSA-algoritmen lar en bruker signere en melding med sin private nøkkel, på en slik måte at hvem som helst som kjenner den tilsvarende offentlige nøkkelen kan verifisere signaturens gyldighet, uten at den private nøkkelen noen gang blir avslørt. I konteksten av Bitcoin, avhenger meldingen som skal signeres av _sighash_ valgt av brukeren. Det er denne _sighash_ som vil bestemme hvilke deler av transaksjonen som er dekket av signaturen. Jeg vil snakke mer om dette i neste kapittel.

Her er stegene for å generere en ECDSA-signatur:

Først beregner vi hashen ($e$) av meldingen som trenger å bli signert. Meldingen $m$ blir dermed sendt gjennom en kryptografisk hashfunksjon, generelt SHA256 eller dobbel SHA256 i tilfellet med Bitcoin:

$$
e = \text{HASH}(m)
$$

Deretter beregner vi en nonce. I kryptografi er en nonce rett og slett et tall generert på en tilfeldig eller pseudo-tilfeldig måte som kun brukes én gang. Det vil si, hver gang en ny digital signatur lages med dette nøkkelparet, vil det være veldig viktig å bruke en annen nonce, ellers vil det kompromittere sikkerheten til den private nøkkelen. Det er derfor tilstrekkelig å bestemme et tilfeldig og unikt heltall $r$ slik at $1 \leq r \leq n-1$, hvor $n$ er ordenen til genereringspunktet $G$ på den elliptiske kurven.

Deretter vil vi beregne punktet $R$ på den elliptiske kurven med koordinatene $(x_R, y_R)$ slik at:

$$
R = r \cdot G
$$

Vi ekstraherer verdien av abscissen til punktet $R$ ($x_R$). Denne verdien representerer den første delen av signaturen. Og til slutt beregner vi den andre delen av signaturen $s$ på denne måten:

$$
s = r^{-1} \left( e + k \cdot x_R \right) \mod n
$$

hvor:

- $r^{-1}$ er den modulære inversen av $r$ modulo $n$, det vil si et heltall slik at $r \cdot r^{-1} \equiv 1 \mod n$;
- $k$ er brukerens private nøkkel;
- $e$ er hashen av meldingen;
- $n$ er ordenen til genereringspunktet $G$ på den elliptiske kurven.

Signaturen er da rett og slett en sammenkjedning av $x_R$ og $s$:

$$
\text{SIG} = x_R \Vert s
$$

### Verifisering av ECDSA-Signaturen

For å verifisere en signatur $(x_R, s)$, kan hvem som helst som kjenner den offentlige nøkkelen $K$ og parameterne til den elliptiske kurven gå frem på denne måten:
Først, verifiser at $x_R$ og $s$ er innenfor intervallet $[1, n-1]$. Dette sikrer at signaturen respekterer de matematiske begrensningene til den elliptiske gruppen. Hvis dette ikke er tilfellet, avviser verifisereren umiddelbart signaturen som ugyldig.
Deretter, beregn hashen av meldingen:

$$
e = \text{HASH}(m)
$$

Beregn den modulære inversen av $s$ modulo $n$:

$$
s^{-1} \mod n
$$

Beregn to skalarverdier $u_1$ og $u_2$ på denne måten:

$$
\begin{align*}
u_1 &= e \cdot s^{-1} \mod n \\
u_2 &= x_R \cdot s^{-1} \mod n
\end{align*}
$$

Og til slutt, beregn punktet $V$ på den elliptiske kurven slik at:

$$
V = u_1 \cdot G + u_2 \cdot K
$$

Signaturen er kun gyldig hvis $x_V \equiv x_R \mod n$, hvor $x_V$ er $x$-koordinaten til punktet $V$. Faktisk, ved å kombinere $u_1 \cdot G$ og $u_2 \cdot K$, oppnår man et punkt $V$ som, hvis signaturen er gyldig, må korrespondere til punktet $R$ brukt under signeringen (modulo $n$).

### Signatur med Schnorr-protokollen

Schnorr-signaturordningen er et alternativ til ECDSA som tilbyr mange fordeler. Det har vært mulig å bruke den på Bitcoin siden 2021 og introduksjonen av Taproot, med P2TR-skriptmønstre. Liksom ECDSA, tillater Schnorr-ordningen signering av en melding ved bruk av en privat nøkkel, på en slik måte at signaturen kan verifiseres av hvem som helst som kjenner den tilsvarende offentlige nøkkelen.
I tilfellet med Schnorr, brukes nøyaktig samme kurve som ECDSA med de samme parametrene. Imidlertid, offentlige nøkler representeres litt annerledes sammenlignet med ECDSA. Faktisk, de er kun betegnet av $x$-koordinaten til punktet på den elliptiske kurven. I motsetning til ECDSA, hvor komprimerte offentlige nøkler representeres av 33 bytes (med prefiksbyte som indikerer pariteten til $y$), bruker Schnorr 32-byte offentlige nøkler, som kun tilsvarer $x$-koordinaten til punktet $K$, og det antas at $y$ er jevn som standard. Denne forenklede representasjonen reduserer størrelsen på signaturene og letter visse optimaliseringer i verifiseringsalgoritmene.
Den offentlige nøkkelen er da $x$-koordinaten til punktet $K$:

$$
\text{pk} = K_x
$$

Det første steget for å generere en signatur er å hashe meldingen. Men i motsetning til ECDSA, gjøres det med andre verdier og en merket hashfunksjon brukes for å unngå kollisjoner i forskjellige kontekster. En merket hashfunksjon innebærer ganske enkelt å legge til en vilkårlig etikett til hashfunksjonens inndata sammen med meldingsdataene.

![CYP201](assets/fr/023.webp)

I tillegg til meldingen, blir $x$-koordinaten til den offentlige nøkkelen $K_x$, samt et punkt $R$ beregnet fra noncen $r$ ($R=r \cdot G$) som i seg selv er et unikt heltall for hver signatur, beregnet deterministisk fra den private nøkkelen og meldingen for å unngå sårbarheter relatert til gjenbruk av nonce, også passert inn i den merkede funksjonen. Akkurat som for den offentlige nøkkelen, beholdes kun $x$-koordinaten til nonsepunktet $R_x$ for å beskrive punktet.

Resultatet av denne hashing notert $e$ kalles "utfordringen":
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n$$

Her er $\text{HASH}$ SHA256 hash-funksjonen, og $\text{``BIP0340/challenge''}$ er den spesifikke taggen for hashing.

Til slutt beregnes parameteren $s$ på denne måten fra den private nøkkelen $k$, nonce $r$, og utfordringen $e$:

$$
s = (r + e \cdot k) \mod n
$$

Signaturen er da rett og slett paret $Rx$ og $s$.

$$
\text{SIG} = R_x \Vert s
$$

### Verifisering av Schnorr-signaturen

Verifiseringen av en Schnorr-signatur er enklere enn den for en ECDSA-signatur. Her er stegene for å verifisere signaturen $(R_x, s)$ med den offentlige nøkkelen $K_x$ og meldingen $m$:
Først verifiserer vi at $K_x$ er et gyldig heltall og mindre enn $p$. Hvis dette er tilfellet, henter vi det tilsvarende punktet på kurven med $K_y$ som er jevn. Vi ekstraherer også $R_x$ og $s$ ved å separere signaturen $\text{SIG}$. Deretter sjekker vi at $R_x < p$ og $s < n$ (kurvens orden).
Neste steg er å beregne utfordringen $e$ på samme måte som utstederen av signaturen:

$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$

Deretter beregner vi et referansepunkt på kurven på denne måten:

$$
R' = s \cdot G - e \cdot K
$$

Til slutt verifiserer vi at $R'_x = R_x$. Hvis de to x-koordinatene stemmer overens, er signaturen $(R_x, s)$ faktisk gyldig med den offentlige nøkkelen $K_x$.

### Hvorfor fungerer dette?

Signereren har beregnet $s = r + e \cdot k \mod n$, så $R' = s \cdot G - e \cdot K$ bør være lik det opprinnelige punktet $R$, fordi:

$$
s \cdot G = (r + e \cdot k) \cdot G = r \cdot G + e \cdot k \cdot G
$$

Siden $K = k \cdot G$, har vi $e \cdot k \cdot G = e \cdot K$. Dermed:

$$
R' = r \cdot G = R
$$

Derfor har vi:

$$
R'_x = R_x
$$

### Fordelene med Schnorr-signaturer

Schnorr-signaturskjemaet tilbyr flere fordeler for Bitcoin over den opprinnelige ECDSA-algoritmen. Først tillater Schnorr aggregasjon av nøkler og signaturer. Dette betyr at flere offentlige nøkler kan kombineres til en enkelt nøkkel.

![CYP201](assets/fr/024.webp)

Og på samme måte kan flere signaturer aggregeres til en enkelt gyldig signatur. Dermed, i tilfellet med en multisignaturtransaksjon, kan et sett med deltakere signere med en enkelt signatur og en enkelt aggregert offentlig nøkkel. Dette reduserer betydelig lagrings- og beregningskostnader for nettverket, ettersom hver node bare trenger å verifisere en enkelt signatur.

![CYP201](assets/fr/025.webp)

I tillegg forbedrer signaturaggregering personvernet. Med Schnorr blir det umulig å skille en multisignaturtransaksjon fra en standard enkeltsignaturtransaksjon. Denne homogeniteten gjør kjedeanalyse vanskeligere, da den begrenser evnen til å identifisere lommebokavtrykk.
Til slutt tilbyr Schnorr også muligheten for samtidig verifisering. Ved å verifisere flere signaturer samtidig, kan noder oppnå effektivitet, spesielt for blokker som inneholder mange transaksjoner. Denne optimaliseringen reduserer tiden og ressursene som trengs for å validere en blokk. I tillegg er ikke Schnorr-signaturer formbare, i motsetning til signaturer produsert med ECDSA. Dette betyr at en angriper ikke kan modifisere en gyldig signatur for å skape en annen gyldig signatur for samme melding og samme offentlige nøkkel. Denne sårbarheten var tidligere til stede på Bitcoin og forhindret spesielt den sikre implementeringen av Lightning Network. Det ble løst for ECDSA med SegWit-softforken i 2017, som innebærer å flytte signaturene til en separat database fra transaksjonene for å forhindre deres formbarhet.

### Hvorfor valgte Satoshi ECDSA?

Som vi har sett, valgte Satoshi opprinnelig å implementere ECDSA for digitale signaturer på Bitcoin. Likevel har vi også sett at Schnorr er overlegen ECDSA på mange områder, og dette protokollet ble opprettet av Claus-Peter Schnorr i 1989, 20 år før oppfinnelsen av Bitcoin.

Vel, vi vet egentlig ikke hvorfor Satoshi ikke valgte det, men en sannsynlig hypotese er at dette protokollet var under patent frem til 2008. Selv om Bitcoin ble opprettet et år senere, i januar 2009, var det ingen åpen kildekode-standardisering for Schnorr-signaturer tilgjengelig på det tidspunktet. Kanskje anså Satoshi det som tryggere å bruke ECDSA, som allerede var mye brukt og testet i åpen kildekode-programvare og hadde flere anerkjente implementasjoner (spesielt OpenSSL-biblioteket brukt frem til 2015 på Bitcoin Core, deretter erstattet av libsecp256k1 i versjon 0.10.0). Eller kanskje han rett og slett ikke var klar over at dette patentet skulle utløpe i 2008. Uansett virker den mest sannsynlige hypotesen å være relatert til dette patentet og det faktum at ECDSA hadde en bevist historie og var lettere å implementere.

## The sighash flags

<chapterId>231c41a2-aff2-4655-9048-47b6d2d83d64</chapterId>

Som vi har sett i tidligere kapitler, brukes digitale signaturer ofte til å låse opp skriptet til en inngang. I signeringsprosessen er det nødvendig å inkludere de signerte dataene i beregningen, betegnet i våre eksempler med meldingen $m$. Disse dataene, når de er signert, kan ikke endres uten å gjøre signaturen ugyldig. Faktisk, enten for ECDSA eller Schnorr, må signaturens verifiserer inkludere den samme meldingen $m$ i sin beregning. Hvis den avviker fra meldingen $m$ som opprinnelig ble brukt av signereren, vil resultatet være feil og signaturen vil bli ansett som ugyldig. Det sies da at en signatur dekker visse data og beskytter dem, på en måte, mot uautoriserte endringer.

### Hva er et sighash-flagg?

I det spesifikke tilfellet med Bitcoin har vi sett at meldingen $m$ tilsvarer transaksjonen. Men i virkeligheten er det litt mer komplekst. Faktisk, takket være sighash-flagg, er det mulig å velge spesifikke data innenfor transaksjonen som vil bli dekket eller ikke av signaturen.
"Sighash-flagget" er dermed en parameter lagt til hver inngang, som tillater bestemmelsen av komponentene i en transaksjon som er dekket av den tilknyttede signaturen. Disse komponentene er inngangene og utgangene. Valget av sighash-flagget bestemmer dermed hvilke innganger og utganger av transaksjonen som er fastsatt av signaturen og hvilke som fortsatt kan endres uten å ugyldiggjøre den. Denne mekanismen tillater signaturer å forplikte transaksjonsdata i henhold til signererens intensjoner.
Åpenbart, når transaksjonen er bekreftet på blokkjeden, blir den uforanderlig, uavhengig av hvilke sighash-flagg som er brukt. Muligheten for modifikasjon via sighash-flaggene er begrenset til perioden mellom signeringen og bekreftelsen.
Generelt tilbyr ikke lommebokprogramvare deg muligheten til manuelt å endre sighash-flagget for dine inndata når du konstruerer en transaksjon. Som standard er `SIGHASH_ALL` satt. Personlig kjenner jeg bare til Sparrow Wallet som tillater denne modifikasjonen fra brukergrensesnittet.

### Hva er de eksisterende sighash-flaggene på Bitcoin?

På Bitcoin er det først og fremst 3 grunnleggende sighash-flagg:

- `SIGHASH_ALL` (`0x01`): Signaturen gjelder for alle inndataene og alle utdataene i transaksjonen. Transaksjonen er dermed helt dekket av signaturen og kan ikke lenger modifiseres. `SIGHASH_ALL` er det mest brukte sighash-flagget i daglige transaksjoner når man enkelt ønsker å gjennomføre en transaksjon uten at den kan modifiseres.

![CYP201](assets/fr/026.webp)

I alle diagrammene i dette kapittelet representerer oransje farge elementene dekket av signaturen, mens svart farge indikerer de som ikke er det.

- `SIGHASH_NONE` (`0x02`): Signaturen dekker alle inndataene, men ingen av utdataene, noe som tillater modifikasjon av utdataene etter signaturen. I praksis er dette lik en blank sjekk. Signataren låser opp UTXOene i inndataene, men etterlater feltet for utdata helt modifiserbart. Enhver som kjenner til denne transaksjonen kan dermed legge til utdataene av sitt valg, for eksempel ved å spesifisere en mottaksadresse for å samle inn midlene som brukes av inndataene, og deretter kringkaste transaksjonen for å gjenopprette bitcoinene. Signaturen til eieren av inndataene vil ikke bli ugyldiggjort, ettersom den bare dekker inndataene.

![CYP201](assets/fr/027.webp)

- `SIGHASH_SINGLE` (`0x03`): Signaturen dekker alle inndata samt et enkelt utdata, som tilsvarer indeksen til det signerte inndataet. For eksempel, hvis signaturen låser opp _scriptPubKey_ for inndata #0, dekker den også utdata #0. Signaturen beskytter også alle andre inndata, som ikke lenger kan modifiseres. Imidlertid kan hvem som helst legge til et ekstra utdata uten å ugyldiggjøre signaturen, forutsatt at utdata #0, som er det eneste som er dekket av den, ikke er modifisert.
  ![CYP201](assets/fr/028.webp)

I tillegg til disse tre sighash-flaggene finnes det også modifikatoren `SIGHASH_ANYONECANPAY` (`0x80`). Denne modifikatoren kan kombineres med et grunnleggende sighash-flagg for å skape tre nye sighash-flagg:

- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Signaturen dekker et enkelt inndata mens den inkluderer alle utdataene i transaksjonen. Dette kombinerte sighash-flagget tillater for eksempel opprettelsen av en crowdfunding-transaksjon. Organisatoren forbereder utdataet med sin adresse og målbeløpet, og hver investor kan deretter legge til inndata for å finansiere dette utdataet. Når tilstrekkelige midler er samlet i inndataene for å tilfredsstille utdataet, kan transaksjonen kringkastes.

![CYP201](assets/fr/029.webp)

- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Signaturen dekker et enkelt inndata, uten å forplikte seg til noe utdata;

![CYP201](assets/fr/030.webp)

- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Signaturen dekker et enkelt inngangspunkt samt utgangspunktet som har samme indeks som dette inngangspunktet. For eksempel, hvis signaturen låser opp _scriptPubKey_ for inngang #3, vil den også dekke utgang #3. Resten av transaksjonen forblir modifiserbar, både med hensyn til andre innganger og andre utganger.
  ![CYP201](assets/fr/031.webp)

### Prosjekter for å legge til nye Sighash-flagg

For øyeblikket (2024) er kun de sighash-flaggene som er presentert i forrige seksjon brukbare på Bitcoin. Imidlertid vurderer noen prosjekter å legge til nye sighash-flagg. For eksempel, BIP118, foreslått av Christian Decker og Anthony Towns, introduserer to nye sighash-flagg: `SIGHASH_ANYPREVOUT` og `SIGHASH_ANYPREVOUTANYSCRIPT` (_AnyPrevOut = "Enhver Tidligere Utgang"_).

Disse to sighash-flaggene ville tilby en ekstra mulighet på Bitcoin: å skape signaturer som ikke dekker noen spesifikk inngang i transaksjonen.

![CYP201](assets/fr/032.webp)

Denne ideen ble opprinnelig formulert av Joseph Poon og Thaddeus Dryja i Lightning White Paper. Før den ble omdøpt, ble dette sighash-flagget kalt `SIGHASH_NOINPUT`.
Hvis dette sighash-flagget integreres i Bitcoin, vil det muliggjøre bruk av covenants, men det er også en obligatorisk forutsetning for å implementere Eltoo, et generelt protokoll for andre lag som definerer hvordan man felles kan håndtere eierskapet av en UTXO. Eltoo ble spesifikt designet for å løse problemene forbundet med mekanismene for å forhandle om tilstanden til Lightning-kanaler, det vil si mellom åpning og lukking.

For å fordype din kunnskap om Lightning Network, etter CYP201-kurset, anbefaler jeg på det sterkeste LNP201-kurset av Fanis Michalakis, som dekker emnet i detalj:

https://planb.network/courses/lnp201

I neste del foreslår jeg å oppdage hvordan den mnemoniske frasen som ligger til grunn for din Bitcoin-lommebok fungerer.

# Den mnemoniske frasen

<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>

## Utviklingen av Bitcoin-lommebøker

<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>

Nå som vi har utforsket hvordan hash-funksjoner og digitale signaturer fungerer, kan vi studere hvordan Bitcoin-lommebøker fungerer. Målet vil være å forestille seg hvordan en lommebok på Bitcoin er konstruert, hvordan den er dekomponert, og hvilke forskjellige informasjonsbiter som utgjør den brukes til. Denne forståelsen av lommebokmekanismene vil tillate deg å forbedre din bruk av Bitcoin når det gjelder sikkerhet og personvern.

Før vi dykker ned i de tekniske detaljene, er det essensielt å klargjøre hva som menes med "Bitcoin-lommebok" og å forstå dens nytte.

### Hva er en Bitcoin-lommebok?

I motsetning til tradisjonelle lommebøker, som lar deg lagre fysiske sedler og mynter, "inneholder" ikke en Bitcoin-lommebok bitcoins per se. Faktisk eksisterer ikke bitcoins i en fysisk eller digital form som kan lagres, men er representert ved enheter av konto avbildet i systemet i form av **UTXOs** (_Ubrukt Transaksjonsutgang_).
UTXOer representerer dermed fragmenter av bitcoins, i varierende størrelser, som kan brukes forutsatt at deres _scriptPubKey_ er oppfylt. For å bruke sine bitcoins, må en bruker gi en _scriptSig_ som låser opp _scriptPubKey_ knyttet til hans UTXO. Dette beviset er vanligvis gjennom en digital signatur, generert fra den private nøkkelen som tilsvarer den offentlige nøkkelen til stede i _scriptPubKey_. Dermed er det avgjørende elementet som brukeren må sikre, den private nøkkelen. Rollen til en Bitcoin-lommebok er nettopp å håndtere disse private nøklene på en sikker måte. I virkeligheten er dens rolle mer lik den til en nøkkelring enn en lommebok i tradisjonell forstand.

### JBOK Lommebøker (_Just a Bunch Of Keys_)

De første lommebøkene som ble brukt på Bitcoin, var JBOK (_Just a Bunch Of Keys_) lommebøker, som grupperte sammen privat genererte nøkler uavhengig og uten noen kobling mellom dem. Disse lommebøkene opererte på en enkel modell hvor hver privat nøkkel kunne låse opp en unik Bitcoin mottaksadresse.

![CYP201](assets/fr/033.webp)

Hvis man ønsket å bruke flere private nøkler, var det da nødvendig å lage like mange sikkerhetskopier for å sikre tilgang til midler i tilfelle problemer med enheten som hoster lommeboken. Hvis man bruker en enkelt privat nøkkel, kan denne lommebokstrukturen være tilstrekkelig, siden en enkelt sikkerhetskopi er nok. Dette stiller imidlertid et problem: på Bitcoin, er det sterkt frarådet å alltid bruke den samme private nøkkelen. Faktisk er en privat nøkkel assosiert med en unik adresse, og Bitcoin mottaksadresser er normalt designet for engangsbruk. Hver gang du mottar midler, bør du generere en ny tom adresse.

Denne begrensningen stammer fra Bitcoins personvernmodell. Ved å gjenbruke samme adresse, gjør det det lettere for eksterne observatører å spore alle mine Bitcoin-transaksjoner. Derfor er gjenbruk av en mottaksadresse sterkt frarådet. Imidlertid, for å ha flere adresser og offentlig skille våre transaksjoner, er det nødvendig å håndtere flere private nøkler. I tilfellet med JBOK-lommebøker, innebærer dette å skape like mange sikkerhetskopier som det er nye par med nøkler, en oppgave som raskt kan bli kompleks og vanskelig å opprettholde for brukere.

For å lære mer om Bitcoins personvernmodell og oppdage metoder for å beskytte ditt personvern, anbefaler jeg også å følge mitt BTC204 kurs på Plan ₿ Network:

https://planb.network/courses/btc204

### HD Lommebøker (_Hierarchical Deterministic_)

For å adressere begrensningen av JBOK-lommebøker, ble en ny lommebokstruktur senere tatt i bruk. I 2012 introduserte Pieter Wuille en forbedring med BIP32, som introduserer hierarkiske deterministiske lommebøker. Prinsippet med en HD-lommebok er å avlede alle private nøkler fra en enkelt informasjonskilde, kalt et frø, på en deterministisk og hierarkisk måte. Dette frøet genereres tilfeldig når lommeboken opprettes og utgjør en unik sikkerhetskopi som tillater gjenoppretting av alle lommebokens private nøkler. Dermed kan brukeren generere et svært stort antall private nøkler for å unngå adressegjenbruk og bevare sitt personvern, samtidig som det kun er nødvendig å lage en enkelt sikkerhetskopi av lommeboken via frøet.
![CYP201](assets/fr/034.webp)

I HD-lommebøker utføres nøkkelavledning i henhold til en hierarkisk struktur som tillater nøkler å bli organisert i avledningssubrom, hvert subspace kan videre deles opp, for å lette fondshåndtering og interoperabilitet mellom forskjellige lommebokprogramvarer. I dag er denne standarden adoptert av det store flertallet av Bitcoin-brukere. Av denne grunn vil vi undersøke den i detalj i de følgende kapitlene.

### BIP39-standarden: Den Mnemoniske Frasen

I tillegg til BIP32 standardiserer BIP39 formatet for frøet som en mnemonic frase, for å lette backup og lesbarhet for brukere. Den mnemonic frasen, også kalt en gjenopprettingsfrase eller 24-ords frase, er en sekvens av ord hentet fra en forhåndsdefinert liste som sikkert koder lommebokens frø.
Den mnemonic frasen forenkler betraktelig backup for brukeren. I tilfelle tap, skade eller tyveri av enheten som huser lommeboken, gjør det å kun kjenne denne mnemonic frasen det mulig å gjenskape lommeboken og gjenopprette tilgangen til alle midlene sikret av den.

I de kommende kapitlene vil vi utforske de interne mekanismene til HD-lommebøker, inkludert mekanismer for nøkkelavledning og de forskjellige mulige hierarkiske strukturene. Dette vil tillate deg å bedre forstå de kryptografiske grunnlagene som sikkerheten til midler på Bitcoin er basert på. Og for å starte, i neste kapittel, foreslår jeg at vi oppdager rollen til entropi i bunnen av lommeboken din.

## Entropi og Tilfeldig Nummer

<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>
Moderne HD-lommebøker (deterministiske og hierarkiske) er avhengige av et enkelt innledende stykke informasjon kalt "entropi" for å deterministisk generere hele settet med lommeboknøkler. Denne entropien er et pseudo-tilfeldig nummer hvis kaosnivå delvis bestemmer sikkerheten til lommeboken.

### Definisjon av Entropi

Entropi, i konteksten av kryptografi og informasjon, er et kvantitativt mål på usikkerheten eller uforutsigbarheten forbundet med en datakilde eller en tilfeldig prosess. Det spiller en viktig rolle i sikkerheten til kryptografiske systemer, spesielt i genereringen av nøkler og tilfeldige tall. Høy entropi sikrer at de genererte nøklene er tilstrekkelig uforutsigbare og motstandsdyktige mot brute force-angrep, der en angriper prøver alle mulige kombinasjoner for å gjette nøkkelen.

I konteksten av Bitcoin brukes entropi til å generere frøet. Når man oppretter en deterministisk og hierarkisk lommebok, blir konstruksjonen av den mnemonic frasen gjort fra et tilfeldig nummer, selv avledet fra en kilde til entropi. Frasen brukes deretter til å generere flere private nøkler, på en deterministisk og hierarkisk måte, for å skape utgiftsbetingelser på UTXOer.

### Metoder for å Generere Entropi

Den innledende entropien som brukes for en HD-lommebok er generelt 128 bits eller 256 bits, der:

- **128 bits entropi** tilsvarer en mnemonic frase på **12 ord**;
- **256 bits entropi** tilsvarer en mnemonic frase på **24 ord**.

I de fleste tilfeller genereres dette tilfeldige nummeret automatisk av lommebokprogramvaren ved hjelp av en PRNG (_Pseudo-Random Number Generator_). PRNG-er er en kategori algoritmer som brukes til å generere sekvenser av tall fra en innledende tilstand, som har egenskaper som nærmer seg det til et tilfeldig tall, uten faktisk å være ett. En god PRNG må ha egenskaper som utgangsuniformitet, uforutsigbarhet og motstand mot prediktive angrep. I motsetning til ekte tilfeldige tallgeneratorer (TRNG), er PRNG-er deterministiske og reproduserbare.

![CYP201](assets/fr/035.webp)

Et alternativ er å manuelt generere entropien, som tilbyr bedre kontroll, men er også mye risikofylt. Jeg fraråder sterkt å generere entropien for din HD-lommebok selv.

I neste kapittel vil vi se hvordan vi går fra et tilfeldig nummer til en mnemonic frase på 12 eller 24 ord.

## Den Mnemonic Frasen

<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>
Mnemonisk frase, også kalt "seed phrase", "recovery phrase", "secret phrase", eller "24-ords frase", er en sekvens som vanligvis består av 12 eller 24 ord, som genereres fra entropi. Den brukes til deterministisk å avlede alle nøklene til en HD-lommebok. Dette betyr at fra denne frasen, er det mulig å deterministisk generere og gjenskape alle de private og offentlige nøklene til Bitcoin-lommeboken, og dermed få tilgang til midlene som er beskyttet med den. Formålet med den mnemoniske frasen er å tilby et middel for sikkerhetskopiering og gjenoppretting av bitcoins som er både sikkert og enkelt å bruke. Den ble introdusert i standarder i 2013 med BIP39.
La oss sammen oppdage hvordan vi går fra entropi til en mnemonisk frase.

### Sjekksummen

For å transformere entropi til en mnemonisk frase, må man først legge til en sjekksum (eller "kontrollsum") på slutten av entropien. Denne sjekksummen er en kort sekvens av bits som sikrer integriteten til dataene ved å verifisere at ingen utilsiktet modifikasjon har blitt introdusert.

For å beregne sjekksummen, anvendes SHA256 hash-funksjonen på entropien (bare én gang; dette er et av de sjeldne tilfellene i Bitcoin der en enkelt SHA256 hash brukes i stedet for en dobbel hash). Denne operasjonen produserer en 256-bits hash. Sjekksummen består av de første bitene av denne hashen, og dens lengde avhenger av entropiens lengde, i henhold til følgende formel:

$$
\text{CS} = \frac{\text{ENT}}{32}
$$

hvor $\text{ENT}$ representerer lengden av entropien i bits, og $\text{CS}$ lengden av sjekksummen i bits.

For eksempel, for en entropi på 256 bits, tas de første 8 bitene av hashen for å danne sjekksummen:

$$
\text{CS} = \frac{256}{32} = 8 \text{ bits}
$$

Når sjekksummen er beregnet, blir den konkatenert med entropien for å oppnå en utvidet bitsekvens notert $\text{ENT} \Vert \text{CS}$ ("konkatenere" betyr å sette ende-til-ende).

![CYP201](assets/fr/036.webp)

### Korrespondanse mellom Entropien og den Mnemoniske Frasen

Antall ord i den mnemoniske frasen avhenger av størrelsen på den opprinnelige entropien, som illustrert i følgende tabell med:

- $\text{ENT}$: størrelsen i bits av entropien;
- $\text{CS}$: størrelsen i bits av sjekksummen;
- $w$: antall ord i den endelige mnemoniske frasen.

$$
\begin{array}{|c|c|c|c|}
\hline
\text{ENT} & \text{CS} & \text{ENT} \Vert \text{CS} & w \\
\hline
128 & 4 & 132 & 12 \\
160 & 5 & 165 & 15 \\
192 & 6 & 198 & 18 \\
224 & 7 & 231 & 21 \\
256 & 8 & 264 & 24 \\
\hline
\end{array}
$$

For eksempel, for en entropi på 256 bits, er resultatet $\text{ENT} \Vert \text{CS}$ 264 bits og gir en mnemonisk frase på 24 ord.

### Konvertering av den Binære Sekvensen til en Mnemonisk Frase

Bitsekvensen $\text{ENT} \Vert \text{CS}$ deles deretter inn i segmenter på 11 bits. Hvert 11-bits segment, når det er konvertert til desimal, tilsvarer et tall mellom 0 og 2047, som angir posisjonen til et ord [i en liste over 2048 ord standardisert av BIP39](https://github.com/Planb-Network/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf).

![CYP201](assets/fr/037.webp)
For eksempel, for en 128-bit entropi, er kontrollsummen 4 bit, og dermed måler den totale sekvensen 132 bit. Den er delt inn i 12 segmenter på 11 bit (de oransje bitene betegner kontrollsummen):
![CYP201](assets/fr/038.webp)

Hvert segment konverteres deretter til et desimaltall som representerer et ord i listen. For eksempel er det binære segmentet `01011010001` ekvivalent i desimal til `721`. Ved å legge til 1 for å justere seg med listens indeksering (som starter på 1 og ikke 0), gir dette ordets rang `722`, som er "*focus*" i listen.

![CYP201](assets/fr/039.webp)

Denne korrespondansen gjentas for hvert av de 12 segmentene, for å oppnå en 12-ords frase.

![CYP201](assets/fr/040.webp)

### Egenskaper ved BIP39 ordlisten

En spesiell egenskap ved BIP39-ordlisten er at intet ord deler de samme første fire bokstavene i samme rekkefølge med et annet ord. Dette betyr at det å notere kun de første fire bokstavene av hvert ord er tilstrekkelig for å lagre den mnemoniske frasen. Dette kan være interessant for å spare plass, spesielt for de som ønsker å gravere den på et metallstøtte.

Denne listen på 2048 ord finnes på flere språk. Disse er ikke enkle oversettelser, men distinkte ord for hvert språk. Det er imidlertid sterkt anbefalt å holde seg til den engelske versjonen, ettersom versjoner på andre språk generelt ikke støttes av lommebokprogramvare.

### Hvilken lengde bør du velge for din mnemoniske frase?
For å bestemme den optimale lengden på din mnemoniske frase, må man vurdere den faktiske sikkerheten den gir. En 12-ords frase sikrer 128 bits sikkerhet, mens en 24-ords frase tilbyr 256 bits.

Men, denne forskjellen i frasenivå-sikkerhet forbedrer ikke den generelle sikkerheten til en Bitcoin-lommebok, ettersom de private nøklene som er avledet fra denne frasen kun nyter godt av 128 bits sikkerhet. Faktisk, som vi har sett tidligere, genereres Bitcoin private nøkler fra tilfeldige tall (eller avledet fra en tilfeldig kilde) som varierer mellom $1$ og $n-1$, hvor $n$ representerer ordenen til generasjonspunktet $G$ på secp256k1-kurven, et tall litt mindre enn $2^{256}$. Man kan derfor tenke at disse private nøklene tilbyr 256 bits sikkerhet. Imidlertid ligger deres sikkerhet i vanskeligheten med å finne en privat nøkkel fra dens tilknyttede offentlige nøkkel, en vanskelighet etablert av det matematiske problemet med den diskrete logaritmen på elliptiske kurver (*ECDLP*). Til dags dato er den best kjente algoritmen for å løse dette problemet Pollards rho-algoritme, som reduserer antall operasjoner som trengs for å bryte en nøkkel til kvadratroten av dens størrelse.

For 256-bits nøkler, slik som de som brukes på Bitcoin, reduserer Pollards rho-algoritme dermed kompleksiteten til $2^{128}$ operasjoner:


$$

O(\sqrt{2^{256}}) = O(2^{128})

$$

Derfor anses det at en privat nøkkel brukt på Bitcoin tilbyr 128 bits sikkerhet.

Som et resultat gir ikke å velge en 24-ords frase ekstra beskyttelse for lommeboken, ettersom 256 bits sikkerhet på frasen er meningsløs hvis de avledede nøklene kun tilbyr 128 bits sikkerhet. For å illustrere dette prinsippet, er det som å ha et hus med to dører: en gammel tre dør og en forsterket dør. I tilfelle av et innbrudd, ville den forsterkede døren være til ingen nytte, siden inntrengeren ville gå gjennom tre døren. Dette er en analog situasjon her.
En 12-ords frase, som også tilbyr 128 bits sikkerhet, er derfor for øyeblikket tilstrekkelig for å beskytte dine bitcoins mot ethvert tyveriforsøk. Så lenge den digitale signaturalgoritmen ikke endres for å bruke større nøkler eller for å stole på et matematisk problem annet enn ECDLP, forblir en 24-ords frase overflødig. Dessuten øker en lengre frase risikoen for tap under sikkerhetskopiering: en sikkerhetskopi som er halvparten så kort er alltid enklere å håndtere.
For å gå videre og lære konkret hvordan man manuelt genererer en test mnemonisk frase, anbefaler jeg deg å oppdage denne opplæringen:

https://planb.network/tutorials/wallet/generate-mnemonic-phrase
Før vi fortsetter med derivasjonen av lommeboken fra denne mnemoniske frasen, vil jeg introdusere deg, i det følgende kapittelet, til BIP39-passfrasen, ettersom den spiller en rolle i derivasjonsprosessen, og den er på samme nivå som den mnemoniske frasen.
## Passfrasen
<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>

Som vi nettopp har sett, genereres HD-lommebøker fra en mnemonisk frase som typisk består av 12 eller 24 ord. Denne frasen er veldig viktig fordi den muliggjør gjenopprettingen av alle nøklene til en lommebok i tilfelle dens fysiske enhet (som en maskinvarelommebok, for eksempel) går tapt. Imidlertid utgjør den et enkelt feilpunkt, fordi hvis den blir kompromittert, kan en angriper stjele alle bitcoinsene. Dette er hvor BIP39-passfrasen kommer inn i bildet.

### Hva er en BIP39-passfrase?

Passfrasen er et valgfritt passord, som du fritt kan velge, som legges til den mnemoniske frasen i nøkkelderivasjonsprosessen for å forbedre lommebokens sikkerhet.

Vær forsiktig, passfrasen bør ikke forveksles med PIN-koden til din maskinvarelommebok eller passordet som brukes for å låse opp tilgangen til lommeboken din på datamaskinen. I motsetning til alle disse elementene, spiller passfrasen en rolle i derivasjonen av lommebokens nøkler. **Dette betyr at uten den, vil du aldri kunne gjenopprette dine bitcoins.**

Passfrasen fungerer i tandem med den mnemoniske frasen, og endrer frøet som nøklene genereres fra. Så selv om noen får tak i din 12 eller 24-ords frase, uten passfrasen, kan de ikke få tilgang til midlene dine. Bruk av en passfrase skaper i hovedsak en ny lommebok med distinkte nøkler. Å endre (selv litt) passfrasen vil generere en annen lommebok.

![CYP201](assets/fr/041.webp)

### Hvorfor bør du bruke en passfrase?

Passfrasen er vilkårlig og kan være hvilken som helst kombinasjon av tegn valgt av brukeren. Bruk av en passfrase tilbyr dermed flere fordeler. Først og fremst reduserer det alle risikoer forbundet med kompromittering av den mnemoniske frasen ved å kreve en andre faktor for å få tilgang til midlene (innbrudd, tilgang til hjemmet ditt, osv.).

Videre kan den brukes strategisk for å skape en avledningslommebok, for å møte fysiske begrensninger for å stjele midlene dine som den beryktede "_$5 skiftenøkkelangrepet_". I dette scenarioet er ideen å ha en lommebok uten en passfrase som inneholder bare en liten mengde bitcoins, nok til å tilfredsstille en potensiell angriper, mens man har en skjult lommebok. Denne sistnevnte bruker samme mnemoniske frase, men er sikret med en ekstra passfrase.
Til slutt er bruken av en passfrase interessant når man ønsker å kontrollere tilfeldigheten av genereringen av HD-lommebokens frø.
### Hvordan velge en god passfrase?

For at passfrasen skal være effektiv, må den være tilstrekkelig lang og tilfeldig. Som med et sterkt passord, anbefaler jeg å velge en passfrase som er så lang og tilfeldig som mulig, med en mangfoldighet av bokstaver, tall og symboler for å gjøre ethvert brute force-angrep umulig.
Det er også viktig å lagre denne passfrasen på riktig måte, på samme måte som den mnemoniske frasen. **Å miste den betyr å miste tilgangen til dine bitcoins**. Jeg råder sterkt mot å bare huske den i hodet, da dette urimelig øker risikoen for tap. Det ideelle er å skrive den ned på et fysisk medium (papir eller metall) separat fra den mnemoniske frasen. Denne sikkerhetskopien må åpenbart oppbevares på et annet sted enn der din mnemoniske frase er lagret for å forhindre at begge blir kompromittert samtidig.
![CYP201](assets/fr/042.webp)

I den følgende seksjonen vil vi oppdage hvordan disse to elementene som er grunnlaget for lommeboken din — den mnemoniske frasen og passfrasen — brukes til å utlede nøkkelparene som brukes i *scriptPubKey* som låser dine UTXOer.

# Opprettelse av Bitcoin-lommebøker
<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>

## Opprettelse av Seed og Master Key
<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>

Når den mnemoniske frasen og den valgfrie passfrasen er generert, kan prosessen med å utlede en Bitcoin HD-lommebok begynne. Den mnemoniske frasen konverteres først til en seed som utgjør grunnlaget for alle nøklene i lommeboken.

![CYP201](assets/fr/043.webp)

### Seedet til en HD-lommebok

BIP39-standarden definerer seedet som en 512-bits sekvens, som tjener som utgangspunkt for utledningen av alle nøklene i en HD-lommebok. Seedet utledes fra den mnemoniske frasen og den mulige passfrasen ved hjelp av **PBKDF2**-algoritmen (*Password-Based Key Derivation Function 2*) som vi allerede har diskutert i kapittel 3.3. I denne utledningsfunksjonen vil vi bruke følgende parametere:

- $m$ : den mnemoniske frasen;
- $p$ : en valgfri passfrase valgt av brukeren for å øke sikkerheten til seedet. Hvis det ikke er noen passfrase, er dette feltet tomt;
- $\text{PBKDF2}$ : utledningsfunksjonen med $\text{HMAC-SHA512}$ og $2048$ iterasjoner;
- $s$: det 512-bits lommebokseedet.
Uavhengig av lengden på den mnemoniske frasen som er valgt (132 bits eller 264 bits), vil PBKDF2-funksjonen alltid produsere en 512-bits utgang, og seedet vil derfor alltid være av denne størrelsen.

### Seed-utledningsskjema med PBKDF2

Følgende ligning illustrerer utledningen av seedet fra den mnemoniske frasen og passfrasen:


$$

s = \text{PBKDF2}_{\text{HMAC-SHA512}}(m, p, 2048)

$$

![CYP201](assets/fr/044.webp)

Verdien av seedet er dermed påvirket av verdien av den mnemoniske frasen og passfrasen. Ved å endre passfrasen, oppnås et annet seed. Men, med samme mnemoniske frase og passfrase, genereres det samme seedet alltid, siden PBKDF2 er en deterministisk funksjon. Dette sikrer at de samme parene av nøkler kan hentes gjennom våre sikkerhetskopier.

**Merk:** I dagligtale refererer begrepet "seed" ofte, ved misbruk av språk, til den mnemoniske frasen. Faktisk, i fravær av en passfrase, er den ene ganske enkelt kodingen av den andre. Men, som vi har sett, i den tekniske virkeligheten til lommebøker, er seedet og den mnemoniske frasen faktisk to distinkte elementer.

Nå som vi har vårt seed, kan vi fortsette med utledningen av vår Bitcoin-lommebok.
### Den Mesterlige Nøkkelen og den Mesterlige Kjedekoden
Når frøet er oppnådd, er neste steg i å utlede en HD-lommebok å beregne den mesterlige private nøkkelen og den mesterlige kjedekoden, som vil representere dybde 0 i vår lommebok.

For å oppnå den mesterlige private nøkkelen og den mesterlige kjedekoden, anvendes HMAC-SHA512-funksjonen på frøet, ved bruk av en fast nøkkel "*Bitcoin Seed*" identisk for alle Bitcoin-brukere. Denne konstanten er valgt for å sikre at nøkkelutledningene er spesifikke for Bitcoin. Her er elementene:
- $\text{HMAC-SHA512}$: utledningsfunksjonen;
- $s$: det 512-biters lommebokfrøet;
- $\text{"Bitcoin Seed"}$: den felles utledningskonstanten for alle Bitcoin-lommebøker.


$$

\text{output} = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)

$$

Utgangen av denne funksjonen er derfor 512 bits. Den deles deretter inn i 2 deler:
- De venstre 256 bitene danner **den mesterlige private nøkkelen**;
- De høyre 256 bitene danner **den mesterlige kjedekoden**.
Matematisk kan disse to verdiene noteres som følger med $k_M$ som den mesterlige private nøkkelen og $C_M$ som den mesterlige kjedekoden:
$$

k_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[:256]}

$$


$$

C_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[256:]}

$$

![CYP201](assets/fr/045.webp)

### Rollen til den Mesterlige Nøkkelen og Kjedekoden

Den mesterlige private nøkkelen anses som foreldrenøkkelen, hvorfra alle avledede private nøkler — barn, barnebarn, oldebarn, osv. — vil bli generert. Den representerer nullnivået i hierarkiet av utledning.

Den mesterlige kjedekoden, på den andre siden, introduserer en ekstra kilde til entropi i nøkkelutledningsprosessen for barn, for å motvirke visse potensielle angrep. Videre, i HD-lommeboken, har hvert par av nøkler en unik kjedekode assosiert med seg, som også brukes til å utlede barnenøkler fra dette paret, men vi vil diskutere dette mer detaljert i de kommende kapitlene.

Før vi fortsetter med utledningen av HD-lommeboken med de følgende elementene, ønsker jeg, i neste kapittel, å introdusere deg for utvidede nøkler, som ofte forveksles med den mesterlige nøkkelen. Vi vil se hvordan de er konstruert og hvilken rolle de spiller i Bitcoin-lommeboken.

## Utvidede Nøkler
<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>

En utvidet nøkkel er ganske enkelt sammensetningen av en nøkkel (enten privat eller offentlig) og dens assosierte kjedekode. Denne kjedekoden er essensiell for utledningen av barnenøkler fordi, uten den, er det umulig å utlede barnenøkler fra en foreldrenøkkel, men vi vil oppdage denne prosessen mer presist i neste kapittel. Disse utvidede nøklene tillater dermed å aggregere all nødvendig informasjon for å utlede barnenøkler, og forenkler dermed kontoadministrasjonen innenfor en HD-lommebok.

![CYP201](assets/fr/046.webp)

Den utvidede nøkkelen består av to deler:
- Nyttelasten, som inneholder den private eller offentlige nøkkelen samt den assosierte kjedekoden;
- Metadata, som er ulike informasjonsstykker for å lette interoperabilitet mellom programvare og forbedre forståelsen for brukeren.

### Hvordan Utvidede Nøkler Fungerer
Når den utvidede nøkkelen inneholder en privat nøkkel, refereres det til som en utvidet privat nøkkel. Den er gjenkjennelig ved sitt prefiks som inneholder nevningen `prv`. I tillegg til den private nøkkelen, inneholder den utvidede private nøkkelen også den tilknyttede kjedekoden. Med denne typen utvidet nøkkel er det mulig å utlede alle typer barns private nøkler, og derfor ved tillegg og dobling av punkter på elliptiske kurver, tillater det også utledning av helheten av barns offentlige nøkler.
Når den utvidede nøkkelen ikke inneholder en privat nøkkel, men i stedet en offentlig nøkkel, refereres det til som en utvidet offentlig nøkkel. Den er gjenkjennelig ved sitt prefiks som inneholder nevningen `pub`. Åpenbart, i tillegg til nøkkelen, inneholder den også den tilknyttede kjedekoden. I motsetning til den utvidede private nøkkelen, tillater den utvidede offentlige nøkkelen utledning av kun "normale" barns offentlige nøkler (det betyr at den ikke kan utlede "hardened" barns nøkler). Vi vil se i det følgende kapittelet hva disse "normale" og "hardened" kvalifikatorene betyr.

Men i alle tilfeller tillater ikke den utvidede offentlige nøkkelen utledning av barns private nøkler. Derfor, selv om noen har tilgang til en `xpub`, vil de ikke kunne bruke de tilknyttede midlene, ettersom de ikke vil ha tilgang til de tilsvarende private nøklene. De kan kun utlede barns offentlige nøkler for å observere de tilknyttede transaksjonene.

For det følgende vil vi adoptere følgende notasjon:
- $K_{\text{PAR}}$: en forelder offentlig nøkkel;
- $k_{\text{PAR}}$: en forelder privat nøkkel;
- $C_{\text{PAR}}$: en forelder kjedekode;
- $C_{\text{CHD}}$: en barn kjedekode;
- $K_{\text{CHD}}^n$: en normal barn offentlig nøkkel;
- $k_{\text{CHD}}^n$: en normal barn privat nøkkel;
- $K_{\text{CHD}}^h$: en "hardened" barn offentlig nøkkel;
- $k_{\text{CHD}}^h$: en "hardened" barn privat nøkkel.

![CYP201](assets/fr/047.webp)

### Konstruksjon av en Utvidet Nøkkel

En utvidet nøkkel er strukturert som følger:
- **Version**: Versjonskode for å identifisere nøkkelens natur (`xprv`, `xpub`, `yprv`, `ypub`...). Vi vil se på slutten av dette kapittelet hva bokstavene `x`, `y`, og `z` tilsvarer.
- **Depth**: Hierarkisk nivå i HD-lommeboken i forhold til hovednøkkelen (0 for hovednøkkelen).
- **Parent Fingerprint**: De første 4 bytene av HASH160-hashen av den forelder offentlige nøkkelen brukt til å utlede nøkkelen til stede i nyttelasten.
- **Index Number**: Identifikator av barnet blant søsken nøkler, det vil si, blant alle nøkler på samme utledningsnivå som har samme foreldrenøkler.
- **Chain Code**: En unik 32-byte kode for utledning av barns nøkler.
- **Key**: Den private nøkkelen (prefikset med 1 byte for størrelse) eller den offentlige nøkkelen.
- **Checksum**: En sjekksum beregnet med HASH256-funksjonen (dobbel SHA256) legges også til, som tillater verifisering av den utvidede nøkkelens integritet under dens overføring eller lagring.

Det komplette formatet av en utvidet nøkkel er derfor 78 bytes uten sjekksummen, og 82 bytes med sjekksummen. Den konverteres deretter til Base58 for å produsere en representasjon som er lett lesbar for brukere. Base58-formatet er det samme som det som brukes for *Legacy* mottaksadresser (før *SegWit*).

| Element           | Beskrivelse                                                                                                        | Størrelse      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ | --------- |
| Versjon           | Indikerer om nøkkelen er offentlig (`xpub`, `ypub`) eller privat (`xprv`, `zprv`), samt versjonen av den utvidede nøkkelen | 4 bytes   |
| Dybde             | Nivå i hierarkiet i forhold til hovednøkkelen                                                                      | 1 byte    |
| Foreldreavtrykk   | De første 4 bytes av HASH160 av den offentlige nøkkelen til forelderen                                              | 4 bytes   |
| Indeksnummer      | Posisjonen til nøkkelen i rekkefølgen av barn                                                                       | 4 bytes   |
| Kjedekode         | Brukes til å avlede barnenøkler                                                                                     | 32 bytes  |
| Nøkkel            | Den private nøkkelen (med et 1-byte prefiks) eller den offentlige nøkkelen                                          | 33 bytes  |
| Sjekksum          | Sjekksum for å verifisere integritet                                                                                | 4 bytes   |

Hvis det legges til ett byte til den private nøkkelen alene, er det fordi den komprimerte offentlige nøkkelen er lengre enn den private nøkkelen med ett byte. Dette ekstra bytet, lagt til i begynnelsen av den private nøkkelen som `0x00`, utjevner størrelsen deres, og sikrer at nyttelasten av den utvidede nøkkelen er av samme lengde, enten det er en offentlig eller en privat nøkkel.

### Prefikser for Utvidede Nøkler
Som vi nettopp har sett, inkluderer utvidede nøkler et prefiks som indikerer både versjonen av den utvidede nøkkelen og dens natur. Notasjonen `pub` indikerer at det refererer til en utvidet offentlig nøkkel, og notasjonen `prv` indikerer en utvidet privat nøkkel. Den ekstra bokstaven ved basen av den utvidede nøkkelen hjelper til med å indikere om standarden som følges er Legacy, SegWit v0, SegWit v1, osv.
Her er en oppsummering av de brukte prefiksene og deres betydninger:

| Base 58 Prefix  | Base 16 Prefix  | Network | Purpose             | Associated Scripts  | Derivation            | Key Type     |
| --------------- | --------------- | ------- | ------------------- | ------------------- | --------------------- | ------------ |
| `xpub`          | `0488b21e`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | public       |
| `xprv`          | `0488ade4`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | private      |
| `tpub`          | `043587cf`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | public       |
| `tprv`          | `04358394`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | private      |
| `ypub`          | `049d7cb2`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | public       |
| `yprv`          | `049d7878`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | private      |
| `upub`          | `049d7cb2`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | public       |
| `uprv`          | `044a4e28`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | private      |
| `zpub`          | `04b24746`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | public       |
| `zprv`          | `04b2430c`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | private      |
| `vpub`          | `045f1cf6`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | public       |
| `vprv`          | `045f18bc`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | private      |


### Detaljer om en utvidet nøkkels elementer

For å bedre forstå den interne strukturen til en utvidet nøkkel, la oss ta en som et eksempel og bryte den ned. Her er en utvidet nøkkel:

- **I Base58**:

```text
xpub6CTNzMUkzpurBWaT4HQoYzLP4uBbGJuWY358Rj7rauiw4rMHCyq3Rfy9w4kyJXJzeFfyrKLUar2rUCukSiDQFa7roTwzjiAhyQAdPLEjqHT
```

- **I heksadesimal**:

```text
0488B21E036D5601AD80000000C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A89303772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF50658051F067C3A
```

Denne utvidede nøkkelen brytes ned i flere distinkte elementer:

1. **Versjon**: `0488B21E`

De første 4 bytene er versjonen. Her tilsvarer det en utvidet offentlig nøkkel på Hovednett med et avledningsformål av enten *Legacy* eller *SegWit v1*.

2. **Dybde**: `03`

Dette feltet indikerer det hierarkiske nivået til nøkkelen innenfor HD-lommeboken. I dette tilfellet betyr en dybde på `03` at denne nøkkelen er tre nivåer av avledning under hovednøkkelen.

3. **Foreldres fingeravtrykk**: `6D5601AD`
Disse er de første 4 bytene av HASH160-hashen av den overordnede offentlige nøkkelen som ble brukt til å utlede denne `xpub`.
4. **Indeksnummer**: `80000000`

Dette indeksnummeret indikerer nøkkelens posisjon blant forelderens barn. `0x80`-prefikset indikerer at nøkkelen er utledet på en hardnet måte, og siden resten er fylt med nuller, indikerer det at denne nøkkelen er den første blant sine mulige søsken.

5. **Kjedekode**: `C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A893`
6. **Offentlig Nøkkel**: `03772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF5065805`
7. **Kontrollsum**: `1F067C3A`

Kontrollsummen tilsvarer de første 4 bytene av hashen (dobbel SHA256) av alt annet.

I dette kapittelet oppdaget vi at det finnes to forskjellige typer barne-nøkler. Vi lærte også at utledningen av disse barne-nøklene krever en nøkkel (enten privat eller offentlig) og dens kjedekode. I neste kapittel vil vi undersøke nærmere naturen til disse forskjellige typene nøkler og hvordan man kan utlede dem fra deres foreldrenøkkel og kjedekode.

## Utledning av Barne-Nøkkelpar
<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>

Utledningen av barne-nøkkelpar i Bitcoin HD-lommebøker er avhengig av en hierarkisk struktur som tillater generering av et stort antall nøkler, samtidig som disse parene organiseres i forskjellige grupper gjennom grener. Hvert barne-par som er utledet fra et foreldrepar, kan brukes direkte i et *scriptPubKey* for å låse bitcoins, eller som et utgangspunkt for å generere flere barne-nøkler, og så videre, for å skape et tre av nøkler.

Alle disse utledningene starter med hovednøkkelen og hovedkjedekoden, som er de første foreldrene på dybdenivå 0. De er, på en måte, Adam og Eva til nøklene i lommeboken din, felles forfedre til alle utledede nøkler.

![CYP201](assets/fr/048.webp)

La oss utforske hvordan denne deterministiske utledningen fungerer.

### De Forskjellige Typene av Barne-Nøkkelutledninger

Som vi kort berørte i forrige kapittel: barne-nøkler er delt inn i to hovedtyper:
1. **Normale barne-nøkler** ($k_{\text{CHD}}^n, K_{\text{CHD}}^n$): Disse er utledet fra den utvidede offentlige nøkkelen ($K_{\text{PAR}}$), eller den utvidede private nøkkelen ($k_{\text{PAR}}$), ved først å utlede den offentlige nøkkelen.
2. **Hardnede barne-nøkler** ($k_{\text{CHD}}^h, K_{\text{CHD}}^h$): Disse kan kun utledes fra den utvidede private nøkkelen ($k_{\text{PAR}}$) og er derfor usynlige for observatører som kun har den utvidede offentlige nøkkelen.
Hvert barnenøkkelpar er identifisert av en 32-biters **indeks** (kalt $i$ i våre beregninger). Indeksene for normale nøkler varierer fra $0$ til $2^{31}-1$, mens de for herdede nøkler varierer fra $2^{31}$ til $2^{32}-1$. Disse tallene brukes til å skille søsken nøkkelpar under derivasjon. Faktisk må hvert foreldrenøkkelpar være i stand til å derivere flere barnenøkkelpar. Hvis vi skulle anvende den samme beregningen systematisk fra foreldrenøklene, ville alle de oppnådde søskennøklene være identiske, noe som ikke er ønskelig. Indeksen introduserer dermed en variabel som endrer derivasjonsberegningen, slik at hvert søskenpar kan differensieres. Bortsett fra spesifikk bruk i visse protokoller og derivasjonsstandarder, starter vi generelt med å derivere det første barnenøkkelen med indeksen `0`, den andre med indeksen `1`, og så videre.
### Derivasjonsprosess med HMAC-SHA512

Derivasjonen av hver barnenøkkel er basert på HMAC-SHA512-funksjonen, som vi diskuterte i Seksjon 2 om hash-funksjoner. Den tar to inndata: foreldrenes kjedekode $C_{\text{PAR}}$ og sammenkjedningen av foreldrenøkkelen (enten den offentlige nøkkelen $K_{\text{PAR}}$ eller den private nøkkelen $k_{\text{PAR}}$, avhengig av hvilken type barnenøkkel som ønskes) og indeksen. Utdataen fra HMAC-SHA512 er en 512-bits sekvens, delt inn i to deler:
- **De første 32 bytene** (eller $h_1$) brukes til å beregne det nye barneparet.
- **De siste 32 bytene** (eller $h_2$) fungerer som den nye kjedekoden $C_{\text{CHD}}$ for barneparet.

I alle våre beregninger vil jeg betegne $\text{hash}$ utdataen fra HMAC-SHA512-funksjonen.

![CYP201](assets/fr/049.webp)

#### Derivasjon av en Barn Privat Nøkkel fra en Forelder Privat Nøkkel

For å derivere en barn privat nøkkel $k_{\text{CHD}}$ fra en forelder privat nøkkel $k_{\text{PAR}}$, er to scenarioer mulige avhengig av om en herdet eller normal nøkkel er ønsket.

For en **normal barnenøkkel** ($i < 2^{31}$), er beregningen av $\text{hash}$ som følger:


$$

\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, G \cdot k_{\text{PAR}} \Vert i)

$$
I denne beregningen observerer vi at vår HMAC-funksjon tar to inndata: først, foreldrenes kjedekode, og deretter sammenkjedningen av indeksen med den offentlige nøkkelen assosiert med den private foreldrenøkkelen. Den offentlige foreldrenøkkelen brukes her fordi vi ser etter å derivere en normal barnenøkkel, ikke en herdet en.
Vi har nå en 64-byte $\text{hash}$ som vi vil dele inn i 2 deler på 32 byte hver: $h_1$ og $h_2$:


$$

\text{hash} = h_1 \Vert h_2

$$


$$

h*1 = \text{hash}_{[:32]} \quad, \quad h*2 = \text{hash}_{[32:]}

$$

Den barn private nøkkelen $k_{\text{CHD}}^n$ beregnes deretter som følger:


$$

k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n

$$
I denne beregningen består operasjonen $\text{parse256}(h_1)$ av å tolke de første 32 bytene av $\text{hash}$ som et 256-bits heltall. Dette tallet legges deretter til den overordnede private nøkkelen, alt tatt modulo $n$ for å holde seg innenfor elliptisk kurves orden, som vi så i seksjon 3 om digitale signaturer. Dermed, for å utlede en normal barnenøkkel, selv om den overordnede offentlige nøkkelen brukes som grunnlag for beregning i inndataene til HMAC-SHA512-funksjonen, er det alltid nødvendig å ha den overordnede private nøkkelen for å fullføre beregningen.
Fra denne barnenøkkelen er det mulig å utlede den tilsvarende offentlige nøkkelen ved å anvende ECDSA eller Schnorr. På denne måten får vi et komplett nøkkelpar.

Deretter tolkes den andre delen av $\text{hash}$ rett og slett som kjedekoden for nøkkelparet til barnet som vi nettopp har utledet:


$$

C\_{\text{CHD}} = h_2

$$

Her er en skjematisk representasjon av den totale derivasjonen:

![CYP201](assets/fr/050.webp)

For en **hardened barnenøkkel** ($i \geq 2^{31}$), er beregningen av $\text{hash}$ som følger:


$$

hash = \text{HMAC-SHA512}(C_{\text{PAR}}, 0x00 \Vert k_{\text{PAR}} \Vert i)

$$

I denne beregningen observerer vi at vår HMAC-funksjon tar to inndata: først, den overordnede kjedekoden, og deretter sammenkjedningen av indeksen med den overordnede private nøkkelen. Den overordnede private nøkkelen brukes her fordi vi ser etter å utlede en hardened barnenøkkel. I tillegg legges en byte lik `0x00` til i begynnelsen av nøkkelen. Denne operasjonen jevner ut lengden for å matche den til en komprimert offentlig nøkkel.
Så, nå har vi en 64-byte $\text{hash}$ som vi vil dele inn i 2 deler på 32 byte hver: $h_1$ og $h_2$:
$$

\text{hash} = h_1 \Vert h_2

$$


$$

h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]

$$

Barnets private nøkkel $k_{\text{CHD}}^h$ beregnes deretter som følger:


$$

k_{\text{CHD}}^h = \text{parse256}(h_1) + k_{\text{PAR}} \mod n

$$

Deretter tolker vi rett og slett den andre delen av $\text{hash}$ som kjedekoden for nøkkelparet til barnet som vi nettopp har utledet:


$$

C\_{\text{CHD}} = h_2

$$

Her er en skjematisk representasjon av den totale derivasjonen:

![CYP201](assets/fr/051.webp)

Vi kan se at normal derivasjon og hardened derivasjon fungerer på samme måte, med denne forskjellen: normal derivasjon bruker den overordnede offentlige nøkkelen som inndata til HMAC-funksjonen, mens hardened derivasjon bruker den overordnede private nøkkelen.

#### Utlede en barn offentlig nøkkel fra en overordnet offentlig nøkkel
Hvis vi kun kjenner den offentlige nøkkelen til forelderen $K_{\text{PAR}}$ og den tilknyttede kjedekoden $C_{\text{PAR}}$, det vil si en utvidet offentlig nøkkel, er det mulig å utlede offentlige nøkler til barn $K_{\text{CHD}}^n$, men kun for normale (ikke-forsterkede) barnenøkler. Dette prinsippet gjør det spesielt mulig å overvåke bevegelsene til en konto i en Bitcoin-lommebok fra `xpub` (*kun-visning*).
For å utføre denne beregningen, vil vi beregne $\text{hash}$ med et indeks $i < 2^{31}$ (normal utledning):


$$

\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, K_{\text{PAR}} \Vert i)

$$

I denne beregningen observerer vi at vår HMAC-funksjon tar to innganger: først kjedekoden til forelderen, deretter sammenkjedningen av indeksen med den offentlige nøkkelen til forelderen.

Så, nå har vi en $hash$ på 64 bytes som vi vil dele inn i 2 deler på 32 bytes hver: $h_1$ og $h_2$:


$$

\text{hash} = h_1 \Vert h_2

$$


$$

h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]

$$

Den offentlige nøkkelen til barnet $K_{\text{CHD}}^n$ beregnes deretter som følger:


$$

K_{\text{CHD}}^n = G \cdot \text{parse256}(h_1) + K_{\text{PAR}}

$$
Hvis $\text{parse256}(h_1) \geq n$ (ordenen til den elliptiske kurven) eller hvis $K_{\text{CHD}}^n$ er punktet i uendelighet, er utledningen ugyldig, og et annet indeks må velges.
I denne beregningen innebærer operasjonen $\text{parse256}(h_1)$ å tolke de første 32 bytes av $\text{hash}$ som et 256-bits heltall. Dette tallet brukes til å beregne et punkt på den elliptiske kurven gjennom addisjon og dobling fra generatorenpunktet $G$. Dette punktet legges deretter til den offentlige nøkkelen til forelderen for å oppnå den normale offentlige nøkkelen til barnet. Således, for å utlede en normal offentlig nøkkel til barnet, er kun den offentlige nøkkelen til forelderen og kjedekoden til forelderen nødvendig; den private nøkkelen til forelderen kommer aldri inn i denne prosessen, i motsetning til beregningen av den private nøkkelen til barnet vi så tidligere.

Videre er kjedekoden til barnet ganske enkelt:


$$

C\_{\text{CHD}} = h_2

$$

Her er en skjematisk representasjon av den samlede utledningen:

![CYP201](assets/fr/052.webp)

### Korrespondanse mellom offentlige og private nøkler for barn

Et spørsmål som kan oppstå er hvordan en normal offentlig nøkkel til barnet utledet fra den offentlige nøkkelen til forelderen kan korrespondere til en normal privat nøkkel til barnet utledet fra den tilsvarende private nøkkelen til forelderen. Denne koblingen sikres nettopp av egenskapene til elliptiske kurver. Faktisk, for å utlede en normal offentlig nøkkel til barnet, blir HMAC-SHA512 anvendt på samme måte, men utdataen brukes forskjellig:
   - **Normal privat nøkkel til barnet**: $k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n$
   - **Normal offentlig nøkkel til barnet**: $K_{\text{CHD}}^n = G \cdot \text{parse256}(h_1) + K_{\text{PAR}}$
Takket være addisjons- og doblingsoperasjonene på den elliptiske kurven, produserer begge metodene konsistente resultater: den offentlige nøkkelen som er avledet fra den private barne-nøkkelen er identisk med den offentlige barne-nøkkelen som er direkte avledet fra den offentlige foreldre-nøkkelen.
### Sammendrag av avledningstyper

For å oppsummere, her er de forskjellige mulige typene av avledninger:

$$
\begin{array}{|c|c|c|c|}
\hline
\rightarrow & \text{PAR} & \text{CHD} & \text{n/h} \\
\hline
k_{\text{PAR}} \rightarrow k_{\text{CHD}} & k_{\text{PAR}} & \{ k_{\text{CHD}}^n, k_{\text{CHD}}^h \} & \{ n, h \} \\
k_{\text{PAR}} \rightarrow K_{\text{CHD}} & k_{\text{PAR}} & \{ K_{\text{CHD}}^n, K_{\text{CHD}}^h \} & \{ n, h \} \\
K_{\text{PAR}} \rightarrow k_{\text{CHD}} & K_{\text{PAR}} & \times & \times \\
K_{\text{PAR}} \rightarrow K_{\text{CHD}} & K_{\text{PAR}} & K_{\text{CHD}}^n & n \\
\hline
\end{array}
$$

For å oppsummere, så langt har du lært å skape de grunnleggende elementene av HD-lommeboken: den mnemoniske frasen, frøet, og deretter hovednøkkelen og hovedkjedekoden. Du har også oppdaget hvordan man avleder barne-nøkkelpar i dette kapittelet. I neste kapittel vil vi utforske hvordan disse avledningene er organisert i Bitcoin-lommebøker og hvilken struktur man skal følge for å konkret oppnå mottaksadressene samt nøkkelparene som brukes i *scriptPubKey* og *scriptSig*.

## Lommebokstruktur og Avledningsveier
<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>

Den hierarkiske strukturen av HD-lommebøker på Bitcoin tillater organiseringen av nøkkelpar på forskjellige måter. Ideen er å avlede, fra hovedprivatnøkkelen og hovedkjedekoden, flere nivåer av dybde. Hvert lagt til nivå tilsvarer avledningen av et barne-nøkkelpar fra et foreldre-nøkkelpar.

Over tid har forskjellige BIP-er introdusert standarder for disse avledningsveiene, med mål om å standardisere bruken på tvers av forskjellig programvare. Så, i dette kapittelet vil vi oppdage betydningen av hvert nivå av avledning i HD-lommebøker, i henhold til disse standardene.

### Dybden av Avledning i en HD-Lommebok

Avledningsveier er organisert i lag av dybde, som strekker seg fra dybde 0, som representerer hovednøkkelen og hovedkjedekoden, til lag av undernivåer for å avlede adresser brukt til å låse UTXO-er. BIP-ene (*Bitcoin Improvement Proposals*) definerer standardene for hvert lag, som bidrar til å harmonisere praksiser på tvers av forskjellig lommebokforvaltningsprogramvare.

En avledningsvei refererer derfor til sekvensen av indekser brukt for å avlede barne-nøkler fra en hovednøkkel.

**Dybde 0: Hovednøkkel (BIP32)**

Denne dybden tilsvarer lommebokens hovedprivate nøkkel og hovedkjedekode. Den er representert ved notasjonen $m/$.

**Dybde 1: Formål (BIP43)**
Målet bestemmer den logiske strukturen av derivasjonen. For eksempel vil en P2WPKH-adresse ha $/84'/$ på dybde 1 (i henhold til BIP84), mens en P2TR-adresse vil ha $/86'/$ (i henhold til BIP86). Dette laget letter kompatibilitet mellom lommebøker ved å indikere indeksnumre som tilsvarer BIP-numrene.
Med andre ord, når du har hovednøkkelen og hovedkjedekoden, fungerer disse som et foreldrenøkkelpar for å derivere et barnenøkkelpar. Indeksen som brukes i denne derivasjonen kan for eksempel være $/84'/$ hvis lommeboken er ment å bruke SegWit v0-type skript. Dette nøkkelparet er da på dybde 1. Dets rolle er ikke å låse bitcoins, men rett og slett å tjene som et veipunkt i derivasjonshierarkiet.

**Dybde 2: Valutatype (BIP44)**

Fra nøkkelparet på dybde 1 utføres en ny derivasjon for å oppnå nøkkelparet på dybde 2. Denne dybden tillater differensiering av Bitcoin-kontoer fra andre kryptovalutaer innenfor samme lommebok.

Hver valuta har et unikt indeks for å sikre kompatibilitet på tvers av flervaluta-lommebøker. For eksempel, for Bitcoin, er indeksen $/0'/$ (eller `0x80000000` i heksadesimal notasjon). Valutaindekser velges i området fra $2^{31}$ til $2^{32}-1$ for å sikre hardnet derivasjon.

For å gi deg andre eksempler, her er indeksene til noen valutaer:
- $1'$ (`0x80000001`) for testnet bitcoins;
- $2'$ (`0x80000002`) for Litecoin;
- $60'$ (`0x8000003c`) for Ethereum...

**Dybde 3: Konto (BIP32)**

Hver lommebok kan deles inn i flere kontoer, nummerert fra $2^{31}$, og representert på dybde 3 av $/0'/$ for den første kontoen, $/1'/$ for den andre, og så videre. Generelt, når man refererer til en utvidet nøkkel `xpub`, refererer det til nøkler på denne derivasjonsdybden.

Denne separasjonen i forskjellige kontoer er valgfri. Den har som mål å forenkle organiseringen av lommeboken for brukerne. I praksis brukes ofte bare én konto, vanligvis den første som standard. Imidlertid, i noen tilfeller, hvis man ønsker å tydelig skille nøkkelpar for forskjellige bruksområder, kan dette være nyttig. For eksempel er det mulig å opprette en personlig konto og en profesjonell konto fra samme frø, med helt distinkte grupper av nøkler fra denne derivasjonsdybden.
**Dybde 4: Kjede (BIP32)**
Hver konto definert på dybde 3 er deretter strukturert inn i to kjeder:
- **Den eksterne kjeden**: I denne kjeden, det som er kjent som "offentlige" adresser, er derivert. Disse mottaksadressene er ment å låse UTXOer som kommer fra eksterne transaksjoner (det vil si, som stammer fra forbruket av UTXOer som ikke tilhører deg). Enkelt sagt, denne eksterne kjeden brukes når man ønsker å motta bitcoins. Når du klikker på "*motta*" i lommebokprogramvaren din, er det alltid en adresse fra den eksterne kjeden som tilbys deg. Denne kjeden representeres av et par nøkler derivert med indeksen $/0/$.
- **Den interne kjeden (veksel)**: Denne kjeden er reservert for mottaksadresser som låser bitcoins som kommer fra forbruket av UTXOer som tilhører deg, med andre ord, vekseladresser. Den er identifisert ved indeksen $/1/$.

**Dybde 5: Adresseindeks (BIP32)**
Til slutt representerer dybde 5 det siste trinnet i derivasjonen i lommeboken. Selv om det teknisk sett er mulig å fortsette på ubestemt tid, stopper nåværende standarder her. På denne siste dybden blir parene av nøkler som faktisk vil bli brukt til å låse og låse opp UTXOene, avledet. Hvert indeks gjør det mulig å skille mellom søsken nøkkelpar: dermed vil den første mottaksadressen bruke indeksen $/0/$, den andre indeksen $/1/$, og så videre.
![CYP201](assets/fr/053.webp)

### Notasjon av Derivasjonsveier

Derivasjonsveien er skrevet ved å skille hvert nivå med en skråstrek ($/$). Hver skråstrek indikerer dermed en derivasjon av et foreldre nøkkelpar ($k_{\text{PAR}}$, $K_{\text{PAR}}$, $C_{\text{PAR}}$) til et barn nøkkelpar ($k_{\text{CHD}}$, $K_{\text{CHD}}$, $C_{\text{CHD}}$). Nummeret notert ved hver dybde tilsvarer indeksen som brukes til å avlede denne nøkkelen fra foreldrene. Apostrofen ($'$) som noen ganger er plassert til høyre for indeksen, indikerer en herdet derivasjon ($k_{\text{CHD}}^h$, $K_{\text{CHD}}^h$). Noen ganger erstattes denne apostrofen med et $h$. I fravær av en apostrof eller $h$, er det derfor en normal derivasjon ($k_{\text{CHD}}^n$, $K_{\text{CHD}}^n$).
Som vi har sett i de foregående kapitlene, starter herdede nøkkelindekser fra $2^{31}$, eller `0x80000000` i heksadesimalt. Derfor, når en indeks følges av en apostrof i en derivasjonsvei, må $2^{31}$ legges til det angitte nummeret for å oppnå den faktiske verdien som brukes i HMAC-SHA512-funksjonen. For eksempel, hvis derivasjonsveien spesifiserer $/44'/$, vil den faktiske indeksen være:
$$

i = 44 + 2^{31} = 2\,147\,483\,692

$$

I heksadesimalt er dette `0x8000002C`.

Nå som vi har forstått hovedprinsippene for derivasjonsveier, la oss ta et eksempel! Her er derivasjonsveien for en Bitcoin mottaksadresse:


$$

m / 84' / 0' / 1' / 0 / 7

$$

I dette eksemplet:
- $84'$ indikerer P2WPKH (SegWit v0) standarden;
- $0'$ indikerer Bitcoin-valutaen på hovednettet;
- $1'$ tilsvarer den andre kontoen i lommeboken;
- $0$ indikerer at adressen er på den eksterne kjeden;
- $7$ indikerer den 8. eksterne adressen til denne kontoen.

### Sammendrag av derivasjonsstrukturen

| Dybde | Beskrivelse        | Standard Eksempel                  |
| ----- | ------------------ | --------------------------------- |
| 0     | Hovednøkkel        | $m/$                              |
| 1     | Formål             | $/86'/$ (P2TR)                    |
| 2     | Valuta             | $/0'/$ (Bitcoin)                  |
| 3     | Konto              | $/0'/$ (Første konto)             |
| 4     | Kjede              | $/0/$ (ekstern) eller $/1/$ (endring)|
| 5     | Adresseindeks      | $/0/$ (første adresse)            |
I neste kapittel skal vi oppdage hva "*output script descriptors*" er, en nylig introdusert innovasjon i Bitcoin Core som forenkler sikkerhetskopieringen av en Bitcoin-lommebok.
## Output script descriptors
<chapterId>e4f1c2d3-9b8a-4d3e-8f2a-7b6c5d4e3f2a</chapterId>
Du får ofte høre at den mnemoniske frasen alene er tilstrekkelig for å gjenopprette tilgang til en lommebok. I virkeligheten er ting litt mer komplekse. I forrige kapittel så vi på avledningsstrukturen til HD-lommeboken, og du kan ha lagt merke til at denne prosessen er ganske kompleks. Avledningsveier forteller programvaren hvilken retning den skal følge for å avlede brukerens nøkler. Men, når man gjenoppretter en Bitcoin-lommebok, hvis man ikke kjenner disse veiene, er den mnemoniske frasen alene ikke nok. Den tillater å oppnå hovednøkkelen og hovedkjedekoden, men det er da nødvendig å kjenne indeksene som ble brukt for å nå barnenøklene.

Teoretisk sett ville det være nødvendig å lagre ikke bare den mnemoniske frasen til vår lommebok, men også veiene til kontoene vi bruker. I praksis er det ofte mulig å gjenopprette tilgang til barnenøklene uten denne informasjonen, forutsatt at standardene har blitt fulgt. Ved å teste hver standard en etter en, er det generelt mulig å gjenopprette tilgang til bitcoinene. Men, dette er ikke garantert og det er spesielt komplisert for nybegynnere. Også, med diversifiseringen av skripttyper og fremveksten av mer komplekse konfigurasjoner, kunne denne informasjonen bli vanskelig å ekstrapolere, og dermed gjøre denne dataen til privat informasjon og vanskelig å gjenopprette ved brute force. Dette er grunnen til at en innovasjon nylig har blitt introdusert og begynner å bli integrert i din favoritt lommebokprogramvare: *output script descriptors*.

### Hva er en "descriptor"?

"*Output script descriptors*", eller enkelt "*descriptors*", er strukturerte uttrykk som fullstendig beskriver et utgangsskript (*scriptPubKey*) og gir all nødvendig informasjon for å følge transaksjonene assosiert med et bestemt skript. De letter håndteringen av nøkler i HD-lommebøker ved å tilby en standardisert og komplett beskrivelse av lommebokstrukturen og typene adresser som brukes.

Hovedfordelen med descriptors ligger i deres evne til å innkapsle all den essensielle informasjonen for å gjenopprette en lommebok i en enkelt streng (i tillegg til gjenopprettingsfrasen). Ved å lagre en descriptor med de tilknyttede mnemoniske frasene, blir det mulig å gjenopprette de private nøklene ved å vite nøyaktig deres posisjon i hierarkiet. For multisig-lommebøker, hvis sikkerhetskopi opprinnelig var mer kompleks, inkluderer descriptor `xpub` for hver faktor, og sikrer dermed muligheten for å regenerere adressene i tilfelle et problem.

### Konstruksjon av en descriptor

En descriptor består av flere elementer:
* Skriptfunksjoner som `pk` (*Pay-to-PubKey*), `pkh` (*Pay-to-PubKey-Hash*), `wpkh` (*Pay-to-Witness-PubKey-Hash*), `sh` (*Pay-to-Script-Hash*), `wsh` (*Pay-to-Witness-Script-Hash*), `tr` (*Pay-to-Taproot*), `multi` (*Multisignatur*), og `sortedmulti` (*Multisignatur med sorterte nøkler*);
* Avledningsveier, for eksempel `[d34db33f/44h/0h/0h]` som indikerer en avledet kontovei og et spesifikt hovednøkkelfingeravtrykk;
* Nøkler i ulike formater som heksadesimale offentlige nøkler eller utvidede offentlige nøkler (`xpub`);
* En sjekksum, forutgått av et hash-tegn, for å verifisere integriteten til descriptor.
For eksempel kan en beskrivelse for en P2WPKH (SegWit v0) lommebok se slik ut:
```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7nr4
```

I denne beskrivelsen indikerer avledningsfunksjonen `wpkh` en skripttype *Pay-to-Witness-Public-Key-Hash*. Den følges av avledningsstien som inneholder:
* `cdeab12f`: fingeravtrykket til hovednøkkelen;
* `84h`: som betegner bruk av et BIP84 formål, ment for SegWit v0 adresser;
* `0h`: som indikerer at det er en BTC valuta på hovednettet;
* `0h`: som refererer til det spesifikke kontonummeret brukt i lommeboken.

Beskrivelsen inkluderer også den utvidede offentlige nøkkelen brukt i denne lommeboken:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Deretter spesifiserer notasjonen `/<0;1>/*` at beskrivelsen kan generere adresser fra den eksterne kjeden (`0`) og den interne kjeden (`1`), med et jokertegn (`*`) som tillater sekvensiell avledning av flere adresser på en konfigurerbar måte, lik håndtering av en "gap-grense" på tradisjonell lommebokprogramvare.
Til slutt representerer `#jy0l7nr4` sjekksummen for å verifisere integriteten til beskrivelsen.
Du vet nå alt om driften av HD-lommeboken på Bitcoin og prosessen med å avlede nøkkelpar. Imidlertid begrenset vi oss i de siste kapitlene til generering av private og offentlige nøkler, uten å adressere konstruksjonen av mottaksadresser. Dette vil nettopp være temaet for neste kapittel!

## Mottaksadresser
<chapterId>ca80a89d-f8da-4e09-8c35-43179b65bced</chapterId>

Mottaksadresser er informasjonsbiter innebygd i *scriptPubKey* for å låse nylig opprettede UTXOer. Enkelt sagt tjener en adresse til å motta bitcoins. La oss utforske deres funksjon i forbindelse med det vi har studert i de foregående kapitlene.

### Rollen til Bitcoin-adresser i Skript

Som forklart tidligere, er en transaksjons rolle å overføre eierskapet av bitcoins fra innganger til utganger. Denne prosessen involverer å forbruke UTXOer som innganger mens man skaper nye UTXOer som utganger. Disse UTXOene sikres av skript, som definerer de nødvendige betingelsene for å låse opp midlene.
Når en bruker mottar bitcoins, oppretter avsenderen en utdata UTXO og låser den med en *scriptPubKey*. Dette skriptet inneholder reglene som vanligvis spesifiserer signaturene og offentlige nøkler som kreves for å låse opp denne UTXOen. For å bruke denne UTXOen i en ny transaksjon, må brukeren gi den etterspurte informasjonen via en *scriptSig*. Utførelsen av *scriptSig* i kombinasjon med *scriptPubKey* må returnere "true" eller `1`. Hvis denne betingelsen er oppfylt, kan UTXOen brukes til å skape en ny UTXO, som selv er låst av en ny *scriptPubKey*, og så videre.
![CYP201](assets/fr/054.webp)

Det er nettopp i *scriptPubKey* at mottaksadressene finnes. Imidlertid varierer bruken av dem avhengig av hvilken skriptstandard som er vedtatt. Her er en oppsummeringstabell over informasjonen som er inneholdt i *scriptPubKey* i henhold til standarden som brukes, samt informasjonen som forventes i *scriptSig* for å låse opp *scriptPubKey*.

| Standard           | *scriptPubKey*                                              | *scriptSig*                     | *innløsningsskript* | *vitne*                                  |
| ------------------ | ----------------------------------------------------------- | ------------------------------- | ------------------- | ---------------------------------------- |
| P2PK               | `<pubkey> OP_CHECKSIG`                                      | `<signatur>`                    |                     |                                          |
| P2PKH              | `OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG` | `<signatur> <offentlig nøkkel>` |                     |                                          |
| P2SH               | `OP_HASH160 <scriptHash> OP_EQUAL`                          | `<data pushes> <innløsningsskript>` | Vilkaarlig data |                                          |
| P2WPKH             | `0 <pubKeyHash>`                                            |                                 |                     | `<signatur> <offentlig nøkkel>`          |
| P2WSH              | `0 <witnessScriptHash>`                                     |                                 |                     | `<data pushes> <vitneskript>`            |
| P2SH-P2WPKH        | `OP_HASH160 <innløsningsskriptHash> OP_EQUAL`               | `<innløsningsskript>`           | `0 <pubKeyHash>`    | `<signatur> <offentlig nøkkel>`          |
| P2SH-P2WSH         | `OP_HASH160 <innløsningsskriptHash> OP_EQUAL`               | `<innløsningsskript>`           | `0 <scriptHash>`    | `<data pushes> <vitneskript>`            |
| P2TR (nøkkelbane)  | `1 <offentlig nøkkel>`                                      |                                 |                     | `<signatur>`                             |
| P2TR (skriptbane)  | `1 <offentlig nøkkel>`                                      |                                 |                     | `<data pushes> <skript> <kontrollblokk>` |

*Kilde: Bitcoin Core PR review club, 7. juli 2021 - Gloria Zhao*

Opcodes brukt i et skript er designet for å manipulere informasjon, og om nødvendig, sammenligne eller teste den. La oss ta eksempelet med et P2PKH-skript, som er som følger:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

Som vi vil se i dette kapittelet, representerer `<pubKeyHash>` faktisk nyttelasten til mottaksadressen som brukes til å låse UTXOen. For å låse opp denne *scriptPubKey*, er det nødvendig å gi en *scriptSig* som inneholder:

```text
<signatur> <offentlig nøkkel>
```
I skriptspråk er "stacken" en "*LIFO*" ("*Last In, First Out*") datastruktur som brukes til å midlertidig lagre elementer under utførelsen av skriptet. Hver skriptoperasjon manipulerer denne stacken, hvor elementer kan legges til (*push*) eller fjernes (*pop*). Skript bruker disse stackene til å evaluere uttrykk, lagre midlertidige variabler og håndtere betingelser.
Utførelsen av skriptet jeg nettopp ga som et eksempel følger denne prosessen:

- Vi har *scriptSig*, *ScriptPubKey*, og stacken:

![CYP201](assets/fr/055.webp)

- *scriptSig* blir pushet på stacken:

![CYP201](assets/fr/056.webp)

- `OP_DUP` dupliserer den offentlige nøkkelen som er oppgitt i *scriptSig* på stacken:

![CYP201](assets/fr/057.webp)

- `OP_HASH160` returnerer hashen av den offentlige nøkkelen som nettopp ble duplisert:

![CYP201](assets/fr/058.webp)

- `OP_PUSHBYTES_20 <pubKeyHash>` pusher Bitcoin-adressen som er inneholdt i *scriptPubKey* på stacken:

![CYP201](assets/fr/059.webp)

- `OP_EQUALVERIFY` verifiserer at den hashede offentlige nøkkelen matcher den oppgitte mottaksadressen:

![CYP201](assets/fr/060.webp)
`OP_CHECKSIG` sjekker signaturen som er inneholdt i *scriptSig* ved hjelp av den offentlige nøkkelen. Denne opcode utfører i hovedsak en signaturverifisering som vi beskrev i del 3 av denne opplæringen:
![CYP201](assets/fr/061.webp)

- Hvis `1` forblir på stacken, da er skriptet gyldig:

![CYP201](assets/fr/062.webp)

Derfor, for å oppsummere, dette skriptet tillater å verifisere, med hjelp av den digitale signaturen, at brukeren som hevder eierskap til denne UTXO og ønsker å bruke den, faktisk besitter den private nøkkelen assosiert med mottaksadressen som ble brukt under opprettelsen av denne UTXO.

### De forskjellige typene Bitcoin-adresser

Gjennom utviklingen av Bitcoin, har flere standard skriptmodeller blitt lagt til. Hver av dem bruker en distinkt type mottaksadresse. Her er en oversikt over de viktigste skriptmodellene som er tilgjengelige til dags dato:

**P2PK (*Pay-to-PubKey*)**:

Denne skriptmodellen ble introdusert i den første versjonen av Bitcoin av Satoshi Nakamoto. P2PK-skriptet låser bitcoins direkte ved å bruke en rå offentlig nøkkel (dermed brukes ingen mottaksadresse med denne modellen). Dens struktur er enkel: den inneholder en offentlig nøkkel og krever en tilsvarende digital signatur for å låse opp midlene. Dette skriptet er en del av "*Legacy*" standarden.

**P2PKH (*Pay-to-PubKey-Hash*)**:

Lik P2PK, ble P2PKH-skriptet introdusert ved lanseringen av Bitcoin. I motsetning til sin forgjenger, låser det bitcoins ved å bruke hashen av den offentlige nøkkelen, i stedet for å direkte bruke den rå offentlige nøkkelen. *scriptSig* må deretter oppgi den offentlige nøkkelen assosiert med mottaksadressen, samt en gyldig signatur. Adressene som tilsvarer denne modellen starter med `1` og er kodet i *base58check*. Dette skriptet tilhører også "*Legacy*" standarden.

**P2SH (*Pay-to-Script-Hash*)**:
Introdusert i 2012 med BIP16, tillater P2SH-modellen bruk av hashen til et vilkårlig skript i *scriptPubKey*. Dette hashede skriptet, kalt "*redeemScript*", inneholder betingelsene for å låse opp midlene. For å bruke en UTXO låst med P2SH, er det nødvendig å gi en *scriptSig* som inneholder det originale *redeemScript* samt nødvendige data for å validere det. Denne modellen brukes spesielt for gamle multisigs. Adressene assosiert med P2SH starter med `3` og er kodet i *base58check*. Dette skriptet tilhører også "*Legacy*" standarden.
**P2WPKH (*Pay-to-Witness-PubKey-Hash*)**:
Dette skriptet er likt P2PKH, da det også låser bitcoins ved å bruke hashen av en offentlig nøkkel. Imidlertid, i motsetning til P2PKH, flyttes *scriptSig* til en separat seksjon kalt "*Witness*". Dette refereres noen ganger til som "*scriptWitness*" for å betegne settet som består av signaturen og den offentlige nøkkelen. Hver SegWit-inngang har sin egen *scriptWitness*, og samlingen av *scriptWitnesses* utgjør *Witness*-feltet i transaksjonen. Denne flyttingen av signaturdata er en innovasjon introdusert av SegWit-oppdateringen, rettet spesielt mot å forhindre malleabilitet av transaksjoner på grunn av ECDSA-signaturer.
P2WPKH-adresser bruker *bech32*-koding og starter alltid med `bc1q`. Denne typen skript tilsvarer versjon 0 SegWit-utganger.

**P2WSH (*Pay-to-Witness-Script-Hash*)**:

P2WSH-modellen ble også introdusert med SegWit-oppdateringen i august 2017. Likt P2SH-modellen, låser den bitcoins ved å bruke hashen av et skript. Hovedforskjellen ligger i hvordan signaturer og skript er inkorporert i transaksjonen. For å bruke bitcoins låst med denne typen skript, må mottakeren gi det originale skriptet, kalt *witnessScript* (tilsvarende *redeemScript* i P2SH), sammen med nødvendige data for å validere dette *witnessScript*. Denne mekanismen tillater implementering av mer komplekse utgiftsbetingelser, som multisigs.

P2WSH-adresser bruker *bech32*-koding og starter alltid med `bc1q`. Dette skriptet tilsvarer også versjon 0 SegWit-utganger.

**P2TR (*Pay-to-Taproot*)**:

P2TR-modellen ble introdusert med implementeringen av Taproot i november 2021. Den er basert på Schnorr-protokollen for kryptografisk nøkkelaggregering, samt på et Merkel-tre for alternative skript, kalt MAST (*Merkelized Alternative Script Tree*). I motsetning til andre typer skript, hvor utgiftsbetingelser er offentlig eksponert (enten ved mottak eller ved bruk), tillater P2TR skjuling av komplekse skript bak en enkelt, tilsynelatende offentlig nøkkel.

Teknisk sett låser et P2TR-skript bitcoins på en unik Schnorr offentlig nøkkel, betegnet som $Q$. Denne nøkkelen $Q$ er faktisk en aggregering av en offentlig nøkkel $P$ og en offentlig nøkkel $M$, sistnevnte beregnet fra Merkel-roten av en liste over *scriptPubKey*. Bitcoins låst med denne typen skript kan brukes på to måter:
- Ved å publisere en signatur for den offentlige nøkkelen $P$ (*nøkkelsti*).
- Ved å tilfredsstille ett av skriptene inneholdt i Merkel-treet (*skriptsti*).
P2TR tilbyr dermed stor fleksibilitet, ettersom det tillater å låse bitcoins enten med en unik offentlig nøkkel, med flere valgte skript, eller begge deler samtidig. Fordelen med denne Merkle-trestrukturen er at kun det brukte utgiftsskriptet avsløres under transaksjonen, men alle andre alternative skript forblir hemmelige. ![CYP201](assets/fr/063.webp)

P2TR tilsvarer versjon 1 SegWit-utdata, noe som betyr at signaturene for P2TR-inndata lagres i transaksjonens *Witness*-seksjon, og ikke i *scriptSig*. P2TR-adresser bruker *bech32m*-kodingen og starter med `bc1p`, men de er ganske unike fordi de ikke bruker en hash-funksjon for sin konstruksjon. Faktisk representerer de direkte den offentlige nøkkelen $Q$ som ganske enkelt er formatert med metadata. Det er derfor en skriptmodell nær P2PK.

Nå som vi har dekket teorien, la oss gå videre til praksis! I det følgende kapittelet foreslår jeg å utlede både en SegWit v0-adresse og en SegWit v1-adresse fra et par nøkler.

## Adresseutledning
<chapterId>3ebdc750-4135-4881-b07e-08965941b93e</chapterId>

La oss sammen utforske hvordan man genererer en mottaksadresse fra et par nøkler som befinner seg, for eksempel, på dybde 5 i en HD-lommebok. Denne adressen kan deretter brukes i en lommebokprogramvare for å låse en UTXO.

Siden prosessen med å generere en adresse avhenger av skriptmodellen som er vedtatt, la oss fokusere på to spesifikke tilfeller: generering av en SegWit v0-adresse i P2WPKH og en SegWit v1-adresse i P2TR. Disse to typene adresser dekker i dag flertallet av bruksområdene.

### Komprimering av offentlig nøkkel

Etter å ha utført alle derivasjonstrinnene fra hovednøkkelen til dybde 5 ved hjelp av de passende indeksene, får vi et par nøkler ($k$, $K$) med $K = k \cdot G$. Selv om det er mulig å bruke denne offentlige nøkkelen som den er for å låse midler med P2PK-standarden, er ikke det vårt mål her. I stedet er målet å skape en adresse i P2WPKH i første omgang, og deretter i P2TR for et annet eksempel.

Det første trinnet er å komprimere den offentlige nøkkelen $K$. For å forstå denne prosessen godt, la oss først minne om noen grunnleggende prinsipper dekket i del 3.
En offentlig nøkkel på Bitcoin er et punkt $K$ som ligger på en elliptisk kurve. Den representeres i formen $(x, y)$, hvor $x$ og $y$ er koordinatene til punktet. I sin ukomprimerte form måler denne offentlige nøkkelen 520 bits: 8 bits for et prefiks (innledende verdi av `0x04`), 256 bits for $x$-koordinaten, og 256 bits for $y$-koordinaten.
Imidlertid har elliptiske kurver en symmetriegenskap med hensyn til x-aksen: for en gitt $x$-koordinat, er det bare to mulige verdier for $y$: $y$ og $-y$. Disse to punktene ligger på hver sin side av x-aksen. Med andre ord, hvis vi kjenner $x$, er det tilstrekkelig å spesifisere om $y$ er partall eller oddetall for å identifisere det eksakte punktet på kurven.

![CYP201](assets/fr/064.webp)
For å komprimere en offentlig nøkkel, kodes bare $x$, som opptar 256 bits, og et prefiks legges til for å spesifisere pariteten til $y$. Denne metoden reduserer størrelsen på den offentlige nøkkelen til 264 bits i stedet for de opprinnelige 520. Prefikset `0x02` indikerer at $y$ er partall, og prefikset `0x03` indikerer at $y$ er oddetall.
La oss ta et eksempel for å forstå godt, med en rå offentlig nøkkel i ukomprimert representasjon:

```text
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Hvis vi dekomponerer denne nøkkelen, har vi:
   - Prefikset: `04`;
   - $x$: `678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6`;
   - $y$: `49f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f`

Det siste heksadesimale tegnet til $y$ er `f`. I base 10, `f = 15`, som tilsvarer et oddetall. Derfor er $y$ oddetall, og prefikset vil være `0x03` for å indikere dette.

Den komprimerte offentlige nøkkelen blir:

```text
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```
Denne operasjonen gjelder for alle skriptmodeller basert på ECDSA, det vil si alle unntatt P2TR som bruker Schnorr. I tilfellet med Schnorr, som forklart i del 3, beholder vi bare verdien av $x$, uten å legge til et prefiks for å indikere pariteten til $y$, i motsetning til ECDSA. Dette gjøres mulig ved at en unik paritet vilkårlig velges for alle nøkler. Dette tillater en liten reduksjon i lagringsplassen som kreves for offentlige nøkler.
### Derivasjon av en SegWit v0 (bech32) adresse

Nå som vi har oppnådd vår komprimerte offentlige nøkkel, kan vi derivere en SegWit v0 mottaksadresse fra den.

Det første steget er å anvende HASH160 hash-funksjonen på den komprimerte offentlige nøkkelen. HASH160 er en sammensetning av to påfølgende hash-funksjoner: SHA256, etterfulgt av RIPEMD160:


$$

\text{HASH160}(K) = \text{RIPEMD160}(\text{SHA256}(K))

$$

Først passerer vi nøkkelen gjennom SHA256:

```text
SHA256(K) = C489EBD66E4103B3C4B5EAFF462B92F5847CA2DCE0825F4997C7CF57DF35BF3A
```

Deretter passerer vi resultatet gjennom RIPEMD160:

```text
RIPEMD160(SHA256(K)) = 9F81322CC88622CA4CCB2A52A21E2888727AA535
```
Vi har oppnådd en 160-bits hash av den offentlige nøkkelen, som utgjør det som kalles nyttelasten til adressen. Denne nyttelasten representerer den sentrale og viktigste delen av adressen. Den brukes også i *scriptPubKey* for å låse UTXOene.
Men, for å gjøre denne nyttelasten lettere brukbar for mennesker, legges metadata til den. Neste steg involverer koding av denne hashen til grupper av 5 bits i desimal. Denne desimalomformingen vil være nyttig for konvertering til *bech32*, som brukes av post-SegWit-adresser. Den 160-bits binære hashen deles dermed inn i 32 grupper av 5 bits:

$$
\begin{array}{|c|c|}
\hline
\text{5 bits} & \text{Decimal} \\
\hline
10011 & 19 \\
11110 & 30 \\
00000 & 0 \\
10011 & 19 \\
00100 & 4 \\
01011 & 11 \\
00110 & 6 \\
01000 & 8 \\
10000 & 16 \\
11000 & 24 \\
10001 & 17 \\
01100 & 12 \\
10100 & 20 \\
10011 & 19 \\
00110 & 6 \\
01011 & 11 \\
00101 & 5 \\
01001 & 9 \\
01001 & 9 \\
01010 & 10 \\
00100 & 4 \\
00111 & 7 \\
10001 & 17 \\
01000 & 8 \\
10001 & 17 \\
00001 & 1 \\
11001 & 25 \\
00111 & 7 \\
10101 & 21 \\
00101 & 5 \\
00101 & 5 \\
10101 & 21 \\
\hline
\end{array}
$$
Så, vi har:

```text
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
```

Når hashen er kodet til grupper av 5 bits, legges en kontrollsum til adressen. Denne kontrollsummen brukes til å verifisere at nyttelasten til adressen ikke har blitt endret under lagring eller overføring. For eksempel, den lar en lommebokprogramvare sikre at du ikke har gjort en skrivefeil når du taster inn en mottaksadresse. Uten denne verifiseringen kunne du ved et uhell sende bitcoins til en feil adresse, noe som resulterer i et permanent tap av midler, siden du ikke eier den tilhørende offentlige eller private nøkkelen. Derfor er kontrollsummen en beskyttelse mot menneskelige feil.

For de gamle Bitcoin *Legacy*-adressene, ble kontrollsummen rett og slett beregnet fra begynnelsen av adressehashen med HASH256-funksjonen. Med introduksjonen av SegWit og *bech32*-formatet, brukes nå BCH-koder (*Bose, Ray-Chaudhuri, og Hocquenghem*). Disse feilkorrigerende kodene brukes til å oppdage og korrigere feil i datasekvenser. De sikrer at den overførte informasjonen ankommer intakt til sitt bestemmelsessted, selv i tilfelle av mindre endringer. BCH-koder brukes i mange felt, som SSDer, DVDer, og QR-koder. For eksempel, takket være disse BCH-kodene, kan en delvis skjult QR-kode fortsatt leses og dekodes.

I konteksten av Bitcoin, tilbyr BCH-koder en bedre kompromiss mellom størrelse og feildeteksjonsevne sammenlignet med de enkle hashfunksjonene som brukes for *Legacy*-adresser. Men, på Bitcoin, brukes BCH-koder kun for feildeteksjon, ikke korreksjon. Dermed vil lommebokprogramvare signalisere en feil mottaksadresse, men vil ikke automatisk korrigere den. Denne begrensningen er bevisst: å tillate automatisk korreksjon ville redusere feildeteksjonsevnen.

For å beregne kontrollsummen med BCH-koder, trenger vi å forberede flere elementer:
- **Den menneskelesbare delen (HRP)**: For Bitcoin hovednettverket er HRP `bc`;
HRP må utvides ved å dele hvert tegn inn i to deler:
- Tar tegnene fra HRP i ASCII:
	- `b`: `01100010`
- `c`: `01100011`
- Ekstraherer de 3 mest signifikante bitene og de 5 minst signifikante bitene:
  - 3 mest signifikante bitene: `011` (3 i desimal)
  - 3 mest signifikante bitene: `011` (3 i desimal)
  - 5 minst signifikante bitene: `00010` (2 i desimal)
  - 5 minst signifikante bitene: `00011` (3 i desimal)

Med skilletegnet `0` mellom de to tegnene, er derfor HRP-utvidelsen:

```text
03 03 00 02 03
```

- **Vitneversjonen**: For SegWit versjon 0, er det `00`;

- **Nyttelasten**: Desimalverdiene av den offentlige nøkkelens hash;

- **Reservasjonen for sjekksummen**: Vi legger til 6 nuller `[0, 0, 0, 0, 0, 0]` på slutten av sekvensen.

Alle dataene kombinert for å legge inn i programmet for å beregne sjekksummen er som følger:

```text
HRP = 03 03 00 02 03
SEGWIT v0 = 00
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
CHECKSUM = 00 00 00 00 00 00

INPUT = 03 03 00 02 03 00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 00 00 00 00 00 00
```

Beregningen av sjekksummen er ganske kompleks. Den involverer polynomisk endelig feltaritmetikk. Vi vil ikke detaljere denne beregningen her og vil gå direkte til resultatet. I vårt eksempel er sjekksummen oppnådd i desimal:

```text
10 16 11 04 13 18
```

Vi kan nå konstruere mottaksadressen ved å sette sammen i rekkefølge følgende elementer:
- **SegWit-versjonen**: `00`
- **Nyttelasten**: Den offentlige nøkkelens hash
- **Sjekksummen**: Verdiene oppnådd i det forrige steget (`10 16 11 04 13 18`)

Dette gir oss i desimal:

```text
00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 10 16 11 04 13 18
```

Deretter må hver desimalverdi kartlegges til sin *bech32*-karakter ved hjelp av følgende konverteringstabell:


$$
\begin{array}{|c|c|c|c|c|c|c|c|c|}
\hline
 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\hline
+0 & q & p & z & r & y & 9 & x & 8 \\
\hline
+8 & g & f & 2 & t & v & d & w & 0 \\
\hline
+16 & s & 3 & j & n & 5 & 4 & k & h \\
\hline
+24 & c & e & 6 & m & u & a & 7 & l \\
\hline
\end{array}
$$

For å konvertere en verdi til et _bech32_-tegn ved hjelp av denne tabellen, finn ganske enkelt verdiene i den første kolonnen og den første raden som, når de legges sammen, gir det ønskede resultatet. Deretter henter du det tilsvarende tegnet. For eksempel vil det desimale tallet `19` bli konvertert til bokstaven `n`, fordi $19 = 16 + 3$.
Ved å kartlegge alle våre verdier, får vi følgende adresse:

```
qn7qnytxgsc3v5nxt9ff2y83g3pe849942stydj
```

Alt som gjenstår er å legge til HRP `bc`, som indikerer at det er en adresse for Bitcoin hovednettverket, samt skilletegnet `1`, for å få den komplette mottaksadressen:

```
bc1qn7qnytxgsc3v5nxt9ff2y83g3pe849942stydj
```

Det spesielle med dette _bech32_-alfabetet er at det inkluderer alle alfanumeriske tegn unntatt `1`, `b`, `i`, og `o` for å unngå visuell forvirring mellom lignende tegn, spesielt under deres inntasting eller lesing av mennesker.

For å oppsummere, her er avledningsprosessen:

![CYP201](assets/fr/065.webp)

Dette er hvordan man avleder en P2WPKH (SegWit v0) mottaksadresse fra et par nøkler. La oss nå gå videre til P2TR (SegWit v1 / Taproot) adresser og oppdage deres genereringsprosess.

### Avledning av en SegWit v1 (bech32m) Adresse

For Taproot-adresser, er genereringsprosessen litt annerledes. La oss se på dette sammen!

Fra trinnet med kompresjon av offentlig nøkkel, vises en første distinksjon sammenlignet med ECDSA: de offentlige nøklene brukt for Schnorr på Bitcoin representeres kun ved deres abscissa ($x$). Derfor er det ingen prefiks, og den komprimerte nøkkelen måler nøyaktig 256 bits.
Som vi så i forrige kapittel, låser en P2TR-script bitcoins på en unik Schnorr offentlig nøkkel, betegnet ved $Q$. Denne nøkkelen $Q$ er en aggregat av to offentlige nøkler: $P$, en hoved intern offentlig nøkkel, og $M$, en offentlig nøkkel avledet fra Merkle-roten av en liste over _scriptPubKey_. Bitcoins låst med denne typen script kan brukes på to måter:

- Ved å publisere en signatur for den offentlige nøkkelen $P$ (_key path_);
- Ved å tilfredsstille ett av scriptene inkludert i Merkle-treet (_script path_).

I virkeligheten er disse to nøklene ikke virkelig "aggregerte." Nøkkelen $P$ er i stedet justert av nøkkelen $M$. I kryptografi betyr det å "justere" en offentlig nøkkel å modifisere denne nøkkelen ved å anvende en additiv verdi kalt en "justering." Denne operasjonen lar den modifiserte nøkkelen forbli kompatibel med den opprinnelige private nøkkelen og justeringen. Teknisk sett er en justering en skalarverdi $t$ som legges til den opprinnelige offentlige nøkkelen. Hvis $P$ er den opprinnelige offentlige nøkkelen, blir den justerte nøkkelen:

$$
P' = P + tG
$$

Hvor $G$ er generatoren av den elliptiske kurven som brukes. Denne operasjonen produserer en ny offentlig nøkkel avledet fra den opprinnelige nøkkelen, samtidig som den beholder kryptografiske egenskaper som tillater dens bruk.
Hvis du ikke trenger å legge til alternative skript (bruker utelukkende via _nøkkelbanen_), kan du generere en Taproot-adresse basert kun på den offentlige nøkkelen som er til stede på dybde 5 i lommeboken din. I dette tilfellet er det nødvendig å opprette et ikke-utgiftbart skript for _skriptbanen_, for å tilfredsstille kravene til strukturen. Justeringen $t$ blir deretter beregnet ved å anvende en merket hash-funksjon, **`TapTweak`**, på den interne offentlige nøkkelen $P$:

$$
t = \text{H}_{\text{TapTweak}}(P)
$$

hvor:

- **$\text{H}_{\text{TapTweak}}$** er en SHA256 hash-funksjon merket med taggen `TapTweak`. Hvis du ikke er kjent med hva en merket hash-funksjon er, inviterer jeg deg til å konsultere kapittel 3.3;
- $P$ er den interne offentlige nøkkelen, representert i sitt komprimerte 256-bits format, ved å bruke kun $x$-koordinaten.

Taproot-offentlige nøkkelen $Q$ blir deretter beregnet ved å legge til justeringen $t$, multiplisert med elliptisk kurvegenerator $G$, til den interne offentlige nøkkelen $P$:

$$
Q = P + t \cdot G
$$

Når Taproot-offentlige nøkkelen $Q$ er oppnådd, kan vi generere den tilsvarende mottaksadressen. I motsetning til andre formater, er Taproot-adresser ikke etablert på en hash av den offentlige nøkkelen. Derfor blir nøkkelen $Q$ satt direkte inn i adressen, på en rå måte.

For å starte, ekstraherer vi $x$-koordinaten til punktet $Q$ for å oppnå en komprimert offentlig nøkkel. På denne lasten beregnes en sjekksum ved hjelp av BCH-koder, som med SegWit v0-adresser. Programmet som brukes for Taproot-adresser, er imidlertid litt forskjellig. Faktisk, etter introduksjonen av _bech32_-formatet med SegWit, ble en feil oppdaget: når den siste karakteren av en adresse er en `p`, gjør innsetting eller fjerning av `q`er rett før denne `p`en ikke sjekksummen ugyldig. Selv om denne feilen ikke har konsekvenser på SegWit v0 (takket være en størrelsesbegrensning), kunne den utgjøre et problem i fremtiden. Denne feilen har derfor blitt rettet for Taproot-adresser, og det nye korrigerte formatet kalles "_bech32m_".

Taproot-adressen genereres ved å kode $x$-koordinaten til $Q$ i _bech32m_-formatet, med følgende elementer:

- **HRP (_Human Readable Part_)**: `bc`, for å indikere hoved Bitcoin-nettverket;
- **Versjonen**: `1` for å indikere Taproot / SegWit v1;
- **Sjekksummen**.

Den endelige adressen vil derfor ha formatet:

```
bc1p[Qx][sjekksum]
```

På den annen side, hvis du ønsker å legge til alternative skript i tillegg til å bruke den interne offentlige nøkkelen (_skriptbanen_), vil beregningen av mottaksadressen være litt annerledes. Du må inkludere hashen av de alternative skriptene i beregningen av justeringen. I Taproot, kalles hvert alternativt skript, som ligger i enden av Merkle-treet, en "blad".

Når de forskjellige alternative skriptene er skrevet, må du sende dem individuelt gjennom en merket hash-funksjon `TapLeaf`, ledsaget av noe metadata:

$$
\text{h}_{\text{blad}} = \text{H}_{\text{TapLeaf}} (v \Vert sz \Vert S)
$$

Med:

- $v$: versjonsnummeret til skriptet (standard `0xC0` for Taproot);
- $sz$: størrelsen på skriptet kodet i _CompactSize_-formatet; 
- $S$: skriptet.

De forskjellige skript-hashene ($\text{h}_{\text{leaf}}$) sorteres først i leksikografisk rekkefølge. Deretter blir de konkatenert i par og sendt gjennom den merkede hash-funksjonen `TapBranch`. Denne prosessen gjentas iterativt for å bygge, steg for steg, Merkle-treet:
$$
\text{h}_{\text{branch}} = \text{H}_{\text{TapBranch}}(\text{h}_{\text{leaf1}} \Vert \text{h}_{\text{leaf2}})
$$

Vi fortsetter deretter med å konkatenere resultatene to og to, og sender dem gjennom den merkede hash-funksjonen `TapBranch` ved hvert steg, til vi oppnår Merkle-treets rot:

![CYP201](assets/fr/066.webp)

Når Merkle-roten $h_{\text{root}}$ er beregnet, kan vi beregne tweaken. For å gjøre dette, kobles den interne offentlige nøkkelen til lommeboken $P$ med roten $h_{\text{root}}$, og resultatet kjøres gjennom den merkede hash-funksjonen `TapTweak`:

$$
t = \text{H}_{\text{TapTweak}}(P \Vert h_{\text{root}})
$$

Til slutt, som tidligere, oppnås Taproot offentlig nøkkel $Q$ ved å legge til den interne offentlige nøkkelen $P$ til produktet av tweaken $t$ og generatorpunktet $G$:

$$
Q = P + t \cdot G
$$

Genereringen av adressen følger deretter samme prosess, hvor den rå offentlige nøkkelen $Q$ brukes som nyttelast, sammen med noen ekstra metadata.


Og der har du det! Vi har nådd slutten av dette CYP201-kurset. Hvis du fant dette kurset nyttig, ville jeg være veldig takknemlig hvis du kunne ta deg noen øyeblikk til å gi det en god vurdering i det følgende evalueringskapittelet. Føl deg også fri til å dele det med dine kjære eller på dine sosiale nettverk. Til slutt, hvis du ønsker å oppnå ditt diplom for dette kurset, kan du ta den endelige eksamenen rett etter evalueringskapittelet.

# Konklusjon

<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>

## Evaluer dette kurset

<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>
<isCourseReview>true</isCourseReview>

## Avsluttende eksamen

<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>
<isCourseExam>true</isCourseExam>

## Konklusjon

<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

Vi har nådd slutten av CYP201-opplæringen. Jeg håper den har vært nyttig i din Bitcoin-læring og har hjulpet deg å bedre forstå hvordan HD-lommebøkene du bruker daglig fungerer. Takk for at du fulgte dette kurset til slutten!

Etter min mening er denne kunnskapen om lommebøker fundamental, da den knytter et teoretisk aspekt av Bitcoin til dens praktiske bruk. Hvis du bruker Bitcoin, håndterer du nødvendigvis lommebokprogramvare. Å forstå deres indre virkemåte gjør det mulig å implementere effektive sikkerhetsstrategier mens du behersker de underliggende mekanismene, risikoene og potensielle svakhetene. Dermed kan du bruke Bitcoin sikrere og med tillit.

Hvis du ikke allerede har gjort det, inviterer jeg deg til å vurdere og kommentere denne opplæringen. Det ville hjulpe meg enormt. Du kan også dele denne opplæringen på dine sosiale nettverk for å spre denne kunnskapen til så mange som mulig.

For å fortsette reisen din ned i kaninhullet, anbefaler jeg sterkt **BTC204**-opplæringen, som jeg også har produsert på Plan ₿ Network. Den er dedikert til Bitcoin-personvern og utforsker nøkkeltemaer: Hva er personvernmodellen? Hvordan fungerer kjedeanalyse? Hvordan bruke Bitcoin optimalt for å maksimere personvernet ditt? Et logisk neste steg for å fordype ferdighetene dine!

https://planb.network/courses/btc204

For å fortsette å fordype din kunnskap i Bitcoin-universet, inviterer vi deg til å utforske andre kurs tilgjengelige på Plan ₿ Network som:

#### Lær å skape ditt Bitcoin-fellesskap med

https://planb.network/courses/btc302

#### Oppdag Lightning Network med

https://planb.network/courses/lnp201

#### Oppdag den økonomiske tankegangen til den østerrikske skolen med

https://planb.network/courses/eco201

#### Oppdag historien om Bitcoins opprinnelse med

https://planb.network/courses/his201

#### Oppdag frihetens utvikling gjennom tidene med

https://planb.network/courses/phi201




