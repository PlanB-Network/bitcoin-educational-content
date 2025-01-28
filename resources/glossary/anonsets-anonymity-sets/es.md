---
term: ANONSETS (CONJUNTOS DE ANONIMATO)

---
Los anonsets sirven como indicadores para evaluar el nivel de privacidad de un UTXO concreto. Más concretamente, miden el número de UTXO indistinguibles dentro del conjunto que incluye la moneda objeto de estudio. Dado que se requiere un grupo de UTXO idénticos, los anonsets se calculan generalmente dentro de un ciclo de coinjoins. Permiten, en su caso, juzgar la calidad de los coinjoins. Un anonset grande significa un mayor nivel de anonimato, ya que resulta difícil distinguir un UTXO específico dentro del conjunto. Existen dos tipos de anonsets:


- El conjunto de anonimato prospectivo;
- El conjunto de anonimato retrospectivo.

El primero indica el tamaño del grupo entre los que se oculta el UTXO estudiado, conociendo el UTXO a la entrada. Este indicador permite medir la resistencia de la privacidad de la moneda frente a un análisis del pasado al presente (de la entrada a la salida). En inglés, el nombre de este indicador es "*forward anonset*", o "*métrica prospectiva*"

![](../../dictionnaire/assets/39.webp)

El segundo indica el número de fuentes posibles para una moneda determinada, conociendo el UTXO a la salida. Este indicador permite medir la resistencia de la privacidad de la moneda frente a un análisis del presente al pasado (de la salida a la entrada). En inglés, el nombre de este indicador es "*backward anonset*", o "*métrica hacia atrás*"

![](../../dictionnaire/assets/40.webp)

> ► *En francés, está generalmente aceptado utilizar el término "anonset" Sin embargo, podría traducirse como "ensemble d'anonymat" o "potentiel d'anonymat" Tanto en inglés como en francés, a veces también se utiliza el término "score" para referirse a los anonsets (prospective score y retrospective score).*