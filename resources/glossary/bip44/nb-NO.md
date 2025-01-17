---
term: BIP44

---
Et forslag til forbedring som innfører en standard hierarkisk avledningsstruktur for HD-lommebøker. BIP44 bygger på prinsippene som ble etablert av BIP32 for nøkkelavledning og på BIP43 for bruk av "purpose"-feltet. Den introduserer en avledningsstruktur med fem nivåer: `m / purpose' / coin_type' / account' / change / address_index`. Her er detaljene for hver dybde:


- `m /` angir den private hovednøkkelen. Den er unik for en lommebok og kan ikke ha søsken på samme dybde. Hovednøkkelen er direkte avledet fra lommebokens seed;
- `m / purpose' /` angir avledningsformålet som bidrar til å identifisere standarden som følges. Dette feltet er beskrevet i BIP43. Hvis lommeboken for eksempel følger BIP84 (SegWit V0)-standarden, vil indeksen være `84';
- `m / purpose' / coin-type' /` angir typen kryptovaluta. Dette gjør det mulig å skille tydelig mellom grener som er dedikert til én kryptovaluta og grener som er dedikert til en annen kryptovaluta i en lommebok med flere mynter. Indeksen dedikert til Bitcoin er `0';
- `m / formål' / mynttype' / konto' /` angir kontonummeret. Denne dybden gjør det enkelt å skille mellom og organisere en lommebok i forskjellige kontoer. Disse kontoene er nummerert fra `0`. Utvidede nøkler (`xpub`, `xprv`...) finnes på denne dybden;
- `m / formål' / mynttype' / konto' / vekslepenger /` angir kjeden. Hver konto som definert i dybde 3 har to kjeder i dybde 4: en ekstern kjede og en intern kjede (også kalt "change"). Den eksterne kjeden utleder adresser som er ment å kommuniseres offentlig, dvs. adressene som tilbys oss når vi klikker på "motta" i lommebokprogramvaren vår. Den interne kjeden utleder adresser som ikke skal utveksles offentlig, dvs. primært endringsadresser. Den eksterne kjeden er identifisert med indeksen `0` og den interne kjeden er identifisert med indeksen `1`. Du vil legge merke til at fra denne dybden utfører vi ikke lenger en herdet avledning, men en normal avledning (det er ingen apostrof). Det er takket være denne mekanismen at vi er i stand til å avlede alle de underordnede offentlige nøklene fra deres `xpub`;
- `m / formål' / mynttype' / konto' / endring / adresse-indeks` angir ganske enkelt nummeret på mottakeradressen og dens nøkkelpar, for å skille den fra søsknene på samme dybde på samme gren. For eksempel har den første avledede adressen indeksen `0`, den andre adressen har indeksen `1`, og så videre ...

Hvis mottaksadressen min for eksempel har avledningsstien `m / 86' / 0' / 0' / 0' / 0 / 5`, kan vi utlede følgende informasjon:


- `86'` indikerer at vi følger avledningsstandarden til BIP86 (Taproot eller SegWitV1);
- `0'` indikerer at det er en Bitcoin-adresse;
- `0'` indikerer at vi befinner oss på den første kontoen i lommeboken;
- `0` indikerer at det er en ekstern adresse;
- `5` indikerer at det er den sjette eksterne adressen til denne kontoen.

![](../../dictionnaire/assets/18.webp)