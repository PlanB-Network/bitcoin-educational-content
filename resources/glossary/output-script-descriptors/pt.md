---
term: DESCRITORES DE SCRIPT DE SAÍDA
---

Descritores de script de saída, ou simplesmente descritores, são expressões estruturadas que descrevem completamente um script de saída (`scriptPubKey`) e fornecem todas as informações necessárias para rastrear transações para ou de um script específico. Esses descritores facilitam o gerenciamento de chaves em carteiras HD através de uma descrição padrão da estrutura e tipos de endereços usados.

O principal interesse dos descritores reside na sua capacidade de encapsular todas as informações essenciais para restaurar uma carteira em uma única string (além da frase de recuperação). Ao salvar um descritor com as frases mnemônicas correspondentes, é possível restaurar não apenas as chaves privadas, mas também a estrutura precisa da carteira e os parâmetros de script associados. De fato, recuperar uma carteira requer não apenas o conhecimento da semente inicial, mas também índices específicos para a derivação de pares de chaves filhas, bem como o `xpub` de cada fator no caso de uma carteira multisig. Anteriormente, assumia-se que essa informação era implicitamente conhecida por todos. No entanto, com a diversificação de scripts e o surgimento de configurações mais complexas, essa informação poderia se tornar difícil de extrapolar, transformando esses dados em informações privadas e difíceis de serem forçadas bruscamente. O uso de descritores simplifica muito o processo: basta conhecer a(s) frase(s) de recuperação e o descritor correspondente para restaurar tudo de maneira confiável e segura.

Um descritor consiste em vários elementos:
* Funções de script como `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature) e `sortedmulti` (Multisignature com chaves ordenadas);
* Caminhos de derivação, por exemplo, `[d34db33f/44h/0h/0h]` indicando um caminho derivado e uma impressão digital de chave mestra específica;
* Chaves em vários formatos, como chaves públicas hexadecimais ou chaves públicas estendidas (`xpub`);
* Um checksum, precedido por um hash, para verificar a integridade do descritor.

Por exemplo, um descritor para uma carteira P2WPKH poderia ser:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```
Neste descritor, a função de derivação `wpkh` indica um tipo de script Pay-to-Witness-Public-Key-Hash. É seguido pelo caminho de derivação que contém:
* `cdeab12f`: a impressão digital da chave mestra;
* `84h`: que significa o uso de um propósito BIP84, destinado a endereços SegWit v0;
* `0h`: que indica que é uma moeda BTC na rede principal;
* `0h`: que se refere ao número de conta específico usado na carteira.

O descritor também inclui a chave pública estendida usada nesta carteira:
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U

A seguir, a notação `/<0;1>/*` especifica que o descritor pode gerar endereços da cadeia externa (`0`) e interna (`1`), com um curinga (`*`) permitindo a derivação sequencial de múltiplos endereços de uma maneira configurável, similar a gerenciar um "limite de lacuna" em softwares de carteira tradicionais.

Finalmente, `#jy0l7nr4` representa o checksum para verificar a integridade do descritor.