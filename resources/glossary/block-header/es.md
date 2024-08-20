---
term: BLOCK HEADER
---

El encabezado de bloque es una estructura de datos que sirve como el componente principal en la construcción de un bloque de Bitcoin. Cada bloque consta de un encabezado y una lista de transacciones. El encabezado del bloque contiene información crucial que asegura la integridad y validez de un bloque dentro de la cadena de bloques. El encabezado del bloque contiene 80 bytes de metadatos y está compuesto por los siguientes elementos:
* La versión del bloque;
* El hash del bloque anterior;
* La raíz del árbol de Merkle de las transacciones;
* El timestamp del bloque;
* El objetivo de dificultad;
* El nonce.

Por ejemplo, aquí está el encabezado del bloque número 785,530 en formato hexadecimal, minado por Foundry USA el 15 de abril de 2023:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Si desglosamos este encabezado, podemos reconocer:
* La versión:

```text
00e0ff3f
```

* El hash anterior:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```

* La raíz de Merkle:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```

* El timestamp:

```text
bcb13a64
```

* El objetivo:

```text
b2e00517
```

* El nonce:

```text
43f09a40
```

Para ser válido, un bloque debe tener un encabezado que, una vez hasheado con `SHA256d`, produce un hash que es menor o igual al objetivo de dificultad.

> ► *En inglés, se le denomina "Block Header".*