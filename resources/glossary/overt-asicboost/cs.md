---
term: OVERT ASICBOOST
---

Otevřená a transparentní verze AsicBoost. AsicBoost je algoritmická optimalizační technika používaná při těžbě Bitcoinu. Těžaři používající verzi Overt manipulují s polem `nVersion` kandidátního bloku a tuto modifikaci používají jako dodatečný nonce. Tato metoda nechává skutečné pole `Nonce` bloku nezměněné při každém pokusu o hashování, čímž snižuje potřebné výpočty pro každý SHA256 tím, že udržuje některá data stejná mezi pokusy. Tato verze je veřejně detekovatelná a na rozdíl od skryté verze AsicBoost neukrývá své modifikace před zbytkem sítě.