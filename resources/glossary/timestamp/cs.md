---
term: TIMESTAMP
---

Časové razítko, nebo "timestamp" v angličtině, je mechanismus, který zahrnuje spojení přesného časového označení s událostí, daty nebo zprávou. V obecném kontextu počítačových systémů se časová razítka používají k určení chronologického pořadí operací a k ověření integrity dat v průběhu času.

Ve specifickém případě Bitcoinu se časová razítka používají k stanovení chronologie transakcí a bloků. Každý blok v blockchainu obsahuje časové razítko, které ukazuje přibližný okamžik jeho vytvoření. Satoshi Nakamoto dokonce hovoří o "timestamp serveru" ve svém White Paperu, aby popsal to, co bychom dnes nazvali "blockchain". Role časového razítkování v Bitcoinu spočívá v určení chronologie transakcí, aby se bez zásahu centrální autority určilo, která transakce přišla první. Tento mechanismus umožňuje každému uživateli ověřit neexistenci transakce v minulosti a tím zabránit zlomyslnému uživateli v provedení dvojitého výdaje. Tento mechanismus je Satoshi Nakamotem v jeho White Paperu odůvodněn slavnou větou: "*Jediný způsob, jak potvrdit neexistenci transakce, je být informován o všech transakcích.*" Tento standard je založen na Unixovém čase, který představuje celkový počet sekund, které uplynuly od 1. ledna 1970.

> ► *Časové razítkování bloků na Bitcoinu je relativně flexibilní, protože aby bylo časové razítko považováno za platné, stačí, když je větší než medián času 11 předcházejících bloků (MTP) a menší než medián časů vrácených uzly (čas upravený podle sítě) plus 2 hodiny.*