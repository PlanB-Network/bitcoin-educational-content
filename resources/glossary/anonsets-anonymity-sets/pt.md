---
termo: ANONSETS (CONJUNTOS DE ANONIMATO)
---

Os anonsets servem como indicadores para avaliar o nível de privacidade de um UTXO específico. Mais especificamente, eles medem o número de UTXOs indistinguíveis dentro do conjunto que inclui a moeda em estudo. Uma vez que um grupo de UTXOs idênticos é necessário, os anonsets são geralmente calculados dentro de um ciclo de coinjoins. Eles permitem, quando apropriado, julgar a qualidade dos coinjoins. Um grande anonset significa um aumento no nível de anonimato, pois torna-se difícil distinguir um UTXO específico dentro do conjunto. Existem dois tipos de anonsets:
* O conjunto de anonimato prospectivo;
* O conjunto de anonimato retrospectivo.

O primeiro indica o tamanho do grupo entre o qual o UTXO estudado está escondido, conhecendo o UTXO na entrada. Este indicador permite medir a resistência da privacidade da moeda contra uma análise do passado para o presente (entrada para saída). Em inglês, o nome deste indicador é “*forward anonset*,” ou “*forward-looking metrics*.”

![](../../dictionnaire/assets/39.png)

O segundo indica o número de possíveis fontes para uma dada moeda, conhecendo o UTXO na saída. Este indicador permite medir a resistência da privacidade da moeda contra uma análise do presente para o passado (saída para entrada). Em inglês, o nome deste indicador é “*backward anonset*,” ou “*backward-looking metrics*.”

![](../../dictionnaire/assets/40.png)

> ► *Em francês, geralmente aceita-se usar o termo “anonset.” No entanto, poderia ser traduzido como “ensemble d'anonymat” ou “potentiel d'anonymat.” Tanto em inglês quanto em francês, o termo “score” também é às vezes usado para se referir a anonsets (prospective score e retrospective score).*