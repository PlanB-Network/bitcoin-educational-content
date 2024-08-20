---
term: RECURSIVE (COVENANT)
---

Um covenant recursivo no Bitcoin é um tipo de contrato inteligente que impõe condições não apenas na transação atual, mas também em futuras transações que gastam as saídas desta transação. Isso permite a criação de cadeias de transações onde cada uma deve aderir a certas regras definidas pela primeira na cadeia. A recursividade cria uma sequência de transações onde cada uma herda as restrições de sua transação pai. Isso possibilitaria um controle complexo e de longo prazo sobre como os bitcoins podem ser gastos, mas também introduziria riscos em relação à liberdade de gasto e fungibilidade.

Para resumir, um covenant não recursivo limitaria-se apenas à transação que segue imediatamente aquela que estabeleceu as regras. Por outro lado, um covenant recursivo tem a capacidade de impor condições específicas a um bitcoin indefinidamente. As transações podem seguir umas às outras, mas o bitcoin em questão sempre reterá as condições iniciais a ele atreladas. Tecnicamente, o estabelecimento de um covenant não recursivo ocorre quando o `scriptPubKey` de um UTXO define restrições sobre o `scriptPubKey` das saídas de uma transação que gasta dito UTXO. Por outro lado, o estabelecimento de um covenant recursivo ocorre quando o `scriptPubKey` de um UTXO define restrições sobre o `scriptPubKey` das saídas de uma transação que gasta dito UTXO, e sobre todos os `scriptPubKey`s que seguirão o gasto deste UTXO.

De forma mais geral, em computação, o que se chama de "recursividade" é a capacidade de uma função chamar a si mesma, criando uma espécie de laço.