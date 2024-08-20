---
term: ANÁLISIS DE CADENA
---

Práctica que abarca todos los métodos utilizados para rastrear el flujo de bitcoins en la blockchain. Generalmente, el análisis de cadena se basa en la observación de características en muestras de transacciones anteriores. Luego implica identificar estas mismas características en una transacción que se desea analizar y deducir interpretaciones plausibles. Este método de resolución de problemas, basado en un enfoque práctico para encontrar una solución suficientemente buena, es conocido como heurística. Para simplificar, el análisis de cadena se realiza en dos pasos principales:
* Identificar características conocidas;
* Deducción de hipótesis.

Uno de los objetivos del análisis de cadena es agrupar diversas actividades en Bitcoin con el fin de determinar la unicidad del usuario que las realizó. Posteriormente, será posible intentar vincular este conjunto de actividades a una identidad real a través de un punto de entrada. Es importante entender que el análisis de cadena no es una ciencia exacta. Se basa en heurísticas derivadas de observaciones previas o interpretaciones lógicas. Estas reglas permiten obtener resultados bastante fiables, pero nunca con precisión absoluta. En otras palabras, el análisis de cadena siempre implica una dimensión de probabilidad en las conclusiones obtenidas. Por ejemplo, se puede estimar con más o menos certeza que dos direcciones pertenecen a la misma entidad, pero la certeza total siempre estará fuera de alcance. El objetivo completo del análisis de cadena yace precisamente en la agregación de diversas heurísticas con el fin de minimizar el riesgo de error. Es, de cierta manera, una acumulación de evidencia que nos permite acercarnos a la realidad. Estas famosas heurísticas pueden agruparse en diferentes categorías:
* Patrones de transacción (o modelos de transacción);
* Heurísticas internas a la transacción;
* Heurísticas externas a la transacción.

Es digno de mención que las primeras dos heurísticas sobre Bitcoin fueron formuladas por el propio Satoshi Nakamoto. Las presenta en la parte 10 del White Paper. Es interesante observar que estas dos heurísticas todavía mantienen una preeminencia en el análisis de cadena hoy en día. Estas son la Heurística de Propiedad de Entrada Común (CIOH, por sus siglas en inglés) y la reutilización de direcciones.