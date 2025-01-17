---
name: Mnemonic Phrase - Dice Roll
description: Hvordan generere din egen gjenopprettingsfrase med terninger?
---
![cover](assets/cover.webp)

I denne veiledningen vil du lære hvordan du manuelt kan konstruere en gjenopprettingsfrase for en Bitcoin-lommebok ved hjelp av terningkast.

**ADVARSEL:** Å generere en mnemonic frase på en sikker måte krever at det ikke etterlates noen digital spor under dens skapelse, noe som er nesten umulig. Ellers ville lommeboken presentere en altfor stor angrepsflate, noe som betydelig øker risikoen for at dine bitcoins blir stjålet. **Det er derfor sterkt frarådet å overføre midler til en lommebok som avhenger av en gjenopprettingsfrase du har generert selv.** Selv om du følger denne veiledningen til punkt og prikke, er det en risiko for at gjenopprettingsfrasen kan bli kompromittert. **Derfor bør denne veiledningen ikke anvendes til opprettelsen av en ekte lommebok.** Bruk av en maskinvarelommebok for denne oppgaven er mye mindre risikabelt, da den genererer frasen offline, og ekte kryptografer har vurdert bruken av kvalitative entropikilder.

Denne veiledningen kan følges kun for eksperimentelle formål for opprettelsen av en fiktiv lommebok, uten intensjonen om å bruke den med ekte bitcoins. Imidlertid tilbyr opplevelsen to fordeler:
- For det første lar den deg bedre forstå mekanismene som ligger til grunn for din Bitcoin-lommebok;
- For det andre gir den deg kunnskap om hvordan du gjør det. Jeg sier ikke at det vil være nyttig en dag, men det kan det være!

## Hva er en mnemonic frase?
En gjenopprettingsfrase, også noen ganger kalt en "mnemonic", "seed phrase", eller "secret phrase", er en sekvens som vanligvis består av 12 eller 24 ord, som genereres på en pseudo-tilfeldig måte fra en kilde til entropi. Den pseudo-tilfeldige sekvensen fullføres alltid med en kontrollsum.

Mnemonic frasen, sammen med en valgfri passfrase, brukes til deterministisk å avlede alle nøklene assosiert med en HD (Hierarchical Deterministic) lommebok. Dette betyr at fra denne frasen, er det mulig å deterministisk generere og gjenskape alle de private og offentlige nøklene til Bitcoin-lommeboken, og dermed, få tilgang til midlene assosiert med den.
![mnemonic](assets/notext/1.webp)
Formålet med denne setningen er å tilby et lett-å-bruke middel for sikkerhetskopiering og gjenoppretting av bitcoins. Det er avgjørende å holde mnemonic frasen på et trygt og sikkert sted, da enhver som er i besittelse av denne frasen ville ha tilgang til midlene i den tilsvarende lommeboken. Hvis den brukes i konteksten av en tradisjonell lommebok, og uten en valgfri passfrase, utgjør den ofte et SPOF (Single Point Of Failure). 
Vanligvis blir denne frasen gitt direkte til deg når du oppretter lommeboken din, av programvaren eller maskinvarelommeboken som brukes. Det er imidlertid også mulig å generere denne frasen selv, og deretter angi den på det valgte støttet for å avlede lommeboknøklene. Dette er hva vi vil lære å gjøre i denne veiledningen.

## Forberedelse av nødvendige materialer
For å skape din gjenopprettingsfrase for hånd, vil du trenge:
- Et ark papir;
- En penn eller blyant, ideelt sett i forskjellige farger for å lette organiseringen;
- Flere terninger, for å minimere risikoen for skjevhet relatert til en ubalansert terning;
- [Listen over 2048 BIP39 ord](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf) printet ut.

Etter dette vil bruk av en datamaskin med en terminal bli nødvendig for beregningen av kontrollsummen. Det er nettopp av denne grunn jeg fraråder manuell generering av mnemonic frasen. Etter min mening øker inngripen av en datamaskin, selv under forholdsreglene nevnt i denne veiledningen, betydelig sårbarheten til en lommebok.
For en eksperimentell tilnærming angående en "fiktiv lommebok", er det mulig å bruke din vanlige datamaskin og dens terminal. Imidlertid, for en mer rigorøs tilnærming rettet mot å begrense risikoen for å kompromittere din frase, ville det ideelle være å bruke en PC frakoblet fra internett (helst uten en wifi-komponent eller RJ45 kablet tilkobling), utstyrt med et minimum av periferiutstyr (alt bør være koblet til med kabel, for å unngå Bluetooth), og fremfor alt, kjørende på en amnesisk Linux-distribusjon som [Tails](https://tails.boum.org/index.fr.html), startet fra et flyttbart medium.
![mnemonic](assets/notext/2.webp)

I en reell kontekst, ville det være avgjørende å sikre konfidensialiteten til arbeidsområdet ditt ved å velge en plassering borte fra nysgjerrige øyne, uten persontrafikk, og fri for kameraer (webkameraer, telefoner...).
Det anbefales å bruke et høyt antall terninger for å redusere effekten av en potensielt ubalansert terning på entropien. Før bruk, anbefales det å sjekke terningene: dette kan oppnås ved å teste dem i en bolle med saltmettet vann, som lar terningene flyte. Deretter fortsetter du å rulle hver terning omtrent tjue ganger i saltvannet, og observere resultatene. Hvis en eller to sider vises uforholdsmessig sammenlignet med de andre, utvid testen med flere kast. Uniformt fordelt resultater indikerer at terningen er pålitelig. Imidlertid, hvis en eller to sider regelmessig dominerer, bør disse terningene settes til side, da de kunne kompromittere entropien til din mnemoniske frase og dermed sikkerheten til lommeboken din.
I reelle forhold, etter å ha utført disse sjekkene, ville du være klar til å generere den nødvendige entropien. For en eksperimentell fiktiv lommebok opprettet som en del av denne opplæringen, kunne du naturligvis hoppe over disse forberedelsene.

## Noen Påminnelser om Gjenopprettingsfrasen
For å begynne, vil vi gjennomgå grunnleggende om å skape en mnemonisk frase i henhold til BIP39. Som tidligere forklart, er frasen avledet fra pseudo-tilfeldig informasjon av en viss størrelse, hvortil et kontrollsum legges til for å sikre dens integritet.

Størrelsen på denne opprinnelige informasjonen, ofte referert til som "entropi", bestemmes av antall ord du ønsker å oppnå i gjenopprettingsfrasen. De mest vanlige formatene er fraser på 12 og 24 ord, som henholdsvis stammer fra en entropi på 128 bits og 256 bits. Her er en tabell som viser de forskjellige størrelsene av entropi i henhold til BIP39:

| Phrase (words) | Entropy (bits) | Checksum (bits) | Entropy + Checksum (bits) |
| --------------- | --------------- | --------------- | -------------------------- |
| 12              | 128             | 4               | 132                        |
| 15              | 160             | 5               | 165                        |
| 18              | 192             | 6               | 198                        |
| 21              | 224             | 7               | 231                        |
| 24              | 256             | 8               | 264                        |

Entropi er altså et tilfeldig tall mellom 128 og 256 bits. I denne opplæringen, vil vi ta eksemplet med en 12-ords frase, der entropien er 128 bits, noe som betyr at vi vil generere en tilfeldig sekvens av 128 `0`er eller `1`er. Dette representerer et tall bestående av 128 sifre i base 2 (binær).
Basert på denne entropien, vil en kontrollsum bli generert. En kontrollsum er en verdi beregnet fra et sett med data, brukt til å verifisere integriteten og gyldigheten av disse dataene under deres overføring eller lagring. Algoritmer for kontrollsum er designet for å oppdage tilfeldige feil eller endringer i dataene.
I tilfellet med vår mnemonic frase, er funksjonen til kontrollsummen å oppdage eventuelle inntastingsfeil når frasen tastes inn i en lommebokprogramvare. En ugyldig kontrollsum signaliserer tilstedeværelsen av en feil i frasen. Omvendt indikerer en gyldig kontrollsum at frasen mest sannsynlig er korrekt.
For å oppnå denne kontrollsummen, blir entropien sendt gjennom SHA256 hash-funksjonen. Denne operasjonen produserer en 256-bits sekvens som output, hvorav kun de første `N` bitene vil bli beholdt, `N` avhengig av den ønskede lengden på gjenopprettingsfrasen (se tabellen ovenfor). Således, for en 12-ords frase, vil de første 4 bitene av hashen bli beholdt.
![mnemonic](assets/en/3.webp)
Disse første 4 bitene, som danner kontrollsummen, vil deretter bli lagt til den opprinnelige entropien. På dette stadiet er gjenopprettingsfrasen praktisk talt konstituert, men den er fortsatt i binær form. For å konvertere denne binære sekvensen til ord i samsvar med BIP39-standarden, vil vi først dele sekvensen inn i 11-bits segmenter.
![mnemonic](assets/notext/4.webp)
Hvert av disse pakkene representerer et tall i binær som deretter vil bli konvertert til et desimaltall (base 10). Vi vil legge til `1` til hvert tall, fordi i databehandling, starter tellingen fra `0`, men BIP39-listen er nummerert fra `1`.

![mnemonic](assets/notext/5.webp)

Til slutt forteller tallet i desimal oss posisjonen til det tilsvarende ordet i [listen over 2048 BIP39 ord](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf). Alt som gjenstår er å velge disse ordene for å sette sammen gjenopprettingsfrasen for vår lommebok.

![mnemonic](assets/notext/6.webp)

Nå, la oss gå videre til praksis! Vi vil generere en 12-ords gjenopprettingsfrase. Imidlertid forblir denne operasjonen identisk i tilfellet av en 24-ords frase, bortsett fra at den ville kreve 256 bits entropi og en 8-bits kontrollsum, som angitt i ekvivalenstabellen som ligger i begynnelsen av denne seksjonen.

## Steg 1: Generering av Entropi
Forbered ditt ark med papir, din penn, og dine terninger. For å begynne, vil vi trenge å generere 128 bits tilfeldig, det vil si, en sekvens av 128 `0`er og `1`er på rad. For å gjøre dette, vil vi bruke terninger.
![mnemonic](assets/notext/7.webp)

Terninger har 6 sider, alle med en identisk sannsynlighet for å bli rullet. Imidlertid er vårt mål å produsere et binært resultat, noe som betyr to mulige utfall. Derfor vil vi tildele verdien `0` til hvert kast som lander på et partall, og `1` for hvert oddetall. Som et resultat, vil vi utføre 128 kast for å skape vår 128-bits entropi. Hvis terningen viser `2`, `4`, eller `6`, vil vi skrive ned `0`; for `1`, `3`, eller `5`, vil det være `1`. Hvert resultat vil bli notert sekvensielt, fra venstre til høyre og fra topp til bunn.

For å lette de følgende trinnene, vil vi gruppere bitene i pakker på fire og tre, som vist på bildet nedenfor. Hver linje må ha 11 bits: 2 pakker med 4 bits og en pakke med 3 bits.

![mnemonic](assets/notext/8.webp)
Som du kan se i eksemplet mitt, består det tolvte ordet for øyeblikket av bare 7 bits. Disse vil bli komplettert av de 4 bitsene fra sjekksummen i neste steg for å danne de 11 bitsene.
![mnemonic](assets/notext/9.webp)

## Steg 2: Beregning av sjekksum
Dette steget er det mest kritiske i den manuelle genereringen av en mnemonic frase, ettersom det krever bruk av en datamaskin. Som nevnt tidligere, tilsvarer sjekksummen begynnelsen av SHA256-hashen generert fra entropien. Selv om det teoretisk er mulig å beregne en SHA256 for hånd for en input på 128 eller 256 bits, kunne denne oppgaven ta en hel uke. Dessuten ville eventuelle feil i manuelle beregninger kun bli identifisert ved slutten av prosessen, noe som tvinger deg til å starte på nytt fra begynnelsen. Derfor er det utenkelig å gjøre dette steget med bare et ark papir og en penn. En datamaskin er nesten obligatorisk. Hvis du fortsatt ønsker å lære hvordan du gjør en SHA256 for hånd, forklarer vi hvordan du gjør det i [CRYPTO301-kurset](https://planb.network/en/courses/crypto301).

Av denne grunn, fraråder jeg sterkt å lage en manuell frase for en faktisk lommebok. Etter min mening, selv med alle nødvendige forholdsregler, øker bruk av en datamaskin på dette stadiet angrepsflaten for lommeboken urimelig.
For å beregne sjekksummen mens man etterlater så få spor som mulig, vil vi bruke en amnesisk Linux-distribusjon fra et flyttbart drev kalt **Tails**. Dette operativsystemet starter fra en USB-stick og opererer helt på datamaskinens RAM, uten å samhandle med harddisken. Dermed, i teorien, etterlater det ingen spor på datamaskinen etter at den er slått av. Vær oppmerksom på at Tails kun er kompatibelt med x86_64-type prosessorer, og ikke med ARM-type prosessorer.
For å starte, fra din vanlige datamaskin, [last ned Tails-bildet fra den offisielle nettsiden](https://tails.net/install/index.fr.html). Sørg for autentisiteten til nedlastingen din ved å bruke utviklerens signatur eller verifiseringsverktøyet som tilbys av nettstedet.
![mnemonic](assets/notext/10.webp)
Først, fortsett å formatere USB-sticken din, deretter installer Tails ved hjelp av et verktøy som [Balena Etcher](https://etcher.balena.io/).
![mnemonic](assets/notext/11.webp)
Etter å ha bekreftet at flashingen er vellykket, slå av datamaskinen din. Deretter fortsett å koble fra strømforsyningen og fjern harddisken fra PC-ens hovedkort. I tilfelle en WiFi-kort er til stede, bør det kobles fra. På samme måte, fjern eventuelle RJ45 Ethernet-kabler. For å minimere risikoen for datalekkasje, anbefales det å koble fra internettboksen din og slå av mobiltelefonen din. Dessuten, sørg for å koble fra eventuelle overflødige periferiutstyr fra datamaskinen din, som mikrofonen, webkameraet, høyttalerne eller headsettet, og sjekk at andre periferiutstyr kun er koblet til via kabel. Alle disse PC-forberedelsesstegene er ikke essensielle, men de hjelper bare til å redusere angrepsflaten så mye som mulig i en reell kontekst.

Sjekk om BIOS-en din er konfigurert til å tillate oppstart fra en ekstern enhet. Hvis ikke, endre denne innstillingen, deretter start maskinen på nytt. Når du har sikret datamaskinmiljøet, start datamaskinen fra USB-sticken med Tails OS.

På Tails velkomstskjerm, velg språket du foretrekker, deretter start systemet ved å klikke på `Start Tails`.

![mnemonic](assets/notext/12.webp)

Fra skrivebordet, klikk på `Applikasjoner`-fanen.

![mnemonic](assets/notext/13.webp)

Naviger til `Verktøy`-menyen.
Og til slutt, klikk på `Terminal`-applikasjonen.

![mnemonic](assets/notext/15.webp)

Du vil komme til et nytt blankt kommandoterminal.

![mnemonic](assets/notext/16.webp)
Skriv inn `echo`-kommandoen, etterfulgt av din tidligere genererte entropi, og sørg for å sette inn et mellomrom mellom `echo` og din binære siffersekvens.
![mnemonic](assets/notext/17.webp)

Legg til et ekstra mellomrom, deretter skriv inn følgende kommando, ved å bruke en *pipe* (`|`):
```plaintext
| shasum -a 256 -0
```

![mnemonic](assets/notext/18.webp)

I eksemplet med min entropi, er den totale kommandoen som følger:
```plaintext
echo 11010111000110111011000011000010011000100111000001000000001001011011001010111111001010011111110001010100000101110010010011011010 | shasum -a 256 -0
```

I denne kommandoen:
- `echo` brukes til å sende bitssekvensen;
- `|`, *pipen*, brukes til å dirigere utdata fra `echo`-kommandoen til inndata for neste kommando;
- `shasum` initierer en hashingfunksjon som tilhører SHA (*Secure Hash Algorithm*)-familien;
- `-a` spesifiserer valget av en spesifikk hashingalgoritme;
- `256` indikerer at SHA256-algoritmen brukes;
- `-0` tillater inndata å bli tolket som et binært tall.

Etter å ha nøye sjekket at din binære sekvens ikke inneholder noen skrivefeil, trykk på `Enter`-tasten for å utføre kommandoen. Terminalen vil deretter vise SHA256-hashen av din entropi.

![mnemonic](assets/notext/19.webp)

For nå er hashen uttrykt i heksadesimalt format (base 16). For eksempel er min:
```plaintext
a27abf1aff70311917a59a43ce86fa45a62723a00dd2f9d3d059aeac9b4b13d8
```

For å fullføre vår mnemoniske frase, trenger vi bare de første 4 bitene av hashen, som utgjør kontrollsummen. I heksadesimalt format representerer hver karakter 4 bit. Dermed vil vi bare beholde den første karakteren av hashen. For en 24-ords frase, ville det være nødvendig å ta hensyn til de to første karakterene. I mitt eksempel tilsvarer dette bokstaven: `a`. Noter nøye denne karakteren et sted på arket ditt, deretter slå av datamaskinen din.

Neste steg er å konvertere denne heksadesimale karakteren (base 16) til en binær verdi (base 2), ettersom vår frase er konstruert i dette formatet. For å gjøre dette, kan du bruke følgende konverteringstabell:


| Desimal (base 10) | Heksadesimal (base 16) | Binær (base 2) |
| ----------------- | --------------------- | --------------- |
| 0                 | 0                     | 0000            |
| 1                 | 1                     | 0001            |
| 2                 | 2                     | 0010            |
| 3                 | 3                     | 0011            |
| 4                 | 4                     | 0100            |
| 5                 | 5                     | 0101            |
| 6                 | 6                     | 0110            |
| 7                 | 7                     | 0111            |
| 8                 | 8                     | 1000            |
| 9                 | 9                     | 1001            |
| 10                | a                     | 1010            |
| 11                | b                     | 1011            |
| 12                | c                     | 1100            |
| 13                | d                     | 1101            |
| 14                | e                     | 1110            |
| 15                | f                     | 1111            |

I mitt eksempel tilsvarer bokstaven `a` det binære tallet `1010`. Disse 4 bitene danner sjekksummen for vår gjenopprettingsfrase. Du kan nå legge dem til entropien du allerede har notert på arket ditt, ved å plassere dem på slutten av det siste ordet.

![mnemonic](assets/notext/20.webp)

Din mnemonic frase er nå komplett, men den er i binært format. Neste steg vil være å konvertere den til desimalsystemet slik at du deretter kan knytte hvert tall til et tilsvarende ord i BIP39-listen.

## Steg 3: Konvertere Ord til Desimal
For å konvertere hver binær linje til et desimaltall, vil vi bruke en metode som letter manuell beregning. For øyeblikket har du tolv linjer på papiret ditt, hver bestående av 11 binære sifre `0` eller `1`. For å fortsette med en konvertering til desimal, tilordne til hvert første siffer verdien `1024` hvis det er `1`, ellers `0`. For det andre sifferet, vil verdien `512` bli tilordnet hvis det er `1`, ellers `0`, og så videre til det ellevte sifferet. Tilsvarelsene er som følger:
- 1. bit: `1024`;
- 2. bit: `512`;
- 3. bit: `256`;
- 4. bit: `128`;
- 5. bit: `64`;
- 6. bit: `32`;
- 7. bit: `16`;
- 8. bit: `8`;
- 9. bit: `4`;
- 10. bit: `2`;
- 11. bit: `1`.

For hver linje, vil vi legge sammen verdiene som tilsvarer sifrene `1` for å få det desimaltallet som tilsvarer det binære tallet. La oss ta eksemplet med en binær linje lik:
```plaintext
1010 1101 101
```

Konverteringen vil være som følger:
![mnemonic](assets/notext/21.webp)
Resultatet vil da være:
```plaintext
1389
```

For hvert bit lik `1`, rapporter det tilhørende tallet nedenfor. For hvert bit lik `0`, rapporter ingenting.

![mnemonic](assets/notext/22.webp)
Deretter, legg ganske enkelt sammen alle tallene validert av `1`-ene for å få det desimaltallet som representerer hver binær linje. For eksempel, her er hvordan det ser ut for mitt ark:
![mnemonic](assets/notext/23.webp)

## Steg 4: Søke etter Ordene til den Mnemoniske Frasen
Med de oppnådde desimaltallene, kan vi nå finne de tilsvarende ordene i listen for å sette sammen den mnemoniske frasen. Imidlertid, nummereringen av de 2048 ordene i BIP39-listen varierer fra `1` til `2048`. Men, våre beregnede binære resultater varierer fra `0` til `2047`. Derfor er det en enhetsforskyvning som må korrigeres. For å rette opp denne forskyvningen, legg ganske enkelt til `1` til de tolv tidligere beregnede desimaltallene.

![mnemonic](assets/notext/24.webp)
Etter denne justeringen har du rangen til hvert ord i listen. Alt som gjenstår er å identifisere hvert ord med dets nummer. Åpenbart, som med alle de andre stegene, må du ikke bruke datamaskinen din til å utføre denne konverteringen. Derfor, sørg for at du har skrevet ut listen på forhånd.
[**-> Skriv ut BIP39-listen i A4-format.**](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf)

For eksempel, hvis nummeret som er avledet fra den første linjen er 1721, vil det tilsvarende ordet være det 1721. på listen:
```plaintext
1721. strike
```
![mnemonic](assets/notext/25.webp)
På denne måten fortsetter vi suksessivt med de 12 ordene for å konstruere vår mnemonic frase.

![mnemonic](assets/notext/26.webp)

## Steg 5: Opprette Bitcoin-lommeboken
På dette tidspunktet er alt som gjenstår å importere vår mnemonic frase inn i en Bitcoin-lommebokprogramvare. Avhengig av våre preferanser, kan dette gjøres på en skrivebordsprogramvare for å få en hot wallet, eller på en hardware-lommebok for en cold wallet.

![mnemonic](assets/notext/27.webp)

Det er bare under importeringen at du kan verifisere gyldigheten av din checksum. Hvis programvaren viser en melding som `Invalid Checksum`, betyr det at en feil har sneket seg inn i din opprettelsesprosess. Generelt stammer denne feilen enten fra en feilberegning under de manuelle konverteringene og tillegg, eller fra en skrivefeil når du taster inn din entropi i terminalen på Tails. Det vil være nødvendig å starte prosessen på nytt fra begynnelsen for å rette opp disse feilene.

![mnemonic](assets/notext/28.webp)
Etter å ha opprettet lommeboken din, ikke glem å sikkerhetskopiere din gjenopprettingsfrase på et fysisk medium, som papir eller metall, og ødelegge regnearket som ble brukt under genereringen for å forhindre eventuelle informasjonslekkasjer.

## Spesifikt tilfelle av Dice Roll-alternativet på Coldcards
Hardware-lommebøkene fra Coldcard-familien tilbyr [en funksjon kalt *Dice Roll*](https://youtu.be/Rc29d9m92xg?si=OeFW2iCGRvxexhK7), for å generere din lommeboks gjenopprettingsfrase med terninger. Denne metoden er utmerket fordi den gir deg direkte kontroll over opprettelsen av entropi, uten å kreve bruk av en ekstern enhet for å beregne checksum som i vår veiledning.

Imidlertid har det nylig blitt rapportert om tilfeller av bitcoin-tyveri på grunn av feil bruk av denne funksjonen. Faktisk kan et for begrenset antall terningkast føre til utilstrekkelig entropi, teoretisk gjør det mulig å brute force mnemonic-frasen og stjele de tilknyttede bitcoinene. For å unngå denne risikoen, anbefales det å utføre minst 99 terningkast på Coldcard, noe som sikrer tilstrekkelig entropi.

Metoden for å tolke resultatene foreslått av Coldcard avviker fra den som er presentert i denne veiledningen. Mens vi anbefaler 128 kast for å oppnå 128 bits sikkerhet i veiledningen, foreslår Coldcard 99 kast for å nå 256 bits sikkerhet. Faktisk, i vår tilnærming, er kun to utfall mulige for hvert terningkast: partall (`0`) eller oddetall (`1`). Derfor er entropien generert av hvert kast lik `log2(2)`. I tilfellet med Coldcard, som tar hensyn til de seks mulige sidene av terningen (fra `1` til `6`), er entropien per kast lik `log2(6)`. Dette er grunnen til at i vår veiledning, må vi utføre flere kast for å oppnå samme nivå av entropi.

```plaintext
Entropi = antall kast * log2(antall mulige utfall på terningen)
Coldcard:

Entropi = 99 * log2(6)
Entropi = 255.91

Vår opplæring:

Entropi = 128 * log2(2)
Entropi = 128