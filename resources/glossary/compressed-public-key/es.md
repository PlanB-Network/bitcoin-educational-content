---
term: CLAVE PÚBLICA COMPRIMIDA
---

Una clave pública se utiliza en scripts (ya sea directamente en forma de una clave pública o como una dirección) para recibir y asegurar bitcoins. Una clave pública en formato bruto se representa por un punto en una curva elíptica, consistiendo en dos coordenadas (`x, y`) cada una de 256 bits. En formato bruto, una clave pública mide por lo tanto 512 bits, sin contar el byte adicional para identificar el formato. Por otro lado, una clave pública comprimida es una forma más compacta de representación de la clave pública. Utiliza solo la coordenada `x` y un prefijo (`02` o `03`) que indica la paridad de la coordenada `y` (par o impar).

Si simplificamos esto al campo de los números reales, dado que la curva elíptica es simétrica respecto al eje x, para cualquier punto $P$ (`x, y`) en la curva, existe un punto $P'$ (`x, -y`) que también estará en esta misma curva. Esto significa que para cada `x`, solo hay dos posibles valores de `y`, positivo y negativo. Por ejemplo, para una abscisa dada `x`, habría dos puntos $P1$ y $P2$ en la curva elíptica, compartiendo la misma abscisa pero con ordenadas opuestas:

![](../../dictionnaire/assets/29.png)
Para elegir entre los dos posibles puntos en la curva, se agrega un prefijo especificando qué `y` elegir a `x`. Este método permite reducir el tamaño de una clave pública de 520 bits a solo 264 bits (8 bits de prefijo + 256 bits para `x`). Esta representación es conocida como la forma comprimida de la clave pública.

Sin embargo, en el contexto de la criptografía de curva elíptica, no usamos los números reales, sino un campo finito de orden `p` (un número primo). En este contexto, el "signo" de `y` se determina por su paridad, es decir, si `y` es par o impar. El prefijo `0x02` indica entonces una `y` par, mientras que `0x03` indica una `y` impar.

Considere el siguiente ejemplo de una clave pública en bruto (un punto en la curva elíptica) en hexadecimal:
```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Podemos aislar el prefijo, `x`, y `y`:
```plaintext
Prefijo = 04
Para determinar la paridad de `y`, examinamos el último carácter hexadecimal de `y`:
```plaintext
Base 16 (hexadecimal): f
Base 10 (decimal): 15
y es impar
```

El prefijo para la clave pública comprimida será `03`. La clave pública comprimida en hexadecimal se convierte en:
```plaintext
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```