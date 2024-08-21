---
term: UTREEXO
---

Protokol navržený Tadge Dryjou pro kompaktní zpracování UTXO setu Bitcoinových uzlů pomocí akumulátoru založeného na Merkleových stromech. Na rozdíl od klasického UTXO setu, který vyžaduje významný úložný prostor, Utreexo drasticky snižuje potřebnou paměť tím, že uchovává pouze kořeny Merkleova stromu. To umožňuje uzlu ověřit existenci UTXO použitých ve vstupu transakce, aniž by musel uchovávat kompletní set UTXO. Použitím Utreexo si každý uzel uchovává pouze kryptografický otisk nazývaný Merkleův kořen. Když je provedena transakce, uživatel poskytne důkazy o vlastnictví UTXO a příslušné Merkleovy cesty. Uzel tak může ověřit transakce bez uchovávání celého setu UTXO. Pojďme si na příkladu s diagramem vysvětlit tento mechanismus:

![](../../dictionnaire/assets/15.png)

V tomto příkladu jsem záměrně zredukoval UTXO set na 4 UTXO, aby bylo pochopení usnadněno. Ve skutečnosti je důležité si představit, že v době psaní těchto řádků existuje na Bitcoinu téměř 140 milionů UTXO. V tomto diagramu by Utreexo uzel potřeboval uchovávat pouze Merkleův kořen v RAM. Pokud obdrží transakci, která utratí UTXO č. 3 (černě), důkaz by se skládal z následujících prvků:
* UTXO 3;
* HASH 4;
* HASH 1-2.

S těmito informacemi předanými odesílatelem transakce Utreexo uzel provede následující ověření:
* Vypočítá otisk UTXO 3, čímž získá HASH 3;
* Spojí HASH 3 s HASH 4;
* Vypočítá jejich otisk, čímž získá HASH 3-4;
* Spojí HASH 3-4 s HASH 1-2;
* Vypočítá jejich otisk, čímž získá Merkleův kořen.

Pokud je Merkleův kořen, který získá tímto procesem, stejný jako Merkleův kořen, který si uchovával v RAM, je přesvědčen, že UTXO č. 3 je skutečně součástí UTXO setu.
Tato metoda snižuje požadavky na RAM pro operátory plných uzlů. Utreexo však má omezení, včetně zvýšení velikosti bloku kvůli dodatečným důkazům a potenciální závislosti uzlů Utreexo na Bridge Nodes pro získání chybějících důkazů. Bridge Nodes jsou tradiční plné uzly, které poskytují nezbytné důkazy uzlům Utreexo, čímž umožňují plné ověření. Tento přístup nabízí kompromis mezi efektivitou a decentralizací, čímž činí ověřování transakcí dostupnějšími pro uživatele s omezenými zdroji.