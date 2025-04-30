---
term: CHECKSUM
---

Kontrolní součet je hodnota vypočtená ze souboru dat, která se používá k ověření integrity a platnosti těchto dat při přenosu nebo ukládání. Algoritmy kontrolních součtů jsou určeny k odhalování náhodných chyb nebo neúmyslných změn dat, jako jsou chyby při přenosu nebo poškození souboru. Existují různé typy algoritmů kontrolních součtů, například paritní kontroly, modulární kontrolní součty, kryptografické funkce Hash nebo kódy BCH (*Bose, Ray-Chaudhuri a Hocquenghem*).


V systému Bitcoin se kontrolní součty používají na úrovni aplikace k zajištění integrity přijímacích adres. Kontrolní součet se vypočítá z užitečného zatížení uživatelské adresy Address a poté se přidá k této adrese Address, aby se zjistily případné chyby na vstupu. Kontrolní součet je také přítomen ve frázích pro obnovení (mnemotechnice).


> ►Všeobecně je přijato používat anglický termín "checksum" přímo ve francouzštině.*