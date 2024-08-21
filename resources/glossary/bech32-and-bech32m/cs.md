---
term: BECH32 A BECH32M
---

`Bech32` a `Bech32m` jsou dva formáty kódování adres pro přijímání bitcoinů. Jsou založeny na mírně upravené bázi 32. Zahrnují kontrolní součet založený na algoritmu pro opravu chyb nazvaném BCH (*Bose-Chaudhuri-Hocquenghem*). Ve srovnání s tradičními adresami, které jsou kódovány v `Base58check`, mají adresy `Bech32` a `Bech32m` efektivnější kontrolní součet, což umožňuje detekci a potenciální automatickou opravu překlepů. Jejich formát také nabízí lepší čitelnost, pouze s malými písmeny. Zde je přídavná matice pro tento formát z báze 10:

&nbsp;

| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

&nbsp;
Bech32 a Bech32m jsou formáty kódování používané pro reprezentaci SegWit adres. Bech32 je formát kódování adres představený BIP173 v roce 2017. Používá specifickou sadu znaků, skládající se z čísel a malých písmen, aby minimalizoval chyby při psaní a usnadnil čtení. Adresy Bech32 obvykle začínají `bc1`, aby naznačily, že jsou nativně SegWit. Tento formát je používán pouze pro SegWit V0 adresy se skripty P2WPKH (Pay to Witness Public Key Hash) a P2WSH (Pay to Witness Script Hash). Nicméně, existuje malá, neočekávaná chyba specifická pro formát Bech32. Kdykoli je poslední znak adresy `p`, přidání nebo odebrání libovolného počtu znaků `q` bezprostředně před ním nezpůsobí neplatnost kontrolního součtu. To neovlivňuje stávající použití SegWit V0 adres (BIP173) díky jejich omezení na dvě definované délky. Nicméně, to by mohlo ovlivnit budoucí použití kódování Bech32. Formát Bech32m je jednoduše formát Bech32 s opravenou touto chybou. Byl představen s BIP350 v roce 2020. Adresy Bech32m také začínají `bc1`, ale jsou specificky navrženy tak, aby byly kompatibilní se SegWit V1 (Taproot) a pozdějšími verzemi, se skriptem P2TR (Pay to TapRoot).