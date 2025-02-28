---
term: SEED (BITCOIN)

---
No contexto do Bitcoin, uma semente é um valor de 512 bits utilizado para derivar todas as chaves privadas e públicas associadas a uma carteira HD (Hierarchical Deterministic). Tecnicamente, a semente é um valor diferente da frase de recuperação (ou mnemónica). A frase, que é normalmente composta por 12 ou 24 palavras, é gerada de forma pseudo-aleatória a partir de uma fonte de entropia e completada por uma soma de controlo. Esta frase facilita o backup humano ao fornecer uma representação textual do valor na base da carteira.

Para obter a semente efectiva, a frase de recuperação, possivelmente acompanhada por uma frase-chave opcional, é processada através do algoritmo PBKDF2 (*Função de Derivação de Chave Baseada em Palavra-Passe 2*). O resultado deste cálculo é uma semente de 512 bits. É esta semente que é utilizada para gerar deterministicamente a chave mestra, e depois todo o conjunto de chaves para a carteira HD, de acordo com o BIP32.

![](../../dictionnaire/assets/31.webp)

> ► *No entanto, na linguagem comum, a maioria dos bitcoiners refere-se à frase mnemónica quando falam da "semente", e não ao estado intermédio de derivação que se situa entre a frase mnemónica e a chave-mestra.*