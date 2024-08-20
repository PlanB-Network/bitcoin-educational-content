---
termo: CHAVE PÚBLICA
---

A chave pública é um elemento utilizado em criptografia assimétrica. É gerada a partir de uma chave privada usando uma função matemática irreversível. No Bitcoin, as chaves públicas são derivadas de suas chaves privadas associadas através dos algoritmos de assinatura digital de curva elíptica ECDSA ou Schnorr. Diferentemente da chave privada, a chave pública pode ser compartilhada livremente sem comprometer a segurança dos fundos. Dentro do protocolo Bitcoin, a chave pública serve como base para a criação de um endereço Bitcoin, que é então usado para criar condições de gasto em um UTXO usando um `scriptPubKey`. Chaves públicas são frequentemente confundidas com a chave mestra ou com chaves estendidas (xpub...). No entanto, esses elementos são bastante diferentes.

> ► *Em inglês, uma chave pública é chamada de "public key". Este termo é às vezes abreviado como "pubkey" ou "PK".*