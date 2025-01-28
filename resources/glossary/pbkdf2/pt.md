---
term: PBKDF2

---
pBKDF2 é o acrónimo de *Password-Based Key Derivation Function 2*. É um método para criar chaves criptográficas a partir de uma palavra-passe utilizando uma função de derivação. Toma como entrada uma palavra-passe, um sal criptográfico e aplica iterativamente uma função predeterminada (frequentemente uma função hash como `SHA256` ou um `HMAC`) a estes dados. Este processo é repetido várias vezes para gerar uma chave criptográfica.

No contexto do Bitcoin, o `PBKDF2` é utilizado em conjunto com a função `HMAC-SHA512` para criar a semente de uma carteira determinística e hierárquica (seed) a partir de uma frase de recuperação de 12 ou 24 palavras. O sal criptográfico utilizado neste caso é a frase-passe BIP39, e o número de iterações é `2048`.