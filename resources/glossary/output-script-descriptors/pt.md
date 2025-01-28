---
term: DESCRITORES DE SCRIPT DE SAÍDA

---
Os descritores de scripts de saída, ou simplesmente descritores, são expressões estruturadas que descrevem completamente um script de saída (`scriptPubKey`) e fornecem todas as informações necessárias para rastrear transações de ou para um script específico. Esses descritores facilitam o gerenciamento de chaves em carteiras HD através de uma descrição padrão da estrutura e dos tipos de endereços utilizados.

O principal interesse dos descritores reside na sua capacidade de encapsular toda a informação essencial para restaurar uma carteira numa única cadeia de caracteres (para além da frase de recuperação). Ao guardar um descritor com as frases mnemónicas correspondentes, é possível restaurar não só as chaves privadas, mas também a estrutura precisa da carteira e os parâmetros de script associados. De facto, a recuperação de uma carteira requer não só o conhecimento da semente inicial, mas também índices específicos para a derivação de pares de chaves filhas, bem como o `xpub` de cada fator no caso de uma carteira multisig. Anteriormente, assumia-se que esta informação era implicitamente conhecida por todos. No entanto, com a diversificação dos scripts e o aparecimento de configurações mais complexas, esta informação poderia tornar-se difícil de extrapolar, transformando assim estes dados em informação privada e difícil de obter. A utilização de descritores simplifica muito o processo: basta conhecer a(s) frase(s) de recuperação e o descritor correspondente para restaurar tudo de forma fiável e segura.

Um descritor é composto por vários elementos:


- Funções de script como `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignature) e `sortedmulti` (Multisignature com chaves ordenadas);
- Caminhos de derivação, por exemplo, `[d34db33f/44h/0h/0h]` indicando um caminho derivado e uma impressão digital de chave mestra específica;
- Chaves em vários formatos, como chaves públicas hexadecimais ou chaves públicas alargadas (`xpub`);
- Uma soma de controlo, precedida de um hash, para verificar a integridade do descritor.

Por exemplo, um descritor para uma carteira P2WPKH poderia ter o seguinte aspeto:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

Neste descritor, a função de derivação `wpkh` indica um tipo de script Pay-to-Witness-Public-Key-Hash. É seguido pelo caminho de derivação que contém:


- `cdeab12f`: a impressão digital da chave mestra;
- `84h`: que significa a utilização de um objetivo BIP84, destinado a endereços SegWit v0;
- `0h`: o que indica que se trata de uma moeda BTC na rede principal;
- `0h`: que se refere ao número de conta específico utilizado na carteira.

O descritor também inclui a chave pública alargada utilizada nesta carteira:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Em seguida, a notação `/<0;1>/*` especifica que o descritor pode gerar endereços a partir da cadeia externa (`0`) e interna (`1`), com um curinga (`*`) permitindo a derivação seqüencial de múltiplos endereços de forma configurável, semelhante ao gerenciamento de um "limite de lacunas" no software de carteira tradicional.

Finalmente, `#jy0l7nr4` representa a soma de controlo para verificar a integridade do descritor.