---
term: RODZAJ WALUTY
---

W kontekście portfeli deterministycznych i hierarchicznych (HD), typ waluty (*coin type* w języku angielskim) jest poziomem derywacji, który pozwala na rozróżnienie gałęzi Wallet w oparciu o różne używane kryptowaluty. Ten Layer derywacji, zdefiniowany przez BIP 44, znajduje się na głębokości 2 struktury derywacji, po kluczu głównym i celu. Na przykład dla Bitcoin przypisany indeks to `0x80000000`, oznaczony jako `/0'/` w ścieżce derywacji. Oznacza to, że wszystkie adresy i konta wyprowadzone z tej ścieżki są powiązane z Bitcoin. Ten Layer derywacji umożliwia wyraźne oddzielenie różnych aktywów w wielowalutowym Wallet. Oto indeksy używane dla różnych kryptowalut:


- Bitcoin: `0x80000000`;
- Bitcoin Testnet: `0x800001`;
- Litecoin: `0x80000002`;
- Dogecoin: `0x80000003`;
- Ethereum: `0x8000003c`...


![](../../dictionnaire/assets/21.webp)