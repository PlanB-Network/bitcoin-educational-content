---
term: ECDSA
---

Acrónimo de "Elliptic Curve Digital Signature Algorithm" (Algoritmo de Firma Digital de Curva Elíptica). Es un algoritmo de firma digital basado en la criptografía de curva elíptica (ECC). Es una variante del DSA (Digital Signature Algorithm). ECDSA utiliza las propiedades de las curvas elípticas para proporcionar niveles de seguridad comparables a los de los algoritmos de clave pública tradicionales, como RSA, mientras utiliza tamaños de clave significativamente menores. ECDSA permite la generación de pares de claves (claves públicas y privadas) así como la creación y verificación de firmas digitales.

En el contexto de Bitcoin, ECDSA se utiliza para derivar claves públicas a partir de claves privadas. También se utiliza para firmar transacciones, con el fin de satisfacer un script para desbloquear bitcoins y gastarlos. La curva elíptica utilizada en el ECDSA de Bitcoin es `secp256k1`, definida por la ecuación $y^2 = x^3 + 7$. Este algoritmo ha sido utilizado desde la creación de Bitcoin en 2009. Hoy en día, comparte su lugar con el protocolo Schnorr, otro algoritmo de firma digital introducido con Taproot en 2021.