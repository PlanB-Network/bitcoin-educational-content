---
term: CLAVE PÚBLICA

---
La clave pública es un elemento utilizado en criptografía asimétrica. Se genera a partir de una clave privada mediante una función matemática irreversible. En Bitcoin, las claves públicas se derivan de su clave privada asociada mediante los algoritmos de firma digital de curva elíptica ECDSA o Schnorr. A diferencia de la clave privada, la clave pública puede compartirse libremente sin comprometer la seguridad de los fondos. Dentro del protocolo Bitcoin, la clave pública sirve como base para crear una dirección Bitcoin, que luego se utiliza para crear condiciones de gasto en un UTXO utilizando una `scriptPubKey`. Las claves públicas se confunden a menudo con la clave maestra o con las claves extendidas (xpub...). Sin embargo, estos elementos son bastante diferentes.

> ► *En inglés, una clave pública se denomina "public key" Este término a veces se abrevia como "pubkey" o "PK"