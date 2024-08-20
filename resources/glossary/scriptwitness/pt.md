---
term: SCRIPTWITNESS
---

Um elemento nas entradas de transações SegWit que contém as assinaturas e chaves públicas necessárias para desbloquear os bitcoins enviados na transação. Semelhante ao `scriptSig` das transações Legacy, o `scriptWitness`, no entanto, não é colocado na mesma localização. De fato, é essa parte, referida como "testemunha" (`*witness*` em inglês), que é movida para um banco de dados separado a fim de resolver o problema de maleabilidade de transação. Cada entrada SegWit tem seu próprio `scriptWitness`, e todos os elementos `scriptWitness` juntos formam o campo `Witness` da transação.

> ► *Tenha cuidado para não confundir `scriptWitness` com `witnessScript`. Enquanto o `scriptWitness` contém os dados de testemunha para qualquer entrada SegWit, o `witnessScript` define as condições de gasto de um UTXO P2WSH ou P2SH-P2WSH e constitui um script por direito próprio, semelhante ao `redeemScript` para uma saída P2SH.*