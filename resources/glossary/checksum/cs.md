---
term: CHECKSUM
---

Checksum je vypočítaná hodnota z určité sady dat, používaná k ověření integrity a platnosti těchto dat během jejich přenosu nebo ukládání. Algoritmy pro výpočet checksumu jsou navrženy tak, aby detekovaly náhodné chyby nebo nezamýšlené změny dat, jako jsou chyby při přenosu nebo poškození souborů. Existují různé typy algoritmů pro výpočet checksumu, jako jsou kontrolní součty parit, modulární checksumy, kryptografické hašovací funkce nebo BCH kódy (*Bose, Ray-Chaudhuri a Hocquenghem*).

V Bitcoinu se checksumy používají na aplikační úrovni k zajištění integrity přijímacích adres. Checksum je vypočítán z nákladu adresy uživatele, poté je přidán k této adrese, aby se detekovaly možné chyby při jejím zadávání. Checksum je také přítomen v obnovovacích frázích (mnemonických).

> ► *Anglický překlad "somme de contrôle" je "checksum". Je obecně přijímáno, že se termín "checksum" přímo používá ve francouzštině.*