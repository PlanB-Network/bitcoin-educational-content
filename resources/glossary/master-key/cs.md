---
term: MASTER KEY
---

V kontextu HD (Hierarchical Deterministic) peněženek je hlavní soukromý klíč unikátní soukromý klíč odvozený ze seedu peněženky. Pro získání hlavního klíče je na seed aplikována funkce `HMAC-SHA512`, přičemž jako klíč se doslova používají slova "*Bitcoin seed*". Výsledek této operace produkuje 512bitový výstup, přičemž prvních 256 bitů tvoří hlavní klíč a zbývajících 256 bitů tvoří hlavní řetězový kód. Hlavní klíč a hlavní řetězový kód slouží jako výchozí bod pro odvození všech dětských soukromých a veřejných klíčů ve stromové struktuře HD peněženky. Hlavní soukromý klíč je tedy na úrovni 0 derivace.

![](../../dictionnaire/assets/19.png)