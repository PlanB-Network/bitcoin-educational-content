---
term: SIGHASH FLAG

---
Um parâmetro em uma transação Bitcoin que determina quais componentes de uma transação (entradas e saídas) são cobertos pela assinatura associada, tornando-se assim imutáveis. O SigHash Flag é um byte adicionado à assinatura digital de cada entrada. Por conseguinte, a escolha do sinalizador SigHash afecta diretamente as partes da transação que são congeladas pela assinatura e as que podem ser modificadas posteriormente. Este mecanismo garante que as assinaturas confirmam de forma precisa e segura os dados da transação de acordo com a intenção do signatário. Existem três bandeiras SigHash principais:


- `SIGHASH_ALL` (`0x01`): A assinatura aplica-se a todas as entradas e saídas da transação, bloqueando-as completamente;
- `SIGHASH_NONE` (`0x02`): A assinatura aplica-se a todas as entradas mas nenhuma das saídas, permitindo que as saídas sejam modificadas após a assinatura;
- `SIGHASH_SINGLE` (`0x03`): A assinatura cobre todas as entradas e apenas uma saída correspondente ao índice da entrada assinada.

Para além destes três sinalizadores SigHash, o modificador `SIGHASH_ANYONECANPAY` (`0x80`) pode ser combinado com cada um dos tipos anteriores. Quando este modificador é utilizado, apenas uma parte das entradas é assinada, deixando as outras abertas a modificações. Aqui estão as combinações existentes com o modificador:


- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): A assinatura se aplica a uma única entrada, cobrindo todas as saídas da transação;
- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): A assinatura cobre uma única entrada, sem comprometer-se com qualquer saída;
- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): A assinatura aplica-se a uma única entrada e apenas à saída com o mesmo índice que esta entrada.

> ► *Um sinónimo por vezes utilizado para "SigHash" é "Signature Hash Types"