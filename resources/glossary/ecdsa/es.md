---
term: ECDSA

---
Acrónimo de "Algoritmo de firma digital de curva elíptica" Es un algoritmo de firma digital basado en la criptografía de curva elíptica (ECC). Es una variante del DSA (Algoritmo de Firma Digital). ECDSA utiliza las propiedades de las curvas elípticas para proporcionar niveles de seguridad comparables a los de los algoritmos tradicionales de clave pública, como RSA, utilizando al mismo tiempo tamaños de clave significativamente menores. ECDSA permite generar pares de claves (pública y privada), así como crear y verificar firmas digitales.

En el contexto de Bitcoin, ECDSA se utiliza para derivar claves públicas a partir de claves privadas. También se utiliza para firmar transacciones, con el fin de satisfacer un script para desbloquear bitcoins y gastarlos. La curva elíptica utilizada en el ECDSA de Bitcoin es `secp256k1`, definida por la ecuación $y^2 = x^3 + 7$. Este algoritmo se ha utilizado desde la creación de Bitcoin en 2009. Hoy en día, comparte su lugar con el protocolo Schnorr, otro algoritmo de firma digital introducido con Taproot en 2021.