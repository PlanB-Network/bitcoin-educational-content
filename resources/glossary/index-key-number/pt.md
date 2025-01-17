---
term: ÍNDICE (NÚMERO CHAVE)

---
No contexto de uma carteira HD, refere-se ao número sequencial atribuído a uma chave filha gerada a partir de uma chave pai. Este índice é utilizado em combinação com a chave-mãe e o código da cadeia-mãe para derivar deterministicamente chaves-filhas únicas. Permite uma organização estruturada e a geração reproduzível de vários pares de chaves filhas irmãs a partir da mesma chave-mãe. É um número inteiro de 32 bits utilizado na função de derivação `HMAC-SHA512`. Este número diferencia assim as chaves filhas de irmãos dentro de uma carteira HD.