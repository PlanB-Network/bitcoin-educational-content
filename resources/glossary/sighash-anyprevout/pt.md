---
term: SIGHASH_ANYPREVOUT

---
Proposta para a implementação de um novo modificador SigHash Flag no Bitcoin, introduzido com o BIP118. o `SIGHASH_ANYPREVOUT` permite maior flexibilidade no gerenciamento de transações, especialmente para aplicações avançadas como canais de pagamento na Lightning Network e a atualização do Eltoo. O `SIGHASH_ANYPREVOUT` permite que a assinatura não seja vinculada a nenhum UTXO (*Any Previous Output*) anterior específico. Utilizada em combinação com `SIGHASH_ALL`, permitiria assinar todas as saídas de uma transação, mas nenhuma das entradas. Isso permitiria a reutilização da assinatura para diferentes transações, desde que certas condições especificadas sejam atendidas.

> ► *Este modificador SigHash SIGHASH_ANYPREVOUT deriva da ideia de SIGHASH_NOINPUT inicialmente proposta por Joseph Poon em 2016 para melhorar o seu conceito da Lightning Network*