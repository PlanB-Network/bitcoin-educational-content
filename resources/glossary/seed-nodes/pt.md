---
termo: NÓS SEMENTE
---

Lista estática de nós públicos do Bitcoin, integrada diretamente no código-fonte do Bitcoin Core (`bitcoin/src/chainparamsseeds.h`). Esta lista serve como pontos de conexão para novos nós do Bitcoin que estão se juntando à rede, mas é utilizada apenas se os DNS seeds não fornecerem uma resposta dentro de 60 segundos de sua solicitação. Neste caso, o novo nó do Bitcoin se conectará a esses nós semente para estabelecer uma primeira conexão com a rede e solicitar endereços IP de outros nós. O objetivo final é adquirir as informações necessárias para realizar o Download Inicial de Bloco (IBD) e sincronizar com a cadeia que tem o maior trabalho acumulado. A lista de nós semente inclui quase 1000 nós, identificados de acordo com o padrão estabelecido pelo BIP155. Assim, os nós semente representam o terceiro método de conexão à rede para um nó do Bitcoin, após o possível uso do arquivo `peers.dat`, criado pelo próprio nó, e a solicitação de DNS seeds.

> ► *Nota, os nós semente não devem ser confundidos com "DNS seeds", que são o segundo método de estabelecimento de conexões.*