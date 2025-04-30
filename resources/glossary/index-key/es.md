---
term: ÍNDICE (CLAVE)
---

En el contexto de una cartera HD, se refiere al número secuencial asignado a una clave hija generada a partir de una clave padre. Este índice se utiliza en combinación con la clave padre y el código de cadena padre para derivar de forma determinista claves hijas únicas. Permite la organización estructurada y la generación reproducible de múltiples pares de claves hijo hermanas a partir de una única clave padre. Es un número entero de 32 bits que se utiliza en la función de derivación `HMAC-SHA512`. Este número puede utilizarse para diferenciar claves hijas dentro de una cartera HD.