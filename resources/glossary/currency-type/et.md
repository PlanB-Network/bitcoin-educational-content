---
term: VALUUTA TÜÜP

---
Deterministlike ja hierarhiliste (HD) rahakottide kontekstis on valuutatüüp (*coin type* inglise keeles) tuletamise tase, mis võimaldab rahakoti harude eristamist erinevate kasutatavate krüptovaluutade alusel. See tuletamistasand, mis on määratletud BIP 44-s, asub tuletamisstruktuuri 2. sügavusel, pärast üldvõtit ja eesmärki. Näiteks Bitcoini puhul on määratud indeks `0x80000000`, mis on tuletamisrajal märgitud kui `/0'/`. See tähendab, et kõik sellest teest tuletatud aadressid ja kontod on seotud Bitcoiniga. See tuletamise kiht võimaldab erinevate varade selget eraldamist mitme valuuta rahakotis. Siin on erinevate krüptovaluutade jaoks kasutatavad indeksid:


- Bitcoin: `0x80000000`;
- Bitcoin Testnet: `0x80000001`;
- Litecoin: `0x80000002`;
- Dogecoin: `0x80000003`;
- Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.webp)