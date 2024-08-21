---
term: FIBRE
---

Akronym pro "*Fast Internet Bitcoin Relay Engine*". Jedná se o protokol navržený Mattem Corallo v roce 2016 za účelem urychlení distribuce Bitcoinových bloků po celém světě. Jeho cílem bylo snížit zpoždění šíření bloků co nejblíže k fyzickým limitům. FIBRE si klade za cíl zajistit spravedlivější rozdělení příležitostí pro těžbu, tím, že se snaží, aby podíl vygenerovaných bloků účastníkem přesně odrážel jeho příspěvek v podobě výpočetního výkonu, bez ohledu na jeho pozici v síti.

Skutečně, latence při přenosu bloků může favorizovat velké, dobře propojené skupiny těžařů, často umístěné blízko sebe, na úkor menších. Tento jev by mohl časem zvýšit centralizaci těžby a snížit celkovou bezpečnost systému. Aby se tento problém řešil, FIBRE zavedl korekční kódy a přenos dodatečných dat pro vyrovnání ztráty paketů, stejně jako použití kompaktních bloků podobných těm, které jsou popsané v BIP152, vše fungující přes UDP, aby se obešly určité omezení TCP. Nicméně, FIBRE byl v roce 2020 opuštěn, hlavně kvůli závislosti na jediném správci a skutečnosti, že adopce BIP152 učinila takový systém méně nezbytným.