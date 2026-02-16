---
term: Anonsets (anonymity sets)

definition: Indicadores que miden el grado de privacidad de un UTXO contando el número de UTXOs indistinguibles en un conjunto, típicamente después de un coinjoin.
---
Los anonsets sirven como indicadores para evaluar el grado de confidencialidad de un UTXO concreto. Más específicamente, miden el número de UTXO indistinguibles dentro del conjunto que incluye la moneda estudiada. Dado que es necesario disponer de un grupo de UTXO idénticos, los anonsets suelen calcularse dentro de un ciclo de coinjoins. Permiten, en su caso, evaluar la calidad de los coinjoins. Un anonset de gran tamaño implica un mayor nivel de anonimato, ya que resulta difícil distinguir un UTXO específico dentro del conjunto.

Existen dos tipos de anonsets: el forward anonset (forward-looking metrics); y el backward anonset (backward-looking metrics). El término "*score*" también se utiliza a veces para designar los anonsets.

El primero indica el tamaño del grupo dentro del cual se oculta el UTXO estudiado en salida, conociendo el UTXO de entrada. Este indicador permite medir la resistencia de la confidencialidad de la moneda frente a un análisis del pasado al presente (de entrada a salida). El segundo indica el número de fuentes posibles para una moneda determinada, conociendo el UTXO de salida. Este indicador permite medir la resistencia de la confidencialidad de la moneda frente a un análisis del presente al pasado (de salida a entrada).










