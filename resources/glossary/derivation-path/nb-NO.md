---
term: AVLEDNINGSVEI

---
I forbindelse med hierarkisk deterministiske (HD) lommebøker refererer en avledningssti til sekvensen av indekser som brukes til å avlede underordnede nøkler fra en hovednøkkel. Denne stien er beskrevet i BIP32 og identifiserer trestrukturen for avledning av underordnede nøkler. En avledningssti representeres av en serie indekser atskilt med skråstreker, og starter alltid med hovednøkkelen (angitt som `m/`). En typisk sti kan for eksempel være `m/84'/0'/0'/0'/0/0`. Hvert avledningsnivå er knyttet til en bestemt dybde:


- `m /` angir den private hovednøkkelen. Den er unik for en lommebok og kan ikke ha søsken på samme dybde. Hovednøkkelen avledes direkte fra seed;
- `m / purpose' /` angir avledningsformålet som bidrar til å identifisere standarden som følges. Dette feltet er beskrevet i BIP43. Hvis lommeboken for eksempel følger BIP84-standarden (SegWit V0), vil indeksen være `84';
- `m / purpose' / coin-type' /` angir typen kryptovaluta. Dette gjør det mulig å skille tydelig mellom grener som er dedikert til én kryptovaluta og grener som er dedikert til en annen i en lommebok med flere mynter. Indeksen dedikert til Bitcoin er `0`;
- `m / formål' / mynttype' / konto' /` angir kontonummeret. Denne dybden gjør det enkelt å skille mellom og organisere en lommebok i forskjellige kontoer. Disse kontoene er nummerert fra `0`. Utvidede nøkler (`xpub`, `xprv`...) finnes på dette dybdenivået;
- `m / formål' / mynttype' / konto' / veksling /` angir banen. Hver konto som er definert i dybde 3, har to stier i dybde 4: en ekstern kjede og en intern kjede (også kalt "change"). Den eksterne kjeden avleder adresser som er ment å deles offentlig, det vil si de adressene som tilbys oss når vi klikker på "motta" i lommebokprogramvaren vår. Den interne kjeden utleder adresser som ikke er ment å utveksles offentlig, hovedsakelig endringsadresser. Den eksterne kjeden er identifisert med indeksen `0` og den interne kjeden er identifisert med indeksen `1`. Du vil legge merke til at fra denne dybden utfører vi ikke lenger en herdet avledning, men en normal avledning (det er ingen apostrof). Det er takket være denne mekanismen at vi er i stand til å avlede alle de underordnede offentlige nøklene fra deres `xpub`;
- `m / formål' / mynttype' / konto' / endring / adresse-indeks` angir ganske enkelt nummeret på mottakeradressen og dens nøkkelpar, for å skille den fra søsknene på samme dybde på samme gren. For eksempel har den første avledede adressen indeksen `0`, den andre adressen har indeksen `1`, og så videre ...

Hvis mottakeradressen min for eksempel har avledningsstien `m / 86' / 0' / 0' / 0' / 0 / 5`, kan vi utlede følgende informasjon:


- `86'` indikerer at vi følger avledningsstandarden til BIP86 (Taproot / SegWit V1);
- `0'` indikerer at det er en Bitcoin-adresse;
- `0'` indikerer at vi befinner oss på den første kontoen i lommeboken;
- `0` indikerer at det er en ekstern adresse;
- `5` indikerer at det er den sjette eksterne adressen til denne kontoen.

![](../../dictionnaire/assets/18.webp)