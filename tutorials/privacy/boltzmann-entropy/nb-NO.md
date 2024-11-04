---
name: Boltzmann-kalkulator
description: Forstå konseptet med entropi og hvordan du bruker Boltzmann
---
![cover](assets/cover.webp)

***ADVARSEL:** Etter arrestasjonen av grunnleggerne av Samourai Wallet og beslagleggelsen av deres servere den 24. april, er nettsiden KYCP.org for øyeblikket utilgjengelig. Gitlab som hoster Python-koden for Boltzmann-kalkulatoren, har også blitt beslaglagt. Fra nå av er det ikke lenger mulig å laste ned dette verktøyet. Det er imidlertid mulig at koden kan bli publisert på nytt av andre i de kommende ukene. I mellomtiden kan du fortsatt dra nytte av denne opplæringen for å forstå hvordan Boltzmann-kalkulatoren fungerer. Indikatorene som dette verktøyet gir, er anvendelige på enhver Bitcoin-transaksjon og kan også beregnes manuelt. Jeg vil gi alle nødvendige beregninger i denne opplæringen. Hvis du allerede hadde lastet ned Python-verktøyet på maskinen din eller hvis du bruker en RoninDojo, kan du fortsette å bruke verktøyet og følge denne opplæringen som vanlig, det fungerer fortsatt.*

_Vi følger nøye med på utviklingen av denne saken samt utviklingen angående de tilknyttede verktøyene. Vær trygg på at vi vil oppdatere denne opplæringen så snart ny informasjon blir tilgjengelig._

_Denne opplæringen er gitt kun for utdannings- og informasjonsformål. Vi støtter eller oppmuntrer ikke bruk av disse verktøyene til kriminelle formål. Det er hver brukers ansvar å overholde lovene i sin jurisdiksjon._

---

Boltzmann-kalkulatoren er et verktøy for å analysere en Bitcoin-transaksjon ved å måle dens entropinivå sammen med andre avanserte målinger. Den gir innsikt i forbindelsene mellom inngangene og utgangene av en transaksjon. Disse indikatorene tilbyr en kvantifisert vurdering av en transaksjons privatliv og hjelper med å identifisere potensielle feil.

Dette Python-verktøyet ble utviklet av teamene hos Samourai Wallet og OXT, men det kan brukes på enhver Bitcoin-transaksjon.

## Hvordan bruke Boltzmann-kalkulatoren?
For å bruke Boltzmann-kalkulatoren, har du to alternativer tilgjengelig. Det første er å installere Python-verktøyet direkte på maskinen din. Alternativt kan du velge KYCP.org (_Know Your Coin Privacy_) nettsiden, som tilbyr en forenklet brukerplattform. For RoninDojo-brukere, merk at dette verktøyet allerede er integrert i noden din.

Å bruke KYCP-siden er ganske enkelt: bare skriv inn transaksjonsidentifikatoren (TXID) du ønsker å analysere i søkefeltet og trykk `ENTER`.
![KYCP](assets/1.webp)
Du vil da finne forskjellig informasjon om transaksjonen, inkludert koblingene mellom inngangene og utgangene. Klikk på `deterministiske koblinger`.
![KYCP](assets/2.webp)
Du vil komme til siden dedikert til indikatorene for Boltzmann-kalkulatoren.
![KYCP](assets/3.webp)
For de som foretrekker å bruke verktøyet direkte fra sin RoninDojo-node, er det tilgjengelig via `RoninCLI > Samourai Toolkit > Boltzmann-kalkulator`.

Som med KYCP.org-siden, når Python-verktøyet er installert, trenger du bare å lime inn TXID for transaksjonen du ønsker å analysere.

![KYCP](assets/7.webp)

Deretter trykker du på `ENTER`-tasten for å få resultatene.

![KYCP](assets/8.webp)

## Hva er indikatorene for Boltzmann-kalkulatoren?
### Kombinasjoner / Tolking:
Den første indikatoren som programvaren beregner, er det totale antallet mulige kombinasjoner, indikert under `nb combinations` eller `interpretations` i verktøyet.
Med tanke på verdiene til UTXOene som er involvert i transaksjonen, beregner denne indikatoren antall måter inndataene kan assosieres med utdataene på. Med andre ord, den bestemmer antall plausible tolkninger som en transaksjon kan fremkalle fra perspektivet til en ekstern observatør som analyserer den. For eksempel, en coinjoin strukturert i henhold til Whirlpool 5x5-modellen presenterer `1,496` mulige kombinasjoner: ![KYCP](assets/4.webp)
En Whirlpool Surge Cycle 8x8 coinjoin, på den andre siden, presenterer `9,934,563` mulige tolkninger: ![KYCP](assets/5.webp)
I kontrast vil en mer tradisjonell transaksjon med 1 inndata og 2 utdata kun presentere en enkelt tolkning: ![KYCP](assets/6.webp)

### Entropi:
Den andre indikatoren som beregnes er entropien til en transaksjon, betegnet ved `Entropy`.

I den generelle konteksten av kryptografi og informasjon, er entropi et kvantitativt mål på usikkerheten eller uforutsigbarheten assosiert med en datakilde eller en tilfeldig prosess. Med andre ord, entropi er en måte å måle hvor vanskelig informasjon er å forutsi eller gjette.

I den spesifikke konteksten av kjedeanalyse, er entropi også navnet på en indikator, avledet fra Shannon entropi og [oppfunnet av LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), som beregnes med Boltzmann-verktøyet.

Når en transaksjon presenterer et høyt antall mulige kombinasjoner, er det ofte mer relevant å referere til dens entropi. Denne indikatoren tillater måling av mangel på kunnskap hos analytikere om den eksakte konfigurasjonen av transaksjonen. Med andre ord, jo høyere entropi, desto vanskeligere blir oppgaven med å identifisere bitcoin-bevegelser mellom inndata og utdata for analytikere.

I praksis avslører entropi om, fra perspektivet til en ekstern observatør, en transaksjon presenterer flere mulige tolkninger, basert utelukkende på mengdene av inndata og utdata, uten å vurdere andre eksterne eller interne mønstre og heuristikker. Høy entropi er da synonymt med bedre konfidensialitet for transaksjonen.

Entropi er definert som den binære logaritmen av antall mulige kombinasjoner. Her er formelen som brukes:
```plaintext
E: entropien til transaksjonen
C: antall mulige kombinasjoner for transaksjonen

E = log2(C)
```

I matematikk tilsvarer den binære logaritmen (base-2 logaritmen) den inverse operasjonen av å opphøye 2. Med andre ord, den binære logaritmen av `x` er eksponenten som `2` må opphøyes til for å oppnå `x`. Denne indikatoren uttrykkes dermed i bits.

La oss ta eksemplet med å beregne entropien for en coinjoin-transaksjon strukturert i henhold til Whirlpool 5x5-modellen, som, som nevnt tidligere, tilbyr et antall mulige kombinasjoner på `1,496`:
```plaintext
C = 1,496
E = log2(1,496)
E = 10.5469 bits
```
Dermed viser denne coinjoin-transaksjonen en entropi på `10.5469 bits`, som anses som meget tilfredsstillende. Jo høyere denne verdien er, desto flere forskjellige tolkninger tillater transaksjonen, og dermed styrker den sitt nivå av privatliv.
For en 8x8 coinjoin-transaksjon som presenterer `9,934,563` tolkninger, ville entropien være:
```plaintext
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bits
```
La oss ta et annet eksempel med en mer konvensjonell transaksjon, som inneholder ett inndata og to utdata: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) I tilfellet med denne transaksjonen er den eneste mulige tolkningen: `(In.0) > (Out.0 ; Out.1)`. Følgelig er dens entropi fastsatt til `0`:
```plaintext
C = 1
E = log2(1)
E = 0 bits
```

### Effektivitet:
Den tredje indikatoren som tilbys av Boltzmann-kalkulatoren er kalt `Wallet Efficiency` (Lommebok Effektivitet). Denne indikatoren vurderer effektiviteten av transaksjonen ved å sammenligne den med den optimale transaksjonen som er tenkelig i en identisk konfigurasjon.

Dette fører oss til å diskutere konseptet med maksimal entropi, som tilsvarer den høyeste entropien en spesifikk transaksjonsstruktur teoretisk kunne oppnå. Transaksjonens effektivitet beregnes deretter ved å konfrontere denne maksimale entropien med den faktiske entropien til den analyserte transaksjonen.

Formelen som brukes er som følger:
```plaintext
ER: den faktiske entropien til transaksjonen uttrykt i bits
EM: den maksimale mulige entropien for en gitt transaksjonsstruktur uttrykt i bits
Ef: effektiviteten til transaksjonen i bits

Ef = ER - EM
```

For eksempel, for en Whirlpool 5x5-type coinjoin-struktur, er den maksimale entropien satt til `10.5469`:
```plaintext
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bits
```

Denne indikatoren uttrykkes også som en prosentandel, og formelen er da:
```plaintext
CR: det faktiske antallet mulige kombinasjoner
CM: det maksimale antallet mulige kombinasjoner med samme struktur
Ef: effektiviteten uttrykt som en prosentandel

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```

En effektivitet på `100%` indikerer dermed at transaksjonen maksimerer sitt potensial for personvern i henhold til sin struktur.

### Entropitetthet:
Den fjerde indikatoren er entropitettheten, notert på verktøyet `Entropy Density` (Entropitetthet). Den gir et perspektiv på entropien i forhold til hvert inndata eller utdata i transaksjonen. Denne indikatoren viser seg nyttig for å evaluere og sammenligne effektiviteten til transaksjoner av forskjellige størrelser. For å beregne den, deler du ganske enkelt den totale entropien til transaksjonen med det totale antallet inndata og utdata som er involvert:
```plaintext
ED: entropitettheten uttrykt i bits
E: entropien til transaksjonen uttrykt i bits
T: det totale antallet inndata og utdata i transaksjonen

ED = E / T
```

La oss ta eksemplet med en Whirlpool 5x5 coinjoin:
```plaintext
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bits
```

La oss også beregne entropitettheten for en Whirlpool 8x8 coinjoin:
```plaintext
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bits
```
Det femte stykket informasjon levert av Boltzmann-kalkulatoren er tabellen over samsvarssannsynligheter mellom inndata og utdata. Denne tabellen indikerer, gjennom Boltzmann-scoren, den betingede sannsynligheten for at en spesifikk inndata er relatert til en gitt utdata.
Det er altså et kvantitativt mål på den betingede sannsynligheten for at en assosiasjon mellom en inndata og en utdata i en transaksjon forekommer, basert på forholdet mellom antall gunstige forekomster av denne hendelsen til det totale antall mulige forekomster, i et sett med tolkninger.

Tar vi eksempelet med en Whirlpool coinjoin igjen, vil tabellen over betingede sannsynligheter fremheve sjansene for kobling mellom hver inndata og utdata, og gir et kvantitativt mål på tvetydigheten av assosiasjoner i transaksjonen:

| %       | Utdata 0 | Utdata 1 | Utdata 2 | Utdata 3 | Utdata 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Inndata 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Inndata 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Inndata 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Inndata 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Inndata 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Her kan vi tydelig se at hver inndata har en like stor sjanse for å være assosiert med hvilken som helst utdata, noe som forbedrer transaksjonens konfidensialitet.
Beregning av Boltzmann-scoren innebærer å dele antall tolkninger der en viss hendelse forekommer, med det totale antall tilgjengelige tolkninger. Så, for å bestemme scoren som assosierer inndata nr. 0 med utdata nr. 3 (`512` tolkninger), brukes følgende prosedyre:
```plaintext
Tolkninger (IN.0 > UT.3) = 512
Totalt antall tolkninger = 1496
Score = 512 / 1496 = 34%
```

Tar vi eksempelet med en Whirlpool 8x8 coinjoin (surge-syklus), ville Boltzmann-tabellen se slik ut:

|       | UT.0 | UT.1 | UT.2 | UT.3 | UT.4 | UT.5 | UT.6 | UT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   || IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

Imidlertid, i tilfellet med en enkel transaksjon med ett inngangspunkt og to utgangspunkter, er situasjonen annerledes:

| %       | Utgang 0 | Utgang 1 |
|---------|----------|----------|
| Inngang 0 | 100%     | 100%     |

Her observeres det at sannsynligheten for at hver utgang stammer fra inngang nr. 0 er `100%`. En lavere sannsynlighet oversetter dermed til større personvern ved å fortynne de direkte koblingene mellom innganger og utganger.

### Deterministiske Koblinger:
Det sjette stykket informasjon som gis er antallet deterministiske koblinger, supplert med forholdet mellom disse koblingene. Denne indikatoren avslører hvor mange forbindelser mellom inngangene og utgangene i den analyserte transaksjonen som er udiskutable, med en sannsynlighet på `100%`. Forholdet, på den andre siden, gir et perspektiv på vekten av disse deterministiske koblingene innenfor hele settet av transaksjonskoblinger.
For eksempel har en Whirlpool-type coinjoin-transaksjon ingen deterministiske koblinger, og viser derfor en indikator og et forhold på `0%`. I motsetning, i vår andre enkle transaksjon undersøkt (med én inngang og to utganger), er indikatoren satt til `2` og forholdet når `100%`. Dermed signaliserer en nullindikator utmerket konfidensialitet på grunn av fraværet av direkte og udiskutable koblinger mellom innganger og utganger.

**Eksterne Ressurser:**

- Boltzmann-kode på Samourai
- [Bitcoin-transaksjoner og personvern (Del I) av Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Bitcoin-transaksjoner og personvern (Del II) av Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Bitcoin-transaksjoner og personvern (Del III) av Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- KYCP-nettsted
- [Medium-artikkel om en introduksjon til Boltzmann-script av Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)