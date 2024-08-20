---
term: SECP256K1
---

Nombre dado a una curva elíptica específica utilizada en el protocolo de Bitcoin para la implementación de los algoritmos de firma digital ECDSA (*Elliptic Curve Digital Signature Algorithm*) y Schnorr. La curva `secp256k1` fue elegida por el inventor de Bitcoin, Satoshi Nakamoto. Tiene algunas propiedades interesantes, notablemente beneficios para el rendimiento.

El uso de `secp256k1` en Bitcoin significa que cada clave privada (un número aleatorio de 256 bits) se mapea a una clave pública correspondiente a través de la adición y duplicación del punto de la clave privada por el punto generador de la curva `secp256k1`. Esta operación es fácil de realizar en una dirección pero prácticamente imposible de revertir, lo que forma la base de la seguridad de las firmas digitales en Bitcoin.

La curva `secp256k1` está especificada por la ecuación de la curva elíptica $y^2 = x^3 + 7$, lo que significa que tiene coeficientes $a$ igual a $0$ y $b$ igual a $7$ en la forma general de una ecuación de curva elíptica $y^2 = x^3 + ax + b$. `secp256k1` está definida sobre un campo finito cuyo orden es un número primo muy grande, específicamente $p = 2^{256} - 2^{32} - 977$. La curva también tiene un orden de grupo, que es el número de puntos distintos en la curva, un punto generador predefinido (o punto $G$), que se utiliza en operaciones criptográficas para generar pares de claves, y un cofactor igual a $1$.

> ► *“SEC” significa “Standards for Efficient Cryptography” (Estándares para Criptografía Eficiente). “P256” indica que la curva está definida sobre un campo $\mathbb{Z}_p$ donde $p$ es un número primo de 256 bits. “K” se refiere al nombre de su inventor, Neal Koblitz. Finalmente, “1” indica que esta es la primera versión de esta curva.*