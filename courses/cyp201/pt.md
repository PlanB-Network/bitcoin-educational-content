---
name: Introdução aos algoritmos criptográficos do Bitcoin
goal: Compreender a criação de uma carteira de Bitcoin do ponto de vista criptográfico
objectives:
  - Desmistificar a terminologia criptográfica relacionada ao Bitcoin.
  - Dominar a criação de uma carteira de Bitcoin.
  - Compreender a estrutura de uma carteira de Bitcoin.
  - Compreender endereços e caminhos de derivação.
---

# Uma Jornada pela Criptografia

Você é fascinado pelo Bitcoin? Está se perguntando como uma carteira de Bitcoin funciona? Prepare-se para embarcar em uma cativante jornada pela criptografia! Loïc, nosso especialista, irá guiá-lo pelas complexidades da criação de uma carteira de Bitcoin, desvendando os mistérios por trás de termos técnicos intimidadores como hash, derivação de chaves e curvas elípticas.

Este treinamento não apenas fornecerá o conhecimento necessário para compreender a estrutura de uma carteira de Bitcoin, mas também o preparará para se aprofundar no emocionante mundo da criptografia. Então, está pronto para embarcar nessa jornada? Junte-se a nós e transforme sua curiosidade em expertise!

+++

# Introdução
<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>

## Introdução à Criptografia
<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>

### Este treinamento é para você? SIM!

É um prazer recebê-lo no novo curso de treinamento intitulado "Crypto 301: Introdução à Criptografia e Carteira HD", ministrado pelo especialista no assunto, Loïc Morel. Este curso irá mergulhá-lo no fascinante mundo da criptografia, a disciplina fundamental da matemática que garante a criptografia e segurança de seus dados.

Em nossas vidas diárias, e especialmente no mundo do Bitcoin, a criptografia desempenha um papel crucial. Conceitos relacionados à criptografia, como chaves privadas, chaves públicas, endereços, caminhos de derivação, semente e entropia, estão no cerne do uso e criação de uma carteira de Bitcoin. Ao longo deste curso, Loïc explicará em detalhes como as chaves privadas são geradas e como estão vinculadas aos endereços. Loïc também dedicará uma hora para explicar os detalhes matemáticos das curvas elípticas. Além disso, você entenderá por que o uso do HMAC SHA512 é importante para a segurança de sua carteira e qual a diferença entre uma semente e uma frase mnemônica.

O objetivo final deste treinamento é capacitar você a compreender os processos técnicos envolvidos na criação de uma carteira HD e os métodos criptográficos utilizados. Ao longo dos anos, as carteiras de Bitcoin evoluíram para se tornarem mais fáceis de usar, mais seguras e padronizadas graças a BIPs específicos. Loïc ajudará você a entender esses BIPs para compreender as escolhas feitas pelos desenvolvedores de Bitcoin e criptógrafos. Assim como todos os treinamentos oferecidos por nossa universidade, este é completamente gratuito e de código aberto. Isso significa que você é livre para fazê-lo e usá-lo como desejar. Esperamos receber seus comentários ao final deste emocionante curso.

### A palavra é sua, professor!

Olá a todos, sou Loïc Morel, seu guia nesta exploração técnica da criptografia usada em carteiras de Bitcoin.

Nossa jornada começa com uma imersão nas profundezas das funções hash criptográficas. Juntos, vamos dissecar o funcionamento interno do essencial SHA256 e explorar vários algoritmos dedicados à derivação.

Continuaremos nossa aventura decifrando o misterioso mundo das assinaturas digitais. Você descobrirá como a magia das curvas elípticas se aplica a essas assinaturas, e lançaremos luz sobre como calcular a chave pública a partir da chave privada. E, é claro, nos aprofundaremos no processo de assinatura digital.
Em seguida, voltaremos no tempo para ver a evolução das carteiras de Bitcoin e nos aventuraremos nos conceitos de entropia e números aleatórios. Vamos revisar a famosa frase mnemônica, enquanto também abordamos a frase secreta. Você até terá a oportunidade de experimentar algo único criando uma semente a partir de 128 rolagens de dados!

Com essas bases sólidas, estaremos prontos para a parte crucial: criar uma carteira de Bitcoin. Desde o nascimento da semente e da chave mestra, até o estudo das chaves estendidas e a derivação de pares de chaves filhas, cada etapa será dissecada. Também discutiremos a estrutura da carteira e os caminhos de derivação.

Para completar, concluiremos nossa jornada examinando os endereços de Bitcoin. Explicaremos como eles são criados e como desempenham um papel essencial no funcionamento das carteiras de Bitcoin.

Junte-se a mim nesta jornada cativante e prepare-se para explorar o mundo da criptografia como nunca antes. Deixe seus preconceitos na porta e abra sua mente para uma nova forma de entender o Bitcoin e sua estrutura fundamental.

# Funções de Hash
<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>

## Introdução às funções de hash criptográficas relacionadas ao Bitcoin
<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>

Bem-vindo à sessão de hoje dedicada a uma imersão profunda no mundo criptográfico das funções de hash, um pilar crucial da segurança do protocolo Bitcoin. Imagine uma função de hash como um robô decifrador criptográfico ultraeficiente que transforma informações de qualquer tamanho em uma impressão digital digital única e de tamanho fixo, chamada de "hash", "digest" ou "checksum".
Em resumo, uma função de hash recebe uma mensagem de entrada de tamanho arbitrário e a converte em uma impressão digital de tamanho fixo.

Descrever o perfil das funções de hash criptográficas requer entender duas qualidades essenciais: sua irreversibilidade e sua resistência à falsificação.

A irreversibilidade, ou resistência à pré-imagem, significa que calcular a saída dado a entrada pode ser feito facilmente, mas calcular a entrada a partir da saída é impossível.
É uma função unidirecional.

![imagem](assets/image/section1/0.webp)

A resistência à falsificação vem do fato de que mesmo a menor modificação da entrada resultará em uma saída profundamente diferente.
Essas funções permitem verificar a integridade de software baixado.

![imagem](assets/image/section1/1.webp)

Outra característica crucial que possuem é a resistência a colisões e segunda pré-imagem. Uma colisão ocorre quando duas entradas distintas produzem a mesma saída.
Certamente, no universo das funções de hash, colisões são inevitáveis, mas uma excelente função de hash criptográfica as minimiza significativamente. O risco deve ser tão baixo que possa ser considerado negligível. É como se cada hash fosse uma casa em uma cidade vasta; apesar do enorme número de casas, uma boa função de hash garante que cada casa tenha um endereço único.

A resistência à segunda pré-imagem depende da resistência a colisões; se houver resistência a colisões, então há resistência à segunda pré-imagem.
Dada uma informação de entrada que nos é imposta, devemos encontrar uma segunda entrada, diferente da primeira, que produza uma colisão no hash de saída da função. A resistência à segunda pré-imagem é semelhante à resistência a colisões, exceto que a entrada é imposta.
Agora vamos navegar pelas águas tumultuadas das funções de hash desatualizadas. SHA0, SHA1 e MD5 agora são considerados cascas enferrujadas no oceano da criptografia de hash. Eles são frequentemente desencorajados, pois perderam sua resistência a colisões. O princípio da gaiola de pombo explica por que, apesar de nossos melhores esforços, a evitação de colisões é impossível devido à limitação do tamanho da saída. Para ser verdadeiramente considerada segura, uma função de hash deve resistir a colisões, segundas pré-imagens e pré-imagens.

Um elemento-chave no protocolo Bitcoin, a função de hash SHA-256 é o capitão do navio. Outras funções, como SHA-512, são usadas para derivação com HMAC e PBKDF. Além disso, o RIPMD160 é usado para reduzir uma impressão digital para 160 bits. Quando nos referimos a HASH256 e HASH160, estamos nos referindo ao uso de hash duplo com SHA-256 e RIPMD.

Para HASH256, é um hash duplo da mensagem usando a função SHA256.
$$
SHA256(SHA256(mensagem))
$$
Para HASH160, é um hash duplo da mensagem usando primeiro o SHA256 e depois o RIPMD160.
$$
RIPMD160(SHA256(mensagem))
$$
O uso de HASH160 é particularmente vantajoso, pois permite a segurança do SHA-256 enquanto reduz o tamanho da impressão digital.

Em resumo, o objetivo final de uma função de hash criptográfica é transformar informações de tamanho arbitrário em uma impressão digital de tamanho fixo. Para ser reconhecida como segura, ela deve ter várias características: irreversibilidade, resistência a adulteração, resistência a colisões e resistência a segundas pré-imagens.

![imagem](assets/image/section1/2.webp)

Ao final desta exploração, desmistificamos as funções de hash criptográficas, destacamos seus usos no protocolo Bitcoin e analisamos seus objetivos específicos. Aprendemos que, para as funções de hash serem consideradas seguras, elas devem ser resistentes a pré-imagens, segundas pré-imagens, colisões e adulteração. Também abordamos a variedade de diferentes funções de hash usadas no protocolo Bitcoin. Em nossa próxima sessão, iremos aprofundar no núcleo da função de hash SHA256 e descobrir a matemática fascinante que lhe confere suas características únicas.

## O Funcionamento Interno do SHA256
<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>

Bem-vindo à continuação de nossa fascinante jornada pelos labirintos criptográficos da função de hash. Hoje, revelamos os mistérios do SHA256, um processo complexo, porém engenhoso, que introduzimos anteriormente.
-> 950 + 1 + P + 64 = 1024-> P = 1024 - 1 - 64 - 950
-> P = 9

Portanto, 9 bits de preenchimento precisam ser adicionados para ter uma mensagem igualada a um múltiplo de 512.

E agora?
Logo após a mensagem inicial, o separador 1 seguido por P, que em nosso exemplo são nove 0s, precisa ser adicionado.

mensagem + 1 000 000 000

#### Preenchimento de Tamanho

Agora passamos para a segunda fase de pré-processamento, que envolve adicionar a representação binária do tamanho da mensagem inicial em bits.

Vamos revisitar o exemplo com uma entrada de 950 bits:

A representação binária do número 950 é: 11 1011 0110

Usamos nossos 64 bits reservados da etapa anterior. Adicionamos zeros para arredondar nossos 64 bits para nossa entrada igualada. Em seguida, mesclamos a mensagem inicial, os bits de preenchimento e o preenchimento de tamanho para obter nossa entrada igualada.

Aqui está o resultado:

![image](assets/image/section1/4.webp)

### Processamento

#### Compreendendo os Pré-requisitos

##### Constantes e Vetores de Inicialização
Agora, estamos nos preparando para as etapas iniciais do processamento da função SHA-256. Assim como em qualquer boa receita, precisamos de alguns ingredientes básicos, que chamamos de constantes e vetores de inicialização.

Os vetores de inicialização, de A a H, são os primeiros 32 bits das partes decimais das raízes quadradas dos primeiros 8 números primos. Eles servirão como valores base nas etapas iniciais do processamento. Seus valores estão em formato hexadecimal.

As constantes K, de 0 a 63, representam os primeiros 32 bits das partes decimais das raízes cúbicas dos primeiros 64 números primos. Elas são usadas em cada rodada da função de compressão. Seus valores também estão em formato hexadecimal.

![image](assets/image/section1/5.webp)

##### Operações Utilizadas

Dentro da função de compressão, usamos operadores específicos como XOR, AND e NOT. Processamos os bits um por um de acordo com sua posição, usando o operador XOR e uma tabela verdade. O operador AND é usado para retornar 1 apenas se ambos os operandos forem iguais a 1, e o operador NOT é usado para retornar o valor oposto de um operando. Também usamos a operação SHR para deslocar os bits para a direita por um número escolhido.

A tabela verdade:

![image](assets/image/section1/6.webp)

Operações de deslocamento de bits:

![image](assets/image/section1/7.webp)

#### A Função de Compressão

Antes de aplicar a função de compressão, dividimos a entrada em blocos de 512 bits. Cada bloco será processado independentemente dos outros.

Cada bloco de 512 bits é então dividido em partes de 32 bits chamadas W. Dessa forma, W(0) representa os primeiros 32 bits do bloco de 512 bits. W(1) representa os próximos 32 bits, e assim por diante, até chegarmos aos 512 bits do bloco.

Uma vez definidas todas as constantes K e as partes W, podemos realizar os seguintes cálculos para cada parte W em cada rodada.

Realizamos 64 rodadas de cálculos na função de compressão. Na última rodada, no nível "Saída da função", teremos um estado intermediário que será adicionado ao estado inicial da função de compressão.

Em seguida, repetimos todos esses passos da função de compressão no próximo bloco de 512 bits, até o último bloco.
Todas as adições na função de compressão são adições módulo 2^32 para manter sempre uma soma de 32 bits.
![image](assets/image/section1/9.webp)

![image](assets/image/section1/8.webp)

##### Uma Rodada da Função de Compressão

![image](assets/image/section1/11.webp)

![image](assets/image/section1/10.webp)
A função de compressão será executada 64 vezes. Temos nossas peças W e nossas constantes K previamente definidas como entrada.
Os quadrados/cruzes vermelhos correspondem a uma adição módulo 2^32 de 32 bits.

As entradas A, B, C, D, E, F, G, H serão associadas a um valor de 32 bits para totalizar 32 * 8 = 256 bits.
Também temos uma nova sequência A, B, C, D, E, F, G, H como saída. Essa saída será então usada como entrada para a próxima rodada e assim por diante até o final da 64ª rodada.

Os valores da sequência de entrada para a primeira rodada da função de compressão correspondem aos vetores de inicialização predefinidos mencionados anteriormente.
Como lembrete, os vetores de inicialização representam os primeiros 32 bits das partes decimais das raízes quadradas dos primeiros 8 números primos.

Aqui está um exemplo de uma rodada:

![image](assets/image/section1/12.1.webp)

##### Estado Intermediário

Como lembrete, a mensagem é dividida em blocos de 512 bits, que são então divididos em peças de 32 bits. Para cada bloco de 512 bits, aplicamos as 64 rodadas da função de compressão.
O estado intermediário corresponde ao final das 64 rodadas de um bloco. Os valores da sequência de saída dessa 64ª rodada são usados como valores iniciais para a sequência de entrada da primeira rodada do próximo bloco.

![image](assets/image/section1/12.2.webp)

#### Visão geral da função hash

![image](assets/image/section1/13.webp)

Podemos observar que a saída da primeira peça de mensagem de 512 bits corresponde aos nossos vetores de inicialização como entrada para a segunda peça de mensagem de 512 bits, e assim por diante.

A saída da última rodada, da última peça, corresponde ao resultado final da função SHA256.

Em conclusão, gostaríamos de enfatizar o papel crucial dos cálculos realizados nas caixas CH, MAJ, σ0 e σ1. Essas operações, entre outras, são os guardiões que garantem a robustez da função hash SHA256 contra ataques, tornando-a uma escolha preferida para garantir muitos sistemas digitais, especialmente dentro do protocolo Bitcoin. É evidente que, embora complexa, a beleza do SHA256 reside em sua capacidade de encontrar a entrada a partir do hash, enquanto verificar o hash para uma determinada entrada é uma ação mecanicamente simples.

## Os algoritmos usados para derivação
<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>

Os algoritmos de derivação HMAC e PBKDF2 são componentes-chave no mecanismo de segurança do protocolo Bitcoin. Eles impedem uma variedade de ataques potenciais e garantem a integridade das carteiras de Bitcoin.
HMAC e PBKDF2 são ferramentas criptográficas usadas para várias tarefas no Bitcoin. HMAC é usado principalmente para combater ataques de extensão de comprimento ao derivar carteiras Determinísticas Hierárquicas (HD), enquanto PBKDF2 é usado para converter uma frase mnemônica em uma semente.

#### HMAC-SHA512

O par HMAC-SHA512 tem duas entradas: uma mensagem m (Entrada 1) e uma chave K escolhida arbitrariamente pelo usuário (Entrada 2). Ele também tem uma saída de tamanho fixo: 512 bits.

Vamos observar:
- m: mensagem de tamanho arbitrário escolhida pelo usuário (entrada 1)
- K: chave arbitrária escolhida pelo usuário (entrada 2)
- K': chave igualada K. Foi ajustada para o tamanho B dos blocos.
- ||: operação de concatenação.
- opad: constante definida pelo byte 0x5c repetido B vezes.
- ipad: constante definida pelo byte 0x36 repetido B vezes.
- B: O tamanho dos blocos da função hash utilizada.


HMAC-SHA512, que recebe uma mensagem e uma chave como entradas, gera uma saída de tamanho fixo. Para garantir a uniformidade, a chave é ajustada com base no tamanho dos blocos usados na função hash. No contexto da derivação de carteira HD, é utilizado o HMAC-SHA-512. Ele opera com blocos de 1024 bits (128 bytes) e ajusta a chave de acordo. Ele utiliza as constantes OPAD (0x5c) e IPAD (0x36), repetidas conforme necessário para aumentar a segurança.

O processo HMAC-SHA-512 envolve a concatenação do resultado de SHA-512 aplicado à chave XOR OPAD e a chave XOR IPAD com a mensagem. Quando usado com blocos de 1024 bits (128 bytes), a chave de entrada é preenchida com zeros, se necessário, e depois XORed com IPAD e OPAD. A chave modificada é então concatenada com a mensagem.

A inclusão de um salt no código da string aumenta a segurança das chaves derivadas. Sem ele, um ataque poderia comprometer toda a carteira e roubar todos os bitcoins.

O PBKDF2 é usado para converter uma frase mnemônica em uma semente. Esse algoritmo realiza 2048 rodadas usando o HMAC SHA512. Através desses algoritmos de derivação, diferentes entradas podem produzir uma saída única e fixa, o que mitiga o problema de possíveis ataques de extensão de comprimento em funções da família SHA-2.
Um ataque de extensão de comprimento explora uma propriedade específica de certas funções hash criptográficas. Em tal ataque, um atacante que já possui o hash de uma mensagem desconhecida pode usá-lo para calcular o hash de uma mensagem mais longa, que é uma extensão da mensagem original. Isso muitas vezes é possível sem conhecer o conteúdo da mensagem original, o que pode levar a vulnerabilidades significativas de segurança se esse tipo de função hash for usado para tarefas como verificação de integridade.

Em conclusão, os algoritmos HMAC e PBKDF2 desempenham papéis essenciais na segurança da derivação de carteira HD no protocolo Bitcoin. O HMAC-SHA-512 é usado para proteger contra ataques de extensão de comprimento, enquanto o PBKDF2 permite a conversão da frase mnemônica em uma semente. O código da string adiciona uma fonte adicional de entropia na derivação de chaves, garantindo a robustez do sistema.

# Assinaturas Digitais
<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>

## Assinaturas Digitais e Curvas Elípticas
<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>

Onde estão armazenados esses famosos bitcoins? Não em uma carteira de Bitcoin, como se poderia pensar. Na realidade, uma carteira de Bitcoin armazena as chaves privadas necessárias para provar a propriedade dos bitcoins. Os próprios bitcoins são registrados no blockchain, um banco de dados descentralizado que arquiva todas as transações.
No sistema Bitcoin, a unidade de conta é o bitcoin (observe o "b" minúsculo). Ele é divisível em até oito casas decimais, sendo a menor unidade o satoshi. UTXOs, ou "Unspent Transaction Outputs" (Saídas de Transações Não Gastas), representam as saídas de transações não gastas pertencentes a uma chave pública que está matematicamente vinculada a uma chave privada. Para gastar esses bitcoins, é necessário satisfazer a condição de gasto da transação. Uma condição de gasto típica envolve provar para o restante da rede que o usuário é o legítimo proprietário da chave pública associada ao UTXO. Para fazer isso, o usuário deve demonstrar a posse da chave privada correspondente à chave pública vinculada a cada UTXO sem revelar a chave privada.

É aí que entra a assinatura digital. Ela serve como prova matemática da posse de uma chave privada associada a uma chave pública específica. Essa técnica de proteção de dados é baseada principalmente em um fascinante campo da criptografia chamado criptografia de curva elíptica (ECC).

A assinatura pode ser verificada matematicamente por outros participantes na rede Bitcoin.

![image](assets/image/section2/0.webp)

Para garantir a segurança das transações, o Bitcoin depende de dois protocolos de assinatura digital: ECDSA (Elliptic Curve Digital Signature Algorithm - Algoritmo de Assinatura Digital de Curva Elíptica) e Schnorr. O ECDSA é um protocolo de assinatura integrado ao Bitcoin desde o seu lançamento em 2009, enquanto as assinaturas Schnorr foram adicionadas mais recentemente em novembro de 2021. Embora ambos os protocolos sejam baseados em criptografia de curva elíptica e usem mecanismos matemáticos semelhantes, eles diferem principalmente em termos de estrutura de assinatura.

Neste curso, apresentaremos o algoritmo ECDSA.

### O que é uma curva elíptica?

A criptografia de curva elíptica é um conjunto de algoritmos que usam uma curva elíptica por suas várias propriedades geométricas e matemáticas em um contexto criptográfico, com segurança baseada na dificuldade de calcular o logaritmo discreto.

As curvas elípticas são úteis em uma variedade de aplicações criptográficas no protocolo Bitcoin, desde trocas de chaves até criptografia assimétrica e assinaturas digitais.

As curvas elípticas possuem propriedades interessantes:

- Simetria: Qualquer linha não vertical que intersecta dois pontos na curva elíptica irá intersectar a curva em um terceiro ponto.
- Qualquer linha não vertical tangente à curva em um ponto sempre intersectará a curva em um segundo ponto único.

O protocolo Bitcoin utiliza uma curva elíptica específica chamada Secp256k1 para suas operações criptográficas.

Antes de aprofundarmos nesses mecanismos de assinatura, é importante entender o que é uma curva elíptica. Uma curva elíptica é definida pela equação y² = x³ + ax + b. Cada ponto nessa curva possui uma simetria distintiva que é fundamental para sua utilidade em criptografia.

![image](assets/image/section2/1.webp)

No final, várias curvas elípticas são reconhecidas como seguras para uso criptográfico. A mais conhecida pode ser a curva secp256r1. No entanto, para o Bitcoin, Satoshi Nakamoto optou por uma curva diferente: secp256k1.

Essa curva é definida pelos parâmetros a=0 e b=7, e sua equação é y² = x³ + 7 módulo n, onde n representa o número primo que determina a ordem da curva.

![image](assets/image/section2/2.webp)

A primeira imagem representa a curva secp256k1 sobre o campo real e sua equação.
A segunda imagem é uma representação da curva secp256k1 sobre o campo ZP, o campo dos números naturais positivos, módulo p onde p é um número primo. Parece uma nuvem de pontos. Usamos esse campo de números naturais positivos para evitar aproximações.
p é um número primo e é a ordem da curva que é usada.
Finalmente, a equação usada no protocolo Bitcoin é: $$y^2 = (x^3 + 7) mod(p)$$ A equação da curva elíptica no Bitcoin corresponde à última equação na imagem anterior.

Na próxima seção deste curso, usaremos curvas que estão no campo real apenas para facilitar a compreensão.

## Calculando a chave pública a partir da chave privada
<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>

Para começar, vamos mergulhar no mundo do Algoritmo de Assinatura Digital de Curva Elíptica (ECDSA). O Bitcoin utiliza esse algoritmo de assinatura digital para vincular chaves privadas e públicas. Nesse sistema, a chave privada é um número aleatório ou pseudo-aleatório de 256 bits. O número total de possibilidades para uma chave privada é teoricamente 2^256, mas na realidade é um pouco menor que isso. Para ser preciso, algumas chaves privadas de 256 bits não são válidas para o Bitcoin.

Para ser compatível com o Bitcoin, uma chave privada deve estar entre 1 e n-1, onde n representa a ordem da curva elíptica. Isso significa que o número total de possibilidades para uma chave privada do Bitcoin é quase igual a 1,158 x 10^77. Para colocar isso em perspectiva, é aproximadamente o mesmo número de átomos presentes no universo observável.

![imagem](assets/image/section2/3.webp)

A chave privada única, denotada como k, é então usada para determinar uma chave pública.

A chave pública, denotada como K, é um ponto na curva elíptica que é derivado da chave privada usando algoritmos irreversíveis como o ECDSA. Quando temos conhecimento da chave privada, é muito fácil recuperar a chave pública, mas quando temos apenas a chave pública, é impossível recuperar a chave privada. Essa irreversibilidade é a base da segurança da carteira Bitcoin.

A chave pública tem 512 bits de comprimento, pois corresponde a um ponto na curva com uma coordenada x de 256 bits e uma coordenada y de 256 bits. No entanto, ela pode ser comprimida em um número de 264 bits.

![imagem](assets/image/section2/4.webp)

O ponto gerador (G) é o ponto na curva a partir do qual todas as chaves públicas são geradas no protocolo Bitcoin. Ele tem coordenadas x e y específicas, geralmente representadas em hexadecimal. Para secp256k1, as coordenadas de G são, em hexadecimal:

- `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
- `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

Este ponto é útil para derivar todas as chaves públicas. Para calcular a chave pública K, basta multiplicar o ponto G pela chave privada k, de forma que: K = k.G

Agora estudaremos como adicionar e multiplicar pontos em curvas elípticas.

#### Adição e duplicação de pontos em curvas elípticas

##### Adicionando dois pontos M + L

Uma das propriedades notáveis das curvas elípticas é que uma linha não vertical que intersecta a curva em dois pontos também a intersectará em um terceiro ponto, chamado ponto O em nosso exemplo. Essa propriedade é usada para determinar o ponto U, que é o oposto do ponto O.

M + L = U

![imagem](assets/image/section2/5.webp)

##### Adicionando um ponto a si mesmo = Duplicação de ponto
Adicionar um ponto G a si mesmo é feito desenhando uma tangente à curva nesse ponto. Essa tangente, de acordo com as propriedades das curvas elípticas, irá intersectar a curva em um segundo ponto único -J. O oposto desse ponto, J, é o resultado de adicionar o ponto G a si mesmo.
G + G = J

Na verdade, o ponto G é o ponto de partida para calcular todas as chaves públicas dos usuários do sistema Bitcoin.

![image](assets/image/section2/6.webp)

#### Multiplicação escalar em curvas elípticas

A multiplicação escalar de um ponto por n é equivalente a adicionar esse ponto a si mesmo n vezes.

Similar à duplicação de ponto, a multiplicação escalar do ponto G por um ponto n é feita desenhando uma tangente à curva no ponto G. Essa tangente, de acordo com as propriedades das curvas elípticas, irá intersectar a curva em um segundo ponto único -2G. O oposto desse ponto, 2G, é o resultado de adicionar o ponto G a si mesmo.

Se n = 4, então a operação é repetida até alcançar 4G.

![image](assets/image/section2/7.webp)

Aqui está um exemplo de cálculo para 3G:

![image](assets/image/section2/8.webp)

Essas operações em pontos de uma curva elíptica são a base para calcular chaves públicas. Derivar uma chave pública conhecendo a chave privada é muito fácil.
Uma chave pública é um ponto na curva elíptica, é o resultado da nossa adição e duplicação do ponto G k vezes. Com k = chave privada.

Neste exemplo:

- A chave privada k = 4
- A chave pública K = kG = 4G

![image](assets/image/section2/9.webp)
Sabendo a chave privada k, é fácil calcular a chave pública K. No entanto, é impossível recuperar a chave privada com base na chave pública. Isso é resultado de uma adição ou duplicação de pontos?

Na nossa próxima lição, exploraremos como uma assinatura digital é criada usando o algoritmo ECDSA com uma chave privada para gastar bitcoins.

## Assinando com a chave privada
<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>

O processo de assinatura digital é um método chave para provar que você é o detentor de uma chave privada sem revelá-la. Isso é alcançado usando o algoritmo ECDSA, que envolve determinar um nonce único, calcular um número específico V e criar uma assinatura digital composta por duas partes, S1 e S2.
É crucial sempre usar um nonce único para evitar ataques de segurança. Um exemplo notório do que pode acontecer quando essa regra não é seguida é o hackeamento do PlayStation 3, que foi comprometido devido ao reuso de nonce.

![](assets/image/section2/10.webp)

Passos:

- Determine um nonce v, que é um número aleatório único.
  Nonce = Número Usado Apenas Uma Vez.
  É determinado por quem realiza a assinatura.
- Calcule adicionando e duplicando pontos em uma curva elíptica a partir do ponto G, a posição de V na curva elíptica.
  De forma que V = v.G
  x e y são as coordenadas de V no plano.
- Calcule S1.
  S1 = x mod n com n = a ordem da curva e x uma coordenada de V no plano.
  Observação: O número de chaves públicas possíveis é maior do que o número de pontos na curva elíptica no campo finito de inteiros positivos usado no Bitcoin.
  A ordem da curva corresponde apenas às possibilidades que a chave pública pode assumir na curva.
- Calcule S2.
  H(Tx) = Hash da transação
k = a chave privada - Calcular a assinatura: a concatenação de S1 + S2.
- Calcular P, o cálculo de verificação da assinatura.
  K = a chave pública

Por exemplo, para obter a chave pública 3G, você traça uma tangente ao ponto G, calcula o oposto de -G para obter 2G e depois adiciona G e 2G. Para realizar uma transação, você deve provar que conhece o número 3 desbloqueando os bitcoins associados à chave pública 3G.

Para criar uma assinatura digital e provar que você conhece a chave privada associada à chave pública 3G, você primeiro calcula um nonce e depois o ponto V associado a esse nonce (no exemplo dado, é 4G). Em seguida, você calcula o ponto T adicionando a chave pública 3G e o ponto V, o que resulta em 7G.

![image](assets/image/section2/11.webp)

Vamos simplificar o processo de assinatura digital.
Na imagem anterior, a chave privada k = 3.
Podemos calcular facilmente a chave pública K associada a essa chave privada: K = 3G.
Em seguida, geramos um nonce pseudoaleatoriamente: v = 4.
A partir desse nonce, é possível calcular V de forma que: V = v.G = 4G.

A partir desse ponto V, calculamos o ponto T de forma que:
T = t.G = 7G (com t = 7).

Agora é hora de prosseguir com a verificação da assinatura digital.

Verificar uma assinatura digital é uma etapa crucial no uso do algoritmo ECDSA, que permite confirmar a autenticidade de uma mensagem assinada sem precisar da chave privada do remetente. Veja como funciona em detalhes:

Em nosso exemplo, temos dois valores importantes: t e V.
t é um valor numérico (7 neste exemplo) e V é um ponto na curva elíptica (representado por 4G aqui). Esses valores são gerados durante a criação da assinatura digital e são enviados junto com a mensagem para permitir a verificação.

Quando o verificador recebe a mensagem, ele também receberá esses dois valores, t e V.

Aqui estão as etapas que o verificador seguirá para validar a assinatura:

1. Primeiro, ele calculará o hash da mensagem, que chamaremos de H.
2. Em seguida, ele calculará u1 e u2. Para fazer isso, ele usará as seguintes fórmulas:
   - u1 = H /\* (S2)^-1 mod n
   - u2 = T /\* (S2)^-1 mod n
     Onde S2 é a segunda parte da assinatura digital, n é a ordem da curva elíptica e (S2)^-1 é o inverso de S2 mod n.
3. O verificador então calculará um ponto P' na curva elíptica usando a fórmula: P' = u1 _ G + u2 _ K
   - G é o ponto gerador da curva
   - K é a chave pública do remetente
4. O verificador então calculará I', que é simplesmente a coordenada x do ponto P' módulo n.
5. Por fim, o verificador confirmará se I' é igual a t. Se for o caso, a assinatura é considerada válida. Caso contrário, a assinatura é inválida.
Esse procedimento garante que apenas o remetente que possui a chave privada correspondente poderia ter produzido uma assinatura que passe por esse processo de verificação.

![image](assets/image/section2/12.webp)

Em termos mais simples:
A pessoa que produz a assinatura fornecerá o número t (em nosso exemplo, t = 7) e o ponto V para a pessoa que a verifica.
É impossível determinar a chave pública ou a chave privada a partir do número 7 e do número V.

Os passos para verificar a assinatura digital são os seguintes:

- Na curva, o verificador adiciona o ponto da chave pública ao ponto V para recuperar o ponto T'.
- O verificador calcula o número t.G.
- O verificador verifica se o resultado de t.G é de fato igual ao número T'.

Em conclusão, verificar uma assinatura digital é um procedimento essencial em transações de Bitcoin. Isso garante que a mensagem assinada não tenha sido alterada durante a transmissão e que o remetente seja realmente o detentor da chave privada. Essa técnica de autenticação digital é baseada em princípios matemáticos complexos, incluindo aritmética de curva elíptica, ao mesmo tempo em que mantém a confidencialidade da chave privada. Ela fornece uma base sólida de segurança para transações criptográficas.

Dito isso, a gestão dessas chaves, bem como sua criação, é outra questão essencial no Bitcoin. Como gerar um novo par de chaves? Como organizar de forma segura e eficiente uma infinidade de chaves? Como recuperá-las, se necessário?

Para responder a essas perguntas e aprofundar sua compreensão sobre segurança criptográfica, nosso próximo curso se concentrará no conceito de Carteiras Determinísticas Hierárquicas (HD wallets) e no uso de frases mnemônicas. Esses mecanismos oferecem maneiras elegantes de gerenciar efetivamente suas chaves de criptomoeda, ao mesmo tempo em que aprimoram a segurança.

# A frase mnemônica
<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>

## Evolução das carteiras de Bitcoin
<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>

A Carteira Determinística Hierárquica, mais conhecida como HD wallet, desempenha um papel proeminente no ecossistema de criptomoedas. O termo "carteira" pode parecer enganador para aqueles que são novos nesse campo, pois não envolve a posse de dinheiro ou moedas. Em vez disso, refere-se a uma coleção de chaves privadas criptográficas.

As primeiras carteiras eram softwares que agrupavam chaves determinadas privadamente de maneira pseudoaleatória, mas não tinham conexão entre elas. Essas carteiras são chamadas de "Just a Bunch Of Keys" (JBOK).

Como as chaves não têm conexão entre si, o usuário precisa fazer um novo backup para cada novo par de chaves gerado. Se o usuário sempre usar o mesmo par de chaves e comprometer a confidencialidade, ou gerar um novo par de chaves aleatoriamente e, portanto, precisar fazer um novo backup dessas chaves.

No entanto, a complexidade de gerenciar essas chaves é compensada por um conjunto de protocolos chamados Propostas de Melhoria do Bitcoin (BIPs). Essas propostas de atualização estão no cerne da funcionalidade e segurança das HD wallets. Por exemplo, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), lançado em 2012, revolucionou a forma como essas chaves são geradas e armazenadas, introduzindo o conceito de chaves derivadas de forma determinística e hierárquica. A ideia é derivar todas as chaves de forma determinística e hierárquica a partir de uma única informação: a semente. Isso simplifica muito o processo de backup dessas chaves, ao mesmo tempo em que mantém seu nível de segurança.

Posteriormente, [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) introduziu uma inovação significativa: a frase mnemônica de 24 palavras. Esse sistema transformou uma sequência complexa e difícil de lembrar de números em uma série de palavras comuns, tornando muito mais fácil memorizar e armazenar. Além disso, [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) propôs adicionar uma senha adicional para aumentar a segurança das chaves individuais. Essas melhorias sucessivas levaram aos padrões BIP43 e BIP44, que padronizaram a estrutura e hierarquização das carteiras HD, tornando-as mais acessíveis e amigáveis para o público em geral.

Nas seções seguintes, iremos aprofundar o funcionamento das carteiras HD. Discutiremos os princípios de derivação de chaves e examinaremos os conceitos fundamentais de entropia e geração de números aleatórios, que são essenciais para garantir a segurança da sua carteira HD.

Em resumo, é essencial destacar o papel central do BIP32 e BIP39 no design e segurança das carteiras HD. Esses protocolos permitem a geração de várias chaves a partir de uma única semente, que deve ser um número aleatório ou pseudo-aleatório. Hoje, esses padrões são adotados pela maioria das carteiras de criptomoedas, sejam elas dedicadas a uma única criptomoeda ou que suportem vários tipos de moedas.

## Entropia e Número Aleatório
<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>

A importância da segurança da chave privada no ecossistema do Bitcoin é inegável. Elas são, de fato, o alicerce que garante a segurança das transações de Bitcoin. Para evitar qualquer vulnerabilidade associada à previsibilidade, essas chaves devem ser geradas de maneira verdadeiramente aleatória, o que pode se tornar rapidamente um exercício trabalhoso. O problema é que, na ciência da computação, é impossível gerar um número verdadeiramente aleatório, pois ele é necessariamente derivado de um processo determinístico; um código. É por isso que é essencial aprender sobre os diferentes Geradores de Números Aleatórios (RNG). Os tipos de RNG variam, desde Geradores de Números Pseudo-Aleatórios (PRNG) até Geradores de Números Verdadeiramente Aleatórios (TRNG), bem como PRNGs que incorporam uma fonte de entropia.

Entropia se refere ao estado de "desordem" de um sistema. A partir de uma entropia externa, ou seja, uma fonte externa de informação, é possível usar um gerador de números aleatórios para obter um número aleatório.

![imagem](assets/image/section3/2.webp)

Vamos dar uma olhada em como um Gerador de Números Pseudo-Aleatórios (PRNG) funciona.

Ele recebe uma semente como entrada, que corresponde ao estado interno 0.
Nesse estado interno, uma função de transformação é aplicada, e o resultado, que é um número pseudo-aleatório, corresponde ao estado interno 1.
Nesse estado interno 1, novamente, uma função de transformação é aplicada, resultando em um novo número aleatório = estado interno 2.
E assim por diante.

A principal desvantagem é que qualquer semente idêntica sempre produzirá a mesma saída. Além disso, se conhecermos o resultado das funções de transformação iniciais, poderemos recuperar o número aleatório na saída do processo.

Um exemplo de função de transformação é a função PBKDF2.

**Em resumo, um PRNG criptograficamente seguro deve:**

- ser estatisticamente aleatório
- ser imprevisível
- ser resistente mesmo se os resultados forem revelados
- ter um período suficientemente longo

![imagem](assets/image/section3/3.webp)

No caso do Bitcoin, as chaves privadas são geradas a partir de uma única informação na base da carteira. Essa informação permite a derivação determinística e hierárquica de pares de chaves filhas. A entropia é a base de toda carteira HD, embora não haja um padrão para gerar esse número aleatório. Portanto, a geração de números aleatórios é um desafio importante na segurança das transações de Bitcoin.

## A frase mnemônica
<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>


A segurança de uma carteira de Bitcoin é uma preocupação importante para todos os seus usuários. Uma maneira essencial de garantir o backup da carteira é gerar uma frase mnemônica com base na entropia e no checksum.

![imagem](assets/image/section3/5.webp)

Para converter a entropia em uma frase mnemônica, basta calcular o checksum da entropia e concatenar a entropia e o checksum.

Uma vez gerada a entropia, a função SHA256 é usada na entropia para criar um hash.
Os primeiros 8 bits do hash são recuperados, que é o checksum.
A frase mnemônica é o resultado da entropia adicionada ao checksum.

O checksum garante a verificação da precisão da frase de recuperação. Sem esse checksum, um erro na frase poderia resultar na criação de uma carteira diferente e, portanto, na perda de fundos. O checksum é obtido passando a entropia pela função SHA256 e recuperando os primeiros 8 bits do hash.

![imagem](assets/image/section3/6.webp)

Existem diferentes padrões para a frase mnemônica, dependendo do tamanho da entropia. O padrão mais comumente usado para uma frase de recuperação de 24 palavras é uma entropia de 256 bits. O tamanho do checksum é determinado dividindo o tamanho da entropia por 32.

Por exemplo, uma entropia de 256 bits gera um checksum de 8 bits. A concatenação da entropia e do checksum leva a tamanhos respectivos de 128 bits, 160 bits, etc. Dependendo do tamanho da entropia, a frase de recuperação consistirá em 12 palavras para 128 bits, 15 palavras para 160 bits e 24 palavras para 256 bits.

**Codificação da frase mnemônica:**

![imagem](assets/image/section3/7.webp)

Os últimos 8 bits correspondem ao checksum.
Cada segmento de 11 bits é convertido em decimal.
Cada decimal corresponde a uma palavra de uma lista de 2048 palavras no BIP39. É importante observar que nenhuma palavra tem a mesma ordem das quatro primeiras letras.

É essencial fazer backup da frase de recuperação de 24 palavras para preservar a integridade da carteira de Bitcoin. Os dois padrões mais comumente usados são baseados em uma entropia de 128 ou 256 bits e uma concatenação de 12 ou 24 palavras. Adicionar uma frase secreta é uma opção adicional para aumentar a segurança da carteira.

Em conclusão, gerar uma frase mnemônica para proteger uma carteira de Bitcoin é um processo crucial. É importante aderir aos padrões da frase mnemônica com base no tamanho da entropia. Fazer backup da frase de recuperação de 24 palavras é essencial para evitar qualquer perda de fundos.

## A frase secreta
<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>

A frase secreta é uma senha adicional que pode ser integrada a uma carteira de Bitcoin para aumentar sua segurança. Seu uso é opcional e fica a critério do usuário. Ao adicionar informações arbitrárias que, juntamente com a frase mnemônica, permitem o cálculo da semente da carteira, a frase secreta melhora sua segurança.

![imagem](assets/image/section3/8.webp)

A frase de acesso é um sal criptográfico opcional de tamanho escolhido pelo usuário. Ele melhora a segurança de uma carteira HD adicionando informações arbitrárias que, quando combinadas com a frase mnemônica, permitirão o cálculo da semente.
Uma vez estabelecida durante a criação de uma carteira, ela é necessária para a derivação de todas as chaves da carteira. A função pbkdf2 é usada para gerar a semente a partir da frase de acesso. Essa semente permite a derivação de todos os pares de chaves filhas da carteira. Se a frase de acesso for alterada, a carteira Bitcoin se torna completamente diferente.

A frase de acesso é uma ferramenta essencial para aumentar a segurança das carteiras Bitcoin. Ela pode permitir a implementação de várias estratégias de segurança. Por exemplo, pode ser usada para criar duplicatas e facilitar backups da frase mnemônica. Também pode melhorar a segurança da carteira ao mitigar os riscos associados à geração aleatória da frase mnemônica.

Uma frase de acesso eficaz deve ser longa (20 a 40 caracteres) e diversa (usando letras maiúsculas, letras minúsculas, números e símbolos). Não deve estar diretamente relacionada ao usuário ou ao seu ambiente. É mais seguro usar uma sequência aleatória de caracteres em vez de uma simples palavra como frase de acesso.

![image](assets/image/section3/9.webp)

Uma frase de acesso é mais segura do que uma senha simples. A frase de acesso ideal é longa, variada e aleatória. Ela pode aumentar a segurança de uma carteira ou software de armazenamento a quente. Também pode ser usada para criar backups redundantes e seguros.

É crucial cuidar dos backups da frase de acesso para evitar a perda de acesso à carteira. Uma frase de acesso é uma opção para uma carteira HD. Ela pode ser gerada aleatoriamente com dados ou outro gerador de números pseudoaleatórios. Não é recomendado memorizar uma frase de acesso ou frase mnemônica.

Em nossa próxima lição, examinaremos em detalhes o funcionamento da semente e do primeiro par de chaves gerado a partir dela. Sinta-se à vontade para seguir este curso para continuar seu aprendizado. Esperamos vê-lo novamente em breve.

# Criação de Carteiras Bitcoin
<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>

## Criação da Semente e Chave Mestra
<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>

Nesta parte do curso, exploraremos os passos para a derivação de uma Carteira Determinística Hierárquica (HD Wallet), que permite a criação e gerenciamento hierárquico e determinístico de chaves privadas e públicas.

![image](assets/image/section4/0.webp)

A base da Carteira HD depende de dois elementos essenciais: a frase mnemônica e a frase de acesso (senha adicional opcional). Juntos, eles constituem a semente, uma sequência alfanumérica de 512 bits que serve como base para a derivação das chaves da carteira. A partir dessa semente, é possível derivar todos os pares de chaves filhas da carteira Bitcoin. A semente é a chave que concede acesso a todos os bitcoins associados à carteira, independentemente do uso de uma frase de acesso ou não.

![image](assets/image/section4/1.webp)

Para obter a semente, é usada a função pbkdf2 (Função de Derivação de Chave Baseada em Senha 2) com a frase mnemônica e a frase de acesso. A saída do pbkdf2 é uma semente de 512 bits.

A partir da semente, é possível determinar a chave privada mestra e o código de cadeia usando o algoritmo HMAC SHA-512 (Código de Autenticação de Mensagem Baseado em Hash Algoritmo Seguro 512). Esse algoritmo requer uma mensagem e uma chave como entrada para gerar um resultado. A chave privada mestra é calculada a partir da semente e da frase "Bitcoin SEED". Essa frase é idêntica para todas as derivações de todas as carteiras HD, garantindo consistência entre as carteiras.
Inicialmente, a função SHA-512 não foi implementada no protocolo Bitcoin, razão pela qual o HMAC SHA-512 é utilizado. O uso do HMAC SHA-512 com a frase "Bitcoin SEED" restringe o usuário a gerar uma carteira específica para o Bitcoin. O resultado do HMAC SHA-512 é um número de 512 bits, dividido em duas partes: os 256 bits mais à esquerda representam a chave privada mestra, enquanto os 256 bits mais à direita representam o código de cadeia mestre.

![image](assets/image/section4/2.webp)

A chave privada mestra é a chave pai de todas as chaves futuras na carteira, enquanto o código de cadeia mestre está envolvido na derivação das chaves filhas. É importante observar que é impossível derivar um par de chaves filhas sem conhecer o código de cadeia correspondente do par pai.

Um par de chaves na carteira consiste em uma chave privada, uma chave pública e um código de cadeia. O código de cadeia introduz uma fonte de aleatoriedade na derivação das chaves filhas e isola cada par de chaves para evitar qualquer vazamento de informações.
É importante observar que a chave privada mestra é a primeira chave privada derivada da semente e não tem conexão com as chaves estendidas da carteira.

Na próxima lição, exploraremos as chaves estendidas em detalhes, como xPub, xPRV, zPub, e entenderemos por que são usadas e como são construídas.

## Chaves Estendidas
<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>

Nesta parte da lição, estudaremos chaves estendidas (xPub, zPub, yPub) e seus prefixos, que desempenham um papel importante na derivação de chaves filhas em uma Carteira Determinística Hierárquica (HD Wallet).

![image](assets/image/section4/3.webp)

Chaves estendidas são distintas das chaves mestras. Uma carteira HD gera uma frase mnemônica e uma semente para obter a chave mestra e o código de cadeia mestre. Chaves estendidas são usadas para derivar chaves filhas e requerem tanto a chave pai quanto o código de cadeia correspondente. Uma chave estendida combina essas duas informações para simplificar o processo de derivação.

![image](assets/image/section4/4.webp)

Chaves públicas estendidas só podem derivar chaves públicas normais, enquanto chaves privadas estendidas podem derivar tanto chaves públicas quanto chaves privadas filhas, seja por derivação normal ou endurecida. A derivação endurecida é a derivação a partir da chave privada pai, enquanto a derivação normal corresponde à derivação a partir da chave pública pai.

O uso de chaves estendidas com o prefixo XPUB permite a derivação de novos endereços sem recorrer às chaves privadas correspondentes, proporcionando assim uma melhor segurança. Os metadados associados às chaves estendidas fornecem informações importantes sobre seu papel e posição na hierarquia de chaves.

Chaves estendidas são identificadas por prefixos específicos (XPRV, XPUB, YPUB, ZPUB) que indicam se é uma chave privada ou pública estendida, bem como seu propósito específico. Os metadados associados a uma chave estendida incluem a versão (prefixo), profundidade, impressão digital da chave pai, índice e carga útil (código de cadeia e chave pai).

![image](assets/image/section4/5.webp)

A versão corresponde ao tipo de chave: xpub, xprv, ...

A profundidade corresponde ao número de derivações entre as chaves pai e filhas desde a chave mestra.

A impressão digital da chave pai são os primeiros 4 bytes do hash 160 da chave pai.
O índice é o número do par que é usado para gerar a chave estendida entre seus irmãos. (irmãos = chaves da mesma profundidade) Por exemplo, se quisermos derivar o xpub de nossa terceira conta, seu índice será 2 (porque o índice começa em 0).
A carga útil é composta pelo código da cadeia (32 bytes) e pela chave pai (33 bytes).
As chaves públicas comprimidas têm um tamanho de 33 bytes, enquanto as chaves públicas brutas têm 512 bits. As chaves públicas comprimidas mantêm as mesmas informações das chaves brutas, mas com um tamanho reduzido. As chaves estendidas têm um tamanho de 82 bytes e seu prefixo é representado em base 58 através de uma conversão para hexadecimal. O checksum é calculado usando a função de hash HASH256.

![imagem](assets/image/section4/6.webp)

As derivações aprimoradas começam a partir de índices que são potências de 2 (2^31). É interessante observar que os prefixos mais comumente usados são xpub e zpub, que correspondem respectivamente aos padrões legados e segwit v1 e segwit v0.

Na próxima lição, vamos nos concentrar na derivação de pares de chaves filhas usando o conhecimento adquirido sobre chaves estendidas e a chave mestra da carteira.

## Derivação de pares de chaves filhas
<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>

Como lembrete, discutimos o cálculo da semente e da chave mestra, que são os primeiros elementos essenciais para a organização hierárquica e derivação da carteira HD (Hierarchical Deterministic). A semente, com um comprimento de 128 a 256 bits, é gerada aleatoriamente ou a partir de uma frase secreta. Ela desempenha um papel determinístico na derivação de todas as outras chaves. A chave mestra é a primeira chave derivada da semente e permite a derivação de todos os outros pares de chaves filhas.

O código da cadeia mestra desempenha um papel importante na recuperação da carteira a partir da semente. Deve-se observar que todas as chaves derivadas da mesma semente terão o mesmo código da cadeia mestra.

![imagem](assets/image/section4/7.webp)

A organização hierárquica e a derivação da carteira HD oferecem uma gestão mais eficiente de chaves e estruturas de carteira. As chaves estendidas permitem a derivação de um par de chaves filhas a partir de um par de chaves pai usando cálculos matemáticos e algoritmos específicos.
Existem diferentes tipos de pares de chaves filhas, incluindo chaves reforçadas e chaves normais. A chave pública estendida permite apenas a derivação de chaves públicas filhas normais, enquanto a chave privada estendida permite a derivação de todas as chaves filhas, tanto públicas quanto privadas, estejam elas no modo normal ou reforçado. Cada par de chaves possui um índice que permite diferenciá-las umas das outras.
![imagem](assets/image/section4/8.webp)

A derivação de chaves filhas usa a função HMAC-SHA512 usando a chave pai concatenada com o índice e o código da cadeia associado ao par de chaves. As chaves filhas normais têm um índice que varia de 0 a 2 elevado à potência de 31 menos 1, enquanto as chaves filhas reforçadas têm um índice que varia de 2 elevado à potência de 31 a 2 elevado à potência de 32 menos 1.

![imagem](assets/image/section4/9.webp)

![imagem](assets/image/section4/10.webp)

Existem dois tipos de pares de chaves filhas: pares reforçados e pares normais. O processo de derivação de chaves filhas usa chaves públicas para gerar condições de gasto, enquanto chaves privadas são usadas para assinar. A chave pública estendida permite apenas a derivação de chaves públicas filhas normais, enquanto a chave privada estendida permite a derivação de todas as chaves filhas, tanto públicas quanto privadas, no modo normal ou reforçado.

![imagem](assets/image/section4/11.webp)
![imagem](assets/image/section4/12.webp)

A derivação reforçada usa a chave privada pai, enquanto a derivação normal usa a chave pública pai. A função HMAC-SHA512 é usada para a derivação reforçada, enquanto a derivação normal usa um resumo de 512 bits. A chave pública filha é obtida multiplicando a chave privada filha pelo gerador da curva elíptica.

![image](assets/image/section4/13.webp)
![image](assets/image/section4/14.webp)

A derivação hierárquica e a derivação de muitos pares de chaves de forma determinística permitem a criação de uma estrutura de árvore para a derivação hierárquica. Na próxima lição deste treinamento, estudaremos a estrutura da carteira HD, bem como os caminhos de derivação, com foco especial nas notações de caminho de derivação.

## Estrutura da Carteira e Caminhos de Derivação
<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>

Neste capítulo, estudaremos a estrutura da árvore de derivação em uma Carteira Determinística Hierárquica (HD Wallet). Já exploramos o cálculo da semente, a chave mestra e a derivação de pares de chaves filhas. Agora, vamos nos concentrar na organização das chaves dentro da carteira.

A HD Wallet usa camadas de profundidade para organizar as chaves. Cada derivação de um par pai para um par filho corresponde a uma camada de profundidade.

![image](assets/image/section4/15.webp)

- A profundidade 0 corresponde à chave mestra e ao código de cadeia mestra.

- A profundidade 1 é usada para derivar chaves filhas para um propósito específico, determinado pelo índice. Os propósitos estão em conformidade com os padrões BIP 84 e Segwit v0/v1.

- A profundidade 2 permite a diferenciação de contas para diferentes criptomoedas ou redes. Isso permite organizar a carteira com base em diferentes fontes de fundos. Para o bitcoin, o índice será 0.

- A profundidade 3 é usada para organizar a carteira em diferentes contas, fornecendo uma estrutura mais clara e organizada.

- A profundidade 4 corresponde às cadeias externas e internas, que são usadas para endereços destinados a serem comunicados publicamente. O índice 0 está associado à cadeia externa, enquanto o índice 1 está associado à cadeia interna. Cada conta possui duas cadeias: a cadeia externa (0) e a cadeia interna (1). A profundidade 4 também é usada para gerenciar tipos de script no caso de carteiras multiassinatura.

- A profundidade 5 é usada para endereços de recebimento em uma carteira padrão. Na próxima seção, examinaremos a derivação de pares de chaves filhas com mais detalhes.

![image](assets/image/section4/16.webp)

Para cada camada de profundidade, usamos índices para diferenciar pares de chaves filhas.

O índice sem apóstrofo corresponde ao índice real usado, enquanto o índice com apóstrofo corresponde ao índice real + 2^31. Derivações reforçadas usam índices de 2^31 a 2^32-1. Por exemplo, o índice 44' corresponde ao índice real 2^31 + 44.

Para gerar um endereço de recebimento específico, derivamos um par de chaves filhas da chave mestra e do código de cadeia mestra. Em seguida, usamos o índice para diferenciar entre diferentes pares de chaves filhas na mesma profundidade.
Chaves estendidas, como XPUB, permitem que você compartilhe sua carteira com várias pessoas. O caminho de derivação é usado para diferenciar entre a cadeia externa (endereços destinados a serem compartilhados) e a cadeia interna (endereços de troco).

No próximo capítulo, estudaremos endereços de recebimento, suas vantagens de uso e as etapas envolvidas em sua construção.

# O que é um endereço Bitcoin?
<partId>81ec8d17-f8ee-5aeb-8035-d370866f4281</partId>

## Endereços Bitcoin
<chapterId>0a887ed8-3424-5a52-98e1-e4b406150475</chapterId>

Neste capítulo, exploraremos os endereços de recebimento, que desempenham um papel crucial no sistema Bitcoin. Eles permitem que os fundos sejam recebidos em uma transação e são gerados a partir de pares de chaves privadas e públicas. Embora exista um tipo de script chamado Pay2PublicKey que permite que bitcoins sejam bloqueados em uma chave pública, os usuários geralmente preferem usar endereços de recebimento em vez desse script.

![image](assets/image/section5/0.webp)

Quando um destinatário deseja receber bitcoins, ele fornece um endereço de recebimento ao remetente em vez de sua chave pública. Um endereço é na verdade um hash de uma chave pública, com um formato específico. A chave pública é derivada da chave privada filha usando operações matemáticas como adição e duplicação de pontos em curvas elípticas.

![image](assets/image/section5/1.webp)

É importante observar que não é possível reverter de um endereço para a chave pública, nem da chave pública para a chave privada. O uso de um endereço reduz o tamanho das informações da chave pública, que inicialmente é de 512 bits.

Os endereços Bitcoin foram reduzidos de tamanho para facilitar seu uso. Eles possuem um checksum, que permite detectar erros de digitação e reduzir o risco de perda de bitcoins. Por outro lado, as chaves públicas não possuem um checksum, o que significa que erros de digitação podem resultar na perda dos fundos correspondentes.

Os endereços também fornecem uma segunda camada de segurança entre informações públicas e privadas, tornando mais difícil assumir o controle da chave privada.

É essencial enfatizar que cada endereço deve ser usado apenas uma vez. Reutilizar o mesmo endereço apresenta problemas de privacidade e deve ser evitado.

Diferentes prefixos são usados para endereços Bitcoin. Por exemplo, BC1Q corresponde a um endereço Segwit V0, BC1P a um endereço Taproot/Segwit V1 e os prefixos 1 e 3 estão associados a endereços Pay2PublicKeyH/Pay2ScriptH (legado). Na próxima lição, explicaremos passo a passo como derivar um endereço de uma chave pública.

## Como criar um endereço Bitcoin?
<chapterId>6dee7bf3-7767-5f8d-a01b-659b95cfe0a5</chapterId>

Neste capítulo, discutiremos a construção de um endereço de recebimento para transações Bitcoin. Um endereço de recebimento é uma representação alfanumérica de uma chave pública comprimida. A conversão de uma chave pública em um endereço de recebimento envolve várias etapas.

### Etapa 1: Compressão da chave pública

![image](assets/image/section5/14.webp)

Um endereço é derivado de uma chave pública filha.

Uma chave pública é um ponto na curva elíptica. Graças à simetria da curva elíptica, um ponto na curva elíptica terá uma coordenada x associada a apenas dois valores possíveis para y: positivo ou negativo. 
No entanto, no protocolo Bitcoin, trabalhamos com um conjunto finito de números inteiros positivos em vez do conjunto de números reais. Para distinguir entre os dois possíveis valores de y, é suficiente indicar se y é par ou ímpar.

A compressão de uma chave pública reduz seu tamanho de 520 bits para 264 bits.

Usamos o prefixo 0x02 para um y par e 0x03 para um y ímpar. Esta é a forma comprimida da chave pública.

### Etapa 2: Hashing da chave pública comprimida

![image](assets/image/section5/3.webp)

O hashing da chave pública comprimida é realizado usando a função SHA256. A função RIPEMD160 é então aplicada ao digest.

### Etapa 3: O payload = Payload do endereço

![image](assets/image/section5/4.webp)

O resumo binário de RIPEMD160(SHA256(K)) é usado para formar grupos de 5 bits. Cada grupo é transformado em base16 (Hexadecimal) e/ou base 10.

### Passo 4: Adicionando metadados para cálculo de checksum com o programa BCH

![imagem](assets/image/section5/5.webp)

No caso de endereços legados, usamos o hash duplo SHA256 para gerar o checksum do endereço. No entanto, para os endereços Segwit V0 e V1, dependemos da tecnologia de checksum BCH para garantir a detecção de erros. O programa BCH é capaz de sugerir e corrigir erros com uma probabilidade extremamente baixa de erro. Atualmente, o programa BCH é usado para detectar e sugerir modificações a serem feitas, mas não as realiza automaticamente em nome do usuário.
O programa BCH requer várias informações de entrada, incluindo o HRP (Parte Legível pelo Humano) que precisa ser estendido. Estender o HRP envolve codificar cada letra em base 2 de acordo com seu código ASCII. Em seguida, pegando os primeiros 3 bits do resultado para cada letra e convertendo-os para base 10 (em azul na imagem). Insira um separador 0. Em seguida, concatene os próximos 5 bits de cada letra previamente convertida para base 10 (em amarelo na imagem).

Estender o HRP em base 10 permite isolar os últimos cinco bits de cada caractere, reforçando assim o checksum.

A versão Segwit V0 é representada pelo código 00 e o "payload" está em preto, em base 10. Isso é seguido por seis caracteres reservados para o checksum.

### Passo 5: Calculando o checksum com o programa BCH

![imagem](assets/image/section5/6.webp)

A entrada contendo os metadados é então submetida ao programa BCH para obter o checksum em base 10.

Aqui temos o checksum.

### Passo 6: Construção do endereço e conversão para Bech32

![imagem](assets/image/section5/7.webp)

A concatenação da versão, payload e checksum permite construir o endereço. Os caracteres em base 10 são então convertidos em caracteres Bech32 usando uma tabela de correspondência. O alfabeto Bech32 inclui todos os caracteres alfanuméricos, exceto 1, b, i e o, para evitar qualquer confusão.

### Passo 7: Adicionando o HRP e o separador

![imagem](assets/image/section5/8.webp)

Em rosa, o checksum.
Em preto, o payload = o hash da chave pública.
Em azul, a versão.

Tudo é convertido para Bech32, então 'bc' é adicionado para bitcoin e '1' como separador, e aqui está o endereço.

# Vá além
<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>

## Criando uma semente a partir de 128 lançamentos de dados!
<chapterId>0f4d40a7-cf0e-5faf-bc4d-691486771ac1</chapterId>

Criar uma frase mnemônica é um passo crucial para garantir a segurança da sua carteira de criptomoedas. Existem vários métodos para gerar uma frase mnemônica, no entanto, vamos nos concentrar no método de geração manual usando dados. É importante observar que este método não é adequado para uma carteira de alto valor. É recomendado usar software de código aberto ou uma carteira de hardware para gerar a frase mnemônica. Para criar uma frase mnemônica, usaremos dados para gerar informações binárias. O objetivo é entender o processo de criação da frase mnemônica.

**Passo 1 - Preparação:**
Certifique-se de ter uma distribuição Linux amnésica, como o Tails OS, instalada em uma chave USB para maior segurança. Observe que este tutorial não deve ser usado para criar uma carteira principal.
**Passo 2 - Gerando um número binário aleatório:**
Usaremos dados para gerar informações binárias. Role um dado 128 vezes e registre cada resultado (1 para ímpar, 0 para par).
**Passo 3 - Organizando números binários:**
Organize os números binários obtidos em linhas de 11 dígitos para facilitar cálculos adicionais. A décima segunda linha deve ter apenas 7 dígitos.

**Passo 4 - Calculando o checksum:**
Os últimos 4 dígitos da décima segunda linha correspondem ao checksum. Para calcular esse checksum, precisamos usar um terminal de uma distribuição Linux. É recomendado usar o [TailOs](https://tails.boum.org/index.fr.html), que é uma distribuição sem memória inicializável a partir de uma chave USB. Uma vez no seu terminal, digite o comando `echo <número binário> | shasum -a 254 -0`. Substitua `<número binário>` pela sua lista de 128 zeros e uns. A saída é um hash hexadecimal. Anote o primeiro caractere desse hash e converta-o para binário. Você pode usar essa [tabela](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) para ajudar. Adicione o checksum binário (4 dígitos) à décima segunda linha da sua planilha.

**Passo 5 - Conversão para decimal:**
Para encontrar as palavras associadas a cada uma das suas linhas, você primeiro precisa converter cada série de 11 bits para decimal. Aqui, você não pode usar um conversor online porque esses bits representam sua frase mnemônica. Portanto, você precisará converter usando uma calculadora e um truque da seguinte maneira: cada bit está associado a uma potência de 2, então da esquerda para a direita, temos 11 posições correspondentes a 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. Para converter sua série de 11 bits para decimal, simplesmente some apenas as posições que contêm um 1. Por exemplo, para a série 00110111011, isso corresponde à seguinte adição: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Agora você pode converter cada linha para decimal. E antes de passar para a codificação em palavras, adicione +1 a todas as linhas porque o índice da lista de palavras BIP39 começa em 1, não em 0.

**Passo 8 - Gerando a frase mnemônica:**
Comece imprimindo a [lista de 2048 palavras](https://seedxor.com/files/wordlist.pdf) para converter entre seus números decimais e as palavras BIP39. A singularidade dessa lista é que nenhuma palavra compartilha as 4 primeiras letras com qualquer outra palavra neste dicionário. Em seguida, procure a palavra associada a cada número decimal de suas linhas.
**Passo 9 - Teste da Frase Mnemônica:**
Teste imediatamente sua frase mnemônica no Sparrow Wallet criando uma carteira a partir dela. Se você receber um erro de checksum inválido, é provável que tenha cometido um erro de cálculo. Corrija esse erro voltando ao passo 4 e teste novamente no Sparrow Wallet. Voilà! Você acabou de criar uma nova carteira Bitcoin a partir de 128 lançamentos de dados.

Gerar uma frase mnemônica é um processo importante para proteger sua carteira de criptomoedas. É recomendado usar métodos mais seguros, como usar software de código aberto ou uma carteira de hardware, para gerar a frase mnemônica. No entanto, completar este workshop ajuda a entender melhor como podemos criar uma carteira Bitcoin a partir de um número aleatório.

## BÔNUS: Entrevista com Théo Pantamis
<chapterId>39f0ec5a-e258-55cb-9789-bc46d314d816</chapterId>

Outro método criptográfico amplamente usado no protocolo Bitcoin é o método de assinaturas digitais.


![video](https://youtu.be/c9MvtGJsEvY?si=bQ1N5NCd6op0G6nW)



## Avalie o curso
<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>
<isCourseReview>true</isCourseReview>

## Exame Final
<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>
<isCourseExam>true</isCourseExam>


## Conclusão e Fim
<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

### Agradecimentos e continue a explorar a toca do coelho

Gostaríamos de agradecer sinceramente por ter concluído o curso Crypto 301. Esperamos que essa experiência tenha sido enriquecedora e educativa para você. Cobrimos muitos tópicos empolgantes, desde matemática até criptografia e o funcionamento do protocolo Bitcoin.

Se você deseja se aprofundar ainda mais no assunto, temos um recurso adicional para oferecer a você. Realizamos uma entrevista exclusiva com Théo Pantamis e Loïc Morel, dois renomados especialistas no campo da criptografia. Essa entrevista explora vários aspectos do assunto em profundidade e oferece perspectivas interessantes.

Sinta-se à vontade para assistir a essa entrevista para continuar explorando o fascinante campo da criptografia. Esperamos que ela seja útil e inspiradora em sua jornada. Mais uma vez, obrigado por sua participação e comprometimento ao longo deste curso.

### Apoie-nos

Este curso, juntamente com todo o conteúdo desta universidade, foi disponibilizado gratuitamente pela nossa comunidade. Para nos apoiar, você pode compartilhá-lo com outras pessoas, tornar-se membro da universidade e até contribuir para o seu desenvolvimento por meio do GitHub. Em nome de toda a equipe, obrigado!

### Avalie o curso

Em breve, um sistema de avaliação para o treinamento será integrado a esta nova plataforma de aprendizado online! Enquanto isso, muito obrigado por fazer o curso e, se você gostou, considere compartilhá-lo com outras pessoas.
