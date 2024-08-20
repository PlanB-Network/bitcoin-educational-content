---
term: NONCE
---

No contexto da computação, o termo "nonce" refere-se a um número que é utilizado apenas uma vez e depois substituído. Geralmente, é aleatório ou pseudoaleatório. Nonces são usados em diversos protocolos criptográficos para garantir a segurança do processo. Por exemplo, as assinaturas ECDSA usadas dentro do protocolo Bitcoin incluem o uso de um nonce. Isso significa que esse número deve ser novo para cada assinatura. Caso contrário, é possível calcular a chave privada usada comparando duas assinaturas que utilizam o mesmo nonce.

Nonces também são usados no processo de mineração do Bitcoin. Os mineradores incrementam esses valores modificáveis dentro de seus blocos candidatos. Eles modificam o valor do nonce a fim de encontrar um hash criptográfico que seja menor ou igual ao alvo de dificuldade. Esse processo requer significativa capacidade computacional, pois envolve uma busca exaustiva entre um grande número de nonces possíveis. Quando um minerador encontra um nonce que, ao ser incluído em seu bloco, produz um resumo que atende aos critérios de dificuldade, o bloco é transmitido para a rede, e o minerador ganha a recompensa.

> ► *Em 2010, pesquisadores descobriram que o PlayStation 3 da Sony usava o mesmo nonce ao assinar diferentes pacotes de código. Esse reuso do nonce permitiu que atacantes calculassem a chave privada usada para assinar o software. Com a chave privada em mãos, os atacantes poderiam criar assinaturas válidas para qualquer código, permitindo-lhes executar software não autorizado, incluindo jogos piratas ou sistemas operacionais personalizados, diretamente no PS3.*

> ► *Há um equívoco comum sobre a origem do termo "nonce". Alguns afirmam que representa a abreviação de "number only used once" (número usado apenas uma vez). Na realidade, a origem da palavra remonta ao século 18 e vem da evolução semântica da expressão em inglês antigo "then anes", que significava "para a ocasião".*