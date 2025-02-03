---
term: BECH32 A BECH32M

---
`Bech32` a `Bech32m` jsou dva formáty kódování adres pro příjem bitcoinů. Jsou založeny na mírně upravené bázi 32. Obsahují kontrolní součet založený na algoritmu pro opravu chyb zvaném BCH (*Bose-Chaudhuri-Hocquenghem*). V porovnání se staršími adresami, kódovanými v `Base58check`, mají adresy `Bech32` a `Bech32m` účinnější kontrolní součet, který umožňuje odhalit a případně automaticky opravit překlepy. Jejich formát také nabízí lepší čitelnost, neboť obsahují pouze malá písmena. Zde je sčítací matice pro tento formát od základu 10:

&nbsp;

| + | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

| --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 0 | q | p | z | r | y | 9 | x | 8 |

| 8 | g | f | 2 | t | v | d | w | 0 |

| 16 | s | 3 | j | n | 5 | 4 | k | h |

| 24 | c | e | 6 | m | u | a | 7 | l |

&nbsp;

Bech32 a Bech32m jsou formáty kódování používané k reprezentaci adres SegWit. Bech32 je formát kódování adres, který v roce 2017 zavedl BIP173. Používá specifickou sadu znaků složenou z čísel a malých písmen, aby se minimalizovaly chyby při psaní a usnadnilo čtení. Adresy Bech32 obvykle začínají znakem `bc1`, který označuje, že se jedná o nativní adresy SegWit. Tento formát se používá pouze u adres SegWit V0 se skripty P2WPKH (Pay to Witness Public Key Hash) a P2WSH (Pay to Witness Script Hash). Existuje však malá, neočekávaná chyba specifická pro formát Bech32. Pokud je posledním znakem adresy `p`, přidání nebo odebrání libovolného počtu znaků `q` bezprostředně před ním nezpůsobí neplatnost kontrolního součtu. To nemá vliv na stávající použití adres SegWit V0 (BIP173) vzhledem k jejich omezení na dvě definované délky. Mohlo by to však ovlivnit budoucí použití kódování Bech32. Formát Bech32m je jednoduše formát Bech32 s opravenou touto chybou. Byl zaveden s protokolem BIP350 v roce 2020. Adresy Bech32m také začínají `bc1`, ale jsou speciálně navrženy tak, aby byly kompatibilní se SegWit V1 (Taproot) a novějšími verzemi, se skriptem P2TR (Pay to TapRoot).