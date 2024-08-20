---
term: OP_CAT (0X7E)
---

Permite a concatenação dos dois elementos mais acima na pilha (ou seja, unindo-os de ponta a ponta). Este opcode foi desativado, tornando atualmente impossível seu uso. No entanto, recentemente voltou a receber atenção. Alguns desejam adicioná-lo ao Tapscript para possibilitar a combinação de objetos na pilha, aumentando assim a expressividade desta linguagem. Esta simples ferramenta adicional poderia permitir:
* O uso de assinaturas Lamport, que presumivelmente são resistentes a ataques quânticos;
* A implementação de Vaults;
* O uso de covenants;
* Ou até mesmo, o uso de contratos de não-equivocação.