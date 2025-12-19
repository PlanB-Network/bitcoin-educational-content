---
name: Programação RGB
goal: Adquirir as competências necessárias para compreender e utilizar o RGB
objectives:
- Compreender os conceitos fundamentais do protocolo RGB
- Dominar os princípios da validação do lado do cliente e dos compromissos Bitcoin
- Saiba como criar, gerir e transferir contratos RGB
- Como operar um nó Lightning compatível com RGB
---
# Descobrir o protocolo RGB

Mergulhe no mundo do RGB, um protocolo concebido para implementar e fazer cumprir direitos digitais, sob a forma de contratos e activos, com base nas regras de consenso e operações da cadeia de blocos Bitcoin. Este curso de formação abrangente guia-o através dos fundamentos técnicos e práticos do RGB, desde os conceitos de "Validação do lado do cliente" e "Selos de utilização única", até à implementação de contratos inteligentes avançados.

Através de um programa estruturado e passo a passo, descobrirá os mecanismos de validação do lado do cliente, compromissos determinísticos no Bitcoin e padrões de interação entre utilizadores. Aprenderá a criar, gerir e transferir RGB tokens em Bitcoin ou na Lightning Network.

Quer seja um programador, um entusiasta do Bitcoin ou simplesmente um curioso para saber mais sobre esta tecnologia, este curso de formação irá fornecer-lhe as ferramentas e os conhecimentos necessários para dominar o RGB e criar soluções inovadoras no Bitcoin.

O curso baseia-se num seminário ao vivo organizado pela Fulgur'Ventures e ministrado por três professores de renome e especialistas em RGB.

+++
# Introdução

<partId>c6f7a70f-d894-595f-8c0a-b54759778839</partId>

## Apresentação do curso

<chapterId>cf2f087b-6c6b-5037-8f98-94fc9f1d7f46</chapterId>

Olá a todos, e bem-vindos a este curso de formação dedicado ao RGB, um sistema de contrato inteligente validado do lado do cliente que funciona com Bitcoin e a Lightning Network. A estrutura deste curso foi concebida para permitir uma exploração aprofundada deste assunto complexo. Veja como o curso está organizado:

**Secção 1: Teoria**

A primeira secção é dedicada aos conceitos teóricos necessários para compreender os fundamentos da validação do lado do cliente e do RGB. Como você descobrirá neste curso, o RGB introduz uma série de conceitos técnicos que não são normalmente vistos no Bitcoin. Nesta seção, você também encontrará um glossário que fornece definições para todos os termos específicos do protocolo RGB.

**Secção 2: Prática**

A segunda secção centrar-se-á na aplicação dos conceitos teóricos vistos na secção 1. Aprenderemos a criar e a manipular contratos RGB. Veremos também como programar com estas ferramentas. Estas duas primeiras secções são apresentadas por Maxim Orlovsky.

**Secção 3: Aplicações**

A secção final é conduzida por outros oradores que apresentam aplicações concretas baseadas em RGB, para realçar casos de utilização reais.

---
Este curso de formação surgiu originalmente de um bootcamp de desenvolvimento avançado de duas semanas em Viareggio, Toscana, organizado pela [Fulgur'Ventures](https://fulgur.ventures/). A primeira semana, focada em Rust e SDKs, pode ser encontrada neste outro curso:

https://planb.academy/courses/9fbd8b57-f278-4304-8d88-a2d384eaff58

Neste curso, concentramo-nos na segunda semana do bootcamp, que se centra no RGB.

**Semana 1 - LNP402:**

![RGB-Bitcoin](assets/en/001.webp)

**Semana 2 - Formação atual CSV402:**

![RGB-Bitcoin](assets/en/002.webp)

Muito obrigado aos organizadores destes cursos em direto e aos 3 professores que participaram:


- Maxim Orlovsky: *Ex Tenebrae sententia sapiens dominabitur astris. Cypher, IA, robótica, transhumanismo. Criador de RGB, Prime, Radiant e lnp_bp, mycitadel_io & cyphernet_io* ;
- Hunter Trujilo: *Programador, Rust, Bitcoin, Lightning, RGB* ;
- Federico Tenga: *Estou a fazer a minha parte para transformar o mundo numa distopia cypherpunk. Atualmente a trabalhar no RGB na Bitfinex*.

A versão escrita deste curso de formação foi elaborada com base em dois recursos principais:


- Vídeos do seminário de Maxim Orlovsky, Hunter Trujilo e Frederico Tenga no Lightning Bootcamp ;
- A documentação RGB, cuja produção foi patrocinada pela [Bitfinex] (https://www.bitfinex.com/).

Pronto para mergulhar no universo complexo e fascinante do RGB? Vamos lá!

# RGB em teoria

<partId>80e797ee-3f33-599f-ab82-e82eeee08219</partId>

## Introdução aos conceitos de computação distribuída

<chapterId>f52f8af5-5d7c-588b-b56d-99b97176204b</chapterId>

:::video id=f27338bc-4210-4a2e-9b27-30278ed3282c:::

O RGB é um protocolo concebido para aplicar e fazer cumprir direitos digitais (sob a forma de contratos e activos) de forma escalável e confidencial, com base nas regras e operações de consenso da cadeia de blocos Bitcoin. O objetivo deste primeiro capítulo é apresentar os conceitos básicos e a terminologia em torno do protocolo RGB, destacando em particular as suas ligações estreitas com conceitos básicos de computação distribuída, como a validação do lado do cliente e os selos de utilização única.

Neste capítulo, exploraremos os fundamentos dos **sistemas de consenso distribuído** e veremos como o RGB se encaixa nessa família de tecnologias. Apresentaremos também os princípios principais que nos ajudam a compreender por que razão o RGB pretende ser extensível e independente do mecanismo de consenso do Bitcoin, embora dependa dele quando necessário.

### Introdução

A computação distribuída, um ramo específico da ciência da computação, estuda os protocolos utilizados para fazer circular e processar informações numa rede de nós. No seu conjunto, estes nós e as regras do protocolo constituem o que se designa por sistema distribuído. Entre as propriedades essenciais que caracterizam um sistema deste tipo contam-se :


- A **capacidade de verificação e validação independentes** de determinados dados por cada nó;
- A possibilidade de os nós construírem (consoante o protocolo) uma visão completa ou parcial da informação. Estas vistas são os **estados** do sistema distribuído;
- A **ordem cronológica** das operações, para que os dados sejam registados de forma fiável no tempo e haja um consenso sobre a sequência dos acontecimentos (sequência de estados).

Em particular, a noção de **consenso** num sistema distribuído abrange dois aspectos:


- Reconhecimento da **validade** das alterações de estado (de acordo com as regras do protocolo);
- O **acordo sobre a ordem** destas alterações de estado, que torna impossível reescrever ou reverter operações validadas a posteriori (isto também é conhecido na Bitcoin como "proteção contra gastos duplos").

A primeira implementação funcional e sem permissões de um mecanismo de consenso distribuído foi introduzida por Satoshi Nakamoto com a Bitcoin, graças à utilização combinada de uma estrutura de dados de cadeia de blocos e de um algoritmo de prova de trabalho (PoW). Neste sistema, a credibilidade do historial do bloco depende do poder de computação que lhe é dedicado pelos nós (mineiros). A Bitcoin é, por conseguinte, um exemplo histórico e importante de um sistema de consenso distribuído aberto a todos (*sem permissões*).

No mundo do blockchain e da computação distribuída, podemos distinguir dois paradigmas fundamentais: ***blockchain*** no sentido tradicional, e ***canais de estado***, cujo melhor exemplo em produção é a Lightning Network. A blockchain é definida como um registo de eventos ordenados cronologicamente, replicados por consenso numa rede aberta e sem permissões. Os canais de estado, por outro lado, são canais peer-to-peer que permitem a dois (ou mais) participantes manter um estado atualizado fora da cadeia, utilizando a cadeia de blocos apenas quando abrem e fecham esses canais.

No contexto da Bitcoin, está sem dúvida familiarizado com os princípios de mineração, descentralização e finalidade das transacções na blockchain, bem como com o funcionamento dos canais de pagamento. Com o RGB, estamos a introduzir um novo paradigma chamado **Client-side Validation**, que, ao contrário do blockchain ou do Lightning, consiste em armazenar e validar localmente (do lado do cliente) as transições de estado de um contrato inteligente. Também difere de outras técnicas "DeFi" (_rollups_, _plasma_, _ARK_, etc.), na medida em que a validação do lado do cliente se baseia na blockchain para evitar gastos duplos e para ter um sistema de marcação de tempo, mantendo o registo de estados e transições fora da cadeia, apenas com os participantes em causa.

![RGB-Bitcoin](assets/en/003.webp)

Mais adiante, introduziremos também um termo importante: a noção de "**stash**", que se refere ao conjunto de dados do lado do cliente necessários para preservar o estado de um contrato, uma vez que estes dados não são replicados globalmente na rede. Por fim, analisaremos a lógica subjacente ao RGB, um protocolo que tira partido da validação do lado do cliente, e a razão pela qual complementa as abordagens existentes (blockchain e canais de estado).

### Trilemas na computação distribuída

Para entender como a validação do lado do cliente e o RGB abordam problemas não resolvidos pelo blockchain e pelo Lightning, vamos descobrir três grandes "trilemas" na computação distribuída:


- **Escalabilidade, descentralização, privacidade**;
- **Teorema CAP** (Consistência, Disponibilidade, Tolerância de Partição);
- Trilema **CIA** (Confidencialidade, Integridade, Disponibilidade).

#### 1. Escalabilidade, descentralização e confidencialidade


- **Cadeia de blocos (Bitcoin)**

A cadeia de blocos é altamente descentralizada, mas não é muito escalável. Além disso, como tudo está num registo global e público, a confidencialidade é limitada. Podemos tentar melhorar a confidencialidade com tecnologias de conhecimento zero (transacções confidenciais, esquemas mimblewimble, etc.), mas a cadeia pública não pode esconder o gráfico da transação.


- **Relâmpagos/Canais estatais**

Os canais estatais (como a Lightning Network) são mais escaláveis e mais privados do que a cadeia de blocos, uma vez que as transacções têm lugar fora da cadeia. No entanto, a obrigação de anunciar publicamente certos elementos (transacções de financiamento, topologia da rede) e a monitorização do tráfego da rede podem comprometer parcialmente a confidencialidade. A descentralização também é afetada: o encaminhamento é intensivo em dinheiro e os nós principais podem tornar-se pontos de centralização. É precisamente este o fenómeno a que começamos a assistir no Lightning.


- **Validação do lado do cliente (RGB)**

Este novo paradigma é ainda mais escalável e mais confidencial, porque não só podemos integrar técnicas de prova de conhecimento de divulgação zero, como também não existe um gráfico global de transacções, uma vez que ninguém detém o registo completo. Por outro lado, também implica um certo compromisso em relação à descentralização: o emissor de um contrato inteligente pode ter um papel central (como um "implantador de contrato" no Ethereum). No entanto, ao contrário da blockchain, com a Validação do lado do cliente, apenas armazena e valida os contratos que lhe interessam, o que melhora a escalabilidade ao evitar a necessidade de descarregar e verificar todos os estados existentes.

![RGB-Bitcoin](assets/en/004.webp)

#### 2. Teorema CAP (Consistência, Disponibilidade, Tolerância de Partição)

O teorema CAP sublinha que é impossível um sistema distribuído satisfazer simultaneamente a consistência (*Consistência*), a disponibilidade (*Disponibilidade*) e a tolerância de partição (*Tolerância de partição*).


- **Cadeia de blocos**

A cadeia de blocos favorece a consistência e a disponibilidade, mas não se dá bem com o particionamento da rede: se não se consegue ver um bloco, não se pode atuar e ter a mesma visão que toda a rede.


- **Relâmpagos** (em francês)

Um sistema de canais de estado tem disponibilidade e tolerância de partição (uma vez que dois nós podem permanecer ligados um ao outro mesmo que a rede esteja fragmentada), mas a consistência global depende da abertura e fecho de canais na cadeia de blocos.


- **Validação do lado do cliente (RGB)**

Um sistema como o RGB oferece consistência (cada participante valida os seus dados localmente, sem ambiguidade) e tolerância de partição (o utilizador mantém os seus dados de forma autónoma), mas não garante a disponibilidade global (cada um tem de se certificar de que possui os elementos relevantes do historial e alguns participantes podem não publicar nada ou deixar de partilhar determinadas informações).

![RGB-Bitcoin](assets/en/005.webp)

#### 3. Trilema CIA (Confidencialidade, Integridade, Disponibilidade)

Este trilema recorda-nos que a confidencialidade, a integridade e a disponibilidade não podem ser optimizadas ao mesmo tempo. Blockchain, Lightning e Validação do lado do cliente caem de forma diferente neste equilíbrio. A ideia é que nenhum sistema pode fornecer tudo; é necessário combinar várias abordagens (o registo de tempo da blockchain, a abordagem síncrona da Lightning e a validação local com RGB) para obter um pacote coerente que ofereça boas garantias em cada dimensão.

![RGB-Bitcoin](assets/en/006.webp)

### O papel da cadeia de blocos e a noção de fragmentação

O blockchain (neste caso, o Bitcoin) serve principalmente como um mecanismo de _time-stamping_ e proteção contra gastos duplos. Em vez de inserir os dados completos de um contrato inteligente ou de um sistema descentralizado, incluímos simplesmente **compromissos criptográficos** (_compromissos_) para as transacções (no sentido da validação do lado do cliente, a que chamaremos "transições de estado"). Assim :


- Libertamos a cadeia de blocos de uma grande quantidade de dados e lógica;
- Cada utilizador armazena apenas o histórico necessário para a sua própria parte do contrato (o seu "*shard*"), em vez de replicar o estado global.

O sharding é um conceito que teve origem nas bases de dados distribuídas (por exemplo, MySQL para redes sociais como o Facebook ou o Twitter). Para resolver o problema do volume de dados e das latências de sincronização, a base de dados é segmentada em _shards_ (EUA, Europa, Ásia, etc.). Cada segmento é localmente consistente e apenas parcialmente sincronizado com os outros.

Para os contratos inteligentes do tipo RGB, fragmentamos de acordo com os próprios contratos. Cada contrato é um _shard_ independente. Por exemplo, se só tiver tokens USDT, não precisa de armazenar ou validar todo o histórico de outro token como o USDC. No Bitcoin, a blockchain não faz _sharding_: tem um conjunto global de UTXOs. Com a validação do lado do cliente, cada participante retém apenas os dados do contrato que detém ou utiliza.

Podemos, portanto, imaginar o ecossistema da seguinte forma:


- A cadeia de blocos **(Bitcoin)** como base que assegura a replicação completa de um registo mínimo e serve de camada de registo temporal;
- A **Lightning Network** para transacções rápidas e confidenciais, ainda baseadas na segurança e na liquidação final da blockchain Bitcoin;
- **RGB e Validação do lado do cliente** para adicionar uma lógica de contrato inteligente mais complexa, sem sobrecarregar a cadeia de blocos ou perder a confidencialidade.

![RGB-Bitcoin](assets/en/007.webp)

Estes três elementos formam um todo triangular, em vez de uma pilha linear de "camada 2", "camada 3" e assim por diante. O Lightning pode ligar-se diretamente à Bitcoin ou ser associado a transacções Bitcoin que incorporem dados RGB. Do mesmo modo, uma utilização "BiFi" (finanças em Bitcoin) pode compor-se com a cadeia de blocos, com Lightning e com RGB de acordo com as necessidades de confidencialidade, escalabilidade ou lógica de contrato.

![RGB-Bitcoin](assets/en/008.webp)

### A noção de transições de estado

Em qualquer sistema distribuído, o objetivo do mecanismo de validação é poder **determinar a validade e a ordem cronológica das mudanças de estado**. O objetivo é verificar se as regras do protocolo foram respeitadas e provar que estas alterações de estado se sucedem numa ordem definitiva e inatacável.

Para compreender como funciona esta validação no contexto da **Bitcoin** e, de uma forma mais geral, para compreender a filosofia subjacente à validação do lado do cliente, vamos primeiro analisar os mecanismos da blockchain da Bitcoin, antes de ver como a validação do lado do cliente difere deles e quais as optimizações que torna possíveis.

![RGB-Bitcoin](assets/en/009.webp)

No caso da cadeia de blocos Bitcoin, a validação da transação baseia-se numa regra simples:


- Todos os nós da rede descarregam todos os blocos e transacções;
- Validam estas transacções para verificar a evolução correta do conjunto UTXO (todas as saídas não gastas);
- Armazenam estes dados (sob a forma de blocos) para que o historial possa ser reproduzido, se necessário.

![RGB-Bitcoin](assets/en/010.webp)

No entanto, este modelo tem dois grandes inconvenientes:


- **Escalabilidade**: uma vez que cada nó deve processar, verificar e arquivar as transacções de todos, existe um limite óbvio para a capacidade de transação, ligado em particular ao tamanho máximo do bloco (1 MB em média em 10 minutos para a Bitcoin, excluindo os cookies);
- **Privacidade**: tudo é transmitido e armazenado publicamente (montantes, endereços de destino, etc.), o que limita a confidencialidade das trocas.

![RGB-Bitcoin](assets/en/012.webp)

Na prática, este modelo funciona para a Bitcoin como camada de base (camada 1), mas pode tornar-se insuficiente para utilizações mais complexas que exijam simultaneamente um elevado débito de transacções e um certo grau de confidencialidade.

A validação do lado do cliente baseia-se na ideia oposta: em vez de exigir que toda a rede valide e armazene todas as transacções, cada participante (cliente) validará apenas a parte do histórico que lhe diz respeito:


- Quando uma pessoa recebe um ativo (ou qualquer outro bem digital), só precisa de conhecer e verificar a cadeia de operações (transições de estado) que conduziram a esse ativo e provar a sua legitimidade;
- Esta sequência de operações, desde a ***Génese*** (emissão inicial) até à transação mais recente, forma um gráfico acíclico dirigido (DAG) ou shard, ou seja, uma fração do histórico global.

![RGB-Bitcoin](assets/en/013.webp)

Ao mesmo tempo, para que o resto da rede (ou, mais precisamente, a camada subjacente, como a Bitcoin) possa bloquear o estado final sem ver os detalhes desses dados, a validação do lado do cliente baseia-se na noção de ***compromisso***.

Um *compromisso* é um compromisso criptográfico, normalmente um _hash_ (SHA-256, por exemplo) inserido numa transação Bitcoin, que prova que foram incluídos dados privados, sem revelar esses dados.

Graças a estes _compromissos_, podemos provar:


- A existência de informação (uma vez que está comprometida com um hash) ;
- A anterioridade desta informação (porque está ancorada e registada na cadeia de blocos, com uma data e uma ordem de blocos).

No entanto, o conteúdo exato não é revelado, preservando assim a sua confidencialidade.

Em termos concretos, eis como funciona uma transição de estado RGB:


- Prepara uma nova transição de estado (por exemplo, a transferência de uma ficha RGB);
- O utilizador gera um compromisso criptográfico para esta transição e insere-o numa transação Bitcoin (estes compromissos são designados "*âncoras*" no protocolo RGB);
- A contraparte (o destinatário) recupera o histórico do lado do cliente associado a este ativo e valida a consistência de ponta a ponta, desde a génese do contrato inteligente até à transição que lhe é transmitida.

![RGB-Bitcoin](assets/en/014.webp)

A validação do lado do cliente oferece duas grandes vantagens:


- **Escalabilidade:**

Os compromissos (*compromissos*) incluídos na cadeia de blocos são pequenos (da ordem de algumas dezenas de bytes). Isso garante que o espaço do bloco não seja saturado, pois apenas o hash precisa ser incluído. Também permite a evolução do protocolo fora da cadeia, uma vez que cada utilizador só tem de armazenar o seu fragmento de história (o seu _stash_).


- **Privacidade:**

As transacções propriamente ditas (ou seja, o seu conteúdo detalhado) não são publicadas na cadeia. Apenas as suas impressões digitais (*hash*) o são. Assim, os valores, endereços e lógica de contrato permanecem privados, e o recetor pode verificar, localmente, a validade do seu fragmento inspeccionando todas as transições anteriores. Não há razão para o recetor tornar estes dados públicos, exceto em caso de disputa ou quando é necessária uma prova.

Num sistema como o RGB, múltiplas transições de estado de diferentes contratos (ou diferentes activos) podem ser agregadas numa única transação Bitcoin através de um único _commitment_. Este mecanismo estabelece uma ligação determinística, com registo de data e hora, entre a transação na cadeia e os dados fora da cadeia (as transições validadas do lado do cliente), e permite que vários fragmentos sejam simultaneamente registados num único ponto de ancoragem, reduzindo ainda mais o custo e a pegada na cadeia.

Na prática, quando esta transação Bitcoin é validada, "bloqueia" permanentemente o estado dos contratos subjacentes, uma vez que se torna impossível modificar o hash já inscrito na cadeia de blocos.

![RGB-Bitcoin](assets/en/015.webp)

### O conceito de esconderijo

Um **stash** é o conjunto de dados do lado do cliente que um participante deve absolutamente reter para manter a integridade e o histórico de um contrato inteligente RGB. Ao contrário de um canal Lightning, onde certos estados podem ser reconstruídos localmente a partir de informações compartilhadas, o stash de um contrato RGB não é replicado em outro lugar: se você o perder, ninguém será capaz de restaurá-lo para você, pois você é responsável por sua parte do histórico. É por isso que é necessário adotar um sistema com procedimentos de cópia de segurança fiáveis em RGB.

![RGB-Bitcoin](assets/en/016.webp)

### Selo de utilização única: origens e funcionamento

Ao aceitar um ativo como uma moeda, são essenciais duas garantias:


- A autenticidade do artigo recebido;
- A singularidade do artigo recebido, para evitar despesas duplas.

Para activos físicos, como uma nota de banco, a presença física é suficiente para provar que não foi duplicada. No entanto, no mundo digital, onde os activos são puramente informativos, esta verificação é mais complexa, uma vez que a informação pode facilmente multiplicar-se e ser duplicada.

Como vimos anteriormente, o facto de o remetente revelar o histórico das transições de estado permite-nos garantir a autenticidade de um token RGB. Ao ter acesso a todas as transacções desde a transação de génese, podemos confirmar a autenticidade do token. Este princípio é semelhante ao da Bitcoin, em que o histórico das moedas pode ser rastreado até à transação original da coinbase para verificar a sua validade. No entanto, ao contrário da Bitcoin, este historial de transições de estado na RGB é privado e mantido no lado do cliente.

Para evitar o gasto duplo de fichas RGB, utilizamos um mecanismo denominado "**Selo de utilização única**". Este sistema garante que cada ficha, uma vez utilizada, não pode ser reutilizada de forma fraudulenta uma segunda vez.

Os selos de utilização única são primitivos criptográficos, propostos em 2016 por Peter Todd, semelhantes ao conceito de selos físicos: uma vez colocado um selo num contentor, torna-se impossível abri-lo ou modificá-lo sem quebrar irreversivelmente o selo.

![RGB-Bitcoin](assets/en/018.webp)

Esta abordagem, transposta para o mundo digital, permite provar que uma sequência de eventos teve efetivamente lugar e que já não pode ser alterada a posteriori. Os selos de utilização única ultrapassam assim a lógica simples de `hash + timestamp`, acrescentando a noção de um selo que pode ser fechado **uma única vez**.

![RGB-Bitcoin](assets/en/017.webp)

Para que os selos de uso único funcionem, é necessário um meio de prova de publicação capaz de provar a existência ou ausência de uma publicação e difícil (se não impossível) de falsificar depois de a informação ter sido disseminada. Uma **blockchain** (como a Bitcoin) pode desempenhar esse papel, assim como um jornal em papel de circulação pública, por exemplo. A ideia é a seguinte:


- Queremos provar que um determinado compromisso sobre uma mensagem `h(m)` foi publicado para um público sem revelar o conteúdo da mensagem `m` ;
- Pretendemos provar que nenhum outro compromisso de mensagem `h(m')` concorrente foi publicado em vez de `h(m)` ;
- Também queremos poder verificar se a mensagem `m` existe antes de uma determinada data.

Uma cadeia de blocos presta-se idealmente a este papel: assim que uma transação é incluída num bloco, toda a rede tem a mesma prova infalsificável da sua existência e do seu conteúdo (pelo menos em parte, uma vez que o _compromisso_ pode esconder os pormenores ao mesmo tempo que prova a autenticidade da mensagem).

Um selo de utilização única pode, portanto, ser visto como uma promessa formal de publicar uma mensagem (ainda desconhecida nesta fase) uma vez e apenas uma vez, de uma forma que possa ser verificada por todas as partes interessadas.

Ao contrário dos _compromissos_ simples (hash) ou dos carimbos de data/hora, que atestam uma data de existência, um selo de utilização única oferece a garantia adicional de que **nenhum compromisso alternativo** pode coexistir: não se pode fechar o mesmo selo duas vezes, nem tentar substituir a mensagem selada.

A comparação que se segue ajuda a compreender este princípio:


- **Compromisso criptográfico (hash)**: Com uma função de hash, é possível comprometer-se com um dado (um número) publicando o seu hash. Os dados permanecem secretos até revelar a pré-imagem, mas pode provar que os conhecia antecipadamente;
- **Carimbo de data/hora (blockchain)**: Ao inserir este hash na cadeia de blocos, provamos também que o conhecíamos num momento preciso (o da inclusão num bloco);
- **Selo de utilização única**: Com os selos de utilização única, damos um passo em frente ao tornar o compromisso único. Com um único hash, é possível criar vários compromissos contraditórios em paralelo (o problema do médico que anuncia "*É um rapaz*" à família e "*É uma rapariga*" no seu diário pessoal). O Selo de Utilização Única elimina esta possibilidade ligando o compromisso a um meio de prova de publicação, como a cadeia de blocos Bitcoin, de modo que uma despesa de UTXO sela definitivamente o compromisso. Uma vez gasto, o mesmo UTXO não pode ser gasto novamente para substituir o compromisso.

|                                                                                  | Compromisso simples (digest/hash) | Timestamps | Selos de uso único |
| -------------------------------------------------------------------------------- | -------------------------------- | ---------- | ------------------ |
| A publicação do compromisso não revela a mensagem                              | Sim                             | Sim        | Sim               |
| Prova da data do compromisso / existência da mensagem antes de uma determinada data | Impossível                      | Possível    | Possível          |
| Prova de que nenhum outro compromisso alternativo pode existir                 | Impossível                      | Impossível  | Possível          |


Os selos de utilização única funcionam em três fases principais:

**Definição de vedação :**


- Alice define antecipadamente as regras de publicação do selo (quando, onde e como a mensagem será publicada);
- O Bob aceita ou reconhece estas condições.

![RGB-Bitcoin](assets/en/021.webp)

**Fechamento do selo :**


- Em tempo de execução, Alice fecha o selo publicando a mensagem efectiva (normalmente sob a forma de um _commitment_, por exemplo, um hash);
- Fornece também uma **testemunha** (prova criptográfica) que prova que o selo é fechado e irrevogável.

![RGB-Bitcoin](assets/en/019.webp)

**Verificação da selagem :**


- Uma vez fechado o selo, o Bob já não o pode abrir: apenas pode verificar se está fechado;
- O Bob recolhe o selo, a **testemunha** e a mensagem (ou o seu compromisso) para se certificar de que tudo corresponde e de que não existem selos concorrentes ou versões diferentes.

O processo pode ser resumido da seguinte forma:

```txt
# Defined by Alice, validated or accepted by Bob
seal <- Define()
# Seal is closed by Alice with the message
witness <- Close(seal, message)
# Verification by Bob
bool <- Verify(seal, witness, message)
```

No entanto, a validação do lado do cliente vai um passo mais além: se a definição de um selo permanecer fora da cadeia de blocos, é possível (em teoria) que alguém conteste a existência ou a legitimidade do selo em questão. Para ultrapassar este problema, é utilizada uma cadeia de selos de utilização única interligados:


- Cada selo fechado contém a definição do selo seguinte;
- Registamos estes encerramentos (com os seus _compromissos_) na cadeia de blocos (numa transação Bitcoin);
- Assim, qualquer tentativa de modificar um selo anterior estaria em contradição com a história incorporada na Bitcoin.

É exatamente isso que o sistema RGB faz:


- As mensagens publicadas são _compromissos_ com dados validados do lado do cliente;
- A definição do selo está associada a um Bitcoin UTXO ;
- O selo fecha-se quando esta UTXO é gasta ou quando uma nova saída é creditada ao mesmo compromisso;
- A cadeia de transacções que gasta estes UTXOs corresponde à prova de publicação: cada transição ou mudança de estado no RGB está assim ancorada na Bitcoin.

Em suma:


- A _definição de selagem_ é o UTXO que pretende selar um compromisso futuro;
- O _seal closing_ ocorre quando se gasta este UTXO, criando uma transação que contém o compromisso;
- A _testemunha_ é a própria transação, que prova que fechou o selo com este conteúdo;
- Não pode provar que um selo não foi fechado (não pode ter a certeza absoluta de que um UTXO não foi já gasto ou não será gasto num bloco que ainda não viu), mas pode provar que foi efetivamente fechado.

Esta singularidade é importante para a validação do lado do cliente: quando valida uma transição de estado, verifica se esta corresponde a um UTXO único, não gasto anteriormente num compromisso concorrente. É isto que garante a ausência de gastos duplos em contratos inteligentes fora da cadeia.

### Múltiplos compromissos e raízes

Um contrato inteligente RGB pode precisar gastar vários selos de uso único (vários UTXOs) simultaneamente. Além disso, uma única transação Bitcoin pode fazer referência a vários contratos distintos, cada um selando a sua própria transição de estado. Isto requer um mecanismo de **multi-compromisso** para provar, de forma determinística e única, que nenhum dos compromissos existe em duplicado. É aqui que a noção de **anchor** entra em jogo no RGB: uma estrutura especial que liga uma transação Bitcoin e um ou mais compromissos do lado do cliente (transições de estado), cada um potencialmente pertencente a um contrato diferente. Iremos analisar este conceito mais detalhadamente no próximo capítulo.

![RGB-Bitcoin](assets/en/023.webp)

Dois dos principais repositórios GitHub do projeto (sob a organização LNPBP) agrupam as implementações básicas destes conceitos estudados no primeiro capítulo:


- **validação_do_lado_do_cliente**: Contém primitivas Rust para validação local ;
- **single_use_seals**: Implementa a lógica para definir e fechar estes selos de forma segura.

![RGB-Bitcoin](assets/en/020.webp)

Note-se que estes blocos de software são agnósticos em relação à Bitcoin; em teoria, poderiam ser aplicados a qualquer outro meio de prova de publicação (outro registo, um jornal, etc.). Na prática, o RGB depende do Bitcoin pela sua robustez e consenso alargado.

![RGB-Bitcoin](assets/en/021.webp)

### Perguntas do público

#### Para uma utilização mais alargada dos selos de utilização única

Peter Todd também criou o protocolo _Open Timestamps_, e o conceito de Single-use Seal é uma extensão natural destas ideias. Para além do RGB, podem ser previstos outros casos de utilização, como a construção de _sidechains_ sem recorrer ao _merge mining_ ou a propostas relacionadas com drivechains como o BIP300. Qualquer sistema que exija um único compromisso pode, em princípio, explorar esta primitiva criptográfica. Atualmente, o RGB é a primeira grande implementação em grande escala.

#### Problemas de disponibilidade de dados

Uma vez que, na validação do lado do cliente, cada utilizador armazena a sua própria parte do histórico, a disponibilidade dos dados não é garantida globalmente. Se o emitente de um contrato retiver ou revogar determinadas informações, o utilizador pode não ter conhecimento da evolução real da oferta. Nalguns casos (como o das stablecoins), espera-se que o emitente mantenha dados públicos que comprovem o volume em circulação, mas não existe qualquer obrigação técnica de o fazer. Por conseguinte, é possível conceber contratos deliberadamente opacos com oferta ilimitada, o que levanta questões de confiança.

#### Fragmentação e isolamento de contratos

Cada contrato representa um _shard_ isolado: O USDT e o USDC, por exemplo, não têm de partilhar os seus históricos. As trocas atómicas continuam a ser possíveis, mas isso não implica a fusão dos seus registos. Tudo é feito através de um compromisso criptográfico, sem revelar todo o histórico a cada participante.

### Conclusão

Vimos onde o conceito de Validação do lado do cliente se encaixa com blockchain e _state channels_, como ele responde a trilemas de computação distribuída, e como ele alavanca o blockchain do Bitcoin exclusivamente para evitar gastos duplos e para *time-stamping*. A ideia baseia-se na noção de **Selo de utilização única**, permitindo a criação de compromissos únicos que não podem ser reutilizados à vontade. Desta forma, cada participante carrega apenas o histórico estritamente necessário, aumentando a escalabilidade e a confidencialidade dos contratos inteligentes, mantendo a segurança do Bitcoin como pano de fundo.

O próximo passo será explicar com mais detalhes como esse mecanismo de Single-use Seal é aplicado no Bitcoin (via UTXOs), como as âncoras são criadas e validadas e, em seguida, como contratos inteligentes completos são construídos em RGB. Em particular, analisaremos a questão dos compromissos múltiplos, o desafio técnico de provar que uma transação Bitcoin sela simultaneamente várias transições de estado em diferentes contratos, sem introduzir vulnerabilidades ou compromissos duplos.

Antes de mergulhar nos detalhes mais técnicos do segundo capítulo, não hesite em reler as principais definições (validação do lado do cliente, selo de utilização única, âncoras, etc.) e tenha em mente a lógica geral: estamos a tentar conciliar os pontos fortes da cadeia de blocos Bitcoin (segurança, descentralização, registo de data e hora) com os das soluções fora da cadeia (velocidade, confidencialidade, escalabilidade), e é precisamente isto que o RGB e a validação do lado do cliente estão a tentar alcançar.

## A camada de compromisso

<chapterId>cc2fe85a-9cc7-5b8c-a00a-c0a867241061</chapterId>

:::video id=73ddea2d-c243-479d-a3dc-12d7db8eef70:::

Neste capítulo, veremos a implementação da validação do lado do cliente e dos selos de uso único dentro da blockchain do Bitcoin. Apresentaremos os principais princípios da **camada de compromisso** (camada 1) da RGB, com um foco particular no esquema **TxO2**, que a RGB usa para definir e fechar um selo em uma transação Bitcoin. De seguida, discutiremos dois pontos importantes que ainda não foram abordados em pormenor:


- Os _compromissos determinísticos da Bitcoin_;
- Compromissos multi-protocolo.

É a combinação destes conceitos que nos permite sobrepor vários sistemas ou contratos a um único UTXO e, por conseguinte, a uma única cadeia de blocos.

Recorde-se que as operações criptográficas descritas podem ser aplicadas, em termos absolutos, a outras blockchains ou meios de publicação, mas as caraterísticas da Bitcoin (em termos de descentralização, resistência à censura e abertura a todos) fazem dela a base ideal para o desenvolvimento de uma programação avançada como a exigida pela **RGB**.

### Esquemas de compromisso na Bitcoin e a sua utilização pela RGB

Como vimos no primeiro capítulo do curso, Selos de uso único são um conceito geral: fazemos uma promessa de incluir um compromisso (_compromisso_) em um local específico de uma transação, e esse local atua como um selo que fechamos em uma mensagem. No entanto, na blockchain do Bitcoin, existem várias opções para escolher onde colocar esse _compromisso_.

Para entender a lógica, vamos relembrar o princípio básico: para fechar um _selo de uso único_, gastamos a área selada inserindo o _compromisso_ numa determinada mensagem. Em Bitcoin, isso pode ser feito de várias maneiras:


- Utilizar uma chave pública ou um endereço

Podemos decidir que uma chave pública ou endereço específico é o _selo de utilização única_. Assim que esta chave ou endereço aparece na cadeia numa transação, significa que o selo foi fechado com uma determinada mensagem.


- Utilizar uma saída de transação **Bitcoin**

Isto significa que um _selo de utilização única_ é definido como um _ponto de saída_ preciso (um par TXID + número de saída). Assim que este _ponto de saída_ é gasto, o selo é fechado.

Enquanto trabalhávamos no RGB, identificámos pelo menos 4 formas diferentes de implementar estes selos na Bitcoin:


- Defina o selo através de uma chave pública e feche-o num _output_ ;
- Defina o selo com um _outpoint_ e feche-o com um _output_ ;
- Defina o selo através do valor de uma chave pública e feche-o num _input_ ;
- Definir o selo através de um _outpoint_ e fechá-lo num _input_.

| Nome do esquema | Definição do selo        | Fechamento do selo      | Requisitos adicionais                                           | Aplicação principal        | Esquemas de compromisso possíveis |
| --------------- | ------------------------ | ----------------------- | -------------------------------------------------------------- | -------------------------- | ---------------------------------- |
| PkO             | Valor da chave pública   | Saída de transação      | P2(W)PKH                                                        | Nenhuma no momento         | Keytweak, taptweak, opret         |
| TxO2            | Saída de transação       | Saída de transação      | Exige compromissos determinísticos em Bitcoin                   | RGBv1 (universal)          | Keytweak, tapret, opret           |
| PkI             | Valor da chave pública   | Entrada de transação    | Somente Taproot & não compatível com carteiras antigas          | Identidades baseadas em Bitcoin | Sigtweak, witweak               |
| TxO1            | Saída de transação       | Entrada de transação    | Somente Taproot & não compatível com carteiras antigas          | Nenhuma no momento         | Sigtweak, witweak                 |

Não entraremos em detalhes sobre cada uma dessas configurações, pois no RGB optamos por usar **um _outpoint_ como definição do selo**, e colocar o _commitment_ na saída da transação que gasta esse _outpoint_. Podemos assim introduzir os seguintes conceitos para a sequência:

- **"Definição do selo "** : Um determinado _ponto de saída_ (identificado por TXID + nº de saída) ;
- **"Fecho do selo "**: A transação que gasta este _outpoint_, na qual um _commitment_ é adicionado a uma mensagem.

Este esquema foi selecionado pela sua compatibilidade com a arquitetura RGB, mas outras configurações podem ser úteis para diferentes utilizações.

O "O2" em "TxO2" recorda-nos que tanto a definição como o encerramento se baseiam na despesa (ou criação) de um resultado de transação.

### Exemplo de diagrama TxO2

Como lembrete, a definição de um _selo de utilização única_ não requer necessariamente a publicação de uma transação na cadeia. É suficiente que Alice, por exemplo, já tenha um UTXO não gasto. Ela pode decidir: "Este _outpoint_ (já existente) é agora o meu selo". Ela regista este facto localmente (_client-side_), e até que este UTXO seja gasto, o selo é considerado aberto.

![RGB-Bitcoin](assets/en/024.webp)

No dia em que pretende fechar o selo (para assinalar um acontecimento ou para ancorar uma determinada mensagem), gasta este UTXO numa nova transação (esta transação é frequentemente designada por "transação de testemunho" (não tem qualquer relação com _segwit_, é apenas o termo que lhe damos). Esta nova transação conterá o _compromisso_ com a mensagem.

![RGB-Bitcoin](assets/en/025.webp)

Note-se que neste exemplo :


- Ninguém, exceto o Bob (ou as pessoas a quem a Alice decidir revelar a prova completa), saberá que uma determinada mensagem está escondida nesta transação;
- Todos podem ver que o _outpoint_ foi gasto, mas só o Bob tem a prova de que a mensagem está efetivamente ancorada na transação.

Para ilustrar este esquema TxO2, podemos utilizar um _selo de utilização única_ como mecanismo de revogação de uma chave PGP. Em vez de publicar um certificado de revogação nos servidores, Alice pode dizer: "Esta saída de Bitcoin, se gasta, significa que a minha chave PGP está revogada".

Alice tem, por conseguinte, um UTXO específico, ao qual está associado localmente (no lado do cliente) um determinado estado ou dados (que só ela conhece).

Alice informa Bob que se este UTXO for gasto, um determinado evento será considerado como tendo ocorrido. Do lado de fora, tudo o que vemos é uma transação de Bitcoin; mas o Bob sabe que esta despesa tem um significado oculto.

![RGB-Bitcoin](assets/en/026.webp)

Quando Alice gasta este UTXO, ela fecha o selo numa mensagem indicando a sua nova chave, ou simplesmente a revogação da antiga. Desta forma, qualquer pessoa que esteja a monitorizar a cadeia verá que o UTXO foi gasto, mas apenas aqueles com a prova completa saberão que é precisamente a revogação da chave PGP.

![RGB-Bitcoin](assets/en/027.webp)

Para que Bob ou qualquer outra pessoa envolvida possa verificar a mensagem oculta, Alice deve fornecer-lhe informações fora da cadeia.

![RGB-Bitcoin](assets/en/028.webp)

Alice deve, portanto, fornecer a Bob :


- A própria mensagem (por exemplo, a nova chave PGP) ;
- Prova criptográfica de que a mensagem esteve envolvida na transação (conhecida como _extra transaction proof_ ou _anchor_).

![RGB-Bitcoin](assets/en/029.webp)

Os terceiros não têm esta informação. Apenas vêem que foi gasto um UTXO. A confidencialidade é assim assegurada.

Para clarificar a estrutura, vamos resumir o processo em duas transacções:


- **Transação 1**: Contém a _definição do selo_, ou seja, o _ponto de saída_ que servirá de selo.

![RGB-Bitcoin](assets/en/031.webp)


- **Transação 2**: Gasta este _outpoint_. Fecha o selo e, na mesma transação, insere o _commitment_ na mensagem.

![RGB-Bitcoin](assets/en/033.webp)

Por conseguinte, designamos a segunda transação por "transação de testemunha".

Para ilustrar isto de outro ângulo, podemos representar duas camadas:


- A camada superior (blockchain, pública): todos vêem a transação e sabem que foi gasto um _outpoint_;
- A camada inferior (do lado do cliente, privada): apenas Alice (ou a pessoa em causa) sabe que esta despesa corresponde a tal e tal mensagem, através da prova criptográfica e da mensagem que guarda localmente.

![RGB-Bitcoin](assets/en/034.webp)

Mas, ao fechar o selo, coloca-se a questão de saber onde deve ser inserido o "compromisso

Na secção anterior, mencionámos brevemente como o modelo de validação do lado do cliente pode ser aplicado ao RGB e a outros sistemas. Aqui, abordamos a parte sobre **compromissos Bitcoin determinísticos** e como integrá-los em uma transação. A ideia é perceber por que razão estamos a tentar inserir um único compromisso na _transacção de testemunho_ e, acima de tudo, como garantir que não pode haver outros compromissos concorrentes não revelados.

### Locais de compromisso numa transação

Quando se dá a alguém uma prova de que uma determinada mensagem está incorporada numa transação, é necessário poder garantir que não existe outra forma de compromisso (uma segunda mensagem oculta) na mesma transação que não lhe tenha sido revelada. Para que a validação do lado do cliente se mantenha robusta, é necessário um mecanismo **determinístico** para colocar um único _compromisso_ na transação que fecha o _selo de utilização única_.

A _transacção testemunha_ gasta o famoso UTXO (ou _definição do selo_) e esta despesa corresponde ao fecho do selo. Tecnicamente, sabemos que cada ponto de saída só pode ser gasto uma vez. É precisamente isto que está na base da resistência do Bitcoin ao duplo gasto. Mas a transação de despesa pode ter vários _inputs_, vários _outputs_, ou ser composta de forma complexa (coinjoins, canais Lightning, etc.). Por conseguinte, é necessário definir claramente onde inserir o _commitment_ nesta estrutura, de forma inequívoca e uniforme.

Qualquer que seja o método (PkO, TxO2, etc.), o _compromisso_ pode ser inserido :


- Numa entrada via :
- **Sigtweak** (modifica o componente `r` da assinatura ECDSA, semelhante ao princípio "Sign-to-contract");
- **Witweak** (os dados da testemunha segregada da transação são modificados).
- **Numa Saída** via :
- **Keytweak** (a chave pública do destinatário é "ajustada" com a mensagem);
- **Opret** (a mensagem é colocada numa saída não gastável `OP_RETURN`);
- **Tapret** (ou _Taptweak_), que se baseia no taproot para inserir o compromisso na parte do script de uma chave taproot, modificando assim a chave pública de forma determinística.

![RGB-Bitcoin](assets/en/035.webp)

Eis os pormenores de cada método:

![RGB-Bitcoin](assets/en/038.webp)

***Sig tweak (sign-to-contract) :***

Um esquema anterior envolvia a exploração da parte aleatória de uma assinatura (ECDSA ou Schnorr) para incorporar o _compromisso_: esta é a técnica conhecida como "**Sign-to-contract**". Substitui-se o nonce gerado aleatoriamente por um hash que contém os dados. Desta forma, a assinatura revela implicitamente o seu compromisso, sem qualquer espaço adicional na transação. Esta abordagem tem uma série de vantagens:


- Sem sobrecarga na cadeia (utiliza o mesmo local que o nonce de base);
- Em teoria, isto pode ser bastante discreto, uma vez que o nonce é inicialmente um dado aleatório.

No entanto, surgiram dois grandes inconvenientes:


- Multisig antes do Taproot: quando tem vários signatários, tem de decidir qual a assinatura que irá efetuar o _compromisso_. As assinaturas podem ser ordenadas de forma diferente e, se um signatário se recusar, perde o controlo sobre o resultado do _compromisso_;
- MuSig e o nonce partilhado: com o Schnorr multisig (*MuSig*), a geração de nonce é um algoritmo multipartidário e torna-se praticamente impossível alterar o nonce individualmente.

Na prática, o **sig tweak** também não é muito compatível com o hardware (carteiras de hardware) e os formatos existentes (Lightning, etc.). Por isso, esta grande ideia é difícil de pôr em prática.

***Ajustamento da chave (pagamento por contrato) :***

O **ajuste da chave** retoma o conceito histórico de _pagar-para-contratar_. Pegamos na chave pública `X` e alteramo-la adicionando o valor `H(mensagem)`. Especificamente, se `X = x * G` e `h = H(mensagem)`, então a nova chave será `X' = X + h * G`. Esta chave modificada esconde o compromisso com a `mensagem`. O detentor da chave privada original pode, ao adicionar `h` à sua chave privada `x`, provar que tem a chave para gastar a saída. Em teoria, isto é elegante, porque :


- O _commitment_ é introduzido sem acrescentar quaisquer campos adicionais;
- Não armazena quaisquer dados adicionais na cadeia.

Na prática, porém, deparamo-nos com as seguintes dificuldades:


- As carteiras já não reconhecem a chave pública padrão, uma vez que foi "ajustada", pelo que não podem associar facilmente o UTXO à sua chave habitual;
- As carteiras de hardware não foram concebidas para assinar com uma chave que não seja derivada da sua derivação padrão;
- É necessário adaptar os guiões, os descritores, etc.

No contexto do RGB, esta via estava prevista até 2021, mas revelou-se demasiado complicada para funcionar com as normas e infra-estruturas actuais.

***Ajuste da testemunha :***

Uma outra ideia, que certos protocolos como _inscriptions Ordinals_ puseram em prática, consiste em colocar os dados diretamente na secção "testemunha" da transação (daí a expressão "witness tweak"). No entanto, este método :


- Torna o compromisso imediatamente visível (cola literalmente os dados em bruto na testemunha);
- Pode estar sujeito a censura (os mineiros ou nós podem recusar-se a retransmitir se for demasiado grande ou qualquer outra caraterística arbitrária);
- Consome espaço nos blocos, contrariando o objetivo de discrição e leveza do RGB.

Além disso, o testemunho foi concebido para ser podável em determinados contextos, o que pode tornar mais complicada a obtenção de provas robustas.

***Abertura-retorno (opret) :***

Muito simples no seu funcionamento, um `OP_RETURN` permite-lhe armazenar um hash ou uma mensagem num campo especial da transação. Mas é imediatamente detetável: todos vêem que há um _compromisso_ na transação, e pode ser censurado ou descartado, bem como adicionar uma saída extra. Uma vez que isto aumenta a transparência e o tamanho, é considerado menos satisfatório do ponto de vista de uma solução de validação do lado do cliente.

```txt
34-byte_Opret_Commitment =
OP_RETURN   OP_PUSHBYTE_32   <mpc::Commitment>
|_________| |______________| |_________________|
1-byte       1-byte         32 bytes
```

### Tapret

A última opção é a utilização do **Taproot** (introduzido com o BIP341) com o esquema *Tapret*. *Tapret* é uma forma mais complexa de compromisso determinístico, que traz melhorias em termos de footprint na blockchain e confidencialidade para operações de contrato. A ideia principal é esconder o compromisso na parte `Script Path Spend` de uma [transação taproot] (https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki).

![RGB-Bitcoin](assets/en/036.webp)

Antes de descrever como o compromisso é inserido numa transação taproot, vejamos a **forma exacta** do compromisso, que deve **imperativamente** corresponder a uma cadeia de 64 bytes [construída](https://github.com/BP-WG/bp-core/blob/master/dbc/src/tapret/mod.rs#L179-L196) da seguinte forma:

```txt
64-byte_Tapret_Commitment =
OP_RESERVED ...  ... .. OP_RESERVED   OP_RETURN   OP_PUSHBYTE_33  <mpc::Commitment>  <Nonce>
|___________________________________| |_________| |______________| |_______________|  |______|
OP_RESERVED x 29 times = 29 bytes      1 byte         1 byte          32 bytes        1 byte
|________________________________________________________________| |_________________________|
TAPRET_SCRIPT_COMMITMENT_PREFIX = 31 bytes                    MPC commitment + NONCE = 33 bytes
```


- Os 29 bytes `OP_RESERVED`, seguidos de `OP_RETURN` e depois de `OP_PUSHBYTE_33`, formam a parte _prefix_ de 31 bytes;
- Segue-se um _commitment_ de 32 bytes (normalmente a raiz Merkle de **MPC**), ao qual acrescentamos 1 byte de **Nonce** (um total de 33 bytes para esta segunda parte).

Assim, o método `Tapret` de 64 bytes parece um `Opret` ao qual prefixámos 29 bytes de `OP_RESERVED` e adicionámos um byte extra como Nonce.

Para manter a flexibilidade em termos de implementação, confidencialidade e escalonamento, o esquema Tapret tem em conta vários casos de utilização, consoante os requisitos:


- Incorporação única de um compromisso Tapret numa transação taproot sem uma estrutura Script Path pré-existente;
- Integração de uma autorização Tapret numa transação Taproot já equipada com um Script Path.

Vejamos mais detalhadamente cada um destes dois cenários.

#### Incorporação de Tapret sem Caminho de Script existente

Neste primeiro caso, começamos a partir de uma chave de saída taproot (*Taproot Output Key*) `Q` que contém apenas a chave pública interna `P` *(Internal Key*), sem nenhum caminho de script associado (*Script Path*) :

![RGB-Bitcoin](assets/en/047.webp)


- `P`: a chave pública interna para o _Key Path Spend_.
- `G`: o ponto gerador da curva elíptica [secp256k1](https://en.bitcoin.it/wiki/Secp256k1).
- t = tH_TWEAK(P)` é o fator de alteração, calculado através de um _tagged hash_ (e.g. `SHA-256(SHA-256(TapTweak) || P)`), de acordo com [BIP86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki#address-derivation). Isto prova que não existe nenhum script escondido.

Para incluir uma autorização **Tapret**, adicione um **Script Path Spend** com um **script único**, como se segue:

![RGB-Bitcoin](assets/en/048.webp)


- t = tH_TWEAK(P || Raiz_do_script)` passa a ser o novo fator de ajustamento, incluindo a **raiz_do_script**.
- `Raiz_do_script = tH_BRANCH(64-byte_Tapret_Commitment)` representa a raiz deste **script**, que é simplesmente um hash do tipo `SHA-256(SHA-256(TapBranch) || 64-byte_Tapret_Commitment)`.

A prova de inclusão e unicidade na árvore de raiz principal resume-se aqui à única chave pública interna `P`.

#### Integração de Tapret num Script Path pré-existente

O segundo cenário diz respeito a uma saída `Q` **taproot** mais complexa, que já contém vários scripts. Por exemplo, temos uma árvore de 3 scripts:

![RGB-Bitcoin](assets/en/049.webp)


- tH_LEAF(x)` designa a função hash normalizada marcada de um script de folha.
- a, B, C` representam guiões já incluídos na estrutura da raiz principal.

Para acrescentar o compromisso Tapret, é necessário inserir um *script não gastável* no primeiro nível da árvore, deslocando os scripts existentes um nível abaixo. Visualmente, a árvore torna-se :

![RGB-Bitcoin](assets/en/050.webp)


- tHABC` representa o hash etiquetado do agrupamento de nível superior `A, B, C`.
- tHT` representa o hash do script correspondente ao `Tapret` de 64 bytes.

De acordo com as regras da raiz principal, cada ramo/folha deve ser combinado de acordo com uma ordem de hash lexicográfica. Há dois casos possíveis:


- `tHT` > `tHABC`: o compromisso Tapret desloca-se para a direita da árvore. A prova de unicidade só precisa de `tHABC` e `P` ;
- **tHT` < `tHABC`**: o compromisso Tapret é colocado à esquerda. Para provar que não há outro compromisso Tapret à direita, `tHAB` e `tHC` devem ser revelados para demonstrar a ausência de qualquer outro script.

Exemplo visual para o primeiro caso (`tHABC < tHT`):

![RGB-Bitcoin](assets/en/051.webp)

Exemplo para o segundo caso (`tHABC > tHT`):

![RGB-Bitcoin](assets/en/052.webp)

#### Otimização com o nonce

Para melhorar a confidencialidade, podemos "minerar" (um termo mais preciso seria "fazer força bruta") o valor do `<Nonce>` (o último byte do `Tapret` de 64 bytes) na tentativa de obter um hash `tHT` tal que `tHABC < tHT`. Neste caso, o compromisso é colocado à direita, poupando o utilizador de ter de divulgar todo o conteúdo de scripts existentes para provar a unicidade do Tapret.

Em suma, o `Tapret` oferece uma forma discreta e determinística de incorporar um compromisso numa transação de raiz principal, respeitando o requisito de unicidade e inequivocidade essencial para a lógica de validação do lado do cliente e do selo de utilização única da RGB.

#### Saídas válidas

Para as transacções de compromisso RGB, o principal requisito para um esquema de compromisso Bitcoin válido é o seguinte: A transação (*transação testemunha*) deve conter comprovadamente um único compromisso. Este requisito impossibilita a construção de um histórico alternativo para dados validados do lado do cliente dentro da mesma transação. Isto significa que a mensagem em torno da qual o _single-use seal_ se fecha é única.

Para satisfazer este princípio, e independentemente do número de saídas numa transação, exigimos que **uma e apenas uma saída** possa conter um compromisso (*compromisso*). Para cada um dos esquemas utilizados (*Opret* ou *Tapret*), as únicas saídas válidas que podem conter um _compromisso_ RGB são :


- A primeira saída `OP_RETURN` (se presente) para o esquema *Opret*;
- A primeira saída taproot (se presente) para o esquema *Tapret*.

Note-se que é perfeitamente possível que uma transação contenha um único compromisso `Opret` e um único compromisso `Tapret` em duas saídas separadas. Graças à natureza determinística da Definição de Selo, estes dois compromissos correspondem então a dois dados distintos validados no lado do cliente.

### Análise e opções práticas em RGB

Quando criámos o RGB, analisámos todos estes métodos para determinar onde e como colocar um _compromisso_ numa transação de forma determinística. Definimos alguns critérios:


- Compatibilidade com diferentes cenários (por exemplo, multisig, Lightning, carteiras de hardware, etc.);
- Impacto no espaço na cadeia ;
- Dificuldade de implementação e manutenção ;
- Confidencialidade e resistência à censura.

| Método                                            | Rastro e tamanho on-chain | Tamanho do lado do cliente | Integração com carteira | Compatibilidade de hardware | Compatibilidade com Lightning | Compatibilidade com Taproot |
| ------------------------------------------------- | ------------------------ | ------------------------- | ---------------------- | -------------------------- | ---------------------------- | -------------------------- |
| Keytweak (P2C determinístico)                    | 🟢                        | 🟡                         | 🔴                      | 🟠                           | 🔴 BOLT, 🔴 Bifrost          | 🟠 Taproot, 🟢 MuSig        |
| Sigtweak (S2C determinístico)                    | 🟢                        | 🟢                         | 🟠                      | 🔴                           | 🔴 BOLT, 🔴 Bifrost          | 🟠 Taproot, 🔴 MuSig        |
| Opret (OP_RETURN)                                 | 🔴                        | 🟢                         | 🟢                      | 🟠                           | 🔴 BOLT, 🟠 Bifrost          | -                          |
| Algoritmo Tapret: nó superior esquerdo           | 🟠                        | 🔴                         | 🟠                      | 🟢                           | 🔴 BOLT, 🟢 Bifrost          | 🟢 Taproot, 🟢 MuSig        |
| Algoritmo Tapret #4: qualquer nó + prova         | 🟢                        | 🟠                         | 🟠                      | 🟢                           | 🔴 BOLT, 🟢 Bifrost          | 🟢 Taproot, 🟢 MuSig        |


| Esquema de compromisso determinístico               | Padrão         | Custo on-chain                                                                                                      | Tamanho da prova no lado do cliente                                                                             |
| --------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Keytweak (P2C determinístico)                      | LNPBP-1, 2     | 0 bytes                                                                                                           | 33 bytes (chave não ajustada)                                                                                   |
| Sigtweak (S2C determinístico)                      | WIP (LNPBP-39) | 0 bytes                                                                                                           | 0 bytes                                                                                                         |
| Opret (OP_RETURN)                                  | -              | 36 (v)bytes (TxOut adicional)                                                                                      | 0 bytes                                                                                                         |
| Algoritmo Tapret: nó superior esquerdo             | LNPBP-6        | 32 bytes no witness (8 vbytes) para qualquer multisig n-of-m e gasto via caminho de script                        | 0 bytes nos scriptless scripts taproot ~270 bytes para um único script, ~128 bytes se houver vários scripts    |
| Algoritmo Tapret #4: qualquer nó + prova de unicidade | LNPBP-6        | 32 bytes no witness (8 vbytes) para casos de script único, 0 bytes no witness na maioria dos outros casos         | 0 bytes nos scriptless scripts taproot, 65 bytes até que o Taptree tenha uma dúzia de scripts                   |


| Camada                         | Custo on-chain (bytes/vbytes) | Custo on-chain (bytes/vbytes) | Custo on-chain (bytes/vbytes) | Custo on-chain (bytes/vbytes) | Custo on-chain (bytes/vbytes) | Custo lado cliente (bytes) | Custo lado cliente (bytes) | Custo lado cliente (bytes) | Custo lado cliente (bytes) | Custo lado cliente (bytes) |
| ------------------------------ | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| **Tipo**                       | **Tapret**                   | **Tapret #4**                | **Keytweak**                 | **Sigtweak**                 | **Opret**                    | **Tapret**               | **Tapret #4**            | **Keytweak**             | **Sigtweak**             | **Opret**                |
| Single-sig                     | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | 0?                       | 0                        |
| MuSig (n-of-n)                 | 0                            | 0                            | 0                            | 0                            | 32                           | 0                        | 0                        | 32                       | ? > 0                    | 0                        |
| Multi-sig 2-of-3               | 32/8                         | 32/8 ou 0                    | 0                            | n/a                          | 32                           | ~270                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 3-of-5               | 32/8                         | 32/8 ou 0                    | 0                            | n/a                          | 32                           | ~340                     | 65                       | 32                       | n/a                      | 0                        |
| Multi-sig 2-of-3 com timeouts  | 32/8                         | 0                            | 0                            | n/a                          | 32                           | 64                       | 65                       | 32                       | n/a                      | 0                        |


| Camada                          | Custo on-chain (vbytes) | Custo on-chain (vbytes) | Custo on-chain (vbytes) | Custo no cliente (bytes) | Custo no cliente (bytes) |
| ------------------------------- | ---------------------- | ---------------------- | ---------------------- | ------------------------ | ------------------------ |
| **Tipo**                        | **Base**               | **Tapret #2**          | **Tapret #4**          | **Tapret #2**            | **Tapret #4**            |
| MuSig (n-of-n)                  | 16.5                   | 0                      | 0                      | 0                        | 0                        |
| FROST (n-of-m)                  | ?                      | 0                      | 0                      | 0                        | 0                        |
| Multi_a (n-of-m)                | 1+16n+8m               | 8                      | 8                      | 33 * m                   | 65                       |
| Ramificação MuSig / Multi_a (n-of-m) | 1+16n+8n+8xlog(n)  | 8                      | 0                      | 64                       | 65                       |
| Com timeouts (n-of-m)           | 1+16n+8n+8xlog(n)      | 8                      | 0                      | 64                       | 65                       |

| Método                                    | Privacidade e Escalabilidade | Interoperabilidade | Compatibilidade | Portabilidade | Complexidade |
| ----------------------------------------- | ------------------------- | ---------------- | ------------- | ----------- | ---------- |
| Keytweak (P2C determinístico)             | 🟢                         | 🔴               | 🔴            | 🟡          | 🟡         |
| Sigtweak (S2C determinístico)             | 🟢                         | 🔴               | 🔴            | 🟢          | 🔴         |
| Opret (OP_RETURN)                         | 🔴                         | 🟠               | 🔴            | 🟢          | 🟢         |
| Algo Tapret: Nó superior esquerdo         | 🟠                         | 🟢               | 🟢            | 🔴          | 🟠         |
| Algo Tapret #4: Qualquer nó + prova       | 🟢                         | 🟢               | 🟢            | 🟠          | 🔴         |






No decurso do estudo, tornou-se claro que nenhum dos esquemas de compromisso era totalmente compatível com a atual norma Lightning (que não emprega Taproot, _muSig2_ ou suporte adicional de _commitment_). Estão a ser desenvolvidos esforços para modificar a construção de canais do Lightning (*BiFrost*) para permitir a inserção de compromissos RGB. Esta é outra área em que precisamos de rever a estrutura da transação, as chaves e a forma como as actualizações do canal são assinadas.

A análise mostrou que, de facto, outros métodos (key tweak, sig tweak, witness tweak, etc.) apresentavam outras formas de complicação:


- Ou temos um grande volume na cadeia;
- Ou existe uma incompatibilidade radical com o código da carteira existente;
- Ou a solução não é viável em multisig não cooperativo.

Para RGB, destacam-se dois métodos em particular: ***Opret*** e ***Tapret***, ambos classificados como "Transaction Output" e compatíveis com o modo TxO2 utilizado pelo protocolo.

### Compromissos multiprotocolo - MPC

Nesta secção, vamos ver como o **RGB** lida com a agregação de vários contratos (ou, mais precisamente, os seus _transition bundles_) dentro de um único compromisso (*commitment*) registado numa transação Bitcoin através de um esquema determinístico (de acordo com `Opret` ou `Tapret`). Para isso, a ordem de Merkelização dos vários contratos ocorre numa estrutura chamada **MPC Tree** (_Multi Protocol Commitment Tree_). Nesta secção, veremos a construção desta Árvore MPC, como obter a sua raiz e como vários contratos podem partilhar a mesma transação de forma confidencial e sem ambiguidades.

O Compromisso Multiprotocolo (MPC) foi concebido para satisfazer duas necessidades:


- A construção do hash `mpc::Commitment`: este será incluído na blockchain do Bitcoin de acordo com um esquema `Opret` ou `Tapret`, e deve refletir todas as mudanças de estado a serem validadas;
- Armazenamento simultâneo de múltiplos contratos num único _commitment_, permitindo actualizações separadas em múltiplos activos ou contratos RGB a serem geridos numa única transação Bitcoin.

Em termos concretos, cada _transition bundle_ pertence a um determinado contrato. Toda esta informação é inserida numa **Árvore MPC**, cuja raiz (`mpc::Root`) é depois novamente hashada para dar o `mpc::Commitment`. É este último hash que é colocado na transação Bitcoin (_witness transaction_), de acordo com o método determinístico escolhido.

![RGB-Bitcoin](assets/en/042.webp)

#### Hash de raiz MPC

O valor efetivamente escrito na cadeia (em `Opret` ou `Tapret`) é chamado `mpc::Commitment`. Este é calculado na forma de [BIP-341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki), de acordo com a fórmula :

```txt
mpc::Commitment = SHA-256(SHA-256(mpc_tag) || SHA-256(mpc_tag) || depth || cofactor || mpc::Root )
```

em que :


- `mpc_tag` é uma etiqueta: `urn:ubideco:mpc:commitment#2024-01-31`, escolhida de acordo com as [convenções de etiquetagem RGB] (https://github.com/RGB-WG/rgb-core/blob/master/doc/Commitments.md);
- `depth` (1 byte) indica a profundidade da *árvore MPC* ;
- cofator` (16 bits, em Little Endian) é um parâmetro utilizado para promover a unicidade das posições atribuídas a cada contrato na árvore;
- `mpc::Root` é a raiz da *Árvore MPC*, calculada de acordo com o processo descrito na secção seguinte.

![RGB-Bitcoin](assets/en/044.webp)

#### Construção de árvores MPC

Para construir esta árvore MPC, temos de garantir que cada contrato corresponde a uma única posição de folha. Suponhamos que temos :


- c` contratos a incluir, indexados por `i` em `i = {0,1,...,C-1}` ;
- Para cada contrato `c_i`, temos um identificador `ContractId(i) = c_i`.

Construímos então uma árvore de largura `w` e profundidade `d` tal que `2^d = w`, com `w > C`, de modo a que cada contrato possa ser colocado numa _folha_ separada. A posição `pos(c_i)` de cada contrato na árvore é determinada por :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

em que o `cofator` é um número inteiro que aumenta a probabilidade de obter posições distintas para cada contrato. Na prática, a construção segue um processo iterativo:


- Partimos de uma profundidade mínima (`d=3` por convenção para ocultar o número exato de contratos);
- Experimentamos diferentes `cofactores` (até `w/2`, ou um máximo de 500 por razões de desempenho);
- Se não conseguirmos posicionar todos os contratos sem colisão, incrementamos `d` e começamos de novo.

O objetivo é evitar as árvores demasiado altas, reduzindo ao mínimo o risco de colisão. Note-se que o fenómeno da colisão segue uma lógica de distribuição aleatória, ligada ao [Paradoxo do Aniversário] (https://en.wikipedia.org/wiki/Birthday_problem).

#### Folhas habitadas

Depois de terem sido obtidas `C` posições distintas `pos(c_i)` para os contratos `i = {0,1,...,C-1}`, cada folha é preenchida com uma função hash (*tagged hash*):

```txt
tH_MPC_LEAF(c_i) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x10 || c_i || BundleId(c_i))
```

em que :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, é sempre escolhido de acordo com as convenções Merkle de RGB ;
- `0x10` identifica uma _folha de contrato_ ;
- `c_i` é o identificador de contrato de 32 bytes (derivado do hash Genesis);
- bundleId(c_i)` é um hash de 32 bytes que descreve o conjunto de `Transições de Estado` relativas a `c_i` (reunidas num *Transition Bundle*).

#### Folhas desabitadas

As restantes folhas, não atribuídas a um contrato (ou seja, as folhas `w - C`), são preenchidas com um valor "fictício" (_folha de entropia_):

```txt
tH_MPC_LEAF(j) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || 0x11 || entropy || j )
```

em que :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, é sempre escolhido de acordo com as convenções Merkle de RGB ;
- `0x11` representa uma _folha de entropia_ ;
- `entropia` é um valor aleatório de 64 bytes, escolhido pela pessoa que está a construir a árvore;
- `j` é a posição (em 32 bits Little Endian) desta folha na árvore.

#### Nós MPC

Depois de gerar as `w` folhas (habitadas ou não), procede-se à merkelização. Todos os nós internos são transformados em hash da seguinte forma:

```txt
tH_MPC_BRANCH(tH1 || tH2) = SHA-256(SHA-256(merkle_tag) || SHA-256(merkle_tag) || b || d || w || tH1 || tH2)
```

em que :


- `merkle_tag = urn:ubideco:merkle:node#2024-01-31`, é sempre escolhido de acordo com as convenções Merkle de RGB ;
- b` é o _factor de ramificação_ (8 bits). Na maioria das vezes, `b=0x02` porque a árvore é binária e completa;
- d` é a profundidade do nó na árvore;
- `w` é a largura da árvore (em binário Little Endian de 256 bits);
- tH1` e `tH2` são os hashes dos nós filhos (ou folhas), já calculados como mostrado acima.

Progredindo desta forma, obtemos a raiz `mpc::Root`. Podemos então calcular `mpc::Commitment` (como explicado acima) e inseri-lo na cadeia.

Para ilustrar isto, vamos imaginar um exemplo em que `C=3` (três contratos). As suas posições são supostas ser `pos(c_0)=7`, `pos(c_1)=4`, `pos(c_2)=2`. As outras folhas (posições 0, 1, 3, 5, 6) são _folhas de entropia_. O diagrama abaixo mostra a sequência de hashes para a raiz com :


- `BUNDLE_i` que representa `BundleId(c_i)` ;
- `tH_MPC_LEAF(A)` e assim por diante, que representam folhas (algumas para contratos, outras para entropia) ;
- Cada ramo `tH_MPC_BRANCH(...)` combina os hashes dos seus dois filhos.

O resultado final é o **mpc::Root**, depois o `mpc::Commitment`.

![RGB-Bitcoin](assets/en/053.webp)

#### Verificação do veio MPC

Quando um verificador deseja garantir que um contrato `c_i` (e seu `BundleId`) está incluído no `mpc::Commitment` final, ele simplesmente recebe uma prova de Merkle. Esta prova indica os nós necessários para rastrear as folhas (neste caso, a _folha de contrato_ de `c_i`) até a raiz. Não é necessário revelar toda a árvore *MPC*: isto protege a confidencialidade de outros contratos.

No exemplo, um verificador `c_2` precisa apenas de um hash intermediário (`tH_MPC_LEAF(D)`), dois `tH_MPC_BRANCH(...)`, a prova de posição `pos(c_2)` e o valor `cofator`. Ele pode então reconstruir localmente a raiz, recalcular o `mpc::Commitment` e compará-lo com o que foi escrito na transação Bitcoin (dentro de `Opret` ou `Tapret`).

![RGB-Bitcoin](assets/en/054.webp)

Este mecanismo garante que :


- O estado relativo a `c_2` está efetivamente incluído no bloco de informação agregada (lado do cliente);
- Ninguém pode construir um histórico alternativo com a mesma transação, porque o _compromisso_ na cadeia aponta para uma única raiz MPC.

#### Resumo da estrutura do CPM

O **Multi Protocol Commitment** (MPC) é o princípio que permite à RGB agregar vários contratos numa única transação Bitcoin, mantendo a unicidade dos compromissos e a confidencialidade em relação aos outros participantes. Graças à construção determinística da árvore, a cada contrato é atribuída uma posição única, e a presença de folhas "fictícias" (*Entropy Leaves*) oculta parcialmente o número total de contratos que participam na transação.

A árvore Merkle completa nunca é armazenada no cliente. Limitamo-nos a gerar um _Merkle path_ para cada contrato em causa, a transmitir ao destinatário (que pode então validar o compromisso). Em alguns casos, pode haver vários activos que passaram pelo mesmo UTXO. É possível fundir vários _Merkle paths_ num chamado _multi-protocol commitment block_, para evitar a duplicação de muitos dados.

Cada _prova de Merkle_ é, portanto, leve, tanto mais que a profundidade da árvore não ultrapassa 32 em RGB. Existe também uma noção de "bloco de Merkle", que retém mais informações (secção transversal, entropia, etc.), útil para combinar ou separar vários ramos.

É por isso que demorou tanto tempo para finalizar o RGB. Tínhamos a visão geral desde 2019: colocar tudo no lado do cliente, circulando tokens fora da cadeia. Mas para detalhes como sharding para vários contratos, a estrutura da árvore Merkle, como lidar com colisões e provas de fusão ... tudo isso exigiu iterações.

### Âncoras: uma assembleia mundial

Na sequência da construção dos nossos compromissos (`Opret` ou `Tapret`) e do nosso MPC (*Multi Protocol Commitment*), precisamos de abordar a noção de **Anchor** no protocolo RGB. Uma âncora é uma estrutura validada do lado do cliente que reúne os elementos necessários para verificar se um compromisso Bitcoin contém efetivamente informações contratuais específicas. Por outras palavras, uma âncora resume todos os dados necessários para validar os _compromissos_ descritos acima.

Uma âncora é constituída por três campos ordenados:


- `Txid`
- prova de MPC
- prova de transação extra - ETP

Cada um destes campos desempenha um papel no processo de validação, quer se trate de reconstruir a transação Bitcoin subjacente ou de provar a existência de um compromisso oculto (particularmente no caso do `Tapret`).

#### TxId

O campo `Txid` corresponde ao identificador de 32 bytes da transação Bitcoin que contém o compromisso `Opret` ou `Tapret`.

Em teoria, seria possível encontrar este `Txid` rastreando a cadeia de transições de estado que apontam para cada transação testemunha, seguindo a lógica dos selos de utilização única. No entanto, para facilitar e acelerar a verificação, este `Txid` é simplesmente incluído na Âncora, evitando assim que o validador tenha de percorrer todo o historial fora da cadeia.

#### Prova de MPC

O segundo campo, `MPC Proof`, refere-se à prova de que este contrato específico (por exemplo, `c_i`) está incluído no _Multi Protocol Commitment_. É uma combinação de :


- `pos_i`, a posição deste contrato na árvore de PPM;
- cofator", o valor definido para resolver as colisões de posições;
- o `Merkle Proof`, ou seja, o conjunto de nós e hashes utilizados para reconstruir a raiz do PPM e verificar se o identificador do contrato e o seu `Transition Bundle` estão atribuídos à raiz.

Este mecanismo foi descrito na secção anterior sobre a construção da *árvore MPC*, onde cada contrato obtém uma folha única graças ao :

```txt
pos(c_i) = c_i mod (w - cofactor)
```

Em seguida, um esquema determinístico de merkelização é utilizado para agregar todas as folhas (contratos + entropia). No final, o `MPC Proof` permite que a raiz seja reconstruída localmente e comparada com o `mpc::Commitment` incluído na cadeia.

#### Prova de transação extra - ETP

O terceiro campo, o **ETP**, depende do tipo de compromisso utilizado. Se o compromisso for do tipo `Opret`, nenhuma prova adicional é necessária. O validador inspeciona a primeira saída `OP_RETURN` da transação e encontra o `mpc::Commitment` diretamente lá.

**Se o compromisso for do tipo `Tapret`**, deve ser apresentada uma prova adicional denominada *Extra Transaction Proof - ETP*. Esta prova contém :


- A chave pública interna (`P`) da saída taproot na qual o *compromisso* está incorporado;
- Os nós parceiros do `Script Path Spend` (quando o Tapret *commitment* é inserido num script), de modo a provar a localização exacta deste script na árvore taproot:
 - Se o *compromisso* do `Tapret` estiver no ramo direito, revelamos o nó esquerdo (por exemplo, `tHABC`),
 - Se o *compromisso* `Tapret` estiver à esquerda, é necessário revelar 2 nós (por exemplo, `tHAB` e `tHC`) para provar que não existe nenhum outro *compromisso* do lado direito.
- O `nonce` pode ser utilizado para "extrair" a melhor configuração, permitindo que o *compromisso* seja colocado à direita da árvore (otimização da prova).

Esta prova adicional é essencial porque, ao contrário do `Opret`, o compromisso `Tapret` está integrado na estrutura de um script taproot, o que requer a revelação de parte da árvore taproot para validar corretamente a localização do *compromisso*.

![RGB-Bitcoin](assets/en/045.webp)

Os **Anchors** encapsulam, portanto, todas as informações necessárias para validar um compromisso Bitcoin no contexto do RGB. Elas indicam tanto a transação relevante (`Txid`) quanto a prova de posicionamento do contrato (`MPC Proof`), enquanto gerenciam a prova adicional (`ETP`) no caso do `Tapret`. Desta forma, uma Âncora protege a integridade e a unicidade do estado fora da cadeia, assegurando que a mesma transação não pode ser reinterpretada para outros dados contratuais.

### Conclusão

Neste capítulo, abordamos :


- Como aplicar o conceito de selos de utilização única na Bitcoin (em particular através de um _outpoint_);
- Os vários métodos para inserir deterministicamente um _commitment_ numa transação (Sig tweak, Key tweak, witness tweak, op_return, Taproot/Tapret) ;
- As razões pelas quais a RGB se concentra nos compromissos Tapret ;
- Gestão multi-contrato através de _multi-protocol commitments_, essencial se não quiser expor um estado inteiro ou outros contratos quando quiser provar um ponto específico;
- Também vimos o papel dos _Anchors_, que reúnem tudo (TXID da transação, prova da árvore Merkle e prova Taproot) num único pacote.

Na prática, a implementação técnica está dividida entre várias _crates_ Rust dedicadas (em _client_side_validation_, _commit-verify_, _bp_core_, etc.). As noções fundamentais estão lá:

![RGB-Bitcoin](assets/en/046.webp)

No próximo capítulo, veremos o componente puramente fora da cadeia do RGB, ou seja, a lógica do contrato. Veremos como os contratos RGB, organizados como _máquinas de estado infinito_ parcialmente replicadas, alcançam uma expressividade muito maior do que os scripts Bitcoin, preservando a confidencialidade de seus dados.

## Introdução aos contratos inteligentes e aos seus estados

<chapterId>04a9569f-3563-5382-bf53-0c7069343ba0</chapterId>

:::video id=db4ee09f-1352-4ad1-9f7a-c962df7ea9fa:::

Neste e no próximo capítulo, analisaremos a noção de **contrato inteligente** no ambiente RGB e exploraremos as diferentes formas como estes contratos podem definir e fazer evoluir o seu *estado*. Veremos porque é que a arquitetura RGB, utilizando a sequência ordenada de selos de utilização única, permite executar vários tipos de ***operações contratuais*** de forma escalável e sem passar por um registo centralizado. Veremos também o papel fundamental da ***Lógica de Negócios*** no enquadramento da evolução do estado do contrato.

### Contratos inteligentes e direitos digitais ao portador

O objetivo da RGB é fornecer uma infraestrutura para a implementação de contratos inteligentes na Bitcoin. Por "contrato inteligente" entende-se um acordo entre várias partes que é aplicado de forma automática e computacional, sem intervenção humana para fazer cumprir as cláusulas. Por outras palavras, a lei do contrato é aplicada pelo software e não por um terceiro de confiança.

Esta automatização levanta a questão da descentralização: como podemos libertar-nos de um registo centralizado (por exemplo, uma plataforma ou base de dados central) para gerir a propriedade e a execução dos contratos? A ideia original, retomada pela RGB, é regressar a um modo de propriedade conhecido como "instrumentos ao portador". Historicamente, certos títulos (obrigações, acções, etc.) eram emitidos ao portador, permitindo a qualquer pessoa que possuísse fisicamente o documento fazer valer os seus direitos.

![RGB-Bitcoin](assets/en/055.webp)

O RGB aplica este conceito ao mundo digital: os direitos (e obrigações) são encapsulados em dados que são manipulados fora da cadeia e o estado destes dados é validado pelos próprios participantes. Isto permite, a priori, um grau de confidencialidade e independência muito maior do que o oferecido por outras abordagens baseadas em registos públicos.

### Introdução ao estado RGB do contrato inteligente

Um contrato inteligente em RGB pode ser visto como uma máquina de estado, definida por :


- Um **State**, ou seja, o conjunto de informações que reflecte a configuração atual do contrato;
- Uma **Lógica Comercial** (conjunto de regras), que descreve em que condições e por quem o estado pode ser modificado.

![RGB-Bitcoin](assets/en/056.webp)

É importante compreender que estes contratos não se limitam à simples transferência de tokens. Podem incorporar uma grande variedade de aplicações: desde activos tradicionais (tokens, acções, obrigações) a mecanismos mais complexos (direitos de utilização, condições comerciais, etc.). Ao contrário de outras cadeias de blocos, em que o código do contrato é acessível e executável por todos, a abordagem da RGB compartimenta o acesso e o conhecimento do contrato pelos participantes ("***participantes do contrato***"). Existem vários papéis:


- O **emitente** ou criador do contrato, que define a génese do contrato e as suas variáveis iniciais;
- Partes com **direitos** (*propriedade*) ou outras capacidades de execução;
- **Observadores**, potencialmente limitados a ver certas informações, mas que não podem desencadear modificações.

Esta separação de papéis contribui para a resistência à censura, garantindo que apenas pessoas autorizadas possam interagir com o estado contratual. Também dá à RGB a capacidade de escalar horizontalmente: a maioria das validações ocorre fora da blockchain, e apenas as âncoras criptográficas (os *compromissos*) são inscritas no Bitcoin.

### Estado e lógica empresarial em RGB

De um ponto de vista prático, a **Lógica Comercial** do contrato assume a forma de regras e guiões, definidos naquilo a que a RGB chama um **Esquema**. O esquema codifica :


- Estrutura do Estado (que domínios são públicos? Que domínios pertencem a que entidades?
- Condições de validade (o que deve ser verificado antes de autorizar uma atualização de estado?) ;
- Autorizações (quem pode iniciar uma *Transição de Estado*? Quem pode apenas observar?).

Ao mesmo tempo, o **Estado Contratual** divide-se frequentemente em duas componentes:


- Um **Estado Global**: parte pública, potencialmente observável por todos (dependendo da configuração);
- **Estados próprios**: partes privadas, atribuídas especificamente aos proprietários através de UTXOs referenciados na lógica do contrato.

Como veremos nos próximos capítulos, qualquer atualização de status (*Contract Operation*) deve ser atrelada a um Bitcoin _commitment_ (via `Opret` ou `Tapret`) e obedecer aos scripts de *Business Logic* para ser considerada válida.

### Operações contratuais: criação e evolução do Estado

No universo RGB, uma ***Operação de Contrato*** é qualquer evento que altere o contrato de um **estado antigo** para um **estado novo**. Estas operações seguem a seguinte lógica:


- Tomamos nota do estado atual do contrato;
- Aplicamos a regra ou operação (uma ***Transição de estado***, uma ***Génese*** se for o primeiro estado, ou uma ***Extensão de estado*** se houver uma *valência* pública para ativar novamente);
- Ancoramos a modificação através de um novo _commitment_ na cadeia de blocos, fechando um _single-use seal_ e criando outro ;
- Os detentores de direitos em causa validam localmente (*client-side*) que a transição está em conformidade com o *Schema* e que a transação Bitcoin associada está registada na cadeia.

![RGB-Bitcoin](assets/en/057.webp)

O resultado final é um contrato atualizado, agora com um estado diferente. Esta transição não requer que toda a rede Bitcoin se preocupe com os detalhes, uma vez que apenas uma pequena impressão digital criptográfica (o _compromisso_) é registada na blockchain. A sequência de selos de uso único impede qualquer gasto duplo ou uso duplo do Estado.

### Cadeia de operações: da génese ao estado terminal

Para colocar isto em perspetiva, um contrato inteligente RGB começa com uma **Génese**, o primeiro estado. A partir daí, várias operações de contrato sucedem-se, formando um DAG (*Direted Acyclic Graph*) de operações:


- Cada transição é baseada num estado anterior (ou em vários, no caso de transições convergentes);
- A ordem cronológica é garantida pela inclusão de cada transição numa âncora Bitcoin, com registo de data e hora e inalterável graças ao consenso por Prova de Trabalho ;
- Quando não há mais operações em curso, é atingido um **Estado Terminal**: o estado mais recente e completo do contrato.

![RGB-Bitcoin](assets/en/012.webp)

Esta topologia DAG (em vez de uma simples cadeia linear) reflecte a possibilidade de diferentes partes do contrato evoluírem em paralelo, desde que não se contradigam. A RGB encarrega-se então de evitar quaisquer incoerências através da verificação *do lado do cliente* de cada participante envolvido.

### Resumo

Os contratos inteligentes na RGB introduzem um modelo de instrumentos digitais ao portador, descentralizados mas ancorados na Bitcoin para marcar o tempo e garantir a ordem das transacções. A execução automatizada destes contratos baseia-se em :


- Um **Estado do contrato**, que indica a configuração atual do contrato (direitos, saldos, variáveis, etc.);
- Uma **Lógica Comercial** (*Esquema*), que define quais as transições permitidas e como devem ser validadas;
- **Operações de contrato**, que actualizam este estado passo a passo, graças a compromissos ancorados em transacções Bitcoin.

No próximo capítulo, entraremos em mais detalhes sobre a representação concreta desses ***estados*** e ***transições de estado*** no nível fora da cadeia, e como eles se relacionam com os UTXOs e Selos de uso único embutidos no Bitcoin. Esta será uma oportunidade para ver como a mecânica interna do RGB, baseada na validação do lado do cliente, consegue manter a consistência dos contratos inteligentes, preservando a confidencialidade dos dados.

## Operações de contrato RGB

<chapterId>78c44e88-50c4-5ec4-befe-456c1a9f080b</chapterId>

:::video id=1caec34d-f214-425b-a1a4-0a40ae7d3e0e:::

Neste capítulo, veremos como funcionam as operações em contratos inteligentes e as transições de estado, mais uma vez no âmbito do protocolo RGB. O objetivo será também compreender como vários participantes cooperam para transferir a propriedade de um ativo.

### Transições de estado e sua mecânica

O princípio geral continua a ser o da validação do lado do cliente, em que os dados de estado são detidos pelo proprietário e validados pelo destinatário. No entanto, a especificidade da RGB reside no facto de Bob, enquanto destinatário, pedir a Alice que incorpore determinadas informações nos dados do contrato para ter um controlo real sobre o bem recebido, através de uma referência oculta a um dos seus UTXO.

Para ilustrar o processo de uma *transição de estado* (que é uma das ***operações contratuais*** fundamentais em RGB), vejamos um exemplo passo a passo de uma transferência de activos entre Alice e Bob:

**Situação inicial**

A Alice tem um ***stash RGB*** de dados validados localmente (*client-side*). Este stash refere-se a um dos seus UTXOs no Bitcoin. Isto significa que uma _definição de selo_ nestes dados aponta para um UTXO pertencente a Alice. A ideia é permitir-lhe transferir certos direitos digitais associados a um ativo (por exemplo, tokens RGB) para o Bob.

![RGB-Bitcoin](assets/en/058.webp)

**O Bob também tem UTXOs :**

O Bob, por outro lado, tem pelo menos um UTXO próprio, sem ligação direta ao da Alice. No caso de o Bob não ter um UTXO, é ainda possível fazer a transferência para ele utilizando a própria *transação de testemunho*: o resultado desta transação incluirá então o compromisso (_commitment_) e associará implicitamente a propriedade do novo contrato ao Bob.

![RGB-Bitcoin](assets/en/059.webp)

**Construção do novo imóvel (*Novo Estado*) :**

O Bob envia à Alice informação codificada sob a forma de uma ***fatura*** (entraremos em mais pormenores sobre a construção de facturas em capítulos posteriores), pedindo-lhe que crie um novo estado que esteja em conformidade com as regras do contrato. Este estado incluirá uma nova *definição de selo* apontando para um dos UTXOs do Bob. Desta forma, o Bob passa a ser proprietário dos activos definidos neste novo estado, por exemplo, uma certa quantidade de fichas RGB.

![RGB-Bitcoin](assets/en/060.webp)

**Preparação da transação modelo:**

Alice então cria uma transação Bitcoin gastando o UTXO referenciado no selo anterior (aquele que a legitimou como titular). Na saída desta transação, um *compromisso* (via `Opret` ou `Tapret`) é inserido para ancorar o novo estado RGB. Os compromissos `Opret` ou `Tapret` são derivados de uma árvore *MPC* (como visto nos capítulos anteriores), que pode agregar várias transições de diferentes contratos.

**Transmissão de *Consignação* para Bob:**

Antes de transmitir a transação, Alice envia a Bob uma ***Consignment*** contendo todos os dados necessários do lado do cliente (o seu *stash*) e a nova informação de estado a favor de Bob. Nesta altura, o Bob aplica as regras de consenso RGB:


- Valida todos os dados RGB contidos na *Consignment*, incluindo o novo estado que lhe confere a propriedade do ativo;
- Com base nos *Anchors* incluídos na *Consignment*, verifica a cronologia das transacções das testemunhas (desde a Génese até à transição mais recente) e valida os compromissos correspondentes na cadeia de blocos.

**Conclusão da transição:**

Se o Bob estiver satisfeito, pode dar a sua aprovação (por exemplo, assinando a *consignação*). A Alice pode então transmitir a transação de amostra preparada. Uma vez confirmada, esta transação encerra o selo anteriormente detido por Alice e formaliza a propriedade por Bob. A segurança anti-gastos duplos baseia-se então no mesmo mecanismo que no Bitcoin: o UTXO é gasto, provando que Alice já não o pode reutilizar.

![RGB-Bitcoin](assets/en/061.webp)

O novo estado agora faz referência ao UTXO de Bob, dando a Bob a propriedade anteriormente detida por Alice. A saída Bitcoin onde os dados RGB estão ancorados torna-se a prova irrevogável da transferência de propriedade.

Um exemplo de um DAG (*Direted Acyclic Graph*) mínimo que inclui duas operações de contrato (uma **Génese** e depois uma ***Transição de Estado***) pode ilustrar a forma como o estado RGB (*camada do lado do cliente*, a vermelho) se liga à cadeia de blocos Bitcoin (*camada de compromisso*, a laranja).

![RGB-Bitcoin](assets/en/062.webp)

Mostra que um Génesis define um selo (*definição de selo*), depois uma *transição de estado* fecha este selo para criar um novo num outro UTXO.

Neste contexto, eis algumas chamadas de atenção para a terminologia:


- Uma ***Assignment*** combina :
    - Uma ***Definição de vedação*** (que aponta para um UTXO);
- **Estados de propriedade**, ou seja, dados ligados à propriedade (por exemplo, a quantidade de tokens transferidos).
- Um **Estado Global** reúne as propriedades gerais do contrato, visíveis para todos, e garante a coerência global das evoluções.

As **Transições de Estado**, descritas no capítulo anterior, são a principal forma de operação de contrato. Referem-se a um ou mais estados anteriores (do Génesis ou de outra Transição de Estado) e actualizam-nos para um novo estado.

![RGB-Bitcoin](assets/en/063.webp)

Este diagrama mostra como, num *State Transition Bundle*, vários selos podem ser fechados numa única transação de amostra, abrindo simultaneamente novos selos. De facto, uma caraterística interessante do protocolo RGB é a sua capacidade de escalar: várias transições podem ser agregadas num Transition Bundle, sendo cada agregação associada a uma folha distinta da *árvore MPC* (um identificador de bundle único). Graças ao mecanismo *Deterministic Bitcoin Commitment* (DBC), toda a mensagem é inserida numa saída `Tapret` ou `Opret`, fechando os selos anteriores e possivelmente definindo novos selos. O `Anchor` serve de ligação direta entre o compromisso armazenado na blockchain e a estrutura de validação do lado do cliente (*client-side*).

Nos capítulos seguintes, veremos todos os componentes e processos envolvidos na construção e validação de uma Transição de Estado. A maioria destes elementos faz parte do consenso RGB, implementado na **RGB Core Library**.

### Pacote de transição

Na RGB, é possível agrupar diferentes Transições de Estado pertencentes ao mesmo contrato (ou seja, partilhando o mesmo **ContractId**, derivado do **OpId** do Genesis). No caso mais simples, como entre Alice e Bob no exemplo acima, um **Transition Bundle** contém apenas uma transição. Mas o suporte para operações multi-pagador (tais como coinjoins, aberturas de canais Lightning, etc.) significa que vários utilizadores podem combinar as suas Transições de Estado num único pacote.

Uma vez recolhidas, estas transições são ancoradas (pelo mecanismo MPC + DBC) numa única transação Bitcoin:


- Cada Transição de Estado é transformada em hash e agrupada num Pacote de Transição ;
- O pacote de transição é, por sua vez, submetido a um hash e inserido na folha da árvore MPC correspondente a este contrato (um BundleId);
- A árvore MPC é finalmente activada através de `Opret` ou `Tapret` na transação testemunha, que fecha assim os selos consumidos e define os novos selos.

Em termos técnicos, o **BundleId** inserido na folha MPC é obtido a partir de um hash marcado aplicado à serialização estrita do campo *InputMap* do pacote:

```txt
BundleId = SHA256( SHA256(bundle_tag) || SHA256(bundle_tag) || InputMap )
```

Em que `bundle_tag = urn:lnp-bp:rgb:bundle#2024-02-03` por exemplo.

O *InputMap* é uma estrutura de dados que enumera, para cada entrada `i` da transação-modelo, a referência ao *OpId* da transição de estado correspondente. Por exemplo:

```txt
InputMap =
N               input_0    OpId(input_0)    input_1    OpId(input_1)   ...    input_N-1  OpId(input_N-1)
|____________________| |_________||______________| |_________||______________|       |__________||_______________|
16-bit Little Endian   32-bit LE   32-byte hash
|_________________________| |_________________________|  ...  |___________________________|
MapElement1                MapElement2                       MapElementN
```


- `N` é o número total de entradas na transação que se referem a um `OpId`;
- opId(input_j)` é o identificador de operação de uma das transições de estado presentes no feixe.

Ao fazer referência a cada entrada apenas uma vez e de forma ordenada, evitamos que o mesmo selo seja gasto duas vezes em duas Transições de Estado simultâneas.

### Geração de estados e estado ativo

As transições de estado podem, portanto, ser utilizadas para transferir a propriedade de um ativo de uma pessoa para outra. No entanto, estas não são as únicas operações possíveis no protocolo RGB. O protocolo define três **operações contratuais** :


- **Transição de estado**;
- **Génesis**;
- Extensão do **Estado**.

Entre estas, **Génese** e **Extensão de estados** são por vezes chamadas "operações de *Geração de estados*", porque criam novos estados sem fechar imediatamente nenhum. Este é um ponto muito importante: **Genesis** e **State Extension** não implicam o fecho de um selo. Em vez disso, definem um novo selo, que deve então ser gasto por uma **Transição de estado** subsequente para ser verdadeiramente validado no histórico da blockchain.

![RGB-Bitcoin](assets/en/064.webp)

O **Estado Ativo** de um contrato é frequentemente definido como o conjunto dos últimos estados resultantes do histórico (o DAG) das transacções, começando com o Genesis e seguindo todas as âncoras na blockchain Bitcoin. Quaisquer estados antigos que já estejam obsoletos (ou seja, ligados a UTXOs gastos) já não são considerados activos, mas continuam a ser essenciais para verificar a consistência do histórico.

### Génesis

O Génesis é o ponto de partida de cada contrato RGB. É criado pelo emitente do contrato e define os parâmetros iniciais, em conformidade com o **Esquema**. No caso de um token RGB, o Genesis pode especificar, por exemplo, :


- O número de tokens originalmente criados e os seus proprietários;
- Limite máximo total de emissão possível ;
- Eventuais regras de reemissão e quais os participantes elegíveis.

Sendo a primeira transação do contrato, a Génesis não faz referência a qualquer estado anterior, nem fecha qualquer selo. No entanto, para aparecer no histórico e ser validado, o Génesis deve ser **consumido** (fechado) por uma primeira Transição de Estado (frequentemente uma transação de digitalização/auto-despesa para o próprio emissor, ou a distribuição inicial aos utilizadores).

### Extensão do Estado

As **Extensões de Estado** oferecem uma caraterística original aos contratos inteligentes. Permitem resgatar certos direitos digitais (*Valências*) previstos na definição do contrato, sem fechar imediatamente o selo. Na maioria das vezes, trata-se de :


- Emissões de fichas distribuídas;
- Mecanismos de swap de activos ;
- Reemissões condicionais (que podem incluir a destruição de outros activos, etc.).

Tecnicamente, uma Extensão de Estado faz referência a um *Redeem* (um tipo particular de entrada RGB) que corresponde a uma *Valência* definida anteriormente (por exemplo, no Génesis ou noutra Transição de Estado). Define um novo selo, disponível para a pessoa ou condição que dele beneficia. Para que este selo se torne efetivo, deve ser gasto por uma Transição de Estado posterior.

![RGB-Bitcoin](assets/en/065.webp)

Por exemplo: o Génesis cria um direito de emissão (*Valência*). Este pode ser exercido por um ator autorizado, que constrói então uma Extensão de Estado:


- Refere-se à Valência (redimir);
- Cria uma nova *atribuição* (novos dados de *Estado próprio*) que aponta para um UTXO ;
- Uma futura Transição de Estado, emitida pelo proprietário deste novo UTXO, irá efetivamente transferir ou distribuir os tokens recentemente emitidos.

### Componentes de uma operação contratual

Gostaria agora de analisar detalhadamente cada um dos elementos constituintes de uma **Operação de Contrato** em RGB. Uma operação contratual é a ação que modifica o estado de um contrato e que é validada do lado do cliente, de forma determinística, pelo destinatário legítimo. Em particular, veremos como a operação contratual tem em conta, por um lado, o **estado antigo** (*Estado antigo*) do contrato e, por outro, a definição de um **novo estado** (*Novo estado*).

```txt
+---------------------------------------------------------------------------------------------------------------------+
|  Contract Operation                                                                                                 |
|                                                                                                                     |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|  | Ffv |     | ContractId | SchemaId |      | TransitionType | ExtensionType |      | Testnet |     | AltLayers1 |  |
|  +-----+     +-----------------------+      +--------------------------------+      +---------+     +------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Metadata                                      |  | Global State                                               |  |
|  |                                               |  | +----------------------------------+                       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  | |          Structured Data            |       |  | | |  GlobalStateType  | |  Data  | |     ...     ...       |  |
|  | +-------------------------------------+       |  | | +-------------------+ +--------+ |                       |  |
|  |                                               |  | +----------------------------------+                       |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|                                                                                                                     +---------> OpId |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |         +------+
|  | Inputs                                        |  | Assignments                                                |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #1                                  | |  | | Assignment #1                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ + ---------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  | | Input #2                                  | |  | | Assignment #2                                          | |  |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
| OpId +--------------> PrevOpId | | AssignmentType | | Index | | |  | | | AssignmentType | | Owned State | | Seal Definition +--------------> Bitcoin UTXO |
+------+       |  | | +----------+ +----------------+ +-------+ | |  | | +----------------+ +-------------+ +-----------------+ | |  |       +--------------+
|  | +-------------------------------------------+ |  | +--------------------------------------------------------+ |  |
|  |                                               |  |                                                            |  |
|  |       ...           ...          ...          |  |     ...          ...             ...                       |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|  | Redeems                                       |  | Valencies                                                  |  |
|  |                                               |  |                                                            |  |
|  | +------------------------------+              |  |                                                            |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
| OpId +--------------> PrevOpId | | ValencyType | |  ...   ...   |  |  | ValencyType |  | ValencyType |         ...              |  |
+------+       |  | | +----------+ +-------------+ |              |  |  +-------------+  +-------------+                          |  |
|  | +------------------------------+              |  |                                                            |  |
|  |                                               |  |                                                            |  |
|  +-----------------------------------------------+  +------------------------------------------------------------+  |
|                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------+
```

Se observarmos o diagrama acima, podemos ver que uma operação de contrato inclui elementos referentes ao **novo estado** e outros referentes ao **antigo estado** atualizado.

Os elementos do **Estado Novo** são :


- **Atribuições**, nas quais são definidos :
 - A **definição de vedação**;
 - O **Estado de propriedade**.
- O **Estado Global**, que pode ser modificado ou enriquecido ;
- **Valências**, possivelmente definidas numa Transição de Estado ou Génese.

O **Old State** é referenciado através de :


- **Inputs**, que apontam para *Assignments* de transições de estado anteriores (não presentes no Génesis);
- **Resgates**, que se referem a Valências previamente definidas (apenas em Extensões de Estado).

Além disso, uma Operação de contrato inclui campos mais gerais específicos da operação:


- ffv` (*Versão de avanço rápido*): número inteiro de 2 bytes que indica a versão do contrato;
- transitionType` ou ExtensionType`: número inteiro de 16 bits que especifica o tipo de transição ou de extensão, de acordo com a lógica comercial;
- `ContractId`: número de 32 bytes referente ao *OpId* do contrato Génesis. Incluído em Transições e Extensões, mas não em Génesis ;
- schemaId: presente apenas no Génesis, é o hash de 32 bytes que representa a estrutura (*Schema*) do contrato;
- testnet`: Booleano que indica se você está na rede Testnet ou Mainnet. Apenas Génesis;
- altlayers1`: variável que identifica a camada alternativa (sidechain ou outra) utilizada para ancorar os dados para além da Bitcoin. Apenas presente em Genesis ;
- metadados": campo que pode armazenar informações temporárias, úteis para a validação de um contrato complexo, mas que não devem ser registadas no historial do estado final.

Finalmente, todos estes campos são condensados por um processo de hashing personalizado, para produzir uma impressão digital única, o `OpId`. Este `OpId` é então integrado no Transition Bundle, permitindo-lhe ser autenticado e validado no âmbito do protocolo.

Cada *operação de contrato* é, portanto, identificada por um hash de 32 bytes denominado `OpId`. Este hash é calculado através de um hash SHA256 de todos os elementos que compõem a operação. Por outras palavras, cada *Contract Operation* tem o seu próprio compromisso criptográfico, que inclui todos os dados necessários para verificar a autenticidade e a consistência da operação.

Um contrato RGB é então identificado por um `ContractId`, derivado do `OpId` do Genesis (uma vez que não existe uma operação anterior ao Genesis). Em termos concretos, pegamos no `OpId` do Genesis, invertemos a ordem dos bytes e aplicamos uma codificação Base58. Esta codificação torna o `ContractId` mais fácil de manusear e reconhecer.

### Métodos e regras de atualização do estado

O **Estado do contrato** representa o conjunto de informações que o protocolo RGB deve seguir para um determinado contrato. É composto por :


- **Um único Estado Global**: é a parte pública e global do contrato, visível para todos;
- Um ou mais **Estados Proprietários**: cada Estado Proprietário está associado a um selo único (e, por conseguinte, a um UTXO na Bitcoin). É feita uma distinção entre :
    - Os Estados de propriedade **pública**,
    - Os Estados de propriedade **privada**.

![RGB-Bitcoin](assets/en/066.webp)

O *Estado global* é diretamente incluído na *Operação contratual* como um bloco único. Os *Owned States* são definidos em cada *Assignment*, juntamente com a *Seal Definition*.

Uma das principais caraterísticas do RGB é a forma como o Estado Global e os Estados Próprios são modificados. Existem geralmente dois tipos de comportamento:


- **Mutável**: quando um elemento de estado é descrito como mutável, cada nova operação substitui o estado anterior por um novo estado. Os dados antigos são então considerados obsoletos;
- **Acumulando**: quando um elemento de estado é definido como acumulando, cada nova operação acrescenta novas informações ao estado anterior, sem o substituir. O resultado é uma espécie de historial acumulado.

Se, no contrato, um elemento de estado não for definido como mutável ou cumulativo, este elemento permanecerá vazio para as operações subsequentes (por outras palavras, não existem novas versões para este campo). É o esquema do contrato (ou seja, a lógica comercial codificada) que determina se um estado (global ou próprio) é mutável, cumulativo ou fixo. Uma vez definido o Génesis, estas propriedades só podem ser modificadas se o próprio contrato o permitir, por exemplo, através de uma Extensão de Estado específica.

A tabela abaixo ilustra como cada tipo de Operação de contrato pode manipular (ou não) o Estado global e o Estado próprio:

|                              | Gênese | Extensão de Estado | Transição de Estado |
| ---------------------------- | :----: | :---------------: | :---------------: |
| **Adição de Global State**   |   +    |        -        |        +        |
| **Mutação de Global State**  |  n/a   |        -        |        +        |
| **Adição de Owned State**    |   +    |        -        |        +        |
| **Mutação de Owned State**   |  n/a   |       Não       |        +        |
| **Adição de Valencies**      |   +    |        +        |        +        |


**`+`** : ação possível se o esquema do contrato o permitir.

**`-`**: a operação deve ser confirmada por uma transição de estado subsequente (a extensão de estado, por si só, não fecha o selo de utilização única).

Além disso, o âmbito temporal e os direitos de atualização de cada tipo de dados podem ser distinguidos no quadro seguinte:

|                                 | Metadados                              | Estado Global                            | Estado Possuído                                                                                         |
| ------------------------------- | ------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Escopo**                      | Definido para uma única Operação de Contrato | Definido globalmente para o contrato  | Definido para cada selo (*Assignment*)                                                               |
| **Quem pode atualizá-lo?**      | Não atualizável (dados efêmeros)      | Operação emitida por atores (emissor, etc.) | Depende do detentor legítimo que possui o selo (quem pode gastá-lo em uma transação seguinte)      |
| **Escopo Temporal**             | Apenas para a operação atual         | O estado é estabelecido ao final da operação | O estado é definido antes da operação (pela *Seal Definition* da operação anterior)                 |


### Estado global

O Estado Global é frequentemente descrito como "ninguém é dono, toda a gente sabe". Contém informações gerais sobre o contrato, que são visíveis publicamente. Por exemplo, num contrato de emissão de tokens, contém potencialmente :


- O ticker (abreviatura simbólica do token): `ticker` ;
- O nome completo do token: `name` ;
- Precisão (número de casas decimais): `precisão` ;
- Oferta inicial (e/ou limite máximo de fichas): `issuedSupply` ;
- Data de emissão: `created` ;
- Dados jurídicos ou outras informações públicas: `data`.

Este Estado Global pode ser colocado em recursos públicos (sítios Web, IPFS, Nostr, Torrent, etc.) e distribuído à comunidade. Além disso, o incentivo económico (a necessidade de manter e transferir estes tokens, etc.) leva naturalmente os utilizadores contratuais a manterem e propagarem eles próprios estes dados.

### Atribuições

A *Atribuição* é a estrutura básica para definir :


- O selo (*Definição do selo*), que aponta para um UTXO específico;
- O *Owned State*, ou seja, o bem ou os dados associados a este selo.

Uma *Assignment* pode ser vista como o análogo de uma saída de transação Bitcoin, mas com mais flexibilidade. É aqui que reside a lógica da transferência de propriedade: a *Assignment* associa um determinado tipo de bem ou direito (`AssignmentType`) a um selo. Quem possuir a chave privada do UTXO associado a este selo (ou quem puder gastar este UTXO) é considerado o proprietário deste *Owned State*.

Um dos grandes pontos fortes do RGB reside na capacidade de revelar (*revelar*) ou ocultar (*ocultar*) os campos *Definição de Selo* e *Estado de Propriedade* à vontade. Isto oferece uma poderosa combinação de confidencialidade e seletividade. Por exemplo, é possível provar que uma transição é válida sem revelar todos os dados, fornecendo a versão revelada à pessoa que tem de a validar, enquanto terceiros apenas vêem a versão oculta (um hash). Na prática, o `OpId` de uma transição é sempre calculado a partir dos dados *ocultos*.

![RGB-Bitcoin](assets/en/067.webp)

#### Definição do selo

A *Definição de Selo*, na sua forma revelada, tem quatro campos básicos: `txptr`, `vout`, `blinding` e `method` :


- **txptr**: trata-se de uma referência a um UTXO na Bitcoin :
    - No caso de um **selo Genesis**, este aponta diretamente para um UTXO existente (o que está associado ao Genesis);
    - No caso de um **Graph seal**, podemos ter :
        - Um `txid` simples, se apontar para um UTXO específico,
        - Ou um `WitnessTx`, que designa uma auto-referência: o selo aponta para a própria transação. Isto é particularmente útil quando não está disponível nenhum UTXO externo, por exemplo, em transacções de abertura de canais Lightning, ou se o destinatário não tiver nenhum UTXO.
- **vout**: o número de saída da transação indicada por `txptr`. Presente apenas para um selo Graph padrão (não para `WitnessTx`);
- **blinding**: um número aleatório de 8 bytes, para reforçar a confidencialidade e impedir tentativas de força bruta sobre a identidade do UTXO;
- **método**: indica o método de ancoragem utilizado (`Tapret` ou `Opret`).

A forma *oculta* da definição do selo é um hash SHA256 (etiquetado) da concatenação destes 4 campos, com uma etiqueta específica para RGB.

![RGB-Bitcoin](assets/en/068.webp)

#### Estados de propriedade

O segundo componente da *Atribuição* é o Estado Próprio. Ao contrário do Estado Global, este pode existir sob a forma pública ou privada:


- **Estado de propriedade pública**: toda a gente conhece os dados associados ao selo. Por exemplo, uma imagem pública;
- **Private Owned State**: os dados são ocultos, conhecidos apenas pelo proprietário (e potencialmente pelo validador, se necessário). Por exemplo, o número de tokens detidos.

A RGB define quatro tipos de estado possíveis (*StateTypes*) para um estado próprio:


- **Declarativa**: não contém dados numéricos, apenas um direito declarativo (por exemplo, o direito de voto). As formas oculta e revelada são idênticas;
- **Fungível**: representa uma quantidade fungível (como as fichas). Na forma revelada, temos `montante` e `obstáculo`. Na forma oculta, temos um único *Compromisso de Pedersen* que oculta a quantidade e a ocultação;
- **Estruturado**: armazena dados estruturados (até 64 kB). Na forma revelada, é o blob de dados. Na forma oculta, é um hash etiquetado deste blob:

```txt
SHA-256(SHA-256(tag_data) || SHA-256(tag_data) || blob)
```

Com, por exemplo :

```txt
tag_data = urn:lnp-bp:rgb:state-data#2024-02-12
```


- **Anexos**: liga um ficheiro (áudio, imagem, binário, etc.) ao Estado Proprietário, armazenando o hash do ficheiro `file_hash`, o tipo MIME `media type` e um sal criptográfico `salt`. O ficheiro em si está alojado noutro local. Na forma oculta, é um hash marcado com os três itens de dados anteriores:

```txt
SHA-256(SHA-256(tag_attachment) || SHA-256(tag_attachment) || file_hash || media_type || salt)
```

Com, por exemplo :

```txt
tag_attachment = urn:rgb:state-attach#2024-02-12
```

Para resumir, eis os 4 tipos possíveis de estado na forma pública e oculta:

```txt
State                      Concealed form                              Revealed form
+---------------------------------------------------------------------------------------------------------
+--------------------------------------------------------------------------------+
|                                                                                |
Declarative        |                              < void >                                          |
|                                                                                |
+--------------------------------------------------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------+ +----------+       |
Fungible           | | Pedersen Commitement | | <========== |         | Amount | | Blinding |       |
| +----------------------+ |             |         +--------+ +----------+       |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             |         +--------------------+        |
Structured         | |     Tagged Hash      | | <========== |         |     Data Blob      |        |
| +----------------------+ |             |         +--------------------+        |
+--------------------------+             +---------------------------------------+
+---------------------------------------------------------------------------------------------------------
+--------------------------+             +---------------------------------------+
| +----------------------+ |             | +-----------+ +------------+ +------+ |
Attachments        | |     Tagged Hash      | | <========== | | File Hash | | Media Type | | Salt | |
| +----------------------+ |             | +-----------+ +------------+ +------+ |
+--------------------------+             +---------------------------------------+
```

| **Elemento**       | **Declarativo** | **Fungível**                          | **Estruturado**                 | **Anexos**                     |
| ------------------ | -------------- | ------------------------------------ | ----------------------------- | ----------------------------- |
| **Dados**         | Nenhum         | Número inteiro de 64 bits assinado ou não assinado | Qualquer tipo de dado estrito | Qualquer arquivo              |
| **Tipo de Info**  | Nenhum         | Assinado ou não assinado              | Tipos estritos                  | Tipo MIME                      |
| **Privacidade**   | Não requerida  | Pedersen commitment                   | Hash com blinding               | Identificador de arquivo com hash |
| **Limites de Tamanho** | N/A        | 256 bytes                             | Até 64 KB                        | Até ~500 GB                    |


### Entradas

As entradas de uma *operação contratual* referem-se às *atribuições* que estão a ser gastas nesta nova operação. Uma entrada indica :


- prevOpId` : o identificador (`OpId`) da operação anterior onde se encontrava a *Atribuição*;
- assignmentType` : o tipo de *Assignment* (por exemplo, `assetOwner` para um token) ;
- `Index`: índice da *Assignment* na lista associada ao `OpId` anterior, determinado após uma ordenação lexicográfica dos selos ocultos.

As entradas nunca aparecem na Génese, uma vez que não existem Atribuições anteriores. Também não aparecem nas Extensões de Estado (porque as Extensões de Estado não fecham selos; em vez disso, redefinem novos selos com base em Valências).

Quando temos Owned States do tipo `Fungible`, a lógica de validação (através do script AluVM fornecido no Schema) verifica a consistência das somas: a soma dos tokens de entrada (*Inputs*) deve ser igual à soma dos tokens de saída (no novo *Assignments*).

### Metadados

O campo **Metadata** pode ter um máximo de 64 KiB e é utilizado para incluir dados temporários úteis para a validação, mas não integrados no estado permanente do contrato. Por exemplo, podem ser armazenadas aqui variáveis de cálculo intermédias para scripts complexos. Este espaço não se destina a ser armazenado no historial global, razão pela qual está fora do âmbito dos Estados Próprios ou do Estado Global.

### Valências

As valências são um mecanismo original do protocolo RGB. Podem ser encontradas em Génesis, Transições de Estado ou Extensões de Estado. Representam direitos numéricos que podem ser activados por uma Extensão de Estado (via *Redeems*), e depois finalizados por uma Transição subsequente. Cada Valência é identificada por um `ValencyType` (16 bits). A sua semântica (direito de reemissão, troca de fichas, direito de queima, etc.) é definida no Schema.

Em termos concretos, poderíamos imaginar um Génesis que define uma valência "direito de reemissão". Uma Extensão de Estado consumi-la-á (*Redeem*) se certas condições estiverem reunidas, a fim de introduzir uma nova quantidade de fichas. Em seguida, uma Transição de Estado que emana do detentor do selo assim criado pode transferir essas novas fichas.

### Resgata

Os resgates são o equivalente em valência das entradas para atribuições. Só aparecem nas Extensões de Estado, pois é aqui que se ativa uma Valência previamente definida. Um Resgate é composto por dois campos:


- `PrevOpId` : o `OpId` da operação em que a Valência foi especificada;
- `Tipo de valência`: o tipo de valência que se pretende ativar (cada `Tipo de valência` só pode ser utilizado uma vez por Extensão do Estado).

Exemplo: um Resgate pode corresponder a uma execução CoinSwap, dependendo do que foi codificado na Valência.

### Caraterísticas do estado RGB

Vamos agora dar uma vista de olhos a várias caraterísticas fundamentais do estado em RGB. Em particular, veremos :


- O **Strict Type System**, que impõe uma organização precisa e tipificada dos dados;
- A importância de separar a **validação** da **propriedade** ;
- O sistema de **consenso evolutivo** em RGB, que inclui as noções de *fast-forward* e *push-back*.

Como sempre, tenha em conta que tudo o que tem a ver com o estado do contrato é validado do lado do cliente, de acordo com as regras de consenso definidas no protocolo, e cuja referência criptográfica final está ancorada nas transacções Bitcoin.

#### Sistema de tipos rigoroso

A RGB utiliza um *Strict Type System* e um modo de serialização determinístico (*Strict Encoding*). Esta organização foi concebida para garantir uma perfeita reprodutibilidade e precisão na definição, tratamento e validação dos dados contratuais.

Em muitos ambientes de programação (JSON, YAML...), a estrutura de dados pode ser flexível, ou mesmo demasiado permissiva. Em RGB, por outro lado, a estrutura e os tipos de cada campo são definidos com restrições explícitas. Por exemplo :


- Cada variável tem um tipo específico (por exemplo, um número inteiro sem sinal de 8 bits `u8`, ou um número inteiro com sinal de 16 bits, etc.);
- Os tipos podem ser compostos (tipos aninhados). Isto significa que pode definir um tipo baseado noutros tipos (por exemplo, um tipo agregado contendo um campo `u8`, um campo `bool`, etc.);
- As colecções também podem ser especificadas: listas (*list*), conjuntos (*set*) ou dicionários (*map*), com uma ordem determinística de progressão;
- Cada campo é limitado (*limite inferior* / *limite superior*). Também impomos limites ao número de elementos nas colecções (contenção);
- Os dados são alinhados por bytes e a serialização é estritamente definida e não ambígua.

Graças a este protocolo de codificação rigoroso :


- A ordem dos campos é sempre a mesma, independentemente da implementação ou da linguagem de programação utilizada;
- Os hashes calculados sobre o mesmo conjunto de dados são, por conseguinte, reprodutíveis e idênticos (*compromissos* estritamente determinísticos);
- Os limites impedem um crescimento descontrolado do tamanho dos dados (por exemplo, demasiados campos);
- Esta forma de codificação facilita a verificação criptográfica, uma vez que cada participante sabe exatamente como serializar e fazer o hash dos dados.

Na prática, a estrutura (*Esquema*) e o código resultante (*Interface* e lógica associada) são compilados. É utilizada uma linguagem descritiva para definir o contrato (tipos, campos, regras) e gerar um formato binário rigoroso. Quando compilado, o resultado é :


- Um *Memory Layout* para cada campo;
- Identificadores semânticos (que indicam se a alteração do nome de uma variável tem um impacto na lógica, mesmo que a estrutura da memória permaneça a mesma).

O sistema de tipos rigoroso permite também um controlo preciso das alterações: qualquer modificação da estrutura (mesmo uma alteração do nome do campo) é detetável e pode levar a uma alteração da pegada global.

Finalmente, cada compilação produz uma impressão digital, um identificador criptográfico que atesta a versão exacta do código (dados, regras, validação). Por exemplo, um identificador do tipo :

```txt
BEiLYE-am9WhTW1-oK8cpvw4-FEMtzMrf-mKocuGZn-qWK6YF#ginger-parking-nirvana
```

Isto permite gerir actualizações de consenso ou de implementação, assegurando ao mesmo tempo uma rastreabilidade detalhada das versões utilizadas na rede.

Para evitar que o estado de um contrato RGB se torne demasiado complicado de validar do lado do cliente, uma regra de consenso impõe um tamanho máximo de `2^16` bytes (64 Kio) para qualquer dado envolvido nos cálculos de validação. Isto aplica-se a cada variável ou estrutura: não mais de 65536 bytes, ou o equivalente em números (32768 números inteiros de 16 bits, etc.). Isto também se aplica a colecções (listas, conjuntos, mapas), que não podem exceder `2^16` elementos.

Este limite garante :


- Controla o tamanho máximo dos dados a manipular durante uma transição de estado;
- Compatibilidade com a máquina virtual (*AluVM*) utilizada para executar os scripts de validação.

#### O paradigma Validação != Propriedade

Uma das principais inovações da RGB é a separação rigorosa entre dois conceitos:


- **Validação**: verificar se uma transição de estado respeita as regras do contrato (lógica comercial, historial, etc.);
- A **propriedade** (ownership, ou controlo): o facto de possuir o Bitcoin UTXO que permite gastar (ou fechar) o Selo de Utilização Única e, assim, realizar a transição de estado.

A **validação** efectua-se ao nível da pilha de software RGB (bibliotecas, protocolo *compromissos*, etc.). O seu papel consiste em garantir o respeito das regras internas do contrato (montantes, autorizações, etc.). Os observadores ou outros participantes podem igualmente validar o historial dos dados.

A **propriedade**, por outro lado, depende inteiramente da segurança do Bitcoin. Possuir a chave privada de um UTXO significa controlar a capacidade de lançar uma nova transição (fechar o selo de utilização única). Assim, mesmo que alguém possa ver ou validar os dados, não pode alterar o estado se não possuir o UTXO em causa.

![RGB-Bitcoin](assets/en/069.webp)

Esta abordagem limita as vulnerabilidades clássicas encontradas em cadeias de blocos mais complexas (em que todo o código de um contrato inteligente é público e modificável por qualquer pessoa, o que por vezes levou a piratarias). Na RGB, um atacante não pode simplesmente interagir com o estado da cadeia, pois o direito de agir sobre o estado (*propriedade*) é protegido pela camada Bitcoin.

Além disso, esse desacoplamento permite que o RGB se integre naturalmente com a Lightning Network. Os canais Lightning podem ser usados para envolver e mover ativos RGB sem envolver * compromissos * na cadeia todas as vezes. Examinaremos mais de perto essa integração do RGB no Lightning nos capítulos posteriores do curso.

#### Evolução do consenso na RGB

Para além do controlo de versões do código semântico, a RGB inclui um sistema de evolução ou atualização das regras de consenso de um contrato ao longo do tempo. Existem duas formas principais de evolução:


- **Avanço rápido**
- **Push-back** (em francês)

Um avanço rápido ocorre quando uma regra anteriormente inválida se torna válida. Por exemplo, se o contrato evoluir para permitir um novo tipo de `AssignmentType` ou um novo campo :


- Isto não pode ser comparado a um hardfork clássico da cadeia de blocos, uma vez que o RGB funciona na validação do lado do cliente e não afecta a compatibilidade geral da cadeia de blocos;
- Em termos práticos, este tipo de alteração é indicado pelo campo "Ffv" (*fast-forward version*) na operação contratual;
- Os actuais titulares não são prejudicados: o seu estatuto permanece válido;
- Os novos beneficiários (ou novos utilizadores), por outro lado, têm de atualizar o seu software (a sua carteira) para reconhecer as novas regras.

Um push-back significa que uma regra anteriormente válida se torna inválida. Trata-se, portanto, de um "endurecimento" das regras, mas não de um softfork propriamente dito:


- Os detentores existentes podem ser afectados (podem encontrar-se com activos que se tornaram obsoletos ou inválidos na nova versão);
- Podemos considerar que estamos, de facto, a criar um novo protocolo: quem adopta a nova regra afasta-se da antiga;
- O emissor pode decidir voltar a emitir activos neste novo protocolo, obrigando os utilizadores a manter duas carteiras separadas (uma para o protocolo antigo e outra para o novo), se quiserem gerir ambas as versões.

Neste capítulo sobre as operações do contrato RGB, explorámos os princípios fundamentais subjacentes a este protocolo. Como deve ter reparado, a complexidade inerente ao protocolo RGB exige a utilização de muitos termos técnicos. Por isso, no próximo capítulo, apresentarei um glossário que resumirá todos os conceitos abordados nesta primeira parte teórica, com definições de todos os termos técnicos relacionados com a RGB. Em seguida, na próxima secção, vamos analisar de forma prática a definição e a implementação de contratos RGB.

## Glossário RGB

<chapterId>545e16a4-3cca-44a3-9fd5-dbc5868abf97</chapterId>

Se precisar de voltar a este pequeno glossário de termos técnicos importantes utilizados no mundo RGB (listados por ordem alfabética), vai achá-lo útil. Este capítulo não é essencial se já tiver compreendido tudo o que foi abordado na primeira secção.

#### AluVM

A abreviatura AluVM significa "_Algorithmic logic unit Virtual Machine_", uma máquina virtual baseada em registos concebida para a validação de contratos inteligentes e a computação distribuída. É utilizada (mas não exclusivamente reservada) para a validação dos contratos RGB. Os scripts ou operações incluídos num contrato RGB podem assim ser executados no ambiente AluVM.

Para mais informações: [Sítio Web oficial do AluVM](https://www.aluvm.org/)

#### Âncora

Uma âncora representa um conjunto de dados do lado do cliente utilizados para provar a inclusão de um _compromisso_ único numa transação. No protocolo RGB, uma âncora é constituída pelos seguintes elementos:


- O identificador de transação Bitcoin (TXID) da **transação de testemunha** ;
- O **Multi Protocol Commitment (MPC)** ;
- O **Deterministic Bitcoin Commitment (DBC)**;
- A **Prova de Transação Extra (ETP)** se for utilizado o mecanismo de compromisso **Tapret** (ver a secção dedicada a este modelo).

Uma âncora serve, portanto, para estabelecer uma ligação verificável entre uma transação Bitcoin específica e os dados privados validados pelo protocolo RGB. Garante que estes dados estão efetivamente incluídos na cadeia de blocos, sem que o seu conteúdo exato seja exposto publicamente.

#### Atribuição

Na lógica da RGB, uma atribuição é o equivalente a uma saída de transação que modifica, actualiza ou cria determinadas propriedades no estado de um contrato. Uma atribuição é composta por dois elementos:


- A **Definição do selo** (referência a um UTXO específico) ;
- Um **Owned State** (dados que descrevem o estado associado a este novo proprietário).

Uma Atribuição indica, portanto, que uma parte do estado (por exemplo, um ativo) está agora atribuída a um determinado titular, identificado através de um Selo de Utilização Única ligado a um UTXO.

#### Lógica empresarial

A lógica comercial agrupa todas as regras e operações internas de um contrato, descritas pelo seu **esquema** (ou seja, a estrutura do próprio contrato). Determina a forma como o estado do contrato pode evoluir e em que condições.

#### Validação do lado do cliente

A validação do lado do cliente refere-se ao processo pelo qual cada parte (cliente) verifica um conjunto de dados trocados em privado, de acordo com as regras de um protocolo. No caso do RGB, esses dados trocados são agrupados no que é conhecido como **consignações**. Ao contrário do protocolo Bitcoin, que exige que todas as transacções sejam publicadas na cadeia, a RGB permite que apenas os _compromissos_ (ancorados na Bitcoin) sejam armazenados em público, enquanto as informações essenciais do contrato (transições, atestados, provas) permanecem fora da cadeia, partilhadas apenas entre os utilizadores em causa.

#### Compromisso

Um compromisso (no sentido criptográfico) é um objeto matemático, denotado `C`, derivado deterministicamente de uma operação sobre dados estruturados `m` (a mensagem) e um valor aleatório `r`. Escrevemos :

$$
C = \text{commit}(m, r)
$$

Este mecanismo compreende duas operações principais:


- **Compromisso**: uma função criptográfica é aplicada a uma mensagem `m` e a um número aleatório `r` para produzir `C` ;
- **Verificar**: utilizamos `C`, a mensagem `m` e o valor `r` para verificar se este compromisso está correto. A função retorna `True` ou `False`.

Um compromisso deve respeitar duas propriedades:


- **Binding**: deve ser impossível encontrar duas mensagens diferentes que produzam o mesmo `C`:

$$
m' : \, | \, : m' \neq m \quad \text{and} \quad r' : \, | \, : r' \neq r \quad
$$

Tais como :

$$
\text{verify}(m, r, C) = \text{verify}(m', r', C) \rightarrow \text{True}
$$


- **Ocultação**: o conhecimento de `C` não deve revelar o conteúdo de `m`.

No protocolo RGB, um compromisso é incluído numa transação Bitcoin para provar a existência de uma determinada informação num determinado momento, sem revelar a informação em si.

#### Consignação

Uma **Consignação** agrupa os dados trocados entre as partes, sujeitos à validação do lado do cliente em RGB. Existem duas categorias principais de consignação:


- **Consignação do contrato**: fornecida pelo *emissor* (emissor do contrato), inclui informações de inicialização como o esquema, a génese, a interface e a implementação da interface.
- **Consignação de transferência**: fornecida pelo pagador (*pagador*). Contém todo o historial das transições de estado que conduzem à consignação terminal (ou seja, o estado final recebido pelo pagador).

Estas remessas não são registadas publicamente na cadeia de blocos; são trocadas diretamente entre as partes interessadas através do canal de comunicação da sua escolha.

#### Contrato

Um contrato é um conjunto de direitos executados digitalmente entre vários actores através do protocolo RGB. Tem um estado ativo e uma lógica comercial, definida por um esquema, que especifica as operações autorizadas (transferências, extensões, etc.). O estado de um contrato, bem como as suas regras de validade, são expressos no esquema. A qualquer momento, o contrato evolui apenas de acordo com o que é permitido por esse esquema e por scripts de validação (executados, por exemplo, no AluVM).

#### Operação do contrato

Uma operação de contrato é uma atualização do estado do contrato executada de acordo com as regras do esquema. Existem as seguintes operações no RGB:


- **Transição de estado**;
- **Génesis**;
- Extensão do **Estado**.

Cada operação modifica o estado, acrescentando ou substituindo certos dados (Estado global, Estado próprio...).

#### Participante no contrato

Um participante no contrato é um ator que toma parte nas operações relacionadas com o contrato. Na RGB, é feita uma distinção entre :


- O emitente do contrato, que cria o Génesis (a origem do contrato);
- As partes contratuais, ou seja, os titulares de direitos sobre o estado do contrato;
- As partes públicas, que podem construir Extensões do Estado se o contrato oferecer Valências acessíveis ao público.

#### Direitos contratuais

Os direitos contratuais referem-se aos vários direitos que podem ser exercidos pelas pessoas envolvidas num contrato RGB. Estes direitos dividem-se em várias categorias:


- **Direitos de propriedade**, associados à propriedade de um determinado UTXO (através de uma _Definição de selo_);
- **Direitos de execução**, ou seja, a capacidade de construir uma ou mais transições (Transições de Estado) em conformidade com o Esquema ;
- **Direitos públicos**, quando o esquema autoriza certas utilizações públicas, por exemplo, a criação de uma extensão de Estado através do resgate de uma valência.

#### Estado do contrato

O Estado do contrato corresponde ao estado atual de um contrato num determinado momento. Pode ser constituído por dados públicos e privados, reflectindo o estado do contrato. A RGB distingue entre :


- O **Estado Global**, que inclui as propriedades públicas do contrato (configuradas no Genesis ou adicionadas através de actualizações autorizadas);
- **Estados de propriedade**, que pertencem a proprietários específicos, identificados pelos seus UTXOs.

#### Compromisso determinístico de Bitcoin - DBC

Deterministic Bitcoin Commitment (DBC) é o conjunto de regras utilizadas para registar de forma comprovada e única um _commitment_ numa transação Bitcoin. No protocolo RGB, existem duas formas principais de DBC:


- **Opret**
- **Tapret**

Estes mecanismos definem com precisão a forma como o _compromisso_ é codificado no resultado ou na estrutura de uma transação Bitcoin, para garantir que este compromisso é deterministicamente rastreável e verificável.

#### Gráfico Acíclico Dirigido - DAG

Um DAG (ou *Acyclic Guided Graph*) é um gráfico sem ciclos, que permite o escalonamento topológico. As cadeias de blocos, como os _shards_ dos contratos RGB, podem ser representadas por DAGs.

Para mais informações: [Direted Acyclic Graph] (https://en.wikipedia.org/wiki/Directed_acyclic_graph)

#### Gravação

A gravação é uma cadeia de dados opcional que os sucessivos proprietários de um contrato podem introduzir no historial do contrato. Esta caraterística existe, por exemplo, na interface **RGB21** e permite acrescentar informações comemorativas ou descritivas ao historial do contrato.

#### Prova de transação extra - ETP

A ETP (*Extra Transaction Proof*) é a parte da Âncora que contém os dados adicionais necessários para validar um **Tapret** *compromisso* (no contexto de _taproot_). Inclui, entre outras coisas, a chave pública interna do script taproot (_internal PubKey_) e informações específicas do _Script Path Spend_.

#### Génesis

Genesis refere-se ao conjunto de dados, regido por um Schema, que forma o estado inicial de qualquer contrato em RGB. Pode ser comparado com o conceito de _Genesis Block_ da Bitcoin, ou com o conceito de transação da Coinbase, mas aqui ao nível do _client-side_ e do token RGB.

#### Estado global

O Estado global é o conjunto das propriedades públicas contidas no Estado do contrato. É definido no Génesis e, em função das regras do contrato, pode ser atualizado por transições autorizadas. Ao contrário dos Estados Próprios, o Estado Global não pertence a uma entidade específica; está mais próximo de um registo público dentro do contrato.

#### Interface

A interface é o conjunto de instruções utilizadas para descodificar os dados binários compilados num esquema ou em operações contratuais e respectivos estados, de modo a torná-los legíveis para o utilizador ou para a sua carteira. Actua como uma camada de interpretação.

#### Implementação da interface

A Implementação da Interface é o conjunto de declarações que ligam uma **Interface** a um **Esquema**. Permite a tradução semântica realizada pela própria Interface, de modo a que os dados brutos de um contrato possam ser compreendidos pelo utilizador ou pelo software envolvido (as carteiras).

#### Fatura

Uma Fatura assume a forma de um URL codificado em [base58](https://en.wikipedia.org/wiki/Binary-to-text_encoding#Base58), que incorpora os dados necessários para a construção de uma **Transição de Estado** (pelo pagador). Por outras palavras, é uma fatura que permite à contraparte (*pagador*) criar a transição correspondente para transferir o ativo ou atualizar o estado do contrato.

#### Rede Lightning

A Lightning Network é uma rede descentralizada de canais de pagamento (ou _state channels_) no Bitcoin, composta por 2/2 carteiras multi-assinatura. Ela permite transações rápidas e de baixo custo _off-chain_, enquanto conta com a Camada 1 do Bitcoin para arbitragem (ou fechamento) quando necessário.

Para obter mais informações sobre o funcionamento do Lightning, recomendo que faça este outro curso:

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

#### Compromisso multiprotocolo - MPC

Multi Protocol Commitment (MPC) refere-se à estrutura de árvore Merkle utilizada no RGB para incluir, numa única transação Bitcoin, vários **Transition Bundles** de diferentes contratos. A ideia é agrupar vários compromissos (potencialmente correspondentes a diferentes contratos ou diferentes activos) num único ponto de ancoragem, de forma a otimizar a ocupação do espaço do bloco.

#### Estado de propriedade

Um Estado Proprietário é a parte de um Estado Contratual que está incluída numa Atribuição e associada a um determinado titular (através de um Selo de Utilização Única que aponta para um UTXO). Isto representa, por exemplo, um ativo digital ou um direito contratual específico atribuído a essa pessoa.

#### Propriedade

A propriedade refere-se à capacidade de controlar e gastar um UTXO referenciado por uma Definição de Selo. Quando um Estado de Propriedade está ligado a uma UTXO, o proprietário desta UTXO tem o direito, potencialmente, de transferir ou evoluir o Estado associado, de acordo com as regras do contrato.

#### Transação Bitcoin parcialmente assinada - PSBT

Uma PSBT (_Partially Signed Bitcoin Transaction_) é uma transação Bitcoin que ainda não está totalmente assinada. Pode ser partilhada entre várias entidades, cada uma das quais pode adicionar ou verificar certos elementos (assinaturas, scripts...), até que a transação seja considerada pronta para distribuição na cadeia.

Para mais informações: [BIP-0174] (https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki)

#### Compromisso Pedersen

Um compromisso Pedersen é um tipo de compromisso criptográfico com a propriedade de ser **homomórfico** relativamente à operação de adição. Isto significa que é possível validar a soma de dois compromissos sem revelar os valores individuais.

Formalmente, se :

$$
C1=\text{commit}(m1,r1) \quad C2=\text{commit}(m2,r2)
$$

depois :

$$
C3=C1⋅C2=\text{commit}(m1+m2, r1+r2)
$$

Esta propriedade é útil, por exemplo, para ocultar as quantidades de tokens trocadas, enquanto ainda é possível verificar os totais.

Para mais informações: [Pedersen commitment](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)

#### Resgatar

Numa Extensão de Estado, um Resgate refere-se à ação de reclamar (ou explorar) uma **Valência** previamente declarada. Como uma Valência é um direito público, o Resgate permite a um participante autorizado reivindicar uma extensão de estado de contrato específica.

#### Esquema

Um esquema em RGB é uma parte declarativa do código que descreve o conjunto de variáveis, regras e lógica comercial (*Lógica comercial*) que regem o funcionamento de um contrato. O esquema define a estrutura do estado, os tipos de transições permitidas e as condições de validação.

#### Definição do selo

A Definição do Selo é a parte de uma Cessão que associa o _compromisso_ a um UTXO propriedade do novo titular. Por outras palavras, indica onde se encontra a condição (em que UTXO) e estabelece a propriedade de um bem ou direito.

#### Fragmento

Um fragmento representa um ramo no DAG do historial das transições de estado de um contrato RGB. Por outras palavras, é um subconjunto coerente do histórico global do contrato, correspondendo, por exemplo, à sequência de transições necessárias para provar a validade de um determinado ativo desde a _Génese_.

#### Selo de utilização única

Um selo de uso único é uma promessa criptográfica de compromisso com uma mensagem ainda desconhecida, que será revelada apenas uma vez no futuro e deve ser conhecida por todos os membros de um público específico. O objetivo é evitar a criação de múltiplos compromissos concorrentes para o mesmo selo.

#### Coleção

O Stash é o conjunto de dados do lado do cliente que um utilizador armazena para um ou mais contratos RGB, para efeitos de validação (*Validação do lado do cliente*). Inclui o historial de transições, as remessas, as provas de validade, etc. Cada titular conserva apenas as partes do historial de que necessita (*shards*).

#### Extensão do Estado

Uma extensão de estado é uma operação de contrato utilizada para voltar a desencadear actualizações de estado através do resgate de **Valências** previamente declaradas. Para ser eficaz, uma Extensão de estado deve ser encerrada por uma Transição de estado (que actualiza o estado final do contrato).

#### Transição de estado

A Transição de estado é a operação que altera o estado de um contrato RGB para um novo estado. Pode modificar os dados do Estado Global e/ou do Estado Próprio. Na prática, cada transição é verificada por regras de esquema e ancorada no blockchain do Bitcoin por meio de um _commitment_.

#### Raiz da torneira

Refere-se ao formato de transação Segwit v1 da Bitcoin, introduzido por [BIP341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) e [BIP342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki). O Taproot melhora a confidencialidade e a flexibilidade dos scripts, em particular ao tornar as transacções mais compactas e mais difíceis de distinguir umas das outras.

#### Consignação terminal - Ponto final de consignação

A consignação terminal (ou _Consignment Endpoint_) é uma *consignação de transferência* que contém o estado final do contrato, incluindo a transição de estado criada a partir da fatura do destinatário (*payee*). Por conseguinte, é o ponto final de uma transferência, com os dados necessários para provar que a propriedade ou o estado foi transferido.

#### Pacote de transição

Um Transition Bundle é um conjunto de Transições de Estado RGB (pertencentes ao mesmo contrato) que estão todas envolvidas na mesma ***transação de testemunho*** Bitcoin. Isto torna possível agrupar várias actualizações ou transferências numa única âncora na cadeia.

#### UTXO

Um Bitcoin UTXO (*Unspent Transaction Output*) é definido pelo hash de uma transação e o índice de saída (*vout*). Também é por vezes chamado de _outpoint_. No protocolo RGB, a referência a um UTXO (através de uma **Seal Definition**) permite a localização do **Owned State**, ou seja, a propriedade mantida na blockchain.

#### Valência

Uma Valência é um direito público que não necessita de armazenamento estatal enquanto tal, mas que pode ser resgatado através de uma **Extensão estatal**. É, portanto, uma forma de possibilidade aberta a todos (ou a certos jogadores), declarada na lógica do contrato, para efetuar uma determinada extensão numa data posterior.

#### Transação de testemunhas

A transação testemunha é a transação Bitcoin que fecha o selo de utilização única em torno de uma mensagem que contém um compromisso multiprotocolo (MPC). Esta transação gasta um UTXO ou cria um, de modo a selar o compromisso ligado ao protocolo RGB. Funciona como uma prova na cadeia de que o estado foi definido num determinado momento.

# Programação em RGB

<partId>148a7436-d079-56d9-be08-aaa4c14c6b3a</partId>

## Implementação de contratos RGB

<chapterId>8333ea5f-51c7-5dd5-b1d7-47d491e58e51</chapterId>

:::video id=97d81b85-5a82-40a5-b111-7d96be5afd0f:::

Neste capítulo, analisaremos em pormenor a forma como um contrato RGB é definido e implementado. Veremos quais são os componentes de um contrato RGB, quais são as suas funções e como são construídos.

### Os componentes de um contrato RGB

Até agora, já falámos da **Génese**, que representa o ponto de partida de um contrato, e vimos como se enquadra na lógica de uma *Operação de Contrato* e no estado do protocolo. A definição completa de um contrato RGB, no entanto, não se limita apenas ao Génesis: envolve três componentes complementares que, em conjunto, formam o coração da implementação.

O primeiro componente é designado por **Esquema**. Trata-se de um ficheiro que descreve a estrutura fundamental e a lógica comercial (*lógica comercial*) do contrato. Especifica os tipos de dados utilizados, as regras de validação, as operações permitidas (por exemplo, emissão inicial de fichas, transferências, condições especiais, etc.), em suma, o quadro geral que determina o funcionamento do contrato.

A segunda componente é a **Interface**. Centra-se na forma como os utilizadores (e, por extensão, o software da carteira) irão interagir com este contrato. Descreve a semântica, ou seja, a representação legível dos vários campos e acções. Assim, enquanto o Esquema define o funcionamento técnico do contrato, a Interface define a forma de apresentar e expor estas funcionalidades: nomes dos métodos, visualização dos dados, etc.

O terceiro componente é a **Interface Implementation**, que complementa os dois anteriores, actuando como uma espécie de ponte entre o Esquema e a Interface. Por outras palavras, associa a semântica expressa pela Interface com as regras subjacentes definidas no Esquema. É esta implementação que vai gerir, por exemplo, a conversão entre um parâmetro introduzido na carteira e a estrutura binária imposta pelo protocolo, ou a compilação das regras de validação em linguagem de máquina.

Esta modularidade é uma caraterística interessante do RGB, pois permite que diferentes grupos de programadores trabalhem separadamente nestes aspectos (*Esquema*, *Interface*, *Implementação*), desde que sigam as regras de consenso do protocolo.

Em suma, cada contrato é composto por :


- **Genesis**, que é o estado inicial do contrato (e pode ser comparado a uma transação especial que define a primeira propriedade de um bem, um direito ou qualquer outro dado parametrizável);
- **Esquema**, que descreve a lógica comercial do contrato (tipos de dados, regras de validação, etc.);
- **Interface**, que fornece uma camada semântica tanto para as carteiras como para os utilizadores humanos, clarificando a leitura e a execução das transacções;
- **Interface de implementação**, que faz a ponte entre a lógica comercial e a apresentação, para garantir que a definição do contrato é coerente com a experiência do utilizador.

![RGB-Bitcoin](assets/en/070.webp)

É importante notar que, para que uma carteira possa gerir um ativo RGB (seja ele um token fungível ou um direito de qualquer tipo), deve ter todos estes elementos compilados: *Schema*, *Interface*, *Interface Implementation* e *Genesis*. Estes elementos são transmitidos através de uma ***remessa de contrato***, ou seja, um pacote de dados que contém todos os elementos necessários para validar o contrato do lado do cliente.

Para ajudar a clarificar estas noções, eis um quadro recapitulativo que compara os componentes de um contrato RGB com conceitos já conhecidos da programação orientada para os objectos (OOP) ou do ecossistema Ethereum:

| Componente do contrato RGB   | Significado                        | Equivalente OOP                        | Equivalente Ethereum               |
| ---------------------------- | --------------------------------- | ------------------------------------- | --------------------------------- |
| **Genesis**                  | Estado inicial do contrato       | Construtor de classe                  | Construtor de contrato            |
| **Schema**                   | Lógica de negócios do contrato   | Classe                                | Contrato                          |
| **Interface**                | Semântica do contrato            | Interface (Java) / Trait (Rust) / Protocolo (Swift) | Padrão ERC                       |
| **Interface Implementation** | Mapeamento de semântica e lógica | Impl (Rust) / Implements (Java)      | Application Binary Interface (ABI) |


A coluna da esquerda apresenta os elementos específicos do protocolo RGB. A coluna do meio mostra a função concreta de cada componente. Em seguida, na coluna "equivalente OOP", encontramos o termo equivalente em programação orientada para objectos:


- A **Génese** desempenha um papel semelhante ao de um *construtor de classe*: é aqui que o estado do contrato é inicializado;
- O **esquema** é a descrição de uma classe, ou seja, a definição das suas propriedades, métodos e lógica subjacente;
- A **Interface** corresponde a *interfaces* (Java), *traits* (Rust) ou *protocolos* (Swift): são as definições públicas de funções, eventos, campos... ;
- A **Interface Implementation** corresponde a *Impl* em Rust ou *Implements* em Java, onde especificamos como o código irá efetivamente executar os métodos anunciados na interface.

No contexto do Ethereum, a Génese está mais próxima do *construtor do contrato*, o Esquema da definição do contrato, a Interface de uma norma como a ERC-20 ou a ERC-721 e a Implementação da Interface da ABI (*Interface Binária da Aplicação*), que especifica o formato das interações com o contrato.

A vantagem da modularidade da RGB reside também no facto de diferentes partes interessadas poderem escrever, por exemplo, a sua própria implementação de interface, desde que respeitem a lógica do *esquema* e a semântica da *interface*. Assim, um emitente pode desenvolver um novo front-end (Interface) mais fácil de utilizar, sem modificar a lógica do contrato, ou, pelo contrário, pode alargar o Esquema para acrescentar funcionalidades e fornecer uma nova versão da Implementação de Interface adaptada, enquanto as implementações antigas permaneceriam válidas para a funcionalidade básica.

Quando compilamos um novo contrato, geramos um Génesis (o primeiro passo na emissão ou distribuição do ativo), bem como os seus componentes (Esquema, Interface, Implementação de Interface). Depois disso, o contrato está totalmente operacional e pode ser propagado para carteiras e utilizadores. Este método, em que o Génesis é combinado com estes três componentes, garante um elevado grau de personalização (cada contrato pode ter a sua própria lógica), descentralização (todos podem contribuir para um determinado componente) e segurança (a validação permanece estritamente definida pelo protocolo, sem depender de código arbitrário na cadeia, como é frequentemente o caso noutras cadeias de blocos).

Gostaria agora de analisar mais detalhadamente cada um destes componentes: o **Esquema**, a **Interface** e a **Implementação da Interface**.

### Esquema

Na secção anterior, vimos que, no ecossistema RGB, um contrato é composto por vários elementos: o Genesis, que estabelece o estado inicial, e vários outros componentes complementares. O objetivo do Esquema é descrever de forma declarativa toda a lógica comercial do contrato, ou seja, a estrutura dos dados, os tipos utilizados, as operações permitidas e as suas condições. Trata-se, por conseguinte, de um elemento muito importante para tornar um contrato operacional do lado do cliente, uma vez que cada participante (uma carteira, por exemplo) deve verificar se as transições de estado que recebe estão em conformidade com a lógica definida no esquema.

Um esquema pode ser comparado a uma "classe" na programação orientada para objectos (OOP). De um modo geral, serve como um modelo que define os componentes de um contrato, tais como :


- Os diferentes tipos de Estados Proprietários e Atribuições ;
- Valências, ou seja, direitos especiais que podem ser acionados (*redimidos*) para determinadas operações;
- Campos de Estado global, que descrevem propriedades globais, públicas e partilhadas do contrato;
- A estrutura Génesis (a primeira operação que ativa o contrato) ;
- As formas permitidas de Transições de Estado e Extensões de Estado, e como estas operações podem modificar o ;
- Metadados associados a cada operação, para armazenar informações temporárias ou adicionais;
- Regras que determinam a forma como os dados internos do contrato podem evoluir (por exemplo, se um campo é mutável ou cumulativo);
- Sequências de operações consideradas válidas: por exemplo, uma ordem de transições a respeitar ou um conjunto de condições lógicas a satisfazer.

![RGB-Bitcoin](assets/en/071.webp)

Quando o *emissor* de um ativo no RGB publica um contrato, fornece o Génesis e o Esquema a ele associado. Os utilizadores ou as carteiras que desejam interagir com o ativo recuperam este esquema para compreender a lógica subjacente ao contrato e para poderem verificar mais tarde se as transições em que vão participar são legítimas.

O primeiro passo, para qualquer pessoa que receba informações sobre um ativo RGB (por exemplo, uma transferência de token), é validar essas informações com base no esquema. Isto implica utilizar a compilação do esquema para :


- Verificar se os Estados Próprios, as Atribuições e outros elementos estão corretamente definidos e se respeitam os tipos impostos (o chamado *sistema de tipos estritos*);
- Verificar se as regras de transição (scripts de validação) são cumpridas. Estes guiões podem ser executados através do AluVM, que está presente no lado do cliente e é responsável pela validação da coerência da lógica comercial (montante da transferência, condições especiais, etc.).

Na prática, o esquema não é um código executável, como se pode ver nas cadeias de blocos que armazenam código na cadeia (EVM no Ethereum). Pelo contrário, o RGB separa a lógica comercial (declarativa) do código executável na cadeia de blocos (que se limita às âncoras criptográficas). Assim, o esquema determina as regras, mas a aplicação destas regras tem lugar fora da cadeia de blocos, no sítio de cada participante, de acordo com o princípio da validação do lado do cliente.

Um Schema deve ser compilado antes de poder ser utilizado por aplicações RGB. Esta compilação produz um ficheiro binário (por exemplo, `.rgb`) ou um ficheiro binário encriptado (`.rgba`). Quando a carteira importa este arquivo, ela sabe que o :


- Qual o aspeto de cada tipo de dados (números inteiros, estruturas, matrizes...) graças ao sistema de tipos estrito ;
- Como deve ser estruturado o Génesis (para compreender a inicialização dos activos);
- Os diferentes tipos de operações (transições de estado, extensões de estado) e a forma como podem modificar o estado;
- As regras de scripting (introduzidas no Schema) que o motor AluVM aplicará para verificar a validade das operações.

Como explicado nos capítulos anteriores, o *sistema de tipos estritos* dá-nos um formato de codificação estável e determinista: todas as variáveis, quer sejam Estados Próprios, Estados Globais ou Valências, são descritas com precisão (tamanho, limites inferior e superior, se necessário, tipo assinado ou não assinado, etc.). Também é possível definir estruturas aninhadas, por exemplo, para suportar casos de utilização complexos.

Opcionalmente, o esquema pode fazer referência a um `SchemaId` de raiz, o que facilita a reutilização de uma estrutura de base existente (um modelo). Desta forma, é possível evoluir um contrato ou criar variações (por exemplo, um novo tipo de token) a partir de um modelo já comprovado. Esta modularidade evita a necessidade de recriar contratos inteiros e incentiva a normalização das melhores práticas.

Outro ponto importante é que a lógica da evolução do estado (transferências, actualizações, etc.) é descrita no esquema sob a forma de scripts, regras e condições. Assim, se o autor do contrato pretender autorizar uma reemissão ou impor um mecanismo de queima (destruição de fichas), pode especificar os guiões correspondentes para o AluVM na parte de validação do esquema.

#### Diferença em relação às cadeias de blocos programáveis na cadeia

Ao contrário de sistemas como o Ethereum, em que o código do contrato inteligente (executável) é escrito na própria cadeia de blocos, o RGB armazena o contrato (a sua lógica) fora da cadeia, sob a forma de um documento declarativo compilado. Isto implica que :


- Não existe uma VM Turing-complete em execução em cada nó da rede Bitcoin. As regras de um contrato RGB não são executadas na cadeia de blocos, mas em cada utilizador que deseja validar um estado;
- Os dados do contrato não poluem a blockchain: apenas a evidência criptográfica (*compromissos*) é incorporada nas transacções Bitcoin (via `Tapret` ou `Opret`);
- O Schema pode ser atualizado ou recusado (*fast-forward*, *push-back*, etc.), sem exigir uma bifurcação na blockchain do Bitcoin. As carteiras simplesmente precisam importar o novo esquema e se adaptar às mudanças de consenso.

#### Utilização pelo emitente e pelos utilizadores

Quando um *emissor* cria um ativo (por exemplo, uma ficha fungível não inflacionista), prepara :


- Um esquema que descreve as regras de emissão, transferência, etc;
- Um Génesis adaptado a este esquema (com o número total de tokens emitidos, a identidade do proprietário inicial, eventuais valências especiais para reemissão, etc.).

Em seguida, disponibiliza o esquema compilado (um ficheiro `.rgb') aos utilizadores, para que qualquer pessoa que receba uma transferência deste token possa verificar localmente a coerência da operação. Sem este esquema, um utilizador não poderia interpretar os dados de estado ou verificar a sua conformidade com as regras do contrato.

Assim, quando uma nova carteira quiser suportar um ativo, basta integrar o esquema relevante. Este mecanismo torna possível adicionar compatibilidade a novos tipos de activos RGB, sem alterar de forma invasiva a base de software da carteira: tudo o que é necessário é importar o binário Schema e compreender a sua estrutura.

O Schema define a lógica comercial em RGB. Enumera as regras de evolução de um contrato, a estrutura dos seus dados (Estados Próprios, Estado Global, Valências) e os scripts de validação associados (executáveis pelo AluVM). Graças a este documento declarativo, a definição de um contrato (ficheiro compilado) está claramente separada da execução efectiva das regras (lado do cliente). Esta dissociação confere à RGB uma grande flexibilidade, permitindo uma vasta gama de casos de utilização (tokens fungíveis, NFT, contratos mais sofisticados), evitando ao mesmo tempo a complexidade e as falhas típicas das cadeias de bloqueio programáveis on-chain.

#### Exemplo de esquema

Vejamos um exemplo concreto de Schema para um contrato RGB. Este é um extrato em Rust do ficheiro `nia.rs` (iniciais de "*Non-Inflatable Assets*"), que define um modelo para tokens fungíveis que não podem ser reemitidos para além do seu fornecimento inicial (um ativo não inflacionário). Este tipo de token pode ser visto como o equivalente, no universo RGB, do ERC20 no Ethereum, ou seja, tokens fungíveis que respeitam certas regras básicas (por exemplo, em transferências, inicialização de fornecimento, etc.).

Antes de mergulhar no código, vale a pena recordar a estrutura geral de um esquema RGB. Existe uma série de declarações que enquadram :


- Um possível `SchemaId` que indica a utilização de outro esquema básico como modelo;
- Os **Estados Globais** e os **Estados Próprios** (com os seus tipos estritos) ;
- **Valências** (se existirem);
- As **Operações** (Génesis, Transições de Estado, Extensões de Estado) que podem fazer referência a estes estados e valências;
- O **Strict Type System** utilizado para descrever e validar dados;
- **Scripts de validação** (executados através do AluVM).

![RGB-Bitcoin](assets/en/072.webp)

O código abaixo mostra a definição completa do esquema Rust. Vamos comentá-lo parte por parte, seguindo as anotações (1) a (9) abaixo:

```rust
// ===== PART 1: Function Header and SubSchema =====
fn nia_schema() -> SubSchema {
// definitions of libraries and variables
// ===== PART 2: General Properties (ffv, subset_of, type_system) =====
Schema {
ffv: zero!(),
subset_of: None,
type_system: types.type_system(),
// ===== PART 3: Global States =====
global_types: tiny_bmap! {
GS_NOMINAL => GlobalStateSchema::once(types.get("RGBContract.DivisibleAssetSpec")),
GS_DATA => GlobalStateSchema::once(types.get("RGBContract.ContractData")),
GS_TIMESTAMP => GlobalStateSchema::once(types.get("RGBContract.Timestamp")),
GS_ISSUED_SUPPLY => GlobalStateSchema::once(types.get("RGBContract.Amount")),
},
// ===== PART 4: Owned Types =====
owned_types: tiny_bmap! {
OS_ASSET => StateSchema::Fungible(FungibleType::Unsigned64Bit),
},
// ===== PART 5: Valencies =====
valency_types: none!(),
// ===== PART 6: Genesis: Initial Operations =====
genesis: GenesisSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: tiny_bmap! {
GS_NOMINAL => Occurrences::Once,
GS_DATA => Occurrences::Once,
GS_TIMESTAMP => Occurrences::Once,
GS_ISSUED_SUPPLY => Occurrences::Once,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
},
// ===== PART 7: Extensions =====
extensions: none!(),
// ===== PART 8: Transitions: TS_TRANSFER =====
transitions: tiny_bmap! {
TS_TRANSFER => TransitionSchema {
metadata: Ty::<SemId>::UNIT.id(None),
globals: none!(),
inputs: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
assignments: tiny_bmap! {
OS_ASSET => Occurrences::OnceOrMore,
},
valencies: none!(),
}
},
// ===== PART 9: Script AluVM and Entry Points =====
script: Script::AluVM(AluScript {
libs: confined_bmap! { alu_id => alu_lib },
entry_points: confined_bmap! {
EntryPoint::ValidateGenesis => LibSite::with(FN_GENESIS_OFFSET, alu_id),
EntryPoint::ValidateTransition(TS_TRANSFER) => LibSite::with(FN_TRANSFER_OFFSET, alu_id),
},
}),
}
}
```


- (1) - **Cabeçalho da função e Subesquema**

A função `nia_schema()` devolve um `SubSchema`, indicando que este esquema pode herdar parcialmente de um esquema mais genérico. No ecossistema RGB, esta flexibilidade permite reutilizar certos elementos padrão de um esquema mestre, e depois definir regras específicas para o contrato em questão. Aqui, optámos por não permitir a herança, uma vez que `subset_of` será `None`.


- (2) - Propriedades gerais: ffv, subset_of, **type_system**

A propriedade `ffv` corresponde à versão *fast-forward* do contrato. Um valor de `zero!()` indica que estamos na versão 0 ou na versão inicial deste esquema. Se mais tarde pretender acrescentar novas funcionalidades (novo tipo de operação, etc.), pode incrementar esta versão para indicar uma alteração consensual.

A propriedade `subset_of: None` confirma a ausência de herança. O campo `type_system` refere-se ao sistema de tipos estritos já definido na biblioteca `types`. Esta linha indica que todos os dados utilizados pelo contrato utilizam a implementação de serialização estrita fornecida pela biblioteca em questão.


- (3) - Estados globais

No bloco `global_types`, declaramos quatro elementos. Utilizamos a chave, como `GS_NOMINAL` ou `GS_ISSUED_SUPPLY`, para referenciá-los posteriormente:


- `GS_NOMINAL` refere-se a um tipo `DivisibleAssetSpec`, que descreve vários campos do token criado (nome completo, ticker, precisão...);
- `GS_DATA` representa dados gerais, como uma declaração de exoneração de responsabilidade, metadados ou outro texto;
- `GS_TIMESTAMP` refere-se a uma data de emissão;
- `GS_ISSUED_SUPPLY` define o fornecimento total, ou seja, o número máximo de fichas que podem ser criadas.

A palavra-chave `once(...)` significa que cada um destes campos só pode aparecer uma vez.


- (4) - Tipos de propriedade

Em `owned_types`, declaramos `OS_ASSET`, que descreve um estado fungível. Usamos `StateSchema::Fungible(FungibleType::Unsigned64Bit)`, indicando que a quantidade de activos (tokens) é armazenada como um inteiro sem sinal de 64 bits. Assim, qualquer transação enviará uma certa quantidade de unidades deste token, que será validado de acordo com esta estrutura numérica estritamente tipificada.


- (5) - **Valências**

Indicamos `valency_types: none!()`, o que significa que não há valências neste esquema, ou seja, não há direitos especiais ou extra (como reemissão, queima condicional, etc.). Se um esquema incluísse valências, estas seriam declaradas nesta secção.


- (6) - Génesis: primeiras operações

Aqui entramos na parte que declara as Operações do Contrato. A Génese é descrita por :


- A ausência de `metadata` (campo `metadata: Ty::<SemId>::UNIT.id(None)`) ;
- Estados globais que devem estar presentes uma vez cada (`Once`);
- Uma lista de atribuições em que `OS_ASSET` deve aparecer `OnceOrMore`. Isto significa que o Genesis requer pelo menos uma atribuição `OS_ASSET` (um titular inicial);
- Sem Valência : `valências: nenhuma!()`.

É assim que limitamos a definição da emissão inicial de fichas: devemos declarar a oferta emitida (`GS_ISSUED_SUPPLY`), mais pelo menos um detentor (um Estado Proprietário do tipo `OS_ASSET`).


- (7) - Extensões

O campo `extensions: none!()` indica que não está prevista qualquer extensão de estado neste contrato. Isto significa que não existe nenhuma operação para resgatar um direito digital (Valência) ou para efetuar uma extensão de estado antes de uma Transição. Tudo é feito através da Génese ou das Transições de Estado.


- (8) - Transições: TS_TRANSFER

Em `transições`, definimos o tipo de operação `TS_TRANSFER`. Explicamos que :


- Não tem metadados;
- Não modifica o Estado Global (que já está definido no Génesis);
- Recebe um ou mais `OS_ASSETs` como entradas. Isso significa que ele deve gastar os estados próprios existentes;
- Cria (`assignments`) pelo menos um novo `OS_ASSET` (por outras palavras, o destinatário ou destinatários recebem tokens) ;
- Não gera nenhuma nova Valência.

Isto modela o comportamento de uma transferência básica, que consome tokens num UTXO, depois cria novos Estados Próprios a favor dos destinatários, e assim preserva a igualdade do montante total entre entradas e saídas.


- (9) - **Script AluVM e pontos de entrada** (em francês)

Finalmente, declaramos um script AluVM (`Script::AluVM(AluScript { ... })`). Este script contém :


- Uma ou mais bibliotecas externas (`libs`) a serem utilizadas durante a validação;
- Pontos de entrada que apontam para os offsets de funções no código AluVM, correspondentes à validação do Genesis (`ValidateGenesis`) e de cada Transição declarada (`ValidateTransition(TS_TRANSFER)`).

Este código de validação é responsável pela aplicação da lógica comercial. Por exemplo, ele verificará :


- Que o valor `GS_ISSUED_SUPPLY` não seja excedido durante o Genesis ;
- Que a soma dos `inputs` (fichas gastas) é igual à soma das `atribuições` (fichas recebidas) para `TS_TRANSFER`.

Se estas regras não forem respeitadas, a transição será considerada inválida.

Este exemplo de um esquema "*Non Inflatable Fungible Asset*" dá-nos uma melhor compreensão da estrutura de um contrato simples de token fungível RGB. Podemos ver claramente a separação entre a descrição dos dados (Global e Owned States), a declaração das operações (Genesis, Transitions, Extensions) e a implementação da validação (scripts AluVM). Graças a este modelo, um token comporta-se como um token fungível clássico, mas permanece validado do lado do cliente e não depende da infraestrutura na cadeia para executar o seu código. Apenas os compromissos criptográficos estão ancorados na cadeia de blocos Bitcoin.

### Interface

A interface é a camada destinada a tornar um contrato legível e manipulável, tanto pelos utilizadores (leitura humana) como pelas carteiras (leitura informática). A interface desempenha, portanto, um papel comparável ao de uma interface numa linguagem de programação orientada para os objectos (Java, Rust trait, etc.), na medida em que expõe e clarifica a estrutura funcional de um contrato, sem revelar necessariamente os pormenores internos da lógica comercial.

Ao contrário do Schema, que é puramente declarativo e compilado num ficheiro binário difícil de utilizar, a Interface fornece as chaves de leitura necessárias para :


- Enumerar e descrever os Estados globais e os Estados detidos incluídos no contrato;
- Aceder aos nomes e valores de cada campo, para que possam ser visualizados (por exemplo, para um token, saber o seu ticker, montante máximo, etc.);
- Interpretar e construir operações contratuais (génese, transição de estado ou extensão de estado) associando dados a nomes compreensíveis (por exemplo, efetuar uma transferência especificando claramente "montante" em vez de um identificador binário).

![RGB-Bitcoin](assets/en/073.webp)

Graças à Interface, é possível, por exemplo, escrever código numa carteira que, em vez de manipular campos, manipula diretamente etiquetas como "número de tokens", "nome do ativo", etc. Desta forma, a gestão de um contrato torna-se mais intuitiva. Desta forma, a gestão dos contratos torna-se mais intuitiva.

#### Funcionamento geral

Este método tem muitas vantagens:


- **Normalização:**

O mesmo tipo de contrato pode ser suportado por uma interface normalizada, partilhada por várias implementações de carteiras. Isto facilita a compatibilidade e a reutilização do código.


- Separação clara entre esquema e interface:

Na conceção RGB, o esquema (lógica comercial) e a interface (apresentação e manipulação) são duas entidades independentes. Os programadores que escrevem a lógica do contrato podem concentrar-se no Esquema, sem se preocuparem com a ergonomia ou a representação dos dados, enquanto outra equipa (ou a mesma equipa, mas com um calendário diferente) pode desenvolver a Interface.


- **Evolução flexível:**

A Interface pode ser modificada ou adicionada depois de o ativo ter sido emitido, sem ter de alterar o próprio contrato. Esta é uma grande diferença em relação a alguns sistemas de contratos inteligentes na cadeia, onde a Interface (muitas vezes misturada com o código de execução) é congelada na cadeia de blocos.


- Capacidade multi-interface

O mesmo contrato pode ser exposto através de diferentes interfaces adaptadas a necessidades distintas: uma interface simples para o utilizador final, outra mais avançada para o emitente que necessita de gerir operações de configuração complexas. A carteira pode então escolher qual a interface a importar, consoante a sua utilização.

![RGB-Bitcoin](assets/en/074.webp)

Na prática, quando a carteira obtém um contrato RGB (através de um arquivo `.rgb` ou `.rgba`), ela também importa a Interface associada, que também é compilada. Em tempo de execução, a carteira pode, por exemplo, :


- Navegar na lista de estados e ler os seus nomes, para apresentar o Ticker, o Montante inicial, a Data de emissão, etc. na interface do utilizador, em vez de um identificador numérico ilegível;
- Construir uma operação (como uma transferência) utilizando nomes de parâmetros explícitos: em vez de escrever `atribuições { OS_ASSET => 1 }`, pode oferecer ao utilizador um campo "Montante" num formulário e traduzir esta informação nos campos estritamente tipificados esperados pelo contrato.

#### Diferença em relação ao Ethereum e a outros sistemas

No Ethereum, a Interface (descrita através da ABI, *Application Binary Interface*) é geralmente derivada do código armazenado na cadeia (o contrato inteligente). Pode ser dispendioso ou complicado modificar uma parte específica da interface sem tocar no próprio contrato. No entanto, o RGB é baseado numa lógica totalmente fora da cadeia, com dados ancorados em *compromissos* no Bitcoin. Esta conceção torna possível modificar a interface (ou a sua implementação) sem afetar a segurança fundamental do contrato, uma vez que a validação das regras de negócio permanece no esquema e no código AluVM referenciado.

#### Compilação de interfaces

Assim como o Schema, a Interface é definida em código fonte (geralmente em Rust) e compilada em um arquivo `.rgb` ou `.rgba`. Este arquivo binário contém todas as informações necessárias para que a carteira :


- Identificar os campos por nome ;
- Ligar cada campo (e o seu valor) ao tipo de sistema estrito definido no contrato;
- Conhecer as diferentes operações permitidas e como construí-las.

Uma vez importada a interface, a carteira pode apresentar corretamente o contrato e propor interações ao utilizador.

### Interfaces normalizadas pela associação LNP/BP

No ecossistema RGB, uma Interface é utilizada para dar um significado legível e manipulável aos dados e às operações de um contrato. A Interface complementa assim o Esquema, que descreve internamente a lógica comercial (tipos estritos, scripts de validação, etc.). Nesta secção, vamos analisar as interfaces normalizadas desenvolvidas pela associação LNP/BP para tipos de contratos comuns (fichas fungíveis, NFT, etc.).

Para relembrar, a ideia é que cada Interface descreva como apresentar e manipular um contrato do lado da carteira, nomeando claramente os campos (tais como `spec`, `ticker`, `issuedSupply`...) e definindo as operações possíveis (tais como `Transfer`, `Burn`, `Rename`...). Várias Interfaces já estão operacionais, mas haverá mais e mais no futuro.

#### Algumas interfaces prontas a utilizar

**RGB20** é a interface para activos fungíveis, que pode ser comparada à norma ERC20 da Ethereum. No entanto, vai um passo mais além, oferecendo uma funcionalidade mais alargada:


- Por exemplo, a capacidade de mudar o nome do ativo (alteração do *ticker* ou do nome completo) depois de ter sido emitido, ou de ajustar a sua precisão (*stock splits*);
- Pode também descrever mecanismos para a reemissão secundária (limitada ou ilimitada) e para a queima e posterior substituição, a fim de autorizar o emitente a destruir e depois recriar activos em determinadas condições;

Por exemplo, a interface RGB20 pode ser ligada ao regime **Non-Inflatable Asset (NIA)**, que impõe um fornecimento inicial não inflacionável, ou a outros regimes mais avançados, conforme necessário.

*O **RGB21** diz respeito a contratos do tipo NFT ou, de um modo mais geral, a qualquer conteúdo digital único, como a representação de suportes digitais (imagens, música, etc.). Para além de descrever a emissão e a transferência de um único ativo, inclui caraterísticas como :*


- Suporte integrado para a inclusão direta de um ficheiro (até 16 MB) no contrato (para recuperação do lado do cliente);
- A possibilidade de o proprietário introduzir uma "*gravura*" no historial para provar a propriedade anterior de um NFT.

*o *RGB25** é uma norma híbrida que combina aspectos fungíveis e não fungíveis. Foi concebida para activos parcialmente fungíveis, como a tokenização de bens imobiliários, em que se pretende dividir uma propriedade, mantendo uma ligação a um único ativo de raiz (por outras palavras, tem partes fungíveis de uma casa, ligadas a uma casa não fungível). Tecnicamente, esta interface pode ser ligada ao esquema **Collectible Fungible Asset* (CFA)**, que tem em conta a noção de divisão enquanto rastreia o ativo original.

#### Interfaces em desenvolvimento

Estão previstas outras interfaces para utilizações mais especializadas, mas ainda não estão disponíveis:


- **RGB22**, dedicado às identidades digitais, para gerir identificadores e perfis na cadeia no ecossistema RGB;
- **RGB23**, para marcação de tempo avançada, utilizando algumas das ideias de *Opentimestamps*, mas com caraterísticas de rastreabilidade;
- **RGB24**, que visa o equivalente a um sistema de nomes de domínio descentralizado (DNS) semelhante ao *Ethereum Name Service*;
- **RGB26**, concebido para gerir DAOs (*Decentralized Autonomous Organization*) num formato mais complexo (governação, votação, etc.);
- **RGB30**, muito semelhante ao RGB20, mas com a particularidade de ter em conta a emissão inicial descentralizada e de utilizar Extensões de Estado. Seria utilizado para activos cuja reemissão é gerida por várias entidades ou sujeita a condições mais rigorosas.

É claro que, dependendo da data em que consultar este curso, estas interfaces podem já estar operacionais e acessíveis.

#### Exemplo de interface

Este trecho de código Rust mostra uma Interface [RGB20](https://github.com/RGB-WG/rgb-std/blob/master/src/interface/rgb20.rs) (ativo fungível). Este código foi retirado do arquivo `rgb20.rs` da biblioteca padrão do RGB. Vamos dar uma vista de olhos para compreender a estrutura de uma Interface e como ela faz a ponte entre, por um lado, a lógica de negócio (definida no Schema) e, por outro, as funcionalidades expostas às carteiras e aos utilizadores.

```rust
// ...
fn rgb20() -> Iface {
let types = StandardTypes::with(rgb20_stl());
Iface {
version: VerNo::V1,
name: tn!("RGB20"),
global_state: tiny_bmap! {
fname!("spec") => GlobalIface::required(types.get("RGBContract.DivisibleAssetSpec")),
fname!("data") => GlobalIface::required(types.get("RGBContract.ContractData")),
fname!("created") => GlobalIface::required(types.get("RGBContract.Timestamp")),
fname!("issuedSupply") => GlobalIface::one_or_many(types.get("RGBContract.Amount")),
fname!("burnedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
fname!("replacedSupply") => GlobalIface::none_or_many(types.get("RGBContract.Amount")),
},
assignments: tiny_bmap! {
fname!("inflationAllowance") => AssignIface::public(OwnedIface::Amount, Req::NoneOrMore),
fname!("updateRight") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnEpoch") => AssignIface::public(OwnedIface::Rights, Req::Optional),
fname!("burnRight") => AssignIface::public(OwnedIface::Rights, Req::NoneOrMore),
fname!("assetOwner") => AssignIface::private(OwnedIface::Amount, Req::NoneOrMore),
},
valencies: none!(),
genesis: GenesisIface {
metadata: Some(types.get("RGBContract.IssueMeta")),
global: tiny_bmap! {
fname!("spec") => ArgSpec::required(),
fname!("data") => ArgSpec::required(),
fname!("created") => ArgSpec::required(),
fname!("issuedSupply") => ArgSpec::required(),
},
assignments: tiny_bmap! {
fname!("assetOwner") => ArgSpec::many(),
fname!("inflationAllowance") => ArgSpec::many(),
fname!("updateRight") => ArgSpec::optional(),
fname!("burnEpoch") => ArgSpec::optional(),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_RESERVES
},
},
transitions: tiny_bmap! {
tn!("Transfer") => TransitionIface {
optional: false,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("previous") => ArgSpec::from_non_empty("assetOwner"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_non_empty("assetOwner"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Issue") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.IssueMeta")),
globals: tiny_bmap! {
fname!("issuedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_non_empty("inflationAllowance"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_many("inflationAllowance"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
ISSUE_EXCEEDS_ALLOWANCE,
INSUFFICIENT_RESERVES
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("OpenEpoch") => TransitionIface {
optional: true,
metadata: None,
globals: none!(),
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnEpoch"),
},
assignments: tiny_bmap! {
fname!("next") => ArgSpec::from_optional("burnEpoch"),
fname!("burnRight") => ArgSpec::required()
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("burnRight")),
},
tn!("Burn") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("burnedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: None,
},
tn!("Replace") => TransitionIface {
optional: true,
metadata: Some(types.get("RGBContract.BurnMeta")),
globals: tiny_bmap! {
fname!("replacedSupply") => ArgSpec::required(),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("burnRight"),
},
assignments: tiny_bmap! {
fname!("beneficiary") => ArgSpec::from_many("assetOwner"),
fname!("future") => ArgSpec::from_optional("burnRight"),
},
valencies: none!(),
errors: tiny_bset! {
NON_EQUAL_AMOUNTS,
SUPPLY_MISMATCH,
INVALID_PROOF,
INSUFFICIENT_COVERAGE
},
default_assignment: Some(fname!("beneficiary")),
},
tn!("Rename") => TransitionIface {
optional: true,
metadata: None,
globals: tiny_bmap! {
fname!("new") => ArgSpec::from_required("spec"),
},
inputs: tiny_bmap! {
fname!("used") => ArgSpec::from_required("updateRight"),
},
assignments: tiny_bmap! {
fname!("future") => ArgSpec::from_optional("updateRight"),
},
valencies: none!(),
errors: none!(),
default_assignment: Some(fname!("future")),
},
},
extensions: none!(),
error_type: types.get("RGB20.Error"),
default_operation: Some(tn!("Transfer")),
type_system: types.type_system(),
}
}
```

Nesta interface, notamos semelhanças com a estrutura do Esquema: encontramos uma declaração de Estado Global, Estados Próprios, Operações de Contrato (Génese e Transições), bem como tratamento de erros. Mas a Interface foca-se na apresentação e manipulação destes elementos para uma carteira ou qualquer outra aplicação.

A diferença em relação ao Schema reside na natureza dos tipos. Schema utiliza tipos estritos (como `FungibleType::Unsigned64Bit`) e identificadores mais técnicos. A Interface utiliza nomes de campos, macros (`fname!()`, `tn!()`), e referências a classes de argumentos (`ArgSpec`, `OwnedIface::Rights`...). O objetivo aqui é facilitar a compreensão funcional e a organização dos elementos para a carteira.

Além disso, a Interface pode introduzir funcionalidades adicionais ao Schema básico (por exemplo, gerenciamento de um direito `burnEpoch`), desde que isso permaneça consistente com a lógica final validada do lado do cliente. A secção "script" do AluVM no Schema assegurará a validade criptográfica, enquanto a Interface descreve a forma como o utilizador (ou a carteira) interage com estes estados e transições.

#### Estado global e atribuições

Na secção `global_state`, encontramos campos como `spec` (descrição do ativo), `data`, `created`, `issuedSupply`, `burnedSupply`, `replacedSupply`. Estes são campos que a carteira pode ler e apresentar. Por exemplo:


- `spec` mostrará a configuração do token;
- `issuedSupply` ou `burnedSupply` nos dão o número total de tokens emitidos ou queimados, etc.

Na secção `atribuições`, definimos várias funções ou direitos. Por exemplo:


- o `assetOwner` corresponde à posse de fichas (é o fungível *Owned State*) ;
- o `burnRight` corresponde à capacidade de queimar fichas ;
- updateRight" corresponde ao direito de mudar o nome do ativo.

A palavra-chave `public` ou `private` (por exemplo, `AssignIface::public(...)`) indica se estes estados são visíveis (`public`) ou confidenciais (`private`). Quanto a `Req::NoneOrMore`, `Req::Optional`, indicam a ocorrência esperada.

#### Génese e transições

A parte `genesis` descreve como o ativo é inicializado:


- Os campos `spec`, `data`, `created`, `issuedSupply` são obrigatórios (`ArgSpec::required()`) ;
- Atribuições como `assetOwner` podem estar presentes em múltiplas cópias (`ArgSpec::many()`), permitindo que os tokens sejam distribuídos a múltiplos detentores iniciais;
- Campos como `inflationAllowance` ou `burnEpoch` podem (ou não) ser incluídos no Genesis.

Depois, para cada Transição (`Transfer`, `Issue`, `Burn`...), a Interface define os campos que a operação espera como entrada, os campos que a operação produzirá como saída e quaisquer erros que possam ocorrer. Por exemplo:

**Transição :**


- Entradas : `previous` → deve ser um `assetOwner` ;
- Atribuições : `beneficiário` → será um novo `proprietário do ativo` ;
- Erro: `NON_EQUAL_AMOUNTS` (a carteira será assim capaz de lidar com casos em que a soma de entrada não corresponde à soma de saída).

**Transição `Issue` :**


- Opcional (`optional: true`), uma vez que a emissão adicional não é necessariamente activada;
- Entradas: `used` → uma `inflationAllowance`, ou seja, permissão para adicionar mais tokens ;
- Atribuições: `beneficiário` (novos tokens recebidos) e `futuro` (restante `inflationAllowance`) ;
- Erros possíveis: `SUPPLY_MISMATCH`, `ISSUE_EXCEEDS_ALLOWANCE`, etc.

**Transição de queima :**


- Entradas : `used` → a `burnRight` ;
- Globais : `burnedSupply` necessário ;
- Atribuições: `future` → uma possível continuação do `burnRight` se ainda não tivermos queimado tudo ;
- Erros: `SUPPLY_MISMATCH`, `INVALID_PROOF`, `INSUFFICIENT_COVERAGE`.

Assim, cada operação é descrita de forma legível para uma carteira. Isto permite apresentar uma interface gráfica onde o utilizador pode ver claramente: "Tem o direito de queimar. Quer queimar uma determinada quantia? O código sabe preencher um campo `burnedSupply` e verificar se o `burnRight` é válido.

Em suma, é importante ter em conta que uma Interface, por mais completa que seja, não define por si só a lógica interna do contrato. O coração do trabalho é feito pelo **Esquema**, que inclui tipos estritos, estrutura Genesis, transições e assim por diante. A Interface simplesmente expõe estes elementos de uma forma mais intuitiva e nomeada, para utilização numa aplicação.

Graças à modularidade do RGB, a Interface pode ser actualizada (por exemplo, adicionando uma transição `Rename`, corrigindo a exibição de um campo, etc.) sem ter que reescrever todo o contrato. Os utilizadores desta Interface podem então beneficiar imediatamente destas melhorias, assim que actualizarem o ficheiro `.rgb` ou `.rgba`.

Mas uma vez declarada uma Interface, é necessário ligá-la ao Schema correspondente. Isto é feito através da ***Interface Implementation***, que especifica como mapear cada campo nomeado (como `fname!("assetOwner")`) para o ID estrito (como `OS_ASSET`) definido no Schema. Isto garante, por exemplo, que quando uma carteira manipula um campo `burnRight`, este é o estado que, no Schema, descreve a capacidade de queimar tokens.

### Implementação da interface

Na arquitetura RGB, vimos que cada componente (esquema, interface, etc.) pode ser desenvolvido e compilado de forma independente. No entanto, existe ainda um elemento indispensável que liga estes diferentes blocos de construção: a ***Interface Implementation***. É esta que mapeia explicitamente os identificadores ou campos definidos no Esquema (do lado da lógica empresarial) para os nomes declarados na Interface (do lado da apresentação e da interação com o utilizador). Assim, quando uma carteira carrega um contrato, pode compreender exatamente que campo corresponde a quê, e como uma operação designada na Interface se relaciona com a lógica do Esquema.

Um ponto importante é que a implementação da interface não se destina necessariamente a expor todas as funcionalidades do esquema, nem todos os campos da interface: pode ser limitada a um subconjunto. Na prática, isto permite restringir ou filtrar certos aspectos do esquema. Por exemplo, pode ter um esquema com quatro tipos de operação, mas uma interface de implementação que mapeia apenas dois deles num determinado contexto. Por outro lado, se uma Interface propuser pontos finais adicionais, podemos optar por não os implementar aqui.

Eis um exemplo clássico de implementação de interface, em que associamos um esquema *Non-Inflatable Asset* (NIA) à interface RGB20:

```rust
fn nia_rgb20() -> IfaceImpl {
let schema = nia_schema();
let iface = Rgb20::iface();
IfaceImpl {
version: VerNo::V1,
schema_id: schema.schema_id(),
iface_id: iface.iface_id(),
script: none!(),
global_state: tiny_bset! {
NamedField::with(GS_NOMINAL, fname!("spec")),
NamedField::with(GS_DATA, fname!("data")),
NamedField::with(GS_TIMESTAMP, fname!("created")),
NamedField::with(GS_ISSUED_SUPPLY, fname!("issuedSupply")),
},
assignments: tiny_bset! {
NamedField::with(OS_ASSET, fname!("assetOwner")),
},
valencies: none!(),
transitions: tiny_bset! {
NamedType::with(TS_TRANSFER, tn!("Transfer")),
},
extensions: none!(),
}
}
```

Nesta interface de implementação :


- Nós referenciamos explicitamente o Esquema, através de `nia_schema()`, e a Interface, através de `Rgb20::iface()`. As chamadas `schema.schema_id()` e `iface.iface_id()` são usadas para ancorar a Implementação da Interface no lado da compilação (isto associa os identificadores criptográficos destes dois componentes);
- É estabelecido um mapeamento entre os elementos do Schema e os elementos da Interface. Por exemplo, o campo `GS_NOMINAL` no Schema é ligado à string `"spec"` no lado da Interface (`NamedField::with(GS_NOMINAL, fname!("spec"))`). Fazemos o mesmo para operações, como `TS_TRANSFER`, que ligamos a `"Transfer"` na Interface... ;
- Podemos ver que não existem valências (`valencies: none!()`) ou extensões (`extensions: none!()`), o que reflecte o facto de este contrato NIA não utilizar estas caraterísticas.

O resultado após a compilação é um ficheiro `.rgb` ou `.rgba` separado, a ser importado para a carteira, para além do Esquema e da Interface. Assim, o software sabe como ligar concretamente este contrato NIA (cuja lógica é descrita pelo seu Esquema) à Interface "RGB20" (que fornece nomes humanos e um modo de interação para tokens fungíveis), aplicando esta Implementação de Interface como uma porta de entrada entre os dois.

#### Porquê separar a implementação da interface?

A separação aumenta a flexibilidade. Um único esquema pode ter várias implementações de interface distintas, cada uma delas mapeando um conjunto diferente de funcionalidades. Além disso, a própria implementação da interface pode evoluir ou ser reescrita sem que seja necessário alterar o esquema ou a interface. Mantém-se assim o princípio de modularidade da RGB: cada componente (Esquema, Interface, Implementação de Interface) pode ser versionado e atualizado independentemente, desde que as regras de compatibilidade impostas pelo protocolo sejam respeitadas (mesmos identificadores, consistência de tipos, etc.).

Na utilização concreta, quando a carteira carrega um contrato, deve :


- Carregar o **esquema** compilado (para conhecer a estrutura da lógica comercial) ;
- Carregar **Interface** compilada (para compreender nomes e operações do lado do utilizador) ;
- Carregar a **Interface Implementation** compilada (para ligar a lógica do esquema aos nomes da interface, operação a operação, campo a campo).

Esta arquitetura modular torna possíveis cenários de utilização como :


- Limitar certas operações a certos utilizadores: oferecer uma interface de implementação parcial que apenas dê acesso a transferências básicas, sem oferecer funções de gravação ou atualização, por exemplo;
- Apresentação de alterações: conceber uma implementação de interface que renomeie um campo na interface ou o mapeie de forma diferente, sem alterar a base do contrato;
- Suporte de múltiplos esquemas: uma carteira pode carregar múltiplas implementações de interface para o mesmo tipo de interface, para lidar com diferentes esquemas (diferentes lógicas de token), desde que a sua estrutura seja compatível.

No próximo capítulo, veremos como funciona uma transferência de contrato e como são geradas as facturas RGB.

## Transferências de contratos

<chapterId>f043a307-d420-5752-b0d7-ebfd845802c0</chapterId>

:::video id=75eb5a8d-1910-4155-b5e3-81204c9a8901:::

Neste capítulo, vamos analisar o processo de transferência de um contrato no ecossistema RGB. Para o ilustrar, vamos ver a Alice e o Bob, os nossos protagonistas habituais, que desejam trocar um ativo RGB. Vamos também mostrar alguns excertos de comandos da ferramenta de linha de comando `rgb`, para ver como funciona na prática.

### Compreender a transferência de contratos RGB

Vejamos um exemplo de uma transferência entre Alice e Bob. Neste exemplo, assumimos que Bob está apenas a começar a utilizar RGB, enquanto Alice já possui activos RGB na sua carteira. Veremos como Bob configura seu ambiente, importa o contrato relevante, solicita uma transferência de Alice e, finalmente, como Alice realiza a transação real no blockchain do Bitcoin.

#### 1) Instalar a carteira RGB

Em primeiro lugar, Bob precisa de instalar uma carteira RGB, ou seja, um software compatível com o protocolo. Esta não contém, à partida, quaisquer contratos. O Bob também precisa de :


- Uma carteira Bitcoin para gerir os seus UTXOs;
- Uma ligação a um nó Bitcoin (ou a um servidor Electrum), para que possa identificar os seus UTXOs e propagar as suas transacções na rede.

Como lembrete, **Owned States** em RGB referem-se a Bitcoin UTXOs. Portanto, devemos sempre ser capazes de gerenciar e gastar UTXOs em uma transação Bitcoin que incorpora compromissos criptográficos (`Tapret` ou `Opret`) apontando para dados RGB.

#### 2) Aquisição de informações sobre os contratos

O Bob precisa então de obter os dados do contrato que lhe interessam. Estes dados podem circular através de qualquer canal: sítio Web, correio eletrónico, aplicação de mensagens... Na prática, são agrupados numa ***consignação***, ou seja, um pequeno pacote de dados contendo :


- A **Génese**, que define o estado inicial do contrato;
- O **esquema**, que descreve a lógica comercial (tipos estritos, scripts de validação, etc.);
- A **Interface**, que define a camada de apresentação (nomes de campos, operações acessíveis);
- A **Implementação de Interface**, que liga concretamente o Esquema à Interface.

![RGB-Bitcoin](assets/en/075.webp)

O tamanho total é muitas vezes da ordem de alguns kilobytes, uma vez que cada componente pesa geralmente menos de 200 bytes. Também pode ser possível transmitir esta remessa em Base58, através de canais resistentes à censura (como Nostr ou através da Lightning Network, por exemplo), ou como um código QR.

#### 3) Importação e validação de contratos

Depois de Bob ter recebido a remessa, ele importa-a para a sua carteira RGB. Isto irá então :


- Verificar se o Genesis e o Schema são válidos;
- Interface de carregamento e implementação da interface ;
- Actualize o seu acervo de dados do lado do cliente.

O Bob pode agora ver o ativo na sua carteira (mesmo que ainda não o possua) e perceber que campos estão disponíveis, que operações são possíveis... Depois, precisa de contactar a pessoa que possui o ativo a transferir. No nosso exemplo, trata-se da Alice.

O processo de descobrir quem detém um determinado ativo RGB é semelhante ao de encontrar um pagador de Bitcoin. Os pormenores desta ligação dependem da utilização (mercados, canais de conversação privados, faturação, venda de bens e serviços, salário...).

#### 4) Emissão de uma fatura

Para iniciar a transferência de um ativo RGB, o Bob deve primeiro emitir uma fatura. Esta fatura é utilizada para :


- Diz à Alice o tipo de operação a efetuar (por exemplo, uma `Transferência` a partir de uma interface RGB20);
- Fornecer à Alice a *definição de selo* do Bob (ou seja, o UTXO onde ele deseja receber o ativo);
- Especificar a quantidade de ingrediente ativo necessária (por exemplo, 100 unidades).

Bob utiliza a ferramenta `rgb` na linha de comando. Suponha que ele quer 100 unidades de um token cujo `ContractId` é conhecido, quer confiar em `Tapret`, e especifica seu UTXO (`456e3..dfe1:0`) :

```bash
bob$ rgb invoice RGB20 100 <ContractId> tapret1st:456e3..dfe1:0
```

No final deste capítulo, analisaremos mais detalhadamente a estrutura das facturas RGB.

#### 5) Transmissão de facturas

A fatura gerada (por exemplo, como URL: `rgb:2WBcas9.../RGB20/100+utxob:...`) contém todas as informações de que Alice necessita para preparar a transferência. Tal como a remessa, pode ser codificada de forma compacta (Base58 ou outro formato) e enviada através de uma aplicação de mensagens, correio eletrónico, Nostr...

![RGB-Bitcoin](assets/en/076.webp)

#### 6) Preparação da transação no lado da Alice

A Alice recebe a fatura do Bob. Na sua carteira RGB, ela tem um stash que contém o ativo a ser transferido. Para gastar o UTXO que contém o ativo, ela deve primeiro gerar uma PSBT (*Partially Signed Bitcoin Transaction*), ou seja, uma transação Bitcoin incompleta, utilizando o UTXO que possui:

```bash
alice$ wallet construct tx.psbt
```

Esta transação básica (por enquanto não assinada) será usada para ancorar o compromisso criptográfico ligado à transferência para o Bob. O UTXO de Alice será assim gasto, e na saída, colocaremos o compromisso `Tapret` ou `Opret` para Bob.

#### 7) Geração de remessa de transferência

Em seguida, Alice constrói a ***remessa de terminal*** (por vezes chamada "remessa de transferência") através do comando :

```bash
alice$ rgb transfer tx.psbt <invoice> consignment.rgb
```

Este novo ficheiro `consignment.rgb` contém :


- O historial completo das Transições de Estado necessárias para validar o ativo até ao momento presente (desde o Génesis);
- A nova Transição de Estado que transfere os activos de Alice para Bob, de acordo com a fatura que Bob emitiu;
- A transação Bitcoin incompleta (*transação testemunha*) (`tx.psbt`), que gasta o selo de utilização única de Alice, modificado para incluir o compromisso criptográfico com Bob.

Nesta fase, a transação ainda não é transmitida na rede Bitcoin. A consignação é maior do que uma consignação básica, pois inclui todo o histórico (*cadeia de prova*) para provar a legitimidade do ativo.

#### 8) Bob verifica e aceita a remessa

Alice transmite esta **remessa terminal** a Bob. O Bob irá então :


- Verificar a validade da transição de estado (garantir que o historial é coerente, que as regras contratuais são respeitadas, etc.);
- Adicione-o ao seu stock local;
- Eventualmente, gerar uma assinatura (`sig:...`) na remessa, para provar que foi examinada e aprovada (por vezes designada por "*payslip*").

```bash
bob$ rgb accept consignment.rgb
sig:DbwzvSu4BZU81jEpE9FVZ3xjcyuTKWWy2gmdnaxtACrS
```

![RGB-Bitcoin](assets/en/077.webp)

#### 9) Opção: O Bob envia a confirmação de volta à Alice (*pagamento*)

Se o Bob quiser, pode enviar esta assinatura de volta para a Alice. Isto indica:


- Que reconhece a transição como válida;
- Que ele concorda com a transmissão da transação Bitcoin.

Não é obrigatório, mas pode dar a Alice a garantia de que não haverá litígios posteriores sobre a transferência.

#### 10) Alice assina e publica a transação

Alice pode então :


- Verificar a assinatura do Bob (`rgb check <sig>`) ;
- Assinar a transação de *testemunho* que continua a ser um PSBT (`sinal de carteira`) ;
- Publicar a transação testemunha na rede Bitcoin (`-publish`).

```bash
alice$ rgb check <sig>
alice$ wallet sign —publish tx.psbt
```

![RGB-Bitcoin](assets/en/078.webp)

Uma vez confirmada, esta transação marca a conclusão da transferência. O Bob torna-se o novo proprietário do ativo: tem agora um Estado de Propriedade que aponta para o UTXO que controla, comprovado pela presença do compromisso na transação.

Para resumir, eis o processo de transferência completo:

![RGB-Bitcoin](assets/en/079.webp)

### Vantagens das transferências RGB


- **Confidencialidade**:

Apenas Alice e Bob têm acesso a todos os dados de transição de estado. Eles trocam essas informações fora da blockchain, por meio de consignações. Os compromissos criptográficos na transação Bitcoin não revelam o tipo de ativo ou o montante, o que garante uma confidencialidade muito maior do que outros sistemas de token na cadeia.


- **Validação do lado do cliente**:

Bob pode verificar a consistência da transferência comparando a *consignação* com as *âncoras* na blockchain do Bitcoin. Ele não precisa de validação de terceiros. Alice não precisa de publicar o histórico completo na blockchain, o que reduz a carga sobre o protocolo de base e melhora a confidencialidade.


- **Atomicidade simplificada**:

As trocas complexas (swaps atómicos entre BTC e um ativo RGB, por exemplo) podem ser efectuadas numa única transação, evitando a necessidade de scripts HTLC ou PTLC. Se o acordo não for difundido, todos podem reutilizar os seus UTXOs de outras formas.

### Diagrama sintético de transferência

Antes de analisar as facturas em mais pormenor, eis um diagrama sumário do fluxo geral de uma transferência RGB:


- Bob instala uma carteira RGB e obtém a consignação inicial do contrato;
- O Bob emite uma fatura mencionando o UTXO onde deve receber o ativo;
- Alice recebe a fatura, constrói o PSBT e gera o consignamento do terminal;
- O Bob aceita-o, verifica, adiciona os dados ao seu stock e assina (*payslip*), se necessário;
- Alice publica a transação na rede Bitcoin;
- A confirmação da transação oficializa a transferência.

![RGB-Bitcoin](assets/en/080.webp)

A transferência ilustra todo o poder e flexibilidade do protocolo RGB: uma troca privada, validada no lado do cliente, ancorada de forma mínima e discreta na blockchain da Bitcoin, e retendo o melhor da segurança do protocolo (sem risco de gasto duplo). Isto faz do RGB um ecossistema promissor para transferências de valor mais confidenciais e escaláveis do que as cadeias de blocos programáveis na cadeia.

### Facturas RGB

Nesta secção, explicaremos em pormenor como funcionam as **facturas** no ecossistema RGB e como permitem realizar operações (em particular transferências) com um contrato. Primeiro, veremos os identificadores utilizados, depois a forma como são codificados e, por fim, a estrutura de uma fatura expressa como URL (um formato suficientemente prático para ser utilizado em carteiras).

#### Identificadores e codificação

É definido um identificador único para cada um dos seguintes elementos:


- Um contrato RGB;
- O seu esquema (lógica empresarial) ;
- Sua interface e implementação de interface ;
- Os seus activos (tokens, NFT, etc.),

Esta unicidade é muito importante, uma vez que cada componente do sistema deve ser distinguível. Por exemplo, um contrato X não pode ser confundido com outro contrato Y, e duas interfaces diferentes (RGB20 vs. RGB21, por exemplo) devem ter identificadores distintos.

Para tornar estes identificadores eficientes (tamanho reduzido) e legíveis, utilizamos :


- Codificação Base58, que evita a utilização de caracteres confusos (por exemplo, `0` e a letra `O`) e permite obter cadeias de caracteres relativamente curtas;
- Um prefixo que indica a natureza do identificador, geralmente sob a forma de `rgb:` ou de um URN semelhante.

Por exemplo, um `ContractId` pode ser representado por algo como :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

O prefixo `rgb:` confirma que se trata de um identificador RGB e não de uma ligação HTTP ou outro protocolo. Graças a este prefixo, as carteiras são capazes de interpretar a cadeia corretamente.

#### Segmentação de identificadores

Os identificadores RGB são frequentemente bastante longos, uma vez que a segurança (criptográfica) subjacente pode exigir campos de 256 bits ou mais. Para facilitar a leitura e verificação humanas, dividimos estas cadeias em vários blocos separados por um hífen (`-`). Assim, em vez de termos uma cadeia de caracteres longa e ininterrupta, dividimo-la em blocos mais curtos. Esta prática é comum para números de cartão de crédito ou de telefone, e também se aplica aqui para facilitar a verificação. Assim, por exemplo, pode ser dito a um utilizador ou parceiro: "*Por favor, verifique se o terceiro bloco é `9GEgnyMj7`*", em vez de ter de comparar tudo de uma só vez. O último bloco é frequentemente utilizado como **checksum**, para ter um sistema de deteção de erros ou gralhas.

A título de exemplo, um `ContractId` em base58 codificado e segmentado poderia ser :

```txt
2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX
```

Cada um dos traços divide a cadeia em secções. Isto não afecta a semântica do código, apenas a sua apresentação.

#### Utilização de URLs para facturas

Uma fatura RGB é apresentada como um URL. Isto significa que pode ser clicado ou digitalizado (como um código QR) e que uma carteira pode interpretá-lo diretamente para efetuar uma transação. Esta simplicidade de interação difere de alguns outros sistemas em que é necessário copiar e colar vários dados em diferentes campos do software.

Uma fatura para uma ficha fungível (por exemplo, uma ficha RGB20) pode ter o seguinte aspeto:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Vamos analisar este URL:


- `rgb:`** (prefixo): indica uma ligação que invoca o protocolo RGB (análogo a `http:` ou `bitcoin:` noutros contextos);
- `2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX`: representa o `ContractId` do token que pretende manipular;
- `/RGB20/100`: indica que é utilizada a interface `RGB20` e que são pedidas 100 unidades do bem. A sintaxe é a seguinte: `/Interface/amount` ;
- `+utxob:` **especifica que são acrescentadas informações sobre o UTXO destinatário (ou, mais precisamente, a definição do selo de utilização única);**
- `egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb`: este é o UTXO *oculto* (ou definição de selo). Por outras palavras, o Bob mascarou o seu UTXO exato, pelo que o remetente (Alice) não sabe qual é o endereço exato. Ela só sabe que existe um selo válido que se refere a um UTXO controlado pelo Bob.

O facto de tudo caber num único URL facilita a vida ao utilizador: um simples clique ou scan na carteira e a operação está pronta a ser executada.

Poder-se-ia imaginar sistemas em que, em vez do `ContractId`, fosse utilizado um simples ticker (por exemplo, `USDT`). No entanto, isso levantaria grandes problemas de confiança e segurança: um ticker não é uma referência única (vários contratos poderiam reivindicar o nome `USDT`). Com o RGB, pretendemos um identificador criptográfico único e não ambíguo. Daí a adoção da cadeia de 256 bits, codificada em base58 e segmentada. O utilizador sabe que está a manipular precisamente o contrato cujo ID é `2WBcas9-yjz...` e não qualquer outro.

#### Parâmetros URL adicionais

Também é possível acrescentar parâmetros adicionais ao URL, da mesma forma que com HTTP, como por exemplo :

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/100+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb?sig=6kzbKKffP6xftkxn9UP8gWqiC41W16wYKE5CYaVhmEve
```


- `?sig=...`: representa, por exemplo, uma assinatura associada à fatura, que algumas carteiras podem verificar;
- Se uma carteira não gere esta assinatura, ignora simplesmente este parâmetro.

Vejamos o caso de um NFT através da interface RGB21. Por exemplo, poderíamos ter :

```txt
rgb:7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK/RGB21/DbwzvSu-4BZU81jEp-E9FVZ3xj-cyuTKWWy-2gmdnaxt-ACrS+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Aqui vemos :


- `rgb:`**: Prefixo do URL ;
- **`7BKsac8-beMNMWA8r-3GEprtFh7-bjzEvGufY-aNLuU4nSN-MRsLOIK`**: ID do contrato (NFT) ;
- **rGB21**: interface para activos não fungíveis (NFT) ;
- `DbwzvSu-4BZU81jEp-...`: uma referência explícita à parte única do NFT, por exemplo, um hash do blob de dados (media, metadados...) ;
- **`+utxob:egXsFnw-...`**: a definição do selo.

A ideia é a mesma: transmitir uma ligação única que a carteira possa interpretar, identificando claramente o ativo único a transferir.

#### Outras operações via URL

Os URLs RGB não são usados apenas para solicitar uma transferência. Eles também podem codificar operações mais avançadas, como a emissão de novos tokens (*issuance*). Por exemplo:

```txt
rgb:2WBcas9-yjzEvGufY-9GEgnyMj7-beMNMWA8r-sPHtV1nPU-TMsGMQX/RGB20/issue/100000+utxob:egXsFnw-5Eud7WKYn-7DVQvcPbc-rR69YmgmG-veacwmUFo-uMFKFb
```

Aqui encontramos :


- `rgb:` : protocolo ;
- `2WBcas9-...`: ID do contrato ;
- `/RGB20/issue/100000`: indica que pretende invocar a transição "*Issue*" para criar 100.000 fichas adicionais;
- `+utxob:`: a definição do selo.

Por exemplo, a carteira pode ter a seguinte redação "Pediram-me para efetuar uma operação de `emissão` a partir da interface `RGB20`, num contrato tal e tal, para 100.000 unidades, em benefício de tal e tal Selo de Utilização Única"

Agora que já analisámos os principais elementos da programação RGB, passo ao capítulo seguinte sobre a elaboração de um contrato RGB.

## Elaboração de contratos inteligentes

<chapterId>0e0a645c-0049-588d-8965-b8c536590cc9</chapterId>

:::video id=a3ad6dcd-90b8-4272-9dfc-76c85c859167:::

Neste capítulo, vamos abordar passo-a-passo a escrita de um contrato, usando a ferramenta de linha de comando `rgb`. O objetivo é mostrar como instalar e manipular o CLI, compilar um **Esquema**, importar a **Interface** e a **Interface Implementation**, e depois emitir (*emitir*) um ativo. Também veremos a lógica subjacente, incluindo compilação e validação de estado. No final deste capítulo, deverá ser capaz de reproduzir o processo e criar os seus próprios contratos RGB.

Relembrando, a lógica interna do RGB baseia-se em bibliotecas Rust que os programadores podem importar para os seus projectos para gerir a parte da validação do lado do cliente. Além disso, a equipa da Associação LNP/BP está a trabalhar em ligações para outras línguas, mas isto ainda não foi finalizado. Além disso, outras entidades, como a Bitfinex, estão a desenvolver as suas próprias pilhas de integração (falaremos sobre elas nos últimos 2 capítulos do curso). Por enquanto, portanto, o `rgb` CLI é a referência oficial, mesmo que permaneça relativamente pouco polido.

### Instalação e apresentação da ferramenta rgb

O comando principal é simplesmente chamado `rgb`. Ele foi projetado para ser uma reminiscência do `git`, com um conjunto de sub-comandos para manipular contratos, invocá-los, emitir ativos e assim por diante. A Bitcoin Wallet não está integrada atualmente, mas estará em uma versão iminente (0.11). Esta próxima versão permitirá aos utilizadores criar e gerir as suas carteiras (através de descritores) diretamente a partir do `rgb`, incluindo a geração de PSBT, compatibilidade com hardware externo (por exemplo, uma carteira de hardware) para assinatura, e interoperabilidade com software como o Sparrow. Isto simplificará todo o cenário de emissão e transferência de activos.

#### Instalação via Cargo

Instalamos a ferramenta em Rust com :

```bash
cargo install rgb-contracts --all-features
```

(Nota: o crate é chamado `rgb-contracts`, e o comando instalado será chamado `rgb`. Se uma crate chamada `rgb` já existia, pode ter havido uma colisão, daí o nome)

A instalação compila um grande número de dependências (por exemplo, análise de comandos, integração Electrum, gestão de provas de conhecimento zero, etc.).

Quando a instalação estiver concluída, o ficheiro :

```bash
rgb
```

Executando `rgb` (sem argumentos) mostra uma lista de sub-comandos disponíveis, tais como `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer`, etc. Você pode mudar o diretório de armazenamento local (um esconderijo que guarda todos os logs, esquemas e implementações), escolher a rede (testnet, mainnet) ou configurar seu servidor Electrum.

![RGB-Bitcoin](assets/en/081.webp)

#### Primeira visão geral dos controlos

Quando executar o seguinte comando, verá que uma interface `RGB20` já está integrada por defeito:

```bash
rgb interfaces
```

Se esta interface não estiver integrada, clone o ficheiro :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Compilar:

```bash
cargo run
```

Em seguida, importe a interface da sua escolha:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-Bitcoin](assets/en/082.webp)

Por outro lado, é-nos dito que ainda não foi importado nenhum esquema para o software. Também não existe nenhum contrato na reserva. Para o ver, execute o comando :

```bash
rgb schemata
```

Pode então clonar o repositório para obter determinados esquemas:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-Bitcoin](assets/en/083.webp)

Este repositório contém, no seu diretório `src/`, vários ficheiros Rust (por exemplo `nia.rs`) que definem esquemas (NIA para "*Non Inflatable Asset*", UDA para "*Unique Digital Asset*", etc.). Para compilar, pode então executar :

```bash
cd rgb-schemata
cargo run
```

Isso gera vários arquivos `.rgb` e `.rgba` correspondentes aos esquemas compilados. Por exemplo, você encontrará `NonInflatableAsset.rgb`.

#### Importação de esquema e implementação de interface

Agora é possível importar o esquema para o `rgb` :

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-Bitcoin](assets/en/084.webp)

Isto adiciona-o ao stock local. Se executarmos o seguinte comando, vemos que o esquema aparece agora:

```bash
rgb schemata
```

### Criação de contratos (emissão)

Existem duas abordagens para criar um novo ativo:


- Ou utilizamos um script ou código em Rust que constrói um Contrato preenchendo os campos do esquema (estado global, Estados Próprios, etc.) e produz um ficheiro `.rgb` ou `.rgba`;
- Ou use o sub-comando `issue` diretamente, com um arquivo YAML (ou TOML) descrevendo as propriedades do token.

Pode encontrar exemplos em Rust na pasta `examples`, que ilustram como construir um `ContractBuilder`, preencher o `estado global` (nome do ativo, ticker, abastecimento, data, etc.), definir o Estado de Propriedade (a que UTXO está atribuído), e depois compilar tudo isto numa *consignação de contrato* que pode exportar, validar e importar para um esconderijo.

A outra maneira é editar manualmente um arquivo YAML para personalizar o `ticker`, o `nome`, o `fornecimento`, e assim por diante. Suponha que o arquivo se chame `RGB20-demo.yaml`. Você pode especificar :


- `spec`: ticker, nome, precisão ;
- `terms`: um campo para avisos legais ;
- `issuedSupply` : a quantidade de fichas emitidas ;
- `assignments`: indica o selo de utilização única (*definição do selo*) e a quantidade desbloqueada.

Eis um exemplo de um ficheiro YAML a criar:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: Plan ₿ Academy
name: Plan ₿ Academy
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-Bitcoin](assets/en/085.webp)

Em seguida, basta executar o comando :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-Bitcoin](assets/en/086.webp)

No meu caso, o identificador único do esquema (que deve ser colocado entre aspas simples) é `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` e não coloquei nenhum emitente. Portanto, o meu pedido é :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Se não souber o ID do esquema, execute o comando :

```bash
rgb schemata
```

O CLI responde que um novo contrato foi emitido e adicionado ao stash. Se digitarmos o seguinte comando, vemos que existe agora um contrato adicional, correspondente ao que acabou de ser emitido:

```bash
rgb contracts
```

![RGB-Bitcoin](assets/en/087.webp)

Em seguida, o comando seguinte apresenta os estados globais (nome, ticker, oferta...) e a lista de Estados Próprios, ou seja, as atribuições (por exemplo, 1 milhão de fichas `Plan ₿ Academy` definidas no UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-Bitcoin](assets/en/088.webp)

### Exportação, importação e validação

Para partilhar este contrato com outros utilizadores, pode ser exportado do esconderijo para um ficheiro :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-Bitcoin](assets/en/089.webp)

O arquivo `myContractPBN.rgb` pode ser passado para outro usuário, que pode adicioná-lo ao seu estoque com o comando :

```bash
rgb import myContractPBN.rgb
```

Aquando da importação, se se tratar de uma simples *contratação de consignação*, será apresentada a mensagem "`Importing consignment rgb`". Se se tratar de uma *consignação de transição de estado* de maior dimensão, o comando será diferente (`rgb accept`).

Para garantir a validade, também é possível utilizar a função de validação local. Por exemplo, é possível executar :

```bash
rgb validate myContract.rgb
```

#### Utilização, verificação e visualização de stocks

Para relembrar, o stash é um inventário local de esquemas, interfaces, implementações e contratos (Genesis + transições). Cada vez que executa "import", adiciona um elemento ao stash. Este stash pode ser visto em pormenor com o comando :

```bash
rgb dump
```

![RGB-Bitcoin](assets/en/090.webp)

Isto irá gerar uma pasta com detalhes de todo o stock.

### Transferência e PSBT

Para efetuar uma transferência, é necessário manipular uma carteira Bitcoin local para gerir os compromissos `Tapret` ou `Opret`.

#### Gerar uma fatura

Na maioria dos casos, a interação entre os participantes num contrato (por exemplo, Alice e Bob) ocorre através da geração de uma fatura. Se a Alice quiser que o Bob execute algo (uma transferência de fichas, uma reemissão, uma ação num DAO, etc.), a Alice cria uma fatura que detalha as suas instruções ao Bob. Assim, temos :


- **Alice** (o emitente da fatura) ;
- **Bob** (que recebe e executa a fatura).

Ao contrário de outros ecossistemas, uma fatura RGB não se limita à noção de pagamento. Pode incluir qualquer pedido ligado ao contrato: revogar uma chave, votar, criar uma gravação (*gravação*) num NFT, etc. A operação correspondente pode ser descrita na interface do contrato. A operação correspondente pode ser descrita na interface do contrato.

O seguinte comando gera uma fatura RGB:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Com :


- `$CONTRACT`: Identificador do contrato (*ContractId*) ;
- `$INTERFACE`: a interface a utilizar (por exemplo, `RGB20`) ;
- `$ACTION`: o nome da operação especificada na interface (para uma simples transferência de token fungível, poderia ser "Transfer"). Se a interface já fornecer uma ação por defeito, não é necessário introduzi-la novamente aqui;
- `$STATE`: os dados de estado a transferir (por exemplo, um montante de fichas se for transferida uma ficha fungível);
- `$SEAL`: o selo de utilização única do beneficiário (Alice), ou seja, uma referência explícita a um UTXO. O Bob utilizará esta informação para construir a transação testemunha, e o resultado correspondente pertencerá então à Alice (em *UTXO oculto* ou não encriptado).

Por exemplo, com os seguintes comandos

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

O CLI gerará uma fatura como :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Pode ser transmitida ao Bob através de qualquer canal (texto, código QR, etc.).

#### Efetuar uma transferência

Para transferir a partir desta fatura :


- Bob (que detém os tokens no seu stash) possui uma wallet Bitcoin. Ele deve preparar uma transação Bitcoin (na forma de PSBT, por ex. `tx.psbt`) que gaste os UTXOs onde se encontram os tokens RGB necessários, além de um UTXO para o troco (change);
- O Bob executa o seguinte comando:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Isto gera um ficheiro `consignment.rgb` que contém :
 - O historial de transição prova à Alice que os tokens são genuínos;
 - A nova transição que transfere fichas para o selo de utilização única da Alice ;
 - Uma transação de testemunha (não assinada).
- Bob envia este ficheiro `consignment.rgb` a Alice (por correio eletrónico, um servidor de partilha ou um protocolo RGB-RPC, Storm, etc.);
- Alice recebe `consignment.rgb` e aceita-o na sua própria reserva :

```bash
alice$ rgb accept consignment.rgb
```


- O CLI verifica a validade da transição e adiciona-a ao esconderijo da Alice. Se for inválido, o comando falha com mensagens de erro detalhadas. Caso contrário, ele é bem-sucedido e informa que a transação de amostra ainda não foi transmitida na rede Bitcoin (Bob está aguardando a luz verde de Alice);
- A título de confirmação, o comando `accept` devolve uma assinatura (*payslip*) que Alice pode enviar a Bob para lhe mostrar que validou a *consignação* ;
- Bob pode então assinar e publicar (`--publish`) sua transação Bitcoin:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Assim que esta transação é confirmada na cadeia, a propriedade do ativo é considerada transferida para Alice. A carteira de Alice, que monitoriza a extração da transação, vê o novo Estado de Propriedade aparecer no seu esconderijo.

No próximo capítulo, analisaremos mais detalhadamente a integração do RGB na rede Lightning.

## RGB na rede Lightning

<chapterId>0962980a-8f94-5d0f-9cd0-43d7f884a01d</chapterId>

:::video id=be25a165-6e23-488c-91d8-3dcfccc6eca1:::

Neste capítulo, proponho-me examinar a forma como o RGB pode ser utilizado na Lightning Network, para integrar e movimentar activos RGB (tokens, NFTs, etc.) através de canais de pagamento fora da cadeia.

A ideia básica é que a transição de estado RGB (*Transição de estado*) pode ser comprometida com uma transação Bitcoin que, por sua vez, pode permanecer fora da cadeia até que o canal Lightning seja fechado. Assim, cada vez que o canal é atualizado, uma nova transição de estado RGB pode ser incorporada na nova transação de confirmação, o que invalida a transição antiga. Desta forma, os canais Lightning podem ser utilizados para transferir activos RGB e podem ser encaminhados da mesma forma que os pagamentos Lightning convencionais.

### Criação e financiamento de canais

Para criar um canal Lightning que transporta activos RGB, precisamos de dois elementos:


- Financiamento Bitcoin para criar o multisig 2/2 do canal (o UTXO básico para o canal);
- Financiamento RGB, que envia activos para o mesmo multisig.

Em termos de Bitcoin, a transação de financiamento deve existir para definir o UTXO de referência, mesmo que contenha apenas uma pequena quantidade de sats (é apenas uma questão de cada saída em futuras transacções de compromisso permanecer acima do limite de poeira). Por exemplo, Alice pode decidir fornecer 10k sats e 500 USDT (emitidos como um ativo RGB). Na transação de financiamento, adicionamos um compromisso (`Opret` ou `Tapret`) que ancora a transição do estado RGB.

![RGB-Bitcoin](assets/en/091.webp)

Depois de a transação de financiamento ter sido preparada (mas ainda não transmitida), são criadas transacções de compromisso para que qualquer uma das partes possa fechar o canal unilateralmente a qualquer momento. Estas transacções assemelham-se às transacções de compromisso clássicas do Lightning, exceto pelo facto de acrescentarmos uma saída adicional que contém a âncora RGB (OP_RETURN ou Taproot) ligada à nova transição de estado.

A transição de estado RGB move então os activos do multisig 2/2 do financiamento para os outputs da transação de compromisso. A vantagem deste processo é que a segurança do estado RGB corresponde exatamente à mecânica punitiva do Lightning: se Bob transmitir um estado de canal antigo, Alice pode puni-lo e gastar o output, de modo a recuperar tanto os sats como os tokens RGB. O incentivo é, portanto, ainda mais forte do que num canal Lightning sem activos RGB, uma vez que um atacante pode perder não só os sats, mas também os activos RGB do canal.

Uma transação de compromisso assinada por Alice e enviada a Bob teria, portanto, o seguinte aspeto

![RGB-Bitcoin](assets/en/092.webp)

E a transação de compromisso que a acompanha, assinada por Bob e enviada a Alice, terá o seguinte aspeto:

![RGB-Bitcoin](assets/en/093.webp)

### Atualização do canal

Quando ocorre um pagamento entre dois participantes do canal (ou estes pretendem alterar a afetação de activos), criam um novo par de transacções de compromisso. O montante em sats de cada saída pode ou não permanecer inalterado, consoante a implementação, uma vez que a sua principal função é permitir a construção de UTXOs válidas. Por outro lado, a saída OP_RETURN (ou Taproot) deve ser modificada para conter a nova âncora RGB, que representa a nova distribuição dos activos no canal.

Por exemplo, se Alice transferir 30 USDT para Bob no canal, a nova transição de estado reflectirá um saldo de 400 USDT para Alice e 100 USDT para Bob. A transação de confirmação é adicionada à (ou modificada pela) âncora OP_RETURN/Taproot para incluir esta transição. Note-se que, do ponto de vista da RGB, a entrada para a transição continua a ser o multisig inicial (onde os activos na cadeia são realmente alocados até o canal fechar). Apenas os outputs do RGB (alocações) mudam, dependendo da redistribuição decidida.

A transação de compromisso assinada por Alice, pronta a ser distribuída por Bob :

![RGB-Bitcoin](assets/en/094.webp)

A transação de compromisso assinada por Bob, pronta a ser distribuída por Alice :

![RGB-Bitcoin](assets/en/095.webp)

### Gestão de HTLC

Na realidade, a Lightning Network permite que os pagamentos sejam encaminhados através de múltiplos canais, utilizando HTLCs (*Hashed Time-Locked Contracts*). O mesmo se passa com o RGB: para cada pagamento em trânsito no canal, é adicionado um output HTLC à transação de confirmação e uma alocação RGB ligada a este HTLC. Assim, quem gasta a saída HTLC (graças ao segredo ou após a expiração do timelock) recupera tanto os sats como os activos RGB associados. Por outro lado, é óbvio que é necessário ter dinheiro suficiente na estrada, tanto em termos de sats como de activos RGB.

![RGB-Bitcoin](assets/en/096.webp)

O funcionamento do RGB no Lightning deve, portanto, ser considerado em paralelo com o da própria rede Lightning. Se quiser aprofundar este assunto, recomendo vivamente que dê uma vista de olhos a este outro curso de formação completo:

https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Mapa de código RGB

Finalmente, antes de passar à secção seguinte, gostaria de dar uma visão geral do código utilizado no RGB. O protocolo baseia-se num conjunto de bibliotecas Rust e especificações de código aberto. Eis um resumo dos principais repositórios e caixas:

![RGB-Bitcoin](assets/en/097.webp)

#### Validação do lado do cliente


- **Repositório**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- **Caixas**: [client_side_validation](https://crates.io/crates/client_side_validation), [single_use_seals](https://crates.io/crates/single_use_seals)

Gestão da validação fora da cadeia e da lógica dos selos de utilização única.

#### Compromissos determinísticos de Bitcoin (DBC)


- **Repositório**: [bp-core](https://github.com/BP-WG/bp-core)
- **Caixa**: [bp-dbc](https://crates.io/crates/bp-dbc)

Gestão da ancoragem determinística nas transacções Bitcoin (Tapret, OP_RETURN, etc.).

#### Compromisso multiprotocolo (MPC)


- **Repositório**: [client_side_validation](https://github.com/LNP-BP/client_side_validation)
- **Crate**: [commit_verify](https://crates.io/crates/commit_verify)

Múltiplas combinações de compromissos e integração com diferentes protocolos.

#### Tipos estritos e codificação estrita


- **Especificações**: [sítio Web strict-types.org](https://www.strict-types.org/)
- **Repositórios**: [strict-types](https://github.com/strict-types/strict-types), [strict-encoding](https://github.com/strict-types/strict-encoding)
- **Caixas**: [strict_types](https://crates.io/crates/strict_types), [strict_encoding](https://crates.io/crates/strict_encoding)

O sistema de tipagem rigoroso e a serialização determinística utilizados para a validação do lado do cliente.

#### Núcleo RGB


- **Repositório**: [rgb-core](https://github.com/RGB-WG/rgb-core)
- **Caixa**: [rgb-core](https://crates.io/crates/rgb-core)

O núcleo do protocolo, que engloba a lógica principal da validação RGB.

#### Biblioteca e carteira padrão RGB


- **Repositório**: [rgb-std](https://github.com/RGB-WG/rgb-std)
- **Caixa**: [rgb-std](https://crates.io/crates/rgb-std)

Implementações normalizadas, gestão de stocks e carteiras.

#### RGB CLI


- **Repositório**: [rgb](https://github.com/RGB-WG/rgb)
- **Caixas**: [rgb-cli](https://crates.io/crates/rgb-cli), [rgb-wallet](https://crates.io/crates/rgb-wallet)

O `rgb` CLI e crate wallet, para manipulação de contratos em linha de comando.

#### Esquema RGB


- **Repositório**: [rgb-schemata](https://github.com/RGB-WG/rgb-schemata/)

Contém exemplos de esquemas (NIA, UDA, etc.) e respectivas implementações.

#### ALuVM


- **Informação**: [aluvm.org](https://www.aluvm.org/)
- **Repositórios**: [aluvm-spec](https://github.com/AluVM/aluvm-spec), [alure](https://github.com/AluVM/alure)
- **Caixas**: [aluvm](https://crates.io/crates/aluvm), [aluasm](https://crates.io/crates/aluasm)

Máquina virtual baseada no registo utilizada para executar scripts de validação.

#### Protocolo Bitcoin - BP


- **Repositórios**: [bp-core](https://github.com/BP-WG/bp-core), [bp-std](https://github.com/BP-WG/bp-std), [bp-wallet](https://github.com/BP-WG/bp-wallet)

Add-ons para suportar o protocolo Bitcoin (transacções, desvios, etc.).

#### Computação Ubíqua Determinística - UBIDECO


- **Repositório**: [UBIDECO](https://github.com/UBIDECO)

Ecossistema ligado a desenvolvimentos determinísticos de fonte aberta.

# Baseando-se no RGB

<partId>3b4b0d66-0c1b-505a-b5ca-4b2e57dd73c2</partId>

## DIBA e o projeto Bitmask

<chapterId>dc92a5e8-ed93-5a3f-bcd0-d433932842f4</chapterId>

:::video id=2ec9a181-a8b0-4da2-b7b5-9dfaaaeb10ba:::

Esta última secção do curso baseia-se nas apresentações feitas por vários oradores no bootcamp RGB. Inclui testemunhos e reflexões sobre o RGB e o seu ecossistema, bem como apresentações de ferramentas e projectos baseados no protocolo. Este primeiro capítulo é moderado por Hunter Beast e os dois seguintes por Frederico Tenga.

### Do JavaScript para o Rust e para o ecossistema Bitcoin

No início, Hunter Beast trabalhava principalmente em JavaScript. Depois descobriu **Rust**, cuja sintaxe parecia pouco atraente e frustrante no início. No entanto, acabou por apreciar o poder da linguagem, o controlo sobre a memória (*heap* e *stack*), a segurança e o desempenho que lhe estão associados. Ele enfatiza que Rust é um excelente campo de treinamento para uma compreensão profunda de como um computador funciona.

Hunter Beast conta a sua experiência em vários projectos do ecossistema *altcoin*, como o Ethereum (com Solidity, TypeScript, etc.) e, mais tarde, o Filecoin. Explica que ficou inicialmente impressionado com alguns dos protocolos, mas que acabou por ficar desiludido com a maior parte deles, nomeadamente devido à sua tokenomics. Denuncia os incentivos financeiros duvidosos, a criação inflacionária de tokens que dilui os investidores e o aspeto potencialmente explorador destes projectos. Assim, acabou por adotar uma postura **Bitcoin maximalista**, até porque algumas pessoas lhe abriram os olhos para os mecanismos económicos mais sólidos do Bitcoin e para a robustez deste sistema.

### O atrativo do RGB e a construção em camadas

O que o convenceu definitivamente da relevância do Bitcoin, nas suas palavras, foi a descoberta do RGB e o conceito de camadas. Ele acredita que as funcionalidades existentes em outros blockchains poderiam ser reproduzidas em camadas superiores, acima do Bitcoin, sem alterar o protocolo básico.

Em fevereiro de 2022, juntou-se à **DIBA** para trabalhar especificamente no RGB e, em particular, na carteira **Bitmask**. Na altura, a Bitmask ainda estava na versão 0.01 e executava o RGB na versão 0.4, apenas para a gestão de tokens individuais. Ele observa que isso era menos orientado para a autocustódia do que hoje, já que a lógica era parcialmente baseada no servidor. Desde então, a arquitetura evoluiu para este modelo, muito apreciado pelos bitcoiners.

### As bases do protocolo RGB

O protocolo **RGB** é a mais recente e mais avançada concretização do conceito de _colored coins_, já explorado por volta de 2012-2013. Na altura, várias equipas procuravam associar diferentes valores de bitcoin aos UTXOs, o que levou a múltiplas implementações dispersas. Esta falta de padronização e a baixa procura na altura impediram que estas soluções ganhassem uma posição duradoura.

Atualmente, a RGB destaca-se pela sua robustez concetual e especificações unificadas através da associação LNP/BP. O princípio baseia-se na validação do lado do cliente. A blockchain Bitcoin apenas armazena compromissos criptográficos (_commitments_, via Taproot ou OP_RETURN), enquanto a maioria dos dados (definições de contratos, históricos de transferências, etc.) é armazenada pelos utilizadores em causa. Desta forma, a carga de armazenamento é distribuída e a confidencialidade das trocas é reforçada, sem sobrecarregar a cadeia de blocos. Esta abordagem permite a criação de activos fungíveis (norma **RGB20**) ou únicos (norma **RGB21**), num quadro modular e escalável.

### A função de ficha (RGB20) e os activos únicos (RGB21)

Com **RGB20**, definimos um token fungível no Bitcoin. O emissor escolhe uma _oferta_, uma _precisão_, e cria um _contrato_ no qual pode então efetuar transferências. Cada transferência é referenciada a um Bitcoin UTXO, que actua como um *Selo de utilização única*. Esta lógica garante que o utilizador não poderá gastar o mesmo ativo duas vezes, uma vez que apenas a pessoa capaz de gastar o UTXO detém a chave para atualizar o estado do contrato do lado do cliente.

**RGB21** visa activos únicos (ou "NFT"). O ativo tem um fornecimento de 1, e pode ser associado a metadados (ficheiro de imagem, áudio, etc.) descritos através de um campo específico. Ao contrário dos NFTs em cadeias de blocos públicas, os dados e os seus identificadores MIME podem permanecer privados, distribuídos ponto a ponto à discrição do proprietário.

### A solução Bitmask: uma carteira para RGB

Para explorar as capacidades do RGB na prática, o projeto **DIBA** concebeu uma carteira chamada [Bitmask](https://bitmask.app/). A ideia é fornecer uma ferramenta sem custódia, baseada no Taproot, acessível como uma aplicação web ou extensão do browser. A Bitmask gere activos RGB20 e RGB21 e integra vários mecanismos de segurança:


- O código principal é escrito em Rust e depois compilado em WebAssembly para ser executado num ambiente JavaScript (React);
- As chaves são geradas localmente e depois armazenadas encriptadas localmente;
- Os dados de estado (stash) são mantidos em memória, serializados e encriptados através da biblioteca **Carbonado**, que efectua a compressão, a correção de erros, a encriptação e a verificação do fluxo utilizando Blake3.

Graças a esta arquitetura, todas as transacções de activos têm lugar no lado do cliente. Do lado de fora, a transação Bitcoin não é mais do que uma transação clássica de gastos Taproot, que ninguém suspeitaria que também transporta uma transferência de tokens fungíveis ou NFTs. A ausência de sobrecarga na cadeia (sem metadados armazenados publicamente) garante um certo grau de discrição e facilita a resistência a possíveis tentativas de censura.

### Segurança e arquitetura distribuída

Na medida em que o protocolo RGB exige que cada participante conserve o seu histórico de transacções (para provar a validade das transferências que recebe), coloca-se a questão do armazenamento. A Bitmask propõe serializar localmente este stash e depois enviá-lo para vários servidores ou nuvens (opcional). Os dados permanecem encriptados pelo utilizador através do **Carbonado**, pelo que um servidor não os pode ler. Em caso de corrupção parcial, a camada de correção de erros pode reconstituir o conteúdo.

A utilização de CRDT (_Conflict-free replicated data type_) permite a fusão de diferentes versões do stash, caso estas divirjam. Cada um é livre de alojar estes dados onde quiser, uma vez que nenhum nó completo contém toda a informação relacionada com o ativo. Isto reflecte exatamente a filosofia *Client-side Validation*, em que cada proprietário é responsável por armazenar provas da validade do seu ativo RGB.

### Rumo a um ecossistema mais vasto: mercado, interoperabilidade e novas funções

A empresa por detrás da Bitmask não se limita ao simples desenvolvimento de uma carteira. A DIBA pretende desenvolver :


- Um **mercado** para troca de tokens, particularmente na forma **RGB21**;
- Compatibilidade com outras carteiras (como a *Iris Wallet*);
- **Técnicas de transferência em lote**, ou seja, a possibilidade de incluir várias transferências RGB sucessivas numa única transação.

Ao mesmo tempo, estamos a trabalhar em **WebBTC** ou **WebLN** (normas que permitem que os sites peçam à carteira para assinar transacções Bitcoin ou Lightning), bem como na capacidade de "telequeimar" entradas Ordinals (se quisermos repatriar Ordinals para um formato RGB mais discreto e flexível).

### Conclusão

Todo este processo mostra como o ecossistema RGB pode ser implementado e tornado acessível aos utilizadores finais através de soluções técnicas robustas. A transição de uma perspetiva altcoin para uma visão mais centrada no Bitcoin, associada à descoberta da *Client-side Validation*, ilustra um caminho bastante lógico: compreendemos que é possível implementar várias funcionalidades (tokens fungíveis, NFT, contratos inteligentes...) sem bifurcar a blockchain, simplesmente tirando partido dos compromissos criptográficos nas transacções Taproot ou OP_RETURNs.

A carteira **Bitmask** faz parte desta abordagem: do lado da blockchain, tudo o que vê é uma transação Bitcoin normal; do lado do utilizador, manipula uma interface web onde cria, troca e armazena todo o tipo de activos fora da cadeia. Este modelo dissocia claramente a infraestrutura monetária (Bitcoin) da lógica de emissão e de transferência (RGB), garantindo simultaneamente um elevado nível de confidencialidade e uma melhor escalabilidade.

## Trabalho da Bitfinex sobre RGB

<chapterId>d4d80e07-5eac-5b29-a93a-123180e97047</chapterId>

:::video id=04555813-516f-4eea-9767-7082c2ea6f01:::

Neste capítulo, com base numa apresentação de Frederico Tenga, analisamos um conjunto de ferramentas e projectos criados pela equipa da Bitfinex dedicados ao RGB, com o objetivo de fomentar a emergência de um ecossistema rico e diversificado em torno deste protocolo. O objetivo inicial da equipa não é lançar um produto comercial específico, mas sim fornecer blocos de construção de software, contribuir para o próprio protocolo RGB e propor referências concretas de implementação, como uma carteira móvel (*Iris Wallet*) ou um nó Lightning compatível com o RGB.

### Antecedentes e objectivos

Desde cerca de 2022, a equipa Bitfinex RGB tem vindo a concentrar-se no desenvolvimento da pilha de tecnologia que permite que o RGB seja explorado e testado de forma eficiente. Várias contribuições foram feitas:


- Participação nas especificações do código-fonte e do protocolo, incluindo a redação de propostas de melhoria, a correção de erros, etc;
- Ferramentas para os programadores simplificarem a integração do RGB nas suas aplicações;
- Conceção de uma carteira móvel denominada [Iris] (https://iriswallet.com/) para experimentar e ilustrar as melhores práticas de utilização do RGB ;
- Criação de um nó Lightning personalizado, capaz de gerir canais com activos RGB;
- Apoiar outras equipas que desenvolvem soluções em RGB, para incentivar a diversidade e um ecossistema forte.

Esta abordagem visa cobrir toda a cadeia de necessidades: desde a biblioteca de baixo nível (*[RGBlib](https://github.com/RGB-Tools/rgb-lib)*), que permite a implementação de uma carteira, até ao aspeto da produção (um nó Lightning, uma carteira para Android, etc.).

### A biblioteca RGBlib: simplificar o desenvolvimento de aplicações RGB

Um ponto importante na democratização da criação de carteiras e aplicações RGB é disponibilizar uma abstração simples o suficiente para que os desenvolvedores não tenham que aprender tudo sobre a lógica interna do protocolo. Este é precisamente o objetivo da **RGBlib**, escrita em Rust.

O RGBlib atua como uma ponte entre os requisitos altamente flexíveis (mas às vezes complexos) do RGB que pudemos estudar nos capítulos anteriores e as necessidades concretas de um desenvolvedor de aplicativos. Por outras palavras, uma carteira (ou serviço) que pretenda gerir transferências de tokens, emissão de activos, verificação, etc., pode confiar no RGBlib sem conhecer todos os detalhes criptográficos ou todos os parâmetros RGB personalizáveis.

A livraria oferece :


- Funções "chave na mão" para a emissão (_emissão_) de activos (fungíveis ou não);
- A capacidade de transferir (enviar/receber) activos através da manipulação de objectos simples (endereços, montantes, UTXOs, etc.);
- Um mecanismo para armazenar e carregar as informações de estado (*consignações*) necessárias para a validação do lado do cliente.

O RGBlib, portanto, se baseia em noções complexas específicas do RGB (validação do lado do cliente, âncoras Tapret/Opret), mas as encapsula para que a aplicação final não tenha que reprogramar tudo ou tomar decisões arriscadas. Além disso, o RGBlib já está ligado a várias linguagens (Kotlin e Python), abrindo a porta a utilizações que vão para além de um simples universo Rust.

### Iris Wallet: um exemplo de uma carteira RGB no Android

Para provar a eficácia do RGBlib, a equipa da Bitfinex desenvolveu a **Iris Wallet**, exclusivamente para Android nesta fase. É uma carteira móvel que ilustra uma experiência de utilizador semelhante à de uma carteira Bitcoin normal: pode emitir um ativo, enviá-lo, recebê-lo e ver o seu histórico, mantendo-se num modelo de auto-custódia.

O Iris tem uma série de caraterísticas interessantes:

**Utilizando um servidor Electrum:**

Como qualquer carteira, a Iris precisa de saber sobre as confirmações de transacções na cadeia de bloqueio. Em vez de incorporar um nó completo, o Iris usa como padrão um servidor Electrum mantido pela equipa da Bitfinex. Os utilizadores podem, no entanto, configurar o seu próprio servidor ou outro serviço de terceiros. Desta forma, as transacções Bitcoin podem ser validadas e a informação recuperada (indexação) de uma forma modular.

**O servidor proxy RGB:**

Ao contrário do Bitcoin, o RGB requer a troca de metadados fora da cadeia (*consignments*) entre o emissor e o recetor. Para simplificar este processo, a Iris oferece uma solução em que a comunicação é efectuada através de um servidor proxy. A carteira recetora gera uma *fatura* que menciona para onde o remetente deve enviar os dados *do lado do cliente*. Por defeito, o URL aponta para um proxy alojado pela equipa Bitfinex, mas é possível alterar este proxy (ou alojar o seu próprio). A ideia é voltar a uma experiência de utilizador familiar em que o destinatário apresenta um código QR e o remetente digitaliza este código para a transação, sem quaisquer manipulações adicionais complexas.

**Cópia de segurança contínua:**

Num contexto estritamente Bitcoin, fazer o backup da sua semente é geralmente suficiente (embora hoje em dia recomendamos fazer o backup da semente e dos descritores). Com a RGB, isso não é suficiente: é preciso também manter o histórico local (as *consignações*), provando que você realmente possui um ativo RGB. Cada vez que recebe um recibo, o dispositivo armazena novos dados, essenciais para as despesas posteriores. O Iris gere automaticamente uma cópia de segurança encriptada no Google Drive do utilizador. Não é necessária qualquer confiança especial no Google, uma vez que a cópia de segurança é encriptada, e estão previstas para o futuro opções mais robustas (como um servidor pessoal) para evitar qualquer risco de censura ou eliminação por um operador terceiro.

**Outras caraterísticas:**


- Crie uma torneira para testar rapidamente ou distribuir fichas para experimentação ou promoção;
- Um sistema de certificação (atualmente centralizado) para distinguir um token legítimo de um token falso que copia um ticker famoso. No futuro, esta certificação pode tornar-se mais descentralizada (via DNS ou outros mecanismos).

Em suma, o Iris oferece uma experiência de utilizador próxima da de uma carteira Bitcoin clássica, mascarando a complexidade adicional (gestão de stash, histórico de *consignações*, etc.) graças à RGBlib e à utilização de um servidor proxy.

### Servidor proxy e experiência do utilizador

O servidor proxy introduzido acima merece ser detalhado, pois é a chave para uma experiência de utilizador sem problemas. Em vez de o remetente ter de transmitir manualmente as *consignações* para o destinatário, a transação RGB tem lugar em segundo plano através de um ficheiro :


- O destinatário gera uma *fatura* (contendo, entre outras coisas, o endereço do proxy);
- O remetente envia (através de um pedido HTTP) um projeto de transição (a *atribuição*) para o proxy ;
- O destinatário recupera este projeto e executa localmente a validação *do lado do cliente*;
- O destinatário publica então, através do proxy, a aceitação (ou eventualmente a rejeição) da transição de estado ;
- O remetente pode ver o estado de validação e, se for aceite, transmitir a transação Bitcoin, finalizando a transferência.

Desta forma, a carteira comporta-se quase como uma carteira normal. O utilizador não tem conhecimento de todos os passos intermédios. É certo que o proxy atual não é encriptado nem autenticado (o que deixa dúvidas quanto à confidencialidade e integridade), mas estas melhorias são possíveis em versões posteriores. O conceito de proxy continua a ser extremamente útil para recriar a experiência "Eu envio um código QR, tu digitalizas para pagar".

### Integração RGB na rede Lightning

Outro ponto-chave do trabalho da equipa da Bitfinex é tornar a Lightning Network compatível com os activos RGB. O objetivo é permitir canais Lightning em USDT (ou qualquer outro token) e beneficiar das mesmas vantagens que a bitcoin na Lightning (transacções quase instantâneas, encaminhamento, etc.). Em termos concretos, trata-se de criar um nó Lightning modificado para :


- Abra um canal colocando não só satoshis, mas também um ou mais activos RGB no multisig UTXO de financiamento;
- Gerar transacções de compromisso Lightning (lado Bitcoin) acompanhadas das correspondentes transições de estado RGB. Cada vez que o canal é atualizado, uma transição RGB redefine a distribuição de activos nos outputs Lightning;
- Permitir o encerramento unilateral, em que o ativo é recuperado num UTXO exclusivo, em conformidade com as regras da Lightning Network (HTLC, timelock, punição, etc.).

Esta solução, apelidada de "**RGB Lightning Node**", usa o LDK (*Lightning Dev Kit*) como base, e adiciona os mecanismos necessários para injetar tokens RGB nos canais. Os compromissos Lightning mantêm a estrutura clássica (saídas pontuáveis, timelock...) e, além disso, ancoram uma transição de estado RGB (via `Opret` ou `Tapret`). Para o usuário, isso abre o caminho para os canais Lightning em stablecoins ou em qualquer outro ativo emitido via RGB.

### Potencial e impacto da DEX na Bitcoin

Uma vez que vários ativos são gerenciados via Lightning, torna-se possível imaginar uma **troca atômica** em um único caminho de roteamento Lightning, usando a mesma lógica de segredos e timelocks. Por exemplo, o utilizador A detém bitcoin num canal Lightning e o utilizador B detém USDT RGB noutro canal Lightning. Eles podem construir um caminho ligando seus dois canais e simultaneamente trocar BTC por USDT, sem a necessidade de confiança. Isto não é mais do que uma **troca atómica** que ocorre em vários saltos, tornando os participantes externos quase alheios ao facto de estarem a fazer uma troca e não apenas um encaminhamento. Esta abordagem oferece :


- Latência muito baixa, uma vez que tudo permanece fora da cadeia no Lightning.
- Uma **privacidade** superior: ninguém sabe que se trata de uma transação, e não de um encaminhamento normal;
- Evitar o frontrunning, um problema recorrente para a DEX na cadeia;
- Custos reduzidos (não paga espaço em bloco, apenas taxas de encaminhamento de relâmpagos).

Podemos então imaginar um ecossistema onde os nós Lightning oferecem preços de swap (fornecendo liquidez). Cada nó, se o desejar, pode desempenhar o papel de _market maker_, comprando e vendendo vários activos no Lightning. Esta perspetiva de uma DEX _layer-2_ reforça a ideia de que não é necessário bifurcar ou utilizar blockchains de terceiros para obter trocas de activos descentralizadas.

O impacto na Bitcoin poderia ser positivo: A infraestrutura da Lightning (nós, canais e serviços) seria mais bem utilizada graças aos volumes gerados por estas *stablecoins*, derivados e outros tokens. Os comerciantes interessados em pagamentos em USDT no Lightning descobririam mecanicamente pagamentos em BTC no Lightning (geridos pela mesma pilha). A manutenção e o financiamento da infraestrutura da rede Lightning poderiam também beneficiar da multiplicação destes fluxos não BTC, o que beneficiaria indiretamente os utilizadores de Bitcoin.

### Conclusão e recursos

A equipa da Bitfinex dedicada ao RGB ilustra, através do seu trabalho, a diversidade do que pode ser feito em cima do protocolo. Por um lado, temos a RGBlib, uma biblioteca que facilita a conceção de carteiras e aplicações. Por outro lado, temos a Iris Wallet, uma demonstração prática no Android de uma interface de utilizador final elegante. Finalmente, a integração do RGB com o Lightning mostra que os canais de stablecoin são possíveis e abre o caminho para um potencial DEX descentralizado no Lightning.

Esta abordagem continua a ser em grande parte experimental e continua a evoluir: a biblioteca RGBlib está a ser aperfeiçoada à medida que avançamos, a Iris Wallet está a receber melhorias regulares e o nó Lightning dedicado ainda não é um cliente Lightning convencional.

Para aqueles que desejam saber mais ou contribuir, estão disponíveis vários recursos, incluindo :


- [Repositórios de ferramentas RGB do GitHub](https://github.com/RGB-Tools);
- [Um sítio de informações dedicado à Iris Wallet] (https://iriswallet.com/) para testar a carteira no Android.

No próximo capítulo, veremos mais detalhadamente como lançar um nó de iluminação RGB.

## RLN - Nó de iluminação RGB

<chapterId>ecaabe32-20ba-5f8c-8ca1-a3f095792958</chapterId>

:::video id=d1e9753e-6093-4a47-bcdc-da1aebaefffc:::

Neste capítulo final, Frederico Tenga leva-o passo a passo através da configuração de um nó Lightning RGB num ambiente Regtest, e mostra-lhe como criar tokens RGB nele. Ao lançar dois nós separados, você também descobrirá como abrir um canal Lightning entre eles e trocar ativos RGB.

Este vídeo serve como um tutorial, semelhante ao que abordámos num capítulo anterior, mas desta vez centrado especificamente no Lightning!

O principal recurso para este vídeo é o repositório do Github [RGB Lightning Node] (https://github.com/RGB-Tools/rgb-lightning-node), que facilita o lançamento dessa configuração no Regtest.

### Implantação de um nó do Lightning compatível com RGB

O processo retoma e põe em prática todos os conceitos abordados nos capítulos anteriores:


- A ideia de que o **UTXO** bloqueado num multisig 2/2 de um canal Lightning pode receber não só bitcoins, mas também ser um selo de utilização única de activos RGB (fungíveis ou não);
- A adição, em cada transação de ligação do relâmpago, de uma saída (`Tapret` ou `Opret`) dedicada a ancorar a transição de estado RGB;
- A infraestrutura associada (bitcoind/indexer/proxy) para validar transacções Bitcoin e trocar dados do lado do cliente.

### Apresentação do nó de iluminação rgb

O projeto **`rgb-lightning-node`** é um daemon Rust baseado em um fork `rust-lightning` (LDK) modificado para levar em conta a existência de assets RGB em um canal. Quando um canal é aberto, a presença de ativos pode ser especificada, e cada vez que o estado do canal é atualizado, uma transição RGB é criada, refletindo a distribuição do ativo nas saídas do Lightning. Isso permite :


- Abrir canais Lightning em USDT, por exemplo;
- Encaminhar estes tokens através da rede, desde que os caminhos de encaminhamento tenham liquidez suficiente;
- Explorar a lógica de punição e bloqueio de tempo do Lightning sem modificação: basta ancorar a transição RGB numa saída adicional da transação de compromisso.

O código ainda está em fase alfa: recomendamos a sua utilização apenas em **regtest** ou na **testnet**.

### Instalação do nó

Para compilar e instalar o binário `rgb-lightning-node`, começamos por clonar o repositório e seus sub-módulos, depois executamos o comando :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RGB-Bitcoin](assets/en/098.webp)


- A opção `--recurse-submodules` também clona os sub-dispositivos necessários (incluindo a versão modificada do `rust-lightning`);
- A opção `--shallow-submodules` restringe a profundidade do clone para acelerar o download, enquanto ainda fornece acesso aos commits essenciais.

A partir da raiz do projeto, execute o seguinte comando para compilar e instalar o binário :

```bash
cargo install --locked --debug --path .
```

![RGB-Bitcoin](assets/en/099.webp)


- `--locked` garante que a versão das dependências seja estritamente respeitada;
- o `--debug` não é obrigatório, mas pode ajudá-lo a concentrar-se (pode utilizar o `--release` se preferir) ;
- `--path .` diz ao `cargo install` para instalar a partir do diretório atual.

No final deste comando, um executável `rgb-lightning-node` estará disponível no seu `$CARGO_HOME/bin/`. Certifique-se que este caminho está no seu `$PATH` para que você possa invocar o comando de qualquer diretório.

### Requisitos de desempenho

Para funcionar, o daemon `rgb-lightning-node` requer a presença e configuração do :


- Um nó `bitcoind`

Cada instância RLN precisará se comunicar com `bitcoind` para transmitir e monitorar suas transações on-chain. Autenticação (login/password) e URL (host/porta) terão de ser fornecidos ao daemon.


- Um **indexador** (Electrum ou Esplora)

O daemon deve ser capaz de listar e explorar transacções na cadeia, em particular para encontrar o UTXO no qual um ativo foi ancorado. Terá de especificar o URL do seu servidor Electrum ou Esplora.


- Um proxy **RGB**

Como visto em capítulos anteriores, o **servidor proxy** é um componente (opcional, mas altamente recomendado) para simplificar a troca de *consignações* entre pares Lightning. Mais uma vez, um URL deve ser especificado.

Os IDs e URLs são introduzidos quando o daemon é _desbloqueado_ através da API. Mais sobre isso mais tarde.

### Lançamento do Regtest

Para uso simples, há um script `regtest.sh` que inicia automaticamente, via Docker, um conjunto de serviços: `bitcoind`, `electrs` (indexador), `rgb-proxy-server`.

![RGB-Bitcoin](assets/en/100.webp)

Isto permite-lhe lançar um ambiente local, isolado e pré-configurado. Cria e destrói contentores e diretórios de dados em cada reinicialização. Começaremos iniciando o arquivo :

```bash
./regtest.sh start
```

Este script irá :


- Crie um diretório `docker/` para armazenar ;
- Execute o `bitcoind` no regtest, bem como o indexador `electrs` e o `rgb-proxy-server` ;
- Esperar até que tudo esteja pronto a utilizar.

![RGB-Bitcoin](assets/en/101.webp)

De seguida, vamos lançar vários nós RLN. Em shells separados, execute, por exemplo (para lançar 3 nós RLN) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RGB-Bitcoin](assets/en/102.webp)


- O parâmetro `--network regtest` indica a utilização da configuração regtest;
- `--daemon-listening-port` indica em qual porta REST o Lightning node escutará as chamadas de API (JSON);
- `--ldk-peer-listening-port` especifica qual porta Lightning p2p deve ser escutada;
- `dataldk0/`, `dataldk1/` são os caminhos para os diretórios de armazenamento (cada nó armazena a sua informação separadamente).

Também pode executar comandos nos seus nós RLN a partir do seu browser:

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Para que um nó possa abrir um canal, deve primeiro ter bitcoins num endereço gerado com o seguinte comando (para o nó n.º 1, por exemplo):

```bash
curl -X POST http://localhost:3001/address
```

A resposta fornecer-lhe-á um endereço.

![RGB-Bitcoin](assets/en/103.webp)

No Regtest `bitcoind`, nós vamos minerar alguns bitcoins. Executar :

```bash
./regtest.sh mine 101
```

![RGB-Bitcoin](assets/en/104.webp)

Enviar os fundos para o endereço do nó gerado acima:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RGB-Bitcoin](assets/en/105.webp)

Em seguida, extrai um bloco para confirmar a transação:

```bash
./regtest.sh mine 1
```

![RGB-Bitcoin](assets/en/106.webp)

### Lançamento da Testnet (sem Docker)

Se quiser testar um cenário mais realista, pode lançar 3 nós RLN na Testnet em vez de na Regtest, apontando para serviços públicos:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Por defeito, se não for encontrada nenhuma configuração, o daemon tentará utilizar o ficheiro :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Com o login :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

Também é possível personalizar estes elementos através da API `init`/`unlock`.

### Emissão de um token RGB

Para emitir um token, começaremos por criar UTXOs "coloríveis":

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RGB-Bitcoin](assets/en/107.webp)

Pode, evidentemente, adaptar a encomenda. Para confirmar a transação, extraímos um :

```bash
./regtest.sh mine 1
```

Agora, podemos criar um ativo RGB. O comando dependerá do tipo de ativo que pretende criar e dos respectivos parâmetros. Aqui estou a criar um token NIA (*Non Inflatable Asset*) chamado "Plan ₿ Academy" com um fornecimento de 1000 unidades. O parâmetro `precision` permite-lhe definir a divisibilidade das unidades.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "Plan ₿ Academy",
"name": "Plan ₿ Academy",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RGB-Bitcoin](assets/en/108.webp)

A resposta inclui o ID do ativo recentemente criado. Não se esqueça de anotar este identificador. No meu caso, é :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RGB-Bitcoin](assets/en/109.webp)

Pode então transferi-lo para a cadeia ou alocá-lo num canal Lightning. É exatamente isso que vamos fazer na próxima secção.

### Abrir um canal e transferir um ativo RGB

Você deve primeiro conectar seu nó a um par na rede Lightning usando o comando `/connectpeer`. No meu exemplo, eu controlo ambos os nós. Então, vou recuperar a chave pública do meu segundo nó do Lightning com este comando:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

O comando devolve a chave pública do meu nó n.º 2:

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RGB-Bitcoin](assets/en/110.webp)

Em seguida, abriremos o canal especificando o ativo relevante (`Plan ₿ Academy`). O comando `/openchannel` permite-lhe definir o tamanho do canal em satoshis e optar por incluir o ativo RGB. Depende do que se pretende criar, mas no meu caso, o comando é :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Saiba mais aqui:


- `peer_pubkey_and_opt_addr`: Identificador do par ao qual nos queremos ligar (a chave pública que encontrámos anteriormente);
- `capacity_sat`: Capacidade total do canal em satoshis ;
- `push_msat`: Quantidade em milisatoshis inicialmente transferida para o par quando o canal é aberto (aqui eu transfiro imediatamente 10.000 sats para que ele possa fazer uma transferência RGB mais tarde) ;
- `asset_amount`: Quantidade de activos RGB a afetar ao canal;
- `asset_id` : Identificador único do ativo RGB envolvido no canal;
- `public`: Indica se o canal deve ser tornado público para encaminhamento na rede.

![RGB-Bitcoin](assets/en/111.webp)

Para confirmar a transação, são extraídos 6 blocos:

```bash
./regtest.sh mine 6
```

![RGB-Bitcoin](assets/en/112.webp)

O canal Lightning está agora aberto e também contém 500 tokens `Plan ₿ Academy` do lado do nó nº 1. Se o nó nº 2 desejar receber tokens `Plan ₿ Academy`, deve gerar uma fatura. Veja como fazer isso:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

Com :


- `amt_msat`: Montante da fatura em milisatoshis (mínimo 3000 sats) ;
- `expiry_sec` : Tempo de expiração da fatura em segundos ;
- `asset_id` : Identificador do ativo RGB associado à fatura ;
- `montante_do_activo`: Montante do ativo RGB a ser transferido com esta fatura.

Em resposta, obterá uma fatura RGB (como descrito nos capítulos anteriores):

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RGB-Bitcoin](assets/en/113.webp)

Vamos agora pagar esta fatura a partir do primeiro nó, que detém o dinheiro necessário com o token `Plan ₿ Academy`:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RGB-Bitcoin](assets/en/114.webp)

O pagamento foi efectuado. Este facto pode ser verificado através da execução do comando :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RGB-Bitcoin](assets/en/115.webp)

Eis como implementar um nó Lightning modificado para transportar activos RGB. Esta demonstração é baseada em :


- Um ambiente regtest (via `./regtest.sh`) ou testnet ;
- Um nó Lightning (`rgb-lightning-node`) baseado num `bitcoind`, um indexador e um `rgb-proxy-server` ;
- Uma série de APIs REST JSON para abrir/fechar canais, emitir tokens, transferir activos através do Lightning, etc.

Graças a este processo :


- As transacções de envolvimento de relâmpagos incluem uma saída adicional (OP_RETURN ou Taproot) com a ancoragem de uma transição RGB;
- As transferências são efectuadas exatamente da mesma forma que os pagamentos Lightning tradicionais, mas com a adição de um token RGB;
- Vários nós RLN podem ser ligados para encaminhar e experimentar pagamentos em vários nós, desde que haja liquidez suficiente em bitcoins e activos RGB no caminho.

O projeto continua na fase alfa. Por conseguinte, recomenda-se vivamente que se limite aos ambientes de teste (regtest, testnet).

As oportunidades abertas por esta compatibilidade LN-RGB são consideráveis: stablecoins na Lightning, DEX layer-2, transferência de tokens fungíveis ou NFTs a um custo muito baixo... Os capítulos precedentes apresentaram a arquitetura concetual e a lógica de validação. Agora tem uma visão prática de como colocar um nó deste tipo em funcionamento, para os seus futuros desenvolvimentos ou testes.

# Seção final

<partId>b0baebfc-d146-5938-849a-f835fafb386f</partId>


## Comentários e classificações

<chapterId>0217e8b0-942a-5fee-bd91-9a866551eff3</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusão

<chapterId>0309536d-c336-56a0-869e-a8395ed8d9ae</chapterId>

<isCourseConclusion>true</isCourseConclusion>