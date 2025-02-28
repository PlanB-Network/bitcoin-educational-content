---
term: MASTER KEY

---
V kontextu peněženek HD (Hierarchical Deterministic) je hlavním soukromým klíčem jedinečný soukromý klíč odvozený ze seedu peněženky. K získání hlavního klíče se na seed použije funkce `HMAC-SHA512`, přičemž jako klíč se doslova použijí slova "*Bitcoin seed*". Výsledkem této operace je 512bitový výstup, přičemž prvních 256 bitů tvoří hlavní klíč a zbývajících 256 bitů tvoří hlavní řetězový kód. Hlavní klíč a hlavní řetězový kód slouží jako výchozí bod pro odvození všech podřízených soukromých a veřejných klíčů ve stromové struktuře peněženky HD. Hlavní soukromý klíč je tedy v hloubce 0 odvození.

![](../../dictionnaire/assets/19.webp)