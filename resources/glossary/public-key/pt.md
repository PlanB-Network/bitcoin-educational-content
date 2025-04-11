---
term: CHAVE PÚBLICA

---
A chave pública é um elemento utilizado na criptografia assimétrica. É gerada a partir de uma chave privada utilizando uma função matemática irreversível. Na Bitcoin, as chaves públicas são derivadas da sua chave privada associada através dos algoritmos de assinatura digital de curva elíptica ECDSA ou Schnorr. Ao contrário da chave privada, a chave pública pode ser livremente partilhada sem comprometer a segurança dos fundos. Dentro do protocolo Bitcoin, a chave pública serve como base para a criação de um endereço Bitcoin, que é então usado para criar condições de gastos em um UTXO usando um `scriptPubKey`. As chaves públicas são frequentemente confundidas com a chave mestra ou com chaves estendidas (xpub...). No entanto, estes elementos são bastante diferentes.

> ► *Em inglês, uma chave pública é designada por "public key" Este termo é por vezes abreviado como "pubkey" ou "PK"