---
name: Configuração de um nó Bitcoin e Lightning
goal: Implementar um nó Bitcoin e Lightning via Umbrel
objectives:
  - Instalar um nó Bitcoin
  - Gerenciar um nó Bitcoin
  - Utilizar uma rede Lightning
---

# Uma jornada para o lado técnico do Bitcoin

Este treinamento é mais técnico e será ainda mais benéfico se você tiver conhecimentos básicos sobre Bitcoin, especialmente a compreensão do funcionamento das carteiras Bitcoin e o princípio de transação, mineração e blockchain. Não é necessário saber programar, sua curiosidade e vontade de aprender são as únicas habilidades necessárias. Lembre-se, todo especialista já foi um iniciante. Então, respire fundo e mergulhe no universo emocionante do Bitcoin. Você está prestes a começar uma jornada emocionante e enriquecedora. Boa sorte!

+++

# Tornando-se um Bitcoiner soberano

![Lançamento do treinamento](https://youtu.be/NF3SHhE1PFw?list=PLinTFKehfR4zoKvBcncHPr-ZTh1enuEhr)

Para participar plenamente da filosofia do Bitcoin e incorporar o lema "Não confie, verifique", nosso objetivo é nos tornarmos usuários soberanos de nós Bitcoin. Nesse processo, vamos usar a interface do Umbrel para configurar nosso próprio nó. As ferramentas necessárias para essa tarefa incluem um Raspberry Pi, um disco rígido externo, um cartão SD, um ventilador e uma caixa, para um investimento total estimado em cerca de 200€.

Ao adotar o Umbrel como nossa base operacional, poderemos integrar a Lightning Network, explorar a mempool e descobrir soluções de multisig. Ao final desta jornada, não apenas teremos nos afirmado como Bitcoiners soberanos, mas também teremos a satisfação de ter contribuído ativamente para a rede Bitcoin.

# O que é um nó Bitcoin?

![O que é um nó?](https://youtu.be/19YgL9vkHh4)

Um nó Bitcoin é simplesmente um dispositivo que executa o software Bitcoin, a pedra angular da existência e comunicação da rede. Esses nós constituem a base da descentralização do Bitcoin, assumindo diferentes formas e responsabilidades diversas. Entre elas, estão a recepção e transmissão de transações, a exibição de transações de saída e o estabelecimento de conexões com outros nós.
Três papéis principais são atribuídos a esses nós: estabelecer o consenso do Bitcoin, validar transações e interagir com a rede. Graças a essa descentralização, o Bitcoin se beneficia de uma maior resiliência, com privacidade reforçada pelo fato de não depender de um servidor terceiro. De acordo com o [Bitnodes](https://bitnodes.io/nodes/all/), cerca de 43.000 nós em todo o mundo formam a rede Bitcoin.

Agora vamos explorar as funções específicas desses nós na rede Bitcoin. Um nó não é apenas um software; é também uma porta de entrada para o consenso da rede Bitcoin e acesso ao histórico do blockchain. Por exemplo, os comerciantes usam seu próprio nó para validar transações de entrada e saída.

A vantagem de gerenciar seu próprio nó reside na melhoria da privacidade e na realização da soberania financeira. De fato, executar seu próprio nó reforça sua contribuição para a rede e o torna seu próprio banco. Isso permite que você verifique transações em tempo real, oferecendo uma melhor tomada de decisão sobre suas finanças.

Em conclusão, executar seu próprio nó na rede Bitcoin oferece muitas vantagens. Não só contribui para a descentralização da rede, fortalecendo assim a resiliência do sistema, mas também garante maior privacidade e autonomia financeira. Ao realizar este processo, você pode autenticar transações em tempo real, tomar decisões financeiras informadas e evitar a dependência de um servidor terceiro, garantindo assim sua privacidade. Além disso, executar seu próprio nó é uma maneira concreta de contribuir para o ecossistema Bitcoin e verdadeiramente incorporar o papel de seu próprio banco.

# Tutorial de nó Bitcoin via Umbrel

![Tutorial umbrel](https://youtu.be/mr4iTzdTczI)

Neste capítulo, vamos implantar nosso próprio nó Bitcoin, abrir canais lightning e experimentar uma carteira multi-assinatura. Isso tem um custo material significativo para algumas pessoas. Saiba que todo o treinamento pode ser seguido SEM o material. Você não ficará perdido se não tiver seu próprio nó.
Se você quiser começar, aqui estão os produtos (link de afiliado):

- Cartão SD de 16 GB - https://amzn.to/3Qi2Opm
- Raspberry Pi 4 - https://amzn.to/3qoSUYl
- SSD de 1 TB - https://amzn.to/3jSvjLC​
- Caixa externa para disco rígido - https://amzn.to/3x5R02S
- Alimentação RASPBERRY - https://amzn.to/3D36zvM
- Raspberry Pi FLIRC Case - https://amzn.to/3TNllgi
  Si você acessou os links de afiliados, obrigado pelo seu apoio! Você permite que este projeto sobreviva e ofereça cada vez mais formações e conteúdos educacionais.

O que é necessário para executar seu nó Bitcoin?

- A blockchain tem cerca de 500GB, portanto, é necessário espaço
- A conexão com a internet deve ser constante, com cerca de 5GB de largura de banda por mês
- É necessário RAM para executar o BTC Core
- É necessário mais RAM se você executar o Umbrel e um nó LN (mínimo de 4 GB)

Você pode executar seu nó Bitcoin diretamente em seu computador ou usar um sistema como o mostrado no vídeo com um Raspberry Pi.

Existem outras [soluções](https://thebitcoinmanual.com/behind-btc/nodes/buy-node/) prontas disponíveis!

Siga estes passos para criar um nó completo com um Raspberry Pi e Umbrel. Antes de começar, observe que você precisará de cerca de 200 euros para comprar o hardware necessário, embora o software seja gratuito.

1. **Preparação das ferramentas**: Acesse [Umbrel](https://umbrel.com/), uma solução de código aberto conhecida por sua excelente interface do usuário e bom serviço, para baixar o software necessário. Além disso, você precisará do Benella Itcher para gravar o cartão SD.
2. **Montagem do Raspberry Pi**: Monte seu Raspberry Pi. Certifique-se de instalar o ventilador e os pequenos componentes de resfriamento incluídos no kit.
3. **Gravação do cartão SD**: Use o dispositivo fornecido no kit para gravar o cartão SD. Se você tiver dificuldades, tente reformatar o cartão ou desconectar/reconectar o dispositivo.
4. **Conexão do hardware**: Depois que o cartão SD for gravado, conecte o SSD ao Raspberry Pi por meio de uma porta 3.0. Em seguida, conecte o Raspberry Pi ao seu roteador e a uma fonte de alimentação elétrica.
5. **Configuração do Umbrel**: Após cerca de 5 minutos, você poderá acessar a interface do Umbrel em seu computador. É recomendável usar um gerenciador de senhas para criar e salvar uma senha segura para acessar seu nó Umbrel.
6. **Proteção da sua seed (frase mnemônica)**: Sua seed é a chave privada que dá acesso aos seus bitcoins. Portanto, certifique-se de mantê-la em um local seguro. Evite tirar fotos ou capturas de tela de sua seed. Também é recomendável salvar o link TOR em seu gerenciador de senhas para acesso fácil posteriormente.
7. **Explorando o painel do Umbrel**: O Umbrel possui um painel claro e uma loja de aplicativos inovadora para baixar outros aplicativos. O tutorial do Umbrel está disponível para todos, basta comprar o hardware e seguir os passos.
8. **Tomar consciência da importância dos nós**: Os nós são essenciais para transformar o sistema bancário e substituir os bancos centrais. Com o seu próprio nó, você participa da verificação das transações Bitcoin e do cumprimento das regras do protocolo. Ao executar o seu próprio nó, você não precisa mais confiar em terceiros e pode verificar as transações por si mesmo. Os nós são um pilar essencial da sua soberania financeira.

Seguindo esses passos, você pode contribuir para a descentralização da rede Bitcoin, aumentar sua privacidade e autonomia financeira e participar ativamente da evolução do sistema bancário tradicional. Então, não hesite em se lançar e se tornar um verdadeiro Bitcoiner soberano.

# Visão geral do Umbrel

![visão geral do umbrel](https://youtu.be/cwEa61BgemM)

Estamos prestes a examinar de forma abrangente esta interface que facilita a gestão da sua carteira Bitcoin e Lightning Network.

Para começar, vamos fazer login na conta usando uma senha segura e um gerenciador de senhas dedicado. Em seguida, faremos uma exploração aprofundada da interface, familiarizando-nos com as características distintivas da carteira Bitcoin e da Lightning Network.

O nó se comunicará com outros nós na rede Bitcoin peer-to-peer de forma aleatória e sob pseudônimo. Essa característica essencial permite baixar a blockchain completa (também chamada de timechain) sem depender de uma entidade central. No entanto, é preciso levar em conta que o download inicial da timechain pode levar vários dias, uma vez que representa um volume de mais de 500 GB para receber.

Em seguida, realizaremos transações dentro da carteira Bitcoin, incluindo uma transferência de teste para uma carteira multisig. Em seguida, abriremos canais da Lightning Network e usaremos conexões ativas na carteira da Lightning Network. A abertura de canais requer alguma exploração visual.

Depois de realizar essas operações, o Bitcoin Core se torna operacional. Você pode então conectar algumas de suas carteiras ao seu nó para verificar o estado de suas contas.

É possível vincular suas carteiras Bitcoin, como [Green Wallet](https://blockstream.com/green/), [Samouraï](https://samouraiwallet.com/), [Spectre](https://specter.solutions/), [Sparrow](https://sparrowwallet.com/) ao seu nó Bitcoin por meio de uma interface dedicada. Ao conectar sua carteira ao seu próprio nó, você pode confirmar o recebimento dos fundos sem precisar confiar em um servidor externo, o que é especialmente recomendado para comerciantes.
Umbrel propõe também uma App Store que reúne Explorers, vários outros serviços relacionados ao Bitcoin, Lightning ou hospedagem de seus próprios dados. Novos aplicativos são adicionados regularmente à sua [appstore](https://apps.umbrel.com/).

Para obter mais informações e suporte, não hesite em consultar seu site, o chat Telegram, o Discord, o Github e o Reddit. Em resumo, graças à Umbrel, você tem a possibilidade de retomar o controle de sua soberania financeira por meio do Bitcoin e se tornar seu próprio banco, contribuindo para a rede. Encorajamos você a aprofundar e aprender esta tecnologia para integrá-la em sua loja, e-commerce, vida pessoal ou simplesmente por curiosidade.

# Análise da MemPool

![mempool](https://youtu.be/0xS859IoMh8)

A Mempool, intrinsecamente, funciona como um espaço de trânsito para as transações Bitcoin que aguardam validação na blockchain. Para examinar a Mempool de forma eficaz, a Umbrel é a ferramenta de escolha. O aplicativo [Mempool.space](https://mempool.space/), acessível pela interface da Umbrel, fornece uma representação clara das transações pendentes, dos custos associados e de várias outras funcionalidades relevantes.

A blockchain do Bitcoin é essencialmente um banco de dados que incorpora blocos de transações em intervalos regulares de cerca de 10 minutos. Após cada série de 2016 blocos, a dificuldade de mineração é ajustada para manter esse intervalo médio. Se os mineradores decidirem retirar sua energia da rede Bitcoin, o tempo médio necessário para encontrar novos blocos aumenta, levando a uma queda na dificuldade de mineração e permitindo que outros mineradores se tornem competitivos novamente.

Além da dificuldade de mineração, o custo atual de uma transação Bitcoin é visível no painel, bem como a blockchain com sua cadeia de blocos. As taxas para uma transação Bitcoin atualmente são de 40 sats/vbytes. As taxas de transação no Bitcoin são baseadas na complexidade da transação, que é considerada proporcional ao peso virtual (os vbytes) da transação. Os vbytes, ou bytes virtuais, são uma unidade de medida usada no Bitcoin para avaliar o tamanho de uma transação levando em consideração a tecnologia SegWit. Assim, o uso de vbytes permite uma medida mais precisa da eficiência do espaço em um bloco.

Cada usuário é livre para determinar as taxas associadas à sua transação, que tendem a refletir a urgência da validação da transação: quanto mais o usuário deseja que sua transação seja validada rapidamente, mais as taxas aumentam. Assim, como o volume de um bloco é limitado a 4 MB (embora o tamanho médio dos blocos seja de cerca de 1,5 MB), quando a demanda aumenta, as taxas para aumentar a probabilidade de que nossa transação seja incluída no próximo bloco podem aumentar significativamente.
O Bitcoin possui várias camadas: o Mainnet (a cadeia principal), o Testnet e o Signet (cadeias dedicadas à experimentação e validação de novas funcionalidades), a Lightning Network (uma rede de pagamento) e a Liquid (uma sidechain onde os blocos são validados a cada minuto). Cada uma dessas camadas tem sua própria utilidade e casos de uso específicos.

Os blocos que contêm transações são construídos pelos pools de mineração e seu nível de preenchimento varia de acordo com a demanda e o tempo decorrido desde a mineração do último bloco. Camadas superiores, como a Lightning Network, permitem transações mais rápidas e menos custosas do que na blockchain principal, mas ainda dependem do Bitcoin para seu modelo de segurança.

Em conclusão, os exploradores de blocos permitem acompanhar as transações em tempo real ou rastreá-las no passado. Essas transações podem apresentar níveis variados de complexidade. O Mempool oferece uma solução eficaz para visualizar a blockchain, acompanhar as transações e analisar as taxas e a congestão da rede.

# Explorador de Blocos e Análise de Estatísticas

![explorador de blocos e análise de estatísticas](https://youtu.be/Qe9VaUhUS0E)

Vamos embarcar em uma jornada de exploração através da blockchain do Bitcoin, usando ferramentas poderosas como os Exploradores de Blocos e o aplicativo BTC Explorer no nó Umbrel. Os Exploradores de Blocos nos dão a capacidade de analisar detalhadamente a blockchain do Bitcoin. Com o BTC Explorer, um aplicativo no Umbrel, você pode verificar todas as informações relacionadas à blockchain do Bitcoin que estão em seu disco rígido, permitindo que você não dependa mais da confiança de terceiros.

Estamos nos referindo a uma transação específica, a mesma examinada no curso anterior, para demonstrar as funcionalidades e a importância dessas ferramentas. Também ilustraremos os últimos blocos minerados e detalharemos as informações sobre seu conteúdo. Em seguida, faremos uma comparação aprofundada entre dois blocos distintos, analisando seu conteúdo e o tempo que levou para serem minerados.

O Explorador de Blocos nos permite visualizar os detalhes de um bloco minerado, como o hash, o resumo, as saídas, as taxas, o tempo e as transações. Quanto ao Bitcoin Explorer, ele oferece ferramentas mais sofisticadas para análise da blockchain. A primeira ferramenta, por exemplo, permite examinar em detalhes seu nó (sincronização, índice, tamanho da blockchain, BIP aceitos).

As Propostas de Melhoria do Bitcoin (BIP) são propostas de melhoria do protocolo Bitcoin. Podemos observar a ativação do Segwit e o número de conexões de rede. Além disso, as Blockstats fornecem estatísticas detalhadas sobre taxas, transações, entradas e saídas.
A análise de dados do Segwit oferece uma visão geral da evolução do Bitcoin ao longo dos anos. As estatísticas de transações, volumes, blocos, UTXO e timestamps estão disponíveis gratuitamente. A interpretação desses dados é crucial para a pesquisa financeira e para verificar a adoção do Bitcoin.

É importante assumir a soberania financeira e buscar os dados por si mesmo. A análise de blocos permite estudar os dados de um bloco específico, como o primeiro bloco minerado por Satoshi em 2009, onde ele voluntariamente destruiu seus 50 primeiros bitcoins para um lançamento honesto.

Os dados das transações Bitcoin são transparentes e consultáveis por todos, incluindo analistas e profissionais do setor. Essas informações são vitais porque fornecem valiosas indicações sobre a atividade da rede Bitcoin, a dinâmica do mercado e as tendências em curso, o que é essencial para uma tomada de decisão informada e a implementação de estratégias financeiras sólidas. Além disso, esses dados são usados para rastrear transações, garantindo a rastreabilidade e transparência da rede Bitcoin.

Uma transação Bitcoin "pesada", como uma que contém 673 inputs e 1 output, ilustra o compromisso entre o número de UTXO (Unspent Transaction Outputs) e a quantidade de Bitcoin em um endereço. Os UTXO representam os fundos não gastos de uma transação anterior, que se tornam os inputs das transações futuras. O aumento do número de UTXO em uma transação a torna mais complexa e cara. Portanto, é essencial agrupar os UTXO para minimizar as taxas de transação e otimizar o uso do espaço em um bloco da blockchain Bitcoin.

A mineração, pivô central do protocolo Bitcoin, desempenha um papel fundamental na segurança das transações. O processo é regulado por um ajuste de dificuldade a cada 2016 blocos para manter um intervalo médio de 10 minutos entre os blocos. Ao mesmo tempo, a taxa de hash, reflexo do poder de computação da rede, está em constante aumento.

Dentro da rede, os mineradores se agrupam em pools de mineração. Essas entidades não têm o poder de controlar toda a rede, pois os mineradores têm o privilégio de poder alternar entre os pools a seu critério. Tecnologias inovadoras como Stratum V2 dão mais poder aos mineradores dentro dos pools de mineração. Além disso, soluções técnicas como MimbleWimble e Dandelion se apresentam como melhorias promissoras para as transações.
Par ailleurs, a riqueza histórica da blockchain reside no fato de que ela arquiva todas as transações, desde o bloco gênesis até as transações mais recentes. Ela inclui a primeira transação Bitcoin feita por Satoshi para Hal Finney no bloco 170 e a famosa transação de 10.000 bitcoins por duas pizzas no bloco 57043, evento que deu origem à celebração anual do "Pizza Day" em 22 de maio.

Para fortalecer sua soberania financeira e evitar a dependência de terceiros para receber e enviar seus bitcoins, é crucial conectar suas carteiras ao seu próprio nó Bitcoin. As transações são primeiro validadas pelos nós da rede durante sua propagação e, em seguida, novamente quando são incorporadas a um bloco.

Para concluir, compartilhar e iniciar seu círculo social no Bitcoin é uma iniciativa louvável. Ao explorar seu próprio nó e contribuir para a rede, você pode se tornar seu próprio banco. O objetivo final é se tornar completamente autônomo.

# Conectar sua carteira ao seu nó

![conectar sua carteira ao seu nó](https://youtu.be/HOV3bVcram4)

No mundo digital de hoje, proteger suas criptomoedas e sua privacidade é primordial. É nesse contexto que vou orientá-lo na conexão de suas carteiras móveis e de desktop ao nosso nó Bitcoin. Este procedimento aumenta significativamente sua segurança e aumenta seu controle sobre seus ativos.

Existem muitas carteiras disponíveis: Bitbox App, Blue Wallet, Blockstream Green, Samouraï, Phoenix, Sparrow, Wasabi, Electrum e muitas outras. Cada um tem suas especificidades, pontos fortes e fracos. Para hoje, nosso foco será no Sparrow, uma alternativa interessante ao Ledger Live, conhecida por sua facilidade de gerenciamento e criação de carteiras.

Em termos de segurança e privacidade, um passo adicional pode ser dado: o uso de um servidor privado em vez de um servidor público. Embora mais complexa, essa abordagem garante um nível superior de controle e proteção. Você encontrará as informações necessárias para se conectar a um servidor privado no Umbrel.

Lembre-se, manter suas carteiras atualizadas é um gesto essencial. As atualizações corrigem bugs, combatem vulnerabilidades, melhoram o produto e às vezes adicionam novos recursos úteis. O Umbrel, em particular, garante a atualização automática de todos os seus aplicativos. Portanto, é sensato manter seu Umbrel atualizado.
Para concluir, conectar suas carteiras diretamente ao nosso nó Bitcoin é um passo em direção à independência financeira. Isso lhe confere um nível superior de privacidade e segurança, permitindo que você mantenha controle total sobre seus ativos digitais. A soberania financeira significa ter posse total e controle sobre seu dinheiro, sem intermediários. Ao diversificar suas carteiras e mantê-las atualizadas, você dá mais um passo em direção a essa autonomia.

# Carteiras multi-sig via Specter

![carteiras multi-sig](https://youtu.be/mV1KS-Uwjew)

Propomos que você dê um passo adiante em direção à autonomia financeira. Nosso objetivo é estabelecer uma carteira multi-sig com o aplicativo Specter, integrado ao Umbrel. Vamos conectar o aplicativo Desktop ao nosso nó, tornando este tutorial acessível a todos.

O conceito de multi-sig é simples: garantir um nível excepcional de segurança para grandes quantias. Para isso, usaremos três chaves privadas para proteger nossa nova carteira Bitcoin. Existem vários níveis de segurança: carteira móvel, carteira física, frase secreta, multi-sig 2 de 3, multi-sig 3 de 5 ou até mesmo uma combinação de todos esses elementos com open dimes. Não é necessário ser um especialista em tecnologia para seguir este tutorial, mas é necessário ter alguma familiaridade com o sistema de chaves privadas e públicas.

Prepare-se, pois o tutorial é rápido. Com os dispositivos já inicializados, deve levar cerca de 15 minutos. Para seguir, você precisará de três dispositivos inicializados, um nó para conectar o aplicativo Specter, uma chave USB e uma impressora. Usaremos o aplicativo Specter para nossa solução multi-sig. Você pode baixá-lo via Umbrel ou diretamente do site da Specter Solutions. Não se esqueça de verificar a assinatura antes de fazer o download. Você também pode fazer seu multi-sig com Sparrow ou Electrum. Não hesite em fazer suas pesquisas e se familiarizar com essas ferramentas antes de usá-las para gerenciar grandes quantias.

Agora vamos para a prática. Aqui, realizamos um 2 de 3 com uma ledger e 2 trezor (branco e preto) e o Specter Desktop, que é a interface da carteira que nos permite interagir com nossas carteiras e está conectado ao Bitcoin Core via Umbrel.
Nous criaremos primeiro uma carteira simples para interagir com a Ledger sem o Ledger Live. Isso nos permitirá gerar novos endereços e enviar Bitcoins. Em seguida, adicionaremos outros dispositivos (tesouros) para criar o multisig. Começaremos escolhendo o segundo dispositivo (o Tesouro branco) que conectaremos via USB. Depois de usar o PIN para ativá-lo, extrairemos as chaves públicas e criaremos uma segunda carteira. Em seguida, adicionaremos um terceiro dispositivo (o Trezor Noir) e o usaremos para criar uma carteira multisig. Criaremos uma carteira multisig escolhendo os três dispositivos, usando o Signet para testar e não perder fundos em caso de erro (no entanto, o processo é o mesmo para o mainnet).

Em seguida, criaremos a carteira combinando as chaves públicas. O backup de uma carteira multisig contém vários elementos. Na verdade, para recriar a carteira, precisaremos das três chaves públicas e duas chaves privadas para gastar o dinheiro. Portanto, é crucial armazenar as chaves públicas com o backup de cada chave privada em um local seguro.

Recomenda-se escrever em papel ou metal as frases mnemônicas (lista de 24 palavras) das 3 chaves privadas em vários exemplares (pelo menos 2). Além disso, é aconselhável escrever informações precisas e detalhadas que permitam recuperar seu dinheiro em caso de problema ou para um plano de herança. Essas instruções também devem ser armazenadas em um local seguro.

Assim, você terá dado mais um passo no caminho da soberania do Bitcoin. Ao dominar sua segurança e usar ferramentas como o multisig, você fortalece sua autonomia financeira e protege seus ativos de maneira ideal. Não se esqueça, a prudência e a aprendizagem contínuas são as chaves para o sucesso no mundo do Bitcoin.
Se você quiser praticar com bitcoins do Testnet, pode obtê-los através deste [faucet](https://bitcoinfaucet.uo1.net/).

# Abertura de canais Lightning

![abertura de canais](https://youtu.be/bAZJn0AH1yU)

Agora vamos abordar a parte Lightning do nó Umbrel. Usaremos o ThunderHub, um aplicativo entre vários que servem como gerenciador de nó Lightning, como o Lightning Terminal e o RideTheLightning (RTL). Esses aplicativos nos dão uma visão precisa do estado de nossos canais, servindo como interface entre nós e nossos canais da Lightning Network (LN).
Neste momento, nosso objetivo principal é abrir um novo canal. Quando você baixa o ThunderHub, uma senha padrão é fornecida, que você pode encontrar diretamente na appstore. É essencial alterá-la e manter essa nova senha em um gerenciador de senhas dedicado.

Ao considerar a abertura de um canal com outro nó Lightning na rede, surgem algumas perguntas. Por exemplo, qual quantidade de liquidez você deseja alocar em um canal? Com quais partes você deseja abrir um canal? As respostas a essas perguntas são cruciais para otimizar suas transações e evitar possíveis problemas.

Vamos falar sobre o tamanho dos canais. Não seria sensato começar abrindo canais com um valor baixo, como 20k, 50k ou 100k sats. Isso seria insuficiente e as taxas de abertura e fechamento do canal não seriam cobertas. Um canal de baixo valor seria mais prejudicial do que útil para você e para o resto da rede. Por exemplo, se você tiver um canal de 20k aberto com meu nó, isso mal cobriria as taxas de abertura e fechamento (+ reserva). Você teria apenas migalhas para gastar.

Por isso, é recomendado abrir canais de pelo menos 500k-1M sats. Isso ofereceria uma melhor rotação, benéfica para você e para todos os outros que roteariam transações através do seu nó. É importante notar que a ideia de "quanto maior, melhor" não se aplica aqui. Seria melhor ter 5 a 6 canais de saída, cada um contendo entre 500k e 1M sats, e, de acordo com suas necessidades, 4 a 5 canais de entrada com capacidade semelhante.

Agora que você está familiarizado com o tamanho dos canais, vamos falar sobre sua gestão. No que diz respeito à liquidez de saída (do seu lado), seu nó LN permite que você faça pagamentos LN, compre coisas, envie dinheiro para amigos, pague serviços, etc. Tente abrir canais LN com os comerciantes com os quais você pretende negociar. No que diz respeito à liquidez de entrada (do lado de seus pares), encontre pares dispostos a abrir canais para o seu nó. Essa liquidez de entrada é necessária para receber pagamentos no LN.
La questão de com quem abrir canais é primordial. Primeiro, com os comerciantes com quem você pretende realizar transações, você pode aproveitar uma rota direta e evitar taxas. Em segundo lugar, pense em amigos e usuários experientes do LN que você conhece e que podem criar um anel de nós (ring of fire) com uma certa quantidade de sats para esses canais. Isso é perfeito para equilibrar a liquidez enquanto reduz as taxas entre os nós do anel. Em terceiro lugar, seu anel de nós pode ter conexões ou canais "externos" com outros bons nós, o que facilita e acelera o roteamento para qualquer destinatário.

Para estabelecer essas conexões, você precisará obter os endereços públicos das outras partes. Você pode fazer isso pedindo diretamente a eles ou por meio de sites como [1ML](https://1ml.com/) ou [Amboss](https://amboss.space/). A abertura de um canal envolve taxas de transação em cadeia, portanto aproveite os momentos em que a Mempool está vazia para abrir canais. Uma vez que um canal é aberto, a liquidez é bloqueada de um lado do canal. Para movê-lo para o outro lado, é necessário realizar transações para pagamentos ou realizar o que é chamado de "submarine swap" (veremos isso na próxima parte). É importante notar que na Lightning Network, há taxas de roteamento. Se um canal se esvazia muito rapidamente, devido ao roteamento, você pode aumentar essas taxas.

Antes de concluir, é importante notar que há outra decisão crucial a ser tomada ao abrir canais Lightning: escolher entre um canal público ou um canal privado. Cada um tem suas vantagens e desvantagens, dependendo de suas necessidades e preferências.

Um canal público é anunciado em toda a rede Lightning e pode ser usado para roteamento de pagamentos. É uma excelente opção se você deseja participar ativamente da rede e ajudar a facilitar as transações de outros usuários. Isso também pode gerar receita (muito baixa) por meio das taxas de roteamento que você pode receber. No entanto, tenha em mente que, uma vez que um canal público é visível para todos, ele não é adequado se você estiver procurando manter um alto nível de privacidade.

Por outro lado, um canal privado não é anunciado na rede e não será usado para roteamento de pagamentos. É uma boa opção se você valoriza a privacidade e planeja usar o canal principalmente para suas próprias transações. É importante notar que, mesmo que um canal privado não ofereça as mesmas oportunidades de receita de taxas de roteamento que um canal público, ele pode oferecer uma tranquilidade de espírito aumentada em termos de segurança e privacidade.
En última instancia, a escolha entre um canal público e um canal privado depende da sua própria situação e prioridades. Avalie cuidadosamente suas necessidades e objetivos antes de tomar uma decisão.

Em conclusão, a abertura de canais na Lightning Network é um passo técnico essencial para otimizar suas transações. A escolha do tamanho dos seus canais, a escolha entre um canal público ou privado e a seleção cuidadosa das partes com as quais abrir canais são fatores determinantes para uma roteamento eficiente e econômico. Na próxima parte, abordaremos a gestão eficaz desses canais. Então, vá para a próxima seção para mais detalhes sobre essa importante faceta da Lightning Network.

# Gestão de canais LN

![gestão de canais LN](https://youtu.be/CgBnGQLar4o)

Agora que cobrimos a abertura de canais na Lightning Network, vamos nos concentrar em sua gestão. Uma gestão eficaz dos canais pode fazer uma grande diferença na otimização da sua experiência na Lightning Network.

O primeiro elemento essencial da gestão de canais é o equilíbrio. Os canais da Lightning Network têm o que é chamado de "liquidez", que é distribuída entre as duas partes do canal. O equilíbrio dessa liquidez é crucial para garantir que as transações possam ser roteadas eficientemente pelo seu nó. Muita liquidez de um lado ou de outro pode tornar o canal menos útil para o roteamento. Felizmente, existem várias estratégias para equilibrar os canais, incluindo o uso de serviços como o Lightning Loop da Lightning Labs, que permite mover a liquidez para dentro e para fora da rede Bitcoin.

O segundo elemento a ser considerado é a monitorização dos seus canais. É importante verificar regularmente o estado dos seus canais e monitorizar o desempenho do seu nó. Ferramentas como ThunderHub e RTL oferecem ótimas funcionalidades para ajudar a monitorizar o seu nó e gerir os seus canais. Eles fornecem informações sobre o estado dos seus canais, incluindo sua liquidez, taxas e capacidade. Além disso, eles oferecem funcionalidades para fechar canais, abrir novos canais e equilibrar a liquidez entre os canais.

Em terceiro lugar, é preciso considerar o fechamento dos canais. Às vezes, você pode acabar com um canal que não é mais útil ou não é mais eficiente. Nesse caso, você vai querer fechar o canal. No entanto, é importante notar que fechar um canal resulta em uma transação na blockchain do Bitcoin, o que pode resultar em taxas. Portanto, é sensato fechar os canais durante períodos de baixa congestão na blockchain para minimizar as taxas.
Em conclusão, a gestão dos canais da Lightning Network é um elemento importante para manter um nó Lightning eficiente e econômico. Com uma boa estratégia de balanceamento, monitoramento regular e gerenciamento inteligente da abertura e fechamento dos canais, você pode otimizar sua experiência com a Lightning Network. No próximo segmento, abordaremos outro aspecto crucial da Lightning Network: a segurança.

# Renomeando seu nó LN

![renommer son noeud LN](https://youtu.be/HnK1_TDYXsY)

Personalizar o alias do seu nó Lightning Network é uma excelente maneira de se destacar na rede. Não é apenas prático, mas também é uma maneira de personalizar sua experiência. Para alterar o alias do seu nó, usaremos a interface de linha de comando. Para aqueles menos familiarizados com essa interface, não se preocupe, este guia o ajudará passo a passo.

Para começar, você precisa abrir o terminal do seu sistema. O terminal é uma interface de comando que permite interagir diretamente com o seu sistema operacional. Depois de abrir o terminal, digite o comando `ssh -t umbrel@umbrel.local` e pressione Enter. Este comando estabelecerá uma conexão segura com o seu Umbrel.

Em seguida, você será solicitado a inserir a senha do seu Umbrel. Observe que, por motivos de segurança, a senha não é exibida na tela ao digitar. Depois de inserir sua senha, você acessará a interface do seu Umbrel.

Depois de conectado, digite o comando `sudo nano umbrel/lnd/lnd.conf` no terminal e pressione Enter. Isso o levará a um editor de texto chamado Nano, onde você pode editar o arquivo de configuração do seu nó Lightning.

Novamente, você precisará digitar sua senha. Em seguida, navegue pelo arquivo até a seção intitulada "Opções de aplicativo". Nesta seção, adicione a linha `alias=SOMENOME`, substituindo "SOMENOME" pelo alias que você deseja para o seu nó. Observe que o uso do mouse é inútil nesta interface, portanto, use as setas para navegar.

Para salvar as alterações, pressione `Ctrl-X`, depois `Y` e, finalmente, `Enter`. Isso fechará o editor e salvará suas alterações. Para que essas alterações entrem em vigor, você precisa reiniciar seu Umbrel. Para fazer isso, acesse o menu de configurações da interface Umbrel e escolha a opção de reinicialização.

E voilà, você conseguiu alterar o alias do seu nó Lightning Network! Agora você pode reivindicar seu nó em sites como 1ML ou Amboss. Na próxima seção, discutiremos outras maneiras de personalizar e otimizar seu nó Lightning Network.

### Apoie-nos

Este curso, assim como todo o conteúdo presente nesta universidade, foi oferecido gratuitamente pela nossa comunidade. Para nos apoiar, você pode compartilhá-lo com seus amigos, tornar-se um membro da universidade e até mesmo contribuir para o seu desenvolvimento via GitHub. Em nome de toda a equipe, obrigado!

### Nota sobre a formação

Um sistema de classificação para a formação será em breve integrado nesta nova plataforma de E-learning! Enquanto isso, muito obrigado por ter seguido o curso e se você gostou, pense em compartilhá-lo com seus amigos.

# Uso lúdico do LN

![uso do LN](https://youtu.be/6yekAvH13E0)

Agora que você configurou seu nó, é hora de usá-lo. Para esta primeira utilização, vamos nos interessar pelo [Satoshi's Place](https://satoshis.place/), um serviço fascinante que permite gastar satoshis, a menor unidade do bitcoin, para fazer pixel art em um espaço público online. Cada pixel muda de cor por um satoshi. Você é livre para dar asas à sua criatividade, eu mesmo criei uma pokebola por 166 satoshis! Os pagamentos são feitos por meio de "faturas" ou "invoices" na rede Lightning. Essas faturas podem ser representadas na forma de um código QR, tornando o pagamento fácil e instantâneo.

Quando uma transação passa por vários nós, geralmente há taxas de roteamento envolvidas. Portanto, é crucial estar bem conectado ao centro da rede para reduzir esses custos. Uma alternativa seria abrir um canal diretamente com o comerciante. Isso apresenta várias vantagens, incluindo taxas de transação mais baixas e velocidade de transação mais rápida.

Como exemplo, vamos criar um canal com o Satoshi's Place para futuros pagamentos. Após a criação do canal, é necessário esperar cerca de 30 minutos para que o canal se torne operacional. Depois de criado o canal, você pode fazer pagamentos diretos. Por exemplo, você pode enviar um satoshi gratuitamente pela rede Lightning sem intermediários de confiança.

A rede Lightning apresenta várias vantagens, incluindo seu baixo custo e a possibilidade de fazer pagamentos regulares. Para começar, é recomendável usar carteiras como Wallet of Satoshi ou Alby. Essas carteiras permitem pagar faturas usando a rede Lightning. Para saber mais, você pode ler este [artigo](https://asi0.substack.com/p/comparatif-des-portefeuilles-ln) de Darthcoin.

Em conclusão, a rede Lightning prova a capacidade do Bitcoin de evoluir. Não só permite transações de baixo custo, mas também oferece uma solução para os problemas de escala que o Bitcoin enfrentou no passado.

# Aceitar Bitcoin com o servidor BTCpay

![aceitar bitcoin em seu comércio](https://youtu.be/zpCMlLfiRgg)
Au long de este último capítulo, exploraremos as diferentes maneiras de aceitar Bitcoin para o seu negócio. Analisaremos três opções principais: BTCPay Server através do seu nó Umbrel, BTCPay através de um nó externo Luna e, finalmente, através do OpenNode. É essencial notar que cada opção tem suas nuances e é crucial escolher aquela que melhor se adapta às suas necessidades específicas.

Vamos imaginar que você é proprietário de um restaurante e tem um nó Umbrel em seu estabelecimento. Nesse caso, você pode usar o BTCpay diretamente no Tor. É uma solução ideal para operações físicas em que os clientes pagam pessoalmente.

Por outro lado, para um e-commerce, o uso do BTCPay no Tor do seu nó Umbrel não é viável. Nesse caso, é preferível usar um nó externo no clearnet, como o Luna Node. Isso oferece mais flexibilidade e permite uma integração mais suave com sua plataforma de comércio eletrônico.

Para aqueles que procuram uma solução tudo-em-um e fácil de gerenciar, o OpenNode é uma excelente opção. No entanto, sua configuração e uso podem ser bastante complexos. É por isso que planejamos cobrir essa solução com mais detalhes em uma formação dedicada separadamente.

Abaixo estão os links para os diferentes serviços mencionados:

- [OpenNode](https://www.opennode.com/)
- [BTCPay Server](https://btcpayserver.org/)
- [Luna Node](https://www.lunanode.com/) e o guia sobre [BTCPay Server com Luna Node](https://docs.btcpayserver.org/Deployment/LunaNode/)

Além disso, tive a oportunidade de entrevistar Nicolas Dorier, o criador do BTCPay Server. Se você estiver interessado, não hesite em assistir à nossa conversa clicando [aqui](https://www.youtube.com/watch?v=XR6qB76hCL0&pp=ygUoaW50ZXJ2aWV3IG5pY29sYSBkb3JpZXIgZGVjb3V2cmUgYml0Y29pbg%3D%3D). Você descobrirá muitas informações interessantes e valiosas dicas para otimizar o uso do BTCPay Server em seu negócio.

Em resumo, a aceitação do Bitcoin pode oferecer uma infinidade de vantagens para o seu negócio. Seja você um restaurante local ou um e-commerce global, existe uma solução adequada às suas necessidades. Reserve um tempo para examinar as diferentes opções e não hesite em embarcar nesta nova aventura do Bitcoin.

# Resumo da formação

![conclusão](https://youtu.be/QrKbagtUE1s)
Nous chegamos à conclusão de nossa exploração aprofundada da rede Lightning do Bitcoin. Percorremos um caminho complexo, repleto de inovações tecnológicas e novas perspectivas sobre como interagimos com nosso dinheiro digital. Desde a exploração inicial do Umbrel até a abertura e gerenciamento dos canais Lightning, cada etapa foi um passo em direção a uma melhor compreensão e domínio dessa tecnologia revolucionária.

Começamos com uma visão geral do Umbrel, nos familiarizando com a interface e recursos-chave. Em seguida, mergulhamos na Mempool, aprendendo a analisar transações pendentes para uma visão mais aprofundada da rede Bitcoin. Depois, exploramos os exploradores de blocos e estatísticas de rede, ferramentas essenciais para monitorar o estado da rede.

Em seguida, abordamos o aspecto mais pessoal da rede Bitcoin: a carteira. Aprendemos a conectar nossa carteira ao nosso nó e descobrimos a importância e segurança das carteiras multisig com o Specter.

Depois, mergulhamos no universo da rede Lightning. Exploramos a abertura e gerenciamento de canais Lightning, dois aspectos cruciais para o funcionamento ideal do nosso nó. Também aprendemos a renomear nosso nó para facilitar sua identificação na rede.

Também tivemos uma visão divertida do uso da Lightning Network com o Satoshi's Place, um exemplo concreto de como a LN pode ser usada para microtransações de baixo custo.

Por fim, abordamos o aspecto comercial do Bitcoin. Exploramos como aceitar Bitcoin em nosso comércio por meio do BTCpay server, levando em consideração diferentes configurações de acordo com as necessidades.

Dito isso, dominar a rede Lightning não é uma tarefa que se faz em um dia. É uma tecnologia em constante evolução, complexa e sutil. Levará tempo, prática e vontade de aprender para realmente dominar essa ferramenta. Assim como o próprio Bitcoin, a Lightning Network é uma aventura, uma exploração do que é possível no campo das finanças digitais. Mas com paciência, perseverança e vontade de aprender, em breve você será capaz de navegar na rede Lightning com facilidade e confiança.

Em resumo, a jornada que empreendemos juntos pela rede Lightning é apenas o começo. Dominar essa tecnologia oferece muitas oportunidades e benefícios. Então continue explorando, aprendendo e experimentando com a Lightning Network. O futuro das finanças está ao seu alcance.
Pour concluir, é importante destacar que esta formação, assim como as outras que oferecemos, é totalmente gratuita. Acreditamos firmemente na importância de compartilhar conhecimento e tornar o acesso à informação o mais livre e aberto possível. É nesse espírito que decidimos compartilhar com você tudo o que aprendemos sobre a rede Lightning.

No entanto, se você encontrou valor nesta formação e deseja nos apoiar, convidamos você a visitar nosso site de comércio eletrônico no seguinte endereço: https://thebitcoinrabbithole.myshopify.com/. Ao fazer compras em nosso site, você contribui não apenas para apoiar nosso trabalho, mas também nos ajuda a continuar fornecendo formações gratuitas e de alta qualidade.

Obrigado por dedicar seu tempo a esta formação. Seu apoio e interesse em nosso trabalho significam muito para nós.

# Agradecimentos e continue a cavar a toca do coelho

Parabéns por concluir esta formação LN 202! Espero sinceramente que tenha gostado e aberto portas para você. Sua descoberta do bitcoin está apenas começando e convido você a descobrir todas as outras formações disponíveis na universidade.

- ECON 201 abordará a economia austríaca
- SECU 101 permitirá que você atualize sua segurança
- MINAGE 201 para saber mais sobre mineração
- (e muitos outros)

Beijos e até breve!
