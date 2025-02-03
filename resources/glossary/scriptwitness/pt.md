---
term: TESTEMUNHA DE ESCRITA

---
Um elemento nas entradas de transações SegWit que contém as assinaturas e chaves públicas necessárias para desbloquear os bitcoins enviados na transação. Semelhante ao `scriptSig` das transacções Legacy, o `scriptWitness` não é, no entanto, colocado no mesmo local. De facto, é esta parte, referida como a "testemunha" (`*witness*` em inglês), que é movida para uma base de dados separada de forma a resolver o problema da maleabilidade da transação. Cada entrada SegWit tem o seu próprio `scriptWitness`, e todos os elementos `scriptWitness` juntos formam o campo `Witness` da transação.

> ► *Tenha cuidado para não confundir `scriptWitness` com `witnessScript`. Enquanto que o `scriptWitness` contém os dados de testemunho para qualquer entrada SegWit, o `witnessScript` define as condições de gasto de um UTXO P2WSH ou P2SH-P2WSH e constitui um script por direito próprio, semelhante ao `redeemScript` para uma saída P2SH.*