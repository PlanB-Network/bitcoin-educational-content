---
term: BECH32 OG BECH32M

---
`Bech32` og `Bech32m` er to adressekodingsformater for mottak av bitcoins. De er basert på en lett modifisert base 32. De inneholder en sjekksum basert på en feilkorrigerende algoritme kalt BCH (*Bose-Chaudhuri-Hocquenghem*). Sammenlignet med eldre adresser, som er kodet i `Base58check`, har `Bech32`- og `Bech32m`-adressene en mer effektiv sjekksum, noe som gjør det mulig å oppdage og potensielt automatisk korrigere skrivefeil. Formatet gir også bedre lesbarhet, med bare små bokstaver. Her er addisjonsmatrisen for dette formatet fra base 10:

&nbsp;

| + | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

| --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 0 | q | p | z | r | y | 9 | x | 8 |

| 8 g f 2 t v d w 0

16 | s | 3 | j | n | 5 | 4 | k | h | 5 | 4 | k | h

| 24 c e 6 m u a 7 l

&nbsp;

Bech32 og Bech32m er kodingsformater som brukes til å representere SegWit-adresser. Bech32 er et adressekodingsformat som ble introdusert av BIP173 i 2017. Det bruker et bestemt sett med tegn, bestående av tall og små bokstaver, for å minimere skrivefeil og gjøre det lettere å lese. Bech32-adresser starter vanligvis med `bc1` for å indikere at de er hjemmehørende i SegWit. Dette formatet brukes bare på SegWit V0-adresser, med skriptene P2WPKH (Pay to Witness Public Key Hash) og P2WSH (Pay to Witness Script Hash). Det er imidlertid en liten, uventet feil som er spesifikk for Bech32-formatet. Når det siste tegnet i adressen er en `p`, blir ikke sjekksummen ugyldig ved å legge til eller fjerne et hvilket som helst antall `q`-tegn umiddelbart før det. Dette påvirker ikke eksisterende bruk av SegWit V0-adresser (BIP173) på grunn av deres begrensning til to definerte lengder. Dette kan imidlertid påvirke fremtidig bruk av Bech32-kodingen. Bech32m-formatet er rett og slett et Bech32-format med denne feilen rettet. Det ble introdusert med BIP350 i 2020. Bech32m-adresser starter også med `bc1`, men de er spesielt utformet for å være kompatible med SegWit V1 (Taproot) og senere versjoner, med skriptet P2TR (Pay to TapRoot).