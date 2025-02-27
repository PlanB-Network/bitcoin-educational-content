---
name: Construir com Elementos e Rede Líquida
goal: Aprender a utilizar e a desenvolver com a plataforma blockchain de código aberto Elements e as suas principais funcionalidades
objectives: 

  - Compreender os conceitos fundamentais da plataforma de blockchain Elements e das sidechains Liquid.
  - Aprenda a configurar e executar nós do Elements para configurações autónomas e sidechain.
  - Ganhar experiência prática com a assinatura de blocos federados e o Federated 2-Way Peg.
  - Configurar e gerir ambientes de cadeia de blocos seguros e eficientes para casos de utilização no mundo real.

---
# Construir sobre o líquido e os elementos

Descubra as caraterísticas e capacidades avançadas do Liquid e do Elements e saiba como utilizar eficazmente estas ferramentas para melhorar os seus projectos de desenvolvimento. Este treinamento fornece uma base teórica e prática completa, permitindo que você domine recursos como Transações Confidenciais, Ativos Emitidos e Assinatura de Bloco Federado.

O Liquid, baseado na estrutura Elements, foi concebido para melhorar a privacidade, a escalabilidade e a funcionalidade das soluções financeiras e técnicas. Neste curso, ganhará experiência prática com a emissão e gestão de activos, o Federated 2-Way Peg e a utilização de ferramentas como elementsd e elements-cli, permitindo-lhe criar soluções inovadoras adaptadas às suas necessidades.

Este curso foi concebido para programadores de todos os níveis de experiência. Os utilizadores principiantes e intermédios encontrarão explicações acessíveis e exemplos práticos, enquanto os utilizadores avançados podem aprofundar os detalhes técnicos e as funcionalidades menos conhecidas do Liquid e do Elements.

Junte-se a nós para elevar as suas competências, desbloquear todo o potencial do Liquid e do Elements e criar ferramentas impactantes para o futuro da inovação Liquid.

+++
# Introdução

<partId>8f34de87-6e9a-4e3b-a326-50fc7c1803b3</partId>

## Introdução aos cursos

<chapterId>a721398e-7040-4edd-be53-b485ea759fa9</chapterId>

![Video](https://youtu.be/gkQfnwYLyI0?si=H6cIPhgZaSAwHaHI)

O objetivo da Elements Academy é apresentar e explicar os principais conceitos do Elements, a plataforma de código aberto na qual o Liquid foi desenvolvido. No final do curso, você deve ter uma boa compreensão dos principais recursos do Elements, como Transações Confidenciais e Ativos Emitidos, e os processos envolvidos na execução do Elements Core.

Cada secção terá lições com texto explicativo e um vídeo que termina com um questionário. O número de perguntas está relacionado com o tamanho do tópico anterior. A secção 10 resume o conteúdo do curso e termina com um teste de maior dimensão.

Quaisquer perguntas, pedidos de informações adicionais ou dúvidas sobre as respostas do questionário podem ser dirigidas ao seu professor James Dorfman.

## Visão geral dos elementos

<chapterId>7a7f2712-5300-4a6d-b1ed-05eab731bc35</chapterId>

![Video](https://youtu.be/ns-JLGdkNig?si=fmWye_boRSvVF1Bt)

A Elements é uma plataforma de blockchain de código aberto, com capacidade para sidechain, que fornece acesso a funcionalidades poderosas desenvolvidas por membros da comunidade, tais como Transacções Confidenciais e Activos Emitidos.

O Elements é, na sua essência, um protocolo que permite a formação de um consenso em torno do histórico de transacções e das regras que regem a transferência e a criação de activos armazenados num livro-razão distribuído da cadeia de blocos.

Mais informações sobre o Elements podem ser encontradas no sítio Web do Projeto Elements (https://elementsproject.org/), no blogue oficial do Liquid (https://blog.liquid.net/) e no portal do programador (https://liquid.net/devs).

### Elementos

Lançado em 2015, o Elements reduz os custos internos de desenvolvimento e pesquisa e aproveita a mais recente tecnologia de blockchain, abrindo muitos novos casos de uso para implementação. Uma blockchain baseada na Elements pode funcionar como uma Blockchain autónoma ou ser ligada a outra e executada como uma Sidechain. A execução da Elements como uma Sidechain permite que os activos sejam transferidos de forma verificável entre diferentes blockchains.

Construído sobre e estendendo a base de código do Bitcoin, permite aos programadores familiarizados com a API do Bitcoin criar rapidamente e de forma económica cadeias de blocos funcionais e testar projectos de prova de conceito. O facto de ser construído sobre a base de código Bitcoin também permite que o Elements funcione como um banco de ensaio para alterações ao próprio protocolo Bitcoin.

Algumas das principais caraterísticas dos Elementos são apresentadas de seguida.

#### Transacções confidenciais

Por defeito, todos os endereços nos Elementos são ocultados utilizando Transacções Confidenciais. A ocultação é o processo pelo qual o montante e o tipo de ativo que está a ser transferido é criptograficamente escondido de todos, exceto dos participantes e daqueles a quem estes escolhem revelar a chave de ocultação.

#### Activos emitidos

Os Activos Emitidos nos Elementos permitem que vários tipos de activos sejam emitidos e transferidos entre os participantes da rede. Um Ativo Emitido também beneficia de Transacções Confidenciais e pode ser reemitido ou destruído por qualquer pessoa que possua o token de reemissão relevante.

#### Peg de 2 vias federado

A Elements é uma plataforma de blockchain de uso geral que também pode ser "ligada" a uma blockchain existente (como a Bitcoin) para permitir a transferência bidirecional de activos de uma cadeia para a outra. A implementação da Elements como uma sidechain permite-lhe contornar algumas das propriedades inerentes à cadeia principal, mantendo um bom grau de segurança proporcionado pelos activos protegidos na cadeia principal.

#### Blocos assinados

A Elements utiliza uma Federação Forte de signatários, denominados Block Signers, que assinam e criam blocos de forma fiável e atempada. Isto elimina a latência de transação do processo de mineração PoW, que está sujeito a uma grande variação de tempo de bloco devido à sua distribuição aleatória de poisson. O processo de assinatura de blocos federados consegue uma criação de blocos fiável sem introduzir a necessidade de confiança de terceiros ou de mineração baseada em algoritmos computacionais.

O Elements adiciona todas estas funcionalidades à base de código Bitcoin Core, alargando a capacidade do protocolo da cadeia principal e permitindo novos casos de utilização empresarial quando implementado como uma cadeia lateral ou como uma solução de cadeia de blocos autónoma.

# Elemento

<partId>ac68d611-be84-432f-a3a8-620d310e131c</partId>

## Como funcionam os elementos

<chapterId>05d88877-58b0-455b-9ae6-a72d19070525</chapterId>

![Video](https://youtu.be/v0lzmfH81AY?si=V-xDWfmDLKyBcdPs)

A Elements fornece uma solução técnica para os problemas que os utilizadores da cadeia de blocos enfrentam diariamente: latência das transacções, falta de privacidade e risco de fungibilidade.

A Elements supera estes problemas através da utilização da assinatura de blocos federados e das transacções confidenciais.

Ao contrário da rede Bitcoin, o processo de assinatura de blocos na Elements não depende de Assinaturas Multipartidárias de Associação Dinâmica (DMMS) e Prova de Trabalho (PoW). Em vez disso, a Elements usa uma Federação Forte de signatários, chamados Block Signers, que podem assinar e criar blocos de forma fiável e atempada. Isto elimina a latência de transação do processo de mineração PoW, que está sujeito a uma grande variação de tempo de bloco devido à sua distribuição aleatória de poisson. O processo de assinatura de blocos federados consegue uma criação de blocos fiável sem introduzir a necessidade de confiança de terceiros.

A Elements pode funcionar como uma sidechain de outra blockchain, como a Bitcoin, ou como uma blockchain autónoma sem dependências de outras redes.

Quando usada como uma sidechain, a Strong Federation também contém membros que permitem a transferência segura e controlada de activos entre uma cadeia principal e uma sidechain de Elementos. A transferência controlada de activos é chamada de Federated 2-Way Peg e os membros que desempenham o papel de transferência de activos são chamados Watchmen.

Os processos envolvidos no funcionamento de uma rede Elements e os papéis dos participantes na rede são importantes para compreender o funcionamento da Elements.

Quer seja implementado como uma sidechain ou uma blockchain autónoma, o Elements utiliza Federações Fortes de Assinantes de Blocos para produzir blocos.

### Federações fortes

A Elements usa um modelo de consenso proposto pela primeira vez pela Blockstream, chamado Strong Federations. Uma Federação Forte não precisa de Prova de Trabalho (PoW) e, em vez disso, baseia-se nas acções colectivas de um grupo de participantes mutuamente desconfiados, chamados Funcionários.

Os papéis que um Funcionário pode cumprir numa Federação Forte são: Assinantes de Bloco e Vigias. Os Assinantes de Bloco são necessários se executar os Elementos no modo sidechain ou no modo blockchain autónomo, enquanto os Vigilantes só são necessários numa configuração sidechain.

As acções que um membro de uma Federação Forte pode realizar estão divididas entre duas funções distintas, de forma a aumentar a segurança e limitar os danos que um atacante pode causar.

Quando combinados, os papéis destes participantes permitem que a Elements forneça tanto a criação rápida de blocos (confirmação mais rápida e final da transação) como activos transferíveis e garantidos (activos indexados diretamente ligados a outra cadeia de blocos).

Pode ler o documento técnico sobre as Federações Fortes aqui: https://blockstream.com/strong-federations.pdf

### Assinantes do bloco

Uma cadeia de blocos como a da Bitcoin é alargada quando qualquer pessoa que faça parte de um grupo dinâmico de signatários de blocos alarga a cadeia, demonstrando a prova do trabalho efectuado. A natureza dinâmica do conjunto introduz os problemas de latência inerentes a esses sistemas.

Ao utilizar um conjunto fixo de signatários, um modelo Federado substitui o conjunto dinâmico por um conjunto conhecido, um esquema de múltiplas assinaturas. A redução do número de participantes necessários para estender a cadeia de blocos aumenta a velocidade e a escalabilidade do sistema, enquanto a validação por todas as partes garante a integridade do histórico de transacções.

A assinatura federada de blocos consiste em várias fases:


- Passo 1 - Os signatários de blocos propõem blocos candidatos de forma rotativa a todos os outros signatários de blocos participantes.
- Passo 2 - Cada signatário de bloco assinala a sua intenção comprometendo-se previamente a assinar um determinado bloco candidato.
- Passo 3 - Se o limiar de pré-compromisso for atingido, cada signatário do bloco assina o bloco.
- Passo 4 - Se o limiar de assinatura (que pode ser diferente do limiar do passo 3) for atingido, o bloco é aceite e enviado para a rede. A Federação Forte chegou a um consenso sobre o último bloco de transacções.
- Passo 5 - O bloco seguinte é então proposto pelo signatário de bloco seguinte no round-robin e o processo repete-se.

Como a geração de blocos de uma Federação Forte não é probabilística e se baseia num conjunto fixo de signatários, nunca estará sujeita a reorganizações de vários blocos. Isto permite uma redução significativa no tempo de espera associado à confirmação de transacções. Também elimina o incentivo para minerar com fins lucrativos (ou seja, as recompensas do bloco) e substitui-o por um incentivo para participar produtivamente numa rede em que todos os participantes têm o mesmo objetivo comum; assegurar que a rede continua a funcionar de uma forma que é benéfica para todos. Isto é feito sem introduzir um único ponto de falha ou requisitos de confiança mais elevados.

### Elementos como uma cadeia lateral - Watchmen e o Peg de 2 vias federado

Quando executado como uma sidechain, alguns membros da Strong Federation têm um papel adicional a cumprir, o de Watchmen. Os vigilantes são responsáveis pela transferência de activos para dentro e para fora de uma sidechain da Elements, processos conhecidos como `Peg-In` e `Peg-Out`.

Para que uma sidechain funcione de forma fiável, deve permitir que os participantes verifiquem que o fornecimento de activos é controlado e verificável. Uma sidechain da Elements usa um 2-Way Federated Peg para permitir a transferência bidirecional de activos dentro e fora de uma blockchain da Elements. Isto satisfaz os requisitos de emissão comprovável e transferências entre cadeias.

O recurso Federated 2-way Peg permite que um ativo seja interoperável com outras blockchains e representativo do ativo nativo de outra blockchain. Ao associar a sua cadeia de blocos a outra, pode alargar as capacidades da cadeia principal e ultrapassar algumas das suas limitações inerentes.

A um nível elevado, as transferências para a sidechain ocorrem quando alguém envia activos da mainchain para um endereço controlado por uma carteira Watchmen com várias assinaturas. Isto congela efetivamente os activos na cadeia principal. A Watchmen valida então a transação e liberta a mesma quantidade do ativo associado na sidechain. Os activos libertados são enviados para uma carteira sidechain que pode provar a reivindicação dos activos originais da mainchain. Este processo move efetivamente os activos da cadeia principal para a sidechain.

Para transferir activos de volta para a cadeia principal, um utilizador faz uma transação especial de peg-out na cadeia lateral. Esta transação é verificada pelos Vigilantes que, em seguida, assinam uma despesa de transação a partir da carteira multi-assinatura que controlam na cadeia principal. Um número limite de participantes na federação deve assinar antes que a transação na cadeia principal se torne válida. Quando os Vigilantes enviam um ativo de volta para a cadeia principal, também destroem o montante correspondente na cadeia lateral, transferindo efetivamente os activos entre cadeias de blocos.

## Configurar e executar elementos

<chapterId>cc806e5a-81ab-457b-9531-9f863120a019</chapterId>

![Video](https://youtu.be/Frr_OjTEPAM?si=iq5XonJyQk8S5OAu)

Como o Elements é baseado na base de código do Bitcoin, os componentes que formam uma rede funcional são muito semelhantes.

O software do nó Elements chama-se `elementsd` e é executado como um daemon na máquina do utilizador. Um daemon (ou serviço no Windows) é um programa que corre como um serviço de fundo sem necessitar do controlo direto de um utilizador com sessão iniciada.

Nota: Ao longo deste documento, iremos sempre referir-nos ao elementsd como a versão daemon, mas tudo pode ser feito com o elements-qt, desde que a opção server esteja activada.

O daemon Elements liga-se a outros nós da rede para poder trocar dados de transacções e blocos, validando e alargando a sua cópia local da cadeia de blocos da rede.

O software Elements também consiste num programa cliente chamado `elements-cli` que lhe permite enviar comandos Remote Procedure Call (RPC) para o elementsd a partir da linha de comandos. Isto pode ser usado para consultar o saldo de uma carteira, visualizar dados de transacções ou blocos ou transmitir uma transação, por exemplo. Esta configuração deve ser familiar para qualquer um que tenha usado os equivalentes do Bitcoin; bitcoind e bitcoin-cli.

Como um nó Elements pode ser configurado passando parâmetros no arranque ou através de um ficheiro de configuração, é possível ter mais do que uma instância a correr na mesma máquina. Isto é útil para fins de teste e desenvolvimento, uma vez que pode configurar a sua própria rede local numa única máquina, com cada nó Elements a ter a sua própria cópia dos dados da blockchain, gerindo o seu próprio conjunto de transacções válidas não confirmadas e ouvindo pedidos RPC em diferentes portas.

### O repositório de código e a comunidade dos elementos

O Elements é um projeto de código aberto e o seu código fonte pode ser encontrado no repositório Elements GitHub em https://github.com/ElementsProject/elements. O repositório contém o código-fonte dos programas elementsd e elements-cli, juntamente com ferramentas de instalação e compilação de suporte, um conjunto de testes e alguma documentação instrucional.

Para complementar o repositório de código, existe também o site https://elementsproject.org, um recurso centrado na comunidade que contém explicações sobre o que é o Elements, como funciona e uma secção de tutorial abrangente. O tutorial centra-se na aprendizagem sobre o Elements seguindo exemplos de linha de comandos e mostra como construir aplicações simples de ambiente de trabalho e da Web com base nele. O site também lista os fóruns de discussão populares da comunidade Elements e está alojado no GitHub, permitindo contribuições da comunidade para o conteúdo do site.

Para executar o Elements na sua máquina, terá primeiro de clonar (descarregar uma cópia) o código fonte, instalar quaisquer dependências que o código tenha e, finalmente, construir os executáveis daemon e cliente. O software Elements está então pronto para ser configurado e executado.

## Configuração de nós e redes

<chapterId>df1ec0aa-84ea-4149-af7a-b4523d67e1d9</chapterId>

As definições de configuração podem ser transmitidas a um nó Elements no arranque, a fim de alterar a forma como funciona, valida os dados, se liga a outros nós e inicializa os seus dados blockchain.

As configurações são carregadas a partir do arquivo `elements.conf` designado ou passadas como parâmetros através da linha de comando.

Alguns dos aspectos podem ser alterados utilizando estes parâmetros:


- O nome do ativo predefinido utilizado nas implementações de uma cadeia de blocos autónoma.
- O número do ativo inicial criado.
- O ativo a ser utilizado para pagar taxas de transação na rede.
- O local de armazenamento dos ficheiros de dados da cadeia de blocos.
- As credenciais RPC usadas para se conectar a um nó Bitcoin.
- O limiar `n de m` a cumprir e as chaves públicas válidas que podem assinar blocos.
- O script que precisa de ser satisfeito para transferir activos para dentro e para fora de uma sidechain.
- Se deve conectar-se a um nó Bitcoin como uma sidechain ou não.

Muitos destes fazem parte das regras de consenso da rede, por isso é importante que sejam aplicados em todos os nós no arranque. Algumas podem ser alteradas depois de uma cadeia ter sido inicializada, mas outras precisam de ser corrigidas depois de serem usadas para inicializar uma cadeia.

A utilização de parâmetros será abordada mais tarde no curso, à medida que se relaciona com cada secção.

### Operações básicas usando a linha de comando

Este curso mostrará exemplos que utilizam o programa `elements-cli` para fazer chamadas RPC para um ou mais nós do Elements. Isto é feito a partir de uma sessão de terminal e para tornar os comandos mais breves será utilizado um `alias`. Por esta convenção, quando vir algo como os seguintes comandos:

```bash
e1-dae
e1-cli getnewaddress
```

O `e1-dae` e o `e1-cli` são na verdade um atalho tipográfico que faz uso do recurso `alias` do terminal. O `e1-dae` e o `e1-cli` serão realmente substituídos quando o comando for executado e o comando que será executado será semelhante a:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir1
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir1 getnewaddress
```

O que vemos acima é uma chamada para iniciar o daemon do Elements e uma chamada para os programas elements-cli localizados no diretório `$HOME/elements/src` e um valor para o parâmetro `datadir`. O parâmetro `datadir` permite-nos dizer às instâncias daemon e cliente onde localizar os seus ficheiros de configuração e, no caso do daemon, onde armazenar a sua cópia da blockchain. Como eles compartilham um arquivo de configuração, o cliente será capaz de fazer chamadas RPC para o daemon.

Executando o comando acima novamente, mas com um valor `datadir` diferente, podemos iniciar mais de uma instância do Elements, cada uma com sua própria cópia separada da blockchain e configurações. Por essa convenção, usaremos os apelidos `e2-dae` e `e2-cli` no curso para nos referirmos a um diretório datadir diferente do e1. Então o exemplo acima para nossa segunda instância `e2` seria:

```
$HOME/elements/src/elementsd -datadir=$HOME/elementsdir2
$HOME/elements/src/elements-cli -datadir=$HOME/elementsdir2 getnewaddress
```

Isto permite-nos realizar todo o tipo de operações, como a transação de activos entre nós, a emissão de activos e a verificação da utilização de blinding em transacções confidenciais entre diferentes nós da mesma rede.

# Utilização do elemento Caso de utilização prático

<partId>3f31a30a-957a-4813-b5fe-5dccbb5366f3</partId>

## Transacções confidenciais

<chapterId>263b1c5b-59ed-49e7-b811-95c354f41eae</chapterId>

![Video](https://youtu.be/-by2xBtXQeE?si=7bLo_geGn3qh7MXN)

Nesta secção, aprenderá a utilizar a funcionalidade Transacções Confidenciais dos Elementos.

Todos os endereços no Elements são, por defeito, ocultados utilizando Transacções Confidenciais, que mantêm o montante e o tipo de activos transferidos visíveis apenas para os participantes na transação (e para aqueles a quem estes optam por revelar a chave de ocultação), garantindo ainda criptograficamente que não podem ser gastas mais moedas do que as disponíveis.

### Endereços confidenciais e transacções confidenciais

Por defeito, quando se cria um novo endereço no Elements utilizando o comando `getnewaddress`, este é criado como um endereço confidencial.

Para demonstrar as transacções confidenciais, vamos fazer com que e2 envie alguns fundos para si próprio e depois tente ver a transação de e1. Isto demonstrará a natureza confidencial das transacções no Elements.

Todos os novos endereços gerados por um nó do Elements são confidenciais por defeito. Podemos demonstrar isto fazendo com que o e2 gere um novo endereço.

```
e2-cli getnewaddress
```

Note-se que o endereço começa por e1. Isto identifica-o como um endereço confidencial. A análise do endereço com mais pormenor, utilizando o comando getaddressinfo, mostra mais detalhes sobre o endereço.

```
e2-cli getaddressinfo <address>
```

Pode ver que existe uma propriedade confidential_key que nos diz que se trata de um endereço confidencial.

A confidential_key é a chave pública cega, que é adicionada ao próprio endereço confidencial. Esta é a razão pela qual um endereço confidencial é tão longo.

Tem também um endereço não confidencial associado. Se pretender utilizar transacções regulares, não confidenciais, na Elements, os activos devem ser enviados para este endereço em vez do endereço com o prefixo lq1.

Podemos agora fazer com que e2 envie alguns fundos para o endereço que gerou. Isto demonstrará mais tarde que e1, como não é uma das partes envolvidas na transação, não poderá ver os detalhes da transação.

```
e2-cli sendtoaddress <address>
```

Anotar o ID da transação. Confirmar a transação.

```
e2-cli -generate 101
```

Analisando a transação em que o e2 enviou alguns fundos para si próprio, na perspetiva do próprio e2.

```
e2-cli gettransaction <txid>
```

Percorrendo os detalhes da transação, pode ver que o e2 pode visualizar os montantes enviados e recebidos, bem como o ativo transaccionado. Também é possível ver as propriedades amountblinder e assetblinder, que são usadas para ocultar os detalhes de outros nós não envolvidos na transação.

Para verificar os detalhes da mesma transação a partir de e1, precisamos primeiro de obter os detalhes brutos da transação.

```
e1-cli getrawtransaction <txid>
```

Isso retorna detalhes brutos da transação. Se olhar para a secção vout, verá que existem três instâncias. As duas primeiras instâncias são os valores de recebimento e de alteração, e a terceira é a taxa de transação. Destes três montantes, a comissão é o único em que é possível ver um valor, uma vez que a própria comissão é sempre apresentada sem ocultação na secção Elements.

### Chaves cegas

O que as duas primeiras secções vout mostram são "intervalos cegos" dos montantes de valor e os dados de compromisso que funcionam como prova do montante real e do tipo de ativo transaccionado.

Mesmo que importássemos a chave privada de e2 para a carteira de e1, esta continuaria a não conseguir ver os montantes e o tipo de activos transaccionados, porque continua a não ter conhecimento da chave cega utilizada por e2. Vamos provar isto importando a chave privada usada pela carteira de e2 para a de e1. Primeiro precisamos de exportar a chave de e2

```
e2-cli dumpprivkey <address>
```

Em seguida, importe-o para e1.

```
e1-cli importprivkey <privkey>
```

Agora podemos provar que e1 ainda não consegue ver os valores.

```
e1-cli gettransaction <txid>
```

De facto, mostra 0 como o valor de tx quando na realidade era 1.

Para podermos ver o valor efetivo, não cegado, precisamos da chave de cegueira. Para o fazer, começamos por exportar a chave de cegueira de e2.

```
e2-cli dumpblindingkey <address>
```

Em seguida, importe-o para e1.

```
e1-cli importblindingkey <address> <blinding key>
```

Agora, quando obtivermos os detalhes da transação de e1.

```
e1-cli gettransaction <txid>
```

Mostra que, com a chave cega importada, podemos agora ver o valor real de 1 na transação.

Nesta secção vimos que a utilização de uma chave de ocultação esconde o montante e o tipo de activos numa transação e que, ao importar a chave de ocultação correta, podemos revelar esses valores. Na prática, uma chave de ocultação pode, por exemplo, ser dada a um auditor, caso seja necessário verificar os montantes e tipos de activos detidos por uma parte. A funcionalidade Transacções Confidenciais da Elements também permite a realização de "provas de intervalo". As provas de intervalo podem provar que um montante de um ativo é detido dentro de um determinado intervalo, sem a necessidade de expor o montante real em si.

Vimos também que as Transacções Confidenciais são opcionais, mas activadas por defeito quando é gerado um novo endereço.

É tudo por esta lição; boa sorte no teste e até à próxima!

## Activos emitidos

<chapterId>c33c7020-5975-457a-99db-4f8b90d1fa1c</chapterId>

![Video](https://youtu.be/XnY4WZUNSs4?si=dG8I5OoSh_0EBdvL)

Nesta secção, aprenderá a utilizar a funcionalidade Activos emitidos dos Elementos.

Os activos emitidos permitem que vários tipos de activos sejam emitidos e transferidos entre os participantes da rede Elements. Qualquer nó da rede pode emitir os seus próprios activos. As emissões podem representar a propriedade fungível de qualquer ativo, incluindo vales, cupões, moedas, depósitos, obrigações, acções, etc. Os Activos Emitidos abrem a porta para a construção de trocas sem confiança, opções e outros contratos inteligentes avançados envolvendo activos auto-emitidos.

Um Ativo Emitido também beneficia de Transacções Confidenciais e pode ser reemitido por qualquer pessoa que detenha o token associado.

O primeiro passo é que precisamos de acesso a dois nós Elements, a que chamaremos e1 e e2. Os nós tiveram as suas cadeias de blocos reiniciadas e o ativo predefinido foi dividido entre eles.

Os dois nós estão na mesma rede local e estão ligados um ao outro, pelo que partilham as mesmas transacções no seu mempool de transacções e blockchains idênticas. Apesar de estarem a correr na mesma máquina, é importante notar que não partilham os mesmos ficheiros blockchain. Cada nó gere a sua própria cópia local da blockchain, que contém o mesmo histórico de transacções porque estão em consenso e aderem às mesmas regras de protocolo que os outros.

Comecemos por verificar a visão de cada nó sobre as emissões de activos existentes na rede.

Isto é feito utilizando o comando listissuances.

```
e1-cli listissuances
e2-cli listissuances
```

Como pode ver, ambos os nós mostram o mesmo histórico de emissão. Ambos apresentam um ativo, a emissão inicial de 21 milhões de Bitcoin que foram criados na inicialização da cadeia. Pode ver a identificação hexadecimal do ativo nos resultados da execução do comando acima e também a etiqueta atribuída ao ativo, que é "bitcoin".

Vale a pena notar que o ativo predefinido recebe sempre uma etiqueta quando a cadeia é inicializada. Quando emite os seus próprios activos, pode definir etiquetas para eles, o que faremos em breve. Antes de o fazermos, precisamos de emitir o nosso próprio ativo.

Vamos fazer com que o e1 emita o novo ativo. Isto é feito utilizando o comando issueasset.

```
e1-cli issueasset 100 1 false
```

`issueasset` aceita 3 parâmetros.

O montante do novo ativo a emitir, nós utilizámos 100. A quantidade de tokens a criar (os tokens são utilizados para reemitir quantidades de um ativo), dos quais escolhemos 1. O parâmetro final diz à Elements para criar a emissão de activos como cega ou não cega. Utilizaremos a opção sem ocultação, uma vez que pretendemos visualizar os montantes de emissão do e2 num minuto, pelo que introduziremos false.

A execução do comando retorna dados sobre a emissão. Estes incluem o ID da transação, do qual pode tirar uma cópia para utilização posterior, o valor hexadecimal único do ativo e o valor hexadecimal único do token do ativo.

Gerar um bloco para confirmar a transação de emissão.

```
e1-cli -generate 1
```

Execute novamente o comando `listissuances` em e1.

```
e1-cli listissuances
```

Isso mostra-nos que e1 está agora ciente de 2 emissões, a emissão inicial de Bitcoin e o nosso ativo recém-emitido, do qual podemos ver 100. Note-se o valor hexadecimal do novo ativo e que não existe uma etiqueta de ativo associada, tal como acontece com a emissão de bitcoin.

Verificar novamente a lista de emissões conhecidas do e2.

```
e2-cli listissuances
```

Isto mostra-nos que e2 não tem conhecimento da emissão de activos que e1 fez. Só pode ver a emissão inicial de bitcoin que já podia ver.

Isto deve-se ao facto de e2 desconhecer, e não estar a observar, o endereço para o qual o novo ativo foi enviado quando foi emitido por e1.

Vale a pena notar que, embora e2 não possa ver a emissão em si, e1 poderia enviar a e2 parte do ativo. O novo ativo apareceria então como um saldo disponível na carteira de e2, mesmo que este não tenha conhecimento da emissão original.

Para que o e2 possa ver a emissão efectiva (e, portanto, o montante emitido), temos de adicionar o endereço ao e2 como endereço vigiado.

Para o fazer, precisamos de descobrir o endereço para o qual o ativo foi enviado. Para isso, utilizaremos o ID da transação que copiámos anteriormente e faremos com que e1 recupere os detalhes dessa transação para que possamos descobrir o endereço correto a adicionar à lista de observação de carteiras de e2.

```
e1-cli gettransaction <the-issuance-transaction-id>
```

Passando pelo hexadecimal dos dados da transação, verá o endereço que recebeu 100 do nosso novo ativo, identificado pelo seu valor hexadecimal.

Pegue no endereço e copie-o para o podermos importar para o e2.

Agora vamos importar esse endereço para o e2. Para o fazer, utilizamos o comando importaddress.

```
e2-cli importaddress <the-issued-to-address>
```

Se verificarmos agora a lista de emissões do e2.

```
e2-cli listissuances
```

Pode ver que o nosso ativo recentemente emitido está agora incluído na lista. O nó e2 também é capaz de determinar o valor do ativo que foi emitido, juntamente com o valor do token associado, uma vez que a emissão foi uma emissão não cega. Para ativar a utilização da ID do ativo para mapeamento de nomes na Elements, primeiro pare a Elements.

```
e1-cli stop
```

Em seguida, reinicie-o com um parâmetro adicional que mapeia o hexadecimal de um ativo para a etiqueta fornecida. Isto permite ao nó mostrar-nos dados sobre o ativo num formato mais legível para humanos. Pode adicionar isto ao final do elements.conf se preferir, assim não precisa de adicionar o argumento ao daemon de cada vez que o inicia. Por exemplo:

```
assetdir=5186d0bc8ed15e6ef85571bd2d8070573adf0e06fd4507082694526975ce4f35:My new asset (MNA)
```

Mas vamos utilizar aqui o método do argumento.

```
e1-dae -assetdir=<assetid-here>:<name-of-the-new-asset>
```

Consultar novamente o nó para obter uma lista de emissões.

```
e1-cli listissuances
```

Isto mostra-nos que o mapeamento do valor hexadecimal do ativo para a sua etiqueta está a funcionar. Verificando novamente a lista de emissões do nó e2.

```
e2-cli listissuances
```

Pode ver-se que o nó e2 não tem acesso a esta etiqueta, porque as etiquetas só estão disponíveis para o nó que as definiu. De facto, podemos atribuir uma etiqueta diferente ao mesmo ativo hexagonal em e2 do que em e1. Primeiro, pare o nó e2.

```
e2-cli stop
```

Reiniciar com uma etiqueta diferente atribuída ao hexágono do nosso novo ativo.

```
e2-dae -assetdir=<assetid-here>:<another-name-for-the-new-asset>
```

Listagem de emissões da e2.

```
e2-cli listissuances
```

As etiquetas dos activos são locais para cada nó, apenas o hexágono do ativo é reconhecido por outros nós da rede.

O mapeamento da etiqueta para o hexágono do ativo é útil quando se realizam acções como transacções e consultas do saldo da carteira, uma vez que permite uma forma abreviada de fazer referência a um ativo. Por exemplo, se quisermos enviar parte do nosso novo ativo (um montante de 10) de e1 para e2 sem utilizar a etiqueta.

Primeiro, precisamos de obter um endereço para o qual enviar o ativo.

```
e2-cli getnewaddress
```

Em seguida, utilize o comando sendtoaddress.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <asset-id-here>
```

Confirmar a transação gerando um bloco.

```
generate 1
```

Verificar se o ativo foi recebido na e2.

```
e2-cli getwalletinfo
```

Podemos ver que o ativo foi efetivamente recebido.

Note-se que e2 mapeia o hexadecimal do ativo recebido e apresenta-o utilizando a sua própria etiqueta. Uma forma mais fácil de fazer a mesma coisa seria utilizar a etiqueta do ativo de e1 ao enviar.

```
e1-cli sendtoaddress <address> 10 "" "" false false 1 UNSET false <name-of-the-new-asset>
```

Nos bastidores, o Elements mapeia etiquetas locais para valores hexadecimais para ajudar a simplificar a utilização de activos emitidos.

Nesta secção vimos como emitir e etiquetar activos. Na próxima secção, veremos como reemitir e destruir quantidades de um ativo emitido.

## Reemissão de activos

<chapterId>78751b21-1dc8-4877-a406-e71bc80a95b0</chapterId>

![Video](https://youtu.be/5em79YHtYk0?si=rhponm6Hw9AB6RJp)

Nesta secção, aprenderá como emitir mais de um ativo já emitido e também como destruir uma determinada quantidade de um ativo emitido.

A necessidade de reemitir (criar mais) de um ativo ou destruir uma quantidade do ativo é algo que provavelmente ocorrerá quando o ativo representa algo que não tem um fornecimento fixo. Isto pode aplicar-se a activos que representam ouro detido num cofre, por exemplo; à medida que as unidades de ouro entram e saem do cofre, o ativo que representa o fornecimento do cofre tem de ser ajustado para cima ou para baixo em conformidade.

A reemissão de um montante de um ativo requer a propriedade do token associado que foi criado juntamente com o ativo quando este foi inicialmente emitido.

Ao criar mais de um ativo, não importa qual o nó que emitiu o ativo em primeiro lugar, desde que o nó que está a reemitir uma quantidade de um ativo esteja na posse do que é normalmente chamado o token de reemissão do ativo. Veremos como criar inicialmente o token de reemissão, como usá-lo para reemitir uma quantidade de um ativo e também como transferir o token de reemissão para outros nós, para que eles também tenham permissão para reemitir o ativo.

Precisamos de aceder a dois nós Elements, a que chamaremos e1 e e2. Os nós tiveram as suas cadeias de blocos reiniciadas e o ativo predefinido foi dividido entre eles.

Faremos com que e1 emita um montante de 100 de um novo ativo e crie 1 token de reemissão para esse mesmo ativo. Vamos criar a emissão como não cega para simplificar o exemplo. Vamos então emitir o ativo e o seu token de reemissão associado.

```
e1-cli issueasset 100 1 false
```

Note o ID do ativo e também o do token (de reemissão).

Como mais tarde iremos reemitir mais do ativo a partir do e2, teremos de tomar nota do ID da transação em que o ativo foi emitido e utilizá-lo para importar o endereço para o qual o ativo foi enviado.

Confirmar a transação.

```
e1-cli -generate 1
```

Vamos agora verificar os detalhes da transação utilizando o comando gettransaction:

```
e1-cli gettransaction <txid>
```

Passando o hexágono dos dados da transação, verá que na transação e1 recebeu 1 token de reemissão e 100 do ativo associado.

Faça uma cópia do endereço para podermos importá-lo para o e2.

E agora importando o endereço para a carteira do e2.

```
e2-cli importaddress <address>
```

Podemos agora ver que tanto e1 como e2 têm conhecimento da emissão de activos.

```
e1-cli listissuances
e2-cli listissuances
```

Atualmente, e1 detém um montante do ativo e 1 ficha de reemissão, mas e2 não.

```
e1-cli getwalletinfo
```

Observe também que e1 tem menos do ativo padrão do que antes porque pagou uma pequena quantia para cobrir as taxas de transação. Este montante deverá ser cobrado por e1 quando o bloco criado for vencido a mais de 100 blocos de profundidade.

```
e2-cli getwalletinfo
```

Como e1 detém o token de reemissão, pode reemitir mais. Isto é feito utilizando o comando reissueasset. Vamos fazer com que e1 reemita mais 100 do ativo.

```
e1-cli reissueasset <asset-id> 100
```

O controlo da reemissão funcionou.

```
e1-cli getwalletinfo
```

Pode ver-se que e1 detém agora 200 do ativo, como esperado.

Como o e2 não detém um montante do token de reemissão, receberá um erro se tentar reemitir o ativo.

```
e2-cli reissueasset <asset-id> 100
```

Anote a mensagem de erro.

Podemos ver os detalhes da reemissão a partir de e1 utilizando o comando listissuances.

```
e1-cli listissuances
```

Note-se o sinal `is_reissuance`.

Se agora enviarmos à e2 um montante do token de reemissão, eles próprios poderão reemitir um montante do ativo. Primeiro, precisamos de um endereço para o enviar. Vale a pena notar que o token de reemissão é tratado da mesma forma que qualquer outro ativo dentro dos elementos ao enviar e exibir saldos e que também pode ser dividido em denominações mais pequenas como qualquer outro ativo, por isso não precisamos de enviar o 1 token de reemissão para a e2 para que esta possa reemitir o ativo. Qualquer denominação será suficiente. Geração de um endereço para o e2 receber o token de reemissão.

```
e2-cli getnewaddress
```

Em seguida, envia uma fração do RIT de e1 para e2.

```
e1-cli sendtoaddress <address-of-e2> 0.1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confirmar a transação.

```
e1-cli -generate 1
```

Podemos agora ver que e2 mantém os 0,1 que lhe foram enviados.

```
e2-cli getwalletinfo
```

Isto significa que a e2 pode agora reemitir mais do ativo associado ao RIT que detém na sua carteira. Vamos fazer com que o e2 reemita 500 do ativo.

```
e2-cli reissueasset <asset-id> 500
```

Verificar o resultado da reemissão.

```
e2-cli getwalletinfo
```

Pode ver-se que o e2 detém agora o montante reemitido no saldo da sua carteira e que o próprio RIT não é consumido no processo de reemissão de activos.

Destruir uma quantidade de um ativo é algo que qualquer pessoa que detenha pelo menos a quantidade que está a ser destruída pode fazer, não é regido pelo token de reemissão.

```
e2-cli destroyamount <asset-id>
e2-cli getwalletinfo
```

Nesta secção vimos como emitir um ativo e como utilizar o token de reemissão que é opcionalmente criado como parte da emissão do ativo. Também vimos como a transferência de um token de reemissão é tão simples como a transferência de qualquer outro ativo, e que a posse de qualquer quantidade de um token de reemissão concede ao detentor o direito de emitir mais do ativo associado. Por isso, é muito importante controlar quem tem acesso aos tokens de reemissão na sua rede. Também vimos como destruir uma quantidade de um ativo e que este processo não é controlado pela posse do token de reemissão.

# Federação de Elementos

<partId>173a2440-0203-4dcc-8e2b-f8fa2cc8d3ca</partId>

## Bloquear assinatura

<chapterId>c47b217e-db14-4843-a66f-3e5f3a00a808</chapterId>

![Video](https://youtu.be/kxWX91fCnus?si=KItm_Am3_RrBcLBN)

O Elements suporta um modelo de assinatura federada que lhe permite especificar o número de membros da Federação Forte que devem assinar um bloco proposto para produzir um bloco válido.

Anteriormente, e para facilitar o exemplo, criávamos blocos utilizando o comando `generate`, que não tinha de satisfazer um requisito de assinatura múltipla para que os blocos criados fossem aceites pela rede como válidos.

Nós estaremos configurando nossos nós para requerer a criação de blocos multisig 2-de-2. Isso será configurado usando o parâmetro signblockscript, que pode ser adicionado ao arquivo de configuração ou passado para o nó na inicialização. Para inicializar uma cadeia com esse parâmetro, primeiro precisamos construir o script que a compõe.

Vamos fazer isto usando alguns nós existentes, guardar os dados que eles produzem e depois limpar a cadeia para a podermos reiniciar usando o nosso parâmetro signblockscript. Isto é necessário porque o script faz parte das regras de consenso da rede e terá de ser definido na inicialização da cadeia. Não pode ser adicionado numa data posterior a uma cadeia já existente.

Precisamos de aceder a dois nós Elements, a que chamaremos e1 e e2. Os nós tiveram as suas cadeias de blocos reiniciadas e o ativo predefinido foi dividido entre eles.

Certifique-se de que o parâmetro con_max_block_sig_size está definido para um valor elevado no seu ficheiro elements.conf, caso contrário, a assinatura em bloco falhará mais tarde nesta secção. Nós definimos con_max_block_sig_size=2000 para este tutorial.

Como vamos reiniciar a blockchain e limpar as carteiras associadas a e1 e e2, precisaremos de fazer uma cópia dos endereços, chaves públicas e chaves privadas que usamos para gerar o script de assinatura de bloco, para que possamos usá-los mais tarde.

Em primeiro lugar, precisamos que cada um dos que serão os nós de assinatura de blocos gere um novo endereço, do qual é necessário fazer uma cópia.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

Depois, temos de extrair as chaves públicas dos endereços e anotá-las para utilização posterior.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

Em seguida, extrai as chaves privadas, que reimportaremos mais tarde para que os nós possam assinar os blocos depois de reinicializarmos a nossa cadeia de blocos e os dados da carteira.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Agora precisamos de gerar um script de redeem com requisitos de assinatura múltipla 2 de 2. Fazemo-lo utilizando o comando createmultisig e passando o primeiro parâmetro como 2 e, em seguida, fornecendo duas chaves públicas. São estas chaves que a propriedade precisa de provar mais tarde, quando o bloco é criado.

Qualquer um dos nós, e1 ou e2, pode gerar o multisig.

```
e1-cli createmultisig 2 '["<e1-pubkey>", "<e2-pubkey>"]'
```

Isto dá-nos o nosso redeemscript, que pode copiar para utilizar mais tarde.

Agora precisamos de limpar a blockchain existente e os dados da carteira para podermos começar de novo com o novo signblockscript como parte das regras de consenso da cadeia. É por isso que precisamos fazer uma cópia de alguns dados anteriormente, como as chaves privadas que serão usadas na nova cadeia para assinar blocos. É necessário fazer isso antes de continuar.

Com a nossa carteira existente e os dados da cadeia eliminados, podemos agora iniciar os nossos nós e fazê-los inicializar uma nova cadeia utilizando o parâmetro signblockscript. Vamos passar -evbparams=dynafed:0::: para desativar a ativação dynafed, porque não precisamos dessa funcionalidade avançada para este exemplo.

```
e1-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
e2-dae -signblockscript=<redeem-script> -evbparams=dynafed:0:::
```

Agora, precisamos de importar as chaves privadas que guardámos anteriormente para que os nossos nós possam assinar e ajudar a completar quaisquer blocos propostos.

```
e1-cli importprivkey <e1-priv-key>
e2-cli importprivkey <e2-priv-key>
```

A utilização do comando generate deve agora apresentar um erro, uma vez que não cumpre as regras de assinatura de blocos agora impostas pelos nossos nós.

```
e1-cli -generate 1
```

Para propor um novo bloco, qualquer nó pode chamar o comando getnewblockhex. Este comando devolve o hexadecimal de um novo bloco que terá de ser assinado antes de ser aceite por qualquer nó da nossa rede.

```
e1-cli getnewblockhex
```

Lembre-se que o comando apenas cria um bloco proposto, não o gera.

Para confirmar isto, podemos ver que não existem atualmente blocos na nossa cadeia de blocos.

```
e1-cli getblockcount
```

Se tentarmos enviar o bloco hexagonal sem o assinar primeiro.

```
e1-cli submitblock <block-hex>
```

Recebemos uma mensagem que nos diz que a prova de bloco é inválida. Isto deve-se ao facto de ainda não ter sido assinado por 2 das 2 partes necessárias.

Vamos então fazer com que e1 assine o bloco proposto.

```
e1-cli signblock <block-hex>
```

O e2 deve assinar o hexágono.

```
e2-cli signblock <block-hex>
```

Repare que e2 não assina o resultado criado por e1 ao assinar o bloco proposto. Ambos assinam o bloco proposto hexadecimal, independentemente dos resultados um do outro.

Agora precisamos de combinar as assinaturas de bloco de e1 e e2. Qualquer um dos nós pode fazer isso, tudo o que precisa é do bloco hexadecimal assinado do outro nó.

```
e1-cli combineblocksigs <block-hex> '["<signed-hex-from-e1>", "<signed-hex-from-e2>"]'
```

Pode ver que o comando combineblocksigs produz o hexadecimal do bloco assinado, bem como um estado de completo, dizendo-nos que o hexadecimal do bloco está pronto para ser submetido.

Agora, qualquer um dos nós pode enviar o bloco hexagonal completo. Vamos pedir ao e1 para o fazer.

```
e1-cli submitblock <combined-signed-hex>
```

Verificar se a submissão é válida.

```
e1-cli getblockcount
e2-cli getblockcount
```

Pode ver que tanto e1 como e2 aceitaram o bloco como válido e adicionaram-no à ponta das suas cópias locais da cadeia de blocos.

Para resumir o processo. Nesta secção, temos:


- Propôs um bloco.
- Pedi a cada nó que o assinasse.
- Combinámos as assinaturas.
- Verificou se as assinaturas são válidas e se cumprem o limiar de redeemscript da cadeia.
- Apresentou o bloco.

Cada nó da rede validou o bloco e adicionou-o à sua cópia local da cadeia de blocos.

### Seleção de blocos

Embora o processo pareça inicialmente complexo, a sequência de assinatura de blocos no Elements é sempre a mesma e a configuração inicial só tem de ser efectuada uma vez:

1. Configuração inicial (efectuada uma vez)

2. É criado um endereço com várias assinaturas chamado `signblockscript` usando as chaves públicas dos Federated Block Signers.

3. O script de resgate é usado para iniciar uma nova blockchain.

4. Produção em bloco (em curso)

5. Os blocos propostos são gerados e trocados para assinatura.

Uma vez que um número limite de signatários tenha assinado o bloco proposto, ele é combinado e submetido à rede. Se ele atender aos critérios do `signblockscript` da cadeia, os nós o aceitam como um bloco válido.

## Elemento como cadeia lateral

<chapterId>432d7a65-255f-44a3-8b38-78508202cb37</chapterId>

![Video](https://youtu.be/egYzj4N8CB8?si=v7_-IXsjHPE-ARDe)

A Elements é uma plataforma de blockchain de código aberto, de uso geral, que também pode ser `pegada` a uma blockchain existente, como a Bitcoin. Quando ligada a outra blockchain, diz-se que a Elements está a funcionar como uma `sidechain`. As sidechains permitem a transferência bidirecional de activos de uma cadeia para outra. Implementar a Elements como uma sidechain permite-lhe contornar algumas das limitações inerentes à mainchain, mantendo um bom grau de segurança fornecida pelos activos assegurados na mainchain.

Enquanto uma sidechain tem conhecimento da mainchain e do seu histórico de transacções, a mainchain não tem conhecimento da sidechain e não é necessário nenhum conhecimento para o seu funcionamento. Isso permite que as sidechains inovem sem restrições ou atrasos associados às propostas de melhoria do protocolo da cadeia principal. Em vez de tentar alterá-lo diretamente, a extensão do protocolo principal permite que a própria cadeia principal permaneça segura e especializada, sustentando o bom funcionamento da cadeia lateral.

Ao estender a funcionalidade do Bitcoin e alavancar a sua segurança subjacente, uma sidechain baseada em elementos é capaz de fornecer novas funcionalidades que anteriormente não estavam disponíveis para os utilizadores da mainchain. Um exemplo de uma sidechain baseada em Elementos em uso produtivo é a Liquid Network.

Para inicializar uma blockchain da Elements como uma sidechain, precisamos usar o parâmetro de script federated peg. Este parâmetro pode ser definido no ficheiro de configuração de um nó ou passado no arranque.

O script de peg federado define quais membros da federação forte podem executar funções de peg-in e peg-out. Esses funcionários são chamados de `Watchmen`, pois observam a mainchain e a sidechain em busca de transações válidas de peg-in e peg-out e as acionam se forem válidas. "Peg-out" significa mover activos indexados da sidechain para a mainchain e "peg-in" significa mover activos indexados da mainchain para a sidechain. Quando dizemos "mover para a sidechain", o que realmente queremos dizer é que os fundos são bloqueados num endereço com várias assinaturas na mainchain e uma quantidade correspondente do ativo é criada na sidechain da Elements. Quando dizemos `move out of the sidechain` o que queremos dizer é que os activos são destruídos na sidechain da Elements e o montante correspondente é libertado dos fundos bloqueados mantidos na mainchain. A permissão para executar as funções de peg-in e peg-out requer que os funcionários provem a propriedade das chaves públicas usadas no script de peg federado. Isso é feito com o uso das chaves privadas correspondentes.

Para criar um script de peg federado, precisamos primeiro de ter cada um dos nossos nós a gerar uma chave pública. Também precisamos de armazenar as chaves privadas associadas para utilização posterior, uma vez que teremos de limpar quaisquer dados de cadeia existentes e inicializar uma nova cadeia utilizando o script de peg federado. Isto deve-se ao facto de o script de peg federado fazer parte das regras de consenso de uma sidechain e não poder ser aplicado a uma blockchain existente, sem peg, numa data posterior.

Portanto, vamos gerar um endereço com cada um dos nossos nós, armazenar os dados relevantes para uso posterior e gerar o script de peg federado que usaremos para inicializar nossa sidechain mais tarde.

Primeiro, precisamos que cada um dos nossos nós, que actuarão como vigilantes na nossa rede, gere um novo endereço.

```
e1-cli getnewaddress
e2-cli getnewaddress
```

De seguida, validamos o endereço para obter as chaves públicas.

```
e1-cli getaddressinfo <e1-address>
e2-cli getaddressinfo <e2-address>
```

E depois recupera as chaves privadas associadas a cada endereço.

```
e1-cli dumpprivkey <e1-address>
e2-cli dumpprivkey <e2-address>
```

Armazene as chaves privadas e públicas para utilização posterior.

Agora precisamos de limpar a blockchain existente e os dados da carteira, pois vamos inicializar uma nova cadeia usando um script de peg federado. Você pode fazer isso agora. Não se esqueça de iniciar o daemon do Bitcoin, que precisaremos para fazer a peg-in.

Agora podemos inicializar uma nova cadeia com um script de peg federado criado usando as chaves públicas que armazenámos anteriormente. Os números que introduzimos e que rodeiam as nossas chaves públicas definem e delimitam o número de chaves utilizadas e a propriedade da chave que tem de ser provada para podermos aceder e sair da nossa sidechain.

```
e1-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
e2-dae -fedpegscript=5221<e1-pubkey>21<e2-pubkey>52ae
```

Agora vamos importar as chaves privadas que guardámos anteriormente, para que os nossos nós possam mais tarde assinar e concluir a transferência de activos entre cadeias e satisfazer os requisitos do script de peg federado.

```
e1-cli importprivkey <priv-key-1>
e2-cli importprivkey <priv-key-1>
```

Agora precisamos de amadurecer alguns blocos em ambas as cadeias. A maturidade dos blocos é um requisito do processo de indexação, pois protege contra reorganizações de blocos na cadeia principal, levando a uma inflação do fornecimento de ativos indexados na cadeia lateral.

Para manter esta secção centrada na peg federada, vamos gerar blocos sem utilizar o modelo de assinatura de blocos que vimos na última secção, e voltar a utilizar o comando 'generate' para criar novos blocos.

```
b-cli generate 101
e1-cli generate 1
```

Neste momento, não precisamos necessariamente de gerar blocos para elementos. Mas, vamos gerar um na mesma. É uma boa prática para evitar possíveis inconsistências.

Agora a nossa cadeia está pronta para ser ligada. Para fazer peg-in, precisamos gerar um tipo especial de endereço usando o comando getpeginaddress. Note que a duração entre gerar um endereço de peg-in com getpeginaddress e reivindicá-lo com claimpegin deve ser a menor possível. endereços de peg-in não são duráveis a longo prazo e não devem ser reutilizados.

```
e1-cli getpeginaddress
```

Você pode ver que o comando cria um novo endereço na mainchain, bem como um novo script que precisará ser satisfeito para reivindicar os fundos de peg-in. O endereço da mainchain é um endereço `pay to script hash` que será usado por funcionários que desempenham o papel de Watchmen dentro da rede Elements.

Tal como getnewaddress, getpeginaddress adiciona um novo segredo à carteira do nó que o chama, por isso é importante ter em conta o backup do ficheiro da carteira no seu processo de gestão de nós.

Vamos agora enviar algum bitcoin da mainchain para a sidechain. A nossa carteira de teste de regressão da mainchain já tem alguns fundos.

```
b-cli getwalletinfo
```

Podemos ver que a carteira tem 50 bitcoin. Vamos enviar um bitcoin da mainchain para a sidechain. Precisamos de enviar fundos para o endereço da mainchain que o nosso nó gerou anteriormente.

```
b-cli sendtoaddress <e1-pegin-address>
```

Temos de guardar o ID desta transação, uma vez que precisamos dele para comprovar o financiamento mais tarde.

Podemos agora ver que o saldo da carteira mainchain diminuiu pelo montante que enviámos, mais um pequeno montante adicional para cobrir as taxas de transação.

```
b-cli getwalletinfo
```

Temos de amadurecer a transação novamente.

```
b-cli generate 101
```

Para que o nosso nó Elements reivindique os fundos de peg-in, precisamos de obter a "prova" de que a transação de peg-in foi efectuada. A prova criptográfica utiliza o ID da transação de financiamento para calcular o caminho merkel e prova que a transação está presente num bloco confirmado.

```
b-cli gettxoutproof '["<tx-id>"]'
```

Precisamos também dos dados brutos da transação.

```
b-cli getrawtransaction <tx-id>
```

Com a prova e os dados brutos da transação de peg-in, o nó dos nossos elementos pode agora reclamar a peg-in utilizando a transação bruta e a prova da transação.

```
e1-cli claimpegin <raw> <proof>
```

Note que existe um terceiro argumento opcional que poderíamos ter fornecido ao claimpegin. Este terceiro parâmetro pode ser usado para especificar o endereço da sidechain para o qual enviar os fundos reivindicados. Isso não foi necessário em nosso exemplo, pois estávamos chamando o comando do mesmo nó que possui o endereço para o qual os fundos reivindicados estão indo.

Verificar o saldo de e1.

```
e1-cli getwalletinfo
```

Geração de um bloco para confirmar o pedido.

```
e1-cli generate 1
```

Verificar o saldo de e1.

```
e1-cli getwalletinfo
```

Podemos ver que a cavilha foi reclamada com êxito.

Para o peg-out, o processo é semelhante. Um endereço é gerado, os fundos são enviados para ele e os fundos são libertados se a transação for válida. Não abordaremos todo o processo de peg-out, uma vez que este envolve trabalho na cadeia principal, o que está fora do âmbito deste curso. Os passos em termos dos eventos dos Elementos são que um endereço é gerado na cadeia principal.

```
b-cli getnewaddress
```

Os fundos são enviados para o endereço da mainchain a partir de um nó da Elements usando o comando sendtomainchain.

```
e1-cli sendtomainchain <new-address> 1
```

Geração de um bloco para confirmar a transação.

```
e1-cli generate 1
```

Verificar o saldo da carteira do nó.

```
e1-cli getwalletinfo
```

E ver que o saldo diminuiu.

Nesta secção, vimos como fazer:


- Gerar um script de peg federado.
- Inicializa uma nova cadeia que utiliza o script como uma regra de parâmetro de consenso de rede.
- Enviar fundos da cadeia principal para a cadeia lateral.
- Reclamar os fundos na sidechain da Elements.
- Entenda como o envio de fundos de volta para a cadeia principal é iniciado.

### FederatedPegScript

Para permitir que o Elements funcione como uma sidechain, o bloco genesis em sua blockchain deve ser criado com um `fedpegscript` no lugar. Isto é feito passando o parâmetro `fedpegscript` no início do nó. O script fará então parte das regras de consenso da blockchain do Elements e permitirá que os pedidos de peg-in e peg-out sejam validados e acionados.

O `fedpegscript` é composto por chaves públicas controladas pelas pessoas autorizadas a realizar as acções de peg. A seguir é apresentado um exemplo de formato de um fedpegscript 2-of-2 multisignature:

```
fedpegscript=5221<public key 1>21<public key 2>52ae
```

Nota: Os caracteres fora das chaves públicas são delimitadores que indicam a chave pública e os requisitos `n de m`. Por exemplo, o modelo para um fedpegscript 1-de-1 seria '5121<pub key 1>51ae'.

### Peg-in

Antes de um peg-in poder ser aceite por uma sidechain da Elements, deve ter confirmações suficientes na mainchain. Isto é necessário para evitar a inflação no fornecimento do ativo indexado na sidechain da Elements, que poderia ser causada por uma reorganização da mainchain.

Pequenas reorganizações da ponta do blockchain do Bitcoin são esperadas como parte da operação normal do mecanismo de consenso de Prova de Trabalho (PoW). Como tal, a Elements apenas aceita que um peg-in seja válido quando tem profundidade suficiente dentro da blockchain da Bitcoin. Isto serve para evitar que a Elements aceite o mesmo peg-in mais do que uma vez.

### Peg-Out

Uma peg-out ocorre quando um nó da Elements chama o comando `sendtomainchain`, que recebe como entrada um endereço da mainchain (o destino da peg-out), bem como o montante do ativo indexado a ser "retirado". Isso cria uma transação de peg-out na sidechain. Assim que os Funcionários que estão a atuar como Vigilantes detectam que a transação de peg-out foi confirmada na sidechain, tratam de libertar o ativo na mainchain para o destino da peg-out, como aprendemos nas secções anteriores do curso.

## Elementos como uma cadeia de blocos autónoma

<chapterId>50dff39b-2702-47d7-9c15-0b54b845e99f</chapterId>

![Video](https://youtu.be/u-3rV7DGtD0?si=G1__H0Uelf4sTUDM)

Até agora, vimos como executar o Elements como uma sidechain. No entanto, ele também pode operar como uma solução de blockchain independente com seu próprio ativo nativo padrão. Nesta configuração, uma blockchain da Elements ainda mantém todas as caraterísticas de uma implementação de sidechain, tais como Transacções Confidenciais e Activos Emitidos, mas não necessita de peg-in ou peg-out para adicionar ou remover montantes de activos predefinidos de circulação.

Nesta secção, iremos:

Inicializa uma nova blockchain Elements com um ativo predefinido chamado `newasset`.

Especifique 1.000.000 `newasset` a ser criado juntamente com 2 tokens de reemissão para ele.

Reclama todas as moedas `newasset` que qualquer pessoa pode gastar.

Reivindicar todos os tokens de reemissão que qualquer pessoa pode gastar para "newasset".

Enviar o ativo e o seu token de reemissão para a carteira de outro nó.

Reemitir mais "newasset" de ambos os nós.

Para inicializar uma rede Elements para operar como uma blockchain autónoma, cada nó precisa de ser iniciado com alguns parâmetros básicos. Estes são utilizados para dizer ao nó para não tentar validar peg-ins de outra blockchain, o nome do ativo predefinido da rede e a quantidade do ativo predefinido e do token de reemissão associado a criar.

Vamos iniciar uma nova cadeia usando esses parâmetros em nossos dois nós Elements conectados agora. Vamos nomear o ativo por defeito `newasset` e emitir um milhão deles e dois tokens de reemissão `newasset`.

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
e2-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

Note-se que os montantes aqui utilizados estão na denominação mais pequena que a rede pode aceitar, pelo que os duzentos milhões de tokens de reemissão equivalem efetivamente a dois tokens inteiros. O mesmo se aplica à denominação das moedas gratuitas iniciais.

Verificar os saldos actuais das carteiras dos nossos nós.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Podemos ver que a inicialização funcionou corretamente.

Como a emissão inicial de activos é criada como "qualquer pessoa pode gastar", pediremos a e1 que os reclame a todos para que possamos retirar o acesso de e2 a eles.

```
e1-cli getnewaddress
e1-cli sendtoaddress <e1-address> 1000000 "" "" true
```

Note-se que não é necessário especificar "newasset" como o ativo a enviar, uma vez que este já é o ativo por defeito e, por conseguinte, também o ativo por defeito utilizado para pagar as taxas de rede.

No Elements, é possível enviar vários tipos de activos para o mesmo endereço, pelo que podemos reutilizar o endereço que acabámos de gerar para receber o ativo predefinido e utilizá-lo como endereço de destino para os tokens de reemissão.

```
e1-cli sendtoaddress <e1-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confirmar as transacções.

```
e1-cli generate 101
```

Vamos verificar se e1 é o único detentor do ativo e do seu token de reemissão.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

O que podemos ver que é efetivamente o caso.

Agora vamos enviar parte do "newasset" para e2, que atualmente tem um saldo de zero.

```
e2-cli getnewaddress
e1-cli sendtoaddress <e2-address> 500 "" "" false
```

Note-se que não foi necessário especificar o tipo de ativo a enviar, uma vez que o `newasset` foi criado como ativo predefinido da rede

Vamos também enviar alguns dos tokens de reemissão do `newasset` para o e2.

```
e1-cli sendtoaddress <e2-address> 1 "" "" false false 1 UNSET false <reissuance-token-id>
```

Confirmar as transacções.

```
e1-cli generate 101
```

Podemos verificar se as carteiras foram actualizadas em conformidade.

```
e1-cli getwalletinfo
e2-cli getwalletinfo
```

Agora vamos reemitir alguns dos activos predefinidos de e1. Note que a capacidade de fazer isto é activada pelo parâmetro de arranque initialreissuancetokens. Que, se for omitido ou definido como zero, resultará num ativo predefinido que não pode ser reemitido numa data posterior.

```
e1-cli reissueasset newasset 100
```

Conseguimos utilizar o rótulo de `newasset` em vez de termos de fornecer o valor hexadecimal do id porque uma cadeia de elementos rotula sempre o seu ativo predefinido.

Verificar se a reemissão do ativo por defeito funcionou:

```
e1-cli generate 101
e1-cli getwalletinfo
```

Vamos agora provar que, como e2 detém alguns dos tokens de reemissão `newasset`, também pode reemitir o ativo por defeito.

```
e2-cli reissueasset newasset 100
```

Verificar se a reemissão do ativo por defeito pela e2 funcionou.

```
e2-cli generate 101
e2-cli getwalletinfo
```

Nesta secção, configurámos o Elements como uma blockchain autónoma e verificámos que a funcionalidade básica funciona como seria de esperar.

Utilizámos parâmetros de arranque para:

Inicializa uma nova blockchain da Elements com um ativo predefinido denominado 'newasset'.

Especifique a quantidade do ativo predefinido a criar na inicialização da cadeia.

Criar alguns tokens de reemissão para o ativo predefinido e reemitir mais do ativo predefinido de ambos os nós.

Na nossa rede autónoma blockchain Elements, todas as outras operações transaccionais funcionarão da mesma forma que os exemplos abordados nas secções principais do curso, mas utilizarão 'newasset' em vez de `bitcoin` como o ativo padrão e de taxa.

### Parâmetros de arranque do nó e de inicialização da cadeia

Para dizer a um nó Elements para operar como uma blockchain autónoma, alguns parâmetros devem ser utilizados em conjunto. Vamos dar uma vista de olhos em cada um deles e descobrir o que fazem.

#### `validatepegin=0`

Como uma blockchain autónoma não precisa de validar quaisquer transacções de peg-in ou peg-out, precisamos de desativar essas verificações. Com esta configuração, não é necessário executar o software cliente Bitcoin ou armazenar uma cópia do blockchain Bitcoin, pois a rede Elements funcionará de forma independente.

#### `defaultpeggedassetname`

Isto permite-lhe especificar o nome do ativo predefinido criado na inicialização da cadeia de blocos.

#### `initialfreecoins`

O número (no equivalente à unidade Satoshi da Bitcoin) do ativo predefinido a criar.

#### "Tokens de emissão inicial

O número (no equivalente à unidade Satoshi da Bitcoin) de tokens de reemissão para o ativo por defeito a criar. Sem isso, seria impossível criar mais do ativo padrão. Se não quiser que seja possível criar mais do ativo predefinido, isto pode ser definido como zero ou omitido.

Utilizando estes parâmetros, o comum para iniciar um nó seria algo como isto:

```
e1-dae -validatepegin=0 -defaultpeggedassetname=newasset -initialfreecoins=100000000000000 -initialreissuancetokens=200000000
```

### Operações básicas

O parâmetro `defaultpeggedassetname` aplica uma etiqueta ao ativo por defeito. Sem esta configuração, o asset padrão será automaticamente nomeado `bitcoin`. Nas secções anteriores, quando enviamos activos que nós próprios emitimos para outro nó, tivemos de especificar o hexadecimal do ativo ou a etiqueta do ativo aplicada localmente para dizer ao Elements qual o ativo que estávamos a enviar. Como o `defaultpeggedassetname` se aplica a todos os nós, não precisamos de o nomear quando o enviamos, mesmo que o seu nome não seja `bitcoin`. Todas as funções que antes enviavam `bitcoin` por defeito, irão agora enviar o que quer que tenha escolhido para rotular o ativo por defeito.

Assim, enviar 10 do novo ativo predefinido para um endereço é tão simples como:

```
e1-cli sendtoaddress <destination address> 10 "" "" true
```

Se você também forneceu ao nó um valor para `initialreissuancetokens` maior que zero, então você também será capaz de reemitir mais do ativo padrão, algo que não é possível se você executar o Elements como uma sidechain.

Para tal, qualquer nó que detenha um montante do token associado ao ativo predefinido só precisa de emitir um comando no formulário:

```
e1-cli reissueasset <default asset name> <amount>
```

Utilizando os parâmetros acima, pode operar a Elements como uma blockchain autónoma com o seu próprio ativo predefinido, dissociada da Bitcoin e de outras blockchains.

## Conclusão

<chapterId>7e2c916d-8114-424c-97f5-cbff9d73b8e3</chapterId>

![Video](https://youtu.be/CTMdamTZBBM?si=16LBcXvN4pBfC7lr)

Neste curso, aprendemos que o Elements é um protocolo de rede de código aberto que pode ser implementado como uma sidechain para outra blockchain, ou como uma solução de blockchain autónoma.

Vimos que o código-fonte e o site da Elements (https://github.com/ElementsProject/elements) estão hospedados no GitHub e que existem fóruns de discussão da comunidade, como o Build On L2(https://community.liquid.net/c/developers/), ou o Liquid Developers Telegram (https://t.me/liquid_devel), que podem ser usados para aprender mais sobre a implantação e o desenvolvimento de aplicativos na Elements e na Liquid. Os principais recursos, como Transações Confidenciais e Ativos Emitidos, foram abordados, juntamente com a forma como os membros de uma Federação Forte permitem a assinatura de blocos federados e o mecanismo 2-Way Peg.

O próximo passo é desafiar-se a si próprio com um questionário cumulativo que abrange todas as secções anteriores e, em seguida, iniciar a sua viagem de Elementos... boa sorte!

# Conclusão

<partId>d5dbd616-e291-42bc-aae3-6c44599dbd06</partId>

## Comentários e classificações

<chapterId>beae23bd-2fd1-49fe-8f38-ed169acde51d</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusão

<chapterId>15f62056-c69c-467e-9565-af48d439a1f5</chapterId>

Parabéns por ter concluído este curso!

Estamos muito satisfeitos por ter alcançado com sucesso este marco na sua jornada de aprendizagem. Através da sua dedicação e empenho, adquiriu conhecimentos e competências valiosos que lhe serão úteis no seu desenvolvimento profissional.