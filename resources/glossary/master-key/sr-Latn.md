---
term: MASTER KEY
---

U kontekstu HD (Hijerarhijski Deterministički) novčanika, glavni privatni ključ je jedinstveni privatni ključ izveden iz Wallet-ovog seed. Da bi se dobio glavni ključ, funkcija `HMAC-SHA512` se primenjuje na seed, koristeći reči "*Bitcoin seed*" doslovno kao ključ. Rezultat ove operacije proizvodi 512-bitni izlaz, pri čemu prvih 256 bita čini glavni ključ, a preostalih 256 bita formira glavni lančani kod. Glavni ključ i glavni lančani kod služe kao početna tačka za izvođenje svih podređenih privatnih i javnih ključeva u HD Wallet-ovoj strukturi stabla. Stoga, glavni privatni ključ je na dubini 0 izvođenja.


![](../../dictionnaire/assets/19.webp)