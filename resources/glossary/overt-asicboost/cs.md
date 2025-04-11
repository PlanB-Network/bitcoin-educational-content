---
term: OVERT ASICBOOST

---
Otevřená a transparentní verze aplikace AsicBoost. AsicBoost je algoritmická optimalizační technika používaná při těžbě bitcoinů. Těžaři používající otevřenou verzi manipulují s polem `nVersion` kandidátského bloku a tuto modifikaci používají jako dodatečnou nonce. Tato metoda ponechává skutečné pole `Nonce` bloku během každého pokusu o hašování beze změny, čímž snižuje počet výpočtů potřebných pro každý pokus o SHA256 tím, že některá data zůstávají mezi pokusy stejná. Tato verze je veřejně zjistitelná a na rozdíl od skryté verze AsicBoost neskrývá své modifikace před zbytkem sítě.