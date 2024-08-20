---
termo: BIP61
---

Introduziu uma mensagem de rejeição no protocolo de comunicação entre nós. O objetivo do BIP61 é adicionar um mecanismo de feedback quando um nó recebe uma transação ou um bloco de outro nó que considera inválido. Essa mensagem de rejeição permitiria a um nó sinalizar ao remetente o motivo pelo qual foi rejeitado. Esse tipo de comunicação tinha como intenção melhorar a interoperabilidade entre diferentes clientes e a comunicação entre nós completos e clientes SPV. As funcionalidades trazidas pelo BIP61 foram eventualmente abandonadas a partir da versão 0.20.0 do Bitcoin Core, pois foram consideradas desnecessárias enquanto envolviam um aumento nas necessidades de largura de banda.