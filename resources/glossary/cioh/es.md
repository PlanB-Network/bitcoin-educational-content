---
term: CIOH
---

Abreviatura de "*Common Input Ownership Heuristic*" (Heurística de Propiedad Común de Entrada). Es una heurística utilizada en el campo del análisis de cadena de Bitcoin que asume que todas las entradas de una transacción pertenecen a la misma entidad o usuario. Al observar los datos públicos de una transacción de Bitcoin, y se detectan múltiples entradas, entonces, si no hay patrones u otra información para refutar esto, se puede estimar que todas las entradas de esta transacción pertenecieron a una sola persona (o entidad).

Esta heurística de análisis fue descubierta por el propio Satoshi Nakamoto, quien la discute en la parte 10 del Libro Blanco:

> "Sin embargo, la conexión es inevitable con transacciones de múltiples entradas, que necesariamente revelan que sus entradas eran propiedad del mismo dueño. El riesgo es que si se revela el propietario de una clave, las conexiones pueden revelar otras transacciones que pertenecieron al mismo dueño." - Nakamoto, S. (2008). "Bitcoin: Un Sistema de Efectivo Electrónico Entre Pares". Consultado en https://bitcoin.org/bitcoin.pdf.

Incluso hoy en día, CIOH sigue siendo la principal heurística utilizada por las empresas de análisis de cadena, junto con el reuso de direcciones.

![](../../dictionnaire/assets/13.png)

> ► *En inglés, "CIOH" podría traducirse como "Heurística de Propiedad Común de Entrada".*