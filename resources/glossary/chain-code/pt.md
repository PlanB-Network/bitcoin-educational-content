---
term: CÓDIGO DE CADEIA

---
No contexto da derivação hierárquica determinística (HD) das carteiras Bitcoin, o código da cadeia é um valor de sal criptográfico de 256 bits utilizado para gerar chaves-filhas a partir de uma chave-mãe, de acordo com a norma BIP32. O código da cadeia é utilizado em combinação com a chave-mãe e o índice da criança para gerar deterministicamente um novo par de chaves (chave privada e chave pública) sem revelar a chave-mãe ou outras chaves-filhas derivadas.

Por conseguinte, existe um código de cadeia único para cada par de chaves. O código da cadeia é obtido através do hashing da semente da carteira e retirando a metade direita dos bits. Neste caso, é referido como um código de cadeia principal, associado à chave privada principal. Em alternativa, pode ser obtido através do hashing de uma chave-mãe com o seu código de cadeia-mãe e um índice, mantendo depois os bits corretos. Este é então referido como um código de cadeia filho.

É impossível derivar chaves sem conhecer o código da cadeia associado a cada par de pais. Introduz dados pseudo-aleatórios no processo de derivação para garantir que a geração de chaves criptográficas permaneça imprevisível para os atacantes e, ao mesmo tempo, determinística para o titular da carteira.

> ► *Em inglês, um "code de chaîne" é designado por "chain code" e um "code de chaîne maître" por "master chain code".*