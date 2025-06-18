---
term: SELFISH Mining
---

Strategie (nebo útok) v Mining, kdy těžař Miner nebo skupina těžařů záměrně zadržuje bloky s platným Proof of Work, aniž by je okamžitě uvolnil do sítě. Cílem je udržet si náskok před ostatními těžaři, pokud jde o Proof of Work, což jim potenciálně umožní Miner několik bloků za sebou a zveřejnit je všechny najednou, čímž maximalizují svůj zisk. Jinými slovy, útočící skupina těžařů netěží na posledním bloku validovaném celou sítí, ale na bloku, který sama vytvořila a který se liší od bloku validovaného sítí.


Tento proces vytváří jakousi tajnou větev Blockchain, která zůstává celé síti neznámá, dokud tento alternativní řetězec potenciálně nepřekročí poctivý Blockchain. Jakmile se tajný řetězec útočících těžařů stane delším (tj. obsahuje více nashromážděné práce) než poctivý, veřejný řetězec, je následně vysílán do celé sítě. V tomto okamžiku se uzly v síti, které sledují nejdelší řetězec (s největším množstvím nahromaděné práce), synchronizují s tímto novým řetězcem. Dochází tedy k reorganizaci.


Sobectví Mining je pro uživatele nepříjemné, protože snižuje bezpečnost systému tím, že plýtvá částí výpočetního výkonu sítě. Pokud je úspěšná, vede také k reorganizaci Blockchain, což ovlivňuje spolehlivost potvrzení transakcí pro uživatele. Přesto tato praxe zůstává pro útočící skupinu těžařů riskantní, protože je často výhodnější Miner normálně nad posledním veřejně známým blokem, než alokovat výpočetní výkon tajné větvi, která pravděpodobně nikdy nepřekročí poctivý Blockchain. Čím větší je počet bloků v reorganizaci, tím menší je pravděpodobnost úspěšného útoku.