---
term: VALUTATYPE

---
I forbindelse med deterministiske og hierarkiske (HD) lommebøker er valutatypen (*coin type* på engelsk) et avledningsnivå som gjør det mulig å differensiere lommebokens grener basert på de ulike kryptovalutaene som brukes. Dette avledningslaget, definert av BIP 44, er plassert på dybde 2 i avledningsstrukturen, etter hovednøkkelen og formålet. For eksempel er den tildelte indeksen for Bitcoin `0x80000000`, notert som `/0'/` i avledningsstien. Dette betyr at alle adresser og kontoer som er avledet fra denne banen, er knyttet til Bitcoin. Dette avledningslaget muliggjør en klar separasjon av ulike eiendeler i en lommebok med flere valutaer. Her er indeksene som brukes for ulike kryptovalutaer:


- Bitcoin: `0x80000000`;
- Bitcoin Testnet: `0x80000001`;
- Litecoin: `0x80000002`;
- Dogecoin: `0x80000003`;
- Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.webp)