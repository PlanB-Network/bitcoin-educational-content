---
term: SPV NODE (LIGHT NODE)
---

Um nó SPV (*Simple Payment Verification*), às vezes chamado de "nó leve", é um cliente leve de um nó Bitcoin que permite aos usuários validar transações sem a necessidade de armazenar toda a blockchain. Em vez disso, um nó SPV armazena apenas os cabeçalhos de blocos e obtém informações sobre transações específicas consultando nós completos quando necessário. Esse princípio de verificação é possibilitado pela estrutura das transações nos blocos Bitcoin, que são organizadas dentro de um acumulador criptográfico (Árvore de Merkle).

Essa abordagem é vantajosa para dispositivos com recursos limitados, como telefones móveis. No entanto, os nós SPV dependem dos nós completos para a disponibilidade de informações, o que implica um nível adicional de confiança e, consequentemente, menos segurança em comparação com os nós completos. Os nós SPV não podem validar transações autonomamente, mas podem verificar se uma transação está incluída em um bloco consultando provas de Merkle.