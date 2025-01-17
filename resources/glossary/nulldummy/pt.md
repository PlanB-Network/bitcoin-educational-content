---
term: NULLDUMMY

---
Regra de consenso introduzida com o BIP147 no soft fork SegWit que exige que o elemento fictício usado nos opcodes `OP_CHECKMULTISIG` e `OP_CHECKMULTISIGVERIFY` seja um array de bytes vazio (`OP_0`). Esta medida foi implementada para eliminar um vetor de maleabilidade, proibindo qualquer valor diferente de `OP_0` para este elemento.