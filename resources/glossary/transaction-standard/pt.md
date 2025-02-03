---
term: NORMA DE TRANSACÇÃO

---
Uma transação Bitcoin que, além de aderir às regras de consenso, também se enquadra nas regras de padronização definidas por padrão nos nós do Bitcoin Core. Estas regras de normalização são impostas individualmente por cada nó Bitcoin, para além das regras de consenso, para definir a estrutura das transacções não confirmadas que aceita no seu mempool e transmite aos seus pares.

Estas regras são assim configuradas e executadas localmente por cada nó e podem variar de um nó para outro. Aplicam-se exclusivamente a transacções não confirmadas. Assim, um nó só aceitará uma transação que considere não normalizada se esta já estiver incluída num bloco válido.

Nota-se que a maioria dos nós deixa as configurações padrão conforme estabelecido no Bitcoin Core, criando assim uma uniformidade de regras de padronização em toda a rede. Uma transação que, embora esteja em conformidade com as regras de consenso, não respeite essas regras de padronização, terá dificuldade de se propagar pela rede. No entanto, pode ainda ser incluída num bloco válido se chegar a um mineiro. Na prática, estas transacções, qualificadas como não padronizadas, são frequentemente transmitidas diretamente a um mineiro através de meios externos à rede Bitcoin peer-to-peer. Esta é frequentemente a única forma de confirmar uma transação deste tipo. Por exemplo, uma transação que não aloca nenhuma taxa é válida de acordo com as regras de consenso e não-padrão, porque a política padrão do Bitcoin Core para o parâmetro `minRelayTxFee` é `0.00001` (em BTC/kB).