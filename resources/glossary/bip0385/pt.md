---
term: BIP0385

definition: Funções addr() e raw() para descrever scripts de saída por endereço ou em hexadecimal nos descriptors.
---
Introduz as funções descritoras `addr(ADDR)` e `raw(HEX)`. A função `addr(ADDR)` permite descrever um script de saída utilizando um endereço de receção, enquanto a função `raw(HEX)` permite especificar um script de saída utilizando uma representação hexadecimal bruta desse script. O BIP385 foi implementado junto com todos os outros BIPs relacionados a descritores (exceto o BIP386) na versão 0.17 do Bitcoin Core.