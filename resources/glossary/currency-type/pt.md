---
term: TIPO DE MOEDA
---

No contexto de carteiras determinísticas e hierárquicas (HD), o tipo de moeda (*coin type* em inglês) é um nível de derivação que permite diferenciar os ramos da carteira com base nas diversas criptomoedas utilizadas. Esta camada de derivação, definida pelo BIP 44, está localizada na profundidade 2 da estrutura de derivação, seguindo a chave mestre e o propósito. Por exemplo, para o Bitcoin, o índice atribuído é `0x80000000`, notado como `/0'/` no caminho de derivação. Isso significa que todos os endereços e contas derivados deste caminho estão associados ao Bitcoin. Esta camada de derivação possibilita uma clara separação de diferentes ativos em uma carteira multi-moeda. Aqui estão os índices usados para várias criptomoedas:
* Bitcoin: `0x80000000`;
* Bitcoin Testnet: `0x80000001`;
* Litecoin: `0x80000002`;
* Dogecoin: `0x80000003`;
* Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.png)