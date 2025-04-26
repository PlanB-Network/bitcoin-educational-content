---
term: ASSUME UTXO

---
Um parâmetro de configuração no cliente líder do Bitcoin Core que permite que um nó que acabou de ser inicializado (mas ainda não passou pelo IBD) adie a verificação de transações e o conjunto UTXO até um determinado snapshot. O conceito baseia-se na utilização de um conjunto UTXO (uma lista de todos os UTXOs existentes num determinado momento) fornecido pelo Core e presumivelmente exato, o que permite que o nó seja rapidamente sincronizado com a cadeia com o trabalho mais acumulado. Uma vez que o nó salta o longo passo de IBD, torna-se operacional para o seu utilizador muito rapidamente. Suponha que o UTXO divide a sincronização (IBD) em duas partes:


- Em primeiro lugar, o nó efectua a primeira sincronização do cabeçalho (verificação apenas dos cabeçalhos) e considera válido o conjunto de UTXO fornecido pelo Core;
- Depois, quando estiver operacional, o nó verificará o histórico completo do bloco em segundo plano, actualizando um novo conjunto UTXO que ele próprio verificou. Se este novo conjunto de UTXOs não corresponder ao fornecido pelo Core, será emitida uma mensagem de erro.

Por conseguinte, Assume que o UTXO acelera a preparação de um novo nó Bitcoin, adiando o processo de verificação da transação e o conjunto UTXO através de um instantâneo atualizado fornecido no Core.