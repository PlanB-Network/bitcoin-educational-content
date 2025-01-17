---
term: TIPO DE MOEDA

---
No contexto das carteiras determinísticas e hierárquicas (HD), o tipo de moeda (*coin type* em inglês) é um nível de derivação que permite diferenciar os ramos da carteira com base nas várias criptomoedas utilizadas. Este nível de derivação, definido pelo BIP 44, situa-se na profundidade 2 da estrutura de derivação, a seguir à chave mestra e à finalidade. Por exemplo, para a Bitcoin, o índice atribuído é `0x80000000`, anotado como `/0'/` no caminho de derivação. Isto significa que todos os endereços e contas derivados deste caminho estão associados à Bitcoin. Esta camada de derivação permite uma separação clara dos diferentes activos numa carteira com várias moedas. Aqui estão os índices usados para várias criptomoedas:


- Bitcoin: `0x80000000`;
- Bitcoin Testnet: `0x80000001`;
- Litecoin: `0x80000002`;
- Dogecoin: `0x80000003`;
- Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.webp)