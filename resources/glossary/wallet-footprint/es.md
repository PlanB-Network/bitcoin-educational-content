---
term: HUELLA DE LA CARTERA

---
Conjunto de características distintivas observables en transacciones realizadas por el mismo monedero Bitcoin. Estas características pueden incluir similitudes en el uso de tipos de escritura, reutilización de direcciones, el orden de UTXOs, la colocación de salidas de cambio, la señalización de RBF (*Replace-by-Fee*), el número de versión, el campo `nSequence` y el campo `nLockTime`.

Las huellas de monedero son utilizadas por los analistas para rastrear las actividades de una entidad concreta en la blockchain mediante la identificación de patrones recurrentes en sus transacciones. Por ejemplo, un usuario que envía sistemáticamente su cambio a direcciones P2TR (`bc1p...`) crea una huella distintiva que puede utilizarse para rastrear sus transacciones futuras.

Como explica LaurentMT en Space Kek #19 (podcast francófono), la utilidad de las huellas de monedero en el análisis de cadenas aumenta considerablemente con el tiempo. En efecto, el número creciente de tipos de script y el despliegue cada vez más progresivo de estas nuevas funcionalidades por parte de los softwares de monedero acentúan las diferencias. Incluso es posible identificar con precisión el software utilizado por la entidad rastreada. Por lo tanto, es importante comprender que el estudio de la huella de un monedero es especialmente relevante para las transacciones recientes, más que para las iniciadas a principios de la década de 2010.