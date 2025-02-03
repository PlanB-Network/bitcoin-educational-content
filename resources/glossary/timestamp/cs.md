---
term: TIMESTAMP

---
Časové razítko, anglicky "timestamping", je mechanismus, který zahrnuje přiřazení přesné časové značky k události, datům nebo zprávě. V obecném kontextu počítačových systémů se časová razítka používají k určení chronologického pořadí operací a k ověření integrity dat v čase.

V konkrétním případě Bitcoinu se časové značky používají k určení chronologie transakcí a bloků. Každý blok v blockchainu obsahuje časové razítko, které udává přibližný okamžik jeho vytvoření. Satoshi Nakamoto ve své Bílé knize dokonce hovoří o "serveru časových razítek", aby popsal to, co bychom dnes nazvali "blockchain" Úkolem časových razítek v Bitcoinu je určit chronologii transakcí, aby bylo možné bez zásahu centrální autority určit, která transakce byla provedena jako první. Tento mechanismus umožňuje každému uživateli ověřit neexistenci transakce v minulosti, a tím zabránit zlomyslnému uživateli provést dvojí útratu. Tento mechanismus zdůvodnil Satoshi Nakamoto ve své Bílé knize slavnou větou: "*Jediný způsob, jak potvrdit neexistenci transakce, je být si vědom všech transakcí*." Tento standard je stanoven na základě unixového času, který představuje celkový počet sekund uplynulých od 1. ledna 1970.

> ► Časové razítko bloku v Bitcoinu je poměrně flexibilní, protože aby bylo časové razítko považováno za platné, musí být jednoduše větší než medián času 11 předchozích bloků (MTP) a menší než medián časů vrácených uzly (čas upravený sítí) plus 2 hodiny.*