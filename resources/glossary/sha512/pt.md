---
term: SHA512

---
Acrónimo de "*Secure Hash Algorithm 512 bits*". É uma função de hash criptográfica que produz um digest de 512 bits. Foi projetado pela *National Security Agency* (NSA) no início dos anos 2000. Para o Bitcoin, a função `SHA512` não é utilizada diretamente no protocolo, mas é utilizada no contexto da derivação de chaves-filhas ao nível da aplicação, de acordo com o BIP32 e o BIP39. Nestes processos, é utilizada várias vezes no algoritmo `HMAC`, bem como na função de derivação de chaves `PBKDF2`. A função `SHA512` faz parte da família SHA 2, assim como a `SHA256`. O seu funcionamento é muito semelhante a este último.