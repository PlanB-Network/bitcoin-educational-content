---
term: OP_CHECKHASHVERIFY (CHV)

definition: Opcode proposto em 2012 para funcionalidades semelhantes ao P2SH, nunca implementado.
---
Um novo opcode proposto em 2012 no BIP17 por Luke Dashjr que ofereceria as mesmas funcionalidades do `OP_EVAL` ou P2SH. O objetivo era fazer o hash do final do `scriptSig`, comparar o resultado com o topo da pilha e tornar a transação inválida se os dois hashes não coincidissem. Este opcode nunca foi implementado.