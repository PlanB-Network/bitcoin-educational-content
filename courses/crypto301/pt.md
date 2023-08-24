---
name: Introdução à criptografia
goal: Compreender a criação de uma carteira Bitcoin do ponto de vista criptográfico
objectives:
  - Desmistificar a terminologia criptográfica relacionada ao Bitcoin.
  - Dominar a criação de uma carteira Bitcoin.
  - Compreender a estrutura de uma carteira Bitcoin.
  - Compreender endereços e caminho de derivação
---

# Uma jornada ao coração da criptografia

**Atenção: este curso foi totalmente traduzido pela IA e ainda não foi revisto. Se o desejar fazer, por favor contribua para [github](https://github.com/DecouvreBitcoin/sovereign-university-data/tree/main/courses/crypto301).**

Você está fascinado pelo Bitcoin? Você se pergunta como uma carteira Bitcoin funciona? Prepare-se para embarcar em uma jornada cativante ao coração da criptografia! Loïc, nosso especialista, irá guiá-lo pelos meandros da criação de uma carteira Bitcoin, revelando os mistérios por trás de termos técnicos intimidantes como hash, derivação de chaves e curvas elípticas.

Este treinamento não apenas fornecerá o conhecimento para entender a estrutura de uma carteira Bitcoin, mas também o preparará para mergulhar mais profundamente no emocionante universo da criptografia. Então, você está pronto para embarcar nessa jornada? Junte-se a nós e transforme sua curiosidade em habilidade!

+++

# Introdução à criptografia

![introdução por Rogzy](https://youtu.be/ul8zU5QWIXg)

É com grande prazer que damos as boas-vindas ao novo treinamento intitulado "Crypto 301: Introdução à criptografia e à carteira HD", orquestrado pelo especialista no assunto, Loïc Morel. Este curso irá mergulhá-lo no fascinante universo da criptografia, essa disciplina fundamental da matemática que garante a criptografia e a segurança de seus dados.

Em nossa vida cotidiana e especialmente no campo do Bitcoin, a criptografia desempenha um papel fundamental. Os conceitos relacionados a ela, como chaves privadas, públicas, endereços, caminhos de derivação, semente e entropia, estão no cerne do uso e criação de uma carteira Bitcoin. Através deste curso, Loïc explicará em detalhes como as chaves privadas são criadas e como estão relacionadas aos endereços. Loïc também dedicará uma hora para explicar os detalhes matemáticos da curva elíptica. Além disso, você entenderá por que o uso do HMAC SHA512 é importante para proteger sua carteira e qual é a diferença entre semente e frase mnemônica.
O objetivo final deste treinamento é permitir que você compreenda tecnicamente os processos de criação de uma carteira HD e os métodos criptográficos utilizados. Ao longo dos anos, as carteiras Bitcoin evoluíram para se tornarem mais fáceis de usar, mais seguras e padronizadas graças a BIPs específicos. Loïc irá ajudá-lo a entender esses BIPs para compreender as escolhas dos desenvolvedores do Bitcoin e dos criptógrafos. Como todos os treinamentos oferecidos pela nossa universidade, este é totalmente gratuito e de código aberto. Isso significa que você pode livremente utilizá-lo como quiser. Estamos ansiosos para receber seus feedbacks ao final deste curso empolgante.
![intro por loïc](https://youtu.be/mwuxXLk4Kws)

Olá a todos, eu sou Loïc Morel, seu guia nesta exploração técnica da criptografia utilizada nas carteiras Bitcoin.

Nossa jornada começa com uma imersão nas profundezas das funções de hash criptográficas. Juntos, desmontaremos as engrenagens do indispensável SHA256 e exploraremos diversos algoritmos dedicados à derivação.

Continuaremos nossa aventura desvendando o mundo misterioso das assinaturas digitais. Você descobrirá como a magia das curvas elípticas se aplica a essas assinaturas, e esclareceremos como calcular a chave pública a partir da chave privada. E, é claro, abordaremos o processo de assinatura digital.

Em seguida, voltaremos no tempo para ver a evolução das carteiras Bitcoin e nos aventuraremos nos conceitos de entropia e números aleatórios. Revisaremos a famosa frase mnemônica, enquanto abrimos um parêntese sobre a passphrase. Você até terá a oportunidade de vivenciar uma experiência única criando uma semente a partir de 128 lançamentos de dados!

Com essas bases sólidas, estaremos prontos para a parte crucial: a criação de uma carteira Bitcoin. Desde o nascimento da semente e da chave mestra, passando pelo estudo das chaves estendidas, até a derivação dos pares de chaves filhas, cada etapa será detalhada. Também discutiremos a estrutura da carteira e os caminhos de derivação.

Para coroar tudo isso, concluiremos nossa jornada examinando os endereços Bitcoin. Explicaremos como eles são criados e como desempenham um papel fundamental no funcionamento das carteiras Bitcoin.

Embarque comigo nesta jornada cativante e prepare-se para explorar o universo da criptografia como nunca antes. Deixe suas preconcepções do lado de fora e abra sua mente para uma nova maneira de entender o Bitcoin e sua estrutura fundamental.

# As funções de hash

## Introdução às funções de hash criptográfico relacionadas ao Bitcoin

![2.1 - les fonctions de hachage cryptographiques](https://youtu.be/dvnGArYvVr8)

Bem-vindo à nossa sessão de hoje dedicada a uma imersão profunda no mundo criptográfico das funções de hash, um elemento fundamental para a segurança do protocolo Bitcoin. Imagine uma função de hash como um robô decifrador criptográfico altamente eficiente que transforma informações de todos os tamanhos em uma impressão digital única e de tamanho fixo, chamada de "hash", "impressão" ou "resumo".

Resumidamente, uma função de hash recebe uma mensagem de tamanho arbitrário como entrada e a converte em uma impressão de tamanho fixo como saída.

Descrever o perfil das funções de hash criptográficas requer entender duas qualidades essenciais: sua irreversibilidade e sua resistência à falsificação.

A irreversibilidade, ou resistência à pré-imagem, significa que o cálculo da saída a partir da entrada pode ser feito facilmente, mas o cálculo da entrada a partir da saída é impossível. É uma função unidirecional.

![image](assets/image/section1/0.JPG)

A resistência à falsificação vem do fato de que qualquer modificação na entrada resultará em uma saída completamente diferente. Essas funções permitem verificar a integridade de softwares baixados.

![image](assets/image/section1/1.JPG)

Outra característica crucial que elas possuem é a resistência a colisões e à segunda pré-imagem. Uma colisão ocorre quando duas entradas distintas produzem a mesma saída. Certamente, no mundo das funções de hash, colisões são inevitáveis, mas uma excelente função de hash criptográfica as minimiza consideravelmente. O risco deve ser tão baixo que possa ser considerado nulo. É como se cada hash fosse uma casa em uma cidade imensa; apesar do grande número de casas, uma boa função de hash garante que cada casa tenha um endereço único.

A resistência à segunda pré-imagem depende da resistência a colisões; se houver resistência a colisões, então há resistência à segunda pré-imagem. Dada uma informação de entrada imposta, é necessário encontrar uma segunda entrada, diferente da primeira, que produza uma colisão no hash de saída da função. A resistência à segunda pré-imagem é semelhante à resistência a colisões, exceto pelo fato de que a entrada é imposta.
Vamos navegar pelas ondas tumultuosas das funções de hash obsoletas. SHA0, SHA1 e MD5 são agora consideradas como cascos enferrujados no oceano do hashing criptográfico. Muitas vezes não são recomendados porque perderam a sua resistência a colisões. O princípio da gaveta explica porque é que, apesar dos nossos melhores esforços, a prevenção de colisões é impossível devido ao tamanho limitado do output. Para ser considerada verdadeiramente segura, uma função hash deve ser resistente a colisões, a segunda pré-imagem e a pré-imagem.

Um elemento chave no protocolo Bitcoin, a função hash SHA-256 é o capitão do navio. Outras funções, como a SHA-512, são usadas para derivação com HMAC e PBKDF. Além disso, o RIPMD160 é utilizado para reduzir uma impressão digital a 160 bits. Quando falamos de HASH256 e HASH160, estamos a referir-nos à utilização de um hash duplo com SHA-256 e RIPMD.

Para o HASH256, estamos a falar de um hash duplo da mensagem utilizando a função SHA256.

$$
SHA256(SHA256(mensagem))
$$

Para HASH160, a mensagem é submetida a um hash duplo utilizando a função SHA256 e, em seguida, RIPMD160.

$$
RIPMD160(SHA256(mensagem))
$$

A utilização do HASH160 é particularmente vantajosa, pois permite-lhe beneficiar da segurança do SHA-256, reduzindo simultaneamente o tamanho da impressão digital.

Resumindo, o objetivo final de uma função hash criptográfica é transmutar informação de tamanho arbitrário numa impressão digital de tamanho fixo. Para ser reconhecida como segura, deve ter várias características: irreversibilidade, resistência à falsificação, resistência a colisões e resistência à segunda pré-imagem.

![image](assets/image/section1/2.JPG)

No final desta exploração, desmistificámos as funções hash criptográficas, destacámos as suas utilizações no protocolo Bitcoin e dissecámos os seus objectivos específicos. Aprendemos que, para serem consideradas seguras, as funções de hash devem ser resistentes a pré-imagem, segunda pré-imagem, colisão e falsificação. Também analisámos a gama de diferentes funções hash utilizadas no protocolo Bitcoin. Na nossa próxima sessão, vamos mergulhar no coração da função hash SHA256 e descobrir a matemática fascinante que lhe dá as suas características únicas.

## O funcionamento do SHA256

O funcionamento do SHA256](https://youtu.be/74SWg_ZbUj4)

Bem-vindo à continuação da nossa fascinante viagem pelos labirintos criptográficos da função hash. Hoje estamos a desvendar os mistérios do SHA256, um processo complexo mas engenhoso que introduzimos anteriormente.
Para lembrar, o objetivo da função de hash SHA256 é pegar uma mensagem de qualquer tamanho como entrada e gerar uma hash de 256 bits como saída.

### Pré-processamento

Vamos dar um passo adiante neste labirinto, começando pelo pré-processamento do SHA256.

#### Bits de preenchimento

O objetivo desta primeira etapa é ter uma mensagem alinhada em múltiplos de 512 bits. Para fazer isso, vamos adicionar bits de preenchimento à mensagem.

Seja M o tamanho da mensagem inicial.
Seja 1 um bit reservado para o separador.
Seja P o número de bits usados para o preenchimento e 64 o número de bits reservados para a segunda fase do pré-processamento.
O total deve ser um múltiplo de 512 bits, que é o que n representa.

![image](assets/image/section1/3.JPG)

Exemplo com uma mensagem de entrada de 950 bits:

```
Passo 1: Determinar o tamanho; o número final de bits ideal.
O primeiro múltiplo de 512 > (M + 64 + 1) (com M = 950) é 1024.
1024 = 2 * 512
Então n = 2.

Passo 2: Determinar P, o número de bits de preenchimento necessários para atingir o número final de bits ideal.
-> M + 1 + P + 64 = n * 512
-> M + 1 + P + 64 = 2 * 512
-> 940 + 1 + P + 64 = 1024
-> P = 1024 - 1 - 64 - 950
-> P = 9

Portanto, serão necessários 9 bits de preenchimento para ter uma mensagem alinhada em múltiplos de 512.
```

E agora?
Logo após a mensagem inicial, é necessário adicionar o separador 1 seguido de P, que no nosso exemplo é igual a nove 0.

```
mensagem + 1 000 000 000
```

#### Preenchimento do tamanho

Agora passamos para a segunda fase do pré-processamento, que envolve adicionar a representação binária do tamanho da mensagem inicial, em bits.

Vamos retomar o exemplo com uma entrada de 950 bits:

```
A representação binária do número 950 é: 11 1011 0110

Usamos nossos 64 bits reservados na etapa anterior. Adicionamos zeros para arredondar nossos 64 bits para a entrada alinhada. Em seguida, combinamos a mensagem inicial, o preenchimento dos bits e o preenchimento do tamanho para obter nossa entrada alinhada.
```

Aqui está o resultado:

![image](assets/image/section1/4.JPG)

### Processamento

#### Pré-requisitos de compreensão

##### As constantes e vetores de inicialização

À presente, estamos nos preparando para as primeiras etapas do processamento da função SHA-256. Como em qualquer boa receita, precisamos de alguns ingredientes básicos, que chamamos de constantes e vetores de inicialização.
Os vetores de inicialização, de A a H, são os primeiros 32 bits das partes decimais das raízes quadradas dos 8 primeiros números primos. Eles serão usados como valores básicos nas primeiras etapas do processamento. Seus valores estão no formato hexadecimal.

As constantes K, de 0 a 63, representam os primeiros 32 bits das partes decimais das raízes cúbicas dos 64 primeiros números primos. Elas são usadas a cada rodada da função de compressão. Seus valores também estão no formato hexadecimal.

![image](assets/image/section1/5.JPG)

##### As operações utilizadas

Dentro da função de compressão, usamos operadores específicos como XOR, AND e NOT. Tratamos os bits um por um de acordo com sua posição, usando o operador XOR e uma tabela de verdade. O operador AND é usado para retornar 1 apenas se ambos os operandos forem iguais a 1, e o operador NOT para retornar o valor oposto de um operando. Também usamos a operação SHR para deslocar os bits para a direita por um número escolhido.

A tabela de verdade:

![image](assets/image/section1/6.JPG)

As operações de deslocamento de bits:

![image](assets/image/section1/7.JPG)

#### A função de compressão

Antes de aplicar a função de compressão, dividimos a entrada em blocos de 512 bits. Cada bloco será processado independentemente dos outros.

Cada bloco de 512 bits é então dividido em pedaços W de 32 bits. Dessa forma, W(0) representa os primeiros 32 bits do bloco de 512 bits. W(1) representa os próximos 32 bits e assim por diante até chegar aos 512 bits do bloco.

Uma vez que todas as constantes K e os pedaços W são definidos, podemos processar os seguintes cálculos para cada pedaço W, em cada rodada.

Realizamos 64 rodadas de cálculo na função de compressão. Na última rodada, teremos no "Resultado da função" um estado intermediário que será adicionado ao estado inicial da função de compressão.

Em seguida, repetimos todas essas etapas da função de compressão no próximo bloco de 512 bits, até o último bloco.

Todas as adições na função de compressão são adições módulo 2^32 para sempre manter uma soma de 32 bits.

![image](assets/image/section1/9.JPG)

![image](assets/image/section1/8.JPG)

##### Uma rodada da função de compressão

![image](assets/image/section1/11.JPG)

![image](assets/image/section1/10.JPG)
O tour da função de compressão será realizado 64 vezes. Encontramos como entrada nossos pedaços W e nossas constantes K definidas anteriormente.
Os quadrados/cruzes vermelhas correspondem a uma adição módulo 2^32 bits.

As entradas A, B, C, D, E, F, G, H serão associadas a um valor de 32 bits para um total de 32 \* 8 = 256 bits.
Também encontramos como saída uma nova sequência A, B, C, D, E, F, G, H. Essa saída será então usada como entrada para a próxima rodada e assim por diante até o final da 64ª rodada.

Os valores da sequência de entrada da primeira rodada da função de compressão correspondem aos vetores de inicialização pré-definidos acima.
Como lembrete, os vetores de inicialização representam os 32 primeiros bits das partes decimais das raízes quadradas dos 8 primeiros números primos.

Aqui está um exemplo de uma rodada:

![image](assets/image/section1/12.1.png)

##### O estado intermediário

Como lembrete, a mensagem é dividida em blocos de 512 bits que são então divididos em pedaços de 32 bits. Para cada bloco de 512 bits, aplicamos as 64 rodadas da função de compressão.
O estado intermediário corresponde ao final das 64 rodadas de um bloco. Os valores da sequência de saída dessa 64ª rodada são usados como valores iniciais da sequência de entrada da primeira rodada do próximo bloco.

![image](assets/image/section1/12.2.png)

#### Visão geral da função de hash

![image](assets/image/section1/13.JPG)

Observaremos que a saída do primeiro pedaço de mensagem de 512 bits corresponde aos nossos vetores de inicialização como entrada para o segundo pedaço de mensagem, e assim por diante.

A saída da última rodada, do último pedaço, corresponde ao resultado final da função SHA256.

Para concluir, gostaríamos de destacar o papel crucial dos cálculos realizados nas caixas CH, MAJ, σ0 e σ1. Essas operações, entre outras, são os guardiões que garantem a robustez da função de hash SHA256 contra ataques, tornando-a uma escolha preferida para a segurança de muitos sistemas digitais, especialmente no protocolo Bitcoin. Portanto, é evidente que, embora complexa, a beleza do SHA256 reside em sua robustez em encontrar a entrada a partir do hash, enquanto a verificação do hash para uma entrada dada é uma ação mecanicamente simples.

## Os algoritmos usados para a derivação

![Os algoritmos usados para a derivação](https://youtu.be/ZF1_BMsOJXc)

Os algoritmos de derivação HMAC e PBKDF2 são componentes-chave na mecânica de segurança do protocolo Bitcoin. Eles previnem uma variedade de ataques potenciais e garantem a integridade das carteiras Bitcoin.
HMAC e PBKDF2 são ferramentas criptográficas usadas para diferentes tarefas no Bitcoin. HMAC é principalmente usado para combater ataques de extensão de comprimento durante a derivação de carteiras hierarquicamente determinísticas (HD), enquanto PBKDF2 é usado para converter uma frase mnemônica em uma semente.

#### HMAC-SHA512

O HMAC-SHA512 tem duas entradas: uma mensagem m (Entrada 1) e uma chave K escolhida arbitrariamente pelo usuário (Entrada 2).
Ele também tem uma saída de tamanho fixo: 512 bits

```
Observações:
- m: mensagem de tamanho arbitrário escolhida pelo usuário (entrada 1)
- K: chave arbitrária escolhida pelo usuário (entrada 2)
- K': a chave K ajustada. Ela foi ajustada para o tamanho B dos blocos.
- ||: operação de concatenação.
- opad: constante definida pelo byte 0x5c repetido B vezes.
- ipad: constante definida pelo byte 0x36 repetido B vezes.
- B: o tamanho dos blocos da função de hash utilizada.
```

![image](assets/image/section1/14.JPG)

O HMAC-SHA512, que recebe uma mensagem e uma chave como entradas, gera uma saída de tamanho fixo. Para garantir a uniformidade, a chave é ajustada de acordo com o tamanho dos blocos usados na função de hash. No contexto da derivação de carteiras HD, o HMAC-SHA-512 é usado. Este último funciona com blocos de 1024 bits (128 bytes) e ajusta a chave de acordo. Ele usa as constantes OPAD (0x5c) e IPAD (0x36), repetidas quantas vezes forem necessárias para reforçar a segurança.

O processo do HMAC-SHA-512 envolve a concatenação do resultado do SHA-512 aplicado à chave XOR OPAD e à chave XOR IPAD com a mensagem. Quando usado com blocos de 1024 bits (128 bytes), a chave de entrada é preenchida com zeros, se necessário, e depois XORada com IPAD e OPAD. A chave modificada é então concatenada com a mensagem.

![image](assets/image/section1/15.JPG)

O salt, ao integrar uma fonte adicional de entropia, aumenta a segurança das chaves derivadas. Sem ele, um ataque poderia comprometer toda a carteira e roubar todos os bitcoins.

#### PBKDF2

O PBKDF2 é usado para converter uma frase mnemônica em uma semente. Nesse caso, na entrada 1, podemos encontrar a frase mnemônica e, na entrada 2, a frase de acesso.
Este algoritmo realiza 2048 iterações usando HMAC SHA512. Graças a esses algoritmos de derivação, duas entradas diferentes podem produzir uma saída única e fixa, o que resolve o problema de possíveis ataques de extensão de comprimento nas funções da família SHA-2. Um ataque de extensão de comprimento explora uma propriedade específica de algumas funções de hash criptográficas. Nesse tipo de ataque, um invasor que já possui o hash de uma mensagem desconhecida pode usá-lo para calcular o hash de uma mensagem mais longa, que é uma extensão da mensagem original. Isso muitas vezes é possível sem conhecer o conteúdo da mensagem original, o que pode levar a falhas de segurança significativas se esse tipo de função de hash for usado para tarefas como verificação de integridade.

![image](assets/image/section1/16.JPG)

Em conclusão, os algoritmos HMAC e PBKDF2 desempenham papéis essenciais na segurança da derivação de carteiras HD no protocolo Bitcoin. O HMAC-SHA-512 é usado para se proteger contra ataques de extensão de comprimento, enquanto o PBKDF2 permite a conversão da frase mnemônica em uma semente. O código de cadeia adiciona uma fonte adicional de entropia na derivação das chaves, garantindo assim a robustez do sistema.

# Assinaturas digitais

## Assinaturas digitais e curvas elípticas

![Assinaturas digitais e curvas elípticas](https://youtu.be/gOjYiPkx4z8)

Onde esses famosos bitcoins são armazenados? Não em uma carteira Bitcoin, como se poderia pensar. Na realidade, uma carteira Bitcoin armazena as chaves privadas necessárias para provar a posse dos bitcoins. Os próprios bitcoins são registrados na blockchain, um banco de dados descentralizado que arquiva todas as transações.

No sistema Bitcoin, a unidade de conta é o bitcoin (observe o "b" minúsculo). Ele é divisível em até oito casas decimais, sendo a menor unidade o satoshi. As UTXOs, ou "Unspent Transaction Outputs", representam as saídas de transações não gastas pertencentes a uma chave pública que está matematicamente ligada a uma chave privada. Para gastar esses bitcoins, é necessário atender à condição de gasto da transação. Uma condição de gasto típica consiste em provar para o restante da rede que o usuário é o proprietário legítimo da chave pública associada às UTXOs. Para fazer isso, ele terá que demonstrar que está em posse da chave privada correspondente à chave pública vinculada a cada UTXO, sem revelar a chave privada.
C'est o que permite a assinatura digital. Ela serve como prova matemática demonstrando a posse de uma chave privada associada a uma chave pública específica. Essa técnica de proteção de dados é essencialmente baseada em um fascinante campo da criptografia chamado criptografia de curva elíptica (ECC).
A assinatura pode ser verificada matematicamente pelas outras partes envolvidas na rede Bitcoin.

![image](assets/image/section2/0.JPG)

Para garantir a segurança das transações, o Bitcoin utiliza dois protocolos de assinatura digital: ECDSA (Elliptic Curve Digital Signature Algorithm) e Schnorr. O ECDSA é um protocolo de assinatura incorporado ao Bitcoin desde o seu lançamento em 2009, enquanto as assinaturas de Schnorr foram adicionadas mais recentemente, em novembro de 2021. Embora esses dois protocolos se baseiem na criptografia de curva elíptica e usem mecanismos matemáticos semelhantes, eles diferem principalmente em termos de estrutura de assinatura.

Neste curso, apresentaremos o algoritmo ECDSA.

### O que é uma curva elíptica?

A criptografia de curva elíptica é um conjunto de algoritmos que utilizam uma curva elíptica por suas diferentes propriedades geométricas e matemáticas com o objetivo de criptografia, e sua segurança é baseada na dificuldade de cálculo do logaritmo discreto.

As curvas elípticas são úteis em uma variedade de aplicações criptográficas no protocolo Bitcoin, desde trocas de chaves até criptografia assimétrica e assinaturas digitais.

As curvas elípticas possuem propriedades interessantes:

- Simetria: Qualquer linha não vertical que intersecta dois pontos na curva elíptica, também intersectará a curva em um terceiro ponto.
- Qualquer linha não vertical tangente à curva em um ponto, sempre intersectará a curva em um segundo ponto único.

O protocolo Bitcoin utiliza uma curva elíptica específica chamada Secp256k1 para realizar suas operações criptográficas.

Antes de mergulharmos mais profundamente nesses mecanismos de assinatura, é importante entender o que é uma curva elíptica. Uma curva elíptica é definida pela equação y² = x³ + ax + b. Qualquer ponto nesta curva possui uma simetria distintiva que é a chave para sua utilidade em criptografia.

![image](assets/image/section2/1.JPG)

No final das contas, várias curvas elípticas são reconhecidas como seguras para uso criptográfico. A mais conhecida talvez seja a curva secp256r1. No entanto, para o Bitcoin, Satoshi Nakamoto optou por outra curva: a secp256k1.

Essa curva é definida pelos parâmetros a=0 e b=7, e sua equação é y² = x³ + 7 modulo n, onde n representa o número primo que determina a ordem da curva.

![image](assets/image/section2/2.JPG)
A primeira imagem representa a curva secp256k1 no corpo dos números reais e sua equação. A segunda imagem é uma representação da curva secp256k1 no corpo ZP, o corpo dos números inteiros naturais e positivos, módulo p onde p é um número primo. Isso se assemelha a uma nuvem de pontos. Usamos esse corpo dos números inteiros naturais e positivos para evitar aproximações.
p é um número primo, é a ordem da curva que é usada.
Finalmente, a equação usada no protocolo Bitcoin é:

$$
y^2 = (x^3 + 7) mod(p)
$$

A equação da curva elíptica no bitcoin corresponde à última equação na imagem anterior.

Na próxima seção deste curso, usaremos curvas que estão no corpo dos números reais apenas para facilitar a compreensão.

### Calcular a chave pública a partir da chave privada

![Calcular a chave pública a partir da chave privada](https://youtu.be/NJENwFU889Y)

Para começar, vamos mergulhar no universo do algoritmo Elliptic Curve Digital Signature Algorithm (ECDSA). O Bitcoin utiliza esse algoritmo de assinatura digital para vincular as chaves privadas e públicas. Nesse sistema, a chave privada é um número aleatório ou pseudo-aleatório de 256 bits. O número total de possibilidades para uma chave privada é teoricamente 2^256, mas na realidade é ligeiramente inferior a isso. Para ser preciso, algumas chaves privadas de 256 bits não são válidas para o Bitcoin.

Para ser compatível com o Bitcoin, uma chave privada deve estar entre 1 e n-1, onde n representa a ordem da curva elíptica. Isso significa que o número total de possibilidades para uma chave privada do Bitcoin é quase igual a 1,158 x 10^77. Para colocar isso em perspectiva, é aproximadamente o mesmo número de átomos presentes no universo observável.

![imagem](assets/image/section2/3.JPG)

A chave privada única, denotada por k, é então usada para determinar uma chave pública.

A chave pública, denotada por K, é um ponto na curva elíptica que é derivado da chave privada usando algoritmos irreversíveis como o ECDSA. Quando temos conhecimento da chave privada, é muito fácil encontrar a chave pública, mas quando possuímos apenas a chave pública, é impossível encontrar a chave privada. Essa irreversibilidade é a pedra angular da segurança da carteira Bitcoin.

A chave pública tem 512 bits, pois corresponde a um ponto na curva com uma coordenada x de 256 bits e uma coordenada y de 256 bits. No entanto, ela pode ser comprimida em um número de 264 bits.

![imagem](assets/image/section2/4.JPG)
O ponto gerador (G) é o ponto na curva a partir do qual todas as chaves públicas são geradas no protocolo Bitcoin. Ele tem coordenadas x e y específicas, geralmente representadas em hexadecimal. Para secp256k1, as coordenadas G são, em hexadecimal:

- `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
- `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

Este ponto é útil para derivar todas as chaves públicas. Para calcular a chave pública K, basta multiplicar o ponto G pela chave privada k, como: K = k.G

Agora vamos estudar como adicionar e multiplicar pontos em curvas elípticas.

#### Adição e duplicação de pontos em curvas elípticas

##### Adicionar dois pontos M + L

Uma das propriedades notáveis das curvas elípticas é que uma reta não vertical que intersecta a curva em dois pontos também intersectará em um terceiro ponto, chamado ponto O em nosso exemplo. Essa propriedade é usada para determinar o ponto U, que é o oposto do ponto O.

M + L = U

![image](assets/image/section2/5.JPG)

##### Adicionar um ponto a si mesmo = Duplicação de ponto

A adição de um ponto G a si mesmo é feita traçando uma tangente à curva no ponto. Essa tangente, de acordo com as propriedades das curvas elípticas, sempre intersectará a curva em um segundo ponto único -J. O oposto desse ponto, J, é o resultado da adição do ponto G a si mesmo.
G + G = J

Aliás, o ponto G é o ponto de partida para calcular todas as chaves públicas dos usuários do sistema Bitcoin.

![image](assets/image/section2/6.JPG)

#### Produto escalar em curvas elípticas

O produto escalar de um ponto por n é equivalente a adicionar esse ponto a si mesmo n vezes.

Da mesma forma que na duplicação de ponto, o produto escalar do ponto G por um ponto n é feito traçando uma tangente à curva no ponto G. Essa tangente, de acordo com as propriedades das curvas elípticas, sempre intersectará a curva em um segundo ponto único -2G. O oposto desse ponto, 2G, é o resultado da adição do ponto G a si mesmo.

Se n = 4, então repetimos a operação até chegarmos a 4G.

![image](assets/image/section2/7.JPG)

Aqui está um exemplo de cálculo para 3G:

![image](assets/image/section2/8.JPG)
Essas operações nos pontos de uma curva elíptica são a base para o cálculo das chaves públicas. A derivação de uma chave pública a partir da chave privada é muito fácil. Uma chave pública é um ponto na curva elíptica, é o resultado da nossa adição e duplicação do ponto G k vezes. Com k = chave privada.

Neste exemplo:

- A chave privada k = 4
- A chave pública K = kG = 4G

![image](assets/image/section2/9.JPG)

Conhecendo a chave privada k, é fácil calcular a chave pública K. No entanto, é impossível recuperar a chave privada a partir da chave pública. Isso é resultado de uma adição ou duplicação de ponto?

No nosso próximo curso, exploraremos como uma assinatura digital é realizada usando o algoritmo ECDSA com uma chave privada para gastar bitcoins.

## Assinar com a chave privada

![Assinar com a chave privada](https://youtu.be/h2hIyGgPqkM)

O processo de assinatura digital é um método chave para provar que você é o detentor de uma chave privada sem precisar revelá-la. Isso é feito usando o algoritmo ECDSA, que envolve a determinação de um nonce único, o cálculo de um número específico, V, e a criação de uma assinatura digital composta por duas partes, S1 e S2.
É crucial sempre usar um nonce único para evitar ataques de segurança. Um exemplo notório do que pode acontecer quando essa regra não é seguida é o caso do hackeamento do PlayStation 3, que foi comprometido devido à reutilização do nonce.

![](assets/image/section2/10.JPG)

Passos:

- Determinar um nonce v, ou seja, um número único aleatório.
  Nonce = Number Only Use Once.
  É determinado pela pessoa que realiza a assinatura.
- Calcular por adição e duplicação de ponto na curva elíptica a partir do ponto G, a posição de V na curva elíptica.
  Como V = v.G
  x e y são as coordenadas de V no plano.
- Calcular S1.
  S1 = x mod n, onde n é a ordem da curva e x é uma coordenada de V no plano.
  Observação: O número de possibilidades da chave pública é maior do que o número de pontos na curva elíptica no corpo finito dos inteiros positivos que é usado no Bitcoin.
  A ordem da curva corresponde apenas às possibilidades que a chave pública pode assumir na curva.
- Calcular S2.
  H(Tx) = Hash da transação
  k = a chave privada
- Calcular a assinatura: a concatenação de S1 + S2.
- Calcular P, o cálculo de verificação da assinatura.
  K = a chave pública
  Por exemplo, para obter a chave pública 3G, você desenha uma tangente no ponto G, calcula o oposto de -G para obter 2G e, em seguida, adiciona G e 2G. Para realizar uma transação, você precisa provar que conhece o número 3 desbloqueando os bitcoins associados à chave pública 3G.

Para criar uma assinatura digital e provar que você conhece a chave privada associada à chave pública 3G, você primeiro calcula um nonce e, em seguida, o ponto V associado a esse nonce (no exemplo dado, é 4G). Em seguida, você calcula o ponto T adicionando a chave pública 3G e o ponto V, o que resulta em 7G.

![image](assets/image/section2/11.JPG)

Vamos simplificar o processo de assinatura digital.
Na imagem anterior, a chave privada k = 3.
Podemos facilmente calcular a chave pública K associada a essa chave privada: K = 3G.
Em seguida, geramos pseudo-aleatoriamente um nonce: v = 4.
A partir desse nonce, é possível calcular V como: V = v.G = 4G.

A partir desse ponto V, calculamos o ponto T como:
T = t.G = 7G (com t = 7)

É hora de realizar a verificação da assinatura digital.

A verificação de uma assinatura digital é uma etapa crucial no uso do algoritmo ECDSA, que permite confirmar a autenticidade de uma mensagem assinada sem precisar da chave privada do remetente. Veja como isso acontece em detalhes:

Em nosso exemplo, temos dois valores importantes: t e V.
t é um valor numérico (7 neste exemplo) e V é um ponto na curva elíptica (representado por 4G aqui). Esses valores são gerados durante a criação da assinatura digital e são enviados junto com a mensagem para permitir a verificação.

Quando o verificador recebe a mensagem, ele também recebe esses dois valores, t e V.

Aqui estão as etapas que o verificador seguirá para validar a assinatura:

1. Ele primeiro calculará o hash da mensagem, que chamaremos de H.
2. Em seguida, ele calculará u1 e u2. Para fazer isso, ele usará as seguintes fórmulas:
   - u1 = H /\* (S2)^-1 mod n
   - u2 = T /\* (S2)^-1 mod n
     Onde S2 é a segunda parte da assinatura digital, n é a ordem da curva elíptica e (S2)^-1 é o inverso de S2 mod n.
3. O verificador então calculará um ponto P' na curva elíptica usando a fórmula: P' = u1 _ G + u2 _ K
   - G é o ponto de geração da curva
   - K é a chave pública do remetente'
4. O verificador então calculará I', que é simplesmente a coordenada x do ponto P' módulo n. 5. Por fim, o verificador confirmará que I' é igual a t. Se for o caso, a assinatura é considerada válida. Se não for o caso, a assinatura é inválida.

Esta procedimento garante que apenas o remetente que possui a chave privada correspondente poderia ter produzido uma assinatura que passa por esse processo de verificação.

![image](assets/image/section2/12.JPG)

Simplificando:
Aquele que produz a assinatura fornecerá ao verificador o número t (no nosso exemplo, t = 7) e o ponto V.

É impossível determinar a chave pública ou a chave privada a partir do número 7 e do número V.

As etapas de verificação da assinatura digital são as seguintes:

- Na curva, ele adiciona o ponto da chave pública ao ponto V para encontrar o ponto T'.
- Ele calcula o número t.G
- Ele verifica se o resultado de t.G é igual ao número T'

Em conclusão, a verificação de uma assinatura digital é um procedimento essencial nas transações de Bitcoin. Isso garante que a mensagem assinada não foi alterada durante a transmissão e que o remetente é o detentor da chave privada. Essa técnica de autenticação digital é baseada em princípios matemáticos complexos, incluindo a aritmética de curva elíptica, enquanto mantém a confidencialidade da chave privada. Ela oferece uma base sólida de segurança para transações criptográficas.

Dito isso, a gestão dessas chaves, bem como sua criação, é outra questão essencial no Bitcoin. Como gerar um novo par de chaves? Como organizar várias chaves de forma segura e eficiente? Como recuperá-las, se necessário?

Para responder a essas perguntas e aprofundar sua compreensão da segurança da criptografia, nosso próximo curso se concentrará no conceito de Carteira Hierárquica Determinística (HD wallets) e no uso de frases mnemônicas. Esses mecanismos oferecem maneiras elegantes de gerenciar eficientemente suas chaves de criptomoeda, ao mesmo tempo em que fortalecem a segurança.

# A frase mnemônica

## Evolução das carteiras Bitcoin

![Evolução das carteiras Bitcoin](https://youtu.be/6tmu1R9cXyk)

A Carteira Hierárquica Determinística, ou mais comumente chamada de carteira HD, desempenha um papel importante no ecossistema das criptomoedas. O termo "carteira" pode parecer enganador para aqueles que são novatos nesse campo, pois não implica a posse de dinheiro ou moedas. Em vez disso, refere-se a uma coleção de chaves criptográficas privadas.
Os primeiros wallets eram softwares que agrupavam chaves privadas determinadas de forma pseudoaleatória, mas que não tinham nenhuma ligação entre si. Esses wallets são chamados de "Just a Bunch Of Keys" (JBOK).

As chaves não tendo nenhuma ligação entre si, o usuário é obrigado a fazer um novo backup para cada novo par de chaves gerado. Ou o usuário usa o mesmo par de chaves o tempo todo e perde em confidencialidade, ou ele gera um novo par de chaves de forma aleatória e, portanto, precisa fazer um novo backup dessas chaves.

![image](assets/image/section3/0.JPG)

No entanto, a complexidade da gestão dessas chaves é compensada por um conjunto de protocolos chamados de Bitcoin Improvement Proposals (BIP). Essas propostas de atualização estão no cerne da funcionalidade e segurança das wallets HD. Por exemplo, o [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), lançado em 2012, revolucionou a forma como essas chaves são geradas e armazenadas, introduzindo o conceito de chaves derivadas de forma determinística e hierárquica. A ideia é derivar todas as chaves de forma determinística e hierárquica a partir de uma única informação: a seed. Assim, o processo de backup dessas chaves é muito simplificado, mantendo seu nível de segurança.

![image](assets/image/section3/1.JPG)

Em seguida, o [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) introduziu uma inovação marcante: a frase mnemônica de 24 palavras. Esse sistema transformou uma sequência complexa de números difícil de lembrar em uma série de palavras comuns, muito mais fácil de memorizar e armazenar. Além disso, o [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) propôs adicionar uma passphrase adicional para reforçar a segurança das chaves individuais. Essas melhorias sucessivas levaram às normas BIP43 e BIP44, que padronizaram a estrutura e hierarquia das wallets HD, tornando essas wallets mais acessíveis e fáceis de usar para o público em geral.

Nas seções seguintes, vamos mergulhar mais profundamente no funcionamento das wallets HD. Vamos abordar os princípios de derivação de chaves e examinar os conceitos fundamentais de entropia e geração de números aleatórios, que são essenciais para garantir a segurança da sua wallet HD.
Em forma de síntese, é essencial destacar o papel central do BIP32 e BIP39 no design e segurança das carteiras HD. Esses protocolos permitem gerar uma infinidade de chaves a partir de uma única semente, que deve ser um número aleatório ou pseudo-aleatório. Hoje em dia, essas normas são adotadas pela maioria das carteiras de criptomoedas, sejam elas dedicadas a uma única criptomoeda ou que suportem vários tipos de moedas.

## Entropia e número aleatório

![Entropia e número aleatório](https://youtu.be/k18yH18w2TE)

A importância da segurança das chaves privadas no ecossistema do Bitcoin é incontestável. Elas são, de fato, a pedra angular que garante a segurança das transações Bitcoin. Para evitar qualquer vulnerabilidade associada à previsibilidade, essas chaves devem ser geradas de forma verdadeiramente aleatória, o que pode rapidamente se tornar um exercício trabalhoso. O problema é que, na computação, é impossível gerar um número verdadeiramente aleatório, pois ele é necessariamente derivado de um processo determinístico; um código.
Portanto, é essencial se informar sobre os diferentes Geradores de Números Aleatórios (RNG). Os tipos de RNG variam, desde Geradores de Números Pseudo-Aleatórios (PRNG) até Geradores de Números Verdadeiramente Aleatórios (TRNG), bem como PRNGs que incorporam uma fonte de entropia.

Entropia refere-se ao estado de "desordem" de um sistema. A partir de uma entropia externa, ou seja, uma fonte de informação externa, é possível usar um gerador de números aleatórios para obter um número aleatório.

![image](assets/image/section3/2.JPG)

Vamos ver juntos como funciona um Gerador de Números Pseudo-Aleatórios (PRNG).

Ele recebe uma semente como entrada, ou seja, uma informação que corresponde ao estado interno 0.
Nesse estado interno, é aplicada uma função de transformação e o resultado, que é um número pseudo-aleatório, corresponde ao estado interno 1.
Nesse estado interno 1, novamente, é aplicada uma função de transformação que resulta em um novo número aleatório = estado interno 2.
E assim por diante.

A principal desvantagem é que qualquer semente idêntica sempre produzirá o mesmo resultado de saída. E também, se conhecermos o resultado das funções de transformação iniciais, seremos capazes de recuperar o número aleatório produzido pelo processo.

Um exemplo de função de transformação é a função PBKDF2.

**Em resumo, um PRNG criptograficamente seguro deve:**

- ser estatisticamente aleatório
- ser imprevisível
- ser resistente mesmo se os resultados forem revelados
- ter um período suficientemente longo

![image](assets/image/section3/3.JPG)
No caso do Bitcoin, as chaves privadas são geradas a partir de uma única informação na base da carteira. Essa informação permite uma derivação determinística e hierárquica dos pares de chaves filhas. A entropia é a base de toda carteira HD, embora não exista um padrão para a geração desse número aleatório. Portanto, a geração de números aleatórios é uma questão importante para garantir a segurança das transações Bitcoin.
![image](assets/image/section3/4.JPG)

A fase de verificação da geração das chaves é crucial para garantir a segurança e autenticidade da geração de números aleatórios, um passo fundamental para prevenir qualquer vulnerabilidade associada à previsibilidade. Portanto, é altamente recomendável usar carteiras de código aberto para permitir essa verificação.

No entanto, é importante observar que algumas carteiras de hardware podem ser "closed source", tornando impossível verificar a geração do número aleatório. Uma possível solução seria gerar sua própria frase mnemônica usando dados, embora essa abordagem possa apresentar alguns riscos.

O uso de uma frase de acesso gerada aleatoriamente pode ajudar a mitigar esses riscos.

Em última análise, o aleatório desempenha um papel central na criptografia e na computação, e a capacidade de gerar aleatoriedade de forma segura é crucial para garantir a segurança das chaves privadas e das transações Bitcoin. A entropia, que está no cerne da carteira HD do Bitcoin, é essencial para sua segurança. Em nossa próxima lição, continuaremos explorando esse assunto, abordando mais detalhadamente como a entropia contribui para a segurança das carteiras HD.

## A frase mnemônica

![A frase mnemônica](https://youtu.be/uJERqH9Xp7I)

A segurança de uma carteira Bitcoin é uma preocupação importante para todos os seus usuários. Uma maneira essencial de garantir a segurança da carteira é gerar uma frase mnemônica com base na entropia e na checksum.

![image](assets/image/section3/5.JPG)

Para converter a entropia em uma frase mnemônica, basta calcular a checksum da entropia e concatenar a entropia e a checksum.

Depois que a entropia é gerada, usamos a função SHA256 na entropia para criar um hash.
Recuperamos os 8 primeiros bits do hash, que é a checksum.
A frase mnemônica é o resultado da entropia adicionada à checksum.

A checksum garante a verificação da precisão da frase de recuperação. Sem essa checksum, um erro na frase pode resultar na criação de uma carteira diferente e, portanto, na perda dos fundos. Obtemos a checksum passando a entropia pela função SHA256 e recuperando os 8 primeiros bits do hash.

![image](assets/image/section3/6.JPG)

Existem diferentes padrões para a frase mnemônica, dependendo do tamanho da entropia. O padrão mais comumente usado para uma frase de recuperação de 24 palavras é uma entropia de 256 bits. O tamanho do checksum é determinado dividindo o tamanho da entropia por 32.

Por exemplo, uma entropia de 256 bits gera um checksum de 8 bits. A concatenação da entropia e do checksum resulta em tamanhos respectivos de 128 bits, 160 bits, etc. Dependendo do tamanho da entropia, a frase de recuperação terá 12 palavras para 128 bits, 15 palavras para 160 bits e 24 palavras para 256 bits.

**Codificação da frase mnemônica:**

![image](assets/image/section3/7.JPG)

Os últimos 8 bits correspondem ao checksum.
Cada segmento de 11 bits é convertido em decimal.
Cada decimal corresponde a uma palavra de uma lista de 2048 palavras no BIP39. É importante ressaltar que nenhuma palavra contém as quatro primeiras letras na mesma ordem.

É essencial salvar a frase de recuperação de 24 palavras para preservar a integridade da carteira Bitcoin. Os dois padrões mais comumente usados são baseados em uma entropia de 128 ou 256 bits e uma concatenação de 12 ou 24 palavras. Adicionar uma passphrase é uma opção adicional para reforçar a segurança da carteira.

Em conclusão, a geração de uma frase mnemônica para proteger uma carteira Bitcoin é um processo crucial. É importante seguir os padrões da frase mnemônica de acordo com o tamanho da entropia. Salvar a frase de recuperação de 24 palavras é essencial para evitar perda de fundos.

## A passphrase

![A passphrase](https://youtu.be/dZkOYO7MXwc)

A passphrase é uma senha adicional que pode ser adicionada a uma carteira Bitcoin para aumentar sua segurança. Seu uso é opcional e fica a critério do usuário. Ao adicionar informações arbitrárias que, juntamente com a frase mnemônica, permitem calcular a semente da carteira, a passphrase fortalece sua segurança.

![image](assets/image/section3/8.JPG)

A passphrase é um sal criptográfico opcional de tamanho escolhido pelo usuário. Ela melhora a segurança de uma carteira HD adicionando uma informação arbitrária que, quando agregada à frase mnemônica, permitirá calcular a semente.
Uma vez estabelecido quando um portefólio é criado, é necessário para a derivação de todas as chaves no portefólio. A função pbkdf2 é utilizada para gerar a semente a partir da frase-chave. Esta semente é utilizada para derivar todos os pares de chaves filho do portefólio. Se a frase-passe for modificada, a carteira Bitcoin torna-se completamente diferente.

A frase-passe é uma ferramenta essencial para reforçar a segurança das carteiras Bitcoin. Ela pode ser usada para aplicar várias estratégias de segurança. Por exemplo, ela pode ser usada para criar duplicatas e facilitar backups de senhas. Também pode melhorar a segurança da carteira, mitigando os riscos associados à geração aleatória da frase secreta.

Uma frase-chave eficaz deve ser longa (20 a 40 caracteres) e diversificada (utilizando letras maiúsculas e minúsculas, números e símbolos). Não deve estar diretamente relacionada com o utilizador ou o seu ambiente. É mais seguro utilizar uma sequência aleatória de caracteres em vez de uma palavra simples como a frase-chave.

![image](assets/image/section3/9.JPG)

Uma frase-chave é mais segura do que uma simples palavra-passe. A frase-chave ideal é longa, variada e aleatória. Pode reforçar a segurança de uma carteira ou de um software quente. Também pode ser utilizada para criar cópias de segurança redundantes e seguras.

É crucial cuidar dos backups de passphrase para evitar perder o acesso à carteira. Uma frase-chave é uma opção para uma carteira HD. Ela pode ser gerada aleatoriamente usando dados ou outro gerador de números pseudo-aleatórios.

# Criando uma carteira Bitcoin

## Criação da seed e da chave mestra

![Criando a seed e a master key](https://youtu.be/56yAt_JDWhY)

Nesta parte do curso, vamos explorar os passos envolvidos na derivação de uma HD (Hierarchical Deterministic Wallet), que permite que as chaves privadas e públicas sejam criadas e geridas de forma hierárquica e determinística.

![image](assets/image/section4/0.JPG)

A base da carteira HD assenta em dois elementos essenciais: a frase mnemónica e a frase-chave (palavra-passe adicional opcional). Juntos formam a seed, uma sequência alfanumérica de 512 bits que serve de base para derivar as chaves da carteira. A partir dessa semente, é possível derivar todos os pares de chaves filhos da carteira Bitcoin. A seed é a chave para aceder a todos os bitcoins associados à carteira, quer se utilize uma frase-chave ou não.

![image](assets/image/section4/1.JPG)
Para obter a seed, utilizamos a função pbkdf2 (Password-Based Key Derivation Function 2) com a frase mnemônica e a passphrase. A saída do pbkdf2 é uma seed de 512 bits.
A partir da seed, é possível determinar a chave privada mestre e o código de cadeia usando o algoritmo HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512). Esse algoritmo requer uma mensagem e uma chave como entrada para gerar um resultado. A chave privada mestre é calculada a partir da seed e da frase "Bitcoin SEED". Essa frase é a mesma para todas as derivações de todas as carteiras HD, garantindo assim consistência entre as carteiras.

Inicialmente, a função SHA-512 não estava implementada no protocolo Bitcoin, por isso usamos o HMAC SHA-512. O uso do HMAC SHA-512 com a frase "Bitcoin SEED" obriga o usuário a gerar uma carteira específica para o Bitcoin. O resultado do HMAC SHA-512 é um número de 512 bits, dividido em duas partes: os 256 bits da esquerda representam a chave privada mestre, enquanto os 256 bits da direita representam o código de cadeia mestre.

![image](assets/image/section4/2.JPG)

A chave privada mestre é a chave pai de todas as futuras chaves da carteira, enquanto o código de cadeia mestre é usado na derivação das chaves filhas. É importante observar que é impossível derivar um par de chaves filhas sem conhecer o código de cadeia correspondente do par pai.

Um par de chaves na carteira inclui uma chave privada, uma chave pública e um código de cadeia. O código de cadeia introduz uma fonte de aleatoriedade na derivação das chaves filhas e isola cada par de chaves para evitar vazamento de informações.

É importante ressaltar que a chave privada mestre é a primeira chave privada derivada da seed e não tem nenhuma relação com as chaves estendidas da carteira.

No próximo curso, exploraremos em detalhes as chaves estendidas, como xPub, xPRV, zPub, e entenderemos por que elas são usadas e como são construídas.

## As chaves estendidas

![As chaves estendidas](https://youtu.be/TRz760E_zUY)

Nesta parte do curso, estudaremos as chaves estendidas (xPub, zPub, yPub) e seus prefixos, que desempenham um papel importante na derivação das chaves filhas em uma carteira HD (Hierarchical Deterministic Wallet).

![image](assets/image/section4/3.JPG)
As chaves estendidas são diferentes das chaves mestras. Uma carteira HD gera uma frase mnemônica e uma semente para obter a chave mestra e o código de cadeia mestre. As chaves estendidas são usadas para derivar chaves filhas e requerem tanto a chave pai quanto o código de cadeia correspondente. Uma chave estendida combina essas duas informações para simplificar o processo de derivação.
![image](assets/image/section4/4.JPG)

As chaves públicas estendidas só podem derivar chaves públicas filhas normais, enquanto as chaves privadas estendidas permitem derivar chaves públicas e privadas filhas, seja em uma derivação normal ou endurecida.
A derivação endurecida é a derivação a partir da chave pai privada. A derivação normal corresponde à derivação a partir da chave pai pública.

O uso de chaves estendidas com o prefixo XPUB permite derivar novos endereços sem voltar às chaves privadas correspondentes, oferecendo assim uma melhor segurança. Os metadados associados às chaves estendidas fornecem informações importantes sobre seu papel e posição na hierarquia das chaves.

As chaves estendidas são identificadas por prefixos específicos (XPRV, XPUB, YPUB, ZPUB) que indicam se é uma chave estendida privada ou pública, bem como seu objetivo específico. Os metadados associados a uma chave estendida incluem a versão (prefixo), a profundidade, a impressão digital da chave pública, o índice e a carga útil (código de cadeia e chave pai).

![image](assets/image/section4/5.JPG)

A versão corresponde ao tipo de chave: xpub, xprv, ...

A profundidade corresponde ao número de derivações entre pai e filho que ocorreram desde a chave mestra.

A impressão digital do pai são os 4 primeiros bytes do hash 160 da chave pai.

O índice é o número do par que é usado para gerar a chave estendida entre suas irmãs. (irmãs = chaves da mesma profundidade)
exemplo: se quisermos derivar o xpub de nossa terceira conta, seu índice será 2 (porque o índice começa em 0).

A carga útil é composta pelo código de cadeia (32 bytes) e pela chave pai (33 bytes).

As chaves públicas comprimidas têm um tamanho de 33 bytes, enquanto as chaves públicas não comprimidas têm 512 bits. As chaves públicas comprimidas mantêm as mesmas informações que as chaves não comprimidas, mas com um tamanho reduzido. As chaves estendidas têm um tamanho de 82 bytes e seu prefixo é representado em base 58 através de uma conversão hexadecimal. O checksum é calculado usando a função de hash HASH256.

![image](assets/image/section4/6.JPG)
As derivações reforçadas começam a partir dos índices que são potências de 2 (2^31). É interessante notar que os prefixos mais comumente usados são xpub e zpub, que correspondem respectivamente aos padrões legacy e segwit v1 e segwit v0.
No nosso próximo curso, vamos nos aprofundar na derivação de pares de chaves filhas usando o conhecimento adquirido sobre chaves estendidas e a chave mestra da carteira.

## Derivação de pares de chaves filhas

![Derivação de pares de chaves filhas](https://youtu.be/FXhI-GmE9Aw)

Como lembrete, abordamos o cálculo da semente e da chave mestra, que são os primeiros elementos essenciais para a hierarquização e derivação da carteira HD (Hierarchical Deterministic Wallet). A semente, com um comprimento de 128 a 256 bits, é gerada aleatoriamente ou a partir de uma frase secreta. Ela desempenha um papel determinístico na derivação de todas as outras chaves. A chave mestra é a primeira chave derivada da semente e permite a derivação de todos os outros pares de chaves filhas.

O código da cadeia mestra desempenha um papel importante na recuperação da carteira a partir da semente. É importante observar que todas as chaves derivadas da mesma semente terão o mesmo código da cadeia mestra.

![imagem](assets/image/section4/7.JPG)

A hierarquização e derivação da carteira HD oferecem uma gestão mais eficiente das chaves e estruturas da carteira. As chaves estendidas permitem a derivação de um par de chaves filhas a partir de um par pai usando cálculos matemáticos e algoritmos específicos.

Existem diferentes tipos de pares de chaves filhas, incluindo chaves reforçadas e chaves normais. A chave pública estendida permite apenas a derivação de chaves públicas filhas normais, enquanto a chave privada estendida permite a derivação de todas as chaves filhas, tanto públicas quanto privadas, seja no modo normal ou reforçado. Cada par de chaves possui um índice que permite diferenciá-las umas das outras.

![imagem](assets/image/section4/8.JPG)

A derivação das chaves filhas usa a função HMAC-SHA512 usando a chave pai concatenada com o índice e o código da cadeia associado ao par de chaves. As chaves filhas normais têm um índice entre 0 e 2 elevado à potência 31 menos 1, enquanto as chaves filhas reforçadas têm um índice entre 2 elevado à potência 31 e 2 elevado à potência 32 menos 1.

![imagem](assets/image/section4/9.JPG)

![imagem](assets/image/section4/10.JPG)
Existem dois tipos de pares de chaves filhas: pares reforçados e pares normais. O processo de derivação das chaves filhas utiliza as chaves públicas para gerar as condições de gasto, enquanto as chaves privadas são utilizadas para a assinatura. A chave pública estendida permite apenas a derivação de chaves públicas filhas normais, enquanto a chave privada estendida permite a derivação de todas as chaves filhas, tanto públicas quanto privadas, em modo normal ou reforçado.
![image](assets/image/section4/11.JPG)
![image](assets/image/section4/12.JPG)
A derivação reforçada utiliza a chave privada pai, enquanto a derivação normal utiliza a chave pública pai. A função HMAC-SHA512 é utilizada para a derivação reforçada, enquanto a derivação normal utiliza um resumo de 512 bits. A chave pública filha é obtida multiplicando a chave privada filha pelo gerador da curva elíptica.

![image](assets/image/section4/13.JPG)
![image](assets/image/section4/14.JPG)

A hierarquização e a derivação de muitos pares de chaves de forma determinística permitem criar um esquema em árvore para a derivação hierárquica. No próximo curso deste treinamento, estudaremos a estrutura da carteira HD, bem como os caminhos de derivação, com ênfase nas notações dos caminhos de derivação.

## Estrutura da carteira e caminhos de derivação

![Estrutura da carteira e caminhos de derivação](https://youtu.be/etO9UxwyE2I)

Neste capítulo, vamos estudar a estrutura da árvore de derivação em uma carteira HD (Hierarchical Deterministic Wallet). Já exploramos o cálculo da semente, a chave mestra e a derivação dos pares de chaves filhas. Agora, vamos nos concentrar na organização das chaves dentro da carteira.

A carteira HD utiliza camadas de profundidade para organizar as chaves. Cada derivação de um par pai para um par filho corresponde a uma camada de profundidade.

![image](assets/image/section4/15.JPG)

- A profundidade 0 corresponde à chave mestra e ao código de cadeia mestra.

- A profundidade 1 é usada para derivar chaves filhas de acordo com um objetivo específico, que é determinado pelo índice. Os objetivos estão em conformidade com os padrões BIP 84 e Segwit v0/v1.

- A profundidade 2 permite diferenciar contas de diferentes criptomoedas ou redes. Isso permite organizar a carteira com base em diferentes fontes de fundos. Para o bitcoin, o índice será 0.

- A profundidade 3 é usada para organizar a carteira em diferentes contas, oferecendo assim uma estrutura mais clara e organizada.
- A profundidade 4 corresponde às cadeias externa e interna, que são usadas para endereços destinados a serem comunicados publicamente. O índice 0 está associado à cadeia externa, enquanto o índice 1 está associado à cadeia interna. Cada conta tem duas cadeias: a cadeia externa (0) e a cadeia interna (1). A profundidade 4 também é usada para lidar com tipos de script no caso de carteiras multiassinaturas.
- A profundidade 5 é usada para endereços de recebimento em uma carteira clássica. Na próxima seção, examinaremos mais detalhadamente a derivação de pares de chaves filhas.

![image](assets/image/section4/16.JPG)

Para cada camada de profundidade, usamos índices para diferenciar os pares de chaves filhas.

O índice sem apóstrofo corresponde ao índice real usado, enquanto o índice com apóstrofo corresponde ao índice real + 2^31. As derivações reforçadas usam índices de 2^31 a 2^32-1. Por exemplo, o índice 44' corresponde ao índice real 2^31 + 44.

Para gerar um endereço de recebimento específico, derivamos um par de chaves filhas da chave mestra e do código da cadeia mestra. Em seguida, usamos o índice para diferenciar os diferentes pares de chaves filhas da mesma profundidade.

Chaves estendidas, como XPUB, permitem compartilhar sua carteira com várias pessoas. A cadeia de derivação é usada para diferenciar a cadeia externa (endereços destinados a serem comunicados) e a cadeia interna (endereços de troco).

No próximo capítulo, estudaremos endereços de recebimento, suas vantagens de uso e os passos para sua construção.

# O que é um endereço Bitcoin?

## Endereços Bitcoin

![Endereços Bitcoin](https://youtu.be/nqGBMjPtFNI)

![image](assets/image/section5/0.JPG)

Neste capítulo, exploraremos os endereços de recebimento, que desempenham um papel crucial no sistema Bitcoin. Eles permitem receber fundos e são gerados a partir de pares de chaves privadas e públicas. Embora exista um tipo de script chamado Pay2PublicKey que permite bloquear bitcoins em uma chave pública, os usuários geralmente preferem usar endereços de recebimento em vez desse script.

Quando um destinatário deseja receber bitcoins, ele fornece um endereço de recebimento ao remetente em vez de sua chave pública. Um endereço é na verdade um hash de uma chave pública, com um formato específico.

![image](assets/image/section5/1.JPG)
É importante notar que não é possível rastrear do endereço para a chave pública, ou da chave pública para a chave privada. O uso de um endereço reduz o tamanho da informação da chave pública, que é inicialmente de 512 bits.
Os endereços Bitcoin foram reduzidos em tamanho para torná-los mais fáceis de usar. Têm uma soma de controlo, que permite detetar erros de digitação e reduzir o risco de perda de bitcoins. As chaves públicas, por outro lado, não têm checksum, o que significa que erros de digitação podem resultar na perda dos fundos correspondentes.

Os endereços também fornecem uma segunda camada de segurança entre as informações públicas e privadas, tornando mais difícil assumir o controlo da chave privada.

É essencial sublinhar que cada endereço deve ser único. A reutilização do mesmo endereço levanta problemas de confidencialidade e deve ser evitada.

São utilizados diferentes prefixos para os endereços Bitcoin. Por exemplo, BC1Q corresponde a um endereço Segwit V0, BC1P a um endereço Taproot/Segwit V1, e os prefixos 1 e 3 estão associados a endereços Pay2PublicKeyH/Pay2ScriptH (legacy). Na próxima lição, explicaremos passo a passo como derivar um endereço a partir de uma chave pública.

## Como criar um endereço Bitcoin?

Como criar um endereço Bitcoin (https://youtu.be/ewMGTN8dKjI)

Neste capítulo, veremos a construção de um endereço de recebimento para transações Bitcoin. Um endereço de recebimento é uma representação alfanumérica de uma chave pública comprimida. Há vários passos envolvidos na conversão de uma chave pública em um endereço de recebimento.

### Passo 1: Comprimir a chave pública

![image](assets/image/section5/14.png)

Um endereço é derivado de uma chave pública filha.

Uma chave pública é um ponto na curva elíptica. Graças à simetria da curva elíptica, um ponto na curva elíptica terá apenas um eixo x associado a dois valores possíveis para y: positivo ou negativo.
No entanto, no protocolo Bitcoin, trabalhamos com um campo finito de números inteiros positivos em vez do campo real. Para distinguir entre os dois valores possíveis para y, basta indicar se y é par ou ímpar.

A compressão de uma chave pública reduz o seu tamanho de 520 bits para 264 bits.

Utilizamos o prefixo 0x02 para um y par e 0x03 para um y ímpar. Esta é a forma comprimida da chave pública.

### Passo 2: Como fazer o hashing da chave pública comprimida

![image](assets/image/section5/3.JPG)
Hashing da chave pública comprimida é realizado com a função SHA256. Em seguida, a função RIPEMD160 é aplicada ao resumo.

### Etapa 3: O payload = Carga útil do endereço

![image](assets/image/section5/4.JPG)

O resumo binário de RIPEMD160(SHA256(K)) é usado para formar grupos de 5 bits. Cada grupo é convertido para base16 (Hexadecimal) e/ou base 10.

### Etapa 4: Adição de metadados para o cálculo do checksum com o programa BCH

![image](assets/image/section5/5.JPG)

No caso dos endereços legados, usamos o hash duplo SHA256 para gerar o checksum do endereço. No entanto, para os endereços Segwit V0 e V1, usamos a tecnologia de checksum BCH para garantir a detecção de erros. O programa BCH é capaz de sugerir e corrigir erros com uma probabilidade de erro extremamente baixa. Atualmente, o programa BCH é usado para detectar e sugerir modificações, mas não as realiza automaticamente em substituição ao usuário.

O programa BCH requer várias informações de entrada, incluindo o HRP (Parte Legível pelo Humano) que precisa ser expandido. A expansão do HRP envolve a codificação de cada letra em base 2 de acordo com seu código ASCII. Em seguida, pegando os 3 primeiros bits do resultado para cada letra em base 10 (em azul na imagem). Inserir um separador 0. Em seguida, concatenar os 5 últimos bits de cada letra previamente convertidos em base 10 (em amarelo na imagem).

A expansão do HRP em base 10 permite isolar os cinco últimos bits de cada caractere, reforçando assim o checksum.

A versão Segwit V0 é representada pelo código 00 e o "payload" está em preto, em base 10. Isso é seguido por seis caracteres reservados para o checksum.

### Etapa 5: Cálculo do checksum com o programa BCH

![image](assets/image/section5/6.JPG)

A entrada contendo os metadados é então submetida ao programa BCH para obter o checksum em base 10.

Aqui temos o checksum.

### Etapa 6: Construção do endereço e conversão para Bech32

![image](assets/image/section5/7.JPG)

A concatenação da versão, do payload e do checksum permite construir o endereço. Os caracteres em base 10 são então convertidos em caracteres bech32 usando uma tabela de correspondência. O alfabeto bech32 inclui todos os caracteres alfanuméricos, exceto 1, b, i e o, para evitar confusão.

### Etapa 7: Adição do HRP e do separador

![image](assets/image/section5/8.JPG)

Em rosa o checksum.
Em preto, o payload = o hash da chave pública.
Em azul, a versão.
O texto traduzido para o português mantendo o mesmo layout markdown é:

Tudo isto é convertido em Bech32, depois adiciona-se 'bc' para bitcoin e '1' como separador, e aqui está o endereço.
Assim, passamos pelas etapas envolvidas na construção de um endereço de receção, usando a tecnologia de soma de verificação BCH e construindo um endereço começando com bc1q ou bc1p usando a variante BCH32 da base 32 específica do Bitcoin.

## Resumo da criptografia para carteiras Bitcoin

![resumo de treinamento](https://youtu.be/NkAYoVUMvOs)

As funções de hash usadas no protocolo Bitcoin têm características necessárias para a segurança do protocolo. Elas devem ser irreversíveis (= resistência à pré-imagem), resistentes à falsificação, resistentes a colisões e à segunda pré-imagem.

![image](assets/image/section5/11.JPG)

Outro método criptográfico amplamente utilizado no protocolo Bitcoin é o método de assinaturas digitais.

![image](assets/image/section5/12.JPG)

Ao longo deste treinamento, estudamos em profundidade a carteira determinística hierárquica (HD) com o BIP32. A entropia desempenha um papel central nesse tipo de carteira, pois é usada para gerar uma frase mnemônica a partir de um número aleatório.

Esse número aleatório é então formatado em um formato de 256 bits usando a função de hash SHA256. O checksum corresponde aos 8 primeiros bits desse resultado. A frase mnemônica corresponde à concatenação do número aleatório com o checksum. Com a lista de 2048 palavras fornecida no BIP39, essa frase mnemônica pode ser codificada em uma série de palavras fáceis de lembrar. A frase mnemônica, juntamente com uma possível frase de acesso, são necessárias para gerar a semente da carteira. A frase de acesso atua como um sal criptográfico que adiciona uma camada adicional de proteção à carteira.

A função pbkdf2 é usada para gerar a semente a partir da frase mnemônica e da frase de acesso, usando um HMAC-SHA512 e 2048 iterações. A chave mestra e o código de cadeia mestre são então derivados dessa semente usando novamente a função HMAC-SHA512 com a frase "bitcoin seed". A chave privada mestra e o código de cadeia mestre são os elementos mais altos na hierarquia da carteira HD.

A derivação de uma chave filha depende de vários fatores, incluindo a chave pai e o código de cadeia correspondente. Uma chave estendida é obtida concatenando uma chave pai com seu código de cadeia, enquanto uma chave mestra é uma chave separada.
Para derivar um endereço, a chave pública comprimida é primeiro hashada usando SHA256 e RIPMD160, e então um checksum é calculado. O hash duplo SHA256 é usado para calcular o checksum no caso de um padrão legado, enquanto o programa BCH (Bose-Chaudhuri-Hocquenghem) é usado para calcular o checksum no caso de um padrão segwit. Em seguida, uma representação no formato base 58 é usada para um padrão legado, enquanto o formato bech32 é usado para um padrão segwit, a fim de obter o endereço da carteira HD.
![image](assets/image/section5/13.JPG)

Resumindo, exploramos em detalhes as funções de hash e suas características, bem como as assinaturas digitais e as curvas elípticas. Em seguida, mergulhamos no mundo da carteira determinística hierárquica (HD) com o BIP32, usando a entropia e a frase de acesso para gerar a semente da carteira. Também aprendemos como derivar as chaves filhas e obter o endereço da carteira HD. Espero que essas informações tenham sido úteis para você, e agora encorajo você a fazer a avaliação para testar seus conhecimentos adquiridos durante o treinamento Crypto 301. Obrigado pela sua atenção.
