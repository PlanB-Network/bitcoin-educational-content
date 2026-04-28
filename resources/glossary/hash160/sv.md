---
term: HASH160
definition: Funktion som kombinerar SHA256 och därefter RIPEMD160, används för att generera Bitcoin-adresser.
---

Kryptografisk funktion som används i Bitcoin, särskilt för att generera Legacy- och SegWit v0-mottagningsadresser. Den kombinerar två Hash-funktioner som körs successivt på indata: först SHA256, sedan RIPEMD160. Utdata från denna funktion är därför 160 bitar.


$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$$