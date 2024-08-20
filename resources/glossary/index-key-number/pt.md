---
term: INDEX (KEY NUMBER)
---

No contexto de uma carteira HD, refere-se ao número sequencial atribuído a uma chave filha gerada a partir de uma chave pai. Este índice é usado em combinação com a chave pai e o código de cadeia pai para derivar deterministicamente chaves filhas únicas. Permite uma organização estruturada e a geração reprodutível de múltiplos pares de chaves filhas irmãs a partir da mesma chave pai. É um inteiro de 32 bits usado na função de derivação `HMAC-SHA512`. Este número, portanto, diferencia chaves filhas irmãs dentro de uma carteira HD.