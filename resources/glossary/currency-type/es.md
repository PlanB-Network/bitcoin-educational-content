---
term: TIPO DE MONEDA

---
En el contexto de los monederos deterministas y jerárquicos (HD), el tipo de moneda (*coin type* en inglés) es un nivel de derivación que permite diferenciar las ramas del monedero en función de las distintas criptomonedas utilizadas. Este nivel de derivación, definido por el BIP 44, se sitúa en la profundidad 2 de la estructura de derivación, a continuación de la clave maestra y de la finalidad. Por ejemplo, para Bitcoin, el índice asignado es `0x80000000`, anotado como `/0'/` en la ruta de derivación. Esto significa que todas las direcciones y cuentas derivadas de esta ruta están asociadas a Bitcoin. Esta capa de derivación permite una clara separación de los diferentes activos en un monedero multidivisa. Estos son los índices utilizados para varias criptomonedas:


- Bitcoin: `0x80000000`;
- Bitcoin Testnet: `0x80000001`;
- Litecoin: `0x80000002`;
- Dogecoin: `0x80000003`;
- Ethereum: `0x8000003c`...

![](../../dictionnaire/assets/21.webp)