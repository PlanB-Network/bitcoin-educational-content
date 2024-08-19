---
termine: P2MS
---

P2MS sta per *Pay to Multisig*, che si traduce in "pagare a più firme". È un modello di script standard utilizzato per stabilire condizioni di spesa su un UTXO. Permette di bloccare bitcoin con più chiavi pubbliche. Per spendere questi bitcoin, è richiesta una firma con un numero predefinito di chiavi private associate. Ad esempio, un `P2MS 2/3` coinvolge `3` chiavi pubbliche con `3` chiavi private segrete associate. Per spendere i bitcoin bloccati con questo script P2MS, è necessaria una firma con almeno `2` delle `3` chiavi private. Questo è un sistema di sicurezza basato su soglia.

Questo script è stato inventato nel 2011 da Gavin Andresen quando ha preso in carico la manutenzione del client Bitcoin principale. Oggi, P2MS è utilizzato solo marginalmente da alcune applicazioni. La stragrande maggioranza delle moderne multisignature utilizza altri script come P2SH o P2WSH. Rispetto a questi, P2MS è estremamente semplice. Le chiavi pubbliche di cui è composto sono rivelate al momento della ricezione della transazione. Utilizzare un P2MS è anche più costoso rispetto ad altri script multisignature.

> ► *I P2MS sono spesso chiamati "bare-multisig", che potrebbe essere tradotto come "multifirma nuda" o "multifirma grezza". All'inizio del 2023, gli script P2MS sono stati al centro di una controversia a causa del loro uso improprio all'interno del protocollo Stamps. Il loro impatto sul set UTXO è stato notevolmente evidenziato.*