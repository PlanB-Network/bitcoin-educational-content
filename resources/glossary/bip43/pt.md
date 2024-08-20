---
termo: BIP43
---

Proposta de melhoria que introduz o uso de um nível de caminho de derivação para descrever o campo de propósito na estrutura das carteiras HD, previamente introduzido no BIP32. De acordo com o BIP43, o primeiro nível de derivação de uma carteira HD, logo após a chave mestra denotada como `m/`, é reservado para o número de propósito, que indica o padrão de derivação usado para o restante do caminho. Esse número é registrado como um índice endurecido. Por exemplo, se a carteira segue o padrão SegWit (BIP84), o início do seu caminho de derivação seria: `m/84'/`. O BIP43, portanto, permite a clarificação dos padrões aderidos por cada software de carteira para ter melhor interoperabilidade entre eles. A padronização do restante do caminho de derivação é descrita no BIP44.