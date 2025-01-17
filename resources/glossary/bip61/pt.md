---
term: BIP61

---
Introduziu uma mensagem de rejeição no protocolo de comunicação entre nós. O objetivo da BIP61 é acrescentar um mecanismo de feedback quando um nó recebe uma transação ou um bloco de outro nó que considera inválido. Esta mensagem de rejeição permitiria a um nó assinalar ao remetente a razão pela qual a transação foi rejeitada. Este tipo de comunicação tinha por objetivo melhorar a interoperabilidade entre os diferentes clientes e as comunicações entre os nós completos e os clientes SPV. As funcionalidades trazidas pelo BIP61 acabaram por ser abandonadas a partir da versão 0.20.0 do Bitcoin Core, por terem sido consideradas desnecessárias e por implicarem maiores necessidades de largura de banda.