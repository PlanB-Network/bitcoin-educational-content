---
term: TYP MĚNY

---
V kontextu deterministických a hierarchických (HD) peněženek je typ měny (anglicky *coin type*) úrovní derivace, která umožňuje rozlišovat větve peněženky na základě různých používaných kryptoměn. Tato úroveň derivace, definovaná v BIP 44, se nachází v hloubce 2 struktury derivace, a to za hlavním klíčem a účelem. Například pro Bitcoin je přiřazený index `0x80000000`, v derivační cestě označený jako `/0'/`. To znamená, že všechny adresy a účty odvozené z této cesty jsou spojeny s Bitcoinem. Tato vrstva odvození umožňuje jasné oddělení různých aktiv v peněžence s více měnami. Zde jsou uvedeny indexy používané pro různé kryptoměny:


- Bitcoin: `0x80000000`;
- Bitcoin Testnet: `0x80000001`;
- Litecoin: `0x80000002`;
- Dogecoin: `0x80000003`;
- Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.webp)