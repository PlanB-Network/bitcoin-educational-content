---
name: Picocrypt
description: Et verktøy med åpen kildekode for å kryptere dataene dine
---
![cover](assets/cover.webp)



___



*Denne opplæringen er basert på originalt innhold av Florian BURNEL publisert på [IT-Connect](https://www.it-connect.fr/). Lisens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Det er gjort endringer i det opprinnelige innholdet.*



___



## I. Presentasjon



I denne veiledningen tar vi en titt på Picocrypt, en enkel, lett og effektiv krypteringsprogramvare for kryptering av data med et høyt sikkerhetsnivå.



Den er egnet for **kryptering av filer**, og du kan bruke den til å beskytte **data på datamaskinen din, på en USB-pinne**, men også data som er lagret i skyen. Du kan for eksempel kryptere data og lagre dem på **Microsoft OneDrive, Google Drive, iCloud eller Dropbox**, selv om jeg til dette formålet foretrekker en annen programvare som vil bli presentert i en fremtidig artikkel.



Du kan også bruke den når du trenger å **dele data med en tredjepart**: Takket være Picocrypt og dekrypteringsnøkkelen kan de dekryptere dataene på sin egen maskin. Så hvis kontoen eller datamaskinen din blir kompromittert, er dataene dine beskyttet.



For å følge Picocrypt-prosjektet finnes det bare én Address:





- [Picocrypt på GitHub](https://github.com/Picocrypt/Picocrypt)



PicoCrypt er helt **gratis og med åpen kildekode**, og er tilgjengelig for **Windows,** **Linux** og **macOS**. På Windows kan du installere det på din egen maskin eller bruke den bærbare versjonen.



## II. Picocrypt, krypteringsprogramvare med åpen kildekode



**Picocrypt** krypteringsprogramvare presenterer seg selv som **et alternativ** til andre velkjente løsninger som **VeraCrypt** og **Cryptomator** (*designet for å kryptere data i skymiljøer*), eller **AxCrypt**. På Picocrypts offisielle GitHub kan du forresten finne en sammenligning med noen konkurrenter:



|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Kilde: [Github.com](https://github.com/Picocrypt/Picocrypt)



Picocrypt er **veldig lett**, veier bare **3 MB**, og trenger ikke installeres: det er et **bærbart program** som ikke krever administratorrettigheter! Sikkerheten er imidlertid ikke satt til side, siden den baserer seg på **robuste og pålitelige algoritmer**:





- **XChaCha20**-krypteringsalgoritme
- Nøkkelforbikoblingsfunksjon **Argon2**



I tillegg til de nevnte fordelene, er det som virkelig appellerer til deg **den enkle bruken**!



Den trenger bare én ting: **en koderevisjon**, men det er planlagt, som du kan se i sammenligningstabellen ovenfor (siste linje). Men siden det er åpen kildekode, er det ingenting som hindrer deg i å ta en titt på kildekoden.



Selv om det sammenlignes med BitLocker i tabellen ovenfor, **er BitLocker og Picocrypt etter min mening beregnet på forskjellige bruksområder**: BitLocker for kryptering av et komplett volum (for eksempel Windows) og Picocrypt for kryptering av en trestruktur eller lagringsplass av typen "Drive".



## III. Bruk av Picocrypt



Til denne demonstrasjonen brukes en Windows 11-maskin.



### A. Kryptering av data med Picocrypt



Først og fremst må du laste ned Picocrypt.exe fra den offisielle GitHub ([se denne siden](https://github.com/Picocrypt/Picocrypt/releases)).



Åpne programmet for å vise den minimalistiske Interface på skjermen. For å kryptere data, det være seg **en fil, flere filer eller en mappe**, er det bare å **dra og slippe den inn i Picocrypts Interface**. Dette vil velge dataene som skal krypteres.



![Image](assets/fr/020.webp)



Når det gjelder kryptering av data, har du tilgang til flere alternativer, blant annet krypteringsnøkkelen. Det kan være **et sterkt passord** eller **en krypteringsnøkkel i form av en nøkkelfil**, eller **begge deler**. Hvis vi tar et passord som eksempel, kan du velge mellom å lage ditt eget passord eller å generere et passord med Picocrypt.



Dette passordet må være sterkt, da det kan brukes til å dekryptere dataene. Skriv det inn under "**Passord**" og "**Bekreft passord**", og klikk deretter på "**Krypter**" for å kryptere dataene! Før det kan du klikke på "** Endre **" -knappen ved siden av "** Lagre utdata som **" for å spesifisere utdatakatalogen.



**Merknad**: For å bruke en nøkkel i filformat, klikk på "**Create**" til høyre for "**Keyfiles**" for å opprette en nøkkel. Velg den deretter ved å klikke på "**Edit**" og dra og slippe nøkkelfilen i det aktuelle området.



![Image](assets/fr/019.webp)



De to valgte filene er **kryptert og gruppert sammen** i filen "**Encrypted.zip.pcv**", siden **PCV** er filtypen som brukes av Picocrypt. Denne ZIP-filen er uleselig takket være krypteringen. For å forhindre at utvalgte filer blir gruppert sammen i én enkelt kryptert ZIP-fil, må du krysse av for alternativet "**Recursively**", slik at det blir like mange krypterte filer som det er filer som skal krypteres.



For å få tilgang til dataene våre må vi dekryptere dem ved hjelp av Picocrypt.



![Image](assets/fr/023.webp)



Før vi snakker om dekryptering av data, får du her litt informasjon om noen av alternativene som er tilgjengelige:





- **Paranoid modus**: Bruk det høyeste sikkerhetsnivået som Picocrypt tilbyr. Verktøyet bruker flere kaskadekrypteringsalgoritmer (XChaCha20 og Serpent) og HMAC-SHA3 i stedet for BLAKE2b for dataautentisering.
- **Reed-Solomon**: implementerer *Reed-Solomon*-feilkorrigeringskoder for å gjøre det lettere å korrigere feil i korrupte data. Dette gjør at du kan støtte et korrupsjonsnivå på rundt 3 % av filen din.
- **Del opp i biter** eller **del opp i flere deler**: Hvis du krypterer en stor fil, kan du be Picocrypt om å dele den opp i flere deler. Dette kan gjøre filen enklere å overføre.
- **Komprimere filer** eller **Komprimere filer**: Komprimere filer for å redusere størrelsen på krypterte filer.
- **Slettede filer** eller **Fichiers supprimés**: slett kildefiler for å beholde kun den krypterte versjonen



### B. Dekryptering av data med Picocrypt



Hvis du trenger å dekryptere dataene, er det ikke mer komplisert enn å kryptere dem. Bare åpne Picocrypt og **dra og slipp PCV-filen som skal dekrypteres**. Deretter skriver du inn passordet og/eller velger nøkkelfilen før du klikker på "**Dekrypter**".



![Image](assets/fr/021.webp)



Den ukrypterte versjonen av ZIP-arkivet "Encrypted.zip" gjør at jeg nå kan gjenopprette de to filene mine i klartekst!



![Image](assets/fr/022.webp)



## IV. Konklusjon



**Du har blitt advart: Picocrypt er veldig enkelt å bruke, og det fungerer! Selv om Interface er minimalistisk, inneholder den noen svært nyttige alternativer for å tilpasse krypteringen! Og siden den er tilgjengelig i en bærbar versjon, kan du ta den med deg overalt, slik at du trygt kan dekryptere dataene dine**



Sørg for å bruke sterke passord for å beskytte data, og hvis du bruker en nøkkelfil, må du huske å ta sikkerhetskopi av den, ellers vil du ikke lenger kunne dekryptere PCV-containeren som genereres av Picocrypt. Til slutt bør du vite at det også finnes [en CLI-versjon](https://github.com/Picocrypt/CLI) (med færre funksjoner) som lar deg kjøre Picocrypt fra kommandolinjen: også her åpner Picocrypt døren til nye muligheter.



https://planb.academy/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5