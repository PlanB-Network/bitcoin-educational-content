---
term: NÓ SPV (NÓ DE LUZ)

---
Um nó SPV (*Simple Payment Verification*), por vezes chamado de "light node", é um cliente leve de um nó Bitcoin que permite aos utilizadores validar transacções sem ter de armazenar toda a blockchain. Em vez disso, um nó SPV armazena apenas os cabeçalhos dos blocos e obtém informações sobre transacções específicas consultando nós completos quando necessário. Este princípio de verificação é possível graças à estrutura das transacções nos blocos Bitcoin, que estão organizados dentro de um acumulador criptográfico (Merkle Tree).

Esta abordagem é vantajosa para dispositivos com recursos limitados, como os telemóveis. No entanto, os nós SPV dependem dos nós completos para a disponibilidade de informações, o que implica um nível adicional de confiança e, consequentemente, menos segurança em comparação com os nós completos. Os nós SPV não podem validar transacções de forma autónoma, mas podem verificar se uma transação está incluída num bloco consultando as provas de Merkle.