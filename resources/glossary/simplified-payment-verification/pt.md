---
term: VERIFICAÇÃO DE PAGAMENTO SIMPLIFICADA
---

Método que permite a clientes leves verificar transações Bitcoin sem baixar o blockchain inteiro. Um nó usando SPV apenas baixa os cabeçalhos dos blocos, que são muito mais leves que os blocos completos. Quando precisa verificar uma transação, o nó SPV solicita uma prova de Merkle dos nós completos para confirmar que a transação está incluída em um bloco específico. Esta abordagem é eficiente para dispositivos com recursos limitados, como smartphones, mas implica uma dependência dos nós completos, o que pode reduzir a segurança e aumentar a confiança necessária.

> ► *A sigla "SPV" é frequentemente usada para se referir a este método.*