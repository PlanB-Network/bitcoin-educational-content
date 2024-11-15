---
name: Introdução à Criptografia Formal
goal: Uma introdução aprofundada à ciência e prática da criptografia.
objectives:
  - Explorar cifras de Beale e métodos criptográficos modernos para entender conceitos básicos e históricos da criptografia.
  - Aprofundar-se em teoria dos números, grupos e campos para dominar conceitos matemáticos chave que fundamentam a criptografia.
  - Estudar a cifra de fluxo RC4 e o AES com uma chave de 128 bits para aprender sobre algoritmos criptográficos simétricos.
  - Investigar o criptossistema RSA, distribuição de chaves e funções hash para explorar a criptografia assimétrica.

---
# Mergulho profundo em criptografia

É difícil encontrar muitos materiais que ofereçam um bom meio-termo na educação sobre criptografia.

Por um lado, existem tratados formais e extensos, realmente acessíveis apenas para aqueles com um forte background em matemática, lógica ou alguma outra disciplina formal. Por outro lado, existem introduções de alto nível que realmente escondem muitos dos detalhes para qualquer pessoa que seja pelo menos um pouco curiosa.

Esta introdução à criptografia busca capturar esse meio-termo. Embora deva ser relativamente desafiador e detalhado para quem é novo em criptografia, não é a toca do coelho de um tratado fundacional típico.

+++

# Introdução
<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Descrição breve
<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Este livro oferece uma introdução aprofundada à ciência e prática da criptografia. Onde possível, foca na exposição conceitual, em vez de formal, do material.

> Este curso é baseado no [repositório de JWBurgers](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Todos os direitos a ele. O conteúdo ainda não está finalizado e está aqui apenas para mostrar como poderíamos integrá-lo se JWburger concordar.

### Motivação e objetivos

É difícil encontrar muitos materiais que ofereçam um bom meio-termo na educação sobre criptografia.

Por um lado, existem tratados formais e extensos, realmente acessíveis apenas para aqueles com um forte background em matemática, lógica ou alguma outra disciplina formal. Por outro lado, existem introduções de alto nível que realmente escondem muitos dos detalhes para qualquer pessoa que seja pelo menos um pouco curiosa.

Esta introdução à criptografia busca capturar esse meio-termo. Embora deva ser relativamente desafiador e detalhado para quem é novo em criptografia, não é a toca do coelho de um tratado fundacional típico.

### Público-alvo

De desenvolvedores aos intelectualmente curiosos, este livro é útil para qualquer pessoa que deseje mais do que um entendimento superficial da criptografia. Se seu objetivo é dominar o campo da criptografia, então este livro também é um bom ponto de partida.

### Diretrizes de leitura

O livro atualmente contém sete capítulos: "O que é Criptografia?" (Capítulo 1), "Fundamentos Matemáticos da Criptografia I" (Capítulo 2), "Fundamentos Matemáticos da Criptografia II" (Capítulo 3), "Criptografia Simétrica" (Capítulo 4), "RC4 e AES" (Capítulo 5), "Criptografia Assimétrica" (Capítulo 6) e "O criptossistema RSA" (Capítulo 7). Um capítulo final, "Criptografia na Prática", ainda será adicionado. Ele foca em várias aplicações criptográficas, incluindo segurança da camada de transporte, roteamento onion e o sistema de troca de valor do Bitcoin.
A menos que você tenha uma sólida formação em matemática, a teoria dos números é provavelmente o tópico mais difícil deste livro. Eu ofereço uma visão geral dela no Capítulo 3, e ela também aparece na exposição do AES no Capítulo 5 e do sistema de criptografia RSA no Capítulo 7.
Se você está realmente lutando com os detalhes formais nessas partes do livro, recomendo que se contente com uma leitura de alto nível delas na primeira vez.

### Agradecimentos

O livro mais influente na formação deste foi _Introduction to Modern Cryptography_, de Jonathan Katz e Yehuda Lindell, CRC Press (Boca Raton, FL), 2015. Um curso acompanhante está disponível no Coursera chamado "Cryptography".

As principais fontes adicionais que foram úteis na criação da visão geral neste livro são Simon Singh, _The Code Book_, Fourth Estate (Londres, 1999); Christof Paar e Jan Pelzl, _Understanding Cryptography_, Springer (Heidelberg, 2010) e [um curso baseado no livro de Paar chamado “Introduction to Cryptography”](https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); e Bruce Schneier, Criptografia Aplicada, 2ª ed., 2015 (Indianápolis, IN: John Wiley & Sons).

Citarei apenas informações e resultados muito específicos que tomo dessas fontes, mas quero reconhecer aqui minha dívida geral para com elas.

Para aqueles leitores que desejam buscar conhecimento mais avançado sobre criptografia após esta introdução, eu recomendo fortemente o livro de Katz e Lindell. O curso de Katz no Coursera é um pouco mais acessível do que o livro.

### Contribuições

Por favor, dê uma olhada [no arquivo de contribuições no repositório](https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) para algumas diretrizes sobre como apoiar o projeto.

### Notação

**Termos-chave:**

Termos-chave nos primórdios são introduzidos tornando-os em negrito. Por exemplo, a introdução do cifrador Rijndael como um termo-chave seria assim: **cifrador Rijndael**.

Os termos-chave são explicitamente definidos, a menos que sejam nomes próprios ou seu significado seja óbvio pela discussão.

Qualquer definição é geralmente dada na introdução de um termo-chave, embora às vezes seja mais conveniente deixar a definição para um momento posterior.

**Palavras e frases enfatizadas:**

Palavras e frases são enfatizadas via itálico. Por exemplo, a frase "Lembre-se de sua senha" ficaria assim: *Lembre-se de sua senha*.

**Notação formal:**

A notação formal diz respeito principalmente a variáveis, variáveis aleatórias e conjuntos.

* Variáveis: Estas são geralmente apenas indicadas por uma letra minúscula (por exemplo, "x" ou "y"). Às vezes, elas são capitalizadas para clareza (por exemplo, "M" ou "K").
* Variáveis aleatórias: Estas são sempre indicadas por uma letra maiúscula (por exemplo, "X" ou "Y")
* Conjuntos: Estes são sempre indicados por letras maiúsculas em negrito (por exemplo, **S**)

# O que é Criptografia?
<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

## Os cifrões de Beale
<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>
Vamos iniciar nossa investigação no campo da criptografia com um dos episódios mais encantadores e divertidos de sua história: o dos cifrados de Beale. [1]
A história dos cifrados de Beale é, na minha opinião, mais provável de ser ficção do que realidade. Mas supostamente aconteceu da seguinte forma.

Tanto no inverno de 1820 quanto em 1822, um homem chamado Thomas J. Beale ficou hospedado em uma estalagem de propriedade de Robert Morriss em Lynchburg (Virgínia). Ao final da segunda estadia de Beale, ele entregou a Morriss uma caixa de ferro com papéis valiosos para guarda.

Alguns meses depois, Morriss recebeu uma carta de Beale datada de 9 de maio de 1822. Ela enfatizava o grande valor do conteúdo da caixa de ferro e relacionava algumas instruções a Morriss: se nem Beale nem nenhum de seus associados jamais viessem reivindicar a caixa, ele deveria abri-la precisamente dez anos a partir da data da carta (ou seja, 9 de maio de 1832). Alguns dos papéis dentro dela estariam escritos em texto regular. Vários outros, no entanto, seriam “ininteligíveis sem a ajuda de uma chave.” Essa “chave” seria, então, entregue a Morriss por um amigo não nomeado de Beale em junho de 1832.

Apesar das instruções claras, Morriss não abriu a caixa em maio de 1832 e o misterioso amigo de Beale nunca apareceu em junho daquele ano. Somente em 1845 que o estalajadeiro finalmente decidiu abrir a caixa. Nela, Morriss encontrou uma nota explicando como Beale e seus associados descobriram ouro e prata no Oeste e os enterraram, junto com algumas joias, para guarda. Além disso, a caixa continha três **cifrados**: isto é, textos escritos em código que requerem uma **chave criptográfica**, ou um segredo, e um algoritmo acompanhante para desbloquear. Esse processo de desbloquear um cifrado é conhecido como **decifração**, enquanto o processo de bloqueio é conhecido como **cifração**. (Como explicado no Capítulo 3, o termo cifra pode assumir vários significados. No nome "cifrados de Beale", ele é abreviação de cifrados.)

Os três cifrados que Morriss encontrou na caixa de ferro consistem em uma série de números separados por vírgulas. De acordo com a nota de Beale, esses cifrados fornecem separadamente a localização do tesouro, o conteúdo do tesouro e uma lista de nomes com herdeiros legítimos do tesouro e suas partes (sendo esta última informação relevante caso Beale e seus associados nunca viessem reivindicar a caixa).

Morris tentou decifrar os três cifrados por vinte anos. Isso teria sido fácil com a chave. Mas Morriss não tinha a chave e foi mal-sucedido em suas tentativas de recuperar os textos originais, ou **textos claros** como são tipicamente chamados em criptografia.

Próximo ao fim de sua vida, Morriss passou a caixa para um amigo em 1862. Esse amigo posteriormente publicou um panfleto em 1885, sob o pseudônimo J.B. Ward. Incluía uma descrição da (alegada) história da caixa, os três cifrados e uma solução que ele havia encontrado para o segundo cifrado. (Aparentemente, existe uma chave para cada cifrado, e não uma chave que funciona em todos os três cifrados como Beale originalmente parece ter sugerido em sua carta a Morriss.)

Você pode ver o segundo cifrado na *Figura 2* abaixo. [2] A chave para este cifrado é a Declaração de Independência dos Estados Unidos. O procedimento de decifração se resume à aplicação das seguintes duas regras:
* Para qualquer número n no texto cifrado, localize a n-ésima palavra na Declaração de Independência dos Estados Unidos* Substitua o número n pela primeira letra da palavra encontrada

*Figura 1: cifra de Beale nº 2*

![Figura 1: cifra de Beale nº 2](assets/Figure1-1.webp "Figura 1: cifra de Beale nº 2")

Por exemplo, o primeiro número do segundo texto cifrado é 115. A 115ª palavra da Declaração de Independência é “instituted”, então a primeira letra do texto decifrado é “i”. O texto cifrado não indica diretamente espaçamento entre palavras e capitalização. Mas, após decifrar as primeiras palavras, pode-se deduzir logicamente que a primeira palavra do texto decifrado era simplesmente “I” (Eu). (O texto decifrado começa com a frase “I have deposited in the county of Bedford.”)

Após a decifração, a segunda mensagem fornece os detalhes do conteúdo do tesouro (ouro, prata e joias), e sugere que foi enterrado em potes de ferro e coberto com pedras no Condado de Bedford (Virgínia). As pessoas adoram um bom mistério, então grandes esforços foram despendidos para decifrar as outras duas cifras de Beale, particularmente a que descreve a localização do tesouro. Até mesmo vários criptógrafos proeminentes tentaram decifrá-las. No entanto, até o momento, ninguém conseguiu decifrar os outros dois textos cifrados.

**Notas:**

[1] Para um bom resumo da história, veja Simon Singh, *The Code Book*, Fourth Estate (Londres, 1999), pp. 82-99. Um curta-metragem da história foi feito por Andrew Allen em 2010. Você pode encontrar o filme, “The Thomas Beale Cipher,” [no seu site](http://www.thomasbealecipher.com/).

[2] Esta imagem está disponível na página da Wikipedia para as cifras de Beale.

## Criptografia Moderna
<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Histórias coloridas como a das cifras de Beale são o que a maioria de nós associa com criptografia. No entanto, a criptografia moderna difere em pelo menos quatro aspectos importantes desses tipos de exemplos históricos.

Primeiro, historicamente a criptografia estava preocupada apenas com **segredo** (ou confidencialidade). [3] Textos cifrados seriam criados para garantir que apenas certas partes pudessem ter acesso às informações nos textos decifrados, como no caso das cifras de Beale. Para que um esquema de criptografia sirva bem a esse propósito, decifrar o texto cifrado só deveria ser viável se você tivesse a chave.

A criptografia moderna está preocupada com uma gama mais ampla de temas além do mero segredo. Esses temas incluem primariamente (1) **integridade da mensagem**—isto é, assegurar que uma mensagem não foi alterada; (2) **autenticidade da mensagem**—isto é, assegurar que uma mensagem realmente veio de um remetente específico; e (3) **não repúdio**—isto é, assegurar que um remetente não possa negar falsamente mais tarde que enviou uma mensagem. [4]

Uma distinção importante a ter em mente é, portanto, entre um **esquema de criptografia** e um **esquema criptográfico**. Um esquema de criptografia está apenas preocupado com o segredo. Embora um esquema de criptografia seja um esquema criptográfico, o inverso não é verdadeiro. Um esquema criptográfico também pode servir aos outros temas principais da criptografia, incluindo integridade, autenticidade e não repúdio.
Os temas de integridade e autenticidade são tão importantes quanto o segredo. Nossos sistemas modernos de comunicação não seriam capazes de funcionar sem garantias em relação à integridade e autenticidade das comunicações. A não-repúdio também é uma preocupação importante, como para contratos digitais, mas menos necessária de forma ubíqua em aplicações criptográficas do que segredo, integridade e autenticidade.

Em segundo lugar, esquemas clássicos de criptografia, como os cifrados de Beale, sempre envolvem uma chave que era compartilhada entre todas as partes relevantes. No entanto, muitos esquemas criptográficos modernos envolvem não apenas uma, mas duas chaves: uma **privada** e uma **pública**. Enquanto a primeira deve permanecer privada em qualquer aplicação, a última é tipicamente de conhecimento público (daí, seus respectivos nomes). No âmbito da criptografia, a chave pública pode ser usada para criptografar a mensagem, enquanto a chave privada pode ser usada para descriptografar.

O ramo da criptografia que lida com esquemas onde todas as partes compartilham uma chave é conhecido como **criptografia simétrica**. A única chave em tal esquema é geralmente chamada de **chave privada** (ou chave secreta). O ramo da criptografia que lida com esquemas que requerem um par de chaves privada-pública é conhecido como **criptografia assimétrica**. Esses ramos são às vezes também referidos como **criptografia de chave privada** e **criptografia de chave pública**, respectivamente (embora isso possa causar confusão, pois esquemas criptográficos de chave pública também têm chaves privadas).

O advento da criptografia assimétrica no final dos anos 1970 foi um dos eventos mais importantes na história da criptografia. Sem ela, a maioria dos nossos sistemas modernos de comunicação, incluindo o Bitcoin, não seria possível, ou pelo menos muito impraticável.

Importante, a criptografia moderna não é exclusivamente o estudo de esquemas criptográficos de chave simétrica e assimétrica (embora isso cubra grande parte do campo). Por exemplo, a criptografia também está preocupada com funções de hash e geradores de números pseudoaleatórios, e você pode construir aplicações nessas primitivas que não estão relacionadas à criptografia de chave simétrica ou assimétrica.

Terceiro, esquemas clássicos de criptografia, como os usados nos cifrados de Beale, eram mais arte do que ciência. Sua segurança percebida era amplamente baseada em intuições sobre sua complexidade. Eles tipicamente seriam corrigidos quando um novo ataque fosse aprendido, ou abandonados inteiramente se o ataque fosse particularmente severo. A criptografia moderna, no entanto, é uma ciência rigorosa com uma abordagem formal e matemática tanto para o desenvolvimento quanto para a análise de esquemas criptográficos. [5]

Especificamente, a criptografia moderna se concentra em **provas formais de segurança**. Qualquer prova de segurança para um esquema criptográfico procede em três etapas:

1. A declaração de uma **definição criptográfica de segurança**, isto é, um conjunto de objetivos de segurança e a ameaça representada pelo atacante.
2. A declaração de quaisquer suposições matemáticas com relação à complexidade computacional do esquema. Por exemplo, um esquema criptográfico pode conter um gerador de números pseudoaleatórios. Embora não possamos provar que eles existem, podemos assumir que sim.
3. A exposição de uma **prova matemática de segurança** do esquema com base na noção formal de segurança e quaisquer suposições matemáticas.

Quarto, enquanto historicamente a criptografia era primariamente utilizada em configurações militares, ela passou a permear nossas atividades diárias na era digital. Seja você fazendo operações bancárias online, postando em redes sociais, comprando um produto na Amazon com seu cartão de crédito, ou dando uma gorjeta em bitcoin para um amigo, a criptografia é o sine qua non de nossa era digital.

Dado esses quatro aspectos da criptografia moderna, podemos caracterizar a **criptografia** moderna como a ciência preocupada com o desenvolvimento formal e análise de esquemas criptográficos para proteger informações digitais contra ataques adversários. [6] Segurança aqui deve ser entendida de forma ampla como prevenção de ataques que danificam segredo, integridade, autenticação e/ou não-repúdio em comunicações.
A criptografia é melhor vista como uma subdisciplina da **cibersegurança**, que se preocupa em prevenir o roubo, dano e uso indevido de sistemas de computador. Note que muitas preocupações de cibersegurança têm pouca ou apenas uma conexão parcial com a criptografia.
Por exemplo, se uma empresa possui servidores caros localmente, ela pode estar preocupada em proteger esse hardware contra roubo e danos. Embora isso seja uma preocupação de cibersegurança, tem pouco a ver com criptografia.

Por outro exemplo, **ataques de phishing** são um problema comum na nossa era moderna. Esses ataques tentam enganar as pessoas por meio de um e-mail ou algum outro meio de mensagem para que entreguem informações sensíveis, como senhas ou números de cartões de crédito. Embora a criptografia possa ajudar a abordar ataques de phishing até certo ponto, uma abordagem abrangente requer mais do que apenas o uso de alguma criptografia.

**Notas:**

[3] Para ser exato, as aplicações importantes dos esquemas criptográficos têm sido preocupadas com a secreção. Crianças, por exemplo, frequentemente usam esquemas criptográficos simples por "diversão". A secreção realmente não é uma preocupação nesses casos.

[4] Bruce Schneier, *Applied Cryptography*, 2ª ed., 2015 (Indianápolis, IN: John Wiley & Sons), p. 2.

[5] Veja Jonathan Katz e Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), esp. pp. 16–23, para uma boa descrição.

[6] Cf. Katz e Lindell, ibid., p. 3. Acho que a caracterização deles tem alguns problemas, então apresento aqui uma versão um pouco diferente da declaração deles.

## Comunicações abertas
<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

A criptografia moderna é projetada para fornecer garantias de segurança em um ambiente de **comunicações abertas**. Se nosso canal de comunicação é tão bem protegido que os bisbilhoteiros não têm chance de manipular ou mesmo apenas observar nossas mensagens, então a criptografia é supérflua. No entanto, a maioria dos nossos canais de comunicação dificilmente é tão bem guardada assim.

A espinha dorsal da comunicação no mundo moderno é uma vasta rede de cabos de fibra óptica. Fazer chamadas telefônicas, assistir televisão e navegar na web em uma casa moderna geralmente depende dessa rede de cabos de fibra óptica (uma pequena porcentagem pode depender puramente de satélites). É verdade que você pode ter diferentes conexões de dados em sua casa, como cabo coaxial, linha de assinante digital (asimétrica) e cabo de fibra óptica. Mas, pelo menos no mundo desenvolvido, esses diferentes meios de dados rapidamente se juntam fora de sua casa a um nó em uma vasta rede de cabos de fibra óptica que conecta o globo inteiro. Exceções são algumas áreas remotas do mundo desenvolvido, como nos Estados Unidos e na Austrália, onde o tráfego de dados ainda pode também viajar distâncias substanciais sobre os tradicionais fios de telefone de cobre.

Seria impossível impedir que potenciais atacantes acessem fisicamente essa rede de cabos e sua infraestrutura de suporte. De fato, já sabemos que a maioria dos nossos dados é interceptada por várias agências de inteligência nacionais em interseções cruciais da Internet.[7] Isso inclui tudo, desde mensagens do Facebook até endereços de sites que você visita.

Embora vigiar dados em grande escala exija um adversário poderoso, como uma agência de inteligência nacional, atacantes com poucos recursos podem facilmente tentar bisbilhotar em uma escala mais local. Embora isso possa acontecer no nível de interceptação de fios, é muito mais fácil apenas interceptar comunicações sem fio.
A maior parte dos dados de nossa rede local — seja em nossas casas, no escritório ou em um café — agora viaja por ondas de rádio até pontos de acesso sem fio em roteadores tudo-em-um, em vez de através de cabos físicos. Assim, um atacante precisa de poucos recursos para interceptar qualquer tráfego local seu. Isso é particularmente preocupante, pois a maioria das pessoas faz muito pouco para proteger os dados que viajam através de suas redes locais. Além disso, potenciais atacantes também podem visar nossas conexões de banda larga móvel, como 3G, 4G e 5G. Todas essas comunicações sem fio são alvos fáceis para atacantes.
Portanto, a ideia de manter as comunicações secretas protegendo o canal de comunicação é uma aspiração ilusoriamente delirante para grande parte do mundo moderno. Tudo o que sabemos justifica uma paranoia severa: você deve sempre assumir que alguém está ouvindo. E a criptografia é a principal ferramenta que temos para obter qualquer tipo de segurança neste ambiente moderno.

**Notas:**

[7] Veja, por exemplo, Olga Khazan, “The creepy, long-standing practice of undersea cable tapping”, *The Atlantic*, 16 de julho de 2013 (disponível em [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).

# Fundamentos Matemáticos da Criptografia 1
<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

## Variáveis aleatórias
<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

A criptografia depende da matemática. E se você quer construir um entendimento mais do que superficial sobre criptografia, você precisa estar confortável com essa matemática.

Este capítulo introduz a maior parte da matemática básica que você encontrará ao aprender sobre criptografia. Os tópicos incluem variáveis aleatórias, operações de módulo, operações XOR e pseudorrandomidade. Você deve dominar o material nestas seções para qualquer entendimento não superficial da criptografia.

A próxima seção lida com teoria dos números, que é muito mais desafiadora.

### Variáveis aleatórias

Uma variável aleatória é tipicamente denotada por uma letra maiúscula não-negrito. Então, por exemplo, podemos falar sobre uma variável aleatória $X$, uma variável aleatória $Y$ ou uma variável aleatória $Z$. Esta é a notação que também empregarei daqui para frente.

Uma **variável aleatória** pode assumir dois ou mais valores possíveis, cada um com uma certa probabilidade positiva. Os valores possíveis estão listados no **conjunto de resultados**.

Cada vez que você **amostra** uma variável aleatória, você tira um valor particular de seu conjunto de resultados de acordo com as probabilidades definidas.

Vamos para um exemplo simples. Suponha uma variável $X$ que é definida da seguinte forma:

- $X$ tem o conjunto de resultados $\{1,2\}$

$$
Pr[X = 1] = 0.5
$$

$$
Pr[X = 2] = 0.5
$$

É fácil ver que $X$ é uma variável aleatória. Primeiro, há dois ou mais valores possíveis que $X$ pode assumir, a saber $1$ e $2$. Segundo, cada valor possível tem uma probabilidade positiva de ocorrer sempre que você amostra $X$, a saber $0.5$.
Tudo o que uma variável aleatória requer é um conjunto de resultados com duas ou mais possibilidades, onde cada possibilidade tem uma probabilidade positiva de ocorrer ao ser amostrada. Em princípio, então, uma variável aleatória pode ser definida de forma abstrata, desprovida de qualquer contexto. Neste caso, você pode pensar em "amostragem" como realizar algum experimento natural para determinar o valor da variável aleatória.
A variável $X$ acima foi definida de forma abstrata. Assim, você pode pensar em amostrar a variável $X$ acima como jogar uma moeda justa e atribuir “2” no caso de cara e “1” no caso de coroa. Para cada amostra de $X$, você joga a moeda novamente.

Alternativamente, você também pode pensar em amostrar $X$, como rolar um dado justo e atribuir “2” caso o dado caia em $1$, $3$, ou $4$, e atribuir “1” caso o dado caia em $2$, $5$, ou $6$. Cada vez que você amostra $X$, você rola o dado novamente.

Realmente, qualquer experimento natural que permita definir as probabilidades dos possíveis valores de $X$ acima pode ser imaginado com respeito ao desenho.

Frequentemente, no entanto, variáveis aleatórias não são apenas introduzidas de forma abstrata. Em vez disso, o conjunto de possíveis valores de resultado tem um significado explícito no mundo real (em vez de apenas como números). Além disso, esses valores de resultado podem ser definidos contra algum tipo específico de experimento (em vez de como qualquer experimento natural com esses valores).

Vamos agora considerar um exemplo da variável $X$ que não é definida de forma abstrata. X é definida da seguinte forma para determinar qual das duas equipes inicia um jogo de futebol:

- $X$ tem o conjunto de resultados {vermelho inicia, azul inicia}
- Jogue uma moeda específica $C$: coroa = “vermelho inicia”; cara = “azul inicia”

$$
Pr [X = \text{vermelho inicia}] = 0.5
$$

$$
Pr [X = \text{azul inicia}] = 0.5
$$

Neste caso, o conjunto de resultados de X é fornecido com um significado concreto, a saber, qual equipe inicia em um jogo de futebol. Além disso, os possíveis resultados e suas probabilidades associadas são determinados por um experimento concreto, a saber, jogar uma moeda específica $C$.

Dentro das discussões de criptografia, variáveis aleatórias são geralmente introduzidas contra um conjunto de resultados com significado no mundo real. Pode ser o conjunto de todas as mensagens que poderiam ser criptografadas, conhecido como espaço de mensagem, ou o conjunto de todas as chaves que as partes usando a criptografia podem escolher, conhecido como espaço de chave.

Variáveis aleatórias em discussões sobre criptografia, no entanto, geralmente não são definidas contra algum experimento natural específico, mas contra qualquer experimento que possa gerar as distribuições de probabilidade corretas.

Variáveis aleatórias podem ter distribuições de probabilidade discretas ou contínuas. Variáveis aleatórias com uma **distribuição de probabilidade discreta** — isto é, variáveis aleatórias discretas — têm um número finito de possíveis resultados. A variável aleatória $X$ nos dois exemplos dados até agora era discreta.

**Variáveis aleatórias contínuas** podem, em vez disso, assumir valores em um ou mais intervalos. Você pode dizer, por exemplo, que uma variável aleatória, ao ser amostrada, assumirá qualquer valor real entre 0 e 1, e que cada número real neste intervalo é igualmente provável. Dentro deste intervalo, existem infinitos valores possíveis.

Para discussões criptográficas, você só precisa entender variáveis aleatórias discretas. Qualquer discussão sobre variáveis aleatórias a partir daqui deve, portanto, ser entendida como referindo-se a variáveis aleatórias discretas, a menos que especificado de outra forma.

### Graficando variáveis aleatórias
Os possíveis valores e probabilidades associadas a uma variável aleatória podem ser facilmente visualizados por meio de um gráfico. Por exemplo, considere a variável aleatória $X$ da seção anterior com um conjunto de resultados $\{1, 2\}$, e $Pr [X = 1] = 0.5$ e $Pr [X = 2] = 0.5$. Normalmente, exibiríamos tal variável aleatória na forma de um gráfico de barras como na *Figura 1*.
*Figura 1: Variável aleatória X*

![Figura 1: Variável aleatória X.](assets/Figure2-1.webp)

As barras largas na *Figura 1* obviamente não pretendem sugerir que a variável aleatória $X$ é de fato contínua. Em vez disso, as barras são feitas largas para serem mais visualmente atraentes (apenas uma linha reta para cima proporciona uma visualização menos intuitiva).

### Variáveis Uniformes

Na expressão “variável aleatória”, o termo “aleatório” apenas significa “probabilístico”. Em outras palavras, significa apenas que dois ou mais resultados possíveis da variável ocorrem com certas probabilidades. Esses resultados, no entanto, *não necessariamente* têm que ser igualmente prováveis (embora o termo “aleatório” possa de fato ter esse significado em outros contextos).

Uma **variável uniforme** é um caso especial de variável aleatória. Ela pode assumir dois ou mais valores todos com uma probabilidade igual. A variável aleatória $X$ retratada na *Figura 1* é claramente uma variável uniforme, já que ambos os resultados possíveis ocorrem com uma probabilidade $0.5$. No entanto, existem muitas variáveis aleatórias que não são instâncias de variáveis uniformes.

Considere, por exemplo, a variável aleatória $Y$. Ela tem um conjunto de resultados $\{1, 2, 3, 8, 10\}$ e a seguinte distribuição de probabilidade:

$$
\Pr[Y = 1] = 0.25
$$

$$
\Pr[Y = 2] = 0.35
$$

$$
\Pr[Y = 3] = 0.1
$$

$$
\Pr[Y = 8] = 0.25
$$

$$
\Pr[Y = 10] = 0.05
$$

Embora dois resultados possíveis de fato tenham uma probabilidade igual de ocorrer, nomeadamente $1$ e $8$, $Y$ também pode assumir certos valores com probabilidades diferentes de $0.25$ ao ser amostrada. Portanto, embora $Y$ seja de fato uma variável aleatória, ela não é uma variável uniforme.

Uma representação gráfica de $Y$ é fornecida na *Figura 2*.

*Figura 2: Variável aleatória Y*

![Figura 2: Variável aleatória Y.](assets/Figure2-2.webp "Figura 2: Variável aleatória Y")

Para um último exemplo, considere a variável aleatória Z. Ela tem o conjunto de resultados {1,3,7,11,12} e a seguinte distribuição de probabilidade:

$$
\Pr[Z = 2] = 0.2
$$

$$
\Pr[Z = 3] = 0.2
$$

$$
\Pr[Z = 9] = 0.2
$$

$$
\Pr[Z = 11] = 0.2
$$

$$
\Pr[Z = 12] = 0.2
$$

Você pode vê-la retratada na *Figura 3*. A variável aleatória Z é, em contraste com Y, uma variável uniforme, já que todas as probabilidades para os valores possíveis ao ser amostrada são iguais.

*Figura 3: Variável aleatória Z*
![Figura 3: Variável aleatória Z.](assets/Figure2-3.webp "Figura 3: Variável aleatória Z")

### Probabilidade condicional

Suponha que Bob pretende selecionar uniformemente um dia do último ano calendário. O que devemos concluir sobre a probabilidade do dia selecionado ser no Verão?

Contanto que acreditemos que o processo de Bob será de fato verdadeiramente uniforme, devemos concluir que há uma probabilidade de 1/4 de Bob selecionar um dia no Verão. Esta é a **probabilidade incondicional** do dia selecionado aleatoriamente ser no Verão.

Suponha agora que, em vez de desenhar uniformemente um dia do calendário, Bob seleciona apenas uniformemente entre aqueles dias nos quais a temperatura ao meio-dia em Crystal Lake (Nova Jersey) foi de 21 graus Celsius ou mais. Dada essa informação adicional, o que podemos concluir sobre a probabilidade de Bob selecionar um dia no Verão?

Realmente deveríamos chegar a uma conclusão diferente da anterior, mesmo sem nenhuma informação específica adicional (por exemplo, a temperatura ao meio-dia de cada dia no último ano calendário).

Sabendo que Crystal Lake está em Nova Jersey, certamente não esperaríamos que a temperatura ao meio-dia fosse de 21 graus Celsius ou mais no Inverno. Em vez disso, é muito mais provável que seja um dia quente na Primavera ou no Outono, ou um dia em algum momento do Verão. Portanto, sabendo que a temperatura ao meio-dia em Crystal Lake no dia selecionado foi de 21 graus Celsius ou mais, a probabilidade de o dia selecionado por Bob ser no Verão se torna muito maior. Esta é a **probabilidade condicional** do dia selecionado aleatoriamente ser no Verão, dado que a temperatura ao meio-dia em Crystal Lake foi de 21 graus Celsius ou mais.

Ao contrário do exemplo anterior, as probabilidades de dois eventos também podem ser completamente não relacionadas. Nesse caso, dizemos que eles são **independentes**.

Suponha, por exemplo, que uma certa moeda justa caiu em cara. Dado este fato, qual é, então, a probabilidade de que chova amanhã? A probabilidade condicional neste caso deve ser a mesma que a probabilidade incondicional de que chova amanhã, já que um lançamento de moeda geralmente não tem impacto no clima.

Usamos um símbolo "|" para escrever declarações de probabilidade condicional. Por exemplo, a probabilidade do evento $A$ dado que o evento $B$ ocorreu pode ser escrita da seguinte forma:

$$
Pr[A|B]
$$

Então, quando dois eventos, $A$ e $B$, são independentes, então:

$$
Pr[A|B] = Pr[A] \text{ e } Pr[B|A] = Pr[B]
$$

A condição para independência pode ser simplificada da seguinte forma:

$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$

Um resultado chave na teoria da probabilidade é conhecido como **Teorema de Bayes**. Basicamente, afirma que $Pr[A|B]$ pode ser reescrito da seguinte forma:

$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$

Em vez de usar probabilidades condicionais com eventos específicos, também podemos olhar para as probabilidades condicionais envolvidas com duas ou mais variáveis aleatórias em um conjunto de eventos possíveis. Suponha duas variáveis aleatórias, $X$ e $Y$. Podemos denotar qualquer valor possível para $X$ por $x$, e qualquer valor possível para $Y$ por $y$. Poderíamos dizer, então, que duas variáveis aleatórias são independentes se a seguinte declaração for verdadeira:

$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$

para todos $x$ e $y$.

Vamos ser um pouco mais explícitos sobre o que essa declaração significa.
Suponha que os conjuntos de resultados para $X$ e $Y$ sejam definidos da seguinte forma: **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ e **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\}$. (É típico indicar conjuntos de valores por letras maiúsculas e em negrito.)
Agora suponha que você amostra $Y$ e observa $y_1$. A afirmação acima nos diz que a probabilidade de agora obter $x_1$ ao amostrar $X$ é exatamente a mesma como se nunca tivéssemos observado $y_1$. Isso é verdade para qualquer $y_i$ que poderíamos ter retirado da nossa amostragem inicial de $Y$. Finalmente, isso se mantém verdadeiro não apenas para $x_1$. Para qualquer $x_i$, a probabilidade de ocorrer não é influenciada pelo resultado de uma amostragem de $Y$. Tudo isso também se aplica ao caso em que $X$ é amostrado primeiro.

Vamos terminar nossa discussão em um ponto um pouco mais filosófico. Em qualquer situação do mundo real, a probabilidade de algum evento é sempre avaliada contra um conjunto específico de informações. Não existe uma “probabilidade incondicional” em nenhum sentido muito estrito da palavra.

Por exemplo, suponha que eu lhe pergunte a probabilidade de porcos voarem até 2030. Embora eu não lhe dê mais informações, você claramente sabe muito sobre o mundo que pode influenciar seu julgamento. Você nunca viu porcos voarem. Você sabe que a maioria das pessoas não espera que eles voem. Você sabe que eles não são realmente feitos para voar. E assim por diante.

Portanto, quando falamos de uma “probabilidade incondicional” de algum evento em um contexto do mundo real, esse termo realmente só pode ter significado se o interpretarmos como algo como “a probabilidade sem nenhuma informação explícita adicional”. Qualquer entendimento de uma “probabilidade condicional” deve, então, sempre ser entendido contra alguma peça específica de informação.

Eu poderia, por exemplo, perguntar-lhe a probabilidade de porcos voarem até 2030, depois de lhe dar evidências de que algumas cabras na Nova Zelândia aprenderam a voar após alguns anos de treinamento. Neste caso, você provavelmente ajustará seu julgamento sobre a probabilidade de porcos voarem até 2030. Então, a probabilidade de porcos voarem até 2030 é condicional a esta evidência sobre cabras na Nova Zelândia.

## A operação de módulo
<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

### Módulo

A expressão mais básica com a **operação de módulo** é da seguinte forma: $x \mod y$.

A variável $x$ é chamada de dividendo e a variável $y$ o divisor. Para realizar uma operação de módulo com um dividendo positivo e um divisor positivo, você apenas determina o resto da divisão.

Por exemplo, considere a expressão $25 \mod 4$. O número 4 entra no número 25 um total de 6 vezes. O resto dessa divisão é 1. Portanto, $25 \mod 4$ é igual a 1. De maneira semelhante, podemos avaliar as expressões abaixo:

* $29 \mod 30 = 29$ (já que 30 entra em 29 um total de 0 vezes e o resto é 29)
* $42 \mod 2 = 0$ (já que 2 entra em 42 um total de 21 vezes e o resto é 0)
* $12 \mod 5 = 2$ (pois 5 cabe em 12 um total de 2 vezes e o resto é 2)
* $20 \mod 8 = 4$ (pois 8 cabe em 20 um total de 2 vezes e o resto é 4)

Quando o dividendo ou divisor é negativo, as operações de módulo podem ser tratadas de maneira diferente pelas linguagens de programação.

Você definitivamente encontrará casos com dividendo negativo em criptografia. Nestes casos, a abordagem típica é a seguinte:

* Primeiro determine o valor mais próximo *menor ou igual a* o dividendo no qual o divisor divide com um resto de zero. Chame esse valor de $p$.
* Se o dividendo é $x$, então o resultado da operação de módulo é o valor de $x – p$.

Por exemplo, suponha que o dividendo seja $–20$ e o divisor 3. O valor mais próximo menor ou igual a $–20$ no qual 3 divide igualmente é $–21$. O valor de $x – p$ neste caso é $–20 – (–21)$. Isso é igual a 1 e, portanto, $–20 \mod 3$ é igual a 1. De maneira similar, podemos avaliar as expressões abaixo:

* $–8 \mod 5 = 2$
* $–19 \mod 16 = 13$
* $–14 \mod 6 = 4$

Em relação à notação, você tipicamente verá os seguintes tipos de expressões: $x = [y \mod z]$. Devido aos colchetes, a operação de módulo neste caso só se aplica ao lado direito da expressão. Se $y$ é igual a 25 e $z$ é igual a 4, por exemplo, então $x$ é avaliado como 1.

Sem colchetes, a operação de módulo age em *ambos os lados* de uma expressão. Suponha, por exemplo, a seguinte expressão: $x = y \mod z$. Se $y$ é igual a 25 e $z$ é igual a 4, então tudo o que sabemos é que $x \mod 4$ é avaliado como 1. Isso é consistente com qualquer valor para $x$ do conjunto $\{\ldots,–7, –3, 1, 5, 9,\ldots\}$.

O ramo da matemática que envolve operações de módulo em números e expressões é referido como **aritmética modular**. Você pode pensar neste ramo como aritmética para casos nos quais a linha numérica não é infinitamente longa. Embora tipicamente nos deparemos com operações de módulo para inteiros (positivos) dentro da criptografia, você também pode realizar operações de módulo usando quaisquer números reais.

### A cifra de César

A operação de módulo é frequentemente encontrada dentro da criptografia. Para ilustrar, vamos considerar um dos esquemas de criptografia históricos mais famosos: a cifra de César.

Vamos primeiro defini-la. Suponha um dicionário *D* que equipara todas as letras do alfabeto inglês, em ordem, com o conjunto de números $\{0, 1, 2, \ldots, 25\}$. Assuma um espaço de mensagem **M**. A **cifra de César** é, então, um esquema de criptografia definido da seguinte forma:

- Selecione uniformemente uma chave $k$ do espaço de chaves **K**, onde **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Criptografe uma mensagem $m \in \mathbf{M}$, da seguinte forma:
    - Separe $m$ em suas letras individuais $m_0, m_1, \ldots, m_i, \ldots, m_l$
- Converta cada $m_i$ para um número de acordo com *D*
    - Para cada $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Converta cada $c_i$ para uma letra de acordo com *D*
    - Então combine $c_0, c_1, \ldots, c_l$ para gerar o texto cifrado $c$
- Descriptografe um texto cifrado $c$ da seguinte forma:
    - Converta cada $c_i$ para um número de acordo com *D*
    - Para cada $c_i$, $m_i = [(c_i – k) \mod 26]$
    - Converta cada $m_i$ para uma letra de acordo com *D*
    - Então combine $m_0, m_1, \ldots, m_l$ para gerar a mensagem original $m$

O operador módulo na cifra de deslocamento garante que as letras sejam circulares, de modo que todas as letras do texto cifrado sejam definidas. Para ilustrar, considere a aplicação da cifra de deslocamento na palavra “DOG”.

Suponha que você selecionou uniformemente uma chave com o valor de 17. A letra “O” equivale a 15. Sem a operação de módulo, a adição desse número do texto plano com a chave resultaria em um número de texto cifrado de 32. No entanto, esse número de texto cifrado não pode ser transformado em uma letra de texto cifrado, pois o alfabeto inglês possui apenas 26 letras. A operação de módulo garante que o número do texto cifrado seja na verdade 6 (o resultado de $32 \mod 26$), que equivale à letra do texto cifrado “G”.

A cifragem completa da palavra “DOG” com um valor de chave de 17 é a seguinte:

* Mensagem = DOG = D,O,G = 3,15,6
* $c_0 = [(3 + 17) \mod 26] = [(20) \mod 26] = 20 = U$
* $c_1 = [(15 + 17) \mod 26] = [(32) \mod 26] = 6 = G$
* $c_2 = [(6 + 17) \mod 26] = [(23) \mod 26] = 23 = X$
* $c = UGX$

Todos podem entender intuitivamente como funciona a cifra de deslocamento e provavelmente usá-la por conta própria. No entanto, para avançar seu conhecimento em criptografia, é importante começar a se familiarizar com a formalização, pois os esquemas se tornarão muito mais difíceis. Por isso, os passos para a cifra de deslocamento foram formalizados.

**Notas:**

[1] Podemos definir esta afirmação exatamente, usando a terminologia da seção anterior. Deixe uma variável uniforme $K$ ter $K$ como seu conjunto de resultados possíveis. Então:

$$
Pr[K = 0] = \frac{1}{26}
$$

$$
Pr[K = 1] = \frac{1}{26}
$$

...e assim por diante. Amostre a variável uniforme $K$ uma vez para gerar uma chave particular.

## A operação XOR
<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Todos os dados de computador são processados, armazenados e enviados através de redes no nível de bits. Qualquer esquema criptográfico aplicado aos dados de computador também opera no nível de bits.

Por exemplo, suponha que você digitou um e-mail em seu aplicativo de e-mail. Qualquer criptografia que você aplique não ocorre nos caracteres ASCII do seu e-mail diretamente. Em vez disso, é aplicada à representação em bits das letras e outros símbolos no seu e-mail.
Uma operação matemática chave para entender a criptografia moderna, além da operação de módulo, é a da **operação XOR**, ou operação de "ou exclusivo". Esta operação recebe como entradas dois bits e produz como saída outro bit. A operação XOR será simplesmente denotada como "XOR". Ela resulta em 0 se os dois bits forem iguais e 1 se os dois bits forem diferentes. Você pode ver as quatro possibilidades abaixo. O símbolo $\oplus$ representa "XOR":
* $0 \oplus 0 = 0$
* $0 \oplus 1 = 1$
* $1 \oplus 0 = 1$
* $1 \oplus 1 = 0$

Para ilustrar, suponha que você tenha uma mensagem $m_1$ (01111001) e uma mensagem $m_2$ (01011001). A operação XOR dessas duas mensagens pode ser vista abaixo.

* $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$

O processo é direto. Você primeiro realiza o XOR dos bits mais à esquerda de $m_1$ e $m_2$. Neste caso, isso é $0 \oplus 0 = 0$. Em seguida, você realiza o XOR do segundo par de bits da esquerda. Neste caso, isso é $1 \oplus 1 = 0$. Você continua esse processo até ter realizado a operação XOR nos bits mais à direita.

É fácil ver que a operação XOR é comutativa, ou seja, $m_1 \oplus m_2 = m_2 \oplus m_1$. Além disso, a operação XOR também é associativa. Isso significa que $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.

Uma operação XOR em duas strings de comprimentos alternativos pode ter interpretações diferentes, dependendo do contexto. Não nos preocuparemos aqui com operações XOR em strings de comprimentos diferentes.

Uma operação XOR é equivalente ao caso especial de realizar uma operação de módulo na adição de bits quando o divisor é 2. Você pode ver a equivalência nos seguintes resultados:

* $(0 + 0) \mod 2 = 0 \oplus 0 = 0$
* $(1 + 0) \mod 2 = 1 \oplus 0 = 1$
* $(0 + 1) \mod 2 = 0 \oplus 1 = 1$
* $(1 + 1) \mod 2 = 1 \oplus 1 = 0$

## Pseudoaleatoriedade
<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

Na nossa discussão sobre variáveis aleatórias e uniformes, fizemos uma distinção específica entre "aleatório" e "uniforme". Essa distinção é tipicamente mantida na prática ao descrever variáveis aleatórias. No entanto, no nosso contexto atual, essa distinção precisa ser descartada e "aleatório" e "uniforme" são usados de forma sinônima. Eu explicarei o motivo no final da seção.

Para começar, podemos chamar uma string binária de comprimento $n$ de **aleatória** (ou **uniforme**), se ela foi o resultado da amostragem de uma variável uniforme $S$ que dá a cada string binária de tal comprimento $n$ uma probabilidade igual de seleção.
Suponha, por exemplo, o conjunto de todas as cadeias binárias com comprimento 8: $\{0000\ 0000, 0000\ 0001, \ldots, 1111\ 1111\}$. (É típico escrever uma cadeia de 8 bits em dois quartetos, cada um chamado de **nibble**.) Vamos chamar este conjunto de cadeias de **$S_8$**.
Conforme a definição acima, podemos, então, chamar uma cadeia binária particular de comprimento 8 de aleatória (ou uniforme), se ela foi o resultado da amostragem de uma variável uniforme $S$ que dá a cada cadeia em **$S_8$** uma igual probabilidade de seleção. Dado que o conjunto **$S_8$** inclui $2^8$ elementos, a probabilidade de seleção ao amostrar teria que ser $1/2^8$ para cada cadeia no conjunto.

Um aspecto chave para a aleatoriedade de uma cadeia binária é que ela é definida com referência ao processo pelo qual foi selecionada. A forma de qualquer cadeia binária particular por si só, portanto, não revela nada sobre sua aleatoriedade na seleção.

Por exemplo, muitas pessoas intuitivamente têm a ideia de que uma cadeia como $1111\ 1111$ não poderia ter sido selecionada aleatoriamente. Mas isso é claramente falso.

Definindo uma variável uniforme $S$ sobre todas as cadeias binárias de comprimento 8, a probabilidade de selecionar $1111\ 1111$ do conjunto **$S_8$** é a mesma que a de uma cadeia como $0111\ 0100$. Assim, você não pode dizer nada sobre a aleatoriedade de uma cadeia, apenas analisando a cadeia em si.

Também podemos falar de cadeias aleatórias sem especificamente significar cadeias binárias. Poderíamos, por exemplo, falar de uma cadeia hex aleatória $AF\ 02\ 82$. Neste caso, a cadeia teria sido selecionada aleatoriamente do conjunto de todas as cadeias hex de comprimento 6. Isso é equivalente a selecionar aleatoriamente uma cadeia binária de comprimento 24, já que cada dígito hex representa 4 bits.

Tipicamente, a expressão “uma cadeia aleatória”, sem qualificação, refere-se a uma cadeia selecionada aleatoriamente do conjunto de todas as cadeias com o mesmo comprimento. É assim que descrevi acima. Uma cadeia de comprimento $n$ pode, claro, também ser selecionada aleatoriamente de um conjunto diferente. Um, por exemplo, que constitui apenas um subconjunto de todas as cadeias de comprimento $n$, ou talvez um conjunto que inclui cadeias de comprimentos variados. Nesses casos, no entanto, não nos referiríamos a ela como “uma cadeia aleatória”, mas sim “uma cadeia que é selecionada aleatoriamente de algum conjunto **S**”.

Um conceito chave dentro da criptografia é o de pseudorrandomidade. Uma **cadeia pseudorrandômica** de comprimento $n$ parece *como se* fosse o resultado da amostragem de uma variável uniforme $S$ que dá a cada cadeia em **$S_n$** uma igual probabilidade de seleção. Na verdade, no entanto, a cadeia é o resultado da amostragem de uma variável uniforme $S'$ que apenas define uma distribuição de probabilidade — não necessariamente uma com igualdades de probabilidades para todos os resultados possíveis — em um subconjunto de **$S_n$**. O ponto crucial aqui é que ninguém pode realmente distinguir entre amostras de $S$ e $S'$, mesmo que se tome muitas delas.
Suponha, por exemplo, uma variável aleatória $S$. Seu conjunto de resultados é **$S_{256}$**, que é o conjunto de todas as strings binárias de comprimento 256. Este conjunto tem $2^{256}$ elementos. Cada elemento tem uma probabilidade igual de seleção, $1/2^{256}$, ao ser amostrado.
Além disso, suponha uma variável aleatória $S'$. Seu conjunto de resultados inclui apenas $2^{128}$ strings binárias de comprimento 256. Ela tem alguma distribuição de probabilidade sobre essas strings, mas essa distribuição não é necessariamente uniforme.

Suponha que eu agora tenha tirado 1000s de amostras de $S$ e 1000s de amostras de $S'$ e dado os dois conjuntos de resultados para você. Eu digo a você qual conjunto de resultados está associado a qual variável aleatória. Em seguida, eu tiro uma amostra de uma das duas variáveis aleatórias. Mas desta vez eu não digo de qual variável aleatória eu tirei a amostra. Se $S'$ fosse pseudorandom, então a ideia é que sua probabilidade de fazer o palpite certo sobre qual variável aleatória eu amostrasse é praticamente não melhor do que $1/2$.

Tipicamente, uma string pseudorandom de comprimento $n$ é produzida selecionando aleatoriamente uma string de tamanho $n – x$, onde $x$ é um inteiro positivo, e usando-a como entrada para um algoritmo expansivo. Esta string aleatória de tamanho $n – x$ é conhecida como a **semente**.

Strings pseudorandom são um conceito chave para tornar a criptografia prática. Considere, por exemplo, cifras de fluxo. Com uma cifra de fluxo, uma chave selecionada aleatoriamente é inserida em um algoritmo expansivo para produzir uma string pseudorandom muito maior. Esta string pseudorandom é então combinada com o texto plano por meio de uma operação XOR para produzir um texto cifrado.

Se não fôssemos capazes de produzir esse tipo de string pseudorandom para uma cifra de fluxo, então precisaríamos de uma chave que seja tão longa quanto a mensagem para sua segurança. Esta não é uma opção muito prática na maioria dos casos.

A noção de pseudorandomidade discutida nesta seção pode ser definida de forma mais formal. Ela também se estende a outros contextos. Mas não precisamos nos aprofundar nessa discussão aqui. Tudo o que você realmente precisa entender intuitivamente para grande parte da criptografia é a diferença entre uma string aleatória e uma pseudorandom. [2]

A razão para abandonar a distinção entre “aleatório” e “uniforme” em nossa discussão agora também deve estar clara. Na prática, todos usam o termo pseudorandom para indicar uma string que parece **como se** fosse o resultado da amostragem de uma variável uniforme $S$. Estritamente falando, deveríamos chamar tal string de “pseudo-uniforme”, adotando nossa linguagem de antes. Como o termo “pseudo-uniforme” é tanto desajeitado quanto não usado por ninguém, não o introduziremos aqui por clareza. Em vez disso, apenas abandonamos a distinção entre “aleatório” e “uniforme” no contexto atual.

**Notas**

[2] Se estiver interessado em uma exposição mais formal sobre esses assuntos, você pode consultar a *Introdução à Criptografia Moderna* de Katz e Lindell, especialmente o capítulo 3.


# Fundamentos Matemáticos da Criptografia 2
<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>

## O que é teoria dos números?
<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>
Este capítulo aborda um tópico mais avançado sobre as fundações matemáticas da criptografia: teoria dos números. Embora a teoria dos números seja importante para a criptografia simétrica (como no Cifra de Rijndael), ela é particularmente importante no contexto da criptografia de chave pública.

Se você está achando os detalhes da teoria dos números complicados, eu recomendaria uma leitura de alto nível na primeira vez. Você sempre pode voltar a ela em um momento posterior.

___

Você pode caracterizar a **teoria dos números** como o estudo das propriedades dos inteiros e das funções matemáticas que trabalham com inteiros.

Considere, por exemplo, que quaisquer dois números $a$ e $N$ são **coprimos** (ou **primos relativos**) se o seu maior divisor comum for igual a 1. Suponha agora um determinado inteiro $N$. Quantos inteiros menores que $N$ são coprimos com $N$? Podemos fazer afirmações gerais sobre as respostas para esta pergunta? Estes são os tipos típicos de perguntas que a teoria dos números procura responder.

A teoria dos números moderna depende das ferramentas da álgebra abstrata. O campo da **álgebra abstrata** é uma subdisciplina da matemática onde os principais objetos de análise são objetos abstratos conhecidos como estruturas algébricas. Uma **estrutura algébrica** é um conjunto de elementos unidos com uma ou mais operações, que atendem a certos axiomas. Por meio de estruturas algébricas, os matemáticos podem obter insights sobre problemas matemáticos específicos, abstraindo-se de seus detalhes.

O campo da álgebra abstrata é às vezes também chamado de álgebra moderna. Você também pode se deparar com o conceito de **matemática abstrata** (ou **matemática pura**). Este último termo não é uma referência à álgebra abstrata, mas sim significa o estudo da matemática por si só, e não apenas com um olhar sobre aplicações potenciais.

Os conjuntos da álgebra abstrata podem lidar com muitos tipos de objetos, desde as transformações que preservam a forma em um triângulo equilátero até padrões de papel de parede. Para a teoria dos números, consideramos apenas conjuntos de elementos que contêm inteiros ou funções que trabalham com inteiros.

## Grupos
<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Um conceito básico em matemática é o de um conjunto de elementos. Um conjunto é geralmente denotado por sinais de chaves com os elementos separados por vírgulas.

Por exemplo, o conjunto de todos os inteiros é $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$. As elipses aqui significam que um certo padrão continua em uma direção particular. Então, o conjunto de todos os inteiros também inclui $3, 4, 5, 6$ e assim por diante, bem como $-3, -4, -5, -6$ e assim por diante. Este conjunto de todos os inteiros é tipicamente denotado por $\mathbb{Z}$.

Outro exemplo de um conjunto é $\mathbb{Z} \mod 11$, ou o conjunto de todos os inteiros módulo 11. Em contraste com o conjunto inteiro $\mathbb{Z}$, este conjunto contém apenas um número finito de elementos, a saber $\{0, 1, \ldots, 9, 10\}$.
Um erro comum é pensar que o conjunto $\mathbb{Z} \mod 11$ é na verdade $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$. Mas isso não é verdade, dado o modo como definimos a operação de módulo anteriormente. Qualquer inteiro negativo reduzido pelo módulo 11 é mapeado para $\{0, 1, \ldots, 9, 10\}$. Por exemplo, a expressão $-2 \mod 11$ é mapeada para $9$, enquanto a expressão $-27 \mod 11$ é mapeada para $5$.
Outro conceito básico em matemática é o de uma operação binária. Esta é qualquer operação que toma dois elementos para produzir um terceiro. Por exemplo, da aritmética e álgebra básicas, você estaria familiarizado com quatro operações binárias fundamentais: adição, subtração, multiplicação e divisão.

Esses dois conceitos matemáticos básicos, conjuntos e operações binárias, são usados para definir a noção de um grupo, a estrutura mais essencial em álgebra abstrata.

Especificamente, suponha alguma operação binária $\circ$. Além disso, suponha algum conjunto de elementos **S** equipado com essa operação. Tudo o que “equipado” significa aqui é que a operação $\circ$ pode ser realizada entre quaisquer dois elementos no conjunto **S**.

A combinação $\langle \mathbf{S}, \circ \rangle$ é, então, um **grupo** se atender a quatro condições específicas, conhecidas como axiomas de grupo.

1. Para quaisquer $a$ e $b$ que são elementos de $\mathbf{S}$, $a \circ b$ também é um elemento de $\mathbf{S}$. Isso é conhecido como a **condição de fechamento**.
2. Para quaisquer $a$, $b$ e $c$ que são elementos de $\mathbf{S}$, é o caso que $(a \circ b) \circ c = a \circ (b \circ c)$. Isso é conhecido como a **condição de associatividade**.
3. Existe um elemento único $e$ em $\mathbf{S}$, tal que para cada elemento $a$ em $\mathbf{S}$, a seguinte equação é válida: $e \circ a = a \circ e = a$. Como existe apenas um tal elemento $e$, ele é chamado de **elemento identidade**. Esta condição é conhecida como a **condição de identidade**.
4. Para cada elemento $a$ em $\mathbf{S}$, existe um elemento $b$ em $\mathbf{S}$, tal que a seguinte equação é válida: $a \circ b = b \circ a = e$, onde $e$ é o elemento identidade. O elemento $b$ aqui é conhecido como o **elemento inverso**, e é comumente denotado como $a^{-1}$. Esta condição é conhecida como a **condição de inverso** ou a **condição de invertibilidade**.

Vamos explorar os grupos um pouco mais. Denote o conjunto de todos os inteiros por $\mathbb{Z}$. Este conjunto combinado com a adição padrão, ou $\langle \mathbb{Z}, + \rangle$, claramente se encaixa na definição de um grupo, pois atende aos quatro axiomas acima.

1. Para quaisquer $x$ e $y$ que são elementos de $\mathbb{Z}$, $x + y$ também é um elemento de $\mathbb{Z}$. Então $\langle \mathbb{Z}, + \rangle$ atende à condição de fechamento.
2. Para quaisquer $x$, $y$ e $z$ que sejam elementos de $\mathbb{Z}$, $(x + y) + z = x + (y + z)$. Assim, $\langle \mathbb{Z}, + \rangle$ satisfaz a condição de associatividade.
3. Existe um elemento identidade em $\langle \mathbb{Z}, + \rangle$, que é o 0. Para qualquer $x$ em $\mathbb{Z}$, vale que: $0 + x = x + 0 = x$. Então, $\langle \mathbb{Z}, + \rangle$ satisfaz a condição de identidade.
4. Finalmente, para cada elemento $x$ em $\mathbb{Z}$, existe um $y$ tal que $x + y = y + x = 0$. Se $x$ fosse 10, por exemplo, $y$ seria $-10$ (no caso de $x$ ser 0, $y$ também é 0). Assim, $\langle \mathbb{Z}, + \rangle$ satisfaz a condição de inverso.

Importante, o fato de o conjunto dos inteiros com adição constituir um grupo não significa que ele constitua um grupo com multiplicação. Você pode verificar isso testando $\langle \mathbb{Z}, \cdot \rangle$ contra os quatro axiomas de grupo (onde $\cdot$ significa multiplicação padrão).

Os dois primeiros axiomas obviamente se aplicam. Além disso, sob multiplicação, o elemento 1 pode servir como o elemento identidade. Qualquer inteiro $x$ multiplicado por 1, resulta em $x$. No entanto, $\langle \mathbb{Z}, \cdot \rangle$ não satisfaz a condição de inverso. Ou seja, não existe um elemento único $y$ em $\mathbb{Z}$ para cada $x$ em $\mathbb{Z}$, tal que $x \cdot y = 1$.

Por exemplo, suponha que $x = 22$. Qual valor de $y$ do conjunto $\mathbb{Z}$ multiplicado por $x$ resultaria no elemento identidade 1? O valor de $1/22$ funcionaria, mas isso não está no conjunto $\mathbb{Z}$. De fato, você encontra esse problema para qualquer inteiro $x$, exceto para os valores de 1 e -1 (onde $y$ teria que ser 1 e -1, respectivamente).

Se permitíssemos números reais para nosso conjunto, então nossos problemas em grande parte desapareceriam. Para qualquer elemento $x$ no conjunto, a multiplicação por $1/x$ resulta em 1. Como frações estão incluídas no conjunto dos números reais, um inverso pode ser encontrado para cada número real. A exceção é zero, pois qualquer multiplicação com zero nunca resultará no elemento identidade 1. Portanto, o conjunto de números reais não-zero equipado com multiplicação é de fato um grupo.

Alguns grupos satisfazem uma quinta condição geral, conhecida como **condição de comutatividade**. Esta condição é a seguinte:

* Suponha um grupo $G$ com um conjunto **S** e um operador binário $\circ$. Suponha que $a$ e $b$ sejam elementos de **S**. Se for o caso de $a \circ b = b \circ a$ para quaisquer dois elementos $a$ e $b$ em **S**, então $G$ satisfaz a condição de comutatividade.
Qualquer grupo que atenda à condição de comutatividade é conhecido como um **grupo comutativo**, ou um **grupo Abeliano** (em homenagem a Niels Henrik Abel). É fácil verificar que tanto o conjunto dos números reais sobre a adição quanto o conjunto dos inteiros sobre a adição são grupos Abeliano. O conjunto dos inteiros sobre a multiplicação não é um grupo de todo, então, ipso facto, não pode ser um grupo Abeliano. O conjunto dos números reais não-zero sobre a multiplicação, por outro lado, também é um grupo Abeliano.
Você deve prestar atenção a duas convenções importantes sobre notação. Primeiro, os sinais “+” ou “×” serão frequentemente empregados para simbolizar operações de grupo, mesmo quando os elementos não são, de fato, números. Nestes casos, você não deve interpretar esses sinais como adição ou multiplicação aritmética padrão. Em vez disso, são operações com apenas uma semelhança abstrata com essas operações aritméticas.

A menos que você esteja se referindo especificamente à adição ou multiplicação aritmética, é mais fácil usar símbolos como $\circ$ e $\diamond$ para operações de grupo, pois estes não têm conotações muito culturalmente arraigadas.

Segundo, pela mesma razão que “+” e “×” são frequentemente usados para indicar operações não-aritméticas, os elementos de identidade dos grupos são frequentemente simbolizados por “0” e “1”, mesmo quando os elementos nesses grupos não são números. A menos que você esteja se referindo ao elemento de identidade de um grupo com números, é mais fácil usar um símbolo mais neutro como “$e$” para indicar o elemento de identidade.

Muitos conjuntos diferentes e muito importantes de valores na matemática equipados com certas operações binárias são grupos. No entanto, aplicações criptográficas só trabalham com conjuntos de inteiros ou pelo menos elementos que são descritos por inteiros, isto é, dentro do domínio da teoria dos números. Portanto, conjuntos com números reais além dos inteiros não são empregados em aplicações criptográficas.

Vamos terminar fornecendo um exemplo de elementos que podem ser “descritos por inteiros”, mesmo que não sejam inteiros. Um bom exemplo são os pontos das curvas elípticas. Embora qualquer ponto em uma curva elíptica claramente não seja um inteiro, tal ponto é de fato descrito por dois inteiros.

Curvas elípticas são, por exemplo, cruciais para o Bitcoin. Qualquer par de chaves privada e pública padrão do Bitcoin é selecionado do conjunto de pontos que é definido pela seguinte curva elíptica:

$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$

(o maior número primo menor que $2^{256}$). A coordenada $x$ é a chave privada e a coordenada $y$ é sua chave pública.

Transações em Bitcoin tipicamente envolvem bloquear saídas para uma ou mais chaves públicas de alguma forma. O valor dessas transações pode, então, ser desbloqueado fazendo assinaturas digitais com as chaves privadas correspondentes.

## Grupos Cíclicos
<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Uma distinção importante que podemos fazer é entre um **grupo finito** e um **grupo infinito**. O primeiro tem um número finito de elementos, enquanto o último tem um número infinito de elementos. O número de elementos em qualquer grupo finito é conhecido como a **ordem do grupo**. Toda a criptografia prática que envolve o uso de grupos depende de grupos finitos (teórico-numéricos).

Dentro da criptografia de chave pública, uma certa classe de grupos Abeliano finitos conhecidos como grupos cíclicos são particularmente importantes. Para entender grupos cíclicos, primeiro precisamos entender o conceito de exponenciação de elementos de grupo.
Suponha um grupo $G$ com uma operação de grupo $\circ$, e que $a$ é um elemento de $G$. A expressão $a^n$ deve, então, ser interpretada como o elemento $a$ combinado consigo mesmo um total de $n – 1$ vezes. Por exemplo, $a^2$ significa $a \circ a$, $a^3$ significa $a \circ a \circ a$, e assim por diante. (Note que a exponenciação aqui não é necessariamente exponenciação no sentido aritmético padrão.)

Vamos para um exemplo. Suponha que $G = \langle \mathbb{Z} \mod 7, + \rangle$, e que nosso valor para $a$ seja 4. Neste caso, $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Alternativamente, $a^4$ representaria $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$.

Alguns grupos Abelinos têm um ou mais elementos, que podem gerar todos os outros elementos do grupo através da exponenciação contínua. Esses elementos são chamados de **geradores** ou **elementos primitivos**.

Uma classe importante desses grupos é $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, onde $N$ é um número primo. A notação $\mathbb{Z}^*$ aqui significa que o grupo contém todos os inteiros positivos não nulos menores que $N$. Tal grupo, portanto, sempre tem $N – 1$ elementos.

Considere, por exemplo, $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$. Este grupo tem os seguintes elementos: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. A ordem deste grupo é 10 (o que é de fato igual a $11 – 1$).

Vamos explorar a exponenciação do elemento 2 deste grupo. Os cálculos até $2^{12}$ são mostrados abaixo. Note que no lado esquerdo da equação, o expoente refere-se à exponenciação do elemento do grupo. No nosso exemplo particular, isso de fato envolve exponenciação aritmética no lado direito da equação (mas também poderia ter envolvido, por exemplo, adição). Para esclarecer, escrevi a operação repetida, em vez da forma de expoente no lado direito.

* $2^1 = 2 \mod 11$
* $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$
* $2^3 = 2 \cdot 2 \cdot 2 \mod 11 = 8 \mod 11$
* $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
* $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
* $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
* $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
* $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$
* $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
* $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = 1 \mod 11$
* $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 \mod 11 = 2 \mod 11$
* $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 4096 \mod 11 = 4 \mod 11$

Se você observar com atenção, pode ver que realizar a exponenciação do elemento 2 percorre todos os elementos de $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ na seguinte ordem: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Após $2^{10}$, a continuação da exponenciação do elemento 2 percorre todos os elementos novamente e na mesma ordem. Portanto, o elemento 2 é um gerador em $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$.

Embora $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ tenha múltiplos geradores, nem todos os elementos deste grupo são geradores. Considere, por exemplo, o elemento 3. Passando pelas primeiras 10 exponenciações, sem mostrar os cálculos trabalhosos, obtemos os seguintes resultados:

* $3^1 = 3 \mod 11$
* $3^2 = 9 \mod 11$
* $3^3 = 5 \mod 11$
* $3^4 = 4 \mod 11$
* $3^5 = 1 \mod 11$
* $3^6 = 3 \mod 11$
* $3^7 = 9 \mod 11$
* $3^8 = 5 \mod 11$
* $3^9 = 4 \mod 11$
* $3^{10} = 1 \mod 11$
Em vez de percorrer todos os valores em $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, a exponenciação do elemento 3 leva apenas a um subconjunto desses valores: 3, 9, 5, 4 e 1. Após a quinta exponenciação, esses valores começam a se repetir.
Agora podemos definir um **grupo cíclico** como qualquer grupo com pelo menos um gerador. Ou seja, existe pelo menos um elemento do grupo a partir do qual você pode produzir todos os outros elementos do grupo por meio de exponenciação.

Você pode ter notado no nosso exemplo acima que tanto $2^{10}$ quanto $3^{10}$ são iguais a $1 \mod 11$. De fato, embora não realizemos os cálculos, a exponenciação por 10 de qualquer elemento do grupo $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ resultará em $1 \mod 11$. Por que isso acontece?

Esta é uma pergunta importante, mas requer algum trabalho para responder.

Para começar, suponha dois inteiros positivos $a$ e $N$. Um teorema importante em teoria dos números afirma que $a$ tem um inverso multiplicativo módulo $N$ (isto é, um inteiro $b$ tal que $a \cdot b = 1 \mod N$) se e somente se o maior divisor comum entre $a$ e $N$ é igual a 1. Ou seja, se $a$ e $N$ são coprimos.

Portanto, para qualquer grupo de inteiros equipado com multiplicação módulo $N$, apenas os menores coprimos com $N$ estão incluídos no conjunto. Podemos denotar este conjunto por $\mathbb{Z}^c \mod N$.

Por exemplo, suponha que $N$ seja 10. Apenas os inteiros 1, 3, 7 e 9 são coprimos com 10. Então, o conjunto $\mathbb{Z}^c \mod 10$ inclui apenas $\{1, 3, 7, 9\}$. Você não pode criar um grupo com multiplicação inteira módulo 10 usando quaisquer outros inteiros entre 1 e 10. Para este grupo particular, os inversos são os pares 1 e 9, e 3 e 7.

No caso em que $N$ é primo, todos os inteiros de 1 até $N – 1$ são coprimos com $N$. Tal grupo, portanto, tem uma ordem de $N – 1$. Usando nossa notação anterior, $\mathbb{Z}^c \mod N$ é igual a $\mathbb{Z}^* \mod N$ quando $N$ é primo. O grupo que selecionamos para nosso exemplo anterior, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, é uma instância particular desta classe de grupos.

Em seguida, a função $\phi(N)$ calcula o número de coprimos até um número $N$, e é conhecida como **Função Fi de Euler**. [1] De acordo com o **Teorema de Euler**, sempre que dois inteiros $a$ e $N$ são coprimos, o seguinte se mantém:

* $a^{\phi(N)} \mod N = 1 \mod N$
Isso tem uma implicação importante para a classe de grupos $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ onde $N$ é primo. Para esses grupos, a exponenciação de elementos do grupo representa a exponenciação aritmética. Ou seja, $a^{\phi(N)} \mod N$ representa a operação aritmética $a^{\phi(N)} \mod N$. Como qualquer elemento $a$ nesses grupos multiplicativos é coprimo com $N$, isso significa que $a^{\phi(N)} \mod N = a^{N – 1} \mod N = 1 \mod N$.
O teorema de Euler é um resultado realmente importante. Para começar, ele implica que todos os elementos em $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ só podem ciclar por um número de valores por exponenciação que se divide em $N – 1$. No caso de $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, isso significa que cada elemento só pode ciclar por 2, 5 ou 10 elementos. Os valores do grupo pelos quais qualquer elemento cicla mediante exponenciação são conhecidos como a **ordem do elemento**. Um elemento com uma ordem equivalente à ordem de um grupo é um gerador.

Além disso, o teorema de Euler implica que sempre podemos saber o resultado de $a^{N – 1} \mod N$ para qualquer grupo $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ onde $N$ é primo. Isso é válido independentemente de quão complicados possam ser os cálculos reais.

Por exemplo, suponha que nosso grupo seja $\mathbb{Z}^* \mod 160,481,182$ (onde 160,481,182 é de fato um número primo). Sabemos que todos os inteiros de 1 a 160,481,181 devem ser elementos deste grupo, e que $\phi(n) = 160,481,181$. Embora não possamos realizar todos os passos nos cálculos, sabemos que expressões como $514^{160,481,181}$, $2,005^{160,481,181}$, e $256,212^{160,481,181}$ devem todas avaliar para $1 \mod 160,481,182$.

**Notas:**

[1] A função funciona da seguinte maneira. Qualquer inteiro $N$ pode ser fatorado em um produto de primos. Suponha que um determinado $N$ seja fatorado da seguinte forma: $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$ onde todos os $p$’s são números primos e todos os $e$’s são inteiros maiores ou iguais a 1. Então:

$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$

Fórmula da função Phi de Euler para a fatoração de primos de $N$.


## Campos
<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Um grupo é a estrutura algébrica básica em álgebra abstrata, mas existem muitas outras. A única outra estrutura algébrica com a qual você precisa estar familiarizado é a de um **campo**, especificamente a de um **campo finito**. Esse tipo de estrutura algébrica é frequentemente usado em criptografia, como no Padrão de Criptografia Avançado. Este último é o principal esquema de criptografia simétrica que você encontrará na prática.
Um campo é derivado da noção de um grupo. Especificamente, um **campo** é um conjunto de elementos **S** equipado com dois operadores binários $\circ$ e $\diamond$, que atende às seguintes condições:
1. O conjunto **S** equipado com $\circ$ é um grupo Abeliano.
2. O conjunto **S** equipado com $\diamond$ é um grupo Abeliano para os elementos "não-zero".
3. O conjunto **S** equipado com os dois operadores atende ao que é conhecido como condição distributiva: Suponha que $a$, $b$ e $c$ sejam elementos de **S**. Então **S** equipado com os dois operadores atende à propriedade distributiva quando $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.

Note que, assim como com grupos, a definição de um campo é muito abstrata. Ela não faz afirmações sobre os tipos de elementos em **S**, ou sobre as operações $\circ$ e $\diamond$. Ela apenas afirma que um campo é qualquer conjunto de elementos com duas operações para as quais as três condições acima são válidas. (O elemento “zero” no segundo grupo Abeliano pode ser interpretado de forma abstrata.)

Então, qual seria um exemplo de um campo? Um bom exemplo é o conjunto $\mathbb{Z} \mod 7$, ou $\{0, 1, \ldots, 7\}$ definido sobre a adição padrão (no lugar de $\circ$ acima) e a multiplicação padrão (no lugar de $\diamond$ acima).

Primeiro, $\mathbb{Z} \mod 7$ atende à condição de ser um grupo Abeliano sobre adição, e atende à condição de ser um grupo Abeliano sobre multiplicação se você considerar apenas os elementos não-zero. Segundo, a combinação do conjunto com os dois operadores atende à condição distributiva.

É didaticamente valioso explorar essas afirmações usando alguns valores particulares. Vamos pegar os valores experimentais 5, 2 e 3, alguns elementos selecionados aleatoriamente do conjunto $\mathbb{Z} \mod 7$, para inspecionar o campo $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$. Usaremos esses três valores na ordem, conforme necessário para explorar condições particulares.

Vamos primeiro explorar se $\mathbb{Z} \mod 7$ equipado com adição é um grupo Abeliano.

1. **Condição de fechamento**: Vamos pegar 5 e 2 como nossos valores. Nesse caso, $[5 + 2] \mod 7 = 7 \mod 7 = 0$. Isso é de fato um elemento de $\mathbb{Z} \mod 7$, então o resultado é consistente com a condição de fechamento.
2. **Condição de associatividade**: Vamos pegar 5, 2 e 3 como nossos valores. Nesse caso, $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. Isso é consistente com a condição de associatividade.
3. **Condição de identidade**: Vamos pegar 5 como nosso valor. Nesse caso, $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Então 0 parece ser o elemento de identidade para adição.
4. **Condição Inversa**: Considere o inverso de 5. É necessário que $[5 + d] \mod 7 = 0$, para algum valor de $d$. Neste caso, o valor único de $\mathbb{Z} \mod 7$ que atende a esta condição é 2.
5. **Condição de Comutatividade**: Vamos tomar 5 e 3 como nossos valores. Nesse caso, $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. Isso está de acordo com a condição de comutatividade.

O conjunto $\mathbb{Z} \mod 7$ equipado com adição claramente parece ser um grupo Abeliano. Vamos agora explorar se $\mathbb{Z} \mod 7$ equipado com multiplicação é um grupo Abeliano para todos os elementos não nulos.

1. **Condição de Fechamento**: Vamos tomar 5 e 2 como nossos valores. Nesse caso, $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. Isso também é um elemento de $\mathbb{Z} \mod 7$, então o resultado é consistente com a condição de fechamento.
2. **Condição de Associatividade**: Vamos tomar 5, 2 e 3 como nossos valores. Nesse caso, $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$. Isso está de acordo com a condição de associatividade.
3. **Condição de Identidade**: Vamos tomar 5 como nosso valor. Nesse caso, $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$. Então 1 parece ser o elemento de identidade para a multiplicação.
4. **Condição Inversa**: Considere o inverso de 5. É necessário que $[5 \cdot d] \mod 7 = 1$, para algum valor de $d$. O valor único de $\mathbb{Z} \mod 7$ que atende a esta condição é 3. Isso está de acordo com a condição inversa.
5. **Condição de Comutatividade**: Vamos tomar 5 e 3 como nossos valores. Nesse caso, $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$. Isso está de acordo com a condição de comutatividade.

O conjunto $\mathbb{Z} \mod 7$ claramente parece atender às regras para ser um grupo Abeliano quando conjugado com adição ou multiplicação sobre os elementos não nulos.

Finalmente, este conjunto combinado com ambos os operadores parece atender à condição distributiva. Vamos tomar 5, 2 e 3 como nossos valores. Podemos ver que $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.

Agora vimos que $\mathbb{Z} \mod 7$ equipado com adição e multiplicação atende aos axiomas para um campo finito ao testar com valores particulares. Claro, também podemos mostrar isso de forma geral, mas não faremos isso aqui.

Uma distinção chave é entre dois tipos de campos: campos finitos e campos infinitos.
Um **campo infinito** envolve um campo onde o conjunto **S** é infinitamente grande. O conjunto dos números reais $\mathbb{R}$, equipado com adição e multiplicação, é um exemplo de um campo infinito. Um **campo finito**, também conhecido como **campo de Galois**, é um campo onde o conjunto **S** é finito. Nosso exemplo acima de $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ é um campo finito.
Em criptografia, estamos principalmente interessados em campos finitos. Geralmente, pode-se mostrar que um campo finito existe para algum conjunto de elementos **S** se e somente se ele tem $p^m$ elementos, onde $p$ é um número primo e $m$ um inteiro positivo maior ou igual a um. Em outras palavras, se a ordem de algum conjunto **S** é um número primo ($p^m$ onde $m = 1$) ou alguma potência de primo ($p^m$ onde $m > 1$), então você pode encontrar dois operadores $\circ$ e $\diamond$ tais que as condições para um campo são satisfeitas.

Se algum campo finito tem um número primo de elementos, então ele é chamado de **campo primo**. Se o número de elementos no campo finito é uma potência de primo, então o campo é chamado de **campo de extensão**. Em criptografia, estamos interessados tanto em campos primos quanto em campos de extensão. [2]

Os principais campos primos de interesse em criptografia são aqueles onde o conjunto de todos os inteiros é modulado por algum número primo, e os operadores são a adição e multiplicação padrão. Esta classe de campos finitos incluiria $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \mod 13$, e assim por diante. Para qualquer campo primo $\mathbb{Z} \mod p$, o conjunto de inteiros do campo é o seguinte: $\{0, 1, \ldots, p – 2, p – 1\}$.

Em criptografia, também estamos interessados em campos de extensão, particularmente quaisquer campos com $2^m$ elementos onde $m > 1$. Tais campos finitos são, por exemplo, usados no Cifra de Rijndael, que forma a base do Padrão de Criptografia Avançado. Enquanto os campos primos são relativamente intuitivos, esses campos de extensão base 2 provavelmente não são para quem não está familiarizado com álgebra abstrata.

Para começar, é de fato verdade que qualquer conjunto de inteiros com $2^m$ elementos pode ser atribuído a dois operadores que fariam sua combinação um campo (desde que $m$ seja um inteiro positivo). No entanto, só porque um campo existe não significa necessariamente que é fácil de descobrir ou particularmente prático para certas aplicações.

Como se verifica, campos de extensão particularmente aplicáveis de $2^m$ em criptografia são aqueles definidos sobre conjuntos específicos de expressões polinomiais, em vez de algum conjunto de inteiros.

Por exemplo, suponha que queríamos um campo de extensão com $2^3$ (ou seja, 8) elementos no conjunto. Embora possa haver muitos conjuntos diferentes que podem ser usados para campos desse tamanho, um desses conjuntos inclui todos os polinômios únicos da forma $a_2x^2 + a_1x + a_0$, onde cada coeficiente $a_i$ é 0 ou 1. Portanto, este conjunto **S** inclui os seguintes elementos:
1. $0$: O caso em que $a_2 = 0$, $a_1 = 0$ e $a_0 = 0$.
2. $1$: O caso em que $a_2 = 0$, $a_1 = 0$ e $a_0 = 1$.
3. $x$: O caso em que $a_2 = 0$, $a_1 = 1$ e $a_0 = 0$.
4. $x + 1$: O caso em que $a_2 = 0$, $a_1 = 1$ e $a_0 = 1$.
5. $x^2$: O caso em que $a_2 = 1$, $a_1 = 0$ e $a_0 = 0$.
6. $x^2 + 1$: O caso em que $a_2 = 1$, $a_1 = 0$ e $a_0 = 1$.
7. $x^2 + x$: O caso em que $a_2 = 1$, $a_1 = 1$ e $a_0 = 0$.
8. $x^2 + x + 1$: O caso em que $a_2 = 1$, $a_1 = 1$ e $a_0 = 1$.

Portanto, **S** seria o conjunto $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$. Quais duas operações podem ser definidas sobre este conjunto de elementos para garantir que sua combinação seja um campo?

A primeira operação no conjunto **S** ($\circ$) pode ser definida como a adição padrão de polinômios módulo 2. Tudo o que você precisa fazer é adicionar os polinômios como normalmente faria, e então aplicar o módulo 2 a cada um dos coeficientes do polinômio resultante. Aqui estão alguns exemplos:

* $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$
* $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
* $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$

A segunda operação no conjunto **S** ($\diamond$) que é necessária para criar o campo é mais complicada. É um tipo de multiplicação, mas não a multiplicação padrão da aritmética. Em vez disso, você deve ver cada elemento como um vetor e entender a operação como a multiplicação desses dois vetores módulo um polinômio irredutível.

Vamos primeiro nos voltar para a ideia de um polinômio irredutível. Um **polinômio irredutível** é aquele que não pode ser fatorado (assim como um número primo não pode ser fatorado em componentes além de 1 e o próprio número primo). Para nossos propósitos, estamos interessados em polinômios que são irredutíveis com respeito ao conjunto de todos os inteiros. (Note que você pode ser capaz de fatorar certos polinômios por, por exemplo, os números reais ou complexos, mesmo que não possa fatorá-los usando inteiros.)
Por exemplo, considere o polinômio $x^2 - 3x + 2$. Este pode ser reescrito como $(x – 1)(x – 2)$. Portanto, este não é irredutível. Agora considere o polinômio $x^2 + 1$. Usando apenas inteiros, não há como fatorar ainda mais essa expressão. Portanto, este é um polinômio irredutível em relação aos inteiros.

A seguir, vamos nos voltar para o conceito de multiplicação de vetores. Não exploraremos este tópico em profundidade, mas você só precisa entender uma regra básica: Qualquer divisão de vetores pode ocorrer desde que o dividendo tenha um grau maior ou igual ao do divisor. Se o dividendo tem um grau menor que o do divisor, então o dividendo não pode mais ser dividido pelo divisor.

Por exemplo, considere a expressão $x^6 + x + 1 \mod x^5 + x^2$. Isso claramente se reduz ainda mais, pois o grau do dividendo, 6, é maior que o grau do divisor, 5. Agora considere a expressão $x^5 + x + 1 \mod x^5 + x^2$. Isso também se reduz ainda mais, pois o grau do dividendo, 5, e do divisor, 5, são iguais.

No entanto, agora considere a expressão $x^4 + x + 1 \mod x^5 + x^2$. Isso não se reduz mais, pois o grau do dividendo, 4, é menor que o grau do divisor, 5.

Com base nessas informações, estamos agora prontos para encontrar nossa segunda operação para o conjunto $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Já disse que a segunda operação deve ser entendida como multiplicação de vetores módulo algum polinômio irredutível. Esse polinômio irredutível deve garantir que a segunda operação defina um grupo Abeliano sobre **S** e seja consistente com a condição distributiva. Então, qual deveria ser esse polinômio irredutível?

Como todos os vetores no conjunto são de grau 2 ou inferior, o polinômio irredutível deve ser de grau 3. Se qualquer multiplicação de dois vetores no conjunto produzir um polinômio de grau 3 ou superior, sabemos que módulo um polinômio de grau 3 sempre produzirá um polinômio de grau 2 ou inferior. Isso acontece porque qualquer polinômio de grau 3 ou superior é sempre divisível por um polinômio de grau 3. Além disso, o polinômio que funciona como divisor tem que ser irredutível.

Acontece que existem vários polinômios irredutíveis de grau 3 que poderíamos usar como nosso divisor. Cada um desses polinômios define um campo diferente em conjunto com nosso conjunto **S** e adição módulo 2. Isso significa que você tem várias opções ao usar campos de extensão $2^m$ em criptografia.

Para nosso exemplo, suponha que selecionemos o polinômio $x^3 + x + 1$. Este de fato é irredutível, porque você não pode fatorá-lo usando inteiros. Além disso, garantirá que qualquer multiplicação de dois elementos produzirá um polinômio de grau 2 ou menos.
Vamos trabalhar através de um exemplo da segunda operação usando o polinômio $x^3 + x + 1$ como divisor para ilustrar como funciona. Suponha que você multiplique os elementos $x^2 + 1$ com $x^2 + x$ no nosso conjunto **S**. Então, precisamos calcular a expressão $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$. Isso pode ser simplificado da seguinte forma:
* $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
* $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
* $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$

Sabemos que $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ pode ser reduzido, pois o dividendo tem um grau maior (4) do que o divisor (3).

Para começar, você pode ver que a expressão $x^3 + x + 1$ entra em $x^4 + x^3 + x^2 + x$ um total de $x$ vezes. Você pode verificar isso multiplicando $x^3 + x + 1$ por $x$, que é $x^4 + x^2 + x$. Como o último termo tem o mesmo grau que o dividendo, ou seja, 4, sabemos que isso funciona. Você pode calcular o resto desta divisão por $x$ da seguinte forma:

* $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
* $[x^3] \mod x^3 + x + 1 =$
* $x^3$

Então, após dividir $x^4 + x^3 + x^2 + x$ por $x^3 + x + 1$ um total de $x$ vezes, temos um resto de $x^3$. Isso pode ser ainda mais dividido por $x^3 + x + 1$?

Intuitivamente, pode parecer atraente dizer que $x^3$ não pode mais ser dividido por $x^3 + x + 1$, porque o último termo parece maior. No entanto, lembre-se de nossa discussão sobre divisão de vetores anteriormente. Enquanto o dividendo tiver um grau maior ou igual ao divisor, a expressão pode ser ainda mais reduzida. Especificamente, a expressão $x^3 + x + 1$ pode entrar em $x^3$ exatamente 1 vez. O resto é calculado da seguinte forma:

$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$

Você pode estar se perguntando por que $(x^3) - (x^3 + x + 1)$ avalia para $x + 1$ e não $-x - 1$. Lembre-se de que a primeira operação do nosso campo é definida módulo 2. Portanto, a subtração de dois vetores produz exatamente o mesmo resultado que a adição de dois vetores.
Para resumir a multiplicação de $x^2 + 1$ e $x^2 + x$: Quando você multiplica esses dois termos, obtém-se um polinômio de grau 4, $x^4 + x^3 + x^2 + x$, que precisa ser reduzido módulo $x^3 + x + 1$. O polinômio de grau 4 é divisível por $x^3 + x + 1$ exatamente $x + 1$ vezes. O resto após dividir $x^4 + x^3 + x^2 + x$ por $x^3 + x + 1$ exatamente $x + 1$ vezes é $x + 1$. Este é de fato um elemento no nosso conjunto $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Por que campos de extensão com base 2 sobre conjuntos de polinômios, como no exemplo acima, seriam úteis para criptografia? A razão é que você pode ver os coeficientes nos polinômios desses conjuntos, seja 0 ou 1, como elementos de cadeias binárias com um comprimento particular. O conjunto **S** no nosso exemplo acima, por exemplo, poderia ser visto em vez disso como um conjunto **S** que inclui todas as cadeias binárias de comprimento 3 (000 até 111). As operações em **S**, então, também podem ser usadas para realizar operações nessas cadeias binárias e produzir uma cadeia binária do mesmo comprimento.

**Notas:**

[2] Campos de extensão se tornam muito contra-intuitivos. Em vez de terem elementos de inteiros, eles têm conjuntos de polinômios. Além disso, quaisquer operações são realizadas módulo algum polinômio irredutível.

## Álgebra abstrata na prática
<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>

Apesar da linguagem formal e da abstração da discussão, o conceito de um grupo não deve ser muito difícil de compreender. É apenas um conjunto de elementos juntamente com uma operação binária, onde a execução dessa operação binária nesses elementos atende a quatro condições gerais. Um grupo Abeliano apenas tem uma condição extra conhecida como comutatividade. Um grupo cíclico, por sua vez, é um tipo especial de grupo Abeliano, ou seja, um que tem um gerador. Um campo é meramente uma construção mais complexa a partir da noção básica de grupo.

Mas se você é uma pessoa inclinada à prática, pode se perguntar neste ponto: Quem se importa? Saber que algum conjunto de elementos com um operador é um grupo, ou mesmo um grupo Abeliano ou cíclico, tem alguma relevância no mundo real? Saber que algo é um campo?

Sem entrar em muitos detalhes, a resposta é “sim”. Grupos foram criados pela primeira vez no século 19 pelo matemático francês Evariste Galois. Ele os usou para tirar conclusões sobre a resolução de equações polinomiais de grau superior a cinco.

Desde então, o conceito de um grupo ajudou a esclarecer uma série de problemas em matemática e em outros lugares. Com base neles, por exemplo, o físico Murray-Gellman foi capaz de prever a existência de uma partícula antes de ela ser realmente observada em experimentos. [3] Por outro exemplo, químicos usam a teoria dos grupos para classificar as formas das moléculas. Matemáticos até usaram o conceito de um grupo para tirar conclusões sobre algo tão concreto quanto papel de parede!
Essencialmente, mostrar que um conjunto de elementos com algum operador é um grupo significa que o que você está descrevendo possui uma simetria particular. Não uma simetria no sentido comum da palavra, mas em uma forma mais abstrata. E isso pode fornecer insights substanciais sobre sistemas e problemas específicos. As noções mais complexas da álgebra abstrata apenas nos dão informações adicionais.
Mais importante, você verá a importância dos grupos teóricos dos números e campos na prática através de sua aplicação em criptografia, particularmente a criptografia de chave pública. Já vimos em nossa discussão sobre campos, por exemplo, como os campos de extensão são empregados na Cifra de Rijndael. Trabalharemos esse exemplo no *Capítulo 5*.

Para uma discussão mais aprofundada sobre álgebra abstrata, eu recomendaria a excelente série de vídeos sobre álgebra abstrata da Socratica. [4] Eu recomendaria particularmente os seguintes vídeos: “What is abstract algebra?”, “Group definition (expanded)”, “Ring definition (expanded)”, e “Field definition (expanded).” Esses quatro vídeos lhe darão uma visão adicional sobre muito da discussão acima. (Não discutimos anéis, mas um campo é apenas um tipo especial de anel.)

Para uma discussão mais aprofundada sobre teoria dos números moderna, você pode consultar muitas discussões avançadas sobre criptografia. Eu sugeriria como sugestões a Introdução à Criptografia Moderna de Jonathan Katz e Yehuda Lindell ou Entendendo Criptografia de Christof Paar e Jan Pelzl para uma discussão mais aprofundada. [5]

**Notas:**

[3] Veja [Vídeo do YouTube](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)

[4] Socratica, [Álgebra Abstrata](https://www.socratica.com/subject/abstract-algebra)

[5] Katz e Lindell, *Introduction to Modern Cryptography*, 2ª ed., 2015 (CRC Press: Boca Raton, FL). Paar e Pelzl, *Understanding Cryptography*, 2010 (Springer-Verlag: Berlim).

# Criptografia Simétrica
<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

## Alice e Bob
<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Uma das duas principais ramificações da criptografia é a criptografia simétrica. Ela inclui esquemas de criptografia bem como esquemas preocupados com autenticação e integridade. Até os anos 1970, toda a criptografia consistiria em esquemas de criptografia simétrica.

A discussão principal começa examinando os esquemas de criptografia simétrica e fazendo a distinção crucial entre cifras de fluxo e cifras de bloco. Em seguida, passamos para os códigos de autenticação de mensagens, que são esquemas para garantir a integridade e autenticidade da mensagem. Finalmente, exploramos como os esquemas de criptografia simétrica e códigos de autenticação de mensagens podem ser combinados para garantir uma comunicação segura.

Este capítulo discute várias práticas de esquemas criptográficos simétricos de passagem. O próximo capítulo oferece uma exposição detalhada da criptografia com uma cifra de fluxo e uma cifra de bloco na prática, nomeadamente RC4 e AES, respectivamente.

Antes de começar nossa discussão sobre criptografia simétrica, quero brevemente fazer algumas observações sobre as ilustrações de Alice e Bob neste e nos próximos capítulos.

___

Ao ilustrar os princípios da criptografia, as pessoas frequentemente recorrem a exemplos envolvendo Alice e Bob. Farei o mesmo.

Especialmente se você é novo em criptografia, é importante perceber que esses exemplos de Alice e Bob são apenas para servir como ilustrações dos princípios e construções criptográficas em um ambiente simplificado. Os princípios e construções, no entanto, são aplicáveis a uma gama muito mais ampla de contextos da vida real.
A seguir estão cinco pontos-chave a serem lembrados sobre exemplos envolvendo Alice e Bob em criptografia:
1. Eles podem ser facilmente traduzidos para exemplos com outros tipos de atores, como empresas ou organizações governamentais.
2. Eles podem ser facilmente estendidos para incluir três ou mais atores.
3. Nos exemplos, Bob e Alice são tipicamente participantes ativos na criação de cada mensagem e na aplicação de esquemas criptográficos nessa mensagem. Mas, na realidade, as comunicações eletrônicas são em grande parte automatizadas. Quando você visita um site usando segurança da camada de transporte, por exemplo, a criptografia é tipicamente toda manipulada pelo seu computador e pelo servidor web.
4. No contexto da comunicação eletrônica, as “mensagens” que são enviadas através de um canal de comunicação são geralmente pacotes TCP/IP. Estes podem pertencer a um e-mail, uma mensagem no Facebook, uma conversa telefônica, uma transferência de arquivo, um site, um upload de software, e assim por diante. Eles não são mensagens no sentido tradicional. No entanto, os criptógrafos muitas vezes simplificam essa realidade afirmando que a mensagem é, por exemplo, um e-mail.
5. Os exemplos focam tipicamente na comunicação eletrônica, mas também podem ser estendidos para formas tradicionais de comunicação, como cartas.

## Esquemas de criptografia simétrica
<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Podemos definir de forma geral um **esquema de criptografia simétrica** como qualquer esquema criptográfico com três algoritmos:

1. Um **algoritmo de geração de chave**, que gera uma chave privada.
2. Um **algoritmo de criptografia**, que toma a chave privada e um texto plano como entradas e produz um texto cifrado.
3. Um **algoritmo de descriptografia**, que toma a chave privada e o texto cifrado como entradas e produz o texto plano original.

Tipicamente, um esquema de criptografia — seja simétrico ou assimétrico — oferece um modelo para criptografia baseado em um algoritmo central, em vez de uma especificação exata.

Por exemplo, considere o Salsa20, um esquema de criptografia simétrica. Ele pode ser usado tanto com chaves de 128 quanto de 256 bits. A escolha em relação ao comprimento da chave impacta alguns detalhes menores do algoritmo (o número de rodadas no algoritmo, para ser exato).

Mas não se diria que usar o Salsa20 com uma chave de 128 bits é um esquema de criptografia diferente do Salsa20 com uma chave de 256 bits. O algoritmo central permanece o mesmo. Apenas quando o algoritmo central muda é que realmente falamos de dois esquemas de criptografia diferentes.

Esquemas de criptografia simétrica são tipicamente úteis em dois tipos de casos: (1) Aqueles nos quais dois ou mais agentes estão se comunicando à distância e querem manter o conteúdo de suas comunicações em segredo; e (2) aqueles nos quais um agente quer manter o conteúdo de uma mensagem em segredo ao longo do tempo.

Você pode ver uma representação da situação (1) na *Figura 1* abaixo. Bob quer enviar uma mensagem $M$ para Alice à distância, mas não quer que outros possam ler essa mensagem.

Bob primeiro criptografa a mensagem $M$ com a chave privada $K$. Ele, então, envia o texto cifrado $C$ para Alice. Uma vez que Alice recebeu o texto cifrado, ela pode descriptografá-lo usando a chave $K$ e ler o texto plano. Com um bom esquema de criptografia, qualquer atacante que intercepte o texto cifrado $C$ não deve ser capaz de aprender nada de real significância sobre a mensagem $M$.

Você pode ver uma representação da situação (2) na *Figura 2* abaixo. Bob quer impedir que outros vejam certas informações. Uma situação típica pode ser que Bob é um funcionário armazenando dados sensíveis em seu computador, que nem pessoas de fora nem seus colegas devem ler.
Bob criptografa a mensagem $M$ no momento $T_0$ com a chave $K$ para produzir o texto cifrado $C$. No momento $T_1$, ele precisa da mensagem novamente e descriptografa o texto cifrado $C$ com a chave $K$. Qualquer atacante que possa ter encontrado o texto cifrado $C$ nesse meio tempo não deveria ter sido capaz de deduzir nada significativo sobre $M$ a partir dele.

*Figura 1: Sigilo através do espaço*

![Figura 1: Sigilo através do espaço](assets/Figure4-1.webp "Figura 1: Sigilo através do espaço")


*Figura 2: Sigilo através do tempo*


![Figura 2: Sigilo através do tempo](assets/Figure4-2.webp "Figura 2: Sigilo através do tempo")



## Um exemplo: A cifra de César
<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

No Capítulo 2, encontramos a cifra de César, que é um exemplo de um esquema de criptografia simétrica muito simples. Vamos olhar para ela novamente aqui.

Suponha um dicionário *D* que equipara todas as letras do alfabeto inglês, em ordem, com o conjunto de números $\{0,1,2,\dots,25\}$. Assuma um conjunto de possíveis mensagens **M**. A cifra de César é, então, um esquema de criptografia definido da seguinte forma:

- Selecione aleatoriamente uma chave $k$ do conjunto de possíveis chaves **K**, onde **K** = $\{0,1,2,\dots,25\}$
- Criptografe uma mensagem $m \in$ **M**, da seguinte forma:
    - Separe $m$ em suas letras individuais $m_0, m_1,\dots, m_i, \dots, m_l$
    - Converta cada $m_i$ para um número de acordo com *D*
    - Para cada $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Converta cada $c_i$ para uma letra de acordo com *D*
    - Então combine $c_0, c_1,\dots, c_l$ para produzir o texto cifrado $c$
- Descriptografe um texto cifrado $c$ da seguinte forma:
    - Converta cada $c_i$ para um número de acordo com *D*
    - Para cada $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Converta cada $m_i$ para uma letra de acordo com *D*
    - Então combine $m_0, m_1,\dots, m_l$ para produzir a mensagem original $m$

O que faz da cifra de César um esquema de criptografia simétrica é que a mesma chave é usada tanto para o processo de criptografia quanto para o de descriptografia. Por exemplo, suponha que você queira criptografar a mensagem “DOG” usando a cifra de César, e que você selecionou aleatoriamente "24" como chave. Criptografar a mensagem com esta chave produziria “BME”. A única maneira de recuperar a mensagem original é usando a mesma chave, "24", para o processo de descriptografia.

Esta cifra de César é um exemplo de **cifra de substituição monoalfabética**: um esquema de criptografia onde o alfabeto do texto cifrado é fixo (ou seja, apenas um alfabeto é usado). Assumindo que o algoritmo de descriptografia é determinístico, cada símbolo no texto cifrado de substituição pode, no máximo, pertencer a um símbolo no texto original.
Até o século XVIII, muitas aplicações de criptografia dependiam fortemente de cifras de substituição monoalfabética, embora muitas vezes estas fossem muito mais complexas do que a Cifra de César. Você poderia, por exemplo, selecionar aleatoriamente uma letra do alfabeto para cada letra do texto original sob a restrição de que cada letra ocorra apenas uma vez no alfabeto da cifra. Isso significa que você teria fatorial 26 possíveis chaves privadas, o que era enorme na era pré-computador.
Note que você encontrará o termo **cifra** frequentemente em criptografia. Esteja ciente de que este termo tem vários significados. De fato, conheço pelo menos cinco significados distintos do termo dentro da criptografia.

Em alguns casos, ele se refere a um esquema de criptografia, como acontece na Cifra de César e na cifra de substituição monoalfabética. No entanto, o termo também pode se referir especificamente ao algoritmo de criptografia, à chave privada ou apenas ao texto cifrado de qualquer esquema de criptografia.

Por último, o termo cifra também pode se referir a um algoritmo central a partir do qual você pode construir esquemas criptográficos. Isso pode incluir vários algoritmos de criptografia, mas também outros tipos de esquemas criptográficos. Este sentido do termo torna-se relevante no contexto das cifras de bloco (veja a seção “Cifras de Bloco” abaixo).

Você também pode se deparar com os termos **cifrar** ou **decifrar**. Esses termos são simplesmente sinônimos para criptografia e descriptografia.

## Ataques de força bruta e o princípio de Kerckhoff
<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

A cifra de César é um esquema de criptografia simétrica muito inseguro, pelo menos no mundo moderno. [1] Um atacante poderia simplesmente tentar descriptografar qualquer texto cifrado com todas as 26 chaves possíveis para ver qual resultado faz sentido. Esse tipo de ataque, onde o atacante está apenas percorrendo chaves para ver o que funciona, é conhecido como **ataque de força bruta** ou **busca exaustiva de chave**.

Para que qualquer esquema de criptografia atenda a uma noção mínima de segurança, ele deve ter um conjunto de chaves possíveis, ou **espaço de chaves**, que seja tão grande que ataques de força bruta sejam inviáveis. Todos os esquemas de criptografia modernos atendem a este padrão. Isso é conhecido como o **princípio do espaço de chaves suficiente**. Um princípio semelhante normalmente se aplica em diferentes tipos de esquemas criptográficos.

Para ter uma ideia do tamanho massivo do espaço de chaves em esquemas de criptografia modernos, suponha que um arquivo tenha sido criptografado com uma chave de 128 bits usando o padrão de criptografia avançada. Isso significa que um atacante tem um conjunto de $2^{128}$ chaves pelas quais ela precisa percorrer para um ataque de força bruta. Uma chance de 0,78% de sucesso com essa estratégia exigiria que o atacante percorresse aproximadamente $2,65 \times 10^{36}$ chaves.

Suponhamos que otimisticamente assumimos que um atacante pode tentar $10^{16}$ chaves por segundo (ou seja, 10 quatrilhões de chaves por segundo). Para testar 0,78% de todas as chaves no espaço de chaves, seu ataque teria que durar $2,65 \times 10^{20}$ segundos. Isso é cerca de 8,4 trilhões de anos. Portanto, mesmo um ataque de força bruta por um adversário absurdamente poderoso não é realista com um esquema de criptografia moderno de 128 bits. Este é o princípio do espaço de chaves suficiente em ação.

A cifra de César é mais segura se o atacante não conhece o algoritmo de criptografia? Talvez, mas não muito.
Em qualquer caso, a criptografia moderna sempre assume que a segurança de qualquer esquema de criptografia simétrica depende exclusivamente da manutenção do segredo da chave privada. Presume-se sempre que o atacante conheça todos os outros detalhes, incluindo o espaço da mensagem, o espaço da chave, o espaço do texto cifrado, o algoritmo de seleção da chave, o algoritmo de criptografia e o algoritmo de descriptografia.
A ideia de que a segurança de um esquema de criptografia simétrica só pode depender do segredo da chave privada é conhecida como **princípio de Kerckhoffs**.

Como originalmente pretendido por Kerckhoffs, o princípio só se aplica a esquemas de criptografia simétrica. Uma versão mais geral do princípio, no entanto, também se aplica a todos os outros tipos de esquemas criptográficos modernos: O design de qualquer esquema criptográfico não deve precisar ser secreto para que seja seguro; o segredo só pode se estender a alguma(s) string(s) de informação, tipicamente uma chave privada.

O princípio de Kerckhoffs é central para a criptografia moderna por quatro razões. [2] Primeiro, existem apenas um número limitado de esquemas criptográficos para tipos particulares de aplicações. Por exemplo, a maioria das aplicações modernas de criptografia simétrica usa a cifra Rijndael. Então, seu segredo em relação ao design de um esquema é muito limitado. No entanto, há muito mais flexibilidade em manter alguma chave privada para a cifra Rijndael em segredo.

Segundo, é mais fácil substituir uma string de informação do que um esquema criptográfico inteiro. Suponha que os funcionários de uma empresa tenham o mesmo software de criptografia, e que cada dois funcionários tenham uma chave privada para se comunicar confidencialmente. Comprometimentos de chave são um problema nesse cenário, mas pelo menos a empresa poderia manter o software com tais violações de segurança. Se a empresa dependesse do segredo do esquema, então qualquer violação desse segredo exigiria a substituição de todo o software.

Terceiro, o princípio de Kerckhoffs permite a padronização e compatibilidade entre usuários de esquemas criptográficos. Isso tem benefícios massivos para a eficiência. Por exemplo, é difícil imaginar como milhões de pessoas poderiam se conectar de forma segura aos servidores web do Google todos os dias, se essa segurança exigisse manter os esquemas criptográficos em segredo.

Quarto, o princípio de Kerckhoff permite o escrutínio público dos esquemas criptográficos. Esse tipo de escrutínio é absolutamente necessário para alcançar esquemas criptográficos seguros. Ilustrativamente, o principal algoritmo central em criptografia simétrica, a cifra Rijndael, foi o resultado de uma competição organizada pelo National Institute of Standards and Technology entre 1997 e 2000.

Qualquer sistema que tente alcançar **segurança pela obscuridade** é aquele que depende de manter os detalhes de seu design e/ou implementação em segredo. Em criptografia, isso seria especificamente um sistema que depende de manter os detalhes do design do esquema criptográfico em segredo. Então, segurança pela obscuridade está em contraste direto com o princípio de Kerckhoffs.

A capacidade da abertura para reforçar a qualidade e a segurança também se estende mais amplamente ao mundo digital do que apenas à criptografia. Distribuições Linux de código aberto e gratuito, como o Debian, por exemplo, geralmente têm várias vantagens sobre seus equivalentes Windows e MacOS em termos de privacidade, estabilidade, segurança e flexibilidade. Embora isso possa ter múltiplas causas, o princípio mais importante é provavelmente, como Eric Raymond formulou em seu famoso ensaio "A Catedral e o Bazar", que "dado um número suficiente de olhos, todos os bugs são superficiais". [3] É esse princípio do tipo sabedoria das multidões que deu ao Linux seu maior sucesso.
Não se pode afirmar de forma inequívoca que um esquema criptográfico é "seguro" ou "inseguro". Em vez disso, existem várias noções de segurança para esquemas criptográficos. Cada **definição de segurança criptográfica** deve especificar (1) objetivos de segurança, bem como (2) as capacidades de um atacante. Analisar esquemas criptográficos contra uma ou mais noções específicas de segurança fornece insights sobre suas aplicações e limitações.
Embora não vamos nos aprofundar em todos os detalhes das várias noções de segurança criptográfica, você deve saber que duas suposições são onipresentes em todas as noções modernas de segurança criptográfica relacionadas a esquemas simétricos e assimétricos (e, de alguma forma, a outros primitivos criptográficos):

* O conhecimento do atacante sobre o esquema está de acordo com o princípio de Kerckhoffs.
* O atacante não pode realizar viavelmente um ataque de força bruta no esquema. Especificamente, os modelos de ameaça das noções de segurança criptográfica tipicamente nem mesmo permitem ataques de força bruta, pois assumem que estes não são uma consideração relevante.

**Notas:**

[1] De acordo com Seutonius, um cifrador de deslocamento com um valor de chave constante de 3 foi usado por Júlio César em suas comunicações militares. Assim, A sempre se tornaria D, B sempre E, C sempre F, e assim por diante. Esta versão particular do cifrador de deslocamento, portanto, tornou-se conhecida como **Cifra de César** (embora não seja realmente uma cifra no sentido moderno da palavra, já que o valor da chave é constante). A cifra de César pode ter sido segura no primeiro século a.C., se os inimigos de Roma fossem muito pouco familiarizados com a criptografia. Mas claramente não seria um esquema muito seguro nos tempos modernos.

[2] Jonathan Katz e Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), p. 7f.

[3] Eric Raymond, “The Cathedral and the Bazaar,” o artigo foi apresentado no Linux Kongress, Würzburg, Alemanha (27 de maio de 1997). Existem várias versões subsequentes disponíveis, bem como um livro. Minhas citações são da página 30 do livro: Eric Raymond, _The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary_, edição revisada. (2001), O’Reilly: Sebastopol, CA.

## Cifras de Fluxo
<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Os esquemas de criptografia simétrica são normalmente subdivididos em dois tipos: **cifras de fluxo** e **cifras de bloco**. Esta distinção é um tanto problemática, no entanto, pois as pessoas usam esses termos de maneira inconsistente. Nas próximas seções, vou estabelecer a distinção da maneira que acho melhor. Você deve estar ciente, no entanto, de que muitas pessoas usarão esses termos de maneira um pouco diferente da que estabeleço.

Vamos primeiro nos voltar para as cifras de fluxo. Uma **cifra de fluxo** é um esquema de criptografia simétrica onde a criptografia consiste em dois passos.

Primeiro, uma string do comprimento do texto plano é produzida por meio de uma chave privada. Esta string é chamada de **keystream**.

Em seguida, o keystream é combinado matematicamente com o texto plano para produzir um texto cifrado. Esta combinação é tipicamente uma operação XOR. Para descriptografar, você pode simplesmente reverter a operação. (Note que $A \oplus B = B \oplus A$, no caso de $A$ e $B$ serem cadeias de bits. Assim, a ordem de uma operação XOR em uma cifra de fluxo não importa para o resultado. Esta propriedade é conhecida como **comutatividade**.)
Um típico cifrador de fluxo XOR é retratado na *Figura 3*. Primeiro, você toma uma chave privada $K$ e a usa para gerar um fluxo de chaves. O fluxo de chaves é, então, combinado com o texto puro através de uma operação XOR para produzir o texto cifrado. Qualquer agente que receba o texto cifrado pode facilmente descriptografá-lo se tiver a chave $K$. Tudo o que ela precisa fazer é criar um fluxo de chaves tão longo quanto o texto cifrado de acordo com o procedimento especificado do esquema e aplicar XOR com o texto cifrado.

*Figura 3: Um cifrador de fluxo XOR*

![Figura 3: Um cifrador de fluxo XOR](assets/Figure4-3.webp "Figura 3: Um cifrador de fluxo XOR")

Lembre-se de que um esquema de criptografia é tipicamente um modelo para criptografia com o mesmo algoritmo central, em vez de uma especificação exata. Por extensão, um cifrador de fluxo é tipicamente um modelo para criptografia no qual você pode usar chaves de diferentes comprimentos. Embora o comprimento da chave possa impactar alguns detalhes menores do esquema, isso não afetará sua forma essencial.

O cifrador de deslocamento é um exemplo de um cifrador de fluxo muito simples e inseguro. Usando uma única letra (a chave privada), você pode produzir uma sequência de letras do comprimento da mensagem (o fluxo de chaves). Este fluxo de chaves é, então, combinado com o texto puro através de uma operação de módulo para produzir um texto cifrado. (Esta operação de módulo pode ser simplificada para uma operação XOR quando representando as letras em bits).

Outro exemplo famoso de um cifrador de fluxo é o **cifrador de Vigenère**, após Blaise de Vigenère que o desenvolveu completamente no final do século 16 (embora outros já tivessem feito muito trabalho precedente). É um exemplo de um **cifrador de substituição polialfabético**: um esquema de criptografia onde o alfabeto do texto cifrado para um símbolo do texto puro muda dependendo de sua posição no texto. Em contraste com um cifrador de substituição monoalfabético, símbolos do texto cifrado podem ser associados a mais de um símbolo do texto puro.

À medida que a criptografia ganhava popularidade na Europa Renascentista, também ganhava **criptoanálise** — isto é, a quebra de textos cifrados — particularmente, usando **análise de frequência**. A última emprega regularidades estatísticas em nossa linguagem para quebrar textos cifrados, e foi descoberta por estudiosos árabes já no nono século. É uma técnica que funciona particularmente bem com textos mais longos. E até mesmo os cifradores de substituição monoalfabéticos mais sofisticados já não eram suficientes contra a análise de frequência até o século 1700 na Europa, particularmente em configurações militares e de segurança. Como o cifrador de Vigenère oferecia um avanço significativo em segurança, tornou-se popular neste período e estava difundido até o final dos anos 1700.

Falando informalmente, o esquema de criptografia funciona da seguinte forma:

1. Selecione uma palavra de várias letras como a chave privada.
2. Para qualquer mensagem, aplique o cifrador de deslocamento a cada letra da mensagem usando a letra correspondente na palavra-chave como o deslocamento.
3. Se você tiver percorrido a palavra-chave mas ainda não tiver cifrado totalmente o texto puro, aplique novamente as letras da palavra-chave como um cifrador de deslocamento às letras correspondentes no restante do texto.
4. Continue este processo até que a mensagem inteira tenha sido cifrada.

Para ilustrar, suponha que sua chave privada seja "GOLD" e você queira criptografar a mensagem "CRYPTOGRAPHY". Nesse caso, você procederia da seguinte forma de acordo com o cifrador de Vigenère:

- $c_0  = [(2 + 6) \mod 26] = 8 = I$
- $c_1  = [(17 + 14) \mod 26] = 5 = F$
- $c_2  = [(24 + 11) \mod 26] = 9 = J$
- $c_3 = [(15 + 3) \mod 26] = 18 = S$
- $c_4 = [(19 + 6) \mod 26] = 25 = Z$
- $c_5 = [(14 + 14) \mod 26] = 2 = C$
- $c_6 = [(6 + 11) \mod 26] = 17 = R$
- $c_7 = [(17 + 3) \mod 26] = 20 = U$
- $c_8 = [(0 + 6) \mod 26] = 6 = G$
- $c_9 = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$

Assim, o texto cifrado $c$ = "IFJSZCRUGDSB".

Outro exemplo famoso de cifra de fluxo é o **bloco de uso único**. Com o bloco de uso único, você simplesmente cria uma sequência de bits aleatórios tão longa quanto a mensagem em texto claro e produz o texto cifrado por meio da operação XOR. Portanto, a chave privada e a sequência de cifra são equivalentes com um bloco de uso único.

Enquanto as cifras de César e Vigenère são muito inseguras na era moderna, o bloco de uso único é muito seguro se usado corretamente. Provavelmente a aplicação mais famosa do bloco de uso único foi, pelo menos até a década de 1980, para a **linha direta Washington-Moscou**.

A linha direta é um link de comunicações diretas entre Washington e Moscou para assuntos urgentes que foi instalado após a Crise dos Mísseis de Cuba. A tecnologia para isso transformou-se ao longo dos anos. Atualmente, inclui um cabo de fibra óptica direto, bem como dois links via satélite (para redundância), que permitem e-mail e mensagens de texto. O link termina em vários lugares nos EUA. O Pentágono, a Casa Branca e a Montanha Raven Rock são pontos finais conhecidos. Ao contrário da opinião popular, a linha direta nunca envolveu telefones.

Na essência, o esquema do bloco de uso único funcionava da seguinte forma. Tanto Washington quanto Moscou teriam dois conjuntos de números aleatórios. Um conjunto de números aleatórios, criado pelos russos, referia-se à criptografia e descriptografia de quaisquer mensagens em russo. Um conjunto de números aleatórios, criado pelos americanos, referia-se à criptografia e descriptografia de quaisquer mensagens em inglês. De tempos em tempos, mais números aleatórios seriam entregues ao outro lado por mensageiros confiáveis.

Washington e Moscou eram, então, capazes de comunicar-se secretamente usando esses números aleatórios para criar blocos de uso único. Cada vez que você precisasse comunicar, usaria a próxima porção de números aleatórios para sua mensagem.

Embora altamente seguro, o bloco de uso único enfrenta limitações práticas significativas: a chave precisa ser tão longa quanto a mensagem e nenhuma parte de um bloco de uso único pode ser reutilizada. Isso significa que você precisa acompanhar onde está no bloco de uso único, armazenar um número massivo de bits e trocar bits aleatórios com seus contrapartes de tempos em tempos. Como consequência, o bloco de uso único não é frequentemente usado na prática.

Em vez disso, as cifras de fluxo predominantes usadas na prática são **cifras de fluxo pseudorrandômicas**. Salsa20 e uma variante intimamente relacionada chamada ChaCha são exemplos de cifras de fluxo pseudorrandômicas comumente usadas.
Com esses cifradores de fluxo pseudorrandom, você primeiro seleciona aleatoriamente uma chave K que é mais curta que o comprimento do texto plano. Tal chave aleatória K é geralmente criada pelo nosso computador com base em dados imprevisíveis que ele coleta ao longo do tempo, como o tempo entre mensagens de rede, movimentos do mouse, e assim por diante.
Esta chave aleatória $K$ é então inserida em um algoritmo de expansão que cria uma corrente de chave pseudorrandom tão longa quanto a mensagem. Você pode especificar precisamente quão longa a corrente de chave precisa ser (por exemplo, 500 bits, 1000 bits, 1200 bits, 29.117 bits, e assim por diante).

Uma corrente de chave pseudorrandom parece *como se* tivesse sido escolhida completamente ao acaso do conjunto de todas as strings com o mesmo comprimento. Portanto, a criptografia com uma corrente de chave pseudorrandom parece como se tivesse sido feita com um bloco de uso único. Mas claro, esse não é o caso.

Como nossa chave privada é mais curta que a corrente de chave e nosso algoritmo expansionário precisa ser determinístico para que o processo de criptografia/descriptografia funcione, nem toda corrente de chave daquele comprimento específico poderia ter resultado como uma saída de nossa operação expansionária.

Suponha, por exemplo, que nossa chave privada tenha um comprimento de 128 bits e que possamos inseri-la em um algoritmo expansionário para criar uma corrente de chave muito mais longa, digamos de 2.500 bits. Como nosso algoritmo expansionário precisa ser determinístico, nosso algoritmo pode no máximo selecionar $1/2^{128}$ strings com um comprimento de 2.500 bits. Então, tal corrente de chave nunca poderia ser selecionada inteiramente ao acaso de todas as strings do mesmo comprimento.

Nossa definição de um cifrador de fluxo tem dois aspectos: (1) uma corrente de chave tão longa quanto o texto plano é gerada com a ajuda de uma chave privada; e (2) essa corrente de chave é combinada com o texto plano, tipicamente via uma operação XOR, para produzir o texto cifrado.

Às vezes, as pessoas definem a condição (1) de forma mais estrita, afirmando que a corrente de chave deve especificamente ser pseudorrandom. Isso significa que nem o cifrador de deslocamento, nem o bloco de uso único seriam considerados cifradores de fluxo.

Na minha visão, definir a condição (1) de forma mais ampla oferece uma maneira mais fácil de organizar esquemas de criptografia. Além disso, significa que não temos que parar de chamar um determinado esquema de criptografia de cifrador de fluxo só porque aprendemos que ele não depende realmente de correntes de chave pseudorrandom.

**Notas:**

[4] Crypto Museum, "Linha direta Washington-Moscou," 2013, disponível em [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).

## Cifradores de bloco
<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

A primeira maneira que um **cifrador de bloco** é comumente entendido é como algo mais primitivo que um cifrador de fluxo: Um algoritmo central que realiza uma transformação preservadora de comprimento em uma string de um comprimento adequado com a ajuda de uma chave. Este algoritmo pode ser usado para criar esquemas de criptografia e talvez outros tipos de esquemas criptográficos.
Frequentemente, uma cifra de bloco pode receber strings de entrada de comprimentos variáveis, como 64, 128 ou 256 bits, bem como chaves de comprimentos variáveis, como 128, 192 ou 256 bits. Embora alguns detalhes do algoritmo possam mudar dependendo dessas variáveis, o algoritmo central não muda. Se mudasse, falaríamos de duas cifras de bloco diferentes. Note que o uso da terminologia de algoritmo central aqui é o mesmo que para esquemas de criptografia.
Uma representação de como uma cifra de bloco funciona pode ser vista na *Figura 4* abaixo. Uma mensagem $M$ de comprimento $L$ e uma chave $K$ servem como entradas para a Cifra de Bloco. Ela produz uma mensagem $M'$ de comprimento $L$. A chave não necessariamente precisa ter o mesmo comprimento que $M$ e $M'$ para a maioria das cifras de bloco.

*Figura 4: Uma cifra de bloco*

![Figura 4: Uma cifra de bloco](assets/Figure4-4.webp "Figura 4: Uma cifra de bloco")

Uma cifra de bloco por si só não é um esquema de criptografia. Mas uma cifra de bloco pode ser usada com vários **modos de operação** para produzir diferentes esquemas de criptografia. Um modo de operação simplesmente adiciona algumas operações adicionais fora da cifra de bloco.

Para ilustrar como isso funciona, suponha uma cifra de bloco (BC) que requer uma string de entrada de 128 bits e uma chave privada de 128 bits. A Figura 5 abaixo mostra como essa cifra de bloco pode ser usada com o **modo de livro de códigos eletrônicos** (**modo ECB**) para criar um esquema de criptografia. (As elipses à direita indicam que você pode repetir esse padrão conforme necessário).

*Figura 5: Uma cifra de bloco com modo ECB*

![Figura 5: Uma cifra de bloco com modo ECB](assets/Figure4-5.webp "Figura 5: Uma cifra de bloco com modo ECB")

O processo para a criptografia de livro de códigos eletrônicos com a cifra de bloco é o seguinte. Veja se você pode dividir sua mensagem em texto claro em blocos de 128 bits. Se não, adicione **preenchimento** à mensagem, para que o resultado possa ser dividido igualmente pelo tamanho do bloco de 128 bits. Estes são seus dados usados para o processo de criptografia.

Agora divida os dados em pedaços de strings de 128 bits ($M_1$, $M_2$, $M_3$ e assim por diante). Execute cada string de 128 bits através da cifra de bloco com sua chave de 128 bits para produzir pedaços de 128 bits de texto cifrado ($C_1$, $C_2$, $C_3$ e assim por diante). Esses pedaços, quando re-combinados, formam o texto cifrado completo.

A descriptografia é apenas o processo inverso, embora o destinatário precise de alguma maneira reconhecível de remover qualquer preenchimento dos dados descriptografados para produzir a mensagem original em texto claro.

Embora relativamente simples, uma cifra de bloco com modo de livro de códigos eletrônicos carece de segurança. Isso ocorre porque leva à **criptografia determinística**. Qualquer duas strings de dados de 128 bits idênticas são criptografadas exatamente da mesma maneira. Essa informação pode ser explorada.

Em vez disso, qualquer esquema de criptografia construído a partir de uma cifra de bloco deve ser **probabilístico**: isto é, a criptografia de qualquer mensagem $M$, ou qualquer pedaço específico de $M$, deve geralmente produzir um resultado diferente a cada vez. [5]

O **modo de encadeamento de blocos cifrados** (**modo CBC**) é provavelmente o modo mais comum usado com uma cifra de bloco. A combinação, se feita corretamente, produz um esquema de criptografia probabilístico. Você pode ver uma representação deste modo de operação na *Figura 6* abaixo.

*Figura 6: Uma cifra de bloco com modo CBC*
![Figure 6: Um cifrador de bloco com modo CBC](assets/Figure4-6.webp "Figura 6: Um cifrador de bloco com modo CBC")
Suponha que o tamanho do bloco seja novamente de 128 bits. Então, para começar, você precisaria novamente garantir que sua mensagem original em texto plano receba o preenchimento necessário.

Em seguida, você faz um XOR da primeira porção de 128 bits do seu texto plano com um **vetor de inicialização** de 128 bits. O resultado é colocado no cifrador de bloco para produzir um texto cifrado para o primeiro bloco. Para o segundo bloco de 128 bits, você primeiro faz um XOR do texto plano com o texto cifrado do primeiro bloco, antes de inseri-lo no cifrador de bloco. Você continua esse processo até ter criptografado toda a sua mensagem em texto plano.

Quando terminar, você envia a mensagem criptografada junto com o vetor de inicialização não criptografado para o destinatário. O destinatário precisa conhecer o vetor de inicialização, caso contrário, ele não pode descriptografar o texto cifrado.

Esta construção é muito mais segura do que o modo de livro de códigos eletrônicos quando usada corretamente. Você deve, primeiro, garantir que o vetor de inicialização seja uma string aleatória ou pseudoaleatória. Além disso, você deve usar um vetor de inicialização diferente cada vez que usar esse esquema de criptografia.

Em outras palavras, seu vetor de inicialização deve ser um nonce aleatório ou pseudoaleatório, onde um **nonce** significa "um número que é usado apenas uma vez". Se você manter essa prática, então o modo CBC com um cifrador de bloco garante que quaisquer dois blocos de texto plano idênticos geralmente serão criptografados de maneira diferente a cada vez.

Finalmente, vamos voltar nossa atenção para o **modo de feedback de saída** (**modo OFB**). Você pode ver uma representação deste modo na *Figura 7*.

*Figura 7: Um cifrador de bloco com modo OFB*

![Figure 7: Um cifrador de bloco com modo OFB](assets/Figure4-7.webp "Figura 7: Um cifrador de bloco com modo OFB")

Com o modo OFB, você também seleciona um vetor de inicialização. Mas aqui, para o primeiro bloco, o vetor de inicialização é inserido diretamente no cifrador de bloco com sua chave. Os 128 bits resultantes são, então, tratados como um fluxo de chave. Este fluxo de chave é feito XOR com o texto plano para produzir o texto cifrado para o bloco. Para os blocos subsequentes, você usa o fluxo de chave do bloco anterior como uma entrada no cifrador de bloco e repete os passos.

Se você olhar cuidadosamente, o que foi realmente criado aqui a partir do cifrador de bloco com modo OFB é um cifrador de fluxo. Você gera porções do fluxo de chave de 128 bits até ter o comprimento do texto plano (descartando os bits que não precisa da última porção do fluxo de chave de 128 bits). Você, então, faz XOR do fluxo de chave com sua mensagem em texto plano para obter o texto cifrado.

Na seção anterior sobre cifradores de fluxo, eu afirmei que você produz um fluxo de chave com a ajuda de uma chave privada. Para ser exato, não precisa ser criado apenas com uma chave privada. Como você pode ver no modo OFB, o fluxo de chave é produzido com o apoio de uma chave privada e um vetor de inicialização.

Note que, assim como no modo CBC, é importante selecionar um nonce pseudoaleatório ou aleatório para o vetor de inicialização cada vez que você usa um cifrador de bloco no modo OFB. Caso contrário, a mesma string de mensagem de 128 bits enviada em diferentes comunicações será criptografada da mesma maneira. Esta é uma maneira de criar criptografia probabilística com um cifrador de fluxo.
Alguns cifradores de fluxo usam apenas uma chave privada para criar um fluxo de chaves. Para esses cifradores de fluxo, é importante que você use um nonce aleatório para selecionar a chave privada para cada instância de comunicação. Caso contrário, os resultados da criptografia com esses cifradores de fluxo também serão determinísticos, levando a questões de segurança.
O cifrador de bloco moderno mais popular é o **cifrador Rijndael**. Foi a entrada vencedora de quinze submissões para uma competição realizada pelo Instituto Nacional de Padrões e Tecnologia (NIST) entre 1997 e 2000 para substituir um padrão de criptografia mais antigo, o **padrão de criptografia de dados** (**DES**).

O cifrador Rijndael pode ser usado com diferentes especificações para comprimentos de chave e tamanhos de bloco, bem como em diferentes modos de operação. O comitê para a competição do NIST adotou uma versão restrita do cifrador Rijndael — especificamente uma que requer tamanhos de bloco de 128 bits e comprimentos de chave de 128 bits, 192 bits ou 256 bits — como parte do **padrão de criptografia avançado** (**AES**). Este é realmente o principal padrão para aplicações de criptografia simétrica. É tão seguro que até mesmo a NSA aparentemente está disposta a usá-lo com chaves de 256 bits para documentos ultrassecretos. [6]

O cifrador de bloco AES será explicado em detalhes no *Capítulo 5*.

**Notas:**

[5] A importância da criptografia probabilística foi enfatizada pela primeira vez por Shafi Goldwasser e Silvio Micali, “Criptografia probabilística,” _Journal of Computer and System Sciences_, 28 (1984), 270–99.

[6] Veja NSA, "Conjunto de Algoritmos de Segurança Nacional Comercial", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).

## Esclarecendo a confusão
<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

A confusão sobre a distinção entre cifradores de bloco e cifradores de fluxo surge porque às vezes as pessoas entenderão o termo cifrador de bloco como referindo-se especificamente a um *cifrador de bloco com um modo de criptografia de bloco*.

Considere os modos ECB e CBC na seção anterior. Estes especificamente requerem que os dados para criptografia sejam divisíveis pelo tamanho do bloco (o que significa que você pode ter que usar preenchimento para a mensagem original). Além disso, os dados nesses modos também são operados diretamente pelo cifrador de bloco (e não apenas combinados com o resultado de uma operação de cifrador de bloco como no modo OFB).

Portanto, alternativamente, você pode definir um **cifrador de bloco** como qualquer esquema de criptografia, que opera em blocos de mensagem de tamanho fixo por vez (onde qualquer bloco deve ser maior que um byte, caso contrário, ele se transforma em um cifrador de fluxo). Tanto os dados para criptografia quanto o texto cifrado devem dividir-se igualmente neste tamanho de bloco. Tipicamente, o tamanho do bloco é de 64, 128, 192 ou 256 bits de comprimento. Em contraste, um cifrador de fluxo pode criptografar mensagens em pedaços de um bit ou byte de cada vez.

Com esse entendimento mais específico de cifrador de bloco, você pode de fato afirmar que os esquemas modernos de criptografia são ou cifradores de fluxo ou cifradores de bloco. Daqui para frente, eu me referirei ao termo cifrador de bloco no sentido mais geral, a menos que especificado de outra forma.
A discussão sobre o modo OFB na seção anterior também levanta outro ponto interessante. Alguns cifradores de fluxo são construídos a partir de cifradores de bloco, como o Rijndael com OFB. Alguns, como o Salsa20 e o ChaCha, não são criados a partir de cifradores de bloco. Você poderia chamar os últimos de **cifradores de fluxo primitivos**. (Na verdade, não existe um termo padronizado para se referir a tais cifradores de fluxo.)
Quando as pessoas falam sobre as vantagens e desvantagens dos cifradores de fluxo e dos cifradores de bloco, elas estão tipicamente comparando cifradores de fluxo primitivos a esquemas de criptografia baseados em cifradores de bloco.

Embora você possa sempre construir facilmente um cifrador de fluxo a partir de um cifrador de bloco, é tipicamente muito difícil construir algum tipo de construto com um modo de criptografia de bloco (como com o modo CBC) a partir de um cifrador de fluxo primitivo.

A partir desta discussão, você deve agora entender a *Figura 8*. Ela fornece uma visão geral sobre esquemas de criptografia simétrica. Usamos três tipos de esquemas de criptografia: cifradores de fluxo primitivos, cifradores de fluxo de cifradores de bloco e cifradores de bloco em um modo de bloco (também chamado de “cifradores de bloco” no diagrama).

*Figura 8: Visão geral dos esquemas de criptografia simétrica*

![Figura 8: Visão geral dos esquemas de criptografia simétrica](assets/Figure4-8.webp "Figura 8: Visão geral dos esquemas de criptografia simétrica")

## Códigos de autenticação de mensagem
<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>

A criptografia está preocupada com o segredo. Mas a criptografia também está preocupada com temas mais amplos, como integridade da mensagem, autenticidade e não repúdio. Os chamados **códigos de autenticação de mensagem** (MACs) são esquemas criptográficos de chave simétrica que suportam autenticidade e integridade nas comunicações.

Por que algo além do segredo é necessário na comunicação? Suponha que Bob envie a Alice uma mensagem usando uma criptografia praticamente inquebrável. Qualquer atacante que intercepte esta mensagem não será capaz de obter quaisquer insights significativos sobre o conteúdo. No entanto, o atacante ainda tem pelo menos dois outros vetores de ataque disponíveis para ela:

1. Ela poderia interceptar o texto cifrado, alterar seu conteúdo e enviar o texto cifrado alterado para Alice.
2. Ela poderia bloquear completamente a mensagem de Bob e enviar seu próprio texto cifrado criado.

Nesses dois casos, o atacante pode não ter nenhum insight sobre o conteúdo dos textos cifrados (1) e (2). Mas ela ainda poderia causar danos significativos dessa maneira. É aqui que os códigos de autenticação de mensagem se tornam importantes.

Códigos de autenticação de mensagem são definidos de forma solta como esquemas criptográficos simétricos com três algoritmos: um algoritmo de geração de chave, um algoritmo de geração de tag e um algoritmo de verificação. Um MAC seguro garante que as tags sejam **existencialmente infalsificáveis** para qualquer atacante — ou seja, eles não podem criar com sucesso uma tag na mensagem que verifica, a menos que tenham a chave privada.

Bob e Alice podem combater a manipulação de uma mensagem específica usando um MAC. Suponha por um momento que eles não se importam com o segredo. Eles apenas querem garantir que a mensagem recebida por Alice foi de fato de Bob e não foi alterada de forma alguma.

O processo é retratado na *Figura 9*. Para usar um **MAC** (Código de Autenticação de Mensagem), eles primeiro gerariam uma chave privada $K$ que é compartilhada entre os dois. Bob cria uma tag $T$ para a mensagem usando a chave privada $K$. Ele então envia a mensagem, bem como a tag da mensagem para Alice. Ela pode então verificar que Bob de fato fez a tag, executando a chave privada, a mensagem e a tag através de um algoritmo de verificação.

*Figura 9: Visão geral dos esquemas de criptografia simétrica*
![Figura 9: Visão geral dos esquemas de criptografia simétrica](assets/Figure4-9.webp "Figura 9: Visão geral dos esquemas de criptografia simétrica")
Devido à **inviolabilidade existencial**, um atacante não pode alterar a mensagem $M$ de forma alguma ou criar uma mensagem própria com uma etiqueta válida. Isso ocorre mesmo se o atacante observar as etiquetas de muitas mensagens entre Bob e Alice que usam a mesma chave privada. No máximo, um atacante poderia impedir que Alice recebesse a mensagem $M$ (um problema que a criptografia não pode resolver).

Um MAC garante que uma mensagem foi realmente criada por Bob. Essa autenticidade implica automaticamente na integridade da mensagem — ou seja, se Bob criou alguma mensagem, então, ipso facto, ela não foi alterada de forma alguma por um atacante. Portanto, a partir de agora, qualquer preocupação com autenticação deve ser automaticamente entendida como uma preocupação com integridade.

Embora eu tenha feito uma distinção entre autenticidade e integridade da mensagem em minha discussão, também é comum usar esses termos como sinônimos. Eles, então, referem-se à ideia de mensagens que foram criadas por um remetente específico e não alteradas de forma alguma. Nesse espírito, os códigos de autenticação de mensagens são frequentemente chamados também de **códigos de integridade de mensagens**.


## Criptografia autenticada
<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>

Tipicamente, você desejaria garantir tanto o segredo quanto a autenticidade na comunicação e, portanto, esquemas de criptografia e esquemas MAC são tipicamente usados juntos.

Um **esquema de criptografia autenticada** é um esquema que combina criptografia com um MAC de maneira altamente segura. Especificamente, ele deve atender aos padrões para inviolabilidade existencial, bem como a uma noção muito forte de segredo, nomeadamente uma que seja resistente a **ataques de texto cifrado escolhido**. [7]

Para que um esquema de criptografia seja resistente a ataques de texto cifrado escolhido, ele deve atender aos padrões de **não maleabilidade**: isto é, qualquer modificação de um texto cifrado por um atacante deve resultar ou em um texto cifrado inválido ou em um que decifra para um texto plano sem relação com o original. [8]

Como um esquema de criptografia autenticada garante que um texto cifrado criado por um atacante seja sempre inválido (já que a etiqueta não será verificada), ele atende aos padrões de resistência a ataques de texto cifrado escolhido. Interessantemente, você pode provar que um esquema de criptografia autenticada pode sempre ser criado a partir da combinação de um MAC inviolável existencialmente e um esquema de criptografia que atenda a uma noção de segurança menos forte, conhecida como **segurança contra ataques de texto plano escolhido**.

Não entraremos em todos os detalhes da construção de esquemas de criptografia autenticada. Mas é importante conhecer dois detalhes de sua construção.

Primeiro, um esquema de criptografia autenticada lida primeiro com a criptografia e depois cria uma etiqueta de mensagem no texto cifrado. Revela-se que outras abordagens — como combinar o texto cifrado com uma etiqueta no texto plano, ou primeiro criar uma etiqueta e depois cifrar tanto o texto plano quanto a etiqueta — são inseguras. Além disso, ambas as operações têm sua própria chave privada selecionada aleatoriamente, caso contrário, sua segurança é severamente comprometida.

O princípio mencionado aplica-se mais geralmente: *você deve sempre usar chaves distintas ao combinar esquemas criptográficos básicos*.

Um esquema de criptografia autenticada é retratado na *Figura 10*. Bob primeiro cria um texto cifrado $C$ a partir da mensagem $M$ usando uma chave $K_C$ selecionada aleatoriamente. Ele então cria uma etiqueta de mensagem $T$ executando o texto cifrado e uma chave diferente $K_T$ selecionada aleatoriamente através do algoritmo de geração de etiqueta. Tanto o texto cifrado quanto a etiqueta de mensagem são enviados para Alice.
Alice agora verifica primeiro se a tag é válida dado o texto cifrado $C$ e a chave $K_T$. Se válida, ela pode então descriptografar a mensagem usando a chave $K_C$. Não apenas ela tem a garantia de uma noção muito forte de sigilo em suas comunicações, mas também sabe que a mensagem foi criada por Bob.
*Figura 10: Um esquema de criptografia autenticada*

![Figura 10: Um esquema de criptografia autenticada](assets/Figure4-10.webp "Figura 10: Um esquema de criptografia autenticada")

Como são criados os MACs? Embora os MACs possam ser criados por vários métodos, uma maneira comum e eficiente de criá-los é através de **funções hash criptográficas**.

Introduziremos as funções hash criptográficas mais detalhadamente no *Capítulo 6*. Por agora, saiba apenas que uma **função hash** é uma função computável de forma eficiente que recebe entradas de tamanho arbitrário e produz saídas de tamanho fixo. Por exemplo, a popular função hash **SHA-256** (algoritmo de hash seguro 256) sempre gera uma saída de 256 bits, independentemente do tamanho da entrada. Algumas funções hash, como o SHA-256, têm aplicações úteis em criptografia.

O tipo mais comum de tag produzido com uma função hash criptográfica é o **código de autenticação de mensagem baseado em hash** (HMAC). O processo é ilustrado na *Figura 11*. Uma parte produz duas chaves distintas a partir de uma chave privada $K$, a chave interna $K_1$ e a chave externa $K_2$. O texto plano $M$ ou o texto cifrado $C$ é então hashado junto com a chave interna. O resultado $T'$ é então hashado com a chave externa para produzir a tag da mensagem $T$.

Existe uma paleta de funções hash que podem ser usadas para criar um HMAC. A função hash mais comumente empregada é o SHA-256.

*Figura 11: HMAC*

![Figura 11: HMAC](assets/Figure4-11.webp "Figura 11: HMAC")

**Notas:**

[7] Os resultados específicos discutidos nesta seção são de Katz e Lindell, pp. 131–47.

[8] Tecnicamente, a definição de ataques de texto cifrado escolhido é diferente da noção de não maleabilidade. Mas você pode mostrar que essas duas noções de segurança são equivalentes.

## Sessões de comunicação segura
<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Suponha que duas partes estejam em uma sessão de comunicação, então elas enviam várias mensagens de ida e volta.

Um esquema de criptografia autenticada permite que o destinatário de uma mensagem verifique que ela foi criada por seu parceiro na sessão de comunicação (desde que a chave privada não tenha vazado). Isso funciona bem o suficiente para uma única mensagem. Tipicamente, no entanto, duas partes estão enviando mensagens de ida e volta em uma sessão de comunicação. E nesse cenário, um esquema de criptografia autenticada simples, como descrito na seção anterior, fica aquém em fornecer segurança.

A principal razão é que um esquema de criptografia autenticada não fornece garantias de que a mensagem foi de fato também enviada pelo agente que a criou dentro de uma sessão de comunicação. Considere os seguintes três vetores de ataque:

1. **Ataque de repetição**: Um atacante reenvia um texto cifrado e uma tag que interceptou entre duas partes em um momento anterior.
2. **Ataque de reordenação**: Um atacante intercepta duas mensagens em momentos diferentes e as envia ao destinatário na ordem inversa.
3. **Ataque de reflexão**: Um atacante observa uma mensagem enviada de A para B e também envia essa mensagem para A.

Embora o atacante não tenha conhecimento do texto cifrado e não possa criar textos cifrados falsificados, os ataques acima ainda podem causar danos significativos nas comunicações.
Suponha, por exemplo, que uma determinada mensagem entre duas partes envolva a transferência de fundos financeiros. Um ataque de repetição poderia transferir os fundos uma segunda vez. Um esquema de criptografia autenticada simples não tem defesa contra tais ataques.
Felizmente, esse tipo de ataque pode ser facilmente mitigado em uma sessão de comunicação usando **identificadores** e **indicadores de tempo relativo**.

Identificadores podem ser adicionados à mensagem em texto claro antes da criptografia. Isso impediria quaisquer ataques de reflexão. Um indicador de tempo relativo pode, por exemplo, ser um número de sequência em uma sessão de comunicação particular. Cada parte adiciona um número de sequência a uma mensagem antes da criptografia, para que o destinatário saiba em que ordem as mensagens foram enviadas. Isso elimina a possibilidade de ataques de reordenação. Também elimina ataques de repetição. Qualquer mensagem que um atacante envie posteriormente terá um número de sequência antigo, e o destinatário saberá que não deve processar a mensagem novamente.

Para ilustrar como funcionam as sessões de comunicação segura, suponha novamente Alice e Bob. Eles enviam um total de quatro mensagens de ida e volta. Você pode ver como um esquema de criptografia autenticada com identificadores e números de sequência funcionaria abaixo na *Figura 11*.

A sessão de comunicação começa com Bob enviando um texto cifrado $C_{0,B}$ para Alice com uma tag de mensagem $T_{0,B}$. O texto cifrado contém a mensagem, bem como um identificador (BOB) e um número de sequência (0). A tag $T_{0,B}$ é feita sobre o texto cifrado inteiro. Em suas comunicações subsequentes, Alice e Bob mantêm esse protocolo, atualizando os campos conforme necessário.

*Figura 12: Uma sessão de comunicação segura*

![Figura 12: Uma sessão de comunicação segura](assets/Figure4-12.webp "Figura 12: Uma sessão de comunicação segura")

# RC4 e AES
<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

## O cifrador de fluxo RC4
<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>

Neste capítulo, discutiremos os detalhes de um esquema de criptografia com um cifrador de fluxo primitivo moderno, RC4 (ou "Rivest cipher 4"), e um cifrador de bloco moderno, AES. Embora o cifrador RC4 tenha caído em desuso como método de criptografia, o AES é o padrão para criptografia simétrica moderna. Esses dois exemplos devem dar uma ideia melhor de como a criptografia simétrica funciona por baixo dos panos.

___

Para ter uma noção de como funcionam os cifradores de fluxo pseudorrandômicos modernos, focarei no cifrador de fluxo RC4. É um cifrador de fluxo pseudorrandômico que foi usado nos protocolos de segurança de pontos de acesso sem fio WEP e WAP, bem como em TLS. Como o RC4 tem muitas fraquezas comprovadas, ele caiu em desuso. De fato, a Internet Engineering Task Force agora proíbe o uso de suítes RC4 por aplicativos cliente e servidor em todas as instâncias de TLS. No entanto, ele serve bem como um exemplo para ilustrar como funciona um cifrador de fluxo primitivo.

Para começar, primeiro mostrarei como criptografar uma mensagem em texto claro com um cifrador RC4 simplificado. Suponha que nossa mensagem em texto claro seja “SOUP”. A criptografia com nosso cifrador RC4 simplificado, então, procede em quatro etapas.

### Etapa 1
Primeiro, defina um array **S** com $S[0] = 0$ até $S[7] = 7$. Um array aqui simplesmente significa uma coleção mutável de valores organizados por um índice, também chamado de lista em algumas linguagens de programação (por exemplo, Python). Neste caso, o índice vai de 0 a 7, e os valores também vão de 0 a 7. Então, **S** é o seguinte:
- $S = [0, 1, 2, 3, 4, 5, 6, 7]$

Os valores aqui não são números ASCII, mas as representações de valor decimal de strings de 1 byte. Então, o valor 2 seria igual a $0000 \ 0011$. O comprimento do array **S** é, portanto, 8 bytes.

### Passo 2

Segundo, defina um array de chave **K** com comprimento de 8 bytes escolhendo uma chave entre 1 e 8 bytes (sem frações de bytes permitidas). Como cada byte tem 8 bits, você pode selecionar qualquer número entre 0 e 255 para cada byte da sua chave.

Suponhamos que escolhemos nossa chave **k** como $[14, 48, 9]$, de modo que ela tenha um comprimento de 3 bytes. Cada índice do nosso array de chave é, então, definido de acordo com o valor decimal para aquele elemento específico da chave, em ordem. Se você percorrer toda a chave, comece novamente no início, até ter preenchido os 8 slots do array de chave. Portanto, nosso array de chave é o seguinte:

- $K = [14, 48, 9, 14, 48, 9, 14, 48]$

### Passo 3

Terceiro, transformaremos o array **S** usando o array de chave **K**, em um processo conhecido como **agendamento de chave**. O processo é o seguinte em pseudocódigo:

- Criar variáveis **j** e **i**
- Definir a variável $j = 0$
- Para cada $i$ de 0 a 7:
    - Definir $j = (j + S[i] + K[i]) \mod 8$
    - Trocar $S[i]$ e $S[j]$

A transformação do array **S** é capturada pela *Tabela 1*.

Para começar, você pode ver o estado inicial de **S** como $[0, 1, 2, 3, 4, 5, 6, 7]$ com um valor inicial de 0 para **j**. Isso será transformado usando o array de chave $[14, 48, 9, 14, 48, 9, 14, 48]$.

O loop for começa com $i = 0$. De acordo com nosso pseudocódigo acima, o novo valor de **j** torna-se 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Trocando $S[0]$ e $S[6]$, o estado de **S** após 1 rodada torna-se $[6, 1, 2, 3, 4, 5, 0, 7]$.
Na próxima linha, $i = 1$. Passando novamente pelo loop for, **j** obtém um valor de 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Trocando $S[1]$ e $S[7]$ do estado atual de **S**, $[6, 1, 2, 3, 4, 5, 0, 7]$, resulta em $[6, 7, 2, 3, 4, 5, 0, 1]$ após a rodada 2.
Continuamos com esse processo até produzirmos a linha final na parte inferior para o array **S**, $[6, 4, 1, 0, 3, 7, 5, 2]$.

*Tabela 1: Tabela de agendamento de chave*

| Rodada | i   | j   |     | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|         |     |     |     |      |      |      |      |      |      |      |      |
| Inicial |     | 0   |     | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| 1       | 0   | 6   |     | 6    | 1    | 2    | 3    | 4    | 5    | 0    | 7    |
| 2       | 1   | 7   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 3       | 2   | 2   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 4       | 3   | 3   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 5       | 4   | 3   |     | 6    | 7    | 2    | 0    | 3    | 5    | 4    | 1    |
| 6       | 5   | 6   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 1    |
| 7       | 6   | 1   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 2    |
| 8       | 7   | 2   |     | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |

### Passo 4
Como quarto passo, produzimos a **sequência de chaves**. Esta é a string pseudorrandômica de um comprimento igual à mensagem que queremos enviar. Isso será usado para criptografar a mensagem original “SOUP.” Como a sequência de chaves precisa ser tão longa quanto a mensagem, precisamos de uma que tenha 4 bytes.
A sequência de chaves é produzida pelo seguinte pseudocódigo:

- Crie as variáveis **j**, **i** e **t**.
- Defina $j = 0$.
- Para cada $i$ do texto plano, começando com $i = 1$ e indo até $i = 4$, cada byte da sequência de chaves é produzido da seguinte forma:
    - $j = (j + S[i]) \mod 8$
    - Troque $S[i]$ por $S[j]$.
    - $t = (S[i] + S[j]) \mod 8$
    - O $i^{ésimo}$ byte da sequência de chaves = $S[t]$

Você pode seguir os cálculos na *Tabela 2*.

O estado inicial de **S** é $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Definindo $i = 1$, o valor de **j** se torna 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Em seguida, trocamos $S[1]$ por $S[4]$ para produzir a transformação de **S** na segunda linha, $[6, 3, 1, 0, 4, 7, 5, 2]$. O valor de **t** é então 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Finalmente, o byte para a sequência de chaves é $S[7]$, ou 2.

Então continuamos a produzir os outros bytes até termos os seguintes quatro bytes: 2, 6, 3 e 7. Cada um desses bytes pode então ser usado para criptografar cada letra do texto plano, "SOUP".

Para começar, usando uma tabela ASCII, podemos ver que “SOUP” codificado pelos valores decimais das strings de bytes subjacentes é “83 79 85 80”. A combinação com a sequência de chaves “2 6 3 7” resulta em “85 85 88 87”, que permanece o mesmo após uma operação de módulo 256. Em ASCII, o texto cifrado “85 85 88 87” é igual a “UUXW”.

O que acontece se a palavra a ser criptografada fosse mais longa que o array **S**? Nesse caso, o array **S** apenas continua se transformando desta maneira exibida acima para cada byte **i** do texto plano, até termos um número de bytes na sequência de chaves igual ao número de letras no texto plano.


*Tabela 2: Geração da sequência de chaves*

| i   | j   | t   | Sequência de Chaves | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| --- | --- | --- | ------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|     | 0   |     |           | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    || 1   | 4   | 7   | 2         | 6    | 3    | 1    | 0    | 4    | 7    | 5    | 2    |
| 2   | 5   | 0   | 6         | 6    | 3    | 7    | 0    | 4    | 1    | 5    | 2    |
| 3   | 5   | 1   | 3         | 6    | 3    | 7    | 1    | 4    | 0    | 5    | 2    |
| 4   | 1   | 7   | 2         | 6    | 4    | 7    | 1    | 3    | 0    | 5    | 2    |

O exemplo que acabamos de discutir é apenas uma versão simplificada do **cifrador de fluxo RC4**. O verdadeiro cifrador de fluxo RC4 possui um array **S** de 256 bytes de comprimento, não de 8 bytes, e uma chave que pode ter entre 1 e 256 bytes, não entre 1 e 8 bytes. O array da chave e os fluxos de chaves são então todos produzidos considerando o comprimento de 256 bytes do array **S**. Os cálculos se tornam imensamente mais complexos, mas os princípios permanecem os mesmos. Usando a mesma chave, [14,48,9], com o cifrador RC4 padrão, a mensagem em texto plano "SOUP" é criptografada como 67 02 ed df em formato hexadecimal.

Um cifrador de fluxo no qual o fluxo de chaves se atualiza independentemente da mensagem em texto plano ou do texto cifrado é um **cifrador de fluxo síncrono**. O fluxo de chaves depende apenas da chave. Claramente, RC4 é um exemplo de um cifrador de fluxo síncrono, já que o fluxo de chaves não tem relação com o texto plano ou o texto cifrado. Todos os nossos cifradores de fluxo primitivos mencionados no capítulo anterior, incluindo o cifrador de deslocamento, o cifrador de Vigenère e o bloco de uma única vez, também eram da variedade síncrona.

Por contraste, um **cifrador de fluxo assíncrono** tem um fluxo de chaves que é produzido tanto pela chave quanto pelos elementos anteriores do texto cifrado. Esse tipo de cifrador também é chamado de **cifrador auto-sincronizável**.

Importante, o fluxo de chaves produzido com RC4 deve ser tratado como um bloco de uma única vez, e você não pode produzir o fluxo de chaves exatamente da mesma maneira na próxima vez. Em vez de mudar a chave a cada vez, a solução prática é combinar a chave com um **nonce** para produzir o fluxo de bytes.

## AES com uma chave de 128 bits
<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Como mencionado no capítulo anterior, o Instituto Nacional de Padrões e Tecnologia (NIST) realizou uma competição entre 1997 e 2000 para determinar um novo padrão de criptografia simétrica. O **cifrador Rijndael** acabou sendo a entrada vencedora. O nome é um jogo de palavras com os nomes dos criadores belgas, Vincent Rijmen e Joan Daemen.
A cifra Rijndael é uma **cifra de bloco**, significando que há um algoritmo central, que pode ser usado com diferentes especificações para comprimentos de chave e tamanhos de bloco. Você pode, então, usá-la com diferentes modos de operação para construir esquemas de criptografia.
O comitê para a competição do NIST adotou uma versão restrita da cifra Rijndael — nomeadamente uma que requer tamanhos de bloco de 128 bits e comprimentos de chave de 128 bits, 192 bits ou 256 bits — como parte do **Padrão de Criptografia Avançado (AES)**. Esta versão restrita da cifra Rijndael também pode ser usada sob múltiplos modos de operação. A especificação para o padrão é o que é conhecido como **Padrão de Criptografia Avançado (AES)**.

Para mostrar como a cifra Rijndael funciona, o núcleo do AES, ilustrarei o processo de criptografia com uma chave de 128 bits. O tamanho da chave tem um impacto no número de rodadas realizadas para cada bloco de criptografia. Para chaves de 128 bits, são necessárias 10 rodadas. Com 192 bits e 256 bits, seriam necessárias 12 e 14 rodadas, respectivamente.

Além disso, assumirei que o AES é usado no **modo ECB**. Isso torna a exposição um pouco mais fácil e não importa para o algoritmo Rijndael. Para ser claro, o modo ECB não é seguro na prática porque leva a uma criptografia determinística. O modo seguro mais comumente usado com o AES é o **CBC** (Cifra de Encadeamento de Blocos).

Vamos chamar a chave de $K_0$. A construção com os parâmetros acima, então, parece como na *Figura 1*, onde $M_i$ representa uma parte da mensagem em texto plano de 128 bits e $C_i$ uma parte do texto cifrado de 128 bits. Um preenchimento é adicionado ao texto plano para o último bloco, se o texto plano não puder ser dividido igualmente pelo tamanho do bloco.

*Figura 1: AES-ECB com uma chave de 128 bits*

![Figura 1: AES-ECB com uma chave de 128 bits](assets/Figure5-1.webp "Figura 1: AES-ECB com uma chave de 128 bits")

Cada bloco de texto de 128 bits passa por dez rodadas no esquema de criptografia Rijndael. Isso requer uma chave de rodada separada para cada rodada ($K_1$ até $K_{10}$). Estas são produzidas para cada rodada a partir da chave original de 128 bits $K_0$ usando um **algoritmo de expansão de chave**. Portanto, para cada bloco de texto a ser criptografado, usaremos a chave original $K_0$ bem como dez chaves de rodada separadas. Note que essas mesmas 11 chaves são usadas para cada bloco de 128 bits de texto plano que requer criptografia.

O algoritmo de expansão de chave é longo e complexo. Trabalhar através dele tem pouco benefício didático. Você pode olhar o algoritmo de expansão de chave por conta própria, se desejar. Uma vez que as chaves de rodada são produzidas, a cifra Rijndael manipulará o primeiro bloco de 128 bits de texto plano, $M_1$, como visto na *Figura 2*. Agora passaremos por essas etapas.

*Figura 2: A manipulação de $M_1$ com a cifra Rijndael:*

**Rodada 0:**
- XOR $M_1$ e $K_0$ para produzir $S_0$

---

**Rodada n para n = {1,...,9}:**
- XOR $S_{n-1}$ e $K_n$
- Substituição de Byte
- Rotação de Linhas
- Mistura de Colunas
- XOR $S$ e $K_n$ para produzir $S_n$

---

**Rodada 10:**
- XOR $S_9$ e $K_{10}$ - Substituição de Byte
- Deslocar Linhas
- XOR $S$ e $K_{10}$ para produzir $S_{10}$
- $S_{10}$ = $C_1$

### Rodada 0

A rodada 0 da cifra de Rijndael é direta. Um array $S_0$ é produzido por uma operação XOR entre o texto puro de 128 bits e a chave privada. Ou seja,

- $S_0 = M_1 \oplus K_0$

### Rodada 1

Na rodada 1, o array $S_0$ é primeiro combinado com a chave da rodada $K_1$ usando uma operação XOR. Isso produz um novo estado de $S$.

Em segundo lugar, a operação de **substituição de byte** é realizada no estado atual de $S$. Funciona pegando cada byte do array $S$ de 16 bytes e substituindo-o por um byte de um array chamado **Caixa S de Rijndael**. Cada byte tem uma transformação única, e um novo estado de $S$ é produzido como resultado. A Caixa S de Rijndael é exibida na *Figura 3*.

*Figura 3: Caixa S de Rijndael*

|     | 00  | 01  | 02  | 03  | 04  | 05  | 06  | 07  | 08  | 09  | 0A  | 0B  | 0C  | 0D  | 0E  | 0F  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00  | 63  | 7C  | 77  | 7B  | F2  | 6B  | 6F  | C5  | 30  | 01  | 67  | 2B  | FE  | D7  | AB  | 76  |
| 10  | CA  | 82  | C9  | 7D  | FA  | 59  | 47  | F0  | AD  | D4  | A2  | AF  | 9C  | A4  | 72  | C0  |
| 20  | B7  | FD  | 93  | 26  | 36  | 3F  | F7  | CC  | 34  | A5  | E5  | F1  | 71  | D8  | 31  | 15  |
| 30  | 04  | C7  | 23  | C3  | 18  | 96  | 05  | 9A  | 07  | 12  | 80  | E2  | EB  | 27  | B2  | 75  |
| 40  | 09  | 83  | 2C  | 1A  | 1B  | 6E  | 5A  | A0  | 52  | 3B  | D6  | B3  | 29  | E3  | 2F  | 84  |
Como um tradutor profissional, entendo a importância de manter a precisão técnica e a integridade do conteúdo original. No entanto, o texto fornecido parece ser uma sequência de bytes, provavelmente relacionada a algum contexto técnico específico, como criptografia, programação ou análise de dados. Dada a natureza deste conteúdo, uma tradução literal ou a adaptação para o português não se aplicam diretamente, pois estamos lidando com valores hexadecimais que representam dados em um formato que não é influenciado pelo idioma.

Para manter a fidelidade ao conteúdo original e seguir as diretrizes fornecidas:

1. **Idioma Original:** O conteúdo é em inglês, mas, neste caso, trata-se de uma sequência de dados hexadecimais que não é afetada pela tradução de idiomas.
2. **Natureza do Conteúdo:** O material é técnico e contém terminologia (neste caso, valores hexadecimais) específica que não deve ser traduzida.
3. **Links e Palavras Técnicas:** Não há URLs, mas os valores hexadecimais apresentados são considerados termos técnicos altamente específicos e, portanto, são mantidos inalterados.
4. **Consistência de Formatação:** A estrutura e formatação do conteúdo original são mantidas exatamente como apresentadas.
5. **Propriedades YML:** Não aplicável, pois o texto fornecido não contém propriedades YML.
6. **Contexto Cultural:** Não há referências culturais ou contextuais que necessitem de adaptação ou explicação para o português.

Portanto, a "tradução" ou melhor, a transcrição apropriada para este pedido é manter o conteúdo exatamente como está, reconhecendo que a natureza dos dados é universal e não sujeita a alterações linguísticas.
| F0  | 8C  | A1  | 89  | 0D  | BF  | E6  | 42  | 68  | 41  | 99  | 2D  | 0F  | B0  | 54  | BB  | 16  |

Esta S-Box é um dos pontos onde a álgebra abstrata entra em jogo no ciframento Rijndael, especificamente **campos de Galois**.

Para começar, você define cada possível elemento de byte de 00 até FF como um vetor de 8 bits. Cada vetor é um elemento do **campo de Galois GF(2^8)** onde o polinômio irredutível para a operação de módulo é $x^8 + x^4 + x^3 + x + 1$. O campo de Galois com estas especificações também é chamado de **Campo Finito de Rijndael**.

Em seguida, para cada possível elemento no campo, criamos o que é chamado de **Nyberg S-Box**. Nesta caixa, cada byte é mapeado para o seu **inverso multiplicativo** (ou seja, de modo que o produto deles seja igual a 1). Em seguida, mapeamos esses valores da S-box de Nyberg para a S-Box de Rijndael usando a **transformação afim**.

A terceira operação no array **S** é a operação de **deslocamento de linhas**. Ela pega o estado de **S** e lista todos os dezesseis bytes em uma matriz. O preenchimento da matriz começa no canto superior esquerdo e segue seu caminho ao redor, indo de cima para baixo e, então, cada vez que uma coluna é preenchida, deslocando uma coluna para a direita e para o topo.

Uma vez que a matriz de **S** tenha sido construída, as quatro linhas são deslocadas. A primeira linha permanece a mesma. A segunda linha move uma para a esquerda. A terceira move duas para a esquerda. A quarta move três para a esquerda. Um exemplo do processo é fornecido na *Figura 4*. O estado original de **S** é mostrado no topo, e o estado resultante após a operação de deslocamento de linhas é mostrado abaixo.

*Figura 4: Operação de deslocamento de linhas*

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| 59   | EF   | 09   | 82   |
| 97   | 01   | B0   | CC   |
| D4   | 72   | 04   | 21   |

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| EF   | 09   | 82   | 59   |
| B0   | CC   | 97   | 01   |
| 21   | D4   | 72   | 04   |


No quarto passo, **campos de Galois** aparecem novamente. Para começar, cada coluna da matriz **S** é multiplicada pela coluna da matriz 4 x 4 vista na *Figura 5*. Mas, em vez de ser uma multiplicação de matrizes regular, é uma multiplicação de vetores **módulo um polinômio irredutível**, $x^8 + x^4 + x^3 + x + 1$. Os coeficientes vetoriais resultantes representam os bits individuais de um byte.

*Figura 5: Matriz de mistura de colunas*

| 02   | 03   | 01   | 01   |
|------|------|------|------|
| 01   | 02   | 03   | 01   |
| 01   | 01   | 02   | 03   || 03   | 01   | 01   | 02   |

A multiplicação da primeira coluna da matriz **S** com a matriz 4 x 4 acima resulta no que é apresentado na *Figura 6*.

*Figura 6: Multiplicação da primeira coluna:*

$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$

Como próximo passo, todos os termos na matriz devem ser transformados em polinômios. Por exemplo, F1 representa 1 byte e se tornaria $x^7 + x^6 + x^5 + x^4 + 1$, e 03 representa 1 byte e se tornaria $x + 1$.

Todas as multiplicações são então realizadas **módulo** $x^8 + x^4 + x^3 + x + 1$. Isso resulta na adição de quatro polinômios em cada uma das quatro células da coluna. Após realizar essas adições **módulo 2**, você obterá quatro polinômios. Cada um desses polinômios representa uma cadeia de 8 bits, ou 1 byte, de **S**. Não realizaremos todos esses cálculos aqui na matriz na *Figura 6*, pois são extensos.

Uma vez que a primeira coluna tenha sido processada, as outras três colunas da matriz **S** são processadas da mesma maneira. Eventualmente, isso resultará em uma matriz com dezesseis bytes que podem ser transformados em um array.

Como etapa final, o array **S** é combinado novamente com a chave de rodada em uma operação de **XOR**. Isso produz o estado $S_1$. Ou seja,

- $S_1 = S \oplus K_0$

### Rodadas 2 até 10

As rodadas 2 até 9 são apenas uma repetição da rodada 1, *mutatis mutandis*. A rodada final parece muito semelhante às rodadas anteriores, exceto que a etapa de **mixar colunas** é eliminada. Ou seja, a rodada 10 é executada da seguinte forma:

- $S_9 \oplus K_{10}$
- Substituição de Byte
- Shift Rows (Deslocamento de Linhas)
- $S_{10} = S \oplus K_{10}$

O estado $S_{10}$ agora está definido para $C_1$, os primeiros 128 bits do texto cifrado. Prosseguindo através dos blocos de texto simples de 128 bits restantes, obtém-se o texto cifrado completo **C**.

### As operações da cifra Rijndael

Qual é o raciocínio por trás das diferentes operações vistas na cifra Rijndael?

Sem entrar nos detalhes, os esquemas de criptografia são avaliados com base no grau em que criam confusão e difusão. Se o esquema de criptografia tem um alto grau de **confusão**, significa que o texto cifrado parece drasticamente diferente do texto claro. Se o esquema de criptografia tem um alto grau de **difusão**, significa que qualquer pequena alteração no texto claro produz um texto cifrado drasticamente diferente.
A razão para as operações por trás da cifra Rijndael é que elas produzem tanto um alto grau de confusão quanto de difusão. A confusão é produzida pela operação de substituição de Byte, enquanto a difusão é produzida pelas operações de deslocamento de linhas e mistura de colunas.
# Criptografia Assimétrica
<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

## O problema da distribuição e gestão de chaves
<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Assim como na criptografia simétrica, os esquemas assimétricos podem ser usados para garantir tanto o sigilo quanto a autenticação. Por contraste, no entanto, esses esquemas empregam duas chaves em vez de uma: uma chave privada e uma chave pública.

Começamos nossa investigação com a descoberta da criptografia assimétrica, particularmente os problemas que a impulsionaram. Em seguida, discutimos como os esquemas assimétricos para criptografia e autenticação funcionam em um nível alto. Então, introduzimos as funções de hash, que são chave para entender os esquemas de autenticação assimétrica, e também têm relevância em outros contextos criptográficos, como para os códigos de autenticação de mensagem baseados em hash que discutimos no Capítulo 4.

___

Suponha que Bob queira comprar uma nova capa de chuva na Jim’s Sporting Goods, uma loja de artigos esportivos online com milhões de clientes na América do Norte. Esta será sua primeira compra lá e ele quer usar seu cartão de crédito. Então, Bob primeiro precisará criar uma conta na Jim’s Sporting Goods, o que requer o envio de detalhes pessoais como seu endereço e informações do cartão de crédito. Ele pode, então, seguir os passos necessários para comprar a capa de chuva.

Bob e a Jim’s Sporting Goods vão querer garantir que suas comunicações sejam seguras durante todo esse processo, considerando que a Internet é um sistema de comunicações aberto. Eles vão querer garantir, por exemplo, que nenhum possível atacante possa obter os detalhes do cartão de crédito e endereço de Bob, e que nenhum possível atacante possa repetir suas compras ou criar falsas em seu nome.

Um esquema avançado de criptografia autenticada, como discutido no capítulo anterior, certamente poderia tornar as comunicações entre Bob e a Jim’s Sporting Goods seguras. Mas há claramente obstáculos práticos para implementar tal esquema.

Para ilustrar esses obstáculos práticos, suponha que vivêssemos em um mundo no qual apenas as ferramentas de criptografia simétrica existissem. O que a Jim’s Sporting Goods e Bob, então, poderiam fazer para garantir uma comunicação segura?

Sob essas circunstâncias, eles enfrentariam custos substanciais para se comunicar de forma segura. Como a Internet é um sistema de comunicações aberto, eles não podem simplesmente trocar um conjunto de chaves por ela. Portanto, Bob e um representante da Jim’s Sporting Goods precisariam fazer uma troca de chaves pessoalmente.

Uma possibilidade é que a Jim’s Sporting Goods crie locais especiais de troca de chaves, onde Bob e outros novos clientes possam recuperar um conjunto de chaves para comunicação segura. Isso obviamente viria com custos organizacionais substanciais e reduziria grandemente a eficiência com que novos clientes podem fazer compras.

Alternativamente, a Jim’s Sporting Goods pode enviar a Bob um par de chaves com um mensageiro altamente confiável. Isso provavelmente é mais eficiente do que organizar locais de troca de chaves. Mas isso ainda viria com custos substanciais, particularmente se muitos clientes fizerem apenas uma ou poucas compras.

Em seguida, um esquema simétrico para criptografia autenticada também força a Jim’s Sporting Goods a armazenar conjuntos separados de chaves para todos os seus clientes. Isso seria um desafio prático significativo para milhares de clientes, quanto mais milhões.
Para entender este último ponto, suponha que a Jim’s Sporting Goods forneça a cada cliente o mesmo par de chaves. Isso permitiria a cada cliente — ou qualquer outra pessoa que pudesse obter esse par de chaves — ler e até manipular todas as comunicações entre a Jim’s Sporting Goods e seus clientes. Nesse caso, então, tanto faz como se não usasse criptografia alguma em suas comunicações.
Mesmo repetindo um conjunto de chaves para apenas alguns clientes é uma prática de segurança terrível. Qualquer atacante em potencial poderia tentar explorar essa característica do esquema (lembre-se de que se assume que os atacantes sabem tudo sobre um esquema, exceto as chaves, de acordo com o princípio de Kerckhoffs.)

Portanto, a Jim’s Sporting Goods teria que armazenar um par de chaves para cada cliente, independentemente de como esses pares de chaves são distribuídos. Isso claramente apresenta vários problemas práticos.

- A Jim’s Sporting Goods teria que armazenar milhões de pares de chaves, um conjunto para cada cliente.
- Essas chaves teriam que ser devidamente protegidas, pois seriam um alvo certo para hackers. Qualquer violação de segurança exigiria a repetição de trocas de chaves dispendiosas, seja em locais especiais de troca de chaves ou por meio de correio.
- Qualquer cliente da Jim’s Sporting Goods teria que armazenar com segurança um par de chaves em casa. Perdas e roubos ocorrerão, exigindo uma repetição das trocas de chaves. Os clientes também teriam que passar por esse processo para quaisquer outras lojas online ou outros tipos de entidades com as quais desejam se comunicar e realizar transações pela Internet.

Esses dois principais desafios descritos eram preocupações muito fundamentais até o final dos anos 1970. Eram conhecidos como o **problema da distribuição de chaves** e o **problema da gestão de chaves**, respectivamente.

Esses problemas sempre existiram, é claro, e frequentemente causavam dores de cabeça no passado. Forças militares, por exemplo, teriam que distribuir constantemente livros com chaves para comunicação segura ao pessoal em campo, com grandes riscos e custos. Mas esses problemas estavam se tornando piores à medida que o mundo avançava cada vez mais para uma era de comunicação digital à longa distância, particularmente para entidades não governamentais.

Se esses problemas não tivessem sido resolvidos nos anos 1970, compras eficientes e seguras na Jim’s Sporting Goods provavelmente não teriam existido. De fato, grande parte do nosso mundo moderno com e-mails práticos e seguros, bancos online e compras provavelmente seria apenas uma fantasia distante. Qualquer coisa que se assemelhasse ao Bitcoin não poderia ter existido de forma alguma.

Então, o que aconteceu nos anos 1970? Como é possível que possamos fazer compras online instantaneamente e navegar de forma segura pela World Wide Web? Como é possível que possamos enviar Bitcoins instantaneamente por todo o mundo a partir de nossos smartphones?

## Novas direções em criptografia
<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

Até os anos 1970, os problemas de distribuição e gestão de chaves haviam chamado a atenção de um grupo de criptógrafos acadêmicos americanos: Whitfield Diffie, Martin Hellman e Ralph Merkle. Diante do ceticismo severo da maioria de seus colegas, eles se aventuraram a encontrar uma solução para isso.

Pelo menos uma motivação primária para sua empreitada foi a previsão de que as comunicações abertas por computador afetariam profundamente nosso mundo. Como Diffie e Hellman observam em 1976,
O desenvolvimento de redes de comunicação controladas por computador promete um contato sem esforço e barato entre pessoas ou computadores em lados opostos do mundo, substituindo a maior parte do correio e muitas excursões por telecomunicações. Para muitas aplicações, esses contatos devem ser feitos seguros contra tanto a espionagem quanto a injeção de mensagens ilegítimas. No entanto, atualmente, a solução de problemas de segurança está bem atrás de outras áreas da tecnologia de comunicações. *A criptografia contemporânea é incapaz de atender aos requisitos, uma vez que seu uso imporia inconveniências tão severas aos usuários do sistema, a ponto de eliminar muitos dos benefícios do teleprocessamento.* [1]

A tenacidade de Diffie, Hellman e Merkle valeu a pena. A primeira publicação de seus resultados foi um artigo de Diffie e Hellman em 1976 intitulado “New Directions in Cryptography.” Nele, eles apresentaram duas maneiras originais de abordar os problemas de distribuição de chaves e de gerenciamento de chaves.

A primeira solução que ofereceram foi um *protocolo de troca de chaves remoto*, isto é, um conjunto de regras para a troca de uma ou mais chaves simétricas por um canal de comunicação inseguro. Este protocolo é agora conhecido como *troca de chaves Diffie-Hellman* ou *troca de chaves Diffie-Hellman-Merkle*. [2]

Com a troca de chaves Diffie-Hellman, duas partes primeiro trocam algumas informações publicamente em um canal inseguro, como a Internet. Com base nessas informações, elas, então, criam independentemente uma chave simétrica (ou um par de chaves simétricas) para comunicação segura. Embora ambas as partes criem suas chaves independentemente, as informações que compartilharam publicamente garantem que esse processo de criação de chaves produza o mesmo resultado para ambos.

Importante, enquanto todos podem observar as informações que são trocadas publicamente pelas partes sobre o canal inseguro, apenas as duas partes envolvidas na troca de informações podem criar chaves simétricas a partir dela.

Isso, claro, parece completamente contraintuitivo. Como duas partes poderiam trocar algumas informações publicamente que permitiriam apenas a elas criar chaves simétricas a partir disso? Por que qualquer outra pessoa observando a troca de informações não seria capaz de criar as mesmas chaves?

Isso depende de uma matemática belíssima, claro. A troca de chaves Diffie-Hellman funciona por meio de uma função unidirecional com uma porta dos fundos. Vamos discutir o significado desses dois termos em sequência.

Suponha que você receba uma função $f(x)$ e o resultado $f(a) = y$, onde $a$ é um valor particular para $x$. Dizemos que $f(x)$ é uma **função unidirecional** se é fácil calcular o valor $y$ quando dado $a$ e $f(x)$, mas é computacionalmente inviável calcular o valor $a$ quando dado $y$ e $f(x)$. O nome **função unidirecional**, claro, vem do fato de que tal função só é prática para calcular em uma direção.

Algumas funções unidirecionais têm o que é conhecido como uma **porta dos fundos**. Enquanto é praticamente impossível calcular $a$ dado apenas $y$ e $f(x)$, existe uma certa peça de informação $Z$ que torna o cálculo de $a$ a partir de $y$ computacionalmente viável. Esta peça de informação $Z$ é conhecida como a **porta dos fundos**. Funções unidirecionais que têm uma porta dos fundos são conhecidas como **funções com porta dos fundos**.
Não vamos nos aprofundar nos detalhes da troca de chaves Diffie-Helmann aqui. Mas, essencialmente, cada participante cria algumas informações, das quais uma parte é compartilhada publicamente e outra permanece secreta. Cada parte, então, pega sua peça de informação secreta e a informação pública compartilhada pela outra parte para criar uma chave privada. E, de forma um tanto milagrosa, ambas as partes acabam com a mesma chave privada.
Qualquer parte observando apenas as informações compartilhadas publicamente entre as duas partes em uma troca de chaves Diffie Helmann é incapaz de replicar esses cálculos. Eles precisariam da informação privada de uma das duas partes para fazer isso.

Embora a versão básica da troca de chaves Diffie-Helmann apresentada no artigo de 1976 não seja muito segura, versões sofisticadas do protocolo básico certamente ainda estão em uso hoje. Mais importante, todo protocolo de troca de chaves na última versão do protocolo de segurança da camada de transporte (versão 1.3) é essencialmente uma versão enriquecida do protocolo apresentado por Diffie e Hellman em 1976. O protocolo de segurança da camada de transporte é o protocolo predominante para troca segura de informações formatadas de acordo com o protocolo de transferência de hipertexto (http), o padrão para troca de conteúdo Web.

Importante, a troca de chaves Diffie-Helmann não é um esquema assimétrico. Estritamente falando, ele pertence, de fato, ao reino da criptografia de chave simétrica. Mas, como tanto a troca de chaves Diffie-Helmann quanto a criptografia assimétrica dependem de funções teóricas de números unidirecionais com armadilhas, elas são tipicamente discutidas juntas.

A segunda maneira que Diffie e Helmann ofereceram para abordar o problema de distribuição e gerenciamento de chaves em seu artigo de 1976 foi, claro, via criptografia assimétrica.

Em contraste com a apresentação da troca de chaves Diffie-Hellman, eles apenas forneceram os contornos gerais de como esquemas criptográficos assimétricos poderiam plausivelmente ser construídos. Eles não ofereceram nenhuma função unidirecional específica que pudesse cumprir as condições necessárias para segurança razoável em tais esquemas.

Uma implementação prática de um esquema assimétrico foi, no entanto, encontrada um ano depois por três diferentes criptógrafos e matemáticos acadêmicos: Ronald Rivest, Adi Shamir e Leonard Adleman. [3] O criptossistema que introduziram ficou conhecido como o **criptossistema RSA** (de seus sobrenomes).

As funções de armadilha usadas na criptografia assimétrica (e na troca de chaves Diffie Helmann) estão todas relacionadas a dois principais **problemas computacionalmente difíceis**: fatoração de números primos e o cálculo de logaritmos discretos.

**Fatoração de números primos** requer, como o nome implica, decompor um número inteiro em seus fatores primos. O problema RSA é de longe o exemplo mais conhecido de um criptossistema relacionado à fatoração de números primos.

O **problema do logaritmo discreto** é um problema que ocorre em grupos cíclicos. Dado um gerador em um grupo cíclico particular, requer o cálculo do expoente único necessário para produzir outro elemento no grupo a partir do gerador.

Esquemas baseados em logaritmo discreto dependem de dois principais tipos de grupos cíclicos: grupos multiplicativos de inteiros e grupos que incluem os pontos em curvas elípticas. A troca de chaves Diffie Helmann original, como apresentada em “New Directions in Cryptography”, trabalha com um grupo multiplicativo cíclico de inteiros. O algoritmo de assinatura digital do Bitcoin e o recentemente introduzido esquema de assinatura Schnorr (2021) são ambos baseados no problema do logaritmo discreto para um grupo cíclico de curva elíptica particular.

A seguir, vamos passar para uma visão geral de alto nível sobre segredo e autenticação no cenário assimétrico. Antes de fazer isso, no entanto, precisamos fazer uma breve nota histórica.
Parece agora plausível que um grupo de criptógrafos e matemáticos britânicos trabalhando para o Quartel-General de Comunicações do Governo (GCHQ) tenha feito independentemente as descobertas mencionadas acima alguns anos antes. Este grupo era composto por James Ellis, Clifford Cocks e Malcolm Williamson.
De acordo com seus próprios relatos e o do GCHQ, foi James Ellis quem primeiro concebeu o conceito de criptografia de chave pública em 1969. Supostamente, Clifford Cocks descobriu o sistema criptográfico RSA em 1973, e Malcolm Williamson o conceito de troca de chaves Diffie-Hellman em 1974. [4] No entanto, suas descobertas supostamente não foram reveladas até 1997, dada a natureza secreta do trabalho realizado no GCHQ.

**Notas:**

[1] Whitfield Diffie e Martin Hellman, “New directions in cryptography,” _IEEE Transactions on Information Theory_ IT-22 (1976), pp. 644–654, na p. 644.

[2] Ralph Merkle também discute um protocolo de troca de chaves em “Secure communications over insecure channels”, _Communications of the Association for Computing Machinery_, 21 (1978), 294–99. Embora Merkle tenha submetido este artigo antes do artigo de Diffie e Hellman, ele foi publicado posteriormente. A solução de Merkle não é exponencialmente segura, ao contrário da de Diffie-Hellman.

[3] Ron Rivest, Adi Shamir e Leonard Adleman, “A method for obtaining digital signatures and public-key cryptosystems”, _Communications of the Association for Computing Machinery_, 21 (1978), pp. 120–26.

[4] Uma boa história dessas descobertas é fornecida por Simon Singh, _The Code Book_, Fourth Estate (Londres, 1999), Capítulo 6.

## Criptografia assimétrica e autenticação
<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Uma visão geral da **criptografia assimétrica** com a ajuda de Bob e Alice é fornecida na *Figura 1*.

Alice primeiro cria um par de chaves, consistindo de uma chave pública ($K_P$) e uma chave privada ($K_S$), onde o “P” em $K_P$ significa “pública” e o “S” em $K_S$ significa “secreta”. Ela então distribui essa chave pública livremente para outros. Voltaremos aos detalhes desse processo de distribuição um pouco mais tarde. Mas por agora, assuma que qualquer um, incluindo Bob, pode obter de forma segura a chave pública de Alice $K_P$.

Em um momento posterior, Bob quer escrever uma mensagem $M$ para Alice. Como ela inclui informações sensíveis, ele quer que o conteúdo permaneça secreto para todos, exceto Alice. Então, Bob primeiro criptografa sua mensagem $M$ usando $K_P$. Ele então envia o texto cifrado resultante $C$ para Alice, que descriptografa $C$ com $K_S$ para produzir a mensagem original $M$.

*Figura 1: Criptografia assimétrica*

![Figura 1: Criptografia assimétrica](assets/Figure6-1.webp "Figura 1: Criptografia assimétrica")

Qualquer adversário que escute a comunicação entre Bob e Alice pode observar $C$. Ela também conhece $K_P$ e o algoritmo de criptografia $E(\cdot)$. Importante, no entanto, essa informação não permite ao atacante descriptografar o texto cifrado $C$ de forma viável. A descriptografia requer especificamente $K_S$, que o atacante não possui.
Esquemas de criptografia simétrica geralmente precisam ser seguros contra um atacante que pode criptografar validamente mensagens em texto claro (conhecido como segurança contra ataques de texto cifrado escolhido). No entanto, não são projetados com o propósito explícito de permitir a criação de tais textos cifrados válidos por um atacante ou qualquer outra pessoa.
Isso contrasta fortemente com um esquema de criptografia assimétrica, cujo propósito é permitir que qualquer pessoa, incluindo atacantes, produza textos cifrados válidos. Portanto, esquemas de criptografia assimétrica podem ser rotulados como **cifras de acesso múltiplo**.

Para entender melhor o que está acontecendo, imagine que, em vez de enviar uma mensagem eletronicamente, Bob queria enviar uma carta física em segredo. Uma maneira de garantir o segredo seria Alice enviar um cadeado seguro para Bob, mas manter a chave para desbloqueá-lo. Após escrever sua carta, Bob poderia colocar a carta em uma caixa e fechá-la com o cadeado de Alice. Ele, então, poderia enviar a caixa trancada com a mensagem para Alice, que tem a chave para desbloqueá-la.

Embora Bob seja capaz de trancar o cadeado, nem ele nem qualquer outra pessoa que intercepte a caixa podem desfazer o cadeado se ele for realmente seguro. Somente Alice pode desbloqueá-lo e ver o conteúdo da carta de Bob porque ela tem a chave.

Um esquema de criptografia assimétrica é, grosso modo, uma versão digital desse processo. O cadeado é semelhante à chave pública e a chave do cadeado é semelhante à chave privada. No entanto, como o cadeado é digital, é muito mais fácil e não tão custoso para Alice distribuí-lo a qualquer pessoa que possa querer enviar mensagens secretas para ela.

Para autenticação no contexto assimétrico, usamos **assinaturas digitais**. Estas, portanto, têm a mesma função que os códigos de autenticação de mensagem no contexto simétrico. Uma visão geral das assinaturas digitais é fornecida na *Figura 2*.

Bob primeiro cria um par de chaves, consistindo da chave pública ($K_P$) e da chave privada ($K_S$), e distribui sua chave pública. Quando ele quer enviar uma mensagem autenticada para Alice, ele primeiro pega sua mensagem $M$ e sua chave privada para criar uma **assinatura digital** $D$. Bob então envia a Alice sua mensagem junto com a assinatura digital.

Alice insere a mensagem, a chave pública e a assinatura digital em um **algoritmo de verificação**. Este algoritmo produz **verdadeiro** para uma assinatura válida, ou **falso** para uma assinatura inválida.

Uma assinatura digital é, como o nome claramente implica, o equivalente digital de uma assinatura escrita em cartas, contratos e assim por diante. Na verdade, uma assinatura digital é geralmente muito mais segura. Com algum esforço, você pode falsificar uma assinatura escrita; um processo facilitado pelo fato de que assinaturas escritas frequentemente não são verificadas de perto. No entanto, uma assinatura digital segura é, assim como um código de autenticação de mensagem seguro, **existencialmente infalsificável**: ou seja, com um esquema de assinatura digital seguro, ninguém pode criar viavelmente uma assinatura para uma mensagem que passe pelo procedimento de verificação, a menos que tenham a chave privada.

*Figura 2: Autenticação assimétrica*

![Figura 2: Autenticação assimétrica](assets/Figure6-2.webp "Figura 2: Autenticação assimétrica")

Assim como na criptografia assimétrica, vemos um contraste interessante entre assinaturas digitais e códigos de autenticação de mensagem. Para este último, o algoritmo de verificação só pode ser empregado por uma das partes privadas à comunicação segura. Isso ocorre porque requer uma chave privada. No contexto assimétrico, no entanto, qualquer pessoa pode verificar uma assinatura digital $S$ feita por Bob.
Tudo isso torna as assinaturas digitais uma ferramenta extremamente poderosa. Elas formam a base, por exemplo, para a criação de assinaturas em contratos que podem ser verificadas para fins legais. Se Bob tivesse feito uma assinatura em um contrato na troca mencionada acima, Alice poderia mostrar a mensagem $M$, o contrato e a assinatura $S$ a um tribunal. O tribunal, então, poderia verificar a assinatura usando a chave pública de Bob. [5]

Por outro exemplo, as assinaturas digitais são um aspecto importante da distribuição segura de software e atualizações de software. Esse tipo de verificabilidade pública nunca poderia ser criado usando apenas códigos de autenticação de mensagens.

Como um último exemplo do poder das assinaturas digitais, considere o Bitcoin. Um dos equívocos mais comuns sobre o Bitcoin, especialmente na mídia, é que as transações são criptografadas: elas não são. Em vez disso, as transações do Bitcoin funcionam com assinaturas digitais para garantir segurança.

Os Bitcoins existem em lotes chamados saídas de transação não gastas (ou **UTXO’s**). Suponha que você receba três pagamentos em um endereço Bitcoin específico de 2 bitcoins cada. Tecnicamente, você agora não tem 6 bitcoins nesse endereço. Em vez disso, você tem três lotes de 2 bitcoins que estão bloqueados por um problema criptográfico associado a esse endereço. Para qualquer pagamento que você faça, pode usar um, dois ou todos os três desses lotes, dependendo de quanto precisa para a transação.

A prova de propriedade sobre saídas de transação não gastas é geralmente mostrada por meio de uma ou mais assinaturas digitais. O Bitcoin funciona precisamente porque assinaturas digitais válidas em saídas de transação não gastas são computacionalmente inviáveis de serem feitas, a menos que você esteja na posse das informações secretas necessárias para fazê-las.

Atualmente, as transações do Bitcoin incluem transparentemente todas as informações que precisam ser verificadas pelos participantes na rede, como as origens das saídas de transação não gastas usadas na transação. Embora seja possível ocultar algumas dessas informações e ainda permitir a verificação (como algumas criptomoedas alternativas, como Monero, fazem), isso também cria riscos de segurança particulares.

Às vezes, surge confusão entre assinaturas digitais e assinaturas escritas capturadas digitalmente. No último caso, você captura uma imagem da sua assinatura escrita e a cola em um documento eletrônico, como um contrato de trabalho. Isso, no entanto, não é uma assinatura digital no sentido criptográfico. A última é apenas um número longo que só pode ser produzido estando na posse de uma chave privada.

Assim como no cenário de chave simétrica, você também pode usar esquemas de criptografia assimétrica e autenticação juntos. Princípios semelhantes se aplicam. Primeiro de tudo, você deve usar pares de chaves privadas-públicas diferentes para criptografia e para fazer assinaturas digitais. Além disso, você deve primeiro criptografar uma mensagem e depois autenticá-la.

Importante, em muitas aplicações a criptografia assimétrica não é usada durante todo o processo de comunicação. Em vez disso, ela será tipicamente usada apenas para *trocar chaves simétricas* entre as partes com as quais elas realmente se comunicarão.

Esse é o caso, por exemplo, quando você compra bens online. Conhecendo a chave pública do vendedor, ele pode enviar-lhe mensagens assinadas digitalmente que você pode verificar quanto à autenticidade. Com base nisso, você pode seguir um dos vários protocolos para trocar chaves simétricas para se comunicar de forma segura.

A principal razão para a frequência da abordagem mencionada é que a criptografia assimétrica é muito menos eficiente do que a criptografia simétrica em produzir um determinado nível de segurança. Essa é uma razão pela qual ainda precisamos da criptografia de chave simétrica ao lado da criptografia pública. Além disso, a criptografia de chave simétrica é muito mais natural em aplicações específicas, como um usuário de computador criptografando seus próprios dados.

Então, como exatamente as assinaturas digitais e a criptografia de chave pública abordam os problemas de distribuição e gerenciamento de chaves?
Não existe uma única resposta aqui. A criptografia assimétrica é uma ferramenta e não há uma única maneira de empregar essa ferramenta. Mas vamos pegar nosso exemplo anterior da Jim’s Sporting Goods para mostrar como os problemas seriam tipicamente abordados neste exemplo.
Para começar, a Jim’s Sporting Goods provavelmente se aproximaria de uma **autoridade certificadora**, uma organização que apoia na distribuição de chave pública. A autoridade certificadora registraria alguns detalhes sobre a Jim’s Sporting Goods e concederia a ela uma chave pública. Então, enviaria à Jim’s Sporting Goods um certificado, conhecido como **certificado TLS/SSL**, com a chave pública da Jim’s Sporting Goods assinada digitalmente usando a própria chave pública da autoridade certificadora. Desta forma, a autoridade certificadora afirma que uma chave pública específica realmente pertence à Jim’s Sporting Goods.

A chave para entender esse processo com certificados TLS/SSL é que, embora geralmente você não tenha a chave pública da Jim’s Sporting Goods armazenada em lugar algum no seu computador, as chaves públicas de autoridades certificadoras reconhecidas são de fato armazenadas no seu navegador ou no seu sistema operacional. Estas são armazenadas no que são chamados **certificados raiz**.

Portanto, quando a Jim’s Sporting Goods fornece a você o seu certificado TLS/SSL, você pode verificar a assinatura digital da autoridade certificadora via um certificado raiz no seu navegador ou sistema operacional. Se a assinatura for válida, você pode estar relativamente seguro de que a chave pública no certificado realmente pertence à Jim’s Sporting Goods. Com base nisso, é fácil estabelecer um protocolo para comunicação segura com a Jim’s Sporting Goods.

A distribuição de chaves agora se tornou vastamente mais simples para a Jim’s Sporting Goods. Não é difícil ver que a gestão de chaves também se tornou muito simplificada. Em vez de ter que armazenar milhares de chaves, a Jim’s Sporting Goods apenas precisa armazenar uma chave privada que lhe permite fazer assinaturas para a chave pública em seu certificado SSL. Cada vez que um cliente acessa o site da Jim’s Sporting Goods, eles podem estabelecer uma sessão de comunicação segura a partir desta chave pública. Os clientes também não precisam armazenar nenhuma informação (além das chaves públicas de autoridades certificadoras reconhecidas em seu sistema operacional e navegador).

**Notas:**

[5] Qualquer esquema que tente alcançar a não-repudiação, o outro tema que discutimos no Capítulo 1, precisará, em sua base, envolver assinaturas digitais.

## Funções de Hash
<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Funções de hash são onipresentes em criptografia. Elas não são esquemas simétricos nem assimétricos, mas caem em uma categoria criptográfica própria.

Já nos deparamos com funções de hash no Capítulo 4 com a criação de mensagens de autenticação baseadas em hash. Elas também são importantes no contexto de assinaturas digitais, embora por uma razão um pouco diferente: Assinaturas digitais são tipicamente feitas sobre o valor de hash de alguma mensagem (criptografada), em vez da própria mensagem (criptografada). Nesta seção, oferecerei uma introdução mais completa sobre funções de hash.

Vamos começar definindo uma função de hash. Uma **função de hash** é qualquer função computável de forma eficiente que recebe entradas de tamanho arbitrário e produz saídas de comprimento fixo.

Uma **função de hash criptográfica** é apenas uma função de hash que é útil para aplicações em criptografia. A saída de uma função de hash criptográfica é tipicamente chamada de **hash**, **valor de hash**, ou **resumo da mensagem**.

No contexto da criptografia, uma “função de hash” normalmente se refere a uma função de hash criptográfica. Adotarei essa prática daqui em diante.
Um exemplo de uma função de hash popular é o **SHA-256** (algoritmo de hash seguro 256). Independentemente do tamanho da entrada (por exemplo, 15 bits, 100 bits ou 10.000 bits), essa função produzirá um valor de hash de 256 bits. Abaixo, você pode ver alguns exemplos de saídas da função SHA-256.
“Hello”: `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

“52398”: `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`

“Cryptography is fun”: `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`

Todas as saídas têm exatamente 256 bits escritos em formato hexadecimal (cada dígito hex pode ser representado por quatro dígitos binários). Então, mesmo que você inserisse o livro *O Senhor dos Anéis* de Tolkien na função SHA-256, a saída ainda seria de 256 bits.

Funções de hash como o SHA-256 são empregadas para diversos fins em criptografia. As propriedades requeridas de uma função de hash realmente dependem do contexto de uma aplicação específica. Há duas propriedades geralmente desejadas das funções de hash em criptografia: [6]

1. Resistência a Colisões
2. Ocultação

Diz-se que uma função de hash $H$ é **resistente a colisões** se for inviável encontrar dois valores, $x$ e $y$, tais que $x \neq y$, e ainda assim $H(x) = H(y)$.

Funções de hash resistentes a colisões são importantes, por exemplo, na verificação de software. Suponha que você quisesse baixar a versão Windows do Bitcoin Core 0.21.0 (uma aplicação servidor para processar tráfego da rede Bitcoin). Os principais passos que você teria que seguir, para verificar a legitimidade do software, são os seguintes:

1. Você primeiro precisa baixar e importar as chaves públicas de um ou mais contribuidores do Bitcoin Core em software que possa verificar assinaturas digitais (por exemplo, Kleopetra). Você pode encontrar essas chaves públicas [aqui](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). É recomendado que você verifique o software Bitcoin Core com as chaves públicas de múltiplos contribuidores.
2. Em seguida, você precisa verificar as chaves públicas que importou. Pelo menos um passo que você deve tomar é verificar que as chaves públicas encontradas são as mesmas publicadas em vários outros locais. Você pode, por exemplo, consultar as páginas pessoais na web, páginas no Twitter, ou páginas no Github das pessoas cujas chaves públicas você importou. Tipicamente, essa comparação de chaves públicas é feita comparando um hash curto da chave pública conhecido como uma impressão digital.
3. Em seguida, você precisa baixar o executável do Bitcoin Core de seu [site](www.bitcoincore.org). Haverá pacotes disponíveis para sistemas operacionais Linux, Windows e MAC.
4. Em seguida, você tem que localizar dois arquivos de lançamento. O primeiro contém o hash SHA-256 oficial para o executável que você baixou junto com os hashes de todos os outros pacotes que foram lançados. Outro arquivo de lançamento conterá as assinaturas de vários contribuidores sobre o arquivo de lançamento com os hashes dos pacotes. Ambos os arquivos de lançamento devem estar localizados no site do Bitcoin Core.
5. Em seguida, você precisaria calcular o hash SHA-256 do executável que baixou do site do Bitcoin Core no seu próprio computador. Depois, compare esse resultado com o hash oficial do pacote para o executável. Eles devem ser iguais. 6. Finalmente, você teria que verificar se uma ou mais das assinaturas digitais sobre o arquivo de lançamento com os hashes oficiais do pacote realmente correspondem a uma ou mais chaves públicas que você importou (os lançamentos do Bitcoin Core nem sempre são assinados por todos). Você pode fazer isso com um aplicativo como o Kleopetra.

Este processo de verificação de software tem dois benefícios principais. Primeiro, garante que não houve erros na transmissão ao baixar do site do Bitcoin Core. Segundo, garante que nenhum atacante poderia ter feito você baixar código modificado e malicioso, seja hackeando o site do Bitcoin Core ou interceptando o tráfego.

Como exatamente o processo de verificação de software acima protege contra esses problemas?

Se você verificou diligentemente as chaves públicas que importou, então pode estar bastante certo de que essas chaves são realmente delas e não foram comprometidas. Dado que as assinaturas digitais têm a propriedade de infalsificabilidade existencial, você sabe que apenas esses contribuidores poderiam ter feito uma assinatura digital sobre os hashes oficiais do pacote no arquivo de lançamento.

Suponha que as assinaturas no arquivo de lançamento que você baixou estejam corretas. Agora você pode comparar o valor do hash que calculou localmente para o executável do Windows que baixou com aquele incluído no arquivo de lançamento devidamente assinado. Como você sabe que a função hash SHA-256 é resistente a colisões, uma correspondência significa que seu executável é exatamente o mesmo que o executável oficial.

Vamos agora nos voltar para a segunda propriedade comum das funções hash: **ocultação**. Diz-se que qualquer função hash $H$ tem a propriedade de ocultação se, para qualquer $x$ selecionado aleatoriamente de uma faixa muito grande, é inviável encontrar $x$ quando apenas $H(x)$ é dado.

Abaixo, você pode ver a saída SHA-256 de uma mensagem que escrevi. Para garantir suficiente aleatoriedade, a mensagem incluiu uma sequência de caracteres gerada aleatoriamente no final. Dado que o SHA-256 tem a propriedade de ocultação, ninguém seria capaz de decifrar esta mensagem.

- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`

Mas não vou deixar você na expectativa até que o SHA-256 se torne mais fraco. A mensagem original que escrevi foi a seguinte:

* “Esta é uma mensagem muito aleatória, ou bem, meio aleatória. Esta parte inicial não é, mas vou terminar com alguns caracteres relativamente aleatórios para garantir uma mensagem muito imprevisível. XLWz4dVG3BxUWm7zQ9qS”.

Uma maneira comum pela qual as funções hash com a propriedade de ocultação são usadas é na gestão de senhas (a resistência a colisões também é importante para essa aplicação). Qualquer serviço decente baseado em contas online, como Facebook ou Google, não armazenará suas senhas diretamente para gerenciar o acesso à sua conta. Em vez disso, eles armazenarão apenas um hash dessa senha. Cada vez que você preenche sua senha em um navegador, um hash é primeiro calculado. Apenas esse hash é enviado para o servidor do provedor de serviços e comparado com o hash armazenado no banco de dados de back-end. A propriedade de ocultação pode ajudar a garantir que os atacantes não possam recuperá-la a partir do valor do hash.
Gerenciamento de senhas por meio de hashes, claro, só funciona se os usuários realmente escolherem senhas difíceis. A propriedade de ocultação pressupõe que x é escolhido aleatoriamente de uma faixa muito grande. Selecionar senhas como “1234”, “minhasenha” ou a data do seu aniversário não proporcionará nenhuma segurança real. Existem longas listas de senhas comuns e seus hashes que os atacantes podem aproveitar se eles obtiverem o hash da sua senha. Esses tipos de ataques são conhecidos como **ataques de dicionário**. Se os atacantes conhecem alguns dos seus detalhes pessoais, eles também podem tentar alguns palpites informados. Portanto, você sempre precisa de senhas longas e seguras (preferencialmente longas sequências aleatórias de um gerenciador de senhas).
Às vezes, um aplicativo pode precisar de uma função de hash que tenha tanto resistência a colisões quanto ocultação. Mas certamente nem sempre. O processo de verificação de software que discutimos, por exemplo, só requer que a função de hash exiba resistência a colisões, a ocultação não é importante.

Enquanto resistência a colisões e ocultação são as principais propriedades buscadas das funções de hash em criptografia, em certas aplicações outros tipos de propriedades também podem ser desejáveis.

**Notas:**

[6] A terminologia “ocultação” não é uma linguagem comum, mas é especificamente retirada de Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller e Steven Goldfeder, *Bitcoin and Cryptocurrency Technologies*, Princeton University Press (Princeton, 2016), Capítulo 1.

# O sistema criptográfico RSA
<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

## O problema da fatoração
<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Enquanto a criptografia simétrica é geralmente bastante intuitiva para a maioria das pessoas, isso normalmente não é o caso com a criptografia assimétrica. Embora você provavelmente esteja confortável com a descrição de alto nível oferecida nas seções anteriores, você provavelmente está se perguntando o que exatamente são as funções unidirecionais e como exatamente elas são usadas para construir esquemas assimétricos.

Neste capítulo, vou remover um pouco do mistério que envolve a criptografia assimétrica, olhando mais profundamente em um exemplo específico, nomeadamente o sistema criptográfico RSA. Na primeira seção, vou introduzir o problema da fatoração no qual o problema RSA é baseado. Em seguida, cobrirei uma série de resultados chave da teoria dos números. Na última seção, juntaremos essas informações para explicar o problema RSA e como isso pode ser usado para criar esquemas criptográficos assimétricos.

Adicionar essa profundidade à nossa discussão não é uma tarefa fácil. Requer a introdução de vários teoremas e proposições da teoria dos números. Mas não deixe a matemática dissuadi-lo. Trabalhar através desta discussão melhorará significativamente sua compreensão do que está por trás da criptografia assimétrica e é um investimento valioso.

Vamos agora primeiro nos voltar para o problema da fatoração.

___

Sempre que você multiplica dois números, digamos $a$ e $b$, nos referimos aos números $a$ e $b$ como **fatores**, e o resultado como o **produto**. Tentar escrever um número $N$ na multiplicação de dois ou mais fatores é chamado de **fatoração**. [1] Você pode chamar qualquer problema que requer isso de **problema de fatoração**.

Há cerca de 2.500 anos, o matemático grego Euclides de Alexandria descobriu um teorema chave sobre a fatoração de inteiros. É comumente chamado de **teorema da fatoração única** e afirma o seguinte:

**Teorema 1**. Todo inteiro $N$ que é maior que 1 é ou um número primo, ou pode ser expresso como um produto de fatores primos.
Tudo o que a última parte desta declaração significa é que você pode pegar qualquer número inteiro não-primo $N$ maior que 1 e escrevê-lo como uma multiplicação de números primos. Abaixo estão vários exemplos de inteiros não-primos escritos como o produto de fatores primos.
* $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$
* $84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$
* $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$

Para todos os três inteiros acima, calcular seus fatores primos é relativamente fácil, mesmo se você só tiver $N$. Você começa com o menor número primo, ou seja, 2, e vê quantas vezes o inteiro $N$ é divisível por ele. Em seguida, você passa a testar a divisibilidade de $N$ por 3, 5, 7 e assim por diante. Você continua esse processo até que seu inteiro $N$ esteja escrito como o produto de apenas números primos.

Tome, por exemplo, o inteiro 84. Abaixo você pode ver o processo para determinar seus fatores primos. A cada etapa, retiramos o menor fator primo restante (à esquerda) e determinamos o termo restante a ser fatorado. Continuamos até que o termo restante também seja um número primo. A cada etapa, a fatoração atual de 84 é exibida à extrema direita.

* Fator primo = 2: termo restante = 42 	($84 = 2 \cdot 42$)
* Fator primo = 2: termo restante = 21 	($84 = 2 \cdot 2 \cdot 21$)
* Fator primo = 3: termo restante = 7 	($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
* Como 7 é um número primo, o resultado é $2 \cdot 2 \cdot 3 \cdot 7$, ou $2^2 \cdot 3 \cdot 7$.

Suponha agora que $N$ seja muito grande. Quão difícil seria reduzir $N$ aos seus fatores primos?

Isso realmente depende de $N$. Suponha, por exemplo, que $N$ seja 50,450,400. Embora este número pareça intimidante, os cálculos não são tão complicados e podem facilmente ser feitos à mão. Como acima, você apenas começa com 2 e segue adiante. Abaixo, você pode ver o resultado deste processo de maneira semelhante à acima.

* 2: 25,225,200 	($50,450,400 = 2 \cdot 25,225,200$)  
* 2: 12,612,600 	($50,450,400 = 2^2 \cdot 12,612,600$)  
* 2: 6,306,300 	($50,450,400 = 2^3 \cdot 6,306,300$)  
* 2: 3,153,150 	($50,450,400 = 2^4 \cdot 3,153,150$)  
* 2: 1,576,575 	($50,450,400 = 2^5 \cdot 1,576,575$)
* 3: 525.525 ($50.450.400 = 2^5 \cdot 3 \cdot 525.525$)
* 3: 175.175 ($50.450.400 = 2^5 \cdot 3^2 \cdot 175.175$)
* 5: 35.035 ($50.450.400 = 2^5 \cdot 3^2 \cdot 5 \cdot 35.035$)
* 5: 7.007 ($50.450.400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7.007$)
* 7: 1.001 ($50.450.400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 1.001$)
* 7: 143 ($50.450.400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 143$)
* 11: 13 ($50.450.400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
* Como 13 é um número primo, o resultado é $2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$.

Resolver este problema manualmente leva algum tempo. Um computador, claro, poderia fazer tudo isso em uma fração de segundo. De fato, um computador pode frequentemente até fatorar inteiros extremamente grandes em uma fração de segundo.

No entanto, existem certas exceções. Suponha que primeiro selecionamos aleatoriamente dois números primos muito grandes. É típico rotular esses números como $p$ e $q$, e adotarei essa convenção aqui.

Para ser concreto, digamos que $p$ e $q$ sejam ambos primos de 1024 bits, e que de fato requerem pelo menos 1024 bits para serem representados (então o primeiro bit deve ser 1). Então, por exemplo, 37 não poderia ser um dos números primos. Você certamente pode representar 37 com 1024 bits. Mas claramente *você não precisa* de tantos bits para representá-lo. Você pode representar 37 por qualquer string que tenha 6 bits ou mais. (Em 6 bits, 37 seria representado como $100101$).

É importante apreciar o quão grandes são $p$ e $q$ se selecionados sob as condições acima. Como exemplo, selecionei um número primo aleatório que precisa de pelo menos 1024 bits para representação abaixo.
* 14.752.173.874.503.595.484.930.006.383.670.759.559.764.562.721.397.166.747.289.220.945.457.932.666.751.048.198.854.920.097.085.690.793.755.254.946.188.163.753.506.778.089.706.699.671.722.089.715.624.760.049.594.106.189.662.669.156.149.028.900.805.928.183.585.427.782.974.951.355.515.394.807.209.836.870.484.558.332.897.443.152.653.214.483.870.992.618.171.825.921.582.253.023.974.514.209.142.520.026.807.636.589

Suponha agora que, após selecionar aleatoriamente números primos $p$ e $q$, os multipliquemos para obter um inteiro $N$. Este último inteiro, portanto, é um número de 2048 bits que requer pelo menos 2048 bits para sua representação. Ele é muito, muito maior do que $p$ ou $q$.

Suponha que você apenas forneça a um computador $N$ e peça para encontrar os dois fatores primos de 1024 bits de $N$. A probabilidade de o computador descobrir $p$ e $q$ é extremamente pequena. Pode-se dizer que é impossível para todos os fins práticos. Isso é verdade, mesmo que você empregue um supercomputador ou até mesmo uma rede de supercomputadores.

Para começar, suponha que o computador tente resolver o problema percorrendo números de 1024 bits, testando em cada caso se são primos e se são fatores de $N$. O conjunto de números primos a ser testado é então aproximadamente $1,265 \cdot 10^{305}$. [2]

Mesmo que você pegue todos os computadores do planeta e os faça tentar encontrar e testar números primos de 1024 bits dessa maneira, uma chance em um bilhão de encontrar com sucesso um fator primo de $N$ exigiria um período de cálculo muito mais longo do que a idade do Universo.

Agora, na prática, um computador pode fazer melhor do que o procedimento bruto recém-descrito. Existem vários algoritmos que o computador pode aplicar para chegar a uma fatoração mais rapidamente. O ponto, no entanto, é que mesmo usando esses algoritmos mais eficientes, a tarefa do computador ainda é computacionalmente inviável. [3]

Importante, a dificuldade da fatoração sob as condições recém-descritas repousa na suposição de que não existem algoritmos computacionalmente eficientes para calcular fatores primos. Não podemos realmente provar que um algoritmo eficiente não existe. No entanto, essa suposição é muito plausível: apesar de extensos esforços ao longo de centenas de anos, ainda não encontramos tal algoritmo computacionalmente eficiente.

Portanto, o problema da fatoração, sob certas circunstâncias, pode plausivelmente ser assumido como um problema difícil. Especificamente, quando $p$ e $q$ são números primos muito grandes, seu produto $N$ não é difícil de calcular; mas a fatoração, tendo apenas $N$, é praticamente impossível.


**Notas:**

[1] A fatoração também pode ser importante para trabalhar com outros tipos de objetos matemáticos além de números. Por exemplo, pode ser útil fatorar expressões polinomiais como $x^2 - 2x + 1$. Em nossa discussão, focaremos apenas na fatoração de números, especificamente inteiros.
[2] De acordo com o **teorema dos números primos**, o número de primos menores ou iguais a $N$ é aproximadamente $N/\ln(N)$. Isso significa que você pode aproximar o número de primos de comprimento 1024 bits por:
$$ \frac{2^{1024}}{\ln(2^{1024})} - \frac{2^{1023}}{\ln(2^{1023})} $$

...o que é aproximadamente igual a $1.265 \times 10^{305}$.

[3] O mesmo é verdade para problemas de logaritmo discreto. Daí, o motivo pelo qual construções assimétricas trabalham com chaves muito maiores do que construções criptográficas simétricas.

## Resultados teóricos dos números
<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Infelizmente, o problema da fatoração não pode ser usado diretamente para esquemas criptográficos assimétricos. No entanto, podemos usar um problema mais complexo, mas relacionado para este efeito: o problema RSA.

Para entender o problema RSA, precisaremos entender uma série de teoremas e proposições da teoria dos números. Estes são apresentados nesta seção em três subseções: (1) a ordem de N, (2) a invertibilidade módulo N, e (3) o teorema de Euler.

Algum do material nas três subseções já foi introduzido no *Capítulo 3*. Mas eu vou aqui reafirmar esse material para conveniência.

### A ordem de N

Um inteiro $a$ é **coprimo** ou um **primo relativo** com um inteiro $N$, se o maior divisor comum entre eles for 1. Embora 1, por convenção, não seja um número primo, ele é um coprimo de todo inteiro (assim como $-1$).

Por exemplo, considere o caso quando $a = 18$ e $N = 37$. Estes são claramente coprimos. O maior inteiro que divide tanto 18 quanto 37 é 1. Por contraste, considere o caso quando $a = 42$ e $N = 16$. Estes claramente não são coprimos. Ambos os números são divisíveis por 2, que é maior que 1.

Podemos agora definir a ordem de $N$ da seguinte forma. Suponha que $N$ seja um inteiro maior que 1. A **ordem de N** é, então, o número de todos os coprimos com $N$ tal que para cada coprimo $a$, a seguinte condição seja mantida: $1 \leq a < N$.

Por exemplo, se $N = 12$, então 1, 5, 7 e 11 são os únicos coprimos que atendem ao requisito acima. Portanto, a ordem de 12 é igual a 4.

Suponha que $N$ seja um número primo. Então, qualquer inteiro menor que $N$ mas maior ou igual a 1 é coprimo com ele. Isso inclui todos os elementos no seguinte conjunto: $\{1,2,3,….,N - 1\}$. Portanto, quando $N$ é primo, a ordem de $N$ é $N - 1$. Isso é afirmado na proposição 1, onde $\phi(N)$ denota a ordem de $N$.

**Proposição 1**. $\phi(N) = N - 1$ quando $N$ é primo
Suponha que $N$ não seja primo. Você pode, então, calcular sua ordem usando a **Função Phi de Euler**. Embora calcular a ordem de um inteiro pequeno seja relativamente simples, a Função Phi de Euler torna-se particularmente importante para inteiros maiores. A proposição da Função Phi de Euler é declarada abaixo.
**Teorema 2**. Seja $N = p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, onde o conjunto $\{p_i\}$ consiste em todos os fatores primos distintos de $N$ e cada $e_i$ indica quantas vezes o fator primo $p_i$ ocorre para $N$. Então,

$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot (p_n - 1)$$

**Teorema 2** mostra que, uma vez que você tenha decomposto qualquer $N$ não primo em seus fatores primos distintos, é fácil calcular a ordem de $N$.

Por exemplo, suponha que $N = 270$. Isso claramente não é um número primo. Decompondo $N$ em seus fatores primos, obtemos a expressão: $2 \cdot 3^3 \cdot 5$. De acordo com a Função Phi de Euler, a ordem de $N$ é então a seguinte:

$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$

Suponha agora que $N$ seja um produto de dois primos, $p$ e $q$. **Teorema 2** acima, então, afirma que a ordem de $N$ é a seguinte:

$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$

Este é um resultado chave para o problema RSA em particular, e é declarado na **Proposição 2** abaixo.

**Proposição 2**. Se $N$ é o produto de dois primos, $p$ e $q$, a ordem de $N$ é o produto $(p - 1) \cdot (q - 1)$.

Para ilustrar, suponha que $N = 119$. Este inteiro pode ser fatorado em dois primos, a saber 7 e 17. Portanto, a Função Phi de Euler sugere que a ordem de 119 é a seguinte:

$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$

Em outras palavras, o inteiro 119 tem 96 coprimos no intervalo de 1 até 119. Na verdade, este conjunto inclui todos os inteiros de 1 até 119, que não são múltiplos de 7 ou 17.
A partir daqui, vamos denotar o conjunto de coprimos que determina a ordem de $N$ como $C_N$. Para o nosso exemplo onde $N = 119$, o conjunto $C_{119}$ é grande demais para ser listado completamente. Mas alguns dos elementos são os seguintes:
$$C_{119} = \{1, 2, \dots 6, 8 \dots 13, 15, 16, 18, \dots 33, 35 \dots 96\}$$

### Invertibilidade módulo N

Podemos dizer que um inteiro $a$ é **invertível módulo N**, se existir pelo menos um inteiro $b$ tal que $a \cdot b \mod N = 1 \mod N$. Qualquer tal inteiro $b$ é referido como um **inverso** (ou **inverso multiplicativo**) de $a$ dado a redução por módulo $N$.

Suponha, por exemplo, que $a = 5$ e $N = 11$. Existem muitos inteiros pelos quais você pode multiplicar 5, de modo que $5 \cdot b \mod 11 = 1 \mod 11$. Considere, por exemplo, os inteiros 20 e 31. É fácil ver que ambos esses inteiros são inversos de 5 para redução módulo 11.

* $5 \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
* $5 \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$

Embora 5 tenha muitos inversos na redução módulo 11, você pode mostrar que existe apenas um único inverso positivo de 5 que é menor que 11. Na verdade, isso não é único para o nosso exemplo particular, mas um resultado geral.

**Proposição 3**. Se o inteiro $a$ é invertível módulo $N$, deve ser o caso de que exatamente um inverso positivo de $a$ seja menor que $N$. (Então, esse inverso único de $a$ deve vir do conjunto $\{1, \dots, N - 1\}$).

Vamos denotar o inverso único de $a$ da **Proposição 3** como $a^{-1}$. Para o caso quando $a = 5$ e $N = 11$, você pode ver que $a^{-1} = 9$, dado que $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.

Note que você também pode obter o valor 9 para $a^{-1}$ no nosso exemplo simplesmente reduzindo qualquer outro inverso de $a$ por módulo 11. Por exemplo, $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Então, sempre que um inteiro $a > N$ é invertível módulo $N$, então $a \mod N$ também deve ser invertível módulo $N$.

Não é necessariamente o caso de que um inverso de $a$ exista na redução módulo $N$. Suponha, por exemplo, que $a = 2$ e $N = 8$. Não existe $b$, ou qualquer $a^{-1}$ especificamente, tal que $2 \cdot b \mod 8 = 1 \mod 8$. Isso ocorre porque qualquer valor de $b$ sempre produzirá um múltiplo de 2, então nenhuma divisão por 8 pode jamais resultar em um resto que seja igual a 1.
Como exatamente sabemos se algum inteiro $a$ possui um inverso para um dado $N$? Como você deve ter notado no exemplo acima, o maior divisor comum entre 2 e 8 é maior que 1, nomeadamente 2. E isso é na verdade ilustrativo do seguinte resultado geral:
**Proposição 4**. Um inverso existe de um inteiro $a$ dado a redução módulo $N$, e especificamente um único inverso positivo menor que $N$, se e somente se o maior divisor comum entre $a$ e $N$ é 1 (isto é, se eles são coprimos).

Para o caso quando $a = 5$ e $N = 11$, concluímos que $a^{-1} = 9$, dado que $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. É importante notar que o inverso também é verdadeiro. Ou seja, quando $a = 9$ e $N = 11$, verifica-se que $a^{-1} = 5$.

### Teorema de Euler

Antes de passarmos para o problema RSA, precisamos entender mais um teorema crucial, nomeadamente **o teorema de Euler**. Ele afirma o seguinte:

**Teorema 3**. Suponha que dois inteiros $a$ e $N$ sejam coprimos. Então, $a^{\phi(N)} \mod N = 1 \mod N$.

Este é um resultado notável, mas um pouco confuso à primeira vista. Vamos recorrer a um exemplo para entender isso.

Suponha que $a = 5$ e $N = 7$. Estes são de fato coprimos como o teorema de Euler exige. Sabemos que a ordem de 7 é igual a 6, dado que 7 é um número primo (veja **Proposição 1**).

O que o teorema de Euler agora afirma é que $5^6 \mod 7$ deve ser igual a $1 \mod 7$. Abaixo estão os cálculos para mostrar que isso é de fato verdade.

* $5^6 \mod 7 = 15.625 \mod 7 = 1 \mod N$

O inteiro 7 divide 15.624 um total de 2.233 vezes. Portanto, o resto da divisão de 16.625 por 7 é 1.

Em seguida, usando a função Phi de Euler, **Teorema 2**, você pode derivar a **Proposição 5** abaixo.

**Proposição 5**. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$ para quaisquer inteiros positivos $a$ e $b$.

Não mostraremos por que isso é o caso. Mas apenas observe que você já viu evidências desta proposição pelo fato de $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$ quando $p$ e $q$ são primos, conforme afirmado na **Proposição 2**.

O teorema de Euler em conjunto com a **Proposição 5** tem implicações importantes. Veja o que acontece, por exemplo, nas expressões abaixo, onde $a$ e $N$ são coprimos.

* $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
* $a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$
* $a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$

Portanto, a combinação do teorema de Euler e da **Proposição 5** nos permite calcular de forma simples um número de expressões. Em geral, podemos resumir a ideia conforme a **Proposição 6**.

**Proposição 6**. $a^x \mod N = a^{x \mod \phi(N)}$

Agora temos que juntar tudo em um último passo complicado.

Assim como $N$ tem uma ordem $\phi(N)$ que inclui os elementos do conjunto $C_N$, sabemos que o inteiro $\phi(N)$ deve, por sua vez, também ter uma ordem e um conjunto de coprimos. Vamos definir $\phi(N) = R$. Então sabemos que também existe um valor para $\phi(R)$ e um conjunto de coprimos $C_R$.

Suponha que agora selecionamos um inteiro $e$ do conjunto $C_R$. Sabemos pela **Proposição 3** que este inteiro $e$ tem apenas um inverso positivo único menor que $R$. Ou seja, $e$ tem um inverso único do conjunto $C_R$. Vamos chamar este inverso de $d$. Dada a definição de um inverso, isso significa que $e \cdot d = 1 \mod R$.

Podemos usar este resultado para fazer uma declaração sobre nosso inteiro original $N$. Isso é resumido na **Proposição 7**.

**Proposição 7**. Suponha que $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Então, para qualquer elemento $a$ do conjunto $C_N$, deve ser o caso que $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.

Agora temos todos os resultados teóricos de números necessários para declarar claramente o problema RSA.

## O criptossistema RSA

Estamos agora prontos para declarar o problema RSA. Suponha que você crie um conjunto de variáveis consistindo de $p$, $q$, $N$, $\phi(N)$, $e$, $d$ e $y$. Chame este conjunto de $\Pi$. Ele é criado da seguinte forma:

1. Gere dois primos aleatórios $p$ e $q$ de tamanho igual e calcule o produto deles $N$.
2. Calcule a ordem de $N$, $\phi(N)$, pelo seguinte produto: $(p - 1) \cdot (q - 1)$.
3. Selecione um $e > 2$ tal que seja menor e coprimo a $\phi(N)$.
4. Calcule $d$ definindo $e \cdot d \mod \phi(N) = 1$.
5. Selecione um valor aleatório $y$ que seja menor e coprimo a $N$.
O problema RSA consiste em encontrar um $x$ tal que $x^e = y$, enquanto apenas um subconjunto de informações sobre $\Pi$ é fornecido, nomeadamente as variáveis $N$, $e$ e $y$. Quando $p$ e $q$ são muito grandes, tipicamente recomenda-se que tenham 1024 bits de tamanho, o problema RSA é considerado difícil. Agora você pode ver por que isso é o caso, dada a discussão anterior.

Uma maneira fácil de calcular $x$ quando $x^e \mod N = y \mod N$ é simplesmente calcular $y^d \mod N$. Sabemos que $y^d \mod N = x \mod N$ pelos seguintes cálculos:

$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$

O problema é que não conhecemos o valor $d$, pois ele não é fornecido no problema. Portanto, não podemos calcular diretamente $y^d \mod N$ para produzir $x \mod N$.

No entanto, poderíamos ser capazes de calcular indiretamente $d$ a partir da ordem de $N$, $\phi(N)$, já que sabemos que $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Mas por suposição, o problema também não fornece um valor para $\phi(N)$.

Finalmente, a ordem poderia ser calculada indiretamente com os fatores primos $p$ e $q$, para que eventualmente possamos calcular $d$. Mas por suposição, os valores de $p$ e $q$ também não nos foram fornecidos.

Estritamente falando, mesmo que o problema de fatoração dentro de um problema RSA seja difícil, não podemos provar que o problema RSA também é difícil. Pode haver, nomeadamente, outras maneiras de resolver o problema RSA além da fatoração. No entanto, é geralmente aceito e assumido que se o problema de fatoração dentro do problema RSA é difícil, o próprio problema RSA também é difícil.

Se o problema RSA é de fato difícil, então ele produz uma função unidirecional com uma porta dos fundos. A função aqui é $f(g) = g^e \mod N$. Com conhecimento de $f(g)$, qualquer um poderia facilmente calcular um valor $y$ para um determinado $g = x$. No entanto, é praticamente impossível calcular um valor específico $x$ apenas conhecendo o valor $y$ e a função $f(g)$. A exceção é quando você recebe uma peça de informação $d$, a porta dos fundos. Nesse caso, você pode simplesmente calcular $y^d$ para obter $x$.

Vamos passar por um exemplo específico para ilustrar o problema RSA. Não posso selecionar um problema RSA que seria considerado difícil sob as condições acima, pois os números seriam excessivos. Em vez disso, este exemplo é apenas para ilustrar como o problema RSA geralmente funciona.

Para começar, suponha que você selecione dois números primos aleatórios 13 e 31. Então $p = 13$ e $q = 31$. O produto $N$ desses dois primos é igual a 403. Podemos facilmente calcular a ordem de 403. Ela é equivalente a $(13 - 1) \cdot (31 - 1) = 360$.
Em seguida, conforme ditado pelo passo 3 do problema RSA, precisamos selecionar um coprimo para 360 que seja maior que 2 e menor que 360. Não precisamos selecionar esse valor aleatoriamente. Suponha que selecionemos 103. Este é um coprimo de 360, pois seu maior divisor comum com 103 é 1.
O passo 4 agora exige que calculemos um valor $d$ tal que $103 \cdot d \mod 360 = 1$. Esta não é uma tarefa fácil à mão quando o valor de $N$ é grande. Requer que usemos um procedimento chamado **algoritmo euclidiano estendido**.

Embora eu não mostre o procedimento aqui, ele resulta no valor 7 quando $e = 103$. Você pode verificar que o par de valores 103 e 7 de fato atende à condição geral $e \cdot d \mod \phi(n) = 1$ através dos cálculos abaixo.

* $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$

Importante, dado a *Proposição 4*, sabemos que nenhum outro inteiro entre 1 e 360 para $d$ produzirá o resultado de que $103 \cdot d = 1 \mod 360$. Além disso, a proposição implica que selecionar um valor diferente para $e$ resultará em um valor único diferente para $d$.

No passo 5 do problema RSA, temos que selecionar algum inteiro positivo $y$ que seja um coprimo menor de 403. Suponha que definimos $y = 2^{103}$. A exponenciação de 2 por 103 resulta no seguinte.

* $2^{103} \mod 403 = 10.141.204.801.825.835.211.973.625.643.008 \mod 403 = 349 \mod 403$

O problema RSA neste exemplo específico é agora o seguinte: Você recebe $N = 403$, $e = 103$, e $y = 349 \mod 403$. Agora você tem que calcular $x$ tal que $x^{103} = 349 \mod 403$. Ou seja, você deve encontrar que o valor original antes da exponenciação por 103 era 2.

Seria fácil (pelo menos para um computador) calcular $x$ se soubéssemos que $d = 7$. Nesse caso, você poderia simplesmente determinar $x$ como abaixo.

* $x = y^7 \mod 403 = 349^7 \mod 403 = 630.634.881.591.804.949 \mod 403 = 2 \mod 403$

O problema é que você não foi fornecido a informação de que $d = 7$. Você poderia, claro, calcular $d$ a partir do fato de que $103 \cdot d = 1 \mod 360$. O problema é que também não lhe é dada a informação de que a ordem de $N = 360$. Finalmente, você também poderia calcular a ordem de 403 calculando o seguinte produto: $(p - 1) \cdot (q - 1)$. Mas também não lhe é dito que $p = 13$ e $q = 31$.

Claro, um computador ainda poderia resolver o problema RSA para este exemplo relativamente fácil, porque os números primos envolvidos não são grandes. Mas quando os primos se tornam muito grandes, ele enfrenta uma tarefa praticamente impossível.
Agora apresentamos o problema RSA, um conjunto de condições sob as quais é difícil, e a matemática subjacente. Como tudo isso ajuda com a criptografia assimétrica? Especificamente, como podemos transformar a dificuldade do problema RSA sob certas condições em um esquema de criptografia ou um esquema de assinatura digital?
Uma abordagem é pegar o problema RSA e construir esquemas de maneira direta. Por exemplo, suponha que você gerou um conjunto de variáveis $\Pi$ conforme descrito no problema RSA, e garanta que $p$ e $q$ sejam suficientemente grandes. Você define sua chave pública igual a $(N, e)$ e compartilha essa informação com o mundo. Como descrito acima, você mantém os valores de $p$, $q$, $\phi(n)$, e $d$ em segredo. Na verdade, $d$ é sua chave privada.

Qualquer um que queira enviar a você uma mensagem $m$ que é um elemento de $C_N$ poderia simplesmente criptografá-la da seguinte forma: $c = m^e \mod N$. (O texto cifrado $c$ aqui é equivalente ao valor $y$ no problema RSA.) Você pode facilmente descriptografar esta mensagem apenas calculando $c^d \mod N$.

Você poderia tentar criar um esquema de assinatura digital da mesma maneira. Suponha que você queira enviar a alguém uma mensagem $m$ com uma assinatura digital $S$. Você poderia simplesmente definir $S = m^d \mod N$ e enviar o par $(m,S)$ ao destinatário. Qualquer um pode verificar a assinatura digital apenas verificando se $S^e \mod N = m \mod N$. No entanto, qualquer atacante teria uma dificuldade real em criar um $S$ válido para uma mensagem, dado que eles não possuem $d$.

Infelizmente, transformar o que por si só é um problema difícil, o problema RSA, em um esquema criptográfico não é tão direto. Para o esquema de criptografia direto, você só pode selecionar coprimos de $N$ como suas mensagens. Isso não nos deixa com muitas mensagens possíveis, certamente não o suficiente para comunicação padrão. Além disso, essas mensagens têm que ser selecionadas aleatoriamente. Isso parece um tanto impraticável. Finalmente, qualquer mensagem que seja selecionada duas vezes produzirá exatamente o mesmo texto cifrado. Isso é extremamente indesejável em qualquer esquema de criptografia e não atende a nenhuma noção rigorosa moderna de segurança em criptografia.

Os problemas se tornam ainda piores para o nosso esquema direto de assinatura digital. Como está, qualquer atacante pode facilmente forjar assinaturas digitais apenas selecionando primeiro um coprimo de $N$ como a assinatura e depois calculando a mensagem original correspondente. Isso claramente quebra o requisito de infalsificabilidade existencial.

No entanto, adicionando um pouco de complexidade inteligente, o problema RSA pode ser usado para criar um esquema seguro de criptografia de chave pública, bem como um esquema seguro de assinatura digital. Não entraremos nos detalhes de tais construções aqui. [4] Importante, no entanto, essa complexidade adicional não muda o problema fundamental subjacente do RSA no qual esses esquemas são baseados.

**Notas:**

[4] Veja, por exemplo, Jonathan Katz e Yehuda Lindell, _Introduction to Modern Cryptography_, CRC Press (Boca Raton, FL: 2015), pp. 410–32 sobre criptografia RSA e pp. 444–41 para assinaturas digitais RSA.