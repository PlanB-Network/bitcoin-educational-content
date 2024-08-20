---
term: PBKDF2
---

`PBKDF2` significa *Password-Based Key Derivation Function 2* (Função de Derivação de Chave Baseada em Senha 2). É um método para criar chaves criptográficas a partir de uma senha usando uma função de derivação. Ele recebe como entrada uma senha, um sal criptográfico e aplica iterativamente uma função predeterminada (geralmente uma função de hash como `SHA256` ou um `HMAC`) a esses dados. Esse processo é repetido muitas vezes para gerar uma chave criptográfica.

No contexto do Bitcoin, `PBKDF2` é usado em conjunto com a função `HMAC-SHA512` para criar a semente de uma carteira determinística e hierárquica (seed) a partir de uma frase de recuperação de 12 ou 24 palavras. O sal criptográfico usado neste caso é a passphrase BIP39, e o número de iterações é `2048`.