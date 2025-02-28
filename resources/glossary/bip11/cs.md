---
term: BIP11

---
BIP představil Gavin Andresen v březnu 2012, který navrhuje standardní metodu pro vytváření transakcí s více podpisy v Bitcoinu. Cílem tohoto návrhu je zvýšit bezpečnost bitcoinů tím, že k ověření transakce bude vyžadováno více podpisů. BIP11 zavádí nový typ skriptu nazvaný "M-of-N multisig", kde `M` představuje minimální počet požadovaných podpisů z `N` potenciálních veřejných klíčů. Tento standard využívá opkód `OP_CHECKMULTISIG`, který již v Bitcoinu existuje, ale dříve nebyl v souladu se standardizačními pravidly uzlů. Ačkoli se tento typ skriptu již běžně nepoužívá pro skutečné multisig peněženky, upřednostňují se P2SH nebo P2WSH, jeho použití je nadále možné. Používá se zejména v metaprotokolech, jako jsou Stamps. Uzly se však mohou rozhodnout, že tyto transakce P2MS nebudou předávat, a to pomocí parametru `permitbaremultisig=0`.

> ► Dnes je tento standard známý jako "bare-multisig" nebo "P2MS".*