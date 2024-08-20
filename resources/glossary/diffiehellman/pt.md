---
term: DIFFIE-HELLMAN
---

Método criptográfico que permite a duas partes gerar um segredo compartilhado por meio de um canal de comunicação não seguro. Esse segredo pode então ser usado para criptografar a comunicação entre as duas partes. Diffie-Hellman utiliza aritmética modular de modo que, mesmo que um atacante possa observar as trocas, ele não pode deduzir o segredo compartilhado sem resolver um problema matemático difícil: o logaritmo discreto. No Bitcoin, uma variante do DH chamada ECDH que usa uma curva elíptica é às vezes usada, especialmente para protocolos de endereço estático como Pagamentos Silenciosos ou BIP47.