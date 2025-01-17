---
term: SELFISH MINING

---
Strategie (nebo útok) při těžbě, kdy těžař nebo skupina těžařů záměrně uchovává bloky s platným důkazem práce, aniž by je okamžitě odeslal do sítě. Cílem je udržet si náskok před ostatními těžaři, pokud jde o důkaz práce, což jim potenciálně umožňuje vytěžit několik bloků za sebou a zveřejnit je všechny najednou, čímž maximalizují svůj zisk.

Jinými slovy, útočící skupina těžařů netěží na posledním bloku potvrzeném celou sítí, ale na bloku, který sama vytvořila a který se liší od bloku potvrzeného sítí. Tímto procesem vzniká jakýsi tajný fork blockchainu, který zůstává celé síti neznámý, dokud tento alternativní řetězec potenciálně nepřekoná poctivý blockchain. Jakmile se tajný řetězec útočících těžařů stane delším (tj. obsahuje více nahromaděné práce) než poctivý a veřejný řetězec, je následně vysílán do celé sítě. V tu chvíli se uzly sítě, které sledují nejdelší řetězec (s nejvíce nahromaděné práce), synchronizují s tímto novým řetězcem. Tím dojde k reorganizaci.

Sobecká těžba je problematická, protože snižuje bezpečnost systému tím, že plýtvá částí výpočetního výkonu sítě. Pokud je úspěšná, vede také k reorganizaci blockchainu, čímž ovlivňuje spolehlivost potvrzení transakcí pro uživatele. Tato praxe zůstává pro útočící skupinu těžařů riziková, protože je často výhodnější normálně těžit na posledním veřejně známém bloku než alokovat výpočetní výkon na tajný fork, který pravděpodobně nikdy nepřekoná poctivý blockchain. Čím větší je počet bloků v reorganizaci, tím menší je pravděpodobnost úspěchu útoku.

> ► Český překlad "minage égoïste" je "sobecké dolování". Všimněte si, že sobecký útok na těžbu by neměl být zaměňován s útokem na zadržování bloků*