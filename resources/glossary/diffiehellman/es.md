---
term: DIFFIE-HELLMAN

---
Método criptográfico que permite a dos partes generar un secreto compartido a través de un canal de comunicación no seguro. Este secreto puede utilizarse después para cifrar la comunicación entre las dos partes. Diffie-Hellman utiliza aritmética modular para que, aunque un atacante pueda observar los intercambios, no pueda deducir el secreto compartido sin resolver un difícil problema matemático: el logaritmo discreto. En Bitcoin, a veces se utiliza una variante de DH llamada ECDH que utiliza una curva elíptica, especialmente para protocolos de direcciones estáticas como Silent Payments o BIP47.