---
term: EXTRA-Nonce
---

Pole používané v `scriptSig` bloku Coinbase Transaction, které umožňuje testovat větší počet možností, aby byl Hash nižší než cílová obtížnost, kromě klasického Nonce, který se nachází přímo v záhlaví každého bloku.


Modifikací extra-Nonce v Coinbase Transaction se změní identifikátor této transakce, a tedy i Merkle Root všech transakcí v bloku, čímž se změní i záhlaví bloku. To umožňuje Miner pokračovat v hledání hashů, když je rozsah klasického Nonce již vyčerpán, aniž by se změnila struktura jeho kandidátního bloku.


V poolech Mining se extra-Nonce často dělí na dvě části: jedna je generována poolem pro identifikaci každého vrtulníku a druhá je modifikována vrtulníkem při hledání platného podílu. To umožňuje různým chopperům v poolu pracovat současně na stejném kandidátském bloku s celým rozsahem nonces, aniž by se stejná práce na úrovni poolu duplikovala.