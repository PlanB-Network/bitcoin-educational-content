---
term: ANONSETS (CONJUNTOS DE ANONIMATO)
---

Los anonsets sirven como indicadores para evaluar el nivel de privacidad de un UTXO particular. Más específicamente, miden el número de UTXOs indistinguibles dentro del conjunto que incluye la moneda en estudio. Dado que se requiere un grupo de UTXOs idénticos, los anonsets generalmente se calculan dentro de un ciclo de coinjoins. Permiten, cuando es apropiado, juzgar la calidad de los coinjoins. Un gran anonset significa un aumento en el nivel de anonimato, ya que se vuelve difícil distinguir un UTXO específico dentro del conjunto. Hay dos tipos de anonsets:
* El conjunto de anonimato prospectivo;
* El conjunto de anonimato retrospectivo.

El primero indica el tamaño del grupo entre el cual se oculta el UTXO estudiado, conociendo el UTXO en la entrada. Este indicador permite medir la resistencia de la privacidad de la moneda contra un análisis de pasado a presente (entrada a salida). En inglés, el nombre de este indicador es “*forward anonset*,” o “*forward-looking metrics*.”

![](../../dictionnaire/assets/39.png)

El segundo indica el número de fuentes posibles para una moneda dada, conociendo el UTXO en la salida. Este indicador permite medir la resistencia de la privacidad de la moneda contra un análisis de presente a pasado (salida a entrada). En inglés, el nombre de este indicador es “*backward anonset*,” o “*backward-looking metrics*.”

![](../../dictionnaire/assets/40.png)

> ► *En francés, generalmente se acepta usar el término “anonset”. Sin embargo, podría traducirse como “ensemble d'anonymat” o “potentiel d'anonymat”. Tanto en inglés como en francés, el término “score” también se usa a veces para referirse a los anonsets (puntuación prospectiva y puntuación retrospectiva).*