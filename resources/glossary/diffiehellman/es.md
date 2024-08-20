---
term: DIFFIE-HELLMAN
---

Método criptográfico que permite a dos partes generar un secreto compartido a través de un canal de comunicación no seguro. Este secreto puede luego utilizarse para cifrar la comunicación entre las dos partes. Diffie-Hellman utiliza aritmética modular de modo que, incluso si un atacante puede observar los intercambios, no puede deducir el secreto compartido sin resolver un problema matemático difícil: el logaritmo discreto. En Bitcoin, se utiliza a veces una variante de DH llamada ECDH que usa una curva elíptica, especialmente para protocolos de direcciones estáticas como los Pagos Silenciosos o BIP47.