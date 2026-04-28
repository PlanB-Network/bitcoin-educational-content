---
term: BIP0031

definition: Introdução da mensagem pong em resposta ao ping para verificar a conectividade entre os nós da rede Bitcoin.
---
Proposta destinada a melhorar os mecanismos de gestão da rede pelos nós Bitcoin. Antes do BIP31, os nós Bitcoin não tinham uma forma direta de saber se os seus pares ainda estavam ligados, operacionais e não sobrecarregados. O BIP31 introduziu a utilização de uma mensagem `pong`, em resposta a uma mensagem `ping`, que permite uma verificação ativa da conetividade entre nós.