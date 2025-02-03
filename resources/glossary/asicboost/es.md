---
term: ASICBOOST

---
ASICBOOST es un método de optimización algorítmica inventado en 2016, diseñado para aumentar la eficiencia de la minería de Bitcoin en torno a un 20% reduciendo la cantidad de cálculos necesarios para cada intento de hash de la cabecera. Esta técnica explota una característica de la función hash SHA256, utilizada para la minería, que divide los datos en bloques antes de procesarlos. ASICBOOST mantiene uno de estos bloques sin cambios en varios intentos de hash, lo que permite al minero realizar sólo una parte del trabajo de este bloque en varios intentos. Esta compartición de datos permite reutilizar los resultados de cálculos anteriores, reduciendo así el número total de cálculos necesarios para encontrar un hash válido.

ASICBOOST puede utilizarse de dos formas: ASICBOOST manifiesto y ASICBOOST encubierto. La forma Overt ASICBOOST es visible para todos, ya que consiste en utilizar el campo `nVersion` del bloque como nonce, y no alterar el `Nonce` real. La forma Covert trata de ocultar estas modificaciones utilizando árboles de Merkle. Sin embargo, este segundo método ha perdido eficacia desde la introducción de SegWit debido al segundo árbol de Merkle, que aumenta el número de cálculos necesarios para utilizarlo.

En resumen, ASICBOOST permite a los mineros no tener que realizar un verdadero SHA256 completo para todos los intentos de hashing, ya que parte del resultado permanece inalterado, lo que acelera el trabajo de los mineros.