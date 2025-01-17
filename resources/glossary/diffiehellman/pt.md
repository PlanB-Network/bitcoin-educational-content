---
term: DIFFIE-HELLMAN

---
Método criptográfico que permite a duas partes gerar um segredo partilhado através de um canal de comunicação não seguro. Este segredo pode então ser utilizado para encriptar a comunicação entre as duas partes. Diffie-Hellman utiliza aritmética modular para que, mesmo que um atacante possa observar as trocas, não possa deduzir o segredo partilhado sem resolver um problema matemático difícil: o logaritmo discreto. No Bitcoin, uma variante do DH chamada ECDH que usa uma curva elíptica é por vezes usada, especialmente para protocolos de endereço estático como Silent Payments ou BIP47.