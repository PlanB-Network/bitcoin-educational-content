---
term: REPLAY ATTACK
---

V kontextu Bitcoin dochází k útoku opakováním, když je platná transakce na jednom Blockchain zákeřně reprodukována na jiném Blockchain, který má stejnou transakční historii. Jinými slovy, transakce vysílaná na jednom kanálu může být replikována na jiném kanálu bez souhlasu odesílatele první transakce.


Vezměme si příklad hypotetického Hard Fork z Bitcoin s názvem "*BitcoinBis*". Pokud provedete platbu v bitcoinech za nákup bagety od pekaře na skutečném Blockchain Bitcoin, tentýž pekař by mohl tuto legitimní transakci přehrát na *BitcoinBis* a získat stejnou částku v kryptoměnách na tomto Fork, aniž by z vaší strany došlo k nějaké akci.


K tomuto typu útoku může dojít pouze v případě větvení Blockchain se dvěma nezávislými řetězci, které přetrvávají v čase. Typicky se jedná o případ Hard Fork. Aby byl útok replay možný, musí mít 2 blockchainy společnou historii a duplikovaná transakce musí jako vstupy spotřebovávat UTXO vytvořené z předchozích transakcí, které proběhly před rozdělením obou řetězců, nebo z předchozích transakcí, které již samy byly přehrány v předchozím útoku replay.


Obecně lze říci, že v oblasti výpočetní techniky spočívá opakovaný útok v zachycení a opětovném použití platných dat za účelem oklamání systému opakováním původního přenosu. To může někdy vést ke krádeži identity v síti.


> ► *V případě opakovaného útoku na transakci Bitcoin se někdy hovoří jednoduše o "opakované transakci". "*