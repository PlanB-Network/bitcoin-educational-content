---
term: ENTROPÍA (ANÁLISIS)

---
En el contexto específico del análisis de cadenas, entropía es también el nombre de un indicador, derivado de la entropía de Shannon, inventado por LaurentMT. Este indicador permite medir el desconocimiento que tienen los analistas sobre la configuración exacta de una transacción Bitcoin. En otras palabras, cuanto mayor es la entropía de una transacción, más difícil resulta para los analistas identificar los movimientos de bitcoins entre entradas y salidas.

En la práctica, la entropía revela si, desde la perspectiva de un observador externo, una transacción presenta múltiples interpretaciones posibles, basadas únicamente en las cantidades de entradas y salidas, sin tener en cuenta otros patrones y heurísticos externos o internos. Una entropía elevada es entonces sinónimo de una mejor confidencialidad de la transacción.

La entropía se define como el logaritmo binario del número de combinaciones posibles. He aquí la fórmula utilizada con $E$ representando la entropía de la operación y $C$ el número de interpretaciones posibles:

$$
E = \log_2(C)
$$

Teniendo en cuenta los valores de los UTXO implicados en la transacción, el número de interpretaciones $C$ representa el número de formas en que las entradas pueden asociarse con las salidas. En otras palabras, determina el número de interpretaciones que una transacción puede suscitar desde el punto de vista de un observador externo que la analice.