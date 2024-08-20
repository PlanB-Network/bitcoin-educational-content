---
termo: PADRÃO DE TRANSAÇÃO
---

Uma transação Bitcoin que, além de aderir às regras de consenso, também se enquadra nas regras de padronização definidas por padrão nos nós do Bitcoin Core. Essas regras de padronização são impostas individualmente por cada nó do Bitcoin, além das regras de consenso, para definir a estrutura das transações não confirmadas que aceita em seu mempool e transmite aos seus pares.

Essas regras são, portanto, configuradas e executadas localmente por cada nó e podem variar de um nó para outro. Elas se aplicam exclusivamente a transações não confirmadas. Portanto, um nó só aceitará uma transação que considera não padrão se ela já estiver incluída em um bloco válido.

Nota-se que a maioria dos nós deixa as configurações padrão conforme estabelecido no Bitcoin Core, criando assim uma uniformidade das regras de padronização em toda a rede. Uma transação que, embora esteja em conformidade com as regras de consenso, não respeita essas regras de padronização, terá dificuldade em se propagar pela rede. No entanto, ainda pode ser incluída em um bloco válido se alcançar um minerador. Na prática, essas transações, qualificadas como não padrão, são frequentemente transmitidas diretamente a um minerador por meios externos à rede peer-to-peer do Bitcoin. Muitas vezes, essa é a única maneira de confirmar tal transação. Por exemplo, uma transação que não aloca taxas é válida de acordo com as regras de consenso e não padrão, porque a política padrão do Bitcoin Core para o parâmetro `minRelayTxFee` é `0.00001` (em BTC/kB).