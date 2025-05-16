---
term: FOFOCAS
---

O Gossip é um algoritmo distribuído peer-to-peer (P2P) para disseminar informação de forma epidémica a todos os agentes da rede. Para Bitcoin, Lightning e outros sistemas distribuídos, este protocolo permite que o Global State dos nós seja trocado e sincronizado em apenas alguns ciclos. Cada nó propaga a informação a um ou mais vizinhos aleatórios ou não aleatórios, que por sua vez propagam a informação a outros vizinhos, e assim sucessivamente, até se atingir um estado globalmente sincronizado.


No Lightning, o gossip é um protocolo de comunicação entre nós para partilhar informações sobre o estado atual e a topologia da rede. O protocolo gossip permite que os nós conheçam o estado dinâmico dos canais de pagamento e de outros nós, para facilitar o encaminhamento de transacções através da rede sem exigir ligações diretas entre todos os nós.


> ► *Em francês, "gossip protocol" poderia ser traduzido como "protocole de bavardage". Fonte : https://dl.acm.org/doi/pdf/10.1145/41840.41841.*