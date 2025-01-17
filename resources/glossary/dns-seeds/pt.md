---
term: SEMENTES DE DNS

---
Pontos de conexão inicial para novos nós Bitcoin que se juntam à rede. Essas sementes, que na verdade são servidores DNS específicos, têm seu endereço permanentemente embutido no código do Bitcoin Core. Quando um novo nó inicia, ele contacta esses servidores para obter uma lista aleatória de endereços IP de nós Bitcoin presumivelmente ativos. O novo nó pode então estabelecer ligações com os nós desta lista para obter a informação necessária para efetuar o seu Initial Block Download (IBD) e sincronizar-se com a cadeia que tem mais trabalho acumulado. A partir de 2024, aqui está a lista de sementes de DNS do Bitcoin Core e os indivíduos responsáveis pela sua manutenção (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):


- seed.bitcoin.sipa.be: Pieter Wuille;
- dnsseed.bluematt.me: Matt Corallo;
- dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
- seed.bitcoinstats.com: Christian Decker;
- seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
- seed.btc.petertodd.net: Peter Todd;
- seed.bitcoin.sprovoost.nl: Sjors Provoost;
- dnsseed.emzy.de: Stephan Oeste;
- seed.bitcoin.wiz.biz: Jason Maurice;
- seed.mainnet.achownodes.xyz: Ava Chow.

Sementes DNS são o segundo método, em ordem de prioridade, para um nó Bitcoin estabelecer conexões. O primeiro método envolve o uso do arquivo peers.dat que o próprio nó criou. Este ficheiro está naturalmente vazio no caso de um novo nó, a menos que o utilizador o tenha modificado manualmente.

> ► *Nota: as sementes DNS não devem ser confundidas com os "nós de sementes", que são a terceira forma de estabelecer ligações