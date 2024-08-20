---
term: CHAIN CODE
---

No contexto da derivação hierárquica determinística (HD) de carteiras Bitcoin, o chain code é um valor de sal criptográfico de 256 bits usado para gerar chaves filhas a partir de uma chave pai, de acordo com o padrão BIP32. O chain code é usado em combinação com a chave pai e o índice do filho para gerar deterministicamente um novo par de chaves (chave privada e chave pública) sem revelar a chave pai ou outras chaves filhas derivadas.

Portanto, existe um chain code único para cada par de chaves. O chain code é obtido ou pela hash da semente da carteira e pegando a metade direita dos bits. Neste caso, é referido como um master chain code, associado à chave privada mestre. Alternativamente, pode ser obtido fazendo a hash de uma chave pai com seu chain code pai e um índice, mantendo então os bits da direita. Isso é então referido como um child chain code.

É impossível derivar chaves sem conhecer o chain code associado a cada par pai. Ele introduz dados pseudo-aleatórios no processo de derivação para garantir que a geração de chaves criptográficas permaneça imprevisível para os atacantes, enquanto é determinística para o detentor da carteira.

> ► *Em inglês, um "code de chaîne" é chamado de "chain code", e um "code de chaîne maître" é chamado de "master chain code".*