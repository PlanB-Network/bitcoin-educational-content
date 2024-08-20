---
term: SHA512
---

Acrônimo para "*Secure Hash Algorithm 512 bits*" (Algoritmo de Hash Seguro de 512 bits). É uma função de hash criptográfico que produz um resumo de 512 bits. Foi projetado pela *National Security Agency* (NSA) no início dos anos 2000. Para o Bitcoin, a função `SHA512` não é usada diretamente dentro do protocolo, mas é utilizada no contexto de derivação de chaves filhas no nível da aplicação, de acordo com o BIP32 e BIP39. Nestes processos, ela é usada múltiplas vezes no algoritmo `HMAC`, assim como na função de derivação de chave `PBKDF2`. A função `SHA512` faz parte da família SHA 2, assim como o `SHA256`. Sua operação é muito semelhante a este último.