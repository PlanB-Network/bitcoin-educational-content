---
term: SELFISH MINING
---

Strategie (nebo útok) při těžbě, kdy těžař nebo skupina těžařů úmyslně zadržuje bloky s platným důkazem práce bez jejich okamžitého vysílání do sítě. Cílem je udržet náskok před ostatními těžaři z hlediska důkazu práce, což jim potenciálně umožňuje těžit několik bloků v řadě a publikovat je všechny najednou, čímž maximalizují své zisky.

Jinými slovy, útočící skupina těžařů netěží na posledním bloku ověřeném celou sítí, ale na bloku, který si sami vytvořili, a který se liší od toho, který ověřila síť. Tento proces generuje jakýsi tajný fork blockchainu, který zůstává neznámý pro celou síť, dokud tato alternativní řetězec potenciálně nepřekoná čestný blockchain. Jakmile se tajný řetězec útočících těžařů stane delším (tj. obsahuje více nahromaděné práce) než čestný a veřejný řetězec, je poté vysílán do celé sítě. V tom okamžiku uzly sítě, které následují nejdelší řetězec (s největším množstvím nahromaděné práce), se synchronizují s tímto novým řetězcem. To vede k reorganizaci.

Selfish mining je problematický, protože snižuje bezpečnost systému tím, že plýtvá částí výpočetního výkonu sítě. Pokud je úspěšný, vede také k reorganizacím blockchainu, čímž ovlivňuje spolehlivost potvrzení transakcí pro uživatele. Tato praxe zůstává pro útočící skupinu těžařů riskantní, jelikož je často ziskovější těžit normálně na posledním bloku veřejně známém, než alokovat výpočetní výkon na tajný fork, který pravděpodobně nikdy nepřekoná čestný blockchain. Čím větší je počet bloků v reorganizaci, tím nižší je pravděpodobnost úspěchu útoku.

> ► *Anglický překlad "minage égoïste" je "selfish mining". Poznámka, útok selfish mining by neměl být zaměňován s útokem na zadržování bloků.*