---
term: P2MS

---
P2MS è l'acronimo di *Pay to Multisig*, che si traduce in "paga a più firme". È un modello di script standard utilizzato per stabilire le condizioni di spesa su un UTXO. Consente di bloccare i bitcoin con più chiavi pubbliche. Per spendere questi bitcoin, è necessaria una firma con un numero predefinito di chiavi private associate. Ad esempio, un `P2MS 2/3` comporta `3` chiavi pubbliche con `3` chiavi private segrete associate. Per spendere i bitcoin bloccati con questo script P2MS, è necessaria una firma con almeno `2` delle `3` chiavi private. Si tratta di un sistema di sicurezza a soglia.

Questo script è stato inventato nel 2011 da Gavin Andresen quando ha assunto la manutenzione del principale client Bitcoin. Oggi, P2MS è utilizzato solo marginalmente da alcune applicazioni. La stragrande maggioranza delle moderne firme multiple utilizza altri script come P2SH o P2WSH. Rispetto a questi, P2MS è estremamente banale. Le chiavi pubbliche che lo compongono vengono rivelate al momento della ricezione della transazione. L'uso di un P2MS è anche più costoso di altri script di firma multipla.

> *P2MS sono spesso chiamati "bare-multisig", che potrebbe essere tradotto come "multisignature nude" o "multisignature grezze". All'inizio del 2023, gli script P2MS sono stati al centro di una controversia a causa del loro uso improprio all'interno del protocollo Stamps. Il loro impatto sul set UTXO è stato sottolineato in modo particolare.*