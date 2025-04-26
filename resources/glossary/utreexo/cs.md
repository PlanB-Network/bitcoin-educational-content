---
term: UTREEXO

---
Protokol navržený Tadgem Dryjou ke zkompaktnění sady UTXO uzlů Bitcoinu pomocí akumulátoru založeného na Merklových stromech. Na rozdíl od klasické sady UTXO, která vyžaduje značný úložný prostor, Utreexo drasticky snižuje potřebu paměti tím, že ukládá pouze kořeny Merkleho stromů. Uzel tak může ověřovat existenci UTXO použitých na vstupech transakcí, aniž by musel uchovávat kompletní sadu UTXO. Při použití nástroje Utreexo si každý uzel uchovává pouze kryptografický otisk zvaný kořen Merkleho. Při provádění transakce uživatel poskytne důkazy o vlastnictví UTXO a příslušných Merkleho cest. Uzel tak může ověřovat transakce, aniž by musel uchovávat celou sadu UTXO. Uveďme si příklad se schématem pro pochopení tohoto mechanismu:

![](../../dictionnaire/assets/15.webp)

V tomto příkladu jsem záměrně omezil sadu UTXO na 4 UTXO, abych usnadnil pochopení. Ve skutečnosti je důležité si představit, že v době psaní těchto řádků je v Bitcoinu téměř 140 milionů UTXO. V tomto schématu by uzel Utreexo potřeboval udržovat v paměti RAM pouze Merkle Root. Pokud by obdržel transakci utrácející UTXO č. 3 (černě), důkaz by se skládal z následujících prvků:


- UTXO 3;
- HASH 4;
- HASH 1-2.

Na základě těchto informací předaných odesílatelem transakce provede uzel Utreexo následující ověření:


- Vypočítá otisk UTXO 3, čímž získá HASH 3;
- Spojuje HASH 3 s HASH 4;
- Vypočítá jejich otisk, čímž získá HASH 3-4;
- Spojuje HASH 3-4 s HASH 1-2;
- Vypočítá jejich otisk, čímž získá Merkleho kořen.

Pokud je Merkleho kořen, který získá svým procesem, stejný jako Merkleho kořen, který má uložený ve své paměti RAM, pak je přesvědčen, že UTXO č. 3 je skutečně součástí souboru UTXO.

Tato metoda snižuje nároky na paměť RAM u operátorů s celým uzlem. Utreexo má však svá omezení, včetně nárůstu velikosti bloku kvůli dodatečným důkazům a potenciální závislosti uzlů Utreexo na mostních uzlech pro získání chybějících důkazů. Mostní uzly jsou tradiční plné uzly, které poskytují potřebné důkazy uzlům Utreexo, a umožňují tak úplné ověření. Tento přístup nabízí kompromis mezi efektivitou a decentralizací, díky čemuž je ověřování transakcí přístupnější uživatelům s omezenými zdroji.