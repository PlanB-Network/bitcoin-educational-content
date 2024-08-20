---
term: BECH32 Y BECH32M
---

`Bech32` y `Bech32m` son dos formatos de codificación de direcciones para recibir bitcoins. Se basan en una base 32 ligeramente modificada. Incorporan un checksum basado en un algoritmo de corrección de errores llamado BCH (*Bose-Chaudhuri-Hocquenghem*). Comparadas con las direcciones Legacy, codificadas en `Base58check`, las direcciones `Bech32` y `Bech32m` tienen un checksum más eficiente, permitiendo la detección y potencial corrección automática de errores tipográficos. Su formato también ofrece una mejor legibilidad, con solo caracteres en minúsculas. Aquí está la matriz de adición para este formato desde base 10:

&nbsp;

| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

&nbsp;
Bech32 y Bech32m son formatos de codificación utilizados para representar direcciones SegWit. Bech32 es un formato de codificación de direcciones introducido por BIP173 en 2017. Utiliza un conjunto específico de caracteres, compuesto por números y letras minúsculas, para minimizar los errores de tipeo y facilitar la lectura. Las direcciones Bech32 generalmente comienzan con `bc1` para indicar que son nativas de SegWit. Este formato solo se utiliza en direcciones SegWit V0, con los scripts P2WPKH (Pay to Witness Public Key Hash) y P2WSH (Pay to Witness Script Hash). Sin embargo, hay un pequeño defecto inesperado específico del formato Bech32. Siempre que el último carácter de la dirección es una `p`, agregar o quitar cualquier número de caracteres `q` inmediatamente antes de este no invalida el checksum. Esto no afecta los usos existentes de direcciones SegWit V0 (BIP173) debido a su restricción a dos longitudes definidas. Sin embargo, esto podría afectar usos futuros de la codificación Bech32. El formato Bech32m es simplemente un formato Bech32 con este error corregido. Fue introducido con BIP350 en 2020. Las direcciones Bech32m también comienzan con `bc1`, pero están específicamente diseñadas para ser compatibles con SegWit V1 (Taproot) y versiones posteriores, con el script P2TR (Pay to TapRoot).