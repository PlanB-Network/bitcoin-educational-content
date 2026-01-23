---
term: Assume utxo

definition: Um parâmetro Bitcoin Core que permite sincronização rápida de um novo nó usando um snapshot do conjunto UTXO presumido válido, antes de verificar o histórico em segundo plano.
---
Parâmetro de configuração no cliente maioritário Bitcoin Core que permite que um nó que acaba de ser inicializado (mas que ainda não realizou o IBD) adie a verificação das transações e do conjunto UTXO antes de um determinado snapshot. O conceito baseia-se na utilização de um conjunto UTXO (lista de todos os UTXOs existentes num determinado momento) fornecido pelo Core e presumivelmente exato, o que permite ao nó sincronizar-se muito rapidamente na cadeia com o maior trabalho acumulado. Uma vez que o nó salta a longa etapa do IBD, torna-se funcional para o seu utilizador muito rapidamente.

Assume UTXO divide a sincronização (IBD) em duas partes: Primeiro, o nó realiza o Header First Sync (apenas verificação de cabeçalhos) e considera válido o conjunto UTXO fornecido pelo Core; Depois, uma vez funcional, o nó verificará o histórico completo de blocos em segundo plano, atualizando um novo conjunto UTXO que ele mesmo terá verificado. Se este último não corresponder ao conjunto UTXO fornecido pelo Core, ele fornecerá uma mensagem de erro.

O Assume UTXO permite, portanto, acelerar a preparação de um novo nó Bitcoin, adiando o processo de verificação das transações e do conjunto UTXO graças a um snapshot atualizado fornecido no Core.





