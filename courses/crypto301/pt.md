---
name: Introdução à criptografia
goal: Compreender a criação de uma carteira Bitcoin do ponto de vista criptográfico
objectives:
  - Desmistificar a terminologia da criptografia relacionada ao Bitcoin.
  - Dominar a criação de uma carteira Bitcoin.
  - Compreender a estrutura de uma carteira Bitcoin.
  - Entender endereços e caminhos de derivação
---

# Uma jornada ao coração da criptografia

Você é fascinado pelo Bitcoin? Você se pergunta como funciona uma carteira Bitcoin? Prepare-se para embarcar em uma jornada fascinante ao coração da criptografia! Loïc, nosso especialista, irá guiá-lo pelos meandros da criação de uma carteira Bitcoin, revelando os mistérios por trás de termos técnicos intimidantes como hash, derivação de chaves e curvas elípticas.

Este treinamento não apenas fornecerá o conhecimento para entender a estrutura de uma carteira Bitcoin, mas também o preparará para mergulhar mais profundamente no emocionante universo da criptografia. Então, você está pronto para embarcar nesta jornada? Junte-se a nós e transforme sua curiosidade em habilidade!

+++

# Introdução à criptografia

![introdução por Rogzy](https://youtu.be/ul8zU5QWIXg)

É com grande prazer que damos as boas-vindas ao novo treinamento intitulado "Crypto 301: Introdução à criptografia e à carteira HD", orquestrado pelo especialista no assunto, Loïc Morel. Este curso irá mergulhá-lo no fascinante universo da criptografia, esta disciplina fundamental da matemática que garante a criptografia e a segurança de seus dados. Em nossa vida cotidiana e especialmente no campo do Bitcoin, a criptografia desempenha um papel fundamental. Os conceitos relacionados a ela, como chaves privadas, públicas, endereços, caminhos de derivação, semente e entropia, estão no cerne do uso e criação de uma carteira Bitcoin. Através deste curso, Loïc explicará em detalhes como as chaves privadas são criadas e como elas estão relacionadas aos endereços. Loïc também dedicará uma hora para explicar os detalhes matemáticos da curva elíptica, esta complexa curva matemática. Além disso, você entenderá por que o uso do HMAC SHA512 é importante para proteger sua carteira e qual é a diferença entre semente e frase mnemônica.

O objetivo final deste treinamento é permitir que você compreenda tecnicamente os processos de criação de uma carteira HD e os métodos criptográficos utilizados. Ao longo dos anos, as carteiras Bitcoin evoluíram para se tornarem mais fáceis de usar, mais seguras e padronizadas graças a BIPs específicos. Loïc irá ajudá-lo a entender esses BIPs para compreender as escolhas dos desenvolvedores do Bitcoin e dos criptógrafos. Como todos os treinamentos oferecidos pela nossa universidade, este é totalmente gratuito e de código aberto. Isso significa que você pode usá-lo livremente. Estamos ansiosos para receber seus comentários no final deste curso emocionante.

![intro por loïc](https://youtu.be/mwuxXLk4Kws)

Olá a todos, eu sou Loïc Morel, seu guia nesta exploração técnica da criptografia usada nas carteiras Bitcoin.

Nossa jornada começa com uma imersão nas profundezas das funções de hash criptográficas. Juntos, desmontaremos as engrenagens do indispensável SHA256 e exploraremos vários algoritmos dedicados à derivação.

Continuaremos nossa aventura decifrando o mundo misterioso das assinaturas digitais. Você descobrirá como a magia das curvas elípticas se aplica a essas assinaturas e esclareceremos como calcular a chave pública a partir da chave privada. E, é claro, abordaremos a ação de assinar com a chave privada.

Em seguida, voltaremos no tempo para ver a evolução das carteiras Bitcoin e nos aventuraremos nos conceitos de entropia e números aleatórios. Revisaremos a famosa frase mnemônica, enquanto abrimos um parêntese sobre a frase secreta. Você até terá a oportunidade de experimentar algo único criando uma semente a partir de 128 lançamentos de dados!

Com essas bases sólidas, estaremos prontos para a parte crucial: a criação de uma carteira Bitcoin. Desde o nascimento da semente e da chave mestra, passando pelo estudo das chaves estendidas, até a derivação dos pares de chaves filhas, cada etapa será analisada. Também discutiremos a estrutura da carteira e os caminhos de derivação.

Para coroar tudo isso, terminaremos nossa jornada examinando os endereços Bitcoin. Explicaremos como eles são criados e como desempenham um papel fundamental no funcionamento das carteiras Bitcoin.

Embarque comigo nesta jornada fascinante e prepare-se para explorar o universo da criptografia como nunca antes. Deixe suas preconcepções na porta e abra sua mente para uma nova maneira de entender o Bitcoin e sua estrutura fundamental.

# Funções de hash

## Introdução às funções de hash criptográficas relacionadas ao Bitcoin

![funções de hash criptográficas](https://youtu.be/dvnGArYvVr8)

Bem-vindo à nossa sessão de hoje dedicada a uma imersão profunda no mundo criptográfico das funções de hash, uma pedra angular essencial para a segurança do protocolo Bitcoin. Imagine uma função de hash como um robô decifrador criptográfico ultra eficiente que transforma informações de todos os tamanhos em uma impressão digital única e de tamanho fixo, chamada "hash". Ao longo de nossa exploração, retrataremos o perfil das funções de hash criptográficas, destacando seu uso no protocolo Bitcoin e definindo os objetivos específicos que essas funções criptográficas devem alcançar.

Retratar o perfil das funções de hash criptográficas requer entender duas qualidades essenciais: sua irreversibilidade e sua resistência à falsificação. Cada função de hash criptográfica é como um artista único, produzindo um "hash" distinto para cada entrada. Mesmo um pincel que desvia ligeiramente altera consideravelmente a imagem final, ou seja, o hash. Essas funções atuam como sentinelas digitais, verificando a integridade de softwares baixados. Outra característica crucial que elas possuem é sua resistência a colisões. Certamente, no universo do hash, as colisões são inevitáveis, mas uma excelente função de hash criptográfica as minimiza consideravelmente. É como se cada hash fosse uma casa em uma cidade enorme; apesar do grande número de casas, uma boa função de hash garante que cada casa tenha um endereço único.

Naveguemos agora pelas águas turbulentas das funções de hash obsoletas. SHA0, SHA1 e MD5 são hoje consideradas cascas enferrujadas no oceano do hash criptográfico. Elas são frequentemente desaconselhadas porque perderam sua resistência a colisões. O princípio das gavetas explica por que, apesar de nossos melhores esforços, evitar colisões é impossível devido à limitação do tamanho de saída. Também é importante observar que a resistência à segunda pré-imagem depende da resistência a colisões. Para ser verdadeiramente considerada segura, uma função de hash deve resistir a colisões, à segunda pré-imagem e à pré-imagem.
Elemento chave no protocolo Bitcoin, a função de hash SHA-256 é o capitão do navio. Outras funções, como SHA-512, são usadas para derivação com HMAC e PBKDF. Além disso, RIPMD160 é usada para reduzir uma impressão digital para 160 bits. Quando falamos de HASH256 e HASH160, estamos nos referindo ao uso de hash duplo com SHA-256 e RIPMD. O uso de HASH160 é particularmente vantajoso porque permite aproveitar a segurança do SHA-256 enquanto reduz o tamanho da impressão digital.

Resumindo, o objetivo final de uma função de hash criptográfica é transformar uma informação de tamanho arbitrário em uma impressão digital de tamanho fixo. Para ser reconhecida como segura, ela deve ter várias cordas em seu arco: irreversibilidade, resistência à falsificação, resistência a colisões e resistência à segunda pré-imagem.

Ao final desta exploração, desmistificamos as funções de hash criptográficas, destacamos seu uso no protocolo Bitcoin e analisamos seus objetivos específicos. Aprendemos que, para serem consideradas seguras, as funções de hash devem ser resistentes à pré-imagem, à segunda pré-imagem, às colisões e à falsificação. Também percorremos a gama de diferentes funções de hash usadas no protocolo Bitcoin. Em nossa próxima sessão, mergulharemos no coração da função de hash SHA256 e descobriremos as fascinantes matemáticas que lhe conferem suas características únicas.

## Os mecanismos do SHA256

![Os mecanismos do SHA256](https://youtu.be/74SWg_ZbUj4)

Bem-vindo à continuação de nossa fascinante jornada pelos labirintos criptográficos da função de hash. Hoje, revelamos o véu sobre os mistérios do SHA256, um processo complexo, mas engenhoso, que introduzimos em nossa discussão anterior sobre funções de hash. Vamos dar mais um passo neste labirinto, começando pelo pré-processamento do SHA256. Imagine o pré-processamento como a preparação de um prato saboroso, onde adicionamos "bits de preenchimento" para que o tamanho de nosso ingrediente principal, a entrada, atinja um múltiplo perfeito de 512 bits. Tudo isso com o objetivo final de gerar um hash suculento de 256 bits a partir de um ingrediente de tamanho variado.

Nesta receita criptográfica, brincamos com os bits, tendo um tamanho de mensagem inicial que chamaremos de M. Um bit é reservado para o separador, enquanto P bits são usados para o preenchimento. Além disso, reservamos 64 bits para a segunda fase de pré-processamento. O total deve ser um múltiplo de 512 bits. Um pouco como garantir que todos os ingredientes se harmonizem perfeitamente em nosso prato.
Passamos agora à segunda fase do pré-processamento, que consiste em adicionar a representação binária do tamanho da mensagem inicial, em bits. Para isso, usamos os 64 bits reservados na etapa anterior. Adicionamos zeros para arredondar os nossos 64 bits para a nossa entrada equilibrada. Depois juntamos a mensagem inicial, o preenchimento de bits e o preenchimento de tamanho, como ingredientes num liquidificador, para obter a nossa entrada equilibrada.

Agora estamos a preparar-nos para as primeiras etapas do processamento da função SHA-256. Como em qualquer boa receita, precisamos de alguns ingredientes básicos, a que chamamos constantes e vectores de inicialização. Os vectores de inicialização, de A a H, são os primeiros 32 bits das partes decimais das raízes quadradas dos primeiros 8 primos. As constantes K, de 0 a 63, representam os primeiros 32 bits das partes decimais das raízes cúbicas dos primeiros 64 primos.

Dentro da função de compressão, usamos operadores específicos como XOR, AND e NOT. Processamos os bits um a um de acordo com a sua classificação, utilizando o operador XOR e uma tabela de verdade. O operador AND é utilizado para devolver 1 apenas se ambos os operandos forem iguais a 1, e o operador NOT para devolver o valor oposto de um operando. Também usamos a operação SHR para deslocar os bits para a direita por um número escolhido.

Finalmente, depois de dividir a entrada equilibrada em diferentes blocos de mensagens de 512 bits, efectuamos 64 voltas de computação na função de compressão. Como numa corrida de bicicletas, cada volta melhora a nossa posição. Adicionamos o estado intermédio ao estado inicial da função de compressão, modulo 2^32. As adições na função de compressão são adições de módulo 2^32 para manter o tamanho das somas em 32 bits.

Para concluir, gostaríamos de realçar o papel crucial dos cálculos efectuados nas caixas CH, SHIFT, σ0 e σ1. Essas operações, entre outras, são os guardiões que garantem a robustez da função hash SHA256 contra ataques, tornando-a uma escolha preferida para proteger muitos sistemas digitais, inclusive dentro do protocolo Bitcoin. É, portanto, claro que, embora complexo, a beleza do SHA256 reside na sua robustez em encontrar a entrada a partir do hash, enquanto que verificar o hash para uma determinada entrada é uma acção mecanicamente simples.

## Algoritmos usados para a derivação

![Os algoritmos usados para a derivação](https://youtu.be/ZF1_BMsOJXc)

Os algoritmos de derivação HMAC e PBKDF2 são componentes-chave na mecânica de segurança do protocolo Bitcoin. Eles previnem uma variedade de ataques potenciais e garantem a integridade das carteiras Bitcoin.

HMAC e PBKDF2 são ferramentas criptográficas usadas para diferentes tarefas no Bitcoin. HMAC é principalmente usado para combater ataques de extensão de comprimento durante a derivação de carteiras hierarquicamente determinísticas (HD), enquanto PBKDF2 é usado para converter uma frase mnemônica em uma semente.

HMAC, que recebe uma mensagem e uma chave como entrada, gera uma saída de tamanho fixo. Para garantir a uniformidade, a chave é ajustada de acordo com o tamanho dos blocos usados na função de hash. No caso da derivação de carteiras HD, é usado o HMAC-SHA-512. Este último funciona com blocos de 1024 bits (128 bytes) e ajusta a chave de acordo. Ele usa as constantes OPAD (0x5c) e IPAD (0x36), repetidas quantas vezes forem necessárias para reforçar a segurança.

O processo de HMAC-SHA-512 envolve a concatenação do resultado de SHA-512 aplicado à chave XOR OPAD e à chave XOR IPAD com a mensagem. Quando usado com blocos de 1024 bits (128 bytes), a chave de entrada é preenchida com zeros, se necessário, e depois XORada com IPAD e OPAD. A chave assim modificada é então concatenada com a mensagem.

O código de cadeia, ao integrar uma fonte adicional de entropia, aumenta a segurança das chaves derivadas. Sem ele, um ataque poderia comprometer toda a carteira e roubar todos os bitcoins.

PBKDF2 é usado para converter uma frase mnemônica em uma semente. Este algoritmo realiza 2048 rodadas usando HMAC SHA512. Graças a esses algoritmos de derivação, duas entradas diferentes podem produzir uma saída única e fixa, o que corrige o problema de possíveis ataques de extensão de comprimento em funções da família SHA-2.

Um ataque de extensão de comprimento explora uma propriedade específica de algumas funções de hash criptográficas. Nesse tipo de ataque, um invasor que já possui o hash de uma mensagem desconhecida pode usá-lo para calcular o hash de uma mensagem mais longa, que é uma extensão da mensagem original. Isso muitas vezes é possível sem conhecer o conteúdo da mensagem original, o que pode levar a falhas de segurança importantes se esse tipo de função de hash for usado para tarefas como verificação de integridade.
Em conclusão, os algoritmos HMAC e PBKDF2 desempenham papéis essenciais na segurança da derivação de carteiras HD no protocolo Bitcoin. O HMAC-SHA-512 é usado para se proteger contra ataques de extensão de comprimento, enquanto o PBKDF2 permite a conversão da frase mnemônica em semente. O código de cadeia adiciona uma fonte adicional de entropia na derivação das chaves, garantindo a robustez do sistema.

# As assinaturas digitais

## Assinaturas digitais e curvas elípticas

![Assinaturas digitais e curvas elípticas](https://youtu.be/gOjYiPkx4z8)

No mundo das criptomoedas, a segurança das transações é primordial. No coração do protocolo Bitcoin, encontramos o uso de assinaturas digitais que servem como provas matemáticas demonstrando a posse de uma chave privada associada a uma chave pública específica. Essa técnica de proteção de dados é essencialmente baseada em um fascinante campo da criptografia chamado criptografia de curvas elípticas (ECC).

A criptografia de curvas elípticas é a espinha dorsal da segurança das transações Bitcoin. Essas curvas elípticas, que lembram as curvas matemáticas que estudamos na escola, são úteis em uma variedade de aplicações criptográficas, desde trocas de chaves até criptografia assimétrica e criação de assinaturas digitais. Um detalhe interessante que distingue as curvas elípticas é sua simetria: qualquer linha não vertical que corta dois pontos da curva intersectará um terceiro ponto.

Agora, vamos aprofundar um pouco mais: o protocolo Bitcoin usa uma curva elíptica particular chamada SecP256K1 para realizar suas operações criptográficas. Essa curva, definida em um conjunto finito de inteiros positivos módulo um número primo de 256 bits, pode ser visualizada como uma nuvem de pontos em vez de uma curva tradicional. É essa concepção única que permite ao Bitcoin garantir efetivamente suas transações.

Quanto à escolha da curva secp256k1 para o Bitcoin, é interessante notar que ela foi preferida à curva secp256r1. Essa curva é definida pelos parâmetros a=0 e b=7, e sua equação é y² = x³ + 7 módulo n, com n representando o número primo que determina a ordem da curva.

Quando falamos das constantes usadas no sistema Bitcoin, geralmente nos referimos aos parâmetros específicos do algoritmo Elliptic Curve Digital Signature Algorithm (ECDSA) e do sistema de curvas elípticas usado pelo Bitcoin, que é a curva secp256k1. Aqui estão esses parâmetros:

- champ primaire (p): Bitcoin utiliza uma curva sobre um campo primário, então p é o primeiro número usado para definir esse campo. Para a curva secp256k1, p é igual a `p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F` em hexadecimal ou p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 -1 em decimal.
- ordem da curva (n): Este é o número de pontos na curva, incluindo o ponto no infinito. Para secp256k1, n é igual a `n = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141` em hexadecimal ou n = 2^256 - 432420386565659656852420866394968145599 em decimal.
- ponto gerador (G): O ponto base, ou gerador, é o ponto na curva a partir do qual todas as outras chaves públicas são geradas. Ele tem coordenadas x e y específicas, geralmente representadas em hexadecimal. Para secp256k1, as coordenadas G são, em hexadecimal:
  - `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
  - `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

Observe que todos os valores hexadecimais são geralmente representados na base 16, enquanto os valores decimais estão na base 10. Além disso, todas as operações nessas constantes são realizadas módulo p para as coordenadas de pontos na curva e módulo n para operações de chave e assinatura.

Então, onde estão armazenados esses famosos bitcoins? Não em uma carteira Bitcoin, como se poderia pensar. Na verdade, uma carteira Bitcoin mantém as chaves privadas necessárias para provar a posse dos bitcoins. Os próprios bitcoins são registrados na blockchain, um banco de dados descentralizado que arquiva todas as transações.

No sistema Bitcoin, a unidade de conta é o bitcoin (observe o "b" minúsculo). Este é divisível até oito casas decimais, sendo a menor unidade o satoshi. Os UTXOs, ou "Unspent Transaction Outputs", representam as saídas de transações não gastas pertencentes a um usuário. Para gastar esses bitcoins, é necessário demonstrar a posse da chave privada correspondente à chave pública vinculada a cada UTXO.
Para garantir a segurança das transações, o Bitcoin utiliza dois protocolos de assinatura digital: ECDSA (Elliptic Curve Digital Signature Algorithm) e Schnorr. O ECDSA é um protocolo de assinatura integrado ao Bitcoin desde o seu lançamento em 2009, enquanto as assinaturas de Schnorr foram adicionadas mais recentemente, em novembro de 2021. Embora esses dois protocolos se baseiem na criptografia de curvas elípticas e usem mecanismos matemáticos semelhantes, eles diferem principalmente em termos de estrutura de assinatura.

Antes de mergulhar mais profundamente nesses mecanismos de assinatura, é importante entender o que é uma curva elíptica. Uma curva elíptica é definida pela equação y² = x³ + ax + b. Qualquer ponto nesta curva tem uma simetria distintiva que é a chave para sua utilidade em criptografia.

No final das contas, várias curvas elípticas são reconhecidas como seguras para uso criptográfico. O mais conhecido talvez seja a curva secp256r1. No entanto, para o Bitcoin, Satoshi Nakamoto optou por outra curva: a secp256k1.

Na próxima seção deste curso, examinaremos mais de perto a chave pública e a chave privada para uma compreensão aprofundada da criptografia em curvas elípticas e do algoritmo de assinatura digital. Este será o momento de consolidar seus conhecimentos e entender como todas essas informações se articulam para garantir a segurança do protocolo Bitcoin.

## Calculando a chave pública a partir da chave privada

![Calculando a chave pública a partir da chave privada](https://youtu.be/NJENwFU889Y)

Na continuação deste curso, vamos nos aprofundar nos mecanismos das chaves públicas e privadas, dois elementos cruciais do protocolo Bitcoin. Essas chaves estão intrinsecamente ligadas pelo algoritmo Elliptic Curve Digital Signature Algorithm (ECDSA). Compreendê-las nos dará uma visão profunda de como o Bitcoin garante a segurança das transações em sua plataforma.

Para começar, vamos mergulhar no universo do algoritmo ECDSA. O Bitcoin utiliza este algoritmo de assinatura digital para vincular as chaves privadas e públicas. Neste sistema, a chave privada é um número aleatório ou pseudo-aleatório de 256 bits. O número total de possibilidades para uma chave privada é teoricamente de 2^256, mas é ligeiramente inferior a isso na realidade. Para ser preciso, algumas chaves privadas de 256 bits não são válidas para o Bitcoin.
Para ser compatível com o Bitcoin, uma chave privada deve estar entre 1 e n-1, onde n representa a ordem da curva elíptica. Isso significa que o número total de possibilidades para uma chave privada do Bitcoin é quase igual a 1,158 x 10^77. Para colocar isso em perspectiva, é aproximadamente o mesmo número de átomos presentes no universo observável. A chave privada única é então usada para determinar uma chave pública de 512 bits.

A chave pública, indicada por K, é um ponto na curva elíptica que é derivado da chave privada usando operações de pontos na curva. É importante notar que a função ECDSA é irreversível, ou seja, é impossível recuperar a chave privada a partir da chave pública. Essa irreversibilidade é a pedra angular da segurança da carteira Bitcoin.

A chave pública é composta por dois pontos de 256 bits cada, totalizando 512 bits. No entanto, pode ser comprimida em um número de 264 bits. O ponto G é o ponto de partida para calcular todas as chaves públicas dos usuários do sistema.

Uma das propriedades notáveis das curvas elípticas é que uma linha que intersecta a curva em dois pontos também intersectará um terceiro ponto, chamado de ponto O. Essa propriedade é usada para determinar o ponto U, que é o oposto do ponto O. A adição de um ponto a si mesmo é feita traçando uma tangente à curva no ponto, o que dá um novo ponto único chamado j. O produto escalar de um ponto por n é igual a adicionar esse ponto a si mesmo n vezes.

Essas operações nos pontos de uma curva elíptica são a base do cálculo das chaves públicas. Sabendo a chave privada, é fácil calcular a chave pública. No entanto, saber a chave pública não permite calcular a chave privada, garantindo assim a segurança do sistema Bitcoin. De fato, a segurança das chaves públicas e privadas é baseada no problema do logaritmo discreto, uma questão matemática complexa.

Em nosso próximo curso, exploraremos como uma assinatura digital é realizada usando o algoritmo ECDSA com uma chave privada para desbloquear bitcoins. Fique ligado para esta emocionante exploração do mundo das criptomoedas e da criptografia.

## Assinar com a chave privada

![Assinar com a chave privada](https://youtu.be/h2hIyGgPqkM)
Le processo de assinatura digital é um método chave para provar que você é o detentor de uma chave privada sem precisar revelá-la. Isso é feito usando o algoritmo ECDSA, que envolve a determinação de um nonce único, o cálculo de um número específico, V, e a criação de uma assinatura digital composta por duas partes, S1 e S2. É crucial sempre usar um nonce único para evitar ataques de segurança. Um exemplo notório do que pode acontecer quando essa regra não é seguida é o caso do hackeamento do PlayStation 3, que foi comprometido devido à reutilização do nonce.

De forma precisa, para validar uma assinatura digital usando o algoritmo ECDSA (Elliptic Curve Digital Signature Algorithm), as seguintes etapas geralmente estão envolvidas:

1. Verifique se os valores da assinatura, S1 e S2, estão no intervalo [1, n-1]. Se não estiverem, a assinatura é inválida.
2. Calcule o inverso de S2 mod n. Vamos chamar isso de u. Isso é frequentemente calculado como: u = (S2)^-1 mod n.
3. Calcule H, que é o valor de hash da mensagem assinada.
4. Calcule u1 = H _ u mod n e u2 = S1 _ u mod n.
5. Calcule o ponto P na curva elíptica usando u1, u2 e a chave pública K: P = u1*G + u2*K, onde G é o ponto de geração da curva.
6. Se P for o ponto no infinito, a assinatura é inválida.
7. Calcule I = coordenada x de P mod n.
8. A assinatura é válida se I for igual a S1.

É importante notar que cada software pode usar diferentes notações e algumas etapas podem ser combinadas ou reorganizadas, mas a lógica básica é a mesma. Observe também que todas as operações aritméticas são realizadas no corpo finito definido pela curva elíptica (mod n, onde n é a ordem da curva). Como lembrete, a curva secp256k1 (usada no Bitcoin) n = 2^256 - 432420386565659656852420866394968145599.

Quanto à geração de chaves públicas e privadas, é essencial se familiarizar com a curva elíptica e o ponto gerador. Para obter uma chave pública, um número aleatório deve ser escolhido como chave privada, frequentemente chamado de `nonce`, e usado na equação da curva elíptica.
La curva elíptica é uma ferramenta poderosa para gerar chaves públicas e privadas seguras. Por exemplo, para obter a chave pública 3G, você desenha uma tangente no ponto G, calcula o oposto de -G para obter 2G e, em seguida, adiciona G e 2G. Para realizar uma transação, você deve provar que conhece o número 3 desbloqueando os bitcoins associados à chave pública 3G.

Para criar uma assinatura digital e provar que você conhece a chave privada associada à chave pública 3G, você primeiro calcula um nonce e, em seguida, o ponto V associado a esse nonce (no exemplo dado, é 4G). Em seguida, você calcula o ponto T adicionando a chave pública 3G e o ponto V, o que resulta em 7G.

A verificação de uma assinatura digital é uma etapa crucial no uso do algoritmo ECDSA, que permite confirmar a autenticidade de uma mensagem assinada sem precisar da chave privada do remetente. Aqui está como isso acontece em detalhes:

Em nosso exemplo, temos duas valores importantes: T e V. T é um valor numérico (7 neste exemplo) e V é um ponto na curva elíptica (representado por 4G aqui). Esses valores são produzidos durante a criação da assinatura digital e são enviados com a mensagem para permitir a verificação.

Quando o verificador recebe a mensagem, ele também receberá esses dois valores, T e V.

Aqui estão as etapas que o verificador seguirá para validar a assinatura:

1. Ele primeiro calculará o hash da mensagem, que chamaremos de H.
2. Em seguida, ele calculará u1 e u2. Para fazer isso, ele usará as seguintes fórmulas:
   - u1 = H \* (S2)^-1 mod n
   - u2 = T \* (S2)^-1 mod n
     Onde S2 é a segunda parte da assinatura digital, n é a ordem da curva elíptica e (S2)^-1 é o inverso de S2 mod n.
3. O verificador então calculará um ponto P' na curva elíptica usando a fórmula: P' = u1 _ G + u2 _ K
   - G é o ponto de geração da curva
   - K é a chave pública do remetente
4. O verificador então calculará I', que é simplesmente a coordenada x do ponto P' modulo n.
5. Finalmente, o verificador confirmará se I' é igual a T. Se for o caso, a assinatura é considerada válida. Se não for o caso, a assinatura é inválida.

Este procedimento garante que apenas o remetente que possui a chave privada correspondente poderia ter produzido uma assinatura que passa por este processo de verificação.
En conclusão, a verificação de uma assinatura digital ECDSA é um procedimento essencial nas transações Bitcoin. Isso garante que a mensagem assinada não foi alterada durante a transmissão e que o remetente é o detentor da chave privada. Essa técnica de autenticação digital é baseada em princípios matemáticos complexos, incluindo a aritmética de curva elíptica, mantendo a confidencialidade da chave privada. Ela oferece uma base sólida de segurança para transações criptográficas.

Dito isso, a gestão dessas chaves, bem como sua criação, é outra questão essencial no Bitcoin. Como gerar um novo par de chaves? Como organizar várias chaves de forma segura e eficiente? Como recuperá-las, se necessário?

Para responder a essas perguntas e aprofundar sua compreensão da segurança da criptografia, nosso próximo curso se concentrará no conceito de Carteira Determinística Hierárquica (HD wallets) e no uso de frases mnemônicas. Esses mecanismos oferecem maneiras elegantes de gerenciar efetivamente suas chaves de criptomoeda, ao mesmo tempo em que reforçam a segurança e a recuperabilidade.

# A frase mnemônica

## Evolução das carteiras Bitcoin

![Evolução das carteiras Bitcoin](https://youtu.be/6tmu1R9cXyk)

A Carteira Determinística Hierárquica, ou mais comumente chamada de carteira HD, desempenha um papel importante no ecossistema de criptomoedas. O termo "carteira" pode parecer enganoso para os novatos nesse campo, pois não implica a posse de dinheiro ou moedas. Em vez disso, refere-se a uma coleção de chaves criptográficas privadas derivadas de uma única chave mestra, por meio de um processo engenhoso de aritmética algorítmica. Essas chaves privadas, que têm um comprimento fixo de 256 bits, são a essência da posse de criptomoedas e às vezes são referidas como "Just a Bunch Of Keys" (JBOC).

No entanto, a complexidade da gestão dessas chaves é compensada por um conjunto de protocolos, chamados de Propostas de Melhoria do Bitcoin (BIP). Essas propostas de atualização estão no cerne da funcionalidade e segurança das carteiras HD. Por exemplo, o [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), lançado em 2012, revolucionou a maneira como essas chaves são geradas e armazenadas, introduzindo o conceito de chaves derivadas de forma determinística e hierárquica. Assim, o processo de backup dessas chaves é muito simplificado, mantendo seu nível de segurança.
Posteriormente, o [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) introduziu uma inovação marcante: a frase mnemônica de 24 palavras. Esse sistema permitiu transformar uma sequência complexa de números difícil de lembrar em uma série de palavras comuns, muito mais fáceis de memorizar e armazenar. Além disso, o [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) propôs adicionar uma frase de senha adicional para reforçar a segurança das chaves individuais. Essas melhorias sucessivas levaram às normas BIP43 e BIP44, que padronizaram a estrutura e a hierarquização das carteiras HD, tornando essas carteiras mais acessíveis e fáceis de usar para o público em geral.

Nas seções seguintes, vamos mergulhar mais profundamente no funcionamento das carteiras HD. Abordaremos os princípios de derivação de chaves e examinaremos os conceitos fundamentais de entropia e geração de números aleatórios, que são essenciais para garantir a segurança da sua carteira HD.

Como síntese, é essencial destacar o papel central dos BIP32 e BIP39 no design e segurança das carteiras HD. Esses protocolos permitem gerar uma infinidade de chaves a partir de uma única semente, que é suposta ser um número aleatório ou pseudoaleatório. Hoje, essas normas são adotadas pela maioria das carteiras de criptomoedas, sejam elas dedicadas a uma única criptomoeda ou que suportem vários tipos de moedas.

Espero que esta introdução tenha ajudado você a entender melhor os fundamentos da carteira HD e suas diversas características. Nosso objetivo é ajudá-lo a dominar esses conceitos essenciais e a navegar de forma mais eficiente no universo complexo das criptomoedas. Então, fique conosco enquanto continuamos a explorar as sutilezas e nuances deste mundo fascinante nas próximas lições.

## Entropia e número aleatório

![Entropia e número aleatório](https://youtu.be/k18yH18w2TE)
A importância da segurança das chaves privadas no ecossistema do Bitcoin é incontestável. Elas são, de fato, a pedra angular que garante a segurança das transações Bitcoin. Para evitar qualquer vulnerabilidade associada à previsibilidade, essas chaves devem ser geradas de forma verdadeiramente aleatória, o que pode rapidamente se tornar um exercício trabalhoso para o usuário. Uma solução para esse enigma é a Carteira Determinística Hierárquica, ou carteira HD. Este método permite gerar de forma determinística e hierárquica pares de chaves filhas a partir de uma única informação na base da carteira. É aqui que a aleatoriedade se torna indispensável para garantir a segurança das chaves derivadas.

A geração de números aleatórios é, de fato, um elemento crucial em criptografia, para garantir a integridade das chaves privadas. Para prevenir qualquer vulnerabilidade relacionada à previsibilidade, uma chave privada deve ser produzida de forma aleatória. O uso de um novo par de chaves para cada transação permite reforçar ainda mais a segurança, embora isso torne a sua salvaguarda mais complexa e preserve a confidencialidade apenas parcialmente. Em resumo, a segurança das chaves privadas é uma prioridade absoluta, exigindo uma geração rigorosa e aleatória. As carteiras HD oferecem uma solução para facilitar a geração e gestão das chaves, mantendo um alto nível de segurança.

No entanto, a geração de números aleatórios em computadores apresenta um grande desafio, uma vez que os resultados obtidos não são verdadeiramente aleatórios. É por isso que é essencial usar um Gerador de Números Aleatórios (RNG). Os tipos de RNG variam, desde Geradores de Números Pseudo-Aleatórios (PRNG) até Geradores de Números Verdadeiramente Aleatórios (TRNG), bem como PRNGs que incorporam uma fonte de entropia.

No caso do Bitcoin, as chaves privadas são geradas a partir de uma única informação na base da carteira. Essa informação permite uma derivação determinística e hierárquica de pares de chaves filhas. A entropia é a base de toda carteira HD, embora não haja um padrão para a geração desse número aleatório. Portanto, a geração de números aleatórios é uma questão importante para garantir a segurança das transações Bitcoin.

A fase de verificação da geração das chaves é crucial para garantir a segurança e autenticidade da geração de números aleatórios, uma etapa fundamental para prevenir qualquer vulnerabilidade associada à previsibilidade. Portanto, é altamente recomendável usar carteiras de código aberto para permitir essa verificação.
Cependant, é importante notar que algumas carteiras de hardware podem ser "closed source", tornando impossível a verificação da geração do número aleatório. Uma possível solução seria gerar sua própria frase mnemônica usando dados, embora essa abordagem possa apresentar alguns riscos. O uso de uma passphrase gerada aleatoriamente pode ajudar a mitigar esses riscos.

Um exemplo de aplicação desse método é a opção "dice roll" oferecida pelo CoinKit para gerar frases mnemônicas. Outra possibilidade seria usar uma informação inicial muito ampla e reduzir essa informação para 256 bits com a função de hash SHA-256, capaz de gerar um bom número aleatório. É importante mencionar que a função de hash SHA-256 é resistente a colisões, falsificação e ataques de pré-imagem e segunda pré-imagem.

Em última análise, o aleatório ocupa um lugar central na criptografia e na informática, e a capacidade de gerar aleatoriedade de forma segura é crucial para garantir a segurança das chaves privadas e das transações Bitcoin. A entropia, que está no cerne da carteira HD do Bitcoin, é essencial para sua segurança. Em nossa próxima lição, continuaremos a explorar esse assunto, abordando mais detalhadamente como a entropia contribui para a segurança das carteiras HD.

### Apoie-nos

Este curso, bem como todo o conteúdo presente nesta universidade, foi oferecido gratuitamente pela nossa comunidade. Para nos apoiar, você pode compartilhá-lo com seus amigos, tornar-se um membro da universidade e até mesmo contribuir para o seu desenvolvimento via GitHub. Em nome de toda a equipe, obrigado!

### Avalie o curso

Um sistema de avaliação para o curso será em breve integrado a esta nova plataforma de E-learning! Enquanto isso, muito obrigado por seguir o curso e se você gostou, pense em compartilhá-lo com seus amigos.

## A frase mnemônica

![A frase mnemônica](https://youtu.be/uJERqH9Xp7I)

A segurança de uma carteira Bitcoin é uma preocupação importante para todos os seus usuários. Uma maneira essencial de garantir a segurança da carteira é gerar uma frase mnemônica baseada na entropia e na checksum.

A entropia é o pilar da segurança da carteira HD. Existem várias maneiras de gerar essa entropia, incluindo geradores de números pseudoaleatórios (PRNG), geradores de números aleatórios verdadeiros (TRNG) ou manualmente. É crucial que essa entropia seja aleatória ou pseudoaleatória para garantir a segurança da carteira.
De seu lado, o checksum garante a verificação da exatidão da frase de recuperação. Sem esse checksum, um erro na frase pode levar à criação de uma carteira diferente e, portanto, à perda dos fundos. O checksum é obtido passando a entropia pela função SHA256 e recuperando os 8 primeiros bits do hash.

Existem diferentes padrões para a frase mnemônica, dependendo do tamanho da entropia. O padrão mais comumente usado para uma frase de recuperação de 24 palavras é uma entropia de 256 bits. O tamanho do checksum é determinado dividindo o tamanho da entropia por 32.

Por exemplo, uma entropia de 256 bits gera um checksum de 8 bits. A concatenação da entropia e do checksum leva a tamanhos respectivos de 128 bits, 160 bits, etc. Dependendo do tamanho da entropia, a frase de recuperação terá 12 palavras para 128 bits, 15 palavras para 160 bits e 24 palavras para 256 bits.

Para transformar bits em palavras, cada segmento é associado a uma palavra de uma lista de 2048 palavras. É importante observar que nenhuma palavra apresenta as quatro primeiras letras na mesma ordem.

É essencial salvar a frase de recuperação de 24 palavras para preservar a integridade da carteira Bitcoin. Os dois padrões mais comumente usados são baseados em uma entropia de 128 ou 256 bits e uma concatenação de 12 ou 24 palavras. Adicionar uma passphrase é uma opção adicional para reforçar a segurança da carteira.

Em conclusão, a geração de uma frase mnemônica para proteger uma carteira Bitcoin é um processo crucial. É importante seguir os padrões da frase mnemônica de acordo com o tamanho da entropia. Salvar a frase de recuperação de 24 palavras é essencial para evitar perda de fundos. Agradecemos sua atenção e esperamos vê-lo em nosso próximo curso sobre criptomoedas.

## A passphrase

![A passphrase](https://youtu.be/dZkOYO7MXwc)

A passphrase é uma senha adicional que pode ser adicionada a uma carteira Bitcoin para aumentar sua segurança. Seu uso é opcional e depende da apreciação do usuário. Ao adicionar informações arbitrárias que, juntamente com a frase mnemônica, permitem calcular a semente da carteira, a passphrase reforça a segurança da mesma.
Para derivar as chaves de uma carteira HD, a frase mnemônica e a passphrase são necessárias. A passphrase é livre e pode ter um tamanho quase infinito. Ela não está incluída na frase mnemônica, que é padronizada e deve seguir certas restrições de tamanho, checksum e codificação. Um atacante não pode acessar os bitcoins de um usuário sem conhecer a passphrase. Esta última desempenha um papel na construção e cálculo de todas as chaves da carteira.

A função pbkdf2 é usada para gerar a semente a partir da passphrase. Esta semente permite derivar todos os pares de chaves filhas da carteira. Se a passphrase for alterada, a carteira Bitcoin se torna completamente diferente.

A passphrase é uma ferramenta essencial para reforçar a segurança das carteiras Bitcoin. Ela pode permitir a aplicação de várias estratégias de segurança. Por exemplo, ela pode ser usada para criar duplicatas e facilitar o backup da frase mnemônica. Ela também pode melhorar a segurança da carteira, reduzindo os riscos associados à geração aleatória da frase mnemônica.

Uma passphrase eficaz deve ser longa (20 a 40 caracteres) e diversificada (usando maiúsculas, minúsculas, números e símbolos). Ela não deve estar diretamente relacionada ao usuário ou ao seu ambiente. É mais seguro usar uma sequência aleatória de caracteres em vez de uma palavra simples como passphrase.

Uma passphrase é mais segura do que uma simples senha. A passphrase ideal é longa, variada e aleatória. Ela pode reforçar a segurança de uma carteira ou de um software quente. Ela também pode ser usada para criar backups redundantes e seguros.

É crucial cuidar dos backups da passphrase para evitar perder o acesso à carteira. Uma passphrase é uma opção para uma carteira HD. Ela pode ser gerada aleatoriamente com dados ou outro gerador de números pseudoaleatórios. Não é recomendável memorizar uma passphrase ou uma frase mnemônica.

Em nosso próximo curso, examinaremos em detalhes o funcionamento da semente e o primeiro par de chaves gerado a partir dela. Não hesite em seguir este curso para continuar sua aprendizagem. Mal podemos esperar para vê-lo novamente em breve.

## Criação de uma semente a partir de 128 lançamentos de dados!

![Criação de uma semente a partir de 128 lançamentos de dados!](https://youtu.be/lUw-1kk75Ok)
A criação de uma frase mnemônica é um passo crucial para a segurança da sua carteira de criptomoedas. Existem várias maneiras de gerar uma frase mnemônica, no entanto, vamos nos concentrar no método de geração manual usando dados. É importante destacar que este método não é adequado para uma carteira de grande valor. É recomendável usar um software de código aberto ou uma carteira de hardware para gerar a frase mnemônica. Para criar uma frase mnemônica, usaremos dados para gerar informações binárias. O objetivo é entender o processo de criação da frase mnemônica.

**Passo 1 - Preparação:**
Certifique-se de ter uma distribuição Linux amnésica, como o Tails OS, instalada em um pendrive para maior segurança. Observe que este tutorial não deve ser usado para criar uma carteira principal.

**Passo 2 - Geração de um número binário aleatório:**
Usaremos dados para gerar informações binárias. Jogue um dado 128 vezes e anote cada resultado (1 para ímpar, 0 para par).

**Passo 3 - Organização dos números binários:**
Organize os números binários obtidos em linhas de 11 dígitos para facilitar os cálculos posteriores. A décima segunda linha deve ter apenas 7 dígitos.

**Passo 4 - Cálculo do checksum:**

Os últimos 4 dígitos da décima segunda linha correspondem ao checksum. Para calcular este checksum, precisamos usar um terminal de uma distribuição Linux. É recomendável usar o [TailOs](https://tails.boum.org/index.fr.html), que é uma distribuição sem memória inicializável a partir de um pendrive. Uma vez no seu terminal, digite o comando `echo <número binário> | shasum -a 254 -0`. Substitua `<número binário>` pela sua lista de 128 zeros e uns. A saída é um hash em hexadecimal. Anote o primeiro caractere deste hash e converta-o em binário. Você pode usar esta [tabela](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) para ajudá-lo. Adicione o checksum em binário (4 dígitos) à décima segunda linha da sua folha.

**Passo 5 - Conversão em decimal:**
Para encontrar as palavras associadas a cada uma de suas linhas, você precisa primeiro converter em decimal cada série de 11 bits. Aqui você não pode usar um conversor online porque esses bits representam sua frase mnemônica. Portanto, você precisará converter usando uma calculadora e um truque que é o seguinte: cada bit está associado a uma potência de 2, então da esquerda para a direita temos 11 posições que correspondem a 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, respectivamente. Para converter sua série de 11 bits em decimal, basta adicionar apenas as posições que contêm um 1. Por exemplo, para a série 00110111011, isso corresponde à seguinte adição: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Agora você pode converter cada linha em decimal. E antes de passar para a codificação em palavras, é necessário adicionar +1 a todas as linhas, pois o índice da lista de palavras BIP39 começa a partir de 1 e não 0.

**Etapa 8 - Geração da frase mnemônica:**
Comece imprimindo a [lista de 2048 palavras](https://seedxor.com/files/wordlist.pdf) para fazer a conversão entre seus números decimais e as palavras do BIP39. A particularidade desta lista é que nenhuma palavra tem as mesmas 4 primeiras letras em comum com todas as outras palavras deste dicionário. Em seguida, procure para cada uma de suas linhas a palavra associada ao número decimal.

**Etapa 9 - Teste da frase mnemônica:**
Teste imediatamente sua frase mnemônica no Sparrow Wallet criando uma carteira a partir dela. Se você receber um erro de checksum inválido, é provável que tenha cometido um erro de cálculo. Corrija esse erro voltando para a etapa 4 e teste novamente no Sparrow Wallet. Pronto! Você acabou de criar uma nova carteira Bitcoin a partir de 128 lançamentos de dados.

Gerar uma frase mnemônica é um processo importante para proteger sua carteira de criptomoedas. É recomendável usar métodos mais seguros, como o uso de software de código aberto ou hardware wallet, para gerar a frase mnemônica. No entanto, realizar esta oficina permite entender melhor como a partir de um número aleatório podemos criar uma carteira Bitcoin.

# Criação de uma carteira Bitcoin

## Criação da semente e da chave mestra

![Criação da semente e da chave mestra](https://youtu.be/56yAt_JDWhY)

Nesta parte do curso, vamos explorar as etapas de derivação de uma carteira HD (Hierarchical Deterministic Wallet), que permite criar e gerenciar chaves privadas e públicas de forma hierárquica.
A base da carteira HD assenta em dois elementos essenciais: a frase mnemónica e a frase-chave (palavra-passe adicional opcional). Juntos, eles formam a semente, uma sequência alfanumérica de 512 bits que serve como base para derivar as chaves da carteira. A partir dessa semente, é possível derivar todos os pares de chaves filhos da carteira Bitcoin. A semente é a chave para aceder a todos os bitcoins associados à carteira, quer se utilize uma frase-chave ou não.

Para obter a semente, usamos a função pbkdf2 (Password-Based Key Derivation Function 2) com a frase mnemónica e a frase-chave. O resultado da pbkdf2 é uma semente de 512 bits. A chave privada mestre e o código de cadeia mestre são determinados utilizando o algoritmo HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512). Este algoritmo requer uma mensagem e uma chave para gerar um resultado. A chave privada mestre é calculada a partir da semente e da frase "Bitcoin SEED". Esta frase é idêntica para todos os derivados da carteira HD, garantindo a consistência entre carteiras.

Inicialmente, a função SHA-512 não foi implementada no protocolo Bitcoin, e é por isso que o HMAC SHA-512 é usado. A utilização do HMAC SHA-512 com a frase "Bitcoin SEED" obriga o utilizador a gerar uma carteira específica para Bitcoin. O resultado do HMAC SHA-512 é um número de 512 bits, dividido em duas partes: os 256 bits da esquerda representam a chave privada mestra, enquanto os 256 bits da direita representam o código da cadeia mestra.

A chave privada mestra é a chave-mãe de todas as chaves futuras na carteira, enquanto o código da cadeia mestra é utilizado para derivar as chaves-filhas. É importante notar que é impossível derivar um par de chaves filho sem conhecer o código de cadeia correspondente do par pai. O código da cadeia acrescenta uma fonte de entropia ao processo de derivação.

Um par de chaves na carteira é composto por uma chave privada, uma chave pública e um código de cadeia. O código da cadeia introduz uma fonte de aleatoriedade na derivação das chaves filhas e isola cada par de chaves para evitar a fuga de informação.

É importante sublinhar que a chave privada mestra é a primeira chave privada derivada da semente e não tem qualquer ligação com as chaves alargadas da carteira. A semente é, portanto, o elemento fundamental para derivar todas as chaves do portefólio. É diferente da frase mnemónica e da frase-chave, que são utilizadas para criar a semente.
Dans a próxima aula, exploraremos em detalhes as chaves estendidas, como xPub, xPRV, zPub, e entenderemos por que elas são usadas e como são construídas.

## Chaves estendidas

![Chaves estendidas](https://youtu.be/TRz760E_zUY)

Nesta parte do curso, vamos estudar as chaves estendidas (xPub, zPub, yPub) e seus prefixos, que desempenham um papel importante na derivação de chaves filhas em uma carteira HD (Hierarchical Deterministic Wallet).

As chaves estendidas se distinguem das chaves mestras. Uma carteira HD gera uma frase mnemônica e uma semente para obter a chave mestra e o código de cadeia mestre. As chaves estendidas são usadas para derivar chaves filhas e exigem tanto a chave pai quanto o código de cadeia correspondente. Uma chave estendida combina essas duas informações para simplificar o processo de derivação.

As chaves estendidas são identificadas por prefixos específicos (XPRV, XPUB, YPUB, ZPUB) que indicam se é uma chave estendida privada ou pública, bem como seu objetivo específico. Os metadados associados a uma chave estendida incluem a versão (prefixo), a profundidade, a impressão digital da chave pública, o índice e a carga útil (código de cadeia e chave pai).

A carga útil é composta pelo código de cadeia (32 bytes) e pela chave pai (33 bytes). Esses elementos são essenciais para a derivação de chaves filhas. Uma chave privada é gerada a partir de um número aleatório ou pseudoaleatório, enquanto uma chave pública é gerada usando o algoritmo ECDSA (Elliptic Curve Digital Signature Algorithm).

Cada par de chaves estendidas está associado a um código de cadeia único, que permite realizar derivações específicas. Concatenando a chave pai com o código de cadeia, obtemos uma chave estendida privada ou pública.

As chaves públicas estendidas só podem derivar chaves públicas filhas normais, enquanto as chaves privadas estendidas podem derivar chaves filhas públicas e privadas, seja em uma derivação normal ou endurecida. O uso de chaves estendidas com o prefixo XPUB permite derivar novos endereços sem voltar às chaves privadas correspondentes, oferecendo assim uma melhor segurança. Os metadados associados às chaves estendidas fornecem informações importantes sobre seu papel e posição na hierarquia das chaves.
Les chaves públicas comprimidas têm um tamanho de 33 bytes, enquanto as chaves públicas não comprimidas têm 512 bits. As chaves públicas comprimidas mantêm as mesmas informações que as chaves não comprimidas, mas com um tamanho reduzido. As chaves estendidas têm um tamanho de 82 bytes e seu prefixo é representado em base 58 através de uma conversão hexadecimal. O checksum é calculado usando a função de hash HASH256.

As derivações reforçadas começam a partir dos índices que são potências de 2 (2^31). As chaves públicas estendidas permitem apenas a derivação de chaves públicas filhas normais, enquanto as chaves privadas estendidas permitem a derivação de qualquer chave filha. É interessante notar que os prefixos mais comumente usados são xpub e zpub, que correspondem respectivamente aos padrões legacy e segwit v1 e segwit v0.

Em nosso próximo curso, abordaremos a derivação de pares de chaves filhas usando o conhecimento adquirido sobre chaves estendidas e a chave mestra da carteira.

Em conclusão, as chaves estendidas desempenham um papel essencial na criptografia e no funcionamento das carteiras HD. Compreender seu uso e cálculo é crucial para garantir a segurança das transações e a proteção de ativos digitais. Os prefixos e metadados associados às chaves estendidas permitem o uso eficiente e a derivação precisa das chaves filhas necessárias.

## Derivação de pares de chaves filhas

![Derivação de pares de chaves filhas](https://youtu.be/FXhI-GmE9Aw)

Agora, abordaremos o cálculo da semente e da chave mestra, que são os primeiros elementos essenciais para a hierarquização e derivação da carteira HD (Hierarchical Deterministic Wallet). A semente, com um comprimento de 128 a 256 bits, é gerada aleatoriamente ou a partir de uma frase secreta. Ela desempenha um papel determinístico na derivação de todas as outras chaves. A chave mestra é a primeira chave derivada da semente e permite a derivação de todos os outros pares de chaves filhas.

O código de cadeia mestra desempenha um papel importante na recuperação da carteira a partir da semente. É importante notar que todas as chaves derivadas da mesma semente terão o mesmo código de cadeia mestra.

A hierarquização e derivação da carteira HD oferecem uma gestão mais eficiente de chaves e estruturas de carteira. As chaves estendidas permitem a derivação de um par de chaves filhas a partir de um par pai usando cálculos matemáticos e algoritmos específicos.
Existem diferentes tipos de pares de chaves filho, incluindo chaves fortes e chaves normais. A chave pública alargada permite apenas a derivação de chaves públicas filhas normais, enquanto a chave privada alargada permite a derivação de todas as chaves filhas, tanto públicas como privadas, quer estejam em modo normal ou melhorado. Cada par de chaves tem um índice para o distinguir dos outros.

A derivação de chaves-filhas utiliza a função HMAC-SHA512, utilizando a chave-mãe concatenada com o índice e o código de cadeia associado ao par de chaves. As chaves filhas normais têm um índice entre 0 e 2 elevado à 31ª potência menos 1, enquanto as chaves filhas reforçadas têm um índice entre 2 elevado à 31ª potência e 2 elevado à 32ª potência menos 1.

Existem dois tipos de pares de chaves filhas: pares reforçados e pares normais. O processo de derivação da chave-filha utiliza as chaves públicas para gerar as condições de despesa, enquanto as chaves privadas são utilizadas para a assinatura. A chave pública alargada apenas permite a derivação de chaves públicas filhas normais, enquanto a chave privada alargada permite a derivação de todas as chaves filhas, tanto públicas como privadas, em modo normal ou melhorado.

A derivação melhorada utiliza a chave privada principal, enquanto a derivação normal utiliza a chave pública principal. A função HMAC-SHA512 é utilizada para a derivação melhorada, enquanto a derivação normal utiliza um resumo de 512 bits. A chave pública filha é obtida através da multiplicação da chave privada filha pelo gerador da curva elíptica.

Hierarquizar e derivar muitos pares de chaves de forma determinística cria um esquema de árvore genealógica para a derivação hierárquica. No próximo curso desta formação, estudaremos a estrutura do portefólio HD e os caminhos de derivação, com particular ênfase nas notações dos caminhos de derivação.

## Estrutura do portefólio e caminhos de derivação

![Estrutura da carteira e caminhos de derivação](https://youtu.be/etO9UxwyE2I)

Neste capítulo, vamos estudar a estrutura da árvore de derivação numa carteira HD (Hierarchical Deterministic Wallet). Já explorámos o cálculo da semente, a chave mestra e a derivação de pares de chaves filhas. Agora vamos concentrar-nos na organização das chaves dentro da carteira.
O portfólio HD usa camadas de profundidade para organizar as chaves. Cada derivação de um par pai para um par filho corresponde a uma camada de profundidade. A profundidade 0 corresponde à chave mestra e ao código de cadeia mestra.
A profundidade 1 é usada para derivar chaves filhas de acordo com um objetivo específico, que é determinado pelo índice. Os objetivos estão em conformidade com os padrões BIP 84 e Segwit v0/v1.

A profundidade 2 permite diferenciar contas de diferentes criptomoedas ou redes. Isso permite que o portfólio seja organizado de acordo com diferentes fontes de fundos.

A profundidade 3 é usada para organizar o portfólio em diferentes contas, oferecendo uma estrutura mais clara e organizada.

A profundidade 4 corresponde às cadeias interna e externa, que são usadas para endereços destinados a serem comunicados publicamente. O índice 0 está associado à cadeia externa, enquanto o índice 1 está associado à cadeia interna. Cada conta tem duas cadeias: a cadeia externa (0) e a cadeia interna (1). A profundidade 4 também é usada para gerenciar tipos de script no caso de carteiras multiassinaturas.

A profundidade 5 é usada para endereços de recebimento em uma carteira clássica. Na próxima seção, examinaremos mais detalhadamente a derivação de pares de chaves filhas.

Para cada camada de profundidade, usamos índices para diferenciar pares de chaves filhas. Índices reforçados são usados com um apóstrofo para algumas derivações. A chave pública por ano é usada como entrada para a função HMAC. O índice em um caminho de derivação indica o valor usado na função HMAC.

O índice sem apóstrofo corresponde ao índice real usado, enquanto o índice com apóstrofo corresponde ao índice real + 2^31. Derivações reforçadas usam índices de 2^31 a 2^32-1. Por exemplo, o índice 44' corresponde ao índice real 2^31 + 44.

Para gerar um endereço de recebimento específico, derivamos um par de chaves filhas da chave mestra e do código de cadeia mestra. Em seguida, usamos o índice para diferenciar os diferentes pares de chaves filhas da mesma profundidade.

Chaves estendidas, como XPUB, permitem compartilhar seu portfólio com várias pessoas. A cadeia de derivação é usada para diferenciar a cadeia externa (endereços destinados a serem comunicados) e a cadeia interna (endereços de troca).
É importante notar que diferentes profundidades são usadas em uma carteira HD de acordo com diferentes padrões. A derivação das chaves pai para as chaves filhas permite passar de uma profundidade para outra. O uso de diferentes ramos na carteira HD permite indicar os diferentes padrões seguidos.

No próximo capítulo, vamos estudar os endereços de recebimento, suas vantagens de uso e os passos para sua construção.

# O que é um endereço Bitcoin?

## Endereços Bitcoin

![Endereços Bitcoin](https://youtu.be/nqGBMjPtFNI)

Neste capítulo, vamos explorar os endereços de recebimento, que desempenham um papel crucial no sistema Bitcoin. Eles permitem receber fundos em uma transação e são gerados a partir de pares de chaves privadas e públicas. Embora exista um tipo de script chamado Pay2PublicKey que permite bloquear bitcoins em uma chave pública, os usuários geralmente preferem usar endereços de recebimento em vez desse script.

Quando um destinatário deseja receber bitcoins, ele fornece um endereço de recebimento ao remetente em vez de sua chave pública. Um endereço é na verdade um hash de uma chave pública, com um formato específico. A chave pública é derivada da chave privada filha usando operações matemáticas como adição e duplicação de pontos em curvas elípticas.

É importante notar que não é possível retroceder do endereço para a chave pública, nem da chave pública para a chave privada. O uso de um endereço permite reduzir o tamanho da informação da chave pública, que inicialmente tem 512 bits. É possível comprimir uma chave pública mantendo apenas o valor de x e adicionando um prefixo, mas essa técnica não era conhecida na época da criação do Bitcoin. O uso de um endereço, portanto, não permite economizar espaço nos blocos.

Os endereços Bitcoin foram reduzidos em tamanho para facilitar seu uso. Eles possuem um checksum, o que permite detectar erros de digitação e reduzir o risco de perda de bitcoins. Por outro lado, as chaves públicas não possuem checksum, o que significa que erros de digitação podem levar à perda dos fundos correspondentes.

Os endereços também oferecem uma segunda camada de segurança entre a informação pública e privada, tornando mais difícil a tomada de controle da chave privada. As funções de hash usadas permitem que os pares de chaves sejam resistentes a possíveis ataques de computadores quânticos. De fato, esses computadores podem potencialmente quebrar o ECDSA (Elliptic Curve Digital Signature Algorithm), mas não podem quebrar uma função de hash.
É essencial destacar que cada endereço é de uso único, o que contribui para a segurança e privacidade. A reutilização de um mesmo endereço traz graves problemas de privacidade e deve ser evitada. Além disso, cada endereço é um hash de uma chave pública, acompanhado de um checksum para reduzir o risco de perda de bitcoins.

Diferentes prefixos são usados para os endereços Bitcoin. Por exemplo, BC1Q corresponde a um endereço Segwit V0, BC1P a um endereço Taproot/Segwit V1, e os prefixos 1 e 3 são associados aos endereços Pay2PublicKeyH/Pay2ScriptH (legacy). No próximo curso, explicaremos passo a passo a derivação de um endereço a partir de uma chave pública.

Em resumo, os endereços de recebimento são um elemento essencial do sistema Bitcoin. Eles são gerados a partir de pares de chaves privadas e públicas, e servem para receber fundos em uma transação. Os endereços integram um checksum para reduzir os riscos de perda de bitcoins e são projetados para serem usados de forma única, garantindo assim a segurança e privacidade. Diferentes tipos de endereços são usados no sistema Bitcoin, oferecendo privacidade e segurança reforçadas.

## Como criar um endereço Bitcoin?

![Como criar um endereço Bitcoin?](https://youtu.be/ewMGTN8dKjI)

Neste capítulo, abordaremos a construção de um endereço de recebimento para transações Bitcoin. Um endereço de recebimento é uma representação em caracteres alfanuméricos de uma chave pública comprimida. A conversão de uma chave pública em um endereço de recebimento passa por várias etapas.

Uma das características vantajosas dos endereços de recebimento é a presença de um checksum, que permite a detecção de erros. Para isso, usamos a tecnologia de checksum BCH (Bose-Chaudhuri-Hocquenghem) que garante uma detecção precisa de erros. Essa tecnologia também contribui para a redução do número de caracteres necessários para representar um endereço, facilitando assim o seu uso.

Para começar a construção de um endereço, devemos comprimir a chave pública correspondente. Uma chave pública bruta ocupa 520 bits, mas graças à simetria da curva elíptica usada, uma curva elíptica pode ter uma abscissa x associada a dois valores possíveis para y: positivo ou negativo. Na rede Bitcoin, trabalhamos com um corpo de inteiros positivos finitos em vez do corpo dos reais. Para representar uma chave pública a partir de x, adicionamos um prefixo indicando o valor de y (par ou ímpar). A compressão de uma chave pública permite reduzir seu tamanho de 520 para 264 bits. A paridade de y em um corpo de inteiros positivos finitos corresponde à paridade de y no corpo dos reais.
Tomemos o exemplo da chave pública pertencente a Satoshi Nakamoto, com um prefixo 0,3 indicando um valor ímpar de y. Podemos então passar para a segunda etapa da construção de um endereço a partir de chaves públicas comprimidas. É possível calcular dois endereços para cada chave pública. Para isso, usamos a função SHA256 para obter o condensado (hash) da chave pública. Em seguida, aplicamos a função ripemd160 no resultado do SHA256 para obter uma sequência de caracteres. Essa sequência é então codificada em formato binário por grupos de 5 bits, aos quais metadados são adicionados para o cálculo da checksum usando o programa BCH.

No caso dos endereços legacy, usamos o duplo hash SHA256 para gerar a soma de verificação do endereço. No entanto, para os endereços Segwit V0 e V1, recorremos à tecnologia de checksum BCH para garantir a detecção de erros. O programa BCH é capaz de sugerir e corrigir erros com uma probabilidade de erro extremamente baixa. Atualmente, o programa BCH é usado para detectar e sugerir modificações a serem feitas, mas não as executa automaticamente no lugar do usuário. O cálculo da checksum com o código BCH é baseado na aritmética polinomial de Chien-Chauffage.

O programa BCH requer várias informações de entrada, incluindo o HRP (Parte Legível pelo Humano) que deve ser expandido. A expansão do HRP consiste em codificar cada letra em base 2, levando os três primeiros bits de cada caractere, inserindo um separador 0 e concatenando os cinco últimos bits de cada caractere. Os caracteres azuis convertidos em base 10 correspondem a 3 e 3 em decimal, enquanto os outros cinco caracteres laranja correspondem a 2 e 3 em base 10. A expansão do HRP em base 10 permite isolar os cinco últimos bits de cada caractere, reforçando assim a checksum.

A versão Segwit V0 é representada pelo código 00 e o "payload" está em preto, em base 10. Isso é seguido por seis caracteres reservados para a checksum. A entrada contendo os metadados é então submetida ao programa BCH para obter a checksum em base 10. A concatenação da versão, do payload e da checksum permite construir o endereço. Os caracteres em base 10 são então convertidos em caracteres bech32 usando uma tabela de correspondência. O alfabeto bech32 inclui todos os caracteres alfanuméricos, exceto 1, b, i e o, para evitar confusão.
Pour construir um endereço começando com bc1q, devemos aplicar uma função de hash (H160) a uma chave pública comprimida, depois adicionar a checksum, a versão (q), o HRP (bc) e o separador (1). Os endereços Taproot, por sua vez, começam com bc1p porque sua versão (Segwit V1) corresponde a 0+1=1, daí o uso do caractere p. Todos esses elementos são então convertidos em BCH32, uma variante da base 32 específica para o Bitcoin.

Assim, percorremos as etapas de construção de um endereço de recebimento, o uso da tecnologia de checksum BCH, bem como a construção de um endereço começando com bc1q ou bc1p usando a variante BCH32 da base 32 específica para o Bitcoin.

## Resumo da criptografia para carteiras Bitcoin

![síntese da formação](https://youtu.be/NkAYoVUMvOs)

Ao longo desta formação, estudamos em profundidade a carteira determinística hierárquica (HD) com o BIP32. A entropia desempenha um papel central nesse tipo de carteira, pois é usada para gerar uma frase mnemônica a partir de um número aleatório. Com a lista de 2048 palavras fornecida no BIP39, essa frase mnemônica pode ser codificada em uma série de palavras fáceis de lembrar. A frase mnemônica, bem como uma possível passphrase, são necessárias para gerar a seed da carteira. A passphrase atua como um sal criptográfico que adiciona uma camada adicional de proteção à carteira.

A função pbkdf2 é usada para gerar a semente a partir da frase mnemônica e da passphrase, usando um hmacha512 e 2048 iterações. A chave mestra e o código de cadeia mestra são então derivados dessa semente usando novamente a função hmacha512 com a frase "bitcoin seed". A chave privada mestra e o código de cadeia mestra são os elementos mais altos na hierarquia da carteira HD.
A derivação de uma chave filha depende de vários fatores, incluindo a chave pai e o código de cadeia correspondente. Uma chave estendida é obtida concatenando uma chave pai com seu código de cadeia, enquanto uma chave mestra é uma chave distinta. Para derivar um endereço, a chave pública comprimida é primeiro hashada usando SHA256 e RIPMD160, e então um checksum é calculado. O hash duplo SHA256 é usado para calcular o checksum no caso de um padrão legacy, enquanto o programa BCH (Bose-Chaudhuri-Hocquenghem) é usado para calcular o checksum no caso de um padrão segwit. Em seguida, uma representação no formato base 58 é usada para um padrão legacy, enquanto o formato bech32 é usado para um padrão segwit, a fim de obter o endereço da carteira HD.

Resumindo, exploramos em detalhes as funções de hash e suas características, bem como as assinaturas digitais e as curvas elípticas. Em seguida, mergulhamos no universo da carteira determinística hierárquica (HD) com o BIP32, usando a entropia e a frase secreta para gerar a semente da carteira. Também aprendemos como derivar chaves filhas e obter o endereço da carteira HD. Espero que essas informações tenham sido úteis para você, e agora o encorajo a fazer a avaliação para testar seus conhecimentos adquiridos durante o treinamento Crypto 301. Obrigado pela sua atenção.

# Agradecimentos e continue a explorar a toca do coelho

Gostaríamos de agradecer sinceramente por ter participado do treinamento Crypto 301. Esperamos que essa experiência tenha sido enriquecedora e formativa para você. Abordamos muitos tópicos emocionantes, desde matemática até criptografia e o funcionamento do protocolo Bitcoin.

Se você quiser aprofundar ainda mais o assunto, temos um recurso adicional para oferecer. Realizamos uma entrevista exclusiva com Théo Pantamis e Loïc Morel, dois especialistas renomados no campo da criptografia. Esta entrevista explora em profundidade vários aspectos do assunto e oferece perspectivas interessantes.

Não hesite em assistir a esta entrevista para continuar explorando o fascinante campo da criptografia. Esperamos que isso seja útil e inspirador em sua jornada. Mais uma vez, obrigado por sua participação e comprometimento ao longo deste treinamento.

## Entrevista com Théo Pantamis

![Entrevista com Théo Pantamis](https://youtu.be/c9MvtGJsEvY)

Aqui está um resumo da entrevista:

Nesta entrevista, Théo Pantamys, especializado em matemática e apaixonado por Bitcoin, Lightning Network e protocolos, compartilha sua jornada e reflexões sobre vários tópicos.
Théo descobriu o Bitcoin em 2009, mas seu interesse se desenvolveu mais em 2015-2016 graças a divulgadores científicos no YouTube. Ele se concentrou na matemática e criptografia do Bitcoin, bem como na comparação com outros protocolos.

Ele destaca a importância da descentralização no Bitcoin e como isso vai contra a autoridade do Estado, oferecendo uma abertura do registro. O Bitcoin também resolve o problema da regulamentação de forma eficaz.

Théo também aborda o assunto da privacidade no Bitcoin. Ele explica a importância do CoinJoin para preservar a privacidade dos usuários e evitar a divulgação de informações pessoais. Ele recomenda o uso de Wasabi e Whirlpool para melhorar o anonimato das transações.

Em seguida, Théo discute o RGB, um protocolo complexo que resolve os problemas técnicos do Bitcoin. Ele explica como o RGB usa contratos discretos para criar tokens e produtos financeiros enquanto mantém a validação do estado do contrato na blockchain do Bitcoin.

A discussão continua sobre a ameaça da computação quântica no Bitcoin. Théo menciona que seriam necessários cerca de cem qubits para quebrar a maioria dos algoritmos e, por enquanto, os computadores quânticos ainda não atingiram esse nível de potência.

Com relação ao checksum dos endereços do Bitcoin, Théo explica como os códigos BCH são usados para detectar e potencialmente corrigir erros de digitação. Ele destaca a importância do checksum para evitar a perda de bitcoins e otimizar o tamanho dos endereços.

Em conclusão, Théo compartilha recursos para aprofundar a compreensão do Bitcoin, incluindo canais do YouTube de divulgação matemática, livros recomendados e espaços no Twitter onde os desenvolvedores discutem seus trabalhos.
