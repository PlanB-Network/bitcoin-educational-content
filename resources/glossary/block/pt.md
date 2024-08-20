---
term: BLOCK
---

Estrutura de dados no sistema Bitcoin. Um bloco contém um conjunto de transações válidas e metadados contidos em seu cabeçalho. Cada bloco está ligado ao próximo pelo hash de seu cabeçalho, formando assim a blockchain. A blockchain atua como um servidor de carimbo de tempo que permite a todos os usuários conhecer todas as transações passadas, a fim de verificar a não existência de uma transação e prevenir o gasto duplo. As transações são organizadas em uma árvore de Merkle. Este acumulador criptográfico permite a produção de um resumo de todas as transações em um bloco, chamado de "raiz de Merkle". O cabeçalho de um bloco contém 6 elementos:
* A versão do bloco;
* A impressão do bloco anterior;
* A raiz da árvore de Merkle de transações;
* O carimbo de tempo do bloco;
* O alvo de dificuldade;
* O nonce.

Para que um bloco seja válido, ele deve ter um cabeçalho que, uma vez hasheado com `SHA256d`, produza um resumo que seja menor ou igual ao alvo de dificuldade.