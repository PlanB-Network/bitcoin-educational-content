---
term: HUELLA DE MONEDERO
---

Un conjunto de características distintivas observables en transacciones realizadas por el mismo monedero de Bitcoin. Estas características pueden incluir similitudes en el uso de tipos de script, reutilización de direcciones, el orden de los UTXOs, la colocación de salidas de cambio, la señalización de RBF (*Replace-by-Fee*), el número de versión, el campo `nSequence` y el campo `nLockTime`.

Las huellas de monedero son utilizadas por analistas para rastrear las actividades de una entidad particular en la blockchain identificando patrones recurrentes en sus transacciones. Por ejemplo, un usuario que sistemáticamente envía su cambio a direcciones P2TR (`bc1p…`) crea una huella distintiva que puede ser utilizada para rastrear sus futuras transacciones.

Como explica LaurentMT en Space Kek #19 (un podcast en francés), la utilidad de las huellas de monedero en el análisis de cadena aumenta significativamente con el tiempo. De hecho, el creciente número de tipos de script y la implementación cada vez más gradual de estas nuevas características por el software de monedero acentúan las diferencias. Incluso es posible identificar con precisión el software utilizado por la entidad rastreada. Por lo tanto, es importante entender que estudiar la huella de un monedero es particularmente relevante para transacciones recientes, más aún que para aquellas iniciadas a principios de la década de 2010.