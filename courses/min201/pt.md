---
name: Introdução à Mineração de Bitcoin
goal: Compreender o funcionamento da indústria de mineração através de um exercício prático de reutilização de ASICs.
objectives:
  - Compreender a teoria da mineração
  - Compreender a indústria de mineração
  - Transformar um S9 em aquecedor
  - Minerar o primeiro satoshi
---

# Seus primeiros passos na mineração!

Neste curso, vamos aprofundar na indústria de mineração para desmistificar esse assunto tão complexo! O curso é acessível a todos e não requer investimento inicial.

A primeira seção será teórica, onde, com Ajelex, teremos uma discussão aprofundada sobre diversos temas relacionados à mineração. Isso nos permitirá entender melhor essa indústria e as questões econômicas e geopolíticas relacionadas a ela.
Na segunda seção, abordaremos um caso prático. Na verdade, vamos aprender a transformar um minerador S9 usado em um aquecedor de ambiente! Através de guias escritos e vídeos, mostraremos e explicaremos todos os passos para você conseguir fazer isso em sua casa :)

Esperamos, com este vídeo, mostrar que a indústria de mineração é mais complexa do que parece e estudá-la permite equilibrar o debate ecológico relacionado a ela!
Se você precisar de ajuda para sua empreitada, um grupo no Telegram foi criado para os alunos e todas as peças necessárias para alcançar o objetivo podem ser encontradas em nossa plataforma de comércio eletrônico!

+++

# Introdução

<partId>a99dc130-3650-563f-8d42-a0b5160af0ab</partId>

## Bem-vindo!

<chapterId>7ad1abeb-a190-5c85-8bff-44df71331e4d</chapterId>

Bem-vindo ao MINING 201: uma introdução à mineração. Ajelex, Jim & Rogzy estão felizes em acompanhá-lo em seus primeiros passos concretos nesta nova indústria. Esperamos que você goste do curso e se junte à aventura da mineração doméstica!

### Visão geral do curso

Neste curso, a primeira seção será dedicada à teoria da mineração com Ajelex. Discutiremos em profundidade os diversos temas relacionados à mineração, o que nos permitirá entender melhor essa indústria, bem como as questões econômicas e geopolíticas envolvidas.

Na segunda seção, embarcaremos em um caso prático fascinante, aprendendo a transformar um minerador S9 usado em um aquecedor de ambiente. Através de guias escritos e vídeos, todas as etapas necessárias serão explicadas minuciosamente, garantindo o seu sucesso neste projeto inovador.

Esta jornada de aprendizado mostrará que a indústria de mineração é mais complexa do que parece, oferecendo uma perspectiva equilibrada sobre o debate ecológico relacionado. Ajuda contínua estará disponível através de um grupo dedicado no Telegram para os alunos, e todas as peças necessárias serão facilmente acessíveis em nossa plataforma de comércio eletrônico.

### Currículo:

Seção Teórica:

- Explicação da mineração.
- A indústria de mineração.
- As nuances da indústria de mineração.
- A mineração no protocolo bitcoin.
- Preço do bitcoin e hashrate, uma correlação?\* Soberania e regulamentação
- Entrevista com um profissional da indústria de mineração

Seção Prática: Attakai

- Introdução ao Attakai.
- Guia de compra.
- Modificação do software de um Antminer S9.
- Substituição dos ventiladores para reduzir o ruído.
- Configuração de um pool.
- Configurando seu Antminer S9 com o Braiins OS+.

Pronto para começar essa aventura cativante? Vamos mergulhar juntos no fascinante mundo da mineração caseira!

# Tudo o que você precisa saber sobre mineração

<partId>aa99ef2c-da29-5317-a533-2ffa4f66f674</partId>

## Explicação da mineração

<chapterId>36a82de7-87ee-5e7a-b69e-48fc30030447</chapterId>

### Mineração explicada: A analogia do quebra-cabeça

Para explicar de forma simplificada o conceito de mineração, uma analogia relevante pode ser usada: a do quebra-cabeça. Assim como um quebra-cabeça, a mineração é uma tarefa complexa de ser realizada, mas fácil de ser verificada uma vez concluída. No contexto da mineração de Bitcoin, os mineradores se esforçam para resolver rapidamente um quebra-cabeça digital. O primeiro minerador a resolver o quebra-cabeça apresenta sua solução para toda a rede, que pode então verificar facilmente sua validade. Essa verificação bem-sucedida permite que o minerador valide um novo bloco e o adicione à cadeia de blocos do Bitcoin. Em reconhecimento ao seu trabalho, que envolve custos significativos, o minerador é recompensado com uma certa quantidade de bitcoins. Essa recompensa serve como um incentivo financeiro para os mineradores continuarem seu trabalho de validação de transações e segurança da rede Bitcoin.

![imagem](assets/en/01.webp)

Inicialmente na rede Bitcoin, a recompensa concedida era de 50 bitcoins a cada dez minutos, em paralelo à descoberta de um bloco a cada dez minutos, em média, pelos mineradores. Essa recompensa é reduzida pela metade a cada 210.000 blocos, aproximadamente a cada quatro anos. Essa remuneração serve como um poderoso incentivo para encorajar os mineradores a participarem do processo de mineração, apesar de seu custo energético. Sem a recompensa, a mineração, que consome muita eletricidade, seria abandonada, comprometendo assim a segurança e a estabilidade de toda a rede Bitcoin.

A recompensa atual de mineração é dupla. Por um lado, inclui a criação de novos bitcoins, que passou de 50 bitcoins a cada dez minutos no início para 6,25 bitcoins hoje (2023). Por outro lado, inclui as taxas de transação, ou taxas de mineração, das transações que o minerador escolhe incluir em seu bloco. Quando uma transação de bitcoin é feita, são pagas taxas de transação. Essas taxas funcionam como um tipo de leilão, onde os usuários indicam quanto estão dispostos a pagar para que sua transação seja incluída no próximo bloco. Para maximizar sua recompensa, os mineradores, agindo em seu próprio interesse, selecionam as transações mais lucrativas para incluir em seu bloco, levando em consideração o espaço limitado disponível. Assim, a recompensa de mineração é composta tanto pela geração de novos bitcoins quanto pelas taxas de transação, garantindo um incentivo contínuo para os mineradores e garantindo a sustentabilidade e segurança da rede Bitcoin.

### Mineradores e suas Ferramentas: Mineração

O processo de mineração consiste em encontrar um hash válido aceitável pela rede Bitcoin. Esse hash, uma vez calculado e encontrado, é irreversível, como batatas transformadas em purê. Ele verifica uma determinada função sem a possibilidade de voltar atrás. Os mineradores, em competição, usam máquinas para calcular esses hashes. Embora seja teoricamente possível encontrar esse hash manualmente, a complexidade da operação torna essa opção inviável. Computadores, capazes de realizar esses cálculos rapidamente, são, portanto, usados, consumindo, no entanto, uma quantidade significativa de eletricidade.

No início, a era da CPU dominava, onde os mineradores usavam seus computadores pessoais para minerar Bitcoin. A descoberta das vantagens das GPUs (placas de vídeo) para essa tarefa marcou uma virada, aumentando substancialmente a taxa de hash e reduzindo o consumo de energia. O progresso não parou por aí, com a posterior introdução dos FPGA (field-programmable gate array / matriz de portas programáveis em campo). Os FPGA serviram como plataforma para o desenvolvimento dos ASICs (application-specific integrated circuit / circuito integrado específico para aplicação).

![image](assets/en/02.webp)

Os ASICs são chips, comparáveis ao chip de uma CPU, no entanto, eles são desenvolvidos para realizar apenas um tipo específico de cálculo da maneira mais eficiente possível. Em outras palavras, uma CPU é capaz de realizar uma variedade de tipos diferentes de cálculos sem ser particularmente otimizada para um tipo de cálculo ou outro, enquanto um ASIC será capaz de realizar apenas um tipo de cálculo, mas de maneira muito eficiente. No caso, os ASICs Bitcoin são projetados para calcular o algoritmo SHA256.

Hoje em dia, os mineradores utilizam exclusivamente ASICs dedicadas a essa operação, otimizadas para testar o maior número possível de combinações com o menor consumo de energia e o mais rápido possível. Esses computadores, incapazes de executar tarefas além da mineração de Bitcoin, são um testemunho tangível da evolução contínua e da crescente especialização da indústria de mineração de Bitcoin. Essa evolução constante reflete a dinâmica intrínseca do Bitcoin, onde um ajuste na dificuldade garante a produção de um bloco a cada dez minutos, apesar do aumento exponencial na capacidade de mineração.

Para ilustrar a intensidade desse processo, considere um minerador típico capaz de realizar 14 TeraHash por segundo, ou seja, 14 trilhões de tentativas a cada segundo para encontrar o hash correto. Em escala da rede Bitcoin, atualmente atingimos cerca de 300 HexaHash por segundo, destacando o poder coletivo mobilizado na mineração de Bitcoin.

### Ajuste de dificuldade:

O ajuste de dificuldade é um mecanismo crucial no funcionamento da rede Bitcoin, garantindo que os blocos sejam minerados em média a cada 10 minutos. Essa duração é uma média, pois o processo de mineração é na verdade um jogo de probabilidades, semelhante a lançar dados na esperança de obter um número menor do que o número definido pela dificuldade. A cada 2016 blocos, a rede ajusta a dificuldade de mineração com base no tempo médio necessário para minerar os blocos anteriores. Se o tempo médio for superior a 10 minutos, a dificuldade é reduzida e, inversamente, se o tempo médio for menor, a dificuldade é aumentada. Esse mecanismo de ajuste garante que o tempo de mineração dos novos blocos permaneça constante ao longo do tempo, independentemente do número de mineradores ou do poder de computação global da rede. É por isso que o Blockchain do Bitcoin também é chamado de Timechain.

![image](assets/en/03.webp)

- Exemplo da China:
  O caso da China ilustra perfeitamente esse mecanismo de ajuste de dificuldade, com sua abundante e barata energia, ela era o principal hub global de mineração de Bitcoin. Em 2021, o país proibiu abruptamente a mineração de Bitcoin em seu território, resultando em uma queda maciça na taxa de hash global da rede Bitcoin, da ordem de 50%. Essa rápida diminuição na potência de mineração poderia ter prejudicado gravemente a rede Bitcoin, aumentando o tempo médio de mineração dos blocos. No entanto, o mecanismo de ajuste de dificuldade entrou em ação, reduzindo a dificuldade de mineração para garantir que a frequência de mineração dos blocos permaneça em média em 10 minutos. Esse caso demonstra a eficiência e a resiliência do mecanismo de ajuste de dificuldade do Bitcoin, que garante a estabilidade e previsibilidade da rede, mesmo diante de mudanças abruptas e significativas no cenário global de mineração.

### Evolução das Máquinas de Mineração de Bitcoin

Em relação à evolução das máquinas de mineração de Bitcoin, é importante ressaltar que o contexto é mais voltado para um modelo de negócios tradicional. Os mineradores obtêm sua receita por meio da validação dos blocos, uma tarefa com uma probabilidade relativamente baixa de sucesso. O modelo de máquina atualmente em uso, o Antminer S9, embora seja um modelo mais antigo lançado por volta de 2016, ainda está em circulação no mercado de segunda mão, sendo negociado por cerca de 100€ a 200€. No entanto, o preço das máquinas de mineração varia de acordo com o valor do Bitcoin, e um modelo mais recente, o Antminer S19, está atualmente avaliado em cerca de 3000€.

Diante da constante evolução tecnológica no campo da mineração, os profissionais precisam se posicionar estrategicamente. A indústria de mineração está sujeita a inovações contínuas, como evidenciado pelo recente lançamento da versão J do S19 e o próximo lançamento do S19 XP, que oferece capacidades de mineração significativamente superiores. Além disso, as melhorias não estão apenas relacionadas ao desempenho bruto das máquinas. Por exemplo, o novo modelo S19 XP utiliza um sistema de resfriamento líquido, uma modificação técnica que permite uma melhoria significativa na eficiência energética. Embora a inovação continue sendo uma constante, os ganhos futuros de eficiência provavelmente serão menores em comparação com os observados até agora, devido ao alcance de um certo limite de inovação tecnológica.

![image](assets/en/04.webp)

Em conclusão, a indústria de mineração de Bitcoin continua a se adaptar e se desenvolver, e os atores do setor devem antecipar ganhos de eficiência, que serão mais limitados no futuro, e ajustar suas estratégias de acordo. Avanços tecnológicos futuros, embora ainda presentes, provavelmente ocorrerão em uma escala menor, refletindo a maturidade crescente do setor.

## A indústria de mineração

<chapterId>0896dfc1-c97e-5bec-9bf1-8c20b3388a2c</chapterId>

### Pools de mineração

Atualmente, a mineração de Bitcoin evoluiu para se tornar uma indústria séria e substancial, com muitos atores agora públicos e um número crescente de mineradores significativos. Essa evolução tornou a mineração quase inacessível para pequenos atores devido ao alto custo associado à aquisição de novas máquinas de mineração. Portanto, surge a questão da distribuição da taxa de hash entre diferentes atores do mercado. A situação é complexa, pois é essencial examinar tanto a distribuição da taxa de hash entre diferentes empresas quanto entre diferentes pools de mineração.

![imagem](assets/en/05.webp)

Um pool de mineração é um grupo de mineradores que unem seus recursos de computação para aumentar suas chances de mineração. Essa cooperação é necessária porque uma pequena máquina de mineração isolada está competindo com gigantes da indústria, reduzindo suas chances de sucesso a um nível insignificante. A mineração funciona de acordo com um princípio de loteria, e as chances de ganhar um bloco (e, portanto, a recompensa em Bitcoin) a cada dez minutos são extremamente baixas para um pequeno minerador individual. Ao se unirem em pools, os mineradores podem combinar seu poder de computação, encontrar blocos com mais frequência e, em seguida, distribuir as recompensas de forma proporcional à contribuição de cada minerador para o pool.

Por exemplo, se um pool encontrar um bloco e ganhar 6,25 bitcoins, um minerador que contribui com 1% do poder de computação total do pool receberia 1% dos 6,25 bitcoins ganhos. No entanto, é importante observar que os pools de mineração geralmente cobram uma pequena comissão (geralmente em torno de 2%) para cobrir os custos operacionais da cooperativa.

### Softwares usados pela indústria

No contexto da mineração de Bitcoin, o papel do software é tão crucial quanto o hardware. Um exemplo disso é ilustrado pelo papel da Bitmain, um fabricante prolífico que desenvolveu o Antminer S9. Além do hardware de mineração, a indústria depende fortemente de pools de mineração colaborativos, como o Brainspool, que controla cerca de 5% da taxa de hash global da rede Bitcoin.
Os atores dessa indústria estão constantemente buscando aumentar a eficiência por meio de hardware e software. Por exemplo, um software popular usado nesse contexto é o BrainsOS Plus. Esse software substitui o sistema operacional original da máquina de mineração, permitindo que as mesmas operações sejam executadas de maneira mais eficiente. Com esse software, um minerador pode aumentar a eficiência de sua máquina em 25%. Isso significa que, para uma quantidade equivalente de eletricidade, a máquina pode produzir 25% a mais de taxa de hash, aumentando assim as recompensas recebidas pelo minerador. Essa otimização de software é um elemento essencial para a competitividade na mineração de Bitcoin, demonstrando a importância de uma abordagem integrada, combinando melhorias de hardware e software para maximizar a eficiência e os retornos.

### Regulação e tarifas de eletricidade

Como observado na China e em outros lugares, a regulação tem uma influência significativa na mineração. Embora não haja mineradores significativos na França, a regulação e as altas tarifas de eletricidade na Europa são obstáculos importantes. Os mineradores estão constantemente em busca de eletricidade de baixo custo para maximizar seus ganhos. Assim, o alto custo da eletricidade na Europa e na França não favorece a atração de mineradores para essas regiões.

Os mineradores tendem a se dirigir a regiões com tarifas de eletricidade baixas, muitas vezes em países emergentes ou países com excedentes de energia. Por exemplo, uma grande parte da taxa de hash global está no Texas, nos Estados Unidos. O Texas possui uma rede elétrica independente, não compartilhando seus recursos energéticos com outros estados. Essa característica faz com que o Texas produza frequentemente mais eletricidade do que o necessário para evitar escassez, criando assim um excedente. Os mineradores de Bitcoin se beneficiam desse excedente ao se estabelecerem no Texas, onde podem minerar bitcoins a tarifas de eletricidade muito baixas durante os períodos de excedente energético. Essa situação demonstra a influência significativa da regulação e das tarifas de eletricidade na mineração de Bitcoin, destacando a importância desses fatores na decisão dos mineradores sobre a localização de suas operações de mineração.

### Para onde vão os mineradores e o gerenciamento de energia?

Ao destacar o impacto dos mineradores de bitcoins no mundo da energia, a trajetória é clara: esses atores estão constantemente em busca de fontes de eletricidade baratas, muitas vezes aquelas que são desperdiçadas ou não utilizadas. Esse fenômeno é evidente em regiões com novas infraestruturas elétricas, como aquelas equipadas com usinas hidrelétricas recentes.
Vamos dar um exemplo. Em um país em processo de construção de uma barragem, a produção de eletricidade muitas vezes começa antes que as linhas de distribuição estejam totalmente operacionais. Essa diferença pode resultar em um custo significativo e desencorajar o investimento em projetos de infraestrutura desse tipo. No entanto, os mineradores de bitcoins podem atuar como uma fonte de demanda flexível, prontos para consumir essa eletricidade "órfã", ajudando assim a amortizar os custos de infraestrutura. A implicação aqui é que novas instalações podem ser rentabilizadas imediatamente, promovendo a criação de novas fontes de eletricidade. Esse princípio também se aplica em escalas menores. Seja um indivíduo usando um gerador hidrelétrico em um pequeno rio ou uma residência equipada com painéis solares, o excedente de eletricidade produzido pode ser usado para alimentar uma operação de mineração de bitcoins.

Na França, por exemplo, o excedente de eletricidade dos painéis solares é injetado na rede e os produtores são remunerados com créditos de consumo pela EDF. De forma semelhante, pode-se imaginar um minerador operando com esse excedente de eletricidade, desligando-se quando a demanda local igualar a oferta. Embora isso possa parecer egoísta, priorizando a produção de bitcoins em vez de apoiar a rede elétrica local, isso apresenta outro ângulo: a estabilização da rede elétrica. A complexa gestão do excedente de eletricidade, às vezes com custos associados à sua eliminação, pode ser grandemente simplificada. Os mineradores de bitcoins podem absorver esses excedentes, atuando como um buffer flexível, ajustando a demanda em vez da oferta. Em um mundo onde a produção de eletricidade a partir de fontes renováveis (pouco controláveis) está em constante aumento, os mineradores podem desempenhar um papel fundamental para garantir o equilíbrio de nossas redes elétricas, ao mesmo tempo em que se beneficiam da eletricidade barata ou excedente para alimentar suas operações de mineração.

### A centralização da mineração

A centralização da mineração é abordada como um desafio significativo. Grandes players, como a Foundry, dominam o mercado, o que pode potencialmente levar à censura de transações. Essa centralização também pode tornar a rede vulnerável a ataques, como o ataque de 51%, em que um ator ou grupo controla mais de 50% do poder de hash da rede, permitindo assim o controle e manipulação da rede.
Risco de Regulação É destacado que se um país como os Estados Unidos decidir regular ou proibir certas transações de Bitcoin, isso pode ter um impacto significativo na rede, especialmente se uma grande parte do poder de hash estiver centralizada nesse país.

![image](assets/en/06.webp)

Para combater essa centralização, diferentes estratégias são discutidas:

- Attakai: Attakai est un concept qui consiste à utiliser la chaleur générée par l'activité de minage pour chauffer les domiciles. Cela permet de réduire les coûts de chauffage tout en contribuant à l'activité de minage. Cette approche est une façon innovante d'utiliser l'énergie produite par le minage de cryptomonnaies de manière plus efficace et durable.

Na atualidade, a prática da mineração de Bitcoin em S9 pode parecer complexa, mas uma análise mais profunda abre caminho para alternativas inovadoras. O princípio do Attakai baseia-se em uma reflexão sobre o uso de instalações de mineração em vários tipos de edifícios, como escolas ou hospitais. A ideia principal é ter algumas máquinas de mineração em diferentes locais, permitindo assim reutilizar o calor emitido por essas máquinas para aquecer as instalações. Optando por modelos mais eficientes, como o S19, seria possível distribuir a atividade de mineração, promovendo um melhor desempenho geral e contribuindo de forma útil para a sociedade. Essa iniciativa visa competir com grandes instalações de mineração centralizadas, utilizando o calor gerado pelas máquinas de mineração de forma produtiva e eficiente.

A iniciativa Attakai surgiu de uma experiência pessoal de mineração em casa, realizada por dois amigos que desejavam participar ativamente da rede Bitcoin. Eles enfrentaram obstáculos significativos, como o alto nível de ruído dos equipamentos de mineração, projetados para uso industrial e não doméstico. Para contornar esse problema, foram feitas modificações nos equipamentos de mineração. Ventiladores mais eficientes e silenciosos substituíram os equipamentos originais, tornando a mineração em casa mais acessível e menos perturbadora. Além disso, a adição de um adaptador Wi-Fi eliminou a necessidade de uma conexão Ethernet por cabo, simplificando ainda mais o processo de mineração em casa. No inverno, esses mineradores modificados foram utilizados como fonte de aquecimento, transformando um incômodo em benefício.

Ao expor seu projeto à comunidade Bitcoin e diante do interesse despertado, os inventores do Ataka decidiram publicar guias detalhados na plataforma Découvre Bitcoin, permitindo que qualquer pessoa reproduza sua experiência de mineração em casa. Agora eles estão planejando expandir esse conceito além do âmbito doméstico. O objetivo é demonstrar como um minerador modificado pode ser transformado em um aquecedor silencioso para uso durante o inverno, oferecendo uma transição suave para uma segunda parte de treinamento dedicada à implementação prática dessas modificações, ilustrada por vídeos explicativos. No entanto, a questão permanece se essa iniciativa pode ser estendida em uma escala maior, oferecendo assim uma alternativa realista e sustentável às estruturas de mineração centralizadas atuais.

![image](assets/en/07.webp)

### O limite dessa descentralização?

Embora a ideia de descentralização da mineração através do uso produtivo do calor produzido pareça promissora, ela tem algumas limitações e questões permanecem. Estabelecimentos com alto consumo de energia, como saunas e piscinas, podem se beneficiar desse conceito usando o calor produzido pelos mineradores para aquecer a água de suas instalações. Essa prática já está sendo implementada por alguns membros da comunidade Bitcoin, que estão explorando diferentes métodos para usar eficientemente o calor gerado pelos equipamentos de mineração. Por exemplo, uma sala de festas teoricamente poderia ser aquecida por três ou quatro S19, cada um consumindo 3000 watts e produzindo uma quantidade equivalente de calor.

No entanto, é importante ressaltar que o consumo de energia e a produção de calor são equivalentes, seja a energia usada por um aquecedor elétrico ou por um minerador. Para cada quilowatt de eletricidade usado, a quantidade de calor produzida será a mesma em ambos os casos. A diferença está no fato de que o minerador fornecerá não apenas o calor, mas também uma recompensa em bitcoin, oferecendo assim um incentivo econômico para usar um minerador em vez de um simples aquecedor elétrico. Essa recompensa adicional pode ajudar a mitigar as preocupações com o alto consumo de energia dos mineradores.

A questão da eficiência e viabilidade a longo prazo do uso de mineradores de bitcoin para aquecimento ainda está em aberto. Inovações contínuas no hardware de mineração e nas tecnologias de aquecimento podem potencialmente abrir novos caminhos para um uso mais eficiente do calor gerado pela mineração, contribuindo assim para a viabilidade dessa abordagem no futuro.

### Por que ter recompensas em BTC?

A questão da recompensa em bitcoin em vez de outra moeda é fundamental no sistema imaginado por Satoshi Nakamoto. A criação do Bitcoin é caracterizada por um limite fixo de 21 milhões de unidades. O objetivo era encontrar uma maneira justa de distribuir essas unidades recém-criadas. Os mineradores, ao fornecerem seu poder de computação para garantir a segurança da rede, tornando qualquer ataque cada vez mais custoso, efetivamente protegem a rede Bitcoin. Em troca dessa contribuição crucial, eles são recompensados com os novos bitcoins criados, facilitando assim a distribuição das moedas no ecossistema.
É um sistema ganha-ganha. Os mineradores são remunerados tanto pela segurança da rede quanto pela aprovação das transações.

Os novos bitcoins criados são dados como incentivo para fortalecer a segurança, e as taxas de transação são uma renda adicional para aprovar as transações. Esses dois elementos combinados constituem a recompensa total pela mineração. A questão do futuro da mineração surge devido à redução programada das recompensas de mineração, que diminuem pela metade a cada quatro anos, em um evento conhecido como "halving". Até 2032, a recompensa do bloco será inferior a um bitcoin, e em 2140, nenhum novo bitcoin será criado. Nesse ponto, os mineradores dependerão apenas das taxas de transação para remuneração. A rede Bitcoin precisará suportar uma grande quantidade de transações, com taxas suficientemente altas, para garantir a rentabilidade da mineração.

A ascensão da Lightning Network, que permite transações rápidas e de baixo custo fora da cadeia principal do Bitcoin, levanta questões sobre o futuro da mineração. A Lightning Network tem o potencial de reduzir significativamente as taxas de transação, afetando assim a receita dos mineradores. No entanto, isso dependerá da adoção e uso da Lightning Network em relação à rede principal do Bitcoin. Em um cenário pessimista, os mineradores podem achar lucrativo minerar mesmo com prejuízo, se tiverem amortizado seus custos e tiverem acesso a eletricidade barata. Em um cenário mais otimista, as taxas de transação na rede principal do Bitcoin podem permanecer suficientemente altas para manter a rentabilidade da mineração.

### O que deve ser incluído em um bloco Bitcoin?

Quanto à questão do que deve ser incluído em um bloco Bitcoin, é crucial considerar a natureza complementar das diferentes camadas da rede Bitcoin. Embora a Lightning Network possa permitir transações mais rápidas e mais baratas, ela ainda depende da camada base do Bitcoin, frequentemente chamada de "camada de liquidação", para a abertura e fechamento dos canais de pagamento.

Com o crescimento previsto da Lightning Network e o consequente aumento na abertura e fechamento de canais, o espaço nos blocos do Bitcoin se tornará cada vez mais valioso. A comunidade Bitcoin já tende a valorizar a preservação desse espaço, reconhecendo sua limitação intrínseca. Essa conscientização levou a discussões sobre o uso legítimo ou não do espaço dos blocos, com preocupações sobre "spam" na blockchain por transações consideradas não essenciais.

![image](assets/en/08.webp)

A especulação cerca do uso futuro do espaço de blocos, mas é geralmente aceito que é um recurso escasso que deve ser usado com sabedoria. Mesmo que haja vontade de preencher esse espaço, é essencial preservá-lo para garantir a viabilidade de longo prazo da rede Bitcoin, antecipando um aumento futuro na demanda por espaço de blocos. Como em qualquer mercado livre, a oferta e a demanda regularão o uso do espaço de blocos. Com oferta limitada, as partes interessadas terão que tomar decisões informadas sobre o uso desse espaço valioso para garantir a eficiência e a segurança de longo prazo da rede Bitcoin.

## A mineração no protocolo bitcoin

<chapterId>7b9ee427-316a-54e3-a2d4-4ea97839a31b</chapterId>

![Quem tem o poder? Bitcoin, energia e fabricantes](https://www.youtube.com/watch?v=4wywK6BfDw8)

O papel dos mineradores na rede Bitcoin foi um tópico de debate intenso durante a guerra dos blocos. Embora sejam essenciais para a segurança e a funcionalidade da rede, os mineradores não necessariamente detêm o poder supremo no ecossistema Bitcoin. O equilíbrio entre os mineradores, os nós e os usuários finais garante a integridade e a distribuição da rede.

### A guerra dos blocos

Durante a guerra dos blocos, muitos mineradores se opuseram a certas evoluções da rede, destacando a tensão entre os diferentes atores do ecossistema. A questão permanece sobre como equilibrar o poder entre os mineradores, os nós e os usuários para assegurar a segurança a longo prazo do Bitcoin.

![image](assets/en/09.webp)

O dilema da segurança do Bitcoin repousa em um equilíbrio delicado. Embora os mineradores desempenhem um papel crucial na validação e criação de blocos, os nós mantêm a integridade ao verificar e validar as transações e os blocos. Um bloco incorreto ou fraudulento será recusado pelos nós, censurando assim o minerador e preservando a segurança da rede. O poder também é detido pelos nós e pelos usuários da rede Bitcoin. Os nós têm o poder de verificação e validação, enquanto os usuários têm o poder de escolher qual cadeia de blocos utilizar. Esta distribuição de poder assegura a distribuição e a integridade da rede Bitcoin.

A guerra dos blocos revelou a incerteza e a tensão inerentes à gestão da rede Bitcoin. Embora o Bitcoin Core seja atualmente a cadeia dominante, o debate sobre a governança e a gestão da rede continua.

No final das contas, a responsabilidade é compartilhada entre todos os atores da rede Bitcoin. Uma diminuição no número de usuários, de nós ou de mineradores poderia enfraquecer a rede, aumentando o risco de centralização e vulnerabilidade a ataques. Cada ator contribui para a robustez e segurança da rede, reforçando a importância de manter um equilíbrio de poder e responsabilidade.

### O poder dos mineradores

A elegante teoria dos jogos de Satoshi Nakamoto estabeleceu uma situação em que cada participante da rede Bitcoin é incentivado a agir corretamente para proteger tanto seus próprios interesses quanto os dos outros participantes. Isso cria um equilíbrio onde comportamentos inadequados podem ser repreendidos, reforçando assim a segurança e a estabilidade de todo o sistema. Apesar desse equilíbrio, os Estados permanecem uma ameaça potencial. Como indicado na apresentação no Surfing Bitcoin 2022, os Estados podem tentar atacar a indústria de mineração, expondo a rede Bitcoin a riscos de centralização e ataque. Cenários hipotéticos como um ataque militar visando instalações de produção de equipamentos de mineração destacam a importância da diversificação geográfica e industrial para a resiliência da rede Bitcoin.
![image](assets/en/10.webp)

A centralização da produção de equipamentos de mineração na China representa outro risco. A recusa em exportar máquinas de mineração ou a acumulação de hashrate para um possível ataque de 51% pela China sublinham a necessidade de uma produção diversificada de equipamentos de mineração. Diante desses riscos, a comunidade Bitcoin está ativamente explorando soluções. Empresas como a Intel estão considerando produzir equipamentos de mineração nos Estados Unidos, contribuindo para a distribuição da produção. Outras iniciativas, como a da Block com seu Mining Development Kit (MDK) de código aberto, visam diminuir o monopólio do design e da produção de equipamentos de mineração, permitindo uma distribuição mais ampla do hashrate. No coração dessas discussões está a missão fundamental do Bitcoin: ser uma rede de troca de valor resistente à censura. A comunidade Bitcoin se esforça constantemente para fortalecer a distribuição, a resistência à censura e a antifragilidade da rede, rejeitando propostas como a transição para o proof of stake, que não estão alinhadas com esses princípios fundamentais.

### O Elo físico do proof of work versus o proof of stake

O Proof of Work (PoW) é essencial porque representa o elo físico entre o mundo real e o Bitcoin. Embora os bitcoins sejam intangíveis, sua produção requer energia tangível, estabelecendo assim uma conexão direta com o mundo físico e real. Essa conexão garante que a produção e a validação dos bitcoins e dos blocos tenham um custo energético real, ancorando assim a rede Bitcoin na realidade física e impedindo sua dominação completa por entidades poderosas. O PoW atua como um baluarte contra a centralização, garantindo que a participação na rede e a validação das transações exijam um investimento em recursos tangíveis. Isso impede a monopolização da rede por entidades que poderiam de outra forma assumir o controle sem nenhuma barreira de entrada significativa, assegurando assim uma distribuição mais equitativa do poder e da influência dentro da rede Bitcoin.

![image](assets/en/11.webp)

### As Limitações do Proof of Stake

Por outro lado, o Proof of Stake (PoS), embora permita a participação em pequena escala, não garante uma proteção equivalente contra a centralização. Em uma rede PoS, aqueles que já possuem uma grande quantidade da moeda têm um poder desproporcional, refletindo as desigualdades de poder existentes na sociedade em geral. Essa dinâmica poderia potencialmente perpetuar a centralização e a concentração de poder nas mãos de poucos, contrariando os objetivos fundamentais de distribuição da rede Bitcoin. O argumento de que todos podem participar do PoS, mesmo em pequena escala, ao se juntar a pools, não é necessariamente sólido. Em uma rede PoW, mesmo um pequeno contribuinte, com equipamento modesto, pode participar ativamente e contribuir para a segurança e distribuição da rede.

### Recapitulação

Para recapitular, os mineradores fortalecem a rede Bitcoin contra a censura usando eletricidade para calcular a prova de trabalho do Bitcoin, e são recompensados com novos bitcoins e taxas de transação. Com a profissionalização da indústria, diferentes atores emergem, desempenhando diversos papéis, desde a criação de chips até a gestão de fazendas de mineração. Além disso, o setor financeiro também intervém, exercendo controle ao decidir quem sobrevive durante as diferentes fases do mercado. A problemática da centralização persiste, com as entidades mais ricas potencialmente dominando o mercado. No entanto, alternativas estão sendo desenvolvidas em nível de hardware e software. Cabe a cada indivíduo agir e contribuir para a distribuição da rede. Bitcoin representa uma oportunidade extraordinária não apenas em termos de liberdade, mas também de independência energética. Apesar das controvérsias em torno de seu consumo de eletricidade, Bitcoin oferece um incentivo econômico para uma transição para um uso mais racional e abundante de energia, concretizando o que antes era um ideal ecológico.

## Preço do Bitcoin e Hashrate, uma correlação?

<chapterId>879a66b0-c20a-56b5-aad0-8a21be61e338</chapterId>

![Como obter um bitcoin branco e puro?](https://youtu.be/A5MTtn4mm44?si=D1Yi0dVwkyafeHv-)

### Hashrate, Preço e Rentabilidade

O atual índice de hash, mesmo com o preço do Bitcoin estando a 30.000 dólares em comparação ao seu pico anterior de 69.000 dólares, destaca a conexão tangível entre a mineração e o mundo real. Períodos de alta nos preços (mercado em alta) geram uma forte demanda por mineração de Bitcoin e um aumento nos pedidos de máquinas de fabricantes como Avalon e Bitmain. No entanto, a produção e a entrega não são instantâneas, criando um descompasso entre uma demanda crescente e uma disponibilidade posterior. Isso pode levar à entrega de máquinas encomendadas durante um mercado em alta em um mercado em baixa, destacando uma assimetria notável entre um preço baixo e um índice de hash elevado.

Esta situação também ilustra a resiliência do Bitcoin, frequentemente avaliada pelo seu preço. Contudo, uma análise mais aprofundada da saúde do Bitcoin requer a avaliação de seu índice de hash, que mede os cálculos por segundo na rede Bitcoin. Enquanto o preço do Bitcoin flutua, seu custo, ligado à eletricidade necessária para operar as máquinas de mineração, permanece essencial para entender a dinâmica do mercado. Ao focar no custo em vez do preço, obtém-se uma perspectiva mais consistente sobre a estabilidade e a viabilidade a longo prazo do Bitcoin. Em geral, o custo do Bitcoin é proporcional ao seu preço, oferecendo uma melhor compreensão das flutuações de preço e das perspectivas futuras.

![image](assets/en/12.webp)

### Índice de Hash e Recompensa

A mineração estabelece um preço mínimo para o Bitcoin, abaixo do qual os mineradores venderiam com prejuízo. O custo da mineração influencia significativamente o preço, como ilustrado pela proibição da mineração na China, onde o índice de hash e o preço caíram significativamente, mas foram rapidamente recuperados. Focar apenas no preço pode ser enganador. O estudo do custo, através de calculadoras de rentabilidade, oferece uma perspectiva mais equilibrada. No entanto, o mercado pode se comportar de maneira irracional, com os mineradores podendo ser forçados a vender com prejuízo, potencialmente baixando o preço abaixo do custo de mineração. Para avaliar a saúde do Bitcoin e sua descentralização, uma equação que integre diversos fatores, como o número de nós e o preço, poderia ser desenvolvida. Essa abordagem poderia fornecer uma análise mais matizada do Bitcoin em comparação às discussões baseadas apenas no preço.

### Minerar para o lucro ou para a rede?

A questão é profunda e abrange várias dimensões da mineração de Bitcoin. O equilíbrio entre a busca por lucro e a contribuição para a segurança e a distribuição da rede Bitcoin é um dilema constante para os mineradores. O debate continua na comunidade Bitcoin, com argumentos sólidos de ambos os lados.

- Minerar para o lucro:

## Mineração para a Rede:

<chapterId>e6676214-007c-5181-968e-c27536231bd6</chapterId>

### Prós:

- Mineração para contribuir com a segurança e a descentralização da rede Bitcoin é uma iniciativa nobre. Isso ajuda a fortalecer a resiliência da rede e a resistir à censura e ataques.

### Contras:

- Sem um incentivo financeiro suficiente, pode ser difícil para os mineiros continuar apoiando a rede, especialmente se estiverem operando com prejuízo.

A iniciativa Attakai destaca a importância da contribuição para a rede enquanto oferece soluções para tornar a mineração mais acessível e menos prejudicial. A possibilidade de minerar em casa, com equipamento mais acessível e soluções para reduzir a poluição sonora, pode ajudar a democratizar a mineração de Bitcoin. Ela incentiva aqueles que têm interesse no Bitcoin não apenas a investir e possuir bitcoins, mas também a participar ativamente na segurança da rede. Ao fornecer equipamentos testados e guias para montagem e instalação, Attakai facilita a entrada no mundo da mineração de Bitcoin. Também incentiva a inovação e melhorias contínuas, convidando a comunidade a contribuir e compartilhar suas ideias e experiências para aprimorar a mineração doméstica. O modelo Attakai é uma resposta à questão de minerar para lucro ou para a rede. Não se trata apenas de realizar lucros, mas também de fortalecer a distribuição e a segurança da rede Bitcoin, permitindo que mais pessoas participem da mineração, aprendam e compreendam essa indústria crucial. O desafio da possível proibição da mineração na Europa permanece uma questão em aberto. Isso levanta preocupações sobre o futuro da mineração de Bitcoin na região e a necessidade de uma regulação equilibrada que reconheça a importância da mineração para a segurança e viabilidade da rede Bitcoin, enquanto aborda as questões ambientais. Attakai e outras iniciativas similares podem desempenhar um papel crucial neste debate, mostrando que é possível minerar de maneira mais sustentável e responsável, contribuindo positivamente para a rede Bitcoin.

## Soberania e Regulação

<chapterId>9d9a5908-2acc-501e-906b-a6fce9ecfebd</chapterId>

### Soberania antes do lucro?

Para abordar a questão crucial da riqueza por meio da mineração, é importante considerar diversas perspectivas e abordagens. As questões sobre a rentabilidade da mineração são frequentes, com perguntas sobre a compra de participações em empresas como a Riot ou o aluguel de máquinas de mineração em países com baixo custo energético, como Islândia ou Rússia. Antes de se aventurar na mineração, uma consideração essencial seria comparar a rentabilidade da mineração com a compra direta de Bitcoin. Se o custo de mineração de um Bitcoin exceder o custo de compra direta, geralmente é mais sensato comprar o Bitcoin diretamente. Isso evita os múltiplos desafios e custos associados ao processo de mineração.

No entanto, a mineração oferece vias únicas para se envolver no ecossistema Bitcoin. Por exemplo, minerar Bitcoin no inverno pode ser uma maneira engenhosa de aquecer sua residência enquanto gera renda em Bitcoin. Outra opção é investir em empresas que vendem equipamentos de mineração e que armazenam e gerenciam as máquinas em locais com baixo custo energético, oferecendo assim acesso a tarifas elétricas vantajosas sem os transtornos de gerenciar os equipamentos.

Apesar dessas opções, a mineração apresenta desafios significativos. O adágio bem conhecido do mundo das criptomoedas, "Não são suas chaves, não são seus Bitcoins", encontra uma ressonância similar no mundo da mineração: "Não é seu hashrate, não é sua recompensa". Histórias de decepções e máquinas desconectadas são comuns, com muitos atores prometendo resultados excepcionais, mas não os entregando. Problemas de fornecimento de energia e falhas de máquinas podem deixar os investidores impotentes, com equipamentos caros que eles não controlam. Neste contexto, a prudência e um entendimento profundo do setor de mineração são cruciais antes de se aventurar. Embora existam oportunidades de ganhos, os riscos são significativos, e uma abordagem informada e reflexiva é essencial para navegar neste campo complexo e frequentemente imprevisível. Portanto, é vital fazer pesquisas aprofundadas e avaliar bem os prós e contras antes de se engajar na mineração de Bitcoin.

![image](assets/en/13.webp)

### Bitcoins Virgens

A aspiração de possuir seu próprio hashrate apresenta-se como um caminho promissor no universo da mineração. No entanto, navegar neste ecossistema complexo requer uma abordagem cautelosa. O campo do cloud mining é marcado por um grande número de fraudes, alimentadas por uma falta de compreensão da mineração por parte de muitos investidores. As ofertas atraentes, embaladas de diversas maneiras, podem facilmente induzir em erro aqueles que não estão suficientemente informados. Por outro lado, possuir seu próprio equipamento de mineração oferece vantagens consideráveis. Além da satisfação pessoal de contribuir ativamente para a segurança da rede Bitcoin e de ver as recompensas caindo em sua carteira, há o aspecto atraente dos "bitcoins virgens". Trata-se de bitcoins recém-minados, que nunca foram gastos e que não têm nenhuma história associada a eles. Esses bitcoins são frequentemente considerados mais valiosos porque nunca foram "contaminados", oferecendo uma certa garantia contra a rejeição por reguladores ou grandes plataformas de troca.

A possibilidade de minerar bitcoins virgens enquanto se evita os procedimentos de conhecimento do cliente (KYC) é outro valor agregado. Muitos pools de mineração não exigem a identidade dos mineradores, permitindo assim adquirir bitcoins sem passar por verificações de identidade tediosas. Os bitcoins virgens são percebidos como "limpos", não carregando nenhuma história ou associação passada. Eles são particularmente procurados por grandes atores institucionais que podem garantir a legitimidade de seus ativos digitais frente às autoridades reguladoras. No entanto, apesar dessas vantagens, é crucial reconhecer que a indústria da mineração permanece extremamente competitiva e volátil e incidentes imprevistos podem perturbar as operações de mineração.

Neste contexto, a escolha de uma abordagem autônoma e educada em matéria de mineração parece prudente. A aquisição de seu próprio hashrate e o investimento em equipamentos de mineração pessoais, enquanto se mantém consciente dos riscos e desafios, pode potencialmente oferecer um caminho mais seguro e mais satisfatório para a aquisição de bitcoins virgens, reforçando assim a soberania financeira do indivíduo enquanto apoia o ecossistema Bitcoin como um todo.

### A mineração é proibida na Europa?

Com a questão do potencial de proibição da mineração na Europa, as discussões sobre regulamentação tornam-se cada vez mais pertinentes. O cenário regulatório flutuante pode, de fato, influenciar consideravelmente a indústria de mineração de Bitcoin. A proibição da mineração na Europa é um cenário possível, especialmente considerando os precedentes na China. Embora as operações de mineração continuem na China apesar da proibição, a Europa poderia seguir um caminho similar. Uma distribuição mais ampla do hashrate em diferentes regiões poderia ajudar a fortalecer a comunidade de mineradores na Europa, permitindo-lhes opor-se eficazmente aos mal-entendidos e às ideias erradas sobre a mineração, seu impacto ambiental e sua pegada na rede elétrica.
![image](assets/en/14.webp)

Diante de campanhas como as da Greenpeace e dos números frequentemente enganosos de alguns estudos, a melhor arma continua sendo a informação verdadeira. É essencial informar o público em geral e os tomadores de decisão sobre a realidade da mineração, sua complexidade e nuances, em vez de deixá-los depender de clichês e informações imprecisas. Quanto mais pessoas estiverem informadas e conscientes do que realmente é a mineração, melhor a indústria poderá se defender contra possíveis regulamentações restritivas.

Em conclusão, apesar do risco regulatório e da possibilidade de uma proibição da mineração na Europa, a arma mais poderosa continua sendo a educação e a informação. A compreensão clara e precisa da mineração, seu funcionamento e seu impacto pode ajudar a desmistificar a indústria e combater a desinformação, oferecendo assim uma melhor resistência às regulamentações potencialmente prejudiciais. A iniciativa de formar e informar as pessoas sobre a mineração, como faz esta discussão, é um passo na direção certa para garantir a sustentabilidade e o crescimento da mineração na Europa e em todo o mundo. Os esforços contínuos para educar e informar são essenciais para assegurar um futuro seguro e próspero para a indústria de mineração de Bitcoin.

## Entrevista com um profissional da indústria de mineração

<chapterId>4d613261-d1a8-5ffe-a50c-047a3d77d6c5</chapterId>

### Bastidores da mineração industrial - Sebastien Gouspillou

![Bastidores da mineração industrial - Sebastien Gouspillou](https://www.youtube.com/watch?v=vYaQRLSDr5E&t=69s)

# Mineração doméstica e reutilização de calor

<partId>78d22d06-2c4a-573f-86bb-1027115dad3a</partId>

## Attakai - tornando a mineração doméstica possível e acessível!

<chapterId>1f5d1b74-2f99-5f31-a088-a73d36491ebf</chapterId>

Attakai, que significa "temperatura ideal" em japonês, é o nome da iniciativa para descobrir a mineração de bitcoins por meio da reutilização de calor lançada por @ajelexBTC e @jimzap21 com o Découvre Bitcoin.
Este guia de retrofitting de um ASIC servirá como base para aprender mais sobre mineração, seu funcionamento e a economia subjacente, demonstrando a possibilidade de adaptar um minerador de Bitcoin para uso como radiadores em residências. Isso oferece mais conforto e economia, permitindo que os participantes recebam cash back em BTC não KYC em sua conta de energia elétrica.

O Bitcoin ajusta automaticamente a dificuldade de mineração e recompensa os mineradores por sua participação, no entanto, a concentração da taxa de hash pode representar riscos para a neutralidade da rede. Utilizar o poder de computação do Bitcoin para soluções de aquecimento beneficia diretamente a própria rede, aumentando a distribuição do poder de computação.

### Por que reutilizar o calor de um ASIC?

É importante entender a relação entre energia e produção de calor em um sistema elétrico.

Para um investimento de 1 kW de energia elétrica, um radiador elétrico produz 1 kW de calor, nem mais nem menos. Os novos radiadores não são mais eficientes do que os radiadores tradicionais. Sua vantagem está em sua capacidade de distribuir o calor de forma contínua e uniforme em um ambiente, proporcionando mais conforto em comparação com os radiadores tradicionais, que alternam entre alta potência de aquecimento e ausência de aquecimento, gerando variações regulares de temperatura e desconforto.

Um computador, ou mais amplamente uma placa eletrônica, não consome energia para realizar cálculos, ele apenas precisa que a energia circule em seus componentes para funcionar. O consumo de energia é devido à resistência elétrica dos componentes, que gera perdas e, portanto, calor, isso é chamado de efeito Joule.

Algumas empresas tiveram a ideia de combinar as necessidades de energia de computação e as necessidades de aquecimento por meio de radiadores/servidores. A ideia é distribuir os servidores de uma empresa em pequenas unidades que podem ser colocadas em residências ou escritórios. No entanto, essa ideia enfrenta vários problemas. A necessidade dos servidores não está relacionada à necessidade de aquecimento e as empresas não podem usar as capacidades de computação de seus servidores de forma flexível. Também existem limites para a largura de banda que os indivíduos podem ter. Todas essas restrições impedem que a empresa rentabilize essas instalações caras ou forneça um serviço de servidor online estável sem ter data centers capazes de assumir quando não há necessidade de aquecimento.

> A energia térmica do seu computador não é desperdiçada se você precisar aquecer sua casa. Se você usa um aquecedor elétrico onde mora, então o calor do seu computador não é desperdício. É o mesmo custo se você gerar esse calor com seu computador. Se você tiver um sistema de aquecimento mais barato do que o elétrico, então o desperdício está apenas na diferença de custo. Se for verão e você estiver usando ar condicionado, então é o dobro. A mineração de bitcoins deve ocorrer onde for mais barata. Talvez seja onde o clima é frio e o aquecimento é elétrico, onde minerar se tornará gratuito.
> Satoshi Nakamoto - 8 de agosto de 2010

O Bitcoin e sua prova de trabalho se destacam porque ajustam automaticamente a dificuldade da mineração com base na quantidade de cálculos realizados por toda a rede, essa quantidade é chamada de hashrate e é expressa em hash/segundo. Atualmente, estima-se que seja de 380 Exahash/segundo, ou seja, 380 bilhões de bilhões de hash/segundo. Esse hashrate representa trabalho e, portanto, uma quantidade de energia gasta. Quanto maior o hashrate, maior a dificuldade e vice-versa. Assim, é possível ativar ou desativar um minerador de Bitcoin a qualquer momento sem impacto na rede, ao contrário de radiadores/servidores que precisam permanecer estáveis para oferecer seu serviço. O minerador é recompensado por sua participação, mesmo que seja pequena em relação aos outros.

Resumindo, um radiador elétrico e um minerador de Bitcoin produzem ambos 1 kW de calor para 1 kW de eletricidade gasta. No entanto, o minerador também recebe bitcoins como recompensa. Independentemente do preço da eletricidade, do preço do bitcoin ou da concorrência na atividade de mineração na rede Bitcoin, é economicamente mais vantajoso aquecer-se com um minerador do que com um radiador elétrico.

### O valor agregado para o Bitcoin

O que é importante entender é como a mineração contribui para a descentralização do Bitcoin.

Várias tecnologias já existentes foram combinadas de forma engenhosa para dar vida ao consenso de Nakamoto. Esse consenso permite recompensar economicamente os atores honestos por sua participação no funcionamento da rede Bitcoin, ao mesmo tempo em que desencoraja os atores desonestos. Esse é um dos pontos-chave que permite a existência sustentável da rede.
Os atores honestos, aqueles que mineram de acordo com as regras, estão competindo entre si para obter a maior parte possível da recompensa pela produção de novos blocos. Esse incentivo econômico naturalmente leva a uma forma de centralização, pois as empresas optam por se especializar nessa atividade lucrativa, reduzindo seus custos por meio de economias de escala. Esses atores industriais têm uma posição vantajosa para a compra, manutenção de máquinas e negociação de tarifas de eletricidade no atacado.

> No início, a maioria dos usuários executaria nós de rede, mas à medida que a rede se expandisse além de um certo ponto, ela seria cada vez mais deixada para especialistas com fazendas de servidores de hardware especializado. Uma bateria de servidores precisaria de apenas um nó na rede e o restante da LAN se conectaria a esse nó.
>
> Satoshi Nakamoto - 2 de novembro de 2008

Algumas entidades possuem uma porcentagem considerável da taxa de hash total em grandes fazendas de mineração. Podemos observar a recente onda de frio nos Estados Unidos, onde uma parte significativa da taxa de hash foi desligada para permitir que a energia fosse redirecionada para residências com necessidades excepcionais de eletricidade. Por vários dias, os mineradores foram incentivados economicamente a desligar suas fazendas e, portanto, podemos ver esse clima excepcional na curva da taxa de hash do Bitcoin.

Esse assunto pode se tornar problemático e representa um risco significativo para a neutralidade da rede. Um ator que possua mais de 51% da taxa de hash poderia facilmente censurar transações, se assim o desejasse. Portanto, é importante distribuir a taxa de hash entre vários atores, em vez de entidades centralizadas que poderiam ser facilmente apreendidas por um governo, por exemplo.

**Se os mineradores estiverem distribuídos em milhares, ou até mesmo milhões, de residências ao redor do mundo, se torna muito difícil para um Estado assumir o controle.**

Quando sai da fábrica, um minerador não é adequado para servir como aquecedor em uma residência, devido a dois problemas principais: ruído excessivo e falta de ajuste. No entanto, esses problemas podem ser facilmente resolvidos por meio de modificações de hardware e software, permitindo obter um minerador muito mais silencioso e que pode ser configurado e automatizado como os aquecedores elétricos modernos.

**Attakaï é uma iniciativa educacional que ensina como fazer uma adaptação do Antminer S9 da maneira mais econômica possível.**

Esta é uma excelente oportunidade para aprender praticando e ser recompensado por sua participação com satoshis KYC gratuitos.

## Guia de compra para um ASIC usado

<chapterId>3b0b3bf0-859b-57f2-b92f-843ac70b7e68</chapterId>

Nesta seção, veremos as melhores práticas para comprar um Bitmain Antminer S9 usado, a máquina na qual este tutorial de retrofitting em radiador será baseado. Este guia também funciona para outros modelos de ASIC, pois é um guia geral de compra de hardware de mineração usado.

O Antminer S9 é um dispositivo oferecido pela Bitmain desde maio de 2016. Ele consome 1400W de eletricidade e produz 13,5 TH/s. Embora seja considerado antigo, ainda é uma excelente opção para começar a mineração. Como foi produzido em grande quantidade, é fácil encontrar peças sobressalentes em abundância em muitas regiões do mundo. Geralmente, pode ser adquirido de forma peer-to-peer em sites como o Ebay ou LeBonCoin, pois os revendedores voltados para profissionais não o oferecem mais devido à sua menor competitividade em comparação com máquinas mais recentes. É menos eficiente do que ASICs como o Antminer S19, lançado em março de 2020, mas isso o torna um hardware usado acessível e mais adequado para as modificações que faremos.

O Antminer S9 existe em várias variantes (i, j) que trazem modificações menores ao hardware de primeira geração. Não acreditamos que esse fator deva influenciar sua decisão de compra, e este guia funciona para todas essas variantes.

O preço dos ASICs varia de acordo com vários fatores, como o preço do bitcoin, a dificuldade da rede, a eficiência da máquina e o custo da eletricidade. Portanto, é difícil dar uma estimativa precisa para a compra de uma máquina usada. Em fevereiro de 2023, o preço esperado na França geralmente varia entre 100€ e 200€, mas esses preços podem mudar rapidamente.

![image](assets/en/15.webp)

O Antminer S9 é composto pelas seguintes partes:

- 3 hashboards que contêm os chips que produzem o hash

![image](assets/en/16.webp)

- Um cartão de controle que inclui um slot para cartão SD, uma porta Ethernet e conectores para os hashboards e ventiladores. É o cérebro do seu ASIC.

![image](assets/en/17.webp)

- 3 cabos de dados que conectam os hashboards ao cartão de controle

![image](assets/en/18.webp)

- A fonte de alimentação que funciona em 220V e pode ser conectada como um eletrodoméstico comum

![image](assets/en/19.webp)

- 2 ventiladores de 120mm

![image](assets/en/20.webp)

- Um cabo macho C13

![image](assets/en/21.webp)

Quando você compra uma máquina usada, é importante verificar se todas as peças estão incluídas e funcionais. Durante a troca, você deve pedir ao vendedor para ligar a máquina e verificar se ela está funcionando corretamente. É importante verificar se o aparelho liga corretamente e, em seguida, verificar a conectividade com a internet conectando um cabo Ethernet e acessando a interface de login da Bitmain por meio de um navegador da web na mesma rede local. Você pode encontrar este endereço IP conectando-se à interface do seu roteador de internet e procurando os dispositivos conectados. Este endereço deve ter o seguinte formato: 192.168.x.x

![image](assets/en/22.webp)

Também verifique se as credenciais padrão funcionam (nome de usuário: root, senha: root). Se as credenciais padrão não funcionarem, será necessário redefinir a máquina.

![image](assets/en/23.webp)

Depois de conectado, você deve ser capaz de ver o status de cada hashboard no painel de controle. Se o minerador estiver conectado a uma pool, você deve ver todos os hashboards funcionando. É importante observar que os mineradores fazem muito barulho, isso é normal. Certifique-se também de que os ventiladores estejam funcionando corretamente.

Em seguida, você pode remover a pool de mineração do antigo proprietário para configurar a sua posteriormente. Se desejar, você também pode inspecionar os hashboards desmontando a máquina. No entanto, esta etapa é mais complexa e requer mais tempo e algumas ferramentas. Se você deseja prosseguir com essa desmontagem, pode consultar a próxima parte deste tutorial que detalha como fazê-lo. É importante observar que os mineradores acumulam muita poeira e requerem manutenção regular. É essa acumulação de poeira e a qualidade da manutenção que você pode observar desmontando a máquina.

Depois de revisar todos esses pontos, você pode comprar sua máquina com um alto grau de confiança. Em caso de dúvida, consulte a comunidade.

Para resumir este guia em uma frase: **"Não confie, verifique"**.

[Você também pode recorrer a profissionais de recondicionamento de máquinas de mineração, como nosso parceiro 21energy. Eles oferecem S9 testados, limpos e com o software BraiiinOS+ já instalado. Com o código de afiliação "decouvre", você receberá um desconto de 10% na compra de um S9, ao mesmo tempo em que apoia o projeto Attakai.](https://21energy.io/en/produkt/bitmain-antminer-s9-bundle/)

## Guia de compra de peças para modificações de hardware do S9

<chapterId>fa5f5eca-bcbf-5a83-9b03-98ecbadbabd6</chapterId>

Proprietário de um Antminer S9, você provavelmente sabe o quão barulhento e volumoso esse equipamento pode ser. No entanto, é possível transformá-lo em um aquecedor silencioso e conectado seguindo alguns passos simples. Nesta parte, apresentaremos os equipamentos necessários para fazer as modificações.

Se você é um habilidoso em trabalhos manuais e está procurando transformar um minerador em um aquecedor, este tutorial é para você. Gostaríamos de alertá-lo que as modificações feitas em um aparelho eletrônico podem apresentar riscos elétricos. Portanto, é essencial tomar todas as precauções necessárias para evitar danos ou ferimentos.

1. Substituir os ventiladores

Os ventiladores originais do Antminer S9 são muito barulhentos para usar o Antminer como aquecedor. A solução é substituí-los por ventiladores mais silenciosos. Nossa equipe testou vários modelos da marca Noctua e selecionou o Noctua NF-A14 iPPC-2000 PWM como a melhor opção, certifique-se de escolher a versão de 12V dos ventiladores. Este ventilador de 140mm pode produzir até 1200W de aquecimento, mantendo um nível teórico de ruído de 31 dB. Para instalar esses ventiladores de 140mm, você precisará usar um adaptador de 140mm para 120mm, que pode ser encontrado na loja DécouvreBitcoin. Também adicionaremos grades de proteção de 140mm.

![image](assets/en/24.webp)
![image](assets/en/25.webp)
![image](assets/en/26.webp)

O ventilador da fonte de alimentação também é bastante barulhento e precisa ser substituído. Recomendamos o Noctua NF-A6x25 PWM. Observe que os conectores dos ventiladores Noctua não são os mesmos que os originais, portanto, você precisará de um adaptador para conectá-los, 2 serão suficientes. Novamente, certifique-se de escolher a versão de 12V do ventilador.

![image](assets/en/27.webp)
![image](assets/en/28.webp)

2. Adicionar uma ponte WIFI/Ethernet

Em vez de usar um cabo Ethernet, você pode conectar seu Antminer via WIFI adicionando uma ponte WIFI/Ethernet. Selecionamos o vonets vap11g-300, pois ele permite facilmente captar o sinal WIFI do seu roteador e transmiti-lo para o Antminer via Ethernet sem criar uma sub-rede. Se você tiver habilidades elétricas, poderá alimentá-lo diretamente com a fonte de alimentação do Antminer, sem a necessidade de adicionar um carregador USB. Para isso, você precisará de uma tomada fêmea de 5,5mmx2,1mm.

![image](assets/en/29.webp)
![image](assets/en/30.webp)

3. Opcional: adicionar uma tomada conectada
   Se você deseja ligar/desligar seu Antminer pelo seu smartphone e monitorar seu consumo de energia, você pode adicionar uma tomada inteligente. Testamos a tomada ANTELA na versão 16A compatível com o aplicativo smartlife. Essa tomada inteligente permite consultar o consumo diário e mensal e se conecta diretamente ao seu roteador Wi-Fi.
   ![imagem](assets/en/31.webp)

Lista de materiais e links

- 2X adaptador 3D de 140mm para 120mm

- [2X NF-A14 iPPC-2000 PWM](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW/ref=sr_1_2?__mk_fr_FR=ÅMÅŽÕÑ&crid=JCNLC31F3ECM&keywords=NF-A14+iPPC-2000+PWM&qid=1676819936&sprefix=nf-a14+ippc-2000+pwm%2Caps%2C114&sr=8-2)

- [2X Grades de ventilador de 140mm](https://www.amazon.fr/dp/B06XD4FTSQ?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [Noctua NF-A6x25 PWM](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4/ref=sr_1_1_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=3T313ABZA5EDE&keywords=Noctua+NF-A6x25+PWM&qid=1676819329&sprefix=noctua+nf-a6x25+pwm%2Caps%2C71&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1&smid=A38F5RZ72I2JQ)

- [Fio elétrico de 2,5mm2](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS/ref=sr_1_3?__mk_fr_FR=ÅMÅŽÕÑ&crid=25IRJD7A0YN2A&keywords=sucre%2Belectrique%2B2mm2&qid=1676820815&sprefix=sucre%2Belectrique%2B2mm2%2Caps%2C84&sr=8-3&th=1)
- [Vonets vap11g-300](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W/ref=sr_1_3_sspa?__mk_fr_FR=ÅMÅŽÕÑ&crid=13Q33UHRKCKG5&keywords=vonet&qid=1676819146&s=electronics&sprefix=vonet%2Celectronics%2C98&sr=1-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
- [Tomada conectada opcional ANTELA](https://www.amazon.fr/dp/B09YYMVXJZ/ref=twister_B0B5X46QLW?_encoding=UTF8&psc=1)

# Attakai - modificação do software de um Antminer S9

<partId>afc9c29a-84aa-5f1d-82e2-5fd9ff2e1805</partId>

## Configurando uma ponte WIFI/Ethernet Vonet

<chapterId>3cf487a4-21ef-5b24-83d5-789b811f740f</chapterId>

Para conectar seu ASIC via Wi-Fi, você precisará de um dispositivo chamado ponte, que permite capturar o sinal Wi-Fi do seu roteador e transmiti-lo para outro dispositivo via Ethernet.

Existem muitos dispositivos que podem fazer isso, mas recomendamos o VONETS WiFi Bridge/Repeteur por sua praticidade.

Alimente a ponte conectando-a via USB.

A partir do seu computador, conecte-se à rede Wi-Fi VONETS\_**\*\*** com a senha 12345678.

![imagem](assets/en/32.webp)

identificador admin admin

![imagem](assets/en/33.webp)

Escolha o Assistente

![imagem](assets/en/34.webp)

Selecione a rede Wi-Fi à qual deseja conectar seu minerador e clique em Avançar

ATENÇÃO: a ponte Vonet funciona apenas em 2,4 GHz. Hoje em dia, os roteadores geralmente oferecem duas redes Wi-Fi, uma em 2,4 GHz e outra em 5 GHz.

![imagem](assets/en/35.webp)

Digite a senha da sua rede Wi-Fi em "Senha do ponto de acesso Wi-Fi de origem".
Se você não deseja usar sua ponte Vonet para estender sua rede Wi-Fi, marque a opção "Desativar ponto de acesso". Caso contrário, deixe essa opção desmarcada.

Em seguida, clique em Aplicar.

E, finalmente, clique em reiniciar. A ponte será reiniciada em alguns minutos.

A ponte deve se conectar ao seu roteador e aparecerá como "[VONETS.COM](http://vonets.com/)".
Se a ponte ainda não estiver conectada após alguns minutos, pode ser necessário desconectá-la e reconectá-la.

Depois de conectar a ponte, conecte o cabo Ethernet da ponte ao seu ASIC e ligue o ASIC à energia. Você poderá então se conectar à interface do ASIC da mesma forma que se estivesse conectado diretamente via Ethernet ao seu roteador.

## Ressetando um Antminer S9

<chapterId>b518b6bd-9dae-5136-ae3c-1fafb1cb2592</chapterId>

Antes de instalar o BraiinOS+, pode ser necessário redefinir seu S9 para as configurações de fábrica.
Esta método pode ser aplicado entre 2 minutos e 10 minutos após a inicialização do minerador.

2 minutos após ligar o minerador, pressione o botão "Reset" por 5 segundos e solte-o. O minerador será restaurado para as configurações de fábrica em 4 minutos e reiniciará automaticamente (não é necessário desligá-lo).

![imagem](assets/en/36.webp)

## Instalando o BraiinsOS+ em um Antminer S9

<chapterId>38e8b1a8-8b1d-51ed-8b92-59d4ddb15184</chapterId>

O software original instalado pela Antminer em suas máquinas de mineração é limitado em funcionalidades. Por isso, neste guia, vamos instalar outro software chamado BraiinsOS+. É um software de terceiros desenvolvido pelo primeiro pool de mineração de Bitcoin, que possui mais funcionalidades e permite, por exemplo, modificar a potência da máquina.

Existem várias maneiras de instalar o Braiins OS+ em um ASIC. Você pode consultar este guia, bem como a [documentação oficial da Braiins](https://academy.braiins.com/en/braiins-os/about/).

Aqui, vamos ver como instalar facilmente o Braiins OS+ diretamente na memória do seu Antminer usando o software BOS toolbox, substituindo assim o sistema operacional original, por meio das etapas detalhadas abaixo.

1. Ligue o seu Antminer e conecte-o à sua caixa de internet.
2. Baixe o BOS toolbox para Windows / Linux.
3. Descompacte o arquivo baixado e abra o arquivo bos-toolbox.bat, escolha o idioma e, após alguns instantes, você verá esta janela:

![imagem](assets/en/37.webp)

4. O BOS toolbox permitirá que você encontre facilmente o endereço IP do seu Antminer e instale o BraiinsOS+. Se você já conhece o endereço IP da sua máquina, pode pular para a etapa 8. Caso contrário, vá para a guia de varredura.

![imagem](assets/en/38.webp)

5. Normalmente, em redes domésticas, a faixa de endereços IP está entre 192.168.1.1 e 192.168.1.255, portanto, insira "192.168.1.0/24" no campo de faixa de IP. Se a sua rede for diferente, altere esses endereços conforme necessário. Em seguida, clique em "Start".

6. Atenção: se o Antminer tiver uma senha, a detecção não funcionará. Se for o caso, a maneira mais simples é fazer uma reinicialização.

7. Você deve ver todos os Antminers em sua rede, aqui o endereço IP é 192.168.1.37.

![imagem](assets/en/39.webp)

8. Clique em "Back" e, em seguida, na guia "Install", insira o endereço IP encontrado anteriormente e clique em "Start".

> Se a instalação não funcionar, pode ser necessário fazer uma reinicialização e tentar novamente (consulte a seção anterior).

![image](assets/en/40.webp)

9. Após alguns instantes, o seu Antminer irá reiniciar e você poderá acessar a interface do Braiins OS+ no endereço IP em questão, aqui 192.168.1.37, digitando-o diretamente na barra de endereço do seu navegador, nome de usuário padrão "root" e sem senha padrão.

## Configurando o BraiinsOS+

<chapterId>36e432f2-85bc-52d0-a62a-009fc4c69338</chapterId>

Você precisará se conectar ao seu ASIC usando o endereço IP local do seu dispositivo na sua rede através de um navegador.

Você pode encontrar o endereço IP da sua máquina usando a ferramenta BOS toolbox ou diretamente na página web do seu roteador.

As credenciais padrão são as mesmas do sistema operacional original.

- nome de usuário: root
- senha: (nenhuma)

Você será então recebido pelo painel de controle do Brains OS+.

### Painel de Controle

![image](assets/en/41.webp)

Nesta primeira página, você poderá observar o desempenho da sua máquina em tempo real.

- Três gráficos em tempo real que mostram a temperatura, a taxa de hash e o status geral da sua máquina.
- À direita, a taxa de hash real, a temperatura média dos chips, a eficiência estimada em W/THs e o consumo de energia.
- Abaixo, a velocidade de rotação dos ventiladores em porcentagem da velocidade máxima e o número de rotações por minuto.

![image](assets/en/42.webp)

- Mais abaixo, você encontrará uma visualização detalhada de cada hashboard. A temperatura média da placa e dos chips que a compõem, a tensão e a frequência.
- Detalhes sobre os pools de mineração ativos em Pools.
- O status do autotuning em Tuner Status.
- À direita, detalhes sobre os dados transmitidos para o pool.

### Configuração

![image](assets/en/43.webp)

### Sistema

![image](assets/en/44.webp)

### Ações rápidas

![image](assets/en/45.webp)

# Attakai - Modificação dos ventiladores

<partId>98266a8f-3745-58a0-9f6b-26a9734e1427</partId>

## Substituindo o ventilador da fonte de alimentação

<chapterId>0c6befa7-f3ef-5bcf-ae8d-0ad5e5d41d70</chapterId>

> ATENÇÃO: É essencial ter instalado previamente o Braiins OS+ no seu minerador, ou qualquer outro software capaz de reduzir o desempenho da sua máquina. Essa medida é crucial, pois, com o objetivo de reduzir o ruído, iremos instalar ventiladores menos potentes, que poderão dissipar menos calor.

![image](assets/en/46.webp)

### Materiais necessários

- 1 ventilador Noctua NF-A6x25 PWM
- Fio elétrico de 2,5mm2

> ATENÇÃO: Antes de começar, certifique-se de desconectar o seu minerador para evitar qualquer risco de choque elétrico.

![image](assets/en/47.webp)

Primeiramente, remova os 6 parafusos nas laterais do gabinete que o mantêm fechado. Depois de remover os parafusos, abra cuidadosamente o gabinete para remover a proteção plástica que cobre os componentes.

![image](assets/en/48.webp)
![image](assets/en/49.webp)

Em seguida, é hora de remover o ventilador original, tendo cuidado para não danificar os outros componentes. Para fazer isso, remova os parafusos que o seguram no lugar e delicadamente descole a cola branca que envolve o conector. É importante proceder com cuidado para evitar danificar os fios ou conectores.

![image](assets/en/50.webp)

Depois de remover o ventilador original, você notará que os conectores do novo ventilador Noctua não correspondem aos do ventilador original. Na verdade, o novo ventilador tem 3 fios, incluindo um fio amarelo que controla a velocidade. No entanto, esse fio não será usado neste caso específico. Para conectar o novo ventilador, é recomendável usar um adaptador especial. No entanto, é importante observar que esse adaptador pode ser difícil de encontrar às vezes.

![image](assets/en/51.webp)

Se você não tiver esse adaptador, ainda poderá conectar o novo ventilador usando um conector de fio elétrico. Para fazer isso, você precisará cortar os cabos do ventilador antigo e do novo ventilador.

![image](assets/en/52.webp)
![image](assets/en/53.webp)

No novo ventilador, use um estilete e corte cuidadosamente as bordas da capa principal a 1cm sem cortar as capas dos cabos abaixo.

![image](assets/en/54.webp)

Em seguida, puxando a capa principal para baixo, corte as capas dos cabos vermelho e preto da mesma maneira que antes. E corte o cabo amarelo rente.

![image](assets/en/55.webp)

No ventilador antigo, é mais delicado cortar a capa principal sem danificar as capas dos cabos vermelho e preto. Para isso, usamos uma agulha que deslizamos entre a capa principal e os fios vermelho e preto.

![image](assets/en/56.webp)
![image](assets/en/57.webp)

Depois de liberar os fios vermelho e preto, corte as capas cuidadosamente para não danificar os fios elétricos.

![image](assets/en/58.webp)

Em seguida, conecte os cabos com um conector, o fio preto com o preto e o fio vermelho com o vermelho. Você também pode adicionar fita isolante.

![image](assets/en/59.webp)
![image](assets/en/60.webp)

Uma vez que a conexão tenha sido feita, é hora de instalar o novo ventilador Noctua com a grade e os parafusos antigos, os novos parafusos que estão na caixa serão reutilizados mais tarde. Certifique-se de colocá-lo na orientação correta. Você notará uma seta em um dos lados do ventilador, que indica a direção do fluxo de ar. É importante colocar o ventilador de forma que essa seta aponte para dentro do gabinete. Em seguida, reconecte o ventilador.

![image](assets/en/61.webp)
![image](assets/en/62.webp)

> Opcional: Se você tiver conhecimentos em eletricidade, pode adicionar diretamente à saída de alimentação de 12V um conector jack fêmea de 5,5 mm que permitirá alimentar diretamente a ponte Wi-Fi Vonet. No entanto, se você não tiver certeza de suas habilidades em eletricidade, é melhor usar o conector USB com um carregador de smartphone para evitar qualquer risco de curto-circuito ou dano elétrico.

![image](assets/en/63.webp)

Depois de fazer as conexões, coloque o plástico da tampa sobre o plástico do gabinete e não dentro dele.

![image](assets/en/64.webp)

Por fim, recoloque a tampa do gabinete no lugar e parafuse os 6 parafusos nas laterais para fixar tudo no lugar. E pronto, sua fonte de alimentação agora está equipada com um novo ventilador.

## Substituindo os Ventiladores Principais

<chapterId>a29f60f1-3fa3-57fc-a630-9c97cec30e56</chapterId>

> ATENÇÃO: É essencial ter instalado previamente o Braiins OS+ em seu minerador, ou qualquer outro software capaz de reduzir o desempenho de sua máquina. Essa medida é crucial, pois, com o objetivo de reduzir o ruído, vamos instalar ventiladores menos potentes, que poderão dissipar menos calor.

![image](assets/en/46.webp)

### Materiais necessários

- 2 adaptadores 3D de 140mm para 120mm
- 2 ventiladores Noctua NF-A14 iPPC-2000 PWM
- 2 grades de ventilador de 140mm

> ATENÇÃO: Antes de começar, certifique-se de desconectar o seu minerador para evitar qualquer risco de choque elétrico.

1. Primeiro, desconecte os ventiladores e desparafuse-os.

![image](assets/en/65.webp)

2. Os conectores dos novos ventiladores Noctua não correspondem aos originais, mas não se preocupe! Pegue seu estilete e corte cuidadosamente as pequenas abas de plástico para que os conectores se encaixem perfeitamente no seu minerador.

![image](assets/en/66.webp)
![image](assets/en/67.webp) 3. É hora de instalar as peças 3D!
Fixe-as em ambos os lados do minerador usando os parafusos que você removeu dos ventiladores. Aperte até que a cabeça do parafuso esteja embutida na peça 3D e que ela esteja bem fixada no lugar. Cuidado para não apertar demais, você pode deformar a peça e um dos parafusos pode tocar em um capacitor!

![imagem](assets/en/68.webp)

4. Agora vamos para os ventiladores.
   Fixe-os nas peças 3D usando os parafusos fornecidos pela caixa. Preste atenção na direção do fluxo de ar, as setas nos lados dos ventiladores indicarão a direção a seguir. Vá do lado da porta Ethernet para o outro lado. Veja a foto abaixo.

![imagem](assets/en/69.webp)
![imagem](assets/en/70.webp)
![imagem](assets/en/71.webp)

5. Última etapa: conecte os ventiladores e fixe as grades por cima com os parafusos que não foram usados na caixa do ventilador de alimentação. Você só tem 4, mas 2 por grade em ângulos opostos serão suficientes. Se necessário, você também pode procurar por outros parafusos semelhantes em uma loja de ferragens.

![imagem](assets/en/72.webp)
![imagem](assets/en/73.webp)

Enquanto espera para poder oferecer uma caixa mais elegante para o seu novo aquecedor, você pode prender o gabinete e a fonte de alimentação com abraçadeiras de eletricista.

![imagem](assets/en/74.webp)

E para o toque final, conecte a ponte Vonet à porta Ethernet com sua fonte de alimentação.

![imagem](assets/en/75.webp)

E pronto, parabéns! Você acabou de substituir toda a parte mecânica do seu minerador. Agora você deve ouvir muito menos barulho.

# Attakai - Configuração

<partId>9c3918a8-d9a3-5a1f-bb9a-70314f7ac175</partId>

## Juntando-se a um pool de mineração

<chapterId>b57a6105-0a53-5fe9-bad1-d6d9daf97c0d</chapterId>

Pode-se imaginar um pool de mineração como uma cooperativa agrícola. Os agricultores juntam sua produção para reduzir a variação da oferta e demanda e, assim, obter receitas mais estáveis para sua exploração. Um pool de mineração funciona da mesma forma e a matéria-prima compartilhada são os hashes. De fato, a descoberta de um único hash válido permite a criação de um bloco e, assim, ganhar a coinbase ou a recompensa atualmente de 6,25 BTC, além das taxas das transações incluídas no bloco. Se você minerar sozinho, só será recompensado quando encontrar um bloco.

Competindo contra todos os outros mineradores do planeta, você teria muito poucas chances de ganhar essa grande loteria e ainda teria que pagar as taxas associadas ao uso do seu minerador sem nenhuma garantia de sucesso. Os pools de mineração resolvem esse problema ao compartilhar o poder de computação de vários (milhares) de mineradores e compartilhar a recompensa deles com base na porcentagem de participação no hashrate do pool quando um bloco é encontrado. Para visualizar suas chances de minerar um bloco sozinho, você pode usar esta ferramenta. Ao inserir as informações de um Antminer S9, vemos que as chances de encontrar um hash que permita a criação de um bloco são de 1/24.777.849 a cada bloco ou de 1/172.068 por dia. Em média (com hashrate e dificuldade constantes), levaria 471 anos para encontrar um bloco.

No entanto, como no Bitcoin tudo é uma questão de probabilidade, às vezes os "mineradores solitários" são recompensados por esse risco: Minerador de Bitcoin Solitário Resolve Bloco com Taxa de Hash de Apenas 10 TH/s, Vencendo Probabilidades Extremamente Improváveis - Decrypt

Se você gosta de jogar, pode tentar, mas nosso guia não seguirá nessa direção. Em vez disso, vamos nos concentrar no pool de mineração que melhor atende às nossas necessidades para criar um sistema de aquecimento.

As considerações a serem feitas ao escolher um pool de mineração são o funcionamento das recompensas do pool, que podem ser diferentes, bem como o valor mínimo antes de poder retirar as recompensas para um endereço. Por exemplo, a Braiins, que oferece o software que estamos discutindo aqui, também oferece um pool. Este pool tem um sistema de recompensa chamado "Score" que incentiva os mineradores a minerar por longos períodos. A participação inclui um fator de tempo de atividade que é expresso com uma "taxa de hash de pontuação". No nosso caso, em que queremos um sistema de aquecimento que possa ser ligado apenas por alguns minutos, esse não é o sistema de recompensa ideal. Preferimos um sistema de recompensa que nos dê uma recompensa igual para cada participação. Além disso, o valor mínimo de retirada para o Braiins Pool é de 100.000 sats e On-Chain. Portanto, perdemos alguns sats em taxas de transação e parte da nossa recompensa pode ser bloqueada se não minerarmos o suficiente durante o inverno.

O modelo de recompensa que nos interessa é o PPS, que significa "pagamento por ação". Isso significa que o minerador receberá uma recompensa por cada ação válida. Também existe uma variante desse sistema, o FPPS (Full Pay Per Share), que divide não apenas a recompensa da coinbase, mas também as taxas de transação incluídas no bloco. Os pools de mineração que recomendamos para conectar sua mineração/aquecimento são Linecoin Pool (FPPS) e Nicehash (PPS).

- Nicehash: A vantagem do Nicehash é que a retirada pode ser feita usando o Lightning com taxas mínimas. Além disso, o valor mínimo de retirada é de 2000 sats. A desvantagem é que o Nicehash usa sua taxa de hash para a blockchain mais lucrativa, sem realmente dar controle ao usuário, e portanto, não necessariamente participa da taxa de hash do Bitcoin.

- Lincoin: A vantagem do Linecoin é o número de recursos oferecidos, como um painel detalhado, a possibilidade de fazer retiradas com um Paynym (BIP 47) para uma melhor proteção de privacidade, e a integração de um bot do Telegram e automações diretamente configuráveis no aplicativo móvel. Este pool minera apenas blocos de Bitcoin, mas o valor mínimo para retirada ainda é alto, 100.000 sats. Vamos examinar mais detalhadamente a interface de um desses pools em um próximo artigo.

Para configurar um pool no Braiins 0S+, você precisará criar uma conta em um dos pools de sua escolha. Aqui vamos usar o exemplo do Lincoin:

![image](assets/en/76.webp)

Depois de criar sua conta, clique em Conectar ao Pool

Em seguida, copie o endereço Stratum e seu nome de usuário:

![image](assets/en/77.webp)

Agora você pode voltar para a interface do Braiins OS+ para inserir essas credenciais. Para a senha, você pode deixar o campo em branco.

![image](assets/en/78.webp)

## Otimizando o desempenho do Antminer S9

<chapterId>25380972-31c7-540d-80d8-17a06b171ca0</chapterId>

O overclocking e o auto-tuning consistem em ajustar as frequências nos cartões de hash para melhorar o desempenho do ASIC. A diferença entre os dois está na complexidade dessas configurações de frequência.

O overclocking é um ajuste simples que envolve aumentar a frequência nos cartões de hash para aumentar a taxa de hash da máquina. O underclocking, por outro lado, envolve diminuir a frequência de clock de um circuito integrado abaixo de sua frequência nominal. Ao reduzir a frequência de clock de um ASIC por meio do underclocking, também reduzimos o calor gerado pelo hardware. Isso permite diminuir a velocidade dos ventiladores necessários para resfriar o ASIC, pois eles não precisam trabalhar tão duro para manter uma temperatura adequada. Ao reduzir a velocidade dos ventiladores, também reduzimos o ruído gerado pelo ASIC. Isso pode ser especialmente útil para usuários que usam ASICs em casa e desejam minimizar as perturbações sonoras causadas pelo equipamento de mineração.

O Braiins OS+ suporta overclocking, underclocking de ASICs e auto-tuning. Ele permite que os usuários ajustem a frequência de clock de seu hardware de forma flexível para maximizar o desempenho ou economizar energia, de acordo com suas preferências.

### Otimizando o desempenho do Antminer S9 com auto-tuning

Antes de 2018, os mineradores tinham duas maneiras de obter vantagem em suas atividades: encontrar eletricidade a um custo razoável e comprar hardware mais eficiente. No entanto, em 2018, uma nova descoberta foi feita no campo de software e firmware de mineração, chamada AsicBoost. Essa técnica permite que os mineradores reduzam seus custos em cerca de 13% ao modificar o firmware executado em seus dispositivos.
Hoje em dia, há um novo avanço na indústria de software e firmware de mineração chamado de autotuning, que oferece uma vantagem ainda maior do que o AsicBoost. Os ASICs são compostos por muitos pequenos chips de computador que realizam o hashing. Esses chips são feitos de silício, o mesmo elemento amplamente utilizado em semicondutores e outros componentes microeletrônicos. A compreensão chave aqui é que nem todos os chips de silício são idênticos, cada um pode variar ligeiramente em suas propriedades elétricas. Os fabricantes de hardware sabem disso e publicam as especificações de desempenho de suas máquinas de mineração com base no limite inferior de suas tolerâncias. Em outras palavras, os fabricantes conhecem a frequência que funciona melhor para os chips médios e usam essa frequência de forma uniforme para todos os chips da máquina.

Isso impõe um limite superior à taxa de hashing que uma máquina pode ter. O autotuning é um processo no qual algoritmos avaliam as frequências ótimas para o hashing chip por chip, em vez de tratar toda a máquina como uma única unidade. Isso significa que um chip de melhor qualidade, que pode realizar mais hashings por segundo, obterá uma frequência mais alta, e um chip de qualidade inferior, que pode realizar relativamente menos, obterá uma frequência mais baixa. O ajuste automático por chip é essencialmente uma maneira de otimizar o desempenho de um ASIC por meio do software e firmware que são executados nele.

O resultado final é uma taxa de hashing mais alta por watt de eletricidade, o que significa margens de lucro maiores para os mineradores. A razão pela qual as máquinas não são distribuídas com esse tipo de software é que a variação por máquina não é desejável, pois os clientes querem saber exatamente o que estão obtendo, e, portanto, é uma má ideia para os fabricantes venderem um produto que não tenha desempenho consistente e previsível de uma máquina para outra. Além disso, o ajuste automático por chip requer recursos de desenvolvimento consideráveis, pois é complexo de implementar. Os fabricantes já gastam muitos recursos para desenvolver seus próprios firmwares. Existem soluções de software que permitem implementar o autotuning, como o Braiins OS+. Além de melhorar o desempenho do ASIC em até 20%.

# Conclusão

<partId>fa42ec0b-b1fd-47f6-8268-6eab684c1d2b</partId>

## Avalie este curso

<chapterId>6af13742-df68-5cf4-b7aa-93dc0c2eaae9</chapterId>
<isCourseReview>true</isCourseReview>

## Exame final

<chapterId>f51a7c88-3b7e-48df-b45f-22bb10fe619f</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusão

<chapterId>2941f29a-d6ce-4a3c-b61b-6e399f5395b1</chapterId>
Parabéns por concluir este curso!

Estamos muito satisfeitos que você tenha alcançado este importante marco em sua jornada de aprendizagem.

Através de sua dedicação e comprometimento, você adquiriu conhecimentos e habilidades valiosos que servirão para seu desenvolvimento profissional.

Para continuar explorando em profundidade o universo Bitcoin, convidamos você a descobrir todos os outros cursos disponíveis na Plan ₿ Network:

#### Descubra o Bitcoin e seus fundamentos com

https://planb.network/courses/btc101

#### Descubra a Lightning Network com

https://planb.network/courses/lnp201

#### Domine os princípios da privacidade no Bitcoin

https://planb.network/courses/btc204

#### Descubra a história das origens do Bitcoin com

https://planb.network/courses/his201

#### Entenda como funciona a carteira Bitcoin com

https://planb.network/courses/cyp201
