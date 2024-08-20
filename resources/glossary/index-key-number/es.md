---
term: INDEX (KEY NUMBER)
---

En el contexto de una cartera HD, se refiere al número secuencial asignado a una clave hija generada a partir de una clave padre. Este índice se utiliza en combinación con la clave padre y el código de cadena padre para derivar de manera determinista claves hijas únicas. Permite una organización estructurada y la generación reproducible de múltiples pares de claves hijas hermanas a partir de la misma clave padre. Es un entero de 32 bits utilizado en la función de derivación `HMAC-SHA512`. Este número, por lo tanto, diferencia las claves hijas hermanas dentro de una cartera HD.