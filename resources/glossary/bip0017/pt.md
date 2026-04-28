---
term: BIP0017

definition: Proposta alternativa ao P2SH introduzindo o opcode OP_CHECKHASHVERIFY, finalmente não adotada em favor do BIP16.
---
Proposta de Luke Dashjr que concorreu com o BIP12 e o BIP16. O BIP17 introduziu um novo opcode, `OP_CHECKHASHVERIFY`, concebido para permitir a verificação de um script presente no `scriptSig` em relação ao seu hash presente no `scriptPubKey` antes de desbloquear os fundos. O BIP16 (P2SH) acabou por ser preferido ao BIP17 (CHV) após um período de intensos debates.