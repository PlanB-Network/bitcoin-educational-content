---
term: REGRAS DE NORMALIZAÇÃO

---
As regras de normalização são adoptadas individualmente por cada nó Bitcoin, para além das regras de consenso, para definir a estrutura das transacções não confirmadas que aceita no seu mempool e transmite aos seus pares. Essas regras são, portanto, configuradas e executadas localmente por cada nó e podem variar de um nó para outro. Aplicam-se exclusivamente a transacções não confirmadas. Assim, um nó só aceitará uma transação que considere não normalizada se esta já estiver incluída num bloco válido.

Observa-se que a maioria dos nós deixa as configurações padrão conforme estabelecido no Bitcoin Core, criando assim uma uniformidade de regras de padronização em toda a rede. Uma transação que, embora esteja em conformidade com as regras de consenso, não adere a essas regras de padronização, terá dificuldade em ser transmitida pela rede. No entanto, pode ainda ser incluída num bloco válido se chegar a um mineiro. Na prática, estas transacções, referidas como "não-padrão", são muitas vezes transmitidas diretamente a um mineiro através de meios externos à rede Bitcoin peer-to-peer. Esta é frequentemente a única forma de confirmar este tipo de transação.

Por exemplo, uma transação que não aloca nenhuma taxa é válida de acordo com as regras de consenso e não é padrão porque a política padrão do Bitcoin Core para o parâmetro `minRelayTxFee` é `0.00001` (em BTC/kB).

> ► *A expressão "regras de mempool" é também por vezes utilizada para designar as regras de normalização.*