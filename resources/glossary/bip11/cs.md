---
term: BIP11
---

BIP představený Gavinem Andresenem v březnu 2012, který navrhuje standardní metodu pro vytváření multisignaturních transakcí na Bitcoinu. Tento návrh má za cíl zvýšit bezpečnost bitcoinů vyžadováním více podpisů pro ověření transakce. BIP11 zavádí nový typ skriptu, nazvaný "M-z-N multisig," kde `M` představuje minimální počet vyžadovaných podpisů z `N` možných veřejných klíčů. Tento standard využívá opcode `OP_CHECKMULTISIG`, který již v Bitcoinu existuje, ale dříve nebyl v souladu s pravidly standardizace uzlů. Ačkoliv tento typ skriptu již není běžně používán pro aktuální multisig peněženky, preferujíc se P2SH nebo P2WSH, jeho použití je stále možné. Je významně používán v meta-protokolech, jako jsou Stamps. Uzly si však mohou vybrat, že tyto P2MS transakce nebudou přeposílat s parametrem `permitbaremultisig=0`.

> ► *V současnosti je tento standard známý jako "bare-multisig" nebo "P2MS".*