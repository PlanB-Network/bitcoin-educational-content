---
term: CLAVE PÚBLICA
---

La clave pública es un elemento utilizado en la criptografía asimétrica. Se genera a partir de una clave privada usando una función matemática irreversible. En Bitcoin, las claves públicas se derivan de su clave privada asociada a través de los algoritmos de firma digital de curva elíptica ECDSA o Schnorr. A diferencia de la clave privada, la clave pública puede ser compartida libremente sin comprometer la seguridad de los fondos. Dentro del protocolo de Bitcoin, la clave pública sirve como base para crear una dirección de Bitcoin, que luego se utiliza para crear condiciones de gasto en un UTXO usando un `scriptPubKey`. Las claves públicas a menudo se confunden con la clave maestra o con las claves extendidas (xpub...). Sin embargo, estos elementos son bastante diferentes.

> ► *En inglés, una clave pública se llama "public key". Este término a veces se abrevia como "pubkey" o "PK".*