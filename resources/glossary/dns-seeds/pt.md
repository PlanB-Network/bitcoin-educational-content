---
termo: DNS SEEDS
---

Pontos de conexão iniciais para novos nós de Bitcoin que se juntam à rede. Essas sementes, que são na verdade servidores DNS específicos, têm seu endereço permanentemente embutido no código do Bitcoin Core. Quando um novo nó é iniciado, ele contata esses servidores para obter uma lista aleatória de endereços IP de nós de Bitcoin presumivelmente ativos. O novo nó pode então estabelecer conexões com os nós nesta lista para obter as informações necessárias para realizar seu Download Inicial de Bloco (IBD) e sincronizar com a cadeia que tem o trabalho mais acumulado. A partir de 2024, aqui está a lista de sementes DNS do Bitcoin Core e os indivíduos responsáveis por sua manutenção (https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp):
* seed.bitcoin.sipa.be: Pieter Wuille;
* dnsseed.bluematt.me: Matt Corallo;
* dnsseed.bitcoin.dashjr-list-of-p2p-nodes.us: Luke Dashjr;
* seed.bitcoinstats.com: Christian Decker;
* seed.bitcoin.jonasschnelli.ch: Jonas Schnelli;
* seed.btc.petertodd.net: Peter Todd;
* seed.bitcoin.sprovoost.nl: Sjors Provoost;
* dnsseed.emzy.de: Stephan Oeste;
* seed.bitcoin.wiz.biz: Jason Maurice;
* seed.mainnet.achownodes.xyz: Ava Chow.

DNS seeds são o segundo método, em ordem de prioridade, para um nó de Bitcoin estabelecer conexões. O primeiro método envolve usar o arquivo peers.dat que o próprio nó criou. Este arquivo está naturalmente vazio no caso de um novo nó, a menos que o usuário tenha modificado manualmente.

> ► *Nota, DNS seeds não devem ser confundidos com "nós semente", que são a terceira maneira de estabelecer conexões.*