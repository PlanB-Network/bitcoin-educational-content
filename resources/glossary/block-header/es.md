---
term: CABECERA DE BLOQUE

---
La cabecera de bloque es una estructura de datos que sirve como componente principal en la construcción de un bloque Bitcoin. Cada bloque consta de una cabecera y una lista de transacciones. La cabecera de bloque contiene información crucial que asegura la integridad y validez de un bloque dentro de la cadena de bloques. La cabecera del bloque contiene 80 bytes de metadatos y se compone de los siguientes elementos:


- La versión en bloque;
- El hash del bloque anterior;
- La raíz del árbol Merkle de las transacciones;
- La marca de tiempo del bloque;
- El objetivo de dificultad;
- El nonce.

Por ejemplo, aquí está la cabecera del bloque número 785.530 en formato hexadecimal, extraído por Foundry USA el 15 de abril de 2023:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Si desglosamos este encabezamiento, podemos reconocer:


- La versión:

```text
00e0ff3f
```


- El hash anterior:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```


- La raíz de Merkle:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```


- La marca de tiempo:

```text
bcb13a64
```


- El objetivo:

```text
b2e00517
```


- El nonce:

```text
43f09a40
```

Para ser válido, un bloque debe tener una cabecera que, una vez hasheada con `SHA256d`, produzca un hash menor o igual que el objetivo de dificultad.

> ► *En inglés se denomina "Block Header "*