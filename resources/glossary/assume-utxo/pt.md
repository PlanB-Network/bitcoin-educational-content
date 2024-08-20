---
term: ASSUME UTXO
---

Um parâmetro de configuração no principal cliente Bitcoin Core que permite a um nó que acabou de ser inicializado (mas ainda não passou pelo IBD) adiar a verificação de transações e o conjunto UTXO até um snapshot dado. O conceito depende do uso de um conjunto UTXO (uma lista de todos os UTXOs existentes em um determinado momento) fornecido pelo Core e presumido como preciso, o que permite que o nó seja sincronizado muito rapidamente com a cadeia com o maior trabalho acumulado. Uma vez que o nó pula a etapa longa do IBD, ele se torna operacional para seu usuário muito rapidamente. Assume UTXO divide a sincronização (IBD) em duas partes:
* Primeiro, o nó realiza a Sincronização Primeiro dos Cabeçalhos (verificação apenas dos cabeçalhos) e considera o conjunto UTXO fornecido pelo Core como válido;
* Então, uma vez que está operacional, o nó verificará o histórico completo do bloco em segundo plano, atualizando um novo conjunto UTXO que ele mesmo verificou. Se este novo conjunto UTXO não corresponder ao fornecido pelo Core, ele produzirá uma mensagem de erro.

Portanto, Assume UTXO acelera a preparação de um novo nó Bitcoin adiando o processo de verificação de transações e o conjunto UTXO por meio de um snapshot atualizado fornecido no Core.