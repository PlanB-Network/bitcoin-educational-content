---
term: LIBSECP256K1
---

Librería en C de alto rendimiento y seguridad para firmas digitales y otras primitivas criptográficas en la curva elíptica `secp256k1`. Dado que esta curva nunca ha sido ampliamente utilizada fuera de Bitcoin (a diferencia de la curva a menudo preferida `secp256r1`), esta biblioteca pretende ser la referencia más completa para su uso. El desarrollo de libsecp256k1 se orientó principalmente hacia las necesidades de Bitcoin, y las características destinadas a otras aplicaciones pueden estar menos probadas o verificadas. El uso apropiado de esta biblioteca requiere una cuidadosa atención, para asegurar que es adecuada para los propósitos específicos de aplicaciones distintas de Bitcoin.


La biblioteca libsecp256k1 ofrece una variedad de características, incluyendo:




- Firma y verificación ECDSA-secp256k1, y generación de claves criptográficas ;
- Operaciones aditivas y multiplicativas sobre claves secretas y públicas ;
- Serialización y análisis de claves secretas, claves públicas y firmas ;
- Firma y generación de claves públicas en tiempo constante con acceso constante a memoria;
- Y muchas otras primitivas criptográficas.