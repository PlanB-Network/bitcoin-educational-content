---
term: ANONSETS (CONJUNTOS DE ANONIMATO)

---
Os anonsets servem como indicadores para avaliar o nível de privacidade de um determinado UTXO. Mais especificamente, medem o número de UTXOs indistinguíveis dentro do conjunto que inclui a moeda em estudo. Uma vez que é necessário um grupo de UTXOs idênticos, os anonsets são geralmente calculados dentro de um ciclo de coinjoins. Permitem, quando apropriado, avaliar a qualidade dos coinjoins. Um anonset grande significa um maior nível de anonimato, uma vez que se torna difícil distinguir um UTXO específico dentro do conjunto. Existem dois tipos de anonsets:


- O conjunto de anonimato prospetivo;
- O conjunto de anonimato retrospetivo.

O primeiro indica o tamanho do grupo entre o qual o UTXO estudado está escondido, conhecendo o UTXO na entrada. Este indicador permite medir a resistência da privacidade da moeda contra uma análise do passado para o presente (input para output). Em inglês, o nome deste indicador é "*forward anonset*", ou "*forward-looking metrics*"

![](../../dictionnaire/assets/39.webp)

O segundo indica o número de fontes possíveis para uma dada moeda, conhecendo o UTXO na saída. Este indicador permite medir a resistência da privacidade da moeda contra uma análise do presente para o passado (saída para entrada). Em inglês, o nome deste indicador é "*backward anonset*", ou "*backward-looking metrics*"

![](../../dictionnaire/assets/40.webp)

> ► *Em francês, é geralmente aceite a utilização do termo "anonset" No entanto, pode ser traduzido como "ensemble d'anonymat" ou "potentiel d'anonymat" Tanto em inglês como em francês, o termo "score" é também por vezes utilizado para designar anonsets (prospective score e retrospective score).*