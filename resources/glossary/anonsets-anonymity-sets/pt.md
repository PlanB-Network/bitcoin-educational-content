---
term: Anonsets (anonymity sets)

definition: Indicadores que medem o grau de privacidade de um UTXO contando o número de UTXOs indistinguíveis em um conjunto, geralmente após um coinjoin.
---
Os anonsets servem como indicadores para avaliar o grau de confidencialidade de um UTXO específico. Mais especificamente, medem o número de UTXOs indistinguíveis dentro do conjunto que inclui a moeda em análise. Como é necessário dispor de um grupo de UTXOs idênticos, os anonsets são geralmente calculados no âmbito de um ciclo de coinjoins. Permitem, quando aplicável, avaliar a qualidade dos coinjoins. Um anonset de grande dimensão implica um nível mais elevado de anonimato, pois torna-se difícil distinguir um UTXO específico dentro do conjunto.

Existem dois tipos de anonsets: o forward anonset (forward-looking metrics); e o backward anonset (backward-looking metrics). O termo "*score*" também é por vezes utilizado para designar os anonsets.

O primeiro indica o tamanho do grupo no qual o UTXO analisado em saída se esconde, dado o UTXO em entrada. Este indicador permite medir a resistência da confidencialidade da moeda face a uma análise do passado para o presente (da entrada para a saída). O segundo indica o número de fontes possíveis para uma determinada moeda, dado o UTXO em saída. Este indicador permite medir a resistência da confidencialidade da moeda face a uma análise do presente para o passado (da saída para a entrada).










