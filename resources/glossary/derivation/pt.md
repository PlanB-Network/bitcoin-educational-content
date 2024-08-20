---
term: DERIVAÇÃO
---

Refere-se ao processo de gerar pares de chaves filhas a partir de um par de chaves pai (chave privada e chave pública) e um código de cadeia dentro de uma carteira determinística e hierárquica (HD). Este processo permite a segmentação de ramos e a organização de uma carteira em diferentes níveis com numerosos pares de chaves filhas, que podem todos ser recuperados conhecendo apenas as informações básicas de recuperação (a frase mnemônica e qualquer potencial frase-senha). Para derivar uma chave filha, a função `HMAC-SHA512` é usada com o código de cadeia pai e a concatenação da chave pai e um índice de 32 bits. Existem dois tipos de derivações:
* Derivação normal, que usa a chave pública pai como base da função `HMAC-SHA512`;
* Derivação reforçada, que usa a chave privada pai como base da função `HMAC-SHA512`;

O resultado do HMAC-SHA512 é dividido em dois: os primeiros 256 bits tornam-se a chave filha (privada ou pública após processamento através do ECDSA), e os 256 bits restantes tornam-se o código de cadeia filha.