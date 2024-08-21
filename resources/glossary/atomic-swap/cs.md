---
term: ATOMIC SWAP
---

Technologie umožňující přímou výměnu kryptoměn mezi dvěma stranami, bez nutnosti důvěry a bez potřeby zprostředkovatele. Tyto výměny se nazývají "atomické", protože mohou mít pouze dva výsledky:
* Buď je výměna úspěšná a oba účastníci účinně vyměnili své kryptoměny;
* Nebo výměna selže a oba účastníci si ponechají své původní kryptoměny.

Atomické swapy lze provádět buď se stejnou kryptoměnou, v tomto případě se také hovoří o "*coinswapu*", nebo mezi různými kryptoměnami. Historicky byly závislé na "Hash Time-Locked Contracts" (HTLC), systému časového zámku, který zaručuje dokončení nebo úplné zrušení výměny, čímž zachovává integritu fondů zúčastněných stran. Tato metoda vyžadovala protokoly schopné zpracovávat jak skripty, tak časové zámky. Nicméně v posledních letech se trend posunul směrem k používání *Adaptor Signatures*. Tento druhý přístup má výhodu v eliminaci potřeby skriptů, čímž snižuje provozní náklady. Další hlavní výhodou je, že nevyžaduje použití identického hashování pro obě části transakce, což pomáhá zabránit odhalení spojení mezi nimi.