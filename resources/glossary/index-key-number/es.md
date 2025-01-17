---
term: ÍNDICE (NÚMERO CLAVE)

---
En el contexto de un monedero HD, se refiere al número secuencial asignado a una clave hija generada a partir de una clave padre. Este índice se utiliza en combinación con la clave padre y el código de cadena padre para derivar de forma determinista claves hijo únicas. Permite una organización estructurada y la generación reproducible de múltiples pares de claves hijo hermanas a partir de la misma clave padre. Es un número entero de 32 bits utilizado en la función de derivación `HMAC-SHA512`. Este número permite diferenciar las claves hijas hermanas dentro de un monedero HD.