---
term: BIP0385

definition: Funciones addr() y raw() para describir scripts de salida por dirección o en hexadecimal en los descriptores.
---
Introduce las funciones descriptoras `addr(ADDR)` y `raw(HEX)`. La función `addr(ADDR)` permite describir un script de salida utilizando una dirección de recepción, mientras que la función `raw(HEX)` permite especificar un script de salida utilizando una representación hexadecimal sin procesar de dicho script. El BIP385 fue implementado junto con el resto de BIPs relacionados con el descriptor (excepto el BIP386) en la versión 0.17 de Bitcoin Core.