---
term: TYP MĚNY
---

V kontextu deterministických a hierarchických (HD) peněženek je typ měny (*coin type* v angličtině) úroveň derivace, která umožňuje rozlišovat větve peněženky na základě různých používaných kryptoměn. Tato vrstva derivace, definovaná BIP 44, se nachází na hloubce 2 struktury derivace, následuje po hlavním klíči a účelu. Například pro Bitcoin je přiřazený index `0x80000000`, označený jako `/0'/` v cestě derivace. To znamená, že všechny adresy a účty odvozené z této cesty jsou spojeny s Bitcoinem. Tato vrstva derivace umožňuje jasnou separaci různých aktiv v peněžence s více měnami. Zde jsou indexy používané pro různé kryptoměny:
* Bitcoin: `0x80000000`;
* Bitcoin Testnet: `0x80000001`;
* Litecoin: `0x80000002`;
* Dogecoin: `0x80000003`;
* Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.png)