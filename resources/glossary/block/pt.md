---
term: BLOCO

---
Estrutura de dados no sistema Bitcoin. Um bloco contém um conjunto de transacções válidas e metadados contidos no seu cabeçalho. Cada bloco está ligado ao seguinte pelo hash do seu cabeçalho, formando assim a blockchain. A cadeia de blocos funciona como um servidor de registo de data e hora que permite a cada utilizador conhecer todas as transacções passadas, a fim de verificar a inexistência de uma transação e evitar gastos duplos. As transacções são organizadas numa árvore de Merkle. Este acumulador criptográfico permite a produção de um resumo de todas as transacções de um bloco, denominado "raiz de Merkle" O cabeçalho de um bloco contém 6 elementos:


- A versão do bloco;
- A marca do bloco anterior;
- A raiz da árvore de Merkle das transacções;
- O carimbo de data/hora do bloco;
- O objetivo de dificuldade;
- O nonce.

Para que um bloco seja válido, ele deve ter um cabeçalho que, uma vez hasheado com `SHA256d`, produza um digest que seja menor ou igual ao alvo de dificuldade.