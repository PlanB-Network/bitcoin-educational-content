---
term: NÓS DE SEMENTE

---
Lista estática de nós Bitcoin públicos, integrada diretamente no código fonte do Bitcoin Core (`bitcoin/src/chainparamsseeds.h`). Esta lista serve como pontos de conexão para novos nós Bitcoin que se juntam à rede, mas só é usada se as sementes DNS não fornecerem uma resposta dentro de 60 segundos de sua solicitação. Nesse caso, o novo nó Bitcoin se conectará a esses nós sementes para estabelecer uma primeira conexão com a rede e solicitar endereços IP de outros nós. O objetivo final é adquirir a informação necessária para realizar o Initial Block Download (IBD) e sincronizar com a cadeia que tem mais trabalho acumulado. A lista de seed nodes inclui cerca de 1000 nós, identificados de acordo com o padrão estabelecido pelo BIP155. Assim, os seed nodes representam o terceiro método de conexão à rede para um nó Bitcoin, após o possível uso do arquivo `peers.dat`, criado pelo próprio nó, e a solicitação de DNS seeds.

> ► *Nota: os nós de semente não devem ser confundidos com "sementes DNS", que são o segundo método de estabelecimento de ligações