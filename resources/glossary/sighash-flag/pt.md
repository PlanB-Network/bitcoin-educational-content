---
term: SIGHASH FLAG
---

Um parâmetro em uma transação Bitcoin que determina quais componentes de uma transação (entradas e saídas) são cobertos pela assinatura associada, tornando-os imutáveis. O SigHash Flag é um byte adicionado à assinatura digital de cada entrada. Portanto, a escolha do SigHash Flag afeta diretamente quais partes da transação são congeladas pela assinatura e quais ainda podem ser modificadas posteriormente. Esse mecanismo garante que as assinaturas comprometam os dados da transação de maneira precisa e segura, de acordo com a intenção do assinante. Existem três principais SigHash Flags:

- `SIGHASH_ALL` (`0x01`): A assinatura aplica-se a todas as entradas e saídas da transação, bloqueando-as inteiramente;

- `SIGHASH_NONE` (`0x02`): A assinatura aplica-se a todas as entradas, mas a nenhuma das saídas, permitindo que as saídas sejam modificadas após a assinatura;

- `SIGHASH_SINGLE` (`0x03`): A assinatura cobre todas as entradas e apenas uma saída correspondente ao índice da entrada assinada.

Além desses três SigHash Flags, o modificador `SIGHASH_ANYONECANPAY` (`0x80`) pode ser combinado com cada um dos tipos anteriores. Quando esse modificador é usado, apenas uma parte das entradas é assinada, deixando as outras abertas para modificação. Aqui estão as combinações existentes com o modificador:

- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): A assinatura aplica-se a uma única entrada, cobrindo todas as saídas da transação;

- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): A assinatura cobre uma única entrada, sem se comprometer com nenhuma saída;

- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): A assinatura aplica-se a uma única entrada e apenas à saída que tem o mesmo índice que esta entrada.

> ► *Um sinônimo às vezes usado para "SigHash" é "Tipos de Hash de Assinatura".*