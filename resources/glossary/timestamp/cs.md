---
term: HORODATAGE
---

Časové razítko, anglicky "Timestamp", je mechanismus pro přiřazení přesné časové značky k události, datům nebo zprávě. V obecném kontextu počítačových systémů se časová značka používá k určení chronologického pořadí operací a k ověření integrity dat v čase.


V konkrétním případě Bitcoin se k určení chronologie transakcí a bloků používají časové značky. Každý blok v Blockchain obsahuje Timestamp, který udává přibližný čas jeho vytvoření. Ve své Bílé knize Satoshi Nakamoto dokonce hovoří o "serveru Timestamp", aby popsal to, co bychom dnes nazvali "Blockchain". Úkolem časových značek na Bitcoin je určit chronologii transakcí, aby bylo možné bez zásahu centrální autority určit, která transakce přišla jako první. Tento mechanismus umožňuje každému uživateli ověřit neexistenci transakce v minulosti, a tím zabránit zlomyslnému uživateli v provedení dvojího výdaje. Tento mechanismus zdůvodnil Satoshi Nakamoto ve své Bílé knize slavnou větou: " *Tento standard je založen na unixovém čase, který představuje celkový počet sekund uplynulých od 1. ledna 1970.


> ► *Časové značky bloků jsou u Bitcoin poměrně flexibilní, protože aby byl blok Timestamp považován za platný, musí být jednoduše větší než medián času 11 předcházejících bloků (MTP) a menší než medián časů vrácených uzly (čas upravený sítí) plus 2 hodiny.*