---
term: VERIFICAÇÃO DE PAGAMENTOS SIMPLIFICADA

---
Método que permite a clientes leves verificar transacções Bitcoin sem descarregar toda a cadeia de blocos. Um nó que usa SPV descarrega apenas os cabeçalhos dos blocos, que são muito mais leves do que os blocos completos. Quando precisa de verificar uma transação, o nó SPV solicita uma prova de Merkle aos nós completos para confirmar que a transação está incluída num bloco específico. Esta abordagem é eficiente para dispositivos com recursos limitados, como os smartphones, mas implica uma dependência dos nós completos, o que pode reduzir a segurança e aumentar a confiança necessária.

> ► *O acrónimo "SPV" é frequentemente utilizado para designar este método.*