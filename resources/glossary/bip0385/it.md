---
term: BIP0385

definition: Funzioni addr() e raw() per descrivere gli script di output per indirizzo o in esadecimale nei descrittori.
---
Introduce le funzioni di descrittore `addr(ADDR)` e `raw(HEX)`. La funzione `addr(ADDR)` consente di descrivere uno script di output utilizzando un indirizzo di ricezione, mentre la funzione `raw(HEX)` consente di specificare uno script di output utilizzando una rappresentazione esadecimale grezza di tale script. BIP385 è stato implementato insieme a tutti gli altri BIP relativi ai descrittori (tranne BIP386) nella versione 0.17 di Bitcoin Core.