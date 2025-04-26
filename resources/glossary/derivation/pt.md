---
term: DERIVAÇÃO

---
Refere-se ao processo de geração de pares de chaves filhas a partir de um par de chaves pai (chave privada e chave pública) e de um código de cadeia numa carteira determinística e hierárquica (HD). Este processo permite a segmentação de ramos e a organização de uma carteira em diferentes níveis com numerosos pares de chaves filhas, que podem ser recuperados conhecendo apenas a informação básica de recuperação (a frase mnemónica e qualquer frase-chave potencial). Para derivar uma chave filha, a função `HMAC-SHA512` é usada com o código da cadeia pai e a concatenação da chave pai e um índice de 32 bits. Existem dois tipos de derivações:


- Derivação normal, que utiliza a chave pública principal como base da função `HMAC-SHA512`;
- Derivação reforçada, que utiliza a chave privada principal como base da função `HMAC-SHA512`;

O resultado do HMAC-SHA512 é dividido em dois: os primeiros 256 bits tornam-se a chave filha (privada ou pública após o processamento através do ECDSA) e os restantes 256 bits tornam-se o código da cadeia filha.