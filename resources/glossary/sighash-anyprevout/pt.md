---
termo: SIGHASH_ANYPREVOUT
---

Proposta para a implementação de um novo modificador de Flag SigHash no Bitcoin, introduzido com o BIP118. `SIGHASH_ANYPREVOUT` permite uma maior flexibilidade na gestão de transações, especialmente para aplicações avançadas como canais de pagamento na Lightning Network e a atualização Eltoo. O `SIGHASH_ANYPREVOUT` possibilita que a assinatura não fique atrelada a nenhum UTXO anterior específico (*Qualquer Saída Anterior*). Usado em combinação com `SIGHASH_ALL`, permitiria assinar todas as saídas de uma transação, mas nenhuma das entradas. Isso possibilitaria a reutilização da assinatura para diferentes transações, desde que certas condições especificadas sejam atendidas.

> ► *Este modificador SigHash SIGHASH_ANYPREVOUT é derivado da ideia de SIGHASH_NOINPUT inicialmente proposta por Joseph Poon em 2016 para aprimorar seu conceito da Lightning Network.*