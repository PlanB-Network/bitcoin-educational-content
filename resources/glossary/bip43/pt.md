---
term: BIP43

---
Proposta de melhoria que introduz a utilização de um nível de caminho de derivação para descrever o campo de objetivo na estrutura das carteiras HD, previamente introduzido na BIP32. De acordo com a BIP43, o primeiro nível de derivação de uma carteira HD, logo após a chave mestra denotada como `m/`, é reservado para o número de objetivo que indica o padrão de derivação utilizado para o resto do caminho. Este número é registado como um índice endurecido. Por exemplo, se a carteira segue o padrão SegWit (BIP84), o início do seu caminho de derivação seria: `m/84'/`. O BIP43 permite assim clarificar as normas seguidas por cada software de carteira para que haja uma melhor interoperabilidade entre eles. A normalização do resto do caminho de derivação é descrita no BIP44.