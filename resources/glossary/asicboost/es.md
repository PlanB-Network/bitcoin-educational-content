---
term: ASICBOOST
---

ASICBOOST es un método de optimización algorítmica inventado en 2016, diseñado para aumentar la eficiencia de la minería de Bitcoin en aproximadamente un 20% al reducir la cantidad de cálculos necesarios para cada intento de hash del encabezado. Esta técnica explota una característica de la función hash SHA256, utilizada para la minería, que divide los datos en bloques antes de procesarlos. ASICBOOST retiene uno de estos bloques sin cambios a través de múltiples intentos de hashing, permitiendo al minero solo hacer parte del trabajo para este bloque en varios intentos. Esta compartición de datos permite la reutilización de resultados de cálculos previos, reduciendo así el número total de cálculos necesarios para encontrar un hash válido.

ASICBOOST puede usarse en dos formas: ASICBOOST abierto y ASICBOOST encubierto. La forma abierta de ASICBOOST es visible para todos, ya que implica usar el campo `nVersion` del bloque como un nonce, y no alterar el `Nonce` real. La forma encubierta busca ocultar estas modificaciones mediante el uso de árboles de Merkle. Sin embargo, este segundo método se ha vuelto menos efectivo desde la introducción de SegWit debido al segundo árbol de Merkle, que aumenta el número de cálculos necesarios para usarlo.

En resumen, ASICBOOST permite a los mineros no tener que realizar un verdadero SHA256 completo para todos los intentos de hashing, ya que parte del resultado permanece sin cambios, lo que acelera el trabajo de los mineros.